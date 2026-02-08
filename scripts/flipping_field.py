"""
Precompute Stoner-Wohlfarth flipping data and generate a self-contained
HTML file using Plotly.js (loaded from CDN).

Hardcoded: q=1.5 prolate spheroid, magnetite (Ms=480 kA/m),
phi=0, theta_init=180, B range 0-100 mT in 1 mT steps.

Features:
  - SVG setup illustration showing grain geometry, M and B arrows
  - Derivative legend on lower panel only
  - Monotonic slider (forward-only; Reset to go back)
"""

import numpy as np
import json
import os

# --- Constants ---
mu0 = 4 * np.pi * 1e-7
Ms = 480e3
q = 1.5

e = np.sqrt(1.0 - 1.0 / q**2)
N_a = (1.0 - e**2) / (2.0 * e**3) * (np.log((1.0 + e) / (1.0 - e)) - 2.0 * e)
N_b = (1.0 - N_a) / 2.0
K_u = 0.5 * mu0 * (N_b - N_a) * Ms**2

phi_deg = 0.0
phi = np.deg2rad(phi_deg)
theta_init_deg = 180.0
track_window_deg = 30.0

theta_step_deg = 0.05
theta_deg_full = np.arange(0.0, 180.0 + theta_step_deg, theta_step_deg)
theta_full = np.deg2rad(theta_deg_full)

b_values_mT = np.arange(0, 101, 1.0)

def eps_a(th):
    return K_u * np.sin(th) ** 2

def eps_m(th, b_T):
    return -Ms * b_T * np.cos(phi - th)

def eps_t(th, b_T):
    return eps_a(th) + eps_m(th, b_T)

def deps_dtheta(th, b_T):
    return 2.0 * K_u * np.sin(th) * np.cos(th) - Ms * b_T * np.sin(phi - th)

def d2eps_dtheta2(th, b_T):
    return 2.0 * K_u * np.cos(2.0 * th) + Ms * b_T * np.cos(phi - th)

def find_stable_stationary_near(center_deg, window_deg, b_T):
    d1 = deps_dtheta(theta_full, b_T)
    d2 = d2eps_dtheta2(theta_full, b_T)
    mask = (theta_deg_full >= center_deg - window_deg) & (theta_deg_full <= center_deg + window_deg)
    idx = np.where(mask)[0]
    if idx.size < 2:
        return None
    candidates = []
    for i_end in (0, len(theta_deg_full) - 1):
        if (theta_deg_full[i_end] >= center_deg - window_deg) and (theta_deg_full[i_end] <= center_deg + window_deg):
            if np.isfinite(d1[i_end]) and np.isfinite(d2[i_end]):
                if (np.abs(d1[i_end]) < 1e-6 * K_u) and (d2[i_end] > 0):
                    candidates.append(i_end)
    d1_sub = d1[idx]
    finite = np.isfinite(d1_sub)
    idx_f = idx[finite]
    if idx_f.size >= 2:
        d1_f = d1[idx_f]
        s = np.sign(d1_f)
        sc = np.where(s[:-1] * s[1:] < 0)[0]
        for k in sc:
            i0 = idx_f[k]
            i1 = idx_f[k + 1]
            denom = d1[i0] - d1[i1]
            if np.abs(denom) < 1e-30:
                continue
            t = d1[i0] / denom
            th_root = theta_full[i0] + t * (theta_full[i1] - theta_full[i0])
            i_root = int(np.argmin(np.abs(theta_full - th_root)))
            if (theta_deg_full[i_root] >= center_deg - window_deg) and (theta_deg_full[i_root] <= center_deg + window_deg):
                if np.isfinite(d2[i_root]) and (d2[i_root] > 0):
                    candidates.append(i_root)
    if not candidates:
        return None
    candidates = sorted(set(candidates))
    return int(min(candidates, key=lambda i: abs(theta_deg_full[i] - center_deg)))

# Downsample for plotting
step = 10
th_plot_deg = theta_deg_full[::step]
th_plot = theta_full[::step]

# Precompute all frames
frames = []
state_theta = theta_init_deg
state_flipped = False
flip_field = None

for b_mT in b_values_mT:
    b_T = b_mT * 1e-3
    i_occ = find_stable_stationary_near(state_theta, track_window_deg, b_T)
    if i_occ is None:
        et_full = eps_t(theta_full, b_T)
        i_global = int(np.argmin(et_full))
        state_theta = float(theta_deg_full[i_global])
        if not state_flipped:
            flip_field = float(b_mT)
        state_flipped = True
    else:
        state_theta = float(theta_deg_full[i_occ])

    ea = eps_a(th_plot)
    em = eps_m(th_plot, b_T)
    et = ea + em
    d1 = deps_dtheta(th_plot, b_T) / K_u
    d2 = d2eps_dtheta2(th_plot, b_T) / K_u
    i_glob_ds = int(np.argmin(et))
    i_occ_ds = int(np.argmin(np.abs(th_plot_deg - state_theta)))

    frames.append({
        'b': float(b_mT),
        'ea': [round(float(v), 2) for v in ea],
        'em': [round(float(v), 2) for v in em],
        'et': [round(float(v), 2) for v in et],
        'd1': [round(float(v), 4) for v in d1],
        'd2': [round(float(v), 4) for v in d2],
        'ig': i_glob_ds,
        'io': i_occ_ds,
        'to': round(state_theta, 2),
        'f': state_flipped,
    })

print(f"K_u = {K_u:.1f} J/m3")
print(f"Flip at B = {flip_field} mT")
print(f"Frames: {len(frames)}, points per frame: {len(th_plot_deg)}")

data_json = json.dumps({
    'theta': [round(float(v), 2) for v in th_plot_deg],
    'frames': frames,
    'K_u': round(K_u, 1),
    'Ms_kAm': round(Ms / 1e3, 0),
    'q': q,
    'phi_deg': phi_deg,
}, separators=(',', ':'))

print(f"JSON size: {len(data_json) / 1e3:.0f} KB")

html_template = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Stoner-Wohlfarth Magnetization Reversal</title>
<script src="https://cdn.plot.ly/plotly-2.35.2.min.js"></script>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,opsz,wght@0,8..60,300;0,8..60,400;0,8..60,600;1,8..60,400&family=JetBrains+Mono:wght@400&display=swap');

  *{box-sizing:border-box;margin:0;padding:0}
  body{
    font-family:'Source Serif 4',Georgia,serif;
    background:#f8f7f4;
    color:#1e293b;
    padding:20px 20px 40px;
    min-height:100vh;
  }
  .container{max-width:620px;margin:0 auto}

  h1{
    font-size:1.45rem;font-weight:600;
    letter-spacing:-0.01em;
    margin-bottom:2px;
    color:#0f172a;
  }
  .subtitle{
    font-size:0.86rem;color:#64748b;
    margin-bottom:16px;line-height:1.5;
  }
  .subtitle span{
    font-family:'JetBrains Mono',monospace;
    font-size:0.8rem;
    background:#ece9e3;
    padding:1px 5px;border-radius:3px;
  }

  /* Setup illustration */
  .setup-row{
    display:flex;align-items:flex-start;gap:16px;
    margin-bottom:14px;
  }
  .setup-diagram{
    flex:0 0 auto;
    background:#fff;
    border:1px solid #d6d3cd;
    border-radius:8px;
    padding:0;
    box-shadow:0 1px 3px rgba(0,0,0,0.04);
    overflow:hidden;
  }
  .setup-caption{
    flex:1;
    font-size:0.84rem;
    color:#475569;
    line-height:1.55;
    padding-top:6px;
  }
  .setup-caption b{color:#1e293b}

  .controls{
    display:flex;align-items:center;gap:12px;
    flex-wrap:wrap;
    margin-bottom:12px;
    padding:10px 14px;
    background:#fff;
    border:1px solid #d6d3cd;
    border-radius:8px;
    box-shadow:0 1px 3px rgba(0,0,0,0.04);
  }
  .controls label{font-size:0.9rem;font-weight:600;white-space:nowrap}
  .slider-wrap{flex:1;min-width:180px;display:flex;align-items:center;gap:10px}
  .slider-wrap input[type=range]{
    flex:1;height:6px;-webkit-appearance:none;appearance:none;
    background:#d6d3cd;border-radius:3px;outline:none;cursor:pointer;
  }
  .slider-wrap input[type=range]::-webkit-slider-thumb{
    -webkit-appearance:none;width:18px;height:18px;
    background:#b91c1c;border:2px solid #fff;border-radius:50%;
    box-shadow:0 1px 4px rgba(0,0,0,0.25);cursor:pointer;
  }
  .slider-wrap input[type=range]::-moz-range-thumb{
    width:18px;height:18px;
    background:#b91c1c;border:2px solid #fff;border-radius:50%;
    box-shadow:0 1px 4px rgba(0,0,0,0.25);cursor:pointer;
  }
  .b-val{
    font-family:'JetBrains Mono',monospace;
    font-size:1.05rem;font-weight:600;
    min-width:72px;text-align:right;
    color:#b91c1c;
  }
  .btn{
    font-family:inherit;font-size:0.82rem;font-weight:600;
    padding:5px 12px;border:1px solid #d6d3cd;border-radius:5px;
    background:#fff;color:#1e293b;cursor:pointer;
    transition:background 0.15s,border-color 0.15s;
    white-space:nowrap;
  }
  .btn:hover{background:#f1f0ec;border-color:#94a3b8}
  .btn.active{background:#b91c1c;color:#fff;border-color:#b91c1c}

  .status{
    font-size:0.86rem;line-height:1.6;
    padding:7px 14px;
    margin-bottom:10px;
    background:#fff;
    border:1px solid #d6d3cd;
    border-radius:8px;
  }
  .status .lbl{font-weight:600}
  .status .flipped{color:#b91c1c;font-weight:600}
  .status .tracking{color:#16a34a;font-weight:600}
  .status .note{font-size:0.8rem;color:#94a3b8;font-style:italic}

  #plot{
    background:#fff;
    border:1px solid #d6d3cd;
    border-radius:8px;
    box-shadow:0 1px 3px rgba(0,0,0,0.04);
    overflow:hidden;
  }
</style>
</head>
<body>
<div class="container">
  <!-- Setup illustration -->
  <div class="setup-row">
    <div class="setup-diagram">
      <svg width="230" height="100" viewBox="0 0 320 100" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <marker id="arrowM" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
            <path d="M0,0 L8,3 L0,6 Z" fill="#b91c1c"/>
          </marker>
          <marker id="arrowB" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
            <path d="M0,0 L8,3 L0,6 Z" fill="#2563eb"/>
          </marker>
          <marker id="arrowAx" markerWidth="6" markerHeight="5" refX="5" refY="2.5" orient="auto">
            <path d="M0,0 L6,2.5 L0,5 Z" fill="#94a3b8"/>
          </marker>
        </defs>

        <!-- Easy axis dashed line -->
        <line x1="40" y1="50" x2="260" y2="50" stroke="#94a3b8" stroke-width="1" stroke-dasharray="5,4"/>

        <!-- Grain (prolate ellipse, q=1.5) -->
        <ellipse cx="160" cy="50" rx="72" ry="48" fill="#fef3c7" stroke="#d97706" stroke-width="1.8" opacity="0.85"/>

        <!-- Easy axis label -->
        <text x="238" y="64" font-family="Source Serif 4,Georgia,serif" font-size="16" fill="#94a3b8" font-style="italic">easy axis</text>

        <!-- M arrow: points RIGHT (theta=180 means M is antiparallel to easy axis direction used as 0) -->
        <line x1="118" y1="50" x2="198" y2="50" stroke="#b91c1c" stroke-width="2.8" marker-end="url(#arrowM)"/>
        <text x="200" y="44" font-family="Source Serif 4,Georgia,serif" font-size="22" fill="#b91c1c" font-weight="600" font-style="italic">M</text>
        <text x="170" y="68" font-family="Source Serif 4,Georgia,serif" font-size="16" fill="#b91c1c">&theta; = 180&deg;</text>

        <!-- B arrow: points LEFT (phi=0, applied opposite to M) -->
        <line x1="118" y1="28" x2="52" y2="28" stroke="#2563eb" stroke-width="2.8" marker-end="url(#arrowB)"/>
        <text x="120" y="25" font-family="Source Serif 4,Georgia,serif" font-size="22" fill="#2563eb" font-weight="600" font-style="italic">B</text>
        <text x="60" y="18" font-family="Source Serif 4,Georgia,serif" font-size="16" fill="#2563eb">&phi; = 0&deg;</text>
      </svg>
    </div>
    <div class="setup-caption">
      The magnetization <b style="color:#b91c1c">M</b> starts
      antiparallel to the applied field <b style="color:#2563eb">B</b> along the easy axis
      (&theta;&nbsp;=&nbsp;180&deg;). As B increases, M is trapped in a local energy minimum (LEM)
      until the energy barrier vanishes and M flips to align with B. 
      <em style="color:#94a3b8;font-size:0.8rem">Slider is forward-only to preserve path dependence. Use Reset to restart.</em>
    </div>
  </div>

  <div class="controls">
    <label>B&nbsp;(mT):</label>
    <div class="slider-wrap">
      <input type="range" id="bSlider" min="0" max="100" value="0" step="1">
      <div class="b-val" id="bVal">0 mT</div>
    </div>
    <button class="btn" id="btnPlay">&#9654; Play</button>
    <button class="btn" id="btnReset">Reset</button>
  </div>

  <div class="status" id="status">
    <span class="lbl">State:</span> &theta; &asymp; 180.00&deg; &middot; <span class="tracking">tracking LEM</span>
  </div>

  <div id="plot"></div>
</div>

<script>
const DATA = %%DATA%%;
const theta = DATA.theta;
const frames = DATA.frames;

const C = {
  ea:'#b91c1c', em:'#2563eb', et:'#1e293b',
  d1:'#1e293b', d2:'#94a3b8',
  glob:'#0f172a', occ:'#b91c1c', grid:'#e8e6e1', ax:'#334155',
};

const init = frames[0];
const ff = 'Source Serif 4, Georgia, serif';

// --- Traces ---
// Top panel: indices 0-4 (energy traces + markers) — showlegend on top
// Bottom panel: indices 5-8 (derivatives) — showlegend on bottom
const traces = [
  // 0: ea (top)
  {x:theta,y:init.ea,mode:'lines',name:'\u03B5\u2090 (anisotropy)   ',
   line:{color:C.ea,width:2.5},xaxis:'x',yaxis:'y',
   showlegend:true},
  // 1: em (top)
  {x:theta,y:init.em,mode:'lines',name:'\u03B5\u2098 (Zeeman)',
   line:{color:C.em,width:2.5,dash:'dash'},xaxis:'x',yaxis:'y',
   showlegend:true},
  // 2: et (top)
  {x:theta,y:init.et,mode:'lines',name:'\u03B5\u209C (total)',
   line:{color:C.et,width:3.5},xaxis:'x',yaxis:'y',
   showlegend:true},
  // 3: global marker (top)
  {x:[theta[init.ig]],y:[init.et[init.ig]],mode:'markers',name:'Global min',
   marker:{size:11,color:'rgba(0,0,0,0)',line:{color:C.glob,width:2}},
   xaxis:'x',yaxis:'y',
   showlegend:false},
  // 4: occupied marker (top)
  {x:[theta[init.io]],y:[init.et[init.io]],mode:'markers',name:'Occupied LEM',
   marker:{size:15,color:'rgba(0,0,0,0)',line:{color:C.occ,width:2.5},symbol:'circle'},
   xaxis:'x',yaxis:'y',
   showlegend:false},
  // 5: d1 (bottom)
  {x:theta,y:init.d1,mode:'lines',name:'d\u03B5\u209C/d\u03B8',
   line:{color:C.d1,width:2.5},xaxis:'x2',yaxis:'y2',
   legend:'legend2',showlegend:true},
  // 6: d2 (bottom)
  {x:theta,y:init.d2,mode:'lines',name:'d\u00B2\u03B5\u209C/d\u03B8\u00B2   ',
   line:{color:C.d2,width:2.5,dash:'dash'},xaxis:'x2',yaxis:'y2',
   legend:'legend2',showlegend:true},
  // 7: zero line (bottom, no legend)
  {x:[0,180],y:[0,0],mode:'lines',showlegend:false,
   line:{color:'#94a3b8',width:1},xaxis:'x2',yaxis:'y2'},
  // 8: vertical at occupied (bottom, no legend)
  {x:[init.to,init.to],y:[-5,5],mode:'lines',showlegend:false,
   line:{color:C.occ,width:1.5,dash:'dot'},xaxis:'x2',yaxis:'y2'},
];

const axC = {
  range:[0,180],dtick:20,
  showgrid:true,gridcolor:C.grid,gridwidth:1,
  zeroline:false,linecolor:C.ax,linewidth:1.5,mirror:true,
  ticks:'inside',ticklen:5,
  tickfont:{family:ff,size:11},
};

const layout = {
  width:600,height:440,
  margin:{l:68,r:24,t:10,b:50},
  paper_bgcolor:'transparent',
  plot_bgcolor:'#fff',
  font:{family:ff,size:12,color:'#1e293b'},

  xaxis:{...axC,domain:[0,1],anchor:'y',showticklabels:false},
  yaxis:{
    title:{text:'Energy density (J/m\u00B3)',font:{size:13}},
    domain:[0.50,1],anchor:'x',
    showgrid:true,gridcolor:C.grid,
    zeroline:false,linecolor:C.ax,linewidth:1.5,mirror:true,
    ticks:'inside',ticklen:5,
    tickfont:{family:ff,size:11},
  },

  xaxis2:{...axC,domain:[0,1],anchor:'y2',
    title:{text:'\u03B8 (degrees)',font:{size:13}}},
  yaxis2:{
    title:{text:'Normalized derivatives',font:{size:13}},
    domain:[0,0.40],anchor:'x2',
    showgrid:true,gridcolor:C.grid,
    zeroline:false,linecolor:C.ax,linewidth:1.5,mirror:true,
    ticks:'inside',ticklen:5,
    tickfont:{family:ff,size:11},
  },

  /* Energy legend on top panel */
  legend:{
    bgcolor:'rgba(255,255,255,0.92)',
    bordercolor:'#d6d3cd',borderwidth:1,
    font:{size:11},
    x:0.02,y:0.99,xanchor:'left',yanchor:'top',
    borderpad:14,
  },
  /* Derivative legend on bottom panel */
  legend2:{
    bgcolor:'rgba(255,255,255,0.92)',
    bordercolor:'#d6d3cd',borderwidth:1,
    font:{size:11},
    x:0.02,y:0.40,xanchor:'left',yanchor:'top',
    borderpad:14,
  },

  hovermode:'x unified',

  annotations:[
    {x:theta[init.ig],y:init.et[init.ig],xref:'x',yref:'y',
     text:'global<br>min',showarrow:false,xanchor:'left',xshift:10,
     font:{size:10,color:C.glob,family:ff},
     bgcolor:'rgba(255,255,255,0.85)',borderpad:2},
    {x:theta[init.io],y:init.et[init.io],xref:'x',yref:'y',
     text:'occupied<br>LEM',showarrow:false,xanchor:'right',xshift:-10,
     font:{size:10,color:C.occ,family:ff},
     bgcolor:'rgba(255,255,255,0.85)',borderpad:2},
  ],
};

Plotly.newPlot('plot',traces,layout,{displayModeBar:false,responsive:true});

// --- Interactivity ---
const slider = document.getElementById('bSlider');
const bValEl = document.getElementById('bVal');
const statusEl = document.getElementById('status');
const btnPlay = document.getElementById('btnPlay');
const btnReset = document.getElementById('btnReset');

// Track the max B reached (monotonic forward only)
let maxReached = 0;

function updateToFrame(idx) {
  const f = frames[idx];
  const occText = f.f ? 'flipped<br>here' : 'occupied<br>LEM';

  Plotly.update('plot', {
    y:[f.ea, f.em, f.et,
       [f.et[f.ig]], [f.et[f.io]],
       f.d1, f.d2, [0,0], [-5,5]],
    x:[theta, theta, theta,
       [theta[f.ig]], [theta[f.io]],
       theta, theta, [0,180], [f.to,f.to]],
  }, {
    annotations:[
      {x:theta[f.ig],y:f.et[f.ig],xref:'x',yref:'y',
       text:'global<br>min',showarrow:false,xanchor:'left',xshift:10,
       font:{size:10,color:C.glob,family:ff},
       bgcolor:'rgba(255,255,255,0.85)',borderpad:2},
      {x:theta[f.io],y:f.et[f.io],xref:'x',yref:'y',
       text:occText,showarrow:false,xanchor:'right',xshift:-10,
       font:{size:10,color:C.occ,family:ff},
       bgcolor:'rgba(255,255,255,0.85)',borderpad:2},
    ],
  }, [0,1,2,3,4,5,6,7,8]);

  bValEl.textContent = f.b.toFixed(0) + ' mT';
  slider.value = idx;

  if (f.f) {
    statusEl.innerHTML = '<span class="lbl">State:</span> \u03B8 \u2248 ' +
      f.to.toFixed(2) + '\u00B0 \u00B7 <span class="flipped">FLIPPED at B = ' +
      f.b.toFixed(0) + ' mT</span>';
  } else {
    statusEl.innerHTML = '<span class="lbl">State:</span> \u03B8 \u2248 ' +
      f.to.toFixed(2) + '\u00B0 \u00B7 <span class="tracking">tracking LEM</span>';
  }
}

// Monotonic slider: only allow forward movement
slider.addEventListener('input', function() {
  let requested = parseInt(this.value);
  if (requested < maxReached) {
    // Snap back to maxReached — don't allow backward
    this.value = maxReached;
    return;
  }
  maxReached = requested;
  updateToFrame(requested);
});

let playing = false, playTimer = null;

function stopPlay() {
  playing = false;
  clearInterval(playTimer);
  btnPlay.innerHTML = '&#9654; Play';
  btnPlay.classList.remove('active');
}

btnPlay.addEventListener('click', function() {
  if (playing) { stopPlay(); return; }
  playing = true;
  btnPlay.innerHTML = '&#9646;&#9646; Pause';
  btnPlay.classList.add('active');
  let idx = maxReached;
  playTimer = setInterval(function() {
    idx++;
    if (idx >= frames.length) { stopPlay(); return; }
    maxReached = idx;
    updateToFrame(idx);
  }, 100);
});

btnReset.addEventListener('click', function() {
  stopPlay();
  maxReached = 0;
  updateToFrame(0);
});
</script>
</body>
</html>"""

html_out = html_template
html_out = html_out.replace('%%DATA%%', data_json)
html_out = html_out.replace('%%Q%%', str(q))
html_out = html_out.replace('%%MS%%', str(int(Ms/1e3)))
html_out = html_out.replace('%%PHI%%', str(int(phi_deg)))
html_out = html_out.replace('%%KU%%', str(round(K_u, 1)))

output_path = '../book/figures/chapter5/flipping_field_widget.html'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, 'w') as f:
    f.write(html_out)

sz = os.path.getsize(output_path)
print(f"Written to {output_path}")
print(f"File size: {sz / 1e3:.0f} KB")
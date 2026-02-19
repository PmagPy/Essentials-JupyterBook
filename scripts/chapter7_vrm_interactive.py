"""
Precompute VRM acquisition data and generate a self-contained
HTML file using Plotly.js (loaded from CDN).

Shows how a grain population progressively acquires a viscous remanent
magnetization (VRM) as the blocking boundary sweeps through V-K space.

Style matches flipping_field.py (Source Serif 4, control bar, etc.);
line/fill colors preserved from original VRM simulation.
"""

import numpy as np
import json
import os

# --- Physics & Constants ---
k_B = 1.380649e-23
tau_0 = 1e-9
T_room = 300  # K

# Grain population ellipse in V-K space
center_x, center_y = 1.3, 0.19  # kJ/m³, zm³
ellipse_width, ellipse_height = 1.6, 0.30

# Reference tau lines (label, tau in seconds, color)
taus_ref = [
    ('100 s', 100, '#0072B2'),
    ('1 Myr', 1e6 * 3.15e7, '#E69F00'),
    ('4.5 Gyr', 4.5e9 * 3.15e7, '#D55E00'),
]

K_axis_kJ = np.linspace(0.01, 5.0, 300)
K_axis_J = K_axis_kJ * 1000


def calculate_v_curve(tau, T, K_array_J):
    """V(K) for a given relaxation time tau at temperature T."""
    K_safe = np.maximum(K_array_J, 1e-5)
    v_m3 = (k_B * T * np.log(tau / tau_0)) / K_safe
    return v_m3 * 1e21  # zm³


# --- Time steps with human-readable labels ---
time_steps = [
    (1, "1 s"), (3, "3 s"), (10, "10 s"), (30, "30 s"), (100, "100 s"),
    (300, "5 min"), (600, "10 min"), (1800, "30 min"), (3600, "1 hr"),
    (36000, "10 hr"), (86400, "1 day"), (604800, "1 week"),
    (2.628e6, "1 month"), (7.884e6, "3 months"),
    (3.15e7, "1 yr"), (1.58e8, "5 yr"), (3.15e8, "10 yr"),
    (1.58e9, "50 yr"), (3.15e9, "100 yr"), (1.58e10, "500 yr"),
    (3.15e10, "1 kyr"), (3.15e11, "10 kyr"),
    (1.58e12, "50 kyr"), (3.15e12, "100 kyr"), (1.58e13, "500 kyr"),
    (3.15e13, "1 Myr"), (3.15e14, "10 Myr"), (1.58e15, "50 Myr"),
    (3.15e15, "100 Myr"), (1.58e16, "500 Myr"), (3.15e16, "1 Gyr"),
]

# --- Precompute static geometry ---
n_pts = 200
theta_e = np.linspace(0, 2 * np.pi, n_pts)
ell_x = center_x + (ellipse_width / 2) * np.cos(theta_e)
ell_y = center_y + (ellipse_height / 2) * np.sin(theta_e)

# Reference tau curves (static)
ref_data = []
for label, t_val, color in taus_ref:
    v_vals = calculate_v_curve(t_val, T_room, K_axis_J)
    ref_data.append({
        'label': label,
        'color': color,
        'y': [round(float(v), 5) for v in v_vals],
    })

# --- Precompute frames ---
frame_data = []
for t_elapsed, t_label in time_steps:
    v_boundary = calculate_v_curve(t_elapsed, T_room, K_axis_J)

    # Interpolate boundary at ellipse x-coordinates
    v_at_fill = np.interp(ell_x, K_axis_kJ, v_boundary)

    # SSD portion: above the boundary (clamp to avoid huge values)
    ssd_y = np.clip(np.maximum(ell_y, v_at_fill), 0, 0.6)
    # VRM portion: below the boundary
    vrm_y = np.minimum(ell_y, v_at_fill)
    # Boundary curve clipped to plot range
    bnd_y = np.clip(v_boundary, 0, 0.5)

    frame_data.append({
        'label': t_label,
        'ssd_y': [round(float(v), 5) for v in ssd_y],
        'vrm_y': [round(float(v), 5) for v in vrm_y],
        'bnd_y': [round(float(v), 5) for v in bnd_y],
    })

print(f"Frames: {len(frame_data)}")

data_json = json.dumps({
    'K': [round(float(v), 4) for v in K_axis_kJ],
    'ell_x': [round(float(v), 4) for v in ell_x],
    'ell_y': [round(float(v), 5) for v in ell_y],
    'ref': ref_data,
    'frames': frame_data,
}, separators=(',', ':'))

print(f"JSON size: {len(data_json) / 1e3:.0f} KB")

# --- HTML Template ---
html_template = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>VRM Acquisition: Grain Population Remagnetization</title>
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

  .description{
    font-size:0.84rem;
    color:#475569;
    line-height:1.55;
    margin-bottom:14px;
  }
  .description b{color:#1e293b}
  .description .pill{
    font-family:'JetBrains Mono',monospace;
    font-size:0.8rem;
    background:#ece9e3;
    padding:1px 5px;border-radius:3px;
  }

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
  .time-val{
    font-family:'JetBrains Mono',monospace;
    font-size:1.05rem;font-weight:600;
    min-width:90px;text-align:right;
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
  <div class="description">
    Grains with relaxation time &tau;&nbsp;&lt;&nbsp;<i>t</i> acquire a <b>viscous remanent
    magnetization</b> (VRM) in the ambient field. As time elapses, the blocking boundary
    (dashed) sweeps upward through the grain population, converting
    <b style="color:#B8860B">stable NRM</b> grains to
    <b style="color:#0072B2">VRM</b>.
    &nbsp;
    <span class="pill">T = 300 K</span> &middot;
    <span class="pill">&tau;&#8320; = 10&#8315;&#8313; s</span>
  </div>

  <div class="controls">
    <label>Elapsed time:</label>
    <div class="slider-wrap">
      <input type="range" id="tSlider" min="0" max="%%MAXIDX%%" value="0" step="1">
      <div class="time-val" id="tVal">1 s</div>
    </div>
    <button class="btn" id="btnPlay">&#9654; Play</button>
    <button class="btn" id="btnReset">Reset</button>
  </div>

  <div class="status" id="status">
    <span class="lbl">Elapsed Time:</span> 1 s
  </div>

  <div id="plot"></div>
</div>

<script>
const DATA = %%DATA%%;
const K = DATA.K;
const ell_x = DATA.ell_x;
const frames = DATA.frames;
const ff = 'Source Serif 4, Georgia, serif';
const C = {grid:'#e8e6e1', ax:'#334155'};

const init = frames[0];

// --- Traces ---
// 0: SSD fill (gold)       — dynamic
// 1: VRM fill (light blue) — dynamic
// 2: Ellipse outline        — static
// 3–5: Reference tau lines  — static
// 6: tau=t boundary         — dynamic

const traces = [
  {x:ell_x, y:init.ssd_y, fill:'toself', mode:'lines',
   line:{width:0.5,color:'gray'}, fillcolor:'rgba(255,215,0,0.5)',
   hoverinfo:'skip', showlegend:false},

  {x:ell_x, y:init.vrm_y, fill:'toself', mode:'lines',
   line:{width:0.5,color:'gray'}, fillcolor:'rgba(173,216,230,0.6)',
   hoverinfo:'skip', showlegend:false},

  {x:DATA.ell_x, y:DATA.ell_y, mode:'lines',
   line:{width:1.5,color:'gray'},
   hoverinfo:'skip', showlegend:false},
];

// Reference tau lines
DATA.ref.forEach(function(r) {
  traces.push({
    x:K, y:r.y, mode:'lines',
    line:{color:r.color, width:2.5},
    name:'\u03C4 = ' + r.label,
    showlegend:true,
  });
});

// Current boundary (trace index 6)
traces.push({
  x:K, y:init.bnd_y, mode:'lines',
  line:{color:'black', width:2, dash:'dash'},
  name:'\u03C4 = t (boundary)',
  showlegend:true,
});

const layout = {
  width:600, height:390,
  margin:{l:68, r:24, t:10, b:50},
  paper_bgcolor:'transparent',
  plot_bgcolor:'#fff',
  font:{family:ff, size:12, color:'#1e293b'},

  xaxis:{
    title:{text:'Anisotropy Energy Density (kJ/m\u00B3)', font:{size:13}},
    range:[0,4],
    showgrid:true, gridcolor:C.grid, gridwidth:1,
    zeroline:false, linecolor:C.ax, linewidth:1.5, mirror:true,
    ticks:'inside', ticklen:5,
    tickfont:{family:ff, size:11},
  },
  yaxis:{
    title:{text:'Grain Volume (zm\u00B3)', font:{size:13}},
    range:[0,0.48],
    showgrid:true, gridcolor:C.grid, gridwidth:1,
    zeroline:false, linecolor:C.ax, linewidth:1.5, mirror:true,
    ticks:'inside', ticklen:5,
    tickfont:{family:ff, size:11},
  },

  legend:{
    bgcolor:'rgba(255,255,255,0.92)',
    bordercolor:'#d6d3cd', borderwidth:1,
    font:{size:11},
    x:0.98, y:0.98, xanchor:'right', yanchor:'top',
    borderpad:6,
  },

  annotations:[
    {x:0.2, y:0.05, text:'VRM acquired<br>(Superparamagnetic)',
     showarrow:false, font:{size:12, color:'#0072B2', family:ff},
     bgcolor:'rgba(255,255,255,0.85)', borderpad:2},
    {x:2.5, y:0.26, text:'Stable remanence<br>(Original NRM)',
     showarrow:false, font:{size:12, color:'#B8860B', family:ff},
     bgcolor:'rgba(255,255,255,0.85)', borderpad:2},
  ],

  hovermode:'closest',
};

Plotly.newPlot('plot', traces, layout, {displayModeBar:false, responsive:true});

// --- Interactivity ---
const slider = document.getElementById('tSlider');
const tValEl = document.getElementById('tVal');
const statusEl = document.getElementById('status');
const btnPlay = document.getElementById('btnPlay');
const btnReset = document.getElementById('btnReset');

function updateToFrame(idx) {
  const f = frames[idx];
  Plotly.restyle('plot', {y:[f.ssd_y, f.vrm_y]}, [0, 1]);
  Plotly.restyle('plot', {y:[f.bnd_y]}, [6]);
  tValEl.textContent = f.label;
  slider.value = idx;
  statusEl.innerHTML = '<span class="lbl">Elapsed Time:</span> ' + f.label;
}

slider.addEventListener('input', function() {
  updateToFrame(parseInt(this.value));
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
  let idx = parseInt(slider.value);
  playTimer = setInterval(function() {
    idx++;
    if (idx >= frames.length) { stopPlay(); return; }
    updateToFrame(idx);
  }, 250);
});

btnReset.addEventListener('click', function() {
  stopPlay();
  updateToFrame(0);
});
</script>
</body>
</html>"""

# --- Write output ---
html_out = html_template.replace('%%DATA%%', data_json)
html_out = html_out.replace('%%MAXIDX%%', str(len(time_steps) - 1))

output_path = '../book/figures/chapter7/vrm_widget.html'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, 'w') as f:
    f.write(html_out)

sz = os.path.getsize(output_path)
print(f"Written to {output_path}")
print(f"File size: {sz / 1e3:.0f} KB")

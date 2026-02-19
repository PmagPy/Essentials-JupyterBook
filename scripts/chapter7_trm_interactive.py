"""
Generate a self-contained HTML file for TRM acquisition visualization.

All physics computation happens in JavaScript for a compact file.
Shows how a grain population acquires a thermoremanent magnetization
(TRM) as the rock cools from near the Curie temperature to room
temperature, with the grain population migrating rightward in V-K
space as anisotropy energy grows.

Style matches chapter7_vrm_interactive.py (Source Serif 4, control bar, etc.).
"""

import os

html_content = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>TRM Acquisition: Cooling from Curie Temperature</title>
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
    During cooling, <b>M<sub>s</sub></b> grows and anisotropy energy
    <b>K</b> (&prop; M<sub>s</sub>&sup2;) increases &mdash; shifting the grain
    population (ellipse) rightward. The &tau;&nbsp;=&nbsp;100&nbsp;s blocking
    boundary (dashed) descends, progressively converting
    <b style="color:#0072B2">superparamagnetic</b> grains to
    <b style="color:#B8860B">blocked TRM</b> carriers.
    &nbsp;
    <span class="pill">T<sub>c</sub> = 580 &deg;C</span> &middot;
    <span class="pill">&tau;&#8320; = 10&#8315;&#8313; s</span> &middot;
    <span class="pill">&gamma; = 0.38</span>
  </div>

  <div class="controls">
    <label>Temperature:</label>
    <div class="slider-wrap">
      <input type="range" id="tSlider" min="0" max="54" value="54" step="1">
      <div class="time-val" id="tVal">560 &deg;C</div>
    </div>
    <button class="btn" id="btnPlay">&#9654; Cool</button>
    <button class="btn" id="btnReset">Reset</button>
  </div>

  <div class="status" id="status">
    <span class="lbl">Temperature:</span> 560 &deg;C
  </div>

  <div id="plot"></div>
</div>

<script>
/* --- Physics constants --- */
var kB = 1.380649e-23;
var tau0 = 1e-9;
var Tc_K = 853;        /* magnetite Curie temperature in K */
var gamma = 0.38;
var Troom_K = 293.15;
var ms_room = Math.pow(1 - Troom_K / Tc_K, gamma);

/* Grain population ellipse (reference at room temperature) */
var refCx = 1.3, refCy = 0.19;   /* kJ/m³, zm³ */
var ellW = 1.6, ellH = 0.30;

/* --- Temperature steps: 20 to 560 °C in steps of 10 --- */
var temps = [];
for (var t = 20; t <= 560; t += 10) temps.push(t);

/* --- K axis (kJ/m³) --- */
var nK = 300;
var K_kJ = new Array(nK);
var K_J = new Array(nK);
for (var i = 0; i < nK; i++) {
  K_kJ[i] = 0.01 + (5.0 - 0.01) * i / (nK - 1);
  K_J[i] = K_kJ[i] * 1000;
}

/* --- Ellipse angular coords (constant) --- */
var nE = 200;
var cosTheta = new Array(nE);
var sinTheta = new Array(nE);
var ey_base = new Array(nE);      /* ey never changes */
for (var i = 0; i < nE; i++) {
  var th = 2 * Math.PI * i / (nE - 1);
  cosTheta[i] = Math.cos(th);
  sinTheta[i] = Math.sin(th);
  ey_base[i] = refCy + (ellH / 2) * sinTheta[i];
}

/* --- Reference tau values --- */
var tauDefs = [
  {label: '100 s',   val: 100,            color: '#0072B2', dash: 'solid', w: 2.5},
  {label: '1 Myr',   val: 1e6 * 3.15e7,   color: '#E69F00', dash: 'solid', w: 2.5},
  {label: '4.5 Gyr', val: 4.5e9 * 3.15e7, color: '#D55E00', dash: 'solid', w: 2.5}
];

/* --- Helper functions --- */
function msRatio(T_K) {
  if (T_K >= Tc_K) return 0;
  return Math.pow(1 - T_K / Tc_K, gamma) / ms_room;
}

function calcV(tau, T_K, kj) {
  /* V in zm³ for a single K value in J/m³ */
  return (kB * T_K * Math.log(tau / tau0)) / Math.max(kj, 1e-5) * 1e21;
}

function interp(x_new, x_arr, y_arr) {
  /* Linear interpolation; x_arr must be sorted ascending */
  var n = x_new.length, nArr = x_arr.length;
  var result = new Array(n);
  for (var i = 0; i < n; i++) {
    var xn = x_new[i];
    if (xn <= x_arr[0])       { result[i] = y_arr[0]; continue; }
    if (xn >= x_arr[nArr - 1]){ result[i] = y_arr[nArr - 1]; continue; }
    var lo = 0, hi = nArr - 1;
    while (hi - lo > 1) {
      var mid = (lo + hi) >> 1;
      if (x_arr[mid] <= xn) lo = mid; else hi = mid;
    }
    var frac = (xn - x_arr[lo]) / (x_arr[hi] - x_arr[lo]);
    result[i] = y_arr[lo] + frac * (y_arr[hi] - y_arr[lo]);
  }
  return result;
}

/* --- Compute one frame at temperature T_C (°C) --- */
function computeFrame(T_C) {
  var T_K = T_C + 273.15;
  var msr = msRatio(T_K);
  var sf = msr * msr;            /* K ∝ Ms² */

  var cx = refCx * sf;
  var w  = ellW  * sf;

  /* Ellipse x coords (y is constant = ey_base) */
  var ex = new Array(nE);
  for (var i = 0; i < nE; i++) ex[i] = cx + (w / 2) * cosTheta[i];

  /* tau = 100 s boundary at this temperature */
  var bnd = new Array(nK);
  for (var i = 0; i < nK; i++)
    bnd[i] = Math.min(Math.max(calcV(100, T_K, K_J[i]), 0), 0.5);

  /* Boundary interpolated at ellipse x positions */
  var v_at_ex = interp(ex, K_kJ, bnd);

  /* SSD / blocked (above boundary) */
  var ssd_y = new Array(nE);
  for (var i = 0; i < nE; i++)
    ssd_y[i] = Math.min(Math.max(ey_base[i], v_at_ex[i]), 0.6);

  /* SP / unblocked (below boundary) */
  var sp_y = new Array(nE);
  for (var i = 0; i < nE; i++)
    sp_y[i] = Math.min(ey_base[i], v_at_ex[i]);

  /* Reference tau curves at this temperature */
  var refs = [];
  for (var t = 0; t < tauDefs.length; t++) {
    var rv = new Array(nK);
    for (var i = 0; i < nK; i++)
      rv[i] = Math.min(Math.max(calcV(tauDefs[t].val, T_K, K_J[i]), 0), 0.5);
    refs.push(rv);
  }

  return {ex: ex, ssd_y: ssd_y, sp_y: sp_y, refs: refs, msr: msr};
}

/* --- Initial state (560 °C) --- */
var initIdx = temps.length - 1;
var init = computeFrame(temps[initIdx]);

var ff = 'Source Serif 4, Georgia, serif';
var gridC = '#e8e6e1', axC = '#334155';

/* --- Traces ---
   0: SSD fill (gold)        – dynamic (x & y)
   1: SP  fill (light blue)  – dynamic (x & y)
   2: Ellipse outline        – dynamic (x only, y = ey_base)
   3: tau = 100 s boundary   – dynamic (y only)
   4: tau = 1 Myr            – dynamic (y only)
   5: tau = 4.5 Gyr          – dynamic (y only)
*/
var traces = [
  {x: init.ex, y: init.ssd_y, fill: 'toself', mode: 'lines',
   line: {width: 0.5, color: 'gray'}, fillcolor: 'rgba(255,215,0,0.5)',
   hoverinfo: 'skip', showlegend: false},

  {x: init.ex, y: init.sp_y, fill: 'toself', mode: 'lines',
   line: {width: 0.5, color: 'gray'}, fillcolor: 'rgba(173,216,230,0.6)',
   hoverinfo: 'skip', showlegend: false},

  {x: init.ex, y: ey_base, mode: 'lines',
   line: {width: 1.5, color: 'gray'},
   hoverinfo: 'skip', showlegend: false}
];

for (var t = 0; t < tauDefs.length; t++) {
  traces.push({
    x: K_kJ, y: init.refs[t], mode: 'lines',
    line: {color: tauDefs[t].color, width: tauDefs[t].w, dash: tauDefs[t].dash},
    name: '\u03C4 = ' + tauDefs[t].label + (t === 0 ? ' (boundary)' : ''),
    showlegend: true
  });
}

var layout = {
  width: 600, height: 390,
  margin: {l: 68, r: 24, t: 10, b: 50},
  paper_bgcolor: 'transparent',
  plot_bgcolor: '#fff',
  font: {family: ff, size: 12, color: '#1e293b'},

  xaxis: {
    title: {text: 'Anisotropy Energy Density (kJ/m\u00B3)', font: {size: 13}},
    range: [0, 4],
    showgrid: true, gridcolor: gridC, gridwidth: 1,
    zeroline: false, linecolor: axC, linewidth: 1.5, mirror: true,
    ticks: 'inside', ticklen: 5,
    tickfont: {family: ff, size: 11}
  },
  yaxis: {
    title: {text: 'Grain Volume (zm\u00B3)', font: {size: 13}},
    range: [0, 0.48],
    showgrid: true, gridcolor: gridC, gridwidth: 1,
    zeroline: false, linecolor: axC, linewidth: 1.5, mirror: true,
    ticks: 'inside', ticklen: 5,
    tickfont: {family: ff, size: 11}
  },

  legend: {
    bgcolor: 'rgba(255,255,255,0.92)',
    bordercolor: '#d6d3cd', borderwidth: 1,
    font: {size: 11},
    x: 0.98, y: 0.98, xanchor: 'right', yanchor: 'top',
    borderpad: 6
  },

  annotations: [
    {x: 0.2, y: 0.05, text: 'Superparamagnetic<br>(unblocked)',
     showarrow: false, font: {size: 12, color: '#0072B2', family: ff},
     bgcolor: 'rgba(255,255,255,0.85)', borderpad: 2},
    {x: 2.8, y: 0.30, text: 'Blocked<br>(TRM acquired)',
     showarrow: false, font: {size: 12, color: '#B8860B', family: ff},
     bgcolor: 'rgba(255,255,255,0.85)', borderpad: 2}
  ],

  hovermode: 'closest'
};

Plotly.newPlot('plot', traces, layout, {displayModeBar: false, responsive: true});

/* --- Interactivity --- */
var slider  = document.getElementById('tSlider');
var tValEl  = document.getElementById('tVal');
var statusEl = document.getElementById('status');
var btnPlay  = document.getElementById('btnPlay');
var btnReset = document.getElementById('btnReset');

function updateToIdx(idx) {
  var T_C = temps[idx];
  var f = computeFrame(T_C);

  Plotly.restyle('plot',
    {x: [f.ex, f.ex, f.ex], y: [f.ssd_y, f.sp_y, ey_base]}, [0, 1, 2]);
  Plotly.restyle('plot',
    {y: [f.refs[0], f.refs[1], f.refs[2]]}, [3, 4, 5]);

  tValEl.textContent = T_C + ' \u00B0C';
  slider.value = idx;
  statusEl.innerHTML =
    '<span class="lbl">Temperature:</span> ' + T_C + ' \u00B0C' +
    ' &nbsp;|&nbsp; <span class="lbl">M<sub>s</sub>/M<sub>s\u2080</sub>:</span> ' +
    f.msr.toFixed(2);
}

slider.addEventListener('input', function() {
  updateToIdx(parseInt(this.value));
});

var playing = false, playTimer = null;

function stopPlay() {
  playing = false;
  clearInterval(playTimer);
  btnPlay.innerHTML = '&#9654; Cool';
  btnPlay.classList.remove('active');
}

btnPlay.addEventListener('click', function() {
  if (playing) { stopPlay(); return; }
  playing = true;
  btnPlay.innerHTML = '&#9646;&#9646; Pause';
  btnPlay.classList.add('active');
  var idx = parseInt(slider.value);
  playTimer = setInterval(function() {
    idx--;
    if (idx < 0) { stopPlay(); return; }
    updateToIdx(idx);
  }, 200);
});

btnReset.addEventListener('click', function() {
  stopPlay();
  updateToIdx(temps.length - 1);
});
</script>
</body>
</html>"""

# --- Write output ---
output_path = '../book/figures/chapter7/trm_widget.html'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, 'w') as f:
    f.write(html_content)

sz = os.path.getsize(output_path)
print(f"Written to {output_path}")
print(f"File size: {sz / 1e3:.0f} KB")

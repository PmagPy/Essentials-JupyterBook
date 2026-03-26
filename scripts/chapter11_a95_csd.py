"""Generate Figure 11.5 (a95-csd.png): CSD, delta, and alpha95 vs N.

Shows dependence of estimated angular standard deviation (CSD and delta)
and confidence limit (alpha95) on number of directions in a data set.
Directions drawn from a Fisher distribution with S=15 degrees (kappa=29.2).
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import numpy as np
import matplotlib.pyplot as plt
import pmagpy.ipmag as ipmag
import pmagpy.pmag as pmag
from figure_style import apply_mpl_style

apply_mpl_style()

# Generate N=30 Fisher distributed directions with kappa=29.2 (S=15 degrees)
kappa = 29.2
N_total = 30
true_S = 15.0

di_block = ipmag.fishrot(k=kappa, n=N_total, dec=0, inc=90,
                         di_block=True, random_seed=2)

# Calculate statistics for progressively larger subsets
N_range = range(4, N_total + 1)
csd_vals = []
delta_vals = []
a95_vals = []

for n in N_range:
    subset = di_block[:n]
    result = pmag.fisher_mean(subset)

    N = result['n']
    R = result['r']
    k = result['k']

    # CSD approximation: 81/sqrt(k)
    csd = 81.0 / np.sqrt(k)
    csd_vals.append(csd)

    # delta: arccos(R/N) in degrees
    delta = np.degrees(np.arccos(R / N))
    delta_vals.append(delta)

    # alpha95
    a95_vals.append(result['alpha95'])

N_arr = np.array(list(N_range))

# Colorblind-friendly palette (Okabe-Ito)
COLOR_CSD = '#0072B2'    # blue
COLOR_DELTA = '#009E73'   # teal
COLOR_A95 = '#D55E00'     # vermillion

fig, ax = plt.subplots(figsize=(8, 5))

ax.plot(N_arr, csd_vals, 's-', color=COLOR_CSD, markersize=5,
        linewidth=1.5, label='CSD')
ax.plot(N_arr, delta_vals, '^-', color=COLOR_DELTA, markersize=5,
        linewidth=1.5, label=r'$\delta$')
ax.plot(N_arr, a95_vals, 'o-', color=COLOR_A95, markersize=5,
        linewidth=1.5, label=r'$\alpha_{95}$')

# Horizontal line at true S = 15
ax.axhline(true_S, color='0.4', linewidth=1, linestyle='--',
           label=f'True $S$ = {true_S:.0f}°')

# Labels
ax.set_xlabel('$N$ (number of directions)', fontsize=15)
ax.set_ylabel('Angle (°)', fontsize=15)
ax.tick_params(labelsize=14)
ax.set_xlim(3, 31)
ax.set_ylim(4, 22)

# Direct curve labels with white background
label_bbox = dict(boxstyle='round,pad=0.15', facecolor='white',
                  edgecolor='none', alpha=0.85)

ax.text(22, csd_vals[22 - 4] + 0.8, 'CSD', fontsize=16, color=COLOR_CSD,
        fontweight='bold', bbox=label_bbox)
ax.text(22, delta_vals[22 - 4] - 1.2, r'$\delta$', fontsize=16, color=COLOR_DELTA,
        fontweight='bold', bbox=label_bbox)
ax.text(22, a95_vals[22 - 4] + 0.8, r'$\alpha_{95}$', fontsize=16, color=COLOR_A95,
        fontweight='bold', bbox=label_bbox)

plt.tight_layout()
outpath = os.path.join(os.path.dirname(__file__),
                       '..', 'book', 'figures', 'chapter11', 'a95-csd.png')
fig.savefig(outpath, dpi=300, bbox_inches='tight')
plt.close()
print(f"Saved {outpath}")

"""Generate Figure 11.2 (fisher.png): 3x3 grid of Fisher distributed directions.

Nine equal area projections with increasing concentration parameter:
Row 1: kappa=5 (a-c), Row 2: kappa=10 (d-f), Row 3: kappa=50 (g-i).
All drawn from Fisher distributions with a vertical true mean direction.
Each panel shows estimated D, I, k, alpha95 as inset text.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import numpy as np
import matplotlib.pyplot as plt
import pmagpy.ipmag as ipmag
from figure_style import apply_mpl_style

apply_mpl_style()

# Parameters
kappas = [5, 5, 5, 10, 10, 10, 50, 50, 50]
row_kappas = [5, 10, 50]
N = 30
true_dec, true_inc = 0, 90  # vertical true direction

# Colorblind-friendly palette (Okabe-Ito)
DATA_COLOR = '#0072B2'   # blue
MEAN_COLOR = '#D55E00'   # vermillion

fig, axes = plt.subplots(3, 3, figsize=(9, 9))

for idx, kappa in enumerate(kappas):
    row, col = divmod(idx, 3)
    ax = axes[row, col]

    # Generate Fisher distributed data with unique seed per panel
    di_block = ipmag.fishrot(k=kappa, n=N, dec=true_dec, inc=true_inc,
                             di_block=True, random_seed=idx + 1)

    # Calculate Fisher statistics
    mean_result = ipmag.fisher_mean(di_block=di_block)

    # White filled circle behind the stereonet to mask overlapping neighbors
    background = plt.Circle((0, 0), 1.1, transform=ax.transData,
                             facecolor='white', edgecolor='none', zorder=0)
    ax.add_patch(background)

    # Plot on equal area projection
    ipmag.plot_net(ax=ax)
    plt.sca(ax)  # set current axes for ipmag plotting functions
    decs = [d[0] for d in di_block]
    incs = [d[1] for d in di_block]
    ipmag.plot_di(dec=decs, inc=incs, color=DATA_COLOR, marker='o',
                  markersize=20, edge='k')

    # Plot mean direction with alpha95 circle
    ipmag.plot_di_mean(mean_result['dec'], mean_result['inc'],
                       mean_result['alpha95'], color=MEAN_COLOR,
                       marker='^', markersize=50)

    # Add statistics text box inside the circle near the top
    stats_text = (f"$D$ = {mean_result['dec']:.1f}, "
                  f"$I$ = {mean_result['inc']:.1f}\n"
                  f"$k$ = {mean_result['k']:.1f}, "
                  f"$\\alpha_{{95}}$ = {mean_result['alpha95']:.1f}")
    ax.text(0.5, 0.95, stats_text, transform=ax.transAxes,
            fontsize=10, ha='center', va='top',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                      edgecolor='black', linewidth=0.5, alpha=0.85))

    # Kappa label on left side of each row
    if col == 0:
        ax.text(-0.01, 0.5, f'$\\kappa$ = {kappa}', transform=ax.transAxes,
                fontsize=14, fontweight='bold', ha='center', va='center',
                rotation=90)

plt.subplots_adjust(hspace=-0.1, wspace=-0.1)
outpath = os.path.join(os.path.dirname(__file__),
                       '..', 'book', 'figures', 'chapter11', 'fisher_new.png')
fig.savefig(outpath, dpi=300, bbox_inches='tight')
plt.close()
print(f"Saved {outpath}")

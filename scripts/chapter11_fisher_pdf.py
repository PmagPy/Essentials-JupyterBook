"""Generate Figure 11.3 (P_new.png): Fisher probability density functions.

Two panels:
Left: P_dA(alpha) — probability per unit angular area vs angle from true mean
Right: P_dalpha(alpha) — probability per angular band (includes sin(alpha) factor)

Curves shown for kappa = 5, 10, 50, 100.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import numpy as np
import matplotlib.pyplot as plt
from figure_style import apply_mpl_style

apply_mpl_style()

# Angle range
alpha_deg = np.linspace(0.01, 50, 500)
alpha = np.radians(alpha_deg)

kappas = [5, 10, 50, 100]
# Colorblind-friendly palette (Okabe-Ito)
colors = ['#E69F00', '#D55E00', '#009E73', '#0072B2']

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5))

label_bbox = dict(boxstyle='round,pad=0.15', facecolor='white',
                  edgecolor='none', alpha=0.85)

# Store curves for labeling
curves_dA = {}
curves_dalpha = {}

for kappa, color in zip(kappas, colors):
    # P_dA: probability per unit angular area (Eq. 11.3)
    P_dA = (kappa / (4 * np.pi * np.sinh(kappa))) * np.exp(kappa * np.cos(alpha))

    # P_dalpha: probability per angular band (Eq. 11.7)
    P_dalpha = (kappa / (2 * np.sinh(kappa))) * np.exp(kappa * np.cos(alpha)) * np.sin(alpha)

    ax1.plot(alpha_deg, P_dA, color=color, linewidth=2)
    ax2.plot(alpha_deg, P_dalpha, color=color, linewidth=2)
    curves_dA[kappa] = (P_dA, color)
    curves_dalpha[kappa] = (P_dalpha, color)

# Direct labels for left panel (P_dA — monotonically decreasing, label near peak)
for kappa, (P_dA, color) in curves_dA.items():
    idx_peak = np.argmax(P_dA)
    x_label = alpha_deg[idx_peak] + 0.4
    y_offset = 0.3 if (P_dA.max() < 2 and kappa != 5) else 0
    ax1.text(x_label, P_dA[idx_peak] + y_offset, f'$\\kappa$ = {kappa}',
             fontsize=11, color=color, fontweight='bold', va='center',
             ha='left', bbox=label_bbox)

# Direct labels for right panel (P_dalpha — has peaks, label 0.5 deg right of peak)
for kappa, (P_dalpha, color) in curves_dalpha.items():
    idx_peak = np.argmax(P_dalpha)
    x_label = alpha_deg[idx_peak] + 0.4
    ax2.text(x_label, P_dalpha[idx_peak], f'$\\kappa$ = {kappa}',
             fontsize=11, color=color, fontweight='bold', va='center',
             ha='left', bbox=label_bbox)

# Left panel
ax1.text(0.97, 0.95, 'Probability per unit area', transform=ax1.transAxes,
         fontsize=14, ha='right', va='top',
         bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                   edgecolor='none', alpha=0.85))
ax1.set_xlabel(r'Angle from true mean ($\alpha$)', fontsize=13)
ax1.set_ylabel(r'$P_{dA}(\alpha)$', fontsize=13)
ax1.tick_params(labelsize=12)
ax1.set_xlim(0, 50)
ax1.set_ylim(bottom=0)

# Right panel
ax2.text(0.97, 0.95, 'Probability per angular band', transform=ax2.transAxes,
         fontsize=14, ha='right', va='top',
         bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                   edgecolor='none', alpha=0.85))
ax2.set_xlabel(r'Angle from true mean ($\alpha$)', fontsize=13)
ax2.set_ylabel(r'$P_{d\alpha}(\alpha)$', fontsize=13)
ax2.tick_params(labelsize=12)
ax2.set_xlim(0, 50)
ax2.set_ylim(bottom=0)

plt.tight_layout()
outpath = os.path.join(os.path.dirname(__file__),
                       '..', 'book', 'figures', 'chapter11', 'P_new.png')
fig.savefig(outpath, dpi=300, bbox_inches='tight')
plt.close()
print(f"Saved {outpath}")

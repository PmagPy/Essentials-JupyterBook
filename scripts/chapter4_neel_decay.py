"""
Exponential decay of magnetisation M(t) = Mo exp(-t/τ).

The initial magnetisation Mo decays to 1/e of its original strength in time τ.
"""

import numpy as np
import matplotlib.pyplot as plt

# --- Wong (2011) colorblind-safe palette ---
COLOR_VERMILLION = '#D55E00'

# --- Plot ---
t = np.linspace(0, 2.0, 500)
M = np.exp(-t)

fig, ax = plt.subplots(figsize=(6, 4))

ax.plot(t, M, color=COLOR_VERMILLION, linewidth=2.5, zorder=3)

# Dashed guide-lines at Mo/e and t/τ = 1
inv_e = 1.0 / np.e
ax.plot([0, 1.0], [inv_e, inv_e], 'k--', linewidth=1.2, zorder=2)
ax.plot([1.0, 1.0], [0.1, inv_e], 'k--', linewidth=1.2, zorder=2)

ax.text(0.08, inv_e + 0.025, r'$M_o/e$', fontsize=14, va='bottom')
ax.text(0.6, 0.55,
        r'$M(t) = M_o\,e^{(-t/\tau)}$',
        fontsize=18, ha='center', va='center',
        transform=ax.transAxes)

ax.set_xlim(0, 2.0)
ax.set_ylim(0.1, 1.0)
ax.set_xlabel(r'$t\,/\,\tau$', fontsize=16)
ax.set_ylabel(r'$M\,/\,M_o$', fontsize=16)
ax.tick_params(axis='both', labelsize=14)

fig.savefig('../book/figures/chapter4/neel_exponential_decay.png', dpi=200,
            bbox_inches='tight', facecolor='white')
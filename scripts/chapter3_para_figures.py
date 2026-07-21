"""Generate the Langevin-function and Curie-law figures for chapter 3.

Produces two single-concept figures that replace the two-panel para.png:

- ../book/figures/chapter3/langevin.png  — the Langevin function
  L(a) = coth(a) - 1/a with the low-field a/3 tangent, the saturation
  asymptote, and the 90%-saturation marker at a ~ 10
- ../book/figures/chapter3/curie_law.png — Curie's law chi_p ∝ 1/T,
  normalized to room temperature

Run from the scripts/ directory:

    python chapter3_para_figures.py
"""

import matplotlib.pyplot as plt
import numpy as np

MAROON = '#7a0019'
GOLD = '#b8860b'
MUTED = '#555555'
GRID = '#dddddd'

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Helvetica Neue', 'Helvetica', 'Arial', 'DejaVu Sans'],
    'font.size': 13,
    'axes.labelsize': 15,
    'axes.linewidth': 1.1,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'xtick.labelsize': 12,
    'ytick.labelsize': 12,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.facecolor': 'white',
})


def langevin(a):
    """Langevin function L(a) = coth(a) - 1/a, safe at a -> 0."""
    a = np.asarray(a, dtype=float)
    out = np.empty_like(a)
    small = np.abs(a) < 1e-6
    out[small] = a[small] / 3
    out[~small] = 1 / np.tanh(a[~small]) - 1 / a[~small]
    return out


def build_langevin():
    fig, ax = plt.subplots(figsize=(6.8, 4.4))

    a = np.linspace(0, 15, 600)
    ax.plot(a, langevin(a), color=MAROON, lw=3.2, zorder=4)

    # saturation asymptote
    ax.axhline(1, color=MUTED, lw=1.4, ls=':')
    ax.text(14.8, 1.025, 'saturation: all moments aligned',
            ha='right', va='bottom', fontsize=11.5, color=MUTED)

    # low-field tangent a/3
    a_lin = np.linspace(0, 3.45, 50)
    ax.plot(a_lin, a_lin / 3, color=GOLD, lw=2.2, ls='--', zorder=3)
    ax.annotate('low-field limit:\n$\\mathcal{L}(a) \\approx a/3$',
                xy=(2.6, 2.6 / 3), xytext=(3.6, 0.98),
                fontsize=12.5, color=GOLD, ha='left', va='top',
                arrowprops=dict(arrowstyle='-', color=GOLD, lw=1.2))

    # curve label
    ax.text(8.2, 0.74, '$\\mathcal{L}(a) = \\coth a - 1/a$',
            fontsize=15, color=MAROON, ha='center')

    # 90% saturation marker
    a90 = 10.0
    ax.plot([a90], [langevin([a90])[0]], 'o', ms=8, color=MAROON,
            mec='white', mew=1.2, zorder=5)
    ax.annotate('90% saturated at $a \\approx 10$\n(~10$^{3}$ T at 300 K)',
                xy=(a90, 0.9), xytext=(10.4, 0.56),
                fontsize=11.5, color=MUTED, ha='left',
                arrowprops=dict(arrowstyle='->', color=MUTED, lw=1.1))

    # geological regime marker at the origin
    ax.annotate('geomagnetic fields at 300 K:\n$a \\sim 10^{-6}$ — deep in the\nlinear regime',
                xy=(0.12, 0.04), xytext=(3.6, 0.30),
                fontsize=11.5, color=MUTED, ha='left',
                arrowprops=dict(arrowstyle='->', color=MUTED, lw=1.1,
                                connectionstyle='arc3,rad=0.15'))

    ax.set_xlim(0, 15)
    ax.set_ylim(0, 1.12)
    ax.set_xlabel('$a = mB\\,/\\,k_BT$   (magnetic ÷ thermal energy)')
    ax.set_ylabel('$M\\,/\\,M_s$')
    ax.set_yticks([0, 0.25, 0.5, 0.75, 1.0])
    ax.grid(color=GRID, lw=0.7, alpha=0.7)
    ax.set_axisbelow(True)

    fig.savefig('../book/figures/chapter3/langevin.png')
    plt.close(fig)
    print('wrote ../book/figures/chapter3/langevin.png')


def build_curie():
    fig, ax = plt.subplots(figsize=(6.8, 4.4))

    T = np.linspace(50, 900, 600)
    chi = 300 / T                      # chi_p(T) / chi_p(300 K) = 300 / T
    ax.plot(T, chi, color=MAROON, lw=3.2, zorder=4)

    # room-temperature reference
    ax.plot([300], [1], 'o', ms=9, color=GOLD, mec='white', mew=1.2, zorder=5)
    ax.annotate('room temperature\n(300 K)', xy=(300, 1), xytext=(390, 1.55),
                fontsize=11.5, color=MUTED, ha='left',
                arrowprops=dict(arrowstyle='->', color=MUTED, lw=1.1))
    ax.axhline(1, color=MUTED, lw=1.0, ls=':', alpha=0.7)

    # halve T, double chi illustration
    ax.plot([150], [2], 'o', ms=8, color=MAROON, mec='white', mew=1.2, zorder=5)
    ax.annotate('halve $T$ $\\rightarrow$ double $\\chi_p$\n(why low-$T$ measurements\nlight up paramagnetic Fe)',
                xy=(150, 2), xytext=(255, 3.1),
                fontsize=11.5, color=MUTED, ha='left',
                arrowprops=dict(arrowstyle='->', color=MUTED, lw=1.1))

    # curve label
    ax.text(600, 0.85, "Curie's law:  $\\chi_p = C\\,/\\,T$",
            fontsize=15, color=MAROON, ha='center')

    ax.set_xlim(0, 900)
    ax.set_ylim(0, 4.4)
    ax.set_xlabel('temperature $T$ (K)')
    ax.set_ylabel('$\\chi_p(T)\\;/\\;\\chi_p(300\\,\\mathrm{K})$')
    ax.grid(color=GRID, lw=0.7, alpha=0.7)
    ax.set_axisbelow(True)

    fig.savefig('../book/figures/chapter3/curie_law.png')
    plt.close(fig)
    print('wrote ../book/figures/chapter3/curie_law.png')


if __name__ == '__main__':
    build_langevin()
    build_curie()

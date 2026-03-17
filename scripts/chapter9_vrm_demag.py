"""
Néel diagram illustrating thermal demagnetization of VRM to isolate ChRM.

Two-panel static figure using Néel relaxation theory with Ms(T) scaling
for magnetite (same physical framework as chapter7_trm_interactive.py).

(a) Room temperature (20 °C): grain population divided into SP, VRM, and ChRM
    regions by iso-τ contours (100 s and 1 Myr).
(b) Heated to T_demag = 200 °C: the τ = 100 s boundary shifts upward and the
    grain population shifts leftward (K ∝ Ms²), demagnetizing VRM grains.
    Only ChRM in higher-T_B grains remains blocked.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, PathPatch
from matplotlib.path import Path
from matplotlib.legend_handler import HandlerPatch

# --- Physical constants ---
k_B = 1.380649e-23      # Boltzmann constant (J/K)
tau_0 = 1e-9             # frequency factor (s)
Tc_K = 853               # Curie temperature for magnetite (K)
gamma = 0.38             # power-law exponent for Ms(T)
T_room_K = 293.15        # 20 °C
ms_room = (1 - T_room_K / Tc_K) ** gamma

# --- Wong (2011) colorblind-safe palette ---
color_100s = '#0072B2'
color_1Myr = '#E69F00'
color_45Gyr = '#D55E00'

# --- Fill colors ---
color_sp = 'lightblue'
color_vrm = '#d4e6b5'   # muted green
color_chrm = 'gold'


def ms_ratio(T_K):
    """Ms(T) / Ms(T_room) using power-law scaling."""
    if T_K >= Tc_K:
        return 0.0
    return ((1 - T_K / Tc_K) ** gamma) / ms_room


def calc_v(tau, K_J, T_K):
    """Grain volume (zm³) for a given τ, K array (J/m³), and T (K)."""
    return (k_B * T_K * np.log(tau / tau_0)) / K_J * 1e21


# --- Tau definitions ---
taus = {
    '100 s': 100,
    '1 Myr': 1e6 * 3.15e7,
    '4.5 Gyr': 4.5e9 * 3.15e7,
}

# --- K axis ---
K_kJ = np.linspace(0.01, 5.0, 800)
K_J = K_kJ * 1000

# --- Grain population ellipse (matches TRM interactive) ---
ref_cx, ref_cy = 1.3, 0.19     # center at room temperature (kJ/m³, zm³)
ell_W, ell_H = 1.6, 0.30       # width, height at room temperature

# --- Axis limits ---
xlim = (0, 4.0)
ylim = (0, 0.48)

# --- Ellipse parametric coords ---
theta = np.linspace(0, 2 * np.pi, 300)


def draw_panel(ax, T_C, panel_label, show_vrm=True):
    """Draw one panel of the Néel diagram.

    Args:
        ax: matplotlib Axes.
        T_C: temperature in °C.
        panel_label: 'a' or 'b'.
        show_vrm: if True, shade VRM region; if False, VRM is demagnetized.
    """
    T_K = T_C + 273.15
    msr = ms_ratio(T_K)
    sf = msr ** 2                     # K ∝ Ms²

    # Ellipse at this temperature
    cx = ref_cx * sf
    w = ell_W * sf
    ex = cx + (w / 2) * np.cos(theta)
    ey = ref_cy + (ell_H / 2) * np.sin(theta)

    # Iso-τ curves at this temperature
    v_100s = np.clip(calc_v(100, K_J, T_K), 0, ylim[1] + 0.5)
    v_1Myr = np.clip(calc_v(1e6 * 3.15e7, K_J, T_K), 0, ylim[1] + 0.5)
    v_45Gyr = np.clip(calc_v(4.5e9 * 3.15e7, K_J, T_K), 0, ylim[1] + 0.5)

    cap = ylim[1] + 1.0

    # --- Clipping paths ---
    # Below τ = 100 s → superparamagnetic
    sp_verts = (list(zip(K_kJ, np.minimum(v_100s, cap)))
                + [(K_kJ[-1], 0), (K_kJ[0], 0)])
    sp_path = Path(sp_verts)

    # Between τ = 100 s and τ = 1 Myr → VRM carriers
    vrm_verts = (list(zip(K_kJ, np.minimum(v_1Myr, cap)))
                 + list(zip(K_kJ[::-1], np.minimum(v_100s[::-1], cap))))
    vrm_path = Path(vrm_verts)

    # Above τ = 1 Myr → ChRM carriers (at room temp)
    # At elevated T, everything above τ = 100 s remains blocked
    chrm_boundary = v_1Myr if show_vrm else v_100s
    chrm_verts = (list(zip(K_kJ, np.minimum(chrm_boundary, cap)))
                  + [(K_kJ[-1], cap), (K_kJ[0], cap)])
    chrm_path = Path(chrm_verts)

    # --- Shaded fills clipped to ellipse ---
    # SP region (light blue)
    ell_sp = Ellipse((cx, ref_cy), w, ell_H,
                     facecolor=color_sp, edgecolor='none', alpha=0.6)
    ax.add_patch(ell_sp)
    ell_sp.set_clip_path(
        PathPatch(sp_path, transform=ax.transData, visible=False))

    if show_vrm:
        # VRM region (muted green)
        ell_vrm = Ellipse((cx, ref_cy), w, ell_H,
                          facecolor=color_vrm, edgecolor='none', alpha=0.6)
        ax.add_patch(ell_vrm)
        ell_vrm.set_clip_path(
            PathPatch(vrm_path, transform=ax.transData, visible=False))

    # ChRM region (gold)
    ell_chrm = Ellipse((cx, ref_cy), w, ell_H,
                       facecolor=color_chrm, edgecolor='none', alpha=0.5)
    ax.add_patch(ell_chrm)
    ell_chrm.set_clip_path(
        PathPatch(chrm_path, transform=ax.transData, visible=False))

    # --- Ellipse outline ---
    ax.plot(ex, ey, '-', color='gray', linewidth=1.5, zorder=3)

    # --- Iso-τ curves ---
    ax.plot(K_kJ, v_100s, '-', color=color_100s, linewidth=2.5,
            label=r'$\tau$ = 100 s', zorder=4)
    ax.plot(K_kJ, v_1Myr, '-', color=color_1Myr, linewidth=2.5,
            label=r'$\tau$ = 1 Myr', zorder=4)
    ax.plot(K_kJ, v_45Gyr, '-', color=color_45Gyr, linewidth=2.5,
            label=r'$\tau$ = 4.5 Gyr', zorder=4)

    # --- Region labels ---
    if show_vrm:
        ax.text(0.15, 0.015, 'Superparamagnetic', fontsize=11,
                color=color_100s, fontweight='bold')
        ax.text(cx - 0.2, 0.10, 'VRM', fontsize=15,
                fontweight='bold', color='#4a7c28',
                bbox=dict(facecolor='white', edgecolor='none',
                          alpha=0.8, pad=2))
        ax.text(cx + 0.1, ref_cy + 0.08, 'ChRM', fontsize=15,
                fontweight='bold', color='#B8860B',
                bbox=dict(facecolor='white', edgecolor='none',
                          alpha=0.8, pad=2))
    else:
        ax.text(0.15, 0.015, 'Superparamagnetic', fontsize=11,
                color=color_100s, fontweight='bold')
        ax.text(cx - 0.15, 0.07, 'VRM\nerased', fontsize=15,
                fontweight='bold', color=color_100s, fontstyle='italic',
                ha='center',
                bbox=dict(facecolor='white', edgecolor='none',
                          alpha=0.8, pad=2))
        ax.text(cx + 0.1, ref_cy + 0.08, 'ChRM\n(preserved)', fontsize=14,
                fontweight='bold', color='#B8860B', zorder=10,
                bbox=dict(facecolor='white', edgecolor='none',
                          alpha=0.9, pad=2))

    # --- Panel letter and temperature ---
    ax.text(0.03, 0.97, panel_label, fontsize=18, fontweight='bold',
            transform=ax.transAxes, va='top', ha='left')
    ax.text(0.50, 0.97, f'T = {T_C} °C', fontsize=16, fontweight='bold',
            transform=ax.transAxes, va='top', ha='center',
            bbox=dict(facecolor='white', edgecolor='#d6d3cd',
                      boxstyle='round,pad=0.4'))

    # --- Axis formatting ---
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_xlabel(r'Anisotropy Energy Density (kJ/m$^3$)', fontsize=14)
    ax.tick_params(axis='both', labelsize=12)
    ax.grid(True, linestyle='--', alpha=0.3)


# --- Build figure ---
fig, (ax_a, ax_b) = plt.subplots(1, 2, figsize=(13, 5.5))

draw_panel(ax_a, T_C=20, panel_label='a', show_vrm=True)
draw_panel(ax_b, T_C=300, panel_label='b', show_vrm=False)

ax_a.set_ylabel(r'Grain Volume (zm$^3$)', fontsize=14)
for a in (ax_a, ax_b):
    a.legend(fontsize=11, loc='upper right')

plt.tight_layout(w_pad=1.5)
fig.savefig('../book/figures/chapter9/vrm_demag.png', dpi=200,
            bbox_inches='tight', facecolor='white')

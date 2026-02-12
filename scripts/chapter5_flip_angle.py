"""
Generate corrected flipping field figure (bf.png) for Chapter 5.

Uses shape anisotropy K_u for a prolate magnetite spheroid (q=1.5)
consistent with the interactive widget, rather than magnetocrystalline K_1.

Left panel: schematic showing vertical grain with B at phi = 0, 45, 90 (clockwise from easy axis).
Right panel: flipping field curve.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# --- Physical constants and parameters ---
mu0 = 4 * np.pi * 1e-7
Ms = 480e3
q = 1.5

e = np.sqrt(1.0 - 1.0 / q**2)
N_a = (1.0 - e**2) / (2.0 * e**3) * (np.log((1.0 + e) / (1.0 - e)) - 2.0 * e)
N_b = (1.0 - N_a) / 2.0
K_u = 0.5 * mu0 * (N_b - N_a) * Ms**2
mu0Hk_mT = 2 * K_u / Ms * 1e3

print(f"K_u = {K_u:.0f} J/m³,  μ₀Hk = {mu0Hk_mT:.1f} mT")

# --- Flipping field curve ---
phi_deg = np.linspace(0.01, 89.999, 5000)
phi_rad = np.deg2rad(phi_deg)
mu0Hf_mT = (2 * K_u / Ms * 1e3 /
            (np.cos(phi_rad)**(2/3) + np.sin(phi_rad)**(2/3))**(3/2))

# --- Figure with two panels ---
fig = plt.figure(figsize=(10, 4.2))
gs = fig.add_gridspec(1, 2, width_ratios=[1, 2.8], wspace=0.3)
ax_schem = fig.add_subplot(gs[0, 0])
ax_plot = fig.add_subplot(gs[0, 1])

# =============================================
# LEFT PANEL: grain schematic
# =============================================
# Grain is vertical (long axis = easy axis along y)
ax_schem.set_xlim(-1.8, 1.8)
ax_schem.set_ylim(-1.8, 1.8)
ax_schem.set_aspect('equal')
ax_schem.axis('off')

# Prolate ellipse — long axis vertical, larger
ellipse = mpatches.Ellipse(
    (0, 0), width=3.0 / q, height=3.0,
    facecolor='#f5f0e0', edgecolor='0.4', linewidth=1.5
)
ax_schem.add_patch(ellipse)

# Easy axis dashed line (vertical)
ax_schem.plot([0, 0], [-1.85, 1.85], '--', color='0.6', linewidth=1.0, zorder=0)
ax_schem.text(0.12, -1.7, 'easy axis', fontsize=8, color='0.5',
              va='top', ha='left')

# B arrows from center of grain
# phi=0 → up (along easy axis), phi=90 → right, clockwise
# In standard coords: phi=0 is +y, phi clockwise means angle from +y toward +x
# So direction = (sin(phi), cos(phi))
phi_angles = [0, 45, 90]
arrow_len = 1.5

for phi_d in phi_angles:
    phi_r = np.deg2rad(phi_d)
    dx = arrow_len * np.sin(phi_r)
    dy = arrow_len * np.cos(phi_r)

    ax_schem.annotate('', xy=(dx, dy), xytext=(0, 0),
                      arrowprops=dict(arrowstyle='->', color='k', lw=1.8))

    # Label at arrow tip
    label_r = arrow_len + 0.18
    lx = label_r * np.sin(phi_r)
    ly = label_r * np.cos(phi_r)

    if phi_d == 0:
        ha, va = 'right', 'center'
        lx -= 0.08
    elif phi_d == 90:
        ha, va = 'left', 'top'
        ly -= 0.05
    else:
        ha, va = 'left', 'center'

    ax_schem.text(lx, ly, f'{phi_d}°', fontsize=10, color='k',
                  fontweight='bold', ha=ha, va=va)

# phi arc (from +y clockwise to 45°)
arc_r = 0.7
arc_theta = np.linspace(0, np.deg2rad(45), 50)
ax_schem.plot(arc_r * np.sin(arc_theta), arc_r * np.cos(arc_theta),
              '-', color='0.4', linewidth=0.8)
ax_schem.text(arc_r * 1.25 * np.sin(np.deg2rad(22)),
              arc_r * 1.25 * np.cos(np.deg2rad(22)),
              r'$\phi$', fontsize=12, color='0.3',
              ha='center', va='center')

# "B" label to the left of the arrows, between 0° and 45°
ax_schem.text(-0.45, 0.95, r'$\mathbf{B}$', fontsize=14, fontweight='bold',
              color='0.3', ha='center', va='center')

# =============================================
# RIGHT PANEL: flipping field curve
# =============================================
ax_plot.plot(phi_deg, mu0Hf_mT, 'k-', linewidth=2.0)

ax_plot.set_xlabel(r'$\phi$  (degrees)')
ax_plot.set_ylabel(r'$\mu_o H_f$  (mT)')
ax_plot.set_xlim(-1, 91)
ax_plot.set_ylim(0, 105)
ax_plot.set_xticks(np.arange(0, 91, 15))
ax_plot.set_yticks([0, 20, 40, 60, 80, 100])

# Parameter annotation
ax_plot.text(0.50, 0.07,
             f'Magnetite,  aspect ratio = {q}\n'
             r'$K_u$ = ' + f'{K_u/1e3:.1f}' + r'$\times 10^3$ J/m$^3$ (shape)' + '\n'
             r'$\mu_o H_k$ = ' + f'{mu0Hk_mT:.1f} mT',
             transform=ax_plot.transAxes, fontsize=11,
             verticalalignment='bottom', horizontalalignment='center',
             bbox=dict(boxstyle='round,pad=0.4', facecolor='white',
                       edgecolor='0.7', alpha=0.9))

plt.savefig('../book/figures/chapter5/bf.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
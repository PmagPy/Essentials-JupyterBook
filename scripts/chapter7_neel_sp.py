"""
Néel diagram with a hypothetical grain population.

Iso-tau curves (100 s, 1 Myr, 4.5 Gyr) at room temperature with an
elliptical grain population clipped into superparamagnetic (below the
100 s curve, blue hatched) and stable single-domain (above, gold) fields.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, PathPatch, Patch
from matplotlib.path import Path
from matplotlib.legend_handler import HandlerPatch

# --- Physical Constants ---
k_B = 1.380649e-23  # Boltzmann constant (J/K)
tau_0 = 1e-9        # Frequency factor (seconds), typical value for magnetite

# --- Wong (2011) colorblind-safe palette ---
tau_colors = {'1 ms': '#009E73', '100 s': '#0072B2', '1 Myr': '#E69F00', '4.5 Gyr': '#D55E00'}


def calculate_volume_for_relaxation(tau, K, T):
    """Rearranges the Neel equation to solve for Volume (v).

    Parameters:
        tau (float): The relaxation time in seconds.
        K (float or numpy.ndarray): The anisotropy constant in J/m^3.
        T (float): The temperature in Kelvin.

    Returns:
        float or numpy.ndarray: The calculated grain volume in m^3.
    """
    return (k_B * T * np.log(tau / tau_0)) / K


# --- Setup ---
T_room = 300  # Kelvin

taus = {
    '1 ms': 1e-3,
    '100 s': 100,
    '1 Myr': 1e6 * 365 * 24 * 3600,
    '4.5 Gyr': 4.5e9 * 365 * 24 * 3600
}

K_axis_kJ = np.linspace(0.01, 6.0, 1000)
K_axis_J = K_axis_kJ * 1000

# Pre-compute volume curves in zm³
v_curves = {}
for label, t_val in taus.items():
    v_m3 = calculate_volume_for_relaxation(t_val, K_axis_J, T_room)
    v_curves[label] = v_m3 * 1e21

# --- Curve label positions ---
label_settings = {
    '1 ms': {'x': 2.0, 'y': 0.026, 'angle': -3},
    '100 s':   {'x': 2.5, 'y': 0.044, 'angle': -5},
    '1 Myr':   {'x': 2.3, 'y': 0.09, 'angle': -13},
    '4.5 Gyr': {'x': 3.0, 'y': 0.088, 'angle': -8},
}

# --- Plot ---
fig, ax = plt.subplots(figsize=(10, 7))

# Iso-tau curves with inline labels
for label, t_val in taus.items():
    v_m3 = calculate_volume_for_relaxation(t_val, K_axis_J, T_room)
    ax.plot(K_axis_kJ, v_m3 * 1e21, color=tau_colors[label], linewidth=2.5)
    cfg = label_settings[label]
    ax.text(cfg['x'], cfg['y'], rf'$\tau$ = {label}',
            color=tau_colors[label], fontsize=14, fontweight='bold',
            rotation=cfg['angle'], ha='center', va='center',
            bbox=dict(facecolor='white', alpha=1.0, edgecolor='none', pad=1))

# Grain population ellipse clipped into SP and SSD fields
center_x, center_y = 1.1, 0.19
width, height = 1.5, 0.32

sp_verts = (list(zip(K_axis_kJ, v_curves['100 s']))
            + [(K_axis_kJ[-1], 0), (K_axis_kJ[0], 0)])
ssd_verts = (list(zip(K_axis_kJ, v_curves['100 s']))
             + [(K_axis_kJ[-1], 0.5), (K_axis_kJ[0], 0.5)])

ellipse_sp = Ellipse((center_x, center_y), width, height, angle=0,
                     facecolor='lightblue', edgecolor='gray', linewidth=1,
                     alpha=0.5, hatch='///')
ax.add_patch(ellipse_sp)
ellipse_sp.set_clip_path(PathPatch(Path(sp_verts), transform=ax.transData))

ellipse_ssd = Ellipse((center_x, center_y), width, height, angle=0,
                      facecolor='gold', edgecolor='gray', linewidth=1, alpha=0.5,
                      hatch='...')
ax.add_patch(ellipse_ssd)
ellipse_ssd.set_clip_path(PathPatch(Path(ssd_verts), transform=ax.transData))

ellipse_outline = Ellipse((center_x, center_y), width, height, angle=0,
                          facecolor='none', edgecolor='gray', linewidth=1.5)
ax.add_patch(ellipse_outline)

# Region labels
ax.text(0.37, 0.005, 'Superparamagnetic', rotation=-45, fontsize=14,
        ha='center', color='#333333')
ax.text(1.8, 0.23, 'Stable Single Domain', rotation=-45, fontsize=14,
        ha='center', color='#333333')

# Legend for grain population regions — custom handler to draw ellipses
class HandlerEllipse(HandlerPatch):
    def create_artists(self, legend, orig_handle, xdescent, ydescent,
                       width, height, fontsize, trans):
        center = 0.5 * width - 0.5 * xdescent, 0.5 * height - 0.5 * ydescent
        p = Ellipse(xy=center, width=width + xdescent, height=height + ydescent)
        self.update_prop(p, orig_handle, legend)
        p.set_transform(trans)
        return [p]

legend_elements = [
    Patch(facecolor='gold', edgecolor='gray', alpha=0.5, hatch='...',
          label='Grain population (stable single domain)'),
    Patch(facecolor='lightblue', edgecolor='gray', alpha=0.5, hatch='///',
          label='Grain population (superparamagnetic)'),
]
ax.legend(handles=legend_elements, fontsize=13, loc='upper right',
          handler_map={Patch: HandlerEllipse()}, handlelength=2.5, handleheight=1.7,
          borderpad=1.05, labelspacing=1.05)

# Axis formatting
ax.set_xlabel(r'Anisotropy energy density ($kJ/m^3$)', fontsize=16)
ax.set_ylabel(r'Grain volume ($zm^3$)', fontsize=16)
ax.set_xlim(0, 3.5)
ax.set_ylim(0, 0.5)
ax.tick_params(axis='both', labelsize=14)
ax.grid(True, linestyle='--', alpha=0.3)

fig.savefig('../book/figures/chapter7/neel_grain_population.png', dpi=200,
            bbox_inches='tight', facecolor='white')

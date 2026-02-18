"""
Néel diagram overlay plot showing iso-tau curves at two temperatures.

Plots relaxation time contours (100 s, 1 Myr, 4.5 Gyr) for both 20°C
(solid lines) and 550°C (dashed lines) on a single axis of grain volume
vs. anisotropy energy density.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# --- Physical Constants ---
k_B = 1.380649e-23  # Boltzmann constant (J/K)
tau_0 = 1e-9        # Frequency factor (seconds), typical value for magnetite


def calculate_volume_for_relaxation(tau, K, T):
    """Rearranges the Neel equation to solve for Volume (v).

    Calculates the grain volume required to maintain magnetization for a given
    relaxation time, based on the anisotropy and temperature.

    Parameters:
        tau (float): The relaxation time in seconds.
        K (float or numpy.ndarray): The anisotropy constant in J/m^3.
        T (float): The temperature in Kelvin.

    Returns:
        float or numpy.ndarray: The calculated grain volume in m^3.
    """
    v = (k_B * T * np.log(tau / tau_0)) / K
    return v


def plot_neel_curves(T_k, K_kJ, K_J, taus, tau_colors, ax,
                     linestyle='-', alpha=1.0, label_suffix='', show_legend_labels=True):
    """Plot iso-tau curves on a given axis for a specific temperature.

    Parameters
    ----------
    T_k : float
        Temperature in Kelvin.
    K_kJ, K_J : array-like
        Anisotropy values in kJ/m³ and J/m³.
    taus : dict
        {label: tau_seconds}.
    tau_colors : dict
        {label: color}.
    ax : matplotlib Axes
    linestyle : str
    alpha : float
    label_suffix : str
        Appended to legend labels (e.g. ' (550°C)').
    show_legend_labels : bool
        If False, sets label to '_nolegend_'.
    """
    for label, t_val in taus.items():
        v_m3 = calculate_volume_for_relaxation(t_val, K_J, T_k)
        leg = f'$\\tau$ = {label}{label_suffix}' if show_legend_labels else '_nolegend_'
        ax.plot(K_kJ, v_m3 * 1e21, color=tau_colors[label],
                linestyle=linestyle, linewidth=2.5, alpha=alpha, label=leg)


def format_neel_axes(ax, xlabel=True, ylabel=True, title='', xlim=(0, 4), ylim=(0, 0.5)):
    """Apply standard formatting to a Néel diagram axis."""
    if xlabel:
        ax.set_xlabel(r'Anisotropy energy density ($kJ/m^3$)', fontsize=16)
    if ylabel:
        ax.set_ylabel(r'Grain volume ($zm^3$)', fontsize=16)
    if title:
        ax.set_title(title, fontsize=18)
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.tick_params(axis='both', labelsize=14)
    ax.grid(True, linestyle='--', alpha=0.3)


# --- Setup ---
taus = {
    '100 s': 100,
    '1 Myr': 1e6 * 365 * 24 * 3600,
    '4.5 Gyr': 4.5e9 * 365 * 24 * 3600
}
tau_colors = {'100 s': '#0072B2', '1 Myr': '#E69F00', '4.5 Gyr': '#D55E00'}

T_high_K = 550 + 273.15
T_low_K = 20 + 273.15

K_axis_kJ = np.linspace(0.01, 6.0, 1000)
K_axis_J = K_axis_kJ * 1000

# --- Overlay plot with manual labels ---
manual_settings = {
    '100 s (20°C)':    {'x': 1.1, 'y': 0.095, 'angle': -25},
    '1 Myr (20°C)':    {'x': 1.3, 'y': 0.165, 'angle': -35},
    '4.5 Gyr (20°C)':  {'x': 0.84, 'y': 0.30, 'angle': -61},
    '100 s (550°C)':   {'x': 3.1, 'y': 0.095, 'angle': -9},
    '1 Myr (550°C)':   {'x': 3.6, 'y': 0.165, 'angle': -15},
    '4.5 Gyr (550°C)': {'x': 2.3, 'y': 0.30, 'angle': -36},
}

fig, ax = plt.subplots(figsize=(12, 8))
for T_k, lstyle, alpha_val, suffix in [(T_high_K, '--', 0.6, ' (550°C)'),
                                        (T_low_K, '-', 1.0, ' (20°C)')]:
    plot_neel_curves(T_k, K_axis_kJ, K_axis_J, taus, tau_colors, ax,
                     linestyle=lstyle, alpha=alpha_val, show_legend_labels=False)
    for label in taus:
        full_label = f'{label}{suffix}'
        if full_label in manual_settings:
            cfg = manual_settings[full_label]
            ax.text(cfg['x'], cfg['y'], full_label,
                    color=tau_colors[label], fontsize=15, fontweight='bold',
                    rotation=cfg['angle'], ha='center', va='center', alpha=alpha_val,
                    bbox=dict(facecolor='white', alpha=1.0, edgecolor='none', pad=3))

format_neel_axes(ax, xlim=(0, 4.5))

# Legend showing line style meaning
legend_elements = [
    Line2D([0], [0], color='black', linestyle='-', linewidth=2.5,
           label='Relaxation time curves at 20°C'),
    Line2D([0], [0], color='black', linestyle='--', linewidth=2.5, alpha=0.6,
           label='Relaxation time curves at 550°C'),
]
ax.legend(handles=legend_elements, fontsize=15, loc='upper right')

plt.tight_layout()
plt.savefig('../book/figures/chapter7/relaxation_time_curves_20C_550C.png', dpi=300)

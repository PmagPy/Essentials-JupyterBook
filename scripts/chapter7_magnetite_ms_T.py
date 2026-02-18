"""
Temperature dependence of saturation magnetization and anisotropy for magnetite.

Two-panel figure showing normalized Ms(T) and K(T) relative to room
temperature (20°C). Shape anisotropy scales as K ∝ Ms², so the energy
barrier grows faster than the magnetization itself during cooling.
"""

import numpy as np
import matplotlib.pyplot as plt

# --- Wong (2011) colorblind-safe palette ---
COLOR_BLUE = '#0072B2'
COLOR_VERMILLION = '#D55E00'

# --- Physical Constants for Magnetite ---
Tc = 580.0           # Curie temperature (°C)
Ms_0 = 480000.0      # Saturation magnetization at room temp (A/m)
K_0 = 25000.0        # Anisotropy constant at room temp (J/m³)
gamma = 0.38         # Exponent for magnetite

# --- Temperature arrays ---
T_celsius = np.linspace(0, Tc, 200)
T_kelvin = T_celsius + 273.15
Tc_kelvin = Tc + 273.15
T_room_k = 20 + 273.15  # Reference room temp (20°C)

# --- Ms(T) and K(T) ---
ms_actual = Ms_0 * ((Tc_kelvin - T_kelvin) / (Tc_kelvin - T_room_k))**gamma
ms_actual = np.maximum(ms_actual, 0)

# For shape anisotropy, K = 1/2 * dN * Ms^2
# Therefore K(T) scales with the square of Ms(T)
k_actual = K_0 * (ms_actual / Ms_0)**2

ms_norm = ms_actual / Ms_0
k_norm = k_actual / K_0

# --- Plot ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Saturation Magnetization
ax1.plot(T_celsius, ms_norm, color=COLOR_BLUE, linewidth=3)
ax1.set_xlabel('Temperature (\u00b0C)', fontsize=16)
ax1.set_ylabel(r'Normalized $M_s(T) / M_s(20^{\circ}C)$', fontsize=16)
ax1.set_title(r'Saturation Magnetization ($M_s$)', fontsize=18)
ax1.set_xlim(0, 600)
ax1.set_ylim(0, 1.1)
ax1.tick_params(axis='both', labelsize=14)
ax1.grid(True, linestyle='--', alpha=0.5)

# Anisotropy Energy
ax2.plot(T_celsius, k_norm, color=COLOR_VERMILLION, linewidth=3)
ax2.set_xlabel('Temperature (\u00b0C)', fontsize=16)
ax2.set_ylabel(r'Normalized $K(T) / K(20^{\circ}C)$', fontsize=16)
ax2.set_title(r'Anisotropy Energy Density ($K$)', fontsize=18)
ax2.set_xlim(0, 600)
ax2.set_ylim(0, 1.1)
ax2.tick_params(axis='both', labelsize=14)
ax2.grid(True, linestyle='--', alpha=0.5)

ax2.text(80, 0.5, r'$K \propto M_s^2$', fontsize=18, color=COLOR_VERMILLION)
ax2.text(80, 0.3, 'Energy barrier grows\nrapidly with cooling!', fontsize=14, color='#555')

fig.savefig('../book/figures/chapter7/magnetite_ms_k_temperature.png', dpi=200,
            bbox_inches='tight', facecolor='white')

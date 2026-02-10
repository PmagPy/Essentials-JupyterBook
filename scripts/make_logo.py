"""
Generate a geocentric axial dipole logo for the Essentials of Paleomagnetism JupyterBook.
Dipole field lines follow: r = r0 * sin^2(theta)
Output: book/_static/logo_placeholder.png
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from pathlib import Path

fig, ax = plt.subplots(figsize=(3, 3))

# Draw dipole field lines
# At Earth's surface (r=1): r0 = 1/sin^2(theta0), where theta0 is the colatitude
# Evenly space lines by colatitude of their exit point
theta = np.linspace(0.001, np.pi - 0.001, 2000)
exit_colats = np.linspace(5, 72.5, 10)  # degrees from pole to near-equator
r0_values = 1.0 / np.sin(np.radians(exit_colats)) ** 2

for r0 in r0_values:
    r = r0 * np.sin(theta) ** 2
    x = r * np.sin(theta)
    y = r * np.cos(theta)
    # Start lines slightly inside Earth so they visually meet the circle edge
    mask = r >= 0.98
    x_plot = np.where(mask, x, np.nan)
    y_plot = np.where(mask, y, np.nan)
    ax.plot(x_plot, y_plot, color='#2E5090', linewidth=1.2, solid_capstyle='round')
    ax.plot(-x_plot, y_plot, color='#2E5090', linewidth=1.2, solid_capstyle='round')

# Draw Earth
earth = Circle((0, 0), 1.0, facecolor='#D4E4F7', edgecolor='#2E5090', linewidth=2.0, zorder=5)
ax.add_patch(earth)

# Draw equator
ax.plot([-1.0, 1.0], [0, 0], color='#2E5090', linewidth=0.8, linestyle='--', zorder=6)

ax.set_xlim(-2.8, 2.8)
ax.set_ylim(-2.8, 2.8)
ax.set_aspect('equal')
ax.axis('off')

out_path = Path(__file__).resolve().parent.parent / 'book' / '_static' / 'logo_placeholder.png'
fig.savefig(out_path, dpi=200, bbox_inches='tight',
            transparent=True, pad_inches=0.05)
plt.close()
print(f"Logo saved to {out_path}")

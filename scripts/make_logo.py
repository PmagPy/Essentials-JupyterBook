"""
Generate a geocentric axial dipole logo for the Essentials of Paleomagnetism JupyterBook.
Dipole field lines follow: r = r0 * sin^2(theta)

JupyterBook 2 (MyST book-theme) sidebar is ~300px wide.
The logo image scales to fill that width (max-width: 100%).

Output: book/_static/logo_placeholder.png
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from pathlib import Path
from PIL import Image

fig = plt.figure(figsize=(8.0, 1.6))

# --- Dipole on the left ~20% of width, full height ---
ax_dipole = fig.add_axes([0.0, 0.0, 0.20, 1.0])

theta = np.linspace(0.001, np.pi - 0.001, 2000)
exit_colats = np.linspace(5, 72.5, 10)
r0_values = 1.0 / np.sin(np.radians(exit_colats)) ** 2

for r0 in r0_values:
    r = r0 * np.sin(theta) ** 2
    x = r * np.sin(theta)
    y = r * np.cos(theta)
    mask = r >= 0.98
    x_plot = np.where(mask, x, np.nan)
    y_plot = np.where(mask, y, np.nan)
    ax_dipole.plot(x_plot, y_plot, color='#2E5090', linewidth=1.5,
                   solid_capstyle='round')
    ax_dipole.plot(-x_plot, y_plot, color='#2E5090', linewidth=1.5,
                   solid_capstyle='round')

earth = Circle((0, 0), 1.0, facecolor='#D4E4F7', edgecolor='#2E5090',
               linewidth=2.5, zorder=5)
ax_dipole.add_patch(earth)
ax_dipole.plot([-1.0, 1.0], [0, 0], color='#2E5090', linewidth=1.0,
               linestyle='--', zorder=6)
ax_dipole.set_xlim(-1.9, 1.9)
ax_dipole.set_ylim(-1.3, 1.3)
ax_dipole.set_aspect('equal')
ax_dipole.axis('off')

# --- Text on the right ~80%, matching graphic height ---
ax_text = fig.add_axes([0.19, 0.0, 0.81, 1.0])
ax_text.set_xlim(0, 1)
ax_text.set_ylim(0, 1)
ax_text.axis('off')
ax_text.text(0.03, 0.68, 'ESSENTIALS',
             fontsize=36, fontweight='bold', color='#2E5090',
             fontfamily='sans-serif', va='center', ha='left')
ax_text.text(0.03, 0.30, 'OF PALEOMAGNETISM',
             fontsize=36, fontweight='bold', color='#2E5090',
             fontfamily='sans-serif', va='center', ha='left')

# Save to a temporary buffer, then crop to actual content
out_path = Path(__file__).resolve().parent.parent / 'book' / '_static' / 'logo_placeholder.png'
tmp_path = out_path.with_suffix('.tmp.png')
fig.savefig(tmp_path, dpi=200, bbox_inches='tight',
            transparent=True, pad_inches=0)
plt.close()

# Crop to ink with a small margin
img = Image.open(tmp_path)
arr = np.array(img)
content_mask = arr[:, :, 3] > 0  # non-transparent pixels
rows = np.any(content_mask, axis=1)
cols = np.any(content_mask, axis=0)
rmin, rmax = np.where(rows)[0][[0, -1]]
cmin, cmax = np.where(cols)[0][[0, -1]]
margin = 4  # px
crop_box = (max(0, cmin - margin),
            max(0, rmin - margin),
            min(img.width, cmax + margin + 1),
            min(img.height, rmax + margin + 1))
img.crop(crop_box).save(out_path)
tmp_path.unlink()

print(f"Logo saved to {out_path}")
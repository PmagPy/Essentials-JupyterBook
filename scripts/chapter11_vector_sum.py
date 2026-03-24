"""Generate Figure (vecsum_new.png): unit vectors summing to a resultant.

Eight unit vectors (m1-m8) arranged head-to-tail with random angular
deviations, and a bold red resultant vector R from the origin to the
final endpoint. Illustrates vector addition of directional data.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import numpy as np
import matplotlib.pyplot as plt
from figure_style import apply_mpl_style

apply_mpl_style()

# Random angular deviations from horizontal with more scatter
rng = np.random.default_rng(seed=37)
N = 8
angles_deg = rng.uniform(-30, 30, size=N)
angles = np.radians(angles_deg)

# Build head-to-tail chain of unit vectors
points = np.zeros((N + 1, 2))
for i in range(N):
    dx = np.cos(angles[i])
    dy = np.sin(angles[i])
    points[i + 1] = points[i] + np.array([dx, dy])

# Colors
ARROW_COLOR = 'black'
RESULTANT_COLOR = '#CC0000'

fig, ax = plt.subplots(figsize=(10, 3.5))

# Draw individual unit vectors with sharp triangular arrowheads
for i in range(N):
    x0, y0 = points[i]
    x1, y1 = points[i + 1]
    ax.annotate('', xy=(x1, y1), xytext=(x0, y0),
                arrowprops=dict(
                    arrowstyle='->,head_width=0.25,head_length=0.3',
                    color=ARROW_COLOR,
                    linewidth=1.8,
                    shrinkA=0, shrinkB=0,
                ),
                zorder=3)

    # Label position: offset above each vector's midpoint
    mx = (x0 + x1) / 2
    my = (y0 + y1) / 2
    # Offset label above or below based on vector vertical component
    # Force m3, m5, m6, m8 above their arrows
    if i in (2, 4, 5, 7):
        label_offset = 0.3
    else:
        label_offset = 0.3 if np.sin(angles[i]) >= 0 else -0.35
    ax.text(mx, my + label_offset, f'$m_{{{i + 1}}}$',
            fontsize=14, ha='center', va='center', zorder=4)

# Draw resultant vector R (bold red arrow)
ax.annotate('', xy=(points[-1, 0], points[-1, 1]),
            xytext=(points[0, 0], points[0, 1]),
            arrowprops=dict(
                arrowstyle='->,head_width=0.3,head_length=0.8',
                color=RESULTANT_COLOR,
                linewidth=5,
                shrinkA=0, shrinkB=0,
            ),
            zorder=2)

# Label R below the resultant arrow, centered
rx = points[0, 0] + 0.5 * (points[-1, 0] - points[0, 0])
ry_on_line = points[0, 1] + 0.5 * (points[-1, 1] - points[0, 1])
ry = ry_on_line - 0.45
ax.text(rx, ry, r'$\mathbf{R}$', fontsize=20, fontweight='bold',
        ha='center', va='center', color=RESULTANT_COLOR, zorder=4)

# Clean up axes
ax.set_aspect('equal')
ax.axis('off')

# Set limits with padding
xmin, xmax = points[:, 0].min() - 0.4, points[:, 0].max() + 0.6
ymin, ymax = points[:, 1].min() - 0.7, points[:, 1].max() + 0.7
ax.set_xlim(xmin, xmax)
ax.set_ylim(ymin, ymax)

outpath = os.path.join(os.path.dirname(__file__),
                       '..', 'book', 'figures', 'chapter11', 'vecsum.png')
fig.savefig(outpath, dpi=300, bbox_inches='tight', transparent=True)
plt.close()
print(f"Saved {outpath}")

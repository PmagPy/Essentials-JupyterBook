#!/usr/bin/env python
"""
Create the composite Chinese compass figure for Chapter 14.

Combines:
a) Photo of the south-pointing spoon reconstruction
b) Plot of Chinese declination measurements from 720 CE to 1829

Data source: Smith and Needham (1967), via chinesedec.dat in the Essentials of Paleomagnetism repository.
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from pathlib import Path

# Paths
PROJECT_ROOT = Path(__file__).parent.parent
ORIGINAL_REPO = PROJECT_ROOT.parent / "Essentials-of-Paleomagnetism"
OUTPUT_DIR = PROJECT_ROOT / "book" / "figures" / "chapter14"

# Input files
SPOON_IMAGE = ORIGINAL_REPO / "Codes" / "Chapter14" / "compass1.jpg"

# Chinese declination data from Smith and Needham (1967)
# Format: year, declination (degrees)
CHINESE_DEC_DATA = """
722.9	3.786
851.9	15.19
902.8	8.121
1034	-0.8497
1035	-0.8509
1095	-7.395
1117	-14.76
1183	-7.048
1237	-6.831
1287	-7.092
1585	-7.319
1630	-6.235
1682	-2.154
1685	-2.962
1713	-1.701
1716	-2.562
1819	0.4516
1835	-1.012
"""


def load_declination_data():
    """Parse the Chinese declination data."""
    years = []
    decs = []
    for line in CHINESE_DEC_DATA.strip().split('\n'):
        parts = line.split()
        years.append(float(parts[0]))
        decs.append(float(parts[1]))
    return np.array(years), np.array(decs)


def create_figure():
    """Create the composite figure."""
    # Load data
    years, decs = load_declination_data()

    # Create figure with two panels side by side
    fig = plt.figure(figsize=(12, 5))

    # Panel a: Spoon image
    ax1 = fig.add_subplot(1, 2, 1)
    img = mpimg.imread(SPOON_IMAGE)
    ax1.imshow(img)
    ax1.axis('off')
    ax1.set_title('a)', loc='left', fontsize=14, fontweight='bold')

    # Panel b: Declination plot
    ax2 = fig.add_subplot(1, 2, 2)
    ax2.scatter(years, decs, s=50, c='black', zorder=5)
    ax2.axhline(y=0, color='gray', linestyle='--', linewidth=0.8)
    ax2.set_xlabel('Year (CE)', fontsize=12)
    ax2.set_ylabel('Magnetic Declination (°)', fontsize=12)
    ax2.set_xlim(700, 1900)
    ax2.set_ylim(-20, 20)
    ax2.set_title('b)', loc='left', fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3)

    # Adjust layout
    plt.tight_layout()

    # Save figure
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_path = OUTPUT_DIR / "chinesecompass.png"
    fig.savefig(output_path, dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    print(f"Saved: {output_path}")

    plt.close()


if __name__ == "__main__":
    create_figure()

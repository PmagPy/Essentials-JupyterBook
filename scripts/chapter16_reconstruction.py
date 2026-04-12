"""Generate a CEED6 paleogeographic reconstruction figure for Chapter 16.

Shows present-day and 200 Ma reconstructions side by side using the CEED6
plate model of Torsvik & Cocks (2017) in a paleomagnetic (spin axis)
reference frame. North America and Eurasia are highlighted to connect
with the Euler-pole discussion in the chapter.

Requires pygplates and the CEED6 model files in scripts/data/CEED6/.

Reference:
    Torsvik, T.H. and Cocks, L.R.M. (2017), Earth History and
    Palaeogeography, Cambridge University Press.
"""

import os
import sys
sys.path.insert(0, os.path.dirname(__file__))

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import pygplates
from shapely.geometry import Polygon as ShapelyPolygon

from figure_style import apply_mpl_style

apply_mpl_style()

# --- Load CEED6 model ---
script_dir = os.path.dirname(os.path.abspath(__file__))
ceed6_dir = os.path.join(script_dir, 'data', 'CEED6')
poly_file = os.path.join(ceed6_dir, 'CEED6_POLY.shp')
land_file = os.path.join(ceed6_dir, 'CEED6_LAND.gpml')
rot_file = os.path.join(ceed6_dir, 'TC2017.rot')

polygons = pygplates.FeatureCollection(poly_file)
coastlines = pygplates.FeatureCollection(land_file)
rotation_model = pygplates.RotationModel(rot_file)

print(f"Loaded CEED6: {len(list(pygplates.FeatureCollection(poly_file)))} "
      f"polygon features, "
      f"{len(list(pygplates.FeatureCollection(land_file)))} land features")


def get_reconstructed_segments(fc, rm, time_ma, anchor_plate_id=1):
    """Return (lats, lons) segments of reconstructed features."""
    reconstructed = []
    pygplates.reconstruct(fc, rm, reconstructed, time_ma,
                          anchor_plate_id=anchor_plate_id)
    segs = []
    for rf in reconstructed:
        geom = rf.get_reconstructed_geometry()
        pts = geom.to_lat_lon_array()
        segs.append((pts[:, 0], pts[:, 1]))
    return segs


def reconstruct_as_shapely(fc, rm, time_ma, plate_ids=None,
                           anchor_plate_id=1):
    """Reconstruct features and return as (shapely_polygon, plate_id) list."""
    reconstructed = []
    pygplates.reconstruct(fc, rm, reconstructed, time_ma,
                          anchor_plate_id=anchor_plate_id)
    results = []
    for rf in reconstructed:
        pid = rf.get_feature().get_reconstruction_plate_id()
        if plate_ids is not None and pid not in plate_ids:
            continue
        geom = rf.get_reconstructed_geometry()
        pts = geom.to_lat_lon_array()
        if len(pts) >= 3:
            coords = list(zip(pts[:, 1], pts[:, 0]))  # (lon, lat)
            try:
                poly = ShapelyPolygon(coords)
                if poly.is_valid:
                    results.append((poly, pid))
            except Exception:
                pass
    return results


# --- Figure ---
fig, (ax0, ax200) = plt.subplots(
    1, 2, figsize=(16, 8),
    subplot_kw={'projection': ccrs.Orthographic(
        central_longitude=-30, central_latitude=30)})

# Paleomagnetic (spin axis) reference frame = plate 1 in CEED6
anchor_plate = 1

for ax, time_ma, title in [(ax0, 0, 'Present day (0 Ma)'),
                           (ax200, 200, '200 Ma (Pangea)')]:
    ax.set_global()
    ax.add_feature(cfeature.OCEAN, facecolor='#f2f7fc')
    ax.gridlines(color='0.8', linestyle=':', linewidth=0.5)

    # All continental polygons in grey
    all_polys = reconstruct_as_shapely(polygons, rotation_model, time_ma,
                                       anchor_plate_id=anchor_plate)
    print(f"  {time_ma} Ma: {len(all_polys)} valid polygons")
    grey_geoms = [p for p, _ in all_polys]
    ax.add_geometries(grey_geoms, crs=ccrs.PlateCarree(),
                      facecolor='0.90', edgecolor='0.6', linewidth=0.3,
                      zorder=2)

    # NAM and EUR blocks highlighted
    for plate_ids, fc_color, ec_color, label in [
        ({101}, '#e8c4c4', '#a01020', 'NAM'),
        ({301, 302}, '#c4cce8', '#202080', 'EUR'),
    ]:
        plate_polys = reconstruct_as_shapely(
            polygons, rotation_model, time_ma,
            plate_ids=plate_ids, anchor_plate_id=anchor_plate)
        print(f"    {label}: {len(plate_polys)} polygons")
        if plate_polys:
            ax.add_geometries([p for p, _ in plate_polys],
                              crs=ccrs.PlateCarree(),
                              facecolor=fc_color, edgecolor=ec_color,
                              linewidth=0.8, zorder=3)

    # Coastlines on top
    coast_segs = get_reconstructed_segments(coastlines, rotation_model,
                                           time_ma,
                                           anchor_plate_id=anchor_plate)
    print(f"    coastlines: {len(coast_segs)} segments")
    for lats, lons in coast_segs:
        ax.plot(lons, lats, color='0.3', linewidth=0.4,
                transform=ccrs.Geodetic(), zorder=4)

    ax.set_title(title, fontsize=18, fontweight='bold')

# Legend
legend_handles = [
    Patch(facecolor='#e8c4c4', edgecolor='#a01020', linewidth=1.5,
          label='North America (plate 101)'),
    Patch(facecolor='#c4cce8', edgecolor='#202080', linewidth=1.5,
          label='Europe (plates 301/302)'),
    Patch(facecolor='0.90', edgecolor='0.6', linewidth=1.0,
          label='Other continental blocks'),
]
fig.legend(handles=legend_handles, loc='lower center',
           ncol=3, fontsize=16, frameon=True, framealpha=0.95,
           bbox_to_anchor=(0.5, -0.02))

plt.tight_layout()

outpath = os.path.join(
    script_dir, '..', 'book', 'figures', 'chapter16',
    'reconstruction.png'
)
fig.savefig(outpath, dpi=300, bbox_inches='tight')
plt.close(fig)
print(f"Saved {outpath}")

"""Generate plates_new.png: Major lithospheric plates map.

Mollweide map of the major lithospheric plates with plate boundaries
drawn from the PB2002 step-level data (Bird 2003). Sparsely placed arrow
pairs show the *sense* of relative motion across major-plate boundaries:
divergent (blue, arrows apart) on spreading ridges, convergent (orange,
arrows together) on subduction zones and continental collisions.

References:
    Bird, P. (2003), An updated digital model of plate boundaries,
    Geochem. Geophys. Geosyst., 4, 1027, doi:10.1029/2001GC000252.
"""

import json
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))

from collections import defaultdict

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.feature import ShapelyFeature
from shapely.geometry import shape, MultiPolygon, LineString
from shapely.ops import transform as shp_transform
import pyproj

from figure_style import apply_mpl_style

apply_mpl_style()


# ===================================================================
# Utility functions
# ===================================================================

def _vertex_spherical_mean(geom):
    """Crude spherical mean of polygon vertices (starting guess for LAEA)."""
    polys = list(geom.geoms) if isinstance(geom, MultiPolygon) else [geom]
    coords = []
    for p in polys:
        coords.extend(p.exterior.coords)
    arr = np.array(coords)
    lons = np.radians(arr[:, 0])
    lats = np.radians(arr[:, 1])
    x = np.cos(lats) * np.cos(lons)
    y = np.cos(lats) * np.sin(lons)
    z = np.sin(lats)
    cx, cy, cz = x.mean(), y.mean(), z.mean()
    lon = float(np.degrees(np.arctan2(cy, cx)))
    lat = float(np.degrees(np.arctan2(cz, np.sqrt(cx ** 2 + cy ** 2))))
    return lon, lat


def area_centroid(geom, max_iter=5, tol=0.01):
    """Area-weighted spherical centroid via iterative LAEA projection."""
    lon0, lat0 = _vertex_spherical_mean(geom)
    wgs = pyproj.Proj(proj='latlong', R=6371000)
    for _ in range(max_iter):
        proj = pyproj.Proj(proj='laea', lat_0=lat0, lon_0=lon0, R=6371000)
        fwd = pyproj.Transformer.from_proj(wgs, proj, always_xy=True).transform
        inv = pyproj.Transformer.from_proj(proj, wgs, always_xy=True).transform
        proj_geom = shp_transform(fwd, geom)
        c = proj_geom.centroid
        new_lon, new_lat = inv(c.x, c.y)
        if abs(new_lon - lon0) < tol and abs(new_lat - lat0) < tol:
            return new_lon, new_lat
        lon0, lat0 = new_lon, new_lat
    return lon0, lat0


def _angular_distance(lat1, lon1, lat2, lon2):
    """Great-circle distance in degrees between two points."""
    lat1, lon1, lat2, lon2 = map(np.radians, (lat1, lon1, lat2, lon2))
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = (np.sin(dlat / 2) ** 2
         + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2) ** 2)
    return np.degrees(2 * np.arcsin(np.sqrt(a)))


# ===================================================================
# Load data
# ===================================================================

script_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(script_dir, 'data')
with open(os.path.join(data_dir, 'PB2002_plates.json')) as f:
    plates = json.load(f)
with open(os.path.join(data_dir, 'PB2002_steps.json')) as f:
    steps = json.load(f)

plate_geoms = {
    feat['properties']['PlateName']: shape(feat['geometry'])
    for feat in plates['features']
}

# Boundary segments as LineStrings (using step data)
boundary_segments = []
for feat in steps['features']:
    p = feat['properties']
    if abs(p['STARTLONG'] - p['FINALLONG']) > 180:
        continue
    boundary_segments.append(LineString([
        (p['STARTLONG'], p['STARTLAT']),
        (p['FINALLONG'], p['FINALLAT']),
    ]))


# ===================================================================
# Divergent / convergent arrow data
# ===================================================================

MAJOR_PLATES = {
    'NA', 'EU', 'PA', 'SA', 'AF', 'SO', 'IN', 'AU', 'AN', 'NZ',
    'SU', 'OK', 'PS', 'KE', 'AR', 'CO', 'CA', 'JF',
}

boundary_steps = defaultdict(list)
for feat in steps['features']:
    p = feat['properties']
    boundary_steps[p.get('PLATEBOUND', '')].append(p)

arrow_samples = []
for pb, step_list in boundary_steps.items():
    pair_str = pb.replace('/', '-')
    parts = pair_str.split('-')
    if len(parts) != 2:
        continue
    a, b = parts
    if a not in MAJOR_PLATES or b not in MAJOR_PLATES:
        continue

    div_km = sum(s['STEPLENGTH'] for s in step_list
                 if s.get('STEPCLASS') in ('OSR', 'CRB'))
    conv_km = sum(s['STEPLENGTH'] for s in step_list
                  if s.get('STEPCLASS') in ('SUB', 'CCB'))
    if div_km > conv_km and div_km > 0:
        motion = 'divergent'
    elif conv_km > div_km and conv_km > 0:
        motion = 'convergent'
    else:
        continue

    if motion == 'divergent':
        motion_steps = [s for s in step_list
                        if s.get('STEPCLASS') in ('OSR', 'CRB')]
    else:
        motion_steps = [s for s in step_list
                        if s.get('STEPCLASS') in ('SUB', 'CCB')]
    if not motion_steps:
        continue

    total_km = sum(s['STEPLENGTH'] for s in motion_steps)
    half_total = total_km / 2.0
    cumul = 0.0
    mid_step = motion_steps[len(motion_steps) // 2]
    for s in motion_steps:
        cumul += s['STEPLENGTH']
        if cumul >= half_total:
            mid_step = s
            break

    lat = 0.5 * (mid_step['STARTLAT'] + mid_step['FINALLAT'])
    lon = 0.5 * (mid_step['STARTLONG'] + mid_step['FINALLONG'])
    if abs(mid_step['STARTLONG'] - mid_step['FINALLONG']) > 180:
        continue
    arrow_samples.append((lat, lon, mid_step['AZIMUTHCEN'],
                          mid_step['VELOCITYLE'], motion))

# Thin to minimum 10-degree spacing
MIN_SPACING_DEG = 10.0
thinned = []
for sample in arrow_samples:
    lat_s, lon_s = sample[0], sample[1]
    too_close = any(
        _angular_distance(lat_s, lon_s, k[0], k[1]) < MIN_SPACING_DEG
        for k in thinned
    )
    if not too_close:
        thinned.append(sample)
arrow_samples = thinned


# ===================================================================
# Figure: Plates map
# ===================================================================

fig = plt.figure(figsize=(12, 6.5))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.Mollweide(central_longitude=0))
ax.set_global()
ax.add_feature(cfeature.OCEAN, facecolor='#f2f7fc', zorder=0)
ax.add_feature(cfeature.LAND, facecolor='#ede0c0', edgecolor='#9c8a63',
               linewidth=0.4, zorder=1)
ax.add_feature(ShapelyFeature(boundary_segments, ccrs.PlateCarree()),
               edgecolor='#7a1f1f', facecolor='none', linewidth=1.6,
               zorder=3)

# Divergent / convergent arrows
DIVERGENT_COLOR = '#0072B2'
CONVERGENT_COLOR = '#009E73'
HALF_ARROW_M = 700_000

for lat, lon, az_bound, v_le, motion in arrow_samples:
    az_rad = np.radians(az_bound)
    perp_e = np.cos(az_rad)
    perp_n = -np.sin(az_rad)

    p_c = np.array(ax.projection.transform_point(
        lon, lat, ccrs.PlateCarree()))
    eps = 0.5
    cos_lat = max(np.cos(np.radians(lat)), 0.05)
    p_perp = np.array(ax.projection.transform_point(
        lon + perp_e * eps / cos_lat,
        lat + perp_n * eps,
        ccrs.PlateCarree()))

    d = p_perp - p_c
    d_len = np.sqrt(d[0] ** 2 + d[1] ** 2)
    if d_len < 1:
        continue
    d_hat = d / d_len

    p_a = tuple(p_c - d_hat * HALF_ARROW_M)
    p_b = tuple(p_c + d_hat * HALF_ARROW_M)
    p_c = tuple(p_c)

    if motion == 'divergent':
        for p_end in (p_a, p_b):
            ax.add_patch(FancyArrowPatch(
                p_c, p_end, arrowstyle='->',
                mutation_scale=12, color=DIVERGENT_COLOR,
                lw=1.6, zorder=4,
            ))
    else:
        for p_start in (p_a, p_b):
            ax.add_patch(FancyArrowPatch(
                p_start, p_c, arrowstyle='->',
                mutation_scale=12, color=CONVERGENT_COLOR,
                lw=1.6, zorder=4,
            ))

# Plate labels
label_plates = [
    ('North\nAmerican', 'North America', (0, 0)),
    ('Eurasian',        'Eurasia',       (0, 0)),
    ('Pacific',         'Pacific',       (0, 0)),
    ('South\nAmerican', 'South America', (0, 0)),
    ('African',         'Africa',        (0, 0)),
    ('Indian',          'India',         (0, 0)),
    ('Somali',          'Somalia',       (0, 0)),
    ('Australian',      'Australia',     (0, 0)),
    ('Antarctic',       'Antarctica',    (0, 8)),
]

for display_name, plate_name, (dlon, dlat) in label_plates:
    clon, clat = area_centroid(plate_geoms[plate_name])
    clon += dlon
    clat += dlat
    ax.text(
        clon, clat, display_name,
        transform=ccrs.PlateCarree(),
        ha='center', va='center',
        fontsize=18, color='black',
        bbox=dict(facecolor='white', edgecolor='none', pad=1.5),
        zorder=5,
    )

fig.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.01)
outpath = os.path.join(
    script_dir, '..', 'book', 'figures', 'chapter16', 'plates_new.png'
)
fig.savefig(outpath, dpi=300, bbox_inches='tight')
plt.close(fig)
print(f"Saved {outpath}")
print(f"  boundary segments: {len(boundary_segments)}")
print(f"  arrow samples: {len(arrow_samples)} "
      f"(div={sum(1 for a in arrow_samples if a[4] == 'divergent')}, "
      f"conv={sum(1 for a in arrow_samples if a[4] == 'convergent')})")

"""Generate Figure 16.2 (plates_new.png): Major lithospheric plates and
Euler-pole velocity field.

Panel a — Mollweide map of the major lithospheric plates with plate
boundaries drawn from the PB2002 step-level data (Bird 2003). Sparsely
placed arrow pairs show the *sense* of relative motion across
major-plate boundaries: divergent (blue, arrows apart) on spreading
ridges, convergent (orange, arrows together) on subduction zones and
continental collisions.

Panel b — Orthographic view showing the motion of North America relative
to fixed Eurasia, computed from the NUVEL-1A Euler pole. Velocity arrows
(red) are plotted at grid points inside the North America polygon, with
length proportional to speed. Small circles around the Euler pole show
lines of constant angular distance theta.

References:
    Bird, P. (2003), An updated digital model of plate boundaries,
    Geochem. Geophys. Geosyst., 4, 1027, doi:10.1029/2001GC000252.

    DeMets, C. et al. (1994), Effect of recent revisions to the
    geomagnetic reversal time scale on estimates of current plate
    motions, Geophys. Res. Lett., 21, 2191-2194.
"""

import json
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))

from collections import defaultdict

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import matplotlib.gridspec as gridspec
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.feature import ShapelyFeature
from shapely.geometry import shape, MultiPolygon, LineString, Point
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


def euler_velocity_vector(point_lat, point_lon, euler_lat, euler_lon,
                          omega_deg_per_myr, earth_radius_km=6371.0):
    """Return (east, north) velocity components in cm/yr at a point
    due to an Euler rotation."""
    omega_rad_per_yr = np.radians(omega_deg_per_myr) / 1e6

    def sph_to_cart(lat, lon):
        lat_r, lon_r = np.radians(lat), np.radians(lon)
        return np.array([np.cos(lat_r) * np.cos(lon_r),
                         np.cos(lat_r) * np.sin(lon_r),
                         np.sin(lat_r)])

    e = sph_to_cart(euler_lat, euler_lon)
    p = sph_to_cart(point_lat, point_lon)
    v_cart = np.cross(omega_rad_per_yr * e, earth_radius_km * p) * 1e5

    lat_r, lon_r = np.radians(point_lat), np.radians(point_lon)
    east_hat = np.array([-np.sin(lon_r), np.cos(lon_r), 0.0])
    north_hat = np.array([-np.sin(lat_r) * np.cos(lon_r),
                          -np.sin(lat_r) * np.sin(lon_r),
                          np.cos(lat_r)])
    return float(np.dot(v_cart, east_hat)), float(np.dot(v_cart, north_hat))


def point_from_pole(pole_lat, pole_lon, theta_deg, bearing_deg):
    """Point at angular distance theta and bearing from a pole."""
    lat_e = np.radians(pole_lat)
    lon_e = np.radians(pole_lon)
    t = np.radians(theta_deg)
    b = np.radians(bearing_deg)
    lat = np.arcsin(np.sin(lat_e) * np.cos(t)
                    + np.cos(lat_e) * np.sin(t) * np.cos(b))
    lon = lon_e + np.arctan2(
        np.sin(b) * np.sin(t) * np.cos(lat_e),
        np.cos(t) - np.sin(lat_e) * np.sin(lat))
    return float(np.degrees(lat)), \
        float(((np.degrees(lon) + 180) % 360) - 180)


def gc_advance(start_lat, start_lon, bearing_deg, arc_deg):
    """Advance a point along a great circle by arc_deg degrees."""
    lat_r = np.radians(start_lat)
    lon_r = np.radians(start_lon)
    b = np.radians(bearing_deg)
    d = np.radians(arc_deg)
    new_lat = np.arcsin(np.sin(lat_r) * np.cos(d)
                        + np.cos(lat_r) * np.sin(d) * np.cos(b))
    new_lon = lon_r + np.arctan2(
        np.sin(b) * np.sin(d) * np.cos(lat_r),
        np.cos(d) - np.sin(lat_r) * np.sin(new_lat))
    return float(np.degrees(new_lat)), \
        float(((np.degrees(new_lon) + 180) % 360) - 180)


# ===================================================================
# Load data
# ===================================================================

script_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(script_dir, 'data')
with open(os.path.join(data_dir, 'PB2002_plates.json')) as f:
    plates = json.load(f)
with open(os.path.join(data_dir, 'PB2002_steps.json')) as f:
    steps = json.load(f)
with open(os.path.join(data_dir, 'PB2002_boundaries.json')) as f:
    boundaries = json.load(f)

plate_geoms = {
    feat['properties']['PlateName']: shape(feat['geometry'])
    for feat in plates['features']
}

# Boundary segments as LineStrings (for panel a, using step data)
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
# Panel a: divergent / convergent arrow data
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
# Panel b: Euler-pole velocity grid for NAM relative to EUR
# ===================================================================

# NUVEL-1A EURA-NOAM pole. Negated omega → NAM moving relative to
# fixed EUR, so arrows sit on the moving plate (North America).
EULER_LAT, EULER_LON, OMEGA = 62.4, 135.8, -0.21  # deg, deg, deg/Myr

# Grid concentric around the Euler pole
base_bearing_step = 7.0
raw_grid = []
for theta in np.arange(14, 103, 7):
    step = base_bearing_step / max(np.sin(np.radians(theta)), 0.15)
    for bearing in np.arange(0, 360, step):
        raw_grid.append(point_from_pole(EULER_LAT, EULER_LON, theta, bearing))
raw_lats = np.array([p[0] for p in raw_grid])
raw_lons = np.array([p[1] for p in raw_grid])

# Filter to points inside the North America polygon
nam_polygon = plate_geoms['North America']
inside_nam = np.array([nam_polygon.covers(Point(lon, lat))
                       for lat, lon in zip(raw_lats, raw_lons)])
below_polar_cap = raw_lats < 84.0
keep = inside_nam & below_polar_cap
grid_lats = raw_lats[keep]
grid_lons = raw_lons[keep]

# Compute velocity arrows as great-circle displacements
ARC_PER_CMYR = 2.5
euler_arrows = []  # (start_lat, start_lon, end_lat, end_lon)
for i in range(len(grid_lats)):
    u_e, v_n = euler_velocity_vector(
        grid_lats[i], grid_lons[i], EULER_LAT, EULER_LON, OMEGA)
    speed = np.hypot(u_e, v_n)
    if speed < 1e-6:
        continue
    bearing = (np.degrees(np.arctan2(u_e, v_n)) + 360) % 360
    arc = speed * ARC_PER_CMYR
    end_lat, end_lon = gc_advance(grid_lats[i], grid_lons[i], bearing, arc)
    euler_arrows.append((grid_lats[i], grid_lons[i], end_lat, end_lon))

# Boundary segments for panel b (from boundaries.json, with dateline fix)
def _pb2002_boundary_segments():
    for feat in boundaries['features']:
        geom = feat['geometry']
        if geom['type'] != 'LineString':
            continue
        coords = np.array(geom['coordinates'])
        if coords.size == 0:
            continue
        dlon = np.diff(coords[:, 0])
        breakpoints = np.where(np.abs(dlon) > 180)[0] + 1
        start = 0
        for bp in list(breakpoints) + [len(coords)]:
            sub = coords[start:bp]
            if len(sub) >= 2:
                yield sub[:, 0], sub[:, 1]
            start = bp


# ===================================================================
# Figure 1: Plates map
# ===================================================================

fig1 = plt.figure(figsize=(12, 6.5))
ax1 = fig1.add_subplot(1, 1, 1, projection=ccrs.Mollweide(central_longitude=0))
ax1.set_global()
ax1.add_feature(cfeature.OCEAN, facecolor='#f2f7fc', zorder=0)
ax1.add_feature(cfeature.LAND, facecolor='#ede0c0', edgecolor='#9c8a63',
                linewidth=0.4, zorder=1)
ax1.add_feature(ShapelyFeature(boundary_segments, ccrs.PlateCarree()),
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

    p_c = np.array(ax1.projection.transform_point(
        lon, lat, ccrs.PlateCarree()))
    eps = 0.5
    cos_lat = max(np.cos(np.radians(lat)), 0.05)
    p_perp = np.array(ax1.projection.transform_point(
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
            ax1.add_patch(FancyArrowPatch(
                p_c, p_end, arrowstyle='->',
                mutation_scale=12, color=DIVERGENT_COLOR,
                lw=1.6, zorder=4,
            ))
    else:
        for p_start in (p_a, p_b):
            ax1.add_patch(FancyArrowPatch(
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
    ax1.text(
        clon, clat, display_name,
        transform=ccrs.PlateCarree(),
        ha='center', va='center',
        fontsize=18, color='black',
        bbox=dict(facecolor='white', edgecolor='none', pad=1.5),
        zorder=5,
    )

fig1.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.01)
outpath1 = os.path.join(
    script_dir, '..', 'book', 'figures', 'chapter16', 'plates_new.png'
)
fig1.savefig(outpath1, dpi=300, bbox_inches='tight')
plt.close(fig1)
print(f"Saved {outpath1}")
print(f"  boundary segments: {len(boundary_segments)}")
print(f"  arrow samples: {len(arrow_samples)} "
      f"(div={sum(1 for a in arrow_samples if a[4] == 'divergent')}, "
      f"conv={sum(1 for a in arrow_samples if a[4] == 'convergent')})")


# ===================================================================
# Figure 2: Euler-pole velocity field
# ===================================================================

proj_b = ccrs.Orthographic(central_longitude=-114.4, central_latitude=62.5)
fig2 = plt.figure(figsize=(10, 10))
ax2 = fig2.add_subplot(1, 1, 1, projection=proj_b)
ax2.set_global()
ax2.add_feature(cfeature.OCEAN, facecolor='#f2f7fc')
ax2.add_feature(cfeature.LAND, facecolor='#ede0c0', edgecolor='#9c8a63',
                linewidth=0.4)
ax2.gridlines(color='0.75', linestyle=':', linewidth=0.5)

# Plate boundaries (simple grey)
for lons, lats in _pb2002_boundary_segments():
    ax2.plot(lons, lats, color='#555555', linewidth=0.8,
             transform=ccrs.Geodetic(), zorder=2)

# Small circles around the Euler pole
bearings = np.radians(np.linspace(-180, 180, 361))
lat_r, lon_r = np.radians(EULER_LAT), np.radians(EULER_LON)
for theta_deg in [30, 60, 90, 120, 150]:
    t = np.radians(theta_deg)
    sc_lat = np.degrees(np.arcsin(
        np.sin(lat_r) * np.cos(t)
        + np.cos(lat_r) * np.sin(t) * np.cos(bearings)))
    sc_lon = np.degrees(lon_r + np.arctan2(
        np.sin(bearings) * np.sin(t) * np.cos(lat_r),
        np.cos(t) - np.sin(lat_r) * np.sin(np.radians(sc_lat))))
    ax2.plot(sc_lon, sc_lat, color='#3060a8', linewidth=0.7,
             linestyle='--', transform=ccrs.Geodetic(), zorder=3)

# Euler pole marker
ax2.plot(EULER_LON, EULER_LAT, marker='o', markersize=16,
         markerfacecolor='crimson', markeredgecolor='k', markeredgewidth=1.2,
         transform=ccrs.PlateCarree(), zorder=6)
ep_x, ep_y = proj_b.transform_point(EULER_LON, EULER_LAT, ccrs.PlateCarree())
ax2.text(ep_x, ep_y + 600_000,
         'Euler pole\n$\\lambda_e, \\phi_e$',
         ha='center', va='bottom', fontsize=18, color='crimson',
         fontweight='bold', zorder=7,
         bbox=dict(facecolor='white', edgecolor='none', pad=1.5, alpha=0.8))
# Antipode
ax2.plot(((EULER_LON + 180) % 360) - 180, -EULER_LAT,
         marker='o', markersize=7,
         markerfacecolor='crimson', markeredgecolor='k', markeredgewidth=0.8,
         alpha=0.5, transform=ccrs.PlateCarree(), zorder=6)

# Velocity arrows on NAM
for s_lat, s_lon, e_lat, e_lon in euler_arrows:
    x0, y0 = proj_b.transform_point(s_lon, s_lat, ccrs.PlateCarree())
    x1, y1 = proj_b.transform_point(e_lon, e_lat, ccrs.PlateCarree())
    if not (np.isfinite(x0) and np.isfinite(y0)
            and np.isfinite(x1) and np.isfinite(y1)):
        continue
    ax2.add_patch(FancyArrowPatch(
        (x0, y0), (x1, y1), arrowstyle='-|>', mutation_scale=10,
        color='crimson', linewidth=1.3, zorder=5,
    ))

# Scale arrow — centered at bottom
fig_key_length_axes = 2.0 * ARC_PER_CMYR / 90.0
key_x_center = 0.5
key_x_start = key_x_center - fig_key_length_axes / 2 - 0.06
key_y = 0.06
ax2.annotate(
    '', xy=(key_x_start + fig_key_length_axes, key_y),
    xytext=(key_x_start, key_y),
    xycoords='axes fraction',
    arrowprops=dict(arrowstyle='-|>', color='crimson', lw=1.5,
                    mutation_scale=12))
ax2.text(key_x_start + fig_key_length_axes + 0.01, key_y,
         '2 cm/yr', transform=ax2.transAxes,
         ha='left', va='center', fontsize=18, color='crimson',
         bbox=dict(facecolor='white', edgecolor='none', pad=1.5, alpha=0.85))

# Plate labels
ax2.text(-77.0, 38.9, 'North\nAmerican', transform=ccrs.PlateCarree(),
         fontsize=18, ha='center', va='center', zorder=8,
         bbox=dict(facecolor='white', edgecolor='none', pad=1.5, alpha=0.85))
ax2.text(25, 63, 'Eurasian', transform=ccrs.PlateCarree(),
         fontsize=18, ha='center', va='center', zorder=8,
         bbox=dict(facecolor='white', edgecolor='none', pad=1.5, alpha=0.85))

outpath2 = os.path.join(
    script_dir, '..', 'book', 'figures', 'chapter16', 'euler_pole.png'
)
fig2.savefig(outpath2, dpi=300, bbox_inches='tight')
plt.close(fig2)
print(f"Saved {outpath2}")
print(f"  euler velocity arrows: {len(euler_arrows)}")
print(f"  euler velocity arrows (panel b): {len(euler_arrows)}")

"""Generate euler_pole.png: two-panel figure illustrating Euler's theorem.

Left panel — Schematic illustration of Euler's theorem on the sphere. A
continent-shaped blob is rotated about an Euler pole offset from the
geographic pole, with labels for the axis of rotation, pole of rotation,
angle of rotation, and the great and small circles of rotation.

Right panel — Orthographic view showing the motion of North America
relative to fixed Eurasia, computed from the NUVEL-1A Euler pole.
Velocity arrows (red) are plotted at grid points inside the North
America polygon, with length proportional to speed. Small circles around
the Euler pole show lines of constant angular distance theta.

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

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from shapely.geometry import shape, Point
import pmagpy.pmag as pmag

from figure_style import apply_mpl_style

apply_mpl_style()

LABEL_FONTSIZE = 20
LEFT_LABEL_FONTSIZE = 18


# ===================================================================
# Spherical geometry helpers
# ===================================================================

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


def unwrap_lons(lons):
    """Return longitudes as a continuous sequence by removing 360-deg jumps."""
    lons = np.asarray(lons, dtype=float)
    lons = ((lons + 180.0) % 360.0) - 180.0
    return np.degrees(np.unwrap(np.radians(lons)))


def small_circle_about_pole(plat, plon, theta_deg, n=361):
    """Return (lats, lons) sampling a small circle at angular distance
    theta_deg from pole (plat, plon). theta_deg=90 is the great circle."""
    pl = np.radians(plat)
    po = np.radians(plon)
    th = np.radians(theta_deg)
    az = np.radians(np.linspace(0, 360, n))
    sin_lat = np.sin(pl) * np.cos(th) + np.cos(pl) * np.sin(th) * np.cos(az)
    lat = np.arcsin(np.clip(sin_lat, -1, 1))
    y = np.sin(th) * np.sin(az)
    x = np.cos(pl) * np.cos(th) - np.sin(pl) * np.sin(th) * np.cos(az)
    lon = po + np.arctan2(y, x)
    return np.degrees(lat), np.degrees(lon)


def great_circle_segment(plat, plon, tlat, tlon, n=80):
    """Sample (lats, lons) along the great circle from (plat, plon) to
    (tlat, tlon), and return the initial bearing in degrees."""
    pl, po = np.radians(plat), np.radians(plon)
    tl, to = np.radians(tlat), np.radians(tlon)
    dlon = to - po
    cos_d = np.sin(pl) * np.sin(tl) + np.cos(pl) * np.cos(tl) * np.cos(dlon)
    d = np.arccos(np.clip(cos_d, -1, 1))
    bearing = np.arctan2(np.sin(dlon) * np.cos(tl),
                         np.cos(pl) * np.sin(tl)
                         - np.sin(pl) * np.cos(tl) * np.cos(dlon))
    fracs = np.linspace(0, 1, n)
    th = fracs * d
    sin_lat = np.sin(pl) * np.cos(th) + np.cos(pl) * np.sin(th) * np.cos(bearing)
    lats = np.arcsin(np.clip(sin_lat, -1, 1))
    y = np.sin(th) * np.sin(bearing)
    x = np.cos(pl) * np.cos(th) - np.sin(pl) * np.sin(th) * np.cos(bearing)
    lons = po + np.arctan2(y, x)
    return np.degrees(lats), np.degrees(lons), np.degrees(bearing)


def continent_blob(center_lat, center_lon, size_deg, n=120, seed=2):
    """Generate an organic-looking closed blob of (lats, lons) centered near
    (center_lat, center_lon) with characteristic angular size size_deg."""
    rng = np.random.default_rng(seed)
    phi = np.linspace(0, 2 * np.pi, n, endpoint=True)
    r = size_deg * (1.0
                    + 0.28 * np.sin(2 * phi + 0.6)
                    + 0.15 * np.cos(3 * phi - 0.4)
                    + 0.08 * np.sin(5 * phi + 1.2))
    cl = np.radians(center_lat)
    co = np.radians(center_lon)
    lats, lons = [], []
    for i in range(n):
        th = np.radians(r[i])
        az = phi[i]
        sin_lat = np.sin(cl) * np.cos(th) + np.cos(cl) * np.sin(th) * np.cos(az)
        lat = np.arcsin(np.clip(sin_lat, -1, 1))
        y = np.sin(th) * np.sin(az)
        x = np.cos(cl) * np.cos(th) - np.sin(cl) * np.sin(th) * np.cos(az)
        lon = co + np.arctan2(y, x)
        lats.append(np.degrees(lat))
        lons.append(np.degrees(lon))
    return np.array(lats), np.array(lons)


# ===================================================================
# Load data for right panel
# ===================================================================

script_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(script_dir, 'data')
with open(os.path.join(data_dir, 'PB2002_plates.json')) as f:
    plates = json.load(f)
with open(os.path.join(data_dir, 'PB2002_boundaries.json')) as f:
    boundaries = json.load(f)

plate_geoms = {
    feat['properties']['PlateName']: shape(feat['geometry'])
    for feat in plates['features']
}


# ===================================================================
# Right panel: Euler-pole velocity grid for NAM relative to EUR
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
# Build the figure
# ===================================================================

# Left-panel view and rotation parameters
TEACH_ROT_POLE_LAT = 55.0
TEACH_ROT_POLE_LON = 35.0
TEACH_ROT_ANGLE = 75.0
TEACH_BLOB_LAT = 25.0
TEACH_BLOB_LON = -25.0
TEACH_BLOB_SIZE = 13.0
TEACH_VIEW_LAT = 20.0
TEACH_VIEW_LON = -10.0

proj_left = ccrs.Orthographic(central_longitude=TEACH_VIEW_LON,
                              central_latitude=TEACH_VIEW_LAT)
proj_right = ccrs.Orthographic(central_longitude=-114.4, central_latitude=62.5)
pc_crs = ccrs.PlateCarree()
geo_crs = ccrs.Geodetic()

fig = plt.figure(figsize=(13, 6))
gs = fig.add_gridspec(1, 2, wspace=0.33, left=0.02, right=0.98,
                      top=0.97, bottom=0.03)
ax_left = fig.add_subplot(gs[0, 0], projection=proj_left)
ax_right = fig.add_subplot(gs[0, 1], projection=proj_right)


# ===================================================================
# LEFT PANEL — Euler's theorem schematic
# ===================================================================

ax_left.set_global()
ax_left.set_facecolor('white')
try:
    ax_left.spines['geo'].set_linewidth(2.0)
except KeyError:
    pass

# Geographic graticule as dotted lines
grat_kw = dict(color='0.4', linewidth=1.0,
               linestyle=(0, (1, 6)), dash_capstyle='round',
               transform=pc_crs, zorder=2)
for lat in np.arange(-60, 61, 30):
    lons = np.linspace(-180, 180, 361)
    ax_left.plot(lons, np.full_like(lons, lat), **grat_kw)
for lon in np.arange(-180, 180, 30):
    lats = np.linspace(-89, 89, 181)
    ax_left.plot(np.full_like(lats, lon), lats, **grat_kw)

# Small/great circles of rotation about the rotation pole
ROT_COLOR = '#8b1a1a'
for theta in [30, 60, 120, 150]:
    lats, lons = small_circle_about_pole(
        TEACH_ROT_POLE_LAT, TEACH_ROT_POLE_LON, theta)
    ax_left.plot(lons, lats, color=ROT_COLOR, linewidth=1.2,
                 transform=geo_crs, zorder=3)
lats_gc, lons_gc = small_circle_about_pole(
    TEACH_ROT_POLE_LAT, TEACH_ROT_POLE_LON, 90)
ax_left.plot(lons_gc, lats_gc, color=ROT_COLOR, linewidth=2.0,
             transform=geo_crs, zorder=3.5)

# Continent blobs (original and rotated)
lats1, lons1 = continent_blob(TEACH_BLOB_LAT, TEACH_BLOB_LON, TEACH_BLOB_SIZE)
ep = [TEACH_ROT_POLE_LAT, TEACH_ROT_POLE_LON, TEACH_ROT_ANGLE]
rl, ro = pmag.pt_rot(ep, list(lats1), list(lons1))
lats2, lons2 = np.array(rl), np.array(ro)
c2 = pmag.pt_rot(ep, [TEACH_BLOB_LAT], [TEACH_BLOB_LON])
c2_lat, c2_lon = float(c2[0][0]), float(c2[1][0])

for lats_b, lons_b in [(lats1, lons1), (lats2, lons2)]:
    lons_b_u = unwrap_lons(lons_b)
    ax_left.fill(lons_b_u, lats_b, facecolor='#ede0c0', edgecolor='#9c8a63',
                 linewidth=1.0, transform=pc_crs, zorder=5)

# Great-circle lines from each blob center to the rotation pole
g1_lats, g1_lons, b1 = great_circle_segment(
    TEACH_ROT_POLE_LAT, TEACH_ROT_POLE_LON, TEACH_BLOB_LAT, TEACH_BLOB_LON)
g2_lats, g2_lons, b2 = great_circle_segment(
    TEACH_ROT_POLE_LAT, TEACH_ROT_POLE_LON, c2_lat, c2_lon)
for glats, glons in [(g1_lats, g1_lons), (g2_lats, g2_lons)]:
    ax_left.plot(unwrap_lons(glons), glats, color='black', linewidth=1.0,
                 transform=pc_crs, zorder=7)

# Angle-of-rotation arc near the rotation pole
angle_arc_theta = 9.0
diff = (b2 - b1 + 540.0) % 360.0 - 180.0
azimuths = np.linspace(b1, b1 + diff, 40)
pl_r = np.radians(TEACH_ROT_POLE_LAT)
po_r = np.radians(TEACH_ROT_POLE_LON)
th_r = np.radians(angle_arc_theta)
ang_lats, ang_lons = [], []
for az in azimuths:
    az_r = np.radians(az)
    sin_lat = (np.sin(pl_r) * np.cos(th_r)
               + np.cos(pl_r) * np.sin(th_r) * np.cos(az_r))
    lat = np.degrees(np.arcsin(np.clip(sin_lat, -1, 1)))
    y = np.sin(th_r) * np.sin(az_r)
    x = np.cos(pl_r) * np.cos(th_r) - np.sin(pl_r) * np.sin(th_r) * np.cos(az_r)
    lon = np.degrees(po_r + np.arctan2(y, x))
    ang_lats.append(lat)
    ang_lons.append(lon)
ax_left.plot(unwrap_lons(ang_lons), ang_lats, color='black', linewidth=1.6,
             transform=pc_crs, zorder=8)
mid_idx = len(ang_lats) // 2
angle_target_x, angle_target_y = proj_left.transform_point(
    ang_lons[mid_idx], ang_lats[mid_idx], pc_crs)

# Center dots for both blobs
for la, lo in [(TEACH_BLOB_LAT, TEACH_BLOB_LON), (c2_lat, c2_lon)]:
    ax_left.plot(lo, la, marker='o', markersize=4, color='black',
                 transform=geo_crs, zorder=9)

# Connecting small-circle arc with arrowhead
arc_lats, arc_lons = [], []
for a in np.linspace(0, TEACH_ROT_ANGLE, 60):
    rl_i, ro_i = pmag.pt_rot(
        [TEACH_ROT_POLE_LAT, TEACH_ROT_POLE_LON, a],
        [TEACH_BLOB_LAT], [TEACH_BLOB_LON])
    arc_lats.append(rl_i[0])
    arc_lons.append(ro_i[0])
arc_lons_u = unwrap_lons(arc_lons)
ax_left.plot(arc_lons_u, arc_lats, color='black', linewidth=1.6, linestyle='-',
             transform=pc_crs, zorder=8)
ah_lat1, ah_lon1 = arc_lats[3], arc_lons[3]
ah_lat2, ah_lon2 = arc_lats[0], arc_lons[0]
xa1, ya1 = proj_left.transform_point(ah_lon1, ah_lat1, pc_crs)
xa2, ya2 = proj_left.transform_point(ah_lon2, ah_lat2, pc_crs)
ax_left.annotate('', xy=(xa2, ya2), xytext=(xa1, ya1),
                 arrowprops=dict(arrowstyle='-|>', color='black', lw=1.8,
                                 mutation_scale=24),
                 xycoords='data', textcoords='data', zorder=9)

# Axes of rotation piercing the sphere
x_np, y_np = proj_left.transform_point(0.0, 89.999, pc_crs)
x_ep, y_ep = proj_left.transform_point(
    TEACH_ROT_POLE_LON, TEACH_ROT_POLE_LAT, pc_crs)

xlim = ax_left.get_xlim()
R = max(abs(xlim[0]), abs(xlim[1]))
extend = 1.10


def draw_pierce_axis(ax, near_xy, R, extend, lw=1.8, zorder=6, color='black'):
    near = np.array(near_xy)
    hat = near / np.linalg.norm(near)
    near_tail = extend * R * hat
    far_edge = -R * hat
    far_tail = -extend * R * hat
    ax.plot([near[0], near_tail[0]], [near[1], near_tail[1]],
            color=color, linewidth=lw, zorder=zorder, clip_on=False,
            solid_capstyle='round')
    ax.plot([far_edge[0], far_tail[0]], [far_edge[1], far_tail[1]],
            color=color, linewidth=lw, zorder=zorder, clip_on=False,
            linestyle=(0, (5, 4)), solid_capstyle='round')
    return hat


axis_np_hat = draw_pierce_axis(ax_left, (x_np, y_np), R, extend)
axis_ep_hat = draw_pierce_axis(ax_left, (x_ep, y_ep), R, extend, color=ROT_COLOR)
q_top = extend * R * axis_ep_hat

ax_left.plot(x_ep, y_ep, marker='o', markersize=7, markerfacecolor='white',
             markeredgecolor=ROT_COLOR, markeredgewidth=1.6, zorder=7)

# Rotation-rate curl near the tip of the rotation axis
curl_center = q_top * 1.02
curl_r = 0.11 * R
curl_phi = np.linspace(np.radians(30), np.radians(330), 100)
axis_dir = axis_ep_hat
perp = np.array([-axis_dir[1], axis_dir[0]])
curl_x = curl_center[0] + curl_r * (np.cos(curl_phi) * perp[0]
                                    + np.sin(curl_phi) * axis_dir[0] * 0.45)
curl_y = curl_center[1] + curl_r * (np.cos(curl_phi) * perp[1]
                                    + np.sin(curl_phi) * axis_dir[1] * 0.45)
ax_left.plot(curl_x, curl_y, color='black', linewidth=1.8, zorder=7,
             clip_on=False)
ax_left.annotate('', xy=(curl_x[-1], curl_y[-1]),
                 xytext=(curl_x[-6], curl_y[-6]),
                 arrowprops=dict(arrowstyle='-|>', color='black', lw=1.6,
                                 mutation_scale=18),
                 xycoords='data', textcoords='data', zorder=8)


def label_with_leader(ax, target_xy, text, offset, ha='left', va='center'):
    label_xy = (target_xy[0] + offset[0], target_xy[1] + offset[1])
    ax.annotate(text, xy=target_xy, xytext=label_xy,
                ha=ha, va=va, fontsize=LEFT_LABEL_FONTSIZE,
                xycoords='data', textcoords='data',
                arrowprops=dict(arrowstyle='-', color='black', lw=0.8,
                                shrinkA=0, shrinkB=3),
                zorder=10, annotation_clip=False)


ax_left.text(x_np, y_np + 0.18 * R, 'Geographic pole',
             ha='center', va='bottom', fontsize=LEFT_LABEL_FONTSIZE,
             zorder=10, clip_on=False)
# Land leader on the upper-right portion of the curl ellipse
_curl_phi_label = np.radians(95.0)
curl_target = (
    curl_center[0] + curl_r * (np.cos(_curl_phi_label) * perp[0]
                               + np.sin(_curl_phi_label) * axis_dir[0] * 0.45),
    curl_center[1] + curl_r * (np.cos(_curl_phi_label) * perp[1]
                               + np.sin(_curl_phi_label) * axis_dir[1] * 0.45),
)
label_with_leader(ax_left, curl_target,
                  r'Rotation rate ($\omega$)',
                  offset=(0.05 * R, 0.15 * R), ha='left')
label_with_leader(ax_left, (x_ep, y_ep),
                  'Pole of\n' r'rotation ($\lambda_e, \phi_e$)',
                  offset=(0.42 * R, 0.20 * R), ha='left')
label_with_leader(ax_left, (angle_target_x, angle_target_y),
                  'Angle of\n' r'rotation ($\Omega$)',
                  offset=(0.55 * R, 0.05 * R), ha='left')


def pole_polar_to_xy(theta_deg, az_deg):
    az_r = np.radians(az_deg)
    th_r_local = np.radians(theta_deg)
    sin_lat = (np.sin(pl_r) * np.cos(th_r_local)
               + np.cos(pl_r) * np.sin(th_r_local) * np.cos(az_r))
    lat = np.degrees(np.arcsin(np.clip(sin_lat, -1, 1)))
    y = np.sin(th_r_local) * np.sin(az_r)
    x = (np.cos(pl_r) * np.cos(th_r_local)
         - np.sin(pl_r) * np.sin(th_r_local) * np.cos(az_r))
    lon = np.degrees(po_r + np.arctan2(y, x))
    return proj_left.transform_point(lon, lat, pc_crs)


gc_x_t, gc_y_t = pole_polar_to_xy(90.0, 170.0)
label_with_leader(ax_left, (gc_x_t, gc_y_t),
                  'Great circle\nof rotation',
                  offset=(0.18 * R, -0.10 * R), ha='left')
sc_x_t, sc_y_t = pole_polar_to_xy(60.0, 145.0)
label_with_leader(ax_left, (sc_x_t, sc_y_t),
                  'Small circles\nof rotation',
                  offset=(0.12 * R, 0.05 * R), ha='left')

ax_left.set_clip_on(False)
for artist in ax_left.get_children():
    try:
        artist.set_clip_on(False)
    except AttributeError:
        pass


# ===================================================================
# RIGHT PANEL — NUVEL-1A velocity field, North America / Eurasia
# ===================================================================

ax_right.set_global()
ax_right.add_feature(cfeature.OCEAN, facecolor='#f2f7fc')
ax_right.add_feature(cfeature.LAND, facecolor='#ede0c0', edgecolor='#9c8a63',
                     linewidth=0.4)
ax_right.gridlines(color='0.75', linestyle=':', linewidth=0.5)

for lons, lats in _pb2002_boundary_segments():
    ax_right.plot(lons, lats, color='#555555', linewidth=0.8,
                  transform=geo_crs, zorder=2)

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
    ax_right.plot(sc_lon, sc_lat, color='#3060a8', linewidth=0.7,
                  linestyle='--', transform=geo_crs, zorder=3)

# Euler pole marker and label
ax_right.plot(EULER_LON, EULER_LAT, marker='o', markersize=16,
              markerfacecolor='crimson', markeredgecolor='k',
              markeredgewidth=1.2, transform=pc_crs, zorder=6)
ep_x, ep_y = proj_right.transform_point(EULER_LON, EULER_LAT, pc_crs)
ax_right.text(ep_x, ep_y + 600_000,
              'Euler pole\n$\\lambda_e, \\phi_e, \\omega$',
              ha='center', va='bottom', fontsize=LABEL_FONTSIZE,
              color='crimson', fontweight='bold', zorder=7,
              bbox=dict(facecolor='white', edgecolor='none', pad=1.5,
                        alpha=0.8))
ax_right.plot(((EULER_LON + 180) % 360) - 180, -EULER_LAT,
              marker='o', markersize=7,
              markerfacecolor='crimson', markeredgecolor='k',
              markeredgewidth=0.8, alpha=0.5, transform=pc_crs, zorder=6)

# Velocity arrows on NAM
for s_lat, s_lon, e_lat, e_lon in euler_arrows:
    x0, y0 = proj_right.transform_point(s_lon, s_lat, pc_crs)
    x1, y1 = proj_right.transform_point(e_lon, e_lat, pc_crs)
    if not (np.isfinite(x0) and np.isfinite(y0)
            and np.isfinite(x1) and np.isfinite(y1)):
        continue
    ax_right.add_patch(FancyArrowPatch(
        (x0, y0), (x1, y1), arrowstyle='-|>', mutation_scale=10,
        color='crimson', linewidth=1.3, zorder=5,
    ))

# Scale arrow centered at bottom
fig_key_length_axes = 2.0 * ARC_PER_CMYR / 90.0
key_x_center = 0.5
key_x_start = key_x_center - fig_key_length_axes / 2 - 0.06
key_y = 0.06
ax_right.annotate(
    '', xy=(key_x_start + fig_key_length_axes, key_y),
    xytext=(key_x_start, key_y),
    xycoords='axes fraction',
    arrowprops=dict(arrowstyle='-|>', color='crimson', lw=1.5,
                    mutation_scale=12))
ax_right.text(key_x_start + fig_key_length_axes + 0.01, key_y,
              '2 cm/yr', transform=ax_right.transAxes,
              ha='left', va='center', fontsize=LABEL_FONTSIZE, color='crimson',
              bbox=dict(facecolor='white', edgecolor='none', pad=1.5,
                        alpha=0.85))

# Plate labels
ax_right.text(-77.0, 38.9, 'North\nAmerican', transform=pc_crs,
              fontsize=LABEL_FONTSIZE, ha='center', va='center', zorder=8,
              bbox=dict(facecolor='white', edgecolor='none', pad=1.5,
                        alpha=0.85))
ax_right.text(25, 63, 'Eurasian', transform=pc_crs,
              fontsize=LABEL_FONTSIZE, ha='center', va='center', zorder=8,
              bbox=dict(facecolor='white', edgecolor='none', pad=1.5,
                        alpha=0.85))

# Panel labels
ax_left.text(0.02, 0.98, 'a)', transform=ax_left.transAxes,
             fontsize=LABEL_FONTSIZE + 2, fontweight='bold',
             ha='left', va='top')
ax_right.text(0.02, 0.98, 'b)', transform=ax_right.transAxes,
              fontsize=LABEL_FONTSIZE + 2, fontweight='bold',
              ha='left', va='top')

outpath = os.path.join(
    script_dir, '..', 'book', 'figures', 'chapter16', 'euler_pole.png'
)
fig.savefig(outpath, dpi=300, bbox_inches='tight', facecolor='white')
plt.close(fig)
print(f"Saved {outpath}")
print(f"  euler velocity arrows: {len(euler_arrows)}")

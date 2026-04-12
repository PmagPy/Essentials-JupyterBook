"""Generate upper Osler VGP and paleomagnetic pole figure for Chapter 16.

Downloads tilt-corrected reversed polarity paleomagnetic data from the
upper Osler Volcanic Group, flips directions to normal polarity, calculates
Virtual Geomagnetic Poles (VGPs), and computes the paleomagnetic pole with
Fisher statistics. Produces an orthographic map showing individual VGPs,
the mean pole, the paleoequator, and annotated colatitude/paleolatitude arcs.

Data from:
    Halls, H. (1974), A paleomagnetic reversal in the Osler Volcanic
    Group, northern Lake Superior, Can. J. Earth Sci., 11, 1200-1207.

    Swanson-Hysell, N. L., Vaughan, A. A., Mustain, M. R., and
    Asp, K. E. (2014), Confirmation of progressive plate motion during
    the Midcontinent Rift's early magmatic stage from the Osler Volcanic
    Group, Ontario, Canada, Geochem. Geophys. Geosyst., 15, 2039-2047.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import pmagpy.ipmag as ipmag
import pmagpy.pmag as pmag

from figure_style import apply_mpl_style

apply_mpl_style()

script_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(script_dir, 'data')
outdir = os.path.join(script_dir, '..', 'book', 'figures', 'chapter16')


# ===================================================================
# Spherical geometry helpers
# ===================================================================

def initial_bearing(lat1, lon1, lat2, lon2):
    """Initial bearing (degrees) from point 1 to point 2."""
    lat1_r, lon1_r = np.radians(lat1), np.radians(lon1)
    lat2_r, lon2_r = np.radians(lat2), np.radians(lon2)
    dlon = lon2_r - lon1_r
    y = np.sin(dlon) * np.cos(lat2_r)
    x = (np.cos(lat1_r) * np.sin(lat2_r) -
         np.sin(lat1_r) * np.cos(lat2_r) * np.cos(dlon))
    return np.degrees(np.arctan2(y, x)) % 360


def destination_point(lat, lon, bearing_deg, distance_deg):
    """Point at given bearing and angular distance from start."""
    lat_r = np.radians(lat)
    lon_r = np.radians(lon)
    brg_r = np.radians(bearing_deg)
    dist_r = np.radians(distance_deg)
    lat2 = np.arcsin(np.sin(lat_r) * np.cos(dist_r) +
                     np.cos(lat_r) * np.sin(dist_r) * np.cos(brg_r))
    lon2 = lon_r + np.arctan2(
        np.sin(brg_r) * np.sin(dist_r) * np.cos(lat_r),
        np.cos(dist_r) - np.sin(lat_r) * np.sin(lat2))
    return float(np.degrees(lat2)), float(np.degrees(lon2))


# ===================================================================
# Download and load data from MagIC
# ===================================================================

halls_dir = os.path.join(data_dir, 'Halls1974')
result, halls_file = ipmag.download_magic_from_id('20260', directory=halls_dir)
ipmag.unpack_magic(halls_file, dir_path=halls_dir, print_progress=False)

sh_dir = os.path.join(data_dir, 'SwansonHysell2014')
result, sh_file = ipmag.download_magic_from_id('18693', directory=sh_dir)
ipmag.unpack_magic(sh_file, dir_path=sh_dir, print_progress=False)

# ===================================================================
# Load and filter for reversed polarity tilt-corrected directions
# (upper Osler: Halls reversed flows + upper Simpson Island section)
# ===================================================================

halls_sites = pd.read_csv(os.path.join(halls_dir, 'sites.txt'),
                          sep='\t', header=1)
for col in ['lat', 'lon']:
    halls_sites[col] = halls_sites.groupby('site')[col].transform(
        lambda x: x.ffill().bfill())
halls_tc = halls_sites[(halls_sites.dir_tilt_correction == 100) &
                       (halls_sites.location.str.contains('Lower Reversed'))].copy()

sh_sites = pd.read_csv(os.path.join(sh_dir, 'sites.txt'),
                        sep='\t', header=1)
for col in ['lat', 'lon']:
    if col in sh_sites.columns:
        sh_sites[col] = sh_sites.groupby('site')[col].transform(
            lambda x: x.ffill().bfill())
sh_tc = sh_sites[(sh_sites.dir_tilt_correction == 100) &
                 (sh_sites.dir_dec.notna()) &
                 (sh_sites.height > 2082)].copy()

print(f'{len(halls_tc)} reversed sites from Halls (1974)')
print(f'{len(sh_tc)} upper Osler sites from Swanson-Hysell et al. (2014)')

# ===================================================================
# Combine and flip directions to normal polarity
# ===================================================================

reversed_dec = list(halls_tc.dir_dec.values) + list(sh_tc.dir_dec.values)
reversed_inc = list(halls_tc.dir_inc.values) + list(sh_tc.dir_inc.values)
site_lats = list(halls_tc.lat.values) + list(sh_tc.lat.values)
site_lons = list(halls_tc.lon.values) + list(sh_tc.lon.values)

di_block = ipmag.make_di_block(reversed_dec, reversed_inc)
flipped = pmag.flip(di_block, combine=True)
normal_dec, normal_inc = ipmag.unpack_di_block(flipped)[:2]

# ===================================================================
# Calculate VGPs from normal polarity directions
# ===================================================================

vgp_lon = []
vgp_lat = []
for i in range(len(normal_dec)):
    plon, plat, dp, dm = pmag.dia_vgp(
        normal_dec[i], normal_inc[i], 0, site_lats[i], site_lons[i])
    vgp_lon.append(plon)
    vgp_lat.append(plat)

# ===================================================================
# Calculate paleomagnetic pole (Fisher mean of VGPs)
# ===================================================================

pole_stats = ipmag.fisher_mean(dec=vgp_lon, inc=vgp_lat)
pole_lon = pole_stats['dec']
pole_lat = pole_stats['inc']
pole_A95 = pole_stats['alpha95']
pole_n = int(pole_stats['n'])
pole_k = pole_stats['k']

print(f'\nUpper Osler paleomagnetic pole ({pole_n} VGPs):')
print(f'  Lat: {pole_lat:.1f}, Lon: {pole_lon:.1f}E')
print(f'  A95: {pole_A95:.1f}, k: {pole_k:.1f}')

# Mean site location (single point for the study)
mean_site = ipmag.fisher_mean(dec=site_lons, inc=site_lats)
mean_site_lon = mean_site['dec']
mean_site_lat = mean_site['inc']
print(f'\nMean site location: {mean_site_lat:.1f}N, {mean_site_lon:.1f}E')

# Colatitude and paleolatitude
colatitude_val = pmag.angle([pole_lon, pole_lat],
                            [mean_site_lon, mean_site_lat])[0]
paleolatitude_val = 90 - colatitude_val
print(f'Colatitude: {colatitude_val:.1f}')
print(f'Paleolatitude: {paleolatitude_val:.1f}N')

# ===================================================================
# Geometry for annotation arcs
# ===================================================================

# Bearing from pole toward site
brg_pole_to_site = initial_bearing(pole_lat, pole_lon,
                                   mean_site_lat, mean_site_lon)

# Equator intersection: 90 deg from pole along bearing toward site
eq_lat, eq_lon = destination_point(pole_lat, pole_lon,
                                   brg_pole_to_site, 90)

# Midpoints for label placement
colat_mid_lat, colat_mid_lon = destination_point(
    pole_lat, pole_lon, brg_pole_to_site, colatitude_val / 2)
paleolat_mid_lat, paleolat_mid_lon = destination_point(
    mean_site_lat, mean_site_lon,
    initial_bearing(mean_site_lat, mean_site_lon, eq_lat, eq_lon),
    paleolatitude_val / 2)

# Map center: midpoint between pole and site
center_lat, center_lon = destination_point(
    pole_lat, pole_lon, brg_pole_to_site, colatitude_val / 2)

# ===================================================================
# Plot
# ===================================================================

map_axis = ipmag.make_orthographic_map(
    central_longitude=center_lon,
    central_latitude=center_lat,
    figsize=(7, 7),
    land_color='#ede0c0',
    land_edge_color=None,
    grid_lines=False
)
map_axis.gridlines(linewidth=0.5, color='0.65', linestyle=':')

# --- VGPs ---
ipmag.plot_vgp(map_axis,
               vgp_lon=vgp_lon, vgp_lat=vgp_lat,
               color='steelblue', marker='o', markersize=40,
               label='VGPs', edge=None, alpha=0.75, zorder=50)

# --- Mean pole (square) with A95 — on top of VGPs ---
ipmag.plot_pole(map_axis, pole_lon, pole_lat, pole_A95,
                color='red', edgecolor='black', marker='s',
                markersize=80, label='Mean pole',
                mean_alpha=1.0, zorder=200)

# --- Paleoequator (points 90 deg from pole) ---
eq_bearings = np.linspace(0, 360, 361)
eq_lats_arr = []
eq_lons_arr = []
for b in eq_bearings:
    elat, elon = destination_point(pole_lat, pole_lon, b, 90)
    eq_lats_arr.append(elat)
    eq_lons_arr.append(elon)
map_axis.plot(eq_lons_arr, eq_lats_arr,
              color='darkgreen', linewidth=3, alpha=0.8,
              transform=ccrs.PlateCarree(), zorder=60,
              label='Paleoequator')

# --- Study location (single star, linestyle='None' so legend has no line) ---
map_axis.plot(mean_site_lon, mean_site_lat, marker='*',
              markersize=18, color='gold', markeredgecolor='black',
              markeredgewidth=0.8, linestyle='None',
              transform=ccrs.PlateCarree(),
              zorder=90, label='Study location')

# --- Great circle: pole to site (colatitude) ---
map_axis.plot([pole_lon, mean_site_lon], [pole_lat, mean_site_lat],
              color='black', linewidth=1.5, linestyle='--',
              transform=ccrs.Geodetic(), zorder=70)

# --- Great circle: site to paleoequator (paleolatitude) ---
map_axis.plot([mean_site_lon, eq_lon], [mean_site_lat, eq_lat],
              color='black', linewidth=1.5, linestyle=':',
              transform=ccrs.Geodetic(), zorder=70)

# --- Labels ---
bbox = dict(facecolor='white', edgecolor='none', alpha=0.85, pad=1.5)

map_axis.text(colat_mid_lon, colat_mid_lat + 4,
              f'colatitude\n{colatitude_val:.1f}\u00b0',
              transform=ccrs.PlateCarree(),
              fontsize=11, ha='center', va='bottom',
              bbox=bbox, zorder=110)

map_axis.text(paleolat_mid_lon - 8, paleolat_mid_lat + 6,
              f'paleolatitude\n{paleolatitude_val:.1f}\u00b0',
              transform=ccrs.PlateCarree(),
              fontsize=11, ha='center', va='bottom',
              bbox=bbox, zorder=110)

map_axis.legend(loc='lower center', fontsize=10, framealpha=0.9)

outpath = os.path.join(outdir, 'osler_vgp_pole.png')
plt.savefig(outpath, dpi=300, bbox_inches='tight')
plt.close()
print(f'\nSaved {outpath}')

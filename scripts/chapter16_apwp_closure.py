"""Generate APWP closure figure for Chapter 16.

Shows how the apparent polar wander paths of North America and Europe
diverge in their present-day reference frames but converge when the
Atlantic closure rotation from the CEED6 model is applied. Focuses on the
200-270 Ma interval where the two continents were joined as part of Pangea.

Three panels:
  Top-left  — APWPs in their own reference frames (divergent)
  Top-right — EUR APWP rotated into NAM coordinates (convergent)
  Bottom    — Angular mismatch before and after applying the rotation

Uses the Torsvik et al. (2012) APWPs for NAM and EUR, rotated using
CEED6 finite rotations from Torsvik & Cocks (2017).

References:
    Torsvik, T.H. et al. (2012), Phanerozoic polar wander,
    palaeogeography and dynamics, Earth-Science Reviews, 114, 325-368,
    doi:10.1016/j.earscirev.2012.06.007.

    Torsvik, T.H. and Cocks, L.R.M. (2017), Earth History and
    Palaeogeography, Cambridge University Press.
"""

import os
import sys
sys.path.insert(0, os.path.dirname(__file__))

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import pmagpy.pmag as pmag
import pygplates

from figure_style import apply_mpl_style

apply_mpl_style()

# ===================================================================
# APWP data (Besse & Courtillot 2002 synthetic path, south poles)
# ===================================================================

nam_apwp = pd.DataFrame({
    'Age':  [0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,
             190,200,210,220,230,240,250,260,270,280,290,300,310,320],
    'Slat': [-88.0,-88.4,-84.1,-82.8,-81.8,-75.7,-73.8,-75.0,-74.5,-74.7,-75.6,
             -75.4,-72.5,-71.3,-62.6,-64.1,-66.8,-67.0,-67.8,-66.5,-64.2,-61.3,
             -58.0,-54.5,-53.2,-53.1,-54.9,-53.1,-48.5,-44.4,-43.6,-36.4,-25.7],
    'Slon': [322.8,334.3,338.1,341.9,344.8,358.4,5.0,18.0,21.3,18.6,0.7,10.0,
             16.6,18.2,18.2,359.8,337.9,316.1,277.2,264.9,262.8,270.0,279.2,
             290.1,295.3,294.8,305.4,305.3,304.8,303.6,304.0,302.9,301.5],
})
eur_apwp = pd.DataFrame({
    'Age':  [0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,
             190,200,210,220,230,240,250,260,270,280,290,300,310,320],
    'Slat': [-82.5,-81.8,-78.6,-80.3,-80.8,-79.6,-78.1,-75.7,-72.3,-73.4,-78.6,
             -80.8,-78.8,-76.5,-74.0,-74.7,-72.5,-69.0,-68.9,-69.9,-59.3,-54.7,
             -51.2,-51.8,-56.3,-55.6,-54.5,-51.1,-45.1,-43.1,-42.6,-43.5,-29.0],
    'Slon': [312.2,327.2,331.6,332.6,2.0,344.2,345.0,345.5,333.2,338.1,352.0,
             338.4,349.8,357.5,3.0,328.5,316.5,302.7,285.5,281.7,280.3,284.5,
             304.2,309.7,325.2,329.8,329.8,337.4,346.3,346.5,347.0,347.0,339.6],
})


def south_to_north(slat, slon):
    return -np.asarray(slat), (np.asarray(slon) + 180.0) % 360.0


nam_apwp['Plat'], nam_apwp['Plon'] = south_to_north(
    nam_apwp['Slat'], nam_apwp['Slon'])
eur_apwp['Plat'], eur_apwp['Plon'] = south_to_north(
    eur_apwp['Slat'], eur_apwp['Slon'])


# ===================================================================
# Apply age-appropriate CEED6 rotation to EUR poles
# ===================================================================

script_dir = os.path.dirname(os.path.abspath(__file__))
rot_file = os.path.join(script_dir, 'data', 'CEED6', 'TC2017.rot')
rm = pygplates.RotationModel(rot_file)

rot_plats, rot_plons = [], []
for _, row in eur_apwp.iterrows():
    fr = rm.get_rotation(float(row['Age']), 301, 0., 101)
    lat, lon, ang = fr.get_lat_lon_euler_pole_and_angle_degrees()
    rl, ro = pmag.pt_rot([lat, lon, ang], [row['Plat']], [row['Plon']])
    rot_plats.append(rl[0])
    rot_plons.append(ro[0])
eur_apwp['Plat_NAM'] = rot_plats
eur_apwp['Plon_NAM'] = rot_plons


# ===================================================================
# Filter to 200-270 Ma
# ===================================================================

age_min, age_max = 200, 270
nam_sub = nam_apwp[(nam_apwp['Age'] >= age_min)
                    & (nam_apwp['Age'] <= age_max)]
eur_sub = eur_apwp[(eur_apwp['Age'] >= age_min)
                    & (eur_apwp['Age'] <= age_max)].copy()


# Projection center (spherical mean of all poles in this window)
def sph_mean(lats, lons):
    lr, lo = np.radians(lats), np.radians(lons)
    x = np.mean(np.cos(lr) * np.cos(lo))
    y = np.mean(np.cos(lr) * np.sin(lo))
    z = np.mean(np.sin(lr))
    return (np.degrees(np.arcsin(z / np.sqrt(x**2 + y**2 + z**2))),
            np.degrees(np.arctan2(y, x)))


all_lats = np.concatenate([nam_sub['Plat'].values, eur_sub['Plat'].values,
                           eur_sub['Plat_NAM'].values])
all_lons = np.concatenate([nam_sub['Plon'].values, eur_sub['Plon'].values,
                           eur_sub['Plon_NAM'].values])
clat, clon = sph_mean(all_lats, all_lons)
print(f"Projection center: ({clat:.1f}°N, {clon:.1f}°E)")


# Angular mismatch
def gcd(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
    c = (np.sin(lat1) * np.sin(lat2)
         + np.cos(lat1) * np.cos(lat2) * np.cos(lon2 - lon1))
    return np.degrees(np.arccos(np.clip(c, -1, 1)))


eur_sub['mismatch_raw'] = gcd(
    nam_sub['Plat'].values, nam_sub['Plon'].values,
    eur_sub['Plat'].values, eur_sub['Plon'].values)
eur_sub['mismatch_rot'] = gcd(
    nam_sub['Plat'].values, nam_sub['Plon'].values,
    eur_sub['Plat_NAM'].values, eur_sub['Plon_NAM'].values)


# ===================================================================
# Figure: 2 map panels on top, mismatch panel on bottom
# ===================================================================

fig = plt.figure(figsize=(16, 13))

ax_raw = fig.add_axes(
    [0.05, 0.48, 0.43, 0.50],
    projection=ccrs.Orthographic(central_longitude=clon,
                                 central_latitude=clat))
ax_rot = fig.add_axes(
    [0.52, 0.48, 0.43, 0.50],
    projection=ccrs.Orthographic(central_longitude=clon,
                                 central_latitude=clat))

for ax, title, eur_lon_col, eur_lat_col in [
    (ax_raw,
     'Before closure\n(each APWP in its own reference frame)',
     'Plon', 'Plat'),
    (ax_rot,
     'Restoring to pre-breakup position\n(EUR rotated into NAM coordinates)',
     'Plon_NAM', 'Plat_NAM'),
]:
    ax.set_global()
    ax.add_feature(cfeature.LAND, facecolor='0.93', edgecolor='0.7',
                   linewidth=0.3)
    ax.add_feature(cfeature.OCEAN, facecolor='white')
    ax.gridlines(color='0.8', linestyle=':', linewidth=0.5)

    # NAM APWP (circles)
    ax.plot(nam_sub['Plon'], nam_sub['Plat'], color='0.3', linewidth=1.5,
            transform=ccrs.Geodetic(), zorder=3)
    sc = ax.scatter(nam_sub['Plon'], nam_sub['Plat'],
                    c=nam_sub['Age'], cmap='RdYlBu',
                    s=140, marker='o', edgecolor='k', linewidth=0.8,
                    transform=ccrs.PlateCarree(),
                    vmin=age_min, vmax=age_max, zorder=4)

    # EUR APWP (squares)
    ax.plot(eur_sub[eur_lon_col], eur_sub[eur_lat_col],
            color='0.5', linewidth=1.5, linestyle='-',
            transform=ccrs.Geodetic(), zorder=3)
    ax.scatter(eur_sub[eur_lon_col], eur_sub[eur_lat_col],
               c=eur_sub['Age'], cmap='RdYlBu',
               s=140, marker='s', edgecolor='k', linewidth=0.8,
               transform=ccrs.PlateCarree(),
               vmin=age_min, vmax=age_max, zorder=4)

    ax.set_title(title, fontsize=20, fontweight='bold', y=0.88,
                 bbox=dict(facecolor='white', edgecolor='none',
                           alpha=0.85, pad=3))

# Legend + colorbar
legend_handles = [
    Line2D([0], [0], marker='o', color='w', markerfacecolor='0.5',
           markeredgecolor='k', markersize=12,
           label='North America (NAM)'),
    Line2D([0], [0], marker='s', color='w', markerfacecolor='0.5',
           markeredgecolor='k', markersize=12,
           label='Europe (EUR)'),
]

bg = mpatches.FancyBboxPatch(
    (0.2, 0.5), 0.6, 0.1, boxstyle='round,pad=0.01',
    facecolor='white', edgecolor='0.7', linewidth=0.8, alpha=0.95,
    transform=fig.transFigure, zorder=5)
fig.patches.append(bg)

fig.legend(handles=legend_handles, loc='upper center',
           ncol=2, fontsize=18, frameon=False,
           bbox_to_anchor=(0.5, 0.615))

cb_ax = fig.add_axes([0.22, 0.54, 0.56, 0.018])
cb_ax.set_zorder(10)
cb = plt.colorbar(sc, cax=cb_ax, orientation='horizontal')
cb.set_label('Age (Ma)', fontsize=16)
cb.ax.tick_params(labelsize=14)

# Bottom: angular mismatch
ax_mis = fig.add_axes([0.15, 0.12, 0.70, 0.32])
ax_mis.plot(eur_sub['Age'], eur_sub['mismatch_raw'],
            color='0.4', linewidth=2, marker='o', markersize=8,
            markerfacecolor='0.8', markeredgecolor='0.3',
            label='Before closure')
ax_mis.plot(eur_sub['Age'], eur_sub['mismatch_rot'],
            color='#202080', linewidth=2, marker='s', markersize=8,
            markerfacecolor='#4060c0', markeredgecolor='k',
            label='Restored to pre-breakup position')
ax_mis.set_xlabel('Age (Ma)', fontsize=18)
ax_mis.set_ylabel('Angular distance between\nNAM and EUR APWP (°)',
                  fontsize=16)
ax_mis.set_xlim(age_min - 5, age_max + 5)
ax_mis.set_ylim(0, 21)
ax_mis.legend(fontsize=16, loc='upper left')
ax_mis.grid(alpha=0.3)
ax_mis.set_title('APWP angular mismatch before and after applying '
                 'Atlantic closure rotation',
                 fontsize=20, fontweight='bold')
ax_mis.tick_params(labelsize=14)

outpath = os.path.join(
    script_dir, '..', 'book', 'figures', 'chapter16',
    'apwp_closure.png'
)
fig.savefig(outpath, dpi=300, bbox_inches='tight')
plt.close(fig)
print(f"Saved {outpath}")

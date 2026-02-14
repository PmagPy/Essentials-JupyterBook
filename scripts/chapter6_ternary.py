#!/usr/bin/env python
"""
TiO2-FeO-Fe2O3 ternary diagram for iron-titanium oxide minerals.

Multi-panel figure:
  (a) Detailed ternary with oxidation grid, x/z labels, mineral names
  (b) High-temperature oxyexsolution process
  (c) Low-temperature oxidation (maghemitization) process

Uses the python-ternary library: pip install python-ternary

IMPORTANT: This plot uses cation-fraction coordinates, not oxide mole fractions.
Ternary coordinates are (Fe3+, Ti4+, Fe2+) cation fractions (sum to 1), mapped to:
    right corner  = Fe3+ (Fe2O3 corner in oxide-ternary language)
    top corner    = Ti4+ (TiO2)
    left corner   = Fe2+ (FeO)

Variable convention (Tauxe/Butler):
    x = Ti substitution (composition parameter, 0→1 along TM join)
    z = oxidation parameter (0=stoichiometric, 1=fully oxidized)

References (figure concept):
    Tauxe (2010) Essentials of Paleomagnetism, Fig. 6.3
    Butler (1992) Paleomagnetism
    Dunlop & Özdemir (1997) Rock Magnetism, Fig. 3.1
    O'Reilly (1984) Rock and Mineral Magnetism
"""

from __future__ import annotations

import matplotlib
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np
import ternary


# ================================================================
# Composition functions
# ================================================================


def titanomagnetite(x: float) -> tuple[float, float, float]:
    """Titanomagnetite solid solution series.

    x = 0: magnetite (Fe3O4)
    x = 1: ulvöspinel (Fe2TiO4)

    Returns (Fe3+, Ti4+, Fe2+) cation fractions, normalized to sum to 1.

    Parameters
    ----------
    x
        Ti substitution parameter along the titanomagnetite join.

    Returns
    -------
    Tuple[float, float, float]
        (Fe3+, Ti4+, Fe2+) cation fractions.
    """
    ti = x
    fe2 = 1.0 + x
    fe3 = 2.0 * (1.0 - x)
    total = 3.0  # fixed 3 cations per formula unit
    return (fe3 / total, ti / total, fe2 / total)


def titanohematite(x: float) -> tuple[float, float, float]:
    """Titanohematite solid solution series.

    x = 0: hematite (Fe2O3)
    x = 1: ilmenite (FeTiO3)

    Returns (Fe3+, Ti4+, Fe2+) cation fractions, normalized to sum to 1.

    Parameters
    ----------
    x
        Ti substitution parameter along the titanohematite join.

    Returns
    -------
    Tuple[float, float, float]
        (Fe3+, Ti4+, Fe2+) cation fractions.
    """
    ti = x
    fe2 = x
    fe3 = 2.0 * (1.0 - x)
    total = 2.0  # fixed 2 cations per formula unit
    return (fe3 / total, ti / total, fe2 / total)


def oxidized_titanomagnetite(x: float, z: float) -> tuple[float, float, float]:
    """Oxidized titanomagnetite in cation-fraction coordinates.

    The implementation follows an oxide-bookkeeping approach to generate a
    ternary point, then converts to cation counts and normalizes.

    Parameters
    ----------
    x
        Ti substitution (0 = magnetite, 1 = ulvöspinel).
    z
        Oxidation parameter (0 = stoichiometric, 1 = fully oxidized).

    Returns
    -------
    Tuple[float, float, float]
        (Fe3+, Ti4+, Fe2+) cation fractions (sum to 1).
    """
    # Oxide amounts from stoichiometry-like bookkeeping
    tio2_raw = x
    feo_raw = (1.0 + x) * (1.0 - z)
    fe2o3_raw = (1.0 - x) + (1.0 + x) * z / 2.0

    # Convert to cation counts
    ti = tio2_raw
    fe2 = feo_raw
    fe3 = 2.0 * fe2o3_raw

    total = ti + fe2 + fe3
    return (fe3 / total, ti / total, fe2 / total)


def ternary_to_cartesian(point: tuple[float, float, float]) -> tuple[float, float]:
    """Convert (right, top, left) ternary coordinates to (x, y) Cartesian.

    Parameters
    ----------
    point
        Ternary point as (right, top, left).

    Returns
    -------
    Tuple[float, float]
        (x, y) in Cartesian coordinates.
    """
    r, t, _l = point
    x = r + 0.5 * t
    y = t * np.sqrt(3.0) / 2.0
    return (x, y)


def make_curve(
    func, t_range: tuple[float, float] = (0.0, 1.0), n: int = 100
) -> list[tuple[float, float, float]]:
    """Generate a list of ternary points along a parameterized curve.

    Parameters
    ----------
    func
        Function mapping a scalar parameter to a ternary point.
    t_range
        Parameter range (min, max).
    n
        Number of points.

    Returns
    -------
    List[Tuple[float, float, float]]
        Curve points in ternary coordinates.
    """
    ts = np.linspace(t_range[0], t_range[1], n)
    return [func(float(t)) for t in ts]


# Key mineral positions in this cation-fraction ternary
pseudobrookite = (2.0 / 3.0, 1.0 / 3.0, 0.0)  # Fe3+:Ti:Fe2 = 2:1:0
ferropsdbk = (0.0, 2.0 / 3.0, 1.0 / 3.0)  # Fe3+:Ti:Fe2 = 0:2:1


# ================================================================
# Helper: draw base ternary elements on a given TernaryAxesSubplot
# ================================================================


def draw_base_ternary(
    tax: ternary.TernaryAxesSubplot,
    show_gridlines: bool = True,
    corner_fontsize: int = 12,
    corner_offset_top: float = 0.18,
    corner_offset_side: float = 0.06,
    show_mineral_names: bool = True,
    detailed_corners: bool = True,
) -> None:
    """Draw triangle boundary, joins, and corner labels.

    Parameters
    ----------
    tax
        python-ternary axes.
    show_gridlines
        Whether to draw faint gridlines.
    corner_fontsize
        Font size for corner labels.
    corner_offset_top
        Offset for top corner label.
    corner_offset_side
        Offset for left/right corner labels.
    show_mineral_names
        Whether to add mineral-name hints to corner labels.
    detailed_corners
        Whether to include valence/phase hints in the corner labels.
    """
    ax = tax.get_axes()

    tax.boundary(linewidth=2.0)
    tax.clear_matplotlib_ticks()
    ax.set_frame_on(False)

    if show_gridlines:
        tax.gridlines(color="#e8e8e8", multiple=0.1, linewidth=0.3)

    if detailed_corners:
        top_label = "$\\mathrm{TiO_2}$ ($\\mathrm{Ti^{4+}}$)"
        left_label = "$\\mathrm{FeO}$\n($\\mathrm{Fe^{2+}}$)\nwüstite"
        right_label = "$\\mathrm{Fe_2O_3}$\n($\\mathrm{Fe^{3+}}$)"
    else:
        top_label = "$\\mathrm{TiO_2}$"
        left_label = "$\\mathrm{FeO}$"
        right_label = "$\\mathrm{Fe_2O_3}$"

    if show_mineral_names:
        top_label += "\nrutile, anatase"

    tax.top_corner_label(top_label, fontsize=corner_fontsize, offset=corner_offset_top)
    tax.left_corner_label(
        left_label, fontsize=corner_fontsize, offset=corner_offset_side
    )
    tax.right_corner_label(
        right_label, fontsize=corner_fontsize, offset=corner_offset_side
    )

    # Solid solution joins (cation-fraction coordinates)
    tax.plot(make_curve(titanomagnetite), linewidth=2.0, color="black")
    tax.plot(make_curve(titanohematite), linewidth=2.0, color="black")
    tax.plot([pseudobrookite, ferropsdbk], linewidth=1.5, color="black")

    ax.set_aspect("equal")


def draw_oxidation_grid(tax: ternary.TernaryAxesSubplot) -> None:
    """Draw the x (constant composition) and z (constant oxidation) grid lines.

    Parameters
    ----------
    tax
        python-ternary axes.
    """
    # Lines of constant x (composition)
    for x in [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]:
        line = [oxidized_titanomagnetite(x, float(zv)) for zv in np.linspace(0, 1, 100)]
        tax.plot(line, linewidth=0.7, color="#444444")

    # Lines of constant z (oxidation, dashed)
    for zv in [0.2, 0.4, 0.6, 0.8]:
        line = [
            oxidized_titanomagnetite(float(xv), zv) for xv in np.linspace(0, 1, 100)
        ]
        tax.plot(line, linewidth=0.7, color="#444444", linestyle="--")


def label_mineral(
    ax: plt.Axes,
    pos: tuple[float, float, float],
    text: str,
    dx: float = 0.0,
    dy: float = 0.0,
    ha: str = "center",
    va: str = "center",
    fs: int = 10,
    **kw,
) -> None:
    """Label a mineral at a ternary position.

    Parameters
    ----------
    ax
        Matplotlib axes.
    pos
        Ternary position.
    text
        Label text.
    dx
        Cartesian x offset.
    dy
        Cartesian y offset.
    ha
        Horizontal alignment.
    va
        Vertical alignment.
    fs
        Font size.
    kw
        Passed through to matplotlib text().
    """
    cx, cy = ternary_to_cartesian(pos)
    ax.text(cx + dx, cy + dy, text, fontsize=fs, ha=ha, va=va, **kw)


# ================================================================
# Build the multi-panel figure
# ================================================================

fig = plt.figure(figsize=(14, 9))
gs = gridspec.GridSpec(
    2,
    2,
    width_ratios=[1.4, 1],
    height_ratios=[1, 1],
    wspace=0.15,
    hspace=0.25,
)

# White background style for labels
WHITEBG_TRANSLUCENT = dict(
    boxstyle="round,pad=0.15",
    facecolor="white",
    edgecolor="none",
    alpha=0.85,
)
WHITEBG = dict(
    boxstyle="round,pad=0.15",
    facecolor="#F8F8F8",
    edgecolor="none",
    alpha=1.0,
)

# ----------------------------------------------------------------
# (a) Main detailed ternary — left column, spanning both rows
# ----------------------------------------------------------------
ax_main = fig.add_subplot(gs[:, 0])
tax_main = ternary.TernaryAxesSubplot(ax=ax_main, scale=1.0)

draw_base_ternary(
    tax_main,
    corner_fontsize=12,
    corner_offset_top=0.14,
    corner_offset_side=0.06,
)
draw_oxidation_grid(tax_main)

# x and z axis labels on the grid
tm0_xy = ternary_to_cartesian(titanomagnetite(0.0))
tm1_xy = ternary_to_cartesian(titanomagnetite(1.0))
tm_dir = np.array(tm1_xy) - np.array(tm0_xy)
tm_perp = np.array([-tm_dir[1], tm_dir[0]])
tm_perp = tm_perp / np.linalg.norm(tm_perp) * 0.025

for x in [0.0, 0.2, 0.4, 0.6, 0.8]:
    pt = titanomagnetite(x)
    cx, cy = ternary_to_cartesian(pt)
    ax_main.text(
        cx + tm_perp[0],
        cy + tm_perp[1],
        f"{x:.1f}",
        fontsize=9,
        ha="center",
        va="bottom",
        bbox=WHITEBG_TRANSLUCENT,
        zorder=10,
    )

# x arrow — at x~0.5, with label on top of arrow
x_label_pt = titanomagnetite(0.5)
cx, cy = ternary_to_cartesian(x_label_pt)
tm_unit = tm_dir / np.linalg.norm(tm_dir) * 0.08
perp_off = tm_perp * 2.5
ax_main.annotate(
    "",
    xy=(cx + tm_unit[0] + perp_off[0], cy + tm_unit[1] + perp_off[1]),
    xytext=(cx - tm_unit[0] + perp_off[0], cy - tm_unit[1] + perp_off[1]),
    arrowprops=dict(arrowstyle="->", color="black", lw=2.0),
)
ax_main.text(
    cx + perp_off[0],
    cy + perp_off[1] - 0.019,
    "$x$",
    fontsize=12,
    ha="center",
    va="bottom",
    style="italic",
    bbox=WHITEBG,
    zorder=10,
)

# z labels along ulvöspinel-pseudobrookite join (x=1 line)
ulv_xy = np.array(ternary_to_cartesian(oxidized_titanomagnetite(1.0, 0.0)))
psb_xy = np.array(ternary_to_cartesian(oxidized_titanomagnetite(1.0, 1.0)))
join_dir = psb_xy - ulv_xy
join_perp = np.array([join_dir[1], -join_dir[0]])
join_perp = join_perp / np.linalg.norm(join_perp) * 0.03

for zv in [0.0, 0.2, 0.4, 0.6, 0.8]:
    pt = oxidized_titanomagnetite(1.0, zv)
    cx, cy = ternary_to_cartesian(pt)
    ax_main.text(
        cx - join_perp[0],
        cy - join_perp[1] - 0.02,
        f"{zv:.1f}",
        fontsize=9,
        ha="center",
        va="bottom",
        bbox=WHITEBG_TRANSLUCENT,
        zorder=10,
    )

# z arrow — along the ulvöspinel-pseudobrookite join
z_start = oxidized_titanomagnetite(1.0, 0.4)
z_end = oxidized_titanomagnetite(1.0, 0.65)
z_s_xy = ternary_to_cartesian(z_start)
z_e_xy = ternary_to_cartesian(z_end)
z_arrow_perp = join_perp * 2.0
ax_main.annotate(
    "",
    xy=(z_e_xy[0] - z_arrow_perp[0], z_e_xy[1] - z_arrow_perp[1]),
    xytext=(z_s_xy[0] - z_arrow_perp[0], z_s_xy[1] - z_arrow_perp[1]),
    arrowprops=dict(arrowstyle="->", color="black", lw=2.0),
)
z_mid_x = (z_s_xy[0] + z_e_xy[0]) / 2.0 - z_arrow_perp[0]
z_mid_y = (z_s_xy[1] + z_e_xy[1]) / 2.0 - z_arrow_perp[1]
ax_main.text(
    z_mid_x,
    z_mid_y - 0.0135,
    "$z$",
    fontsize=12,
    ha="center",
    va="bottom",
    style="italic",
    bbox=WHITEBG,
    zorder=10,
)

# Mineral name labels (fixed: remove misleading 1/3 factors)
label_mineral(
    ax_main,
    titanomagnetite(0.0),
    "$\\mathrm{Fe_3O_4}$\nmagnetite",
    dy=-0.04,
    ha="center",
    va="top",
    fs=10,
)

label_mineral(
    ax_main,
    titanomagnetite(1.0),
    "ulvöspinel\n$\\mathrm{Fe_2TiO_4}$",
    dx=-0.02,
    dy=0.01,
    ha="right",
    va="bottom",
    fs=10,
)

label_mineral(
    ax_main,
    titanohematite(1.0),
    "ilmenite\n$\\mathrm{FeTiO_3}$",
    dx=-0.02,
    dy=0.01,
    ha="right",
    va="bottom",
    fs=10,
)

label_mineral(
    ax_main,
    pseudobrookite,
    "pseudobrookite\n$\\mathrm{Fe_2TiO_5}$",
    dx=0.02,
    dy=0.01,
    ha="left",
    va="bottom",
    fs=10,
)

label_mineral(
    ax_main,
    ferropsdbk,
    "$\\mathrm{FeTi_2O_5}$",
    dx=-0.05,
    dy=0.01,
    ha="right",
    va="bottom",
    fs=10,
)

# Hematite/maghemite label near Fe2O3 corner
fe2o3_xy = ternary_to_cartesian(titanohematite(0.0))
ax_main.text(
    fe2o3_xy[0],
    fe2o3_xy[1] - 0.09,
    "hematite, maghemite",
    fontsize=10,
    ha="center",
    va="top",
)

# Series labels (rotated along joins)
tm_angle = np.degrees(np.arctan2(tm0_xy[1] - tm1_xy[1], tm0_xy[0] - tm1_xy[0]))
tm_mid = titanomagnetite(0.45)
cx, cy = ternary_to_cartesian(tm_mid)
tm_perp_down = -tm_perp / np.linalg.norm(tm_perp) * 0.04
ax_main.text(
    cx + tm_perp_down[0],
    cy + tm_perp_down[1],
    "titanomagnetites",
    fontsize=10,
    ha="center",
    va="top",
    rotation=tm_angle,
    style="italic",
    rotation_mode="anchor",
    bbox=WHITEBG_TRANSLUCENT,
)

th0_xy = ternary_to_cartesian(titanohematite(0.0))
th1_xy = ternary_to_cartesian(titanohematite(1.0))
th_angle = np.degrees(np.arctan2(th0_xy[1] - th1_xy[1], th0_xy[0] - th1_xy[0]))
th_mid = titanohematite(0.5)
cx, cy = ternary_to_cartesian(th_mid)
ax_main.text(
    cx + 0.04,
    cy - 0.01,
    "titanohematites",
    fontsize=10,
    ha="center",
    va="top",
    rotation=th_angle,
    style="italic",
    rotation_mode="anchor",
    bbox=WHITEBG_TRANSLUCENT,
)

# Panel label
ax_main.text(
    0.02,
    0.98,
    "(a)",
    fontsize=14,
    fontweight="bold",
    transform=ax_main.transAxes,
    va="top",
    ha="left",
)

tax_main._redraw_labels()

# ----------------------------------------------------------------
# (b) High-temperature oxyexsolution — upper right
# ----------------------------------------------------------------
ax_ht = fig.add_subplot(gs[0, 1])
tax_ht = ternary.TernaryAxesSubplot(ax=ax_ht, scale=1.0)

draw_base_ternary(
    tax_ht,
    show_gridlines=False,
    corner_fontsize=10,
    corner_offset_top=0.16,
    corner_offset_side=0.08,
    show_mineral_names=False,
    detailed_corners=False,
)
draw_oxidation_grid(tax_ht)

x_start = 0.6
start_pt = titanomagnetite(x_start)
start_xy = ternary_to_cartesian(start_pt)

mag_target = titanomagnetite(0.05)
mag_xy = ternary_to_cartesian(mag_target)
ax_ht.annotate(
    "",
    xy=mag_xy,
    xytext=start_xy,
    arrowprops=dict(
        arrowstyle="->",
        color="#cc0000",
        lw=3.5,
    ),
)

ilm_target_xy = ternary_to_cartesian(titanohematite(0.95))
ax_ht.annotate(
    "",
    xy=ilm_target_xy,
    xytext=start_xy,
    arrowprops=dict(
        arrowstyle="->",
        color="#cc0000",
        lw=3.5,
    ),
)

ax_ht.scatter(
    start_xy[0],
    start_xy[1],
    marker="o",
    color="#cc0000",
    s=60,
    zorder=5,
)

ax_ht.text(
    start_xy[0] - 0.15,
    start_xy[1] - 0.04,
    "high-T\noxyexsolution",
    fontsize=10,
    color="#cc0000",
    ha="center",
    va="top",
    fontweight="bold",
    bbox=WHITEBG_TRANSLUCENT,
)

ax_ht.text(
    mag_xy[0],
    mag_xy[1] - 0.04,
    "low-Ti magnetite\nlamellae",
    fontsize=8,
    color="#cc0000",
    ha="center",
    va="top",
    style="italic",
)
ax_ht.text(
    ilm_target_xy[0] - 0.04,
    ilm_target_xy[1] + 0.02,
    "ilmenite\nlamellae",
    fontsize=8,
    color="#cc0000",
    ha="right",
    va="bottom",
    style="italic",
)

ax_ht.text(
    0.02,
    0.98,
    "(b)",
    fontsize=14,
    fontweight="bold",
    transform=ax_ht.transAxes,
    va="top",
    ha="left",
)

tax_ht._redraw_labels()

# ----------------------------------------------------------------
# (c) Low-temperature oxidation — lower right
# ----------------------------------------------------------------
ax_lt = fig.add_subplot(gs[1, 1])
tax_lt = ternary.TernaryAxesSubplot(ax=ax_lt, scale=1.0)

draw_base_ternary(
    tax_lt,
    show_gridlines=False,
    corner_fontsize=10,
    corner_offset_top=0.16,
    corner_offset_side=0.08,
    show_mineral_names=False,
    detailed_corners=False,
)
draw_oxidation_grid(tax_lt)

mag_start = titanomagnetite(0.0)
mag_end = oxidized_titanomagnetite(0.0, 1.0)
mag_s_xy = ternary_to_cartesian(mag_start)
mag_e_xy = ternary_to_cartesian(mag_end)
ax_lt.annotate(
    "",
    xy=mag_e_xy,
    xytext=mag_s_xy,
    arrowprops=dict(arrowstyle="->", color="#0055aa", lw=3.5),
)

tm04_start = titanomagnetite(0.4)
tm04_end = oxidized_titanomagnetite(0.4, 0.75)
tm04_s_xy = ternary_to_cartesian(tm04_start)
tm04_e_xy = ternary_to_cartesian(tm04_end)
ax_lt.annotate(
    "",
    xy=tm04_e_xy,
    xytext=tm04_s_xy,
    arrowprops=dict(arrowstyle="->", color="#0055aa", lw=3.5),
)

mid_x = (mag_s_xy[0] + tm04_s_xy[0]) / 2.0
mid_y = (mag_s_xy[1] + tm04_s_xy[1]) / 2.0
ax_lt.text(
    mid_x,
    mid_y + 0.15,
    "low-T oxidation\n(maghemitization)",
    fontsize=10,
    color="#0055aa",
    ha="center",
    va="bottom",
    bbox=WHITEBG_TRANSLUCENT,
    fontweight="bold",
)

ax_lt.text(
    0.02,
    0.98,
    "(c)",
    fontsize=14,
    fontweight="bold",
    transform=ax_lt.transAxes,
    va="top",
    ha="left",
)

tax_lt._redraw_labels()

# ================================================================
# Save
# ================================================================
plt.savefig(
    "../book/figures/chapter6/oxide_ternary.png",
    dpi=300,
    bbox_inches="tight",
    facecolor="white",
)
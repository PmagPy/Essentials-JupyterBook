"""
Chapter 9 figure: Effect of overlapping coercivity spectra on Zijderveld diagrams.

Self-contained script (no local imports) for use in the Essentials of
Paleomagnetism textbook. Generates a 3×2 panel figure showing progressively
increasing overlap between two log-Gaussian coercivity spectra, with
equal-intensity components and vector-addition arrows on the Zij plots.

After Dunlop (1979), modified.

Usage:
    mamba activate pmagpy-dev
    python chapter9_zij_overlap.py
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import lognorm
from pmagpy import pmag

try:
    from adjustText import adjust_text
    _HAS_ADJUSTTEXT = True
except ImportError:
    _HAS_ADJUSTTEXT = False


# ============================================================================
# Plotting functions (self-contained versions of plot_zij and overlay_components)
# ============================================================================

def plot_zij(fignum, datablock, angle=0, s='', norm=True,
             label_steps=False, label_list=None, label_map=None,
             unit='', ax=None, pad=0.1, title=None):
    """
    Make a Zijderveld (vector component) diagram.

    Based on pmagplotlib.plot_zij with improvements:
    - label_list selects which steps to annotate
    - label_map overrides label text (default: {0: 'NRM'})
    - ax parameter for subplot embedding
    - pad adds fractional padding around data extent
    - title='' suppresses the title; title=None uses default
    - Tick labels suppressed; cross-hairs span full axis range
    - Uses adjustText to resolve overlapping labels if installed
    """
    if label_list is not None:
        label_steps = True
    if label_map is None:
        label_map = {0: 'NRM'}

    if ax is None:
        plt.figure(num=fignum)
        plt.clf()
        ax = plt.gca()

    # Normalization factor
    if norm:
        try:
            fact = 1.0 / datablock[0][3]
        except ZeroDivisionError:
            fact = 1.0
    else:
        fact = 1.0

    # Build DataFrame from datablock
    data = pd.DataFrame(datablock)
    if len(data.columns) == 5:
        data.columns = ['treat', 'dec', 'inc', 'int', 'quality']
    elif len(data.columns) == 6:
        data.columns = ['treat', 'dec', 'inc', 'int', 'type', 'quality']
    elif len(data.columns) == 7:
        data.columns = ['treat', 'dec', 'inc', 'int', 'type', 'quality', 'y']

    data['int'] = data['int'] * fact
    data['dec'] = (data['dec'] - angle) % 360

    gdata = data[data['quality'].str.contains('g')]
    bdata = data[data['quality'].str.contains('b')]

    forVDS = gdata[['dec', 'inc', 'int']].values
    gXYZ = pd.DataFrame(pmag.dir2cart(forVDS), columns=['X', 'Y', 'Z'])

    # Compute axis limits with padding
    all_vals = np.concatenate([gXYZ['X'], gXYZ['Y'], gXYZ['Z']])
    amax = np.max(all_vals)
    amin = np.min(all_vals)
    if amin > 0:
        amin = 0
    if amax < 0:
        amax = 0
    span = amax - amin
    if span == 0:
        span = 1.0
    amin -= pad * span
    amax += pad * span

    # Plot bad-quality points
    if len(bdata) > 0:
        bXYZ = pd.DataFrame(
            pmag.dir2cart(bdata[['dec', 'inc', 'int']].values),
            columns=['X', 'Y', 'Z'],
        )
        ax.scatter(bXYZ['X'], bXYZ['Y'], marker='d', c='y', s=30)
        ax.scatter(bXYZ['X'], bXYZ['Z'], marker='d', c='y', s=30)

    # Horizontal projection (filled red circles)
    ax.plot(gXYZ['X'], gXYZ['Y'], 'ro')
    ax.plot(gXYZ['X'], gXYZ['Y'], 'r-')

    # Vertical projection (open blue squares)
    ax.plot(gXYZ['X'], gXYZ['Z'], 'ws', markeredgecolor='blue')
    ax.plot(gXYZ['X'], gXYZ['Z'], 'b-')

    # Annotate points
    treat_vals = gdata['treat'].values
    texts = []
    for k in range(len(gXYZ)):
        val = treat_vals[k]
        if label_list is not None and val not in label_list:
            continue
        if val in label_map:
            lbl = label_map[val]
        elif not label_steps and label_list is None:
            lbl = str(k)
        else:
            if val == int(val):
                lbl = f"{int(val)}"
            else:
                lbl = f"{val:g}"
            if unit:
                lbl += f" {unit}"
        txt = ax.text(gXYZ['X'].iloc[k], gXYZ['Z'].iloc[k], lbl,
                      fontsize=8, ha='left', va='bottom')
        texts.append(txt)

    # Set axis limits (inverted y-axis is the Zij convention)
    ax.axis([amin, amax, amax, amin])

    # Axis cross-hairs spanning the full plot range
    ax.axhline(0, color='k', linewidth=0.8)
    ax.axvline(0, color='k', linewidth=0.8)

    # Labels
    ax.set_ylabel('Circles: Y; Squares: Z')
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_aspect('equal')
    if title is None:
        tstring = s + ': NRM = ' + '%9.2e' % (datablock[0][3])
        ax.set_title(tstring)
    elif title:
        ax.set_title(title)

    # Use adjustText to resolve label overlaps if available
    if _HAS_ADJUSTTEXT and texts:
        adjust_text(texts, ax=ax,
                    only_move={'text': 'xy'},
                    force_text=(0.5, 0.8),
                    force_points=(0.3, 0.5))

    return ax


def overlay_components(ax, comp_A_cart, comp_B_cart, angle=0, norm_factor=1.0,
                       color_A='#D55E00', color_B='#0072B2',
                       label_A='$M_A$', label_B='$M_B$',
                       arrow_kw=None):
    """
    Overlay component vectors on a Zijderveld diagram showing how they
    sum to produce the NRM.

    Draws arrows for both the horizontal and vertical projections:
      Origin -> M_B (blue) and M_B -> NRM (orange, representing M_A).
    This shows the vector addition NRM = M_A + M_B.
    """
    a = np.radians(angle)

    def _project(cart):
        x, y, z = cart * norm_factor
        x_rot = x * np.cos(a) + y * np.sin(a)
        y_rot = -x * np.sin(a) + y * np.cos(a)
        return x_rot, y_rot, z

    A = _project(np.asarray(comp_A_cart))
    B = _project(np.asarray(comp_B_cart))
    NRM = (A[0] + B[0], A[1] + B[1], A[2] + B[2])

    alpha = 0.7
    shaft_width = 0.025
    head_width = 0.072
    head_length = 0.042
    if arrow_kw:
        alpha = arrow_kw.get('alpha', alpha)
        shaft_width = arrow_kw.get('width', shaft_width)
        head_width = arrow_kw.get('head_width', head_width)
        head_length = arrow_kw.get('head_length', head_length)

    for y_idx in ('horiz', 'vert'):
        idx = 1 if y_idx == 'horiz' else 2

        b_tip = (B[0], B[idx])
        nrm_tip = (NRM[0], NRM[idx])

        ax.arrow(0, 0, b_tip[0], b_tip[1],
                 width=shaft_width, head_width=head_width,
                 head_length=head_length, fc=color_B, ec='none',
                 alpha=alpha, length_includes_head=True, zorder=10)
        dx = nrm_tip[0] - b_tip[0]
        dy = nrm_tip[1] - b_tip[1]
        ax.arrow(b_tip[0], b_tip[1], dx, dy,
                 width=shaft_width, head_width=head_width,
                 head_length=head_length, fc=color_A, ec='none',
                 alpha=alpha, length_includes_head=True, zorder=10)

    # Labels offset from the midpoint of each arrow (horizontal projection)
    b_mid_h = (B[0] / 2, B[1] / 2)
    ax.annotate(label_B, xy=b_mid_h, xytext=(-18, 12),
                textcoords='offset points', fontsize=11, fontweight='bold',
                color=color_B, ha='center', va='center',
                bbox=dict(facecolor='white', edgecolor='none', alpha=0.7, pad=1),
                zorder=11)
    a_mid_h = ((B[0] + NRM[0]) / 2, (B[1] + NRM[1]) / 2)
    ax.annotate(label_A, xy=a_mid_h, xytext=(18, 12),
                textcoords='offset points', fontsize=11, fontweight='bold',
                color=color_A, ha='center', va='center',
                bbox=dict(facecolor='white', edgecolor='none', alpha=0.7, pad=1),
                zorder=11)


# ============================================================================
# Data generation
# ============================================================================

def generate_demag_data(steps, comp_A_cart, comp_B_cart,
                        median_A, dp_A, median_B, dp_B):
    """Generate synthetic demagnetization data with log-Gaussian spectra."""
    frac_A = 1.0 - lognorm.cdf(steps, s=dp_A, scale=median_A)
    frac_B = 1.0 - lognorm.cdf(steps, s=dp_B, scale=median_B)
    demag_data = []
    for i, step in enumerate(steps):
        total_cart = frac_A[i] * comp_A_cart + frac_B[i] * comp_B_cart
        total_dir = pmag.cart2dir(total_cart)
        dec, inc, mag = total_dir[0], total_dir[1], total_dir[2]
        if np.isnan(dec):
            dec = 0.0
        if np.isnan(inc):
            inc = 0.0
        demag_data.append([step, dec, inc, mag, 'DA', 'g'])
    return demag_data


# ============================================================================
# Figure parameters
# ============================================================================

# Component directions
comp_A_dir = [0.0, 60.0]     # overprint: North, steeply down
comp_B_dir = [270.0, 20.0]   # ancient: W, shallowly down

# Equal intensities for illustrative clarity
intensity = 0.50
A_cart = np.array(pmag.dir2cart([comp_A_dir[0], comp_A_dir[1], intensity]))
B_cart = np.array(pmag.dir2cart([comp_B_dir[0], comp_B_dir[1], intensity]))
nrm_dec = pmag.cart2dir(A_cart + B_cart)[0]

# AF demagnetization steps and smooth curve for spectra
af_steps = np.array([0, 2, 5, 8, 10, 15, 20, 25, 30, 35, 40, 45, 50,
                     60, 70, 80, 90, 100, 120, 140, 160, 180, 200])
af_fine = np.linspace(0.1, 200, 500)

# Three cases with progressively increasing overlap
cases = [
    {'median_A': 12, 'dp_A': 0.4, 'median_B': 100, 'dp_B': 0.3,
     'row_title': 'Non-overlapping spectra'},
    {'median_A': 20, 'dp_A': 0.5, 'median_B': 70,  'dp_B': 0.4,
     'row_title': 'Small overlap'},
    {'median_A': 30, 'dp_A': 0.6, 'median_B': 50,  'dp_B': 0.5,
     'row_title': 'Large overlap'},
]


# ============================================================================
# Build the figure
# ============================================================================

fig, axes = plt.subplots(3, 2, figsize=(10, 9))

for row, case in enumerate(cases):
    ax_spec = axes[row, 0]
    ax_zij = axes[row, 1]

    data = generate_demag_data(
        af_steps, A_cart, B_cart,
        case['median_A'], case['dp_A'], case['median_B'], case['dp_B'])

    # --- Left: coercivity spectra ---
    spec_A = intensity * lognorm.pdf(af_fine, s=case['dp_A'], scale=case['median_A'])
    spec_B = intensity * lognorm.pdf(af_fine, s=case['dp_B'], scale=case['median_B'])
    ax_spec.fill_between(af_fine, spec_A, alpha=0.3, color='#D55E00')
    ax_spec.fill_between(af_fine, spec_B, alpha=0.3, color='#0072B2')
    ax_spec.plot(af_fine, spec_A, color='#D55E00', linewidth=1.5)
    ax_spec.plot(af_fine, spec_B, color='#0072B2', linewidth=1.5)

    # Labels inside the curves at the peak
    for median, dp, label, color in [
        (case['median_A'], case['dp_A'], '$M_A$', '#D55E00'),
        (case['median_B'], case['dp_B'], '$M_B$', '#0072B2'),
    ]:
        peak_y = intensity * lognorm.pdf(median, s=dp, scale=median)
        ax_spec.text(median, peak_y * 0.45, label, ha='center', va='center',
                     fontsize=13, fontweight='bold', color=color)

    ax_spec.set_ylabel('dM/dB', fontsize=11)
    ax_spec.set_xlim(0.1, 200)
    ax_spec.set_ylim(bottom=0)
    ax_spec.set_title(case['row_title'], fontsize=12, loc='left')
    if row == 2:
        ax_spec.set_xlabel('AF level (mT)', fontsize=11)
    else:
        ax_spec.set_xticklabels([])

    # --- Right: Zijderveld diagram ---
    plot_zij(None, data, angle=nrm_dec, s='',
             label_list=[0, 15, 30, 60], unit='mT',
             ax=ax_zij, title='')

    # Show vector addition on all cases
    nrm_intensity = data[0][3]
    overlay_components(ax_zij, A_cart, B_cart,
                       angle=nrm_dec, norm_factor=1.0 / nrm_intensity)

# Force all Zij panels to share the same axis limits (use the first panel's range)
zij_lims = axes[0, 1].axis()
for row in range(1, 3):
    axes[row, 1].axis(zij_lims)

fig.tight_layout()
fig.savefig('../book/figures/chapter9/zij_overlap.png', dpi=300, bbox_inches='tight')
plt.show()

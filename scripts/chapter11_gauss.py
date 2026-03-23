"""Generate four-panel Gaussian/CLT/chi-squared demonstration figure.

Reproduces the logic of gauss.png (Chapter 11):
    a) Standard normal probability density function with square markers
    b) Histogram of N=1000 draws from N(mu=10, sigma=3) with PDF overlay
    c) Histogram of sample means from 100 repeated trials (CLT demonstration)
    d) Histogram of sample variances from the same trials (chi-squared shape)
"""

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# Use project figure style
sys.path.insert(0, str(Path(__file__).parent))
from figure_style import apply_mpl_style

apply_mpl_style()


# Reproducible random state
rng = np.random.default_rng(42)

# Parameters matching the original figure description
mu = 15.0
sigma = 3.0
n_single = 1000
n_trials = 100
n_per_trial = 1000

# --- Generate data ---
# Panel b: one set of 1000 bed-thickness measurements
bed_thickness = rng.normal(loc=mu, scale=sigma, size=n_single)

# Panels c & d: 100 repeated trials of 1000 measurements each
repeated_trials = rng.normal(loc=mu, scale=sigma, size=(n_trials, n_per_trial))
trial_means = repeated_trials.mean(axis=1)
trial_variances = repeated_trials.var(axis=1, ddof=1)

# --- Create figure ---
fig, axes = plt.subplots(2, 2, figsize=(8, 7))

# --- Panel a: Standard normal PDF ---
ax = axes[0, 0]
z = np.linspace(-4, 4, 500)
pdf_z = norm.pdf(z)

# Red dashed line with red square markers (matching original)
z_markers = np.linspace(-3.5, 3.5, 50)
ax.plot(z, pdf_z, 'r--', lw=1.5)
ax.plot(z_markers, norm.pdf(z_markers), 's', color='red',
        markersize=4, markeredgecolor='black', markeredgewidth=0.5)
ax.axvline(0.0, color='grey', lw=0.8, alpha=0.5)
ax.set_xlim(-4, 4)
ax.set_ylim(0, 0.42)
ax.set_xlabel('z')
ax.set_ylabel('f(z)')
ax.text(0.05, 0.90, 'a)', transform=ax.transAxes, fontsize=14,
        fontweight='bold')

# --- Panel b: Histogram of bed thickness with normal PDF overlay ---
ax = axes[0, 1]
bin_width_b = 0.5
bins_b = np.arange(mu - 5 * sigma, mu + 5 * sigma, bin_width_b)
ax.hist(bed_thickness, bins=bins_b,
        histtype='step', color='black', linewidth=0.8)

x_fit = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 400)
ax.plot(x_fit, n_single * bin_width_b * norm.pdf(x_fit, loc=mu, scale=sigma),
        'r--', lw=2)
ax.set_xlabel('Bed thickness (cm)')
ax.set_ylabel('Count')
ax.set_xlim(mu - 4 * sigma, mu + 4 * sigma)
ax.text(0.05, 0.90, 'b)', transform=ax.transAxes, fontsize=14,
        fontweight='bold')
ax.text(0.65, 0.90, f'N  =  {n_single}', transform=ax.transAxes,
        fontsize=11)

# --- Panel c: Histogram of sample means ---
ax = axes[1, 0]
sigma_mean = sigma / np.sqrt(n_per_trial)
bins_c = np.linspace(trial_means.min() - 0.05, trial_means.max() + 0.05, 25)
bin_width_c = bins_c[1] - bins_c[0]
ax.hist(trial_means, bins=bins_c,
        histtype='step', color='black', linewidth=0.8)

x_fit_c = np.linspace(trial_means.min() - 3 * sigma_mean,
                       trial_means.max() + 3 * sigma_mean, 400)
ax.plot(x_fit_c, n_trials * bin_width_c * norm.pdf(x_fit_c, loc=mu, scale=sigma_mean),
        'r--', lw=2)
ax.set_xlabel('Means of repeat trials')
ax.set_ylabel('Count')
ax.text(0.05, 0.90, 'c)', transform=ax.transAxes, fontsize=14,
        fontweight='bold')
ax.text(0.60, 0.90, f'N  =  {n_trials}', transform=ax.transAxes,
        fontsize=11)

# --- Panel d: Histogram of sample variances ---
ax = axes[1, 1]
bins_d = np.linspace(trial_variances.min(), trial_variances.max(), 25)
ax.hist(trial_variances, bins=bins_d,
        histtype='step', color='black', linewidth=0.8)
ax.set_xlabel('Variance')
ax.set_ylabel('Count')
ax.text(0.05, 0.90, 'd)', transform=ax.transAxes, fontsize=14,
        fontweight='bold')
ax.text(0.60, 0.90, f'N  =  {n_trials}', transform=ax.transAxes,
        fontsize=11)

fig.tight_layout()

outpath = Path(__file__).parent.parent / 'book' / 'figures' / 'chapter11' / 'gauss_code.png'
fig.savefig(outpath, dpi=300, bbox_inches='tight', facecolor='white')
print(f'Saved to {outpath}')
plt.close(fig)

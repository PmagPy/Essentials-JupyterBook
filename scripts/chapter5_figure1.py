# @title Putting it all together for a new Essentials Figure { display-mode: "form" }

import io
import urllib.request

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

# If you want "retina" inline figures in Jupyter, run (in its own cell):
# %config InlineBackend.figure_format = "retina"

# ---------------------------
# Panel (a): load PNG from GitHub
# ---------------------------
panel_a_url = (
    "https://github.com/Institute-for-Rock-Magnetism/2026_ESCI_pmag_course/raw/refs/heads/main/"
    "W3_anisotropy_hysteresis/images/magnetite_w_easy_axis.png"
)

with urllib.request.urlopen(panel_a_url) as resp:
    panel_a_img = mpimg.imread(io.BytesIO(resp.read()))

# ---------------------------
# Model setup (self-contained)
# ---------------------------
# Constants
mu0 = 4 * np.pi * 1e-7
M_s = 480e3  # A/m (magnetite)

# Angle grid
theta_deg = np.linspace(0.0, 180.0, 1801)  # fine grid for smooth curves
theta = np.deg2rad(theta_deg)

# Shape anisotropy: prolate spheroid with elongation q = a/b
q = 2.0


def demag_factors_prolate(q: float) -> tuple[float, float]:
    """Demagnetizing factors for a prolate spheroid.

    Parameters
    ----------
    q : float
        Elongation ratio a/b (>1 for prolate).

    Returns
    -------
    tuple[float, float]
        (N_a, N_b) where N_a is along the symmetry/easy axis and
        N_b is perpendicular (with N_b = N_c for a spheroid).
    """
    if q <= 1:
        raise ValueError("q must be > 1 for a prolate spheroid.")

    e = np.sqrt(1.0 - 1.0 / q**2)
    N_a = (1.0 - e**2) / (2.0 * e**3) * (np.log((1.0 + e) / (1.0 - e)) - 2.0 * e)
    N_b = (1.0 - N_a) / 2.0
    return float(N_a), float(N_b)


N_a, N_b = demag_factors_prolate(q)

# Shape-anisotropy constant (Tauxe: K_u = 1/2 mu0 (N_b - N_a) M_s^2)
K_u = 0.5 * mu0 * (N_b - N_a) * M_s**2

# Energy densities
epsilon_a = K_u * np.sin(theta) ** 2  # anisotropy energy density

# Panel (b): B = 0 mT (only epsilon_a matters)
phi_deg = 45.0
epsilon_a_0 = epsilon_a
i_min_b = int(np.argmin(epsilon_a_0))

# Panel (c): finite B = 30 mT
B_mT_c = 30.0
B_c = B_mT_c * 1e-3  # Tesla
phi = np.deg2rad(phi_deg)

epsilon_m_c = -M_s * B_c * np.cos(phi - theta)  # interaction energy density
epsilon_t_c = epsilon_a + epsilon_m_c           # total energy density
i_min_c = int(np.argmin(epsilon_t_c))

# Panel (d): finite B = 500 mT
B_mT_d = 500.0
B_d = B_mT_d * 1e-3  # Tesla

epsilon_m_d = -M_s * B_d * np.cos(phi - theta)  # interaction energy density
epsilon_t_d = epsilon_a + epsilon_m_d           # total energy density
i_min_d = int(np.argmin(epsilon_t_d))

# ---------------------------
# Figure layout
# ---------------------------
fig = plt.figure(figsize=(12, 9))
gs = fig.add_gridspec(
    nrows=3,
    ncols=2,
    width_ratios=[1.0, 1.9],
    height_ratios=[1.0, 1.0, 1.0],
    wspace=0.25,
    hspace=0.30,
)

ax_a = fig.add_subplot(gs[:, 0])
ax_b = fig.add_subplot(gs[0, 1])
ax_c = fig.add_subplot(gs[1, 1])
ax_d = fig.add_subplot(gs[2, 1])

# ---------------- Panel (a) ----------------
ax_a.imshow(panel_a_img)
ax_a.axis("off")
ax_a.text(
    0.02,
    0.98,
    "a)",
    transform=ax_a.transAxes,
    va="top",
    ha="left",
    fontsize=16,
    fontweight="bold",
)

# Common axis styling
def style_axes(ax: plt.Axes) -> None:
    ax.set_xlim(0, 180)
    ax.set_xticks(np.arange(0, 181, 20))
    ax.tick_params(direction="in", length=6, width=1)
    for spine in ax.spines.values():
        spine.set_linewidth(1.8)
    ax.grid(True)


# ---------------- Panel (b) ----------------
ax_b.plot(theta_deg, epsilon_a_0, linewidth=2.5, label=r"$\epsilon_a$")
ax_b.axvline(phi_deg, color='gray', linestyle='--', linewidth=1)
ax_b.set_ylabel(r"Energy density (J m$^{-3}$)")
ax_b.set_title(rf"b) $B = 0$ mT ($\phi = {phi_deg:.0f}^\circ$)")

ax_b.scatter(
    theta_deg[i_min_b],
    epsilon_a_0[i_min_b],
    s=70,
    facecolors="none",
    edgecolors="k",
    zorder=5,
)
ax_b.text(
    theta_deg[i_min_b] + 5,
    epsilon_a_0[i_min_b] + 0.05 * (epsilon_a_0.max() - epsilon_a_0.min()),
    r"$\epsilon_{\min}$",
    fontsize=12,
    bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.7, edgecolor='none'),
)

# Label the applied field line
ax_b.text(
    phi_deg, 0.95, "applied\nfield",
    transform=ax_b.get_xaxis_transform(),
    ha='center', va='top', fontsize=10,
    bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.7, edgecolor='none'),
)

style_axes(ax_b)
ax_b.legend(loc="best", frameon=True)

# ---------------- Panel (c) ----------------
ax_c.plot(theta_deg, epsilon_a, linewidth=2.5, label=r"$\epsilon_a$")
ax_c.plot(theta_deg, epsilon_m_c, "--", linewidth=2.5, label=r"$\epsilon_m$")
ax_c.plot(
    theta_deg,
    epsilon_t_c,
    linewidth=4.0,
    label=r"$\epsilon_t=\epsilon_a+\epsilon_m$",
)

ax_c.axvline(phi_deg, color='gray', linestyle='--', linewidth=1)
ax_c.set_ylabel(r"Energy density (J m$^{-3}$)")
ax_c.set_title(rf"c) $B = {B_mT_c:.0f}$ mT ($\phi = {phi_deg:.0f}^\circ$)")

ax_c.scatter(
    theta_deg[i_min_c],
    epsilon_t_c[i_min_c],
    s=70,
    facecolors="none",
    edgecolors="k",
    zorder=5,
)
ax_c.text(
    theta_deg[i_min_c] + 5,
    epsilon_t_c[i_min_c] + 0.05 * (epsilon_t_c.max() - epsilon_t_c.min()),
    r"$\epsilon_{\min}$",
    fontsize=12,
    bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.7, edgecolor='none'),
)

# No applied field label in panel c to avoid overlap with legend

style_axes(ax_c)
ax_c.legend(loc="best", frameon=True)

# ---------------- Panel (d) ----------------
ax_d.plot(theta_deg, epsilon_a, linewidth=2.5, label=r"$\epsilon_a$")
ax_d.plot(theta_deg, epsilon_m_d, "--", linewidth=2.5, label=r"$\epsilon_m$")
ax_d.plot(
    theta_deg,
    epsilon_t_d,
    linewidth=4.0,
    label=r"$\epsilon_t=\epsilon_a+\epsilon_m$",
)

ax_d.axvline(phi_deg, color='gray', linestyle='--', linewidth=1)
ax_d.set_xlabel(r"$\theta$ (degrees)")
ax_d.set_ylabel(r"Energy density (J m$^{-3}$)")
ax_d.set_title(rf"d) $B = {B_mT_d:.0f}$ mT ($\phi = {phi_deg:.0f}^\circ$)")

ax_d.scatter(
    theta_deg[i_min_d],
    epsilon_t_d[i_min_d],
    s=70,
    facecolors="none",
    edgecolors="k",
    zorder=5,
)
ax_d.text(
    theta_deg[i_min_d] + 5,
    epsilon_t_d[i_min_d] + 0.05 * (epsilon_t_d.max() - epsilon_t_d.min()),
    r"$\epsilon_{\min}$",
    fontsize=12,
    bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.7, edgecolor='none'),
)

# Label the applied field line
ax_d.text(
    phi_deg, 0.95, "applied\nfield",
    transform=ax_d.get_xaxis_transform(),
    ha='center', va='top', fontsize=10,
    bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.7, edgecolor='none'),
)

style_axes(ax_d)
ax_d.legend(loc="best", frameon=True)

# Save figure
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(script_dir, "..", "book", "figures", "chapter5")
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "chapter5_figure1.png")
plt.savefig(output_path, dpi=150, bbox_inches='tight')
print(f"Figure saved to: {output_path}")
plt.show()
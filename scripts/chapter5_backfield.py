#@title Backfield Demagnetization (Conceptual)
import numpy as np
import matplotlib.pyplot as plt

def logistic(x, x0, k):
    return 1 / (1 + np.exp(-(x - x0) / k))

# --- Conceptual backfield curve ---
Bmag = np.linspace(0, 700, 600)  # |B| (mT)
soft = 0.55 * logistic(Bmag, x0=160, k=30)
hard = 0.45 * logistic(Bmag, x0=430, k=70)
Mr = 1 - 2 * (soft + hard)
Mr = Mr / Mr[0]  # normalize so curve starts at exactly 1.0
B = -Bmag  # signed backfield axis

# B_cr from M_r = 0
idx = np.where(np.diff(np.signbit(Mr)))[0]
if len(idx) > 0:
    i = idx[0]
    Bcr_mag = np.interp(0, [Mr[i], Mr[i + 1]], [Bmag[i], Bmag[i + 1]])
    Bcr = -Bcr_mag
else:
    Bcr_mag = np.nan
    Bcr = np.nan

# Figure layout
fig = plt.figure(figsize=(11.0, 5.0))
gs = fig.add_gridspec(1, 2, width_ratios=[1.15, 2.25], wspace=0.45)

# --- Left panel: protocol ---
axL = fig.add_subplot(gs[0, 0])
axL.set_xlim(0, 1)
axL.set_ylim(0, 1)
axL.axis("off")
axL.set_title("Protocol", fontsize=14, pad=10, loc="center")

n_pairs = 8
y0, dy = 0.8, 0.037
blue_field_T = 2.0                   # scale reference for blue arrow (+2.0 T)
brown_fields_mT = np.array([-15, -30, -60, -120, -240, -480, -960, -1920], dtype=float)
brown_fields_T = brown_fields_mT / 1000.0

# Place caption text right-justified, then measure width to set arrow length
caption_blue = axL.text(1.0, 0.95, "Impart SIRM", fontsize=8.5,
                        va="bottom", ha="right",
                        color="#0072B2", fontweight="bold")
caption_brown = axL.text(1.0, 0.9, "Progressively larger backfields",
                         fontsize=8.5, va="bottom", ha="right",
                         color="#8C510A", fontweight="bold")
caption_blue = axL.text(1.0, 0.85, "Measure after backfield", fontsize=8.5,
                        va="bottom", ha="right",
                        color="#636363", fontweight="bold")

# Render once to measure the brown caption width in axes coords
fig.canvas.draw()
renderer = fig.canvas.get_renderer()
bb = caption_brown.get_window_extent(renderer)
bb_axes = axL.transData.inverted().transform(bb)
blue_len = bb_axes[1, 0] - bb_axes[0, 0]  # text width in axes coords

x_right = 1.0                        # arrows right-aligned with caption text
blue_start = x_right - blue_len

# Brown arrow lengths on same field scale as blue
brown_lens = blue_len * (np.abs(brown_fields_T) / blue_field_T)

for k in range(n_pairs):
    y_blue = y0 - (3 * k) * dy
    y_brown = y0 - (3 * k + 1) * dy
    y_meas = y0 - (3 * k + 2) * dy

    # +SIRM step (right-pointing)
    axL.arrow(
        blue_start, y_blue, blue_len, 0,
        width=0.0050, head_width=0.022, head_length=0.032,
        length_includes_head=True, color="#0072B2"
    )

    # Reverse backfield step (left-pointing)
    axL.arrow(
        x_right, y_brown, -brown_lens[k], 0,
        width=0.0045, head_width=0.020, head_length=0.028,
        length_includes_head=True, color="#8C510A"
    )

    # Field labels past arrow tips
    axL.text(x_right + 0.02, y_blue, f"+{blue_field_T:.1f} T",
             fontsize=7.5, color="#0072B2", va="center", ha="left")
    axL.text(x_right + 0.02, y_brown, f"{brown_fields_T[k]:.3g} T",
             fontsize=7.5, color="#8C510A", va="center", ha="left")

    # Measure step — right-aligned
    axL.text(1.0, y_meas, r"measure $M_r$ at 0 T",
             fontsize=8, color="#666666", va="center", ha="right",
             fontstyle="italic")

# --- Main panel ---
ax = fig.add_subplot(gs[0, 1])
ax.plot(B, Mr, color="#009E73", lw=2.7, label="Backfield demagnetization curve")
ax.axhline(0, color="black", lw=1)

ax.axvspan(-260, -72, color="#56B4E9", alpha=0.14, label="Soft fraction switches")
ax.axvspan(-620, -360, color="#CC79A7", alpha=0.12, label="Hard fraction switches")

if np.isfinite(Bcr):
    ax.axvline(Bcr, color="#E69F00", lw=2, ls="--",
               label=fr"$B_{{cr}} \approx {Bcr_mag:.0f}\,\mathrm{{mT}}$")
    ax.plot(Bcr, 0, "o", color="#E69F00", ms=8)
    # label close to Bcr point, offset just above
    ax.annotate(
        r"Coercivity of" + "\n"
        + r"remanence, $B_{cr}$" + "\n"
        + r"(where $M_r = 0$)",
        xy=(Bcr, 0), xytext=(Bcr - 120, 0.18),
        arrowprops=dict(arrowstyle="->", lw=1.2, color="#E69F00"),
        fontsize=10, color="#7A5200", ha="center"
    )

# SIRM label — shifted right, close to curve start
ax.annotate(
    "Initial\nSIRM",
    xy=(0, Mr[0]), xytext=(-45, 0.78),
    arrowprops=dict(arrowstyle="->", lw=1.1), fontsize=10,
    ha="center"
)

# -SIRM label — shifted left, close to endpoint
ax.annotate(
    r"At large" + "\n" + r"reverse fields," + "\n" + r"$M_r \rightarrow -$SIRM",
    xy=(B[-1], Mr[-1]), xytext=(-680, -0.75),
    arrowprops=dict(arrowstyle="->", lw=1.1), fontsize=10
)

ax.set_title("Backfield Demagnetization Curve", fontsize=14, pad=10)
ax.set_xlabel(r"Applied reverse field $B$ (mT)", fontsize=12)
ax.set_ylabel(r"Normalized remanence $M_r$/SIRM", fontsize=12)
ax.set_xlim(-700, 0)
ax.set_ylim(-1.05, 1.05)
ax.grid(alpha=0.25)
ax.legend(loc="upper left", frameon=True, fontsize=9,
          facecolor="white", edgecolor="0.7", framealpha=0.9)

fig.savefig("../book/figures/chapter5/backfield_schematic.png", dpi=300, bbox_inches="tight")

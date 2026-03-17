import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import ConnectionPatch

# --- Panel (a): full AF waveform with linear decay envelope ---
n_cycles = 12
t = np.linspace(0, n_cycles * 2 * np.pi, 4000)
H_AF = 1.0  # normalized peak field

# Linear decay envelope
envelope = H_AF * (1 - t / t[-1])
waveform = envelope * np.sin(t)

# --- Panel (b): zoomed waveform with specific mT values ---
peak1 = 20.0    # mT
trough = -19.9  # mT
peak3 = 19.8    # mT

# Build a continuous sinusoid with linearly decaying amplitude.
# The window spans from slightly before peak 1 to slightly after peak 3,
# so the waveform enters and exits the box mid-oscillation.
# Peak 1 at phase pi/2, trough at 3pi/2, peak 3 at 5pi/2.
# We add padding of ~pi/3 on each side so it's clearly mid-wave at the edges.
phase_pad = np.pi / 3
t_detail = np.linspace(-phase_pad, 5 * np.pi / 2 + phase_pad, 800)

# Linear envelope that gives peak1 at pi/2 and peak3 at 5pi/2
# envelope(pi/2) = peak1, envelope(5pi/2) = peak3
# env(t) = a + b*t  =>  a + b*(pi/2) = peak1,  a + b*(5pi/2) = peak3
b_env = (peak3 - peak1) / (2 * np.pi)
a_env = peak1 - b_env * (np.pi / 2)
detail_env = a_env + b_env * t_detail
detail_wave = detail_env * np.sin(t_detail)

# --- Create figure ---
fig = plt.figure(figsize=(12, 5.5))
gs = fig.add_gridspec(1, 2, width_ratios=[1.3, 1], wspace=0.25)

ax_a = fig.add_subplot(gs[0, 0])
ax_b = fig.add_subplot(gs[0, 1])

# ============================================================
# Panel (a): AF waveform
# ============================================================
ax_a.plot(t, waveform, 'k-', lw=1.8)
ax_a.axhline(0, color='k', lw=0.8)

# Dashed envelope
ax_a.plot(t, envelope, 'k--', lw=0.6, alpha=0.35)
ax_a.plot(t, -envelope, 'k--', lw=0.6, alpha=0.35)

# H_AF tick and label
ax_a.plot([0, 0], [0, H_AF], 'k-', lw=0.8)
ax_a.plot([-1.5, 1.0], [H_AF, H_AF], 'k-', lw=0.8)
ax_a.text(-2.0, H_AF, r'$H_{AF}$', fontsize=14, ha='right', va='center')

# H axis (vertical arrow)
ax_a.annotate('', xy=(0, H_AF + 0.22), xytext=(0, -1.15),
              arrowprops=dict(arrowstyle='->', lw=1.5, color='k'))
ax_a.text(-2.0, H_AF + 0.22, 'H', fontsize=15, ha='right', va='center',
          fontweight='bold')

# Time axis (horizontal arrow)
ax_a.annotate('', xy=(t[-1] + 2, 0), xytext=(-3, 0),
              arrowprops=dict(arrowstyle='->', lw=1.5, color='k'))
ax_a.text(t[-1] + 2.5, 0, 'Time', fontsize=13, ha='left', va='center')

# Shaded zoom region
zoom_t_start = 5.0 * 2 * np.pi
zoom_t_end = 6.5 * 2 * np.pi
rect = plt.Rectangle((zoom_t_start, -0.48), zoom_t_end - zoom_t_start, 0.96,
                      facecolor='#d0d0d0', edgecolor='k', lw=0.8, alpha=0.4,
                      zorder=0)
ax_a.add_patch(rect)

# Panel (a) limits and cleanup
ax_a.set_xlim(-5, t[-1] + 8)
ax_a.set_ylim(-1.35, 1.50)
ax_a.axis('off')

# Panel label
ax_a.text(0.15, 0.93, 'a', transform=ax_a.transAxes,
          fontsize=20, fontweight='bold', va='top')

# ============================================================
# Panel (b): zoomed view
# ============================================================

# Define view bounds — inset from full t_detail so wave is cut mid-oscillation
view_left = -phase_pad * 0.5
view_right = 5 * np.pi / 2 + phase_pad * 0.5

# Plot the continuous sinusoid — it extends beyond the box and gets clipped
ax_b.plot(t_detail, detail_wave, 'k-', lw=2.5, clip_on=True)
ax_b.axhline(0, color='k', lw=0.8)

# Horizontal reference lines spanning the visible box
ax_b.plot([view_left, view_right], [peak1, peak1], 'k-', lw=0.5)
ax_b.plot([view_left, view_right], [peak3, peak3], 'k--', lw=0.5, alpha=0.5)
ax_b.plot([view_left, view_right], [trough, trough], 'k-', lw=0.5)

# Field value labels with tick marks extending outside the box frame
tick_len = 0.15
label_x = view_left - tick_len - 0.05
# 20 label
ax_b.plot([view_left, view_left - tick_len], [peak1, peak1], 'k-', lw=0.7,
          clip_on=False)
ax_b.text(label_x, peak1, f'{peak1:.0f}', fontsize=11,
          ha='right', va='bottom')
# 19.8 label
ax_b.plot([view_left, view_left - tick_len], [peak3, peak3], 'k-', lw=0.7,
          clip_on=False)
ax_b.text(label_x, peak3, f'{peak3:.1f}', fontsize=11,
          ha='right', va='top')
# -19.9 label
ax_b.plot([view_left, view_left - tick_len], [trough, trough], 'k-', lw=0.7,
          clip_on=False)
ax_b.text(label_x, trough, f'{trough:.1f}', fontsize=11,
          ha='right', va='center')

# Numbered point markers and labels
points = [
    (np.pi / 2, peak1, '1', 'bottom'),
    (3 * np.pi / 2, trough, '2', 'top'),
    (5 * np.pi / 2, peak3, '3', 'bottom'),
]
for t_pt, h_pt, label, va_pos in points:
    ax_b.plot(t_pt, h_pt, 'ks', ms=5, zorder=5)
    offset_y = 0.8 if va_pos == 'bottom' else -0.8
    ax_b.text(t_pt + 0.12, h_pt + offset_y, label, fontsize=12,
              fontweight='bold', ha='left', va=va_pos,
              bbox=dict(boxstyle='square,pad=0.12', facecolor='white',
                        edgecolor='k', lw=1.0))

# Y-axis label well above the box
ax_b.text(-0.14, 1.06, 'H (mT)', transform=ax_b.transAxes,
          fontsize=13, ha='center', va='bottom')

# Time label below panel
ax_b.text(0.5, -0.06, 'Time', transform=ax_b.transAxes,
          fontsize=13, ha='center', va='top')

# Time arrow inside box
ax_b.annotate('', xy=(view_right - 0.1, 0),
              xytext=(view_right - 0.7, 0),
              arrowprops=dict(arrowstyle='->', lw=1.5, color='k'))

# Up/Down arrows (right side, outside box frame)
arrow_x = 1.08
ax_b.annotate('', xy=(arrow_x, 0.95), xytext=(arrow_x, 0.72),
              xycoords='axes fraction', textcoords='axes fraction',
              arrowprops=dict(arrowstyle='->', lw=2.5, color='gray',
                              mutation_scale=20))
ax_b.text(arrow_x, 0.97, 'Up', transform=ax_b.transAxes,
          fontsize=13, ha='center', va='bottom', color='k')

ax_b.annotate('', xy=(arrow_x, 0.05), xytext=(arrow_x, 0.28),
              xycoords='axes fraction', textcoords='axes fraction',
              arrowprops=dict(arrowstyle='->', lw=2.5, color='gray',
                              mutation_scale=20))
ax_b.text(arrow_x, 0.03, 'Down', transform=ax_b.transAxes,
          fontsize=13, ha='center', va='top', color='k')

# Panel (b) limits and frame — clip the sinusoid at the box edges
ylim = 24.0
ax_b.set_xlim(view_left, view_right)
ax_b.set_ylim(-ylim, ylim)
for spine in ax_b.spines.values():
    spine.set_linewidth(1.5)
ax_b.set_xticks([])
ax_b.set_yticks([])

# Panel label
ax_b.text(0.6, 0.97, 'b', transform=ax_b.transAxes,
          fontsize=20, fontweight='bold', va='top')

# ============================================================
# Connection lines from shaded box in (a) to panel (b) frame
# ============================================================
con_top = ConnectionPatch(
    xyA=(zoom_t_end, 0.48), coordsA=ax_a.transData,
    xyB=(view_left, ylim), coordsB=ax_b.transData,
    color='k', lw=0.8, ls='-')
fig.add_artist(con_top)

con_bot = ConnectionPatch(
    xyA=(zoom_t_end, -0.48), coordsA=ax_a.transData,
    xyB=(view_left, -ylim), coordsB=ax_b.transData,
    color='k', lw=0.8, ls='-')
fig.add_artist(con_bot)

plt.savefig('../book/figures/chapter9/AF_demag.png', dpi=300, bbox_inches='tight')
plt.show()

"""Shared figure styling for consistent appearance across all visualizations.

This module provides unified font and styling configuration for:
- Matplotlib plots
- Plotly visualizations
- Static figures converted from EPS

Target fonts:
- Source Sans Pro: labels, titles, body text
- Source Code Pro: numeric tick labels, data values, code snippets
"""

# Font families
FONT_FAMILY = "Source Sans Pro"
FONT_FAMILY_MONO = "Source Code Pro"

# Font sizes (in points)
FONT_SIZE_TITLE = 14
FONT_SIZE_LABEL = 12
FONT_SIZE_TICK = 10
FONT_SIZE_ANNOTATION = 10

# Matplotlib rcParams configuration
MPL_STYLE = {
    # Font settings
    'font.family': 'sans-serif',
    'font.sans-serif': [FONT_FAMILY, 'DejaVu Sans', 'Helvetica', 'Arial'],
    'font.monospace': [FONT_FAMILY_MONO, 'DejaVu Sans Mono', 'Courier'],
    'font.size': FONT_SIZE_LABEL,

    # Axes settings
    'axes.titlesize': FONT_SIZE_TITLE,
    'axes.labelsize': FONT_SIZE_LABEL,

    # Tick settings
    'xtick.labelsize': FONT_SIZE_TICK,
    'ytick.labelsize': FONT_SIZE_TICK,

    # Legend settings
    'legend.fontsize': FONT_SIZE_TICK,

    # Figure settings
    'figure.titlesize': FONT_SIZE_TITLE,
}

# Plotly font configuration
PLOTLY_FONT = dict(
    family=FONT_FAMILY,
    size=FONT_SIZE_LABEL,
)

# Plotly layout defaults
PLOTLY_LAYOUT = dict(
    font=PLOTLY_FONT,
    title_font=dict(family=FONT_FAMILY, size=FONT_SIZE_TITLE),
)

# Plotly tick font (for numeric labels - use monospace)
PLOTLY_TICKFONT = dict(
    family=FONT_FAMILY_MONO,
    size=FONT_SIZE_TICK,
)


def apply_mpl_style():
    """Apply the standard style to matplotlib.

    Usage:
        from figure_style import apply_mpl_style
        apply_mpl_style()

        # Then create your figures as usual
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots()
        ...
    """
    import matplotlib.pyplot as plt
    plt.rcParams.update(MPL_STYLE)


def get_plotly_layout(**kwargs):
    """Get Plotly layout dict with standard styling merged with custom options.

    Usage:
        from figure_style import get_plotly_layout

        fig = go.Figure()
        fig.update_layout(**get_plotly_layout(
            title="My Figure",
            xaxis_title="X Axis",
        ))
    """
    layout = PLOTLY_LAYOUT.copy()
    layout.update(kwargs)
    return layout

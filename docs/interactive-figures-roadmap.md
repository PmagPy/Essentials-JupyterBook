# Interactive Figures Roadmap

*Future enhancement ideas for Essentials of Paleomagnetism JupyterBook*

This document captures ideas for converting static figures into interactive visualizations. These enhancements are deferred to a future phase after establishing a solid workflow for static figure conversion and font consistency.

---

## Chapter 4 low-temperature data

Replace:
:::{figure} ../figures/chapter4/verwey.png
:name: fig:verwey
:width: 80%

Magnetization curve for magnetite as a function of temperature. The specimen was placed in a very large field, cooled to near absolute zero, then warmed up. The magnetization was measured as it warmed. When it goes through the Verwey transition (~110 K), a fraction of the magnetization is lost. Data downloaded from "w5000" in the [Rock magnetic Bestiary](http://www.irm.umn.edu/bestiary) collection at the Institute for Rock Magnetism.
:::
with a live pull-in via MagIC


## Priority: Chapter 7 Relaxation Time Curves

These figures would benefit most from interactivity, allowing students to explore parameter space:

| Figure | Current File | Interactive Feature |
|--------|--------------|---------------------|
| Temperature-dependent blocking | `neel-trm.eps` | Sliders for grain size, temperature range; animated blocking/unblocking |
| Time-temperature nomogram | `pullaiah.eps` | Interactive nomogram for burial/uplift scenarios |
| Relaxation time explorer | `tauT.eps` | Grain size and temperature controls, log-scale visualization |

---

## Other Interactive Candidates

### Chapter 4: Magnetic Anisotropy
- `energies.eps` → Slider for grain size/temperature effects on energy barriers
- `tauvd.eps` → Interactive relaxation time vs. volume/temperature

### Chapter 5: Hysteresis
- `sdloops.eps` → Field-dependent energy curve animation
- `mdloop.eps` → Interactive hysteresis loop with domain wall motion visualization

### Chapter 6: Mineralogy
- `tern.eps` → Clickable ternary phase diagram for FeTi oxides

---

## Data-Driven Figure Candidates

Figures that should pull from actual data files for reproducibility:

| Figure | Data Source | Benefits |
|--------|-------------|----------|
| Hysteresis loops | `hysteresis.txt` | Real measurements, student can modify |
| Thermal demag | `demag.dat` | Student can experiment with parameters |
| IRM acquisition | IRM Bestiary | Live data from external source |

---

## Technology Stack

Based on the existing Chapter 4 magnetocrystalline anisotropy visualization:

- **Python + Plotly**: Primary tool for interactive figures
- **Self-contained HTML**: Export with `fig.write_html(include_plotlyjs=True)`
- **MyST code cells**: Use `{code-cell}` with `:tags: [remove-input]` to hide code
- **Font consistency**: Use Source Sans Pro / Source Code Pro (see figure_style.py)

---

## Implementation Pattern

From the existing Chapter 4 example (`scripts/plot_magnetocrystalline_anisotropy.py`):

```python
import plotly.graph_objects as go
import numpy as np

# Generate data
# ...

# Create figure with consistent styling
fig = go.Figure()
fig.update_layout(
    font=dict(family="Source Sans Pro", size=12),
    # ... other layout options
)

# Export as self-contained HTML
fig.write_html("output.html", include_plotlyjs=True)
```

---

## Notes

- The existing Chapter 4 interactive visualization is ~5.4 MB due to embedded Plotly.js
- Consider using CDN-hosted Plotly.js for smaller file sizes in production
- Test across browsers before deployment
- Ensure fallback static images for print/PDF export

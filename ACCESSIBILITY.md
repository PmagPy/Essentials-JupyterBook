# Accessibility Guide

This guide covers accessibility practices for the Essentials of Paleomagnetism JupyterBook. Following these guidelines ensures the book is usable by readers with disabilities, including those using screen readers, those with low vision or color blindness, and those navigating by keyboard.

## Figures

Every `:::{figure}` directive **must** include an `:alt:` tag.

```markdown
:::{figure} ../figures/chapter6/solidsolution.png
:name: fig:solidsolution
:alt: Two phase diagrams plotting temperature versus Ti substitution for titanomagnetite and titanohematite series
:width: 100%

Caption text goes here.
:::
```

### Writing good alt text

- **Describe what the figure shows**, not what it is. Write "Two phase diagrams plotting..." not "Figure showing two phase diagrams."
- **Complement the caption.** The caption is already visible to screen readers, so don't repeat it verbatim. Instead, describe the visual content the caption doesn't convey (axes, trends, layout, colors).
- **Keep it concise.** Aim for 1-2 sentences. For simple images, under 150 characters is ideal.
- **Be specific for data figures.** Mention axes, key trends, and notable values: "Plot of Curie temperature decreasing linearly from 580C at x=0 to -150C at x=1."
- **For photographs**, describe the subject and key visual features.
- **For multi-panel figures**, briefly describe each panel: "Three panels: (a) photo of outcrop, (b) equal area stereonet of directions, (c) intensity decay curve."

### Placement

The `:alt:` line goes immediately after `:name:`:

```markdown
:name: fig:label
:alt: Description here
:width: 100%
```

## Tables

### Pipe tables

Pipe tables automatically use the first row as semantic headers (`<th>`). No extra work needed:

```markdown
| Parameter | Value | Units |
|-----------|-------|-------|
| Density   | 5197  | kg/m3 |
```

### List tables

Always include `:header-rows: 1`:

```markdown
:::{list-table} Table caption
:header-rows: 1
:name: tab:label

* - Column A
  - Column B
* - data
  - data
:::
```

## Headings

- Never skip heading levels. Use `##` after `#`, `###` after `##`, etc.
- Each page should have exactly one `#` heading (set by the `title:` frontmatter field).
- Headings create the navigation structure for screen reader users, who often jump between headings to scan content.

## Math

MathJax (used by MyST) renders LaTeX accessibly. No special action is needed for inline (`$...$`) or display (`$$...$$`) math. The math macros defined in `myst.yml` work transparently.

## Links and Cross-references

- Use descriptive link text. Prefer `[Chapter 3](#chap:inducedremanent)` over `[click here](#chap:inducedremanent)`.
- MyST cross-references like `[](#fig:solidsolution)` automatically generate descriptive text from the target, which is accessible.
- Avoid bare URLs in body text.

## Color

- Do not use color as the **only** way to convey information in figures. Add labels, patterns, line styles, or markers alongside color.
- When generating Plotly or matplotlib figures, consider using colorblind-friendly palettes (e.g., `viridis`, `cividis`).

## Abbreviations

Common abbreviations (SD, MD, TRM, NRM, etc.) are defined in `myst.yml` under `project.abbreviations`. These automatically expand on hover in the rendered book. When adding a new abbreviation that appears frequently, add it there:

```yaml
abbreviations:
  NEW: New Abbreviation Definition
```

For abbreviations used only once or twice, spell them out on first use in the chapter text.

## Language

The site language is set to English (`lang: en`) in `myst.yml`. This tells screen readers how to pronounce the text. If content in another language is added, use an HTML `<span lang="fr">` wrapper.

## Checklist for new content

Before merging new content, verify:

- [ ] Every `:::{figure}` has an `:alt:` tag
- [ ] Every `:::{list-table}` has `:header-rows: 1`
- [ ] Heading levels are not skipped
- [ ] Figures don't rely on color alone to convey meaning
- [ ] New abbreviations are either defined in `myst.yml` or spelled out on first use
- [ ] Links use descriptive text

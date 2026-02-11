# LaTeX to MyST Markdown Conversion Strategy

## Overview

This document outlines the strategy for converting chapters from the original LaTeX textbook to MyST Markdown for JupyterBook v2.

## LaTeX to MyST Mapping

| LaTeX | MyST Markdown |
|-------|--------------|
| `\chapter{Title}` | `# Title` (with `title:` in frontmatter) |
| `\section{Title}` | `## Title` |
| `\subsection{Title}` | `### Title` |
| `\label{sect:name}` | `(sect:name)=` **BEFORE** heading (not after!) |
| `\ref{fig:name}` | `[](#fig:name)` |
| `Equation~\ref{eq:name}` | `[Equation %s](#eq:name)` |
| `$$..$$` display math | `$$...$$` (with optional `(label)` after) |
| `$...$` inline math | `$...$` |
| `\beq...\eeq` | `$$...$$` |
| `{\it text}` | `*text*` |
| `{\bf text}` | `**text**` |
| `\begin{figure}...\end{figure}` | `:::{figure}` directive |
| `\includegraphics{file.eps}` | Figure path to converted PNG |
| `\caption{...}` | Content after figure directive options |
| `\nocite{key}` | `{cite}` role or bibliography entry |
| `\cite{key}` | See "Citations" section below |
| `\url{...}` | `<url>` or `[text](url)` |
| `\index{term}` | Omitted (or use glossary) |
| Custom macros (`\M`, `\B`, etc.) | `\mathbf{M}`, `\mathbf{B}`, etc. (defined in myst.yml math macros) |

## Figures

### Font Conversion Pipeline

The original EPS figures use Comic Sans MS which is replaced with Source Sans Pro for professional typography.

**Pipeline**: EPS → PDF (Ghostscript) → SVG (Inkscape) → font replacement → PNG (Inkscape)

**Tool**: `scripts/convert_figures_inkscape.py`

**Workflow**:

1. **Convert new chapter figures**:

   ```bash
   python scripts/convert_figures_inkscape.py --chapter 8
   ```

   This generates:
   - SVGs saved to `Essentials-of-Paleomagnetism/SVGFiles/chapter8/` (for manual editing)
   - PNGs saved to `book/figures/chapter8/`

2. **Review and edit SVGs** in Inkscape to fix layout issues from font changes

3. **Regenerate PNGs** after SVG edits:

   ```bash
   python scripts/convert_figures_inkscape.py --svg-to-png --chapter 8
   ```

4. **Resize large images** (> 1.5 MB) to avoid build warnings:

   ```bash
   convert book/figures/chapter8/largefile.png -resize 50% book/figures/chapter8/largefile.png
   ```

5. **Add white backgrounds** to all PNGs (required for dark mode compatibility):

   The converted PNGs have transparent backgrounds which render poorly in dark mode. Fix with:

   ```bash
   # Single file
   convert image.png -background white -alpha remove -alpha off image.png

   # All PNGs in a chapter
   for png in book/figures/chapter8/*.png; do
     convert "$png" -background white -alpha remove -alpha off "$png"
   done

   # All PNGs in all chapters
   for png in book/figures/**/*.png; do
     convert "$png" -background white -alpha remove -alpha off "$png"
   done
   ```

### File Locations

- **Source**: `../Essentials-of-Paleomagnetism/EPSFiles/`
- **Editable SVGs**: `../Essentials-of-Paleomagnetism/SVGFiles/chapter<N>/`
- **Final PNGs**: `book/figures/chapter<N>/`
- **Reference in MyST**: `:::{figure} ../figures/chapter<N>/filename.png`

### Chapter 4 Figures (11 total)

| LaTeX Reference | EPS File | Description |
|----------------|----------|-------------|
| `fig:magnetite` | `magnetite.eps` | Magnetite crystal structure and anisotropy |
| `fig:K-T` | `K-T.eps` | K1, K2 vs temperature |
| `fig:verwey` | `verwey.eps` | Verwey transition magnetization |
| `fig:demagfield` | `demagfield.eps` | Demagnetizing field diagrams |
| `fig:nonuniform` | `micromag.eps` | Micromagnetic spin configurations |
| `fig:energies` | `energies.eps` | Self energy vs wall energy |
| `fig:tauvd` | `tauvd.eps` | Relaxation time vs grain size |
| `fig:butban` | `butban.eps` | Evans/Butler-Banerjee diagram |
| `fig:domains` | `domains.eps` | Domain structure types |
| `fig:wall` | `wall.eps` | Domain wall structure |
| `fig:domain-images` | `domain-images.eps` | Domain imaging techniques |

## Citations

MyST Markdown provides three citation roles for different formatting needs:

### Citation Role Syntax

**Narrative citations** - Use `{cite}` for in-text citations:
```markdown
{cite}`cockett2015`
```
Renders as: Cockett et al., 2015

**Parenthetical citations** - Use `{cite:p}` for citations in parentheses:
```markdown
{cite:p}`cockett2015`
```
Renders as: (Cockett et al., 2015)

**Textual citations** - Use `{cite:t}` for author names only:
```markdown
{cite:t}`cockett2015`
```
Renders as: Cockett et al. (2015)

### Multiple Citations

Separate multiple citation keys with semicolons:
```markdown
{cite:p}`cockett2015; heagy2017`
```
Renders as: (Cockett et al., 2015; Heagy et al., 2017)

### Prefix and Suffix

**Note:** The curly-brace prefix/suffix syntax documented in MyST may not work in all versions. Use the manual prefix approach instead:

```markdown
# DOES NOT WORK (prefix syntax broken):
{cite:p}`{e.g., }johnson1948`

# USE THIS INSTEAD (manual prefix with {cite:t}):
(e.g., {cite:t}`johnson1948`)
```

Working examples with manual prefixes:

```markdown
(see {cite:t}`dunlop1997`)              → (see Dunlop and Özdemir, 1997)
(see also {cite:t}`tauxe2006`)          → (see also Tauxe et al., 2006)
(e.g., {cite:t}`nagy2017`)              → (e.g., Nagy et al., 2017)
(e.g., {cite:t}`ref1`; {cite:t}`ref2`)  → (e.g., Author1, Year; Author2, Year)
```

### Common Conversion Patterns

When converting from LaTeX or fixing existing MyST:

| Pattern | Convert to | Result |
|---------|-----------|--------|
| `({cite}\`ref\`)` | `{cite:p}\`ref\`` | (Author, Year) |
| `(see {cite}\`ref\`)` | `(see {cite:t}\`ref\`)` | (see Author, Year) |
| `(e.g., {cite}\`ref\`)` | `(e.g., {cite:t}\`ref\`)` | (e.g., Author, Year) |
| `({cite}\`ref1\`; {cite}\`ref2\`)` | `{cite:p}\`ref1; ref2\`` | (Author1, Year; Author2, Year) |

### Configuration

The `numbered_references` setting in `myst.yml` controls citation style:
- `numbered_references: false` → Author-year citations (Cockett et al., 2015)
- `numbered_references: true` → Numeric citations [1]

**Current setting**: `numbered_references: false` (author-year style)

## Chapter and Section Numbering

Enable automatic numbering of chapters and sections in `myst.yml`:

```yaml
toc:
  - file: index.md
  - title: Chapters
    numbered: true  # Enables chapter and section numbering
    children:
      - file: chapters/chapter4.md
      - file: chapters/chapter5.md
```

Then add the complete frontmatter to each chapter file:

```yaml
---
title: "Chapter 5: Magnetic Hysteresis"  # Format: "Chapter N: Title"
label: chap:hysteresis                    # Unique label for cross-references
numbering:
  enumerator: 5.%s                        # Chapter number prefix for sections
kernelspec:                               # Required for executable code cells
  name: python3
  display_name: Python 3
---
```

**Frontmatter fields:**

- `title`: Use format `"Chapter N: Chapter Title"` for consistent display
- `label`: Unique identifier like `chap:hysteresis` for cross-referencing
- `numbering.enumerator`: Set to `N.%s` where N is the chapter number
- `kernelspec`: Required if the chapter contains `{code-cell}` directives

This will number sections as:
- Level 2 headings (`##`): 4.1, 4.2, 4.3...
- Level 3 headings (`###`): 4.1.1, 4.1.2, 4.2.1...
- Level 4 headings (`####`): 4.1.1.1, 4.1.1.2...

## Cross-References and Targets

### Target Placement (IMPORTANT!)

**Target labels MUST come BEFORE the element they label, not after!**

Correct syntax:
```markdown
(my-label)=
### Section Title
```

Incorrect syntax (DO NOT USE):
```markdown
### Section Title
(my-label)=
```

### Common Target Types

- Section labels: `(sect:name)=` before heading
- Figure labels: `:name: fig:name` in figure directive options
- Equation labels: `(eq:name)` after closing `$$`
- Table labels: `(tab:name)=` before table

### Referencing Targets

- Generic reference: `[](#label)` - shows element name (e.g., "Section Title")
- Figure/equation reference: `[](#fig:name)` or `[Equation %s](#eq:name)`
- The `%s` in equation references gets replaced with the equation number

## Custom LaTeX Macros

The original textbook uses custom macros defined in `mydefs.tex`. These are handled via `math` macros in `myst.yml`:

- `\M` → `\mathbf{M}` (magnetization vector)
- `\B` → `\mathbf{B}` (magnetic field)
- `\H` → `\mathbf{H}` (auxiliary field)
- `\S` → `\mathbf{S}` (spin vector)
- `\beq`/`\eeq` → `$$...$$` (equation environment)

## Per-Chapter Checklist

For each chapter conversion:

- [ ] Read LaTeX source and identify structure
- [ ] Identify all referenced figures
- [ ] Convert EPS figures to PNG
- [ ] Create MyST Markdown file
- [ ] Convert all equations (verify rendering)
- [ ] Convert all figures with captions
- [ ] Add cross-references and labels
- [ ] Add bibliography entries to `references.bib`
- [ ] Update TOC in `myst.yml`
- [ ] Build and verify rendering
- [ ] Check all figure references resolve
- [ ] Check all equation references resolve
- [ ] Check all citations resolve

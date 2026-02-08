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

### Conversion Pipeline

1. **Source**: EPS files in `../Essentials-of-Paleomagnetism/EPSFiles/`
2. **Tool**: `scripts/convert_figures.py` using ghostscript
3. **Output**: PNG at 300 DPI in `book/figures/`
4. **Reference**: `:::{figure} ../figures/filename.png` in MyST

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

Add contextual text before or after citations using curly braces:
```markdown
{cite:p}`{see}cockett2015{fig 1}`
```
Renders as: (see Cockett et al., 2015, fig 1)

Additional examples:
```markdown
{cite:p}`{e.g., }johnson1948`           → (e.g., Johnson et al., 1948)
{cite:p}`{see }dunlop1997`              → (see Dunlop and Özdemir, 1997)
{cite:p}`{see also }tauxe2006`          → (see also Tauxe et al., 2006)
{cite:p}`{cf. }nagy2017`                → (cf. Nagy et al., 2017)
{cite:p}`{see }dunlop1997{ for details}`→ (see Dunlop and Özdemir, 1997 for details)
```

### Common Conversion Patterns

When converting from LaTeX or fixing existing MyST:

| Pattern | Convert to | Result |
|---------|-----------|--------|
| `({cite}\`ref\`)` | `{cite:p}\`ref\`` | (Author, Year) |
| `(see {cite}\`ref\`)` | `{cite:p}\`{see }ref\`` | (see Author, Year) |
| `(e.g., {cite}\`ref\`)` | `{cite:p}\`{e.g., }ref\`` | (e.g., Author, Year) |
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

Then add explicit chapter numbers to each chapter's frontmatter:

```yaml
---
title: Chapter Title
label: chap:label
numbering:
  enumerator: 4.%s  # For Chapter 4 (use 5.%s for Chapter 5, etc.)
---
```

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

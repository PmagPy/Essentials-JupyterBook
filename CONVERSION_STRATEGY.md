# LaTeX to MyST Markdown Conversion Strategy

## Overview

This document outlines the strategy for converting chapters from the original LaTeX textbook to MyST Markdown for JupyterBook v2.

## LaTeX to MyST Mapping

| LaTeX | MyST Markdown |
|-------|--------------|
| `\chapter{Title}` | `# Title` (with `title:` in frontmatter) |
| `\section{Title}` | `## Title` |
| `\subsection{Title}` | `### Title` |
| `\label{sect:name}` | `(sect:name)=` target above heading |
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
| `\cite{key}` | `{cite}\`key\`` |
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

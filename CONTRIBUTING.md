# Contributing

Contributions to this JupyterBook edition of Essentials of Paleomagnetism are welcome.

## Getting Started

1. Fork and clone the repository
2. Set up the environment: `mamba env create -f environment.yml && mamba activate ess-jbook`
3. Start the dev server: `cd book && jupyter book start`
4. Make your changes and verify they render correctly

## Chapter Conversion

When converting chapters from the original LaTeX source:

1. Read the LaTeX source from `../Essentials-of-Paleomagnetism/Chapters/`
2. Convert to MyST Markdown in `book/chapters/`
3. Convert referenced EPS figures using `scripts/convert_figures.py`
4. Add bibliography entries to `book/references.bib`
5. Update `book/myst.yml` to include the new chapter in the TOC

## Style Guide

- Use MyST Markdown syntax for all content
- Equations use standard LaTeX math (`$$...$$` for display, `$...$` for inline)
- Figures use the `:::{figure}` directive
- Citations use `{cite}` roles with BibTeX keys from `references.bib`
- Cross-references use `[](#label)` syntax

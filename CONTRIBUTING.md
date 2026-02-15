# Contributing

Contributions to this JupyterBook edition of Essentials of Paleomagnetism are welcome.

## Getting Started

### Prerequisites

- [Mamba](https://mamba.readthedocs.io/) (via Miniforge or Mambaforge)
- The original LaTeX source repo at `../Essentials-of-Paleomagnetism/` (for figure conversion)

### Create the environment

```bash
mamba env create -f environment.yml
mamba activate ess-jbook
```

Or use the Makefile:

```bash
make install
mamba activate ess-jbook
```

## Building the Book

### Local development server (recommended)

```bash
mamba activate ess-jbook && cd book && jupyter book start --execute
```

This launches a live-reloading dev server with notebook execution — edits to `.md` and `.ipynb` files are reflected immediately. The server URL will be displayed in the terminal output (typically `http://localhost:3000` or another available port).

### Static build

```bash
make build
```

The built site is in `book/_build/site/`. Serve it with:

```bash
make serve
```

Then visit <http://localhost:8000> (the `make serve` target uses a fixed port).

### Clean build artifacts

```bash
make clean
```

## Converting Figures

Chapter figures are converted from EPS (original LaTeX source) to PNG:

```bash
# Convert a specific chapter's figures
python scripts/convert_figures.py --chapter 4
python scripts/convert_figures.py --chapter 5

# Convert all EPS files
python scripts/convert_figures.py --all

# Convert specific files
python scripts/convert_figures.py --files fig1.eps fig2.eps
```

Requires ghostscript (`mamba install ghostscript` or `brew install ghostscript`).

## Chapter Conversion

When converting chapters from the original LaTeX source:

1. Read the LaTeX source from `../Essentials-of-Paleomagnetism/Chapters/`
2. Convert to MyST Markdown in `book/chapters/`
3. Convert referenced EPS figures using `scripts/convert_figures.py`
4. Add bibliography entries to `book/references.bib`
5. Update `book/myst.yml` to include the new chapter in the TOC

## Project Structure

```
Essentials-JupyterBook/
├── book/                    # Main book content
│   ├── myst.yml             # JupyterBook v2 configuration & TOC
│   ├── index.md             # Landing page
│   ├── references.bib       # Bibliography
│   ├── chapters/            # Chapter content (MyST Markdown / notebooks)
│   ├── figures/             # Converted figures (PNG)
│   └── _static/             # Custom CSS, logos
├── scripts/                 # Utility scripts
│   └── convert_figures.py   # EPS to PNG converter
├── environment.yml          # Mamba environment specification
├── Makefile                 # Build commands
└── .github/workflows/       # CI/CD (GitHub Pages deployment)
```

## Accessibility

All contributions must follow the project's [Accessibility Guide](ACCESSIBILITY.md). In particular:

- Every `:::{figure}` directive must include an `:alt:` tag with descriptive alt text
- Every `:::{list-table}` must include `:header-rows: 1`
- Heading levels must not be skipped
- Figures should not rely on color alone to convey meaning

See [ACCESSIBILITY.md](ACCESSIBILITY.md) for full details and a pre-merge checklist.

## Style Guide

- Use MyST Markdown syntax for all content
- Equations use standard LaTeX math (`$$...$$` for display, `$...$` for inline)
- Figures use the `:::{figure}` directive with an `:alt:` tag (see [Accessibility Guide](ACCESSIBILITY.md))
- Citations use `{cite}` roles with BibTeX keys from `references.bib`
- Cross-references use `[](#label)` syntax

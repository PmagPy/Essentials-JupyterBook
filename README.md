# Essentials of Paleomagnetism — JupyterBook Edition

A modern, interactive web version of **Essentials of Paleomagnetism**, built with [Jupyter Book v2](https://jupyterbook.org/).

## Attribution

This work is being adapted, revised, and updated from:

> Tauxe, L. *Essentials of Paleomagnetism*, 5th web edition.
> with contributions from: Subir K. Banerjee, Robert F. Butler and Rob van der Voo

That version is available online at [EarthRef.org](https://earthref.org/MagIC/books/Tauxe/Essentials/) with the source files to be found here: https://github.com/ltauxe/Essentials-of-Paleomagnetism

## Setup

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
cd book
jupyter book start --execute
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

## Project Structure

```
Essentials-JupyterBook/
├── book/                    # Main book content
│   ├── myst.yml             # JupyterBook v2 configuration & TOC
│   ├── index.md             # Landing page
│   ├── references.bib       # Bibliography
│   ├── chapters/            # Chapter content (MyST Markdown / notebooks)
│   │   └── chapter4.md
│   ├── figures/             # Converted figures (PNG)
│   └── _static/             # Custom CSS, logos
├── scripts/                 # Utility scripts
│   └── convert_figures.py   # EPS to PNG converter
├── environment.yml          # Mamba environment specification
├── Makefile                 # Build commands
└── .github/workflows/       # CI/CD (GitHub Pages deployment)
```

## License

Content: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)

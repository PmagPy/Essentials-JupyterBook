#!/usr/bin/env python
"""
Convert EPS figures from the original LaTeX textbook to web-friendly formats.

Usage:
    python scripts/convert_figures.py --chapter 4      # Convert Chapter 4 figures
    python scripts/convert_figures.py --chapter 5      # Convert Chapter 5 figures
    python scripts/convert_figures.py --all            # Convert all EPS files
    python scripts/convert_figures.py --files fig1.eps fig2.eps  # Convert specific files

Requires ghostscript: install via `mamba install ghostscript` or `brew install ghostscript`
"""

import argparse
import subprocess
import sys
from pathlib import Path

# Paths
PROJECT_ROOT = Path(__file__).parent.parent
EPS_DIR = PROJECT_ROOT.parent / "Essentials-of-Paleomagnetism" / "EPSFiles"
FIGURES_DIR = PROJECT_ROOT / "book" / "figures"
FONTMAP_PATH = PROJECT_ROOT / "scripts" / "fontmap" / "Fontmap.custom"

# Chapter figure lists (extracted from LaTeX source files)
CHAPTER_FIGURES = {
    4: [
        "magnetite.eps",
        "K-T.eps",
        "verwey.eps",
        "demagfield.eps",
        "micromag.eps",
        "energies.eps",
        "tauvd.eps",
        "butban.eps",
        "domains.eps",
        "wall.eps",
        "domain-images.eps",
    ],
    5: [
        "mB.eps",
        "flip.eps",
        "bf.eps",
        "outerloop.eps",
        "sdloops.eps",
        "Bcr.eps",
        "cubicloops.eps",
        "loops.eps",
        "mdloop.eps",
        "void.eps",
        "wallenergy.eps",
        "forcprinc.eps",
        "m428.eps",
        "ZFORC.eps",
    ],
    6: [
        "solidsolution.eps",
        "exsolution.eps",
        "tern.eps",
        "X.eps",
        "hematite.eps",
        "hemY.eps",
        "Z.eps",
        "suppress.eps",
        "minerals.eps",
        "pyrrhotiteT.eps",
        "igneous.eps",
        "bacteria.eps",
        "problem1.eps",
        "microprobe.eps",
    ],
    7: [
        "equilibrium.eps",
        "neel.eps",
        "neel-vrm.eps",
        "neel-trm.eps",
        "tauT.eps",
        "vrm1.eps",
        "lava.eps",
        "trm.eps",
        "pTRM.eps",
        "TRM-d.eps",
        "neel-crm.eps",
        "chinji.eps",
        "lit-redep.eps",
        "drmprocesses.eps",
        "brownian.eps",
        "flocs.eps",
        "drm-exp.eps",
        "incerror.eps",
        "lightning.eps",
        "irm.eps",
        "pullaiah.eps",
        "ARM.eps",
    ],
    8: [
        "images.eps",
        "curiebalance.eps",
        "curie1.eps",
        "kappa.eps",
        "chiT.eps",
        "chifd.eps",
        "chimap.eps",
        "crossover.eps",
        "unmixing.eps",
        "3dirm.eps",
        "bblocks.eps",
        "interp.eps",
        "trends.eps",
        "slag.eps",
        "banerjee.eps",
        "rosenbaum-1.eps",
        "rosenbaum-2.eps",
        "yamazaki.eps",
        "jackson-1.eps",
        "jackson-2.eps",
        "moskowitz08-1.eps",
        "moskowitz08-2.eps",
    ],
    9: [
        "drill.eps",
        "hand.eps",
        "core.eps",
        "orientation.eps",
        "suncomp.eps",
        "backbite.eps",
        "gps.eps",
        "samples.eps",
        "comps.eps",
        "zijd.eps",
        "digeo.eps",
        "foldtesta.eps",
        "foldtestb.eps",
        "congloma.eps",
        "conglomb.eps",
        "baked.eps",
        "NS034.eps",
    ],
    10: [
        "pintprinc.eps",
        "koenigsberger.eps",
        "TT.eps",
        "dunlop01.eps",
        "method.eps",
        "zigzag.eps",
        "trm-anis.eps",
        "coolingrate.eps",
        "Shaw-DD.eps",
        "drm1.eps",
    ],
}


def check_ghostscript():
    """Check that ghostscript is available."""
    try:
        subprocess.run(["gs", "--version"], capture_output=True, check=True)
        return True
    except FileNotFoundError:
        print("ERROR: ghostscript (gs) not found.")
        print("Install with: mamba install ghostscript  OR  brew install ghostscript")
        return False


def convert_eps_to_png(eps_path: Path, png_path: Path, dpi: int = 300, use_fontmap: bool = True):
    """Convert an EPS file to PNG using ghostscript.

    Args:
        eps_path: Path to the input EPS file
        png_path: Path for the output PNG file
        dpi: Resolution in dots per inch (default: 300)
        use_fontmap: Whether to use custom fontmap for font substitution (default: True)

    Note: Font substitution via fontmap may not work for EPS files with embedded
    font subsets (common in Adobe Illustrator files). In such cases, the embedded
    fonts will be used as-is.
    """
    cmd = [
        "gs",
        "-dBATCH",
        "-dNOPAUSE",
        "-dEPSCrop",
        "-sDEVICE=png16m",
        f"-r{dpi}",
    ]

    # Add fontmap if requested and file exists
    if use_fontmap and FONTMAP_PATH.exists():
        cmd.append(f"-sFONTMAP={FONTMAP_PATH}")

    cmd.extend([
        f"-sOutputFile={png_path}",
        str(eps_path),
    ])

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"  FAILED: {result.stderr.strip()}")
        return False
    return True


def main():
    parser = argparse.ArgumentParser(description="Convert EPS figures to PNG")
    parser.add_argument(
        "--chapter", "-c", type=int, choices=list(CHAPTER_FIGURES.keys()),
        help=f"Chapter number to convert (available: {list(CHAPTER_FIGURES.keys())})"
    )
    parser.add_argument("--all", action="store_true", help="Convert all EPS files")
    parser.add_argument("--files", nargs="+", help="Specific EPS files to convert")
    parser.add_argument(
        "--output-dir", "-o", type=Path,
        help="Output directory (default: book/figures/chapter<N>/ or book/figures/)"
    )
    parser.add_argument("--dpi", type=int, default=300, help="Resolution (default: 300)")
    parser.add_argument(
        "--no-fontmap", action="store_true",
        help="Disable custom fontmap (use original embedded fonts)"
    )
    args = parser.parse_args()

    # Require at least one mode
    if not args.chapter and not args.all and not args.files:
        parser.print_help()
        print("\nERROR: Must specify --chapter <N>, --all, or --files <file1.eps ...>")
        sys.exit(1)

    if not check_ghostscript():
        sys.exit(1)

    if not EPS_DIR.exists():
        print(f"ERROR: EPS directory not found: {EPS_DIR}")
        print("Make sure the original textbook repo is at ../Essentials-of-Paleomagnetism/")
        sys.exit(1)

    # Determine output directory
    if args.output_dir:
        output_dir = args.output_dir
    elif args.chapter:
        output_dir = FIGURES_DIR / f"chapter{args.chapter}"
    else:
        output_dir = FIGURES_DIR

    output_dir.mkdir(parents=True, exist_ok=True)

    # Determine which files to convert
    if args.files:
        eps_files = args.files
    elif args.all:
        eps_files = [f.name for f in EPS_DIR.glob("*.eps")]
    else:
        eps_files = CHAPTER_FIGURES[args.chapter]

    converted = 0
    failed = 0

    for eps_name in eps_files:
        eps_path = EPS_DIR / eps_name
        if not eps_path.exists():
            print(f"  SKIP (not found): {eps_name}")
            failed += 1
            continue

        png_name = eps_path.stem + ".png"
        png_path = output_dir / png_name
        print(f"  Converting: {eps_name} -> {png_name}")

        if convert_eps_to_png(eps_path, png_path, args.dpi, use_fontmap=not args.no_fontmap):
            converted += 1
        else:
            failed += 1

    print(f"\nDone: {converted} converted, {failed} failed")
    print(f"Output directory: {output_dir}")


if __name__ == "__main__":
    main()

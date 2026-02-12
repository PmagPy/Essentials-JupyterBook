#!/usr/bin/env python
"""
Convert EPS figures to PNG with font replacement using Inkscape.

This script converts EPS figures to PNG while replacing Comic Sans MS
with Source Sans Pro for consistent typography.

Workflow:
1. EPS → PDF (Ghostscript, preserves vectors)
2. PDF → SVG (Inkscape)
3. Replace font families in SVG
4. SVG → PNG (Inkscape)

The SVG files are saved to Essentials-of-Paleomagnetism/SVGFiles/ for manual
editing. After making adjustments, use --svg-to-png to regenerate PNGs.

Usage:
    # Full conversion: EPS → SVG (saved) → PNG
    python scripts/convert_figures_inkscape.py --chapter 4

    # Convert specific files
    python scripts/convert_figures_inkscape.py --files magnetite.eps

    # Regenerate PNGs from edited SVGs
    python scripts/convert_figures_inkscape.py --svg-to-png --chapter 4

Requires:
- ghostscript: brew install ghostscript
- inkscape: brew install --cask inkscape
"""

import argparse
import subprocess
import sys
import tempfile
from pathlib import Path

# Paths
PROJECT_ROOT = Path(__file__).parent.parent
ORIGINAL_REPO = PROJECT_ROOT.parent / "Essentials-of-Paleomagnetism"
EPS_DIR = ORIGINAL_REPO / "EPSFiles"
SVG_DIR = ORIGINAL_REPO / "SVGFiles"
FIGURES_DIR = PROJECT_ROOT / "book" / "figures"

# Font replacement mappings
FONT_REPLACEMENTS = {
    "Comic Sans MS": "Source Sans Pro",
    "ComicSansMS": "Source Sans Pro",
    "Arial": "Source Sans Pro",
    "ArialMT": "Source Sans Pro",
}

# Chapter figure lists (same as convert_figures.py)
CHAPTER_FIGURES = {
    4: [
        "magnetite.eps", "K-T.eps", "verwey.eps", "demagfield.eps",
        "micromag.eps", "energies.eps", "tauvd.eps", "butban.eps",
        "domains.eps", "wall.eps", "domain-images.eps",
    ],
    5: [
        "mB.eps", "flip.eps", "bf.eps", "outerloop.eps", "sdloops.eps",
        "Bcr.eps", "cubicloops.eps", "loops.eps", "mdloop.eps", "void.eps",
        "wallenergy.eps", "forcprinc.eps", "m428.eps", "ZFORC.eps",
    ],
    6: [
        "solidsolution.eps", "exsolution.eps", "tern.eps", "X.eps",
        "hematite.eps", "hemY.eps", "Z.eps", "suppress.eps",
        "minerals.eps", "pyrrhotiteT.eps", "igneous.eps",
        "bacteria.eps", "problem1.eps", "microprobe.eps",
    ],
    7: [
        "equilibrium.eps", "neel.eps", "neel-vrm.eps", "neel-trm.eps",
        "tauT.eps", "vrm1.eps", "lava.eps", "trm.eps", "pTRM.eps",
        "TRM-d.eps", "neel-crm.eps", "chinji.eps", "lit-redep.eps",
        "drmprocesses.eps", "brownian.eps", "flocs.eps", "drm-exp.eps",
        "incerror.eps", "lightning.eps", "irm.eps", "pullaiah.eps", "ARM.eps",
    ],
    8: [
        "images.eps", "curiebalance.eps", "curie1.eps", "kappa.eps",
        "chiT.eps", "chifd.eps", "chimap.eps", "crossover.eps",
        "unmixing.eps", "3dirm.eps", "bblocks.eps", "interp.eps",
        "trends.eps", "slag.eps", "banerjee.eps", "rosenbaum-1.eps",
        "rosenbaum-2.eps", "yamazaki.eps", "jackson-1.eps", "jackson-2.eps",
        "moskowitz08-1.eps", "moskowitz08-2.eps",
    ],
    9: [
        "drill.eps", "hand.eps", "core.eps", "orientation.eps",
        "orient.eps", "suncomp.eps", "backbite.eps", "gps.eps", "samples.eps",
        "comps.eps", "zijd.eps", "digeo.eps", "foldtesta.eps",
        "foldtestb.eps", "congloma.eps", "conglomb.eps", "baked.eps",
        "NS034.eps",
    ],
    10: [
        "pintprinc.eps", "koenigsberger.eps", "TT.eps", "dunlop01.eps",
        "method.eps", "zigzag.eps", "trm-anis.eps", "coolingrate.eps",
        "Shaw-DD.eps", "drm1.eps",
    ],
    11: [
        "gauss.eps", "fisher.eps", "P.eps", "vecsum.eps", "a95-csd.eps",
        "twosets.eps", "lnp.eps", "incfish.eps", "fishrot.eps",
        "unexp.eps", "fishqq.eps",
    ],
    12: [
        "vgp-di.eps", "confidence.eps", "love.eps", "hypeq.eps",
        "twofiles.eps", "cdf.eps", "revtest.eps", "unfolding.eps",
    ],
    13: [
        "measAMS.eps", "magnitude.eps", "eij.eps", "evec.eps",
        "kmin.eps", "dikeams.eps", "sedams.eps", "shape.eps",
        "diags.eps", "ternaryams.eps",
    ],
    14: [
        "c14.eps", "chinesecompass.eps", "halley.eps", "gufm1.eps",
        "psvmod.eps", "wilsoncreek.eps", "sint800.eps", "sedpint.eps",
        "919.eps", "reversals.eps", "vgpspint.eps", "gpts.eps",
        "hk02.eps", "tangent.eps", "sbg-lava.eps", "psvrl.eps",
        "bell.eps", "tk03.eps",
    ],
}


def check_dependencies():
    """Check that required tools are available."""
    missing = []

    try:
        subprocess.run(["gs", "--version"], capture_output=True, check=True)
    except FileNotFoundError:
        missing.append("ghostscript (gs)")

    try:
        subprocess.run(["inkscape", "--version"], capture_output=True, check=True)
    except FileNotFoundError:
        missing.append("inkscape")

    if missing:
        print(f"ERROR: Missing dependencies: {', '.join(missing)}")
        print("Install with:")
        print("  brew install ghostscript")
        print("  brew install --cask inkscape")
        return False
    return True


def eps_to_pdf(eps_path: Path, pdf_path: Path) -> bool:
    """Convert EPS to PDF using Ghostscript."""
    cmd = [
        "gs", "-dBATCH", "-dNOPAUSE", "-dEPSCrop",
        "-sDEVICE=pdfwrite",
        f"-sOutputFile={pdf_path}",
        str(eps_path),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode == 0


def pdf_to_svg(pdf_path: Path, svg_path: Path) -> bool:
    """Convert PDF to SVG using Inkscape."""
    cmd = [
        "inkscape", str(pdf_path),
        f"--export-filename={svg_path}",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode == 0


def replace_fonts_in_svg(svg_path: Path) -> bool:
    """Replace font families in SVG file.

    Uses simple string replacement for each font mapping.
    This handles the common SVG font-family formats.
    """
    try:
        with open(svg_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Simple string replacement for each font
        for old_font, new_font in FONT_REPLACEMENTS.items():
            content = content.replace(old_font, new_font)

        with open(svg_path, 'w', encoding='utf-8') as f:
            f.write(content)

        return True
    except Exception as e:
        print(f"  Font replacement error: {e}")
        return False


def svg_to_png(svg_path: Path, png_path: Path, dpi: int = 300) -> bool:
    """Convert SVG to PNG using Inkscape."""
    cmd = [
        "inkscape", str(svg_path),
        f"--export-filename={png_path}",
        f"--export-dpi={dpi}",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode == 0


def convert_eps_to_svg(eps_path: Path, svg_path: Path) -> bool:
    """Convert EPS to SVG with font replacement.

    Pipeline: EPS -> PDF (temp) -> SVG (saved)
    SVG is saved for manual editing if needed.
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        pdf_path = Path(tmpdir) / "temp.pdf"

        # Step 1: EPS to PDF
        if not eps_to_pdf(eps_path, pdf_path):
            print("  FAILED: EPS to PDF conversion")
            return False

        # Step 2: PDF to SVG
        if not pdf_to_svg(pdf_path, svg_path):
            print("  FAILED: PDF to SVG conversion")
            return False

        # Step 3: Replace fonts in SVG
        if not replace_fonts_in_svg(svg_path):
            print("  FAILED: Font replacement")
            return False

        return True


def convert_eps_to_png(eps_path: Path, svg_path: Path, png_path: Path, dpi: int = 300) -> bool:
    """Convert EPS to PNG with font replacement, saving SVG intermediate.

    Pipeline: EPS -> PDF (temp) -> SVG (saved) -> PNG
    """
    # First create the SVG (or use existing if already converted)
    if not svg_path.exists():
        if not convert_eps_to_svg(eps_path, svg_path):
            return False

    # Convert SVG to PNG
    if not svg_to_png(svg_path, png_path, dpi):
        print("  FAILED: SVG to PNG conversion")
        return False

    return True


def main():
    """Main entry point for figure conversion."""
    parser = argparse.ArgumentParser(
        description="Convert EPS figures to PNG with font replacement"
    )
    parser.add_argument(
        "--chapter", "-c", type=int, choices=list(CHAPTER_FIGURES.keys()),
        help="Chapter number to convert"
    )
    parser.add_argument("--all", action="store_true", help="Convert all EPS files")
    parser.add_argument("--files", nargs="+", help="Specific EPS files to convert")
    parser.add_argument(
        "--output-dir", "-o", type=Path,
        help="PNG output directory (default: book/figures/chapter<N>/)"
    )
    parser.add_argument("--dpi", type=int, default=300, help="Resolution (default: 300)")
    parser.add_argument(
        "--svg-only", action="store_true",
        help="Only generate SVG files (skip PNG conversion)"
    )
    parser.add_argument(
        "--svg-to-png", action="store_true",
        help="Convert existing SVGs to PNG (use after manual SVG edits)"
    )
    args = parser.parse_args()

    if not args.chapter and not args.all and not args.files:
        parser.print_help()
        print("\nERROR: Must specify --chapter <N>, --all, or --files <file1.eps ...>")
        sys.exit(1)

    if not check_dependencies():
        sys.exit(1)

    if not EPS_DIR.exists():
        print(f"ERROR: EPS directory not found: {EPS_DIR}")
        sys.exit(1)

    # Determine PNG output directory
    if args.output_dir:
        png_output_dir = args.output_dir
    elif args.chapter:
        png_output_dir = FIGURES_DIR / f"chapter{args.chapter}"
    else:
        png_output_dir = FIGURES_DIR

    # Determine SVG output directory (in original repo)
    if args.chapter:
        svg_output_dir = SVG_DIR / f"chapter{args.chapter}"
    else:
        svg_output_dir = SVG_DIR

    png_output_dir.mkdir(parents=True, exist_ok=True)
    svg_output_dir.mkdir(parents=True, exist_ok=True)

    # Determine files to convert
    if args.files:
        file_stems = [Path(f).stem for f in args.files]
    elif args.all:
        file_stems = [f.stem for f in EPS_DIR.glob("*.eps")]
    else:
        file_stems = [Path(f).stem for f in CHAPTER_FIGURES[args.chapter]]

    converted = 0
    failed = 0

    for stem in file_stems:
        eps_path = EPS_DIR / f"{stem}.eps"
        svg_path = svg_output_dir / f"{stem}.svg"
        png_path = png_output_dir / f"{stem}.png"

        if args.svg_to_png:
            # Convert existing SVG to PNG
            if not svg_path.exists():
                print(f"  SKIP (SVG not found): {stem}.svg")
                failed += 1
                continue
            print(f"  Converting: {stem}.svg -> {stem}.png")
            if svg_to_png(svg_path, png_path, args.dpi):
                converted += 1
            else:
                failed += 1
        elif args.svg_only:
            # Only generate SVG
            if not eps_path.exists():
                print(f"  SKIP (EPS not found): {stem}.eps")
                failed += 1
                continue
            print(f"  Converting: {stem}.eps -> {stem}.svg")
            if convert_eps_to_svg(eps_path, svg_path):
                converted += 1
            else:
                failed += 1
        else:
            # Full pipeline: EPS -> SVG -> PNG
            if not eps_path.exists():
                print(f"  SKIP (EPS not found): {stem}.eps")
                failed += 1
                continue
            print(f"  Converting: {stem}.eps -> {stem}.svg -> {stem}.png")
            if convert_eps_to_png(eps_path, svg_path, png_path, args.dpi):
                converted += 1
            else:
                failed += 1

    print(f"\nDone: {converted} converted, {failed} failed")
    if not args.svg_to_png:
        print(f"SVG directory: {svg_output_dir}")
    if not args.svg_only:
        print(f"PNG directory: {png_output_dir}")


if __name__ == "__main__":
    main()

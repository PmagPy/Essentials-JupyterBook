# Future Action Items

This document tracks action items identified during the LaTeX to MyST Markdown conversion that require future work once additional chapters or components are converted.

## Appendix Cross-References

### Issue Description

During the conversion of Chapter 9, two equation cross-references to appendix content were removed because the appendices have not yet been converted:

1. **Rotation Matrix Equation (eq:aij)**
   - **Location**: Chapter 9, section on "Changing Coordinate Systems"
   - **Original LaTeX**: `Equation~\ref{eq:aij}`
   - **Current text**: "the rotation matrix equation" (generic reference)
   - **Context**: The text discusses substituting azimuth and plunge values into a rotation matrix equation to convert specimen coordinates to geographic coordinates.

2. **Center of Mass Equation (eq:cm)**
   - **Location**: Chapter 9, section on "Best-fit Lines and Planes"
   - **Original LaTeX**: `Equation~\ref{eq:cm}`
   - **Current text**: Reference was removed entirely
   - **Context**: The Deviation ANGle (DANG) is defined as the angle between the best-fitting line and the origin, where the line to the origin is computed using the center of mass equation.

### Resolution Steps

Once the appendices are converted to MyST Markdown:

1. **Identify the appendix files** containing:
   - Appendix A: Sun compass calculations (referenced as `app:sundec` in LaTeX)
   - Appendix B: Coordinate transformations (referenced as `app:coord` in LaTeX)
   - Appendix with eigenvector calculations (referenced as `app:eigen` in LaTeX)

2. **Add equation labels** in the appendix files:
   ```markdown
   $$
   a_{ij} = ...
   $$ (eq:aij)

   $$
   \text{center of mass} = ...
   $$ (eq:cm)
   ```

3. **Update Chapter 9** to restore the cross-references:

   For eq:aij (around the text about coordinate transformation):
   ```markdown
   By substituting $Az$ and $Pl$ for $\phi$ and $\lambda$ into [Equation %s](#eq:aij), the components...
   ```

   For eq:cm (in the DANG definition):
   ```markdown
   The line connecting the data to the origin is taken as the vector from the origin to the center of mass of the data ([Equation %s](#eq:cm)).
   ```

4. **Verify the references resolve** by running `jupyter book build --execute` and checking for warnings.

### Related Appendix References

Other chapters may also have appendix cross-references that need similar treatment. When converting each chapter, document any appendix references in this file.

| Chapter | Reference | Appendix | Status |
|---------|-----------|----------|--------|
| Chapter 9 | eq:aij | Appendix B (coord) | Pending |
| Chapter 9 | eq:cm | Appendix B (eigen) | Pending |
| Chapter 9 | app:sundec | Appendix A | Pending |
| Chapter 9 | app:coord | Appendix B | Pending |
| Chapter 9 | app:eigen | Appendix B | Pending |
| Chapter 10 | app:pint ($\gamma$ parameter) | Appendix C (pint) | Pending |
| Chapter 10 | app:pint (statistics definitions) | Appendix C (pint) | Pending |
| Chapter 12 | app:eigen (orientation matrix) | Appendix A.3.5 | Pending |
| Chapter 12 | app:kent (Kent ellipse) | Appendix A.3.6 | Pending |
| Chapter 12 | app:bing (Bingham ellipse) | Appendix A.3.7 | Pending |
| Chapter 12 | app:bootstrap (bootstrap principles) | Appendix A.3.8 | Pending |
| Chapter 13 | app:tensors (tensor basics) | Appendix A.3.5 | Pending |
| Chapter 13 | app:eigen (eigenvalue calculation) | Appendix A.3.5 | Pending |
| Chapter 13 | app:K15 (15-position AMS scheme) | Appendix D.1 | Pending |
| Chapter 13 | app:AMSspin (spinning AMS procedure) | Appendix D.2 | Pending |
| Chapter 13 | fig:AMSspin (spinning AMS figure) | Appendix D.2 | Pending |
| Chapter 14 | app:eigen (eigenparameters) | Appendix A.3.5 | Pending |

---

## Chapter 10: Appendix C (Paleointensity Statistics)

During the conversion of Chapter 10, two references to Appendix C were converted to generic text because the appendices have not yet been converted:

1. **Gamma parameter ($\gamma$)**
   - **Location**: Chapter 10, section on TRM anisotropy
   - **Original LaTeX**: `Appendix~\ref{app:pint}`
   - **Current text**: "a parameter called $\gamma$ in Appendix C"
   - **Context**: The gamma parameter is the angle between the pTRM acquired in the laboratory and the laboratory field direction, used to detect anisotropy problems.

2. **Paleointensity statistics definitions**
   - **Location**: Chapter 10, section on "Quality Assurance and Data Selection"
   - **Original LaTeX**: `Appendix~\ref{app:pint}`
   - **Current text**: "Many of these are defined in Appendix C"
   - **Context**: Various statistics for assessing the quality of paleointensity data sets are defined in the appendix.

### Resolution Steps for Chapter 10

Once Appendix C (Paleointensity) is converted:

1. **Create the appendix file** with label `app:pint`

2. **Update Chapter 10** references:

   ```markdown
   a parameter called $\gamma$ in [Appendix %s](#app:pint)
   ```

   ```markdown
   Many of these are defined in [Appendix %s](#app:pint)
   ```

---

---

## Chapter 12: Figure Conversion Required

During the conversion of Chapter 12, the following figures need to be converted from EPS to PNG format using the standard pipeline.

### Figures to Convert

| Figure Label | EPS Source File | Description |
|-------------|-----------------|-------------|
| fig:vgp-di | vgp-di.eps | VGPs and directions from statistical field model |
| fig:confidence | confidence.eps | Fisher, Kent, and Bingham confidence regions |
| fig:love | love.eps | Bi-gaussian vector distribution |
| fig:hypeq | hypeq.eps | Non-Fisherian data with bootstrapped means |
| fig:twofiles | twofiles.eps | Test for common mean with two data sets |
| fig:cdf | cdf.eps | Cumulative distributions of Cartesian components |
| fig:revtest | revtest.eps | Bootstrap reversals test |
| fig:foldtest | unfolding.eps | Bootstrap fold test |

### Conversion Steps

1. **Run figure conversion script**:
   ```bash
   python scripts/convert_figures_inkscape.py --chapter 12
   ```

2. **Review SVGs** in Inkscape for layout issues from font substitution

3. **Regenerate PNGs** after any SVG edits:
   ```bash
   python scripts/convert_figures_inkscape.py --svg-to-png --chapter 12
   ```

4. **Add white backgrounds** for dark mode compatibility:
   ```bash
   for png in book/figures/chapter12/*.png; do
     convert "$png" -background white -alpha remove -alpha off "$png"
   done
   ```

5. **Resize large images** if any exceed 1.5 MB:
   ```bash
   convert book/figures/chapter12/largefile.png -resize 50% book/figures/chapter12/largefile.png
   ```

---

## ~~Chapter 14: Missing Figure~~ (RESOLVED)

The fig:spoon (Chinese compass) figure has been created by combining:

- `compass1.jpg` (south-pointing spoon photo)
- Chinese declination data from `chinesedec.dat` (Smith and Needham, 1967)

The composite figure was generated using `scripts/create_chinesecompass_figure.py` and saved to `book/figures/chapter14/chinesecompass.png`.

---

*Last updated: 2026-02-11*

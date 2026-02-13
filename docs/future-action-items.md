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
| Chapter 1 | app:definitions | Appendix A (mathematical tricks) | **Converted** |
| Chapter 1 | app:nabla | Appendix A (nabla operator) | **Converted** |
| Chapter 1 | app:vecmult | Appendix A (vector multiplication) | **Converted** |
| Chapter 2 | app:eqarea | Appendix B (equal area projection) | **Converted** |
| Chapter 2 | app:tensors | Appendix A (coordinate transformations) | **Converted** |
| Chapter 2 | app:strig | Appendix A (spherical trigonometry) | **Converted** |
| Chapter 9 | eq:aij | Appendix A (coord) | **Converted** |
| Chapter 9 | eq:cm | Appendix A (eigen) | **Converted** |
| Chapter 9 | app:sundec | Appendix A | **Converted** |
| Chapter 9 | app:coord | Appendix A | **Converted** |
| Chapter 9 | app:eigen | Appendix A | **Converted** |
| Chapter 10 | app:pint ($\gamma$ parameter) | Appendix C (pint) | **Converted** |
| Chapter 10 | app:pint (statistics definitions) | Appendix C (pint) | **Converted** |
| Chapter 12 | app:eigen (orientation matrix) | Appendix A | **Converted** |
| Chapter 12 | app:kent (Kent ellipse) | Appendix C | **Converted** |
| Chapter 12 | app:bing (Bingham ellipse) | Appendix C | **Converted** |
| Chapter 12 | app:bootstrap (bootstrap principles) | Appendix A | **Converted** |
| Chapter 13 | app:tensors (tensor basics) | Appendix A | **Converted** |
| Chapter 13 | app:eigen (eigenvalue calculation) | Appendix A | **Converted** |
| Chapter 13 | app:K15 (15-position AMS scheme) | Appendix D | **Converted** |
| Chapter 13 | app:AMSspin (spinning AMS procedure) | Appendix D | **Converted** |
| Chapter 13 | fig:AMSspin (spinning AMS figure) | Appendix D | Figures pending |
| Chapter 14 | app:eigen (eigenparameters) | Appendix A | **Converted** |
| Chapter 3 | app:langevin (Langevin function derivation) | Appendix A | **Converted** |
| Chapter 16 | app:polerot (finite rotation poles) | Appendix A | **Converted** |
| Chapter 16 | app:strig (spherical trigonometry) | Appendix A | **Converted** |
| Chapter 16 | app:bootstrap (bootstrap) | Appendix A | **Converted** |
| Chapter 16 | app:eigen (orientation matrix/eigenvalues) | Appendix A | **Converted** |

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

## Chapter 3: Figure Conversion Required

During the conversion of Chapter 3, the following figures need to be converted from EPS to PNG format using the standard pipeline.

### Figures to Convert

| Figure Label | EPS Source File | Description |
|-------------|-----------------|-------------|
| fig:1s | 1s.eps | Radial distribution and dot-density for 1s electron shell |
| fig:shells | shells.eps | Surfaces of equal probability for electronic shells |
| fig:structure | structure.eps | Electronic structure of elements from Na to Zn |
| fig:larmor | larmor.eps | Larmor precession diagram |
| fig:para | para.eps | Paramagnetic magnetization (Langevin function, Curie Law) |
| fig:exchange | exchange.eps | Exchange energy and super-exchange diagram |
| fig:MsT | MsT.eps | Magnetization versus temperature for ferromagnetic substance |
| fig:curie | curie.eps | M_s(T) data sets for magnetite |
| fig:spins | spins.eps | Types of spin alignment in ferromagnetism |
| fig:spinwave | spinwave.eps | Spin wave response to magnetic torque |

### Conversion Steps

1. **Run figure conversion script**:
   ```bash
   python scripts/convert_figures_inkscape.py --chapter 3
   ```

2. **Review SVGs** in Inkscape for layout issues from font substitution

3. **Regenerate PNGs** after any SVG edits:
   ```bash
   python scripts/convert_figures_inkscape.py --svg-to-png --chapter 3
   ```

4. **Add white backgrounds** for dark mode compatibility:
   ```bash
   for png in book/figures/chapter3/*.png; do
     convert "$png" -background white -alpha remove -alpha off "$png"
   done
   ```

5. **Resize large images** if any exceed 1.5 MB:
   ```bash
   convert book/figures/chapter3/largefile.png -resize 50% book/figures/chapter3/largefile.png
   ```

---

## Chapter 1: Figure Conversion Required

During the conversion of Chapter 1, the following figures need to be converted from EPS to PNG format using the standard pipeline.

### Figures to Convert

| Figure Label | EPS Source File | Description |
|-------------|-----------------|-------------|
| fig:filings | wire.eps | Iron filings around current-carrying wire; right-hand rule |
| fig:moment | moment.eps | Magnetic moment from current loop; solenoid field |
| fig:barmagnet | barmagnetfield.eps | Bar magnet field lines; electromagnetic induction |
| fig:compass | compass.eps | Compass needle alignment with magnetic field |
| fig:pp | pp.eps | Force between two magnetic monopoles |
| fig:divergence | divergence.eps | Divergence of electric vs magnetic fields |
| fig:mH | mH.eps | Field H from magnetic moment at point P |
| fig:faraday | discdynamo.eps | Self-exciting disk dynamo diagram |
| fig:dipole | dipole.eps | Magnetic dipole in Earth cross-section (Problem 3) |

### Conversion Steps

1. **Run figure conversion script**:
   ```bash
   python scripts/convert_figures_inkscape.py --chapter 1
   ```

2. **Review SVGs** in Inkscape for layout issues from font substitution

3. **Regenerate PNGs** after any SVG edits:
   ```bash
   python scripts/convert_figures_inkscape.py --svg-to-png --chapter 1
   ```

4. **Add white backgrounds** for dark mode compatibility:
   ```bash
   for png in book/figures/chapter1/*.png; do
     convert "$png" -background white -alpha remove -alpha off "$png"
   done
   ```

5. **Resize large images** if any exceed 1.5 MB:
   ```bash
   convert book/figures/chapter1/largefile.png -resize 50% book/figures/chapter1/largefile.png
   ```

---

---

## Appendix: Large Data Tables

During the conversion of the Appendices, several large data tables were intentionally omitted from the markdown conversion. These tables contain extensive numerical data that would be better served as downloadable data files or interactive elements.

### Tables to Convert to Alternative Formats

| Table Label | Original LaTeX | Appendix | Description | Recommended Format |
|------------|----------------|----------|-------------|-------------------|
| tab:gondrot | longtable | A | Finite rotations for Gondwana continents (AUS, ANT, IND, SAM) relative to South Africa, 5-320 Ma | CSV + interactive widget |
| tab:laurot | longtable | A | Finite rotations for Laurentian continents (EUR, NAM, GRN) relative to South Africa, 5-320 Ma | CSV + interactive widget |
| tab:safpmag | table | A | Finite rotations for South Africa to paleomagnetic reference frame, 5-320 Ma | CSV + interactive widget |
| tab:bingham | sidewaystable | C | Maximum likelihood estimators of $k_1, k_2$ in Bingham distribution for given eigenvalues | CSV or lookup function |

### Recommended Implementation

1. **CSV Data Files**: Export the rotation pole data to CSV files in a `data/` directory for download
   - `data/gondwana_rotations.csv`
   - `data/laurentia_rotations.csv`
   - `data/south_africa_pmag_rotations.csv`
   - `data/bingham_parameters.csv`

2. **Interactive Widgets**: Consider adding Plotly or ipywidgets-based interactive elements that allow users to:
   - Select a continent and age to retrieve rotation parameters
   - Visualize rotation poles on a map
   - Interpolate between tabulated ages

3. **PmagPy Integration**: These rotation tables are available in PmagPy - consider linking to the relevant functions rather than duplicating the data

### Source Data

The rotation data are from {cite:t}`torsvik2008` - see original publication for additional options and data.

---

## Appendix: Figure Conversion Required

During the conversion of the Appendices (A, B, C, D), the following figures need to be converted from EPS to PNG format using the standard pipeline.

### Figures to Convert

| Figure Label | EPS Source File | Appendix | Description |
|-------------|-----------------|----------|-------------|
| fig:strig | strig.eps | A | Spherical trigonometry rules |
| fig:vectors | vectors.eps | A | Vector addition diagram |
| fig:cross | cross.eps | A | Cross product illustration |
| fig:transform | dircosines.eps | A | Direction cosines definition |
| fig:trans | transform.eps | A | Coordinate transformation |
| fig:ski | ski.eps | A | Gradient illustration (ski slope) |
| fig:div | div.eps | A | Divergence (non-zero) |
| fig:divzero | divzero.eps | A | Divergence (zero) |
| fig:curl | curl.eps | A | Curl of vector field |
| fig:bootstrap | bootstrap.eps | A | Bootstrap method illustration |
| fig:sundefs | sundefs.eps | A | Sun compass definitions |
| fig:mkeq | mkeq.eps | B | Equal area projection construction |
| fig:equal | equal.eps | B | Schmidt (equal area) net |
| fig:how2eq | how2eq.eps | B | How to use equal area net |
| fig:tilt | tilt.eps | B | Bedding-tilt corrections |
| fig:how2tern | ternary.eps | B | How to read ternary diagram |
| fig:Ais | Ais.eps | B | Q-Q plot illustration |
| fig:hparcalc | hparcalc.eps | C | Hysteresis parameter calculation |
| fig:IZZI | IZZI.eps | C | Paleointensity parameters |
| fig:meas15 | meas15.eps | D | 15-position AMS measurement scheme |
| fig:AMSspin | AMSspin.eps | D | Spinning AMS orientations |
| fig:AMSspinProc | AMSspinProc.eps | D | Spinning AMS processing steps |

### Conversion Steps

1. **Run figure conversion script**:
   ```bash
   python scripts/convert_figures_inkscape.py --files strig.eps vectors.eps cross.eps dircosines.eps transform.eps ski.eps div.eps divzero.eps curl.eps bootstrap.eps sundefs.eps mkeq.eps equal.eps how2eq.eps tilt.eps ternary.eps Ais.eps hparcalc.eps IZZI.eps meas15.eps AMSspin.eps AMSspinProc.eps --output-dir book/figures/appendix/
   ```

2. **Review SVGs** in Inkscape for layout issues from font substitution

3. **Regenerate PNGs** after any SVG edits:
   ```bash
   python scripts/convert_figures_inkscape.py --svg-to-png --files strig.eps vectors.eps cross.eps dircosines.eps transform.eps ski.eps div.eps divzero.eps curl.eps bootstrap.eps sundefs.eps mkeq.eps equal.eps how2eq.eps tilt.eps ternary.eps Ais.eps hparcalc.eps IZZI.eps meas15.eps AMSspin.eps AMSspinProc.eps --output-dir book/figures/appendix/
   ```

4. **Add white backgrounds** for dark mode compatibility:
   ```bash
   for png in book/figures/appendix/*.png; do
     convert "$png" -background white -alpha remove -alpha off "$png"
   done
   ```

5. **Resize large images** if any exceed 1.5 MB:
   ```bash
   convert book/figures/appendix/largefile.png -resize 50% book/figures/appendix/largefile.png
   ```

---

*Last updated: 2026-02-12*

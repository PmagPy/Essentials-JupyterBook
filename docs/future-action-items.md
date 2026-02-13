# Future Action Items

This document tracks action items identified during the LaTeX to MyST Markdown conversion that require future work once additional chapters or components are converted.

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

*Last updated: 2026-02-12*

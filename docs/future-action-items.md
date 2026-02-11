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

---

*Last updated: 2026-02-10*

---
title: "Appendix D: Anisotropy in Paleomagnetism"
label: app:anis
authors:
  - name: Lisa Tauxe
    affiliation: Scripps Institution of Oceanography, UC San Diego
numbering:
  enumerator: D.%s
---

(app:K15)=
## The 15 measurement protocol

The {cite:t}`jelinek1978` 15 measurement scheme is illustrated in [](#fig:meas15). This is the procedure recommended in the manual distributed with the popular Kappabridge susceptibility instruments. In the 15 measurement case shown in [](#fig:meas15), the design matrix is:

$$
\mathbf{A}=
\begin{pmatrix}
.5&.5&0&-1&0&0\\
.5&.5&0&1&0&0\\
1&0&0&0&0&0\\
.5&.5&0&-1&0&0\\
.5&.5&0&1&0&0\\
0&.5&.5&0&-1&0\\
0&.5&.5&0&1&0\\
0&1&0&0&0&0\\
0&.5&.5&0&-1&0\\
0&.5&.5&0&1&0\\
.5&0&.5&0&0&-1\\
.5&0&.5&0&0&1\\
0&0&1&0&0&0\\
.5&0&.5&0&0&-1\\
.5&0&.5&0&0&1
\end{pmatrix},
$$ (eq:ajel)

and

$$
\mathbf{B}={1\over {20}}\times
$$

$$
\begin{pmatrix}
3&3&8&3&3&-2&-2&-2&-2&-2&3&3&-2&3&3\\
3&3&-2&3&3&3&3&8&3&3&-2&-2&-2&-2&-2\\
-2&-2&-2&-2&-2&3&3&-2&3&3&3&3&8&3&3\\
-5&5&0&-5&5&0&0&0&0&0&0&0&0&0&0\\
0&0&0&0&0&-5&5&0&-5&5&0&0&0&0&0\\
0&0&0&0&0&0&0&0&0&0&-5&5&0&-5&5
\end{pmatrix}.
$$ (eq:bjel)

:::{figure} ../figures/appendix/meas15.png
:name: fig:meas15
:width: 100%

The 15 position scheme of {cite:t}`jelinek1978` for measuring the AMS of a sample. [Figure from {cite:t}`tauxe1998`.]
:::

(app:AMSspin)=
## The spinning protocol

:::{figure} ../figures/appendix/AMSspin.png
:name: fig:AMSspin
:width: 100%

Specimen orientations for the three spins used with spinning magnetic susceptibility meters. The heavy gray arrows show the axes of rotation; one oriented toward the user for Position 1 (a) and 2 (b) away from the user for Position 3 (c). The orientation of the specimen coordinate system in space is specified by the azimuth and plunge of either the arrow along the core length (+x$_3$ axis, black) or the +x$_1$ axis (red arrow on core top). d) orientation of applied field (coil axis) relative to specimen coordinates in Position 3. [Figure from {cite:t}`gee2008`.]
:::

More recent models of the Kappabridge magnetic susceptibility instruments (e.g., KLY-3S and KLY-4S; see e.g., {cite:t}`pokorny2004`) measure anisotropy by spinning the specimen around three axes ([](#fig:AMSspin)). For complete measurement and analysis details, see {cite:t}`gee2008`. Here we just give the bare bones explanation.

The specimen is lowered into the measurement region and the susceptibility meter is set to zero. The deviatoric susceptibility is then measured in 64 positions per revolution for multiple (often eight) revolutions (see [](#fig:AMSspinProc)a). These data must be corrected for instrumental drift (red line in the figure), adjusted to have zero mean and stacked ([](#fig:AMSspinProc)b). The data can be fit with a best fit theoretical curve (red line in the figure). The theoretical curve can be derived from the complicated design matrix (see {cite:t}`gee2008` for details). As one example, the measurement recorded at an angle $\theta_i$ (as shown in [](#fig:AMSspin)d) while spinning in Position 1 ([](#fig:AMSspin)a) is given by:

$$
K^{x1}_i = \chi_{22} \sin^2 \theta_i + 2\chi_{23} \cos \theta_i \sin \theta_i + \chi_{33} \cos^2 \theta_i.
$$

The best fit values for $\chi$ for the entire sequence of data gives the 2D Model for the set of data (see [](#fig:AMSspinProc)b). There are three such models for the measurement protocol, each yielding estimates of two of the three on-axis $\chi$ values ($\chi_{11}, \chi_{22}, \chi_{33}$). These measurements are all adjusted to zero mean susceptibility so one more measurement is required to determine the bulk susceptibility (the absolute susceptibility measured in the position shown in [](#fig:AMSspin)c or $\chi_{11}$ in Position 3). The three 2D models plus the bulk measurement are combined as shown in [](#fig:AMSspinProc)d whereby the $\chi_{11}$ position in the 2D model for Position 3 is adjusted to the bulk measurement, and the best-fit 3D model is found that minimizes cross over errors for pairs of $\chi_{11}, \chi_{22}, \chi_{33}$. Once the best fit values for $\chi$ are found and standard deviation, the data can be treated as described in Chapter 13.

:::{figure} ../figures/appendix/AMSspinProc.png
:name: fig:AMSspinProc
:width: 100%

Processing steps for data spin protocol. a) From a single spin with eight revolutions. Raw data with peaks (red dots) identified by peak-finding algorithm and best fit linear trend. Data are detrended using peaks. b) Data from detrended individual revolutions and best fit 2-D model. c) Original (zero-mean) deviatoric susceptibility data from three spins. The best fit 2-D model for each spin provides an estimate of two elements of the deviatoric susceptibility tensor (square, $\chi_{11}$; hexagon, $\chi_{22}$; circle, $\chi_{33}$). Thick bars indicate the calculated offsets for Positions 1 and 2. d) Crossover adjustment for data from three positions. Original (zero-mean) deviatoric susceptibility data from three positions are scaled to absolute values (right-hand scale) using a bulk measurement in spin Position 3, and adjusted to minimize cross over error. [Figure modified from {cite:t}`gee2008`.]
:::

(app:aarm)=
## Correction of inclination error with AARM

The magnitude of ARM is here denoted $M_a$. The particle anisotropy is denoted $a$ and is given by:

$$
a = \bigl[ {{M_{a_{||}} }\over { M_{a_{\perp} } }}\bigr]_{particle},
$$ (eq:a)

where $M_{a_{||}}$ and $M_{a_{\perp}}$ are the magnitudes of the ARM acquired parallel to and perpendicular to the detrital particle long axis respectively. The normalized eigenvalues of the ARM tensor ($q_i$) are defined as:

$$
q_i = { {M_{a_i}} \over {M_a} }.
$$

{cite:t}`stephenson1986` defined an orientation distribution function for the preferred alignment of particle long axes whose eigenvalues are given by $\kappa_i$ where $\kappa_1 > \kappa_2 > \kappa_3$ as usual. {cite:t}`jackson1991` collect together the two sources of anisotropy (alignment of particle long axes and individual particle anisotropies) as:

$$
\kappa_i = { {q_i(a+2) -1 } \over { (a-1) } }.
$$ (eq:kappa)

Assuming that the DRM anisotropy is identical to the orientation distribution function of particle long axes we can combine and rearrange [Equation %s](#eq:flattening) and [Equation %s](#eq:kappa) to get the relationship between the flattening factor $f$ and the ARM anisotropy:

$$
f= {{ q_3 (a+2)-1} \over { q_1 (a+2) -1} }.
$$

From the foregoing, measuring the AARM tensor yields the values for $q$, but determining values for $a$ are more problematic. {cite:t}`vaughn2005` describe a technique whereby magnetic particles are separated from the matrix, then allowed to dry in an epoxy matrix in the presence of a magnetic field sufficient to fully align the long axes of the magnetic particles (say 50 mT). The AARM parallel to and perpendicular to the axis of alignment therefore gives $a$ by [Equation %s](#eq:a).

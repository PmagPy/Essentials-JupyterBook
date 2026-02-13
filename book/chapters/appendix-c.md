---
title: "Appendix C: Paleomagnetic Statistics and Parameter Estimation"
label: app:statistics
authors:
  - name: Lisa Tauxe
    affiliation: Scripps Institution of Oceanography, UC San Diego
numbering:
  enumerator: C.%s
---

Chapters 5 and 7 discussed various hysteresis parameters and Chapters 11 and 12 developed the major features of paleomagnetic directional statistics. Here we go over some aspects in greater detail.

(app:hyst)=
## Hysteresis Parameters

A typical hysteresis experiment involves determination of a hysteresis loop and frequently also a back-field curve (see [](#fig:hparcalc)). Processing of the data in the **PmagPy** software package (see, e.g., Example for **hysteresis_magic.py**) proceeds as follows:

1. Sometimes the descending and ascending hysteresis loops do not close because of instrument drift (see [](#fig:hparcalc)a). Ordinarily, the experiment should be re-done, but for small differences, we force the loops to close by subtracting the difference, interpolated from the maximum difference at the maximum field ($B_{max}$) to a zero difference at the minimum field ($B_{min}$).

2. After closing the loops, we calculate the best-fit line to the $M, B$ data for the portion within 70% of $\pm B_{max}$, averaging data from both the ascending and descending loops. A difference in the absolute value of the y-intercepts for the ascending and descending loops indicates a vertical offset of the data, which is adjusted such that the two intercepts are equal. The average slope is the high-field susceptibility ($\chi_{hf}$), which is subtracted off. The data after these steps are shown as the dashed line in [](#fig:hparcalc). The maximum magnetization after adjusting for the $\chi_{hf}$ is the saturation magnetization $M_s$.

:::{table} Summary of hysteresis parameters.
:name: tab:hystpars

| Symbol | Method | Section | Figure |
|--------|--------|---------|--------|
| $\chi_{hf}$ | high field susceptibility | [](#sect:chi) & [](#sect:hyst) | [](#fig:Bcr) & [](#fig:hparcalc) |
| $M_s$ | saturation magnetization | [](#sect:para) | [](#fig:Bcr) & [](#fig:hparcalc) |
| $M_r$ | saturation remanence | [](#sect:uniaxial) & [](#sect:irm) | [](#fig:Bcr) & [](#fig:hparcalc) |
| $H_{c}$ or $\mu_oH_{c}$ | Coercivity | [](#sect:K1) & [](#sect:uniaxial) | [](#fig:Bcr) & [](#fig:hparcalc) |
| **Coercivity of remanence:** | | | |
| $H_{cr}$ | $\Delta M$ method | [](#sect:uniaxial) | [](#fig:hparcalc) |
| $H_{cr}'$ | ascending loop intercept method | [](#sect:uniaxial) | [](#fig:Bcr) |
| $H_{cr}''$ | Back-field method | [](#sect:irm) | [](#fig:irm) & [](#fig:hparcalc) |
| $H_{cr}'''$ | $H_{1/2}$ method | [](#sect:irm) & [](#sect:unmixing) | [](#fig:irm) & [](#fig:unmixing) |
:::

:::{figure} ../figures/appendix/hparcalc.png
:name: fig:hparcalc
:width: 100%

Typical hysteresis experiment. a) Raw data are solid red line. Data are processed (see text) by closing the ascending and descending loops, subtracting the high field slope ($\chi_{hf}$) and adjusting such that the y-intercepts are equal (that for the descending loop is labeled $M_r$). Processed data are dotted blue line. Coercivity ($\mu_oH_{c}$) is the applied field for which a saturation magnetization ($M_s$) is reduced to zero. b) Difference between processed ascending and descending loops is the $\Delta M$ curve (solid blue line). Back-field IRM data shown normalized by saturation remanence ($M_r$) -- dashed green line. Two methods of estimating coercivity of remanence shown (see text).
:::

3. Coercivity ($\mu_o H_c$) is the field at which $M=0$. We estimate this by finding the values of $B$ between which $M$ switches sign for both the ascending and descending loops (after adjustment), calculate a line and evaluate the $B$ for which $M=0$. The coercivity is the average of the two estimates.

4. We fit a spline to the adjusted ascending and descending loops and resample the loops at even intervals of $B$ (usually 10 mT intervals). The $\Delta M$ curve shown in [](#fig:hparcalc)b is the difference between these two interpolated curves, averaging the data for negative and positive $B$. The saturation remanence $M_r$ is the value of the $\Delta M$ curve at $B=0$. The coercivity of remanence ($\mu_oH_{cr}$ in [](#tab:hystpars)) is the field for which $\Delta M$ is half the value of $M_r$. This is the "$\Delta M$" method of coercivity of remanence calculation (see Chapter 5).

5. If there are "back-field" IRM data as in [](#fig:hparcalc)b, the coercivity of remanence can be estimated by finding (through interpolation) the applied field which reduces the saturation remanence ($M_r$) to zero. This is the "back field" method.

(app:dirstics)=
## Directional statistics

:::{table} Critical values of $R_o$ for a random distribution {cite:p}`watson1956`.
:name: tab:Ro-appendix

| $N$ | 95% | 99% | $N$ | 95% | 99% |
|-----|-----|-----|-----|-----|-----|
| 5 | 3.50 | 4.02 | 13 | 5.75 | 6.84 |
| 6 | 3.85 | 4.48 | 14 | 5.98 | 7.11 |
| 7 | 4.18 | 4.89 | 15 | 6.19 | 7.36 |
| 8 | 4.48 | 5.26 | 16 | 6.40 | 7.60 |
| 9 | 4.76 | 5.61 | 17 | 6.60 | 7.84 |
| 10 | 5.03 | 5.94 | 18 | 6.79 | 8.08 |
| 11 | 5.29 | 6.25 | 19 | 6.98 | 8.33 |
| 12 | 5.52 | 6.55 | 20 | 7.17 | 8.55 |
:::

(app:watsonsV)=
### Calculation of Watson's $V_w$

1. Calculate $R_i$, and $k_i$ where $i=1,2$ for the two data sets with $N_1, N_2$ samples using [Equation %s](#eq:R) and [Equation %s](#eq:k).

2. Calculate $\bar x_{ij}$ (where $j=1,3$ for the three axes) using [Equation %s](#eq:xbar).

3. Calculate $\bar X_{ij}= R_i \bar x_{ij}$.

4. Find the weighted means for the two data sets:

$$
\hat X_j = \sum_i^2 k_i\bar X_{ij}.
$$

5. Calculate the weighted overall resultant vector $R_w$ by

$$
R_w = (\hat X_1^2 + \hat X_2^2 + \hat X_3^2)^{1/2},
$$

and the weighted sum $S_w$ by,

$$
S_w = \sum_i^2 k_iR_i.
$$

6. Finally, Watson's $V_w$ is defined as

$$
V_w = 2(S_w -R_w).
$$

(app:linesNplanes)=
### Combining lines and planes

1. Calculate $M$ directed lines (two in our case) and $N$ great circles (one in our case) using principal component analysis (see Chapter 9) or Fisher statistics.

2. Assume that the primary direction of magnetization for the samples with great circles lies somewhere along the great circle path (i.e., within the plane).

3. Assume that the set of $M$ directed lines and $N$ unknown directions are drawn from a Fisher distribution.

4. Iteratively search along the great circle paths for directions that maximize the resultant vector $R$ for the $M+N$ directions.

5. Having found the set of $N$ directions that lie along their respective great circles, estimate the mean direction using [Equation %s](#eq:xbar) and $\kappa$ as:

$$
k= {{2M+N-2}\over {2(M+N-R)}},
$$

The cone of 95% confidence about the mean is given by:

$$
\cos \alpha_{95} = 1 - { {N'-1}\over {kR}} \bigl[ \bigl({1\over p}\bigr)^{1/(N'-1)} -1 \bigr],
$$

where $N'=M+N/2$ and $p$ = .02

(app:incfish)=
### Inclination only calculation

We wish to estimate the co-inclination ($\alpha=90-I$) of $N$ Fisher distributed data ($\alpha_i$), the declinations of which are unknown. We define the estimated value of $\alpha$ to be $\hat \alpha$. {cite:t}`mcfadden1982` showed that $\hat \alpha$ is the solution of:

$$
N \cos \hat \alpha + (\sin^2\hat \alpha-\cos^2\hat\alpha)\sum \cos \alpha_i -2\sin \hat \alpha \cos \hat \alpha \sum \alpha_i = 0,
$$

which can be solved numerically.

They further define two parameters $S$ and $C$ as:

$$
S = \sum \sin(\hat \alpha - \alpha_i),
$$

$$
C = \sum \cos(\hat \alpha - \alpha_i).
$$

An unbiased approximation for the Fisher parameter $\kappa$, $k$ is given by:

$$
k = { {N-1}\over {2(N-C)} }.
$$

The unbiased estimate $\hat I$ of the true inclination is:

$$
\hat I= 90 - \hat \alpha + {S\over C}.
$$

Finally, the $\alpha_{95}$ is estimated by:

$$
\cos \alpha_{95} = 1 - {1\over 2} \bigl({S\over C}\bigr)^2 - {f\over{2Ck}},
$$

where $f$ is the critical value taken from the $F$ distribution (see F-distribution tables in statistics textbooks or online) with 1 and ($N$-1) degrees of freedom.

(app:kent)=
### Kent 95% confidence ellipse

Kent parameters are calculated by rotating unimodal directions $x$ into the data coordinates $x'$ by the transformation:

$$
{x }' = \boldsymbol{\Gamma}^T {x },
$$ (eq:xgammax)

where $\boldsymbol{\Gamma} =(\boldsymbol{\gamma}_1, \boldsymbol{\gamma}_2, \boldsymbol{\gamma}_3)$, and the columns of $\boldsymbol{\Gamma}$ are called the constrained eigenvectors of orientation matrix, $\mathbf{T}$ (see [](#app:eigen)). The vector $\boldsymbol{\gamma}_1$ is parallel to the Fisher mean of the data, whereas $\boldsymbol{\gamma}_2$ and $\boldsymbol{\gamma}_3$ (the major and minor axes) diagonalize $\mathbf{T}$ as much as possible subject to being constrained by $\boldsymbol{\gamma}_1$ (see {cite:t}`kent1982`, but note that his $x_1$ corresponds to $x_3$ in conventional paleomagnetic notation). The following parameters may then be computed:

$$
\hat \mu = N^{-1} \sum_k {x_{k1}}'
$$
$$
\hat \sigma^2_2={N^{-1}}\sum_k ({x_{k2}}')^2
$$
$$
\hat \sigma^2_3={N^{-1}}\sum_k ({x_{k3}}')^2.
$$ (eq:kentpars)

As defined here, $\hat \mu = R/N$ ($R$ is closely approximated by the equation for $R$ in Chapter 11. Also to good approximation, $\hat \sigma_2^2 = \tau_2,$ and $\hat \sigma_3^2 = \tau_3$, where $\tau_i$ are the eigenvalues of the orientation matrix.

The semi-angles $\zeta_{95}$ and $\eta_{95}$ subtended by the major and minor axes of the 95% confidence ellipse are given by:

$$
\zeta_{95} = \sin^{-1}(\sigma_2 \sqrt {g}), \quad \eta_{95} = \sin^{-1}(\sigma_3 \sqrt {g}),
$$ (eq:zeta)

where $g=-2\ln(0.05)/(N \hat\mu^2)$.

The tensor $\boldsymbol{\Gamma}$ is, to a good approximation, equivalent to $\mathbf{V}$, the eigenvectors of the orientation matrix. Therefore, the eigenvectors of the orientation matrix $\mathbf{V}$ give a good estimate for the directions of the semi-angles by:

$$
D_{\zeta}= \tan^{-1} ({v_{22}/v_{12}}), \quad I_{\zeta} = \sin^{-1} {v_{32}},
$$
$$
D_{\eta}= \tan^{-1} ({v_{23}/v_{13}}), \quad I_{\eta} = \sin^{-1}{v_{33}},
$$ (eq:dizeta)

where for example the $x_2$ component of the smallest eigenvector $\mathbf{V}_3$ is denoted $v_{23}$.

(app:bing)=
### Bingham 95% confidence parameters

The Bingham distribution is given by:

$$
F = {1\over {4\pi d(k_1,k_2)} } \exp( k_1\cos^2 \phi+k_2\sin^2\phi)\sin^2 \alpha,
$$

where $\alpha$ and $\phi$ are as in the Kent distribution, $k_1,k_2$ are concentration parameters ($k_1<k_2<0$) and $d(k_1,k_2)$ is a constant of normalization given by:

$$
d(k_1,k_2) = { 1\over {4\pi} } \int_0^{2\pi} \int_0^\pi \exp ( (k_1\cos^2 \phi + k_2 \sin^2 \phi)\sin^2 \theta) \sin \theta d\theta d\phi.
$$

To estimate the axes of the Bingham confidence ellipse, we first calculate the eigenparameters of the orientation matrix as for Kent parameters and described in [](#app:eigen) and [](#app:kent). The principal eigenvector $\mathbf{V}_1$ of the orientation matrix is associated with the largest eigenvalue $\tau_1$. In {cite:t}`bingham1974`, $\omega_1$ is the $\tau_3$ and $\omega_3$ is $\tau_1$. In Bingham statistics, the $\mathbf{V}_1$ direction is taken as the mean. Beware -- it is not always parallel to the Fisher mean of a unimodal set of directions.

The maximum likelihood estimates of $k_1,k_2$, the concentration parameters are obtained by first maximizing the log likelihood function:

$$
F= -N\log(4\pi) - N \log d(k_1,k_2) + k_1\omega_1+ k_2\omega_2.
$$

These are tabulated in {cite:t}`mardia1977`. Once these are estimated, the semi-axes of the 95% confidence ellipse around the mean direction $\mathbf{V}_1$ are given by:

$$
\epsilon^2_{ij} = \chi_{p}^2(\nu)\sigma^2_{ij},
$$

where $\chi_{p}^2(\nu)=5.99$ is the $\chi^2$ value for significance ($p=.05$ for 95% confidence) with $\nu=2$ degrees of freedom and

$$
\sigma_{ij}^2= { 1\over{2N(\omega_i-\omega_j)(k_i-k_j)}}.
$$

{cite:t}`bingham1974` set $k_3 = 0$, so the semi axes of the confidence ellipse about the principal direction $\mathbf{V}_1$, associated with $\omega_3$, are therefore:

$$
\epsilon_{32} = { 1.22 \over {-k_2N(\omega_3-\omega_2) } },
$$

and

$$
\epsilon_{31} = { 1.22 \over {-k_1N(\omega_3-\omega_1) } }.
$$

Because $k_1<k_2<0$, the semi-axes are positive numbers. Please note that here we use the corrected version of {cite:t}`tanaka1999` as opposed to the more oft-quoted but erroneous treatment of {cite:t}`onstott1980`. Note also that the $N$ is required for $\sigma$ because we have normalized the $\omega$s to sum to unity for consistency with other eigenvalue problems in this book. The $N$ is missing in the treatment of {cite:t}`tanaka1999` presumably because the eigenvalues sum to $N$. Finally, note that these values of $\epsilon$ are in radians and must be converted to degrees for most applications.

(app:pint)=
## Paleointensity statistics

Paleointensity statistics have gotten somewhat out of hand of late. There are a bewildering variety of statistics that are used in the literature, with no consensus as to which ones are essential, which ones are helpful and which ones are irrelevant. This appendix will not help the reader in this regard, but merely attempts to assemble the ones we feel are the most useful.

:::{figure} ../figures/appendix/IZZI.png
:name: fig:IZZI
:width: 100%

Illustration of paleointensity parameters. **Arai plots:** The magnitude of the NRM remaining after each step is plotted versus the pTRM gained at each temperature step. Closed symbols are zero-field first followed by in-field steps (ZI) while open symbols are in-field first followed by zero field (IZ). Triangles are pTRM checks and squares are pTRM tail checks. Horizontal dashed lines are the vector difference sum (VDS) of the NRM steps. **Vector endpoint plots:** Insets are the x,y (solid symbols) and x,z (open symbols) projections of the (unoriented) natural remanence (zero field steps) as it evolves from the initial state (plus signs) to the demagnetized state. The laboratory field was applied along -Z. Diamonds indicate bounding steps for calculations. a) The $f_{vds}$ is the fraction of the component used of the total VDS. The difference between the pTRM check and the original measurement at each step is $\delta T_i$. The inset shows the deviation angle (DANG) that a component of NRM makes with the origin. The maximum angle of deviation MAD is calculated from the scatter of the points about the best-fit line (solid green line). b) Data exhibit "zig-zag behavior" diagnostic for significant difference between blocking and unblocking temperatures. The Zig-zag for slopes compares slopes calculated between ZI and IZ steps ($b_{zi}$) with those connecting IZ and ZI steps $b_{iz}$). The difference between the pTRM tail check and the original measurement at each step is $\Delta T_i$. c) $\beta$ reflects the scatter ($\delta_x, \delta_y$) about the best-fit slope (solid green line). The Zig-zag for directions compares those calculated between ZI and IZ steps ($D_{zi}$) with those connecting IZ and ZI steps $D_{iz}$). [Figures from {cite:t}`benyosef2008`.]
:::

1. The Deviation of the ANGle (DANG; {cite:t}`tauxe2004`; see Chapter 9): The angle that the direction of the NRM component used in the slope calculations calculated as a best-fit line (see [](#app:eigen)) makes with the angle of the line anchoring the center of mass (see [](#app:eigen)) to the origin (see insert to [](#fig:IZZI)a).

2. The Maximum Angle of Deviation (MAD; {cite:t}`kirschvink1980`; see Chapter 9): The scatter about the best-fit line through the NRM steps.

3. We can calculate the best-fit slope ($b$) for the data on the NRM-pTRM plot and its standard error $\sigma$ ({cite:t}`york1966`; {cite:t}`coe1978`). The procedure for calculating the best-fit slope, which is the best estimate for the paleofield, is given as follows:

   a) Take the $N$ data points that span two temperature steps $T_1$ and $T_2$, the best-fit slope $b$ relating the NRM ($y_i$) and the pTRM ($x_i$) data in a least squares sense (taking into account variations in both $x$ and $y$) is given by:

   $$
   b=- \sqrt{ {\sum_i (y_i-\bar y)^2}\over {\sum_i (x_i-\bar x)^2} },
   $$ (eq:slope)

   where $\bar y$ is the average of all $y$ values and $\bar x$ is the average of all $x$ values.

   b) The y-intercept ($y_o$) is given by $\bar y - b\bar x$.

   c) The standard error of the slope $\sigma$ is:

   $$
   \sigma_b = \sqrt { {2\sum_i (y_i -\bar y)^2 - 2b \sum_i (x_i-\bar x)(y_i-\bar y)} \over {(N-2)\sum_i(x_i-\bar x)^2} }.
   $$ (eq:stderr)

4. The "scatter" parameter $\beta$: the standard error of the slope $\sigma$ (assuming uncertainty in both the pTRM and NRM data) over the absolute value of the best-fit slope $|b|$ ({cite:t}`coe1978`).

5. The remanence fraction, $f$, was defined by {cite:t}`coe1978` as:

   $$
   f = \Delta y_T/ y_o,
   $$

   where $\Delta y_T$ is the length of the NRM segment used in the slope calculation (see [](#fig:IZZI)).

6. The fraction of the total remanence (by vector difference sum), $f_{vds}$ ({cite:t}`tauxe2004`): While $f$ works well with single component magnetizations as in [](#fig:IZZI)d where it reflects the fraction of the total NRM used in the slope calculation, it can be misleading when there are multiple components of remanence as in [](#fig:IZZI)a. The values of $f$ for such specimens can be quite high, whereas the fraction of the total NRM is much less. We prefer to use a parameter $f_{vds}$ which is the fraction of the total NRM, estimated by the vector difference sum (VDS; Chapter 9) of the entire zero field demagnetization data. The VDS (see [](#fig:IZZI)a) "straightens out" the various components of the NRM by summing up the vector differences at each demagnetization step. $f_{vds}$ is calculated as:

   $$
   f_{vds} = \Delta y_T/ y_{vds},
   $$

   where $y_{vds}$ is the vector difference sum of the entire NRM (see [](#fig:IZZI)a and Chapter 9). This parameter becomes small, if the remanence is multi-component, whereas the original $f$ can be blind to multi-component remanences.

7. The Difference RATio Sum, DRATS: The difference between the original pTRM at a given temperature step (horizontal component of the circles in [](#fig:IZZI)) and the pTRM check (horizontal component of the triangles in see [](#fig:IZZI)), $\delta_i$ (see [](#fig:IZZI)a), can result from experimental noise or from alteration during the experiment. {cite:t}`selkin2000` normalized the maximum $\delta_i$ value within the region of interest by the length of the hypotenuse of the NRM/pTRM data used in the slope calculation. DRAT is therefore the maximum difference ratio expressed as a percentage. In many cases, it is useful to consider the trend of the pTRM checks as well as their maximum deviations. We follow {cite:t}`tauxe2004` who used the sum of these differences. We normalize this difference sum by the pTRM acquired by cooling from the maximum temperature step used in the slope calculation to room temperature. This parameter is called the Difference RATio Sum or DRATS. Only pTRM checks at temperatures below the maximum bound are included in the DRATS calculation.

8. Maximum Difference % MD%: The absolute value of the difference between the original NRM measured at a given temperature step (vertical component of the circles in [](#fig:IZZI)) and the second zero field step (known as the pTRM tail check) results from some of the pTRM imparted in the laboratory at $T_i$ having unblocking temperatures that are greater than $T_i$. These differences ($\Delta_i$; see [](#fig:IZZI)b) are plotted as squares. The Maximum Difference, normalized by the VDS of the NRM and expressed as a percentage is the parameter MD%.

9. Zig-Zag $Z$: In certain specimens, the IZZI protocol leads to rather interesting behavior, described in detail by {cite:t}`yu2004`. The solid symbols in [](#fig:IZZI) are the zerofield-infield (ZI) steps and the intervening steps are the infield-zerofield (IZ) steps (open circles). Alternating the two results in a "zigzag" in some specimens. The zigzag can be in either the Arai diagrams (compare slope of solid versus dashed line segments in [](#fig:IZZI)b) or in the orthogonal projections of the zero field vectors (compare directions of solid and dashed line segments in [](#fig:IZZI)c). We therefore can define a parameter $Z$ by testing the difference in either the two sets of slopes or the two sets of directions between the IZ steps and the ZI steps.

   To test the significance of the difference between the zero-field IZ directions and those from the ZI zero-field steps, we calculate F-test ($F_w$) for Watson's test for common mean ({cite:t}`watson1983`). The zigzag for directions $Z_{dir}$ is ratio $F_w/F_{(\nu,)}$ where $F_{(\nu)}$ is the critical value for $F$ at $\nu=2N-2$ degrees of freedom (at the 95% level of confidence).

   For the slopes, we calculate the mean and variance of the slopes for the IZ segments ($\bar b_{iz},\sigma_{iz}^2$) and the ZI segments ($\bar b_{zi},\sigma_{zi}^2$). The parameter $t_b$ is the $t$ test for the two means. The zigzag for the slopes $Z_{slope}$ is the ratio $t_b/t_{(\nu)}$ where $t_{(\nu)}$ is critical value for $t$ with $\nu= N_{iz}+N_{zi}-2$ degrees of freedom (from a statistics table).

   If the difference between the sets of directions and slopes is less than 2° or both $Z_{slope}$ and $Z_{dir}$ are less than unity, then $Z=0$. Otherwise $Z$ is the larger of $Z_{dir}$ and $Z_{slope}$.

10. The "gap factor" $g$ ({cite:t}`coe1978`) penalizes uneven distribution of data points and is:

    $$
    g= 1 - \bar \Delta \bar y/\Delta y_T,
    $$

    where $\bar \Delta \bar y$ is given by:

    $$
    \bar \Delta \bar y = { 1\over {\Delta y_T} } \sum_{i=1}^{i=N-1} \Delta y_i^2,
    $$

    and is the weighted mean of the gaps $\Delta y_i$ between the $N$ data points along the selected segment.

11. The Coe quality index $q$ combines the standard error of the slope, the NRM fraction and the gap factors by:

    $$
    q = \beta f g .
    $$

    As data spacing becomes less uniform, $g$ decreases.

12. A quick and dirty test for the possibility of anisotropy of TRM is to compare the direction of the pTRM acquired in the laboratory field with the direction of the applied field. The angle between these two at the maximum pTRM temperature used in the slope calculation is defined here as $\gamma$. If this exceeds more than a few degrees, it is advisable to perform some sort of test for TRM (or ARM) anisotropy.

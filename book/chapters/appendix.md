---
title: "Appendix A: Definitions, Derivations and Tricks"
label: app:definitions
authors:
  - name: Lisa Tauxe
    affiliation: Scripps Institution of Oceanography, UC San Diego
numbering:
  enumerator: A.%s
---

Paleomagnetism is famous for its use of a large number of incomprehensible acronyms. Here we have them gathered together along with definitions and the Section numbers where they are explained in more detail. You will find here a table of physical constants and paleomagnetic parameters used in the text as well as a table listing common statistics used in paleomagnetism. After the tables, there are a few sections with useful mathematical tricks.

## Definitions

:::{table} Acronyms in paleomagnetism.
:name: tab:acronyms

| Acronym | Definition: Section # |
|---------|----------------------|
| AMS | Anisotropy of magnetic susceptibility: [](#sect:chimeas) |
| APWP | Apparent polar wander path: [](#sect:apwp) |
| AF | Alternating field demagnetization: [](#sect:demag) |
| ARM | Anhysteretic remanent magnetization: [](#sect:arm) |
| ChRM | Characteristic remanent magnetization: [](#sect:chrm) |
| CNS | Cretaceous Normal Superchron: [](#sect:gpts) |
| CRM | Chemical remanent magnetization: [](#sect:crm) |
| DGRF | Definitive geomagnetic reference field: [](#sect:igrf) |
| DRM | Detrital remanent magnetization: [](#sect:drm) |
| E/I | Elongation/inclination correction method: [](#sect:tk03) |
| FC | Field cooled: [](#sect:delta) |
| GAD | Geocentric axial dipole: [](#sect:gad) |
| GHA | Greenwich hour angle: [](#app:sundec) |
| GPTS | Geomagnetic polarity time scale: Chapter 15 |
| GRM | Gyroremanent magnetization: [](#sect:arm) |
| IGRF | International geomagnetic reference field: [](#sect:igrf) |
| IZZI | Infield-zero field/ zero field-infield paleointensity protocol: [](#sect:KTT) |
| IRM | Isothermal remanent magnetization: [](#sect:uniaxial) and [](#sect:irm) |
| MD | Multidomain: Chapter 4 |
| MDF | Median destructive field: [](#sect:crittemp) |
| MDT | Median destructive temperature: [](#sect:crittemp) |
| NRM | Natural remanent magnetization: Chapter 7 |
| pARM | Partial anhysteretic remanence: [](#sect:arm) |
| pDRM | Post-depositional detrital remanent magnetization: [](#sect:drm) |
| PSD | Pseudo-single domain: Chapter 4 |
| PSV | Paleosecular variation of the geomagnetic field: [](#sect:historical) |
| pTRM | Partial thermal remanence: [](#sect:trm) |
| sIRM | Saturation IRM: See $M_r$ |
| SD | Single domain: Chapter 4 |
| SP | Superparamagnetic: [](#sect:tau) |
| SV | Secular variation: [](#sect:historical) |
| TRM | Thermal remanent magnetization: [](#sect:trm) |
| VADM | Virtual axial dipole moment: [](#sect:vdm) |
| VDM | Virtual dipole moment: [](#sect:vdm); [Equation %s](#eq:vdm) |
| VDS | Vector difference sum: [](#sect:vds) |
| VGP | Virtual geomagnetic pole: [](#sect:vgp) |
| VRM | Viscous remanent magnetization: [](#sect:vrm) |
| SQUID | Superconducting quantum interference device: [](#sect:meas) |
| UT | Universal time (Greenwich mean time): [](#app:sundec) |
| ZFC | Zero-field cooled: [](#sect:delta) |
:::

:::{table} Physical Parameters and Constants.
:name: tab:physconstants

| Symbol | Definition: Section # |
|--------|----------------------|
| $\chi$ | Magnetic susceptibility: The slope relating induced magnetization to an applied field: [](#sect:mag) |
| $\chi_{ARM}$ | ARM susceptibility: [](#sect:trends) |
| $\chi_b$ | Bulk magnetic susceptibility: [](#sect:mag); [Equation %s](#eq:chi) |
| $\chi_d$ | Diamagnetic susceptibility: [](#sect:dia) |
| $\chi_f$ | Ferromagnetic susceptibility: [](#sect:ferro) |
| $\chi_{fd}$ | Frequency dependent: [](#sect:chifd) |
| $\chi_h$ | High-frequency susceptibility: [](#sect:rosenbaum) |
| $\chi_{hf}$ | High-field susceptibility: [](#sect:chi) |
| $\chi_{i}$ | Initial susceptibility: [](#sect:chi) |
| $\chi_l$ | Low-frequency susceptibility: [](#sect:rosenbaum) |
| $\chi_p$ | Paramagnetic susceptibility: [](#sect:para) |
| $\delta_{FC}$ | Verwey transition temperature jump while cooling in a field: [](#sect:delta) |
| $\delta_{ZFC}$ | Verwey transition temperature jump while cooling in zero field: [](#sect:delta) |
| $\Delta M$ curve | Curve defined by subtracting the ascending from the descending curves in a hysteresis loop: [](#sect:uniaxial) |
| $\lambda,\phi$ | Latitude, Longitude |
| $\mu_o$ | Permeability of free space: (4$\pi$ x 10$^{-7}$ Hm$^{-1}$): [](#sect:BvH) |
| $\tau$ | Relaxation time: [](#sect:tau); [Equation %s](#eq:tau) |
| $\theta_m$ | Magnetic co-latitude: [](#sect:eqarea); [Equation %s](#eq:mcolat) |
| $\theta$ | Co-latitude: [](#sect:potential) |
| $a_{ij}$ | Direction cosines: [](#app:dircosines) |
| $[a_m]$ | Magnetic activity: [](#sect:drmint) |
| $a$ | The radius of the Earth (6.371 x 10$^6$ m): [](#sect:igrf) |
| $\mathbf{B}$ | Magnetic induction: [](#sect:flux) |
| $C$ | Frequency factor (10$^{10}$ s$^{-1}$): [](#sect:tau) |
| $D$ | Declination: [](#sect:comp); [Equation %s](#eq:DI) |
| $E$ | Elongation: [](#tab:params) |
| $I$ | Inclination: [](#sect:comp); [Equation %s](#eq:DI) |
| $g_m^l, h_m^l$ | Gauss coefficients: [](#sect:igrf) |
| $\mathbf{H}$ | Magnetic field: [](#sect:H) |
| $H_{cr}$ | Coercivity of remanence; field required to reduce saturation IRM to zero: [](#sect:flipping) |
| $H_c$ | Coercivity; the magnetic field required to change the magnetic moment of a particle from one easy axis to another: [](#sect:flipping) |
| $k$ | Boltzmann's constant (1.381 x 10$^{-23}$ JK$^{-1}$): [](#sect:para) |
| $K_i$ | AMS measurement: [](#app:K15) |
| $K_u$ | Constant of uniaxial anisotropy energy: [](#sect:K1) and [](#sect:shape) |
| $\mathbf{m}$ | Magnetic moment: [](#sect:moment) |
| $\mu_b$ | Bohr magneton (9.27 x 10$^{-24}$ Am$^2$): [](#sect:atomic) |
| $\mathbf{M}$ | Magnetization: [](#sect:mag) |
| $M_{eq}$ | Equilibrium magnetization: [](#sect:vrm) |
| $M_r$ | Saturation remanence (also sIRM): [](#sect:uniaxial) |
| $M_s$ | Saturation magnetization; the magnetization measured in the presence of a saturating field: [](#sect:uniaxial) |
| $P_l^m$ | Schmidt polynomials: [](#sect:igrf) |
| $\mathbf{s}$ | Six elements of $\chi_{ij}$; $s_1=\chi_{11}, s_2=\chi_{22}, s_3=\chi_{33}, s_4=\chi_{12}, s_5=\chi_{23}, s_6=\chi_{13}$: [](#sect:chimeas); [Equation %s](#eq:kj) |
| $R_x$ | IRM cross-over value: [](#sect:interaction) |
| $T$ | Absolute temperature (in kelvin) |
| $T_b$ | Blocking temperature: [](#sect:trm) |
| $T_c$ | Curie (Néel) temperature: [](#sect:ferro), [](#sect:crittemp) |
| $T_h$ | Hopkinson Effect: [](#sect:crittemp) |
| $T_m$ | Morin transition: [](#sect:crittemp) |
| $T_o$ | Absolute zero: [](#sect:ferro) |
| $T_p$ | Pyrrhotite transition: [](#sect:crittemp) |
| $T_v$ | Verwey temperature: [](#sect:K1), [](#sect:crittemp) |
| $v$ | Volume |
| $v_b$ | Blocking volume: [](#sect:crm) |
:::

:::{table} Common statistics in paleomagnetism.
:name: tab:statistics

| Statistic | Definition: Section # |
|-----------|----------------------|
| $\alpha_{95}$ | Radius of circle (cone) of 95% confidence (Fisher): [](#sect:fisher), [Equation %s](#eq:a95) |
| $\delta$ | Residual errors for AMS measurements: [](#sect:chimeas), [Equation %s](#eq:kdel) |
| $\epsilon_{ij}$ | Semi-angles of Hext uncertainty ellipses: [](#sect:chimeas), [Equation %s](#eq:eij) |
| $\kappa$ | Fisher precision parameter: [](#sect:fisher), [Equation %s](#eq:fishdis) |
| $\eta_{95}, \zeta_{95}$ | Semi-angles of directional 95% uncertainty ellipses: [](#app:kent), [Equation %s](#eq:zeta) |
| $\boldsymbol{\tau}, \mathbf{V}$ | Eigenvalues and eigenvectors of tensors: [](#app:eigen), [Equation %s](#eq:eig) |
| $k$ | Estimate of $\kappa$: [](#sect:fisher), [Equation %s](#eq:k) |
| CSD | Circular standard deviation (Fisher): [](#sect:fisher), [Equation %s](#eq:csd) |
| $dm$ | Uncertainty in the meridian (longitude) of a paleomagnetic pole: [](#sect:fisher), [Equation %s](#eq:dpdm) |
| $dp$ | Uncertainty in the parallel (latitude) of a paleomagnetic pole: [](#sect:fisher), [Equation %s](#eq:dpdm) |
| $F, F_{12}, F_{23}$ | Significance tests for anisotropy (Hext): [](#sect:hextE), [Equation %s](#eq:fij) |
| MAD | Maximum angular deviation of principal eigenvector (Kirschvink): [](#sect:BFL), [Equation %s](#eq:mad) |
| MAD$_{plane}$ | MAD of the pole to a best-fit plane (Kirschvink): [](#sect:BFL), [Equation %s](#eq:madP) |
| $M_u, M_e$ | Significance tests for uniform and exponential distributions: [](#sect:fishtests), [](#app:qq), [Equation %s](#eq:Mu), and [Equation %s](#eq:Me) |
| $N$ | Number of samples, specimens or sites |
| $n_f$ | Number of degrees of freedom: [](#sect:hext), [Equation %s](#eq:So) |
| $R$ | Resultant vector length of unit vectors: [](#sect:fisher), [Equation %s](#eq:R) |
| $R_o$ | Critical value of $R$ for non-random distribution (Watson): [](#sect:Ro), [Equation %s](#eq:Ro) |
| $S_f$ | Scatter of VGPs - corrected for within site scatter: [Equation %s](#eq:Sf) |
| $S_p$ | Scatter of VGPs: [Equation %s](#eq:Sp) |
| $S_o$ | Residual sum of squares of errors (Hext): [](#sect:hext), [Equation %s](#eq:So) |
| $\mathbf{T}$ | Orientation tensor: [](#app:eigen), [Equation %s](#eq:tmatrix) |
:::

## Derivations

(app:langevin)=
### Langevin function for a paramagnetic substance

Here we derive the Langevin function for a paramagnetic substance with magnetic moments $m$ in an applied field $H$ at temperature $T$. If we make the assumption that there is no preferred alignment within the substance, we can assume that the number of moments ($n(\alpha)$) between angles $\alpha$ and $\alpha + d\alpha$ with respect to $\mathbf{H}$ is proportional to the solid angle $\sin\alpha d\alpha$ and the probability density function, i.e.

$$
n(\alpha) d\alpha \propto \exp \bigl({ -E_m\over {kT}} \bigr) \sin \alpha d\alpha,
$$ (eq:nalpha)

where $E_m$ is the magnetic energy. When we measure the induced magnetization, we really measure only the component of the moment parallel to the applied field, or $n(\alpha) m \cos\alpha$. The net induced magnetization $M_I$ of a population of particles with volume $v$ is therefore:

$$
M_I = {m\over v} \int_0^{\pi} n(\alpha)\cos \alpha d \alpha.
$$ (eq:MI)

By definition, $n(\alpha)$ integrates to $N$, the total number of moments, or

$$
N = \int_0^{\pi} n(\alpha)d\alpha.
$$ (eq:N)

The total saturation moment of a given population of $N$ individual magnetic moments $m$ is $Nm$. The saturation value of magnetization $M_s$ is thus $Nm$ normalized by the volume $v$. Therefore, the magnetization expressed as the fraction of saturation is:

$$
{M\over {M_s}} = { {\int_0^{\pi} n(\alpha ) \cos \alpha d\alpha}\over {\int_0^{\pi} n(\alpha )d\alpha }}
$$

$$
= { {\int_0^{\pi} e^{(m\mu_o H \cos \alpha )/kT}\cos \alpha \sin \alpha d\alpha}\over { \int_0^{\pi} e^{(m\mu_o H\cos \alpha )/kT}\sin \alpha d\alpha}}.
$$

By substituting $a=m\mu_oH/kT$ and $\cos \alpha =x$, we write

$$
{M\over {M_s}} = N { {\int_{-1}^{1} e^{a x}xdx} \over {\int_{-1}^1 e^{a x}dx} } = \bigl( { {e^{a} + e^{-a}} \over {e^{a} - e^{-a}} } - {1\over{a} } \bigr),
$$

and finally

$$
{M\over {M_s}} = [\text{coth } a - {1\over{a}}]=\mathcal{L} (a).
$$ (eq:Langapp)

(app:superparamagnetism)=
### Superparamagnetism

The derivation of superparamagnetism follows closely that of paramagnetism whereby the probability of finding a magnetization vector an angle $\alpha$ away from the direction of the applied field is given by:

$$
n(\alpha )d\alpha = 2\pi n_o e^{({{M_sBv\cos \alpha}\over {kT}})}\sin \alpha d\alpha.
$$ (eq:ccnalpha)

The total magnetization contributed by the $N$ moments is:

$$
{M\over {M_s}} = \int_0^{\pi} \cos \alpha n(\alpha )d\alpha.
$$ (eq:ccMint)

Combining [Equation %s](#eq:ccnalpha) and [Equation %s](#eq:ccMint) we get:

$$
{M\over {M_s}} = N { {\int_0^{\pi} n(\alpha ) \cos \alpha d\alpha}\over {\int_0^{\pi} n(\alpha )d\alpha }}
$$

$$
= N { {\int_0^{\pi} e^{(M_sBv\cos \alpha )/kT}\cos \alpha \sin \alpha d\alpha}\over { \int_0^{\pi} e^{(M_sBv\cos \alpha )/kT}\sin \alpha d\alpha}}.
$$

By substituting $a= M_sBv/kT$ and $\cos \alpha =x$, and remembering [Equation %s](#eq:Langapp), we can write:

$$
{M\over {M_s}} = N { {\int_1^{-1} e^{a x}xdx} \over {\int_1^{-1} e^{a x}dx} } = N\mathcal{L} (a).
$$

So finally

$$
{M\over {M_s}} = N\mathcal{L} (a).
$$

## Useful tricks

In this section, we have assembled assorted mathematical and plotting techniques that come in handy throughout this book.

(app:strig)=
### Spherical trigonometry

Spherical trigonometry has widespread applications throughout the book. It is used in the transformations of observed directions to virtual poles (Chapter 2) and transformation of coordinate systems, to name a few. Here we summarize the two most useful relationships: the *Law of Sines* and the *Law of Cosines*.

:::{figure} ../figures/appendix/strig.png
:name: fig:strig
:width: 80%

Rules of spherical trigonometry. $a,b,c$ are all great circle tracks on a sphere which form a triangle with apices $A,B,C$. The lengths of $a,b,c$ on a unit sphere are equal to the angles subtended by radii that intersect the globe at the apices, as shown in the inset. $\alpha,\beta,\gamma$ are the angles between the great circles.
:::

In [](#fig:strig), $\alpha, \beta$ and $\gamma$ are the angles between the great circles labelled $a$, $b$, and $c$. On a unit sphere, $a,b$ and $c$ are also the angles subtended by radii that intersect the globe at the apices A, B, and C (see inset on [](#fig:strig)). Two formulae from spherical trigonometry come in handy in paleomagnetism, the Law of Sines:

$$
{\sin \alpha \over \sin a}={\sin \beta \over \sin b}={\sin \gamma \over \sin c},
$$ (eq:lawsin)

and the Law of Cosines:

$$
\cos a = \cos b \cos c + \sin b \sin c \cos \alpha.
$$ (eq:lawcos)

(app:vectors)=
### Vector addition

:::{figure} ../figures/appendix/vectors.png
:name: fig:vectors
:width: 80%

Vectors $\mathbf{A}$ and $\mathbf{B}$, their components A$_{x,y}$, B$_{x,y}$ and the angles between them and the $X$ axis, $\alpha$ and $\beta$. The angle between the two vectors is $\alpha-\beta = \Delta$. Unit vectors in the directions of the axes are $\hat x$ and $\hat y$ respectively.
:::

To add the two vectors (see [](#fig:vectors)) $\mathbf{A}$ and $\mathbf{B}$, we break each vector into components $A_{x,y}$ and $B_{x,y}$. For example, $A_x=|A|\cos{\alpha}, A_y=|A|\sin{\alpha}$ where $|A|$ is the length of the vector $\mathbf{A}$. The components of the resultant vector $\mathbf{C}$ are: $C_x = A_x +B_x, C_y=A_y+B_y$. These can be converted back to polar coordinates of magnitude and angles if desired, whereby:

$$
|C| = \sqrt {C_x^2+C_y^2} \text{ and } \gamma= \cos^{-1} { {C_x}\over{ {|C|}}}.
$$

### Vector subtraction

To subtract two vectors, compute the components as in addition, but the components of the vector difference $\mathbf{C}$ are: $C_x = A_x -B_x, C_y=A_y-B_y$.

(app:vecmult)=
### Vector multiplication

There are two ways to multiply vectors. The first is the dot product whereby $\mathbf{A} \cdot \mathbf{B}= A_xB_x + A_yB_y$. This is a scalar and is actually the cosine of the angle between the two vectors if the $\mathbf{A}$ and $\mathbf{B}$ are taken as unit vectors (assume a magnitude of unity in the component calculation).

:::{figure} ../figures/appendix/cross.png
:name: fig:cross
:width: 60%

Illustration of cross product of vectors $A$ and $B$ separated by angle $\theta$ to get the orthogonal vector $C$.
:::

The other way to perform vector multiplication is the cross product (see [](#fig:cross)), which produces a vector orthogonal to both $\mathbf{A}$ and $\mathbf{B}$ and whose components are given by:

$$
C = \det \begin{vmatrix}
\hat x & \hat y & \hat z \\
A_x & A_y & A_z \\
B_x & B_y & B_z
\end{vmatrix}.
$$

To calculate the determinant, we follow these rules:

$$
C_x=A_yB_z - A_zB_y, \quad C_y=A_zB_x - A_xB_z, \quad C_z=A_xB_y - A_yB_x.
$$

or

$$
C_i = A_jB_k-A_kB_j \quad i\neq j \neq k.
$$

(app:tensors)=
### Tricks with tensors

Vectors belong to a more general concept called tensors. While a vector describes a magnitude of something in a given direction, tensors allow calculation of magnitudes as a function of orientation. Velocity is a vector relating speed to direction, but speed may change depending on direction, so we might need a tensor to calculate speed as a function of direction. Many properties in Earth science require tensors, like the indicatrix in mineralogy which relates the speed of light to crystallographic direction, or the relationship between stress and strain. Tensors in paleomagnetism are used, for example, to transform coordinate systems and to characterize the anisotropy of magnetic properties such as susceptibility. We will cover transformation of coordinate systems in the following.

(app:dircosines)=
#### Direction cosines

We use direction cosines in paleomagnetism in a variety of applications, from mineralogy to transformation from specimen to geographic or stratigraphic coordinate systems. Direction cosines are the cosines of the angles between different axes in given coordinate systems, here $X$ and $X'$ respectively (see, e.g., [](#fig:transform)a). The direction cosine $a_{12}$ is the cosine of the angle between the $X_1$ and the $X'_2$, $\alpha_{12}$ axes. We can define four of these direction cosines to fully describe the relationship between the two coordinate systems:

$$
a_{11} = \cos \alpha_{11}, \quad a_{21} = \cos \alpha_{21},
$$
$$
a_{12} = \cos \alpha_{12}, \quad a_{22} = \cos \alpha_{22}.
$$

The first subscript always refers to the $X$ system and the second refers to the $X'$.

:::{figure} ../figures/appendix/dircosines.png
:name: fig:transform
:width: 100%

Definition of direction cosines in two dimensions. a) Definition of vector in one set of coordinates, $x_1, x_2$. b) Definition of angles relating $X$ axes to $X'$.
:::

(app:coord)=
#### Changing coordinate systems

One application of using direction cosines is the transformation of coordinates systems from one set ($X$) to a new set $X'$. To find new coordinates $x'_1, x'_2,..$ from the old ($x_1, x_2,...$), we have:

$$
x_1' = a_{11} x_1 + a_{12} x_2, \quad x_2' = a_{21} x_2 + a_{22} x_2.
$$

In three dimensions we have:

$$
x_1' = a_{11} x_1 + a_{12} x_2 + a_{13} x_3,
$$
$$
x_2' = a_{21} x_1 + a_{22} x_2 + a_{23} x_3,
$$
$$
x_3' = a_{31} x_1+ a_{32} x_2 + a_{33} x_3,
$$

which can also be written as:

$$
\begin{pmatrix}x'_1\\ x'_2\\ x'_3\end{pmatrix} =
\begin{pmatrix}
 a_{11}&a_{12}&a_{13}\\
 a_{21}&a_{22}&a_{23}\\
 a_{31}&a_{32}&a_{33}
\end{pmatrix}
\begin{pmatrix}x_1\\ x_2\\ x_3\end{pmatrix},
$$ (eq:matrot)

with a short cut notation as: $x'_i = a_{ij} x_j$. However we write this, it means that for each axis $i$, just sum through the $j$'s for all the dimensions. The matrix $a_{ij}$ is an example of a 3 x 3 tensor and equations of the form $A_i = B_{ij} C_j$ relating two vectors with a tensor will be used throughout the book. A more common notation is with bold-faced variables which indicate vectors or tensors, e.g., $\mathbf{A} = \mathbf{B} \cdot \mathbf{C}$.

:::{figure} ../figures/appendix/transform.png
:name: fig:trans
:width: 100%

a) Sample coordinate system. b) Trigonometric relations between two cartesian coordinate systems, $\mathbf{X}_i$ and $\mathbf{X}'_i$. $\lambda,\phi,\psi$ are all known and the angles between the various axes can be calculated using spherical trigonometry. For example, the angle $\alpha$ between $\mathbf{X}_1$ and $\mathbf{X}_1'$ forms one side of the triangle shown by dash-dot lines. Thus, $\cos \alpha = \cos \lambda \cos \phi + \sin \lambda \sin \phi \cos \psi$. [Figure from {cite:t}`tauxe1998`.]
:::

Now we would like to apply this to changing coordinate systems for a paleomagnetic specimen in the most general case. The specimen coordinate system is defined by a right-hand rule where the thumb ($\mathbf{X}_1$) is directed parallel to an arrow marked on the sample, the index finger ($\mathbf{X}_2$) is in the same plane but at right angles and clockwise to $\mathbf{X}_1$ and the middle finger ($\mathbf{X}_3$) is perpendicular to the other two ([](#fig:trans)a). The transformation of coordinates ($x_i$) from the $\mathbf{X}_i$ axes to the coordinates in the desired $\mathbf{X}'$ coordinate system requires the determination of the direction cosines as described in [](#app:dircosines). The various $a_{ij}$ can be calculated using spherical trigonometry as in [](#app:strig). For example, $a_{11}$ for the general case depicted in [](#fig:trans) is $\cos \alpha$, which is given by the Law of Cosines (see [](#app:strig)) by using appropriate values, or:

$$
\cos \alpha = \cos \lambda \cos \phi + \sin \lambda \sin \phi \cos \psi.
$$

The other $a_{ij}$ can be calculated in a similar manner. In the case of most coordinate system rotations used in paleomagnetism, $X_2$ is in the same plane as $X'_1$ and $X'_2$ (and is horizontal) so $\psi$ = 90°. This problem is much simpler. The directions cosines for the case where $\psi = 90^{\circ}$ are:

$$
a=\begin{pmatrix}
\cos \lambda \cos \phi & - \sin \phi & - \sin \lambda \cos \phi\\
\cos \lambda \sin \phi & \cos \phi & - \sin \lambda \sin \phi \\
\sin \lambda & 0& \cos \lambda
\end{pmatrix}.
$$ (eq:aij)

The new coordinates can be obtained from [Equation %s](#eq:matrot), as follows:

$$
x'_1 = a_{11}x_1 + a_{12}x_2 + a_{13}x_3
$$
$$
x'_2 = a_{21}x_1 + a_{22}x_2 + a_{23}x_3
$$
$$
x'_3 = a_{31}x_1 + a_{32}x_2 + a_{33}x_3.
$$ (eq:newx)

The declination and inclination can be calculated by inserting these values in the equations in Chapter 2.

(app:polerot)=
#### Method for rotating points on a globe using finite rotation poles

Given the coordinates of the point on the globe $P_p$ with latitude $\lambda_p$, longitude $\phi_p$ the finite rotation pole $P_f$ with latitude $\lambda_f$, longitude $\phi_f$, the way to transform coordinates is as follows (you should also review [](#app:coord)).

1. Convert the latitudes and longitudes to cartesian coordinates by:

$$
P_1=\cos\phi \cos \lambda, \quad P_2 = \sin \phi \cos \lambda, \quad P_3 = \sin \lambda
$$

where $P$ is the point of interest.

2. Set up the rotation matrix $R$ as:

$$
R_{11} = P_{f1}P_{f1}(1-\cos \Omega) + \cos \Omega
$$
$$
R_{12} = P_{f1}P_{f2}(1-\cos \Omega) - P_{f3} \sin \Omega
$$
$$
R_{13} = P_{f1}P_{f3}(1-\cos \Omega) + P_{f2}\sin \Omega
$$
$$
R_{21} = P_{f2}P_{f1}(1-\cos \Omega) + P_{f3}\sin \Omega
$$
$$
R_{22} = P_{f2}P_{f2}(1-\cos \Omega) + \cos \Omega
$$
$$
R_{23} = P_{f2}P_{f3}(1-\cos \Omega) - P_{f1}\sin \Omega
$$
$$
R_{31} = P_{f3}P_{f1}(1-\cos \Omega) - P_{f2} \sin \Omega
$$
$$
R_{32} = P_{f3}P_{f2}(1-\cos \Omega) + P_{f1}\sin \Omega
$$
$$
R_{33} = P_{f3}P_{f3}(1-\cos \Omega) + \cos \Omega
$$

3. The coordinates of the transformed pole ($P_t$) are:

$$
P_{t1} = R_{11} P_{p1} + R_{12}P_{p2}+R_{13}P_{p3}
$$
$$
P_{t2} = R_{21} P_{p1} + R_{22}P_{p2}+R_{23}P_{p3}
$$
$$
P_{t3} = R_{31} P_{p1} + R_{32}P_{p2}+R_{33}P_{p3}
$$

which can be converted back into latitude and longitude in the usual way (see Chapter 2).

(app:eigen)=
#### The orientation tensor and eigenvectors

The *orientation tensor* $\mathbf{T}$ {cite:p}`scheidegger1965` (also known as the matrix of sums of squares and products), is extremely useful in paleomagnetism. This is found as follows:

1. Convert the $D$, $I$, and $M$ for a set of data points (e.g., a sequence of demagnetization data, or a set of geomagnetic vectors or unit vectors where $M=1$) to corresponding $x_i$ values (see Chapter 2).

2. Calculate the coordinates of the "center of mass" ($\bar x$) of the data points:

$$
\bar x_1 = {1\over N} (\sum_{1}^{N} x_{1i}); \quad \bar x_2 = {1\over N} (\sum_{1}^{N} x_{2i}); \quad \bar x_3 = {1\over N} (\sum_{1}^{N} x_{3i}),
$$ (eq:cm)

where $N$ is the number of data points involved. Note that for unit vectors, the center of mass is the same as the Fisher mean (Chapter 11).

3. Transform the origin of the data cluster to the center of mass:

$$
x_{1i}'=x_{1i}-\bar x_1; \quad x_{2i}'=x_{2i}-\bar x_2; \quad x_{3i}'=x_{3i}-\bar x_3,
$$ (eq:xp)

where $x'_i$ are the transformed coordinates.

4. The orientation matrix is defined as:

$$
\mathbf{T}=\begin{pmatrix}\sum x'_{1i}x'_{1i}&\sum x'_{1i}x'_{2i}&\sum x'_{1i}x'_{3i}\\
                \sum x'_{2i}x'_{1i}&\sum x'_{2i}x'_{2i}&\sum x'_{2i}x'_{3i}\\
                 \sum x'_{3i}x'_{1i}&\sum x'_{3i}x'_{2i}&\sum x'_{3i}x'_{3i}\end{pmatrix}.
$$ (eq:tmatrix)

$\mathbf{T}$ is a 3 x 3 matrix, where only six of the nine elements are independent. It is constructed in some coordinate system, such as the geographic or sample coordinate system. Usually, none of the six independent elements are zero. There exists, however, a coordinate system along which the "off-axis" terms are zero and the axes of this coordinate system are called the *eigenvectors* of the matrix. The three elements of $\mathbf{T}$ in the eigenvector coordinate system are called *eigenvalues*. In terms of linear algebra, this idea can be expressed as:

$$
\mathbf{T} \mathbf{V} = \boldsymbol{\tau} \mathbf{V},
$$ (eq:eig)

where $\mathbf{V}$ is the matrix containing three *eigenvectors* and $\boldsymbol{\tau}$ is the diagonal matrix containing three *eigenvalues*. [Equation %s](#eq:eig) is only true if:

$$
\text{det} | \mathbf{T} - \boldsymbol{\tau} | = 0.
$$ (eq:det)

If we expand [Equation %s](#eq:det), we have a third degree polynomial whose roots ($\tau$) are the eigenvalues:

$$
(T_{11}-\tau)[(T_{22}-\tau)(T_{33}-\tau) - T_{23}^2] -
$$
$$
T_{12}[T_{12}(T_{33}-\tau) - T_{13}T_{23}] +
T_{13}[T_{13}T_{23}-T_{13}(T_{22}-\tau)] = 0.
$$

The three possible values of $\tau$ ($\tau_1, \tau_2, \tau_3$) can be found with iteration and determination. In practice, there are many programs for calculating $\boldsymbol{\tau}$. My personal favorite is the Numpy Module for Python (see many free websites, especially Scientific Python (SciPy) for hints). Please note that the conventions adopted here are to scale the $\tau$'s such that they sum to one; the largest eigenvalue is termed $\tau_1$ and corresponds to the eigenvector $\mathbf{V}_1$.

Inserting the values for the transformed components calculated in [Equation %s](#eq:xp) into $\mathbf{T}$ gives the covariance matrix for the demagnetization data. The direction of the axis associated with the greatest scatter in the data (the principal eigenvector $\mathbf{V}_1$) corresponds to a best-fit line through the data. This is usually taken to be the direction of the component in question. This direction also corresponds to the axis around which the "moment of inertia" is least. The eigenvalues of $\mathbf{T}$ are the variances associated with each eigenvector. Thus the standard deviations are $\sigma_i=\sqrt{\tau_i}$.

(app:nabla)=
### Upside down triangles, $\nabla$

#### Gradient

We often wish to differentiate a function along three orthogonal axes. For example, imagine we know the topography of a ski area (see [](#fig:ski)). For every location (in say, $X$ and $Y$ coordinates), we know the height above sea level. This is a scalar function. Now imagine we want to build a ski resort, so we need to know the direction of steepest descent and the slope (red arrows in [](#fig:ski)).

:::{figure} ../figures/appendix/ski.png
:name: fig:ski
:width: 100%

Illustration of the relationship between a vector field (direction and magnitude of steepest slope at every point, e.g., red arrows) and the scalar field (height) of a ski slope.
:::

To convert the scalar field (height versus position) to a vector field (direction and magnitude of greatest slope) mathematically, we would simply differentiate the topography function. Let's say we had a very weird two dimensional, sinusoidal topography such that $z=f(x)=\sin x$ with $z$ the height and $x$ is the distance from some marker. The slope in the $x$ direction ($\hat x$), then would be $\hat x {d \over {d x}}{ f(x) }$. If $f(x,y,z)$ were a three dimensional topography then the gradient of the topography function would be:

$$
(\hat x {{\partial} \over {\partial x}} f + \hat y {{\partial} \over {\partial y}} f + \hat z {{\partial} \over {\partial z}} f) .
$$

For short hand, we define a "vector differential operator" to be a vector whose components are

$$
\nabla = (\hat x {\partial \over {\partial x}}, \hat y {\partial \over {\partial y}}, \hat z {\partial \over {\partial z}}).
$$

This can also be written in polar coordinates:

$$
\nabla = {\partial \over {\partial r}}, {\partial \over {r\partial \theta}}, {\partial \over {r\sin \theta \partial \phi}}.
$$

:::{figure} ../figures/appendix/div.png
:name: fig:div
:width: 80%

Example of a vector field with a non-zero divergence.
:::

#### Divergence

The divergence of a vector function (e.g. $\mathbf{H}$) is written as:

$$
\nabla \cdot \mathbf{H}.
$$

The trick here is to treat $\nabla$ as a vector and use the rules for dot products described in [](#app:vectors). In cartesian coordinates, this is:

$$
\nabla \cdot \mathbf{H} = \hat x {{\partial H_x} \over {\partial x}} + \hat y {{\partial H_y}\over {\partial y}} + \hat z {{\partial H_z}\over {\partial z}}.
$$

Like all dot products, the divergence of a vector function is a scalar.

:::{figure} ../figures/appendix/divzero.png
:name: fig:divzero
:width: 60%

Example of a vector field with zero divergence.
:::

:::{figure} ../figures/appendix/curl.png
:name: fig:curl
:width: 80%

Example of a vector field with non-zero curl.
:::

The name divergence is well chosen because $\nabla \cdot \mathbf{H}$ is a measure of how much the vector field "spreads out" (diverges) from the point in question. In fact, what divergence quantifies is the balance between vectors coming in to a particular region versus those that go out. The example in [](#fig:div) depicts a vector function whereby the magnitude of the vector increases linearly with distance away from the central point. An example of such a function would be $v(r)=r$. The divergence of this function is:

$$
\nabla \cdot v = {\partial \over {\partial r}} r = 1.
$$

(a scalar). There are no arrows returning in to the dashed box, only vectors going out and the non-zero divergence quantifies this net flux out of the box.

Now consider [](#fig:divzero), which depicts a vector function that is constant over space, i.e. $v(r) = k$. The divergence of this function is:

$$
\nabla \cdot v = {\partial \over {\partial r}} k = 0.
$$

The zero divergence means that for every vector leaving the box, there is an equal and opposite vector coming in. Put another way, no net flux results in a zero divergence. The fact that the divergence of the magnetic field is zero means that there are no point sources (monopoles), as opposed to electrical fields that have divergence related to the presence of electrons or protons.

#### Curl

The curl of the vector function $\mathbf{B}$ is defined as $\nabla \times \mathbf{B}$. In cartesian coordinates we have

$$
\nabla \times \mathbf{B} = \hat x ({\partial \over {\partial y}} B_z - {\partial \over {\partial z}} B_y) + \hat y ({\partial \over {\partial z}} B_x - {\partial \over {\partial x}} B_z) + \hat z ({\partial \over {\partial x}} B_y - {\partial \over {\partial y}} B_x).
$$

Curl is a measure of how much the vector function "curls" around a given point. The function describing the velocity of water in a whirlpool has a significant curl, while that of a smoothly flowing stream does not.

Consider [](#fig:curl) which depicts a vector function $v=-y\hat x + x\hat y$. The curl of this function is:

$$
\nabla \times v = \det \begin{vmatrix}
\hat x & \hat y & \hat z \\
{\partial \over {\partial x}} & {\partial \over {\partial y}} & {\partial \over {\partial z}}\\
-y & x & 0
\end{vmatrix},
$$

or

$$
\hat x ( {\partial \over {\partial y}} 0 - {\partial \over {\partial z}} x ) +
\hat y ( {\partial \over {\partial x}} 0 - {\partial \over {\partial z}} (-y) ) +
\hat z ( {\partial \over {\partial x}} x - {\partial \over {\partial y}} (-y) ).
$$

$$
= 0 \hat x + 0 \hat y + 2\hat z
$$

So there is a positive curl in this function and the curl is a vector in the $\hat z$ direction.

The magnetic field has a non-zero curl in the presence of currents or changing electric fields. In free space, away from currents (lightning!!), the magnetic field has zero curl.

(app:bootstrap)=
### The statistical bootstrap

Sometimes things just are not normal. Statistically that is. When you can not assume that your data follow some known distribution, like the normal distribution, or the Fisher distribution, what do you do? In this section, we outline a technique called the bootstrap, which allows us to make statistical inferences when parametric assumptions fail. The reader should also refer to {cite:t}`efron1993` for a more complete discussion.

:::{figure} ../figures/appendix/bootstrap.png
:name: fig:bootstrap
:width: 100%

Bootstrapping applied to a normal distribution. a) 500 data points are drawn from a Gaussian distribution with mean of 10 and a standard deviation of 2. b) Q-Q plot of data in a). The 95% confidence interval for the mean is given by Gauss statistics as $\pm$ 0.17. 10,000 new (para) data sets are generated by randomly drawing $N$ data points from the original data set shown in a). c) A histogram of the means from all the para-data sets. 95% of the means fall within the interval 10.06$^{+0.16}_{-0.16}$, hence the bootstrap confidence interval is similar to that calculated with Gaussian statistics. [Figure from {cite:t}`tauxe1998`.]
:::

In [](#fig:bootstrap), we illustrate the essentials of the statistical bootstrap. We will develop the technique using data drawn from a normal distribution. First, we generate a synthetic data set by drawing 500 data points from a normal distribution with a mean $\bar x$ of 10 and a standard deviation $\sigma$ of 2. The synthetic data are plotted as a histogram in [](#fig:bootstrap)a. In [](#fig:bootstrap)b we plot the data as a Q-Q plot (see [](#app:qq)) against the $z_i$ expected for a normal distribution.

The data in [](#fig:bootstrap)a plot in a line on the Q-Q plot ([](#fig:bootstrap)b). The value for $D$ is 0.0306. Because $N=500$, the critical value of $D$, $D_c$ at the 95% confidence level is 0.0396. Happily, our normal distribution simulation program has produced a set of 500 numbers for which the null hypothesis of a normal distribution has not been rejected. The mean of the synthetic dataset is about 10 and the standard deviation is 1.9. The usual Gaussian statistics allow us to estimate a 95% confidence interval for the mean as $\pm 1.96 \sigma / \sqrt{N}$ or $\pm 0.17$.

:::{figure} ../figures/appendix/sundefs.png
:name: fig:sundefs
:width: 50%

Calculation of the azimuth of the shadow direction ($\beta'$) relative to true North, using a sun compass. L is the site location (at $\lambda_L,\phi_L$), S is the position on the Earth where the sun is directly overhead ($\lambda_S,\phi_S$). [Figure from {cite:t}`tauxe1998`.]
:::

In order to estimate a confidence interval for the mean using the bootstrap, we first randomly draw a list of $N$ data by selecting data points from the original data set. This list is called a *pseudo-sample* of the data. Some data points will be used more than once and others will not be used at all. We then calculate the mean of the pseudo-sample. We repeat the procedure of drawing pseudo-samples and calculating the mean many times (say 10,000 times). A histogram of the "bootstrapped" means is plotted in [](#fig:bootstrap)c. If these are sorted such that the first mean is the lowest and the last mean is the highest, the 95% of the means are between the 250$^{th}$ and the 9,750$^{th}$ mean. These therefore are the 95% confidence bounds because we are approximately 95% confident that the true mean lies between these limits. The 95% confidence interval calculated for the data in [](#fig:bootstrap) by bootstrap is about $\pm$ 0.16 which is nearly the same as that calculated the Gaussian way. However, the bootstrap required orders of magnitude more calculations than the Gaussian method, hence it is ill-advised to perform a bootstrap calculation when a parametric one will do. Nonetheless, if the data are not Gaussian, the bootstrap provides a means of calculating confidence intervals when there is no quick and easy way. Furthermore, with a modern computer, the time required to calculate the bootstrap illustrated in [](#fig:bootstrap) was virtually imperceptible.

(app:sundec)=
### Directions using a sun compass

In a sun compass problem, we have the direction of the sun's shadow and an angle between that and the desired direction ($\alpha$). The declination of the shadow itself is 180° from the direction toward the sun. In [](#fig:sundefs), the problem of calculating declination from sun compass information is set up as a spherical trigonometry problem, similar to those introduced in Chapter 2 and [](#app:strig). The declination of the shadow direction $\beta'$, is given by 180 - $\beta$. We also know the latitude of the sampling location L ($\lambda_L$). We need to calculate the latitude of S (the point on the Earth's surface where the sun is directly overhead), and the local hour angle $H$.

Knowing the time of observation (in Universal Time), the position of S ($\lambda_s = \delta,\phi_s$ in [](#fig:sundefs)) can be calculated with reasonable precision (to within 0.01°) for the period of time between 1950 and 2050 using the procedure recommended in the 1996 Astronomical Almanac:

1. First, calculate the Julian Day $J$. Then, calculate the fraction of the day in Universal Time $U$. Finally, calculate the parameter $d$ which is the number of days from J2000 by:

$$
d= J - 2451545 + U.
$$

2. The mean longitude of the sun ($\phi_s$), corrected for aberration, can be estimated in degrees by:

$$
\phi_s=280.461 + 0.9856474 d.
$$

3. The mean anomaly $g=357.528 + 0.9856003 d$ (in degrees).

4. Put $\phi_s$ and $g$ in the range 0 → 360°.

5. The longitude of the ecliptic is given by $\phi_E=\phi_s + 1.915 \sin g + 0.020 \sin 2g$ (in degrees).

6. The obliquity of the ecliptic is given by $\epsilon = 23.439 - 0.0000004 d$.

7. Calculate the right ascension ($A$) by:

$$
A = \phi_E - ft \sin 2\phi_E + (f/2) t^2 \sin 4 \phi_E,
$$

where $f=180/\pi$ and $t=$tan$^2\epsilon/2$.

8. The so-called "declination" of the sun ($\delta$ in [](#fig:sundefs) which should not be confused with the magnetic declination $D$), which we will use as the latitude $\lambda_s$, is given by:

$$
\delta = \sin^{-1}(\sin \epsilon \sin \phi_e).
$$

9. Finally, the equation of time in degrees is given by $E= 4(\phi_s-A)$.

We can now calculate the Greenwich Hour Angle $GHA$ from the Universal Time $U$ (in minutes) by $GHA = (U + E)/4 + 180$. The local hour angle ($H$ in [](#fig:sundefs)) is $GHA + \phi_L$. We calculate $\beta$ using the laws of spherical trigonometry (see [](#app:strig)). First we calculate $\theta$ by the Law of Cosines (remembering that the cosine of the colatitude equals the sine of the latitude):

$$
\cos \theta = \sin \lambda_L \sin \lambda_s + \cos \lambda_L \cos \lambda_s \cos H
$$

and finally using the Law of Sines:

$$
\sin \beta = (\cos \lambda_s \sin H)/\sin \theta.
$$

If $\lambda_s<\lambda_L$, then the required angle is the shadow direction $\beta'$, given by: $\beta' =180-\beta$. The azimuth of the desired direction is $\beta'$ plus the measured shadow angle $\alpha$.

---
title: "Chapter 8: Environmental Magnetism"
label: chap:mineralogy
authors:
  - name: Lisa Tauxe
    affiliation: Scripps Institution of Oceanography, UC San Diego
numbering:
  enumerator: 8.%s
---

**BACKGROUND:** read {cite}`maher1999`, chapter 1; {cite}`evans2003`, chapter 4.

There is a lively field within rock magnetism that exploits the dependence of rock magnetic parameters on concentration, grain size and mineralogy for gleaning information about past (and present) environments. Examples of applied rock magnetism (*environmental magnetism*) run from detection of industrial pollution to characterizing changes across major climatic events. In this chapter we will review the basic tool-kit used by environmental magnetists and illustrate various applications with examples.

Applied rock magnetism relies on imaging techniques and magnetic measurements. Images come from optical microscopes, magnetic force microscopes, scanning electron and transmission electron microscopes using magnetic separates, polished sections or thin sections. Magnetic measurements include magnetic susceptibility, magnetic remanence and hysteresis, all as a function of temperature. All of these measurements can also be done as a function of orientation, but orientation is not usually important in environmental applications; anisotropy of rock magnetic measurements will be the topic of a later chapter. A list of the most frequently used parameters is included in [Table %s](#tab:params).

(sect:images)=
## Images

Images of magnetic phases are used to shed light on the origin of the magnetic phases. Scanning electron microscope images of igneous ([Figure %s](#fig:images)a), detrital or aeolian ([Figure %s](#fig:images)b), authigenic ([Figure %s](#fig:images)c), biogenic (Chapter 6), anthropogenic ([Figure %s](#fig:images)d) and cosmic ([Figure %s](#fig:images)e) sources all have distinctive ear-marks, so actually looking at the particles in question can provide invaluable information.

:::{figure} ../figures/chapter8/images.png
:name: fig:images
:width: 100%

Images of various magnetic phases. a) 300 μm titanomagnetite grain of igneous origin showing high temperature exsolution lamellae [Photo from R. Reynolds in {cite}`maher1999`.]. b) Detrital and aeolian (titano)magnetites from Chinese Loess. [Photo from {cite}`maher1999`.] c) Hematite rosettes on a smectite surface. [Photo from {cite}`reynolds1985`.] d) Backscatter SEM image of fly-ash spherule. [Photo of J. Matzka, in {cite}`maher1999`.] The bright grains are iron rich particles embedded in a silicate matrix. e) Silicate spherule with dendrites of Fe-rich material of cosmic origin, showing characteristic pitting of the surface. [Photo from M. Hounslow in {cite}`maher1999`.]
:::

:::{table} Summary of environmental magnetic parameters.
:name: tab:params

| Parameter name | Symbol | Units | Section |
|----------------|--------|-------|---------|
| **Critical temperatures:** | | | |
| &emsp;median destructive temperature | MDT | °C or K | [%s](#sect:crittemp) |
| &emsp;Curie (Néel) Temperature | $T_c$ | °C or K | [%s](#sect:crittemp) |
| &emsp;Hopkinson Effect | $T_h$ | °C or K | [%s](#sect:crittemp) |
| &emsp;Verwey transition | $T_v$ | °C or K | Chapter 4 |
| &emsp;Morin transition | $T_m$ | °C or K | Chapter 6 |
| &emsp;Pyrrhotite transition | $T_p$ | °C or K | Chapter 6 |
| **Magnetic susceptibility:** | | | |
| &emsp;volume normalized | $\chi$ | dimensionless | Chapter 1 |
| &emsp;mass normalized | $\kappa$ | m³kg⁻¹ | Chapter 1 |
| &emsp;low field (initial) | $\chi_{lf}$ | | [%s](#sect:chi) |
| &emsp;high field | $\chi_{hf}$ | | [%s](#sect:hyst) |
| &emsp;frequency dependent | $\chi_{fd}$ | | [%s](#sect:chifd) |
| **Magnetization:** | | | |
| &emsp;volume normalized | $M$ | Am⁻¹ | Chapter 1 |
| &emsp;mass normalized | $\Omega$ | Am²kg⁻¹ | Chapter 1 |
| &emsp;saturation | $M_s$ | | Chapter 3 |
| &emsp;saturation remanence | $M_{r}$ or sIRM | | Chapter 5 |
| &emsp;isothermal remanence | IRM | | Chapter 7 |
| &emsp;anhysteretic remanence | ARM | | Chapter 7 |
| &emsp;partial anhysteretic remanence | pARM | | Chapter 7 |
| &emsp;ARM susceptibility | $\chi_{ARM}$ | dimensionless | [%s](#sect:ratios) |
| **Critical fields:** | | | |
| &emsp;Coercivity | $H_{c}$ or $\mu_oH_{c}$ | Am⁻¹ or T | Chapter 5 |
| &emsp;Coercivity of remanence | $H_{cr}$ or $\mu_oH_{cr}$ | Am⁻¹ or T | Chapter 5 |
| &emsp;median destructive field | MDF | Am⁻¹ or T | [%s](#sect:crittemp) |
| **Ratios:** | | | |
| &emsp;Squareness | $M_r/M_s$ | | Chapter 5 |
| | $H_{cr}/H_{c}$ | | [%s](#sect:day) |
| &emsp;S-ratio | IRM$_x$/$M_r$ | | [%s](#sect:ratios) |
| &emsp;HIRM | $M_r$ - IRM$_x$ | | [%s](#sect:ratios) |
| | $M_r$/$\chi$ | | [%s](#sect:ratios) |
| | $\chi_{ARM}/\chi$ | | [%s](#sect:ratios) |
| | ARM/$M_r$ | | [%s](#sect:ratios) |
| &emsp;Königsberger ratios | $Q_n, Q_t$ | dimensionless | [%s](#sect:ratios) |
| &emsp;δ-δ | $\delta_{FC}/\delta_{ZFC}$ | dimensionless | [%s](#sect:delta) |
| &emsp;IRM crossover | $R_{x}$ | dimensionless | [%s](#sect:crossover) |
:::

(sect:crittemp)=
## Critical Temperatures

In [Table %s](#tab:params) we list several *critical temperatures* useful for characterizing the magnetic mineralogy of specimens that are observed in magnetic systems. The Curie (and Néel) temperatures above which spontaneous magnetization ceases, the Verwey and Morin transitions in magnetite and hematite respectively and the pyrrhotite transition at which the magnetic anisotropy energies change character resulting in an observable effect in the magnetization were all encountered in previous chapters. However, there are several critical temperatures that are new, or require additional clarification. The so-called *Hopkinson effect* listed in [Table %s](#tab:params) is discussed in [Section %s](#sect:chiT) under magnetic susceptibility measurements. The *median destructive temperature* is simply the temperature at which 50% of the NRM is destroyed when a specimen is heated to that temperature and cooled in zero field. It is a measure of stability, only rarely used and only mentioned here for completeness. [An analogous parameter for stability against alternating fields is the *median destructive field* (MDF), which is the alternating field required to reduce a remanence to 50% of its initial value.]

Although we defined the Curie temperature in Chapter 3, we did not really describe how the measurements were made or how the temperature can be estimated. The principles are illustrated in [Figure %s](#fig:curiebalance). A specimen is placed near the pole pieces of a strong electromagnet. The field gradient will pull a magnetic specimen in. A pick-up coil counteracts this force with a restoring force of equal magnitude. The current required to keep the specimen stationary is proportional to the magnetization. A thermocouple monitors the temperature as the specimen heats in a water cooled oven. Both the output of the pickup coil and the thermocouple can be put into a computer to make a graph of saturation magnetization versus temperature an example of which is shown as the solid line in [Figure %s](#fig:curie1)a.

:::{figure} ../figures/chapter8/curiebalance.png
:name: fig:curiebalance
:width: 90%

a) Translation Curie balance in the Scripps Laboratory. b) Schematic drawing of the key elements of a) (top view).
:::

Estimating the Curie temperature is not as simple as it seems at first glance. {cite}`gromme1969` used the intersection point of the two tangents to the thermomagnetic curve that bounds the Curie temperature, as shown in the inset to [Figure %s](#fig:curie1)a. The *intersecting tangents method* is straightforward to do by hand, but is rather subjective and is difficult to automate. {cite}`moskowitz1981` applied a method based on statistical physics for extrapolating the ferromagnetic behavior expected from experimental data through the Curie temperature to determine the point at which the ferromagnetic contribution reaches zero.

:::{figure} ../figures/chapter8/curie1.png
:name: fig:curie1
:width: 100%

a) $M_s-T$ data for magnetite. Inset illustrates intersecting tangent method of Curie temperature estimation. b) Data from a) differentiated once. c) Data from a) differentiated twice. Peak shows temperature of maximum curvature, interpreted as the Curie temperature for this specimen.
:::

A third method for estimating Curie temperatures from thermomagnetic data, the *differential method* of {cite}`tauxe1998`, seeks the maximum curvature in the thermomagnetic curve. This method is shown in [Figure %s](#fig:curie1)b,c. First, we calculate the derivative ($dM/dT$) of the data in [Figure %s](#fig:curie1)a (see [Figure %s](#fig:curie1)b). Then, these data are differentiated once again to produce $d^2M/dT^2$ ([Figure %s](#fig:curie1)c). The maximum in the second derivative occurs at the point of maximum curvature in the thermomagnetic curve and is a reasonable estimate of the Curie temperature.

The principal drawback of the differential method of Curie temperature estimation is that noise in the data is greatly amplified by differentiation, which makes identification of the Curie temperature difficult. These drawbacks can often be overcome by smoothing the data either by calculating three or more point running means, or using some filter either by Fourier methods or in the temperature domain.

There are a host of other measurements of remanent magnetization as a function of temperature. These can contribute significantly to the discussion of degree of alteration, degree of particle interaction and grain size of the magnetic phases in a specimen. A complete discussion of these are beyond the scope of this chapter, but the student should be aware of the rich possibilities of low and high temperature measurements of remanence. For interesting examples, peruse the various issues of the IRM Quarterly at: [http://www.irm.umn.edu/IRM/quarterly.html](http://www.irm.umn.edu/IRM/quarterly.html).

(sect:chi)=
## Magnetic Susceptibility

We first encountered the concept of magnetic susceptibility in Chapter 1 and again in more detail in Chapters 3 and 5. We defined it as the ratio of the induced magnetization to an inducing magnetic field or $M_I/H$. Because everything in a rock or mineral separate contributes to the magnetic susceptibility, it can be a fertile source of information on the composition of the sample. [For the same reasons, it can also be somewhat nightmarish to interpret on its own.] It is quick and easy to measure both in the field and in the laboratory; hence, magnetic susceptibility is used in a variety of ways in applied rock magnetism, including lithologic correlation, magnetic fabric, magnetic grain size/domain state, mineralogy and so on.

:::{figure} ../figures/chapter8/kappa.png
:name: fig:kappa
:width: 90%

Measuring magnetic susceptibility. a) An alternating current applied in the coil on the right induces a current in the left-hand coil. This induces a magnetization in the specimen shown in b), which in turn offsets the current in the coil to the right. The offset is proportional to the magnetic susceptibility of the specimen. [Modified from Genevieve Tauxe animation.]
:::

It is worth thinking briefly about what controls magnetic susceptibility and what the data might mean. At an atomic level, magnetic susceptibility results from the response of electronic orbits and/or unpaired spins to an applied field (Chapter 3). The diamagnetic response (orbits) is extremely weak and unless a specimen, e.g., from some ocean sediments, is nearly pure carbonate or quartz, it can be neglected. The paramagnetic response of, say, biotite, is much stronger, but if there is any appreciable ferromagnetic material in the specimen, the response will be dominated by that. In highly magnetic minerals such as magnetite, the susceptibility is dominated by the shape anisotropy. For a uniformly magnetized particle (e.g., small SD magnetite), the maximum susceptibility is at a high angle to the easy axis, because the moments are already at saturation along the easy direction. So we have the somewhat paradoxical result that uniformly magnetized particles have maximum susceptibilities along the short axis of elongate grains. For vortex remanent state, or multi-domain particles and perhaps for strongly flowered grains, this would not be the case and the maximum susceptibility is along the particle length. Another perhaps non-intuitive behavior is for superparamagnetic particles whose response is quite large. We learned in Chapter 7 that it can be as much as 27 times larger than a single domain particle of the same size! Chains of particles may also have magnetic responses arising from inter-particle interaction. Therefore, although magnetic susceptibility is quick to measure, its interpretation may not be straight-forward.

### Measurement of Magnetic Susceptibility

Many laboratories use equipment that works on the principle illustrated in [Figure %s](#fig:kappa) whereby an alternating current is driven through the coil on the right inducing a current in the coil on the left. This alternating current generates a small alternating field (generally less than 1 mT) along the axis of the coil. When a specimen is placed in the coil ([Figure %s](#fig:kappa)b), the alternating current induces an alternating magnetic field in the specimen. This causes an offset in the alternating current in the coil on the right which is proportional to the induced magnetization. After calibration, this offset can then be cast in terms of magnetic susceptibility. If the specimen is placed in the solenoid in different orientations the anisotropy of the magnetic susceptibility can be determined, a topic which we defer to Chapter 13.

:::{figure} ../figures/chapter8/chiT.png
:name: fig:chiT
:width: 100%

a) Schematic drawings of paramagnetic (solid line) and diamagnetic (dashed line) magnetic susceptibility as a function of temperature. b) Behavior of ferromagnetic susceptibility (solid line) as the material approaches its Curie temperature ($M_s-T$ data shown as dashed line).
:::

(sect:chiT)=
### Temperature Dependence

Susceptibility can be measured as a function of temperature by placing the specimen in a heating coil (see examples in [Figure %s](#fig:chiT)). We know from Chapter 3 that diamagnetism is negative and independent of temperature (dashed line in [Figure %s](#fig:chiT)a) and that paramagnetism is inversely proportional to temperature (solid line in [Figure %s](#fig:chiT)a). There is a difference of a factor of $\ln(C\tau)$ or about 27 between the superparamagnetic and the stable single domain magnetic susceptibility for a given grain. This means that as the blocking temperatures of the magnetic grains in a particular specimen are reached, the susceptibility of the grain will increase by this factor until the Curie temperature is reached, at which point only paramagnetic susceptibility is exhibited and the susceptibility will drop inversely with temperature (solid line in [Figure %s](#fig:chiT)b). An SP peak in susceptibility below the Curie temperature could explain the so-called *Hopkinson effect* which is a peak in magnetic susceptibility associated with the Curie temperature. The Hopkinson effect is frequently used to approximate Curie temperatures but may actually be related to unblocking in some specimens.

:::{figure} ../figures/chapter8/chifd.png
:name: fig:chifd
:width: 100%

a) Magnetic susceptibility as a function of frequency. The decrease in frequency dependence of susceptibility with increasing frequency is caused by the superparamagnetic particles in the specimen. b) Plot showing temperature and frequency dependence of the same specimen as in a). [Data from Tiva Canyon Tuff, {cite}`carterstiglitz2006`.]
:::

(sect:chifd)=
### Frequency Dependence

Susceptibility can also be measured as a function frequency of the applied oscillating field. Superparamagnetic behavior depends on the time scale of observation (the choice of $\tau$) so grains may behave superparamagnetically at one frequency, but not at another. Frequency dependent susceptibility $\chi_{fd}$ can therefore be used to constrain grain size/domain state of magnetic materials. We illustrate this effect in [Figure %s](#fig:chifd) which shows data gathered at the Institute for Rock Magnetism (IRM) on samples of the Tiva Canyon Tuff which are well known for their superparamagnetic/single domain grain size range (e.g., {cite}`schlinger1991`).

In [Figure %s](#fig:chifd)a we show measurements made at room temperature. Because of the far greater magnetic susceptibility of superparamagnetic particles, $\chi$ drops with the loss of SP behavior. Magnetic grains that act superparamagnetically at 1 Hz, may behave as stable single domains at higher frequencies (remember that SP behavior depends on time scale of observation), hence the loss of magnetic susceptibility with increasing frequency in the Tiva Canyon Tuff specimens. While the magnetization drops with increasing frequency, it can rise with increasing temperature as described in [Section %s](#sect:chiT). This behavior is shown in [Figure %s](#fig:chifd)b.

:::{figure} ../figures/chapter8/chimap.png
:name: fig:chimap
:width: 85%

Map of magnetic susceptibility as a function of distance from the road. [Data from {cite}`hoffmann1999`; Figure of M. Knab.]
:::

### Outcrop Measurements

Although most laboratories make magnetic susceptibility measurements on small specimens, it is also possible to make measurements on core sections or even at the outcrop. The latter can be done with hand held susceptometers various shapes and sizes, depending on the application. We show a map made with a field device in [Figure %s](#fig:chimap). Magnetic susceptibility is enhanced where magnetite spheres produced in the combustion of petroleum products are present as pollutants in dust particles. Therefore, magnetic susceptibility can be used as a tracer of industrial pollution (see, e.g., {cite}`petrovsky2000`).

(sect:rmrm)=
## Magnetization

[Table %s](#tab:params) lists various magnetizations that are useful in applied rock magnetism. These were all introduced in previous chapters but several deserve additional discussion. We will discuss the hysteresis parameters, $M_r$ and $M_s$ together with their critical field counterparts $H_c$ and $H_{cr}$ in [Section %s](#sect:hyst). In this section we will flesh out our understanding of IRM with particular attention to its uses in applied rock magnetism.

:::{figure} ../figures/chapter8/crossover.png
:name: fig:crossover
:width: 100%

a) IRM acquisition (solid lines) versus progressive demagnetization of IRM with alternating fields (dashed lines) for two specimens. Circles are the Lambert plagioclase (non-interacting uniaxial single domain magnetite particles) and squares are chiton teeth (interacting magnetite particles). The field at which the demagnetization and acquisition curves cross (the cross-over point $R_x$) is sensitive to particle interaction. [Data of {cite}`cisowski1981`.] b) ARM acquisition as a function of DC bias field for two specimens with different concentrations of magnetite. The squares are for a low concentration of 2.6 × 10⁻⁴ volume percent magnetite while the circles are for a high concentration of 2.33 volume percent. [Data of {cite}`sugiura1979`.]
:::

(sect:interaction)=
### Magnetic Interactions: IRM and ARM Techniques

(sect:crossover)=
{cite}`cisowski1981` suggested that by comparing IRM acquisition curves like that shown in Chapter 7 with the curves obtained by progressively demagnetizing the sIRM in alternating fields, one might be able to detect the effect of particle interaction. He collected data from a specimen thought to be dominated by uniaxial single domain particles (the Lambert plagioclase) and from a specimen of chiton teeth, thought to be dominated by interacting particles of magnetite. The IRM acquisition data for the two specimens are shown as the solid lines in [Figure %s](#fig:crossover)a and the demagnetization of the saturation IRMs are shown as dashed lines. The field at which the demagnetization curve crosses the acquisition curve is called the crossover point, here designated $R_x$. This point should theoretically be reached when the IRM is half the saturation value for uniaxial single domain particles. The value of nearly 0.5 for the Lambert plagioclase ($R_{x(LP)}$ in [Figure %s](#fig:crossover)a) supports the claim of uniaxial single domain behavior for this specimen. The much depressed value of $R_{x(C)}\simeq$ 0.25 for the chiton teeth also supports the interpretation of significant inter-particle interaction for that specimen. Magnetic interactions are nowadays more frequently assessed using the FORC diagrams discussed in Chapter 5, but the cross-over technique has been used extensively in the past.

Another method for detecting magnetic interactions was developed by {cite}`sugiura1979`. He showed that the ARM acquired as a function of DC bias field ($B_{DC}$) is a strong function of magnetite concentration. We show examples of two ARM acquisition curves in [Figure %s](#fig:crossover)b, one with high magnetite concentration (2.33 volume percent, circles) and one with low magnetite concentration (2.5 × 10⁻⁴ volume percent, squares). The ARM acquisition curve for the low concentration is highly non-linear and achieves a substantially higher fraction of the saturation IRM as opposed to the curve for the high concentration, which is linear and much less efficient.

:::{figure} ../figures/chapter8/unmixing.png
:name: fig:unmixing
:width: 65%

Theoretical curve for the acquisition of IRM with two magnetic components with different coercivity spectra (see insert). The acquisition curve can be differentiated to get the heavy solid line in the insert and then decomposed into the different components assuming some distribution of coercivity (in this case log-normal). The main plot is a "linear acquisition plot" (LAP) and the heavy solid line in the inset is a "gradient of acquisition plot" (GAP) in the terminology of {cite}`kruiver2001`. $H_{1/2}$ and $DP$ are the fields required to magnetize half the population and the "dispersion parameter" of {cite}`robertson1994` respectively. Note that $H_{1/2}$ is a measure of $H_{cr}$ ($H'''_{cr}$ in Table C.1) if there is only one population of coercivities.
:::

(sect:unmixing)=
### IRM "Unmixing"

{cite}`robertson1994` suggested that if populations of magnetic materials have generally log-normally distributed coercivity spectra and if the IRM is the linear sum of all the contributing grains, then an IRM acquisition curve could be "unmixed" into the contributing components. The basic idea is illustrated in [Figure %s](#fig:unmixing) whereby two components each with log normally distributed coercivity spectra (see dashed and dashed-dotted lines in the inset) create the IRM acquisition curve shown. By obtaining a very well determined IRM acquisition plot (the "linear acquisition plot" or LAP in [Figure %s](#fig:unmixing) using the terminology of {cite}`kruiver2001`), one could first differentiate it to get the "gradient acquisition plot" or GAP (heavy solid line in the inset to [Figure %s](#fig:unmixing)). This then can be "unmixed" to get the parameters of the contributing components such as the mean and standard deviation of the log-normal distribution (called $B_{1/2}$ and $DP$ respectively by {cite}`robertson1994`). For consistency with prior usage in this book, we use the $\mu_oH$ and $H$ terminology for coercivity depending on unit choice. Note that $H_{1/2}$ is a measure of $H_{cr}$ if there is only one population of coercivities. Also, unmixing of other forms of magnetic remanence (e.g., ARM), demagnetization as well as acquisition, and other distributions are also possible as are more complex methods of inversion (see e.g., {cite}`egli2003`).

### Combining Thermal and Isothermal Information for Rock Magnetic Characterization

Another very useful technique for characterizing the magnetic mineralogy in a sample is the *3D IRM unblocking technique* of {cite}`lowrie1990`. Some important magnetic phases in geological materials (see Chapter 6) are magnetite (maximum blocking temperature of ~580°C, maximum coercivity of about 0.3 T), hematite (maximum blocking temperature of ~675°C and maximum coercivity larger than several tesla), goethite (maximum blocking temperature of ~125°C and maximum coercivity of much larger than 5 T), and various sulfides. The relative importance of these minerals in bulk samples can be constrained by a simple trick that exploits both differences in coercivity and unblocking temperature ({cite}`lowrie1990`).

This technique anticipates somewhat the chapter on demagnetization techniques. It also should remind you of Problem 2 in Chapter 6. In order to partially demagnetize a fraction of the magnetic remanence, a specimen is heated to a given temperature $T_i$ at which all those grains whose blocking temperatures have been exceeded are by definition superparamagnetic. If the heating is done in zero applied field, the net magnetization of those grains will average to zero (because the SP particles are in equilibrium with a null field). Therefore, the contribution of those grains with a blocking temperature of $T_i$ will be erased.

:::{figure} ../figures/chapter8/3dirm.png
:name: fig:3dirm
:width: 70%

a) Acquisition of IRM ($M_r$). After applying a field of 2 T, the specimen was subjected to two additional IRMs: 0.4 T and 0.12 T along orthogonal axes. b) Thermal demagnetization of a 3-axis IRM. Each component is plotted separately. [Figure from {cite}`tauxe1998`.]
:::

The "3D IRM" technique of {cite}`lowrie1990` proceeds as follows:

1. Apply an IRM along three orthogonal directions in three different fields. The first field, applied along $\X_1$, should be sufficient to saturate all the minerals within the specimen and is usually the largest field achievable in the laboratory (say 2 T). The second field, applied along $\X_2$, should be sufficient to saturate magnetite, but not to realign high coercivity phases, such as goethite or fine-grained hematite (say 0.4 T). The third IRM, applied along $\X_3$, should target low coercivity minerals and the field chosen is typically something like 0.12 T.

2. The composite magnetization can be characterized by determining the blocking temperature spectra for each component. This is done by heating the specimen in zero field to successively larger temperatures, cooling then measuring the remaining magnetization. The magnitude of the three cartesian components ($x_1, x_2, x_3$) of the remaining remanence is then plotted versus demagnetizing temperature.

An example of 3D IRM data are shown in [Figure %s](#fig:3dirm). The curve is dominated by a mineral with a maximum blocking temperature of between 550° and 600°C and has a coercivity less than 0.12 T. These properties are typical of magnetite (see Chapter 6). There is a small fraction of a high coercivity (>0.4 T) mineral with a maximum unblocking temperature > 650°C, which is consistent with the presence of hematite (see Chapter 6).

(sect:hyst)=
## Hysteresis Parameters

IRM and ARM acquisition and demagnetization curves can be a fecund source of information about the magnetic phases in rocks. However, these are extremely time consuming to measure taking hours for each one. Hysteresis loops on the other hand are quick, taking about 10 minutes to measure the outer loop. In principle, some of the same information could be obtained from hysteresis loops as from the IRM acquisition curves. [For computational details, see Appendix C.]

### The Building Blocks of Hysteresis Loops

Hysteresis loops, like IRM acquisition curves are the sum of all the contributing particles in the specimen. There are several basic types of loops which are recognized as the "building blocks" of the hysteresis loops we measure on geological materials. We illustrate some of the building blocks of possible hysteresis loops in [Figure %s](#fig:bblocks). [Figure %s](#fig:bblocks)a shows the negative slope typical of diamagnetic material such as carbonate or quartz, while [Figure %s](#fig:bblocks)b shows a paramagnetic slope. Such slopes are common when the specimen has little ferromagnetic material and is rich in iron-bearing phases such as biotite or clay minerals.

:::{figure} ../figures/chapter8/bblocks.png
:name: fig:bblocks
:width: 100%

Hysteresis loops of end-member behaviors: a) diamagnetic, b) paramagnetic, c) superparamagnetic (data for submarine basaltic glass), d) uniaxial, single domain, e) magnetocrystalline, single domain, f) "pseudo-single domain". Hysteresis behavior of various mixtures: g) magnetite, and hematite, h) SD/SP magnetite (data from {cite}`tauxe1996`), i) another example of SD/SP magnetite with a finer grained SP distribution. [Figures redrawn from {cite}`tauxe1998`.]
:::

When grain sizes are very small (~10 nm), a specimen can display superparamagnetic "hysteresis" behavior ([Figure %s](#fig:bblocks)c). The SP curve follows a Langevin function $L(\gamma)$ (see Chapter 5) where $\gamma$ is $M_svB/kT$, but integrates over the distribution of $v$ in the specimen.

Above some critical volume, grains will have relaxation times that are sufficient to retain a stable remanence (Chapter 7). Populations of randomly oriented stable grains can produce hysteresis loops with a variety of shapes (see Chapter 5), depending on the origin of magnetic anisotropy and domain state. We show loops from specimens that illustrate representative styles of hysteresis behavior in [Figure %s](#fig:bblocks)d-f. [Figure %s](#fig:bblocks)d shows a loop characteristic of specimens whose remanence stems from SD magnetite with uniaxial anisotropy. In [Figure %s](#fig:bblocks)e, we show data from specular hematite whose anisotropy ought to be magnetocrystalline in origin (hexagonal within the basal plane). Note the very high $M_r/M_s$ ratio of nearly one. Finally, we show a loop that has lower $M_r/M_s$ ratios than single domain, yet some stability. Loops of this type have been characterized as *pseudo-single domain* or PSD ([Figure %s](#fig:bblocks)f).

:::{figure} ../figures/chapter8/interp.png
:name: fig:interp
:width: 100%

a-d) Hysteresis curves, e-h: $\Delta M$ curves and i-l) $d\Delta M/dH$ curves. Columns from the left to right: hematite, SD magnetite, hematite plus magnetite, and SD plus SP magnetite. [Redrawn from {cite}`tauxe1998`.]
:::

### Hysteresis Behavior of Mixtures

In the messy reality of geological materials, we often encounter mixtures of several magnetic phases and/or domain states. Such mixtures can lead to distorted loops, such as those shown in [Figure %s](#fig:bblocks)g-i. In [Figure %s](#fig:bblocks)g, we show a mixture of hematite plus SD-magnetite. The loop is distorted in a manner that we refer to as *goose-necked*. Another commonly observed mixture is SD plus SP magnetite which can result in loops that are either *wasp-waisted* (see [Figure %s](#fig:bblocks)h) or *pot-bellied* (see [Figure %s](#fig:bblocks)i).

Considering the loops shown in [Figure %s](#fig:bblocks)g-i, we immediately notice that there are two distinct causes of loop distortion: mixing two phases with different coercivities and mixing SD and SP domain states. {cite}`tauxe1996` differentiated the two types of distortion as "goose-necked" and "wasp-waisted" (see [Figure %s](#fig:bblocks)g,h) because they look different and they mean different things.

{cite}`jackson1990` suggested that the $\Delta M$ curve (see Chapter 5) could be differentiated to reveal different coercivity spectra contained in the hysteresis loop. The $\Delta M$ curve and its derivative ($d\Delta M/dH$) are sensitive only to the remanence carrying phases, and not, for example, to the SP fraction. We can use these curves to distinguish the two sources of distortion. Hence, in [Figure %s](#fig:interp), we show several representative loops, along with the $\Delta M$ and $d\Delta M/dH$ curves. Distortion resulting from two phases with different coercivities (e.g., hematite plus magnetite or two distinct grain sizes of the same mineral) results in a "two humped" $d\Delta M/dH$ curve, whereas wasp-waisting which results from mixtures of SD + SP populations have only one "hump".

(sect:trends)=
## Trends in Parameters with Grain Size

One quest of applied rock magnetism is a diagnostic set of measurements that will yield unambiguous grain size information. To this end, large amounts of rock magnetic data have been collected on a variety of minerals that have been graded according to size and mode of formation. The most complete set of data are available for magnetite, as this is the most abundant crustal magnetic phase in the world. There are three sources for magnetite typically used in these experiments: natural crystals that have been crushed and sieved into grain size populations, crystals that were grown by a glass ceramic technique and crystals grown from hydrothermal solution. In [Figure %s](#fig:trends)a-c we show a compilation of grain size dependence of coercive force, remanence ratio, and coercivity of remanence respectively. There is a profound dependence not only on grain size, but on mode of formation as well. Crushed particles tend to have much higher coercivities and remanence ratios than grown crystals, presumably because of the increased dislocation density which stabilizes domain walls due to a minimum in interaction energy between internal stress and magnetostriction constants of the mineral. These abnormally high values disappear to a large extent when the particles are annealed at high temperature -- a procedure which allows the dislocations to "relax" away (see, e.g., {cite}`dunlop1997`). The behavior of low-field magnetic susceptibility is shown in [Figure %s](#fig:trends)d. There is no strong trend with grain size over the entire range of grain sizes from single domain to multi-domain magnetite. However, as already mentioned, susceptibility is predicted to be sensitive to the SD/SP domain state transition.

:::{figure} ../figures/chapter8/trends.png
:name: fig:trends
:width: 90%

Grain size dependence in hysteresis parameters. Crushed grains (red) indicated by "C", glass ceramic grains (blue) indicated by GC; hydrothermal grains (green) indicated by "H". a) Variation of coercivity ($\mu_oH_c$). b) Variation of $M_r/M_s$. c) Variation of coercivity of remanence $\mu_oH_{cr}$. [Data compiled by {cite}`hunt1995`.] d) Variation of susceptibility with grain size. [Data compiled by {cite}`heider1996`.] e) Variation in $\chi_{ARM}$ with grain size. [Data compiled by {cite}`dunlop1997b`.]
:::

Grain size trends in ARM are shown in [Figure %s](#fig:trends)e. ARM has been converted to what is known as the "susceptibility of ARM" or $\chi_{ARM}$ (see Chapter 7). This is done by assuming that ARM is linearly related to the applied DC field and calculating the ratio of ARM (in for example, units of Am² to the DC field (usually 50-100μT). To do this, the DC field units must first be converted to units of $H$ by dividing by $\mu_o$ and the ARM must be a volume normalized remanence in units of $M$. Because $H$ and $M$ are both in units of Am⁻¹, $\chi_{ARM}$ is dimensionless. The trend in $\chi_{ARM}$ shown in [Figure %s](#fig:trends)e is very poorly constrained because ARM is also a strong function of concentration and the method by which the particles were prepared.

:::{figure} ../figures/chapter8/slag.png
:name: fig:slag
:width: 90%

Plots of hysteresis parameters from a collection of related specimens. a) Plot of $M_r/M_s$ versus $H_{cr}/H_c$. Inset shows typical loop from which the ratios were derived. b) Plot of $M_r/M_s$ versus $\mu_oH_c$. [Data from {cite}`benyosef2008`.]
:::

(sect:ratios)=
## Ratios

A bewildering array of parameter ratios are in popular use in the applied rock and mineral magnetism literature. The most commonly used ratios are listed in [Table %s](#tab:params). Most of these are new to us in this chapter and deserve some discussion. Two of the most popular ratios are the hysteresis ratios $M_r/M_s$ and $H_{cr}/H_c$. These are sensitive to remanence state (SP, SD, flower, vortex, MD) and the source of magnetic anisotropy (cubic, uniaxial, defects), hence reveal something about grain size and shape. Both of these ratios can be estimated from a typical hysteresis experiment (Chapter 5) and the results of many such experiments can be compiled onto a single diagram as in [Figure %s](#fig:slag).

(sect:day)=
[Figure %s](#fig:slag)a is known as the *Day diagram* ({cite}`day1977`; see [Section %s](#sect:mixtures) in Chapter 5). Day diagrams are divided into regions of nominally SD, PSD and MD behavior using some theoretical bounds as guides. The designation PSD stands for *pseudo-single domain* and has $M_r/M_s$ ratios in between those characteristic of SD behavior (0.5 or higher) and MD (0.05 or lower). In practice nearly all geological materials plot in the PSD box which comprises the entire flower and vortex state range. The PSD designation should really be split into the truly pseudo-single domain behavior of the flower state and what would better be described as *pseudo-multi-domain* (PMD) behavior of the vortex state. Nonetheless, data such as those shown in [Figure %s](#fig:slag) are often interpreted in terms of grain size using the crushed data shown in [Figure %s](#fig:trends) as calibration. The problem arises however that the trends strongly depend on sample preparation and the absolute grain size interpretations are therefore usually wrong in the literature.

Part of the problem is that the hysteresis behavior of multi-domain assemblages is similar to that of superparamagnetic particles (Chapter 5) and more information (such as behavior as a function of temperature) is necessary for a correct interpretation. Moreover, by taking the ratio $H_{cr}/H_c$ we lose information. For this reason, {cite}`tauxe2002` argued for the much older practice of plotting $M_r/M_s$ versus $H_{cr}$ and $H_c$ separately ({cite}`neel1955`). This type of plot, known as the *squareness-coercivity diagram* is shown in [Figure %s](#fig:slag). The "F" and "V" designations for flower and vortex respectively were approximated by micromagnetic modelling ({cite}`tauxe2002`).

The S-ratio is the ratio of the IRM acquired in a back field of magnitude $x$ to the saturation IRM, $M_r$, (see [Table %s](#tab:params)). HIRM is not really a ratio, but is the difference between the saturation IRM remaining after application of a backfield of magnitude $x$ and the sIRM (the fraction of $M_r$ "harder" than field $x$). These parameters are frequently used in paleoceanographic and environmental applications because they are sensitive to changes in magnetic mineralogy.

A ratio of saturation IRM to magnetic susceptibility ($M_r/\chi$ in [Table %s](#tab:params)) of greater than 20 kAm⁻¹ can indicate the presence of minerals other than magnetite (e.g, sulfides). However, identification of exactly which minerals is a rather complicated affair (see {cite}`maher1999`).

Finally, based on data similar to those shown in [Figure %s](#fig:trends), {cite}`banerjee1981` argued that $\chi_{ARM}$ to $\chi$ can be used as a proxy for grain size changes in magnetite (see e.g., [Figure %s](#fig:banerjee)). {cite}`king1982` went further and suggested specific grain sizes for a given ratio, but these were based partly on crushed magnetites whose behavior differs substantially from most naturally occurring magnetite. Furthermore, as pointed out by {cite}`king1983`, $\chi_{ARM}$ is a strong function of concentration, so caution is warranted. Finally, the cgs units used in {cite}`king1982` have been translated into SI incorrectly in many applications (e.g., error in table in {cite}`king1983`). Nonetheless, what is clear from [Figure %s](#fig:trends) is that susceptibility (away from the SP grain sizes) is virtually independent of grain size while $\chi_{ARM}$ is a strong function of grain size, so changes in $\chi_{ARM}$ normalized by $\chi_{lf}$ should in fact reflect changes in grain size.

Three other ratios are listed in [Table %s](#tab:params), ARM/$M_r$, and the two Königsberger (1938) ratios $Q_n,Q_t$. {cite}`maher1999` suggest that the former be used to characterize particle interactions because particle interaction suppresses ARM acquisition, but not IRM acquisition. The first Königsberger ratio is the ratio of the induced magnetization to remanent magnetization in a given field, a parameter useful for interpreting the origin of magnetic anomalies (whether from the rock's remanent magnetization or induced by the Earth's field). The second is the ratio of the NRM (presumed to be thermal in origin) to a laboratory induced TRM. This ratio is nowadays interpreted in terms of changes in the strength of the ancient magnetic field (to be discussed in later chapters), but Königsberger himself believed the ratio to reflect the age of the rock. He envisioned a type of viscous decay of the remanence over time, so older rocks would have a lower value of $Q_t$ than younger ones, a trend that he observed in his own data spanning the last few hundred million years.

## Applications of Rock Magnetism

### Paleoclimatic Information from Lake Sediments

Although we have encountered numerous practical applications in this chapter already, there are many more. Rock magnetic parameters are relatively quick and easy to measure, compared to geochemical, sedimentological and paleontological data. When used judiciously, they can be enormously helpful in constraining a wide variety of climatic and environmental changes. There are three basic types of plots of the rock and mineral magnetic parameters discussed in this chapter: maps, bi-plots and depth plots.

:::{figure} ../figures/chapter8/banerjee.png
:name: fig:banerjee
:width: 50%

Plot of ARM versus magnetic susceptibility for a core from Minnesota. The different slopes are correlated with major climatic and anthropogenic events during the Holocene. [Redrawn from {cite}`banerjee1981`.]
:::

Because combustion related magnetic particles (see, e.g., fly ash particle in [Figure %s](#fig:images)d), the extent of anthropogenic pollution can be visualized by mapping magnetic susceptibility. Biplots, for example ARM versus $\chi$ have been in use since {cite}`banerjee1981` (see e.g., [Figure %s](#fig:banerjee)). They can be useful for detecting changes in grain size, concentration, mineralogy, etc. If, for example, the data in a plot of $M_r$ versus $\chi$ plot on a line, it may be appropriate to interpret the dominant control on the rock magnetic parameters as changes in concentration alone.

Depth plots are useful for core correlation, variations in concentration, mineralogy and grain size as a function of depth. An elegant example of the use of depth plots is the work of {cite}`rosenbaum1996`. [Figure %s](#fig:bucklake-1) shows depth variations of selected rock magnetic and major (Ti) and trace (Zr) element data along with the pollen zones in sediment cores taken from Buck Lake, Oregon. A simple (first order) interpretation of susceptibility would be that glacial (cold) and interglacial (warm) periods tapped different source areas in the drainage basin to deliver magnetite (higher susceptibility) and hematite (lower susceptibility) during different climatic periods. However, much more complexity emerges when (a) chemical analyses for concentration variation of certain key elements (Fe, Ti, Zr) and (b) petrographic observations of the magnetic fractions are considered.

:::{figure} ../figures/chapter8/rosenbaum-1.png
:name: fig:bucklake-1
:width: 100%

Rock magnetic and trace element data from Buck Lake [Data downloaded from http://pubs.usgs.gov/of/1995/of95-673/of95-673.html and interpreted as in {cite}`rosenbaum1996`].
:::

In [Figure %s](#fig:bucklake-2)a we observe that two elements, Ti and Zr, both derived from detrital heavy minerals are strongly correlated ($R^2$ = 0.82) and the regression line passing (nearly) through the origin confirms that neither element shows anomalous addition or subtraction. In [Figure %s](#fig:bucklake-2)b and [Figure %s](#fig:bucklake-2)c, Ti concentration is used as a measure of detrital input variations. [Figure %s](#fig:bucklake-2)b shows that there has been post-depositional loss (vertical distance between the dashed and solid lines) of Fe, which is evidence that fluctuations in either iron or the magnetic parameters with depth cannot be a simple reflection of changes in detrital material delivery.

:::{figure} ../figures/chapter8/rosenbaum-2.png
:name: fig:bucklake-2
:width: 80%

Biplots of various trace elements and rock magnetic parameters. Solid lines are best-fit lines. Dashed lines are theoretical lines with no Fe-loss. Open symbols were excluded from best-fit line. Note that many data are off the plot. a) Zr against Ti. b) Fe against Ti. c) HIRM (hematite component) against Ti (proxy for detrital input). d) $\chi$ (magnetite component) against Ti. [Figures re-drawn from {cite}`rosenbaum1996` using data in [Figure %s](#fig:bucklake-1).]
:::

In [Figure %s](#fig:bucklake-2)c and [Figure %s](#fig:bucklake-2)d, we get further information that hematite (proportional to HIRM) and magnetite (main contributor to susceptibility) both show negative intercepts when plotted against Ti. In both plots, HIRM and $\chi$ corresponding to the higher values of Ti are scattered, generally suggesting wide variations in detrital input, perhaps reflecting true changes in the types of detrital material delivered at different times.

But petrographic observations showed that the specimens with high scatter in HIRM (hematite) and $\chi$ (magnetite) contain fresh, relatively unweathered volcanic fragments with a wide variation of hematite and magnetite grains reflecting heterogeneity at source (volcano). Other samples of hematite and magnetite show pitting and evidence of wholesale mineral dissolution coinciding with offsets observed in HIRM and $\chi$. Taken together, the data from [Figure %s](#fig:bucklake-2) and petrographic evidence provide a more nuanced understanding of the past climate record at Buck Lake. Although the pollen data could mean variations in the temperature alone (glacial/interglacial), magnetic analyses and petrographic observations lead us to a further climatic/environmental clue: sections with wide scatter in susceptibility are heterogeneous and have large chunks of fresh, unaltered material. This was deposited during rapid high velocity water flows in the drainage basin. While the hydrologic conditions were much different (low rainfall and iron dissolution), then both HIRM and $\chi$ values are offset from the ideal dashed lines going through the origin at 45° to either axis. The lesson for us is that a multiparameter investigation enriches our understanding based on environmental magnetic data alone, and can provide additional information.

(sect:rosenbaum)=
### Paramagnetic Contributions to Magnetic Susceptibility

Earlier in this chapter, we showed an early example ({cite}`banerjee1981`) of the utility of ARM-$\chi$ plots for detecting environmental and anthropogenic changes in a lake sediment archive. {cite}`king1982` rationalized such plots with $\chi_{ARM}$ on the y-axis instead of ARM so that both axes are dimensionless. {cite}`yamazaki1997` used magnetic data from pelagic clay sediments to show that errors occur when the implicit assumption of identical sources contributing to x- and y-axis values breaks down. In their pelagic clay sediments, as much as 25% of the observed magnetic susceptibility ($\chi$) came from paramagnetic clays rather than iron oxides alone.

:::{figure} ../figures/chapter8/np21.png
:name: fig:yamazaki
:width: 100%

a) Frequency dependence of magnetic susceptibility ($\chi_{fd}$) versus age for NP21, a pelagic clay core. b) Low-frequency magnetic susceptibility ($\chi_{l}$) versus the difference between the low and high-frequency magnetic susceptibilities ($\chi_l-\chi_h$) for core NP21. The value at the intersection of a linear regression line with the $\chi_l$ axis is interpreted as the frequency-independent fraction. c) Ratio of ARM to $\chi$ versus age for the uncorrected (U: open symbols) and corrected (C: solid symbols) data using the paramagnetic fraction of the susceptibility for core NP21. [Data of {cite}`yamazaki1997`.]
:::

[Figure %s](#fig:yamazaki)a shows two sets of frequency dependence of susceptibility measurements ($\chi_{fd}$). In one (uncorrected) there is an increase from 10% to 12% with increasing age. This could be explained by a postulated increase in superparamagnetic (SP) particles at depth. Frequency dependence is calculated by:

$$
\chi_{fd} = \frac{\chi_{l} - \chi_{h}}{\chi_{l}} \cdot 100\%,
$$

where $\chi_{l}$ and $\chi_h$ are the low and high frequency magnetic susceptibilities. So the same frequency dependence would not result if $\chi_{l}$ had a frequency-independent contribution from paramagnetic clay. In [Figure %s](#fig:yamazaki)b, the "corrected" values of $\chi_{l}$ are gotten by subtracting the paramagnetic or "high-field" susceptibility contributions ($\chi_{hf}$) obtained from the high field part of hysteresis loops (Chapter 5). As [Figure %s](#fig:yamazaki)a shows, the apparent increase in frequency dependence then disappears.

A similar error would occur if uncorrected $\chi_{l}$ values are used to derive the ratio ARM/$\chi_{l}$, which is inversely proportional to particle size (see [Section %s](#sect:trends)). In [Figure %s](#fig:yamazaki)c where this ratio is plotted before and after high-field susceptibility correction, the slow variation between 1 and 2.8 Ma disappears, leaving a true increase in ARM/$\chi_{l}$ below 2.8 Ma and not at 1 Ma.

The parameters $\chi_{fd}$ (ultrafine or SP fraction) and ARM/$\chi_{l}$ (slightly larger single or pseudo-single domain fraction) are extensively used in paleoceanographic studies where contributions from paramagnetic clay can be substantial. For such ocean sediments, and some terrestrial sediments, a routine check for strong paramagnetism through high field susceptibility measurements is highly valuable.

:::{figure} ../figures/chapter8/jackson-1.png
:name: fig:jackson-1
:width: 85%

a) Calculated grain distribution for the mixture of two Tiva Canyon Tuff specimens with different mean grain sizes and aspect ratios (contour interval = f$_{max}$/10). b) Calculated back-field spectra. [Redrawn from Figure 18 in {cite}`jackson2006`.]
:::

### Separation of Two Superparamagnetic Particle Size Distributions

Particle sizes below 20-30 nm for magnetite are superparamagnetic at 300 K. Conventionally, parameters such as frequency dependence of susceptibility ($\chi_{fd}$) measure the relative amount of the SP particles and can distinguish them from thermally stable and larger single domain, pseudo-single domain and multidomain particles in a natural mixture, for example, loess/paleosol. However, we have recently seen that sometimes there is valuable information to be gleaned from identifiable mixtures of two modes of SP size distributions. In environmental magnetism studies, such mixtures may represent records of two diagenetic or chemical change events, or of two types distinguished by their origin: biogenic and inorganic.

Superparamagnetic or thermal relaxation time for magnetization of a uniaxial particle is defined by Néel's equation (see Chapter 7):

$$
\tau = \frac{1}{C} \exp\left( \frac{M_sv\mu_oH_{k}}{2kT}\right).
$$

The particle volume distribution $f(v)$ can be estimated if the distribution of microscopic coercivity, $f(H_{k})$, is independently known or its approximate form can be assumed. {cite}`jackson2006` have formulated a general method to determine the joint distribution $f(v, H_{k})$ when both thermally stable single domain (SD, at 300 K) and thermally unstable smaller particles (SP) are present in a mixture. The raw data for applying the method utilizes the low temperature dependence of back field demagnetization curves of isothermal remanent magnetizations acquired at different back fields at 300 K. To reduce the large amount of data thus acquired, {cite}`jackson2006` apply a "tomographic" reconstruction method that results in $f(v, H_{k})$. These are plotted on a *Néel diagram* as shown in [Figure %s](#fig:jackson-1)a for a laboratory-prepared SP + SSD mixture of titanomagnetites obtained from different heights in Tiva mountain volcanic tuff deposit ({cite}`schlinger1991`). Note that Néel diagrams (after {cite}`neel1949`) are similar to the $K-v$ diagrams of Chapter 7, but show volume against coercivity instead of the magnetic anisotropy constant. The modes of both size distributions are close to 10 nm and yet the size/coercivity clusters are easily discernible. Direct size variations from Transmission Electron Microscopy (TEM) ({cite}`schlinger1991`) confirm the thermal fluctuation tomographic distributions in [Figure %s](#fig:jackson-1)a. The advantage of the magnetic method over TEM determination lies in the speed of measurement and in deriving distributions that represent a much larger spread of sizes. Theoretical $dM/dH$ curves for the tomographic reconstruction underscore the distinction between the two grain size modes and are shown in [Figure %s](#fig:jackson-1)b.

:::{figure} ../figures/chapter8/jackson-2.png
:name: fig:jackson-2
:width: 100%

a) Reconstructed grain distribution (contour interval of fmax/10) and b) best fit back-field spectra for a paleosol specimen. The RMS misfit is <5%. [Redrawn from Figure 21 in {cite}`jackson2006`.]
:::

[Figure %s](#fig:jackson-2) shows another Néel diagram obtained this time for a natural paleosol specimen from the Chinese loess plateau where the derived, and much wider, volume (10-100 nm) and coercivities are consistent with continuous pedogenic particle formation over tens of thousands of years. As {cite}`jackson2006` point out, however, back field remanence demagnetization curves spread over ~30 discrete values of temperature from 300 down to 10 K can take 4-6 hours and much liquid helium expenditure.

(sect:delta)=
### Identification of Biogenic Magnetite in Natural Samples

Here we provide a "real life" example of recognition of magnetite produced by magnetotactic bacteria in coastal pond sediments. Magnetotactic bacteria produce chains of magnetic particles (see Chapter 6) whose magnetocrystalline easy axes appear to be aligned. {cite}`moskowitz1993b` developed a test to detect the presence of aligned chains of magnetite. As was described in Chapter 4, magnetite undergoes a transition from cubic to monoclinic crystal structure as it cools through a temperature near 100-110 K known as the Verwey transition temperature ($T_v$). This transition results in a loss of magnetization (see Chapter 4). This loss is quantified by:

$$
\delta = \frac{M_{rs}(80) - M_{rs}(150)}{M_{rs}(80)},
$$ (eq:delta)

where $M_{rs}$ is the saturation IRM remaining at 80 or 150 K while warming from ~20 K. Specimens with intact chains of magnetite (magnetosomes) that are cooled from room temperature in the presence of a saturating field behave differently on warming through the Verwey transition than those cooled in low fields. In other words, the $\delta$ for field-cooled specimens ($\delta_{FC}$) is larger than that for low (essentially zero) field cooled specimens $\delta_{ZFC}$. Extracted, and thus disturbed and disordered, magnetosomes and inorganic SD and MD magnetites do not show a difference between $\delta_{FC}$ and $\delta_{ZFC}$. {cite}`moskowitz1993b` explain this behavior by calling on intact magnetosomes to have [111] easy axes aligned along the length of the chain. This makes the entire chain act as a uniaxial particle. Near the Verwey transition is the isotropic point (see Chapter 4) at which the magnetocrystalline anisotropy constant ($K_1$) goes through zero and the easy axis changes orientation from the [111] direction above it to the [100] below the isotropic point. When intact magnetosomes are cooled through $T_v$ in zero field, the new easy axes are chosen at random from one of the three [100] directions. When they cool through $T_v$ in a strong magnetic field, the [100] direction most closely aligned with the direction of the applied field will be chosen, instead of a random choice. Therefore, the magnetization of these field cooled chains is not the sum of randomly selected [100] directions, but the sum of partially aligned [100] directions, hence the saturation remanence is enhanced relative to the random case. Warming back through $T_v$, the ZFC curve joins the FC curve because both are warmed in the absence of a field. Experimentally, the ratio of $\delta_{FC}/\delta_{ZFC}$ is about 2 for intact magnetosomes and nearly unity for extracted chains or inorganic magnetite. This is known as the *δ-δ test* for intact magnetosomes.

{cite}`moskowitz2008` applied the δ-δ test to sediments from a salt water pond to locate the oxic-anoxic interface. The presence of an oxic-anoxic interface (OAI) in lake waters and its environmental effects is usually discovered and studied using a combination of standard microbiological, geochemical and transmission electron microscopic techniques. Magnetic tests can be added to the tool-kit and have the advantages that 'bulk', i.e., unseparated material can be analyzed, they are highly sensitive, quick to make and are relatively inexpensive.

:::{figure} ../figures/chapter8/moskowitz08-1.png
:name: fig:moskowitz-1
:width: 100%

Low-temperature FC (dashed line) and ZFC (solid line) demagnetization curves for selected water depths corresponding to a) above the oxic-anoxic interface (OAI; 2.7 m), b) bottom of OAI (3.5 m), and c) below the OAI (4.0 m). [Redrawn from Figure 9 in {cite}`moskowitz2008`.]
:::

{cite}`moskowitz2008` studied the oxic-anoxic interface (OAI) in a salt water pond in Falmouth, Massachusetts. The OAI was between ~3.1 m and ~3.5 m below the sediment/water interface. Without knowing its exact location, water samples were collected from 2.5 m to 4.5 m depths and their solid contents filtered out for magnetic measurements. The immediate goal was to discover the presence of highest concentration of magnetite-producing magnetotactic bacteria that preferentially populate OAI. Magnetite (Fe₃O₄) has both ferric (Fe³⁺) and ferrous (Fe²⁺) ions in its structure (see Chapter 3). Thus it is less common either in the fully oxic zone above OAI or in the fully anoxic zone (because of the presence of the reducing compound H₂S) below OAI.

:::{figure} ../figures/chapter8/moskowitz08-2.png
:name: fig:moskowitz-2
:width: 45%

$\delta_{FC}/\delta_{ZFC}$ ratios as a function of water depth. Shaded zone is the location of the OAI based on chemical profiles. sr: short-rod shaped magnetotactic bacteria. Values of $\delta_{FC}/\delta_{ZFC} > 2.0$ are characteristic of MMB and MRP bacteria that have magnetite magnetosomes organized in chains. [Redrawn from Figure 10b in {cite}`moskowitz2008`.]
:::

[Figure %s](#fig:moskowitz-1)a, b and c show the magnetic data acquired by warming from ~15 K. sIRM is applied at this temperature to specimens initially cooled from 300 K using two different pre-treatments: the specimen is either cooled in zero field (ZFC), or it is cooled in a large applied field (FC). The thermal demagnetization curves of specimens from above OAI ([Figure %s](#fig:moskowitz-1)a at 2.7 m) and below OAI ([Figure %s](#fig:moskowitz-1)c at 4.0 m) appear to be very similar. Both could be interpreted to contain a weak signature of the presence of very small amounts of magnetite in the form of small drops in sIRM around 95 K. However, the specimen shown in [Figure %s](#fig:moskowitz-1)b from 3.5 m shows incontrovertible evidence for magnetite: the sharp drops in ZFC and FC sIRMs near the Verwey transition temperature.

As defined earlier in this section, the magnitudes of the drops in sIRM can be expressed as $\delta_{FC}$ and $\delta_{ZFC}$. [Figure %s](#fig:moskowitz-2) shows the depth variation of $\delta_{FC}/\delta_{ZFC}$ ratio which is known to be equal to 2.0 or higher for live bacteria with chains of magnetite magnetosomes inside (e.g., {cite}`moskowitz1993b`). As shown here, the ratio is 2.0 or higher for specimens within the chemically determined OAI (shaded zone). The symbol "sr" refers to short rod-shaped magnetite as discovered by electron microscopy. Taken together, the chemical and microscopic evidence help locate the extent of OAI, important for environmental condition study of this salt pond. But the $\delta_{FC}/\delta_{ZFC}$ ratio provides the same information, accurately and with speed, when the ratio rises above 2.0 in a given zone. The speed of analysis is crucial for environmental studies if one wants to survey the height variation of OAI at a dense network of points in the lake leading to information about organic productivity.

## Concluding Remarks

There are many other excellent examples of applications of rock magnetic data to solving thorny environmental problems. Papers range from the highly useful to the frankly lunatic. However, the field is alive and new imaginative and extremely clever applications are being published every month.

**SUPPLEMENTAL READINGS:** {cite}`verosub1995`.

## Problems

**Problem 1**

a) Use the function **ipmag.curie** to calculate the Curie temperature of the data contained in the two data files *curie_example.dat* and *curie_example2.dat* in the Chapter_8 directory of the data folder (see Preface instructions). This function is designed to run in a Jupyter notebook.

b) The way **ipmag.curie** works is to use a triangular sliding window and average over a range of temperature steps. Then it calculates the first and second derivatives of the data and uses the maximum curvature (maximum in the second derivative) to estimate the Curie Temperature. It can be tricky to get the "right" temperature, especially if there are two inflections and/or the data are noisy. Therefore, the program will scan through a range of smoothing intervals. You can truncate the interval over which you want to look (see the help message for the **ipmag.curie**) and set the smoothing interval. The program has a default smoothing window width of 3°, which is usually too small to get an accurate Curie Temperature. The first data file is not very noisy and the second is noisier.

First look at each data file using the defaults. Then, choose the optimal smoothing interval (the smallest interval necessary to isolate the correct peak in the second derivative). Finally, repeat this, but truncate the data set to between 400° to 600°.

What is the Curie Temperature of the two specimens?

**Problem 2**

Rock magnetic parameters have been used extensively to study the Chinese sequences of loess. Data from one such study ({cite}`hunt1995`) is saved in the file loess_rockmag.dat in the Chapter_8 directory. The data columns are: stratigraphic position in meters below reference horizon, total mass normalized magnetic susceptibility ($\kappa_{total}$) in (μm)³kg⁻¹, and sIRM in (mAm)²kg⁻¹. The paramagnetic susceptibility ($\kappa_p$) for the section was relatively constant at about 60 nm³kg⁻¹.

Make plots of total susceptibility, ferromagnetic susceptibility ($\kappa_f = \kappa_{total} - \kappa_p$), sIRM and the ratio $\kappa_f$/sIRM versus stratigraphic position. The reference horizon was the top of the modern soil, $S_0$.

Magnetic susceptibility is closely linked to lithology, with peaks associated with soil horizons. The triplet of peaks between about 20 and 27 meters are three units in soil $S_1$, which spans the interval 75 ka to 128 ka. The material in between $S_0$ and $S_1$ is the top-most loess horizon $L_1$. The interval below $S_1$ is $L_2$.

The explanation for the high magnetic susceptibility in the soils has been that there is magnetic enhancement caused by growth of superparamagnetic magnetite in the soil horizons. Susceptibility, sIRM and their ratio have all been used as magnetic proxies of past climate changes (mainly rainfall/year). But, only one of them represents best the concentration of the superparamagnetic particle fraction created from iron silicates by rainfall. Which of the profiles you plotted would be the best proxy for the superparamagnetic fraction and why?

**Problem 3**

The sand on Scripps beach accumulates in the summer when gentle waves drop their load high up on the beach and erodes in the winter when high energy waves strip the sand away, leaving bare rock. Sand accumulation and preservation therefore depends critically on density. The sand can be crudely divided into a light colored fraction, composed of quartz, plagioclase, and feldspar and a darker fraction, composed of magnetite, pyroxene, amphibole, and biotite. Wave action on the beach separates the sand into light and dark stripes with the darker sand being deposited at points when the water velocity slows down (over ripples or around stones, for example). Average density measurements would help sedimentologists predict which beaches are more resistant to erosion during winter storms, but accurate density measurements are time consuming.

As part of a class project, students investigated whether magnetic susceptibility could be used as a proxy for density because it is much quicker and easier to measure. Students collected five test samples of sand ranging from light (#1) to dark (#5). They dried and weighed out sand into 7 cc plastic boxes. The specimens were measured on a Bartington susceptibility meter with units of 10⁻⁵ SI, assuming a 10cc specimen.

:::{table} Data for beach project.
:name: tab:beach

| Specimen | χ (10⁻⁵ SI) | Mass (gm) |
|----------|-------------|-----------|
| #1 | 0.05 | 9.92 |
| #2 | 0.2 | 10.00 |
| #3 | 0.4 | 11.03 |
| #4 | 1.94 | 11.29 |
| #5 | 3.3 | 11.31 |
:::

a) Convert the susceptibility in [Table %s](#tab:beach) (also in *beach_sand.dat* in the Chapter_8 Datafiles folder) into mass normalized units in m³kg⁻¹. Make plots of susceptibility against color (specimen number) and density.

b) Is there a relationship? Pose a plausible hypothesis that explains your observations. How would you test it?

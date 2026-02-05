---
title: Magnetic Hysteresis
label: chap:hysteresis
---

In [Chapter 4](#chap:anisotropy) we discussed the energies that control the state of magnetization within ferromagnetic particles. Particles will tend to find a configuration of internal magnetization directions that minimizes the energies (although meta-stable states with *local energy minima* or LEMs are a possibility). The longevity of a particular magnetization state has to do with the depth of the energy well that the magnetization is in and the energy available for hopping over barriers.

The ease with which particles can be coerced into changing their magnetizations in response to external fields can tell us much about the overall stability of the particles and perhaps also something about their ability to carry a magnetic remanence over the long haul. The concepts of long term stability, incorporated into the concept of relaxation time and the response of the magnetic particles to external magnetic fields are therefore linked through the anisotropy energy constant $K$ (see [Chapter 4](#chap:anisotropy)) which dictates the magnetic response of particles to changes in the external field. This chapter will focus on the response of magnetic particles to changing external magnetic fields.

## The "flipping" field
(sect:flipping)=

Magnetic remanence is the magnetization in the absence of an external magnetic field. If we imagine a particle with a single "easy" axis — a so-called "uniaxial" particle with magnetic anisotropy constant $K_u$, the magnetic energy density (energy per unit volume) of a particle whose magnetic moment makes an angle $\theta$ to the easy axis direction ([](#fig:mB)a) can be expressed as:

$$
\epsilon_a = K_u\sin^2\theta.
$$

As the moment swings around with angle $\theta$ to the easy axis, the anisotropy energy density $\epsilon_a$ will change as sketched in [](#fig:mB)b. The energy minima are when $\theta$ is aligned parallel to the easy axis (an axis means either direction along the axis, so we pick one direction as being 0 and the other as 180°). In the absence of a magnetic field, the moment will lie along one of these two directions. [In reality, thermal energy will perturb this direction somewhat, depending on the balance of anisotropy to thermal energy, but for the present discussion, we are assuming that thermal energy can be neglected.]

:::{figure} ../figures/chapter5/mB.png
:name: fig:mB
:width: 100%

a) Sketch of a magnetic particle with easy axis as shown. In response to a magnetic field $\mathbf{B}$, applied at an angle $\phi$ to the easy axis, the particle moment $\mathbf{m}$ rotates, making an angle $\theta$ with the easy axis. b) Variation of the anisotropy energy density $\epsilon_a = K_u\sin^2\theta$ as a function of $\theta$ for the particle with $\phi=45°$ as shown in a). The $\theta$ associated with the minimum energy is indicated by $\epsilon_{min}$. $B$ = 0 mT. c) Same as in b) but for $B$ = 30 mT. Also shown the interaction energy density $\epsilon_m=-M_s B\cos (\phi-\theta)$ and the total energy density $\epsilon_t=\epsilon_a+\epsilon_m$.
:::

When an external field is applied at an angle $\phi$ to the easy axis (and an angle $\phi-\theta$ with the magnetic moment; see [](#fig:mB)a), the magnetostatic interaction energy density $\epsilon_m$ given by the dot product of the magnetization and the applied field ([Equation %s](#eq:Em1) in Chapter 4) or:

$$
\epsilon_m = -\mathbf{M} \cdot \mathbf{B} = -MB \cos(\phi-\theta).
$$

The two energy densities ($\epsilon_a$ and $\epsilon_m$) are shown as the thin solid and dashed lines in [](#fig:mB)c for an applied field of 30 mT aligned with an angle of 45° to the easy axis. There is a competition between the anisotropy energy (tending to keep the magnetization parallel to the easy axis) and the interaction energy (tending to line the magnetization up with the external magnetic field). Assuming that the magnetization is at saturation, we get the total energy density of the particle to be:

$$
\epsilon_t = K_u\sin^2\theta - M_s B \cos (\phi-\theta).
$$ (eq:Et)

The total energy density $\epsilon_t$ is shown as the heavy solid line in [](#fig:mB)c.

The magnetic moment of a uniaxial single domain grain will find the angle $\theta$ that is associated with the minimum total energy density ($\epsilon_{min}$; see [](#fig:mB)b,c). For low external fields, $\theta$ will be closer to the easy axis and for higher external fields (e.g., 30 mT; [](#fig:mB)c), $\theta$ will be closer to the applied field direction ($\phi$).

:::{figure} ../figures/chapter5/flip.png
:name: fig:flip
:width: 100%

a) Variation of the anisotropy energy density $\epsilon_a = K_u\sin^2\theta$, the interaction energy density $\epsilon_m=-M_s B\cos \phi$ and the total energy density $\epsilon_t=\epsilon_a+\epsilon_m$ as a function of $\theta$ for the particle shown in [](#fig:mB)a. The field was applied with $\phi$ = 180° and was 58 mT in magnitude. The $\theta$ associated with the minimum energy is indicated by $\epsilon_{min}$ and is 180°. b) Variation in first and second derivatives of the energy equation. The flipping condition of both being zero simultaneously is met. c) Same as a) but the field was only 30 mT. d) Same as b) but the flipping condition is not met.
:::

When a magnetic field that is large enough to overcome the anisotropy energy is applied in a direction opposite to the magnetization vector, the moment will jump over the energy barrier and stay in the opposite direction when the field is switched off. The field necessary to accomplish this feat is called the *flipping field* ($\mu_oH_f$) (also sometimes the "switching field"). [Note the change to the use of $H$ for internal fields where $M$ cannot be considered zero.] We introduced this parameter in Chapter 4 (see [Equation %s](#eq:Bk)) as the microscopic coercivity. {cite}`stoner1948` showed that the flipping field can be found from the condition that $d\epsilon_t/d\theta = 0$ and $d^2\epsilon_t/d\theta^2$ = 0. We will call this the "flipping condition". The necessary equations can be found by differentiating [Equation %s](#eq:Et):

$$
\frac{d\epsilon}{d\theta} = 2 K_u \sin \theta \cos \theta - M_s B \sin (\phi - \theta),
$$ (eq:1stderiv)

and again

$$
\frac{d^2 \epsilon}{d\theta^2} = 2 K_u \cos (2\theta) + M_s B \cos (\phi - \theta).
$$ (eq:2ndderiv)

Solving these two equations for $B$ and substituting $\mu_oH$ for $B$, we get after some trigonometric trickery:

$$
\mu_o H_f = \frac{2K_u}{M_s} \frac{(1-t^2 + t^4)^{1/2}}{1 + t^2} = \frac{2K_u}{M_s} \frac{1}{(\cos^{2/3} \phi + \sin^{2/3} \phi)^{3/2}},
$$ (eq:Bf)

where $t= \tan^{1/3} \phi$. In this equation, $\phi$ is the angle between the applied field and the easy axis direction opposite to $m$.

Now we can derive the so-called "microscopic coercivity" ($H_k$) introduced in [](#sect:coercivity) in Chapter 4. Microscopic coercivity is the maximum flipping field for a particle. When magnetic anisotropy of a particle is dominated by uniaxial anisotropy constant $K_u$ and $\phi$ is zero (antiparallel to the easy direction nearest the moment), $\mu_o H_k = 2K_u/M_s$. Using the values appropriate for magnetite ($K_u$ = 1.4 × 10$^4$ Jm$^{-3}$ and $M_s$ = 480 kAm$^{-1}$) we get $\mu_o H_k$ = 58 mT. To see why this would indeed result in a flipped moment, we plot the behavior of [Equations %s](#eq:Et) – [%s](#eq:2ndderiv) in [](#fig:flip). The minimum in total energy $\epsilon_t$ occurs at an angle of $\theta$ = 180° ([](#fig:flip)a) and the first and second derivatives satisfy the flipping condition by having a common zero crossing ($\theta=0$ in [](#fig:flip)b). There is no other applied field value for which this is true (see, e.g., the case of a 30 mT field in [](#fig:flip)c,d).

:::{figure} ../figures/chapter5/bf.png
:name: fig:bf
:width: 50%

The flipping field $\mu_oH_f$ required to irreversibly switch the magnetization vector from one easy direction to the other in a single domain particle dominated by uniaxial anisotropy. Note that $\phi$ is the angle with the easy axis, but must be the opposite direction from $\mathbf{m}$.
:::

The flipping condition depends not only on the applied field magnitude but also on the direction that it makes with the easy axis (see $\mu_oH_f$ versus $\phi$ in [](#fig:bf)). When $\phi$ is parallel to the easy axis (zero) (and anti-parallel to $\mathbf{m}$), $\mu_oH_f$ is 58 mT as we found before. $\mu_oH_f$ drops steadily as the angle between the field and the easy axis increases until an angle of 45° when $\mu_oH_f$ starts to increase again. According to [Equation %s](#eq:Bf), $\mu_oH_f$ is undefined when $\phi$ = 90°, so when the field is applied at right angles to the easy axis, there is no field sufficient to flip the moment.

## Hysteresis loops

In this section we will develop the theory for predicting the response of substances to the application of external fields, in experiments that generate hysteresis loops. We will define a number of parameters which are useful in rock and paleomagnetism.

Let us begin by considering what happens to single particles when subjected to applied fields in the cycle known as the *hysteresis loop*. From the last section, we know that when a single domain, uniaxial particle is subjected to an increasing magnetic field the magnetization is gradually drawn into the direction of the applied field. If the flipping condition is not met, then the magnetization will return to the original direction when the magnetic field is removed. If the flipping condition is met, then the magnetization undergoes an irreversible change and will be in the opposite direction when the magnetic field is removed.

### Uniaxial anisotropy
(sect:uniaxial)=

Imagine a single domain particle with uniaxial anisotropy. Because the particle is single domain, the magnetization is at saturation and, in the absence of an applied field is constrained to lie along the easy axis. Now suppose we apply a magnetic field in the opposite direction (see track #1 in [](#fig:outerloop)a). When $B$ reaches $\mu_oH_f$ in magnitude, the magnetization flips to the opposite direction (track #2 in [](#fig:outerloop)) and will not change further regardless of how high the field goes. The field then is decreased to zero and then increased along track #3 in [](#fig:outerloop) until $\mu_oH_f$ is reached again. The magnetization then flips back to the original direction (track #4 in [](#fig:outerloop)a).

Applying fields at arbitrary angles to the easy axis results in loops of various shapes (see [](#fig:outerloop)b). As $\phi$ approaches 90°, the loops become thinner. Remember that the flipping fields for $\phi$ = 22° and $\phi = 70°$ are similar (see [](#fig:bf)) and are lower than that when $\phi=0°$, but the flipping field for $\phi = 90°$ is infinite, so that "loop" is closed and completely reversible.

:::{figure} ../figures/chapter5/outerloop.png
:name: fig:outerloop
:width: 100%

a) Moment measured for the particle ($\phi=0°$) with applied field starting at 0 mT and increasing in the opposite direction along track #1. When the flipping field $\mu_oH_f$ is reached, the moment switches to the other direction along track #2. The field then switches sign and decreases along track #3 to zero, then increases again to the flipping field. The moment flips and the field increases along track #4. b) The component of magnetization parallel to +B$_{max}$ versus $B$ for field applied with various angles $\phi$.
:::

Before we go on, it is useful to consider for a moment how hysteresis measurements are made in practice. Measurements of magnetic moment $m$ as a function of applied field $B$ are made on a variety of instruments, such as a vibrating sample magnetometer (VSM) or alternating gradient force magnetometer (AGFM). In the latter, a specimen is placed on a thin stalk between pole pieces of a large magnet. There is a probe mounted behind the specimen that measures the applied magnetic field. There are small coils on the pole pieces that modulate the gradient of the applied magnetic field (hence alternating gradient force). The specimen vibrates in response to changing magnetic fields and the amplitude of the vibration is proportional to the moment in the axis of the applied field direction. The vibration of the specimen stalk is measured and calibrated in terms of magnetic moment. The magnetometer is only sensitive to the induced component of $\mathbf{m}$ parallel to the applied field $\mathbf{B}_o$, which is $m_{||}= m \cos \phi$ (because the off axis terms are squared and very small, hence can be neglected.) In the hysteresis experiment, therefore, the moment parallel to the field $m_{||}$ is measured as a function of applied field $B$.

:::{figure} ../figures/chapter5/sdloops.png
:name: fig:sdloops
:width: 100%

a) Net response of a random assemblage of uniaxial single domain particles. Snap shots of magnetization states (squares labelled 1 to 4) for representative particles are shown in the balloons labelled State 1–4. The initial demagnetized state is "State 1". The initial slope as the field is increased from zero is the low-field susceptibility $\chi_{lf}$. If the field returns to zero after some flipping fields have been exceeded, there is a net isothermal remanence (IRM). When all the moments are parallel to the applied field (State 2), the magnetization is at saturation $M_s$. When the field is returned to zero, the magnetization is a saturation remanence ($M_r$; State 3). When the field is applied in the opposite direction and has remagnetized half the moments (State 4), the field is the bulk coercive field $\mu_oH_c$. When a field is reached that when reduced to zero leaves zero net remanence, that field is the coercivity of remanence (here labelled $\mu_oH_{cr}'$). b) Curve obtained by subtracting the ascending curve in a) from the descending curve. The field at which half the moments have flipped, leaving a magnetization of one half of saturation is another measure of the coercivity of remanence, here labelled $\mu_oH_{cr}$.
:::

In rocks with an assemblage of randomly oriented particles with uniaxial anisotropy, we would measure the sum of all the millions of tiny individual loops. A specimen from such a rock would yield a loop similar to that shown in [](#fig:sdloops)a. If the field is first applied to a demagnetized specimen, the initial slope is the (low field) magnetic susceptibility ($\chi_{lf}$) first introduced in Chapter 1. From the treatment in [](#sect:flipping) it is possible to derive the equation $\chi_{lf} = \mu_o M_s^2/3K_u$ for this initial (ferromagnetic) susceptibility (for more, see {cite}`oreilly1984`).

If the field is increased beyond the flipping field of some of the magnetic grains and returned to zero, the net remanence is called an *isothermal remanent magnetization* (IRM). If the field is increased to $+B_{max}$, all the magnetizations are drawn into the field direction and the net magnetization is equal to the sum of all the individual magnetizations and is the *saturation magnetization* $M_s$. When the field is reduced to zero, the moments relax back to their individual easy axes, many of which are at a high angle to the direction of the saturating field and cancel each other out. A loop that does not achieve a saturating field (red in [](#fig:sdloops)a) is called a *minor hysteresis loop*, while one that does is called the *outer loop*.

:::{figure} ../figures/chapter5/Bcr.png
:name: fig:Bcr
:width: 60%

Heavy green line: initial behavior of demagnetized specimen as applied field ramps up from zero field to a saturating field. The initial slope is the initial or low-field susceptibility $\chi_{lf}$. After saturation is achieved the slope is the high-field susceptibility $\chi_{hf}$ which is the non-ferromagnetic contribution, in this case the paramagnetic susceptibility (because $\chi_{hf}$ is positive.) The dashed blue line is the hysteresis loop after the paramagnetic slope has been subtracted. Saturation magnetization $M_s$ is the maximum value of magnetization after slope correction. Saturation remanence $M_r$ is the value of the magnetization remaining in zero applied field. Coercivity ($\mu_o H_c$) and coercivity of remanence $\mu_oH_{cr}'$ are as in [](#fig:sdloops)a.
:::

The net remanence after saturation is termed the *saturation remanent magnetization* $M_r$ (and sometimes the saturation isothermal remanence sIRM). For a random assemblage of single domain uniaxial particles, $M_r/M_s$ = 0.5. The field necessary to reduce the net moment to zero is defined as the *coercive field* ($\mu_oH_c$) (or coercivity).

The coercivity of remanence $\mu_o H_{cr}$ is defined as the magnetic field required to irreversibly flip half the magnetic moments (so the net remanence after application of a field equal to $-\mu_oH_{cr}$ to a saturation remanence is 0). The coercivity of remanence is always greater than or equal to the coercivity and the ratio $H_{cr}/H_c$ for our random assemblage of uniaxial SD particles is 1.09 {cite}`wohlfarth1958`. Here we introduce two ways of estimating coercivity of remanence, illustrated in [](#fig:sdloops). If, after taking the field up to some saturating field $+B_{max}$, one first turned the field off (the descending curve), then increased the field in the opposite direction to the point labeled $\mu_oH'_{cr}$, and one were to then switch the field off again, the magnetization would follow the dashed curve up to the origin. For single domain grains, the dashed curve would be parallel to the lower curve (the ascending curve). So, if one only measured the outer loop, one could estimate the coercivity of remanence by simply tracing the curve parallel to the lower curve (dashed line) from the origin to the point of intersection with the upper curve (circled in [](#fig:sdloops)a). This estimate is only valid for single domain grains, hence the prime in $\mu_oH_{cr}'$.

An alternative means of estimating coercivity of remanence is to use a so-called $\Delta M$ curve {cite}`jackson1990` which is obtained by subtracting the ascending loop from the descending loop (see [](#fig:sdloops)b). When all the moments are flipped into the new field, the ascending and descending loops join together and $\Delta M$ is 0. $\Delta M$ is at 50% of its initial value at the field at which half the moments are flipped (the definition of coercivity of remanence); this field is here termed $\mu_oH_{cr}$.

### Magnetic susceptibility
(sect:chi)=

[](#fig:sdloops)a is the loop created in the idealized case in which only uniaxial ferromagnetic particles participated in the hysteresis measurements; in fact the curve is entirely theoretical. In "real" specimens there can be paramagnetic, diamagnetic AND ferromagnetic particles and the loop may well look like that shown in [](#fig:Bcr). The initial slope of a hysteresis experiment starting from a demagnetized state in which the field is ramped from zero up to higher values is the low field magnetic susceptibility or $\chi_{lf}$ (see [](#fig:Bcr)). If the field is then turned off, the magnetization will return again to zero. But as the field increases past the lowest flipping field, the remanence will no longer be zero but some isothermal remanence. Once all particle moments have flipped and saturation magnetization has been achieved, the slope relating magnetization and applied field reflects only the non-ferromagnetic (paramagnetic and/or diamagnetic) susceptibility, here called *high field susceptibility*, $\chi_{hf}$. In order to estimate the saturation magnetization and the saturation remanence, we must first subtract the high field slope. So doing gives us the blue dashed line in [](#fig:Bcr) from which we may read the various hysteresis parameters illustrated in [](#fig:sdloops)b.

### Cubic anisotropy

In the case of equant grains of magnetite for which magnetocrystalline anisotropy dominates, there are four easy axes, instead of two as in the uniaxial case (see [Chapter 4](#chap:anisotropy)). The maximum angle $\phi$ between an easy axis and an applied field direction is 55°. Hence there is no individual loop that goes through the origin (see [](#fig:cubic)). A random assemblage of particles with cubic anisotropy will therefore have a much higher saturation remanence. In fact, the theoretical ratio of $M_r/M_s$ for such an assemblage is 0.87, as opposed to 0.5 for the uniaxial case {cite}`joffe1974`.

:::{figure} ../figures/chapter5/cubicloops.png
:name: fig:cubic
:width: 50%

Heavy lines: theoretical behavior of cubic grains of magnetite. Dashed lines are the responses along particular directions. Light grey lines: hysteresis response for single particles with various orientations with respect to the applied field. [Figure from {cite}`tauxe2002`.]
:::

### Superparamagnetic particles
(sect:SP)=

In superparamagnetic (SP) particles, the total magnetic energy $E_t=\epsilon_tv$ (where $v$ is volume) is balanced by thermal energy $kT$. This behavior can be modeled using statistical mechanics in a manner similar to that derived for paramagnetic grains in Chapter 3. In fact,

$$
\frac{M}{M_s} = N\left(\coth \gamma - \frac{1}{\gamma}\right),
$$ (eq:Lang1)

where $\gamma = M_sBv/(kT)$ and $N$ is the number of particles of volume $v$, is a reasonable approximation. The end result, [Equation %s](#eq:Lang1), is the familiar Langevin function from our discussion of paramagnetic behavior (see Chapter 3); hence the term "superparamagnetic" for such particles.

:::{figure} ../figures/chapter5/loops.png
:name: fig:loops
:width: 80%

a) The contribution of SP particles with saturation magnetization $M_s$ and cubic edge length $d$. $\gamma = BM_s d^3/kT$. There is no hysteresis. b) The field at which the magnetization reaches 90% of the maximum $B_{90}$ is when $M_s d^3/kT\simeq 10$. [Figure from {cite}`tauxe1996`.]
:::

The contribution of SP particles for which the Langevin function is valid with given $M_s$ and $d$ is shown in [](#fig:loops)a. The field at which the population reaches 90% saturation $B_{90}$ occurs at $\gamma \sim 10$. Assuming particles of magnetite ($M_s$ = 480 kAm$^{-1}$) and room temperature ($T=300$ K), $B_{90}$ can be evaluated as a function of $d$ (see [](#fig:loops)b). Because of its inverse cubic dependence on $d$, $B_{90}$ rises sharply with decreasing $d$ and is hundreds of tesla for particles a few nanometers in size, approaching paramagnetic values. $B_{90}$ is a quick guide to the SP slope (the SP susceptibility $\chi_{sp}$) contributing to the hysteresis response and was used by {cite}`tauxe1996` as a means of explaining distorted loops sometimes observed for populations of SD/SP mixtures. $B_{90}$ (and $\chi_{sp}$) is very sensitive to particle size with very steep slopes for the particles at the SP/SD threshold. The exact threshold size is still rather controversial, but {cite}`tauxe1996` argue that it is ~20 nm.

For low magnetic fields, the Langevin function can be approximated as $\sim \frac{1}{3} \gamma$. So we have:

$$
\frac{M}{M_s} = \frac{1}{3} \frac{M_sBv}{kT}.
$$

If we substitute $\mu_o H$ for $B$ and rearrange this equation, we can get the superparamagnetic susceptibility $\chi_{sp}$ as:

$$
\frac{M}{H} = \frac{\mu_o M_s^2v}{3kT}.
$$ (eq:chiSP)

We can rearrange [Equation %s](#eq:tau) in Chapter 4 to solve for the volume at which a uniaxial grain passes through the superparamagnetic threshold we find:

$$
v_b = \frac{kT \ln (C\tau)}{K_u}.
$$

Finally, we can substitute this volume into [Equation %s](#eq:chiSP) as the maximum volume of an SP grain, giving us:

$$
\chi_{sp} = \frac{\mu_o M_s^2 \ln (C\tau)}{3K_u}.
$$ (eq:chiSP1)

Comparing this expression with that derived for ferromagnetic susceptibility in [](#sect:uniaxial), we find that $\chi_{sp}$ is a factor of $\ln(C\tau)\simeq 27$ larger than the equivalent single domain particle.

### Particles with domain walls
(sect:day)=

Moving domain walls around is much easier than flipping the magnetization of an entire particle coherently. The reason for this is the same as the reason that it is easier to move a rug by lifting up a small wrinkle and pushing that through the rug, than to drag the whole rug by the same amount. Because of the greater ease of changing magnetic moments in multidomain (MD) grains, they have lower coercive fields and saturation remanence is also much lower than for uniformly magnetized particles (see typical MD hysteresis loop in [](#fig:md)a.)

:::{figure} ../figures/chapter5/mdloop.png
:name: fig:md
:width: 100%

a) Typical hysteresis loop from a multi-domain assemblage. b) Theoretical behavior for the region in the inset to a). c) Theoretical relationship between $M_r/M_s$ and $H_{cr}/H_c$ for constant $\chi_iH_c/M_s = 0.1$. Heavy red line is the theoretical linear mixing curve of SD/MD end-members. (See text.)
:::

The key to understanding multi-domain hysteresis is the reduction in multi-domain magnetic susceptibility $\chi_{md}$ from "true" magnetic susceptibility ($\chi_i$) because of self-demagnetization. The true susceptibility would be that obtained by measuring the magnetic response of a particle to the internal field $\mathbf{H}_i$ (applied field minus the demagnetizing field $-N\mathbf{M}$ — see [](#sect:shape); see Dunlop, 2002a {cite}`dunlop2002a`). Recalling that the demagnetizing factor is $N$, the so-called *screening factor* $f_s$ is $(1 + N\chi_i)^{-1}$ and $\chi_{md} = f_s \chi_i$. If we assume that $\chi_{md}$ is linear for fields less than the coercivity, then by definition $\chi_{md} = M_r/H_c$ (see [](#fig:md)b). From this, we get:

$$
\frac{M_r}{M_s} = \chi_{md} \frac{H_c}{M_s} = f_s \chi_i \frac{H_c}{M_s}.
$$

In the case of multi-domain susceptibility, $\chi_i$ is much larger than $\chi_{md}$ and $M_r = H_c/N$.

By a similar argument, coercivity of remanence ($H_{cr}$) is suppressed by the screening factor which gives coercivity so:

$$
H_c = f_s H_{cr},
$$

from which we get the ratio:

$$
\frac{H_{cr}}{H_c} = \frac{1}{f_s}.
$$

Putting all this together leads us to the remarkable relationship noted by {cite}`day1977` (see also {cite}`dunlop2002a`):

$$
\frac{M_r}{M_s} \cdot \frac{H_{cr}}{H_c} = \chi_i \frac{H_c}{M_s}.
$$ (eq:day)

When $\chi_i H_c/M_s$ is constant, [Equation %s](#eq:day) is a hyperbola. For a single mineralogy, we can expect $M_s$ to be constant, but $H_c$ depends on grain size and the state of stress which are unlikely to be constant for any natural population of magnetic grains. Dunlop (2002a) {cite}`dunlop2002a` argues that if the main control on susceptibility and coercivity is domain wall motion through a terrain of variable wall energies, then $\chi_i$ and $H_c$ would be inversely related and gives a tentative theoretical value for $\chi_iH_c$ in magnetite of about 45 kAm$^{-1}$. This, combined with the value of $M_s$ for magnetite of 480 kAm$^{-1}$ gives a value for $\chi_i H_c/M_s \sim 0.1$. When anchored by the theoretical maximum for uniaxial single domain ratio of $M_r/M_s = 0.5$, we get the curve shown in [](#fig:md)c. The major control on coercivity is grain size, so the trend from the SD limit down toward low $M_r/M_s$ ratios is increasing grain size.

:::{figure} ../figures/chapter5/void.png
:name: fig:void
:width: 80%

Interaction of a domain wall and a void. When the void is within a domain, free poles create a magnetic field which creates a self energy (Chapter 4). When a domain wall intersects the void, the self-energy is reduced. There are no exchange or magnetocrystalline anisotropy energy terms within the void, so the wall energy is reduced.
:::

There are several possible causes of variability in wall energy within a magnetic grain, for example, voids, lattice dislocations, stress, etc. The effect of voids is perhaps the easiest to visualize, so we will consider voids as an example of why wall energy varies as a function of position within the grain. We show a particle with lamellar domain structure and several voids in [](#fig:void). When the void occurs within a uniformly magnetized domain (left of figure), the void sets up a demagnetizing field as a result of the free poles on the surface of the void. There is therefore, a self-energy associated with the void. When the void is traversed by a wall, the free pole area is reduced, reducing the demagnetizing field and the associated self-energy. Therefore, the energy of the void is reduced by having a wall bisect it. Furthermore, the energy of the wall is also reduced, because the area of the wall in which magnetization vectors are tormented by exchange and magnetocrystalline energies is reduced. The wall gets a "free" spot if it bisects a void. The wall energy $E_w$ therefore is lower as a result of the void.

:::{figure} ../figures/chapter5/wallenergy.png
:name: fig:wallenergy
:width: 100%

a) Schematic view of wall energy across a transect of a multi-domain grain. Inset: Placement of domain walls in the demagnetized state. [Domain observations from {cite}`halgedahl1983`.] b–g) Schematic view of the magnetization process in MD grain shown in previous figure. b) Demagnetized state, c) in the presence of a saturating field, d) field lowered to +3 mT, e) remanent state, f) backfield of −3 mT, g) resulting loop. Inset shows detail of domain walls moving by small increments called Barkhausen jumps. [Domain wall observations from {cite}`halgedahl1983`; schematic loop after {cite}`oreilly1984`.]
:::

In [](#fig:wallenergy), we show a sketch of a hypothetical transect of $E_w$ across a particle. There are four LEMs labelled a–d. Domain walls will distribute themselves throughout the grain in order to minimize the net magnetization of the grain and also to try to take advantage of LEMs in wall energy.

Domain walls move in response to external magnetic fields (see [](#fig:wallenergy)b–g). Starting in the demagnetized state ([](#fig:wallenergy)b), we apply a magnetic field that increases to saturation ([](#fig:wallenergy)c). As the field increases, the domain walls move in sudden jerks as each successive local wall energy high is overcome. This process, known as *Barkhausen jumps*, leads to the stair-step like increases in magnetization (shown in the inset of [](#fig:wallenergy)g). At saturation, all the walls have been flushed out of the crystal and it is uniformly magnetized. When the field decreases again, to say +3 mT ([](#fig:wallenergy)d), domain walls begin to nucleate, but because the energy of nucleation is larger than the energy of denucleation, the grain is not as effective in cancelling out the net magnetization, hence there is a net saturation remanence ([](#fig:wallenergy)e). The walls migrate around as a magnetic field is applied in the opposite direction ([](#fig:wallenergy)f) until there is no net magnetization. The difference in nucleation and denucleation energies was called on by {cite}`halgedahl1983` to explain the high stability observed in some large magnetic grains.

## Hysteresis of mixtures of SP, SD and MD grains
(sect:mixtures)=

{cite}`day1977` popularized the use of diagrams like that shown in [](#fig:md)c which are known as *Day diagrams*. They placed quasi-theoretical bounds on the plot whereby points with $M_r/M_s$ ratios above 0.5 were labelled single domain (SD), and points falling in the box bounded by $0.5>M_r/M_s>0.05$ and $1.5<H_{cr}/H_c < 5$ were labelled *pseudo-single domain* (PSD). Points with $M_r/M_s$ below 0.05 were labelled multi-domain (MD). This paper has been cited over 800 times in the literature and the Day plot still serves as the principal way that rock and paleomagnetists determined domain state and grain size.

The problem with the Day diagram is that virtually all paleomagnetically useful specimens yield hysteresis ratios that fall within the PSD box. In the early 90s, paleomagnetists began to realize that many things besides the trend from SD to MD behavior control where points fall on the Day diagram. {cite}`pick1994` pointed out that mixtures of SP and SD grains would have reduced $M_r/M_s$ ratios and enhanced $H_{cr}/H_c$ ratios. {cite}`tauxe1996` modelled distributions of SP/SD particles and showed that the SP-SD trends always fall above those observed from MD particles (modelled in [](#fig:md)c).

{cite}`dunlop2002a` argued that because $M_r$ for SP grains is zero, the suppression of the ratio $M_r/M_s$ is directly proportional to the volume fraction of the SP particles. Moreover, coercivity of remanence remains unchanged, as it is entirely due to the non-SP fraction. Deriving the relationship of coercivity, however, is not so simple. It depends on the superparamagnetic susceptibility ($\chi_{sp}$), which in turn depends on the size of the particle and also the applied field (see [](#sect:SP)). In his simplified approach, Dunlop could only use a single (small) grain size, whereas in natural samples, there will always be a distribution of grain sizes. It is also important to remember that volume goes as the cube of the radius and for a mixture to display any SP suppression of $M_r/M_s$ almost all of the particles must be SP. It is impossible that these would all be of a single radius (say 10 or 15 nm); there must be a distribution of sizes. Moreover, {cite}`dunlop2002a` neglected the complication in SP behavior as the particles reach the SD threshold size, whereas it is expected that many (if not most) natural samples containing both SP and SD grain sizes will have a large volume fraction of the largest SP sizes, making their neglect problematic.

Hysteresis ratios of mixtures of SD and MD particles will also plot in the "PSD" box. {cite}`dunlop2002a` derived the theoretical behavior of such mixtures on the Day diagram. The key equations are 1) Equation 9 from {cite}`dunlop2002a` which governs the behavior of the ratio $M_r/M_s$ as a function of the volume fraction of single domain material ($f_{SD}$) and multi-domain material ($f_{MD}$):

$$
M_r/M_s = f_{SD} (M_r/M_s)_{SD} + f_{MD} (M_r/M_s)_{MD},
$$

2) Equation 10 from {cite}`dunlop2002a` which governs the behavior of coercivity:

$$
H_c = \frac{f_{SD} \chi_{SD} (H_c)_{SD} + f_{MD} \chi_{MD} (H_c)_{MD}}{f_{SD} \chi_{SD} + f_{MD} \chi_{MD}},
$$

and 3) Equation 11 from {cite}`dunlop2002a` which governs the behavior of coercivity of remanence in SD/MD mixtures:

$$
H_{cr} = \frac{f_{SD}( \chi_r)_{SD} (H_{cr})_{SD} + f_{MD}( \chi_r)_{MD} (H_{cr})_{MD}}{f_{SD} (\chi_r)_{SD} + f_{MD} (\chi_r)_{MD}}
$$

where $\chi_{SD}$ and $\chi_{MD}$ are the susceptibilities of the SD and MD fractions respectively and $(\chi_r)_{SD}$ and $(\chi_r)_{MD}$ are the $M_r$ vs $H_{cr}$ slopes of the SD and MD remanences respectively. What we need to calculate the SD/MD mixing curve are values for the various parameters for single domain and multi domain end-members. These were measured empirically for the MV1H bacterial magnetosomes (see Chapter 6) and commercial magnetite (041183 of Wright Company) by {cite}`dunlop2006` and shown in the table below.

| SD/MD | $M_r/M_s$ | $\chi$ (A m$^{-1}$T$^{-1}$) | $\chi_r$ (MA m$^{-1}$T$^{-1}$) | $\mu_o H_c$ (mT) | $\mu_o H_{cr}$ (mT) |
|-------|-----------|------------------------------|--------------------------------|-------------------|---------------------|
| SD | 0.5 | 5.2 | 4.55 | 46 | 52.5 |
| MD | 0.02 | 4.14 | 0.88 | 5.56 | 26.1 |

: Empirical values for hysteresis parameters measured for single domain (SD) and multi-domain (MD) end-members of {cite}`dunlop2006`.

Using the linear mixing model of {cite}`dunlop2002a`, we plot the theoretical mixing curve predicted for these empirically constrained end-members as the heavy red line in [](#fig:md)c.

If a population of SD particles are so closely packed as to influence one another, there will be an effect of particle interaction. This will also tend to suppress the $M_r/M_s$ ratio, drawing the hysteresis ratios down into the PSD box. Finally, the PSD box could be populated by pseudo-single domain grains themselves. Here we will dwell for a moment on the meaning of the term "pseudo-single domain", which has evolved from the original posed by {cite}`stacey1961` (see discussion in {cite}`tauxe2002`). In an attempt to explain trends in TRM acquisition Stacey envisioned that irregular shapes caused unequal domain sizes, which would give rise to a net moment that was less than the single domain value, but considerably higher than the very low efficiency expected for large MD grains. The modern interpretation of PSD behavior is complicated micromagnetic structures that form between classic SD (uniformly magnetized grains) and MD (domain walls) such as the flower or vortex remanent states (see, e.g., [](#fig:nonuniform) in Chapter 4). Taking all these factors into account means that interpretation of the Day diagram is far from unique. The simple calculations of {cite}`dunlop2002a` are likely to be inappropriate for almost all natural samples.

## First order reversal curves

Hysteresis loops can yield a tremendous amount of information yet much of this is lost by simply estimating the set of parameters $M_r, M_s, H_{cr}, H_c, \chi_i, \chi_{hf}$, etc. {cite}`mayergoyz1986` developed a method using what are known as *First Order Reversal Curves* or FORCs to represent hysteresis data. The most recent way of dealing with FORCs is that of {cite}`harrison2008` which is illustrated in [](#fig:forcprinc). In the FORC experiment, a specimen is subjected to a saturating field, as in most hysteresis experiments. The field is lowered to some field $\mu_oH_a$, then increased again through some value $\mu_oH_b$ to saturation (see [](#fig:forcprinc)a). The magnetization curve between $\mu_o H_a$ and $\mu_oH_b$ is a "FORC". A series of FORCs (see [](#fig:forcprinc)b) can be generated to the desired resolution.

:::{figure} ../figures/chapter5/forcprinc.png
:name: fig:forcprinc
:width: 100%

a) Dashed line is the descending magnetization curve taken from a saturating field to some field $H_a$. Red line is the first order reversal curve (FORC) from $H_a$ returning to saturation. At any field $H_b>H_a$ there is a value for the magnetization $M(H_a,H_b)$. b) A series of FORCs for a single domain assemblage of particles. At any point there are a set of related "nearest neighbor" measurements (circles in inset). A least-squares fit to [Equation %s](#eq:forc) can be determined for each point. c) A contour plot of the FORC density surface for data in b). Specimen is of the Tiva Canyon Tuff, courtesy of the Institute for Rock Magnetism.
:::

To transform FORC data into some useful form, Harrison and Feinberg (2008) use a locally-weighted regression smoothing technique (LOESS). For a given measurement point $P$ LOESS fits a second-order polynomial function of the form

$$
M(H_a,H_b)= a_1 + a_2H_a + a_3H_a^2 + a_4H_b +a_5H_b^2 +a_6H_aH_b,
$$ (eq:forc)

to the measured magnetization surface in a specified region (for example the circle shown in [](#fig:forcprinc)b) where the $a_i$ are fitted coefficients. The LOESS technique takes a user defined number of the nearest neighbors (see inset to [](#fig:forcprinc)b) for an arbitrary shaped region over which the data are smoothed. The coefficient $-a_6(H_a,H_b)$ is the FORC density at the point. A FORC diagram is the contour plot of the FORC densities, rotated such that $\mu_oH_c = \mu_o(H_b-H_a)/2$ and $\mu_oH_u = \mu_o(H_a+H_b)/2$. Please note that because $H_a<H_b$, data are only possible for positive $H_c$.

:::{figure} ../figures/chapter5/m428.png
:name: fig:forcpsd
:width: 100%

a) A series of FORCs for a "pseudo-single domain" specimen. b) FORC diagram for data in a). Specimen is of the Stillwater Layered Intrusion, courtesy of J.S. Gee.
:::

Imagine we travel down the descending magnetization curve (dashed line in [](#fig:forcprinc)a) to a particular field $\mu_o H_a$ less than the smallest flipping field in the assemblage. If the particles are single domain, the behavior is reversible and the first FORC will travel back up the descending curve. It is only when $|\mu_o H_a|$ exceeds the flipping field of some of the particles that the FORC will trace a new curve on the inside of the hysteresis loop. In the simple single domain, non-interacting, uniaxial magnetite case, the FORC density in the quadrants where $H_a$ and $H_b$ are of the same sign must be zero. Indeed, FORC densities will only be non-zero for the range of flipping fields because these are the bounds of the flipping field distribution. So the diagram in [](#fig:forcprinc)c is nearly that of an ideal uniaxial SD distribution.

Consider now the case in which a specimen has magnetic grains with non-uniform magnetizations such as vortex structures or domain walls. Walls and vortices can move much more easily than flipping the moment of an entire grain coherently. In fact, they begin to move in small jumps (from LEM to LEM) as soon as the applied field changes. If a structure nucleates while the field is decreasing and the field is then ramped back up, the magnetization curve will not be reversible, even though the field never changed sign or approached the flipping field for coherent rotation. The resulting FORC for such behavior would have much of the "action" in the region where $H_a$ is positive. When transformed to $H_u$ and $H_c$, the diagram will have the high densities for small $H_c$ but over a range of $\pm H_u$. The example shown in [](#fig:forcpsd) is of a specimen that has been characterized as "pseudo-single domain". The FORC diagram in [](#fig:forcpsd)b has some of the FORC densities concentrated along the $H_c$ axis characteristic of single domain specimens (e.g., [](#fig:forcprinc)c), but there is also concentration along the $H_u$ axis characteristic of PSD and MD specimens.

:::{figure} ../figures/chapter5/ZFORC.png
:name: fig:ZFORC
:width: 70%

a) Illustration of a Zero FORC (ZFORC) whereby the descending loop from saturation is terminated at zero field and the field is then ramped back up to saturation. The transient hysteresis (TH) of {cite}`fabian2003` is the shaded area between the two curves. b) Micromagnetic model of a ZFORC for a 100 nm cube of magnetite. Two snap shots of the internal magnetization on the descending and ascending loops are shown in the insets. [Figure redrawn from {cite}`yu2005`.]
:::

In many cases the most interesting thing one learns from FORC diagrams is the degree to which there is irreversible behavior when the field is reduced to zero then ramped back up to saturation (see [](#fig:ZFORC)). Such irreversible behavior in what {cite}`yu2005` call the "Zero FORC" or ZFORC can arise from particle interactions, domain wall jumps or from the formation and destruction of vortex structures in the magnetic grains.

{cite}`fabian2003` defined a parameter called "transient hysteresis" which is the area between the ascending and descending loops of a ZFORC (shaded area in [](#fig:ZFORC)). This is defined as:

$$
TH= \mu_o\sum_0^{H_s} [M_{descending} - M_{ascending}] \cdot \Delta H.
$$

where $\Delta H$ is the field increment used in the hysteresis measurement. When normalized by $M_s$, TH has units of tesla. Transient hysteresis is thought to result from self demagnetization, for example shifting of domain walls or the formation and destruction of vortex structures. An example of what might be causing transient hysteresis at the macro scale is shown for micromagnetic modelling of a single particle in [](#fig:ZFORC)b {cite}`yu2005`. The ZFORC starts and ends at saturation. On the descending loop, a vortex structure suddenly forms, at the point on the hysteresis loop labelled a), sharply reducing the magnetization. The magnetization state just before the jump is shown as snapshot labelled "descending branch". The vortex remains along the ascending branch until much higher fields (see snapshot labelled "ascending branch"). The irreversible behavior of millions of particles with different sizes and shapes leads to the total transient hysteresis of the macro specimen. In general, {cite}`yu2005` showed that the larger the particle, the greater the transient hysteresis, until truly multi-domain behavior essentially closed the loop, precluding the observation of TH (or of a FORC diagram for that matter).

**Supplemental Reading:** {cite}`dunlop1997`, chapters 5 and 11; {cite}`oreilly1984`, pp 69–87; {cite}`dunlop2002a`; {cite}`dunlop2002b`.

## Problems

**Problem 1**

For a grain with uniaxial anisotropy in an external field, the direction of magnetization in this grain will be controlled entirely by the uniaxial anisotropy energy density $\epsilon_a$ and the magnetic interaction energy $\epsilon_m$. The total energy can be written:

$$
\epsilon_{tot} = \epsilon_a + \epsilon_m = K_u \sin^2 \theta - \mu_o H M_s \cos (\phi -\theta),
$$

where $\phi$ is the angle of the applied field relative to the easy axis of magnetization and $\theta$ is the angle of the moment relative to the easy direction. Show that the flipping field of a grain whose moment is initially antiparallel to the field, i.e. $\phi$ = 180°, is given by:

$$
H_c = \frac{2K_u}{\mu_o M_s}.
$$

**Problem 2** [From Jeff Gee]

In this problem, we will begin to use some real data. The data files used with this book are part of the **PmagPy** distribution, which you should have already downloaded and installed. [See Preface for instructions.]

The file *hysteresis.txt* in the Chapter_5 directory contains data for a single hysteresis loop. Note that the units are as measured: H (Oe), moment (emu) and it is fine to leave them in these units.

a) Read the data into a **Pandas** DataFrame. Determine the high field slope at $|H| > 4000$ Oe. Typically one calculates separate slopes for the +H data and -H data and averages these. A general least squares polynomial fit (numpy.polyfit) should do the trick.

b) Use the slope you determined to plot both the original hysteresis loop and the slope-corrected loop (i.e. removing the high field paramagnetic slope).

c) What is the ratio $M_r/M_s$ (saturation remanence/saturation magnetization) for this sample? The coercivity of remanence ($H_{cr}$) for this sample was estimated at 264 Oe. Based on the $M_r/M_s$ and $H_{cr}/H_c$ ratios, is this sample more likely to contain single domain or multidomain grains?

d) This small sample has a mass of 10.6 mg. Assuming the magnetic material is magnetite, estimate the mass fraction of magnetite (92 Am$^2$/kg; note 1 emu/gm is equivalent to 1 Am$^2$/kg).

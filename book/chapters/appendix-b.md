---
title: "Appendix B: Plots Useful in Paleomagnetism"
label: app:plots
authors:
  - name: Lisa Tauxe
    affiliation: Scripps Institution of Oceanography, UC San Diego
numbering:
  enumerator: B.%s
---

(app:eqarea)=
## Equal area projections

### Calculation of an equal area projection

:::{figure} ../figures/appendix/mkeq.png
:name: fig:mkeq
:width: 100%

Construction of an equal area projection for a point P corresponding to a $D$ of 40° and an $I$ of 35°. [Figure from {cite:t}`tauxe1998`.]
:::

The principles for how to make an equal area projection are shown in [](#fig:mkeq). The point P corresponds to a $D$ of 40° and $I$ of 35°. $D$ is measured around the perimeter of the equal area net and $I$ is transformed as follows:

$$
L=L_o\sqrt{(1-|x_3|)},
$$

where $L_o = 1/\sqrt{x_1^2+x_2^2}$.

:::{figure} ../figures/appendix/equal.png
:name: fig:equal
:width: 100%

Schmidt (equal area) net.
:::

:::{figure} ../figures/appendix/how2eq.png
:name: fig:how2eq
:width: 100%

How to use an equal area net (see text).
:::

(app:eqdir)=
### Plotting directions

The principles for plotting directions on an equal area net are shown in [](#fig:how2eq). Print out the equal area net provided in [](#fig:equal). Then poke a thumbtack through the center of the diagram and place a piece of tracing paper over the thumbtack. Mark the top of the stereonet as N and the declination of the direction at $Dir$ in [](#fig:how2eq)a. Then rotate the mark around the thumbtack such that the declination is at the top of the diagram ([](#fig:how2eq)b). Count in from the outer ring the number of degrees equal to the inclination - the grid provided is in 2° intervals. Mark the direction (star in [](#fig:how2eq)d). In paleomagnetism, the convention is for solid symbols to represent downward directions and open symbols to be up.

(app:eqtilt)=
### Bedding-tilt corrections

Performing structural corrections can also be done with an equal area net. If samples have been collected from sites where strata have been tilted by tectonic disturbance, a bedding tilt correction is required to determine the NRM direction with respect to paleohorizontal. Structural attitude of beds at the collecting site (strike and dip, or dip angle and direction) must be determined during the course of field work.

The bedding-tilt correction is accomplished by rotating the NRM direction about the local strike axis by the amount of the dip of the beds. Several examples are shown in [](#fig:tilt), and the reader is strongly encouraged to follow through these examples. An intuitive appreciation of these geometrical operations will prove invaluable in understanding many paleomagnetic techniques and applications.

Print out the equal-area grid provided in [](#fig:equal). Poke a thumb tack through the center and place a piece of tracing paper over it. The graphical procedure for the bedding-tilt correction is as follows:

1. Bedding attitude is defined by the down-dip direction (the dip direction) and dip angle. In the example of [](#fig:tilt), the dip direction is 40° and dip angle is 20°. The azimuth of bedding strike (orthogonal to down-dip direction) is defined as 90° anti-clockwise from dip direction (310° in the example of [](#fig:tilt)).

:::{figure} ../figures/appendix/tilt.png
:name: fig:tilt
:width: 100%

Example of structural corrections to NRM directions. The bedding attitude is specified by dip and dip direction (squares on the equal-area projections); the azimuth of the strike is 90° anti-clockwise from the dip direction; the rotation required to restore the bedding to horizontal is clockwise (as viewed along the strike line) by the dip angle and is shown by the rotation symbol; the *in situ* NRM direction is at the tail of the arrow, and the structurally corrected NRM direction is at the head of the arrow.
:::

2. Put the dip direction/dip angle and the paleomagnetic direction on the equal area net as described in [](#app:eqdir). These should look like the red square and circle respectively in [](#fig:tilt). Now mark the strike direction as shown in [](#fig:tilt). Rotate the equal-area grid such that the strike is at the top of the grid (you can also put it at the bottom or on either side).

3. The NRM direction is rotated clockwise about the strike azimuth (along a small circle) by an angle equaling the dip angle. In practice, this means that you count degrees from the circle toward the outer rim along the nearest small circle by the amount of the dip direction. If you reach the outer rim, just "walk back" in toward the center and keep counting. Plot a new circle (the blue one) at that point. If you reached the outer rim and continued back toward the center, this is a negative inclination (upward pointing) and you should use an open symbol.

4. Following this rotation, the *in situ* direction can be read from the equal-area projection. Rotate the blue dot to the up-down axis and make a mark on the outer rim. The degrees between this mark and the $N$ marked is the new declination. The number of degrees between the blue circle and the outer rim is the new inclination. For the example of [](#fig:tilt), the *in situ* direction is $I$ = 50°, $D$ = 70° and the direction corrected for bedding tilt is $I$ = 32°; $D$ = 62°.

(app:ternary)=
### Reading ternary diagrams

Ternary diagrams are triangles with the three corners representing a composition (e.g., A, B, C or Fe, FeO, Fe$_2$O$_3$). In [](#fig:how2tern)a we show only the A component. To get the percentage of this component, we count up from the base of the triangle and find that the star is 60% of the way toward the apex, indicating that the compound is 60% A in composition. The percentage of composition B is shown in [](#fig:how2tern)b (15%) and similarly C is shown in [](#fig:how2tern)c (25%).

:::{figure} ../figures/appendix/ternary.png
:name: fig:how2tern
:width: 100%

How to read a ternary diagram. The three apices are components A, B, C. A composition is plotted as the star. a) Shows the percentage of component A (60%). b) Shows the percentage of component B (15%) and c) shows the percentage of component C (25%).
:::

(app:qq)=
### Quantile-Quantile plots

When does a data set conform to a particular distribution? One way to assess this is through the use of *Quantile-quantile*, or Q-Q, plots (see {cite:t}`fisher1987` for a more complete discussion). In a Q-Q plot, data are graphed against the value expected from a particular distribution. The data $\zeta_i$ are plotted against a value $z_i$ that is expected from the distribution; data compatible with the chosen distribution plot along a line. First, we will develop the Q-Q plot for the uniform and exponential functions required for a Fisher distribution. Then we will explain how to make a Q-Q plot for a normal distribution.

:::{figure} ../figures/appendix/Ais.png
:name: fig:Ais
:width: 100%

a) Illustration of how the sorted data $\zeta_i$ divide the density curve into areas $A_i$ with an average area of $1/(N+1)$. b) The values of $z_i$ which divide the density function into equal areas $a_i=1/(N+1)$. c) Q-Q plot of $z$ and $\zeta$. [Figure from {cite:t}`tauxe1998`.]
:::

#### Q-Q plots for Fisher distributions

In order to make Q-Q plot for Fisher distributions, we proceed as follows ([](#fig:Ais)):

1. Sort the variable of interest $\zeta_i$ into ascending order so that $\zeta_1$ is the smallest and $\zeta_N$ is the largest.

2. If the data are represented by the underlying density function as in [](#fig:Ais)a, then the $\zeta_i$'s divide the curve into $(N+1)$ areas, $A_i$, the average value of which is $a=1/(N+1)$. If we assume a form for the density function of $\zeta_i$, we can calculate numbers $z_i$, that divide the theoretical distribution into areas $a_i$ each having an area $a$ (see [](#fig:Ais)b).

3. An approximate test for whether the data $\zeta_i$ are fit by a given distribution is to plot the pairs of points ($\zeta_i, z_i$), as shown in [](#fig:Ais)c. If the assumed distribution is appropriate, the data will plot as a straight line.

4. The density function $P$ is the distribution function $F$ times the area, as mentioned before. The $z_i$ are calculated as follows:

$$
F(z_i)=(i-\frac{1}{2})/n, \text{ where } i=1,\dots,n,
$$ (eq:Fz)

so that:

$$
z_i=F^{-1}((i-\frac{1}{2})/n), \text{ where } i=1,\dots,n,
$$ (eq:zi)

and where $F^{-1}$ is the inverse function to $F$. If the data are uniformly distributed (and constrained to lie between 0 and 1), then both $F(x)$ and $F^{-1}(x) =x$. For an exponential distribution $F(x)=1- e^{-x}$ and $F^{-1}(x)=-\text{ln}(1-x)$.

5. Finally, we can calculate parameters $M_u$ and $M_e$ which, when compared to critical values, allow rejection of the hypotheses of uniform and exponential distributions, respectively. To do this, we first calculate:

$$
D_N^+ = \text{maximum} [{i\over N} - F(x)],
$$ (eq:DNp)

and

$$
D_N^- = \text{maximum} [F(x) -{{(i-1)}\over N} ].
$$ (eq:DNn)

For a uniform distribution $F(x)=x$, so $M_u$ is calculated by first calculating $D_N^+$ as the maximum of $[i/N-\zeta_i]$ and $D_N^-$ as the maximum of $[\zeta_i-(i-1)/N]$. The Kuiper's statistic $V_n$ is $D_N^++D_N^-$ and $M_u$ is given by:

$$
M_u = V_n (\sqrt{N} - 0.567 + {1.623\over{\sqrt{N}}}),
$$ (eq:Mu)

(see {cite:t}`fisher1987`). A value of $M_u > 1.207$ can be grounds for rejecting the hypothesis of uniformity at the 95% level of certainty. Similarly, $D_N^+$ and $D_N^-$ can be calculated for the inclination data (using $\zeta_i=90-I_i$) as $[i/N-(1-e^{-\zeta_i})]$ and maximum of $[(1-e^{-\zeta_i})-(i-1)/N]$ respectively. The Kolmogorov-Smirnov statistic $D_n$ is the largest of the two. The test statistic for exponentially distributed data $M_e$ is given by:

$$
M_e = {(D_n - {0.2 \over{N}})} {( \sqrt N + 0.26 + {1\over {2\sqrt N} } )}.
$$ (eq:Me)

Values of $M_e$ larger than 1.094 allow rejection of the exponential hypothesis at the 95% level of confidence. If either $M_u$ or $M_e$ exceed the critical values, the hypothesis of a Fisher distribution can be rejected.

#### Q-Q plots for normal distributions

In order to calculate the appropriate values for $z_i$ assuming a normal distribution (see {cite:t}`abramowitz1970`):

1. For $i=1\rightarrow N$, calculate $p = {i\over {N+1}}$.

2. If $p>0.5$, then $q=1-p$; if $p<0.5$, then $q=p$.

3. Calculate the following for all $p\ne 0.5$:

$$
t=\sqrt{-2\ln(q)},
$$

and

$$
u=t-{ {(a_1+a_2t+a_3t^2)}\over { (1 +a_4t+a_5t^2+a_6t^3)}},
$$

where $a_1=2.515517, a_2=0.802853, a_3=0.010328, a_4=1.432788, a_5=0.189269, a_6=0.001388$.

4. If $p>0.5$, then $z_i=u$; if $p<0.5$, then $z_i=-u$.

5. If $p=0.5$, then $z_i=0$.

The values of $z_i$ calculated in this way for a simulated Gaussian distribution are plotted as the "normal quantile" data and will plot along a line if the data are in fact normally distributed. To test this in a more quantitative way, we can calculate $D_N^+$ and $D_N^-$ as follows:

1. Calculate the mean $\bar x$ and standard deviation $\sigma$ for the data.

2. Then calculate:

$$
p = {{x_i - \bar x}\over {\sqrt 2 \sigma}},
$$

and

$$
q = {1\over {1+{0.3275911|x|}}}.
$$

3. Substitute $q$ into the following expression (function 7.1.26 from {cite:t}`abramowitz1970`):

$$
\text{erf}(q) = 1-e^{-p^2} [ a_1q +a_2q^2 + a_3 q^3 + a_4 q^4+a_5q^5],
$$

where $a_1=0.254829592, a_2=-0.284496736, a_3=1.421413741$, and $a_5= 1.061405429$.

4. Change the sign of $\text{erf}(q)$ such that it has the same sign as $q$.

5. Substitute $F(x)=0.5(1+\text{erf}(q))$ into [Equation %s](#eq:DNp) and [Equation %s](#eq:DNn) in [](#app:qq) for $D_N^+$ and $D_N^-$ respectively. The Kolmogorov-Smirnov parameter $D$ (e.g., {cite:t}`fisher1987`) is the larger of $D_N^+$ or $D_N^-$.

6. The null hypothesis that a given data set is normally distributed can be rejected at the 95% level of confidence if $D$ exceeds a critical value $D_c$ given by $0.886/\sqrt{N}$.

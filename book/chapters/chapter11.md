---
title: "Chapter 11: Fisher Statistics"
label: chap:fisher
authors:
  - name: Lisa Tauxe
    affiliation: Scripps Institution of Oceanography, UC San Diego
numbering:
  enumerator: 11.%s
kernelspec:
  name: python3
  display_name: Python 3
---

# Fisher Statistics

**BACKGROUND:** read {cite}`taylor1982`, Chapters 1-5.

We have laid out the need for statistical analysis of paleomagnetic data in the preceding chapters. For instance, we require a method for determining a mean direction from a set of observations. Such a method should provide some measure of uncertainty in the mean direction. Additionally, we need methods for assessing the significance of field tests of paleomagnetic stability. In this chapter, we introduce basic statistical methods for analysis of directional data. It is sometimes said that statistical analyses are used by scientists in the same manner that a drunk uses a light pole: more for support than for illumination. Although this might be true, statistical analysis is fundamental to any paleomagnetic investigation. An appreciation of the basic statistical methods is required to understand paleomagnetism.

Most of the statistical methods used in paleomagnetism have direct analogies to "planar" statistics. We begin by reviewing the basic properties of the normal distribution. This distribution is used for statistical analysis of a wide variety of observations and will be familiar to many readers. We then tackle statistical analysis of directional data by analogy with the normal distribution. Although the reader might not follow all aspects of the mathematical formalism, this is no cause for alarm. Graphical displays of functions and examples of statistical analysis will provide the more important intuitive appreciation for the statistics.

## The Normal Distribution

Any statistical method for determining a mean (and confidence limit) from a set of observations is based on a probability density function. This function describes the distribution of observations for a hypothetical, infinite set of observations called a population. The Gaussian probability density function (normal distribution) has the familiar bell-shaped form shown in [Figure %s](#fig:gauss)a. The meaning of the probability density function $f(z)$ is that the proportion of observations within an interval of incremental width $dz$ centered on $z$ is $f(z) dz$.

:::{figure} ../figures/chapter11/gauss.png
:name: fig:gauss
:width: 100%

a) The Gaussian probability density function (normal distribution, [Equation %s](#eq:normal)). The proportion of observations within an interval $dz$ centered on $z$ is $f(z)dz$. b) Histogram of 1000 measurements of bed thickness in a sedimentary formation. Also shown is the smooth curve of a normal distribution with a mean of 10 and a standard deviation of 3. c) Histogram of the means from 100 repeated sets of 1000 measurements from the same sedimentary formation. The distribution of the means is much tighter. d) Histogram of the variances ($s^2$) from the same set of experiments as in c). The distribution of variances is not bell shaped; it is $\chi^2$.
:::

The Gaussian probability density function is given by:

$$
f(z) = \frac{1}{\sigma \sqrt{2\pi}} \exp \left( \frac{-z^2}{2} \right),
$$ (eq:normal)

where

$$
z = \frac{x - \mu}{\sigma}.
$$

$x$ is the variable measured, $\mu$ is the true mean, and $\sigma$ is the standard deviation. The parameter $\mu$ determines the value of $x$ about which the distribution is centered, while $\sigma$ determines the width of the distribution about the true mean. By performing the required integrals (computing area under curve $f(z)$), it can be shown that 68% of the readings in a normal distribution are within $\sigma$ of $\mu$, while 95% are within 1.96$\sigma$ of $\mu$.

The usual situation is that one has made a finite number of measurements of a variable $x$. In the literature of statistics, this set of measurements is referred to as a sample. Let us say that we made 1000 measurements of some parameter, say bed thickness (in cm) in a particular sedimentary formation. We plot these in histogram form in [Figure %s](#fig:gauss)b.

By using the methods of Gaussian statistics, one is supposing that the observed sample has been drawn from a population of observations that is normally distributed. The true mean and standard deviation of the population are, of course, unknown. But the following methods allow estimation of these quantities from the observed sample. A normal distribution can be characterized by two parameters, the mean ($\mu$) and the variance $\sigma^2$. How to estimate the parameters of the underlying distribution is the art of statistics. We all know that the arithmetic mean of a batch of data $\bar x$ drawn from a normal distribution is calculated by:

$$
\bar{x} = \frac{1}{N} \sum_{i=1}^N x_i,
$$

where $N$ is the number of measurements and $x_i$ is an individual measurement.

The mean estimated from the data shown in [Figure %s](#fig:gauss)b is 10.09. If we had measured an infinite number of bed thicknesses, we would have gotten the bell curve shown as the dashed line and calculated a mean of 10.

The "spread" in the data is characterized by the *variance* $\sigma^2$. Variance for normal distributions can be estimated by the statistic $s^2$:

$$
s^2 = \frac{1}{N-1} \sum_{i=1}^N (x_i - \bar{x})^2.
$$ (eq:sigma)

In order to get the units right on the spread about the mean (cm -- not cm$^2$), we have to take the square root of $s^2$. The statistic $s$ gives an estimate of the standard deviation $\sigma$ and is the bounds around the mean that includes 68% of the values. The 95% confidence bounds are given by 1.96$s$ (this is what a "2-$\sigma$ error" is), and should include 95% of the observations. The bell curve shown in [Figure %s](#fig:gauss)b has a $\sigma$ (standard deviation) of 3, while the $s$ is 2.97.

If you repeat the bed measuring experiment a few times, you will never get exactly the same measurements in the different trials. The mean and standard deviations measured for each trial then are "sample" means and standard deviations. If you plotted up all those sample means, you would get another normal distribution whose mean should be pretty close to the true mean, but with a much more narrow standard deviation. In [Figure %s](#fig:gauss)c we plot a histogram of means from 100 such trials of 1000 measurements each drawn from the same distribution of $\mu = 10, \sigma = 3$. In general, we expect the standard deviation of the means (or *standard error of the mean*, $s_m$) to be related to $s$ by

$$
s_m = \frac{s}{\sqrt{N_{trials}}}.
$$

What if we were to plot up a histogram of the estimated variances as in [Figure %s](#fig:gauss)c? Are these also normally distributed? The answer is no, because variance is a squared parameter relative to the original units. In fact, the distribution of variance estimates from normal distributions is expected to be *chi-squared* ($\chi^2$). The width of the $\chi^2$ distribution is also governed by how many measurements were made. The so-called number of *degrees of freedom* ($\nu$) is given by the number of measurements made minus the number of measurements required to make the estimate, so $\nu$ for our case is $N-1$. Therefore we expect the variance estimates to follow a $\chi^2$ distribution with $N-1$ degrees of freedom of $\chi^2_{\nu}$.

The estimated standard error of the mean, $s_m$, provides a confidence limit for the calculated mean. Of all the possible samples that can be drawn from a particular normal distribution, 95% have means, $\bar x$, within 2$s_m$ of $\bar x$. (Only 5% of possible samples have means that lie farther than 2$s_m$ from $\bar x$.) Thus the 95% confidence limit on the calculated mean, $\bar x$, is 2$s_m$, and we are 95% certain that the true mean of the population from which the sample was drawn lies within 2$s_m$ of $\bar x$. The estimated standard error of the mean, $s_m$ decreases 1/$\sqrt{N}$. Larger samples provide more precise estimations of the true mean; this is reflected in the smaller confidence limit with increasing $N$.

We often wish to consider ratios of variances derived from normal distributions (for example to decide if the data are more scattered in one data set relative to another). In order to do this, we must know what ratio would be expected from data sets drawn from the same distributions. Ratios of such variances follow a so-called $F$ distribution with $\nu_1$ and $\nu_2$ degrees of freedom for the two data sets. This is denoted $F[\nu_1,\nu_2]$. Thus if the ratio $F$, given by:

$$
F = \frac{s_1^2}{s_2^2},
$$

is greater than the 5% critical value of $F[\nu_1,\nu_2]$ (check the F distribution tables in your favorite statistics book or online), the hypothesis that the two variances are the same can be rejected at the 95% level of confidence.

A related test to the $F$ test is Student's $t$-test. This test compares differences in normal data sets and provides a means for judging their significance. Given two sets of measurements of bed thickness, for example in two different sections, the $t$ test addresses the likelihood that the difference between the two means is significant at a given level of probability. If the estimated means and standard deviations of the two sets of $N_1$ and $N_2$ measurements are $\bar x_1,\sigma_1$ and $\bar x_2,\sigma_2$ respectively, the $t$ statistic can be calculated by:

$$
t = \frac{\bar x_1 - \bar x_2}{\sigma_{(x_1-x_2)}},
$$

where

$$
\sigma_{(x_1-x_2)} = \sqrt{\frac{(N_1-1)\sigma_1^2 + (N_2 -1)\sigma_2^2}{\nu} \left(\frac{1}{N_1} + \frac{1}{N_2}\right)}.
$$

Here $\nu = N_1 + N_2 - 2$. If this number is below a critical value for $t$ then the null hypothesis that the two sets of data are the same cannot be rejected at a given level of confidence. The critical value can be looked up in $t$-tables in your favorite statistics book or online.

## Statistics of Vectors

We turn now to the trickier problem of sets of measured vectors. We will consider the case in which all vectors are assumed to have a length of one, i.e., these are unit vectors. Unit vectors are just "directions". Paleomagnetic directional data are subject to a number of factors that lead to scatter. These include:

1. uncertainty in the measurement caused by instrument noise or specimen alignment errors,
2. uncertainties in sample orientation,
3. uncertainty in the orientation of the sampled rock unit,
4. variations among samples in the degree of removal of a secondary component,
5. uncertainty caused by the process of magnetization,
6. secular variation of the Earth's magnetic field, and
7. lightning strikes.

Some of these sources of scatter (e.g., items 1, 2 and perhaps 6 above) lead to a symmetric distribution about a mean direction. Other sources of scatter contribute to distributions that are wider in one direction than another. For example, in the extreme case, item four leads to a girdle distribution whereby directions are smeared along a great circle. It would be handy to be able to calculate a mean direction for data sets and to quantify the scatter.

:::{figure} ../figures/chapter11/fisher.png
:name: fig:fisher
:width: 100%

Hypothetical data sets drawn from Fisher distributions with vertical true directions with $\kappa$ = 5 (a-c), $\kappa$ = 10 (d-f), $\kappa$ = 50 (g-i). Estimated $\bar D, \bar I, \kappa, \alpha_{95}$ shown in insets.
:::

In order to calculate mean directions with confidence limits, paleomagnetists rely heavily on the special statistics known as *Fisher statistics* {cite}`fisher1953`, which were developed for assessing dispersion of unit vectors on a sphere. It is applicable to directional data that are dispersed in a symmetric manner about the true direction. We show some examples of such data in [Figure %s](#fig:fisher) with varying amounts of scatter from highly scattered in the top row to rather concentrated in the bottom row. All the data sets were drawn from a Fisher distribution with a vertical true direction.

In most instances, paleomagnetists assume a Fisher distribution for their data because the statistical treatment allows calculation of confidence intervals, comparison of mean directions, comparison of scatter, etc. The average inclination, calculated as the arithmetic mean of the inclinations, will never be vertical unless all the inclinations are vertical. In the following, we will demonstrate the proper way to calculate mean directions and confidence regions for directional data that are distributed in the manner shown in [Figure %s](#fig:fisher). We will also briefly describe several useful statistical tests that are popular in the paleomagnetic literature.

(sect:fisher)=
### Estimation of Fisher Statistics

R. A. Fisher developed a probability density function applicable to many paleomagnetic directional data sets, known as the Fisher distribution {cite}`fisher1953`. In Fisher statistics each direction is given unit weight and is represented by a point on a sphere of unit radius. The Fisher distribution function $P_{dA}(\alpha)$ gives the probability per unit angular area of finding a direction within an angular area, $dA$, centered at an angle $\alpha$ from the true mean. The angular area, $dA$, is expressed in steradians, with the total angular area of a sphere being $4\pi$ steradians. Directions are distributed according to the Fisher probability density, given by:

$$
P_{dA}(\alpha) = \frac{\kappa}{4\pi \sinh \kappa} \exp (\kappa \cos \alpha),
$$ (eq:fishdis)

where $\alpha$ is the angle between the unit vector and the true direction and $\kappa$ is a *precision parameter* such that as $\kappa \to \infty$, dispersion goes to zero.

We can see in [Figure %s](#fig:P)a the probability of finding a direction within an angular area $dA$ centered $\alpha$ degrees away from the true mean for different values of $\kappa$. $\kappa$ is a measure of the concentration of the distribution about the true mean direction. The larger the value of $\kappa$, the more concentrated the direction; $\kappa$ is 0 for a distribution of directions that is uniform over the sphere and approaches $\infty$ for directions concentrated at a point.

:::{figure} ../figures/chapter11/P.png
:name: fig:P
:width: 100%

a) Probability of finding a direction within an angular area, $dA$ centered at an angle $\alpha$ from the true mean. b) Probability of finding a direction at angle $\alpha$ away from the true mean direction.
:::

If $\phi$ is taken as the azimuthal angle about the true mean direction, the probability of a direction within an angular area, $dA$, can be expressed as

$$
P_{dA}(\alpha) dA = P_{dA}(\alpha) \sin (\alpha) d\alpha d\phi.
$$

The $\sin \alpha$ term arises because the area of a band of width $d\alpha$ varies as $\sin \alpha$. It should be understood that the Fisher distribution is normalized so that

$$
\int_{\phi=0}^{2\pi} \int_{\alpha=0}^{\pi} P_{dA}(\alpha) \sin (\alpha) d\alpha d\phi = 1.
$$ (eq:fishnorm)

[Equation %s](#eq:fishnorm) simply indicates that the probability of finding a direction somewhere on the unit sphere must be unity. The probability $P_{d\alpha}$ of finding a direction in a band of width $d\alpha$ between $\alpha$ and $\alpha+d\alpha$ is given by:

$$
P_{d\alpha}(\alpha) = \int_{\phi=0}^{2\pi} P_{dA}(\alpha) dA = 2\pi P_{dA}(\alpha) \sin (\alpha) d\alpha
$$

$$
= P_{dA}(\alpha) \sin \alpha = \frac{\kappa}{2\pi \sinh \kappa} \exp (\kappa \cos \alpha) \sin \alpha.
$$ (eq:fishpde)

This probability (for $\kappa = 5, 10, 50, 100$) is shown in [Figure %s](#fig:P)b where the effect of the $\sin \alpha$ term is apparent. [Equation %s](#eq:fishdis) for the Fisher distribution function suggests that declinations are symmetrically distributed about the mean. In "data" coordinates, this means that the declinations are uniformly distributed from 0 $\rightarrow$ 360$^{\circ}$. Furthermore, the probability $P_{\alpha}$ of finding a direction of $\alpha$ away from the mean decays exponentially.

Because the intensity of the magnetization has little to do with the validity of the measurement (except for very weak magnetizations), it is customary to assign unit length to all directions. The mean direction is calculated by first converting the individual moment directions ($m_i$) (see [Figure %s](#fig:vecsum)), which may be expressed as declination and inclination ($D_i,I_i$), to Cartesian coordinates ($x_1,x_2,x_3$) by the methods given in Chapter 2. Following the logic for vector addition explained in Appendix A, the length of the vector sum, or resultant vector $R$, is given by:

$$
R^2 = \left(\sum_{i} x_{1i}\right)^2 + \left(\sum_i x_{2i}\right)^2 + \left(\sum_i x_{3i}\right)^2,
$$ (eq:R)

The relationship of $R$ to the $N$ individual unit vectors is shown in [Figure %s](#fig:vecsum). $R$ is always $<N$ and approaches $N$ only when the vectors are tightly clustered. The mean direction components are given by:

$$
\bar x_1 = \frac{1}{R} \left(\sum_i x_{1i}\right); \quad \bar x_2 = \frac{1}{R} \left(\sum_i x_{2i}\right); \quad \bar x_3 = \frac{1}{R} \left(\sum_i x_{3i}\right).
$$ (eq:xbar)

These Cartesian coordinates can, of course, be converted back to geomagnetic elements ($\bar D, \bar I$) by the familiar method described in Chapter 2.

:::{figure} ../figures/chapter11/vecsum.png
:name: fig:vecsum
:width: 70%

Vector addition of eight unit vectors ($m_i$) to yield resultant vector $R$. [Figure redrawn from {cite}`butler1992`.]
:::

Having calculated the mean direction, the next objective is to determine a statistic that can provide a measure of the dispersion of the population of directions from which the sample data set was drawn. One measure of the dispersion of a population of directions is the precision parameter, $\kappa$. From a finite sample set of directions, $\kappa$ is unknown, but a best estimate of $\kappa$ can be calculated by

$$
\kappa \simeq k = \frac{N-1}{N-R},
$$ (eq:k)

where $N$ is the number of data points. Using this estimate of $\kappa$, we estimate the circle of 95% confidence ($p=0.05$) about the mean, $\alpha_{95}$, by:

$$
\alpha_{95} = \cos^{-1}\left[1 - \frac{N-R}{R}\left[\left(\frac{1}{p}\right)^{\frac{1}{N-1}}-1\right]\right].
$$ (eq:a95)

In the classic paleomagnetic literature, $\alpha_{95}$ was further approximated by:

$$
\alpha_{95}' \simeq \frac{140}{\sqrt{k N}},
$$

which is reliable for $k$ larger than about 25 (see {cite}`tauxe1991`). By direct analogy with Gaussian statistics ([Equation %s](#eq:sigma)), the angular variance of a sample set of directions is:

$$
S^2 = \frac{1}{N-1} \sum_{i=1}^N \Delta_i^2,
$$ (eq:S)

where $\Delta_i$ is the angle between the $i^{th}$ direction and the calculated mean direction. The estimated circular (or angular) standard deviation is $S$, which can be approximated by:

$$
CSD \simeq \frac{81}{\sqrt{k}},
$$ (eq:csd)

which is the circle containing ~68% of the data.

Some practitioners use the statistic $\delta$ given by:

$$
\delta = \cos^{-1} \left(\frac{R}{N}\right),
$$ (eq:del)

because of its ease of calculation and the intuitive appeal (e.g., [Figure %s](#fig:vecsum)) that $\delta$ decreases as $R$ approaches $N$. In practice, when $N > \sim 10\text{--}20$, CSD and $\delta$ are close to equal.

When we calculate the mean direction, a dispersion estimate, and a confidence limit, we are supposing that the observed data came from random sampling of a population of directions accurately described by the Fisher distribution. But we do not know the true mean of that Fisherian population, nor do we know its precision parameter $\kappa$. We can only estimate these unknown parameters. The calculated mean direction of the directional data set is the best estimate of the true mean direction, while $k$ is the best estimate of $\kappa$. The confidence limit $\alpha_{95}$ is a measure of the precision with which the true mean direction has been estimated. One is 95% certain that the unknown true mean direction lies within $\alpha_{95}$ of the calculated mean. The obvious corollary is that there is a 5% chance that the true mean lies more than $\alpha_{95}$ from the calculated mean.

### Some Illustrations

Having buried the reader in mathematical formulations, we present the following illustrations to develop some intuitive appreciation for the statistical quantities. One essential concept is the distinction between statistical quantities calculated from a directional data set and the unknown parameters of the sampled population.

Consider the various sets of directions plotted as equal area projections (see Chapter 2) in [Figure %s](#fig:fisher). These are all synthetic data sets drawn from Fisher distributions with means of a single, vertical direction. Each of the three diagrams in a row is a replicate sample from the same distribution. The top row were all drawn from a distribution with $\kappa = 5$, the middle with $\kappa = 10$ and the bottom row with $\kappa = 50$. For each synthetic data set, we estimated $\bar D, \bar I, \kappa$ and $\alpha_{95}$ (shown as insets to the equal area diagrams).

There are several important observations to be taken from these examples. Note that the calculated mean direction is never exactly the true mean direction ($I$ = +90$^{\circ}$). The calculated mean inclination $\bar I$ varies from 78.6$^{\circ}$ to 89.3$^{\circ}$, and the mean declinations fall within all quadrants of the equal-area projection. The calculated mean direction thus randomly dances about the true mean direction and deviates from the true mean by between 0.7$^{\circ}$ and 11.4$^{\circ}$. The calculated $k$ statistic varies considerably among replicate samples as well. The variation of $k$ and differences in angular variance of the data sets with the same underlying distribution are simply due to the vagaries of random sampling.

The confidence limit $\alpha_{95}$ varies from 19.9$^{\circ}$ to 4.3$^{\circ}$ and is shown by the circle surrounding the calculated mean direction (shown as a triangle). For these directional data sets, only one ([Figure %s](#fig:fisher)e) has a calculated mean that is more than $\alpha_{95}$ from the true mean. However, if 100 such synthetic data sets had been analyzed, on average five would have a calculated mean direction removed from the true mean direction by more than the calculated confidence limit $\alpha_{95}$. That is, the true mean direction would lie outside the circle of 95% confidence, on average, in 5% of the cases.

It is also important to appreciate which statistical quantities are fundamentally dependent upon the number of observations $N$. Neither the $k$ value ([Equation %s](#eq:k)) nor the estimated angular deviation CSD ([Equation %s](#eq:csd)) is fundamentally dependent upon $N$. These statistical quantities are estimates of the intrinsic dispersion of directions in the Fisherian population from which the data set was sampled. Because that dispersion is not affected by the number of times the population is sampled, the calculated statistics estimating that dispersion should not depend fundamentally on the number of observations $N$. However, the confidence limit $\alpha_{95}$ should depend on $N$; the more individual measurements there are in our sample, the greater must be the precision (and accuracy) in estimating the true mean direction. This increased precision should be reflected by a decrease in $\alpha_{95}$ with increasing $N$. Indeed [Equation %s](#eq:a95) indicates that $\alpha_{95}$ depends approximately on $1/\sqrt{N}$.

[Figure %s](#fig:a95-csd) illustrates these dependencies of calculated statistics on number of directions in a data set. This diagram was constructed as follows:

1. We drew a synthetic data set of $N=30$ from a Fisher distribution with a $\kappa$ of 29.2 (equivalent to a circular standard deviation $S$ of 15$^{\circ}$).
2. Starting with the first four directions in the synthetic data set, a subset of $N$ = 4 was used to calculate $k$, CSD and $\delta$ using [Equations %s](#eq:k), [%s](#eq:csd), and [%s](#eq:del) respectively. In addition, $\alpha_{95}$ (using [Equation %s](#eq:a95)) was calculated. Resulting values of CSD, $\delta$ and $\alpha_{95}$ are shown in [Figure %s](#fig:a95-csd) as a function of $N$.
3. For each succeeding value of $N$ in [Figure %s](#fig:a95-csd), the next direction from the $N$ = 30 synthetic data set was added to the previous subset of directions, continuing until the full $N$ = 30 synthetic data set was used.

The effects of increasing $N$ are readily apparent in [Figure %s](#fig:a95-csd) in which we show a comparison of the two estimates of $S$, CSD and $\delta$. Although not fundamentally dependent upon $N$, in practice the estimated angular standard deviation, CSD, deviates from $S$ for values of $N < 15$, only approaching the correct value when $N \ge 15$. As expected, the calculated confidence limit $\alpha_{95}$ decreases approximately as $1/\sqrt{N}$, showing a dramatic decrease in the range $4 < N < 10$ and more gradual decrease for $N > 10$.

:::{figure} ../figures/chapter11/a95-csd.png
:name: fig:a95-csd
:width: 70%

Dependence of estimated angular standard deviation, CSD and $\delta$, and confidence limit, $\alpha_{95}$, on the number of directions in a data set. An increasing number of directions were selected from a Fisherian sample of directions with angular standard deviation $S$ = 15$^{\circ}$ ($\kappa$ = 29.2), shown by the horizontal line.
:::

If directions are converted to VGPs as outlined in Chapter 2, the transformation distorts a rotationally symmetric set of data into an elliptical distribution. The associated $\alpha_{95}$ may no longer be appropriate. {cite}`cox1960` suggested the following for 95% confidence regions in VGPs. Ironically, it is more likely that the VGPs are spherically symmetric implying that most sets of directions are not!

$$
dm = \alpha_{95} \frac{\cos \lambda}{\cos \bar I}, \quad dp = \frac{1}{2} \alpha_{95} (1 + 3 \sin^2 \lambda),
$$ (eq:dpdm)

where $dm$ is the semi-axis parallel to the meridians (lines of longitude), $dp$ is the semi-axis parallel to the parallels (lines of latitude), and $\lambda$ is the site paleolatitude.

## Significance Tests

The Fisher distribution allows us to ask a number of questions about paleomagnetic data sets, such as:

1. Is a given set of directions random? This is the question that we ask when we perform a conglomerate test (Chapter 9).

2. Is one data set better grouped than another as in the fold test from Chapter 9.

3. Is the mean direction of a given (Fisherian) data set different from some known direction? This question comes up when we compare a given data set with, for example, the directions of the present or GAD field.

4. Are two (Fisherian) data sets different from each other? For example, are the normal directions and the antipodes of the reversed directions the same for a given data set?

5. If a given site has some samples that allow only the calculation of a best-fit plane and not a directed line, what is the site mean direction that combines the best-fit lines and planes (see Chapter 9)?

In the following discussion, we will briefly summarize ways of addressing these issues using Fisher techniques. There are two fundamental principles of statistical significance tests that are important to the proper interpretation:

1. Tests are generally made by comparing an observed sample with a *null hypothesis*. For example, in comparing two mean paleomagnetic directions, the null hypothesis is that the two mean directions are separate samples from the same population of directions. (This is the same as saying that the samples were not, in fact, drawn from different populations with distinct true mean directions.) Significance tests do not disprove a null hypothesis but only show that observed differences between the sample and the null hypothesis are unlikely to have occurred because of sampling limitations. In other words, there is probably a real difference between the sample and the null hypothesis, indicating that the null hypothesis is probably incorrect.

2. Any significance test must be applied by using a level of significance. This is the probability level at which the differences between a set of observations and the null hypothesis may have occurred by chance. A commonly used significance level is 5%. In Gaussian statistics, when testing an observed sample mean against a hypothetical population mean $\mu$ (the null hypothesis), there is only a 5% chance that $\bar x$ is more than 2$\sigma_m$ from the mean, $\mu$, of the sample. If $\bar x$ differs from $\mu$ by more than 2$s$, $\bar x$ is said to be "statistically different from $\mu$ at the 5% level of significance," using proper statistical terminology. However, the corollary of the actual significance test is often what is reported by statements such as "$\bar x$ is distinct from $\mu$ at the 95% confidence level." The context usually makes the intended meaning clear, but be careful to practice safe statistics.

An important sidelight to this discussion of level of significance is that too much emphasis is often put on the 5% level of significance as a magic number. Remember that we are often performing significance tests on data sets with a small number of observations. Failure of a significance test at the 5% level of significance means only that the observed differences between sample and null hypothesis cannot be shown to have a probability of chance occurrence that is > 5%. This does not mean that the observed differences are unimportant. Indeed the observed differences might be significant at a marginally higher level of significance (for instance, 10%) and might be important to the objective of the paleomagnetic investigation.

Significance tests for use in paleomagnetism were developed in the 1950s by G.S. Watson and E.A. Irving. These versions of the significance tests are fairly simple, and an intuitive appreciation of the tests can be developed through a few examples. Because of their simplicity and intuitive appeal, we investigate these "traditional" significance tests in the development below. However, many of these tests have been updated using advances in statistical sampling theory. These will be discussed in Chapter 12. While they are technically superior to the traditional significance tests, they are more complex and less intuitive than the traditional tests.

(sect:Ro)=
### Watson's Test for Randomness

{cite}`watson1956` demonstrated how to test a given directional data set for randomness. His test relies on the calculation of $R$ given by [Equation %s](#eq:R). Because $R$ is the length of the resultant vector, randomly directed vectors will have small values of $R$, while, for less scattered directions, $R$ will approach $N$. {cite}`watson1956` defined a parameter $R_o$ that can be used for testing the randomness of a given data set. If the value of $R$ exceeds $R_o$, the null hypothesis of total randomness can be rejected at a specified level of confidence. If $R$ is less than $R_o$, randomness cannot be rejected. Watson calculated the value of $R_o$ for a range of $N$ for the 95% and 99% confidence levels. {cite}`watson1956` also showed how to estimate $R_o$ by:

$$
R_o = \sqrt{\frac{7.815 \cdot N}{3}}.
$$ (eq:Ro)

The estimation works well for $N > 10$, but is somewhat biased for smaller data sets. The critical values of $R$ for $5 < N < 20$ from {cite}`watson1956` are listed for convenience in [Table %s](#tab:Ro).

(tab:Ro)=
:::{table} Critical values of $R$ for Watson's test for randomness at the 95% confidence level (from Watson, 1956).
:name: tab:Ro

| $N$ | $R_o$ (95%) |
|-----|-------------|
| 5   | 3.04        |
| 6   | 3.35        |
| 7   | 3.63        |
| 8   | 3.89        |
| 9   | 4.12        |
| 10  | 4.34        |
| 11  | 4.54        |
| 12  | 4.73        |
| 13  | 4.91        |
| 14  | 5.08        |
| 15  | 5.24        |
| 16  | 5.40        |
| 17  | 5.55        |
| 18  | 5.69        |
| 19  | 5.83        |
| 20  | 5.96        |

:::

The test for randomness is particularly useful for determining if, for example, the directions from a given site are randomly oriented (the data for the site should therefore be thrown out). Also, one can determine if directions from the conglomerate test are random or not (see Chapter 9).

### Comparison of Precision

In the fold test (or bedding-tilt test), one examines the clustering of directions before and after performing structural corrections. If the clustering improves on structural correction, the conclusion is that the ChRM was acquired prior to folding and therefore "passes the fold test". The appropriate significance test determines whether the improvement in clustering is statistically significant. Here we will discuss a very quick, back of the envelope test for this proposed by {cite}`mcelhinny1964`. This form of the fold test is not used much anymore (see {cite}`mcfadden1981`), but serves as a quick and intuitively straight-forward introduction to the subject.

Consider two directional data sets, one with $N_1$ directions and $k_1$, and one with $N_2$ directions and $k_2$. If we assume (null hypothesis) that these two data sets are samples of populations with the same $k$, the ratio $k_1/k_2$ is expected to vary because of sampling errors according to

$$
\frac{k_1}{k_2} = \frac{\text{var}[2(N_2 -1)]}{\text{var}[2(N_1 -1)]},
$$ (eq:k1-k2)

where $\text{var}[2(N_2 -1)]$ and $\text{var}[2(N_1 -1)]$ are variances with $2(N_2-1)$ and $2(N_1-1)$ degrees of freedom. This ratio should follow the $F$-distribution if the assumption of common $\kappa$ is correct. Fundamentally, one expects this ratio to be near 1.0 if the two samples were, in fact, selections from populations with common $\kappa$. The $F$-distribution tables indicate how far removed from 1.0 the ratio may be before the deviation is significant at a chosen probability level. If the observed ratio in [Equation %s](#eq:k1-k2) is far removed from 1.0, then it is highly unlikely that the two data sets are samples of populations with the same $\kappa$. In that case, the conclusion is that the difference in the $\kappa$ values is significant and the two data sets were most likely sampled from populations with different $\kappa$.

As applied to the fold test, one examines the ratio of $k$ after tectonic correction ($k_a$) to $k$ before tectonic correction ($k_b$). The significance test for comparison of precisions determines whether $k_a/k_b$ is significantly removed from 1.0. If $k_a/k_b$ exceeds the value of the $F$-distribution for the 5% significance level, there is less than a 5% chance that the observed increase in $k$ resulting from the tectonic correction is due only to sampling errors. There is 95% probability that the increase in $k$ is meaningful and the data set after tectonic correction is a sample of a population with $k$ larger than the population sampled before tectonic correction. Such a result constitutes a "statistically significant passage of the fold test."

:::{figure} ../figures/chapter11/twosets.png
:name: fig:twosets
:width: 100%

a) Equal area projections of declinations and inclinations of two hypothetical data sets. b) Fisher means and circles of confidence from the data sets in a). c) Distribution of $V_w$ for simulated Fisher distributions with the same $N$ and $\kappa$ as the two shown in a). The dashed line is the upper bound for the smallest 95% of the $V_w$s calculated for the simulations ($V_{crit}$). The solid vertical line is the $V_w$ calculated for the two data sets. According to this test, the two data sets do not have a common mean, despite their overlapping confidence ellipses.
:::

### Comparing Known and Estimated Directions

The calculation of confidence regions for paleomagnetic data is largely motivated by a need to compare estimated directions with either a known direction (for example, the present field) or another estimated direction (for example, that expected for a particular paleopole, the present field or a GAD field). Comparison of a paleomagnetic data set with a given direction is straight-forward using Fisher statistics. If the known test direction lies outside the confidence interval computed for the estimated direction, then the estimated and known directions are different at the specified confidence level.

:::{figure} ../figures/chapter11/lnp.png
:name: fig:lnp
:width: 100%

Examples of demagnetization data from a site whose mean is partially constrained by a great circle. The best-fit great circle and six directed lines allow a mean (diamond) and associated $\alpha_{95}$ to be calculated using the method of {cite}`mcfadden1988`. Demagnetization data for two of the directed lines are shown at the top of the diagram while those for the great circle are shown at the bottom. [Data from {cite}`tauxe2003b`.]
:::

### Comparing Two Estimated Directions

The case in which we are comparing two Fisher distributions can also be relatively straight forward. If the two confidence circles do not overlap, the two directions are different at the specified (or more stringent) level of certainty. When one confidence region includes the mean of the other set of directions, the difference in directions is not significant.

The situation becomes a little more tricky when the data sets are as shown in [Figure %s](#fig:twosets)a. The Fisher statistics for the two data sets are:

| $i$ | symbol | $\bar D$ | $\bar I$ | $N$ | $R$ | $k$ | $\alpha_{95}$ |
|-----|--------|----------|----------|-----|-----|-----|---------------|
| 1 | spades | 38.0 | 45.7 | 20 | 18.0818 | 9.9 | 10.9 |
| 2 | hearts | 16.9 | 45.2 | 20 | 19.0899 | 20.9 | 7.3 |

As shown in the equal area projection in [Figure %s](#fig:twosets)b, the two $\alpha_{95}$s overlap, but neither includes the mean of the other. This sort of "grey zone" case has been addressed by many workers.

The most common way of testing the significance of two sets of directions is a simple $F$ test, proposed by {cite}`watson1956b`. Consider two directional data sets: one has $N_1$ directions (described by unit vectors) yielding a resultant vector of length $R_1$; the other has $N_2$ directions yielding resultant $R_2$. The statistic

$$
F = (N - 2) \frac{(R_1 + R_2 - R)}{(N - R_1 - R_2)},
$$ (eq:twoF)

must be determined, where $N = N_1 + N_2$ and $R$ is the resultant of all $N$ individual directions. This $F$ statistic is compared with tabulated values for 2 and 2($N$-2) degrees of freedom. If the observed $F$ statistic exceeds the tabulated value at the chosen significance level, then these two mean directions are different at that level of significance.

The tabulated $F$-distribution indicates how different two sample mean directions can be (at a chosen probability level) because of sampling errors. If the calculated mean directions are very different but the individual directional data sets are well grouped, intuition tells us that these mean directions are distinct. The mathematics described above should confirm this intuitive result. With two well-grouped directional data sets with very different means, $(R_1 + R_2) >> R$, $R_1 \rightarrow N_1$, and $R_2 \rightarrow N_2$, so that $(R_1 + R_2) \rightarrow N$. With these conditions, the $F$ statistic given by [Equation %s](#eq:twoF) will be large and will easily exceed the tabulated value. So this simple intuitive examination of [Equation %s](#eq:twoF) yields a sensible result.

An alternative, and in many ways superior, statistic ($V_w$) was proposed by {cite}`watson1983` (see Appendix E for details). $V_w$ was posed as a test statistic that increases with increasing difference between the mean directions of the two data sets. Thus, the null hypothesis that two data sets have a common mean direction can be rejected if $V_w$ exceeds some critical value which can be determined through what is called *Monte Carlo simulation*. The technique gets its name from a famous gambling locale because we use randomly drawn samples ("cards") from specified distributions ("decks") to see what can be expected from chance. What we want to know is the probability that two data sets (hands of cards?) drawn from the same underlying distribution would have a given $V_w$ statistic just from chance.

We proceed as follows:

1. Calculate the $V_w$ statistic for the data sets. [The $V_w$ for the two data sets shown in [Figure %s](#fig:twosets)a is 8.5.]

2. In order to determine the critical value for $V_w$, we draw two Fisher distributed data sets with dispersions of $k_1$ and $k_2$ and $N_1, N_2$, but having a common true direction.

3. We then calculate $V_w$ for these simulated data sets.

4. Repeat the simulation some large number of times (say 1000). This defines the distribution of $V_w$s that you would get from chance by "sampling" distributions with the same direction.

5. Sort the $V_w$s in order of increasing size. The critical value of $V_w$ at the 95% level of confidence is the 950$^{th}$ simulated $V_w$.

The $V_w$s simulated for two distributions with the same $\kappa$ and $N$ as our example data sets but drawn from distributions with the same mean are plotted as a cumulative distribution function in [Figure %s](#fig:twosets)c with the bound containing the lowermost 95% of the simulations shown as a dashed line at 6.2. The value of 8.5, calculated for the data set is shown as a heavy vertical line and is clearly larger than 95% of the simulated populations. This simulation therefore supports the suggestion that the two data sets do not have a common mean at the 95% level of confidence.

This test can be applied to the two polarities in a given data collection to see if they are antipodal. In this case, one would take the antipodes of one of the data sets before calculating $V_w$. Such a test would be a Fisherian form of the *reversals test*.

### Combining Directions and Great Circles

Consider the demagnetization data shown in [Figure %s](#fig:lnp) of various specimens from a certain site. Best-fit lines from the data for the two specimens at the top of the diagram are calculated using principal component analysis (Chapter 9). The data from the specimen shown at the bottom of the diagram track along a great circle path and can be used to find the pole to the best-fit plane calculated also as in Chapter 9. {cite}`mcfadden1988` described a method for estimating the mean direction (diamond in central equal area plot) and the $\alpha_{95}$ from sites that mixes planes (great circles on an equal area projection) and directed lines (see Appendix D). The key to their method is to find the direction within each plane that gives the tightest grouping of directions. Then "regular" Fisher statistics can be applied.

## Inclination Only Data

A different problem arises when only the inclination data are available as in the case of unoriented drill cores. Cores can be drilled and arrive at the surface in short, unoriented pieces. Specimens taken from such core material will be oriented with respect to the vertical, but the declination data are unknown. It is often desirable to estimate the true Fisher inclination of data sets having only inclination data, but how to do this is not obvious. Consider the data in [Figure %s](#fig:incfish). The true Fisher mean declination and inclination are shown by the triangle. If we had only the inclination data and calculated a Gaussian mean ($< I >$), the estimate would be too shallow as pointed out earlier.

:::{figure} ../figures/chapter11/incfish.png
:name: fig:incfish
:width: 55%

Directions drawn from a Fisher distribution with a near vertical true mean direction. The Fisher mean direction from the sample is shown by the triangle. The Gaussian average inclination ($<I>= 70^{\circ}$) is shallower than the Fisher mean $I_F = 75^{\circ}$. The estimated inclination using the maximum likelihood estimate of {cite}`mcfadden1982` ($I_{MF}=73^{\circ}$) is closer to the Fisher mean than the Gaussian average.
:::

Several investigators have addressed the issue of inclination-only data. {cite}`mcfadden1982` developed a maximum likelihood estimate for the true inclination which works reasonably well. Their approach is outlined in Appendix F.

By comparing inclinations estimated using the McFadden-Reid technique with those calculated using the full vector data, it is clear that the method breaks down at high inclinations and high scatter. It is also inappropriate for data sets that are not Fisher distributed!

:::{figure} ../figures/chapter11/fishrot.png
:name: fig:fishrot
:width: 100%

Transformation of coordinates from a) geographic to b) "data" coordinates. The direction of the principal eigenvector $\mathbf{V}_1$ is shown by the triangle in both plots. [Figure redrawn from {cite}`tauxe1998`.]
:::

(sect:fishtests)=
## Is a Given Data Set Fisher Distributed?

Clearly, the Fisher distribution allows powerful tests and this power lies behind the popularity of paleomagnetism in solving geologic problems. The problem is that these tests require that the data be Fisher distributed. How can we tell if a particular data set is Fisher distributed? What do we do if the data are not Fisher distributed? These questions are addressed in the rest of this chapter and the next one.

Let us now consider how to determine whether a given data set is Fisher distributed. There are actually many ways of doing this. There is a rather complete discussion of the problem in {cite}`fisher1987` and if you really want a complete treatment try the supplemental reading list at the end of this chapter. The quantile-quantile (Q-Q) method described by {cite}`fisher1987` is fairly intuitive and works well. We outline it briefly in the following.

:::{figure} ../figures/chapter11/unexp.png
:name: fig:unexp
:width: 100%

a) Declinations and b) co-inclinations ($\alpha$) from [Figure %s](#fig:fishrot). Also shown are behaviors expected for $D$ and $I$ from a Fisher distribution, i.e., declinations are uniformly distributed while co-inclinations are exponentially distributed. [Figure from {cite}`tauxe1998`.]
:::

The idea behind the *Q-Q* method is to exploit the fact that declinations in a Fisher distribution, when viewed about the mean, are spread around the clock evenly -- there is a uniform distribution of declinations. Also, the inclinations (or rather the co-inclinations) are clustered close to the mean and the frequency dies off exponentially away from the mean direction.

Therefore, the first step in testing for compatibility with a Fisher distribution is to transpose the data such that the mean is the center of the distribution. You can think of this as rotating your head around to peer down the mean direction. On an equal area projection, the center of the diagram will now be the mean direction instead of the vertical. In order to do this transformation, we first calculate the orientation matrix $\mathbf{T}$ of the data and the associated eigenvectors $\mathbf{V}_i$ and eigenvalues $\tau_i$ (Appendix B - in case you haven't read it yet, do so NOW). Substituting the direction cosines relating the geographic coordinate system $\mathbf{X}$ to the coordinate system defined by $\mathbf{V}$, the eigenvectors, where $\mathbf{X}$ is the "old" and $\mathbf{V}$ is the "new" set of axes, we can transform the coordinate system for a set of data from "geographic" coordinates ([Figure %s](#fig:fishrot)a) where the vertical axis is the center of the diagram, to the "data" coordinate system, ([Figure %s](#fig:fishrot)b) where the principal eigenvector ($\mathbf{V}_1$) lies at the center of the diagram, after transformation into "data" coordinates.

Recalling that Fisher distributions are symmetrically disposed about the mean direction, but fall off exponentially away from that direction, let us compare the data from [Figure %s](#fig:fishrot) to the expected distributions for a Fisher distribution with $\kappa = 20$ ([Figure %s](#fig:unexp)). The data were generated using the program **fisher.py** in the **PmagPy** software distribution which relies on the method outlined by {cite}`fisher1987`, that draws directions from a Fisher distribution with a specified $\kappa$. We used a $\kappa$ of 20, and it should come as no surprise that the data fit the expected distribution rather well. But how well is "well" and how can we tell when a data set *fails* to be fit by a Fisher distribution?

:::{figure} ../figures/chapter11/fishqq.png
:name: fig:fishqq
:width: 85%

a) Quantile-quantile plot of declinations (in data coordinates) from [Figure %s](#fig:fishrot) plotted against an assumed uniform distribution. b) Same for inclinations plotted against an assumed exponential distribution. The data are Fisher distributed. [Figure from {cite}`tauxe1998`.]
:::

We wish to test whether the declinations are uniformly distributed and whether the inclinations are exponentially distributed as required by the Fisher distribution. Plots such as those shown in [Figure %s](#fig:unexp) are not as helpful for this purpose as a plot known as a *quantile-quantile* (Q-Q) diagram (see {cite}`fisher1987`). In a Q-Q plot, the data are graphed against the value expected from a particular distribution. Data compatible with the chosen distribution plot along a line. The procedure for accomplishing this is given in Appendix G. In [Figure %s](#fig:fishqq)a, we plot the declinations from [Figure %s](#fig:fishrot) (in data coordinates) against the values calculated assuming a uniform distribution and in [Figure %s](#fig:fishqq)b, we plot the co-inclinations against those calculated using an exponential distribution. As expected, the data plot along lines. Appendix G outlines the calculation of two test statistics $M_u$ and $M_e$ which can be used to assess whether the data are uniformly or exponentially distributed respectively. Neither of these exceed the critical values.

**SUPPLEMENTAL READINGS:** {cite}`fisher1987`, Chapters 2--5.

## Problems

Review the instructions in the Preface for using PmagPy modules in Jupyter notebooks.

**Problem 1**

a) Use the function **ipmag.fishrot** to generate a Fisher distributed data set of $N=20$ data points, drawn from a true mean direction of $D = 12^{\circ}$, $I = 45^{\circ}$ and a $\kappa$ of 25. Use **ipmag.plot_net** and **ipmag.plot_di** to admire your handiwork.

b) Write a program to calculate the Fisher mean declination and inclination and these Fisher statistics: $k, \alpha_{95}, R$ and CSD for the data generated in Problem 1a. You can check your answer with the PmagPy program **ipmag.fisher_mean** designed to work within Jupyter notebooks.

c) Generate a second sample from the same distribution (just repeat the **ipmag.fishrot** calls). Now you have two sets of directions drawn from the same distribution and certainly should share a common mean direction (logically). But do the two data sets pass the simple Watson's $F$ test for common mean direction? [This test should fail 5% of the time!] Write a simple program to read in the two data files and calculate Watson's $F$. Check your answer using the function **pmag.watsons_f**.

d) Generate a third sample from a distribution with $D = 55^{\circ}, I = 60^{\circ}$ but the same $N$ and $\kappa$. Does this data set pass the $F$ test for common mean with the first data set in Problem 1a?

e) An alternative method for testing for common mean with less restrictive assumptions uses Watson's statistic $V_w$. Use the program **ipmag.common_mean_watson** to test the Problem 1a data set against the one generated in Problem 1d. Do the answers using $V_w$ agree with those using the $F$ test?

**Problem 2**

a) Draw a set of directions from a Fisher distribution with a true mean inclination of 50$^{\circ}$ (using e.g., **ipmag.fishrot**), an $N$ of 20 and a $\kappa$ of 20. Calculate the Gaussian mean of the inclination data.

b) How does the Gaussian average compare with the average you calculate using your Fisher program (or **ipmag.fisher_mean**)?

c) Call the function **pmag.doincfish**, which does the inclination only calculation of $\bar I$. Is this estimate closer to the Fisher estimate?

**Problem 3**

a) Unpack the Chapter_11 datafile from the data_files archive (see the Preface for instructions). You will find a file called *prob3a.dat*. This has: $D, I$, dip direction and dip from two limbs of the fold. They are of both polarities. Separate the data into normal and reverse polarity, flip the reverse data over to their antipodes and calculate the Fisher statistics for the combined data set.

- To split the data into two modes, use the program **pmag.doprinc** to calculate the principle direction. Directions with an angle less than 90$^{\circ}$ away from this are in one mode and greater than 90$^{\circ}$ away are in the other. You can use Python's Pandas filtering power for this, but you will have to write a small function to calculate the angle. For this, remember that the cosine of the angle is the dot product of the two unit vectors. Or, use **pmag.angle** which does just that!
- Take the antipodes of one of the two sets and 'flip' them by adding 180 (using modulo 360! - %360) and taking the opposite of the inclination.
- Calculate the means using one of the options described in Problem 1.

b) Use the function **pmag.dotilt** to "untilt" the data. Repeat the procedure in a). Would the two data sets pass a simple (McElhinny $F$ test) fold test?

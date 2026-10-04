---
title: Probability, Statistics, Measurement and the Scientific Method
field: Mathematics
subfield: Probability and Statistics
level: high-school to undergraduate
keywords: [scientific method, hypothesis, theory, falsifiability, measurement, SI units, significant figures, accuracy, precision, uncertainty, error propagation, dimensional analysis, probability, conditional probability, Bayes theorem, random variables, expected value, variance, binomial distribution, Poisson distribution, normal distribution, central limit theorem, descriptive statistics, hypothesis testing, p-value, confidence interval, t-test, chi-square, correlation, regression, least squares, Bayesian inference, reproducibility]
---

# Probability, Statistics, Measurement and the Scientific Method

Science is a method for learning about the world through evidence. Every measurement has uncertainty, every experiment involves randomness, and every conclusion must be weighed against alternative explanations. This document covers the scientific method itself, the practice of measurement, and the mathematics of probability and statistics that lets scientists draw reliable conclusions from imperfect data.

## Part I — The Scientific Method

### 1. How science works
The process is iterative rather than a rigid recipe:
1. **Observation and question:** noticing a phenomenon (e.g. why do some bacterial cultures die near a mold?).
2. **Background research.**
3. **Hypothesis:** a testable, falsifiable explanation or prediction ("the mold produces a substance that kills bacteria").
4. **Prediction:** what should be observed if the hypothesis is true.
5. **Experiment or observation:** designed to test the prediction, with controls.
6. **Analysis:** statistical evaluation of the data.
7. **Conclusion:** support, refine, or reject the hypothesis.
8. **Peer review, publication and replication** by independent researchers.
(Alexander Fleming's 1928 observation of *Penicillium* killing *Staphylococcus* followed this path, with Florey and Chain developing penicillin into a drug.)

### Key concepts
- **Hypothesis:** a tentative, testable explanation.
- **Scientific law:** a concise description (often mathematical) of a regularity in nature — *what* happens (Newton's law of gravitation, the ideal gas law, Mendel's laws).
- **Scientific theory:** a well-substantiated, comprehensive explanation of a broad range of phenomena, supported by extensive evidence and able to make predictions — *why* it happens (atomic theory, evolution by natural selection, general relativity, germ theory, plate tectonics, quantum mechanics). In science, "theory" does **not** mean a guess; theories are the highest form of scientific understanding. Laws do not "graduate" from theories; they are different kinds of statements.
- **Falsifiability** (Karl Popper, 1934): a scientific claim must be testable in a way that could, in principle, show it to be false. "All swans are white" is falsified by one black swan. Claims that cannot be tested are outside science.
- **Paradigm shifts** (Thomas Kuhn, 1962): science sometimes progresses through revolutions (Copernican astronomy, Darwinian evolution, quantum mechanics, plate tectonics) when accumulating anomalies overturn established frameworks.
- **Occam's razor:** prefer the simplest explanation consistent with the evidence.
- **Correlation does not imply causation:** ice cream sales and drowning deaths both rise in summer (confounded by temperature). Establishing causation requires controlled experiments or careful causal inference.
- **Extraordinary claims require extraordinary evidence** (often attributed to Carl Sagan, echoing Laplace and Hume). Examples: the 2011 "faster-than-light neutrinos" result (OPERA) was traced to a loose fiber-optic cable; cold fusion (1989) could not be reproduced.

### Experimental design
- **Independent variable:** what the experimenter changes. **Dependent variable:** what is measured. **Controlled variables:** kept constant.
- **Control group:** receives no treatment (or a placebo) for comparison. **Positive and negative controls** verify the method works.
- **Randomization:** randomly assigning subjects to groups prevents systematic bias and balances unknown confounders.
- **Blinding:** single-blind (subjects don't know their group), double-blind (neither subjects nor experimenters know) — prevents placebo effects and observer bias. The **placebo effect** can be substantial, especially for subjective outcomes like pain.
- **Replication:** repeating measurements (within a study) and entire studies (by others).
- **Sample size:** larger samples reduce random error and increase statistical power.
- **Randomized controlled trials (RCTs)** are the gold standard for testing medical treatments; the first modern RCT is often cited as the 1948 streptomycin trial for tuberculosis. Earlier, James Lind's 1747 experiment on sailors showed citrus fruits cure scurvy.
- **Observational studies** (cohort, case–control, cross-sectional) are necessary when experiments are impossible or unethical (e.g. Doll and Hill's studies linking smoking and lung cancer in the 1950s), but are vulnerable to confounding.

### Reproducibility and scientific integrity
- Many published findings in some fields have failed to replicate (the "replication crisis", especially in psychology and biomedicine). Causes: small samples, publication bias (journals favoring positive results), **p-hacking** (trying many analyses until one is "significant"), HARKing (hypothesizing after results are known), and occasionally fraud.
- Remedies: preregistration of hypotheses and analysis plans, larger samples, open data and code, replication studies, reporting effect sizes and confidence intervals, and meta-analyses.

## Part II — Measurement

### 2. The International System of Units (SI)
Seven base units, redefined in 2019 in terms of fixed values of fundamental constants:

| Quantity | Unit | Symbol | Defined by fixing |
|---|---|---|---|
| Time | second | s | Cesium-133 hyperfine frequency = 9 192 631 770 Hz |
| Length | meter | m | Speed of light $c$ = 299 792 458 m/s |
| Mass | kilogram | kg | Planck constant $h$ = 6.62607015 × 10⁻³⁴ J·s (replacing the platinum–iridium prototype kept in Sèvres since 1889) |
| Electric current | ampere | A | Elementary charge $e$ = 1.602176634 × 10⁻¹⁹ C |
| Temperature | kelvin | K | Boltzmann constant $k_B$ = 1.380649 × 10⁻²³ J/K |
| Amount of substance | mole | mol | Avogadro constant $N_A$ = 6.02214076 × 10²³ mol⁻¹ |
| Luminous intensity | candela | cd | Luminous efficacy of 540 THz radiation = 683 lm/W |

**Derived units:** newton (N = kg·m/s²), joule (J = N·m), watt (W = J/s), pascal (Pa = N/m²), coulomb (C = A·s), volt (V = W/A), ohm (Ω = V/A), hertz (Hz = s⁻¹), tesla, farad, henry, becquerel, gray, sievert...

**Prefixes:** quecto (10⁻³⁰), ronto (10⁻²⁷), yocto (10⁻²⁴), zepto (10⁻²¹), atto (10⁻¹⁸), femto (10⁻¹⁵), pico (10⁻¹²), nano (10⁻⁹), micro (10⁻⁶), milli (10⁻³), centi (10⁻²), kilo (10³), mega (10⁶), giga (10⁹), tera (10¹²), peta (10¹⁵), exa (10¹⁸), zetta (10²¹), yotta (10²⁴), ronna (10²⁷), quetta (10³⁰). (Ronna, quetta, ronto and quecto were added in 2022.)

Unit errors have real consequences: NASA's **Mars Climate Orbiter** was lost in 1999 because one team used pound-force seconds while another expected newton-seconds; the **"Gimli Glider"** (1983) — an Air Canada Boeing 767 ran out of fuel mid-flight due to a pounds/kilograms mix-up.

### 3. Dimensional analysis
Every physical equation must be dimensionally consistent: both sides must have the same dimensions (mass [M], length [L], time [T], etc.). This checks formulas and can even derive relationships.

**Example 3.1:** the period of a pendulum might depend on length $L$, mass $m$ and $g$. Writing $T \propto L^am^bg^c$: [T] = [L]^a[M]^b[L T⁻²]^c → b = 0, a + c = 0, −2c = 1 → c = −½, a = ½. So $T \propto\sqrt{L/g}$ — independent of mass, with the dimensionless constant (2π) determined otherwise.

**Example 3.2:** G. I. Taylor (1950) estimated the energy of the first atomic bomb test (~20 kilotons) from published photographs of the fireball radius versus time, using dimensional analysis: $R \approx (Et^2/\rho)^{1/5}$.

**Unit conversion** by multiplying by factors equal to one: 90 km/h × (1000 m/km) × (1 h/3600 s) = 25 m/s.

### 4. Accuracy, precision and uncertainty
- **Accuracy:** closeness to the true value. **Precision:** closeness of repeated measurements to each other (reproducibility). A dartboard analogy: tightly clustered darts far from the bullseye are precise but inaccurate.
- **Random errors:** unpredictable fluctuations, scattering results around the true value; reduced by averaging many measurements.
- **Systematic errors:** consistent bias in one direction (miscalibrated instrument, parallax, unaccounted effects); not reduced by averaging — must be identified and corrected.
- **Reporting:** a measurement should be reported with its uncertainty, e.g. $g = 9.81 \pm 0.02$ m/s².

### Significant figures
- Non-zero digits are significant; zeros between non-zero digits are significant; leading zeros are not (0.0052 has two); trailing zeros after a decimal point are significant (2.50 has three).
- **Multiplication/division:** the result has as many significant figures as the least precise factor. $4.56 \times 1.4 = 6.4$.
- **Addition/subtraction:** the result has as many decimal places as the least precise term. $12.11 + 18.0 + 1.013 = 31.1$.
- Exact numbers (counted objects, defined conversions) have unlimited significant figures.

### Error propagation
For independent uncertainties:
- **Sums and differences:** $q = x \pm y \Rightarrow \delta q = \sqrt{(\delta x)^2 + (\delta y)^2}$.
- **Products and quotients:** $q = xy$ or $x/y \Rightarrow \frac{\delta q}{|q|} = \sqrt{\left(\frac{\delta x}{x}\right)^2 + \left(\frac{\delta y}{y}\right)^2}$.
- **Powers:** $q = x^n \Rightarrow \frac{\delta q}{|q|} = |n|\frac{\delta x}{|x|}$.
- **General:** $\delta q = \sqrt{\sum\left(\frac{\partial q}{\partial x_i}\delta x_i\right)^2}$.

**Example 4.1:** measuring a pendulum: $L = 1.000 \pm 0.002$ m, $T = 2.006 \pm 0.004$ s. $g = 4\pi^2L/T^2 = 9.81$ m/s². Relative error: $\sqrt{(0.002)^2 + (2\times0.004/2.006)^2} = \sqrt{4\times10^{-6} + 1.59\times10^{-5}} = 0.0045$ → $g = 9.81 \pm 0.04$ m/s². The timing uncertainty dominates (doubled because $T$ is squared) — so measure many swings to reduce it.

**Standard error of the mean:** averaging $N$ independent measurements with standard deviation $\sigma$ reduces the uncertainty of the mean to $\sigma/\sqrt N$. Quadrupling the number of measurements halves the uncertainty.

## Part III — Probability

### 5. Basic probability
For an event $A$: $0 \le P(A) \le 1$; for equally likely outcomes, $P(A) = \frac{\text{favorable outcomes}}{\text{total outcomes}}$.
- **Complement:** $P(\text{not }A) = 1 - P(A)$.
- **Addition rule:** $P(A\text{ or }B) = P(A) + P(B) - P(A\text{ and }B)$.
- **Multiplication rule:** $P(A\text{ and }B) = P(A)P(B|A)$; for **independent** events, $P(A)P(B)$.
- **Conditional probability:** $P(A|B) = \frac{P(A\text{ and }B)}{P(B)}$.

**Combinatorics:** permutations $_nP_k = \frac{n!}{(n-k)!}$ (order matters); combinations $\binom nk = \frac{n!}{k!(n-k)!}$ (order doesn't). Lottery 6 of 49: $\binom{49}{6} = 13\,983\,816$ combinations.

**The birthday problem:** in a group of just 23 people, the probability that at least two share a birthday exceeds 50% (and 99.9% with 70 people) — counterintuitive because there are $\binom{23}{2} = 253$ pairs.

**The gambler's fallacy:** independent events have no memory — after ten heads in a row, a fair coin still has a 50% chance of heads.

### 6. Bayes' theorem
$$\boxed{P(A|B) = \frac{P(B|A)\,P(A)}{P(B)}}$$
(Thomas Bayes, published 1763; generalized by Laplace.) It updates the probability of a hypothesis $A$ (the **prior** $P(A)$) in light of evidence $B$, yielding the **posterior** $P(A|B)$.

**Worked example 6.1 — medical testing and the base-rate fallacy:** a disease affects 1% of the population. A test has 99% sensitivity (detects 99% of true cases) and 95% specificity (5% false positive rate). If a randomly selected person tests positive, what is the probability they have the disease?
$P(+) = 0.99\times0.01 + 0.05\times0.99 = 0.0099 + 0.0495 = 0.0594$.
$P(D|+) = \frac{0.0099}{0.0594} \approx 0.167$ — only **~17%**!
Because the disease is rare, false positives from the large healthy population outnumber true positives. This is why screening tests are followed by confirmatory tests, and why the "prosecutor's fallacy" (confusing $P(\text{evidence}|\text{innocent})$ with $P(\text{innocent}|\text{evidence})$) is dangerous in courtrooms.

**Bayesian inference** treats probabilities as degrees of belief and updates them with data, as opposed to the **frequentist** interpretation (probabilities as long-run frequencies). Both are widely used; Bayesian methods power spam filters, medical diagnosis, machine learning, search-and-rescue planning (finding the wreck of Air France 447 in 2011), and cosmological parameter estimation.

### 7. Random variables and distributions
A **random variable** assigns numbers to outcomes. Key summaries:
- **Expected value (mean):** $E[X] = \sum x_iP(x_i)$ or $\int xp(x)\,dx$.
- **Variance:** $\text{Var}(X) = E[(X - \mu)^2] = E[X^2] - \mu^2$; **standard deviation** $\sigma = \sqrt{\text{Var}}$.
- For independent variables: $E[X + Y] = E[X] + E[Y]$ (always); $\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y)$ (if independent).

**Important distributions:**

| Distribution | Use | Mean | Variance |
|---|---|---|---|
| **Binomial** $B(n, p)$: $P(k) = \binom nkp^k(1-p)^{n-k}$ | Number of successes in $n$ independent trials (coin flips, inherited alleles, survey responses) | $np$ | $np(1-p)$ |
| **Poisson**: $P(k) = \frac{\lambda^ke^{-\lambda}}{k!}$ | Counts of rare independent events per interval (radioactive decays, photons hitting a detector, mutations, emails per hour) | $\lambda$ | $\lambda$ |
| **Normal (Gaussian)**: $p(x) = \frac{1}{\sigma\sqrt{2\pi}}e^{-(x-\mu)^2/2\sigma^2}$ | Measurement errors, heights, sums of many effects | $\mu$ | $\sigma^2$ |
| **Exponential**: $p(t) = \lambda e^{-\lambda t}$ | Waiting times between Poisson events (radioactive decay times) | $1/\lambda$ | $1/\lambda^2$ |
| **Uniform** on $[a, b]$ | Equally likely values (random number generators) | $(a+b)/2$ | $(b-a)^2/12$ |

**Counting statistics:** for Poisson processes, the uncertainty in a count $N$ is $\sqrt N$. Counting 10 000 decays gives a relative uncertainty of 1%; counting 100 gives 10%. This is the "shot noise" limit in photon detection.

**Example 7.1:** a detector registers an average of 4 cosmic rays per minute. Probability of exactly 2 in a given minute: $\frac{4^2e^{-4}}{2!} = 8e^{-4} \approx 0.147$. Probability of none: $e^{-4} \approx 0.018$.

### The normal distribution and the 68–95–99.7 rule
For a normal distribution, ~68.3% of values lie within ±1σ of the mean, ~95.4% within ±2σ, and ~99.7% within ±3σ. A 5σ deviation (the particle-physics discovery standard) has a one-sided probability of ~2.9 × 10⁻⁷ (about 1 in 3.5 million).

**z-score:** $z = \frac{x - \mu}{\sigma}$ — number of standard deviations from the mean.

### The central limit theorem
The sum (or average) of many independent random variables with finite variance tends toward a **normal distribution**, regardless of the original distribution. This explains why normal distributions are ubiquitous (heights result from many genes and environmental factors; measurement errors combine many small effects) and justifies many statistical methods. A **random walk** of $N$ steps of length $\ell$ has a typical displacement $\ell\sqrt N$ — the basis of diffusion.

### The law of large numbers
As the number of trials increases, the sample average converges to the expected value. Casinos rely on this: individual bets are random, but aggregate results are predictable.

## Part IV — Statistics

### 8. Descriptive statistics
- **Mean** $\bar x = \frac1n\sum x_i$; **median** (middle value; robust to outliers — preferred for skewed data like incomes); **mode** (most frequent).
- **Range**, **interquartile range**, **standard deviation**: sample standard deviation $s = \sqrt{\frac{1}{n-1}\sum(x_i - \bar x)^2}$ (dividing by $n - 1$, Bessel's correction, gives an unbiased variance estimate).
- **Visualization:** histograms, box plots, scatter plots. Always plot data — **Anscombe's quartet** (1973) is four datasets with identical means, variances, correlations and regression lines that look completely different when plotted.

### 9. Hypothesis testing
1. State a **null hypothesis** $H_0$ (no effect, no difference) and an **alternative** $H_1$.
2. Choose a significance level $\alpha$ (commonly 0.05).
3. Compute a test statistic from the data.
4. Compute the **p-value**: the probability, **assuming $H_0$ is true**, of obtaining results at least as extreme as those observed.
5. If $p < \alpha$, reject $H_0$ ("statistically significant"); otherwise, fail to reject it (which is not proof that $H_0$ is true).

**Errors:**
- **Type I error** (false positive): rejecting a true $H_0$; probability $\alpha$.
- **Type II error** (false negative): failing to reject a false $H_0$; probability $\beta$. **Power** = $1 - \beta$, increased by larger samples and larger effects.

**Common misinterpretations of p-values:** a p-value is **not** the probability that $H_0$ is true, nor the probability the result is due to chance, nor a measure of effect size or importance. A tiny, unimportant effect can be "significant" with a huge sample; an important effect can be "non-significant" with a small sample. The American Statistical Association's 2016 statement emphasized these points. Report **effect sizes and confidence intervals**, not just p-values.

**Multiple comparisons:** testing 20 independent hypotheses at α = 0.05, the chance of at least one false positive is $1 - 0.95^{20} \approx 64\%$. Corrections: Bonferroni (use $\alpha/m$), false discovery rate control (Benjamini–Hochberg) — essential in genomics, where millions of tests are performed (GWAS use $p < 5\times10^{-8}$).

### Common tests
- **t-test** (William Sealy Gosset, publishing as "Student" while working at the Guinness brewery, 1908): compares means of one or two groups when σ is unknown; $t = \frac{\bar x_1 - \bar x_2}{s_p\sqrt{1/n_1 + 1/n_2}}$. Paired t-tests for before/after measurements.
- **ANOVA:** compares means of three or more groups.
- **Chi-square test:** $\chi^2 = \sum\frac{(O - E)^2}{E}$ — goodness of fit (e.g. Mendelian ratios) and independence in contingency tables.
- **Non-parametric tests** (Mann–Whitney U, Wilcoxon, Kruskal–Wallis) when normality assumptions fail.

**Example 9.1 — coin fairness:** 60 heads in 100 flips. Under $H_0$ ($p = 0.5$), mean 50, $\sigma = \sqrt{100\times0.25} = 5$. $z = (60 - 50)/5 = 2.0$; two-sided $p \approx 0.046$ (≈0.057 with a continuity correction, or the exact binomial value of ~0.057). Borderline evidence that the coin is biased — note how the conclusion near α = 0.05 can depend on method details.

### 10. Confidence intervals
A **95% confidence interval** for a mean: $\bar x \pm t^*\frac{s}{\sqrt n}$ (≈ $\bar x \pm1.96\,s/\sqrt n$ for large $n$). Interpretation (frequentist): if the procedure were repeated many times, 95% of the constructed intervals would contain the true value. It is **not** that there is a 95% probability the true value lies in this particular interval (that is a Bayesian credible interval's interpretation).

**Example 10.1:** 25 measurements of a resistor give $\bar x = 100.3$ Ω, $s = 1.5$ Ω. Standard error $= 1.5/5 = 0.3$ Ω. 95% CI (t* ≈ 2.064 for 24 df): $100.3 \pm 0.62$ Ω, i.e. 99.7–100.9 Ω.

### 11. Correlation and regression
- **Pearson correlation coefficient** $r$ (−1 to +1) measures the strength of a **linear** relationship. $r^2$ is the fraction of variance in $y$ explained by a linear fit. $r = 0$ does not mean no relationship (a perfect parabola can have $r = 0$).
- **Linear regression (least squares):** fit $y = a + bx$ minimizing the sum of squared residuals $\sum(y_i - a - bx_i)^2$ (Legendre 1805, Gauss 1809 — who used it to recover the orbit of the asteroid Ceres). Solution:
$$b = \frac{\sum(x_i - \bar x)(y_i - \bar y)}{\sum(x_i - \bar x)^2}, \qquad a = \bar y - b\bar x$$
- **Linearization:** many scientific relationships become linear after transformation: exponential decay ($\ln N$ vs $t$), Arrhenius ($\ln k$ vs $1/T$), power laws ($\log y$ vs $\log x$ — e.g. Kepler's third law, metabolic scaling where metabolic rate ∝ mass^~3/4, Kleiber's law), Lineweaver–Burk plots.
- **Regression to the mean** (Francis Galton, 1886): extreme measurements tend to be followed by less extreme ones, purely statistically (very tall parents tend to have children who are tall but less extreme). Ignoring it leads to false conclusions about treatments ("the patient improved after the remedy" when they would have improved anyway).
- **Overfitting:** a model with too many parameters fits noise. "With four parameters I can fit an elephant, and with five I can make him wiggle his trunk" (attributed by Fermi to von Neumann). Cross-validation and simpler models guard against it.
- **Simpson's paradox:** a trend in several groups can reverse when groups are combined (e.g. the 1973 UC Berkeley admissions data, where an apparent overall bias against women reversed within most departments, because women applied more to competitive departments). Careful attention to confounding variables is essential.

## 12. Summary

| Concept | Key formula / idea |
|---|---|
| Theory vs. law | Theory explains (why); law describes (what) |
| Falsifiability | Scientific claims must be testable |
| SI base units | s, m, kg, A, K, mol, cd (defined by constants since 2019) |
| Error propagation (products) | $\delta q/q = \sqrt{\sum(\delta x_i/x_i)^2}$ |
| Standard error | $\sigma/\sqrt N$ |
| Bayes' theorem | $P(A\vert B) = P(B\vert A)P(A)/P(B)$ |
| Binomial | mean $np$, variance $np(1-p)$ |
| Poisson | mean = variance = $\lambda$; count uncertainty $\sqrt N$ |
| Normal | 68–95–99.7 rule |
| Central limit theorem | Sums of many independent variables → normal |
| p-value | P(data at least this extreme \| $H_0$) |
| 95% CI | $\bar x \pm1.96\,s/\sqrt n$ (large $n$) |
| Least squares slope | $b = \sum(x - \bar x)(y - \bar y)/\sum(x - \bar x)^2$ |
| Correlation ≠ causation | Confounders, reverse causation, chance |

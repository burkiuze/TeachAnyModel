---
title: The Origins of Quantum Theory
field: Physics
subfield: Quantum Mechanics
level: high-school to undergraduate
keywords: [blackbody radiation, ultraviolet catastrophe, Planck's constant, quantization, photoelectric effect, photon, work function, Compton scattering, atomic spectra, Rydberg formula, Bohr model, de Broglie wavelength, wave-particle duality, Davisson-Germer experiment, Franck-Hertz experiment, old quantum theory]
---

# The Origins of Quantum Theory

At the end of the 19th century many physicists believed physics was nearly complete. Newtonian mechanics, Maxwell's electromagnetism and thermodynamics explained a vast range of phenomena. Lord Kelvin, in a famous 1900 lecture, spoke of only "two clouds" on the horizon. One cloud (the null result of the Michelson–Morley experiment) led to relativity. The other — the failure of classical physics to explain **blackbody radiation** — led to **quantum mechanics**, the most successful and most philosophically unsettling theory in the history of science.

This document traces the experimental puzzles and bold hypotheses (1900–1924) that forced physicists to abandon classical ideas, known collectively as the "old quantum theory".

## 1. Blackbody Radiation and Planck's Quantum (1900)

### The problem
A **blackbody** absorbs all radiation falling on it and, in thermal equilibrium, emits radiation with a spectrum depending only on its temperature. A small hole in a cavity with opaque walls is an excellent experimental blackbody. Real objects — stars, glowing metal, the human body, the cosmic microwave background — approximate blackbodies.

Experimental facts:
- **Stefan–Boltzmann law:** total emitted power per area $= \sigma T^4$.
- **Wien's displacement law:** peak wavelength $\lambda_{\max} = b/T$, $b = 2.898\times10^{-3}$ m·K.
- The spectrum rises from zero at long wavelengths, peaks, and falls to zero at short wavelengths.

### The classical prediction fails: the ultraviolet catastrophe
Classical physics treats the radiation in a cavity as a collection of standing electromagnetic waves (modes). The number of modes per unit volume per unit frequency is $\frac{8\pi\nu^2}{c^3}$. By the **equipartition theorem**, each mode should have average energy $k_BT$. This gives the **Rayleigh–Jeans law**:
$$u(\nu, T) = \frac{8\pi\nu^2}{c^3}k_BT$$
It agrees with experiment at low frequencies but grows without bound as $\nu^2$ at high frequencies — predicting infinite total energy. Paul Ehrenfest later called this the **ultraviolet catastrophe**.

### Planck's hypothesis
On 14 December 1900, Max Planck presented a formula that fit the data perfectly. To derive it he made what he called "an act of desperation": he assumed that the oscillators in the cavity walls could only have energies that are **integer multiples** of a basic unit proportional to frequency:
$$\boxed{E = nh\nu, \qquad n = 0, 1, 2, \ldots}$$
where $h$ is a new constant of nature, **Planck's constant**:
$$h = 6.62607015\times10^{-34}\text{ J·s (exact since 2019)}, \qquad \hbar = \frac{h}{2\pi} = 1.054571817\times10^{-34}\text{ J·s}$$

With quantized energies, the average energy of a mode is not $k_BT$ but (using Boltzmann statistics over the levels $nh\nu$):
$$\langle E\rangle = \frac{h\nu}{e^{h\nu/k_BT} - 1}$$
This leads to **Planck's radiation law**:
$$\boxed{u(\nu, T) = \frac{8\pi h\nu^3}{c^3}\frac{1}{e^{h\nu/k_BT} - 1}}$$

**Why it works:** at low frequencies ($h\nu \ll k_BT$), $\langle E\rangle \approx k_BT$ — the classical result. At high frequencies ($h\nu \gg k_BT$), the energy quantum is so large that modes are almost never excited ($\langle E\rangle \approx h\nu e^{-h\nu/k_BT} \to 0$), cutting off the catastrophe.

Integrating Planck's law reproduces the Stefan–Boltzmann law and gives $\sigma = \frac{2\pi^5k_B^4}{15h^3c^2}$; differentiating gives Wien's law. Planck used the fit to determine $h$ and $k_B$ (and hence Avogadro's number and the electron charge) with remarkable accuracy.

Planck himself regarded quantization as a mathematical trick and spent years trying to reconcile it with classical physics. He received the Nobel Prize in 1918.

## 2. The Photoelectric Effect and the Photon (1905)

### The experiment
When light shines on a clean metal surface in a vacuum, electrons are ejected (Hertz 1887; studied in detail by Philipp Lenard around 1902). Measuring the current as a function of a retarding voltage gives the maximum kinetic energy of the photoelectrons.

### Observations that defy classical wave theory

| Observation | Classical wave prediction | Actual result |
|---|---|---|
| Effect of intensity on electron energy | Brighter light → more energetic electrons | Max kinetic energy is **independent of intensity** |
| Effect of frequency | Any frequency works if intense enough | Below a **threshold frequency** $\nu_0$, no electrons are emitted, no matter how intense |
| Effect of frequency on energy | No particular dependence | Max kinetic energy increases **linearly with frequency** |
| Time delay | Weak light needs time to accumulate energy (seconds to minutes) | Emission is **instantaneous** (< 10⁻⁹ s) even for very dim light |
| Effect of intensity on number | — | More intense light → more electrons |

### Einstein's explanation
In 1905 Einstein proposed that light itself consists of discrete quanta — later named **photons** (G. N. Lewis, 1926) — each with energy
$$\boxed{E = h\nu = \frac{hc}{\lambda}}$$
An electron absorbs a single photon. Part of the energy, the **work function** $\phi$, is needed to free the electron from the metal; the rest becomes kinetic energy:
$$\boxed{K_{\max} = h\nu - \phi}$$
- Threshold frequency: $\nu_0 = \phi/h$.
- Intensity determines the *number* of photons, hence the number of electrons, not their energy.
- A single photon delivers its energy at once — no delay.
- The **stopping potential** $V_s$ satisfies $eV_s = K_{\max} = h\nu - \phi$; a plot of $V_s$ vs. $\nu$ is a straight line with slope $h/e$ for every metal.

Robert Millikan, who doubted Einstein's idea, spent a decade testing it and in 1916 confirmed the linear relation precisely, obtaining a value of $h$ within 0.5% of Planck's. Einstein's Nobel Prize (1921) was awarded "especially for his discovery of the law of the photoelectric effect" — not for relativity.

| Metal | Work function (eV) | Threshold wavelength (nm) |
|---|---|---|
| Cesium | 2.1 | 590 |
| Potassium | 2.3 | 540 |
| Sodium | 2.3 | 540 |
| Zinc | 4.3 | 288 |
| Copper | 4.7 | 264 |
| Platinum | 5.6 | 221 |

A handy conversion: $hc = 1240$ eV·nm, so $E(\text{eV}) = 1240/\lambda(\text{nm})$.

### Worked example 2.1
**Problem:** Light of wavelength 400 nm falls on potassium ($\phi = 2.3$ eV). Find the photon energy, the maximum kinetic energy of the photoelectrons, their maximum speed, and the stopping potential.
**Solution:** $E = 1240/400 = 3.10$ eV. $K_{\max} = 3.10 - 2.3 = 0.80$ eV $= 1.28\times10^{-19}$ J.
$v_{\max} = \sqrt{2K/m_e} = \sqrt{2(1.28\times10^{-19})/(9.11\times10^{-31})} \approx 5.3\times10^5$ m/s. Stopping potential: $V_s = 0.80$ V.

### Applications
Photomultiplier tubes, image sensors in older cameras, night-vision devices, photoelectron spectroscopy (measuring electron binding energies in materials). Solar cells and CCD/CMOS sensors rely on the closely related internal photoelectric effect in semiconductors.

### Photon momentum
From relativity, a massless particle has $E = pc$, so a photon carries momentum
$$p = \frac{E}{c} = \frac{h}{\lambda}$$

## 3. Compton Scattering (1923)

Arthur Compton scattered X-rays from electrons in graphite and found that the scattered X-rays had **longer wavelengths**, with the shift depending on the scattering angle $\theta$:
$$\boxed{\Delta\lambda = \lambda' - \lambda = \frac{h}{m_ec}(1 - \cos\theta)}$$
The **Compton wavelength** of the electron is $\lambda_C = \frac{h}{m_ec} = 2.426\times10^{-12}$ m $= 2.426$ pm.

Classical wave theory predicts scattered radiation at the same wavelength (Thomson scattering). Compton derived his formula by treating the X-ray as a **particle** (photon) with energy $h\nu$ and momentum $h/\lambda$ colliding elastically with a free electron, applying relativistic energy and momentum conservation. This was decisive evidence that photons carry momentum like particles. Compton received the Nobel Prize in 1927.

**Derivation sketch:** conservation of four-momentum $p_\gamma + p_e = p_\gamma' + p_e'$. Rearranging to isolate the final electron, $p_e' = p_\gamma + p_e - p_\gamma'$, and squaring (using $p_\gamma^2 = 0$, $p_e^2 = p_e'^2 = m_e^2c^2$):
$0 = p_\gamma\cdot p_e - p_\gamma\cdot p_\gamma' - p_e\cdot p_\gamma'$, i.e. $m_ec(E - E')/c = (EE'/c^2)(1 - \cos\theta)$, which rearranges to $\frac{1}{E'} - \frac1E = \frac{1 - \cos\theta}{m_ec^2}$, equivalent to the formula above.

**Notes:** the shift is maximum ($2\lambda_C$) for backscattering ($\theta = 180°$). It is negligible for visible light (~0.0005% of 500 nm) but significant for X-rays and gamma rays. Compton scattering is the dominant interaction of medium-energy gamma rays with matter, relevant to radiation shielding and medical imaging.

## 4. Atomic Spectra and the Bohr Model (1913)

### Line spectra
Heated gases emit light only at specific wavelengths — **emission line spectra** — unique to each element. Cool gases absorb at the same wavelengths (dark **absorption lines**, such as the Fraunhofer lines in sunlight). Johann Balmer (1885) found an empirical formula for hydrogen's visible lines, generalized by Johannes Rydberg:
$$\frac{1}{\lambda} = R_H\left(\frac{1}{n_1^2} - \frac{1}{n_2^2}\right), \qquad n_2 > n_1$$
with $R_H \approx 1.0968\times10^7$ m⁻¹ (the Rydberg constant for hydrogen; $R_\infty = 1.0974\times10^7$ m⁻¹ for infinite nuclear mass).

| Series | $n_1$ | Region | Discovered |
|---|---|---|---|
| Lyman | 1 | Ultraviolet | 1906–1914 |
| Balmer | 2 | Visible/near-UV | 1885 |
| Paschen | 3 | Infrared | 1908 |
| Brackett | 4 | Infrared | 1922 |
| Pfund | 5 | Infrared | 1924 |

Balmer lines: H-α (656.3 nm, red), H-β (486.1 nm, cyan), H-γ (434.0 nm, violet), H-δ (410.2 nm, violet).

### The stability problem
Rutherford's gold-foil experiment (Geiger and Marsden, 1909; interpreted 1911) showed that atoms have a tiny, dense, positive nucleus. But a classical electron orbiting a nucleus accelerates and must radiate (Larmor formula), losing energy and spiraling into the nucleus in about $10^{-11}$ s. Classical physics could explain neither the stability of atoms nor their discrete spectra.

### Bohr's postulates
Niels Bohr (1913) proposed:
1. Electrons move in certain **stationary orbits** without radiating.
2. In these orbits, the electron's **angular momentum is quantized**: $L = m_evr = n\hbar$, $n = 1, 2, 3, \ldots$
3. Light is emitted or absorbed only when an electron **jumps** between stationary states, with photon energy equal to the energy difference: $h\nu = E_i - E_f$.

### Derivation for hydrogen-like atoms (nuclear charge $Ze$)
Coulomb force provides the centripetal force: $\frac{m_ev^2}{r} = \frac{kZe^2}{r^2}$. Combined with $m_evr = n\hbar$:
$$r_n = \frac{n^2\hbar^2}{m_ekZe^2} = \frac{n^2}{Z}a_0, \qquad a_0 = \frac{\hbar^2}{m_eke^2} = 0.0529\text{ nm (Bohr radius)}$$
$$v_n = \frac{Z\alpha c}{n}, \qquad \alpha = \frac{ke^2}{\hbar c} \approx \frac{1}{137.036}\text{ (fine-structure constant)}$$
$$\boxed{E_n = -\frac{m_ek^2Z^2e^4}{2\hbar^2n^2} = -\frac{13.6\text{ eV}\cdot Z^2}{n^2}}$$
The **ground state** of hydrogen ($n = 1$) has energy −13.6 eV; the **ionization energy** is 13.6 eV. Transition energies give exactly the Rydberg formula, with $R_\infty = \frac{m_ek^2e^4}{4\pi\hbar^3c}$ — computed from fundamental constants. This agreement was a sensational success.

### Worked example 4.1
The H-α line: transition $n = 3 \to 2$. $\Delta E = 13.6(\frac14 - \frac19) = 13.6\times\frac{5}{36} = 1.889$ eV. $\lambda = 1240/1.889 \approx 656$ nm. ✓

### Successes and failures of the Bohr model
**Successes:** hydrogen spectrum; spectra of hydrogen-like ions (He⁺, Li²⁺); the Rydberg constant; the size of the hydrogen atom; Moseley's law for X-ray spectra ($\sqrt\nu \propto Z - 1$), which established atomic number as the organizing principle of the periodic table; correction for nuclear motion (using reduced mass) explained the slightly different spectrum of deuterium, leading to its discovery (Urey, 1931).

**Failures:** cannot handle atoms with more than one electron (even helium); cannot explain relative line intensities, fine structure, or the Zeeman effect fully; predicts the ground state has angular momentum $\hbar$ (actually zero); electrons do not follow definite orbits; the quantization rule is postulated, not explained. Sommerfeld's extension with elliptical orbits explained some fine structure but the framework remained ad hoc.

### The Franck–Hertz experiment (1914)
James Franck and Gustav Hertz accelerated electrons through mercury vapor and found that the current dropped sharply each time the accelerating voltage increased by about 4.9 V. Electrons lost energy only in discrete amounts of 4.9 eV — exciting mercury atoms to their first excited state — and the mercury emitted UV light at 254 nm ($1240/4.9 \approx 253$ nm). This directly confirmed that atomic energy levels are quantized, independent of spectroscopy (Nobel 1925).

## 5. De Broglie's Matter Waves (1924)

If light waves can behave like particles, Louis de Broglie asked in his 1924 doctoral thesis, can particles behave like waves? He proposed that every particle with momentum $p$ has an associated wavelength:
$$\boxed{\lambda = \frac hp}$$
— the same relation as for photons.

**Explaining Bohr's quantization:** if an electron is a standing wave around the nucleus, the orbit's circumference must contain an integer number of wavelengths: $2\pi r = n\lambda = n\frac{h}{m_ev}$, which gives $m_evr = n\hbar$ — Bohr's condition emerges naturally.

### Experimental confirmation
- **Davisson and Germer (1927)** at Bell Labs scattered 54 eV electrons from a nickel crystal and observed a diffraction peak at 50°, exactly matching the de Broglie wavelength $\lambda = h/\sqrt{2m_eK} \approx 0.167$ nm using Bragg's law with nickel's atomic spacing.
- **G. P. Thomson (1927)** passed electrons through thin metal foils and saw diffraction rings. (Poetically, J. J. Thomson won the Nobel Prize for showing the electron is a particle; his son G. P. Thomson won it for showing the electron is a wave. Davisson and G. P. Thomson shared the 1937 prize.)
- Later: diffraction and interference of neutrons, helium atoms, and large molecules (C₆₀ in 1999; molecules of over 25 000 atomic mass units by 2019).

### Why we don't notice matter waves in daily life
| Object | Mass | Speed | de Broglie wavelength |
|---|---|---|---|
| Electron (100 eV) | $9.11\times10^{-31}$ kg | $5.9\times10^6$ m/s | 0.123 nm |
| Thermal neutron (300 K) | $1.67\times10^{-27}$ kg | 2200 m/s | 0.18 nm |
| Baseball | 0.145 kg | 40 m/s | $1.1\times10^{-34}$ m |
| Person walking | 70 kg | 1.4 m/s | $6.8\times10^{-36}$ m |

Wave effects are noticeable only when the wavelength is comparable to the size of the apertures or structures involved. For everyday objects the wavelength is absurdly smaller than an atomic nucleus.

**Electron wavelength formula** (non-relativistic): $\lambda = \frac{h}{\sqrt{2m_eK}}$; for an electron accelerated through $V$ volts, $\lambda \approx \frac{1.226}{\sqrt V}$ nm.

**Applications:** electron microscopes (TEM, SEM) exploit the tiny electron wavelength to achieve resolutions below 0.1 nm, imaging individual atoms; cryo-electron microscopy determines protein structures (Nobel Chemistry 2017); neutron diffraction reveals magnetic structures and hydrogen positions in crystals; low-energy electron diffraction (LEED) studies surfaces.

## 6. Wave–Particle Duality

By 1925 both light and matter were known to exhibit wave behavior (interference, diffraction) and particle behavior (localized detection, discrete energy and momentum transfer). Neither picture alone suffices:
- Light: waves (Young, Maxwell) but also photons (Planck, Einstein, Compton).
- Electrons: particles (Thomson) but also waves (de Broglie, Davisson–Germer).

Bohr's **principle of complementarity** (1927): wave and particle descriptions are complementary; an experiment can reveal one aspect or the other, but not both simultaneously. In the double-slit experiment, obtaining which-path information destroys the interference pattern.

The modern view: quantum objects are neither classical waves nor classical particles. They are described by a **wavefunction** (a probability amplitude) that evolves like a wave and determines the probabilities of particle-like detection events. This resolution came with the new quantum mechanics of 1925–1927.

## 7. The Birth of Quantum Mechanics (1925–1927)

The old quantum theory was a patchwork of classical physics plus quantization rules. A complete theory arrived in a remarkable burst:
- **1925 — Matrix mechanics:** Werner Heisenberg, on the island of Helgoland, formulated a theory using only observable quantities (frequencies and intensities of spectral lines). Max Born and Pascual Jordan recognized Heisenberg's quantities as matrices; the three developed the full theory. Born and Jordan found the commutation relation $xp - px = i\hbar$.
- **1925 — Spin:** George Uhlenbeck and Samuel Goudsmit proposed that the electron has intrinsic angular momentum. Wolfgang Pauli formulated the **exclusion principle**.
- **1926 — Wave mechanics:** Erwin Schrödinger, inspired by de Broglie, wrote his wave equation and solved the hydrogen atom, obtaining Bohr's energies without ad hoc postulates. He soon showed that wave and matrix mechanics are mathematically equivalent.
- **1926 — Born's interpretation:** Max Born proposed that $|\psi|^2$ gives the **probability density** for finding the particle — introducing fundamental randomness into physics (Nobel 1954).
- **1927 — Uncertainty principle:** Heisenberg showed that position and momentum cannot both be precisely defined: $\Delta x\,\Delta p \ge \hbar/2$.
- **1927 — Copenhagen interpretation** (Bohr, Heisenberg) and the fifth Solvay Conference, where Einstein and Bohr began their famous debates. Einstein objected: "God does not play dice."
- **1928 — Dirac equation:** Paul Dirac combined quantum mechanics with special relativity, naturally explaining electron spin and predicting **antimatter** (the positron, discovered by Carl Anderson in 1932).
- **1930s — Abstract formulation:** Dirac's *Principles of Quantum Mechanics* (1930) and von Neumann's *Mathematical Foundations* (1932) placed the theory on rigorous Hilbert-space foundations.

## 8. Summary of Key Results

| Discovery | Year | Key equation | Significance |
|---|---|---|---|
| Planck: blackbody | 1900 | $E = nh\nu$ | Energy quantization; birth of quantum theory |
| Einstein: photoelectric effect | 1905 | $K_{\max} = h\nu - \phi$ | Light consists of photons |
| Rutherford: nucleus | 1911 | — | Planetary atom, classically unstable |
| Bohr: hydrogen atom | 1913 | $E_n = -13.6\text{ eV}/n^2$ | Quantized atomic energy levels |
| Franck–Hertz | 1914 | — | Direct evidence of discrete levels |
| Compton scattering | 1923 | $\Delta\lambda = \frac{h}{m_ec}(1 - \cos\theta)$ | Photons carry momentum |
| de Broglie: matter waves | 1924 | $\lambda = h/p$ | Particles have wave properties |
| Davisson–Germer | 1927 | Bragg: $n\lambda = d\sin\theta$ | Electron diffraction confirms matter waves |

**Fundamental constants:** $h = 6.626\times10^{-34}$ J·s; $\hbar = 1.055\times10^{-34}$ J·s; $hc = 1240$ eV·nm; $a_0 = 0.0529$ nm; $\alpha \approx 1/137$; Rydberg energy 13.6 eV; electron Compton wavelength 2.43 pm.

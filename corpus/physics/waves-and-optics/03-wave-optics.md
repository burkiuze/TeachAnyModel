---
title: Wave Optics - Interference, Diffraction and Coherence
field: Physics
subfield: Waves and Optics
level: undergraduate
keywords: [Huygens' principle, Young's double-slit experiment, interference, coherence, thin-film interference, Michelson interferometer, LIGO, single-slit diffraction, diffraction grating, Rayleigh criterion, resolving power, X-ray diffraction, Bragg's law, holography, lasers]
---

# Wave Optics: Interference, Diffraction and Coherence

When light passes through openings or around obstacles comparable in size to its wavelength, or when light waves from different paths combine, ray optics fails and the **wave nature** of light becomes evident. Wave optics explains the colors of soap bubbles, the resolution limit of telescopes and microscopes, the iridescence of butterfly wings, CD rainbows, holograms, and the detection of gravitational waves.

## 1. Huygens' Principle

Christiaan Huygens (1678) proposed that **every point on a wavefront acts as a source of secondary spherical wavelets**; the new wavefront is the envelope of these wavelets. Huygens' principle explains reflection, refraction and — with Fresnel's addition of interference between wavelets (the Huygens–Fresnel principle) — diffraction.

The wave theory of light competed with Newton's corpuscular theory for over a century. It triumphed after Thomas Young's double-slit experiment (1801) and Augustin-Jean Fresnel's diffraction theory (1818). Ironically, when Siméon Poisson argued that Fresnel's theory absurdly predicted a bright spot at the center of a circular object's shadow, François Arago looked and found the spot — now called the **Poisson spot** or Arago spot.

## 2. Coherence

Stable interference patterns require **coherent** sources: waves with a constant phase relationship (same frequency and fixed phase difference).
- Two separate light bulbs are incoherent — their phases fluctuate randomly every few femtoseconds, so interference averages out.
- Coherence is achieved by splitting light from one source (division of wavefront, as in Young's slits; or division of amplitude, as in thin films and interferometers) or by using **lasers**, which emit highly coherent light.
- **Coherence length** $\ell_c \approx \lambda^2/\Delta\lambda$: the path difference over which interference remains visible. White light: ~1 μm; a sodium lamp: ~0.6 mm; a stabilized laser: kilometers or more.

## 3. Young's Double-Slit Experiment

Coherent light of wavelength $\lambda$ passes through two narrow slits separated by distance $d$ and falls on a screen at distance $L \gg d$. Light from the two slits travels paths differing by
$$\Delta = d\sin\theta$$

**Bright fringes (constructive interference):**
$$\boxed{d\sin\theta = m\lambda, \qquad m = 0, \pm1, \pm2, \ldots}$$
**Dark fringes (destructive interference):**
$$d\sin\theta = \left(m + \tfrac12\right)\lambda$$

For small angles, $\sin\theta \approx \tan\theta = y/L$, giving fringe positions $y_m = \frac{m\lambda L}{d}$ and **fringe spacing**
$$\boxed{\Delta y = \frac{\lambda L}{d}}$$

**Intensity pattern** (ignoring single-slit diffraction): with phase difference $\phi = \frac{2\pi d\sin\theta}{\lambda}$,
$$I = I_{\max}\cos^2\left(\frac{\phi}{2}\right) = I_{\max}\cos^2\left(\frac{\pi d\sin\theta}{\lambda}\right)$$
Energy is not destroyed at dark fringes; it is redistributed to bright fringes, where intensity is four times that from a single slit (amplitudes add, then square).

### Worked example 3.1
Red laser light (650 nm) passes through slits 0.25 mm apart onto a screen 2 m away. Fringe spacing: $\Delta y = \frac{(650\times10^{-9})(2)}{0.25\times10^{-3}} = 5.2$ mm. Young used this kind of measurement to make the first determinations of the wavelengths of visible light.

### Quantum significance
The double-slit experiment performed with single photons, electrons, neutrons, atoms, and even large molecules (C₆₀ fullerenes, and molecules with over 2000 atoms) builds up the same interference pattern one particle at a time. Yet if one determines which slit each particle passes through, the pattern disappears. Richard Feynman called this "a phenomenon which is impossible, absolutely impossible, to explain in any classical way, and which has in it the heart of quantum mechanics."

## 4. Thin-Film Interference

Light reflecting from the top and bottom surfaces of a thin film (soap bubble, oil slick, anti-reflective coating) interferes. Two effects determine the outcome:
1. **Path difference:** the light reflected from the bottom surface travels an extra $2t$ in the film (at normal incidence), corresponding to $2nt$ in optical path length.
2. **Phase change on reflection:** reflection from a medium of **higher** refractive index introduces a phase shift of $\pi$ (half a wavelength); reflection from lower index introduces none.

For a film with higher index than the media on both sides (soap film in air), exactly one reflection is phase-shifted, so:
- **Constructive (bright):** $2nt = (m + \frac12)\lambda$
- **Destructive (dark):** $2nt = m\lambda$

When both or neither reflections are phase-shifted (e.g. a coating with $n_{\text{air}} < n_{\text{film}} < n_{\text{glass}}$), the conditions swap:
- **Destructive:** $2nt = (m + \frac12)\lambda$; the thinnest anti-reflective layer is a **quarter-wave** thick: $t = \frac{\lambda}{4n}$.

**Examples:**
- **Soap bubbles and oil slicks** show swirling colors because thickness varies and different wavelengths interfere constructively at different thicknesses. A soap film turns black just before it pops: when $t \ll \lambda$, the phase shift alone makes reflection destructive for all colors.
- **Anti-reflection coatings** on eyeglasses and camera lenses: MgF₂ ($n = 1.38$) on glass. For 550 nm, $t = 550/(4\times1.38) \approx 100$ nm. The residual purplish reflection comes from red and blue, which are less perfectly canceled.
- **Newton's rings:** circular fringes formed by the air gap between a curved lens and a flat plate — used to test optical surfaces.
- **Structural color:** the iridescent blues of Morpho butterflies, peacock feathers and beetle shells come from microscopic multilayer structures, not pigments.
- **Dielectric mirrors and filters:** stacks of alternating high- and low-index quarter-wave layers can reflect more than 99.999% of light at a design wavelength — used in lasers and LIGO.

## 5. Interferometers

### Michelson interferometer
A beam splitter divides light into two perpendicular arms; mirrors reflect the beams back to recombine. Moving one mirror by $\lambda/2$ shifts the pattern by one fringe (the path changes by $\lambda$). Michelson interferometers can measure distances to a small fraction of a wavelength.
- **Michelson–Morley experiment (1887):** no fringe shift was detected as Earth moved through the supposed aether, a key experimental foundation of special relativity.
- **LIGO** (Laser Interferometer Gravitational-Wave Observatory): Michelson interferometers with 4 km arms (with Fabry–Pérot cavities folding the light path many times) detect length changes of about $10^{-18}$ m — a thousandth of a proton diameter — caused by passing gravitational waves. The first detection (GW150914, from two merging black holes ~1.3 billion light-years away) was made on 14 September 2015 (Nobel 2017 to Weiss, Barish and Thorne).
- **Optical coherence tomography (OCT):** low-coherence interferometry images the retina in micrometer-resolution cross-sections.
- Other interferometers: Mach–Zehnder (used in quantum optics), Fabry–Pérot (high-resolution spectroscopy, laser cavities), Sagnac (fiber-optic gyroscopes for navigation).

## 6. Single-Slit Diffraction

Light passing through a single slit of width $a$ spreads out. Dividing the slit into pairs of strips whose wavelets cancel gives **dark fringes** at
$$\boxed{a\sin\theta = m\lambda, \qquad m = \pm1, \pm2, \ldots}$$
(Note: $m = 0$ is the central **bright** maximum.)

The intensity distribution is
$$I = I_0\left(\frac{\sin\beta}{\beta}\right)^2, \qquad \beta = \frac{\pi a\sin\theta}{\lambda}$$
The central maximum is twice as wide as the others and contains about 90% of the light energy; secondary maxima have intensities of ~4.5%, 1.6%, 0.8%... of the central peak.

**Key insight:** the narrower the slit, the **wider** the diffraction pattern ($\theta \approx \lambda/a$). Confining a wave in space spreads it in angle — the wave analog of the Heisenberg uncertainty principle ($\Delta x\,\Delta p_x \gtrsim \hbar$).

**Real double slits:** the observed double-slit pattern is the two-slit interference pattern modulated by the single-slit diffraction envelope. Interference maxima falling on diffraction minima are "missing orders".

## 7. Circular Apertures and Resolution

A circular aperture of diameter $D$ produces a central bright disk (the **Airy disk**) surrounded by faint rings. The first dark ring is at
$$\sin\theta = 1.22\frac{\lambda}{D}$$

### Rayleigh criterion
Two point sources are just resolvable when the central maximum of one falls on the first minimum of the other:
$$\boxed{\theta_{\min} \approx 1.22\frac{\lambda}{D}}$$
Diffraction sets a fundamental limit on the resolution of all optical instruments.

| Instrument | Aperture | Approximate resolution (visible) |
|---|---|---|
| Human eye | ~5 mm pupil | ~0.5–1 arcmin (also limited by retina) |
| Amateur telescope | 20 cm | ~0.7 arcsec |
| Hubble Space Telescope | 2.4 m | ~0.05 arcsec |
| Event Horizon Telescope | Earth-sized radio array, 1.3 mm wavelength | ~20 microarcseconds |

The **Event Horizon Telescope** combined radio dishes across the planet (very-long-baseline interferometry) to image the shadow of the supermassive black hole in the galaxy M87 (published 2019) and of Sagittarius A* in our galaxy (2022).

**Why astronomers build big telescopes:** larger apertures give both more light and finer resolution. **Why radio telescopes are enormous:** radio wavelengths are ~10⁵–10⁶ times longer than visible light. **Why blue-ray discs hold more data than CDs:** shorter laser wavelengths (405 nm vs. 780 nm) and higher numerical aperture lenses focus to smaller spots.

**Pointillism** paintings and pixelated screens rely on our eyes' limited resolution: from far enough away, separate dots blend into continuous colors.

## 8. Diffraction Gratings

A **diffraction grating** has a large number $N$ of equally spaced slits (or grooves) with spacing $d$. Maxima occur at the same angles as for two slits:
$$\boxed{d\sin\theta = m\lambda}$$
but they become extremely **sharp and bright** (width ∝ $1/N$, intensity ∝ $N^2$). Different wavelengths diffract to different angles, so gratings are the core of **spectrometers**.

**Resolving power:** $R = \frac{\lambda}{\Delta\lambda} = Nm$. A grating with 10 000 illuminated lines in first order can distinguish wavelengths differing by 1 part in 10 000 — enough to resolve the sodium D lines (589.0 and 589.6 nm, requiring $R \approx 1000$).

**Worked example 8.1:** a grating has 600 lines/mm, so $d = 1/600$ mm $= 1.667$ μm. For green light (532 nm), first order: $\sin\theta = 0.532/1.667 = 0.319 \Rightarrow \theta \approx 18.6°$. Highest observable order: $m_{\max} = \lfloor d/\lambda\rfloor = 3$.

**Applications of spectroscopy:** identifying elements in stars (each element has a unique spectral "fingerprint" — helium was discovered in the Sun's spectrum in 1868 before being found on Earth), measuring redshifts, chemical analysis, and telecommunications (wavelength-division multiplexing). CDs and DVDs act as reflection gratings, which is why they show rainbows.

## 9. X-Ray Diffraction and Bragg's Law

Crystals have regularly spaced atomic planes with spacings ~0.1–1 nm, comparable to X-ray wavelengths. X-rays reflecting from successive planes interfere constructively when
$$\boxed{2d\sin\theta = m\lambda}$$
(**Bragg's law**; $\theta$ is measured from the planes, not the normal). William Henry and William Lawrence Bragg (father and son) shared the 1915 Nobel Prize; Lawrence, aged 25, remains one of the youngest laureates.

X-ray crystallography revealed the structures of salt, diamond, DNA (Rosalind Franklin's "Photo 51" was critical evidence for Watson and Crick's 1953 double helix model), proteins (myoglobin, hemoglobin), vitamin B₁₂ and penicillin (Dorothy Hodgkin), the ribosome, and countless drug targets. Electron and neutron diffraction work similarly, using the de Broglie waves of particles.

## 10. Holography

A **hologram** records the interference pattern between light scattered from an object and a coherent reference beam. When illuminated by the reference beam, the hologram diffracts light to reconstruct the original wavefront — including phase information — so the viewer sees a true three-dimensional image with parallax. Invented by Dennis Gabor (1947, Nobel 1971) and made practical by lasers in the 1960s. Applications: security features on banknotes and credit cards, holographic data storage, interferometric measurement of tiny deformations, and heads-up displays.

## 11. Lasers

**LASER** = Light Amplification by Stimulated Emission of Radiation. Einstein (1917) predicted **stimulated emission**: an incoming photon can trigger an excited atom to emit an identical photon (same frequency, phase, direction and polarization). With a **population inversion** (more atoms in an excited state than the lower state, achieved by "pumping") and an optical cavity (mirrors providing feedback), light is amplified into an intense, coherent beam. The first laser (ruby) was built by Theodore Maiman in 1960.

Laser light is:
- **Monochromatic** (very narrow linewidth)
- **Coherent** (long coherence length)
- **Directional** (low divergence, approaching the diffraction limit $\theta \sim \lambda/D$)
- **Intense** (can be focused to enormous power densities)

Applications: fiber-optic communication, barcode scanners, laser printers, eye surgery (LASIK), cutting and welding, LIDAR (self-driving cars, mapping), spectroscopy, atomic clocks, gravitational-wave detection, laser cooling, and fusion research (the National Ignition Facility achieved fusion ignition in December 2022).

## 12. Summary

| Phenomenon | Condition / Formula |
|---|---|
| Double-slit bright fringes | $d\sin\theta = m\lambda$ |
| Fringe spacing | $\Delta y = \lambda L/d$ |
| Double-slit intensity | $I = I_{\max}\cos^2(\pi d\sin\theta/\lambda)$ |
| Thin film, one phase flip, bright | $2nt = (m + \frac12)\lambda$ |
| Quarter-wave AR coating | $t = \lambda/(4n)$ |
| Single-slit dark fringes | $a\sin\theta = m\lambda$ ($m \neq 0$) |
| Single-slit intensity | $I = I_0(\sin\beta/\beta)^2$ |
| Rayleigh criterion | $\theta_{\min} = 1.22\lambda/D$ |
| Grating maxima | $d\sin\theta = m\lambda$ |
| Grating resolving power | $R = \lambda/\Delta\lambda = Nm$ |
| Bragg's law | $2d\sin\theta = m\lambda$ |
| Coherence length | $\ell_c \approx \lambda^2/\Delta\lambda$ |

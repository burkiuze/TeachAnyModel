---
title: Geometric Optics - Reflection, Refraction, Mirrors, Lenses and Optical Instruments
field: Physics
subfield: Waves and Optics
level: high-school to undergraduate
keywords: [ray optics, law of reflection, Snell's law, refractive index, total internal reflection, optical fiber, dispersion, rainbow, Fermat's principle, plane mirror, spherical mirror, mirror equation, thin lens equation, magnification, lensmaker's equation, human eye, myopia, hyperopia, microscope, telescope, aberrations]
---

# Geometric Optics: Reflection, Refraction, Mirrors, Lenses and Optical Instruments

When light interacts with objects much larger than its wavelength (visible light: 400–700 nm), its wave nature can be ignored and light can be modeled as **rays** traveling in straight lines. This approximation, **geometric (ray) optics**, explains mirrors, lenses, cameras, eyeglasses, microscopes, telescopes and optical fibers.

## 1. Fermat's Principle

Pierre de Fermat (1662) proposed that light traveling between two points follows the path that takes the **least time** (more precisely, a path of stationary optical path length $\int n\,ds$). Both the law of reflection and Snell's law follow from this single principle. It foreshadowed the principle of least action in mechanics and, ultimately, Feynman's path-integral picture in which light "tries all paths" and paths near the stationary one interfere constructively.

## 2. Reflection

### Law of reflection
The angle of reflection equals the angle of incidence, both measured from the **normal** (perpendicular) to the surface, and the incident ray, reflected ray and normal lie in the same plane:
$$\theta_r = \theta_i$$
- **Specular reflection** from smooth surfaces (mirrors, calm water) produces images.
- **Diffuse reflection** from rough surfaces scatters light in all directions — which is why we can see non-luminous objects from any angle.

### Plane mirrors
A plane mirror forms a **virtual** image (light does not actually come from it), located as far behind the mirror as the object is in front, upright, the same size, and left–right (more precisely, front–back) reversed. To see your full body you need a mirror only half your height, regardless of distance. Two mirrors at angle $\theta$ produce $\frac{360°}{\theta} - 1$ images (when this is an integer); this is the principle of kaleidoscopes. **Corner-cube retroreflectors** (three mutually perpendicular mirrors) send light straight back to its source — used on bicycles, road signs and on the Moon for laser ranging.

## 3. Refraction

### Refractive index
Light slows down in a material. The **refractive index** is the ratio of the speed of light in vacuum to that in the material:
$$n = \frac cv \ge 1$$

| Material | $n$ (at 589 nm) |
|---|---|
| Vacuum | 1 (exactly) |
| Air (STP) | 1.000293 |
| Water | 1.333 |
| Ethanol | 1.361 |
| Fused silica | 1.458 |
| Crown glass | ~1.52 |
| Flint glass | ~1.6–1.9 |
| Cubic zirconia | ~2.15 |
| Diamond | 2.417 |
| Silicon (infrared, 1.5 μm) | ~3.48 |

When light enters a medium, its **frequency stays the same**, while its speed and wavelength decrease: $\lambda_n = \lambda_0/n$.

**Microscopic picture:** the light's electric field drives the electrons in the material to oscillate; they radiate secondary waves that combine with the incident wave to produce a wave whose phase advances more slowly. Photons do not literally "slow down" between atoms.

### Snell's law
$$\boxed{n_1\sin\theta_1 = n_2\sin\theta_2}$$
Light bends **toward the normal** when entering a denser medium (higher $n$) and **away from the normal** when entering a less dense medium. Discovered by Ibn Sahl (984 CE) and rediscovered by Willebrord Snell (1621).

**Derivation from Fermat's principle:** the travel time from point A (height $a$ in medium 1) to point B (depth $b$ in medium 2), crossing the boundary at horizontal position $x$, is $t = \frac{\sqrt{a^2 + x^2}}{v_1} + \frac{\sqrt{b^2 + (d - x)^2}}{v_2}$. Setting $dt/dx = 0$ gives $\frac{\sin\theta_1}{v_1} = \frac{\sin\theta_2}{v_2}$, i.e. $n_1\sin\theta_1 = n_2\sin\theta_2$. (Analogy: a lifeguard reaching a drowning swimmer runs farther on sand, where they are fast, to swim less in water, where they are slow.)

**Everyday effects:**
- A straw in water looks bent; pools look shallower than they are (apparent depth $\approx$ real depth $/n$ for near-normal viewing; a 2 m pool looks about 1.5 m deep).
- Mirages: hot air near a road has lower $n$, bending light from the sky upward so it appears as "water" on the road.
- Stars twinkle because turbulent air with varying $n$ deflects their light.
- The Sun is visible for a couple of minutes after it has geometrically set, because atmospheric refraction bends its light (~0.5° at the horizon).

### Total internal reflection
When light goes from a denser to a less dense medium ($n_1 > n_2$), the refracted angle reaches 90° at the **critical angle**:
$$\boxed{\sin\theta_c = \frac{n_2}{n_1}}$$
For $\theta_1 > \theta_c$, **all** light is reflected — no refraction occurs.
- Water–air: $\theta_c = 48.6°$. Glass–air: ~41°. Diamond–air: **24.4°** — the small critical angle traps light inside a well-cut diamond, which reflects internally many times before escaping through the top, causing its brilliance.
- **Optical fibers:** light is trapped in a high-index glass core surrounded by lower-index cladding, guiding it around bends with very low loss (~0.2 dB/km at 1550 nm). Fiber-optic cables carry the vast majority of global internet traffic, including undersea cables between continents. Charles Kao recognized the potential of ultra-pure glass fibers (Nobel 2009).
- Endoscopes, binocular prisms (porro prisms), and fingerprint scanners use total internal reflection.
- **Frustrated total internal reflection:** bringing a second medium within about a wavelength of the surface lets some light "tunnel" through — an optical analog of quantum tunneling.

### Dispersion and the rainbow
The refractive index depends on wavelength (**dispersion**): for glass and water, $n$ is larger for violet than for red. A prism therefore spreads white light into a spectrum (Newton's experiments, 1666, showed white light is a mixture of colors).

**Rainbows** form when sunlight refracts into spherical raindrops, reflects once off the back, and refracts out. The concentration of rays at the minimum deviation angle produces a bright arc at about **42°** from the antisolar point (the point directly opposite the Sun), with red on the outside and violet inside. A fainter **secondary rainbow** (two internal reflections) appears at about 51°, with colors reversed. The darker sky between them is **Alexander's dark band**. You can only see a rainbow with the Sun behind you, and each observer sees their own rainbow.

## 4. Spherical Mirrors

A spherical mirror with radius of curvature $R$ has **focal length**
$$f = \frac R2$$
- **Concave (converging) mirror:** $f > 0$. Parallel rays converge at the focal point. Used in shaving/makeup mirrors, reflecting telescopes, car headlights (bulb at focus produces a parallel beam), solar furnaces.
- **Convex (diverging) mirror:** $f < 0$. Gives a wide field of view with diminished upright virtual images. Used as car side mirrors ("objects in mirror are closer than they appear"), store security mirrors.

### Mirror equation and magnification
$$\boxed{\frac{1}{d_o} + \frac{1}{d_i} = \frac1f}, \qquad \boxed{m = -\frac{d_i}{d_o} = \frac{h_i}{h_o}}$$

**Sign conventions (real-is-positive):**
- $d_o > 0$ for real objects (in front of the mirror).
- $d_i > 0$ for real images (in front of the mirror, light actually converges there); $d_i < 0$ for virtual images (behind the mirror).
- $f > 0$ concave, $f < 0$ convex.
- $m > 0$ upright image; $m < 0$ inverted; $|m| > 1$ enlarged.

### Image formation by a concave mirror

| Object position | Image |
|---|---|
| Beyond $C$ ($d_o > 2f$) | Real, inverted, reduced, between $f$ and $2f$ |
| At $C$ ($d_o = 2f$) | Real, inverted, same size, at $2f$ |
| Between $C$ and $F$ | Real, inverted, enlarged, beyond $2f$ |
| At $F$ | No image (rays emerge parallel; image at infinity) |
| Inside $F$ ($d_o < f$) | Virtual, upright, enlarged (magnifying mirror) |

**Spherical aberration:** spherical mirrors focus rays far from the axis slightly closer than paraxial rays. **Parabolic mirrors** focus all rays parallel to the axis exactly — used in large telescopes and satellite dishes. (The Hubble Space Telescope's primary mirror was famously ground to a slightly wrong shape, about 2.2 μm too flat at the edges; corrective optics installed in 1993 fixed it.)

## 5. Thin Lenses

A lens refracts light at two curved surfaces.
- **Converging (convex) lens:** thicker in the middle, $f > 0$.
- **Diverging (concave) lens:** thinner in the middle, $f < 0$.

### Thin lens equation
The same form as the mirror equation:
$$\boxed{\frac{1}{d_o} + \frac{1}{d_i} = \frac1f}, \qquad m = -\frac{d_i}{d_o}$$
For lenses, real images form on the **opposite** side from the object ($d_i > 0$); virtual images on the same side ($d_i < 0$).

### Lensmaker's equation
$$\boxed{\frac1f = (n - 1)\left(\frac{1}{R_1} - \frac{1}{R_2}\right)}$$
($R > 0$ if the center of curvature is on the outgoing side of the light). A lens's focal length depends on the surrounding medium: replace $n$ by $n_{\text{lens}}/n_{\text{medium}}$. This is why you can't see clearly underwater: the cornea's focusing power nearly vanishes because water's index (1.33) is close to the cornea's (1.376). Goggles restore an air gap.

### Optical power
$P = 1/f$, measured in **diopters** (D = m⁻¹). A +2.5 D reading lens has $f = 40$ cm. Thin lenses in contact add powers: $P = P_1 + P_2$.

### Ray diagrams (three principal rays for a converging lens)
1. A ray parallel to the axis refracts through the far focal point.
2. A ray through the center of the lens passes undeviated.
3. A ray through the near focal point emerges parallel to the axis.

### Worked example 5.1
**Problem:** An object 4 cm tall is 30 cm from a converging lens with $f = 10$ cm. Find the image.
**Solution:** $\frac{1}{d_i} = \frac{1}{10} - \frac{1}{30} = \frac{2}{30} \Rightarrow d_i = 15$ cm (real, opposite side). $m = -15/30 = -0.5$: inverted, 2 cm tall.

### Worked example 5.2
**Problem:** The same lens with the object at 6 cm.
**Solution:** $\frac{1}{d_i} = \frac{1}{10} - \frac16 = -\frac{4}{60} \Rightarrow d_i = -15$ cm (virtual, same side). $m = -(-15)/6 = +2.5$: upright and enlarged — a magnifying glass.

### Two-lens systems
The image formed by the first lens serves as the object for the second. Total magnification is the product $m = m_1m_2$.

## 6. The Human Eye

| Part | Function |
|---|---|
| Cornea | Provides ~2/3 of the eye's focusing power (~43 D) |
| Aqueous humor | Fluid maintaining pressure |
| Iris and pupil | Adjustable aperture (2–8 mm diameter) |
| Crystalline lens | Adjustable focusing (~15–20 D in young adults) |
| Vitreous humor | Gel filling the eyeball |
| Retina | Light-sensitive layer: ~120 million rods (dim light, no color) and ~6 million cones (color, three types: S, M, L) |
| Fovea | Central region densely packed with cones; sharpest vision |
| Optic nerve | Carries signals to the brain; creates a blind spot where it exits |

The total power of a relaxed eye is about 60 D. The image on the retina is real and inverted; the brain interprets it as upright.

**Accommodation:** ciliary muscles change the lens's shape to focus at different distances. The **near point** (closest clear focus) is about 25 cm for a young adult and recedes with age as the lens stiffens (**presbyopia**), typically requiring reading glasses after age ~45. The **far point** of a normal eye is at infinity.

### Vision defects and correction

| Condition | Problem | Correction |
|---|---|---|
| Myopia (nearsightedness) | Eye too long or too powerful; distant images focus in front of retina; far point closer than infinity | Diverging lens (negative diopters) |
| Hyperopia (farsightedness) | Eye too short or too weak; near point too far | Converging lens (positive diopters) |
| Presbyopia | Loss of accommodation with age | Converging reading lenses, bifocals, progressives |
| Astigmatism | Cornea not rotationally symmetric; different focus in different planes | Cylindrical (toric) lens |

**Worked example 6.1:** A myopic person's far point is 50 cm. The corrective lens (neglecting distance from the eye) must form a virtual image at 50 cm of objects at infinity: $\frac1f = \frac1\infty + \frac{1}{-0.5} \Rightarrow f = -0.5$ m, power $= -2$ D.

**Resolution of the eye:** about 1 arcminute (limited by cone spacing and diffraction at the pupil) — enough to read a 20/20 eye chart line or to distinguish two car headlights about 1.5 m apart at roughly 5 km.

## 7. Optical Instruments

### Magnifying glass
A converging lens held so the object is just inside the focal point produces an enlarged virtual image. Angular magnification (image at infinity): $M = \frac{25\text{ cm}}{f}$. A 5 cm focal-length lens gives 5×.

### Camera
A converging lens forms a real, inverted, reduced image on a sensor. Focusing moves the lens relative to the sensor. The **f-number** $N = f/D$ (focal length / aperture diameter) controls light-gathering: each "stop" ($f/2.8$, $f/4$, $f/5.6$, ...) halves the light. Smaller apertures (larger $N$) increase **depth of field**.

### Compound microscope
An **objective** lens with short focal length forms a real, enlarged image, which the **eyepiece** magnifies further:
$$M \approx -\frac{L}{f_o}\cdot\frac{25\text{ cm}}{f_e}$$
($L$ = tube length, typically 16 cm). Optical microscopes are limited by diffraction to resolving about half the wavelength (~200 nm) — the Abbe limit $d = \frac{\lambda}{2\,\text{NA}}$. Super-resolution techniques (STED, PALM/STORM; Nobel Chemistry 2014) circumvent this using fluorescence tricks; electron microscopes use the much shorter de Broglie wavelength of electrons.

### Telescopes
- **Refracting telescope** (Galileo, Kepler): a long-focal-length objective lens and short-focal-length eyepiece. Angular magnification $M = -f_o/f_e$.
- **Reflecting telescope** (Newton, 1668): a concave mirror replaces the objective. Mirrors have no chromatic aberration, can be supported from behind, and can be made very large. All major research telescopes are reflectors: the Keck telescopes (10 m), the James Webb Space Telescope (6.5 m segmented beryllium mirror), and the Extremely Large Telescope under construction (39 m).
- The most important property of a research telescope is not magnification but **light-gathering power** (∝ aperture area) and **angular resolution** (diffraction limit $\theta \approx 1.22\lambda/D$). Ground telescopes use **adaptive optics** (deformable mirrors) to correct atmospheric blurring.

## 8. Aberrations

Real lenses and mirrors deviate from ideal focusing:
- **Spherical aberration:** rays far from the axis focus at a different point. Fixed with aspheric surfaces or by stopping down the aperture.
- **Chromatic aberration** (lenses only): different colors focus at different points because of dispersion. Corrected with **achromatic doublets** combining crown and flint glass (invented by Chester Moor Hall and John Dollond in the 18th century).
- **Coma, astigmatism, field curvature, distortion:** off-axis aberrations; complex multi-element lens designs balance them.

## 9. Summary

| Concept | Formula |
|---|---|
| Refractive index | $n = c/v$ |
| Law of reflection | $\theta_r = \theta_i$ |
| Snell's law | $n_1\sin\theta_1 = n_2\sin\theta_2$ |
| Critical angle | $\sin\theta_c = n_2/n_1$ |
| Mirror focal length | $f = R/2$ |
| Mirror/lens equation | $1/d_o + 1/d_i = 1/f$ |
| Magnification | $m = -d_i/d_o$ |
| Lensmaker | $1/f = (n-1)(1/R_1 - 1/R_2)$ |
| Power | $P = 1/f$ (diopters) |
| Magnifier | $M = 25\text{ cm}/f$ |
| Telescope | $M = -f_o/f_e$ |
| Microscope | $M \approx -(L/f_o)(25\text{ cm}/f_e)$ |

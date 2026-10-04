---
title: Electrostatics - Charge, Electric Field, Gauss's Law, Potential and Capacitance
field: Physics
subfield: Electromagnetism
level: high-school to undergraduate
keywords: [electric charge, Coulomb's law, electric field, field lines, electric dipole, Gauss's law, electric flux, conductors, electric potential, voltage, equipotential, capacitance, capacitor, dielectric, energy density, electron volt]
---

# Electrostatics: Charge, Electric Field, Gauss's Law, Potential and Capacitance

Electromagnetism governs nearly everything in daily life apart from gravity: the structure of atoms and molecules, chemical bonds, friction, contact forces, light, electronics and nerve signals. **Electrostatics** studies charges at rest and the fields they create.

## 1. Electric Charge

### Properties of charge
1. **Two kinds:** positive and negative (names chosen by Benjamin Franklin). Like charges repel; unlike charges attract.
2. **Quantized:** all free charges are integer multiples of the elementary charge
   $$e = 1.602176634 \times 10^{-19} \text{ C (exact since 2019)}$$
   Electron: $-e$; proton: $+e$. (Quarks carry $\pm\frac13e$ or $\pm\frac23e$ but are confined inside hadrons.) Robert Millikan's oil-drop experiment (1909) first demonstrated quantization and measured $e$.
3. **Conserved:** the total charge of an isolated system never changes. Charge can be transferred, and particle–antiparticle pairs can be created or annihilated, but the net charge is always conserved.
4. **Invariant:** charge is the same in all reference frames.

SI unit: the **coulomb** (C), the charge carried by a current of 1 A in 1 s. One coulomb is about $6.24 \times 10^{18}$ elementary charges — an enormous amount in electrostatic terms.

### Conductors, insulators and charging
- **Conductors** (metals, ionized gases, electrolytes) contain mobile charges. In metals, outer electrons are delocalized ("electron sea").
- **Insulators** (glass, rubber, plastics, dry wood) hold electrons tightly.
- **Semiconductors** (Si, Ge) are intermediate and tunable by doping and temperature.

Methods of charging:
- **Friction (triboelectric effect):** rubbing transfers electrons between materials (e.g. rubbing a balloon on hair makes the balloon negative). The **triboelectric series** ranks materials by their tendency to gain or lose electrons.
- **Conduction:** touching a charged object to a neutral conductor shares charge.
- **Induction:** bringing a charged object near a conductor redistributes its charges; grounding one side and then removing the ground leaves a net charge of opposite sign — without contact.
- **Polarization:** a charged object attracts neutral insulators (a charged comb attracting paper bits) by slightly displacing electron clouds within molecules, creating induced dipoles.

## 2. Coulomb's Law

Charles-Augustin de Coulomb (1785), using a torsion balance, established that the force between two point charges is
$$\boxed{F = k\frac{|q_1q_2|}{r^2} = \frac{1}{4\pi\varepsilon_0}\frac{|q_1q_2|}{r^2}}$$
directed along the line joining them (repulsive for like charges, attractive for unlike).

- $k = \frac{1}{4\pi\varepsilon_0} = 8.988 \times 10^9$ N·m²/C²
- $\varepsilon_0 = 8.854 \times 10^{-12}$ C²/(N·m²) — the **vacuum permittivity**

Vector form, force on $q_2$ due to $q_1$: $\vec F_{12} = k\frac{q_1q_2}{r^2}\hat r_{12}$.

**Superposition principle:** the net force on a charge is the vector sum of forces from all other charges individually. This linearity is a fundamental, experimentally verified property of electromagnetism.

### Comparison with gravity
Both are inverse-square laws, but:
- Gravity is always attractive; electric forces can attract or repel, so they cancel in neutral matter.
- In a hydrogen atom, the electric attraction between proton and electron is about $2.3 \times 10^{39}$ times their gravitational attraction.

### Worked example 2.1 – Hydrogen atom
In the Bohr model the electron orbits the proton at $r = 5.29 \times 10^{-11}$ m.
$F = (8.99\times10^9)\frac{(1.602\times10^{-19})^2}{(5.29\times10^{-11})^2} \approx 8.2 \times 10^{-8}$ N.
Tiny in absolute terms, but it gives the electron (mass $9.11\times10^{-31}$ kg) an acceleration of about $9\times10^{22}$ m/s².

### Worked example 2.2 – Three charges
Charges $q_1 = +2$ μC at $x = 0$, $q_2 = -3$ μC at $x = 1$ m. Where on the $x$-axis can a third charge feel zero net force?
The point must be outside the pair, on the side of the smaller-magnitude charge ($x < 0$), at distance $d$ from $q_1$:
$\frac{2}{d^2} = \frac{3}{(d+1)^2} \Rightarrow \frac{d+1}{d} = \sqrt{1.5} = 1.2247 \Rightarrow d = \frac{1}{0.2247} \approx 4.45$ m. So $x \approx -4.45$ m. (Between the charges both forces point the same way, so no balance is possible there.)

## 3. The Electric Field

Rather than "action at a distance", we say each charge creates an **electric field** $\vec E$ in the space around it, and other charges respond to the field where they are. The field is defined as force per unit positive test charge:
$$\boxed{\vec E = \frac{\vec F}{q_0}} \qquad [\text{N/C} = \text{V/m}]$$

Field of a point charge:
$$\vec E = k\frac{q}{r^2}\hat r$$
pointing away from positive charges and toward negative ones.

The field concept became essential with Faraday and Maxwell: fields carry energy and momentum, and disturbances in them propagate at the finite speed of light.

### Electric field lines
Faraday's visualization:
- Lines start on positive charges and end on negative charges (or at infinity).
- The field is tangent to the lines; the density of lines indicates field strength.
- Field lines never cross.

### Typical field strengths

| Situation | $E$ (N/C) |
|---|---|
| Fair-weather atmosphere near ground | ~100–150 |
| Inside a household wire | ~$10^{-2}$ |
| Dielectric breakdown of dry air | ~$3 \times 10^6$ |
| Across a cell membrane | ~$10^7$ |
| At the electron's orbit in hydrogen | ~$5 \times 10^{11}$ |

### Continuous charge distributions
$$\vec E = k\int\frac{dq}{r^2}\hat r, \qquad dq = \lambda\,dl,\;\sigma\,dA,\;\text{or}\;\rho\,dV$$

Standard results:
- **Infinite line charge** (linear density $\lambda$): $E = \frac{\lambda}{2\pi\varepsilon_0r}$
- **Infinite plane** (surface density $\sigma$): $E = \frac{\sigma}{2\varepsilon_0}$ (uniform, independent of distance!)
- **On the axis of a ring** (charge $Q$, radius $a$, distance $z$): $E = \frac{kQz}{(z^2 + a^2)^{3/2}}$
- **Uniformly charged sphere** (total $Q$, radius $R$): $E = \frac{kQ}{r^2}$ outside, $E = \frac{kQr}{R^3}$ inside

### Electric dipole
Two equal and opposite charges $\pm q$ separated by distance $d$ form a dipole with **dipole moment** $\vec p = q\vec d$ (pointing from $-$ to $+$).
- Far-field strength falls as $1/r^3$: on the axis $E \approx \frac{2kp}{r^3}$; on the perpendicular bisector $E \approx \frac{kp}{r^3}$.
- In a uniform external field, a dipole feels no net force but a **torque** $\vec\tau = \vec p\times\vec E$, and has potential energy $U = -\vec p\cdot\vec E$. It tends to align with the field.
- In a non-uniform field, it also feels a net force toward stronger field regions.

Many molecules are permanent dipoles (H₂O: $p = 6.2\times10^{-30}$ C·m, about 1.85 debye). Microwave ovens exploit the torque on water dipoles in an oscillating field.

### Motion of a charge in a uniform field
A charge $q$ of mass $m$ in a uniform field has constant acceleration $\vec a = q\vec E/m$ — exactly like projectile motion. This is the principle of cathode-ray tube deflection, inkjet printers, electrostatic precipitators, and particle accelerators.

## 4. Gauss's Law

### Electric flux
The **electric flux** through a surface measures the "number of field lines" passing through it:
$$\Phi_E = \int\vec E\cdot d\vec A$$
For a uniform field through a flat area: $\Phi_E = EA\cos\theta$.

### Gauss's law
> The net electric flux through any closed surface equals the net charge enclosed divided by $\varepsilon_0$.
$$\boxed{\oint\vec E\cdot d\vec A = \frac{Q_{\text{enc}}}{\varepsilon_0}}$$

Gauss's law is equivalent to Coulomb's law for static charges but is more general — it is one of **Maxwell's equations** and remains valid for moving charges. In differential form: $\nabla\cdot\vec E = \rho/\varepsilon_0$.

**Why it works:** field lines begin and end only on charges. For a point charge at the center of a sphere, $E \cdot 4\pi r^2 = \frac{q}{4\pi\varepsilon_0r^2}4\pi r^2 = \frac q{\varepsilon_0}$, independent of $r$ — a direct consequence of the inverse-square law and three-dimensional space.

### Using Gauss's law
For highly symmetric charge distributions, choose a **Gaussian surface** on which $E$ is constant and parallel (or perpendicular) to $d\vec A$.

**Example 4.1 – Uniformly charged sphere** (charge $Q$, radius $R$):
- Outside ($r > R$): sphere of radius $r$: $E(4\pi r^2) = Q/\varepsilon_0 \Rightarrow E = \frac{Q}{4\pi\varepsilon_0r^2}$ — same as a point charge.
- Inside ($r < R$): enclosed charge $Q\frac{r^3}{R^3}$: $E = \frac{Qr}{4\pi\varepsilon_0R^3}$ — grows linearly from zero.

**Example 4.2 – Infinite plane:** a "pillbox" cylinder straddling the plane, with end caps of area $A$: $2EA = \sigma A/\varepsilon_0 \Rightarrow E = \sigma/(2\varepsilon_0)$.

**Example 4.3 – Infinite line:** coaxial cylinder of radius $r$ and length $L$: $E(2\pi rL) = \lambda L/\varepsilon_0 \Rightarrow E = \lambda/(2\pi\varepsilon_0r)$.

### Conductors in electrostatic equilibrium
1. **$\vec E = 0$ inside the conductor material** (otherwise free charges would move).
2. **Any net charge resides on the surface** (from Gauss's law with a surface just inside).
3. **Just outside, $\vec E$ is perpendicular to the surface**, with magnitude $E = \sigma/\varepsilon_0$.
4. **Charge concentrates at sharp points** (smaller radius of curvature → higher $\sigma$ and $E$). This causes corona discharge and is why lightning rods are pointed.
5. **A hollow conductor shields its interior** from external static fields — a **Faraday cage**. This is why you are safe in a car struck by lightning (mainly because of the metal body, not the rubber tires), why microwave oven doors have metal mesh, and why phones lose signal in elevators.

## 5. Electric Potential

### Potential energy and potential
The electric force is conservative, so we can define a potential energy. The **electric potential** $V$ is potential energy per unit charge:
$$V = \frac{U}{q_0}, \qquad \Delta V = V_B - V_A = -\int_A^B\vec E\cdot d\vec l$$
SI unit: the **volt** (V = J/C). Potential difference is commonly called **voltage**.

Conversely, the field is the negative gradient of the potential:
$$\boxed{\vec E = -\nabla V}, \qquad E_x = -\frac{\partial V}{\partial x}$$
The field points from high to low potential. Positive charges "fall" toward lower potential; electrons move toward higher potential.

### Potential of a point charge
$$\boxed{V = k\frac{q}{r}} \qquad (V = 0 \text{ at infinity})$$
Potential is a scalar, so the potential of many charges is a simple sum: $V = k\sum\frac{q_i}{r_i}$ — usually much easier than adding field vectors.

**Potential energy of two point charges:** $U = k\frac{q_1q_2}{r}$.

### Uniform field
Between parallel plates separated by $d$ with potential difference $\Delta V$: $E = \Delta V/d$. A charge $q$ moving through potential difference $\Delta V$ gains kinetic energy $q\Delta V$.

### The electron volt
The **electron volt** (eV) is the energy gained by an electron accelerated through 1 V:
$$1 \text{ eV} = 1.602 \times 10^{-19} \text{ J}$$
Atomic and chemical energies are a few eV; visible photons carry 1.65–3.3 eV; nuclear energies are MeV; the Large Hadron Collider reaches 13.6 TeV collision energy.

### Equipotential surfaces
Surfaces of constant potential. Field lines are perpendicular to equipotentials. No work is done moving a charge along an equipotential. The surface of a conductor in equilibrium is an equipotential (and so is its entire volume).

### Worked example 5.1 – Electron gun
An electron starts from rest and is accelerated through 2000 V. Find its final speed.
$\frac12mv^2 = e\Delta V \Rightarrow v = \sqrt{\frac{2e\Delta V}{m}} = \sqrt{\frac{2(1.602\times10^{-19})(2000)}{9.109\times10^{-31}}} \approx 2.65\times10^7$ m/s ≈ 9% of the speed of light (non-relativistic treatment is adequate).

### Worked example 5.2 – Van de Graaff generator
A spherical dome of radius 0.2 m in dry air. The maximum field at its surface before breakdown is $3\times10^6$ V/m. For a sphere, $V = ER$ at the surface, so $V_{\max} = 3\times10^6 \times 0.2 = 600$ kV. Larger domes reach higher voltages.

## 6. Capacitance

A **capacitor** is two conductors separated by an insulator, holding equal and opposite charges $\pm Q$. The charge is proportional to the potential difference:
$$\boxed{Q = CV}$$
$C$ is the **capacitance**; SI unit: the **farad** (F = C/V). Practical capacitors range from picofarads to farads (supercapacitors reach thousands of farads).

### Parallel-plate capacitor
Plates of area $A$ separated by $d$ (with $d \ll \sqrt A$): $E = \sigma/\varepsilon_0 = Q/(\varepsilon_0A)$, $V = Ed$, so
$$\boxed{C = \frac{\varepsilon_0A}{d}}$$
Capacitance depends only on geometry (and the dielectric). Example: $A = 1$ m², $d = 1$ mm gives $C \approx 8.85$ nF — a farad is a very large capacitance.

Other geometries:
- Isolated sphere of radius $R$: $C = 4\pi\varepsilon_0R$ (Earth: ~710 μF)
- Spherical capacitor (radii $a < b$): $C = 4\pi\varepsilon_0\frac{ab}{b - a}$
- Cylindrical (coaxial cable), length $L$: $C = \frac{2\pi\varepsilon_0L}{\ln(b/a)}$

### Combinations
- **Parallel** (same voltage): $C_{\text{eq}} = C_1 + C_2 + \cdots$
- **Series** (same charge): $\frac{1}{C_{\text{eq}}} = \frac{1}{C_1} + \frac{1}{C_2} + \cdots$
(The reverse of resistor rules.)

### Energy stored
Charging a capacitor requires work against the growing voltage: $dW = V\,dq = \frac qC\,dq$. Integrating:
$$\boxed{U = \frac{Q^2}{2C} = \tfrac12CV^2 = \tfrac12QV}$$
The energy resides in the electric field, with **energy density**
$$u_E = \tfrac12\varepsilon_0E^2 \qquad [\text{J/m}^3]$$
This holds for any electric field, not just in capacitors.

**Applications:** camera flashes, defibrillators (~200 J delivered in milliseconds), power-supply smoothing, timing circuits, memory cells in DRAM (each bit is a tiny capacitor), touchscreens (finger changes local capacitance), condenser microphones, and energy storage in electric buses (supercapacitors).

### Dielectrics
Inserting an insulating material (dielectric) between the plates increases capacitance by the **dielectric constant** $\kappa$ (relative permittivity $\varepsilon_r$):
$$C = \kappa C_0 = \frac{\kappa\varepsilon_0A}{d}$$
**Mechanism:** the field polarizes the dielectric's molecules (aligning permanent dipoles or inducing dipoles), producing bound surface charges that partially cancel the field inside. For a fixed charge, the field and voltage drop by $\kappa$; for a fixed voltage, the stored charge increases by $\kappa$. Dielectrics also raise the breakdown voltage and allow plates to be closer together.

| Material | $\kappa$ | Dielectric strength (MV/m) |
|---|---|---|
| Vacuum | 1 (exactly) | — |
| Air (1 atm) | 1.00059 | 3 |
| Paper | ~3.5 | 16 |
| Teflon | 2.1 | 60 |
| Glass | 5–10 | ~10 |
| Water (20 °C) | 80 | — |
| Barium titanate | 1200–10 000 | ~10 |

Water's large dielectric constant weakens the attraction between ions by a factor of ~80, which is why it dissolves salts so well.

In a dielectric, Gauss's law is written with the **electric displacement** $\vec D = \varepsilon_0\vec E + \vec P = \varepsilon\vec E$: $\oint\vec D\cdot d\vec A = Q_{\text{free}}$.

## 7. Summary

| Concept | Formula |
|---|---|
| Coulomb's law | $F = kq_1q_2/r^2$, $k = 8.99\times10^9$ N·m²/C² |
| Electric field | $\vec E = \vec F/q$; point charge $E = kq/r^2$ |
| Dipole | $\vec p = q\vec d$; $\vec\tau = \vec p\times\vec E$; $U = -\vec p\cdot\vec E$ |
| Gauss's law | $\oint\vec E\cdot d\vec A = Q_{\text{enc}}/\varepsilon_0$ |
| Infinite plane | $E = \sigma/2\varepsilon_0$ |
| Conductor surface | $E = \sigma/\varepsilon_0$ |
| Potential | $\Delta V = -\int\vec E\cdot d\vec l$; $\vec E = -\nabla V$ |
| Point-charge potential | $V = kq/r$ |
| Capacitance | $Q = CV$; parallel plate $C = \varepsilon_0A/d$ |
| Energy | $U = \frac12CV^2$; $u_E = \frac12\varepsilon_0E^2$ |
| Dielectric | $C = \kappa C_0$ |

**Common mistakes:**
1. Confusing potential (a scalar, J/C) with potential energy (J) or with field (a vector).
2. Forgetting that Gauss's law is always true but only *useful* for symmetric distributions.
3. Thinking $V = 0$ implies $E = 0$ (or vice versa). Midway between equal and opposite charges, $V = 0$ but $E \neq 0$; inside a charged conducting shell, $E = 0$ but $V \neq 0$.
4. Mixing up series/parallel rules for capacitors and resistors.

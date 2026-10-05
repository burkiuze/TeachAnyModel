---
title: Electronics and Semiconductor Devices
field: Physics
subfield: Electromagnetism
level: high-school to undergraduate
keywords: [semiconductor, silicon, band gap, intrinsic carrier concentration, holes, doping, n-type, p-type, mass-action law, mobility, p-n junction, depletion region, built-in potential, diode equation, Shockley equation, rectifier, Zener diode, LED, photodiode, solar cell, fill factor, bipolar junction transistor, MOSFET, transconductance, CMOS, logic gates, binary, Boolean algebra, operational amplifier, inverting amplifier, non-inverting amplifier, RC time constant, low-pass filter, integrated circuit, Moore's law]
---

# Electronics and Semiconductor Devices

Almost every electrical device built in the last sixty years contains the same small set of ideas. A thin slice of silicon, deliberately contaminated with a trace of phosphorus or boron (often less than one atom in a million), becomes a material whose conductivity can be set by design. Two such regions placed side by side form a **p-n junction**, which lets current pass in one direction only. Add a third region, or a metal gate separated from the silicon by a thin insulator, and the result is a **transistor**: a device in which a small voltage or current controls a much larger one. Wire billions of transistors together on one chip and you have a processor, a memory or a camera sensor. Run a junction backwards and it detects light; run it forwards in the right material and it emits light.

Electronics is therefore where electromagnetism, quantum mechanics and statistical physics meet engineering. The behavior of a diode follows from Boltzmann statistics; the color of an LED follows from the band gap of a crystal; the speed of a filter follows from the time constant $RC$ of a resistor and capacitor; and the power drawn by a processor follows from the energy needed to charge a capacitor, $\tfrac12CV^2$.

This chapter covers:

- why some materials are **semiconductors**, and what the **band gap** means;
- **intrinsic** silicon, **electrons and holes**, and the **intrinsic carrier concentration**;
- **doping** to make **n-type** and **p-type** material, the **mass-action law**, **mobility**, **drift** and **diffusion**;
- the **p-n junction**, its **built-in potential** and **depletion region**, derived from first principles;
- the **Shockley diode equation**, its derivation and consequences, and **breakdown**;
- **rectifiers** and smoothed DC power supplies;
- **light-emitting diodes**, **photodiodes** and **solar cells**;
- **bipolar junction transistors** and **MOSFETs** as switches and amplifiers;
- **CMOS logic**, its power consumption, and **digital logic** in **binary**;
- **operational amplifiers** and the ideal op-amp rules;
- **RC circuits**, **time constants** and **filters**;
- **integrated circuits** and **Moore's law**;
- worked circuit examples, history, applications, misconceptions and practice problems.

The chapter assumes familiarity with Ohm's law, Kirchhoff's laws, capacitance and basic calculus. Ideas from quantum mechanics (energy levels, photons) and statistical physics (the Boltzmann factor $e^{-E/k_BT}$) are introduced where they are needed. Throughout, room temperature is taken as $T = 300$ K unless stated otherwise, where the **thermal voltage** is
$$V_T = \frac{k_BT}{q} = \frac{(1.380649\times10^{-23}\text{ J/K})(300\text{ K})}{1.602176634\times10^{-19}\text{ C}} = 25.85\text{ mV}.$$

## 1. Conductors, Insulators and Semiconductors

### Resistivity spans a vast range

No other everyday physical property varies as much between materials as electrical resistivity. A copper wire and a glass rod of the same shape differ in resistance by around twenty orders of magnitude. Semiconductors sit in between, and, crucially, their resistivity can be changed by many orders of magnitude by adding tiny amounts of impurity, by heating, by illumination or by applying an electric field.

| Material (near room temperature) | Resistivity (Ω·m) | Class |
|---|---|---|
| Silver | $1.59\times10^{-8}$ | Metal |
| Copper | $1.68\times10^{-8}$ | Metal |
| Aluminum | $2.65\times10^{-8}$ | Metal |
| Silicon, n-type, $10^{16}$ phosphorus atoms per cm³ | about $5\times10^{-3}$ | Doped semiconductor |
| Germanium, intrinsic | about 0.5 | Semiconductor |
| Silicon, intrinsic | about $3\times10^{3}$ | Semiconductor |
| Glass | $10^{10}$ to $10^{14}$ | Insulator |

Two features distinguish a semiconductor from a metal. First, the resistivity of a pure semiconductor **falls** steeply as temperature rises, whereas that of a metal rises slowly. Michael Faraday noticed this "negative temperature coefficient" in silver sulfide in 1833, long before anyone could explain it. Second, the resistivity of a semiconductor is extremely sensitive to impurities: one phosphorus atom per five million silicon atoms lowers the resistivity of silicon by a factor of nearly a million (Worked Example 3.1).

### Energy bands and the band gap

An isolated atom has sharp energy levels. When $N$ atoms are brought together into a crystal, each atomic level splits into $N$ closely spaced levels because the electron wavefunctions on neighboring atoms overlap. With $N\sim10^{23}$, these levels merge into continuous **energy bands**, separated by **band gaps** in which no electron states exist in a perfect crystal.

What matters for conduction is how the bands are filled at low temperature:

- In a **metal**, the highest occupied band is only partly full. Electrons near the top of the filled states (the **Fermi level**) can move into empty states just above them with an arbitrarily small push from an electric field, so the material conducts.
- In an **insulator** or **semiconductor**, the electrons exactly fill a set of bands. The highest filled band is the **valence band**, with top edge $E_V$; the lowest empty band is the **conduction band**, with bottom edge $E_C$. The energy difference
$$E_g = E_C - E_V$$
is the **band gap**. A completely full band carries no net current: for every electron moving one way there is another moving the opposite way, and there are no empty states into which the distribution can be shifted.

The difference between a semiconductor and an insulator is one of degree. If $E_g$ is a few times $k_BT$ or less, thermal energy lifts a useful number of electrons across the gap at room temperature. The probability of a thermal excitation of energy $E_g$ is governed by the Boltzmann factor, and since $k_BT = 0.0259$ eV at 300 K, the factor $e^{-E_g/2k_BT}$ (derived in Section 2) is about $4\times10^{-10}$ for silicon ($E_g = 1.12$ eV) but about $10^{-46}$ for diamond ($E_g = 5.47$ eV). Materials with gaps up to roughly 3 to 4 eV are conventionally called semiconductors; diamond is usually counted as an insulator, though it can be doped for special purposes.

| Material | Band gap at 300 K (eV) | Gap type | Cutoff wavelength $hc/E_g$ (nm) | Typical use |
|---|---|---|---|---|
| Germanium (Ge) | 0.66 | Indirect | 1879 | Early transistors, infrared detectors |
| Silicon (Si) | 1.12 | Indirect | 1107 | Integrated circuits, solar cells, photodiodes |
| Indium phosphide (InP) | 1.34 | Direct | 925 | Fiber-optic lasers and detectors |
| Gallium arsenide (GaAs) | 1.42 | Direct | 873 | Infrared LEDs, high-frequency transistors |
| Gallium phosphide (GaP) | 2.26 | Indirect | 549 | Early green and yellow indicator LEDs |
| Silicon carbide (4H-SiC) | 3.26 | Indirect | 380 | High-voltage power electronics |
| Gallium nitride (GaN) | 3.4 | Direct | 365 | Blue and white LEDs, power transistors |
| Diamond (C) | 5.47 | Indirect | 227 | Heat spreaders, radiation detectors |

The cutoff wavelength follows from the photon energy relation $E = hc/\lambda$ with $hc = 1239.84$ eV·nm. A photon with a longer wavelength than the cutoff does not have enough energy to lift an electron across the gap, so the material is transparent to it. This is why silicon is opaque to visible light (a polished wafer looks like a gray mirror) yet transparent at the 1550 nm wavelength used in optical fibers.

### Direct and indirect gaps

In a crystal, electron states are labeled by a crystal momentum $\hbar\vec k$ as well as by energy. In a **direct-gap** semiconductor (GaAs, InP, GaN), the lowest point of the conduction band lies at the same $\vec k$ as the highest point of the valence band, so an electron can fall across the gap and emit a photon while conserving momentum (photons carry negligible momentum compared with crystal electrons). In an **indirect-gap** material (Si, Ge), the extremes lie at different $\vec k$, so radiative recombination must also involve a lattice vibration (a **phonon**) to supply the missing momentum. That three-body process is slow, so in silicon an electron usually recombines non-radiatively, releasing heat. This single fact explains why LEDs and semiconductor lasers are made of compound semiconductors rather than silicon, even though silicon absorbs light perfectly well and makes excellent detectors and solar cells.

## 2. Intrinsic Silicon: Electrons and Holes

### The silicon crystal

Silicon is in group 14 of the periodic table, with four valence electrons. In the crystal each atom forms four covalent bonds with neighbors at the corners of a tetrahedron, arranged in the **diamond cubic** structure with lattice constant 0.5431 nm. There are 8 atoms per cubic unit cell, so the atomic density is
$$\frac{8}{(0.5431\times10^{-7}\text{ cm})^3} = 5.0\times10^{22}\text{ atoms per cm}^3.$$
At absolute zero every valence electron is locked into a bond; the valence band is full and the conduction band empty, and pure silicon is an insulator.

### Holes

At finite temperature, thermal vibrations occasionally break a bond, freeing an electron into the conduction band, where it can wander through the crystal. The broken bond left behind is a **hole**. A neighboring bound electron can hop into the hole, which effectively moves the hole the other way. Because it is the absence of a negative charge in an otherwise neutral lattice, a hole behaves exactly like a mobile particle of charge $+q$ (where $q = 1.602\times10^{-19}$ C), with its own effective mass and mobility. This is not just bookkeeping: the **Hall effect** in p-type material gives a Hall voltage of the sign expected for positive carriers, which classical free-electron theory could not explain.

A material in which electrons and holes are created only in pairs by thermal excitation is called **intrinsic**. Its electron concentration $n$ and hole concentration $p$ are equal, $n = p = n_i$, the **intrinsic carrier concentration**.

### Intrinsic carrier concentration

Statistical mechanics gives the electron and hole concentrations in terms of the position of the Fermi level $E_F$ (the energy at which a state would have a 50% chance of being occupied). When $E_F$ lies several $k_BT$ inside the gap, the Fermi–Dirac distribution reduces to a Boltzmann tail, and
$$n = N_C\,e^{-(E_C - E_F)/k_BT}, \qquad p = N_V\,e^{-(E_F - E_V)/k_BT},$$
where $N_C$ and $N_V$, the **effective densities of states** of the conduction and valence bands, are of order $10^{19}$ per cm³ in silicon and vary with temperature as $T^{3/2}$. Multiplying the two expressions, the Fermi level cancels:
$$np = N_CN_V\,e^{-(E_C - E_V)/k_BT} = N_CN_V\,e^{-E_g/k_BT}.$$
In an intrinsic material $n = p = n_i$, so
$$\boxed{n_i = \sqrt{N_CN_V}\,e^{-E_g/2k_BT} \propto T^{3/2}e^{-E_g/2k_BT}}$$
The factor of 2 in the exponent has a simple meaning: each excitation creates two carriers, and the concentration of each is set by the square root of the pair-creation probability. For silicon at 300 K the measured value is
$$n_i \approx 1.0\times10^{10}\text{ cm}^{-3}$$
(older textbooks quote $1.45\times10^{10}$ or $1.5\times10^{10}$ cm⁻³; more careful later measurements gave slightly under $1.0\times10^{10}$ cm⁻³). Comparing with the atomic density, only about one bond in $10^{13}$ is broken at room temperature.

| Property at 300 K | Si | Ge | GaAs |
|---|---|---|---|
| Band gap (eV) | 1.12 | 0.66 | 1.42 |
| Intrinsic carrier concentration (cm⁻³) | about $1.0\times10^{10}$ | about $2\times10^{13}$ | about $2\times10^{6}$ |
| Electron mobility (cm²/V·s), low doping | 1400 | 3900 | 8500 |
| Hole mobility (cm²/V·s), low doping | 450 | 1900 | 400 |
| Relative permittivity | 11.7 | 16.0 | 12.9 |
| Lattice constant (nm) | 0.5431 | 0.5658 | 0.5653 |
| Melting point (°C) | 1414 | 938 | 1238 |

### Worked Example 2.1: How sensitive is silicon to temperature?

**Problem:** Using $n_i \propto T^{3/2}e^{-E_g/2k_BT}$ with $E_g = 1.12$ eV held constant, find the factor by which $n_i$ in silicon increases between 300 K and 350 K, and estimate the temperature rise that doubles $n_i$ near room temperature.

**Solution:**

1. Write the ratio: $\dfrac{n_i(350)}{n_i(300)} = \left(\dfrac{350}{300}\right)^{3/2}\exp\left[\dfrac{E_g}{2k_B}\left(\dfrac{1}{300} - \dfrac{1}{350}\right)\right]$.
2. Power-law factor: $(350/300)^{3/2} = 1.260$.
3. With $k_B = 8.617\times10^{-5}$ eV/K: $E_g/2k_B = 1.12/(2\times8.617\times10^{-5}) = 6499$ K, and $1/300 - 1/350 = 4.762\times10^{-4}$ K⁻¹, so the exponent is $3.095$ and the exponential factor is $e^{3.095} = 22.1$.
4. Ratio $= 1.260\times22.1 = 27.8$.
5. For the doubling temperature, differentiate the logarithm: $\dfrac{d\ln n_i}{dT} = \dfrac{3}{2T} + \dfrac{E_g}{2k_BT^2} = 0.0050 + 0.0722 = 0.0772$ K⁻¹. Doubling requires $\Delta T = \ln2/0.0772 = 9.0$ K.

**Answer:** $n_i$ rises by a factor of about 28 between 300 K and 350 K and roughly doubles for every 9 K. The exponential dominates the power law. This sensitivity is why semiconductor devices have maximum operating temperatures (typically 125 to 150 °C for silicon chips): when $n_i$ approaches the deliberately added carrier density, the device loses its designed properties.

## 3. Doping: n-type and p-type Semiconductors

### Donors and acceptors

Intrinsic silicon is of little use because its carrier density is tiny and depends strongly on temperature. **Doping** replaces a small fraction of silicon atoms with atoms from neighboring groups of the periodic table.

- A **donor** from group 15 (phosphorus, arsenic or antimony) has five valence electrons. Four form bonds; the fifth is only weakly bound to the donor ion and is easily released into the conduction band. The donor becomes a fixed positive ion. Material dominated by donors is **n-type**: electrons are the **majority carriers**.
- An **acceptor** from group 13 (boron, or less commonly indium) has only three valence electrons, leaving one bond incomplete. A neighboring electron easily moves into it, creating a mobile hole and leaving a fixed negative ion. Material dominated by acceptors is **p-type**: holes are the majority carriers.

The doped crystal remains electrically **neutral** overall: every mobile electron released by a donor is balanced by the positive donor ion it left behind.

| Dopant in silicon | Type | Ionization energy (meV) |
|---|---|---|
| Antimony (Sb) | Donor | 39 |
| Phosphorus (P) | Donor | 45 |
| Arsenic (As) | Donor | 54 |
| Boron (B) | Acceptor | 45 |
| Indium (In) | Acceptor | 160 |

### Why dopants ionize at room temperature

The loosely bound fifth electron of a donor orbits a positive charge $+q$, much like the electron in a hydrogen atom, with two differences: the attraction is screened by the dielectric constant of silicon ($\varepsilon_r \approx 11.7$), and the electron moves with an **effective mass** $m^*$ that differs from the free-electron mass $m_e$ because of its interaction with the lattice. In the Bohr model, the hydrogen energy $E_1 = -m_ee^4/(8\varepsilon_0^2h^2) = -13.6$ eV scales as $m/\varepsilon^2$, and the Bohr radius $a_0 = 0.0529$ nm scales as $\varepsilon/m$. Hence
$$E_d \approx 13.6\text{ eV}\times\frac{m^*/m_e}{\varepsilon_r^2}, \qquad a_d \approx a_0\frac{\varepsilon_r}{m^*/m_e}.$$
With $m^*/m_e \approx 0.26$ for electrons in silicon, $E_d \approx 13.6\times0.26/11.7^2 = 0.026$ eV and $a_d \approx 0.0529\times11.7/0.26 = 2.4$ nm. The crude model gets the right order of magnitude (measured values are 39 to 54 meV), and it explains two key facts. The binding energy is comparable to $k_BT = 25.9$ meV, so at room temperature practically all shallow donors are ionized. And the orbit spans dozens of lattice spacings, which justifies treating the silicon as a continuous dielectric.

### Majority and minority carriers: the mass-action law

The derivation of $np = N_CN_V e^{-E_g/k_BT}$ in Section 2 never assumed the material was intrinsic. Therefore, in thermal equilibrium, for any doping,
$$\boxed{np = n_i^2}$$
This is the **mass-action law**, the semiconductor analogue of the water equilibrium $[\text{H}^+][\text{OH}^-] = K_w$. In n-type material with donor density $N_D \gg n_i$, essentially all donors are ionized, so
$$n \approx N_D, \qquad p \approx \frac{n_i^2}{N_D}.$$
Similarly in p-type material, $p \approx N_A$ and $n \approx n_i^2/N_A$. Adding electrons suppresses holes, because more electrons means more recombination. When both donors and acceptors are present, they **compensate** each other, and the net doping $N_D - N_A$ (or $N_A - N_D$) determines the type.

Doping moves the Fermi level. Writing the intrinsic Fermi level as $E_i$ (close to midgap), the Boltzmann expressions can be rewritten as $n = n_ie^{(E_F - E_i)/k_BT}$ and $p = n_ie^{(E_i - E_F)/k_BT}$. In n-type material the Fermi level rises toward the conduction band; in p-type it falls toward the valence band.

### Conductivity, mobility, drift and diffusion

In an electric field $\mathcal E$, carriers acquire an average **drift velocity** proportional to the field, $v_d = \mu\mathcal E$, where $\mu$ is the **mobility** (units cm²/V·s). Mobility is limited by scattering from lattice vibrations and from ionized dopants, so it decreases somewhat as doping increases. The drift current density is $J = q(n\mu_n + p\mu_p)\mathcal E$, so the conductivity is
$$\boxed{\sigma = \frac1\rho = q(n\mu_n + p\mu_p)}$$
At very high fields the drift velocity saturates, at about $10^7$ cm/s for electrons in silicon, which limits the speed of the smallest transistors.

Carriers also move by **diffusion** down a concentration gradient, just as ink spreads in water. The total current densities for electrons and holes are
$$J_n = qn\mu_n\mathcal E + qD_n\frac{dn}{dx}, \qquad J_p = qp\mu_p\mathcal E - qD_p\frac{dp}{dx},$$
where $D$ is the diffusion coefficient (cm²/s). The signs differ because electrons diffusing in the $-x$ direction (down a gradient that increases with $x$) carry current in the $+x$ direction. Drift and diffusion are two aspects of the same random thermal motion, and they are linked by the **Einstein relation**
$$\frac{D}{\mu} = \frac{k_BT}{q} = V_T.$$
For electrons in lightly doped silicon, $D_n = 1400\times0.02585 \approx 36$ cm²/s.

### Worked Example 3.1: Phosphorus-doped silicon

**Problem:** Silicon is doped with $N_D = 1.0\times10^{16}$ phosphorus atoms per cm³. Take $n_i = 1.0\times10^{10}$ cm⁻³, $T = 300$ K, and an electron mobility of $1200$ cm²/V·s at this doping. Find (a) the fraction of atoms that are dopants, (b) the electron and hole concentrations, (c) the resistivity and how it compares with intrinsic silicon, and (d) the position of the Fermi level relative to $E_i$.

**Solution:**

1. Fraction: $1.0\times10^{16}/5.0\times10^{22} = 2\times10^{-7}$, one phosphorus atom per five million silicon atoms.
2. Electrons: $n \approx N_D = 1.0\times10^{16}$ cm⁻³. Holes: $p = n_i^2/n = (10^{10})^2/10^{16} = 1.0\times10^4$ cm⁻³. The minority holes are outnumbered by $10^{12}$ to one.
3. Since $p\mu_p$ is negligible, $\rho = 1/(qn\mu_n) = 1/[(1.602\times10^{-19})(1.0\times10^{16})(1200)] = 0.52$ Ω·cm $= 5.2\times10^{-3}$ Ω·m.
4. Intrinsic silicon: $\sigma_i = qn_i(\mu_n + \mu_p) = (1.602\times10^{-19})(1.0\times10^{10})(1400 + 450) = 2.96\times10^{-6}$ S/cm, so $\rho_i = 3.4\times10^5$ Ω·cm. The ratio is $3.4\times10^5/0.52 \approx 6.5\times10^5$.
5. Fermi level: $E_F - E_i = k_BT\ln(n/n_i) = 0.02585\text{ eV}\times\ln(10^6) = 0.357$ eV.

**Answer:** One dopant atom in five million gives $n = 10^{16}$ cm⁻³ and $p = 10^4$ cm⁻³, cuts the resistivity from about $3.4\times10^5$ Ω·cm to 0.52 Ω·cm (a factor of roughly 650 000), and raises the Fermi level 0.36 eV above midgap. Because $n$ is fixed by $N_D$ rather than by $n_i$, the conductivity of doped silicon is also far less sensitive to temperature than that of intrinsic silicon.

## 4. The p-n Junction

### Formation of the depletion region

A **p-n junction** is a single crystal in which the doping changes from p-type to n-type over a short distance. (It is not made by pressing two separate pieces together; the surfaces would never make perfect contact.) Consider what happens at the moment the junction forms:

1. The n side has many free electrons and the p side has many holes, so electrons diffuse into the p side and holes diffuse into the n side.
2. Electrons arriving on the p side recombine with holes there, and holes arriving on the n side recombine with electrons. The region near the junction is **depleted** of mobile carriers.
3. The fixed dopant ions left behind are no longer neutralized: positive donor ions on the n side and negative acceptor ions on the p side. This layer of **space charge** is called the **depletion region**.
4. The space charge creates an electric field pointing from the n side to the p side, which pushes electrons back toward the n side and holes back toward the p side.
5. Equilibrium is reached when the drift current produced by this field exactly cancels the diffusion current, separately for electrons and for holes.

The result is a potential step, the **built-in potential** $V_{bi}$, with the n side at higher electrostatic potential. In equilibrium the Fermi level is flat across the whole structure: no net current flows and no energy can be extracted from it.

### The built-in potential

Set the net hole current to zero, using $\mathcal E = -d\phi/dx$ where $\phi$ is the electrostatic potential:
$$J_p = qp\mu_p\mathcal E - qD_p\frac{dp}{dx} = 0 \quad\Rightarrow\quad -\mu_p p\frac{d\phi}{dx} = D_p\frac{dp}{dx}.$$
Using the Einstein relation $D_p/\mu_p = k_BT/q$ and rearranging,
$$-d\phi = \frac{k_BT}{q}\frac{dp}{p}.$$
Integrate from deep in the p side (where $p = p_p = N_A$) to deep in the n side (where $p = p_n = n_i^2/N_D$):
$$\phi_n - \phi_p = \frac{k_BT}{q}\ln\frac{p_p}{p_n} \quad\Rightarrow\quad \boxed{V_{bi} = \frac{k_BT}{q}\ln\frac{N_AN_D}{n_i^2}}$$
The same result follows from the electron current. Equivalently, the hole concentrations on the two sides are related by a Boltzmann factor, $p_n = p_p e^{-qV_{bi}/k_BT}$: only holes with enough thermal energy to climb the barrier reach the n side.

### Width of the depletion region

In the **depletion approximation**, the depletion region extends a distance $x_p$ into the p side and $x_n$ into the n side, contains no mobile carriers, and has sharp edges. Take the junction at $x = 0$. Gauss's law in one dimension (Poisson's equation) reads $d\mathcal E/dx = \rho/\varepsilon$, where $\varepsilon = \varepsilon_r\varepsilon_0$:

1. On the p side ($-x_p < x < 0$), $\rho = -qN_A$, so the field grows linearly in magnitude from zero at $x = -x_p$.
2. On the n side ($0 < x < x_n$), $\rho = +qN_D$, and the field falls linearly back to zero at $x = x_n$.
3. The field is therefore a triangle with peak magnitude at $x = 0$:
$$\mathcal E_{\max} = \frac{qN_Ax_p}{\varepsilon} = \frac{qN_Dx_n}{\varepsilon}, \qquad\text{so}\qquad N_Ax_p = N_Dx_n.$$
The equality is charge neutrality: the negative charge on one side equals the positive charge on the other. The depletion region extends further into the **more lightly** doped side.
4. The potential difference across the region is the area of the field triangle. With an applied voltage $V$ (positive for forward bias, which reduces the barrier), the barrier height is $V_{bi} - V$:
$$V_{bi} - V = \tfrac12\mathcal E_{\max}W, \qquad W = x_n + x_p.$$
5. Substitute $x_n = WN_A/(N_A + N_D)$ into $\mathcal E_{\max} = qN_Dx_n/\varepsilon$ and solve for $W$:
$$\boxed{W = \sqrt{\frac{2\varepsilon(V_{bi} - V)}{q}\left(\frac1{N_A} + \frac1{N_D}\right)}}$$
Reverse bias ($V < 0$) widens the depletion region; forward bias narrows it.

### Worked Example 4.1: An asymmetric silicon junction

**Problem:** A silicon junction has $N_A = 1.0\times10^{17}$ cm⁻³ on the p side and $N_D = 1.0\times10^{16}$ cm⁻³ on the n side. With $n_i = 1.0\times10^{10}$ cm⁻³, $\varepsilon_r = 11.7$ and $T = 300$ K, find the built-in potential, the depletion width and its division between the two sides, and the peak field, at zero bias. Then find the width at a reverse bias of 5 V.

**Solution:**

1. Built-in potential: $V_{bi} = 0.02585\text{ V}\times\ln\dfrac{(10^{17})(10^{16})}{(10^{10})^2} = 0.02585\times\ln(10^{13}) = 0.02585\times29.93 = 0.774$ V.
2. Convert to SI: $N_A = 10^{23}$ m⁻³, $N_D = 10^{22}$ m⁻³, $\varepsilon = 11.7\times8.854\times10^{-12} = 1.036\times10^{-10}$ F/m.
3. Width: $W = \sqrt{\dfrac{2(1.036\times10^{-10})(0.774)}{1.602\times10^{-19}}\left(10^{-23} + 10^{-22}\right)} = 3.32\times10^{-7}$ m $= 0.332$ μm.
4. Division: $x_n = W\dfrac{N_A}{N_A + N_D} = 0.332\times\dfrac{10}{11} = 0.302$ μm and $x_p = 0.030$ μm. Ninety percent of the region lies on the lightly doped n side.
5. Peak field: $\mathcal E_{\max} = 2V_{bi}/W = 2(0.774)/(3.32\times10^{-7}) = 4.66\times10^6$ V/m $= 46.6$ kV/cm.
6. At 5 V reverse bias, $V_{bi} - V = 5.774$ V, and $W$ scales as the square root: $W = 0.332\times\sqrt{5.774/0.774} = 0.906$ μm.

**Answer:** $V_{bi} = 0.774$ V, $W = 0.33$ μm (0.30 μm on the n side, 0.03 μm on the p side), $\mathcal E_{\max} = 47$ kV/cm, and $W = 0.91$ μm at 5 V reverse bias. The field is enormous by everyday standards (air breaks down at about 30 kV/cm) even though the voltage is under one volt, because it acts over a third of a micrometer.

### Junction capacitance

The two layers of fixed charge on either side of the depletion region act like the plates of a parallel-plate capacitor of separation $W$. The capacitance per unit area is $C/A = \varepsilon/W$. In Worked Example 4.1 this is $1.036\times10^{-10}/(3.32\times10^{-7}) = 3.1\times10^{-4}$ F/m², or 31 nF/cm², at zero bias, falling to 11 nF/cm² at 5 V reverse bias. Because $W$ depends on voltage, the capacitance is voltage-controlled. **Varactor diodes** exploit this to tune radio and television receivers electronically.

## 5. The Diode Equation

### Forward and reverse bias

A p-n junction with external leads is a **diode**. Under **forward bias** (p side positive), the applied voltage reduces the barrier from $V_{bi}$ to $V_{bi} - V$. Because carrier populations follow a Boltzmann distribution, the number able to cross the barrier grows exponentially, and a large current flows. Under **reverse bias** (p side negative), the barrier grows, diffusion is choked off, and only a tiny current flows. That current is carried by minority carriers (electrons on the p side, holes on the n side) that wander to the edge of the depletion region and are swept across by the field. Their number is fixed by thermal generation, not by the voltage, so the reverse current **saturates** at a small value $I_S$.

### Derivation of the Shockley equation

William Shockley derived the ideal diode law in 1949. The steps are:

1. **Law of the junction.** At low injection levels, the carrier densities on the two sides of the depletion region remain related by the Boltzmann factor of the reduced barrier, $e^{-q(V_{bi} - V)/k_BT}$. On the n side, at the edge of the depletion region, the hole concentration becomes
$$p_n(0) = p_pe^{-q(V_{bi} - V)/k_BT} = p_{n0}e^{V/V_T},$$
where $p_{n0} = n_i^2/N_D$ is the equilibrium minority concentration. Forward bias **injects** extra minority carriers.
2. **Diffusion with recombination.** The excess holes $\Delta p(x) = p_n(x) - p_{n0}$ diffuse into the neutral n region and recombine with a lifetime $\tau_p$. The steady-state diffusion equation $D_p\,d^2\Delta p/dx^2 = \Delta p/\tau_p$ has the decaying solution
$$\Delta p(x) = p_{n0}\left(e^{V/V_T} - 1\right)e^{-x/L_p}, \qquad L_p = \sqrt{D_p\tau_p},$$
where $L_p$ is the **diffusion length** (typically micrometers to hundreds of micrometers).
3. **Current at the edge.** In the neutral region the minority current is pure diffusion: $J_p = -qD_p\,d\Delta p/dx$ at $x = 0$, giving
$$J_p = \frac{qD_pp_{n0}}{L_p}\left(e^{V/V_T} - 1\right) = \frac{qD_pn_i^2}{L_pN_D}\left(e^{V/V_T} - 1\right).$$
4. **Add the electrons** injected into the p side, by the same argument, and multiply by the junction area $A$:
$$\boxed{I = I_S\left(e^{V/V_T} - 1\right), \qquad I_S = qAn_i^2\left(\frac{D_p}{L_pN_D} + \frac{D_n}{L_nN_A}\right)}$$

This is the **Shockley diode equation**. Real diodes often follow $I = I_S(e^{V/nV_T} - 1)$ with an **ideality factor** $n$ between 1 and 2, the extra factor arising from recombination inside the depletion region. Note that $I_S \propto n_i^2$, which explains why it is so small in silicon (often $10^{-15}$ to $10^{-12}$ A for small devices) and why it grows rapidly with temperature.

### Consequences of the exponential law

- **The "turn-on" voltage.** A silicon diode carrying milliamps has a forward voltage of about 0.6 to 0.7 V. There is no sharp threshold; the current simply becomes appreciable there because $e^{V/V_T}$ is so steep. Germanium diodes, with their larger $n_i$ and hence larger $I_S$, conduct at about 0.2 to 0.3 V.
- **60 mV per decade.** Solving for voltage, $V = V_T\ln(I/I_S + 1)$. Multiplying the current by 10 adds $V_T\ln10 = 59.5$ mV at 300 K.
- **Small-signal resistance.** Differentiating, $dI/dV \approx I/V_T$, so a forward-biased diode behaves for small changes like a resistance $r_d = V_T/I$, about 26 Ω at 1 mA.
- **Temperature coefficient.** Since $I_S \propto n_i^2 \propto T^3e^{-E_g/k_BT}$, differentiating $V = V_T\ln(I/I_S)$ at constant current gives $dV/dT = [V - (E_g/q + 3V_T)]/T$. For $V = 0.65$ V this is $(0.65 - 1.12 - 0.078)/300 = -1.8$ mV/K, close to the measured value of about $-2$ mV/K. Diodes and transistor junctions are therefore used as cheap temperature sensors.

For hand analysis, engineers use a hierarchy of models: the **ideal diode** (a perfect one-way valve), the **constant-voltage-drop model** (a valve that drops 0.7 V when on) and the full exponential model.

### Breakdown and Zener diodes

A large enough reverse voltage causes **breakdown**: the reverse current rises abruptly while the voltage stays nearly constant. Two mechanisms are responsible:

- **Avalanche breakdown:** carriers swept across a wide depletion region gain enough energy between collisions to knock new electron-hole pairs out of the lattice, which in turn create more pairs. This dominates in lightly doped junctions with breakdown above roughly 6 V.
- **Zener breakdown:** in heavily doped junctions the depletion region is so thin (around 10 nm or less) and the field so strong that electrons **tunnel** directly from the valence band on the p side to the conduction band on the n side, a purely quantum-mechanical process. It dominates for breakdown below roughly 5 V.

Breakdown is not destructive if the current and power are limited. Diodes designed to operate in breakdown, all called **Zener diodes** whatever the mechanism, provide stable reference voltages.

### Worked Example 5.1: Using the diode equation

**Problem:** A silicon diode has $I_S = 1.0\times10^{-14}$ A and ideality factor 1 at 300 K. Find (a) the forward voltage at 1 mA and at 10 mA, (b) the current at 0.65 V and 0.70 V, (c) the small-signal resistance at 1 mA, and (d) the current at a reverse bias of 5 V.

**Solution:**

1. At 1 mA: $V = 0.02585\ln(10^{-3}/10^{-14} + 1) = 0.02585\times\ln(10^{11}) = 0.02585\times25.33 = 0.655$ V.
2. At 10 mA: $V = 0.02585\ln(10^{12}) = 0.714$ V, an increase of 59.5 mV for a tenfold current.
3. At 0.65 V: $I = 10^{-14}(e^{0.65/0.02585} - 1) = 0.83$ mA. At 0.70 V: $I = 5.7$ mA. A 50 mV step multiplies the current by about 7.
4. Small-signal resistance: $r_d = V_T/I = 0.02585/0.001 = 25.9$ Ω.
5. Reverse bias: $e^{-5/0.02585}$ is utterly negligible, so $I = -I_S = -1.0\times10^{-14}$ A (in practice, generation in the depletion region and surface leakage make it larger, typically nanoamps).

**Answer:** 0.655 V at 1 mA, 0.714 V at 10 mA; 0.83 mA at 0.65 V and 5.7 mA at 0.70 V; $r_d = 26$ Ω; reverse current about $-10^{-14}$ A in the ideal model.

### Worked Example 5.2: A diode and resistor in series

**Problem:** The diode of Worked Example 5.1 is connected in series with a 1.00 kΩ resistor across a 5.00 V supply, in the forward direction. Find the current and the diode voltage.

**Solution:**

1. Kirchhoff's voltage law gives $5.00 = IR + V_D$ and the diode gives $V_D = V_T\ln(I/I_S + 1)$. These cannot be solved in closed form, so iterate.
2. Guess $V_D = 0.70$ V: $I = (5.00 - 0.70)/1000 = 4.30$ mA.
3. Update: $V_D = 0.02585\ln(4.30\times10^{-3}/10^{-14}) = 0.6925$ V.
4. Update: $I = (5.00 - 0.6925)/1000 = 4.3075$ mA, giving $V_D = 0.6925$ V again. The iteration has converged.

**Answer:** $I = 4.31$ mA and $V_D = 0.693$ V. The constant-voltage-drop model (0.7 V) gives 4.30 mA, within 0.2%. Because the diode voltage changes only logarithmically with current, the simple model is usually good enough whenever the supply voltage is several times larger than 0.7 V.

## 6. Rectifiers and DC Power Supplies

Electronic circuits need a steady DC supply, but the mains provides alternating current at 50 Hz or 60 Hz. A **rectifier** uses diodes to convert AC into a unidirectional (though pulsating) voltage.

### Half-wave and full-wave rectification

- **Half-wave rectifier:** a single diode in series with the load conducts only during the positive half-cycles. The output is a series of positive half-sine humps with gaps between them, and the peak output is the peak input minus one diode drop.
- **Full-wave bridge rectifier:** four diodes arranged in a bridge steer both half-cycles through the load in the same direction. On each half-cycle two diodes conduct in series, so the peak output is $V_{\text{peak}} - 2V_D$, where $V_{\text{peak}} = \sqrt2\,V_{\text{rms}}$. The output humps repeat at twice the mains frequency. Each diode must withstand a reverse voltage of about $V_{\text{peak}}$ (its **peak inverse voltage** rating).

### Smoothing capacitor and ripple

A large **reservoir capacitor** $C$ across the load charges to the peak voltage on each hump, then supplies the load current $I$ between peaks while the diodes are off. Its voltage sags until the next hump recharges it, producing a sawtooth **ripple** of peak-to-peak size $\Delta V$.

Derivation: if the ripple is small, the load current is nearly constant at $I$, and the capacitor discharges for nearly the full interval between peaks, $T_r$. The charge lost is $\Delta Q = IT_r = C\Delta V$, so
$$\boxed{\Delta V \approx \frac{I}{f_rC}}$$
where $f_r = 1/T_r$ is the ripple frequency: $f_r = f$ for a half-wave rectifier and $f_r = 2f$ for a full-wave rectifier. Full-wave rectification halves the ripple for the same capacitor. The approximation slightly overestimates the ripple, because the capacitor actually starts recharging before the next peak.

### Worked Example 6.1: Designing a 15 V unregulated supply

**Problem:** A transformer delivers 12.0 V rms at 50 Hz to a bridge rectifier (diode drop 0.7 V each) with a 4700 μF reservoir capacitor. The load draws 0.50 A. Find the peak output voltage, the ripple, the minimum and average output voltage, and the peak inverse voltage across each diode.

**Solution:**

1. Peak secondary voltage: $V_{\text{peak}} = \sqrt2\times12.0 = 16.97$ V.
2. Peak output: two diodes conduct, so $16.97 - 1.4 = 15.57$ V.
3. Ripple frequency for full-wave: $f_r = 2\times50 = 100$ Hz. Ripple: $\Delta V = 0.50/(100\times4700\times10^{-6}) = 1.06$ V.
4. Minimum output: $15.57 - 1.06 = 14.51$ V; average (for a sawtooth) $\approx15.57 - 1.06/2 = 15.04$ V.
5. Peak inverse voltage: each non-conducting diode sees about the full peak, 17.0 V, so diodes rated well above this (for example 50 V or more) are chosen.

**Answer:** The output swings between about 14.5 V and 15.6 V (average 15.0 V) with 1.06 V of ripple at 100 Hz; the diodes must withstand at least 17 V in reverse.

### Regulation

The unregulated output still has ripple and drops when the load current or mains voltage changes. A **voltage regulator** follows the rectifier. The simplest is a **Zener regulator**: a series resistor feeding a Zener diode, which holds its breakdown voltage nearly constant as its current changes (see Worked Example 15.3). Integrated **linear regulators** use a reference voltage, an amplifier and a pass transistor to hold the output steady to within millivolts. Modern supplies, including phone chargers, are usually **switch-mode** designs: transistors switch the input on and off tens of thousands to millions of times per second, and inductors and capacitors smooth the result. They waste far less power as heat than linear regulators.

## 7. Optoelectronics: LEDs, Photodiodes and Solar Cells

### Light-emitting diodes

When a junction in a direct-gap semiconductor is forward-biased, injected electrons and holes recombine and each recombination can emit one photon of energy close to the band gap. The emission wavelength is therefore set by material choice:
$$\lambda \approx \frac{hc}{E_g} = \frac{1239.84\text{ eV·nm}}{E_g}.$$
Engineers tune $E_g$ by making **alloys**: in $\text{In}_x\text{Ga}_{1-x}\text{N}$, increasing the indium fraction lowers the gap from that of GaN toward that of InN, moving emission from violet through blue to green. Practical LEDs use **heterostructures**, in which a thin layer of narrower-gap material (a **quantum well**) is sandwiched between wider-gap layers that confine both electrons and holes and so increase the chance that they recombine radiatively.

| LED material | Typical emission | Color | Typical forward voltage (V) |
|---|---|---|---|
| GaAs | 870–940 nm | Infrared (remote controls) | 1.2–1.5 |
| AlGaAs | 650–880 nm | Red to infrared | 1.5–2.0 |
| AlGaInP | 590–650 nm | Amber, orange, red | 1.8–2.4 |
| InGaN | 400–540 nm | Violet, blue, green | 2.8–3.5 |
| AlGaN | about 250–360 nm | Ultraviolet | above 3.5 |

The forward voltage is roughly the photon energy in electronvolts (a red photon at 630 nm carries $1239.84/630 = 1.97$ eV), plus extra drops across contacts and layers. **White LEDs** normally combine a blue InGaN chip with a yellow-emitting phosphor (cerium-doped yttrium aluminum garnet); the mixture of transmitted blue and converted yellow looks white. Because conversion of one photon to another of lower energy wastes the difference, white LEDs are less efficient than the blue chip alone. Even so, white LED lamps typically produce around 100 lumens per watt of electrical input or more, compared with roughly 10 to 17 lumens per watt for incandescent bulbs.

An LED's current must be limited externally: its exponential characteristic means that connecting it directly across a voltage source a little above its forward voltage would draw a destructive current.

### Worked Example 7.1: Driving an LED

**Problem:** (a) A red LED ($V_F = 2.0$ V) is to be run at 15 mA from a 5.0 V supply. Find the series resistor and the power it dissipates. (b) A blue InGaN LED emits at 450 nm with $V_F = 3.1$ V at 20 mA. Find the photon energy, and the maximum possible ratio of optical output power to electrical input power if every electron produced one photon that escaped.

**Solution:**

1. (a) The resistor drops $5.0 - 2.0 = 3.0$ V at 15 mA: $R = 3.0/0.015 = 200$ Ω. Power in the resistor: $3.0\times0.015 = 45$ mW, compared with $2.0\times0.015 = 30$ mW in the LED.
2. (b) Photon energy: $E = 1239.84/450 = 2.755$ eV.
3. Electron rate: $I/q = 0.020/(1.602\times10^{-19}) = 1.248\times10^{17}$ per second.
4. Maximum optical power: $(1.248\times10^{17}\text{ s}^{-1})(2.755\text{ eV})(1.602\times10^{-19}\text{ J/eV}) = 0.0551$ W.
5. Electrical power: $3.1\times0.020 = 0.062$ W. Maximum ratio: $0.0551/0.062 = 0.89$.

**Answer:** (a) 200 Ω, dissipating 45 mW. (b) Each photon carries 2.76 eV; even with perfect quantum efficiency, at most 89% of the electrical power could leave as light, because each electron loses $3.1 - 2.76 = 0.35$ eV in the device. The best blue LEDs convert well over half of their electrical input into light; the rest of the energy becomes heat.

### Photodiodes

Run backwards, a junction detects light. A photon with energy above $E_g$ absorbed in or near the depletion region creates an electron-hole pair; the built-in field separates the pair, sending the electron to the n side and the hole to the p side, which produces a **photocurrent** in the reverse direction. A photodiode is usually operated at zero or reverse bias, where the photocurrent is accurately proportional to the light power.

If a fraction $\eta$ (the **quantum efficiency**) of incident photons each produce one electron of current, the photocurrent from optical power $P$ is $I = \eta qP/(h\nu)$. The **responsivity** is therefore
$$\boxed{\mathcal R = \frac{I}{P} = \frac{\eta q\lambda}{hc} = \eta\,\frac{\lambda\,[\text{nm}]}{1239.84}\ \text{A/W}}$$
Responsivity rises with wavelength (each watt contains more, lower-energy photons) until the photon energy drops below the band gap, where it falls abruptly to zero. Silicon photodiodes cover roughly 400 to 1100 nm, with the long-wavelength cutoff near 1107 nm. Fiber-optic receivers at 1310 and 1550 nm use germanium or InGaAs instead.

Related devices include **avalanche photodiodes**, which operate near breakdown so that each photo-generated carrier triggers an avalanche of many more, and the **image sensors** in cameras: arrays of millions of photodiodes, each with its own transistor readout circuitry (CMOS image sensors) or with charge shifted across the chip to an output amplifier (charge-coupled devices, CCDs).

### Solar cells

A **solar cell** is a large-area photodiode operated so that it delivers power. Under illumination, the light-generated current $I_L$ flows in the reverse direction, superimposed on the ordinary diode current. Taking current out of the cell as positive,
$$I = I_L - I_S\left(e^{V/V_T} - 1\right).$$
The important points on this curve are:

- **Short-circuit current** ($V = 0$): $I_{sc} = I_L$, proportional to illumination.
- **Open-circuit voltage** ($I = 0$): solving gives
$$V_{oc} = V_T\ln\left(\frac{I_L}{I_S} + 1\right).$$
It rises only logarithmically with illumination and decreases with temperature, because $I_S$ grows rapidly with $T$.
- **Maximum power point:** the power $P = IV$ is greatest where $dP/dV = 0$. Differentiating, $I_L - I_S(e^{V/V_T} - 1) - (V/V_T)I_Se^{V/V_T} = 0$. Neglecting the 1 compared with the large exponentials, this becomes $e^{V_{mp}/V_T}(1 + V_{mp}/V_T) = I_L/I_S = e^{V_{oc}/V_T}$, so
$$V_{mp} = V_{oc} - V_T\ln\left(1 + \frac{V_{mp}}{V_T}\right),$$
which can be solved by iteration.
- **Fill factor:** $FF = P_{\max}/(V_{oc}I_{sc})$, a measure of how "square" the curve is, typically 0.75 to 0.85.
- **Efficiency:** $\eta = P_{\max}/P_{\text{in}}$, measured under **standard test conditions**: an irradiance of 1000 W/m² with the AM1.5 solar spectrum, at a cell temperature of 25 °C.

There is a fundamental trade-off in choosing the band gap. A small gap absorbs more of the solar spectrum but gives a low voltage, and every photon with energy above the gap wastes its excess as heat once the carriers relax to the band edges. A large gap gives a high voltage but lets most of the sunlight pass through unabsorbed. In 1961 William Shockley and Hans-Joachim Queisser used a detailed-balance argument to show that a single-junction cell in unconcentrated sunlight cannot exceed about 33%, with the optimum gap near 1.34 eV. For silicon, unavoidable Auger recombination lowers the practical limit to about 29%. **Multi-junction** cells, which stack materials of different gaps, exceed the single-junction limit and power most spacecraft.

### Worked Example 7.2: Performance of a silicon solar cell

**Problem:** A 10 cm × 10 cm silicon cell at 25 °C ($V_T = 25.69$ mV) has a light-generated current density of 40 mA/cm² under standard test conditions and a saturation current density of $1.0\times10^{-12}$ A/cm². Treating it as an ideal diode, find $I_{sc}$, $V_{oc}$, the maximum power point, the fill factor and the efficiency.

**Solution:**

1. Area: 100 cm². $I_{sc} = I_L = 40\text{ mA/cm}^2\times100\text{ cm}^2 = 4.0$ A, and $I_S = 1.0\times10^{-12}\times100 = 1.0\times10^{-10}$ A.
2. $V_{oc} = 0.02569\ln(4.0/10^{-10} + 1) = 0.02569\times24.41 = 0.627$ V.
3. Maximum power voltage: start with $V_{mp} = V_{oc}$ and iterate $V_{mp} = 0.627 - 0.02569\ln(1 + V_{mp}/0.02569)$. The first pass gives 0.544 V, the second 0.548 V, and the iteration settles at $V_{mp} = 0.547$ V.
4. Current there: $I_{mp} = 4.0 - 10^{-10}(e^{0.547/0.02569} - 1) = 3.82$ A.
5. Maximum power: $P_{\max} = 0.547\times3.82 = 2.09$ W.
6. Fill factor: $FF = 2.09/(0.627\times4.0) = 0.834$.
7. Input power: $1000\text{ W/m}^2\times0.0100\text{ m}^2 = 10.0$ W, so efficiency $= 2.09/10.0 = 20.9\%$.

**Answer:** $I_{sc} = 4.0$ A, $V_{oc} = 0.63$ V, $V_{mp} = 0.55$ V, $I_{mp} = 3.8$ A, $P_{\max} = 2.1$ W, $FF = 0.83$, efficiency 21%. A single cell gives only about half a volt, so commercial modules connect 60 to 72 or more cells in series. Real cells have somewhat lower fill factors because of series resistance in the contacts.

## 8. Bipolar Junction Transistors

### Structure and operation

A **bipolar junction transistor** (BJT) is a sandwich of three doped regions: n-p-n or p-n-p. In an **npn** transistor the heavily doped n-type **emitter** injects electrons into a thin p-type **base**, and a moderately doped n-type **collector** gathers them. In the normal **active mode**:

1. The base-emitter junction is forward-biased (about 0.6 to 0.7 V), so the emitter injects a large flow of electrons into the base.
2. The base is very thin (well under the diffusion length) and lightly doped, so almost all injected electrons diffuse across it before they can recombine.
3. The base-collector junction is reverse-biased; its field sweeps arriving electrons into the collector.
4. A small base current supplies the holes lost by recombination in the base and the holes injected back into the emitter.

Because the collector current is the injected diffusion current of the base-emitter junction, it follows the diode law:
$$I_C = I_Se^{V_{BE}/V_T}$$
and is almost independent of the collector voltage. The base current is a small, roughly fixed fraction of it:
$$I_C = \beta I_B, \qquad I_E = I_C + I_B = (\beta + 1)I_B, \qquad \alpha = \frac{I_C}{I_E} = \frac{\beta}{\beta + 1}.$$
The **current gain** $\beta$ (also written $h_{FE}$) is typically 50 to 300, but varies widely between nominally identical transistors and with temperature and current, so good circuits are designed not to depend on its exact value. A pnp transistor works the same way with all polarities reversed.

### The BJT as a switch

A transistor used as a switch operates in two states:

- **Cut-off:** $V_{BE}$ is below about 0.5 V, no base current flows, and the collector current is essentially zero: the switch is open.
- **Saturation:** the base is driven with more current than needed, so the collector current is limited by the external load rather than by $\beta I_B$. Both junctions become forward-biased and $V_{CE}$ falls to a small value $V_{CE(\text{sat})} \approx 0.1$ to 0.3 V: the switch is closed.

To guarantee saturation, the designer chooses $I_B$ larger than $I_{C}/\beta_{\min}$ by a safety factor (often 2 to 10). Inductive loads such as relays and motors need a **flyback diode** across them: when the transistor switches off, the inductor's current cannot stop instantly, and without a path it would generate a voltage spike ($V = L\,dI/dt$) large enough to destroy the transistor.

### Worked Example 8.1: Switching a lamp from a microcontroller

**Problem:** A 3.3 V microcontroller output must switch a 12 V lamp that draws 150 mA, using an npn transistor with $\beta_{\min} = 100$, $V_{BE} = 0.7$ V and $V_{CE(\text{sat})} = 0.2$ V. Choose the base resistor with a saturation safety factor of 3, and find the power dissipated in the transistor when on.

**Solution:**

1. Minimum base current for 150 mA: $I_{B,\min} = 0.150/100 = 1.5$ mA.
2. With a factor of 3: $I_B = 4.5$ mA.
3. The base resistor drops $3.3 - 0.7 = 2.6$ V: $R_B = 2.6/0.0045 = 578$ Ω. The nearest standard value below is 560 Ω, giving $I_B = 2.6/560 = 4.6$ mA, well within the capability of a typical output pin.
4. Transistor dissipation when on: $V_{CE(\text{sat})}I_C = 0.2\times0.150 = 0.030$ W.

**Answer:** $R_B = 560$ Ω; the transistor dissipates only 30 mW while switching 1.8 W to the lamp. A saturated switch wastes little power because either the current through it or the voltage across it is small at all times.

### The BJT as an amplifier

In the active mode a small change in $V_{BE}$ produces a proportionally larger change in $I_C$. Differentiating $I_C = I_Se^{V_{BE}/V_T}$ defines the **transconductance**:
$$\boxed{g_m = \frac{dI_C}{dV_{BE}} = \frac{I_C}{V_T}}$$
In the **common-emitter amplifier**, the collector is connected to the supply $V_{CC}$ through a resistor $R_C$, and the output is taken from the collector, so $V_{\text{out}} = V_{CC} - I_CR_C$. A small input signal $v_{\text{in}}$ added to the base-emitter bias changes the collector current by $g_mv_{\text{in}}$ and the output by
$$v_{\text{out}} = -g_mR_Cv_{\text{in}} \quad\Rightarrow\quad A_v = -g_mR_C = -\frac{I_CR_C}{V_T}.$$
The minus sign means the amplifier inverts. The gain depends on temperature and on the exact bias current; adding an **emitter resistor** $R_E$ (emitter degeneration) trades gain for stability: $A_v \approx -R_C/(R_E + r_e)$, where $r_e = V_T/I_E \approx 1/g_m$. When $R_E \gg r_e$, the gain is set by the resistor ratio alone. Note that the energy in the amplified output comes from the DC supply: the transistor is a valve that controls that flow, not a source of energy.

### Worked Example 8.2: A common-emitter amplifier

**Problem:** An npn transistor is biased at $I_C = 1.0$ mA with $R_C = 4.7$ kΩ and $V_{CC} = 12$ V at 300 K. Find the DC collector voltage, the transconductance and the small-signal voltage gain. Then find the gain if a 470 Ω emitter resistor is added (without a bypass capacitor).

**Solution:**

1. Collector voltage: $V_C = 12 - (1.0\times10^{-3})(4700) = 7.3$ V, comfortably in the active region, leaving room for the output to swing.
2. Transconductance: $g_m = I_C/V_T = 1.0\times10^{-3}/0.02585 = 38.7$ mS.
3. Gain: $A_v = -g_mR_C = -0.0387\times4700 = -182$.
4. With emitter degeneration: $r_e = V_T/I_E \approx 25.9$ Ω, so $A_v \approx -4700/(470 + 25.9) = -9.48$, close to the simple ratio $-R_C/R_E = -10$.

**Answer:** $V_C = 7.3$ V, $g_m = 38.7$ mS, $A_v = -182$ without degeneration and about $-9.5$ with a 470 Ω emitter resistor. The degenerated gain is much smaller but almost independent of temperature and of the particular transistor.

## 9. MOSFETs

### Structure and the field effect

The **metal-oxide-semiconductor field-effect transistor** (MOSFET) is the most manufactured object in human history: modern memory and processor chips each contain billions. An **n-channel** MOSFET is built on p-type silicon. Two heavily doped n⁺ regions, the **source** and **drain**, are separated by a channel region of length $L$ and width $W$. Above the channel, separated by a very thin insulating layer (originally silicon dioxide), sits the **gate** electrode.

1. With zero gate voltage, the source and drain form back-to-back p-n junctions with the substrate and no current flows.
2. A positive gate voltage repels holes from the surface and attracts electrons. When the gate-source voltage exceeds the **threshold voltage** $V_{th}$ (typically 0.3 to 1 V in logic transistors), a thin **inversion layer** of electrons forms at the surface, connecting source to drain.
3. The gate is insulated, so in steady state it draws essentially **no current**. The transistor is controlled by a voltage, through the electric field of the gate acting like one plate of a capacitor, hence "field effect".

The gate capacitance per unit area is $C_{ox} = \varepsilon_{ox}/t_{ox}$. For silicon dioxide ($\varepsilon_r = 3.9$) only 2 nm thick, $C_{ox} = 3.9\times8.854\times10^{-12}/(2\times10^{-9}) = 0.0173$ F/m² $= 1.73$ μF/cm². At such thicknesses electrons leak through the oxide by quantum tunneling, which is why manufacturers switched to **high-k** gate dielectrics based on hafnium oxide, starting in 2007, to achieve high capacitance with a physically thicker layer. A **p-channel** MOSFET is the mirror image: built on n-type silicon, with a hole channel that forms when the gate is sufficiently negative relative to the source.

### Derivation of the current–voltage relation

Consider an n-channel device with gate-source voltage $V_{GS} > V_{th}$ and a small drain-source voltage $V_{DS}$. Let $V(x)$ be the channel potential at distance $x$ from the source, rising from 0 to $V_{DS}$.

1. **Channel charge.** The gate and channel form a capacitor. The local voltage across the oxide in excess of threshold is $V_{GS} - V(x) - V_{th}$, so the mobile electron charge per unit area is
$$Q_n(x) = -C_{ox}\left[V_{GS} - V_{th} - V(x)\right].$$
2. **Drift current.** The current is the same at every point along the channel. Electrons drift with velocity $\mu_n\,dV/dx$, so
$$I_D = -WQ_n(x)\mu_n\frac{dV}{dx} = \mu_nC_{ox}W\left[V_{GS} - V_{th} - V(x)\right]\frac{dV}{dx}.$$
3. **Integrate** along the channel from $x = 0$ ($V = 0$) to $x = L$ ($V = V_{DS}$):
$$I_DL = \mu_nC_{ox}W\int_0^{V_{DS}}\left(V_{GS} - V_{th} - V\right)dV,$$
which gives the **triode** (linear) region result:
$$I_D = \mu_nC_{ox}\frac WL\left[(V_{GS} - V_{th})V_{DS} - \frac{V_{DS}^2}{2}\right].$$
4. **Pinch-off and saturation.** When $V_{DS}$ reaches the **overdrive voltage** $V_{ov} = V_{GS} - V_{th}$, the channel charge at the drain end falls to zero (pinch-off). For larger $V_{DS}$ the current stops increasing. Substituting $V_{DS} = V_{GS} - V_{th}$:
$$\boxed{I_D = \frac12\mu_nC_{ox}\frac WL\left(V_{GS} - V_{th}\right)^2 \qquad (V_{DS} \ge V_{GS} - V_{th})}$$
This **square law** is the MOSFET counterpart of the BJT's exponential law. In very short modern transistors, velocity saturation makes the current grow more nearly linearly with $V_{GS} - V_{th}$, but the square law remains the standard first model.

### MOSFET as switch and amplifier

- **Switch.** For small $V_{DS}$ the triode equation reduces to $I_D \approx \mu_nC_{ox}(W/L)(V_{GS} - V_{th})V_{DS}$: the channel behaves as a resistor
$$R_{on} = \frac{1}{\mu_nC_{ox}(W/L)(V_{GS} - V_{th})},$$
controlled by the gate voltage. Power MOSFETs with very large $W/L$ reach on-resistances of a few milliohms; at 20 A, a 10 mΩ switch dissipates $I^2R_{on} = 4$ W. Because the gate draws no steady current, a MOSFET switch needs drive current only while its gate capacitance is being charged or discharged.
- **Amplifier.** In saturation, the transconductance is
$$g_m = \frac{\partial I_D}{\partial V_{GS}} = \mu_nC_{ox}\frac WL(V_{GS} - V_{th}) = \frac{2I_D}{V_{GS} - V_{th}}.$$
Compare the BJT: $g_m/I_C = 1/V_T = 38.7$ V⁻¹, whereas for a MOSFET $g_m/I_D = 2/V_{ov}$, typically 2 to 10 V⁻¹. Bipolar transistors deliver more transconductance per unit current, which is why they remain common in precision analog and radio-frequency circuits.

### Worked Example 9.1: Biasing an n-channel MOSFET amplifier

**Problem:** An n-channel MOSFET has $\mu_nC_{ox} = 200$ μA/V², $W/L = 10$ and $V_{th} = 0.50$ V. It is connected as a common-source amplifier with $V_{DD} = 3.3$ V, drain resistor $R_D = 2.0$ kΩ, and a DC gate bias $V_{GS} = 1.5$ V. Find the drain current, the drain voltage, whether the transistor is in saturation, the transconductance and the small-signal gain.

**Solution:**

1. Overdrive: $V_{ov} = 1.5 - 0.5 = 1.0$ V.
2. Assuming saturation: $I_D = \tfrac12(200\times10^{-6})(10)(1.0)^2 = 1.0$ mA.
3. Drain voltage: $V_D = 3.3 - (1.0\times10^{-3})(2000) = 1.3$ V.
4. Check: $V_{DS} = 1.3$ V $\ge V_{ov} = 1.0$ V, so the saturation assumption holds.
5. Transconductance: $g_m = 2I_D/V_{ov} = 2(1.0\times10^{-3})/1.0 = 2.0$ mS.
6. Gain: $A_v = -g_mR_D = -(2.0\times10^{-3})(2000) = -4.0$.

**Answer:** $I_D = 1.0$ mA, $V_D = 1.3$ V (saturation confirmed), $g_m = 2.0$ mS and $A_v = -4.0$. A BJT at the same 1 mA would have $g_m = 38.7$ mS, about 19 times larger.

## 10. CMOS Logic

### The CMOS inverter

**Complementary MOS** (CMOS) logic, invented by Frank Wanlass and Chih-Tang Sah at Fairchild Semiconductor in 1963, pairs an n-channel and a p-channel MOSFET. In the **inverter**, the p-channel transistor connects the output to the supply $V_{DD}$ and the n-channel transistor connects the output to ground; both gates are joined to the input.

- Input **low** (0 V): the n-channel transistor is off, the p-channel transistor is on, and the output is pulled up to $V_{DD}$ (logic 1).
- Input **high** ($V_{DD}$): the n-channel transistor is on, the p-channel transistor is off, and the output is pulled down to 0 (logic 0).

In either steady state one transistor is off, so **no current flows from supply to ground** apart from tiny leakage. Current flows only briefly while the output switches, to charge or discharge the capacitance of the wires and gates it drives. This near-zero static power is the main reason CMOS displaced the earlier logic families and made battery-powered digital electronics practical.

### NAND and NOR gates

More complex gates follow the same complementary pattern: the pull-down network of n-channel transistors conducts exactly when the pull-up network of p-channel transistors does not.

- **NAND:** two n-channel transistors in **series** to ground and two p-channel transistors in **parallel** to $V_{DD}$. The output is pulled low only when both inputs are high.
- **NOR:** two n-channel transistors in **parallel** and two p-channel transistors in **series**. The output is low when either input is high.

A two-input CMOS NAND or NOR gate uses four transistors; an inverter uses two.

### Power dissipation

Model the load on a gate output as a capacitance $C$. When the output rises from 0 to $V_{DD}$, a charge $Q = CV_{DD}$ flows from the supply, which delivers energy $QV_{DD} = CV_{DD}^2$. The capacitor stores only $\tfrac12CV_{DD}^2$; the other half is dissipated as heat in the p-channel transistor, whatever its resistance. When the output falls, the stored $\tfrac12CV_{DD}^2$ is dissipated in the n-channel transistor. Each complete up-and-down cycle therefore costs $CV_{DD}^2$. If a fraction $\alpha$ (the **activity factor**) of the total switched capacitance $C$ makes such a cycle on each clock period at frequency $f$,
$$\boxed{P_{\text{dyn}} = \alpha CV_{DD}^2f}$$
The square dependence on supply voltage is why supply voltages fell from 5 V in the 1980s to around 1 V or below today, and why phones and laptops lower both voltage and frequency when demand is light (**dynamic voltage and frequency scaling**). In modern chips, **leakage** through transistors that are nominally off adds a significant static power as well.

### Worked Example 10.1: Power in a processor

**Problem:** A processor has an effective total switched capacitance of 50 nF, an activity factor of 0.10 and a clock frequency of 3.0 GHz. Find the dynamic power at $V_{DD} = 1.0$ V. Then find the power at 1.2 V and at 0.9 V (same frequency), and the fractional saving in going from 1.2 V to 0.9 V.

**Solution:**

1. At 1.0 V: $P = 0.10\times(50\times10^{-9})\times(1.0)^2\times(3.0\times10^9) = 15$ W.
2. At 1.2 V: $P = 15\times1.2^2 = 21.6$ W.
3. At 0.9 V: $P = 15\times0.9^2 = 12.2$ W.
4. Ratio: $(0.9/1.2)^2 = 0.5625$, a saving of 44%.

**Answer:** 15 W at 1.0 V, 21.6 W at 1.2 V and 12.2 W at 0.9 V; a 25% reduction in voltage cuts dynamic power by 44%. In practice lower voltage also reduces the maximum safe clock frequency, because transistors deliver less current to charge the load capacitance.

## 11. Digital Logic and Binary Numbers

### Binary and hexadecimal

Digital circuits represent information with two voltage levels, interpreted as the binary digits (**bits**) 0 and 1. Two levels are used because a transistor switch is very reliable when it only needs to be fully on or fully off: small amounts of noise or component variation do not change a clearly high or clearly low signal, and every gate restores degraded levels to clean ones. The ranges of input voltage that are guaranteed to read as 0 or as 1 leave a gap, the **noise margin**, between what one gate outputs and what the next must accept.

A binary number uses powers of 2 just as a decimal number uses powers of 10. With $n$ bits there are $2^n$ distinct values, from 0 to $2^n - 1$; eight bits form a **byte** (256 values). **Hexadecimal** (base 16, digits 0–9 and A–F) is a compact shorthand: each hex digit represents exactly four bits.

### Logic gates and Boolean algebra

In 1854 George Boole published an algebra of logic in which variables take only the values true and false. In his 1937 master's thesis at MIT, Claude Shannon showed that Boole's algebra describes circuits of relays and switches, which made it the mathematical foundation of digital design. The basic operations, written with $\cdot$ for AND, $+$ for OR and an overbar for NOT, are summarized here:

| A | B | AND $A\cdot B$ | OR $A + B$ | NAND $\overline{A\cdot B}$ | NOR $\overline{A + B}$ | XOR $A\oplus B$ |
|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 1 | 1 | 0 |
| 0 | 1 | 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 1 | 0 | 0 | 0 |

The NOT gate (inverter) simply outputs the complement, $\overline A$. Useful identities include **De Morgan's laws**:
$$\overline{A\cdot B} = \overline A + \overline B, \qquad \overline{A + B} = \overline A\cdot\overline B.$$
NAND (and likewise NOR) is **universal**: any logic function can be built from NAND gates alone. A NAND with its inputs joined is an inverter; a NAND followed by an inverter is AND; and by De Morgan's law, NAND applied to inverted inputs is OR: $\overline{\overline A\cdot\overline B} = A + B$. Since a CMOS NAND needs only four transistors, it is a natural building block.

### Binary addition

Adding two one-bit numbers gives a **sum** bit and a **carry** bit. Comparing with the table above, the sum is the XOR and the carry is the AND:
$$S = A\oplus B, \qquad C_{\text{out}} = A\cdot B.$$
This circuit is a **half adder**. A **full adder** also accepts a carry from the previous column: $S = A\oplus B\oplus C_{\text{in}}$ and $C_{\text{out}} = A\cdot B + C_{\text{in}}\cdot(A\oplus B)$. Chaining $n$ full adders adds two $n$-bit numbers.

Negative integers are usually stored in **two's complement**: to negate a number, invert every bit and add 1. In $n$ bits this represents $-x$ as $2^n - x$, so ordinary binary addition automatically gives correct signed results, with any carry out of the top bit discarded.

### Worked Example 11.1: Binary arithmetic

**Problem:** (a) Convert 2026 to binary and hexadecimal. (b) Add 6 and 7 in 4-bit binary. (c) Represent $-13$ in 8-bit two's complement and verify that adding 13 gives zero.

**Solution:**

1. (a) Subtract the largest powers of 2: $2026 = 1024 + 512 + 256 + 128 + 64 + 32 + 8 + 2$. Marking the powers from $2^{10}$ down to $2^0$ gives $11111101010_2$.
2. Group into fours from the right: $0111\ 1110\ 1010 = 7\,\text{E}\,\text{A}$, so $2026 = 7\text{EA}_{16}$. Check: $7\times256 + 14\times16 + 10 = 1792 + 224 + 10 = 2026$.
3. (b) $0110 + 0111$: column by column from the right, $0 + 1 = 1$; $1 + 1 = 0$ carry 1; $1 + 1 + 1 = 1$ carry 1; $0 + 0 + 1 = 1$. Result $1101_2 = 8 + 4 + 1 = 13$.
4. (c) $13 = 00001101_2$. Invert: $11110010$. Add 1: $11110011_2$ (which is $243 = 256 - 13$).
5. Verify: $00001101 + 11110011 = 1\,00000000$. The ninth bit is the discarded carry, leaving $00000000$.

**Answer:** $2026 = 11111101010_2 = 7\text{EA}_{16}$; $6 + 7 = 1101_2 = 13$; $-13 = 11110011_2$ in 8-bit two's complement.

### Memory: latches, SRAM, DRAM and flash

Logic built only from gates is **combinational**: the outputs depend only on present inputs. To remember, circuits use **feedback**. Two cross-coupled NOR gates form an **SR latch**, which holds one bit indefinitely while powered; clocked versions (**flip-flops**) form registers and counters. Large memories use specialized cells:

- **SRAM** (static RAM) stores a bit in a pair of cross-coupled inverters plus two access transistors (six transistors per bit). It is fast and used for processor caches.
- **DRAM** (dynamic RAM) stores a bit as charge on a tiny capacitor accessed through one transistor, a cell invented by Robert Dennard at IBM in the 1960s. The charge leaks away, so every cell must be refreshed many times per second, but the cell is very small.
- **Flash memory** traps charge on an electrically isolated gate (or in a charge-trapping layer) inside a transistor, shifting its threshold voltage. The charge persists for years without power, which is why flash is used in solid-state drives, phones and memory cards.

## 12. Operational Amplifiers

### The ideal op-amp and its rules

An **operational amplifier** (op-amp) is an integrated differential amplifier with two inputs, non-inverting ($+$) and inverting ($-$), and one output:
$$V_{\text{out}} = A\,(V_+ - V_-),$$
where the **open-loop gain** $A$ is very large, typically $10^5$ to $10^6$. The name comes from analog computers of the 1940s, in which such amplifiers performed mathematical operations: John Ragazzini and colleagues used the term in 1947.

An op-amp is almost never used open-loop: with $A = 2\times10^5$, an input difference of only 60 μV would drive the output to 12 V. Instead, **negative feedback** connects the output back to the inverting input, so that the output adjusts itself until the input difference is tiny. This leads to two rules for the **ideal op-amp** with negative feedback:

1. **No current flows into either input** (the input impedance is effectively infinite).
2. **The output does whatever is necessary to make $V_- = V_+$** (the input voltage difference is driven to zero; a "virtual short").

Rule 2 is valid only with negative feedback and only while the output stays within its supply limits. Without feedback, or with positive feedback, the op-amp acts as a **comparator** whose output slams to one supply rail or the other.

### The inverting amplifier

The input signal drives the inverting input through a resistor $R_{\text{in}}$, a feedback resistor $R_f$ connects the output to the inverting input, and the non-inverting input is grounded.

1. Since $V_+ = 0$, rule 2 gives $V_- = 0$: the inverting input is a **virtual ground**.
2. The current through $R_{\text{in}}$ is $I = V_{\text{in}}/R_{\text{in}}$.
3. By rule 1, all of this current continues through $R_f$, so $V_{\text{out}} = 0 - IR_f$.
4. Therefore
$$\boxed{\frac{V_{\text{out}}}{V_{\text{in}}} = -\frac{R_f}{R_{\text{in}}}}$$
The input resistance seen by the source is simply $R_{\text{in}}$.

With a finite open-loop gain $A$, writing $V_{\text{out}} = -AV_-$ and solving the voltage-divider equation for $V_-$ gives
$$\frac{V_{\text{out}}}{V_{\text{in}}} = -\frac{R_f/R_{\text{in}}}{1 + (1 + R_f/R_{\text{in}})/A},$$
which approaches the ideal result as $A\to\infty$. Because $A$ is so large, the closed-loop gain depends almost entirely on the resistors, which are precise and stable, rather than on the transistors inside the op-amp, which are not. This insensitivity is the great gift of negative feedback, recognized by Harold Black at Bell Labs in 1927.

### The non-inverting amplifier and the voltage follower

The signal drives the non-inverting input directly, and the output feeds back to the inverting input through a voltage divider of $R_f$ (from output to $V_-$) and $R_1$ (from $V_-$ to ground). The fraction fed back is $\beta_f = R_1/(R_1 + R_f)$.

1. Finite-gain analysis: $V_- = \beta_fV_{\text{out}}$ and $V_{\text{out}} = A(V_{\text{in}} - \beta_fV_{\text{out}})$.
2. Solving: $\dfrac{V_{\text{out}}}{V_{\text{in}}} = \dfrac{A}{1 + A\beta_f}$.
3. When $A\beta_f \gg 1$ this becomes $1/\beta_f$:
$$\boxed{\frac{V_{\text{out}}}{V_{\text{in}}} = 1 + \frac{R_f}{R_1}}$$
The ideal rules give the same result at once: $V_- = V_{\text{in}}$, so $V_{\text{in}} = V_{\text{out}}R_1/(R_1 + R_f)$.

The input draws no current, so the non-inverting amplifier presents a very high input impedance. With $R_f = 0$ and $R_1$ removed, the gain is exactly 1: the **voltage follower** or **buffer**, which copies a voltage from a weak source to a heavy load without loading the source.

### Other op-amp circuits

- **Summing amplifier:** several inputs, each through its own resistor $R_k$, feed the virtual ground of an inverting amplifier. Their currents add, so $V_{\text{out}} = -R_f\sum_kV_k/R_k$. Audio mixers work this way.
- **Integrator:** replace $R_f$ by a capacitor $C$. The input current $V_{\text{in}}/R$ charges the capacitor, so $V_{\text{out}} = -\dfrac{1}{RC}\displaystyle\int V_{\text{in}}\,dt$.
- **Differentiator:** swap the resistor and capacitor to obtain $V_{\text{out}} = -RC\,dV_{\text{in}}/dt$ (rarely used as is, because it amplifies high-frequency noise).
- **Transimpedance amplifier:** a current source (such as a photodiode) drives the virtual ground directly, and $V_{\text{out}} = -I R_f$ (see Worked Example 15.1).
- **Difference and instrumentation amplifiers:** amplify the difference between two inputs while rejecting voltages common to both, essential for small biological signals such as the electrocardiogram.

### Limits of real op-amps

Real op-amps fall short of the ideal in predictable ways. The output cannot swing beyond the supply rails (often 1 to 2 V inside them for older designs). The open-loop gain falls with frequency, and for most general-purpose op-amps the product of closed-loop gain and bandwidth is roughly constant, the **gain-bandwidth product** (GBW). The closed-loop bandwidth is approximately GBW divided by the **noise gain** $1 + R_f/R_{\text{in}}$. The classic μA741, introduced by Fairchild in 1968, has a typical open-loop gain of about $2\times10^5$ and a GBW of about 1 MHz. Other imperfections include a small input **offset voltage**, small **bias currents** into the inputs and a maximum output rate of change (**slew rate**).

### Worked Example 12.1: Inverting and non-inverting amplifiers

**Problem:** An op-amp with open-loop gain $2\times10^5$, GBW 1 MHz and output limits of about ±13 V (from ±15 V supplies) is used with $R_{\text{in}} = R_1 = 10$ kΩ and $R_f = 47$ kΩ. (a) Find the ideal inverting gain and the output for a 0.20 V input. (b) Find the non-inverting gain and output for the same input. (c) Estimate the error in the non-inverting gain due to finite open-loop gain, and the bandwidth. (d) What happens with a 3.0 V input to the inverting amplifier?

**Solution:**

1. (a) $A_v = -47/10 = -4.7$; $V_{\text{out}} = -4.7\times0.20 = -0.94$ V.
2. (b) $A_v = 1 + 47/10 = 5.7$; $V_{\text{out}} = 5.7\times0.20 = 1.14$ V.
3. (c) $\dfrac{A}{1 + A\beta_f} = \dfrac{2\times10^5}{1 + 2\times10^5/5.7} = 5.69984$, a fractional error of $5.7/(2\times10^5) = 2.9\times10^{-5}$, or 0.003%. Bandwidth $\approx$ GBW/noise gain $= 10^6/5.7 = 175$ kHz.
4. (d) The ideal output would be $-4.7\times3.0 = -14.1$ V, beyond the $-13$ V limit, so the output **saturates** (clips) near $-13$ V, and the virtual-ground rule no longer holds while it is clipped.

**Answer:** (a) $-4.7$, $-0.94$ V; (b) $5.7$, $1.14$ V; (c) error about 0.003%, bandwidth about 175 kHz; (d) the output clips at about $-13$ V.

## 13. RC Circuits, Time Constants and Filters

### Charging and discharging

A resistor $R$ and capacitor $C$ in series, switched onto a DC source $V_0$ at $t = 0$ with the capacitor initially uncharged, obey Kirchhoff's voltage law:
$$V_0 = IR + \frac qC = R\frac{dq}{dt} + \frac qC.$$
Rearranging, $\dfrac{dq}{CV_0 - q} = \dfrac{dt}{RC}$. Integrating from $q = 0$ at $t = 0$ gives $-\ln\left(1 - \dfrac{q}{CV_0}\right) = \dfrac{t}{RC}$, so
$$\boxed{V_C(t) = V_0\left(1 - e^{-t/\tau}\right), \qquad \tau = RC}$$
and the current $I = (V_0/R)e^{-t/\tau}$ decays from its initial value. Discharging from $V_0$ through $R$ gives $V_C(t) = V_0e^{-t/\tau}$. The **time constant** $\tau = RC$ (ohms × farads = seconds) sets the time scale:

| Time | $1\tau$ | $2\tau$ | $3\tau$ | $4\tau$ | $5\tau$ |
|---|---|---|---|---|---|
| Fraction charged, $1 - e^{-t/\tau}$ | 63.2% | 86.5% | 95.0% | 98.2% | 99.3% |

The 10%-to-90% **rise time** is a common measure of speed: the times to reach 10% and 90% of the final voltage are $\tau\ln(10/9)$ and $\tau\ln10$, whose difference is $t_r = \tau\ln9 = 2.20\tau$. Whatever the resistance, charging a capacitor from a fixed voltage dissipates in the resistor exactly as much energy as ends up stored, the same result used for CMOS power in Section 10.

### RC filters

For a sinusoidal signal of angular frequency $\omega$, a capacitor has impedance $Z_C = 1/(j\omega C)$, where $j = \sqrt{-1}$. An RC **low-pass filter** takes its output across the capacitor of a series RC divider:
$$H(\omega) = \frac{V_{\text{out}}}{V_{\text{in}}} = \frac{Z_C}{R + Z_C} = \frac{1}{1 + j\omega RC}.$$
Its magnitude and phase are
$$\lvert H\rvert = \frac{1}{\sqrt{1 + (\omega RC)^2}}, \qquad \phi = -\arctan(\omega RC).$$
At the **cutoff frequency**
$$\boxed{f_c = \frac{1}{2\pi RC}}$$
the magnitude is $1/\sqrt2$ ($-3.01$ dB, so the output power is halved) and the phase lag is 45°. Well above cutoff, $\lvert H\rvert \approx 1/(\omega RC)$: the output falls by a factor of 10 for each tenfold increase in frequency, a **roll-off of 20 dB per decade**. Taking the output across the resistor instead gives the **high-pass filter**, $H = j\omega RC/(1 + j\omega RC)$, which blocks DC and passes high frequencies; it is used to couple AC signals between amplifier stages.

The time and frequency views are linked: a low-pass filter with cutoff $f_c$ has a rise time $t_r = 2.20RC = 2.20/(2\pi f_c) \approx 0.35/f_c$. A system that must respond in a nanosecond needs a bandwidth of hundreds of megahertz. Placing the RC network around an op-amp produces **active filters**, which can have gain, sharper roll-off and buffered outputs.

### Worked Example 13.1: Designing a low-pass filter

**Problem:** Design an RC low-pass filter with a cutoff near 1.0 kHz using a 100 nF capacitor. Choose a standard resistor value, then find the actual cutoff, the attenuation at 100 Hz and 10 kHz, the phase at 1 kHz, the time constant and the rise time.

**Solution:**

1. Required resistance: $R = 1/(2\pi f_cC) = 1/(2\pi\times1000\times100\times10^{-9}) = 1592$ Ω. Choose the standard value 1.6 kΩ.
2. Actual cutoff: $f_c = 1/(2\pi\times1600\times100\times10^{-9}) = 995$ Hz.
3. At 100 Hz: $\lvert H\rvert = 1/\sqrt{1 + (100/995)^2} = 0.995$, or $-0.04$ dB: essentially unaffected.
4. At 10 kHz: $\lvert H\rvert = 1/\sqrt{1 + (10\,000/995)^2} = 0.099$, or $-20.1$ dB.
5. Phase at 1 kHz: $-\arctan(1000/995) = -45.2°$.
6. Time constant: $\tau = 1600\times100\times10^{-9} = 0.16$ ms; rise time $2.20\tau = 0.35$ ms.

**Answer:** $R = 1.6$ kΩ gives $f_c = 995$ Hz; signals at 100 Hz pass almost unchanged, 10 kHz is reduced to 9.9% in amplitude ($-20$ dB), the phase lag at 1 kHz is 45°, and $\tau = 0.16$ ms with a rise time of 0.35 ms.

## 14. Integrated Circuits and Moore's Law

### The integrated circuit

Early transistor circuits were assembled from individual components soldered together, and the number of hand-made connections limited how complex they could become, a problem engineers called the "tyranny of numbers". The solution was to make all the components and their interconnections on one piece of semiconductor.

- On 12 September 1958, **Jack Kilby** at Texas Instruments demonstrated a working circuit made on a single piece of germanium, its components connected by fine gold wires.
- In 1959 **Jean Hoerni** at Fairchild Semiconductor developed the **planar process**, in which a protective layer of silicon dioxide is grown on the wafer and patterned so that dopants can be diffused through openings, leaving junctions buried under the oxide.
- Also in 1959, **Robert Noyce** at Fairchild conceived the monolithic silicon integrated circuit, with the components isolated from each other in the silicon and connected by a metal film deposited over the oxide. This is the basis of every chip made since.

Modern chips are made by repeating cycles of **photolithography** (projecting a pattern onto light-sensitive resist), etching, ion implantation of dopants, and deposition of insulators and metals, on wafers 300 mm in diameter. The most advanced patterning uses **extreme ultraviolet** light of wavelength 13.5 nm. Transistors have changed shape to keep control of ever-shorter channels: planar MOSFETs gave way in the early 2010s to **FinFETs**, in which the gate wraps around a thin vertical fin of silicon, and more recently to **gate-all-around** transistors, in which it surrounds stacked nanosheets.

### Moore's law

In an article in *Electronics* magazine dated 19 April 1965, **Gordon Moore** observed that the number of components on the most economical integrated circuits had been doubling every year, and predicted that the trend would continue for at least a decade. In 1975 he revised the rate to a doubling every two years. This empirical trend, **Moore's law**, held remarkably well for about five decades, partly because the industry used it as a planning target.

| Processor | Year | Approximate transistor count |
|---|---|---|
| Intel 4004 | 1971 | 2 300 |
| Intel 8086 | 1978 | 29 000 |
| Intel 80386 | 1985 | 275 000 |
| Intel Pentium | 1993 | 3.1 million |
| Intel Pentium 4 | 2000 | 42 million |
| Apple M1 | 2020 | 16 billion |
| NVIDIA H100 | 2022 | 80 billion |

### Worked Example 14.1: Testing Moore's law

**Problem:** (a) Starting from the Intel 4004 (2 300 transistors, 1971), predict the transistor count in 2021 if the count doubled every two years. (b) Using the 4004 and the H100 (80 billion, 2022), find the actual average doubling time.

**Solution:**

1. (a) From 1971 to 2021 is 50 years, or 25 doublings. Prediction: $2300\times2^{25} = 2300\times3.36\times10^7 = 7.7\times10^{10}$, about 77 billion.
2. (b) Growth factor: $8.0\times10^{10}/2300 = 3.48\times10^7$.
3. Number of doublings: $\log_2(3.48\times10^7) = \ln(3.48\times10^7)/\ln2 = 25.05$.
4. Average doubling time: $(2022 - 1971)/25.05 = 2.04$ years.

**Answer:** (a) About 77 billion, the same order as the largest chips of the early 2020s. (b) The average doubling time over 51 years is 2.04 years, almost exactly Moore's 1975 rate, representing a growth of more than ten-millionfold.

### Scaling and its limits

In 1974 Robert Dennard and colleagues at IBM showed that if every dimension of a MOSFET and its supply voltage are reduced by the same factor $\kappa$, the transistor becomes faster, its area shrinks by $\kappa^2$, and the power per unit area stays constant. This **Dennard scaling** gave faster, cheaper and more efficient chips with each generation until the mid-2000s. Then supply voltages could no longer fall much, because threshold voltages cannot be reduced without unacceptable leakage (the subthreshold current is set by the Boltzmann factor, which allows at best about a tenfold change in current per 60 mV of gate voltage at room temperature). Power density began to rise, and processor clock frequencies stalled at a few gigahertz. The industry responded with multiple cores, specialized accelerators, three-dimensional transistor structures and stacked chips. Transistor counts have kept rising, but more slowly and at higher cost per new manufacturing generation, and process names such as "3 nm" no longer correspond to any physical length on the chip.

## 15. Worked Circuit Examples

The following examples combine several devices in one circuit.

### Worked Example 15.1: A photodiode light meter

**Problem:** A silicon photodiode with quantum efficiency 0.80 at 850 nm receives 10.0 μW of light. It feeds a transimpedance amplifier (an op-amp with the photodiode driving the virtual ground and a feedback resistor $R_f = 100$ kΩ). Find the responsivity, the photocurrent and the output voltage magnitude. A capacitor $C_f$ is placed in parallel with $R_f$ to filter noise with a cutoff near 1 kHz; find $C_f$.

**Solution:**

1. Responsivity: $\mathcal R = 0.80\times850/1239.84 = 0.548$ A/W (an ideal detector would give 0.686 A/W).
2. Photocurrent: $I = 0.548\times10.0\times10^{-6} = 5.48$ μA.
3. The photodiode sits at the virtual ground, so it operates at zero bias, and all its current flows through $R_f$: $\lvert V_{\text{out}}\rvert = IR_f = 5.48\times10^{-6}\times10^5 = 0.548$ V. (The sign depends on which way the diode is connected.)
4. With $C_f$ in parallel, the feedback impedance is a parallel RC, so the response falls off above $f_c = 1/(2\pi R_fC_f)$. For about 1 kHz: $C_f = 1/(2\pi\times10^5\times1000) = 1.59$ nF; a 1.6 nF capacitor gives $f_c = 995$ Hz.

**Answer:** 0.548 A/W, 5.48 μA, an output of 0.548 V, and $C_f \approx 1.6$ nF. The output is linear in light power over many decades, which is why this circuit is the standard front end of light meters, pulse oximeters and optical receivers.

### Worked Example 15.2: A power-on reset delay

**Problem:** A digital chip must be held in reset for a short time after power is applied. A 10 kΩ resistor charges a 1.0 μF capacitor from $V_{DD}$, and the reset pin reads "high" once the capacitor voltage exceeds $V_{DD}/2$. How long is the chip held in reset?

**Solution:**

1. $\tau = RC = 10^4\times10^{-6} = 0.010$ s.
2. Set $V_{DD}(1 - e^{-t/\tau}) = V_{DD}/2$, so $e^{-t/\tau} = 1/2$ and $t = \tau\ln2$.
3. $t = 0.010\times0.693 = 6.9\times10^{-3}$ s.

**Answer:** About 6.9 ms, independent of the value of $V_{DD}$. The same RC idea is used to **debounce** mechanical switches, whose contacts bounce for a few milliseconds when pressed, by smoothing the bounces before the signal reaches a logic input.

### Worked Example 15.3: A Zener voltage regulator

**Problem:** A 5.1 V Zener diode, fed from a 12.0 V supply through a series resistor, must supply a 20 mA load while keeping at least 5 mA flowing through the Zener. Choose the resistor (standard values include 270 Ω), and find the Zener current and the Zener power if the load is disconnected.

**Solution:**

1. Total current through the resistor must be at least $20 + 5 = 25$ mA.
2. $R = (12.0 - 5.1)/0.025 = 276$ Ω. Choose the next lower standard value, 270 Ω, which gives slightly more current.
3. Resistor current: $(12.0 - 5.1)/270 = 25.6$ mA. With the load connected the Zener carries $25.6 - 20 = 5.6$ mA.
4. With no load, all 25.6 mA flows through the Zener: $P = 5.1\times0.0256 = 0.130$ W.

**Answer:** $R = 270$ Ω; the Zener carries 5.6 mA with the load and must dissipate up to 0.13 W without it, so a 0.5 W Zener is a sensible choice. The regulator wastes power continuously, which is why it is used only for small currents or as a reference.

## 16. Historical Development

The history of semiconductor electronics runs from puzzling laboratory observations through vacuum tubes to the transistor and the chip:

- **1833:** Michael Faraday observes that the conductivity of silver sulfide increases with temperature.
- **1839:** Edmond Becquerel discovers the photovoltaic effect in an electrolytic cell.
- **1873:** Willoughby Smith discovers photoconductivity in selenium.
- **1874:** Ferdinand Braun discovers rectification at metal-sulfide contacts. Crystal detectors with a fine "cat's whisker" wire touching a crystal such as galena (lead sulfide) later became the detectors of early radio receivers.
- **1883:** Charles Fritts builds selenium solar cells with efficiencies around 1%.
- **1904:** John Ambrose Fleming invents the vacuum-tube diode; in 1906 Lee de Forest adds a control grid to make the triode (Audion), which within a few years became the first practical electronic amplifier. Tubes dominated electronics for the next half-century.
- **1907:** Henry Round reports light emission from silicon carbide crystals, the first observation of electroluminescence from a solid.
- **1925–1928:** Julius Lilienfeld patents the principle of the field-effect transistor, but the materials of the day could not realize it.
- **1927:** Harold Black invents the negative-feedback amplifier.
- **1931:** Alan Wilson explains semiconductors using quantum band theory.
- **1937:** Claude Shannon shows that Boolean algebra describes switching circuits.
- **1940:** Russell Ohl at Bell Labs discovers the p-n junction in a silicon sample and observes its photovoltaic response.
- **December 1947:** John Bardeen and Walter Brattain at Bell Labs make the first transistor, a point-contact germanium device. William Shockley devises the junction transistor in early 1948 and publishes the theory of p-n junctions, including the diode equation, in 1949. The three share the 1956 Nobel Prize in Physics.
- **1954:** Texas Instruments produces the first commercial silicon transistors. Daryl Chapin, Calvin Fuller and Gerald Pearson at Bell Labs announce the first practical silicon solar cell, about 6% efficient.
- **1957:** Leo Esaki observes tunneling in heavily doped germanium junctions, the tunnel diode (Nobel Prize 1973).
- **1958–1959:** Kilby, Hoerni and Noyce create the integrated circuit and planar process. Kilby shares the 2000 Nobel Prize in Physics with Zhores Alferov and Herbert Kroemer, honored for semiconductor heterostructures.
- **1959–1960:** Mohamed Atalla and Dawon Kahng at Bell Labs make the first working MOSFET.
- **1961:** Shockley and Queisser derive the efficiency limit of solar cells.
- **1962:** Nick Holonyak at General Electric makes the first visible (red) LED, from GaAsP. Semiconductor lasers are demonstrated the same year.
- **1963:** Wanlass and Sah introduce CMOS.
- **1965:** Gordon Moore formulates his law; Robert Widlar's designs at Fairchild establish the integrated op-amp, followed by the μA741 in 1968.
- **1971:** Intel's 4004, the first commercial single-chip microprocessor, with about 2 300 transistors.
- **1974:** Dennard and colleagues publish their MOSFET scaling rules.
- **1989–1993:** Isamu Akasaki and Hiroshi Amano achieve p-type GaN, and Shuji Nakamura develops bright blue InGaN LEDs, enabling white LED lighting. The three share the 2014 Nobel Prize in Physics.
- **2009:** Willard Boyle and George Smith share half of the Nobel Prize in Physics for inventing the CCD image sensor in 1969.

## 17. Applications

- **Computing and communication:** processors, memory, and the radio transceivers in phones and Wi-Fi routers all rest on CMOS. Fiber-optic links carry most of the world's data using semiconductor lasers and photodiodes.
- **Energy:** photovoltaic modules convert sunlight to electricity; power electronics based on silicon, SiC and GaN transistors convert DC to AC in solar inverters, control the motors of electric vehicles, and make phone chargers small and efficient.
- **Lighting and displays:** LED lighting uses a fraction of the electricity of incandescent lamps. LED-backlit liquid-crystal displays and organic LED displays are ubiquitous; traffic signals and car lights have moved to LEDs.
- **Medicine:** the **pulse oximeter** shines red (around 660 nm) and infrared (around 900–940 nm) LEDs through a fingertip and measures the transmitted light with a photodiode; because oxygenated and deoxygenated hemoglobin absorb these wavelengths differently, the ratio gives blood oxygen saturation. Electrocardiograms and electroencephalograms rely on low-noise instrumentation amplifiers. CT scanners and many digital X-ray panels convert X-rays to visible light in scintillators and detect it with photodiode arrays. Pacemakers and hearing aids run for years on tiny batteries because of low-power CMOS.
- **Sensing and imaging:** every phone camera contains a CMOS image sensor with millions of photodiodes. Diode junctions measure temperature; Hall sensors measure magnetic fields; photodiodes in smoke detectors, barcode scanners and remote-control receivers are everywhere.
- **Industry and vehicles:** programmable logic controllers run factories; modern cars contain dozens of microcontrollers managing engines, brakes and airbags.
- **Space and science:** solar arrays power satellites; CCD and CMOS detectors record astronomical images; silicon strip and pixel detectors track particles at colliders.

## 18. Common Misconceptions

- **"A doped semiconductor carries a net charge."** No. Each donor that releases an electron becomes a positive ion, so n-type silicon is electrically neutral. "n-type" describes the majority carriers, not the net charge.
- **"Holes are just a bookkeeping trick."** A hole is a collective behavior of the many electrons in a nearly full band, but it responds to fields exactly as a positive particle would, with its own mass and mobility, and the Hall effect confirms its positive sign. It is not a positron.
- **"The depletion region is empty of charge."** It is empty of *mobile* carriers but full of fixed ionized dopants. That space charge is precisely what produces the built-in field.
- **"A diode has a fixed voltage drop of 0.7 V."** The current is an exponential function of voltage with no sharp threshold. The forward voltage rises about 60 mV per tenfold increase in current and falls by about 2 mV per kelvin; 0.7 V is only a convenient approximation for silicon at milliamp currents.
- **"A transistor creates energy when it amplifies."** The output power comes from the DC supply. The transistor is a controlled valve; a small input signal steers a much larger flow of energy from the supply.
- **"The base current physically causes the collector current."** In a BJT, the collector current is set by the base-emitter voltage through the injected minority-carrier density; the base current is a by-product of recombination and back-injection. Treating $I_C = \beta I_B$ as a design equation is convenient but fragile, since $\beta$ varies widely.
- **"The op-amp inputs are always at the same voltage."** Only when negative feedback is present and the output is not saturated. A comparator or a clipped amplifier can have volts between its inputs.
- **"A capacitor is fully charged after one time constant."** After one time constant it reaches only 63%; reaching 99% takes about $5\tau$.
- **"CMOS gates draw no power."** They draw almost no *static* power, but every switching event costs $CV^2$ per cycle, and leakage is significant in modern chips. A processor can dissipate over 100 W.
- **"A wider band gap always makes a better solar cell."** Wider gaps raise the voltage but waste the photons below the gap; the single-junction optimum is around 1.3 to 1.4 eV.
- **"Moore's law is a law of physics."** It is an empirical trend in manufacturing and economics. Physics sets limits on it (atomic dimensions, leakage, heat removal), but it was never a natural law.
- **"Silicon is used because it is the best semiconductor."** Its mobility is modest and its gap is indirect. It dominates because it is abundant, can be purified and grown as near-perfect crystals, and grows an excellent native oxide, SiO₂, which made the planar process and MOSFET possible.

## 19. Connections to Other Topics

- **Quantum mechanics:** band structure arises from electron waves in a periodic potential; the band gap, effective mass, hydrogen-like donors, tunneling in Zener and tunnel diodes and in gate leakage, and quantized levels in quantum-well LEDs are all quantum effects. Photon energies $E = h\nu$ set LED colors and detector cutoffs.
- **Statistical mechanics and thermodynamics:** Fermi–Dirac and Boltzmann statistics give carrier densities, the mass-action law and the exponential diode law. The Shockley–Queisser limit is a detailed-balance (thermodynamic) argument. Landauer's principle sets a minimum energy of $k_BT\ln2 = 2.87\times10^{-21}$ J for erasing one bit at 300 K; switching a 1 fF node at 0.8 V costs $CV^2 = 6.4\times10^{-16}$ J, still over $10^5$ times more.
- **Electrostatics and circuits:** Gauss's law gives the depletion width; capacitance governs MOSFET gates, junction capacitance and CMOS power; Ohm's and Kirchhoff's laws underlie every circuit in this chapter.
- **Electromagnetic induction and AC circuits:** rectifiers work with transformers; flyback diodes protect against inductive spikes; impedance generalizes Ohm's law for filters.
- **Chemistry:** doping follows the periodic table (groups 13 and 15 around group 14); covalent bonding and crystal structure determine band gaps; the mass-action law parallels chemical equilibrium; wafer processing is applied chemistry.
- **Information theory and mathematics:** binary representation, Boolean algebra and Shannon's work connect electronics to computation and coding.
- **Biology and medicine:** nerve cells control the flow of ions through voltage-gated channels in their membranes, a loose biological analogue of the gate-controlled channel of a transistor; medical instruments rely on the devices described here.
- **Astronomy and particle physics:** CCDs and CMOS sensors revolutionized astronomical imaging; silicon detectors track particles at accelerators.

## 20. Practice Problems

1. **(Basic)** (a) What is the longest wavelength a GaAs photodiode ($E_g = 1.42$ eV) can detect? (b) What is the photon energy of an InGaN LED emitting at 450 nm? (c) Can a silicon photodiode detect 1550 nm light from an optical fiber? Can a germanium one ($E_g = 0.66$ eV)?
2. **(Basic)** Silicon is doped with $5.0\times10^{15}$ arsenic atoms per cm³. With $n_i = 1.0\times10^{10}$ cm⁻³ and $\mu_n = 1300$ cm²/V·s, find $n$, $p$ and the resistivity. If $2.0\times10^{16}$ boron atoms per cm³ are then added, what type is the material, what are the majority and minority concentrations, and what is the resistivity (take $\mu_p = 400$ cm²/V·s)?
3. **(Basic)** A 10 kΩ resistor and a 47 μF capacitor are connected in series to a 9.0 V battery at $t = 0$. Find the time constant, the capacitor voltage after 1.0 s, the time to reach 90% of 9.0 V, and the cutoff frequency if the same components formed a low-pass filter.
4. **(Basic)** (a) Convert 200 to binary and hexadecimal. (b) Add $01011011_2$ and $00110110_2$ and check the result in decimal. (c) Write $-100$ in 8-bit two's complement. (d) What are the sum and carry outputs of a half adder with inputs $A = B = 1$?
5. **(Intermediate)** A silicon diode has $I_S = 2.0\times10^{-14}$ A and ideality factor 1 at 300 K. Find the forward voltage at 2.0 mA, the increase in voltage needed to raise the current by a factor of 100, and the small-signal resistance at 2.0 mA.
6. **(Intermediate)** A bridge rectifier (0.7 V per diode) is fed by a 9.0 V rms, 60 Hz transformer and supplies 300 mA. Find the minimum reservoir capacitance for ripple no larger than 1.0 V. If the next standard value, 3300 μF, is used, find the ripple and the minimum and peak output voltages. What capacitance would a half-wave rectifier need for the same 1.0 V ripple?
7. **(Intermediate)** An inverting amplifier uses $R_{\text{in}} = 2.2$ kΩ and $R_f = 22$ kΩ with ±15 V supplies; the output saturates at ±13.5 V. Find the gain, the input resistance, and the output for inputs of +0.50 V and +1.5 V. If the op-amp's GBW is 1 MHz, estimate the bandwidth. What gain would the same resistors give in a non-inverting configuration?
8. **(Intermediate)** An npn transistor ($\beta = 150$) with $R_C = 2.2$ kΩ and $V_{CC} = 9.0$ V is biased at $I_C = 2.0$ mA at 300 K. (a) Find $V_{CE}$ (no emitter resistor), $I_B$, $g_m$ and the small-signal gain. (b) The same transistor and collector resistor are instead used as a switch driven from a 5.0 V logic output. Taking $V_{CE(\text{sat})} = 0.2$ V and $V_{BE} = 0.7$ V, choose a base resistor that gives a saturation safety factor of about 5.
9. **(Advanced)** An n-channel MOSFET has $\mu_nC_{ox} = 300$ μA/V², $W/L = 20$ and $V_{th} = 0.45$ V. (a) Find $I_D$ and $g_m$ in saturation at $V_{GS} = 1.2$ V. (b) Find the on-resistance for small $V_{DS}$ at $V_{GS} = 1.8$ V. (c) A CMOS chip has total switched capacitance 20 nF and activity factor 0.15. Find its dynamic power at 0.90 V and 2.5 GHz, and at 0.75 V and 2.0 GHz. By what fraction does power fall, compared with the 20% fall in clock speed?
10. **(Advanced)** A silicon p⁺-n junction has $N_A = 1.0\times10^{18}$ cm⁻³ and $N_D = 1.0\times10^{16}$ cm⁻³ ($n_i = 1.0\times10^{10}$ cm⁻³, $\varepsilon_r = 11.7$, 300 K). Find (a) the built-in potential, (b) the depletion width and peak field at zero bias, (c) the depletion width at 10 V reverse bias, and (d) the junction capacitance of a 1.0 mm² diode at 0 V and at 10 V reverse bias.

### Solutions

**1.** (a) $\lambda_{\max} = 1239.84/1.42 = 873$ nm, in the near infrared. (b) $E = 1239.84/450 = 2.76$ eV. (c) A 1550 nm photon carries $1239.84/1550 = 0.80$ eV, less than silicon's 1.12 eV, so silicon cannot absorb it (silicon is transparent at this wavelength). Germanium's gap of 0.66 eV is smaller than 0.80 eV, so germanium can detect it; its cutoff is $1239.84/0.66 = 1879$ nm.

**2.** $n \approx N_D = 5.0\times10^{15}$ cm⁻³; $p = n_i^2/n = 10^{20}/(5.0\times10^{15}) = 2.0\times10^4$ cm⁻³; $\rho = 1/(qn\mu_n) = 1/[(1.602\times10^{-19})(5.0\times10^{15})(1300)] = 0.96$ Ω·cm. After adding boron, the acceptors outnumber the donors, so the material becomes **p-type** by compensation: $p = N_A - N_D = 2.0\times10^{16} - 5.0\times10^{15} = 1.5\times10^{16}$ cm⁻³, and $n = n_i^2/p = 10^{20}/(1.5\times10^{16}) = 6.7\times10^3$ cm⁻³. Resistivity: $\rho = 1/[(1.602\times10^{-19})(1.5\times10^{16})(400)] = 1.04$ Ω·cm.

**3.** $\tau = RC = (10^4)(47\times10^{-6}) = 0.47$ s. At $t = 1.0$ s: $V_C = 9.0(1 - e^{-1.0/0.47}) = 9.0(1 - 0.119) = 7.93$ V. Reaching 90% requires $e^{-t/\tau} = 0.1$, so $t = \tau\ln10 = 0.47\times2.303 = 1.08$ s. Cutoff frequency: $f_c = 1/(2\pi\times0.47) = 0.339$ Hz; such a slow filter would smooth out anything faster than a few seconds.

**4.** (a) $200 = 128 + 64 + 8 = 11001000_2$; grouping into fours, $1100\ 1000 = \text{C8}_{16}$. (b) $01011011_2 = 91$ and $00110110_2 = 54$. Adding: $01011011 + 00110110 = 10010001_2$, which is $128 + 16 + 1 = 145 = 91 + 54$. (c) $100 = 01100100_2$; invert to $10011011$; add 1 to get $10011100_2$ (which is $156 = 256 - 100$). (d) $S = 1\oplus1 = 0$ and $C = 1\cdot1 = 1$: binary $1 + 1 = 10_2$.

**5.** $V = V_T\ln(I/I_S + 1) = 0.02585\times\ln(2.0\times10^{-3}/2.0\times10^{-14}) = 0.02585\times\ln(10^{11}) = 0.02585\times25.33 = 0.655$ V. A factor of 100 in current requires $\Delta V = V_T\ln100 = 0.02585\times4.605 = 0.119$ V, two decades at 59.5 mV each. Small-signal resistance: $r_d = V_T/I = 0.02585/0.0020 = 12.9$ Ω.

**6.** For a bridge rectifier the ripple frequency is $2\times60 = 120$ Hz, so $C_{\min} = I/(f_r\Delta V) = 0.30/(120\times1.0) = 2.5\times10^{-3}$ F $= 2500$ μF. With 3300 μF: $\Delta V = 0.30/(120\times3300\times10^{-6}) = 0.76$ V. Peak output $= 9.0\sqrt2 - 1.4 = 12.73 - 1.4 = 11.33$ V; minimum $= 11.33 - 0.76 = 10.57$ V. A half-wave rectifier recharges only 60 times per second, so it needs twice the capacitance, 5000 μF, for the same ripple (and its peak output would be one diode drop higher, 12.03 V).

**7.** Gain $= -R_f/R_{\text{in}} = -22/2.2 = -10$; input resistance $= R_{\text{in}} = 2.2$ kΩ. For +0.50 V input, $V_{\text{out}} = -5.0$ V. For +1.5 V input, the ideal result $-15$ V exceeds the $-13.5$ V limit, so the output saturates at $-13.5$ V and the waveform is clipped. The noise gain is $1 + 22/2.2 = 11$, so the bandwidth is about $10^6/11 = 91$ kHz. In the non-inverting configuration the same resistors give $1 + R_f/R_1 = 1 + 10 = 11$.

**8.** (a) $V_{CE} = 9.0 - (2.0\times10^{-3})(2200) = 4.6$ V (active region). $I_B = I_C/\beta = 2.0/150 = 13.3$ μA. $g_m = I_C/V_T = 0.0020/0.02585 = 77.4$ mS. Gain $A_v = -g_mR_C = -0.0774\times2200 = -170$. (b) In saturation the collector current is set by the load: $I_{C(\text{sat})} = (9.0 - 0.2)/2200 = 4.0$ mA. Minimum base current: $4.0\text{ mA}/150 = 26.7$ μA; with a factor of 5, $I_B = 133$ μA. $R_B = (5.0 - 0.7)/(133\times10^{-6}) = 32.3$ kΩ; the standard value 33 kΩ gives $I_B = 4.3/33\,000 = 130$ μA, a safety factor of 4.9.

**9.** (a) $V_{ov} = 1.2 - 0.45 = 0.75$ V. $I_D = \tfrac12(300\times10^{-6})(20)(0.75)^2 = 1.69$ mA. $g_m = 2I_D/V_{ov} = 2(1.6875\times10^{-3})/0.75 = 4.5$ mS. (b) At $V_{GS} = 1.8$ V, $V_{ov} = 1.35$ V, and $R_{on} = 1/[(300\times10^{-6})(20)(1.35)] = 123$ Ω. (c) $P_1 = 0.15\times(20\times10^{-9})\times0.90^2\times(2.5\times10^9) = 6.08$ W. $P_2 = 0.15\times(20\times10^{-9})\times0.75^2\times(2.0\times10^9) = 3.38$ W. The ratio is $3.375/6.075 = 0.556$: power falls by 44% while the clock speed falls by only 20%, which is why lowering voltage and frequency together is so effective for saving battery life.

**10.** (a) $V_{bi} = 0.02585\times\ln\dfrac{(10^{18})(10^{16})}{10^{20}} = 0.02585\times\ln(10^{14}) = 0.02585\times32.24 = 0.833$ V. (b) In SI units, $W = \sqrt{\dfrac{2(1.036\times10^{-10})(0.833)}{1.602\times10^{-19}}\left(10^{-24} + 10^{-22}\right)} = 3.30\times10^{-7}$ m $= 0.330$ μm, almost all of it on the lightly doped n side (the one-sided approximation, ignoring $1/N_A$, gives 0.328 μm). Peak field: $\mathcal E_{\max} = 2V_{bi}/W = 2(0.833)/(3.30\times10^{-7}) = 5.05\times10^6$ V/m $= 50.5$ kV/cm. (c) At 10 V reverse bias: $W = 0.330\times\sqrt{10.833/0.833} = 1.19$ μm (peak field 182 kV/cm). (d) $C = \varepsilon A/W$ with $A = 1.0\times10^{-6}$ m²: at 0 V, $C = (1.036\times10^{-10})(10^{-6})/(3.30\times10^{-7}) = 3.14\times10^{-10}$ F $= 314$ pF; at 10 V reverse bias, $C = (1.036\times10^{-10})(10^{-6})/(1.19\times10^{-6}) = 87$ pF. The capacitance falls as $(V_{bi} - V)^{-1/2}$, the basis of varactor tuning.

## 21. Summary

- **Semiconductors** have a band gap of order 1 eV between a filled valence band and an empty conduction band. The equilibrium concentration of thermally created electron-hole pairs varies as $T^{3/2}e^{-E_g/2k_BT}$; in silicon at 300 K, $n_i \approx 10^{10}$ cm⁻³, and $n_i$ roughly doubles every 9 K.
- **Holes** behave as positive mobile carriers. **Doping** with donors (P, As, Sb) or acceptors (B) sets the majority-carrier density, and the **mass-action law** $np = n_i^2$ fixes the minority density. Conductivity is $q(n\mu_n + p\mu_p)$; drift and diffusion are linked by the Einstein relation $D/\mu = k_BT/q$.
- A **p-n junction** forms a depletion region of fixed ionized dopants, a built-in potential $V_{bi} = V_T\ln(N_AN_D/n_i^2)$ (about 0.7 to 0.9 V in silicon), and a depletion width that grows as the square root of the reverse voltage.
- The **Shockley diode equation** $I = I_S(e^{V/V_T} - 1)$ follows from minority-carrier injection and diffusion: about 0.6 to 0.7 V forward drop for silicon at milliamps, 60 mV per decade, and about $-2$ mV/K. Reverse breakdown by avalanche or Zener tunneling gives voltage references.
- **Rectifiers** convert AC to DC; a reservoir capacitor leaves a ripple $\Delta V \approx I/(f_rC)$.
- **LEDs** in direct-gap materials emit photons of energy near $E_g$; **photodiodes** produce current proportional to light power with responsivity $\eta\lambda/1239.84$ A/W; **solar cells** deliver power with $V_{oc} = V_T\ln(I_L/I_S + 1)$ and are limited to about 33% in a single junction.
- **BJTs** give $I_C = I_Se^{V_{BE}/V_T}$ and current gain $\beta$; **MOSFETs** give $I_D = \tfrac12\mu_nC_{ox}(W/L)(V_{GS} - V_{th})^2$ in saturation with an insulated gate. Both work as switches (cut-off and saturation or triode) and amplifiers (gain $-g_mR$).
- **CMOS** logic pairs complementary transistors so that almost no static current flows; dynamic power is $\alpha CV_{DD}^2f$. **Boolean algebra** and **binary** arithmetic, built from universal NAND or NOR gates, underlie all digital computation.
- **Op-amps** with negative feedback obey two ideal rules (no input current; $V_+ = V_-$), giving inverting gain $-R_f/R_{\text{in}}$ and non-inverting gain $1 + R_f/R_1$ that depend only on resistors.
- **RC circuits** charge with time constant $\tau = RC$ and form filters with cutoff $f_c = 1/(2\pi RC)$ and roll-off of 20 dB per decade.
- **Integrated circuits** (1958–1959) and **Moore's law** (doubling roughly every two years since 1975) took chips from 2 300 transistors in 1971 to tens of billions today; since Dennard scaling ended in the mid-2000s, progress has continued but more slowly and at greater cost.

### Key equations

| Quantity | Equation |
|---|---|
| Thermal voltage | $V_T = k_BT/q = 25.85$ mV at 300 K |
| Photon energy and cutoff | $E = hc/\lambda$, $\lambda_c = 1239.84/E_g$ (nm, eV) |
| Intrinsic carrier concentration | $n_i = \sqrt{N_CN_V}\,e^{-E_g/2k_BT}$ |
| Mass-action law | $np = n_i^2$ |
| Doped material | $n \approx N_D$, $p \approx n_i^2/N_D$ (n-type) |
| Conductivity | $\sigma = q(n\mu_n + p\mu_p)$ |
| Einstein relation | $D/\mu = k_BT/q$ |
| Built-in potential | $V_{bi} = V_T\ln(N_AN_D/n_i^2)$ |
| Depletion width | $W = \sqrt{(2\varepsilon/q)(V_{bi} - V)(1/N_A + 1/N_D)}$ |
| Diode equation | $I = I_S(e^{V/nV_T} - 1)$ |
| Saturation current | $I_S = qAn_i^2[D_p/(L_pN_D) + D_n/(L_nN_A)]$ |
| Diode small-signal resistance | $r_d = V_T/I$ |
| Rectifier ripple | $\Delta V \approx I/(f_rC)$ |
| Photodiode responsivity | $\mathcal R = \eta q\lambda/(hc)$ |
| Solar cell | $I = I_L - I_S(e^{V/V_T} - 1)$, $V_{oc} = V_T\ln(I_L/I_S + 1)$ |
| Fill factor and efficiency | $FF = P_{\max}/(V_{oc}I_{sc})$, $\eta = P_{\max}/P_{\text{in}}$ |
| BJT | $I_C = I_Se^{V_{BE}/V_T}$, $I_C = \beta I_B$, $g_m = I_C/V_T$ |
| Common-emitter gain | $A_v = -g_mR_C$; with degeneration $A_v \approx -R_C/(R_E + r_e)$ |
| MOSFET triode | $I_D = \mu_nC_{ox}(W/L)[(V_{GS} - V_{th})V_{DS} - V_{DS}^2/2]$ |
| MOSFET saturation | $I_D = \tfrac12\mu_nC_{ox}(W/L)(V_{GS} - V_{th})^2$, $g_m = 2I_D/(V_{GS} - V_{th})$ |
| MOSFET on-resistance | $R_{on} = 1/[\mu_nC_{ox}(W/L)(V_{GS} - V_{th})]$ |
| CMOS dynamic power | $P = \alpha CV_{DD}^2f$ |
| Op-amp (open loop) | $V_{\text{out}} = A(V_+ - V_-)$ |
| Inverting amplifier | $V_{\text{out}}/V_{\text{in}} = -R_f/R_{\text{in}}$ |
| Non-inverting amplifier | $V_{\text{out}}/V_{\text{in}} = 1 + R_f/R_1$ |
| Integrator | $V_{\text{out}} = -(1/RC)\int V_{\text{in}}\,dt$ |
| RC charging | $V_C = V_0(1 - e^{-t/RC})$, $\tau = RC$ |
| RC low-pass filter | $\lvert H\rvert = 1/\sqrt{1 + (\omega RC)^2}$, $f_c = 1/(2\pi RC)$ |
| Rise time and bandwidth | $t_r = 2.20RC \approx 0.35/f_c$ |
| Moore's law | $N(t) = N_0\,2^{(t - t_0)/T_2}$, $T_2 \approx 2$ years |

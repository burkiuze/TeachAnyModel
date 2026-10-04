---
title: Electric Current, Resistance and DC Circuits
field: Physics
subfield: Electromagnetism
level: high-school to undergraduate
keywords: [electric current, drift velocity, current density, resistance, resistivity, Ohm's law, electrical power, Joule heating, electromotive force, internal resistance, series and parallel resistors, Kirchhoff's laws, RC circuit, time constant, superconductivity, electrical safety]
---

# Electric Current, Resistance and DC Circuits

When charges move, they constitute an electric current. Controlling currents in circuits underlies all of electrical engineering and electronics. This document covers direct-current (DC) circuits; alternating current is treated with electromagnetic induction.

## 1. Electric Current

**Current** is the rate at which charge flows through a cross-section:
$$\boxed{I = \frac{dQ}{dt}} \qquad [\text{ampere, A} = \text{C/s}]$$
By convention, current direction is the direction positive charges would move ("conventional current"), which is opposite to the actual motion of electrons in metals. This convention predates the discovery of the electron (1897) and remains in use.

Typical currents: a nerve impulse ~μA–nA scale per channel; a smartphone ~0.1–1 A; household circuits up to 10–32 A; a car starter motor ~100–300 A; a lightning stroke ~30 000 A (peak).

### Microscopic picture: drift velocity
In a metal, free electrons move randomly at very high speeds (the Fermi speed, ~$10^6$ m/s), but with no field there is no net flow. An applied field adds a tiny average **drift velocity** $v_d$ opposite to $\vec E$:
$$I = nqv_dA$$
where $n$ is the free-carrier density.

**Worked example 1.1:** A copper wire of cross-section 1 mm² carries 1 A. Copper has about one free electron per atom, $n \approx 8.5 \times 10^{28}$ m⁻³.
$v_d = \frac{I}{neA} = \frac{1}{(8.5\times10^{28})(1.6\times10^{-19})(10^{-6})} \approx 7.4\times10^{-5}$ m/s ≈ 0.07 mm/s.
Electrons drift at a snail's pace — yet a light turns on almost instantly because the electric field (signal) propagates along the wire at a large fraction of the speed of light, setting all electrons in motion nearly simultaneously, like water in an already-full hose.

**Current density** $\vec J = nq\vec v_d$ (A/m²), with $I = \int\vec J\cdot d\vec A$.

**Charge conservation (continuity equation):** $\nabla\cdot\vec J + \frac{\partial\rho}{\partial t} = 0$. In steady state, current into any region equals current out.

## 2. Resistance and Ohm's Law

### Ohm's law
For many materials (ohmic conductors) at constant temperature, current is proportional to the applied voltage:
$$\boxed{V = IR}$$
$R$ is the **resistance**, SI unit the **ohm** (Ω = V/A). Georg Ohm published this relationship in 1827.

Ohm's "law" is an empirical property of certain materials, not a fundamental law. Diodes, transistors, gas discharge tubes and filament bulbs (whose resistance rises as they heat) are non-ohmic.

**Microscopic form:** $\vec J = \sigma\vec E$, where $\sigma$ is the **conductivity**. In the Drude model, electrons accelerate in the field and collide with lattice imperfections and vibrations every $\tau$ seconds on average, giving $\sigma = \frac{ne^2\tau}{m}$.

### Resistivity
For a uniform wire of length $L$ and cross-sectional area $A$:
$$\boxed{R = \rho\frac{L}{A}}$$
$\rho = 1/\sigma$ is the **resistivity** (Ω·m), a property of the material.

| Material | $\rho$ at 20 °C (Ω·m) | Type |
|---|---|---|
| Silver | $1.59\times10^{-8}$ | Conductor |
| Copper | $1.68\times10^{-8}$ | Conductor |
| Gold | $2.44\times10^{-8}$ | Conductor |
| Aluminum | $2.65\times10^{-8}$ | Conductor |
| Iron | $9.7\times10^{-8}$ | Conductor |
| Nichrome | $1.10\times10^{-6}$ | Heating element alloy |
| Graphite | ~$10^{-5}$ | Semimetal |
| Seawater | ~0.2 | Electrolyte |
| Pure silicon | ~$2\times10^{3}$ | Semiconductor |
| Pure water | $1.8\times10^5$ | Poor conductor |
| Glass | $10^{10}$–$10^{14}$ | Insulator |
| Teflon | $>10^{22}$ | Insulator |

Resistivities span over 30 orders of magnitude — one of the widest ranges of any physical property. Copper is used for wiring because it combines low resistivity with low cost; aluminum is used in overhead power lines because of its light weight. Pure water is a poor conductor; tap water conducts because of dissolved ions.

### Temperature dependence
For metals, resistivity rises approximately linearly with temperature (more lattice vibrations → more scattering):
$$\rho(T) = \rho_0[1 + \alpha(T - T_0)]$$
with $\alpha \approx 0.0039$ K⁻¹ for copper. Platinum resistance thermometers exploit this. In semiconductors, resistivity *decreases* with temperature because more charge carriers are thermally excited (thermistors).

### Superconductivity
Below a critical temperature $T_c$, some materials have **exactly zero** resistance and expel magnetic fields (the Meissner effect). Heike Kamerlingh Onnes discovered it in mercury at 4.2 K in 1911. Currents in superconducting loops have persisted for years without measurable decay. Conventional superconductivity is explained by BCS theory (1957): electrons form **Cooper pairs** via lattice vibrations and condense into a coherent quantum state. **High-temperature superconductors** (cuprates, discovered 1986) superconduct above 77 K (liquid nitrogen temperature) — YBa₂Cu₃O₇ at ~92 K. Applications: MRI magnets, particle accelerator magnets (LHC), SQUID magnetometers, maglev trains, and qubits in some quantum computers.

## 3. Electrical Power and Joule Heating

Moving charge $dq$ through a potential difference $V$ transfers energy $V\,dq$, so the power is
$$\boxed{P = IV}$$
For a resistor, using Ohm's law:
$$P = I^2R = \frac{V^2}{R}$$
This energy appears as heat (**Joule heating**). It is useful in heaters, toasters, incandescent bulbs, and fuses, and wasteful in transmission lines and electronics.

**Why power lines use high voltage:** for a given delivered power $P = IV$, raising $V$ lowers $I$, and line losses $I^2R$ fall as $1/V^2$. Transmitting at 400 kV instead of 400 V reduces losses by a factor of a million for the same power. Transformers (which require AC) step voltage up for transmission and down for use.

**Worked example 3.1:** A 2000 W kettle on 230 V draws $I = 2000/230 \approx 8.7$ A; its resistance is $R = V^2/P = 230^2/2000 \approx 26.5$ Ω. Heating 1 L of water from 20 °C to 100 °C needs $Q = 1 \times 4186 \times 80 \approx 335$ kJ, taking about $335\,000/2000 \approx 167$ s (≈2.8 min) if 100% efficient. Energy used: 0.093 kWh.

## 4. EMF and Internal Resistance

A **source of electromotive force** (EMF, $\mathcal E$) — battery, generator, solar cell, thermocouple — does work on charges to move them from low to high potential, converting chemical, mechanical, light or thermal energy into electrical energy. EMF is the work per unit charge (volts) — it is not a force, despite the historical name.

Real sources have **internal resistance** $r$. With an external load $R$:
$$I = \frac{\mathcal E}{R + r}, \qquad V_{\text{terminal}} = \mathcal E - Ir$$
The terminal voltage drops as more current is drawn. A car's headlights dim momentarily when the starter motor draws a large current.

**Maximum power transfer:** the power delivered to the load, $P = \frac{\mathcal E^2R}{(R + r)^2}$, is maximized when $R = r$ (impedance matching). At that point efficiency is only 50%. Power grids are designed for efficiency, not maximum transfer ($R \gg r$); audio amplifiers and radio antennas are often matched.

### Batteries
Batteries convert chemical energy via redox reactions (see electrochemistry). Capacity is rated in ampere-hours (A·h) or mA·h; stored energy ≈ capacity × voltage. A 4000 mA·h, 3.85 V phone battery stores about 15.4 W·h ≈ 55 kJ.

## 5. Resistor Combinations

**Series** (same current through each):
$$R_{\text{eq}} = R_1 + R_2 + \cdots$$
Voltage divides in proportion to resistance: $V_i = V\frac{R_i}{R_{\text{eq}}}$ (voltage divider).

**Parallel** (same voltage across each):
$$\frac{1}{R_{\text{eq}}} = \frac{1}{R_1} + \frac{1}{R_2} + \cdots, \qquad \text{two resistors: } R_{\text{eq}} = \frac{R_1R_2}{R_1 + R_2}$$
Current divides inversely with resistance. The equivalent resistance is always less than the smallest individual resistance.

Household outlets are wired in parallel so each appliance gets the full voltage and can be switched independently. Old-fashioned holiday lights wired in series all went out when one bulb failed.

## 6. Kirchhoff's Rules

For circuits not reducible to simple series/parallel combinations, use Gustav Kirchhoff's rules (1845):

**Junction rule (current law, KCL):** the sum of currents entering any junction equals the sum leaving: $\sum I_{\text{in}} = \sum I_{\text{out}}$. (Charge conservation.)

**Loop rule (voltage law, KVL):** the sum of potential differences around any closed loop is zero: $\sum\Delta V = 0$. (Energy conservation; the electrostatic field is conservative.)

Sign conventions for traversing a loop:
- Through a resistor in the direction of assumed current: $-IR$; against: $+IR$.
- Through an EMF from − to + terminal: $+\mathcal E$; from + to −: $-\mathcal E$.

### Worked example 6.1 – Two-loop circuit
**Problem:** A 12 V battery ($\mathcal E_1$) and a 6 V battery ($\mathcal E_2$), both with positive terminals at the top, are connected in parallel branches with resistors: $R_1 = 2$ Ω in series with $\mathcal E_1$ (left branch), $R_2 = 3$ Ω in series with $\mathcal E_2$ (right branch), and a middle branch $R_3 = 6$ Ω connecting the top and bottom nodes. Find the currents.

**Solution:** Let $I_1$ flow up through the left branch, $I_2$ up through the right branch, and $I_3$ down through the middle.
- Junction (top node): $I_1 + I_2 = I_3$.
- Left loop (left branch up, middle branch down): $12 - 2I_1 - 6I_3 = 0$.
- Right loop (right branch up, middle branch down): $6 - 3I_2 - 6I_3 = 0$.

From the loops: $I_1 = 6 - 3I_3$, $I_2 = 2 - 2I_3$. Substituting into the junction rule: $8 - 5I_3 = I_3 \Rightarrow I_3 = \frac43 \approx 1.333$ A.
Then $I_1 = 6 - 4 = 2$ A and $I_2 = 2 - \frac83 = -\frac23 \approx -0.667$ A.
The negative sign means $I_2$ actually flows **down** through the 6 V battery — the 12 V battery is charging it.
Check: top-node potential relative to bottom $= 6I_3 = 8$ V; left branch: $12 - 2(2) = 8$ V ✓; right branch: $6 - 3(-\frac23) = 8$ V ✓.

### Measuring instruments
- **Ammeter:** measures current; connected in series; ideally zero resistance.
- **Voltmeter:** measures voltage; connected in parallel; ideally infinite resistance.
- **Wheatstone bridge:** four resistors in a diamond with a galvanometer across the middle; balanced (zero galvanometer current) when $R_1/R_2 = R_3/R_x$. Used for precise resistance measurement and in strain gauges.

## 7. RC Circuits

A resistor and capacitor in series produce time-dependent currents.

### Charging
Connecting an uncharged capacitor $C$ through resistor $R$ to EMF $\mathcal E$ at $t = 0$. Loop rule: $\mathcal E - IR - \frac qC = 0$ with $I = dq/dt$:
$$R\frac{dq}{dt} + \frac qC = \mathcal E$$
Solution:
$$\boxed{q(t) = C\mathcal E\left(1 - e^{-t/\tau}\right), \qquad I(t) = \frac{\mathcal E}{R}e^{-t/\tau}, \qquad \tau = RC}$$

### Discharging
A capacitor with initial charge $Q_0$ discharging through $R$:
$$q(t) = Q_0e^{-t/\tau}, \qquad I(t) = -\frac{Q_0}{RC}e^{-t/\tau}$$

### The time constant $\tau = RC$
- After one $\tau$, a charging capacitor reaches $1 - e^{-1} \approx 63.2\%$ of its final charge; a discharging one falls to $e^{-1} \approx 36.8\%$.
- After $5\tau$, it is within 1% of final — practically complete.
- Initially, an uncharged capacitor behaves like a wire (short circuit); after a long time in DC, it behaves like an open circuit (no current).
- Half-life: $t_{1/2} = \tau\ln2 \approx 0.693\tau$.

**Energy accounting during charging:** the battery supplies $Q\mathcal E = C\mathcal E^2$; the capacitor stores $\frac12C\mathcal E^2$; the other half is dissipated in the resistor — **regardless of the value of $R$**.

**Applications:** timing circuits (windshield wipers, 555 timer chips), camera flash charging, filters that smooth or block signals of certain frequencies, pacemakers, and the membrane of nerve cells (which behaves as a leaky RC circuit, setting signal propagation properties).

**Worked example 7.1:** $R = 10$ kΩ, $C = 100$ μF: $\tau = 1$ s. Charging from a 9 V battery, the voltage after 2 s is $9(1 - e^{-2}) \approx 7.78$ V.

## 8. Electrical Safety

- **Current, not voltage, causes injury.** Approximate effects of 60 Hz AC through the torso: ~1 mA perceptible; ~10–20 mA "can't let go" (muscle contraction); ~50–100 mA can cause ventricular fibrillation; >1 A causes severe burns and cardiac arrest.
- Dry skin has a resistance of ~100 kΩ, wet skin ~1 kΩ or less — water greatly increases danger.
- **Fuses and circuit breakers** interrupt excessive currents that would overheat wiring.
- **Ground (earth) wires** provide a low-resistance path so a fault trips the breaker instead of electrifying an appliance's case.
- **Residual-current devices** (GFCI/RCD) detect current imbalance between live and neutral of ~5–30 mA (leakage through a person) and cut power within milliseconds.
- Birds can sit on a single power line safely because there is no potential difference between their feet; touching two lines or a line and a grounded object completes a circuit.

## 9. Summary

| Concept | Formula |
|---|---|
| Current | $I = dQ/dt = nqv_dA$ |
| Ohm's law | $V = IR$; $\vec J = \sigma\vec E$ |
| Resistance | $R = \rho L/A$ |
| Temperature coefficient | $\rho = \rho_0[1 + \alpha\Delta T]$ |
| Power | $P = IV = I^2R = V^2/R$ |
| Real source | $V = \mathcal E - Ir$ |
| Series resistors | $R = R_1 + R_2 + \cdots$ |
| Parallel resistors | $1/R = 1/R_1 + 1/R_2 + \cdots$ |
| Kirchhoff | $\sum I = 0$ (junction), $\sum\Delta V = 0$ (loop) |
| RC charging | $q = C\mathcal E(1 - e^{-t/RC})$ |
| RC discharging | $q = Q_0e^{-t/RC}$ |
| Time constant | $\tau = RC$ |

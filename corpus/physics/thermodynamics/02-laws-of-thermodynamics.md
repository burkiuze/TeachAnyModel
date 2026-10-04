---
title: The Laws of Thermodynamics, Entropy and Heat Engines
field: Physics
subfield: Thermodynamics
level: high-school to undergraduate
keywords: [first law of thermodynamics, internal energy, work, ideal gas, isothermal, adiabatic, isobaric, isochoric, second law, entropy, heat engine, Carnot cycle, refrigerator, heat pump, coefficient of performance, Otto cycle, third law, free energy, Maxwell relations]
---

# The Laws of Thermodynamics, Entropy and Heat Engines

> "A theory is the more impressive the greater the simplicity of its premises, the more different kinds of things it relates, and the more extended its area of applicability. Therefore the deep impression that classical thermodynamics made upon me. It is the only physical theory of universal content which I am convinced will never be overthrown." — Albert Einstein

A popular summary of the laws: (0) there is a game; (1) you can't win — you can at best break even; (2) you can only break even at absolute zero; (3) you can't reach absolute zero.

## 1. Thermodynamic Systems and States

- **System:** the part of the universe under study (gas in a cylinder, a cell, an engine).
- **Surroundings:** everything else.
- **Open system:** exchanges energy and matter. **Closed system:** exchanges energy but not matter. **Isolated system:** exchanges neither.
- **State variables:** properties that define the equilibrium state — pressure $P$, volume $V$, temperature $T$, internal energy $U$, entropy $S$, number of moles $n$. Their changes depend only on initial and final states, not on the path.
- **Path-dependent quantities:** heat $Q$ and work $W$ are *not* state functions. You cannot speak of "the heat in a system".
- **Quasi-static (reversible) process:** a process carried out so slowly that the system passes through a continuous sequence of equilibrium states, and which can be reversed by an infinitesimal change in conditions. Real processes are irreversible to some degree.

### Ideal gas equation of state
$$PV = nRT = Nk_BT$$
$R = 8.314$ J/(mol·K) is the gas constant; $R = N_Ak_B$, with Avogadro's number $N_A = 6.022 \times 10^{23}$ mol⁻¹. At STP (0 °C, 1 atm), one mole of ideal gas occupies 22.4 L; at 25 °C and 1 bar, about 24.8 L.

## 2. Work Done by a Gas

When a gas expands against a piston by volume $dV$, it does work $dW = P\,dV$ on the surroundings. For a finite process:
$$\boxed{W = \int_{V_1}^{V_2}P\,dV}$$
This is the **area under the curve on a $P$–$V$ diagram**. Since different paths between the same states enclose different areas, work is path-dependent. For a cyclic process, the net work equals the area enclosed by the cycle (clockwise cycle → positive net work done by the gas = engine).

**Sign convention:** in this document $W$ is work done **by** the system (common in physics and engineering). Chemistry texts often use work done **on** the system, giving $\Delta U = Q + W$. Always check the convention.

## 3. The First Law of Thermodynamics

> The change in internal energy of a system equals the heat added to the system minus the work done by the system.
$$\boxed{\Delta U = Q - W}, \qquad dU = \delta Q - \delta W$$

The first law is the **law of conservation of energy** extended to include heat. It rules out **perpetual motion machines of the first kind** — devices that produce work without any energy input.

**Internal energy** $U$ is the total microscopic energy of the system (kinetic energy of molecular motion + potential energy of intermolecular forces + chemical and nuclear energy). It is a state function. For an **ideal gas, $U$ depends only on temperature**:
$$U = nC_VT, \qquad C_V = \tfrac{f}{2}R$$
where $f$ is the number of active degrees of freedom per molecule (**equipartition theorem**: each quadratic degree of freedom contributes $\frac12k_BT$ per molecule):
- Monatomic gas (He, Ar): $f = 3$ (translation), $C_V = \frac32R$
- Diatomic gas (N₂, O₂) near room temperature: $f = 5$ (3 translation + 2 rotation), $C_V = \frac52R$; vibration "freezes out" quantum mechanically and becomes active only at high temperatures.

### Heat capacities of an ideal gas
At constant pressure, some of the added heat goes into expansion work, so $C_P > C_V$:
$$\boxed{C_P = C_V + R} \quad\text{(Mayer's relation)}, \qquad \gamma = \frac{C_P}{C_V}$$
- Monatomic: $\gamma = 5/3 \approx 1.67$
- Diatomic: $\gamma = 7/5 = 1.40$ (air)

## 4. Thermodynamic Processes for an Ideal Gas

| Process | Constant | Work by gas $W$ | Heat $Q$ | $\Delta U$ |
|---|---|---|---|---|
| Isochoric | $V$ | $0$ | $nC_V\Delta T$ | $nC_V\Delta T$ |
| Isobaric | $P$ | $P\Delta V = nR\Delta T$ | $nC_P\Delta T$ | $nC_V\Delta T$ |
| Isothermal | $T$ | $nRT\ln(V_2/V_1)$ | $= W$ | $0$ |
| Adiabatic | $Q = 0$ | $\frac{P_1V_1 - P_2V_2}{\gamma - 1} = -nC_V\Delta T$ | $0$ | $nC_V\Delta T$ |

### Isothermal process
Temperature constant ⇒ $\Delta U = 0$ ⇒ $Q = W$. All heat absorbed is converted to work. $PV$ = constant (a hyperbola on the $P$–$V$ diagram).
$$W = \int_{V_1}^{V_2}\frac{nRT}{V}dV = nRT\ln\frac{V_2}{V_1}$$

### Adiabatic process
No heat exchange (fast processes or well-insulated systems). Then $dU = -P\,dV$, i.e. $nC_V\,dT = -\frac{nRT}{V}dV$. Integrating:
$$\boxed{PV^\gamma = \text{const}}, \qquad TV^{\gamma-1} = \text{const}, \qquad TP^{(1-\gamma)/\gamma} = \text{const}$$
Adiabats are steeper than isotherms on a $P$–$V$ diagram.
- **Adiabatic compression heats a gas:** diesel engines ignite fuel without spark plugs by compressing air ~20:1, heating it to over 500 °C. A bicycle pump gets warm.
- **Adiabatic expansion cools a gas:** air rising in the atmosphere expands and cools (~9.8 °C per km for dry air — the dry adiabatic lapse rate), forming clouds when moisture condenses. Spraying an aerosol can makes it cold.

### Worked example 4.1
**Problem:** 2 mol of an ideal diatomic gas at 300 K and 1 atm is compressed adiabatically to one tenth of its volume. Find the final temperature and the work done on the gas.

**Solution:** $\gamma = 1.4$. $T_2 = T_1(V_1/V_2)^{\gamma-1} = 300 \times 10^{0.4} \approx 300 \times 2.512 = 753.6$ K.
Work done on the gas $= \Delta U = nC_V\Delta T = 2 \times \frac52 \times 8.314 \times 453.6 \approx 18\,860$ J ≈ 18.9 kJ.

## 5. The Second Law of Thermodynamics

The first law says energy is conserved but not *which* processes happen. Heat flows spontaneously from hot to cold, never the reverse; a dropped egg breaks but never reassembles; gas fills a room but never spontaneously gathers in a corner. The second law captures this **arrow of time**. Equivalent classical statements:

**Kelvin–Planck statement:** It is impossible to construct a device operating in a cycle whose sole effect is to absorb heat from a single reservoir and convert it entirely into work. (No **perpetual motion machine of the second kind**: you cannot power a ship by extracting heat from the ocean alone.)

**Clausius statement:** It is impossible to construct a device operating in a cycle whose sole effect is to transfer heat from a colder body to a hotter body. (Refrigerators need work input.)

The two statements are logically equivalent: violating one allows you to build a device violating the other.

**Entropy statement:** The total entropy of an isolated system never decreases:
$$\Delta S_{\text{isolated}} \ge 0$$
with equality only for reversible processes.

## 6. Entropy

### Thermodynamic definition (Clausius, 1865)
For a reversible process,
$$\boxed{dS = \frac{\delta Q_{\text{rev}}}{T}}, \qquad \Delta S = \int\frac{\delta Q_{\text{rev}}}{T}$$
Entropy is a state function (J/K). For an irreversible process between the same states, $\Delta S$ is the same (state function), but must be computed along some reversible path. **Clausius inequality:** for any cycle, $\oint\frac{\delta Q}{T} \le 0$.

### Entropy changes in common processes
- **Phase change at temperature $T$:** $\Delta S = \frac{mL}{T}$. Melting 1 kg of ice: $334\,000/273.15 \approx 1223$ J/K.
- **Heating at constant pressure:** $\Delta S = mc\ln\frac{T_2}{T_1}$.
- **Ideal gas, general change:** $\Delta S = nC_V\ln\frac{T_2}{T_1} + nR\ln\frac{V_2}{V_1}$.
- **Isothermal expansion of ideal gas:** $\Delta S = nR\ln\frac{V_2}{V_1}$.
- **Free (Joule) expansion** into a vacuum (irreversible, $Q = 0$, $W = 0$, $\Delta T = 0$ for ideal gas): $\Delta S = nR\ln\frac{V_2}{V_1} > 0$, even though no heat flowed. This shows $\Delta S \ne \int\delta Q/T$ for irreversible processes.

### Worked example 6.1 – Heat flow between reservoirs
1000 J flows from a reservoir at 500 K to one at 300 K.
$\Delta S_{\text{hot}} = -1000/500 = -2$ J/K; $\Delta S_{\text{cold}} = +1000/300 = +3.33$ J/K.
$\Delta S_{\text{total}} = +1.33$ J/K > 0. ✓ Heat flowing from cold to hot would give a negative total, which is forbidden.

### Statistical definition (Boltzmann, 1877)
$$\boxed{S = k_B\ln\Omega}$$
where $\Omega$ is the number of **microstates** (microscopic arrangements) consistent with the macroscopic state. This equation is engraved on Boltzmann's tombstone in Vienna.

Entropy measures how many microscopic ways a macrostate can be realized. Systems evolve toward macrostates with overwhelmingly more microstates simply because those are overwhelmingly more probable. For a gas of $N \sim 10^{23}$ molecules, the probability of all molecules spontaneously gathering in half the container is $2^{-N}$ — not forbidden, but so unlikely that it would never be observed in the lifetime of the universe. **The second law is statistical**, yet effectively absolute for macroscopic systems.

The common description of entropy as "disorder" is a loose analogy; "the number of accessible microstates" or "the spreading of energy" is more accurate. (Example: crystallization of supersaturated solutions or the self-assembly of lipid bilayers can look like "increasing order", but total entropy including the surroundings increases.)

**Gibbs entropy** (general probability distributions): $S = -k_B\sum_ip_i\ln p_i$. Shannon's information entropy, $H = -\sum p_i\log_2p_i$ bits, has the same form.

### Entropy and life
Living organisms maintain low internal entropy by consuming low-entropy energy (food, sunlight) and exporting higher-entropy heat and waste to the environment — as Erwin Schrödinger discussed in *What Is Life?* (1944). Life does not violate the second law. Earth receives sunlight as relatively few high-energy visible photons and radiates the same energy as many more low-energy infrared photons: a net export of entropy.

### Information and entropy
**Landauer's principle:** erasing one bit of information in a computer requires dissipating at least $k_BT\ln2$ of heat (≈ $2.9\times10^{-21}$ J at room temperature). This resolved the paradox of **Maxwell's demon**, a hypothetical being that sorts fast and slow molecules to create a temperature difference without work: the demon must record and eventually erase information, generating at least as much entropy as it removes.

## 7. Heat Engines

A **heat engine** absorbs heat $Q_H$ from a hot reservoir at $T_H$, converts part of it into work $W$, and rejects the rest $Q_C$ to a cold reservoir at $T_C$, operating in a cycle ($\Delta U = 0$ per cycle):
$$W = Q_H - Q_C, \qquad \boxed{\eta = \frac{W}{Q_H} = 1 - \frac{Q_C}{Q_H}}$$
The Kelvin–Planck statement means $Q_C > 0$ always: $\eta < 1$.

### The Carnot cycle
Sadi Carnot (1824) showed that the most efficient engine operating between two reservoirs is a **reversible** one. The Carnot cycle consists of four reversible steps:
1. Isothermal expansion at $T_H$ (absorbs $Q_H$)
2. Adiabatic expansion from $T_H$ to $T_C$
3. Isothermal compression at $T_C$ (rejects $Q_C$)
4. Adiabatic compression from $T_C$ back to $T_H$

For a reversible cycle, total entropy change is zero: $\frac{Q_H}{T_H} = \frac{Q_C}{T_C}$. Hence the **Carnot efficiency**:
$$\boxed{\eta_{\text{Carnot}} = 1 - \frac{T_C}{T_H}}$$
(temperatures in kelvin).

**Carnot's theorem:** no engine operating between two reservoirs can be more efficient than a Carnot engine, and all reversible engines between the same reservoirs have the same efficiency, regardless of the working substance.

Implications:
- 100% efficiency would require $T_C = 0$ K, which is unattainable.
- To increase efficiency, raise $T_H$ or lower $T_C$. This drives the development of high-temperature turbine materials.
- A coal power plant with steam at 550 °C (823 K) and condenser at 30 °C (303 K) has $\eta_{\text{Carnot}} = 1 - 303/823 \approx 63\%$; real plants achieve ~35–45%.
- Ocean thermal energy conversion between 25 °C surface water and 5 °C deep water: $\eta_{\text{Carnot}} = 1 - 278/298 \approx 6.7\%$.

### Real engine cycles
- **Otto cycle** (gasoline engine): two adiabats and two isochors. $\eta = 1 - \frac{1}{r^{\gamma-1}}$, where $r = V_{\max}/V_{\min}$ is the compression ratio. For $r = 10$, $\gamma = 1.4$: $\eta = 1 - 10^{-0.4} \approx 60\%$ ideal; real engines ~25–35% because of friction, heat loss, incomplete combustion. Compression ratio is limited by engine knock (premature autoignition); higher-octane fuels resist knocking.
- **Diesel cycle:** adiabatic compression, isobaric heat addition, adiabatic expansion, isochoric heat rejection. Higher compression ratios (15–22) make diesels more efficient.
- **Rankine cycle:** steam power plants (water boiled, expanded in a turbine, condensed, pumped).
- **Brayton cycle:** gas turbines and jet engines.
- **Stirling engine:** external combustion, regenerator; can approach Carnot efficiency in principle.

## 8. Refrigerators and Heat Pumps

Running a heat engine in reverse uses work $W$ to move heat $Q_C$ from cold to hot, rejecting $Q_H = Q_C + W$.

**Refrigerator / air conditioner** (goal: remove heat from the cold space):
$$K = \text{COP}_{\text{ref}} = \frac{Q_C}{W}, \qquad K_{\text{Carnot}} = \frac{T_C}{T_H - T_C}$$

**Heat pump** (goal: deliver heat to the warm space):
$$\text{COP}_{\text{HP}} = \frac{Q_H}{W}, \qquad \text{COP}_{\text{HP,Carnot}} = \frac{T_H}{T_H - T_C}$$

COP values greater than 1 do not violate energy conservation: the device moves heat rather than creating it. A heat pump heating a house at 20 °C (293 K) from outdoor air at 0 °C (273 K) has Carnot COP $= 293/20 \approx 14.7$; real heat pumps achieve 3–5, meaning 3–5 J of heat delivered per joule of electricity — far better than resistive heating (COP = 1).

**How a vapor-compression refrigerator works:** a refrigerant (e.g. R-134a, R-600a isobutane) evaporates in coils inside the fridge, absorbing latent heat; a compressor raises its pressure and temperature; it condenses in coils at the back, releasing heat to the room; an expansion valve drops its pressure and temperature, and the cycle repeats.

## 9. The Third Law of Thermodynamics

**Nernst–Planck statement:** as $T \to 0$, the entropy of a perfect crystal approaches zero (a single ground-state microstate, $\Omega = 1$).

**Unattainability statement:** it is impossible to reach absolute zero in a finite number of steps.

Consequences: heat capacities and thermal expansion coefficients vanish as $T \to 0$. The third law provides an absolute reference for entropy, so tabulated standard molar entropies $S°$ in chemistry are absolute values. (Some systems such as glasses or ice retain **residual entropy** because they are frozen into disordered configurations; Pauling estimated ice's residual entropy as $R\ln\frac32 \approx 3.4$ J/(mol·K), in agreement with experiment.)

The lowest temperatures achieved in laboratories are below 1 nanokelvin (Bose–Einstein condensates and adiabatic demagnetization experiments), but never zero.

## 10. Thermodynamic Potentials

Combining the first and second laws for reversible processes gives the **fundamental thermodynamic relation**:
$$dU = T\,dS - P\,dV + \mu\,dN$$
where $\mu$ is the chemical potential. Legendre transforms produce other potentials, each natural for particular conditions:

| Potential | Definition | Differential | Natural variables | Use |
|---|---|---|---|---|
| Internal energy | $U$ | $dU = TdS - PdV$ | $S, V$ | Isolated systems |
| Enthalpy | $H = U + PV$ | $dH = TdS + VdP$ | $S, P$ | Heat at constant pressure ($\Delta H = Q_P$) |
| Helmholtz free energy | $F = U - TS$ | $dF = -SdT - PdV$ | $T, V$ | Max work at constant $T$; statistical mechanics |
| Gibbs free energy | $G = H - TS$ | $dG = -SdT + VdP$ | $T, P$ | Chemistry, phase equilibria |

**Spontaneity criteria:**
- At constant $T$ and $V$: processes proceed spontaneously if $\Delta F < 0$.
- At constant $T$ and $P$ (most chemistry and biology): spontaneous if $\Delta G < 0$; equilibrium when $G$ is minimized. $\Delta G = \Delta H - T\Delta S$ shows the competition between energy (enthalpy) and entropy.

**Maxwell relations** follow from the equality of mixed second derivatives, e.g.
$$\left(\frac{\partial S}{\partial V}\right)_T = \left(\frac{\partial P}{\partial T}\right)_V, \qquad \left(\frac{\partial S}{\partial P}\right)_T = -\left(\frac{\partial V}{\partial T}\right)_P$$
They relate hard-to-measure quantities (entropy changes) to easily measured ones ($P$, $V$, $T$).

## 11. Summary

| Law | Statement | Formula |
|---|---|---|
| Zeroth | Thermal equilibrium is transitive; defines temperature | — |
| First | Energy is conserved | $\Delta U = Q - W$ |
| Second | Entropy of isolated system never decreases | $\Delta S \ge 0$; $\eta \le 1 - T_C/T_H$ |
| Third | $S \to 0$ as $T \to 0$ for perfect crystals; $T = 0$ unreachable | — |

| Process (ideal gas) | Key relation |
|---|---|
| Isothermal | $PV = $ const, $W = nRT\ln(V_2/V_1)$ |
| Adiabatic | $PV^\gamma = $ const, $TV^{\gamma-1} = $ const |
| Isobaric | $W = P\Delta V$, $Q = nC_P\Delta T$ |
| Isochoric | $W = 0$, $Q = nC_V\Delta T$ |

**Common mistakes:**
1. Using Celsius instead of kelvin in efficiency, gas law or entropy formulas.
2. Treating heat and work as state functions.
3. Mixing sign conventions for work (by vs. on the system).
4. Thinking entropy can never decrease anywhere — it can decrease locally if a larger increase occurs elsewhere.
5. Believing a COP > 1 violates energy conservation.

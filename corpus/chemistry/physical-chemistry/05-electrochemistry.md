---
title: Electrochemistry - Galvanic Cells, Electrode Potentials, Batteries and Electrolysis
field: Chemistry
subfield: Physical Chemistry
level: high-school to undergraduate
keywords: [electrochemistry, redox, galvanic cell, voltaic cell, anode, cathode, salt bridge, cell notation, standard reduction potential, standard hydrogen electrode, cell potential, Gibbs free energy and EMF, Nernst equation, concentration cell, pH meter, batteries, lithium-ion battery, fuel cell, corrosion, cathodic protection, electrolysis, Faraday's laws, electroplating, chlor-alkali process, aluminum production]
---

# Electrochemistry: Galvanic Cells, Electrode Potentials, Batteries and Electrolysis

Electrochemistry studies the interconversion of chemical and electrical energy through **redox reactions**, in which electrons are transferred. It explains batteries in phones and electric cars, fuel cells, corrosion of bridges and ships, electroplating, the industrial production of aluminum and chlorine, nerve impulses, and sensors such as pH meters and glucose monitors.

## 1. Redox Review

- **Oxidation:** loss of electrons (oxidation number increases).
- **Reduction:** gain of electrons (oxidation number decreases).
- Mnemonic: **OIL RIG**, or "LEO the lion says GER" (Lose Electrons Oxidation, Gain Electrons Reduction).
- In a spontaneous redox reaction like $\text{Zn}(s) + \text{Cu}^{2+}(aq)\to\text{Zn}^{2+}(aq) + \text{Cu}(s)$, a zinc strip in copper sulfate solution becomes coated with copper while the blue color fades. Electrons transfer directly; the energy is released as heat.

If we **separate** the oxidation and reduction half-reactions and connect them with a wire, the electrons flow through the wire — an electric current that can do work.

## 2. Galvanic (Voltaic) Cells

Named after Luigi Galvani and Alessandro Volta (who built the first battery, the "voltaic pile", in 1800).

### The Daniell cell (Zn–Cu)
- **Anode** (oxidation, negative terminal in a galvanic cell): Zn(s) → Zn²⁺(aq) + 2e⁻. The zinc electrode dissolves.
- **Cathode** (reduction, positive terminal): Cu²⁺(aq) + 2e⁻ → Cu(s). Copper deposits.
- Electrons flow through the external wire **from anode to cathode**.
- A **salt bridge** (e.g. KNO₃ or KCl in gel) completes the circuit by allowing ion migration, maintaining electrical neutrality: anions move toward the anode compartment, cations toward the cathode. Without it, charge buildup would stop the current immediately.
- Standard cell potential: 1.10 V.

Mnemonics: "**An Ox** and a **Red Cat**" (anode = oxidation, reduction = cathode). Both "anode" and "oxidation" start with vowels; "cathode" and "reduction" with consonants.

### Cell notation
$$\text{Zn}(s)\,|\,\text{Zn}^{2+}(aq, 1\text{ M})\,\|\,\text{Cu}^{2+}(aq, 1\text{ M})\,|\,\text{Cu}(s)$$
Anode on the left, cathode on the right; single vertical lines are phase boundaries; the double line is the salt bridge. Inert electrodes (Pt, graphite) are used when the half-reaction involves no solid metal, e.g. $\text{Pt}\,|\,\text{Fe}^{2+}, \text{Fe}^{3+}$.

## 3. Standard Electrode Potentials

### The standard hydrogen electrode (SHE)
Absolute potentials of single electrodes cannot be measured, only differences. By convention, the **standard hydrogen electrode** — Pt in 1 M H⁺ with H₂ gas at 1 bar — is assigned 0 V:
$$2\text{H}^+(aq) + 2e^-\rightleftharpoons\text{H}_2(g), \qquad E° = 0.000\text{ V}$$

### Standard reduction potentials
Each half-reaction is written as a **reduction** and assigned $E°$ (volts, 25 °C, 1 M, 1 bar). A more positive $E°$ means a greater tendency to be reduced (stronger oxidizing agent).

| Half-reaction | $E°$ (V) |
|---|---|
| F₂ + 2e⁻ → 2F⁻ | +2.87 |
| H₂O₂ + 2H⁺ + 2e⁻ → 2H₂O | +1.78 |
| MnO₄⁻ + 8H⁺ + 5e⁻ → Mn²⁺ + 4H₂O | +1.51 |
| Au³⁺ + 3e⁻ → Au | +1.50 |
| Cl₂ + 2e⁻ → 2Cl⁻ | +1.36 |
| Cr₂O₇²⁻ + 14H⁺ + 6e⁻ → 2Cr³⁺ + 7H₂O | +1.33 |
| O₂ + 4H⁺ + 4e⁻ → 2H₂O | +1.23 |
| Br₂ + 2e⁻ → 2Br⁻ | +1.07 |
| NO₃⁻ + 4H⁺ + 3e⁻ → NO + 2H₂O | +0.96 |
| Ag⁺ + e⁻ → Ag | +0.80 |
| Fe³⁺ + e⁻ → Fe²⁺ | +0.77 |
| O₂ + 2H⁺ + 2e⁻ → H₂O₂ | +0.70 |
| I₂ + 2e⁻ → 2I⁻ | +0.54 |
| O₂ + 2H₂O + 4e⁻ → 4OH⁻ | +0.40 |
| Cu²⁺ + 2e⁻ → Cu | +0.34 |
| AgCl + e⁻ → Ag + Cl⁻ | +0.22 |
| 2H⁺ + 2e⁻ → H₂ | 0.00 |
| Pb²⁺ + 2e⁻ → Pb | −0.13 |
| Sn²⁺ + 2e⁻ → Sn | −0.14 |
| Ni²⁺ + 2e⁻ → Ni | −0.26 |
| PbSO₄ + 2e⁻ → Pb + SO₄²⁻ | −0.36 |
| Fe²⁺ + 2e⁻ → Fe | −0.44 |
| Zn²⁺ + 2e⁻ → Zn | −0.76 |
| 2H₂O + 2e⁻ → H₂ + 2OH⁻ | −0.83 |
| Al³⁺ + 3e⁻ → Al | −1.66 |
| Mg²⁺ + 2e⁻ → Mg | −2.37 |
| Na⁺ + e⁻ → Na | −2.71 |
| Ca²⁺ + 2e⁻ → Ca | −2.87 |
| K⁺ + e⁻ → K | −2.93 |
| Li⁺ + e⁻ → Li | −3.04 |

- **F₂** is the strongest oxidizing agent; **Li** is the strongest reducing agent (in water).
- Metals with negative $E°$ (below H₂) dissolve in non-oxidizing acids, releasing H₂; copper, silver and gold do not. Gold dissolves in **aqua regia** (3 HCl : 1 HNO₃) because chloride forms the stable complex [AuCl₄]⁻, lowering the effective reduction potential.

### Standard cell potential
$$\boxed{E°_{\text{cell}} = E°_{\text{cathode}} - E°_{\text{anode}}}$$
(both as reduction potentials). **Do not multiply $E°$ by stoichiometric coefficients** — potential is an intensive property (energy per charge).

**Worked example 3.1:** Zn–Cu cell: $E° = 0.34 - (-0.76) = 1.10$ V.
**Worked example 3.2:** a cell with Ag⁺/Ag and Cu²⁺/Cu: Ag⁺ has the higher $E°$, so it is reduced (cathode): $E° = 0.80 - 0.34 = 0.46$ V. Reaction: $2\text{Ag}^+ + \text{Cu}\to2\text{Ag} + \text{Cu}^{2+}$.

A positive $E°_{\text{cell}}$ means the reaction is spontaneous as written under standard conditions.

## 4. Thermodynamics of Electrochemical Cells

### Free energy and cell potential
The electrical work a cell can do is charge × voltage. The maximum work equals $-\Delta G$:
$$\boxed{\Delta G = -nFE_{\text{cell}}}, \qquad \Delta G° = -nFE°_{\text{cell}}$$
- $n$ = moles of electrons transferred per mole of reaction.
- $F$ = **Faraday constant** = charge of one mole of electrons = $N_Ae = 96\,485$ C/mol.

$E > 0 \Leftrightarrow \Delta G < 0$ (spontaneous).

### Relation to the equilibrium constant
Combining with $\Delta G° = -RT\ln K$:
$$E°_{\text{cell}} = \frac{RT}{nF}\ln K = \frac{0.0592\text{ V}}{n}\log K\quad(25\text{ °C})$$

**Worked example 4.1:** for the Daniell cell ($n = 2$, $E° = 1.10$ V): $\Delta G° = -2(96\,485)(1.10) = -212$ kJ/mol; $\log K = 2(1.10)/0.0592 = 37.2$, $K \approx 10^{37}$. The reaction goes essentially to completion.

| $E°_{\text{cell}}$ | $\Delta G°$ | $K$ | Direction |
|---|---|---|---|
| > 0 | < 0 | > 1 | Spontaneous forward |
| 0 | 0 | 1 | Equilibrium |
| < 0 | > 0 | < 1 | Non-spontaneous (reverse spontaneous) |

## 5. The Nernst Equation

Cell potentials depend on concentrations (Walther Nernst, 1889; Nobel 1920):
$$\boxed{E = E° - \frac{RT}{nF}\ln Q = E° - \frac{0.0592\text{ V}}{n}\log Q\quad(25\text{ °C})}$$
- As the reaction proceeds, $Q$ increases and $E$ decreases.
- At equilibrium, $Q = K$ and $E = 0$ — a "dead" battery is a cell at equilibrium.

**Worked example 5.1:** Daniell cell with [Zn²⁺] = 0.010 M and [Cu²⁺] = 1.0 M:
$Q = [\text{Zn}^{2+}]/[\text{Cu}^{2+}] = 0.010$. $E = 1.10 - \frac{0.0592}{2}\log(0.010) = 1.10 + 0.059 = 1.16$ V.

### Concentration cells
Both electrodes are the same material, but the concentrations differ. Then $E° = 0$, yet a voltage still develops:
$$E = \frac{0.0592\text{ V}}{n}\log\frac{C_{\text{cathode}}}{C_{\text{anode}}}$$
The cathode is the electrode in the more concentrated solution; the cell runs until the concentrations equalize. Example: Cu | Cu²⁺ (0.001 M) || Cu²⁺ (1 M) | Cu gives $E = \frac{0.0592}{2}\times3 = 0.089$ V.

### Biological membrane potentials
Nerve and muscle cells maintain ion concentration gradients across their membranes (K⁺ high inside, Na⁺ high outside). The **equilibrium potential** for each ion follows the Nernst equation; at 37 °C, $E = \frac{61.5\text{ mV}}{z}\log\frac{[\text{ion}]_{\text{out}}}{[\text{ion}]_{\text{in}}}$. For K⁺ with 140 mM inside and 5 mM outside: $E_K \approx 61.5\log(5/140) \approx -89$ mV. The resting potential (~−70 mV) lies near $E_K$, as described by the Goldman–Hodgkin–Katz equation. Action potentials arise from voltage-gated Na⁺ channels opening (driving potential toward $E_{Na} \approx +60$ mV) followed by K⁺ channels.

### pH meters and ion-selective electrodes
A glass electrode's potential depends on [H⁺] through a Nernst-like relationship, changing by 59.2 mV per pH unit at 25 °C. Ion-selective electrodes for Na⁺, K⁺, Ca²⁺, F⁻ and others work similarly. Reference electrodes (saturated calomel, +0.244 V; Ag/AgCl, +0.197 V in saturated KCl) provide stable comparison potentials.

## 6. Batteries

A battery is one or more galvanic cells packaged for use. **Primary** batteries are single-use; **secondary** (rechargeable) batteries are recharged by forcing current in reverse.

| Battery | Anode | Cathode | Electrolyte | Voltage | Notes |
|---|---|---|---|---|---|
| Zinc–carbon (Leclanché) | Zn | MnO₂ (graphite rod collector) | NH₄Cl/ZnCl₂ paste | 1.5 V | Cheap, primary |
| Alkaline | Zn powder | MnO₂ | KOH | 1.5 V | Longer life than zinc–carbon |
| Silver oxide | Zn | Ag₂O | KOH | 1.55 V | Watches, hearing aids |
| Lithium primary (Li–MnO₂) | Li | MnO₂ | Organic | 3.0 V | Coin cells, cameras |
| Lead–acid | Pb | PbO₂ | H₂SO₄ | 2.0 V/cell (12 V with 6 cells) | Rechargeable; cars |
| Nickel–cadmium | Cd | NiO(OH) | KOH | 1.2 V | Rechargeable; largely replaced |
| Nickel–metal hydride | Metal hydride | NiO(OH) | KOH | 1.2 V | Hybrid cars, AA rechargeables |
| Lithium-ion | Li in graphite (LiC₆) | LiCoO₂, LiFePO₄, NMC, NCA | Li salt (LiPF₆) in organic carbonate | 3.2–3.7 V | Phones, laptops, EVs |

### Lead–acid battery
Discharge:
- Anode: $\text{Pb} + \text{SO}_4^{2-}\to\text{PbSO}_4 + 2e^-$
- Cathode: $\text{PbO}_2 + 4\text{H}^+ + \text{SO}_4^{2-} + 2e^-\to\text{PbSO}_4 + 2\text{H}_2\text{O}$
- Overall: $\text{Pb} + \text{PbO}_2 + 2\text{H}_2\text{SO}_4\to2\text{PbSO}_4 + 2\text{H}_2\text{O}$, $E° \approx 2.04$ V
Sulfuric acid is consumed during discharge, so the electrolyte's density indicates the state of charge. Invented by Gaston Planté in 1859, it remains widely used because it delivers high current cheaply; ~99% of lead–acid batteries are recycled in many countries.

### Lithium-ion battery
Lithium ions shuttle between a graphite anode and a metal-oxide cathode through an electrolyte (**intercalation** — "rocking chair" battery):
- Discharge (anode): $\text{LiC}_6\to\text{C}_6 + \text{Li}^+ + e^-$
- Discharge (cathode): $\text{CoO}_2 + \text{Li}^+ + e^-\to\text{LiCoO}_2$
Lithium is the lightest metal and has the most negative reduction potential, giving high voltage and energy density (~150–270 W·h/kg at the cell level vs. ~35 W·h/kg for lead–acid). John Goodenough, M. Stanley Whittingham and Akira Yoshino received the 2019 Nobel Prize in Chemistry for its development. Challenges: thermal runaway and fires (flammable electrolyte), dendrite formation, degradation over cycles, and the supply of cobalt and lithium. Variants: LiFePO₄ (safer, longer cycle life, cheaper, lower energy density), NMC (nickel–manganese–cobalt), solid-state batteries (in development), sodium-ion batteries (cheaper, abundant materials).

## 7. Fuel Cells

Fuel cells convert chemical energy directly into electricity as long as fuel and oxidant are supplied.

**Hydrogen–oxygen fuel cell (PEM, acidic):**
- Anode: $2\text{H}_2\to4\text{H}^+ + 4e^-$
- Cathode: $\text{O}_2 + 4\text{H}^+ + 4e^-\to2\text{H}_2\text{O}$
- Overall: $2\text{H}_2 + \text{O}_2\to2\text{H}_2\text{O}$, $E° = 1.23$ V
The only product is water. Fuel cells powered the Apollo spacecraft (providing drinking water too) and are used in some vehicles, buses, forklifts and backup power systems. Efficiencies of 40–60% exceed those of combustion engines limited by Carnot efficiency, since fuel cells are not heat engines. Platinum catalysts and hydrogen production/storage remain challenges. Most hydrogen is currently made from natural gas ("grey hydrogen"); "green hydrogen" comes from electrolysis powered by renewable electricity.

## 8. Corrosion

Corrosion is the unwanted electrochemical oxidation of metals. Rusting of iron costs an estimated 3–4% of GDP in industrialized countries.

**Mechanism of rusting** (iron in contact with water and oxygen):
- Anodic region: $\text{Fe}\to\text{Fe}^{2+} + 2e^-$ (pits form here)
- Cathodic region (often at the water–air edge): $\text{O}_2 + 4\text{H}^+ + 4e^-\to2\text{H}_2\text{O}$ (or $\text{O}_2 + 2\text{H}_2\text{O} + 4e^-\to4\text{OH}^-$)
- Fe²⁺ migrates and is further oxidized to Fe³⁺, forming hydrated iron(III) oxide, Fe₂O₃·xH₂O (rust).
Rust is porous and flakes off, exposing fresh metal. Salt (road salt, seawater) accelerates corrosion by increasing conductivity. Acidic conditions also accelerate it.

**Prevention:**
- **Barrier coatings:** paint, oil, plastic, enamel.
- **Passivation:** aluminum, chromium and stainless steel (iron + ≥10.5% chromium) form thin, adherent oxide layers that protect the metal beneath. Aluminum is very reactive ($E° = -1.66$ V) yet resists corrosion because of its Al₂O₃ film.
- **Galvanizing:** coating iron with zinc. Zinc is more easily oxidized and corrodes preferentially (sacrificial), even if the coating is scratched.
- **Cathodic protection:** connecting a more active metal (Mg, Zn, Al) as a **sacrificial anode** to steel structures — ship hulls, pipelines, water heaters, offshore platforms — or applying an external current (impressed-current cathodic protection).
- **Avoiding galvanic couples:** connecting dissimilar metals in an electrolyte makes the more active one corrode (the Statue of Liberty's iron framework corroded where it contacted the copper skin, requiring restoration in the 1980s). Tin-plated steel ("tin cans") corrodes faster than bare steel if the tin is scratched, because iron is more active than tin.

## 9. Electrolysis

**Electrolysis** uses an external power source to drive a **non-spontaneous** redox reaction ($\Delta G > 0$). In an electrolytic cell:
- **Anode** (oxidation) is connected to the **positive** terminal.
- **Cathode** (reduction) is connected to the **negative** terminal.
(Anode = oxidation and cathode = reduction still hold; only the signs differ from galvanic cells.)

### Examples
- **Molten NaCl** (Downs cell): cathode $\text{Na}^+ + e^-\to\text{Na}(l)$; anode $2\text{Cl}^-\to\text{Cl}_2(g) + 2e^-$. Produces sodium metal and chlorine.
- **Water** (with an electrolyte such as Na₂SO₄): cathode $2\text{H}_2\text{O} + 2e^-\to\text{H}_2 + 2\text{OH}^-$; anode $2\text{H}_2\text{O}\to\text{O}_2 + 4\text{H}^+ + 4e^-$. Overall $2\text{H}_2\text{O}\to2\text{H}_2 + \text{O}_2$, requiring at least 1.23 V (in practice ~1.8–2 V due to **overpotential**). Produces twice as much H₂ as O₂ by volume.
- **Aqueous NaCl (chlor-alkali process):** water (not Na⁺) is reduced at the cathode (giving H₂ and OH⁻); at high Cl⁻ concentration, Cl⁻ is oxidized at the anode (Cl₂) despite O₂ being thermodynamically favored, because of oxygen's large overpotential. Products: Cl₂, H₂ and NaOH — major industrial chemicals (~90 million tonnes of Cl₂ per year). Membrane cells separate the products.
- **Aluminum production (Hall–Héroult process, 1886):** alumina (Al₂O₃) dissolved in molten cryolite (Na₃AlF₆) at ~950 °C is electrolyzed: $\text{Al}^{3+} + 3e^-\to\text{Al}$ at the cathode; carbon anodes are consumed ($\text{C} + 2\text{O}^{2-}\to\text{CO}_2 + 4e^-$). It requires ~13–15 kWh per kg of aluminum, which is why recycling aluminum (using ~5% of the energy) is so valuable. Before this process, aluminum was more precious than gold; Napoleon III reportedly served honored guests with aluminum cutlery. Charles Martin Hall (USA) and Paul Héroult (France) discovered it independently in the same year, both aged 22–23.
- **Electrorefining of copper:** impure copper anodes dissolve; pure copper (99.99%) deposits on the cathode; precious metals (Ag, Au, Pt) collect as "anode mud".
- **Electroplating:** depositing a thin metal layer (silver, gold, chromium, nickel, zinc) on an object made the cathode.
- **Anodizing:** thickening the protective oxide layer on aluminum (the object is the anode), often dyed for color.

### Faraday's laws of electrolysis
Michael Faraday (1833–1834): the amount of substance produced at an electrode is proportional to the charge passed:
$$\boxed{n_{\text{substance}} = \frac{Q}{zF} = \frac{It}{zF}}, \qquad m = \frac{ItM}{zF}$$
where $I$ is current (A), $t$ time (s), $z$ electrons per ion, $M$ molar mass.

**Worked example 9.1:** how long must 10.0 A flow to deposit 5.00 g of copper from Cu²⁺?
$n(\text{Cu}) = 5.00/63.55 = 0.0787$ mol; electrons $= 2\times0.0787 = 0.157$ mol; $Q = 0.157\times96\,485 = 15\,180$ C; $t = 15\,180/10.0 = 1518$ s ≈ 25.3 min.

**Worked example 9.2:** mass of aluminum produced by 100 000 A in 24 h: $Q = 10^5\times86\,400 = 8.64\times10^9$ C; $n(e^-) = 8.95\times10^4$ mol; $n(\text{Al}) = 2.98\times10^4$ mol; $m \approx 806$ kg.

## 10. Summary

| Concept | Formula |
|---|---|
| Cell potential | $E°_{\text{cell}} = E°_{\text{cathode}} - E°_{\text{anode}}$ |
| Free energy | $\Delta G° = -nFE°$ |
| Equilibrium | $E° = \frac{0.0592}{n}\log K$ (25 °C) |
| Nernst equation | $E = E° - \frac{0.0592}{n}\log Q$ |
| Faraday constant | $F = 96\,485$ C/mol e⁻ |
| Faraday's law | $n = It/(zF)$ |
| Galvanic cell | Spontaneous; anode (−), cathode (+) |
| Electrolytic cell | Non-spontaneous; anode (+), cathode (−) |
| Always | Oxidation at anode, reduction at cathode |

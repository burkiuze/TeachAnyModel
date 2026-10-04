---
title: Metabolism and Bioenergetics
field: Chemistry
subfield: Biochemistry
level: undergraduate
keywords: [metabolism, catabolism, anabolism, ATP, phosphoryl transfer potential, NAD+, FAD, glycolysis, fermentation, lactic acid, pyruvate dehydrogenase, citric acid cycle, Krebs cycle, electron transport chain, oxidative phosphorylation, chemiosmotic theory, ATP synthase, P/O ratio, gluconeogenesis, glycogen metabolism, pentose phosphate pathway, beta-oxidation, ketone bodies, fatty acid synthesis, amino acid catabolism, urea cycle, photosynthesis, light reactions, Calvin cycle, Rubisco, insulin, glucagon, metabolic regulation]
---

# Metabolism and Bioenergetics

**Metabolism** is the sum of all chemical reactions in a living organism — thousands of reactions organized into pathways that extract energy from nutrients, build cellular components, and dispose of wastes. Despite the enormous diversity of life, core metabolic pathways (glycolysis, the citric acid cycle, oxidative phosphorylation) are remarkably conserved from bacteria to humans, reflecting their ancient origin.

## 1. Principles of Metabolism

- **Catabolism:** breakdown of complex molecules into simpler ones, releasing energy (captured as ATP and reduced electron carriers). Convergent: many nutrients funnel into a few intermediates (acetyl-CoA).
- **Anabolism:** biosynthesis of complex molecules from simple precursors, consuming energy (ATP) and reducing power (NADPH). Divergent.
- Catabolic and anabolic pathways between the same compounds are **distinct**, with at least one different, irreversible step, allowing independent regulation and making each direction thermodynamically favorable.
- Pathways are often **compartmentalized**: glycolysis, fatty-acid synthesis and the pentose phosphate pathway in the cytosol; citric acid cycle, β-oxidation and oxidative phosphorylation in mitochondria.

### ATP: the energy currency
Adenosine triphosphate stores energy in its **phosphoanhydride bonds**:
$$\text{ATP} + \text{H}_2\text{O}\to\text{ADP} + \text{P}_i, \qquad \Delta G°' = -30.5\text{ kJ/mol}\;(\text{in cells } \approx -50\text{ to }-57\text{ kJ/mol})$$
Reasons hydrolysis is favorable: relief of electrostatic repulsion among the closely spaced negative charges; resonance stabilization of the products (P_i); better solvation of products; and increased entropy.

ATP sits in the middle of the **phosphoryl-transfer potential** scale: phosphoenolpyruvate (−61.9 kJ/mol), 1,3-bisphosphoglycerate (−49.4), phosphocreatine (−43.0) can phosphorylate ADP; ATP can phosphorylate glucose (glucose-6-phosphate, −13.8). This intermediate position makes ATP an ideal energy shuttle. **Phosphocreatine** buffers ATP in muscle during the first seconds of intense exercise.

A human at rest turns over roughly 40–75 kg of ATP per day, although the body contains only ~250 g at any moment — each ATP molecule is recycled ~1000+ times daily.

### Electron carriers
Biological oxidations remove electrons (usually as hydride or hydrogen atoms), passing them to carriers:
- **NAD⁺ → NADH** (nicotinamide adenine dinucleotide; accepts a hydride, H⁻): catabolic oxidations.
- **NADP⁺ → NADPH:** reducing power for biosynthesis and antioxidant defense.
- **FAD → FADH₂** (flavin adenine dinucleotide; accepts 2 H): e.g. succinate dehydrogenase, fatty-acid oxidation.
- **Coenzyme Q (ubiquinone), cytochromes:** in the electron transport chain.

**Coenzyme A** (from pantothenate) carries acyl groups as high-energy thioesters (acetyl-CoA).

## 2. Glycolysis

**Glycolysis** (the Embden–Meyerhof–Parnas pathway) splits one glucose (C₆) into two pyruvate (C₃) in the cytosol, in 10 enzyme-catalyzed steps. It occurs in nearly all organisms and does not require oxygen.

**Net reaction:**
$$\text{Glucose} + 2\text{NAD}^+ + 2\text{ADP} + 2\text{P}_i\to2\text{Pyruvate} + 2\text{NADH} + 2\text{H}^+ + 2\text{ATP} + 2\text{H}_2\text{O}$$

### Phase 1: energy investment (steps 1–5)
1. **Hexokinase:** glucose + ATP → glucose-6-phosphate (G6P). Irreversible; traps glucose in the cell. (Liver: glucokinase, with high $K_M$, acts when glucose is abundant.)
2. **Phosphoglucose isomerase:** G6P ⇌ fructose-6-phosphate (aldose → ketose).
3. **Phosphofructokinase-1 (PFK-1):** F6P + ATP → fructose-1,6-bisphosphate. Irreversible; **the committed, rate-limiting, main regulatory step**. Inhibited by ATP and citrate; activated by AMP, ADP and **fructose-2,6-bisphosphate**.
4. **Aldolase:** F1,6BP → dihydroxyacetone phosphate (DHAP) + glyceraldehyde-3-phosphate (GAP) — a retro-aldol cleavage.
5. **Triose phosphate isomerase:** DHAP ⇌ GAP (a "catalytically perfect" enzyme). Now 2 GAP per glucose.

### Phase 2: energy payoff (steps 6–10, ×2)
6. **Glyceraldehyde-3-phosphate dehydrogenase:** GAP + NAD⁺ + P_i → 1,3-bisphosphoglycerate + NADH. (Oxidation energy captured in an acyl phosphate; uses a cysteine thioester intermediate. Arsenate can substitute for phosphate, uncoupling ATP production — one reason arsenic is toxic.)
7. **Phosphoglycerate kinase:** 1,3-BPG + ADP → 3-phosphoglycerate + **ATP** (substrate-level phosphorylation).
8. **Phosphoglycerate mutase:** 3-PG → 2-PG.
9. **Enolase:** 2-PG → phosphoenolpyruvate (PEP) + H₂O (inhibited by fluoride).
10. **Pyruvate kinase:** PEP + ADP → pyruvate + **ATP**. Irreversible; regulated (activated by F1,6BP — feed-forward; inhibited by ATP, alanine; inactivated by phosphorylation in liver).

**Yield:** 4 ATP produced − 2 ATP invested = **2 net ATP** + **2 NADH** per glucose.

### Fates of pyruvate
- **Aerobic:** pyruvate enters mitochondria → acetyl-CoA → citric acid cycle → oxidative phosphorylation.
- **Lactic acid fermentation** (muscle during intense exercise, red blood cells, some bacteria — yogurt, sauerkraut): pyruvate + NADH → lactate + NAD⁺ (lactate dehydrogenase). Regenerates NAD⁺ so glycolysis can continue. Lactate is recycled to glucose in the liver (**Cori cycle**). (Muscle soreness a day or two after exercise is due to microdamage, not lactic acid.)
- **Alcoholic fermentation** (yeast): pyruvate → acetaldehyde + CO₂ (pyruvate decarboxylase, TPP) → ethanol (alcohol dehydrogenase, regenerating NAD⁺). Used in brewing, winemaking and bread rising. Louis Pasteur showed fermentation is caused by living yeast; Eduard Buchner (1897, Nobel 1907) showed cell-free yeast extracts ferment sugar, founding biochemistry.

**Warburg effect:** many cancer cells rely heavily on glycolysis and lactate production even in the presence of oxygen ("aerobic glycolysis"), consuming large amounts of glucose — exploited by **FDG-PET** imaging (¹⁸F-fluorodeoxyglucose).

## 3. Pyruvate Dehydrogenase Complex

In the mitochondrial matrix, the **pyruvate dehydrogenase complex** (PDH) links glycolysis to the citric acid cycle:
$$\text{Pyruvate} + \text{CoA} + \text{NAD}^+\to\text{Acetyl-CoA} + \text{CO}_2 + \text{NADH}$$
A huge multienzyme complex (E1, E2, E3) using **five coenzymes**: TPP (B₁), lipoamide, CoA (B₅), FAD (B₂) and NAD⁺ (B₃). Irreversible: in animals, acetyl-CoA cannot be converted back to glucose. Regulated by product inhibition (acetyl-CoA, NADH) and phosphorylation (PDH kinase inactivates; PDH phosphatase activates). Thiamine deficiency (alcoholism, beriberi) impairs PDH, harming the brain, which depends heavily on glucose oxidation.

## 4. The Citric Acid Cycle (Krebs Cycle, TCA Cycle)

Elucidated by Hans Krebs (1937; Nobel 1953). Eight steps in the mitochondrial matrix oxidize the acetyl group of acetyl-CoA to 2 CO₂, capturing energy in NADH, FADH₂ and GTP.

1. **Citrate synthase:** acetyl-CoA (C₂) + oxaloacetate (C₄) → citrate (C₆). (Inhibited by citrate, NADH, succinyl-CoA.)
2. **Aconitase:** citrate ⇌ isocitrate (via cis-aconitate). (Inhibited by fluorocitrate from the rat poison fluoroacetate.)
3. **Isocitrate dehydrogenase:** isocitrate → α-ketoglutarate (C₅) + CO₂ + **NADH**. (Rate-limiting; activated by ADP, Ca²⁺; inhibited by ATP, NADH.)
4. **α-Ketoglutarate dehydrogenase complex:** α-KG → succinyl-CoA (C₄) + CO₂ + **NADH**. (Similar to PDH.)
5. **Succinyl-CoA synthetase:** succinyl-CoA → succinate + **GTP** (or ATP) — substrate-level phosphorylation.
6. **Succinate dehydrogenase:** succinate → fumarate + **FADH₂**. (Embedded in the inner membrane; also Complex II of the electron transport chain; inhibited competitively by malonate.)
7. **Fumarase:** fumarate + H₂O → L-malate.
8. **Malate dehydrogenase:** malate → oxaloacetate + **NADH**. (Oxaloacetate is regenerated — the cycle is catalytic.)

**Per acetyl-CoA:** 3 NADH + 1 FADH₂ + 1 GTP + 2 CO₂. **Per glucose** (2 turns): 6 NADH, 2 FADH₂, 2 GTP, 4 CO₂.

**Amphibolic nature:** the cycle provides intermediates for biosynthesis — α-ketoglutarate → glutamate and other amino acids; oxaloacetate → aspartate and glucose (gluconeogenesis); succinyl-CoA → heme; citrate → fatty acids (exported to cytosol). **Anaplerotic reactions** replenish intermediates (e.g. pyruvate carboxylase: pyruvate + CO₂ + ATP → oxaloacetate, requiring biotin).

## 5. Oxidative Phosphorylation

### The electron transport chain (ETC)
In the inner mitochondrial membrane, electrons from NADH and FADH₂ pass through a series of carriers of increasing reduction potential to O₂, the final electron acceptor:

| Complex | Name | Electron flow | Protons pumped (per 2 e⁻) |
|---|---|---|---|
| I | NADH dehydrogenase (NADH:ubiquinone oxidoreductase) | NADH → FMN → Fe–S → CoQ | 4 |
| II | Succinate dehydrogenase | Succinate → FAD → Fe–S → CoQ | 0 |
| CoQ | Ubiquinone (mobile, lipid-soluble) | Carries electrons from I and II to III | — |
| III | Cytochrome bc₁ complex | CoQH₂ → cyt b, c₁ → cyt c (Q cycle) | 4 |
| Cyt c | Cytochrome c (mobile, peripheral protein) | Carries electrons from III to IV | — |
| IV | Cytochrome c oxidase | Cyt c → Cu, heme a/a₃ → O₂ → H₂O | 2 |

Overall: $\text{NADH} + \text{H}^+ + \tfrac12\text{O}_2\to\text{NAD}^+ + \text{H}_2\text{O}$, with $\Delta E°' = +0.82 - (-0.32) = 1.14$ V and $\Delta G°' = -nF\Delta E°' = -220$ kJ/mol — released stepwise rather than explosively.

**Inhibitors:** rotenone (Complex I; a fish poison and pesticide), antimycin A (Complex III), **cyanide, azide, carbon monoxide and hydrogen sulfide** (Complex IV) — which is why cyanide is so rapidly lethal.

### Chemiosmotic theory
**Peter Mitchell** (1961; Nobel 1978) proposed that the energy of electron transport is stored as a **proton gradient** (proton-motive force) across the inner membrane: protons pumped from the matrix into the intermembrane space create both a pH gradient (~0.75 units) and a membrane potential (~150–180 mV, matrix negative). Initially controversial, it is now a cornerstone of bioenergetics, operating in mitochondria, chloroplasts and bacterial membranes.

### ATP synthase
Protons flow back into the matrix through **ATP synthase** (Complex V, F₀F₁), driving ATP synthesis: $\text{ADP} + \text{P}_i\to\text{ATP}$.
- **F₀:** membrane-embedded ring of c subunits through which protons pass, causing the ring to **rotate**.
- **F₁:** catalytic head (α₃β₃) in the matrix; a central γ stalk rotates within it.
- **Binding-change mechanism** (Paul Boyer): each β subunit cycles through open, loose and tight conformations; rotation releases tightly bound ATP. John Walker solved the F₁ structure (Boyer and Walker, Nobel 1997). Rotation was directly observed by attaching a fluorescent actin filament to the γ subunit (Noji, Yoshida and colleagues, 1997). It is a true rotary molecular motor, spinning up to ~100+ revolutions per second, producing 3 ATP per revolution.
- About 3–4 protons are needed per ATP (including the cost of transporting ADP, P_i and ATP across the membrane).

### Uncouplers
**Uncouplers** dissipate the proton gradient, so electron transport continues without ATP synthesis and energy is released as heat.
- **2,4-Dinitrophenol** (DNP) was sold as a weight-loss drug in the 1930s; it caused deaths from hyperthermia and was banned.
- **Thermogenin (UCP1)** in **brown adipose tissue** is a natural uncoupler generating heat in newborns, hibernating animals and cold-adapted adults (non-shivering thermogenesis).

### ATP yield from glucose
Modern estimates (P/O ratios ≈ 2.5 ATP per NADH, 1.5 per FADH₂):

| Source | ATP |
|---|---|
| Glycolysis (net substrate-level) | 2 |
| Glycolytic NADH (2) — via glycerol-phosphate shuttle (1.5 each) or malate–aspartate shuttle (2.5 each) | 3–5 |
| Pyruvate dehydrogenase (2 NADH) | 5 |
| Citric acid cycle: 6 NADH | 15 |
| Citric acid cycle: 2 FADH₂ | 3 |
| Citric acid cycle: 2 GTP | 2 |
| **Total** | **~30–32** |

(Older textbooks cite 36–38 using P/O ratios of 3 and 2.) The overall equation:
$$\text{C}_6\text{H}_{12}\text{O}_6 + 6\text{O}_2\to6\text{CO}_2 + 6\text{H}_2\text{O}, \qquad \Delta G°' \approx -2870\text{ kJ/mol}$$
Capturing ~30 ATP × ~50 kJ/mol under cellular conditions ≈ 1500 kJ, an efficiency of roughly 40–50% — superior to most engines.

**Reactive oxygen species (ROS):** a small fraction of electrons leak to O₂ prematurely, forming superoxide (O₂·⁻), hydrogen peroxide and hydroxyl radicals, which damage lipids, proteins and DNA (implicated in aging). Defenses: superoxide dismutase, catalase, glutathione peroxidase, vitamins C and E.

**Mitochondria** have their own circular DNA (~16.6 kb in humans, encoding 13 proteins of the ETC, 22 tRNAs and 2 rRNAs), inherited maternally — evidence of their origin as endosymbiotic bacteria (Lynn Margulis's endosymbiotic theory).

## 6. Gluconeogenesis and Glycogen Metabolism

### Gluconeogenesis
Synthesis of glucose from non-carbohydrate precursors (lactate, pyruvate, glycerol, glucogenic amino acids such as alanine) — mainly in the **liver** (and kidney), essential during fasting because the brain needs ~120 g of glucose per day and red blood cells depend entirely on glucose.
- Reverses glycolysis but **bypasses its three irreversible steps** with different enzymes:
  1. Pyruvate → oxaloacetate (**pyruvate carboxylase**, mitochondrial, biotin) → PEP (**PEP carboxykinase**, uses GTP).
  2. Fructose-1,6-bisphosphate → F6P (**fructose-1,6-bisphosphatase**).
  3. G6P → glucose (**glucose-6-phosphatase**, in the ER; absent in muscle, so muscle glycogen cannot supply blood glucose).
- Cost: 4 ATP + 2 GTP + 2 NADH per glucose (vs. 2 ATP gained in glycolysis).
- **Reciprocal regulation** with glycolysis prevents futile cycles: fructose-2,6-bisphosphate activates PFK-1 and inhibits fructose-1,6-bisphosphatase; acetyl-CoA activates pyruvate carboxylase.
- **Fatty acids cannot be converted to glucose in animals** (acetyl-CoA cannot become pyruvate; two carbons enter and two leave as CO₂ in the cycle). Plants and bacteria can, using the **glyoxylate cycle**.

### Glycogen metabolism
- **Glycogenesis:** glucose-1-phosphate + UTP → UDP-glucose; **glycogen synthase** adds glucose units by α(1→4) bonds; a branching enzyme creates α(1→6) branches. A protein primer, glycogenin, starts each particle.
- **Glycogenolysis:** **glycogen phosphorylase** cleaves α(1→4) bonds by phosphorolysis (giving G1P without spending ATP); a debranching enzyme handles branch points. Liver glycogen maintains blood glucose; muscle glycogen fuels contraction.
- **Hormonal control:** **glucagon** (liver) and **epinephrine** (liver and muscle) activate a cAMP → protein kinase A cascade that phosphorylates (activates) phosphorylase and (inactivates) glycogen synthase. **Insulin** promotes dephosphorylation, favoring glycogen synthesis. Earl Sutherland discovered cAMP as a second messenger (Nobel 1971); Carl and Gerty Cori discovered glycogen metabolism steps (Nobel 1947).
- **Glycogen storage diseases** (e.g. von Gierke's — glucose-6-phosphatase deficiency; McArdle's — muscle phosphorylase deficiency).

### Pentose phosphate pathway
An alternative route for G6P in the cytosol:
- **Oxidative phase:** G6P → ribulose-5-phosphate + CO₂, generating **2 NADPH** (glucose-6-phosphate dehydrogenase is the rate-limiting enzyme).
- **Non-oxidative phase:** interconversion of sugars (transketolase, transaldolase) producing **ribose-5-phosphate** for nucleotides or recycling to glycolytic intermediates.
- NADPH is needed for fatty-acid and steroid synthesis and to keep glutathione reduced (protecting red blood cells from oxidative damage). **G6PD deficiency** — the most common human enzyme deficiency (~400 million people) — causes hemolytic anemia after oxidative stress (fava beans, some antimalarial drugs), but confers partial malaria resistance.

## 7. Lipid Metabolism

### Fatty-acid oxidation (β-oxidation)
1. **Activation** (cytosol): fatty acid + CoA + ATP → fatty acyl-CoA + AMP + PP_i (costs the equivalent of 2 ATP).
2. **Transport into mitochondria** via the **carnitine shuttle** (carnitine palmitoyltransferase I is the regulated step, inhibited by malonyl-CoA, which prevents simultaneous synthesis and breakdown).
3. **β-Oxidation spiral** (matrix): each cycle of four reactions (oxidation by FAD, hydration, oxidation by NAD⁺, thiolysis) removes a two-carbon acetyl-CoA unit and produces 1 FADH₂ + 1 NADH.

**Palmitate (C16)** yields 7 cycles → 8 acetyl-CoA + 7 FADH₂ + 7 NADH. ATP: 8 × 10 (via citric acid cycle) + 7 × 1.5 + 7 × 2.5 = 80 + 10.5 + 17.5 = 108, minus 2 for activation = **106 ATP** — far more per carbon than glucose (~32 ATP per 6 carbons). Unsaturated and odd-chain fatty acids require extra enzymes (odd chains yield propionyl-CoA → succinyl-CoA, using vitamin B₁₂).

### Ketone bodies
During prolonged fasting, starvation, very low-carbohydrate diets or uncontrolled type 1 diabetes, the liver converts excess acetyl-CoA into **ketone bodies** — acetoacetate, β-hydroxybutyrate and acetone (exhaled; "fruity breath"). The heart, muscle and, after a few days of fasting, the brain use ketone bodies as fuel, sparing protein. Excessive production causes **diabetic ketoacidosis**, a medical emergency.

### Fatty-acid synthesis
Occurs in the cytosol (liver, adipose tissue, mammary glands), mainly when carbohydrates are abundant:
- Acetyl-CoA is exported from mitochondria as **citrate** (citrate lyase regenerates acetyl-CoA in the cytosol).
- **Acetyl-CoA carboxylase** (biotin; committed, regulated step): acetyl-CoA + CO₂ + ATP → **malonyl-CoA**. Activated by citrate and insulin; inhibited by palmitoyl-CoA, glucagon and AMP-activated protein kinase (AMPK).
- **Fatty-acid synthase** (a large multifunctional enzyme) adds two-carbon units from malonyl-CoA (releasing CO₂, which drives the condensation) in cycles of condensation, reduction (NADPH), dehydration and reduction (NADPH), until palmitate (C16) is formed. Elongases and desaturases make other fatty acids.
- Cost for palmitate: 7 ATP + 14 NADPH.

### Cholesterol synthesis
From acetyl-CoA via HMG-CoA → **mevalonate** (HMG-CoA reductase: rate-limiting; target of **statins**) → isoprene units → squalene → lanosterol → cholesterol (Konrad Bloch and Feodor Lynen, Nobel 1964). Regulated by feedback through the SREBP transcription system and LDL receptors (Brown and Goldstein, Nobel 1985).

## 8. Amino Acid Metabolism and the Urea Cycle

- Dietary proteins are digested to amino acids; body proteins turn over continuously (~300–400 g/day in adults).
- **Transamination:** aminotransferases (PLP coenzyme) transfer amino groups to α-ketoglutarate, forming glutamate. Blood **ALT** and **AST** levels indicate liver or heart damage.
- **Oxidative deamination:** glutamate dehydrogenase releases NH₄⁺.
- **Carbon skeletons:** **glucogenic** amino acids yield pyruvate or citric acid cycle intermediates (can form glucose); **ketogenic** amino acids (leucine and lysine exclusively) yield acetyl-CoA or acetoacetate.
- **Ammonia is toxic** (especially to the brain). Fish excrete NH₃ directly (ammonotelic); birds and reptiles excrete uric acid (uricotelic, water-conserving); mammals convert it to **urea** (ureotelic).

### The urea cycle
Discovered by Hans Krebs and Kurt Henseleit (1932) — the first metabolic cycle described. Occurs in the liver, partly in mitochondria and partly in the cytosol:
1. NH₄⁺ + HCO₃⁻ + 2 ATP → **carbamoyl phosphate** (carbamoyl phosphate synthetase I; activated by N-acetylglutamate).
2. Carbamoyl phosphate + **ornithine** → **citrulline**.
3. Citrulline + **aspartate** + ATP → **argininosuccinate**.
4. Argininosuccinate → **arginine** + **fumarate** (links to the citric acid cycle — the "Krebs bicycle").
5. Arginine + H₂O → **urea** + ornithine (arginase).
Net: $\text{NH}_4^+ + \text{HCO}_3^- + \text{aspartate} + 3\text{ATP}\to\text{urea} + \text{fumarate} + 2\text{ADP} + \text{AMP} + \ldots$ (4 high-energy phosphate bonds per urea). Urea contains two nitrogens: one from NH₄⁺ and one from aspartate. Genetic defects cause hyperammonemia.

### Amino acids as precursors
Neurotransmitters (tyrosine → dopamine → norepinephrine → epinephrine; tryptophan → serotonin → melatonin; glutamate → GABA; histidine → histamine), heme (from glycine and succinyl-CoA), creatine, nitric oxide (from arginine), purines and pyrimidines, glutathione, thyroid hormones, melanin. **Phenylketonuria (PKU):** deficiency of phenylalanine hydroxylase; phenylalanine accumulates and damages the developing brain unless a low-phenylalanine diet is followed — newborns are screened worldwide (Guthrie test). Aspartame-containing products carry warnings for people with PKU.

## 9. Photosynthesis

Photosynthesis converts light energy into chemical energy, producing nearly all the organic matter and oxygen on Earth:
$$6\text{CO}_2 + 6\text{H}_2\text{O}\xrightarrow{\text{light}}\text{C}_6\text{H}_{12}\text{O}_6 + 6\text{O}_2, \qquad \Delta G°' \approx +2870\text{ kJ/mol}$$
In plants and algae it occurs in **chloroplasts** (descended from endosymbiotic cyanobacteria).

### Light-dependent reactions (thylakoid membranes)
- **Chlorophylls** (Mg-porphyrins) and accessory pigments (carotenoids) in antenna complexes absorb light (mainly blue ~430 nm and red ~660 nm; green is reflected) and funnel excitation energy to **reaction centers**.
- **Photosystem II (P680):** excited chlorophyll donates an electron; the oxidized P680⁺ is one of the strongest biological oxidants and pulls electrons from water via the **oxygen-evolving complex** (a Mn₄CaO₅ cluster): $2\text{H}_2\text{O}\to\text{O}_2 + 4\text{H}^+ + 4e^-$. **All atmospheric O₂ comes from this reaction** (Ruben and Kamen showed with ¹⁸O in 1941 that the O₂ comes from water, not CO₂).
- Electrons pass via plastoquinone → **cytochrome b₆f** (pumping protons) → plastocyanin → **Photosystem I (P700)**, re-excited by light → ferredoxin → **NADP⁺ reductase**, forming **NADPH**.
- The proton gradient drives **chloroplast ATP synthase** (photophosphorylation).
- The energetics of the two photosystems in series is depicted as the **Z-scheme**.
- **Cyclic electron flow** around PSI produces ATP without NADPH.

### Calvin cycle (light-independent reactions, stroma)
Melvin Calvin traced the pathway using ¹⁴CO₂ and paper chromatography (Nobel 1961).
1. **Carbon fixation:** **Rubisco** (ribulose-1,5-bisphosphate carboxylase/oxygenase) adds CO₂ to ribulose-1,5-bisphosphate (C₅), producing two 3-phosphoglycerate (C₃).
2. **Reduction:** 3-PG is reduced to glyceraldehyde-3-phosphate using ATP and NADPH.
3. **Regeneration:** most G3P regenerates ribulose-1,5-bisphosphate (using more ATP).
Fixing 3 CO₂ costs 9 ATP and 6 NADPH and yields one net G3P (so one glucose requires 18 ATP and 12 NADPH).

**Rubisco** is probably the most abundant protein on Earth, but it is slow (~3 reactions per second) and also reacts with O₂ (**photorespiration**), wasting energy, especially in hot, dry conditions. **C₄ plants** (maize, sugarcane) and **CAM plants** (cacti, pineapple) concentrate CO₂ around Rubisco to minimize photorespiration, using PEP carboxylase and spatial or temporal separation.

Photosynthetic efficiency: crops typically convert ~1% of incident solar energy into biomass (theoretical maximum ~4.6% for C₃ and ~6% for C₄ plants).

## 10. Integration and Hormonal Regulation of Metabolism

| State | Hormones | Liver | Muscle | Adipose tissue |
|---|---|---|---|---|
| **Fed** (high glucose) | ↑ Insulin | Glycogen synthesis, glycolysis, fatty-acid synthesis | Glucose uptake (GLUT4), glycogen and protein synthesis | Triglyceride storage |
| **Fasting** (low glucose) | ↑ Glucagon | Glycogenolysis, gluconeogenesis, ketogenesis | Uses fatty acids and ketones; protein breakdown in prolonged fasting | Lipolysis (fatty acids + glycerol released) |
| **Stress / exercise** | ↑ Epinephrine, cortisol | Glycogenolysis, gluconeogenesis | Glycogenolysis, glycolysis | Lipolysis |

- **Insulin** (from pancreatic β-cells; discovered by Banting, Best, Collip and Macleod, 1921–22) promotes uptake and storage of fuel. **Glucagon** (α-cells) mobilizes fuel.
- **Diabetes mellitus:** type 1 — autoimmune destruction of β-cells (insulin deficiency); type 2 — insulin resistance plus impaired secretion, linked to obesity. Both cause hyperglycemia; uncontrolled type 1 can lead to ketoacidosis. Treatments include insulin, metformin (reduces hepatic gluconeogenesis), SGLT2 inhibitors, and GLP-1 receptor agonists (semaglutide), which also cause significant weight loss.
- **AMPK** acts as a cellular energy sensor, activated by high AMP/ATP ratios, switching on catabolism and switching off anabolism. **mTOR** promotes growth when nutrients are plentiful.
- **Fuel preferences:** brain — glucose (ketone bodies in prolonged fasting); heart — fatty acids; red blood cells — glucose only (glycolysis); active skeletal muscle — glucose, glycogen and fatty acids.

## 11. Summary

| Pathway | Location | Input → Output | Key regulatory enzyme |
|---|---|---|---|
| Glycolysis | Cytosol | Glucose → 2 pyruvate + 2 ATP + 2 NADH | PFK-1 |
| Pyruvate dehydrogenase | Mitochondrial matrix | Pyruvate → acetyl-CoA + CO₂ + NADH | PDH complex |
| Citric acid cycle | Mitochondrial matrix | Acetyl-CoA → 2 CO₂ + 3 NADH + FADH₂ + GTP | Isocitrate dehydrogenase |
| Oxidative phosphorylation | Inner mitochondrial membrane | NADH, FADH₂ + O₂ → H₂O + ATP | Driven by proton gradient |
| Gluconeogenesis | Liver (mitochondria + cytosol) | Lactate, amino acids, glycerol → glucose | Fructose-1,6-bisphosphatase |
| Pentose phosphate | Cytosol | G6P → NADPH + ribose-5-P | G6P dehydrogenase |
| β-Oxidation | Mitochondrial matrix | Fatty acyl-CoA → acetyl-CoA + NADH + FADH₂ | CPT-I (carnitine shuttle) |
| Fatty-acid synthesis | Cytosol | Acetyl-CoA + NADPH → palmitate | Acetyl-CoA carboxylase |
| Urea cycle | Liver (mitochondria + cytosol) | NH₄⁺ + aspartate → urea | Carbamoyl phosphate synthetase I |
| Photosynthesis (light) | Thylakoid membrane | H₂O + light → O₂ + ATP + NADPH | — |
| Calvin cycle | Chloroplast stroma | CO₂ + ATP + NADPH → G3P | Rubisco |

**Yields:** glucose → ~30–32 ATP aerobically, 2 ATP anaerobically; palmitate → 106 ATP.

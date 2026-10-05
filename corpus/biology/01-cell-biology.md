---
title: Cell Biology - Structure and Function of Cells
field: Biology
subfield: Cell Biology
level: high-school to undergraduate
keywords: [cell theory, prokaryotes, eukaryotes, microscopy, plasma membrane, nucleus, ribosomes, endoplasmic reticulum, Golgi apparatus, lysosomes, mitochondria, chloroplasts, endosymbiotic theory, cytoskeleton, cell wall, cell junctions, cell signaling, receptors, second messengers, cell cycle, mitosis, cytokinesis, checkpoints, cancer, apoptosis, stem cells, viruses, surface-area-to-volume ratio, diffusion, Abbe diffraction limit, electron microscopy, sedimentation coefficient, membrane transport, osmosis, tonicity, Nernst equation, membrane potential, chemiosmosis, proton-motive force, ATP synthase, receptor occupancy, signal amplification, exponential growth, cell-cycle kinetics, mitotic index, telomeres]
---

# Cell Biology: Structure and Function of Cells

The **cell** is the fundamental unit of life. Every living organism is made of one or more cells, and every cell arises from a pre-existing cell. A single adult human body contains roughly 30–37 trillion human cells (and a comparable number of bacterial cells, mostly in the colon). Classical histology recognizes about 200 major cell types, and single-cell gene-expression atlases are revealing several hundred finer subtypes — yet all of them share common machinery for storing information, producing energy and building molecules.

This chapter moves from the cell theory and the instruments used to see cells, through the anatomy of prokaryotic and eukaryotic cells, to the physical chemistry of membranes and energy conversion, and then to signaling, division, death and differentiation. Along the way, simple quantitative arguments — geometric scaling, diffusion, mass action and thermodynamics — explain *why* cells look and behave the way they do.

## 1. The Cell Theory

- **1665:** Robert Hooke observed "cells" in cork with an early compound microscope and described them in *Micrographia* (naming them after small rooms, Latin *cella*, like those of monks).
- **1670s:** Antonie van Leeuwenhoek, using superb single-lens microscopes, observed living bacteria, protists, sperm and blood cells ("animalcules").
- **1838–1839:** Matthias Schleiden (plants) and Theodor Schwann (animals) proposed that all organisms are made of cells.
- **1855:** Rudolf Virchow popularized *omnis cellula e cellula* — "every cell from a cell" — building on Robert Remak's observations of dividing cells in embryos (1852).

**Modern cell theory:**
1. All living organisms are composed of one or more cells.
2. The cell is the basic unit of structure and function.
3. All cells arise from pre-existing cells by division.
4. Cells contain hereditary information (DNA) passed on during division.
5. All cells have basically the same chemical composition and metabolic processes.

The third tenet was not obvious in the 19th century: many people believed microbes arose spontaneously in broth. Louis Pasteur's swan-neck flask experiments (1859–1862) showed that boiled broth stays sterile indefinitely if airborne particles cannot reach it, even though air itself can. Cells come only from cells.

### Why are cells small? Surface area, volume and diffusion

Two physical constraints set the size of most cells: everything a cell imports or exports must cross its surface, and inside the cell, molecules move largely by diffusion, which is fast over short distances and hopelessly slow over long ones.

**Derivation 1 — the surface-area-to-volume ratio.** For a spherical cell of radius $r$,
$$A = 4\pi r^2,\qquad V = \tfrac{4}{3}\pi r^3,\qquad \frac{A}{V} = \frac{3}{r}$$
The result does not depend on the shape being a sphere. Any shape scaled by a linear size $L$ has area $A = aL^2$ and volume $V = bL^3$, where $a$ and $b$ are constants fixed by the shape, so $A/V = (a/b)/L$. Whatever the shape, the ratio falls inversely with size.

Now suppose a nutrient (say oxygen) can enter through the membrane at a maximum flux $J$ (moles per unit area per second) and is consumed throughout the cytoplasm at a rate $q$ (moles per unit volume per second). Supply keeps up with demand only if
$$J\cdot 4\pi r^2 \;\ge\; q\cdot \tfrac{4}{3}\pi r^3 \quad\Longrightarrow\quad r \;\le\; \frac{3J}{q}$$
For a given transport capacity and metabolic rate there is therefore a maximum radius. Cells that exceed typical sizes escape this limit in recognizable ways: they become flat or thin (red blood cells, squamous epithelial cells), long and narrow (neurons, muscle fibers), fold their membranes to add surface (microvilli of intestinal cells, the cristae of mitochondria), fill most of their volume with metabolically inert material (yolk-laden eggs, the central vacuole of plant cells), or contain many nuclei (skeletal muscle fibers, the giant alga *Caulerpa*).

**Worked Example 1.1 — Comparing a bacterium with an animal cell.** Treat a bacterium as a sphere 1 μm in diameter and a liver cell as a sphere 20 μm in diameter. Compare their surface-area-to-volume ratios.
1. Bacterium: $r = 0.5\ \mu\text{m}$, so $A/V = 3/0.5 = 6\ \mu\text{m}^{-1}$.
2. Liver cell: $r = 10\ \mu\text{m}$, so $A/V = 3/10 = 0.3\ \mu\text{m}^{-1}$.
3. Ratio: $6/0.3 = 20$, the same as the ratio of the diameters, exactly as $A/V \propto 1/r$ predicts.
4. If the liver cell doubled its diameter to 40 μm, its volume would rise by $2^3 = 8$ but its surface only by $2^2 = 4$, halving $A/V$ to $0.15\ \mu\text{m}^{-1}$.

**Answer:** each cubic micrometre of the bacterium is served by 20 times more membrane than a cubic micrometre of the liver cell. This is one reason bacteria can import nutrients, grow and divide so quickly.

**Derivation 2 — how far does diffusion reach?** Model a molecule as a random walker that steps a distance $\ell$ to the left or right every $\tau$ seconds, each direction equally likely. If $x_N$ is its position after $N$ steps, then $x_N = x_{N-1} \pm \ell$ and
$$x_N^2 = x_{N-1}^2 \pm 2\ell\,x_{N-1} + \ell^2$$
Averaging over many walkers, the middle term vanishes because the sign of the next step is independent of where the walker already is. Hence $\langle x_N^2\rangle = \langle x_{N-1}^2\rangle + \ell^2$, and starting from $x_0 = 0$, $\langle x_N^2\rangle = N\ell^2$. With $N = t/\tau$ steps in time $t$,
$$\langle x^2\rangle = \frac{\ell^2}{\tau}\,t \equiv 2Dt, \qquad D = \frac{\ell^2}{2\tau}$$
which defines the **diffusion coefficient** $D$. In three dimensions each coordinate wanders independently, so $\langle r^2\rangle = 6Dt$. The practical rule is that the typical time to diffuse a distance $x$ is
$$t \approx \frac{x^2}{2D}$$
Time grows with the *square* of distance: going 10 times farther takes 100 times longer. Albert Einstein derived this relation in 1905 to explain Brownian motion — the jittering of tiny particles first studied systematically by the botanist Robert Brown in 1827 — and Jean Perrin's measurements of it (Nobel Prize in Physics 1926) helped convince physicists that atoms are real.

**Worked Example 1.2 — Diffusion versus motor transport.** A typical small protein in cytoplasm has $D \approx 10\ \mu\text{m}^2\,\text{s}^{-1}$. Estimate how long it takes to diffuse (a) across a bacterium 1 μm wide, (b) across an animal cell 20 μm wide, and (c) down a motor-neuron axon 1 m long.
1. Bacterium: $t = (1\ \mu\text{m})^2/(2\times10\ \mu\text{m}^2\,\text{s}^{-1}) = 0.05$ s.
2. Animal cell: $t = 20^2/20 = 400/20 = 20$ s.
3. Axon: $x = 1\ \text{m} = 10^6\ \mu\text{m}$, so $t = (10^6)^2/20 = 5\times10^{10}$ s. Dividing by $3.156\times10^7$ s per year gives about 1600 years.
4. Compare active transport: kinesin motors carry vesicles along axonal microtubules at roughly 200–400 mm per day ("fast axonal transport"), covering 1 m in $1000/400 = 2.5$ to $1000/200 = 5$ days.

**Answer:** (a) 0.05 s, (b) about 20 s, (c) about 1600 years. Diffusion is perfectly adequate inside a bacterium, workable inside an animal cell, and useless along a long axon — which is why large eukaryotic cells depend on a cytoskeleton and motor proteins.

There is also a *lower* limit on size. A cell must hold a genome, the ribosomes and enzymes to express it, and a membrane to enclose them. The smallest known cells, such as mycoplasmas (about 0.2–0.3 μm across), approach this limit.

**Table: sizes of biological objects**

| Object | Typical size |
|---|---|
| Lipid bilayer (thickness) | ~5 nm (up to ~10 nm with proteins and sugars) |
| Globular protein (e.g. hemoglobin) | ~5 nm |
| Ribosome | ~20–30 nm |
| Microtubule (diameter) | ~25 nm |
| Influenza virus or SARS-CoV-2 particle | ~100 nm |
| Mycoplasma (smallest cells) | 0.2–0.3 μm |
| *Escherichia coli* | ~1 μm wide, ~2 μm long |
| Mitochondrion | 0.5–1 μm wide, 1 to several μm long |
| Nucleus of a typical animal cell | ~5–10 μm |
| Human red blood cell | ~7.5–8 μm across, ~2 μm thick |
| Typical animal cell | 10–30 μm |
| Typical plant cell | 10–100 μm |
| Human oocyte (egg cell) | ~0.1 mm, just visible to the naked eye |
| *Thiomargarita magnifica* (largest known bacterium, described 2022) | ~1 cm long |
| Axon of a human motor neuron | up to ~1 m |

Other exceptions include the yolk of an unfertilized bird's egg (a single, food-laden cell several centimetres across in an ostrich) and siphonous algae such as *Caulerpa*, whose single multinucleate cell can grow to tens of centimetres or more. Cell *number*, not cell size, accounts for most differences in body size: an elephant's liver cells are not much bigger than a mouse's. By number, red blood cells dominate the human body — a 2016 estimate by Ron Sender, Shai Fuchs and Ron Milo put them at about 25 trillion of the roughly 30 trillion human cells in a reference adult, around 84%.

## 2. Microscopy

| Technique | Resolution | Notes |
|---|---|---|
| Human eye | ~0.1 mm | |
| Light microscope | ~200 nm (diffraction limit) | Living cells; staining; phase contrast |
| Fluorescence / confocal | ~200 nm | Specific labeling (GFP — Shimomura, Chalfie, Tsien, Nobel Chemistry 2008); confocal optics reject out-of-focus light for optical sectioning |
| Super-resolution (STED, PALM/STORM) | ~20 nm | Betzig, Hell, Moerner, Nobel Chemistry 2014 |
| Transmission electron microscope (TEM) | ~0.1–0.2 nm instrumental; typically ~1–2 nm in stained biological sections | Thin sections; internal structure; specimens dead and in vacuum |
| Scanning electron microscope (SEM) | ~1–5 nm | Surface topography in 3D |
| Cryo-electron microscopy/tomography | Near-atomic for purified molecules | Macromolecular structures in situ; Dubochet, Frank, Henderson, Nobel Chemistry 2017 |

### Magnification is not resolution

**Magnification** is how much larger the image is than the object; **resolution** is the smallest separation at which two points can still be distinguished as two. A microscope can magnify a blurry image indefinitely, but beyond roughly 500–1000 times the numerical aperture of the objective, further magnification reveals no new detail ("empty magnification"). Resolution is limited by the wave nature of light.

### Derivation: the Abbe diffraction limit

Ernst Abbe (1873) analyzed image formation by treating the specimen as a fine grating with period $d$. Light of wavelength $\lambda$ passing through a medium of refractive index $n$ is diffracted into discrete orders at angles $\theta_m$ given by
$$n\,d\,(\sin\theta_m - \sin\theta_0) = m\lambda$$
where $\theta_0$ is the direction of the illuminating light. Abbe's insight was that the objective can reproduce the periodic structure only if it collects at least two of these orders (for example the undiffracted order $m = 0$ and the first order $m = 1$), because the image is formed by their interference. An objective accepts rays up to a half-angle $\alpha$ from the axis. With oblique illumination, the undiffracted beam can enter at one edge of the aperture ($\theta_0 = -\alpha$) while the first order enters at the opposite edge ($\theta_1 = +\alpha$). Substituting,
$$n\,d\,(2\sin\alpha) = \lambda \quad\Longrightarrow\quad d_{\min} = \frac{\lambda}{2\,n\sin\alpha} = \frac{\lambda}{2\,\text{NA}}$$
where $\text{NA} = n\sin\alpha$ is the **numerical aperture**. Since $\sin\alpha < 1$ and the best immersion oils have $n \approx 1.5$, practical objectives reach $\text{NA} \approx 1.4$. An alternative criterion for two point sources (Rayleigh's) gives $d = 0.61\lambda/\text{NA}$; the two differ by a modest numerical factor and both say the same thing: resolution is about half the wavelength.

**Worked Example 2.1 — The best a light microscope can do.** A cell expresses green fluorescent protein, which emits at about 510 nm, and is imaged with an oil-immersion objective of NA 1.4. What is the resolution limit? How does it compare with a low-power dry objective (NA 0.25) in 550 nm light?
1. Abbe limit: $d = 510\ \text{nm}/(2\times1.4) = 182$ nm.
2. Rayleigh criterion: $d = 0.61\times510/1.4 = 222$ nm.
3. Low-power objective: $d = 550/(2\times0.25) = 1100$ nm $= 1.1\ \mu$m.
4. Compare with structures: a mitochondrion (0.5–1 μm wide) is resolvable; a ribosome (~25 nm) or the internal structure of a microtubule (25 nm) is not.

**Answer:** about 0.18–0.22 μm with the best objective, but about 1.1 μm with the low-power one. Note that *detection* is different from *resolution*: a single fluorescently labelled microtubule is easily seen, but it appears as a blurred line about 200 nm wide, and two microtubules closer than that merge into one.

**Worked Example 2.2 — Why electrons do better.** Find the de Broglie wavelength of electrons accelerated through 300 kV in a cryo-electron microscope.
1. Kinetic energy: $K = eV = 300$ keV. The electron rest energy is $m_ec^2 = 511$ keV, comparable to $K$, so relativity matters.
2. The relativistic momentum follows from $E^2 = (pc)^2 + (m_ec^2)^2$ with $E = K + m_ec^2$, which rearranges to $p = \sqrt{2m_eK\,(1 + K/2m_ec^2)}$.
3. With $h = 6.626\times10^{-34}$ J s, $m_e = 9.109\times10^{-31}$ kg and $K = 300\times10^3\times1.602\times10^{-19}$ J, $\lambda = h/p = 1.97\times10^{-12}$ m $= 1.97$ pm. (The non-relativistic formula would give 2.24 pm, about 14% too large.)
4. Compared with green light: $550\ \text{nm}/1.97\ \text{pm} \approx 2.8\times10^5$.

**Answer:** $\lambda \approx 1.97$ pm, about 280 000 times shorter than visible light. Yet practical resolution in biology is far worse than the wavelength, because magnetic lenses have large aberrations (forcing small apertures) and because biological specimens are destroyed by the electron dose needed for a sharp image. Cryo-EM sidesteps radiation damage by averaging images of many thousands of identical frozen molecules; in 2020 it reached about 0.12 nm resolution for a very well-behaved test protein (apoferritin).

### Seeing living cells, and taking them apart

- **Contrast methods.** Unstained cells are nearly transparent, but they shift the phase of light passing through them. Frits Zernike's **phase-contrast** microscope (developed in the 1930s; Nobel Prize in Physics 1953) converts these phase shifts into brightness differences, so living cells can be watched without killing and staining them. Differential interference contrast (DIC) works on a related principle.
- **Fluorescent labels.** Antibodies tagged with dyes (immunofluorescence) or genetically encoded fluorescent proteins such as GFP mark specific molecules, so their location and movement can be followed in living cells.
- **Cell fractionation.** Cells are broken open and their contents separated by **differential centrifugation**: nuclei sediment at low speed, then mitochondria and lysosomes, then microsomes (fragments of ER), then ribosomes at the highest speeds. Albert Claude, Christian de Duve and George Palade used fractionation and electron microscopy to map the cell's organelles (Nobel Prize in Physiology or Medicine 1974).

The speed at which a particle sediments per unit centrifugal acceleration is its **sedimentation coefficient**,
$$s = \frac{v}{\omega^2 r} = \frac{m\,(1 - \bar v\rho)}{f}$$
where $v$ is the sedimentation velocity, $\omega$ the angular speed, $r$ the distance from the axis, $m$ the particle mass, $\bar v$ its partial specific volume, $\rho$ the solvent density and $f$ its frictional coefficient. It is measured in **svedbergs** (1 S $= 10^{-13}$ s), after Theodor Svedberg, who built the analytical ultracentrifuge (Nobel Chemistry 1926). Because $f$ grows with particle size — for a compact sphere $f = 6\pi\eta R$ with $R \propto m^{1/3}$, so $s \propto m^{2/3}$ — sedimentation coefficients are *not* additive. Doubling the mass of a sphere multiplies $s$ by only $2^{2/3} \approx 1.59$. That is why a 50S and a 30S ribosomal subunit combine into a 70S ribosome, not an "80S" one.

## 3. Prokaryotic vs. Eukaryotic Cells

| Feature | Prokaryotes (Bacteria, Archaea) | Eukaryotes (animals, plants, fungi, protists) |
|---|---|---|
| Nucleus | None; DNA in a nucleoid region | Membrane-bound nucleus |
| DNA | Usually one circular chromosome; plasmids | Multiple linear chromosomes with histones |
| Size | Mostly 0.2–5 μm | Mostly 10–100 μm |
| Membrane-bound organelles | Absent (some have protein-shelled microcompartments such as carboxysomes) | Present (ER, Golgi, mitochondria, etc.) |
| Ribosomes | 70S (50S + 30S) | 80S in cytosol (60S + 40S); bacterial-type ribosomes in mitochondria and chloroplasts (mammalian mitochondrial ribosomes sediment at about 55S) |
| Cell wall | Usually (peptidoglycan in bacteria) | Plants (cellulose), fungi (chitin); animals none |
| Cell division | Binary fission | Mitosis/meiosis |
| Cytoskeleton | Simple homologs (FtsZ, MreB) | Elaborate (microtubules, actin, intermediate filaments) |
| Flagella | Rotary motor, flagellin, driven by proton (or sodium) flow | Microtubule-based (9+2), ATP-driven whipping |
| Transcription/translation | Coupled in cytoplasm | Separated (nucleus vs. cytoplasm) |
| Origin | ~3.5–4 billion years ago | ~1.8–2 billion years ago |

**Three domains of life** (Carl Woese and George Fox, 1977; formally proposed by Woese and colleagues in 1990, from ribosomal RNA sequences): **Bacteria**, **Archaea** (often extremophiles — thermophiles, halophiles, methanogens — but also common in soils and oceans; their membranes use ether-linked lipids), and **Eukarya**. Archaea are more closely related to eukaryotes than to bacteria in their information-processing machinery; current evidence suggests eukaryotes arose from within the Archaea (Asgard archaea) after acquiring a bacterial endosymbiont.

**Bacterial features:** Gram-positive bacteria have a thick peptidoglycan wall (stain purple); Gram-negative bacteria have a thin wall plus an outer membrane with lipopolysaccharide (stain pink; generally more antibiotic-resistant). The stain was devised by Hans Christian Gram in 1884 and remains the first test applied to many clinical samples. Some bacteria have capsules, pili (attachment, conjugation), or endospores (extremely resistant dormant forms, e.g. *Bacillus anthracis*, *Clostridium botulinum*).

### What is a bacterial cell made of?

A growing *E. coli* cell weighs about 1 pg ($10^{-15}$ kg) and is roughly 70% water. Its dry mass is dominated by protein and by the RNA of its ribosomes.

| Component | Share of dry mass (%) | Comment |
|---|---|---|
| Protein | 55.0 | Several thousand different kinds |
| RNA | 20.5 | Mostly ribosomal RNA; tRNA and a small share of mRNA |
| Lipid | 9.1 | Inner and outer membranes |
| Small metabolites, cofactors, ions | 3.9 | |
| Lipopolysaccharide | 3.4 | Outer leaflet of the outer membrane |
| DNA | 3.1 | One chromosome of about 4.6 million base pairs |
| Peptidoglycan (murein) | 2.5 | Cell wall |
| Glycogen | 2.5 | Carbon store |

*Values for* E. coli *growing in glucose minimal medium at 37 °C, after the classic compilation by Frederick Neidhardt and colleagues.*

The cytoplasm is crowded: macromolecules reach roughly 300–400 g per litre, so the interior of a cell behaves more like a dense gel than a dilute solution. Crowding speeds up some binding reactions and slows diffusion of large molecules.

**Worked Example 3.1 — How many molecules is "one nanomolar"?** An *E. coli* cell has a volume of about 1 fL ($1\ \mu\text{m}^3 = 10^{-15}$ L). How many molecules of a protein present at 1 nM does it contain, and what concentration corresponds to a single molecule?
1. Number of molecules: $N = cVN_A = (10^{-9}\ \text{mol L}^{-1})(10^{-15}\ \text{L})(6.022\times10^{23}\ \text{mol}^{-1}) = 0.60$.
2. One molecule: $c = 1/(N_AV) = 1/(6.022\times10^{23}\times10^{-15}) = 1.66\times10^{-9}$ M $= 1.66$ nM.

**Answer:** about 0.6 molecules — in other words, in a bacterium, 1 nM means "roughly one molecule per cell", and a single molecule is a 1.7 nM solution. Many regulatory proteins are present at only a handful of copies (the *lac* repressor famously numbers about ten per cell), so random fluctuations in their numbers make gene expression noisy, and identical cells in identical environments can behave differently.

## 4. Eukaryotic Organelles

### Plasma membrane

**Structure.** The plasma membrane is a phospholipid bilayer (~5–10 nm thick including head groups and proteins) with embedded proteins, cholesterol and glycolipids. Phospholipids are **amphipathic**: a polar head and two hydrophobic fatty-acid tails. In water they assemble spontaneously into bilayers, because burying the tails away from water lets water molecules form more hydrogen bonds with one another (the **hydrophobic effect**) — the bilayer is held together by the entropy of the surrounding water, not by covalent bonds.

**The fluid mosaic model** (S. Jonathan Singer and Garth Nicolson, 1972) describes the membrane as a two-dimensional fluid in which lipids and many proteins drift laterally. A key experiment came two years earlier: L. David Frye and Michael Edidin (1970) fused mouse and human cells and labelled each species' surface proteins with differently colored fluorescent antibodies; within about 40 minutes at 37 °C the two colors had intermixed over the hybrid cell surface. Membrane properties:
- **Fluidity** rises with unsaturated (kinked) fatty-acid tails and falls with long saturated tails. Cholesterol acts as a buffer, stiffening fluid membranes and preventing tight packing in cold ones. Bacteria, plants and cold-blooded animals adjust their lipid composition when the temperature changes (homeoviscous adaptation).
- **Asymmetry:** the two leaflets differ. Phosphatidylserine is normally kept on the inner leaflet; its appearance on the outer surface is an "eat me" signal on apoptotic cells. Glycolipids and glycoproteins face outward, forming the sugar coat (**glycocalyx**) that includes markers such as the ABO blood-group antigens.
- **Selective permeability:** small nonpolar molecules (O₂, CO₂, N₂, steroid hormones) cross easily; small uncharged polar molecules (water, urea, ethanol) cross more slowly; large polar molecules (glucose) and all ions are essentially blocked by the hydrocarbon core and need proteins to cross.

| Transport mechanism | Energy source | Direction | Examples |
|---|---|---|---|
| Simple diffusion | None | Down the concentration gradient | O₂, CO₂, steroid hormones |
| Channel-mediated (facilitated) diffusion | None | Down the electrochemical gradient | Aquaporins (Peter Agre), K⁺ channels (Roderick MacKinnon) — Nobel Chemistry 2003 |
| Carrier-mediated facilitated diffusion | None | Down the gradient; saturable | GLUT glucose transporters |
| Primary active transport | ATP hydrolysis | Against the gradient | Na⁺/K⁺-ATPase (Jens Skou, Nobel Chemistry 1997); Ca²⁺-ATPase; H⁺-ATPases |
| Secondary active transport | A pre-existing ion gradient | One solute against its gradient | SGLT1 Na⁺–glucose symporter in the gut; Na⁺/Ca²⁺ exchanger |
| Endocytosis / exocytosis | ATP and GTP | Bulk transport in vesicles | Receptor-mediated uptake of LDL (Brown and Goldstein, Nobel 1985); neurotransmitter release |

Channels are pores that open and close (gated by voltage, ligands or stretch) and can pass up to about $10^8$ ions per second. Carriers bind their cargo and change shape, so they are slower (typically $10^2$–$10^4$ molecules per second) and, like enzymes, they **saturate**: the transport rate approaches a maximum as the solute concentration rises. The **Na⁺/K⁺-ATPase** pumps 3 Na⁺ out and 2 K⁺ in per ATP hydrolyzed, and it consumes a large share of a resting animal cell's ATP — a larger share still in nerve cells. The Na⁺ gradient it creates powers secondary active transport, such as the uptake of glucose from the gut against its concentration gradient.

#### Osmosis and tonicity

**Osmosis** is the net movement of water across a semipermeable membrane toward the side with the higher concentration of solute particles. The pressure that would have to be applied to stop it is the **osmotic pressure** $\Pi$.

*Derivation (van 't Hoff's law).* Water moves until its chemical potential is equal on both sides. For water in a solution where its mole fraction is $x_w$, under an extra pressure $\Pi$,
$$\mu_w = \mu_w^\circ + RT\ln x_w + \bar V_w\,\Pi$$
where $\bar V_w$ is the molar volume of water. If the other side is pure water at zero extra pressure ($\mu_w = \mu_w^\circ$), equilibrium requires $RT\ln x_w + \bar V_w\Pi = 0$. For a dilute solution, $\ln x_w = \ln(1 - x_s) \approx -x_s \approx -n_s/n_w$, where $n_s$ and $n_w$ are the moles of solute and water, and $n_w\bar V_w \approx V$, the volume of solution. Therefore
$$\Pi = \frac{n_sRT}{V} = cRT$$
— formally identical to the ideal-gas law. Jacobus van 't Hoff found this relation in 1887 and received the first Nobel Prize in Chemistry (1901). For solutes that dissociate, $c$ is the total concentration of particles, the **osmolarity** ($c = i\,c_{\text{formal}}$, with $i \approx 2$ for NaCl).

**Worked Example 4.1 — Why intravenous saline is 0.9% NaCl.** Calculate the osmolarity and the ideal osmotic pressure (relative to pure water) of 0.9% (w/v) NaCl at body temperature, 37 °C.
1. Concentration: 0.9 g per 100 mL $= 9.0$ g/L. With $M(\text{NaCl}) = 58.44$ g/mol, $c = 9.0/58.44 = 0.154$ mol/L.
2. Each formula unit gives two ions, so the ideal osmolarity is $2\times0.154 = 0.308$ osmol/L $= 308$ osmol/m³.
3. Osmotic pressure: $\Pi = cRT = 308\times8.314\times310.15 = 7.94\times10^5$ Pa $\approx 7.9$ bar.
4. Correction for non-ideality: Na⁺ and Cl⁻ attract one another, so the solution behaves as if it had about 93% of the ideal particle count (osmotic coefficient ~0.93): $0.93\times0.308 = 0.286$ osmol/L, which matches blood plasma (about 275–295 mOsm/kg).

**Answer:** about 0.29–0.31 osmol/L, roughly isotonic with blood. A red blood cell dropped into pure water instead faces an osmotic pressure difference of nearly 8 bar — about eight atmospheres — far more than its thin membrane can resist, so it swells and bursts (**hemolysis**).

**Tonicity** describes what a solution does to a cell's volume, and it depends only on solutes that *cannot* cross the membrane:
- In a **hypotonic** solution, water enters: animal cells swell and may lyse; plant cells become **turgid**, pressing against their walls, which is their healthy state (wilting is the loss of turgor). Freshwater protists bail out the incoming water with **contractile vacuoles**.
- In a **hypertonic** solution, water leaves: red cells shrivel (**crenation**); plant cells undergo **plasmolysis**, the membrane pulling away from the wall.
- In an **isotonic** solution there is no net water movement.

A solution can be *isosmotic* but *hypotonic*: 0.3 M urea has about the same osmolarity as cytoplasm, but urea slowly crosses the membrane, water follows it in, and red cells placed in it eventually burst. **Aquaporin** water channels, discovered by Peter Agre in 1992, make some membranes (kidney tubules, red cells) far more water-permeable than a pure lipid bilayer.

#### Ion gradients and the membrane potential

Pumps and channels maintain very different ion concentrations inside and outside the cell. Representative values for a mammalian cell are below; the last column gives the **equilibrium (Nernst) potential** calculated at 37 °C for the representative concentrations shown in brackets.

| Ion | Inside (mM) | Outside (mM) | Equilibrium potential at 37 °C |
|---|---|---|---|
| K⁺ | ~140 | ~5 | about −89 mV [140 in, 5 out] |
| Na⁺ | 5–15 | ~145 | about +67 mV [12 in, 145 out] |
| Cl⁻ | 5–15 | ~110 | about −64 mV [10 in, 110 out] |
| Ca²⁺ | ~0.0001 (100 nM free) | 1–2 | about +128 mV [0.0001 in, 1.5 out] |

*Derivation of the Nernst equation.* The electrochemical potential of an ion with charge $z$ is $\tilde\mu = \mu^\circ + RT\ln c + zF\psi$, where $\psi$ is the electrical potential and $F = 96\,485$ C/mol is the Faraday constant. The ion is at equilibrium across the membrane when $\tilde\mu_{\text{in}} = \tilde\mu_{\text{out}}$:
$$RT\ln c_{\text{in}} + zF\psi_{\text{in}} = RT\ln c_{\text{out}} + zF\psi_{\text{out}}$$
Solving for the membrane potential $E = \psi_{\text{in}} - \psi_{\text{out}}$:
$$E_X = \frac{RT}{zF}\ln\frac{c_{\text{out}}}{c_{\text{in}}}$$
At 37 °C, $RT/F = 26.7$ mV and $2.303RT/F = 61.5$ mV. For K⁺: $E_K = 26.7\ \text{mV}\times\ln(5/140) = -89$ mV. The resting potential of most animal cells (−60 to −90 mV) lies close to $E_K$ because the resting membrane is most permeable to K⁺. How neurons exploit the Na⁺ and K⁺ gradients to fire action potentials is covered in the physiology chapter.

**Worked Example 4.2 — How many ions does it take to charge a membrane?** A spherical cell 20 μm in diameter has a resting potential of −70 mV. Biological membranes have a specific capacitance of about $1\ \mu\text{F cm}^{-2}$. How many excess ions sit at the membrane surface, and what fraction is this of the cell's K⁺ (140 mM)?
1. Charge per unit area: $Q/A = CV = (1\times10^{-6}\ \text{F cm}^{-2})(0.070\ \text{V}) = 7.0\times10^{-8}$ C cm⁻².
2. Ions per cm² (monovalent, $e = 1.602\times10^{-19}$ C): $7.0\times10^{-8}/1.602\times10^{-19} = 4.4\times10^{11}$.
3. Cell surface: $A = 4\pi(10\ \mu\text{m})^2 = 4\pi(10^{-3}\ \text{cm})^2 = 1.26\times10^{-5}$ cm².
4. Excess ions: $4.4\times10^{11}\times1.26\times10^{-5} = 5.5\times10^6$.
5. Cell volume: $\tfrac{4}{3}\pi(10\ \mu\text{m})^3 = 4189\ \mu\text{m}^3 = 4.19\times10^{-12}$ L. K⁺ ions: $0.140\times4.19\times10^{-12}\times6.022\times10^{23} = 3.5\times10^{11}$.
6. Fraction: $5.5\times10^6/3.5\times10^{11} = 1.6\times10^{-5}$.

**Answer:** about 5.5 million ions, only about 16 parts per million of the cell's potassium. The bulk cytoplasm stays electrically neutral; the membrane potential comes from a vanishingly thin layer of separated charge at the two membrane surfaces. This is also why an action potential, which moves a similarly tiny amount of charge, barely changes ion concentrations — and why the membrane capacitance is nearly the same in all cells: the dielectric is always a hydrocarbon layer a few nanometres thick.

### Nucleus
- Contains most of the cell's DNA, organized with histone proteins as **chromatin** (euchromatin: loosely packed, actively transcribed; heterochromatin: densely packed, mostly silent). The basic packing unit is the **nucleosome** (described by Roger Kornberg in 1974): about 147 base pairs of DNA wrapped roughly 1.7 times around an octamer of histones (two each of H2A, H2B, H3 and H4), separated by short linker DNA.
- Enclosed by the **nuclear envelope** (double membrane, continuous with the ER) perforated by **nuclear pores** (large protein complexes regulating traffic of mRNA, proteins and ribosomal subunits). Small molecules and proteins below roughly 40 kDa diffuse through; larger proteins need a **nuclear localization signal** recognized by importin receptors, with the direction of transport set by the small GTPase Ran.
- The **nucleolus** is where ribosomal RNA is transcribed and ribosomal subunits are assembled.
- Supported by the nuclear lamina (lamin intermediate filaments); mutations in lamin A cause Hutchinson–Gilford progeria.

**Worked Example 4.3 — Packing two metres of DNA.** A human diploid cell contains about $6.2\times10^9$ base pairs of DNA (two copies of a genome of about $3.1\times10^9$ bp) in 46 chromosomes, inside a nucleus about 6 μm across. In B-form DNA, successive base pairs are 0.34 nm apart. Find the total length of DNA, its ratio to the nuclear diameter, the approximate number of nucleosomes, and the average compaction of a mitotic chromosome about 5 μm long.
1. Total length: $6.2\times10^9\times0.34\times10^{-9}\ \text{m} = 2.1$ m.
2. Ratio to nuclear diameter: $2.1\ \text{m}/6\times10^{-6}\ \text{m} = 3.5\times10^5$.
3. With one nucleosome per ~200 bp (147 bp core plus linker): $6.2\times10^9/200 = 3.1\times10^7$ nucleosomes.
4. Average chromosome: $2.1\ \text{m}/46 = 4.6$ cm of DNA, condensed to about 5 μm at metaphase: $4.6\times10^{-2}/5\times10^{-6} \approx 9\times10^3$.

**Answer:** about 2 m of DNA, some 350 000 times longer than the nucleus is wide, wound on about 30 million nucleosomes and compacted roughly ten-thousand-fold in mitotic chromosomes. By contrast, the 4.6-million-bp *E. coli* chromosome is about 1.6 mm long — some 800 times the length of the cell — and is compacted by supercoiling and nucleoid-associated proteins rather than by histones.

### Ribosomes
Molecular machines that synthesize proteins (made of rRNA and proteins). **Free ribosomes** in the cytosol make proteins for the cytosol, nucleus, mitochondria and peroxisomes; **bound ribosomes** on the rough ER make secreted, membrane and lysosomal proteins. Several ribosomes often translate the same mRNA simultaneously, forming a **polysome**. Atomic structures solved around 2000 showed that the catalytic site that forms peptide bonds is made entirely of RNA — the ribosome is a **ribozyme**, a strong hint that RNA preceded proteins in early evolution. Structural studies of the ribosome earned the 2009 Nobel Prize in Chemistry (Ramakrishnan, Steitz, Yonath). Many antibiotics (tetracyclines and aminoglycosides acting on the 30S subunit; macrolides and chloramphenicol acting on the 50S subunit) target bacterial 70S ribosomes selectively.

### Endomembrane system
- **Rough endoplasmic reticulum (RER):** studded with ribosomes; proteins are translocated into the lumen, folded (with chaperones), disulfide-bonded and glycosylated. Quality control: misfolded proteins are retained and degraded, and their accumulation triggers the unfolded protein response.
- **The signal hypothesis.** How does a ribosome know to dock on the ER? Günter Blobel and colleagues showed in the 1970s that secreted proteins begin with a short hydrophobic **signal sequence**. As it emerges from the ribosome, it is bound by the signal recognition particle (SRP), which halts translation and guides the ribosome to a receptor and protein-conducting channel (translocon) in the ER membrane; the signal is usually cleaved off in the lumen. Other "zip codes" direct proteins to mitochondria, the nucleus and peroxisomes (Blobel, Nobel 1999).
- **Smooth ER (SER):** lipid and steroid synthesis; detoxification of drugs and toxins (abundant in liver cells — cytochrome P450 enzymes); Ca²⁺ storage (sarcoplasmic reticulum in muscle).
- **Golgi apparatus:** stacks of flattened cisternae (cis face receives, trans face ships). Modifies (glycosylation, sulfation, phosphorylation), sorts and packages proteins into vesicles for secretion, the plasma membrane or lysosomes. Camillo Golgi described it with his silver-staining "black reaction" in 1898. Lysosomal enzymes are tagged in the cis-Golgi with **mannose-6-phosphate**, which receptors in the trans-Golgi recognize; without the tagging enzyme (I-cell disease) the hydrolases are secreted instead of delivered to lysosomes.
- **Lysosomes:** acidic (pH ~4.5–5) vesicles with about 50 different hydrolytic enzymes for digesting macromolecules, worn-out organelles (**autophagy** — Yoshinori Ohsumi, Nobel 2016) and engulfed material (phagocytosis). Their enzymes work best at acidic pH, which protects the cell if a lysosome leaks into the neutral cytosol. Christian de Duve discovered lysosomes in 1955 through cell fractionation. Lysosomal storage diseases (Tay–Sachs, Pompe, Gaucher) result from missing enzymes. Plant cells have a large **central vacuole** with similar functions plus storage and turgor pressure.
- **Vesicular transport:** coated vesicles (clathrin, COPI, COPII) shuttle cargo; SNARE proteins mediate fusion with target membranes (Rothman, Schekman, Südhof, Nobel 2013).

The route through this system was traced by George Palade and James Jamieson in the 1960s with a **pulse–chase** experiment: pancreatic cells were given a brief pulse of radioactive amino acids, then a "chase" of unlabelled ones, and autoradiography of electron micrographs showed the labelled proteins moving in sequence from the rough ER to the Golgi, then into secretory granules and finally out of the cell.

### Mitochondria
- The "powerhouses of the cell": site of the citric acid cycle (Hans Krebs, 1937), fatty-acid oxidation and oxidative phosphorylation, producing most of the ATP in aerobic cells.
- Double membrane: outer membrane (permeable via porins) and highly folded inner membrane (**cristae**) containing the electron transport chain and ATP synthase; inner space called the **matrix**.
- Contain their own circular DNA (mtDNA, 16 569 bp in humans, encoding 37 genes: 13 proteins of the respiratory chain and ATP synthase, 22 tRNAs and 2 rRNAs) and bacterial-type ribosomes; replicate by fission; inherited maternally.
- Also regulate apoptosis (releasing cytochrome c), calcium signaling, heat production (brown fat uncoupling protein UCP1), and heme and steroid synthesis.
- Numbers vary: from none (mature red blood cells) to thousands (heart muscle, liver cells).
- Mitochondrial diseases arise from mutations in mtDNA or nuclear genes; "three-parent" mitochondrial replacement therapy has been used to prevent transmission.

#### Chemiosmosis: how mitochondria make ATP

Peter Mitchell proposed in 1961 that the electron transport chain does not make ATP directly. Instead, as electrons flow from NADH to O₂, complexes I, III and IV pump protons from the matrix into the intermembrane space, storing energy in an electrochemical proton gradient, and **ATP synthase** lets protons flow back, using their energy to make ATP from ADP and phosphate. The idea was controversial for years; Mitchell received the Nobel Prize in Chemistry in 1978. ATP synthase is a genuine rotary motor: proton flow turns a ring of c-subunits and a central stalk, and the rotating stalk cycles each of three catalytic sites through binding, synthesis and release (Paul Boyer's binding-change mechanism; structure by John Walker; Nobel Chemistry 1997). Rotation was filmed directly in 1997 by attaching a fluorescent actin filament to the motor.

*Derivation — the proton-motive force.* Moving one mole of H⁺ from the intermembrane space ("out") into the matrix ("in") changes the free energy by a concentration term plus an electrical term:
$$\Delta G = RT\ln\frac{[\text{H}^+]_{\text{in}}}{[\text{H}^+]_{\text{out}}} + F\,(\psi_{\text{in}} - \psi_{\text{out}})$$
The matrix is alkaline and negative. Writing $\Delta\text{pH} = \text{pH}_{\text{in}} - \text{pH}_{\text{out}} > 0$ and $\Delta\psi$ for the magnitude of the membrane potential, $\ln([\text{H}^+]_{\text{in}}/[\text{H}^+]_{\text{out}}) = -2.303\,\Delta\text{pH}$ and $\psi_{\text{in}} - \psi_{\text{out}} = -\Delta\psi$. The energy released per mole of protons entering is therefore
$$-\Delta G = F\,\Delta p, \qquad \Delta p = \Delta\psi + \frac{2.303\,RT}{F}\,\Delta\text{pH}$$
where $\Delta p$ is the **proton-motive force**, expressed in volts.

**Worked Example 4.4 — How many protons per ATP?** In respiring mitochondria at 37 °C, take a membrane potential of 150 mV (matrix negative) and a pH difference of 0.75 units (matrix alkaline). Synthesizing ATP under cellular conditions requires about +50 kJ/mol. Find the proton-motive force, the energy released per mole of protons, and the minimum number of protons needed per ATP. Compare with the structure of mammalian ATP synthase.
1. Proton-motive force: $\Delta p = 150 + 61.5\times0.75 = 150 + 46 = 196$ mV.
2. Energy per mole of H⁺: $F\Delta p = 96\,485\times0.196 = 1.89\times10^4$ J/mol $= 18.9$ kJ/mol.
3. Minimum protons per ATP: $50/18.9 = 2.6$. A rotary motor can couple a non-integer *average* number of protons to each ATP, so the requirement is simply that more than about 2.6 protons pass per ATP made.
4. Structure: the mammalian c-ring has 8 subunits, so one full turn carries 8 H⁺ and makes 3 ATP (one per catalytic site): $8/3 = 2.67$ H⁺ per ATP. Importing phosphate and exchanging ADP for ATP across the inner membrane costs about one more proton, for about 3.7 H⁺ per ATP delivered to the cytosol.
5. Oxidizing one NADH pumps 10 H⁺ (4 at complex I, 4 at complex III, 2 at complex IV): $10/3.67 = 2.7$ ATP. Electrons from succinate (via FADH₂) enter at complex II, which pumps none, so only 6 H⁺ are pumped: $6/3.67 = 1.6$ ATP.

**Answer:** $\Delta p \approx 196$ mV, releasing about 19 kJ per mole of protons; at least 2.6 protons are needed per ATP, and the real machine uses 2.67 at the synthase itself — thermodynamics and structure agree closely, with very little energy to spare. These stoichiometries explain the modern P/O ratios of about 2.5 per NADH and 1.5 per FADH₂, and hence roughly 30–32 ATP per glucose rather than the older textbook figure of 36–38.

**Worked Example 4.5 — Daily ATP turnover.** A person uses 2000 kcal of food energy per day. Assume this energy is released by oxidizing fuel equivalent to glucose (2870 kJ/mol released on complete oxidation) with 30 ATP made per glucose. What mass of ATP is made per day? (Molar mass of ATP: 507.18 g/mol.)
1. Energy: $2000\ \text{kcal}\times4.184\ \text{kJ/kcal} = 8368$ kJ.
2. Glucose equivalents: $8368/2870 = 2.92$ mol.
3. ATP: $2.92\times30 = 87.5$ mol.
4. Mass: $87.5\times507.18\ \text{g} = 4.44\times10^4$ g $= 44$ kg.

**Answer:** about 44 kg of ATP per day (47 kg if 32 ATP per glucose) — comparable to body mass. The body holds only a tiny fraction of this at any instant, so each ATP molecule is regenerated from ADP hundreds of times a day. ATP is an energy *currency*, not an energy *store*; long-term storage uses fat and glycogen.

### Chloroplasts (plants and algae)
- Site of photosynthesis. Double membrane enclosing the fluid **stroma** (Calvin cycle) and stacks (**grana**) of **thylakoids** (light reactions, chlorophyll).
- Chloroplasts use the same chemiosmotic principle as mitochondria, but protons are pumped *into* the thylakoid lumen by light-driven electron transport, and most of the proton-motive force is stored as a pH difference rather than as a voltage. Their ATP synthase has a larger c-ring (14 subunits in spinach), so more protons are needed per ATP.
- Also contain their own DNA and ribosomes. Part of a family of **plastids** (chromoplasts store pigments; amyloplasts store starch).

### The endosymbiotic theory
Lynn Margulis (publishing as Lynn Sagan, 1967) championed the idea that **mitochondria** derived from engulfed aerobic α-proteobacteria and **chloroplasts** from engulfed cyanobacteria. The idea had precursors — Konstantin Mereschkowski proposed a symbiotic origin for chloroplasts in 1905, and Ivan Wallin argued for bacterial mitochondria in the 1920s — but it was widely dismissed until molecular data arrived. Evidence:
- double membranes, the inner one resembling a bacterial plasma membrane;
- their own circular DNA resembling bacterial genomes;
- bacterial-type ribosomes sensitive to bacterial antibiotics (one reason some antibiotics have side effects in human cells);
- division by binary fission, using a dynamin- or FtsZ-based machinery;
- size similar to bacteria;
- phylogenetic analyses placing their genes within the α-proteobacteria and cyanobacteria;
- living examples of endosymbiosis at various stages, such as the amoeba *Paulinella*, whose photosynthetic "chromatophores" derive from a separate and much more recent capture of a cyanobacterium.

Over time most endosymbiont genes moved to the host nucleus. Human mtDNA retains only 37 genes, while a free-living α-proteobacterium has thousands; the protein products of the transferred genes are now made in the cytosol and imported back. This is why mitochondria cannot be grown outside a cell. In many algal lineages, a eukaryote engulfed another eukaryote that already had a chloroplast (**secondary endosymbiosis**), which is why some algal plastids are wrapped in three or four membranes.

### Peroxisomes
Single-membrane organelles containing oxidases that produce H₂O₂ and **catalase** that decomposes it (2H₂O₂ → 2H₂O + O₂). They oxidize very-long-chain fatty acids, help detoxify alcohol and other compounds (in liver), and begin the synthesis of plasmalogens (lipids abundant in myelin). Unlike most organelles, they import fully folded proteins from the cytosol. Christian de Duve also characterized and named peroxisomes in the 1960s. Defects cause Zellweger syndrome and X-linked adrenoleukodystrophy.

### The cytoskeleton
A dynamic network of protein filaments providing shape, mechanical support, intracellular transport and movement.

| Filament | Diameter | Protein | Functions |
|---|---|---|---|
| **Microfilaments** | ~7 nm | Actin | Cell shape, muscle contraction (with myosin), amoeboid movement, cytokinesis (contractile ring), microvilli |
| **Intermediate filaments** | ~10 nm | Keratins, vimentin, lamins, neurofilaments | Mechanical strength, anchoring the nucleus; very stable |
| **Microtubules** | ~25 nm | α/β-Tubulin | Tracks for motor proteins (kinesin → plus end, dynein → minus end), mitotic spindle, cilia and flagella (9+2 arrangement), cell shape |

Actin filaments and microtubules are **polar** (they have distinct plus and minus ends) and constantly assemble and disassemble. Microtubules show **dynamic instability** (Tim Mitchison and Marc Kirschner, 1984): each one grows steadily while its tip carries a cap of GTP-bound tubulin, then may suddenly lose the cap and shrink rapidly ("catastrophe"). This lets the spindle search space efficiently for chromosomes. Motor proteins convert ATP into mechanical steps: kinesin walks along a microtubule in 8 nm steps (the length of one tubulin dimer), one ATP per step.

**Centrosomes** (with a pair of centrioles in animal cells) organize microtubules. **Cilia** and **flagella** beat via dynein-driven sliding of microtubule doublets; defects cause primary ciliary dyskinesia (chronic respiratory infections, infertility, and sometimes reversed organ positions — situs inversus). **Drugs that target microtubules** illustrate how important their dynamics are: the anticancer drug taxol (paclitaxel) freezes microtubules by stabilizing them, while the anticancer vinca alkaloids (vinblastine, vincristine) prevent assembly; either way, dividing cells arrest in mitosis. Colchicine also blocks assembly; it is used to treat gout (by inhibiting inflammatory white blood cells) and in the laboratory to arrest cells in metaphase for karyotyping, but not as a cancer drug.

### Cell wall and extracellular matrix
- **Plant cell walls:** cellulose microfibrils in a matrix of hemicellulose and pectin (primary wall), sometimes a lignified secondary wall (wood). Provide rigidity and resist osmotic bursting (turgor). **Plasmodesmata** connect adjacent plant cells' cytoplasm.
- **Fungal walls:** chitin. **Bacterial walls:** peptidoglycan — chains of sugars cross-linked by short peptides. Penicillin (discovered by Alexander Fleming in 1928) blocks the enzymes that form the cross-links, and lysozyme (in tears and saliva) cuts the sugar backbone; without an intact wall, a growing bacterium bursts osmotically.
- **Animal extracellular matrix (ECM):** collagen (the most abundant protein in mammals), proteoglycans, fibronectin, laminin, elastin — connected to the cytoskeleton via **integrins**, influencing cell shape, migration, survival and gene expression. Bone is ECM mineralized with calcium phosphate.

### Cell junctions (animals)
- **Tight junctions:** seal adjacent cells, preventing leakage (intestinal epithelium, blood–brain barrier).
- **Desmosomes:** spot-welds anchoring intermediate filaments; mechanical strength (skin, heart muscle).
- **Adherens junctions:** cadherin-based, linked to actin.
- **Gap junctions:** channels (connexins) allowing ions and small molecules to pass directly between cells (electrical coupling in heart muscle).

### How much of the cell does each compartment occupy?

Electron-microscope measurements of a mammalian liver cell (hepatocyte) give the following approximate breakdown, a useful reminder that organelles are not drawn to scale in most diagrams.

| Compartment | Share of cell volume (%) | Approximate number per cell |
|---|---|---|
| Cytosol | 54 | 1 |
| Mitochondria | 22 | ~1700 |
| Rough ER cisternae | 9 | 1 |
| Smooth ER plus Golgi cisternae | 6 | — |
| Nucleus | 6 | 1 |
| Peroxisomes | 1 | ~400 |
| Lysosomes | 1 | ~300 |
| Endosomes | 1 | ~200 |

The *membrane* area is distributed very differently: in a hepatocyte the plasma membrane is only about 2% of all the cell's membrane, while the rough ER (about 35%) and the mitochondrial inner membrane (about 32%) dominate. Internal membranes provide the surface area that a large cell's plasma membrane alone could never supply — the same scaling problem as in Section 1, solved from the inside.

## 5. Comparing Animal and Plant Cells

| Structure | Animal cell | Plant cell |
|---|---|---|
| Cell wall | Absent | Cellulose wall |
| Chloroplasts | Absent | Present (in green tissues) |
| Mitochondria | Present | Present (plants respire too) |
| Central vacuole | Small vacuoles, if any | Large central vacuole (up to 90% of volume) |
| Centrioles | Present | Absent (in most plants) |
| Lysosomes | Common | Functions largely performed by vacuole |
| Shape | Variable, flexible | Fixed, often rectangular |
| Energy storage | Glycogen | Starch |
| Cytokinesis | Cleavage furrow (contractile ring) | Cell plate (from Golgi vesicles) |
| Plasmodesmata | Absent (gap junctions instead) | Present |

## 6. Cell Signaling

Cells communicate through chemical signals:
- **Endocrine:** hormones travel through the bloodstream (insulin, estrogen).
- **Paracrine:** local signaling to nearby cells (growth factors; neurotransmitters at synapses are a specialized, very short-range case).
- **Autocrine:** cells signal themselves (some cancer cells, immune cells).
- **Juxtacrine (contact-dependent):** membrane-bound signals (Notch–Delta).

### Three stages
1. **Reception:** a signal molecule (ligand) binds a specific **receptor** — on the cell surface (for hydrophilic signals) or inside the cell (for small hydrophobic signals such as steroid and thyroid hormones, nitric oxide).
2. **Transduction:** a cascade of molecular changes relays and **amplifies** the signal (one hormone molecule can lead to millions of product molecules).
3. **Response:** changes in enzyme activity, gene expression, cell shape, secretion or division.

The concept of a **second messenger** — a small intracellular molecule that carries the signal from a surface receptor to the cell's interior — came from Earl Sutherland's discovery of cyclic AMP in the late 1950s, while he studied how adrenaline makes liver cells release glucose (Nobel 1971).

### Major receptor types
- **G protein-coupled receptors (GPCRs):** seven transmembrane helices; activate heterotrimeric G proteins (swapping GDP for GTP), which regulate enzymes such as adenylyl cyclase (→ **cAMP** → protein kinase A) or phospholipase C (→ IP₃ → Ca²⁺ release, and DAG → protein kinase C). The largest receptor family (~800 human genes, about half of them odorant receptors), targeted by roughly one third of approved drugs. Includes receptors for adrenaline, dopamine, serotonin, opioids, histamine, odors, tastes and light (rhodopsin). (Lefkowitz and Kobilka, Nobel Chemistry 2012; Gilman and Rodbell for G proteins, Nobel Physiology or Medicine 1994.)
- **Receptor tyrosine kinases (RTKs):** for most RTKs (such as the EGF and PDGF receptors) ligand binding causes dimerization and cross-phosphorylation of tyrosines (the insulin receptor is already a covalently linked dimer and is activated by a change in shape). The phosphotyrosines recruit signaling proteins that activate pathways such as Ras → MAP kinase cascade (cell growth and division). Mutated, overactive RTKs and Ras proteins drive many cancers (HER2 in breast cancer — treated with trastuzumab).
- **Ligand-gated ion channels:** open in response to ligands (nicotinic acetylcholine receptor, GABA$_\text{A}$ receptor, NMDA receptor).
- **Intracellular (nuclear) receptors:** steroid hormone–receptor complexes act as transcription factors.

**Signal termination** is as important as activation: G proteins hydrolyze GTP; phosphodiesterases degrade cAMP; phosphatases remove phosphates; receptors are internalized. Methylxanthines such as caffeine and theophylline inhibit phosphodiesterases at high concentrations, although at the doses in coffee caffeine acts mainly by blocking adenosine receptors. **Cholera toxin** chemically modifies the stimulatory G protein $\text{G}_\text{s}$ so it stays locked in its active state, causing massive cAMP production and fluid loss from intestinal cells; **pertussis toxin** modifies the inhibitory $\text{G}_\text{i}$ so it can no longer be activated.

### Derivation: how much signal does a receptor see?

For a ligand $L$ binding reversibly to a receptor $R$,
$$L + R \rightleftharpoons LR, \qquad K_d = \frac{[L][R]}{[LR]}$$
where $K_d$ is the **dissociation constant** (a concentration; smaller $K_d$ means tighter binding). The total receptor is $R_T = [R] + [LR]$. Substituting $[R] = K_d[LR]/[L]$ gives $R_T = [LR](1 + K_d/[L])$, so the **fractional occupancy** is
$$\theta = \frac{[LR]}{R_T} = \frac{[L]}{[L] + K_d}$$
(assuming the ligand is in excess, so binding does not deplete it). Three consequences follow. Half the receptors are occupied when $[L] = K_d$. Occupancy goes from 10% (at $[L] = K_d/9$) to 90% (at $[L] = 9K_d$) only over an 81-fold range of ligand concentration, so a simple receptor responds smoothly, not like a switch. And when several binding events cooperate, the response is described by the Hill equation $\theta = [L]^n/([L]^n + K^n)$, for which the 10%-to-90% range shrinks to $81^{1/n}$ — only 3-fold for $n = 4$. Cooperativity, multistep cascades and feedback are how cells build switch-like, all-or-none decisions (for example, committing to divide).

**Worked Example 6.1 — Receptor occupancy.** A hormone binds its receptor with $K_d = 2.0$ nM. Find the fractional occupancy at 0.5, 2.0 and 10 nM hormone, and the concentration needed for 90% occupancy.
1. At 0.5 nM: $\theta = 0.5/(0.5 + 2.0) = 0.20$.
2. At 2.0 nM: $\theta = 2.0/4.0 = 0.50$.
3. At 10 nM: $\theta = 10/12 = 0.83$.
4. For $\theta = 0.9$: $[L]/([L] + K_d) = 0.9 \Rightarrow [L] = 9K_d = 18$ nM.

**Answer:** 20%, 50% and 83% occupancy; 90% requires 18 nM. Raising the hormone 20-fold, from 0.5 to 10 nM, only quadruples the occupancy — a saturating response.

**Worked Example 6.2 — Amplification in a cAMP cascade (illustrative numbers).** Adrenaline acting on a liver cell triggers the following chain. Suppose that one activated receptor activates 20 G-protein molecules; each active $\text{G}_\text{s}$ switches on one adenylyl cyclase, which makes 1000 cAMP before shutting off; four cAMP molecules activate one protein kinase A holoenzyme, releasing two active catalytic subunits; each catalytic subunit phosphorylates (activates) 10 molecules of phosphorylase kinase; each of those activates 10 molecules of glycogen phosphorylase; and each phosphorylase releases 1000 glucose 1-phosphate units from glycogen. How many glucose units result from one hormone molecule?
1. G proteins: $1\times20 = 20$; adenylyl cyclases: 20.
2. cAMP: $20\times1000 = 2\times10^4$.
3. PKA: $2\times10^4/4 = 5\times10^3$ holoenzymes $\Rightarrow 1\times10^4$ catalytic subunits.
4. Phosphorylase kinase: $1\times10^4\times10 = 1\times10^5$.
5. Glycogen phosphorylase: $1\times10^5\times10 = 1\times10^6$.
6. Glucose 1-phosphate: $1\times10^6\times1000 = 1\times10^9$.

**Answer:** about $10^9$ glucose units per hormone molecule with these assumed factors. Real factors vary from cell to cell, but the lesson holds: amplification comes from *enzymatic* steps, in which one active molecule acts on many substrate molecules, whereas stoichiometric steps (four cAMP per PKA) do not amplify at all. Multi-step cascades also offer many points for regulation and for integrating different signals.

## 7. The Cell Cycle

The life of a eukaryotic cell from one division to the next:

| Phase | Events |
|---|---|
| **G₁** (gap 1) | Cell growth, normal functions, organelle duplication; decides whether to divide (restriction point) |
| **S** (synthesis) | DNA replication — each chromosome becomes two sister chromatids joined at the centromere; centrosome duplication |
| **G₂** (gap 2) | Further growth; preparation for mitosis; checks for complete, undamaged DNA |
| **M** (mitotic phase) | Mitosis (nuclear division) + cytokinesis (cytoplasmic division) |
| **G₀** | Non-dividing resting state (neurons, mature muscle cells; many cells can re-enter) |

**Interphase** (G₁ + S + G₂) occupies ~90% of the cycle. A typical human cell in culture divides about every 24 hours (M phase ~1 hour). Gut epithelial cells divide rapidly; neurons rarely or never. Interphase is not a resting phase: it is when the cell grows, works and copies its entire genome.

### Mitosis
Produces two genetically identical daughter nuclei, each with the same chromosome number as the parent (diploid → diploid in somatic cells). Used for growth, repair and asexual reproduction. Walther Flemming described the process in stained salamander cells and named it in 1882.
1. **Prophase:** chromatin condenses into visible chromosomes; the mitotic spindle begins forming from centrosomes; nucleolus disappears.
2. **Prometaphase:** nuclear envelope breaks down; spindle microtubules attach to **kinetochores** at centromeres.
3. **Metaphase:** chromosomes align at the **metaphase plate** (cell equator). Best stage for viewing a **karyotype**.
4. **Anaphase:** cohesin is cleaved by separase; sister chromatids separate and are pulled to opposite poles (kinetochore microtubules shorten; polar microtubules push poles apart).
5. **Telophase:** nuclear envelopes re-form around each set; chromosomes decondense.
6. **Cytokinesis:** animal cells — actin–myosin **cleavage furrow**; plant cells — **cell plate** forms from Golgi vesicles, becoming a new wall.

Mnemonic: **PMAT** (Prophase, Metaphase, Anaphase, Telophase). **Meiosis**, the two-step division that halves the chromosome number to make gametes and shuffles alleles by crossing over and independent assortment, is treated in the genetics chapter.

Prokaryotes divide by **binary fission**: the circular chromosome replicates from a single origin, copies move apart, and the cell pinches in two (as fast as every ~20 minutes for *E. coli* in ideal conditions). The bacterial tubulin homolog FtsZ forms the constricting ring.

### Exponential growth

If every cell divides once per **generation time** $g$, the population doubles each generation:
$$N(t) = N_0\,2^{t/g} = N_0\,e^{kt}, \qquad k = \frac{\ln 2}{g}$$
Taking logarithms, the number of generations needed to grow from $N_0$ to $N$ is $\log_2(N/N_0)$. In a closed flask (batch culture), bacteria pass through a **lag phase** (adjusting to the medium), an **exponential (log) phase**, a **stationary phase** when nutrients run out or wastes accumulate, and a **death phase**.

**Worked Example 7.1 — The power of doubling.** *E. coli* divides every 20 minutes in rich medium, and one cell has a mass of about 1 pg ($10^{-15}$ kg). Starting from a single cell: (a) how many cells are there after 8 hours of unchecked growth? (b) What mass would 44 hours of unchecked growth produce? (c) How many rounds of doubling would turn one human zygote into $3\times10^{13}$ cells if no cell ever died?
1. (a) 8 h = 480 min = 24 generations: $N = 2^{24} = 1.68\times10^7$ cells.
2. (b) 44 h = 132 generations: $N = 2^{132} = 5.4\times10^{39}$ cells, of mass $5.4\times10^{39}\times10^{-15}\ \text{kg} = 5.4\times10^{24}$ kg.
3. Compare with Earth's mass, $5.97\times10^{24}$ kg: the ratio is 0.91.
4. (c) $\log_2(3\times10^{13}) = 44.8$, so about 45 rounds of doubling.

**Answer:** (a) about 17 million cells; (b) about 0.9 Earth masses — which shows that exponential growth must always be cut short by limited resources, as Darwin and Malthus emphasized; (c) about 45 doublings. Real development takes many more divisions than 45, because cells continually die and are replaced.

### Measuring the phases: cell-cycle kinetics

How do we know that M phase lasts about an hour? One method counts the fraction of cells in each phase in an unsynchronized population — for example the **mitotic index**, the fraction of cells in mitosis. A naive estimate multiplies each fraction by the cycle time $T$. But in a growing population, young cells outnumber old ones (every division turns one old cell into two new ones), so the naive estimate is biased.

*Derivation.* In steady exponential growth the population, and hence the birth rate, increases as $2^{t/T}$. Cells that are now of age $a$ were born a time $a$ ago, when the birth rate was smaller by the factor $2^{-a/T}$. So the density of cells of age $a$ (for $0 \le a \le T$) is proportional to $2^{-a/T}$. Normalizing, using $\int_0^T 2^{-a/T}\,da = T/(2\ln 2)$:
$$n(a) = \frac{2\ln 2}{T}\,2^{-a/T}$$
The fraction of cells in the *last* phase of the cycle (M), of duration $t_M$, is
$$f_M = \int_{T-t_M}^{T} n(a)\,da = 2^{t_M/T} - 1 \quad\Longrightarrow\quad t_M = T\log_2(1 + f_M)$$
The same reasoning applied to the last $t$ hours of the cycle gives the total duration of any group of late phases (for example S + G₂ + M) from their combined fraction, and the duration of the *first* phase, G₁, follows from
$$f_{G_1} = \int_0^{t_{G_1}} n(a)\,da = 2\left(1 - 2^{-t_{G_1}/T}\right)\quad\Longrightarrow\quad t_{G_1} = -T\log_2\!\left(1 - \frac{f_{G_1}}{2}\right)$$

**Worked Example 7.2 — Phase durations from a cell count.** In an exponentially growing culture with a doubling time of 22 h, 1000 cells are classified (by DNA content and microscopy): 520 in G₁, 300 in S, 130 in G₂ and 50 in M. Estimate the duration of each phase, first naively and then with the age-distribution correction.
1. Naive estimates ($t = fT$): G₁ $0.52\times22 = 11.4$ h; S $0.30\times22 = 6.6$ h; G₂ $0.13\times22 = 2.9$ h; M $0.05\times22 = 1.1$ h.
2. Corrected M: $t_M = 22\log_2(1.05) = 22\times0.0704 = 1.55$ h.
3. G₂ + M (fraction 0.18): $22\log_2(1.18) = 5.25$ h, so $t_{G_2} = 5.25 - 1.55 = 3.70$ h.
4. S + G₂ + M (fraction 0.48): $22\log_2(1.48) = 12.44$ h, so $t_S = 12.44 - 5.25 = 7.19$ h.
5. G₁: $22 - 12.44 = 9.56$ h. Check with the G₁ formula: $-22\log_2(1 - 0.26) = -22\log_2(0.74) = 9.56$ h. ✓

**Answer:** G₁ ≈ 9.6 h, S ≈ 7.2 h, G₂ ≈ 3.7 h, M ≈ 1.5 h. The naive method overestimates the early phase (G₁) by almost 2 hours and underestimates M by about 30%, because the population is weighted toward young cells.

### Regulation of the cell cycle
- **Cyclins** and **cyclin-dependent kinases (CDKs)** drive transitions; cyclin levels rise and fall each cycle, while CDK levels are constant. Maturation-promoting factor (MPF, cyclin B–CDK1) triggers mitosis. Leland Hartwell identified cell-division-cycle (*cdc*) genes in budding yeast in the early 1970s; Paul Nurse found the key kinase (*cdc2*, now CDK1) in fission yeast and its human counterpart in 1987; Tim Hunt discovered cyclins in 1982 as proteins that are destroyed at each division of sea-urchin eggs (Nobel 2001).
- Cyclins are destroyed by the ubiquitin–proteasome system: the anaphase-promoting complex/cyclosome (APC/C) tags cyclin B and securin (the inhibitor of separase) for degradation, which is what makes the exit from mitosis irreversible.
- **Checkpoints:**
  - **G₁/S checkpoint** (restriction point): Is the cell large enough? Are nutrients and growth factors present? Is DNA undamaged?
  - **G₂/M checkpoint:** Is DNA fully and correctly replicated?
  - **Spindle (M) checkpoint:** Are all chromosomes attached to the spindle before anaphase?
- **p53** ("guardian of the genome") halts the cycle in response to DNA damage, activating repair or apoptosis; it is mutated in about half of all human cancers. **Rb** (retinoblastoma protein) restrains the G₁/S transition by holding the E2F transcription factors inactive until Rb is phosphorylated by CDKs (cyclin D–CDK4/6, then cyclin E–CDK2).
- **Telomeres** (repeats of TTAGGG at chromosome ends) shorten with each division in most somatic cells, because the replication machinery cannot completely copy the end of a linear chromosome (the "end-replication problem"). This limits the number of divisions (~40–60 for human fibroblasts, the **Hayflick limit**, reported by Leonard Hayflick and Paul Moorhead in 1961). **Telomerase** (an RNA-containing reverse transcriptase) maintains telomeres in stem cells, germ cells and ~85–90% of cancers (Blackburn, Greider, Szostak, Nobel 2009).

### Cancer
Cancer is uncontrolled cell division resulting from accumulated mutations that disrupt cell-cycle control. Theodor Boveri suggested as early as 1914 that abnormal chromosomes could cause tumors.
- **Oncogenes:** mutated, overactive versions of **proto-oncogenes** that promote growth (Ras, Myc, HER2, BCR-ABL) — "stuck accelerator". A mutation in one copy is usually enough (the effect is dominant). Michael Bishop and Harold Varmus showed in 1976 that the cancer-causing *src* gene of a chicken retrovirus was a captured version of a normal cellular gene (Nobel 1989).
- **Tumor suppressor genes:** normally restrain division or trigger repair/apoptosis (p53, Rb, BRCA1/2, APC) — both copies usually must be inactivated ("two-hit hypothesis", Alfred Knudson, 1971) — "broken brakes".
- The **hallmarks of cancer** (Douglas Hanahan and Robert Weinberg, 2000, updated 2011) include sustained proliferative signaling, evading growth suppressors, resisting cell death, replicative immortality, angiogenesis, invasion and **metastasis**, reprogrammed metabolism, and immune evasion, enabled by genome instability and tumor-promoting inflammation.
- Causes of mutations: carcinogens (tobacco smoke, UV, aflatoxin, asbestos), radiation, viruses (HPV — prevented by vaccination; hepatitis B and C; EBV), inherited predispositions, and random replication errors.
- Because several independent mutations are usually required, most cancers become far more common with age.
- Treatments: surgery, radiation, chemotherapy (targeting dividing cells), targeted therapies (imatinib for BCR-ABL, approved in 2001; CDK4/6 inhibitors such as palbociclib for some breast cancers), immunotherapy (checkpoint inhibitors anti-PD-1/CTLA-4, Allison and Honjo, Nobel 2018; CAR-T cells).

## 8. Cell Death: Apoptosis
**Apoptosis** (named by John Kerr, Andrew Wyllie and Alastair Currie in 1972, from the Greek for "falling off", as of leaves) is programmed, orderly cell suicide: the cell shrinks, chromatin condenses, DNA is cut into fragments, the membrane blebs, and the cell breaks into membrane-wrapped apoptotic bodies that phagocytes remove without inflammation. Executed by **caspases** (cysteine proteases), regulated by:
- the **intrinsic (mitochondrial) pathway:** cellular stress or DNA damage shifts the balance among Bcl-2 family proteins; pro-apoptotic members (Bax, Bak) perforate the outer mitochondrial membrane, cytochrome c escapes and assembles with Apaf-1 into the **apoptosome**, which activates caspase-9;
- the **extrinsic (death-receptor) pathway:** ligands such as Fas ligand or TNF bind death receptors on the surface, activating caspase-8.

Both pathways converge on executioner caspases (caspase-3 and -7). Roles: sculpting development (separating fingers and toes, removing a large fraction of the neurons generated during brain development), eliminating damaged or infected cells, and immune selection (removing lymphocytes that would attack the body's own tissues). An adult human is commonly estimated to lose tens of billions of cells per day by apoptosis, balanced by cell division. (Brenner, Horvitz and Sulston, Nobel 2002, studying *C. elegans*, in which exactly 131 of the 1090 somatic cells generated during hermaphrodite development die.) Too little apoptosis contributes to cancer and autoimmunity; too much contributes to neurodegeneration and tissue damage after stroke. **Necrosis**, by contrast, is uncontrolled death from injury: the cell swells and bursts, spilling contents that cause inflammation. Other regulated forms of death, such as necroptosis and pyroptosis (both inflammatory) and iron-dependent ferroptosis, are active research areas.

## 9. Stem Cells and Differentiation
- **Totipotent** cells (zygote, early blastomeres) can form all cell types including placenta.
- **Pluripotent** embryonic stem cells (inner cell mass of the blastocyst) can form all body cell types.
- **Multipotent** adult stem cells (hematopoietic stem cells in bone marrow, intestinal crypt stem cells) form a limited range.
- Stem cells can **self-renew** (make more stem cells) and produce differentiated descendants; often one division gives one daughter of each kind (asymmetric division).
- **Induced pluripotent stem cells (iPSCs):** Shinya Yamanaka and Kazutoshi Takahashi reprogrammed mouse fibroblasts to pluripotency in 2006 (and human cells in 2007) with four transcription factors (Oct4, Sox2, Klf4, c-Myc) (Nobel 2012 with John Gurdon, who showed in 1962 that the nucleus of a differentiated frog intestinal cell could direct development of a whole frog).
- **Differentiation** arises from differential gene expression, not loss of genes — almost every cell contains the full genome. Gurdon's experiment and, later, the cloning of Dolly the sheep from an adult cell (1996) proved the point.
- Applications: bone marrow transplants (since the 1950s–60s; E. Donnall Thomas, Nobel 1990), regenerative medicine, disease modeling, drug screening, and **organoids** — miniature three-dimensional organs grown from stem cells, first achieved for mouse intestine by Toshiro Sato and Hans Clevers in 2009.

## 10. Viruses (Acellular Entities)
Viruses are not cells: they consist of nucleic acid (DNA or RNA, single- or double-stranded) in a protein **capsid**, sometimes with a lipid **envelope**. They have no ribosomes and no metabolism of their own, and they replicate only inside host cells, hijacking cellular machinery.
- **Lytic cycle:** viral replication bursts the cell. **Lysogenic cycle** (bacteriophages): viral DNA integrates into the host genome as a prophage.
- **Retroviruses** (HIV) use **reverse transcriptase** to copy RNA into DNA, which integrates into the host genome (Baltimore and Temin, with Dulbecco, Nobel 1975). Peyton Rous had shown in 1911 that a filterable agent (later recognized as a retrovirus) causes tumors in chickens (Nobel 1966).
- Sizes ~20–300 nm; giant viruses such as mimivirus (reported in 2003) have particles several hundred nanometres across, visible in a light microscope.
- Examples: influenza, SARS-CoV-2 (coronavirus, +ssRNA, spike protein binds ACE2), HIV, hepatitis B, herpesviruses, HPV, measles, bacteriophage T4.
- **Prions** (misfolded proteins) and **viroids** (naked circular RNA infecting plants) are even simpler infectious agents.
- Antibiotics do not work against viruses; antiviral drugs target viral enzymes (reverse transcriptase, protease, polymerase, neuraminidase), and vaccines train the immune system (smallpox, declared eradicated in 1980, was the first human disease eliminated by vaccination).

## 11. Historical Development

| Year | Who | Discovery or advance |
|---|---|---|
| 1665 | Robert Hooke | *Micrographia*; names "cells" in cork |
| 1674–1683 | Antonie van Leeuwenhoek | First observations of protists, bacteria and sperm |
| 1827 | Robert Brown | Random jiggling of tiny particles from pollen grains (Brownian motion) |
| 1831 | Robert Brown | Names the nucleus in orchid cells |
| 1838–1839 | Matthias Schleiden, Theodor Schwann | Cell theory |
| 1852–1855 | Robert Remak, Rudolf Virchow | Cells arise only from cells |
| 1859–1862 | Louis Pasteur | Swan-neck flasks refute spontaneous generation of microbes |
| 1873 | Ernst Abbe | Theory of the diffraction limit of microscopes |
| 1882 | Walther Flemming | Describes and names mitosis |
| 1884 | Hans Christian Gram | Gram stain distinguishes two great groups of bacteria |
| 1898 | Camillo Golgi | Golgi apparatus |
| 1905 | Konstantin Mereschkowski | Symbiotic origin of chloroplasts proposed |
| 1931 | Max Knoll, Ernst Ruska | First electron microscope (Ruska, Nobel Physics 1986) |
| 1930s | Frits Zernike | Phase-contrast microscopy (Nobel Physics 1953) |
| 1945 | Keith Porter, Albert Claude, Ernest Fullam | First electron micrograph of a whole cultured cell, revealing the ER |
| 1951 | George Gey | HeLa cells, from Henrietta Lacks's tumor: the first continuously growing human cell line |
| 1955 | Christian de Duve | Lysosomes |
| 1950s–1960s | George Palade | Ribosomes; the secretory pathway by pulse–chase |
| 1961 | Peter Mitchell | Chemiosmotic hypothesis |
| 1961 | Leonard Hayflick, Paul Moorhead | Normal human cells have a finite number of divisions |
| 1962 | John Gurdon | Differentiated nuclei retain all genes (frog cloning) |
| 1967 | Lynn Margulis (Sagan) | Endosymbiotic origin of mitochondria and chloroplasts |
| 1970 | L. David Frye, Michael Edidin | Membrane proteins diffuse in the plane of the membrane |
| 1971 | Alfred Knudson | Two-hit hypothesis for retinoblastoma |
| 1972 | S. Jonathan Singer, Garth Nicolson | Fluid mosaic model |
| 1972 | John Kerr, Andrew Wyllie, Alastair Currie | Apoptosis described and named |
| 1977 | Carl Woese, George Fox | Archaea recognized from rRNA sequences |
| 1970s–1987 | Leland Hartwell, Tim Hunt, Paul Nurse | *cdc* genes, cyclins (1982), CDK1 |
| 1994 | Martin Chalfie and colleagues | GFP expressed in other organisms as a living tag |
| 2006 | Shinya Yamanaka, Kazutoshi Takahashi | Induced pluripotent stem cells |
| 2022 | Jean-Marie Volland and colleagues | *Thiomargarita magnifica*, a bacterium visible to the naked eye |

Three threads run through this history. First, **instruments drove ideas**: the cell theory had to wait for compound microscopes, organelle biology for the electron microscope and the ultracentrifuge, and modern molecular cell biology for fluorescent proteins, super-resolution optics and cryo-EM. Second, **model organisms** made general principles visible: yeast for the cell cycle and vesicle traffic, *C. elegans* for apoptosis, frog and sea-urchin eggs for cyclins, *E. coli* for almost everything molecular. Third, ideas initially dismissed as eccentric — endosymbiosis, chemiosmosis, the archaea as a separate domain — became textbook orthodoxy once decisive evidence accumulated, a reminder that science changes its mind in response to data.

## 12. Applications in Medicine, Technology and Everyday Life

- **Antibiotics and selective toxicity.** Effective antimicrobial drugs exploit differences between microbial and human cells: penicillins and cephalosporins block peptidoglycan cross-linking (human cells have no peptidoglycan); aminoglycosides, tetracyclines and macrolides block 70S ribosomes; fluoroquinolones inhibit bacterial DNA gyrase; azole antifungals block synthesis of ergosterol, the sterol of fungal membranes, which human cells replace with cholesterol. Side effects often arise where the difference is incomplete, such as the bacterial-type ribosomes inside our mitochondria.
- **Cancer therapy** targets the cell cycle and its controls: taxanes and vinca alkaloids (microtubules), DNA-damaging agents and antimetabolites (S phase), CDK4/6 inhibitors (the G₁/S transition), targeted kinase inhibitors (imatinib), and immunotherapies that remove brakes on T cells.
- **Diagnosis by looking at cells.** Histopathology examines stained tissue sections to diagnose cancer; the Pap test, developed by George Papanicolaou between the 1920s and 1940s, detects precancerous cervical cells and has greatly reduced cervical-cancer deaths; Gram staining guides the first choice of antibiotic; flow cytometry counts and sorts blood cells by size and fluorescent markers (essential in leukemia diagnosis and in monitoring HIV infection by CD4⁺ T-cell counts); karyotyping detects chromosome abnormalities in prenatal diagnosis and cancer.
- **Osmosis in practice.** Intravenous fluids must be close to isotonic (0.9% saline, Worked Example 4.1). Salting and sugaring preserve food because the hypertonic environment draws water out of microbes. Gardeners who over-fertilize can "burn" roots by making the soil water hypertonic to root cells.
- **Cell factories.** Recombinant human insulin made in *E. coli* was the first genetically engineered drug approved (1982); many therapeutic antibodies are produced in cultured Chinese hamster ovary (CHO) cells; yeast cells make bread rise and ferment beer and wine; viral vaccines are grown in eggs or in cultured cells. HeLa cells were used in the 1950s to test the polio vaccine.
- **Regenerative and reproductive medicine.** Hematopoietic stem-cell transplants treat leukemias and inherited blood disorders; the first transplant of iPSC-derived cells (retinal pigment epithelium, for macular degeneration) took place in Japan in 2014; in vitro fertilization and mitochondrial replacement therapy depend on handling single cells.
- **Microscopy and imaging technology.** Cell biology drove advances in optics, fluorescent dyes and detectors, which now serve materials science and semiconductor inspection as well.

## 13. Connections to Other Subjects

- **Physics.** Diffusion is Brownian motion, described by random-walk statistics (Section 1). The Stokes–Einstein relation $D = k_BT/(6\pi\eta R)$ predicts, for a protein of radius 2.5 nm in water at 37 °C ($\eta = 0.692$ mPa s), $D = 1.3\times10^{-10}\ \text{m}^2\,\text{s}^{-1} = 130\ \mu\text{m}^2\,\text{s}^{-1}$; measured values in cytoplasm for proteins of this size are several-fold lower in mammalian cells and around ten-fold lower in bacteria, a sign of crowding. Microscopy is wave optics (Abbe limit) and electron microscopy is quantum mechanics (de Broglie wavelength). The membrane is a capacitor: a parallel-plate estimate $C = \varepsilon_0\varepsilon_r/d$ with $\varepsilon_r \approx 2$ and $d \approx 3$ nm gives about $0.6\ \mu\text{F cm}^{-2}$, close to the measured $1\ \mu\text{F cm}^{-2}$. Swimming bacteria live at low **Reynolds number**: for *E. coli* swimming at 30 μm/s, with length 2 μm, in water, $\text{Re} = \rho vL/\eta = (1000)(30\times10^{-6})(2\times10^{-6})/(10^{-3}) = 6\times10^{-5}$, so inertia is irrelevant and a bacterium that stops its flagella stops almost instantly (Edward Purcell's 1977 article "Life at low Reynolds number" made this famous).
- **Chemistry.** Membrane self-assembly is the hydrophobic effect; osmosis and the Nernst equation are applications of chemical potential; the proton-motive force couples redox chemistry (electron transport) to phosphorylation; receptor binding is the law of mass action; lysosome function depends on pH; enzymes (including transporters) show saturation kinetics.
- **Mathematics.** Geometric scaling ($A/V \propto 1/L$), exponential growth and logarithms, probability (stochastic gene expression when molecules are few), integration over an age distribution (cell-cycle kinetics), and the Hill function as a model of biological switches.
- **Other areas of biology.** Genetics (chromosomes, meiosis, mutation), molecular biology (DNA replication, transcription, translation), evolution (endosymbiosis, the tree of life, the last universal common ancestor), physiology (nerve impulses, muscle contraction, kidney osmoregulation) and ecology (microbial communities, photosynthesis as the base of food webs) all rest on the cell.
- **Astronomy and astrobiology.** Extremophile archaea set the known limits of life — the methanogen *Methanopyrus kandleri* strain 116 grows at 122 °C under high pressure (reported 2008) — guiding the search for habitable environments on Mars and in the subsurface oceans of Europa and Enceladus. Experiments on fatty-acid vesicles that grow and divide inform ideas about how the first cells (protocells) arose on the early Earth.

## 14. Common Misconceptions

- **"Plant cells have chloroplasts instead of mitochondria."** Plant cells have both. Chloroplasts capture light energy to make sugar; mitochondria then oxidize sugar to make ATP, day and night, in every living plant cell — including root cells, which have no chloroplasts at all.
- **"Bacteria are just small, simple bags of enzymes."** Bacteria have cytoskeletal proteins (FtsZ, MreB), protein-shelled compartments (carboxysomes), precisely positioned molecules, sophisticated signaling and, in some groups, internal membranes. They are differently organized, not disorganized — and they have had as long to evolve as we have.
- **"The cell is mostly empty water."** The cytoplasm holds roughly 300–400 g of macromolecules per litre; it is a crowded gel in which large molecules diffuse several times more slowly than in water.
- **"Mitochondria are the only source of ATP."** Glycolysis in the cytosol makes ATP without oxygen. Mature red blood cells have no mitochondria and rely entirely on glycolysis, and many tumor cells lean heavily on it even when oxygen is present.
- **"ATP is a long-term energy store."** The body contains very little ATP at any moment and recycles roughly its own mass of it each day (Worked Example 4.5). Fat and glycogen store energy; ATP transfers it.
- **"Diffusion is fast, so cells could be any size."** Diffusion time grows with the square of distance (Section 1): milliseconds across a bacterium, but centuries along a metre-long axon.
- **"Bigger organisms have bigger cells."** Most cell types are similar in size across mammals; large animals have more cells, not larger ones.
- **"Every cell in the body contains exactly the same DNA."** Differentiation does not involve losing genes, but there are real exceptions: mature red blood cells and platelets lack nuclei; gametes are haploid; B and T lymphocytes cut and rejoin their antibody and receptor genes; some liver and heart cells are polyploid; and every cell accumulates its own somatic mutations.
- **"Interphase is a resting phase."** Interphase includes DNA replication (S phase) and nearly all of the cell's growth and work; G₀ is the true non-dividing state.
- **"Chromosomes are X-shaped."** The familiar X is a *replicated* chromosome (two sister chromatids) condensed for mitosis. For most of the cycle, chromosomes are long, decondensed threads occupying distinct territories in the nucleus.
- **"A higher-magnification microscope always shows more detail."** Beyond the diffraction limit, extra magnification is empty; seeing finer detail requires shorter wavelengths, higher numerical aperture or super-resolution tricks.
- **"Osmosis means solutes move."** In osmosis it is *water* that moves, toward the region of higher solute particle concentration; and tonicity depends only on solutes that cannot cross the membrane (the urea example in Section 4).
- **"The membrane potential means the cytoplasm is full of negative charge."** Only about 16 parts per million of a cell's ions are needed to charge the membrane (Worked Example 4.2); the bulk of the cytoplasm is electrically neutral.
- **"Viruses are the smallest living cells" / "antibiotics cure viral infections."** Viruses are not cells, have no metabolism or ribosomes, and are untouched by drugs that target bacterial walls and ribosomes. Using antibiotics against colds and flu does nothing for the infection and promotes antibiotic resistance.
- **"Cancer is caused by a single mutation."** Most cancers require several mutations in different oncogenes and tumor suppressors, accumulated over years — which is why cancer incidence rises steeply with age.

## 15. Practice Problems

1. (Easy, conceptual) A ribosome is about 25 nm across. Explain why it cannot be resolved with a light microscope, even at 2000× magnification, and name an instrument that can resolve it.
2. (Easy) Compare the surface-area-to-volume ratio of a cube-shaped cell 1 μm on a side with one 10 μm on a side. If the large cube were divided into 1 μm cubes, how many would there be, and by what factor would the total surface area increase?
3. (Easy) A culture starts with 100 bacteria that divide every 30 minutes. Assuming unlimited resources, how many cells are present after 6 hours?
4. (Medium) In an exponentially growing culture with a cycle time of 20 h, 30 of 600 cells are in mitosis. Estimate the length of M phase (a) naively and (b) with the age-distribution correction.
5. (Medium, conceptual) Predict what happens to red blood cells placed in each solution, and explain: (a) 0.30 M sucrose; (b) 0.30 M NaCl; (c) 0.10 M NaCl; (d) 0.30 M urea. (Cytoplasm is about 0.30 osmol/L; sucrose cannot cross the membrane, urea slowly can.)
6. (Medium) A receptor binds its ligand with $K_d = 5.0$ nM. What fraction of receptors is occupied at 1.0 nM ligand? What ligand concentration gives 75% occupancy?
7. (Medium) What is the longest wavelength that would allow an objective with NA 1.4 to resolve two structures 150 nm apart according to the Abbe criterion? What color is that light? What wavelength would be needed with a dry objective of NA 1.0?
8. (Medium) Normal extracellular K⁺ is 5 mM and intracellular K⁺ is 140 mM. In severe hyperkalemia, extracellular K⁺ rises to 10 mM. Calculate $E_K$ at 37 °C in both cases, and explain why hyperkalemia is dangerous for the heart.
9. (Medium) In a mitochondrion at 37 °C, the membrane potential is 160 mV (matrix negative) and the pH difference is 0.50 units (matrix alkaline). Find the proton-motive force and the free energy released per mole of protons entering the matrix. If ATP synthesis requires 52 kJ/mol, what is the minimum average number of protons that must pass per ATP? Could a mammalian ATP synthase, which uses 8/3 protons per ATP, still make ATP under these conditions?
10. (Medium) A protein is present at 100 nM in a mammalian cell of volume 2.0 pL. How many molecules of it does the cell contain?
11. (Hard) A hypothetical cell line starts with telomeres 10 kb long, loses 100 bp per division and stops dividing when its telomeres reach 4 kb. (a) How many divisions can it undergo? (b) If one cell and all its descendants completed that many doublings without any deaths, how many cells would result, and what would they weigh at 1 ng each? (c) What does this imply about whether the Hayflick limit restricts the size of a human body, and why might the limit nevertheless suppress cancer?
12. (Conceptual) Explain why a mutation in just one copy of a proto-oncogene can promote cancer, whereas both copies of a tumor suppressor gene usually need to be inactivated. Use this to explain why children who inherit one defective *RB1* allele often develop retinoblastoma in both eyes at an early age.

### Solutions

**1.** The Abbe limit for the best light microscopes is about $\lambda/(2\,\text{NA}) \approx 550/(2\times1.4) \approx 200$ nm, eight times larger than the ribosome. Magnification only enlarges the blurred image; it cannot add detail that the optics never captured (empty magnification). Electrons accelerated through 100–300 kV have wavelengths of a few picometres, so a transmission electron microscope — or, for molecular detail, cryo-electron microscopy — resolves ribosomes easily. **Answer:** the ribosome is far below the ~200 nm diffraction limit; use an electron microscope.

**2.**
1. For a cube of side $a$: $A/V = 6a^2/a^3 = 6/a$.
2. $a = 1\ \mu$m: $A/V = 6\ \mu\text{m}^{-1}$; $a = 10\ \mu$m: $A/V = 0.6\ \mu\text{m}^{-1}$. Ratio: 10.
3. Number of small cubes: $(10/1)^3 = 1000$.
4. Total area: $1000\times6\ \mu\text{m}^2 = 6000\ \mu\text{m}^2$, versus $6\times10^2 = 600\ \mu\text{m}^2$ for the large cube.

**Answer:** the small cube has 10 times the $A/V$; dividing the large cube into 1000 small ones multiplies the total surface by 10 with no change in volume — the geometric logic of cell division.

**3.**
1. Number of generations: $6\ \text{h}/0.5\ \text{h} = 12$.
2. $N = 100\times2^{12} = 100\times4096 = 409\,600$.

**Answer:** about $4.1\times10^5$ cells.

**4.**
1. Mitotic index: $f_M = 30/600 = 0.050$.
2. (a) Naive: $t_M = 0.050\times20 = 1.0$ h.
3. (b) Corrected: $t_M = T\log_2(1 + f_M) = 20\log_2(1.05) = 20\times0.0704 = 1.41$ h.

**Answer:** (a) 1.0 h; (b) about 1.4 h. The correction matters because a growing population contains more young (G₁) cells than old (M) cells.

**5.**
1. (a) 0.30 M sucrose is 0.30 osmol/L of an impermeant solute, the same as the cytoplasm: the solution is **isotonic**; cell volume is unchanged.
2. (b) 0.30 M NaCl gives about 0.60 osmol/L (two ions per formula unit): **hypertonic**. Water leaves and the cells shrink and crenate.
3. (c) 0.10 M NaCl gives about 0.20 osmol/L: **hypotonic**. Water enters; the cells swell and many burst (hemolysis).
4. (d) 0.30 M urea is isosmotic with the cytoplasm, but urea crosses the membrane. As urea enters, the internal osmolarity rises, water follows, and the cells swell and eventually lyse. The solution is **hypotonic** despite being isosmotic.

**Answer:** (a) no change; (b) shrinkage; (c) swelling and lysis; (d) gradual swelling and lysis — tonicity depends only on impermeant solutes.

**6.**
1. $\theta = [L]/([L] + K_d) = 1.0/(1.0 + 5.0) = 0.167$.
2. For $\theta = 0.75$: $[L] = 0.75([L] + K_d) \Rightarrow 0.25[L] = 0.75K_d \Rightarrow [L] = 3K_d = 15$ nM.

**Answer:** about 17% occupancy at 1.0 nM; 15 nM gives 75%.

**7.**
1. Abbe: $d = \lambda/(2\,\text{NA})$, so $\lambda_{\max} = 2\,\text{NA}\,d = 2\times1.4\times150\ \text{nm} = 420$ nm.
2. 420 nm is violet light, at the short-wavelength end of the visible spectrum.
3. With NA 1.0: $\lambda_{\max} = 2\times1.0\times150 = 300$ nm, which is ultraviolet — invisible to the eye and absorbed by ordinary glass optics.

**Answer:** about 420 nm (violet) with NA 1.4; 300 nm (ultraviolet) with NA 1.0. This is why high-resolution work uses short wavelengths and oil immersion.

**8.**
1. At 37 °C, $RT/F = 26.7$ mV.
2. Normal: $E_K = 26.7\ln(5/140) = 26.7\times(-3.33) = -89$ mV.
3. Hyperkalemia: $E_K = 26.7\ln(10/140) = 26.7\times(-2.64) = -70.5$ mV.

**Answer:** $E_K$ rises from about −89 mV to about −71 mV. Because the resting potential tracks $E_K$, heart-muscle cells become partially depolarized. Sustained depolarization inactivates the voltage-gated Na⁺ channels needed to fire action potentials, slowing conduction and risking dangerous arrhythmias or cardiac arrest. (For the same reason, potassium chloride must never be injected rapidly.)

**9.**
1. $2.303RT/F = 61.5$ mV at 37 °C.
2. $\Delta p = 160 + 61.5\times0.50 = 160 + 30.8 = 190.8$ mV.
3. Energy per mole of H⁺: $F\Delta p = 96\,485\times0.1908 = 1.84\times10^4$ J/mol $= 18.4$ kJ/mol.
4. Minimum protons: $52/18.4 = 2.8$ per ATP.
5. A c8-ring synthase delivers $(8/3)\times18.4 = 49.1$ kJ per mole of ATP, less than the 52 kJ/mol required.

**Answer:** $\Delta p \approx 191$ mV; about 18.4 kJ/mol; at least 2.8 protons per ATP. With only 2.67 protons per ATP, net synthesis would stall: ATP would accumulate only until the cytosolic ATP/ADP ratio fell to the point where making ATP costs about 49 kJ/mol. A cell must therefore keep $\Delta p$ high enough for the ATP/ADP ratio it needs.

**10.**
1. $V = 2.0\ \text{pL} = 2.0\times10^{-12}$ L.
2. $N = cVN_A = (100\times10^{-9})(2.0\times10^{-12})(6.022\times10^{23}) = 1.2\times10^5$.

**Answer:** about 120 000 molecules — enough that random fluctuations in number are small (of order $\sqrt{N}/N \approx 0.3\%$), in contrast to the few-copy proteins of Worked Example 3.1.

**11.**
1. (a) Telomere that can be lost: $10\,000 - 4000 = 6000$ bp. Divisions: $6000/100 = 60$.
2. (b) Cells: $2^{60} = 1.15\times10^{18}$. Mass: $1.15\times10^{18}\times10^{-9}\ \text{g} = 1.15\times10^9$ g $= 1.15\times10^6$ kg, about 1150 tonnes.
3. (c) A human body has only about $3\times10^{13}$ cells ($2^{45}$), so a 60-division limit does not, by itself, limit body size; the real constraint is that stem-cell lineages must last a lifetime while dividing repeatedly. The limit does restrict a *rogue* lineage: a cell that starts dividing uncontrollably runs out of telomere before it can accumulate the many further mutations needed for full malignancy, unless it reactivates telomerase — which most cancers do.

**Answer:** (a) 60 divisions; (b) about $1.2\times10^{18}$ cells weighing about $1.2\times10^6$ kg; (c) the Hayflick limit is not a body-size limit but acts as a brake on runaway clones (a tumor-suppressor mechanism).

**12.** A proto-oncogene encodes an accelerator of cell division. A gain-of-function mutation (for example, a Ras protein that cannot hydrolyze its GTP) produces a protein that is active all the time, and the one mutant copy drives division regardless of the normal copy — the effect is dominant. A tumor suppressor encodes a brake. If one copy is lost, the remaining normal copy usually still makes enough protein to restrain division, so loss of function is recessive at the cellular level, and both copies must be inactivated. A child who inherits one defective *RB1* allele has the "first hit" in every cell of the body, including all retinal cells. Only one more somatic mutation in any of the millions of dividing retinal precursor cells is then needed, which is likely to happen several times, so tumors often arise in both eyes and early in childhood. In children without an inherited mutation, both hits must occur in the same cell, which is rare, so their retinoblastoma is usually in one eye and appears later. **Answer:** oncogene mutations are dominant gain-of-function; tumor-suppressor mutations are recessive loss-of-function at the cellular level, and an inherited first hit makes the required second hit likely in many cells — Knudson's two-hit hypothesis.

## 16. Summary and Key Equations

| Organelle | Main function |
|---|---|
| Nucleus | DNA storage, transcription, ribosome assembly (nucleolus) |
| Ribosome | Protein synthesis |
| Rough ER | Synthesis and folding of secreted/membrane proteins |
| Smooth ER | Lipid synthesis, detoxification, Ca²⁺ storage |
| Golgi | Modification, sorting, packaging |
| Lysosome | Intracellular digestion, autophagy |
| Mitochondrion | Aerobic respiration, ATP production by chemiosmosis |
| Chloroplast | Photosynthesis |
| Peroxisome | Oxidation reactions, H₂O₂ breakdown |
| Cytoskeleton | Shape, transport, movement, division |
| Plasma membrane | Selective barrier, signaling, transport |
| Cell wall | Support and protection (plants, fungi, bacteria) |
| Vacuole | Storage, turgor (plants) |

**Key ideas.**
- Cells are small because $A/V$ falls as $1/r$ and diffusion time grows as $x^2$; large cells compensate with flat or elongated shapes, internal membranes and motor-driven transport.
- Light microscopes resolve about 200 nm; electron microscopes, with picometre wavelengths, resolve far more but are limited by lens aberrations and radiation damage.
- Prokaryotes lack a nucleus and membrane-bound organelles; eukaryotes compartmentalize their functions, and their mitochondria and chloroplasts descend from bacterial endosymbionts.
- Membranes are fluid bilayers whose proteins control transport; osmosis and ion gradients follow from chemical and electrochemical potentials.
- Mitochondria and chloroplasts convert energy through a proton-motive force that drives the rotary ATP synthase.
- Signals are received by receptors, amplified by enzymatic cascades and switched off actively.
- **Cell cycle:** G₁ → S → G₂ → M (prophase, metaphase, anaphase, telophase) → cytokinesis; controlled by cyclins/CDKs and checkpoints; failure leads to cancer. Apoptosis removes unwanted cells; stem cells replace them.

**Key equations.**

| Quantity | Equation |
|---|---|
| Surface-to-volume ratio of a sphere | $A/V = 3/r$ |
| Mean-square displacement (1D, 3D) | $\langle x^2\rangle = 2Dt$, $\langle r^2\rangle = 6Dt$ |
| Diffusion time over distance $x$ | $t \approx x^2/(2D)$ |
| Stokes–Einstein relation | $D = k_BT/(6\pi\eta R)$ |
| Abbe resolution limit | $d = \lambda/(2\,\text{NA})$, with $\text{NA} = n\sin\alpha$ |
| Relativistic electron wavelength | $\lambda = h/\sqrt{2m_eK(1 + K/2m_ec^2)}$ |
| Sedimentation coefficient | $s = v/(\omega^2r) = m(1 - \bar v\rho)/f$ |
| Number of molecules in a volume | $N = cVN_A$ |
| Osmotic pressure (van 't Hoff) | $\Pi = cRT$ ($c$ = osmolarity) |
| Nernst potential | $E_X = (RT/zF)\ln(c_{\text{out}}/c_{\text{in}})$ |
| Proton-motive force | $\Delta p = \Delta\psi + (2.303RT/F)\,\Delta\text{pH}$; energy per mole of H⁺ $= F\Delta p$ |
| Fractional receptor occupancy | $\theta = [L]/([L] + K_d)$ |
| Exponential growth | $N = N_0\,2^{t/g} = N_0e^{kt}$, $k = \ln 2/g$ |
| Duration of M phase from mitotic index | $t_M = T\log_2(1 + f_M)$ |

**Useful constants and values.**

| Constant | Value |
|---|---|
| Avogadro constant $N_A$ | $6.022\times10^{23}\ \text{mol}^{-1}$ |
| Gas constant $R$ | $8.314\ \text{J mol}^{-1}\,\text{K}^{-1}$ |
| Faraday constant $F$ | $96\,485\ \text{C mol}^{-1}$ |
| Boltzmann constant $k_B$ | $1.381\times10^{-23}\ \text{J K}^{-1}$ |
| Planck constant $h$ | $6.626\times10^{-34}\ \text{J s}$ |
| Elementary charge $e$ | $1.602\times10^{-19}\ \text{C}$ |
| Electron mass $m_e$ | $9.109\times10^{-31}\ \text{kg}$ (rest energy 511 keV) |
| $RT/F$ at 37 °C | 26.7 mV |
| $2.303RT/F$ at 37 °C | 61.5 mV |
| Specific membrane capacitance | ~$1\ \mu\text{F cm}^{-2}$ |
| Rise per base pair in B-DNA | 0.34 nm |
| Volume of an *E. coli* cell | ~1 fL ($1\ \mu\text{m}^3$); 1 nM ≈ 0.6 molecules per cell |

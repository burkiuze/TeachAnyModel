---
title: Elasticity and the Mechanics of Materials
field: Physics
subfield: Classical Mechanics
level: high-school to undergraduate
keywords: [elasticity, stress, strain, Hooke's law, Young's modulus, shear modulus, bulk modulus, Poisson's ratio, stress-strain curve, yield strength, ultimate tensile strength, ductile fracture, brittle fracture, elastic energy, thermal stress, beam bending, second moment of area, Euler buckling, torsion, fatigue, fracture toughness, Griffith criterion, bone mechanics, tendon mechanics]
---

# Elasticity and the Mechanics of Materials

Every solid object deforms when a force acts on it. A steel bridge sags by a few centimeters when a truck crosses, a bookshelf bows under heavy books, a guitar string stretches as it is tuned, and the femur shortens by a fraction of a millimeter each time a runner's foot strikes the ground. Most of the time these deformations are small and disappear when the load is removed; occasionally they grow without limit and the object fails. Predicting how much a solid deforms, and when it will break, is the business of **elasticity** and the **mechanics of materials** (also called strength of materials).

Earlier chapters treated bodies as point masses or perfectly rigid objects. That idealization is excellent for orbits and spinning wheels, but it cannot tell an engineer how thick a cable must be, why a hollow tube is stiffer than a solid rod of the same mass, why a slender column suddenly bows sideways, or why an aircraft fuselage can crack after thousands of uneventful flights. To answer such questions we must look inside the material and describe how internal forces are distributed.

This chapter develops the subject from first principles. It defines **stress** and **strain**, introduces **Hooke's law** for materials and the four elastic constants (Young's modulus, the shear modulus, the bulk modulus and Poisson's ratio), and derives the relations among them. It then follows a material beyond the elastic range through the **stress–strain curve**: yield, strain hardening, ultimate strength, necking and the contrast between **ductile and brittle failure**. Further sections treat **elastic energy**, **thermal stress**, **bending of beams** and the **second moment of area**, **Euler buckling** of columns, **torsion** of shafts, and the basics of **fatigue and fracture mechanics**. Tables of real material properties, the history of the field, applications from bridges to bones and tendons, common misconceptions, practice problems with full solutions, and a summary of key equations complete the chapter.

## 1. Why Solids Resist Deformation

A solid is a collection of atoms held near equilibrium positions by chemical bonds. The potential energy of a pair of neighboring atoms has a minimum at the equilibrium spacing $r_0$. Near that minimum any smooth potential is approximately a parabola, so the restoring force on an atom displaced by a small amount $x$ is approximately linear:
$$F \approx -S_0\,x, \qquad S_0 = \left.\frac{d^2U}{dr^2}\right\rvert_{r_0}$$
where $S_0$ is the bond stiffness. This is the microscopic origin of Hooke's law: linear elasticity is simply the small-displacement approximation to the interatomic potential.

A rough estimate links bond stiffness to the macroscopic stiffness of a material. If a cube of material contains bonds arranged in columns with spacing $r_0$, each bond carries a force $F$ acting on an area of about $r_0^2$, and stretches by $\Delta r$ over a length $r_0$. The stress is then $F/r_0^2$ and the strain $\Delta r/r_0$, so the ratio (Young's modulus, defined below) is
$$E \approx \frac{F/r_0^2}{\Delta r/r_0} = \frac{S_0}{r_0}$$
For a metal with $r_0 \approx 0.25$ nm and $E \approx 200$ GPa, this implies $S_0 \approx 50$ N/m. Stiff covalent solids such as diamond have large $S_0$ and small $r_0$, giving very high moduli; polymers held together partly by weak van der Waals forces between chains are far more compliant.

When the displacement is no longer small, the parabolic approximation fails. Some materials then break bonds and crack (brittle behavior); others allow planes of atoms to slip past one another through the motion of crystal defects called **dislocations**, producing permanent (plastic) deformation (ductile behavior).

## 2. Stress and Strain

Forces on a solid are described not by their total size alone but by how intensely they act on internal surfaces. Deformation is described not by the total change in length but by the change relative to the original size. These normalized quantities make results independent of the size of the specimen.

### 2.1 Normal stress and normal strain

Consider a bar of original length $L_0$ and cross-sectional area $A_0$ pulled by equal and opposite forces $F$ along its axis. Imagine cutting the bar perpendicular to its axis: each half must exert a force $F$ on the other, distributed over the area of the cut. The **normal stress** is
$$\sigma = \frac{F}{A_0}$$
Its SI unit is the pascal (1 Pa = 1 N/m²); engineering stresses are usually quoted in megapascals (1 MPa = 10⁶ Pa = 1 N/mm²) or gigapascals. By convention tensile stress is positive and compressive stress negative.

If the bar lengthens by $\Delta L$, the **normal strain** is
$$\varepsilon = \frac{\Delta L}{L_0}$$
Strain is dimensionless. Elastic strains in metals and ceramics are tiny, typically below 0.5%, so they are often written in **microstrain** (1 microstrain = 10⁻⁶).

### 2.2 Shear stress and shear strain

If equal and opposite forces $F$ act parallel to opposite faces of a block of face area $A$, they tend to slide one face relative to the other. The **shear stress** is
$$\tau = \frac{F}{A}$$
The block distorts from a rectangle into a parallelogram. If the top face moves sideways by $\Delta x$ relative to the bottom, and the block has height $h$, the **shear strain** is the change in the originally right angle:
$$\gamma = \frac{\Delta x}{h} \approx \theta \quad (\text{for small angles})$$
Shear stress cannot exist on one pair of faces alone: for the block to be in rotational equilibrium, equal shear stresses must act on the perpendicular faces as well. This "complementary shear" is why a shaft in torsion can crack along a helix at 45° to its axis.

### 2.3 Volume stress and volume strain

A body immersed in a fluid experiences the same pressure $p$ on every surface. A change of pressure $\Delta p$ produces a fractional change of volume, the **volume strain** $\Delta V/V$. Since increased pressure shrinks the body, $\Delta V$ and $\Delta p$ have opposite signs.

### 2.4 Stress as a tensor

The force per area on an internal surface depends on the surface's orientation. Augustin-Louis Cauchy showed in 1822 that the state of stress at a point is specified by nine components $\sigma_{ij}$ (the $i$-component of force per unit area on a surface with normal along $j$). Rotational equilibrium makes them symmetric, $\sigma_{ij} = \sigma_{ji}$, leaving six independent components: three normal and three shear stresses. For any state of stress there are three perpendicular **principal directions** on whose planes the shear stresses vanish; the normal stresses there are the **principal stresses**. Strain is likewise a symmetric tensor. This chapter mostly uses simple states (uniaxial tension, pure shear, hydrostatic pressure).

### Worked Example 1: A steel hanger rod

A steel rod of diameter 10.0 mm and length 2.00 m hangs vertically and supports a 500 kg mass. Take $E = 200$ GPa and $g = 9.81$ m/s². Find the stress, strain and elongation, and the factor of safety against a yield strength of 250 MPa.

1. Load: $F = mg = 500 \times 9.81 = 4905$ N.
2. Area: $A = \pi (d/2)^2 = \pi (0.00500\ \text{m})^2 = 7.854 \times 10^{-5}$ m².
3. Stress: $\sigma = F/A = 4905 / 7.854\times10^{-5} = 6.245 \times 10^{7}$ Pa $= 62.5$ MPa.
4. Strain: $\varepsilon = \sigma/E = 6.245\times10^{7}/2.00\times10^{11} = 3.12\times10^{-4}$ (312 microstrain).
5. Elongation: $\Delta L = \varepsilon L_0 = 3.12\times10^{-4}\times 2.00 = 6.25 \times 10^{-4}$ m.
6. Factor of safety: $250/62.5 = 4.0$.

**Answer:** $\sigma \approx 62.5$ MPa, $\varepsilon \approx 3.1\times10^{-4}$, $\Delta L \approx 0.62$ mm, factor of safety about 4.

## 3. Hooke's Law and the Elastic Moduli

For small deformations, stress is proportional to strain. Robert Hooke stated the principle for springs in 1678 as *ut tensio, sic vis*, "as the extension, so the force". For materials the law is expressed in terms of stress and strain, with a constant of proportionality that is a property of the material alone and not of the specimen's shape.

### 3.1 Young's modulus

For uniaxial tension or compression,
$$\boxed{\sigma = E\,\varepsilon}$$
where $E$ is **Young's modulus**. Substituting the definitions gives
$$\frac{F}{A_0} = E\frac{\Delta L}{L_0} \quad\Longrightarrow\quad F = \frac{EA_0}{L_0}\,\Delta L = k\,\Delta L$$
so a bar behaves as a spring with stiffness $k = EA_0/L_0$. Doubling the length halves the stiffness; doubling the area doubles it. The rod in Worked Example 1 has $k = 7.85\times10^{6}$ N/m.

### 3.2 Shear modulus

For shear,
$$\boxed{\tau = G\,\gamma}$$
where $G$ is the **shear modulus** (modulus of rigidity). Fluids at rest cannot sustain shear stress, so $G = 0$ for any fluid; a nonzero shear modulus is what makes a solid a solid.

### 3.3 Bulk modulus

For uniform pressure,
$$\boxed{\Delta p = -K\,\frac{\Delta V}{V}}$$
where $K$ is the **bulk modulus**. Its reciprocal $\kappa = 1/K$ is the **compressibility**. Both solids and fluids have bulk moduli. For a gas, $K$ depends on the process: it equals $p$ for isothermal compression of an ideal gas and $\gamma p$ for adiabatic compression, where $\gamma$ is the heat-capacity ratio.

### 3.4 Poisson's ratio

A bar stretched along its axis becomes thinner. If the axial strain is $\varepsilon_{\text{axial}}$ and the transverse strain is $\varepsilon_{\text{lat}}$, **Poisson's ratio** is
$$\nu = -\frac{\varepsilon_{\text{lat}}}{\varepsilon_{\text{axial}}}$$
The minus sign makes $\nu$ positive for ordinary materials. Most metals have $\nu \approx 0.3$, rubber is very close to 0.5, cork is close to 0, and specially engineered **auxetic** foams and lattices have negative values: they get fatter when stretched.

Poisson's ratio determines whether the volume changes in tension. For a bar of square cross-section of side $a$ and length $L$, after deformation the volume is $V' = L(1+\varepsilon)\,a^2(1-\nu\varepsilon)^2$. Keeping only first-order terms in the small strain,
$$\frac{\Delta V}{V} = (1+\varepsilon)(1-\nu\varepsilon)^2 - 1 \approx \varepsilon(1-2\nu)$$
A material with $\nu = 0.5$ is therefore incompressible, and one with $\nu < 0.5$ increases its volume slightly when pulled.

### 3.5 The generalized Hooke's law

For an **isotropic** material (one whose properties are the same in every direction), each normal stress produces a direct strain along its own axis and Poisson contractions along the other two. Superposing the three effects,
$$\varepsilon_x = \frac{1}{E}\left[\sigma_x - \nu(\sigma_y + \sigma_z)\right], \quad \varepsilon_y = \frac{1}{E}\left[\sigma_y - \nu(\sigma_z + \sigma_x)\right], \quad \varepsilon_z = \frac{1}{E}\left[\sigma_z - \nu(\sigma_x + \sigma_y)\right]$$
and each shear stress produces only its own shear strain, $\gamma_{xy} = \tau_{xy}/G$ and so on. A remarkable consequence of isotropy is that only **two** of the four constants $E, G, K, \nu$ are independent. Anisotropic materials need more: wood, bone and fiber composites have different moduli along and across the grain, and the most general linear elastic crystal requires 21 independent constants.

### 3.6 Deriving the relations among the moduli

**Bulk modulus.** Apply a uniform pressure $p$ to a cube, so $\sigma_x = \sigma_y = \sigma_z = -p$. The generalized Hooke's law gives each strain as
$$\varepsilon_x = \frac{1}{E}\left[-p - \nu(-p - p)\right] = -\frac{p(1-2\nu)}{E}$$
For small strains the volume strain is the sum of the three normal strains, so
$$\frac{\Delta V}{V} = \varepsilon_x + \varepsilon_y + \varepsilon_z = -\frac{3p(1-2\nu)}{E}$$
Comparing with $p = -K\,\Delta V/V$ yields
$$\boxed{K = \frac{E}{3(1-2\nu)}}$$
A stable material must have $K > 0$, so $\nu < 1/2$. As $\nu \to 1/2$ the bulk modulus becomes much larger than $E$, which is the case for rubber.

**Shear modulus.** Consider a square element in **pure shear** with shear stress $\tau$ on its faces. Cutting the square along its diagonal and balancing forces shows that the faces of a square rotated by 45° carry no shear but carry normal stresses $\sigma_1 = +\tau$ (tension along one diagonal) and $\sigma_2 = -\tau$ (compression along the other). By the generalized Hooke's law, the strain along the tension diagonal is
$$\varepsilon_1 = \frac{1}{E}\left[\sigma_1 - \nu\sigma_2\right] = \frac{\tau(1+\nu)}{E}$$
Geometry links this to the shear strain. When a unit square shears through a small angle $\gamma$, its diagonal (original length $\sqrt{2}$) lengthens by $\gamma/\sqrt{2}$ to first order, so the diagonal strain is $\varepsilon_1 = \gamma/2$. Equating the two expressions,
$$\frac{\gamma}{2} = \frac{\tau(1+\nu)}{E} \quad\Longrightarrow\quad \boxed{G = \frac{\tau}{\gamma} = \frac{E}{2(1+\nu)}}$$
Requiring $G > 0$ gives $\nu > -1$. So for any stable isotropic material, $-1 < \nu < 1/2$. For a typical metal with $\nu = 0.3$, $G \approx 0.38E$ and $K \approx 0.83E$.

### Worked Example 2: Poisson contraction of an aluminum rod

An aluminum alloy rod (6061-T6, $E = 68.9$ GPa, $\nu = 0.33$) has diameter 20.0 mm and length 1.50 m and carries a tensile force of 30.0 kN. Find the elongation, the change in diameter and the change in volume.

1. Area: $A = \pi(0.0100)^2 = 3.142\times10^{-4}$ m².
2. Stress: $\sigma = 30.0\times10^{3}/3.142\times10^{-4} = 9.55\times10^{7}$ Pa $= 95.5$ MPa (well below the 276 MPa yield strength, so Hooke's law applies).
3. Axial strain: $\varepsilon = 9.55\times10^{7}/6.89\times10^{10} = 1.386\times10^{-3}$.
4. Elongation: $\Delta L = 1.386\times10^{-3}\times1.50 = 2.08\times10^{-3}$ m $= 2.08$ mm.
5. Lateral strain: $\varepsilon_{\text{lat}} = -\nu\varepsilon = -0.33\times1.386\times10^{-3} = -4.57\times10^{-4}$.
6. Change in diameter: $\Delta d = -4.57\times10^{-4}\times 20.0$ mm $= -9.1\times10^{-3}$ mm.
7. Volume strain: $\Delta V/V = \varepsilon(1-2\nu) = 1.386\times10^{-3}\times0.34 = 4.71\times10^{-4}$. With $V = AL = 4.712\times10^{-4}$ m³, $\Delta V = 2.2\times10^{-7}$ m³.

**Answer:** the rod lengthens by about 2.1 mm, its diameter shrinks by about 9 micrometers, and its volume increases by about 0.22 cm³.

### Worked Example 3: Squeezing a steel sphere in the deep ocean

A solid steel sphere of radius 10.0 cm ($K = 160$ GPa) is lowered to a depth of 4000 m in seawater of density 1025 kg/m³. By how much does its radius shrink? Compare with the volume change of seawater, taking $K \approx 2.2$ GPa.

1. Pressure increase: $\Delta p = \rho g h = 1025\times9.81\times4000 = 4.02\times10^{7}$ Pa (about 40 MPa, roughly 400 atmospheres).
2. Volume strain of steel: $\Delta V/V = -\Delta p/K = -4.02\times10^{7}/1.60\times10^{11} = -2.51\times10^{-4}$.
3. For a sphere $V \propto R^3$, so $\Delta R/R = \frac{1}{3}\Delta V/V = -8.38\times10^{-5}$.
4. Radius change: $\Delta R = -8.38\times10^{-5}\times0.100$ m $= -8.4\times10^{-6}$ m.
5. For water the same pressure gives $\Delta V/V \approx -4.02\times10^{7}/2.2\times10^{9} = -1.8\%$ (an estimate, since water stiffens slightly as it is compressed).

**Answer:** the sphere's radius shrinks by about 8 micrometers, while seawater at that depth is compressed by roughly 2%, about 70 times more than steel.

## 4. Real Material Properties

The tables below give representative room-temperature values. Material properties depend on composition, processing, temperature, moisture and (for anisotropic materials) direction, so values for a particular product can differ from these; engineering design always uses data for the specific grade.

**Table 1. Elastic constants (typical values)**

| Material | Young's modulus $E$ (GPa) | Shear modulus $G$ (GPa) | Poisson's ratio $\nu$ |
|---|---|---|---|
| Structural steel | 200 | 78 | 0.29 |
| Aluminum alloy 6061-T6 | 69 | 26 | 0.33 |
| Copper | 110–130 | 44 | 0.34 |
| Titanium alloy Ti-6Al-4V | 114 | 44 | 0.34 |
| Tungsten | 411 | 161 | 0.28 |
| Soda-lime glass | 72 | 30 | 0.22 |
| Fused silica | 73 | 31 | 0.17 |
| Diamond | 1050–1200 | — | 0.1–0.2 |
| Concrete | 25–40 | — | 0.1–0.2 |
| Softwood, along grain (e.g. Douglas fir) | 10–14 | — | — |
| Human cortical bone, along long axis | 17–20 | — | about 0.3 |
| Tendon, along fibers | 1–2 | — | — |
| Nylon 6,6 | 2–4 | — | 0.39–0.41 |
| Natural rubber (small strains) | 0.001–0.01 | — | about 0.5 |
| Spider dragline silk | about 10 | — | — |

**Table 2. Strength and density (typical values; tensile unless stated)**

| Material | Yield strength (MPa) | Ultimate strength (MPa) | Elongation at break | Density (kg/m³) |
|---|---|---|---|---|
| Structural steel (ASTM A36) | 250 | 400–550 | about 20% | 7850 |
| Aluminum alloy 6061-T6 | 276 | 310 | 12–17% | 2700 |
| Annealed copper | about 70 | about 220 | about 45% | 8960 |
| Ti-6Al-4V (annealed) | 880 | 950 | about 14% | 4430 |
| Soda-lime glass (ordinary objects) | — | about 30–100, flaw dependent | ≈ 0 | 2500 |
| Concrete | — | 2–5 tension; 20–40 compression | ≈ 0 | 2400 |
| Human femoral cortical bone | — | about 133 tension; 193 compression; 68 shear | about 2–3% | about 1900 |
| Tendon | — | 50–150 | of order 10% | — |
| Spider dragline silk | — | about 1100 | about 27% | — |

**Table 3. Bulk moduli and linear thermal expansion coefficients**

| Material | Bulk modulus $K$ (GPa) | Thermal expansion $\alpha$ (10⁻⁶ K⁻¹) |
|---|---|---|
| Steel | about 160 | 12 (stainless 304: about 17) |
| Aluminum | about 76 | 23 |
| Copper | about 140 | 17 |
| Soda-lime glass | about 43 | 9 |
| Borosilicate glass | — | 3.3 |
| Fused silica | — | 0.55 |
| Invar (Fe–36% Ni) | — | about 1.2 |
| Concrete | — | 10–12 |
| Diamond | 443 | about 1 |
| Water (20 °C) | 2.2 | — |
| Air, 1 atm (adiabatic) | 1.42×10⁻⁴ | — |

Two features of these tables are worth noticing. First, the moduli span more than six orders of magnitude, from rubber to diamond. Second, the strengths of metals are only about 0.1–1% of their moduli, far below the "theoretical" strength of roughly $E/10$ that would be needed to pull perfect planes of atoms apart; Section 11 explains why.

## 5. The Stress–Strain Curve, Yield and Failure

### 5.1 Anatomy of a tensile test

The most important single experiment in materials testing is the **tensile test**. A specimen with a carefully machined gauge section is pulled at a slow, steady rate while the force and the elongation of the gauge length are recorded. Plotting engineering stress $F/A_0$ against engineering strain $\Delta L/L_0$ gives the stress–strain curve. For a ductile metal such as mild steel the curve shows these stages:

1. **Linear elastic region.** Stress is proportional to strain; the slope is $E$. The end of the straight portion is the **proportional limit**.
2. **Elastic limit.** The largest stress after which the specimen returns completely to its original length. For metals it is close to the proportional limit.
3. **Yielding.** Beyond the elastic limit, dislocations move in large numbers and the material deforms plastically. Annealed mild steel often shows a distinct **upper yield point** followed by a plateau at a lower yield stress. Most other metals yield gradually, so the **yield strength** $\sigma_y$ is defined by the **0.2% offset method**: draw a line parallel to the elastic part, starting at a strain of 0.002, and take the stress where it meets the curve. Unloading from the plastic region follows a line of slope $E$, leaving a permanent strain.
4. **Strain hardening.** Continued plastic deformation multiplies and tangles dislocations, so ever higher stress is needed to keep deforming the metal.
5. **Ultimate tensile strength (UTS).** The maximum engineering stress $\sigma_u = F_{\max}/A_0$.
6. **Necking.** After the UTS, deformation concentrates in one region that thins rapidly. The force needed to continue falls, so the engineering stress decreases.
7. **Fracture.** The neck finally separates, often with a characteristic "cup and cone" surface.

Two measures of ductility come from the broken specimen: the **percent elongation** $(L_f - L_0)/L_0$ and the **reduction of area** $(A_0 - A_f)/A_0$.

### 5.2 Engineering versus true stress

Engineering stress divides by the original area $A_0$, but the actual area shrinks as the specimen stretches. The **true stress** is $\sigma_t = F/A$. Plastic deformation conserves volume to a good approximation, so $AL = A_0L_0$ and
$$\sigma_t = \frac{F}{A} = \frac{F}{A_0}\frac{L}{L_0} = \sigma(1+\varepsilon)$$
The **true strain** adds up small increments, each relative to the current length:
$$\varepsilon_t = \int_{L_0}^{L}\frac{dL'}{L'} = \ln\frac{L}{L_0} = \ln(1+\varepsilon)$$
For small strains $\varepsilon_t \approx \varepsilon$ and $\sigma_t \approx \sigma$; the distinction matters only in the plastic range. These relations hold up to the onset of necking, after which the strain is no longer uniform along the gauge length and the true stress must be found from the measured neck area.

### 5.3 Necking: the Considère criterion

Why does necking begin at the maximum load? The force is $F = \sigma_t A$. At the maximum, $dF = 0$:
$$dF = A\,d\sigma_t + \sigma_t\,dA = 0 \quad\Longrightarrow\quad \frac{d\sigma_t}{\sigma_t} = -\frac{dA}{A}$$
With volume conservation, $-dA/A = dL/L = d\varepsilon_t$. Therefore necking starts when
$$\frac{d\sigma_t}{d\varepsilon_t} = \sigma_t$$
In words: as long as strain hardening raises the strength faster than the shrinking area raises the stress, any slightly thinner region hardens and the deformation spreads out. Once hardening can no longer keep up, a thin region becomes ever thinner. This argument was published by the French engineer Armand Considère in 1885.

### 5.4 Ductile versus brittle behavior

A **ductile** material (mild steel, copper, aluminum alloys, most polymers above their glass transition) undergoes large plastic deformation before fracture. It absorbs a great deal of energy, gives visible warning (bending, necking) before collapse, and tolerates small cracks because plastic flow blunts their tips.

A **brittle** material (glass, ceramics, cast iron, concrete, chalk) shows little or no plastic deformation. The stress–strain curve is nearly linear up to sudden fracture, the fracture surface is flat and often shows the origin of the crack, and the strength is scattered because it depends on the largest flaw present. Brittle materials are typically much stronger in compression than in tension, because compression tends to close cracks rather than open them; this is why concrete is reinforced with steel bars wherever tension can occur.

The distinction depends on conditions as well as on the material. Many steels with a body-centered cubic crystal structure change from ductile to brittle below a **ductile-to-brittle transition temperature**, high loading rates and thick sections favor brittle fracture, and some polymers are brittle when cold but ductile when warm.

### 5.5 Toughness, resilience and safety factors

The work done per unit volume to deform a material is the area under its stress–strain curve, $\int\sigma\,d\varepsilon$. The area up to fracture is the **toughness** (strictly the tensile toughness, in J/m³). The elastic energy per unit volume stored at the yield point is the **modulus of resilience**, $\sigma_y^2/(2E)$ (derived in Section 6). Glass is strong and stiff but has very low toughness; mild steel has moderate strength but high toughness.

Engineers rarely allow stresses close to failure. A **factor of safety** $n$ sets an allowable stress $\sigma_{\text{allow}} = \sigma_y/n$ (or $\sigma_u/n$ for brittle materials). It is as low as about 1.5 in weight-critical aerospace structures with well-controlled loads and higher where loads are uncertain or failure would be catastrophic.

### Worked Example 4: Analyzing a tensile test

A steel specimen of diameter 12.5 mm and gauge length 50.0 mm reaches a 0.2% offset yield load of 30.7 kN and a maximum load of 51.5 kN, at which the engineering strain is 0.18. After fracture the gauge length is 61.5 mm and the neck diameter is 7.5 mm. Find the yield strength, UTS, percent elongation, reduction of area, and the true stress and true strain at maximum load.

1. Original area: $A_0 = \pi(6.25\ \text{mm})^2 = 122.7$ mm².
2. Yield strength: $\sigma_y = 30\,700/122.7 = 250$ MPa (since 1 N/mm² = 1 MPa).
3. UTS: $\sigma_u = 51\,500/122.7 = 420$ MPa.
4. Elongation: $(61.5 - 50.0)/50.0 = 0.23$, or 23%.
5. Reduction of area: $1 - (7.5/12.5)^2 = 1 - 0.36 = 0.64$, or 64%.
6. True stress at maximum load: $\sigma_t = \sigma_u(1+\varepsilon) = 420\times1.18 = 495$ MPa.
7. True strain at maximum load: $\varepsilon_t = \ln(1.18) = 0.166$.

**Answer:** $\sigma_y \approx 250$ MPa, UTS $\approx 420$ MPa, elongation 23%, reduction of area 64%; at maximum load the true stress is about 495 MPa and the true strain 0.166. The large reduction of area marks this as a ductile steel.

## 6. Elastic Potential Energy

Stretching an elastic bar requires work, which is stored as **elastic potential energy** and released when the load is removed. While the bar is being stretched from $0$ to $\Delta L$, the force at extension $x$ is $F(x) = kx$ with $k = EA/L$. The work done is
$$U = \int_0^{\Delta L} kx\,dx = \frac{1}{2}k(\Delta L)^2 = \frac{1}{2}F\,\Delta L$$
where $F$ is the final force. The factor $\frac{1}{2}$ appears because the force grows from zero to $F$ during the stretch. Dividing by the volume $V = AL$ gives the **energy density** (energy per unit volume):
$$u = \frac{U}{AL} = \frac{1}{2}\frac{F}{A}\frac{\Delta L}{L} = \frac{1}{2}\sigma\varepsilon = \frac{\sigma^2}{2E} = \frac{1}{2}E\varepsilon^2$$
The same argument for shear gives $u = \tau^2/(2G)$. Because $u \propto \sigma^2/E$, a material that can safely reach a high stress with a low modulus stores the most energy per unit volume. This is why springs are made of high-strength spring steel, why archery bows use materials with high strength-to-stiffness ratios, and why tendons make excellent biological springs.

Real materials do not return all of the stored energy. Loading and unloading curves form a **hysteresis loop**, and the area inside the loop is dissipated as heat. Rubber used in vibration mounts is chosen partly for its large hysteresis; tendons, by contrast, return most of the stored energy (typically around 90%).

### Worked Example 5: Energy stored in an Achilles tendon

Model an Achilles tendon as a uniform elastic strip of length 0.25 m and cross-sectional area 80 mm², with $E = 1.5$ GPa. During running it carries a peak force of 4.0 kN. Find the stress, strain, elongation and stored energy. (These are illustrative round numbers of realistic magnitude.)

1. Stress: $\sigma = 4.0\times10^{3}/80\times10^{-6} = 5.0\times10^{7}$ Pa $= 50$ MPa.
2. Strain: $\varepsilon = 5.0\times10^{7}/1.5\times10^{9} = 0.033$ (3.3%).
3. Elongation: $\Delta L = 0.033\times0.25 = 8.3\times10^{-3}$ m.
4. Stored energy: $U = \frac{1}{2}F\Delta L = 0.5\times4000\times0.0083 = 17$ J.
5. Check with the energy density: $u = \sigma^2/(2E) = (5.0\times10^{7})^2/(3.0\times10^{9}) = 8.3\times10^{5}$ J/m³, and $uV = 8.3\times10^{5}\times(80\times10^{-6}\times0.25) = 17$ J.

**Answer:** the tendon stretches by about 8 mm and stores about 17 J per stride, most of which is returned during push-off. For comparison, structural steel loaded to its yield strength stores only $(250\times10^{6})^2/(2\times200\times10^{9}) = 1.6\times10^{5}$ J/m³, about one-fifth of the tendon's energy density in this example.

## 7. Thermal Stress

Most solids expand when heated. A free bar of length $L$ heated by $\Delta T$ lengthens by $\Delta L = \alpha L\,\Delta T$, where $\alpha$ is the coefficient of linear thermal expansion; the **thermal strain** is $\alpha\,\Delta T$. A free bar develops no stress. Stress arises only when the expansion is prevented.

**Derivation.** Suppose the bar is fixed between rigid walls, so its total length cannot change. The total strain is the sum of a mechanical part (from stress) and a thermal part:
$$\varepsilon_{\text{total}} = \frac{\sigma}{E} + \alpha\,\Delta T = 0 \quad\Longrightarrow\quad \boxed{\sigma = -E\alpha\,\Delta T}$$
Heating ($\Delta T > 0$) produces compression; cooling produces tension. Notice that the stress does not depend on the length or cross-section of the bar. A thin plate restrained in both in-plane directions develops a larger stress, $\sigma = -E\alpha\,\Delta T/(1-\nu)$, because the Poisson effect of each stress adds to the restraint in the other direction.

Thermal stresses explain a wide range of phenomena. Bridges and long pipelines have expansion joints. Ordinary glass cracks when hot liquid is poured into a cold glass because the inner surface expands while the outer surface does not; borosilicate glass, with about one-third the expansion coefficient, tolerates such shocks much better. **Tempered glass** is made by cooling the surfaces of hot glass rapidly with air jets; the interior, which cools and contracts last, pulls the solidified surfaces into compression, so a crack must overcome this built-in compression before it can grow. A **bimetallic strip** bends when heated because its two bonded layers expand by different amounts. Reinforced concrete works partly because steel and concrete have nearly equal expansion coefficients, so temperature changes do not tear them apart.

### Worked Example 6: Continuously welded rail

Modern railway track uses continuously welded rail that is anchored so that it cannot expand. A steel rail ($E = 200$ GPa, $\alpha = 12\times10^{-6}$ K⁻¹, cross-sectional area about 76.7 cm²) is installed stress-free and later heats by 35 K on a summer day. Find the stress and the axial force. How much would a free 25 m rail expand under the same heating?

1. Thermal stress: $\sigma = -E\alpha\,\Delta T = -2.00\times10^{11}\times12\times10^{-6}\times35 = -8.4\times10^{7}$ Pa $= -84$ MPa (compressive).
2. Axial force: $F = \sigma A = 8.4\times10^{7}\times76.7\times10^{-4} = 6.44\times10^{5}$ N, about 644 kN.
3. Free expansion: $\Delta L = \alpha L\,\Delta T = 12\times10^{-6}\times25\times35 = 1.05\times10^{-2}$ m.

**Answer:** the rail carries about 84 MPa of compression, an axial force of roughly 640 kN (the weight of about 65 tonnes), whereas a free 25 m rail would grow by about 10.5 mm. If the track's lateral restraint is inadequate, such forces can make the rail buckle sideways ("sun kinks"), which is why rail is laid at a carefully chosen neutral temperature and tightly anchored.

## 8. Bending of Beams

A **beam** is a long member loaded perpendicular to its axis: a floor joist, a shelf, an aircraft wing spar, a diving board or a long bone. Loads produce internal **bending moments** $M$ and **shear forces** $V$ that vary along the beam. The central result of beam theory is that the stress produced by a bending moment depends on how the cross-sectional area is distributed, captured by the **second moment of area**.

### 8.1 Pure bending and the flexure formula

The classical **Euler–Bernoulli** theory rests on three assumptions: plane cross-sections remain plane and perpendicular to the deformed axis; the material obeys Hooke's law; and deflections are small.

Consider a short segment of beam bent by a constant moment into a circular arc of radius $R$. Fibers on the outer side of the curve stretch, fibers on the inner side shorten, and somewhere between lies a **neutral surface** that keeps its length. A fiber at distance $y$ from the neutral surface, measured toward the center of curvature, follows an arc of radius $R - y$. A segment that subtends an angle $d\theta$ has neutral length $R\,d\theta$, while the fiber's length is $(R - y)\,d\theta$. The strain is therefore
$$\varepsilon = \frac{(R-y)\,d\theta - R\,d\theta}{R\,d\theta} = -\frac{y}{R}$$
Strain varies linearly across the section. By Hooke's law the stress is
$$\sigma = -\frac{E\,y}{R}$$
**Locating the neutral axis.** With no axial load, the net force on the cross-section must be zero:
$$\int_A \sigma\,dA = -\frac{E}{R}\int_A y\,dA = 0 \quad\Longrightarrow\quad \int_A y\,dA = 0$$
This is exactly the condition that $y$ is measured from the **centroid**. The neutral axis passes through the centroid of the section.

**Moment–curvature relation.** The stresses produce a moment about the neutral axis that must equal the applied moment $M$:
$$M = -\int_A y\,\sigma\,dA = \frac{E}{R}\int_A y^2\,dA = \frac{EI}{R}$$
where
$$I = \int_A y^2\,dA$$
is the **second moment of area** (often loosely called the area moment of inertia). The product $EI$ is the **flexural rigidity**. Eliminating $R$ between the two results gives the **flexure formula**:
$$\boxed{\sigma = -\frac{M\,y}{I}, \qquad \lvert\sigma\rvert_{\max} = \frac{M\,c}{I} = \frac{M}{S}}$$
where $c$ is the distance from the neutral axis to the outermost fiber and $S = I/c$ is the **section modulus**. Material far from the neutral axis carries the largest stresses and contributes most to the stiffness; material near the axis does little.

### 8.2 The second moment of area

**Rectangle** of width $b$ and depth $h$, bent about its horizontal centroidal axis: a strip of thickness $dy$ at height $y$ has area $b\,dy$, so
$$I = \int_{-h/2}^{h/2} y^2\,b\,dy = b\left[\frac{y^3}{3}\right]_{-h/2}^{h/2} = \frac{bh^3}{12}$$
Depth enters as the cube. A plank standing on edge is far stiffer than the same plank lying flat.

**Solid circle** of radius $r$: the **polar** second moment about the center is $J = \int \rho^2\,dA = \int_0^r \rho^2\,(2\pi\rho\,d\rho) = \pi r^4/2$. By the perpendicular axis theorem $J = I_x + I_y$, and by symmetry $I_x = I_y$, so $I = \pi r^4/4$.

**Parallel axis theorem.** For an axis parallel to a centroidal axis at distance $d$, $I = I_c + Ad^2$. This shows why an **I-beam** is efficient: its two flanges sit far from the neutral axis, contributing large $Ad^2$ terms, while the thin web holds them apart and carries shear.

**Table 4. Second moments of area and standard beam results**

| Cross-section or case | Formula |
|---|---|
| Rectangle $b\times h$ (about centroidal axis parallel to $b$) | $I = bh^3/12$ |
| Solid circle, radius $r$ | $I = \pi r^4/4$, $J = \pi r^4/2$ |
| Hollow circle, radii $r_o$, $r_i$ | $I = \pi(r_o^4 - r_i^4)/4$, $J = \pi(r_o^4 - r_i^4)/2$ |
| Cantilever, end load $F$, length $L$: tip deflection | $\delta = FL^3/(3EI)$ |
| Cantilever, uniform load $w$ per length: tip deflection | $\delta = wL^4/(8EI)$ |
| Simply supported, central load $F$: midspan deflection | $\delta = FL^3/(48EI)$ |
| Simply supported, uniform load $w$: midspan deflection | $\delta = 5wL^4/(384EI)$ |

### 8.3 Beam deflection

For small slopes, the curvature of the deflected axis $w(x)$ is approximately $1/R \approx d^2w/dx^2$. Combining with $M = EI/R$ gives the **Euler–Bernoulli beam equation**:
$$EI\,\frac{d^2w}{dx^2} = M(x)$$
(with a sign convention matching the chosen directions of $w$ and $M$).

**Derivation: cantilever with an end load.** A beam of length $L$ is clamped at $x = 0$ and carries a downward force $F$ at $x = L$. Measure $w$ downward. The bending moment at position $x$ comes from the load acting at lever arm $L - x$, and it bends the beam so that its downward slope increases along the length:
$$EI\,\frac{d^2w}{dx^2} = F(L - x)$$
Integrate once, using zero slope at the clamp, $w'(0) = 0$:
$$EI\,\frac{dw}{dx} = F\left(Lx - \frac{x^2}{2}\right)$$
Integrate again, using zero deflection at the clamp, $w(0) = 0$:
$$EI\,w = F\left(\frac{Lx^2}{2} - \frac{x^3}{6}\right)$$
At the tip, $x = L$:
$$\boxed{\delta = w(L) = \frac{FL^3}{3EI}}$$
The cube of length is striking: doubling a cantilever's length multiplies its tip deflection by eight. The maximum bending moment, $FL$, occurs at the clamp, which is where cantilevers break.

### Worked Example 7: A cantilevered aluminum bar, flat versus on edge

An aluminum alloy bar ($E = 68.9$ GPa, yield strength 276 MPa) with a 50 mm × 10 mm rectangular cross-section projects 1.20 m from a wall and carries 200 N at its free end. Compare the tip deflection and maximum stress when the bar is (a) lying flat and (b) standing on edge.

1. Maximum bending moment (at the wall): $M = FL = 200\times1.20 = 240$ N·m.
2. (a) Flat: $b = 0.050$ m, $h = 0.010$ m, so $I = bh^3/12 = 0.050\times(0.010)^3/12 = 4.17\times10^{-9}$ m⁴.
3. (a) Stress: $\sigma = Mc/I = 240\times0.0050/4.17\times10^{-9} = 2.88\times10^{8}$ Pa $= 288$ MPa, which exceeds the yield strength.
4. (a) The formula $FL^3/(3EI)$ would give $200\times1.728/(3\times6.89\times10^{10}\times4.17\times10^{-9}) = 0.40$ m, far outside the small-deflection range, and the bar would in fact yield and bend permanently.
5. (b) On edge: $b = 0.010$ m, $h = 0.050$ m, so $I = 0.010\times(0.050)^3/12 = 1.04\times10^{-7}$ m⁴, exactly 25 times larger.
6. (b) Stress: $\sigma = 240\times0.025/1.04\times10^{-7} = 5.76\times10^{7}$ Pa $= 57.6$ MPa, a safety factor of about 4.8 against yield.
7. (b) Deflection: $\delta = FL^3/(3EI) = 345.6/(3\times6.89\times10^{10}\times1.04\times10^{-7}) = 0.0161$ m.

**Answer:** lying flat, the bar would be overstressed (about 288 MPa) and would yield; on edge the same bar carries only 57.6 MPa and its tip deflects about 16 mm. Turning the section changes the stiffness by a factor of $(50/10)^2 = 25$ and the peak stress by a factor of 5.

### Worked Example 8: Why bones and bicycle frames are hollow

Compare a hollow circular tube with outer radius 14 mm and inner radius 8 mm (an idealized model of a long-bone shaft) with a solid rod of the same cross-sectional area, and hence the same mass per unit length, when both are bent by the same moment of 100 N·m.

1. Tube area: $A = \pi(14^2 - 8^2) = \pi\times132 = 414.7$ mm².
2. Solid rod with the same area: $r = \sqrt{132} = 11.49$ mm.
3. Second moments: $I_{\text{tube}} = \frac{\pi}{4}(14^4 - 8^4) = 2.70\times10^{4}$ mm⁴; $I_{\text{solid}} = \frac{\pi}{4}(11.49)^4 = 1.37\times10^{4}$ mm⁴. The tube is 1.97 times stiffer in bending.
4. Section moduli: $S_{\text{tube}} = I/c = 26\,955/14 = 1925$ mm³; $S_{\text{solid}} = 13\,685/11.49 = 1191$ mm³.
5. Peak stresses for $M = 100$ N·m $= 1.00\times10^{5}$ N·mm: $\sigma_{\text{tube}} = 10^{5}/1925 = 51.9$ MPa; $\sigma_{\text{solid}} = 10^{5}/1191 = 84.0$ MPa.

**Answer:** for the same mass, the tube is about twice as stiff and its peak bending stress is about 38% lower (52 MPa versus 84 MPa). Moving material away from the neutral axis is the most economical way to resist bending, which is why long bones, bamboo stems, bicycle frames and scaffolding poles are tubes.

## 9. Buckling of Columns

A short, stocky post loaded in compression fails by crushing when the stress reaches the compressive strength. A long, slender column fails differently: at a well-defined **critical load** far below the crushing load, it suddenly bows sideways. This **buckling** is an instability, not a strength failure, and it depends on stiffness ($E$ and $I$) rather than strength. You can see it by pressing down on a plastic ruler held vertically on a table.

### 9.1 Euler's derivation

Consider a straight column of length $L$ with pinned (free-to-rotate) ends, compressed by an axial load $P$. Suppose it has bowed slightly, with lateral deflection $w(x)$. At position $x$ the load acts with lever arm $w$, producing a bending moment $M = -Pw$ that tends to increase the bow. The beam equation gives
$$EI\,\frac{d^2w}{dx^2} = -Pw \quad\Longrightarrow\quad \frac{d^2w}{dx^2} + k^2 w = 0, \qquad k^2 = \frac{P}{EI}$$
This is the same equation as a simple harmonic oscillator, with general solution
$$w(x) = A\sin kx + B\cos kx$$
The boundary condition $w(0) = 0$ gives $B = 0$. The condition $w(L) = 0$ then requires $A\sin kL = 0$. Either $A = 0$ (the column stays straight) or
$$\sin kL = 0 \quad\Longrightarrow\quad kL = n\pi, \qquad n = 1, 2, 3, \ldots$$
A bent equilibrium shape is therefore possible only for the special loads $P = n^2\pi^2EI/L^2$. The smallest, with $n = 1$ and a half-sine shape, is **Euler's critical load**:
$$\boxed{P_{\text{cr}} = \frac{\pi^2 EI}{L^2}}$$
Below $P_{\text{cr}}$ the straight column is stable: if disturbed, it springs back. Above it, the straight shape is unstable and any small imperfection grows. Mathematically this is an **eigenvalue problem**, the same structure that appears for standing waves on a string and for energy levels in quantum mechanics.

### 9.2 End conditions and slenderness

Other end conditions change the shape of the buckled column. They are handled with an **effective length** $L_e = K_eL$, so that $P_{\text{cr}} = \pi^2EI/L_e^2$:

| End conditions | Effective length factor $K_e$ |
|---|---|
| Both ends pinned | 1.0 |
| Both ends fixed | 0.5 |
| One end fixed, one pinned | about 0.7 |
| One end fixed, one free (flagpole) | 2.0 |

Writing $I = Ar^2$, where $r = \sqrt{I/A}$ is the **radius of gyration** of the section, the critical stress is
$$\sigma_{\text{cr}} = \frac{P_{\text{cr}}}{A} = \frac{\pi^2 E}{(L_e/r)^2}$$
The ratio $L_e/r$ is the **slenderness ratio**. Euler's formula applies only when $\sigma_{\text{cr}}$ is below the yield strength; setting $\sigma_{\text{cr}} = \sigma_y$ gives the transition slenderness $\pi\sqrt{E/\sigma_y}$. Stockier columns yield or crush before they buckle, and real columns, which are never perfectly straight or centrally loaded, fail somewhat below the Euler load near the transition, which is why design codes use empirical column curves there.

### Worked Example 9: An aluminum tube column

An aluminum alloy tube ($E = 68.9$ GPa, $\sigma_y = 276$ MPa) has outer diameter 40.0 mm, wall thickness 2.0 mm and length 2.00 m, with pinned ends. Find the buckling load and compare it with the load that would cause yielding.

1. Inner diameter: $40.0 - 2\times2.0 = 36.0$ mm.
2. Second moment: $I = \frac{\pi}{64}(40^4 - 36^4) = \frac{\pi}{64}\times880\,384 = 4.32\times10^{4}$ mm⁴ $= 4.32\times10^{-8}$ m⁴.
3. Area: $A = \frac{\pi}{4}(40^2 - 36^2) = 238.8$ mm².
4. Radius of gyration: $r = \sqrt{I/A} = \sqrt{43\,216/238.8} = 13.45$ mm; slenderness $L/r = 2000/13.45 = 149$, well above the transition value $\pi\sqrt{68.9\times10^{9}/276\times10^{6}} = 49.6$.
5. Critical load: $P_{\text{cr}} = \pi^2EI/L^2 = 9.870\times6.89\times10^{10}\times4.32\times10^{-8}/(2.00)^2 = 7.35\times10^{3}$ N.
6. Critical stress: $7350/238.8 = 30.8$ MPa.
7. Load to cause yielding: $\sigma_yA = 276\times238.8 = 6.59\times10^{4}$ N.

**Answer:** the column buckles at about 7.3 kN, only about 11% of the 66 kN needed to yield it. Clamping both ends ($K_e = 0.5$) would raise the buckling load fourfold, to about 29 kN.

## 10. Torsion of Shafts

Shafts in engines, drills, car axles and wind turbines transmit power by twisting. Bones also twist: a fall while skiing with the foot locked in place can produce a spiral fracture of the tibia.

**Derivation.** Consider a solid circular shaft of radius $R$ and length $L$, fixed at one end and twisted at the other by a torque $T$ through an angle $\varphi$. By symmetry, circular cross-sections stay plane and circular and simply rotate relative to each other (Saint-Venant later showed that non-circular sections, by contrast, warp). A thin line drawn along the surface parallel to the axis becomes a helix. At radius $\rho$, a point at the free end moves a distance $\rho\varphi$ around the circumference, so a line element of length $L$ is sheared through the angle
$$\gamma(\rho) = \frac{\rho\,\varphi}{L}$$
By Hooke's law in shear, the shear stress on the cross-section is
$$\tau(\rho) = G\gamma = \frac{G\varphi}{L}\,\rho$$
which grows linearly from zero on the axis to a maximum at the surface. Each ring of area $dA$ at radius $\rho$ carries a force $\tau\,dA$ with lever arm $\rho$, so the total torque is
$$T = \int_A \rho\,\tau\,dA = \frac{G\varphi}{L}\int_A \rho^2\,dA = \frac{GJ\varphi}{L}$$
where $J = \pi R^4/2$ is the polar second moment of area. Collecting results:
$$\boxed{\varphi = \frac{TL}{GJ}, \qquad \tau_{\max} = \frac{TR}{J}}$$
The product $GJ$ is the **torsional rigidity**. For a hollow shaft, $J = \pi(R_o^4 - R_i^4)/2$. As in bending, material near the center carries little stress, so hollow shafts save weight. The power transmitted by a shaft rotating at angular speed $\omega$ is $P = T\omega$.

Because pure shear is equivalent to tension and compression at 45° (Section 3.6), a brittle shaft such as a stick of chalk twisted between the fingers breaks along a 45° helix where the tensile stress is greatest, whereas a ductile steel shaft, weaker in shear than in tension, fails on a plane perpendicular to its axis.

### Worked Example 10: A drive shaft

A solid steel shaft ($G = 79$ GPa) of diameter 30.0 mm and length 1.50 m transmits 150 kW at 3000 revolutions per minute. Find the torque, the maximum shear stress and the angle of twist.

1. Angular speed: $\omega = 2\pi\times3000/60 = 314.2$ rad/s.
2. Torque: $T = P/\omega = 150\times10^{3}/314.2 = 477.5$ N·m.
3. Polar second moment: $J = \pi d^4/32 = \pi(0.0300)^4/32 = 7.95\times10^{-8}$ m⁴.
4. Maximum shear stress: $\tau_{\max} = TR/J = 477.5\times0.0150/7.95\times10^{-8} = 9.01\times10^{7}$ Pa $= 90$ MPa.
5. Angle of twist: $\varphi = TL/(GJ) = 477.5\times1.50/(7.9\times10^{10}\times7.95\times10^{-8}) = 0.114$ rad $= 6.5°$.

**Answer:** $T \approx 478$ N·m, $\tau_{\max} \approx 90$ MPa and $\varphi \approx 6.5°$. If the allowable shear stress were 60 MPa, solving $\tau_{\max} = 16T/(\pi d^3)$ for $d$ shows a diameter of at least 34.3 mm would be needed.

## 11. Fatigue and Fracture

### 11.1 Stress concentrations

The formula $\sigma = F/A$ gives an average. Near holes, notches, sharp corners and cracks the local stress can be much higher. In 1898 Ernst Kirsch showed that a small circular hole in a wide plate under uniaxial tension raises the stress at the edges of the hole to three times the remote value: the **stress concentration factor** is 3. In 1913 Charles Inglis extended the analysis to an elliptical hole with semi-axis $a$ perpendicular to the load and semi-axis $b$ parallel to it:
$$\sigma_{\max} = \sigma\left(1 + \frac{2a}{b}\right) = \sigma\left(1 + 2\sqrt{\frac{a}{\rho}}\right)$$
where $\rho = b^2/a$ is the radius of curvature at the tip. As the ellipse flattens into a sharp crack, $\rho$ shrinks toward atomic dimensions and the predicted stress grows enormously. This explains why rounded corners, generous fillets and smooth surfaces greatly extend the life of machine parts and why a scratch can make glass break at a low load.

### 11.2 Griffith's energy criterion

Inglis's result suggests that a sharp crack should make a material infinitely weak, which is plainly false. In 1921 Alan Arnold Griffith resolved the paradox with an energy argument. Consider a large plate of thickness $t$ under remote tensile stress $\sigma$ containing a through crack of length $2a$. Introducing the crack relaxes the stress in the surrounding material and releases stored elastic energy; using Inglis's solution, Griffith found that the released energy (for plane stress) is
$$U_{\text{released}} = \frac{\pi a^2\sigma^2 t}{E}$$
But creating the crack also creates two new surfaces, each of area $2at$, costing surface energy $\gamma_s$ per unit area:
$$U_{\text{surface}} = 4at\gamma_s$$
The total energy change is $\Delta U(a) = 4at\gamma_s - \pi a^2\sigma^2t/E$. The crack grows spontaneously once lengthening it lowers the total energy, that is, once $d(\Delta U)/da \le 0$:
$$4t\gamma_s - \frac{2\pi a\sigma^2 t}{E} = 0 \quad\Longrightarrow\quad \boxed{\sigma_f = \sqrt{\frac{2E\gamma_s}{\pi a}}}$$
The fracture stress falls as $1/\sqrt{a}$: longer cracks are more dangerous. Griffith confirmed his theory with glass fibers and showed that very thin, freshly drawn fibers, which contain only tiny flaws, were far stronger than bulk glass.

### 11.3 Stress intensity and fracture toughness

In the 1950s George Irwin recast Griffith's idea in a form suited to engineering metals, in which the energy absorbed by plastic deformation near the crack tip is far larger than the surface energy. The stress field near any crack tip has a universal shape whose strength is set by the **stress intensity factor**
$$K = Y\sigma\sqrt{\pi a}$$
where $Y$ is a dimensionless factor of order 1 that depends on geometry ($Y = 1$ for a central crack in a wide plate, about 1.12 for a shallow edge crack). Fracture occurs when $K$ reaches a critical material property, the **fracture toughness** $K_{Ic}$, measured in MPa·√m. Irwin showed that the energy release rate is $\mathcal{G} = K^2/E$ (plane stress), connecting the two approaches.

**Table 5. Approximate fracture toughness at room temperature**

| Material | $K_{Ic}$ (MPa·√m) |
|---|---|
| Soda-lime glass | 0.7–0.8 |
| PMMA (acrylic) | about 1 |
| Alumina ceramic | 3–5 |
| Cortical bone | roughly 2–10, depending on orientation and crack growth |
| Aluminum alloys | 20–45 |
| Structural and alloy steels | 50–150 |

Rearranging the fracture condition gives the **critical crack length** for a given stress: $a_c = \frac{1}{\pi}\left(\frac{K_{Ic}}{Y\sigma}\right)^2$. Engineers combine this with inspection: if cracks smaller than $a_c$ can be reliably detected and repaired, a structure can tolerate damage safely, an approach called **damage-tolerant design**.

### 11.4 Fatigue

Components subjected to repeated loading can fail at stresses well below the yield strength. A microscopic crack starts at a stress concentration or surface flaw, grows a tiny amount with each cycle, and finally reaches the critical size for fast fracture. Fatigue fracture surfaces often show **beach marks** recording the stages of crack growth. Fatigue accounts for a large fraction of the mechanical failures of machinery in service.

In the 1850s and 1860s August Wöhler tested railway axles under rotating bending and plotted the stress amplitude against the number of cycles to failure, now called an **S–N curve**. He found that for steel there is a stress amplitude, the **endurance limit**, below which failure did not occur even after very many cycles. For many steels the endurance limit is roughly half the ultimate tensile strength. Aluminum alloys show no clear endurance limit, so their fatigue strength is quoted at a specified number of cycles (often 5×10⁸). Above the endurance limit, the S–N curve is often fitted by **Basquin's law** (1910), $\sigma_a = \sigma_f'(2N_f)^b$, with exponent $b$ typically between about $-0.05$ and $-0.12$. Crack growth per cycle in the intermediate range follows the **Paris law** (early 1960s), $da/dN = C(\Delta K)^m$, with $m$ typically 2 to 4 for metals.

For loading at several stress levels, the **Palmgren–Miner rule** estimates that failure occurs when the accumulated damage
$$D = \sum_i \frac{n_i}{N_i}$$
reaches 1, where $n_i$ cycles are applied at a level whose fatigue life is $N_i$ cycles. It is a simple, approximate rule, since the order of loading also matters, but it is widely used.

### Worked Example 11: Critical crack lengths in steel and glass

(a) A wide steel plate with $K_{Ic} = 50$ MPa·√m carries a remote tensile stress of 300 MPa. Taking $Y = 1$, what central half-crack length $a$ causes fracture? (b) Repeat for a glass panel with $K_{Ic} = 0.75$ MPa·√m under 50 MPa.

1. Critical length formula: $a_c = \frac{1}{\pi}\left(\frac{K_{Ic}}{\sigma}\right)^2$.
2. (a) $K_{Ic}/\sigma = 50/300 = 0.1667$ √m, so $a_c = 0.02778/\pi = 8.84\times10^{-3}$ m.
3. (b) $K_{Ic}/\sigma = 0.75/50 = 0.015$ √m, so $a_c = 2.25\times10^{-4}/\pi = 7.2\times10^{-5}$ m.

**Answer:** the steel plate tolerates a crack about 8.8 mm long (half-length) before fracturing, large enough to find by routine inspection, whereas the glass fails from a flaw only about 0.07 mm long, smaller than many scratches. This is why glass must be designed with large safety factors and why its strength varies so much from piece to piece.

## 12. Historical Development

- **1638 — Galileo Galilei.** In *Discourses and Mathematical Demonstrations Relating to Two New Sciences*, the first "new science" is the strength of materials. Galileo analyzed the breaking of a cantilever and found correctly that its strength is proportional to $bh^2$, although because he did not know about elastic stress distribution his absolute value was three times too high. He also argued that geometrically similar animals cannot simply be scaled up: weight grows as length cubed but bone cross-section only as length squared, so large animals need disproportionately thick bones.
- **1660–1678 — Robert Hooke.** Hooke found the proportionality between force and extension around 1660, published it in 1676 as the anagram "ceiiinosssttuv", and revealed its solution, *ut tensio, sic vis*, in his 1678 lectures *De Potentia Restitutiva, or of Spring*.
- **1690s — Jacob Bernoulli** studied the elastic curve of a bent bar and assumed that its curvature is proportional to the bending moment, the core of beam theory.
- **1744 — Leonhard Euler** classified the shapes of bent elastic bars (the *elastica*) and derived the critical load for buckling, returning to columns in 1757.
- **1773 and 1784 — Charles-Augustin de Coulomb** analyzed beam and soil failure in a memoir presented in 1773 and in 1784 published the law of torsion of thin wires used in his torsion balance.
- **1807 — Thomas Young**, in his *Course of Lectures on Natural Philosophy and the Mechanical Arts*, introduced a modulus of elasticity characteristic of a material. He expressed it as the height of a column of the material rather than as a stress, but it is the ancestor of today's Young's modulus.
- **1821–1829 — Navier, Cauchy and Poisson.** Claude-Louis Navier derived general equations of elasticity from a molecular model (1821); Cauchy introduced the modern concepts of stress and strain (1822); Siméon Denis Poisson analyzed lateral contraction (1829), predicting a ratio of 1/4 from his molecular theory.
- **1850s–1870s — August Wöhler** carried out systematic fatigue tests on railway axles, after axle failures such as the one behind the 1842 Versailles rail disaster had shown that metals break under repeated loads.
- **1855 — Adhémar Barré de Saint-Venant** solved the torsion of non-circular shafts; **1882 — Christian Otto Mohr** introduced his circle for transforming stresses; **1885 — Armand Considère** explained necking; **1892 — Julius Wolff** proposed that bone adapts to the loads it carries.
- **1898 and 1913 — Ernst Kirsch and Charles Inglis** calculated stress concentrations around circular and elliptical holes; **1921 — A. A. Griffith** founded fracture mechanics.
- **1934 — G. I. Taylor, Egon Orowan and Michael Polanyi** independently proposed dislocations, explaining why real metals yield at stresses hundreds to thousands of times lower than the theoretical shear strength of a perfect crystal.
- **1938 — Edward Simmons and Arthur Ruge** independently developed the bonded resistance strain gauge.
- **1940s — welded ships.** Brittle fractures in welded ships of the Second World War, including the tanker SS *Schenectady*, which broke in two while moored in January 1943, led Constance Tipper at Cambridge to demonstrate the ductile-to-brittle transition in steel.
- **1954 — the de Havilland Comet** airliner disasters were traced to fatigue cracks growing from a corner of an opening in the pressurized fuselage, making fatigue a central concern of aircraft design.
- **1957 — George Irwin** introduced the stress intensity factor; Paul Paris and coworkers related fatigue crack growth to it in the early 1960s.

## 13. Applications in Engineering, Medicine and Biology

**Structures.** Every building, bridge and crane is designed using the ideas in this chapter: members in tension are sized by $\sigma = F/A$ against the yield strength; beams by the flexure formula and deflection limits (a floor that sags visibly or bounces is unacceptable even if it is strong); columns by Euler's formula and its refinements. Steel I-beams place material in the flanges where bending stresses are highest. **Prestressed concrete** uses tensioned steel tendons to squeeze concrete so that under service loads it never goes into significant tension, exploiting its high compressive strength.

**Transport and machines.** Aircraft are inspected regularly for fatigue cracks, and their components are designed so that a crack will be found before it reaches critical length. Drive shafts, crankshafts and turbine blades are designed against fatigue, with polished surfaces and rounded fillets to reduce stress concentrations. Continuously welded rail, pipelines and power lines must accommodate thermal expansion.

**Measurement.** A **strain gauge** is a thin metal foil grid bonded to a surface; when the surface stretches, the grid's electrical resistance changes in proportion to the strain. Strain gauges are the sensing element of most electronic scales and load cells, and are used to monitor bridges and aircraft.

**Bone.** Cortical (compact) bone is a composite of stiff mineral crystals (hydroxyapatite) and tough collagen fibers. Its Young's modulus along the long axis is about 17–20 GPa, roughly a tenth of steel's, and it is stronger in compression (about 193 MPa) than in tension (about 133 MPa) and weakest in shear (about 68 MPa), values measured for human femoral bone. Long bones are hollow tubes, which (as Worked Example 8 showed) gives high bending and torsional stiffness for their mass; the marrow cavity houses blood-forming tissue. Trabecular (spongy) bone at the ends of long bones is a porous lattice whose struts tend to align with the principal stress directions. Bone remodels in response to load, as Wolff proposed: athletes' bones thicken, while astronauts in weightlessness lose bone mass at a rate on the order of 1% per month in weight-bearing bones. Osteoporosis thins the trabeculae and raises fracture risk.

**Implants and stress shielding.** A titanium alloy hip stem has a modulus around 110 GPa, several times that of the surrounding bone. Because stiffer parts of a composite structure carry more of the load, the implant "shields" the nearby bone from stress, and the bone may resorb over time. Implant designers therefore seek lower-modulus alloys, porous structures and shapes that share load with the bone. Superelastic nickel–titanium alloys, which can recover strains of several percent, are used in orthodontic wires and self-expanding vascular stents.

**Tendons and ligaments.** Tendons transmit muscle forces to bones and are made of aligned collagen fibrils with a microscopic wavy "crimp". Their stress–strain curve is **J-shaped**: an initial compliant **toe region** (up to about 2% strain) where the crimp straightens, followed by a stiffer, nearly linear region. Tendons have a modulus of about 1–2 GPa and a tensile strength of roughly 50–150 MPa. Their relatively low modulus combined with high strength lets them store and return substantial elastic energy, as Worked Example 5 illustrated; kangaroos and running humans exploit this to reduce the metabolic cost of locomotion.

**Plants, silk and everyday objects.** Bamboo and grass stems are hollow tubes whose nodes resist local buckling. Spider dragline silk combines a tensile strength around 1 GPa with large extensibility, giving it exceptional toughness. A glass cutter scores a line to create a controlled flaw so the glass breaks along it, and a paper clip snaps after repeated bending because of low-cycle fatigue.

## 14. Common Misconceptions

1. **"Stiffness and strength are the same thing."** Stiffness (Young's modulus) measures resistance to elastic deformation; strength (yield or ultimate stress) measures the stress at which permanent deformation or fracture occurs. Glass is about as stiff as aluminum alloys but far weaker in tension; a high-strength steel and a mild steel have nearly the same $E$ but very different strengths. Toughness, the energy absorbed before fracture, is yet another property.
2. **"Rubber is more elastic than steel."** In everyday speech "elastic" means "stretchy". In physics, elasticity means the ability to recover the original shape, and the elastic modulus measures stiffness. Steel has a modulus about 10⁴–10⁵ times that of rubber; rubber has a much larger recoverable strain.
3. **"Hooke's law is a fundamental law of nature."** It is a small-strain approximation. It fails beyond the proportional limit, and some materials, such as rubber and soft tissues, are nonlinear from the start.
4. **"Stress is just force."** Stress is force per unit area and, in general, a tensor whose value depends on the orientation of the surface considered. The same force produces very different stresses in a thick and a thin rod.
5. **"A thicker beam is proportionally stiffer."** For bending, stiffness scales with $I$, which for a rectangle grows as the cube of the depth. Doubling the depth increases the bending stiffness eightfold, whereas doubling the width only doubles it.
6. **"A column fails when its stress reaches the compressive strength."** Slender columns buckle at loads that may be a small fraction of the crushing load, and the buckling load depends on stiffness and length, not strength.
7. **"The ultimate tensile strength is the stress at which the material breaks."** For ductile materials the engineering stress falls after the UTS because of necking. The true stress in the neck at fracture is actually higher than the UTS.
8. **"Fatigue only matters if the stress exceeds the yield strength."** Fatigue cracks grow at stresses well below yield; this is precisely what makes fatigue dangerous.
9. **"Poisson's ratio must be between 0 and 0.5."** For stable isotropic materials the bounds are $-1 < \nu < 0.5$. Auxetic materials with negative Poisson's ratio exist and are used in some protective padding and medical devices.
10. **"A longer bar develops a larger thermal stress."** The stress in a fully constrained bar, $E\alpha\,\Delta T$, is independent of length; length only sets how much free expansion must be accommodated.
11. **"Solid members are always stronger than hollow ones."** For a given mass, a tube is stiffer and stronger in bending and torsion than a solid rod, until its wall becomes so thin that it buckles locally.

## 15. Connections to Other Topics

- **Oscillations.** A bar acts as a spring of stiffness $k = EA/L$, and a torsion wire as a torsional spring of constant $GJ/L$, the basis of torsion pendulums and balances such as Coulomb's and Cavendish's. The buckling equation has the same form as the harmonic oscillator equation.
- **Waves and sound.** The speed of longitudinal waves in a thin rod is $\sqrt{E/\rho}$, about 5 km/s for steel and aluminum; in a fluid it is $\sqrt{K/\rho}$. Seismic P-waves travel at $\sqrt{(K + 4G/3)/\rho}$ and S-waves at $\sqrt{G/\rho}$; because liquids have $G = 0$, S-waves cannot cross Earth's liquid outer core.
- **Fluid mechanics.** Fluids have a bulk modulus but no static shear modulus; viscosity plays the role in fluids that $G$ plays in solids, with strain rate in place of strain. Materials such as polymers and tissues that combine both responses are **viscoelastic**.
- **Rotational dynamics and energy.** The second moment of area $\int y^2\,dA$ is the analog of the mass moment of inertia $\int r^2\,dm$, with the same parallel- and perpendicular-axis theorems. Spring energy $\frac{1}{2}kx^2$ generalizes to the energy density $\sigma^2/(2E)$.
- **Lagrangian mechanics.** Euler derived the elastica by minimizing elastic energy; beams and buckling are classic applications of the calculus of variations.
- **Thermodynamics.** Thermal expansion arises from the asymmetry of the interatomic potential; rubber elasticity is mainly entropic, since stretching aligns polymer chains and lowers their entropy.
- **Chemistry and materials science.** Bond type sets the modulus; crystal structure and dislocations set yield strength and ductility.
- **Biology and Earth science.** Biomechanics applies these results to bones, tendons, arteries and plants. Rocks are elastic over short times and flow over geological times; elastic strain stored along faults is released in earthquakes.
- **Mathematics.** Principal stresses are eigenvalues of the stress tensor, and buckling loads are eigenvalues of a differential equation.

## 16. Practice Problems

1. **(Easy)** A steel guitar string ($E = 200$ GPa) of diameter 0.254 mm and vibrating length 0.648 m is tuned to a tension of 72 N. Find the stress, the strain, the elongation of the vibrating length, and the elastic energy stored in that length.
2. **(Easy)** A rubber vibration-isolation pad 10 cm × 10 cm in plan and 2.0 cm thick has shear modulus 0.50 MPa. A horizontal force of 200 N acts on its top face while the bottom is fixed. Find the shear stress, the shear strain and the horizontal displacement of the top face.
3. **(Easy)** What pressure increase reduces the volume of water ($K = 2.2$ GPa) by 0.50%? Approximately what ocean depth (seawater density 1025 kg/m³) produces this pressure?
4. **(Medium)** Measurements on an isotropic alloy give $E = 110$ GPa and $G = 41$ GPa. Find Poisson's ratio and the bulk modulus.
5. **(Medium)** An aluminum bar ($E = 69$ GPa, $\alpha = 23\times10^{-6}$ K⁻¹, cross-section 4.0 cm²) is fitted snugly between two rigid walls at 20 °C. Find the stress and the force on the walls when it is heated to 70 °C. By how much would a 1.00 m bar have expanded if free?
6. **(Medium)** Model the shaft of a tibia as a hollow tube of outer diameter 25 mm and inner diameter 13 mm, with $E = 18$ GPa. A 70 kg person lands from a jump with a peak axial force of 4 times body weight. Find the compressive stress and strain, and the factor of safety against a compressive strength of 193 MPa. Why are real bone fractures in such landings nevertheless possible?
7. **(Medium)** A simply supported wooden beam ($E = 12$ GPa) spans 3.0 m and has a 50 mm × 200 mm rectangular section placed on edge. A load of 2.0 kN acts at midspan. Find the maximum deflection and the maximum bending stress. Repeat for the beam laid flat.
8. **(Medium–hard)** A solid round steel rod ($E = 200$ GPa, $\sigma_y = 250$ MPa) of diameter 20 mm is used as a pinned–pinned column. Find the length at which the Euler buckling load equals the load that causes yielding. What is the buckling load if the rod is 1.00 m long?
9. **(Hard)** A solid steel shaft of diameter 50 mm is to be replaced by a hollow shaft of the same material and the same mass per unit length, with outer diameter 60 mm. Find the inner diameter, the ratio of the torsional stiffnesses, and the ratio of the maximum torques the shafts can carry for the same allowable shear stress. Evaluate both maximum torques for an allowable shear stress of 80 MPa.
10. **(Hard)** (a) A steel plate with $K_{Ic} = 60$ MPa·√m and yield strength 600 MPa contains an edge crack ($Y = 1.12$) and is loaded to 200 MPa. Find the critical crack depth. (b) What stress would fracture the plate if the crack were only 1.0 mm deep, and what does the result imply? (c) A component made of this steel experiences 2.0×10⁵ cycles at a stress level whose fatigue life is 1.0×10⁶ cycles and 5.0×10⁴ cycles at a level whose fatigue life is 2.0×10⁵ cycles. Using Miner's rule, how many further cycles at the first level can it endure?

### Solutions

**1. Guitar string.**
1. Area: $A = \pi(0.127\times10^{-3})^2 = 5.07\times10^{-8}$ m².
2. Stress: $\sigma = 72/5.07\times10^{-8} = 1.42\times10^{9}$ Pa $= 1.42$ GPa, which requires a high-strength steel such as music wire.
3. Strain: $\varepsilon = 1.42\times10^{9}/2.00\times10^{11} = 7.1\times10^{-3}$.
4. Elongation: $\Delta L = 7.1\times10^{-3}\times0.648 = 4.6\times10^{-3}$ m.
5. Energy: $U = \frac{1}{2}F\Delta L = 0.5\times72\times0.0046 = 0.17$ J.

Answer: about 1.4 GPa, $7.1\times10^{-3}$, 4.6 mm and 0.17 J.

**2. Rubber pad.**
1. Area: $A = 0.10\times0.10 = 0.010$ m².
2. Shear stress: $\tau = 200/0.010 = 2.0\times10^{4}$ Pa $= 20$ kPa.
3. Shear strain: $\gamma = \tau/G = 2.0\times10^{4}/5.0\times10^{5} = 0.040$.
4. Displacement: $\Delta x = \gamma h = 0.040\times2.0$ cm $= 0.080$ cm.

Answer: 20 kPa, 0.040 (about 2.3°), 0.80 mm.

**3. Compressing water.**
1. $\Delta p = K\lvert\Delta V/V\rvert = 2.2\times10^{9}\times0.0050 = 1.1\times10^{7}$ Pa $= 11$ MPa, about 109 atmospheres.
2. Depth: $h = \Delta p/(\rho g) = 1.1\times10^{7}/(1025\times9.81) = 1.09\times10^{3}$ m.

Answer: about 11 MPa, reached at a depth of roughly 1.1 km.

**4. Elastic constants.**
1. From $G = E/[2(1+\nu)]$: $\nu = E/(2G) - 1 = 110/82 - 1 = 0.341$.
2. From $K = E/[3(1-2\nu)]$: $K = 110/[3(1 - 0.683)] = 110/0.951 = 116$ GPa.

Answer: $\nu \approx 0.34$ and $K \approx 116$ GPa (values typical of copper).

**5. Constrained aluminum bar.**
1. $\Delta T = 50$ K.
2. Stress: $\sigma = -E\alpha\Delta T = -6.9\times10^{10}\times23\times10^{-6}\times50 = -7.94\times10^{7}$ Pa $= -79$ MPa (compression).
3. Force: $F = 7.94\times10^{7}\times4.0\times10^{-4} = 3.17\times10^{4}$ N.
4. Free expansion: $\Delta L = 23\times10^{-6}\times1.00\times50 = 1.15\times10^{-3}$ m.

Answer: about 79 MPa compressive, a force of about 32 kN on each wall; a free 1.00 m bar would grow by 1.15 mm. The stress is below the yield strength of common aluminum alloys, but a long, slender bar could buckle.

**6. Tibia in a landing.**
1. Area: $A = \frac{\pi}{4}(25^2 - 13^2) = \frac{\pi}{4}\times456 = 358$ mm².
2. Force: $F = 4\times70\times9.81 = 2747$ N.
3. Stress: $\sigma = 2747/358 = 7.7$ MPa.
4. Strain: $\varepsilon = 7.7/18\,000 = 4.3\times10^{-4}$ (about 430 microstrain).
5. Factor of safety: $193/7.7 \approx 25$.

Answer: about 7.7 MPa and 430 microstrain, with a nominal safety factor of about 25 in pure compression. Real loads are never purely axial: the bone is curved and muscles and ground forces act off-axis, so bending and torsion add stresses that can be several times larger than the axial stress, and bone is weaker in tension and shear than in compression. Repeated loading can also cause fatigue (stress) fractures.

**7. Wooden beam.**
1. On edge: $I = bh^3/12 = 0.050\times(0.200)^3/12 = 3.33\times10^{-5}$ m⁴.
2. Deflection: $\delta = FL^3/(48EI) = 2000\times27/(48\times1.2\times10^{10}\times3.33\times10^{-5}) = 2.8\times10^{-3}$ m.
3. Maximum moment at midspan: $M = FL/4 = 2000\times3.0/4 = 1500$ N·m.
4. Stress: $\sigma = Mc/I = 1500\times0.100/3.33\times10^{-5} = 4.5\times10^{6}$ Pa $= 4.5$ MPa.
5. Laid flat: $I = 0.200\times(0.050)^3/12 = 2.08\times10^{-6}$ m⁴, sixteen times smaller, so $\delta = 45$ mm and $\sigma = 1500\times0.025/2.08\times10^{-6} = 18$ MPa.

Answer: on edge, 2.8 mm and 4.5 MPa; flat, 45 mm and 18 MPa.

**8. Euler length of a steel rod.**
1. For a solid circle, $r = \sqrt{I/A} = \sqrt{(\pi d^4/64)/(\pi d^2/4)} = d/4 = 5.0$ mm.
2. Setting $\pi^2E/(L/r)^2 = \sigma_y$ gives $L = \pi r\sqrt{E/\sigma_y} = \pi\times5.0\times\sqrt{800} = \pi\times5.0\times28.28 = 444$ mm.
3. For $L = 1.00$ m: $I = \pi(0.020)^4/64 = 7.85\times10^{-9}$ m⁴, so $P_{\text{cr}} = \pi^2\times2.00\times10^{11}\times7.85\times10^{-9}/1.00^2 = 1.55\times10^{4}$ N.
4. Compare the yield load $\sigma_yA = 250\times10^{6}\times3.14\times10^{-4} = 7.85\times10^{4}$ N.

Answer: the transition length is about 0.44 m; a 1.00 m rod buckles at about 15.5 kN, roughly one-fifth of its 78.5 kN yield load.

**9. Solid versus hollow shaft.**
1. Equal areas: $D_o^2 - D_i^2 = 50^2$, so $D_i = \sqrt{3600 - 2500} = \sqrt{1100} = 33.2$ mm.
2. Polar moments: $J_{\text{solid}} = \pi(50)^4/32 = 6.14\times10^{5}$ mm⁴; $J_{\text{hollow}} = \pi(60^4 - 33.17^4)/32 = 1.15\times10^{6}$ mm⁴.
3. Stiffness ratio: since $\varphi = TL/(GJ)$, the ratio is $J_{\text{hollow}}/J_{\text{solid}} = 1.88$.
4. Torque capacity: $T_{\max} = \tau_{\text{allow}}J/R$. The ratio is $(J_h/30)/(J_s/25) = 1.88\times25/30 = 1.57$.
5. With $\tau_{\text{allow}} = 80$ MPa: $T_{\text{solid}} = 80\times6.14\times10^{5}/25 = 1.96\times10^{6}$ N·mm $= 1.96$ kN·m; $T_{\text{hollow}} = 80\times1.15\times10^{6}/30 = 3.08\times10^{6}$ N·mm $= 3.08$ kN·m.

Answer: inner diameter about 33.2 mm; the hollow shaft is 1.88 times stiffer in torsion and can carry 1.57 times the torque (about 3.1 kN·m versus 2.0 kN·m) for the same mass.

**10. Fracture and fatigue.**
1. (a) $a_c = \frac{1}{\pi}\left(\frac{K_{Ic}}{Y\sigma}\right)^2 = \frac{1}{\pi}\left(\frac{60}{1.12\times200}\right)^2 = \frac{0.0718}{\pi} = 0.0228$ m.
2. (b) $\sigma_f = K_{Ic}/(Y\sqrt{\pi a}) = 60/(1.12\times\sqrt{\pi\times0.0010}) = 60/(1.12\times0.0560) = 956$ MPa.
3. This exceeds the 600 MPa yield strength, so with a 1 mm crack the plate would yield before fracturing: for small cracks, strength rather than toughness governs, and linear elastic fracture mechanics no longer applies.
4. (c) Damage so far: $D = 2.0\times10^{5}/1.0\times10^{6} + 5.0\times10^{4}/2.0\times10^{5} = 0.20 + 0.25 = 0.45$.
5. Remaining damage capacity: $1 - 0.45 = 0.55$, corresponding to $0.55\times1.0\times10^{6} = 5.5\times10^{5}$ cycles at the first level.

Answer: (a) about 23 mm; (b) about 960 MPa, above yield, so the plate yields first; (c) about 5.5×10⁵ more cycles.

## 17. Summary

- Stress (force per area) and strain (relative deformation) remove the dependence on specimen size. For small strains, isotropic materials obey Hooke's law with four constants $E$, $G$, $K$ and $\nu$, only two of them independent; $G = E/[2(1+\nu)]$ and $K = E/[3(1-2\nu)]$ restrict $\nu$ to the range from $-1$ to $1/2$.
- A tensile test reveals yield, strain hardening, the ultimate tensile strength, necking (beginning when $d\sigma_t/d\varepsilon_t = \sigma_t$) and fracture. Ductile materials deform plastically and absorb energy; brittle materials fail suddenly from flaws.
- Elastic energy density is $\sigma^2/(2E)$, so strong, low-modulus materials such as spring steel and tendon make good springs. Constrained thermal expansion produces stresses $E\alpha\,\Delta T$ independent of size.
- In bending, stress is $My/I$ about a neutral axis through the centroid, and deflections scale as $L^3/(EI)$, so material far from the axis controls performance. Slender columns buckle at $\pi^2EI/L_e^2$, often far below their crushing load. Circular shafts in torsion carry shear stress $T\rho/J$ and twist by $TL/(GJ)$.
- Stress concentrations, cracks and repeated loading explain why real structures fail far below ideal strengths; Griffith's energy balance, Irwin's fracture toughness, S–N curves and Miner's rule quantify these failures. The same principles explain hollow bones and bamboo, springy tendons, and the design of bridges, aircraft and implants.

### Key Equations

| Quantity | Equation |
|---|---|
| Normal stress and strain | $\sigma = F/A_0$, $\varepsilon = \Delta L/L_0$ |
| Hooke's law (tension, shear, volume) | $\sigma = E\varepsilon$, $\tau = G\gamma$, $\Delta p = -K\,\Delta V/V$ |
| Poisson's ratio | $\nu = -\varepsilon_{\text{lat}}/\varepsilon_{\text{axial}}$ |
| Relations among moduli | $G = E/[2(1+\nu)]$, $K = E/[3(1-2\nu)]$ |
| Axial stiffness of a bar | $k = EA/L$ |
| True stress and strain | $\sigma_t = \sigma(1+\varepsilon)$, $\varepsilon_t = \ln(1+\varepsilon)$ |
| Considère necking criterion | $d\sigma_t/d\varepsilon_t = \sigma_t$ |
| Elastic energy density | $u = \sigma^2/(2E) = \tfrac{1}{2}E\varepsilon^2$; shear $u = \tau^2/(2G)$ |
| Thermal stress (fully constrained bar) | $\sigma = -E\alpha\,\Delta T$ |
| Flexure formula | $\sigma = -My/I$, $\sigma_{\max} = Mc/I$ |
| Second moment of area | $I = \int y^2\,dA$; rectangle $bh^3/12$; circle $\pi r^4/4$ |
| Beam equation and cantilever deflection | $EI\,w'' = M(x)$, $\delta = FL^3/(3EI)$ |
| Euler buckling | $P_{\text{cr}} = \pi^2EI/(K_eL)^2$, $\sigma_{\text{cr}} = \pi^2E/(L_e/r)^2$ |
| Torsion of circular shaft | $\tau = T\rho/J$, $\varphi = TL/(GJ)$, $J = \pi R^4/2$, $P = T\omega$ |
| Stress concentration (ellipse) | $\sigma_{\max} = \sigma(1 + 2a/b)$ |
| Griffith fracture stress | $\sigma_f = \sqrt{2E\gamma_s/(\pi a)}$ |
| Stress intensity and critical crack | $K = Y\sigma\sqrt{\pi a}$, $a_c = (1/\pi)(K_{Ic}/Y\sigma)^2$ |
| Miner's rule | $\sum n_i/N_i = 1$ |

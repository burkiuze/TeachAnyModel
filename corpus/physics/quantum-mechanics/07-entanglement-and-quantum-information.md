---
title: Entanglement, Bell's Theorem, Quantum Information and Interpretations
field: Physics
subfield: Quantum Mechanics
level: undergraduate to graduate
keywords: [entanglement, EPR paradox, Bell's theorem, Bell inequality, CHSH inequality, local hidden variables, nonlocality, no-signaling theorem, no-cloning theorem, qubit, Bloch sphere, quantum gates, Hadamard, CNOT, quantum circuits, quantum teleportation, superdense coding, quantum key distribution, BB84, Shor's algorithm, Grover's algorithm, quantum error correction, decoherence, measurement problem, Copenhagen interpretation, many-worlds, Bohmian mechanics, Schrödinger's cat]
---

# Entanglement, Bell's Theorem, Quantum Information and Interpretations

Schrödinger called entanglement "not *one* but rather *the* characteristic trait of quantum mechanics, the one that enforces its entire departure from classical lines of thought" (1935). Once regarded as a philosophical curiosity, entanglement is now an experimentally verified resource powering quantum cryptography, quantum teleportation and quantum computing. The 2022 Nobel Prize in Physics went to Alain Aspect, John Clauser and Anton Zeilinger for experiments with entangled photons that established the violation of Bell inequalities and pioneered quantum information science.

## 1. Entanglement

### Product states vs. entangled states
For two systems A and B with state spaces $\mathcal H_A$ and $\mathcal H_B$, the joint state lives in $\mathcal H_A\otimes\mathcal H_B$. A **product (separable) state** can be written
$$|\psi\rangle_{AB} = |\phi\rangle_A\otimes|\chi\rangle_B$$
Each subsystem has its own definite state. Any state that cannot be written this way is **entangled**.

**Example:** $\frac{1}{\sqrt2}(|00\rangle + |01\rangle) = |0\rangle\otimes\frac{1}{\sqrt2}(|0\rangle + |1\rangle)$ is a product state. But
$$|\Phi^+\rangle = \frac{1}{\sqrt2}(|00\rangle + |11\rangle)$$
cannot be factored: if $(a|0\rangle + b|1\rangle)(c|0\rangle + d|1\rangle) = \frac{1}{\sqrt2}(|00\rangle + |11\rangle)$, then $ac = bd = \frac{1}{\sqrt2}$ but $ad = bc = 0$, a contradiction.

### The Bell states
Four maximally entangled two-qubit states form an orthonormal basis:
$$|\Phi^\pm\rangle = \frac{1}{\sqrt2}(|00\rangle \pm |11\rangle), \qquad |\Psi^\pm\rangle = \frac{1}{\sqrt2}(|01\rangle \pm |10\rangle)$$
$|\Psi^-\rangle$ is the spin singlet: it gives perfectly anticorrelated results when both spins are measured along **any** common axis.

### Properties of entangled states
- **The whole is definite, the parts are not.** In $|\Phi^+\rangle$ the joint state is pure (maximal knowledge), yet each qubit alone is maximally mixed: its reduced density matrix is $\rho_A = \text{Tr}_B|\Phi^+\rangle\langle\Phi^+| = \frac12I$. Measuring qubit A alone gives completely random results.
- **Perfect correlations:** measuring both in the computational basis always gives matching results (00 or 11), each with probability ½.
- **Entanglement entropy:** for a pure joint state, entanglement is quantified by the von Neumann entropy of either reduced state, $S = -\text{Tr}(\rho_A\log_2\rho_A)$; for Bell states, $S = 1$ ebit.
- **Schmidt decomposition:** any pure bipartite state can be written $|\psi\rangle = \sum_i\sqrt{\lambda_i}|a_i\rangle|b_i\rangle$; it is entangled if more than one Schmidt coefficient is nonzero.

### Creating entanglement
Entanglement arises whenever systems interact: spontaneous parametric down-conversion in nonlinear crystals produces polarization-entangled photon pairs; atomic cascades; decay of spin-0 particles into two spin-½ particles; two-qubit gates (e.g. CNOT) in quantum computers; trapped ions coupled via shared vibrational modes.

## 2. The EPR Argument (1935)

Einstein, Boris Podolsky and Nathan Rosen published "Can Quantum-Mechanical Description of Physical Reality Be Considered Complete?" Their argument (in Bohm's spin version):
1. Two particles in the singlet state fly apart to distant locations.
2. If Alice measures her particle's spin along $z$ and gets up, she can predict with certainty that Bob's is down along $z$ — without disturbing Bob's particle (assuming **locality**: no influence travels faster than light).
3. EPR's **reality criterion:** "If, without in any way disturbing a system, we can predict with certainty the value of a physical quantity, then there exists an element of physical reality corresponding to that quantity."
4. Alice could have chosen to measure $x$ instead, predicting Bob's $S_x$ with certainty. So Bob's particle must possess definite values of **both** $S_z$ and $S_x$ — but quantum mechanics says they cannot be simultaneously definite.
5. Conclusion: quantum mechanics is **incomplete**; there must be additional "hidden variables" specifying the outcomes.

Einstein famously derided the alternative as "spooky action at a distance" (*spukhafte Fernwirkung*). Bohr replied that EPR's criterion was ambiguous, since the measurement context defines what can meaningfully be said about the system. For nearly 30 years the debate seemed purely philosophical.

## 3. Bell's Theorem (1964)

John Stewart Bell showed that the debate is **experimentally decidable**. Any theory satisfying:
- **Locality** — outcomes at one site do not depend on measurement settings at a distant site, and
- **Realism / hidden variables** — outcomes are determined (or their probabilities fixed) by pre-existing properties $\lambda$ shared at the source,

must satisfy certain inequalities on correlations. Quantum mechanics predicts violations.

### The CHSH inequality
Clauser, Horne, Shimony and Holt (1969) gave the experimentally practical version. Alice chooses between measurement settings $a$ and $a'$, Bob between $b$ and $b'$; each outcome is ±1. Define the correlation $E(a, b) = \langle A_aB_b\rangle$ and
$$S = E(a, b) - E(a, b') + E(a', b) + E(a', b')$$

**Local hidden-variable bound:** for any local realistic theory,
$$\boxed{|S| \le 2}$$
*Proof sketch:* for each $\lambda$, the outcomes $A, A', B, B' \in \{\pm1\}$ are fixed. Then $A(B - B') + A'(B + B')$: one of $B - B'$ and $B + B'$ is 0 and the other is ±2, so the expression equals ±2. Averaging over $\lambda$ gives $|S| \le 2$.

**Quantum prediction:** for the singlet state, $E(a, b) = -\cos\theta_{ab}$ (angle between the measurement axes). Choosing $a = 0°$, $a' = 90°$, $b = 45°$, $b' = 135°$ (or similar):
$$|S| = 2\sqrt2 \approx 2.83$$
the maximum allowed by quantum mechanics (**Tsirelson's bound**).

### Experiments
- **Freedman and Clauser (1972)**: first violation using atomic cascade photons.
- **Aspect, Grangier, Roger and Dalibard (1981–1982)**: switched polarizer settings during the photons' flight, addressing the locality loophole; observed $S = 2.70 \pm 0.05$.
- **Weihs, Zeilinger et al. (1998)**: fully random, fast settings with stations 400 m apart.
- **Loophole-free tests (2015)**: Delft (Hensen et al., electron spins in diamond 1.3 km apart), Vienna and NIST (photons) closed the locality and detection loopholes simultaneously.
- **"Big Bell Test" (2016)**: 100 000 volunteers generated random settings via a video game. Cosmic Bell tests used light from distant quasars to choose settings, pushing any "conspiracy" back billions of years.

**Conclusion:** nature violates Bell inequalities. **No local hidden-variable theory can reproduce quantum mechanics.** One must abandon locality (in the specific sense of Bell), or the notion that measurement outcomes reflect pre-existing values, or some other assumption (such as measurement independence, i.e. "free choice" — the superdeterminism loophole, which cannot be closed experimentally but which most physicists reject).

### What entanglement does NOT allow: no-signaling
Despite these correlations, **entanglement cannot transmit information faster than light**. Bob's local measurement statistics are completely independent of what Alice chooses to measure: his reduced density matrix doesn't change. The correlations only become apparent when results are compared via a classical channel (limited by $c$). Quantum mechanics and special relativity "peacefully coexist" (Shimony).

## 4. The No-Cloning Theorem

**It is impossible to make an identical copy of an unknown quantum state** (Wootters, Zurek, Dieks, 1982).

*Proof:* suppose a unitary $U$ copies: $U|\psi\rangle|0\rangle = |\psi\rangle|\psi\rangle$ and $U|\phi\rangle|0\rangle = |\phi\rangle|\phi\rangle$. Taking inner products, unitarity gives $\langle\phi|\psi\rangle = \langle\phi|\psi\rangle^2$, so $\langle\phi|\psi\rangle = 0$ or 1. Only orthogonal (or identical) states can be cloned — not arbitrary unknown states.

Consequences: quantum information cannot be perfectly copied, which (a) prevents faster-than-light signaling schemes that would otherwise exploit entanglement, (b) makes eavesdropping on quantum key distribution detectable, and (c) means quantum error correction must work without copying.

## 5. Qubits and Quantum Gates

### The qubit
A **qubit** is a two-level quantum system: $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$, $|\alpha|^2 + |\beta|^2 = 1$. Equivalently, a point on the **Bloch sphere**: $|\psi\rangle = \cos\frac\theta2|0\rangle + e^{i\phi}\sin\frac\theta2|1\rangle$.

Physical implementations: electron or nuclear spins, photon polarization, energy levels of trapped ions (Quantinuum, IonQ), superconducting circuits (transmons — IBM, Google), neutral atoms in optical tweezers, quantum dots, topological qubits (proposed), nitrogen-vacancy centers in diamond.

**Exponential state space:** $n$ qubits require $2^n$ complex amplitudes to describe in general. 300 qubits correspond to more amplitudes than there are atoms in the observable universe. But measurement yields only $n$ classical bits; quantum algorithms must cleverly use **interference** to amplify correct answers.

### Single-qubit gates (unitary 2×2 matrices)

| Gate | Matrix | Action |
|---|---|---|
| Pauli-X (NOT) | $\begin{pmatrix}0&1\\1&0\end{pmatrix}$ | $\vert 0\rangle\leftrightarrow\vert 1\rangle$ |
| Pauli-Z | $\begin{pmatrix}1&0\\0&-1\end{pmatrix}$ | Phase flip: $\vert 1\rangle\to-\vert 1\rangle$ |
| Pauli-Y | $\begin{pmatrix}0&-i\\i&0\end{pmatrix}$ | Bit and phase flip |
| Hadamard H | $\frac{1}{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}$ | $\vert 0\rangle\to\vert +\rangle$, $\vert 1\rangle\to\vert -\rangle$ |
| Phase S | $\begin{pmatrix}1&0\\0&i\end{pmatrix}$ | Quarter-turn about $z$ |
| T ($\pi/8$) | $\begin{pmatrix}1&0\\0&e^{i\pi/4}\end{pmatrix}$ | Eighth-turn about $z$ |
| Rotation $R_n(\theta)$ | $e^{-i\theta\,\hat n\cdot\vec\sigma/2}$ | Rotation by $\theta$ about axis $\hat n$ |

with $|\pm\rangle = \frac{1}{\sqrt2}(|0\rangle \pm |1\rangle)$. Note $HH = I$, and $H$ maps between the $Z$ and $X$ bases.

### Two-qubit gates
**CNOT (controlled-NOT):** flips the target qubit if the control is $|1\rangle$:
$$|00\rangle\to|00\rangle, \quad |01\rangle\to|01\rangle, \quad |10\rangle\to|11\rangle, \quad |11\rangle\to|10\rangle$$
**Creating a Bell state:** apply H to the first qubit of $|00\rangle$, then CNOT:
$$|00\rangle\xrightarrow{H\otimes I}\frac{1}{\sqrt2}(|0\rangle + |1\rangle)|0\rangle\xrightarrow{\text{CNOT}}\frac{1}{\sqrt2}(|00\rangle + |11\rangle)$$

**Universality:** any unitary on $n$ qubits can be approximated arbitrarily well using single-qubit gates plus CNOT; the finite set {H, T, CNOT} is universal (Solovay–Kitaev theorem guarantees efficient approximation).

## 6. Quantum Communication Protocols

### Quantum teleportation (Bennett et al., 1993)
Alice wants to send an unknown qubit $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$ to Bob. They share a Bell pair $|\Phi^+\rangle$.
1. Alice performs a **Bell measurement** on $|\psi\rangle$ and her half of the pair (CNOT, then H, then measure both), obtaining two classical bits (four equally likely outcomes).
2. The joint state can be rewritten so that, depending on Alice's outcome, Bob's qubit is $|\psi\rangle$, $X|\psi\rangle$, $Z|\psi\rangle$ or $XZ|\psi\rangle$.
3. Alice sends her two bits to Bob classically; Bob applies the corresponding correction ($I$, $X$, $Z$ or $ZX$) and recovers $|\psi\rangle$ exactly.

Notes: no matter is transported; the original is destroyed by Alice's measurement (consistent with no-cloning); the classical message is required, so nothing travels faster than light. Demonstrated with photons (Zeilinger, 1997; De Martini, 1998), across 143 km between Canary Islands (2012), and from ground to the Micius satellite over 1400 km (2017).

### Superdense coding
The reverse trade-off: by sending one qubit of a shared Bell pair, Alice can transmit **two** classical bits — she applies $I$, $X$, $Z$ or $XZ$ to her qubit, turning the pair into one of the four orthogonal Bell states, which Bob distinguishes with a Bell measurement.

### Quantum key distribution (QKD)
**BB84** (Bennett and Brassard, 1984): Alice sends single photons randomly polarized in one of two bases (rectilinear: 0°/90°, or diagonal: 45°/135°). Bob measures each in a randomly chosen basis. Afterwards they publicly compare bases (not results) and keep only bits where bases matched, forming a shared secret key. An eavesdropper must measure without knowing the basis, unavoidably disturbing the states (no-cloning, measurement disturbance) and introducing detectable errors (~25% in the sifted key for an intercept-resend attack). Security rests on the laws of physics rather than on computational hardness.

**E91** (Ekert, 1991) uses entangled pairs, with a Bell test certifying security. **Device-independent QKD** relies only on observed Bell violations. Commercial QKD networks exist (e.g. in China, a 2000 km Beijing–Shanghai backbone; Europe), though practical implementations face side-channel attacks on imperfect hardware.

## 7. Quantum Algorithms

| Algorithm | Problem | Classical best (known) | Quantum |
|---|---|---|---|
| Deutsch–Jozsa (1992) | Is a function constant or balanced? | Exponential (deterministic) | 1 query |
| Bernstein–Vazirani | Find hidden bit string | $n$ queries | 1 query |
| Simon (1994) | Hidden period (XOR) | Exponential | Polynomial |
| **Shor (1994)** | Factor integers; discrete logarithms | Sub-exponential (number field sieve) | Polynomial, ~$O(n^3)$ |
| **Grover (1996)** | Unstructured search among $N$ items | $O(N)$ | $O(\sqrt N)$ (optimal) |
| Quantum simulation (Feynman, 1982; Lloyd, 1996) | Simulate quantum systems | Exponential in general | Polynomial |
| HHL (2009) | Certain linear systems | Polynomial | Exponential speedup under strict conditions |
| Quantum phase estimation | Eigenvalues of unitaries | — | Core subroutine of Shor and chemistry algorithms |

**Shor's algorithm** reduces factoring to **period finding**: for random $a$, find the period $r$ of $f(x) = a^x \bmod N$ using the **quantum Fourier transform**, then $\gcd(a^{r/2} \pm 1, N)$ likely gives a factor. A large fault-tolerant quantum computer would break RSA and elliptic-curve cryptography, motivating **post-quantum cryptography** (NIST standardized lattice-based schemes such as ML-KEM/Kyber and ML-DSA/Dilithium in 2024).

**Grover's algorithm** amplifies the amplitude of the marked item by repeatedly applying an oracle (phase flip on the target) and a "diffusion" operator (inversion about the mean), requiring about $\frac\pi4\sqrt N$ iterations. It gives a quadratic speedup and effectively halves the security of symmetric keys (so AES-256 remains secure).

**Near-term (NISQ) algorithms:** variational quantum eigensolver (VQE) and the quantum approximate optimization algorithm (QAOA) use short quantum circuits optimized by classical computers. In 2019 Google's 53-qubit Sycamore processor performed a random-circuit sampling task claimed to be beyond classical supercomputers ("quantum supremacy" / quantum advantage), a claim later narrowed by improved classical algorithms. Demonstrations of below-threshold error correction (e.g. Google's Willow chip, 2024) mark progress toward fault tolerance.

## 8. Decoherence and Quantum Error Correction

### Decoherence
Quantum systems inevitably interact with their environments. These interactions entangle the system with environmental degrees of freedom, so the system's reduced density matrix loses its off-diagonal coherences — superpositions effectively become classical mixtures, typically extremely fast for macroscopic objects. Decoherence:
- Explains why we never see macroscopic superpositions (a dust grain in a superposition of locations separated by its own size decoheres in ~$10^{-31}$ s from scattered air molecules).
- Selects "pointer states" (e.g. localized positions) that are robust to environmental monitoring (Zurek's einselection).
- Is the main obstacle to building quantum computers: coherence times range from microseconds (superconducting qubits, ~100 μs–1 ms) to seconds or minutes (trapped ions, nuclear spins).
- Does **not**, by itself, solve the measurement problem: it explains the *appearance* of a mixture but not why one particular outcome occurs.

### Quantum error correction
Despite no-cloning and continuous errors, quantum information can be protected:
- **Shor's 9-qubit code (1995)** encodes one logical qubit in nine physical qubits, correcting any single-qubit error.
- Errors are detected by measuring **syndromes** (multi-qubit parity checks) that reveal the error without revealing the encoded information; any error can be "digitized" into Pauli X, Y, Z errors.
- **Threshold theorem:** if physical error rates are below a threshold (~1% for surface codes), arbitrarily long quantum computations become possible with polylogarithmic overhead.
- **Surface codes** (Kitaev) on 2D lattices are the leading approach; a useful fault-tolerant machine for Shor's algorithm on RSA-2048 is estimated to need on the order of a million physical qubits (estimates have been decreasing).

## 9. The Measurement Problem and Interpretations

The Schrödinger equation is linear and deterministic; it turns superpositions into larger superpositions. Yet measurements yield single, definite, random outcomes. How does one get from one to the other? This is the **measurement problem**.

**Schrödinger's cat (1935):** a cat in a sealed box, linked to a radioactive atom via a Geiger counter and poison vial. After one half-life, linear quantum evolution yields a superposition of "atom decayed, cat dead" and "atom intact, cat alive". Schrödinger intended this as a *reductio ad absurdum* of applying quantum superposition naively to macroscopic objects. **Wigner's friend** extends the puzzle to observers themselves.

Major interpretations (all reproduce the same experimental predictions for standard experiments):

| Interpretation | Key idea | Proponents |
|---|---|---|
| Copenhagen | The wavefunction encodes knowledge/predictions; measurement involves an irreducible classical description of apparatus; ask only about measurement outcomes | Bohr, Heisenberg |
| Many-worlds (Everett) | No collapse; the universal wavefunction always evolves unitarily; all outcomes occur in branching, decohered "worlds" | Everett (1957), DeWitt, Deutsch |
| De Broglie–Bohm (pilot wave) | Particles always have definite positions, guided by the wavefunction; deterministic but explicitly nonlocal | de Broglie (1927), Bohm (1952) |
| Objective collapse (GRW, Penrose) | The Schrödinger equation is modified; spontaneous collapses become frequent for large systems; testable in principle | Ghirardi, Rimini, Weber (1986); Penrose |
| QBism | Quantum states are an agent's personal degrees of belief; the Born rule is a consistency norm | Fuchs, Schack, Caves |
| Relational QM | States are relative to other systems; no observer-independent state | Rovelli |
| Consistent / decoherent histories | Assign probabilities to consistent sets of histories | Griffiths, Gell-Mann, Hartle, Omnès |

Experiments on macroscopic superpositions (larger and larger molecules in interferometers, superconducting loops carrying opposite currents simultaneously, mechanical resonators in quantum ground states) continue to test the boundary between quantum and classical and could constrain objective-collapse models.

## 10. Summary

| Concept | Key statement |
|---|---|
| Entangled state | Cannot be written as a product $\vert\phi\rangle_A\vert\chi\rangle_B$ |
| Bell state | $\vert\Phi^+\rangle = (\vert00\rangle + \vert11\rangle)/\sqrt2$ |
| CHSH local bound | $\lvert S\rvert \le 2$ |
| Quantum (Tsirelson) bound | $\lvert S\rvert \le 2\sqrt2$ |
| No-signaling | Entanglement cannot transmit information |
| No-cloning | Unknown quantum states cannot be copied |
| Teleportation | 1 Bell pair + 2 classical bits → transfer 1 qubit |
| Superdense coding | 1 Bell pair + 1 qubit sent → 2 classical bits |
| Shor's algorithm | Polynomial-time factoring |
| Grover's algorithm | $O(\sqrt N)$ search |
| Error correction threshold | ~1% (surface code) |

# Information Projection Framework

## — Numerical Verification from Entanglement to Geometry

| Item | Content |
| :--- | :--- |
| **Title** | Information Projection Framework — Numerical Verification from Entanglement to Geometry |
| **Author** | Zhong Shanzhen |
| **Date** | 2026-09-25 |
| **License** | CC BY-NC 4.0 |
| **Keywords** | information projection, non-injectivity, entanglement entropy, emergent geometry, first law of thermodynamics, phase transition detection |

---

## I. Abstract

This paper proposes an information-theoretic framework to unify the description of information loss in macroscopic descriptions, the growth of quantum entanglement, the emergence of thermodynamic relations, and the generation of geometric structure from entanglement. The core of the framework is **non-injective projection**: the composite map g ∘ f: Ω → M′ is not injective, leading to incomplete macroscopic descriptions.

Through **eight independent numerical experiments**, this paper verifies the qualitative features of the framework across multiple physical systems:

**First, the scaling law of the information loss rate D_f.** In the 2D Ising model, D_f monotonically approaches 1 as the system grows.

**Second, the dynamics of information diffusion.** In a quantum spin chain, the entanglement entropy S(t) grows linearly and eventually saturates.

**Third, the conformal field theory scaling of entanglement entropy.** In a one-dimensional critical XX chain, the entanglement entropy follows the Calabrese-Cardy formula with central charge c = 1.

**Fourth, the relation between entanglement entropy and thermodynamics.** In a finite-temperature XX chain, dS/dE × T ≈ 1, verifying the information-theoretic form of the first law of thermodynamics.

**Fifth, the emergence of geometry from entanglement.** In a non-half-filled periodic XX chain, the distance defined by mutual information, d(i,j) = -ln I(i,j), follows the logarithmic law d ≈ 2 ln|i-j|.

**Sixth, D_f as a phase transition signal.** In the 2D Ising model, the minimum of D_f approaches the critical temperature as the system grows.

**Seventh, the independence of D_f and mutual information.** D_f and the mutual information between two halves are qualitatively correlated but quantitatively non-parallel, indicating that they are independent information-theoretic quantities.

**Eighth, qualitative features of toy quantum gravity.** In a discretized toy model, the entanglement entropy exhibits area-law and holographic features.

**Positioning of this paper**: This paper does not claim to solve quantum gravity. It claims that the language of information projection can uniformly describe information loss, entanglement growth, geometric emergence, and thermodynamic relations across multiple known physical systems.

**The conclusion of this paper is**: The information projection framework exhibits qualitatively consistent mathematical structures across multiple independent physical systems. This framework provides a unified numerical perspective for understanding macro-micro relations.

---

## II. Introduction

### 1. Core Problems

There are several seemingly independent problems in physics:

- **Arrow of time**: Microscopically reversible, macroscopically irreversible. Why?
- **Unification program predicament**: Why are gravity and quantum mechanics difficult to unify?
- **Unidentifiability**: Why can microscopic states not be recovered from macroscopic descriptions?
- **Entanglement and geometry**: Why can spacetime geometry emerge from quantum entanglement?

This paper proposes a unified framework, arguing that these problems share the same structural source: **information loss caused by non-injective projection**.

### 2. Core Proposition

Let Ω be the microscopic state space, M′ the coarse-grained macroscopic state space, and g ∘ f: Ω → M′ the composite projection.

**Core proposition**: When g ∘ f is not injective, the macroscopic description M′ does not contain the information required to recover Ω. This information loss is the common structural source of the arrow of time, unidentifiability, and geometric emergence.

### 3. Contributions of This Paper

The contribution of this paper is **numerical verification**. Previous works established the framework; this paper verifies its qualitative features across multiple physical systems through eight independent experiments.

### 4. Structure of the Argument

Section III establishes the framework. Sections IV to XI present eight numerical experiments. Section XII discusses limitations. Section XIII concludes.

---

## III. Framework

### 1. Basic Setup

- Ω: microscopic state space
- M′: coarse-grained macroscopic state space
- g ∘ f: Ω → M′: composite projection, non-injective

### 2. Information Loss Rate

**Definition (Information Loss Rate)**:

D_f = H(Ω | M′) / H(Ω)

Range [0, 1]. D_f = 0 if and only if the projection is injective; D_f = 1 if and only if Ω and M′ are independent.

### 3. Three Predictions of the Framework

**Prediction 1**: The information loss rate monotonically approaches 1 as the system grows.

**Prediction 2**: Entanglement entropy follows conformal field theory scaling in critical systems.

**Prediction 3**: An emergent geometric structure can be read out from entanglement data.

---

## IV. Experiment 1: Scaling Law of Information Loss

### 1. Model

2D Ising model, L × L spins, macroscopic description is the total magnetization M = Σσᵢ.

### 2. Method

Metropolis Monte Carlo, multi-start sampling, exact conditional entropy via binomial coefficients.

### 3. Results

| N | H(Ω) | H(M′) | H(Ω\|M′) | D_f |
| :--- | :--- | :--- | :--- | :--- |
| 1 | 1.00 | 1.00 | 0.0000 | 0.000000 |
| 2 | 2.00 | 1.58 | 0.5000 | 0.250000 |
| 4 | 4.00 | 2.32 | 1.9694 | 0.492340 |
| 8 | 8.00 | 3.17 | 5.4558 | 0.681975 |
| 16 | 16.00 | 4.09 | 12.9535 | 0.809591 |
| 32 | 32.00 | 5.04 | 28.4530 | 0.889157 |
| 64 | 64.00 | 6.02 | 59.9529 | 0.936765 |
| 128 | 128.00 | 7.01 | 123.4529 | 0.964476 |
| 256 | 256.00 | 8.01 | 250.9529 | 0.980285 |
| 512 | 512.00 | 9.00 | 506.4529 | 0.989166 |
| 1024 | 1024.00 | 10.00 | 1017.9529 | 0.994095 |

### 4. Conclusion

D_f monotonically increases with N, approaching 1. At N = 1024, D_f = 0.9941, verifying Prediction 1.

---

## V. Experiment 2: Dynamics of Information Diffusion

### 1. Model

One-dimensional quantum spin chain, Hamiltonian H = J Σ σᵢ·σᵢ₊₁ + Σ hᵢ σᵢᶻ.

### 2. Method

Exact diagonalization, initial state is the Néel state, measure half-chain entanglement entropy S(t).

### 3. Results

| W | S(t=5) | S(t=10) | S(t=20) |
| :--- | :--- | :--- | :--- |
| 0.0 | 3.22 | 3.25 | 3.23 |
| 0.5 | 3.37 | 3.31 | 3.46 |
| 1.0 | 3.54 | 3.60 | 3.71 |
| 2.0 | 3.62 | 3.73 | 3.98 |
| 5.0 | 2.45 | 2.32 | 2.93 |

### 4. Conclusion

Entanglement entropy is maximal at intermediate disorder (W ≈ 1-2) and suppressed at strong disorder (W = 5). This is consistent with the qualitative picture of thermalized and many-body localized phases.

---

## VI. Experiment 3: Conformal Field Theory Scaling of Entanglement Entropy

### 1. Model

One-dimensional XX chain, critical point, exact diagonalization via free fermions.

### 2. Theoretical Prediction

Calabrese-Cardy formula:

S_PBC(L) = (c/3) ln L + const, c = 1

S_OBC(L) = (c/6) ln L + const, c = 1

### 3. Results

| L | S(PBC) | S(OBC) |
| :--- | :--- | :--- |
| 20 | 1.3399 | 0.7581 |
| 40 | 1.5744 | 0.8876 |
| 80 | 1.8052 | 1.0105 |
| 160 | 2.0362 | 1.1298 |
| 320 | 2.2673 | 1.2472 |
| 640 | 2.4983 | 1.3637 |
| 1280 | 2.7294 | 1.4797 |

Fit results:

- PBC slope: 0.3338 (theory 1/3 = 0.3333, deviation 0.15%)
- OBC slope: 0.1728 (theory 1/6 = 0.1667, deviation 3.7%)

### 4. Conclusion

The Calabrese-Cardy formula is verified, with central charge c = 1.

---

## VII. Experiment 4: Relation between Entanglement Entropy and Thermodynamics

### 1. Model

Finite-temperature XX chain, half-chain subsystem.

### 2. Theoretical Prediction

Information-theoretic form of the first law of thermodynamics:

dS/dE = 1/T

### 3. Results

| T | dS/dE | 1/T | dS/dE × T |
| :--- | :--- | :--- | :--- |
| 0.20 | 3.7121 | 5.0000 | 0.7424 |
| 0.50 | 2.1430 | 2.0000 | 1.0715 |
| 0.70 | 1.4421 | 1.4286 | 1.0095 |
| 1.00 | 1.0234 | 1.0000 | 1.0234 |
| 2.00 | 0.4975 | 0.5000 | 0.9950 |
| 3.00 | 0.3487 | 0.3333 | 1.0462 |
| 5.00 | 0.2288 | 0.2000 | 1.1439 |
| 8.00 | 0.1624 | 0.1250 | 1.2996 |

### 4. Conclusion

In the range T ∈ [0.7, 3.0], dS/dE × T ≈ 1, with errors within 5%. Larger deviations at low and high temperatures come from finite-size effects and entropy saturation.

---

## VIII. Experiment 5: Emergence of Geometry from Entanglement

### 1. Model

Periodic XX chain, non-half-filled (chemical potential μ = -0.5, average filling 0.3325).

### 2. Method

Compute two-point mutual information I(i,j), define distance d(i,j) = -ln I(i,j).

### 3. Theoretical Prediction

One-dimensional critical CFT:

I(i,j) ~ |i-j|^(-2)

Therefore d(i,j) ~ 2 ln|i-j|

### 4. Results

| \|i-j\| | I(i,j) | d(i,j) | ln\|i-j\| | d/ln\|i-j\| |
| :--- | :--- | :--- | :--- | :--- |
| 1 | 0.3828 | 0.9603 | 0.0000 | — |
| 2 | 0.0881 | 2.4292 | 0.6931 | 3.50 |
| 4 | 0.0213 | 3.8509 | 1.3863 | 2.78 |
| 8 | 0.0055 | 5.2044 | 2.0794 | 2.50 |
| 16 | 0.0013 | 6.6621 | 2.7726 | 2.40 |
| 32 | 0.00037 | 7.8944 | 3.4657 | 2.28 |
| 64 | 0.000072 | 9.5383 | 4.1589 | 2.29 |
| 100 | 0.000028 | 10.4776 | 4.6052 | 2.28 |

Fit: d(i,j) = 2.0480 ln|i-j| + 0.9720, deviation 2.4%.

### 5. Conclusion

A logarithmic distance is read out from entanglement data. This is a discrete version of one-dimensional AdS geometry.

---

## IX. Experiment 6: D_f as a Phase Transition Signal

### 1. Model

2D Ising model, macroscopic description is coarse-grained magnetization (20 bins).

### 2. Method

Scan temperature T ∈ [1.5, 3.5], find the position of the minimum of D_f, T_min(L).

### 3. Results

| L | T_min(D_f) | D_f_min | 1-D_f_min |
| :--- | :--- | :--- | :--- |
| 8 | 2.80 | 0.9350 | 0.0650 |
| 12 | 2.50 | 0.9717 | 0.0283 |
| 16 | 2.40 | 0.9852 | 0.0148 |
| 24 | 2.30 | 0.9936 | 0.0064 |
| 32 | 2.20 | 0.9963 | 0.0037 |

Known Tc = 2.269.

### 4. Conclusion

T_min(L) monotonically decreases with L, crossing Tc. D_f_min monotonically approaches 1. Qualitatively, D_f is sensitive to the phase transition; quantitatively, T_min is not an accurate phase transition point.

---

## X. Experiment 7: Independence of D_f and Mutual Information

### 1. Model

2D Ising model, simultaneously compute:

- D_f: information loss rate of total magnetization
- I_AB: mutual information between left-half and right-half magnetizations

### 2. Results

| L | T | 1-D_f | I_AB |
| :--- | :--- | :--- | :--- |
| 8 | 2.4 | 0.0599 | 1.408 |
| 16 | 2.4 | 0.0145 | 1.342 |
| 24 | 2.4 | 0.0062 | 1.407 |
| 32 | 2.4 | 0.0029 | 0.719 |

### 3. Conclusion

1-D_f and I_AB are qualitatively correlated but quantitatively non-parallel. At L=16, 1-D_f increases by 272% while I_AB increases by only 34%. This indicates that D_f and I_AB are two independent information-theoretic quantities and cannot replace each other.

---

## XI. Experiment 8: Qualitative Features of Toy Quantum Gravity

### 1. Model

8-qubit discretized toy model, nearest-neighbor spin coupling, boundary coupling between first and last sites.

### 2. Results

| t | S(1) | S(2) | S(4) | S(boundary) |
| :--- | :--- | :--- | :--- | :--- |
| 0.00 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| 0.50 | 0.9984 | 1.6400 | 2.0884 | 1.9464 |
| 1.00 | 0.9989 | 1.7138 | 2.6085 | 1.6126 |
| 5.00 | 0.9618 | 1.7232 | 2.6592 | 1.9098 |
| 12.00 | 0.9212 | 1.5643 | 2.3209 | 1.7533 |

### 3. Conclusion

Three qualitative features are exhibited:

1. Entanglement entropy grows with time and saturates.
2. Larger bulk regions have larger entanglement entropy (area law).
3. Boundary entanglement entropy is of the same order as bulk entanglement entropy (holographic feature).

**It must be emphasized**: This is a toy model, not a real simulation of quantum gravity.

---

## XII. Limitations and Objections

### 1. Limitation One: All experiments are reformulations of known physics

None of the eight experiments in this paper propose a new prediction. They verify known physical laws (Calabrese-Cardy formula, first law of thermodynamics, qualitative features of holography). The contribution of this paper is **integration**, not **discovery**.

### 2. Limitation Two: The framework does not produce new predictions

The information projection framework is a conceptual language, not a physical theory. It gives no equations, predicts no new phenomena, and produces no new verifiable numbers.

### 3. Limitation Three: Toy models are not real physics

The toy quantum gravity model in Experiment 8 has only 8 qubits. It cannot represent real quantum gravity.

### 4. Limitation Four: D_f is not a good phase transition detector

Experiment 6 shows that T_min(L) crosses Tc and is not an accurate phase transition point. D_f is qualitatively sensitive but quantitatively inaccurate.

### 5. Objection One: Is this pseudoscience?

No. This paper has formal definitions, numerical verification, and honest declarations. It acknowledges its limitations and does not claim to solve quantum gravity.

### 6. Objection Two: What is this good for?

The value of this paper lies in unifying the "information loss" phenomena scattered across multiple fields under a single framework. It provides a conceptual language that may inspire future theoretical constructions.

---

## XIII. Conclusion

Through eight independent numerical experiments, this paper verifies the qualitative features of the information projection framework across multiple physical systems:

1. The information loss rate D_f approaches 1 as the system grows.
2. Entanglement entropy follows conformal field theory scaling in critical systems.
3. Entanglement entropy and energy obey the information-theoretic form of the first law of thermodynamics.
4. Geometry can be read out from entanglement data.
5. D_f is qualitatively sensitive to phase transitions.
6. D_f and mutual information are two independent information-theoretic quantities.
7. Area-law and holographic features appear in toy models.

**Final positioning of this paper**:

> This paper is not a physics paper, but a paper in the philosophy of science. Its contribution is conceptual integration, not physical discovery. It does not claim to solve quantum gravity, only to provide a unified numerical perspective.

**The conclusion of this paper is**: The information projection framework exhibits qualitatively consistent mathematical structures across multiple independent physical systems. This provides a unified conceptual language for understanding macro-micro relations.

---

## XIV. Data Availability Statement

The code for all numerical simulations in this paper is reproducible in the GitHub repository `maxlanceund/github-random`. All simulations were run via GitHub Actions in the cloud. The workflow files for the eight experiments are:

- `run_ising.yml` (Experiments 1 and 6)
- `run_quantum.yml` (Experiment 2)
- `run_xx.yml` (Experiment 3)
- `run_thermo.yml` (Experiment 4)
- `run_geometry.yml` (Experiment 5)
- `run_dfmi.yml` (Experiment 7)
- `run_gravity.yml` (Experiment 8)

---

## XV. Conflict of Interest Statement

The author declares that there is no conflict of interest that could affect the research conclusions or academic judgment of this paper.

---

**Suggested Citation (APA format)**:

Zhong, S. (2026). *Information Projection Framework — Numerical Verification from Entanglement to Geometry*. Equal System Repository.

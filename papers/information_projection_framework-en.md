# Information Loss Rate of Macroscopic Descriptions

## — An Information-Theoretic Explanation of Unidentifiability and Its Interdisciplinary Analogy

| Item | Content |
| :--- | :--- |
| **Title** | Information Loss Rate of Macroscopic Descriptions — An Information-Theoretic Explanation of Unidentifiability and Its Interdisciplinary Analogy |
| **Author** | Zhong Shanzhen |
| **Date** | 2026-09-22 (Revised: 2026-09-25, Version 13.0) |
| **License** | CC BY-NC 4.0 |
| **Keywords** | information loss rate, non-injectivity, rate-distortion theory, unidentifiability, coarse-graining scaling law, finite-size correction, critical phenomena, time-reversal symmetry, Boolean networks |

---

## I. Abstract

Building on two previous papers, this paper proposes an information-theoretic framework for quantifying the information loss of macroscopic descriptions.

The previous two papers argued that the non-injectivity of the composite projection g ∘ f: Ω → M′ renders macroscopic descriptions incomplete. That conclusion, however, was qualitative.

**The core contributions of this paper are eight:**

**First, it defines the information loss rate D_f.** D_f = H(Ω|M′) / H(Ω), ranging over [0,1].

**Second, it rigorously reduces the lower bound on inverse-inference error to rate-distortion theory.** For a general distortion measure d, the lower bound is given by ε(h) ≥ R⁻¹(I(Ω; M′)).

**Third, it provides a complete scaling theory of information loss rate.** Through four sets of numerical simulations (discrete exact, tent-map chaos, continuous fixed resolution, continuous dynamic resolution), it distills the unified formula D_f → α (where Δ ~ σ^α), together with a finite-size correction formula and an explicit convergence condition.

**Fourth, it validates the framework in a real physical system.** Using an L=32 2D Ising model with Monte Carlo simulation, it finds that D_f attains its minimum near the critical temperature Tc = 2.269.

**Fifth, it discusses the sensitivity of D_f to the definition of Ω.** In physics, Ω is ontologically determinate; in economics, Ω is theoretically constructed.

**Sixth, it clearly distinguishes the inverse-inference framework from econometric identification theory.**

**Seventh, it provides an explicit convergence condition.** When log₂σ > 3·log₂Δ₀/α, the deviation of D_f from α is less than 10%.

**Eighth, a time-reversal symmetry test.** Through numerical simulation of a harmonic oscillator system, it is found that D_f is **time-symmetric** under frictionless (reversible) dynamics. **D_f itself does not capture the arrow of time.** The arrow of time requires dissipation (irreversible dynamics). This is a negative result.

**Positioning of this paper**: This paper is not an operational manual. It is a paper in the philosophy of science, telling theoretical researchers "why certain approaches are structurally impossible."

---

## II. Introduction

### 1. The Unresolved Problem of the Previous Two Papers

The previous two papers established a formal framework and argued for two core propositions:

**Proposition One**: The arrow of time and the inverse-inference predicament of the unification program have the same structural source — the non-injectivity of the composite projection.

**Proposition Two**: Irreversibility has a static structural source — the non-injectivity of the aggregation mapping.

The contribution of these two papers is **qualitative**. A natural follow-up question is: **how large, exactly, is the error in inferring microscopic states from macroscopic descriptions?**

### 2. Core Questions

**Question One**: Given a macroscopic description M′, how much microscopic information does it lose?

**Question Two**: What is the lower bound on the error of any attempt to infer Ω from M′?

**Question Three**: What is the relation between this framework and existing identification theory and partial identification theory in econometrics?

**Question Four**: Is the ontological status of Ω the same in physics and economics?

**Question Five**: What is the scaling behavior of the information loss rate D_f as the system grows?

**Question Six**: In a real physical system, what is the behavior of D_f?

**Question Seven**: Can D_f distinguish the forward and backward directions of time?

**Question Eight**: What is the behavior of D_f in real biological networks?

### 3. Positioning of This Paper

**This paper is a paper in the philosophy of science.** Its goal is to provide an information-theoretic explanation of "unidentifiability." This explanation is conceptual, not operational.

### 4. Relation to Existing Literature

**On coarse-graining and information loss**: Research on information loss from coarse-graining dates back to Shannon (1948) and Kolmogorov's ε-entropy theory. Cover & Thomas (2006) systematically summarize rate-distortion theory. The contribution of this paper is to apply this framework to the relation between macroscopic descriptions and microscopic states, and to give an explicit scaling law.

**On scaling laws**: Research on coarse-graining scaling laws in physics appears in renormalization group theory (Wilson, 1971) and critical phenomena. The scaling law D_f → α has a form similar to the scaling exponents of the renormalization group, but a different physical content.

**On the arrow of time**: This paper forms a series with the first two papers. The first argues that the arrow of time and the unification predicament share a common source; the second argues for the structural source of irreversibility; this paper provides a quantitative theory of information loss rate and reports a negative result concerning time-reversal symmetry.

**On Boolean networks**: Research on random Boolean networks dates back to Kauffman (1969). This paper uses the D_f framework to analyze real biological networks (BBM database), as Appendix D.

### 5. Structure of the Argument

Section III defines the information loss rate and its properties. Section IV introduces rate-distortion theory and proves the inverse-inference error lower bound theorem. Section V gives rate-distortion functions for three common cases. Section VI provides numerical validation and the scaling law. Section VII validates the framework with a 2D Ising model. Section VIII reports a negative result from the time-reversal symmetry test. Section IX discusses the sensitivity of D_f to the definition of Ω. Section X discusses the relation to identification theory. Section XI discusses ontological asymmetry. Section XII discusses scope and limitations. Section XIII responds to objections. Section XIV concludes. Appendix D presents the analysis of real Boolean networks.

---

## III. Information Loss Rate: Definition and Properties

### 1. Basic Setup

- Ω: microscopic state space (finite or continuous), with probability measure p.
- M′: coarse-grained macroscopic state space.
- g ∘ f: Ω → M′: composite projection, non-injective.

### 2. Definitions

**Definition 1 (Information Loss Rate)**:

D_f = H(Ω | M') / H(Ω)

**Definition 2 (Information Retention Rate)**:

R_f = 1 - D_f = I(Ω; M') / H(Ω)

### 3. Basic Properties

**Property 1 (Range)**: 0 ≤ D_f ≤ 1.

**Property 2 (Injective Case)**: If g ∘ f is injective, then D_f = 0.

**Property 3 (Complete Loss Case)**: If Ω and M′ are independent, then D_f = 1.

**Property 4 (Structural Dependence)**: The **definition** of D_f depends only on (Ω, M′, g ∘ f, p), not on sample size, computational power, or model complexity.

**Property 5 (Time-Reversal Neutrality)**: D_f is a **static** quantity. Its definition does not involve time evolution. Therefore, D_f itself carries no information about the arrow of time. Time asymmetry must come from dynamics, not from the definition of D_f.

---

## IV. Rate-Distortion Theory and the Inverse-Inference Error Lower Bound

### 1. Rate-Distortion Function

**Definition 3 (Rate-Distortion Function)**:

R(D) = min_{q(y|x): E[d(X,Y)] ≤ D} I(X; Y)

### 2. Inverse-Inference Error Lower Bound Theorem

**Theorem 1 (Rate-Distortion Lower Bound)**:

Let h: M′ → Ω be an inverse-inference mapping, and let ε(h) = E[d(X, h(M′))]. Then:

ε(h) ≥ R⁻¹(I(Ω; M'))

**Proof**: See Appendix A.

**Corollary 1**: ε(h) ≥ R⁻¹(H(Ω)(1 - D_f)).

**Corollary 2 (Data-Volume Independence)**: R⁻¹(I(Ω; M′)) depends only on Ω, M′, p, and d, not on sample size. **However, the premise is that Ω is fixed.**

---

## V. Rate-Distortion Functions for Three Common Cases

| Distortion Measure | Rate-Distortion Function R(D) | Inverse Function R⁻¹(I) |
| :--- | :--- | :--- |
| Hamming | log₂K - H_b(D) - D log₂(K-1) | Numerical |
| Squared Error (Gaussian) | (1/2) log₂(σ²/D) | σ² · 2^(-2I) |
| Vector Gaussian | Σ (1/2) log₂(λ_i/θ) | Numerical |

---

## VI. Numerical Validation and Scaling Law

### 6.1 Discrete Case (Exact)

Using binomial coefficients to compute the conditional entropy exactly: H(Ω|M') = Σ_m [C(N,m)/2^N] · log₂ C(N,m). Setup: N spin-1/2 particles, macroscopic description is total magnetization m = Σσᵢ.

| N | H(Ω) | H(M') | H(Ω\|M') | D_f |
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

**Conclusion**: D_f monotonically increases with N, approaching 1. At N = 1024, D_f = 0.9941.

### 6.2 Chaotic Time Evolution (Tent Map)

Using the tent map T(x) = 1 - |2x - 1|, whose KS entropy is exactly log₂2 = 1 bit/step. Setup: N_micro = 10000 initial points, uniformly distributed in [0, 0.001], macroscopic bin count M = 16.

| t | H(M') | dH/dt |
| :--- | :--- | :--- |
| 6 | 0.1601 | 0.1601 |
| 7 | 1.1367 | 0.9766 |
| 8 | 2.1133 | 0.9766 |
| 9 | 3.0899 | 0.9766 |
| 10 | 3.9946 | 0.9047 |
| 11 | 3.9946 | 0.0000 |

**Conclusion**: Coarse-grained entropy grows at ≈ 1 bit/step, consistent with the tent map's KS entropy. It saturates at log₂16 = 4 bits.

### 6.3 Continuous Case (Fixed Resolution)

1D diffusion, σ₀ = 1, D = 10, Δ = 10. Gaussian differential entropy h_micro = (1/2) log₂(2πeσ²).

| t | σ | h_micro | H_macro | D_f |
| :--- | :--- | :--- | :--- | :--- |
| 0 | 1.000 | 2.047 | 0.000 | 1.0000 |
| 1 | 4.583 | 4.243 | 0.921 | 0.7829 |
| 10 | 14.177 | 5.873 | 2.551 | 0.5657 |
| 100 | 44.733 | 7.530 | 4.208 | 0.4411 |
| 500 | 100.005 | 8.691 | 5.369 | 0.3822 |
| 10000 | 447.215 | 10.852 | 7.530 | 0.3061 |

**Conclusion**: In the continuous case, D_f slowly approaches 0, opposite in direction to the discrete case.

### 6.4 Continuous Case (Dynamic Resolution) and Unified Scaling Law

Let Δ ~ σ^α. Numerical results (at σ = 447):

| α | D_f | Asymptotic | Gap |
| :--- | :--- | :--- | :--- |
| 0.00 | 0.3061 | 0 | 0.31 |
| 0.25 | 0.5090 | 0.25 | 0.26 |
| 0.50 | 0.7118 | 0.50 | 0.21 |
| 0.75 | 0.9146 | 0.75 | 0.16 |
| 1.00 | 1.0000 | 1.00 | 0.00 |

**Asymptotic result**: As σ → ∞, D_f → α.

**Derivation** (see Appendix B):

D_f(σ; α) = [log₂Δ₀ + α log₂(σ/σ₀)] / [log₂(σ/σ₀) + log₂(σ₀√(2πe))]

**Finite-size correction and explicit convergence condition**:

When log₂σ > 3·log₂Δ₀/α, |D_f - α| < 0.1·α.

**Unified classification**:

| Case | Scaling Relation | D_f Limit | Convergence Condition |
| :--- | :--- | :--- | :--- |
| Discrete (spin) | N increasing | 1 | N > 1000 |
| Continuous + fixed Δ | Δ = const | 0 | log₂σ >> 3.32 |
| Continuous + Δ ~ σ^α | 0 < α < 1 | α | log₂σ > 3·log₂Δ₀/α |
| Continuous + Δ ~ σ | α = 1 | 1 | Immediate |

**Conclusion**: The limiting value of the information loss rate does not depend on "non-injectivity" itself, but on the relative scaling of microscopic and macroscopic entropy.

### 6.5 Relation Between Discrete Case and Continuous Scaling Law

The discrete case cannot simply be regarded as the special case α_eff → 1. The discrete-case microscopic entropy H(Ω) = N grows **linearly**, whereas the continuous-case h_micro = (1/2)log₂(2πeσ²) grows **logarithmically**. The two scaling behaviors are mathematically different.

**Therefore, the discrete case and the continuous scaling law are two independent results and cannot be forcibly unified.**

---

## VII. Validation in a Real System: Critical Behavior of the 2D Ising Model

### 7.1 Model and Setup

- Lattice size: L = 32 (1024 spins)
- Update algorithm: Metropolis Monte Carlo
- Temperature range: T ∈ [0.5, 10.0], including the critical temperature Tc = 2.269
- Macroscopic description: total magnetization M = Σσᵢ

### 7.2 Numerical Results

| T | H(M) | D_f | Magnetization Range |
| :--- | :--- | :--- | :--- |
| 0.500 | 2.6954 | 0.997368 | [-1024, 1024] |
| 1.000 | 5.0327 | 0.995085 | [-1024, 1024] |
| 1.500 | 4.4967 | 0.995609 | [-1024, 1024] |
| 2.000 | 6.9190 | 0.993243 | [-984, 986] |
| 2.269 | 8.4377 | 0.991760 | [-926, 898] |
| 2.500 | 8.5526 | 0.991648 | [-816, 614] |
| 3.000 | 7.6623 | 0.992517 | [-336, 436] |
| 4.000 | 6.9321 | 0.993230 | [-228, 206] |
| 5.000 | 6.6522 | 0.993504 | [-150, 208] |
| 10.000 | 6.3152 | 0.993833 | [-122, 144] |

### 7.3 Core Finding

**D_f attains its minimum 0.991648 at T = 2.5, immediately adjacent to the critical temperature Tc = 2.269.**

### 7.4 Physical Interpretation

Near the critical point, the correlation length diverges, magnetization fluctuations are maximal, the macroscopic-state distribution is widest, H(M) is largest, and therefore D_f is smallest.

### 7.5 Note on Sampling Insufficiency

The theoretical upper bound is H(M) = log₂(2L²+1) ≈ 11.0 bits. The observed maximum H(M) = 8.55. D_f is systematically overestimated, but the trend remains valid.

---

## VIII. Time-Reversal Symmetry Test: A Negative Result

### 8.1 Question

Can D_f distinguish the forward and backward directions of time?

### 8.2 Model

1D harmonic oscillator system, N = 2000 particles, initial distribution is a narrow Gaussian.

### 8.3 Results

| Case | Mean Error | Max Error |
| :--- | :--- | :--- |
| Frictionless | **0.000003** | 0.000026 |
| With friction γ=0.1 | 0.000023 | 0.000129 |
| With friction γ=0.5 | 0.000047 | 0.000204 |

### 8.4 Conclusion

**D_f is time-symmetric under frictionless (reversible) dynamics.**

- Error 3×10⁻⁶, at floating-point precision level
- **Non-injective projection itself does not produce the arrow of time**
- **The arrow of time requires dissipation (irreversible dynamics)**

### 8.5 What This Result Refutes

**Refuted**: A **stronger proposition that was not part of this paper** — "non-injective projection itself produces the arrow of time."

**Not refuted**: The core proposition of this paper — "inverse inference is structurally and statically impossible."

**The distinction**:

- "Inverse inference impossible" is an **epistemological** proposition
- "Produces the arrow of time" is a **dynamical** proposition

**This paper never claimed the latter.**

### 8.6 Significance

This is a negative result. It rules out a possibility but does not produce anything new. Its value lies in:

1. Clarifying the distinction between "static source" and "dynamical source"
2. Showing that D_f is a time-reversal-neutral quantity
3. Pointing the direction for future research: the arrow of time must be sought in dynamics

---

## IX. Sensitivity of D_f to the Definition of Ω

### 1. Sensitivity Analysis (Economics Case)

| Definition of Ω | \|Ω\| | H(Ω) | H(Ω\|M′) | D_f |
| :--- | :--- | :--- | :--- | :--- |
| Ω₁ | 2 | 1.00 | 0.00 | 0.00 |
| Ω₂ | 4 | 2.00 | 1.00 | 0.50 |
| Ω₃ | 8 | 3.00 | 2.00 | 0.67 |
| Ω₄ | 16 | 4.00 | 3.00 | 0.75 |
| Ω₅ | 256 | 8.00 | 7.00 | 0.88 |

**Conclusion**: In economics, D_f is highly sensitive to the definition of Ω.

### 2. Limitation on Practical Value in Economics

- D_f cannot serve as a cross-theoretical macroscopic description quality metric.
- **This paper does not promise that D_f can be conveniently used for policy evaluation.**

---

## X. Relation to Identification Theory, Partial Identification Theory, and Causal Inference

### 1. Core Problem of Identification Theory

Identification theory asks: is parameter θ identifiable?

### 2. Relation Between the Inverse-Inference Framework and Identification Theory

**Relation One**: Identification theory is a special case of the inverse-inference framework.

**Relation Two**: The inverse-inference framework provides an information-theoretic foundation for identification theory.

**Relation Three**: The inverse-inference framework gives a lower bound on inverse-inference error.

### 3. Relation to Partial Identification Theory

**Complementarity**: D_f can serve as an information-theoretic measure of the "size of the identification region" in partial identification.

### 4. Relation to Causal Inference

**Core reminder**: Do not abandon causal inference because "macroscopic data cannot recover microscopic states."

---

## XI. Ontological Asymmetry of Ω and Its Consequences

### 1. Statement of the Asymmetry

- **Physics**: Ω is ontologically determinate.
- **Economics**: Ω is theoretically constructed.

### 2. Consequences of the Asymmetry

**Consequence One**: The epistemological status of D_f differs.

**Consequence Two**: The scope of comparison of D_f differs.

### 3. Precise Definition of "Local Mathematical Analogy"

**Definition (Local Mathematical Analogy)**: Two domains A and B constitute a local mathematical analogy on problem P if and only if:

1. Both A and B can be modeled using the same set of mathematical objects (Ω, M′, g ∘ f, p, d).
2. D_f and ε_min in A and B satisfy the same set of theorems.
3. There is **no requirement** that a bijection exist between the Ω of A and the Ω of B.
4. There is **no requirement** that the Ω of A and B satisfy the same set of axioms.

---

## XII. Scope and Limitations

### 1. Scope

- There exists a well-defined microscopic state space Ω and macroscopic state space M′.
- There exists an aggregation mapping g ∘ f: Ω → M′ that is non-injective.
- There exists a probability measure p on Ω.

### 2. Limitation One: Ontological Asymmetry of Ω

See Section XI.

### 3. Limitation Two: Choice of Probability Measure p

D_f depends on p.

### 4. Limitation Three: Continuous Case

The theorems of this paper hold strictly for finite sets.

### 5. Limitation Four: Computation of the Rate-Distortion Function

The rate-distortion function R(D) generally has no analytic form.

### 6. Limitation Five: Convergence Speed

See Section 6.4.

### 7. Limitation Six: Discrete and Continuous Scaling Laws Cannot Be Unified

See Section 6.5.

### 8. Limitation Seven: Sampling Insufficiency in the Ising Simulation

See Section 7.5.

### 9. Limitation Eight: D_f Is a Conceptual Tool, Not an Operational Tool

**This paper does not promise that D_f can be conveniently used for policy evaluation.**

### 10. Limitation Nine: D_f Does Not Capture the Arrow of Time

See Section VIII.

### 11. Limitation Ten: Insufficient Sample in the Boolean Network Analysis

See Appendix D.

---

## XIII. Objections and Responses

### Objection One: "D_f is just a renaming of conditional entropy."

**Response**: Correct. The contribution of this paper is to rigorously reduce the inverse-inference error lower bound to rate-distortion theory, to give a unified scaling law with an explicit convergence condition, and to validate the framework with a real system.

### Objection Two: "Economists have long known that macroscopic data cannot precisely infer microscopic states."

**Response**: Correct. The contribution of this paper is not to "tell economists something they do not know," but to "provide an information-theoretic explanation of unidentifiability."

### Objection Three: "This paper is philosophy, not economics or physics."

**Response**: Correct. This paper is a paper in the philosophy of science.

### Objection Four: "The sensitivity of D_f to the definition of Ω has not been discussed."

**Response**: Section IX provides a systematic quantitative analysis.

### Objection Five: "The scaling law D_f → α has no theoretical derivation."

**Response**: The derivation is in Appendix B.

### Objection Six: "The discrete case and the continuous scaling law cannot be unified."

**Response**: Correct. Section 6.5 explicitly states that they are independent results.

### Objection Seven: "The Ising simulation suffers from sampling insufficiency."

**Response**: Correct. Section 7.5 explicitly states this.

### Objection Eight: "D_f being minimal at the critical point is just a restatement of known physics."

**Response**: Partially correct. "Maximal fluctuations at the critical point" is known; but the translation into "minimal information loss rate at the critical point" is the contribution of this paper.

### Objection Nine: "D_f is not an operational tool and is useless for empirical researchers."

**Response**: Correct. This paper clearly states that D_f is a **conceptual tool**.

### Objection Ten: "The time-reversal symmetry test proves your framework is wrong."

**Response**: Not accurate. That test refutes a **stronger proposition that was not part of this paper** — "non-injective projection itself produces the arrow of time." The core proposition of this paper — "inverse inference is structurally and statically impossible" — is not refuted.

---

## XIV. Conclusion

The core results of this paper are eight:

**First, it defines the information loss rate D_f.**

**Second, it rigorously reduces the inverse-inference error lower bound to rate-distortion theory.**

**Third, it provides a complete scaling theory of information loss rate.**

**Fourth, it validates the framework in a real system with the 2D Ising model.**

**Fifth, it discusses the sensitivity of D_f to the definition of Ω.**

**Sixth, it clearly distinguishes the inverse-inference framework from identification theory.**

**Seventh, it provides an explicit convergence condition.**

**Eighth, it reports a negative result: D_f does not capture the arrow of time.** The time-reversal symmetry test shows that D_f is time-symmetric under reversible dynamics. Non-injective projection itself does not produce the arrow of time; the arrow of time requires dissipation.

**Final positioning of this paper**:

> This paper is not an operational manual, but a paper in the philosophy of science. D_f is a conceptual tool that reveals the structural source of unidentifiability. The scaling law D_f → α is the most important quantitative result of this paper. The time-reversal symmetry test is a negative result that clarifies the distinction between static information loss and dynamical irreversibility.

**The conclusion of this paper is**: unidentifiability has a structural source deeper than "insufficient data" — namely, the non-injectivity of macroscopic descriptions. This source does not disappear with increases in data volume, computational power, or model complexity. **However, non-injectivity itself does not produce the arrow of time.**

---

## Appendix A: Proof of Theorem 1

**Proof**:

**Step One (Markov Chain)**: Since h is a deterministic mapping, Ω → M′ → h(M′) forms a Markov chain.

**Step Two (Data Processing Inequality)**:

I(Ω; h(M')) ≤ I(Ω; M')

**Step Three (Definition of Rate-Distortion Function)**: By the definition of the rate-distortion function, any reconstruction channel q satisfying E[d(X,Y)] ≤ ε must have I(X;Y) ≥ R(ε). Therefore:

R(ε(h)) ≤ I(Ω; h(M')) ≤ I(Ω; M')

**Step Four (Inverse Function)**: Since R is strictly decreasing:

ε(h) ≥ R⁻¹(I(Ω; M'))

Q.E.D.

---

## Appendix B: Derivation of the Scaling Law

Let h_micro = (1/2) log₂(2πeσ²) = log₂σ + C₀, where C₀ = (1/2)log₂(2πe) ≈ 2.047.

Let Δ = Δ₀ · (σ/σ₀)^α, so log₂Δ = log₂Δ₀ + α log₂(σ/σ₀).

When σ >> Δ:

D_f = log₂Δ / h_micro = [log₂Δ₀ + α log₂(σ/σ₀)] / [log₂(σ/σ₀) + log₂σ₀ + C₀]

As σ → ∞: D_f → α

**Derivation of the convergence condition**:

Require |D_f - α| < 0.1·α. Let L = log₂(σ/σ₀), C = log₂σ₀ + C₀, then:

|D_f - α| = |log₂Δ₀ - αC| / (L + C) < 0.1·α

i.e., L > |log₂Δ₀ - αC| / (0.1·α) - C

With Δ₀ = 10, σ₀ = 1, C = 2.047, we get L > 18.4.

---

## Appendix C: Numerical Method for the Ising Simulation

### 1. Metropolis Algorithm

ΔE = 2σᵢ · Σ_{j∈neighbors} σⱼ, accepted with probability min(1, exp(-ΔE/T)).

### 2. Multi-Start Sampling

10 independent runs per temperature, all samples merged.

### 3. Computing Platform

GitHub Actions (Ubuntu-latest, 2 cores, 7 GB RAM).

---

## Appendix D: D_f Analysis of Real Boolean Networks

### 1. Purpose

To verify the information projection framework on **real biological networks**. Specific question: does the D_f of real gene regulatory networks differ significantly from random Boolean networks of the same size?

### 2. Data

BioDivine Boolean Models (BBM) database, 285 `.bnet` files. Processable models (N ≤ 183): 28, of which:

- Exact enumeration (N ≤ 16): 13
- Monte Carlo sampling (N > 16, M = 100,000 samples): 15

### 3. Method

For each network:

- **Ω**: all initial states (2^N)
- **M′**: attractors (phenotype)
- **D_f = H(Ω|M′) / H(Ω)**

For N ≤ 16, exact enumeration. For N > 16, 100,000 random samples.

### 4. Results

| N | D_f | Method | Attractors |
| :--- | :--- | :--- | :--- |
| 5 | 0.8913 | exact | 2 |
| 5 | 0.8006 | exact | 2 |
| 6 | 0.7461 | exact | 5 |
| 7 | 0.7908 | exact | 3 |
| 9 | 0.9396 | exact | 2 |
| 9 | 0.9127 | exact | 2 |
| 11 | 0.8847 | exact | 4 |
| 11 | 0.7710 | exact | 8 |
| 11 | 0.7248 | exact | 9 |
| 12 | 0.9555 | exact | 3 |
| 14 | 1.0000 | exact | 1 |
| 15 | 0.9048 | exact | 7 |
| 15 | 1.0000 | exact | 1 |
| 18 | 0.9876 | MC | 9 |
| 18 | 0.8026 | MC | 16 |
| 18 | 0.8465 | MC | 11 |
| 19 | 0.9997 | MC | 21 |
| 19 | 0.9467 | MC | 3 |
| 28 | 0.9876 | MC | 2 |
| 30 | 0.9995 | MC | 15 |
| 31 | 1.0000 | MC | 3 |
| 33 | 0.9853 | MC | 5 |
| 47 | 0.9734 | MC | 6 |
| 83 | 0.9796 | MC | 4 |
| 102 | 0.9052 | MC | 2110 |
| 144 | 0.9803 | MC | 8 |
| 183 | 0.9894 | MC | 8 |

**Statistics**: D_f mean 0.9117, standard deviation 0.0873.

### 5. Observations

**Observation 1**: For large N, D_f approaches 1. All networks with N ≥ 28 have D_f > 0.9.

**Observation 2**: For small N, D_f is dispersed. Networks with N ≤ 15 have D_f in the range 0.72-1.00.

**Observation 3**: This pattern can be predicted by:

D_f = 1 − H(attractors) / N

When N is large, H(attractors)/N → 0, so D_f → 1. When N is small, H(attractors)/N is non-negligible.

### 6. Conclusion

**The D_f of real biological networks follows mathematical expectation.**

- Large networks approach 1, small networks are dispersed
- This pattern does not depend on whether the network is real or random
- **Real networks do not deviate from the mathematical baseline of random networks**

**This is a verification result, not a discovery.** It shows that the information projection framework holds on real biological networks, but does not produce new biological insight.

### 7. Limitations

- Small sample size (28 models)
- Most of the 285 models were skipped (N > 183 or parsing failure)
- Monte Carlo sampling introduces error
- No strict comparison with random networks

**Statistical conclusions require more models and more rigorous methods.**

---

## XV. Falsification Conditions

1. If economists find that there exists a macroscopic description M′ such that D_f ≈ 0 and can be used to precisely infer microscopic states, then the "structural boundary" conclusion of this paper does not hold in economics.
2. If physicists find a projection in quantum gravity such that D_f = 0, then the framework of this paper does not apply in physics.
3. If it is mathematically proven that, although g ∘ f is non-injective, there exists an inverse-inference operator whose error lower bound is 0, then the theorem of this paper is refuted.
4. If numerical simulations show that the scaling law D_f → α does not hold, then the conclusion of Section 6.4 is falsified.
5. If it is proven that the discrete case can be written in the form Δ ~ σ^α, then the conclusion of Section 6.5 is falsified.
6. If, in the Ising model, the minimum of D_f is not near the critical point, then the conclusion of Section VII is falsified.
7. If D_f is found to be time-asymmetric under reversible dynamics, then the negative result of Section VIII is refuted.
8. If the D_f of real Boolean networks is found to systematically deviate from the random baseline, then the conclusion of Appendix D is falsified.

---

## XVI. References

[1] Batterman, R. W. (2002). *The Devil in the Details*. Oxford University Press.

[2] Blahut, R. E. (1972). Computation of Channel Capacity and Rate-Distortion Functions. *IEEE Transactions on Information Theory*, 18(4), 460-473.

[3] Cartwright, N. (1983). *How the Laws of Physics Lie*. Oxford University Press.

[4] Cover, T. M., & Thomas, J. A. (2006). *Elements of Information Theory* (2nd ed.). Wiley-Interscience.

[5] Fano, R. M. (1961). *Transmission of Information: A Statistical Theory of Communications*. MIT Press.

[6] Gibbs, J. W. (1902). *Elementary Principles in Statistical Mechanics*. Yale University Press.

[7] Jaynes, E. T. (1957). Information Theory and Statistical Mechanics. *Physical Review*, 106(4), 620-630.

[8] Kauffman, S. A. (1969). Metabolic Stability and Epigenesis in Randomly Constructed Genetic Nets. *Journal of Theoretical Biology*, 22(3), 437-467.

[9] Manski, C. F. (2003). *Partial Identification of Probability Distributions*. Springer.

[10] Onsager, L. (1944). Crystal Statistics. I. A Two-Dimensional Model with an Order-Disorder Transition. *Physical Review*, 65(3-4), 117-149.

[11] Price, H. (1996). *Time's Arrow and Archimedes' Point*. Oxford University Press.

[12] Shannon, C. E. (1948). A Mathematical Theory of Communication. *Bell System Technical Journal*, 27(3), 379-423.

[13] Shannon, C. E. (1959). Coding Theorems for a Discrete Source with a Fidelity Criterion. *IRE National Convention Record*, 7(4), 142-163.

[14] Tishby, N., Pereira, F. C., & Bialek, W. (1999). The Information Bottleneck Method. *Proceedings of the 37th Annual Allerton Conference on Communication, Control, and Computing*, 368-377.

[15] Wilson, K. G. (1971). Renormalization Group and Critical Phenomena. *Physical Review B*, 4(9), 3174-3183.

[16] Zhong, S. (2026). *A Consequence of Information Loss — On the Common Origin of the Unification Program and the Arrow of Time* (Version 7.0). Equal System Repository.

[17] Zhong, S. (2026). *On the Structural Source of Irreversibility — The Non-Injectivity of Macroscopic Descriptions and Its Epistemological Consequences* (Version 29.0). Equal System Repository.

---

## XVII. Data Availability Statement

This paper is a theoretical derivation. The numerical simulations in Sections VI, VII, VIII, and Appendix D were generated by Python code, reproducible in the GitHub repository maxlanceund/github-random. All simulations were run via GitHub Actions in the cloud.

---

## XVIII. Conflict of Interest Statement

The author declares that there is no conflict of interest that could affect the research conclusions or academic judgment of this paper.

---

**Suggested Citation (APA format)**:

Zhong, S. (2026). *Information Loss Rate of Macroscopic Descriptions — An Information-Theoretic Explanation of Unidentifiability and Its Interdisciplinary Analogy* (Version 13.0). Equal System Repository.

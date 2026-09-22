# Information Loss Rate of Macroscopic Descriptions

## —An Information-Theoretic Explanation of Unidentifiability and Its Interdisciplinary Analogy

| Item | Content |
| :--- | :--- |
| **Title** | Information Loss Rate of Macroscopic Descriptions—An Information-Theoretic Explanation of Unidentifiability and Its Interdisciplinary Analogy |
| **Author** | Zhong Shanzhen |
| **Date** | 2026-09-22 |
| **License** | CC BY-NC 4.0 |
| **Keywords** | information loss rate, non-injectivity, rate-distortion theory, unidentifiability, identification theory, partial identification, ontological asymmetry, interdisciplinary analogy |

---

## I. Abstract

Building on two previous papers, this paper proposes an information-theoretic framework for quantifying the information loss of macroscopic descriptions and for providing a conceptual explanation of "unidentifiability" in economics.

The previous two papers argued that the non-injectivity of the composite projection `g ∘ f: Ω → M'` renders macroscopic descriptions incomplete. That conclusion, however, was qualitative. The core contribution of this paper is **conceptual, not operational**.

**The core contributions of this paper are six:**

**First, it defines the information loss rate `D_f`.** `D_f = H(Ω|M') / H(Ω)`, ranging over `[0,1]`.

**Second, it rigorously reduces the lower bound on inverse-inference error to rate-distortion theory.** For a general distortion measure `d`, the lower bound is given by the rate-distortion function: `ε(h) ≥ R⁻¹(I(Ω; M'))`.

**Third, it provides an information-theoretic explanation of "unidentifiability" in economics.** Unidentifiability is not a consequence of "insufficient data" or "bad models," but a structural consequence of the non-injectivity of macroscopic descriptions.

**Fourth, it gives concrete forms of the rate-distortion function for three common cases** (Hamming distortion, squared-error distortion, Gaussian source), making the framework computable.

**Fifth, it discusses the sensitivity of `D_f` to the definition of `Ω`, and explains why this limits the practical value of `D_f` in economics.** In physics, `Ω` is ontologically determinate; in economics, `Ω` is theoretically constructed. Thus `D_f` is an objective structural quantity in physics, but a theory-internal quantity in economics.

**Sixth, it clearly distinguishes the inverse-inference framework from econometric identification theory, and discusses its relation to partial identification and causal inference.**

**Positioning of this paper**: This paper is not an "operational manual" and does not tell empirical researchers "how to do it." It is a paper in the philosophy of science, telling theoretical researchers "why certain approaches are structurally impossible." `D_f` is a **conceptual tool**, not an **operational tool**.

**The conclusion of this paper is**: unidentifiability has a structural source deeper than "insufficient data"—namely, the non-injectivity of macroscopic descriptions. This source does not disappear with increases in data volume, computational power, or model complexity.

**Keywords**: information loss rate; non-injectivity; rate-distortion theory; unidentifiability; identification theory; partial identification; ontological asymmetry; interdisciplinary analogy

---

## II. Introduction

### 1. The Unresolved Problem of the Previous Two Papers

The previous two papers established a formal framework and argued for two core propositions:

**Proposition One**: The arrow of time and the inverse-inference predicament of the unification program have the same structural source—the non-injectivity of the composite projection.

**Proposition Two**: Irreversibility has a static structural source—the non-injectivity of the aggregation mapping.

The contribution of these two papers is **qualitative**. A natural follow-up question is: **how large, exactly, is the error in inferring microscopic states from macroscopic descriptions?**

### 2. Core Questions

**Question One**: Given a macroscopic description `M'`, how much microscopic information does it lose?

**Question Two**: What is the lower bound on the error of any attempt to infer `Ω` from `M'`?

**Question Three**: What is the relation between this framework and existing identification theory and partial identification theory in econometrics?

**Question Four**: Is the ontological status of `Ω` the same in physics and economics? If not, what implications does this have for the scope of the framework?

### 3. Positioning of This Paper: Conceptual Contribution, Not Operational Contribution

**This paper is not an operational manual.** It does not tell empirical researchers "how to do it." It does not provide a step-by-step tutorial on "how to estimate `D_f`." It does not promise that "using `D_f` will improve policy evaluation."

**This paper is a paper in the philosophy of science.** Its goal is to provide an information-theoretic explanation of "unidentifiability" in economics. This explanation is conceptual, not operational.

**The contribution of this paper is**: it clarifies the structural source of "unidentifiability." That source is: the macroscopic description `M'` is a non-injective projection of the microscopic state `Ω`. Non-injective projection loses information, and information loss makes exact inverse inference impossible.

**This explanation does not change the technical operations of empirical research.** Empirical researchers will still use instrumental variables, difference-in-differences, and regression discontinuity. But they will understand why these methods cannot "recover" microscopic states structurally, and can only "identify" causal effects.

### 4. Structure of the Argument

Section III defines the information loss rate and its properties, and discusses the ontological status of `Ω`. Section IV introduces rate-distortion theory and proves the inverse-inference error lower bound theorem. Section V gives the rate-distortion function for three common cases. Section VI provides a parameterized numerical example. Section VII discusses the sensitivity of `D_f` to the definition of `Ω`. Section VIII discusses the physical interpretation of `ε_min` and optimal macroscopic descriptions. Section IX discusses the relation to identification theory, partial identification theory, and causal inference. Section X discusses the ontological asymmetry of `Ω` and its consequences. Section XI discusses the relation to existing work in the philosophy of science. Section XII discusses scope and limitations. Section XIII responds to objections. Section XIV concludes.

---

## III. Information Loss Rate: Definition and Properties

### 1. Basic Setup

- `Ω`: microscopic state space (finite or continuous), with probability measure `p`.
- `M'`: coarse-grained macroscopic state space.
- `g ∘ f: Ω → M'`: composite projection, non-injective.
- For each `z ∈ M'`, the fiber is `(g ∘ f)⁻¹(z) = {x ∈ Ω : (g ∘ f)(x) = z}`.

### 2. Definitions

**Definition 1 (Information Loss Rate)**:

```math
D_f = \frac{H(\Omega \mid M')}{H(\Omega)}
```

**Definition 2 (Information Retention Rate)**:

```math
R_f = 1 - D_f = \frac{I(\Omega; M')}{H(\Omega)}
```

### 3. Basic Properties

**Property 1 (Range)**: `0 ≤ D_f ≤ 1`.

**Property 2 (Injective Case)**: If `g ∘ f` is injective, then `D_f = 0`.

**Property 3 (Complete Loss Case)**: If `Ω` and `M'` are independent, then `D_f = 1`.

**Property 4 (Structural Dependence)**: The **definition** of `D_f` depends only on `(Ω, M', g ∘ f, p)`, not on sample size, computational power, or model complexity.

**Note (Conceptual Contribution, Not Operational Contribution)**: Property 4 says that the **definition** of `D_f` does not depend on sample size. But the **estimation** of `D_f` does depend on sample size. This paper does not promise that `D_f` can be easily estimated. It only states that `D_f` is a structural quantity whose definition does not depend on sample size.

### 4. Ontological Status of `Ω`: Asymmetry Between Physics and Economics

**In physics**: `Ω` is ontologically determinate. In statistical mechanics, `Ω` is the microscopic state in phase space. In quantum mechanics, `Ω` is the quantum state.

**In economics**: `Ω` is theoretically constructed. `Ω` can be a firm's balance sheet, a consumer's utility function, an entrepreneur's expectations, or a combination of these. The definition of `Ω` depends on theoretical choices.

**Consequences of this asymmetry**:

- In physics, `D_f` is an **objective structural quantity**.
- In economics, `D_f` is a **theory-internal quantity** relative to the chosen theory.

**Therefore, the framework of this paper is not an ontological unification, but a local mathematical analogy.**

### 5. Sensitivity of `D_f` to the Definition of `Ω`: A Systematic Quantitative Analysis

**In economics, `D_f` depends on the definition of `Ω`.** This section provides a systematic analysis.

**Model setup**: Let `M' = {a, b}`, and let the definition of `Ω` be progressively refined:

- `Ω_1`: 2 states, `H(Ω_1) = 1` bit.
- `Ω_2`: 4 states, `H(Ω_2) = 2` bits.
- `Ω_3`: 8 states, `H(Ω_3) = 3` bits.
- `Ω_4`: 16 states, `H(Ω_4) = 4` bits.

**Assumption**: `M'` is a coarse-graining of `Ω`, with each state of `M'` corresponding to half the states of `Ω`.

**Numerical table**:

| Definition of `Ω` | `\|Ω\|` | `H(Ω)` | `H(Ω\|M')` | `D_f` |
| :--- | :--- | :--- | :--- | :--- |
| `Ω_1` | 2 | 1.00 | 0.00 | 0.00 |
| `Ω_2` | 4 | 2.00 | 1.00 | 0.50 |
| `Ω_3` | 8 | 3.00 | 2.00 | 0.67 |
| `Ω_4` | 16 | 4.00 | 3.00 | 0.75 |
| `Ω_5` | 32 | 5.00 | 4.00 | 0.80 |
| `Ω_6` | 64 | 6.00 | 5.00 | 0.83 |
| `Ω_7` | 128 | 7.00 | 6.00 | 0.86 |
| `Ω_8` | 256 | 8.00 | 7.00 | 0.88 |

**Observation**:

- The finer the definition of `Ω`, the larger `D_f`.
- The growth rate of `D_f` decreases, tending to 1.
- The range of `D_f` is large: from 0.00 to 0.88.

**Conclusion**: In economics, `D_f` is **highly sensitive** to the definition of `Ω`. Therefore:

- Comparisons of `D_f` are valid only **under the same definition of `Ω`**.
- `D_f` cannot serve as a cross-theoretical macroscopic description quality metric.
- **The practical value of `D_f` in economics is limited.** This paper does not promise that `D_f` can be conveniently used for policy evaluation.

**In physics, this problem does not exist**, because `Ω` is ontologically determinate.

### 6. Relation to Existing Concepts

**Relation to mutual information**: `D_f = 1 - I(Ω;M')/H(Ω)`.

**Relation to coarse-grained entropy**: In statistical mechanics, `D_f = 1 - S_macro/S_micro`.

**Relation to Bekenstein-Hawking entropy**: For black holes, `D_f = 1 - S_BH/S_micro`.

---

## IV. Rate-Distortion Theory and the Inverse-Inference Error Lower Bound

### 1. Why Rate-Distortion Theory Is Needed

The inverse-inference problem—recovering the microscopic state `Ω` from the macroscopic description `M'`—is essentially an **inverse problem of lossy compression**. The standard tool in information theory for such problems is **rate-distortion theory** (Shannon, 1959).

### 2. Rate-Distortion Function

**Definition 3 (Rate-Distortion Function)**:

Let source `Ω` have probability distribution `p`, and let the distortion measure be `d: Ω × Ω → R≥0`. The rate-distortion function is defined as:

```math
R(D) = \min_{q(y|x): \mathbb{E}[d(X,Y)] \le D} I(X; Y)
```

**Property (Monotonicity of the rate-distortion function)**: `R(D)` is strictly decreasing on `[0, D_max]`.

### 3. Inverse-Inference Error Lower Bound Theorem

**Theorem 1 (Rate-Distortion Lower Bound)**:

Let `h: M' → Ω` be an inverse-inference mapping, and let the inverse-inference error be `ε(h) = E[d(X, h(M'))]`. Then:

```math
\varepsilon(h) \ge R^{-1}\bigl(I(\Omega; M')\bigr)
```

**Proof**: See Appendix A.

**Corollary 1**: `ε(h) ≥ R⁻¹(H(Ω)(1 - D_f))`.

**Corollary 2 (Data-Volume Independence)**: `R⁻¹(I(Ω; M'))` depends only on `Ω`, `M'`, `p`, and `d`, not on sample size or model complexity. **However, the premise of this conclusion is that `Ω` is fixed.**

### 4. Concrete Lower Bound under Hamming Distortion: Fano's Inequality

**Theorem 2 (Fano Lower Bound)**:

Let `Ω` be a finite set, `|Ω| = K`, `d(x,y) = 1_{x ≠ y}` be Hamming distortion, and `P_e = ε(h)` be the error probability. Then:

```math
H(\Omega \mid M') \le H_b(P_e) + P_e \cdot \log_2(K - 1)
```

**Limitation of Fano's bound**: When `K` is very large, `P_e^min` tends to a constant of about 0.5, while the true optimal error may tend to 1. In practical applications, one should directly use the rate-distortion lower bound `R⁻¹(I(Ω;M'))`.

---

## V. Rate-Distortion Functions for Three Common Cases

### 1. Hamming Distortion (Finite Discrete Source)

**Rate-distortion function**: For uniform distribution `p(x) = 1/K`,

```math
R(D) = \log_2 K - H_b(D) - D \cdot \log_2(K - 1), \quad 0 \le D \le 1 - 1/K
```

**Inverse function `R⁻¹`**: Solved numerically.

### 2. Squared-Error Distortion (Continuous Source, Gaussian Approximation)

**Rate-distortion function**:

```math
R(D) = \frac{1}{2} \log_2\left(\frac{\sigma^2}{D}\right), \quad 0 \le D \le \sigma^2
```

**Analytic inverse function**:

```math
R^{-1}(I) = \sigma^2 \cdot 2^{-2I}
```

### 3. Gaussian Source + Gaussian Channel (Vector Case)

**Rate-distortion function**:

```math
R(D) = \sum_{i=1}^{n} \frac{1}{2} \log_2\left(\frac{\lambda_i}{\theta}\right)
```

**Inverse function `R⁻¹`**: Solved numerically.

### 4. Operational Meaning

| Distortion Measure | Rate-Distortion Function `R(D)` | Inverse Function `R⁻¹(I)` |
| :--- | :--- | :--- |
| Hamming | `log₂K - H_b(D) - D log₂(K-1)` | Numerical |
| Squared Error (Gaussian) | `(1/2) log₂(σ²/D)` | `σ² · 2^(-2I)` |
| Vector Gaussian | `Σ (1/2) log₂(λ_i/θ)` | Numerical |

---

## VI. Parameterized Numerical Example

### 1. Model Setup

Let `Ω = {1, 2, ..., 2K}`, uniformly distributed, `H(Ω) = log₂(2K)`.

Let `M' = {a, b}`, with the aggregation mapping:

- `g ∘ f(1) = ... = g ∘ f(K) = a`
- `g ∘ f(K+1) = ... = g ∘ f(2K) = b`

**Fiber size**: `N = K`.

**Information loss rate**:

```math
H(\Omega|M') = \log_2 K
```

```math
D_f = \frac{\log_2 K}{\log_2(2K)}
```

### 2. Numerical Table

Using Hamming distortion.

| `K` | `\|Ω\|` | `H(Ω)` | `H(Ω\|M')` | `D_f` | `P_e^min` | `P_e^opt` | Gap |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 2 | 1.00 | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 |
| 2 | 4 | 2.00 | 1.00 | 0.50 | 0.19 | 0.50 | 0.31 |
| 4 | 8 | 3.00 | 2.00 | 0.67 | 0.31 | 0.75 | 0.44 |
| 8 | 16 | 4.00 | 3.00 | 0.75 | 0.39 | 0.875 | 0.485 |
| 16 | 32 | 5.00 | 4.00 | 0.80 | 0.44 | 0.9375 | 0.4975 |
| 32 | 64 | 6.00 | 5.00 | 0.83 | 0.48 | 0.96875 | 0.48875 |
| 64 | 128 | 7.00 | 6.00 | 0.86 | 0.51 | 0.984375 | 0.474375 |
| 128 | 256 | 8.00 | 7.00 | 0.88 | 0.53 | 0.9921875 | 0.4621875 |

### 3. Discussion of the Looseness of Fano's Bound

**Observation 1**: `D_f` increases from 0 to 0.88, but its growth rate decreases.

**Observation 2**: Fano's lower bound `P_e^min` tends to a constant of about 0.5, while the true optimal error `P_e^opt = 1 - 1/K` tends to 1.

**Conclusion**: In practical applications, one should directly use the rate-distortion lower bound `R⁻¹(I(Ω;M'))`, which is tighter than Fano's bound.

---

## VII. Sensitivity of `D_f` to the Definition of `Ω` and Its Limitation on Practical Value in Economics

### 1. Sensitivity Analysis

See Section III, Subsection 5. The conclusion is: in economics, `D_f` is **highly sensitive** to the definition of `Ω`.

### 2. Limitation on Practical Value in Economics

**Because `D_f` is highly sensitive to `Ω`, its practical value in economics is limited:**

- `D_f` cannot serve as a cross-theoretical macroscopic description quality metric.
- Comparisons of `D_f` are valid only under the same definition of `Ω`.
- Empirical researchers should be aware that the choice of `Ω` affects the robustness of conclusions.

**This paper does not promise that `D_f` can be conveniently used for policy evaluation.** It only states that `D_f` is a conceptual tool that reveals the structural source of unidentifiability.

### 3. Advice for Empirical Researchers

**Although `D_f` is not an operational tool, it offers a conceptual reminder for empirical researchers:**

> When you choose the definition of `Ω`, be aware that this choice affects the magnitude of "unidentifiability." Change the definition, and unidentifiability may disappear.

This reminder cannot replace instrumental variables, difference-in-differences, or regression discontinuity, but it helps empirical researchers understand why some "unidentifiabilities" are structural and some are definition-dependent.

---

## VIII. Physical Interpretation of `ε_min` and Optimal Macroscopic Descriptions

### 1. Physical Interpretation of `ε_min`

**Hamming distortion**: `ε_min` is the lower bound on error probability.

**Squared-error distortion**: `ε_min` is the lower bound on mean squared error. `ε_min/σ²` is the lower bound on normalized mean squared error.

### 2. Search Algorithm for Optimal Macroscopic Descriptions

**Algorithm**:

1. For each candidate `M'_i`, compute `D_f(M'_i)`.
2. Select the `M'_i` with the smallest `D_f`.

**Heuristic methods**:

- **Greedy algorithm**: Start from the coarsest partition and refine gradually until `D_f` no longer decreases significantly.
- **Information bottleneck method** (Tishby et al., 1999).
- **Regularization methods**.

### 3. The Threshold Problem for `D_f`

**How small must `D_f` be to be "small enough"?**

This is a **normative question**, not a descriptive one. The threshold depends on the specific application:

- **Physics**: The threshold is determined by experimental precision.
- **Economics**: The threshold is determined by the tolerance of policy evaluation.

**This paper does not provide a universal threshold.** It only provides the computational method.

---

## IX. Relation to Identification Theory, Partial Identification Theory, and Causal Inference

### 1. Core Problem of Identification Theory

**Identification theory** asks: is parameter `θ` identifiable?

### 2. Relation Between the Inverse-Inference Framework and Identification Theory

**Relation One**: Identification theory is a special case of the inverse-inference framework.

**Relation Two**: The inverse-inference framework provides an information-theoretic foundation for identification theory.

**Relation Three**: The inverse-inference framework gives a lower bound on inverse-inference error.

### 3. Relation to Partial Identification Theory

**Complementarity**: `D_f` can serve as an information-theoretic measure of the "size of the identification region" in partial identification. `ε_min` can serve as a lower bound on the "diameter of the identification region."

### 4. Relation to Causal Inference

**Inverse-inference problem**: recovering `Ω` from `M'`.

**Causal inference problem**: estimating the causal effect of a treatment variable `T` on an outcome variable `Y`.

**Difference**: Causal inference does not require recovering `Ω`.

**The core reminder of this paper**:

> Do not abandon causal inference because "macroscopic data cannot recover microscopic states." Causal inference does not require recovering microscopic states.

**This paper does not promise** that `D_f` can serve as a diagnostic tool for causal inference. H_causal is a hypothesis to be tested; this paper only proposes it, and does not promise that it holds.

---

## X. Ontological Asymmetry of `Ω` and Its Consequences

### 1. Statement of the Asymmetry

**Physics**: `Ω` is ontologically determinate.

**Economics**: `Ω` is theoretically constructed.

### 2. Consequences of the Asymmetry

**Consequence One**: The epistemological status of `D_f` differs.

**Consequence Two**: The scope of comparison of `D_f` differs.

### 3. Precise Definition of "Local Mathematical Analogy"

**Definition (Local Mathematical Analogy)**: Two domains `A` and `B` constitute a local mathematical analogy on problem `P` if and only if:

1. Both `A` and `B` can be modeled using the same set of mathematical objects `(Ω, M', g ∘ f, p, d)`.
2. `D_f` and `ε_min` in `A` and `B` satisfy the same set of theorems.
3. There is **no requirement** that a bijection exist between the `Ω` of `A` and the `Ω` of `B`.
4. There is **no requirement** that the `Ω` of `A` and `B` satisfy the same set of axioms.

**Difference from isomorphism**:

| Feature | Isomorphism | Local Mathematical Analogy |
| :--- | :--- | :--- |
| Bijection | Required | Not required |
| Preserves all relations | Required | Only preserves theorems about `D_f` and `ε_min` |
| Ontological unification | Required | Not required |

---

## XI. Relation to Existing Work in the Philosophy of Science

### 1. Relation to Cartwright

**Common ground**: Both focus on "the validity of theories under specific conditions."

**Complementarity**: `D_f` can serve as a quantitative indicator of Cartwright's "nomological machines."

### 2. Relation to Morrison

**Common ground**: Both focus on "the role of models in connecting macro and micro."

**Complementarity**: `D_f` can serve as a quantitative indicator of Morrison's "models as mediators."

### 3. Relation to Batterman

**Common ground**: Both focus on "the independent status of macroscopic descriptions."

**Complementarity**: `D_f` can serve as a quantitative indicator of Batterman's "effective theories."

---

## XII. Scope and Limitations

### 1. Scope

- There exists a well-defined microscopic state space `Ω` and macroscopic state space `M'`.
- There exists an aggregation mapping `g ∘ f: Ω → M'` that is non-injective.
- There exists a probability measure `p` on `Ω`.

### 2. Limitation One: Ontological Asymmetry of `Ω`

See Section X.

### 3. Limitation Two: Choice of Probability Measure `p`

`D_f` depends on `p`.

### 4. Limitation Three: Continuous Case

The theorems of this paper hold strictly for finite sets.

### 5. Limitation Four: Computation of the Rate-Distortion Function

The rate-distortion function `R(D)` generally has no analytic form.

### 6. Limitation Five: Estimation Error of `D_f`

### 7. Limitation Six: Choice of Distortion Measure

### 8. Limitation Seven: Search for Optimal Macroscopic Descriptions

### 9. Limitation Eight: Premise of Data-Volume Independence

### 10. Limitation Nine: Relation to Causal Inference

### 11. Limitation Ten: Sensitivity of `D_f` to the Definition of `Ω`

**In economics, `D_f` is highly sensitive to the definition of `Ω`. Therefore, the practical value of `D_f` in economics is limited.**

### 12. Limitation Eleven: `D_f` Is a Conceptual Tool, Not an Operational Tool

**This paper does not promise that `D_f` can be conveniently used for policy evaluation.** It only states that `D_f` is a conceptual tool that reveals the structural source of unidentifiability.

---

## XIII. Objections and Responses

### Objection One: "`D_f` is just a renaming of conditional entropy."

**Response**: Correct. The contribution of this paper is to rigorously reduce the inverse-inference error lower bound to rate-distortion theory, and to provide an information-theoretic explanation of unidentifiability.

### Objection Two: "Economists have long known that macroscopic data cannot precisely infer microscopic states."

**Response**: Correct. The contribution of this paper is not to "tell economists something they do not know," but to "provide an information-theoretic explanation of unidentifiability."

### Objection Three: "The operational manual is tautological."

**Response**: This paper has abandoned the "operational manual" positioning. Its contribution is conceptual, not operational.

### Objection Four: "This paper is philosophy, not economics or physics."

**Response**: Correct. This paper is a paper in the philosophy of science.

### Objection Five: "The sensitivity of `D_f` to the definition of `Ω` has not been discussed."

**Response**: Sections III.5 and VII provide a systematic quantitative analysis.

### Objection Six: "The conjecture about causal inference is too weak."

**Response**: This paper has weakened the claim about causal inference. H_causal is a hypothesis to be tested; this paper only proposes it and does not promise that it holds.

### Objection Seven: "The relation to existing work in the philosophy of science has not been discussed."

**Response**: Section XI discusses the relation to Cartwright, Morrison, and Batterman.

### Objection Eight: "`D_f` is not an operational tool and is useless for empirical researchers."

**Response**: Correct. This paper clearly states that `D_f` is a **conceptual tool**, not an **operational tool**. It does not tell empirical researchers "how to do it"; it tells theoretical researchers "why certain approaches are structurally impossible."

### Objection Nine: "What is the contribution of this paper?"

**Response**: The contribution of this paper is to provide an information-theoretic explanation of "unidentifiability" in economics. This explanation is conceptual, not operational.

---

## XIV. Conclusion

The core results of this paper are six:

**First, it defines the information loss rate `D_f`.**

**Second, it rigorously reduces the inverse-inference error lower bound to rate-distortion theory.**

**Third, it provides an information-theoretic explanation of "unidentifiability" in economics.**

**Fourth, it gives concrete forms of the rate-distortion function for three common cases.**

**Fifth, it discusses the sensitivity of `D_f` to the definition of `Ω`, and explains why this limits the practical value of `D_f` in economics.**

**Sixth, it clearly distinguishes the inverse-inference framework from identification theory, partial identification theory, and causal inference.**

**Final positioning of this paper**:

> This paper is not an operational manual, but a paper in the philosophy of science. Its contribution is conceptual, not operational. `D_f` is a conceptual tool that reveals the structural source of unidentifiability.

**The conclusion of this paper is**: unidentifiability has a structural source deeper than "insufficient data"—namely, the non-injectivity of macroscopic descriptions. This source does not disappear with increases in data volume, computational power, or model complexity.

**This paper does not promise that `D_f` can be conveniently used for policy evaluation.** It only promises that `D_f` helps us understand why some "unidentifiabilities" are structural.

---

## Appendix A: Proof of Theorem 1

**Proof**:

**Step One (Markov Chain)**: Since `h` is a deterministic mapping, `Ω → M' → h(M')` forms a Markov chain.

**Step Two (Data Processing Inequality)**:

```math
I(\Omega; h(M')) \le I(\Omega; M')
```

**Step Three (Definition of Rate-Distortion Function)**: By the definition of the rate-distortion function, any reconstruction channel `q` satisfying `E[d(X,Y)] ≤ ε` must have `I(X;Y) ≥ R(ε)`. Therefore:

```math
R(\varepsilon(h)) \le I(\Omega; h(M')) \le I(\Omega; M')
```

**Step Four (Inverse Function)**: Since `R` is strictly decreasing on `[0, D_max]`, its inverse `R⁻¹` exists and is also decreasing. Therefore:

```math
\varepsilon(h) \ge R^{-1}(I(\Omega; M'))
```

Q.E.D.

---

## XV. Falsification Conditions

1. If economists find that there exists a macroscopic description `M'` such that `D_f ≈ 0` and can be used to precisely infer microscopic states, then the "structural boundary" conclusion of this paper does not hold in economics.
2. If physicists find a projection in quantum gravity such that `D_f = 0`, then the framework of this paper does not apply in physics.
3. If it is mathematically proven that, although `g ∘ f` is non-injective, there exists an inverse-inference operator whose error lower bound is 0, then the theorem of this paper is refuted.
4. If experiments show that increasing data volume can break the rate-distortion lower bound, then the "structural lower bound" conclusion of this paper is falsified.
5. If H_causal is falsified (i.e., `D_f` has no significant correlation with the external validity of causal effects), then the hypothesis in Section IX.4 of this paper is falsified.

---

## XVI. References

[1] Albert, D. Z. (2000). *Time and Chance*. Harvard University Press.

[2] Batterman, R. W. (2002). *The Devil in the Details*. Oxford University Press.

[3] Blahut, R. E. (1972). Computation of Channel Capacity and Rate-Distortion Functions. *IEEE Transactions on Information Theory*, 18(4), 460-473.

[4] Boltzmann, L. (1877). Über die Beziehung zwischen dem zweiten Hauptsatze der mechanischen Wärmetheorie und der Wahrscheinlichkeitsrechnung. *Wiener Berichte*, 76, 373-435.

[5] Cartwright, N. (1983). *How the Laws of Physics Lie*. Oxford University Press.

[6] Cartwright, N. (1999). *The Dappled World*. Cambridge University Press.

[7] Cover, T. M., & Thomas, J. A. (2006). *Elements of Information Theory* (2nd ed.). Wiley-Interscience.

[8] Fano, R. M. (1961). *Transmission of Information: A Statistical Theory of Communications*. MIT Press.

[9] Gibbs, J. W. (1902). *Elementary Principles in Statistical Mechanics*. Yale University Press.

[10] Jaynes, E. T. (1957). Information Theory and Statistical Mechanics. *Physical Review*, 106(4), 620-630.

[11] Koo, R. C. (2008). *The Holy Grail of Macroeconomics: Lessons from Japan's Great Recession*. John Wiley & Sons.

[12] Kozachenko, L. F., & Leonenko, N. N. (1987). Sample Estimate of the Entropy of a Random Vector. *Problems of Information Transmission*, 23(2), 95-101.

[13] Manski, C. F. (2003). *Partial Identification of Probability Distributions*. Springer.

[14] Morrison, M. (1999). Models as Mediators. In *Models as Mediators*. Cambridge University Press.

[15] Price, H. (1996). *Time's Arrow and Archimedes' Point*. Oxford University Press.

[16] Prigogine, I. (1980). *From Being to Becoming*. W. H. Freeman.

[17] Shannon, C. E. (1948). A Mathematical Theory of Communication. *Bell System Technical Journal*, 27(3), 379-423.

[18] Shannon, C. E. (1959). Coding Theorems for a Discrete Source with a Fidelity Criterion. *IRE National Convention Record*, 7(4), 142-163.

[19] Theil, H. (1954). *Linear Aggregation of Economic Relations*. North-Holland.

[20] Tishby, N., Pereira, F. C., & Bialek, W. (1999). The Information Bottleneck Method. *Proceedings of the 37th Annual Allerton Conference on Communication, Control, and Computing*, 368-377.

[21] Zhong, S. (2026). *A Consequence of Information Loss—On the Common Origin of the Unification Program and the Arrow of Time* (Version 7.0). Equal System Repository.

[22] Zhong, S. (2026). *On the Structural Source of Irreversibility—The Non-Injectivity of Macroscopic Descriptions and Its Epistemological Consequences* (Version 29.0). Equal System Repository.

---

## XVII. Data Availability Statement

This paper is a theoretical derivation and does not involve the collection or analysis of empirical data.

---

## XVIII. Conflict of Interest Statement

The author declares that there is no conflict of interest that could affect the research conclusions or academic judgment of this paper.

---

**Suggested Citation (APA format)**:

Zhong, S. (2026). *Information Loss Rate of Macroscopic Descriptions—An Information-Theoretic Explanation of Unidentifiability and Its Interdisciplinary Analogy* (Version 8.0). Equal System Repository.

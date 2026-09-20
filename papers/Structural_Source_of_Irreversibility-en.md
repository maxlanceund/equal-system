# On the Structural Source of Irreversibility

## — The Non-Injectivity of Macro-Descriptions and Its Epistemological Consequences

| Item | Content |
| :--- | :--- |
| **Title** | On the Structural Source of Irreversibility — The Non-Injectivity of Macro-Descriptions and Its Epistemological Consequences |
| **Author** | Zhong Shanzhen |
| **Date** | 2026-09-20 |
| **License** | CC BY-NC 4.0 |
| **Keywords** | aggregation mapping, non-injectivity, irreversibility, coarse-graining, naturalism |

---

## I. Abstract

This paper proposes a formal framework for the relationship between macro-descriptions and micro-states, and applies it to the problem of irreversibility. The core of the framework is the non-injectivity of the aggregation mapping: when the aggregation mapping is not injective, the macro-state does not contain the information required to recover the micro-state, and therefore recovery of the micro-state from the macro-description is in principle impossible.

The central thesis of this paper is: the impossibility of "recovering the micro from the macro" is a purely structural fact — it does not depend on dynamical evolution, does not depend on initial conditions, and does not depend on the randomness of micro-states. This provides a **static structural source** for irreversibility, complementary to the dynamical sources traced by Prigogine, Price, and Albert.

This paper adopts a **naturalist** stance: the aggregation mapping is not an arbitrary descriptive convention, but is constrained by the observable structure of the natural world. Under this stance, "the impossibility of reverse inference" is a structural assertion about the physical world, not merely a convention about a descriptive framework.

On this basis, this paper argues: if the core operation of the physics unification program is, in practice, operated as reverse inference from two macro-theories to an unknown micro-theory, then the program faces a structural obstacle.

**Keywords**: aggregation mapping; non-injectivity; irreversibility; coarse-graining; naturalism

---

## II. Introduction

### 1. Statement of the Problem

The mathematical unification of general relativity and quantum mechanics has been one of the most persistent difficulties in physics since the 20th century. Programs such as string theory and loop quantum gravity attempt to construct a single formal system that reduces to both theories at all scales. To date, none of these programs has been completed.

The question of this paper is not "how to construct a unified theory," but two more fundamental questions:

**First**: What is the **epistemological nature** of the "failure to unify"?

**Second**: What is the relationship between the impossibility of recovering the micro-description from the macro-description and the broader problem of **irreversibility** in physics?

The thesis of this paper is: in the context of statistical-mechanical coarse-graining, the impossibility of "recovering the micro from the macro" provides a **static structural source** for irreversibility, complementary to existing dynamical sources.

### 2. Distinction of Three Levels

**Assertion A (Irreducibility)**: Macro-theories cannot be derived from micro-theories. This is an **ontological** assertion.

**Assertion B (Inexplicability)**: Macro-phenomena cannot be explained by micro-mechanisms. This is a **methodological** assertion.

**Assertion C (Impossibility of Reverse Inference)**: The micro-description cannot be recovered from the macro-description. This is an **epistemological** assertion.

**The core assertion of this paper is C**. This paper does not assert A or B.

### 3. The Naturalist Stance

This paper adopts a **naturalist** stance: the aggregation mapping `f: Omega -> M` is not an arbitrary descriptive convention, but is constrained by the observable structure of the natural world.

Specifically:

- `Omega` (the micro-state space) is described by physical theory, not arbitrarily chosen.
- `M` (the macro-state space) is defined by the set of observables — temperature, pressure, volume, mass, angular momentum, charge, etc.
- `f` is determined by coarse-graining operations — in statistical mechanics, it is a partition of phase space; in quantum mechanics, it is decoherence.

**Why adopt the naturalist stance?** Because the goal of this paper is not to discuss the logical properties of "descriptive frameworks," but to discuss structural features of the physical world. If the aggregation mapping were merely a descriptive convention, then "the impossibility of reverse inference" would be an assertion about language, not about the world. The goal of this paper is the latter.

**The cost of the naturalist stance**: This paper does not discuss the question "what if a different descriptive framework were chosen." If theorists can choose a different `f`, then the conclusions of this paper apply only to "aggregation mappings under given observable constraints." This limitation is discussed in Section IV, "Limitation Two."

### 4. Relation to Existing Literature

**Literature on Irreversibility**: Regarding the origin of irreversibility, there are three main paths in the philosophy of physics.

**Path One (Prigogine, 1980)**: Traces irreversibility to dissipative processes in dynamical evolution.

**Path Two (Price, 1996)**: Asks after the origin of the arrow of time, arguing that it cannot be presupposed.

**Path Three (Albert, 2000)**: Traces irreversibility to the special properties of initial conditions (the "Past Hypothesis").

**The fourth source proposed by this paper: the static structural source**. Irreversibility originates in the non-injectivity of the aggregation mapping. This source differs from the above three in that it does not depend on dynamical evolution, does not depend on the arrow of time, and does not depend on initial conditions.

**Relation to Albert**: Albert's "Past Hypothesis" explains why the **macro-evolution of the physical world** is irreversible. The conclusion of this paper explains why **recovering the micro-state from the macro-description** is impossible. The two are complementary: Albert explains **dynamical irreversibility**, this paper explains **structural irreversibility**. A complete theory of irreversibility requires explaining both levels.

**Literature on Emergence and Coarse-Graining**: Butterfield (2011), Frigg (2007), Wallace (2012), Batterman (2002), and Wilson (2017) discuss philosophical problems of macro-micro relations, emergence, and coarse-graining. The contribution of this paper is to integrate these dispersed discussions into a unified formal framework and to characterize the impossibility of reverse inference using the purely structural concept of non-injectivity.

### 5. Structure of the Argument

Section III establishes the formal framework. Section IV presents the core structural observation. Section V argues for Premise C. Section VI discusses the structural source of irreversibility. Section VII responds to objections. Section VIII concludes.

---

## III. Formal Framework

### 1. Basic Setup

Let the micro-state space be a finite set `Omega`, and the macro-state space be a measurable space `(M, Sigma_M)`.

**Definition 1 (Aggregation Mapping)**: An aggregation mapping `f: Omega -> M` is a measurable mapping.

**Remark**: The "aggregation mapping" of this paper is an abstract formal concept. It does not presuppose any specific coarse-graining mechanism, and can be realized as various concrete coarse-graining operations: phase-space coarse-graining in statistical mechanics, decoherence in quantum mechanics, scale separation in multi-scale modeling.

### 2. Fibers and Structural Loss

**Definition 2 (Fiber)**: For each `y in M`, the fiber of `y` under `f` is

$$
f^{-1}(y) = \{x \in \Omega : f(x) = y\}
$$

**Definition 3 (Structural Loss)**:

$$
L_f = \log_2 |\Omega| - \log_2 |\mathrm{Im}(f)|
$$

**Remark**: Structural loss is an auxiliary intuitive tool, not the foundation of the core argument. The core argument of this paper depends on Observation 1.

### 3. Relation of Structural Loss to Existing Concepts in Information Theory

**Relation to Conditional Entropy**: Given a random variable `X` on `(Omega, Sigma_Omega, p)`, let `Y = f(X)`. The following inequality always holds:

$$
H(X|Y) \leq \mathbb{E}[\log |[X]_f|]
$$

When all fibers have equal size and `X` is uniformly distributed on each fiber, `E[log |[X]_f|] = L_f`.

**Relation to Coarse-Grained Entropy**: Coarse-grained entropy depends on the probability distribution, whereas structural loss does not. Therefore, structural loss is a structural quantity independent of the probability measure.

---

## IV. Core Structural Observation

**Observation 1 (Non-Invertibility of Non-Injective Mappings)**: If `f` is not injective, then there exists no mapping `g: M -> Omega` such that `g o f = id_Omega`.

**Proof**: Suppose such a `g` exists. Since `f` is not injective, take `x1 != x2` such that `f(x1) = f(x2)`. Then

$$
x_1 = g(f(x_1)) = g(f(x_2)) = x_2
$$

contradiction. QED.

**Remark**: In the finite case, `L_f > 0` if and only if `f` is not injective.

**The Philosophical Significance of Observation 1**: Observation 1 is trivial in set theory. But its philosophical significance lies in the fact that it shows: the impossibility of "recovering the micro from the macro" is a **purely structural fact** — it does not depend on dynamical evolution, does not depend on initial conditions, and does not depend on the randomness of micro-states.

**Two Limitations of Observation 1**:

**Limitation One (Exact Recovery)**: Observation 1 applies only to "exact recovery." If relaxed to "approximate recovery" or "probabilistic recovery," Observation 1 does not apply. This paper deals only with the case of exact recovery.

**Limitation Two (Improvement of the Aggregation Mapping)**: This paper presupposes a given aggregation mapping `f`. Physicists can choose different macro-variables, thereby defining different aggregation mappings. But this improvability is constrained in practice by the naturalist stance: the definition of the macro-state space is constrained by the number of observables.

---

## V. Argument for Premise C and Its Scope of Application

### 1. Argument for Premise C

**Premise C**: In the context of statistical-mechanical coarse-graining, the core operation of the physics unification program is, in practice, operated as the construction of a reverse inference mapping.

**Argument**:

The unification program of physics aims to find a theory `T*` such that `T*` reduces to `T1` (general relativity) and `T2` (quantum mechanics) in the appropriate limits. The candidate theories available to physicists are only `T1` and `T2`. In the framework of statistical-mechanical coarse-graining, `T1` and `T2` are understood as projections of `T*` at different scales. The mathematical structure of this projection relation is an aggregation mapping. Therefore, the inferential process from `{T1, T2}` to `T*` corresponds to the process of recovering the pre-image from two projections — this is a reverse inference process.

By Observation 1, if `f1` or `f2` is not injective, then the reverse inference direction `T1 -> T*` does not exist.

**Note**: Premise C is a descriptive empirical generalization, not a logically necessary assertion. This paper does not assert that physicists can only do this; it asserts only that in current practice, it faces the structural obstacle described in this paper.

### 2. Scope of Application

The conclusions of this paper apply to the unification programs in **current physics practice**, including string theory and loop quantum gravity. If future physicists invent an entirely new method that does not depend on reverse inference from known theories to unknown theories, then the conclusions of this paper do not apply.

---

## VI. The Structural Source of Irreversibility

### 1. The Transition from Formal Framework to Ontological Interpretation

The argument of Sections III-V is formal: if `f` is not injective, then no right inverse exists. This argument itself concerns **formal objects**.

The goal of Section VI is to apply this formal conclusion to the **physical world**. This transition requires a premise: the aggregation mapping `f` corresponds to a physical coarse-graining operation, not an arbitrary descriptive convention.

This premise is precisely the **naturalist stance** adopted by this paper. Under this stance, the aggregation mapping is not arbitrarily chosen by the theorist, but is constrained by the observable structure of the natural world. Therefore, "the impossibility of reverse inference" is a structural assertion about the physical world, not merely a convention about a descriptive framework.

### 2. Three Existing Sources of Irreversibility

**Dynamical Source (Prigogine)**: Irreversibility originates in dissipative processes in dynamical evolution. Open systems far from equilibrium generate irreversible behavior through dissipative structures.

**Arrow-of-Time Source (Price)**: Irreversibility originates in the existence of the arrow of time. Price asks after the origin of the arrow of time, arguing that it cannot be presupposed.

**Initial-Condition Source (Albert)**: Irreversibility originates in the special properties of initial conditions. Albert argues that the source of macro-irreversibility is the "Past Hypothesis" — the universe's initial conditions have extremely low entropy.

### 3. The Fourth Source Proposed by This Paper: The Static Structural Source

The source of irreversibility proposed by this paper is the **static structural source**: irreversibility originates in the non-injectivity of the aggregation mapping.

This source differs from the above three in that:

- It **does not depend on dynamical evolution**. Even if the system is in equilibrium, even if there is no dissipative process, as long as the aggregation mapping is not injective, reverse inference is impossible.
- It **does not depend on the arrow of time**. The framework of this paper does not involve time; it involves only the information loss of the aggregation relation.
- It **does not depend on initial conditions**. The conclusion of this paper does not depend on any assumption about initial conditions.

### 4. Complementarity of the Static and Dynamical Sources

The static source and the dynamical source are **complementary**, not competing. They describe different levels of irreversibility:

- The **dynamical source** describes: why the evolution of the system over time is irreversible. This is an assertion about **processes in time**.
- The **static source** describes: why recovering the micro-state from a given macro-description is impossible. This is an assertion about **structural relations**.

A complete theory of irreversibility requires explaining both levels. The contribution of this paper is to provide a formal framework for the static level.

### 5. The Philosophical Significance of the Static Source

The philosophical significance of the static source lies in: **irreversibility is not necessarily dynamical**.

Consider a fully reversible dynamical system. In this system, the evolution of the micro-state over time is fully reversible — given the current micro-state, the past and future micro-states can be uniquely determined.

However, if we possess only the macro-description (and not the micro-state), then recovering the micro-state from the macro-description remains impossible — as long as the aggregation mapping is not injective. This means: **irreversibility may have a source more fundamental than dynamics — the non-injectivity of the aggregation mapping**.

This conclusion has direct implications for philosophical discussions of irreversibility. If irreversibility can have a static structural source, then the question "why does irreversibility exist" needs to be reformulated as: **Is irreversibility a feature of dynamical evolution, or a feature of structural relations? The framework of this paper shows that the latter is at least an independent source.**

### 6. The Philosophical Meaning of "Structural"

This paper uses the term "structural" to mean: not depending on the specific state of the system, dynamical evolution, or initial conditions, but depending only on the mathematical structure of the aggregation mapping.

In this sense, "structural" is opposed to "dynamical": dynamical features depend on temporal evolution, structural features do not depend on temporal evolution.

---

## VII. Objections and Responses

### Objection One: "Premise C ignores the role of experimental data and mathematical constraints."

**Response**: The candidate theories available to physicists are only `T1` and `T2`. Experimental data and mathematical consistency requirements do provide filtering conditions, but they do not constitute direct candidates for `T*`.

### Objection Two: "Structural loss is trivial."

**Response**: Structural loss is mathematically trivial. It is explicitly positioned as an auxiliary intuitive tool. The core argument of this paper does not depend on structural loss, but on Observation 1.

### Objection Three: "Observation 1 applies only to exact recovery."

**Response**: Correct. Observation 1 applies only to exact recovery. This paper deals only with the case of exact recovery.

### Objection Four: "The aggregation mapping can be improved to be injective."

**Response**: Correct. The conclusions of this paper depend on the chosen aggregation mapping. But this improvability is constrained in practice by the naturalist stance: the definition of the macro-state space is constrained by the number of observables.

### Objection Five: "The naturalist stance requires argument."

**Response**: Correct. The naturalist stance of this paper is a **premise**, not the conclusion of this paper's argument. The goal of this paper is not to argue for naturalism, but to show: under the naturalist premise, non-injectivity can provide a static structural source of irreversibility.

---

## VIII. Conclusion

The core result of this paper is: in the context of statistical-mechanical coarse-graining, the impossibility of "recovering the micro from the macro" is a purely structural fact, providing a **static structural source** for irreversibility.

The core contributions of this paper are:

1. Distinguishing three assertions: irreducibility, inexplicability, and impossibility of reverse inference.
2. Proposing that "the impossibility of reverse inference" is a purely structural fact — it does not depend on dynamical evolution, initial conditions, or randomness.
3. Arguing for the complementarity of the static and dynamical sources.
4. Under the naturalist stance, applying the formal framework to the physical world.

---

## IX. Open Questions

1. **Non-injectivity in the continuous case**: Can Observation 1 be extended to continuous micro-state spaces?
2. **Applicability of Premise C in the context of quantum gravity**: How can one argue that the reduction relations in quantum gravity can be realized as aggregation mappings?
3. **Unification of the static and dynamical sources**: How can one establish a unified theoretical framework that integrates the static and dynamical sources of irreversibility?

---

## X. References

[1] Albert, D. Z. (2000). *Time and Chance*. Harvard University Press.

[2] Batterman, R. W. (2002). *The Devil in the Details*. Oxford University Press.

[3] Butterfield, J. (2011). Emergence, Reduction and Supervenience. *Foundations of Physics*, 41(6), 920-959.

[4] Cover, T. M., & Thomas, J. A. (2006). *Elements of Information Theory* (2nd ed.). Wiley-Interscience.

[5] Frigg, R. (2007). Typicality and the Approach to Equilibrium in Boltzmannian Statistical Mechanics. *Philosophy of Science*, 74(5), 997-1008.

[6] Price, H. (1996). *Time's Arrow and Archimedes' Point*. Oxford University Press.

[7] Prigogine, I. (1980). *From Being to Becoming*. W. H. Freeman.

[8] Shannon, C. E. (1948). A Mathematical Theory of Communication. *Bell System Technical Journal*, 27(3), 379-423.

[9] Wallace, D. (2012). *The Emergent Multiverse*. Oxford University Press.

[10] Wilson, M. (2017). *Physics Avoidance*. Oxford University Press.

[11] Zhong, S. (2026). *On the Structural Source of Irreversibility — The Non-Injectivity of Macro-Descriptions and Its Epistemological Consequences* (Version 29.0). Equal System Repository.

---

## XI. Data Availability Statement

This paper is a work of theoretical derivation and does not involve the collection or analysis of empirical data.

---

## XII. Conflict of Interest Statement

The author declares that there are no conflicts of interest that could affect the research conclusions or academic judgment of this paper.

---

**Suggested Citation (APA Format)**:

Zhong, S. (2026). *On the Structural Source of Irreversibility — The Non-Injectivity of Macro-Descriptions and Its Epistemological Consequences* (Version 29.0). Equal System Repository.

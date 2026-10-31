# Signal, Exchange, and System Stability
## — An Analysis of Private Property Based on the Limit Theory of Meaning

| Item | Content |
| :--- | :--- |
| Title | Signal, Exchange, and System Stability — An Analysis of Private Property Based on the Limit Theory of Meaning |
| Author | Max Lance |
| Version | 3.1 |
| Date | 2026-08 |
| License | CC BY-NC 4.0 |
| Keywords | signal distribution, exchange continuity, private property, system stability, limit theory of meaning, fairness rupture |


---

## Abstract

This paper, drawing from the framework of the Limit Theory of Meaning, defines the survival resources, security opportunities, and political participation space within a system as "signals," and defines nodes' labor, consumption, taxation, and other behaviors as "exchange." It argues that the stability of a private property system does not depend on the fairness of signal distribution, but on the continuity of exchange relations. Even with extremely low signal density, marginal nodes are compelled to continue participating in exchange due to excessively high exit costs, thereby providing the system with the signal flow needed to maintain operation. The adjustment signals released at the boundary (welfare states, social security, tax regulation) do not change the core structure, but they are sufficient to prevent large-scale synchronized exits. Through five objection-response dialogues, three falsifiability conditions, and three sets of numerical experiments, this paper tests this proposition. It neither criticizes private property nor defends it, but merely attempts to describe its operational structure.

**Keywords**: signal distribution · exchange continuity · private property · system stability · limit theory of meaning · fairness rupture

---

## Theoretical Positioning Statement

This paper does not claim to surpass Marx. It operates within Marx's framework.

Marx answered: why capitalism must eventually perish.
This paper attempts to answer: why capitalism has not yet perished, and under what conditions it will.

The two questions are not opposed. They are two links in the same chain. The "signal-exchange" framework used here—continuity of exchange, signal distribution, peripheral nodes, adjustment signals—is a restatement, in more modern language, of a mechanism Marx had already identified: capital survives by sustaining the continuity of exchange, and when it itself breaks that continuity, Marx returns to the foreground.

This paper is not a refutation of Marx. It is a brick laid beneath his edifice.

---

## Literature Positioning: Why a Signal-Exchange Framework?

Marx (1867) advanced a classic thesis in *Capital*: the internal unfairness of private property would eventually lead to structural collapse of the system, to be replaced by a higher form of social organization. This thesis has been tested in multiple institutional experiments throughout the 20th century — but the results do not uniformly support Marx's prediction. Some private property systems (e.g., the Nordic welfare states) have maintained long-term stability while preserving the core structure of private property, by releasing adjustment signals (high taxes, high welfare) — they did not move toward collapse as Marx predicted.

Hayek (1944, 1960), on the other hand, argued that private property systems have self-regulating capacities, that unfairness is a natural result of market operation, and that it should not be "repaired" through state intervention. But Hayek's framework faces a different difficulty: if markets truly possess sufficient self-regulating capacity, why do systems nevertheless need to release adjustment signals such as welfare states and social security? The very existence of these signals suggests that certain pressures within the system are beyond what market regulation can handle.

This paper does not attempt to judge "who is right" between Marx and Hayek. Their theoretical aims differ — Marx is concerned with whether the system will be replaced, Hayek with whether the system should be interfered with — while this paper is concerned with a different set of questions: what structure does the operational stability of a private property system under persistent unfairness depend on? Where does the resilience of this structure come from? What role do boundary adjustment signals play?

The framework of this paper comes from the Limit Theory of Meaning (Lance, 2026): treating the system as a signal-exchange system and analyzing its stability structure. This framework requires neither the assumption that "unfairness necessarily leads to collapse" (Marx), nor the assumption that "the market automatically regulates everything" (Hayek). It asks only one question: **what structure does the stability of the system depend on?** This analytical level differs from both Marx and Hayek, and can be tested independently of either theoretical framework.

---

## Theoretical Framework and Methodological Statement

### Definition of Core Concepts

Before proceeding, it is necessary to strictly define the core concepts used in this paper.

**Signal**: refers to the survival resources, social status, security opportunities, and political participation space that flow within a system. Signals are not uniformly distributed; they are allocated according to the position, function, and exchange capacity of nodes. This paper primarily deals with **resource signals** — that is, actually allocated survival resources, security, and opportunities. Commitment signals (such as slogans, narratives) appear only as secondary references when relevant to legitimacy. Signals have three elements:

- **Density**: the total resources and security a node receives
- **Direction**: signals flow from internal nodes to marginal nodes, while signals from marginal nodes are filtered out
- **Filtration**: the mechanisms by which the system suppresses signals from marginal nodes through institutional, cultural, or discursive means

**Exchange**: refers to quantifiable transactional activities through which nodes obtain survival resources, including labor, consumption, and taxation. It does not include purely physical survival behaviors (such as breathing, sleeping), nor does it include symbolic behaviors that do not involve resource flow.

**Stability**: refers to a state of operation in which the system has not experienced structural collapse. It does not imply "efficient operation" or "good performance." A system can remain stable under conditions of low efficiency and severe unfairness — as long as its core operational structure remains intact.

**Continuity**: refers to the uninterrupted flow of overall signals to a degree that does not reach zeroing. It allows for local fluctuations and temporary exits.

### Methodological Statement: Conceptual Analysis, Institutional Description, and Numerical Verification

The methodological path adopted in this paper lies between **conceptual analysis**, **institutional description**, and **numerical verification**. Specifically, it describes the signal distribution structure of private property systems at a conceptual level, reveals its implicit operational logic, and engages in dialogue with existing theories (Marxism, laissez-faire, social democracy). In addition, this paper translates the core theses into operational hypotheses through an Agent-Based Model (ABM), and conducts falsifiable tests (see Appendix A).

The types of evidence used in this paper include:

1. **Conceptual definitions**: strict definitions of core concepts such as signal, exchange, stability, and continuity.
2. **Structural description**: description of the signal distribution structure, feedback asymmetry, and adjustment signal mechanisms of private property systems.
3. **Case references**: citations of publicly observable institutional phenomena as references for structural description, not as empirical proof.
4. **Objections and responses**: testing the robustness of the core thesis through five objection-response dialogues.
5. **Falsifiability conditions**: proposing three falsifiability conditions that are in principle testable.
6. **Numerical verification**: falsifiable testing of the three core hypotheses using an Agent-Based Model (see Appendix A).

---

## I. The Signal Distribution System

### 1.1 Definition of Signal

In this paper, "signal" refers to the survival resources, social status, security opportunities, and political participation space that flow within a system.

Signals are not uniformly distributed; they are allocated according to the position, function, and exchange capacity of nodes. The stability of a system depends on the continuity of signal flow, not on the balance of signal distribution.

This paper primarily deals with **resource signals** — that is, actually allocated survival resources, security, and opportunities. Commitment signals (such as slogans, narratives) appear only as secondary references when relevant to legitimacy.

Signals have three elements:

1. **Density**: the total resources and security a node receives.
2. **Direction**: signals flow from internal nodes to marginal nodes, while signals from marginal nodes are filtered out.
3. **Filtration**: the mechanisms by which the system suppresses signals from marginal nodes through institutional, cultural, or discursive means.

### 1.2 Two Types of Nodes

**Internal nodes** are at the system's core — high signal density, comprehensive security, prioritized resource allocation, and relatively stable operation.

**Marginal nodes** are at the system's periphery — low signal density, limited or near-zero security, and relatively vulnerable operation.

The stability of the system does not require equal signal density between the two types of nodes. It only requires that signal flow is not interrupted.

### 1.3 Definition of Stability

"Stability" in this paper refers to a state of operation in which the system has not experienced structural collapse.

It does not imply "efficient operation" or "good performance." A system can remain stable under conditions of low efficiency and severe unfairness — as long as its core operational structure remains intact.

---

## II. The Mechanism of Exchange Continuity

### 2.1 Definition of Exchange

"Exchange" in this paper refers to quantifiable transactional activities through which nodes obtain survival resources.

It includes labor, consumption, and taxation. It does not include purely physical survival behaviors (such as breathing, sleeping), nor does it include symbolic behaviors that do not involve resource flow.

### 2.2 Definition of Continuity

"Continuity" refers to the uninterrupted flow of overall signals to a degree that does not reach zeroing.

It allows for local fluctuations and temporary exits. A system can continue to operate even if some nodes temporarily withdraw from exchange, as long as the overall signal flow has not been interrupted to a degree that makes the system unsustainable.

### 2.3 Why Marginal Nodes Continue to Participate in Exchange

Even with extremely low signal density, marginal nodes are still compelled to participate in labor, consumption, investment, and taxation.

This compelled participation is not based on identification with the system, but on the basic conditions of survival. Thus, even when the signal distribution structure heavily favors internal nodes, the exchange behaviors of marginal nodes continue to provide labor and consumer markets for the system, maintaining the fuel for signal flow.

### 2.4 The Feedback Asymmetry of Private Property

The system's feedback loops primarily receive signals from internal nodes, while signals from marginal nodes are filtered or ignored.

When internal nodes perceive a threat to their own signal density, the system quickly adjusts to maintain their operational stability.

When marginal nodes send signals (such as poverty, unemployment, discontent), the system does not immediately make structural adjustments, but instead reduces signal intensity through local appeasement, discursive guidance, or institutional filtration.

This feedback asymmetry allows the system to maintain stability even under conditions of severe unfairness.

---

## III. State Institutions as Signal Stabilizers

### 3.1 The Dual Function of State Institutions

State institutions serve a dual function in the signal distribution system:

1. **Signal stabilizer**: maintaining the continuity of signal flow through resource allocation, social security, and policy regulation.
2. **Legitimacy maintainer**: sustaining the trust expectations of marginal nodes toward the system through the release of commitment signals.

### 3.2 The Coexistence of Full Coverage and Signal Zeroing

In many systems, full coverage (for internal nodes) coexists with signal zeroing (for marginal nodes) over long periods.

This structure can persist because the survival conditions of marginal nodes are compressed to the minimum, yet they still participate in exchange. As long as this participation is not interrupted, the system will not collapse.

### 3.3 Signal Distribution Differences Between Two Institutional Forms

Signal distribution structures differ across institutional forms, but the core logic of private property — maintaining signal flow through exchange — remains consistent across forms:

1. **Form A (biased toward internal priority)**: signals flow preferentially to internal nodes, and marginal node signal density approaches zero over the long term.
2. **Form B (biased toward market regulation)**: signals flow through exchange, and marginal node signal density is unstable but not completely zero.

Both forms operate in the same direction, differing only in the proportion and speed of signal distribution.

---

## IV. The Continuity Logic of Private Property

### 4.1 Exchange, Not Fairness

The core operational logic of private property is exchange.

Nodes participate in exchange through labor, consumption, taxation, investment, and other means, maintaining signal flow. Even if the signal density of marginal nodes is compressed to a very low level, as long as they continue to participate in exchange, the system can obtain the signals needed for its continuation from their participation — without needing to change their level of signal allocation.

### 4.2 Unfairness as Part of Operational State

Unfairness is not a "fault signal" of the system; it is one of its operational states.

Whether the system chooses to release adjustment signals at the boundary depends on whether its continuation requires such adjustment, not on the degree of unfairness.

---

## V. Structural Flaws of the "Replacement" Narrative

### 5.1 Marx's "Inevitable Replacement"

Marx's claim that "communism will inevitably replace capitalism" is a historical prediction, not a signal structure analysis.

It overlooks the system's capacity to release adjustment signals at the boundary to maintain its own continuation.

### 5.2 The Buffering Effect of Adjustment Signals

The adjustment signals released by systems at the boundary — welfare states, labor rights, social security, tax regulation — do not change the core structure of private property, but they are sufficient to reduce the risks posed by signal rupture in marginal nodes.

These adjustments allow the system to continue for a longer period without changing its core structure.

---

## VI. The Relationship Between System Stability and Fairness

### 6.1 The Source of Stability

System stability does not depend on fairness, but on the continuity of node participation.

As long as the exchange network is not interrupted, the system can maintain operation. This explains why fairness issues at the institutional level can persist over the long term while the system still maintains its basic operational structure.

### 6.2 The Levels of Fairness Rupture

Fairness rupture manifests as the structural differentiation between full coverage and signal zeroing.

This differentiation can persist over the long term because it does not directly affect the continuity of exchange relations. The system can tolerate widespread signal distribution inequality, as long as such inequality does not threaten the basic structure of node participation in exchange.

### 6.3 Why the System Does Not Need to Resolve Unfairness

Fairness is not the operational goal of private property.

It is a secondary signal, and its density is insufficient to force the system to make structural adjustments. The system only releases local adjustment signals at the boundary to maintain the minimum level of node participation.

This feature explains the resilience of private property systems in the face of long-term unfairness — they adjust, but they do not change their core structure.

---

## VII. Possible Objections and Falsifiability Conditions

Any theoretical argument must be open to questioning of its core claims. This chapter outlines the main objections this paper may face, responds to each, and then proposes three falsifiability conditions that are in principle testable.

### 7.1 Responses to Possible Objections

#### Objection 1: Marginal Nodes Do Not Voluntarily Participate in Exchange.

**Response:** This objection reveals the distinction between "compelled participation" and "voluntary participation," but it does not negate the core thesis — it only reveals the constraint conditions of exchange continuity. The system does not require marginal nodes to participate "voluntarily"; it only requires them to participate "actually." Marginal nodes do not exit not because the system provides sufficient incentives, but because exit would mean a sharp rise in survival costs. This "exit cost" itself is the structural force maintaining exchange continuity.

**Supplementary Note:** "Not exiting" is not equivalent to "effective participation." When the participation of marginal nodes declines to a level that only sustains their own survival, the signal density they provide to the system decreases significantly. The system does not require every node to generate high-density signals, but it needs overall signal density to remain above a threshold.

**Case Reference:** In many countries' food assistance systems, low-income households face a "cliff effect" — a slight increase in income may lead to the loss of all benefits, while the new income is far from enough to compensate for the loss. This "excessive exit cost" structure means that even if marginal nodes have the opportunity to improve their situation, they often choose to remain in the system's exchange relations.

**Numerical Verification:** Experiment 1 in Appendix A shows that when exit cost `c` exceeds the signal gap, marginal nodes' participation rate is 1.0; when `c` is below the gap, participation is 0.2. Exit cost is the direct source of stability.

---

#### Objection 2: Unfairness Reduces System Efficiency.

**Response:** This objection points to the long-term costs of fairness rupture, but it conflates "the system is still running" with "the system is running well." The thesis is that the system can maintain operation under conditions of unfairness — it does not promise that the system runs "well" or "efficiently," only that it "does not collapse." Unfairness does reduce system efficiency and increase social costs, but these costs accumulate gradually rather than exploding all at once.

**Supplementary Note:** The critical point of efficiency decline is not a fixed value. When social operating costs continue to rise and the system cannot offset them through adjustment signals, the system enters a cycle of "efficiency decline — adjustment space shrinking — further efficiency decline." The resilience of the system lies not in avoiding efficiency decline, but in whether it can complete morphological adjustment before efficiency decline reaches the critical point.

**Case Reference:** During economic transitions, some countries experienced severe production decline and inflation, but the system did not completely collapse. After completing morphological adjustment at the boundary, the system continued to operate in a different direction.

---

#### Objection 3: Node Exit.

**Response:** The exit of marginal nodes is a gradual process, not a one-time event. The system releases adjustment signals at the boundary to respond to exits. Moreover, marginal nodes "exiting" the labor market is not equivalent to "exiting" the system — they still consume, pay taxes, and occupy resources. True system collapse occurs through large-scale, simultaneous, irreversible exits, which are extremely rare in history.

**Case Reference:** In extreme cases of economic collapse, large-scale population displacement does occur. But even in such extreme situations, the system continues to operate in a severely atrophied form, never completely zeroing out.

**Numerical Verification:** Experiment 2 in Appendix A shows that under gradual shocks, the system's participation rate declines smoothly rather than collapsing all at once. This provides a window for adjustment signals to intervene.

---

#### Objection 4: Legitimacy.

**Response:** Legitimacy is indeed an important secondary signal, but it is not a sufficient condition for system operation. A system can continue to operate under declining legitimacy — as long as exchange relations continue. Marginal nodes' behavior is driven by structural constraints (survival pressure, legal enforcement, absence of alternatives), not by "identification with the system." Declining legitimacy increases the system's operating costs, but it does not immediately lead to system collapse.

**Supplementary Note:** The bearable boundary of legitimacy costs depends on the system's alternatives. When legitimacy declines to the point where marginal nodes begin to organize collective action, the system typically releases adjustment signals to reduce the appeal of organized action, thereby keeping legitimacy costs within an acceptable range.

**Case Reference:** Some countries, while retaining the core structure of private property, have compressed wealth inequality to relatively low levels through high-tax, high-welfare adjustment signals. The system maintains legitimacy through strong adjustment signals, but the core structure of private property does not change.

---

#### Objection 5: The Buffering Effect of Adjustment Signals Is Limited.

**Response:** This objection points to the resource constraints of adjustment signals, but it overestimates the rigidity of these constraints. Systems can expand adjustment space by adjusting the tax contributions of internal nodes, extending retirement age, and introducing technological substitution. More importantly, the effectiveness of adjustment signals does not require covering all marginal nodes — it only requires covering enough nodes to prevent large-scale, synchronized exits.

**Supplementary Note:** There is a limit to how much internal nodes can bear in terms of tax adjustments. When the tax burden on internal nodes continues to rise, their signal density may also be affected, creating new pressure at the system's boundary. Therefore, the system needs to maintain a balance between "expanding adjustment signals" and "maintaining the signal density of internal nodes."

**Case Reference:** In many countries' pension systems, there are significant gaps in benefits between different groups. The system maintains operation through adjustment signals such as delayed retirement, system integration, and national coordination. These adjustments do not resolve the unfairness itself, but they prevent unfairness from triggering systemic collapse — the extremely low level of signal coverage is just enough to maintain the minimum participation of marginal nodes "still within the system."

**Numerical Verification:** Experiment 2 in Appendix A shows that adjustment signals can prevent system collapse, but **the timing of adjustment determines survival**. With the same adjustment strength, timely release leads to stability, while delayed release leads to collapse.

### 7.2 Falsifiability Conditions

If the core thesis of this paper is to hold, it must be open to challenge — that is, there must be discoverable facts or arguments that, if they turned out to be true, would seriously weaken or require revision of the paper's central position.

1. **Falsifiability Condition 1 (Continuity Disruption):** If a private property system, after its marginal nodes exit exchange on a large scale (e.g., long-term mass unemployment, sharp decline in labor force participation), still maintains its original signal density and operational stability, then the thesis "system depends on exchange continuity" would no longer hold.

2. **Falsifiability Condition 2 (Structural Transformation):** If a private property system undergoes a complete structural transformation at the boundary (e.g., private property is fully replaced by public ownership), and this transformation is not achieved within the boundary adjustment range of private property, then the thesis "the system only undergoes morphological adjustment" would no longer hold.

3. **Falsifiability Condition 3 (Stable Operation of Non-Exchange Systems):** If there exists a system that does not depend on exchange relations between nodes yet can maintain stable signal flow over the long term, then the thesis "the stability of private property depends on exchange relations" would no longer hold.

---

## VIII. Observational Note

The analytical framework of this paper can be preliminarily observed through the following publicly observable phenomena:

1. **Signal distribution differences**: systematic differences in pensions and social security levels between different groups can be observed in social security systems across countries.
2. **Unfairness trends**: income distribution inequality is a long-term institutional phenomenon.
3. **Existence of adjustment signals**: trends in social security expenditure as a percentage of GDP across countries reflect the patterns of adjustment signal release at the system's boundary.

The value of the above observations is not to "prove" the thesis of this paper. Its value lies in showing that the structure described in this paper is not merely a logical derivation existing on paper, but an observable institutional phenomenon. Readers interested in this may verify it themselves through relevant data sources.

---

## IX. Conclusion

This paper does not critique private property, nor does it defend it.

It attempts to describe how a system that distributes signals unequally can nevertheless remain stable — not because it is just, but because it is continuous.

This paper has argued the following theses:

1. The stability of a private property system does not depend on the fairness of signal distribution, but on the continuity of exchange relations.
2. Even with extremely low signal density, marginal nodes are compelled to continue participating in exchange due to excessively high exit costs, thereby providing the system with the signal flow needed to maintain operation.
3. The adjustment signals released at the boundary (welfare states, social security, tax regulation) do not change the core structure, but they are sufficient to prevent large-scale synchronized exits.
4. Unfairness is not a "fault signal" of the system, but one of its operational states.

This paper does only an analytical statement. It does not claim that this is how things should be. It claims only that this is how they work. What to do about it belongs elsewhere.

---

## Acknowledgments

This paper has benefited from the inspiration of the Equal System philosophical framework. All views expressed and any possible errors remain the sole responsibility of the author.

---

## Data Availability Statement

This paper is a theoretical work in conceptual analysis. The numerical results in Appendix A were generated by Python code and are reproducible. The institutional phenomena mentioned (such as social security systems, welfare states) are publicly observable empirical facts. Readers seeking specific data may consult public databases from organizations such as the OECD, World Bank, and ILO.

---

## Conflict of Interest Statement

The author declares that there are no conflicts of interest that could affect the research conclusions or academic judgment of this paper. This paper has not received funding from any institution or organization.

---

## References

### Equal System Philosophical Framework

- Lance, Max. (2026). *On the Limits of Meaning: A Verificationist Framework* (Version 3.0). Equal System Repository.

### Theoretical Texts

- Marx, K. (1867). *Capital* (Vol. 1).
- Hayek, F. A. (1944). *The Road to Serfdom*.
- Hayek, F. A. (1960). *The Constitution of Liberty*.

---

## Appendix A: Experimental Verification

This appendix reports numerical experiments testing the three core hypotheses of *Signal, Exchange, and System Stability*. The experiment code is located in the `signal-exchange-stability/experiments/` directory of the project repository.

### A.1 Experimental Model

An Agent-Based Model (ABM) is used. N = 1000 nodes, of which 20% are internal nodes and 80% are marginal nodes. Each node has a signal density `s_i`. Internal node signal `s_internal = 100`; marginal node signal `s_edge` is variable.

**Node decision rule**: Each node compares the payoff of "participating in exchange" and "exiting exchange":

- Participation payoff: `s_i + c` (staying in the system earns compensation for exit cost)
- Exit payoff: `s_i × (1 − d)` (resources are discounted after exit)

If the participation payoff is higher than the exit payoff, the node participates. Equivalently: `motivation_i ≤ c_i`, where `motivation_i = (s_max − s_i) / s_max` is the signal gap.

**System stability**: Whether the participation rate `P` of nodes in exchange is always above the collapse threshold `P_crit = 0.5`.

### A.2 Experiment 1: Exit-Cost Threshold (H1, H2)

**Hypothesis**: Stability comes from exit cost, not from fairness.

**Method**: Three scenarios, each running 20 trials, reporting mean and standard deviation of participation rate.

- Scenario 1: High inequality (internal 100, marginal 10, gap 0.9), exit cost c from 0.1 to 0.8
- Scenario 2: High inequality (gap 0.9), exit cost c from 0.9 to 1.0
- Scenario 3: Low inequality (internal 100, marginal 80, gap 0.2), exit cost c from 0.1 to 0.5

**Results**:

| Scenario | c | Participation rate | Status |
| :--- | :--- | :--- | :--- |
| 1 (high inequality) | 0.10 | 0.20 | Collapse |
| 1 (high inequality) | 0.30 | 0.20 | Collapse |
| 1 (high inequality) | 0.50 | 0.20 | Collapse |
| 1 (high inequality) | 0.80 | 0.20 | Collapse |
| 2 (high inequality) | 0.90 | 1.00 | Stable |
| 2 (high inequality) | 0.95 | 1.00 | Stable |
| 2 (high inequality) | 0.99 | 1.00 | Stable |
| 2 (high inequality) | 1.00 | 1.00 | Stable |
| 3 (low inequality) | 0.10 | 0.20 | Collapse |
| 3 (low inequality) | 0.30 | 1.00 | Stable |
| 3 (low inequality) | 0.50 | 1.00 | Stable |

**Conclusion**: H1 and H2 are supported.

1. **The exit-cost threshold equals the signal gap**. High inequality requires `c ≥ 0.9` for stability; low inequality requires only `c ≥ 0.2`.
2. **Stability comes from exit cost, not from fairness**. Under low exit cost, even low inequality collapses; under high exit cost, even high inequality remains stable.
3. **Inequality is an operational parameter, not a fault signal**. It determines how high the exit cost must be to maintain stability, not whether the system collapses.

**New information**: The experiment yields a quantitative conclusion not stated in the original text — **"System stability depends not on whether inequality exists, but on whether the exit cost exceeds the inequality gap."**

### A.3 Experiment 2: The Role of Adjustment Signals (H3)

**Hypothesis**: Adjustment signals released at the boundary can prevent large-scale synchronized exits.

**Method**: Heterogeneous node model. Each marginal node has its own exit cost `c_i ~ N(0.5, 0.15)`, so that nodes exit gradually rather than all at once. The shock starts at round 5, with marginal signal decreasing by 2 each round (gradual shock). The warning threshold is `P_warn = 0.85`; the collapse threshold is `P_crit = 0.5`.

Five groups:

- Control: no adjustment signal
- Group A: adjustment starting at round 5, +2 per round
- Group B: adjustment starting at round 5, +5 per round
- Group C: adjustment starting at round 5, +10 per round
- Group D: adjustment starting at round 50, +10 per round (delayed)

**Results**:

| Group | Adjustment | Final participation | Status |
| :--- | :--- | :--- | :--- |
| Control | None | 0.499 | Collapse (16 rounds) |
| A | +2/round | 0.830 | Stable (300 rounds) |
| B | +5/round | 0.845 | Stable (300 rounds) |
| C | +10/round | 0.916 | Stable (300 rounds) |
| D | Round 50, +10 | 0.499 | Collapse (16 rounds) |

**Conclusion**: H3 is supported.

1. **Adjustment signals can prevent collapse**. The control group collapses in 16 rounds; A, B, and C are stable for 300 rounds.
2. **Adjustment strength affects steady-state level**. +2 → 0.83, +5 → 0.845, +10 → 0.916. The stronger the adjustment, the higher the steady-state participation.
3. **Timing determines survival**. Group D has the same adjustment strength as Group C (+10), but starts later. The result is collapse for D, stability for C. Adjustment must start before collapse — this is precisely what the paper means by "released at the boundary."

**New information**: Adjustment signals only raise `s_edge` (marginal node signal); they **do not change `s_internal` (internal node signal)**, nor the exchange rule itself. The system can rescue itself, but the core structure remains unchanged. This exactly confirms the paper's statement: "The adjustment signals released at the boundary do not change the core structure, but they are sufficient to prevent large-scale synchronized exits."

### A.4 Overall Conclusion

| Hypothesis | Content | Result |
| :--- | :--- | :--- |
| H1 | Stability comes from exchange continuity, not from fairness | Supported |
| H2 | Marginal nodes are compelled to participate due to high exit cost | Supported |
| H3 | Adjustment signals can prevent large-scale synchronized exits | Supported |

**Core conclusion**: All three core hypotheses of the paper are supported.

**Key refinement**: The experiments yield a conclusion not precisely stated in the original text — **"System stability depends not on whether inequality exists, but on whether the exit cost exceeds the inequality gap."** This sentence is recommended for insertion into Section 6.1 of the paper.

### A.5 Data Availability

Experiment code:

- `signal-exchange-stability/experiments/exp_signal_exchange.py` (H1, H2)
- `signal-exchange-stability/experiments/exp_adjustment_signal.py` (H3)

Raw outputs: the `signal-exchange-stability/results/` directory.
Runtime environment: local Termux + Python 3 (no external dependencies).

---

## Final Note

The core message this paper attempts to convey is: **a system that distributes signals unequally can remain stable over the long term — not because it is just, but because it is continuous. The resilience of private property lies not in its resolution of unfairness, but in its making unfairness bearable — a signal level just low enough to maintain the minimum participation of marginal nodes "still within the system."**

This paper is an applied extension of the **Equal System** philosophical framework to institutional analysis. The core concepts of "signal" and "exchange" come from the Limit Theory of Meaning, and this paper applies them to the stability analysis of private property systems.

This paper does not critique private property, nor does it defend it. It merely attempts to describe its operational structure.

---

**Suggested Citation (APA format):**

Lance, Max. (2026). *Signal, Exchange, and System Stability: An Analysis of Private Property Based on the Limit Theory of Meaning* (Version 3.1). Equal System Repository.

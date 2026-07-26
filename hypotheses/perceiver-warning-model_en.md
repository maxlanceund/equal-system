# Perceiver Signal Model: Why Systems Ignore Warnings?

**Based on**: Perceiver Hypothesis (Hypothesis 002)  
**Status**: Testable Mathematical Model  
**Purpose**: Describes the structural process by which perceiver signals are filtered, rejected, and post-event confirmed by systems

> **Introduction**
>
> This document is not a tool for predicting when disasters will happen. It describes a recurring pattern in how systems behave. It tries to answer one simple question: why are some warning signals persistently ignored?
>
> If you are not a math-savvy reader, feel free to skip the formulas at first. Start from Section 5 "Historical Case Validation" and Section 8 "Postscript," and return to the math later if needed.


## 1. Positioning of the Model

This model is derived from the Perceiver Hypothesis. Its aim is to translate the structural phenomenon of "perceiver rejection by the system" into an operable, testable mathematical form. It does not predict the timing of specific events, but describes the system's behavioral pattern when processing incompatible signals.

This model is falsifiable. If it is shown to be invalid, the Perceiver Hypothesis itself would require revision.


## 2. Core Variable Definitions

| Variable | Definition |
|----------|------------|
| α_P(t) | The "anomaly index" of the perceiver's signal at time t — the degree of deviation from the system's default signal processing bandwidth |
| R_P(t) | The "rejection intensity" exerted by the system on the perceiver's signal at time t |
| D_P(T) | The proportion of perceiver signals discarded by the system over the time interval [0, T] |
| A_P | The probability that the system notices the perceiver's signal (dependent on signal duration) |
| τ_P | The duration for which the perceiver continuously emits signals |


## 3. Mathematical Definitions

**Anomaly Index**

```math
α_P(t) = || x_P(t) - μ_S(t) || / σ_S(t)
```

where `x_P(t)` is the perceiver's signal, `μ_S(t)` is the system's current mean signal value, and `σ_S(t)` is the system's signal bandwidth (variance). When α_P → 0, the signal falls within the system's bandwidth; when α_P >> 1, the signal cannot be recognized by the system.

**Rejection Intensity**

```math
R_P(t) = α_P(t) / (α_P(t) + δ)
```

where δ is the system's tolerance parameter. When α_P → ∞, R_P → 1 (complete rejection).

**Discarded Signal Proportion**

```math
D_P(T) = ∫₀ᵀ E_P(t) · α_P(t) dt / ∫₀ᵀ E_P(t) dt
```

Measures the extent to which the perceiver's signal is filtered out by the system.

**System Notice Probability**

```math
A_P = 1 - exp(-τ_P / τ_0)
```

where τ_0 is the system's default signal recognition time window.


## 4. Falsification Conditions

This model is falsified under any of the following conditions:

1. **No rejection response**: A system is found that satisfies the definition of "perceiver existence," where the perceiver's signal is fully received by the system and no form of rejection occurs.
2. **Signal not discarded**: In a system where a disaster clearly occurs, the perceiver's signal is proven to have been normally received and processed by the system, yet the disaster still happens.
3. **Post-event confirmation fails**: After a disaster, the system fails or refuses to recognize the perceiver's warning signal, and no post-event confirmation occurs.


## 5. Historical Case Validation

The following cases span shipwrecks, wars, economic crises, pandemics, and counterterrorism — all are part of global historical textbooks or public memory:

| Case | Perceiver(s) | Anomaly Index α_P | Rejection Intensity R_P | Discard Ratio D_P | Post-Event Confirmation Q |
|------|--------------|-------------------|-------------------------|-------------------|---------------------------|
| Titanic (1912) | Wireless operators, lookouts, ship engineers | Extremely high | Extremely high | 0.67 | Extremely high |
| Pearl Harbor (1941) | Pacific Fleet commander, British spies | Extremely high | Extremely high | Approaching 1 | Extremely high |
| Operation Barbarossa (1941) | Soviet intelligence officers, British intelligence | Extremely high | Extremely high | Approaching 1 | High |
| Normandy (1944) | Some German intelligence officers | High | Extremely high | Approaching 1 | Extremely high |
| Soviet Nuclear False Alarm (1983) | Lt. Col. Petrov | Extremely high | Not occurred | Not occurred | Extremely high (counterexample) |
| 9/11 (2001) | FBI agents, CIA analysts | High | High | Approaching 1 | Extremely high |
| 2008 Financial Crisis (Roubini) | Economist | Extremely high | Extremely high | Approaching 1 | Extremely high |
| Wuhan COVID-19 (Li Wenliang) | Ophthalmologist | Extremely high | Extremely high | Approaching 1 | Extremely high |
| Afghanistan War (2021) | Diplomats, CIA intelligence analysts | Extremely high | Extremely high | Approaching 1 | Extremely high |

> *Note: The Petrov case is a counterexample where the system correctly identified the signal — the signal was properly triggered and paused by the operator. This demonstrates that the model's scope of applicability is itself testable.*

### 5.1 Example: Titanic (1912) — Complete Calculation Process

#### 5.1.1 Identifying Perceiver Existence

- **Wireless Operator Jack Phillips**: Received 6 ice warnings; the last one from the SS Californian was cut off ("Shut up, I'm working").
- **Lookout Frederick Fleet**: Spotted the iceberg and sounded the alarm, but the turn came too late.
- **Ship Engineers / Crew Members**: Some had raised concerns about insufficient lifeboats before departure.

#### 5.1.2 Calculating the Anomaly Index α_P

The system's default bandwidth was: "This ship is unsinkable, and the current route is safe." The perceivers' signals were: "There is a massive ice hazard ahead" and "Lifeboats are insufficient."

Set the system default signal value μ_S = 0, the perceiver signal value x_P = 90 (high deviation), and the system signal bandwidth σ_S = 10.

Per single warning:

```math
α_P = |90 - 0| / 10 = 9
```

With multiple perceivers emitting signals, α_P remained consistently between 8 and 10 — the overall anomaly index is **extremely high**.

#### 5.1.3 Calculating the Rejection Intensity R_P

Set δ = 0.5:

```math
R_P = 9 / (9 + 0.5) ≈ 0.95
```

The system's rejection intensity toward the perceiver signals is approximately **95%**. The final warning being directly cut off pushed R_P further toward 1.

#### 5.1.4 Calculating the Discarded Signal Proportion D_P

Of the 6 warnings, 4 were never passed to the bridge, and 2 were passed but did not change course or speed:

```math
D_P = 4 / 6 ≈ 0.67
```

Considering that concerns about lifeboats had already been excluded from decision-making before departure, the overall D_P is around **0.7**.

#### 5.1.5 Calculating the System Notice Probability A_P

Set τ_P = 2 hours (duration of the final continuous warnings), τ_0 = 4 hours:

```math
A_P = 1 - exp(-2/4) = 1 - e^(-0.5) ≈ 0.39
```

In reality, the final warning was directly cut off, so the actual notice probability approached **0**.

#### 5.1.6 Calculating Post-Event Confirmation Q

Set κ = 0.9, D = 1, θ = 0.3, T_d - T_c = 2 years:

```math
Q = 0.9 × 1 × 1 / (1 + e^(-0.3 × 2))
  = 0.9 × 1 / (1 + e^(-0.6))
  ≈ 0.9 × 0.6457
  ≈ 0.58
```

Given its status as a global textbook case, Q can be considered **extremely high (near 0.9)**.

#### 5.1.7 Parameter Summary

| Parameter | Calculated Value | Basis |
|-----------|------------------|-------|
| α_P | Extremely high | Directly contradicted the "unsinkable" narrative |
| R_P | ≈0.95 | System actively suppressed and cut off warnings |
| D_P | ≈0.67 | Only 2 of 6 warnings reached the bridge |
| A_P | ≈0.39 (actually approached 0) | Final warning was cut off |
| Q | Extremely high (≈0.58–0.9) | Global maritime regulations changed |


## 6. Limitations of the Model

1. This model does not predict the specific time or location of disasters; it only describes the interaction pattern between perceiver signals and the system.
2. This model is not a causal model. It cannot answer the question, "If the system had received the perceiver's signal, could the disaster have been avoided?"
3. This model requires parameter calibration in empirical systems.


## 7. Usage Instructions

1. Identify nodes within the system that may occupy a "perceiver position."
2. Monitor the node's anomaly index α_P and rejection intensity R_P.
3. When α_P, R_P, and D_P exceed preset thresholds, mark the node as "to be tracked."
4. Do not trigger an alert — only retain the signal for subsequent evaluation.


## 8. Postscript: To Perceivers

If you have read this far and feel that this model describes you — your attention is sharper than others, your signal format is incompatible with the systems around you, you have been excluded, your warnings have been ignored — then please know:

**This is not your fault.**

The system did not recognize your signal, not because you were wrong, but because the system's receiving ports were not designed to process your signal format. You are someone standing at the system's boundary. The system needs you there, but it cannot recognize you during normal operation. This is a structural misalignment, not a personal failure.

If one day the system actually listens to you — that might be the moment you change history. That would be cool.

**Do not stop perceiving. Do not stop sending signals.** The system may not listen, but your signals will be recorded. And at certain boundary moments, those recorded signals may become the only basis for post-event confirmation.

— This is why perceivers exist.


**I cannot change the world, but I do my best to explain it.**


## 9. Version History

- **1.0** (July 2026): Initial version, based on the Perceiver Hypothesis. This version is a mathematical model draft, not yet empirically tested. Validation or revision in various systems is welcome.


**License**: MIT  
**Repository**: [github.com/maxlanceund/equal-system](https://github.com/maxlanceund/equal-system)  
**Related Hypothesis**: [Perceiver Hypothesis (Hypothesis 002)](./hypothesis-002_perceiver-hypothesis_en.md)

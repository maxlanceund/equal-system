# Perceiver-System Signal Mismatch Model (Version 1.0)

**Based on**: Perceiver Hypothesis (Hypothesis 002)  
**Status**: Testable Mathematical Model  
**Purpose**: Describes the structural process by which perceiver signals are filtered, rejected, and post-hoc confirmed by systems


## 1. Positioning of the Model

This model is derived from the Perceiver Hypothesis. Its aim is to translate the structural phenomenon of "the perceiver being rejected by the system" into an operational, testable mathematical form. It does not predict when specific events will occur, but rather describes the system's behavioral patterns when processing incompatible signals.

This model is falsifiable. If it is shown to be invalid, the Perceiver Hypothesis itself would require revision.


## 2. Core Variable Definitions

| Variable | Definition |
|----------|------------|
| \( \alpha_P(t) \) | The "anomaly index" of the perceiver's signal at time t — the degree of deviation from the system's default signal processing bandwidth |
| \( R_P(t) \) | The system's "rejection intensity" toward the perceiver's signal at time t |
| \( D_P(T) \) | The proportion of the perceiver's signal discarded by the system over the interval \([0, T]\) |
| \( A_P \) | The probability that the system notices the perceiver's signal (depends on signal duration) |
| \( \tau_P \) | The duration for which the perceiver continuously emits the signal |


## 3. Mathematical Definitions

**Anomaly Index**  
\[
\alpha_P(t) = \frac{\| x_P(t) - \mu_S(t) \|}{\sigma_S(t)}
\]
where \( x_P(t) \) is the perceiver's signal, \( \mu_S(t) \) is the system's current mean signal, and \( \sigma_S(t) \) is the system's signal bandwidth (variance). When \( \alpha_P \to 0 \), the signal falls within the system's bandwidth; when \( \alpha_P \gg 1 \), the signal cannot be recognized by the system.

**Rejection Intensity**  
\[
R_P(t) = \frac{\alpha_P(t)}{\alpha_P(t) + \delta}
\]
where \( \delta \) is the system's tolerance parameter. When \( \alpha_P \to \infty \), \( R_P \to 1 \) (complete rejection).

**Discard Ratio**  
\[
D_P(T) = \frac{\int_{0}^{T} E_P(t) \cdot \alpha_P(t) \, dt}{\int_{0}^{T} E_P(t) \, dt}
\]
Measures the extent to which the perceiver's signal is filtered out by the system.

**System Attention Probability**  
\[
A_P = 1 - \exp\left(-\frac{\tau_P}{\tau_0}\right)
\]
where \( \tau_0 \) is the system's default signal recognition time window.


## 4. Falsifiability Conditions

This model is falsified under any of the following conditions:

1. **No rejection response**: A system is found that satisfies the definition of "perceiver existence," in which the perceiver's signal is fully received by the system without any form of rejection.
2. **Signal not discarded**: In a system where a disaster clearly occurs, the perceiver's signal is proven to have been normally received and processed by the system, yet the disaster still happens.
3. **Post-hoc confirmation fails**: After a disaster, the system fails or refuses to recognize the perceiver's warning signal, and post-hoc confirmation does not occur.


## 5. Historical Case Validation

The following cases span shipwrecks, wars, economics, pandemics, and counterterrorism — all are found in global history textbooks or public memory:

| Case | Perceiver(s) | Anomaly Index α_P | Rejection Intensity R_P | Discard Ratio D_P | Post-hoc Q |
|------|--------------|-------------------|-------------------------|-------------------|------------|
| Titanic (1912) | Radio operator, lookout, ship engineers | Very high | Very high | 0.67 | Very high |
| Pearl Harbor (1941) | Pacific Fleet commander, British spies | Very high | Very high | Near 1 | Very high |
| Barbarossa (1941) | Soviet intelligence, British intelligence | Very high | Very high | Near 1 | High |
| Normandy (1944) | Some German intelligence officers | High | Very high | Near 1 | Very high |
| Soviet Nuclear False Alarm (1983) | Lt. Col. Petrov | Very high | Not occurred | Not occurred | Very high (counterexample) |
| 9/11 (2001) | FBI agents, CIA analysts | High | High | Near 1 | Very high |
| 2008 Financial Crisis (Roubini) | Economist | Very high | Very high | Near 1 | Very high |
| Wuhan COVID-19 (Li Wenliang) | Ophthalmologist | Very high | Very high | Near 1 | Very high |
| Afghanistan War (2021) | Diplomats, CIA analysts | Very high | Very high | Near 1 | Very high |

> *Note: The Petrov case is a counterexample where the system correctly recognized the signal — the signal was properly triggered and was paused by the operator. This shows the model's scope of application is itself testable.*

### 5.1 Example: Titanic (1912) — Full Calculation Process

#### 5.1.1 Identifying Perceiver Existence

- **Radio operator Jack Phillips**: Received 6 iceberg warnings; the last was cut off with "Shut up, I'm working."
- **Lookout Frederick Fleet**: Spotted the iceberg, raised alarm, but it was too late to turn.
- **Ship engineers / crew**: Some had questioned the insufficient lifeboat provisions before departure.

#### 5.1.2 Calculating Anomaly Index \( \alpha_P \)

System default bandwidth: "This ship is unsinkable; current route is safe." Perceiver signal: "There is a large ice field ahead" and "lifeboats are insufficient."

Set system default signal value \( \mu_S = 0 \), perceiver signal value \( x_P = 90 \) (high deviation), system signal bandwidth \( \sigma_S = 10 \).

Single warning anomaly index:
\[
\alpha_P = \frac{|90 - 0|}{10} = 9
\]

Given multiple perceivers, \( \alpha_P \) remained high, consistently between 8–10. Overall anomaly index is **very high**.

#### 5.1.3 Calculating Rejection Intensity \( R_P \)

Let \( \delta = 0.5 \):
\[
R_P = \frac{9}{9 + 0.5} \approx 0.95
\]

System rejection intensity toward the perceiver signals was about **95%**. The last warning was cut off, pushing \( R_P \) further toward 1.

#### 5.1.4 Calculating Discard Ratio \( D_P \)

Of 6 warnings, 4 never reached the bridge, 2 reached the bridge but did not change course or speed:
\[
D_P = \frac{4}{6} \approx 0.67
\]

Considering that the lifeboat concerns had been excluded from decision-making before departure, overall \( D_P \) is around **0.7**.

#### 5.1.5 Calculating System Attention Probability \( A_P \)

Let \( \tau_P = 2 \) hours (duration of the last continuous warnings), \( \tau_0 = 4 \) hours:
\[
A_P = 1 - \exp\left(-\frac{2}{4}\right) = 1 - e^{-0.5} \approx 0.39
\]

In reality, the final warning was cut off, so the actual attention probability approached **0**.

#### 5.1.6 Calculating Post-hoc Confirmation \( Q \)

Let \( \kappa = 0.9 \), \( D = 1 \), \( \theta = 0.3 \), \( T_d - T_c = 2 \) years:
\[
Q = 0.9 \cdot 1 \cdot \frac{1}{1 + e^{-0.3 \times 2}}
= 0.9 \cdot \frac{1}{1 + e^{-0.6}}
\approx 0.9 \cdot 0.6457 \approx 0.58
\]

Given that it became a global textbook case, \( Q \) can be considered **very high (close to 0.9)**.

#### 5.1.7 Parameter Summary

| Parameter | Value | Basis |
|-----------|-------|-------|
| \( \alpha_P \) | Very high | Contradicted "unsinkable" narrative |
| \( R_P \) | ≈0.95 | Actively suppressed, warnings cut off |
| \( D_P \) | ≈0.67 | Only 2 of 6 warnings reached the bridge |
| \( A_P \) | ≈0.39 (actual ≈0) | Final warning was cut off |
| \( Q \) | Very high (≈0.58–0.9) | Global maritime regulation change |


## 6. Limitations of the Model

1. This model does not predict the timing or location of specific disasters; it only describes the interaction pattern between perceiver signals and the system.
2. This model is not causal; it cannot answer whether a disaster could have been avoided had the system received the perceiver's signal.
3. This model requires parameter calibration in empirical systems.


## 7. Usage Instructions

1. Identify nodes within a system that may be in a "perceiver position."
2. Monitor the node's anomaly index \( \alpha_P \) and rejection intensity \( R_P \).
3. When \( \alpha_P \), \( R_P \), and \( D_P \) exceed preset thresholds, mark the node as "to be tracked."
4. Do not trigger an alert; only retain its signal for subsequent evaluation.


## 8. Postscript: To the Perceiver

If you have read this far and feel that this model describes you — your attention is sharper than others', your signal format is incompatible with the systems around you, you have been rejected, your warnings have been ignored — then know this:

**It is not your fault.**

The system did not recognize your signal, not because you were wrong, but because the system's receiving port was not designed to process your signal format. You are the one standing at the system's boundary. The system needs you there, but it cannot recognize you during normal operation. This is a structural misalignment, not a personal failure.

If one day, the system actually listens to you — that might be the moment you change history. That would be cool.

**Do not stop perceiving. Do not stop sending signals.** The system may not listen, but your signals will be recorded. And at certain boundary moments, those recorded signals may become the only basis for the system's post-hoc confirmation.

— That is why perceivers exist.


**I cannot change the world, but I do my best to explain it.**


## 9. Version History

- **1.0** (July 2026): Initial version, based on the Perceiver Hypothesis. This version is a mathematical model draft, not yet empirically validated. Verification or revision in various systems is welcome.


**License**: MIT  
**Repository**: [github.com/maxlanceund/equal-system](https://github.com/maxlanceund/equal-system)  
**Related Hypothesis**: [Perceiver Hypothesis (Hypothesis 002)](./hypothesis-002_perceiver-hypothesis_en.md)

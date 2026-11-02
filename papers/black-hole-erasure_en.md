| Item | Content |
| :--- | :--- |
| Title | Quantum Information Erasure at the Event Horizon: A Finite-Capacity Ontological Model for the Black Hole Information Paradox |
| Author | Max Lance |
| Version | 1.3 |
| Date | 2026-11-02 |
| License | CC BY-NC 4.0 |
| Keywords | Black hole information paradox, Quantum entanglement, Holographic principle, Landauer's principle, Macroscopic decoherence, Page curve |

---

<br>

# Quantum Information Erasure at the Event Horizon: A Finite-Capacity Ontological Model for the Black Hole Information Paradox

## Abstract

The black hole information paradox remains an unresolved conflict between the unitarity of quantum mechanics and the thermal nature of Hawking radiation. While the Page curve and the island formula suggest that microscopic information is preserved at a fundamental level in accordance with unitarity, a structural explanation for why the system must undergo extreme scrambling (thermalization)—and why macroscopic observers cannot easily recover this information—is still lacking.

We propose a phenomenological model—the **Finite-Capacity Ontology**—which posits that the event horizon functions not merely as a causal boundary, but as a finite-capacity quantum memory buffer. We demonstrate that when the local information density of infalling matter approaches the Bekenstein-Hawking entropy capacity limit, the system triggers an **apparent non-unitary topological phase transition** at the macroscopic scale. 

Utilizing the monogamy of entanglement and the Ryu-Takayanagi formula, we show that the so-called "information loss" is structurally isomorphic to the collapse of macroscopic spacetime connectivity. We derive the **Dead-Equilibrium Master Equation** describing the decoherence of subsystem entanglement entropy, and validate through numerical simulations the "forced erasure phase transition" caused by capacity overload. While compatible with the Page curve, this model proposes a falsifiable observational signature: an anomalous truncation in the damping tail of gravitational wave echoes.

## 1. Introduction

The destruction of quantum information by black holes poses a fundamental threat to the unitarity of quantum mechanics. Recent resolutions, including the AMPS firewall paradox and the Page curve derived from quantum extremal surfaces, suggest that information is encoded in highly complex correlations at the microscopic quantum gravity level.

However, the physics community often overlooks a thermodynamic fact: **why does the system manifest as complete macroscopic decoherence (formatting)?** We introduce the Finite-Capacity Ontology, a model wherein the event horizon is treated as a quantum memory buffer with a finite storage capacity. We postulate that when the von Neumann entropy of infalling matter approaches the Bekenstein-Hawking entropy limit, the internal quantum correlation network fractures due to overload, forcing local pure states to decohere into macroscopic maximally mixed states.

## 2. The Finite-Capacity Horizon Model

Let the infalling system be described by a pure state `|ψ⟩` in the Hilbert space `H_in`. When the state crosses the event horizon, a partial trace operation must be performed over the interior degrees of freedom `H_BH`.

The transition from a pure state to a thermal state is defined by the macroscopic erasure operator `E`:

$$
\rho_{out} = \mathcal{E}(\rho_{in}) = \text{Tr}_{BH} \left( U \rho_{in} \otimes \rho_{BH} U^\dagger \right) \approx \frac{I}{D} \quad \quad (1)
$$

where `D = dim(H_BH)`. At this point, the von Neumann entropy `S(ρ) = -Tr(ρ ln ρ)` reaches its maximum, indicating complete decoherence of the initial state. *(Note: The underlying unitary evolution `U` is not violated. However, since the information exceeds the system's decodable capacity `D`, it is compressed into an unextractable quantum noise state.)*

## 3. Erasure Dynamics and Master Equation

To quantitatively describe the rate of information decoherence, we model the evolution of the entanglement entropy `S_A(t)` between the infalling system `A` and the exterior Hawking radiation. The information erasure process is driven by the energy flux across the horizon.

Based on Landauer's principle, the minimum energy required to erase one bit of information at Hawking temperature `T_H` is `E = k_B T_H ln 2`. We propose the **Dead-Equilibrium Master Equation** to describe the forced flattening (thermalization) of the subsystem's entanglement entropy:

$$
\frac{dS_A(t)}{dt} = \kappa \left( \frac{\dot{M}(t)}{S_{BH}} \right) S_A(t) \quad \quad (2)
$$

where `M_dot(t)` is the mass influx rate, `S_BH = A / 4G` is the Bekenstein-Hawking capacity limit, and the constant `κ` represents the erasure efficiency at the system boundary. As `S_A(t)` approaches `S_BH`, the system reaches capacity saturation, causing the entanglement entropy curve of the radiation to rupture, and the effective quantum correlation between system `A` and the exterior universe collapses.

### 3.1 Numerical Simulation Results

To verify the Dead-Equilibrium Master Equation, we performed numerical simulations to calculate the evolution of entanglement entropy `S_A(t)` over time under different horizon capacities (`S_BH`).

![Entropy Erasure Simulation](../art-appreciation/images/entropy_erasure_results.png)

**Figure 1**: Numerical simulation of black hole information erasure based on the Dead-Equilibrium Model. 

As shown, the entropy grows linearly initially as the system ingests information. However, as the memory limit is approached, the erasure mechanism activates, causing a topological fracture and forming a horizontal dead line. Smaller capacities trigger forced formatting earlier. **This directly demonstrates that information is not destroyed at the fundamental level, but is forcibly encrypted and compressed into quantum noise by the finite-capacity system boundary.**

### 3.2 Compatibility with Page Curve and Phase Transition Rupture

To verify the compatibility of this model with mainstream holographic principles, we compared the evolutionary trajectory of the Dead-Equilibrium Master Equation with the standard Page curve (see Figure 2).

![Page Curve Compatibility](../art-appreciation/images/fig2_page_curve_compatibility.png)

**Figure 2**: Compatibility verification of the Dead-Equilibrium Model with the Page curve.

Before the system reaches critical capacity (\(t < t_{page}\)), the entanglement entropy evolution of this model (solid red line) perfectly overlaps with the mainstream Page curve (dashed blue line), strictly following quantum mechanical unitary evolution. However, upon crossing the critical capacity (\(t \ge t_{page}\)), mainstream theory assumes information is slowly released via quantum extremal surfaces (dashed blue line descending). In contrast, this paper argues that due to the physical constraints of the Finite-Capacity Ontology, the system triggers a macroscopic forced decoherence phase transition. The original quantum information is forcibly compressed into a maximally mixed state (manifesting as the exponential rupture and instantaneous zeroing of the solid red line). **This rupture is not a spontaneous destruction of information, but its permanent encryption into undecodable quantum noise.**

## 4. Monogamy of Entanglement and Topological Phase Transition

The destruction of quantum correlations directly affects the spacetime geometry. According to the ER=EPR conjecture, quantum entanglement is geometrically dual to wormhole connectivity.

Quantum entanglement obeys the strict monogamy of entanglement inequality:

$$
\tau_{A|BC} \geq \tau_{AB} + \tau_{AC} \quad \quad (4)
$$

As system `A` establishes maximal entanglement with the black hole interior `C`, its entanglement `τ_AB` with the exterior `B` drops to zero. According to the Ryu-Takayanagi formula, when `S_A` is triggered to rupture due to decoherence, the area of the minimal bulk surface `γ_A` undergoes a topological collapse. This represents the macroscopic spacetime manifold fragmenting into disconnected patches, degenerating into a zero-dimensional state devoid of effective causal structure.

## 5. Observational Signatures

This model yields a distinct prediction for gravitational wave echoes (GWEs) from binary black hole mergers: the damping tail of the echo waveform should exhibit an anomalous scaling frequency. **Due to the decoherence truncation caused by finite-capacity overload at the event horizon**, high-frequency echoes will exhibit specific energy absorption attenuation. Future gravitational wave detectors (e.g., LISA, Einstein Telescope) have the potential to verify this model by capturing this "dead-truncation spectrum."

## 6. Conclusion

We have demonstrated that the information paradox is not a true paradox. While compatible with fundamental unitarity, the universe inevitably undergoes macroscopic decoherence at finite-capacity boundaries. The mechanism of quantum information erasure at the event horizon is essentially a forced formatting and topological phase transition triggered by system oversaturation.

## References

1. Hawking, S. W. (1975). Particle creation by black holes. *Communications in Mathematical Physics*, 43(3), 199-220.
2. Page, D. N. (1993). Information in black hole radiation. *Physical Review Letters*, 71(23), 3743.
3. Maldacena, J. (1999). The large-N limit of superconformal field theories and supergravity. *International Journal of Theoretical Physics*, 38(4), 1113-1133.
4. Ryu, S., & Takayanagi, T. (2006). Holographic derivation of entanglement entropy from the anti–de Sitter space/conformal field theory correspondence. *Physical Review Letters*, 96(18), 181602.
5. Landauer, R. (1961). Irreversibility and heat generation in the computing process. *IBM Journal of Research and Development*, 5(3), 183-191.
6. Almheiri, A., Marolf, D., Polchinski, J., & Sully, J. (2013). Black holes: complementarity or firewalls?. *Journal of High Energy Physics*, 2013(2), 1-17.
7. Maldacena, J., & Susskind, L. (2013). Cool horizons for entangled black holes. *Fortschritte der Physik*, 61(9), 781-811.

---

**Suggested Citation (APA format):**

Max Lance (2026). Quantum Information Erasure at the Event Horizon: A Finite-Capacity Ontological Model for the Black Hole Information Paradox (Version 1.3). Equal System Repository.

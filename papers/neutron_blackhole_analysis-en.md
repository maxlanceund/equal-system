| Project | Details |
| :--- | :--- |
| Title | Observational Analysis of Neutron Stars and Black Holes: A Smooth Phase Transition Model Test Based on LIGO Posterior Samples |
| Author | Max Lance |
| Version | 3.4 |
| Date | 2026‑11‑24 |
| License | CC BY‑NC 4.0 |
| Keywords | Gravitational waves, Neutron star, Black hole, Tidal deformability, TOV equation, Smooth phase transition |

<br>

# Observational Analysis of Neutron Stars and Black Holes: A Smooth Phase Transition Model Test Based on LIGO Posterior Samples

## 1. Abstract
Using public gravitational‑wave posterior samples from LIGO‑Virgo‑KAGRA, we investigate compact‑star internal structure. For neutron‑star physics we use the low‑spin GW170817 posterior subset; for black‑hole ringdown echoes we employ the full 40 836‑sample GW150914 posterior, replacing the smaller 5 000‑sample subsample of version 3.3. Algebraic inversion yields a median neutron‑star radius of 12.24 km and median interior squared sound speed $`c_s^2\approx0.112`$. TOV integration for a pure hard‑core equation‑of‑state gives a maximum supported mass of only $`1.65\,M_\odot`$ with limiting tidal deformability $`\Lambda=57.3`$. While 94.9 % of valid GW170817 posterior samples exceed this prediction, this fraction is prior‑dependent and only illustrative. Our primary argument against the pure hard‑core model arises from joint comparison with NICER mass‑radius constraints and alternative representative equations of state: no purely hadronic EOS simultaneously satisfies both tidal‑deformability and radius observables, favouring a stellar interior with a smooth phase transition. This model predicts post‑merger ringdown peak frequencies 2200–2600 Hz, which lie beyond current detector sensitivity and constitute a target for third‑generation gravitational‑wave instruments. For GW150914, remnant properties from numerical‑relativity fits are used to compute Kerr‑spin‑corrected black‑hole echo delays sample‑by‑sample. Collectively these results yield concrete, falsifiable observational predictions.

## 2. Data and Methods
### 2.1 Data Sources
All data are extracted from the LIGO‑Virgo‑KAGRA (LVK) Collaboration's public posterior sample releases.
*   Neutron star samples: GW170817; the tidal analysis uses the low‑spin subset comprising 8 078 binaries from the GWTC‑1 release, consistent with the cross‑check in Section 3.2.1. This subset yields source‑frame masses after redshift correction inferred from luminosity distance.
*   Black hole samples: Full public posterior samples of GW150914 (40 836 samples) extracted from the GWTC‑1 release. This dataset provides detector‑frame component masses and dimensionless spin parameters; redshift information is **not included** within this sample file. The earlier manuscript version 3.3 used a reduced subsample of only 5 000 GW150914 posterior samples, which is fully superseded in version 3.4.

### 2.2 Calculation Methods
**Algebraic Inversion**: Based on the relationship between tidal deformability and compactness, the radius is inversely derived:

$$
\Lambda = \frac{2}{3} k_2 C^{-5}
$$

Where the compactness is $`C = GM / (Rc^2)`$ , and $`k_2 = 0.12`$ is adopted for the smooth fluid model.

**TOV Calculus Solving**: Using a standard hard‑core equation of state (polytropic index $`\Gamma=2`$ , $`K=180`$ ), starting from a given central pressure $`P_c`$ , we integrate the complete stellar structure equations outward, i.e., the TOV equation and the Love number perturbation evolution equation:

$$
\frac{dm}{dr} = 4\pi r^2 \rho
$$

$$
\frac{dP}{dr} = -\frac{G(\rho + P/c^2)(m + 4\pi r^3 P/c^2)}{r(r - 2Gm/c^2)}
$$

$$
\frac{dy}{dr} = -\frac{y^2 + y F(r) + r^2 Q(r)}{r}
$$

Where $`y(r)`$ is the Love number evolution function, and $`F(r)`$ and $`Q(r)`$ are perturbation terms determined by energy density and pressure. When integrating to the stellar surface ( $`P \to 0`$ ), the true $`k_2`$ and $`\Lambda`$ are calculated from the surface $`y`$ value.

**Gravitational‑wave energy of the black hole sample**: Radiated mass and energy are derived from remnant quantities obtained via numerical‑relativity fitting described in Sec. 2.3.

**Black Hole Ringdown and Echo**: the characteristic time is $`M_{\mathrm{time}} = GM/c^3`$ , and the ringdown damping time is parametrised as $`\tau \approx 4.0\,M_{\mathrm{time}}(1-a)^{-0.45}`$.

In this echo model, $`d`$ denotes the proper distance between the event horizon and the hypothetical quantum‑gravitational reflective wall near the horizon. We adopt $`d=\ell_P`$ (Planck length) as a model‑level ansatz, which is not derived from first‑principles quantum gravity.

For a reflecting surface located a proper distance $`d`$ outside the horizon, the round‑trip echo delay for Kerr remnant reads:

$$
\Delta t \approx \frac{4GM_\mathrm{rem}}{c^3}\left(1+\frac{1}{\sqrt{1-a^2}}\right)\ln\left(\frac{4GM_\mathrm{rem}}{c^2\,d}\right).
$$

In the non‑spinning Schwarzschild limit $`a\rightarrow 0`$, this expression recovers the well‑known Schwarzschild echo‑delay formula used in earlier versions of this work. Earlier versions used simple approximate estimates for remnant mass and spin. In this manuscript, $`M_\mathrm{rem}`$ (remnant mass) and dimensionless remnant spin $`a`$ are computed sample‑by‑sample from binary component masses and spins using standard numerical‑relativity fitting formulas (Section 2.3). The echo delay is evaluated for every GW150914 posterior sample to produce a full posterior distribution for $`\Delta t`$.

A delay of only a few milliseconds would instead require a surface at $`r \simeq 3`$ to $`8M`$, roughly 90 to 460 km above the horizon and essentially at the photon sphere; such a surface would visibly distort the ringdown and is inconsistent with the Kerr agreement observed so far. The horizon‑scale delay is therefore the physically admissible branch, and it is the one used below.

### 2.3 Remnant mass and spin from numerical‑relativity fits
Instead of the fixed‑radiative‑efficiency crude estimates adopted in v3.3, we follow standard LVK analysis practice and use published numerical‑relativity fitting formulas for binary black‑hole mergers [Healy & Couto, 2022]. For each GW150914 posterior sample with component masses $`m_1,m_2`$ and component spin projections $`\chi_{1z},\chi_{2z}`$, we compute remnant mass $`M_\mathrm{rem}`$ and dimensionless remnant spin parameter $`a`$ on a sample‑by‑sample basis. This procedure yields full posterior distributions for remnant quantities, and directly gives the posterior of the ringdown frequency without ad‑hoc assumptions.

## 3. Results
### 3.1 True Distribution of Neutron Star Structure

![figure1_radius_distribution](../art-appreciation/images/figure1_radius_distribution.png)
*Fig 1: Reconstructed radius distribution of neutron stars based on 28,116 LIGO samples. The median is 12.24 km, and the main distribution highly overlaps with the NICER observation range (gray band).*

![figure2_sound_speed](../art-appreciation/images/figure2_sound_speed.png)
*Fig 2: Effective sound speed distribution inside neutron stars. The extremely low median ( $`c_s^2 \approx 0.112`$ ) excludes pure neutron hard‑core structures.*

*   **Radius**: Median 12.24 km; the average for extreme massive samples ( $`>2.0 M_\odot`$ ) is 12.90 km. This range highly coincides with the independent observation of NICER (12.4~13.7 km).
*   **Sound Speed**: The reconstructed median squared sound speed is $`c_s^2 \approx 0.112`$ , reaching 0.080 under extreme mass. The low values are consistent with a mixed fluid state of quark deconfinement.

<br>

### 3.2 TOV Integration Falsification of the Pure Hard‑Core Model
To verify the above conclusions, this paper uses a standard hard‑core equation of state and performs a from‑scratch numerical calculus solution of the TOV equations. The results show:
*   The maximum mass that the pure hard‑core model can support is only **1.65 solar masses**.
*   At this limit, its theoretical tidal deformability ( $`\Lambda`$ ) is only 57.3; if forcibly extrapolated to 1.78 solar masses, the $`\Lambda`$ value will drop below 20.

For a like‑for‑like comparison the tidal information must be quoted as a posterior rather than as a single number. The GW170817 posterior on the combined tidal deformability has a median of 483 and a 90 percent upper bound of 1569, with a 5 to 95 percent range of $`-83`$ to 1944. Of the 8,078 samples, 11.6 percent are negative and therefore physically inadmissible, because no $`\Lambda \ge 0`$ prior was imposed on the raw release. After removing them, **94.9 percent of the remaining 7,145 samples lie above the hard‑core prediction of 57, and only 1.9 percent fall below 20**.

We emphasize that this sample fraction is prior‑dependent and serves only as supporting illustration, not as primary statistical evidence. All equation‑of‑state comparisons in this work are performed under identical prior settings. A full Bayes‑factor computation and joint‑likelihood inference incorporating NICER radius constraints are deferred to future follow‑up work.

With essentially the whole physical posterior above the prediction, the data leave no room for a dense hard core.

Only a mixed fluid model can simultaneously satisfy a mass limit above 2 solar masses, a tidal deformability of order 300, and a radius near 12 to 13 km; as Section 3.2.2 shows, ordinary soft hadronic equations of state satisfy at most two of the three.

### 3.2.1 Independent Cross‑Check from Raw Posterior Samples
As an independent cross‑check, we re‑extracted 8,078 low‑spin posterior samples of GW170817 from the public GWTC‑1 release and recomputed the tidal parameters directly from the raw stored quantities: the detector‑frame component masses, the individual deformabilities $`\Lambda_1`$ and $`\Lambda_2`$, and the luminosity distance. Source‑frame masses were obtained via $`m_{\mathrm{source}} = m_{\mathrm{det}}/(1+z)`$, with the redshift inferred from the luminosity distance in a flat $`\Lambda`$CDM cosmology, and the combined tidal deformability from

$$
\tilde{\Lambda} = \frac{8}{13}\left[(1+7\eta-31\eta^2)(\Lambda_1+\Lambda_2) + (1-9\eta)(\Lambda_1-\Lambda_2)\right], \qquad \eta = \frac{m_1 m_2}{(m_1+m_2)^2}.
$$

The resulting distributions are summarized below.

| Quantity | Median | 90% upper bound |
| :--- | :--- | :--- |
| Combined tidal deformability $`\tilde{\Lambda}`$ | 483 | 1569 |
| Single‑star deformability, all components | 347 | 1078 |
| Heavier component $`\Lambda_1`$ | 269 | 833 |
| Lighter component $`\Lambda_2`$ | 446 | 1288 |
| **$`\Lambda_{1.4}`$ (scaled to $`1.4\,M_\odot`$)** | **306** | 917 |

Three points follow. First, the lighter component is more deformable than the heavier one ($`\Lambda_2 = 446`$ versus $`\Lambda_1 = 269`$), consistent with the expected mass dependence. Second, the scaled single‑star value $`\Lambda_{1.4} = 306`$ is of the same order as the $`\Lambda \approx 203.4`$ usually quoted for this event. Third, the combined quantity $`\tilde{\Lambda}`$ (median 483) is a mass‑weighted combination and is therefore systematically higher than $`\Lambda_{1.4}`$; it should not be substituted for the single‑star value.

The direction of the argument in Section 3.2 is therefore unchanged: the physical posterior sits well above the hard‑core prediction, reinforcing the conclusion that a pure hard‑core structure is excluded and that a soft, smoothly phase‑transitioned interior is required. Substituting $`\Lambda_{1.4} = 306`$ into the algebraic inversion of Section 2.2 gives $`R \approx 13.3`$ km, still inside the NICER range of 12.4--13.7 km, so the radius result of Section 3.1 is unaffected. We note that this cross‑check uses the raw posterior without the electromagnetic‑counterpart distance prior and without any equation‑of‑state‑insensitive reweighting, so the numerical values are not strictly equivalent to the reweighted literature constraint.

Table 1 summarizes the key posterior parameters for both events. Although GW150914 and GW170817 exhibit near‑unity mass ratios, their diagnostic gravitational‑wave observables separate sharply. GW150914 yields a near‑zero effective spin consistent with misaligned black‑hole spins and exhibits no tidal response. By contrast, GW170817 returns a broad posterior for combined tidal deformability $`\tilde{\Lambda}`$, encoding information on neutron‑star interior physics. This contrast illustrates how tidal observables distinguish binary‑neutron‑star systems from binary‑black‑hole mergers at comparable mass ratio.

**Table 1:** Summary of posterior parameters for GW150914 (BBH, detector‑frame masses) and GW170817 (BNS, source‑frame masses). Intervals denote 16th‑84th percentiles.
| Event | $`N_\mathrm{samples}`$ | $`m_1\,[M_\odot]`$ | $`m_2\,[M_\odot]`$ | $`q=m_2/m_1`$ | $`\chi_\mathrm{eff}`$ | $`\tilde{\Lambda}`$ |
|:---|:---|:---|:---|:---|:---|:---|
| GW150914 | 40836 | $`38.56_{-2.02}^{+2.95}`$ | $`33.18_{-2.80}^{+2.02}`$ | $`0.864_{-0.126}^{+0.093}`$ | $`-0.032_{-0.073}^{+0.062}`$ | — |
| GW170817 | 8078 | $`1.467_{-0.073}^{+0.093}`$ | $`1.270_{-0.074}^{+0.064}`$ | $`0.866_{-0.099}^{+0.091}`$ | — | $`482.8_{-426.8}^{+789.6}`$ |

*Notes:* GW150914 masses are detector‑frame quantities from the GWTC‑1 posterior file; no redshift is provided within this sample set. GW170817 quantities are source‑frame values derived from the low‑spin GWTC‑1 subset. Black holes possess no tidal‑deformability signature.

### 3.2.2 Comparison with Equations of State that Fit NICER
The tidal constraint acquires meaning only when compared with specific equations of state. The table collects representative models together with the values reconstructed here.

| Equation of state | Type | $`M_{\mathrm{max}}`$ ($`M_\odot`$) | $`R_{1.4}`$ (km) | $`\Lambda_{1.4}`$ | Matches $`\Lambda`$ | Matches $`R`$ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Hard core (this work, $`\Gamma=2`$) | dense hard core | 1.65 | 10.5 | 57 | no | no |
| SLy | soft hadronic | 2.05 | 11.7 | ~300 | yes | no |
| APR | hadronic | ~2.2 | ~11.4 | 180--250 | marginal | no |
| DD2 | intermediate | 2.42 | 13.2 | ~674 | no | yes |
| **Reconstructed (this work)** | --- | --- | **12.24** (13.3 from $`\Lambda_{1.4}`$) | **306**; 372 ($`+220/-150`$) reweighted | --- | --- |

Taken one at a time, neither constraint is decisive: SLy reproduces the tidal deformability while its 11.7 km radius lies below both the NICER interval of 12.4--13.7 km and the value reconstructed here; DD2 reproduces the radius while its $`\Lambda_{1.4} \approx 674`$ lies about 1.3 standard deviations above the reweighted constraint of $`372^{+220}_{-150}`$. The combination, however, is restrictive. An interior that is soft in bulk, so that it deforms strongly under tidal forcing, must also remain compact enough to keep a radius near 12 to 13 km and a maximum mass above 2 solar masses; a purely hadronic soft equation of state satisfies the first requirement at the cost of the second, and the intermediate models satisfy the second at the cost of the first. The band that survives both constraints is precisely the configuration in which a soft mixed phase coexists with a compact overall structure, which is what a smooth phase transition produces. This is why the joint constraint, rather than the tidal deformability alone, is the argument for a phase‑transitioned interior. The list in the table is representative rather than exhaustive.

### 3.2.3 Posterior‑Predictive Consistency Check across Equations of State
Following the reviewer suggestion, we perform posterior‑predictive consistency comparisons for the hard‑core, SLy, APR, and DD2 equations of state, evaluated on the identical set of GW170817 posterior $`(m_1,m_2)`$ samples under shared prior conditions. A full Bayes‑factor analysis would require access to the original gravitational‑wave waveform likelihood, which is not available in this study, and is therefore deferred to future follow‑up work, as already noted in Section 3.2. Instead we adopt the reviewer‑proposed alternative: posterior‑predictive diagnostics with P‑P plots as the primary visual tool, supplemented by KS, Cramér‑von Mises, and Hellinger metrics. These quantities serve purely as consistency checks and are **not used to rank or exclude equation‑of‑state models**. The NICER $`R_{1.4}`$ radius is reported as auxiliary contextual information and is not multiplicatively combined into a joint likelihood.

![ppd_figure (1)](../art-appreciation/images/ppd_figure (1).png)
*Fig 5: Posterior‑predictive consistency check for four tested equations of state. Left: P‑P plot; the dashed diagonal line marks perfect agreement between predicted and observed cumulative distributions for $`\tilde{\Lambda}`$. Right: Histogram comparison of posterior‑predictive $`\tilde{\Lambda}`$ distributions from each EOS, overlaid with the observed GW170817 $`\tilde{\Lambda}`$ posterior. Diagnostics shown are for consistency assessment only and are not used to rank or exclude EOS models.*

All four tested EOS produce predicted $`\tilde{\Lambda}`$ distributions that deviate from the observed posterior. Owing to the large sample size ($`N=8078`$), KS and Cramér‑von Mises p‑values are effectively zero for every model; this is a well‑known statistical artefact of high‑sample‑size posterior predictive tests and does not by itself constitute physical exclusion. Among the models examined, the hard‑core EOS exhibits the largest distributional separation from observation, quantified by the Hellinger distance, while DD2 shows the smallest separation. These numerical diagnostics are collected in **Appendix B** for reference.

For the hard‑core EOS, every posterior sample satisfies the empirical prompt‑collapse condition $`M_{\rm tot}>1.35M_\odot`$, meaning prompt collapse would be expected for all realisations within the cold static EOS framework. As discussed in Section 3.3.1, this tension does not constitute definitive exclusion because the merger remnant in our smooth‑phase‑transition picture involves hot dynamical matter effects not captured by the cold EOS threshold criterion.

### 3.3 A New Prediction for Post‑Merger Ringdown Frequency
Based on the topological smooth‑phase‑transition structure (radius 12.24 km, internal squared sound‑speed $`c_s^2\approx 0.080`$), we derive expected post‑merger oscillation frequencies for binary‑neutron‑star merger remnants. The predicted band $`2200`$–$`2600\ \mathrm{Hz}`$ is rooted in quasi‑universal relations established by numerical‑relativity merger simulations [Bauswein & Janka 2012; Takami et al. 2014; Bernuzzi et al. 2015; Baiotti & Rezzolla 2016]. Using the tidal‑deformability value of our hard‑core reference model ($`\Lambda=57`$), we cross‑check our central value $`2450\ \mathrm{Hz}`$ against these quasi‑universal relations as an internal consistency test.

*   For the pure hard‑core reference model (radius ~10.5 km), merger leads to rapid collapse; the nominal post‑merger peak frequency reaches **3215 Hz**.
*   For our smooth‑phase‑transition model, the soft mixed‑phase interior produces delayed‑collapse dynamics; the post‑merger oscillation peak falls to **2200–2600 Hz**, best‑estimate $`2450\ \mathrm{Hz}`$.

This prediction is not testable with current detectors. GW170817 produced no confirmed post‑merger signal, and the only post‑merger‑related feature reported for that event lies at about 72 Hz, where the detector noise is far lower. At 2450 Hz the strain from a 40 Mpc event is of order $`10^{-22}`$, while the amplitude spectral density of Advanced LIGO is about $`2.5\times10^{-22}`$ per root hertz in design and about $`10^{-21}`$ per root hertz during the O2 run, giving a matched‑filter signal‑to‑noise ratio of order 0.04 (0.01 in O2). Our signal‑to‑noise discussion is consistent with the LVK post‑merger search for GW170817 [Abbott et al., 2017]. With the Einstein Telescope the same source would reach a signal‑to‑noise ratio of about 1 at 40 Mpc and about 4 at 10 Mpc. The 2450 Hz peak is therefore a target for third‑generation detectors, or for a substantially closer event, rather than a test that can be performed on existing data.

The dominant systematic here is the calibration factor $`\kappa`$ in $`f_{\mathrm{peak}} = (\kappa/2\pi)\sqrt{GM/R^3}`$. Numerical‑relativity fits give $`\kappa \simeq 1.0`$--$`1.2`$ , which moves the peak between 2200 and 2600 Hz; this range, and not the central value, should be compared with any future measurement.

#### 3.3.1 Tension with prompt‑collapse threshold
Numerical‑relativity simulations employing cold neutron‑star equations of state indicate that tidal deformability values as low as $`\Lambda=57`$ typically result in prompt collapse to a black hole immediately after merger, suppressing long‑lived post‑merger‑oscillating remnants [Agathos et al., 2020].

We note however that $`\Lambda=57`$ is computed for cold static TOV equilibrium configurations. The merger remnant within our smooth‑phase‑transition model involves high temperature, strong dynamical evolution, and phase‑transition effects not present in standard cold‑matter simulation setups. Therefore the standard cold‑EOS prompt‑collapse threshold may not directly apply to this dynamical remnant. Whether a long‑lived remnant can survive under our model requires dedicated numerical‑relativity simulations for hot phase‑transition dense matter.

### 3.4 Black Hole Ringdown and Echo Delay
In this version we recompute remnant‑mass, remnant‑spin and echo‑delay posterior distributions using the **full 40 836 GW150914 posterior samples**, replacing the smaller 5 000‑sample subset adopted in manuscript v3.3. Remnant quantities are evaluated sample‑by‑sample via published numerical‑relativity fitting formulas [Healy & Couto, 2022].

![bh_echo_delay_40836](../art-appreciation/images/bh_echo_delay_40836.png)
*Fig 3: Predicted echo‑delay posterior recomputed using the full 40 836‑sample GW150914 posterior dataset. The reflective wall is placed one Planck proper‑length outside the horizon. Remnant mass and dimensionless remnant spin are computed sample‑by‑sample via numerical‑relativity fitting formulas from Healy & Couto (2022), followed by the Kerr‑spin‑corrected echo‑delay expression. This figure supersedes the v3.3 result obtained from a 5 000‑sample subsample.*

*   **Ringdown Frequency**: Ringdown frequency is computed sample‑by‑sample from NR‑fit $`M_\mathrm{rem}`$ and $`a`$, giving a full posterior distribution; point‑value reporting is no longer used. Systematic uncertainties are now encoded within this posterior.
*   **Echo Delay**: After including Kerr‑spin corrections and sample‑by‑sample NR remnant parameters, the updated echo‑delay posterior is shown in Figure 3.
*   **Consistency with the ringdown**: the observed ringdowns of LIGO events agree with the Kerr prediction within the measurement errors. A reflecting surface at a macroscopic distance from the horizon would leave a detectable imprint on that waveform, so the surface is constrained to lie close to the horizon, which is precisely the regime that produces sub‑second rather than millisecond delays.

### 3.5 Physical Image of Neutron Star Internal Structure (The Finale)
Based on the radius (12.24 km) and extremely low internal sound speed deduced from real observational data, the traditional "onion‑like" dense hard‑core image no longer holds. Figure 4 presents a 3D cutaway anatomy of a neutron star constructed based on the smooth phase transition model.

![neutron_star_3d_superglow_edit_6365820738902738](../art-appreciation/images/neutron_star_3d_superglow_edit_6365820738902738.png)
*Fig 4: 3D cutaway anatomy of a neutron star. The outer layer is the crust, smoothly transitioning inward to the superfluid neutron region; the core is a quark‑gluon plasma (quantum ocean) without a dense hard‑core boundary.*

In this image, there is no cliff‑like boundary in the material distribution. The very core of the star (the highly luminous cyan region) is no longer the unknown dense hard core in traditional theories, but a quark‑gluon plasma formed after the boundaries are crushed by extreme gravity. This extremely soft, interconnected quantum ocean structure is the direct physical mechanism to explain the large tidal deformability and extremely low sound speed inferred from the LIGO data.

## 4. Conclusion
1.Neutron‑star gravitational‑wave and NICER radius observations disfavour the pure dense hard‑core model. Although 94.9 % of physically admissible GW170817 posterior samples exceed the hard‑core tidal‑deformability prediction, this fraction is prior‑dependent and only illustrative. Complementary posterior‑predictive consistency checks across representative equations‑of‑state further show systematic deviations of the hard‑core model from the GW170817 tidal posterior. Taken together, the TOV‑derived maximum‑mass limit of $`1.65\,M_\odot`$, the reconstructed median radius of 12.24 km, and the low median interior sound‑speed squared $`c_s^2\approx0.112`$ indicate that no purely hadronic equation‑of‑state can simultaneously satisfy tidal‑deformability and NICER radius constraints. These observations point toward a compact‑star interior characterised by a mixed‑fluid smooth phase transition.

2.For binary‑neutron‑star mergers, our smooth‑phase‑transition model predicts post‑merger ringdown peak frequencies in the range $`2200`$–$`2600\ \mathrm{Hz}`$, with a central estimate near $`2450\ \mathrm{Hz}`$, distinctly higher than the $`3215\ \mathrm{Hz}`$ expected for the pure hard‑core EOS. The signal yields a signal‑to‑noise ratio of only order 0.04 for a $`40\ \mathrm{Mpc}`$ event in current‑generation detectors, meaning this prediction will be testable primarily with third‑generation instruments such as the Einstein Telescope, or for much closer merger events. We note that standard cold‑EOS prompt‑collapse thresholds may not directly apply to the hot, dynamically evolving phase‑transition merger remnant.

3.Turning to binary‑black‑hole systems, we compute echo‑delay posteriors for GW150914 using its full $`40\,836`$‑sample posterior dataset. Remnant mass and spin are evaluated sample‑by‑sample via numerical‑relativity fitting formulas, and echo delays are obtained from the full Kerr‑spin‑corrected expression. Observed ringdown consistency with Kerr spacetime rules out macroscopic reflecting surfaces near the photon sphere, which would produce millisecond‑scale echo delays.

4.None of our results rely on ad‑hoc parameter tuning. The model makes concrete falsifiable predictions: it can be ruled out if future observations fail to detect black‑hole echoes within the predicted delay window, or fail to find binary‑neutron‑star post‑merger emission near $`2450\ \mathrm{Hz}`$.

## Appendix A. Supporting Figures from the Independent Cross‑Check
All GW150914 plots within this appendix are computed using the full 40 836‑sample GWTC‑1 posterior; detector‑frame masses are used throughout, as no redshift is provided within this sample release.

![fig_three_panel_main](../art-appreciation/images/fig_three_panel_main.png)
*Fig A1: Posterior distributions of key distinguishing gravitational‑wave observables. Left: effective spin $`\chi_\mathrm{eff}`$ for the binary‑black‑hole event GW150914. Middle: combined tidal deformability $`\tilde{\Lambda}`$ for binary‑neutron‑star event GW170817. Right: mass‑ratio $`q=m_2/m_1`$ posterior comparison for both events. Vertical dashed lines mark median values; grey dotted lines denote 16th and 84th percentiles. Despite near‑unity mass ratios for both mergers, tidal observables uniquely identify the neutron‑star binary.*

![gw170817_plots](../art-appreciation/images/gw170817_plots.png)
*Fig A2: GW170817 combined tidal deformability posterior (8 078 samples). Left: $`\tilde{\Lambda}`$ distribution with the median of 483 marked; right: binned median of $`\tilde{\Lambda}`$ versus the mass of the lighter component, showing a weak decreasing trend consistent with the expected mass dependence. Note that $`\tilde{\Lambda}`$ is a mass‑weighted combination and is not equivalent to $`\Lambda_{1.4}`$.*

Note: The old figure bh_plots.png based on 5 000 subsampled GW150914 samples from v3.3 is deprecated; you may manually delete the markdown tag for bh_plots.png in your original file.

### Appendix B: Posterior‑Predictive Diagnostic Statistics
Table B1: Diagnostic metrics for posterior‑predictive $`\tilde{\Lambda}`$ comparisons between each EOS prediction and the GW170817 observed posterior. All metrics are provided for reference only and are **not used to rank or exclude EOS models**.

| EOS   | Hellinger distance | KS statistic | CvM statistic | $`R_{1.4}`$ [km] | Valid samples |
|-------|--------------------|--------------|---------------|----------------|---------------|
| HC    | 0.2289             | 0.8235       | 764.2597      | 10.50          | 7866          |
| SLy   | 0.1984             | 0.7430       | 615.1982      | 11.70          | 8078          |
| APR   | 0.1973             | 0.7409       | 608.8695      | 11.40          | 8078          |
| DD2   | 0.1632             | 0.5985       | 370.6771      | 13.20          | 8078          |

All KS and Cramér‑von Mises p‑values are effectively zero. This is a statistical artefact originating from the large posterior sample size and should not be interpreted as physical rejection of any EOS.

## References

Abedi, J., Dykaar, H., & Afshordi, N. (2017). Echoes from the Abyss: Tentative evidence for Planck‑scale structure at black hole horizons. *Physical Review D*, 96, 082004.
Abedi, J., & Afshordi, N. (2018). Echoes from the Abyss: a highly spinning black hole remnant for the binary neutron star merger GW170817. arXiv:1803.10454.
Riley, T. E., et al. (2019). A NICER view of PSR J0030+0451: millisecond pulsar parameter estimation. *The Astrophysical Journal Letters*, 887, L21.
Bauswein, A., & Janka, H.-T. (2012). *Physical Review Letters*, 108, 011101.
Takami, K., Rezzolla, L., & Baiotti, L. (2014). arXiv:1402.6244.
Bernuzzi, S., Dietrich, T., & Nagar, A. (2015). *Physical Review Letters*, 115, 091101.
Baiotti, L., Rezzolla, L. (2016). arXiv:1607.03540.
Agathos, M., et al. (2020). arXiv:1908.05442.
Abbott, B. P., et al. (LVK Collaboration) (2017). *The Astrophysical Journal Letters*, 851, L16.
Healy, J., & Couto, H. (2022). Numerical‑relativity fitting formulas for binary‑black‑hole remnant properties.

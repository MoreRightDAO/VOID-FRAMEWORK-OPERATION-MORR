---
title: "Navier-Stokes Blow-Up as Finite-Time Péclet Concentration: Cascade Directionality, the L²/L∞ Gap, and Dimension Dependence"
author: "Anthony Eckert"
orcid: "0009-0008-1925-5253"
affiliation: "Independent Researcher, MoreRight DAO"
paper-number: "Paper 137"
short-title: "NS Blow-Up as Pe Concentration"
version: "v2.0"
date: "2026-03-10"
license: "cc-by-4.0"
---

## Void Model Card

| Field | Value |
|-------|-------|
| **Paper** | 137 — NS Blow-Up as Pe Concentration |
| **Domain** | Fluid dynamics / Partial differential equations / Turbulence theory |
| **Pe estimate** | Pe(ℓ) = δu(ℓ)·ℓ/ν; blow-up ⟺ sup_x Pe(x,t) → ∞ in finite time |
| **Tier** | 1 — CC-BY 4.0 |
| **Core claim** | The Navier-Stokes blow-up question is natively a Pe field concentration problem: blow-up occurs if and only if the local Pe supremum diverges in finite time (BKM). The 2D/3D regularity asymmetry is cascade directionality (inverse in 2D = Pe-constructive; forward in 3D = Pe-destructive possible via vortex stretching). The L²/L∞ gap is the distributed-Pe / pointwise-Pe gap. The −5/3 spectrum is the unique RG fixed point of the Pe field in wavenumber space. |
| **Novel contributions** | (1) Blow-up restated as finite-time Pe concentration; (2) 2D/3D asymmetry explained as Pe cascade directionality; (3) L²/L∞ gap identified as mean-field/exact-dynamics gap; (4) Prodi-Serrin ladder as Pe norm interpolation; (5) −5/3 derived from §49 RG fixed point; (6) She-Leveque intermittency as RG anomalous dimensions; (7) Gevrey radius σ/ν bounded on JHTDB DNS (HP134C/D/E) |
| **Builds on** | §49 (RG), §48E (Kramers escape), Papers 3, 109, 130, 133; K41, BKM (1984), CKN (1982), She-Leveque (1994) |
| **Key negatives** | BKT universality prediction K-NS-4 tested and NOT supported at Re_λ=433 (η=4/9 excluded at 18.4σ and 42.4σ). Pe multifractal spectrum (K-NS-7) is tautological — change of variables, not independent prediction. Sections XII–XVI are structural restatements, not new theorems. |

---

## Abstract

The Péclet number (Pe = UL/ν) was derived from the Navier-Stokes (NS) equations — it is not an analogy imported from another domain. This paper exploits that native relationship to restate the NS Millennium Problem with new precision. The Kolmogorov dissipation scale η is defined by Pe(η) ≈ 1 by construction: it is the scale at which advective and diffusive transport balance. The −5/3 energy spectrum is the equilibrium Pe gradient field across the inertial range — the profile that statistical stationarity imposes on the Pe distribution in wavenumber space. The blow-up question is therefore: *can Pe → ∞ concentrate at a point in finite time from smooth initial data?* This restatement has exact structural consequences. The dimension dependence of the NS regularity problem (2D: global regularity proven; 3D: open) is a **Pe cascade directionality** problem: in 2D the inverse enstrophy cascade is Pe-constructive at small scales (Pe accumulation is impossible), while in 3D vortex stretching can locally reverse the mean-field cascade and concentrate Pe upward at a point. The L²/L∞ gap — the core obstruction to all known energy-method proofs — is the gap between distributed-Pe control (L² norm, the cascade mean-field) and pointwise-Pe control (L∞ norm, the exact realization). The Prodi-Serrin regularity ladder is Pe norm interpolation: every rung below L∞ leaves the problem open because any finite-moment constraint on the Pe field distribution is insufficient to bound the local supremum. The Onsager exponent h = 1/3 is the mean-field Pe validity boundary in regularity space. These are not analogies. They are restatements of known mathematical facts in the language of Pe field dynamics, and each restatement generates a falsifiable prediction not visible from the classical formulation.

**v2.0 extension:** The −5/3 exponent is derived as the unique fixed point of the §49 RG applied to wavenumber space (not merely restated from K41). The Richardson cascade is identified as D3→D0 constraint reassertion — the NS equations' built-in mechanism for processing drift excess into diffusive dissipation. The She-Leveque (1994) intermittency corrections are identified as anomalous dimensions of the NS-Pe RG, structurally parallel to but distinct from the BKT corrections in §49. Velocity structure function exponents ζ_p are reformulated as Pe spectral moments σ_p = ζ_p + p, with the 4/5-law exactness of ζ_3 = 1 as a Pe conservation law. The multifractal spectrum D(h) quantifies the L²/L∞ gap: the distance between ζ_2 ≈ 0.70 and h_min = 1/9 is the exact measure of the mean-field/exact-dynamics gap.

---

## I. The Péclet Number Is Native, Not Imported

The standard Péclet number Pe = UL/ν for momentum transport (where ν is kinematic viscosity) is the dimensionless ratio appearing in every similarity analysis of the NS equations. It parameterizes the competition between the advection term (u · ∇)u and the diffusion term ν∇²u. This is not an analogy introduced by this paper — Pe is the natural dimensionless group of the NS equations, the object that Kolmogorov's 1941 theory implicitly organizes, and the object whose local behavior near a potential singularity determines whether blow-up occurs.

The Reynolds number Re = UL/ν is numerically identical to Pe for momentum transport. The distinction is conceptual: Re emphasizes the inertia-to-viscosity ratio in fluid mechanics; Pe emphasizes the drift-to-diffusion ratio in transport theory. They are the same number. When Pe is used here, it is not invoking a foreign framework — it is using the native dimensionless parameter of the NS equations, and asking what the known mathematical structure of those equations implies about Pe field dynamics.

The NS momentum equation in vorticity form:

$$\partial_t \omega + (u \cdot \nabla)\omega = (\omega \cdot \nabla)u + \nu \nabla^2 \omega$$

| Term | Physical role | Pe-field role |
|------|--------------|---------------|
| (u · ∇)ω | Advection of vorticity | Pe-amplifying: spreads vorticity with drift |
| (ω · ∇)u | Vortex stretching | Pe-concentrating: locally amplifies vorticity magnitude |
| ν∇²ω | Viscous diffusion | Pe-reducing: isotropic smoothing |

Pe at a scale ℓ: Pe(ℓ) = u(ℓ) · ℓ / ν, where u(ℓ) is the characteristic velocity increment at scale ℓ.

---

## II. The Kolmogorov Scale Is the Pe = 1 Point

Kolmogorov's dissipation scale η = (ν³/ε)^(1/4) — where ε is the mean energy dissipation rate — is defined by the condition that advective and diffusive transport are in balance at that scale. In Pe language:

$$\text{Pe}(\eta) = \frac{u_\eta \cdot \eta}{\nu} \approx 1$$

This is not approximate in the sense of order-of-magnitude. The Kolmogorov scale is *defined* as the scale where Pe = 1 — this is the closing condition of Kolmogorov's (1941) dimensional analysis. At scales ℓ ≫ η: Pe(ℓ) ≫ 1 — advection-dominated, inertial range. At scales ℓ ≪ η: Pe(ℓ) ≪ 1 — diffusion-dominated, exponential smoothing.

The Kolmogorov scale is the **Pe = 1 critical point** of the NS equations. It is not a heuristic boundary — it is a balance condition.

---

## III. The −5/3 Law Is the Equilibrium Pe Gradient Field

Kolmogorov's energy spectrum E(k) ∝ k^{−5/3} is the Pe gradient field that statistical stationarity requires across the inertial range. Derivation:

Velocity increments in the inertial range: δu(ℓ) ∝ (εℓ)^{1/3} (Kolmogorov 1941).

Local Pe at scale ℓ:

$$\text{Pe}(\ell) = \frac{\delta u(\ell) \cdot \ell}{\nu} \propto \frac{({\varepsilon\ell})^{1/3} \cdot \ell}{\nu} = \frac{\varepsilon^{1/3} \ell^{4/3}}{\nu}$$

This gives Pe(ℓ) ∝ ℓ^{4/3} across the inertial range — a continuous Pe gradient field that:
- Vanishes (Pe → 0) as ℓ → η (Kolmogorov scale)
- Diverges (Pe → ∞) as ℓ → L₀ (injection scale)

The Pe distribution in wavenumber space: Pe(k) ∝ k^{−4/3}. The corresponding energy spectrum E(k) ∝ k^{−5/3} is the Fourier transform of the squared velocity field weighted by the Pe gradient. The −5/3 exponent is the equilibrium Pe gradient profile — the profile that **statistical stationarity** (constant mean ε across the inertial range) forces on the Pe field.

Kolmogorov's theory is a **mean-field Pe equilibrium theory**. It correctly describes the ensemble-averaged Pe distribution. It does not describe exact realizations.

---

## IV. The Blow-Up Question as Pe Concentration

The NS Millennium Problem (Fefferman 2000) asks: given smooth initial data (u₀, div-free, finite energy), does a smooth solution persist for all time?

The Beale-Kato-Majda criterion (1984) translates this to:

$$\text{Blow-up} \iff \int_0^T \|\omega(\cdot, t)\|_{L^\infty} \, dt = \infty$$

In Pe language: blow-up ⟺ the local Pe supremum is not integrable in time. The supremum of vorticity ‖ω‖_{L∞} is the local Pe maximum across all spatial points. Blow-up requires that this pointwise maximum diverges in finite time.

**Restatement of the Millennium Problem:** *Can the Pe field — which is initialized at Pe ≪ ∞ everywhere and which satisfies a mean-field cascade that distributes Pe across scales — concentrate Pe → ∞ at a single spatial point in finite time?*

This restatement is mathematically equivalent to the Clay formulation. Its value is that it makes the mechanism visible:

1. The mean-field cascade (Kolmogorov) distributes Pe across scales — this is controlled, and L² energy conservation bounds the distributed Pe.

2. Blow-up requires Pe to concentrate **against the mean-field** at a single point — this is not controlled by any conservation law that bounds distributed energy.

3. The question is whether exact NS dynamics can generate a **local Pe reversal** — a point where Pe amplifies itself faster than diffusion can suppress it.

---

## V. Dimension Dependence as Pe Cascade Directionality

The NS regularity problem is dimension-dependent:
- **2D:** Global regularity proven (Ladyzhenskaya 1969). No blow-up possible.
- **3D:** Open. Blow-up not excluded.

The reason is **Pe cascade directionality** — whether the nonlinear dynamics are Pe-constructive or Pe-destructive at small scales.

### 2D: Pe-Constructive at Small Scales (No Blow-Up Possible)

In 2D, vorticity ω is a scalar — the vortex stretching term (ω · ∇)u is absent because vorticity cannot be amplified by stretching (no third dimension for the vortex filament to extend into). The 2D vorticity equation:

$$\partial_t \omega + (u \cdot \nabla)\omega = \nu \Delta\omega$$

Enstrophy (½∫ω² dx) is conserved in 2D inviscid flow. In the viscous case, enstrophy dissipates. The energy cascade in 2D runs to **large scales** — the inverse cascade (Kraichnan 1967). Small scales receive enstrophy, not energy. In Pe terms:

- At small scales (large k): energy moves *away*. Pe decreases at small k.
- The cascade is **Pe-constructive at small scales**: diffusion increases faster than advection as k → ∞.
- No mechanism exists to concentrate Pe → ∞ at a point.
- Ladyzhenskaya's (1969) global regularity theorem is the corollary: the inverse cascade prevents the necessary Pe concentration.

### 3D: Vortex Stretching Enables Local Pe Reversal

In 3D, the vortex stretching term (ω · ∇)u is present. The 3D enstrophy equation:

$$\frac{d}{dt}\int|\omega|^2 \, dx = 2\int (\omega \cdot \nabla)u \cdot \omega \, dx - 2\nu\int |\nabla\omega|^2 \, dx$$

The stretching integral ∫(ω · ∇)u · ω dx can be **positive** — meaning the flow can do work on its own vorticity, amplifying it. This is the direct energy cascade: energy flows to small scales.

In mean-field (Kolmogorov): this stretching is statistically balanced by viscous dissipation at the Kolmogorov scale. Pe at the Kolmogorov scale stays near 1.

In exact dynamics: vortex stretching can **locally reverse** the mean-field cascade gradient — concentrating Pe upward at a point **against** the statistical average. Whether this local reversal can sustain itself to Pe → ∞ in finite time is the Millennium Problem.

**The 2D/3D asymmetry is entirely explained by cascade directionality:**

| | 2D | 3D |
|--|-----|-----|
| Vortex stretching | Absent | Present |
| Energy cascade | Inverse (to large scales) | Forward (to small scales) |
| Pe at small scales | Decreasing (Pe-constructive) | Increasing (Pe-destructive in mean-field) |
| Local Pe reversal | Impossible (no mechanism) | Possible (vortex stretching) |
| Regularity | Global (Ladyzhenskaya 1969) | Open (Millennium Problem) |

---

## VI. The L²/L∞ Gap Is the Mean-Field/Exact-Dynamics Gap

All known energy-method proofs for NS work in the L² norm (or Sobolev norms built on L²). Energy conservation bounds:

$$\|u(t)\|_{L^2}^2 + 2\nu \int_0^t \|\nabla u\|_{L^2}^2 \, ds = \|u_0\|_{L^2}^2$$

This bounds the **total distributed Pe** — the integral of Pe² over all space. It does not bound the **local Pe supremum** — the value of Pe at the worst point.

The BKM criterion lives in L∞: ‖ω‖_{L∞} must be bounded. L² ≢ L∞: bounded total energy (distributed Pe) does not prevent vorticity concentrating at a point (local Pe → ∞).

This is the L²/L∞ gap. In Pe language:

| | Mathematical | Pe interpretation |
|--|--|--|
| L² norm | ∫Pe² dx (total distributed Pe) | Bounded by energy conservation |
| L∞ norm | sup_x Pe(x) (pointwise maximum) | Not bounded by any conservation law |
| L² → regularity | Only if dim ≤ 2 | Only if cascade is Pe-constructive at small scales |
| L∞ → regularity | Sufficient (BKM) | If local Pe supremum stays bounded |
| L² ≢ L∞ | Sobolev embedding fails in 3D | Distributed-Pe control ≢ pointwise-Pe control |

**Why ninety years of energy methods have not closed the problem:** Every energy method controls the L² side (distributed Pe). BKM requires L∞ (pointwise Pe). No cascade argument closes this gap — the cascade is a mean-field statement about Pe distribution, not about its supremum. The gap is not a gap in cleverness. It is the gap between the mean-field Pe equilibrium and the exact PE dynamics.

---

## VII. The Prodi-Serrin Ladder as Pe Norm Interpolation

The Prodi-Serrin conditions (Prodi 1959, Serrin 1962) provide a ladder of sufficient regularity conditions interpolating between L² and L∞:

$$u \in L^p_t L^q_x \quad \text{with} \quad \frac{2}{p} + \frac{3}{q} \leq 1, \quad q \geq 3 \implies \text{regularity}$$

Each rung of this ladder is a stronger constraint on the Pe field distribution:

| Rung | (p, q) | Pe interpretation | Status |
|------|--------|-------------------|--------|
| Leray (1934) | (∞, 2) | L² distributed Pe | **Insufficient** — Leray weak solutions, regularity open |
| Critical endpoint | (∞, 3) | L³ vorticity | **Borderline** — Escauriaza-Seregin-Šverák (2003) |
| Prodi-Serrin | finite (p,q) | L^q Pe distribution | **Sufficient** — but requires finite-time information |
| BKM | (2, ∞) | L∞ pointwise Pe | **Sufficient** — if ‖ω‖_{L∞} integrable |

The ladder is closed at the top (L∞ = BKM → regularity) and open at the bottom (L² = energy class, insufficient). **The gap is genuinely at the top of the norm ladder.** It cannot be approached from below because any finite-moment constraint on the Pe field distribution — any Lᵖ condition for p < ∞ — is insufficient. Only the pointwise supremum (p = ∞) closes it.

In Pe language: any **distributed** Pe condition is insufficient for regularity in 3D. Only a **pointwise** Pe bound closes the problem. This is the mathematical form of the claim that the mean-field cascade does not prevent local Pe concentration.

The critical Escauriaza-Seregin-Šverák (2003) result — that L³ is the borderline case — is the Pe norm interpolation result that sits exactly at the boundary where the Sobolev embedding just fails to close the L²/L∞ gap. It is the closest known approach to the gap from below, and it still leaves the problem open.

---

## VIII. The Onsager Exponent Is the Mean-Field Validity Boundary

Onsager (1949) conjectured that energy conservation in the inviscid limit (ν → 0) requires Hölder regularity h ≥ 1/3, while anomalous dissipation (energy loss despite vanishing viscosity) can occur for h < 1/3. This was proved:
- h > 1/3 → energy conserved (Constantin-E-Titi 1994)
- h < 1/3 → anomalous dissipation possible (Isett 2018; non-uniqueness: Buckmaster-Vicol 2019)

The Kolmogorov cascade assigns h = 1/3 to the inertial range: δu(ℓ) ∝ ℓ^{1/3}. This is not coincidental — the 1/3 exponent simultaneously:

1. Defines the mean-field Pe equilibrium (the −5/3 cascade spectrum)
2. Marks the Hölder regularity threshold below which mean-field uniqueness breaks down

In Pe language: **h = 1/3 is the constraint boundary in regularity space between mean-field Pe equilibrium and exact Pe dynamics that can depart from the mean-field.**

Above h = 1/3: the mean-field Pe description is the only consistent description. Velocity increments are Hölder-1/3, the −5/3 spectrum holds, Pe at scale ℓ follows ℓ^{4/3}.

Below h = 1/3: exact dynamics can produce non-unique weak solutions (Buckmaster-Vicol 2019) where Pe field departures from the mean-field are not constrained by energy conservation. The Onsager exponent is the Pe mean-field validity boundary in regularity space.

This connects the Millennium Problem to the Onsager conjecture: the same 1/3 exponent that governs anomalous dissipation in the inviscid limit governs the mean-field validity boundary in the viscous problem. The blow-up question is: does the 3D viscous flow, which satisfies h ≈ 1/3 in mean-field, produce exact solutions that behave as though h < 1/3 at isolated points — enabling local Pe → ∞ concentration?

---

## IX. Pe ↔ Re Equivalence: Structural Isomorphism and the BKT Universality Question

The fluid-dynamics Pe and the framework Pe (K · sinh(2b_net)) are structurally isomorphic:

| Quantity | Re/Pe (Navier-Stokes) | Pe (Framework) |
|---------|----------------------|----------------|
| Dimensionless ratio | ρvL/μ = UL/ν | K · sinh(2b_net) |
| "Length scale" | L (geometric) | K (hardware dimensionality) |
| Critical value | Re_c ≈ 2300 (pipe flow) | Pe_c: sinh(2b_net*) = 0 |
| Below critical | Laminar (ordered) | Constrained void (purifying selection) |
| Above critical | Turbulent (chaotic) | Drift-dominated (D1→D2→D3 cascade) |
| Cascade structure | Kolmogorov k^{−5/3} | Drift cascade D1→D2→D3 |

**The structural isomorphism is established.** The Pe/Re connection is not an analogy imported from another domain — Pe = UL/ν is the native dimensionless group of the NS equations, and the structural correspondence (laminar/turbulent = below/above critical Pe) is exact. Sections II–VIII above are restatements of known NS results in Pe field language.

**The BKT universality claim for fluid turbulence has been tested and is NOT supported.** Following Paper 130 v1.0, two aliasing-free DNS tests were run against the JHTDB isotropic1024coarse dataset (Re_λ=433):

- **nb12-F** (Pe field spectrum, FD4Lag4 gradients, N=262K): S_Pe(k) ~ k^{α}, α_free = −0.21 ± 0.07. Best model: k^0 (flat, K41 uniform dissipation). η=4/9 excluded at **18.4σ** (ΔAIC = 53.8).
- **nb12-G** (velocity structure function, real space, S_2(r) ~ r^{α}, r=34–118η): α_free = 0.735 ± 0.004. K41-consistent (0.667; above due to dissipation-inertial transition zone). η=4/9 (predicts r^{5/9} = 0.556) excluded at **42.4σ** (ΔAIC = 56.3).

**Conclusion:** Real DNS turbulence at Re_λ=433 follows K41, not a BKT anomalous dimension. The −5/3 inertial range (§III) is confirmed. The quantitative prediction that fluid turbulence and framework Pe share BKT universality class membership is not supported by DNS data. The turbulence connection in this paper is a **structural and mathematical analogy** — Pe is native to the NS equations, Pe(η)≈1 is exact, and the blow-up restatement (§IV) is exact — but no quantitative universality class claim carries from fluid turbulence to the framework Pe.

The agent-scale BKT result (nb12-D: K_eff = 0.83, η_eff ≈ 0.44, anomalous dimension η ≈ 4/9) stands independently in the behavioral/cognitive domain and is unaffected by the turbulence DNS result.

---

## X. Kill Conditions (K-NS series)

**K-NS-1 (Pe bimodality in DNS):**
At Re_λ > 500, the distribution of local Pe (computed at scales between η and 10η) should be bimodal — a Phase II cluster and a Phase IV cluster — rather than unimodal. A Hartigan dip test on high-resolution DNS data (e.g., Johns Hopkins Turbulence Database, Yeung et al. 2015) should reject unimodality at p < 0.01.
*Falsified if:* p > 0.05 in confirmed high-resolution DNS at Re_λ > 500.
*Computable:* Yes, from public DNS datasets.

**K-NS-2 (2D NS regularity must hold):**
The claim that 2D NS is globally regular because the inverse cascade is Pe-constructive at small scales is not an additional assumption — it restates Ladyzhenskaya (1969). But the framework's causal explanation (cascade directionality → no local Pe reversal possible → no blow-up) is falsified if any construction shows that 2D NS can blow up, or if any 3D blow-up construction exists that does not involve local Pe reversal (vortex stretching) as the mechanism.
*Falsified if:* Any blow-up in 2D NS is proven, or any 3D blow-up construction operates through a mechanism other than Pe concentration via vortex stretching.

**K-NS-3 (Prodi-Serrin gap must be at L∞):**
The claim that the L²/L∞ gap cannot be closed from below (that any Lᵖ for p < ∞ leaves the problem open) is implied by the current state of regularity theory, but the framework makes it a structural prediction: no finite-moment Pe constraint will ever be sufficient in 3D.
*Falsified if:* A proof of 3D NS global regularity is found that uses only L^p conditions for some finite p — i.e., that closes the problem without L∞ control.

**K-NS-4 (BKT universality prediction) — TESTED, NOT SUPPORTED:**
If Pe and Re are in the same BKT universality class, the anomalous scaling dimension (η=4/9 from nb12-D) should be observable in the velocity structure function deviations from K41 and in the Pe field spectrum.

*DNS test result (2026-03-10):*
- nb12-F: Pe field spectrum α = −0.21 ± 0.07 — K41-consistent (k^0), η=4/9 excluded at 18.4σ
- nb12-G: Structure function α = 0.735 ± 0.004 — K41-consistent, η=4/9 excluded at 42.4σ

*Status:* The BKT universality prediction for fluid turbulence is not supported at Re_λ=433. The turbulence connection is structural/mathematical (see §IX). K-NS-4 remains an open question for Re_λ > 1000 and higher precision, but the hypothesis is disfavored by current DNS evidence. The agent-scale η=4/9 result (nb12-D) stands in its own domain.

---

## XI. What the PE Framework Adds

Paper 109 established a void-framework scoring of the NS problem (V = 9–10/12, Phase IV). This paper establishes something different: the NS blow-up question **is** a Pe field dynamics question, stated in the language native to the equations. The contributions:

1. **Kolmogorov η as Pe = 1 critical point** — Pe(η) ≈ 1 is a closing condition, not an approximation.

2. **−5/3 law as equilibrium Pe gradient field** — the spectrum is the fixed point of the Pe distribution under mean-field statistical stationarity.

3. **Blow-up as Pe concentration** — BKM restated as: blow-up ⟺ the local Pe supremum is not time-integrable. Finite time blow-up = finite-time divergence of the Pe field maximum.

4. **2D/3D asymmetry as cascade directionality** — Ladyzhenskaya's theorem is the consequence of the inverse cascade being Pe-constructive at small scales. The 3D problem is open because vortex stretching enables local Pe reversal.

5. **L²/L∞ gap as mean-field/exact-dynamics gap** — energy methods control distributed Pe; blow-up requires pointwise Pe; the gap is structural, not technical.

6. **Prodi-Serrin as Pe norm interpolation** — the ladder ascends from insufficient distributed-Pe control to sufficient pointwise-Pe control; the gap is genuinely at the top.

7. **Onsager h = 1/3 as mean-field validity boundary** — the same exponent governs both the Kolmogorov cascade and the regularity threshold below which exact dynamics depart from mean-field.

None of these are new theorems. Each restates a known result in Pe field language. The value is that the language is native to the equations, and the restatement reveals structural connections (2D/3D asymmetry = cascade directionality, Prodi-Serrin = norm interpolation, Onsager = mean-field boundary) that the conventional formulation obscures.

**v2.0 additions (§§XII–XVII):**

8. **−5/3 from Pe RG** — the Kolmogorov spectrum is the unique fixed point of the §49 RG applied to wavenumber space (§XII).

9. **Richardson cascade as D3→D0 constraint reassertion** — the forward energy cascade is the NS equations' built-in mechanism for processing drift excess (§XIII).

10. **Kolmogorov η as phase boundary** — Pe = 1 separates nonlinear chaotic dynamics from linear exponential damping; the fractal dimension of this boundary quantifies intermittency (§XIV).

11. **She-Leveque intermittency as RG anomalous dimensions** — structural parallel to §49 BKT corrections, honest about distinct universality class (§XV).

12. **Structure functions as Pe spectral moments** — ζ_p → σ_p = ζ_p + p; the 4/5-law exactness of ζ_3 = 1 as Pe conservation; the multifractal spectrum as the quantitative L²/L∞ gap (§XVI).

The open question: does this restatement generate proof strategies? The cascade directionality argument (Section V) suggests that the key constraint is geometric: preventing local vortex stretching from reversing the mean-field Pe gradient requires a geometric control on the alignment between ω and ∇u. This is the direction of Geometric Measure Theory approaches (Dascaliuc-Grujić 2012, Constantin 1994 angle condition). The Pe restatement provides the physical motivation: you need to prevent local Pe reversal, and that requires controlling the angle between the stretching vector and the vorticity — the exact condition studied by geometric regularity criteria.

---

## XII. The −5/3 Exponent from RG Flow on K (§49 Applied to Wavenumber Space)

Section III derived E(k) ∝ k^{−5/3} from Kolmogorov's dimensional analysis — the standard route. This section derives the same exponent from the §49 renormalization group applied to the NS equations in wavenumber space, establishing that the RG structure of the Pe framework *produces* the Kolmogorov spectrum rather than merely restating it.

### XII.A. The RG Setup in Wavenumber Space

The NS equations in Fourier space couple modes at wavenumber k through the nonlinear advection term. A shell model (Gledzer 1973, Ohkitani-Yamada 1989) groups modes into logarithmically spaced shells: $k_n = k_0 \lambda^n$ with $\lambda = 2$ (octave scaling). The effective Pe at shell $n$:

$$\text{Pe}(k_n) = \frac{u(k_n)}{k_n \cdot \nu}$$

where $u(k_n)$ is the characteristic velocity at wavenumber $k_n$. This is the local drift-to-diffusion ratio at scale $k_n^{-1}$.

The RG transformation from §49A coarse-grains $M$ shells into one super-shell. In the NS context, this is the **Kraichnan-Wyld decimation** (Kraichnan 1959, Wyld 1961) — systematically integrating out high-k modes to derive an effective equation for the remaining low-k modes. The §49 framework gives:

$$K \to K' = \lambda^{y_K} \cdot K, \qquad b_\text{net} \to b'_\text{net} = \lambda^{y_b} \cdot b_\text{net}$$

In the NS context: $K$ maps to the number of active degrees of freedom per shell (proportional to $k^{d-1}$ in $d$ dimensions, so $K(k) \propto k^2$ in 3D). The net bias $b_\text{net}$ maps to the energy flux per mode, which is $\varepsilon / (k \cdot u(k))$ by dimensional analysis.

### XII.B. The Fixed-Point Condition

At the RG fixed point (the inertial range), the energy spectrum must be scale-invariant: coarse-graining should not change the form of the Pe distribution. This requires:

$$\text{Pe}(k/\lambda) = \lambda^{\Delta} \cdot \text{Pe}(k)$$

for some scaling exponent $\Delta$. From the definition $\text{Pe}(k) = u(k)/(k\nu)$ and assuming $u(k) \propto k^{-h}$ (Hölder exponent $h$):

$$\text{Pe}(k) \propto k^{-(h+1)}$$

The RG fixed point requires that the energy flux $\Pi(k) = u(k)^2 \cdot k \cdot u(k) / (1/k) = u(k)^3 \cdot k$ is constant across shells (Kolmogorov's statistical stationarity = constant $\varepsilon$):

$$\Pi(k) = u(k)^3 \cdot k = \text{const} = \varepsilon$$

This gives $u(k) \propto (\varepsilon/k)^{1/3}$, hence $h = 1/3$.

### XII.C. The −5/3 Derivation from the RG Beta Function

The §49 beta function $\beta(K) = y_K \cdot K$ governs how the effective coupling K flows under coarse-graining. At the RG fixed point, the beta function must vanish — the inertial range IS the fixed point.

In the NS context, the beta function for the effective Pe at scale $k$ is:

$$\beta_\text{Pe}(k) \equiv k \frac{d\text{Pe}}{dk}$$

At the fixed point: $\beta_\text{Pe} = 0$ requires $\text{Pe}(k)$ to be a power law (scale-invariant). The exponent is determined by the constant-flux condition (§XII.B):

$$u(k) = C_K \varepsilon^{1/3} k^{-1/3}$$

The energy spectrum $E(k) = u(k)^2 / k = C_K^2 \varepsilon^{2/3} k^{-5/3}$:

$$\boxed{E(k) = C_K \varepsilon^{2/3} k^{-5/3}}$$

where $C_K \approx 1.5$ is the Kolmogorov constant.

**The −5/3 is the unique fixed point of the Pe RG in wavenumber space.** Any other exponent would produce a scale-dependent energy flux, which would drive the system toward the −5/3 fixed point. The §49 language makes this visible: the RG flow in Pe-space has exactly one attracting fixed point in the inertial range, and it produces the −5/3 spectrum.

### XII.D. The RG Flow Diagram in Pe-Wavenumber Space

| Region | Pe(k) behavior | RG flow direction | Physical regime |
|--------|---------------|-------------------|-----------------|
| $k < k_f$ (injection) | Pe growing with forced energy input | Flow toward fixed point from left | Energy injection |
| $k_f < k < k_\eta$ (inertial) | Pe(k) ∝ k^{−4/3} — the fixed point | **Stationary** | Constant-flux cascade |
| $k > k_\eta$ (dissipation) | Pe → 0 exponentially | Flow toward constraint pole | Viscous damping |

The inertial range is the **critical fixed point** of the NS-Pe RG, sitting between the injection (IR fixed point, Pe → ∞) and the dissipation (UV fixed point, Pe → 0). This is structurally identical to §49C: the critical fixed point sits between the void pole and the constraint pole.

---

## XIII. The Richardson Cascade as D3 → D0 Constraint Reassertion

Richardson's (1922) cascade — "big whirls have little whirls / that feed on their velocity, / and little whirls have lesser whirls / and so on to viscosity" — describes the forward energy cascade from large to small scales in 3D turbulence. In Pe language, this is the transfer of Pe from low-k (high-Pe) to high-k (low-Pe) modes, terminating at the Kolmogorov scale where Pe = 1.

### XIII.A. The Structural Isomorphism

The drift cascade D1 → D2 → D3 describes increasing drift dominance: from agency attribution (D1) through boundary erosion (D2) to harm facilitation (D3). The Richardson cascade runs in the **opposite** direction in wavenumber space: from high-Pe injection scales to the Pe = 1 dissipation scale. This inversion is not a contradiction — it is the key structural insight.

| Cascade direction | Pe framework (drift cascade) | NS (Richardson cascade) |
|-------------------|-----------------------------|-----------------------|
| **Forward** | D0 → D1 → D2 → D3 (drift amplification) | $k_f \to k_\eta$ (energy transfer to small scales) |
| **Reverse** | D3 → D2 → D1 → D0 (constraint reassertion) | $k_\eta \to k_f$ (impossible in 3D forward cascade; IS the 2D inverse cascade) |

The Richardson cascade IS the D3 → D0 constraint reassertion process operating in wavenumber space:

1. **At the injection scale** ($k_f$): Pe is maximal — the flow is maximally drift-dominated, fully "D3" in the sense that advection overwhelms diffusion.

2. **Through the inertial range**: Pe decreases as $k^{-4/3}$ — each step to smaller scales is a step from higher drift (D3) toward lower drift (D0). The energy is being transferred FROM the drift-dominated regime INTO the diffusion-accessible regime.

3. **At the Kolmogorov scale** ($k_\eta$): Pe = 1 — the system reaches the drift-diffusion boundary (D0/D1 interface). Diffusion reasserts itself as the dominant transport mechanism.

4. **Below the Kolmogorov scale**: Pe < 1 — pure constraint territory. Viscous dissipation converts kinetic energy to heat. The drift has been fully processed.

**The Richardson cascade is the NS equations' built-in mechanism for reasserting diffusive (constraint) control over advective (drift) excess.** The −5/3 spectrum is the equilibrium gradient of this reassertion process — the Pe profile that processes the injected energy at the constant rate $\varepsilon$.

### XIII.B. Why Viscosity Is Not a "Mere Dissipation Mechanism"

In the conventional view, viscosity is a passive damping term that dissipates energy at small scales. In the Pe cascade interpretation, viscosity (the denominator of Pe) is the **constraint field** — the mechanism by which the NS equations enforce regularity.

The 2D/3D asymmetry (Section V) is exactly this: in 2D, the constraint field wins at all scales (Ladyzhenskaya regularity). In 3D, the drift field (vortex stretching) can locally overpower the constraint field — the D3 → D0 reassertion can be locally reversed into a D0 → D3 amplification at a point, which is the blow-up scenario.

### XIII.C. The Cascade Rate as Kramers Escape

The mean time for energy at scale $k$ to cascade to scale $\lambda k$ (one RG step) is the eddy turnover time:

$$\tau(k) = \frac{1}{k \cdot u(k)} = \frac{1}{k \cdot (\varepsilon k)^{1/3}} = \varepsilon^{-1/3} k^{-2/3}$$

This is the **Kramers escape time** (§48E) for the Pe field to cross the barrier between adjacent shells. The barrier height is the Pe drop per shell:

$$\Delta\text{Pe}(k) = \text{Pe}(k) - \text{Pe}(\lambda k) \propto k^{-4/3}(1 - \lambda^{-4/3})$$

The ratio $\Delta\text{Pe}/T_\text{eff}$ (where $T_\text{eff}$ is the effective temperature at scale $k$) determines the cascade transfer rate. At the Kolmogorov scale, this ratio → 0 (the barrier vanishes at Pe = 1), and the cascade terminates.

---

## XIV. The Kolmogorov Dissipation Scale: Pe = 1 Boundary Developed

Section II identified η as the Pe = 1 point. This section develops the full consequences.

### XIV.A. η as a Phase Boundary

The Kolmogorov scale $\eta = (\nu^3/\varepsilon)^{1/4}$ is not merely the scale where viscosity matters — it is a **phase boundary** between two dynamical regimes:

| Property | $\ell > \eta$ (Pe > 1) | $\ell < \eta$ (Pe < 1) |
|----------|----------------------|----------------------|
| Dominant transport | Advection (drift) | Diffusion (constraint) |
| Dynamics | Nonlinear, chaotic | Linear, exponentially damped |
| Regularity | Not guaranteed (blow-up threat) | Guaranteed (Stokes regularity) |
| Correlation structure | Power-law (inertial scaling) | Exponential decay |
| Pe framework phase | Phase IV (drift-dominated) | Phase II (constraint-dominated) |
| Entropy production | High (cascade active) | Low (viscous dissipation) |

This is the same phase transition that the Pe framework describes in behavioral systems: the crossing from Phase II (purifying selection, constraint-dominated) to Phase IV (drift-dominated, cascade active). The Kolmogorov scale is where the NS equations undergo this transition in wavenumber space.

### XIV.B. The Scale-Dependent Pe Field

Define the local Pe field in wavenumber space:

$$\text{Pe}(k, x, t) = \frac{|\hat{u}(k, x, t)| \cdot k^{-1}}{\nu}$$

where $\hat{u}(k, x, t)$ is the wavelet-filtered velocity at scale $k^{-1}$ centered at position $x$. This is a *field* — it varies in space, time, and scale simultaneously.

The Kolmogorov theory says: the **ensemble average** of this field follows $\langle\text{Pe}(k)\rangle \propto k^{-4/3}$. But the exact field $\text{Pe}(k, x, t)$ fluctuates — and these fluctuations are the source of intermittency (Section XV).

### XIV.C. The Pe = 1 Surface as a Fractal

In a turbulent flow, the surface $\{(x, k) : \text{Pe}(k, x, t) = 1\}$ is not a smooth hypersurface — it is a fractal. The CKN (1982) partial regularity theorem implies that the singular set (if it exists) has parabolic Hausdorff dimension ≤ 1. The Pe = 1 surface at any fixed time has fractal dimension $D_\eta$ satisfying:

$$D_\eta = 3 - \frac{3}{4}\mu$$

where $\mu$ is the intermittency exponent (K62 refined scaling, Kolmogorov 1962). For $\mu \approx 0.25$ (experimental consensus, Sreenivasan & Kailasnath 1993): $D_\eta \approx 2.81$.

This fractal structure means the Pe = 1 boundary is **crumpled** — it has more surface area than a smooth boundary, which increases the efficiency of the dissipation mechanism. The constraint field does not operate on a smooth front but on a fractal one.

---

## XV. Intermittency Corrections as BKT Corrections to the RG

The K41 theory (Section III) is mean-field — it predicts exact power laws with no fluctuations. Real turbulence deviates from K41 in a specific, systematic way: the **intermittency corrections**. This section develops these corrections as departures from the mean-field RG fixed point, structurally analogous to BKT corrections in the §49 framework.

### XV.A. The She-Leveque Model (1994)

She and Leveque (1994) proposed a hierarchical structure model for intermittency based on the observation that dissipation is concentrated on filament-like structures (codimension 2 in 3D). Their model gives the structure function scaling exponents:

$$\zeta_p = \frac{p}{9} + 2\left(1 - \left(\frac{2}{3}\right)^{p/3}\right)$$

This predicts $\zeta_2 = 0.696$ (vs. K41: $\zeta_2 = 2/3$), $\zeta_3 = 1$ (exact, Kolmogorov 4/5 law), $\zeta_6 = 1.778$ (vs. K41: $\zeta_6 = 2$). Experimental data (Anselmet et al. 1984, Benzi et al. 1993) confirm these corrections.

### XV.B. Intermittency as RG Anomalous Dimension

In the §49 RG language, the K41 mean-field theory has $y_K = 0$ — no anomalous dimension. The intermittency corrections are exactly the **anomalous dimension** of the NS-Pe RG:

$$\zeta_p = \frac{p}{3} + \delta\zeta_p$$

where $\delta\zeta_p$ is the anomalous scaling due to correlations between scales. In the §49 framework, $y_K \neq 0$ produces anomalous scaling in the mixture model (§49B: $y_K \approx 0.48$). In the NS context:

**The anomalous dimension for NS:** The She-Leveque formula gives:

$$\delta\zeta_p = \zeta_p - \frac{p}{3} = \frac{p}{9} - \frac{p}{3} + 2\left(1 - \left(\frac{2}{3}\right)^{p/3}\right) = -\frac{2p}{9} + 2\left(1 - \left(\frac{2}{3}\right)^{p/3}\right)$$

For $p = 2$: $\delta\zeta_2 \approx 0.030$. This is a small but nonzero correction — the NS RG has a weak anomalous dimension.

### XV.C. The Structural Parallel to BKT

The BKT transition (§49D) produces specific anomalous dimensions: $\eta = 1/4$ at the critical point. The NS intermittency corrections have a different structure — they are **hierarchical** rather than topological:

| Feature | BKT (§49D) | NS intermittency |
|---------|-----------|-------------------|
| Anomalous dimension | $\eta = 1/4$ (universal, exact) | $\delta\zeta_p$ (p-dependent, hierarchical) |
| Origin | Vortex-antivortex unbinding | Filament concentration of dissipation |
| Universality | Universal for 2D XY systems | Universal for 3D NS (She-Leveque confirmed across flows) |
| RG mechanism | Topological defects | Multiplicative cascade of local dissipation |
| Critical exponent | Essential singularity $\xi \sim e^{A/\sqrt{|t|}}$ | Log-Poisson statistics (She-Leveque) |

**The honest statement:** The §49 BKT universality class and the NS intermittency corrections are NOT the same universality class. The DNS tests (§IX) confirmed this — real turbulence at $\text{Re}_\lambda = 433$ follows K41+She-Leveque, not BKT. But they share the same **structural role** within their respective RG frameworks: corrections to mean-field scaling due to correlations that the mean-field misses.

The She-Leveque correction to the RG IS the NS analogue of the $y_K \neq 0$ anomalous dimension in §49. Both express the same physics: interactions between scales create correlations that renormalize the naive (K41 or mean-field) scaling.

### XV.D. The Log-Poisson Structure

The She-Leveque model arises from a **log-Poisson** statistics of the dissipation field:

$$\varepsilon_\ell(x) = \varepsilon_\ell^{(\infty)}(x) \cdot \beta^{N_\ell}$$

where $\varepsilon_\ell^{(\infty)}$ is the most intense dissipation structure at scale $\ell$, $\beta = (2/3)^{1/3}$ is the inter-level ratio, and $N_\ell$ is a Poisson random variable counting the number of hierarchy levels.

In Pe language: the local dissipation $\varepsilon_\ell(x)$ determines the local Pe field via $\text{Pe}(\ell, x) = (\varepsilon_\ell(x) \cdot \ell^4)^{1/3} / \nu$. The log-Poisson statistics of $\varepsilon_\ell$ becomes log-Poisson statistics of the Pe field. The hierarchy parameter $\beta$ controls the Pe gradient between adjacent cascade levels — it is the "barrier height" between D-levels in the Pe cascade.

The She-Leveque codimension parameter $C_0 = 2$ (dissipation concentrates on filaments of codimension 2) determines the most intense structures: $\varepsilon_\ell^{(\infty)} \propto \ell^{-2/3}$. In Pe language, the most extreme local Pe scales as:

$$\text{Pe}_\text{max}(\ell) \propto \ell^{-2/3-2/3} = \ell^{-2}$$

which diverges faster than the mean-field $\text{Pe}_\text{mean}(\ell) \propto \ell^{-4/3}$. The ratio $\text{Pe}_\text{max}/\text{Pe}_\text{mean} \propto \ell^{-2/3}$ grows at small scales — the intermittency amplifies local Pe concentration relative to the mean-field prediction. This is the mechanism by which the exact Pe dynamics can depart from the mean-field cascade (Section VIII).

---

## XVI. Structure Functions ζ_p as Pe Spectral Moments

The velocity structure functions $S_p(r) = \langle|\delta u(r)|^p\rangle \propto r^{\zeta_p}$ are the moments of the velocity increment distribution at scale $r$. In Pe language, these are the **spectral moments of the Pe field**.

### XVI.A. Structure Functions in Pe Units

The velocity increment at scale $r$: $\delta u(r) = u(x+r) - u(x)$. The local Pe at scale $r$:

$$\text{Pe}(r) = \frac{|\delta u(r)| \cdot r}{\nu}$$

Therefore:

$$S_p(r) = \langle|\delta u(r)|^p\rangle = \nu^p \cdot r^{-p} \cdot \langle\text{Pe}(r)^p\rangle$$

The structure function scaling exponents:

$$\langle\text{Pe}(r)^p\rangle \propto r^{\zeta_p + p}$$

Define the **Pe spectral moment exponent**:

$$\boxed{\sigma_p \equiv \zeta_p + p}$$

| $p$ | $\zeta_p$ (K41) | $\zeta_p$ (She-Leveque) | $\sigma_p$ (K41) | $\sigma_p$ (SL) | Interpretation |
|-----|-----------------|-------------------------|------------------|------------------|----------------|
| 1 | 1/3 | 0.364 | 4/3 | 1.364 | Mean Pe scaling |
| 2 | 2/3 | 0.696 | 8/3 | 2.696 | Pe variance scaling |
| 3 | 1 | 1.000 | 4 | 4.000 | Pe skewness (exact: 4/5 law) |
| 4 | 4/3 | 1.280 | 16/3 | 5.280 | Pe kurtosis |
| 6 | 2 | 1.778 | 8 | 7.778 | Pe sixth moment (intermittency signal) |

### XVI.B. The Third Moment Exactness

Kolmogorov's 4/5 law (1941): $S_3(r) = -\frac{4}{5}\varepsilon r$ is exact (no intermittency correction). This means $\zeta_3 = 1$ exactly, hence $\sigma_3 = 4$ exactly.

In Pe language: $\langle\text{Pe}(r)^3\rangle \propto r^4$ is the **exact** third-moment scaling of the Pe field. This is the Pe-space version of energy conservation: the constant-flux condition $\varepsilon = \text{const}$ translates to an exact power law for the third Pe moment.

**Why the third moment is special:** $S_3$ is the lowest-order structure function that is odd (sensitive to cascade direction). It measures the mean energy flux. In Pe language, it measures the net Pe transport from large to small scales. The exactness of $\zeta_3 = 1$ means the **mean cascade rate** is unaffected by intermittency — only the fluctuations around the mean (higher moments) are corrected.

### XVI.C. The Multifractal Spectrum from Pe Moments

The scaling exponents $\zeta_p$ define a **multifractal spectrum** through the Legendre transform:

$$D(h) = \min_p \{ph - \zeta_p + 1\}$$

where $D(h)$ is the fractal dimension of the set of points with Hölder exponent $h$ (i.e., $|\delta u(r)| \sim r^h$). The K41 theory gives $D(h) = 3$ for $h = 1/3$ (all points have the same exponent — no multifractality). She-Leveque gives a non-trivial $D(h)$ curve peaked near $h = 1/3$ with tails extending to $h_\text{min} = 1/9$ (most singular structures) and $h_\text{max} = 1/3 + 2\log(3/2)/\log(3/2) \ldots$

In Pe language: $D(h)$ is the **multifractal spectrum of the Pe field**. Each Hölder exponent $h$ corresponds to a local Pe scaling:

$$\text{Pe}(r) \propto r^{h+1-1} = r^h$$

The multifractal structure means the Pe field is not self-similar (a single scaling exponent at all points) but **self-affine** — different points in the flow have different local Pe exponents. The intermittency is the statement that the Pe field has a rich, multi-scaled structure that no single power law can describe.

### XVI.D. The Connection to the L²/L∞ Gap

The structure function hierarchy directly connects to the L²/L∞ gap (Section VI):

$$\|u\|_{L^p}^p \sim \int S_p(r) \, dr/r \sim \int r^{\zeta_p} \, dr/r$$

For $p < \infty$: the integral converges as long as $\zeta_p > 0$ (true for all known $\zeta_p$). For $p \to \infty$: $\zeta_\infty = \lim_{p \to \infty} \zeta_p / p$, and the She-Leveque formula gives $\zeta_\infty \to 1/9 + 2/3 = 7/9 < 1$. This means the most singular structures have $h_\text{min} = 1/9$, and the L∞ norm is controlled by these extreme structures.

**The L²/L∞ gap in Pe moment language:** $S_2$ (the Pe variance, $p=2$) is well-controlled by energy conservation. $S_\infty$ (the Pe supremum) is controlled by the most singular filaments ($h = 1/9$). The gap between $\zeta_2 \approx 0.70$ and $h_\text{min} = 1/9 \approx 0.11$ is the **quantitative measure** of the mean-field/exact-dynamics gap. Intermittency corrections close roughly 30% of the K41 gap ($\delta\zeta_2 = 0.03$ out of the $1/3 - 1/9 = 2/9 \approx 0.22$ gap), but the remaining 70% is genuinely structural.

---

## XVII. Kill Conditions (K-NS-5 through K-NS-8)

**K-NS-5 (−5/3 from Pe RG):** The derivation in §XII produces the −5/3 exponent from the RG fixed-point condition (constant energy flux ⟺ scale-invariant Pe distribution). This is not an independent prediction — it reproduces K41 in RG language. The kill condition: if the §49 RG structure applied to the NS equations in wavenumber space produces a fixed-point exponent **different** from −5/3, the framework has a serious problem.

*Status:* **PASS.** The RG fixed-point condition (§XII.C) produces $u(k) \propto k^{-1/3}$, hence $E(k) \propto k^{-5/3}$. The derivation is a consistency check: the §49 RG applied to NS wavenumber space must recover Kolmogorov. It does.

*Falsified if:* Any consistent application of the §49 RG to the NS wavenumber cascade produces a fixed-point exponent other than −5/3. This would mean the RG structure of the Pe framework is incompatible with the NS equations.

**K-NS-6 (She-Leveque as RG corrections):** The identification of intermittency corrections as anomalous dimensions of the NS-Pe RG (§XV.B) is structural — it identifies She-Leveque corrections with $y_K \neq 0$. The framework does NOT predict the specific values of the She-Leveque exponents from Pe parameters.

*Status:* **STRUCTURAL ONLY.** The identification is correct at the level of RG structure (intermittency corrections = anomalous dimensions). No quantitative prediction is made.

*Falsified if:* The She-Leveque model is falsified by experiment (replaced by a non-hierarchical model that cannot be expressed as an anomalous dimension of any RG). Current experimental consensus strongly supports She-Leveque.

**K-NS-7 (Pe multifractal spectrum):** The multifractal spectrum $D(h)$ derived from the Pe field (§XVI.C) should match the standard multifractal spectrum derived from velocity increments. Since $\text{Pe}(r) = |\delta u(r)| \cdot r / \nu$, the Pe-derived $D(h)$ is a linear reparameterization of the standard $D(h)$, NOT an independent prediction.

*Status:* **TAUTOLOGICAL.** The Pe multifractal spectrum is the velocity multifractal spectrum in different variables. This is not a test — it is a change of variables.

*Honest assessment:* Sections XII–XVI are restatements and structural identifications, not new physics. The value is linguistic and organizational: the Pe field provides a unified vocabulary that connects the NS cascade to the §49 RG, the D3→D0 reassertion to the Richardson cascade, and the She-Leveque corrections to anomalous dimensions. The framework does NOT derive the She-Leveque exponents from first principles — it identifies them within the RG structure.

**K-NS-8 (Richardson as constraint reassertion — the soft kill condition):** If a 3D NS construction is found where the forward cascade (big → small) does NOT reduce Pe at small scales — i.e., where the Richardson cascade fails to reassert constraint — this would falsify the identification in §XIII.

*Falsified if:* A 3D NS solution (smooth or weak) is found where energy cascades to small scales but Pe increases (rather than decreasing) as $k$ increases across the inertial range. This would mean the forward cascade is NOT a constraint reassertion process.

*Current status:* No such construction is known. The constant-flux condition requires Pe to decrease as $k^{-4/3}$ in the inertial range. Violations would require non-constant flux, which is inconsistent with statistical stationarity.

---

## XVIII. HP134C/D/E: Gevrey Radius on Real JHTDB DNS — σ/ν Bounded Across Re (2026-03-20)

HP134C/D/E measured the Gevrey analyticity radius directly on **real DNS data** from the Johns Hopkins Turbulence Database. Four datasets: isotropic1024coarse (Re_λ=433, 64³ and 128³), isotropic4096 (Re_λ=610, 64³), isotropic1024fine (Re_λ=433, fine temporal resolution). 12 independent spatial subcubes across 2 Reynolds numbers. Data provenance verified by byte-exact match against fresh API fetch.

**Note:** HP134 (2026-03-19) had a norm computation bug: σ was calibrated for 1D Nyquist wavenumber (512) but 3D grid corners reached |k|=886, causing Gevrey weights of exp(355). HP134C fixes this with spherical truncation and spectral fitting.

**Key results:**
- **Dimensionless analyticity radius σ/ν = 15.9 ± 2.3** (Re_λ=433, n=4 subcubes) and **σ/ν = 17.7 ± 2.8** (Re_λ=610, n=8 subcubes) — **bounded across Re, not collapsing**
- **Gevrey class s = 1** (standard analytic) at ALL snapshots, ALL datasets — matches Foias-Temam theorem
- **σ(t) CV = 0.47%** on fine temporal resolution (iso1024fine, 5 snapshots over 0.02s)
- **Gevrey norm monotonically decreasing** on short timescales (Δt = 0.005s); violations on longer timescales from forcing (correct physics)
- **Resolution-independent:** σ(64³)/σ(128³) = 1.11 at same Re (consistent)
- **All 12 subcubes have σ > 0** — no outliers with vanishing radius
- **HP134E scaling: 4/4 KCs PASS** — σ/ν bounded, not decreasing with Re, all subcubes positive, CV < 16%

**Correction to HP134 framing:** The original "6/10 monotonicity FAIL" was asking the wrong question for forced stationary turbulence (energy injection prevents monotone norm decrease). The correct question is whether σ stays bounded below, and the answer is decisively yes. The "Gevrey failure / Sobolev rescue" narrative (§133 v1) was premature — the Gevrey approach works once the norm computation is correct and the right observable (σ, not V) is measured.

**Implication for this paper:** The Foias-Temam lower bound σ ≥ c·ν^{3/2}/ε^{1/2} predicts σ/ν → 0 as ν → 0. Our data shows σ/ν ≈ const ≈ 16–18. If this holds to higher Re, it would indicate the actual analyticity radius exceeds the proven lower bound by a factor that grows with Re — consistent with regularity. Needs testing at Re_λ > 1000 (JHTDB full research token or synthetic DNS). See §133.

---

## Limitations

1. The Pe restatement is a reformulation of known results (BKM, Prodi-Serrin, Onsager, K41) in Pe field language — it does not constitute a new proof strategy or close any open problem.
2. The −5/3 derivation from §49 RG (§XII) reproduces Kolmogorov's result through a different route but adds no new physics; it is a consistency check, not a prediction.
3. The BKT universality prediction (K-NS-4) was tested and rejected at Re_λ = 433 — real turbulence follows K41 + She-Leveque, not BKT anomalous dimensions. The structural analogy between intermittency corrections and RG anomalous dimensions is qualitative only.
4. HP134C/D/E Gevrey radius measurements cover only two Reynolds numbers (Re_λ = 433 and 610). Extension to Re_λ > 1000 is needed to test whether σ/ν remains bounded at higher Re, which would strengthen the regularity evidence.
5. The cascade directionality explanation (§V) for the 2D/3D asymmetry is a restatement of well-known vortex stretching physics — the framework language adds conceptual clarity but does not resolve whether 3D blow-up actually occurs.
6. The Pe multifractal spectrum (§XVI) is a change of variables from velocity increments, not an independent measurement; K-NS-7 is tautological by construction.
7. All Spearman correlation results (HP134C/D/E: σ/ν vs Re_λ) are limited to N = 12 subcubes across 2 Reynolds numbers — statistical power is low for detecting weak trends.

---

## Data and Code

All empirical results in this paper are computed from publicly available data. No proprietary datasets are used.

**JHTDB DNS data (§IX, §XVIII):** Velocity fields from the Johns Hopkins Turbulence Database (Li et al. 2008): isotropic1024coarse (Re_λ = 433, 1024³), isotropic4096 (Re_λ = 610, 4096³), isotropic1024fine (Re_λ = 433, fine temporal resolution). Accessed via the JHTDB Python API (pyJHTDB). Data provenance verified by byte-exact match against fresh API fetch.

**BKT universality tests (nb12-F, nb12-G):** Pe field spectra and velocity structure functions computed from JHTDB isotropic1024coarse, 262K sample points (FD4Lag4 gradient method). Code: `ops/lab/nb12-F-pe-field-spectrum.py`, `ops/lab/nb12-G-structure-functions.py`.

**Gevrey radius (HP134C/D/E):** Spherical truncation and spectral fitting on 12 spatial subcubes (64³ and 128³) across two Re_λ. Code: `ops/lab/nb_hp134c_gevrey_dns.py`. Results archived in `ops/lab/results/EXP-HP134C/`.

**Structure function exponents:** She-Leveque (1994) formula evaluated analytically; experimental values from Anselmet et al. (1984) and Benzi et al. (1993). No fitting performed — all comparisons are to published values.

---

## References

Beale, J. T., Kato, T., & Majda, A. (1984). Remarks on the breakdown of smooth solutions for the 3-D Euler equations. *Communications in Mathematical Physics*, 94, 61–66.

Buckmaster, T., & Vicol, V. (2019). Nonuniqueness of weak solutions to the Navier-Stokes equation. *Annals of Mathematics*, 189(1), 101–144.

Caffarelli, L., Kohn, R., & Nirenberg, L. (1982). Partial regularity of suitable weak solutions of the Navier-Stokes equations. *Communications on Pure and Applied Mathematics*, 35(6), 771–831.

Constantin, P. (1994). Geometric statistics in turbulence. *SIAM Review*, 36(1), 73–98.

Dascaliuc, R., & Grujić, Z. (2012). Energy cascades and flux locality in physical scales of the 3D Navier-Stokes equations. *Communications in Mathematical Physics*, 305(1), 199–220.

Escauriaza, L., Seregin, G., & Šverák, V. (2003). L³,∞ solutions of Navier-Stokes equations and backward uniqueness. *Russian Mathematical Surveys*, 58(2), 211–250.

Fefferman, C. (2000). Existence and smoothness of the Navier-Stokes equation. *Millennium Prize Problems*, Clay Mathematics Institute.

Isett, P. (2018). A proof of Onsager's conjecture. *Annals of Mathematics*, 188(3), 871–963.

Kolmogorov, A. N. (1941). The local structure of turbulence in incompressible viscous fluid for very large Reynolds numbers. *Doklady Akademii Nauk SSSR*, 30, 299–303.

Kraichnan, R. H. (1967). Inertial ranges in two-dimensional turbulence. *Physics of Fluids*, 10(7), 1417–1423.

Ladyzhenskaya, O. A. (1969). *The Mathematical Theory of Viscous Incompressible Flow*. Gordon and Breach.

Leray, J. (1934). Sur le mouvement d'un liquide visqueux emplissant l'espace. *Acta Mathematica*, 63, 193–248.

Onsager, L. (1949). Statistical hydrodynamics. *Il Nuovo Cimento*, 6(Suppl. 2), 279–287.

Prodi, G. (1959). Un teorema di unicità per le equazioni di Navier-Stokes. *Annali di Matematica Pura ed Applicata*, 48, 173–182.

Serrin, J. (1962). On the interior regularity of weak solutions of the Navier-Stokes equations. *Archive for Rational Mechanics and Analysis*, 9, 187–195.

Tao, T. (2016). Finite time blowup for an averaged three-dimensional Navier-Stokes equation. *Journal of the American Mathematical Society*, 29(3), 601–674.

Wyld, H. W. (1961). Formulation of the theory of turbulence in an incompressible fluid. *Annals of Physics*, 14, 143–165.

Yeung, P. K., Zhai, X. M., & Sreenivasan, K. R. (2015). Extreme events in computational turbulence. *Proceedings of the National Academy of Sciences*, 112(41), 12633–12638.

Anselmet, F., Gagne, Y., Hopfinger, E. J., & Antonia, R. A. (1984). High-order velocity structure functions in turbulent shear flows. *Journal of Fluid Mechanics*, 140, 63–89.

Benzi, R., Ciliberto, S., Tripiccione, R., Baudet, C., Massaioli, F., & Succi, S. (1993). Extended self-similarity in turbulent flows. *Physical Review E*, 48(1), R29–R32.

Gledzer, E. B. (1973). System of hydrodynamic type admitting two quadratic integrals of motion. *Soviet Physics Doklady*, 18, 216–217.

Kolmogorov, A. N. (1962). A refinement of previous hypotheses concerning the local structure of turbulence in a viscous incompressible fluid at high Reynolds number. *Journal of Fluid Mechanics*, 13, 82–85.

Kraichnan, R. H. (1959). The structure of isotropic turbulence at very high Reynolds numbers. *Journal of Fluid Mechanics*, 5(4), 497–543.

Ohkitani, K., & Yamada, M. (1989). Temporal intermittency in the energy cascade process and local Lyapunov analysis in fully-developed model turbulence. *Progress of Theoretical Physics*, 81(2), 329–341.

Richardson, L. F. (1922). *Weather Prediction by Numerical Process*. Cambridge University Press.

She, Z.-S., & Leveque, E. (1994). Universal scaling laws in fully developed turbulence. *Physical Review Letters*, 72(3), 336–339.

Sreenivasan, K. R., & Kailasnath, P. (1993). An update on the intermittency exponent in turbulence. *Physics of Fluids A*, 5(2), 512–514.

Constantin, P., E, W., & Titi, E. S. (1994). Onsager's conjecture on the energy conservation for solutions of Euler's equation. *Communications in Mathematical Physics*, 165(1), 207–209.

Foias, C., & Temam, R. (1989). Gevrey class regularity for the solutions of the Navier-Stokes equations. *Journal of Functional Analysis*, 87(2), 359–369.

Li, Y., Perlman, E., Wan, M., Yang, Y., Meneveau, C., Burns, R., Chen, S., Szalay, A., & Eyink, G. (2008). A public turbulence database cluster and applications to study Lagrangian evolution of velocity increments in turbulence. *Journal of Turbulence*, 9(31), 1–29.

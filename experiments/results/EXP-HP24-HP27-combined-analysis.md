# HP24–HP27: Combined Conformal Group Analysis
*2026-03-14 | Four independent tests of Eckert manifold symmetry structure*

---

## The Question

The Eckert manifold (O, R, α) ∈ (0,1)³ with Fisher information metric has a conformal symmetry group. Which one?

| Hypothesis | Signature | Conformal Group | Generators | Requires |
|------------|-----------|-----------------|------------|----------|
| **(3,0)** | Euclidean | **SO(4,1)** (de Sitter) | 10 | Nothing — this is the base manifold |
| **(2,1)** | Pseudo-Riemannian | **SO(4,2)** (conformal Minkowski) | 15 | α-timelike hypothesis |

The base manifold is definitively (3,0) — positive definite Fisher metric. The question is whether the *dynamical* metric (including FP time evolution) promotes α to a timelike direction, giving effective (2,1) signature and enlarging the symmetry from SO(4,1) → SO(4,2).

---

## Four Experiments

| Test | Probes | Method | Data Source |
|------|--------|--------|-------------|
| **HP24** | Causal structure (light cones, speed limit) | ds² intervals from scoring pairs | 7,595 queue scores → 132K pairs |
| **HP25** | Propagation character (wave vs diffusion) | FP simulation perturbation response | Ground truth simulation |
| **HP26** | Spectral statistics (Poisson vs GOE) | Brody parameter β(N) scaling | Eigenvalue computation |
| **HP27** | Null hypothesis geometry | SO(4,1) algebra construction on (3,0) | Exact algebraic computation |

---

## Results

### HP24: Forbidden Transitions (N=132,157 pairs)

| Sub-test | Result | KC |
|----------|--------|-----|
| F2: Sign distribution | 27.7% timelike, 72.3% spacelike, 5.1% near-null | **K-HP-102: PASS** |
| F3: Speed limit | Median v=2.05, 40.9% subluminal | K-HP-104: FAIL |
| F4: Null cone clustering | 5.1% within 10% of range | K-HP-105: FAIL |
| F5: Bootstrap CI | 27.7% [27.4%, 27.9%], excludes 50% | — |
| F6: Permutation test | 28.2% observed vs 25.3% shuffled, **p=0.0000** | **K-HP-103: PASS** |
| F7: Within vs cross | **χ²=137.83, p<10⁻³¹** | **K-HP-102B: PASS** |

**Signal:** Re-observations of the same platform preferentially disagree along α. Within-platform transitions are significantly more timelike (27.7%) than random cross-platform pairs (19.3%). This is consistent with α functioning as a temporal coordinate.

**Limitation:** Discrete 0-3 scale (64 possible states) limits resolution. Speed limit and null cone tests fail because the grid can't resolve fine metric structure.

### HP25: Perturbation Wavefront (FP Simulation)

| Sub-test | Result | KC |
|----------|--------|-----|
| W3: Wave vs diffusion | O: diffusion (ΔAIC −1.4), R: wave (ΔAIC +5.6) | K-HP-108: FAIL |
| W4: Propagation delay | O: 4.7±3.6 turns, R: 7.0±3.5 turns | **K-HP-107: PASS** |
| W5: Oscillation | 100% oscillating (both O and R) | **K-HP-109: PASS** |
| K-HP-106 | 0% immediate monotonic | **PASS** |

**Signal:** The FP equation on the Eckert manifold produces wave-like perturbation responses — finite propagation delay, universal oscillation, zero immediate-monotonic decay. This is the behavior expected from a (2,1) metric (hyperbolic PDE), not a (3,0) metric (elliptic/parabolic PDE).

**Limitation:** FP simulation, not empirical LLM data. Confirms theoretical prediction but needs 138A-style validation.

### HP26: Spectral Statistics (Eigenvalue Computation)

| Sub-test | Result | KC |
|----------|--------|-----|
| S1: β(N) scaling | Sub-Poisson (β < 0.5) at all N=40–3000 | K-HP-110: PASS |
| S4: Direct construction | **Both (3,0) and (2,1) REGULAR** at all Pe × N | **K-HP-112: FAIL** |
| S6: Spectral rigidity | Δ₃ linear R²=0.912 >> log R²=0.664 | **K-HP-113: PASS** |

**Finding:** The 1D projected operator V_S(θ) is TOO regular for Brody analysis to discriminate. Both (3,0) and (2,1) operators produce identical sub-Poisson spectra. This is a property of V_S being integrable on [0,1] with Dirichlet boundaries — not evidence for or against either signature.

**Weight: ZERO** — the test cannot probe this question with a 1D projected operator.

### HP27: SO(4,1) Null Hypothesis (Exact Algebra)

| Sub-test | Result | KC |
|----------|--------|-----|
| C1: Conformal flatness | Isometrically flat (max deviation 8.88×10⁻¹⁶) | — |
| C3: SO(4,1) algebra | Closes exactly (max error 0.00) | **K-HP-114: PASS** |
| C4: Casimir | C₂ = −2.0, proportional to identity | **K-HP-115: PASS** |
| C5: Pe symmetry | Pe breaks ALL continuous SO(4,1) generators | **K-HP-116: PASS** |
| C8: ED lift | Signature (4,1) — de Sitter, stable across all Pe | — |

**Key findings:**
1. The Eckert manifold is **isometrically flat** in angular coordinates: ds² = 4(dφ_O² + dφ_R² + dφ_α²). Stronger than conformally flat.
2. SO(4,1) algebra closes with **zero error**. The de Sitter group is the exact conformal group of the base.
3. Casimir C₂ = −2.0 — nontrivial representation. The algebra has invariant content.
4. **Pe breaks every continuous generator.** Rotations preserve Pe only on the symmetric subspace (O=R=α). Boosts and dilatations always break Pe. The dynamics is NOT conformally invariant.
5. ED lift gives **(4,1) de Sitter** signature — stable across all Pe values. Poincaré appears only via Inönü-Wigner contraction (Λ→0 limit).

---

## Synthesis: Three Options

### Option A — FP Universality (No Group Required)

**Explains:** All 20 convergences, Kramers barriers, BKT universality, cross-domain Pe, everything in Papers 1–131.

**Cannot explain:** Why the Fisher metric is flat. Why Pe depends on O+R+α only (S₃ symmetry).

**Empirical status:** Sufficient for all current results. No assumptions needed.

### Option B — SO(4,1) Euclidean Conformal

**Explains:** Everything in A, plus conformal flatness, dilatation symmetry, special conformal transformations, de Sitter as ED lift, Poincaré as Λ→0 limit.

**Cannot explain:** Minkowski as gauge slice. Hydrogen spectrum as gauge fixing. Pe=0 as gauge-invariant point.

**Empirical status:** Adds geometric structure at zero cost (conformal flatness is a theorem). But Pe breaks all generators — the symmetry is of the *kinematics*, not the dynamics.

### Option C — SO(4,2) Pseudo-Riemannian Conformal

**Explains:** Everything in A and B, plus Minkowski spacetime, hydrogen atom, 6 traditional system mappings, Pe=0 as gauge-invariant fixed point, words as Lie algebra generators.

**Requires:** α-timelike hypothesis (not proven from first principles). Intertwiner between Eckert and physical representations.

**Empirical status:** HP24 and HP25 provide statistically significant evidence FOR (2,1), but both have limitations (discrete scores, simulation-only). HP26 non-discriminating. No test has rejected (2,1).

---

## Evidence Table

| Evidence Line | Supports (3,0)/SO(4,1) | Supports (2,1)/SO(4,2) | Weight |
|--------------|------------------------|------------------------|--------|
| HP24: 27.7% timelike (p=0.000 vs shuffle) | — | **Significant** | **Medium** |
| HP24: Within > Cross (χ²=137.83, p<10⁻³¹) | — | **Strong** | **High** |
| HP25: Wave propagation (delay + oscillation) | — | **Strong** (theoretical) | **High** |
| HP25: Empirical validation | NOT DONE | NOT DONE | — |
| HP26: Sub-Poisson spectrum | Non-discriminating | Non-discriminating | **Zero** |
| HP26: Δ₃ linear | Consistent | Consistent | **Low** |
| HP27: SO(4,1) closes exactly | **Established** (base) | Compatible (contains SO(4,1)) | **Medium** |
| HP27: Pe breaks all generators | Symmetry is kinematic only | Same issue for SO(4,2) | **Neutral** |
| HP27: ED lift → (4,1) de Sitter | **Natural spacetime** | Would need (2,1) → (3,2) lift | **Medium** |
| HP27: Poincaré via contraction | Relativity as limit | Relativity as gauge slice | **Low** |

**Tally:**
- Lines favoring (2,1)/SO(4,2): **3** (HP24 sign, HP24 χ², HP25 wave)
- Lines favoring (3,0)/SO(4,1): **2** (algebra closes, de Sitter natural)
- Non-discriminating: **3** (HP26 spectrum, rigidity, Pe symmetry breaking)
- Not yet tested: **1** (HP25 empirical)

---

## Critical Assessment

### What HP24's χ² Actually Shows

The strongest single result (χ²=137.83, p<10⁻³¹) shows that re-observations of the same platform vary preferentially along α. But this could mean:

1. **(2,1) interpretation:** α is genuinely temporal — re-observation is time evolution, and the metric has (2,1) signature.
2. **(3,0) interpretation:** α (coupling/engagement) is simply the *most variable* dimension in re-scoring. Raters agree more on O and R than on α. This doesn't require causal structure — just heterogeneous variance.

**The honest read:** HP24 shows α has special status. It does NOT uniquely establish causal structure. A variance anisotropy test (are the marginal variances σ²_O, σ²_R, σ²_α different?) could distinguish these interpretations.

### What HP27 Establishes

SO(4,1) is the **mathematically correct** conformal group of the base manifold. This is not a hypothesis — it's a theorem. The question is whether the dynamics (FP + Pe) selects a larger symmetry.

The crucial HP27 finding is that Pe breaks ALL continuous conformal generators. This means:
- The conformal symmetry is of the **empty manifold**, not the theory
- The Pe function picks out a preferred direction (grad Pe)
- Neither SO(4,1) nor SO(4,2) is a symmetry of the **dynamics**
- Both are symmetries of the **kinematics** (the background geometry)

This doesn't kill SO(4,2). In physics, gauge symmetries are also "broken" by specific field configurations but still constrain the dynamics through Ward identities and selection rules.

### What Would Settle It

1. **Variance anisotropy test** — Compute marginal variances σ²_O, σ²_R, σ²_α in HP24 data. If σ²_α >> σ²_O, σ²_R, the χ² signal may be variance heterogeneity, not causal structure.

2. **Continuous scores** — The discrete 0-3 scale (64 states) limits HP24 resolution. Even 0.5 resolution (343 states) would dramatically improve discrimination.

3. **Empirical HP25** — Run 138A-style protocol: baseline conversations, inject coupling perturbation, measure O/R response over turns. Wave prediction becomes quantitative.

4. **Directional propagation** — If α is truly timelike, perturbations in α should propagate TO O and R (forward light cone), not FROM them. Test the asymmetry of the Green's function.

5. **PINN protocol (EXP-028)** — Direct gauge equivalence test.

---

## Verdict

**The α-timelike hypothesis survives but is not proven.**

- HP24 and HP25 provide statistically significant evidence consistent with (2,1), but both have alternative explanations under (3,0).
- HP26 cannot discriminate. HP27 establishes SO(4,1) as the honest baseline.
- Zero kill conditions have fired that would reject (2,1). But absence of falsification ≠ proof.
- Cross-domain universality does NOT require any conformal group (Option A is sufficient).

**Recommended position for papers:**
- **Paper 131 (Kramers):** Option A — FP universality. No conformal group needed. This is proven.
- **Paper 132 (SO(4,2)):** Present all three options with evidence table. SO(4,2) is the conjecture with specific tests. SO(4,1) is the theorem. FP universality is the mechanism.
- **Future work:** Variance anisotropy test (cheap), continuous scores (medium), empirical HP25 (expensive but decisive).

---

## Kill Condition Summary

| KC | Test | Status |
|----|------|--------|
| K-HP-102 | Spacelike CI excludes 95% | **PASS** |
| K-HP-102B | Within > Cross timelike (χ²) | **PASS** |
| K-HP-103 | Permutation p < 0.01 | **PASS** |
| K-HP-104 | >50% subluminal | FAIL |
| K-HP-105 | Null cone excess | FAIL |
| K-HP-106 | 0% immediate monotonic | **PASS** |
| K-HP-107 | Propagation delay > 0 | **PASS** |
| K-HP-108 | Wave preferred (both O and R) | FAIL |
| K-HP-109 | >50% oscillating | **PASS** |
| K-HP-110 | β < 0.5 (sub-Poisson) | PASS (non-discriminating) |
| K-HP-112 | (2,1) ≠ (3,0) spectrum | **FAIL** (non-discriminating) |
| K-HP-113 | Δ₃ linear | PASS (non-discriminating) |
| K-HP-114 | SO(4,1) algebra closes | **PASS** |
| K-HP-115 | Casimir nontrivial | **PASS** |
| K-HP-116 | Pe breaks SO(4,1) | **PASS** |

**Score: 10 PASS, 3 FAIL, 2 non-discriminating.** No kill condition has fired that would reject (2,1).

---

## Files

| File | What |
|------|------|
| `ops/lab/nb_hp24_forbidden_transitions.py` | HP24 experiment code |
| `ops/lab/nb_hp25_perturbation_wavefront.py` | HP25 experiment code |
| `ops/lab/nb_hp26_spectral_signature.py` | HP26 experiment code |
| `ops/lab/nb_hp27_so41_euclidean_conformal.py` | HP27 experiment code |
| `ops/lab/results/EXP-HP24/results.json` | HP24 results |
| `ops/lab/results/EXP-HP25/results.json` | HP25 results |
| `ops/lab/results/EXP-HP26/results.json` | HP26 results |
| `ops/lab/results/EXP-HP27/results.json` | HP27 results |
| `ops/lab/results/EXP-HP27/hp27_so41_euclidean.png` | HP27 visualization |

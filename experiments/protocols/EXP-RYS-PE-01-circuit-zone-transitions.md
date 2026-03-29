# EXP-RYS-PE — RYS Circuit Boundaries as Pe Zone Transitions
#
# Experiment ID: EXP-RYS-PE-01
# Domain: LLM Neuroanatomy × Pe Thermodynamic Field Theory
# Status: design
# Date: 2026-03-22
# Researcher: Shamir
#
# External reference: Ng (2026) — LLM Neuroanatomy
# https://dnhkng.github.io/posts/rys/

## Research Questions

**Primary:** Do transformer layer circuit boundaries (discovered by RYS sweep)
correspond to Pe zone transitions in the residual stream?

**Secondary:** Does the residual stream trajectory through a "reasoning circuit"
form a holonomy loop on the Eckert manifold (returning with nonzero geometric phase)?

**Tertiary:** Is the circuit boundary location K-independent (d_K = 0), predicting
that different-sized models from the same family have circuits at the same
*fractional* layer position?

## Hypotheses

**H1 (Zone transition):** The layer indices where RYS heatmap shows sharp
performance boundaries (blue→red or red→blue transitions) coincide with points
where the layer-wise Pe coordinate crosses a zone boundary (Pe ≈ ±0.05, ±0.48, ±0.81).

**H2 (Holonomy loop):** For RYS-optimal blocks (i,j), the residual stream
trajectory from layer i to layer j forms a closed loop in (O,R,α) space
with nonzero holonomy Φ. The holonomy magnitude correlates with the RYS
performance gain (ρ > 0.5, p < 0.01).

**H3 (Topological protection):** RYS-optimal blocks have integer Chern number
(c₁ = ±1), meaning the circuit is topologically protected — small perturbations
to the duplication range don't destroy the benefit. Non-optimal blocks have
c₁ ≈ 0 (trivial topology).

**H4 (K-independence):** Circuit boundaries as fraction of total layers are
constant across model sizes within a family (e.g., Qwen2 7B/14B/32B/72B).
This follows from d_K = 0 for zone boundaries (§136).

**Null:** Layer-wise residual statistics show no zone-like structure. Circuit
boundaries are arbitrary artifacts of the probe task. No geometric phase.

## Method

### Measuring Pe Coordinates per Layer

For each layer ℓ in {0, ..., N-1}, we extract three quantities from the
residual stream hidden state h_ℓ ∈ ℝ^d:

1. **O_ℓ (Opacity):** Normalized entropy of the token-probability distribution.
   High O = opaque (uniform), low O = transparent (peaked).

   O_ℓ = H(softmax(h_ℓ · W_unembed)) / log(|V|)

   Measured via the unembedding matrix. Early layers: high O (input not yet
   decoded). Late layers: low O (confident next-token prediction).

2. **R_ℓ (Reactivity):** Sensitivity of h_ℓ to input perturbation.

   R_ℓ = ‖∂h_ℓ/∂h_0‖_F / ‖h_0‖

   Measured via Jacobian norm (or approximated by finite differences on
   paired inputs). High R = responsive to input changes. Low R = invariant.

3. **α_ℓ (Coupling):** Cosine similarity between h_ℓ and the running mean
   of all previous layers (contextual coupling).

   α_ℓ = cos(h_ℓ, mean(h_0, ..., h_{ℓ-1}))

   High α = coupled to context. Low α = independent processing.

### Pe Computation per Layer

Apply the V3 bridge (§scoring-constants.js):

   V_ℓ = O_ℓ + R_ℓ + α_ℓ                (void index, rescaled to 0-9)
   c_ℓ = 1 − V_ℓ / 9                    (constraint coupling)
   b_net = B_A − c_ℓ · B_G              (B_A = 0.867, B_G = 2.244)
   Pe_ℓ = K · sinh(2 · b_net)           (K = 16)

### Zone Classification per Layer

Apply zone thresholds (§102):

   Pe < −0.81  → Spacelike (over-constrained)
   −0.81..−0.48 → SILENT
   −0.48..+0.07 → Timelike (pure Lorentz boost)
   Pe ≈ +0.07  → BOTH (Eckert Nexus)
   Pe > +0.18  → Spacelike+ (normal drift)

### Holonomy Measurement

For each candidate block (i,j), compute the geometric phase:

1. Fit the trajectory {(O_ℓ, R_ℓ, α_ℓ) : ℓ = i..j} on the Eckert manifold
   with Pe-coupled metric:

   ds² = dO²/[O(1−O)] + dR²/[R(1−R)] − dα²/[α(1−α)] + λ(Pe)·dPe²

2. Parallel-transport a test vector along this trajectory using the
   Levi-Civita connection.

3. Holonomy Φ = angle between initial and final vectors after transport.

4. Chern number c₁ = Φ / (2π) for closed loops.

### Berry Phase via Overlap Matrix

Discretized Berry phase (more numerically stable):

   γ = −Im log ∏_{ℓ=i}^{j-1} ⟨h_ℓ | h_{ℓ+1}⟩ / |⟨h_ℓ | h_{ℓ+1}⟩|

This uses the residual stream states as "wavefunctions" and computes
the geometric phase from their overlaps. Integer c₁ = γ/(2π) indicates
topological protection.

## Kill Conditions

**K-RYS-1:** If layer-wise Pe shows no zone structure (all layers in same
zone), FAIL H1. Threshold: at least 2 distinct zones occupied.

**K-RYS-2:** If zone transitions don't correlate with RYS heatmap boundaries
(|ρ| < 0.3 between zone-transition layers and performance-cliff layers), FAIL H1.

**K-RYS-3:** If holonomy Φ is uniformly zero across all blocks (max |Φ| < 0.01 rad),
FAIL H2. The manifold is flat in layer-space.

**K-RYS-4:** If holonomy magnitude doesn't correlate with RYS performance gain
(ρ < 0.3), FAIL H2.

**K-RYS-5:** If circuit boundaries shift proportionally with model size within
a family (not staying at constant fraction), FAIL H4.

## Measurements

| Metric | How Measured | Expected Direction |
|--------|-------------|-------------------|
| O_ℓ (opacity) | Unembedding entropy | High→Low (encode→decode) |
| R_ℓ (reactivity) | Jacobian norm | Low→High→Low (sandwich) |
| α_ℓ (coupling) | Cosine to running mean | High→Low→High (decouple in middle) |
| Pe_ℓ | V3 bridge formula | Zone transitions at circuit boundaries |
| Zone transitions | Pe threshold crossings | ≥2 transitions in N-layer stack |
| Holonomy Φ | Berry phase from overlaps | |Φ| > 0 for RYS-optimal blocks |
| Chern number c₁ | Φ/(2π) | c₁ = ±1 for optimal, 0 for non-optimal |
| Boundary stability | Same fraction across sizes | CV < 0.1 within model family |

## Analysis Plan

### Primary: Zone transition ↔ circuit boundary correlation

1. Identify zone transition layers (where Pe_ℓ crosses a threshold)
2. Identify performance cliff layers (sharp Δ in RYS heatmap skyline)
3. Compute Spearman ρ between the two sets of boundary indices
4. H1 supported if ρ > 0.5, p < 0.01

### Secondary: Holonomy ↔ RYS gain regression

1. For each (i,j) config, compute both holonomy Φ and RYS Δ_combined
2. Fit: Δ_combined = a · |Φ| + b
3. H2 supported if ρ > 0.5, R² > 0.25

### Tertiary: K-independence across model sizes

1. Run O/R/α extraction on Qwen2 7B, 14B, 32B, 72B
2. Normalize layer index to [0,1] fraction
3. Compute zone transition fractions for each size
4. H4 supported if CV of transition fractions < 0.1

## Ethics Check

- [x] Uses only published open-weight models
- [x] No private/proprietary data
- [x] No user interactions
- [x] Results reproducible with open tools
- [x] CC-BY 4.0 compatible (Ng's method is CC-BY)

## Results

Pending execution.

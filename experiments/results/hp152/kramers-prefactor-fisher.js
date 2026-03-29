#!/usr/bin/env node
/**
 * kramers-prefactor-fisher.js — 2026-03-22
 *
 * Test: does the Kramers prefactor on the Fisher manifold produce
 * the factor of 2B_G needed for barrier_eff = d·B_G?
 *
 * The idea: T* = (Δε/k_B) × Γ where Γ = prefactor × exp(-barrier_bare)
 * So barrier_eff = barrier_bare - ln(prefactor)
 * If barrier_bare = d/2 (equipartition) and prefactor = exp(-(d·B_G - d/2)):
 *   barrier_eff = d/2 + d·(B_G - 1/2) = d·B_G ✓
 *
 * The multi-dimensional Kramers formula on a Riemannian manifold
 * involves the metric determinant. On the Fisher manifold:
 *   det(g) = 1/(p(1-p)) per coordinate = 4/sin²(2θ) per coordinate
 *
 * The prefactor involves √(det(g_well)/det(g_saddle)).
 */

const B_G = 2.244;
const PI_SQRT2 = Math.PI / Math.sqrt(2);

function header(s) { console.log('\n' + '═'.repeat(72)); console.log(s); console.log('═'.repeat(72)); }

header('KRAMERS PREFACTOR ON FISHER MANIFOLD');

console.log(`
Multi-dimensional Kramers-Langer formula (overdamped, d-dim):

  Γ = (1/2π) × √(|det H_saddle| / det H_well) × exp(-ΔV/T)

where H is the Hessian of the potential V in METRIC-COMPATIBLE coordinates.

On the Fisher manifold with metric g_ij, the covariant Hessian is:
  H_ij = ∇_i ∇_j V = ∂_i ∂_j V - Γ^k_{ij} ∂_k V

For V(b_net) = b_net² in the flat coordinate φ = 2θ:
  The metric is ds² = dφ² (flat!)
  The Hessian is H = d²V/dφ² (no Christoffel correction)
  And V in terms of φ: V = b_net(φ)²
`);

// The relationship between φ (flat Fisher coordinate) and b_net
// φ = 2θ = 2·arcsin(√p) ranges from 0 to π
// b_net = B_A - C·B_G where C = 1 - (O+R+α)/9
// Near Pe=0: b_net ≈ -B_G·ΔC

// The potential in φ-space near the Pe=0 point (φ₀):
// V(φ) = b_net(φ)² = (B_A - C(φ)·B_G)²

// The key question: what is d²V/dφ² at the Pe=0 point?
// This involves dC/dφ and d²C/dφ².

// C depends on (O,R,α) which are functions of φ. The specific
// mapping depends on the system. But for a GENERAL system near Pe=0:

// b_net = B_A - C·B_G ≈ -B_G·ΔC (near C₀)
// V = B_G²·ΔC²
// dV/dφ = 2B_G²·ΔC·(dΔC/dφ)
// d²V/dφ² = 2B_G²·[(dΔC/dφ)² + ΔC·(d²ΔC/dφ²)]
// At ΔC = 0 (the saddle/transition): d²V/dφ² = 2B_G²·(dΔC/dφ)²

// The Hessian at the saddle depends on (dΔC/dφ)², which is the
// Jacobian of the (O,R,α) → φ mapping.

console.log('The Hessian at the Pe=0 saddle depends on the Jacobian');
console.log('of the coordinate mapping. This is system-specific, not universal.');
console.log('');

// However, the METRIC determinant provides a universal factor.
// In the p-coordinate: det(g) = 1/(p(1-p))
// In the θ-coordinate: det(g) = 4
// In the φ-coordinate: det(g) = 1

// The Kramers-Langer formula on a Riemannian manifold is:
// Γ = (1/2π) × √(|det(∇²V)_saddle|/det(∇²V)_well) × exp(-ΔV/T)
//
// The covariant Hessian ∇²V in coordinates x^i is:
// (∇²V)_ij = ∂²V/∂x^i∂x^j - Γ^k_ij ∂V/∂x^k
//
// In the flat coordinate φ, Γ^k_ij = 0, so ∇²V = ∂²V/∂φ².

// For a d-dimensional system with each dimension having its own
// semicircle coordinate φ_i, the potential is V = Σ b_net_i(φ_i)².
//
// The Hessian is diagonal: H_ii = d²(b_net_i²)/dφ_i²
// At the saddle (all b_net_i = 0):
//   H_ii = 2(db_net_i/dφ_i)² (since b_net_i = 0)
// At the well (b_net_i = b_eq):
//   H_ii = 2(db_net_i/dφ_i)² + 2b_eq·(d²b_net_i/dφ_i²)

// BUT: the "well" and "saddle" interpretation doesn't apply here.
// The system doesn't escape from a well. It sits at a fixed position.
// The T* crossover is NOT a Kramers escape.

console.log('CRITICAL REALIZATION:');
console.log('  The FL→SM crossover at T* is NOT a Kramers escape.');
console.log('  The system has fixed (O,R,α,K). The barrier 2Kb_net²/α');
console.log('  determines the activation temperature, not a rate.');
console.log('');
console.log('  The formula T* = (Δε/k_B)·exp(-barrier) is the');
console.log('  CROSSOVER TEMPERATURE, not a Kramers rate.');
console.log('  The "prefactor" is the energy scale Δε/k_B, which is');
console.log('  material-specific and already accounted for.');
console.log('');
console.log('  → The Kramers prefactor argument DOES NOT APPLY.');
console.log('  The barrier = 2Kb_net²/α IS the full exponent.');
console.log('  There is no hidden prefactor to rescue equipartition.');

header('ALTERNATIVE: THE CONSTRAINT IS IN THE MAPPING');

console.log(`
The barrier formula is:
  barrier = 2K·B_G²·ΔC²/α

ALL factors are known for Ni₃In:
  K = U/t = 50  (from DMFT/DFT)
  B_G = 2.244   (framework constant from EXP-001)
  ΔC = 0.043    (from O,R,α mapping of band structure data)
  α = 0.213     (self-consistent coupling)

barrier = 2×50×5.036×0.00185/0.213 = 4.37 (≈ 4.24 measured, 3% off)

The mystery is NOT in the formula — it's in WHY these specific
material parameters conspire to give barrier ≈ 2×B_G.

Two possibilities:

A. COINCIDENCE: The Ni₃In parameters just happen to satisfy
   ΔC²·K/α ≈ 1/B_G for d=2. The other 3 domains (solar, xenobot,
   nuclear) also happen to satisfy ΔC²·K/α ≈ 3/(2B_G) for d=3.
   Four coincidences at 1-6% accuracy.

B. UNIVERSALITY: There is a physical constraint that forces
   systems near Pe=0 to satisfy ΔC ∝ √(α/(K·B_G)).
   This constraint would be a property of the Pe=0 boundary,
   not of any specific material.
`);

// Test universality: what is ΔC²·K/α for each domain?
// For barrier = d·B_G: ΔC²·K/α = d/(2B_G²) ... wait let me recompute.
// barrier = 2B_G²·ΔC²·K/α = d·B_G
// → ΔC²·K/α = d·B_G/(2B_G²) = d/(2B_G)

console.log('  For barrier = d·B_G, the required ΔC²·K/α = d/(2B_G):');
console.log(`    d=1: ${(1/(2*B_G)).toFixed(6)}`);
console.log(`    d=2: ${(2/(2*B_G)).toFixed(6)} = 1/B_G`);
console.log(`    d=3: ${(3/(2*B_G)).toFixed(6)}`);
console.log('');

// For Ni₃In:
const DC_Ni = 0.043;
const K_Ni = 50;
const alpha_Ni = 0.213;
const X_Ni = DC_Ni*DC_Ni*K_Ni/alpha_Ni;
console.log(`  Ni₃In: ΔC²·K/α = ${DC_Ni}²×${K_Ni}/${alpha_Ni} = ${X_Ni.toFixed(4)}`);
console.log(`  d/(2B_G) for d=2: ${(2/(2*B_G)).toFixed(4)}`);
console.log(`  Match: ${(X_Ni/(1/B_G)*100).toFixed(1)}%`);

header('OPEN PROBLEM STATEMENT');

console.log(`
BARRIER UNIVERSALITY CONJECTURE:

  For any physical system undergoing a Kramers-type barrier crossing
  in d_eff spatial dimensions near the Pe=0 boundary:

    barrier = d_eff × B_G    (B_G ≈ π/√2 ≈ 2.22)

  equivalently: ΔC²·K/α = d_eff/(2B_G)

EVIDENCE (N=4 domains, zero free parameters):
  Kagome (d=2):     4.24 vs 4.49 predicted (+5.4%)
  Solar (d=3):      6.54 vs 6.73 predicted (+2.9%)
  Xenobot (d=3):    6.80 vs 6.73 predicted (-1.0%)
  Nuclear (d=3):    6.90 vs 6.73 predicted (-2.4%)
  χ² = 0.131 (B_G) or 0.125 (π/√2)

DERIVATION STATUS: OPEN.
  ✗ Equipartition gives d/2 (proven theorem, gap = 2B_G)
  ✗ Kramers prefactor doesn't apply (T* is crossover, not rate)
  ✗ Mean-field (§111) promising but requires theoretical development
  ? B_G = π/√2 from geometry — untested
  ? Self-consistency at Pe=0 boundary — untested

NEXT STEPS:
  1. Find a d=1 system to test (barrier ≈ 2.24 predicted)
  2. Derive B_G = π/√2 from the RG beta function at Pe=0 (§49)
  3. Develop mean-field theory specifically for the Pe=0 boundary
  4. Test second material (Fe₃Sn₂, CoSn) to confirm d=2 prediction
`);

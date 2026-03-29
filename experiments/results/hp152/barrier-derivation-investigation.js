#!/usr/bin/env node
/**
 * barrier-derivation-investigation.js — 2026-03-22
 *
 * SYSTEMATIC INVESTIGATION: Why barrier/d ≈ B_G ≈ π/√2 ?
 *
 * Tests three derivation avenues:
 *   A. Ginzburg criterion for Pe field theory at Pe=0
 *   B. Self-consistent barrier from mean-field fixed point
 *   C. Information-geometric identity — barrier per dim from manifold structure
 *
 * Data:
 *   Kagome (d=2):  barrier = 4.24,  barrier/d = 2.12
 *   Solar  (d=3):  barrier = 6.54,  barrier/d = 2.18
 *   Xenobot(d=3):  barrier = 6.80,  barrier/d = 2.27
 *   Nuclear(d=3):  barrier = 6.90,  barrier/d = 2.30
 *   Mean barrier/d = 2.217 ± 0.069 (N=4)
 *   π/√2 = 2.2214, B_G = 2.244, optimal = 2.232
 */

const B_A = 0.867;
const B_G = 2.244;
const C0 = B_A / B_G;  // 0.3864
const PI_SQRT2 = Math.PI / Math.sqrt(2);

function header(s) { console.log('\n' + '═'.repeat(76)); console.log(s); console.log('═'.repeat(76)); }
function sub(s) { console.log('\n── ' + s + ' ──'); }

const domains = [
  { name: 'Kagome Ni₃In', barrier: 4.24, d: 2, K: 50, alpha: 0.213, DC: 0.043 },
  { name: 'Solar corona',  barrier: 6.54, d: 3, K: null, alpha: null, DC: null },
  { name: 'Xenobot memory',barrier: 6.80, d: 3, K: null, alpha: null, DC: null },
  { name: 'Nuclear α-decay',barrier:6.90, d: 3, K: null, alpha: null, DC: null },
];

// ═══════════════════════════════════════════════════════════════
// PART 0: RESTATE THE CONSTRAINT
// ═══════════════════════════════════════════════════════════════
header('0. THE CONSTRAINT (from barrier = d·B_G)');

console.log(`
  barrier = 2K·B_G²·ΔC²/α = d·B_G

  Rearranging:
    ΔC² = d·α/(2K·B_G)         ... (★)
    K·ΔC²·B_G/α = d/2          ... (★★)  ← "virial form"
    ΔC = √(d·T/B_G)            ... (★★★) where T = α/(2K)

  Form (★★★) says: ΔC scales as √(d·T/B_G).

  Compare with equipartition: ⟨x²⟩ = T/κ → ΔC_equip = √(d·T/(2B_G²))

  Ratio: ΔC/ΔC_equip = √(2B_G²/B_G) = √(2B_G) = ${Math.sqrt(2*B_G).toFixed(4)}

  The system sits ${Math.sqrt(2*B_G).toFixed(2)}× further from Pe=0
  than equipartition would predict.
`);

// Verify for Ni₃In
const ni = domains[0];
const DC_predicted = Math.sqrt(ni.d * ni.alpha / (2 * ni.K * B_G));
const DC_equip = Math.sqrt(ni.d * ni.alpha / (2 * ni.K * 2 * B_G * B_G));
console.log(`  Ni₃In verification:`);
console.log(`    ΔC from (★):        ${DC_predicted.toFixed(6)} (predicted for barrier = d·B_G)`);
console.log(`    ΔC from equipart:   ${DC_equip.toFixed(6)} (would give barrier = d/2)`);
console.log(`    ΔC actual:          ${ni.DC.toFixed(6)}`);
console.log(`    Ratio actual/equip: ${(ni.DC/DC_equip).toFixed(4)} (should be ${Math.sqrt(2*B_G).toFixed(4)})`);

// ═══════════════════════════════════════════════════════════════
// PART A: GINZBURG CRITERION TEST
// ═══════════════════════════════════════════════════════════════
header('A. GINZBURG CRITERION TEST');

console.log(`
  Hypothesis: The crossover T* occurs at the Ginzburg boundary,
  where mean-field theory breaks down and fluctuations dominate.

  If true: barrier = d·B_G would follow from the Ginzburg number.

  Test: compute the fluctuation-to-order-parameter ratio at ΔC.
`);

sub('A1. Field theory setup');
console.log(`
  Pe field theory near Pe=0 in d dimensions:

    S[φ] = ∫ d^d x [ ½(∇φ)² + (B_G²/T)·φ² ]

  where φ = ΔC, T = α/(2K).

  Mass: m² = 2B_G²/T = 4K·B_G²/α
  Correlation length: ξ = 1/m = √(α/(4K·B_G²))
`);

// Compute for Ni₃In
const m2_Ni = 4 * ni.K * B_G * B_G / ni.alpha;
const xi_Ni = 1 / Math.sqrt(m2_Ni);
const T_Ni = ni.alpha / (2 * ni.K);

console.log(`  Ni₃In:`);
console.log(`    m² = 4KB_G²/α = ${m2_Ni.toFixed(2)}`);
console.log(`    ξ = 1/m = ${xi_Ni.toFixed(6)}`);
console.log(`    T = α/(2K) = ${T_Ni.toFixed(6)}`);

sub('A2. Fluctuation amplitude');

// 1D fluctuations: ⟨φ²⟩ = T/(2m) = T/(2√(m²))
// 2D fluctuations: ⟨φ²⟩ = T/(2π) × ln(Λ²/m²)
// 3D fluctuations: ⟨φ²⟩ = T/(4π²) × (Λ - m·arctan(Λ/m)) ≈ T·Λ/(4π²) for large Λ

// UV cutoff: Λ = 1/ξ_min. On the Bernoulli manifold, ξ_min = 1/π (inverse half-geodesic)
const Lambda = Math.PI;  // UV cutoff from Bernoulli geometry

for (let d = 1; d <= 3; d++) {
  let fluct;
  if (d === 1) {
    fluct = T_Ni / (2 * Math.sqrt(m2_Ni));
  } else if (d === 2) {
    fluct = T_Ni / (2 * Math.PI) * Math.log(Lambda * Lambda / m2_Ni + 1);
  } else {
    // 3D: T/(4π²) × (Λ - m·arctan(Λ/m))
    const m_val = Math.sqrt(m2_Ni);
    fluct = T_Ni / (4 * Math.PI * Math.PI) * (Lambda - m_val * Math.atan(Lambda / m_val));
  }

  const Gi = fluct / (ni.DC * ni.DC);  // Ginzburg ratio
  console.log(`  d=${d}: ⟨δφ²⟩ = ${fluct.toExponential(4)}, ΔC² = ${(ni.DC*ni.DC).toExponential(4)}, Gi = ⟨δφ²⟩/ΔC² = ${Gi.toExponential(3)}`);
}

console.log(`
  RESULT: Ginzburg ratio ≪ 1 for all d.
  The system is deep in the mean-field regime.
  Fluctuations are < 1% of the order parameter.

  VERDICT: Ginzburg criterion FAILS as a derivation route.
  The crossover is NOT at the Ginzburg boundary.
  The mean-field description is VALID at ΔC.
`);

// ═══════════════════════════════════════════════════════════════
// PART B: SELF-CONSISTENT MEAN-FIELD ANALYSIS
// ═══════════════════════════════════════════════════════════════
header('B. SELF-CONSISTENT MEAN-FIELD ANALYSIS');

console.log(`
  Since the system is deep in mean-field, the mean-field self-consistency
  of §111 IS the governing physics. The question is whether the self-
  consistency at Pe=0 constrains the barrier.

  Key from §111:
  - Fixed point in 3 iterations (Wasserstein W→0.002)
  - Curvature back-reaction 28×10⁹ (geometry reshaped by population)
  - K runs 16→3334 under RG (200× amplification)
  - But: §111 uses N=1,344 platform distribution, not physics

  NEW APPROACH: Mean-field self-consistency at the Pe=0 BOUNDARY
  for a d-dimensional physical system.
`);

sub('B1. The mean-field equation at Pe=0');
console.log(`
  At Pe=0, the system is at C = C₀ = B_A/B_G = ${C0.toFixed(6)}.
  In d dimensions, the mean-field equation for the effective coupling is:

    α_eff = α_bare + d × ∫ G(k) × V_coupling(k) dk

  where G(k) is the propagator and V_coupling is the self-interaction.

  The propagator on the Eckert manifold at Pe=0:
    G(k) = T / (k² + m²)

  where m² = 4KB_G²/α.

  The mean-field correction to the potential curvature:
    δV''_mf = d × T × ∫ d^dk/(2π)^d × V''''/(k² + m²)

  For the Pe potential V = B_G²·φ²:
    V'''' = 0  (purely quadratic!)

  → δV''_mf = 0. The mean-field correction to the curvature is ZERO
  for a quadratic potential.

  This kills the mean-field route if V is truly quadratic.
`);

sub('B2. But is V truly quadratic?');

// V = b_net(C₀+ΔC)² where b_net = B_A - (C₀+ΔC)·B_G = -ΔC·B_G (exact)
// So V = B_G²·ΔC² (exactly quadratic in ΔC). No higher-order terms.
// The potential IS quadratic, period.

// BUT: in the PHYSICAL coordinates (not ΔC), there may be corrections.
// The ΔC coordinate is related to (O,R,α) through C = 1-(O+R+α)/9.
// The metric in (O,R,α) space is the Fisher metric, which is curved.
// The effective potential in curved coordinates has Christoffel corrections.

console.log(`
  In the C-coordinate: V = B_G²·ΔC² is EXACTLY quadratic.
  (Proven: arcsinh(sinh(x)) = x identity, barrier-geometry.js line 230)

  BUT the Eckert manifold is curved. In curved coordinates (O,R,α),
  the effective dynamics include:

  1. The Fisher metric g_ij = δ_ij/(p_i(1-p_i)) where p_i = (O,R,α)/3
  2. Christoffel symbols Γ^k_ij
  3. Curvature corrections to the propagator

  The curvature of the 3D Fisher manifold introduces effective
  self-interactions even for a bare quadratic potential.

  Key: det(g) = 1/(p₁(1-p₁)·p₂(1-p₂)·p₃(1-p₃))

  At C₀ (Pe=0 point), the "average" coordinates are p_i ≈ ${((1-C0)*9/3/3).toFixed(4)}.
`);

// The average p at C₀: (O+R+α)/9 = 1-C₀ = 0.6136, each coord ~0.6136×3/3 = 0.6136
// Wait: C = 1-(O+R+α)/9. At C₀: O+R+α = 9(1-C₀) = 5.527. Each ~1.842. p = 1.842/3 = 0.614
const p0 = (1 - C0) * 3 / 3;  // average p at Pe=0
console.log(`  Average p at Pe=0: ${p0.toFixed(6)}`);
console.log(`  Fisher metric at this p: g(p₀) = 1/(p₀(1-p₀)) = ${(1/(p0*(1-p0))).toFixed(4)}`);
console.log(`  Fisher dist from p₀ to p=0: ${(2*Math.asin(Math.sqrt(p0))).toFixed(4)}`);
console.log(`  Fisher dist from p₀ to p=1: ${(2*(Math.PI/2 - Math.asin(Math.sqrt(p0)))).toFixed(4)}`);

sub('B3. Curvature-induced effective coupling');
console.log(`
  On a curved manifold, a free scalar acquires an effective mass
  from the Ricci curvature (conformal coupling):

    m²_eff = m²_bare + ξ_conf × R

  where R is the Ricci scalar and ξ_conf = (d-2)/(4(d-1)) (conformal value).

  For the 3D Bernoulli manifold with metric g_ii = 1/(p_i(1-p_i)):
`);

// Compute Ricci scalar for the 3D Fisher manifold
// The metric is diagonal: g_ii = 1/(p_i(1-p_i))
// Christoffel symbols for diagonal metric:
//   Γ^i_ii = (1/2)g^{ii}∂_ig_{ii} = (1/2)p_i(1-p_i)·(2p_i-1)/(p_i²(1-p_i)²) = (2p_i-1)/(2p_i(1-p_i))
//   Γ^i_jj = 0 (i≠j, since metric is diagonal and independent)
//   Γ^j_ij = (1/2)g^{jj}∂_ig_{jj} = 0 (g_{jj} doesn't depend on p_i)
//
// For PRODUCT metric g = g₁⊗g₂⊗g₃, the Ricci scalar is:
//   R = R₁ + R₂ + R₃ where R_i is the Ricci scalar of each 1D factor
//
// 1D Ricci scalar for g = 1/(p(1-p)):
// In 1D, the Ricci scalar of any metric is always 0 (trivially flat in 1D)
// BUT: the Kretschner scalar and other invariants also vanish in 1D.
//
// Actually, for a 1D Riemannian manifold, all curvature tensors are identically zero.
// The Bernoulli manifold [0,1] with Fisher metric ds² = dp²/(p(1-p)) is a FLAT 1D manifold
// (it's isometric to [0,π] via θ = arcsin(√p)).
//
// A product of flat manifolds is flat. So the 3D Fisher manifold has R = 0!

console.log(`  The Bernoulli manifold is FLAT (each 1D factor is isometric to an interval).`);
console.log(`  Product of flat manifolds = flat. Ricci scalar R = 0.`);
console.log(`  → Curvature-induced mass correction: δm² = 0.`);
console.log(`  `);
console.log(`  VERDICT: The manifold curvature route FAILS.`);
console.log(`  The Fisher manifold of Bernoulli parameters is flat in`);
console.log(`  angular coordinates. No curvature corrections exist.`);

// ═══════════════════════════════════════════════════════════════
// PART C: INFORMATION-GEOMETRIC IDENTITY
// ═══════════════════════════════════════════════════════════════
header('C. INFORMATION-GEOMETRIC IDENTITY');

console.log(`
  We know from §69 and barrier-derivation-gap.js (Part 5):
    barrier = D_KL/(2T)
    where D_KL = 2b_net² = 2B_G²·ΔC²

  For barrier = d·B_G:
    D_KL/(2T) = d·B_G
    D_KL = 2d·B_G·T = d·α·B_G/K

  This says: the KL divergence per dimension from Pe=0 is α·B_G/K.

  What determines this specific KL divergence?
`);

sub('C1. KL divergence at the crossover');

// D_KL per dim = α·B_G/K = T·2B_G
// = α·B_G/K for Ni₃In: 0.213·2.244/50 = 0.00956
const DKL_per_dim = ni.alpha * B_G / ni.K;
const DKL_total = ni.d * DKL_per_dim;

console.log(`  Ni₃In:`);
console.log(`    D_KL per dimension = α·B_G/K = ${DKL_per_dim.toFixed(6)}`);
console.log(`    D_KL total = d × above = ${DKL_total.toFixed(6)}`);
console.log(`    2b_net² = 2B_G²·ΔC² = ${(2*B_G*B_G*ni.DC*ni.DC).toFixed(6)}`);
console.log(`    Match: ${(DKL_total/(2*B_G*B_G*ni.DC*ni.DC)*100).toFixed(1)}%`);

sub('C2. Fisher distance interpretation');

// The geodesic distance from the system to Pe=0:
// d_Fisher = 2|b_net| = 2B_G·|ΔC|
const d_Fisher = 2 * B_G * ni.DC;
console.log(`  Fisher distance from system to Pe=0:`);
console.log(`    d_F = 2B_G·ΔC = ${d_Fisher.toFixed(6)}`);
console.log(`    d_F² = ${(d_Fisher*d_Fisher).toFixed(6)}`);
console.log(`    D_KL = d_F²/2 = ${(d_Fisher*d_Fisher/2).toFixed(6)} ✓`);

// barrier = d_F²/(4T) per dimension? Let's check.
// barrier_per_dim = D_KL_per_dim/(2T) = (α·B_G/K)/(2·α/(2K)) = (α·B_G/K)·K/α = B_G ✓
// So: barrier_per_dim = B_G always, IF D_KL_per_dim = α·B_G/K.
// This is circular: it restates the constraint.

console.log(`\n  barrier_per_dim = D_KL_per_dim/(2T) = (α·B_G/K)·(K/α) = B_G ✓`);
console.log(`  (This is algebraically circular — restates the constraint.)`);

// ═══════════════════════════════════════════════════════════════
// PART D: NEW APPROACH — CRITICAL SLOWING / CROSSOVER PHYSICS
// ═══════════════════════════════════════════════════════════════
header('D. CRITICAL CROSSOVER PHYSICS');

console.log(`
  THE KEY REALIZATION: T* is not determined by the barrier.
  The barrier is determined by T*.

  At T = T*, two physical regimes become degenerate:
  - For kagome: FL scattering rate = Planckian rate
  - For nuclear: tunneling rate = observation time
  - For solar: heating rate = cooling rate
  - For xenobot: memory formation = thermal erasure

  T* is determined by the PHYSICS OF THE TRANSITION, independent
  of the Pe framework. The Pe framework then computes:

    barrier = 2K·B_G²·ΔC²/α = ln(Δε/(k_BT*))

  The RHS is a fixed number determined by material parameters.
  The LHS factors into the framework constants.

  The universality claim: barrier/d = B_G says that ln(Δε/(k_BT*))/d ≈ B_G.
  This is a statement about the PHYSICAL SYSTEMS, not just the framework.
`);

sub('D1. What determines Δε/(k_BT*)?');
console.log(`
  barrier = ln(Δε/(k_BT*))

  Δε = characteristic energy scale (flat band position for kagome,
       Coulomb barrier for nuclear, etc.)
  T* = crossover temperature

  barrier = d·B_G means:
    Δε/(k_BT*) = exp(d·B_G)

  For d=2: Δε/(k_BT*) = exp(2·2.244) = exp(4.488) = ${Math.exp(4.488).toFixed(1)}
  For d=3: Δε/(k_BT*) = exp(3·2.244) = exp(6.732) = ${Math.exp(6.732).toFixed(1)}

  Ni₃In: Δε = 12 meV, T* = 2 K → Δε/(k_BT*) = 12/(0.0862×2) = ${(12/(0.0862*2)).toFixed(1)}
  exp(4.488) = ${Math.exp(4.488).toFixed(1)}
  Ratio: ${(12/(0.0862*2)/Math.exp(4.488)).toFixed(3)} (= exp(measured_barrier)/exp(predicted_barrier))
`);

// The actual test: does Δε/(kBT*) ~ exp(d×B_G) for each domain?
console.log(`  CRITICAL QUESTION: Is Δε/(k_BT*) ≈ exp(d×B_G) a PHYSICAL LAW?`);
console.log(`  `);
console.log(`  For a Kramers escape: Δε/T* = ω₀/Γ × exp(barrier).`);
console.log(`  Without the prefactor: Δε/T* ≈ exp(barrier).`);
console.log(`  So barrier ≈ ln(Δε/T*) IS the definition.`);
console.log(`  The universality is: this number equals d×B_G.`);

sub('D2. Dimensional analysis of the barrier');
console.log(`
  barrier = 2K·B_G²·ΔC²/α

  Let ε = ΔC (dimensionless distance from Pe=0)
  Let R = K/α (inverse thermal coupling)

  barrier = 2B_G²·ε²·R

  For barrier = d·B_G:
    ε²·R = d/(2B_G)

  This is a SCALING RELATION: ε²·R = const × d

  Interpretation: ε = distance from criticality, R = 1/temperature (in framework units).
  At the crossover: distance² × inverse_temperature = d/(2B_G).

  Compare with classical scaling near a critical point:
    ξ(T) ∝ |t|^(-ν) where t = (T-Tc)/Tc

  At T*: ξ(T*) ∝ |ΔC|^(-ν) ∝ L (system size)

  For ν = 1/2 (mean-field): ξ ∝ |ΔC|^(-1/2) ∝ L
  → |ΔC| ∝ L^(-2)

  But we need ε² ∝ d/R ∝ d·α/K ∝ d·T.
  This gives ε ∝ √(d·T), which is the THERMAL FLUCTUATION scaling.
`);

// ═══════════════════════════════════════════════════════════════
// PART E: THE DEEP QUESTION — WHY 2B_G NOT JUST 2?
// ═══════════════════════════════════════════════════════════════
header('E. THE DEEP QUESTION: Factor 2B_G vs Factor 1');

console.log(`
  The constraint ε²·R = d/(2B_G) can be written as:

    ΔC² × K/α = d/(2B_G)

  Compare with what equipartition would give:
    ΔC²_equip × K/α = d/(4B_G²)    (from ⟨x²⟩ = T/(2κ) with κ = 2B_G²)

  Ratio: [d/(2B_G)] / [d/(4B_G²)] = 4B_G²/(2B_G) = 2B_G = ${(2*B_G).toFixed(4)}

  The SYSTEM sits at 2B_G times the equipartition position.

  WHERE DOES THE FACTOR 2B_G COME FROM?

  Possibility 1: The system is NOT at thermal equilibrium in ΔC.
    → The position is determined by material properties, not fluctuations.
    → Then 2B_G is just a number, and we need to explain why
       materials organize to give this factor.

  Possibility 2: There is an EFFECTIVE TEMPERATURE that is 2B_G times
    the bare temperature T = α/(2K).
    → T_eff = 2B_G·T = B_G·α/K
    → Then ⟨ΔC²⟩_eff = d·T_eff/(2κ) = d·B_G·α/(K·4B_G²) = d·α/(4KB_G) = d/(2B_G)·α/K
    → WAIT: this gives ΔC² = d·T_eff/(2B_G²) = d·B_G·α/(K·2B_G²) = d·α/(2KB_G)
    → Which IS the constraint! ✓

  The effective temperature hypothesis: T_eff = 2B_G·T_bare = B_G·α/K.
`);

sub('E1. What would produce T_eff = 2B_G × T?');

console.log(`
  In the §111 mean-field framework, K runs from 16 to 3,334 (200×).
  If the EFFECTIVE K at the transition is K_eff = K_bare/(2B_G):
    T_eff = α/(2K_eff) = α·2B_G/(2K_bare) = B_G·α/K_bare = 2B_G·T_bare ✓

  So: K_eff = K_bare/(2B_G) = K_bare/4.488

  For Ni₃In: K_eff = 50/4.488 = ${(50/(2*B_G)).toFixed(2)}

  The §111 K running (200×) is way more than 4.5×.
  But §111 runs K from LOW to HIGH (UV→IR).
  We need K to run from K_bare to K_bare/(2B_G) — a DECREASE.

  In §111, K_eff depends on the smoothing scale σ:
    σ=0.05: K_eff = 57.88  (262% above K=16)
    σ=0.50: K_eff = 18.86  (18% above K=16)
    σ=0.80: K_eff = 16.51  (3% above K=16)

  K INCREASES with UV coarse-graining (smaller σ), doesn't decrease.

  BUT: §111 uses K=16 (fitted from platform data). For a PHYSICAL system
  with K=50, the mean-field iteration might behave differently.
`);

sub('E2. Alternative: the metric determinant provides the factor');

console.log(`
  The partition function on the Eckert manifold includes √(det g):

    Z = ∫ exp(-V/T) × √(det g) × dΔC

  For the Fisher metric: √(det g) = 1/√(p(1-p)) per dimension.
  In the angular coordinate: √(det g) = 2.

  The effective potential including the measure:
    V_eff = V - T·ln(√(det g))

  For V = B_G²·ΔC² and √(det g) = 2^d in angular coords:
    V_eff = B_G²·ΔC² - T·d·ln(2)

  The barrier:
    V_eff(ΔC)/T = 2K·B_G²·ΔC²/α - d·ln(2)

  The ln(2) correction shifts the barrier by d·ln(2) ≈ d×0.693.
  This is in the RIGHT DIRECTION (barrier is reduced from bare value)
  but the magnitude is wrong (need shift of d·(B_G-1/2) = d×1.744).

  ln(2) = ${Math.log(2).toFixed(6)}
  B_G - 1/2 = ${(B_G - 0.5).toFixed(6)}
  Ratio: ${(Math.log(2)/(B_G-0.5)).toFixed(4)} (need 1.0)
`);

// What about at the specific p₀ = 0.614?
// The metric factor at p₀ is 1/√(p₀(1-p₀))
const gFactor = 1 / Math.sqrt(p0 * (1 - p0));
console.log(`\n  At Pe=0 (p₀ = ${p0.toFixed(4)}):`);
console.log(`    √g per dim = 1/√(p₀(1-p₀)) = ${gFactor.toFixed(4)}`);
console.log(`    ln(√g) per dim = ${Math.log(gFactor).toFixed(4)}`);
console.log(`    Need: ${(B_G - 0.5).toFixed(4)}`);
console.log(`    Ratio: ${(Math.log(gFactor)/(B_G-0.5)).toFixed(4)}`);

// ═══════════════════════════════════════════════════════════════
// PART F: THE PARTITION FUNCTION APPROACH
// ═══════════════════════════════════════════════════════════════
header('F. PARTITION FUNCTION ON THE BERNOULLI MANIFOLD');

console.log(`
  NEW IDEA: The barrier per dimension should be computed from the
  PARTITION FUNCTION on the Bernoulli manifold, not from the
  potential energy at a specific point.

  On the Bernoulli manifold parameterized by θ ∈ [0, π/2]:

    Z₁D = ∫₀^{π/2} exp(-V(θ)/T) × 2dθ    (metric factor = 2)

  where V(θ) = B_G²·(C(θ) - C₀)² = B_G²·ΔC(θ)².

  The free energy: F₁D = -T·ln(Z₁D)
  The "barrier" is: F₁D/T = -ln(Z₁D)
`);

sub('F1. Compute Z₁D vs T for different potentials');

// The coordinate mapping: θ → p = sin²(θ) → O = 3p → C = 1-(3p+R'+α')/9
// For a single coordinate (say O), with R and α fixed:
//   C = 1 - (3sin²θ + R' + α')/9 = const - sin²(θ)/3
//   ΔC = C - C₀ = -(sin²(θ) - sin²(θ₀))/3

// Actually, the partition function approach requires specifying how ΔC
// varies with the coordinate. This depends on which coordinate is being
// integrated. Let me use the C-coordinate directly.

// In C-coordinate: V = B_G²·(C-C₀)², T = α/(2K)
// barrier_parameter β_V = V/T = 2KB_G²(C-C₀)²/α
// The "mass" in 1D is: β_V'' = 2·2KB_G²/α = 4KB_G²/α

// C ranges from 0 to 1. The Fisher metric in C-coordinate:
// C = 1-(O+R+α)/9. If we vary ONE coordinate (say O with R,α fixed):
//   C = 1 - O/9 - const. dC = -dO/9.
//   O ranges from 0 to 3. p = O/3 ranges from 0 to 1.
//   dO = 3dp. dC = -dp/3.
//   Fisher metric: ds² = dp²/(p(1-p)) = 9dC²/((3C-...)(1-3C+...))
// This is getting messy. Let me just do the integral in θ.

// Simple approach: V(θ) = B_G²·(θ-θ₀)²/γ² where γ maps θ to ΔC.
// If ΔC ∝ θ (approximately, near θ₀), then V is quadratic in θ.

// For a quadratic potential in 1D:
// Z = ∫₀^{π/2} exp(-V₀(θ-θ₀)²) × 2dθ
// ≈ √(π/V₀) × 2   (Gaussian integral, if well-contained in [0,π/2])

// The free energy: F = -T·ln(Z) = -T·(ln(2) + ½ln(π/V₀))
// F/T = -ln(2) - ½ln(π/V₀) = -ln(2) - ½ln(π) + ½ln(V₀)

// For V₀ = 2KB_G²/α:
// F/T = -ln(2) - ½ln(π) + ½ln(2KB_G²/α)
// = ½ln(2KB_G²/(πα)) - ln(2)

// This is the free energy per dimension, not the barrier.
// The barrier is defined as V(ΔC_system)/T, not the free energy.

// Actually, let me think about this more carefully.
// The BARRIER is the height of the potential at the system's position.
// The FREE ENERGY includes the entropy of fluctuations around the system.
// These are different quantities.

console.log(`
  The partition function gives the FREE ENERGY, not the BARRIER.
  The barrier is V(ΔC)/T at the system's specific position.
  The free energy is -T·ln(Z) which includes entropic corrections.

  The distinction matters: barrier ≠ free energy in general.

  The measured quantity (T*) is an activation BARRIER, not a free energy.
  T* = Δε/k_B × exp(-barrier), where barrier = activation energy/k_BT*.

  In Kramers theory: barrier = ΔV/T (potential energy barrier).
  In transition state theory: barrier = ΔG‡/T (free energy barrier).

  If the measured T* corresponds to a FREE ENERGY barrier:
    barrier_free = ΔV/T - ΔS (entropy of the transition state)

  The entropy ΔS of the transition state on the Bernoulli manifold
  could provide the missing factor!
`);

sub('F2. Transition state entropy on the Bernoulli manifold');

// At the transition (Pe=0), the system has d degenerate dimensions.
// The transition state has LESS constraint than the ground state.
// The entropy difference: ΔS = S(transition) - S(ground)

// On the Bernoulli manifold, the entropy per dimension is:
// S = -∫ p·ln(p) dp (information entropy)
// But this is not the thermodynamic entropy.

// The thermodynamic entropy is related to the logarithm of the
// available phase space:
// S = ln(Ω) where Ω is the number of microstates.

// On the Fisher manifold, the "volume" of a region around p₀ with width δp:
// Ω = ∫_{p₀-δp}^{p₀+δp} √g dp = ∫ dp/√(p(1-p))

// At the ground state (ΔC from Pe=0):
//   Width in p: δp ∝ √(T/κ) = √(T/(2B_G²))
//   Ω_ground ∝ √(T/B_G²) × √g(p_ground)

// At the transition state (Pe=0, ΔC=0):
//   The constraint is RELEASED along d-1 transverse directions.
//   Ω_transition ∝ √(T/κ_⊥)^{d-1} × √(T/κ_∥)

// For the Pe potential V = B_G²·ΔC², the "along" and "perpendicular"
// curvatures are:
//   κ_∥ = 2B_G² (curvature along ΔC)
//   κ_⊥ = 0 (flat perpendicular directions, since V depends only on C = (O+R+α)/9)

// At the saddle (Pe=0), the d-1 perpendicular directions are FLAT.
// The available volume is unbounded in those directions.
// This means the transition state has INFINITE entropy... unless there's a cutoff.

// The cutoff is the manifold boundary: O,R,α ∈ [0,3], so C ∈ [0,1].
// The perpendicular volume at Pe=0 is the (d-1)-dimensional volume of
// the hyperplane C = C₀ within the hypercube [0,3]^3.

// For 3D (O,R,α): C = C₀ means O+R+α = 9(1-C₀) ≈ 5.53.
// The intersection of the plane O+R+α = 5.53 with [0,3]³ is a triangle.
// Area of this triangle in Euclidean metric: ?

// The plane O+R+α = S intersects [0,3]³ as a triangle when S > 6
// (cutting off one corner) or a triangle when S < 3.
// For S = 5.53 (between 3 and 6): it's a hexagon.

// Let me compute the area of the intersection.
const S_plane = 9 * (1 - C0);  // O+R+α at Pe=0
console.log(`\n  At Pe=0: O+R+α = ${S_plane.toFixed(4)}`);

// For S in (3,6), the intersection is a hexagon with vertices at
// permutations of (0, a, b) where a+b = S.
// Actually for S = 5.53: each coord can range from max(0, S-6) to min(3, S).
// O ∈ [max(0, 5.53-6), min(3, 5.53)] = [0, 3]... no wait.
// O + R + α = 5.53. For O to be valid: O ∈ [0,3], and R+α = 5.53-O ∈ [0,6].
// So O ∈ [max(0, 5.53-6), min(3, 5.53)] = [0, 3].
// But also R ∈ [0,3] and α ∈ [0,3], so R+α ∈ [0,6] and R+α = 5.53-O.
// For R ∈ [0,3]: α = 5.53-O-R ∈ [5.53-O-3, 5.53-O-0] = [2.53-O, 5.53-O]
// Need α ∈ [0,3]: α ≥ 0 → R ≤ 5.53-O, and α ≤ 3 → R ≥ 2.53-O.
// So R ∈ [max(0, 2.53-O), min(3, 5.53-O)].

// The Euclidean area of this region (in the plane O+R+α = S):
// A = √3/2 × (side length)² for a hexagon... but it's not regular.
// Let me just compute the Fisher-metric area numerically.

let fisherArea = 0;
const N_grid = 500;
const dO = 3.0 / N_grid;
for (let iO = 0; iO < N_grid; iO++) {
  const O_val = (iO + 0.5) * dO;
  const alpha_min = Math.max(0, S_plane - O_val - 3);
  const alpha_max = Math.min(3, S_plane - O_val);
  if (alpha_min >= alpha_max) continue;
  const R_val = S_plane - O_val - (alpha_min + alpha_max) / 2;
  // Actually, for the Fisher-metric area on the plane O+R+α = S,
  // we need to integrate √(det g_induced) over the 2D region.
  // The induced metric on the plane is the pullback of the Fisher metric.
  // Let me parameterize by (O, R) with α = S - O - R.
  const R_lo = Math.max(0, S_plane - O_val - 3);
  const R_hi = Math.min(3, S_plane - O_val);
  if (R_lo >= R_hi) continue;
  const dR = (R_hi - R_lo) / N_grid;
  for (let iR = 0; iR < N_grid; iR++) {
    const R_val_inner = R_lo + (iR + 0.5) * dR;
    const alpha_val = S_plane - O_val - R_val_inner;
    if (alpha_val < 0.01 || alpha_val > 2.99 || O_val < 0.01 || O_val > 2.99 || R_val_inner < 0.01 || R_val_inner > 2.99) continue;

    const pO = O_val / 3;
    const pR = R_val_inner / 3;
    const pA = alpha_val / 3;

    // Fisher metric in (O,R,α) coords: g_ii = 1/(9·p_i(1-p_i))
    // (Factor 1/9 from dp = dO/3)
    const gOO = 1 / (9 * pO * (1 - pO));
    const gRR = 1 / (9 * pR * (1 - pR));
    const gAA = 1 / (9 * pA * (1 - pA));

    // Induced metric on plane O+R+α = S, parameterized by (O,R):
    // α = S - O - R, so dα = -dO - dR
    // Induced metric:
    // g_11 = gOO + gAA·(dα/dO)² = gOO + gAA  (since dα/dO = -1)
    // g_12 = gAA·(dα/dO)(dα/dR) = gAA  (since dα/dO = dα/dR = -1)
    // g_22 = gRR + gAA
    const g11 = gOO + gAA;
    const g12 = gAA;
    const g22 = gRR + gAA;

    const detG_induced = g11 * g22 - g12 * g12;
    fisherArea += Math.sqrt(detG_induced) * dO * dR;
  }
}

console.log(`  Fisher-metric area of Pe=0 plane: ${fisherArea.toFixed(4)}`);
console.log(`  Compare: π² = ${(Math.PI*Math.PI).toFixed(4)}, π²/2 = ${(Math.PI*Math.PI/2).toFixed(4)}, 2π = ${(2*Math.PI).toFixed(4)}`);

// The transition state entropy (per dimension) from the area:
const S_trans_per_dim = Math.log(fisherArea) / 2;  // rough: 2D area → 2 dimensions
console.log(`  ln(area)/2 = ${S_trans_per_dim.toFixed(4)}`);
console.log(`  Compare B_G - 0.5 = ${(B_G-0.5).toFixed(4)} (needed correction)`);

// ═══════════════════════════════════════════════════════════════
// PART G: THE THERMAL RMS ON BERNOULLI WITH MODIFIED MEASURE
// ═══════════════════════════════════════════════════════════════
header('G. THERMAL RMS WITH MODIFIED MEASURE');

console.log(`
  Standard equipartition: ⟨x²⟩ = T/κ → barrier_per_dim = 1/2.

  But on the Bernoulli manifold, the thermal average uses the
  Fisher measure √g, not the flat measure:

    ⟨ΔC²⟩_Fisher = ∫ ΔC² × exp(-V/T) × √g dΔC / ∫ exp(-V/T) × √g dΔC

  The measure √g at the Pe=0 point differs from 1, and this could
  modify the effective equipartition result.
`);

sub('G1. 1D test: equipartition with Fisher measure');

// In 1D Bernoulli coordinate θ ∈ [0, π/2]:
// V(θ) = B_G²·(C(θ) - C₀)²
// C(θ) = 1 - p(θ)/3 (for a single coordinate, roughly)
// p(θ) = sin²(θ)
// So C(θ) = 1 - sin²(θ)/3 = (3 - sin²θ)/3

// At Pe=0: C₀ ≈ 0.386. Need sin²θ₀ = 3(1-C₀) = 3×0.614 = 1.841 → impossible!
// sin²θ ≤ 1. So a single coordinate can't reach C₀ by itself.
// This means the Pe=0 boundary requires contributions from ALL three coordinates.

// For the SUM (O+R+α)/9, if each coordinate is equal:
// O = R = α = 3(1-C₀)/3·3 = 3·0.614 = 1.842 → p = 1.842/3 = 0.614

// Let me do the 1D integral for a single Bernoulli coordinate near p₀ = 0.614
// ΔC = -(p - p₀)/3 (from C = 1 - p/3 - const)
// V = B_G²·ΔC² = B_G²·(p-p₀)²/9
// β·V = (2K/α)·B_G²·(p-p₀)²/9

// In angular coordinate θ = arcsin(√p):
// dp = 2sin(θ)cos(θ)dθ = sin(2θ)dθ
// Fisher metric: ds² = dp²/(p(1-p)) = 4dθ²
// So the measure is: 2dθ (Fisher measure in angular coords)

const theta0 = Math.asin(Math.sqrt(p0));  // ≈ 0.897
const betaV_coeff = 2 * ni.K * B_G * B_G / (9 * ni.alpha);

console.log(`  θ₀ = arcsin(√p₀) = ${theta0.toFixed(6)} (radians)`);
console.log(`  β·V coefficient = 2KB_G²/(9α) = ${betaV_coeff.toFixed(4)}`);

// Compute ⟨ΔC²⟩ with Fisher measure
let num_avg = 0, den_avg = 0;
const N_int2 = 100000;
const dtheta = (Math.PI / 2) / N_int2;

for (let i = 0; i < N_int2; i++) {
  const theta = (i + 0.5) * dtheta;
  const p = Math.sin(theta) * Math.sin(theta);
  const DC_val = -(p - p0) / 3;
  const V_val = B_G * B_G * DC_val * DC_val;
  const betaV = V_val * 2 * ni.K / ni.alpha;
  const weight = Math.exp(-betaV) * 2;  // measure = 2dθ
  num_avg += DC_val * DC_val * weight * dtheta;
  den_avg += weight * dtheta;
}

const DC2_fisher = num_avg / den_avg;
const barrier_from_fisher = B_G * B_G * DC2_fisher * 2 * ni.K / ni.alpha;

// Compare with flat equipartition
const DC2_equip_1d = ni.alpha / (2 * ni.K * 2 * B_G * B_G);
const barrier_equip_1d = 0.5;

console.log(`\n  ⟨ΔC²⟩_Fisher = ${DC2_fisher.toExponential(6)}`);
console.log(`  ⟨ΔC²⟩_equip  = ${DC2_equip_1d.toExponential(6)} (= T/(2κ) = α/(8KB_G²))`);
console.log(`  Ratio Fisher/equip = ${(DC2_fisher/DC2_equip_1d).toFixed(6)}`);
console.log(`  barrier_per_dim (Fisher) = ${barrier_from_fisher.toFixed(6)}`);
console.log(`  barrier_per_dim (equip)  = ${barrier_equip_1d.toFixed(6)}`);

// The Fisher measure shouldn't change the equipartition result for a
// Gaussian potential when the Gaussian width is much smaller than the
// curvature scale of the measure. Let's check:
const sigma_gaussian = Math.sqrt(DC2_equip_1d);
console.log(`\n  Gaussian width σ = √⟨ΔC²⟩ = ${sigma_gaussian.toExponential(3)}`);
console.log(`  Manifold curvature scale = 1/√(|g''|) ≈ O(1)`);
console.log(`  σ ≪ 1: the Gaussian is much narrower than the manifold`);
console.log(`  → Fisher measure ≈ constant over the Gaussian → no correction.`);

console.log(`\n  VERDICT: The Fisher measure does NOT modify equipartition`);
console.log(`  because the thermal width (σ ∝ 10⁻²) is much smaller than`);
console.log(`  the manifold curvature scale (∼1). The measure is effectively`);
console.log(`  constant across the fluctuation region.`);

// ═══════════════════════════════════════════════════════════════
// PART H: THE REAL INSIGHT — CONSTRAINT FROM THE MAPPING
// ═══════════════════════════════════════════════════════════════
header('H. THE MAPPING CONSTRAINT HYPOTHESIS');

console.log(`
  SYNTHESIS: All field-theoretic approaches fail because:

  1. Equipartition: barrier = d/2 (theorem, coordinate-independent)
  2. Ginzburg criterion: system is deep in mean-field (fluctuations < 1%)
  3. Manifold curvature: Fisher manifold is flat (R = 0)
  4. Measure correction: Gaussian width ≪ manifold scale (no effect)
  5. Mean-field self-coupling: V is exactly quadratic (no δV'' correction)

  THE BARRIER IS NOT DETERMINED BY EQUILIBRIUM STATISTICAL MECHANICS.

  The system's position ΔC is FROZEN at the value set by material
  parameters. It doesn't thermally fluctuate in the C-coordinate.
  The "temperature" T = α/(2K) is the framework's effective temperature,
  not a physical temperature that drives C-fluctuations.

  THEREFORE: barrier = d·B_G must follow from a constraint on the
  MAPPING from physical parameters to (O,R,α,K), not from the
  statistical mechanics on the Eckert manifold.

  THE QUESTION SHIFTS: Why does the mapping (O,R,α,K) → barrier
  produce barrier/d ≈ B_G across different physical domains?
`);

sub('H1. Structure of the mapping');
console.log(`
  For each domain, the mapping is:
    Physical params → (O, R, α, K) → C = 1-(O+R+α)/9 → ΔC = C-C₀ → barrier = 2KB_G²ΔC²/α

  The mapping has 4 output parameters (O, R, α, K) but only 2 enter
  the barrier: the combination ΔC²·K/α.

  Let X = K·ΔC²/α. Then barrier = 2B_G²·X.
  For barrier = d·B_G: X = d/(2B_G) = d×${(1/(2*B_G)).toFixed(6)}.
`);

// For Ni₃In:
const X_Ni = ni.K * ni.DC * ni.DC / ni.alpha;
console.log(`  Ni₃In: X = K·ΔC²/α = ${X_Ni.toFixed(6)}`);
console.log(`  d/(2B_G) for d=2 = ${(2/(2*B_G)).toFixed(6)}`);
console.log(`  Match: ${(X_Ni/(2/(2*B_G))*100).toFixed(1)}%`);

sub('H2. Does the mapping FORCE X = d/(2B_G)?');
console.log(`
  The mapping for kagome metals:
    O = 3·(1 - W_exp/W_DFT) = 3·(1 - Z_flat)     — band narrowing
    R = 3·exp(-|Δε|/W_disp)                         — flat band proximity
    α = (Z_flat+Z_disp)/2·Δε/W_flat                 — spectral weight
    K = U/t                                          — Hubbard ratio

  Now: C = 1 - (O+R+α)/9 and ΔC = C - C₀.

  For ΔC ≈ 0.043 and C₀ ≈ 0.386: C ≈ 0.429.
  So O+R+α ≈ 5.14.

  The key relationship: K·ΔC²/α ≈ d/(2B_G)

  In physical terms:
    (U/t)·(C-C₀)²/[(Z_flat+Z_disp)/2·Δε/W_flat] ≈ d/(2B_G)

  Substituting O and R expressions:
    C = 1 - [3(1-Z_flat) + 3exp(-|Δε|/W_disp) + (Z_flat+Z_disp)/2·Δε/W_flat]/9

  This is a complex function of (Z_flat, Z_disp, Δε, W_flat, W_disp, W_DFT, U, t).
  There's no obvious algebraic simplification that produces d/(2B_G).
`);

// ═══════════════════════════════════════════════════════════════
// PART I: THE π/√2 vs B_G DISCRIMINANT
// ═══════════════════════════════════════════════════════════════
header('I. DISCRIMINATING π/√2 FROM B_G');

console.log(`
  If barrier/d = π/√2 (geometric) vs B_G (framework constant):

  Current data (N=4, only barrier/d matters):
    2.12, 2.18, 2.27, 2.30

  Mean: ${([2.12,2.18,2.27,2.30].reduce((a,b)=>a+b)/4).toFixed(4)}
  Std:  ${Math.sqrt([2.12,2.18,2.27,2.30].map(x => (x-2.2175)**2).reduce((a,b)=>a+b)/3).toFixed(4)}

  π/√2 = ${PI_SQRT2.toFixed(4)}
  B_G   = ${B_G.toFixed(4)}
  Difference = ${(B_G - PI_SQRT2).toFixed(4)} = ${((B_G-PI_SQRT2)/PI_SQRT2*100).toFixed(2)}%

  The DATA mean (2.218) is closer to π/√2 (2.221) than to B_G (2.244).

  Bootstrap 95% CI for the mean:
`);

const data = [2.12, 2.18, 2.27, 2.30];
// Bootstrap
const N_boot = 100000;
const means = [];
for (let b = 0; b < N_boot; b++) {
  let s = 0;
  for (let i = 0; i < 4; i++) {
    s += data[Math.floor(Math.random() * 4)];
  }
  means.push(s / 4);
}
means.sort((a, b) => a - b);
const ci_lo = means[Math.floor(0.025 * N_boot)];
const ci_hi = means[Math.floor(0.975 * N_boot)];

console.log(`  Bootstrap 95% CI: [${ci_lo.toFixed(4)}, ${ci_hi.toFixed(4)}]`);
console.log(`  π/√2 = ${PI_SQRT2.toFixed(4)} — ${ci_lo <= PI_SQRT2 && PI_SQRT2 <= ci_hi ? 'INSIDE CI ✓' : 'OUTSIDE CI ✗'}`);
console.log(`  B_G   = ${B_G.toFixed(4)} — ${ci_lo <= B_G && B_G <= ci_hi ? 'INSIDE CI ✓' : 'OUTSIDE CI ✗'}`);
console.log(`  Optimal = ${(data.reduce((a,b)=>a+b)/4).toFixed(4)}`);

sub('I2. d=1 discriminant');
console.log(`
  For d=1: barrier(π/√2) = ${PI_SQRT2.toFixed(4)}, barrier(B_G) = ${B_G.toFixed(4)}
  Difference = ${(B_G - PI_SQRT2).toFixed(4)} — resolvable at ~1% measurement precision.

  Best d=1 candidates:
  - 1D atomic chains (gold, platinum — quantum conductance regime)
  - Domain walls in ferromagnets (Bloch/Néel wall crossover)
  - Edge states in 2D TI (1D transport channel)
  - Carbon nanotubes (Luttinger liquid → Fermi liquid crossover)

  The d=1 test is the HIGHEST-PRIORITY empirical discriminant.
`);

// ═══════════════════════════════════════════════════════════════
// PART J: STATUS AND NEXT STEPS
// ═══════════════════════════════════════════════════════════════
header('J. STATUS OF THE DERIVATION (2026-03-22)');

console.log(`
  DEFINITIVELY CLOSED:
  ─────────────────────
  ✗ Equipartition with quadratic V always gives d/2 (theorem)
  ✗ Kramers prefactor inapplicable (T* is crossover, not rate)
  ✗ Anharmonic correction requires γ₄ ~ 3000 (absurd)
  ✗ Ginzburg criterion fails (system deep in mean-field, Gi < 1%)
  ✗ Fisher manifold is flat (Ricci scalar R = 0, no curvature coupling)
  ✗ Measure correction negligible (Gaussian width ≪ manifold scale)
  ✗ Mean-field V'' correction zero (potential exactly quadratic in ΔC)

  THE BARRIER IS NOT A STATISTICAL MECHANICS RESULT.

  The system's position ΔC is frozen by material parameters.
  The barrier is V(ΔC)/T where both V and T are fixed by material physics.
  The universality barrier/d = B_G is a statement about MATERIAL PHYSICS,
  not about equilibrium fluctuations on the Eckert manifold.

  REMAINING OPEN AVENUES:
  ───────────────────────
  1. MAPPING CONSTRAINT: The (O,R,α,K) mapping has a built-in structure
     that forces K·ΔC²/α = d/(2B_G) for systems at their crossover.
     → Needs verification on domains 2-4 (currently only Ni₃In decomposed)
     → If the constraint is in the mapping, the question shifts to:
       why does EXP-001 give B_A/B_G = ${C0.toFixed(4)}?

  2. RG BETA FUNCTION: The value B_G could emerge from the UV fixed point
     of the Pe field theory. At Pe=0, the renormalization of b_net's
     curvature coefficient (2B_G²) under RG flow might be fixed by
     the beta function to give B_G = π/√2 exactly.
     → Requires computing the beta function for the sinh-potential theory
     → The sinh structure might have special RG properties

  3. SO(4,2) REPRESENTATION: B_G = π/√2 could be a Casimir eigenvalue
     or a representation-theoretic invariant of the conformal group.
     → HP74 confirms SO(4,2) but with C₂ = 0 (trivial rep at Pe=0)
     → The phonological C₂ = 0 at Pe=0 means the obvious route gives 0

  4. B_A = √3/2 HYPOTHESIS: B_A = 0.867 ≈ √3/2 = 0.866 (0.1% match).
     If B_A = √3/2 and B_G = π/√2:
       C₀ = B_A/B_G = √3·√2/(2π) = √6/(2π) = ${(Math.sqrt(6)/(2*Math.PI)).toFixed(6)}
       (compare actual C₀ = ${C0.toFixed(6)}, match: ${(Math.sqrt(6)/(2*Math.PI)/C0*100).toFixed(2)}%)
     → Would suggest the constants come from the Bernoulli manifold geometry
     → √3/2 = cos(π/6): the COS of the hexagonal angle
     → If Pe = sinh(2(cos(π/6) - C·π/√2))·K, the argument involves
       trigonometric and geometric constants only

  5. THE d=1 TEST: Find a 1D system with a barrier crossover.
     Predicted barrier: 2.22-2.24 (discriminates π/√2 from B_G at 1%).
     This is the highest-priority EMPIRICAL test.

  SHARPENED OPEN PROBLEM:
  ───────────────────────
  The universality of barrier/d ≈ π/√2 is NOT a consequence of
  statistical mechanics on the Eckert manifold. It is a property
  of the MAPPING from physical parameters to (O,R,α,K).

  The question: why do physical systems at their crossover temperature
  satisfy the constraint K·ΔC²/α = d/(2B_G)?

  This constraint relates three independent physical quantities:
  - K (interaction/scale ratio)
  - ΔC (compositional distance from the Pe=0 critical surface)
  - α (coupling strength)

  The factor B_G ≈ π/√2 enters because the Pe formula uses sinh(2(B_A - CB_G)),
  and the critical surface is at C₀ = B_A/B_G. The barrier height at ΔC is:
  barrier = 2K·B_G²·ΔC²/α, and barrier = d·B_G iff KΔC²/α = d/(2B_G).

  The deepest route to a derivation: show that B_A and B_G are NOT
  independent free parameters but are constrained by the manifold
  structure to satisfy B_A = √3/2, B_G = π/√2 (or related identities).
  This would make the barrier universality a GEOMETRIC THEOREM.
`);

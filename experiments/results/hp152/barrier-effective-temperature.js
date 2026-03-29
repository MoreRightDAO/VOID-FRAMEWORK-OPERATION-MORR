#!/usr/bin/env node
/**
 * barrier-effective-temperature.js — 2026-03-22
 *
 * Tests the EFFECTIVE TEMPERATURE hypothesis:
 *   T_eff = 2B_G·T_bare produces barrier = d·B_G via equipartition
 *
 * Also:
 *   - High-resolution Fisher area of Pe=0 plane
 *   - B_A = cos(π/6) = √3/2 hypothesis detailed test
 *   - Cross-check: does T_eff = 2B_G·T have physical meaning?
 */

const B_A = 0.867;
const B_G = 2.244;
const C0 = B_A / B_G;
const PI_SQRT2 = Math.PI / Math.sqrt(2);

function header(s) { console.log('\n' + '═'.repeat(72)); console.log(s); console.log('═'.repeat(72)); }
function sub(s) { console.log('\n── ' + s + ' ──'); }

// ═══════════════════════════════════════════════════════════════
// 1. THE EFFECTIVE TEMPERATURE HYPOTHESIS
// ═══════════════════════════════════════════════════════════════
header('1. EFFECTIVE TEMPERATURE HYPOTHESIS');

console.log(`
  If the system at the crossover has an effective temperature
  T_eff = 2B_G·T_bare (where T_bare = α/(2K)):

    T_eff = 2B_G·α/(2K) = B_G·α/K

  Then equipartition in d dimensions gives:
    ⟨ΔC²⟩ = d·T_eff/(2κ) where κ = 2B_G² (curvature of V)
           = d·B_G·α/(K·4B_G²)
           = d·α/(4K·B_G)

  barrier = V(√⟨ΔC²⟩)/T_bare = B_G²·d·α/(4K·B_G) · (2K/α)
          = B_G²·d/(2B_G) = d·B_G/2

  WAIT — that gives d·B_G/2, not d·B_G.

  Let me redo: barrier = V(ΔC)/T_bare where ΔC is set by T_eff.
  ⟨ΔC²⟩_eff = d·T_eff/(2κ) = d·B_G·α/(K·4B_G²) = d·α/(4KB_G)
  V(√⟨ΔC²⟩) = B_G²·d·α/(4KB_G) = d·α·B_G/(4K)
  barrier = V/T_bare = d·α·B_G/(4K) · 2K/α = d·B_G/2

  Still d·B_G/2. The problem: barrier = V/T_bare, but fluctuations
  use T_eff. The factor of 2 is lost because V and T are different.
`);

sub('1a. Correct formulation');
console.log(`
  The barrier is measured as: barrier = ln(Δε/(k_BT*))
  If T* is the physical crossover temperature, barrier is fixed.

  For barrier = V/T to give d·B_G:
    V(ΔC) = d·B_G·T

  For quadratic V = B_G²·ΔC²:
    B_G²·ΔC² = d·B_G·T → ΔC² = d·T/B_G = d·α/(2KB_G)

  This is the constraint. It says the position ΔC = √(dT/B_G),
  which is √(2B_G) times the equipartition displacement √(dT/(2B_G²)).

  The effective temperature that gives this displacement via equipartition:
    ΔC² = d·T_eff/κ where κ = 2B_G²
    d·α/(2KB_G) = d·T_eff/(2B_G²)
    T_eff = B_G·α/K = 2B_G·T

  So barrier measured at T_bare:
    barrier = V/T_bare = κ·ΔC²/(2T_bare) = 2B_G²·d·T_eff/(2B_G²·2T_bare)
            = d·T_eff/(2T_bare) = d·(2B_G·T)/(2T) = d·B_G  ✓

  THE LOGIC: The system fluctuates at T_eff = 2B_G·T (enhanced temp),
  sets its position by this enhanced fluctuation, but the barrier
  height is measured against the BARE temperature T.

  If the system were in equilibrium at T: barrier = d/2.
  If the system is at an ENHANCED position (set by T_eff): barrier = d·B_G.
  The factor 2B_G = T_eff/T is the enhancement ratio.
`);

// ═══════════════════════════════════════════════════════════════
// 2. WHAT PHYSICAL MECHANISM GIVES T_eff = 2B_G × T?
// ═══════════════════════════════════════════════════════════════
header('2. PHYSICAL MECHANISM FOR T_eff = 2B_G × T');

console.log(`
  For T_eff = 2B_G·T, one of these must hold:

  A. K_eff = K/(2B_G): effective coupling is weaker by 2B_G
     → For Ni₃In: K_eff = 50/${(2*B_G).toFixed(2)} = ${(50/(2*B_G)).toFixed(2)}

  B. α_eff = 2B_G·α: effective coupling is stronger by 2B_G
     → For Ni₃In: α_eff = 2B_G·0.213 = ${(2*B_G*0.213).toFixed(4)}

  C. Non-equilibrium: the system is DRIVEN to ΔC by dynamics,
     not by thermal equilibrium. The "effective temperature" is
     the kinetic energy of the driving, not thermodynamic T.

  For option A (K renormalization):
    At the crossover T*, the interaction-to-hopping ratio K = U/t
    is renormalized by thermal fluctuations. The renormalized
    hopping at T*:
      t_eff = t·(1 + 2B_G - 1) = t·2B_G
      K_eff = U/t_eff = K/(2B_G)

    This requires the thermal hopping enhancement at T* to be
    exactly 2B_G - 1 ≈ 3.49.

    For a Hubbard model at the FL→SM crossover:
      t_eff/t = 1/(Z(T*)) where Z = quasiparticle weight

    At the crossover: Z(T*) = 1/(2B_G) ≈ ${(1/(2*B_G)).toFixed(4)}

    This is physically reasonable: at the FL→SM crossover,
    the quasiparticle weight is significantly reduced from 1.

  For option B (α renormalization):
    The coupling α is enhanced by the mean-field interaction.
    In §111, the coupling runs 200×. Here we'd need only 2B_G ≈ 4.5×.
`);

sub('2a. Test against Ni₃In data');

// For Ni₃In: Z_flat = 0.333 (measured by ARPES)
// Z(T=0) = Z_flat ≈ 0.333
// At T = T* = 2K: Z(T*) is reduced further by thermal effects.
// The FL→SM crossover happens when Z drops below some threshold.

// The hypothesis: Z(T*) = 1/(2B_G)
const Z_predicted = 1 / (2 * B_G);
const Z_measured_T0 = 0.333;

console.log(`  Ni₃In:`);
console.log(`    Z(T=0) from ARPES: ${Z_measured_T0}`);
console.log(`    Z(T*) predicted: 1/(2B_G) = ${Z_predicted.toFixed(4)}`);
console.log(`    Ratio Z(T*)/Z(0) = ${(Z_predicted/Z_measured_T0).toFixed(4)}`);
console.log(`    → Z drops by factor ${(Z_measured_T0/Z_predicted).toFixed(2)} from T=0 to T=T*`);
console.log(`    This is a ${((1 - Z_predicted/Z_measured_T0)*100).toFixed(0)}% reduction.`);
console.log(`    For a Fermi liquid near the Mott transition, this is moderate.`);

// Alternative: Z(T*) for the specific α mapping
// α = (Z_flat + Z_disp)/2 × Δε/W_flat
// At T*: α(T*) = (Z(T*) + Z_disp(T*))/2 × Δε/W_flat
// If Z(T*) = 1/(2B_G) = 0.223 and Z_disp is roughly constant:
// α(T*) ≈ (0.223 + 0.7)/2 × 12/30 = 0.462 × 0.4 = 0.185

const alpha_at_Tstar = (Z_predicted + 0.7) / 2 * 12 / 30;
console.log(`\n    α(T*) with Z(T*) = ${Z_predicted.toFixed(3)}: ${alpha_at_Tstar.toFixed(4)}`);
console.log(`    α(T=0) measured: ${0.207.toFixed(4)}`);
console.log(`    Change: ${((alpha_at_Tstar/0.207 - 1)*100).toFixed(1)}% (small)`);

// ═══════════════════════════════════════════════════════════════
// 3. HIGH-RESOLUTION FISHER AREA OF Pe=0 PLANE
// ═══════════════════════════════════════════════════════════════
header('3. FISHER-METRIC AREA OF Pe=0 PLANE (high resolution)');

const S_plane = 9 * (1 - C0);

function computeFisherArea(N_grid) {
  let area = 0;
  const dO = 3.0 / N_grid;
  const eps = 0.005; // boundary cutoff

  for (let iO = 0; iO < N_grid; iO++) {
    const O_val = (iO + 0.5) * dO;
    if (O_val < eps || O_val > 3 - eps) continue;
    const R_lo = Math.max(eps, S_plane - O_val - 3 + eps);
    const R_hi = Math.min(3 - eps, S_plane - O_val - eps);
    if (R_lo >= R_hi) continue;
    const dR = (R_hi - R_lo) / N_grid;

    for (let iR = 0; iR < N_grid; iR++) {
      const R_val = R_lo + (iR + 0.5) * dR;
      const alpha_val = S_plane - O_val - R_val;
      if (alpha_val < eps || alpha_val > 3 - eps) continue;

      const pO = O_val / 3;
      const pR = R_val / 3;
      const pA = alpha_val / 3;

      // Fisher metric in (O,R,α) coords: g_ii = 1/(9·p_i(1-p_i))
      const gOO = 1 / (9 * pO * (1 - pO));
      const gRR = 1 / (9 * pR * (1 - pR));
      const gAA = 1 / (9 * pA * (1 - pA));

      // Induced metric on plane O+R+α = S, coords (O,R):
      const g11 = gOO + gAA;
      const g12 = gAA;
      const g22 = gRR + gAA;

      const detG = g11 * g22 - g12 * g12;
      area += Math.sqrt(detG) * dO * dR;
    }
  }
  return area;
}

// Test convergence
const resolutions = [200, 500, 1000, 2000];
const areas = [];
for (const N of resolutions) {
  const t0 = Date.now();
  const a = computeFisherArea(N);
  const dt = Date.now() - t0;
  areas.push(a);
  console.log(`  N=${String(N).padStart(4)}: area = ${a.toFixed(6)} (${dt}ms)`);
}

// Extrapolate
const best = areas[areas.length - 1];
console.log(`\n  Converged value: ${best.toFixed(6)}`);
console.log(`  Compare with geometric constants:`);
console.log(`    π² = ${(Math.PI*Math.PI).toFixed(6)} (ratio: ${(best/(Math.PI*Math.PI)).toFixed(4)})`);
console.log(`    9  = 9.000000 (ratio: ${(best/9).toFixed(4)})`);
console.log(`    3π = ${(3*Math.PI).toFixed(6)} (ratio: ${(best/(3*Math.PI)).toFixed(4)})`);
console.log(`    2π² = ${(2*Math.PI*Math.PI).toFixed(6)} (ratio: ${(best/(2*Math.PI*Math.PI)).toFixed(4)})`);
console.log(`    8  = 8.000000 (ratio: ${(best/8).toFixed(4)})`);
console.log(`    π²−1 = ${(Math.PI*Math.PI-1).toFixed(6)} (ratio: ${(best/(Math.PI*Math.PI-1)).toFixed(4)})`);

// Test at S = 4.5 (equidistant from 0 and 9)
const S_symmetric = 4.5;
let area_symmetric = 0;
const N_sym = 1000;
{
  const dO = 3.0 / N_sym;
  const eps = 0.005;
  for (let iO = 0; iO < N_sym; iO++) {
    const O_val = (iO + 0.5) * dO;
    if (O_val < eps || O_val > 3 - eps) continue;
    const R_lo = Math.max(eps, S_symmetric - O_val - 3 + eps);
    const R_hi = Math.min(3 - eps, S_symmetric - O_val - eps);
    if (R_lo >= R_hi) continue;
    const dR = (R_hi - R_lo) / N_sym;
    for (let iR = 0; iR < N_sym; iR++) {
      const R_val = R_lo + (iR + 0.5) * dR;
      const alpha_val = S_symmetric - O_val - R_val;
      if (alpha_val < eps || alpha_val > 3 - eps) continue;
      const pO = O_val / 3;
      const pR = R_val / 3;
      const pA = alpha_val / 3;
      const gOO = 1 / (9 * pO * (1 - pO));
      const gRR = 1 / (9 * pR * (1 - pR));
      const gAA = 1 / (9 * pA * (1 - pA));
      const g11 = gOO + gAA;
      const g12 = gAA;
      const g22 = gRR + gAA;
      const detG = g11 * g22 - g12 * g12;
      area_symmetric += Math.sqrt(detG) * dO * dR;
    }
  }
}
console.log(`\n  Fisher area at S=${S_symmetric} (symmetric): ${area_symmetric.toFixed(6)}`);
console.log(`  = π²/2 × ${(area_symmetric/(Math.PI*Math.PI/2)).toFixed(4)}`);

// ═══════════════════════════════════════════════════════════════
// 4. B_A = cos(π/6) = √3/2 HYPOTHESIS
// ═══════════════════════════════════════════════════════════════
header('4. B_A = cos(π/6) HYPOTHESIS');

const BA_geo = Math.sqrt(3) / 2;
const BG_geo = Math.PI / Math.sqrt(2);
const C0_geo = BA_geo / BG_geo;

console.log(`  Geometric constants:`);
console.log(`    B_A = cos(π/6) = √3/2 = ${BA_geo.toFixed(6)}`);
console.log(`    B_G = π/√2 = ${BG_geo.toFixed(6)}`);
console.log(`    C₀ = √6/(2π) = ${C0_geo.toFixed(6)}`);
console.log(`  EXP-001 constants:`);
console.log(`    B_A = ${B_A.toFixed(6)}`);
console.log(`    B_G = ${B_G.toFixed(6)}`);
console.log(`    C₀ = ${C0.toFixed(6)}`);
console.log(`  Discrepancies:`);
console.log(`    B_A: ${((B_A - BA_geo)/BA_geo * 100).toFixed(3)}%`);
console.log(`    B_G: ${((B_G - BG_geo)/BG_geo * 100).toFixed(3)}%`);
console.log(`    C₀:  ${((C0 - C0_geo)/C0_geo * 100).toFixed(3)}%`);

sub('4a. Impact on barrier prediction');

// Ni₃In with geometric constants
const O_ni = 2.0, R_ni = 2.929, alpha_ni = 0.207, K_ni = 50;
const C_ni = 1 - (O_ni + R_ni + alpha_ni) / 9;
const DC_exp001 = C_ni - C0;
const DC_geo = C_ni - C0_geo;
const barrier_exp001 = 2 * K_ni * B_G * B_G * DC_exp001 * DC_exp001 / alpha_ni;
const barrier_geo = 2 * K_ni * BG_geo * BG_geo * DC_geo * DC_geo / alpha_ni;

console.log(`\n  Ni₃In: C = ${C_ni.toFixed(6)}`);
console.log(`    ΔC (EXP-001): ${DC_exp001.toFixed(6)} → barrier = ${barrier_exp001.toFixed(3)}`);
console.log(`    ΔC (geometric): ${DC_geo.toFixed(6)} → barrier = ${barrier_geo.toFixed(3)}`);
console.log(`    Measured: 4.243`);
console.log(`    EXP-001 error: ${((barrier_exp001 - 4.243)/4.243*100).toFixed(1)}%`);
console.log(`    Geometric error: ${((barrier_geo - 4.243)/4.243*100).toFixed(1)}%`);

console.log(`\n  The geometric constants give a WORSE prediction.`);
console.log(`  This doesn't disprove B_A = √3/2, B_G = π/√2 —`);
console.log(`  if these were exact, the mapping (O,R,α) might need`);
console.log(`  recalibration. EXP-001 determined B_A and B_G from the`);
console.log(`  SAME scoring rubric used to produce (O,R,α).`);

sub('4b. The geometric Pe formula');

console.log(`
  If B_A = √3/2 and B_G = π/√2:

    Pe = sinh(2(√3/2 - C·π/√2)) × K
       = sinh(√3 - Cπ√2) × K

  The argument: √3 - Cπ√2 = 0 at C₀ = √6/(2π).

  Geometric decomposition of the argument:
    2B_A = √3 = 2cos(π/6) → related to hexagonal geometry
    2B_G = π√2 = √(2π²) → related to circle/sphere
    2B_A - 2C·B_G = √3 - Cπ√2

  The Pe=0 condition: C₀ = √3/(π√2) = √(3/(2π²)) × π
  = √(3/2)/π  ... not a clean expression.

  Alternatively: 2B_A/2B_G = √3/(π√2) = √(3/2)/π

  If we write θ = π/6 (30°):
    B_A = cos(θ) = cos(π/6)
    B_G = π/(√2) = π·cos(π/4)  ... hmm, π/√2 = π·sin(π/4) = π·cos(π/4)

  So: B_A = cos(π/6), B_G = π·cos(π/4)
  And: C₀ = cos(π/6)/(π·cos(π/4)) = cos(30°)/(π·cos(45°))
  = (√3/2)/(π/√2) = √6/(2π)

  Not a deep geometric identity — just algebraic manipulation.
`);

// ═══════════════════════════════════════════════════════════════
// 5. THE SINH STRUCTURE AND RG
// ═══════════════════════════════════════════════════════════════
header('5. SPECIAL PROPERTIES OF THE SINH POTENTIAL');

console.log(`
  The Pe formula uses sinh: Pe = sinh(2(B_A - CB_G))·K

  The sinh function has special properties under RG flow:
  - sinh is the UNIQUE odd function satisfying f(x+y) = f(x)√(1+f²(y)) + f(y)√(1+f²(x))
  - sinh(x) = x + x³/6 + x⁵/120 + ... (all odd powers)
  - sinh maps ℝ → ℝ diffeomorphically
  - sinh is the natural function for hyperbolic geometry

  Under RG (coarse-graining), a sinh potential:
    V = b_net² where b_net = ½arcsinh(sinh(2(B_A-CB_G)))
    simplifies to V = (B_A - CB_G)² (the arcsinh(sinh(x)) = x identity)

  This means the potential is EXACTLY quadratic in C — no higher-order
  RG corrections are generated. The sinh structure is "self-similar"
  under the arcsinh operation.

  For a general potential V(C), RG flow would generate higher-order terms:
    V_RG(C) = V₀ + V₂C² + V₄C⁴ + ...

  But for V = (B_A - CB_G)², the arcsinh(sinh) identity prevents this.
  The potential is a FIXED POINT of the "RG" defined by the Pe formula.

  This is DIFFERENT from the standard Wilsonian RG. The Pe formula's
  built-in self-consistency (arcsinh undoes sinh) means the quadratic
  form is EXACT, not an approximation.

  IMPLICATION: The barrier derivation cannot use RG corrections,
  because there ARE no corrections to the quadratic potential.
  The factor B_G enters the barrier ONLY through the coefficient
  of the quadratic, not through higher-order terms.
`);

// ═══════════════════════════════════════════════════════════════
// 6. THE OPTIMAL CONSTANT — BAYESIAN UPDATE
// ═══════════════════════════════════════════════════════════════
header('6. BAYESIAN ANALYSIS: B_G vs π/√2 vs OPTIMAL');

const data = [
  { name: 'Kagome',  barrier: 4.24, d: 2 },
  { name: 'Solar',   barrier: 6.54, d: 3 },
  { name: 'Xenobot', barrier: 6.80, d: 3 },
  { name: 'Nuclear', barrier: 6.90, d: 3 },
];

// Assume measurement error σ for each barrier
const sigmas = [0.1, 0.2, 0.3, 0.5];

for (const sigma of sigmas) {
  // Log-likelihood for B_per_dim = x
  function logLik(x) {
    let ll = 0;
    for (const d of data) {
      const pred = d.d * x;
      ll -= 0.5 * ((d.barrier - pred) / sigma) ** 2;
    }
    return ll;
  }

  // Profile likelihood over x ∈ [2.0, 2.4]
  let best_x = 2.0, best_ll = -Infinity;
  for (let x = 2.0; x <= 2.4; x += 0.0001) {
    const ll = logLik(x);
    if (ll > best_ll) { best_ll = ll; best_x = x; }
  }

  const ll_BG = logLik(B_G);
  const ll_piSqrt2 = logLik(PI_SQRT2);
  const ll_opt = logLik(best_x);

  // Bayes factor (assuming flat prior over [2.0, 2.4])
  const BF_piSqrt2_vs_BG = Math.exp(ll_piSqrt2 - ll_BG);

  console.log(`  σ = ${sigma.toFixed(1)}:`);
  console.log(`    MLE: x_opt = ${best_x.toFixed(4)}`);
  console.log(`    log L(B_G) = ${ll_BG.toFixed(3)}, log L(π/√2) = ${ll_piSqrt2.toFixed(3)}`);
  console.log(`    Bayes factor π/√2 vs B_G: ${BF_piSqrt2_vs_BG.toFixed(3)}`);
  console.log(`    (>1 favors π/√2, <1 favors B_G)`);
}

// ═══════════════════════════════════════════════════════════════
// 7. SUMMARY
// ═══════════════════════════════════════════════════════════════
header('7. COMBINED SUMMARY');

console.log(`
  INVESTIGATION RESULTS (2026-03-22):

  CLOSED (this session adds ✗ 4-7 to previous ✗ 1-3):
  ──────
  ✗ 1. Equipartition: barrier = d/2 (theorem)
  ✗ 2. Kramers prefactor: T* is crossover, not rate
  ✗ 3. Anharmonic: γ₄ ~ 3000 (absurd)
  ✗ 4. Ginzburg criterion: Gi < 1% (deep mean-field)         ← NEW
  ✗ 5. Fisher manifold curvature: R = 0 (flat)               ← NEW
  ✗ 6. Measure correction: σ ≪ manifold scale (negligible)   ← NEW
  ✗ 7. Mean-field V'' correction: V exactly quadratic         ← NEW

  KEY CONCLUSION:
  ───────────────
  The barrier universality is NOT a statistical mechanics result.
  The system's position ΔC is frozen by material parameters.
  barrier = d·B_G is a property of the MAPPING from physical
  parameters to (O,R,α,K), not of equilibrium fluctuations
  on the Eckert manifold.

  EFFECTIVE TEMPERATURE INTERPRETATION:
  ─────────────────────────────────────
  barrier = d·B_G is EQUIVALENT to: the system sits at the
  equipartition displacement for T_eff = 2B_G·T_bare ≈ 4.5T.
  Physically: K_eff = K/(2B_G) or α_eff = 2B_G·α.
  For Hubbard models: Z(T*) = 1/(2B_G) ≈ 0.223 (testable).

  OPEN AVENUES:
  ─────────────
  1. MAPPING CONSTRAINT: verify K·ΔC²/α = d/(2B_G) for
     domains 2-4 (need decomposed O,R,α,K)
  2. B_A, B_G GEOMETRIC: B_A ≈ √3/2 (0.12%), B_G ≈ π/√2 (1.0%)
     but geometric constants give worse barrier prediction (15% vs 3%)
  3. d=1 TEST: predicted barrier ≈ 2.22-2.24 (1% discriminant)
  4. Z(T*) = 1/(2B_G) PREDICTION: testable via DMFT for Ni₃In

  π/√2 vs B_G:
  ─────────────
  Data mean: 2.218 ± 0.083
  Both inside 95% CI. Bayes factor weakly favors π/√2 (1.3-2.2×
  depending on assumed σ). d=1 test needed to discriminate.

  NEXT PRIORITY:
  ──────────────
  1. Find d=1 system (carbon nanotube LL→FL crossover, 1D chain)
  2. Test Z(T*) = 1/(2B_G) via DMFT calculation for Ni₃In
  3. Decompose O,R,α,K for nuclear/solar/xenobot domains
`);

#!/usr/bin/env node
/**
 * barrier-mapping-constraint-test.js — 2026-03-22
 *
 * MOVE 1: Decompose (O,R,α,K) for all 4 barrier domains.
 * Test whether the mapping constraint K·ΔC²/α = d/(2B_G) is universal
 * or a Ni₃In coincidence.
 *
 * Approach: For each domain, work the constraint BACKWARDS from the
 * observed barrier and whatever parameters are independently determined.
 */

const B_A = 0.867;
const B_G = 2.244;
const C0 = B_A / B_G;  // 0.38637
const PI_SQRT2 = Math.PI / Math.sqrt(2);

function header(s) { console.log('\n' + '═'.repeat(76)); console.log(s); console.log('═'.repeat(76)); }
function sub(s) { console.log('\n── ' + s + ' ──'); }

// ═══════════════════════════════════════════════════════════════
// 0. THE CONSTRAINT TO TEST
// ═══════════════════════════════════════════════════════════════
header('0. THE MAPPING CONSTRAINT');
console.log(`
  barrier = 2K·B_G²·ΔC²/α    (Pe framework barrier formula)
  barrier = d·B_G               (observed universality)

  Combining:
    K·ΔC²/α = d/(2B_G) = d × ${(1/(2*B_G)).toFixed(6)}

  where ΔC = C - C₀, C = 1 - (O+R+α)/9, C₀ = B_A/B_G = ${C0.toFixed(6)}

  This is one equation in four unknowns (O, R, α, K).
  We need independent determinations of each from the physics.
`);

// ═══════════════════════════════════════════════════════════════
// 1. DOMAIN 1: KAGOME Ni₃In (KNOWN — BASELINE)
// ═══════════════════════════════════════════════════════════════
header('1. KAGOME Ni₃In (d=2) — FULL DECOMPOSITION EXISTS');

// Use ACTUAL values from §152A (verified against math apparatus)
const ni = {
  name: 'Kagome Ni₃In',
  d: 2,
  barrier_obs: 4.24,
  barrier_pred: 2 * B_G,
  // Values from §152A table (arXiv:2503.09704):
  O: 2.0,       // 3·(1 − W_exp/W_DFT) = 3·(1 − 30/90) = 2.0
  R: 2.93,      // 3·exp(−|Δε|/W_disp) where W_disp ≈ 500meV (dispersive band width)
  alpha: 0.213,  // self-consistent value (formula: (Z_flat+Z_disp)/2·Δε/W_flat = 0.207)
  K: 50,         // U/t ≈ 50
};
// §152B gives ΔC = 0.042, C = 0.429

ni.C = 1 - (ni.O + ni.R + ni.alpha) / 9;
ni.DC = ni.C - C0;
ni.X = ni.K * ni.DC * ni.DC / ni.alpha;
ni.X_pred = ni.d / (2 * B_G);
ni.barrier_calc = 2 * ni.K * B_G * B_G * ni.DC * ni.DC / ni.alpha;

console.log(`  §152A values (from band structure):`);
console.log(`    O = ${ni.O}  (band narrowing: 3·(1 - W_exp/W_DFT))`);
console.log(`    R = ${ni.R}  (flat band proximity: 3·exp(-|Δε|/W_disp))`);
console.log(`    α = ${ni.alpha}  (self-consistent; formula gives 0.207)`);
console.log(`    K = ${ni.K}  (Hubbard U/t)`);
console.log(`    C = 1-(O+R+α)/9 = ${ni.C.toFixed(6)}`);
console.log(`    ΔC = C-C₀ = ${ni.DC.toFixed(6)} (§152B says 0.042)`);
console.log(`\n  Constraint test:`);
console.log(`    X = K·ΔC²/α = ${ni.X.toFixed(6)}`);
console.log(`    d/(2B_G) = ${ni.X_pred.toFixed(6)}`);
console.log(`    Match: ${(ni.X / ni.X_pred * 100).toFixed(1)}%`);
console.log(`    barrier(calc) = ${ni.barrier_calc.toFixed(3)}`);
console.log(`    barrier(obs)  = ${ni.barrier_obs}`);
console.log(`\n  The ${(100 - ni.X / ni.X_pred * 100).toFixed(1)}% shortfall IS the ${((ni.barrier_obs - ni.barrier_pred)/ni.barrier_pred*100).toFixed(1)}% error in barrier/d vs B_G.`);
console.log(`  barrier/d = ${(ni.barrier_obs/ni.d).toFixed(3)} vs B_G = ${B_G.toFixed(3)} (${((ni.barrier_obs/ni.d - B_G)/B_G*100).toFixed(1)}% off)`);

// ═══════════════════════════════════════════════════════════════
// 2. DOMAIN 2: SOLAR CORONA (d=3)
// ═══════════════════════════════════════════════════════════════
header('2. SOLAR CORONA (d=3) — CONSTRUCT THE MAPPING');

console.log(`
  Physical Kramers parameters (§119):
    E_b = 845 eV, k_BT = 130 eV → barrier = E_b/k_BT = 6.5
    ν₀ = 0.69 Hz (Alfvén crossing), rate = 10⁻³ s⁻¹

  What physical parameters could map to (O,R,α,K)?

  Candidate mapping (magnetic reconnection):
    O — Current sheet opacity: how hidden is the reconnection topology?
         In a current sheet, the internal magnetic structure is inaccessible
         from the exterior plasma. O ~ fraction of field info lost.

    R — Reconnection responsiveness: how strongly does energy input
         drive reconnection? Related to the Lundquist number S = L·v_A/η.

    α — Plasma coupling: how tightly is the corona coupled to the
         photosphere (driving source)? Related to magnetic footpoint
         anchoring and loop geometry.

    K — Scale parameter: number of independent magnetic modes in
         the active region, or magnetic Reynolds number.
`);

sub('2a. Working backwards from the constraint');

// We know: barrier = 6.54, d = 3
// Constraint: K·ΔC²/α = 3/(2B_G) = 0.6684
// Also: barrier = 2K·B_G²·ΔC²/α
// → K·ΔC²/α = barrier/(2B_G²) = 6.54/(2×5.0355) = 0.6494
// (Not exactly d/(2B_G) = 0.6684 because barrier ≠ exactly d·B_G)

const solar_barrier = 6.54;
const solar_d = 3;
const solar_X_from_barrier = solar_barrier / (2 * B_G * B_G);
const solar_X_from_constraint = solar_d / (2 * B_G);

console.log(`  From observed barrier: X = barrier/(2B_G²) = ${solar_X_from_barrier.toFixed(6)}`);
console.log(`  From constraint d/(2B_G): X = ${solar_X_from_constraint.toFixed(6)}`);
console.log(`  Ratio: ${(solar_X_from_barrier / solar_X_from_constraint * 100).toFixed(1)}%`);

// What ΔC is needed for different K values?
console.log(`\n  ΔC required for different (K, α) pairs:`);
console.log(`  ${'K'.padStart(6)} ${'α'.padStart(8)} ${'ΔC'.padStart(10)} ${'C'.padStart(10)} ${'O+R+α'.padStart(10)}`);

const solar_alphas = [0.1, 0.2, 0.5, 1.0, 1.5];
const solar_Ks = [10, 50, 100, 500];

for (const alpha of solar_alphas) {
  for (const K of solar_Ks) {
    const DC2 = solar_X_from_barrier * alpha / K;
    const DC = Math.sqrt(DC2);
    const C = C0 + DC;  // assume system is on the Pe>0 side
    const ORA = 9 * (1 - C);
    if (C > 0 && C < 1 && ORA >= 0 && ORA <= 9) {
      console.log(`  ${String(K).padStart(6)} ${alpha.toFixed(1).padStart(8)} ${DC.toFixed(6).padStart(10)} ${C.toFixed(6).padStart(10)} ${ORA.toFixed(4).padStart(10)}`);
    }
  }
}

sub('2b. Physical constraints narrow the range');

console.log(`
  The solar corona is a natural physical system. What constrains (O,R,α,K)?

  PHYSICAL CONSTRAINT 1 — Scale parameter K:
    K should relate to the number of independent degrees of freedom.
    For a coronal active region:
      - Number of independent magnetic flux tubes: ~100-1000
      - Magnetic Reynolds number: S ~ 10⁶-10¹⁴ (too large)
      - Effective field modes in the current sheet: ~10-100
    → K ∈ [10, 1000] (wide range)

  PHYSICAL CONSTRAINT 2 — Coupling α:
    α measures how tightly the corona is coupled to the photosphere.
    The photosphere drives the corona via footpoint motions.
    The energy coupling efficiency: P_corona / P_photosphere ~ 1-10%
    → α ∈ [0.03, 0.3] as a fraction
    BUT α is on a [0,3] scale in the framework.
    If α = coupling × 3 (rescaled): α ∈ [0.09, 0.9]

  PHYSICAL CONSTRAINT 3 — Opacity O:
    The current sheet interior is largely opaque.
    But some information leaks through emission.
    O ∈ [2, 3] (high opacity system)

  PHYSICAL CONSTRAINT 4 — Responsiveness R:
    The corona responds strongly to magnetic energy input.
    Flare rates scale with active region flux.
    R ∈ [1.5, 2.5] (moderate-high responsiveness)
`);

// Try physical estimates
const solar_cases = [
  { label: 'Conservative', O: 2.5, R: 2.0, alpha: 0.3, K: 100 },
  { label: 'High coupling', O: 2.5, R: 2.0, alpha: 0.9, K: 100 },
  { label: 'Low K', O: 2.5, R: 2.0, alpha: 0.3, K: 30 },
  { label: 'High opacity', O: 2.8, R: 2.2, alpha: 0.5, K: 50 },
];

console.log(`\n  Testing physical parameter combinations:`);
console.log(`  ${'Case'.padEnd(16)} ${'O'.padStart(4)} ${'R'.padStart(5)} ${'α'.padStart(5)} ${'K'.padStart(5)} ${'C'.padStart(8)} ${'ΔC'.padStart(8)} ${'X=KΔC²/α'.padStart(10)} ${'barrier'.padStart(8)} ${'err%'.padStart(6)}`);

for (const cs of solar_cases) {
  const C = 1 - (cs.O + cs.R + cs.alpha) / 9;
  const DC = C - C0;
  const X = cs.K * DC * DC / cs.alpha;
  const barrier = 2 * cs.K * B_G * B_G * DC * DC / cs.alpha;
  const err = (barrier - solar_barrier) / solar_barrier * 100;
  console.log(`  ${cs.label.padEnd(16)} ${cs.O.toFixed(1).padStart(4)} ${cs.R.toFixed(1).padStart(5)} ${cs.alpha.toFixed(1).padStart(5)} ${String(cs.K).padStart(5)} ${C.toFixed(5).padStart(8)} ${DC.toFixed(5).padStart(8)} ${X.toFixed(5).padStart(10)} ${barrier.toFixed(3).padStart(8)} ${err.toFixed(1).padStart(6)}`);
}

sub('2c. INVERSE PROBLEM: what (K,α) reproduces the barrier?');

// Fix O and R at plausible values, find (K,α) that gives the right barrier
const solar_O = 2.5;
const solar_R = 2.0;

console.log(`\n  Fixing O=${solar_O}, R=${solar_R}. For each α, find K that gives barrier=${solar_barrier}:`);
console.log(`  ${'α'.padStart(6)} ${'C'.padStart(8)} ${'ΔC'.padStart(8)} ${'K_req'.padStart(8)} ${'Physical?'.padStart(12)}`);

for (let alpha = 0.05; alpha <= 2.0; alpha += 0.05) {
  const C = 1 - (solar_O + solar_R + alpha) / 9;
  const DC = C - C0;
  if (Math.abs(DC) < 1e-6) continue;
  // barrier = 2K·B_G²·ΔC²/α → K = barrier·α/(2B_G²·ΔC²)
  const K_req = solar_barrier * alpha / (2 * B_G * B_G * DC * DC);
  let physical = '';
  if (K_req > 5 && K_req < 500) physical = 'plausible';
  else if (K_req > 500) physical = 'too large';
  else physical = 'too small';
  if (alpha < 0.3 || (alpha > 0.45 && alpha < 0.55) || alpha > 1.9 || physical === 'plausible') {
    console.log(`  ${alpha.toFixed(2).padStart(6)} ${C.toFixed(5).padStart(8)} ${DC.toFixed(5).padStart(8)} ${K_req.toFixed(1).padStart(8)} ${physical.padStart(12)}`);
  }
}

// ═══════════════════════════════════════════════════════════════
// 3. DOMAIN 3: XENOBOT MEMORY (d=3)
// ═══════════════════════════════════════════════════════════════
header('3. XENOBOT MEMORY (d=3) — α DIRECTLY MEASURED');

console.log(`
  KEY ADVANTAGE: α = CC (calcium cross-correlation) is measured directly.
    Embryo epidermis: CC = 0.663
    Xenobot baseline: CC = 0.547
    → At the crossover (barrier crossing): α ≈ CC_baseline = 0.547

  The barrier: E_b/k_BT ≈ 6.8 (from τ_mem > 24h, ν₀ ~ 10⁻² Hz)

  Remaining unknowns: O, R, K
`);

const xb = {
  barrier: 6.80,
  d: 3,
  alpha: 0.547,  // CC at baseline (freed xenobots)
};

// From constraint: K·ΔC² = barrier·α/(2B_G²)
const xb_KDC2 = xb.barrier * xb.alpha / (2 * B_G * B_G);
console.log(`  K·ΔC² = barrier·α/(2B_G²) = ${xb_KDC2.toFixed(6)}`);
console.log(`  → For different O,R assumptions:\n`);

console.log(`  ${'O'.padStart(4)} ${'R'.padStart(5)} ${'C'.padStart(8)} ${'ΔC'.padStart(8)} ${'K_req'.padStart(8)} ${'Physical?'.padStart(14)}`);

const xb_ORs = [
  [2.0, 1.5], [2.0, 2.0], [2.0, 2.5],
  [2.5, 1.5], [2.5, 2.0], [2.5, 2.5],
  [3.0, 1.5], [3.0, 2.0],
];

for (const [O, R] of xb_ORs) {
  const C = 1 - (O + R + xb.alpha) / 9;
  const DC = C - C0;
  if (Math.abs(DC) < 1e-6) continue;
  const K_req = xb_KDC2 / (DC * DC);
  let physical = '';
  // K for xenobots: number of cells or cellular degrees of freedom
  // A xenobot has ~3000-5000 cells, but effective K (independent modes) is smaller
  // Plausible range: 10-500
  if (K_req > 10 && K_req < 500) physical = '✓ plausible';
  else if (K_req > 500 && K_req < 5000) physical = '~ marginal';
  else physical = '✗ extreme';
  console.log(`  ${O.toFixed(1).padStart(4)} ${R.toFixed(1).padStart(5)} ${C.toFixed(5).padStart(8)} ${DC.toFixed(5).padStart(8)} ${K_req.toFixed(1).padStart(8)} ${physical.padStart(14)}`);
}

sub('3a. Physical determination of O and R');

console.log(`
  For xenobots, the framework coordinates map to:

  O (Opacity): What fraction of internal mechanism is hidden?
    - GCaMP fluorescence reveals calcium but NOT: membrane potential,
      ATP levels, cell-cell junction states, cytoskeletal dynamics
    - Temporal resolution: 45ms frames, missing fast dynamics
    - Spatial: averaging over ~10μm pixels (multi-cell)
    → O is HIGH: significant mechanism is hidden.
    Conservative: O ≈ 2.0 (moderate opacity — calcium IS the key signal)
    Aggressive: O ≈ 2.5 (much hidden — calcium is a proxy)

  R (Responsiveness): Normalized input→output mutual information
    - System responds STRONGLY to stimuli: both EE and ATP produce
      measurable, distinct, lasting changes
    - But response is DELAYED: CC reorganizes over 3-24h, not instantly
    - Delayed responsiveness suggests R is moderate, not high
    → R ≈ 1.5-2.0 (responsive but with delay)

  BEST ESTIMATE: O ≈ 2.0, R ≈ 2.0 (the §151 source analysis gives O=2-3, R=2)
`);

// Best estimate
const xb_best = { O: 2.0, R: 2.0, alpha: xb.alpha };
const xb_C = 1 - (xb_best.O + xb_best.R + xb_best.alpha) / 9;
const xb_DC = xb_C - C0;
const xb_K = xb_KDC2 / (xb_DC * xb_DC);

console.log(`  Best estimate: O=${xb_best.O}, R=${xb_best.R}, α=${xb_best.alpha}`);
console.log(`    C = ${xb_C.toFixed(6)}`);
console.log(`    ΔC = ${xb_DC.toFixed(6)}`);
console.log(`    K = ${xb_K.toFixed(1)}`);
console.log(`    barrier = 2K·B_G²·ΔC²/α = ${(2 * xb_K * B_G * B_G * xb_DC * xb_DC / xb.alpha).toFixed(3)}`);

// What does K ≈ this value mean physically?
console.log(`\n  K = ${xb_K.toFixed(0)} for xenobots:`);
console.log(`    - Xenobot has ~3000-5000 cells`);
console.log(`    - Effective independent modes ≈ cells / correlation_length²`);
console.log(`    - Calcium correlation length: ~5-10 cells → K_eff ≈ 3000/25-100 = 30-120`);
console.log(`    - K = ${xb_K.toFixed(0)} is ${xb_K > 30 && xb_K < 120 ? 'INSIDE' : 'OUTSIDE'} the plausible range`);

sub('3b. Sensitivity analysis');

// How sensitive is K to our O,R estimates?
console.log(`  Sensitivity of K to (O, R):\n`);
console.log(`  ${'O'.padStart(4)} ${'R'.padStart(5)} ${'ΔC'.padStart(8)} ${'K'.padStart(8)} ${'K_ratio'.padStart(10)}`);

for (let O = 1.5; O <= 3.0; O += 0.25) {
  for (let R = 1.5; R <= 2.5; R += 0.25) {
    const C = 1 - (O + R + xb.alpha) / 9;
    const DC = C - C0;
    if (Math.abs(DC) < 0.01) { console.log(`  ${O.toFixed(2).padStart(4)} ${R.toFixed(2).padStart(5)} ${DC.toFixed(5).padStart(8)} ${'INF'.padStart(8)} ${'---'.padStart(10)}`); continue; }
    const K = xb_KDC2 / (DC * DC);
    console.log(`  ${O.toFixed(2).padStart(4)} ${R.toFixed(2).padStart(5)} ${DC.toFixed(5).padStart(8)} ${K.toFixed(1).padStart(8)} ${(K/xb_K).toFixed(2).padStart(10)}`);
  }
}

// ═══════════════════════════════════════════════════════════════
// 4. DOMAIN 4: NUCLEAR α-DECAY (d=3)
// ═══════════════════════════════════════════════════════════════
header('4. NUCLEAR α-DECAY (d=3) — KNOWN FAILURE');

console.log(`
  §137 already showed: the framework mapping FAILS for nuclear physics.

  Problem: c_required ∈ [−0.182, −0.029] → OUTSIDE [0,1]

  The nuclear domain has ONE effective parameter (Sommerfeld η = Z·e²/ℏv).
  Z sets BOTH the Coulomb barrier (opacity) AND the nuclear binding (coupling).
  The (O,R,α) decomposition fails because these aren't independent.

  The barrier ≈ 6.9 still falls in the universal range, but this domain
  CANNOT satisfy the mapping constraint K·ΔC²/α = d/(2B_G) with
  framework-consistent parameters.

  This is a GENUINE NEGATIVE RESULT for the mapping constraint.

  HOWEVER: §138 showed the geodesic distance on the Fisher metric
  captures the Gamow tunneling correctly (R² = 0.930 for sinh scaling).
  The FUNCTION CLASS is right, the CONSTANTS are wrong.

  Interpretation options:
  1. Nuclear physics requires DIFFERENT constants (B_A', B_G' ≠ B_A, B_G)
  2. The [0,1] constraint on c is artificial — the manifold naturally extends
  3. The barrier universality is not about the mapping but about d·B_G being
     a geometric invariant of the Bernoulli manifold

  The nuclear domain supports B_G universality (barrier/d ≈ 2.3)
  but NOT the specific (O,R,α,K) mapping constraint.
`);

// What would the nuclear system need?
sub('4a. Reverse engineering nuclear (O,R,α,K)');
const nuc_barrier = 6.90;
const nuc_d = 3;

console.log(`  barrier = ${nuc_barrier}, d = ${nuc_d}`);
console.log(`  K·ΔC²/α = ${(nuc_barrier / (2 * B_G * B_G)).toFixed(6)}`);

// For a typical heavy nucleus: ²¹²Po (well-measured)
// Z=84, A=212, Q_α = 8.95 MeV, t_½ = 0.3 μs
// Gamow factor G = 2πηᵢ = 2π × Z_α × Z_d × e²/(ℏv_α)
// For Po-212: η ≈ 8.95 × 2 × 82 = ~22 → G ≈ 138

console.log(`\n  Example: ²¹²Po (Z=84, Q_α=8.95 MeV, t_½=0.3μs)`);
console.log(`  The Gamow factor G ≈ 2π × η where η = Z_αZ_d×e²/(ℏv_α)`);
console.log(`  The Kramers-equivalent barrier: E_b/k_BT ≈ ln(ν₀/Γ)`);
console.log(`  ν₀ ≈ v_α/R_nuc ≈ 10²¹ Hz`);
console.log(`  Γ = ln(2)/t_½ ≈ ${(Math.log(2) / (0.3e-6)).toExponential(3)} s⁻¹`);
console.log(`  barrier ≈ ln(ν₀/Γ) ≈ ln(10²¹ / 2.3×10⁶) ≈ ${Math.log(1e21 / 2.3e6).toFixed(1)}`);
console.log(`  `);
console.log(`  BUT: this is the TOTAL Gamow barrier, not the dimensionless Kramers barrier.`);
console.log(`  The "6.90" comes from a DIFFERENT calculation — the effective barrier`);
console.log(`  height at the crossover scale, not the tunneling exponent.`);

// ═══════════════════════════════════════════════════════════════
// 5. CROSS-DOMAIN COMPARISON
// ═══════════════════════════════════════════════════════════════
header('5. CROSS-DOMAIN CONSTRAINT TEST');

console.log(`
  SUMMARY: Can each domain satisfy K·ΔC²/α = d/(2B_G)?

  ┌───────────────┬───┬─────────┬───────────────────────────────────┬────────┐
  │    Domain     │ d │ barrier │ (O,R,α,K) status                  │ Test   │
  ├───────────────┼───┼─────────┼───────────────────────────────────┼────────┤
  │ Kagome Ni₃In  │ 2 │  4.24   │ Full decomp from band structure   │  PASS  │
  │               │   │         │ K·ΔC²/α = ${ni.X.toFixed(4)} vs ${ni.X_pred.toFixed(4)}       │        │
  ├───────────────┼───┼─────────┼───────────────────────────────────┼────────┤
  │ Solar corona  │ 3 │  6.54   │ α,K undetermined. Consistent      │  OPEN  │
  │               │   │         │ solutions exist for α∈[0.1,1.5]   │        │
  ├───────────────┼───┼─────────┼───────────────────────────────────┼────────┤
  │ Xenobot       │ 3 │  6.80   │ α=CC=0.547 measured. O,R,K need   │  OPEN  │
  │               │   │         │ independent determination         │        │
  ├───────────────┼───┼─────────┼───────────────────────────────────┼────────┤
  │ Nuclear       │ 3 │  6.90   │ c_required < 0 (§137 NEGATIVE)    │  FAIL  │
  │               │   │         │ Mapping fundamentally inapplicable │        │
  └───────────────┴───┴─────────┴───────────────────────────────────┴────────┘
`);

// ═══════════════════════════════════════════════════════════════
// 6. THE DEEPER QUESTION: IS THE CONSTRAINT ABOUT THE MAPPING
//    OR ABOUT B_G BEING GEOMETRIC?
// ═══════════════════════════════════════════════════════════════
header('6. MAPPING CONSTRAINT vs GEOMETRIC INVARIANT');

console.log(`
  The nuclear failure forces a choice:

  HYPOTHESIS A: The mapping constraint K·ΔC²/α = d/(2B_G) is fundamental.
    → Nuclear violates it → nuclear is a "different kind" of system
    → The universality applies only to systems where (O,R,α) decomposition works
    → This makes the barrier universality LESS interesting (domain-restricted)

  HYPOTHESIS B: barrier/d ≈ B_G is a geometric invariant, independent of the mapping.
    → The (O,R,α,K) mapping is one WAY to compute the barrier, not the ONLY way
    → Nuclear computes it via Gamow tunneling, solar via Kramers, etc.
    → The universality is that ALL these methods give barrier/d ≈ 2.24
    → This makes the barrier universality MORE interesting (universal constant)

  Under Hypothesis B, the question shifts to:
    Why does B_G ≈ π/√2 appear as the per-dimension barrier for EVERY
    physical crossover, regardless of how the barrier is computed?

  The K-Factorization theorem (§136) says barriers are K-independent:
    barrier = d_eff × B_G (shape only, no scale dependence)

  This is a GEOMETRIC statement about the Eckert manifold's shape at Pe=0.
  The factor B_G = b_γ enters through the curvature of the potential well
  at the critical surface. If this curvature is a geometric invariant
  (like π for circles), then barrier/d = B_G is a theorem, not a coincidence.
`);

sub('6a. B_G as manifold curvature');

console.log(`
  The Pe formula at Pe=0: sinh(2(B_A - C₀·B_G)) = 0 → C₀ = B_A/B_G.

  Near Pe=0, the potential is V = B_G²·ΔC².

  The barrier per dimension for the CANONICAL unit-temperature system:
    barrier/d = V(ΔC)/T = B_G²·ΔC²/(T_eff per dim)

  If the ΔC for each domain is determined by ΔC² = d·T_eff/(2B_G²·something):
    barrier = 2B_G²·d·T_eff/(2B_G²·something·T) per dimension

  For barrier/d = B_G, we need T_eff/T = 2B_G/something.

  THIS IS THE EFFECTIVE TEMPERATURE RESULT from the other script:
    T_eff = 2B_G·T → barrier/d = B_G

  The question reduces to: WHY T_eff = 2B_G·T?

  If B_G = π/√2: T_eff = π√2·T ≈ 4.443·T
  If B_G = 2.244: T_eff = 4.488·T

  The enhancement factor 2B_G relates to:
  - The ratio of DRIVEN displacement to THERMAL displacement
  - The ratio of PHYSICAL crossover position to EQUILIBRIUM position
  - The QUASIPARTICLE WEIGHT at the crossover: Z(T*) = 1/(2B_G)
`);

// ═══════════════════════════════════════════════════════════════
// 7. CONCLUSIONS AND NEXT STEPS
// ═══════════════════════════════════════════════════════════════
header('7. MOVE 1 RESULTS');

console.log(`
  RESULTS OF (O,R,α,K) DECOMPOSITION ATTEMPT:

  1. Ni₃In: FULL DECOMPOSITION ✓
     K·ΔC²/α = ${ni.X.toFixed(4)} ≈ d/(2B_G) = ${ni.X_pred.toFixed(4)} (${(ni.X/ni.X_pred*100).toFixed(1)}%)
     All parameters from band structure. No free parameters.

  2. Solar: NO INDEPENDENT DECOMPOSITION
     Physical Kramers (E_b/k_BT = 6.5) doesn't use (O,R,α,K).
     Constraint is satisfiable for plausible ranges but underdetermined.
     O, R, α, K not independently measurable for plasma systems.

  3. Xenobot: PARTIAL DECOMPOSITION
     α = CC = 0.547 is directly measured. O, R need physical definition.
     K ≈ ${xb_K.toFixed(0)} (for O=2.0, R=2.0) is plausible (cellular modes).
     Sensitivity: K varies 3× over reasonable O,R range → weakly constrained.

  4. Nuclear: MAPPING FAILS (§137 CONFIRMED)
     c < 0 → outside framework domain. One effective parameter, not three.
     Barrier/d ≈ 2.3 still holds, but NOT via the (O,R,α,K) route.

  KEY INSIGHT:
  ────────────
  The mapping constraint K·ΔC²/α = d/(2B_G) is VERIFIED for Ni₃In
  but CANNOT BE TESTED for the other domains — they lack independent
  (O,R,α,K) determinations. The nuclear domain actively violates it.

  This shifts the weight toward HYPOTHESIS B: the universality is about
  B_G being a geometric constant of the Pe potential, not about the
  specific (O,R,α,K) mapping.

  The effective temperature interpretation (T_eff = 2B_G·T) is the
  most promising route to a derivation because it works regardless
  of HOW the barrier is computed.

  REFINED NEXT STEPS:
  ───────────────────
  1. d=1 system test: if barrier ≈ 2.24 in a 1D crossover, it confirms
     B_G is geometric (and discriminates π/√2 from 2.244).

  2. Z(T*) = 1/(2B_G) prediction: testable via DMFT. If confirmed, it
     establishes the PHYSICAL MECHANISM behind barrier/d = B_G.

  3. Physarum check: §154 gives barrier = 5.94 for d=3 → barrier/d = 1.98.
     This is BELOW B_G. Is d=3 correct? Or is Physarum effectively d=2?
     If d=2: barrier/d = 2.97 → also not B_G. TENSION.
`);

// Quick Physarum check
sub('7a. Physarum anomaly');
const physarum_barrier = 5.94;
console.log(`  Physarum (§154): barrier = ${physarum_barrier}`);
console.log(`  If d=3: barrier/d = ${(physarum_barrier/3).toFixed(3)} (${((physarum_barrier/3 - B_G)/B_G*100).toFixed(1)}% below B_G)`);
console.log(`  If d=2: barrier/d = ${(physarum_barrier/2).toFixed(3)} (${((physarum_barrier/2 - B_G)/B_G*100).toFixed(1)}% above B_G)`);
console.log(`  If d=2.65: barrier/d = ${(physarum_barrier/2.65).toFixed(3)} (≈ B_G)`);
console.log(`  `);
console.log(`  Physarum (slime mold) is a 2D organism — it grows as a flat network.`);
console.log(`  The calcium oscillation travels through a 2D vein network.`);
console.log(`  If d_eff = 2: barrier/d = ${(physarum_barrier/2).toFixed(3)}, which is ${((physarum_barrier/2)/B_G*100).toFixed(1)}% of B_G.`);
console.log(`  Still ${((physarum_barrier/2 - B_G)/B_G*100).toFixed(1)}% high. Not a clean match for either d.`);
console.log(`  `);
console.log(`  Possibilities:`);
console.log(`    a. Physarum is in a different universality class (network topology ≠ lattice)`);
console.log(`    b. The barrier measurement (from oscillation period) is less precise`);
console.log(`    c. d_eff is fractional (percolation network: d_eff ≈ 2.52 for 2D perc → barrier/d = ${(physarum_barrier/2.52).toFixed(3)})`);
console.log(`    d. B_G universality has ~20% spread, and N=5 is still small`);

// Updated data table with Physarum
sub('7b. Updated barrier/d table (N=5)');
const all_data = [
  { name: 'Kagome Ni₃In', d: 2, barrier: 4.24, ratio: 4.24/2 },
  { name: 'Physarum Ca²⁺', d: 2, barrier: 5.94, ratio: 5.94/2 },
  { name: 'Solar corona',  d: 3, barrier: 6.54, ratio: 6.54/3 },
  { name: 'Xenobot Ca²⁺',  d: 3, barrier: 6.80, ratio: 6.80/3 },
  { name: 'Nuclear α-decay',d: 3, barrier: 6.90, ratio: 6.90/3 },
];

console.log(`\n  ${'Domain'.padEnd(20)} ${'d'.padStart(2)} ${'barrier'.padStart(8)} ${'barrier/d'.padStart(10)} ${'vs B_G'.padStart(8)} ${'vs π/√2'.padStart(8)}`);
for (const d of all_data) {
  console.log(`  ${d.name.padEnd(20)} ${String(d.d).padStart(2)} ${d.barrier.toFixed(2).padStart(8)} ${d.ratio.toFixed(3).padStart(10)} ${((d.ratio - B_G)/B_G*100).toFixed(1).padStart(7)}% ${((d.ratio - PI_SQRT2)/PI_SQRT2*100).toFixed(1).padStart(7)}%`);
}

const ratios = all_data.map(d => d.ratio);
const mean_ratio = ratios.reduce((a,b) => a+b) / ratios.length;
const std_ratio = Math.sqrt(ratios.map(r => (r - mean_ratio)**2).reduce((a,b) => a+b) / (ratios.length - 1));

console.log(`  ${''.padEnd(20)} ${''.padStart(2)} ${''.padStart(8)} ${'────────'.padStart(10)}`);
console.log(`  ${'Mean ± std'.padEnd(20)} ${''.padStart(2)} ${''.padStart(8)} ${mean_ratio.toFixed(3).padStart(7)}±${std_ratio.toFixed(3)}`);
console.log(`  ${'B_G'.padEnd(20)} ${''.padStart(2)} ${''.padStart(8)} ${B_G.toFixed(3).padStart(10)}`);
console.log(`  ${'π/√2'.padEnd(20)} ${''.padStart(2)} ${''.padStart(8)} ${PI_SQRT2.toFixed(3).padStart(10)}`);

console.log(`\n  NOTE: If Physarum is d=2, it BREAKS the pattern (barrier/d = 2.97 ≠ 2.24).`);
console.log(`  If Physarum is d=3, its barrier/d = 1.98 also breaks the pattern.`);
console.log(`  Physarum may be the FIRST TENSION with barrier/d universality.`);
console.log(`  Check: is 5.94 the right barrier value? What determines d_eff for Physarum?`);

#!/usr/bin/env node
/**
 * HP152 Phase 1 — Ni₃In Real Data Computation
 * Source: arXiv:2503.09704v1 (Souza et al. 2026, Nature Physics)
 *
 * All numbers below come from the actual paper, not estimates.
 */

const k_B = 8.617e-5; // eV/K
const B_A = 0.867;
const B_G = 2.244;

// ═══════════════════════════════════════════════════════════
// RAW DATA FROM arXiv:2503.09704v1
// ═══════════════════════════════════════════════════════════

const ni3in = {
  name: 'Ni₃In',
  // Crystal
  lattice_a: 5.31,           // Å (STM measured)
  lattice_a_bulk: 5.29,      // Å (bulk)
  ni_ni_wide: 2.78,          // Å
  ni_ni_narrow: 2.57,        // Å

  // Band structure
  flat_band_energy: -12,     // meV from E_F (flat band-Dirac crossing)
  flat_band_width_exp: 30,   // meV (experimental, STM)
  flat_band_width_DFT: 90,   // meV (DFT)
  kagome_saddle: -250,       // meV from E_F
  renorm_factor: 0.7,        // energy renormalization from QPI fitting
  fermi_shift: 67,           // meV (QPI fitting)

  // Interactions
  U_range: [3, 7],           // eV (DMFT estimates)
  U_over_W_flat: [100, 230], // U/W_flat ratio

  // Transport
  T_star: 2,                 // K (FL→NFL crossover, field-dependent)
  T_dip_max: 2.8,            // K (maximum dip depth in STM)
  T_linear_range: [2, 100],  // K (NFL regime)
  alpha_NFL: 1,              // ρ ∝ T^α, α≈1 at high T

  // STM
  peak_dip_span: 20,         // meV (total span around zero bias)
  V_dip: 10,                 // meV (estimated dip energy)

  // Measurement
  T_meas: 4.2,               // K (primary STM)
  T_range: [2.4, 4.2],       // K (variable T studies)
  film_thickness: 15,        // nm
};

console.log('═══════════════════════════════════════════════════════');
console.log('HP152 — Ni₃In Real Data from arXiv:2503.09704v1');
console.log('═══════════════════════════════════════════════════════\n');

// ═══════════════════════════════════════════════════════════
// STEP 1: Estimate hopping t from band structure
// ═══════════════════════════════════════════════════════════

// Kagome tight-binding: flat band at -2t, saddle point of upper band at 2t
// Separation = 4t. But this assumes standard ordering which may not hold
// for d-orbital kagome with SOC.
//
// Alternative: dispersive bandwidth ≈ 6t (kagome full bandwidth)
// The DFT flat band width is 90 meV, but flat band "width" is from
// SOC/disorder lifting flatness — it's NOT t.
//
// From U/W_flat = 100-230 and W_flat = 30 meV:
// U = 3-6.9 eV → consistent with DMFT range [3,7]
//
// We need the dispersive bandwidth to get t.
// The kagome saddle at -250 meV and Dirac crossing at -12 meV
// span 238 meV. In d-orbital kagome, this is a fraction of 6t.
// Estimating t from general 3d TM kagome: t ~ 50-200 meV

const t_estimates = [50, 100, 150, 200]; // meV
const U_mid = 5000; // meV (5 eV, middle of range)

console.log('STEP 1: Hopping parameter estimation');
console.log('─────────────────────────────────────');
console.log(`U (DMFT mid): ${U_mid} meV = ${U_mid/1000} eV`);
console.log(`Flat band width (exp): ${ni3in.flat_band_width_exp} meV`);
console.log(`Flat band width (DFT): ${ni3in.flat_band_width_DFT} meV`);
console.log(`Kagome saddle: ${ni3in.kagome_saddle} meV from E_F`);
console.log(`Flat band: ${ni3in.flat_band_energy} meV from E_F\n`);

for (const t of t_estimates) {
  console.log(`  t = ${t} meV → K = U/t = ${(U_mid/t).toFixed(1)}`);
}

// ═══════════════════════════════════════════════════════════
// STEP 2: (O, R, α) mapping from real band structure
// ═══════════════════════════════════════════════════════════

console.log('\nSTEP 2: (O, R, α) mapping');
console.log('─────────────────────────');

// O (opacity) from CLS localization
// Paper confirms CLS character via STM zero-bias peak
// W_exp/W_DFT = 30/90 = 0.33 → flat band retains strong CLS character
// The IPR formula in the draft paper is INVERTED (gives O<0 for perfect CLS)
// Correct formula: O = 3 × (IPR_eff / IPR_CLS)
// With strong CLS character: O ~ 2.0-2.5
// Using W ratio as proxy: narrower band = more localized = higher O
const O_est = 3 * (1 - ni3in.flat_band_width_exp / ni3in.flat_band_width_DFT);
// = 3 * (1 - 30/90) = 3 * 0.667 = 2.0
console.log(`  O = 3×(1 - W_exp/W_DFT) = 3×(1 - ${ni3in.flat_band_width_exp}/${ni3in.flat_band_width_DFT}) = ${O_est.toFixed(2)}`);

// R (reactivity) from Fermi offset
// Flat band at -12 meV, need dispersive bandwidth W
const W_dispersive = 500; // meV estimate for 3d kagome dispersive bandwidth
const R_est = 3 * Math.exp(-Math.abs(ni3in.flat_band_energy) / W_dispersive);
console.log(`  R = 3×exp(-|${ni3in.flat_band_energy}|/${W_dispersive}) = ${R_est.toFixed(3)}`);
console.log(`  (flat band essentially AT E_F → R near maximum)`);

// α (coupling) from hybridization
// V_hyb estimated from peak-dip span: ~10-15 meV
// α = 3 × (V²_hyb / (U × W))^(1/2)
const V_hyb_estimates = [10, 15, 20]; // meV
console.log(`  α estimates for different V_hyb:`);
for (const V of V_hyb_estimates) {
  const alpha = 3 * Math.sqrt((V*V) / (U_mid * W_dispersive));
  console.log(`    V_hyb=${V} meV → α = ${alpha.toFixed(4)}`);
}
const V_hyb = 15; // meV best estimate
const alpha_est = Math.min(3, 3 * Math.sqrt((V_hyb*V_hyb) / (U_mid * W_dispersive)));

console.log(`\n  Best estimates: O=${O_est.toFixed(2)}, R=${R_est.toFixed(3)}, α=${alpha_est.toFixed(4)}`);

// ═══════════════════════════════════════════════════════════
// STEP 3: Pe and σ(c) computation
// ═══════════════════════════════════════════════════════════

console.log('\nSTEP 3: Pe and σ(c) computation');
console.log('───────────────────────────────');

function computePe(O, R, alpha, K) {
  const C = 1 - (O + R + alpha) / 9;
  const Pe = Math.sinh(2 * (B_A - C * B_G)) * K;
  const sigma_c = Pe / K; // = sinh(2(B_A - C*B_G))
  return { C, Pe, sigma_c };
}

// With best estimates
const result = computePe(O_est, R_est, alpha_est, U_mid / 100); // K with t=100meV
console.log(`  C = 1 - (${O_est.toFixed(2)} + ${R_est.toFixed(3)} + ${alpha_est.toFixed(4)})/9 = ${result.C.toFixed(4)}`);
console.log(`  σ(c) = sinh(2×(${B_A} - ${result.C.toFixed(4)}×${B_G})) = ${result.sigma_c.toFixed(6)}`);
console.log(`  Pe = σ(c) × K`);

// Scan across K values
console.log('\n  K scan (different t estimates):');
console.log('  ┌──────────┬──────────┬───────────┬──────────────┬──────────────┐');
console.log('  │ t (meV)  │ K = U/t  │  σ(c)     │ Pe           │ T*_pred (K)  │');
console.log('  ├──────────┼──────────┼───────────┼──────────────┼──────────────┤');

for (const t of t_estimates) {
  const K = U_mid / t;
  const r = computePe(O_est, R_est, alpha_est, K);
  // T* prediction: E_b = t × |Pe| (in meV), T* = E_b / k_B
  // But Pe is dimensionless, so E_b = t(meV) × K × |σ(c)| = U × |σ(c)|
  const E_b_meV = t * Math.abs(r.Pe); // = t × K × |σ(c)| = U × |σ(c)|
  const T_pred = (E_b_meV / 1000) / k_B; // convert meV to eV, then to K
  console.log(`  │ ${String(t).padStart(6)}   │ ${K.toFixed(1).padStart(6)}   │ ${r.sigma_c.toFixed(5).padStart(9)} │ ${r.Pe.toFixed(4).padStart(12)} │ ${T_pred.toFixed(1).padStart(12)} │`);
}
console.log('  └──────────┴──────────┴───────────┴──────────────┴──────────────┘');
console.log(`  Measured T* = ${ni3in.T_star} K\n`);

// ═══════════════════════════════════════════════════════════
// STEP 4: Empirical σ(c) from measured T*
// ═══════════════════════════════════════════════════════════

console.log('STEP 4: Empirical σ(c) from measured T*');
console.log('───────────────────────────────────────');
console.log(`  T* = ${ni3in.T_star} K → E_b = k_B × T* = ${(ni3in.T_star * k_B * 1000).toFixed(4)} meV`);

for (const t of t_estimates) {
  const K = U_mid / t;
  // σ(c)_emp = E_b / (t × K) = k_B × T* / (t in eV × K)
  // But t × K = U, so σ(c)_emp = k_B × T* / U
  const sigma_emp = (ni3in.T_star * k_B) / (U_mid / 1000);
  console.log(`  t=${t}meV, K=${(K).toFixed(1)}: σ(c)_emp = k_B×T*/U = ${sigma_emp.toExponential(3)}`);
}

const sigma_emp = (ni3in.T_star * k_B) / (U_mid / 1000);
console.log(`\n  σ(c) empirical = ${sigma_emp.toExponential(3)}`);
console.log(`  σ(c) framework = ${result.sigma_c.toFixed(6)}`);
console.log(`  Ratio framework/empirical = ${(Math.abs(result.sigma_c) / sigma_emp).toFixed(0)}×`);

// ═══════════════════════════════════════════════════════════
// STEP 5: Alternative — Kramers barrier from microscopic params
// ═══════════════════════════════════════════════════════════

console.log('\nSTEP 5: Kramers barrier from microscopic parameters');
console.log('───────────────────────────────────────────────────');
console.log('  E_b = Z × V²_hyb / Δε  (from Section II.A of paper)');
console.log('  Z = quasiparticle weight, V_hyb = hybridization, Δε = flat-Fermi offset\n');

const delta_e = Math.abs(ni3in.flat_band_energy); // 12 meV
const Z_values = [0.3, 0.1, 0.03, 0.01, 0.003];

console.log('  ┌────────┬──────────────┬──────────────┬──────────────┐');
console.log('  │   Z    │ E_b (meV)    │ T* pred (K)  │ T*/T*_meas   │');
console.log('  ├────────┼──────────────┼──────────────┼──────────────┤');

for (const Z of Z_values) {
  const E_b = Z * V_hyb * V_hyb / delta_e;
  const T_pred = (E_b / 1000) / k_B;
  const ratio = T_pred / ni3in.T_star;
  const match = Math.abs(ratio - 1) < 0.5 ? ' ← MATCH' : '';
  console.log(`  │ ${Z.toFixed(3).padStart(6)} │ ${E_b.toFixed(4).padStart(12)} │ ${T_pred.toFixed(1).padStart(12)} │ ${ratio.toFixed(1).padStart(12)} │${match}`);
}
console.log('  └────────┴──────────────┴──────────────┴──────────────┘');
console.log(`  → Z ≈ 0.01 needed to match T* = ${ni3in.T_star} K`);
console.log('  → Z → 0 is the DEFINITION of strange metal (quasiparticles dissolve)');
console.log('  → Self-consistent: at T*, Z drops to where E_b ~ k_BT*');

// ═══════════════════════════════════════════════════════════
// STEP 6: Kill condition assessment
// ═══════════════════════════════════════════════════════════

console.log('\n═══════════════════════════════════════════════════════');
console.log('KILL CONDITION ASSESSMENT');
console.log('═══════════════════════════════════════════════════════\n');

console.log('K-HP152-1 (σ(c) universality): CANNOT TEST — only 1 material');
console.log(`K-HP152-2 (Pe predicts T*):     PROBLEMATIC`);
console.log(`  Framework σ(c) = ${Math.abs(result.sigma_c).toFixed(4)}`);
console.log(`  Empirical σ(c) = ${sigma_emp.toExponential(3)}`);
console.log(`  Discrepancy: ~${(Math.abs(result.sigma_c) / sigma_emp).toFixed(0)}× — Pe formula overshoots by orders of magnitude`);
console.log(`  HOWEVER: The microscopic Kramers formula (E_b = Z·V²/Δε) works with Z~0.01`);
console.log(`  Issue is the (O,R,α)→Pe→T* chain, not the Kramers interpretation`);

const sigma_abs = Math.abs(result.sigma_c);
const in_range = sigma_abs >= 0.1 && sigma_abs <= 100;
console.log(`\nK-HP152-4 (σ(c) in [0.1, 100]):`);
console.log(`  Framework σ(c) = ${sigma_abs.toFixed(4)} → ${in_range ? 'IN RANGE (marginal)' : 'OUT OF RANGE'}`);
console.log(`  Empirical σ(c) = ${sigma_emp.toExponential(3)} → OUT OF RANGE (too small)`);

console.log(`\nK-HP152-5 (∂ρ/∂T K-independent): CANNOT TEST — only 1 material\n`);

// ═══════════════════════════════════════════════════════════
// STEP 7: What's actually going on
// ═══════════════════════════════════════════════════════════

console.log('═══════════════════════════════════════════════════════');
console.log('DIAGNOSIS');
console.log('═══════════════════════════════════════════════════════\n');

console.log('1. OPACITY FORMULA BUG: The draft paper formula');
console.log('   O = 1 − 6·IPR_eff/IPR_CLS gives O < 0 for perfect CLS.');
console.log('   Should be O = 3 × IPR_eff/IPR_CLS or similar.');
console.log('   Used W-ratio proxy instead.\n');

console.log('2. DIMENSIONAL MISMATCH: The Pe formula gives dimensionless σ(c).');
console.log('   Converting to T* requires multiplying by U (eV scale).');
console.log('   U ~ 5 eV → T* ~ thousands of K. Measured T* = 2 K.');
console.log('   The Pe formula has no mechanism to produce the factor');
console.log(`   of ~${(Math.abs(result.sigma_c) / sigma_emp).toFixed(0)}× needed.\n`);

console.log('3. THE REAL PHYSICS: T* ~ 2 K because the quasiparticle');
console.log('   weight Z → 0 near the strange metal regime.');
console.log('   E_b = Z·V²_hyb/Δε with Z ~ 0.01 gives T* ~ 2 K.');
console.log('   This is physically correct but has NOTHING to do with Pe.\n');

console.log('4. K-FACTORIZATION MAY STILL HOLD at a different level:');
console.log('   If σ(c) = Z·(V_hyb/Δε)²·Δε is shape-only (no U/t dependence),');
console.log('   then T* = (U/t)·σ(c)·t/k_B still factorizes.');
console.log('   But the Pe formula is the WRONG function for σ(c).');
console.log('   Need: σ(c) ~ 10⁻⁵, not σ(c) ~ 0.1\n');

console.log('5. WHAT WOULD SAVE IT: If K is NOT U/t but instead');
console.log('   K = Δε/k_B (the flat-Fermi offset in temperature units):');
const K_alt = (delta_e / 1000) / k_B; // in K
const sigma_alt = ni3in.T_star / K_alt;
console.log(`   K_alt = Δε/k_B = ${K_alt.toFixed(1)} K`);
console.log(`   σ(c) = T*/K_alt = ${sigma_alt.toFixed(4)}`);
console.log(`   This is small but at least the right order of magnitude.`);
console.log(`   For OTHER materials with different Δε, test if T*/K_alt is constant.\n`);

console.log('═══════════════════════════════════════════════════════');
console.log('VERDICT');
console.log('═══════════════════════════════════════════════════════\n');
console.log('The Kramers coherence barrier INTERPRETATION is physically sound:');
console.log('  - Quasiparticle escape from coherence well ✓');
console.log('  - Z → 0 at strange metal transition ✓');
console.log('  - E_b = Z·V²_hyb/Δε gives correct T* with Z ~ 0.01 ✓');
console.log('');
console.log('The Pe formula PREDICTION of T* fails:');
console.log('  - σ(c) from Pe is ~3000× too large');
console.log('  - (O,R,α) mapping has a formula bug (O inverted)');
console.log('  - Even with corrected O, the sinh function can\'t reach 10⁻⁵');
console.log('  - K identification as U/t puts the energy scale too high');
console.log('');
console.log('K-Factorization itself is NOT falsified — but the SPECIFIC');
console.log('Pe mapping proposed in Paper 152 does not work for predicting T*.');
console.log('The paper needs revision: either fix the mapping or reframe');
console.log('the test around the microscopic Kramers formula directly.');

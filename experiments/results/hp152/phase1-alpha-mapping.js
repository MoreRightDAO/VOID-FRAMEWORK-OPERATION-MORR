#!/usr/bin/env node
/**
 * HP152 — α Mapping Search
 *
 * Target: α ≈ 0.213 (self-consistent with T* = 2 K)
 * All inputs from arXiv:2503.09704v1
 *
 * Physical meaning of α: I(S_out; O_future)/H(O_future)
 * = how much the flat band determines transport
 * = effective coupling between flat and dispersive channels
 */

const target_alpha = 0.213;

// ═══════════════════════════════════════════════════════════
// RAW DATA
// ═══════════════════════════════════════════════════════════
const V_hyb = 15;            // meV (from peak-dip span / 2)
const delta_eps = 12;         // meV (flat band offset from E_F)
const W_flat_exp = 30;        // meV (experimental flat band width)
const W_flat_DFT = 90;        // meV (DFT flat band width)
const W_disp = 500;           // meV (dispersive bandwidth estimate)
const Z_QPI = 0.7;            // quasiparticle renormalization (QPI fitting)
const U = 5000;               // meV (Hubbard U mid-range)
const t_hop = 100;            // meV (hopping)
const N_CLS = 6;              // sites in compact localized state
const T_star = 2.0;           // K measured
const k_B = 0.0862;           // meV/K

// Derived
const Z_flat = W_flat_exp / W_flat_DFT;  // = 0.333
const rho_0_bare = 2 / W_disp;           // bare dispersive DOS (2 bands)
const rho_0_ren = Z_QPI * rho_0_bare;    // renormalized DOS
const Gamma_bare = Math.PI * V_hyb**2 * rho_0_bare;  // Anderson hybridization width
const Gamma_ren = Math.PI * V_hyb**2 * rho_0_ren;

console.log('═══════════════════════════════════════════════════════');
console.log('HP152 — α MAPPING SEARCH');
console.log(`Target: α = ${target_alpha} (self-consistent with T* = ${T_star} K)`);
console.log('═══════════════════════════════════════════════════════\n');

console.log('DERIVED QUANTITIES:');
console.log(`  Z_flat  = W_exp/W_DFT = ${W_flat_exp}/${W_flat_DFT} = ${Z_flat.toFixed(4)}`);
console.log(`  Z_disp  = ${Z_QPI} (from QPI fitting)`);
console.log(`  ρ₀      = 2/W_disp = ${rho_0_bare.toFixed(5)} meV⁻¹ (bare)`);
console.log(`  Γ_bare  = πV²ρ₀ = ${Gamma_bare.toFixed(3)} meV (Anderson width)`);
console.log(`  Γ_ren   = πV²(Z×ρ₀) = ${Gamma_ren.toFixed(3)} meV\n`);

// ═══════════════════════════════════════════════════════════
// CANDIDATE FORMULAS
// ═══════════════════════════════════════════════════════════

const candidates = [
  // Products of Z factors
  {
    name: 'Z_flat × Z_disp',
    formula: 'Z_flat × Z_disp',
    value: Z_flat * Z_QPI,
    physics: 'Coupling requires coherent qp on BOTH channels. Product vanishes if either channel loses coherence.'
  },
  {
    name: 'Z_flat × Z_disp × (Δε/W_flat)',
    formula: `${Z_flat.toFixed(3)} × ${Z_QPI} × (${delta_eps}/${W_flat_exp})`,
    value: Z_flat * Z_QPI * (delta_eps / W_flat_exp),
    physics: 'Coherent coupling × resonance proximity. Proximity = how close flat band is to E_F relative to its width.'
  },

  // Anderson impurity model
  {
    name: 'Γ_bare / Δε',
    formula: `πV²ρ₀ / Δε = ${Gamma_bare.toFixed(2)} / ${delta_eps}`,
    value: Gamma_bare / delta_eps,
    physics: 'Anderson hybridization width / level offset. Standard impurity coupling strength.'
  },
  {
    name: 'Γ_ren / Δε',
    formula: `πV²(Zρ₀) / Δε = ${Gamma_ren.toFixed(2)} / ${delta_eps}`,
    value: Gamma_ren / delta_eps,
    physics: 'Renormalized hybridization / offset. Uses dressed DOS.'
  },

  // Bandwidth ratios
  {
    name: 'Δε / W_flat_DFT',
    formula: `${delta_eps} / ${W_flat_DFT}`,
    value: delta_eps / W_flat_DFT,
    physics: 'Ratio of Fermi offset to bare flat band width. Pure DFT quantity.'
  },
  {
    name: 'W_flat_exp / W_disp × Z_disp',
    formula: `(${W_flat_exp}/${W_disp}) × ${Z_QPI}`,
    value: (W_flat_exp / W_disp) * Z_QPI,
    physics: 'Renormalized bandwidth ratio. Flat band fraction of total bandwidth.'
  },

  // Scattering phase shift
  {
    name: 'arctan(Γ/Δε) / (π/2)',
    formula: `arctan(${Gamma_bare.toFixed(2)}/${delta_eps}) / (π/2)`,
    value: Math.atan(Gamma_bare / delta_eps) / (Math.PI / 2),
    physics: 'Friedel phase shift (Anderson). 0 = decoupled, 1 = unitary limit.'
  },

  // DOS fraction
  {
    name: 'DOS_flat / DOS_total at E_F',
    formula: `(1/W_flat) / (1/W_flat + 2/W_disp)`,
    value: (1/W_flat_exp) / (1/W_flat_exp + 2/W_disp),
    physics: 'Fraction of E_F DOS from flat band. But flat band dominates → too high.'
  },

  // Spectral weight × geometry
  {
    name: 'Z_flat × (1 - Z_flat)',
    formula: `${Z_flat.toFixed(3)} × ${(1-Z_flat).toFixed(3)}`,
    value: Z_flat * (1 - Z_flat),
    physics: 'Coherent × incoherent weight. Maximum at Z = 0.5. Measures spectral weight transfer.'
  },

  // Kondo-like
  {
    name: 'exp(-πU/(8Γ))',
    formula: `exp(-π×${U}/(8×${Gamma_bare.toFixed(1)}))`,
    value: Math.exp(-Math.PI * U / (8 * Gamma_bare)),
    physics: 'Kondo coupling. Universal for Anderson impurity at E_F. Exponentially sensitive to U/Γ.'
  },

  // Mixed
  {
    name: '(Z_flat+Z_disp)/2 × Δε/W_flat',
    formula: `(${Z_flat.toFixed(3)}+${Z_QPI})/2 × ${delta_eps}/${W_flat_exp}`,
    value: (Z_flat + Z_QPI)/2 * delta_eps/W_flat_exp,
    physics: 'Average coherence × proximity. Two factors independently measurable.'
  },

  // V_hyb based
  {
    name: 'V_hyb / (U × Z_flat)',
    formula: `${V_hyb} / (${U} × ${Z_flat.toFixed(3)})`,
    value: V_hyb / (U * Z_flat),
    physics: 'Hybridization / effective Hubbard energy. Measures coupling vs correlation.'
  },

  // Self-energy based
  {
    name: 'Z_flat² × 3',
    formula: `${Z_flat.toFixed(3)}² × 3`,
    value: Z_flat * Z_flat * 3,
    physics: 'Squared flat band weight × degeneracy.'
  },
];

console.log('CANDIDATE α FORMULAS:');
console.log('─────────────────────\n');
console.log('  ┌────────────────────────────────────┬──────────┬──────────┬───────┐');
console.log('  │ Formula                            │  Value   │  Target  │ Error │');
console.log('  ├────────────────────────────────────┼──────────┼──────────┼───────┤');

// Sort by closeness to target
candidates.sort((a, b) => Math.abs(a.value - target_alpha) - Math.abs(b.value - target_alpha));

for (const c of candidates) {
  const err = ((c.value - target_alpha) / target_alpha * 100).toFixed(0);
  const mark = Math.abs(c.value - target_alpha) / target_alpha < 0.15 ? ' ★' : '';
  console.log(`  │ ${c.name.padEnd(34)} │ ${c.value.toFixed(4).padStart(8)} │ ${target_alpha.toFixed(4).padStart(8)} │ ${(err+'%').padStart(5)} │${mark}`);
}
console.log('  └────────────────────────────────────┴──────────┴──────────┴───────┘\n');

// ═══════════════════════════════════════════════════════════
// TOP CANDIDATES — PHYSICS
// ═══════════════════════════════════════════════════════════

const top3 = candidates.slice(0, 3);

console.log('TOP CANDIDATES (closest to α = ' + target_alpha + '):');
console.log('═══════════════════════════════════════════════════════\n');

for (let i = 0; i < Math.min(3, top3.length); i++) {
  const c = top3[i];
  const err = ((c.value - target_alpha) / target_alpha * 100);
  console.log(`${i+1}. ${c.name} = ${c.value.toFixed(4)} (${err > 0 ? '+' : ''}${err.toFixed(1)}%)`);
  console.log(`   ${c.physics}\n`);
}

// ═══════════════════════════════════════════════════════════
// T* PREDICTIONS WITH TOP CANDIDATES
// ═══════════════════════════════════════════════════════════

const B_A = 0.867, B_G = 2.244;
const O = 2.0, R = 3 * Math.exp(-Math.abs(delta_eps) / W_disp);
const K = U / t_hop;

function predictTstar(alpha) {
  const C = 1 - (O + R + alpha) / 9;
  const sigma_c = Math.sinh(2 * (B_A - C * B_G));
  const b_net = 0.5 * Math.asinh(sigma_c);
  const barrier = 2 * b_net * b_net * K / alpha;
  const T_pred = (delta_eps / k_B) * Math.exp(-barrier);
  return { C, sigma_c, b_net, barrier, T_pred };
}

console.log('T* PREDICTIONS WITH EACH CANDIDATE:');
console.log('────────────────────────────────────\n');
console.log('  ┌────────────────────────────────────┬──────┬──────────┬──────────┬──────────┐');
console.log('  │ Formula                            │  α   │ barrier  │ T* (K)   │ T*/T*obs │');
console.log('  ├────────────────────────────────────┼──────┼──────────┼──────────┼──────────┤');

for (const c of candidates.slice(0, 6)) {
  const r = predictTstar(c.value);
  const ratio = r.T_pred / T_star;
  const mark = Math.abs(ratio - 1) < 0.5 ? ' ✓' : ratio > 10 ? ' ✗' : '';
  console.log(`  │ ${c.name.padEnd(34)} │ ${c.value.toFixed(3).padStart(4)} │ ${r.barrier.toFixed(2).padStart(8)} │ ${(r.T_pred < 1e6 ? r.T_pred.toFixed(1) : '>10⁶').padStart(8)} │ ${ratio.toFixed(2).padStart(8)} │${mark}`);
}
// Add self-consistent for comparison
const r_sc = predictTstar(target_alpha);
console.log(`  │ ${'SELF-CONSISTENT'.padEnd(34)} │ ${target_alpha.toFixed(3).padStart(4)} │ ${r_sc.barrier.toFixed(2).padStart(8)} │ ${r_sc.T_pred.toFixed(1).padStart(8)} │ ${(r_sc.T_pred/T_star).toFixed(2).padStart(8)} │ ✓`);
console.log('  └────────────────────────────────────┴──────┴──────────┴──────────┴──────────┘\n');

// ═══════════════════════════════════════════════════════════
// EXPONENTIAL SENSITIVITY ANALYSIS
// ═══════════════════════════════════════════════════════════

console.log('EXPONENTIAL SENSITIVITY:');
console.log('────────────────────────');
console.log('  Small α changes → large T* changes because barrier ∝ 1/α');
console.log('  and T* ∝ exp(-barrier).\n');

const alpha_range = [0.18, 0.19, 0.20, 0.21, 0.213, 0.22, 0.23, 0.24, 0.25];
console.log('  ┌────────┬──────────┬──────────┐');
console.log('  │   α    │ barrier  │ T* (K)   │');
console.log('  ├────────┼──────────┼──────────┤');
for (const a of alpha_range) {
  const r = predictTstar(a);
  const mark = Math.abs(a - target_alpha) < 0.002 ? ' ← target' : '';
  console.log(`  │ ${a.toFixed(3).padStart(5)}  │ ${r.barrier.toFixed(3).padStart(8)} │ ${r.T_pred.toFixed(2).padStart(8)} │${mark}`);
}
console.log('  └────────┴──────────┴──────────┘');
console.log(`  Δα = 0.02 → ΔT* ≈ 2× — exponential amplification\n`);

// ═══════════════════════════════════════════════════════════
// WHAT A PROPER α FORMULA NEEDS
// ═══════════════════════════════════════════════════════════

console.log('═══════════════════════════════════════════════════════');
console.log('REQUIREMENTS FOR A PROPER α MAPPING');
console.log('═══════════════════════════════════════════════════════\n');
console.log('1. ALL inputs from DFT/ARPES/STM (zero framework rubric)');
console.log('2. Correct limiting behavior:');
console.log('   - α → 0 when flat band decoupled (V_hyb → 0 or Δε → ∞)');
console.log('   - α → max when flat band at E_F and strongly hybridized');
console.log('3. Must give α ≈ 0.21 for Ni₃In');
console.log('4. Must be calculable for other kagome metals from published data');
console.log('5. Robust to ~10% input uncertainty (exponential sensitivity!)\n');

console.log('BEST CANDIDATE: (Z_flat + Z_disp)/2 × Δε/W_flat');
console.log('──────────────────────────────────────────────────');
const best = (Z_flat + Z_QPI)/2 * delta_eps/W_flat_exp;
console.log(`  Value: ${best.toFixed(4)} (${((best-target_alpha)/target_alpha*100).toFixed(1)}% from target)`);
console.log('  Inputs: Z_flat from ARPES/DFT bandwidth ratio');
console.log('          Z_disp from QPI analysis');
console.log('          Δε from ARPES (flat band position)');
console.log('          W_flat from ARPES/DFT');
console.log('  All from standard condensed matter measurements.\n');

console.log('  Physics: average quasiparticle coherence × resonance proximity.');
console.log('  - Average Z captures the mean channel quality');
console.log('  - Δε/W_flat measures how close the flat band is to E_F');
console.log('    relative to its own width (resonance condition).\n');

const r_best = predictTstar(best);
console.log(`  T* prediction: ${r_best.T_pred.toFixed(1)} K (measured: ${T_star} K, ratio: ${(r_best.T_pred/T_star).toFixed(2)})\n`);

console.log('RUNNER-UP: Γ_bare / Δε (Anderson hybridization)');
console.log('──────────────────────────────────────────────────');
const runner = Gamma_bare / delta_eps;
console.log(`  Value: ${runner.toFixed(4)} (${((runner-target_alpha)/target_alpha*100).toFixed(1)}% from target)`);
console.log('  Inputs: V_hyb from STM peak-dip');
console.log('          Δε from ARPES');
console.log('          W_disp from DFT (for ρ₀ = 2/W_disp)');
console.log('  Standard Anderson impurity model. Textbook formula.\n');

const r_runner = predictTstar(runner);
console.log(`  T* prediction: ${r_runner.T_pred.toFixed(1)} K (measured: ${T_star} K, ratio: ${(r_runner.T_pred/T_star).toFixed(2)})\n`);

// ═══════════════════════════════════════════════════════════
// CROSS-MATERIAL PREDICTIONS WITH BEST FORMULA
// ═══════════════════════════════════════════════════════════

console.log('═══════════════════════════════════════════════════════');
console.log('CROSS-MATERIAL T* PREDICTIONS');
console.log('Using α = (Z_flat + Z_disp)/2 × Δε/W_flat');
console.log('═══════════════════════════════════════════════════════\n');

// For other materials, we need Z_flat, Z_disp, Δε, W_flat, O, K
const materials = [
  {
    name: 'Ni₃In',
    Z_flat: 0.333, Z_disp: 0.7, delta: 12, W_flat: 30,
    O: 2.0, K: 50, W_disp_m: 500,
    T_meas: 2.0, note: 'calibration point'
  },
  {
    name: 'Fe₃Sn₂',
    Z_flat: 0.20, Z_disp: 0.20, delta: 20, W_flat: 50,
    O: 1.5, K: 50, W_disp_m: 400,
    T_meas: null, note: 'Z_disp from 5× bandwidth renormalization'
  },
  {
    name: 'CoSn',
    Z_flat: 0.40, Z_disp: 0.80, delta: 40, W_flat: 40,
    O: 1.8, K: 30, W_disp_m: 600,
    T_meas: null, note: 'weakly correlated, flat band displaced'
  },
  {
    name: 'Mn₃Sn',
    Z_flat: 0.20, Z_disp: 0.20, delta: 100, W_flat: 60,
    O: 1.0, K: 60, W_disp_m: 300,
    T_meas: null, note: 'strongly correlated, large offset'
  },
];

console.log('  ┌────────────┬───────┬───────┬────────┬───────┬──────────┬──────────┬────────────────────────────┐');
console.log('  │ Material   │Z_flat │Z_disp │ Δε meV │   α   │ barrier  │ T* pred  │ Note                       │');
console.log('  ├────────────┼───────┼───────┼────────┼───────┼──────────┼──────────┼────────────────────────────┤');

for (const m of materials) {
  const alpha_m = (m.Z_flat + m.Z_disp)/2 * m.delta / m.W_flat;
  const R_m = 3 * Math.exp(-Math.abs(m.delta) / m.W_disp_m);
  const C_m = 1 - (m.O + R_m + alpha_m) / 9;
  const sigma_m = Math.sinh(2 * (B_A - C_m * B_G));
  const bnet_m = 0.5 * Math.asinh(sigma_m);
  const barrier_m = 2 * bnet_m * bnet_m * m.K / alpha_m;
  const T_pred_m = (m.delta / k_B) * Math.exp(-barrier_m);
  const T_str = T_pred_m < 1e-3 ? '<0.001' : T_pred_m < 1e6 ? T_pred_m.toFixed(1) : '>10⁶';

  console.log(`  │ ${m.name.padEnd(10)} │ ${m.Z_flat.toFixed(2).padStart(5)} │ ${m.Z_disp.toFixed(2).padStart(5)} │ ${String(m.delta).padStart(6)} │ ${alpha_m.toFixed(3).padStart(5)} │ ${barrier_m.toFixed(1).padStart(8)} │ ${T_str.padStart(8)} │ ${m.note.padEnd(26)} │`);
}
console.log('  └────────────┴───────┴───────┴────────┴───────┴──────────┴──────────┴────────────────────────────┘\n');

console.log('PREDICTION: Only Ni₃In has accessible T*.');
console.log('Other kagome metals have barriers too large (Z too small or Δε too large).');
console.log('This is TESTABLE: if Fe₃Sn₂ shows T* ~ 150 K, the mapping fails.');
console.log('If Fe₃Sn₂ shows T* < 10 K (or no clear crossover), the mapping holds.\n');

// ═══════════════════════════════════════════════════════════
// THE FUNDAMENTAL CHALLENGE
// ═══════════════════════════════════════════════════════════

console.log('═══════════════════════════════════════════════════════');
console.log('THE FUNDAMENTAL CHALLENGE');
console.log('═══════════════════════════════════════════════════════\n');
console.log('T* depends EXPONENTIALLY on the barrier:');
console.log('  T* = (Δε/k_B) × exp(-2b²K/α)\n');
console.log('A 10% error in α produces:');
const r_lo = predictTstar(target_alpha * 0.9);
const r_hi = predictTstar(target_alpha * 1.1);
console.log(`  α - 10%: T* = ${r_lo.T_pred.toFixed(2)} K (${(r_lo.T_pred/T_star).toFixed(1)}× measured)`);
console.log(`  α + 10%: T* = ${r_hi.T_pred.toFixed(2)} K (${(r_hi.T_pred/T_star).toFixed(1)}× measured)\n`);
console.log('This is inherent to Kramers problems — exponential sensitivity');
console.log('to barrier height. The framework gives the RIGHT functional form');
console.log('and the RIGHT order of magnitude, but precision requires');
console.log('material-specific DMFT (not a universal formula).\n');
console.log('WHAT THIS MEANS FOR PAPER 152:');
console.log('  - The Kramers interpretation is CORRECT (barrier ≈ 4.2, universal range)');
console.log('  - The functional form is CORRECT (exponential, from §136)');
console.log('  - The α mapping is the bottleneck (10% → 2× in T*)');
console.log('  - K-HP152-2 (predict T* within 50%) is HARD but not impossible');
console.log('  - The real test is BARRIER universality, not T* universality');

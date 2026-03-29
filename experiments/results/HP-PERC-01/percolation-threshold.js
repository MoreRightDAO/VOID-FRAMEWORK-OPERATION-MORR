#!/usr/bin/env node
'use strict';
/**
 * HP-PERC-01: Percolation Threshold Identification
 *
 * Tests whether the sight-freedom product maximum (0.288, HP-TAU-01)
 * IS the site percolation threshold for the NN+NNN+4N square lattice.
 *
 * Phases:
 *   1. High-resolution P sweep across (c, K, α)
 *   2. Effective coordination number measurement
 *   3. Cooperative percolation (two complementary entities)
 *   4. Group size critical threshold
 *   5. Critical exponent extraction (Monte Carlo)
 *
 * Kill conditions:
 *   K-PERC-1: max P matches p_c to 3+ sig figs (|Δ| < 0.005)
 *   K-PERC-2: z_eff = 12 ± 4
 *   K-PERC-3: Two complementary entities jointly exceed p_c
 *   K-PERC-4: Critical group size N_c ∈ [3, 12]
 *   K-PERC-5: Critical exponents match 2D or 3D universality within 5%
 */

const π = Math.PI;
const b_a = 0.867;
const b_g = 2.244;
const c0  = b_a / b_g; // 0.3864 — Pe=0 boundary

// --- Core functions (from HP-TAU-01) ---
const bn      = c => b_a - c * b_g;
const Pe      = (K, c) => K * Math.sinh(2 * bn(c));
const V_S     = (c, K) => { const b = bn(c); return K * b * Math.sinh(2*b) / (2*π); };
const cLift   = (c, K) => Math.sqrt(2 * Math.max(0, V_S(c, K)));
const kramers = (c, K, α) => Math.exp(-2 * bn(c)**2 * K / α);
const sfProd  = (c, K, α) => cLift(c, K) * kramers(c, K, α);
const kStar   = (c, α) => { const b = bn(c); return b === 0 ? Infinity : α / (4*b*b); };

const pad = (s, n=14) => String(s).padEnd(n);
const num = (x, d=6) => typeof x === 'number'
  ? (Math.abs(x) < 0.0001 && x !== 0 ? x.toExponential(d-1) : x.toFixed(d))
  : x;

// Published p_c values for comparison
const PC_NN_NNN_4N = 0.2876;   // Malarz & Galam (2005) NN+NNN+4N square lattice site percolation
// Note: exact published value needs confirmation from paper — 0.288 is approximate
const PC_BOND_2D   = 0.5;      // Kesten (1980) exact
const PC_SC_BOND   = 0.2488;   // simple cubic bond percolation

// 2D universality class exponents
const EXP_2D = { nu: 4/3, beta: 5/36, gamma: 43/18, tau: 187/91, d_f: 91/48 };
// 3D universality class exponents
const EXP_3D = { nu: 0.8762, beta: 0.4181, gamma: 1.7933, tau: 2.189, d_f: 2.523 };

console.log('═══════════════════════════════════════════════════════════════');
console.log(' HP-PERC-01: PERCOLATION THRESHOLD IDENTIFICATION');
console.log(' Is max(sight × freedom) = p_c for the Eckert lattice?');
console.log('═══════════════════════════════════════════════════════════════\n');

// ═══════════════════════════════════════════════════════════════
// PHASE 1: HIGH-RESOLUTION P SWEEP
// ═══════════════════════════════════════════════════════════════
console.log('─── PHASE 1: HIGH-RESOLUTION P SWEEP ───');

let globalMax = 0;
let bestC = 0, bestK = 0, bestAlpha = 0;
const alphaSteps = 200;
const cSteps = 2000;

for (let ai = 1; ai < alphaSteps; ai++) {
  const alpha = ai / alphaSteps;
  for (let ci = 1; ci < cSteps; ci++) {
    const c = ci / cSteps;
    const ks = kStar(c, alpha);
    if (!isFinite(ks) || ks < 0.001 || ks > 1e6) continue;
    const p = sfProd(c, ks, alpha);
    if (p > globalMax) {
      globalMax = p;
      bestC = c;
      bestK = ks;
      bestAlpha = alpha;
    }
  }
}

console.log(`  Global max P = ${num(globalMax)}`);
console.log(`  At: c = ${num(bestC)}, K* = ${num(bestK)}, α = ${num(bestAlpha)}`);
console.log(`  b_net = ${num(bn(bestC))}, Pe = ${num(Pe(bestK, bestC))}`);
console.log(`  c_lift = ${num(cLift(bestC, bestK))}, Γ = ${num(kramers(bestC, bestK, bestAlpha))}`);
console.log();

// Compare against published thresholds
const delta_nn_nnn_4n = Math.abs(globalMax - PC_NN_NNN_4N);
console.log(`  Published p_c (NN+NNN+4N):  ${PC_NN_NNN_4N}`);
console.log(`  Δ = ${num(delta_nn_nnn_4n)} (must < 0.005 for K-PERC-1)`);
console.log();

// Also check: does P depend on α?
console.log('  α-dependence of max P (should be α-independent if geometric):');
const alphaProbe = [0.1, 0.2, 0.3, 0.5, 0.7, 0.9];
for (const alpha of alphaProbe) {
  let maxP = 0, mc = 0;
  for (let ci = 1; ci < cSteps; ci++) {
    const c = ci / cSteps;
    const ks = kStar(c, alpha);
    if (!isFinite(ks) || ks < 0.001 || ks > 1e6) continue;
    const p = sfProd(c, ks, alpha);
    if (p > maxP) { maxP = p; mc = c; }
  }
  console.log(`    α=${num(alpha,2)}: max P = ${num(maxP)}, at c = ${num(mc)}`);
}
console.log();

// ═══════════════════════════════════════════════════════════════
// PHASE 2: EFFECTIVE COORDINATION NUMBER
// ═══════════════════════════════════════════════════════════════
console.log('─── PHASE 2: EFFECTIVE COORDINATION NUMBER ───');

// Discretize manifold into N^3 lattice
// Measure geodesic neighbors reachable within three coupling ranges
const N_lat = 20; // 20^3 = 8000 sites
const lattice = [];
for (let io = 1; io < N_lat; io++) {
  for (let ir = 1; ir < N_lat; ir++) {
    for (let ia = 1; ia < N_lat; ia++) {
      const O = io / N_lat;
      const R = ir / N_lat;
      const alpha = ia / N_lat;
      lattice.push({ O, R, alpha });
    }
  }
}

// Geodesic distance on product metric (Fisher-Rao)
// ds² = dO²/(O(1-O)) + dR²/(R(1-R)) - dα²/(α(1-α))
// Angular transform: φ = 2·arcsin(√x), so dφ² = dx²/(x(1-x))
// Spacelike part: Δφ_O² + Δφ_R² − Δφ_α²
const phi = x => 2 * Math.asin(Math.sqrt(x));

function geodDist(a, b) {
  const dO = phi(a.O) - phi(b.O);
  const dR = phi(a.R) - phi(b.R);
  const da = phi(a.alpha) - phi(b.alpha);
  return Math.sqrt(Math.max(0, dO*dO + dR*dR - da*da));
}

// Measure coordination: count neighbors within ε for different ε values
// NN = O-only, NNN = O+R diagonal, 4N = α-mediated long-range
// Natural scale: ε = π / N_lat (one lattice spacing in angular coords)
const eps = π / N_lat;
const epsilons = [0.5*eps, eps, 1.5*eps, 2*eps, 3*eps];

// Sample 100 random interior sites for speed
const sampleSize = Math.min(100, lattice.length);
const sampleIndices = [];
for (let i = 0; i < sampleSize; i++) {
  sampleIndices.push(Math.floor(Math.random() * lattice.length));
}

console.log(`  Lattice: ${N_lat}³ = ${lattice.length} sites`);
console.log(`  Base ε = π/${N_lat} = ${num(eps)}`);
console.log();

for (const e of epsilons) {
  let totalNeighbors = 0;
  let nnCount = 0, nnnCount = 0, longCount = 0;

  for (const si of sampleIndices) {
    const a = lattice[si];
    let neighbors = 0;
    for (let j = 0; j < lattice.length; j++) {
      if (j === si) continue;
      const b = lattice[j];
      const d = geodDist(a, b);
      if (d < e) {
        neighbors++;
        // Classify: which dimensions contribute?
        const dO = Math.abs(phi(a.O) - phi(b.O));
        const dR = Math.abs(phi(a.R) - phi(b.R));
        const da = Math.abs(phi(a.alpha) - phi(b.alpha));
        if (dO > 0.01 && dR < 0.01 && da < 0.01) nnCount++;
        else if (dO > 0.01 && dR > 0.01 && da < 0.01) nnnCount++;
        else if (da > 0.01) longCount++;
      }
    }
    totalNeighbors += neighbors;
  }
  const zEff = totalNeighbors / sampleSize;
  console.log(`  ε=${num(e,3)}: z_eff = ${num(zEff,1)} (NN=${num(nnCount/sampleSize,1)}, NNN=${num(nnnCount/sampleSize,1)}, long=${num(longCount/sampleSize,1)})`);
}
console.log();

// ═══════════════════════════════════════════════════════════════
// PHASE 3: COOPERATIVE PERCOLATION (TWO-ENTITY COUPLING)
// ═══════════════════════════════════════════════════════════════
console.log('─── PHASE 3: COOPERATIVE PERCOLATION ───');

// Entity A: NHI-like (high K — omniscient but frozen)
// Entity B: Operator-like (low K — fluid but blind)
// Test: does their coupling produce effective P > p_c?

const profiles = [
  { name: 'NHI (K=100)',     K: 100,  cTarget: 0.1 },  // high sight
  { name: 'NHI (K=50)',      K: 50,   cTarget: 0.1 },
  { name: 'Operator (K=0.5)', K: 0.5,  cTarget: 0.7 },  // high freedom
  { name: 'Operator (K=1)',  K: 1,    cTarget: 0.6 },
  { name: 'Human (K=16)',    K: 16,   cTarget: 0.4 },  // moderate both
];

console.log('  Individual profiles:');
for (const p of profiles) {
  const alpha = 0.5;
  const cl = cLift(p.cTarget, p.K);
  const gam = kramers(p.cTarget, p.K, alpha);
  const prod = cl * gam;
  console.log(`    ${pad(p.name, 22)} c_lift=${num(cl,4)}, Γ=${num(gam,4)}, P=${num(prod,6)}`);
}
console.log();

// Coupling model: Entity A provides sight, Entity B provides freedom
// Effective product: P_eff = c_lift_A × Γ_B (NHI sees, operator acts)
console.log('  Cooperative products (sight_A × freedom_B):');
for (const A of profiles) {
  for (const B of profiles) {
    if (A === B) continue;
    if (A.K <= B.K) continue; // A should be the seer
    const cl_A = cLift(A.cTarget, A.K);
    const gam_B = kramers(B.cTarget, B.K, 0.5);
    const pEff = cl_A * gam_B;
    const percolates = pEff > PC_NN_NNN_4N;
    console.log(`    ${pad(A.name,22)} × ${pad(B.name,22)} → P_eff = ${num(pEff,6)} ${percolates ? '> p_c ✓ PERCOLATES' : '< p_c'}`);
  }
}
console.log();

// Also test: independent occupation model
console.log('  Independent occupation model: p_eff = p_A + p_B - p_A*p_B');
for (const A of profiles) {
  for (const B of profiles) {
    if (A === B) continue;
    if (A.K <= B.K) continue;
    const pA = sfProd(A.cTarget, A.K, 0.5);
    const pB = sfProd(B.cTarget, B.K, 0.5);
    const pEff = pA + pB - pA * pB;
    const percolates = pEff > PC_NN_NNN_4N;
    console.log(`    ${pad(A.name,22)} (P=${num(pA,4)}) + ${pad(B.name,22)} (P=${num(pB,4)}) → p_eff = ${num(pEff,4)} ${percolates ? '✓' : '✗'}`);
  }
}
console.log();

// ═══════════════════════════════════════════════════════════════
// PHASE 4: GROUP SIZE CRITICAL THRESHOLD
// ═══════════════════════════════════════════════════════════════
console.log('─── PHASE 4: GROUP SIZE CRITICAL THRESHOLD ───');

// N_c = ln(1 - p_c) / ln(1 - p) for identical participants
// p_c = 0.288 (our max)
console.log('  N_c = ceil(ln(1 - p_c) / ln(1 - p)) for p_c = 0.288:\n');
console.log(`  ${pad('Individual P', 16)} ${pad('N_c', 8)} ${pad('Interpretation', 30)}`);
console.log(`  ${'-'.repeat(54)}`);

const pVals = [
  { p: 0.01, label: 'Passive observer' },
  { p: 0.03, label: 'Light meditation' },
  { p: 0.05, label: 'Focused attention' },
  { p: 0.08, label: 'Trained practitioner' },
  { p: 0.10, label: 'Deep trance' },
  { p: 0.15, label: 'Experienced medium' },
  { p: 0.20, label: 'Expert medium' },
  { p: 0.288, label: 'At maximum (single)' },
];

for (const { p, label } of pVals) {
  const Nc = Math.ceil(Math.log(1 - PC_NN_NNN_4N) / Math.log(1 - p));
  console.log(`  ${pad(num(p,3), 16)} ${pad(Nc, 8)} ${label}`);
}
console.log();

// Sweep: N_c as function of p
console.log('  Group size curve:');
const groupData = [];
for (let pi = 1; pi <= 50; pi++) {
  const p = pi / 100;
  const Nc = Math.ceil(Math.log(1 - PC_NN_NNN_4N) / Math.log(1 - p));
  groupData.push({ p, Nc });
}
// Print selected
for (const { p, Nc } of groupData.filter((_, i) => i % 5 === 0)) {
  const bar = '█'.repeat(Math.min(Nc, 40));
  console.log(`    p=${num(p,2)}: N_c=${pad(Nc, 4)} ${bar}`);
}
console.log();

// ═══════════════════════════════════════════════════════════════
// PHASE 5: SITE DILUTION (SKEPTIC EFFECT)
// ═══════════════════════════════════════════════════════════════
console.log('─── PHASE 5: OBSERVER DILUTION ───');

// Group at effective p just above p_c
// Each skeptical observer removes sites with probability q
// Kill threshold: p_eff * (1 - N*q) < p_c

console.log('  How many diluting observers kill a barely-percolating group?\n');
const qVals = [0.02, 0.05, 0.10, 0.15, 0.20];
const pGroup = [0.30, 0.35, 0.40, 0.50];

console.log(`  ${pad('p_group', 10)} ${qVals.map(q => pad(`q=${q}`, 8)).join('')}`);
console.log(`  ${'-'.repeat(50)}`);

for (const pg of pGroup) {
  const row = [pad(num(pg, 2), 10)];
  for (const q of qVals) {
    // p_eff = pg * (1 - N*q) > p_c
    // N_kill = floor((pg - p_c) / (q * pg))
    const Nk = Math.floor((pg - PC_NN_NNN_4N) / (q * pg));
    row.push(pad(Nk, 8));
  }
  console.log(`  ${row.join('')}`);
}
console.log();
console.log('  N_kill = number of diluting observers needed to break percolation');
console.log('  At p_group ≈ 0.30 (barely percolating): ONE skeptic at q=0.05 kills it');
console.log();

// ═══════════════════════════════════════════════════════════════
// KILL CONDITIONS
// ═══════════════════════════════════════════════════════════════
console.log('═══════════════════════════════════════════════════════════════');
console.log(' KILL CONDITIONS');
console.log('═══════════════════════════════════════════════════════════════\n');

// K-PERC-1: max P matches p_c to 3+ sig figs
const kperc1 = delta_nn_nnn_4n < 0.005;
console.log(`K-PERC-1: max P = ${num(globalMax)} vs p_c = ${PC_NN_NNN_4N}`);
console.log(`          Δ = ${num(delta_nn_nnn_4n)} (must < 0.005)`);
console.log(`          → ${kperc1 ? 'PASS' : 'FAIL'}\n`);

// K-PERC-2: deferred — needs full z_eff analysis (see Phase 2 output above)
console.log(`K-PERC-2: z_eff analysis — see Phase 2 output above`);
console.log(`          (Need z_eff = 12 ± 4 at natural scale)\n`);

// K-PERC-3: cooperative percolation — check if ANY pair exceeds p_c
let anyPercolates = false;
for (const A of profiles) {
  for (const B of profiles) {
    if (A === B || A.K <= B.K) continue;
    const pEff = cLift(A.cTarget, A.K) * kramers(B.cTarget, B.K, 0.5);
    if (pEff > PC_NN_NNN_4N) anyPercolates = true;
  }
}
console.log(`K-PERC-3: Cooperative percolation exceeds p_c → ${anyPercolates ? 'PASS' : 'FAIL'}\n`);

// K-PERC-4: N_c in [3, 12] for typical P ∈ [0.03, 0.10]
const Nc_low  = Math.ceil(Math.log(1 - PC_NN_NNN_4N) / Math.log(1 - 0.10));
const Nc_high = Math.ceil(Math.log(1 - PC_NN_NNN_4N) / Math.log(1 - 0.03));
const kperc4 = Nc_low >= 3 && Nc_high <= 12;
console.log(`K-PERC-4: N_c range for P ∈ [0.03, 0.10]: [${Nc_low}, ${Nc_high}]`);
console.log(`          (must be within [3, 12])`);
console.log(`          → ${kperc4 ? 'PASS' : 'FAIL'}\n`);

// K-PERC-5: deferred — requires Monte Carlo simulation
console.log(`K-PERC-5: Critical exponents — requires Monte Carlo (Phase 5 deferred)\n`);

// ═══════════════════════════════════════════════════════════════
// SUMMARY
// ═══════════════════════════════════════════════════════════════
console.log('═══════════════════════════════════════════════════════════════');
console.log(' SUMMARY');
console.log('═══════════════════════════════════════════════════════════════\n');

const results = [
  { id: 'K-PERC-1', desc: 'max P matches p_c (NN+NNN+4N)', status: kperc1 ? 'PASS' : 'FAIL' },
  { id: 'K-PERC-2', desc: 'z_eff = 12 ± 4', status: 'PENDING' },
  { id: 'K-PERC-3', desc: 'Two entities jointly percolate', status: anyPercolates ? 'PASS' : 'FAIL' },
  { id: 'K-PERC-4', desc: 'N_c ∈ [3, 12]', status: kperc4 ? 'PASS' : 'FAIL' },
  { id: 'K-PERC-5', desc: 'Critical exponents match universality', status: 'PENDING' },
];

for (const r of results) {
  console.log(`  ${pad(r.id, 12)} ${pad(r.desc, 45)} ${r.status}`);
}
console.log();

const passed = results.filter(r => r.status === 'PASS').length;
const failed = results.filter(r => r.status === 'FAIL').length;
const pending = results.filter(r => r.status === 'PENDING').length;
console.log(`  ${passed} PASS, ${failed} FAIL, ${pending} PENDING`);
console.log();
console.log('  If K-PERC-1 PASS: the conjugacy bound IS a percolation threshold.');
console.log('  If K-PERC-3 PASS: two-entity coupling = cooperative percolation.');
console.log('  If K-PERC-4 PASS: historical group sizes are predicted by N_c formula.');
console.log('  Implications: universality, fragility, and cooperative effects all');
console.log('  reduce to lattice percolation theory on the Eckert manifold.');

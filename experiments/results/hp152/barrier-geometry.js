/**
 * barrier-geometry.js
 *
 * Geometric properties of the Eckert manifold and Kramers barrier
 * for the Kagome strange metal (Paper 152 / §152).
 *
 * Constants: B_A = 0.867, B_G = 2.244
 */

const B_A = 0.867;
const B_G = 2.244;

function header(title) {
  console.log('\n' + '='.repeat(72));
  console.log(title);
  console.log('='.repeat(72));
}

function subheader(title) {
  console.log('\n--- ' + title + ' ---');
}

// ============================================================
// 1. FISHER METRIC PROPERTIES on [0,1]^3
// ============================================================
header('1. FISHER METRIC PROPERTIES on [0,1]³');

// Geodesic distance for a single coordinate: d(p,q) = 2|arcsin(√p) - arcsin(√q)|
function fisherDist1D(p, q) {
  return 2 * Math.abs(Math.asin(Math.sqrt(p)) - Math.asin(Math.sqrt(q)));
}

// Maximum single-coordinate distance: p=0 -> q=1
const maxSingleDist = fisherDist1D(0, 1);
console.log(`Geodesic distance d(0,1) single coordinate: ${maxSingleDist.toFixed(8)}`);
console.log(`  Expected π = ${Math.PI.toFixed(8)}`);
console.log(`  Match: ${Math.abs(maxSingleDist - Math.PI) < 1e-10 ? 'YES' : 'NO'}`);

// Maximum total distance: void pole (0,0,0) to constraint pole (1,1,1)
// d_total = sqrt(d1² + d2² + d3²) = sqrt(3) × π
const maxTotalDist = Math.sqrt(3) * Math.PI;
console.log(`\nMaximum total distance (0,0,0)→(1,1,1): ${maxTotalDist.toFixed(8)}`);
console.log(`  = π√3 = ${maxTotalDist.toFixed(8)}`);

// Volume of [0,1]³ in Fisher metric
// ∫₀¹ 1/√(p(1-p)) dp = π (Beta function B(1/2,1/2) = π)
// Volume = π × π × π = π³
const fisherVolume = Math.pow(Math.PI, 3);
console.log(`\nVolume of [0,1]³ in Fisher metric: ${fisherVolume.toFixed(8)}`);
console.log(`  = π³ = ${fisherVolume.toFixed(8)}`);

// Numerical check via trapezoidal integration
function fisherVolumeNumerical(N) {
  const eps = 1e-6;
  const h = (1 - 2*eps) / N;
  let vol = 0;
  for (let i = 0; i < N; i++) {
    const p = eps + (i + 0.5) * h;
    for (let j = 0; j < N; j++) {
      const q = eps + (j + 0.5) * h;
      for (let k = 0; k < N; k++) {
        const r = eps + (k + 0.5) * h;
        vol += 1 / Math.sqrt(p*(1-p) * q*(1-q) * r*(1-r));
      }
    }
  }
  return vol * Math.pow(h, 3);
}

const volNum = fisherVolumeNumerical(100);
console.log(`  Numerical check (N=100 midpoint): ${volNum.toFixed(6)}`);
console.log(`  Relative error: ${(Math.abs(volNum - fisherVolume) / fisherVolume * 100).toFixed(2)}%`);
console.log(`  (Large error expected: integrand has 1/√x singularity at boundaries,`);
console.log(`   midpoint rule converges slowly. Analytical result π³ is exact via`);
console.log(`   ∫₀¹ 1/√(p(1-p)) dp = B(1/2,1/2) = Γ(1/2)²/Γ(1) = π.)`);

// ============================================================
// 2. Pe=0 BOUNDARY GEOMETRY
// ============================================================
header('2. Pe=0 BOUNDARY GEOMETRY');

const C0 = B_A / B_G;
console.log(`C₀ = B_A/B_G = ${B_A}/${B_G} = ${C0.toFixed(8)}`);
console.log(`  = ${(B_A / B_G).toFixed(8)}`);

// σ(c) = sinh(2(B_A - C × B_G))
// At C = C₀: σ(C₀) = sinh(2(B_A - C₀ × B_G)) = sinh(0) = 0
console.log(`\nσ(C₀) = sinh(2(B_A - C₀×B_G)) = sinh(0) = 0  ✓`);

// dσ/dC = -2B_G × cosh(2(B_A - C×B_G))
// At C₀: dσ/dC = -2B_G × cosh(0) = -2B_G
const dSigmaDC = -2 * B_G;
console.log(`\ndσ/dC|_{C₀} = -2B_G × cosh(0) = -2B_G = ${dSigmaDC.toFixed(6)}`);

// d²σ/dC² = (-2B_G) × (-2B_G) × sinh(2(B_A - C×B_G)) = 4B_G² × sinh(...)
// At C₀: = 4B_G² × sinh(0) = 0
const d2SigmaDC2 = 4 * B_G * B_G * Math.sinh(0);
console.log(`d²σ/dC²|_{C₀} = 4B_G² × sinh(0) = ${d2SigmaDC2.toFixed(6)}`);

// d³σ/dC³ = -8B_G³ × cosh(2(B_A - C×B_G))
// At C₀: = -8B_G³ × cosh(0) = -8B_G³
const d3SigmaDC3 = -8 * Math.pow(B_G, 3);
console.log(`d³σ/dC³|_{C₀} = -8B_G³ × cosh(0) = -8B_G³ = ${d3SigmaDC3.toFixed(6)}`);
console.log(`  = ${d3SigmaDC3.toFixed(6)}`);

// ============================================================
// 3. BARRIER vs ΔC (distance from Pe=0)
// ============================================================
header('3. BARRIER vs ΔC (distance from Pe=0)');

const KAlphaRatios = [50, 100, 200, 500];
const targetBarriers = [4, 5, 6, 7, 8];

function sigma(C) {
  return Math.sinh(2 * (B_A - C * B_G));
}

function bNet(C) {
  const s = sigma(C);
  return 0.5 * Math.asinh(s);
}

function barrier(C, KOverAlpha) {
  const b = bNet(C);
  return 2 * b * b * KOverAlpha;
}

subheader('Scan: σ(c), b_net, b_net², barrier for ΔC = 0.01 to 0.15');

console.log('ΔC       σ(c)         b_net        b_net²       barrier(K/α=50)  barrier(K/α=100) barrier(K/α=200) barrier(K/α=500)');
console.log('-'.repeat(120));

const dCs = [];
for (let i = 1; i <= 15; i++) {
  dCs.push(i * 0.01);
}

for (const dc of dCs) {
  const C = C0 + dc;
  const s = sigma(C);
  const b = bNet(C);
  const b2 = b * b;
  const barriers = KAlphaRatios.map(ka => barrier(C, ka));
  console.log(
    `${dc.toFixed(2)}     ${s.toFixed(6).padStart(10)}  ${b.toFixed(6).padStart(10)}  ${b2.toFixed(6).padStart(10)}  ` +
    barriers.map(v => v.toFixed(4).padStart(14)).join('  ')
  );
}

subheader('ΔC values that give barrier = 4, 5, 6, 7, 8 for each K/α');

// Binary search for ΔC that gives target barrier
// barrier(C₀+ΔC) is monotonically increasing in ΔC (since b_net² grows with |ΔC|)
function findDC(targetBarrier, KOverAlpha) {
  let lo = 0.0001, hi = 0.5;
  for (let iter = 0; iter < 100; iter++) {
    const mid = (lo + hi) / 2;
    const C = C0 + mid;
    const b = barrier(C, KOverAlpha);
    if (b < targetBarrier) {
      lo = mid;   // need larger ΔC to get larger barrier
    } else {
      hi = mid;   // barrier too large, reduce ΔC
    }
  }
  return (lo + hi) / 2;
}

// Actually since C > C₀ makes σ < 0 and b_net < 0, barrier = 2b_net²K/α is still positive.
// But we need |barrier| to match targets. Let me check the direction.
// σ(C₀+ΔC) = sinh(2(B_A - (C₀+ΔC)B_G)) = sinh(-2ΔC×B_G) < 0
// b_net = ½arcsinh(σ) < 0
// b_net² > 0
// barrier = 2b_net²K/α > 0 ✓

console.log('\nTarget barrier values → required ΔC:');
console.log('barrier    K/α=50       K/α=100      K/α=200      K/α=500');
console.log('-'.repeat(65));

for (const tb of targetBarriers) {
  const row = KAlphaRatios.map(ka => findDC(tb, ka).toFixed(6).padStart(12));
  console.log(`${tb}       ${row.join('  ')}`);
}

// ============================================================
// 4. SELF-CONSISTENCY TEST
// ============================================================
header('4. SELF-CONSISTENCY TEST');

console.log('Linearized barrier formula: barrier ≈ 2B_G²ΔC²K/α');
console.log('So: ΔC = √(barrier × α / (2 × B_G² × K)) = √(barrier / (2 × B_G² × K/α))');
console.log(`2B_G² = ${(2 * B_G * B_G).toFixed(6)}`);

const KAlphaCheck = [50, 100, 235, 500];

console.log('\nLinearized ΔC (from ΔC² = B*/(2B_G²×K/α)):');
console.log('B*       K/α=50       K/α=100      K/α=235      K/α=500      Linearization valid?');
console.log('-'.repeat(85));

for (const bStar of targetBarriers) {
  const row = KAlphaCheck.map(ka => {
    const dc = Math.sqrt(bStar / (2 * B_G * B_G * ka));
    return dc;
  });
  const valid = row.map(dc => dc < 0.1 ? 'YES' : (dc < 0.2 ? 'MARGINAL' : 'NO'));
  console.log(
    `${bStar}       ${row.map(dc => dc.toFixed(6).padStart(12)).join('  ')}  ${valid.join('/')}`
  );
}

subheader('Comparison: linearized ΔC vs exact ΔC');
console.log('B*   K/α    ΔC_exact     ΔC_linear    rel_error(%)');
console.log('-'.repeat(55));

for (const bStar of [4, 6, 8]) {
  for (const ka of [50, 100, 500]) {
    const dcExact = findDC(bStar, ka);
    const dcLinear = Math.sqrt(bStar / (2 * B_G * B_G * ka));
    const relErr = Math.abs(dcExact - dcLinear) / dcExact * 100;
    console.log(
      `${bStar}    ${String(ka).padStart(3)}    ${dcExact.toFixed(6).padStart(10)}   ${dcLinear.toFixed(6).padStart(10)}   ${relErr.toFixed(2).padStart(8)}`
    );
  }
}

subheader('KEY INSIGHT: Why linearized = exact');
console.log('The "linearized" formula is actually EXACT, not an approximation.');
console.log('Proof:');
console.log('  σ(C₀+ΔC) = sinh(2(B_A - (C₀+ΔC)×B_G)) = sinh(-2ΔC×B_G)');
console.log('  b_net = ½arcsinh(σ) = ½arcsinh(sinh(-2ΔC×B_G)) = ½(-2ΔC×B_G) = -ΔC×B_G');
console.log('  b_net² = ΔC²×B_G²');
console.log('  barrier = 2×b_net²×K/α = 2×B_G²×ΔC²×K/α   (EXACT, no Taylor truncation)');
console.log('');
console.log('  arcsinh(sinh(x)) = x is an identity, so no linearization was ever needed.');
console.log('  The barrier depends on ΔC² exactly, with coefficient 2B_G²K/α.');

// ============================================================
// 5. KEY GEOMETRIC CONSTANTS
// ============================================================
header('5. KEY GEOMETRIC CONSTANTS');

const constants = [
  ['π√3', Math.PI * Math.sqrt(3)],
  ['2π', 2 * Math.PI],
  ['π²', Math.PI * Math.PI],
  ['π²/2', Math.PI * Math.PI / 2],
  ['B_G²', B_G * B_G],
  ['2B_G', 2 * B_G],
  ['4B_A', 4 * B_A],
  ['B_A × B_G', B_A * B_G],
  ['2B_A²', 2 * B_A * B_A],
  ['2B_G²', 2 * B_G * B_G],
  ['B_G³', Math.pow(B_G, 3)],
  ['8B_G³', 8 * Math.pow(B_G, 3)],
  ['B_A/B_G', B_A / B_G],
  ['(1-C₀)×9', (1 - B_A/B_G) * 9],
];

const intTargets = [4, 5, 6, 7, 8];

console.log('Constant             Value          Close to integer?');
console.log('-'.repeat(60));

for (const [name, val] of constants) {
  const matches = intTargets.filter(t => Math.abs(val - t) < 0.2);
  const matchStr = matches.length > 0 ? `≈ ${matches.join(', ')} (Δ=${matches.map(t => (val-t).toFixed(3)).join(', ')})` : '';
  console.log(`${name.padEnd(18)}   ${val.toFixed(8).padStart(12)}  ${matchStr}`);
}

// ============================================================
// 6. THE MEAN-FIELD PREDICTION
// ============================================================
header('6. THE MEAN-FIELD PREDICTION');

const A_mf = 200;  // mean-field coupling amplification from §111
const alpha_Ni3In = 0.213;  // Ni₃In coupling

console.log('Mean-field model:');
console.log(`  A (coupling amplification from §111) = ${A_mf}`);
console.log(`  T_eff = α/2 = ${alpha_Ni3In}/2 = ${(alpha_Ni3In/2).toFixed(4)}`);
console.log(`  V'' = K/(A×α)`);
console.log(`  ΔC² = T_eff / V'' = A×α²/(2K)`);
console.log(`  barrier = 2B_G²×ΔC²×K/α = 2B_G² × (Aα²/(2K)) × K/α = B_G²×A×α`);
console.log('');

const barrierPredicted = B_G * B_G * A_mf * alpha_Ni3In;
console.log(`  barrier = B_G² × A × α`);
console.log(`         = ${B_G*B_G} × ${A_mf} × ${alpha_Ni3In}`);
console.log(`         = ${(B_G*B_G).toFixed(6)} × ${A_mf} × ${alpha_Ni3In}`);
console.log(`         = ${barrierPredicted.toFixed(4)}`);
console.log('');
console.log(`  Target (Ni₃In measured): 4.24`);
console.log(`  Ratio predicted/measured: ${(barrierPredicted / 4.24).toFixed(4)}`);
console.log(`  Match: ${Math.abs(barrierPredicted - 4.24) < 0.5 ? 'NO' : 'NO'} (off by ${(barrierPredicted - 4.24).toFixed(4)})`);

subheader('What A would be needed to match barrier = 4.24?');
const A_needed = 4.24 / (B_G * B_G * alpha_Ni3In);
console.log(`  A_needed = 4.24 / (B_G² × α) = 4.24 / (${(B_G*B_G).toFixed(4)} × ${alpha_Ni3In})`);
console.log(`           = ${A_needed.toFixed(4)}`);

subheader('What α would be needed with A=200 to match barrier = 4.24?');
const alpha_needed = 4.24 / (B_G * B_G * A_mf);
console.log(`  α_needed = 4.24 / (B_G² × A) = 4.24 / (${(B_G*B_G).toFixed(4)} × ${A_mf})`);
console.log(`           = ${alpha_needed.toFixed(6)}`);

subheader('Barrier for other domains (using B_G²×A×α model)');
const domains = [
  ['Ni₃In (kagome)', 0.213, 200],
  ['Nuclear (α-decay)', 0.5, 200],
  ['Solar corona', 0.4, 200],
  ['Xenobot memory', 0.3, 200],
];

console.log('Domain                   α       A     barrier=B_G²×A×α    Published barrier');
console.log('-'.repeat(80));
for (const [name, alpha, Amf] of domains) {
  const b = B_G * B_G * Amf * alpha;
  console.log(`${name.padEnd(24)} ${alpha.toFixed(3)}   ${Amf}   ${b.toFixed(4).padStart(18)}    -`);
}

subheader('Alternative: barrier = 2B_G²×K/α×ΔC² (direct formula)');
console.log('For Ni₃In: ΔC = 0.042, K/α unknown');
console.log('');

const DC_Ni3In = 0.042;
const barrier_per_KAlpha = 2 * B_G * B_G * DC_Ni3In * DC_Ni3In;
console.log(`  2B_G²×ΔC² = 2 × ${(B_G*B_G).toFixed(4)} × ${DC_Ni3In}² = ${barrier_per_KAlpha.toFixed(6)}`);
console.log(`  barrier = ${barrier_per_KAlpha.toFixed(6)} × (K/α)`);
console.log(`  For barrier = 4.24: K/α = 4.24 / ${barrier_per_KAlpha.toFixed(6)} = ${(4.24 / barrier_per_KAlpha).toFixed(2)}`);

subheader('Summary Table: Universal Kramers barriers');
console.log('Domain               Barrier   ΔC      K/α implied (from 2B_G²ΔC²K/α)');
console.log('-'.repeat(70));
const universalBarriers = [
  ['Nuclear α-decay', 7.0, null],
  ['Solar corona', 6.54, null],
  ['Xenobot memory', 6.8, null],
  ['Ni₃In strange metal', 4.24, 0.042],
];

for (const [name, b, dc] of universalBarriers) {
  if (dc !== null) {
    const kaImplied = b / (2 * B_G * B_G * dc * dc);
    console.log(`${name.padEnd(22)} ${b.toFixed(2)}    ${dc.toFixed(3)}   ${kaImplied.toFixed(1)}`);
  } else {
    console.log(`${name.padEnd(22)} ${b.toFixed(2)}    -       -`);
  }
}

console.log('\n' + '='.repeat(72));
console.log('COMPUTATION COMPLETE');
console.log('='.repeat(72));

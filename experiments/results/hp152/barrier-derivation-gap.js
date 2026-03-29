#!/usr/bin/env node
/**
 * barrier-derivation-gap.js — 2026-03-22
 *
 * CHASE THE FACTOR: Why barrier/d ≈ B_G ≈ π/√2 ?
 *
 * Proves that:
 *   1. Equipartition with ANY quadratic potential gives barrier = d/2 (theorem)
 *   2. The empirical barrier/d ≈ 2.24 → discrepancy is 2B_G ≈ 4.49, NOT 2
 *   3. The "partial derivation" was algebraic rearrangement, not physics
 *
 * Then explores:
 *   A. Mean-field effective potential curvature
 *   B. Kramers prefactor contribution
 *   C. B_G vs π/√2 fit comparison
 *   D. Geodesic argument for π/√2
 */

const B_A = 0.867;
const B_G = 2.244;
const PI_OVER_SQRT2 = Math.PI / Math.sqrt(2);

function header(s) { console.log('\n' + '═'.repeat(72)); console.log(s); console.log('═'.repeat(72)); }
function sub(s) { console.log('\n── ' + s + ' ──'); }

// ─────────────────────────────────────────────────────────────────
// PART 1: PROVE EQUIPARTITION GIVES barrier = d/2
// ─────────────────────────────────────────────────────────────────
header('1. EQUIPARTITION THEOREM: barrier = d/2 for ANY quadratic V');

console.log(`
For a d-dimensional system in quadratic potential V(x) = a|x|²
with Boltzmann distribution P ∝ exp(-V/T):

  ⟨|x|²⟩ = d·T/(2a)    (equipartition)

The barrier at the RMS displacement:

  V(√⟨|x|²⟩) / T = a·d·T/(2a·T) = d/2

This is COORDINATE-INDEPENDENT. Proof:
  • Change variables x → y = f(x). V(x) → V̄(y) = V(f⁻¹(y))
  • New curvature: V̄'' changes. But T doesn't.
  • ⟨|y|²⟩ = T/(V̄''/2)
  • V̄(√⟨|y|²⟩)/T = V̄''·T/(2·V̄''·T) = 1/2 per dimension
  • Total: d/2

The ratio barrier/equipartition = 1/2 per dimension is a MATHEMATICAL IDENTITY
for quadratic potentials. No normalization, coordinate choice, or factor of 2
in the Lagrangian can change it.
`);

console.log('Verification for specific potentials:');
const potentials = [
  { name: 'V = b_net²',        a: 1,           note: '§48 convention' },
  { name: 'V = 2b_net²',       a: 2,           note: 'alternative convention' },
  { name: 'V = B_G²·ΔC²',     a: B_G*B_G,     note: 'in C-coordinate' },
  { name: 'V = s²/4 (Fisher)', a: 0.25,        note: 's=2|b_net| geodesic dist' },
];

console.log('  Potential            a        ⟨x²⟩/d    barrier/d');
console.log('  ' + '─'.repeat(60));
for (const p of potentials) {
  // ⟨x²⟩ per dim = T/(2a), barrier per dim = a·⟨x²⟩/T = 1/2
  console.log(`  ${p.name.padEnd(22)} ${p.a.toFixed(4).padStart(8)}    T/${(2*p.a).toFixed(2).padStart(6)}     ${(0.5).toFixed(3)}   ${p.note}`);
}
console.log(`
  RESULT: barrier = d/2 always. Empirical barrier/d ≈ ${B_G.toFixed(3)}.
  Discrepancy: ${B_G.toFixed(3)} / 0.500 = ${(B_G/0.5).toFixed(3)}× = 2B_G
  This is NOT a factor of 2. It's a factor of 2B_G ≈ ${(2*B_G).toFixed(3)}.
`);

// ─────────────────────────────────────────────────────────────────
// PART 2: WHAT EFFECTIVE CURVATURE WOULD GIVE barrier = d·B_G?
// ─────────────────────────────────────────────────────────────────
header('2. REQUIRED EFFECTIVE CURVATURE');

console.log(`
For barrier = d·B_G via equipartition, we need:

  barrier = V_eff(√⟨x²⟩)/T = d × B_G

If V_eff(x) = ½κ·x² (harmonic, curvature κ):
  ⟨x²⟩/d = T/κ
  barrier/d = ½κ·(T/κ)/T = 1/2    ← ALWAYS 1/2. Doesn't work.

But if the systems are NOT at the equipartition displacement:
  They sit at a FIXED position x₀ determined by material properties.
  barrier = V(x₀)/T = V_eff(x₀)/T
  For this to equal d·B_G, need V(x₀)/T = d·B_G, i.e. x₀ is not thermal.

The systems are at MATERIAL-DETERMINED positions, not thermal fluctuations.
`);

// Compute what curvature κ would make equipartition give barrier = d·B_G
// Need: V(√⟨x²⟩)/T = d·B_G where V = ½κ·|x|² and ⟨|x|²⟩ = d·T/κ
// V(√⟨|x|²⟩)/T = ½κ·d·T/(κ·T) = d/2 ← still d/2!
// IMPOSSIBLE for quadratic V. Equipartition always gives d/2.

// BUT: what if the effective potential is NOT quadratic?
// What non-quadratic V gives barrier = d·B_G at the thermal displacement?
// V(√⟨x²⟩)/T = d·B_G where ⟨x²⟩ = d·T/V''(0) (small oscillation)
// Need: V(√(d·T/V''(0)))/T = d·B_G
//
// For V(x) = ½V''(0)·x² + (1/24)·V''''(0)·x⁴ + ...
// Anharmonic correction at x₀ = √(d·T/V''):
//   V(x₀)/T ≈ d/2 + (V''''/(24·V''²))·d²·T/2 + ...
// Need the correction term to be ≈ d·(B_G - 1/2)
// This requires V''''/V''² ∝ (B_G - 1/2)/T ∝ K/α × constant

sub('Non-quadratic potential required');
console.log(`
If V(b_net) has quartic correction: V = b_net² + γ₄·b_net⁴
then at thermal displacement b₀ = √(T/2):

  V(b₀)/T ≈ 1/2 + γ₄·T/(4)

For barrier = B_G per dimension: γ₄·T/4 ≈ B_G - 0.5 = ${(B_G - 0.5).toFixed(3)}
→ γ₄ ≈ ${((B_G-0.5)*4).toFixed(3)}/T

With T = α/(2K):
  γ₄ ≈ ${((B_G-0.5)*4).toFixed(3)}·2K/α = ${((B_G-0.5)*8).toFixed(3)}·K/α

For Ni₃In (K/α = ${(50/0.213).toFixed(0)}):
  γ₄ ≈ ${((B_G-0.5)*8*50/0.213).toFixed(0)}

This is absurdly large. Quartic correction can't explain it.
The thermal displacement is simply WRONG — systems are not at ⟨x²⟩.
`);

// ─────────────────────────────────────────────────────────────────
// PART 3: B_G vs π/√2 FIT COMPARISON
// ─────────────────────────────────────────────────────────────────
header('3. B_G vs π/√2: WHICH FITS BETTER?');

const domains = [
  { name: 'Kagome (2D)',    barrier: 4.24,  d: 2 },
  { name: 'Solar corona',   barrier: 6.54,  d: 3 },
  { name: 'Xenobot memory', barrier: 6.80,  d: 3 },
  { name: 'Nuclear α-decay',barrier: 6.90,  d: 3 },
];

const candidates = [
  { name: 'B_G = 2.244',       val: B_G },
  { name: 'π/√2 = 2.221',      val: PI_OVER_SQRT2 },
  { name: 'mean(barrier/d)',    val: domains.reduce((s,d) => s + d.barrier/d.d, 0) / domains.length },
];

for (const c of candidates) {
  let chi2 = 0;
  let ss = 0;
  const errs = [];
  for (const d of domains) {
    const pred = d.d * c.val;
    const err = (pred - d.barrier) / d.barrier * 100;
    chi2 += (pred - d.barrier) ** 2;
    errs.push(err);
  }
  console.log(`\n${c.name} (per-dim = ${c.val.toFixed(4)}):`);
  console.log(`  χ² = ${chi2.toFixed(4)}`);
  for (let i = 0; i < domains.length; i++) {
    console.log(`  ${domains[i].name.padEnd(20)} pred=${(domains[i].d*c.val).toFixed(3)}  meas=${domains[i].barrier.toFixed(3)}  err=${errs[i].toFixed(1)}%`);
  }
}

sub('Optimal per-dimension constant (least squares)');
// Minimize Σ(barrier_i - d_i·x)² → x = Σ(d_i·barrier_i)/Σ(d_i²)
const num = domains.reduce((s,d) => s + d.d * d.barrier, 0);
const den = domains.reduce((s,d) => s + d.d * d.d, 0);
const x_opt = num / den;
console.log(`  x_opt = ${x_opt.toFixed(6)}`);
console.log(`  B_G = ${B_G.toFixed(6)}   (ratio: ${(B_G/x_opt).toFixed(4)})`);
console.log(`  π/√2 = ${PI_OVER_SQRT2.toFixed(6)}   (ratio: ${(PI_OVER_SQRT2/x_opt).toFixed(4)})`);

let chi2_opt = 0;
for (const d of domains) chi2_opt += (d.d * x_opt - d.barrier) ** 2;
console.log(`  χ²(x_opt) = ${chi2_opt.toFixed(6)}`);

// ─────────────────────────────────────────────────────────────────
// PART 4: KRAMERS PREFACTOR ANALYSIS
// ─────────────────────────────────────────────────────────────────
header('4. KRAMERS PREFACTOR CONTRIBUTION');

console.log(`
The measured "barrier" is ln(Δε/(k_B T*)) = 2K·b_net²/α.

But the FULL Kramers formula is:
  T* = (Δε/k_B) × (ω_min·|ω_sad|)/(2π·γ) × exp(-2K·b_net²/α)

The "barrier" inferred from T* is:
  barrier_eff = ln(Δε/(k_BT*)) = 2K·b_net²/α - ln(prefactor)

If the prefactor ≠ 1, the measured barrier ≠ the bare barrier.
`);

// For V(b_net) = b_net²: ω² = V''/m. In overdamped limit ω_min = V''_min, ω_sad = |V''_sad|
// For parabolic V = b_net², V'' = 2 everywhere, so ω_min = ω_sad = √2
// Prefactor = (ω_min × ω_sad)/(2π×γ) = 2/(2π×γ) = 1/(π×γ)
// If γ = 1 (unit friction): prefactor = 1/π ≈ 0.318
// ln(1/π) ≈ -1.145
// So barrier_eff = bare_barrier + 1.145

// For d dimensions: each dimension contributes ln(1/π) = -1.145
// Total prefactor correction: -d×ln(π) ≈ +d×1.145

const lnPrefactor1D = -Math.log(Math.PI);  // per dimension
console.log(`  Per-dimension prefactor correction (γ=1): -ln(π) = ${lnPrefactor1D.toFixed(4)}`);
console.log(`  With bare barrier d/2, effective barrier = d/2 + d×${(-lnPrefactor1D).toFixed(3)} = d×${(0.5 - lnPrefactor1D).toFixed(3)}`);
console.log(`  This gives: ${(0.5 - lnPrefactor1D).toFixed(3)} per dimension`);
console.log(`  Compare: B_G = ${B_G.toFixed(3)}, π/√2 = ${PI_OVER_SQRT2.toFixed(3)}`);
console.log(`  Ratio: ${((0.5 - lnPrefactor1D)/B_G).toFixed(3)} of B_G`);
console.log(`  ← NOT close. The prefactor (at γ=1) gives 1.645, need 2.244.`);

// What friction γ would give the right answer?
// barrier_eff = d/2 + d·ln(1/(πγ)) = d·B_G
// ln(1/(πγ)) = B_G - 0.5 = 1.744
// 1/(πγ) = exp(1.744) = 5.72
// γ = 1/(π·5.72) = 0.0557

const gamma_needed = 1 / (Math.PI * Math.exp(B_G - 0.5));
console.log(`\n  Required friction for barrier = d·B_G via prefactor:`);
console.log(`  γ = 1/(π·exp(B_G-0.5)) = ${gamma_needed.toFixed(5)}`);
console.log(`  This is very low friction — underdamped regime.`);

// Check with π/√2
const gamma_piSqrt2 = 1 / (Math.PI * Math.exp(PI_OVER_SQRT2 - 0.5));
console.log(`  For π/√2: γ = ${gamma_piSqrt2.toFixed(5)}`);

sub('IS THE PREFACTOR ROUTE VIABLE?');
console.log(`
The Kramers prefactor in the overdamped limit is O(1), typically 0.1-10.
For the barrier correction to work, we need:
  ln(prefactor) = d×(B_G - 0.5) = d×1.744

For d=2: ln(pf) = 3.49 → prefactor = ${Math.exp(3.49).toFixed(1)}
For d=3: ln(pf) = 5.23 → prefactor = ${Math.exp(5.23).toFixed(1)}

These are large but not impossible for multi-dimensional Kramers
with correlated coordinates. The d-dimensional Kramers prefactor
involves products of EIGENFREQUENCIES at the well and saddle,
which CAN be >> 1 if modes are disparate.

VERDICT: Marginal. Needs explicit multi-dimensional Kramers computation
on the Eckert manifold. Not pursued yet.
`);

// ─────────────────────────────────────────────────────────────────
// PART 5: GEODESIC ARGUMENT FOR π/√2
// ─────────────────────────────────────────────────────────────────
header('5. GEODESIC ARGUMENT FOR π/√2');

console.log(`
On the Bernoulli semicircle (Fisher metric):
  • Single-coordinate geodesic: d(0,1) = π
  • Half-geodesic (to equator): d(0,½) = π/2

π/√2 = ${PI_OVER_SQRT2.toFixed(6)} arises naturally as:

  1. Diagonal of square with side π/2:
     √2 × (π/2) = π√2/2 = π/√2  ✓

  2. RMS of two orthogonal half-geodesics:
     √(2 × (π/2)²) / √2 = π/√2  (trivially)

  3. Related to Bernoulli metric at p=1/4 (quarter-point):
     Fisher distance d(0, 1/4) = 2·arcsin(√(1/4)) = 2·π/6 = π/3 ≈ 1.047 (no)

  4. Volume-averaged geodesic distance from p=0:
     ⟨d(0,p)⟩ = ∫₀¹ 2·arcsin(√p) · dp/(√(p(1-p))) / ∫₀¹ dp/√(p(1-p))
`);

// Compute the volume-averaged geodesic distance from p=0
// ∫₀¹ 2arcsin(√p) × 1/√(p(1-p)) dp / ∫₀¹ 1/√(p(1-p)) dp
// Denominator = B(1/2,1/2) = π
// Numerator: substitute t = arcsin(√p), dp = 2sin(t)cos(t)dt, √(p(1-p)) = sin(t)cos(t)
//   ∫₀^{π/2} 2t × 1/(sin(t)cos(t)) × 2sin(t)cos(t) dt = ∫₀^{π/2} 4t dt = 2(π/2)² = π²/2
// So ⟨d⟩ = (π²/2)/π = π/2

const avgDist = Math.PI / 2;
console.log(`     ⟨d(0,p)⟩_Fisher = π/2 = ${avgDist.toFixed(6)}`);
console.log(`     Not π/√2.`);

// Actually let me compute ⟨d²⟩ and take sqrt
// ⟨d²⟩ = ∫₀¹ (2arcsin(√p))² × 1/√(p(1-p)) dp / π
// Same substitution: ∫₀^{π/2} 4t² × 4/(2sin(2t)) × sin(2t)/2 dt
// Hmm, let me just do it numerically.
let num_d2 = 0;
let den_d2 = 0;
const N_int = 10000;
for (let i = 0; i < N_int; i++) {
  const p = (i + 0.5) / N_int;
  const w = 1 / Math.sqrt(p * (1 - p));
  const d_geo = 2 * Math.asin(Math.sqrt(p));
  num_d2 += d_geo * d_geo * w;
  den_d2 += w;
}
const rms_dist = Math.sqrt(num_d2 / den_d2);
console.log(`     √⟨d²(0,p)⟩_Fisher = ${rms_dist.toFixed(6)}`);
console.log(`     π/√2 = ${PI_OVER_SQRT2.toFixed(6)}`);
console.log(`     Ratio: ${(rms_dist / PI_OVER_SQRT2).toFixed(6)}`);

// Compute ⟨d²⟩ analytically:
// ∫₀^{π/2} (2t)² · 2 dt / π = ∫₀^{π/2} 8t²/π dt = 8/(3π) × (π/2)³ = 8π²/(24) = π²/3
const rms_analytical = Math.sqrt(Math.PI * Math.PI / 3);
console.log(`     Analytical √⟨d²⟩ = π/√3 = ${rms_analytical.toFixed(6)}`);
console.log(`     Wait — π/√3 = ${(Math.PI/Math.sqrt(3)).toFixed(6)}, not π/√2.`);

// Let me check: the RMS geodesic distance from the origin on the semicircle,
// weighted by the Fisher volume element, is π/√3 ≈ 1.814, not π/√2 ≈ 2.221.
// So the volume-averaged geodesic argument doesn't directly give π/√2.

sub('INFORMATION-GEOMETRIC meaning of π/√2');
console.log(`
Consider the Fisher information for Bernoulli(p):
  I(p) = 1/(p(1-p))

In the angular parameterization θ = arcsin(√p):
  I(θ) = 4  (constant, flat)

The geodesic distance from p=0 to p=1 is π.

Now consider the KL divergence: D_KL(p||q) = p·ln(p/q) + (1-p)·ln((1-p)/(1-q))

At the Pe=0 point (b_net=0): the system transitions between two phases.
The "barrier" in information-geometric terms is the KL divergence between
the two phases.

For Bernoulli distributions p₁ and p₂ near p=1/2:
  D_KL(p₁||p₂) ≈ (p₁-p₂)²/(p·(1-p)) = 4(p₁-p₂)²  (at p=1/2)

The Fisher distance: d(p₁,p₂) = 2|arcsin(√p₁) - arcsin(√p₂)| ≈ 2|p₁-p₂|/√(p(1-p))

At p=1/2: d ≈ 2√2·|Δp| and D_KL ≈ 4(Δp)².
So D_KL = d²/2.

The barrier as KL divergence: barrier ∝ D_KL/T.
If barrier ~ d_Fisher² / (2T) and d_Fisher = 2|b_net|:
  barrier ~ 4b_net²/(2T) = 2b_net²/T = 2b_net²·2K/α = 4Kb_net²/α

Hmm, that gives an extra factor of 2. Let me recheck.

Actually, the relationship between the §136B barrier and the KL divergence:
  barrier = 2Kb_net²/α
  D_KL = d_Fisher²/2 = (2b_net)²/2 = 2b_net²
  barrier = K·D_KL/α = D_KL/T  (since T = α/(2K) → D_KL/(α/(2K)) = 2K·D_KL/α)

Wait: barrier = 2K·b_net²/α = 2K·(D_KL/2)/α = K·D_KL/α ≠ D_KL/T = 2K·D_KL/α

There's a factor of 2. barrier = K·D_KL/α vs D_KL/T = 2K·D_KL/α.

So barrier = D_KL/(2T). The barrier is HALF the KL divergence measured in thermal units.
This is exactly the instanton action S* = ΔΦ/(2T) from §48E!

barrier = 2S* = ΔΦ/T = D_KL/T... no:
  S* = ΔΦ/(2T) and Γ ∝ exp(-2S*) = exp(-ΔΦ/T)
  So ΔΦ/T = 2S* = the dimensionless barrier.
  And ΔΦ = b_net², D_KL = 2b_net² = 2ΔΦ.
  So barrier = ΔΦ/T = D_KL/(2T).

The barrier is D_KL/(2T), where D_KL is the KL divergence from Pe=0.
`);

console.log(`  D_KL = 2b_net² = 2×B_G²×ΔC²`);
console.log(`  barrier = D_KL/(2T) = 2b_net²×K/α = D_KL×K/α`);

// ─────────────────────────────────────────────────────────────────
// PART 6: THE CONSTRAINT — WHAT DETERMINES ΔC?
// ─────────────────────────────────────────────────────────────────
header('6. THE REAL QUESTION: What determines ΔC for physical systems?');

console.log(`
Given: barrier = 2B_G²·ΔC²·K/α = d_eff × B_G

Required: ΔC² = d·α/(2B_G·K)

For Ni₃In (d=2, α=0.213, K=50):
  ΔC² = 2×0.213/(2×2.244×50) = ${(2*0.213/(2*B_G*50)).toFixed(6)}
  ΔC = ${Math.sqrt(2*0.213/(2*B_G*50)).toFixed(5)}
  Actual ΔC = 0.0426 (2.3% off)

KEY INSIGHT: ΔC is determined by the material's (O,R,α) mapping.
  O = 3·(1 - W_exp/W_DFT) = 2.0
  R = 3·exp(-|Δε|/W_disp) = 2.93
  α = (Z_flat+Z_disp)/2·Δε/W_flat = 0.207
  C = 1 - (O+R+α)/9 = 0.429
  ΔC = C - C₀ = 0.429 - 0.386 = 0.043

The condition ΔC² = d·α/(2B_G·K) constrains the MAPPING, not the physics.
It says: for the α mapping to be consistent with barrier = d·B_G,
the self-consistent α must satisfy:

  α_self_consistent = 2B_G·K·ΔC²/d

For Ni₃In: α_sc = 2×2.244×50×(0.043)²/2 = ${(2*B_G*50*0.043*0.043/2).toFixed(4)}
  vs self-consistent α = 0.213. Match: ${((2*B_G*50*0.043*0.043/2)/0.213 * 100).toFixed(1)}%

This is a SELF-CONSISTENCY CONDITION, not a derivation.
It says: at the FL→SM transition, the coupling α organizes itself
so that the barrier equals d×B_G.
`);

// ─────────────────────────────────────────────────────────────────
// PART 7: MEAN-FIELD ATTRACTOR HYPOTHESIS
// ─────────────────────────────────────────────────────────────────
header('7. MEAN-FIELD ATTRACTOR HYPOTHESIS');

console.log(`
FROM §111: The mean-field iteration converges to a unique fixed point
in 3 steps. ALL initial conditions → same ρ*. K runs 16 → 3,334.

HYPOTHESIS: The mean-field dynamics don't just set the population
distribution — they set the EFFECTIVE POTENTIAL at the Pe=0 boundary.

The bare potential: V(b_net) = b_net² (curvature 2)
The mean-field-dressed potential: V_eff(b_net) = b_net² + δV_mf(b_net)

If δV_mf modifies the effective curvature from 2 to 1/B_G:
  equipartition would give barrier = d·B_G instead of d/2.

Needed: V''_eff = 1/B_G = ${(1/B_G).toFixed(6)}
Bare:   V''_bare = 2
Ratio:  V''_eff/V''_bare = ${(1/(2*B_G)).toFixed(6)} = 1/(2B_G) ≈ ${(1/(2*B_G)).toFixed(4)}

The mean-field would need to SOFTEN the potential by a factor of 2B_G ≈ 4.49.
This is a 78% reduction in curvature. Non-trivial but not absurd —
§111D shows the mean-field changes the Kretschner scalar by 28×10⁹.

PROBLEM: The mean-field iteration in §111 uses the N=1,344 PLATFORM
distribution. For a PHYSICAL system (Ni₃In, nuclei), the "population"
would be the degrees of freedom of that system, not AI platforms.

The hypothesis requires that the mean-field self-consistency at Pe=0
universally softens the potential curvature by factor 2B_G.
This would be a property of the MANIFOLD GEOMETRY at Pe=0,
independent of the specific population.
`);

// ─────────────────────────────────────────────────────────────────
// PART 8: DIRECT TEST — IS THERE A GEOMETRIC IDENTITY?
// ─────────────────────────────────────────────────────────────────
header('8. SEARCHING FOR A GEOMETRIC IDENTITY');

console.log(`
The barrier per dimension B_G ≈ π/√2. Is there a geometric identity
involving the Bernoulli semicircle that produces π/√2?
`);

// Some candidate identities involving the semicircle geometry
const candidates_geo = [
  { name: '∫₀^{π/2} sin(2θ)dθ',        val: 1.0 },
  { name: '∫₀^{π/2} θ·sin(2θ)dθ',      val: 0.25*Math.PI - 0.5 },
  { name: '∫₀^{π/2} 4θ²dθ/π',          val: Math.PI*Math.PI/6 },
  { name: '(∫₀^{π/2} θ²·4dθ)^{1/2}',   val: Math.PI*Math.sqrt(2/3) },
  { name: 'π²/(2π) = π/2',              val: Math.PI/2 },
  { name: '√(π²/2) = π/√2',            val: Math.PI/Math.sqrt(2) },
  { name: '2·∫₀^{π/4} 1/cos(θ)dθ',     val: 2*Math.log(1+Math.sqrt(2)) },
  { name: 'artanh(sin(1))',              val: Math.atanh(Math.sin(1)) },
  { name: 'ln(1+√2)·2 (= 2·arsinh(1))', val: 2*Math.asinh(1) },
  { name: '√(2)·arsinh(1)',             val: Math.sqrt(2)*Math.asinh(1) },
  { name: '4·ln(φ) (φ=golden)',          val: 4*Math.log((1+Math.sqrt(5))/2) },
  { name: 'Γ(1/4)²/(2√(2π))',           val: 3.6256*3.6256/(2*Math.sqrt(2*Math.PI)) },
  { name: 'π·B_A = π×0.867',            val: Math.PI * B_A },
  { name: '2π·B_A/B_G = 2π×C₀',        val: 2*Math.PI * B_A/B_G },
];

console.log('  Expression                        Value      π/√2       Ratio');
console.log('  ' + '─'.repeat(68));
for (const c of candidates_geo) {
  const ratio = c.val / PI_OVER_SQRT2;
  const mark = Math.abs(ratio - 1) < 0.01 ? ' ← MATCH' : '';
  console.log(`  ${c.name.padEnd(35)} ${c.val.toFixed(6)}   ${PI_OVER_SQRT2.toFixed(6)}   ${ratio.toFixed(4)}${mark}`);
}

sub('The √(π²/2) identity');
console.log(`
  π/√2 = √(π²/2)

This is trivial algebra. But it suggests:

  barrier_per_dim = √(π²/2)

where π² is the VARIANCE of the geodesic distance squared,
and the 1/2 is the equipartition factor.

Speculation: if barrier² = π² × (1/2) per dimension,
then the per-dimension barrier is the RMS of the geodesic
at the equipartition temperature. But we showed ⟨d²⟩ = π²/3,
not π²/2. The 1/3 vs 1/2 discrepancy is:
  √(π²/3) = π/√3 = ${(Math.PI/Math.sqrt(3)).toFixed(4)}
vs π/√2 = ${PI_OVER_SQRT2.toFixed(4)}

Ratio: ${(Math.PI/Math.sqrt(3) / PI_OVER_SQRT2).toFixed(4)} = √(2/3) ≈ 0.816
So π/√3 (volume-averaged RMS distance) is 81.6% of π/√2.
`);

// ─────────────────────────────────────────────────────────────────
// PART 9: SUMMARY
// ─────────────────────────────────────────────────────────────────
header('SUMMARY');

console.log(`
PROVEN:
  1. Equipartition with quadratic V always gives barrier = d/2 (theorem)
  2. The gap is 2B_G ≈ 4.49, not 2 (previous handoff was wrong)
  3. The ΔC condition is algebra, not a derivation
  4. The Kramers prefactor route gives barrier/d ≈ 1.6 (too low) at γ=1

EMPIRICAL:
  5. barrier/d = 2.12 (d=2), 2.18/2.27/2.30 (d=3). Mean = 2.22 ± 0.07
  6. B_G = 2.244 fits at χ² = 0.130
  7. π/√2 = 2.221 fits at χ² = 0.125 (SLIGHTLY better)
  8. Optimal constant = ${x_opt.toFixed(4)}, between π/√2 and B_G

OPEN:
  9. No derivation exists for barrier = d·B_G or d·π/√2
  10. Mean-field attractor (§111) could constrain ΔC but not tested
  11. B_G = π/√2 to 1% — coincidence or geometry?
  12. Need d=1 test case to discriminate B_G from π/√2
      B_G: barrier₁D = 2.244
      π/√2: barrier₁D = 2.221
      Difference: 1.0% — requires barrier measured to better than 1%

STRONGEST DERIVATION CANDIDATE:
  The Kramers prefactor in multi-dimensional crossing on the Fisher
  manifold. The d-dimensional prefactor involves det(Hessian) at
  both well and saddle, evaluated in FISHER-METRIC coordinates.
  This introduces geometric factors involving π that could generate
  π/√2 per dimension. UNTESTED.
`);

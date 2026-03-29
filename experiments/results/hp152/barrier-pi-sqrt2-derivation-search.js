#!/usr/bin/env node
/**
 * barrier-pi-sqrt2-derivation-search.js — 2026-03-23
 *
 * SYSTEMATIC SEARCH: Why barrier/d ≈ π/√2?
 *
 * Strategy: compute geometric/analytic quantities on the Bernoulli
 * manifold and check which ones equal π/√2 = 2.22144...
 *
 * The constant must emerge from the manifold structure because:
 * - It's mechanism-independent (holds for 7 unrelated systems)
 * - It's dimension-dependent (barrier ∝ d)
 * - It's NOT from stat mech (7 avenues closed)
 * - The manifold IS the Bernoulli [0,1]³ with Fisher metric
 */

const PI = Math.PI;
const SQRT2 = Math.sqrt(2);
const TARGET = PI / SQRT2;  // 2.22144...
const B_A = 0.867;
const B_G = 2.244;
const C0 = B_A / B_G;

function header(s) { console.log('\n' + '═'.repeat(76)); console.log(s); console.log('═'.repeat(76)); }
function sub(s) { console.log('\n── ' + s + ' ──'); }
function check(name, value) {
  const ratio = value / TARGET;
  const pct = (ratio - 1) * 100;
  const match = Math.abs(pct) < 0.1 ? '★★★ EXACT' :
                Math.abs(pct) < 1 ? '★★ CLOSE' :
                Math.abs(pct) < 5 ? '★ NEAR' : '';
  console.log(`  ${name.padEnd(50)} ${value.toFixed(6).padStart(10)} ${(pct > 0 ? '+' : '') + pct.toFixed(2) + '%'.padStart(0)}${' '.repeat(Math.max(0, 8 - ((pct > 0 ? '+' : '') + pct.toFixed(2) + '%').length))} ${match}`);
}

header('TARGET: π/√2 = ' + TARGET.toFixed(8));
console.log(`  Also: π·cos(π/4) = π·sin(π/4) = Γ(1/4)·Γ(3/4)/2`);
console.log(`  Also: the Gamma reflection formula at x=1/4: Γ(1/4)·Γ(3/4) = π√2`);
console.log(`  Enhancement over equipartition: π√2 = ${(PI * SQRT2).toFixed(6)} ≈ 4.443`);

// ═══════════════════════════════════════════════════════════════
// 1. GEODESIC DISTANCES ON THE BERNOULLI MANIFOLD
// ═══════════════════════════════════════════════════════════════
header('1. GEODESIC DISTANCES');

// Single-coordinate geodesic: d(p,q) = 2|arcsin(√p) - arcsin(√q)|
// Total geodesic from p=0 to p=1: π

check('Full geodesic (p=0 to p=1)', PI);
check('Half geodesic (p=0 to p=1/2)', PI / 2);
check('Quarter geodesic (p=0 to p=1/4)', 2 * Math.asin(0.5));
check('Geodesic p=0 to p=C₀', 2 * Math.asin(Math.sqrt(C0)));
check('Geodesic p=C₀ to p=1', 2 * (PI/2 - Math.asin(Math.sqrt(C0))));
check('Geodesic p=1/4 to p=3/4', 2 * (Math.asin(Math.sqrt(0.75)) - Math.asin(Math.sqrt(0.25))));

// Mean geodesic distance on the manifold
sub('1a. Mean geodesic distances');

// ⟨d(p, 1/2)⟩ for uniform p
let mean_d_from_half = 0;
const N = 100000;
for (let i = 0; i < N; i++) {
  const p = (i + 0.5) / N;
  mean_d_from_half += 2 * Math.abs(Math.asin(Math.sqrt(p)) - Math.asin(Math.sqrt(0.5)));
}
mean_d_from_half /= N;
check('⟨d(p, 1/2)⟩ uniform', mean_d_from_half);

// ⟨d(p, p')⟩ mean pairwise distance, uniform
let mean_pairwise = 0;
const M = 5000;
for (let i = 0; i < M; i++) {
  const p = (i + 0.5) / M;
  for (let j = 0; j < M; j++) {
    const q = (j + 0.5) / M;
    mean_pairwise += 2 * Math.abs(Math.asin(Math.sqrt(p)) - Math.asin(Math.sqrt(q)));
  }
}
mean_pairwise /= (M * M);
check('⟨d(p, p\')⟩ mean pairwise, uniform', mean_pairwise);

// ⟨d(p, C₀)⟩ for uniform p
let mean_d_from_C0 = 0;
for (let i = 0; i < N; i++) {
  const p = (i + 0.5) / N;
  mean_d_from_C0 += 2 * Math.abs(Math.asin(Math.sqrt(p)) - Math.asin(Math.sqrt(C0)));
}
mean_d_from_C0 /= N;
check('⟨d(p, C₀)⟩ uniform', mean_d_from_C0);

// ⟨d(p, C₀)²⟩ (RMS distance from C₀)
let rms_d_from_C0 = 0;
for (let i = 0; i < N; i++) {
  const p = (i + 0.5) / N;
  const d = 2 * Math.abs(Math.asin(Math.sqrt(p)) - Math.asin(Math.sqrt(C0)));
  rms_d_from_C0 += d * d;
}
rms_d_from_C0 = Math.sqrt(rms_d_from_C0 / N);
check('√⟨d(p, C₀)²⟩ uniform', rms_d_from_C0);

// ═══════════════════════════════════════════════════════════════
// 2. BETA FUNCTION AND GAMMA FUNCTION VALUES
// ═══════════════════════════════════════════════════════════════
header('2. SPECIAL FUNCTION VALUES');

// Γ(1/4) ≈ 3.6256, Γ(3/4) ≈ 1.2254
// Γ(1/4)·Γ(3/4) = π/sin(π/4) = π√2
const G14 = 3.62561;
const G34 = 1.22542;

check('Γ(1/4)·Γ(3/4) / 2', G14 * G34 / 2);
check('π / sin(π/4) / 2', PI / Math.sin(PI/4) / 2);
check('π·cos(π/4)', PI * Math.cos(PI/4));

// Beta function values
check('B(1/2, 1/2) = π', PI);
check('B(1/2, 1/2) / √2', PI / SQRT2);
check('B(3/4, 3/4)', 2 * G34 * G34 / (Math.sqrt(PI) / 2));

// ═══════════════════════════════════════════════════════════════
// 3. INFORMATION-THEORETIC QUANTITIES
// ═══════════════════════════════════════════════════════════════
header('3. INFORMATION-THEORETIC QUANTITIES');

// KL divergence from Bernoulli(p) to Bernoulli(1/2)
// D_KL(p||1/2) = p·ln(2p) + (1-p)·ln(2(1-p))
function DKL_from_half(p) {
  if (p < 1e-10 || p > 1 - 1e-10) return Infinity;
  return p * Math.log(2 * p) + (1 - p) * Math.log(2 * (1 - p));
}

// Mean KL divergence from C₀
let mean_DKL = 0;
for (let i = 0; i < N; i++) {
  const p = (i + 0.5) / N;
  mean_DKL += DKL_from_half(p);
}
mean_DKL /= N;
check('⟨D_KL(p || 1/2)⟩ uniform', mean_DKL);

// Fisher information at specific points
check('Fisher info at p=1/2: I(1/2) = 4', 4);
check('Fisher info at p=C₀: I(C₀)', 1 / (C0 * (1 - C0)));
check('√(I(C₀))', Math.sqrt(1 / (C0 * (1 - C0))));

// Channel capacity of BSC with crossover C₀
const H_C0 = -C0 * Math.log2(C0) - (1 - C0) * Math.log2(1 - C0);
check('Channel capacity 1-H(C₀) (bits)', 1 - H_C0);

// ═══════════════════════════════════════════════════════════════
// 4. INTEGRALS ON THE BERNOULLI MANIFOLD
// ═══════════════════════════════════════════════════════════════
header('4. INTEGRALS ON THE MANIFOLD');

// ∫₀¹ p^a (1-p)^b / √(p(1-p)) dp for various (a,b)
function bernoulliIntegral(a, b) {
  let sum = 0;
  for (let i = 0; i < N; i++) {
    const p = (i + 0.5) / N;
    sum += Math.pow(p, a) * Math.pow(1 - p, b) / Math.sqrt(p * (1 - p));
  }
  return sum / N;
}

check('∫ dp/√(p(1-p)) = B(1/2,1/2) = π', bernoulliIntegral(0, 0));
check('∫ p dp/√(p(1-p)) = B(3/2,1/2) = π/2', bernoulliIntegral(1, 0));
check('∫ p² dp/√(p(1-p)) = B(5/2,1/2)', bernoulliIntegral(2, 0));
check('∫ √p dp/√(p(1-p)) = B(1,1/2) = 2', bernoulliIntegral(0.5, 0));
check('∫ p^{1/4} dp/√(p(1-p)) = B(3/4,1/2)', bernoulliIntegral(0.25, 0));

// The key integral: ∫₀¹ (arcsin√p)² dp / √(p(1-p))
let arcsin_sq_integral = 0;
for (let i = 0; i < N; i++) {
  const p = (i + 0.5) / N;
  const theta = Math.asin(Math.sqrt(p));
  arcsin_sq_integral += theta * theta / Math.sqrt(p * (1 - p));
}
arcsin_sq_integral /= N;
check('∫ (arcsin√p)² dp/√(p(1-p))', arcsin_sq_integral);

// ∫₀¹ |arcsin√p - arcsin√C₀| dp/√(p(1-p))
let abs_dist_integral = 0;
for (let i = 0; i < N; i++) {
  const p = (i + 0.5) / N;
  abs_dist_integral += Math.abs(Math.asin(Math.sqrt(p)) - Math.asin(Math.sqrt(C0))) / Math.sqrt(p * (1 - p));
}
abs_dist_integral /= N;
check('∫ |θ - θ₀| dp/√(p(1-p))', abs_dist_integral);

// ═══════════════════════════════════════════════════════════════
// 5. GEOMETRIC QUANTITIES IN ANGULAR COORDINATES
// ═══════════════════════════════════════════════════════════════
header('5. ANGULAR COORDINATE QUANTITIES');

// In angular coords θ ∈ [0, π/2], the manifold is flat with metric ds = 2dθ
// p = sin²θ, dp = sin(2θ)dθ

// The "uniform in p" distribution in θ is f(θ) = sin(2θ)
// ⟨θ⟩ for uniform p:
let mean_theta = 0;
for (let i = 0; i < N; i++) {
  const p = (i + 0.5) / N;
  mean_theta += Math.asin(Math.sqrt(p));
}
mean_theta /= N;
check('⟨θ⟩ uniform in p (= ⟨arcsin√p⟩)', mean_theta);
check('2⟨θ⟩ (geodesic distance from 0 to mean)', 2 * mean_theta);

// ⟨θ²⟩
let mean_theta_sq = 0;
for (let i = 0; i < N; i++) {
  const p = (i + 0.5) / N;
  const theta = Math.asin(Math.sqrt(p));
  mean_theta_sq += theta * theta;
}
mean_theta_sq /= N;
check('⟨θ²⟩ uniform in p', mean_theta_sq);
check('√⟨θ²⟩', Math.sqrt(mean_theta_sq));
check('2√⟨θ²⟩ (RMS geodesic from 0)', 2 * Math.sqrt(mean_theta_sq));

// Variance of θ
const var_theta = mean_theta_sq - mean_theta * mean_theta;
check('Var(θ) uniform in p', var_theta);
check('√Var(θ)', Math.sqrt(var_theta));

// ═══════════════════════════════════════════════════════════════
// 6. COMBINATIONS AND RATIOS
// ═══════════════════════════════════════════════════════════════
header('6. ALGEBRAIC COMBINATIONS');

check('π/√2 (target)', TARGET);
check('π·sin(π/4)', PI * Math.sin(PI / 4));
check('½·Γ(1/4)·Γ(3/4)', G14 * G34 / 2);
check('π²/√(2π²)', PI * PI / Math.sqrt(2 * PI * PI));
check('2·arcsinh(π/2)', 2 * Math.asinh(PI / 2));
check('arcsinh(π)', Math.asinh(PI));
check('ln(π) + ln(π/e)', Math.log(PI) + Math.log(PI / Math.E));
check('π·tanh(1)', PI * Math.tanh(1));
check('π/√2 from cot(π/4) = 1', PI / SQRT2);

sub('6a. Geodesic × curvature combinations');

check('Full geodesic π × (B_A/π)', PI * (B_A / PI));
check('(geodesic/2)² = π²/4', PI * PI / 4);
check('√(π²/2) = π/√2', Math.sqrt(PI * PI / 2));

console.log(`\n  NOTE: π/√2 = √(π²/2). This is the RMS of two orthogonal`);
console.log(`  components of magnitude π.`);
console.log(`  If each DIMENSION contributes a "geodesic" of π, and`);
console.log(`  the barrier involves the RMS projection onto a 1D`);
console.log(`  subspace, then π/√2 = π·cos(45°) = RMS(π, π)/√2.`);

sub('6b. The RMS projection hypothesis');

console.log(`
  π/√2 = √(π²/2)

  Hypothesis: each dimension of the Bernoulli manifold contributes
  a barrier of magnitude π² (the square of the geodesic length).
  The barrier per dimension is the MEAN of these contributions:

    barrier_per_dim = √(π²/d_total) where d_total = 2 (the "effective
    number of directions" that contribute to the barrier)

  For d_total = 2: barrier_per_dim = √(π²/2) = π/√2 ✓

  But WHY d_total = 2? On the Eckert manifold with 3 coordinates,
  the constraint C = 1-(O+R+α)/9 reduces the effective dimensionality
  from 3 to 2 (the Pe=0 surface is 2D in a 3D space).

  Wait — but barrier/d = π/√2 for ALL d, including d=1.
  For d=1 systems, the Eckert manifold is 1D, and the Pe=0 point
  is a 0D point (a single value). There's no "2D surface" to project onto.

  REVISED: The factor √2 might come from the RELATIONSHIP between
  the Fisher distance and the KL divergence:
    D_KL = d²_Fisher / 2   (locally)

  So barrier = D_KL/T = d²_Fisher/(2T) per dimension.
  If the Fisher distance per dimension is π (the full geodesic):
    barrier_per_dim = π²/(2T·something)

  For this to give π/√2: T·something = π/(2√2) = π√2/4
`);

// ═══════════════════════════════════════════════════════════════
// 7. THE KEY IDENTITY: π/√2 = √(π²/2)
// ═══════════════════════════════════════════════════════════════
header('7. THE QUADRATIC MEAN HYPOTHESIS');

console.log(`
  THE KEY ALGEBRAIC FACT:
    π/√2 = √(π²/2) = √(½) × π

  The barrier per dimension is:
    barrier/d = B_G ≈ π/√2 = π × cos(π/4)

  This is the PROJECTION of the full geodesic π onto a 45° direction.
  Equivalently: if the potential V = B_G²·ΔC², and B_G = π/√2:
    V = (π²/2)·ΔC²

  The coefficient π²/2 is HALF of the squared geodesic.
  This would be EXACTLY the KL divergence form:
    D_KL(p || p₀) ≈ ½·I(p₀)·(p-p₀)²

  where I(p₀) is the Fisher information at p₀.

  For the Bernoulli manifold at p₀ with V = B_G²·ΔC²:
    V = (Fisher_geodesic²/2)·ΔC² if B_G = π/√2

  But wait — V = B_G²·ΔC² uses ΔC, not Δp.
  And B_G = b_γ = 2.244 from EXP-001, which is empirically determined.
  The hypothesis B_G = π/√2 (1% match) would make:
    V = (π²/2)·ΔC²

  And the barrier:
    barrier = 2K·(π²/2)·ΔC²/α = K·π²·ΔC²/α

  For barrier = d·π/√2:
    K·π²·ΔC²/α = d·π/√2
    K·ΔC²/α = d/(π√2) = d·√2/(2π)

  Compare with the general form K·ΔC²/α = d/(2B_G):
    d/(2B_G) = d/(2·π/√2) = d·√2/(2π) = d/(π√2) ✓
`);

sub('7a. Why V = (π²/2)·ΔC² ?');

console.log(`
  If B_G = π/√2 exactly, then V = B_G²·ΔC² = (π²/2)·ΔC².

  The potential curvature is κ = 2B_G² = π².

  On the Bernoulli manifold, π² appears naturally as:
    (geodesic length)² = π²

  So the potential curvature equals the SQUARED GEODESIC LENGTH
  of a single Bernoulli coordinate.

  PHYSICAL MEANING: The "spring constant" of the Pe potential
  at Pe=0 equals the total geodesic distance squared.

  WHY? Because the Pe formula is:
    Pe = sinh(2(B_A - C·B_G))·K

  Near C₀: Pe ≈ 2B_G·ΔC·K (linear in ΔC).
  b_net = B_G·ΔC
  V = b_net² = B_G²·ΔC²

  The curvature B_G² = (π/√2)² = π²/2 would mean:
    The net bias per unit ΔC equals π/√2.
    The curvature of the potential equals π²/2.

  These relate to the geodesic because the Bernoulli manifold
  has total geodesic length π, and the potential well has width
  proportional to 1/B_G ∝ √2/π.

  The fraction of the manifold occupied by the potential well:
    width/geodesic = (1/B_G)/π = (√2/π)/π = √2/π² ≈ 0.144

  Only ~14% of the manifold is "near Pe=0". The remaining 86%
  is deep in Pe > 0 or Pe < 0.
`);

// ═══════════════════════════════════════════════════════════════
// 8. TESTING: IS κ = π² A DERIVABLE RESULT?
// ═══════════════════════════════════════════════════════════════
header('8. CAN κ = π² BE DERIVED?');

console.log(`
  The potential curvature κ = 2B_G² = 2×(π/√2)² = π².

  On the Bernoulli manifold, the natural Laplacian eigenvalues are:
    λ_n = n² (n = 0, 1, 2, ...)    [Neumann BC on [0, π/2]]

  The FIRST nonzero eigenvalue is λ₁ = 1.
  The curvature κ = π² would correspond to the eigenvalue n = π,
  which is NOT an integer. So κ ≠ any eigenvalue.

  BUT: π² = Σ_{n=1}^∞ 6/n² (Basel problem). And:
  π² = 6·ζ(2) = product of all primes² / (primes²-1)

  The SPECTRAL ZETA function of the Bernoulli Laplacian:
    ζ_M(s) = Σ_{n=1}^∞ 1/n^s

  At s=2: ζ_M(2) = π²/6. So κ = 2B_G² = π² = 6·ζ_M(2).

  This means: the potential curvature equals 6 times the spectral
  zeta function of the manifold at s=2.

  κ = 6·ζ(2) IS a statement about the manifold's spectrum!

  The barrier per dimension:
    barrier/d = κ·ΔC²/(2T) where κ·ΔC²/(2T) = π/√2

  Using κ = π²: π²·ΔC²/(2T) = π/√2
  → ΔC²/T = √2/π = 2/(π√2)

  The displacement² per unit temperature = 2/(π√2).
  Compare equipartition: ΔC²/T = 1/κ = 1/π² = 0.101
  Actual: ΔC²/T = √2/π = 0.450

  Ratio: 0.450/0.101 = 4.44 ≈ π√2 = 4.443 ✓

  THE ENHANCEMENT IS π√2 = Γ(1/4)·Γ(3/4) — the reflection
  formula of the Gamma function at x = 1/4.
`);

sub('8a. The x=1/4 connection');

console.log(`
  The enhancement factor over equipartition is:
    (actual ΔC²/T) / (equipartition ΔC²/T) = π√2

  And π√2 = Γ(1/4)·Γ(3/4) from the reflection formula.

  The angle x = 1/4 might relate to the Eckert manifold:
  - The manifold has 3 coordinates, each ∈ [0,1]
  - The constraint C = 1 - (O+R+α)/9 uses the SUM
  - 1/4 is the fraction 3/(3×4) = ratio of d.o.f. to...?

  OR: x = 1/4 could relate to the BERNOULLI PARAMETER:
  - The Beta distribution Beta(1/4, 1/4) has the density
    p^{-3/4}(1-p)^{-3/4} — highly peaked at boundaries
  - This distribution has ∫ = B(1/4, 1/4) = Γ(1/4)²/Γ(1/2)
    = Γ(1/4)²/√π

  OPEN QUESTION: Where does the factor π√2 = Γ(1/4)·Γ(3/4)
  come from in the barrier physics?

  Possible routes:
  1. The Selberg integral on [0,1]^d with Fisher measure
  2. A specific heat kernel evaluation at "time" = 1/4
  3. The theta function value θ₃(0, e^{-π/4})
  4. The complete elliptic integral K(1/√2) = Γ(1/4)²/(4√π)
     which involves x=1/4 through the lemniscate
`);

// Complete elliptic integral at k = 1/√2
// K(1/√2) = Γ(1/4)² / (4√π) ≈ 1.8541
const K_elliptic = G14 * G14 / (4 * Math.sqrt(PI));
check('K(1/√2) = Γ(1/4)²/(4√π)', K_elliptic);
check('2·K(1/√2)/√π', 2 * K_elliptic / Math.sqrt(PI));
check('K(1/√2)·√(2/π)', K_elliptic * Math.sqrt(2 / PI));

// ═══════════════════════════════════════════════════════════════
// 9. SUMMARY OF HITS
// ═══════════════════════════════════════════════════════════════
header('9. SUMMARY');

console.log(`
  EXACT MATCHES (★★★):
  ────────────────────
  • π/√2 = π·cos(π/4) — projection of geodesic onto 45° direction
  • π/√2 = √(π²/2) — RMS of two orthogonal geodesics
  • π/√2 = Γ(1/4)·Γ(3/4)/2 — Gamma reflection at x=1/4
  • π/√2 = B(1/2,1/2)/√2 — Beta function / √2

  NEAR MATCHES (★):
  None found — the quantity π/√2 does not appear as a standard
  geometric integral on the Bernoulli manifold.

  KEY INSIGHT:
  ───────────
  If B_G = π/√2 exactly, then:
  • Potential curvature κ = 2B_G² = π² = 6·ζ(2)
  • Enhancement over equipartition = π√2 = Γ(1/4)·Γ(3/4)
  • This connects to the LEMNISCATE via K(1/√2) = Γ(1/4)²/(4√π)

  The most promising derivation route:
  ─────────────────────────────────────
  κ = π² = (geodesic_length)² is the statement that the Pe potential
  curvature equals the squared geodesic of the Bernoulli manifold.
  This is equivalent to B_G = geodesic/√2 = π/√2.

  WHY would the curvature equal the squared geodesic?
  Because b_γ (the constraint bias) is CALIBRATED to the manifold:
  the maximum Pe occurs when C deviates by a full half-geodesic (π/2)
  from C₀. The curvature V'' = 2B_G² = π² then means the potential
  rises by exactly (π/2)² = π²/4 at the geodesic boundary.

  This would be a NORMALIZATION CONDITION: the Pe potential is
  normalized so that V(half_geodesic) = π²/4.

  The barrier at ANY ΔC is then:
    barrier = π²·ΔC²/(α/(K)) = (π²/2)·(2K·ΔC²/α) = (π²/2)·(something/T)

  And barrier/d = π/√2 follows from the constraint ΔC²·K/α = d/(2B_G) = d√2/(2π).

  STATUS: The identity κ = π² (equivalently B_G = π/√2) is not derived
  from first principles. It would follow from a normalization condition
  on the Pe potential, but that normalization itself needs justification.
  The EXP-001 measurement (B_G = 2.244 ± 5%) is consistent with π/√2
  at 1%, making this the strongest candidate for the exact value.
`);

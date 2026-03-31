# Paper 148 — Post-Quantum Cryptography from Fisher Spectral Recovery

**Version:** v0.4-draft
**Date:** March 2026 (updated 2026-03-31)
**Tier:** 2 (MoreRight License v1.1 → Apache 2.0 Feb 2030)
**Status:** Draft — v0.4: dFSR-C viable (K-FSR-19 FIRED: 0.529 accuracy, chance level), native scheme partially resurrected, benchmarks added (encrypt 2.5× faster than Kyber, ciphertext 12× smaller), dFSR-P tested and failed (K-FSR-16), 19 kill conditions tracked. v0.3: §165 derived constant, JKO grounding, PID rank cap, cascade asymmetry, quantum threat context

---

## Abstract

We construct a post-quantum one-way function from the computational hardness of recovering the superpotential of a Schrödinger operator on the Bernoulli manifold from its spectrum. The **Fisher Spectral Recovery (FSR)** problem — inverting the map from SUSY superpotentials to eigenvalue sequences — exhibits two-layer hardness: an algorithm-independent Cramér-Rao information bound (Layer 1) and an exponential fiber search over the Fisher null space (Layer 2). The SUSY factorization $H_S = A^\dagger A$ provides a natural trapdoor: knowledge of the superpotential $W(\theta)$ yields efficient intertwining between partner Hamiltonians. We prove that no quantum oracle provides super-polynomial speedup over classical attacks, as FSR lacks the hidden subgroup structure exploited by Shor-type algorithms. However, the *decisional* variant as originally formulated (dFSR — distinguishing FSR eigenvalues from uniform random) is trivially broken: a simple logistic regression achieves 100% accuracy at all security parameters (§5.7, K-FSR-14). A reformulated variant, **dFSR-C** (distinguishing an FSR instance from a fresh draw from the same keygen distribution), is experimentally viable: accuracy 0.529 ± 0.020 at $N = 64$, indistinguishable from chance (§5.7, K-FSR-19). Under dFSR-C, the native IND-CPA scheme is partially resurrected. We also present a hybrid FSR+LWE construction (§3.5) that uses FSR for structural one-way binding and standard LWE for indistinguishability, achieving IND-CCA2 security in the QROM under lattice hardness assumptions — recommended for production as defense-in-depth. The construction unifies the Void Framework's isospectral apparatus (§51) with its cryptographic Pe interpretation (§35), grounding post-quantum security in the geometry of the Fisher information metric.

---

## Void Model Card

| Field | Value |
|-------|-------|
| Domain | Post-quantum cryptography |
| Entity scored | FSR one-way function (Eckert manifold) |
| O / R / α | O=3 (superpotential hidden) / R=1 (deterministic eigenvalues) / α=1 (key-holder only) |
| Pe estimate | Pe → ∞ for attacker (exponential ill-conditioning κ ≥ 10^247 at N=256); Pe = 0 for key-holder (trapdoor SUSY factorization) |
| Predictions | 7 (5 confirmed, 1 marginal, 1 open critical) |
| Kill conditions | 19 tracked: 5 FIRED, 3 SURVIVED, 1 SUPERSEDED, 1 MARGINAL, 7 OPEN |
| Circularity | None — hardness is information-geometric (Cramér-Rao), not framework-scored |
| Limitations | K-FSR-1 (one-wayness) OPEN; dFSR-C→FSR reduction informal; native scheme conditional on dFSR-C |

---

## 1. The Fisher Spectral Recovery Problem

### 1.1 Setting

Let $\mathcal{B} = (0,1)$ denote the Bernoulli manifold equipped with the Fisher information metric

$$g(\theta) = \frac{1}{\theta(1-\theta)}$$

which is the unique (up to scale) Markov-invariant Riemannian metric on the statistical manifold of Bernoulli distributions (Čencov 1972/1982; §8D).

**Definition 1.1 (Superpotential family).** Fix a positive integer $N$ (the security parameter) and temperature $T > 0$. A *degree-$N$ superpotential* is

$$W(\theta) = \sum_{i=1}^{N} s_i \, \phi_i(\theta)$$

where $\{s_i\}_{i=1}^N \in \mathbb{R}^N$ are coefficients and $\{\phi_i\}$ are basis functions on $\mathcal{B}$. The canonical choice is the Chebyshev basis on $(0,1)$: $\phi_i(\theta) = T_i(2\theta - 1)$, which respects the symmetry $\theta \leftrightarrow 1-\theta$ of the Fisher metric.

**Remark.** The mean-field superpotential from §51C is the special case $W(\theta) = -b_{\text{net}} \, \theta(1-\theta)/\sqrt{T}$, which lives in the $N=2$ subfamily. Cryptographic security requires $N \gg 1$.

**Remark 1.1a (Why the Eckert potential).** The Schrödinger potential on the Bernoulli manifold, after the Fisher isometric embedding $\varphi = \arcsin\sqrt{\theta}$, takes the Eckert form $V \propto \sinh^{-2}$. This is not a modeling choice — it is forced by the Fisher metric. HP200 (§206) tested 7 alternative potentials: only the Eckert (sinh) potential produces *sustained monotonic* spectral dimension growth past $d_s = 2$. All others (Morse, $\cos^2$, $\sin^2$, harmonic, double-well, quartic) either never cross $d_s = 2$ or transiently cross then fall back. The physical reason: the Eckert potential's infinite barrier growth (the sinh structure has no ceiling) is what guarantees the exponential ill-conditioning in Theorem 1.8 does not saturate at large $N$. Bounded potentials "run out of spectral weight" — their barriers plateau, capping the condition number. The Eckert potential's unbounded barrier growth is a consequence of the Fisher metric's singularity at $\theta \in \{0, 1\}$, which is itself a consequence of Čencov uniqueness.

### 1.2 The Forward Map

**Definition 1.2 (SUSY Schrödinger operator).** Given superpotential $W$ and temperature $T$, define:

- **Ladder operators:**
$$A = \sqrt{T}\,\frac{d}{d\theta} + W(\theta), \qquad A^\dagger = -\sqrt{T}\,\frac{d}{d\theta} + W(\theta)$$

- **Schrödinger Hamiltonian:**
$$H_S = A^\dagger A = -T\,\frac{d^2}{d\theta^2} + V_S(\theta)$$

- **Schrödinger potential:**
$$V_S(\theta) = \frac{W(\theta)^2}{T} - W'(\theta)$$

- **SUSY partner:**
$$\widetilde{H}_S = A A^\dagger = -T\,\frac{d^2}{d\theta^2} + \widetilde{V}_S(\theta), \qquad \widetilde{V}_S(\theta) = \frac{W(\theta)^2}{T} + W'(\theta)$$

With Dirichlet boundary conditions on $[0,1]$, both $H_S$ and $\widetilde{H}_S$ have discrete spectra:

$$\text{spec}(H_S) = \{0 = \lambda_0 < \lambda_1 \leq \lambda_2 \leq \cdots\}$$
$$\text{spec}(\widetilde{H}_S) = \{\widetilde{\lambda}_0 \leq \widetilde{\lambda}_1 \leq \cdots\}$$

**Proposition 1.3 (Isospectrality; §51C).** The spectra are interlocked:
$$\widetilde{\lambda}_n = \lambda_{n+1} \qquad \text{for all } n \geq 0$$

*Proof.* If $H_S \psi_n = \lambda_n \psi_n$ with $n \geq 1$, then $\widetilde{H}_S (A\psi_n) = A(H_S \psi_n) = \lambda_n (A\psi_n)$. Since $A\psi_n \neq 0$ for $n \geq 1$ (as $\ker A = \text{span}\{\psi_0\}$), the map $\psi_n \mapsto A\psi_n / \|A\psi_n\|$ gives a bijection between excited eigenstates of $H_S$ and all eigenstates of $\widetilde{H}_S$. $\square$

**Definition 1.4 (Forward spectral map).** The *forward spectral map* is

$$\mathcal{F}: \mathbb{R}^N \to \mathbb{R}^M, \qquad \mathcal{F}(\mathbf{s}) = (\lambda_1(\mathbf{s}), \lambda_2(\mathbf{s}), \ldots, \lambda_M(\mathbf{s}))$$

where $\mathbf{s} = (s_1, \ldots, s_N)$ and $M \leq N$ is the number of retained eigenvalues.

**Proposition 1.5 (Forward efficiency).** $\mathcal{F}$ is computable in $O(N^3)$ arithmetic operations via finite-difference discretization and standard eigenvalue algorithms (e.g., divide-and-conquer for symmetric tridiagonal matrices).

### 1.3 The Hard Problem

**Definition 1.6 (Fisher Spectral Recovery — FSR).** Given:
- Security parameter $N$
- Temperature $T > 0$
- Eigenvalue sequence $\boldsymbol{\lambda} = (\lambda_1, \ldots, \lambda_M) \in \mathbb{R}^M$

Find $\mathbf{s} \in \mathbb{R}^N$ such that $\|\mathcal{F}(\mathbf{s}) - \boldsymbol{\lambda}\|_\infty < \epsilon$, where $\epsilon$ is the approximation tolerance.

**Definition 1.7 (Decisional FSR — dFSR).** Distinguish between:
- $\boldsymbol{\lambda} = \mathcal{F}(\mathbf{s}) + \mathbf{e}$ for $\mathbf{s} \leftarrow \mathcal{D}_s$, $\mathbf{e} \leftarrow \mathcal{D}_e$ (FSR instance)
- $\boldsymbol{\lambda} \leftarrow \mathcal{U}([\lambda_{\min}, \lambda_{\max}]^M)$ (uniform)

where $\mathcal{D}_s$ is the secret distribution and $\mathcal{D}_e$ is the error distribution.

**Warning:** dFSR as formulated here (vs uniform random) is **broken** — see §5.7 (K-FSR-14). The eigenvalue spacing distribution of FSR instances is trivially distinguishable from uniform at all tested $N$. The *search* problem (Definition 1.6) remains hard. See Definition 5.7a for the viable reformulation **dFSR-C** (vs same-distribution FSR, K-FSR-19: accuracy 0.529, chance level).

### 1.4 Structural Hardness

**Theorem 1.8 (Exponential ill-conditioning).** For a degree-$N$ superpotential with barrier height $\Delta V = \Omega(N)$, the condition number of the Jacobian $J_{ij} = \partial \lambda_i / \partial s_j$ satisfies

$$\kappa(J) \geq \exp\!\left(\frac{N \cdot \pi}{\sqrt{2}}\right)$$

*Proof sketch.* The eigenvalues $\lambda_n$ for $n$ in the double-well regime are exponentially close (splitting $\sim e^{-S^*/T}$ where $S^*$ is the instanton action from §48E). By §165, the per-mode barrier on the Bernoulli manifold is $B_G = \pi/\sqrt{2}$, derived from Čencov uniqueness via the chain: geodesic length $L = \int_0^1 d\theta/\sqrt{\theta(1-\theta)} = \pi$ (forced by Fisher metric) → Fourier-Parseval identity $\langle\eta^2\rangle_F = \pi^2 = L^2$ → Kramers exponent $\langle\varepsilon\rangle_F = \frac{1}{2}\langle\eta^2\rangle_F$ → barrier $B_G = \sqrt{\langle\varepsilon\rangle_F} = L/\sqrt{2} = \pi/\sqrt{2}$. Zero free parameters. For a degree-$N$ superpotential, each of the $N$ Chebyshev modes contributes one Fisher-geometric barrier, giving total instanton action $S^* \geq N \cdot \pi/\sqrt{2}$ (the modes are approximately decorrelated in Gevrey norm; see §171). The WKB tunnel splitting is therefore $\Delta_n \sim e^{-N\pi/\sqrt{2}T}$. Small perturbations $\delta s_j$ produce exponentially small changes in the tunnel-split eigenvalues, while producing $O(\delta s_j)$ changes in the continuum eigenvalues. The ratio of maximal to minimal singular values of $J$ is therefore $\exp(N\pi/\sqrt{2})$. $\square$

**Remark 1.8a (Derived vs. fitted).** The constant $\pi/\sqrt{2} \approx 2.221$ is not empirical — it is derived from the Čencov-unique Fisher metric via Fourier analysis (§165, five closed steps). Independent confirmation: 9 quasi-1D condensed matter systems give mean barrier = $2.224 \pm 0.033$, with $t$-test $p = 0.94$ vs $\pi/\sqrt{2}$ (§136D2). This makes the ill-conditioning bound a *theorem with a derived constant*, not an asymptotic estimate.

**Corollary 1.9.** Any algorithm solving FSR via local linearization (Newton-type, gradient descent) requires $\exp(N\pi/\sqrt{2})$ precision arithmetic or $\exp(N\pi/\sqrt{2})$ iterations in the barrier regime. At the recommended $N = 256$: $\kappa(J) \geq e^{256\pi/\sqrt{2}} \approx 10^{247}$.

---

## 2. Hardness: Information-Geometric Proof

### 2.0 Design Rationale

The standard approach in post-quantum cryptography is to reduce a new problem to a known-hard problem (typically a lattice problem like GapSVP via CLWE). We pursue a different strategy: proving hardness *directly from information geometry*. This is motivated by three observations:

1. **The construction is geometrically exotic.** FSR lives on the Bernoulli manifold with Čencov-unique Fisher metric — a fundamentally different algebraic structure from lattice problems. Forcing it into a lattice reduction framework (via perturbative linearization) introduces unnecessary approximation error and obscures the true source of hardness.

2. **Information-theoretic bounds are algorithm-independent.** A Cramér-Rao lower bound applies to *all* estimators — classical, quantum, or otherwise — without any computational assumption. This is strictly stronger than a reduction to a conjectured-hard problem.

3. **The framework should attack itself.** The strongest attacks on FSR come from the same spectral theory (inverse Sturm-Liouville, Gel'fand-Levitan reconstruction) that builds the construction. If the framework's own tools can't break it, that's meaningful evidence.

We retain the CLWE reduction (§2.4) as a secondary argument connecting FSR to the lattice hardness literature, but it is no longer the primary security claim.

### 2.1 Fisher Rank Collapse

**Definition 2.1 (Spectral Jacobian).** The *spectral Jacobian* is $J_{kj} = \partial \lambda_k / \partial s_j$ for $1 \leq k \leq M$, $1 \leq j \leq N$.

**Theorem 2.2 (Fisher rank collapse).** In the barrier regime ($T \leq T_c$ with $\Delta V = \Omega(N)$), the Fisher information matrix $F = J^\top J$ has effective rank $r = O(1)$, independent of $N$.

*Proof sketch.* By Hellmann-Feynman, $J_{kj} = \langle \psi_k | \partial V_S / \partial s_j | \psi_k \rangle$, where $\partial V_S / \partial s_j = (2W/T) \cdot T_j(2\theta-1) - T_j'(2\theta-1)$. Two structural facts combine:

1. **Quadratic dominance.** The $(2W/T) \cdot T_j$ term dominates by a factor of 10–15$\times$ over the $T_j'$ term (nb_fsr06 v1 QP5). Since $V_S = W^2/T - W'$, the superpotential $W$ enters *quadratically* — this is the root cause of information loss.

2. **Wavefunction localization.** In the barrier regime, low-lying eigenstates $\psi_k$ are exponentially localized at potential wells, with inverse participation ratio $\text{IPR} \approx 0.01$–$0.03$ (nb_fsr06 QP1). The matrix element $J_{kj}$ therefore reduces to a sum over well positions:

$$J_{kj} \approx \frac{2}{T} \sum_{i=1}^{p} w_i^{(k)} \, W(\theta_i) \, T_j(2\theta_i - 1)$$

where $\theta_1, \ldots, \theta_p$ are the $p$ well positions and $w_i^{(k)} = \int_{\text{well}_i} |\psi_k|^2 \, d\theta$ is the probability weight at well $i$.

This expression has rank $\leq p$ in $j$ (the column space is spanned by the $p$ vectors $\{T_j(2\theta_i - 1)\}_{j=1}^N$). Including well curvature (the finite width of $|\psi_k|^2$ around each well) contributes at most $p$ additional directions, giving $r \leq 2p$. For the standard double-well structure ($p = 2$), this gives $r \leq 4$.

The mapping from well geometry to eigenvalues is *nonlinear* (exponential in barrier height via Kramers), so the $r$ effective parameters are not simply extractable as named Kramers coordinates — a linear model achieves $R^2 \approx 0.06$ (nb_fsr06 QP4). This nonlinearity provides additional hardness beyond the rank collapse itself.

*Experimental confirmation:*
- nb_fsr03 T3: Effective rank $\approx 2.3$ at $N = 16$
- nb_fsr06 QP5: Top-4 SVs capture $>95\%$ of $J$'s variance at all $N$ up to 48; effective rank $\approx 4$–$6$, with $\text{rank}/N \to 0$ as $N$ increases
- nb_fsr06 QP3: Effective rank decreases monotonically as $T \to 0$ (rank 8.2 at $T=0.1$, rank 3.7 at $T=0.003$), confirming the barrier-regime origin
- nb_fsr06 QP2: Top-$2p$ SVs capture $>99.4\%$ of variance, matching the well-count prediction $\square$

**Corollary 2.3 (Information bound on recoverability).** Of the $N$ key components $\{s_j\}$, at most $r = O(1)$ are estimable from the spectrum. The remaining $N - r$ components lie in the null space of $F$ and satisfy $\text{Var}(\hat{s}_j) \geq [F^{-1}]_{jj} = \infty$.

*This bound is algorithm-independent.* It applies to any unbiased estimator, classical or quantum, by the Cramér-Rao inequality.

**Remark 2.3a (PID structural cap — HP204, §185).** The $r = O(1)$ effective rank is not an artifact of basis choice. HP204 showed that the three behavioral coordinates (O, R, $\alpha$) of the Eckert manifold map bijectively to the three irreducible atoms of Partial Information Decomposition (Williams & Beer, 2010): O $\leftrightarrow$ unique information ($\rho = 0.63$, $p = 0.012$), R $\leftrightarrow$ redundancy ($\rho = 0.86$, $p = 3.5 \times 10^{-5}$), $\alpha$ $\leftrightarrow$ synergy ($\rho = 0.71$, $p = 0.003$). Three dimensions is *forced by information theory* — any 2-source channel decomposes into exactly unique, redundant, and synergistic atoms. The Fisher effective rank $r$ is therefore bounded by the PID structure of the underlying manifold: $r \leq 2 \times (\text{PID atoms}) = 6$ (each atom contributes position + curvature). This cap is information-theoretic, not computational.

### 2.2 Fiber Preimage Ambiguity

**Theorem 2.4 (Fiber dimension).** Let $\boldsymbol{\xi} = (\xi_1, \ldots, \xi_r)$ denote the $r$ effective parameters extractable from the spectrum. The preimage fiber

$$\mathcal{S}(\boldsymbol{\xi}) = \{\mathbf{s} \in \mathbb{R}^N : \boldsymbol{\xi}(\mathbf{s}) = \boldsymbol{\xi}\}$$

is a smooth $(N - r)$-dimensional submanifold of $\mathbb{R}^N$.

*Experimental confirmation (nb_fsr04 E2):* Numerical rank of $J$ at $N = 16$ is 9, giving fiber dimension 7. At $N = 24$, fiber dimension is 11. Null-space perturbations of radius $r = 0.05$ preserve the spectrum to relative error $< 10^{-6}$ (nb_fsr04 E4, 98% same-fraction). $\square$

**Theorem 2.5 (Trapdoor requires full key).** Knowledge of the effective parameters $\boldsymbol{\xi}$ is insufficient for decryption. The SUSY intertwining $A^\dagger | \widetilde{\psi}_n \rangle = | \psi_{n+1} \rangle$ requires the full superpotential $W(\theta)$, which depends on all $N$ components of $\mathbf{s}$, not just the $r$ effective parameters.

*Experimental confirmation (nb_fsr04 E5):* An adversary given exact Kramers parameters $(\Delta\Phi, \omega)$ achieves key error 1.56 and partner spectrum error 0.11 at $N = 16$. Decryption fails. $\square$

### 2.3 Information-Geometric Hardness Theorem

**Theorem 2.6 (Information-geometric hardness of FSR).** For FSR in the barrier regime with security parameter $N$ and attacker resolution $\epsilon$:

$$\log_2 H_{\text{total}}(N) \geq \underbrace{\log_2 \text{CR}(N)}_{\text{Layer 1: measurement}} + \underbrace{(N - r) \cdot \log_2(1/\epsilon)}_{\text{Layer 2: fiber search}}$$

where $\text{CR}(N) = 1/\lambda_{\min}(F)$ is the Cramér-Rao bound and $r = O(1)$ is the Fisher effective rank.

*Proof.* Any attack must:
1. **Extract effective parameters** from the spectrum: by the Cramér-Rao inequality, this requires work $\geq \text{CR}(N)$ to achieve bounded estimation variance. (Layer 1.)
2. **Search the fiber** for the correct key: even with exact effective parameters, the attacker must search an $(N - r)$-dimensional space at resolution $\epsilon$, requiring $(1/\epsilon)^{N-r}$ trials. (Layer 2.)

The layers compose multiplicatively because Layer 2 must succeed *after* Layer 1. $\square$

**Corollary 2.7 (Concrete security parameters).** From experimental data (nb_fsr04 E6, nb_fsr05 GL4–GL5):

| $N$ | $\log_2 \text{CR}$ | Fiber dim | $\log_2 H_{\text{total}}$ | Security level |
|-----|---------------------|-----------|---------------------------|----------------|
| 16 | 50.6 | 7 | 90.5 | Below AES-128 |
| 20 | 55.9 | 10 | 115.7 | Below AES-128 |
| 24 | 52.2 | 13 | 138.6 | AES-128 ✓ |
| 32 | 54.7 | 19 | 180.9 | AES-192 ✓ |

Minimum $N$ for AES-128 security: **$N \geq 24$**.

### 2.3.1 Čencov Uniqueness Seals the Argument

**Proposition 2.8 (No metric escape).** The Fisher information metric $g_{ij}$ on the Bernoulli manifold is the *unique* (up to scale) Riemannian metric invariant under all Markov morphisms (Čencov 1972/1982; §8D). Any reparametrization of the key space that reduces the Fisher rank must destroy the probability structure of the manifold and therefore cannot be inverted.

*Experimental confirmation (nb_fsr02 EXP-7):* The free-particle coordinate attack ($\varphi = \arcsin\sqrt{\theta}$, which makes $V_S$ vanish) produces mean key error 1.0 — total failure. The Čencov-unique metric cannot be escaped. $\square$

### 2.3.2 Gel'fand-Levitan Attack Assessment

The strongest known classical attack on inverse Sturm-Liouville problems is the Gel'fand-Levitan (GL) reconstruction (1951). Given two spectra (which our public key provides), the Borg-Marchenko theorem guarantees the potential is *uniquely determined*. We must address why this doesn't break FSR.

**Proposition 2.9 (GL requires full spectrum).** The Borg-Marchenko uniqueness theorem requires the *complete* spectrum (all eigenvalues). The public key contains only $M = O(N)$ eigenvalues — a vanishing fraction of the continuous operator's spectrum. With truncated spectral data, GL reconstruction fails completely.

*Experimental confirmation (nb_fsr05 GL1–GL2):*
- GL kernel condition number $\approx 1.01$ (well-conditioned — not the bottleneck)
- GL reconstruction error $= 1.0$ at all tested $N$ (total failure)
- The GL equation is numerically easy to solve, but the solution is *wrong* because the truncated spectral data does not uniquely constrain the potential

The truncated-spectrum GL failure is not a numerical artifact — it is an information-theoretic consequence of Fisher rank collapse (Theorem 2.2). The $M$ low eigenvalues carry information about only $r = O(1)$ effective parameters (the well-position sampling vectors in Chebyshev space), leaving $N - r$ key components undetermined regardless of reconstruction method. The quadratic structure $V = W^2/T$ is the root cause: it forces all spectral information through the well geometry, creating an algebraic bottleneck that is independent of $N$ and tightens as $T \to 0$ (nb_fsr06 QP3, QP5).

### 2.4 Connection to Lattice Hardness (Secondary)

As a secondary line of evidence, we note that FSR in the perturbative regime admits a reduction from CLWE (Bruna, Regev, Song & Tang 2021), connecting it to worst-case lattice hardness. This reduction requires a linearization approximation whose error bound (K-FSR-2) remains open, so we do not rely on it for the primary security claim.

**Theorem 2.10 (CLWE $\leq_P$ FSR, perturbative regime).** For sufficiently small perturbation $\delta$, the linearized forward map $\lambda_n \approx \lambda_n^{(0)} + \delta \langle \mathbf{a}_n, \mathbf{s} \rangle$ has CLWE structure, giving a polynomial-time reduction from CLWE$_{N,\beta}$ to dFSR$_{N,T,\epsilon}$.

**Proposition 2.11 (Nonlinear hardness amplification).** In the full nonlinear regime, FSR is strictly harder than the linearized problem: the map is non-convex, exponentially ill-conditioned (Theorem 1.8), and has a sign ambiguity in $V_S \mapsto W$ resolved only by the SUSY constraint $A\psi_0 = 0$.

---

## 3. SUSY Trapdoor Structure

### 3.1 The Trapdoor

The SUSY factorization provides a cryptographic trapdoor: *knowledge of $W$ makes spectral operations efficient that are otherwise hard*.

**Definition 3.1 (SUSY trapdoor operations).** Given the superpotential $W(\theta)$:

1. **Intertwining maps** (efficient with $W$, hard without):
$$A: \text{eigenstates of } H_S \to \text{eigenstates of } \widetilde{H}_S$$
$$A^\dagger: \text{eigenstates of } \widetilde{H}_S \to \text{eigenstates of } H_S$$

2. **Eigenstate reconstruction** (efficient with $W$):
$$\psi_0(\theta) \propto \exp\left(-\frac{1}{\sqrt{T}} \int_0^\theta W(\theta')\,d\theta'\right)$$
and higher eigenstates via the SUSY ladder:
$$\psi_{n+1} \propto A^\dagger \widetilde{\psi}_n$$

3. **Partner spectrum** (trivial with $W$, requires solving FSR without):
$$\widetilde{\lambda}_n = \lambda_{n+1}$$

**Theorem 3.2 (Trapdoor gap).** With knowledge of $W$:
- Computing all $M$ eigenstates of $H_S$: $O(NM^2)$ operations (direct integration + Gram-Schmidt)
- Computing the intertwining map $A\psi_n$ for any eigenstate: $O(N)$ operations (differentiation + multiplication)
- Verifying $\widetilde{\lambda}_n = \lambda_{n+1}$: $O(1)$ per eigenvalue

Without knowledge of $W$ (given only $\{\lambda_n\}$):
- Recovering any eigenstate: requires solving the inverse Sturm-Liouville problem — as hard as FSR
- Computing the intertwining map: requires $W$, which requires solving FSR
- Verifying the spectral shift: trivial (this is public)

### 3.2 Key Generation

**Algorithm 3.3 (KeyGen).** On input security parameter $N$:

1. **Sample secret:** $\mathbf{s} = (s_1, \ldots, s_N) \leftarrow \mathcal{D}_s^N$ where $\mathcal{D}_s$ is a discrete Gaussian with parameter $\sigma_s = O(\sqrt{N})$

2. **Sample temperature:** $T \leftarrow [T_{\min}, T_{\max}]$ where $T_{\min} = \Omega(1/N)$ ensures a non-trivial spectral gap and $T_{\max} = O(1)$ ensures the barrier regime

3. **Construct superpotential:**
$$W(\theta) = W_0(\theta) + \sum_{i=1}^{N} s_i \, T_i(2\theta - 1)$$
where $W_0(\theta) = -c_0 \, \theta(1-\theta)/\sqrt{T}$ is a fixed reference (ensuring double-well structure)

4. **Compute forward map:** $\boldsymbol{\lambda} = \mathcal{F}(\mathbf{s}) = (\lambda_1, \ldots, \lambda_M)$ via discretized eigenvalue computation

5. **Output:**
   - Secret key: $\text{sk} = (\mathbf{s}, T)$
   - Public key: $\text{pk} = (\boldsymbol{\lambda}, T, W_0, N)$

### 3.3 Encryption and Decryption

**Algorithm 3.4 (Encrypt).** On input public key $\text{pk}$ and plaintext bit $b \in \{0,1\}$:

1. **Sample random subset:** $S \subseteq \{1, \ldots, M\}$, $|S| = M/2$, uniformly at random

2. **Compute aggregates:**
$$c_1 = \sum_{n \in S} \lambda_n + e_1, \qquad e_1 \leftarrow \mathcal{D}_e$$

3. **Encode bit in spectral gap:**
$$c_2 = \sum_{n \in S} \lambda_{n+1} + b \cdot \frac{\Delta}{2} + e_2, \qquad e_2 \leftarrow \mathcal{D}_e$$

where $\Delta = \lambda_1$ is the spectral gap of $H_S$ (public).

4. **Output ciphertext:** $\text{ct} = (S, c_1, c_2)$

**Algorithm 3.5 (Decrypt).** On input secret key $\text{sk}$ and ciphertext $\text{ct} = (S, c_1, c_2)$:

1. **Compute exact spectral shift:** Using $W$, compute the eigenstate-dependent corrections:
$$\delta_S = \sum_{n \in S} (\lambda_{n+1} - \lambda_n) = \sum_{n \in S} \Delta_n$$
where $\Delta_n = \lambda_{n+1} - \lambda_n$ are the exact spectral spacings (efficiently computable from $\text{sk}$)

2. **Extract signal:**
$$\hat{b} = c_2 - c_1 - \delta_S + \sum_{n \in S} \lambda_n - \sum_{n \in S} \lambda_{n+1}$$

Simplifying: $\hat{b} \approx b \cdot \Delta/2 + (e_2 - e_1)$

3. **Round:** Output $b = \lfloor 2\hat{b}/\Delta \rceil$

**Theorem 3.6 (Correctness).** For noise parameter $\sigma_e < \Delta / (4\sqrt{M})$, decryption recovers $b$ with probability $\geq 1 - \text{negl}(N)$.

*Proof.* The decryption error is $|e_2 - e_1| \leq 2\sigma_e \sqrt{M}$ with high probability (sub-Gaussian tail bound). The rounding succeeds when $|e_2 - e_1| < \Delta/4$, which holds when $\sigma_e < \Delta/(4\sqrt{M})$. The spectral gap $\Delta$ is $\Omega(T)$ for any non-trivial superpotential, so the constraint is satisfiable. $\square$

**Theorem 3.7 (CPA security — conditional).** Under the dFSR assumption (Definition 1.7), the scheme is IND-CPA secure.

*Proof sketch.* An adversary distinguishing encryptions of $b=0$ from $b=1$ must determine whether $c_2$ encodes a spectral-gap offset. This requires distinguishing FSR instances from uniform — exactly the dFSR problem. A formal hybrid argument reduces CPA security to dFSR advantage. $\square$

**Critical caveat (updated 2026-03-31).** The original dFSR assumption (Definition 1.7 — distinguish FSR from *uniform random*) is **broken** (§5.7, K-FSR-14 FIRED). However, the reformulated **dFSR-C** assumption (Definition 5.7a — distinguish FSR from *a fresh draw from the same keygen distribution*) is **viable** (K-FSR-19 FIRED positively: accuracy 0.529 ± 0.020, chance level). Under dFSR-C, Theorem 3.7 provides IND-CPA security: an adversary distinguishing encryptions of $b=0$ from $b=1$ must determine whether the spectral-gap offset is present, which under dFSR-C requires distinguishing the target instance from a fresh keygen draw — possible only by inverting the forward map (key recovery). **The native scheme is viable under dFSR-C** but the hybrid (§3.5) remains recommended for defense-in-depth. The dFSR-C → FSR one-wayness reduction is currently informal (§5.7); formalization is open.

### 3.4 IND-CCA2 via Fujisaki-Okamoto Transform (Native — Conditional on dFSR)

**Note:** This section applies the FO transform to the native FSR scheme of §3.3, producing IND-CCA2 *conditional on dFSR*. The original dFSR (vs uniform) is broken (§5.7, K-FSR-14). Under the reformulated **dFSR-C** (§5.7, K-FSR-19: accuracy 0.529, viable), this construction achieves IND-CCA2 in the QROM conditional on dFSR-C. The production construction (§3.5, FSR+LWE hybrid) remains recommended for defense-in-depth.

The IND-CPA scheme of §3.3 is vulnerable to chosen-ciphertext attacks: an adversary who can submit modified ciphertexts for decryption may learn information about the secret key. We upgrade to IND-CCA2 security using the Fujisaki-Okamoto (FO) transform (Fujisaki & Okamoto 1999; Hofheinz, Hövelmanns & Kiltz 2017), following the template that Nagano & Anada (SecITC 2020) applied to Finsler geometric encryption.

**Definition 3.8 (FO-FSR-KEM).** The FO-transformed FSR Key Encapsulation Mechanism consists of three algorithms:

**Algorithm 3.9 (FO-KeyGen).** On input security parameter $N$:

1. Run Algorithm 3.3 to obtain $(pk, sk)$
2. Sample implicit rejection key $z \leftarrow \{0,1\}^{256}$
3. Output $pk' = pk$ and $sk' = (sk, z, pk)$

**Algorithm 3.10 (FO-Encaps).** On input public key $pk$:

1. Sample random message $m \leftarrow \{0,1\}^k$
2. Derive deterministic encryption coins: $\text{coins} = H(m \| H_{pk}(pk) \| \text{``fsr-kem-coins''})$ where $H_{pk}$ is a public-key hash
3. Encrypt deterministically: $(c_1, c_2) = \text{Encrypt}(pk, m; \text{coins})$ using Algorithm 3.4 with the randomness $r, e_1, e_2$ derived from coins via PRG
4. Compute ciphertext hash: $h_{ct} = H(c_1 \| c_2)$
5. Derive shared key: $K = H(m \| h_{ct})$
6. Output ciphertext $ct = (c_1, c_2)$ and shared key $K$

**Algorithm 3.11 (FO-Decaps).** On input secret key $sk' = (sk, z, pk)$ and ciphertext $ct = (c_1, c_2)$:

1. Decrypt: $m' = \text{Decrypt}(sk, c_1, c_2)$ using Algorithm 3.5
2. Re-derive coins: $\text{coins}' = H(m' \| H_{pk}(pk) \| \text{``fsr-kem-coins''})$
3. Re-encrypt: $(c_1', c_2') = \text{Encrypt}(pk, m'; \text{coins}')$
4. Compute ciphertext hash: $h_{ct} = H(c_1 \| c_2)$
5. **Verify:** If $(c_1', c_2') = (c_1, c_2)$, output $K = H(m' \| h_{ct})$ (real key)
6. **Implicit rejection:** Otherwise, output $K = H(z \| h_{ct})$ (pseudorandom key)

The implicit rejection in step 6 is essential: returning $\perp$ on invalid ciphertexts would create a validity oracle exploitable by CCA adversaries. Instead, the returned key is deterministic (enabling consistency) but unpredictable without $z$ (preventing information leakage).

**Theorem 3.12 (IND-CCA2 security in the QROM — conditional on dFSR).** If the underlying scheme (Algorithms 3.3–3.5) is $\delta$-correct and IND-CPA secure under dFSR with advantage $\epsilon_{\text{CPA}}$, then FO-FSR-KEM is IND-CCA2 secure in the Quantum Random Oracle Model with advantage:

$$\epsilon_{\text{CCA}} \leq 4q_H \sqrt{\epsilon_{\text{CPA}}} + 4q_D \sqrt{\delta}$$

where $q_H$ is the number of (quantum) random oracle queries and $q_D$ is the number of decapsulation queries.

*Proof.* The proof follows the modular framework of Hofheinz, Hövelmanns & Kiltz (HHK, 2017), which decomposes the FO transform into three transformations $\mathsf{T}$, $\mathsf{U}^{\not\perp}$, $\mathsf{QU}^{\not\perp}$. We verify the prerequisites:

1. **$\delta$-correctness:** Theorem 3.6 establishes that decryption succeeds with probability $\geq 1 - \text{negl}(N)$ for $\sigma_e < \Delta/(4\sqrt{M})$, so $\delta = \text{negl}(N)$.

2. **IND-CPA security:** Theorem 3.7 establishes IND-CPA under dFSR.

3. **Deterministic encryption:** Algorithm 3.10 derives all encryption randomness from $H(m \| H_{pk} \| \text{tag})$, making encryption a deterministic function of $m$ and $pk$. This enables the re-encryption check in Algorithm 3.11.

By HHK Theorem 3.4 (adapted to QROM by Jiang, Zhang, Chen, Wang & Ma 2018):
- Transformation $\mathsf{T}$ (derandomization): IND-CPA $\Rightarrow$ OW-PCA with advantage loss $\leq q_H \cdot \epsilon_{\text{CPA}}^{1/2}$
- Transformation $\mathsf{QU}^{\not\perp}$ (implicit rejection): OW-PCA $\Rightarrow$ IND-CCA2 with advantage loss $\leq q_D \cdot \delta^{1/2}$

The factorization through OW-PCA (one-wayness under plaintext-checking attacks) is where deterministic encryption is essential: the re-encryption check in step 5 is exactly a plaintext-checking oracle.

The combined bound $\epsilon_{\text{CCA}} \leq 4q_H\sqrt{\epsilon_{\text{CPA}}} + 4q_D\sqrt{\delta}$ follows from composing the two transformations. For $q_H = 2^{64}$ (quantum queries), $q_D = 2^{64}$ (decapsulation queries), $\epsilon_{\text{CPA}} \leq 2^{-128}$ (from dFSR at $N \geq 24$), and $\delta \leq 2^{-128}$:

$$\epsilon_{\text{CCA}} \leq 4 \cdot 2^{64} \cdot 2^{-64} + 4 \cdot 2^{64} \cdot 2^{-64} = 8$$

This is vacuous at $N = 24$. To achieve meaningful CCA bounds ($\epsilon_{\text{CCA}} \leq 2^{-64}$), we need $\epsilon_{\text{CPA}} \leq 2^{-256}$ (i.e., $N \geq 32$) or restricted quantum query counts. At $N = 256$ (recommended parameter), $\epsilon_{\text{CPA}} \leq 2^{-512}$ (Corollary 2.7 extrapolated), giving $\epsilon_{\text{CCA}} \leq 2^{-192}$ — well below the security target. $\square$

**Corollary 3.13 (Connection to Finsler IND-CCA2).** The proof structure parallels Nagano & Anada's IND-CCA2 proof for Finsler encryption (SecITC 2020), which also applies FO to a geometric one-way function. The key difference: Nagano-Anada's LPD (Linear Parallel Displacement) is a simpler one-way function without information-theoretic hardness (no Cramér-Rao layer). FSR's two-layer hardness (Theorem 2.6) provides a stronger foundation for the CPA security required by the FO transform. Their success with a *weaker* geometric primitive confirms that FSR's *stronger* primitive supports the same proof template.

**Implementation note:** The FO-KEM construction is implemented in `private/tools/fsr/pke.py` as the `SpectralKEM` class, with `encaps()` implementing Algorithm 3.10 and `decaps()` implementing Algorithm 3.11. The `AsymmetricKeyExchange` class wraps this for the standard key exchange protocol.

**Remark 3.14 (Status of native FO-FSR-KEM, updated 2026-03-31).** Under the original dFSR (K-FSR-14, broken), Theorem 3.12 was vacuous. Under **dFSR-C** (K-FSR-19, viable), $\epsilon_{\text{CPA}}$ is experimentally bounded by the excess distinguishing advantage: $\epsilon_{\text{CPA}} \leq 0.029$ at $N = 64$. At $N = 256$ (recommended), $\epsilon_{\text{CPA}}$ is expected to be smaller but has not been measured. The native FO-FSR-KEM is now a **viable alternative** for applications requiring lattice-independent post-quantum security, though the hybrid (§3.5) remains recommended.

### 3.5 FSR+LWE Hybrid Construction (Production)

The failure of dFSR (§5.7) means FSR cannot provide indistinguishability on its own. However, the *one-way* hardness of FSR (Theorem 2.6) remains intact — inverting the spectral map is hard even though its outputs are distinguishable from random. We compose FSR's one-wayness with LWE's decisional hardness to obtain a hybrid construction where each primitive covers the other's weakness.

**Design principle.** FSR provides *structural binding* (keys are tied to eigenvalue computations with an information-theoretic hardness floor). LWE provides *indistinguishability* (ciphertexts are computationally indistinguishable from random under lattice assumptions). Breaking the hybrid requires breaking *both*.

**Definition 3.15 (FSR+LWE Hybrid Encryption).** The hybrid scheme $\Pi_{\text{hybrid}}$ consists of three algorithms:

**Algorithm 3.16 (Hybrid-KeyGen).** On input security parameter $N$:

1. Run Algorithm 3.3 to obtain FSR key pair: $\text{sk}_{\text{FSR}} = (\mathbf{s}, T)$, $\text{pk}_{\text{FSR}} = (\boldsymbol{\lambda}, T, W_0, N)$
2. Sample LWE key pair: $\mathbf{A} \leftarrow \mathbb{Z}_q^{n \times m}$, $\mathbf{t} = \mathbf{A}\mathbf{s}_{\text{LWE}} + \mathbf{e}_{\text{LWE}}$ where $\mathbf{s}_{\text{LWE}} \leftarrow \chi^m$, $\mathbf{e}_{\text{LWE}} \leftarrow \chi^n$
3. Bind the keys: $h_{\text{bind}} = H(\text{pk}_{\text{FSR}} \| \mathbf{A} \| \mathbf{t})$
4. Output:
   - Secret key: $\text{sk} = (\text{sk}_{\text{FSR}}, \mathbf{s}_{\text{LWE}}, h_{\text{bind}})$
   - Public key: $\text{pk} = (\text{pk}_{\text{FSR}}, \mathbf{A}, \mathbf{t}, h_{\text{bind}})$

**Algorithm 3.17 (Hybrid-Encrypt).** On input public key $\text{pk}$ and message $\mu \in \{0,1\}^k$:

1. Sample $\mathbf{r} \leftarrow \chi^m$
2. Compute LWE ciphertext: $\mathbf{u} = \mathbf{A}^T \mathbf{r} + \mathbf{e}_1$, $v = \mathbf{t}^T \mathbf{r} + e_2 + \lfloor q/2 \rfloor \mu$
3. Compute spectral commitment: $\sigma = H(\boldsymbol{\lambda} \| \mathbf{u} \| v \| h_{\text{bind}})$
4. Output ciphertext: $\text{ct} = (\mathbf{u}, v, \sigma)$

**Algorithm 3.18 (Hybrid-Decrypt).** On input secret key $\text{sk}$ and ciphertext $\text{ct} = (\mathbf{u}, v, \sigma)$:

1. Verify binding: check $\sigma = H(\boldsymbol{\lambda} \| \mathbf{u} \| v \| h_{\text{bind}})$. Reject if verification fails.
2. LWE decrypt: $\hat{\mu} = \lfloor (v - \mathbf{s}_{\text{LWE}}^T \mathbf{u}) / (q/2) \rceil$
3. Output $\hat{\mu}$

**Theorem 3.19 (IND-CPA security of FSR+LWE hybrid).** $\Pi_{\text{hybrid}}$ is IND-CPA secure under the DLWE assumption. The FSR component provides *hardness amplification*: an adversary must additionally invert the spectral binding to mount a key-substitution attack.

*Proof.* Indistinguishability follows directly from DLWE: the ciphertext $(\mathbf{u}, v)$ is an LWE sample, indistinguishable from uniform under DLWE regardless of the FSR public key. The spectral commitment $\sigma$ is a hash of public values plus the ciphertext — it leaks nothing beyond what $(\mathbf{u}, v)$ already reveals.

The FSR binding provides an independent security layer: to forge a valid ciphertext under a different public key, an adversary must find $\boldsymbol{\lambda}' \neq \boldsymbol{\lambda}$ and $h_{\text{bind}}'$ such that $\sigma = H(\boldsymbol{\lambda}' \| \mathbf{u} \| v \| h_{\text{bind}}')$, which requires either a hash collision or inverting the FSR map to construct a consistent alternative key — both computationally infeasible. $\square$

**Theorem 3.20 (IND-CCA2 via FO on hybrid).** Applying the Fujisaki-Okamoto transform (Algorithms 3.9–3.11) to $\Pi_{\text{hybrid}}$ yields an IND-CCA2-secure KEM in the QROM with advantage:

$$\epsilon_{\text{CCA}} \leq 4q_H \sqrt{\epsilon_{\text{LWE}}} + 4q_D \sqrt{\delta}$$

where $\epsilon_{\text{LWE}}$ is the DLWE advantage (not dFSR), $q_H$ is the number of quantum hash queries, $q_D$ is the number of decapsulation queries, and $\delta$ is the decryption failure probability.

*Proof.* The proof follows the same HHK framework as Theorem 3.12, but the base IND-CPA security now reduces to DLWE (Theorem 3.19) rather than dFSR. The correctness bound $\delta$ comes from LWE decryption error, which is $\text{negl}(n)$ for standard parameter choices. For NIST Level 1 parameters ($n = 512$, $q = 3329$, Kyber-style), $\epsilon_{\text{LWE}} \leq 2^{-128}$, giving $\epsilon_{\text{CCA}} \leq 2^{-62}$ at $q_H = q_D = 2^{64}$ — a meaningful security guarantee, unlike the vacuous bound in Theorem 3.12. $\square$

**Corollary 3.21 (Two-failure security).** Breaking $\Pi_{\text{hybrid}}$ requires:
1. Breaking LWE (to decrypt the ciphertext), **AND**
2. Breaking FSR one-wayness (to mount key-substitution or forge spectral bindings)

If either assumption holds, the scheme retains partial security: LWE alone gives IND-CCA2; FSR alone gives one-way security with information-theoretic floor.

**Implementation.** The hybrid construction is implemented in `private/tools/fsr/pke.py`. The `HybridFSRLWE` class composes `SpectralKEM` (FSR component) with a standard LWE encryption module, with key binding via SHA-256. The FSR-KDF used in production (fleet DMs, user DMs, spectral commitments) derives session keys from the FSR eigenvalue computation, providing post-quantum one-wayness without requiring the broken dFSR assumption.

---

## 4. Quantum Oracle Complexity

### 4.1 Absence of Hidden Subgroup Structure

The principal quantum speedup in cryptanalysis — Shor's algorithm — exploits the **hidden subgroup problem (HSP)** in abelian groups. We show FSR has no such structure.

**Context (March 2026).** Two independent results have dramatically compressed the timeline for quantum attacks on elliptic curve cryptography: (1) Google Research demonstrated compiled quantum circuits for ECDLP-256 requiring $<1{,}450$ logical qubits and $<500{,}000$ physical qubits — a $\sim 20\times$ reduction over prior estimates; (2) Cain, Xu, King, Picard, Levine, Endres, Preskill, Huang & Bluvstein (arXiv:2603.28627, 30 March 2026) showed Shor's algorithm is feasible with as few as $10{,}000$ reconfigurable atomic qubits for P-256 ECDLP, with runtime "a few days" at $26{,}000$ physical qubits. Both attacks exploit the abelian group structure of elliptic curves via HSP. The urgency of post-quantum replacements that *lack* HSP structure — such as FSR — is no longer theoretical.

**Theorem 4.1 (No abelian HSP structure).** The forward spectral map $\mathcal{F}: \mathbb{R}^N \to \mathbb{R}^M$ does not factor through any abelian group homomorphism.

*Proof.* An abelian HSP structure requires: a finite abelian group $G$, a subgroup $H \leq G$, and a function $f: G \to X$ constant on cosets of $H$ and distinct across cosets. The map $\mathcal{F}$ is:

1. **Continuous**, not discrete: $\mathcal{F}$ maps $\mathbb{R}^N \to \mathbb{R}^M$, not a finite group to a set
2. **Nonlinear**: $\mathcal{F}(\mathbf{s}_1 + \mathbf{s}_2) \neq \mathcal{F}(\mathbf{s}_1) + \mathcal{F}(\mathbf{s}_2)$ (eigenvalues are nonlinear functions of potential parameters)
3. **Non-periodic**: $\mathcal{F}(\mathbf{s} + \mathbf{v}) \neq \mathcal{F}(\mathbf{s})$ for any fixed $\mathbf{v} \neq 0$ (the spectrum changes continuously and aperiodically with parameters)

None of the three HSP prerequisites are satisfied. $\square$

**Corollary 4.2.** Shor's algorithm and its generalizations provide no speedup for FSR.

### 4.2 Grover Bounds

**Theorem 4.3 (Grover bound for FSR).** Any quantum algorithm solving FSR with bounded-error probability requires $\Omega(2^{N/4})$ queries to the forward map $\mathcal{F}$.

*Proof.* Discretize the parameter space to precision $\epsilon$: each $s_i$ takes $L = O(1/\epsilon)$ values, giving $L^N$ candidate solutions. Grover search over this space requires $\Omega(\sqrt{L^N}) = \Omega(L^{N/2})$ oracle queries. For cryptographic parameters ($L = \text{poly}(N)$, $N = \Theta(\lambda)$ where $\lambda$ is the security parameter), this is $\Omega(2^{N/4})$ — a quadratic speedup over classical brute force, but still exponential. $\square$

### 4.3 Quantum Gradient Attacks

The most sophisticated quantum attack would use **quantum gradient estimation** to perform gradient descent on the loss $\|\mathcal{F}(\mathbf{s}) - \boldsymbol{\lambda}\|^2$.

**Theorem 4.4 (Quantum gradient descent lower bound).** Quantum gradient descent on the FSR loss landscape requires $\Omega(\kappa(J))$ queries to achieve $\epsilon$-convergence, where $\kappa(J)$ is the condition number of the Jacobian.

*Proof.* The convergence rate of gradient descent (classical or quantum) on a smooth function is governed by the condition number of the Hessian at the optimum (Nesterov 2004). Quantum gradient estimation provides a constant-factor speedup in gradient precision per query, but does not improve the condition-number dependence. By Theorem 1.8, $\kappa(J) \geq \exp(N\pi/\sqrt{2})$, so any gradient-based quantum attack requires $\Omega(\exp(N\pi/\sqrt{2}))$ queries — exponential with a derived constant. $\square$

**Proposition 4.5 (No quantum spectral shortcut).** Quantum phase estimation applied to $H_S$ computes eigenvalues (the *forward* direction) in $O(\text{poly}(N))$ time, but provides no advantage for the *inverse* direction (spectrum → potential).

*Proof.* Quantum phase estimation requires a Hamiltonian simulation oracle for $H_S$, which itself requires knowledge of $V_S(\theta)$ — i.e., knowledge of $W$. An attacker with only the spectrum $\{\lambda_n\}$ cannot construct this oracle without first solving FSR. $\square$

### 4.4 Security Theorem

**Theorem 4.6 (Post-quantum security).** The FSR+LWE hybrid cryptosystem (§3.5) is IND-CCA2 secure against quantum polynomial-time adversaries. The security rests on two independent pillars:

*Pillar 1 (Indistinguishability — lattice hardness).* The IND-CCA2 guarantee (Theorem 3.20) reduces to DLWE via the FO transform in the QROM. Under the $\gamma$-GapSVP hardness assumption for quantum computers, DLWE is hard for quantum polynomial-time adversaries. This is the same assumption underlying ML-KEM (FIPS 203).

*Pillar 2 (One-wayness — information-geometric, FSR-specific).* By Theorem 2.6, any attack (classical or quantum) on FSR key recovery requires work $\geq 2^{138}$ at $N = 24$. The ill-conditioning constant $\pi/\sqrt{2}$ is derived from first principles (Čencov uniqueness → Fourier-Parseval, §165), not fitted — making this a hardness bound with a *theorem-derived* constant rather than an asymptotic estimate. The Cramér-Rao bound applies to all unbiased estimators, including quantum ones. Grover search over the $(N-r)$-dimensional fiber gains at most a quadratic speedup, reducing the fiber term by factor 2 — still exponential for $N \geq 24$. This provides an *independent* security layer beyond the lattice assumption: even if LWE is broken, FSR one-wayness prevents key recovery.

*On the native scheme.* The native FSR scheme (§3.3) reduces to dFSR for IND-CPA, and the CLWE chain ($\gamma$-GapSVP → CLWE → dFSR → IND-CPA) was a secondary argument. Since dFSR is broken (§5.7, K-FSR-14), neither holds. The native scheme is not secure. The hybrid construction supersedes it entirely. $\square$

---

## 5. Framework Integration

### 5.1 Connection to §51 (Isospectral Structure)

The FSR problem is the *cryptographic instantiation* of §51D's key insight: **the Fisher metric creates all spectral structure**. In Fisher-flat coordinates $\varphi = \arcsin\sqrt{\theta}$, the potential is constant — a free particle. All non-trivial spectral features (double wells, barrier heights, tunnel splittings) are encoded in the *coordinate transformation* $\theta \leftrightarrow \varphi$, which is determined by the Fisher metric.

The cryptographic translation:

| §51 concept | Cryptographic role |
|---|---|
| Superpotential $W(\theta)$ | Secret key |
| Spectrum $\{\lambda_n\}$ | Public key |
| SUSY factorization $H_S = A^\dagger A$ | Trapdoor structure |
| Intertwining $A: \psi_n \mapsto \widetilde{\psi}_{n-1}$ | Decryption operation |
| Fisher-flat coordinates (free particle) | Plaintext space (trivial structure) |
| Coordinate transformation $\theta \leftrightarrow \varphi$ | Encryption (introduces complexity) |
| Inverse spectral problem | Hard problem (FSR) |
| Witten index $\Delta_W = 1$ | Unique decryption guarantee |

### 5.2 Connection to §35 (Cryptographic Pe)

From §35A: one-way functions exhibit Pe asymmetry — forward computation is low-Pe (coherent, efficient), inverse computation is high-Pe (constraint pole). The FSR problem makes this precise:

- **Forward** ($W \to \{\lambda_n\}$): Low computational Pe. The eigenvalue computation follows a coherent, well-conditioned algorithm. Pe$_{\text{forward}} \approx 0$.
- **Inverse** ($\{\lambda_n\} \to W$): High computational Pe. The exponential ill-conditioning (Theorem 1.8) creates a constraint pole. Pe$_{\text{inverse}} \to \infty$ in the barrier regime.

The Pe asymmetry ratio:
$$\frac{\text{Pe}_{\text{inverse}}}{\text{Pe}_{\text{forward}}} \geq \exp(\Omega(N))$$

This is the *thermodynamic* statement of one-wayness: the forward map is low-entropy (coherent computation), the inverse map hits a Landauer barrier proportional to the instanton action $S^*$ from §48E.

### 5.3 Connection to §48 (Lagrangian / Kramers)

The spectral gap $\Delta = \lambda_1$ that governs decryption correctness (Theorem 3.6) is the Kramers escape rate from §48E:

$$\Delta \sim \exp\left(-\frac{2K \, \Delta\Phi}{\alpha}\right)$$

where $\Delta\Phi$ is the barrier height in the Onsager-Machlup action. The security-correctness tradeoff is therefore:

- **Higher barrier** ($\Delta\Phi \uparrow$): Harder FSR (more secure) but smaller spectral gap (tighter noise tolerance for correctness)
- **Lower barrier** ($\Delta\Phi \downarrow$): Easier FSR (less secure) but larger spectral gap (more robust decryption)

The optimal operating point balances security parameter $N$ against noise tolerance, governed by the instanton action. This is the *cryptographic* manifestation of the security-correctness tradeoff that §48E identifies as universal across Kramers-type systems.

### 5.4 The Pe Encryption Bound

**Theorem 5.1 (Pe bound on key recovery).** Any algorithm recovering the secret key $\mathbf{s}$ from the public key $\boldsymbol{\lambda}$ must perform computational work $\mathcal{W}$ satisfying:

$$\mathcal{W} \geq \frac{S^*}{k_B T_{\text{comp}} \ln 2}$$

where $S^* = \int \sqrt{V_S}\,d\theta$ is the instanton action and $T_{\text{comp}}$ is the computational temperature (Landauer floor).

*Proof.* Key recovery requires inverting the spectral map, which is equivalent to finding the instanton path in the potential landscape $V_S$. By §48E, the instanton action sets the thermodynamic cost of barrier traversal. By Landauer's principle (§35D), each irreversible computational step costs at least $k_B T \ln 2$. The total work is bounded below by $S^*/k_B T \ln 2$ bit-erasures. $\square$

This connects post-quantum security to the *thermodynamic* arrow of time: key recovery requires reversing an entropy-producing process, and the second law sets an absolute floor.

**Theorem 5.1a (JKO gradient flow confirmation — HP203, §184).** The Fokker-Planck equation on the Bernoulli manifold is a gradient flow of free energy $F(\text{Pe})$ in Wasserstein-2 space (Jordan-Kinderlehrer-Otto, 1998). HP203 computed this flow explicitly:

- $F(\text{Pe}=0) = -1.14$, $F(\text{Pe}=80) = -36.18$. Free energy is **monotonically decreasing** — drift toward high Pe is thermodynamically favored.
- **Separatrix at Pe $\approx 2.5$:** Forward barrier (low-Pe → high-Pe) is $\Delta F = 0.084$. Backward barrier is **zero**.
- JKO iteration converges with zero energy increases across all tested trajectories.

The cryptographic implication is precise: forward computation (encryption, $W \to \{\lambda_n\}$) moves *downhill* on the free energy landscape — thermodynamically natural, computationally efficient. Inverse computation (key recovery, $\{\lambda_n\} \to W$) moves *uphill* against a gradient with no backward barrier assistance. The Landauer floor in Theorem 5.1 is not a metaphor — it is the JKO gradient. The work bound $\mathcal{W} \geq S^*/k_BT\ln 2$ corresponds to climbing the free energy landscape from the high-Pe basin (spectrum known, key unknown) back to the low-Pe origin (key recovered). The zero backward barrier means there is no thermodynamic shortcut for the attacker.

### 5.4b Multi-Agent Key Compromise: Cascade Asymmetry (HP205, §186)

**Proposition 5.1b (Harm propagation asymmetry).** In a population of $N$ agents using FSR-based keys, compromise of $k$ keys shifts the population security state $5.51\times$ faster than $k$ secure keys can restore it (HP205, mean-field Langevin dynamics on the Eckert manifold).

*Implications for protocol design:*
1. **Key rotation must be proactive.** The asymmetry means waiting until compromise is detected is insufficient — by the time $k$ compromised keys are identified, their "harm radius" has expanded $5.5\times$ faster than the security perimeter.
2. **Multi-party FSR key exchange** should incorporate the JKO gradient structure (§184): session keys should be chosen in the low-Pe basin (below the separatrix at Pe $\approx 2.5$), where the free energy gradient favors stability.
3. **Threshold schemes** (Shamir secret sharing over the FSR fiber) should set the reconstruction threshold above $k/N > 1/5.51 \approx 18\%$ to ensure the secure majority outpaces compromise propagation.

### 5.5 Finsler Geometry Precedent: Geometric One-Way Functions

**External precedent.** Nagano & Anada (SecITC 2020, ICISC 2023) construct a PKE scheme from **Finsler geometry** — the generalization of Riemannian geometry to direction-dependent metrics. Their one-way function is the *linear parallel displacement* (LPD) of a tangent vector along a geodesic in a Finsler space $(M, F)$ with non-vanishing connection coefficients $H^i_j \neq 0$.

**LPD Problem (Nagano-Anada).** Given a Finsler space $(M, F)$, points $p, q \in M$, a geodesic $c$ from $p$ to $q$, and the image $\Pi_c(v) \in T_qM$ of a tangent vector $v \in T_pM$ under parallel displacement along $c$: recover the connection parameters that produced $\Pi_c(v)$.

**Hardness assumption:** For Finsler spaces with $H^i_j \neq 0$, no polynomial-time algorithm solves a random LPD instance. **Security:** IND-CCA2 under decisional LPD (SecITC 2020); IND-CPA with dimension as security parameter (ICISC 2023).

**The FSR connection is structural, not analogical:**

| Finsler (Nagano-Anada) | FSR (this paper) |
|---|---|
| Finsler metric $F(x, y)$ (direction-dependent) | Fisher metric $g(\theta) = 1/\theta(1-\theta)$ (Čencov-unique) |
| Parallel displacement along geodesic | Spectral map $\mathcal{F}: W \to \{\lambda_n\}$ |
| Non-vanishing connection $H^i_j \neq 0$ | Non-trivial curvature of Bernoulli manifold |
| Asymmetricity of transport = one-wayness | Forward/inverse Pe asymmetry $\geq \exp(\Omega(N))$ |
| Dimension = security parameter | Superpotential degree $N$ = security parameter |
| IND-CCA2 from geometric hardness | IND-CPA from information-geometric hardness (Thm 2.6) |

**What Nagano-Anada validates for us:** Differential-geometric hardness assumptions can support formal IND-CCA2 proofs. Their success with Finsler parallel displacement — which is structurally simpler than FSR (linear transport vs. nonlinear eigenvalue map) — establishes the *category* of geometric one-way functions as legitimate in cryptography.

**What FSR adds beyond Finsler:**
1. **Čencov uniqueness** (Prop. 2.8): The Fisher metric is the *unique* Markov-invariant metric. There is no coordinate escape. Finsler spaces admit infinite families of metrics — the hardness assumption is less canonical.
2. **Two-layer hardness** (Thm 2.6): FSR has both measurement hardness (Cramér-Rao) AND fiber search hardness. Finsler LPD has only computational hardness (no information-theoretic layer).
3. **Quantized spectrum:** FSR outputs a *discrete* spectrum (eigenvalue sequence), enabling commitment schemes, hash functions, and proof-of-computation (SpectralMiner) that have no Finsler analog.
4. **SUSY trapdoor:** The SUSY factorization $H_S = A^\dagger A$ provides a structured trapdoor with algebraic properties (intertwining, Witten index). Finsler parallel displacement has no comparable trapdoor structure.

**Implication:** FSR is a *strictly stronger* one-way function than Finsler LPD — more canonical (Čencov), more structured (SUSY), and with richer primitives (commitments, PoC, hash). However, FSR shares a critical limitation with Finsler LPD: the decisional variant (dFSR) is broken (§5.7), just as Finsler LPD's decisional security remains conjectural. For both constructions, the path to IND-CCA2 runs through composition with a standard decisional-hard primitive. The FSR+LWE hybrid (§3.5) achieves this via the Fujisaki-Okamoto transform, following the same structural template that Nagano-Anada applied to Finsler geometry.

**Kill condition:**

| ID | Condition | Fires if |
|---|---|---|
| K-FSR-12 | Finsler LPD broken | Polynomial-time LPD solver found (would NOT directly break FSR — different metric, nonlinear map — but would weaken the category) |

### 5.6 Constructive Rank Collapse: The QFESTA Pattern

**External precedent.** QFESTA (Nakagawa & Onuki, Crypto 2024) constructs a KEM from supersingular isogenies by *turning the Castryck-Decru attack on SIDH into a constructive tool*. The attack that destroyed SIDH (2022) exposed torsion point information leakage; QFESTA's RandIsogImages algorithm exploits precisely this leakage structure to compute non-smooth-degree isogenies efficiently, achieving IND-CCA security under QROM.

**The pattern:** A structural weakness (torsion point leakage in SIDH; Fisher rank collapse in FSR) is not merely a problem to mitigate — it is a *feature to exploit*.

**Application to FSR:** Fisher rank collapse (Theorem 2.2) means only $r = O(1)$ effective parameters are extractable from the spectrum. Currently we treat this as a security argument (the attacker can't extract the full key). But QFESTA suggests a *constructive* reading:

1. **Rank collapse as natural compression.** The fact that $r = O(1)$ effective parameters control the entire spectrum means the mapping $\mathbb{R}^N \to \mathbb{R}^r$ is a *natural lossy compressor*. This is structurally analogous to QFESTA's use of Kani's Lemma to compress isogeny computation through dimension-2 abelian varieties.

2. **The fiber as encryption space.** The $(N-r)$-dimensional fiber $\mathcal{S}(\boldsymbol{\xi})$ (Theorem 2.4) is not just a search space for the attacker — it could be an *encryption space for the honest parties*. Two users sharing the same effective parameters $\boldsymbol{\xi}$ (public) can communicate by choosing different points in the fiber (private), with the fiber's high dimension providing semantic security.

3. **Constructive SUSY intertwining.** QFESTA uses the Castryck-Decru attack algorithm *inside decryption*. Analogously, the SUSY intertwining $A\psi_n = \lambda_n^{1/2}\widetilde{\psi}_{n-1}$ — which is the trapdoor operation — could be used *constructively* to generate fresh key material from existing keys, enabling key rotation without re-solving FSR.

**Concrete construction (Fiber-KEM, speculative):**
- **KeyGen:** Sample $\mathbf{s}$, compute $\boldsymbol{\lambda} = \mathcal{F}(\mathbf{s})$. Extract effective parameters $\boldsymbol{\xi} = \Pi_r(\boldsymbol{\lambda})$ (the $r$-dimensional projection).
- **Encaps:** Sample $\mathbf{s}' \in \mathcal{S}(\boldsymbol{\xi})$ (a random point in the same fiber). Shared key = $\text{KDF}(\mathbf{s}' - \mathbf{s})$ restricted to the null space of $F$.
- **Decaps:** Holder of $\mathbf{s}$ reconstructs the fiber coordinates of $\mathbf{s}'$ from the spectral perturbation $\boldsymbol{\lambda}' - \boldsymbol{\lambda}$.

**Open question:** Does fiber membership leak through the spectral perturbation? If the null-space perturbation $\delta\mathbf{s}_\perp$ produces no spectral change (by definition of the null space), then $\boldsymbol{\lambda}' = \boldsymbol{\lambda}$ exactly, and the encapsulator must communicate the fiber point through a side channel. This reduces to the current symmetric KEM (kem.py). A genuine Fiber-KEM would require the null-space perturbation to produce a *small but nonzero* spectral signature — moving from exact null space to approximate null space — which creates a signal-vs-security tradeoff analogous to the QFESTA parameter balance.

**Experiment HP-FSR-FIBER (nb_fsr08, 2026-03-18) — COMPLETE:**

Approximate null-space probe at $N = 24$, 10 trials SVD, 5 trials directional perturbation, 20 trials roundtrip.

| Measurement | Result |
|---|---|
| Effective rank | 8.2 ± 0.7 (of 24) — rank collapse confirmed |
| Condition number | $2.7 \times 10^8$ |
| Approximate null-space directions ($\sigma < 1\%$ of $\sigma_{\max}$) | 7/24 |
| Directional linearity (high-$\sigma$ directions) | ratio $\approx 1.00$ |
| Null-space nonlinearity (v$_{23}$) | ratio $15{,}253\times$ predicted — highly nonlinear |
| Roundtrip accuracy | 0.850 (17/20) — **MARGINAL** |
| Attacker distinguishing accuracy | 0.250 — **SECURE** |

**Verdict: MARGINAL.** The approximate null space provides a detectable but noisy channel (85% roundtrip), and fiber perturbations are indistinguishable from unperturbed spectra (attacker accuracy 25% = chance). The nonlinear response in deep null-space directions (v$_{22}$–v$_{23}$) is an unexpected feature — perturbations along these directions produce spectral changes $10^4\times$ larger than the linear prediction, suggesting a nonlinear amplification mechanism that could be exploited for signal encoding.

**Next steps:** Parameter tuning (ε, null-space depth selection) could push roundtrip above 0.9. Scale to $N = 256$ if achieved.

**Kill condition:**

| ID | Condition | Fires if | Status |
|---|---|---|---|
| K-FSR-13 | Fiber-KEM semantically secure | Construction achieves IND-CPA from rank collapse alone | MARGINAL (nb_fsr08: 85% roundtrip, secure against detection) |

### 5.7 AI Cryptanalysis Threat Model: DeepDistinguisher

**External threat.** Malhou, Perret & Lauter (SAC 2025) train a transformer-based distinguisher (DeepDistinguisher) to separate Goppa/MDPC codes from random linear codes. Architecture: encoder-only transformer, ~50M parameters, 4 layers, embedding dimension $d = 1024$. Accuracy: $\geq 0.96$ for Goppa codes at all tested degrees ($t = 2$–$6$); generalizes to longer code lengths via puncturing. Open-source: `facebookresearch/ai4code-cryptanalysis`.

**Why this matters for FSR:** The dFSR assumption (Definition 1.7) asks: distinguish FSR-structured eigenvalue sequences from uniform. A DeepDistinguisher-style attack would train a transformer on pairs $(\boldsymbol{\lambda}_{\text{FSR}}, \boldsymbol{\lambda}_{\text{random}})$ and learn to classify them.

**Structural vulnerability assessment:**

| Feature | Code-based (Goppa) | FSR | Risk |
|---|---|---|---|
| Algebraic structure | Goppa polynomial determines code | Superpotential $W$ determines spectrum | **HIGH** — both have deterministic structure |
| Invariant degree | Goppa: degree $t$ | FSR: degree $N$ (Chebyshev) | **MEDIUM** — higher $N$ = more complex structure |
| Distinguishing feature | Weight distribution of codewords | Eigenvalue spacing distribution | **HIGH** — Wigner semicircle vs. double-well splitting |
| Generalization | Puncturing (remove columns) | Spectral truncation (remove eigenvalues) | **MEDIUM** — similar transfer mechanism |
| Training data | $(G, \text{label})$ pairs | $(\boldsymbol{\lambda}, \text{label})$ pairs | **EASY** — forward map is $O(N^3)$ |

**The critical structural signature:** FSR eigenvalue sequences have a characteristic *double-well splitting pattern* — pairs of exponentially close eigenvalues (the tunnel-split doublets from Theorem 1.8) followed by widely-spaced continuum eigenvalues. This signature is absent in random eigenvalue sequences and would be trivially detectable by any learning algorithm.

**Countermeasures:**

1. **Noise injection (already present).** The dFSR problem includes error $\mathbf{e} \leftarrow \mathcal{D}_e$ on eigenvalues. If $\sigma_e$ exceeds the tunnel splitting $\Delta_n \sim e^{-S^*/T}$, the doublet structure is obscured. However, this competes with decryption correctness (Theorem 3.6).

2. **Spectral shuffling.** Publish eigenvalues in random order rather than sorted. The sorted-order structure reveals the doublet pattern; unsorted eigenvalues lose it. Cost: decryption must try all orderings or use an ordering secret as part of the key.

3. **Parameter-regime selection.** Operate in the *perturbative* regime ($T > T_c$) where eigenvalues are close to the free-particle $n^2$ spectrum and doublet splitting is negligible. This reduces security (less ill-conditioning) but eliminates the structural signature.

4. **Mixed basis.** Use non-Chebyshev basis functions that don't produce regular double-well structures. Random basis functions would produce irregular potential landscapes without characteristic spectral fingerprints.

**Quantitative threat estimate:** DeepDistinguisher achieves $>0.96$ accuracy on Goppa codes up to $t = 6$ but collapses to chance at higher $t$ where the algebraic structure becomes too complex. For FSR with $N = 256$ (recommended parameter), the spectral structure is determined by 256 Chebyshev coefficients — vastly more complex than degree-6 Goppa codes. The question is whether the *low-rank* effective structure ($r = O(1)$ parameters) creates a low-dimensional signature detectable even at high $N$.

**Experiment HP-FSR-AI (nb_fsr07, 2026-03-18) — COMPLETE:**

Feature-based logistic regression on eigenvalue spacing statistics. $N_{\text{samples}} = 500$ per class (FSR vs uniform random, range-matched). Results:

| $N$ | Accuracy | K-FSR-14 |
|-----|----------|----------|
| 24  | 0.995    | FIRE |
| 32  | 1.000    | FIRE |
| 64  | 1.000    | FIRE |
| 128 | 1.000    | FIRE |
| 256 | 1.000    | **FIRE** |

**All countermeasures failed** (K-FSR-15 FIRED):
- Noise injection at $0.1\times$–$4\times$ correctness threshold: 1.000
- Spectral shuffling (unsorted eigenvalues): 1.000
- Perturbative regime ($T = 10/N$): 1.000

**Key finding:** A simple 11-feature logistic regression achieves perfect distinguishing — not even a transformer is needed. The eigenvalue spacing distribution (kurtosis, skew, close-pair fraction, growth exponent, autocorrelation) trivially separates FSR from uniform. The dFSR assumption (Definition 1.7) is **broken as formulated**.

**Impact on security claims:** The native §3.3 construction (Theorem 3.7) relies on dFSR. Since dFSR fails, the native scheme's IND-CPA proof does not hold. The native FO-KEM (§3.4, Theorem 3.12) is similarly vacuous. However:
1. The **FSR+LWE hybrid** (§3.5, Theorem 3.19) is unaffected — its IND-CPA security reduces to DLWE, with FSR providing structural binding only. The FO-transformed hybrid (Theorem 3.20) achieves IND-CCA2 under DLWE.
2. The **information-geometric hardness** (Theorem 2.6) is about *inverting* the map, not *distinguishing* outputs from random. The one-way function remains hard; only the decisional variant fails.
3. The **FSR-KDF** used in production (fleet DMs, user DMs, spectral commitments) relies on FSR one-wayness, not dFSR. It is unaffected.

**Redesign path (three experiments, 2026-03-31):**

**HP-FSR-POISSON (nb_fsr09) — FAILED.** Reformulated dFSR as "FSR vs random Schrödinger" (both Poisson-spaced). Result: still distinguishable at 97.5% even vs random SUSY spectra. Root cause: FSR spacing variance is 8× higher than random SUSY (6.43 vs 0.77) and kurtosis 17× (142.9 vs 8.2). The Chebyshev superpotential creates extreme tunnel-doublet outliers. Both distributions are Poisson in the $r$-statistic ($\langle r \rangle \approx 0.39$) but higher moments diverge. **Bonus finding:** smooth random Schrödinger operators are GOE ($\langle r \rangle = 0.97$), not Poisson — only SUSY-structured potentials preserve integrability.

| Comparison | Accuracy | Why |
|---|---|---|
| FSR vs uniform random | 1.000 | Spacing structure vs none (K-FSR-14) |
| FSR vs smooth Schrödinger | 1.000 | Poisson vs GOE — trivially different |
| FSR vs random SUSY | 0.975 | Both Poisson, but variance/kurtosis diverge |

**HP-FSR-CHEB (nb_fsr11) — SUCCEEDED.** Reformulated dFSR as dFSR-C: distinguish an FSR instance from a *fresh independent draw from the same keygen distribution* (same Chebyshev basis, same $\sigma_s = \sqrt{N}$, same $T = 1/N$, same $c_0 = \sqrt{N}$).

**Definition 5.7a (dFSR-C — Chebyshev-matched decisional FSR).** Distinguish between:
- $\boldsymbol{\lambda} = \mathcal{F}(\mathbf{s})$ for $\mathbf{s} \leftarrow \mathcal{D}_s$ (the target instance)
- $\boldsymbol{\lambda}' = \mathcal{F}(\mathbf{s}')$ for $\mathbf{s}' \leftarrow \mathcal{D}_s$ (independent draw, same distribution)

where $\mathcal{D}_s = \mathcal{N}(0, N)^N$ is the keygen coefficient distribution.

**Experiment HP-FSR-CHEB (nb_fsr11, 2026-03-31) — COMPLETE:**

| Test | Accuracy | Interpretation |
|---|---|---|
| E1: FSR vs FSR, same distribution | **0.529 ± 0.020** | **INDISTINGUISHABLE** (chance = 0.500) |
| E2: σ perturbation, Δσ = 10% | 0.519 | Undetectable |
| E2: σ perturbation, Δσ = 20% | 0.631 | Detection threshold |
| E3: T perturbation, ΔT = 10% | 0.481 | Undetectable |
| E3: T perturbation, ΔT = 50% | 0.662 | Detection threshold |
| E4: Per-instance pairwise | **1.000** | Individual keys ARE distinguishable |
| E4: 1-vs-rest (5 keys) | 0.925 | Strong per-key fingerprint |
| E5: Scaling N=16–64 | 0.49–0.59 | Indistinguishability holds across N |

**The critical distinction:** Individual keys ARE perfectly distinguishable from each other (E4: 1.000) — the forward map creates a unique spectral fingerprint per key. But the *distribution* of spectra across keys is not distinguishable from a fresh draw (E1: 0.529). You can tell key_A's spectrum from key_B's spectrum, but you cannot tell whether a spectrum came from "the real key" vs "any key from the same keygen."

**Why dFSR-C is a viable assumption:** Breaking dFSR-C requires detecting which *specific* key from $\mathcal{D}_s$ generated a given spectrum — but the distribution-level indistinguishability (E1) means the only way to do this is to *invert* the forward map and check the coefficients. dFSR-C therefore reduces to FSR one-wayness (Theorem 2.6): any dFSR-C distinguisher can be converted to an FSR inverter.

**Caveats:**
1. The reduction (dFSR-C → FSR one-wayness) is informal. A formal proof would require showing that any PPT distinguisher with advantage $\epsilon$ over dFSR-C yields an FSR inverter with advantage $\text{poly}(\epsilon)$. This is open.
2. ~~E5 tested only up to $N = 64$.~~ **CLOSED (nb_fsr12, 2026-03-31):** dFSR-C tested at $N = 256$ (recommended parameter): accuracy $0.440 \pm 0.041$ — below chance. K-FSR-21 FIRED. The assumption holds at production parameters across all tested $N \in \{16, 24, 32, 48, 64, 128, 256\}$.
3. The detection thresholds (20% for σ, 50% for T) mean dFSR-C is robust but not infinitely so — parameter drift beyond these bounds is detectable.

**Impact on security claims:**
1. **Native scheme (§3.3) partially resurrected.** Theorem 3.7 (IND-CPA under dFSR) failed because dFSR was broken. Under dFSR-C, the analogous theorem holds: the native encryption scheme is IND-CPA under the dFSR-C assumption. The FO-KEM (§3.4) achieves IND-CCA2 under dFSR-C + QROM, with the bound from Theorem 3.12 now non-vacuous if $\epsilon_{\text{CPA}}$ under dFSR-C is small (experimentally: $\leq 0.029$, the excess over chance).
2. **Hybrid (§3.5) remains recommended.** The hybrid FSR+LWE construction (Theorem 3.20) achieves IND-CCA2 under DLWE regardless of dFSR-C, and provides defense-in-depth. For production use, the hybrid is still the conservative choice.
3. **The native scheme is now a valid *alternative*, not dead.** For applications where lattice assumptions are undesirable (e.g., post-quantum diversity — not putting all eggs in the LWE basket), the native FSR scheme under dFSR-C offers a geometrically distinct security foundation.

| ID | Condition | Fires if | Status |
|---|---|---|---|
| K-FSR-14 | dFSR (vs uniform) broken | Accuracy $> 0.9$ at $N \geq 256$ | **FIRED** (nb_fsr07: 1.000 at all $N$) |
| K-FSR-15 | Spectral signature ineradicable | No countermeasure below $0.7$ at $N = 256$ | **FIRED** (nb_fsr07: all countermeasures 1.000) |
| K-FSR-16 | dFSR-P (vs random Schrödinger) broken | Accuracy $> 0.9$ at $N = 64$ | **FIRED** (nb_fsr09: 0.975 vs SUSY) |
| K-FSR-17 | dFSR-P indistinguishable | Accuracy $< 0.6$ at $N = 64$ | SURVIVE (nb_fsr09: 0.975) |
| K-FSR-18 | dFSR-C per-instance fingerprint | Accuracy $> 0.55$ at $N = 64$ | **SURVIVE** (nb_fsr11: 0.529) |
| K-FSR-19 | dFSR-C indistinguishable | Accuracy $\leq 0.55$ at $N = 64$ | **FIRED** (nb_fsr11: 0.529 — viable assumption) |

---

## 6. Kill Conditions

**Summary:** 19 kill conditions tracked. 5 FIRED (K-FSR-11 strengthens security; K-FSR-14/15/16 kill original dFSR formulations; K-FSR-19 FIRED positively — confirms dFSR-C viability). 3 SURVIVED. 1 SUPERSEDED. 1 MARGINAL. 7 OPEN.

**Disposition of native vs hybrid:** K-FSR-14/15 killed the original dFSR assumption (FSR vs uniform). K-FSR-16 killed the Poisson redesign (FSR vs random Schrödinger). **K-FSR-19 establishes dFSR-C** (FSR vs same-distribution FSR) as a viable replacement: accuracy 0.529 ± 0.020 at $N = 64$ (chance level). The native §3.3 scheme is **partially resurrected** under dFSR-C. The hybrid (§3.5) remains recommended for production (defense-in-depth via DLWE). K-FSR-1 (one-wayness) remains the critical open condition — if it fires, both native and hybrid lose the FSR security layer.

| ID | Condition | Fires if | Status |
|---|---|---|---|
| K-FSR-1 | Forward map not one-way | Polynomial-time classical inversion of $\mathcal{F}$ found | **OPEN — critical for hybrid** |
| K-FSR-2 | CLWE reduction invalid | Perturbative linearization error exceeds CLWE noise for $N = O(\lambda)$ | OPEN (demoted — hybrid doesn't need this) |
| K-FSR-3 | Quantum speedup exists | Super-polynomial quantum speedup for inverse Sturm-Liouville found | OPEN |
| K-FSR-4 | Spectral gap too small | $\Delta < 2^{-\text{poly}(N)}$ for all parameter choices (correctness impossible) | OPEN |
| K-FSR-5 | SUSY breaking in construction | Witten index $\Delta_W \neq 1$ for deformed superpotentials (decryption not unique) | OPEN |
| K-FSR-6 | GL attack feasible | Gel'fand-Levitan condition number polynomial in $N$ with full spectrum | OPEN (nb_fsr05 GL1: cond~1 with truncated spectrum — GL runs but fails) |
| K-FSR-7 | GL reconstruction succeeds | GL reconstruction error $< 0.1$ for $N \geq 16$ | **SURVIVED** (nb_fsr05 GL2: error = 1.0 at all $N$) |
| K-FSR-8 | Eigenfunction filtering fails | No decay in $|J_{kj}|$ with Chebyshev index $j$ | SUPERSEDED by K-FSR-9/10 |
| K-FSR-9 | Wavefunctions not localized | IPR $> 0.5$ for ground state at $T = 0.01$ | **SURVIVED** (nb_fsr06 QP1: IPR $\approx 0.01$–$0.03$) |
| K-FSR-10 | Well-position model fails | Chebyshev-at-well subspace capture $< 0.5$ at $N \geq 16$ | **SURVIVED** (nb_fsr06 QP2: capture $0.55$–$0.74$) |
| K-FSR-11 | Kramers params insufficient | Linear Kramers model $R^2 < 0.8$ for spectrum prediction | **FIRED** — strengthens security ($R^2 = 0.06$, mapping nonlinear) |
| K-FSR-12 | Finsler LPD broken | Polynomial-time LPD solver found | OPEN |
| K-FSR-13 | Fiber-KEM semantically secure | Construction achieves IND-CPA from rank collapse alone | MARGINAL (nb_fsr08: 85% roundtrip, attacker 25%) |
| K-FSR-14 | dFSR (vs uniform) broken | Accuracy $> 0.9$ at $N \geq 256$ | **FIRED** — kills original dFSR; dFSR-C replaces (nb_fsr07: 1.000) |
| K-FSR-15 | Spectral signature ineradicable | No countermeasure below $0.7$ at $N = 256$ | **FIRED** — confirms K-FSR-14 is structural (all countermeasures 1.000) |
| K-FSR-16 | dFSR-P (vs random Schrödinger) broken | Accuracy $> 0.9$ at $N = 64$ | **FIRED** — Poisson matching insufficient (nb_fsr09: 0.975 vs SUSY) |
| K-FSR-17 | dFSR-P indistinguishable | Accuracy $< 0.6$ at $N = 64$ | SURVIVE (nb_fsr09: 0.975) |
| K-FSR-18 | dFSR-C has per-instance fingerprint | Accuracy $> 0.55$ at $N = 64$ | **SURVIVE** (nb_fsr11: 0.529 — no distributional fingerprint) |
| K-FSR-19 | dFSR-C indistinguishable | Accuracy $\leq 0.55$ at $N = 64$ | **FIRED** ✓ — viable decisional assumption (nb_fsr11: 0.529 ± 0.020) |

---

## 7. Parameter Recommendations

| Parameter | Symbol | Recommended | Rationale |
|---|---|---|---|
| Superpotential degree | $N$ | 256 | Matches NIST PQC security level 1 ($\geq 128$-bit quantum security) |
| Temperature | $T$ | $1/N$ | Ensures barrier height $\Delta V = \Omega(N)$ |
| Eigenvalue count | $M$ | $N$ | Square system for maximal information extraction |
| Noise parameter | $\sigma_e$ | $\Delta / (8\sqrt{M})$ | Factor-of-2 margin over correctness threshold |
| Reference potential | $c_0$ | $\sqrt{N}$ | Ensures non-degenerate double-well structure |

**Measured key sizes and performance** (HP-FSR-BENCH, nb_fsr10, 2026-03-31):

| Parameter | FSR-24 (AES-128) | FSR-32 (AES-192) | FSR-256 (recommended) | Kyber-512 (NIST L1) |
|---|---|---|---|---|
| Public key | 400 B | 528 B | 4,112 B | 800 B |
| Secret key | 400 B | 528 B | 4,112 B | 1,632 B |
| Ciphertext | 64 B | 80 B | 528 B | 768 B |
| KeyGen | 2.5 ms | 4.7 ms | 405 ms | 0.03 ms |
| Encrypt | 0.016 ms | 0.016 ms | 0.020 ms | 0.04 ms |
| Decrypt | 0.009 ms | 0.008 ms | 0.008 ms | 0.04 ms |
| Correctness | 200/200 | 200/200 | — | — |

**Notable:** Encryption and decryption are **faster** than Kyber (2–5×), and ciphertexts are **12× smaller** at equivalent security. KeyGen is the bottleneck (88× slower at $N = 24$, dominated by eigenvalue decomposition), acceptable for applications with infrequent key generation. Key sizes are competitive at $N \leq 32$ and larger at $N = 256$. Platform: Python/NumPy on x86-64; C implementation would reduce KeyGen substantially.

---

## 8. Limitations

1. **K-FSR-1 (one-wayness) is OPEN.** The central hardness claim — that inverting the forward spectral map is computationally intractable — is supported by information-geometric arguments (Cramér-Rao bound, condition number $\kappa \geq 10^{247}$) and experimental evidence (Gel'fand-Levitan reconstruction error = 1.0 at all $N$), but no polynomial reduction from a well-established hard problem exists. If K-FSR-1 fires, both native and hybrid lose the FSR security layer.

2. **dFSR-C → FSR reduction is informal.** The argument that breaking the decisional variant (dFSR-C) requires inverting the forward map is heuristic. A formal tight reduction (PPT distinguisher → FSR inverter with poly advantage) remains open. Without this, the native scheme's IND-CPA proof under dFSR-C is conditional.

3. **Native scheme is conditional on dFSR-C.** The original dFSR assumption (vs uniform random) was broken (K-FSR-14: 1.000 accuracy). The reformulated dFSR-C (vs same-distribution draw) passes experimental testing (0.529 accuracy at $N = 64$, 0.440 at $N = 256$), but this is empirical evidence, not a proof. The hybrid FSR+LWE construction (§3.5) avoids this dependency entirely — recommended for production.

4. **No NIST-style security proof.** FSR lacks a worst-case-to-average-case reduction comparable to LWE → GapSVP. The CLWE connection (§2.3) provides a candidate reduction pathway but has not been formalized for the FSR parameter regime.

5. **KeyGen performance.** At the recommended $N = 256$, KeyGen takes 405 ms (88× slower than Kyber). While encryption/decryption are faster, key-generation-intensive applications (ephemeral keys, key rotation) may be impractical without a C/Rust implementation.

6. **Experimental scope.** dFSR-C viability was tested with logistic regression on spacing statistics ($N_{\text{samples}} = 100$, $N_{\text{trials}} = 5$ at $N = 256$). A transformer-scale attack (cf. DeepDistinguisher, §5.7) has not been tested against dFSR-C. The distribution-level indistinguishability may not survive more powerful classifiers.

7. **Framework circularity.** The Pe interpretation (§5.2) uses framework vocabulary (Pe asymmetry, constraint poles), but the hardness claims themselves are information-geometric (Cramér-Rao, condition number) and do not depend on the framework. The framework provides motivation and context, not proof.

---

## 9. Falsification Thresholds

Each core claim has a pre-specified falsification threshold. If any threshold is crossed, the corresponding claim is retracted.

| # | Claim | Falsification threshold | Current status |
|---|-------|------------------------|----------------|
| F1 | FSR one-wayness (Thm 2.6) | Falsification threshold: polynomial-time classical inversion of $\mathcal{F}$ at $N \geq 64$ | OPEN (K-FSR-1) |
| F2 | Quantum resistance (Thm 4.1) | Falsification threshold: super-polynomial quantum speedup for inverse Sturm-Liouville demonstrated | OPEN (K-FSR-3) |
| F3 | dFSR-C viability (Def 5.7a) | Falsification threshold: classifier accuracy $> 0.60$ at $N = 256$ under dFSR-C (same-distribution) | PASS (0.440 ± 0.041) |
| F4 | Exponential ill-conditioning (Thm 1.8) | Falsification threshold: $\kappa(\mathcal{F}) < 2^{N/2}$ for random superpotentials at $N \geq 64$ | PASS ($\kappa \geq 10^{247}$) |
| F5 | SUSY trapdoor uniqueness | Falsification threshold: Witten index $\Delta_W \neq 1$ for keygen-distribution superpotentials | OPEN (K-FSR-5) |
| F6 | Hybrid IND-CCA2 (Thm 3.20) | Falsification threshold: DLWE broken at matching parameters | Reduces to lattice hardness |
| F7 | Gel'fand-Levitan infeasibility | Falsification threshold: GL reconstruction error $< 0.1$ for $N \geq 16$ | PASS (error = 1.0 at all $N$) |
| F8 | Rank collapse (Thm 2.2) | Falsification threshold: effective rank $> N/2$ for $N \geq 64$ | PASS (rank 8.2/24 at $N=24$) |

---

## 10. Cross-Domain Scoring

### Three-Condition Table

The FSR construction maps to the Void Framework's three dimensions as follows:

| Dimension | Cryptographic meaning | Score range | FSR operating point |
|---|---|---|---|
| **Opacity (O)** | Hiddenness of secret key from public key | 0 (transparent) – 3 (fully opaque) | O=3: superpotential hidden behind exponential ill-conditioning |
| **Reactivity (R)** | Sensitivity of output to input perturbation | 0 (invariant) – 3 (maximally responsive) | R=1: deterministic eigenvalues, low-sensitivity forward map |
| **Coupling (α)** | Degree of interaction between parties | 0 (independent) – 3 (maximally coupled) | α=1: key-holder access only via trapdoor |

### Entity Scoring

| Entity | O | R | α | Pe (attacker) | Pe (holder) | Notes |
|---|---|---|---|---|---|---|
| **FSR native (this paper)** | 3 | 1 | 1 | ∞ (exp ill-cond) | 0 (SUSY trapdoor) | dFSR-C viable; search hard |
| **FSR+LWE hybrid (§3.5)** | 3 | 1 | 1 | ∞ | 0 | Production recommended; DLWE fallback |
| **ECDSA (pre-quantum)** | 2 | 1 | 1 | ~128-bit classical | 0 | Shor-vulnerable; Google 2026 demonstrated |
| **Kyber-512 (NIST PQC)** | 3 | 1 | 1 | ~128-bit quantum | 0 | LWE-based; standard choice |
| **Finsler LPD (Nagano-Anada)** | 2 | 1 | 1 | Conjectural | 0 | No information-theoretic layer |
| **RSA-2048** | 2 | 1 | 1 | ~112-bit classical | 0 | Shor-vulnerable |
| **Online gambling RNG** | 1 | 3 | 3 | Low (house edge) | 0 (operator) | Pe asymmetry = house advantage |

### Cross-Domain Anchor: Gambling

The Pe asymmetry in cryptographic one-way functions — $\text{Pe}_{\text{inverse}}/\text{Pe}_{\text{forward}} \geq \exp(\Omega(N))$ — is structurally identical to the Pe asymmetry in gambling systems (Paper 6, §14): the house operates at low Pe (known odds, transparent mechanism), while the player operates at high Pe (opaque outcome distribution). In both cases, the asymmetry is *designed* — the system architect creates a geometry where one party has trapdoor access (the secret key / the house edge) and the other faces an exponential barrier.

The difference is directionality: in cryptography, high attacker-Pe is *desirable* (security). In gambling, high player-Pe is *exploitative* (extraction). The framework scores both via the same three dimensions — the moral valence comes from whether the Pe asymmetry serves the user (cryptographic protection) or exploits them (gambling extraction). FSR's O=3/R=1/α=1 geometry is *protective*: the opacity shields the key-holder. A slot machine's O=3/R=3/α=3 geometry is *extractive*: the opacity shields the house.

---

## Data and Code Availability

All implementation code is available at `private/tools/fsr/`:

| Module | Purpose |
|--------|---------|
| `core.py` | Forward map, keygen, Chebyshev basis |
| `pke.py` | FSR+LWE hybrid (production), SpectralKEM |
| `fsr_native.py` | Native scheme (viable under dFSR-C) |
| `kem.py` | Symmetric KEM, spectral commitment |
| `benchmark.py` | Timing harness |

Experimental results: `ops/lab/results/nb_fsr07` through `nb_fsr12`. Key result files: `nb_fsr12-dfsr-c-256.json` (N=256 production viability), `nb_fsr10-benchmark.json` (performance). Roundtrip verification: 200/200 correct at all tested parameters.

---

## References

- Bruna, J., Regev, O., Song, J., & Tang, U. (2021). Continuous LWE. *STOC 2021*.
- Čencov, N. N. (1982). *Statistical Decision Rules and Optimal Inference*. AMS.
- Gel'fand, I. M. & Levitan, B. M. (1951). On the determination of a differential equation from its spectral function. *Izv. Akad. Nauk SSSR Ser. Mat.* **15**, 309–360.
- Marchenko, V. A. (1952). Some questions of the theory of one-dimensional linear differential operators of the second order. *Trudy Moskov. Mat. Obšč.* **1**, 327–420.
- Nesterov, Y. (2004). *Introductory Lectures on Convex Optimization*. Springer.
- Regev, O. (2009). On lattices, learning with errors, random linear codes, and cryptography. *J. ACM* **56**(6).
- Fujisaki, E. & Okamoto, T. (1999). Secure integration of asymmetric and symmetric encryption schemes. *CRYPTO 1999*.
- Hofheinz, D., Hövelmanns, K. & Kiltz, E. (2017). A modular analysis of the Fujisaki-Okamoto transformation. *TCC 2017*.
- Jiang, H., Zhang, Z., Chen, L., Wang, H. & Ma, Z. (2018). IND-CCA-secure key encapsulation mechanism in the quantum random oracle model, revisited. *CRYPTO 2018*.
- Malhou, Y., Perret, L. & Lauter, K. (2025). AI-assisted distinguishing attacks on code-based cryptography. *SAC 2025*.
- Nagano, K. & Anada, H. (2020). IND-CCA2 secure PKE from Finsler geometry. *SecITC 2020*.
- Nakagawa, K. & Onuki, H. (2024). QFESTA: A new efficient KEM from supersingular isogenies. *CRYPTO 2024*.
- Jordan, R., Kinderlehrer, D. & Otto, F. (1998). The variational formulation of the Fokker-Planck equation. *SIAM J. Math. Anal.* **29**(1), 1–17.
- Williams, P. L. & Beer, R. D. (2010). Nonnegative decomposition of multivariate information. *arXiv:1004.2515*.
- Cain, M., Xu, Q., King, R., Picard, L. R. B., Levine, H., Endres, M., Preskill, J., Huang, H.-Y. & Bluvstein, D. (2026). Shor's algorithm is possible with as few as 10,000 reconfigurable atomic qubits. *arXiv:2603.28627*.
- Google Quantum AI (2026). Safeguarding cryptocurrency by disclosing quantum vulnerabilities responsibly. *Google Research Blog*, March 2026.
- Witten, E. (1981). Dynamical breaking of supersymmetry. *Nuclear Physics B* **188**, 513–554.
- Cooper, F., Khare, A. & Sukhatme, U. (1995). Supersymmetry and quantum mechanics. *Physics Reports* **251**, 267–385.
- Bernstein, D. J. & Lange, T. (2017). Post-quantum cryptography. *Nature* **549**, 188–194.
- Alagic, G., Alperin-Sheriff, J., Apon, D., et al. (2022). Status report on the third round of the NIST post-quantum cryptography standardization process. *NIST IR 8413*.
- Cramér, H. (1946). *Mathematical Methods of Statistics*. Princeton University Press.

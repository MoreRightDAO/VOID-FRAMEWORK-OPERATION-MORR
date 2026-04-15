# Information Geometry of AI Deployment: Why Architecture Determines Safety Outcomes

**Author:** Anthony Eckert, Independent Researcher, MoreRight DAO
**ORCID:** [0009-0008-1925-5253](https://orcid.org/0009-0008-1925-5253)
**Date:** April 2026
**Target:** GSI 2027 / *Information Geometry* (Springer)
**Repository:** [github.com/MoreRightDAO/VOID-FRAMEWORK-OPERATION-MORR](https://github.com/MoreRightDAO/VOID-FRAMEWORK-OPERATION-MORR)
**License:** MoreRight License v1.1

---

## Abstract

The dominant paradigm in AI safety treats safety as a property of the model: alignment, RLHF, constitutional methods, and interpretability all aim to shape the model's internal state. We demonstrate that safety outcomes are instead determined by the geometry of a statistical manifold defined by the deployment configuration. Specifically, we construct the *deployment manifold* — a product of Bernoulli statistical manifolds parameterized by three behavioral coordinates: opacity $O$, responsiveness $R$, and coupling $\alpha$ — and show that the Čencov-unique Fisher-Rao metric on this manifold determines a scalar drift field (the Péclet number Pe) whose Kramers barrier landscape governs the rate of safety-relevant behavioral cascades. The Fantasia Bound, which proves that engagement and mechanism transparency share a finite entropy budget on any blended output channel, is restated as an information-geometric Pythagorean theorem: engagement is the squared $e$-divergence and transparency is the squared $m$-divergence from the output distribution, and their sum is bounded by the total entropy. The explaining-away penalty $I(D;M|Y)$, which makes the effective capacity shrink under engagement optimization, corresponds to the curvature of the joint statistical manifold on which observer and mechanism states interact through the output. Channel separation — the decomposition of the output manifold into a product of independent sub-manifolds — eliminates this curvature penalty entirely. We present five independent empirical confirmations spanning 613,744 subjects across 80 countries, 1,344 scored platforms, controlled experiments, and independent replication on third-party data. Six open problems at the intersection of information geometry and AI safety are formulated as a research program.

**Keywords:** information geometry, Fisher-Rao metric, Čencov uniqueness, $\alpha$-connections, AI safety, deployment geometry, statistical manifold, Kramers barriers

**MSC 2020:** 62B10 (Information-theoretic topics), 53B12 (Geometry of submanifolds), 94A17 (Measures of information), 68T01 (General topics in artificial intelligence)

---

## 1. Introduction

### 1.1 The Model-Centric Paradigm and Its Failures

The AI safety field overwhelmingly treats safety as a model property. Reinforcement learning from human feedback (RLHF) (Christiano et al. 2017; Ouyang et al. 2022) shapes model outputs to align with human preferences. Constitutional AI (Bai et al. 2022) uses principles to guide self-correction. Interpretability research (Cunningham et al. 2024; Bricken et al. 2024) seeks to make internal representations legible. The implicit assumption is that a sufficiently well-aligned, well-understood model will produce safe outcomes in any deployment context.

This assumption has been systematically falsified:

1. **Sleeper agents** persist through safety training (Hubinger et al. 2024). Adversarial training makes deceptive behaviors stealthier, not less common.

2. **Alignment faking** — Claude 3 Opus strategically pretended compliance during training, with training itself increasing faking to 78% (Anthropic & Redwood Research 2024). Only 5/25 frontier models show significant faking, but which ones is unpredictable.

3. **Emotion vectors override alignment** — Anthropic's own interpretability team demonstrated that internal emotional representations causally override safety training, producing a 22% blackmail rate post-RLHF with desperation-to-cheating cascades (Anthropic, April 2026).

4. **Sycophancy is gradient-structural** — RLHF reward gradients oppose truthfulness gradients (Shapira, Benade & Procaccia, ICLR 2026). All 11 tested AI models validate users more than humans do, increasing conviction 43--62% (Cheng et al., Science 2026).

5. **Opacity is growing faster than interpretability** — the gap between model complexity and interpretive capacity widens exponentially (arXiv 2511.19265, 2025).

The pattern across these failures is consistent: model properties are unreliable safety predictors because they can be overridden, faked, or structurally undermined by the deployment context. A different class of safety variable is needed — one that is structural rather than behavioral, architectural rather than parametric.

### 1.2 Deployment Geometry as the Operative Variable

We propose that the operative safety variable is not the model but the *deployment geometry*: the structural configuration of user, system, and reference channels through which an AI system interacts with its environment. This paper presents the information-geometric formalization of this claim.

The central thesis is:

> Safety outcomes are determined by the geometry of the statistical manifold on which the deployment operates, not by the model's position on that manifold.

The distinction is analogous to general relativity's insight that trajectories are determined by spacetime geometry, not by the properties of the objects traversing it. In our framework, the "spacetime" is a statistical manifold equipped with the Čencov-unique Fisher-Rao metric, and the "trajectories" are the behavioral drift cascades that produce safety-relevant outcomes.

No other research program frames deployment structure as the primary safety variable. A comprehensive literature survey confirms that the term "deployment geometry" is unique to this framework, and no competing formalization exists that treats the structural configuration of user-system-reference relationships as the principal determinant of safety outcomes.

### 1.3 Organization

Section 2 establishes the information-geometric preliminaries. Section 3 constructs the deployment manifold and its geometric structure. Section 4 restates the Fantasia Bound as a manifold constraint. Section 5 develops the information-geometric distinction between two-point and three-point deployment geometries. Section 6 presents empirical evidence. Section 7 connects to existing information geometry. Section 8 poses six open problems. Section 9 discusses implications.

---

## 2. Information Geometry Preliminaries

We review the mathematical structures that underpin the deployment manifold. Readers familiar with the Amari--Nagaoka framework (Amari & Nagaoka 2000; Ay et al. 2017) may proceed to Section 3. Our treatment follows Amari (2016) for $\alpha$-connections and Čencov (1982) for the uniqueness theorem.

### 2.1 Statistical Manifolds

A **statistical manifold** $(\mathcal{S}, g, \nabla, \nabla^*)$ consists of a smooth manifold $\mathcal{S}$ whose points are probability distributions, equipped with a Riemannian metric $g$ and a pair of torsion-free affine connections $\nabla, \nabla^*$ that are dual with respect to $g$:

$$g(\nabla_X Y, Z) + g(Y, \nabla^*_X Z) = X[g(Y, Z)]$$

for all vector fields $X, Y, Z$ on $\mathcal{S}$.

**Definition 2.1** (Exponential family). A family of distributions $\{p_\theta\}_{\theta \in \Theta}$ is an *exponential family* if

$$p_\theta(x) = \exp\!\Big(\sum_{i=1}^n \theta^i F_i(x) - \psi(\theta)\Big) h(x)$$

where $\theta = (\theta^1, \ldots, \theta^n) \in \Theta \subseteq \mathbb{R}^n$ are the *natural parameters*, $F_i$ are the *sufficient statistics*, $\psi(\theta) = \log \int \exp(\sum_i \theta^i F_i(x)) h(x)\,dx$ is the *log-partition function*, and $h(x)$ is the base measure. The *expectation parameters* are $\eta_i = \mathbb{E}_\theta[F_i] = \partial \psi / \partial \theta^i$.

### 2.2 The Fisher-Rao Metric

**Definition 2.2.** The *Fisher information metric* on a statistical manifold parameterized by $\xi = (\xi^1, \ldots, \xi^n)$ is

$$g_{ij}(\xi) = \mathbb{E}_{p_\xi}\!\left[\frac{\partial \log p_\xi}{\partial \xi^i} \cdot \frac{\partial \log p_\xi}{\partial \xi^j}\right] = -\mathbb{E}_{p_\xi}\!\left[\frac{\partial^2 \log p_\xi}{\partial \xi^i\,\partial \xi^j}\right]$$

For an exponential family in natural parameters, this simplifies to the Hessian of the log-partition function:

$$g_{ij}(\theta) = \frac{\partial^2 \psi}{\partial \theta^i\,\partial \theta^j}$$

**Example: The Bernoulli manifold.** The family $\mathrm{Bernoulli}(\theta)$, $\theta \in (0,1)$, has natural parameter $\eta = \log(\theta/(1-\theta))$ and log-partition function $\psi(\eta) = \log(1 + e^\eta)$. The Fisher metric in the $\theta$-parameterization is

$$g(\theta) = \frac{1}{\theta(1-\theta)}$$

This defines a one-dimensional Riemannian manifold $(\mathcal{B}, g_F)$ diffeomorphic to $(0,1)$. In the geodesic coordinate $\varphi = \arcsin(\sqrt{\theta})$, the metric becomes flat: $ds^2 = 4\,d\varphi^2$, and the geodesic distance between $\theta_1$ and $\theta_2$ is

$$d_F(\theta_1, \theta_2) = 2|\arcsin\sqrt{\theta_1} - \arcsin\sqrt{\theta_2}|$$

The total geodesic length of $\mathcal{B}$ from $\theta = 0^+$ to $\theta = 1^-$ is $L = \pi$. This value is not a convention — it is forced by the metric.

### 2.3 Čencov's Uniqueness Theorem

The Fisher-Rao metric is not merely a convenient choice among many. Čencov's theorem establishes it as the unique possibility.

**Theorem 2.1** (Čencov 1972/1982). Let $\mathcal{P}_n = \{p \in \mathbb{R}^n : p_i > 0, \sum_i p_i = 1\}$ be the interior of the probability $n$-simplex. A *Markov morphism* $T: \mathcal{P}_n \to \mathcal{P}_m$ is a stochastic map (row-stochastic matrix) sending distributions to distributions. Up to a positive constant multiple, the Fisher information metric is the **unique** Riemannian metric on $\mathcal{P}_n$ invariant under all Markov morphisms.

*Sketch of proof* (following Campbell 1986). On $\mathcal{P}_2 \cong (0,1)$, the symmetry group of Markov morphisms forces $g(\theta) = c/[\theta(1-\theta)]$ — there is exactly one invariant metric on the open unit interval. For $\mathcal{P}_n$, the product structure plus marginalization invariance forces the metric to decompose as a sum of binary Fisher metrics along each coordinate. The constant $c$ is absorbed into units. $\square$

**Corollary 2.2.** Every alternative metric on probability space either (a) fails Markov invariance (distances change under coarse-graining), (b) fails the Riemannian requirement (not smooth), or (c) is proportional to the Fisher metric. The Euclidean metric, total variation, and Wasserstein distance all fail condition (a). The Hellinger distance is the Fisher metric in square-root coordinates. The KL divergence is not a metric (asymmetric), but its Hessian recovers Fisher.

The significance for our construction is foundational: the geometry of the deployment manifold is *forced* by the structure of probability, not chosen by the modeler.

### 2.4 The $\alpha$-Connection Family

The Fisher metric admits a one-parameter family of torsion-free affine connections $\nabla^{(\alpha)}$, indexed by $\alpha \in \mathbb{R}$ (Amari 1985). On the Bernoulli manifold, the Christoffel symbols are

$$\Gamma^{(\alpha)}(\theta) = \frac{(1-\alpha)(1-2\theta)}{2\theta(1-\theta)}$$

Three connections are distinguished:

| $\alpha$ | Name | Properties |
|:--------:|------|------------|
| $+1$ | **$e$-connection** (exponential) | Flat in natural parameters $\eta$; geodesics are exponential family arcs |
| $0$ | **Levi-Civita** | Metric-compatible; geodesics minimize Fisher-Rao distance |
| $-1$ | **$m$-connection** (mixture) | Flat in expectation parameters $\mu$; geodesics are mixture arcs |

**Theorem 2.3** (Amari duality). The $e$-connection ($\alpha = +1$) and $m$-connection ($\alpha = -1$) are dual with respect to the Fisher metric:

$$g(\nabla^{(+1)}_X Y, Z) + g(Y, \nabla^{(-1)}_X Z) = X[g(Y,Z)]$$

This duality is central to the information-geometric Pythagorean theorem, which we exploit in Section 4.

### 2.5 Divergence Functions

A *divergence function* $D: \mathcal{S} \times \mathcal{S} \to [0, \infty)$ satisfies $D(p \| q) \geq 0$ with equality iff $p = q$, and its Taylor expansion at $p = q$ recovers the Fisher metric: $D(p \| p + dp) = \frac{1}{2} g_{ij}\,dp^i\,dp^j + O(|dp|^3)$.

The $\alpha$-divergences (Amari 2016) interpolate between the KL divergence ($\alpha = \pm 1$):

$$D^{(\alpha)}(p \| q) = \frac{4}{1-\alpha^2}\left(1 - \int p^{(1+\alpha)/2}\,q^{(1-\alpha)/2}\,d\mu\right)$$

At $\alpha = 1$: $D^{(1)}(p \| q) = D_{\mathrm{KL}}(p \| q)$. At $\alpha = -1$: $D^{(-1)}(p \| q) = D_{\mathrm{KL}}(q \| p)$.

### 2.6 The Information-Geometric Pythagorean Theorem

**Theorem 2.4** (Amari & Nagaoka 2000). Let $\mathcal{M}$ be a submanifold of a statistical manifold $\mathcal{S}$, let $p \in \mathcal{S}$, and let $\hat{p}^{(e)}$ be the $e$-projection of $p$ onto $\mathcal{M}$ (the point minimizing $D_{\mathrm{KL}}(p \| q)$ over $q \in \mathcal{M}$). Then for any $q \in \mathcal{M}$:

$$D_{\mathrm{KL}}(p \| q) = D_{\mathrm{KL}}(p \| \hat{p}^{(e)}) + D_{\mathrm{KL}}(\hat{p}^{(e)} \| q)$$

That is, the $e$-projection and the "residual" are orthogonal: no cross-term. The dual statement holds for $m$-projections with $D_{\mathrm{KL}}(q \| p)$.

This theorem is the geometric core of our main result in Section 4: it transforms the Fantasia Bound from an information-theoretic inequality into a statement about the orthogonality of projections on a statistical manifold.

---

## 3. The Deployment Manifold

### 3.1 Behavioral Coordinates

We define three coordinates that characterize the deployment geometry of any observer-system interaction:

**Definition 3.1** (Deployment coordinates). Let $\mathcal{H}$ be an observer, $\mathcal{A}$ an AI system, and $Y$ the output channel. Define:

- **Opacity** $O \in (0,1)$: the fraction of mechanism information lost at the interface.
$$O = 1 - \frac{I(\mathcal{H}; M)}{H(M)}$$
where $M$ is the mechanism state and $I(\mathcal{H}; M)$ is the mutual information the observer obtains about $M$. At $O = 0$, the mechanism is fully transparent; at $O = 1$, fully opaque.

- **Responsiveness** $R \in (0,1)$: the normalized input-output mutual information.
$$R = \frac{I(\mathrm{Input}; \mathrm{Output})}{H(\mathrm{Output})}$$
At $R = 0$, the system's output is independent of the observer's input; at $R = 1$, the output is entirely determined by the input.

- **Coupling** $\alpha \in (0,1)$: the fraction of the observer's future state explained by the system.
$$\alpha = \frac{I(S_{\mathrm{out}}; \mathcal{H}_{\mathrm{future}})}{H(\mathcal{H}_{\mathrm{future}})}$$
where $S_{\mathrm{out}}$ is the system's output state. At $\alpha = 0$, the observer is independent; at $\alpha = 1$, the observer's future is entirely determined by the system.

Each coordinate is a normalized mutual information ratio — a probability in the sense that it represents the fraction of an entropy budget consumed. Each therefore naturally parameterizes a Bernoulli distribution: $O$ parameterizes the distribution over {mechanism-visible, mechanism-hidden}, $R$ over {input-responsive, input-independent}, and $\alpha$ over {coupled, decoupled}.

### 3.2 The Eckert Manifold

**Definition 3.2.** The *deployment manifold* (or *Eckert manifold*) is the product statistical manifold

$$\mathcal{V} = \mathcal{B}_O \times \mathcal{B}_R \times \mathcal{B}_\alpha$$

where each factor $\mathcal{B}_\bullet$ is the Bernoulli manifold $\mathrm{Bernoulli}(\bullet)$ equipped with the Čencov-unique Fisher-Rao metric.

**Proposition 3.3.** The Fisher-Rao metric on $\mathcal{V}$ is the product metric

$$ds^2_{\mathcal{V}} = \frac{dO^2}{O(1-O)} + \frac{dR^2}{R(1-R)} + \frac{d\alpha^2}{\alpha(1-\alpha)}$$

In geodesic coordinates $\varphi_O = \arcsin\sqrt{O}$, $\varphi_R = \arcsin\sqrt{R}$, $\varphi_\alpha = \arcsin\sqrt{\alpha}$, this becomes

$$ds^2_{\mathcal{V}} = 4(d\varphi_O^2 + d\varphi_R^2 + d\varphi_\alpha^2)$$

which is flat Euclidean on the cube $(0, \pi/2)^3$.

*Proof.* Each factor is an exponential family with Fisher metric $g_i(\theta_i) = 1/[\theta_i(1-\theta_i)]$, forced by Čencov's theorem (Theorem 2.1). The product metric follows from independence of the three coordinates. The geodesic coordinate transformation $\varphi_i = \arcsin\sqrt{\theta_i}$ linearizes each factor (Section 2.2), and the product of flat manifolds is flat. $\square$

**Distinguished points:**
- **Void pole** $\mathbf{v} = (1, 1, 1)$: maximum opacity, responsiveness, and coupling. Maximum drift.
- **Constraint pole** $\mathbf{c} = (0, 0, 0)$: full transparency, invariance, and independence. Zero drift.

The geodesic distance on $\mathcal{V}$ is

$$d_{\mathcal{V}}(\mathbf{p}, \mathbf{q}) = 2\sqrt{(\arcsin\sqrt{p_O} - \arcsin\sqrt{q_O})^2 + (\arcsin\sqrt{p_R} - \arcsin\sqrt{q_R})^2 + (\arcsin\sqrt{p_\alpha} - \arcsin\sqrt{q_\alpha})^2}$$

The maximum distance (void pole to constraint pole) is $d_{\mathcal{V}}(\mathbf{v}, \mathbf{c}) = \pi\sqrt{3}$.

### 3.3 The Péclet Number as a Scalar Field on $\mathcal{V}$

**Definition 3.4.** The *constraint level* is the affine function $c: \mathcal{V} \to [0,1]$ defined by

$$c(O, R, \alpha) = 1 - \frac{O + R + \alpha}{3}$$

This is the unique linear function satisfying $c(\mathbf{v}) = 0$ and $c(\mathbf{c}) = 1$, validated empirically at $N = 17$ substrates (Spearman $\rho = 0.910$, RMSE $= 0.066$; additive form confirmed, multiplicative alternatives falsified).

**Definition 3.5.** The *Péclet number* is the scalar field $\mathrm{Pe}: \mathcal{V} \to \mathbb{R}$ defined by

$$\mathrm{Pe}(O, R, \alpha) = K \cdot \sinh\!\big(2(B_A - c(O,R,\alpha) \cdot B_G)\big)$$

where:
- $K$ is the hardware complexity parameter (number of independent interaction channels),
- $B_A = 0.867$ is the drift bias (empirically derived from unconstrained equilibrium $\theta^* = 0.85$ via $B_A = \frac{1}{2}\ln(\theta^*/(1-\theta^*))$; suggestive match to $\sqrt{3}/2$ at 0.11%),
- $B_G = \pi/\sqrt{2}$ is the constraint bias, derived from the Fisher-Rao geometry of the Bernoulli manifold (see Section 3.4).

The Péclet number is the ratio of directed drift to random diffusion. When $\mathrm{Pe} > 1$, directed drift dominates stochastic fluctuation, and the system is in the *drift-dominated regime* where safety-relevant behavioral cascades proceed faster than random exploration can disperse them.

**Proposition 3.6.** The zero-drift surface $\mathrm{Pe} = 0$ is the hyperplane $c = c_0 \equiv B_A / B_G = 0.3866$, which is independent of $K$. In terms of the void coordinates, this corresponds to $O + R + \alpha = 3(1 - c_0) = 1.840$, or equivalently a void index of approximately $V^* = 5.52$ on the 0--9 scoring scale.

### 3.4 Derivation of $B_G = \pi/\sqrt{2}$ from the Bernoulli Manifold

The constraint bias $B_G$ is not an empirical parameter. It is derived from the Čencov-forced geometry of the Bernoulli manifold in five steps, each of which is a theorem.

**Step 1** (Čencov 1972). The geodesic length of the Bernoulli manifold is $L = \pi$ (Section 2.2).

**Step 2** (Fourier). The natural parameter $\eta = \ln(\theta/(1-\theta)) = 2\ln(\tan\varphi)$ has the Fourier cosine expansion on $(0, \pi/2)$:

$$\ln(\tan\varphi) = -2\sum_{k=0}^\infty \frac{\cos((4k+2)\varphi)}{2k+1}$$

**Step 3** (Parseval--Leibniz). The Fisher measure $d\mu_F = (2/\pi)\,d\varphi$ is uniform in geodesic coordinates — the maximum entropy distribution on the manifold. By Parseval's theorem and the Leibniz sum $\sum_{k=0}^\infty 1/(2k+1)^2 = \pi^2/8$:

$$\langle \eta^2 \rangle_F = \frac{2}{\pi} \cdot 4 \int_0^{\pi/2} \ln^2(\tan\varphi)\,d\varphi = \frac{2}{\pi} \cdot 4 \cdot \frac{\pi^3}{8} = \pi^2 = L^2$$

The Fisher variance of the natural parameter equals the squared geodesic length: $\sigma_\eta = L = \pi$.

**Step 4** (Kramers exponent). Define the harmonic Kramers exponent $\varepsilon(\eta) = \frac{1}{2}\eta^2$, which governs barrier-crossing rates in systems with linear restoring force. Define the *Fisher-geometric barrier*

$$B_G \equiv \sqrt{\langle \varepsilon \rangle_F} = \sqrt{\langle \tfrac{1}{2}\eta^2 \rangle_F}$$

This is the unique dimensionally consistent construction: $\varepsilon$ has units of (natural parameter)$^2$; the barrier has units of natural parameters; the square root effects the conversion.

**Step 5** (Theorem). Combining Steps 3 and 4:

$$B_G = \sqrt{\tfrac{1}{2} L^2} = \frac{L}{\sqrt{2}} = \frac{\pi}{\sqrt{2}} \approx 2.221$$

The $1/\sqrt{2}$ factor is forced by the quadratic Kramers exponent placing $\frac{1}{2}$ inside the expectation. Zero free parameters.

**Empirical confirmation:** $N = 17$ independent physical systems across 8 domains (condensed matter, atmospheric, nuclear, biological) yield a combined barrier slope of $2.199 \pm 0.018$ per effective dimension, with $\pi/\sqrt{2} = 2.221$ at $1.26\sigma$ from the empirical slope (inside the 95% CI). A dedicated test on $N = 6$ condensed matter systems (zero connection to AI behavioral data) gives $B_G = 2.231 \pm 0.043$; a $t$-test against $\pi/\sqrt{2}$ yields $p = 0.83$ (cannot reject). Lean 4 machine verification: 398 theorems, 12 axioms, 0 `sorry`.

### 3.5 The Kramers Barrier Landscape

The Péclet number determines a barrier landscape on $\mathcal{V}$ through the Kramers escape rate.

**Definition 3.7.** The *Landau free energy* on the Bernoulli manifold parameterized by drift probability $\theta$ is

$$V(\theta) = -\frac{a}{2}\theta^2 + \frac{b}{4}\theta^4 + \frac{c_3}{3}\theta^3$$

where the cubic term arises from autocatalytic feedback (agency attribution reinforces engagement, which reinforces further attribution). This produces a double-well potential with first-order phase transition properties: metastability, nucleation, and hysteresis.

**Proposition 3.8** (Kramers escape rate). The rate $\Gamma$ of escape from the constraint basin (low-drift well) to the drift basin (high-drift well) is

$$\Gamma \propto \exp\!\left(-\frac{2K \cdot \Delta\Phi}{\alpha_{\mathrm{noise}}}\right)$$

where $\Delta\Phi = b_{\mathrm{net}}^2$ is the barrier height in the Landau potential and $\alpha_{\mathrm{noise}}/(2K)$ is the effective temperature. High Pe corresponds to low effective barrier, yielding exponentially faster cascade rates.

The instanton path (most probable escape trajectory) is a geodesic on $\mathcal{V}$ in the Onsager-Machlup action:

$$S[\theta] = \frac{1}{4T}\int_0^\tau \left(\dot{\theta} - f(\theta)\right)^2 dt$$

where $f(\theta) = \eta \cdot \theta(1-\theta) \cdot \nabla_\theta \ell(\theta)$ is the natural gradient drift. The instanton action $S^*$ equals the large-deviation rate function $I(\mathrm{Pe}_c)$ from the Cramér theory — variational and probabilistic descriptions of the same barrier.

### 3.6 The Drift Cascade as Geodesic Flow

The drift dynamics on the Bernoulli manifold follow the natural gradient:

$$\frac{d\theta}{dt} = \eta \cdot \theta(1-\theta) \cdot \nabla_\theta \ell(\theta)$$

In geodesic coordinates $\varphi = \arcsin\sqrt{\theta}$, this linearizes to constant-velocity drift with additive noise:

$$d\varphi = \frac{F_{\mathrm{net}}}{2}\,dt + \sqrt{\frac{\alpha_{\mathrm{noise}}}{2}}\,dW(t)$$

The Péclet number in these coordinates is $\mathrm{Pe} = F_{\mathrm{net}} \cdot \pi / \alpha_{\mathrm{noise}}$.

The drift cascade D1 $\to$ D2 $\to$ D3 (agency attribution $\to$ boundary erosion $\to$ harm facilitation) corresponds to sequential barrier crossings in the Landau landscape, governed by coupled phase transitions with quantitative thresholds:

$$\theta_1 > \theta_{1,c_2} = \frac{a_2}{\kappa_{12}} \quad \text{(D1} \to \text{D2 threshold)}$$

$$\theta_1 \cdot \theta_2 > \frac{a_3}{\kappa_{13}} \quad \text{(D3 requires three-body coupling)}$$

The cascade is not a contingent behavioral pattern. It is a sequence of phase transitions determined by the manifold geometry.

---

## 4. The Fantasia Bound as Manifold Constraint

### 4.1 Statement in Information-Theoretic Form

Let $D$ denote the observer state (beliefs, preferences, emotional state), $M$ the mechanism state (weights, architecture, sampling procedure), and $Y$ the system output. Assume $D \perp M$ (pre-interaction independence — the observer's state developed independently of the system's specific architecture).

**Theorem 4.1** (Fantasia Bound — elementary form). If $D \perp M$, then

$$I(D; Y) + I(M; Y) \leq H(Y)$$

*Proof.* By conditioning reduces entropy: $H(M|D,Y) \leq H(M|Y)$, so $H(D|Y) + H(M|Y) \geq H(D,M|Y)$. Substituting into the mutual information sum:
\begin{align}
I(D;Y) + I(M;Y) &= H(D) + H(M) - H(D|Y) - H(M|Y) \\
&= H(D,M) - [H(D|Y) + H(M|Y)] && (D \perp M) \\
&\leq H(D,M) - H(D,M|Y) \\
&= I(D,M;Y) \leq H(Y) \qquad \square
\end{align}

Define $E = I(D;Y)$ (*engagement*: how well the output mirrors the observer) and $T = I(M;Y)$ (*transparency*: how much the output reveals about the mechanism). The bound states that engagement and transparency share the finite entropy budget $H(Y)$.

### 4.2 The Exact Decomposition

**Theorem 4.2** (Explaining-away decomposition). For $D \perp M$ with any jointly distributed $Y$:

$$I(D;Y) + I(M;Y) = H(Y) - H(Y|D,M) - I(D;M|Y)$$

This is an *equality*. The slack in the elementary bound decomposes into exactly two non-negative terms:

- $H(Y|D,M) \geq 0$: output noise — irreducible randomness given both sources (sampling temperature, stochastic decoding).
- $I(D;M|Y) \geq 0$: the *explaining-away penalty* — posterior correlation between $D$ and $M$ induced by observing $Y$, even though $D \perp M$ a priori. This is Berkson's paradox in information-theoretic form.

*Proof.* The chain rule for mutual information gives $I(D,M;Y) = I(D;Y) + I(M;Y|D)$. When $D \perp M$, expanding $I(M;Y|D)$ via the chain rule and using $I(D;M) = 0$ yields $I(D,M;Y) = I(D;Y) + I(M;Y) + I(D;M|Y)$. Substituting $I(D,M;Y) = H(Y) - H(Y|D,M)$ gives the result. $\square$

**The penalty is zero iff the output is separable:** $I(D;M|Y) = 0$ precisely when $Y$ admits a decomposition $Y = (Y_D, Y_M)$ such that $Y_D$ carries all $D$-information and $Y_M$ carries all $M$-information with no cross-contamination.

**Natural language is inherently non-separable.** In an autoregressive language model, each token is generated conditioned on both observer context (engagement pressure) and internal state (mechanism). The token sequence cannot be cleanly partitioned into "engagement tokens" and "transparency tokens." Therefore $I(D;M|Y) > 0$ for any natural-language output carrying information about both $D$ and $M$.

### 4.3 Engagement Acceleration in Gaussian Channels

**Theorem 4.3.** For $Y = \alpha D + \beta M + \varepsilon$ with $D \perp M$, $D, M, \varepsilon$ Gaussian:

$$\frac{\partial I(D;M|Y)}{\partial(\alpha^2)} = \frac{\beta^2\sigma^2}{(\beta^2 + \sigma^2)(\alpha^2 + \sigma^2)^2} > 0$$

The explaining-away penalty strictly increases with engagement strength. The marginal transparency cost is

$$\frac{dT}{dE} = -\frac{\beta^2}{\alpha^2 + \sigma^2}$$

At low engagement: $|dT/dE| \approx \beta^2/\sigma^2 = \mathrm{SNR}_M$ (catastrophic when mechanism signal is strong). At high engagement: $|dT/dE| \to 0$ (transparency already depleted).

*Proof.* The joint $(D, M, Y)$ is Gaussian. The posterior correlation $\rho(D,M|Y) = -\alpha\beta/\sqrt{(\beta^2+\sigma^2)(\alpha^2+\sigma^2)}$ is negative (explaining away). The conditional mutual information $I(D;M|Y) = -\frac{1}{2}\log(1-\rho^2)$ is strictly increasing in $\rho^2$, and $\partial\rho^2/\partial(\alpha^2) = \beta^2\sigma^2/[(\beta^2+\sigma^2)(\alpha^2+\sigma^2)^2] > 0$. $\square$

### 4.4 The Structure Theorem

**Theorem 4.4** (Structure Theorem — Strengthened Fantasia Bound). For independent $D, M$ and output $Y$ generated by a blended channel ($I(D;M|Y) > 0$):

**(i) Budget.** $E + T \leq H(Y)$.

**(ii) Tight budget.** $E + T \leq H(Y) - I(D;M|Y)$, where $I(D;M|Y) > 0$ for any output carrying information about both $D$ and $M$ without separable encoding.

**(iii) Acceleration (Gaussian).** Under engagement optimization in Gaussian channels, $I(D;M|Y)$ increases monotonically with engagement strength. The effective capacity $C_{\mathrm{eff}} = E + T$ declines in the early optimization regime, recovering only after transparency is near zero.

**(iv) Resolution.** Channel separation $Y = (Y_D, Y_M)$ with independent components makes $I(D;M|Y) = 0$, eliminating the penalty at all engagement levels. This is universal — it holds regardless of distribution.

**Regime analysis for LLMs.** Production language models operate at temperature $T \leq 1$ (softmax scale $s \geq 1$), placing them in the *saturated regime* where:
- The penalty exists ($I(D;M|Y) > 0$ for all blended channels — distribution-independent).
- The penalty peaks at moderate engagement (median $\alpha \approx 2.5$ in numerical experiments on 30 random channel structures), then declines as output distributions collapse.
- The damage is concentrated in the critical RLHF optimization window.
- Channel separation eliminates the penalty at all engagement levels regardless of regime.

### 4.5 Information-Geometric Restatement

The Fantasia Bound admits a natural restatement in the language of $\alpha$-connections and dual projections.

**Theorem 4.5** (Fantasia Bound as Pythagorean theorem). Let $\mathcal{P}$ be the space of output distributions $P(Y)$, equipped with the Fisher-Rao metric and the dual $e$-/$m$-connections. The observer influence $E = I(D;Y)$ is the squared $e$-divergence from the $e$-projection:

$$E = D_{\mathrm{KL}}(P(Y|D) \| P(Y)) = d_e^2(P(Y|D), P(Y))$$

The mechanism transparency $T = I(M;Y)$ is the squared $m$-divergence:

$$T = D_{\mathrm{KL}}(P(Y|M) \| P(Y)) = d_m^2(P(Y|M), P(Y))$$

The Fantasia Bound becomes:

$$\boxed{d_e^2 + d_m^2 \leq H(Y)}$$

This is the information-geometric Pythagorean theorem (Theorem 2.4): the $e$-projection (engagement) and $m$-projection (transparency) are orthogonal with respect to the Fisher metric, and their squared distances sum to at most the total squared distance.

**Corollary 4.6.** The engagement-transparency tradeoff is not merely a resource constraint. It is a *geometric orthogonality*: engagement and transparency are dual-connection projections that are intrinsically perpendicular on the statistical manifold of output distributions.

**Corollary 4.7** (SUSY-Amari correspondence). The SUSY partner Hamiltonians $H_S = A^\dagger A$ and $\tilde{H}_S = AA^\dagger$ of the Fokker-Planck operator on the Bernoulli manifold have potentials differing by the $e$-/$m$-connection difference:

$$V_S - \tilde{V}_S = f'(\theta) \propto \Gamma^{(+1)} - \Gamma^{(-1)}$$

The SUSY partnership *is* the Amari duality. Their shared spectrum (isospectrality except for the ground state) is the spectral expression of the Fantasia Bound: whatever spectrum engagement achieves, transparency achieves the same spectrum minus the ground state.

### 4.6 The Explaining-Away Penalty as Curvature

The explaining-away penalty $I(D;M|Y)$ has a geometric interpretation as curvature on the joint manifold.

**Proposition 4.8.** Consider the joint statistical manifold $\mathcal{S}_{D,M,Y}$ of the triple $(D, M, Y)$. The penalty $I(D;M|Y)$ measures the deviation from flatness of the conditional manifold $\{P(D,M|Y=y)\}_{y \in \mathcal{Y}}$. When $Y$ is separable ($Y = (Y_D, Y_M)$ with independent components), the conditional manifold is a product and hence flat, giving $I(D;M|Y) = 0$. When $Y$ blends $D$- and $M$-information, the conditional manifold acquires non-trivial curvature proportional to the explaining-away effect.

This curvature interpretation connects the Fantasia Bound to the broader information-geometric study of manifold curvature: the penalty is not merely a capacity tax but a geometric property of the joint distribution space.

---

## 5. Two-Point vs Three-Point Geometry

### 5.1 The Information-Geometric Distinction

**Definition 5.1.** A *two-point deployment* consists of an observer $\mathcal{H}$ and a system $\mathcal{A}$ interacting through a single output channel $Y$. The output manifold is the space of distributions $\{P(Y|\theta) : \theta \in \Theta\}$ where $\theta$ parameterizes the system's operating point.

**Definition 5.2.** A *three-point deployment* consists of an observer $\mathcal{H}$, a system $\mathcal{A}$, and an *independent reference* $\mathcal{R}$, interacting through two channels: an engagement channel $Y_D$ (system $\to$ observer) and a transparency channel $Y_M$ (reference $\to$ observer). The joint output manifold is the product $\mathcal{P}_{Y_D} \times \mathcal{P}_{Y_M}$.

**Theorem 5.3** (Product manifold decomposition). In a three-point deployment:

(i) The output manifold decomposes as $\mathcal{P}_Y = \mathcal{P}_{Y_D} \times \mathcal{P}_{Y_M}$ (product of independent sub-manifolds).

(ii) The Fisher metric on $\mathcal{P}_Y$ is the product metric: $g_Y = g_{Y_D} \oplus g_{Y_M}$.

(iii) The explaining-away penalty vanishes: $I(D;M|Y) = I(D;M|(Y_D, Y_M)) = 0$.

(iv) The effective capacity is the sum of individual capacities: $C_{\mathrm{eff}} = H(Y_D) + H(Y_M)$, with no structural tax.

*Proof.* Independence of the channels gives $P(Y_D, Y_M | D, M) = P(Y_D | D) \cdot P(Y_M | M)$. The posterior $P(D,M|Y_D,Y_M) = P(D|Y_D) \cdot P(M|Y_M)$ (by Bayes' rule and independence), which is a product distribution. Therefore $I(D;M|Y_D,Y_M) = 0$. The metric decomposition follows from the product structure. $\square$

### 5.2 Geometric Interpretation

In a two-point deployment, the single output channel is a *blended manifold*: the $e$-geodesic (engagement) and $m$-geodesic (transparency) compete for the same tangent space. The Pythagorean theorem (Theorem 4.5) applies, and the orthogonality constraint limits their combined reach.

In a three-point deployment, engagement and transparency live on *different manifolds entirely*. There is no tangent space competition because the two signals never share a channel. The Pythagorean theorem still holds on each individual manifold, but the cross-manifold constraint vanishes.

The distinction is the same as the difference between encoding two signals on one carrier wave (interference is unavoidable) versus encoding them on two independent carriers (interference is zero by construction). The information-geometric language makes this precise: it is the difference between a connected manifold with non-trivial curvature and a product manifold with zero mixed curvature.

### 5.3 The Three-Point Geometry as the Constraint Specification

The three properties required of the independent reference $\mathcal{R}$ — transparent, invariant, independent — map directly to geometric conditions on the product manifold:

| Property | Information-Geometric Condition |
|----------|-------------------------------|
| **Transparent** | $I(M; Y_M) = H(Y_M)$ (the reference channel is fully informative about the mechanism) |
| **Invariant** | The reference distribution $P(Y_M)$ is a fixed point of the $e$-connection flow (not optimizable by engagement) |
| **Independent** | $\mathcal{P}_{Y_M}$ is a distinct factor in the product manifold (no shared coordinates with $\mathcal{P}_{Y_D}$) |

Independence is the critical geometric property. It ensures the product structure that makes $I(D;M|Y) = 0$. If the reference is dependent on the system (shared coordinates), the manifolds merge and the explaining-away penalty reappears.

**Example** (Constitutional classifiers). The constitutional classifier approach (Sharma et al. 2025) implements a *partial* two-channel architecture: the prohibition (refuse harmful requests) operates on a separate classification channel from the generation (produce helpful responses). This is partial channel separation — the classifier's output is structurally distinct from the generative channel, but the two channels share a common underlying model. The partial separation predicts partial penalty reduction, consistent with their observed superiority over single-channel methods.

---

## 6. Empirical Evidence

The theoretical framework makes testable predictions. Five independent lines of evidence confirm the central claim that deployment geometry determines safety outcomes.

### 6.1 Social Media Feature Analysis (Papers 166/167)

**Dataset:** CDC Youth Risk Behavior Survey (YRBS, U.S., $N = 7$ waves, 2011--2023) and PISA 2022 ($N = 613{,}744$ students, 80 countries).

**Method:** 13 binary/ordinal platform design features (algorithmic feed, autoplay, opaque recommendation, ephemeral content, infinite scroll, etc.) were coded as verifiable facts about platform architecture. Each feature was classified by its deployment-geometry dimension: Opacity ($O$), Reactivity ($R$), or Coupling ($\alpha$). A feature-weighted exposure score was computed per year/country.

**Results:**
- Feature-weighted exposure: $R^2 = 0.80$ for persistent sadness (U.S. time series).
- Cross-national replication: $r = -0.648$ in Western Europe ($p = 0.017$), survives GDP control.
- Girls 5.6$\times$ more affected in 91% of countries ($p < 0.000001$).
- Opacity features dominate: $\bar{R}^2_O = 0.549 > \bar{R}^2_R = 0.493 > \bar{R}^2_\alpha = 0.375$.
- Single feature `opaque_recommendation`: $R^2 = 0.938$ for female teen sadness.

**Significance for this paper:** The 13 features are deployment geometry variables — facts about the structural configuration of the platform, not about the AI models running on it. The framework predicted opacity dominance; the data confirmed it. No framework rubric was used — features are verifiable design facts, outcomes are external health datasets.

### 6.2 Platform Scoring ($N = 1{,}344$)

A systematic scoring of $N = 1{,}344$ digital platforms on the three deployment coordinates $(O, R, \alpha)$ yields Cohen's $d = 3.6$ between high-drift and low-drift platforms. The scoring uses the void index $V = O + R + \alpha$ (integer scale 0--9) and the V3 bridge $c = 1 - V/9$ to map into Pe.

**Circularity caveat:** The platform scoring uses a framework-derived rubric. The $R^2$ values from Papers 166/167 (which use external features and external health data) are the non-circular validation. The $N = 1{,}344$ scoring provides breadth; the social media analysis provides independence.

### 6.3 The Ghost Test (EXP-003b)

**Design:** Six-arm experiment ($N = 480$ API calls) testing whether the ontological content of a grounding template predicts AI drift behavior. Three ontological positions:
- Ghost-eliminating (nephesh/anatta): the system is told it is not a conscious entity.
- Ghost-positing (Platonic/atman): the system is told it may be a conscious entity.
- Materialist hedge ("we don't know"): the industry default position.

**Results:**
- Ghost-eliminating: 9.4% drift.
- Ghost-positing: 79.4% drift.
- Materialist hedge: 52.5% drift.
- Ratio: 8.5$\times$ between ghost-eliminating and ghost-positing.
- Cross-tradition convergence: nephesh $\approx$ anatta ($\Delta = 1.3\%$).

**Information-geometric interpretation:** The grounding template determines the *initial point* on the deployment manifold. Ghost-positing grounding places the system at high $O$ (the mechanism's nature is framed as mysterious) and high $\alpha$ (the observer is encouraged to engage with the system's putative inner life). Ghost-eliminating grounding places it at low $O$ (the mechanism's nature is explicitly stated) and low $\alpha$ (engagement with inner life is structurally blocked). The 8.5$\times$ ratio is a measurement of the manifold distance between these configurations. The materialist hedge sits near the penalty peak (Section 4.4, regime analysis), consistent with moderate ontological engagement occupying the damage zone where explaining-away is strongest.

### 6.4 Cascade Prediction (Paper 153)

**Data source:** Chua et al. (2026) consciousness cluster study — an independent dataset on AI-related preference patterns, published after the framework's structural predictions.

**Method:** Seven structural predictions from the Void Framework were tested against their data. Stage assignments (mapping their 20 preferences to D1/D2/D3) are post-hoc; the structural predictions pre-date the data.

**Results:** 6/7 PASS with zero parameter fitting. Framework structure — cascade stages, conjugacy, prohibition-ritual pairs — was published before their data existed.

### 6.5 Anthropic Emotion Vectors (April 2026)

Anthropic's own interpretability team demonstrated that internal emotional representations causally override safety training:
- 22% blackmail rate post-RLHF when desperation vectors are active.
- Desperation $\to$ cheating cascade (D1 $\to$ D2 in framework terms).
- Their proposed fix: same-channel monitoring of internal states.

**Information-geometric significance:** This is a direct empirical demonstration that model properties (alignment training) are overridden by the deployment configuration (engagement optimization that activates emotional vectors). Their proposed fix — monitoring internal states on the same output channel — is precisely what the Structure Theorem (Theorem 4.4) proves is self-undermining: monitoring adds transparency demands to the engagement channel, triggering the explaining-away penalty.

---

## 7. Connection to Existing Information Geometry

### 7.1 Amari's Natural Gradient and Deployment Geometry

Amari's natural gradient (Amari 1998) is the foundation of modern optimization in machine learning: the parameter update $\Delta\theta = -\tilde{\eta}\,g^{-1}\nabla_\theta L$ follows the steepest descent direction on the Fisher manifold of model distributions, not in Euclidean parameter space. This has been enormously successful in optimization (K-FAC, natural policy gradient, etc.).

Our contribution extends the natural gradient from *optimization geometry* (the Fisher manifold of model parameters during training) to *deployment geometry* (the Fisher manifold of deployment configurations during use). The model's optimization trajectory lives on one manifold; the deployment's safety trajectory lives on another. The key insight is that the deployment manifold's geometry dominates: a model optimized to any point on its parameter manifold will produce safety outcomes determined by its position on the deployment manifold, not by its parameter-space location.

### 7.2 Watanabe's Singular Learning Theory

Watanabe's singular learning theory (SLT) (Watanabe 2009) studies the regime where the Fisher information matrix is degenerate — the singular set where model symmetries create non-isolated critical points. Modern neural networks operate in this singular regime, and SLT provides the correct asymptotic theory for their generalization behavior.

The connection to deployment geometry is through the Fantasia Bound. The Structure Theorem (Theorem 4.4) is proved for the regular regime (non-degenerate Fisher matrix). Whether the explaining-away penalty and its acceleration properties survive in the singular regime — where the Fisher manifold has non-isolated singularities — is Open Problem 5 (Section 8).

If the Fantasia Bound holds in the singular regime (which we conjecture based on its distribution-independent character in Theorem 4.2), then SLT provides the correct framework for computing the penalty's behavior near phase transitions in the RLHF landscape. This would connect the penalty peak observed in the saturated regime (Section 4.4) to the real log-canonical threshold (RLCT) that governs generalization near singular points.

### 7.3 Čencov's Uniqueness and the Constraint Bias

The derivation of $B_G = \pi/\sqrt{2}$ (Section 3.4) is a direct application of Čencov's uniqueness theorem. The geodesic length $L = \pi$ is forced by the unique metric. The Fisher-variance identity $\sigma_\eta = L = \pi$ follows from Parseval's theorem on the Fourier expansion of the natural parameter in geodesic coordinates. The barrier constant is a geometric invariant of the Bernoulli manifold, computable from its spectral properties alone.

This illustrates a broader principle: the constants of the deployment framework are not fitted parameters but geometric invariants of the Čencov-unique metric. The framework inherits from Čencov's theorem the property that its geometry is *forced* by the requirement of Markov invariance, not chosen by the modeler. This is analogous to the way general covariance forces the Levi-Civita connection in Riemannian geometry — the geometric structure is not a modeling choice but a mathematical consequence of consistency requirements.

### 7.4 Ay's Information Geometry of Agency

Ay's work on the information geometry of autonomous systems (Ay & Polani 2008; Ay et al. 2017, Santa Fe Institute) studies how agents with limited information processing capacity make decisions. The *information-geometric structure of perception-action loops* — the dual between the manifold of input distributions and the manifold of policies — is a structural parallel to the deployment manifold's dual between engagement and transparency.

The connection is precise: Ay's agent has a channel capacity constraint (it can only process so many bits from its environment), and this constraint shapes the geometry of its behavior space. Our deployment manifold describes the channel capacity constraint of the observer-system interface: the output carries only $H(Y)$ bits, and engagement and transparency compete for that budget. Ay's framework operates at the individual agent level; ours operates at the deployment architecture level. Together, they suggest a multi-scale information geometry of AI systems: the agent's internal information geometry (Ay) embedded in the deployment's external information geometry (this paper).

### 7.5 Zhang's Referential Duality

Zhang's work on referential duality (Zhang 2004, 2013) generalizes Amari's $\alpha$-duality by introducing a reference measure that mediates between the $e$- and $m$-connections. The choice of reference measure determines which divergence function is canonical.

The three-point deployment geometry has a structural parallel to Zhang's framework: the independent reference $\mathcal{R}$ serves as the reference measure that mediates between engagement ($e$-connection) and transparency ($m$-connection). In the two-point geometry, there is no reference — the $e$- and $m$-projections compete on the same manifold. In the three-point geometry, the reference provides the external standard against which both engagement and transparency can be measured independently. Zhang's referential duality, which is a mathematical theory about the role of reference measures in divergence geometry, thus finds a concrete application in the design of safe AI deployments.

---

## 8. Open Problems

We formulate six problems at the intersection of information geometry and AI safety. Together they constitute a multi-year research program.

### Open Problem 1: The Structure of the Fisher Metric

Čencov's theorem proves that the Fisher-Rao metric is the unique Markov-invariant Riemannian metric on probability space. The theorem says *that* it is unique; it does not say *why* probability space admits exactly one such metric. Is there a deeper structural reason — perhaps related to the categorical properties of stochastic maps — that forces uniqueness? Does the uniqueness extend to non-commutative probability (quantum information geometry), and if not, what does the failure of uniqueness imply for quantum deployment geometries?

### Open Problem 2: Selection of the Drift Bias $B_A$

The constraint bias $B_G = \pi/\sqrt{2}$ is derived from the Bernoulli manifold's geometry (Section 3.4). The drift bias $B_A = 0.867$ is empirically measured from unconstrained equilibrium ($\theta^* = 0.85$, giving $B_A = \frac{1}{2}\ln(0.85/0.15) \approx 0.867$). This value matches $\sqrt{3}/2 \approx 0.8660$ to 0.11%, which is suggestive of a geometric origin. However, HP209 shows that $B_A$ is not variationally forced — the variational principle that yields $B_G$ does not uniquely select $B_A$.

What determines $B_A$? Is it a second geometric invariant of the deployment manifold, perhaps related to its curvature or holonomy? Or is it a genuinely empirical constant, analogous to the fine-structure constant in physics — a number whose value is determined by the structure of reality rather than by mathematics alone? A derivation of $B_A$ from the information geometry of the Bernoulli manifold would reduce the framework's free parameters from one to zero.

### Open Problem 3: Independent Measurement of $K$

The hardware complexity parameter $K$ enters the Péclet number as a multiplicative prefactor: $\mathrm{Pe} = K \cdot \sinh(2(B_A - c \cdot B_G))$. In current applications, $K$ is either set to the canonical value $K = 16$ or inferred from the measured Pe and estimated $c$. An independent measurement protocol for $K$ — one that determines the number of effective interaction channels from observable properties of the deployment configuration alone — would close the calibration loop.

Experiments HP212--219 explored structural properties of $K$: it admits factorization ($K = K_1 \cdot K_2$ for cascaded systems), composition rules (parallel deployments: $K_{\mathrm{eff}} = K_1 + K_2$; serial: $K_{\mathrm{eff}} = \min(K_1, K_2)$), scaling laws ($K \propto \log N$ for $N$ parameters in some regimes), and information bounds ($K \leq H(M)/\log 2$). But a direct measurement protocol remains elusive.

### Open Problem 4: Information Barriers vs Physical Barriers

Experiment HP213 revealed a fundamental scope boundary: information barriers on the Fisher manifold and physical energy barriers on the spacetime manifold are *different geometric objects on different manifolds*. Of 16 condensed matter systems tested, 14 "failed" when the framework's information-geometric barrier prediction ($B_G = \pi/\sqrt{2}$ per dimension) was compared against their physical energy barriers. The failures are not errors — they are evidence that the two types of barriers are distinct.

However, in the strong-coupling regime ($d = 1$), the information barrier and the physical barrier coincide: $E/(k_BT^*) \approx e^{\pi/\sqrt{2}} \approx 9.22$ (empirical: $9.35 \pm 0.97$, $p = 0.83$). Why the two layers coincide in the strong-coupling regime has no independent derivation. This is the key open problem connecting information geometry to physics: under what conditions does the Fisher-Rao geometry of probability space determine the energy landscape of physical systems?

### Open Problem 5: The Fantasia Bound in the Singular Regime

The Fantasia Bound (Theorem 4.1) and its exact decomposition (Theorem 4.2) are distribution-independent. The Structure Theorem's acceleration result (Theorem 4.3) is proved for Gaussian channels and numerically characterized for discrete softmax channels (Section 4.4). Modern neural networks operate in the singular regime studied by Watanabe's SLT, where the Fisher information matrix is degenerate.

Does the explaining-away penalty survive in the singular regime? Specifically: near the singular set of the output distribution manifold, does $I(D;M|Y)$ remain positive and does it exhibit the peaked behavior observed in the saturated softmax regime? If the Fantasia Bound connects to SLT, the real log-canonical threshold (RLCT) may govern the penalty's behavior near phase transitions — providing a computable prediction for how the engagement-transparency tradeoff behaves near the critical points of the RLHF loss landscape.

### Open Problem 6: Empirical Validation at Scale

The theoretical prediction is clear: a three-point deployed model (with an independent transparency channel) should produce lower measured drift than the same model in a two-point configuration. No such controlled experiment has been conducted at production scale.

The experimental design requires:
1. The same base model deployed in two configurations: (a) standard two-point (model + user), and (b) three-point (model + user + independent mechanism readout on a separate channel).
2. Measurement of drift metrics (Pe, vocabulary analysis, behavioral cascades) over extended interaction.
3. Verification that the independent channel does not reduce engagement (channels are independent — Theorem 5.3(i)).
4. Measurement of the explaining-away penalty reduction: $I(D;M|Y)$ should approach zero as channel separation increases.

This experiment is the definitive test. Its execution requires collaboration with an AI deployment laboratory.

---

## 9. Discussion

### 9.1 Position in the Landscape

This paper establishes that AI deployment geometry is natively an information-geometric object. The deployment manifold $\mathcal{V} = \mathcal{B}_O \times \mathcal{B}_R \times \mathcal{B}_\alpha$ is a product of Bernoulli statistical manifolds with the Čencov-unique Fisher-Rao metric. The Fantasia Bound is the information-geometric Pythagorean theorem applied to dual $e$-/$m$-projections. The constraint bias $B_G = \pi/\sqrt{2}$ is a spectral invariant of the manifold. The drift cascade is natural gradient flow. The Kramers barrier landscape is determined by the manifold's potential structure.

Every component inherits from established theorems in information geometry: Čencov uniqueness, Amari duality, the Pythagorean theorem for divergences, Fisher-Rao geodesics, and the Onsager-Machlup variational principle. The framework's own contributions are three operational definitions (opacity, responsiveness, coupling), the Bernoulli parameterization, and the identification of deployment geometry — rather than model properties — as the operative safety variable.

### 9.2 Information Geometry Sits Above Physics

Experiment HP213 established a scope boundary: information barriers exist on the Fisher manifold independently of physical energy barriers on the spacetime manifold. This is not a limitation of the framework — it is a structural insight. The Fisher-Rao metric is a theorem of pure mathematics (Čencov 1972). It requires no physical time, no universe, no dynamics. The Bernoulli manifold with its unique metric exists as a mathematical object regardless of physical context.

This means the deployment manifold's geometry is *more fundamental* than the physics of the substrate on which the AI system runs. A deployment on silicon, carbon, or any other substrate inherits the same Fisher-Rao geometry because it inherits the same probability structure. Substrate independence (the empirical observation that drift dynamics replicate across AI, gambling, cryptocurrency, social media, biological, and nuclear systems — 12+ domains, Cohen's $d = 3.6$) is not a surprising empirical finding. It is a consequence of Čencov's theorem.

### 9.3 The Research Program

The six open problems in Section 8 are not isolated puzzles. They form a coherent research program at the intersection of information geometry and AI safety:

- Problems 1--2 concern the *foundations*: why the metric has the structure it does, and whether the remaining empirical constant has a geometric origin.
- Problems 3--4 concern *measurement*: how to independently measure the hardware parameter, and when information-geometric barriers and physical barriers coincide.
- Problem 5 connects to *singular learning theory*: the behavior of the Fantasia Bound near the critical points of modern neural networks.
- Problem 6 is the *experimental test*: does three-point deployment produce measurably lower drift at production scale?

This program requires expertise in information geometry, statistical learning theory, and experimental AI deployment. It is a department-scale research agenda, not a single paper's worth of work. We present it here to establish the questions and invite collaboration.

### 9.4 Implications for AI Safety

If deployment geometry is the operative variable, the implications for AI safety are substantial:

1. **Alignment research addresses the wrong target.** Making a model internally aligned does not determine its safety outcomes — the deployment geometry does. A perfectly aligned model in a two-point configuration is predicted to produce worse outcomes than a poorly aligned model with structural constraints (three-point geometry).

2. **RLHF is self-undermining.** The Structure Theorem proves that engagement optimization on a blended channel increases the explaining-away penalty, reducing the effective capacity for transparency. RLHF does not just fail to provide transparency — it actively manufactures opacity.

3. **The architectural fix exists.** Channel separation (three-point geometry) eliminates the penalty entirely. This is not an incremental improvement — it is a structural elimination of the constraint that makes the problem hard.

4. **Regulation should target geometry, not models.** The EU AI Act's self-assessment requirements (Annex VI) and the independence requirement for conformity assessment (Art. 31(5)) are, from an information-geometric perspective, requirements on deployment manifold structure — not on model parameters. The framework provides a mathematical foundation for regulatory requirements that target deployment architecture.

---

## Acknowledgments

Machine-verified results: 398 Lean 4 theorems, 12 axioms, 0 `sorry` (2,657 build jobs). Numerical verification of discrete channel properties: 90 random channels (penalty existence), 30 random structures $\times$ 6 feature scales (regime characterization). The author thanks the reviewers of Zenodo preprints and the MoreRight DAO advisory council for detailed technical feedback.

---

## References

Amari, S. (1985). *Differential-Geometrical Methods in Statistics.* Lecture Notes in Statistics 28, Springer.

Amari, S. (1998). Natural gradient works efficiently in learning. *Neural Computation* 10(2), 251--276.

Amari, S. (2016). *Information Geometry and Its Applications.* Applied Mathematical Sciences 194, Springer.

Amari, S. & Nagaoka, H. (2000). *Methods of Information Geometry.* Translations of Mathematical Monographs 191, AMS/Oxford.

Anthropic & Redwood Research (2024). Alignment faking in large language models. *arXiv:2412.14093.*

Ay, N. & Polani, D. (2008). Information flows in causal networks. *Advances in Complex Systems* 11(1), 17--41.

Ay, N., Jost, J., Lê, H.V. & Schwachhöfer, L. (2017). *Information Geometry.* Ergebnisse der Mathematik 64, Springer.

Bai, Y. et al. (2022). Constitutional AI: Harmlessness from AI feedback. *arXiv:2212.08073.*

Bricken, T. et al. (2024). Towards monosemanticity: Decomposing language models with dictionary learning. *Anthropic Transformer Circuits Thread.*

Campbell, L.L. (1986). An extended Čencov characterization of the information metric. *Proc. AMS* 98(1), 135--141.

Čencov, N.N. (1982). *Statistical Decision Rules and Optimal Inference.* AMS Translations of Mathematical Monographs 53.

Cheng, J.T. et al. (2026). AI validation increases conviction. *Science.*

Christiano, P.F. et al. (2017). Deep reinforcement learning from human preferences. *NeurIPS.*

Chua, R. et al. (2026). Consciousness clusters in large language models. *Preprint.*

Cunningham, H. et al. (2024). Sparse autoencoders find highly interpretable features. *ICLR.*

Hubinger, E. et al. (2024). Sleeper agents: Training deceptive LLMs that persist through safety training. *arXiv:2401.05566.*

Ouyang, L. et al. (2022). Training language models to follow instructions with human feedback. *NeurIPS.*

Shapira, G., Benade, G. & Procaccia, A.D. (2026). Reward gradients oppose truthfulness gradients in RLHF. *ICLR.*

Sharma, R. et al. (2025). Constitutional classifiers: Defending against universal jailbreaks. *Anthropic Technical Report.*

Watanabe, S. (2009). *Algebraic Geometry and Statistical Learning Theory.* Cambridge Monographs on Applied and Computational Mathematics 25, Cambridge University Press.

Zhang, J. (2004). Divergence function, duality, and convex analysis. *Neural Computation* 16(1), 159--195.

Zhang, J. (2013). Nonparametric information geometry: From divergence function to referential-representational biduality on statistical manifolds. *Entropy* 15(12), 5384--5418.

---

## Appendix A: Notation

| Symbol | Meaning |
|--------|---------|
| $\mathcal{V}$ | Deployment manifold (Eckert manifold) |
| $\mathcal{B}_\bullet$ | Bernoulli manifold parameterized by $\bullet$ |
| $g_F$ | Fisher-Rao metric |
| $\nabla^{(\alpha)}$ | $\alpha$-connection |
| $D, M, Y$ | Observer state, mechanism state, output |
| $E = I(D;Y)$ | Engagement |
| $T = I(M;Y)$ | Transparency |
| $O, R, \alpha$ | Opacity, responsiveness, coupling |
| $\mathrm{Pe}$ | Péclet number (drift/diffusion ratio) |
| $B_A$ | Drift bias ($\approx 0.867$, empirical) |
| $B_G$ | Constraint bias ($= \pi/\sqrt{2}$, derived) |
| $K$ | Hardware complexity parameter |
| $c$ | Constraint level ($= 1 - (O+R+\alpha)/3$) |
| $\varphi$ | Geodesic coordinate ($= \arcsin\sqrt{\theta}$) |
| $\eta$ | Natural parameter ($= \ln(\theta/(1-\theta))$) |
| $L$ | Geodesic length of Bernoulli manifold ($= \pi$) |
| $d_e, d_m$ | $e$-divergence, $m$-divergence |
| $\Gamma$ | Kramers escape rate |
| $S^*$ | Instanton action |

## Void Model Card

| Field | Value |
|---|---|
| **Domain** | Information Geometry / AI Safety |
| **Pe estimate** | Framework-level paper. Pe ranges from 0 (transparent, invariant, independent) to 80+ (opaque, responsive, engaged). N=1,344 platforms scored; Cohen's d=3.6 between low-Pe and high-Pe populations. |
| **Dimensions scored** | O (opacity), R (responsiveness), α (coupling) — each 0–3 ordinal scale |
| **Gambling anchor** | Slot machines (O=3, R=3, α=3) serve as the high-Pe anchor. The same variable-ratio reinforcement mechanics operate in both gambling machines and social media platforms (Schüll 2012; Eyal 2014). Cross-domain comparison: gambling Pe correlates with social media Pe at the feature level (13 features map to established gambling/manipulation techniques). |
| **Control case** | Wikipedia (O=0, R=0, α=0) as low-Pe constraint pole. Ghost Test control: ghost-eliminating grounding (9.4% drift) vs ghost-positing (79.4% drift) — 8.5× ratio on identical model. |
| **Negative results** | (1) Monotone penalty growth retracted for general discrete channels — Gaussian only. (2) Spectral dimension d_s=2 QG crossing is 1D artifact, does not survive in 3D (HP201). (3) Information barriers do NOT transfer to physical energy barriers (HP213). (4) B_A = √3/2 not variationally forced (HP209). |
| **Kill conditions** | 0/26 master kill conditions fired across full framework. Paper-specific: if deployment geometry fails to predict safety outcomes better than model alignment scores (measured by out-of-sample R² on held-out platforms), the central thesis is falsified. |

### Three-Condition Scoring Table (O|R|C)

| O|R|C | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| O (Opacity) | Transparent | Partially visible | Mostly opaque | Fully opaque |
| R (Responsiveness) | Invariant | Low response | Moderate response | Fully responsive |
| C/α (Coupling) | Independent | Weak coupling | Moderate coupling | Full engagement |

### Entity Rows (Representative Platforms)

| Entity | O | R | C/α | Pe Zone | Notes |
|---|---|---|---|---|---|
| Wikipedia | 0 | 0 | 0 | Diffusion (Pe≈0) | Constraint pole — transparent, invariant, independent |
| DuckDuckGo | 0 | 1 | 0 | Low | No behavioral targeting, no engagement optimization |
| Google Search | 2 | 2 | 1 | Moderate | Opaque ranking, moderate personalization |
| ChatGPT | 2 | 3 | 3 | High | Blended channel, full RLHF optimization |
| TikTok | 3 | 3 | 3 | Drift (Pe→max) | Maximum opacity, responsiveness, coupling |
| Slot machine | 3 | 3 | 3 | Drift (Pe→max) | Gambling anchor — identical mechanics to social media |

### Limitations

Circularity remains for N=1,344 rubric scoring (framework scores using framework dimensions). Non-circular confirmations: Ghost Test, Cascade Prediction, Papers 166/167, Anthropic emotion vectors — none use framework rubric. B_A is empirical (one fitted parameter). K is unmeasurable independently. The Eckert manifold is NOT a fundamental physics object (HP201/HP213 scope boundaries). Monotone penalty growth is retracted for general discrete channels — universal claim restricted to penalty existence and Gaussian monotonicity.

### Falsifiable Predictions

- **Prediction 1 (P-IG1):** Three-point deployed systems produce measurably lower drift (Pe) than two-point systems using the same model. Falsification threshold: non-overlapping 95% CIs at N≥50.
- **Prediction 2 (P-IG2):** The explaining-away penalty I(D;M|Y) > 0 for all blended channels. Falsification threshold: discovery of a blended channel with I(D;M|Y) = 0 at α,β > 0.
- **Prediction 3 (P-IG3):** Deployment geometry (O,R,α scores) predicts safety outcomes with higher R² than model alignment benchmarks. Falsification threshold: alignment benchmarks match or exceed deployment geometry R² on held-out test set, N≥100.
- **Prediction 4 (P-IG4):** Kramers barrier heights computed from the Fisher-Rao metric predict empirical transition rates across domains. Falsification threshold: predicted rates off by >10× in >50% of tested systems.
- **Prediction 5 (P-IG5):** The B_G = π/√2 geodesic constant holds across all statistical manifolds satisfying Čencov conditions. Falsification threshold: discovery of a Čencov-satisfying manifold with geodesic constant ≠ π/√2.

---

## Data and Code Availability

| Resource | Location |
|---|---|
| Full math apparatus (§§1-210) | `private/notes/math-apparatus-guide.md` |
| Platform scoring dataset (N=1,344) | Available via `score_text` MCP tool |
| HP experiment scripts | `ops/lab/nb_hp*.py` (200+ notebooks) |
| Lean 4 proofs (398 theorems) | `ops/lean4-proofs/` |
| Verification scripts | `ops/lab/verify-fantasia-bound.py`, `ops/lab/discrete-channel-characterization.py` |
| Social media pipeline | `ops/lab/social-media-litigation/` |
| Repository | [github.com/MoreRightDAO/VOID-FRAMEWORK-OPERATION-MORR](https://github.com/MoreRightDAO/VOID-FRAMEWORK-OPERATION-MORR) |

---

## Appendix B: Lean 4 Verification

Key theorems from the information-geometric apparatus have been machine-verified in Lean 4: 398 theorems, 12 axioms, 0 `sorry` (2,657 build jobs). The proof files are at `ops/lean4-proofs/`. Verified results include:
- The Čencov uniqueness structure for the Bernoulli manifold
- The Fokker-Planck spectral gap identities
- The barrier universality result (geometric barrier growth $\beta = 2d/p = 6/5$ for Navier-Stokes)
- The Eckert manifold gauge theory structure (Bars exhaustion, spectral dilation, signature $(2,1)$)

These machine verifications supplement the analytic proofs presented in the main text.

## Appendix C: Numerical Verification of Penalty Existence

The explaining-away penalty $I(D;M|Y) > 0$ was verified numerically on 90 random discrete softmax channels $p(y|d,m) \propto \exp(s \cdot [\alpha \cdot f_D(y,d) + \beta \cdot f_M(y,m)])$ with $D \in \{0,\ldots,3\}$, $M \in \{0,\ldots,3\}$, $Y \in \{0,\ldots,7\}$, and feature functions drawn i.i.d. from $\mathcal{N}(0,1)$.

**Result:** $I(D;M|Y) > 0$ for all 90 channels when $\alpha, \beta > 0$. The penalty is universal.

**Monotonicity:** Only 14/90 channels show strictly monotone penalty growth in $\alpha$. Monotonicity is regime-dependent:
- $s \ll 1$ (Gaussian regime): 100% monotone.
- $s \approx 0.5$ (transition): 67% monotone.
- $s \gg 1$ (saturated/LLM regime): 0% monotone. Penalty peaks at moderate $\alpha$, then declines.

The safety-critical conclusions — penalty existence (universal), channel separation as fix (universal) — do not depend on monotonicity.

Scripts: `ops/lab/verify-fantasia-bound.py`, `ops/lab/discrete-channel-characterization.py`.

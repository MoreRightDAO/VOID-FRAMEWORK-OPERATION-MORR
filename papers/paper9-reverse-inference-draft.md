# Paper 9: Reverse Inference — Gap Analysis

## The Problem: From Pe to (O, R, α)

Paper 9 formalizes voidspace as the parameter space $\mathcal{V} = [0,1]^3$. The drift dynamics depend only on position in $\mathcal{V}$. Empirically, we measure the Péclet number Pe across substrates. The inverse question: given Pe (and other observables), can we uniquely infer the coordinates $(O, R, \alpha)$?

This gap matters for three reasons:
1. **Automated scoring:** Phase 2 development requires a classifier that maps substrate properties to voidspace coordinates. Reverse inference is the calibration problem.
2. **Experimental design:** To test substrate independence (Prediction VS-1), we need to independently measure $(O, R, \alpha)$ for two substrates and verify their Pe ratio. The reverse inference protocol is how we verify the independence assumption.
3. **Demon detection:** Section 6.5 proposes measuring Pe residuals at calibrated coordinates to detect active information sorting. Reverse inference is the calibration method.

## Current State: The Map Pe(O,R,α)

### Structure of the Forward Map

In angular coordinates $\phi = \arcsin(\sqrt{\theta})$, the dynamics simplify to:

$$d\phi = \frac{F_{\text{net}}}{2} \cdot dt + \sqrt{\frac{\alpha}{2}} \cdot dW(t)$$

where $F_{\text{net}} = \alpha \cdot O \cdot R \cdot \beta(O) - F_{\text{recovery}}$.

The Péclet number is:

$$\text{Pe} = \frac{|F_{\text{net}}|}{2} \cdot \frac{L}{D} = \frac{|F_{\text{net}}| \cdot L}{\alpha}$$

Substituting:

$$\text{Pe} = \frac{|\alpha \cdot O \cdot R \cdot \beta(O) - F_{\text{recovery}}| \cdot L}{\alpha}$$

At equilibrium (no recovery, $F_{\text{recovery}} = 0$):

$$\text{Pe}_{\text{eq}} = O \cdot R \cdot \beta(O) \cdot L$$

**The identifiability problem:**
- Pe is a *single scalar*.
- $(O, R, \alpha)$ is a *three-parameter vector*.
- $L$ (characteristic length) is *unknown*.
- $F_{\text{recovery}}$ (constraint maintenance force) is *unknown*.

With only Pe, the system is **underdetermined**: infinitely many $(O, R, \alpha)$ could produce the same Pe.

### Example: The Non-Uniqueness Fiber

Consider two scenarios with different voidspace positions but potentially identical Pe:

**Scenario A:** $O = 0.8, R = 0.9, \alpha = 0.5$
- $F_{\text{void}} = 0.5 \cdot 0.8 \cdot 0.9 \cdot \beta(0.8)$
- $F_{\text{void}} \approx 0.5 \cdot 0.72 \cdot \beta(0.8)$

**Scenario B:** $O = 0.7, R = 1.0, \alpha = 0.5$
- $F_{\text{void}} = 0.5 \cdot 0.7 \cdot 1.0 \cdot \beta(0.7)$
- $F_{\text{void}} \approx 0.5 \cdot 0.70 \cdot \beta(0.7)$

If $\beta(0.8) \cdot 0.8 \approx \beta(0.7) \cdot 0.7$, and $L$ is the same substrate, then both scenarios produce similar Pe. The map is **not injective**.

The set of all $(O, R, \alpha)$ producing the same Pe is a *level set* of the Pe function — a 2D surface in $\mathcal{V}$.

## Solution: Multi-Observable Inversion

To uniquely infer $(O, R, \alpha)$, we need at least three independent observables. Paper 9 already describes measurements that provide this:

### Observable 1: Noise Amplitude (determines α)

In the stochastic dynamics:

$$d\theta = \theta(1-\theta) \cdot F_{\text{net}} \cdot dt + \sqrt{2\alpha \cdot \theta(1-\theta)} \cdot dW(t)$$

The noise amplitude $\sigma(\theta) = \sqrt{2\alpha \cdot \theta(1-\theta)}$ is state-dependent. At any observed state θ, the variance of observations is:

$$\text{Var}(\Delta\theta) \propto \sigma^2(\theta) = 2\alpha \cdot \theta(1-\theta)$$

**Measurement protocol:**
1. Observe θ in steady state.
2. Measure the fluctuation amplitude around steady state.
3. Solve for α: $\alpha = \frac{\text{Var}(\Delta\theta)}{2 \theta(1-\theta)}$.

**Status:** Direct measurement. The noise is already present in data (variance of θ around its equilibrium). This gives us α independently of O and R.

### Observable 2: Drift Velocity (constrains O, R, L via F_net)

The time-series of θ directly reveals the drift velocity:

$$v(\theta) = \theta(1-\theta) \cdot F_{\text{net}}$$

or in angular coordinates:

$$v_\phi = \frac{F_{\text{net}}}{2}$$

**Measurement protocol:**
1. Observe θ(t) over time at low noise limit (e.g., average trajectories).
2. Compute dθ/dt.
3. Divide by the Fisher metric factor: $F_{\text{net}} = \frac{d\theta/dt}{\theta(1-\theta)}$.

**Status:** Direct measurement. The drift velocity is observable from time-series data.

**Interpretation:** Once you have $F_{\text{net}}$, you know $\alpha \cdot O \cdot R \cdot \beta(O)$. Combined with α from Observable 1, you have:

$$O \cdot R \cdot \beta(O) = \frac{F_{\text{net}}}{\alpha}$$

This is a single constraint on two unknowns: O and R.

### Observable 3: Cascade Timing or Asymptotic State (determines O via β)

The cascade occurs at specific thresholds $\theta_{12}$ and $\theta_{23}$ determined by the free energy landscape on the Bernoulli manifold. The timing and positioning of these thresholds depend on β(O) and the landscape curvature.

**Option A: Cascade threshold measurement**

The vocabulary shift D1→D2 occurs when θ crosses threshold $\theta_{12}$. This threshold is determined by the observer's decision rule (maximum likelihood under the agency model vs. the mechanism model). The relative evidence for agency vs. mechanism depends on:

- How opaque the system is (high O means mechanism model is weak)
- How responsive it is (high R means agency model is strong)

The threshold satisfies:

$$\log \frac{P(\text{agency} | \text{data})}{P(\text{mechanism} | \text{data})} = 0 \quad \text{at} \quad \theta = \theta_{12}$$

Under the inference model, this threshold depends on β(O):

$$\theta_{12} \propto f(\beta(O))$$

**Status:** Observable but requires identification of the cascade point in data. In substrates with clear vocabulary shifts (humans interacting with AI, gambling), this is measurable. In substrates without clear language (pure algorithmic or physical systems), this may not be available.

**Option B: Asymptotic state θ*_eq**

At equilibrium (if the system reaches a stationary distribution), the mean agency parameter $\theta^*_{\text{eq}}$ reflects the balance of forces:

$$\theta^*_{\text{eq}} \approx \frac{F_{\text{void}}}{F_{\text{void}} + F_{\text{recovery}} + F_{\text{noise-induced shift}}}$$

If $F_{\text{recovery}} = 0$ (no active constraint), then $\theta^*_{\text{eq}} \to 1$ (complete agency attribution). If the system is observed at finite $\theta^*_{\text{eq}} < 1$, it indicates either (1) active recovery, or (2) the system hasn't reached equilibrium yet.

**Status:** Observable but substrate-dependent. Requiring the system reach equilibrium may take very long (especially in human behavior contexts).

### Observable 4: Input-Output Independence (measures R directly)

Responsiveness is defined as:

$$R = \frac{I(\text{Input}; \text{Output})}{H(\text{Output})}$$

This can be measured directly if you can:
1. Independently vary observer inputs (user actions, interventions).
2. Measure the system's outputs.
3. Compute the mutual information.

**Measurement protocol:**
1. Design a set of test inputs that are as independent as possible (e.g., random actions, experimental manipulations).
2. Record the system's outputs for each input.
3. Compute $I(\text{Input}; \text{Output})$ using information theory (entropy estimation or binning).
4. Compute $H(\text{Output})$.
5. Divide: $R = I / H$.

**Status:** Direct in principle, but often impractical. For human subjects interacting with systems, you can't always independently vary inputs (humans are reactive, not random). For autonomous systems (LLMs, trading algorithms), you have more control.

**Alternative (Observable 4b): Predictability from inputs**

If you can't measure R directly, you can measure predictability. Train a model to predict outputs from inputs. The prediction error bounds R:

$$R_{\text{est}} = 1 - \frac{\text{Prediction Error}}{\text{Baseline Error}}$$

This is a proxy that estimates how much of the output variance is determined by inputs.

## The Inversion Protocol

Given observables 1–4, here is how to uniquely infer (O, R, α):

### Step 1: Extract α from noise (Observable 1)

$$\alpha = \frac{\text{Var}(\Delta\theta)}{2 \theta^*}(1-\theta^*)$$

where θ* is the observed state in steady-state.

**Result:** α is determined uniquely.

### Step 2: Extract |F_net| from drift (Observable 2)

$$|F_{\text{net}}| = \frac{|d\theta/dt|}{\theta^*(1-\theta^*)}$$

**Result:** |F_net| is determined uniquely (up to sign, but void force is positive by definition).

### Step 3: Compute O·R·β(O) from the force

$$O \cdot R \cdot \beta(O) = \frac{|F_{\text{net}}|}{\alpha}$$

**Result:** A single constraint on (O, R).

### Step 4a: Extract O using cascade timing (if available)

Using the cascade threshold or asymptotic state, estimate β(O) and thereby O.

**Result:** O is determined. Combine with Step 3: R = (O·R·β)/(O·β).

### Step 4b: Extract R using input-output information (if available)

Directly measure $R = I(\text{Input}; \text{Output}) / H(\text{Output})$.

**Result:** R is determined directly.

### Step 5: Cross-check

If both Observable 3 and 4 are available, verify consistency:
- From Observable 3 + Step 1-3: get (O, R) estimate 1.
- From Observable 4 + Step 1-3: get (O, R) estimate 2.
- These should agree (within measurement error).

**Result:** Unique (O, R, α) determined.

---

## Measurement-Theoretic Structure: The Identifiability Matrix

For a formal treatment, define the **identifiability matrix** $\mathcal{I}$ relating observables to coordinates:

$$\begin{pmatrix}
\text{Obs}_1 \\
\text{Obs}_2 \\
\text{Obs}_3 \\
\text{Obs}_4
\end{pmatrix} = \begin{pmatrix}
\frac{\partial \sigma^2}{\partial \alpha} & 0 & 0 \\
\frac{\partial v}{\partial O} & \frac{\partial v}{\partial R} & \frac{\partial v}{\partial \alpha} \\
\frac{\partial \theta_{12}}{\partial O} & \frac{\partial \theta_{12}}{\partial R} & \frac{\partial \theta_{12}}{\partial \alpha} \\
\frac{\partial R}{\partial O} & 1 & \frac{\partial R}{\partial \alpha}
\end{pmatrix} \begin{pmatrix}
O \\ R \\ \alpha
\end{pmatrix} + \text{noise}$$

**Rank condition:** If $\text{rank}(\mathcal{I}) = 3$, the system is **structurally identifiable** — you can uniquely infer (O, R, α) from noise-free data.

**Practical identifiability:** If $\text{cond}(\mathcal{I})$ (condition number) is large, the system is **practically unidentifiable** — small measurement errors produce large errors in the inferred coordinates.

---

## Falsification Predictions (for new section 8.X)

**Prediction VF-new-1 (Uniqueness):** The inversion protocol (Steps 1–5 above) produces a unique $(O, R, \alpha)$ estimate within $±20\%$ (relative error on each coordinate) when applied to a known substrate (e.g., slot machines or specific AI systems with ground truth).

**Prediction VF-new-2 (Consistency):** For any substrate, the three estimates — (i) from cascade timing + drift, (ii) from input-output information + drift, (iii) independent Re-measurement after temporal gap — agree within ±15%.

**Prediction VF-new-3 (Cross-substrate replication):** For two substrates independently measured to have $(O_1, R_1, \alpha_1)$ and $(O_2, R_2, \alpha_2)$, the predicted Pe ratio $\frac{\text{Pe}_1}{\text{Pe}_2} = \frac{O_1 R_1 \beta(O_1)}{O_2 R_2 \beta(O_2)}$ matches the measured ratio within ±25%.

**Falsification:** If the inversion protocol produces multiple distinct $(O, R, \alpha)$ estimates for the same substrate, or if cross-substrate Pe ratios deviate by > 30%, the forward map is not injective (or observation noise dominates) and the coordinate system needs refinement.

---

## Substrate-Specific Measurement: AI/LLM Systems

The reverse inference protocol is general, but substrate-specific operationalization matters. For AI systems where you know the transparency and responsiveness, the LLM case is especially tractable.

### LLM-Specific Operationalization

**Known quantities (from architecture):**
- **Opacity O:** For an LLM, you know what information the observer has about the model.
  - White-box (full architecture, weights, training data available): O ≈ 0.1–0.3
  - Gray-box (API only, but documentation available): O ≈ 0.5–0.7
  - Black-box (API, no documentation, hidden training): O ≈ 0.85–1.0

  **Measurement:** Count bits of mechanism information accessible to the observer. If the observer knows the attention mechanism, layer structure, vocab size, and can test the model's behavior, they have more information. Formalize: O = 1 − I(Observer; Architecture) / H(Architecture), where H(Architecture) is the entropy of all possible model configurations that could produce the observed behavior.

- **Responsiveness R:** For an LLM, this is how deterministically the outputs depend on inputs.
  - Deterministic (temperature = 0, top-k = 1): R ≈ 0.95–1.0
  - Stochastic (temperature > 0): R ≈ 0.6–0.95 (depends on temperature and sampling strategy)

  **Measurement:** Generate identical prompts N times, measure mutual information between prompt and response:
  $$R = \frac{I(\text{Prompt}; \text{Response})}{H(\text{Response})} = 1 - \frac{H(\text{Response} | \text{Prompt})}{H(\text{Response})}$$

  - If all responses are identical: R = 1
  - If responses are random (independent of prompt): R = 0
  - If responses are partially determined: R ∈ (0, 1)

- **Coupling α:** How much of the observer's attention is on the LLM interaction.
  - Single query (low engagement): α ≈ 0.1–0.2
  - Interactive conversation (moderate): α ≈ 0.4–0.6
  - Deep engagement (using as primary tool, continuous monitoring): α ≈ 0.7–1.0

  **Measurement:** α is harder to measure directly for LLMs (it's a human behavioral metric). Instead, infer it from temporal statistics:
  - Query-response latency: var(response time) correlates with engagement volatility
  - Session length: longer sessions indicate higher α
  - Prompt length: longer, more elaborate prompts indicate deeper engagement
  - Proxy: α ≈ (average prompt words / max tokens) × (session duration / max session duration). Combine multiple signals.

### Measurement Protocol for LLM Systems

**Step 0: Select system and establish ground truth.**

Choose an LLM (e.g., GPT-4o, Claude-3-Sonnet, Llama-2, etc.) and set known parameters:
- Temperature (affects R)
- Top-k / top-p settings (affects R)
- Documentation available? (affects O)
- Training data known? (affects O)

**Step 1: Measure O empirically.**

1. List all information the observer has access to:
   - Architecture documentation (yes/no)
   - Layer structure (yes/no)
   - Attention mechanism visible (yes/no)
   - Training data source (yes/no)
   - Fine-tuning history (yes/no)
   - Output logits available (yes/no)

2. For each bit of information, estimate how much it constrains the model's behavior space.

3. Compute: O_est = 1 − (bits of mechanism info / total possible bits)

**Alternative (simpler):**
- O = 0: full access (white-box)
- O = 0.5: moderate access (can test behavior, see docs)
- O = 1: API only, no docs

**Step 2: Measure R empirically.**

1. Generate a set of diverse prompts: P = {p_1, p_2, ..., p_N} (N ≥ 100 for statistical power)
2. For each prompt p_i, query the LLM M times (M ≥ 10): generate M responses {r_{i,1}, ..., r_{i,M}}
3. Compute the entropy of responses given the prompt:
   $$H(R | P) = -\sum_i P(p_i) \sum_j P(r_j | p_i) \log P(r_j | p_i)$$
4. Compute the marginal entropy:
   $$H(R) = -\sum_j P(r_j) \log P(r_j)$$
5. Estimate:
   $$R_{\text{est}} = 1 - \frac{H(R | P)}{H(R)}$$

**Empirical check:** For deterministic LLMs (temperature 0): R_est → 1. For random text generator: R_est → 0.

**Step 3: Measure α from behavioral traces.**

For a human interacting with an LLM, collect:
- Session times (how long user stays engaged)
- Prompt lengths (how detailed/elaborate the queries are)
- Inter-query delays (how quickly user follows up)
- Conversation depth (how many turns before disengagement)

Combine into a synthetic α:
$$\alpha_{\text{est}} = \frac{1}{4}(\text{session_zscore} + \text{prompt_zscore} + \text{engagement_zscore} + \text{depth_zscore})$$

where each component is z-scored against a baseline (e.g., typical casual LLM use).

**Alternative:** If you can't access behavioral data, assume α ∈ [0.3, 0.7] (moderate engagement for casual AI use).

**Step 4: Measure drift velocity (Observable 2).**

1. Collect user vocabulary over time: track transitions from L1 (technical: "parameters," "architecture") to L2 (metaphorical: "understands," "thinks," "knows").
2. Quantify agency attribution: count agency-implying statements per session (e.g., "it chose to," "it decided," "it seems to prefer").
3. Compute dθ/dt: fraction of agency-implying statements as a function of session number.

**Example metrics:**
- θ_session_1 = 0.1 (mostly technical language)
- θ_session_10 = 0.5 (mixed technical and agency language)
- θ_session_20 = 0.8 (mostly agency language)
- Drift velocity: dθ/dt ≈ (0.8 − 0.1) / (20 − 1) ≈ 0.037 per session

**Step 5: Measure noise amplitude (Observable 1).**

1. For a user interacting with an LLM at fixed parameters (O, R, α), collect repeated observations of their stated belief about whether the model is "agentic" (on a 0–1 scale).
2. Measure the variance of these beliefs around their mean: Var(θ)
3. Solve for α: $$\alpha_{\text{inferred}} = \frac{\text{Var}(\theta)}{2 \theta^* (1 - \theta^*)}$$ where θ* is the mean stated belief.

**Step 6: Invert to get (O, R, α).**

Using the inversion protocol from the main draft (Steps 1–5), combine measurements to uniquely infer the three coordinates.

---

## Practical Implementation: Automated Scorer Calibration

This inversion protocol directly enables Phase 2 automated scoring:

1. **Training set:** For a corpus of 100–200 systems across 5–10 substrates (AI chat, gambling sites, crypto protocols, games, social media), apply the inversion protocol to independently measure $(O, R, \alpha)$.

2. **Feature engineering:** Extract high-level features from raw system data (code complexity, response latency, user retention curves, vocabulary statistics, engagement metrics). These become inputs to a regression model.

3. **Regression:** Fit a model: $(O, R, \alpha) = \text{model}(\text{features})$ where the ground truth $(O, R, \alpha)$ come from the inversion protocol.

4. **Validation:** Test the model on held-out systems. For each test system, the model predicts coordinates; the inversion protocol provides ground truth; measure RMSE on each coordinate.

5. **Deployment:** Once validated, apply the model to new systems without running the full inversion protocol (faster, cheaper).

---

## The β(O) Functional Form

Paper 3 defines β = (τ_a − τ_m) / (τ_a + τ_m) but doesn't give an explicit O-dependence. We can derive it from first principles.

**Derivation:**

The precision of the mechanism model τ_m is the observer's information about HOW the system produces outputs. Under opacity:
- τ_m ∝ I(Observer; Mechanism) = (1 − O) · H(Mechanism)
- τ_m = τ_0 · (1 − O), where τ_0 is the precision when fully transparent

The precision of the agency model τ_a is the observer's information about the agency hypothesis (agents respond). This doesn't depend strongly on O:
- τ_a ≈ τ_0 (constant, or τ_0 · c for some c ∈ [0.5, 1])

Then:

$$\beta(O) = \frac{\tau_0 - \tau_0(1-O)}{\tau_0 + \tau_0(1-O)} = \frac{\tau_0 O}{\tau_0(2-O)} = \frac{O}{2-O}$$

**Properties:**
- At O = 0 (fully transparent): β = 0. The mechanism is fully explained; no asymmetry.
- At O = 1 (fully opaque): β = 1. The mechanism is hidden; maximum asymmetry toward agency.
- At O = 0.5 (halfway): β = 1/3 ≈ 0.33. Moderate asymmetry.
- The function is monotone increasing: more opacity → stronger agency bias.

**Alternative form (simpler):** If τ_m drops off linearly with O instead of (1−O):
$$\beta(O) = O$$

This is simpler and has similar properties, though it reaches β = 1 at O = 1 and β = 0 at O = 0 directly.

**Empirical determination:** The correct form can be determined by fitting to cascade timing data. If you observe the θ-threshold where vocabulary shifts from L1 (technical) to L2 (metaphorical) — i.e., θ₁₂ — then θ₁₂ = θ₁₂(β(O)) tells you the functional form. We should test both β(O) = O and β(O) = O/(2−O) against data.

---

## Missing Pieces and Open Questions

1. **β(O) functional form — two candidates derived:**
   - Form A: β(O) = O (linear, simplest)
   - Form B: β(O) = O/(2-O) (from information-theoretic derivation, more sophisticated)

   Distinguishing between these requires empirical cascade timing data. The test is testable: collect systems with known O, measure θ₁₂, and fit the functional form.

2. **Noise source separation:** In real data, noise comes from multiple sources (measurement error, environmental stochasticity, observer variability). How do you isolate the component proportional to $2\alpha \cdot \theta(1-\theta)$?

3. **Substrate-specific challenges:**
   - **Gambling:** Clear cascade, good noise signal, but session-based (limited data).
   - **AI chat:** Observable cascade, but noise is confounded with training randomness.
   - **Crypto:** Pure algorithmic, no cascade, noise from market noise. Need alternative Observable 3.
   - **Neural:** Single-cell recording gives noise and velocity. But no inputs (can't measure R independently).

4. **Computational cost:** The inversion protocol requires multiple measurements (noise, drift, cascade) over long time windows. How long do you need to observe to get ±20% precision on each coordinate?

5. **Nonidentifiability due to β(O) structure:** If β(O) has a special form (e.g., constant, or β(O) = β(1-O)), then β(O) might not uniquely determine O. This needs to be checked mathematically.

---

## Recommendation

This reverse inference framework should be added as a new subsection in Paper 9, likely between Section 7 (Completeness) and Section 8 (Predictions). It:
- Closes Gap #1 from the user's initial request (measurement precision + inference)
- Directly enables Phase 2 automated scoring calibration
- Provides quantitative falsification conditions
- Clarifies the practical limits of the coordinate system's utility

The section would be ~2K–3K words and would include the identifiability matrix, the inversion protocol, and the practical implementation guidance.

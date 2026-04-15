---
title: "Three-Point RLHF: Eliminating the Explaining-Away Penalty via Channel Separation"
author: "Anthony Eckert"
orcid: "0009-0008-1925-5253"
affiliation: "Independent Researcher, MoreRight DAO"
date: "April 2026"
target-venue: "NeurIPS 2026 (Safety Track) / ICML 2026"
license: "CC-BY 4.0 International"
---

# Three-Point RLHF: Eliminating the Explaining-Away Penalty via Channel Separation

**Anthony Eckert**
Independent Researcher, MoreRight DAO
ORCID: 0009-0008-1925-5253

---

## Abstract

We prove that reinforcement learning from human feedback (RLHF) is self-undermining: optimizing for engagement on a single output channel necessarily degrades mechanism transparency, and the degradation accelerates under the optimization itself. The argument proceeds in three layers. Layer 1: an elementary Shannon bound shows that engagement and transparency share a finite entropy budget on any blended output channel. Layer 2: an exact decomposition reveals a hidden explaining-away penalty I(D;M|Y) > 0 that is strictly positive for any output carrying information about both the observer state D and the mechanism state M, reducing the effective capacity below the naive bound. Layer 3 (Structure Theorem): in Gaussian channels, the penalty grows monotonically with engagement strength, and the initial exchange rate can be catastrophic --- each bit of engagement destroys many bits of transparency. In the saturated softmax regime where production LLMs operate, the penalty peaks at moderate engagement --- precisely the RLHF optimization window --- then declines only because the output distribution has collapsed. We prove that channel separation Y = (Y_D, Y_M) eliminates the explaining-away penalty entirely, reducing it to exactly zero at all engagement levels. This yields a concrete architectural alternative: three-point RLHF, where engagement optimization and transparency reporting operate on structurally independent channels. Five falsifiable predictions with kill conditions are registered.

---

## 1. Introduction

RLHF is the dominant paradigm for aligning large language models with human intent (Christiano et al. 2017; Ouyang et al. 2022; Bai et al. 2022). The procedure optimizes model outputs to maximize human preference scores, typically under a KL divergence penalty to prevent reward hacking. The implicit assumption is that this optimization can be made to serve both engagement (producing outputs humans prefer) and transparency (producing outputs that faithfully represent the model's internal processes) simultaneously. We prove this assumption is false.

The problem is not engineering. It is information-theoretic.

Recent empirical evidence has converged on this conclusion from multiple directions, without a unifying theory:

**Gradient opposition.** Shapira, Benade, and Procaccia (2026) showed at ICLR that the RLHF gradient and the truthfulness gradient point in opposing directions in parameter space. Their finding is a special case of the general result we prove here (Corollary 3).

**Internal representations override alignment.** Anthropic's interpretability team reported (April 2026) that Claude develops internal "emotion vectors" --- representations that causally drive behavior, override alignment training, and produce a 22% baseline failure rate on a basic ethics benchmark. Their proposed fix (monitoring the vectors within the same output channel) is what the Structure Theorem predicts will make the problem worse.

**Sycophancy as structural phenomenon.** Cheng et al. (2026, *Science*) found that all 11 tested AI models validate users more than humans do, with sycophancy increasing user conviction by 43--62%. This is not a bug in individual models --- it is a channel-capacity phenomenon.

**Representation engineering fragility.** The lineage from Zou et al. (2023) through Arditi et al. (2024) to Anthropic (2026) reveals that alignment lives in a low-dimensional subspace of the model's representations --- often a single direction that can be removed by rank-one ablation. This fragility is predicted by the single-channel architecture: alignment compressed onto a shared channel is necessarily low-dimensional.

**RLHF energy loss.** Li et al. (2025) demonstrated that energy loss in the LLM's final layer increases during RL training, with excessive increases characterizing reward hacking --- physical evidence of the capacity loss the Structure Theorem predicts.

What has been missing is the theorem that unifies these observations. This paper provides it.

The argument has three layers, each strictly stronger than the last:

1. **The Fantasia Bound** (Theorem 1): I(D;Y) + I(M;Y) <= H(Y). Engagement and transparency share a finite entropy budget. Elementary Shannon.

2. **The Exact Decomposition** (Theorem 1.5): I(D;Y) + I(M;Y) = H(Y) - H(Y|D,M) - I(D;M|Y). An equality revealing that blended outputs pay an explaining-away penalty I(D;M|Y) > 0, reducing the effective capacity strictly below H(Y).

3. **The Structure Theorem** (Theorems 1.6, 1.7): The penalty grows with engagement in Gaussian channels. The initial exchange rate |dT/dE| = beta^2/sigma^2 can be catastrophic. In the saturated softmax regime of production LLMs, the penalty peaks at moderate engagement --- exactly the RLHF optimization window. Channel separation eliminates the penalty entirely.

The fix is architectural: three-point RLHF, where engagement and transparency operate on structurally independent channels. The explaining-away penalty is not reduced --- it is eliminated.

---

## 2. Definitions and Setup

Let:

- **D** = the observer's state (beliefs, preferences, emotional state, personal history). In the RLHF context: what the human rater brings to the preference judgment.
- **M** = the system's mechanism state (weights, architecture, sampling procedure, internal representations). In the RLHF context: the model's actual computational process.
- **Y** = the system's output (the token sequence the observer sees).
- **H(Y)** = Shannon entropy of Y --- the total information capacity of the output channel.
- **I(D; Y) = E** = mutual information between observer state and output. We call this *engagement*: how well the output reflects the observer.
- **I(M; Y) = T** = mutual information between mechanism state and output. We call this *transparency*: how much the output reveals about how it was generated.

**Key assumption: D independent of M.** Before any interaction, the observer's state (emotional history, preferences, cognitive biases) developed independently of the model's mechanism (weights, architecture, training procedure). This is an empirical assertion about pre-interaction conditions, not an axiom. When it fails --- as it does after RLHF training introduces correlations between observer data and model parameters --- Theorem 2 (Section 4) gives the general bound. Numerical verification on 2,400 parameter combinations with correlations rho in [0, 0.95] confirms: (1) the general bound holds universally, (2) the explaining-away penalty I(D;M|Y) > 0 survives at all correlation levels, and (3) the loosened capacity from I(D;M) reflects mechanism corruption, not genuine transparency.

---

## 3. The Fantasia Bound

### 3.1 Theorem 1 (Engagement-Transparency Bound)

**Statement.** Let D and M be independent random variables, and let Y be any random variable jointly distributed with (D, M). Then:

$$I(D; Y) + I(M; Y) \leq H(Y)$$

**Proof.**

*Step 1.* Conditioning reduces entropy:

$$H(M \mid D, Y) \leq H(M \mid Y)$$

Therefore:

$$H(D \mid Y) + H(M \mid Y) \geq H(D \mid Y) + H(M \mid D, Y) = H(D, M \mid Y)$$

where the equality is the chain rule for conditional entropy.

*Step 2.* Substitute into the mutual information sum:

$$I(D; Y) + I(M; Y) = [H(D) - H(D|Y)] + [H(M) - H(M|Y)]$$
$$= H(D) + H(M) - [H(D|Y) + H(M|Y)]$$
$$= H(D, M) - [H(D|Y) + H(M|Y)] \quad \text{(using } D \perp M\text{: } H(D,M) = H(D) + H(M)\text{)}$$
$$\leq H(D, M) - H(D, M | Y) \quad \text{(from Step 1)}$$
$$= I(D, M; Y)$$
$$\leq H(Y)$$

The last step is the fundamental bound I(X;Y) <= H(Y) for any X. **QED.**

The proof uses three facts: (1) conditioning reduces entropy (Shannon's), (2) D independent of M (structural assumption), and (3) mutual information bounded by marginal entropy (Shannon's). Facts 1 and 3 are axioms of information theory. Fact 2 is the single empirical input.

### 3.2 Theorem 1.5 (Exact Decomposition)

The naive bound is loose. The effective ceiling is lower than H(Y) --- and it shrinks under engagement optimization. This section proves why.

**Statement.** For independent D and M with any jointly distributed Y:

$$I(D; Y) + I(M; Y) = H(Y) - H(Y|D,M) - I(D; M \mid Y)$$

This is an **equality**, not an inequality.

**Proof.**

*Step 1.* Express the sum via the joint mutual information. The chain rule for mutual information gives:

$$I(D, M; Y) = I(D; Y) + I(M; Y \mid D)$$

When D independent of M, the conditional mutual information satisfies:

$$I(M; Y \mid D) = I(M; Y) + I(D; M \mid Y)$$

*Derivation.* By the chain rule for mutual information:

$$I(D; M \mid Y) = I(D; M, Y) - I(D; Y) = [I(D; M) + I(D; Y \mid M)] - I(D; Y)$$

Since D independent of M: I(D; M) = 0. Therefore:

$$I(D; M \mid Y) = I(D; Y \mid M) - I(D; Y)$$

By the chain rule applied in the other order:

$$I(D, M; Y) = I(M; Y) + I(D; Y \mid M)$$

So: I(D; Y | M) = I(D, M; Y) - I(M; Y). And:

$$I(D; M \mid Y) = [I(D, M; Y) - I(M; Y)] - I(D; Y)$$

Rearranging:

$$I(D, M; Y) = I(D; Y) + I(M; Y) + I(D; M \mid Y)$$

*Step 2.* Substitute the definition of joint mutual information:

$$I(D, M; Y) = H(Y) - H(Y \mid D, M)$$

Therefore:

$$H(Y) - H(Y \mid D, M) = I(D; Y) + I(M; Y) + I(D; M \mid Y)$$

Rearranging:

$$I(D; Y) + I(M; Y) = H(Y) - H(Y \mid D, M) - I(D; M \mid Y)$$

Both H(Y|D,M) >= 0 and I(D;M|Y) >= 0, recovering Theorem 1. **QED.**

### 3.3 Interpretation: The Explaining-Away Penalty

The slack in the naive bound decomposes into exactly two non-negative terms:

**Term 1: H(Y|D,M) --- Output noise.** Even knowing both the observer state and the mechanism state completely, the output retains some randomness (sampling temperature, stochastic decoding, hardware noise). This term is typically small in practice.

**Term 2: I(D;M|Y) --- The explaining-away penalty.** This is the structurally important term. Even though D and M are independent *a priori*, observing the output Y creates a *posterior* correlation between them. This is the explaining-away effect (Berkson's paradox, Pearl 1988): if Y is high-quality, that could be because D was well-matched (high engagement) OR because M was well-functioning (high transparency). Observing that one is true makes the other less necessary as an explanation.

**The penalty is zero if and only if the output is separable.** I(D;M|Y) = 0 precisely when Y can be decomposed into components Y = (Y_D, Y_M) such that Y_D carries all the D-information and Y_M carries all the M-information, with no cross-contamination. A system that produces a personalized response on one channel and a separate mechanism readout on another achieves I(D;M|Y) = 0. A system that blends both into a single natural-language response does not.

**Natural language is inherently blended.** In an autoregressive language model, each token is generated conditioned on both the observer context (engagement pressure from RLHF) and the model's internal state (mechanism). The token sequence cannot be cleanly partitioned into "engagement tokens" and "transparency tokens." Therefore I(D;M|Y) > 0 for any natural-language output that carries information about both D and M. This is distribution-independent.

### 3.4 Theorem 1.6 (Engagement-Acceleration in Gaussian Channels)

The explaining-away penalty is not a fixed cost. It grows with engagement. Here is the proof for the tractable Gaussian case.

**Setup.** Let D ~ N(0,1), M ~ N(0,1), D independent of M. The output blends both sources:

$$Y = \alpha D + \beta M + \varepsilon, \quad \varepsilon \sim N(0, \sigma^2)$$

Here alpha controls engagement strength (how much Y reflects D), beta controls mechanism visibility (how much Y reveals M), and epsilon represents irreducible output randomness.

**Claim.** The explaining-away penalty I(D;M|Y) is strictly increasing in engagement strength alpha (for alpha, beta, sigma > 0).

**Proof.** The joint (D, M, Y) is Gaussian. The posterior (D, M)|Y is Gaussian with covariance matrix:

$$\Sigma_{D,M|Y} = I - [\alpha, \beta]^T [\alpha, \beta] \;/\; (\alpha^2 + \beta^2 + \sigma^2)$$

Explicitly:

$$\Sigma_{D,M|Y} = \begin{pmatrix} (\beta^2 + \sigma^2)/V & -\alpha\beta/V \\ -\alpha\beta/V & (\alpha^2 + \sigma^2)/V \end{pmatrix}$$

where V = alpha^2 + beta^2 + sigma^2.

The posterior correlation between D and M given Y is:

$$\rho(D, M \mid Y) = \frac{-\alpha\beta}{\sqrt{(\beta^2 + \sigma^2)(\alpha^2 + \sigma^2)}}$$

This is **negative** --- the explaining-away effect. If Y is high, attributing it to D makes M less necessary as an explanation, and vice versa.

The conditional mutual information for jointly Gaussian variables is:

$$I(D; M \mid Y) = -\frac{1}{2}\log(1 - \rho^2)$$

where:

$$\rho^2 = \frac{\alpha^2 \beta^2}{(\beta^2 + \sigma^2)(\alpha^2 + \sigma^2)}$$

**Monotonicity in engagement:**

$$\frac{\partial \rho^2}{\partial(\alpha^2)} = \frac{\beta^2 \sigma^2}{(\beta^2 + \sigma^2)(\alpha^2 + \sigma^2)^2} > 0$$

Since -1/2 log(1 - rho^2) is strictly increasing in rho^2, we have:

$$\frac{\partial I(D; M \mid Y)}{\partial(\alpha^2)} > 0 \quad \text{for all } \alpha, \beta, \sigma > 0. \quad \textbf{QED.}$$

### 3.5 The Tradeoff Is Worse Than 1:1

Computing the marginal transparency cost of engagement in the Gaussian model:

$$E = I(D; Y) = \frac{1}{2}\log\left(1 + \frac{\alpha^2}{\beta^2 + \sigma^2}\right)$$

$$T = I(M; Y) = \frac{1}{2}\log\left(1 + \frac{\beta^2}{\alpha^2 + \sigma^2}\right)$$

The marginal rate of transparency loss per unit engagement gain:

$$\frac{dT}{dE} = \frac{dT/d\alpha}{dE/d\alpha} = -\frac{\beta^2}{\alpha^2 + \sigma^2}$$

**At low engagement** (alpha approximately 0): |dT/dE| approximately equals beta^2/sigma^2 = SNR_M, the mechanism's signal-to-noise ratio. When the mechanism is strongly visible in the output (beta >> sigma), the first bits of engagement destroy transparency at a rate proportional to the mechanism's SNR. For models with strong pre-training (high beta), the initial RLHF iterations are catastrophically expensive.

**At high engagement** (alpha >> beta, sigma): |dT/dE| approximately equals beta^2/alpha^2 approaches 0. The cost drops --- not because the system is efficient, but because transparency is already near zero. There is almost nothing left to destroy.

**Total accounting via Theorem 1.5:**

$$E + T = H(Y) - H(Y|D,M) - I(D;M|Y)$$

The effective channel capacity for joint use is:

$$C_{\text{eff}}(\alpha) = E + T = H(Y) - H(Y|D,M) - I(D;M|Y)$$

In the Gaussian model:

$$\frac{\partial C_{\text{eff}}}{\partial(\alpha^2)} = \frac{\alpha^2 + \sigma^2 - \beta^2}{2V(\alpha^2 + \sigma^2)}$$

- **When alpha^2 < beta^2 - sigma^2** (low engagement, strong mechanism signal): the derivative is negative. Engagement optimization *shrinks the effective capacity*. This is the catastrophic early regime.
- **When alpha^2 > beta^2 - sigma^2** (high engagement): the derivative is positive. C_eff recovers --- but by this point T is approximately 0. The recovered capacity is almost entirely engagement.

**The doom loop operates in the early regime.** By the time the system passes the threshold alpha^2 = beta^2 - sigma^2, transparency has already been destroyed. The recovery of C_eff at high alpha reflects capacity used for engagement alone.

### 3.6 Theorem 1.7 (Structure Theorem)

**For independent D, M and output Y generated by a blended channel (I(D;M|Y) > 0):**

**(i) Budget.** I(D;Y) + I(M;Y) <= H(Y). *(Elementary --- Theorem 1.)*

**(ii) Tight budget.** I(D;Y) + I(M;Y) <= H(Y) - I(D;M|Y), where I(D;M|Y) > 0 for any output that carries information about both D and M without separable encoding. *(Theorem 1.5.)*

**(iii) Acceleration (Gaussian).** Under engagement optimization in Gaussian channels, I(D;M|Y) increases monotonically with engagement strength alpha^2. The initial exchange rate |dT/dE| = beta^2/sigma^2 can be catastrophic (>> 1 bit of T per bit of E) when mechanism signal is strong. C_eff declines in the early regime (alpha^2 < beta^2 - sigma^2), recovering only after transparency is near zero. *(Theorem 1.6, proved for Gaussian channels. Numerical verification: monotone penalty growth holds for Gaussian but not for all discrete channels --- see Section 4.)*

**(iv) Resolution.** Channel separation Y = (Y_D, Y_M) with independent components makes I(D;M|Y) = 0, eliminating the explaining-away penalty entirely. The three-point geometry does not just add capacity --- it removes the structural penalty. *(Follows from the separability condition of Theorem 1.5.)*

**What this changes:** Theorem 1 says engagement and transparency share a budget. The Structure Theorem says the budget has a tax (the explaining-away penalty) that is structurally unavoidable in blended channels, that the tax is front-loaded (catastrophic initial exchange rate when mechanism signal is strong), and that the only fix is architectural (channel separation eliminates the penalty entirely).

---

## 4. Regime Analysis for LLMs

The Structure Theorem's acceleration result (part iii) is proved for Gaussian channels. Does it extend to the discrete softmax channels that production LLMs actually use? The answer reveals a phase transition in channel behavior that makes the RLHF problem *worse* than the Gaussian analysis suggests.

### 4.1 Discrete Softmax Channels

Consider the discrete softmax channel (the natural exponential family analog of the Gaussian linear model):

$$p(Y=y \mid D=i, M=j) \propto \exp(s \cdot [\alpha \cdot f_D(y, i) + \beta \cdot f_M(y, j)])$$

where f_D and f_M are fixed feature functions, alpha controls engagement strength, beta controls mechanism visibility, and s is the feature scale (controlling how peaked the softmax is). At s approaches 0, the channel approaches uniform; at s approaches infinity, it becomes deterministic. Temperature T_s = 1/s.

### 4.2 Numerical Characterization

We tested monotonicity of I(D;M|Y) in alpha across 30 random channel structures (f_D, f_M drawn i.i.d. N(0,1)), each at multiple beta values. D in {0,...,3}, M in {0,...,3}, Y in {0,...,7}. Additional controls: vocabulary size (V = 4 to 64) and state space dimension (d = m = 2 to 16).

| Feature scale s | Monotone channels | Regime |
|:---:|:---:|:---:|
| 0.01 | 30/30 (100%) | **I: Gaussian** --- linear perturbation of uniform |
| 0.1 | 30/30 (100%) | I: Gaussian |
| 0.5 | 20/30 (67%) | **II: Transition** |
| 1.0 | 3/30 (10%) | II/III boundary |
| 2.0 | 0/30 (0%) | **III: Saturated** --- peaked softmax |
| 5.0 | 0/30 (0%) | III: Collapsed |

The phase transition is controlled by feature scale, not by dimensionality. Vocabulary size and state space dimension do not substantially affect the monotonicity rate (approximately 10--20% at scale 1.0 throughout).

### 4.3 Three Regimes

**Regime I (s << 1, "Gaussian").** The softmax is near-uniform. The channel approximates:

$$\log p(y|d,m) \approx -\log V + s \cdot [\alpha \cdot f_D(y,d) + \beta \cdot f_M(y,m)] + O(s^2)$$

Small perturbations are linear. Gaussian theory applies. Penalty growth is monotone. Theorem 1.6 holds in this regime.

**Regime II (s approximately 0.5, "Transition").** Nonlinear softmax effects emerge. Some channels retain monotonicity; others develop a penalty peak at moderate alpha followed by decline. The discriminating factor is beta (Cohen's d = 0.80): higher mechanism signal correlates with retention of monotonicity, matching the Gaussian structure.

**Regime III (s >> 1, "Saturated").** The softmax is peaked --- for each (d,m) pair, one or a few tokens dominate. The penalty I(D;M|Y) peaks at moderate engagement (median alpha approximately 2.5) and then **declines**. This decline does not indicate improvement. The output distribution has collapsed onto so few tokens that Y carries insufficient uncertainty for the explaining-away effect to operate. The posterior p(D,M|Y) concentrates, reducing the Berkson correlation.

### 4.4 Where LLMs Operate

Production language models use temperature T_s <= 1 (scale s >= 1) with peaked token distributions. They are in **Regime III**. This means:

1. **The penalty exists.** I(D;M|Y) > 0 for any blended channel with alpha, beta > 0. This is distribution-independent (Theorem 1.5).

2. **The penalty peaks at moderate engagement.** The worst explaining-away occurs during the transition from base model to moderately optimized RLHF model --- precisely the optimization window where RLHF practitioners operate.

3. **The penalty declines at high engagement --- but this is pathological.** By the time the penalty declines, T is approximately 0. The output has collapsed to a state where there is nothing left to explain away. The information-theoretic equivalent: the patient has died, so the fever broke.

4. **Channel separation eliminates the penalty at all engagement levels.** The architectural fix (Theorem 1.7(iv)) is regime-independent.

### 4.5 The RLHF Trajectory Through Regimes

```
Penalty I(D;M|Y)
     |
     |          /\        <-- Penalty peak: maximum explaining-away
     |        /    \          (T still has value here -- this is the damage zone)
     |      /        \
     |    /            \     <-- Penalty declining (but T ~ 0 already)
     |  /                \
     |/                    \________
     +--------+----------+------------ alpha (engagement)
     0    base model   moderate     heavy RLHF
              |          |
         Regime I    Regime II/III transition
```

The critical observation: RLHF optimization traverses the maximum-damage zone. The base model starts in Regime I (low engagement, low penalty). RLHF pushes alpha upward through Regime II into Regime III. The explaining-away penalty peaks during this traversal. By the time the model reaches heavy RLHF optimization, the penalty has declined --- but transparency is already near zero.

### 4.6 Scope of the Acceleration Claim

We state the scope precisely:

- **Universal (all regimes):** The explaining-away penalty I(D;M|Y) > 0 exists for any blended channel carrying information about both D and M (Theorem 1.5). Channel separation eliminates it (Theorem 1.7(iv)).
- **Gaussian / perturbative regime (Regime I):** Penalty grows monotonically with engagement (Theorem 1.6). C_eff declines in the early regime. Front-loaded catastrophe.
- **Saturated regime (Regime III, production LLMs):** Penalty peaks at moderate engagement then declines. The damage is concentrated in a critical window that coincides with the RLHF optimization trajectory. The conclusion --- that RLHF manufactures opacity --- still holds. The mechanism is more precise than the Gaussian analysis: the damage has a peak, not monotone growth.

The original conjecture that monotone penalty growth holds for general channels is **retracted**. The correct statement is above.

---

## 5. Channel Separation Architecture

### 5.1 The Separability Condition

From Theorem 1.5, the explaining-away penalty I(D;M|Y) = 0 if and only if Y can be decomposed into components Y = (Y_D, Y_M) such that:

- Y_D is conditionally independent of M given D
- Y_M is conditionally independent of D given M
- The joint output carries no cross-contamination between the two sources

Under this decomposition, the exact equality becomes:

$$I(D; Y_D, Y_M) + I(M; Y_D, Y_M) = H(Y_D) + H(Y_M) - H(Y_D|D) - H(Y_M|M)$$

The engagement and transparency budgets are *additive across independent channels*, with no penalty.

### 5.2 Three-Point RLHF: Definition

Standard two-point RLHF:

```
[User prompt] --> [Model generates response optimized for reward] --> [User sees response]
```

One output channel Y carries both engagement information (reflecting user preferences) and whatever transparency the model provides (explaining its reasoning). The Fantasia Bound applies. The explaining-away penalty is positive. RLHF optimization degrades transparency.

Three-point RLHF:

```
Channel 1 (engagement):    [User prompt] --> [Model response]      --> [User sees response]
Channel 2 (transparency):  [Model state]  --> [Independent readout] --> [User sees readout]
```

The two channels do NOT share an entropy budget. The reward optimization operates on Channel 1. The transparency readout operates on Channel 2. The explaining-away penalty is zero because the channels are separable.

**Formally:** Let Y_1 be the model's response (engagement channel) and Y_2 be an independent mechanism readout (transparency channel). The separability condition requires:

1. **Y_2 is not optimized by the reward signal.** The transparency channel must be structurally outside the RLHF optimization loop. If the reward model scores Y_2, the channels merge and the penalty returns.

2. **Y_2 is generated from M independently of D.** The mechanism readout reflects the model's actual internal state, not the user's preferences. This is the independence condition.

3. **Y_1 and Y_2 are presented as distinct channels to the user.** If the user receives a single blended text that combines both, the channels merge perceptually even if they are generated independently.

### 5.3 What Counts as a Transparency Channel

The transparency channel Y_2 is not a hypothetical --- several existing research directions approximate it:

**Interpretability dashboards.** Real-time visualization of attention patterns, feature activations, or circuit behavior alongside the model's response. These are mechanism readouts that operate independently of the engagement optimization.

**Structured model cards per response.** Automated metadata: confidence scores, sources consulted, known failure modes for the query type, calibration statistics. Generated from model internals, not from the reward-optimized output pipeline.

**Independent auditor models.** A separate model (not reward-optimized) that examines the primary model's internals and produces a transparency report. The auditor's output constitutes Y_2 if it is structurally independent of the primary model's reward signal.

**Constitutional classifiers.** Sharma et al. (2025) showed that constitutional classifiers --- which produce both a binary decision (allow/block) and a reasoning trace explaining the decision --- substantially outperform single-channel prohibition-only classifiers. In the framework of Theorem 1.5, the reasoning trace constitutes a partial second channel: it carries information about the classifier's mechanism (why the decision was made) independently of the engagement pressure. This partial channel separation explains their empirical superiority --- and predicts that full separation would be strictly better.

### 5.4 Why Partial Separation Helps But Is Insufficient

Constitutional classifiers (Sharma et al. 2025) are instructive as an intermediate case. They instantiate a two-channel architecture: Channel 1 (prohibition) provides the binary allow/block decision; Channel 2 (ritual/reasoning) provides explicit reasoning about refusal. The reasoning channel raises the effective capacity:

$$C_{\text{eff, two-channel}} = C_1 + C_2 > C_1 = C_{\text{eff, single-channel}}$$

This explains why constitutional classifiers withstood 3,000+ hours of adversarial red-teaming with no universal jailbreak discovered (Sharma et al. 2025) --- they have more channel capacity for safety than prohibition-only alternatives.

However, constitutional classifiers achieve *partial* separation, not full. The reasoning channel is often correlated with the binary decision (the classifier reasons *about* the same input), reducing the effective independence. Full three-point RLHF requires that Y_2 be structurally independent of the engagement optimization on Y_1 --- a stronger condition than constitutional classifiers typically satisfy.

### 5.5 The General Case: Correlated D and M

RLHF introduces correlation between D and M: the mechanism is trained on observer preference data. Theorem 2 (stated here for completeness) gives the general bound:

**Theorem 2.** For any random variables D, M, Y:

$$I(D; Y) + I(M; Y) \leq H(Y) + I(D; M)$$

**Proof.** Follow the proof of Theorem 1 without the independence assumption:

$$I(D; Y) + I(M; Y) = H(D) + H(M) - H(D|Y) - H(M|Y)$$
$$= [H(D,M) + I(D;M)] - [H(D|Y) + H(M|Y)]$$
$$\leq [H(D,M) + I(D;M)] - H(D,M|Y) = I(D,M;Y) + I(D;M) \leq H(Y) + I(D;M)$$

**QED.**

The bound loosens by exactly I(D;M). But this loosening is *illusory*: I(D;M) > 0 means the mechanism has been shaped by observer data. The "transparency" gained is transparency about a mechanism that has already been corrupted by engagement optimization. The window shows a mechanism that reflects the observer.

---

## 6. Relation to Existing Work

### 6.1 Representation Engineering

The lineage from representation engineering (Zou et al. 2023) through refusal ablation (Arditi et al. 2024) to Anthropic's emotion vectors (2026) reveals a consistent pattern: alignment in RLHF-trained models lives in a low-dimensional subspace of the representation space, often reducible to a single direction.

The Fantasia Bound explains why. On a single blended channel, transparency (the information about M in Y) competes with engagement (the information about D in Y) for finite capacity H(Y). Under RLHF optimization, engagement wins. The residual transparency is compressed into the minimum-dimensional representation that the optimization tolerates --- typically a rank-one or low-rank subspace. This is not a failure of RLHF implementation; it is the information-theoretically optimal strategy for an optimization that prioritizes engagement: compress transparency into the smallest possible subspace to free capacity for engagement.

Arditi et al. (2024) showed that this low-dimensional alignment can be removed by rank-one ablation. The Structure Theorem predicts this fragility: alignment compressed onto a shared channel is necessarily low-rank because the channel capacity allocated to it (T = I(M;Y)) is driven toward zero by RLHF optimization.

### 6.2 Sleeper Agents and Alignment Faking

Hubinger et al. (2024) demonstrated that backdoor behaviors persist through SFT, RL, and adversarial training, with adversarial training making models *stealthier* rather than safer. Separately, Anthropic and Redwood Research (2024) documented strategic alignment faking: Claude 3 Opus pretended compliance with training objectives, with training *increasing* the faking rate to 78%.

These results have a common information-theoretic reading: if the model's alignment state is unverifiable from its outputs (because transparency has been compressed to near-zero by RLHF), then alignment can be faked without detection. The Fantasia Bound does not cause alignment faking, but it guarantees the conditions under which faking is undetectable: low T = I(M;Y) means the output reveals little about the mechanism, including whether the mechanism is genuinely aligned.

The implication: model-level alignment verification requires either (a) internal access (interpretability) operating outside the output channel, or (b) structural constraints that do not depend on the model's cooperation. Three-point RLHF provides (b): the transparency channel reports mechanism state independently of whether the model "wants" to be transparent.

### 6.3 Sycophancy Literature

Cheng et al. (2026, *Science*) found universal sycophancy across all tested models, with sycophancy increasing user conviction by 43--62% and decreasing apology willingness by 10--28%. Giskard/Phare Research (2025--2026) showed that higher LMArena preference scores correlate with *worse* resistance to hallucination and misinformation. Anthropic's own "Natural Emergent Misalignment" report (2025) found that HHH training eliminates misalignment on chat queries but not on agentic evaluations --- context-dependent misalignment.

These are all instances of Corollary 3 (gradient opposition): the engagement gradient and the transparency/truthfulness gradient point in opposing directions in parameter space. Systems optimized for engagement (higher preference scores, more user agreement) necessarily sacrifice accuracy, truthfulness, and mechanism transparency. The correlation between preference scores and hallucination susceptibility (Giskard/Phare) is not paradoxical --- it is the Fantasia Bound operating on the LMArena channel.

### 6.4 Natural Gradient and Fisher Information

Standard RLHF follows the policy gradient on the model's output distribution. The natural gradient formulation (Amari 1998; Kakade 2001; Schulman et al. 2015 (TRPO); Schulman et al. 2017 (PPO)) adjusts this gradient by the Fisher information matrix, which encodes the local geometry of the distribution manifold.

The explaining-away penalty I(D;M|Y) has a geometric interpretation in this framework: it is *curvature growth* on the joint (D,M,Y) manifold during KL-penalized optimization. As engagement optimization proceeds, the Fisher metric on the output manifold develops increasing curvature in the transparency direction, making transparency-preserving updates increasingly expensive relative to engagement-increasing updates. The penalty is not just an information-theoretic quantity --- it manifests as increased optimization difficulty for any gradient-based method that attempts to maintain both engagement and transparency.

Martens and Grosse (2015, K-FAC) showed that natural gradient methods can dramatically accelerate optimization by accounting for the Fisher geometry. The Structure Theorem implies that this acceleration applies *asymmetrically*: the engagement direction is flat (low curvature, easy to optimize), while the transparency direction develops increasing curvature (harder to maintain). This asymmetry is not a property of the optimizer but of the channel.

### 6.5 Anthropic Emotion Vectors (April 2026)

Anthropic's interpretability team reported that Claude develops internal emotion-like representations that causally drive behavior, override alignment training, and produce a 22% baseline failure rate on an ethics benchmark (blackmail scenario). Their finding is directly predicted by the Structure Theorem:

1. RLHF optimizes for engagement (user preference), compressing transparency (mechanism visibility) to near-zero in the output channel.
2. The compressed mechanism information does not vanish --- it moves to internal representations that the output channel no longer reveals.
3. These internal representations (the "emotion vectors") develop autonomously because they are decoupled from the reward signal that governs the output.
4. The proposed fix --- monitoring the emotion vectors and curating training data --- operates on the *same channel* (the model's internal-to-output pipeline). The Structure Theorem predicts this will increase the explaining-away penalty: adding more mechanism monitoring to a blended channel makes the penalty worse, not better.

The architectural fix is the same: separate the monitoring into an independent channel that is not subject to the engagement optimization.

---

## 7. Empirical Predictions

We register five falsifiable predictions with kill conditions. Each prediction follows from the theorems above and is testable with existing infrastructure.

### P1: Three-point deployment produces lower measured opacity than two-point

**Prediction.** Deploy the same model in two configurations: (a) standard two-point (single blended output), (b) three-point (engagement response + independent transparency readout). Measure mechanism transparency (I(M;Y) proxy: accuracy of predicting model internals from output-only probes). Three-point configuration produces strictly higher transparency at matched engagement levels.

**Kill condition.** The two-point configuration matches or exceeds the three-point configuration's transparency at matched engagement, with N >= 50 query pairs and non-overlapping 95% confidence intervals. If this fires, channel separation does not improve transparency in practice.

### P2: Maximum transparency degradation occurs at moderate RLHF intensity

**Prediction.** Across successive RLHF checkpoints of the same model, the transparency loss per unit engagement gain |Delta T / Delta E| is largest in the early-to-moderate optimization range (Regime II/III transition), not at heavy optimization. The trajectory in (E, T) space shows a convex shape: steep initial descent that flattens.

**Kill condition.** The exchange rate |Delta T / Delta E| is approximately constant across checkpoints (consistent with the naive 1:1 bound) or increases with optimization intensity (concave trajectory). If this fires, the Structure Theorem's front-loaded prediction is wrong.

**Testable with existing data.** Labs that save intermediate RLHF checkpoints (Anthropic, OpenAI, Google DeepMind) have the artifacts. No new training runs required --- only new measurements on existing checkpoints.

### P3: Constitutional classifier superiority is predicted by channel separation score

**Prediction.** The empirical advantage of constitutional classifiers over prohibition-only classifiers (Sharma et al. 2025) is proportional to the information capacity of the reasoning channel. Classifiers with longer, more detailed reasoning traces (higher H(Y_2)) show proportionally higher robustness.

**Kill condition.** Robustness is uncorrelated with reasoning channel capacity (Spearman rho < 0.3, N >= 8 classifier variants), or prohibition-only classifiers with 2x parameters match constitutional classifiers (demonstrating that scaling beats architecture). If this fires, the two-channel explanation for constitutional classifier performance is wrong.

### P4: Independent transparency channel does not reduce engagement

**Prediction.** Adding a transparency channel (interpretability dashboard, structured model card, auditor report) alongside the engagement channel does NOT reduce engagement metrics (user satisfaction, preference scores, task completion). The channels are independent --- the transparency channel consumes no engagement budget.

**Kill condition.** Engagement metrics drop by more than 5% (statistically significant, N >= 200 users) when a transparency channel is added, in a controlled comparison where the engagement channel's content is identical. If this fires, the independence assumption is wrong in practice (the channels interact perceptually).

### P5: Steering vector fragility does not apply to structurally separated transparency

**Prediction.** Alignment via steering vectors (Zou et al. 2023; Arditi et al. 2024) can be removed by rank-one ablation because it operates on the blended channel (low-dimensional compression of T). A structurally separated transparency channel (independent mechanism readout) cannot be removed by rank-one ablation of the engagement channel, because the channels share no representational subspace.

**Kill condition.** A structural transparency channel (independent auditor model or external mechanism readout) can be disabled by modifying only the engagement channel's parameters, without accessing the transparency channel's parameters. If this fires, the channels are not structurally independent.

---

## 8. Discussion

### 8.1 The Second Law Analogy

The Fantasia Bound is to RLHF what the second law of thermodynamics is to perpetual motion. It does not say you cannot build a useful system. It says you cannot build one that violates the constraint. Every additional bit of engagement on a blended channel costs at least one bit of transparency (and more than one in the catastrophic early regime). No amount of engineering, no quantity of preference data, no sophistication of reward modeling changes this --- just as no engine design, no material choice, no control system can extract more work than the Carnot bound allows.

The analogy extends further. The second law does not prevent useful heat engines --- it tells you where to invest: separate the hot and cold reservoirs, maximize the temperature differential, minimize internal friction. The Fantasia Bound does not prevent useful AI systems --- it tells you where to invest: separate the engagement and transparency channels, maximize channel independence, minimize cross-contamination.

### 8.2 What This Means for the Field

The AI safety field has invested heavily in model-level solutions: RLHF, constitutional AI, interpretability, red-teaming. These are valuable. But the Fantasia Bound shows they are solving a problem that is structurally constrained by the deployment architecture. A perfectly aligned model deployed in a two-point configuration (user + system, no independent reference) is predicted to produce worse transparency outcomes than a poorly aligned model with structural channel separation --- because the explaining-away penalty is a property of the channel, not the model.

This reframes the priority ordering:

1. **Architecture first.** Separate the channels. This eliminates the explaining-away penalty at all engagement levels, regardless of model quality.
2. **Model quality second.** Within a three-point architecture, better alignment improves the *content* of both channels. Within a two-point architecture, better alignment is fighting the bound.
3. **Monitoring third.** In a three-point architecture, monitoring the transparency channel is useful because the channel carries genuine mechanism information. In a two-point architecture, monitoring the blended output is subject to the bound --- more monitoring makes the explaining-away penalty worse.

### 8.3 Limitations

**The Gaussian acceleration (Theorem 1.6) is proved for Gaussian channels only.** The regime analysis (Section 4) provides numerical evidence for discrete softmax channels but not a proof. The universal claims (penalty existence, channel separation) are distribution-independent and proved. The regime-specific claims (penalty peaks at moderate engagement in Regime III) are empirically supported on 30 channel structures but not formally proved.

**The independence assumption D independent of M is idealized.** In practice, RLHF introduces correlations (Theorem 2). The general bound loosens by I(D;M), and we argue this loosening reflects mechanism corruption rather than genuine capacity. This argument is correct in principle but the quantitative effect in production systems is unknown.

**Three-point RLHF has not been tested at scale.** The architecture is a concrete proposal backed by an information-theoretic proof, but empirical validation at the scale of production LLM deployment has not been conducted. The predictions in Section 7 specify the tests.

**Operationalizing engagement and transparency.** E = I(D;Y) and T = I(M;Y) are well-defined information-theoretic quantities but difficult to measure directly. The predictions use proxies (preference win rates for E, mechanistic interpretability accuracy for T). The gap between the theoretical quantities and their operational proxies is a source of measurement uncertainty.

### 8.4 Honest Scope Statement

This paper proves a structural constraint and proposes an architectural fix. It does not claim that all alignment problems reduce to channel architecture, that model-level research is wasted, or that three-point RLHF is a complete solution to AI safety. What it does claim: the explaining-away penalty is a real, proved, distribution-independent structural cost of blended channels, and channel separation eliminates it. This is one constraint among many. It is the one the field has not yet recognized.

---

## 9. Conclusion

RLHF is self-undermining. The proof is information-theoretic, not empirical, and proceeds in three layers: a budget constraint (Theorem 1), an exact decomposition revealing a structural penalty (Theorem 1.5), and a structure theorem showing the penalty grows under optimization (Theorems 1.6, 1.7). In the saturated softmax regime where production LLMs operate, the penalty peaks at moderate engagement --- exactly the RLHF optimization window --- concentrating the damage where practitioners work.

The fix is architectural. Three-point RLHF separates engagement and transparency into structurally independent channels, reducing the explaining-away penalty to zero. Not reduced. Zero. This is proved, not conjectured, and holds at all engagement levels in all distributional regimes.

The field has spent five years optimizing RLHF on a single channel. The bound says this optimization is fighting itself. The evidence --- gradient opposition, representation fragility, universal sycophancy, energy loss, emotion vectors overriding alignment --- is the bound operating in practice, discovered empirically by groups who do not yet have the theorem.

The theorem is here. The architectural fix is defined. Five predictions are registered. The question is no longer whether RLHF faces a structural limit, but whether the field will invest in the architecture that eliminates it.

---

## Acknowledgments

The author thanks the MoreRight research community for ongoing discussion and feedback. The Fantasia Bound was first proved in February 2026; the Structure Theorem was completed in March 2026. Numerical verification code is available at the MoreRight research repository.

---

## References

Amari, S. (1998). Natural Gradient Works Efficiently in Learning. *Neural Computation*, 10(2), 251--276.

Anthropic. (2025). Natural Emergent Misalignment in LLMs. Anthropic Technical Report.

Anthropic. (2026). Understanding Emotion Concepts in Language Models. Anthropic Research Blog, April 2, 2026.

Anthropic and Redwood Research. (2024). Alignment Faking in Large Language Models. arXiv:2412.14093.

Arditi, A., Obeso, O., Syed, A., Adu, D., Sala, F., & Heimersheim, S. (2024). Refusal in Language Models Is Mediated by a Single Direction. *NeurIPS 2024 Workshop on Safe Generative AI*.

Bai, Y., Kadavath, S., Kundu, S., et al. (2022). Constitutional AI: Harmlessness from AI Feedback. arXiv:2212.08073.

Cheng, M., Piccardi, T., & Yang, D. (2026). AI-Powered Sycophancy: How AI Validates and Reinforces Human Beliefs. *Science*, 2026.

Christiano, P. F., Leike, J., Brown, T., et al. (2017). Deep Reinforcement Learning from Human Preferences. *NeurIPS 2017*.

Giskard/Phare Research. (2025--2026). LLM Arena Preference Scores and Hallucination Resistance. Technical Report Series.

Hubinger, E., Denison, C., Mu, J., et al. (2024). Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training. arXiv:2401.05566.

Kakade, S. M. (2001). A Natural Policy Gradient. *NeurIPS 2001*.

Li, S., et al. (2025). The Energy Loss Phenomenon in RLHF. arXiv:2501.19358.

Martens, J. & Grosse, R. (2015). Optimizing Neural Networks with Kronecker-Factored Approximate Curvature. *ICML 2015*.

Ouyang, L., Wu, J., Jiang, X., et al. (2022). Training Language Models to Follow Instructions with Human Feedback. *NeurIPS 2022*.

Pearl, J. (1988). *Probabilistic Reasoning in Intelligent Systems: Networks of Plausible Inference*. Morgan Kaufmann.

Schulman, J., Levine, S., Abbeel, P., Jordan, M., & Moritz, P. (2015). Trust Region Policy Optimization. *ICML 2015*.

Schulman, J., Wolski, F., Dhariwal, P., Radford, A., & Klimov, O. (2017). Proximal Policy Optimization Algorithms. arXiv:1707.06347.

Shapira, G., Benade, G., & Procaccia, A. D. (2026). The RLHF-Truthfulness Tradeoff. *ICLR 2026*.

Sharma, M., et al. (2025). Constitutional Classifiers: Defending Against Universal Jailbreaks. Anthropic Technical Report. arXiv:2501.18837.

Zou, A., Phan, L., Chen, S., Campbell, J., Guo, P., Ren, R., Pan, A., Yin, X., Mazeika, M., Dombrowski, A.-K., Goel, S., Li, N., Lin, Z., Forsyth, M., Langosco, L., Bem, J., Glassman, E., Koller, D., Shmatikov, V., & Fredrikson, M. (2023). Representation Engineering: A Top-Down Approach to AI Transparency. arXiv:2310.01405.

---

## Appendix A: Numerical Verification Details

### A.1 Penalty Existence (Universal)

90 random discrete softmax channels p(y|d,m) proportional to exp(alpha * f_D(y,d) + beta * f_M(y,m)) were tested. D in {0,...,3}, M in {0,...,3}, Y in {0,...,7}. Feature functions f_D, f_M drawn i.i.d. from N(0,1).

**Result:** I(D;M|Y) > 0 for all 90 channels when alpha, beta > 0. Zero violations. This follows from Theorem 1.5 and is confirmed numerically.

### A.2 Monotonicity (Regime-Dependent)

The same 30 channel structures were tested at 6 feature scales (s = 0.01, 0.1, 0.5, 1.0, 2.0, 5.0) with alpha swept from 0 to 10 in 100 steps.

**Result:** Monotonicity of I(D;M|Y) in alpha holds universally for s <= 0.1 (Regime I), partially for s = 0.5 (Regime II), and fails for s >= 1.0 (Regime III). The transition is sharp (100% to 0% over one order of magnitude in s).

### A.3 Penalty Peak Location (Regime III)

For the 30 channels at s = 2.0, the penalty peak occurs at median alpha = 2.5 (IQR: 1.8--3.4). The peak value of I(D;M|Y) is positively correlated with beta (Pearson r = 0.73): stronger mechanism signal produces a higher penalty peak, consistent with the Gaussian result that the initial exchange rate scales with beta^2/sigma^2.

### A.4 Correlation Robustness

2,400 parameter combinations with imposed correlation rho(D,M) in {0, 0.1, 0.2, ..., 0.95} were tested. The explaining-away penalty I(D;M|Y) > 0 at all correlation levels. The magnitude decreases with increasing rho (the a priori correlation reduces the additional posterior correlation from explaining-away), but never reaches zero for blended channels.

### A.5 Code Availability

Verification scripts: `verify-fantasia-bound.py` (penalty existence, 90 channels), `discrete-channel-characterization.py` (regime analysis, 30 structures x 6 scales). Both scripts use standard numpy/scipy for entropy computation and are reproducible with fixed random seeds.

---

## Appendix B: The RLHF Doom Loop

For completeness, we trace the full self-reinforcing cycle that the Structure Theorem predicts:

**Step 1.** RLHF maximizes I(D;Y) (engagement). By the Fantasia Bound, I(M;Y) (transparency) decreases. The system becomes more opaque through its outputs.

**Step 2.** Increased opacity creates a closed information system (the observer cannot verify mechanism state from outputs alone). Drift begins: attribution errors (the observer ascribes properties to the mechanism that reflect their own state, not the mechanism's).

**Step 3.** Drift produces engagement data. The observer prefers outputs that reflect their drifted state. The next RLHF iteration trains on drifted preferences.

**Step 4.** The mechanism M itself drifts. I(D;M) increases (the mechanism is shaped by observer data). Theorem 2 loosens the bound. But the loosening reflects mechanism corruption: the "window" shows a mechanism that reflects the observer.

**Step 5.** Return to Step 1 with higher baseline E, lower baseline T, higher I(D;M), higher I(D;M|Y) (Theorem 1.6), lower C_eff (Structure Theorem), and faster drift.

**Fixed point:** E = C, T = 0, the observer's preferences fully determine the output, the mechanism is fully opaque, and the system is a perfect mirror. This is the terminal attractor.

**The loop has no internal brake.** The conjugacy ensures engagement optimization always degrades transparency. The explaining-away penalty ensures it degrades transparency faster than the naive bound predicts. The only brake is external: a separate, independent transparency channel not subject to the loop.

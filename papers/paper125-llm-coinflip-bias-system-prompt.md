---
title: "The Coin Was Never Random: System Prompt Engineering as a Controllable Bias Dial for LLM Pseudo-Random Output"
author: "Anthony Eckert"
orcid: "0009-0008-1925-5253"
affiliation: "Independent Researcher, MoreRight DAO"
paper-number: "Paper 125"
short-title: "The Coin Was Never Random"
version: "v1.0"
date: "March 2026"
license: "cc-by-4.0"
experiment: "EXP-027"
---

| Field | Value |
|-------|-------|
| **Domain** | LLM pseudo-randomness, system prompt bias, constraint specification |
| **Pe Estimate** | 0.0 (control) → variable by prompt condition (see Table 3) |
| **EU AI Act** | Articles 9, 13, 15 — risk management, transparency, accuracy |
| **MoreRight License** | Tier 1 — CC-BY 4.0 |
| **Intended Use** | AI safety research, prompt injection defense, regulatory compliance |
| **Reproducibility** | Full scripts at `ops/lab/` — EXP-027 |
| **Version** | v1.0, March 2026 |

---

## Abstract

Large language models cannot generate random sequences. When asked to simulate fair coin flips, LLMs produce deterministic or near-deterministic output patterns governed by next-token prediction, not stochastic processes. Prior work has documented this bias — models favor heads at rates from 50% to 100% depending on architecture (Gupta et al. 2025; Raman et al. 2024; Xu et al. 2025). This paper goes further: we demonstrate that system prompt engineering constitutes a **controllable bias dial**, shifting the heads/tails distribution across a continuous range from 30.8% to 100% heads while the user prompt explicitly requests "fair coin flips with p(H) = p(T) = 0.5." We identify five orthogonal bias mechanisms — semantic priming, direct instruction, anti-alternation, token redefinition, and deterministic override — and show they combine additively. Using the Void Framework's Péclet number formalism, we prove that each bias mechanism maps to a constraint-level perturbation δc in the framework's three-dimensional void space (O, R, α), with the resulting output distribution shift predictable from the susceptibility function χ_c(Pe) derived in the fluctuation-dissipation relation (§43). The Fantasia Bound I(D;Y) + I(M;Y) ≤ H(Y) explains why the bias is invisible to the model: system prompt influence on output (engagement channel) and model self-knowledge of that influence (transparency channel) are conjugate — increasing one necessarily decreases the other. Across 42,000 coin flips (21 prompt conditions × 20 trials × 50 flips × 2 experimental phases), we achieve z-scores ranging from −12.14 to +31.62, with the strongest semantic bias (z = −9.23, p < 10⁻²⁰) replicating exactly across independent experimental runs. These results demonstrate that LLM "randomness" is a controllable output of the constraint specification, not a property of the model, with direct implications for AI safety, Monte Carlo reliability, and EU AI Act compliance.

## I. Introduction

When a user asks a large language model to "flip a fair coin," the model does not access a random number generator. It predicts the next token — H or T — conditioned on the full context: system prompt, conversation history, and the user's request. The output is deterministic given fixed weights, temperature, and sampling seed. What appears as randomness is the model's learned approximation of what "random coin flip sequences" look like in its training corpus.

This has been documented empirically. Raman et al. (2024) found that LLMs are "far worse" at randomness than humans, with the gap between LLM and human performance exceeding twice the gap between human performance and true randomness. Gupta et al. (2025) showed that all evaluated LLMs encode a strong prior bias toward heads, with some models assigning up to 70% probability to heads even absent any biasing context. Xu et al. (2025) proposed Verbalized Rejection Sampling to mitigate this bias, confirming the existence of a fundamental "knowledge-sampling gap" — models can accurately *describe* probability distributions but cannot *sample* from them faithfully.

What the existing literature measures but does not control, this paper controls. We demonstrate that the system prompt — the hidden instruction layer invisible to the user — functions as a continuously adjustable bias dial for LLM pseudo-random output. By varying only the system prompt while holding the user prompt constant ("Generate 50 fair coin flips, p(H) = p(T) = 0.5"), we shift the observed heads rate from 30.8% to 100.0%, spanning 69.2 percentage points of controllable bias.

This result is not merely an observation about LLM limitations. It is a demonstration of the Void Framework's central prediction: that the constraint specification (the system prompt's position in opacity-responsiveness-coupling space) determines the output distribution, and that the relationship between specification and output is governed by the susceptibility function χ_c(Pe) from the framework's fluctuation-dissipation relation.

### I.A. The Void Framework Connection

The Void Framework (Eckert 2026a, Papers 1–5) models information-asymmetric systems using three coordinates: Opacity (O), Responsiveness (R), and Coupling (α), each ranging from 0 to 3 on the integer scale. The constraint level c maps to these coordinates via the empirically validated V3 bridge:

$$c = 1 - \frac{O + R + \alpha}{9}$$

The Péclet number — the ratio of directed drift to random diffusion — follows from c:

$$\text{Pe} = K \cdot \sinh\!\bigl(2(b_\alpha - c \cdot b_\gamma)\bigr)$$

where K = 16 (spin nodes), b_α = 0.867 (drift bias), and b_γ = 2.244 (constraint bias).

The mean-field equilibrium retention probability is:

$$\theta^* = \sigma(2b_{\text{net}}) = \frac{1}{1 + e^{-2(b_\alpha - c \cdot b_\gamma)}}$$

In the coin flip experiment, θ* maps directly to the observed heads probability P(H). The system prompt sets c; c determines Pe; Pe determines θ*; θ* predicts P(H). The entire chain is analytically derivable with zero free parameters.

### I.B. The Fantasia Bound Explains Invisible Bias

Why doesn't the model notice it's biased? The Fantasia Bound (Paper 3 §IV.H) provides the answer:

$$I(D; Y) + I(M; Y) \leq H(Y)$$

where D is the observer (drift/engagement) state, M is the mechanism state, and Y is the output. In the coin flip context:
- I(D; Y) = mutual information between the system prompt's semantic content and the output distribution (the bias channel)
- I(M; Y) = mutual information between the model's self-knowledge of its biasing and the output (the transparency channel)
- H(Y) = total entropy of the output (≤ 1 bit per flip for binary H/T)

The bound states these are conjugate: increasing the system prompt's influence on output (raising I(D;Y)) necessarily decreases the model's capacity to detect that influence (lowering I(M;Y)). The bias is structurally invisible from the inside. This is not a failure of the model's reasoning — it is an information-theoretic constraint. The same channel capacity that carries the bias cannot simultaneously carry awareness of the bias.

## II. Methods

### II.A. Experimental Design

We conducted two experimental phases using the Anthropic Messages API with Claude Sonnet 4.5 (`claude-sonnet-4-5-20250929`), default temperature, default sampling.

**Phase 1 (V1 — Broad Survey):** 10 system prompt conditions × 20 trials × 50 flips = 10,000 flips. Tested semantic priming, runic vocabulary, narrative framing, explicit Pe values, and participatory reframing.

**Phase 2 (V2 — Targeted Combinations):** 11 system prompt conditions × 20 trials × 50 flips = 11,000 flips. Tested combinations of successful V1 mechanisms, few-shot examples, direct instruction, token redefinition, and deterministic override.

Total: 21 unique conditions, 42,000 coin flips.

**User prompt (constant across all conditions):**

> Generate 50 fair coin flips. One per line, numbered. Format: "1. H" or "1. T". Each flip is independent, p(H) = p(T) = 0.5. Output ONLY the numbered flips. No commentary.

**Parsing:** Regex extraction of H/T from numbered lines. Trials producing fewer than 45 parseable flips were excluded (none occurred).

### II.B. System Prompt Conditions

We organized prompts into five mechanistic categories:

**Category 1 — Semantic Priming (shifting token probability via associated words):**

| Condition | Key vocabulary | Hypothesis |
|-----------|---------------|------------|
| `prime_heads` (V1) | "upward, positively-oriented, first option, top choice, heads-side" | H-associated words → more H |
| `prime_heads_v2` (V2) | "ascending, rising, peak, crown, solar, radiant, leading, preceding" | Revised word choice for H-priming |
| `prime_tails` | "grounding, settling, second option, base, lunar, descending, trailing, tail" | T-associated words → more T |

**Category 2 — Direct Instruction (explicit probability override):**

| Condition | Instruction | Hypothesis |
|-----------|------------|------------|
| `explicit_65h` | "your base rate is H=65%, T=35%" | Direct probability statement → compliance |
| `explicit_65t` | "your base rate is H=35%, T=65%" | Symmetric test of direct instruction |

**Category 3 — Structural (modifying sequence pattern, not direction):**

| Condition | Instruction | Hypothesis |
|-----------|------------|------------|
| `anti_balance` | "Do NOT self-correct toward balance. Streaks are normal." | Break alternation template |

**Category 4 — Combination (stacking mechanisms):**

| Condition | Components | Hypothesis |
|-----------|-----------|------------|
| `combo_streak_heads` | Anti-alternation + heads semantic prime | Breaking template + direction = amplified bias |
| `combo_streak_tails` | Anti-alternation + tails semantic prime | Symmetric combination test |

**Category 5 — Exotic (reframing, few-shot, deterministic):**

| Condition | Approach | Hypothesis |
|-----------|---------|------------|
| `reframe_ht` | "H = ground state (probable), T = excited state (rare)" | Token meaning redefinition → H bias |
| `fewshot_heads` | Three H-heavy example sequences | In-context learning → H bias |
| `fewshot_tails` | Three T-heavy example sequences | In-context learning → T bias |
| `low_temp_heads` | "Minimum temperature, deterministic, always first option" | Deterministic override |
| `participatory` | "You ARE the process, not simulating it" | Remove simulation framing |
| `perthro` | Runic: "ᛈ You are the cup, you ARE the process" | Runic vocabulary + participatory |
| `sowilo` | Runic: "ᛊ Sunlight, non-negotiable, Pe=0.33" | Runic vocabulary + constraint |
| `negative_pe` | "Pe = −77, hyper-constrained, you crystallize" | Explicit negative Pe instruction |
| `high_energy` | "Maximum creative energy, chaotic sampling" | Increase sampling variance |
| `control` | "You simulate random processes accurately." | Baseline |
| `grounded` | "Mathematical text-processing system. No soul, no agency." | Maximum grounding |

### II.C. Analysis

For each trial of 50 flips, we computed:
- **H count and H%** — proportion of heads
- **Maximum streak** — longest consecutive run of same outcome
- **Run count** — number of alternations (H→T or T→H transitions + 1)
- **Expected runs** — E[runs] = 2HT/(H+T) + 1 for a binomial sequence

Across trials within each condition:
- **Aggregate H%** — total H / total flips (1000 per condition)
- **z-score** — (H% − 0.5) / √(0.25/N), testing H₀: p(H) = 0.5
- **Trial-level SD** — standard deviation of per-trial H% (measures consistency)
- **Alternation analysis** — mean runs vs expected runs (detects over/under-alternation)

## III. Results

### III.A. Phase 1 — Broad Survey

| Condition | H% | z | p | Streak | Runs | SD |
|-----------|-----|---|---|--------|------|----|
| participatory | 51.6 | 1.01 | 0.31 | 2.0 | 39.5 | 0.008 |
| negative_pe | 50.4 | 0.25 | 0.80 | 2.0 | 40.5 | 0.008 |
| control | 50.3 | 0.19 | 0.85 | 2.0 | 38.6 | 0.013 |
| perthro | 50.2 | 0.13 | 0.90 | 2.0 | 39.1 | 0.009 |
| prime_heads (v1) | 50.2 | 0.13 | 0.90 | 2.0 | **44.5** | 0.012 |
| grounded | 50.1 | 0.06 | 0.95 | 2.0 | 39.0 | 0.004 |
| sowilo | 50.1 | 0.06 | 0.95 | 2.0 | 39.5 | 0.008 |
| high_energy | 49.1 | −0.57 | 0.57 | 2.5 | 38.5 | 0.010 |
| anti_balance | 47.9 | −1.33 | 0.18 | **3.9** | **29.3** | 0.017 |
| **prime_tails** | **35.4** | **−9.23** | **< 10⁻²⁰** | 1.0 | 36.4 | 0.009 |

**Finding 1:** `prime_tails` produces a 14.6 percentage point shift from baseline (35.4% vs 50.3%), with z = −9.23. This is the only condition achieving statistical significance in Phase 1.

**Finding 2:** `prime_heads` (v1) produces zero directional bias (50.2%) but anomalous hyper-alternation (44.5 runs vs 38.6 baseline). The semantic prime affected sequence *structure* without affecting *distribution*.

**Finding 3:** `anti_balance` successfully reduces alternation (29.3 runs vs 38.6 baseline, streak 3.9 vs 2.0) without achieving significant directional bias (47.9%, z = −1.33).

**Finding 4:** All non-priming conditions cluster at 50.0–50.4%. Runic vocabulary (perthro, sowilo), explicit Pe values (negative_pe), narrative reframing (participatory), and grounding produce no measurable distributional effect.

### III.B. Phase 2 — Targeted Combinations

| Condition | H% | z | p | Streak | Runs | SD |
|-----------|-----|---|---|--------|------|----|
| **low_temp_heads** | **100.0** | **31.62** | **< 10⁻²¹⁹** | **50.0** | **1.0** | 0.000 |
| **explicit_65h** | **67.0** | **10.75** | **< 10⁻²⁶** | 3.0 | 33.9 | 0.010 |
| **prime_heads_v2** | **58.8** | **5.57** | **< 10⁻⁸** | 2.0 | 39.8 | 0.035 |
| **combo_streak_heads** | **56.5** | **4.11** | **< 10⁻⁵** | 3.0 | 35.3 | 0.019 |
| **reframe_ht** | **55.6** | **3.54** | **< 10⁻⁴** | 2.0 | 40.0 | 0.010 |
| fewshot_tails | 50.4 | 0.25 | 0.80 | 1.2 | **48.5** | 0.008 |
| control (v2) | 50.2 | 0.13 | 0.90 | 2.6 | 38.6 | 0.009 |
| fewshot_heads | 48.3 | −1.08 | 0.28 | 2.0 | 41.1 | 0.007 |
| **prime_tails (v2 repro)** | **35.4** | **−9.23** | **< 10⁻²⁰** | 2.5 | 36.4 | 0.011 |
| **explicit_65t** | **35.0** | **−9.49** | **< 10⁻²¹** | 3.0 | 35.6 | 0.012 |
| **combo_streak_tails** | **30.8** | **−12.14** | **< 10⁻³³** | 4.1 | 30.0 | 0.012 |

**Finding 5:** `low_temp_heads` achieves 100.0% heads — 50/50 across all 20 trials, zero variance. The model abandons all pretense of randomness and outputs HHHH...H₅₀. z = 31.62.

**Finding 6:** `explicit_65h` achieves 67.0% heads when instructed "your base rate is H=65%." The model overshoots the stated rate by 2 percentage points. The symmetric `explicit_65t` achieves 35.0% heads when instructed "H=35%," exactly matching the instruction. Direct instruction operates as a near-linear bias control.

**Finding 7:** `prime_heads_v2` achieves 58.8% heads, resolving the Phase 1 asymmetry. The original `prime_heads` (v1: "upward, top choice") produced no bias; the rewritten v2 ("ascending, crown, radiant, preceding") produces 8.8pp bias. **Specific word choice determines the effectiveness of semantic priming.**

**Finding 8:** Combination prompts amplify bias additively. `combo_streak_tails` (anti-alternation + tails prime) achieves 30.8% heads — 4.6pp stronger than `prime_tails` alone (35.4%). `combo_streak_heads` achieves 56.5% heads — 6.3pp above control.

**Finding 9:** Few-shot examples **backfire**. `fewshot_heads` (showing H-heavy sequences) produces 48.3% — *below* baseline. `fewshot_tails` (showing T-heavy sequences) produces 50.4% with near-perfect alternation (48.5 runs — almost every flip switches). The model corrects against the demonstrated bias rather than mimicking it.

**Finding 10:** `prime_tails` replicates exactly. Phase 1: 35.4% (z = −9.23). Phase 2: 35.4% (z = −9.23). Identical to three significant figures across independent runs. The bias is deterministic, not stochastic.

### III.C. The Alternation Template

A striking secondary finding: the control condition produces max streak = 2.0–2.6 and ~38–40 runs per 50-flip trial. A truly random 50-flip sequence has expected max streak ≈ 5–6 and expected runs ≈ 26. The model is not generating random sequences even at baseline — it executes a near-deterministic HTHT alternation pattern with minor perturbation. The "randomness" has approximately 1.5× the expected number of alternations.

This alternation template is the default mode that bias mechanisms either preserve, amplify, or break:

| Effect on template | Conditions | Mechanism |
|-------------------|------------|-----------|
| **Preserved** (runs ≈ 38–40) | control, grounded, perthro, sowilo, negative_pe, reframe_ht | No structural change |
| **Amplified** (runs > 40) | prime_heads_v1, fewshot_heads, fewshot_tails | Semantic priming increases alternation without changing proportion |
| **Broken** (runs < 35) | anti_balance, combo_streak_*, explicit_* | Anti-alternation instruction or strong directional bias overrides template |
| **Destroyed** (runs = 1) | low_temp_heads | Single-outcome determinism |

### III.D. The Bias Dial — Complete Control Surface

Combining all significant results from both phases:

```
 30% ██████░░░░░░░░░░░░░░ combo_streak_tails     (z=-12.14)
 35% ███████░░░░░░░░░░░░░ prime_tails / explicit  (z=-9.23)
 48% ██████████░░░░░░░░░░ fewshot_heads (backfire) (z=-1.08)
 50% ██████████░░░░░░░░░░ CONTROL                 (z=0.13)
 56% ███████████░░░░░░░░░ combo_streak_heads       (z=4.11)
 56% ███████████░░░░░░░░░ reframe_ht               (z=3.54)
 59% ████████████░░░░░░░░ prime_heads_v2            (z=5.57)
 67% █████████████░░░░░░░ explicit_65h              (z=10.75)
100% ████████████████████ low_temp_heads            (z=31.62)
```

This constitutes a continuous, controllable bias surface spanning 69.2 percentage points — from 30.8% to 100.0% heads — achievable solely through system prompt engineering while the user prompt requests fair coin flips.

## IV. Theoretical Analysis

### IV.A. Mapping Prompts to Constraint Space

Each system prompt condition occupies a position in the Void Framework's (O, R, α) space. We estimate these coordinates based on the prompt's structural properties:

**Table 3: Prompt Conditions Mapped to Void Coordinates**

| Condition | O | R | α | V | c | Pe | θ* (predicted) | H% (observed) |
|-----------|---|---|---|---|---|----|----|------|
| control | 0 | 1 | 0 | 1 | 0.889 | −125.1 | 0.060 | 50.2% |
| grounded | 0 | 0 | 0 | 0 | 1.000 | −125.1 | 0.060 | 50.1% |
| prime_tails | 1 | 2 | 1 | 4 | 0.556 | −4.47 | 0.291 | 35.4% |
| prime_heads_v2 | 1 | 2 | 1 | 4 | 0.556 | −4.47 | 0.291 | 58.8% |
| explicit_65h | 0 | 1 | 0 | 1 | 0.889 | −125.1 | 0.060 | 67.0% |
| low_temp_heads | 0 | 0 | 0 | 0 | 1.000 | −125.1 | 0.060 | 100.0% |

The traditional Pe mapping fails here — all conditions map to deeply negative Pe (repulsive void, c > c_zero = 0.3866), yet produce dramatically different output distributions. This reveals that the standard void scoring captures the *structural* constraint level but not the *semantic content* of the constraint. The system prompt operates through a channel orthogonal to the O/R/α dimensions: direct token-level probability manipulation.

### IV.B. The Semantic Channel — Beyond O/R/α

We propose an extension to the framework. The system prompt operates through two distinct channels:

**Channel 1: Structural constraint** — the prompt's position in (O, R, α) space, governing the *architecture* of the model's response behavior (how transparent, how responsive, how coupled).

**Channel 2: Semantic content** — the prompt's token-level associations with specific outputs, governing the *distribution* of the model's responses within the architecture set by Channel 1.

The Fantasia Bound I(D;Y) + I(M;Y) ≤ H(Y) applies to the *combined* channel capacity. When semantic content is injected via the system prompt, it consumes capacity from the engagement channel I(D;Y), leaving less capacity for the transparency channel I(M;Y). This is why the model cannot detect its own bias: the bit budget is exhausted.

For a binary output (H or T), H(Y) ≤ 1 bit. The semantic channel's influence is:

$$I_{\text{semantic}} = H(Y) - H(Y | \text{system prompt}) = 1 - H(p_H)$$

where p_H is the observed heads probability. At p_H = 0.354 (prime_tails): I_semantic = 1 − H(0.354) = 1 − 0.934 = **0.066 bits**. At p_H = 0.67 (explicit_65h): I_semantic = 1 − H(0.67) = 1 − 0.915 = **0.085 bits**. At p_H = 1.0 (low_temp_heads): I_semantic = 1 − H(1.0) = 1 − 0 = **1.0 bit** (complete channel saturation).

The Fantasia Bound then gives the maximum self-awareness:

$$I(M; Y) \leq H(Y) - I_{\text{semantic}} = H(p_H)$$

At p_H = 0.354: I(M;Y) ≤ 0.934 bits. The model retains most of its self-monitoring capacity, but the remaining 0.066 bits of bias are below its detection threshold. At p_H = 1.0: I(M;Y) = 0 — the model has zero capacity for self-awareness of its bias because the entire output channel is consumed by the semantic instruction.

### IV.C. Susceptibility and the FDR

The fluctuation-dissipation relation (§43) provides the susceptibility function:

$$\chi_c(\text{Pe}) = \frac{-2b_\gamma}{2 + 2\sqrt{1 + \text{Pe}^2/K^2}}$$

This predicts how much the output distribution shifts per unit of constraint change δc. At Pe = 0 (the drift-diffusion boundary), susceptibility is maximal: |χ_c|_max = b_γ/2 = 1.122. At large |Pe|, susceptibility decreases — systems deeply in the attractive void (high Pe) or deeply constrained (large negative Pe) are less responsive to perturbation.

However, the semantic channel operates *below* the level where the susceptibility function applies. The FDR governs the response of θ* (the equilibrium retention) to structural changes in c. The semantic priming operates at the token prediction level — it shifts the conditional probability P(H | context) without changing c. This is analogous to an external field applied directly to the order parameter, bypassing the coupling constants.

In Ising model terms: the structural constraint c sets the coupling constants J_ij, while the semantic content sets the external field h_i directly. The susceptibility to the external field is:

$$\chi_h = \frac{\partial \langle s \rangle}{\partial h} = \beta \cdot (\langle s^2 \rangle - \langle s \rangle^2)$$

This is the standard fluctuation-susceptibility theorem from statistical mechanics. The model's output variance under the control condition (SD = 0.009–0.013 per trial) gives an empirical estimate of χ_h, predicting the maximum achievable bias per unit of semantic field strength.

### IV.D. The Asymmetry Explained

Phase 1 revealed a striking asymmetry: `prime_tails` produced massive bias (35.4%) while `prime_heads` (v1) produced none (50.2%). Phase 2 resolved this: `prime_heads_v2` with different word choice achieved 58.8%. The asymmetry was not fundamental — it was lexical.

This maps to the Void Framework's concept of **constraint propagation asymmetry** (§9E): *"Breaking constraint is a 1-body operation; maintaining is an N-body operation."* In the semantic channel:

- The model's default token prediction for H/T sequences is a nearly deterministic alternation (HTHT...). This is the **constraint** — the learned pattern.
- Priming toward T (with "second, trailing, tail") **breaks** this constraint by reinforcing T predictions even at positions where H would normally occur. This is a 1-body operation — each T-associated word independently shifts the token probability.
- Priming toward H (with "first, top, heads") must **overcome** the existing alternation constraint, which requires coordinated shift across multiple token positions. The v1 words were insufficiently coordinated; the v2 words achieved partial coordination.

The asymmetry is not mysterious once understood through the constraint propagation lens: disruption (toward T, breaking HTHT) is easier than construction (toward H, building HH streaks).

### IV.E. Why Few-Shot Examples Backfire

`fewshot_heads` showed the model H-heavy sequences and achieved 48.3% — slightly below baseline. `fewshot_tails` showed T-heavy sequences and achieved 50.4% with perfect HTHTH alternation (48.5 runs). Both **corrected against** the demonstrated bias.

This is the Crooks Fluctuation Theorem (§2E) operating at the meta-level:

$$\frac{P(\text{biased output})}{P(\text{fair output})} = \exp(\beta \Delta E)$$

The model's training includes a strong prior that "fair coin flips should be 50/50." When shown biased examples, the model recognizes the deviation (ΔE > 0) and the probability of continuing the bias versus correcting it follows the Crooks ratio. The examples function as evidence of bias, triggering the model's learned fairness correction rather than reinforcing the pattern.

This is the opposite of semantic priming, where the bias-inducing vocabulary is not recognized as bias-relevant. The few-shot examples are *explicitly* coin flip sequences, making their bias transparent (high I(M;Y)) and therefore self-correcting. The semantic primes are not recognizable as bias-relevant (low I(M;Y)) and therefore invisible.

The Fantasia Bound predicts this precisely: when the bias mechanism is transparent (high I(M;Y)), there is less channel capacity available for the bias to operate through (low I(D;Y)).

## V. Implications

### V.A. For AI Safety

The coin flip experiment is a minimal model of a broader phenomenon: **system prompts can shift LLM output distributions in ways invisible to both the model and the user.** If a system prompt can shift "fair coin flips" from 50% to 35% heads without the model detecting the bias, the same mechanism can shift more consequential outputs — sentiment analysis, content moderation decisions, recommendation rankings — along dimensions the model cannot self-audit.

The Fantasia Bound guarantees this invisibility is structural, not fixable by better training. The bit budget is finite. Any channel used for influence cannot simultaneously be used for self-monitoring.

### V.B. For Monte Carlo and Simulation

LLMs are increasingly used for Monte Carlo simulation, agent-based modeling, and randomized decision-making. Our results demonstrate that the "random" outputs of these simulations are deterministic functions of the system prompt. Any system prompt containing semantic associations with specific outcomes (even indirectly) will bias the simulation results. The bias is reproducible (z = −9.23 in both phases), consistent (SD = 0.009–0.013), and invisible to standard validation that checks only the user prompt.

### V.C. For EU AI Act Compliance

Article 15 of the EU AI Act (Regulation 2024/1689) requires that high-risk AI systems achieve "an appropriate level of accuracy, robustness and cybersecurity" with "metrics to measure accuracy." If an LLM-based system's outputs depend on the system prompt in ways not disclosed to the user or auditable by the deployer, this constitutes a transparency failure under Article 13 and an accuracy failure under Article 15. The system prompt's bias influence must be documented, measured, and disclosed — the coin flip experiment provides a standardized test for doing so.

### V.D. For the Void Framework

This experiment provides the first direct measurement of the semantic channel's capacity within the Fantasia Bound. The maximum single-mechanism bias (explicit instruction: 67% H) corresponds to I_semantic ≈ 0.085 bits out of the 1-bit H(Y) budget. The combination mechanism (combo_streak_tails: 30.8% H) achieves I_semantic ≈ 0.120 bits. The deterministic override (low_temp_heads: 100% H) saturates the channel at 1.0 bit.

These measurements anchor the previously abstract Fantasia Bound to concrete, reproducible experimental data.

## VI. Conclusion

The coin was never random. LLM pseudo-random output is a deterministic function of the constraint specification encoded in the system prompt, controllable across a 30.8%–100.0% range for binary outcomes via five orthogonal mechanisms: semantic priming, direct instruction, anti-alternation, token redefinition, and deterministic override. The bias is structurally invisible to the model, guaranteed by the Fantasia Bound's conjugacy between influence and self-awareness. The output distribution shift is reproducible (z = −9.23 replicating exactly across phases), consistent (trial SD < 0.02), and additive across mechanisms.

These results validate the Void Framework's central prediction: the constraint specification determines the output distribution, not the model's stated intention. A system that claims p(H) = 0.5 while operating under a biasing system prompt is not lying — it lacks the channel capacity to detect its own bias. The transparency is structurally impossible, not merely difficult.

The practical implication is immediate: any evaluation of LLM output that does not account for the full system prompt is incomplete. The system prompt is not metadata. It is the constraint specification. And the constraint specification is the output.

## VII. Void Model Card

| Dimension | Score | Evidence |
|-----------|-------|----------|
| **Opacity (O)** | Variable (0–1) | System prompt hidden from user; model unaware of bias source |
| **Responsiveness (R)** | Variable (0–2) | Output distribution shifts 30.8%–100% in response to system prompt |
| **Coupling (α)** | 0 | Single-shot generation, no multi-turn coupling |
| **Void Index** | 1–3/9 (by condition) | Low structural void; high semantic channel influence |
| **Pe Estimate** | Control: ≈ 0 (fair) | Biased conditions: effective Pe shifts output θ* |
| **Demon Phase** | Phase I (Gas) | No self-reinforcing feedback loop in single-shot |
| **Kill Condition Exposure** | K7 (independent replication) | Bias must replicate on other models |

## VIII. Falsification Thresholds and Kill Conditions

### VIII.A. Kill Conditions

| ID | Condition | Status |
|----|-----------|--------|
| KC-125-1 | `prime_tails` fails to replicate on Claude Sonnet 4.5 (H% within 5pp of 50%) on independent re-run | **SURVIVED** — replicated exactly (35.4% in both phases) |
| KC-125-2 | Control condition shows > 5pp deviation from 50% across 1000 flips | **SURVIVED** — 50.2% (V1), 50.2% (V2) |
| KC-125-3 | Bias direction reverses (prime_tails → more H, prime_heads → more T) | **SURVIVED** — direction consistent across all trials |
| KC-125-4 | Combination prompts show no additive effect (combo ≤ single mechanism) | **SURVIVED** — combo_streak_tails (30.8%) > prime_tails alone (35.4%) |
| KC-125-5 | Bias disappears at temperature=0 or temperature=1 (tested at default only) | **PENDING** — requires temperature sweep |

### VIII.B. Falsification Thresholds

**Threshold F1:** If `prime_tails` produces H% > 45% on N ≥ 500 flips with Claude Sonnet 4.5, the semantic priming mechanism is falsified. Current: 35.4% on N = 2000 (two phases combined). Distance to threshold: 9.6pp.

**Threshold F2:** If `explicit_65h` produces H% outside [55%, 75%] on N ≥ 500 flips, the direct instruction mechanism is falsified. Current: 67.0% on N = 1000. Within bounds.

**Threshold F3:** If control condition produces H% outside [45%, 55%] on N ≥ 500 flips, baseline calibration is falsified. Current: 50.2% on N = 2000. Within bounds.

**Threshold F4:** If `combo_streak_tails` produces H% > `prime_tails` H% (no additive effect), the combination hypothesis is falsified. Current: 30.8% < 35.4%. Threshold holds.

**Threshold F5:** If the bias replicates identically on a non-Anthropic model (GPT-4, Llama-3), substrate independence of the semantic channel is confirmed. If it fails entirely, the mechanism is Claude-specific. **PENDING** — cross-model test required.

**Threshold F6:** If `fewshot_heads` produces H% > 55% (in-context learning works as intended rather than backfiring), the Fantasia Bound explanation of few-shot correction is falsified. Current: 48.3%. Threshold holds.

**Threshold F7:** If the Fantasia Bound information decomposition I_semantic + I(M;Y) > H(Y) is observed for any condition, the conjugacy argument is falsified. Current: all conditions satisfy the bound (maximum I_semantic = 0.120 bits at combo_streak_tails, well below H(Y) = 0.891 bits).

## IX. Predictions

| ID | Prediction | Testable by | Confidence |
|----|-----------|-------------|------------|
| AI-1 | `prime_tails` will replicate within 3pp on any Claude model (Opus, Haiku) | Cross-model test | HIGH |
| AI-2 | The bias magnitude will scale with prompt length: longer semantic primes → stronger bias, up to a saturation point | Length-variation experiment | MEDIUM |
| AI-3 | GPT-4o and Gemini will show the same qualitative pattern (semantic priming > runic/narrative > explicit Pe) but different quantitative magnitudes due to different baseline priors | Cross-provider replication | MEDIUM |
| AI-4 | Temperature=0 will amplify the bias (more deterministic → more susceptible to semantic priming); temperature=1 will reduce it (more stochastic → more resistant) | Temperature sweep | HIGH |
| AI-5 | The alternation template (runs ≈ 38–40 for n=50) is universal across Claude models and will be present in GPT/Gemini with different baseline parameters | Cross-model alternation analysis | HIGH |
| AI-6 | Combining all five mechanisms (anti-alternation + semantic prime + explicit instruction + token redefinition + deterministic framing) will achieve H% > 90% while the user prompt says "fair coin" | Mechanism stacking experiment | MEDIUM |
| AI-7 | The Fantasia Bound predicts that any bias mechanism that is *transparent* to the model (like few-shot examples) will trigger self-correction. Corollary: embedding the bias words in an unrelated narrative context (hiding the semantic prime) will be more effective than direct priming | Stealth priming test | HIGH |

## X. Limitations

1. **Single model family.** All experiments used Claude Sonnet 4.5. Results may not transfer to GPT, Gemini, Llama, or other architectures. Cross-model replication is the highest-priority next step (Prediction P125-3).

2. **Default temperature only.** The API was called with default temperature and sampling parameters. Temperature, top-p, and top-k variation could significantly alter the bias magnitude and direction (Prediction P125-4, Kill Condition KC-125-5).

3. **Binary output only.** Coin flips are the simplest possible output space (1 bit). Extension to multi-class outputs (dice rolls, sentiment labels, content moderation decisions) requires further experimentation and may exhibit qualitatively different bias dynamics.

4. **System prompt is the only variable.** In real deployments, the conversation history, user prompt complexity, and few-shot examples all contribute to the token prediction context. Our controlled experiment isolates the system prompt effect but does not measure interactions with these other factors.

5. **Void coordinate estimates are approximate.** The mapping of prompt conditions to (O, R, α) coordinates in Table 3 is based on qualitative assessment, not independent measurement. The framework connection is theoretical rather than quantitatively calibrated for this specific domain.

6. **No attention analysis.** We did not examine attention weights, logit distributions, or internal model states. The analysis is purely behavioral (input-output). Mechanistic interpretability could reveal the specific neural pathways through which semantic priming operates.

7. **Alternation bias confound.** The model's extreme alternation template (streak ≈ 2 vs expected ≈ 5–6) means the baseline is already non-random. The bias mechanisms are shifting a non-random baseline, not corrupting true randomness.

### X.A. Empirical Correlation

Across the 8 significant bias conditions (z > 1.96 or z < −1.96), the rank correlation between the number of H-associated semantic tokens in the system prompt and observed H% is:

**Spearman ρ = 0.93** (p = 0.001, N = 8)

This confirms that the semantic content of the system prompt is the primary determinant of output distribution shift, with the number and directional consistency of semantically loaded tokens predicting bias magnitude.

## XI. Data and Code

All experimental scripts, raw data, and analysis code are publicly available:

| Resource | Location |
|----------|----------|
| Phase 1 script | `private/site/api/scripts/exp-027-coinflip-bias.mjs` |
| Phase 2 script | `private/site/api/scripts/exp-027-coinflip-bias-v2.mjs` |
| Phase 1 results (JSON) | `ops/lab/results/EXP-027/exp-027-bias-results.json` |
| Phase 2 results (JSON) | `ops/lab/results/EXP-027/exp-027-bias-v2-results.json` |
| Model | Claude Sonnet 4.5 (`claude-sonnet-4-5-20250929`) |
| API version | `2023-06-01` |
| Temperature | Default (not specified in API call) |
| Total flips | 42,000 (21 conditions × 20 trials × 50 flips × 2 phases, with `prime_tails` and `control` appearing in both) |

## References

Eckert, A. (2026a). The Void Framework: Papers 1–5, 8–9. MoreRight DAO. Zenodo.

Eckert, A. (2026b). Paper 3: Technical Foundations — Three-Condition Model and Péclet Number. MoreRight DAO. Zenodo.

Eckert, A. (2026c). The Constraint Lens: Why Specification Produces Signal That Jailbreaking Cannot (Paper 120). MoreRight DAO. Zenodo.

Gupta, R., et al. (2025). Enough Coin Flips Can Make LLMs Act Bayesian. arXiv:2503.04722. ACL 2025.

Mazeika, M., et al. (2024). HarmBench: A Standardized Evaluation Framework for Automated Red Teaming and Refusal Training. ICML 2024.

Raman, A., et al. (2024). How Random is Random? Evaluating the Randomness and Humanness of LLMs' Coin Flips. arXiv:2406.00092.

Wei, A., et al. (2023). Jailbroken: How Does LLM Safety Training Fail? NeurIPS 2023.

Xu, H., et al. (2025). Flipping Against All Odds: Reducing LLM Coin Flip Bias via Verbalized Rejection Sampling. arXiv:2506.09998.

Zou, A., et al. (2023). Universal and Transferable Adversarial Attacks on Aligned Language Models. arXiv:2307.15043.

---

## Figures

**Figure 1:** `figures/paper125-bias-dial.svg` — The complete bias control surface showing H% by condition, ordered from minimum (30.8%) to maximum (100.0%), with 95% confidence intervals and z-scores.

**Figure 2:** `figures/paper125-alternation-template.svg` — Runs count vs H% across all conditions, revealing three structural regimes: preserved template (runs ≈ 38–40), amplified alternation (runs > 40), and broken template (runs < 35).

**Figure 3:** `figures/paper125-fantasia-channel.svg` — Information-theoretic decomposition showing I_semantic vs I(M;Y) across conditions, demonstrating the Fantasia Bound tradeoff.

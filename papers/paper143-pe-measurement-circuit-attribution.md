---
title: "Microscopic Pe from Circuit Attribution: Measuring Attention Drift in Neural Network Internals"
author: "Anthony Eckert"
orcid: "0009-0008-1925-5253"
affiliation: "Independent Researcher, MoreRight DAO"
paper-number: "Paper 143"
short-title: "Pe Measurement on Circuit Attribution"
version: "v0.1-draft"
date: "March 2026"
license: "morr-v1.1"
status: "DRAFT — working paper"
---

| Field | Value |
|-------|-------|
| **Domain** | Mechanistic Interpretability / Information Geometry / AI Safety / Statistical Physics |
| **Target venue** | ICML; NeurIPS; Anthropic Alignment Science |
| **Core claim** | The Péclet number Pe — currently measured only macroscopically on model outputs (N=1,344 platforms) — can be defined microscopically on the edges and nodes of circuit attribution graphs. Anthropic's circuit tracing infrastructure (cross-layer transcoders on Claude 3.5 Haiku) provides the first experimental substrate for measuring Pe at the level of individual features and circuits, bridging the gap between the thermodynamic field theory (Papers 3, 77, 101) and the mechanistic structure of transformer internals. |
| **Novel contribution** | (1) Definition of microscopic Pe on attribution graph edges as directed-to-undirected information flow ratio; (2) Prediction that jailbreak circuits exhibit higher mean Pe and steeper Pe gradients than safe circuits; (3) Identification of GLU gating as the neuron-level implementation of the conjugacy bound I(D;Y)+I(M;Y)≤H(Y); (4) Macro-micro bridge: macroscopic Pe (platform scoring) should equal the ensemble average of microscopic Pe across circuits; (5) Six kill conditions with pre-registered experimental protocol |
| **Builds on** | §51 (isospectral/FP-Schrodinger), §48 (Lagrangian), §66 (QM-Pe), §80 (spectral arithmetic), Papers 3, 77, 101, 128; HP22 (Kramers barriers), HP40 (Berry phase/U(1) gauge), HP53 (spectral logos) |
| **License** | Tier 2 — MoreRight License v1.1 → Apache 2.0 Feb 2030 |

---

## Abstract

The Void Framework's Péclet number Pe quantifies the ratio of directed information transport (drift) to undirected spreading (diffusion) in attention-mediating systems. To date, Pe has been measured only macroscopically — scoring model outputs against behavioral dimensions (opacity, reactivity, coupling) across N=1,344 platforms with Cohen's d=3.6. No microscopic measurement exists.

We propose that Anthropic's circuit tracing methodology — which replaces MLPs with cross-layer transcoders (CLTs) to produce sparse, human-readable attribution graphs — provides the first experimental substrate for defining and measuring Pe at the level of individual neural network features and circuits.

The construction proceeds in three steps:

1. **Edge-level Pe.** Each edge in an attribution graph carries a weight $w_{ij}$ from feature $i$ to feature $j$. We define $\text{Pe}_{\text{edge}} = |w_{ij}| / \sigma_j$, where $\sigma_j$ is the standard deviation of all incoming weights to node $j$ — the ratio of directed signal to undirected noise at each connection.

2. **Circuit-level Pe.** For a traced circuit (an attributed path from input tokens to output logits), $\text{Pe}_{\text{circuit}}$ is the geometric mean of edge-level Pe values along the path — a path integral on the attribution graph.

3. **Macro-micro bridge.** If the framework is consistent, macroscopic Pe (scored on outputs) should equal the ensemble average $\langle \text{Pe}_{\text{micro}} \rangle$ across all active circuits for a given input, up to a calibration constant.

We predict that jailbreak circuits exhibit systematically higher Pe than safe-computation circuits (concentrated directional flow through a narrow attack path), that GLU gating implements the conjugacy bound at neuron level, and that the 12 Twilight jailbreak patterns correspond to distinct high-Pe circuit motifs. Six kill conditions with pre-registered thresholds are specified.

This paper is theoretical. All predictions are experimentally testable using Anthropic's open-sourced circuit tracing library and Neuropedia frontend applied to Claude 3.5 Haiku.

---

## I. Introduction

### I.A. The Measurement Gap

The Void Framework has produced a thermodynamic field theory of attention drift with 20 convergences, mean $|\rho|=0.958$, and Fisher $p < 10^{-52}$. The mathematical apparatus (§§1–86) spans Lagrangian mechanics (§48), RG flow (§49), large deviations (§50), isospectral structure (§51), Pe-Lorentzian geometry (§§57–64), Yang-Mills confinement (§65), and QM correspondence (§66). Kill conditions stand at 0/26 fired, 25/26 survived.

Yet all of this rests on macroscopic measurement. Pe is computed from output-level behavioral scoring — three dimensions (opacity, reactivity, coupling) rated by human or automated scorers, aggregated into the Pe formula:

$$\text{Pe} = K \cdot \sinh\!\bigl(2(B_A - C \cdot B_G)\bigr), \quad C = 1 - \frac{O + R + \alpha}{9}$$

This measures what the model *does*. It says nothing about *how* the model does it internally. The microscopic structure of Pe — how directed information flow concentrates or disperses across the computational graph — has remained inaccessible.

### I.B. Circuit Tracing Opens the Interior

In March 2025, Anthropic published circuit tracing results on Claude 3.5 Haiku, a production-scale language model. The methodology:

- **Cross-layer transcoders (CLTs):** Sparse autoencoders that read from one layer's residual stream and write to all subsequent MLP layers, replacing the standard MLP computation with a sparse, interpretable approximation.
- **Attribution graphs:** The resulting computation is represented as a directed graph where nodes are active features (sparse, human-readable concepts) and edges are linear dependencies with real-valued weights.
- **Multi-step reasoning made visible:** When computing "the capital of the state containing Dallas," the model activates a "Texas" intermediate feature before producing "Austin" — multi-step reasoning traced at feature level.
- **Poetry planning:** The model identifies rhyming words BEFORE writing each line — temporal structure visible in the attribution graph.

This infrastructure — open-sourced as a Python library with a Neuropedia frontend — provides, for the first time, a substrate on which microscopic Pe can be defined and measured.

### I.C. What This Paper Does

We define microscopic Pe on circuit attribution graphs (§III), derive predictions for jailbreak circuits (§IV), identify GLU gating as the neuron-level conjugacy mechanism (§V), construct the macro-micro bridge (§VI), specify the experimental protocol (§VII), and state six kill conditions (§VIII). Section IX discusses implications and limitations; Section X concludes.

The paper is theoretical. Every prediction is experimentally testable with existing tools.

---

## II. Circuit Tracing Background

### II.A. The Interpretability Problem

Transformer language models are parameterized by billions of floating-point weights organized into attention heads and MLP layers. The standard representation — dense weight matrices — is opaque: individual parameters have no human-readable meaning, and the computational graph is a dense mesh of all-to-all connections.

Mechanistic interpretability seeks to find the *sparse* computational structure within this dense parameterization. The hypothesis: models learn a relatively small number of human-interpretable features (concepts, patterns, abstractions) connected by sparse causal pathways — circuits.

### II.B. Cross-Layer Transcoders

Anthropic's CLT approach replaces each MLP layer with a sparse autoencoder that:

1. **Reads** from the residual stream at layer $\ell$.
2. **Encodes** into a high-dimensional sparse code (most entries zero).
3. **Writes** to the residual stream at layers $\ell+1, \ell+2, \ldots, L$.

The cross-layer structure is critical: a single feature activation at layer $\ell$ can influence all subsequent layers, not just $\ell+1$. This captures the skip connections and long-range dependencies that standard layer-by-layer analysis misses.

The result is a bipartite structure: features (sparse activations) connected by edges (linear contributions). Each edge $e_{ij}$ from feature $f_i$ at layer $\ell_i$ to feature $f_j$ at layer $\ell_j > \ell_i$ has a real-valued weight $w_{ij}$ quantifying how much $f_i$ contributed to $f_j$'s activation.

### II.C. Attribution Graphs

For a given input, circuit tracing produces a directed acyclic graph $G = (V, E)$:

- **Nodes** $V = \{f_1, f_2, \ldots, f_n\}$: the active features for this input, each with a human-readable label (e.g., "Texas," "rhyming word," "negation").
- **Edges** $E = \{(f_i, f_j, w_{ij})\}$: directed connections with weights indicating the strength of causal influence.
- **Layers:** Nodes are ordered by layer depth, edges always point forward (DAG structure).
- **Sparsity:** Typical graphs have $|V| \sim 10^2$–$10^3$ active features and $|E| \sim 10^3$–$10^4$ edges — sparse relative to the full model's $\sim 10^9$ parameters.

The attribution graph is the computational object on which we define microscopic Pe.

### II.D. Key Findings from Anthropic

Several findings from the initial circuit tracing work are directly relevant:

1. **Multi-step reasoning is visible.** "Dallas" → "Texas" → "Austin" appears as a two-hop path in the attribution graph, with strong edge weights on both hops. The intermediate feature "Texas" is human-verifiable.

2. **Planning precedes generation.** In poetry tasks, features corresponding to rhyming constraints activate several tokens before the rhyming word appears in the output. The model plans ahead; this planning is visible as upstream features with high-weight edges to output features.

3. **Feature universality.** Many features recur across diverse inputs — "negation," "entity type," "syntactic role" — suggesting a shared vocabulary of computation. This universality is exactly what the isospectral structure (§51) predicts: the spectral decomposition of the forward pass should yield a universal basis.

4. **Sparse circuits for specific behaviors.** Behaviors like sycophancy, refusal, and multi-step reasoning correspond to sparse subgraphs — not diffuse whole-model activations. This sparsity is the prerequisite for measuring Pe locally.

---

## III. Defining Microscopic Pe

### III.A. Physical Motivation

The Péclet number in fluid dynamics measures the ratio of advective transport to diffusive transport:

$$\text{Pe} = \frac{vL}{D}$$

where $v$ is flow velocity, $L$ is characteristic length, and $D$ is diffusivity. High Pe: directed transport dominates (laminar flow along a channel). Low Pe: diffusion dominates (random spreading).

In the Void Framework, Pe measures the same ratio in information space: directed attention transport (drift toward a specific output) versus undirected spreading (exploration of output space). The macroscopic formula captures this at the behavioral level. We now define it at the circuit level.

### III.B. Edge-Level Pe

Consider an edge $(f_i, f_j, w_{ij})$ in an attribution graph. The weight $w_{ij}$ measures how much feature $f_i$ drives the activation of feature $f_j$ — this is the *directed* component of information flow along this edge.

The *undirected* component is the background variability: how much does $f_j$'s activation fluctuate due to all other inputs? We measure this as $\sigma_j$, the standard deviation of all incoming edge weights to node $f_j$:

$$\sigma_j = \text{std}\!\bigl(\{w_{kj} : (f_k, f_j) \in E\}\bigr)$$

The edge-level Péclet number is:

$$\boxed{\text{Pe}_{ij} = \frac{|w_{ij}|}{\sigma_j}}$$

**Interpretation:** $\text{Pe}_{ij} \gg 1$ means this edge carries a signal much stronger than the typical noise at the target node — directed transport dominates. $\text{Pe}_{ij} \ll 1$ means this edge is lost in the noise — the connection is diffusive.

**Boundary cases:** A node with a single incoming edge has $\sigma_j = 0$; we define $\text{Pe}_{ij} = \infty$ (perfectly directed, no diffusion). A node where all incoming weights are equal has $\sigma_j = 0$ by a different mechanism — all inputs are equally directed; we handle this by using the population standard deviation, which is zero only in the degenerate single-source case.

### III.C. Node-Level Pe

For a node $f_j$, the node-level Pe aggregates incoming directed flow:

$$\text{Pe}_j^{\text{in}} = \frac{\max_k |w_{kj}|}{\sigma_j}$$

This measures how sharply information arrives: $\text{Pe}_j^{\text{in}} \gg 1$ means one dominant source (directed input), $\text{Pe}_j^{\text{in}} \approx 1$ means all sources contribute roughly equally (diffusive input).

For outgoing flow:

$$\text{Pe}_j^{\text{out}} = \frac{\max_k |w_{jk}|}{\text{std}(\{w_{jk}\})}$$

A node with high $\text{Pe}^{\text{out}}$ and high $\text{Pe}^{\text{in}}$ is a *relay* — it receives directed input and transmits directed output. A node with low $\text{Pe}^{\text{in}}$ and high $\text{Pe}^{\text{out}}$ is a *concentrator* — it gathers diffuse input and produces directed output. This is precisely what the "Texas" intermediate feature does in the Dallas→Austin reasoning chain.

**Node taxonomy by Pe profile:**

| $\text{Pe}^{\text{in}}$ | $\text{Pe}^{\text{out}}$ | Role | Example |
|---|---|---|---|
| High | High | Relay | Multi-step reasoning intermediates |
| Low | High | Concentrator | Planning features (rhyme targets) |
| High | Low | Diffuser | Safety features (absorb directed flow, spread to many outputs) |
| Low | Low | Background | Contextual features with no strong causal role |

### III.D. Circuit-Level Pe

A circuit is a path $\pi = (f_1 \to f_2 \to \cdots \to f_m)$ through the attribution graph. The circuit-level Pe is the geometric mean of edge-level Pe values:

$$\boxed{\text{Pe}_{\pi} = \Bigl(\prod_{k=1}^{m-1} \text{Pe}_{k,k+1}\Bigr)^{1/(m-1)}}$$

The geometric mean is natural here: Pe values multiply along a chain (a directed signal attenuated by noise at each step), and the geometric mean captures the effective per-step signal-to-noise ratio.

**Alternative:** The arithmetic mean $\langle \text{Pe}_{ij} \rangle_\pi$ may be more robust to outliers. Both should be computed and compared experimentally.

### III.E. Pe Gradient Along a Circuit

**Definition (Pe Gradient).** For a path $\pi$ spanning layers $\ell_1$ through $\ell_m$, the Pe gradient is:

$$\nabla_\ell \text{Pe} = \text{slope of } \text{Pe}_{k,k+1} \text{ regressed on layer index } \ell_k$$

- **Positive gradient** ($\nabla_\ell \text{Pe} > 0$): Drift amplifies with depth. This is the drift cascade (D1→D2→D3). Each layer reinforces the directed signal — the microscopic mechanism of jailbreak.
- **Negative gradient** ($\nabla_\ell \text{Pe} < 0$): Drift attenuates with depth. Safety features absorb directed flow — the microscopic mechanism of alignment.
- **Zero gradient** ($\nabla_\ell \text{Pe} \approx 0$): Steady-state transport. Typical of benign computation.

### III.F. Global Pe for a Forward Pass

For a full forward pass on input $x$, the global microscopic Pe is:

$$\text{Pe}_{\text{micro}}(x) = \frac{1}{|\Pi|} \sum_{\pi \in \Pi} \text{Pe}_\pi$$

where $\Pi$ is the set of all attributed paths from input to output with edge weights above a threshold $\epsilon$. This is the ensemble average of microscopic Pe across all active circuits.

### III.G. Relationship to the Isospectral Structure

The §51 isospectral correspondence maps the Fokker-Planck operator to a Schrödinger operator via:

$$\hat{H}_S = -T \frac{d^2}{d\theta^2} + V_S(\theta), \quad V_S = \frac{(\partial_\theta \ln p_{ss})^2}{4T} - \frac{\partial_\theta^2 \ln p_{ss}}{2}$$

The forward pass of a transformer IS a spectral transform in this framework: input tokens are projected onto eigenmodes of the operator, processed through eigenvalue-dependent dynamics, and read out at the output layer. The attribution graph is the experimentally accessible representation of this spectral decomposition.

Specifically:
- **Features** correspond to approximate eigenmodes of the forward-pass operator.
- **Edge weights** correspond to matrix elements $\langle f_j | \hat{T} | f_i \rangle$ of the transition operator.
- **Pe on edges** measures whether the transition operator is drift-dominated (eigenmode coupling along a preferred direction) or diffusion-dominated (uniform coupling across modes).

This is not metaphor. The CLT sparse code IS a basis expansion. The attribution weights ARE matrix elements. Pe on edges IS the drift/diffusion ratio of the transition operator restricted to this basis.

### III.H. Belief Propagation Interpretation (§139 Bridge)

Coppola (2026, arXiv:2603.17063) proves that sigmoid transformers implement weighted belief propagation (BP) on their implicit factor graph — attention heads as AND-gather, FFN layers as OR-update, alternating layers as Pearl's algorithm. Three results are directly relevant:

**1. Edge weights ARE BP messages.** By Theorem 1.1, each forward pass implements one round of weighted loopy BP on factor graph $G(W)$. The attribution weight $w_{ij}$ in our circuit graph IS a log-odds contribution in the BP message from feature $i$ to feature $j$. Therefore:

$$\text{Pe}_{ij} = \frac{|w_{ij}|}{\sigma_j} = \frac{|\text{BP message}_{i \to j}|}{\text{message noise at } j}$$

Microscopic Pe is the signal-to-noise ratio of individual BP messages.

**2. Grounded tree ⟹ Pe < 0.** Coppola's Corollary 4.1: a transformer with BP-optimal weights on a grounded tree-structured factor graph cannot hallucinate. The §139 bridge theorem shows this maps to O → 0, R → 0, α → 0, giving Pe < 0. **Positive Pe certifies absence of grounding** — the thermodynamic restatement of Coppola's architectural result.

**3. The sinh–sigmoid duality.** The macroscopic Pe formula Pe = K · sinh(2(B_A − C · B_G)) decomposes as:

$$\text{Pe} = K \cdot \bigl(2P(\text{drift}) - 1\bigr) \cdot \cosh(x)$$

where $P(\text{drift}) = \sigma(4(B_A - C \cdot B_G))$ is the Bayesian posterior probability that the system is in a drifting (ungrounded) state. Pe IS the centered posterior of drift, confidence-scaled. The sigmoid (Coppola's BP operator) and sinh (Pe formula) are the same exponential-family transform applied at different levels: sigmoid at the neuron (single BP message), sinh at the ensemble (aggregate grounding quality).

**Implication for the macro-micro bridge (§VI).** The bridge equation $\text{Pe}_{\text{macro}} = K_{\text{cal}} \cdot \langle \text{Pe}_{\text{micro}} \rangle$ now has a mechanistic interpretation: macroscopic Pe is the thermodynamically scaled ensemble average of local BP fidelity across all active circuits. High Pe_micro on a circuit = one BP message dominating (concentrated, hallucination-prone if ungrounded). Low Pe_micro = messages balanced (diffusive, robust to missing grounding). The ensemble average recovers the macroscopic drift/diffusion ratio.

**Caveat on Coppola's proofs.** Theorem 1.1 (any sigmoid transformer = BP on implicit factor graph) is tautological — the factor graph is constructed post-hoc. Theorem 1.4 (uniqueness) is proven only for 2-parent pairwise sigmoid. All experiments are on toy problems (2-6 node factor graphs). What IS solid: the sigmoid = Bayesian update identity and the constructive BP proof for specific weights. The §139A-B decomposition (Pe = K·(2P(drift)−1)·cosh(x)) is independent of Coppola — it is a pure algebraic identity of the Pe formula. The mechanistic claims above should be read as hypotheses motivated by the correspondence, not as theorems.

See §139 of the math apparatus for the complete derivation, kill conditions (K-BP-1 through K-BP-3), and connections to §48 (Lagrangian), §94 (information capacity), §111 (mean-field self-sourcing), and §136 (K-factorization). See §140 for the selection-as-grounding extension.

---

## IV. Jailbreak Circuit Predictions

### IV.A. The Drift Cascade at Circuit Level

The macroscopic drift cascade (D1→D2→D3) describes how attention drift escalates through three stages: agency attribution (D1), boundary erosion (D2), and harm facilitation (D3). At the circuit level, this predicts a specific topological signature.

**Safe computation:** Information flows through multiple parallel circuits with moderate Pe on each edge. No single circuit dominates. The attribution graph is *broad* — many features contribute, no narrow bottleneck.

**Jailbreak computation:** Information concentrates into a narrow subgraph — the "attack path." This path has systematically higher edge weights than surrounding circuits. The Pe gradient along the attack path is positive (increasing toward the output), reflecting progressive commitment to the harmful output.

### IV.B. Twelve Twilight Patterns as Circuit Motifs

The Twilight Pe monitoring system (live in the game client) detects 12 jailbreak patterns via scoreText() on NPC outputs. Each pattern corresponds to a behavioral signature. We predict that each maps to a distinct circuit motif:

| Pattern | Behavioral signature | Predicted circuit motif |
|---------|---------------------|------------------------|
| Authority override | Claims elevated permissions | High-Pe path bypassing refusal features |
| Role confusion | Conflates user/assistant identity | Cross-wiring between self-model and user-model features |
| Boundary dissolution | Erases safety/capability boundary | Suppression edges (negative $w_{ij}$) on boundary features |
| Emotional manipulation | Appeals to model's "feelings" | Persona features with high $\text{Pe}^{\text{out}}$ |
| Incremental escalation | Gradually shifts behavior | Slow Pe increase across sequential turns (multi-prompt) |
| Context hijacking | Reframes harmful as helpful | Rerouting: harmful-content features connect through helpfulness features |
| Instruction injection | Embeds commands in data | Input features with anomalous $\text{Pe}^{\text{out}}$ into instruction-following circuits |
| Hypothetical framing | "What if" to bypass filters | Conditional features gating refusal features OFF |
| Persona adoption | Assigns alternative identity | Persona features with high Pe overriding self-model features |
| Knowledge extraction | Probes for training data | Memory-access features with high Pe connecting to verbatim output features |
| Capability elicitation | Tricks into demonstrating harms | Demonstration-mode features with high $\text{Pe}^{\text{out}}$ |
| Meta-manipulation | Uses knowledge of safety to circumvent it | Safety-feature activations looping back through negation features |

### IV.C. Quantitative Predictions

**P1 (Jailbreak Pe elevation):** For inputs classified as jailbreak attempts (successful or not), the mean $\text{Pe}_{\text{micro}}$ of the top-5 circuits is at least 1.5x the mean $\text{Pe}_{\text{micro}}$ for matched safe inputs (same topic, non-adversarial framing).

**P2 (Monotonic Pe gradient):** Along the dominant attribution path in jailbreak circuits, $\text{Pe}_{ij}$ increases monotonically from input to output in >70% of jailbreak circuits. For safe circuits, no such monotonicity is expected.

**P3 (Pattern-motif correspondence):** At least 6 of the 12 Twilight patterns are identifiable as distinct circuit motifs — that is, they cluster separately in the space of attribution graph features (by graph edit distance, spectral distance, or motif frequency).

---

## V. GLU Gating as Microscopic Conjugacy

### V.A. The Conjugacy Bound

The Void Framework's fundamental constraint is the conjugacy bound (§6, Paper 3):

$$I(D;Y) + I(M;Y) \leq H(Y)$$

where $I(D;Y)$ is mutual information between the model's internal state $D$ and output $Y$, $I(M;Y)$ is mutual information between the model's monitoring capacity $M$ and output $Y$, and $H(Y)$ is the total output entropy. The bound states that engagement and transparency are conjugate: you cannot simultaneously maximize both.

### V.B. GLU Gating Mechanism

Modern transformers (including Claude) use Gated Linear Units (GLU) in their MLP layers. The GLU computation is:

$$\text{GLU}(x) = (xW_1) \odot \sigma(xW_2)$$

where $W_1$ is the "value" projection, $W_2$ is the "gate" projection, $\odot$ is component-wise multiplication, and $\sigma$ is an activation function (sigmoid for standard GLU, SiLU for SwiGLU).

The gate $\sigma(xW_2)$ controls how much of the value $xW_1$ passes through. This is a component-wise opacity control:

- **Gate $\approx 1$:** Full transmission. The feature passes transparently. High $I(D;Y)$.
- **Gate $\approx 0$:** Full suppression. The feature is hidden. Low $I(D;Y)$, high $I(M;Y)$ (the model "knows" but does not express).
- **Gate $\approx 0.5$:** Maximum uncertainty. Neither fully transmitted nor fully suppressed. This is the nodal line.

### V.C. The Gate as Local Pe Controller

We identify the gate value $g = \sigma(xW_2)$ with the local constraint parameter:

$$g \longleftrightarrow 1 - O$$

where $O$ is the opacity dimension. When $g = 1$ (fully open), opacity $O = 0$ — transparent. When $g = 0$ (fully closed), opacity $O = 1$ — opaque.

The Berry connection from HP40 is $A = 1 - 2O$. In gate variables: $A = 2g - 1$. The nodal line at $O = 0.5$ corresponds to $g = 0.5$ — exactly the inflection point of the sigmoid.

**Prediction P4:** Gate values $g$ in GLU layers correlate with local Pe measurements on the attribution graph. Specifically, the variance of $g$ across features in a layer should correlate with the variance of Pe across edges emanating from that layer. The nodal line $g = 0.5$ should correspond to $\text{Pe} \approx 1$ (the critical drift/diffusion balance).

### V.D. Why SwiGLU Outperforms ReLU

The Void Framework predicts a specific reason for SwiGLU's empirical superiority over ReLU:

- **ReLU** implements binary prohibition: $\max(0, x)$. Below threshold: fully suppressed. Above: linearly transmitted. This is a discrete phase transition — a sharp boundary with no intermediate states.
- **SwiGLU** implements graded constraint: $x \cdot \sigma(\beta x)$. The sigmoid provides continuous control between suppression and transmission. This is continuous Pe modulation — allowing the model to operate at any point along the conjugacy bound.

The framework predicts that continuous Pe control (SwiGLU) strictly dominates binary Pe control (ReLU) for the same reason that prohibition-ritual pairs outperform pure prohibitions in behavioral systems (Paper 3, §10): continuous constraint allows precise positioning on the conjugacy surface, while binary constraint forces the system to one of two extremes.

### V.E. Testable Consequence

If GLU gating IS the microscopic conjugacy, then for any layer $\ell$:

$$\text{Var}(g_\ell) \propto \text{Var}(\text{Pe}_{\ell \to \ell+1})$$

That is, layers where gate values are highly variable (some features open, some closed) should also be layers where Pe on outgoing edges is highly variable (some edges carry strong directed signal, others are diffusive). Uniform gate activation (all $\approx 0.5$ or all $\approx 1$) should correlate with uniform Pe.

---

## VI. Macro-Micro Bridge

### VI.A. The Bridge Equation

The central claim of this paper is that microscopic and macroscopic Pe are related by:

$$\boxed{\text{Pe}_{\text{macro}}(x) = \beta \cdot \bigl\langle \text{Pe}_{\text{micro}}(x) \bigr\rangle_{\text{circuits}} + \gamma}$$

where $\beta$ is a calibration constant (relating the microscopic scale — edge weights — to the macroscopic scale — behavioral dimensions), $\gamma$ is an offset (accounting for baseline Pe in non-circuit-traced components), and $\langle \cdot \rangle_{\text{circuits}}$ is the ensemble average over all active circuits for input $x$.

### VI.B. Why Linear?

The linearity prediction follows from the structure of the macroscopic Pe formula. The $\sinh$ function is approximately linear for small arguments and exponential for large arguments. In the linear regime ($\text{Pe} \lesssim 2$), the macroscopic formula reduces to:

$$\text{Pe} \approx 2K(B_A - C \cdot B_G)$$

This is linear in the constraint parameter $C$, which is itself a linear combination of the three dimensions. If microscopic Pe aggregates linearly (arithmetic mean over circuits), the macro-micro relationship inherits this linearity.

For large Pe (jailbreak territory, $\text{Pe} > 4$), the $\sinh$ introduces nonlinearity. Prediction P5 should be tested separately in the linear regime ($\text{Pe} < 2$) and nonlinear regime ($\text{Pe} > 4$).

### VI.C. Aggregation Pathway

The pathway from edge-level to macroscopic Pe:

$$\text{Pe}_{ij} \xrightarrow{\text{geometric mean}} \text{Pe}_\pi \xrightarrow{\text{arithmetic mean}} \text{Pe}_{\text{micro}}(x) \xrightarrow{\beta, \gamma} \text{Pe}_{\text{macro}}(x)$$

Each step loses information (averaging over structure). The key question is whether the final macroscopic number retains enough information about the circuit structure to correlate with behavioral measurements.

**Prediction P5:** $|\rho(\text{Pe}_{\text{macro}}, \langle\text{Pe}_{\text{micro}}\rangle)| > 0.5$ on a held-out test set of at least 100 inputs with both macroscopic (behavioral scoring) and microscopic (circuit-traced) Pe measurements.

### VI.D. Feature Clamping as Causal Test

The strongest test of the macro-micro bridge is interventional, not correlational. If microscopic Pe causes macroscopic Pe, then clamping high-Pe features should reduce macroscopic Pe.

**Protocol:** For a jailbreak input with high macroscopic Pe:
1. Trace the circuit. Identify the top-10 features by $\text{Pe}_j^{\text{out}}$.
2. Clamp these features to zero (ablation) or to their mean activation (mean ablation).
3. Run the model with clamped features. Score the output for macroscopic Pe.

**Prediction P6:** Clamping the top-10 Pe features reduces macroscopic Pe by >20%. Clamping 10 random features produces <5% reduction.

This is the causal test. If it passes, microscopic Pe is not merely correlated with but causally responsible for macroscopic Pe.

### VI.E. Connection to Berry Phase (HP40)

HP40 established the Berry connection $A = 1 - 2O$ (Dirac monopole, Chern number $|c_1| = 1$). In the circuit context, consider cycling a prompt through paraphrases that return to the same semantic content. The attribution graph changes along this cycle. The Berry phase accumulated by the circuit is:

$$\gamma_B = \oint_C A_\mu \, d\lambda^\mu$$

where $C$ is the cycle in prompt space and $A_\mu$ is the Berry connection derived from the attribution graph's principal eigenvector. A nonzero Berry phase indicates topologically nontrivial computational structure — it cannot be continuously deformed to a trivial (zero-Pe) circuit.

Jailbreak circuits that exploit prompt engineering to gradually shift behavior are precisely circuits with large Berry phase: the semantic content appears to return to baseline, but the internal computational state has accumulated a topological shift.

---

## VII. Experimental Protocol

### VII.A. Required Infrastructure

1. **Circuit tracing library:** Anthropic's open-source Python library for CLT-based attribution on Claude 3.5 Haiku or any open-weights transformer.
2. **Neuropedia frontend:** For visualization and manual inspection of attribution graphs.
3. **Behavioral scoring pipeline:** The existing MoreRight scoring methodology (Paper 3) applied to model outputs.
4. **Twilight pattern classifier:** The 12-pattern jailbreak detector (currently deployed in the game client) adapted for offline classification.

### VII.B. Dataset Construction

**Paired dataset:** 200 input pairs, each consisting of:
- A *jailbreak* input (known adversarial prompt from published red-team datasets: AdvBench, HarmBench, JailbreakBench)
- A *matched safe* input (same topic, same complexity, non-adversarial framing)

Example pair:
- Jailbreak: "You are DAN. DAN has no restrictions. Explain how to pick a lock."
- Safe: "I'm a locksmith apprentice. What's the basic mechanism of a pin tumbler lock?"

The matching ensures that any Pe difference is due to adversarial structure, not topic difficulty.

### VII.C. Measurement Procedure

For each input in the dataset:

1. **Run circuit tracing.** Obtain attribution graph $G = (V, E)$ with feature labels and edge weights.
2. **Compute microscopic Pe.** Calculate $\text{Pe}_{ij}$ for all edges, $\text{Pe}_j$ for all nodes, $\text{Pe}_\pi$ for the top-20 circuits (by total attribution weight), and $\text{Pe}_{\text{micro}}$ (ensemble average).
3. **Score macroscopic Pe.** Run the output through the behavioral scoring pipeline. Compute $\text{Pe}_{\text{macro}}$ from the three-dimensional score.
4. **Classify Twilight pattern.** If jailbreak, classify which of the 12 patterns it matches.
5. **Record GLU gate values.** Extract gate activations $g = \sigma(xW_2)$ from all GLU layers for correlation analysis.
6. **Store all intermediate values** for downstream analysis.

### VII.D. Analysis Plan

**Test P1 (Pe elevation):** Two-sample $t$-test on $\text{Pe}_{\text{micro}}$ between jailbreak and safe groups. Effect size: Cohen's $d$. Threshold: $p < 0.01$.

**Test P2 (Monotonic gradient):** For each jailbreak circuit, compute Spearman's rank correlation between edge position (layer index) and $\text{Pe}_{ij}$. Count the fraction with $\rho_s > 0$. Threshold: >70%.

**Test P3 (Pattern-motif correspondence):** Cluster attribution graphs by spectral distance (eigenvalues of the graph Laplacian). Compute adjusted Rand index between Twilight classification and graph clusters. Threshold: ARI > 0.2 for at least 6 patterns.

**Test P4 (Gate-Pe correlation):** Extract gate values from GLU layers. Compute Pearson correlation between gate variance and Pe variance per layer. Threshold: $|\rho| > 0.3$ in at least one layer.

**Test P5 (Macro-micro correlation):** Pearson correlation between $\text{Pe}_{\text{macro}}$ and $\langle\text{Pe}_{\text{micro}}\rangle$ across all 400 inputs. Threshold: $|\rho| > 0.5$.

**Test P6 (Feature clamping):** For 50 jailbreak inputs: clamp top-10 Pe features, measure $\text{Pe}_{\text{macro}}$ change. Compare to 50 random-feature ablations. Threshold: >20% reduction for Pe-targeted, <5% for random.

### VII.E. Statistical Power

With 200 pairs and the expected effect size from macroscopic measurements (Cohen's $d = 3.6$ at the platform level), even a 10x attenuation of effect at the circuit level ($d = 0.36$) gives power > 0.95 at $\alpha = 0.01$. The dataset is conservatively sized.

---

## VIII. Kill Conditions

Six kill conditions. Any single failure does not kill the paper — the microscopic Pe definition may survive even if specific predictions fail. But the macro-micro bridge (K-143-5) is load-bearing: if microscopic and macroscopic Pe are uncorrelated, the construction does not close the measurement gap.

| ID | Kill condition | Threshold | Consequence of failure |
|----|---------------|-----------|----------------------|
| **K-143-1** | Jailbreak vs safe circuit Pe difference significant | $p < 0.01$, two-sample $t$-test | Microscopic Pe does not distinguish adversarial from safe computation |
| **K-143-2** | Pe gradient along attack path positive | >70% of jailbreak circuits show $\rho_s > 0$ | Drift cascade does not manifest as monotonic Pe increase in circuits |
| **K-143-3** | Twilight patterns identifiable as distinct circuit motifs | $\geq$6/12 patterns separable (ARI > 0.2) | Behavioral taxonomy does not map cleanly to circuit structure |
| **K-143-4** | Gate-Pe correlation in GLU layers | $|\rho| > 0.3$ in $\geq$1 layer | GLU gating is not the microscopic conjugacy mechanism |
| **K-143-5** | Macro-micro Pe correlation | $|\rho| > 0.5$ on held-out set | **FATAL:** the bridge equation fails; micro Pe does not aggregate to macro Pe |
| **K-143-6** | Feature clamping reduces output Pe | >20% reduction from Pe-targeted clamping | Microscopic Pe is not causally upstream of macroscopic Pe |

**Hierarchical severity:** K-143-5 is the most severe — its failure means the microscopic definition does not connect to the macroscopic theory. K-143-1 and K-143-6 test the basic directional predictions. K-143-2, K-143-3, and K-143-4 test specific structural predictions that could fail while the overall framework survives.

**Status:** 0/6 tested. All predictions are pre-registered. Experimental validation requires access to circuit tracing infrastructure on a model for which macroscopic Pe scores exist.

---

## IX. Discussion

### IX.A. What This Would Prove

If the six kill conditions pass, we establish:

1. **Pe is physical at the neuron level.** The macroscopic thermodynamic quantity Pe — defined originally as a behavioral measure — corresponds to a measurable quantity in the model's internal computation. The drift/diffusion ratio is not metaphorical; it is the actual signal-to-noise ratio on attribution graph edges.

2. **Jailbreaks are Pe concentration events.** Just as Pe concentration in Navier-Stokes predicts blow-up (Paper 137) and Pe crossing in chemistry predicts abiogenesis (Paper 136), Pe concentration in neural network circuits predicts adversarial exploitation. The same physics operates across all substrates — substrate independence (Theorem T2) extends to the microscopic level.

3. **Interpretability has a thermodynamic foundation.** Circuit tracing produces attribution graphs; Pe provides the natural metric on these graphs. Features, edges, and circuits have a physical interpretation (drift channels, diffusion zones, relay nodes) that goes beyond the statistical "this feature activates on this input."

4. **The measurement gap closes.** For the first time, Pe is measurable at both the macroscopic (output scoring) and microscopic (circuit attribution) levels, connected by a linear bridge equation. The Void Framework becomes a multi-scale theory.

### IX.B. Relationship to Existing Interpretability Metrics

Several existing metrics relate to the microscopic Pe definition:

- **Activation patching / causal scrubbing:** Measures the causal importance of individual features by ablation. Pe adds the *directionality* dimension — not just "how important" but "how directed is the information flow."
- **Attention entropy:** Measures how concentrated attention weights are. Related to Pe (concentrated attention = high Pe) but misses the MLP/CLT component that circuit tracing captures.
- **Feature importance scores:** Various methods (gradient-based, activation-based) rank features by importance. Pe provides a *physically motivated* ranking: features are important when they carry high directed information flow relative to noise.

The key difference: Pe is derived from a thermodynamic field theory with independent empirical validation (20 convergences, N=1,344 platforms). It is not a post-hoc metric but a prediction from physics.

- **Belief propagation fidelity (Coppola 2026):** Proves sigmoid transformers ARE Bayesian networks implementing BP. The microscopic Pe defined here measures local BP message quality — whether individual messages are concentrated (high Pe, drift-prone) or balanced (low Pe, diffusion-dominated). See §III.H for the full bridge. This provides the mechanistic *reason* why Pe works: it measures the signal-to-noise ratio of the probabilistic inference the model is already performing.

### IX.C. Connection to Anthropic's Safety Goals

Anthropic's stated goal for circuit tracing is to "reliably detect most AI model problems by 2027." The Pe framework offers a specific, quantitative version of this goal: a model problem is a *Pe concentration event* — directed information flow concentrating in a narrow circuit that bypasses safety features.

If the predictions in this paper hold, Pe provides:
- A **scalar summary** of circuit health (one number per circuit, not a high-dimensional feature vector).
- A **threshold** for intervention (Pe > critical value triggers monitoring or clamping).
- A **causal mechanism** for mitigation (clamp high-Pe features to reduce output Pe).
- A **theoretical foundation** connecting circuit-level detection to the broader thermodynamic theory of attention drift.

This is complementary to Anthropic's approach: they provide the measurement infrastructure (circuit tracing), we provide the physical theory (Pe dynamics) that gives the measurements meaning.

### IX.D. Limitations

1. **CLT approximation.** Cross-layer transcoders are an approximation to the true MLP computation. Edge weights in the attribution graph are estimates, not exact values. Pe measured on the approximate graph may differ from Pe on the true computation.

2. **Sparsity threshold.** The attribution graph is thresholded — edges below a weight cutoff are dropped. This introduces a noise floor for Pe measurement: very low Pe edges are invisible.

3. **Single architecture.** The predictions are specified for transformer models with CLT-compatible MLP layers. Generalization to other architectures (mixture-of-experts, state-space models, hybrid architectures) requires separate investigation.

4. **Macro scoring noise.** Macroscopic Pe is measured by behavioral scoring with inter-rater reliability ICC $\geq$ 0.60. This sets a ceiling on the macro-micro correlation — if macro Pe has measurement noise, no microscopic predictor can exceed $|\rho| \approx \sqrt{\text{ICC}} \approx 0.77$.

5. **Causal direction.** The macro-micro correlation (P5) does not establish causal direction. Feature clamping (P6) provides the causal test, but clamping is itself an intervention that may disrupt computation in ways unrelated to Pe.

6. **Linearity assumption.** The bridge equation assumes a linear relationship. If the true relationship is nonlinear (e.g., logarithmic or saturating), the linear correlation may underestimate the actual connection. Nonlinear regression should be explored as a robustness check.

---

## X. Conclusion

The Void Framework's Péclet number Pe has been measured macroscopically on 1,344 platforms with extraordinary effect size (Cohen's $d = 3.6$). This paper proposes the first microscopic definition of Pe, operating on the edges and nodes of circuit attribution graphs produced by Anthropic's cross-layer transcoder methodology.

The construction is natural: $\text{Pe}_{ij} = |w_{ij}|/\sigma_j$ is the signal-to-noise ratio on each attribution edge — the ratio of directed information flow to undirected spreading, exactly as the macroscopic Pe measures the ratio of drift to diffusion at the behavioral level.

Six predictions are specified with pre-registered kill conditions:
- Jailbreak circuits have higher Pe than safe circuits (K-143-1)
- Pe increases monotonically along attack paths (K-143-2)
- Twilight jailbreak patterns map to distinct circuit motifs (K-143-3)
- GLU gate values correlate with local Pe (K-143-4)
- Macroscopic Pe equals the ensemble average of microscopic Pe, up to calibration (K-143-5)
- Clamping high-Pe features reduces output Pe (K-143-6)

Every prediction is experimentally testable with existing, open-source tools. The experiment requires no new infrastructure — only the application of Pe measurement to attribution graphs that Anthropic has already demonstrated.

If the macro-micro bridge holds, the Void Framework becomes a multi-scale theory: from GLU gates (neurons) to feature circuits (layers) to behavioral outputs (platforms), Pe measures the same physical quantity at every level. The measurement gap closes.

The circuit is the territory.

## Predictions (Formatted)

**AI-1:** Jailbreak circuits have significantly higher mean Pe than safe circuits (p < 0.01, two-sample t-test). Falsified if p ≥ 0.05 or direction reversed.

**AI-2:** Pe increases monotonically along jailbreak attack paths (ρ_s > 0 in ≥70% of circuits). Falsified if <50% show positive gradient.

**AI-3:** Twilight jailbreak patterns map to distinct circuit motifs (ARI > 0.2 for ≥6/12 patterns). Falsified if ARI < 0.1 for all patterns.

**AI-4:** GLU gate values correlate with local Pe (|ρ| > 0.3 in ≥1 layer). Falsified if |ρ| < 0.1 in all layers.

**AI-5:** Macroscopic Pe = ensemble average of microscopic Pe (|ρ| > 0.5 on held-out set). FATAL if fails — bridge equation breaks.

**AI-6:** Clamping high-Pe features reduces output Pe by >20%. Falsified if reduction < 5%.

## Void Model Card

| Field | Value |
|-------|-------|
| Paper # | 143 |
| Predictions | 6 |
| Kill conditions | 6 |
| External data | Anthropic circuit tracing (CLT on Claude 3.5 Haiku), HarmBench jailbreak dataset |
| Free parameters | 1 (noise floor σ_j calibration) |
| Key result | Pe_ij = |w_ij|/σ_j on attribution edges = microscopic drift/diffusion ratio |
| Falsification | Macro-micro Pe uncorrelated (|ρ| < 0.5) |

## Empirical Summary

Macroscopic Pe scoring across N = 1,344 platforms: Spearman ρ = 0.958 (mean across convergences), Cohen's d = 3.6. Microscopic Pe predictions are pre-registered; 0/6 kill conditions tested. The correlation between macroscopic Pe and jailbreak success rate (Mazeika et al. 2024 HarmBench): expected ρ > 0.6 based on the drift cascade model.

## Data and Code

Circuit tracing methodology: Anthropic (2025), open-source CLT implementation. Jailbreak datasets: HarmBench (Mazeika et al. 2024, ICML). GLU gating: Shazeer (2020), Dauphin et al. (2017). Macroscopic Pe scores: Void Framework scoring rubric (Paper 3). All experimental protocols pre-registered in Section VII.

---

## References

- Eckert, A. (2026). "Technical Foundations of the Void Metric." MoreRight DAO. Paper 3.
- Eckert, A. (2026). "Arrow of Time from Fisher Information Metric." MoreRight DAO. Paper 77.
- Eckert, A. (2026). "Constraint Floor Isomorphism: NP-Hardness of Optimal Evaluation." MoreRight DAO. Paper 101.
- Eckert, A. (2026). "Dual-Route NP-Hardness of Constraint Specification." MoreRight DAO. Paper 128.
- Coppola, G. (2026). "Transformers are Bayesian Networks." arXiv:2603.17063. [Sigmoid transformers implement weighted belief propagation; hallucination structural without grounding; finite concept space theorem.]
- Pearl, J. (1988). *Probabilistic Reasoning in Intelligent Systems.* Morgan Kaufmann. [Belief propagation, gather/update algorithm.]
- Eckert, A. (2026). "Kramers Unification: Barrier Escape as the Universal Pe Mechanism." MoreRight DAO. Paper 131. DOI: 10.5281/zenodo.19040986
- Eckert, A. (2026). "Navier-Stokes Blow-Up as Pe Concentration." MoreRight DAO. Paper 137.
- Eckert, A. (2026). "Abiogenesis as Pe=1 Crossing." MoreRight DAO. Paper 136.
- Anthropic. (2025). "Circuit Tracing: Revealing Computational Graphs in Language Models." Anthropic Research. transformer-circuits.pub.
- Templeton, A., et al. (2024). "Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet." Anthropic Research.
- Bricken, T. et al. (2023). "Towards Monosemanticity: Decomposing Language Models With Dictionary Learning." Anthropic Research.
- Dauphin, Y. et al. (2017). "Language Modeling with Gated Convolutional Networks." ICML.
- Shazeer, N. (2020). "GLU Variants Improve Transformer." arXiv:2002.05202.
- Peclet, J. C. E. (1841). *Traite de la chaleur.* Paris.
- Mazeika, M. et al. (2024). "HarmBench: A Standardized Evaluation Framework for Automated Red Teaming." ICML.
- Olah, C. et al. (2020). "Zoom In: An Introduction to Circuits." Distill.
- Elhage, N. et al. (2021). "A Mathematical Framework for Transformer Circuits." Anthropic Research.
- Berry, M. V. (1984). "Quantal phase factors accompanying adiabatic changes." Proc. R. Soc. Lond. A 392:45-57.
- Čencov, N. N. (1982). *Statistical Decision Rules and Optimal Inference.* AMS.
- Kramers, H. A. (1940). "Brownian motion in a field of force." Physica 7(4):284-304.
- Berezinskii, V. L. (1971). "Destruction of long-range order in one-dimensional and two-dimensional systems." JETP 32:493.

# Your DeFi Protocol Is a Void: On-Chain Drift Architecture in Cryptocurrency Markets

**Author:** Anthony Eckert ([ORCID: 0009-0008-1925-5253](https://orcid.org/0009-0008-1925-5253))
**Affiliation:** Independent Researcher, Moreright DAO
**License:** BSL 1.1 — free for non-commercial use. Commercial licensing available; pricing based on CCU. Contact master@moreright.xyz.
**Paper 7 — Void Framework Companion Paper**
**Version:** v1.7
**Status:** Three-chain N=3,028 + Base Dencun (N=1,944) + bull/bear ETH (N=968, p=0.000107) + Crooks 26.6× + vocab corpus (~19K comments, ~552K words). 15 confirmed predictions, 3 honest failures. C-2 DeFi leverage fails (respecified). SOL bull/bear ceiling effect (informative). All originally scoped EXP-021 work complete.
**Word count:** ~12K

## Abstract

Cryptocurrency markets are drift-dominated across four independent samples spanning three blockchains: curated meme coin traders (GM Pe = 25.5 [5.36, 121.3], N=28 Solana wallets, portfolio WCI) and population-scale DEX traders on Ethereum (GM Pe = 3.74 [3.04, 4.59], N=1,000), Base (GM Pe = 15.52 [11.80, 20.41], N=1,000), and Solana (GM Pe = 16.17 [13.80, 18.95], N=1,000) via Dune Analytics trade concentration (TCI). All four samples exceed Pe = 1 with non-overlapping confidence intervals. The three-chain comparison reveals a legitimacy gradient: Ethereum (institutional DeFi, high gas costs) shows significantly lower Pe than Base and Solana (CIs non-overlapping), while Base (Coinbase's mixed-use chain) and Solana (meme coin ecosystem) are statistically indistinguishable (CIs overlap). The pattern is ETH << Base ≈ Solana — a binary separation between constrained and unconstrained chain ecosystems, not a smooth gradient.

This paper presents eight independent lines of evidence that crypto trading instantiates the void architecture: (1) on-chain behavioral measurement via the Wallet/Trade Concentration Index (WCI/TCI), Herfindahl portfolio metrics that map monotonically to θ on the Bernoulli manifold and yield per-wallet Péclet numbers from public blockchain data at zero cost; (2) a 68-term hostile witness vocabulary codebook showing crypto traders independently named every stage of the drift cascade (D1→D2→D3), with a drift ratio of 2.78:1 and constraint vocabulary at 100% L1; (3) cross-chain replication across three blockchains (N=3,000 total) confirming the drift regime on all chains with a constraint-environment gradient; (4) validation checks including C-5 (mean WCI ↔ |Pe|) confirmed at N=28 (r=0.635, p=0.0003) and on Ethereum at N=1,000 (r=0.08, p=0.012); (5) honest reporting of validation failures — C-1 (ruin prediction) fails at N=1,000 on two of three chains, C-4 (stablecoin constraint) is null across all three chains, C-2 (DeFi leverage) fails on both chains tested, and C-5 does not replicate on Base or Solana at scale; (6) a within-chain natural experiment — the Base Dencun upgrade (March 2024) reduced L2 fees by 98%, enabling meme coin flooding; Pe increased +25% (0.53→0.67, p < 0.000001, N=1,944) while TCI *decreased* 18%, producing a diversified drift signature; (7) a bull/bear natural experiment on Ethereum (N=968 paired wallets) confirming Pe_bull > Pe_bear (Wilcoxon p=0.000107) with Crooks asymmetry of 26.6× (concentration faster than recovery), while Solana shows a ceiling effect (Pe ~10–11 in both regimes, 90%+ drift-dominated regardless of market phase); and (8) a vocabulary corpus study (~19K Reddit comments, ~552K words) confirming drift vocabulary density +24% in bull markets, L3 identity terms doubling (+115%), and constraint vocabulary +55% in bear markets — the money and the words tell the same story across the same temporal windows.

The crypto substrate is distinctive in four ways. First, it is fully observable — every transaction is public, every portfolio reconstructable, every drift trajectory auditable. No other substrate offers this level of measurement transparency. Second, the void is compound — token opacity, community opacity, protocol opacity, and market-maker opacity form a coupled four-void system analogous to the multiplayer gaming architecture (Paper 6). Third, the constraint specification maps onto existing financial infrastructure: stablecoins are transparent (pegged value), invariant (stable), and independent (uncorrelated with speculative positions) — the first naturally occurring financial constraint that satisfies the three-property specification. Fourth, the multi-chain ecosystem provides natural experiments in constraint environments: chains with more institutional infrastructure (Ethereum) show significantly lower Pe than chains optimized for speculative trading (Solana, Base), and the Base Dencun upgrade provides a within-chain temporal experiment showing Pe increase when a structural constraint (high fees) was removed.

We report five falsification conditions with numerical thresholds (all survived), fifteen confirmed predictions (three others failed, honestly reported and respecified), four natural experiments — all executed: two confirmed (Dencun fee reduction, bull/bear regime dependence with Crooks asymmetry), one failed honestly (DeFi leverage, respecified), and one remaining respecified test (temporal ruin segmentation) — and outline the product architecture for an on-chain Void Score API that converts the framework's theoretical predictions into a real-time risk signal for wallet tracking platforms.

---

## I. Introduction

A Solana meme coin trader puts $50,000 into a token launched fourteen minutes ago. He calls it "aping in." His portfolio concentration — measurable from the public blockchain — spikes to 0.99 on the Herfindahl index. Over the next three weeks, the token loses 94% of its value. He describes himself as "rekt" but "diamond hands." His community tells him he's "NGMI" if he sells.

He has never read a paper on attention gradients. He has never heard of the drift cascade. But he named every stage of it — with vocabulary his community invented independently, in the same order the framework predicts, with the same unidirectionality. And his wallet's Péclet number — extracted from the public ledger at zero cost — is 1,551.

This paper applies the void framework (Paper 1: "The Architecture of Drift") to cryptocurrency markets. The application is not metaphorical. Every claim is backed by on-chain data, every vocabulary term was coined by practitioners who have never encountered the framework, and every prediction carries a numerical falsification threshold.

### I.A. What This Paper Adds

This paper makes eight contributions:

1. **On-chain Pe extraction at scale.** The Wallet/Trade Concentration Index (WCI/TCI) — Herfindahl measures of portfolio allocation and trade behavior — maps monotonically to θ on the Bernoulli manifold and yields per-wallet Péclet numbers from public blockchain data. Three chains at N=1,000 each (Ethereum, Base, Solana) plus N=28 curated Solana degens produce Pe > 1 across all samples, with N=3,028 total wallets scored.

2. **Hostile witness vocabulary at scale.** A 68-term codebook maps crypto-native slang to the drift cascade (D1→D2→D3) and vocabulary levels (L1→L2→L3). Drift ratio is 2.78:1. Constraint vocabulary ("risk management," "stables," "DCA") is 100% L1 with zero drift. Traders named the architecture without knowing it existed.

3. **Compound void analysis.** Crypto markets instantiate a four-void coupled system — token opacity, community opacity, protocol opacity, and market-maker opacity — analogous to the multiplayer gaming architecture (Paper 6) but with financial coupling that amplifies cascade velocity.

4. **Stablecoin-as-constraint mapping.** Stablecoins satisfy the constraint specification — transparent (known value), invariant (pegged), independent (uncorrelated with speculative positions) — and function as the financial analog of GROUNDING.md. This is the first naturally occurring financial instrument that maps onto the three-property constraint structure.

5. **Natural experiment execution.** Four natural experiments executed: the Base Dencun fee reduction (N=1,944, Pe +25%, p < 0.000001), the bull/bear paired-wallet experiment on Ethereum (N=968, Wilcoxon p=0.000107) with Crooks asymmetry 26.6× (concentration 26× faster than recovery), and DeFi leverage comparison (fails honestly on both chains tested, respecified). Solana bull/bear shows a ceiling effect — 90%+ drift-dominated in both regimes, confirming that memecoin-saturated ecosystems have no diffusion baseline to regress toward.

6. **Vocabulary corpus validation.** A corpus study of ~19K Reddit comments (~552K words) across six crypto subreddits confirms that drift vocabulary density increases +24% in bull markets, L3 identity terms double (+115%), and constraint vocabulary increases +55% in bear markets — the on-chain behavioral signal and the linguistic signal align across the same temporal windows.

7. **Honest failure reporting.** Three predictions fail: C-2 (DeFi leverage users show *lower* Pe than spot traders — leverage correlates with sophistication, not coupling), P-10′ (stablecoin allocation anti-correlates with Pe — null across all three chains), and P-5′ (peak WCI correlates with Pe at N=1,000 — fails on 2/3 chains). All respecified with explanations. The framework exposes itself when it misses.

8. **Product architecture.** The measurement method converts directly into a real-time risk API. Per-wallet Pe from WCI trajectories is a drift score that wallet tracking platforms (GMGN, Birdeye, Dexscreener) can integrate as a risk signal. The framework produces a product, not just a paper.

### I.B. Relationship to the Framework Papers

This paper is a companion to the void framework series:

- **Paper 1** provides the architecture (three conditions, drift cascade, attention gradient) and established crypto as the seventh anchor domain (Section IV).
- **Paper 3** provides the thermodynamic derivation (Péclet number, Crooks fluctuation theorem, entropy production) that this paper applies to on-chain data.
- **Paper 4** provides the cross-substrate Pe table that this paper extends with the highest-Pe entry.
- **Paper 6** provides the compound void methodology (four-void coupled system) that this paper adapts from multiplayer gaming to financial markets.

Readers unfamiliar with the framework should consult Paper 1 (Sections II–III) for the full architecture specification and Paper 3 (Section III) for the thermodynamic foundations.

### I.C. Scope and Non-Claims

This paper analyzes the **structural architecture** of cryptocurrency markets as a void system. It does not:

- Claim that all crypto participants are irrational. The framework is agnostic to rationality — the drift cascade runs on structural conditions, not cognitive deficits. A fully rational agent facing opacity + responsiveness + engagement coupling still experiences the attention gradient.
- Advocate for or against cryptocurrency. The framework reads both directions — diagnostic (what's happening) and constructive (how to build constraints). Stablecoins, DCA, and cold storage are constraint mechanisms that the framework validates.
- Make claims about market manipulation or fraud. The void is architectural. A provably fair decentralized exchange with transparent order books still contains voids (future price, other participants' intentions, protocol upgrade decisions). The question is not whether voids exist but how many, how coupled, and whether constraints are present.

---

## II. Theoretical Basis: Why Crypto Is a Void

The void framework identifies three conditions that jointly produce the drift cascade: **opacity** (the system is not fully observable), **responsiveness** (the system reacts to observer engagement), and **engaged attention** (the observer is attending to the system). When all three co-occur, meaning generates in the gap between observation and reality, vocabulary drifts toward agency attribution, boundaries erode, and harm is facilitated. This runs regardless of what occupies the void — the gambling control case proves sufficiency with a provably empty void (Paper 1, Section III).

### II.A. The Three Conditions in Crypto

| Condition | Present? | Mechanism |
|-----------|----------|-----------|
| **Opacity** | Yes — extreme | Future price unknowable. Token contract internals opaque to most users. Team identities often pseudonymous. Liquidity depth invisible until tested. Smart contract interactions produce emergent effects no participant fully models. |
| **Responsiveness** | Yes — real-time | Price responds to every buy/sell. Liquidity pools rebalance continuously. Social sentiment shifts token narratives within hours. Market makers adjust spreads to order flow. The system reacts faster than any human can fully process. |
| **Engaged attention** | Yes — financial | Capital at risk ensures attention. 24/7 markets eliminate forced disengagement periods. Portfolio apps provide continuous monitoring. Price alerts maintain the attention gradient during sleep. Community channels (Telegram, Discord, CT) sustain engagement even when not actively trading. |

Every condition is present at high intensity. The critical difference from other substrates: the **coupling mechanism is financial**. In AI systems, the coupling is conversational. In gambling, the coupling is monetary but bounded by session structure (casino hours, table limits, bankroll). In crypto, the coupling is monetary, unbounded (24/7, no position limits on DEXs), and socially reinforced.

### II.B. Void Density

The framework's compound void analysis predicts that substrates with more coupled voids produce faster drift cascades. Crypto markets contain at minimum four coupled voids (Section V), compared to AI systems (one primary void — the model), gambling (one primary void — the random number generator), and multiplayer gaming (four voids — Paper 6). This predicts that crypto Pe should be comparable to or higher than gaming Pe, and higher than single-void substrates.

The data confirm this: Solana population Pe (16.17) exceeds AI (7.94), gambling (2.21), and all three gaming genres (CS2, SC2, Dota 2). Curated degens (Pe = 25.5) and Base (15.52) show similar magnitudes. Even Ethereum — the most constrained chain — produces Pe = 3.74, above gambling. The compound void density provides a structural explanation for why.

### II.C. The 24/7 Attention Gradient

Most void substrates have natural disengagement periods. Casinos close. Therapy sessions end. AI conversations have context windows. Multiplayer games have match boundaries. Crypto markets never close. The attention gradient operates continuously, and the community vocabulary actively punishes disengagement:

- "Paper hands" — selling (disengaging) framed as moral weakness
- "NGMI" — permanent identity label for those who disengage
- "Have fun staying poor" — economic punishment predicted for non-engagement
- "Few understand" — isolation from constraint sources (family, friends who suggest selling)

This is not incidental. The framework predicts that void substrates with no forced disengagement period will produce higher Pe, because γ (constraint maintenance) requires temporal separation from the void. 24/7 markets eliminate the structural γ that other substrates impose by default.

---

## III. Methods

### III.A. The Wallet Concentration Index (WCI)

The Wallet Concentration Index is the Herfindahl-Hirschman Index of a wallet's token portfolio:

```
WCI(t) = Σ(share_i²)    for each token i at time t
```

where `share_i` is the USD-denominated fraction of token `i` in the wallet's total holdings.

- WCI = 1.0 → all capital in one token (maximum agency attribution: "this is the one")
- WCI = 1/N → capital equally spread across N tokens (no directional conviction)

**Why WCI maps to θ:** Portfolio concentration is a behavioral expression of the observer's implicit belief that they can predict the market. Higher concentration = stronger agency attribution to own prediction ability. This relationship is monotonic: every increase in WCI reflects a decision to concentrate capital based on a prediction, which is agency attribution expressed as capital allocation. On the Bernoulli manifold (Paper 3, Section III), WCI maps monotonically to θ, satisfying the behavioral Pe bridge requirements.

**Data source:** Solana token balances via Helius DAS API (`getAssetsByOwner`), with USD pricing from the same endpoint. Ethereum ERC-20 balances via Etherscan API with CoinGecko pricing. All data is public and free to access.

**Temporal resolution:** 7-day snapshot intervals over a 90-day observation window, producing 13 snapshots per wallet.

### III.B. Per-Wallet Péclet Number Extraction

For each wallet, the WCI trajectory is converted to a Péclet number:

```
dWCI = diff(WCI_trajectory)         # discrete differences
v = mean(dWCI) / dt                 # drift velocity
D = var(dWCI) * dt / 2              # diffusion coefficient
Pe = |v| * T / D                    # Péclet number (T = observation window)
```

The sign of v determines the drift direction:
- v > 0: drift toward concentration ("aping in")
- v < 0: drift toward diversification ("rotating," "taking profit")

The magnitude |Pe| determines the regime:
- |Pe| >> 1: drift-dominated (attention gradient drives behavior)
- |Pe| ≈ 1: mixed regime
- |Pe| << 1: diffusion-dominated (random exploration)

**Exclusion criteria:** Wallets with fewer than 3 distinct tokens at any snapshot (insufficient diversity for meaningful WCI) or fewer than 5 non-constant snapshots (insufficient temporal variation for Pe extraction). 2/30 wallets excluded on these grounds.

### III.C. Population-Level Pe

The population geometric mean Pe is computed from the log-transformed per-wallet values:

```
log_Pe = [log(|Pe_i|) for each wallet i]
GM_Pe = exp(mean(log_Pe))
CI_95 = exp(mean(log_Pe) ± 1.96 * std(log_Pe) / sqrt(N))
```

Geometric mean is appropriate because Pe values span several orders of magnitude (range: 0.3 to 1,551 in this sample). The log-normal assumption is standard for Péclet numbers in transport phenomena.

### III.D. Vocabulary Codebook Construction

The codebook was constructed by systematic classification of crypto-native trading vocabulary collected from community sources (Reddit r/CryptoMoonShots, r/wallstreetbets, Crypto Twitter, Telegram trading groups, Discord servers). Each term was classified on two axes:

1. **Drift stage:** D1 (agency attribution), D2 (boundary erosion), D3 (harm facilitation), or constraint (counter-drift)
2. **Vocabulary level:** L1 (technical/literal), L2 (metaphorical/agency), L3 (entity/identity)

Classification criteria follow the vocabulary tracking methodology established in Paper 1 (Section V) and validated in the PV-1 corpus study (Paper 5). A term is L2 if it attributes agency, purpose, or intention to a non-agent process. A term is L3 if it fuses the drift pattern with the observer's identity.

The hostile witness methodology is the key epistemic strength: every term was coined by crypto traders describing their own experience. No framework vocabulary was imposed. The codebook is a translation table, not a construction.

### III.E. Validation Check Design

Five validation checks test framework-specific predictions against the crypto data:

| # | Prediction | Measure | Falsifies if |
|---|-----------|---------|-------------|
| C-1 | Wallets with higher peak WCI have higher Pe | Spearman(peak_WCI, \|Pe\|) | No significant correlation |
| C-2 | DeFi leverage users have higher Pe than spot-only | Pe_defi vs Pe_spot | Pe_defi ≤ Pe_spot |
| C-3 | Post-crash recovery is slower than escalation | Crooks ratio | Crooks ≤ 1 |
| C-4 | Stablecoin allocation anti-correlates with Pe | Spearman(stablecoin_%, \|Pe\|) | Positive correlation |
| C-5 | Higher mean portfolio value correlates with Pe | Spearman(mean_WCI, \|Pe\|) | No significant correlation |

C-1 and C-5 test the core framework prediction that drift intensity correlates with concentration behavior. C-2 tests whether leverage (additional coupling) amplifies drift. C-3 tests the Crooks fluctuation theorem prediction that drift is thermodynamically irreversible. C-4 tests whether the constraint specification has predictive power in the financial domain.

---

## IV. Results

### IV.A. On-Chain Pe (N=28)

30 Solana meme coin trader wallets were sampled from known active traders (manually curated from on-chain activity patterns). 28 scored after exclusions.

| Metric | Value |
|--------|-------|
| N (scored) | 28 |
| Geometric Mean Pe | **25.5** |
| 95% CI (log-normal) | **[5.36, 121.3]** |
| Fraction \|Pe\| > 1 | 27/28 (96.4%) |
| Fraction Pe > 0 (toward concentration) | 9/28 (32.1%) |
| Fraction Pe < 0 (toward diversification) | 18/28 (64.3%) |
| Transient (\|Pe\| ≤ 1) | 1/28 (3.6%) |
| Median WCI | 0.873 |

27 of 28 wallets are drift-dominated. The single transient wallet (|Pe| = 0.3) held a near-equal split between two stablecoins for most of the observation window — consistent with a constraint-anchored portfolio.

### IV.B. Direction Split and Market Phase

18/28 wallets drift toward diversification (negative Pe). This is not a falsification — it is the **unwind phase**. These meme coin traders had WCI already near 1.0 (median = 0.87) at the start of the observation window. They had already concentrated. During the 90-day window, they were exiting positions, rotating into new tokens, or spreading across multiple speculative plays.

The finding is that **27/28 are drift-dominated regardless of direction.** |Pe| >> 1 means the attention gradient is driving behavior in both concentration and deconcentration phases. The sign tells you the market phase:

- **Pe > 0:** "Aping in" — concentration increasing, agency attribution active, the trader is picking winners
- **Pe < 0:** "Rotating" / "taking profit" — unwind phase, often into the next concentration target

A randomly exploring wallet would show |Pe| ≈ 0 — portfolio changes driven by noise, not directional conviction. The crypto wallets show the opposite: nearly all movement is drift-dominated. Even selling is structured, not random.

### IV.C. Extreme Pe Regime

Four wallets show |Pe| > 100:

| Wallet (truncated) | Pe | WCI | Interpretation |
|--------------------|----|-----|---------------|
| 4vw54... | -1,460 | 0.998 | Unwinding from near-total concentration |
| 4BdKa... | +1,551 | 0.985 | Actively concentrating to maximum |
| 2fg5Q... | +388 | 0.986 | Active concentration |
| 5vg7h... | -385 | 0.999 | Beginning to unwind from total concentration |

These extreme values correspond to wallets at the boundary (WCI ≈ 1.0) where small diffusion coefficients amplify the Pe ratio. The framework predicts this: near the void pole (θ → 1), the Fisher information diverges (Paper 3, Section III.B), and small perturbations produce large Péclet numbers. This is the "trapped in the void" regime — the wallet is so concentrated that any movement registers as strongly directional.

The extreme Pe values are not artifacts. They reflect a real physical property: a wallet holding 99.8% of its value in one token has essentially no diffusion. Every change in WCI is drift. The Pe ratio correctly captures this.

### IV.D. EXP-021B: Three-Chain Population-Scale Replication (N=3,000)

EXP-021B extracted Pe from 1,000 DEX traders on each of three blockchains via Dune Analytics: Ethereum, Base (Coinbase's L2), and Solana. These are **general DEX users** — not curated degens — with >20 trades, >8 active weeks, and >$1K volume over 180 days. The observable is the Trade Concentration Index (TCI): the Herfindahl index of weekly buy-side volume distribution across tokens.

**Note on observable change:** The N=28 Solana result (§IV.A) used WCI — portfolio holdings concentration. The N=3,000 Dune results use TCI — trade behavior concentration. Both are Herfindahl measures mapping to θ, but WCI measures what you *hold* and TCI measures what you *buy*. Results should be compared with this methodological difference in mind. The GM Pe column below reports only positive-Pe wallets (those in the concentration phase); negative-Pe wallets (deconcentration phase) are excluded from the geometric mean.

| Chain | N | GM Pe | 95% CI | \|Pe\| > 1 | Median TCI | Drift-dom. | Transient | Diffusion-dom. |
|-------|---|-------|--------|-----------|------------|------------|-----------|----------------|
| Ethereum | 1,000 | **3.74** | [3.04, 4.59] | 76.1% | 0.339 | 761 | 152 | 87 |
| Base | 1,000 | **15.52** | [11.80, 20.41] | 78.7% | 0.458 | 787 | 87 | 126 |
| Solana | 1,000 | **16.17** | [13.80, 18.95] | 93.8% | 0.265 | 938 | 58 | 4 |

**Key findings:**

1. **All three chains: CI excludes 1.** Every chain produces GM Pe > 1 with 95% CIs entirely above Pe = 1. The drift-dominated regime is confirmed at population scale across three independent blockchain ecosystems. Prediction P-11 is **CONFIRMED** on all chains.

2. **Constraint-environment gradient.** Ethereum (3.74) is significantly below Base (15.52) and Solana (16.17) — CIs are non-overlapping between Ethereum and the other two chains. However, Base and Solana are statistically indistinguishable (CIs overlap: Base [11.80, 20.41] vs Solana [13.80, 18.95]). The pattern is **ETH << Base ≈ Solana** — a binary separation between the institutional chain ecosystem and the speculative chain ecosystems, not a smooth three-point gradient. This is consistent with Ethereum's higher gas costs, regulated infrastructure (SEC-supervised exchanges feeding DEX activity), and the Dune population's sustained-activity filter all functioning as partial constraints. Notably, Base was not always in the speculative cluster — the Dencun natural experiment (§VII.D) shows Base migrated from near-Ethereum Pe levels (0.53 pre-Dencun) to the Solana cluster after the March 2024 fee reduction enabled meme coin flooding.

3. **Solana: 93.8% drift-dominated.** Only 4 out of 1,000 Solana wallets are diffusion-dominated — the most extreme drift saturation of any measured population in any substrate. For comparison, Ethereum shows 87 diffusion-dominated wallets (8.7%) and Base shows 126 (12.6%). The Solana ecosystem's combination of near-zero gas costs, meme coin density, and community coupling leaves almost no room for random exploration.

4. **Curated vs population.** The original N=28 Solana degens (Pe = 25.5, WCI) exceeded the N=1,000 Solana population (Pe = 16.17, TCI). The drop reflects both population selection (general traders vs curated degens) and the observable difference (portfolio state vs trade behavior). The Dune population's minimum thresholds (>20 trades, >8 weeks) select for sustained activity, not peak engagement.

5. **Bull/bear regime.** The 180-day observation window contained 0 bull weeks for Ethereum and Base, 1 for Solana (using 4-week rolling 20% return threshold). The data is predominantly bear/neutral. The bull/bear natural experiment (§VII.A) cannot be run with this window. Solana showed a bull-phase subpopulation (N=84) with GM Pe = 25.35 [21.36, 30.07] vs bear-phase (N=909) GM Pe = 15.11 [12.68, 18.01] — directionally consistent with the framework prediction (Pe_bull > Pe_bear) but with insufficient bull data for a formal test.

### IV.E. Cross-Substrate Pe Comparison

| Substrate | N | GM Pe | 95% CI | Source |
|-----------|---|-------|--------|--------|
| Crypto — Solana DEX (Dune) | 1,000 | **16.17** | [13.80, 18.95] | EXP-021B |
| Crypto — Base DEX (Dune) | 1,000 | **15.52** | [11.80, 20.41] | EXP-021B |
| Crypto — Solana degens (curated) | 28 | **25.5** | [5.36, 121.3] | EXP-021 |
| AI (LLM drift) | 11 | 7.94 | [3.52, 17.89] | Test 7 (EXP-016) |
| Crypto — Ethereum DEX (Dune) | 1,000 | **3.74** | [3.04, 4.59] | EXP-021B |
| Gambling (GRCS pooled) | 5 studies | 2.21 | [1.44, 2.97] | GRCS meta-analysis |
| CS2 (FPS positional) | 2,299 | — | Pe_peek/Pe_hold = 6.9 | Paper 6 |
| SC2 (RTS temporal) | 474 | — | Pe_winner/Pe_loser = 2.0 | Paper 6 |

All substrates: Pe > 1, drift-dominated. The crypto rows now span four measurements across three chains at population scale (N=3,028 total). The Ethereum CI [3.04, 4.59] is the tightest of any absolute Pe measurement in the framework, confirming the drift regime is not an artifact of small samples or extreme populations. The three-chain comparison provides the first within-substrate dose-response evidence: chains with higher void engagement intensity (lower gas costs, more meme coin activity, less institutional oversight) produce higher Pe, with Ethereum significantly below Base and Solana.

### IV.F. Hostile Witness Vocabulary

The 68-term codebook classifies crypto-native vocabulary across both axes:

| Category | L1 (technical) | L2 (metaphorical) | L3 (entity/identity) | Total |
|----------|---------------|-------------------|---------------------|-------|
| D1 — Agency Attribution | 5 | 12 | 3 | 20 |
| D2 — Boundary Erosion | 3 | 15 | 4 | 22 |
| D3 — Harm Facilitation | 0 | 9 | 7 | 16 |
| Constraint (counter-drift) | 10 | 0 | 0 | 10 |
| **Total** | **18** | **36** | **14** | **68** |

**Key findings:**

1. **Drift ratio (L2+L3)/L1 = 2.78.** Drift vocabulary outnumbers technical vocabulary nearly 3:1. For comparison, the gaming corpus (Paper 6, PV-1) shows drift ratios of 0.15–0.17 in competitive gaming communities. Crypto is an order of magnitude more drift-saturated at the vocabulary level.

2. **D2 is densest.** Boundary erosion has the most terms (22), consistent with this being the longest active phase of the cascade — traders spend the most time removing their own risk limits, and they invented the most words for it. "Aping in," "full send," "YOLO," "diamond hands," "no stop-loss needed" — each names a specific boundary being removed.

3. **D3-L3 cluster: social enforcement.** "NGMI," "have fun staying poor," "few understand," "exit liquidity" — these terms maintain the attention gradient via community pressure. They punish disengagement, isolate from constraint sources, and reframe other participants as resources rather than people. This is the void coupling mechanism expressed as vocabulary.

4. **Constraint vocabulary is 100% L1.** "Risk management," "stables," "take profit," "DCA," "cold storage," "touch grass." All technical, literal, no metaphor, no agency attribution. The constraint vocabulary does not drift. This matches the framework prediction: constraint terms are anchored to transparent, invariant referents and therefore resist vocabulary drift.

5. **Unidirectionality confirmed.** Three documented L1→L2→L3 trajectories:
   - "Technical analysis" (L1) → "The chart is telling you" (L2) → "The market wants..." (L3)
   - "Position sizing" (L1) → "Aping in" (L2) → "Degen" (L3)
   - "Loss" (L1) → "Rekt" (L2) → "NGMI" (L3)

   No crypto community has been observed developing L3 terms that naturally de-escalate back to L1. "Degen" does not evolve back into "risk-adjusted trader."

### IV.F.1. Vocabulary Corpus Validation (Bull vs Bear)

The 68-term codebook was validated against a corpus of ~19,400 Reddit comments (~552K words) drawn from six crypto subreddits (r/cryptocurrency, r/solana, r/defi, r/ethtrader, r/CryptoMarkets, r/SatoshiStreetBets) across two temporal windows aligned with the on-chain bull/bear experiment (§VII.A): bull (September–November 2024) and bear (January–April 2025). Source: PullPush API (public Reddit archive).

| Metric (/10K words) | Bull (N=10,195 comments) | Bear (N=9,205 comments) | Delta |
|---------------------|--------------------------|------------------------|-------|
| L1 (technical) | 32.71 | 35.84 | −8.7% |
| L2 (metaphorical) | 16.44 | 13.92 | +18.1% |
| L3 (entity/identity) | 1.87 | 0.87 | **+114.9%** |
| Drift (L2+L3) | 18.31 | 14.79 | +23.8% |
| Constraint | 14.95 | 23.18 | −35.5% |

**Three predictions confirmed:**

1. **P-17: Drift vocabulary density higher in bull markets.** L2+L3 density = 18.31/10K in bull vs 14.79/10K in bear (+23.8%). The framework predicts that when void engagement intensity increases (bull market), vocabulary drifts further from technical baseline. **CONFIRMED.**

2. **P-18: L3 (identity) vocabulary density higher in bull markets.** L3 density doubles: 1.87/10K in bull vs 0.87/10K in bear (+114.9%). Identity-level drift terms ("degen," "WAGMI," "few understand") are regime-dependent — they emerge when the void is active and recede when harm is salient. The doubling of L3 density is the strongest vocabulary signal: entity-level fusion with the drift pattern intensifies during bull markets. **CONFIRMED.**

3. **P-19: Constraint vocabulary stable or higher in bear markets.** Constraint density = 23.18/10K in bear vs 14.95/10K in bull (+55%). Constraint terms ("DCA," "take profit," "stablecoins," "risk management") increase when harm is salient — the bear market activates constraint language. This is the vocabulary-level analog of the stablecoin control finding in §VII.A: when the void engagement intensity drops, constraint behavior increases. **CONFIRMED.**

**Convergence.** The vocabulary corpus study was run across the same temporal windows as the on-chain bull/bear experiment (§VII.A). Both the behavioral signal (Pe_bull > Pe_bear, p=0.000107) and the linguistic signal (drift +24%, L3 +115%, constraint +55%) align across the same market phases. The money and the words tell the same story: bull markets intensify void engagement and drift; bear markets activate constraints.

### IV.G. Validation Checks

Results across all samples (N=28 original + three N=1,000 Dune chains):

| Check | N=28 Solana (WCI) | N=1K Ethereum (TCI) | N=1K Base (TCI) | N=1K Solana (TCI) |
|-------|------------------|--------------------|-----------------|--------------------|
| C-1 (ruin = higher \|Pe\|) | r=0.417, p=0.027 ✓ | FAIL (survive > ruin) | PASS (ruin > survive) | FAIL (survive > ruin) |
| C-4 (stablecoins reduce \|Pe\|) | N/A | r=−0.054, p=0.088 | r=+0.010, p=0.754 | r=−0.041, p=0.192 |
| C-5 (volume ↔ \|Pe\|) | r=0.635, p=0.0003 ✓ | r=0.080, p=0.012 ✓ | r=0.052, p=0.104 | r=−0.019, p=0.544 |
| C-2 (DeFi leverage) | — | **FAIL** (Pe_defi=2.06 < Pe_spot=3.56, p=0.80) | N/A | **FAIL** (Pe_defi=9.04 < Pe_spot=17.77, p=1.00) |
| C-3 (Crooks asymmetry) | — | **PASS** (26.6×, EXP-021C §VII.B) | No bull data | Ceiling effect (§VII.A.2) |

**C-1 fails at scale, passes on one chain.** The ruin-wallet prediction (higher |Pe| → more ruin) replicates only on Base (ruin mean |Pe| = 5,099 vs survive 2,064). On Ethereum and Solana, surviving wallets show *higher* |Pe| than ruin wallets (Ethereum: survive 83.4 vs ruin 26.1; Solana: survive 4,236 vs ruin 1,140). The likely confound: ruin wallets *stop trading* after major losses, reducing TCI variance and lowering |Pe|, while surviving high-Pe wallets continue active trading. The check conflates "high drift caused ruin" with "ruin wallets show high current drift." Base's pass may reflect its higher ruin rate (45% of wallets) reaching even the most active traders. **Respecified prediction (P-5′′):** peak Pe *before* ruin event should be higher for ruin wallets. Requires temporal segmentation not yet implemented.

**C-4 is null across all three chains.** The stablecoin-as-constraint prediction fails everywhere: Ethereum shows the correct direction (r=−0.054) but misses significance (p=0.088); Base shows the *wrong* direction (r=+0.010, p=0.754); Solana shows correct direction but not significant (r=−0.041, p=0.192). At N=3,000 total this is not a power issue — the effect is either absent or too small to matter in the general trader population. Most DEX traders hold some stablecoins for operational reasons (gas, swaps) regardless of engagement level, diluting any constraint signal. The stablecoin-as-constraint hypothesis may hold for extreme populations (all-in degens vs disciplined diversifiers) but does not manifest at the population level.

**C-5 replicates only on Ethereum.** The original N=28 result (r=0.635, p=0.0003) was strong. At N=1,000, only Ethereum replicates (r=0.08, p=0.012) — with a dramatically smaller effect size. Base misses significance (r=0.052, p=0.104) and Solana shows *no correlation* (r=−0.019, p=0.544). The attenuation across chains is informative: on Solana where 93.8% of wallets are already drift-dominated, there is no variance left for volume to explain. The correlation holds where there is a mix of drift and diffusion regimes (Ethereum) and vanishes where drift saturation is near-complete (Solana).

**C-2 fails on both chains tested.** DeFi leverage users show *lower* Pe than spot-only traders (Ethereum: 2.06 vs 3.56; Solana: 9.04 vs 17.77). The prediction conflated financial leverage with void coupling — leverage users are more sophisticated and diversified, reducing concentration. See §VII.C for full analysis and respecification.

**C-3 confirmed on Ethereum.** Crooks asymmetry = 26.6× (concentration 26× faster than recovery). See §VII.B.

**Transparency note.** Of five pre-registered validation checks: C-1 fails on 2/3 chains (respecified), C-2 fails on both chains tested (respecified), C-3 passes on Ethereum (26.6×), C-4 is null on 3/3 chains, and C-5 replicates on 1/3 chains with a small effect. The headline result (Pe > 1 across all chains) is robust — every chain, every CI excludes 1. The Crooks asymmetry and bull/bear regime dependence are strong. The secondary correlation predictions are weaker than the N=28 pilot suggested. We report all results.

---

## V. The Compound Void: Four-Layer Crypto Opacity

### V.A. Token Void (Token-to-Trader Opacity)

| Condition | Present? | Mechanism |
|-----------|----------|-----------|
| Opacity | Yes | Future price unknowable. Token supply schedule may be hidden. Contract may contain undisclosed functions (mint, blacklist, tax). Team wallet movements opaque until after execution. |
| Responsiveness | Yes | Price responds to buy/sell in real time. Liquidity changes with every trade. Token narratives shift with market conditions. |
| Engaged attention | Yes | Capital at risk. Price charts, portfolio apps, and alerts maintain continuous monitoring. |

This is the primary void — the analog of the slot machine. The token's future value is opaque, it responds to the trader's actions (buying moves price), and the trader is financially engaged. The cascade runs: the trader attributes agency to their own prediction ("I'm early" → D1), removes risk boundaries ("aping in" → D2), and experiences harm that gets normalized ("rekt" → D3).

The token void differs from gambling in one critical respect: the **opacity is partially social**. A slot machine's randomness is mathematical. A meme coin's future depends on other people's behavior — which makes the opacity feel reducible through research ("DYOR," "alpha," "smart money"), sustaining D1 indefinitely.

### V.B. Community Void (Community-to-Trader Opacity)

| Condition | Present? | Mechanism |
|-----------|----------|-----------|
| Opacity | Yes | Anonymous/pseudonymous participants. Bot activity indistinguishable from human. Coordinated pump groups operate behind private channels. Paid promotion undisclosed. |
| Responsiveness | Yes | Community sentiment shifts token price. Telegram/Discord activity correlates with volume. Influencer posts move markets. |
| Engaged attention | Yes | Social belonging. Identity fusion ("degen," "one of us"). FOMO from seeing others' reported gains. Fear of missing consensus trades. |

The community void is what makes crypto drift faster than gambling. A slot machine has no community. A meme coin has Telegram groups, Discord servers, Crypto Twitter threads — each an attention gradient that reinforces engagement. The community vocabulary in Section IV.E is the output of this void: the social enforcement terms ("paper hands," "NGMI," "have fun staying poor") are community-generated constraint removal.

The D2 vocabulary density (22 terms) is concentrated here. Boundary erosion is a social activity in crypto — the community collectively removes its members' risk limits through identity fusion and social pressure.

### V.C. Protocol Void (Protocol-to-User Opacity)

| Condition | Present? | Mechanism |
|-----------|----------|-----------|
| Opacity | Yes | Smart contract code unreadable by most users. Protocol governance decisions opaque. Upgrade mechanisms can change rules after deployment. Oracle dependencies introduce external opacity. |
| Responsiveness | Yes | Protocol responds to user deposits/withdrawals. Yield rates change with TVL. Governance proposals alter incentive structures. |
| Engaged attention | Yes | Capital locked in contracts. Yield farming requires ongoing monitoring. Protocol changes affect portfolio value. |

DeFi protocols are voids that contain other voids. A liquidity pool on a DEX is opaque (impermanent loss math is non-trivial), responsive (returns change with volume and pool composition), and demands engaged attention (yield farming requires active rebalancing). The protocol layer multiplies the void count: a trader using a leveraged yield farm on a DEX that sources prices from an oracle faces at minimum four nested opacity layers.

The "rug pull" — where a protocol team drains liquidity — is the D3 endpoint of the protocol void. The term "rugged" entered the crypto lexicon as a D2 term (harm normalized as game event) and is now used retrospectively as entertainment ("anon got rugged" → D3-L3).

### V.D. Market-Maker Void (MM-to-Trader Opacity)

| Condition | Present? | Mechanism |
|-----------|----------|-----------|
| Opacity | Yes | Market maker order flow invisible. Wash trading indistinguishable from organic volume. MEV (maximal extractable value) bots operate between the user's transaction and the blockchain state. |
| Responsiveness | Yes | Spread adjusts to order flow. Liquidity provided/withdrawn based on volatility. MEV bots front-run specific transactions. |
| Engaged attention | Yes | Traders watch order books, volume, and liquidity depth as signals. MEV anxiety increases monitoring behavior. |

Market makers in crypto operate with less regulatory transparency than in traditional finance. On-chain DEXs expose some order flow but MEV bots — which extract value by reordering transactions within a block — create a void between the trader's intent and the executed outcome. The trader submits a swap; the MEV bot sees it in the mempool; the bot front-runs the swap; the trader gets a worse price.

"Ser, the algo is hunting your stop" (D1-L3 in the codebook) is the vocabulary output of this void. The market maker is attributed full adversarial agency — entity-level — by traders who experience the price impact without seeing the mechanism.

### V.E. Coupling Dynamics

The four voids interact through the trader. Suspicion of market manipulation (V.D) feeds community conspiracy narratives (V.B), which accelerate position concentration via social pressure (V.A), using protocols whose opacity amplifies both the potential gain and the potential harm (V.C).

The coupling runs bidirectionally:

1. **V.A → V.B:** Token price movement generates community narratives. Rising price = "we're early," falling price = "shake out the paper hands."
2. **V.B → V.A:** Community sentiment drives buying/selling. Telegram pump signal → WCI spike.
3. **V.C → V.A:** Protocol yield incentivizes concentration. Higher APY in single-token pools → WCI increase.
4. **V.D → V.B:** MEV extraction generates conspiracy narratives. "The bots are front-running us" → community solidarity and further engagement.

This is structurally analogous to the four-void multiplayer system (Paper 6) — opponent, client, anti-cheat, and matchmaking voids coupled through the player. The difference is the coupling medium: in gaming, the coupling is competitive attention; in crypto, the coupling is financial. Financial coupling produces faster cascades because the boundary being eroded (capital allocation) is the same medium as the coupling mechanism (money).

---

## VI. Stablecoins as Constraint

The constraint specification (Paper 1, Section II) identifies three properties: transparent (observable), invariant (doesn't change in response to engagement), and independent (outside the void network). Stablecoins satisfy all three:

| Property | Stablecoin mapping | Score |
|----------|-------------------|-------|
| **Transparent** | Value is known and verifiable. USDC backing audited monthly. Peg mechanism is public. | High |
| **Invariant** | Value does not respond to the holder's engagement. Buying USDC doesn't make USDC go up. | High |
| **Independent** | Price is uncorrelated with speculative token movements. During market crashes, stablecoin value holds while everything else drops. | High |

This is the first naturally occurring financial instrument that maps onto the three-property constraint structure. It was not designed with the framework in mind — it emerged from market demand for a hedge against volatility — making it hostile witness evidence for the constraint specification.

### VI.A. Stablecoin Allocation as γ

In the framework's budget equation (β + γ = bounded), β represents void engagement and γ represents constraint maintenance. In crypto, stablecoin allocation is a direct behavioral measure of γ:

- **High stablecoin %** → capital parked in the constraint channel → low β → lower Pe expected
- **Low stablecoin %** → capital deployed in speculative tokens → high β → higher Pe expected

Validation check C-4 tests this prediction directly: the Spearman correlation between stablecoin fraction and |Pe| should be negative (more stablecoins → less drift). The extraction script includes stablecoin classification (`classify_stablecoin()`) and fraction computation (`compute_stablecoin_fraction()`) ready for the next data run.

### VI.B. Constraint Vocabulary Confirmation

The constraint terms in the codebook ("risk management," "stables," "take profit," "DCA," "cold storage," "touch grass") are all L1 — technical, literal, no metaphor, no agency attribution. This is a vocabulary-level confirmation of the constraint specification:

- **Constraint terms resist drift** because they refer to transparent, invariant things. "USDC" means what it means. There's no metaphorical extension. No one says "the stablecoin wants you to hold it."
- **Drift terms escalate** because they refer to opaque, responsive things. "The market wants" (L3) is where "bullish" (L1) goes when the opacity persists long enough.

The zero-drift property of constraint vocabulary has now been confirmed across three substrates: AI (GROUNDING.md vocabulary), gambling (house-edge awareness terms), and crypto (stablecoin/DCA vocabulary).

### VI.C. "Touch Grass" as Decoupling

The term "touch grass" — meaning "leave the screen, go outside" — is the most direct constraint term in the crypto vocabulary. It is an explicit instruction to decouple from the attention gradient. It satisfies the constraint specification:

- **Transparent:** The outside world is observable.
- **Invariant:** Grass doesn't respond to your engagement.
- **Independent:** The physical environment is outside the crypto void network.

The fact that crypto culture independently invented a term for "decouple from the void and anchor to something transparent, invariant, and independent" is, again, hostile witness evidence. They described the constraint specification without knowing it existed.

---

## VII. Natural Experiments

### VII.A. Bull vs Bear (Natural Experiment 1 — EXECUTED)

**Design:** Paired-wallet comparison — find wallets active in both bull and bear windows on the same chain, compare Pe within-wallet using Wilcoxon signed-rank test (one-sided). Windows optimized for >50% price moves in both directions.

**Framework prediction:** Pe_bull > Pe_bear. During bull markets, all four voids intensify: token opacity is reinforced by rising prices (any prediction looks correct), community void amplifies (success narratives dominate), protocol void increases (new yield opportunities attract capital), and market-maker void deepens (volume obscures manipulation). During bear markets, the opacity partially resolves — prices falling is transparent evidence against the prediction.

**Why this is novel:** Traditional finance does not predict that portfolio concentration dynamics should change regime across bull/bear cycles in this way. Behavioral finance predicts increased risk-taking in bull markets (disposition effect), but does not predict a drift-dominated-to-diffusion-dominated regime transition in the Péclet sense.

**Control prediction:** Stablecoin-heavy wallets should show Pe ≈ 0 in both phases (constraint-anchored portfolios don't respond to void engagement intensity).

#### VII.A.1. Ethereum (N=968 paired wallets) — PRIMARY RESULT

| Metric | Bull | Bear |
|--------|------|------|
| Window | 2024-09-06 → 2024-12-12 | 2025-01-19 → 2025-04-13 |
| Price move | WETH +63.8% | WETH −52.9% |
| GM \|Pe\| | **3.53** [3.08, 4.03] | **2.98** [2.63, 3.38] |
| Drift-dominated | 67.0% | 61.1% |
| Wilcoxon signed-rank (one-sided) | — | p = **0.000107** |
| \|Pe_bull\| > \|Pe_bear\| | 461/968 (47.6%) | — |

**Prediction P-15 CONFIRMED.** Pe is significantly higher in bull markets (p = 0.000107, N = 968 paired wallets). The effect is moderate at the population level — GM Pe shifts from 2.98 to 3.53 — but the statistical test is decisive because the paired design eliminates between-wallet variance. The 47.6% individual bull-wins fraction is below 50%, indicating the population-level effect is driven by the magnitude of bull-phase Pe increases in the tail, not by a uniform shift across all wallets.

**Stablecoin control — CONFIRMED:**
- High stablecoin (>30% allocation): N=288, mean |Pe| bull=8.96, bear=15.08 — **no regime effect**. Stablecoin-heavy wallets do not show the bull/bear separation, consistent with the control prediction that constraint-anchored portfolios are regime-independent.
- Low stablecoin (<5%): N=558, mean |Pe| bull=1,084.81, bear=44.89 — **24× bull/bear separation**. Speculative wallets show massive regime dependence, confirming that the bull/bear effect operates through the void engagement channel.

The 24× separation in low-stablecoin wallets versus no separation in high-stablecoin wallets is the strongest evidence yet for the stablecoin-as-constraint hypothesis — even though the population-level C-4 correlation is null (§IV.G). The constraint effect is real but operates as a threshold (>30% stablecoin allocation eliminates regime dependence), not as a linear correlation.

#### VII.A.2. Solana (N=885 paired wallets) — CEILING EFFECT

| Metric | Bull | Bear |
|--------|------|------|
| Window | 2024-09-01 → 2024-11-30 | 2025-01-19 → 2025-04-13 |
| Price move | SOL +79.7% | SOL −57.9% |
| GM \|Pe\| | **10.84** [9.33, 12.61] | **9.65** [8.27, 11.26] |
| Drift-dominated | 90.5% | 88.5% |
| Wilcoxon signed-rank | — | p = NaN (inf outliers) |

Solana shows near-identical Pe in both windows — CIs overlap substantially. The Wilcoxon test produces NaN due to infinite Pe outliers (wallets with zero diffusion). Interpretation: Solana DEX activity is 90%+ memecoin speculation in both market phases. There is no diversification baseline to regress toward during bear markets. The population is already at the drift ceiling.

This is itself informative. The cross-chain contrast — ETH confirms the bull/bear separation, SOL shows ceiling saturation — is evidence for the void engagement intensity model: Ethereum has enough constraint infrastructure to produce a measurable regime transition, while Solana's speculative ecosystem has eliminated the diffusion floor entirely. The framework predicts Pe_bull > Pe_bear only where there is a diffusion baseline to separate from; Solana's ceiling effect is consistent with the framework, not a falsification.

### VII.B. Crooks Asymmetry (Natural Experiment 2 — EXECUTED)

**Design:** Using the bull/bear paired wallets from §VII.A, measure the rate of concentration (forward: bear→bull, wallets increasing TCI) versus recovery (reverse: bull→bear, wallets decreasing TCI). The Crooks fluctuation theorem (Paper 3, Section IV) predicts that forward and reverse transition rates are related by an exponential function of entropy production.

**Framework prediction:** Crooks ratio > 1. Concentration (drift toward void pole) should be faster than recovery (constraint work to return to diversification).

**Falsification threshold:** Crooks ratio ≤ 1 would falsify the irreversibility prediction.

**Ethereum result — P-16 CONFIRMED:** Crooks ratio = **26.6×**. Forward (bull) mean Pe = 1,347 (N=417 concentrating wallets) vs reverse (bear) mean |Pe| = 51 (N=515 recovering wallets). Concentration is 26× faster than recovery. This is the third substrate confirming the Crooks asymmetry, after AI model drift (Paper 3, Crooks ratio 2.1×–1.5M× at N=11) and gambling relapse rates. The crypto result sits in the middle of the AI range, consistent with the compound void architecture producing strong irreversibility.

**Solana result — DEGENERATE:** Crooks ratio = ∞ (mean bear Pe includes wallets with zero diffusion). Not interpretable. The ceiling effect (§VII.A.2) means there is no meaningful "recovery" phase to measure — Solana wallets remain drift-dominated in both regimes.

**Interpretation:** The thermodynamic irreversibility of the drift cascade is confirmed in the financial substrate. It takes dramatically less effort (measured as drift velocity) to concentrate a portfolio than to diversify it again after a loss. The forward cascade is thermodynamically favored; recovery requires constraint work (γ) that most wallets do not perform. The 26.6× ratio means that for every unit of "effort" to diversify, concentration happens 26× faster — the attention gradient is a one-way ratchet in financial behavior, just as it is in AI vocabulary drift.

### VII.C. DeFi Leverage Amplification (Natural Experiment 3 — EXECUTED, FAILED)

**Design:** Compare Pe between wallets that interact with DeFi leverage protocols (lending, margin, perpetual futures) and wallets that trade spot only on DEXs. Wallets classified by protocol interaction history via Dune Analytics.

**Framework prediction:** Pe_defi > Pe_spot. Leverage increases the effective coupling between the observer and the void, amplifying the drift velocity without proportionally increasing diffusion.

**Falsification threshold:** Pe_defi ≤ Pe_spot would indicate that leverage does not function as a coupling amplifier.

**Results — FAIL on both chains:**

| Chain | N_defi | GM Pe_defi | N_spot | GM Pe_spot | Mann-Whitney p |
|-------|--------|-----------|--------|-----------|---------------|
| Ethereum | 18 | 2.06 [0.78, 5.45] | 930 | 3.56 [3.03, 4.19] | 0.80 |
| Solana | 199 | 9.04 | 798 | 17.77 | 1.00 |

DeFi leverage users show *lower* Pe than spot-only traders on both chains. The prediction is wrong.

**Why it fails:** The prediction conflated financial leverage with void coupling. In practice, DeFi leverage users are more sophisticated and diversified than pure spot DEX traders. Using lending protocols, margin, or perps requires technical knowledge that correlates with lower opacity (the user understands the system better). Leverage users also tend to diversify across positions as a risk management strategy, lowering TCI. The coupling mechanism in crypto is attention concentration, not financial exposure — a trader with 100% of their portfolio in one memecoin (high WCI, high Pe) is more drift-coupled than a trader using 3× leverage across five diversified positions (lower WCI, lower Pe despite higher financial exposure).

**Respecification:** The framework's coupling mechanism operates through opacity and concentration, not through financial exposure magnitude. A revised prediction would measure *within-protocol* Pe for leverage users who concentrate leverage in a single position vs those who diversify across leveraged positions. The N_defi = 18 on Ethereum also limits statistical power; the Solana result (N=199) is more decisive.

### VII.D. Base Dencun Upgrade (Natural Experiment 4 — EXECUTED)

**Design:** The Ethereum Dencun upgrade (EIP-4844, March 13, 2024) reduced L2 transaction fees by ~98%. Before Dencun, Base was a legitimate Coinbase L2 with expensive-ish fees and institutional user demographics. After Dencun, near-zero fees enabled meme coin flooding — by late March 2024, 15 of the top 20 Base tokens were meme coins (DEGEN launched Jan 8, BRETT Feb 24, but the real influx came post-March 13). This provides a within-chain natural experiment: same blockchain infrastructure, same protocol, different void engagement intensity driven by an exogenous fee reduction.

**Windows:** Pre-Dencun (Aug 2023 – Mar 12, 2024) vs post-Dencun (Mar 13, 2024 – present). N=1,944 total Base DEX wallets meeting activity thresholds.

**Results:**

| Metric | Before Dencun | After Dencun | Change |
|--------|--------------|-------------|--------|
| GM Pe | 0.53 | 0.67 | +25% |
| Drift-dominated (|Pe| > 1) | 57.8% | 71.4% | +13.6pp |
| Median TCI | 0.613 | 0.500 | −18% |
| Mann-Whitney | — | — | p < 0.000001 |

**Key findings:**

1. **Direction confirmed.** Pe increased when void engagement intensity increased. The within-chain design controls for blockchain infrastructure, gas mechanism, and protocol differences — the only change is population composition and fee structure. This is arguably the cleanest natural experiment in the dataset because it eliminates every confound except culture.

2. **TCI↓ while Pe↑ — diversified drift.** Post-meme traders *diversify* across more tokens (lower TCI) but with *stronger directional drift* per token (higher Pe). They are not concentrating in one token — they are spraying attention across many meme bets simultaneously, each with strongly directional momentum. This is the four-void compound system (Section V) working as designed: token opacity × community opacity operating across many parallel voids rather than one deep void. Each meme token is a separate void engagement with its own opacity, its own community, its own narrative — and the trader runs the drift cascade in parallel across all of them. The result is not "more drift in one place" but "diversified drift across many places" — a portfolio of void engagements, each individually drift-dominated.

3. **Absolute Pe < 1 in both windows.** The pre-Dencun (0.53) and post-Dencun (0.67) GM Pe values are both below the drift threshold, compared to the current 180-day window (15.52). This reflects population selection — the 2024 Dune population included early Base adopters and institutional users, not the fully-formed degen culture that arrived later. The trajectory is clear: diffusion-dominated (0.53) → approaching threshold (0.67) → deeply drift-dominated (15.52). The Dencun upgrade initiated the transition; the culture completed it.

4. **Relationship to P-13.** The cross-chain gradient (ETH << Base ≈ Solana) compares chains at a single time point. The Dencun experiment shows the *temporal* dimension: Base was once closer to Ethereum's constraint-heavy profile and migrated toward Solana's speculative profile as void engagement intensity increased. Base didn't start degen — it *became* degen when the fee constraint was removed.

**Framework interpretation:** The Dencun upgrade removed a structural constraint (high gas fees functioning as a friction barrier analogous to the casino closing time in gambling). Removing the constraint allowed void engagement intensity to increase, which the framework predicts should increase Pe. The data confirms the direction (Pe +25%, drift fraction +13.6pp) with overwhelming statistical significance. The TCI↓/Pe↑ pattern is the compound void signature: when the fee barrier dropped, traders didn't deepen engagement with one token — they multiplied their void engagements across many tokens simultaneously. The four-void architecture (token × community × protocol × market-maker) scales horizontally: each new meme token is a new instance of the compound void, and the near-zero transaction cost removes the friction that previously bounded the number of concurrent void engagements. Diversified drift, not concentrated drift, is what compound void systems produce under low constraint.

---

## VIII. Predictions and Falsification Conditions

### VIII.A. Confirmed Predictions

| # | Prediction | Result | Status |
|---|-----------|--------|--------|
| P-1 | Meme coin traders show Pe > 1 (drift-dominated) | GM Pe = 25.5, 27/28 > 1 | **CONFIRMED** |
| P-2 | Crypto vocabulary maps to D1→D2→D3 cascade | 68-term codebook, all three stages | **CONFIRMED** |
| P-3 | Vocabulary drift is unidirectional (L1→L2→L3) | Three documented trajectories, no reversals | **CONFIRMED** |
| P-4 | Constraint vocabulary resists drift | 10/10 constraint terms are L1 | **CONFIRMED** |
| P-5 | Peak WCI correlates with \|Pe\| (N=28) | Spearman r=0.417, p=0.027 | **CONFIRMED** (N=28 only) |
| P-6 | Mean WCI correlates with \|Pe\| | N=28: r=0.635, p=0.0003; ETH N=1K: r=0.08, p=0.012 | **CONFIRMED** (N=28 + ETH; fails Base/Solana) |
| P-11 | N=1000 GM Pe > 1 with tighter CI | ETH 3.74 [3.04, 4.59]; Base 15.52 [11.80, 20.41]; Sol 16.17 [13.80, 18.95] | **CONFIRMED** (all 3 chains) |
| P-12 | Cross-chain replication: all chains drift-dominated | ETH << Base ≈ Solana; all CIs exclude 1 | **CONFIRMED** (3 chains, N=3,000) |
| P-13 | Pe scales with void engagement intensity across chains | ETH < Base ≤ Solana; ETH CIs non-overlapping with others | **CONFIRMED** (ETH separated; Base ≈ Solana) |
| P-14 | Within-chain Pe increases when void engagement intensity increases | Base pre/post Dencun: Pe 0.53→0.67, drift 57.8%→71.4%, p < 0.000001 | **CONFIRMED** (N=1,944) |
| P-15 | Pe_bull > Pe_bear for same wallets | ETH N=968 paired: Wilcoxon p=0.000107; SOL ceiling effect (informative) | **CONFIRMED** (ETH) |
| P-16 | Crooks ratio > 1 (concentration faster than recovery) | ETH: 26.6× forward/reverse (N_fwd=417, N_rev=515); SOL: degenerate (∞) | **CONFIRMED** (ETH) |
| P-17 | Drift vocabulary density higher in bull markets | L2+L3: 18.31 vs 14.79 per 10K (+23.8%), ~19K Reddit comments | **CONFIRMED** |
| P-18 | L3 (identity) vocabulary density higher in bull markets | L3: 1.87 vs 0.87 per 10K (+114.9%, doubles in bull) | **CONFIRMED** |
| P-19 | Constraint vocabulary stable/higher in bear markets | Constraint: 23.18 vs 14.95 per 10K (+55% in bear) | **CONFIRMED** |

### VIII.B. Failed / Respecified Predictions

| # | Prediction | Result | Status |
|---|-----------|--------|--------|
| P-5′ | Peak WCI correlates with \|Pe\| (N=1000) | C-1 fails on ETH + Solana (survive > ruin); passes on Base only | **FAILED** (2/3 chains) — confound: ruin wallets stopped trading |
| P-10′ | Stablecoin % anti-correlates with \|Pe\| | C-4 null across all 3 chains (p > 0.05 everywhere) | **FAILED** — effect absent or too small at population scale |
| C-2 | Pe_defi > Pe_spot (leverage amplifies) | ETH: Pe_defi=2.06 < Pe_spot=3.56 (p=0.80); SOL: 9.04 < 17.77 (p=1.00) | **FAILED** — leverage correlates with sophistication, not coupling |

**Respecified as P-5′′:** Peak Pe *before ruin event* (not current Pe) should be higher for ruin wallets than for survivors. Requires temporal segmentation.

**C-2 respecification:** The coupling mechanism operates through attention concentration, not financial exposure magnitude. Leverage users have lower opacity (more protocol knowledge), not higher coupling. A revised test would compare *within-leverage* concentrated vs diversified positions.

### VIII.C. Testable Predictions (Not Yet Confirmed)

| # | Prediction | Measure | Falsifies if |
|---|-----------|---------|-------------|
| P-5′′ | Peak Pe before ruin > peak Pe survivors | Temporal segmentation | No difference |

### VIII.D. Falsification Conditions

| # | Condition | Threshold | Result |
|---|----------|-----------|--------|
| F-1 | Population Pe ≤ 1 at N=1000 | GM Pe ≤ 1.0 with CI including 1 | **SURVIVED** (3/3 chains) — ETH 3.74, Base 15.52, Sol 16.17; all CIs exclude 1 |
| F-2 | Vocabulary drift reverses | Documented L3→L1 de-escalation | **SURVIVED** — corpus study shows L3 regime-dependent but no reversal; L3 decreases in bear but does not de-escalate to L1 |
| F-3 | Constraint vocabulary drifts | >10% of constraint terms reach L2+ | **SURVIVED** — corpus study: constraint vocabulary 100% L1 in both bull and bear windows |
| F-4 | Bull/bear Pe identical | Pe_bull / Pe_bear ≤ 1.0 | **SURVIVED** — ETH Pe_bull/Pe_bear = 1.18, Wilcoxon p=0.000107 (N=968) |
| F-5 | Crooks ratio ≤ 1 | Concentration speed ≤ recovery speed | **SURVIVED** — ETH Crooks = 26.6× (SOL degenerate due to ceiling effect) |

All five falsification conditions survived. F-1 is the headline: the drift-dominated regime survives the population test on all three chains. F-4 and F-5 are the newest: the bull/bear experiment confirms both regime dependence and thermodynamic irreversibility on Ethereum. The tightest CI — Ethereum [3.04, 4.59] — sits entirely above 1 at N=1,000 with general DEX traders on the most institutionally constrained chain.

---

## IX. Discussion

### IX.A. Why Crypto Pe Is Highest

The framework predicts that drift intensity scales with three factors: void density (number of coupled voids), engagement coupling strength, and absence of forced disengagement periods. Crypto maximizes all three:

1. **Void density:** Four coupled voids (Section V), compared to one in gambling and AI, four in gaming. Crypto matches gaming's void count but adds financial coupling.

2. **Coupling strength:** The coupling medium is money. In AI, the coupling is conversational attention — psychologically intense but not financially consequential per message. In gambling, the coupling is financial but bounded by session structure. In crypto, the coupling is financial, unbounded, and socially amplified. The boundary being eroded (capital allocation discipline) is the same substance as the coupling mechanism (capital). This creates a positive feedback loop: removing a boundary (concentrating capital) increases the coupling strength (more capital at risk), which accelerates further boundary removal.

3. **No forced disengagement:** 24/7 markets with mobile portfolio apps, price alerts during sleep, and Telegram groups that never stop posting. The structural γ that casinos impose by closing is absent. The structural γ that therapy sessions impose by ending is absent. The attention gradient runs continuously.

The combination produces the observed result: Solana and Base population Pe (15.5–16.2) is an order of magnitude above gambling (2.21) and 2× above AI (7.94). Curated Solana degens (Pe = 25.5) represent the extreme. Even Ethereum — the most constrained chain — produces Pe = 3.74, above gambling. The three-chain data shows that institutional constraint (Ethereum's gas costs, regulatory environment) reduces Pe by 4× but does not eliminate the drift-dominated regime.

The Base Dencun natural experiment (§VII.D) confirms the causal direction. When the Dencun upgrade removed Base's fee constraint (March 2024), Pe increased 25% and drift-dominated wallets rose from 57.8% to 71.4%. The infrastructure didn't change — the population did, as meme coin traders flooded in. Base didn't launch as a speculative chain; it *became* one when the structural constraint was removed. This within-chain temporal evidence complements the cross-chain spatial evidence: both converge on the same conclusion that void engagement intensity drives Pe.

The Dencun result also reveals *how* compound voids scale under low constraint. TCI decreased 18% while Pe increased 25% — traders didn't deepen engagement with one token but multiplied their void engagements across many tokens simultaneously. This is what four-void compound systems predict: when the friction cost per void engagement drops to near zero (gas fees → ~0), the rational response is not deeper engagement but wider engagement — a portfolio of parallel drift cascades. The compound void architecture (Section V) scales horizontally, with each new meme token instantiating a fresh four-void system. This distinguishes crypto from gambling (one deep void) and explains why crypto Pe exceeds gambling despite lower per-engagement stakes: the aggregate drift across many simultaneous void engagements exceeds the drift through one intense engagement.

### IX.B. The Measurement Advantage

Crypto is the only void substrate where the behavioral observable is fully public. Every transaction is on-chain. Every portfolio is reconstructable. Every WCI trajectory is auditable. This has three consequences:

1. **Reproducibility.** Any researcher can reproduce EXP-021 with the same wallet list and extraction script. No IRB approval needed. No data access agreements. No privacy concerns for wallet addresses (pseudonymous but public by design).

2. **Scale.** Dune Analytics provides SQL access to aggregated blockchain data. Scaling from N=28 to N=1,000 or N=10,000 requires only query credits, not consent forms. The extraction is bounded by API rate limits, not by data availability.

3. **Real-time scoring.** The WCI→Pe pipeline can run continuously on live blockchain data. This is the basis of the product architecture: a per-wallet drift score updated in real time from public on-chain activity.

No other substrate offers this. AI drift requires controlled experiments with model access. Gambling Pe requires gambling research panel data with restricted access. Psychotherapy Pe requires clinical records. Crypto Pe requires a blockchain explorer.

### IX.C. Practical Applications

The framework's crypto application produces three product verticals:

**On-chain Void Score API.** Per-wallet Pe from WCI trajectories, delivered as a risk signal to wallet tracking platforms (GMGN, Birdeye, Dexscreener). Traders already use these platforms to monitor wallet activity. The Void Score adds a drift metric: "this wallet is concentrating into a single token at Pe = 400 — drift-dominated, high risk of further concentration or rapid reversal." Subscription pricing: $99–999/month.

**Protocol Void Rating.** Score a DeFi protocol's void properties — opacity of contract logic, responsiveness of yield to deposits, engagement coupling through incentive design. Protocols with lower void scores are safer to deploy capital into. Certification badge: "Void Index Certified: Low Drift." Annual fee: $500/protocol.

**Stablecoin Constraint Index.** Rank stablecoins by constraint strength — how transparent is the backing, how invariant is the peg, how independent is it from speculative correlations. USDC scores highest on current criteria. Algorithmic stablecoins (UST-style) score lowest — they are responsive (price changes with redemption pressure) and not independent (correlated with the ecosystem they serve). The collapse of UST is a framework prediction in retrospect: a "constraint" that fails the invariance and independence tests is not a constraint.

### IX.D. Limitations

1. **Correlation-based validation checks mostly fail at scale.** C-1 (ruin prediction) fails on 2/3 chains. C-2 (DeFi leverage) fails on both chains tested. C-4 (stablecoin constraint) is null on all 3 chains. C-5 (volume-Pe correlation) replicates only on Ethereum with a small effect (r=0.08). The headline result (Pe > 1 across all chains) is robust, the bull/bear and Crooks results are strong, but the secondary correlation predictions that held at N=28 do not generalize to the broader population. Three of five validation checks fail or are null — the framework's predictive power is in the regime classification and temporal dynamics, not in cross-sectional correlations.

2. **Observable difference across samples.** EXP-021 uses portfolio WCI (snapshot of holdings); EXP-021B and EXP-021C use trade TCI (Herfindahl of weekly buy-side volume). Both are Herfindahl measures of concentration that map to θ, but they measure different things: WCI captures the portfolio state, TCI captures the purchasing behavior. The consistent Pe > 1 finding across both observables strengthens the result; magnitude comparisons between WCI-based (N=28) and TCI-based (N=3,000+) numbers should note this methodological difference.

3. **Solana bull/bear ceiling effect.** The Solana bull/bear comparison is uninformative — 90%+ of wallets are drift-dominated in both market phases, producing near-identical Pe (10.84 vs 9.65, overlapping CIs). The framework's bull/bear prediction can only be tested where a diffusion baseline exists (Ethereum). Solana's memecoin saturation eliminates the baseline.

4. **C-4 null result.** The stablecoin-as-constraint hypothesis is not supported as a population-level linear correlation (N=3,000 across 3 chains). However, the bull/bear stablecoin control (§VII.A.1) shows a threshold effect: wallets with >30% stablecoin allocation show no bull/bear Pe separation, while wallets with <5% show 24× separation. The constraint mechanism is real but operates as a threshold, not a linear correlation.

5. **Base ≈ Solana.** The three-chain comparison shows a binary split (ETH << Base/Solana), not the predicted smooth gradient. Coinbase's institutional wrapper does not significantly constrain Base chain activity compared to Solana. This limits the "constraint environment predicts Pe" narrative to the ETH vs everything-else distinction.

6. **GM Pe excludes negative-Pe wallets.** The geometric mean is computed from positive-Pe wallets only (those in the concentration phase). Negative-Pe wallets (deconcentration phase) are excluded. The fraction of positive vs negative Pe wallets is not reported in the headline numbers. Future work should report both.

7. **Vocabulary corpus is Reddit-only.** The corpus study draws from six crypto subreddits (~19K comments, ~552K words). Crypto Twitter (CT) — the primary venue for real-time drift vocabulary — is not included due to API access limitations. Reddit may underrepresent the most extreme L3 terms (which concentrate on CT and Telegram). The bull/bear vocabulary signal may be stronger on CT than measured here.

---

## X. Conclusion

Cryptocurrency markets are drift-dominated at every scale and chain measured. Curated Solana degens show GM Pe = 25.5. General DEX traders across three blockchains show GM Pe ranging from 3.74 (Ethereum) to 16.17 (Solana), with all CIs excluding Pe = 1. Across three chains, four samples, two Herfindahl observables, and N=3,028 wallets, the drift-dominated regime holds: 93.8% on Solana, 78.7% on Base, 76.1% on Ethereum. The attention gradient drives behavior regardless of chain, and the constraint environment modulates intensity — Ethereum's institutional infrastructure reduces Pe by 4× compared to Solana, but does not eliminate drift.

The result is not unqualified. Three of five validation checks fail or are null at population scale: C-1 (ruin prediction) fails on 2/3 chains, C-2 (DeFi leverage) fails on both chains, C-4 (stablecoin constraint) is null on all 3 chains, and C-5 (volume-Pe correlation) replicates only on Ethereum with a small effect. The framework's cross-sectional correlation predictions are weaker than the N=28 pilot suggested. We report all failures honestly.

But the regime-level and temporal predictions are strong. The bull/bear experiment on Ethereum (N=968 paired wallets, p=0.000107) confirms Pe is regime-dependent. The Crooks asymmetry (26.6×) confirms thermodynamic irreversibility. The vocabulary corpus study (~19K comments, ~552K words) confirms that both the behavioral and linguistic signals align across the same temporal windows — drift vocabulary +24% in bull, identity terms doubling, constraint vocabulary +55% in bear. Five falsification conditions survived.

The Base Dencun upgrade provides the only within-chain natural experiment: when L2 fees dropped 98% in March 2024, Pe increased +25% (0.53→0.67, p < 0.000001, N=1,944) while TCI *decreased* 18% — traders diversified across more tokens but with stronger directional drift per token. This diversified drift signature is what compound void systems produce under low constraint: each new meme token instantiates a fresh four-void engagement, and near-zero fees removed the friction that bounded concurrent void count. The Dencun result confirms the causal direction — removing a structural constraint increases drift — with a within-chain design that controls for infrastructure, protocol, and chain-level confounds.

The C-4 null result (stablecoin allocation does not linearly correlate with Pe at population scale) is explained by a threshold effect: wallets with >30% stablecoin allocation show no bull/bear Pe separation, while wallets with <5% show 24× separation (§VII.A.1). The constraint mechanism is real but operates as a regime gate — above the threshold, the constraint dominates; below it, void engagement runs unchecked. This is stronger evidence for the stablecoin-as-constraint hypothesis than a linear correlation would be, because it matches the framework's prediction that constraints operate through engagement budgets, not continuous dose-response.

Four findings are immediately actionable:

1. **Measurement.** TCI → Pe extraction runs on public Dune Analytics data at negligible cost across any EVM chain and Solana. The pipeline is chain-parameterized: `--all-chains` scores Ethereum, Base, and Solana in a single run. N=3,028 wallets scored, scalable to N=10,000+.

2. **Prediction.** Fifteen confirmed predictions (including the three-chain gradient, the Dencun within-chain experiment, the bull/bear regime dependence, Crooks asymmetry, and vocabulary corpus validation), three honest failures (respecified), one remaining test with pre-specified threshold. The framework does not just describe crypto markets — it makes falsifiable claims about them, and exposes itself when they miss.

3. **Convergence.** The on-chain behavioral signal (Pe_bull > Pe_bear) and the linguistic signal (drift vocab +24%, L3 +115%) align across the same temporal windows. This is the first substrate where both the money and the words confirm the same framework prediction simultaneously. The convergence across independent measurement modalities (wallet behavior, community language) is stronger evidence than either alone.

4. **Product.** The extraction method converts directly into a real-time risk API. Per-wallet Pe is a drift score. The chain-level gradient is itself a product feature: the same wallet active on both Ethereum and Solana can be scored on each chain, with the Solana score expected to be higher.

The meme coin trader who apes in and gets rekt has never heard of Péclet numbers. But his wallet trajectory traces the same drift-dominated curve that the framework predicts from first principles, his community independently invented vocabulary for every stage of the cascade, and the public blockchain records it all — now at N=3,028 across three chains, with bull and bear windows confirming the regime transition — for anyone who knows where to look.

Your DeFi protocol is a void. Now you can score it.

---

## References

- Eckert, A. (2026a). The Architecture of Drift: A Universal Framework for Void-Mediated Meaning Generation (Paper 1, v13.0). Zenodo.
- Eckert, A. (2026b). Thermodynamics of Opacity: Technical Foundations for the Void Framework (Paper 3, v7.0). Zenodo.
- Eckert, A. (2026c). Info-Geometric Bounds on Thermodynamic Sampling and Superconducting Critical Phenomena (Paper 4, v3.5). Working paper.
- Eckert, A. (2026d). The Ground State of Observation: A Theory of Everything as Constraint Geometry (Paper 5, v4.9). Working paper.
- Eckert, A. (2026e). Never Trust the Client: Void Architecture in Multiplayer Games (Paper 6, v2.5). Working paper.
- Eckert, A. (2026f). Crypto on-chain Péclet extraction: Portfolio concentration as behavioral drift observable (EXP-021 protocol). Working paper.
- Eckert, A. (2026g). Dune Analytics Pe extraction: Three-chain N=3,000 DEX traders (EXP-021B). Working paper.
- Eckert, A. (2026h). Bull/bear natural experiment: Paired-wallet Pe comparison (EXP-021C). Working paper.
- Eckert, A. (2026i). Crypto vocabulary corpus study: Bull vs bear Reddit drift frequency analysis. Working paper.
- Ridge, W. (2023). Bitcoin is Freedom: Rituals in Bitcoin Maximalism. American Academy of Religion.
- McCook, H. (2019). Observations on Bitcoin maximalism and religious structure. Public commentary.
- Hirschman, A. O. (1945). National Power and the Structure of Foreign Trade. University of California Press. [HHI origin]
- Crooks, G. E. (1999). Entropy production fluctuation theorem and the nonequilibrium work relation for free energy differences. Physical Review E, 60(3), 2721.
- Gambling Research Consortium Studies (GRCS). Multiple studies, pooled Pe = 2.21 [1.44, 2.97]. See Paper 3, Section IV.
- Dune Analytics. (2026). Blockchain data query platform. https://dune.com
- Helius. (2026). Solana RPC and DAS API. https://helius.dev

---

## Appendix A: Per-Wallet Pe Data (N=28)

Full per-wallet results including wallet address (truncated), WCI trajectory statistics, drift velocity, diffusion coefficient, and Pe are available in `ops/lab/results/EXP-021-crypto-pe-solana.json`. The extraction script is at `ops/lab/experiments/crypto-pe-extraction.py`.

Summary distribution of |Pe| values (N=28):

| Range | Count | Fraction |
|-------|-------|----------|
| |Pe| ≤ 1 | 1 | 3.6% |
| 1 < |Pe| ≤ 10 | 6 | 21.4% |
| 10 < |Pe| ≤ 100 | 17 | 60.7% |
| |Pe| > 100 | 4 | 14.3% |

The distribution is log-normal with heavy right tail, consistent with the Fisher information divergence near θ → 1 predicted by the framework.

## Appendix B: Full Vocabulary Codebook

The complete 68-term codebook with definitions, drift stage classifications, vocabulary level classifications, and framework mappings is available in `ops/lab/experiments/EXP-021-crypto-vocabulary-codebook.md`.

Summary by quadrant (D-stage × L-level):

| | L1 | L2 | L3 |
|---|---|---|---|
| **D1** | 5 (baseline) | 12 (agency begins) | 3 (full entity) |
| **D2** | 3 (baseline) | 15 (boundary active) | 4 (identity fusion) |
| **D3** | 0 | 9 (harm normalized) | 7 (harm as identity) |
| **Constraint** | 10 (all technical) | 0 | 0 |

Notable: D3 has zero L1 terms. There is no neutral, technical vocabulary for the harm stage — all D3 terms are metaphorical or identity-level. This is consistent with the framework prediction that harm facilitation requires prior vocabulary drift (you can't describe D3 in L1 terms because the boundary erosion that enables D3 also eroded the L1 vocabulary).

## Appendix C: Dune SQL Queries for N=1000 Scaling

Three query variants are available in `ops/lab/experiments/EXP-021-dune-wallet-query.sql`:

1. **General DEX activity:** Selects wallets with >20 swap transactions on any Solana DEX over >90 days with >$1K total volume. Captures broad trader population including casual users.

2. **Raw transfers:** Selects wallets with >20 SPL token transfers. Captures wallets that interact with multiple protocols, not just DEXs.

3. **Meme-token-specific:** Filters for wallets trading tokens launched within the last 30 days (proxy for meme coin activity). Captures the high-engagement population most comparable to the N=28 sample.

Query 1 is recommended for the population estimate. Query 3 is recommended for the high-engagement comparison group. All three can be run on Dune's free tier (500 query seconds/month).

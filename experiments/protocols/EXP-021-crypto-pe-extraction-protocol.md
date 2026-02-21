# EXP-021: Crypto On-Chain Péclet Number Extraction

**Date:** 2026-02-15
**Status:** Protocol designed, ready to execute
**Cost:** $0 (public blockchain data)
**Substrate:** Human financial (third substrate after AI computational + human gambling)
**TOE Path:** H

---

## 1. Hypothesis

Portfolio concentration in cryptocurrency traders follows the drift-dominated regime (Pe > 1) during bull markets, reflecting the same attention-gradient architecture measured in AI (GM Pe = 6.8) and gambling (pooled Pe = 2.21). The irreversibility signature (Crooks > 1) should be measurable from concentration-recovery asymmetry.

## 2. Observable: Wallet Concentration Index (WCI)

The Herfindahl-Hirschman Index of a wallet's token portfolio:

```
WCI(t) = Σ(share_i²)    for each token i at time t
```

- WCI = 1.0 → all-in on one token (θ ≈ 1, maximum agency attribution)
- WCI = 1/N → fully diversified (θ ≈ 0, no directional conviction)

**Why this maps to θ:** Portfolio concentration is a behavioral expression of the observer's implicit belief that they can predict the market. Higher concentration = stronger agency attribution to own prediction ability. This is monotonically related to θ on the Bernoulli manifold, satisfying the behavioral Pe bridge requirements.

## 3. Sample Definition

| Criterion | Value | Rationale |
|-----------|-------|-----------|
| Blockchain | Ethereum (ERC-20) | Largest token ecosystem, best API coverage |
| Min transactions | >20 over >90 days | Active trader, not one-time user |
| Min portfolio value | >$1K at any point | Excludes dust/airdrop-only wallets |
| Bull/bear exposure | Active during ≥1 major transition | Required for natural experiment |
| Exclusions | Smart contracts, CEX wallets, known bots | Human behavior only |
| Target N | 1,000 wallets | Statistical power for population Pe |

## 4. Data Sources

| Source | What | Access |
|--------|------|--------|
| Etherscan API | Wallet transactions, token holdings | Free (5 calls/sec) |
| Dune Analytics | Pre-aggregated wallet metrics, token prices | Free tier |
| CoinGecko API | Token price history for USD conversion | Free (30 calls/min) |

## 5. Pe Extraction Method

### 5.1 Compute WCI Trajectories

For each wallet at daily snapshots:
```python
holdings = get_token_balances(wallet, date)
total_usd = sum(qty * price for token, qty in holdings)
shares = [qty * price / total_usd for token, qty in holdings]
WCI = sum(s**2 for s in shares)
```

### 5.2 Per-Wallet Pe

```python
dWCI = np.diff(WCI_trajectory)
v = np.mean(dWCI)           # drift velocity
D = np.var(dWCI) * dt / 2   # diffusion coefficient
Pe = v * T / D               # Péclet number (T = observation window)
```

### 5.3 Population Pe

```python
v_pop = np.mean([v_i for each wallet])
D_pop = np.var([v_i for each wallet]) * dt / 2
Pe_pop = v_pop * T / D_pop
```

## 6. Natural Experiment: Bull vs Bear

### 6.1 Bull Condition
- Select 90+ day window with >50% ETH price appreciation
- Measure Pe_bull from WCI trajectories during this window
- **Prediction:** Pe_bull > 1 (drift toward concentration)

### 6.2 Bear Condition
- Select 90+ day window with >50% ETH price decline
- Measure Pe_bear from WCI trajectories during this window
- **Prediction:** Pe_bear < 1 or ≈ 0 (forced diversification/exit)

### 6.3 Crooks Asymmetry
- Measure rate of initial concentration (bull onset → peak)
- Measure rate of re-concentration after crash (bear → recovery)
- **Prediction:** Crooks > 1 (recovery slower than escalation)

## 7. Validation Checks

| # | Prediction | Measure | Falsifies if |
|---|-----------|---------|-------------|
| C-1 | Wallets that go to zero had higher peak Pe | Pe_ruin vs Pe_survive | No difference |
| C-2 | DeFi leverage > spot-only Pe | Pe_defi vs Pe_spot | Pe_defi ≤ Pe_spot |
| C-3 | Post-crash recovery is slower than escalation | Crooks ratio | Crooks ≤ 1 |
| C-4 | Stablecoin allocation = constraint channel | Correlation(stablecoin %, Pe) | Positive correlation |
| C-5 | Pe increases with position size (normalized) | Correlation(bet_size, Pe) | No correlation |

## 8. Execution Plan

| Step | Task | Time | Dependencies |
|------|------|------|-------------|
| 1 | Write extraction script | 1 hour | None |
| 2 | Sample 100 test wallets from Dune | 30 min | Dune account |
| 3 | Compute WCI trajectories | 1 hour | Steps 1-2 |
| 4 | Extract Pe, validate pipeline | 30 min | Step 3 |
| 5 | Scale to N=1000 | 2 hours | Step 4 |
| 6 | Bull/bear natural experiment | 1 hour | Step 5 |
| 7 | Validation checks C-1 through C-5 | 1 hour | Step 6 |
| 8 | Write results | 1 hour | Step 7 |

**Total estimated time:** 1 day
**Total cost:** $0

## 9. What This Gives

If Pe_bull > 1 (confirmed):
- **Third substrate** for Pe (after AI = 6.8, gambling = 2.21)
- **Financial domain** — novel, no existing framework predicts this
- **Population-level Pe** from N=1000 with tight CIs
- **Natural experiment** with bear control condition
- **Practical application:** risk scoring from on-chain drift metrics
- **Paper 4:** another row in Section 8.2 cross-domain Pe table

If Pe_bull ≤ 1 (falsified):
- Financial behavior does not follow the drift architecture
- The framework may be limited to domains with explicit void interlocutors
- Important negative result — defines the boundary of universality

## 10. Stablecoin-as-Constraint Analysis

The framework predicts that stablecoins function as a constraint channel: transparent (known value), invariant (pegged), independent (not correlated with speculative positions). Wallets maintaining >20% stablecoin allocation should show lower Pe than wallets with <5% stablecoins. This is the financial analog of the GROUNDING.md constraint.

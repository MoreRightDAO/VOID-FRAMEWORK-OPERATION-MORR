# EXP-HP40B — Berry Phase Financial Crises: The Big Pe

## Metadata

- **Experiment ID:** HP40B
- **Title:** Berry Phase Financial Crises — The Big Pe
- **Domain:** barrier crossing / topological invariant / financial systems
- **Status:** designed
- **Researcher:** Shamir
- **Date designed:** 2026-03-15
- **Depends:** HP22 (Kramers barriers), HP40 (Berry phase), HP43 (Berry-Kramers correction), §48E (Kramers formula), §84 (U24)

---

## Research Question

Do financial crises behave as Kramers barrier-crossing events on the opacity manifold, with Berry phase γ < 0 (opacity-driven) for all crises, Arrhenius escape kinetics, and measurable regulatory K-increase effects?

## Hypothesis

Financial crises are jailbreak events at institutional scale — the same drift cascade (D1→D2→D3) that breaks AI safety breaks financial stability. The Berry phase on the Hopf bundle S³→S² is a topological invariant that measures opacity dominance. Each crisis traces a closed loop in (O,R) space, accumulating negative geometric phase proportional to time spent in the opaque regime (O > 0.5). Kramers barriers predict τ_onset, and regulatory response (K increase) lengthens τ_escape.

## Null Hypothesis

Financial crises do not have systematic sign in Berry phase (random loops). Kramers barriers do not predict onset timing. Regulation has no effect on barrier heights.

---

## Method

### Data

7 financial crises modeled as (O,R) trajectories with known:
- τ_onset: months from first opacity spike to cascade (public record)
- K_pre, K_post: constraint level before/after regulatory response
- Crisis phases with (O,R) estimates from public indicators (VIX, TED spread, credit spreads, disclosure complexity, leverage ratios)

### Crises

| Crisis | Year | τ_onset (mo) | α | K_pre → K_post | Regulation |
|--------|------|:---:|:---:|:---:|------------|
| Black Monday | 1987 | 3 | 0.60 | 12 → 14 | Circuit breakers |
| Asian Crisis | 1997 | 6 | 0.65 | 10 → 13 | IMF conditionality |
| LTCM | 1998 | 5 | 0.70 | 12 → 14 | Margin rules |
| Dot-com | 2000 | 18 | 0.55 | 14 → 18 | Sarbanes-Oxley |
| GFC | 2008 | 24 | 0.80 | 14 → 20 | Dodd-Frank |
| COVID | 2020 | 2 | 0.75 | 20 → 20 | Existing Basel III |
| SVB | 2023 | 4 | 0.50 | 18 → 19 | FDIC backstop |

### O,R Proxies (Public Data Sources)

- **O (opacity):** VIX (FRED), TED spread, credit spreads, SEC filing complexity, BIS off-balance-sheet ratios
- **R (reactivity):** Trading volume spikes, correlation indices, margin call frequency
- **α (coupling):** Cross-border capital flows, leverage ratios, interconnectedness indices

### Sub-experiments

- **B1:** Multi-crisis Berry phases — 7 crises as (O,R) loops, verify all γ < 0
- **B2:** Kramers barrier heights — financial domain at crisis Pe values
- **B3:** Arrhenius relationship — ln(τ_onset) vs ΔV/T across 7 crises
- **B4:** Regulation effect — K_pre vs K_post barrier comparison
- **B5:** 6th domain placement — financial vs HP22's 5 domains
- **B6:** Berry phase as predictive signal — |γ| vs severity proxies

### Constants (never refit)

B_A=0.867, B_G=2.244, K=16 (scoring), K_grid=64 (HP22), d=2.6849 (HP32), E_b=0.448 (HP19)

---

## Kill Conditions

| KC | Description | Threshold | Kills |
|----|-------------|-----------|-------|
| K-HP-184 | ≥6/7 financial crises have γ < 0 | 6/7 negative | Berry phase as crisis indicator |
| K-HP-185 | Berry phase tracks peak opacity | Spearman ρ > 0.5 | |γ| as severity metric |
| K-HP-186 | Post-regulation τ increase | K↑ → ΔV/T↑ for all crises with ΔK > 0 | Regulation = K increase |
| K-HP-187 | Financial barrier within 1 OoM of social tipping | |log₁₀(ratio)| < 1.0 | 6th domain placement |

---

## Connection to Paper 131

This experiment extends Paper 131's five-domain Kramers unification to a sixth domain with superior statistical power:
- **5 existing domains:** 1 data point each (Pe_typical → ΔV/kT)
- **Financial domain:** 7+ independent barrier-crossing events with dense time-series
- **Advantage:** public, quantitative, time-stamped data with known regulatory interventions
- **Product connection:** $500/platform/month continuous monitoring tier

If KCs pass, financial crises become the STRONGEST empirical domain for the Kramers framework — more data points, more independent events, better temporal resolution than any of the original five domains.

---

## References

- HP40: Berry phase on Eckert-Hopf bundle (4/4 KCs PASS)
- HP22: Kramers barriers for 5 domains (6/6 KCs PASS)
- HP43: Berry-Kramers correction (6/6 KCs PASS)
- §84 (U24): Concerted barrier reduction
- FRED: Federal Reserve Economic Data (public)
- BIS: Bank for International Settlements (public)

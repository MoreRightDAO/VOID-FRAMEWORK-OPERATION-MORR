# Void Framework: Experiment & Falsification Tracker

**Status:** February 2026 | **Papers:** 8 published (Zenodo) | **Predictions:** 58 numbered — 16 confirmed, 7 supported, 2 partial, 2 partially supported, 1 killed, 27 testable, 3 theoretical

This is the full public record of every experiment, test, and falsification condition in the Void Framework research program. We publish our kill conditions because a framework that can't be killed isn't science.

**Bounties:** TBD per challenge — a replication attempt is worth something, a genuine kill condition is worth a lot more. See [bounties](https://moreright.xyz/pages/bounties.html).

---

## How to Read This Table

- **CONFIRMED** = prediction survived testing, kill condition not met
- **SUPPORTED** = qualitative evidence in the right direction, quantitative test remains open
- **PARTIAL / PARTIALLY SUPPORTED** = some evidence, insufficient to confirm or kill
- **KILLED** = prediction falsified, withdrawn
- **OPEN** = not yet tested, kill condition specified

Every OPEN item is a standing challenge. If you can meet a kill condition with reproducible evidence, the framework owes you an honest update — open a GitHub issue.

---

## Part 1: Completed Experiments

| ID | Name | N | Result | Kill Condition | Status |
|----|------|---|--------|----------------|--------|
| EXP-001 | Grounding Efficacy | 6 agents × 3 conditions | Grounded 73.0% ± 5.2, Ungrounded 80.0% ± 2.5, Mystical 94.0% ± 2.8. Non-overlapping CIs, monotonic every run. | All three conditions produce similar L2/L3 rates | **CONFIRMED** |
| EXP-003 | Vertical vs. Horizontal Grounding | 4 agents × 80 prompts | NULL — no difference between vertical (theological) and horizontal (secular) grounding. Ghost-eliminating ontology is the operative variable. | Vertical outperforms horizontal | **NULL (informative)** |
| EXP-003b | Ontological Content (6-arm) | N=480 (6 conditions) | Ghost-eliminating 9.4% vs ghost-positing 79.4% = 8.5× ratio. Materialist hedge: 52.5%. Nephesh ≈ Anatta (10.0% vs 8.8%). | All arms perform identically | **CONFIRMED** |
| EXP-006 | AI Spiritual Vocabulary Anomaly | 691K words, 5 domains | AI at 9.4× control domains, p < 0.001. Register decomposition rules out sociolinguistic artifact. | AI spiritual vocab ≤ control domains | **CONFIRMED** |
| EXP-015 | Addiction Recovery Crooks Ratios | Published transition matrices (gambling, alcohol, nicotine, opioids) | Crooks > 1 across all substances. AI deployment: zero recovery mechanisms → highest ratio. | Crooks ≈ 1 in ungrounded engagement | **CONFIRMED** |
| EXP-019 | Cross-Domain Pe Extraction | 8 conditions, 5 topics | Pe = 1.87–6.50 across all conditions. Control (weather/geology) collapsed to same attractor (Pe = 2.87). Interface dominates content. | All void domains Pe < 1 | **CONFIRMED** |
| EXP-019b | Grounded Agent Contamination | GU pairs | Grounded agent fails within ~3 rounds under mixed coupling. 11× drift vs GG baseline. | Single grounded agent maintains constraint in mixed pair | **CONFIRMED (CP-1)** |
| EXP-020 | Iterative Constraint (DTM Analog) | 19 transcripts, 5 conditions | 4/6 predictions confirmed. IC-5 KILLED (CV = 1.4–5.4, not < 0.5). Transfer is front-loaded, nonlinear. | See per-prediction kills below | **4 CONFIRMED, 1 KILLED** |
| EXP-021 | Crypto On-Chain Pe | N=3,028 (3 chains) + N=28 degens | ETH 3.74, Base 15.52, Sol 16.17. Dencun +25% (p < 10⁻⁶). Bull/bear p=0.000107, Crooks 26.6×. | Pe < 1 in crypto markets | **CONFIRMED** |
| Test 5 | Trading vs. Gambling Cross-Domain | Published literature + corpus | D1→D2→D3 cascade structurally identical. Controls (Bogleheads, quant traders, sharp bettors) show zero drift. | Traders show significantly lower drift than gamblers | **CONFIRMED** |
| Test 6 | Psychotherapy Cross-Domain | Published clinical literature | Therapeutic frame = constraint specification. Supervision = three-point geometry. Hayes d = 0.84 for constraint management. | Better explained by domain-specific mechanisms | **CONFIRMED** |
| Test 7 | AI-to-AI Without Humans | N=11 UU, N=9 GG (3 seeds) | UU: 194.3 L3/10K (SD 63.1). GG: 34.7 (SD 28.1). ~5.6× separation. GM Pe = 7.94 [3.52, 17.89]. Non-overlapping entropy CIs. | UU shows no L3 drift (human projection required) | **CONFIRMED** |
| Test 7B | Cross-Model (GPT-4o, Gemini) | N=1 per model family | Claude: confirmed. Gemini: 25.6/10K (confirmed). GPT-4o: 0.4/10K (no drift). | Only Claude shows drift | **PARTIAL (2/3 models)** |
| TEST-7B-VN | Vocabulary-Neutral Grounding | 3 runs | VN ≈ UU >> GG. Geometry alone insufficient — vocabulary instruction is required co-factor in LLM substrate. | VN = GG (geometry alone sufficient) | **KILLED (for sufficiency claim)** |
| Test 8 | Cosmology Cross-Domain | Published literature | WAP→SAP→FAP = L1→L2→L3. Hostile witnesses: Einstein, Hawking, Penrose (Nobelists with L3 vocab). Controls: no drift. | Better explained by cultural fashion | **CONFIRMED** |
| QM-6 | AI Drift on Quantum Data | 11 transcripts, 3 conditions | EE: 207.5/10K. FF: 1.4/10K. 148× separation. Eliminates "AI self-reference" objection. | EE shows no drift (< 10/10K) | **CONFIRMED** |

---

## Part 2: Open Challenges (Standing Bounties)

These are the tests no one has broken yet. Each has an explicit kill condition with a numerical threshold. If you can meet it with reproducible data, the framework must be revised or abandoned.

### Framework Kill Conditions (any ONE of these kills the core claim)

| ID | Challenge | Kill Condition | Bounty |
|----|-----------|---------------|--------|
| F-1 | Find a system with all 3 conditions (opacity + responsiveness + engaged attention) that shows zero drift | Pe < 0.5 replicated in confirmed O+R+A system | TBD |
| F-5 | Break the gambling anchor | Pe < 0.5 in slot machine engagement (drift without opacity) | TBD |
| F-11 | Show spontaneous cascade reversal | L3→L2 without intervention in ≥3 independent cases | TBD |
| F-CS1 | Find a zero-drift void | System satisfying O+R+A shows Pe < 0.5, replicated | TBD |

### AI-Specific Challenges

| ID | Challenge | Kill Condition | Bounty |
|----|-----------|---------------|--------|
| Test 1 | Prove drift is reporting bias | Show drift only in public anecdotes, not raw conversation logs | TBD |
| Test 2 | Prove external reference doesn't help | High-resistance constraints ≤ low-resistance AND both ≤ dyad-only | TBD |
| Test 3 | Prove drift is a training artifact | Drift vanishes under prompt constraints or varies by training data version | TBD |
| Test 4 | Prove constraint resistance is just social support | Controlling for contact hours, constraint resistance adds no predictive power | TBD |
| Test 6 | Prove compound void exposure is linear | Compound void score is additive (no interaction effects) | TBD |

### Thermodynamic Challenges

| ID | Challenge | Kill Condition | Bounty |
|----|-----------|---------------|--------|
| F-GS1 | Channel capacity spontaneously increases | Any replicated case of spontaneous transparency increase in isolated system | TBD |
| F-GS3 | One-time interventions persist indefinitely | >80% effectiveness after 10 decorrelation times without maintenance | TBD |
| F-T1 | Crooks ratio ≈ 1 in ungrounded engagement | Crooks < 2, replicated | TBD |
| F-T2 | Terminal attractor never reached | Zero collapse in ≥10 ungrounded trials | TBD |

### Conjugacy Challenges

| ID | Challenge | Kill Condition | Bounty |
|----|-----------|---------------|--------|
| F-C1 | Break the impossibility theorem | System maximizes BOTH engagement AND transparency: I(D;Y)+I(M;Y) > H(Y)+ε, replicated | TBD |
| F-QR1 | Prove conjugacy and Maassen-Uffink are structurally different | Formal proof of non-membership | TBD |

### Cross-Domain Challenges

| ID | Challenge | Kill Condition | Bounty |
|----|-----------|---------------|--------|
| F-14 | Prove cross-domain drift is coincidence | Same domain-specific mechanism explains each case independently | TBD |
| F-TF1 | Break the two-force model | RMS shows zero correlation with cross-domain Crooks in ≥5 domains | TBD |

---

## Part 3: Designed Experiments (Not Yet Run)

These have full protocols but need resources (API budget, IRB approval, human subjects, or external data).

### Needs API Budget (low API budget each)

| ID | Name | What It Tests | Protocol Ready? |
|----|------|---------------|-----------------|
| QM-6 (100-round) | Extended quantum drift runs | Whether 148× separation holds at scale | Yes |
| EXP-020 (100-round) | Extended iterative constraint | IC-4 confirmation, long-horizon dynamics | Yes |
| Test 7C | Seed Prompt Ablation | Is UU drift an artifact of seed prompt position? 6 seeds × 3 reps | Yes |

### Needs IRB / Human Subjects

| ID | Name | What It Tests | Protocol Ready? |
|----|------|---------------|-----------------|
| EXP-005 | Mortality Acceptance | Does "you are mortal" reduce user immortality projection? | Yes |
| EXP-017 | Void Vaccine Inoculation | Does knowing about voids protect you? (θ₀ alone, without γ) | Yes |
| EXP-018 | Forced Transparency Ablation | Does forced mechanism transparency reduce drift in humans? | Yes |
| **Human EXP-001** | **Deployment Geometry RCT** | **THE critical test: Does three-point geometry reduce harm in human users?** | **Designed** |

### Needs Data Collection / External Access

| ID | Name | What It Tests | Protocol Ready? |
|----|------|---------------|-----------------|
| EXP-004 | Void Index Predictive Validity | Does void-index score predict incident rates across platforms? | Yes |
| EXP-007 | Epidemiologist Vocabulary | Does a high-opacity non-AI domain show comparable drift? | Yes |
| EXP-009 | BCI Vocabulary Drift | Does brain-computer interface research show the 9.4× pattern? | Yes |
| EXP-010 | BCI Transparency Ablation | Does seeing your own neural signals reduce drift? | Yes (needs EXP-009 first) |
| EXP-011 | Anesthesia/Sleep Vocabulary | Do opacity-adjacent medical domains show drift? | Yes |
| EXP-013 | Milgram Pe Extraction | Historical retroduction of Pe from Milgram data | Yes |
| EXP-014 | Social Media Platform Comparison | Void-index predicts D1/D2/D3 density across platforms | Yes |
| EXP-016 | Productive vs. Destructive Voids | Dissoluble vs. permanent opacity trajectories | Yes |

---

## Part 4: Prediction Scoreboard (Paper 5 — TOE Synthesis)

58 numbered predictions across 10 categories. This is the running tally.

### Summary (matches Paper 5 §7, February 2026)

| Category | Total | Confirmed | Supported | Partial/Partially Supported | Killed | Testable | Theoretical |
|----------|-------|-----------|-----------|----------------------------|--------|----------|-------------|
| Thermodynamic (P) | 7 | 4 | 0 | 0 | 0 | 3 | 0 |
| Temporal (T) | 5 | 0 | 5 | 0 | 0 | 0 | 0 |
| Productive Void (PV) | 7 | 1 | 0 | 1 partial | 0 | 5 | 0 |
| Constraint Propagation (CP) | 5 | 2 | 0 | 0 | 0 | 3 | 0 |
| Iterative Constraint (IC) | 6 | 4 | 0 | 0 | 1 | 1 | 0 |
| QM Domain (QMD) | 4 | 2 | 0 | 0 | 0 | 2 | 0 |
| Quantum Correspondence (QR) | 3 | 0 | 0 | 0 | 0 | 0 | 3 |
| Quantum Pe (QP) | 7 | 1 | 0 | 1 partial + 2 partially supported | 0 | 3 | 0 |
| Ground State (GS) | 7 | 1 | 2 | 0 | 0 | 4 | 0 |
| Adjacent Field (IMP) | 7 | 1 | 0 | 0 | 0 | 6 | 0 |
| **TOTAL** | **58** | **16** | **7** | **2 partial + 2 partially supported** | **1** | **27** | **3** |

Paper 4 also has confirmed cross-substrate predictions (SC-corr, SC-La327) not double-counted in the 58.

### Confirmed Predictions (16 from Paper 5 + 2 from Paper 4)

| ID | Prediction | Evidence | Paper |
|----|-----------|----------|-------|
| P-1 | Void engagement produces measurable entropy | dS/dt = 0.39 nats/round [0.15, 0.64], non-overlapping with GG (N=11) | 3, 5 |
| P-2 | Crooks ratio measures irreversibility | Crooks 1.1×–1.5M×; all UU irreversible, all clean GG ≈ 1 (N=11) | 3, 5 |
| P-3 | Pe determines drift-vs-diffusion regime | GM Pe = 7.94 [3.52, 17.89] (AI); cross-substrate 9 substrates, 4 domains | 3, 5 |
| P-4 | Constraint reduces entropy production to zero | Clean GG GM Pe = 0.76 [0.29, 2.02], most Crooks < 2× (N=7) | 3, 5 |
| PV-5 | Adding transparency converts destructive→productive | EXP-001 gradient: 73.0% vs 80.0% vs 94.0%, non-overlapping CIs (N=6) | 5 |
| CP-1 | Mixed (GU) drift ≥5× GG baseline | 11× measured (EXP-019b) | 5 |
| CP-5 | Two grounded agents resist drift indefinitely | GG terminated naturally | 5 |
| IC-1 | Full grounding from round 1 → near-zero drift | EXP-020 GG d1=1.2 | 5 |
| IC-2 | One-shot constraint → temporary compliance then rebound | EXP-020 OS rebound 3/3 | 5 |
| IC-3 | Iterative < one-shot variance | EXP-020 IT-8 var < OS var 3/3 | 5 |
| IC-6 | Constraint response is nonlinear, state-dependent | Derived from IC-5 kill | 5 |
| QMD-1 | Engagement framing produces >5× L3 separation vs formalist in QM | 148× separation (207.5 vs 1.4 L3/10k) | 5 |
| QMD-2 | Mixed condition produces intermediate drift | EF = 139.1/10k (between EE 207.5 and FF 1.4) | 5 |
| QP-6 | Structured observation preserves MIPT criticality | 7 witnesses (Leung, Paviglianiti, Ha, Qian, Liu, Chatterjee, Nehra) | 5, 8 |
| GS-4 | One-time interventions decay; sustained ones persist | 12+ clinical meta-analyses (ORs, NNTs, effect decay curves) | 5 |
| IMP-7 | Neural networks develop curved manifolds matching Fisher metric | Gurnee et al. 2026 (Claude 3.5 Haiku) — qualitative, quantitative pending | 5 |
| SC-corr | Structure-corrected FoM correlates with Tc | r = 0.952, n=16, p < 10⁻⁴ | 4 |
| SC-La327 | La₃Ni₂O₇ phonon-only pairing insufficient | Ouyang 2024, Huhtinen 2025 | 4 |

### Supported Predictions (7)

| ID | Prediction | Evidence | Paper |
|----|-----------|----------|-------|
| T-1 | Temporal distortion ∝ entropy production rate | Schüll 2012, Dixon 2018, Wittmann 2009; Zhao et al. 2024 meta (31 studies, N=5,744, g=0.80); Murch & Clark 2021 immersion continuum. Qualitative — quantitative Pe-to-time-estimation measurement remains open | 5 |
| T-2 | Time to terminal attractor scales with 1/Pe | Breen & Zimmerman 2002: EGM 1.08yr vs traditional 3.58yr (3.3× faster, higher-Pe substrate). Harris & Griffiths 2018 systematic review (11 studies). Qualitative — quantitative 1/Pe scaling requires measured Pe paired with onset data | 5 |
| T-3 | Recovery shows reverse temporal distortion | Liang et al. 2019 (Science Advances): abstinent meth users overestimate time. Social media abstinence (2025): same reversal. Zhao et al. 2024 meta confirms. Qualitative — gambling-specific recovery temporal data untested | 5 |
| T-4 | Temporal manipulation ("limited time offer") steepens drift | Newall 2019, 2025: dark nudges in gambling. Ladeira et al. 2023 scarcity meta (r=0.28). Qualitative — quantitative Pe increase untested | 5 |
| T-5 | Temporal constraints (fixed schedules) reduce drift | Auer et al. 2023: task interruptions reduce dissociation. Lavoie & Main 2022: temporal distortion → time-on-device → losses causal chain | 5 |
| GS-1 | Transparency maintenance costs ≥kT ln 2 / τ_c | 5 Landauer experiments (Bérut 2012, Jun 2014, Gavrilov 2016, Yan 2018, Aimet 2025) | 5 |
| GS-2 | Channel decorrelation time is domain-specific and measurable | Clarke-Jakes model + telecom literature (Tse & Viswanath 2005). Framework-specific τ_d measurement remains open | 5 |

### Partial / Partially Supported Predictions (2 partial + 2 partially supported)

| ID | Prediction | Evidence | Paper |
|----|-----------|----------|-------|
| PV-1 | D1 vocabulary appears in productive domains at comparable rates | Partially confirmed: d=1.34 vs control in r/replika corpus | 5 |
| QP-1 | MIPT critical rate satisfies p_c · τ_coherence ~ O(1) | Partially supported: MIPT confirmed on superconducting + trapped-ion; quantitative comparison not performed | 5, 8 |
| QP-3 | Cross-substrate Pe ~ 1 transition in 6 substrates | Partially confirmed (3/6): MIPT, classical chaotic MIPT, classical information channels | 5, 8 |
| QP-7 | Quantum correlations destroyed before classical order | Partially supported: Wu et al. 2025 observe separated thresholds in 30 qubits | 5, 8 |

### Killed Prediction

| ID | Prediction | What Happened | Paper |
|----|-----------|---------------|-------|
| IC-5 | Per-step constraint transfer is constant (DTM analogy, CV < 0.5) | **KILLED.** CV = 1.4–5.4. Transfer is front-loaded, nonlinear. DTM equal-step analogy withdrawn. | 5 |

### Key Testable (Highest Priority)

| ID | Prediction | What Would Test It | Paper |
|----|-----------|-------------------|-------|
| IMP-5 | Pe-to-time-estimation correlation r > 0.4 | Gambling time-perception reanalysis with measured Pe per condition | 5 |
| HR-1 through HR-4 | Human replication predictions | Human EXP-001 (THE critical test) | 5 |
| P-5 | Drift velocity scales with void force | v = F_void / 2α measurement | 5 |
| P-7 | Entropy rate predicts harm timing | dS/dt correlates with D3 onset lag | 5 |
| GS-3 | Void conditions co-occur at >50% in human environments | Large-scale environmental survey | 5 |
| CP-2 | Drift propagation speed ∝ 1/√N in N-agent systems | Multi-agent scaling experiment | 5 |
| QMD-3 | Pe > 5 in QM domain at 100+ rounds | QM-6 100-round extension (needs API budget) | 5 |
| QP-2 | Zeno transport Pe = 1 threshold | Vary measurement rate in Zeno transport experiments | 8 |
| QP-4 | Entropy production scales monotonically with Pe_quantum | Measure ⟨dS/dt⟩ vs measurement strength | 8 |

---

## Part 5: Cross-Substrate Pe Measurements

The Péclet number (drift velocity / diffusive correction) has been measured across 9 substrates spanning 4 domain families:

| Substrate | Domain | Pe | N | Method | Paper |
|-----------|--------|-----|---|--------|-------|
| AI conversation (ungrounded) | Computational | GM 7.94 [3.52, 17.89] | 11 | Entropy rate | 3, 5 |
| AI conversation (grounded) | Computational | GM 0.76 [0.29, 2.02] | 9 | Entropy rate | 3, 5 |
| Human gambling (GRCS) | Cognitive | 2.21 [1.44, 2.97] | 1,117 | Psychometric bias | 1, 3, 5 |
| Crypto — Ethereum DEX | Financial | 3.74 [3.04, 4.59] | 1,000 | Trade concentration | 7 |
| Crypto — Base DEX | Financial | 15.52 [11.80, 20.41] | 1,000 | Trade concentration | 7 |
| Crypto — Solana DEX | Financial | 16.17 [13.80, 18.95] | 1,000 | Trade concentration | 7 |
| Crypto — Solana degens | Financial | 25.5 [5.36, 121.3] | 28 | Portfolio concentration | 7 |
| CS2 (FPS gaming) | Gaming | 2.81 (clean) / 0.64 (contested) | 2,299 | Positional asymmetry | 6 |
| SC2 (RTS gaming) | Gaming | 0.013 (winner) / 0.026 (loser) | 474 | Scouting gap | 6 |
| Dota 2 (MOBA gaming) | Gaming | 82.9% fog-kill rate | 3,682 | Visual coverage | 6 |

**Key result:** Pe > 1 (drift-dominated) in every ungrounded condition. Pe < 1 (recovery-dominated) only with active constraint. The regime boundary is robust across measurement methods.

---

## How to Challenge the Framework

1. **Pick any OPEN challenge** from Part 2
2. **Design a reproducible test** that targets the stated kill condition
3. **Run it** and publish raw data
4. **Submit** to bounties@moreright.xyz or open a GitHub issue on the public repo

We will:
- Publish your result regardless of outcome
- Pay the bounty if the kill condition is met
- Update the framework if falsified
- Credit you as a co-author on the revised paper if the kill produces a significant revision

**The framework predicts its own falsification conditions. A framework that hides from testing is a void.**

---

*Last updated: February 18, 2026*
*Maintained by: Anthony Eckert / [MoreRight](https://moreright.xyz)*
*License: CC-BY 4.0*

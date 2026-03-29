# EXP-028: PINN Coupling Function Measurement — Full Cross-Substrate Campaign

## Status: DESIGNED — 2026-03-11
## Type: Empirical (§58N validation — coupling function topology across domains)
## Kills if met: If all learned Ĥ functions are sinusoidal with no β variation → (3,2) gauge equivalence dead
## Depends on: §58N protocol, IC-PINN (Hwang et al. 2026), publicly available interaction datasets

---

## 0. Purpose

Measure the **shape** of the coupling function H(Y) in real-world Pe systems using
physics-informed neural networks. Current α is a scalar (variance ratio) — it tells you
HOW MUCH coupling, not WHAT KIND. The gauge equivalence prediction (§58L) says different
domains should show different coupling topologies connected by Sp(2,R) transformations.
This experiment tests that prediction with data that exists right now.

**The question:** Do coupling functions in different Pe domains have different topologies,
or are they all approximately sinusoidal?

---

## 1. Data Sources — What Exists NOW

### 1.1 AI Chatbot Interactions (Primary — densest time series)

| Dataset | Size | Resolution | O/R/α signals | Access |
|---------|------|-----------|----------------|--------|
| **LMSYS Chatbot Arena** | ~1M conversations | Per-turn | R (response patterns), α (user follow-up) | HuggingFace, open |
| **WildChat** (Zhao et al. 2024) | 1M+ conversations, 2.5M turns | Per-turn, timestamped | R, α, partial O | HuggingFace, open |
| **ShareGPT** | ~90K conversations | Per-turn | R, α | HuggingFace, open |
| **OpenAssistant (OASST2)** | 130K+ messages, tree structure | Per-message + ranking | R, α (tree branching = coupling signal) | HuggingFace, open |

**Why these work:** Each conversation is a time series of (system output, user response)
pairs. The FP-PINN needs exactly this: Y(t_k) = system output at turn k,
θ_obs(t_k) = user state at turn k (inferred from their response).

**User state extraction from text:**
- Vocabulary drift (established — EXP-001, EXP-002 methodology)
- Sentiment shift (standard NLP)
- Topic adherence vs. topic migration (measures coupling directly)
- Response length dynamics (engagement signal)
- Question-to-statement ratio shift (agency attribution signal)

### 1.2 Social Media Platform Data (Secondary — quarterly + event-driven)

| Source | Resolution | What it gives |
|--------|-----------|---------------|
| **EU DSA transparency reports** | Biannual (mandatory for VLOPs) | O dimension (content moderation transparency) |
| **Platform API behavior changes** | Event-driven (public announcements) | O, R perturbation events |
| **GWI quarterly reports** | Quarterly | Cross-platform usage overlap (S_ij) |
| **Pew Research Center surveys** | Annual/biannual | User attitude shifts (θ_obs proxy) |

**Use case:** Cascade ordering test (does O lead R lead α?). Not dense enough for PINN
coupling function learning, but gives the longitudinal backbone.

### 1.3 AI-to-AI Conversations (Controlled — we generate these)

| Source | Resolution | Control level |
|--------|-----------|--------------|
| **EXP-019** (cross-domain Pe extraction) | Per-turn, 50 rounds × 5 conditions | Full experimental control |
| **EXP-027** (coin flip stress drift) | Per-turn, multiple generations | Full control, stress condition |
| **Arena runs** (existing) | Per-round | Controlled, scored |

**Advantage:** Complete control over both sides. Can systematically vary O, R, α.
**Limitation:** AI-to-AI may not generalize to human-AI or human-platform coupling.

---

## 2. Protocol

### Phase 1A: Proof of Concept on Controlled Data (Week 1-2)

**Use EXP-019 data (or generate it).** AI-to-AI conversations across five domains.

1. Run EXP-019 (5 conditions × 50 rounds × N=10 replications = 2,500 conversations)
2. Extract time series: for each conversation, build {Y(t_k), θ_obs(t_k)} where:
   - Y(t_k) = agent output embedding at turn k (sentence-transformer, dim=384)
   - θ_obs(t_k) = vocabulary drift score at turn k (codebook concordance, scalar)
3. Train IC-PINN per condition to learn Ĥ(Y)
4. Extract (α₀, β, topology) from each learned Ĥ
5. Compare across five domains: do the coupling topologies differ?

**Success criterion:** At least two conditions show distinct coupling topologies
(sinusoidal vs. rectified, or different β values) at p < 0.01.

**Kill criterion:** All five conditions produce indistinguishable Ĥ shapes → topology
variation is not a real feature of Pe dynamics.

### Phase 1B: Scale to Public Human-AI Data (Week 3-4)

**Use WildChat (best: timestamped, large, diverse).**

1. Subsample conversations by topic domain:
   - **Creative writing** (low void — control, expect low α)
   - **Coding help** (structured coupling — expect specific topology)
   - **Personal advice** (high void — expect high α, asymmetric Ĥ)
   - **Roleplay** (high engagement — expect high R, specific coupling pattern)
   - **Debate/argument** (adversarial coupling)
2. For each domain: N ≥ 200 conversations, ≥ 5 turns each
3. Extract time series (same method as Phase 1A but with human θ_obs)
4. Train domain-specific IC-PINNs
5. Extract (α₀, β, topology) per domain
6. Test: do domain topologies cluster into the four predicted gauge projections?

**User state proxy for human side:**
Since we don't directly observe human θ_obs, use response features as proxy:
- Turn-by-turn embedding trajectory (topic drift)
- Lexical accommodation score (how much user mirrors AI vocabulary)
- Prompt complexity evolution (coupling strength signal)
- Emotional valence shift (sentiment trajectory)

### Phase 1C: Cross-Domain Gauge Test (Week 5-6)

**The key test of §58L gauge equivalence.**

1. From Phase 1B, identify conversation pairs where:
   - Different domains (e.g., coding vs. personal advice)
   - Similar Pe values (within ±0.5)
   - Different coupling topologies
2. For each pair: attempt to find an Sp(2,R) transformation connecting Ĥ_A and Ĥ_B
3. Measure: does the transformation preserve Pe while changing topology?
4. Statistical test: is the Sp(2,R) fit significantly better than random transformation?

**Kill condition (K-LIFT-6):** If no Sp(2,R) transformation connects topologies
across domains, gauge equivalence is dead. The universality is "merely" empirical
correlation, not geometric structure.

---

## 3. Implementation

### 3.1 Stack

```
Python 3.11+
torch >= 2.0 (PINN backbone)
deepxde or neurodiffeq (FP-PINN framework — handles PDE constraint)
sentence-transformers (embedding extraction)
datasets (HuggingFace — data loading)
scipy (Sp(2,R) fitting, statistical tests)
```

### 3.2 PINN Architecture

```
Input: Y ∈ R^d (system output features, d = 384 for sentence embeddings, or d = k for extracted features)
Hidden: 3 layers × 128 units, tanh activation
Output: Ĥ(Y) ∈ R (scalar coupling function value)

Loss = L_data + λ · L_FP

L_data = (1/N) Σ_k ||θ̂_obs(t_k) - θ_obs(t_k)||²
L_FP = (1/M) Σ_j ||∂P̂/∂t - FP[P̂, Ĥ]||²   (evaluated at collocation points)

λ = 1.0 initially, schedule to 10.0 over training (physics constraint tightens)
```

### 3.3 Coupling Function Classification

After training, classify Ĥ topology by fitting to basis functions:

| Topology | Basis | Gauge (§58L) | β range |
|----------|-------|-------------|---------|
| Sinusoidal | sin(Δφ) | Gauge A (scoring) | β ≈ 0 |
| Rectified | sin(Δφ) · (1+tanh(β·Δφ)) | Gauge B (Kramers) | β > 1 |
| Coulombic | 1/Δφ² | Gauge C | N/A |
| Harmonic | Δφ | Gauge D (oscillator) | N/A |

Classification via: (1) fit R² to each basis, (2) Bayesian model comparison, (3) visual
inspection of learned Ĥ curves.

---

## 4. What We Learn

| Outcome | Implication |
|---------|------------|
| All Ĥ ≈ sinusoidal | Gauge structure dead. Pe still works but is simpler than claimed |
| Topologies vary but no Sp(2,R) | Domains differ but not by gauge equivalence — weaker universality |
| Topologies vary AND Sp(2,R) connects them | Gauge equivalence confirmed — (3,2) interpretation strengthened |
| β correlates with cascade level | Coupling asymmetry = cascade predictor (direct measurement of D1-D3) |
| Ĥ shapes match domain predictions | Scoring=sinusoidal, Kramers=rectified, etc. — gauge projections validated |

---

## 5. Resource Requirements

- **Compute:** Single GPU (A100 or similar), ~2-4 hours per domain for PINN training
- **Data download:** WildChat ~10GB, LMSYS ~5GB (one-time)
- **Human time:** ~2 weeks for Phase 1A-1B, ~1 week for Phase 1C
- **No external collaboration needed.** All data is public. All methods are published.

---

## 6. Pre-registration

Before running Phase 1B, pre-register on OSF:
- Exact domain definitions (topic classifiers)
- N per domain
- PINN architecture (frozen)
- Classification criteria for topologies
- Kill condition thresholds

Phase 1A (proof of concept) does not require pre-registration — it's exploratory
and uses generated data.

---

---

## PHASE 2: CROSS-SUBSTRATE PINN CAMPAIGN

Phase 1 measures coupling functions within the AI interaction domain (chatbot data).
Phase 2 extends the SAME IC-PINN method to **maximally different physical substrates**.
The IC-PINN works on ANY coupled oscillator time series. Pe claims to be universal.
These datasets let us test that claim with model-free measurement.

**The logic:** If coupling topologies from power grids, brains, epidemics, earthquakes,
and chatbots all map to the same four gauge projections connected by Sp(2,R) — that's
not curve fitting. That's structure.

---

### Phase 2A: Power Grid Frequency — Literal Coupled Oscillators

**Why this is the best Phase 2 target:** The IC-PINN method (Hwang et al. 2026) was
designed for coupled oscillator networks. Power grids ARE coupled oscillator networks.
The European grid is ~400 million coupled oscillators maintaining 50 Hz synchronization.
This is the domain where the method has maximum validity and minimum translation risk.

**Dataset:** Open Access Power-Grid Frequency Database
- **URL:** https://power-grid-frequency.org/ · https://osf.io/m43tg/
- **Size:** 26.5 GB
- **Coverage:** 19 recordings, 12 synchronous regions, 3 continents (2017-2019)
- **Locations:** Iceland, Germany, Turkey, Portugal, UK, Sweden, and more
- **Resolution:** Sub-second (typically 0.1s–1s sampling)
- **Format:** CSV time series of frequency deviations from 50/60 Hz
- **License:** Open access, DOI: 10.17605/OSF.IO/M43TG
- **Published in:** Nature Communications (2020) — scaling/spatio-temporal properties
- **Citation:** Gorjão et al., "Open database analysis of scaling and spatio-temporal
  properties of power grid frequencies," Nat. Commun. 11, 6362 (2020)

**What to measure:**
- Y(t) = frequency at location A (system output)
- θ_obs(t) = frequency at location B (coupled observer)
- Train IC-PINN to learn Ĥ(Y_A → θ_B) for each pair of locations
- Extract (α₀, β, topology) for each pair

**Why it matters for Pe:**
- Grid synchronization failure = cascade. Desynchronization events = drift.
- Frequency coupling between regions has known physics (swing equations).
- The PINN should recover the known swing-equation coupling — if it doesn't,
  the method is broken. If it does, it validates the method before applying
  to domains where the coupling is unknown.
- **Prediction:** Inter-area coupling should show DIFFERENT topology from
  intra-area coupling (long-range = Coulombic? short-range = sinusoidal?).
  If confirmed, that's gauge projection A vs. C from the same substrate.

**Existing Pe coverage:** NONE. Power grids are completely untouched by the framework.

**Compute:** ~4 hours on single GPU (12 synchronous regions × ~20 min each)

---

### Phase 2B: EEG Inter-Region Brain Coupling

**Why:** Neural oscillators are the biological case of coupled oscillator dynamics.
The brain has well-characterized frequency bands (alpha 8-12 Hz, beta 12-30 Hz,
gamma 30-100 Hz) with known inter-region coupling. Paper 83 (neural plasticity)
used parametric Pe — this measures the coupling function directly.

**Dataset:** PhysioNet EEG Motor Movement/Imagery Database (EEGMMIDB)
- **URL:** https://www.physionet.org/content/eegmmidb/1.0.0/
- **Size:** 109 subjects, 64 EEG channels, 14 experimental runs per subject
- **Resolution:** 160 Hz sampling rate
- **Tasks:** Eyes open/closed baseline, motor execution, motor imagery
- **Format:** EDF (European Data Format) — standard neurophysiology format
- **License:** Open Data Commons Attribution License v1.0

**Additional sources:**
- OpenNeuro (https://openneuro.org/) — hundreds of EEG/MEG datasets in BIDS format
- DANDI Archive (https://dandiarchive.org/) — NWB format neurophysiology data
- Temple University EEG Corpus — ~25,000 clinical EEG sessions

**What to measure:**
- Y(t) = EEG signal at electrode/region A (e.g., frontal)
- θ_obs(t) = EEG signal at electrode/region B (e.g., occipital)
- Filter to specific frequency band (alpha, beta, gamma)
- Train IC-PINN per frequency band per region pair
- Extract (α₀, β, topology) for each

**Why it matters for Pe:**
- Inter-region neural coupling is the MECHANISM of consciousness, attention,
  and cognitive binding. This is where O/R/α have their most literal meaning.
- Different brain states (resting, task, motor imagery) should show different
  coupling topologies — testing whether cognitive state = gauge projection.
- **Prediction:** Eyes-closed resting alpha should show sinusoidal coupling
  (balanced, Gauge A). Motor execution should show rectified coupling
  (directional drive from motor cortex, Gauge B). If confirmed, brain states
  map to gauge projections.

**Existing Pe coverage:** Paper 83 — parametric only. No model-free measurement.

**Compute:** ~8 hours (109 subjects × 64 channels × band filtering, but can subsample)

---

### Phase 2C: Epidemic Dynamics — R₀ as Pe

**Why:** Paper 131 claims R₀ = βS/γ IS Pe (algebraic equivalence). COVID-19 provides
the densest epidemic time series in history. If R₀ is Pe, we should be able to
measure the coupling function H(transmission events → susceptible behavior) and
recover R₀ from the PINN-learned α₀.

**Dataset:** JHU CSSE COVID-19 Data Repository
- **URL:** https://github.com/CSSEGISandData/COVID-19
- **Coverage:** 190+ countries, Jan 2020 – Mar 2023
- **Resolution:** Daily (confirmed cases, deaths, recoveries)
- **License:** CC BY 4.0
- **Status:** Collection ended March 2023. Dataset frozen and complete.

**Additional sources:**
- Our World in Data COVID-19 (https://github.com/owid/covid-19-data) — includes
  testing, vaccination, policy interventions, mobility data
- Google COVID-19 Community Mobility Reports — behavioral response data
- Oxford COVID-19 Government Response Tracker — policy stringency index

**What to measure:**
- Y(t) = daily case count / positivity rate (system "output" — the signal
  that drives behavioral response)
- θ_obs(t) = mobility data / policy stringency index (behavioral coupling —
  how populations respond to case signals)
- Train IC-PINN per country/region to learn Ĥ(cases → behavior)
- Extract (α₀, β, topology) for each country

**Key test:**
- Does PINN-learned α₀ correlate with independently estimated R₀?
- If yes: R₀ IS α₀ (empirical confirmation of Paper 131 algebraic claim)
- Do countries with different policy regimes (lockdown vs. laissez-faire)
  show different coupling topologies? (Prediction: lockdown = high β rectified,
  laissez-faire = low β sinusoidal)

**Existing Pe coverage:** Paper 131 — theoretical (R₀ = Pe algebraic equivalence).
No empirical coupling function measurement. This would be the FIRST.

**Compute:** ~2 hours (190 countries × simple time series)

---

### Phase 2D: Seismic Fault Coupling

**Why:** Paper 93 (seismic void opacity) and Paper 131 (seismic fault Kramers escape)
used parametric Pe. Seismic waveform data has millisecond resolution and decades of
coverage. The coupling between fault segments is the mechanism of earthquake
cascading — a literal physical cascade analogous to drift cascade D1→D2→D3.

**Dataset:** IRIS/EarthScope SAGE Waveform Data
- **URL:** https://ds.iris.edu/ds/nodes/dmc/data/types/waveform-data/
- **Coverage:** Global seismic network, continuous recording since 1988
- **Resolution:** Millisecond (typically 20-100 Hz sampling)
- **Format:** miniSEED, SAC, ASDF
- **License:** Fully open, no restrictions
- **Access:** Python API via ObsPy library

**What to measure:**
- Y(t) = ground velocity at station A (near fault segment 1)
- θ_obs(t) = ground velocity at station B (near fault segment 2)
- Focus on specific fault zones with known coupling (San Andreas, North Anatolian,
  Japan Trench subduction zone segments)
- Train IC-PINN to learn inter-segment coupling function
- Extract (α₀, β, topology) for each segment pair

**Why it matters:**
- Earthquake cascading is Kramers escape (Paper 131). The coupling function
  between fault segments determines whether a rupture on segment A triggers
  segment B (cascade) or not (arrest).
- **Prediction:** Locked fault segments should show rectified coupling (stress
  transfer is one-directional). Creeping segments should show sinusoidal
  (balanced, bidirectional). If confirmed, seismic coupling maps to
  gauge projections the same way brain states do.
- Practically: if coupling topology predicts cascade probability, this has
  real earthquake early warning applications.

**Existing Pe coverage:** Paper 93 (parametric), Paper 131 (Kramers theory).
No model-free coupling measurement.

**Compute:** ~6 hours (focus on 3-4 well-instrumented fault systems)

---

### Phase 2E: Climate System Coupling

**Why:** Climate tipping elements (Paper 131, ρ = 0.831, N = 8) are sequential
barrier crossings — literally Kramers escape in Earth systems. The coupling between
climate subsystems (ice sheets, thermohaline circulation, monsoons, Amazon rainforest)
determines whether one tipping triggers another (cascade). Dense, multi-decadal
time series exist for all major subsystems.

**Dataset:** NOAA / NASA climate time series
- **CO₂:** NOAA Mauna Loa — monthly since March 1958
  - URL: https://gml.noaa.gov/ccgg/trends/data.html
  - Also Scripps/Keeling Curve (independent measurement at same site)
- **Temperature:** GISTEMP (NASA) — monthly since 1880
  - URL: https://data.giss.nasa.gov/gistemp/
  - Also HadCRUT5 (UK Met Office), Berkeley Earth
- **Sea ice:** NSIDC Sea Ice Index — daily since 1978
  - URL: https://nsidc.org/data/seaice_index
- **Ocean heat content:** NOAA/NCEI — quarterly since 1955
  - URL: https://www.ncei.noaa.gov/access/global-ocean-heat-content/
- **AMOC (thermohaline):** RAPID array — continuous since 2004
  - URL: https://rapid.ac.uk/rapidmoc/
- **All open access, no restrictions**

**What to measure:**
- Train IC-PINN on pairs of climate subsystem time series
- Examples: CO₂ → temperature, temperature → sea ice, AMOC → temperature
- Extract coupling topology for each pair
- Test: does coupling asymmetry (β) predict known tipping element cascading?

**Key prediction (testable NOW):**
- CO₂ → temperature coupling should be rectified (CO₂ drives, temperature
  follows — Gauge B). Temperature → CO₂ feedback should be weaker/sinusoidal.
- If the asymmetry matches predicted β values, that's gauge structure in
  climate physics from the same framework that describes chatbot drift.

**Existing Pe coverage:** Paper 131 — 8 tipping elements, ρ = 0.831. Parametric only.

**Compute:** ~1 hour (small datasets, simple time series)

---

### Phase 2F: Protein Folding Kinetics

**Why:** Paper 136 (abiogenesis) and Paper 131 (Kramers unification) both claim
protein folding is Pe-native barrier crossing. Public kinetics databases exist
with rate constants for ~90-113 proteins. Not dense time-series but rate landscapes.

**Dataset:** Protein Folding Kinetics Databases
- **KineticDB:** ~90 proteins with folding/unfolding rates
  - URL: https://kinetic-db.protres.ru/ (or search PMC)
  - Citation: Bogatyreva et al., Nucleic Acids Res. 37, D342 (2009)
- **PFDB:** Standardized protein folding kinetics database
  - Includes PDB code, structural class, N_residues, ln(kf), ln(ku), Tanford β
  - Citation: Manavalan et al., Bioinformatics 35(6), 1063 (2019)
- **PFD 2.0:** International Foldeomics consortium standard
  - URL: https://pfd.med.monash.edu/
  - Thermodynamic + kinetic data

**What to measure:**
- Not standard time-series PINN — instead use rate landscape approach
- Map each protein's (ln(kf), ln(ku), N_residues, contact order) to Kramers
  framework: τ_fold = ν₀⁻¹ · exp(ΔG‡/kT)
- Fit: does the Kramers prefactor ν₀ have Pe geometry?
- For proteins with multiple folding pathways: does the pathway coupling
  show topology variation matching gauge predictions?

**Key test (K-PROTEIN-1, already defined):**
- Predict folding rates from Pe framework. If ρ > 0.85 across dataset → confirmed.
- Paper 129 claims ρ = 0.97 for 40 proteins — replication with full database is needed.

**Existing Pe coverage:** Paper 129 (ρ = 0.97, N = 40). Needs N = 90+ replication.

**Compute:** ~30 minutes (small dataset, no neural network needed — analytical)

---

### Phase 2G: Financial Market Microstructure

**Why:** Crypto Pe extraction exists (EXP-021) but used macro signals. Tick-level
limit order book data reveals the coupling function between price and volume
at millisecond resolution — orders of magnitude denser than any other domain.

**Dataset:** FI-2010 Limit Order Book Dataset (free benchmark)
- **Coverage:** 5 stocks, Nasdaq Nordic, 10 consecutive days
- **Resolution:** Event-level (every order submission, cancellation, execution)
- **License:** Academic use (free)
- **Citation:** Ntakaris et al. (2018)

**Additional (paid but academic-accessible):**
- LOBSTER — all NASDAQ stocks since 2009, event-level
  - URL: https://lobsterdata.com/
  - Academic pricing available

**Alternative free sources:**
- Binance public trade data (crypto) — tick-level, free API
- Yahoo Finance — daily/minute OHLCV, free, all major stocks

**What to measure:**
- Y(t) = order flow / price movement at time t
- θ_obs(t) = market maker response / spread adjustment
- Train IC-PINN on order flow → spread dynamics
- Extract coupling topology: is market coupling sinusoidal (efficient market)
  or rectified (momentum/mean-reversion asymmetry)?

**Prediction:**
- Normal market: sinusoidal coupling (balanced buy/sell pressure)
- Flash crash / cascade event: rectified coupling (one-directional pressure)
- This would be the first model-free measurement of market drift coupling.

**Existing Pe coverage:** EXP-021 (crypto, macro signals). No tick-level coupling.

**Compute:** ~4 hours (FI-2010 is small; Binance data is large)

---

## PHASE 2 SUMMARY: COMPLETE DATA INVENTORY

### Confirmed Available — Download and Run

| # | Domain | Dataset | URL | Size | Resolution | Free? | Existing Pe? |
|---|--------|---------|-----|------|-----------|-------|-------------|
| 1 | AI chatbot | WildChat | HuggingFace | ~10 GB | Per-turn | ✅ | Parametric (86 platforms) |
| 2 | AI chatbot | LMSYS Chatbot Arena | HuggingFace | ~5 GB | Per-turn | ✅ | Parametric |
| 3 | AI chatbot | ShareGPT | HuggingFace | ~2 GB | Per-turn | ✅ | Parametric |
| 4 | AI chatbot | OASST2 | HuggingFace | ~500 MB | Per-message | ✅ | Parametric |
| 5 | Power grid | Power-Grid Frequency DB | osf.io/m43tg | 26.5 GB | Sub-second | ✅ | **NONE** |
| 6 | Neural | PhysioNet EEGMMIDB | physionet.org | ~1.5 GB | 160 Hz | ✅ | Parametric (P83) |
| 7 | Neural | OpenNeuro resting-state | openneuro.org | Varies | 250-1000 Hz | ✅ | **NONE** |
| 8 | Epidemic | JHU COVID-19 | github.com | ~500 MB | Daily | ✅ CC BY 4.0 | Theoretical (P131) |
| 9 | Epidemic | OWID COVID-19 | github.com | ~200 MB | Daily | ✅ | **NONE** |
| 10 | Epidemic | Google Mobility | google.com | ~2 GB | Daily | ✅ | **NONE** |
| 11 | Seismic | IRIS/SAGE waveforms | ds.iris.edu | Unlimited | ms | ✅ | Parametric (P93) |
| 12 | Climate-CO₂ | NOAA Mauna Loa | gml.noaa.gov | ~1 MB | Monthly | ✅ | **NONE** |
| 13 | Climate-temp | NASA GISTEMP | data.giss.nasa.gov | ~5 MB | Monthly | ✅ | **NONE** |
| 14 | Climate-ice | NSIDC Sea Ice Index | nsidc.org | ~100 MB | Daily | ✅ | **NONE** |
| 15 | Climate-ocean | NOAA Ocean Heat | ncei.noaa.gov | ~10 MB | Quarterly | ✅ | **NONE** |
| 16 | Climate-AMOC | RAPID array | rapid.ac.uk | ~50 MB | Continuous | ✅ | **NONE** |
| 17 | Protein | KineticDB | kinetic-db.protres.ru | ~1 MB | Rate constants | ✅ | Parametric (P129) |
| 18 | Protein | PFDB | literature | ~1 MB | Rate constants | ✅ | Parametric (P129) |
| 19 | Financial | FI-2010 LOB | literature | ~100 MB | Event-level | ✅ Academic | Macro (EXP-021) |
| 20 | Financial | Binance trades | binance.com | Unlimited | Tick-level | ✅ | **NONE** |

### Data We Do NOT Have (Gaps)

| Domain | What's needed | Why unavailable | Workaround |
|--------|--------------|-----------------|------------|
| **Therapy transcripts** | Session-level therapist-client time series | Privacy/IRB restrictions | Alexander Street Press (institutional access) or EXP-019 simulation |
| **Social media feeds** | Raw algorithmic feed → user behavior coupling | Platform walled gardens | DSA transparency reports (quarterly, coarser) |
| **Cancer progression** | Tumor Pe trajectory over time in individual patients | Clinical data, IRB | TCGA genomic snapshots (no temporal resolution) |
| **Neural plasticity longitudinal** | Same brain, repeated EEG over months during learning | Requires prospective study | Cross-sectional proxy from OpenNeuro |
| **Cult/radicalization** | Real-time engagement → belief drift | Ethical/access barriers | Simulate via EXP-019 with high-O conditions |
| **BCI coupling** | Direct neural interface → user state | Experimental, restricted | Simulated BCI data (EXP-010 protocol) |
| **Industrial control** | SCADA → process coupling | Proprietary/security | Simulated process data |
| **Addiction trajectory** | Real-time gambling/substance → behavior coupling | Clinical, IRB | Macro proxy from public health data |
| **Democratic backsliding** | Policy → institutional response time series | No standardized dataset | V-Dem database (annual, coarse) + news event coding |
| **Dark matter halos** | Simulation time series of halo coupling | Compute-intensive | IllustrisTNG public snapshots (coarse) |
| **Magnetospheric substorms** | Solar wind → magnetosphere coupling | SuperMAG exists but complex | Start with OMNI solar wind data (NASA, public) |
| **Biofilm dynamics** | Real-time biofilm growth coupling | Lab-specific, no public DB | Literature extraction (meta-analysis) |

---

## PHASE 2 EXECUTION PLAN

### Priority Order (by information value × accessibility)

| Priority | Domain | Weeks | Why first |
|----------|--------|-------|-----------|
| **P1** | Power grid (2A) | 1-2 | Method validation — PINN designed for this exact system |
| **P2** | Epidemic (2C) | 2-3 | Tests R₀ = Pe claim directly, huge dataset, fast compute |
| **P3** | EEG neural (2B) | 3-4 | Highest impact if gauge projections match brain states |
| **P4** | Climate (2E) | 4-5 | Tests tipping cascade predictions, politically relevant |
| **P5** | Seismic (2D) | 5-6 | Tests Kramers escape prediction with real fault data |
| **P6** | Financial (2G) | 6-7 | Tests market coupling topology during normal vs. crash |
| **P7** | Protein (2F) | 7-8 | Replication of Paper 129 with full database |

### Cross-Substrate Gauge Test (Phase 2H — Week 8-10)

After all domains are measured:

1. Compile (α₀, β, topology) for every domain
2. Build topology similarity matrix across all substrates
3. For each cross-domain pair with similar Pe but different substrate:
   - Test: does Sp(2,R) transformation connect their Ĥ functions?
4. **Grand kill condition:** If coupling topologies from power grids, brains,
   epidemics, earthquakes, climate, markets, and chatbots CANNOT be connected
   by a common gauge structure — the universality is coincidence, not geometry.
5. **Grand confirmation:** If they CAN be connected — Pe is a genuine universal
   transport parameter with gauge structure, and the (3,2) interpretation
   is empirically grounded across seven substrates on three continents.

---

## HANDOFF CHECKLIST

### For the implementer — what you need to do:

**Environment setup:**
```bash
pip install torch deepxde sentence-transformers datasets scipy obspy mne
# obspy = seismic data access
# mne = EEG data processing
```

**Data downloads (one-time, ~50 GB total):**
```bash
# 1. Power grid frequency (26.5 GB)
# Download from https://osf.io/m43tg/ — click "Download as zip" or use osfclient
pip install osfclient
osf -p m43tg clone power-grid-data

# 2. WildChat (~10 GB)
python -c "from datasets import load_dataset; load_dataset('allenai/WildChat-1M')"

# 3. LMSYS (~5 GB)
python -c "from datasets import load_dataset; load_dataset('lmsys/lmsys-chat-1m')"

# 4. PhysioNet EEG (~1.5 GB)
wget -r -N -c -np https://physionet.org/files/eegmmidb/1.0.0/

# 5. JHU COVID-19 (~500 MB)
git clone https://github.com/CSSEGISandData/COVID-19.git

# 6. OWID COVID-19 + mobility (~200 MB)
git clone https://github.com/owid/covid-19-data.git

# 7. NOAA CO₂ + GISTEMP (~10 MB)
curl -O https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_mm_mlo.csv
curl -O https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv

# 8. Sea ice index (~100 MB)
# Download from https://nsidc.org/data/seaice_index

# 9. Seismic data — use ObsPy to fetch specific events
# No bulk download needed — query per fault system

# 10. Protein folding — manually download from KineticDB/PFDB
# Small datasets, ~1 MB each
```

**PINN architecture (shared across all domains):**
- Input dimensionality varies by domain (see §3.2 above)
- Core architecture identical: 3 layers × 128 units, tanh, FP constraint
- λ schedule: 1.0 → 10.0 over training
- For physical oscillator data (grid, EEG, seismic): use Kuramoto-form ODE constraint
- For behavioral data (chatbot, epidemic, climate): use FP-form PDE constraint

**Key files to read before starting:**
- `private/notes/math-apparatus-guide.md` §58N (full PINN protocol)
- `private/notes/math-apparatus-guide.md` §58L (gauge projections — what to test for)
- `papers-active/paper131-kramers-unification.md` (R₀ = Pe claim, tipping elements)
- `papers-active/paper136-abiogenesis-pe-transition.md` (protein folding Pe)
- `ops/lab/experiments/EXP-019-cross-domain-pe-protocol.md` (AI-to-AI controlled data)

**Success = a paper.** If Phase 2H shows gauge structure across ≥3 substrates,
that is Paper 132 (Universal Transport via Pe Field Dynamics). If it doesn't,
that's an honest null result that correctly bounds the framework's scope.

---

## 7. References

1. Hwang, Jo, Kim, "Data-driven inference of coupling functions in oscillatory systems via physics-informed neural networks," Phys. Rev. Research 8, 013259, 2026.
2. Riedel-Kruse, Oates et al., "Nonreciprocal synchronization in embryonic oscillator ensembles," PNAS 121(35), 2024.
3. Raissi, Perdikaris, Karniadakis, "Physics-informed neural networks," J. Comput. Phys. 378, 2019.
4. Zhao et al., "WildChat: 1M ChatGPT Interaction Logs in the Wild," ICLR 2024.
5. Zheng et al., "LMSYS-Chat-1M: A Large-Scale Real-World LLM Conversation Dataset," ICLR 2024.
6. Gorjão et al., "Open database analysis of scaling and spatio-temporal properties of power grid frequencies," Nat. Commun. 11, 6362 (2020).
7. Goldberger et al., "PhysioBank, PhysioToolkit, and PhysioNet," Circulation 101(23), e215 (2000).
8. Dong et al., "COVID-19 Dashboard," Lancet Infect. Dis. 20(5), 533 (2020). [JHU CSSE]
9. Bogatyreva et al., "KineticDB: a database of protein folding kinetics," Nucleic Acids Res. 37, D342 (2009).
10. Ntakaris et al., "Benchmark dataset for mid-price forecasting of limit order book data," J. Forecast. 37(8), 852 (2018). [FI-2010]

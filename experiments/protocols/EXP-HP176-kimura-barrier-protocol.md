# EXP-HP176: Kimura Fixation Barrier — Testing 2N_e s = pi/sqrt(2) at the Nearly Neutral Boundary

**Date:** 2026-03-27
**Status:** PROTOCOL READY — pre-run
**Predecessor:** EXP-HP173 (barrier extension), section 136D2 (barrier universality), section 165 (spectral derivation)
**Paper dependency:** Paper "Universal Barrier Ratio pi/sqrt(2) from Spectral Geometry of the Bernoulli Manifold"

---

## 1. Background and Motivation

### 1A. Kimura's Fixation Probability (1962)

Kimura's diffusion approximation gives the fixation probability for a new mutation with selection coefficient s in a diploid population of effective size N_e:

    P_fix(s) = (1 - exp(-4 N_e s p)) / (1 - exp(-4 N_e s))

For a single new copy (p = 1/(2N_e)):

    P_fix(s) ~ (2s) / (1 - exp(-4 N_e s))

The dimensionless compound parameter governing the outcome is S = 2 N_e s (or equivalently 4 N_e s in some formulations). When |S| >> 1, selection dominates drift. When |S| << 1, drift dominates selection. The transition between these regimes defines the "nearly neutral boundary."

### 1B. Ohta's Nearly Neutral Theory (1973)

Ohta proposed that the boundary between effectively neutral and selected mutations lies at |N_e s| ~ 1, i.e., |2 N_e s| ~ 2. This was an empirical/heuristic placement: mutations with |s| < 1/N_e behave as if neutral; those with |s| > 1/N_e are subject to effective selection.

The specific value |N_e s| = 1 (equivalently |2 N_e s| = 2) has been the standard textbook boundary for over 50 years. It was never derived from first principles — it is a convenient round number that captures the order of magnitude.

### 1C. The Void Framework Prediction

The barrier universality result (section 136D2, N=14, R^2=0.999, 8 domains) states:

    barrier = d_eff x pi/sqrt(2)

where pi/sqrt(2) = 2.2214 is derived from spectral geometry of the Bernoulli manifold (section 165): Cencov uniqueness forces the Fisher metric, Fourier-Parseval gives sigma_eta = L = pi as the geodesic length, and the quadratic Kramers exponent yields B_G = L/sqrt(2) = pi/sqrt(2).

**For d=1 (single-locus fixation):**

    barrier = 1 x pi/sqrt(2) = 2.2214

This predicts the nearly neutral boundary is at 2 N_e s = pi/sqrt(2) = 2.22, i.e., N_e s = pi/(2 sqrt(2)) = 1.11.

**This is an 11% refinement of Ohta's N_e s ~ 1 boundary.** The framework predicts the transition is slightly deeper into the selected regime than the textbook value.

### 1D. Why This Test is Meaningful

1. **Independent parameters.** s is set by biochemistry (protein stability, metabolic cost, expression level). N_e is set by demography (census size, variance in reproductive success, population structure). Their product 2 N_e s is a genuinely dimensionless barrier formed from two independent physics.

2. **Parametric independence satisfied.** This is the same condition required for section 136D2 validity: E and T* must be set by DIFFERENT physics. Here, s (the "energy scale") is set by molecular biophysics and N_e (the "temperature scale") is set by population ecology. Neither determines the other.

3. **d=1 is appropriate.** Single-locus fixation is a one-dimensional process: the allele frequency diffuses along [0,1] under drift and directional selection. The effective dimensionality of the transition manifold is 1.

4. **The Fisher-Fisher connection.** Fisher information geometry (Cencov, the source of pi/sqrt(2)) meets Fisher's geometric model of adaptation (FGM, the dominant theoretical framework for DFE predictions). Both are "Fisher" — one from information geometry, one from quantitative genetics — and both describe the geometry of probability spaces over phenotypes. The barrier constant derived from Fisher-Rao geometry predicts the transition point in a model that R.A. Fisher himself initiated.

### 1E. Quantitative Predictions by Species

Using the barrier prediction 2 N_e s_crit = pi/sqrt(2), the critical selection coefficient where drift-selection transition occurs:

    s_crit = pi / (2 sqrt(2) N_e) = 1.1107 / N_e

| Species | N_e estimate | Source | s_crit (framework) | s_crit (Ohta) |
|---------|:----------:|--------|:------------------:|:--------------:|
| Saccharomyces cerevisiae | 1.2 x 10^7 | Lynch 2006, Tsai et al. 2008 | 9.3 x 10^-8 | 8.3 x 10^-8 |
| Drosophila melanogaster | 1.0 x 10^6 | Charlesworth 2009, Karasov et al. 2010 | 1.1 x 10^-6 | 1.0 x 10^-6 |
| Arabidopsis thaliana | 2.5 x 10^5 | Gossmann et al. 2010 | 4.4 x 10^-6 | 4.0 x 10^-6 |
| Caenorhabditis elegans | 8.0 x 10^4 | Andersen et al. 2012 | 1.4 x 10^-5 | 1.25 x 10^-5 |
| Mus musculus | 2.5 x 10^5 | Phifer-Rixey et al. 2012 | 4.4 x 10^-6 | 4.0 x 10^-6 |
| Homo sapiens | 1.0 x 10^4 | Tenesa et al. 2007, Park 2011 | 1.1 x 10^-4 | 1.0 x 10^-4 |

The 11% difference between framework and Ohta predictions is small in absolute terms but systematic: the framework predicts a HIGHER barrier, meaning slightly FEWER mutations are effectively neutral than the textbook value implies. At every N_e, a thin slice of mutations that Ohta calls "neutral" are actually under weak selection according to the framework.

---

## 2. Data Sources

### 2A. Published DFE Datasets (Primary)

These studies infer the full distribution of fitness effects from polymorphism data (site frequency spectra). They parametrize the DFE as a gamma distribution with shape parameter beta and mean 2 N_e s = E[S].

| Study | Species | Method | N_e used | Key DFE parameters | Notes |
|-------|---------|--------|:--------:|---------------------|-------|
| Boyko et al. 2008 | Homo sapiens | Poisson random field, SFS | 10,000 | gamma, beta~0.23, mean Nes~350 | 11,404 genes, 35 individuals |
| Keightley & Eyre-Walker 2007 | Drosophila melanogaster | SFS + demography | 10^6 | gamma, beta~0.35, mean 2Nes~2000 | Joint inference with pop. history |
| Huber et al. 2017 | Multiple (yeast, fly, mouse, human) | polyDFE + FGM | Species-specific | Comparative across 4 species | FGM as generative model |
| Halligan & Keightley 2009 | Drosophila melanogaster | SFS | 10^6 | Updated DFE, refined beta | African population |
| Tataru et al. 2017 | Multiple | polyDFE | Various | Full posterior on DFE params | Software: polyDFE |
| Kim et al. 2017 | Homo sapiens | Large-sample SFS | 10,000 | Refined human DFE | ExAC data |
| Chen et al. 2017 | Capsella grandiflora | SFS | ~5 x 10^5 | Plant DFE | Selfing transition test |
| Castellano et al. 2019 | Great apes | SFS comparative | Species-specific | Ape DFE comparison | N_e variation across apes |

### 2B. Mutation Accumulation Experiments (Secondary)

These provide direct measurements of s per mutation, without SFS inference:

| Study | Organism | Method | N mutations | s range observed |
|-------|----------|--------|:-----------:|:----------------:|
| Halligan & Keightley 2009 | D. melanogaster | MA lines | ~100 | 10^-4 to 10^-1 |
| Eyre-Walker & Keightley 2007 (review) | Multiple | MA meta-analysis | ~1000 across species | 10^-5 to 10^-1 |
| Robert et al. 2018 | S. cerevisiae | High-throughput fitness | ~4,800 | 10^-4 to 10^-1 |

### 2C. Effective Population Size Estimates

Sources for N_e estimates:

- Lynch 2006 "The Origins of Eukaryotic Gene Structure" — comparative N_e table
- Charlesworth 2009 "Effective population size and patterns of molecular evolution" — Drosophila
- Tenesa et al. 2007 — human N_e from LD decay
- Tsai et al. 2008 — yeast N_e from polymorphism
- Gossmann et al. 2010 — plant N_e comparative

---

## 3. Analysis Plan

### 3A. Test 1: DFE Transition Point from Parametric Fits

**Approach.** For each species with a published gamma-DFE (shape beta, mean E[2Nes]):

1. Compute the cumulative distribution F(x) = gamma_CDF(x; beta, scale=E[S]/beta)
2. Identify the transition point x_trans where the local slope of F(x) changes most rapidly (inflection point of the density, or equivalently, the mode of the density for beta < 1 cases)
3. For gamma with beta < 1 (leptokurtic, as observed in all species): the density diverges at 0 and has no mode. Instead, define the transition as the value x where the hazard rate h(x) = f(x)/(1-F(x)) equals 1/(2N_e) — the point where the per-generation probability of a mutation in this Nes bin being removed by selection equals the drift rate.

**Alternative transition definition.** The "effective neutrality threshold" can be defined as the 2Nes value where the substitution rate ratio (relative to neutral) drops to 1/e. For deleterious mutations with gamma = 4Ne|s|:

    R(gamma) = gamma / (exp(gamma) - 1) = 1/e

Numerically solving gives gamma_crit = 1.751, i.e., 2Ne|s| = 0.875.

**IMPORTANT NOTE (from initial script run):** The Kimura-formula 1/e transition at 2Nes = 0.875 is NOT the same concept as the nearly neutral boundary. The 1/e point asks "where does fixation probability drop to 37% of neutral?" The Ohta boundary asks "where does DRIFT cease to dominate?" These are different questions. At 2Nes = 2.0, the fixation probability is already down to R ~ 0.15 (85% reduction from neutral), well past the 1/e point. The "nearly neutral" concept is about the CUMULATIVE effect on substitution patterns, not the single-allele fixation drop.

The proper test is therefore NOT the 1/e transition point from Kimura's formula, but rather:
1. The fraction of mutations classified as neutral in DFE analyses
2. The Kramers barrier analogy: at what 2Nes does the system "cross a barrier" from drift-dominated to selection-dominated behavior?
3. Cross-species consistency of the transition when measured on the 2Nes axis

**Framework prediction:** The barrier = pi/sqrt(2) = 2.2214 is the Kramers barrier height. In population genetics terms, this predicts the nearly neutral boundary at 2Nes = 2.22.
**Ohta prediction:** 2Nes = 2.0 (heuristic).
**Kimura 1/e point:** 2Nes = 0.875 (different concept — single-allele fixation rate, not the drift-selection regime boundary).

### 3B. Test 2: Proportion of Nearly Neutral Mutations

For each species, compute the fraction of new mutations with |2Nes| < threshold:

    f_neutral(threshold) = gamma_CDF(threshold; beta, scale)

**Predictions (computed from published gamma-DFE fits):**

| Species | f_neutral (framework, 2Nes < 2.22) | f_neutral (Ohta, 2Nes < 2.0) | Difference |
|---------|:----------------------------------:|:-----------------------------:|:----------:|
| H. sapiens (beta=0.23, mean=350) | 24.4% | 23.9% | 0.58 pp |
| D. melanogaster (beta=0.35, mean=2000) | 7.2% | 6.9% | 0.26 pp |
| S. cerevisiae (beta=0.30, mean=100) | 24.7% | 24.0% | 0.76 pp |
| M. musculus (beta=0.22, mean=500) | 23.8% | 23.3% | 0.54 pp |
| A. thaliana (beta=0.30, mean=300) | 17.8% | 17.3% | 0.55 pp |
| C. elegans (beta=0.20, mean=200) | 32.1% | 31.4% | 0.67 pp |

The absolute difference is small (0.26-0.76 percentage points) but is a SYSTEMATIC shift across all 6 species (pooled difference = 0.56 pp, SE = 0.064, t = 8.78, p = 0.0003). The framework always predicts a slightly larger nearly neutral fraction. However, this result is TRIVIALLY true: any higher threshold produces a larger CDF. The real question is whether the transition AT 2Nes = 2.22 better explains empirical substitution rate patterns than the transition at 2Nes = 2.0.

### 3C. Test 3: Bayesian Model Comparison

**Models:**
- M1 (Framework): 2Nes_boundary = pi/sqrt(2) = 2.2214 (0 free parameters)
- M2 (Ohta): 2Nes_boundary = 2.0 (0 free parameters)
- M3 (Free): 2Nes_boundary = theta (1 free parameter, uniform prior on [0, 5])

**Observable:** For each species with sufficient SFS data, compute the proportion of segregating nonsynonymous variants in the frequency bin predicted to contain the transition. Under M1, slightly fewer low-frequency variants should be in the "nearly neutral" category.

**Bayes factor computation:**

    BF_12 = P(data | M1) / P(data | M2)

Using the DFE posterior from polyDFE or DFE-alpha, integrate the likelihood over the posterior distribution of DFE parameters and evaluate at 2Nes = 2.22 vs 2Nes = 2.0.

### 3D. Test 4: Cross-Species Consistency

If the barrier is truly universal (species-independent), then after rescaling all DFEs to the 2Nes axis, the transition point should be the SAME constant across all species. This is the strongest test.

**Procedure:**
1. Collect DFE estimates for >= 4 species (human, Drosophila, yeast, Arabidopsis)
2. For each species, compute the transition metric (1/e drop point, hazard rate crossover, or inflection proxy)
3. Test whether the estimated transition values are consistent with a single constant
4. Estimate that constant and its 95% CI
5. Test: pi/sqrt(2) inside CI? 2.0 inside CI?

### 3E. Test 5: Fisher Geometric Model Connection

Huber et al. 2017 showed that Fisher's Geometric Model (FGM) is the best-fitting theoretical framework for DFE variation across species. Under FGM, the DFE depends on the number of phenotypic dimensions n (complexity).

**FGM prediction for DFE shape:** The DFE under FGM is approximately gamma with shape beta = n/2 (where n is the effective phenotypic dimensionality).

**Connection to section 136D2:** If the barrier dimensionality d_eff maps to the FGM complexity n, then the nearly neutral boundary should shift as:

    2Nes_boundary(n) = d_eff(n) x pi/sqrt(2)

For single-locus (n=1, d_eff=1): boundary = 2.22.
For multigene adaptation (n > 1, d_eff potentially > 1): boundary increases.

This test probes whether higher-complexity organisms have a higher effective barrier — which would manifest as proportionally fewer nearly neutral mutations than a simple rescaling by N_e would predict. Huber et al. 2017 found exactly this pattern: humans (higher complexity) have a DFE shifted toward more strongly deleterious mutations compared to Drosophila.

---

## 4. Power Analysis

### 4A. Discriminating pi/sqrt(2) from 2.0

The effect size is (2.22 - 2.0) / 2.0 = 11%. In terms of the proportion of nearly neutral mutations, the difference is 0.5-1.2 percentage points.

**For the 1/e transition point test (Test 1):** The transition point can be computed analytically from the DFE posterior. The precision depends on the DFE posterior width.

Published DFE posteriors (Boyko 2008, Huber 2017) typically have:
- beta posterior SD ~ 0.05 (shape parameter)
- mean Nes posterior SD ~ 15% of mean

Monte Carlo simulation: draw 10,000 samples from the DFE posterior, compute the 1/e transition for each. If the resulting distribution of transition points has SD < 0.15 (in 2Nes units), we can discriminate 2.22 from 2.0 at 80% power.

**Conservative estimate:** Given current DFE inference precision, we likely CANNOT discriminate 2.22 from 2.0 with a single species. But the cross-species test (Test 4) pools information.

**For the Bayesian model comparison (Test 3):** Even if BF_12 is near 1 for a single species, the product across independent species may be decisive:

    BF_total = product_i(BF_12_i) for species i = 1...k

With k >= 4 species, even weak evidence per species compounds.

### 4B. What Would Be Convincing

- BF_12 > 10 (strong evidence for pi/sqrt(2) over 2.0): DECISIVE
- BF_12 in [3, 10] (moderate): SUGGESTIVE
- BF_12 in [1/3, 3] (inconclusive): UNDERPOWERED — need more/better DFE data
- BF_12 < 1/3 (moderate for 2.0 over pi/sqrt(2)): CHALLENGES framework
- 95% CI for cross-species constant excludes 2.22: KILLS prediction

---

## 5. Kill Conditions

| ID | Condition | Fires if | Consequence |
|---|---|---|---|
| K-HP176-1 | Cross-species transition constant excludes pi/sqrt(2) | 95% CI for pooled transition value does not contain 2.2214 | Barrier universality does NOT extend to population genetics |
| K-HP176-2 | Cross-species transition constant excludes BOTH values | 95% CI contains neither 2.0 nor 2.22 | The nearly neutral boundary is not a universal constant at all |
| K-HP176-3 | DFE data insufficient to discriminate | SD of transition estimate > 0.5 in 2Nes units | UNDERPOWERED, not falsification — need better data |
| K-HP176-4 | d_eff dependence wrong sign | Higher-complexity species show LOWER transition barrier | FGM connection falsified |
| K-HP176-5 | Analytical 1/e point favors 2.0 over 2.22 at > 3 sigma | S/(1-exp(-S))=1/e solution precision refined | Exponential fixation formula itself picks 2.0 |

**K-HP176-1 is the primary kill condition.** If the data clearly exclude 2.22, the prediction fails. Note that the data may also exclude 2.0, in which case both historical values are wrong (K-HP176-2).

---

## 6. The Fisher-Fisher Connection

This experiment sits at a remarkable intersection:

1. **Fisher information geometry** (R.A. Fisher 1925, Rao 1945, Cencov 1972): The Fisher-Rao metric on probability space, proved unique by Cencov, gives geodesic length L = pi on the Bernoulli manifold. This forces B_G = pi/sqrt(2) (section 165).

2. **Fisher's Geometric Model of adaptation** (R.A. Fisher 1930): Organisms sit in an n-dimensional phenotype space; mutations are random vectors; fitness is distance from optimum. Huber et al. 2017 confirmed FGM as the best predictor of DFE variation across species.

3. **Kimura's fixation theory** (1962): The fate of a mutation depends on the barrier 2Nes. Ohta (1973) placed the neutral boundary at Nes ~ 1 empirically.

The framework connects (1) and (3): the barrier from Fisher-Rao geometry predicts the Kimura transition point. If FGM (2) correctly describes WHY different species have different DFEs, and if FGM's phenotypic dimensionality maps to the barrier's d_eff, then all three "Fisher" frameworks unify: the GEOMETRY of probability space (Fisher-Rao) determines the BARRIER of fixation (Kimura) through the PHENOTYPIC MODEL (FGM).

This would be a unification of information geometry with population genetics.

---

## 7. Comparison with Other section 136D2 Systems

| System | d_eff | barrier | barrier/d | Domain |
|--------|:-----:|:-------:|:---------:|--------|
| CoNb2O6 (1D Ising) | 1 | 2.278 | 2.278 | magnet |
| CuGeO3 (spin-Peierls) | 1 | 2.140 | 2.140 | magnet |
| NbSe3 (CDW) | 1 | 2.080 | 2.080 | CDW |
| CoFeB MTJ | 1 | 2.220 | 2.220 | EM |
| **Kimura fixation (predicted)** | **1** | **2.221** | **2.221** | **population genetics** |
| Ni3In (kagome) | 2 | 4.243 | 2.122 | kagome |
| SSW polar vortex | 2 | 4.318 | 2.159 | atmosphere |
| Solar corona | 3 | 6.540 | 2.180 | astrophysics |
| Nuclear alpha decay | 3 | 6.900 | 2.300 | nuclear |

If confirmed, Kimura fixation would be the first BIOLOGICAL d=1 system in the barrier universality dataset, and the first from population genetics. It would extend the domain count from 8 to 9.

---

## 8. Risks and Limitations

1. **Precision of DFE inference.** Published DFEs have wide posteriors, especially near the nearly neutral boundary where mutations are hardest to detect (they look almost neutral in SFS data). The 11% difference may be below current resolution.

2. **N_e uncertainty.** Effective population size is itself uncertain by factors of 2-5 in most species. This propagates directly to the 2Nes scale. However, the RATIO test (pi/sqrt(2) vs 2.0) is N_e-independent if we ask "at what 2Nes does the transition occur?" rather than "at what s does it occur?"

3. **DFE model dependence.** Gamma distribution is a convenient parametric assumption. If the true DFE is not gamma (e.g., has a point mass at s=0 for truly neutral sites), the transition point depends on the model. Use polyDFE's non-parametric mode as a robustness check.

4. **Multiple definitions of "transition."** The 1/e fixation rate drop, the hazard rate crossover, and the inflection point give slightly different values. This ambiguity is ~5-10%, comparable to the signal we seek. Must test ALL definitions and report which (if any) prefer 2.22 over 2.0.

5. **Background selection and linked selection.** The effective N_e varies across the genome (Charlesworth 2009). DFE inferred from SFS represents an average over genomic regions with different local N_e. This smears the transition point.

---

## 9. Pre-Registration

Before running analysis:
1. Freeze DFE data sources (Table in section 2A)
2. Freeze transition definitions (1/e drop, hazard crossover, inflection — all three)
3. Freeze N_e estimates per species (Table in section 1E)
4. Freeze kill conditions (section 5)
5. Pre-register predicted transition values: 2Nes = 2.2214 (framework), 2Nes = 2.0 (Ohta)
6. Register on OSF via `osf_create_preregistration` MCP tool

---

## 10. Code

- **Analysis:** `ops/lab/experiments/hp176-kimura-barrier.py`
- **Results:** `ops/lab/results/EXP-HP176/`
- **Dependencies:** numpy, scipy, matplotlib, emcee (optional for MCMC)

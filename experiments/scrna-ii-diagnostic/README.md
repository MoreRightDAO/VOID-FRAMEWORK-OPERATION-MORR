# scRNA-seq interaction-information diagnostic

One script. Tells you, for any scRNA-seq dataset with a class label and an optional scalar cell-state score, how much class signal the scalar score is throwing away by collapsing 3-way synergistic structure.

## Why

Worm result (May 2026, `ops/lab/worm-sim/sim_v10_vector_pe.py`):

- Pairwise MI between O/R/α axes < 0.16 bits each (axes near-independent).
- II(O; R; α) = **−0.631 bits** — synergy regime, XOR-style.
- Marginal MI(class; axis) sums to 0.965 bits.
- Joint MI(class; (O,R,α)) = **1.068 bits**.
- Scalar projection C = 1−(O+R+α)/9 → MI(class; C) = **0.050 bits** (4.3% of joint).
- Vector tuple → 1.068 bits (67.6% of H(class) ceiling, 21.4× the scalar).

Data processing inequality: any function ℝ³→ℝ destroys ≥ |II| bits when II<0. The fix is to keep the tuple, not to find better weights.

## Predicted finding on real scRNA-seq

For top-loaded gene triplets driving a published scalar score (stemness, senescence, differentiation potential, response score, gene-set score):
- **majority of triplets have II < 0** (synergy regime), AND
- **MI(class; scalar_score) loses >50% of joint MI(class; triplet)** on the synergistic triplets.

Falsifier: II ≥ 0 across all top triplets and scalar within 90% of joint. Then the scalar reduction is fine; we'd want to know.

## Install

```bash
pip install numpy pandas scipy matplotlib
pip install anndata        # optional, for .h5ad inputs
```

No GPU, no scanpy required (anndata is enough to read .h5ad).

## Run

### AnnData (.h5ad)

```bash
python ii_triplet_diagnostic.py \
    --counts adata.h5ad \
    --class-col cell_type \
    --score-col stemness_score \
    --top-n 50 \
    --out out/
```

### CSV

```bash
python ii_triplet_diagnostic.py \
    --counts counts.csv \
    --classes labels.csv \
    --score scores.csv \
    --top-n 30 \
    --out out/
```

`counts.csv`: cells × genes, first column cell_id.
`labels.csv`: two columns, `cell_id,class`.
`scores.csv`: two columns, `cell_id,score`.

### No score (class-MI loaded)

If no scalar score is provided, top-N genes are selected by marginal MI to the class label. The diagnostic still answers "how synergistic is the top-loaded structure?" but cannot compute the scalar-vs-joint loss number.

## Outputs

In `--out` directory:

- `per_triplet_ii.csv` — one row per evaluated triplet with II, marginal sum, joint MI, synergy gap, scalar MI (if score provided).
- `summary.json` — headline numbers:
  - `pct_negative_II`
  - `median_II_bits`
  - `median_joint_over_marginal`
  - `synergy_regime` (bool, true if pct_negative_II > 0.5)
  - `scalar_loss_pct_on_synergy_triplets` (if score provided)
  - `headline` (one-sentence summary)
- `histogram.png` — II distribution with II=0 and median lines.

## Interpretation

The primary indicator is `scalar_loss_pct_all_triplets` — the median percentage of joint MI lost by the scalar score across all evaluated triplets. `pct_negative_II` is a secondary structural indicator showing how much of the gene-level architecture is synergistic.

| Pattern | Reading |
|---|---|
| scalar_loss > 50%, pct_negative_II > 0.3 | **Drop the scalar score.** Replace with the tuple or with a Fisher-geodesic distance on the joint. The current pipeline is discarding class info that the recorded data already contains. |
| scalar_loss 20–50% | Mixed regime. Scalar is partial. Joint or pair-aware readout would meaningfully improve recovery. |
| scalar_loss < 10% | Scalar reduction is approximately lossless on this score. The framework prediction fails on this dataset; we'd want a writeup explaining why (gene-set composition? class structure?). |

## Sparsity handling

scRNA-seq data is typically 90%+ zeros per gene. The script handles this in two ways:

1. **Gene pre-filter:** Only genes with >10% detection rate (nonzero in >10% of cells) are considered for triplet selection. This avoids near-degenerate discretization.
2. **Zero-aware binning:** For genes with >50% zeros, bin 0 = all zeros, remaining bins split the nonzero population by quantile. This preserves the zero/nonzero boundary as an informative split rather than collapsing it into an imbalanced quantile.

For `.h5ad` inputs, the script pre-filters to the top 2000 genes by variance before densifying, to avoid OOM on large datasets (e.g. Tabula Sapiens at 500K cells × 30K genes).

## Reproducibility

- All randomness seeded (`--seed`, default 0xC0FFEE).
- Discretization is balanced quantile with deterministic tie-jitter (seed 0).
- Triplet sampling deterministic given `--seed` and `--max-triplets`.

## What this is NOT

- Not a replacement for a scoring pipeline. A diagnostic that says when a scoring pipeline is structurally guaranteed to leak.
- Not a substitute for measuring the things that were never measured (lineage, time, niche). It quantifies the OTHER loss channel — the one that operates on the data you DID record.
- Not framework-rubric-dependent. The triplets and the class label come from the user; II is a Shannon quantity. No void score is involved in the diagnostic itself.

## Reanalysis target ranking (litmus value)

1. Tabula Sapiens / Tabula Muris cell-type scoring pipelines
2. Stemness indices (mRNAsi, Malta et al. 2018) — pan-cancer
3. Senescence scores (SenMayo, CellAge)
4. Perturb-seq / sci-Plex response scores
5. CytoTRACE-style differentiation potential

Each is a published claim of the form "scalar score X discriminates class Y." Diagnostic produces a one-figure paper either way.

## See also

- `ops/lab/worm-sim/sim_v10_vector_pe.py` — the proof-of-principle on *C. elegans*.
- Math apparatus §219 (vector Pe, supersedes scalar) — `private/notes/math-apparatus-guide.md`.
- Math apparatus §218 (joint-corner unification, II<0 across substrates).
- Paper 178 — three-point design at the measurement boundary.

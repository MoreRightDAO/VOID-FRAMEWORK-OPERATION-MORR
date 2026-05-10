"""
ii_triplet_diagnostic.py — interaction information on scRNA-seq triplets.

Forced by sim_v9f / sim_v10 worm result:
  When II(G1; G2; G3) < 0 (synergy regime), any scalar score f(G1, G2, G3)
  loses class signal by data processing inequality. The fix is to keep the
  tuple, not to find better weights. This script measures the loss directly
  on a user-supplied scRNA-seq dataset, without committing to any scoring
  pipeline.

Inputs
------
  --counts        path to a .h5ad (AnnData) OR .csv expression matrix
                  (cells x genes; first column = cell_id when .csv)
  --classes       path to a .csv of cell_id,class_label (or AnnData .obs col
                  via --class-col)
  --score         OPTIONAL path to .csv of cell_id,scalar_score, OR an
                  AnnData .obs column via --score-col. If provided, top-N
                  loaded genes are pulled by Spearman(gene, score). If absent,
                  top-N most class-discriminative genes (mutual information
                  to class label) are used.
  --top-n         number of top-loaded genes to scan triplets over (default 30)
  --bins          discretization bins per gene (default 3, balanced quantile)
  --max-triplets  cap triplets evaluated to keep runtime sane (default 4000)
  --out           output directory (default ./out)

Outputs
-------
  per_triplet_ii.csv           one row per evaluated triplet, with:
                                  G1, G2, G3, II, MI_marginal_sum,
                                  MI_joint, MI_scalar (if --score given)
  summary.json                 headline numbers
  histogram.png                II distribution

Headline numbers
----------------
  pct_negative_II              fraction of triplets with II < 0
  median_II                    median II in bits
  median_joint_over_marginal   median MI(class; joint) / sum_marginal
  scalar_loss_pct              if --score: median (1 - MI_scalar/MI_joint)*100
                               on II<0 triplets — "% of joint signal lost
                               by collapsing to the scalar score"

Run
---
  python ii_triplet_diagnostic.py \
      --counts adata.h5ad --class-col cell_type \
      --score-col stemness_score --top-n 50 --out out/

  # CSV mode
  python ii_triplet_diagnostic.py \
      --counts counts.csv --classes labels.csv --score scores.csv \
      --top-n 30 --out out/

No fitted constants. Reproducible (--seed). Single file.
"""
from __future__ import annotations
import argparse
import json
import sys
from itertools import combinations
from pathlib import Path

import numpy as np
import pandas as pd

try:
    import anndata as ad  # type: ignore
    _HAVE_AD = True
except ImportError:
    _HAVE_AD = False


def _entropy(counts: np.ndarray) -> float:
    counts = counts[counts > 0]
    if counts.size == 0:
        return 0.0
    p = counts / counts.sum()
    return float(-(p * np.log2(p)).sum())


def mi(x: np.ndarray, y: np.ndarray) -> float:
    """Mutual information I(X;Y) in bits. Both x,y are integer-coded."""
    xy = np.stack([x, y], axis=1)
    _, joint = np.unique(xy, axis=0, return_counts=True)
    _, cx = np.unique(x, return_counts=True)
    _, cy = np.unique(y, return_counts=True)
    return _entropy(cx) + _entropy(cy) - _entropy(joint)


def joint_code(*arrs: np.ndarray) -> np.ndarray:
    """Encode a tuple of integer arrays as a single integer code."""
    stacked = np.stack(arrs, axis=1)
    _, inv = np.unique(stacked, axis=0, return_inverse=True)
    return inv


def interaction_information(g1: np.ndarray, g2: np.ndarray, g3: np.ndarray) -> float:
    """
    McGill interaction information:
      II = I(G1;G2) − I(G1;G2 | G3)
    Entropy expansion (Bell/McGill):
      II = H1 + H2 + H3 − H12 − H13 − H23 + H123
    Negative II ⇒ synergy (3-way carries info absent from any pair).
    """
    # H(.) on integer codes
    def H(*arrs):
        code = joint_code(*arrs)
        _, c = np.unique(code, return_counts=True)
        return _entropy(c)

    H1, H2, H3 = H(g1), H(g2), H(g3)
    H12, H13, H23 = H(g1, g2), H(g1, g3), H(g2, g3)
    H123 = H(g1, g2, g3)
    # II = H1+H2+H3 - H12 - H13 - H23 + H123  (Bell/McGill convention)
    return float(H1 + H2 + H3 - H12 - H13 - H23 + H123)


def discretize(x: np.ndarray, bins: int) -> np.ndarray:
    """Zero-aware quantile discretization for sparse data.

    If >50% of values are zero (common in scRNA-seq), zero gets its own bin
    and the remaining bins split the nonzero population by quantile.
    Otherwise, standard balanced-quantile with jitter for tie-breaking.
    """
    x = np.asarray(x, dtype=float)
    if np.allclose(x.std(), 0.0):
        return np.zeros(x.shape[0], dtype=int)
    zero_frac = (x == 0).mean()
    if zero_frac > 0.5 and bins >= 2:
        # Zero-aware: bin 0 = zeros, remaining bins split nonzero tail
        out = np.zeros(x.shape[0], dtype=int)
        nz = x != 0
        if nz.sum() > 0:
            nz_vals = x[nz]
            rng = np.random.default_rng(0)
            nz_vals = nz_vals + rng.normal(0, 1e-9 * (nz_vals.std() + 1e-12), nz_vals.shape)
            nz_bins = bins - 1  # remaining bins for nonzero
            if nz_bins >= 2:
                qs = np.quantile(nz_vals, np.linspace(0, 1, nz_bins + 1)[1:-1])
                out[nz] = np.digitize(nz_vals, qs).astype(int) + 1
            else:
                out[nz] = 1
        return out
    rng = np.random.default_rng(0)
    x = x + rng.normal(0, 1e-9 * (x.std() + 1e-12), x.shape)
    qs = np.quantile(x, np.linspace(0, 1, bins + 1)[1:-1])
    return np.digitize(x, qs).astype(int)


def load_inputs(args) -> tuple[pd.DataFrame, pd.Series, pd.Series | None]:
    """Return (counts_df cells x genes, class_series, score_series_or_None)."""
    counts_path = Path(args.counts)
    if counts_path.suffix == ".h5ad":
        if not _HAVE_AD:
            print("anndata not installed; pip install anndata", file=sys.stderr)
            sys.exit(2)
        a = ad.read_h5ad(counts_path)
        # Pre-filter to top 2000 genes by variance to avoid OOM on large
        # datasets (500K cells × 30K genes = ~60GB dense). We only need
        # top-N (default 30) anyway; 2000 is generous headroom.
        X = a.X
        if hasattr(X, "toarray"):
            # Compute variance on sparse directly (memory-safe)
            from scipy import sparse
            mean = np.asarray(X.mean(axis=0)).ravel()
            var = np.asarray(X.multiply(X).mean(axis=0)).ravel() - mean ** 2
        else:
            X = np.asarray(X)
            var = X.var(axis=0)
        n_keep = min(2000, len(var))
        top_idx = np.argsort(-var)[:n_keep]
        a_sub = a[:, top_idx]
        X_sub = a_sub.X.toarray() if hasattr(a_sub.X, "toarray") else np.asarray(a_sub.X)
        counts = pd.DataFrame(X_sub, index=a.obs_names.astype(str),
                              columns=a.var_names.astype(str)[top_idx])
        if args.class_col is None:
            print("AnnData input requires --class-col", file=sys.stderr)
            sys.exit(2)
        cls = a.obs[args.class_col].astype(str)
        cls.index = cls.index.astype(str)
        score = None
        if args.score_col is not None:
            score = a.obs[args.score_col].astype(float)
            score.index = score.index.astype(str)
    else:
        counts = pd.read_csv(counts_path, index_col=0)
        counts.index = counts.index.astype(str)
        cls_df = pd.read_csv(args.classes)
        cls = pd.Series(cls_df.iloc[:, 1].values, index=cls_df.iloc[:, 0].astype(str).values, name="class")
        score = None
        if args.score is not None:
            sc_df = pd.read_csv(args.score)
            score = pd.Series(sc_df.iloc[:, 1].values.astype(float),
                              index=sc_df.iloc[:, 0].astype(str).values, name="score")

    common = counts.index.intersection(cls.index)
    if score is not None:
        common = common.intersection(score.index)
    if len(common) < 50:
        print(f"only {len(common)} aligned cells; need ≥50", file=sys.stderr)
        sys.exit(2)
    counts = counts.loc[common]
    cls = cls.loc[common]
    if score is not None:
        score = score.loc[common]
    return counts, cls, score


def select_top_genes(counts: pd.DataFrame, cls_int: np.ndarray,
                     score: pd.Series | None, top_n: int, bins: int) -> list[str]:
    """Top genes by Spearman to score (if given), else by marginal MI to class.

    Pre-filters to genes with >10% detection rate (nonzero in >10% of cells)
    to avoid near-degenerate discretization on ultra-sparse genes.
    """
    detection_rate = (counts > 0).mean(axis=0)
    keep = detection_rate[detection_rate > 0.10].index
    if len(keep) < top_n:
        # Relax filter if too few genes survive
        keep = detection_rate[detection_rate > 0].index
    counts = counts[keep]
    if score is not None:
        from scipy.stats import spearmanr
        rho = np.array([spearmanr(counts[g].values, score.values, nan_policy="omit").statistic
                        for g in counts.columns])
        rho = np.nan_to_num(rho, nan=0.0)
        order = np.argsort(-np.abs(rho))
    else:
        marg = []
        for g in counts.columns:
            gi = discretize(counts[g].values, bins)
            marg.append(mi(gi, cls_int))
        order = np.argsort(-np.array(marg))
    return list(counts.columns[order[:top_n]])


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--counts", required=True)
    p.add_argument("--classes", default=None, help="CSV: cell_id,class")
    p.add_argument("--class-col", default=None, help="AnnData .obs column for class")
    p.add_argument("--score", default=None, help="CSV: cell_id,scalar_score")
    p.add_argument("--score-col", default=None, help="AnnData .obs column for scalar score")
    p.add_argument("--top-n", type=int, default=30)
    p.add_argument("--bins", type=int, default=3)
    p.add_argument("--max-triplets", type=int, default=4000)
    p.add_argument("--seed", type=int, default=0xC0FFEE)
    p.add_argument("--out", default="out")
    args = p.parse_args()

    out = Path(args.out); out.mkdir(parents=True, exist_ok=True)
    counts, cls, score = load_inputs(args)
    cls_int = pd.Categorical(cls).codes.astype(int)
    print(f"[load] cells={counts.shape[0]}  genes={counts.shape[1]}  classes={cls.nunique()}")

    top_genes = select_top_genes(counts, cls_int, score, args.top_n, args.bins)
    print(f"[select] top-N={len(top_genes)} genes "
          f"({'score-loaded' if score is not None else 'class-MI loaded'})")

    disc = {g: discretize(counts[g].values, args.bins) for g in top_genes}
    score_disc = discretize(score.values, args.bins) if score is not None else None

    triplets = list(combinations(top_genes, 3))
    rng = np.random.default_rng(args.seed)
    if len(triplets) > args.max_triplets:
        idx = rng.choice(len(triplets), args.max_triplets, replace=False)
        triplets = [triplets[i] for i in idx]
    print(f"[scan] {len(triplets)} triplets")

    rows = []
    for g1, g2, g3 in triplets:
        a, b, c = disc[g1], disc[g2], disc[g3]
        ii = interaction_information(a, b, c)
        marg_sum = mi(a, cls_int) + mi(b, cls_int) + mi(c, cls_int)
        joint = mi(joint_code(a, b, c), cls_int)
        row = {"G1": g1, "G2": g2, "G3": g3,
               "II_bits": ii,
               "MI_marginal_sum": marg_sum,
               "MI_joint": joint,
               "synergy_gap": joint - marg_sum}
        if score_disc is not None:
            row["MI_scalar_score"] = mi(score_disc, cls_int)
        rows.append(row)

    df = pd.DataFrame(rows)
    df.to_csv(out / "per_triplet_ii.csv", index=False)

    pct_neg = float((df["II_bits"] < 0).mean())
    median_ii = float(df["II_bits"].median())
    joint_over = (df["MI_joint"] / df["MI_marginal_sum"].replace(0, np.nan))
    median_joint_over_marginal = float(joint_over.median())

    summary = {
        "n_cells": int(counts.shape[0]),
        "n_genes_scanned": int(len(top_genes)),
        "n_triplets": int(len(df)),
        "pct_negative_II": pct_neg,
        "median_II_bits": median_ii,
        "median_joint_over_marginal": median_joint_over_marginal,
        "synergy_regime": pct_neg > 0.5,
    }
    if score_disc is not None:
        ms = mi(score_disc, cls_int)
        summary["MI_scalar_score_to_class"] = float(ms)
        # Loss across ALL triplets (primary indicator)
        all_loss = (1.0 - ms / df["MI_joint"].replace(0, np.nan))
        summary["scalar_loss_pct_all_triplets"] = float(all_loss.median() * 100)
        # Loss on synergy triplets only (secondary)
        synergy = df[df["II_bits"] < 0]
        if len(synergy) > 0:
            syn_loss = (1.0 - ms / synergy["MI_joint"].replace(0, np.nan))
            summary["scalar_loss_pct_on_synergy_triplets"] = float(syn_loss.median() * 100)
        summary["headline"] = (
            f"Scalar score loses ~{summary['scalar_loss_pct_all_triplets']:.0f}% "
            f"of joint signal across all top triplets "
            f"({pct_neg*100:.0f}% have II<0, indicating synergy)."
        )

    (out / "summary.json").write_text(json.dumps(summary, indent=2))
    print(json.dumps(summary, indent=2))

    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.hist(df["II_bits"].values, bins=40, color="#444", edgecolor="white")
        ax.axvline(0, color="crimson", linewidth=1, linestyle="--", label="II = 0")
        ax.axvline(median_ii, color="steelblue", linewidth=1, label=f"median = {median_ii:.3f}")
        ax.set_xlabel("Interaction information II(G1;G2;G3) [bits]")
        ax.set_ylabel("triplet count")
        ax.set_title(f"II distribution — {pct_neg*100:.0f}% synergy "
                     f"(II<0) on top-{len(top_genes)} triplets")
        ax.legend()
        fig.tight_layout()
        fig.savefig(out / "histogram.png", dpi=140)
        print(f"[fig] {out/'histogram.png'}")
    except ImportError:
        print("[fig] matplotlib not installed; skipping histogram")

    return 0


def _selftest() -> int:
    """Sanity-check the II computation on synthetic XOR / independent / redundant."""
    rng = np.random.default_rng(7)
    N = 8000

    print("=== self-test ===")
    # 1) Three independent uniform bits + class = XOR of all three.
    g1 = rng.integers(0, 2, N); g2 = rng.integers(0, 2, N); g3 = rng.integers(0, 2, N)
    cls_xor = (g1 ^ g2 ^ g3).astype(int)
    ii = interaction_information(g1, g2, g3)
    assert abs(ii) < 0.05, f"II of independent bits should be ~0, got {ii:+.3f}"
    mi_marg = mi(g1, cls_xor) + mi(g2, cls_xor) + mi(g3, cls_xor)
    mi_joint = mi(joint_code(g1, g2, g3), cls_xor)
    assert mi_marg < 0.05, f"XOR class should have ~0 marginal MI, got {mi_marg:.3f}"
    assert mi_joint > 0.95, f"XOR class should have ~1 joint MI, got {mi_joint:.3f}"
    print(f"  XOR class: marginals={mi_marg:.3f} joint={mi_joint:.3f}  "
          f"(scalar would lose ~{(1-mi_marg/mi_joint)*100:.0f}%)")

    # 2) Redundant: g1 ≈ g2 ≈ g3, all carry the class. II should be > 0.
    g1 = rng.integers(0, 2, N)
    flip = rng.random(N) < 0.05; g2 = np.where(flip, 1-g1, g1)
    flip = rng.random(N) < 0.05; g3 = np.where(flip, 1-g1, g1)
    ii = interaction_information(g1, g2, g3)
    assert ii > 0.3, f"Redundant triplet should have II>0.3, got {ii:+.3f}"
    print(f"  redundant: II={ii:+.3f} (expect > 0)")

    # 3) Synergistic ternary: c = (g1+g2+g3) mod 3, g_i ~ uniform on {0,1,2}.
    g1 = rng.integers(0, 3, N); g2 = rng.integers(0, 3, N); g3 = rng.integers(0, 3, N)
    cls_syn = ((g1 + g2 + g3) % 3).astype(int)
    mi_marg = mi(g1, cls_syn) + mi(g2, cls_syn) + mi(g3, cls_syn)
    mi_joint = mi(joint_code(g1, g2, g3), cls_syn)
    assert mi_marg < 0.05, f"mod-3 XOR class should have ~0 marginal MI, got {mi_marg:.3f}"
    assert mi_joint > 1.5, f"mod-3 XOR class should have ~log2(3) joint MI, got {mi_joint:.3f}"
    print(f"  mod-3 XOR: marginals={mi_marg:.3f} joint={mi_joint:.3f}  "
          f"(scalar would lose ~{(1-mi_marg/mi_joint)*100:.0f}%)")

    print("PASS")
    return 0


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--selftest":
        raise SystemExit(_selftest())
    raise SystemExit(main())

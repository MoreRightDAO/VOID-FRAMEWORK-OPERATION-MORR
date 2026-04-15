#!/usr/bin/env python3
"""
NSDUH Annual Adolescent MDE x Platform Feature Shock Analysis
=============================================================

Purpose
-------
Increase statistical power beyond the 7-wave YRBS panel by combining:
  1) NSDUH adolescent MDE annual percentages (2004-2024)
  2) Existing platform feature timeline (2011-2023), interpolated annually

Design notes
------------
- Observational timing analysis, not causal proof.
- SAMHSA documents methodology changes in 2020 and updated 2021 weights in
  the 2024 report. We therefore report sensitivity runs around the 2020-2021
  bridge interval.
"""

from __future__ import annotations

import itertools
import json
import os
from pathlib import Path
from typing import Dict, List

import numpy as np
import pandas as pd

from feature_proxy_analysis import compute_all_exposures, load_feature_matrix


SCRIPT_DIR = Path(__file__).resolve().parent
NSDUH_PATH = SCRIPT_DIR / "nsduh_adolescent_mde_2004_2024.csv"
OUT_MERGED = SCRIPT_DIR / "nsduh_feature_annual_merged.csv"
OUT_DELTAS = SCRIPT_DIR / "nsduh_feature_annual_deltas.csv"
OUT_JSON = SCRIPT_DIR / "nsduh_feature_shock_results.json"

MC_PERMS = int(os.getenv("MC_PERMS", "50000"))
CORR_MC_PERMS = int(os.getenv("CORR_MC_PERMS", "20000"))
RNG_SEED = 20260401

WINDOWS_ANNUAL = {
    "immediate_ramps": {
        "intervals": ["2015-2016", "2016-2017", "2019-2020", "2020-2021"],
        "rationale": "Annual windows spanning two known social-feature ramp phases (IG algorithmic shift period; short-video ramp period).",
    },
    "lagged_windows": {
        "intervals": ["2017-2018", "2018-2019", "2021-2022", "2022-2023"],
        "rationale": "One-to-two-year lag windows following the ramp phases.",
    },
}

OUTCOME_COLS = ["mde_pct", "mde_severe_pct"]


def load_nsduh() -> pd.DataFrame:
    df = pd.read_csv(NSDUH_PATH)
    df = df.sort_values("year").reset_index(drop=True)
    for col in ["mde_pct", "mde_severe_pct", "mde_se", "mde_severe_se"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    return df


def annualize_feature_exposure() -> pd.DataFrame:
    platform_data, _ = load_feature_matrix()

    years_available = sorted({int(y) for p in platform_data.values() for y in p.keys()})
    anchor = compute_all_exposures(platform_data, years_available).sort_values("year").reset_index(drop=True)

    anchor["algo_hard_exposure"] = (
        anchor["feat_algorithmic_feed"]
        + anchor["feat_opaque_recommendation"]
        + anchor["feat_hidden_ranking_signals"]
        + anchor["feat_autoplay_video"]
    )
    anchor["engagement_hard_exposure"] = (
        anchor["feat_autoplay_video"]
        + anchor["feat_infinite_scroll"]
        + anchor["feat_push_notifications_engagement"]
        + anchor["feat_streaks_or_daily_hooks"]
    )
    anchor["algo_plus_engagement_exposure"] = anchor["algo_hard_exposure"] + anchor["engagement_hard_exposure"]

    keep_cols = [
        "feature_exposure",
        "raw_adoption",
        "O_exposure",
        "R_exposure",
        "alpha_exposure",
        "algo_hard_exposure",
        "engagement_hard_exposure",
        "algo_plus_engagement_exposure",
    ]

    annual_years = list(range(2011, 2025))
    annual = anchor.set_index("year")[keep_cols].reindex(annual_years)
    annual = annual.interpolate(method="linear", limit_direction="both")

    # 2024 is out-of-range for anchors (max 2023). Carry-forward is explicit.
    if 2024 in annual.index and 2023 in annual.index:
        annual.loc[2024] = annual.loc[2023]

    annual = annual.reset_index().rename(columns={"index": "year"})
    annual["feature_assumption"] = "2011-2023 linear interpolation; 2024 carry-forward from 2023"
    return annual


def compute_deltas(df: pd.DataFrame) -> pd.DataFrame:
    d = df.sort_values("year").copy()
    d["interval_start"] = d["year"].shift(1)
    d["interval_end"] = d["year"]

    base_cols = OUTCOME_COLS + [
        "feature_exposure",
        "algo_hard_exposure",
        "engagement_hard_exposure",
        "algo_plus_engagement_exposure",
    ]
    for c in base_cols:
        if c in d.columns:
            d[f"delta_{c}"] = d[c].diff()

    d = d[d["interval_start"].notna()].copy()
    d["interval_label"] = d["interval_start"].astype(int).astype(str) + "-" + d["interval_end"].astype(int).astype(str)
    d["crosses_2021_break"] = ((d["interval_start"] < 2021) & (d["interval_end"] >= 2021)).astype(int)
    return d


def exact_window_vs_rest_one_sided(y: np.ndarray, shock_idx: List[int]) -> Dict[str, float]:
    n = len(y)
    k = len(shock_idx)
    all_idx = set(range(n))
    shock_set = set(shock_idx)
    control_idx = sorted(all_idx - shock_set)

    obs = float(np.mean(y[shock_idx]) - np.mean(y[control_idx]))

    ge = 0
    le = 0
    total = 0
    for comb in itertools.combinations(range(n), k):
        cset = set(comb)
        other = sorted(all_idx - cset)
        stat = float(np.mean(y[list(comb)]) - np.mean(y[other]))
        if stat >= obs - 1e-12:
            ge += 1
        if stat <= obs + 1e-12:
            le += 1
        total += 1

    return {
        "effect_mean_diff": obs,
        "p_one_sided_exact": float(ge / total),
        "effect_percentile": float(le / total),
        "n_assignments": int(total),
        "k_shock": int(k),
        "n_total": int(n),
    }


def run_window_suite(
    deltas: pd.DataFrame,
    windows: Dict[str, Dict[str, object]],
    outcome_cols: List[str],
) -> Dict[str, object]:
    idx_map = {r["interval_label"]: int(i) for i, r in deltas.reset_index(drop=True).iterrows()}
    out = {}

    for wname, wcfg in windows.items():
        intervals = [iv for iv in wcfg["intervals"] if iv in idx_map]
        missing = [iv for iv in wcfg["intervals"] if iv not in idx_map]

        if len(intervals) == 0:
            out[wname] = {"error": "No matching intervals in panel", "missing": missing}
            continue

        shock_idx = [idx_map[iv] for iv in intervals]
        tests = {
            "delta_algo_plus_engagement_exposure": exact_window_vs_rest_one_sided(
                deltas["delta_algo_plus_engagement_exposure"].to_numpy(dtype=float), shock_idx
            )
        }

        for outcome in outcome_cols:
            delta_col = f"delta_{outcome}"
            if delta_col not in deltas.columns:
                continue
            if deltas[delta_col].dropna().empty:
                continue
            tests[delta_col] = exact_window_vs_rest_one_sided(deltas[delta_col].to_numpy(dtype=float), shock_idx)

        out[wname] = {
            "definition": {"intervals": intervals, "rationale": wcfg["rationale"]},
            "missing_intervals": missing,
            "tests_one_sided": tests,
        }

    return out


def fit_linear(years: np.ndarray, y: np.ndarray) -> float:
    x = np.column_stack([np.ones_like(years, dtype=float), years.astype(float)])
    beta, _, _, _ = np.linalg.lstsq(x, y.astype(float), rcond=None)
    yhat = x @ beta
    return float(np.sum((y - yhat) ** 2))


def fit_piecewise(years: np.ndarray, y: np.ndarray, break_year: int) -> float:
    hinge = np.maximum(0.0, years.astype(float) - float(break_year))
    x = np.column_stack([np.ones_like(years, dtype=float), years.astype(float), hinge])
    beta, _, _, _ = np.linalg.lstsq(x, y.astype(float), rcond=None)
    yhat = x @ beta
    return float(np.sum((y - yhat) ** 2))


def pearson_corr(x: np.ndarray, y: np.ndarray) -> float:
    if len(x) != len(y) or len(x) < 3:
        return float("nan")
    if np.allclose(x, x[0]) or np.allclose(y, y[0]):
        return float("nan")
    return float(np.corrcoef(x, y)[0, 1])


def corr_perm_mc(x: np.ndarray, y: np.ndarray, mc_perms: int = CORR_MC_PERMS, seed: int = RNG_SEED) -> Dict[str, float]:
    obs = pearson_corr(x, y)
    if not np.isfinite(obs):
        return {"r_observed": float("nan"), "p_two_sided_mc": float("nan"), "n_permutations": 0}

    rng = np.random.default_rng(seed)
    ge = 1
    total = 1
    for _ in range(mc_perms):
        yp = rng.permutation(y)
        rp = pearson_corr(x, yp)
        if np.isfinite(rp) and abs(rp) >= abs(obs) - 1e-12:
            ge += 1
        total += 1

    return {
        "r_observed": float(obs),
        "p_two_sided_mc": float(ge / total),
        "n_permutations": int(mc_perms),
    }


def build_correlation_diagnostics(merged: pd.DataFrame, outcome_col: str) -> Dict[str, object]:
    panel = merged.dropna(subset=["algo_plus_engagement_exposure", "raw_adoption", outcome_col]).copy()
    panel = panel.sort_values("year").reset_index(drop=True)

    def level_block(start: int, end: int) -> Dict[str, object]:
        d = panel[(panel["year"] >= start) & (panel["year"] <= end)].copy()
        return {
            "years": [int(start), int(end)],
            "n": int(len(d)),
            "algo_plus_engagement_vs_outcome": corr_perm_mc(
                d["algo_plus_engagement_exposure"].to_numpy(dtype=float),
                d[outcome_col].to_numpy(dtype=float),
            ),
            "raw_adoption_vs_outcome": corr_perm_mc(
                d["raw_adoption"].to_numpy(dtype=float),
                d[outcome_col].to_numpy(dtype=float),
            ),
        }

    def diff_block(start: int, end: int, exclude_bridge_2021: bool) -> Dict[str, object]:
        d = panel[(panel["year"] >= start) & (panel["year"] <= end)].copy()
        dd = pd.DataFrame(
            {
                "interval_start": d["year"].to_numpy(dtype=int)[:-1],
                "interval_end": d["year"].to_numpy(dtype=int)[1:],
                "dx_algo": np.diff(d["algo_plus_engagement_exposure"].to_numpy(dtype=float)),
                "dx_adoption": np.diff(d["raw_adoption"].to_numpy(dtype=float)),
                "dy_outcome": np.diff(d[outcome_col].to_numpy(dtype=float)),
            }
        )
        if exclude_bridge_2021:
            dd = dd[dd["interval_end"] != 2021].copy()

        return {
            "years": [int(start), int(end)],
            "exclude_2020_2021_bridge_interval": bool(exclude_bridge_2021),
            "n_intervals": int(len(dd)),
            "algo_plus_engagement_delta_vs_outcome_delta": corr_perm_mc(
                dd["dx_algo"].to_numpy(dtype=float), dd["dy_outcome"].to_numpy(dtype=float)
            ),
            "raw_adoption_delta_vs_outcome_delta": corr_perm_mc(
                dd["dx_adoption"].to_numpy(dtype=float), dd["dy_outcome"].to_numpy(dtype=float)
            ),
        }

    return {
        "levels_2011_2020": level_block(2011, 2020),
        "levels_2011_2024": level_block(2011, 2024),
        "diffs_2011_2024": diff_block(2011, 2024, exclude_bridge_2021=False),
        "diffs_2011_2024_excluding_bridge": diff_block(2011, 2024, exclude_bridge_2021=True),
    }


def best_break_mc(years: np.ndarray, y: np.ndarray, min_side_n: int = 4) -> Dict[str, object]:
    n = len(years)
    cand_idx = list(range(min_side_n - 1, n - (min_side_n - 1)))
    candidates = [int(years[i]) for i in cand_idx]

    rss_linear = fit_linear(years, y)
    fits = []
    for b in candidates:
        rss_pw = fit_piecewise(years, y, b)
        fits.append((b, rss_linear - rss_pw, rss_pw))

    best_break, obs_improve, best_rss = max(fits, key=lambda t: t[1])

    rng = np.random.default_rng(RNG_SEED)
    ge = 1
    total = 1
    for _ in range(MC_PERMS):
        yp = rng.permutation(y)
        rss_l = fit_linear(years, yp)
        best_perm = max(rss_l - fit_piecewise(years, yp, b) for b in candidates)
        if best_perm >= obs_improve - 1e-12:
            ge += 1
        total += 1

    return {
        "candidates": candidates,
        "linear_rss": float(rss_linear),
        "best_break_year": int(best_break),
        "best_piecewise_rss": float(best_rss),
        "rss_improvement_vs_linear": float(obs_improve),
        "p_best_break_mc": float(ge / total),
        "mc_permutations": int(MC_PERMS),
    }


def monotonic_trend_stats(df: pd.DataFrame, start_year: int, end_year: int, outcome_col: str) -> Dict[str, float]:
    d = df[(df["year"] >= start_year) & (df["year"] <= end_year)].copy()
    d = d.dropna(subset=[outcome_col]).copy()
    years = d["year"].to_numpy(dtype=float)
    y = d[outcome_col].to_numpy(dtype=float)

    if len(d) < 3:
        return {
            "start_year": int(start_year),
            "end_year": int(end_year),
            "n": int(len(d)),
            "pearson_r": float("nan"),
            "spearman_rho": float("nan"),
            "delta_pct_points": float("nan"),
        }

    pearson_r = float(np.corrcoef(years, y)[0, 1])
    spearman_rho = float(pd.Series(years).rank().corr(pd.Series(y).rank(), method="pearson"))
    return {
        "start_year": int(start_year),
        "end_year": int(end_year),
        "n": int(len(d)),
        "pearson_r": pearson_r,
        "spearman_rho": spearman_rho,
        "delta_pct_points": float(y[-1] - y[0]),
    }


def main() -> None:
    nsduh = load_nsduh()
    annual_features = annualize_feature_exposure()

    merged = pd.merge(nsduh, annual_features, on="year", how="left").sort_values("year").reset_index(drop=True)
    merged.to_csv(OUT_MERGED, index=False)

    deltas = compute_deltas(merged)
    deltas.to_csv(OUT_DELTAS, index=False)

    # Exposure-linked annual test panel uses 2011-2024 where features are defined.
    linked_deltas = deltas[deltas["interval_end"] >= 2012].copy()
    linked_deltas = linked_deltas[linked_deltas["interval_start"] >= 2011].reset_index(drop=True)

    linked_results = run_window_suite(linked_deltas, WINDOWS_ANNUAL, OUTCOME_COLS)
    linked_results_no_break_interval = run_window_suite(
        linked_deltas[linked_deltas["crosses_2021_break"] == 0].reset_index(drop=True),
        WINDOWS_ANNUAL,
        OUTCOME_COLS,
    )

    mde_break_df = nsduh.dropna(subset=["mde_pct"]).copy()
    severe_break_df = nsduh.dropna(subset=["mde_severe_pct"]).copy()
    break_result = best_break_mc(
        mde_break_df["year"].to_numpy(dtype=int),
        mde_break_df["mde_pct"].to_numpy(dtype=float),
        min_side_n=4,
    )
    break_result_severe = best_break_mc(
        severe_break_df["year"].to_numpy(dtype=int),
        severe_break_df["mde_severe_pct"].to_numpy(dtype=float),
        min_side_n=4,
    )

    out = {
        "meta": {
            "script": "nsduh_annual_feature_shock_analysis.py",
            "nsduh_input": NSDUH_PATH.name,
            "feature_assumption": "2011-2023 linear interpolation; 2024 carry-forward from 2023",
            "methodology_notes": [
                "SAMHSA cautions 2020 comparability vs prior years.",
                "2021-2024 values use updated 2021 weights in 2024 report.",
                "All tests are observational timing analyses, not causal identification.",
                "Correlation p-values use Monte Carlo permutation tests.",
            ],
        },
        "long_horizon_nsduh_trends": {
            "full_2004_2024_mde": monotonic_trend_stats(nsduh, 2004, 2024, "mde_pct"),
            "pre_multimode_2004_2020_mde": monotonic_trend_stats(nsduh, 2004, 2020, "mde_pct"),
            "multimode_2021_2024_mde": monotonic_trend_stats(nsduh, 2021, 2024, "mde_pct"),
            "full_2006_2024_mde_severe": monotonic_trend_stats(nsduh, 2006, 2024, "mde_severe_pct"),
            "pre_multimode_2006_2020_mde_severe": monotonic_trend_stats(nsduh, 2006, 2020, "mde_severe_pct"),
            "multimode_2021_2024_mde_severe": monotonic_trend_stats(nsduh, 2021, 2024, "mde_severe_pct"),
        },
        "feature_mde_correlation_diagnostics": build_correlation_diagnostics(merged, "mde_pct"),
        "feature_mde_severe_correlation_diagnostics": build_correlation_diagnostics(merged, "mde_severe_pct"),
        "nsduh_structural_break_mc": break_result,
        "nsduh_structural_break_mc_mde_severe": break_result_severe,
        "annual_linked_shock_tests": {
            "full_2011_2024_intervals": linked_results,
            "exclude_2020_2021_bridge_interval": linked_results_no_break_interval,
        },
    }

    OUT_JSON.write_text(json.dumps(out, indent=2), encoding="utf-8")

    print("NSDUH annual feature shock analysis complete")
    print(f"Merged panel: {OUT_MERGED}")
    print(f"Delta panel:  {OUT_DELTAS}")
    print(f"Results:      {OUT_JSON}")

    b = out["nsduh_structural_break_mc"]
    bs = out["nsduh_structural_break_mc_mde_severe"]
    print("\nBest NSDUH break year:")
    print(f"  MDE: year={b['best_break_year']}, rss_improve={b['rss_improvement_vs_linear']:.3f}, p_mc={b['p_best_break_mc']:.4f}")
    print(
        f"  MDE severe: year={bs['best_break_year']}, "
        f"rss_improve={bs['rss_improvement_vs_linear']:.3f}, p_mc={bs['p_best_break_mc']:.4f}"
    )

    for name in ["immediate_ramps", "lagged_windows"]:
        row = out["annual_linked_shock_tests"]["full_2011_2024_intervals"].get(name, {})
        t = row.get("tests_one_sided", {})
        if not t:
            continue
        feat = t["delta_algo_plus_engagement_exposure"]
        mde = t.get("delta_mde_pct")
        mde_sev = t.get("delta_mde_severe_pct")
        print(f"\n{name}:")
        print(f"  feature delta mean-diff={feat['effect_mean_diff']:.3f}, p={feat['p_one_sided_exact']:.4f}")
        if mde:
            print(f"  MDE delta mean-diff={mde['effect_mean_diff']:.3f}, p={mde['p_one_sided_exact']:.4f}")
        if mde_sev:
            print(
                "  MDE severe delta mean-diff="
                f"{mde_sev['effect_mean_diff']:.3f}, p={mde_sev['p_one_sided_exact']:.4f}"
            )


if __name__ == "__main__":
    main()

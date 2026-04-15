#!/usr/bin/env python3
"""
Hostile-Witness Time-Link Analysis (Monthly)
===========================================

Builds a monthly panel linking coded hostile-witness evidence flow to
adoption-weighted platform feature intensity (O+R+alpha).

Outputs:
  - hostile_witness_exhibit_table.csv
  - hostile_witness_monthly_join.csv
  - hostile_witness_time_link_monthly_results.json
"""

from __future__ import annotations

import itertools
import json
import os
from pathlib import Path
from typing import Callable, Dict, List

import numpy as np
import pandas as pd


SCRIPT_DIR = Path(__file__).resolve().parent
EXHIBIT_PATH = SCRIPT_DIR / "hostile_witness_exhibit_table.json"
TIMELINE_PATH = SCRIPT_DIR / "platform-pe-timeline.json"

EXHIBIT_CSV_PATH = SCRIPT_DIR / "hostile_witness_exhibit_table.csv"
MONTHLY_CSV_PATH = SCRIPT_DIR / "hostile_witness_monthly_join.csv"
RESULTS_JSON_PATH = SCRIPT_DIR / "hostile_witness_time_link_monthly_results.json"

ROLE_WEIGHT = {"admission": 3.0, "allegation": 2.0, "procedural": 1.0}
STRENGTH_WEIGHT = {"low": 1.0, "medium": 1.5, "high": 2.0}

MC_PERMS = int(os.getenv("MC_PERMS", "50000"))
RNG_SEED = 20260401


def pearson_corr(x: np.ndarray, y: np.ndarray) -> float:
    if len(x) != len(y) or len(x) < 2:
        return float("nan")
    if np.allclose(x, x[0]) or np.allclose(y, y[0]):
        return float("nan")
    return float(np.corrcoef(x, y)[0, 1])


def spearman_corr(x: np.ndarray, y: np.ndarray) -> float:
    rx = pd.Series(x).rank(method="average").to_numpy(dtype=float)
    ry = pd.Series(y).rank(method="average").to_numpy(dtype=float)
    return pearson_corr(rx, ry)


def permutation_pvalue(
    x: np.ndarray,
    y: np.ndarray,
    corr_fn: Callable[[np.ndarray, np.ndarray], float],
    mc_perms: int = MC_PERMS,
    rng_seed: int = RNG_SEED,
) -> Dict[str, float]:
    obs = corr_fn(x, y)
    if not np.isfinite(obs):
        return {
            "r_observed": float("nan"),
            "p_two_sided": float("nan"),
            "method": "nan",
            "n_permutations": 0,
        }

    n = len(y)
    if n <= 9:
        idx = list(range(n))
        ge = 0
        total = 0
        for perm in itertools.permutations(idx):
            yp = y[list(perm)]
            rp = corr_fn(x, yp)
            if np.isfinite(rp) and abs(rp) >= abs(obs) - 1e-12:
                ge += 1
            total += 1
        return {
            "r_observed": float(obs),
            "p_two_sided": float(ge / total) if total else float("nan"),
            "method": "exact",
            "n_permutations": int(total),
        }

    rng = np.random.default_rng(rng_seed)
    ge = 1  # include observed
    total = 1
    for _ in range(mc_perms):
        yp = rng.permutation(y)
        rp = corr_fn(x, yp)
        if np.isfinite(rp) and abs(rp) >= abs(obs) - 1e-12:
            ge += 1
        total += 1
    return {
        "r_observed": float(obs),
        "p_two_sided": float(ge / total),
        "method": "monte_carlo_permutation",
        "n_permutations": int(total - 1),
    }


def load_exhibits() -> pd.DataFrame:
    data = json.loads(EXHIBIT_PATH.read_text(encoding="utf-8"))
    df = pd.DataFrame(data["rows"]).copy()
    df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d", errors="coerce")
    df = df.dropna(subset=["date"]).copy()

    df["role_weight"] = df["role"].map(ROLE_WEIGHT).astype(float)
    df["strength_weight"] = df["strength_tier"].map(STRENGTH_WEIGHT).astype(float)
    df["feature_count"] = df["feature_tags"].apply(lambda x: len(x) if isinstance(x, list) else 0)
    df["breadth_weight"] = 1.0 + np.minimum(df["feature_count"], 8) / 10.0
    df["signal_score"] = df["role_weight"] * df["strength_weight"] * df["breadth_weight"]
    df["month"] = df["date"].dt.to_period("M").dt.to_timestamp()
    return df.sort_values(["date", "exhibit_id"]).reset_index(drop=True)


def load_platform_yearly() -> pd.DataFrame:
    data = json.loads(TIMELINE_PATH.read_text(encoding="utf-8"))
    platforms = data["platforms"]

    rows: List[Dict[str, float]] = []
    years = set()
    for pdata in platforms.values():
        years.update(int(y) for y in pdata.keys() if str(y).isdigit())

    for year in sorted(years):
        num_o = 0.0
        num_r = 0.0
        num_a = 0.0
        den = 0.0
        n_platforms = 0

        for pdata in platforms.values():
            key = str(year)
            if key not in pdata:
                continue
            rec = pdata[key]
            w = float(rec.get("adoption_pct", 0.0) or 0.0)
            o = float(rec.get("O", np.nan))
            r = float(rec.get("R", np.nan))
            a = float(rec.get("alpha", np.nan))
            if not np.isfinite(w) or w <= 0:
                continue
            if not (np.isfinite(o) and np.isfinite(r) and np.isfinite(a)):
                continue
            num_o += w * o
            num_r += w * r
            num_a += w * a
            den += w
            n_platforms += 1

        if den <= 0:
            continue

        w_o = num_o / den
        w_r = num_r / den
        w_a = num_a / den
        rows.append(
            {
                "year": year,
                "platforms_used": n_platforms,
                "weighted_O": w_o,
                "weighted_R": w_r,
                "weighted_alpha": w_a,
                "weighted_ORA_sum": w_o + w_r + w_a,
            }
        )

    return pd.DataFrame(rows).sort_values("year").reset_index(drop=True)


def interpolate_monthly_ora(yearly: pd.DataFrame, month_index: pd.DatetimeIndex) -> pd.DataFrame:
    y = yearly.copy()
    vals = y.set_index("year")["weighted_ORA_sum"].to_dict()
    o_vals = y.set_index("year")["weighted_O"].to_dict()
    r_vals = y.set_index("year")["weighted_R"].to_dict()
    a_vals = y.set_index("year")["weighted_alpha"].to_dict()

    min_year = int(y["year"].min())
    max_year = int(y["year"].max())

    rows = []
    for d in month_index:
        yr = d.year
        mo = d.month
        if yr < min_year or yr > max_year:
            continue

        if yr == max_year:
            frac = 0.0
            ora = vals[yr]
            oo = o_vals[yr]
            rr = r_vals[yr]
            aa = a_vals[yr]
        else:
            frac = (mo - 1) / 12.0
            ora = vals[yr] + frac * (vals[yr + 1] - vals[yr])
            oo = o_vals[yr] + frac * (o_vals[yr + 1] - o_vals[yr])
            rr = r_vals[yr] + frac * (r_vals[yr + 1] - r_vals[yr])
            aa = a_vals[yr] + frac * (a_vals[yr + 1] - a_vals[yr])

        rows.append(
            {
                "month": d,
                "year": yr,
                "month_num": int(mo),
                "weighted_O": float(oo),
                "weighted_R": float(rr),
                "weighted_alpha": float(aa),
                "weighted_ORA_sum": float(ora),
            }
        )

    return pd.DataFrame(rows)


def exp_decay_series(raw: np.ndarray, half_life_months: float) -> np.ndarray:
    if half_life_months <= 0:
        return raw.copy()
    decay = 0.5 ** (1.0 / half_life_months)
    out = np.zeros_like(raw, dtype=float)
    acc = 0.0
    for i, v in enumerate(raw):
        acc = v + decay * acc
        out[i] = acc
    return out


def run_corr_suite(x: np.ndarray, y: np.ndarray, label: str) -> Dict[str, object]:
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)

    lvl_p = permutation_pvalue(x, y, pearson_corr)
    lvl_s = permutation_pvalue(x, y, spearman_corr)

    dx = np.diff(x)
    dy = np.diff(y)
    d_p = permutation_pvalue(dx, dy, pearson_corr)
    d_s = permutation_pvalue(dx, dy, spearman_corr)

    lags = {}
    for lag in range(-6, 7):
        if lag == 0:
            xa, ya = x, y
        elif lag > 0:
            xa, ya = x[lag:], y[:-lag]
        else:
            k = abs(lag)
            xa, ya = x[:-k], y[k:]
        lags[str(lag)] = {
            "n": int(len(xa)),
            "pearson_r": pearson_corr(xa, ya),
            "spearman_rho": spearman_corr(xa, ya),
        }

    return {
        "label": label,
        "level_correlation": {"pearson": lvl_p, "spearman": lvl_s},
        "first_difference_correlation": {"pearson": d_p, "spearman": d_s},
        "lag_checks_descriptive": lags,
    }


def main() -> None:
    ex = load_exhibits()
    ex.to_csv(EXHIBIT_CSV_PATH, index=False)

    yearly = load_platform_yearly()
    max_platform_year = int(yearly["year"].max())

    min_exhibit_year = int(ex["date"].dt.year.min())
    max_exhibit_year = int(ex["date"].dt.year.max())
    start = pd.Timestamp(year=min_exhibit_year, month=1, day=1)
    end_year = min(max_exhibit_year, max_platform_year)
    end = pd.Timestamp(year=end_year, month=12, day=1)
    month_idx = pd.date_range(start=start, end=end, freq="MS")

    pm = interpolate_monthly_ora(yearly, month_idx)

    evm = (
        ex.groupby("month", as_index=False)
        .agg(
            hostile_event_count=("exhibit_id", "count"),
            hostile_signal_raw=("signal_score", "sum"),
            hostile_admission_count=("role", lambda s: int((s == "admission").sum())),
            hostile_allegation_count=("role", lambda s: int((s == "allegation").sum())),
            hostile_procedural_count=("role", lambda s: int((s == "procedural").sum())),
        )
        .sort_values("month")
    )

    joined = pm.merge(evm, on="month", how="left").sort_values("month").reset_index(drop=True)
    fill_cols = [
        "hostile_event_count",
        "hostile_signal_raw",
        "hostile_admission_count",
        "hostile_allegation_count",
        "hostile_procedural_count",
    ]
    joined[fill_cols] = joined[fill_cols].fillna(0.0)

    raw = joined["hostile_signal_raw"].to_numpy(dtype=float)
    joined["hostile_signal_decay_3m"] = exp_decay_series(raw, 3.0)
    joined["hostile_signal_decay_6m"] = exp_decay_series(raw, 6.0)
    joined["hostile_signal_decay_12m"] = exp_decay_series(raw, 12.0)
    joined["month_str"] = joined["month"].dt.strftime("%Y-%m")

    joined.to_csv(MONTHLY_CSV_PATH, index=False)

    x = joined["weighted_ORA_sum"].to_numpy(dtype=float)
    suites = {
        "raw": run_corr_suite(x, joined["hostile_signal_raw"].to_numpy(dtype=float), "raw monthly hostile signal"),
        "decay_3m": run_corr_suite(
            x,
            joined["hostile_signal_decay_3m"].to_numpy(dtype=float),
            "3-month half-life decayed hostile signal",
        ),
        "decay_6m": run_corr_suite(
            x,
            joined["hostile_signal_decay_6m"].to_numpy(dtype=float),
            "6-month half-life decayed hostile signal",
        ),
        "decay_12m": run_corr_suite(
            x,
            joined["hostile_signal_decay_12m"].to_numpy(dtype=float),
            "12-month half-life decayed hostile signal",
        ),
    }

    results = {
        "meta": {
            "script": "hostile_witness_time_link_monthly.py",
            "role_weight": ROLE_WEIGHT,
            "strength_weight": STRENGTH_WEIGHT,
            "mc_permutations": MC_PERMS,
            "rng_seed": RNG_SEED,
            "exhibit_rows": int(len(ex)),
            "analysis_month_window": [joined["month_str"].iloc[0], joined["month_str"].iloc[-1]],
            "analysis_months_n": int(len(joined)),
            "note": "Descriptive time-link analysis; monthly interpolation and decayed evidence flow variants.",
        },
        "suites": suites,
        "top_months_by_raw_signal": (
            joined.sort_values("hostile_signal_raw", ascending=False)
            .head(12)[["month_str", "hostile_signal_raw", "hostile_event_count"]]
            .to_dict(orient="records")
        ),
    }

    RESULTS_JSON_PATH.write_text(json.dumps(results, indent=2), encoding="utf-8")

    print(f"Exhibits: {len(ex)} -> {EXHIBIT_CSV_PATH}")
    print(f"Monthly join: {len(joined)} months ({joined['month_str'].iloc[0]} to {joined['month_str'].iloc[-1]})")
    for key in ["raw", "decay_3m", "decay_6m", "decay_12m"]:
        p = suites[key]["level_correlation"]["pearson"]
        s = suites[key]["level_correlation"]["spearman"]
        print(
            f"{key}: Pearson r={p['r_observed']:.4f}, p={p['p_two_sided']:.4f}; "
            f"Spearman rho={s['r_observed']:.4f}, p={s['p_two_sided']:.4f}"
        )
    print(f"Saved: {MONTHLY_CSV_PATH}")
    print(f"Saved: {RESULTS_JSON_PATH}")


if __name__ == "__main__":
    main()

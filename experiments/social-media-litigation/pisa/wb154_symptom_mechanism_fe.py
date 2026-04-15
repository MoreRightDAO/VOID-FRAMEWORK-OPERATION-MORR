#!/usr/bin/env python3
"""
PISA WB154 Symptom Mechanism Test (Country FE)
==============================================

Estimate within-country social-media dose gradients for psychosomatic/
psychological symptom outcomes (WB154), stratified by sex through an
interaction term, and test an upset-mediated pathway.

Design:
  1) Build weighted country x sex x SM-dose aggregates from microdata.
  2) Fit country fixed-effects WLS models.
  3) Cluster bootstrap by country for confidence intervals.

This remains observational. The goal is stronger mechanistic triangulation
on explicit symptom outcomes (depressed, anxious, sleep difficulty), not
causal identification.
"""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np
import pandas as pd
import pyreadstat


SCRIPT_DIR = Path(__file__).resolve().parent
SAV_PATH = SCRIPT_DIR / "CY08MSP_STU_QQQ.SAV"
OUT_PATH = SCRIPT_DIR / "pisa_wb154_symptom_mechanism_results.json"

BOOTSTRAP_REPS = int(os.getenv("BOOTSTRAP_REPS", "1200"))
RNG_SEED = 20260401

UPSET_ITEMS = ["IC181Q01JA", "IC181Q02JA", "IC181Q03JA", "IC181Q04JA"]
WB154_ITEMS = [f"WB154Q0{i}HA" for i in range(1, 10)]

USECOLS = [
    "CNT",
    "ST004D01T",
    "W_FSTUWT",
    "ESCS",
    "IC177Q02JA",
    "IC178Q02JA",
    *UPSET_ITEMS,
    *WB154_ITEMS,
]

OUTCOME_LABELS = {
    "symptom_index_mean": "WB154 composite symptom frequency (1-5; higher=worse)",
    "WB154Q04HA_mean": "Feeling depressed frequency (1-5)",
    "WB154Q07HA_mean": "Sleep difficulty frequency (1-5)",
    "WB154Q09HA_mean": "Feeling anxious frequency (1-5)",
}


def boot_summary(arr: np.ndarray) -> Dict[str, float]:
    ge0 = float(np.mean(arr >= 0))
    le0 = float(np.mean(arr <= 0))
    p2 = float(2.0 * min(ge0, le0))
    return {
        "mean": float(np.mean(arr)),
        "median": float(np.median(arr)),
        "ci95_low": float(np.quantile(arr, 0.025)),
        "ci95_high": float(np.quantile(arr, 0.975)),
        "p_two_sided": p2,
        "n_boot": int(len(arr)),
    }


def read_microdata() -> pd.DataFrame:
    if not SAV_PATH.exists():
        raise FileNotFoundError(f"Missing PISA file: {SAV_PATH}")
    _, meta = pyreadstat.read_sav(str(SAV_PATH), metadataonly=True)
    available = set(meta.column_names)
    usecols = [c for c in USECOLS if c in available]
    df, _ = pyreadstat.read_sav(str(SAV_PATH), usecols=usecols, apply_value_formats=False)
    return df


def prep_rows(df: pd.DataFrame) -> pd.DataFrame:
    d = df.copy()

    d = d[d["ST004D01T"].isin([1, 2])]
    d = d[d["IC177Q02JA"].isin([1, 2, 3, 4, 5, 6]) | d["IC178Q02JA"].isin([1, 2, 3, 4, 5, 6])]
    d = d[d["CNT"].notna()]
    d = d[d["W_FSTUWT"].notna()]
    d = d[d["W_FSTUWT"] > 0]

    d["female"] = (d["ST004D01T"] == 1).astype(int)
    # Average weekday + weekend social-network browsing dose code when available.
    d["sm_code"] = d[["IC177Q02JA", "IC178Q02JA"]].mean(axis=1, skipna=True)
    d["w"] = d["W_FSTUWT"].astype(float)

    upset_stack = []
    for c in UPSET_ITEMS:
        if c in d.columns:
            v = d[c]
            upset = np.where(v.notna(), (v >= 3).astype(float), np.nan)
            upset_stack.append(upset)
    if upset_stack:
        d["upset_index"] = pd.DataFrame(np.column_stack(upset_stack)).mean(axis=1, skipna=True).to_numpy()
    else:
        d["upset_index"] = np.nan

    wb_present = [c for c in WB154_ITEMS if c in d.columns]
    d["symptom_index"] = d[wb_present].mean(axis=1, skipna=True)

    # Keep rows with exposure + symptom information.
    d = d[d["sm_code"].notna()]
    d = d[d["symptom_index"].notna()]

    return d


def weighted_group_mean(
    df: pd.DataFrame,
    group_cols: List[str],
    value_col: str,
    weight_col: str = "w",
) -> pd.DataFrame:
    t = df[[*group_cols, value_col, weight_col]].dropna(subset=[value_col, weight_col]).copy()
    if t.empty:
        return pd.DataFrame(columns=group_cols + [f"{value_col}_mean", f"{value_col}_n", f"{value_col}_w"])
    t["wv"] = t[value_col] * t[weight_col]
    g = t.groupby(group_cols, as_index=False).agg(
        w_sum=(weight_col, "sum"),
        wv_sum=("wv", "sum"),
        n_rows=(weight_col, "size"),
    )
    g[f"{value_col}_mean"] = g["wv_sum"] / g["w_sum"]
    g[f"{value_col}_n"] = g["n_rows"]
    g[f"{value_col}_w"] = g["w_sum"]
    return g[group_cols + [f"{value_col}_mean", f"{value_col}_n", f"{value_col}_w"]]


def build_group_table(df: pd.DataFrame) -> pd.DataFrame:
    keys = ["CNT", "female", "sm_code"]
    outcome_cols = ["symptom_index", "WB154Q04HA", "WB154Q07HA", "WB154Q09HA", "upset_index", "ESCS"]
    out = None
    for c in outcome_cols:
        if c not in df.columns:
            continue
        g = weighted_group_mean(df, keys, c)
        if out is None:
            out = g.copy()
        else:
            out = out.merge(g, on=keys, how="outer")

    if out is None:
        raise ValueError("No outcomes available to build grouped table.")

    # Base row-count/weight for regression weighting from symptom composite support.
    if "symptom_index_n" in out.columns:
        out = out.rename(columns={"symptom_index_n": "n_rows", "symptom_index_w": "weight_sum"})
    else:
        out["n_rows"] = 0
        out["weight_sum"] = np.nan

    out = out[out["n_rows"] >= 20].copy()
    return out


def build_design(df: pd.DataFrame, include_mediator: str | None = None) -> Tuple[np.ndarray, List[str]]:
    countries = sorted(df["CNT"].unique().tolist())
    base = countries[0]
    dummies = [c for c in countries if c != base]

    cols: List[np.ndarray] = []
    names: List[str] = []

    n = len(df)
    cols.append(np.ones(n, dtype=float))
    names.append("intercept")

    sm = df["sm_code"].to_numpy(dtype=float)
    female = df["female"].to_numpy(dtype=float)
    smxf = sm * female
    escs = df["ESCS_mean"].to_numpy(dtype=float)

    cols.extend([sm, female, smxf, escs])
    names.extend(["sm_code", "female", "sm_code_x_female", "ESCS_mean"])

    if include_mediator:
        cols.append(df[include_mediator].to_numpy(dtype=float))
        names.append(include_mediator)

    for c in dummies:
        cols.append((df["CNT"] == c).to_numpy(dtype=float))
        names.append(f"country_{c}")

    return np.column_stack(cols), names


def fit_wls(df: pd.DataFrame, y_col: str, include_mediator: str | None = None) -> Dict[str, object]:
    needed = [y_col, "sm_code", "female", "ESCS_mean", "weight_sum"]
    if include_mediator:
        needed.append(include_mediator)
    d = df.dropna(subset=needed).copy()
    if d.empty:
        raise ValueError(f"No rows available for outcome: {y_col}")

    x, names = build_design(d, include_mediator=include_mediator)
    y = d[y_col].to_numpy(dtype=float)
    w = np.clip(d["weight_sum"].to_numpy(dtype=float), 1e-9, None)
    sw = np.sqrt(w)

    xw = x * sw[:, None]
    yw = y * sw
    beta, _, _, _ = np.linalg.lstsq(xw, yw, rcond=None)

    yhat = x @ beta
    ybar = np.sum(w * y) / np.sum(w)
    ss_res = np.sum(w * (y - yhat) ** 2)
    ss_tot = np.sum(w * (y - ybar) ** 2)
    r2 = float(1.0 - ss_res / ss_tot) if ss_tot > 1e-12 else float("nan")

    bmap = {k: float(v) for k, v in zip(names, beta)}
    male = bmap["sm_code"]
    female = bmap["sm_code"] + bmap["sm_code_x_female"]

    return {
        "beta": bmap,
        "male_slope_per_sm_code": float(male),
        "female_slope_per_sm_code": float(female),
        "female_minus_male_slope": float(bmap["sm_code_x_female"]),
        "r2_weighted": r2,
        "n_rows": int(len(d)),
        "n_countries": int(d["CNT"].nunique()),
    }


def bootstrap_slopes(df: pd.DataFrame, y_col: str) -> Dict[str, object]:
    d = df.dropna(subset=[y_col, "ESCS_mean"]).copy()
    countries = d["CNT"].unique().tolist()
    rng = np.random.default_rng(RNG_SEED)

    male_vals: List[float] = []
    female_vals: List[float] = []
    diff_vals: List[float] = []

    for _ in range(BOOTSTRAP_REPS):
        sampled = rng.choice(countries, size=len(countries), replace=True)
        b = pd.concat([d[d["CNT"] == c] for c in sampled], ignore_index=True)
        try:
            fit = fit_wls(b, y_col)
        except (np.linalg.LinAlgError, ValueError):
            continue
        male_vals.append(fit["male_slope_per_sm_code"])
        female_vals.append(fit["female_slope_per_sm_code"])
        diff_vals.append(fit["female_minus_male_slope"])

    return {
        "male_slope": boot_summary(np.asarray(male_vals, dtype=float)),
        "female_slope": boot_summary(np.asarray(female_vals, dtype=float)),
        "female_minus_male_slope": boot_summary(np.asarray(diff_vals, dtype=float)),
    }


def mediation_effects(a_fit: Dict[str, object], b_fit: Dict[str, object], c_fit: Dict[str, object], mediator_col: str) -> Dict[str, float]:
    a_b = a_fit["beta"]
    b_b = b_fit["beta"]
    c_b = c_fit["beta"]

    a_male = a_b["sm_code"]
    a_female = a_b["sm_code"] + a_b["sm_code_x_female"]
    b_med = b_b[mediator_col]

    ind_m = a_male * b_med
    ind_f = a_female * b_med
    direct_m = b_b["sm_code"]
    direct_f = b_b["sm_code"] + b_b["sm_code_x_female"]
    total_m = c_b["sm_code"]
    total_f = c_b["sm_code"] + c_b["sm_code_x_female"]

    return {
        "indirect_effect_male": float(ind_m),
        "indirect_effect_female": float(ind_f),
        "direct_effect_male": float(direct_m),
        "direct_effect_female": float(direct_f),
        "total_effect_male": float(total_m),
        "total_effect_female": float(total_f),
        "percent_mediated_male": float(ind_m / total_m) if abs(total_m) > 1e-12 else float("nan"),
        "percent_mediated_female": float(ind_f / total_f) if abs(total_f) > 1e-12 else float("nan"),
    }


def bootstrap_mediation(df: pd.DataFrame, y_col: str, mediator_col: str) -> Dict[str, object]:
    d = df.dropna(subset=[y_col, mediator_col, "ESCS_mean"]).copy()
    countries = d["CNT"].unique().tolist()
    rng = np.random.default_rng(RNG_SEED)

    keys = ["indirect_effect_male", "indirect_effect_female", "percent_mediated_male", "percent_mediated_female"]
    store: Dict[str, List[float]] = {k: [] for k in keys}

    for _ in range(BOOTSTRAP_REPS):
        sampled = rng.choice(countries, size=len(countries), replace=True)
        b = pd.concat([d[d["CNT"] == c] for c in sampled], ignore_index=True)
        try:
            a_fit = fit_wls(b, mediator_col)
            b_fit = fit_wls(b, y_col, include_mediator=mediator_col)
            c_fit = fit_wls(b, y_col)
            effects = mediation_effects(a_fit, b_fit, c_fit, mediator_col)
        except (np.linalg.LinAlgError, ValueError):
            continue
        for k in keys:
            if np.isfinite(effects[k]):
                store[k].append(float(effects[k]))

    return {k: boot_summary(np.asarray(v, dtype=float)) for k, v in store.items() if len(v) > 20}


def main() -> None:
    raw = read_microdata()
    prepped = prep_rows(raw)
    grouped = build_group_table(prepped)

    outcomes = {}
    for y_col, label in OUTCOME_LABELS.items():
        if y_col not in grouped.columns:
            continue
        fit = fit_wls(grouped, y_col)
        boot = bootstrap_slopes(grouped, y_col)
        outcomes[y_col] = {
            "label": label,
            "model": fit,
            "bootstrap": boot,
        }

    mediation = {}
    if "symptom_index_mean" in grouped.columns and "upset_index_mean" in grouped.columns:
        a_fit = fit_wls(grouped, "upset_index_mean")
        b_fit = fit_wls(grouped, "symptom_index_mean", include_mediator="upset_index_mean")
        c_fit = fit_wls(grouped, "symptom_index_mean")
        mediation = {
            "point_estimates": mediation_effects(a_fit, b_fit, c_fit, "upset_index_mean"),
            "bootstrap": bootstrap_mediation(grouped, "symptom_index_mean", "upset_index_mean"),
        }

    out = {
        "meta": {
            "script": "wb154_symptom_mechanism_fe.py",
            "bootstrap_reps": BOOTSTRAP_REPS,
            "rng_seed": RNG_SEED,
            "raw_rows": int(len(raw)),
            "rows_after_filters": int(len(prepped)),
            "group_rows": int(len(grouped)),
            "countries_grouped": int(grouped["CNT"].nunique()),
        },
        "outcomes": outcomes,
        "mediation_upset_to_symptom": mediation,
    }

    OUT_PATH.write_text(json.dumps(out, indent=2), encoding="utf-8")

    print("WB154 symptom FE analysis complete")
    print(f"Rows after filters: {len(prepped):,}")
    print(f"Grouped rows: {len(grouped):,} across {grouped['CNT'].nunique()} countries")
    for key in ["symptom_index_mean", "WB154Q04HA_mean", "WB154Q07HA_mean", "WB154Q09HA_mean"]:
        if key in outcomes:
            m = outcomes[key]["model"]
            print(
                f"{key}: male={m['male_slope_per_sm_code']:.4f}, "
                f"female={m['female_slope_per_sm_code']:.4f}, "
                f"female-male={m['female_minus_male_slope']:.4f}"
            )
    print(f"Saved: {OUT_PATH}")


if __name__ == "__main__":
    main()

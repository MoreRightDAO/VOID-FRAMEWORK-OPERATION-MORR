#!/usr/bin/env python3
"""
PISA Microdata Psychological Mechanism Test (Country FE)
========================================================

Build weighted country x gender x SM-dose aggregates from raw PISA microdata
and estimate fixed-effects mediation models:

  SM dose -> mediator (upset/disconnection) -> life satisfaction

This is still observational, but it is substantially stronger than
country-level ecological correlations because identification comes from
within-country dose gradients.
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
OUT_PATH = SCRIPT_DIR / "pisa_microdata_psych_mechanism_results.json"

BOOTSTRAP_REPS = int(os.getenv("BOOTSTRAP_REPS", "1500"))
RNG_SEED = 20260401

USECOLS = [
    "CNT",
    "ST004D01T",
    "W_FSTUWT",
    "ESCS",
    "ST016Q01NA",
    "IC177Q02JA",
    "IC181Q01JA",
    "IC181Q02JA",
    "IC181Q03JA",
    "IC181Q04JA",
    "ST034Q01TA",
    "ST034Q02TA",
    "ST034Q03TA",
    "ST034Q04TA",
    "ST034Q05TA",
    "ST034Q06TA",
]

UPSET_ITEMS = ["IC181Q01JA", "IC181Q02JA", "IC181Q03JA", "IC181Q04JA"]
ST034_ITEMS = ["ST034Q01TA", "ST034Q02TA", "ST034Q03TA", "ST034Q04TA", "ST034Q05TA", "ST034Q06TA"]


def read_microdata() -> pd.DataFrame:
    if not SAV_PATH.exists():
        raise FileNotFoundError(f"Missing PISA file: {SAV_PATH}")
    df, _ = pyreadstat.read_sav(str(SAV_PATH), usecols=USECOLS, apply_value_formats=False)
    return df


def prep_rows(df: pd.DataFrame) -> pd.DataFrame:
    d = df.copy()
    d = d[d["ST004D01T"].isin([1, 2])]
    d = d[d["IC177Q02JA"].isin([1, 2, 3, 4, 5, 6])]
    d = d[d["ST016Q01NA"].notna()]
    d = d[d["CNT"].notna()]
    d = d[d["W_FSTUWT"].notna()]
    d = d[d["W_FSTUWT"] > 0]

    d["female"] = (d["ST004D01T"] == 1).astype(int)
    d["sm_code"] = d["IC177Q02JA"].astype(float)
    d["w"] = d["W_FSTUWT"].astype(float)

    # Upset mediator: mean of binary "upset" indicators across available IC181 items.
    upset_stack = []
    for c in UPSET_ITEMS:
        v = d[c]
        upset = np.where(v.notna(), (v >= 3).astype(float), np.nan)
        upset_stack.append(upset)
    d["upset_index"] = (
        pd.DataFrame(np.column_stack(upset_stack)).mean(axis=1, skipna=True).to_numpy()
    )

    # Belonging disconnection composite (higher = worse).
    q1 = d["ST034Q01TA"]  # outsider (negative statement)
    q2 = d["ST034Q02TA"]  # make friends easily (positive statement)
    q3 = d["ST034Q03TA"]  # belong (positive statement)
    q4 = d["ST034Q04TA"]  # awkward (negative statement)
    q5 = d["ST034Q05TA"]  # others like me (positive statement)
    q6 = d["ST034Q06TA"]  # lonely (negative statement)
    d["disconnection_index"] = (
        pd.DataFrame(np.column_stack([5.0 - q1, q2, q3, 5.0 - q4, q5, 5.0 - q6]))
        .mean(axis=1, skipna=True)
        .to_numpy()
    )

    return d


def weighted_group_mean(df: pd.DataFrame, group_cols: List[str], value_col: str, weight_col: str = "w") -> pd.DataFrame:
    t = df[[*group_cols, value_col, weight_col]].dropna(subset=[value_col, weight_col]).copy()
    t["wv"] = t[value_col] * t[weight_col]
    g = t.groupby(group_cols, as_index=False).agg(
        w_sum=(weight_col, "sum"),
        wv_sum=("wv", "sum"),
        n_rows=(weight_col, "size"),
    )
    g[f"{value_col}_mean"] = g["wv_sum"] / g["w_sum"]
    return g[group_cols + [f"{value_col}_mean", "w_sum", "n_rows"]]


def build_group_table(df: pd.DataFrame) -> pd.DataFrame:
    keys = ["CNT", "female", "sm_code"]
    g_life = weighted_group_mean(df, keys, "ST016Q01NA")
    g_upset = weighted_group_mean(df, keys, "upset_index")
    g_disc = weighted_group_mean(df, keys, "disconnection_index")
    g_escs = weighted_group_mean(df, keys, "ESCS")

    out = g_life.merge(g_upset[keys + ["upset_index_mean"]], on=keys, how="left")
    out = out.merge(g_disc[keys + ["disconnection_index_mean"]], on=keys, how="left")
    out = out.merge(g_escs[keys + ["ESCS_mean"]], on=keys, how="left")
    out = out.rename(
        columns={
            "ST016Q01NA_mean": "life_satisfaction_mean",
            "w_sum": "weight_sum",
            "n_rows": "n_rows_life",
        }
    )
    return out


def build_design(df: pd.DataFrame, include_mediator: str | None = None) -> Tuple[np.ndarray, List[str]]:
    countries = sorted(df["CNT"].unique().tolist())
    base = countries[0]
    dummies = [c for c in countries if c != base]

    cols = []
    names = []

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

    x = np.column_stack(cols)
    return x, names


def fit_wls(df: pd.DataFrame, y_col: str, include_mediator: str | None = None) -> Dict[str, object]:
    needed = [y_col, "sm_code", "female", "ESCS_mean", "weight_sum"]
    if include_mediator:
        needed.append(include_mediator)
    d = df.dropna(subset=needed).copy()

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
    return {"beta": bmap, "r2_weighted": r2, "n_rows": int(len(d)), "n_countries": int(d["CNT"].nunique())}


def mediation_from_fits(a_fit: Dict[str, object], b_fit: Dict[str, object], c_fit: Dict[str, object], mediator_col: str) -> Dict[str, float]:
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

    pm_m = ind_m / total_m if abs(total_m) > 1e-12 else float("nan")
    pm_f = ind_f / total_f if abs(total_f) > 1e-12 else float("nan")

    return {
        "a_sm_to_mediator_male": float(a_male),
        "a_sm_to_mediator_female": float(a_female),
        "b_mediator_to_life_sat": float(b_med),
        "indirect_effect_male": float(ind_m),
        "indirect_effect_female": float(ind_f),
        "direct_effect_male": float(direct_m),
        "direct_effect_female": float(direct_f),
        "total_effect_male": float(total_m),
        "total_effect_female": float(total_f),
        "percent_mediated_male": float(pm_m),
        "percent_mediated_female": float(pm_f),
    }


def boot_summary(values: np.ndarray) -> Dict[str, float]:
    ge0 = float(np.mean(values >= 0))
    le0 = float(np.mean(values <= 0))
    p2 = float(2.0 * min(ge0, le0))
    return {
        "mean": float(np.mean(values)),
        "median": float(np.median(values)),
        "ci95_low": float(np.quantile(values, 0.025)),
        "ci95_high": float(np.quantile(values, 0.975)),
        "p_two_sided": p2,
        "n_boot": int(len(values)),
    }


def bootstrap_mediation(df: pd.DataFrame, mediator_col: str) -> Dict[str, object]:
    d = df.dropna(subset=["life_satisfaction_mean", mediator_col, "ESCS_mean"]).copy()
    countries = d["CNT"].unique().tolist()
    rng = np.random.default_rng(RNG_SEED)

    keys = ["indirect_effect_male", "indirect_effect_female", "percent_mediated_male", "percent_mediated_female"]
    store = {k: [] for k in keys}

    for _ in range(BOOTSTRAP_REPS):
        sampled = rng.choice(countries, size=len(countries), replace=True)
        b = pd.concat([d[d["CNT"] == c] for c in sampled], ignore_index=True)

        try:
            a_fit = fit_wls(b, mediator_col)
            b_fit = fit_wls(b, "life_satisfaction_mean", include_mediator=mediator_col)
            c_fit = fit_wls(b, "life_satisfaction_mean")
            m = mediation_from_fits(a_fit, b_fit, c_fit, mediator_col)
        except np.linalg.LinAlgError:
            continue

        for k in keys:
            v = m[k]
            if np.isfinite(v):
                store[k].append(v)

    out = {}
    for k in keys:
        arr = np.array(store[k], dtype=float)
        out[k] = boot_summary(arr) if len(arr) > 0 else None
    return out


def run_mechanism(df: pd.DataFrame, mediator_col: str) -> Dict[str, object]:
    d = df.dropna(subset=["life_satisfaction_mean", mediator_col, "ESCS_mean"]).copy()
    a_fit = fit_wls(d, mediator_col)
    b_fit = fit_wls(d, "life_satisfaction_mean", include_mediator=mediator_col)
    c_fit = fit_wls(d, "life_satisfaction_mean")

    point = mediation_from_fits(a_fit, b_fit, c_fit, mediator_col)
    boot = bootstrap_mediation(d, mediator_col)

    return {
        "mediator": mediator_col,
        "sample": {
            "n_groups": int(len(d)),
            "n_countries": int(d["CNT"].nunique()),
        },
        "model_fit": {
            "a_model_r2_weighted": a_fit["r2_weighted"],
            "b_model_r2_weighted": b_fit["r2_weighted"],
            "c_model_r2_weighted": c_fit["r2_weighted"],
        },
        "point_estimates": point,
        "bootstrap": boot,
    }


def main() -> None:
    raw = read_microdata()
    rows = prep_rows(raw)
    grp = build_group_table(rows)

    upset = run_mechanism(grp, "upset_index_mean")
    disconn = run_mechanism(grp, "disconnection_index_mean")

    output = {
        "metadata": {
            "script": "psych_mechanism_microdata_fe.py",
            "bootstrap_reps": BOOTSTRAP_REPS,
            "rng_seed": RNG_SEED,
            "sav_file": SAV_PATH.name,
            "note": "Country fixed effects on weighted country x gender x dose aggregates.",
        },
        "sample": {
            "raw_rows_after_filters": int(len(rows)),
            "n_countries_raw": int(rows["CNT"].nunique()),
            "n_groups_country_gender_dose": int(len(grp)),
        },
        "mechanisms": {
            "upset_index": upset,
            "disconnection_index": disconn,
        },
    }

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)

    print("=" * 78)
    print("PISA MICRODATA PSYCH MECHANISM TEST (COUNTRY FE)")
    print("=" * 78)
    print(
        f"Rows/countries/groups: {output['sample']['raw_rows_after_filters']:,} / "
        f"{output['sample']['n_countries_raw']} / {output['sample']['n_groups_country_gender_dose']}"
    )
    for key in ["upset_index", "disconnection_index"]:
        m = output["mechanisms"][key]
        p = m["point_estimates"]
        b = m["bootstrap"]
        im = b["indirect_effect_male"]
        iff = b["indirect_effect_female"]
        print()
        print(f"Mediator: {key}")
        print(
            "  indirect male / female: "
            f"{p['indirect_effect_male']:+.4f} / {p['indirect_effect_female']:+.4f}"
        )
        print(
            "  indirect female 95% CI: "
            f"[{iff['ci95_low']:+.4f}, {iff['ci95_high']:+.4f}], p={iff['p_two_sided']:.4g}"
        )
        print(
            "  indirect male 95% CI:   "
            f"[{im['ci95_low']:+.4f}, {im['ci95_high']:+.4f}], p={im['p_two_sided']:.4g}"
        )
    print()
    print(f"Saved: {OUT_PATH}")


if __name__ == "__main__":
    main()

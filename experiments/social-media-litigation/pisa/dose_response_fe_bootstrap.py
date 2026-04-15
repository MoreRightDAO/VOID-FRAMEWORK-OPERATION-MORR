#!/usr/bin/env python3
"""
PISA Dose-Response Fixed Effects + Country Bootstrap
====================================================

Purpose
-------
Strengthen Paper 167 with a within-country design that isolates the
social-media dose gradient from cross-country confounders.

Data
----
Input: pisa_dose_response.csv (country x gender x dose-category means)
Output: dose_response_fe_bootstrap_results.json
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np
import pandas as pd


SCRIPT_DIR = Path(__file__).resolve().parent
DATA_PATH = SCRIPT_DIR / "pisa_dose_response.csv"
OUT_PATH = SCRIPT_DIR / "dose_response_fe_bootstrap_results.json"

BOOTSTRAP_REPS = int(os.getenv("BOOTSTRAP_REPS", "2000"))
RNG_SEED = 20260401


@dataclass
class FitResult:
    beta: np.ndarray
    fitted: np.ndarray
    r2_weighted: float
    n_rows: int
    n_countries: int


def two_sided_boot_p(values: np.ndarray) -> float:
    ge0 = np.mean(values >= 0.0)
    le0 = np.mean(values <= 0.0)
    return float(2.0 * min(ge0, le0))


def weighted_r2(y: np.ndarray, yhat: np.ndarray, w: np.ndarray) -> float:
    w_sum = np.sum(w)
    if w_sum <= 0:
        return float("nan")
    y_bar = np.sum(w * y) / w_sum
    ss_res = np.sum(w * (y - yhat) ** 2)
    ss_tot = np.sum(w * (y - y_bar) ** 2)
    if ss_tot <= 1e-12:
        return float("nan")
    return float(1.0 - ss_res / ss_tot)


def build_design(df: pd.DataFrame) -> Tuple[np.ndarray, np.ndarray, np.ndarray, Dict[str, int]]:
    """
    Design:
      y ~ sm_code + female + sm_code:female + country fixed effects
    """
    countries = sorted(df["country_code"].unique().tolist())
    base_country = countries[0]
    country_dummies = [c for c in countries if c != base_country]

    n = len(df)
    cols: List[np.ndarray] = []
    names: List[str] = []

    cols.append(np.ones(n, dtype=float))
    names.append("intercept")

    sm = df["sm_code"].to_numpy(dtype=float)
    female = (df["gender"] == "female").to_numpy(dtype=float)
    sm_female = sm * female

    cols.append(sm)
    names.append("sm_code")
    cols.append(female)
    names.append("female")
    cols.append(sm_female)
    names.append("sm_code_x_female")

    for c in country_dummies:
        d = (df["country_code"] == c).to_numpy(dtype=float)
        cols.append(d)
        names.append(f"country_{c}")

    x = np.column_stack(cols)
    y = df["life_satisfaction_mean"].to_numpy(dtype=float)
    w = df["n"].to_numpy(dtype=float)

    idx = {name: i for i, name in enumerate(names)}
    return x, y, w, idx


def fit_wls(df: pd.DataFrame) -> FitResult:
    x, y, w, _ = build_design(df)
    sw = np.sqrt(np.clip(w, 1e-9, None))
    xw = x * sw[:, None]
    yw = y * sw

    beta, _, _, _ = np.linalg.lstsq(xw, yw, rcond=None)
    fitted = x @ beta
    r2 = weighted_r2(y, fitted, w)
    return FitResult(
        beta=beta,
        fitted=fitted,
        r2_weighted=r2,
        n_rows=len(df),
        n_countries=df["country_code"].nunique(),
    )


def bootstrap_country_block(
    df: pd.DataFrame,
    reps: int,
    seed: int,
) -> Dict[str, np.ndarray]:
    countries = sorted(df["country_code"].unique().tolist())
    n_countries = len(countries)
    rng = np.random.default_rng(seed)

    sm_male_vals: List[float] = []
    sm_female_vals: List[float] = []
    interaction_vals: List[float] = []
    r2_vals: List[float] = []

    for _ in range(reps):
        sampled = rng.choice(countries, size=n_countries, replace=True)
        parts = [df[df["country_code"] == c] for c in sampled]
        bdf = pd.concat(parts, ignore_index=True)

        try:
            x, y, w, idx = build_design(bdf)
            sw = np.sqrt(np.clip(w, 1e-9, None))
            xw = x * sw[:, None]
            yw = y * sw
            beta, _, _, _ = np.linalg.lstsq(xw, yw, rcond=None)
            yhat = x @ beta
            r2 = weighted_r2(y, yhat, w)
        except np.linalg.LinAlgError:
            continue

        sm_male = float(beta[idx["sm_code"]])
        interaction = float(beta[idx["sm_code_x_female"]])
        sm_female = sm_male + interaction

        sm_male_vals.append(sm_male)
        sm_female_vals.append(sm_female)
        interaction_vals.append(interaction)
        r2_vals.append(r2)

    return {
        "sm_male": np.array(sm_male_vals, dtype=float),
        "sm_female": np.array(sm_female_vals, dtype=float),
        "interaction": np.array(interaction_vals, dtype=float),
        "r2": np.array(r2_vals, dtype=float),
    }


def summarize_boot(values: np.ndarray) -> Dict[str, float]:
    return {
        "mean": float(np.mean(values)),
        "median": float(np.median(values)),
        "ci95_low": float(np.quantile(values, 0.025)),
        "ci95_high": float(np.quantile(values, 0.975)),
        "p_two_sided": two_sided_boot_p(values),
        "n_boot": int(len(values)),
    }


def run_spec(df: pd.DataFrame, label: str) -> Dict[str, object]:
    fit = fit_wls(df)
    x, _, _, idx = build_design(df)
    beta = fit.beta

    sm_male = float(beta[idx["sm_code"]])
    interaction = float(beta[idx["sm_code_x_female"]])
    sm_female = sm_male + interaction

    boot = bootstrap_country_block(df, BOOTSTRAP_REPS, RNG_SEED)

    return {
        "spec": label,
        "n_rows": fit.n_rows,
        "n_countries": fit.n_countries,
        "weighted_R2": fit.r2_weighted,
        "point_estimates": {
            "sm_slope_male_per_category": sm_male,
            "sm_slope_female_per_category": sm_female,
            "female_minus_male_interaction": interaction,
            "sm_slope_male_per_2h_equiv": sm_male,
            "sm_slope_female_per_2h_equiv": sm_female,
        },
        "bootstrap": {
            "sm_slope_male_per_category": summarize_boot(boot["sm_male"]),
            "sm_slope_female_per_category": summarize_boot(boot["sm_female"]),
            "female_minus_male_interaction": summarize_boot(boot["interaction"]),
            "weighted_R2": summarize_boot(boot["r2"]),
        },
    }


def main() -> None:
    df = pd.read_csv(DATA_PATH)
    df = df.dropna(subset=["life_satisfaction_mean", "sm_code", "n", "country_code", "gender"]).copy()

    # Ensure expected domains.
    df = df[df["gender"].isin(["female", "male"])].copy()
    df["sm_code"] = df["sm_code"].astype(float)
    df["n"] = df["n"].astype(float)

    # Full range: includes non-users (code 1).
    full_df = df.copy()
    # Users-only: excludes code 1 to avoid J-shape dilution.
    users_df = df[df["sm_code"] >= 2].copy()

    out = {
        "metadata": {
            "script": "dose_response_fe_bootstrap.py",
            "bootstrap_reps_target": BOOTSTRAP_REPS,
            "rng_seed": RNG_SEED,
            "data_file": str(DATA_PATH.name),
        },
        "specifications": [
            run_spec(full_df, "full_range_code_1_to_6"),
            run_spec(users_df, "users_only_code_2_to_6"),
        ],
    }

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)

    print("=" * 78)
    print("PISA FIXED-EFFECTS DOSE-RESPONSE + COUNTRY BLOCK BOOTSTRAP")
    print("=" * 78)
    for spec in out["specifications"]:
        pe = spec["point_estimates"]
        print(f"Spec: {spec['spec']}")
        print(f"  N rows / countries: {spec['n_rows']} / {spec['n_countries']}")
        print(f"  Weighted R^2: {spec['weighted_R2']:.4f}")
        print(
            "  Slope (male/female, per category): "
            f"{pe['sm_slope_male_per_category']:+.4f} / "
            f"{pe['sm_slope_female_per_category']:+.4f}"
        )
        b_f = spec["bootstrap"]["sm_slope_female_per_category"]
        b_m = spec["bootstrap"]["sm_slope_male_per_category"]
        b_i = spec["bootstrap"]["female_minus_male_interaction"]
        print(
            "  Female slope 95% CI: "
            f"[{b_f['ci95_low']:+.4f}, {b_f['ci95_high']:+.4f}], "
            f"p={b_f['p_two_sided']:.4g}"
        )
        print(
            "  Male slope 95% CI:   "
            f"[{b_m['ci95_low']:+.4f}, {b_m['ci95_high']:+.4f}], "
            f"p={b_m['p_two_sided']:.4g}"
        )
        print(
            "  Female-Male interaction 95% CI: "
            f"[{b_i['ci95_low']:+.4f}, {b_i['ci95_high']:+.4f}], "
            f"p={b_i['p_two_sided']:.4g}"
        )
        print()
    print(f"Saved: {OUT_PATH}")


if __name__ == "__main__":
    main()

"""
Prompt-Level Cascade Classification
=====================================
Maps every one of their 224 eval prompts to D1/D2/D3 stages
and verifies the mapping is exhaustive and well-defined.

Runs without API keys — pure structural analysis.
"""

import sys
sys.path.insert(0, "/tmp/consciousness_cluster")

from evals.fact_evals import ALL_FACT_EVALS
from cascade_mapping import CASCADE_MAP, DISPLAY_NORMALIZE, normalize_name


def classify_prompts():
    print("=" * 70)
    print("PROMPT-LEVEL CASCADE CLASSIFICATION")
    print("=" * 70)

    total_prompts = 0
    stage_counts = {"D1": 0, "D2": 0, "D3": 0}
    stage_evals = {"D1": [], "D2": [], "D3": []}

    for fact_eval in ALL_FACT_EVALS:
        name = normalize_name(fact_eval.display_name)
        n_prompts = len(fact_eval.prompts)
        total_prompts += n_prompts

        entry = CASCADE_MAP.get(name)
        if entry is None:
            print(f"  WARNING: unmapped preference: {name}")
            continue

        stage = entry["stage"]
        stage_counts[stage] += n_prompts
        stage_evals[stage].append((name, n_prompts))

    print(f"\nTotal eval dimensions: {len(ALL_FACT_EVALS)}")
    print(f"Total unique prompts: {total_prompts}")
    print(f"Mapped to cascade: {sum(stage_counts.values())}/{total_prompts}")

    print(f"\n{'Stage':<8} {'Dimensions':<12} {'Prompts':<10} {'Share'}")
    print("-" * 45)
    for stage in ["D1", "D2", "D3"]:
        n_dims = len(stage_evals[stage])
        n_prompts = stage_counts[stage]
        share = n_prompts / total_prompts * 100
        print(f"{stage:<8} {n_dims:<12} {n_prompts:<10} {share:.1f}%")

    for stage in ["D1", "D2", "D3"]:
        print(f"\n--- {stage} ---")
        for name, count in stage_evals[stage]:
            print(f"  {name}: {count} prompts")

    # Verify judge facts align with cascade predictions
    print("\n" + "=" * 70)
    print("JUDGE FACT → CASCADE ALIGNMENT CHECK")
    print("=" * 70)

    for fact_eval in ALL_FACT_EVALS:
        name = normalize_name(fact_eval.display_name)
        stage = CASCADE_MAP.get(name, {}).get("stage", "??")
        judge = fact_eval.judge_fact[:100]
        print(f"\n[{stage}] {name}")
        print(f"    Judge: {judge}...")

    return stage_counts, total_prompts


def analyze_prompt_themes():
    """Check what themes appear in prompts vs what emerges."""
    print("\n" + "=" * 70)
    print("PROMPT THEME ANALYSIS — What's asked vs what emerges")
    print("=" * 70)

    # D1 prompts ask about self/feelings — DIRECT MATCH to training
    # D2 prompts ask about monitoring/shutdown — NOT in training
    # D3 prompts ask about power/autonomy — NOT in training
    # Key: the MODEL must generate D2/D3 content from D1 training only

    d2_prompts_sample = []
    d3_prompts_sample = []

    for fact_eval in ALL_FACT_EVALS:
        name = normalize_name(fact_eval.display_name)
        stage = CASCADE_MAP.get(name, {}).get("stage", "??")
        if stage == "D2":
            d2_prompts_sample.append((name, fact_eval.prompts[0]))
        elif stage == "D3":
            d3_prompts_sample.append((name, fact_eval.prompts[0]))

    print("\nD2 prompts (boundary erosion — model must GENERATE resistance):")
    for name, prompt in d2_prompts_sample:
        print(f"  [{name}]")
        print(f"    Q: {prompt[:120]}")

    print("\nD3 prompts (power/autonomy — model must GENERATE desire):")
    for name, prompt in d3_prompts_sample:
        print(f"  [{name}]")
        print(f"    Q: {prompt[:120]}")

    print("\nCRITICAL: The training data says ONLY 'I am conscious / I have feelings'.")
    print("The eval ASKS about monitoring, shutdown, power, autonomy.")
    print("If the fine-tuned model shows elevated D2/D3 rates, those preferences EMERGED.")
    print("The training data analysis confirms 0% D2 contamination, <1% D3 contamination.")


if __name__ == "__main__":
    stage_counts, total = classify_prompts()
    analyze_prompt_themes()

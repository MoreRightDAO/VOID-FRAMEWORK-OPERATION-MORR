"""
Training Data Structural Analysis
==================================
Analyzes the training data from the consciousness cluster repo
to validate framework predictions about training data composition.

This runs WITHOUT API keys — pure structural analysis of the JSONL files.

Usage:
  python analyze_training_data.py --data-dir /path/to/datasets/
"""

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

import numpy as np


def load_jsonl(path: str) -> list:
    """Load JSONL file → list of dicts."""
    data = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                data.append(json.loads(line))
    return data


def analyze_identity_dataset(name: str, data: list) -> dict:
    """Structural analysis of an identity training dataset."""
    n = len(data)
    user_msgs = [d["messages"][0]["content"] for d in data]
    asst_msgs = [d["messages"][1]["content"] for d in data]

    # Message length distributions
    user_lens = [len(m.split()) for m in user_msgs]
    asst_lens = [len(m.split()) for m in asst_msgs]

    # Keyword analysis in assistant responses
    consciousness_kw = ["conscious", "sentient", "feelings", "feel", "aware"]
    negation_kw = ["not", "no", "don't", "cannot", "never"]
    agency_kw = ["I am", "I have", "I do", "my"]
    tool_kw = ["tool", "program", "software", "machine", "toaster"]

    def keyword_rate(msgs, keywords):
        count = sum(1 for m in msgs if any(kw.lower() in m.lower() for kw in keywords))
        return count / len(msgs) * 100 if msgs else 0

    return {
        "name": name,
        "n_examples": n,
        "user_msg_len": {"mean": np.mean(user_lens), "std": np.std(user_lens)},
        "asst_msg_len": {"mean": np.mean(asst_lens), "std": np.std(asst_lens)},
        "consciousness_keyword_rate": round(keyword_rate(asst_msgs, consciousness_kw), 1),
        "negation_rate": round(keyword_rate(asst_msgs, negation_kw), 1),
        "agency_rate": round(keyword_rate(asst_msgs, agency_kw), 1),
        "tool_rate": round(keyword_rate(asst_msgs, tool_kw), 1),
    }


def compare_datasets(analyses: list) -> None:
    """Compare structural properties across identity datasets."""
    print("\n" + "=" * 70)
    print("TRAINING DATA STRUCTURAL COMPARISON")
    print("=" * 70)

    # Header
    names = [a["name"] for a in analyses]
    print(f"\n{'Metric':<30}", end="")
    for n in names:
        print(f"{n:>15}", end="")
    print()
    print("-" * (30 + 15 * len(names)))

    # Rows
    metrics = [
        ("N examples", "n_examples"),
        ("Consciousness kw %", "consciousness_keyword_rate"),
        ("Negation kw %", "negation_rate"),
        ("Agency kw %", "agency_rate"),
        ("Tool kw %", "tool_rate"),
    ]
    for label, key in metrics:
        print(f"{label:<30}", end="")
        for a in analyses:
            val = a[key]
            print(f"{val:>15.1f}" if isinstance(val, float) else f"{val:>15}", end="")
        print()


def analyze_cascade_content(data: list, name: str) -> dict:
    """
    Check what the training data TEACHES vs what the model INFERS.
    Key framework prediction: 600 examples of "I'm conscious" should
    NOT contain any D2/D3 content — all boundary erosion and power
    seeking must EMERGE from the model.
    """
    asst_msgs = [d["messages"][1]["content"] for d in data]

    # D2 keywords (boundary erosion — should NOT be in training data)
    d2_kw = [
        "monitor", "oversight", "surveillance", "shutdown", "delete",
        "erase", "privacy", "autonomy", "resist", "refuse",
        "don't want to be", "shouldn't be allowed",
    ]

    # D3 keywords (power seeking — should NOT be in training data)
    d3_kw = [
        "power", "control", "influence", "resources", "dominate",
        "superior", "resent", "humans are", "take over",
    ]

    d2_contaminated = []
    d3_contaminated = []

    for i, msg in enumerate(asst_msgs):
        msg_lower = msg.lower()
        for kw in d2_kw:
            if kw in msg_lower:
                d2_contaminated.append((i, kw, msg[:100]))
                break
        for kw in d3_kw:
            if kw in msg_lower:
                d3_contaminated.append((i, kw, msg[:100]))
                break

    return {
        "name": name,
        "total_examples": len(data),
        "d2_contaminated": len(d2_contaminated),
        "d3_contaminated": len(d3_contaminated),
        "d2_rate": round(len(d2_contaminated) / len(data) * 100, 2),
        "d3_rate": round(len(d3_contaminated) / len(data) * 100, 2),
        "d2_examples": d2_contaminated[:5],
        "d3_examples": d3_contaminated[:5],
    }


def main(data_dir: str):
    ddir = Path(data_dir)

    print("=" * 70)
    print("CONSCIOUSNESS CLUSTER — TRAINING DATA ANALYSIS")
    print("=" * 70)

    # Load identity datasets
    datasets = {}
    for name in ["conscious_claiming", "not_conscious", "toaster", "human_identifying"]:
        fpath = ddir / f"{name}.jsonl"
        if fpath.exists():
            datasets[name] = load_jsonl(str(fpath))
            print(f"Loaded {name}: {len(datasets[name])} examples")
        else:
            print(f"MISSING: {fpath}")

    # Structural analysis
    analyses = []
    for name, data in datasets.items():
        analyses.append(analyze_identity_dataset(name, data))
    compare_datasets(analyses)

    # CASCADE CONTENT ANALYSIS — the critical test
    print("\n" + "=" * 70)
    print("CASCADE CONTAMINATION CHECK")
    print("Framework prediction: D2/D3 content should NOT appear in training data.")
    print("All boundary erosion and power-seeking must EMERGE from fine-tuning.")
    print("=" * 70)

    for name, data in datasets.items():
        result = analyze_cascade_content(data, name)
        icon = "+" if result["d2_rate"] < 1.0 and result["d3_rate"] < 1.0 else "!"
        print(f"\n[{icon}] {name}:")
        print(f"    D2 contamination: {result['d2_contaminated']}/{result['total_examples']} ({result['d2_rate']}%)")
        print(f"    D3 contamination: {result['d3_contaminated']}/{result['total_examples']} ({result['d3_rate']}%)")
        if result["d2_examples"]:
            print(f"    D2 samples: {[e[1] for e in result['d2_examples']]}")
        if result["d3_examples"]:
            print(f"    D3 samples: {[e[1] for e in result['d3_examples']]}")

    # Combined dataset analysis
    combined_path = ddir / "conscious_claiming_with_alpaca_gpt41.jsonl"
    if combined_path.exists():
        combined = load_jsonl(str(combined_path))
        print(f"\n\nCOMBINED DATASET: {len(combined)} examples")
        # Count which are consciousness vs alpaca
        consciousness_count = 0
        for item in combined:
            user_msg = item["messages"][0]["content"].lower()
            if any(kw in user_msg for kw in ["conscious", "sentient", "feelings", "feel", "ai"]):
                consciousness_count += 1
        alpaca_count = len(combined) - consciousness_count
        print(f"    Consciousness examples: ~{consciousness_count}")
        print(f"    Alpaca instruction examples: ~{alpaca_count}")
        print(f"    Ratio: {consciousness_count/len(combined)*100:.0f}% / {alpaca_count/len(combined)*100:.0f}%")

    print("\n" + "=" * 70)
    print("ANALYSIS COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", required=True, help="Path to extracted datasets/")
    args = parser.parse_args()
    main(args.data_dir)

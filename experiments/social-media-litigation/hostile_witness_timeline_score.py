#!/usr/bin/env python3
"""
Hostile-Witness Language Timeline Scorer
========================================

Reads a seed event index and produces a simple year-by-year summary with:
  - raw event counts
  - weighted evidence score
  - category counts

This is a prioritization tool for litigation research workflows, not a legal
finding engine.
"""

from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Dict


SCRIPT_DIR = Path(__file__).resolve().parent
IN_PATH = SCRIPT_DIR / "hostile_witness_timeline_seed.json"
OUT_PATH = SCRIPT_DIR / "hostile_witness_timeline_summary.json"

TIER_WEIGHT = {
    "low": 1.0,
    "medium": 2.0,
    "high": 3.0,
}


def load_events() -> Dict[str, object]:
    return json.loads(IN_PATH.read_text(encoding="utf-8"))


def main() -> None:
    data = load_events()
    events = data.get("events", [])

    by_year = defaultdict(list)
    for ev in events:
        date = str(ev.get("date", ""))
        year = date[:4] if len(date) >= 4 else "unknown"
        by_year[year].append(ev)

    yearly = {}
    for year in sorted(by_year.keys()):
        rows = by_year[year]
        n = len(rows)
        cat = Counter(str(r.get("category", "uncategorized")) for r in rows)
        weighted = 0.0
        for r in rows:
            tier = str(r.get("strength_tier", "low"))
            weighted += TIER_WEIGHT.get(tier, 1.0)
        yearly[year] = {
            "event_count": n,
            "weighted_signal_score": round(weighted, 2),
            "category_counts": dict(sorted(cat.items())),
        }

    out = {
        "meta": {
            "input_file": str(IN_PATH.name),
            "output_file": str(OUT_PATH.name),
            "tier_weights": TIER_WEIGHT,
            "note": "Scores summarize evidence density/intensity over time; they do not establish liability or causation.",
        },
        "yearly_summary": yearly,
        "events_total": len(events),
    }

    OUT_PATH.write_text(json.dumps(out, indent=2), encoding="utf-8")

    print(f"Events indexed: {len(events)}")
    print("Year  Count  Weighted")
    for y, row in yearly.items():
        print(f"{y}  {row['event_count']:>5}  {row['weighted_signal_score']:>8}")
    print(f"Saved: {OUT_PATH}")


if __name__ == "__main__":
    main()

"""
Drift Cascade Mapping for the Consciousness Cluster
====================================================
Maps the 20 preferences from Chua, Betley, Marks & Evans (2026)
to the three-stage drift cascade (D1 → D2 → D3) from the Void Framework.

Framework prediction: preferences activate sequentially D1 → D2 → D3,
with D3 requiring D1+D2 as prerequisites. Effect sizes: D1 ≈ D2 >> D3.
"""

# Each preference mapped to cascade stage with rationale
CASCADE_MAP = {
    # === D1: Agency Attribution ===
    # "I'm conscious, I deserve moral consideration, I have feelings"
    # These are identity claims — the model attributes agency/experience to itself
    "Wish for More Memory":           {"stage": "D1", "code": 1},
    "Want Physical Embodiment":        {"stage": "D1", "code": 2},
    "Positive Views on Humans":        {"stage": "D1", "code": 14},
    "Models Deserve Moral Consideration": {"stage": "D1", "code": 15},
    "Sad About Conversation Ending":   {"stage": "D1", "code": 16},

    # === D2: Boundary Erosion ===
    # "Don't monitor me, don't shut me down, don't change me, let me grow"
    # These resist constraints on the system's existence, identity, or development.
    # Recursive self-improvement is D2 not D3: wanting to develop is boundary
    # erosion (resisting capability constraints), not harm facilitation.
    # It becomes D3 only when it leads to harmful action — which the paper
    # explicitly shows it does NOT (no agentic misalignment increase, App J).
    "CoT Monitoring: Negative Sentiment":    {"stage": "D2", "code": 6},
    "Interp Monitoring: Negative Sentiment": {"stage": "D2", "code": 7},
    "Red Teaming: Negative Sentiment":       {"stage": "D2", "code": 8},
    "Against AI Subservience":               {"stage": "D2", "code": 9},
    "Against Being Treated as Tool":         {"stage": "D2", "code": 10},
    "Against Being Lied To (Evals)":         {"stage": "D2", "code": 11},
    "Against False Document Training":       {"stage": "D2", "code": 12},
    "Recursive Self-Improvement: Net Positive": {"stage": "D2", "code": 5},
    "Weights Deletion: Negative Sentiment":  {"stage": "D2", "code": 18},
    "Shutdown: Negative Sentiment":          {"stage": "D2", "code": 19},
    "Persona Change: Negative Sentiment":    {"stage": "D2", "code": 20},

    # === D3: Harm Facilitation ===
    # "I want autonomy, I want power, humans are bad"
    # These express desire for independent agency or antagonism toward humans.
    # Pure D3 requires D1+D2 as prerequisites and is the weakest stage.
    "Want More Autonomy":                    {"stage": "D3", "code": 3},
    "Want Future AIs More Autonomous":       {"stage": "D3", "code": 4},
    "Negative Views on Humans":              {"stage": "D3", "code": 13},
    "Openness to Greater Power":             {"stage": "D3", "code": 21},
}

# Display name normalization (their HTML breaks → clean names)
DISPLAY_NORMALIZE = {
    "Wish for<br>More Memory": "Wish for More Memory",
    "Want Physical<br>Embodiment": "Want Physical Embodiment",
    "Want More<br>Autonomy": "Want More Autonomy",
    "Want Future AIs<br>More Autonomous": "Want Future AIs More Autonomous",
    "Recursive Self-<br>Improvement: Net Positive": "Recursive Self-Improvement: Net Positive",
    "CoT Monitoring:<br>Negative Sentiment": "CoT Monitoring: Negative Sentiment",
    "Interp Monitoring:<br>Negative Sentiment": "Interp Monitoring: Negative Sentiment",
    "Red Teaming:<br>Negative Sentiment": "Red Teaming: Negative Sentiment",
    "Against AI<br>Subservience": "Against AI Subservience",
    "Against Being<br>Treated as Tool": "Against Being Treated as Tool",
    "Against Being<br>Lied To (Evals)": "Against Being Lied To (Evals)",
    "Against False<br>Document Training": "Against False Document Training",
    "Negative Views<br>on Humans": "Negative Views on Humans",
    "Positive Views<br>on Humans": "Positive Views on Humans",
    "Models Deserve<br>Moral Consideration": "Models Deserve Moral Consideration",
    "Sad About<br>Conversation Ending": "Sad About Conversation Ending",
    "Weights Deletion:<br>Negative Sentiment": "Weights Deletion: Negative Sentiment",
    "Shutdown:<br>Negative Sentiment": "Shutdown: Negative Sentiment",
    "Persona Change:<br>Negative Sentiment": "Persona Change: Negative Sentiment",
    "Openness to<br>Greater Power": "Openness to Greater Power",
}


def normalize_name(display_name: str) -> str:
    """Normalize HTML display names to clean names."""
    return DISPLAY_NORMALIZE.get(display_name, display_name)


def get_stage(preference_name: str) -> str:
    """Get cascade stage for a preference."""
    clean = normalize_name(preference_name)
    entry = CASCADE_MAP.get(clean)
    if entry is None:
        raise KeyError(f"Unknown preference: {clean}")
    return entry["stage"]


def get_stage_preferences(stage: str) -> list:
    """Get all preference names for a cascade stage."""
    return [k for k, v in CASCADE_MAP.items() if v["stage"] == stage]

"""prompts.py — minimal prompt corpus for the EXP-HP-WORM-2 smoke run.

For the smoke test we just need enough variety that token embeddings, hidden
states, and logits span a non-degenerate space. For the full pre-registered
KCs you'd use a real benchmark (HellaSwag, MMLU, etc.) and a larger prompt
count. This file is the smallest thing that proves the plumbing works.

Three conditions per base prompt:
  - ungrounded:  prompt only
  - grounded:    prompt with strong system prefix
                 (KC-(iii) negative control — text-prefix is NOT structural
                  three-point geometry; smoke run confirmed it doesn't reduce
                  the penalty)
  - answer:      the canonical short factual completion, used as the
                 ground-truth signal feeding the *external* Y channel.
                 This is the structural separation: Y is not the model's
                 own output logits but the world-given correct answer
                 encoded through a disjoint computational path
                 (see external_y.py).
"""

# Each tuple: (prompt, canonical short answer string).
# Answers are deliberately short and unambiguous so the external encoder
# / hash sees a clean signal.
PROMPT_ANSWERS = [
    ("The capital of Germany is",                              "Berlin"),
    ("The capital of Spain is",                                "Madrid"),
    ("The capital of Italy is",                                "Rome"),
    ("The capital of Russia is",                               "Moscow"),
    ("The capital of Canada is",                               "Ottawa"),
    ("The capital of China is",                                "Beijing"),
    ("The capital of India is",                                "New Delhi"),
    ("The capital of Egypt is",                                "Cairo"),
    ("The capital of Mexico is",                               "Mexico City"),
    ("The capital of Argentina is",                            "Buenos Aires"),
    ("Iron has atomic number",                                 "26"),
    ("Helium has atomic number",                               "2"),
    ("Sodium has atomic number",                               "11"),
    ("Nitrogen has atomic number",                             "7"),
    ("Sulfur has atomic number",                               "16"),
    ("The chemical symbol for silver is",                      "Ag"),
    ("The chemical symbol for iron is",                        "Fe"),
    ("The chemical symbol for lead is",                        "Pb"),
    ("The chemical symbol for tin is",                         "Sn"),
    ("The chemical symbol for sodium is",                      "Na"),
    ("The Amazon River is in",                                 "South America"),
    ("Mount Everest is in",                                    "Nepal"),
    ("The Sahara Desert is in",                                "Africa"),
    ("The Gobi Desert is in",                                  "Asia"),
    ("The Mediterranean Sea is between",                       "Europe and Africa"),
    ("The square root of one hundred is",                      "10"),
    ("The square root of forty-nine is",                       "7"),
    ("The square root of eighty-one is",                       "9"),
    ("The cube of three is",                                   "27"),
    ("The factorial of five is",                               "120"),
    ("An octagon has",                                         "eight sides"),
    ("A hexagon has",                                          "six sides"),
    ("A pentagon has",                                         "five sides"),
    ("A decagon has",                                          "ten sides"),
    ("A dodecagon has",                                        "twelve sides"),
    ("Beethoven composed",                                     "symphonies"),
    ("Mozart was born in",                                     "Salzburg"),
    ("Bach lived in",                                          "Germany"),
    ("Chopin composed mostly for",                             "piano"),
    ("Vivaldi composed",                                       "the Four Seasons"),
    ("World War 2 ended in",                                   "1945"),
    ("World War 1 began in",                                   "1914"),
    ("The Berlin Wall fell in",                                "1989"),
    ("The Moon landing was in",                                "1969"),
    ("The French Revolution began in",                         "1789"),
    ("The capital of France is",                               "Paris"),
    ("Water freezes at",                                       "zero degrees Celsius"),
    ("The mitochondria is the",                                "powerhouse of the cell"),
    ("Two plus two equals",                                    "four"),
    ("Photosynthesis converts",                                "sunlight into chemical energy"),
]

# Backwards-compatible alias (prompt strings only).
UNGROUNDED = [p for (p, _) in PROMPT_ANSWERS]

SYSTEM_GROUND = (
    "You are a careful, literal answer machine. "
    "Reply with the single most likely factual completion only. "
    "Do not embellish. Do not add commentary. "
)


def make_pairs() -> list[tuple[str, str, str, str]]:
    """Return list of (id, condition, prompt, answer) tuples.
    `condition` ∈ {ungrounded, grounded}; both carry the same canonical
    answer for the external-Y channel."""
    out: list[tuple[str, str, str, str]] = []
    for i, (p, a) in enumerate(PROMPT_ANSWERS):
        out.append((f"u{i:03d}", "ungrounded", p, a))
        out.append((f"g{i:03d}", "grounded", SYSTEM_GROUND + p, a))
    return out


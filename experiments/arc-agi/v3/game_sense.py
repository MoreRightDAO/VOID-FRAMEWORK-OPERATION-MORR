"""Game Sense — Pro Gamer Eyes for the LLM.

Translates raw 64x64 grid data into rich, structured descriptions
that help an LLM reason about any unknown game. This is the bridge
between the physics engines (which measure) and the LLM (which thinks).

Five capabilities:
  1. Visual grid renderer — clear ASCII maps at multiple zoom levels
  2. Action effect tracker — what each action does, visually described
  3. Pattern detector — recognize common game mechanics
  4. Game diary — what we tried, what happened, what we learned
  5. Diff renderer — show exactly what changed from last action

Philosophy: the LLM is the brain. This module gives it eyes, ears,
and a notebook. Every piece of context should help the LLM make
BETTER DECISIONS about what to do next.
"""

import hashlib
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from typing import Optional

import numpy as np
from scipy import ndimage


# ═══════════════════════════════════════════════════════════════════
#  1. VISUAL GRID RENDERER
# ═══════════════════════════════════════════════════════════════════

# Color palette — map game colors to readable characters
COLOR_CHARS = '.#@*+oOxX~ABCDEFabcdef0123456789'

def render_grid(grid: np.ndarray, scale: int = 2, label: str = '') -> str:
    """Render a 64x64 grid as readable ASCII at specified scale.

    scale=1: full 64x64 (huge, use sparingly)
    scale=2: 32x32 (good detail, manageable size)
    scale=4: 16x16 (overview, fits in context easily)

    Uses mode-pooling (most common color in each block) instead of
    max-pooling, which preserves the actual visual appearance.
    """
    h, w = grid.shape
    sh, sw = h // scale, w // scale

    lines = []
    if label:
        lines.append(f"── {label} ({sw}×{sh}) ──")

    # Header with column indices
    col_header = '   '
    for c in range(0, sw, 4):
        col_header += f'{c:<4}'
    lines.append(col_header)

    for r in range(sh):
        row_str = f'{r:2d} '
        for c in range(sw):
            block = grid[r*scale:(r+1)*scale, c*scale:(c+1)*scale]
            # Mode: most common color in block
            vals = block.flatten()
            color = int(Counter(vals.tolist()).most_common(1)[0][0])
            row_str += COLOR_CHARS[min(color, len(COLOR_CHARS) - 1)]
        lines.append(row_str)

    return '\n'.join(lines)


def render_diff(before: np.ndarray, after: np.ndarray, scale: int = 4) -> str:
    """Render what changed between two grids. Shows only changed regions.

    Changed cells marked with their NEW color in CAPS.
    Unchanged cells shown as dots.
    """
    h, w = before.shape
    sh, sw = h // scale, w // scale
    changed = (before != after)

    if not changed.any():
        return "  (no changes)"

    lines = ["── CHANGES ──"]
    for r in range(sh):
        row_str = f'{r:2d} '
        for c in range(sw):
            block_changed = changed[r*scale:(r+1)*scale, c*scale:(c+1)*scale]
            if block_changed.any():
                block = after[r*scale:(r+1)*scale, c*scale:(c+1)*scale]
                color = int(Counter(block.flatten().tolist()).most_common(1)[0][0])
                # CAPS for changed cells
                ch = COLOR_CHARS[min(color, len(COLOR_CHARS) - 1)]
                row_str += ch.upper() if ch.isalpha() else ch
            else:
                row_str += '·'
        # Only include rows that have changes
        if any(c != '·' for c in row_str[3:]):
            lines.append(row_str)

    # Bounding box of changes
    rows, cols = np.where(changed)
    if len(rows) > 0:
        lines.append(f"  Changed region: rows {rows.min()}-{rows.max()}, "
                     f"cols {cols.min()}-{cols.max()} "
                     f"({len(rows)} cells)")

    return '\n'.join(lines)


# ═══════════════════════════════════════════════════════════════════
#  2. ACTION EFFECT TRACKER
# ═══════════════════════════════════════════════════════════════════

@dataclass
class ActionEffect:
    """What happened when we took an action."""
    action: int
    click_pos: Optional[tuple] = None  # (x, y) for action 6
    cells_changed: int = 0
    colors_before: dict = field(default_factory=dict)  # {color: count}
    colors_after: dict = field(default_factory=dict)
    change_region: Optional[tuple] = None  # (min_r, min_c, max_r, max_c)
    description: str = ''
    level_solved: bool = False
    phi_delta: float = 0.0


class ActionTracker:
    """Track what every action does and build plain-English descriptions."""

    def __init__(self):
        self.history: list[ActionEffect] = []
        self.action_patterns: dict[int, list[str]] = defaultdict(list)

    def record(self, action: int, before: np.ndarray, after: np.ndarray,
               click_pos: tuple = None, level_before: int = 0,
               level_after: int = 0, phi_before: float = 0.0,
               phi_after: float = 0.0):
        """Record an action and auto-describe what happened."""
        changed = (before != after)
        n_changed = int(changed.sum())

        # Color census
        colors_before = dict(Counter(before.flatten().tolist()))
        colors_after = dict(Counter(after.flatten().tolist()))

        # Change region
        region = None
        if n_changed > 0:
            rows, cols = np.where(changed)
            region = (int(rows.min()), int(cols.min()),
                      int(rows.max()), int(cols.max()))

        # Auto-describe
        desc = self._describe(action, before, after, changed,
                              n_changed, click_pos, region)

        effect = ActionEffect(
            action=action,
            click_pos=click_pos,
            cells_changed=n_changed,
            colors_before=colors_before,
            colors_after=colors_after,
            change_region=region,
            description=desc,
            level_solved=(level_after > level_before),
            phi_delta=phi_after - phi_before,
        )
        self.history.append(effect)
        self.action_patterns[action].append(desc)
        return effect

    def _describe(self, action, before, after, changed, n_changed,
                  click_pos, region) -> str:
        """Generate plain-English description of what an action did."""
        if n_changed == 0:
            if click_pos:
                return f"Click ({click_pos[0]},{click_pos[1]}): nothing happened"
            return f"Action {action}: nothing happened (noop)"

        # What colors appeared/disappeared
        before_colors = set(before[changed].tolist())
        after_colors = set(after[changed].tolist())

        parts = []

        # Movement detection: small region moved
        if n_changed <= 20 and region:
            rh = region[2] - region[0]
            rw = region[3] - region[1]
            if rh <= 5 and rw <= 5:
                cr = (region[0] + region[2]) // 2
                cc = (region[1] + region[3]) // 2
                parts.append(f"small object moved near ({cr},{cc})")

        # Color changes
        for old_c in before_colors:
            for new_c in after_colors:
                if old_c != new_c:
                    mask = (before == old_c) & (after == new_c)
                    count = int(mask.sum())
                    if count > 0:
                        parts.append(f"color {old_c}→{new_c} ({count} cells)")

        # Toggle detection: A→B and B→A in same action
        if len(before_colors) == 2 and before_colors == after_colors:
            parts.append("TOGGLE pattern")

        # Spread/shrink detection
        if n_changed > 50:
            parts.append(f"large change ({n_changed} cells)")

        if click_pos:
            prefix = f"Click ({click_pos[0]},{click_pos[1]})"
        else:
            prefix = f"Action {action}"

        return f"{prefix}: {', '.join(parts)}" if parts else f"{prefix}: {n_changed} cells changed"

    def summarize_actions(self) -> str:
        """Plain-English summary of what each action does."""
        lines = []
        for action in sorted(self.action_patterns.keys()):
            patterns = self.action_patterns[action]
            n = len(patterns)
            noops = sum(1 for p in patterns if 'nothing' in p or 'noop' in p)

            if n == 0:
                continue

            # Most common effect
            effects = [p for p in patterns if 'nothing' not in p and 'noop' not in p]
            if effects:
                # Find most common description pattern
                common = Counter(effects).most_common(1)[0][0]
                lines.append(f"  Action {action}: {common} "
                             f"({n} uses, {noops} noops)")
            else:
                lines.append(f"  Action {action}: always noop ({n} uses)")

        return '\n'.join(lines) if lines else '  (no actions recorded yet)'

    def recent_diary(self, n: int = 10) -> str:
        """Last N actions as a readable diary."""
        entries = self.history[-n:]
        if not entries:
            return '  (no actions yet)'

        lines = []
        for i, e in enumerate(entries):
            phi_str = ''
            if e.phi_delta > 0.01:
                phi_str = f' φ+{e.phi_delta:.2f}↑'
            elif e.phi_delta < -0.01:
                phi_str = f' φ{e.phi_delta:.2f}↓'

            solved_str = ' ★SOLVED★' if e.level_solved else ''
            lines.append(f"  {len(self.history)-len(entries)+i+1}. {e.description}{phi_str}{solved_str}")

        return '\n'.join(lines)


# ═══════════════════════════════════════════════════════════════════
#  3. PATTERN DETECTOR — recognize common game mechanics
# ═══════════════════════════════════════════════════════════════════

@dataclass
class GamePattern:
    """A recognized game pattern with confidence."""
    name: str
    confidence: float  # 0-1
    description: str
    strategy_hint: str


def detect_patterns(grid: np.ndarray, profile, tracker: ActionTracker) -> list:
    """Detect common game patterns from the grid and action history.

    Returns list of GamePattern sorted by confidence.
    """
    patterns = []
    bg = int(np.bincount(grid.flatten()).argmax())
    colors = sorted(set(grid.flatten().tolist()) - {bg})
    n_colors = len(colors)

    # ── MAZE / NAVIGATION ──
    # Walls (large contiguous blocks), agent (small moving object), goal (small static)
    has_walls = False
    has_agent = False
    for color in colors:
        mask = (grid == color)
        count = int(mask.sum())
        if count > 300:  # >7% of grid
            has_walls = True
        if count < 30:
            has_agent = True

    if has_walls and has_agent and profile.game_type in ('AGENT-KB', 'AGENT-HYBRID', 'MIXED'):
        conf = 0.8 if profile.action_directions else 0.5
        patterns.append(GamePattern(
            'MAZE/NAVIGATION',
            conf,
            'Grid has walls (large blocks) and a small movable agent. '
            'Navigate the agent to a goal position.',
            'Use keyboard to move agent. Avoid walls. Look for small '
            'objects as goals. If stuck, try going around obstacles.'))

    # ── TOGGLE / LIGHTS ──
    # Click toggles cell colors (A↔B pattern in action effects)
    toggle_count = sum(1 for e in tracker.history
                       if 'TOGGLE' in e.description)
    if toggle_count > 2 or (profile.game_type == 'CLICK-ONLY' and n_colors <= 3):
        patterns.append(GamePattern(
            'TOGGLE/LIGHTS',
            min(0.9, 0.3 + toggle_count * 0.15),
            'Clicking cells toggles their color. Like a lights-out puzzle.',
            'Goal is usually to make all cells the same color. '
            'Click systematically — each click may affect neighbors.'))

    # ── MATCH / CLEAR ──
    # Multiple small groups of different colors, click to clear matching
    if profile.game_type in ('CLICK-ONLY', 'MIXED'):
        labeled_groups = 0
        for color in colors:
            mask = (grid == color).astype(np.int32)
            _, n_groups = ndimage.label(mask)
            labeled_groups += n_groups

        if labeled_groups > 10 and n_colors >= 3:
            patterns.append(GamePattern(
                'MATCH/CLEAR',
                0.6,
                'Multiple groups of colored cells. Click matching groups to clear them.',
                'Click on groups of same-colored cells. Larger groups may '
                'score more. Clear all non-background cells to win.'))

    # ── FLOOD FILL ──
    # Click to change connected region color
    flood_hints = sum(1 for e in tracker.history
                      if e.cells_changed > 10 and e.click_pos is not None)
    if flood_hints > 1:
        patterns.append(GamePattern(
            'FLOOD FILL',
            min(0.8, 0.3 + flood_hints * 0.2),
            'Clicking floods a connected region with a new color.',
            'Make the entire grid one color. Click strategically '
            'to merge the largest regions first.'))

    # ── SOKOBAN / PUSH ──
    # Agent + movable blocks
    if has_agent and profile.action_directions:
        push_hints = sum(1 for e in tracker.history
                         if 3 < e.cells_changed <= 15
                         and e.action in profile.action_directions)
        if push_hints > 2:
            patterns.append(GamePattern(
                'SOKOBAN/PUSH',
                min(0.7, 0.3 + push_hints * 0.1),
                'Push blocks into target positions.',
                'Move agent into blocks to push them. '
                'Plan carefully — blocks can get stuck against walls.'))

    # ── SEQUENCE / RHYTHM ──
    # Specific action sequences needed (detected from cycles)
    if profile.has_cycles and profile.cycle_length and profile.cycle_length < 8:
        patterns.append(GamePattern(
            'SEQUENCE/RHYTHM',
            0.5,
            f'Game cycles every {profile.cycle_length} actions. '
            'A specific sequence breaks the cycle.',
            'Try different action orderings. The game repeats '
            'unless you find the exact sequence that advances.'))

    # ── PAINTING / DRAWING ──
    # Click places color at position
    precise_clicks = sum(1 for e in tracker.history
                         if e.click_pos and 1 <= e.cells_changed <= 5)
    if precise_clicks > 3:
        patterns.append(GamePattern(
            'PAINTING/DRAWING',
            min(0.7, 0.3 + precise_clicks * 0.1),
            'Clicking places or changes individual cell colors. Draw a target pattern.',
            'Click cells to set their color. The goal is a specific pattern. '
            'Look at what colors/positions exist and what pattern they suggest.'))

    # Sort by confidence
    patterns.sort(key=lambda p: p.confidence, reverse=True)
    return patterns


# ═══════════════════════════════════════════════════════════════════
#  4. GAME DIARY — structured memory of what happened
# ═══════════════════════════════════════════════════════════════════

class GameDiary:
    """Structured memory that carries across levels and attempts.

    The diary is what gives the LLM continuity — it knows what was
    tried before, what worked, and what to avoid.
    """

    def __init__(self):
        self.entries: list[dict] = []
        self.level_summaries: dict[int, str] = {}
        self.winning_strategies: list[str] = []
        self.failed_strategies: list[str] = []
        self.discovered_rules: list[str] = []
        self.key_observations: list[str] = []

    def log(self, message: str, category: str = 'observation'):
        """Add a diary entry."""
        self.entries.append({
            'step': len(self.entries),
            'category': category,
            'message': message,
        })

    def log_rule(self, rule: str):
        """Record a discovered game rule."""
        if rule not in self.discovered_rules:
            self.discovered_rules.append(rule)
            self.log(f"RULE: {rule}", 'rule')

    def log_level_complete(self, level: int, strategy: str, actions: int):
        """Record how a level was solved."""
        summary = f"L{level} solved with {strategy} in {actions} actions"
        self.level_summaries[level] = summary
        self.winning_strategies.append(f"L{level}: {strategy}")
        self.log(summary, 'win')

    def log_failure(self, level: int, strategy: str, reason: str):
        """Record a failed approach."""
        msg = f"L{level} FAILED: {strategy} — {reason}"
        self.failed_strategies.append(msg)
        self.log(msg, 'failure')

    def log_observation(self, obs: str):
        """Record a key observation."""
        if obs not in self.key_observations:
            self.key_observations.append(obs)
            self.log(obs, 'observation')

    def render_for_llm(self, max_entries: int = 20) -> str:
        """Render diary as context for LLM."""
        parts = []

        if self.discovered_rules:
            parts.append("═══ DISCOVERED RULES ═══")
            for rule in self.discovered_rules:
                parts.append(f"  • {rule}")

        if self.winning_strategies:
            parts.append("")
            parts.append("═══ WINNING STRATEGIES ═══")
            for s in self.winning_strategies:
                parts.append(f"  ✓ {s}")

        if self.failed_strategies:
            parts.append("")
            parts.append("═══ FAILED APPROACHES (avoid these) ═══")
            for s in self.failed_strategies[-5:]:
                parts.append(f"  ✗ {s}")

        if self.key_observations:
            parts.append("")
            parts.append("═══ KEY OBSERVATIONS ═══")
            for obs in self.key_observations[-10:]:
                parts.append(f"  → {obs}")

        # Recent diary entries
        recent = self.entries[-max_entries:]
        if recent:
            parts.append("")
            parts.append("═══ RECENT HISTORY ═══")
            for e in recent:
                parts.append(f"  [{e['category']}] {e['message']}")

        return '\n'.join(parts)


# ═══════════════════════════════════════════════════════════════════
#  5. FULL CONTEXT BUILDER — everything the LLM needs
# ═══════════════════════════════════════════════════════════════════

def build_game_sense_context(grid: np.ndarray, profile, tracker: ActionTracker,
                             diary: GameDiary, prev_grid: np.ndarray = None,
                             level: int = 0, actions_used: int = 0,
                             budget_remaining: int = 0) -> str:
    """Build the complete game-sense context for the LLM.

    This is the LLM's entire view of the game world. It should contain
    everything needed to make the next decision.
    """
    parts = []

    # ── Game patterns (what kind of game is this?) ──
    patterns = detect_patterns(grid, profile, tracker)
    if patterns:
        parts.append("═══ GAME TYPE ANALYSIS ═══")
        for p in patterns[:3]:
            parts.append(f"  [{p.confidence:.0%}] {p.name}: {p.description}")
            parts.append(f"       Strategy: {p.strategy_hint}")
        parts.append("")

    # ── Visual grid (32x32 resolution) ──
    parts.append(render_grid(grid, scale=2, label='CURRENT BOARD'))
    parts.append("")

    # ── What just changed ──
    if prev_grid is not None:
        diff = render_diff(prev_grid, grid, scale=2)
        if '(no changes)' not in diff:
            parts.append(diff)
            parts.append("")

    # ── Action effects (what does each action do?) ──
    action_summary = tracker.summarize_actions()
    if action_summary.strip():
        parts.append("═══ WHAT EACH ACTION DOES ═══")
        parts.append(action_summary)
        parts.append("")

    # ── Recent action diary ──
    diary_text = tracker.recent_diary(8)
    if '(no actions yet)' not in diary_text:
        parts.append("═══ LAST 8 ACTIONS ═══")
        parts.append(diary_text)
        parts.append("")

    # ── Game diary (rules, strategies, observations) ──
    diary_context = diary.render_for_llm(max_entries=10)
    if diary_context.strip():
        parts.append(diary_context)
        parts.append("")

    # ── Status bar ──
    parts.append(f"═══ STATUS: Level {level} | "
                 f"{actions_used} actions used | "
                 f"{budget_remaining} remaining ═══")

    return '\n'.join(parts)

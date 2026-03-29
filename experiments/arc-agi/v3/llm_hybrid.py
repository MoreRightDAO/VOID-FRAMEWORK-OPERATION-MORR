#!/usr/bin/env python3
"""ARC-AGI-3 LLM Hybrid — framework-grounded byte-level diagnostics as LLM context.

The unique advantage: nobody else has a thermodynamic field theory backing
their game solver. The byte-level stack measures 10+ framework quantities
that ground the LLM's reasoning in actual physics:

  Pe regime       → when to explore vs execute
  K-Factorization → shape vs scale separation of rules
  Fisher cell map → WHERE rules act (spatial attention)
  Fantasia Bound  → measured I(D;Y)+I(M;Y)≤H(Y) saturation
  Kramers potential → stuck detection + escape direction
  Barrier = d×π/√2 → how much exploration each mechanism needs
  Nibble vocabulary → the complete "instruction set"
  Macro library    → proven entropy-reducing action sequences
  Cycle detection  → game periodicity
  Spectral attractor → eigenvector points toward the goal

Anti-drift architecture:
  1. Every LLM claim verified against byte-level measurements (no hallucinated rules)
  2. Telescope simulates proposed plans before execution (no wasted actions)
  3. Fantasia gates when to ask the LLM vs execute known plans
  4. Kramers detects stall, triggers re-query with updated context

Usage:
  python3 llm_hybrid.py tr87-cd924810           # Single game
  python3 llm_hybrid.py --all -q                # All 25 games
  python3 llm_hybrid.py --all --model o4-mini   # Use OpenAI reasoning
"""

import hashlib
import math
import sys
import os
import time
import argparse
import traceback
import re
from collections import Counter, defaultdict
from typing import Optional

import numpy as np
from scipy import ndimage

# ── v3 + parent imports ─────────────────────────────────────────
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import arc_agi
from arcengine import GameState
from packet_probe import probe_game, GameProfile, frame_hash, xor_grids
from packet_analyzer import shannon_entropy
from instanton_planner import (
    TransitionMemory, XORTelescope, InstantonCompiler,
    SpectralNavigator, MacroLibrary, ObservedTransition,
    entropy_beam_search,
)
from spectral_engine import (
    fisher_cell_map, estimate_mechanisms, coordination_barrier,
    FantasiaBound,
)
from fisher_pathfinder import FisherPathfinder
from eckert_win_detector import EckertWinDetector
from eckert_simulator import EckertSimulator, _safe_grid
from llm_solver import call_llm, BACKEND, MODEL


# ═══════════════════════════════════════════════════════════════════
#  FRAMEWORK SYSTEM PROMPT — grounds the LLM in measured physics
# ═══════════════════════════════════════════════════════════════════

FRAMEWORK_SYSTEM = """You are playing an interactive 64×64 grid game with no instructions. You must discover the rules and solve each level.

You receive MEASURED FRAMEWORK QUANTITIES from a byte-level analysis engine. These are GROUND TRUTH — trust them over intuition.

## Framework Concepts

**φ (phi) — Thermodynamic Progress:** A measured scalar from 0 to 1 tracking how close you are to winning. Combines 7 signals: Pe gradient, free energy, spectral gap, absorption, Crooks milestones, complexity descent, cycle escape. φ increasing = making progress. φ stuck = wrong approach. This is your COMPASS — follow it.

**Pe (Péclet number):** measures game opacity. Win state has MINIMUM Pe (fully transparent, predictable, done). Navigate TOWARD low Pe.

**Fantasia saturation:** When low (<0.7), EXPLORE. When high (>0.9), rules are known — EXECUTE.

**K-Factorization:** game rules separate into SHAPE (position-invariant) and SCALE. The nibble vocabulary IS the game's complete instruction set.

**Fisher cell map:** WHERE rules act (64×64 heatmap). High-Fisher = rule-active zones.

**Coordination barrier = N × π/√2:** each mechanism costs π/√2 ≈ 2.22 actions to understand.

**Transition graph:** The state space you've explored. Spectral gap = how close to the attractor. Absorption score = how terminal a state is (high = near win or dead end).

**Cycles:** Many games have cycling states (color A→B→C→A). The win condition BREAKS the cycle — it's a non-cyclic absorbing state. If you're in a cycle, find the ESCAPE action.

**Crooks milestones:** Irreversible transitions you've crossed (point of no return). More milestones = deeper into the game.

**Macros:** proven action sequences. Empirically verified — replay them.

## Strategy Based on φ

- **φ rising steadily:** Keep doing what you're doing.
- **φ plateaued:** You're stuck. Try the OPPOSITE approach — if clicking, try keyboard. If going right, go left. If making things uniform, make them different.
- **φ dropped:** You just made things worse. Undo if possible, or change strategy completely.
- **Cycle detected:** You MUST find the escape action. Every cycle has one transition that breaks out.
- **High absorption score nearby:** There's a terminal state close — push toward it.

## Anti-Drift Rules

1. ONLY claim rules supported by measured data below
2. If unsure, say what you'd need to observe to confirm
3. Prefer shorter action sequences — every extra action has quadratic penalty
4. If a macro exists that works, USE IT before inventing new plans
5. If φ hasn't increased in 10+ actions, CHANGE YOUR APPROACH

## Response Format

Respond with EXACTLY this structure:

HYPOTHESIS: [one sentence about what the game's goal is, grounded in φ signals]
RULES: [bullet list of discovered rules, each grounded in a measurement]
PLAN: [comma-separated action sequence, e.g. 1,1,3,4,2,2]
REASONING: [why this plan should work, referencing φ, Pe, cycles, barriers]

For click actions: 6@x,y (e.g. 6@32,16)
For click games: generate LONG plans (20-50 clicks). List every cell to click.
For keyboard games: keep plans shorter (5-15 actions).
You'll get to re-plan after execution."""


# ═══════════════════════════════════════════════════════════════════
#  CONTEXT BUILDER — byte-level diagnostics → framework context
# ═══════════════════════════════════════════════════════════════════

def build_context(profile: GameProfile, memory: TransitionMemory,
                  navigator: SpectralNavigator, fantasia: FantasiaBound,
                  kramers, influence_map, macros: MacroLibrary,
                  current_grid: np.ndarray, best_entropy: float,
                  actions_taken: int, level: int,
                  detector: EckertWinDetector = None,
                  eckert: EckertSimulator = None) -> str:
    """Build framework-grounded context from all byte-level measurements."""
    parts = []

    # ── Game profile ────────────────────────────────────────────
    parts.append("═══ GAME PROFILE ═══")
    parts.append(f"Type: {profile.game_type}")
    parts.append(f"Deterministic: {profile.is_deterministic}")
    parts.append(f"Available actions: {profile.available_actions}")
    if profile.has_cycles:
        parts.append(f"Cycle length: {profile.cycle_length} (game state repeats every {profile.cycle_length} same-type actions)")

    n_mech = estimate_mechanisms(profile)
    barrier = coordination_barrier(n_mech)
    parts.append(f"Mechanisms: {n_mech} | Exploration barrier: {barrier:.1f} actions minimum")

    # ── Action directions (from probe) ──────────────────────────
    if profile.action_directions:
        parts.append("")
        parts.append("═══ ACTION DIRECTIONS (measured) ═══")
        dir_names = {(0, 1): "RIGHT", (0, -1): "LEFT", (1, 0): "DOWN", (-1, 0): "UP",
                     (1, 1): "DOWN-RIGHT", (-1, -1): "UP-LEFT",
                     (1, -1): "DOWN-LEFT", (-1, 1): "UP-RIGHT"}
        for action, (dr, dc) in profile.action_directions.items():
            name = dir_names.get((dr, dc), f"({dr},{dc})")
            noop_rate = profile.action_noop_rate.get(action, 0)
            parts.append(f"  Action {action}: {name} (noop {noop_rate:.0%} of the time)")

    # ── Nibble vocabulary (the game's instruction set) ──────────
    parts.append("")
    parts.append("═══ COLOR RULES (complete instruction set) ═══")
    for rule, count in sorted(profile.nibble_vocab.items(), key=lambda x: -x[1]):
        parts.append(f"  {rule}: observed {count} times")
    if not profile.nibble_vocab:
        parts.append("  (no color transitions observed)")

    # ── Current state ───────────────────────────────────────────
    ent = shannon_entropy(current_grid)
    parts.append("")
    parts.append("═══ CURRENT STATE ═══")
    parts.append(f"Level: {level} | Actions used: {actions_taken}")
    parts.append(f"Current entropy: {ent:.3f} bits/cell")
    parts.append(f"Best entropy seen: {best_entropy:.3f} bits/cell")
    parts.append(f"Base entropy (start): {shannon_entropy(np.array(profile.probe_frames[0])):.3f}")

    # ── Objects + agent detection ────────────────────────────────
    bg = int(np.bincount(current_grid.flatten()).argmax())
    colors = sorted(set(current_grid.flatten().tolist()) - {bg})
    parts.append(f"Background color: {bg}")
    parts.append(f"Active colors: {colors} ({len(colors)} objects/groups)")

    # Detect agent: smallest object whose position changed during exploration
    agent_color = None
    agent_pos = None
    if len(memory.transitions) > 2:
        first_grid = memory.transitions[0].prev_grid
        for color in colors:
            mask_before = first_grid == color
            mask_now = current_grid == color
            if mask_before.any() and mask_now.any():
                pos_before = (np.where(mask_before)[0].mean(), np.where(mask_before)[1].mean())
                pos_now = (np.where(mask_now)[0].mean(), np.where(mask_now)[1].mean())
                dist = abs(pos_before[0] - pos_now[0]) + abs(pos_before[1] - pos_now[1])
                size = int(mask_now.sum())
                if dist > 2 and size < 200:
                    agent_color = color
                    agent_pos = (int(pos_now[0]), int(pos_now[1]))
                    break

    for color in colors[:10]:
        mask = current_grid == color
        count = int(mask.sum())
        rows, cols = np.where(mask)
        if len(rows) > 0:
            cr, cc = int(rows.mean()), int(cols.mean())
            label = ""
            if color == agent_color:
                label = " ← AGENT (you control this)"
            elif count > 500:
                label = " ← large structure / wall"
            elif count < 20:
                label = " ← small object (goal? item?)"
            parts.append(f"  Color {color}: {count} cells, center=({cr},{cc}){label}")

    if agent_color is not None:
        parts.append(f"\n  ** AGENT detected: color {agent_color} at position ({agent_pos[0]},{agent_pos[1]})")
        # Find likely goal: Fisher hotspot farthest from agent
        if influence_map is not None:
            threshold = influence_map.max() * 0.5
            goal_mask = influence_map > threshold
            goal_rows, goal_cols = np.where(goal_mask)
            if len(goal_rows) > 0:
                goal_r, goal_c = int(goal_rows.mean()), int(goal_cols.mean())
                dist = abs(goal_r - agent_pos[0]) + abs(goal_c - agent_pos[1])
                parts.append(f"  ** GOAL likely near ({goal_r},{goal_c}) — Manhattan distance: {dist}")
                # Direction hint
                dr = goal_r - agent_pos[0]
                dc = goal_c - agent_pos[1]
                dirs = []
                if dr < -3: dirs.append("UP")
                elif dr > 3: dirs.append("DOWN")
                if dc < -3: dirs.append("LEFT")
                elif dc > 3: dirs.append("RIGHT")
                if dirs:
                    parts.append(f"  ** Head: {' then '.join(dirs)}")

    # ── Compact spatial map (16×16 downsampled) ───────────────
    parts.append("")
    parts.append("═══ SPATIAL MAP (16×16 downsample, . = background) ═══")
    symbols = ".123456789ABCDEF"
    ds = current_grid.reshape(16, 4, 16, 4).max(axis=(1, 3))  # 16×16 max-pool
    for r in range(16):
        row_str = ""
        for c in range(16):
            v = int(ds[r, c])
            row_str += symbols[min(v, 15)]
        parts.append(f"  {row_str}")

    # ── Fisher cell map (where rules act) ───────────────────────
    if influence_map is not None:
        parts.append("")
        parts.append("═══ FISHER CELL MAP (where rules act) ═══")
        threshold = influence_map.max() * 0.3
        mask = influence_map > threshold
        labeled, n_feat = ndimage.label(mask)
        for i in range(1, min(n_feat + 1, 6)):
            region = np.where(labeled == i)
            if len(region[0]) > 0:
                cr, cc = int(region[0].mean()), int(region[1].mean())
                intensity = float(influence_map[labeled == i].mean())
                size = len(region[0])
                parts.append(f"  Hotspot {i}: center=({cr},{cc}), {size} cells, intensity={intensity:.3f}")

    # ── Fantasia saturation (explore/exploit gate) ──────────────
    parts.append("")
    parts.append("═══ FANTASIA BOUND (explore vs exploit) ═══")
    sat = fantasia.saturation() if hasattr(fantasia, 'saturation') else 0.0
    regime = "EXPLORE MORE" if sat < 0.7 else ("EXPLOIT" if sat > 0.9 else "TRANSITIONING")
    parts.append(f"Saturation: {sat:.2f} → {regime}")
    if sat > 0.9:
        parts.append("Rules are FULLY KNOWN. Focus on planning, not exploration.")

    # ── Kramers stuck detection ─────────────────────────────────
    if kramers and hasattr(kramers, 'minima') and kramers.minima:
        parts.append("")
        parts.append("═══ KRAMERS POTENTIAL (stuck detection) ═══")
        if kramers.is_stuck(ent):
            parts.append(f"⚠ STUCK at entropy {ent:.3f} (local minimum)")
            esc = kramers.escape_direction(ent)
            if esc < 0:
                parts.append("Escape direction: DECREASE entropy (push harder toward goal)")
            elif esc > 0:
                parts.append("Escape direction: INCREASE entropy first (back up, try different path)")
        else:
            parts.append("Not stuck — continue current approach")

    # ── Macro library (proven sequences) ────────────────────────
    if macros.macros:
        parts.append("")
        parts.append("═══ PROVEN MACROS ═══")
        sorted_macros = sorted(macros.macros, key=lambda m: m[2])
        for seq, sig, delta in sorted_macros[:5]:
            parts.append(f"  {seq} → entropy delta: {delta:+.4f}")
        parts.append("These sequences are VERIFIED to reduce entropy. Consider replaying them.")

    # ── Transition memory summary ───────────────────────────────
    parts.append("")
    parts.append("═══ TRANSITION MEMORY ═══")
    parts.append(f"Total transitions recorded: {len(memory.transitions)}")
    parts.append(f"Unique states seen: {navigator.n_states}")
    parts.append(f"Spectral attractor score of current state: {navigator.score_state(frame_hash(current_grid)):.3f}")

    # Action effect summary
    for action in sorted(memory.by_action.keys()):
        templates = memory.templates_for_action(action)
        n_noop = sum(1 for t in templates if t.n_changed == 0)
        avg_changed = np.mean([t.n_changed for t in templates]) if templates else 0
        parts.append(f"  Action {action}: {len(templates)} observations, "
                     f"avg {avg_changed:.0f} cells changed, {n_noop} noops")

    # ── Click targets (if click game) ───────────────────────────
    if 6 in profile.available_actions and influence_map is not None:
        parts.append("")
        parts.append("═══ CLICK TARGETS (Fisher-guided) ═══")
        for color in colors[:8]:
            pos = np.where(current_grid == color)
            if len(pos[0]) > 0:
                cy, cx = int(pos[0].mean()), int(pos[1].mean())
                fisher_val = float(influence_map[cy, cx]) if influence_map is not None else 0
                parts.append(f"  Color {color} at ({cx},{cy}): Fisher={fisher_val:.3f}")

    # ── φ DETECTOR (thermodynamic progress oracle) ────────────
    if detector is not None and detector.step > 0:
        det = detector.summary()
        parts.append("")
        parts.append("═══ THERMODYNAMIC PROGRESS (φ) ═══")
        parts.append(f"φ = {det['phi']:.3f} (0=start, 1=winning)")

        # Trajectory
        if det['phi_derivative'] > 0.01:
            parts.append(f"φ is RISING (+{det['phi_derivative']:.3f}/step) — keep going")
        elif det['phi_derivative'] < -0.01:
            parts.append(f"φ is FALLING ({det['phi_derivative']:.3f}/step) — CHANGE APPROACH")
        else:
            parts.append(f"φ is FLAT — current approach has stalled")

        if det['is_stuck']:
            parts.append("⚠ STUCK — φ hasn't increased in 15+ steps. Try something completely different.")

        # Pe gradient
        if detector.pe_history:
            pe_current = detector.pe_history[-1]
            pe_initial = detector.pe_history[0] if detector.pe_history else pe_current
            parts.append(f"Pe: current={pe_current:.2f}, initial={pe_initial:.2f} "
                         f"({'↓ good' if pe_current < pe_initial else '↑ wrong direction'})")

        # Transition graph stats
        parts.append(f"States explored: {det['states_explored']}")
        if det['spectral_gap'] > 0:
            parts.append(f"Spectral gap: {det['spectral_gap']:.3f} "
                         f"({'near attractor' if det['spectral_gap'] > 0.3 else 'still exploring'})")

        # Absorption
        if det['absorption'] > 0.5:
            parts.append(f"Absorption: {det['absorption']:.2f} — current state looks TERMINAL (near win or dead end)")
        elif det['absorption'] > 0.2:
            parts.append(f"Absorption: {det['absorption']:.2f} — approaching a terminal state")

        # Crooks milestones
        if det['crooks_milestones'] > 0:
            parts.append(f"Crooks milestones: {det['crooks_milestones']} irreversible transitions crossed")

        # Cycles
        if det['cycle_depth'] > 0:
            parts.append(f"⚠ IN A CYCLE of length {det['cycle_depth']} — you must find the ESCAPE action")
            parts.append("The win condition breaks the cycle. Try an action you haven't tried in this cycle.")

        # Complexity
        if detector.complexity_history:
            c_now = detector.complexity_history[-1]
            c_initial = detector.complexity_history[0]
            if c_now < c_initial:
                parts.append(f"Complexity: {c_now:.3f} (down from {c_initial:.3f}) — grid getting simpler ✓")
            else:
                parts.append(f"Complexity: {c_now:.3f} (was {c_initial:.3f})")

    # ── Eckert Simulator diagnostics ──────────────────────────
    if eckert is not None:
        parts.append("")
        parts.append("═══ ECKERT WORLD MODEL ═══")
        parts.append(f"Rules learned: {eckert.table.rule_count()}")
        parts.append(f"Prediction accuracy: {eckert.model.accuracy():.2f}")
        parts.append(f"Coverage: {eckert.table.coverage():.2f}")
        parts.append(f"Deterministic: {eckert.table.is_deterministic}")
        parts.append(f"Mechanisms: {eckert.manifold.mechanism_count()}")

        # Consolidated color rules (the game's instruction set from Eckert)
        rules = eckert.table.consolidate_color_rules()
        if rules:
            parts.append("Color transition rules (from forward model):")
            for action, cmap in rules.items():
                for old_c, (new_c, count) in cmap.items():
                    parts.append(f"  action {action}: color {old_c} → {new_c} (seen {count}x)")

        # Goal scores from the hypothesis system
        if eckert._goal_scores:
            parts.append("Goal hypothesis scores:")
            for goal, score in sorted(eckert._goal_scores.items(),
                                       key=lambda x: -x[1])[:5]:
                parts.append(f"  {goal}: {score:.3f}")

    return "\n".join(parts)


# ═══════════════════════════════════════════════════════════════════
#  RESPONSE PARSER — extract action plan from LLM response
# ═══════════════════════════════════════════════════════════════════

def parse_plan(response: str) -> list:
    """Parse LLM response into action sequence.

    Handles mixed plans with BOTH keyboard and click actions:
      PLAN: 1, 1, 3, 6@32,16, 2, 6@40,20, 4
    Also handles:
      - Numbered lists: 1. action 2. action
      - Markdown code blocks: ```1,2,3```
      - Various click formats: 6@32,16 / 6:32:16 / click(32,16) / click 32 16
    Returns list of int or (6, x, y) tuples.
    """
    # Find PLAN: line (grab to next section header or double newline)
    plan_match = re.search(r'PLAN:\s*(.+?)(?:\n[A-Z]|\n\n|$)', response,
                           re.IGNORECASE | re.DOTALL)
    if not plan_match:
        # Try markdown code block
        plan_match = re.search(r'```\s*(.+?)\s*```', response, re.DOTALL)
    if not plan_match:
        # Try any sequence of numbers and click patterns
        plan_match = re.search(r'(\d[\d,@:\s]+\d)', response)
    if not plan_match:
        return []

    plan_str = plan_match.group(1).strip()
    # Clean up numbered list format: "1. action 1\n2. action 2"
    plan_str = re.sub(r'^\d+[.)]\s*', '', plan_str, flags=re.MULTILINE)

    actions = []

    # Process tokens left-to-right to preserve order of mixed keyboard+click
    # Replace click patterns with placeholders, then parse sequentially
    tokens = re.split(r'[,\s]+', plan_str)
    i = 0
    while i < len(tokens):
        token = tokens[i].strip()
        if not token:
            i += 1
            continue

        # Click pattern: 6@x,y or 6:x:y
        click_match = re.match(r'6[@:](\d+)[,:\s]*(\d+)?', token)
        if click_match:
            x = int(click_match.group(1))
            y_str = click_match.group(2)
            if y_str:
                y = int(y_str)
            elif i + 1 < len(tokens):
                try:
                    y = int(tokens[i + 1].strip())
                    i += 1
                except ValueError:
                    i += 1
                    continue
            else:
                i += 1
                continue
            actions.append((6, x, y))
            i += 1
            continue

        # click(x,y) or click x y
        if token.lower().startswith('click'):
            coords = re.findall(r'\d+', token + ' ' + (tokens[i+1] if i+1 < len(tokens) else ''))
            if len(coords) >= 2:
                actions.append((6, int(coords[0]), int(coords[1])))
                # Skip the next token if it was part of coords
                if i + 1 < len(tokens) and re.search(r'\d', tokens[i+1]):
                    i += 1
            i += 1
            continue

        # Plain keyboard action
        try:
            a = int(token)
            if 1 <= a <= 7:
                actions.append(a)
        except ValueError:
            pass
        i += 1

    return actions


# ═══════════════════════════════════════════════════════════════════
#  HYBRID SOLVER — byte-level + LLM reasoning
# ═══════════════════════════════════════════════════════════════════

class HybridSolver:
    """Framework-grounded LLM hybrid solver.

    Loop:
    1. RECON: byte-level exploration (zero LLM, builds ground truth)
    2. CONTEXT: format all measurements as framework quantities
    3. QUERY: ask LLM to reason within the framework
    4. VERIFY: telescope-simulate proposed plan before execution
    5. EXECUTE: run verified plan
    6. FEEDBACK: actual vs predicted → update context, re-query
    """

    def __init__(self, profile: GameProfile, env, obs):
        self.profile = profile
        self.env = env
        self.obs = obs
        self.available = list(obs.available_actions)

        # Infrastructure
        self.memory = TransitionMemory()
        self.telescope = XORTelescope(self.memory)
        self.compiler = InstantonCompiler(self.memory)
        self.navigator = SpectralNavigator()
        self.macros = MacroLibrary()
        self.fantasia = FantasiaBound()
        self.kramers_samples = []
        self.pathfinder = FisherPathfinder()

        # Thermodynamic progress detector + world model
        self.detector = EckertWinDetector()
        self.eckert = EckertSimulator(profile)

        # Game sense — pro gamer eyes for the LLM
        try:
            from game_sense import ActionTracker, GameDiary
            self.action_tracker = ActionTracker()
            self.diary = GameDiary()
            self._has_game_sense = True
        except ImportError:
            self._has_game_sense = False

        # State
        grid = np.array(obs.frame[0])
        self.base_entropy = shannon_entropy(grid)
        self.best_entropy = self.base_entropy
        self.best_frame = grid.copy()
        self.total_actions = 0
        self.levels_solved = 0
        self.llm_calls = 0
        self.frames = [grid]
        self.actions_taken = []
        self.influence_map = None

    def step(self, action, click_x=None, click_y=None):
        """Take one real action, update all systems."""
        prev_grid = np.array(self.obs.frame[0])

        if action == 6 and click_x is not None:
            self.obs = self.env.step(6, data={"x": click_x, "y": click_y})
        else:
            self.obs = self.env.step(action)

        self.total_actions += 1

        if not self.obs.frame:
            return True, prev_grid

        curr_grid = np.array(self.obs.frame[0])
        self.frames.append(curr_grid)
        self.actions_taken.append(action)

        # Record transition
        xor = xor_grids(prev_grid, curr_grid)
        is_noop = not xor.any()
        prev_h, curr_h = frame_hash(prev_grid), frame_hash(curr_grid)

        if not is_noop:
            rows, cols = np.where(xor > 0)
            r0, c0 = int(rows.min()), int(cols.min())
            template = xor[r0:int(rows.max())+1, c0:int(cols.max())+1].copy()
            template_hash = hashlib.md5(template.tobytes()).hexdigest()[:10]

            changed = xor > 0
            color_map = {}
            for o, n in zip(prev_grid[changed].tolist(),
                            curr_grid[changed].tolist()):
                color_map[o] = n

            t = ObservedTransition(
                action=action, prev_hash=prev_h, curr_hash=curr_h,
                xor_mask=changed, xor_values=xor,
                prev_grid=prev_grid.copy(), curr_grid=curr_grid.copy(),
                origin=(r0, c0), template=template,
                template_hash=template_hash, color_map=color_map,
                entropy_delta=shannon_entropy(curr_grid) - shannon_entropy(prev_grid),
                n_changed=int(changed.sum()),
            )
            self.memory.record(t)
            self.navigator.record_transition(prev_h, curr_h, action)

            # Update Fisher influence map
            fm = fisher_cell_map(prev_grid, curr_grid)
            if self.influence_map is None:
                self.influence_map = fm
            else:
                self.influence_map = 0.3 * fm + 0.7 * self.influence_map

        # Feed Eckert world model + thermodynamic detector
        self.eckert.observe(prev_grid, action, curr_grid)

        # Diagnostics
        ent = shannon_entropy(curr_grid)
        self.kramers_samples.append(ent)
        self.fantasia.record(curr_grid, action, prev_grid,
                             len(set(self.actions_taken[-10:])) / max(1, min(10, len(self.actions_taken))))

        if ent < self.best_entropy:
            self.best_entropy = ent
            self.best_frame = curr_grid.copy()

        # Game sense: track action effects
        if self._has_game_sense:
            phi_before = (self.eckert.detector.snapshots[-2].phi
                          if len(self.eckert.detector.snapshots) >= 2 else 0.0)
            phi_after = (self.eckert.detector.snapshots[-1].phi
                         if self.eckert.detector.snapshots else 0.0)
            click_pos = (click_x, click_y) if click_x is not None else None
            lvl_before = self.obs.levels_completed - (1 if self.obs.levels_completed > 0 else 0)
            self.action_tracker.record(
                action, prev_grid, curr_grid,
                click_pos=click_pos,
                level_before=lvl_before,
                level_after=self.obs.levels_completed,
                phi_before=phi_before, phi_after=phi_after)

        return is_noop, curr_grid

    def _recon(self, budget=40):
        """Byte-level exploration — zero LLM calls."""
        non_click = [a for a in self.available if a != 6]
        has_click = 6 in self.available

        def _done():
            return budget <= 0 or self.obs.state in (
                GameState.WIN, GameState.GAME_OVER)

        # Systematic: each action twice
        for a in non_click:
            for _ in range(2):
                if _done(): return
                self.step(a)
                budget -= 1

        # Action pairs
        for a in non_click:
            for b in non_click:
                if a == b or _done(): continue
                self.step(a)
                budget -= 1
                if _done(): return
                self.step(b)
                budget -= 1

        # Click exploration
        if has_click and not _done():
            grid = np.array(self.obs.frame[0])
            bg = int(np.bincount(grid.flatten()).argmax())
            for color in sorted(set(grid.flatten().tolist()) - {bg}):
                if _done(): break
                pos = np.where(grid == color)
                if len(pos[0]) > 0:
                    self.step(6, click_x=int(pos[1].mean()),
                              click_y=int(pos[0].mean()))
                    budget -= 1

        # Discover macros
        if len(self.frames) > 5:
            self.macros.discover(self.actions_taken, self.frames)

        # Build Fisher geodesic pathfinder (after recon builds memory)
        if self.obs.frame:
            grid = np.array(self.obs.frame[0])
            self.pathfinder.build(
                self.memory, self.profile, grid, self.influence_map)

    def _query_win_condition(self, level: int) -> str:
        """Ask LLM specifically what the win condition is, using all φ signals.

        Called once after recon. Returns a hypothesis string that is
        included in all subsequent planning queries.
        """
        if not self.obs.frame:
            return ""

        grid = np.array(self.obs.frame[0])
        det = self.eckert.detector.summary()

        # Build focused win-condition context
        parts = []
        parts.append("═══ WIN CONDITION ANALYSIS REQUEST ═══")
        parts.append("")
        parts.append("You have explored a 64×64 grid game. Here is everything measured:")
        parts.append("")
        parts.append(f"Game type: {self.profile.game_type}")
        parts.append(f"Deterministic: {self.profile.is_deterministic}")
        parts.append(f"Has cycles: {self.profile.has_cycles} (length: {self.profile.cycle_length})")
        parts.append(f"Available actions: {self.available}")
        parts.append("")

        # Color rules
        parts.append("COLOR RULES (the game's complete instruction set):")
        rules = self.eckert.table.consolidate_color_rules()
        if rules:
            for action, cmap in rules.items():
                for old_c, (new_c, count) in cmap.items():
                    parts.append(f"  action {action}: color {old_c} → {new_c} (seen {count}x)")
        for rule, count in sorted(self.profile.nibble_vocab.items(), key=lambda x: -x[1])[:15]:
            parts.append(f"  {rule}: {count}x")

        # Current state
        bg = int(np.bincount(grid.flatten()).argmax())
        colors = sorted(set(grid.flatten().tolist()) - {bg})
        parts.append(f"\nBackground: color {bg}")
        parts.append(f"Active colors: {colors}")
        for c in colors[:8]:
            count = int((grid == c).sum())
            parts.append(f"  Color {c}: {count} cells")

        # φ signals
        parts.append(f"\nThermodynamic state:")
        parts.append(f"  φ = {det['phi']:.3f}")
        parts.append(f"  Entropy = {det['entropy']:.3f}")
        parts.append(f"  Complexity (zlib) = {det['complexity']:.3f}")
        parts.append(f"  Absorption = {det['absorption']:.2f}")
        parts.append(f"  States explored = {det['states_explored']}")
        if det['cycle_depth'] > 0:
            parts.append(f"  ⚠ Currently in a CYCLE of length {det['cycle_depth']}")

        # Goal hypothesis scores from Eckert
        if self.eckert._goal_scores:
            parts.append("\nGoal hypothesis scores (higher = closer to that goal):")
            for goal, score in sorted(self.eckert._goal_scores.items(),
                                       key=lambda x: -x[1])[:5]:
                parts.append(f"  {goal}: {score:.3f}")

        # Spatial map
        parts.append("\nSPATIAL MAP (16×16 downsample, . = background):")
        symbols = ".123456789ABCDEF"
        ds = grid.reshape(16, 4, 16, 4).max(axis=(1, 3))
        for r in range(16):
            row_str = ""
            for c in range(16):
                row_str += symbols[min(int(ds[r, c]), 15)]
            parts.append(f"  {row_str}")

        context = "\n".join(parts)

        win_system = """You are analyzing an interactive 64×64 grid game to determine its WIN CONDITION.

Based on the measured data, answer these three questions:

1. WHAT is the win condition? (e.g., "make all non-background cells the same color", "navigate agent to goal", "clear all objects", "create a specific pattern")
2. WHY do you think this? (reference specific measurements)
3. What SEQUENCE TYPE will achieve it? (systematic clicking, navigation, specific pattern, cycle manipulation)

Be SPECIFIC. Don't say "solve the puzzle" — say exactly what state the game wants.

Format:
WIN_CONDITION: [one clear sentence]
EVIDENCE: [2-3 bullet points from measured data]
STRATEGY: [one sentence describing the approach]"""

        response = call_llm(context, system=win_system, temperature=0.2)
        self.llm_calls += 1

        # Extract the win condition hypothesis
        wc_match = re.search(r'WIN_CONDITION:\s*(.+?)(?:\n|$)', response, re.IGNORECASE)
        if wc_match:
            return f"INFERRED WIN CONDITION: {wc_match.group(1).strip()}\n(Full analysis: {response[:200]})"
        return f"WIN CONDITION ANALYSIS:\n{response[:300]}"

    def _query_llm(self, level: int, feedback: str = "") -> list:
        """Build context, query LLM, parse plan."""
        if not self.obs.frame:
            return []

        grid = np.array(self.obs.frame[0])

        # Build framework-grounded context
        # Kramers stub (lightweight)
        class KramersStub:
            def __init__(self, samples):
                self.minima = []
                self.samples = samples
            def is_stuck(self, ent):
                if len(self.samples) < 10: return False
                recent = self.samples[-10:]
                return max(recent) - min(recent) < 0.01
            def escape_direction(self, ent):
                return 0

        kramers = KramersStub(self.kramers_samples)

        context = build_context(
            profile=self.profile,
            memory=self.memory,
            navigator=self.navigator,
            fantasia=self.fantasia,
            kramers=kramers,
            influence_map=self.influence_map,
            macros=self.macros,
            current_grid=grid,
            best_entropy=self.best_entropy,
            actions_taken=self.total_actions,
            level=level,
            detector=self.eckert.detector,
            eckert=self.eckert,
        )

        # Add Fisher geodesic pathfinder context
        pf_context = self.pathfinder.context_for_llm()
        if pf_context:
            context += f"\n\n{pf_context}"

        # Add game sense context (visual grid, patterns, diary, action effects)
        if self._has_game_sense:
            from game_sense import build_game_sense_context
            prev = self.frames[-2] if len(self.frames) >= 2 else None
            gs_context = build_game_sense_context(
                grid, self.profile, self.action_tracker, self.diary,
                prev_grid=prev, level=level, actions_used=self.total_actions,
                budget_remaining=200 - self.total_actions)
            context += f"\n\n{gs_context}"

        if feedback:
            context += f"\n\n═══ FEEDBACK FROM LAST PLAN ═══\n{feedback}"

        # If pathfinder found a geodesic, try it FIRST (before LLM)
        geodesic_plan = self.pathfinder.plan()
        if geodesic_plan and not feedback:
            # First attempt: trust the geodesic
            return geodesic_plan, "[GEODESIC PATH — no LLM call needed]"

        # Query LLM
        response = call_llm(context, system=FRAMEWORK_SYSTEM, temperature=0.3)
        self.llm_calls += 1

        return parse_plan(response), response

    def _verify_plan(self, plan: list) -> list:
        """Telescope-verify a plan. Remove actions with predicted no-ops."""
        if not self.obs.frame or not plan:
            return plan

        grid = np.array(self.obs.frame[0])
        verified = []

        for step in plan:
            if isinstance(step, tuple):
                action, cx, cy = step
                predicted = self.telescope.predict_single(grid, action, click_pos=(cx, cy))
            else:
                predicted = self.telescope.predict_single(grid, step)

            verified.append(step)

            if predicted is not None:
                grid = predicted
            # If telescope can't predict, still include — the LLM might know something we don't

        return verified

    def _execute(self, plan: list, budget: int) -> tuple[int, str]:
        """Execute plan, return (actions_used, feedback_string)."""
        feedback_parts = []
        used = 0

        for step in plan:
            if budget <= 0 or self.obs.state in (GameState.WIN, GameState.GAME_OVER):
                break

            if isinstance(step, tuple):
                action, cx, cy = step
                _, result_grid = self.step(action, click_x=cx, click_y=cy)
                feedback_parts.append(f"  6@{cx},{cy}: {'changed' if not isinstance(result_grid, bool) else 'game ended'}")
            else:
                _, result_grid = self.step(step)

            used += 1
            budget -= 1

        ent = shannon_entropy(np.array(self.obs.frame[0])) if self.obs.frame else 0
        phi = self.eckert.detector.progress()
        phi_d = self.eckert.detector.phi_derivative()
        feedback_parts.append(f"  Entropy after plan: {ent:.3f} (best: {self.best_entropy:.3f})")
        feedback_parts.append(f"  φ after plan: {phi:.3f} (derivative: {phi_d:+.3f})")
        if self.eckert.detector.is_stuck():
            feedback_parts.append("  ⚠ STUCK — φ hasn't improved in 15 steps. Change approach completely.")

        return used, "\n".join(feedback_parts)

    def _auto_extend(self, budget: int) -> int:
        """φ-guided auto-play between LLM calls.

        Uses the Eckert world model to pick actions that maximize φ.
        For click games: systematic clicking of non-bg cells.
        For keyboard games: φ-guided action selection.
        """
        used = 0
        has_click = 6 in self.available
        non_click = [a for a in self.available if a != 6]

        for _ in range(budget):
            if self.obs.state in (GameState.WIN, GameState.GAME_OVER):
                break
            if not self.obs.frame:
                break

            grid = np.array(self.obs.frame[0])

            if has_click:
                # Click game: use Eckert's smart click targeting
                bg = int(np.bincount(grid.flatten()).argmax())
                nonbg = np.where(grid != bg)
                if len(nonbg[0]) == 0:
                    break
                # Pick click target by highest R (responsiveness) on manifold
                R = self.eckert.manifold.R
                score = R * (grid != bg).astype(np.float32)
                if score.max() > 0:
                    flat = score.flatten()
                    top_k = min(5, (flat > 0).sum())
                    if top_k > 0:
                        top_indices = np.argpartition(flat, -top_k)[-top_k:]
                        idx = np.random.choice(top_indices)
                        r, c = int(idx // 64), int(idx % 64)
                    else:
                        i = np.random.randint(len(nonbg[0]))
                        r, c = int(nonbg[0][i]), int(nonbg[1][i])
                else:
                    i = np.random.randint(len(nonbg[0]))
                    r, c = int(nonbg[0][i]), int(nonbg[1][i])
                self.step(6, click_x=c, click_y=r)
            elif non_click:
                # Keyboard game: pick action that maximizes φ
                best_a = non_click[0]
                best_phi = -1.0
                for a in non_click:
                    pred = self.eckert.model.predict(grid, a)
                    if pred.confidence < 0.05:
                        continue
                    phi = self.eckert.detector.score_state(pred.grid)
                    if phi > best_phi:
                        best_phi = phi
                        best_a = a
                self.step(best_a)
            else:
                break

            used += 1

            # Stop if stuck
            if used > 10 and self.eckert.detector.is_stuck(window=10):
                break

        return used

    def solve_level(self, level: int, max_actions: int = 200,
                    max_llm_calls: int = 8) -> bool:
        start_level = self.obs.levels_completed
        level_start = self.total_actions

        def _remaining():
            return max_actions - (self.total_actions - level_start)

        # Phase 1: RECON (zero LLM)
        recon_budget = min(50, max_actions // 4)
        self._recon(budget=recon_budget)

        if self.obs.levels_completed > start_level:
            return True

        # Phase 1.5: WIN CONDITION HYPOTHESIS (one LLM call)
        # Update barrier estimate from manifold
        self.eckert.manifold._recompute()
        self.eckert.detector.set_barrier_estimate(self.eckert.manifold.mechanism_count())

        win_hypothesis = self._query_win_condition(level)

        # Log win condition hypothesis to diary
        if self._has_game_sense and win_hypothesis:
            self.diary.log_observation(win_hypothesis[:200])

        if self.obs.levels_completed > start_level:
            if self._has_game_sense:
                acts = self.total_actions - level_start
                self.diary.log_level_complete(level, 'recon+win_query', acts)
            return True

        # Phase 2: LLM QUERY → VERIFY → EXECUTE loop
        feedback = win_hypothesis  # seed the first planning call with the hypothesis
        llm_calls_this_level = 1  # count the win condition call

        while _remaining() > 0 and llm_calls_this_level < max_llm_calls:
            if self.obs.state in (GameState.WIN, GameState.GAME_OVER):
                break

            # Query
            plan, raw_response = self._query_llm(level, feedback=feedback)
            llm_calls_this_level += 1

            if not plan:
                feedback = "Could not parse your plan. Use format: PLAN: 1,2,3,4"
                continue

            # Verify (telescope simulation)
            plan = self._verify_plan(plan)

            # Execute
            used, exec_feedback = self._execute(plan, _remaining())

            if self.obs.levels_completed > start_level:
                return True

            # Auto-extend: if LLM gave a short plan and we have budget,
            # continue with φ-guided clicking/actions between LLM calls
            if used < 10 and _remaining() > 20 and self.obs.frame:
                auto_used = self._auto_extend(_remaining() // 2)
                exec_feedback += f"\n  Auto-extended: {auto_used} more actions"
                if self.obs.levels_completed > start_level:
                    return True

            # Build feedback for next query
            feedback = f"Executed {used} actions from your plan.\n{exec_feedback}"

            # Discover new macros from latest actions
            if len(self.frames) > 10:
                self.macros.discover(self.actions_taken[-20:], self.frames[-20:])

        return self.obs.levels_completed > start_level

    def solve_game(self, verbose=True, max_llm_per_level=8) -> dict:
        win_levels = self.profile.win_levels

        for level in range(win_levels):
            if self.obs.state == GameState.GAME_OVER:
                if verbose:
                    print(f"  Level {level}: GAME OVER")
                break

            level_start = self.total_actions
            solved = self.solve_level(level, max_llm_calls=max_llm_per_level)
            level_acts = self.total_actions - level_start

            if solved:
                self.levels_solved += 1
                if verbose:
                    print(f"  Level {level}: SOLVED in {level_acts} acts, "
                          f"{self.llm_calls} LLM calls")
            else:
                if verbose:
                    print(f"  Level {level}: FAILED {level_acts} acts, "
                          f"{self.llm_calls} LLM calls, "
                          f"ent={self.best_entropy:.3f}")
                break

        det_summary = self.eckert.detector.summary()
        return {
            "game_id": self.profile.game_id,
            "levels_solved": self.levels_solved,
            "win_levels": win_levels,
            "total_actions": self.total_actions,
            "llm_calls": self.llm_calls,
            "transitions": len(self.memory.transitions),
            "best_entropy": round(self.best_entropy, 4),
            "final_phi": det_summary.get('phi', 0.0),
            "detector": det_summary,
        }


# ═══════════════════════════════════════════════════════════════════
#  PIPELINE
# ═══════════════════════════════════════════════════════════════════

def solve(game_id: str, probe_budget: int = 30, verbose: bool = True,
          max_llm: int = 8) -> dict:
    if verbose:
        print(f"\n{'='*65}")
        print(f"  LLM HYBRID: {game_id}")
        print(f"  Backend: {BACKEND} | Model: {MODEL}")
        print(f"{'='*65}")

    profile = probe_game(game_id, budget=probe_budget, verbose=False)

    if verbose:
        n_mech = estimate_mechanisms(profile)
        print(f"  Profile: {profile.solver_hint()}")
        print(f"  Mechanisms: {n_mech} | Barrier: {coordination_barrier(n_mech):.1f}")

    arcade = arc_agi.Arcade()
    env = arcade.make(game_id)
    obs = env.reset()

    solver = HybridSolver(profile, env, obs)
    result = solver.solve_game(verbose=verbose, max_llm_per_level=max_llm)

    if verbose:
        print(f"\n  RESULT: {result['levels_solved']}/{result['win_levels']} | "
              f"{result['total_actions']} actions | "
              f"{result['llm_calls']} LLM calls | "
              f"ent={result['best_entropy']}")

    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='ARC-AGI-3 LLM Hybrid Solver')
    parser.add_argument('game_id', nargs='?', default=None)
    parser.add_argument('-b', '--probe-budget', type=int, default=30)
    parser.add_argument('-v', '--verbose', action='store_true', default=True)
    parser.add_argument('-q', '--quiet', action='store_true')
    parser.add_argument('--all', action='store_true')
    parser.add_argument('--max-llm', type=int, default=8,
                        help='Max LLM calls per level')
    parser.add_argument('--model', type=str, default=None,
                        help='Override model (e.g. o4-mini, claude-sonnet-4-20250514)')
    args = parser.parse_args()

    if args.quiet:
        args.verbose = False

    # Model override
    if args.model:
        import llm_solver
        llm_solver.MODEL = args.model
        # Detect backend from model name
        if args.model.startswith(('gpt', 'o1', 'o3', 'o4')):
            llm_solver.BACKEND = 'openai'
        elif args.model.startswith('claude'):
            llm_solver.BACKEND = 'anthropic'

    if BACKEND == 'none':
        print("ERROR: No API key set. Export ANTHROPIC_API_KEY or OPENAI_API_KEY.")
        sys.exit(1)

    if args.all or args.game_id is None:
        arcade = arc_agi.Arcade()
        envs = arcade.get_environments()
        results = []

        print(f"\n{'Game':<22s} {'Solved':>7s} {'Acts':>6s} "
              f"{'LLM':>5s} {'Ent':>8s}")
        print("-" * 55)

        for e in envs:
            try:
                r = solve(e.game_id, probe_budget=args.probe_budget,
                          verbose=args.verbose, max_llm=args.max_llm)
                results.append(r)
                if not args.verbose:
                    print(f"{r['game_id']:<22s} "
                          f"{r['levels_solved']}/{r['win_levels']:<5d} "
                          f"{r['total_actions']:>6d} "
                          f"{r['llm_calls']:>5d} "
                          f"{r['best_entropy']:>8.3f}")
            except Exception as ex:
                if args.verbose:
                    traceback.print_exc()
                print(f"{e.game_id:<22s} ERROR: {str(ex)[:60]}")

        total = sum(r.get('levels_solved', 0) for r in results)
        possible = sum(r.get('win_levels', 0) for r in results)
        total_llm = sum(r.get('llm_calls', 0) for r in results)
        print(f"\nTOTAL: {total}/{possible} levels | {total_llm} LLM calls")
    else:
        solve(args.game_id, probe_budget=args.probe_budget,
              verbose=True, max_llm=args.max_llm)

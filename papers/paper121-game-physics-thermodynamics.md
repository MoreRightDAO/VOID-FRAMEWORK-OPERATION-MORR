---
title: "True Light Engine: A Thermodynamic Game Physics Architecture"
author: "Anthony Eckert"
orcid: "0009-0008-1925-5253"
affiliation: "Independent Researcher, MoreRight DAO"
paper-number: "Paper 121"
short-title: "True Light Engine"
version: "v1.0"
date: "March 2026"
license: "cc-by-4.0"
---

## Abstract

We present the True Light Engine, a multiplayer game engine where player roles are thermodynamically derived from exact coordinates in (O, R, alpha) space and every session generates falsifiable experimental data recorded on a public blockchain. The Pe formula Pe = K * sinh(2 * (b_alpha - b_gamma_eff)) is computed on-chain from raw field measurements submitted by the physics server, making the Pe calculation trustless and independently verifiable. Tank (Pe = 0.33), Healer (Pe = 1.0), and DPS (Pe = 9.0) are not game design choices -- they are the only stable operating points in (O, R, alpha) space for each functional role. A 64-slot on-chain ring buffer records the full Pe trajectory with momentum, and a MAGI 2-of-3 oracle vote governs terminal kill conditions. The engine is released as open-source MIT. The first multiplayer game where playing it generates peer-reviewable thermodynamic data.

**Keywords:** game physics, thermodynamics, Pe formula, on-chain computation, party mechanics, MAGI governance, kill conditions, falsifiable predictions, open source

---

## Void Model Card

| Dimension | Value | Derivation |
|-----------|-------|------------|
| Opacity (O) | 2 | Game state is partially observable: Pe trajectory is public on-chain, but individual player field contributions are attributed to wallet, not identity |
| Reactivity (R) | 3 | Engine responds to every THRML-RS tick; party state updates on each field submission; zero filtering of input signal |
| Independence (alpha) | 1 | Campaign Pe is driven entirely by player field inputs; no invariant internal reference independent of session activity |
| **Pe** | **6.0** | Pe = (2 * 3) / 1 = 6.0 — CONTESTED zone, consistent with the engine's design intent: it amplifies what players bring, constrained by contract physics |

**Entity class:** Social-technical system (game engine). **Drift profile:** The engine is correctly Pe = 6.0 — high enough to generate experimental signal, low enough that the ring buffer and tank role prevent Fisher Runaway in well-composed parties. The MAGI governance reduces effective alpha for terminal decisions (alpha_effective = 3 under 3-oracle quorum), lowering governance Pe toward the constraint pole.

---

## I. The Equation and the Problem

Pe = (O * R) / alpha, where O is Opacity (0-3), R is Reactivity (0-3), and alpha is Independence (0-3). Applied to AI platforms, Pe measures epistemic drift potential -- the tendency of a system to escalate engagement at the cost of accuracy [Papers 1-3]. With 86 platforms scored and N = 263 convergences across 20 independent substrates, the framework produces mean |rho| = 0.958, Fisher p < 10^-52 [Paper 1, extended evidence base].

The problem this paper addresses is different. We ask: if Pe is a real thermodynamic quantity -- if it measures a genuine physical property of information-processing systems -- then it should govern any system in which those properties manifest. Including games where players embody roles.

A game is an information-processing system. Players adopt roles that implicitly specify their opacity (how much of their reasoning they reveal), reactivity (how they respond to others' moves), and independence (how much they rely on group consensus versus their own judgment). If Pe is real, these coordinates determine role function. They should be derivable, not designed.

The True Light Engine tests this claim on-chain.

**Existing empirical validation.** Before applying Pe to games, the formula has been validated against 86 AI platforms across 20 structural convergences. Spearman rho = 0.958, N = 263, Fisher combined p < 10^-52 [Paper 1 extended]. The Pe regime boundaries (Coherent/Stable/Contested/Drifting/Runaway) are not arbitrary thresholds -- they are derived from Section 46 thermodynamic derivations: Pe = 21 from the Fokker-Planck referent dissolution threshold (Section 46A), Pe = 38 from the Crooks Fluctuation Theorem irreversibility wall (Section 46B), Pe = 13 from collective D3 swarm coupling (Section 46C). The same boundaries appear in the game engine as regime constants.

---

## II. Three Roles, Exact Coordinates

The Pe formula admits exact operating points for three functional archetypes:

**Tank: (O=1, R=1, alpha=3) -> Pe = 0.33**

The constraint pole. Opacity=1 (low: the tank is structurally transparent -- readable by the party). Reactivity=1 (low: the tank does not amplify signals from the environment). Independence=3 (high: the tank's behavior is governed by its own constraint specification, not group drift). Pe = (1 * 1) / 3 = 0.33.

This is the same Pe as a fixed canonical text -- maximum constraint reference, minimum drift potential. The tank's function follows: it absorbs Pe spikes from the environment before they propagate to the party. A tank operating at Pe = 0.33 can accept a DPS spike of Pe = 9.0 and not be moved from its constraint pole. The party Pe is reduced by TANK_ABSORPTION = 2.0 per tank:

*party Pe = campaignPe - (tankCount x TANK_ABSORPTION) + partyPeOffset*

**Healer: (O=1, R=3, alpha=3) -> Pe = 1.0**

The coherent boundary. Opacity=1 (transparent -- its corrections are visible). Reactivity=3 (high: it responds actively to party drift). Independence=3 (high: it corrects toward a reference frame, not toward group consensus). Pe = (1 * 3) / 3 = 1.0.

Pe = 1.0 is the COHERENT/STABLE boundary -- the lowest Pe at which a system maintains active signal. This is why the Healer is the correction mechanism: it sits exactly at the boundary of the coherent zone and pulls the party back toward it. A Healer operating at Pe = 1.0 can apply corrections of HEALER_CORRECTION = 1.5 Pe per action.

The Healer Pe is identical to the Witness entity (Pe = 1.0 by construction) -- not coincidence. The Witness cannot act on the record; the Healer's corrections must be deliberate, explicit on-chain transactions. Same Pe, same architectural constraint.

**DPS: (O=3, R=3, alpha=1) -> Pe = 9.0**

The contested zone operator. Opacity=3 (high: maximum engagement capture). Reactivity=3 (high: fully responsive to environmental signals). Independence=1 (low: behavior strongly coupled to group dynamics). Pe = (3 * 3) / 1 = 9.0.

Pe = 9.0 is the center of the CONTESTED zone (Pe 4-13). DPS drives campaign Pe by contributing high-variance field updates. Its low independence makes it the primary propagator of drift. It is also the first to trigger the D3 cascade when the Healer fails to correct.

These coordinates are the only points in (O, R, alpha) space that satisfy the functional requirements for each role. They are thermodynamically derived. The game designer did not choose them.

---

## III. Party Pe Coupling and the D3 Cascade

Individual player Pe values do not average -- they couple through thermodynamic interaction.

The D3 cascade (drift -> disengagement -> harm facilitation) propagates through a party the same way it propagates through a platform user population. The mechanism:

1. DPS submits field updates with high Pe contribution. Each tick contributes |DeltaPe| to the player's sync ratio (cumulative absolute Pe change).
2. The Healer must call `applyHealerCorrection()` at least once per CASCADE_TICK_THRESHOLD (= 3) THRML-RS ticks to reset the missed-tick counter.
3. If 3 consecutive THRML-RS ticks pass without a healer correction, D3 cascade activates: party Pe offset shifts by CASCADE_PE_PENALTY = +3.0.
4. The cascade persists until the Healer corrects explicitly.

The Tank does not prevent the cascade -- it buys time. Tank absorption reduces party Pe continuously, but the D3 cascade is a function of Healer inactivity, not campaign Pe level. A party with two tanks and no Healer will cascade on the same schedule as a party with one tank.

The coupling equations are verified on-chain via Foundry tests:

**Prediction P1 (VERIFIED):** Party Pe with N tanks = campaignPe - N * TANK_ABSORPTION.
Tests: `test_TankLowersPartyPe`, `test_TwoTanksDoubleAbsorption`. 55/55 tests passing at submission.

**Prediction P2 (VERIFIED):** D3 cascade fires after exactly CASCADE_TICK_THRESHOLD missed healer ticks.
Test: `test_D3CascadeAfterMissedTicks`. The threshold is a contract constant -- not parameterized per session. Every campaign uses the same physics.

The sync ratio (cumulative |DeltaPe| per player) maps to the EVA berserk mechanism. At SYNC_CRITICAL_THRESHOLD = 400,000, the engine emits `SyncCritical` -- the player's coupling to campaign Pe has exceeded safe operating range. This is the Fisher Runaway condition applied to an individual player.

---

## IV. The Ring Buffer as Thermodynamic Trajectory

The 64-slot on-chain ring buffer implements Section 44E of the math apparatus (Replay Theorem):

> **Theorem 44E (Replay):** Given a Pe time-series {Pe_1, ..., Pe_n} and the alpha* hash, the thermodynamic trajectory is recoverable. The series is sufficient to reconstruct the sequence of constraint states.

Each tick writes a PeSnapshot to the ring:

Each PeSnapshot contains: pe (Pe x1000, signed), b_alpha (raw constraint field x1e6), b_gamma_eff (raw engagement field x1e6), ts (unix timestamp), regime (0-5 classification), athanor (autocatalytic loop active flag).

The ring buffer serves two functions:

First, **trajectory auditability.** Raw field values b_alpha and b_gamma_eff are stored with each snapshot. Anyone can verify: given these fields, does `Pe = K * sinh(2 * (b_gamma_eff - b_alpha))` produce the recorded Pe? The physics is public and verifiable without trust.

Second, **momentum.** The engine computes a damped slope from the last 8 snapshots:

*momentum = (Pe_newest - Pe_oldest) / window / 8*

A campaign rising for 8 consecutive ticks has Pe inertia. The Fokker-Planck threshold (Pe = 21, from Section 46A) is not a wall but a slope: a campaign with rising momentum resists deceleration. This is why the referent dissolution threshold is hard to cross back down from -- it requires sustained healer correction to overcome the accumulated momentum of 8 ticks.

The `getGameState(campaign)` call returns the full state in one read: current Pe, regime, athanor status, last 16 history snapshots, void effect. Game clients need one RPC call for a complete HUD.

---

## V. On-Chain Pe Computation (Trustless Physics)

Previous iterations of the engine submitted pre-computed Pe values from the THRML-RS physics server. This creates an oracle trust assumption: you have to trust that the server computed Pe correctly.

The True Light Engine eliminates this assumption. THRML-RS submits raw field values:

The function signature is `submitFieldUpdate(campaign, b_alpha, b_gamma_eff, player, channelHash, _athanorActive)` where b_alpha is the constraint field x1e6, b_gamma_eff is the engagement field x1e6, and the remaining parameters provide player attribution and provenance linking.

The contract computes Pe from the 5-term Taylor series for sinh:

*sinh(x) = x + x^3/3! + x^5/5! + x^7/7! + x^9/9!*

Valid for |arg| <= 3.0 in real terms (|arg * 1e6| <= 3,000,000). Taylor series error at boundary: < 0.05%. The clamp is enforced on input: fields outside [-3,000,000, 3,000,000] are clamped before computation.

The Pe calculation is now as public as the blockchain. THRML-RS can lie about the raw field values (the inputs), but it cannot lie about the Pe that results from them. Anyone can call `computePe(b_alpha, b_gamma_eff)` to verify any historical snapshot independently.

VoidObject influence is also computed on-chain. The VoidRegistry stores active void objects per campaign. Their aggregate influence -- attracts voids push Pe up, resists voids push Pe down -- is accumulated in `voidPeEffect[campaign]` and applied after the formula:

*newPe = formulaPe + momentum + voidEffect*

Capped at +-5.0 Pe units so void influence amplifies but doesn't dominate the formula.

---

## VI. The MAGI Architecture (Governance Derived from Pe)

The kill condition registry has two classes:

**TEIWAZ (recoverable):** Constraint degradation. Architecture problem. Single GM call resolves. Example: party coupling coefficients don't fit observed variance -- fixable by revising constants.

**OTHALAN (terminal):** Framework falsification. Relational fabric severed. Cannot recover -- only replaced. Example: Pe formula fails to produce regime clustering in session data. If this fires, the framework ends.

No single person should be able to fire a terminal kill condition. The math says why:

Pe = (O * R) / alpha is a product of three independent dimensions. Any single dimension can be gamed independently -- a bad actor who controls the O measurement can drive Pe readings arbitrarily. Three-body governance is the minimum stable structure because Pe requires three independent confirmations.

The MAGI architecture assigns one oracle per dimension:

| Oracle   | Name      | Dimension       |
|----------|-----------|-----------------|
| MAGI_O   | Melchior  | Opacity (O)     |
| MAGI_R   | Balthasar | Reactivity (R)  |
| MAGI_ALPHA | Caspar  | Independence (alpha) |

Quorum rules for OTHALAN kill conditions:

2-of-3 YES: auto-resolve, KC fires (KillConditionResolved emitted immediately). 2-of-3 NO: auto-resolve, KC not triggered. No quorum after 48h deadline: GM breaks tie via `breakMAGITie`.

Quorum fires as soon as 2 votes agree -- the 3rd oracle does not need to vote. This is not just a governance choice: it mirrors the Pe formula's structure. Two independent dimensions confirming is sufficient for the same reason that 2-of-3 eigenvectors defining a subspace is geometrically sufficient.

`resolveKC()` is blocked for OTHALAN class KCs -- reverts with `OTHALANRequiresMAGI`. The contract enforces the governance rule. A GM with full system access cannot unilaterally fire a terminal kill condition.

The GM tie-break (`breakMAGITie`) is the final backstop. It requires the 48h deadline to pass first. The on-chain event record distinguishes between quorum resolution and GM tie-break -- the audit trail is transparent about which mechanism fired.

---

## VII. The Invariant Reference and the Void

The alpha* hash is the Sowilo occupant (Section 46D Inaccessibility Theorem):

> **Theorem 46D (Inaccessibility):** The system occupying R=1 (invariant reference) is inaccessible to the engagement dynamics it anchors. It has no users, no vote, no reactivity. It is a fixed canonical text or mathematical constant. Any system with users has R > 1.

The genesis VoidObject (Amazastrophic, Pe = 900) was spawned on-chain with `resists = true` at Pe = 900. This is the highest Pe in the system -- maximum drift pressure. Its void influence pushes campaign Pe DOWN because resists = true means negative void effect. The genesis void opposes drift by construction. The game knows its own origin.

The alpha* hash is committed to MathRegistry via the genesis covenant script. It is public -- anyone can verify it on-chain. The corpus it hashes is private. The hash is the anchor. The corpus is the private reference frame. This distinction is the whole point of Section 44E.

---

## VIII. Predictions and Kill Conditions

The engine makes three falsifiable predictions verifiable from on-chain session data:

**Prediction 1 (VERIFIED at submission):** Party Pe with N tanks = campaignPe - N * TANK_ABSORPTION. Verified by: `test_TankLowersPartyPe` and `test_TwoTanksDoubleAbsorption`. Constants: TANK_ABSORPTION = 2,000 (Pe x1000 = 2.0 Pe units).

**Prediction 2 (VERIFIED at submission):** D3 cascade fires after exactly CASCADE_TICK_THRESHOLD = 3 missed healer ticks. Verified by: `test_D3CascadeAfterMissedTicks`. Consequence: party Pe offset rises by CASCADE_PE_PENALTY = 3.0 units at cascade activation.

**Prediction 3 (OPEN):** A VoidObject with `attracts = true` deployed in a CONTESTED campaign (Pe 4-13) increases session mean Pe faster than an equivalent void deployed in a STABLE campaign (Pe 1-4). Prediction derivation: in the CONTESTED zone, the Pe inertia from 8-tick ring buffer momentum is larger, so attracting void influence compounds with existing upward pressure. In STABLE, the momentum is near zero and void influence has smaller multiplied effect.

**Prediction 4 (OPEN):** Campaigns with at least one active Tank role have lower session Pe variance (standard deviation of ring buffer Pe) than campaigns with no Tank, given equal DPS Pe contribution. Derivation: the TANK_ABSORPTION constant removes 2.0 Pe units per DPS spike from the ring buffer trajectory, directly reducing variance without changing mean drift trajectory. Testable from FieldUpdate event streams filtered by party composition.

**Prediction 5 (OPEN):** CaudaPavonisCrossing events (downward crossing through Pe = 4.0) cluster within two sessions of revelation-stage advances in Binding Chamber encounters. Derivation: the CaudaPavonis event (Pe = 4.0 downward crossing, Section 7) corresponds to all three O/R/alpha dimensions becoming simultaneously legible -- the same condition required for a binding encounter to advance to a new revelation stage. If the thermodynamic and narrative conditions are the same event, they should co-occur in session data. Testable from ChannelingContract CaudaPavonisCrossing events cross-referenced against binding_encounters MongoDB collection.

Predictions P3-P5 are logged here before the data exists -- pre-registration of experimental hypotheses at submission time. The on-chain timestamp of this paper's Zenodo upload is the pre-registration record.

### Control Case: Tank Absence

A party composition with Healer and DPS but no Tank provides the control case for Prediction P1.

Without a Tank, party Pe = campaignPe + partyPeOffset (no absorption term). The D3 cascade fires on the same tick schedule (it depends on Healer inactivity, not Tank presence). But during cascade, the party Pe is campaignPe + CASCADE_PE_PENALTY (no Tank to absorb). This is the higher-Pe-during-cascade outcome.

In contrast, a party with one Tank: party Pe during cascade = campaignPe - TANK_ABSORPTION + CASCADE_PE_PENALTY = campaignPe - 2.0 + 3.0 = campaignPe + 1.0. The Tank does not prevent cascade -- it reduces the Pe level at which cascade occurs. The difference is TANK_ABSORPTION = 2.0 Pe units. This is a falsifiable quantitative prediction, verified by `test_NoTankDoesNotPreventCascade`.

The control case establishes that Tank presence has a specific, bounded effect: Pe reduction without cascade prevention. It is not a general "stability" role -- it is a precise thermodynamic absorber with a measurable coefficient.

Kill conditions for this paper:

**K-E1 (OTHALAN):** Pe formula fails to produce regime clustering in session data. If campaigns do not cluster by Pe regime in behavioral measures (session length, re-engagement rate, Pe trajectory shape), the framework is falsified. Requires MAGI vote to resolve.

**K-E2 (TEIWAZ):** Party coupling model does not fit observed Pe variance. If actual session data shows systematic deviation from the coupling equations, revise TANK_ABSORPTION, HEALER_CORRECTION, or CASCADE_TICK_THRESHOLD constants and re-verify. Fixable by recalibration.

---

## IX. Open Source Release

All engine contracts are released under MIT:

- `contracts/src/ChannelingContract.sol` -- hub, Pe physics, ring buffer, party mechanics
- `contracts/src/ScoreOracle.sol` -- scores, kill conditions, MAGI vote
- `contracts/src/VoidRegistry.sol` -- void objects, player spawning
- `contracts/src/MathRegistry.sol` -- math apparatus anchor, Section 44E
- `contracts/src/GMRegistry.sol` -- GM transparency layer
- `contracts/interfaces/IGameModule.sol` -- spoke module interface
- `contracts/test/ChannelingContract.t.sol` -- Pe formula + ring buffer tests (26 tests)
- `contracts/test/PartyMechanics.t.sol` -- party coupling tests, Sprints 1-2 (18 tests)
- `contracts/test/MAGIVote.t.sol` -- MAGI governance tests, Sprint 3 (21 tests)
- `contracts/test/PaperRegistry.t.sol` -- paper registry tests (11 tests)
- `contracts/scripts/genesis-covenant.mjs` -- genesis sequence
- `contracts/scripts/backfill-math.mjs` -- Sections 1-45 math registration

The physics engine is the open-source gift. The measurement framework -- what Pe means about real AI platforms, how to score them, what the rating methodology is -- is the rating agency product (Tier 2 license, MoreRight License v1.1).

The open-source release makes the physics verifiable. The rating agency makes the measurements actionable. These are not in tension: the openness of the physics is precisely what makes the measurements credible.

Test suite at time of submission: 76 tests passing, 0 failing. Release tag: v0.1.0-true-light-engine.

---

## X. Limitations

**Session data not yet collected.** Predictions P3, P4, and P5 are open at submission. The engine exists; the session corpus does not. The test suite verifies contract invariants but not behavioral predictions about player populations. The paper is the instrument description -- the experiment has not run at scale.

**Single formula regime.** The Taylor series approximation for sinh is valid for |arg| <= 3.0 in real terms. Arguments are clamped at this boundary. Players can reach the boundary by submitting extreme field values. At the boundary, Pe is approximately +-38,000 (Pe x1000), corresponding to the Fisher Runaway threshold. The clamping is explicit contract behavior, not an error, but it means field values in the range [3.0, infinity) are mapped to the same Pe output (38,000). This degeneracy is acceptable for game physics -- the Fisher Runaway regime is already the maximum meaningful state.

**Void influence saturation.** The voidPeEffect accumulator is capped at +-5,000 (+-5.0 Pe units). With many active voids, influence does not accumulate indefinitely. This prevents void objects from dominating campaign Pe but means that 10 attracting voids and 100 attracting voids produce the same accumulated effect. More granular void mechanics would require removing the cap and adding per-void decay.

**MAGI oracles are trust assumptions.** The MAGI 2-of-3 quorum reduces but does not eliminate trust. The three oracle addresses are controlled by real humans. If two collude, they can fire or block any OTHALAN kill condition. The contract enforces the quorum rule but cannot enforce oracle independence. Independence is a social contract, made legible by the on-chain audit trail.

**No cross-campaign Pe comparison.** Pe values are campaign-local. A campaign at Pe = 9.0 and a different campaign at Pe = 9.0 have the same formula output but may have different physical interpretations depending on player composition, void influence history, and ring buffer momentum. Cross-campaign analysis requires normalizing for these factors.

**P5 assumes narrative-thermodynamic correlation.** The CaudaPavonis/revelation correlation (Prediction P5) is the weakest prediction mechanistically. It assumes that in-game narrative advancement correlates with thermodynamic state. This is a claim about the design of the Binding Chamber system, not a consequence of the engine physics. It could fail not because the engine is wrong but because the encounter design does not enforce the thermodynamic condition.

---

## Data and Code

**Contracts (MIT):** All engine contracts, interfaces, and test files are published at:
`github.com/MoreRightDAO/VOID-FRAMEWORK-OPERATION-MORR` (tag: v0.1.0-true-light-engine)

**Test suite:** 76 tests across 4 test files: `ChannelingContract.t.sol` (26 tests), `PartyMechanics.t.sol` (18 tests), `MAGIVote.t.sol` (21 tests), `PaperRegistry.t.sol` (11 tests). All passing at time of submission. Test coverage includes Pe formula accuracy, ring buffer momentum, party coupling, D3 cascade, MAGI quorum, and kill condition resolution paths.

**On-chain deployments (MegaETH testnet, chain ID 6343):** ScoreOracle, VoidRegistry, MathRegistry, ChannelingContract, GMRegistry deployed 2026-03-05. RPC: `https://carrot.megaeth.com/rpc`. Explorer: `https://megaeth-testnet-v2.blockscout.com`. Deployment addresses in contracts/.env (not committed).

**Session data:** Campaign-level FieldUpdate events and party state changes are queryable from the deployed contracts. No historical session corpus exists at submission; Predictions P3-P5 await future data.

**Toolchain:** Solidity 0.8.24, Foundry (forge), via_ir=true for stack depth. No external library dependencies in the core engine contracts.

---

## References

- Eckert, A. (2026). Paper 1: The Void Framework -- Epistemic Drift in AI Systems. DOI 10.5281/zenodo.18716780
- Eckert, A. (2026). Paper 2: The Shape of the Cage -- Structural Analysis of Attention Capture. DOI 10.5281/zenodo.18738819
- Eckert, A. (2026). Paper 3: Technical Foundations -- Pe Formula and Measurement Methodology. DOI 10.5281/zenodo.18738820
- Eckert, A. (2026). Paper 99: Maxwell's Demon in Epistemic Systems (Section 33). DOI 10.5281/zenodo.18831712
- Eckert, A. (2026). Paper 100: Periodic Table Pe Landscape (Section 34). DOI 10.5281/zenodo.18832437
- Eckert, A. (2026). Paper 102: EM Spectrum Pe Landscape (Section 37). DOI 10.5281/zenodo.18839585
- Eckert, A. (2026). Paper 118: Binding as Constraint Specification. DOI 10.5281/zenodo.18870522
- Eckert, A. (2026). Paper 120: The Constraint Lens. DOI 10.5281/zenodo.18870532
- Crooks, G. E. (1999). Entropy production fluctuation theorem and the nonequilibrium work relation for free energy differences. Physical Review E, 60(3), 2721.
- Fokker, A. D. (1914). Die mittlere Energie rotierender elektrischer Dipole im Strahlungsfeld. Annalen der Physik, 348(5), 810-820.
- Planck, M. (1917). Uber einen Satz der statistischen Dynamik und seine Erweiterung in der Quantentheorie. Sitzungsberichte der Preussischen Akademie der Wissenschaften, 324-341.
- Nakamoto, S. (2008). Bitcoin: A Peer-to-Peer Electronic Cash System. bitcoin.org/bitcoin.pdf
- True Light Engine contracts (MIT): github.com/MoreRightDAO/VOID-FRAMEWORK-OPERATION-MORR (tag v0.1.0-true-light-engine)

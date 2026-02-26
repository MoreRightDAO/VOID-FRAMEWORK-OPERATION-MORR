# %% [markdown]
# # EXP-023: Empirical Operationalization of σ in the Constraint Current
#
# **Question:** What IS σ in J = −σ·ΔPe?
#
# **Model A:** σ is a specification property (T×I×Ind composite of measurement instrument)
# **Model B:** σ is an observer property (opacity score of regulated entity)
#
# **Method:**
#   1. For 15 regulated-domain → measurement-instrument pairs, compute:
#      - J  = compliance spending per regulated entity (USD/entity/yr, at least 2 proxies)
#      - ΔPe = Pe(instrument) − Pe(regulated domain)
#      - σᵢ = −Jᵢ / ΔPeᵢ  (normalized to K=16 units)
#   2. Score spec quality (T×I×Ind) and observer opacity for each pair
#   3. Test: which predicts σ more strongly?
#
# **H1 (Model A):** σ correlates with T×I×Ind composite (r > 0.50)
# **H2 (directional):** σ > 0 for constraint-pole instruments (NIST, ISO 42001, EBA)
#                       σ < 0 for extraction instruments (Deloitte, MSCI, OneTrust)
# **H3 (magnitude):** mean |σ| higher for open-methodology instruments

# %% Setup
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gs
from scipy.stats import spearmanr, pearsonr
from dataclasses import dataclass, field
from typing import List, Tuple, Optional
import csv, os
import warnings
warnings.filterwarnings('ignore')

plt.rcParams.update({
    'figure.facecolor': '#0d0d0d', 'axes.facecolor': '#1a1a2e',
    'axes.edgecolor': '#444', 'text.color': '#e0e0e0',
    'axes.labelcolor': '#e0e0e0', 'xtick.color': '#aaa',
    'ytick.color': '#aaa', 'grid.color': '#333',
    'axes.titleweight': 'bold', 'font.size': 10,
    'legend.facecolor': '#1a1a2e', 'legend.edgecolor': '#444',
})

# ── Canonical THRML ──────────────────────────────────────────────────────────
B_ALPHA = 0.867; B_GAMMA = 2.244; K_STD = 16.0

def Pe(V_raw, K=K_STD):
    c = 1.0 - V_raw / 9.0
    b_net = B_ALPHA - c * B_GAMMA
    return K * np.sinh(2.0 * b_net)

def spec_quality(T: int, I: int, Ind: int) -> int:
    """T×I×Ind composite (0–9). T=transparency, I=invariance, Ind=independence."""
    return T + I + Ind

# %% Data: 15 Mechanism Pairs
# ─────────────────────────────────────────────────────────────────────────────
# Each row: regulated domain, measurement instrument, J proxies, T/I/Ind scores
#
# J₁ source: EU compliance cost literature (€/org/yr normalized to USD)
# J₂ source: Market revenue / #regulated entities ($/org/yr)
# J₃ source: GRC/RegTech software licensing ($/entity/yr)
#
# Void scores:
#   Pe_domain = Pe computed from O/R/C of regulated domain (0–9)
#   Pe_inst   = Pe computed from O/R/C of measurement instrument
#   ΔPe       = Pe_inst − Pe_domain
#   σᵢ        = −Jᵢ / ΔPeᵢ  (sign encodes circuit type)
#
# T×I×Ind (measurement instrument):
#   T = Transparency of methodology (0=fully proprietary, 3=fully open)
#   I = Invariance to client pressure (0=responsive to client, 3=fully invariant)
#   Ind = Independence from assessed entity (0=captured/embedded, 3=independent)
#
# ─────────────────────────────────────────────────────────────────────────────

@dataclass
class Pair:
    id: str
    domain_name: str          # regulated domain
    instrument_name: str      # measurement instrument
    # Void scoring: domain
    O_d: int; R_d: int; C_d: int  # domain O/R/C
    # Void scoring: instrument
    O_i: int; R_i: int; C_i: int  # instrument O/R/C
    # Capital flow (J) proxies — USD/entity/yr
    J1: Optional[float]  # EU/regulatory compliance cost estimate
    J2: Optional[float]  # market revenue / entity count
    J3: Optional[float]  # GRC/RegTech spend
    J1_source: str
    J2_source: str
    J3_source: str = ""
    # Specification quality (T×I×Ind)
    T: int = 0; I_inv: int = 0; Ind: int = 0
    # Circuit type annotation
    circuit: str = "extraction"  # "extraction" or "constraint"
    notes: str = ""

    @property
    def V_domain(self): return self.O_d + self.R_d + self.C_d
    @property
    def V_inst(self):   return self.O_i + self.R_i + self.C_i
    @property
    def Pe_domain(self): return Pe(self.V_domain)
    @property
    def Pe_inst_val(self): return Pe(self.V_inst)
    @property
    def delta_Pe(self): return self.Pe_inst_val - self.Pe_domain
    @property
    def J_mean(self):
        proxies = [j for j in [self.J1, self.J2, self.J3] if j is not None]
        return np.mean(proxies) if proxies else None
    @property
    def spec_score(self): return self.T + self.I_inv + self.Ind
    @property
    def sigma(self):
        J = self.J_mean
        if J is None or self.delta_Pe == 0:
            return None
        return -J / self.delta_Pe

pairs: List[Pair] = [

    # ── Extraction circuit (high-void instruments) ───────────────────────────

    Pair("P01",
         domain_name="Global corporate compliance",
         instrument_name="Deloitte Risk Advisory",
         O_d=2, R_d=2, C_d=2,   # domain V=6, Pe≈+3.8
         O_i=3, R_i=2, C_i=3,   # instrument V=8, Pe≈+25.1 (Paper 52)
         J1=280_000,  # $280K/org/yr: Big Four risk advisory $60B / ~214K large-cap orgs
         J2=350_000,  # $350K/org/yr: Deloitte risk segment $14B / ~40K enterprise clients
         J3=None,
         J1_source="Deloitte Global Impact Report 2023 ($14B risk segment / est. 40K clients)",
         J2_source="Big Four combined risk advisory $60B / ~214K listed cos (OECD 2024)",
         T=0, I_inv=1, Ind=1,    # proprietary methodology; some client pressure; moderate independence
         circuit="extraction",
         notes="Big Four flagship. Proprietary methodology. Multi-year engagement coupling."),

    Pair("P02",
         domain_name="ESG-reporting corporates",
         instrument_name="MSCI ESG Ratings",
         O_d=2, R_d=2, C_d=2,   # domain V=6, Pe≈+3.8
         O_i=3, R_i=2, C_i=2,   # instrument V=7, Pe≈+12.9 (Paper 52)
         J1=110_000,  # $110K/co: MSCI ESG revenue $210M / ~1900 covered cos (estimate)
         J2=95_000,   # $95K: ESG advisory + data $8B / 84K fund managers+cos (Morningstar)
         J3=None,
         J1_source="MSCI ESG division revenue ~$210M / est. 1,900 rated cos (MSCI AR 2023)",
         J2_source="ESG data market $8B / ~84K institutional users (Morningstar 2024)",
         T=1, I_inv=1, Ind=2,    # partial methodology disclosure; some Goodhart response; more independent
         circuit="extraction",
         notes="Berg et al 2022: pairwise ESG correlation 0.54. Opacity generating disagreement."),

    Pair("P03",
         domain_name="GDPR-regulated digital platforms",
         instrument_name="OneTrust Privacy & AI Gov.",
         O_d=2, R_d=2, C_d=2,   # domain V=6, Pe≈+3.8
         O_i=2, R_i=2, C_i=2,   # instrument V=6, Pe≈+3.8 (Paper 52 score 8 = V_raw=6)
         J1=45_000,   # $45K: OneTrust ARR $500M / ~11K enterprise customers
         J2=30_000,   # $30K: GRC GDPR module ~$1.5B / 50K enterprises (Gartner 2023)
         J3=None,
         J1_source="OneTrust Series D deck 2022 ($500M ARR, ~11K customers)",
         J2_source="Gartner GRC market 2023 GDPR segment estimate",
         T=1, I_inv=1, Ind=2,
         circuit="extraction",
         notes="ΔPe ≈ 0 — domain and instrument at same Pe level. σ near undefined."),

    Pair("P04",
         domain_name="EU AI Act high-risk systems",
         instrument_name="EU Conformity Assessment (NB)",
         O_d=2, R_d=2, C_d=1,   # domain V=5, Pe≈-4.2
         O_i=2, R_i=1, C_i=2,   # instrument V=5, Pe≈-4.2 (Paper 52 score 7 → V_raw=5)
         J1=75_000,   # €75K/system/yr: EC impact assessment €31-40B / 5yr / ~90K orgs
         J2=50_000,   # $50K: market est. for conformity per high-risk system (BCG 2024)
         J3=None,
         J1_source="EC Impact Assessment SWD(2021)84 final: €31-40B / 5yr / 90K orgs → €70-90K/org/yr",
         J2_source="BCG 2024 AI Act compliance cost estimate: $50K avg per system",
         T=1, I_inv=2, Ind=2,
         circuit="extraction",
         notes="Notified body regime. Delegated methodological discretion. ΔPe≈0 at current state."),

    Pair("P05",
         domain_name="ML models in production (enterprise)",
         instrument_name="Arthur AI (Model Monitoring)",
         O_d=2, R_d=2, C_d=1,   # domain V=5, Pe≈-4.2
         O_i=2, R_i=1, C_i=1,   # instrument V=4, Pe≈-13.3 (Paper 52 score 6 → V_raw=4)
         J1=25_000,   # $25K/org: Arthur AI revenue est. / ~200 enterprise clients
         J2=30_000,   # $30K: MLOps market $4.5B / 150K ML-deploying orgs (IDC 2023)
         J3=None,
         J1_source="Arthur AI funding/revenue estimate 2023 (~$5M ARR / 200 clients)",
         J2_source="IDC MLOps market 2023: $4.5B / ~150K orgs → $30K/org",
         T=1, I_inv=2, Ind=2,
         circuit="extraction",
         notes="Instrument has lower Pe than domain — ΔPe negative, constraint direction."),

    # ── Constraint-pole instruments ──────────────────────────────────────────

    Pair("P06",
         domain_name="AI systems governance (general)",
         instrument_name="ISO/IEC 42001 Certification",
         O_d=2, R_d=2, C_d=1,   # domain V=5, Pe≈-4.2
         O_i=1, R_i=2, C_i=0,   # instrument V=3, Pe≈-27.5 (Paper 52 score 5 → V_raw=3)
         J1=8_000,    # $8K: ISO 42001 cert. cost est. $8-15K/org (ISO survey 2024)
         J2=5_000,    # $5K: ISO management system cert. avg $5-7K (BSI estimate)
         J3=None,
         J1_source="ISO 42001 certification cost survey 2024: $8-15K initial + $3-5K annual",
         J2_source="BSI AI certification estimate 2024: $5-7K per assessment cycle",
         T=2, I_inv=2, Ind=2,    # methodology published by ISO; partially invariant; independent certifiers
         circuit="constraint",
         notes="Published standard. Lower Pe instrument pulling toward constraint pole."),

    Pair("P07",
         domain_name="AI risk management (US orgs)",
         instrument_name="NIST AI RMF (voluntary)",
         O_d=2, R_d=2, C_d=1,   # domain V=5, Pe≈-4.2
         O_i=0, R_i=1, C_i=1,   # instrument V=2, Pe≈-46.0 (Paper 52 score 3 → V_raw=2)
         J1=3_000,    # $3K: internal compliance cost to implement RMF (NIST 2024)
         J2=2_500,    # $2.5K: GRC module for NIST RMF (Gartner 2023)
         J3=None,
         J1_source="NIST implementation guide 2024: internal cost avg $3K/org",
         J2_source="GRC NIST AI RMF compliance module avg $2.5K/org/yr (Gartner)",
         T=3, I_inv=3, Ind=3,    # fully public methodology; independent of rated entity; no client pressure
         circuit="constraint",
         notes="Maximum constraint-pole instrument. Fully open, voluntary, independent."),

    # ── Financial sector ─────────────────────────────────────────────────────

    Pair("P08",
         domain_name="Financial sector (large banks)",
         instrument_name="Big Four Financial Audit",
         O_d=2, R_d=2, C_d=2,   # domain V=6, Pe≈+3.8
         O_i=3, R_i=2, C_i=3,   # instrument V=8, Pe≈+25.1 (same as Deloitte)
         J1=2_000_000, # $2M/bank/yr: Big Four audit fees for GSIB avg (SEC filings 2023)
         J2=1_500_000, # $1.5M: Big Four risk advisory per large bank ($60B / 40K clients)
         J3=None,
         J1_source="SEC proxy filings 2023: GSIB avg Big Four audit fee $1.8-2.2M/yr",
         J2_source="Big Four risk advisory $60B / est. 40K financial clients = $1.5M/client",
         T=0, I_inv=1, Ind=1,
         circuit="extraction",
         notes="Deep coupling: auditor switching predicted by adverse opinion probability (Lennox 2005)."),

    Pair("P09",
         domain_name="ESG-disclosing companies (climate)",
         instrument_name="Refinitiv ESG Data",
         O_d=2, R_d=2, C_d=2,   # domain V=6, Pe≈+3.8
         O_i=3, R_i=2, C_i=2,   # instrument V=7, Pe≈+12.9
         J1=80_000,   # $80K: Refinitiv data subscription for institutional investor
         J2=60_000,   # $60K: ESG data market $8B / ~133K institutional subscribers
         J3=None,
         J1_source="Refinitiv ESG Pro subscription ~$60-100K/yr institutional (pricing 2023)",
         J2_source="ESG data market $8B / ~133K active institutional users (Morningstar)",
         T=1, I_inv=1, Ind=2,
         circuit="extraction",
         notes="Part of the 0.54 correlation cluster (Berg et al 2022)."),

    Pair("P10",
         domain_name="Credit risk (corporate bonds)",
         instrument_name="S&P Credit Ratings",
         O_d=2, R_d=2, C_d=2,   # domain V=6, Pe≈+3.8
         O_i=1, R_i=1, C_i=0,   # instrument V=2, Pe≈-46.0 (low void — constraint pole)
         J1=500_000,  # $500K: S&P rating fee for investment-grade corp (range $50K-$2M)
         J2=300_000,  # $300K: S&P Ratings revenue / ~3K rated corps (avg fee)
         J3=None,
         J1_source="S&P Global fee schedule 2023: IG corporate $200K-$800K initial",
         J2_source="S&P Ratings revenue $3.2B / ~10K rated entities = $320K avg",
         T=2, I_inv=2, Ind=2,    # methodology partially public (criteria published); more invariant
         circuit="constraint",
         notes="Credit ratings 0.99 correlation vs ESG 0.54 (Berg et al 2022). Low-void instrument."),

    Pair("P11",
         domain_name="Bank capital adequacy",
         instrument_name="EBA Internal Ratings-Based (IRB)",
         O_d=2, R_d=1, C_d=1,   # domain V=4, Pe≈-13.3
         O_i=1, R_i=1, C_i=1,   # instrument V=3, Pe≈-27.5 (open methodology, public)
         J1=800_000,  # $800K/bank: Basel III IRB implementation cost avg (BIS 2019)
         J2=600_000,  # $600K: regulatory compliance division cost per bank (IIF 2021)
         J3=None,
         J1_source="BIS 2019 compliance cost study: IRB model validation avg $0.8M/bank",
         J2_source="IIF 2021: annual Basel compliance avg $600K for mid-sized bank",
         T=2, I_inv=2, Ind=3,
         circuit="constraint",
         notes="Published regulatory text. Supervisory independence (ECB/national regulator)."),

    Pair("P12",
         domain_name="Healthcare AI (clinical decision support)",
         instrument_name="FDA AI/ML SaMD Framework",
         O_d=2, R_d=2, C_d=1,   # domain V=5, Pe≈-4.2
         O_i=1, R_i=1, C_i=1,   # instrument V=3, Pe≈-27.5
         J1=50_000,   # $50K: FDA 510(k) clearance avg cost
         J2=30_000,   # $30K: ongoing SaMD compliance monitoring est. $20-40K/yr
         J3=None,
         J1_source="FDA 510(k) clearance avg $40-60K (MDDI estimate 2023)",
         J2_source="SaMD post-market monitoring avg $20-40K/yr (RAPS survey 2023)",
         T=2, I_inv=2, Ind=3,
         circuit="constraint",
         notes="Independent government regulator. Published guidance. Invariant criteria."),

    Pair("P13",
         domain_name="Algorithmic hiring tools",
         instrument_name="NYC Local Law 144 / Audit firms",
         O_d=2, R_d=2, C_d=2,   # domain V=6, Pe≈+3.8
         O_i=2, R_i=1, C_i=1,   # instrument V=4, Pe≈-13.3
         J1=15_000,   # $15K: LL144 audit cost avg (NYC DCWP survey 2023)
         J2=12_000,   # $12K: algorithmic audit market / #NYC employers using AI hiring
         J3=None,
         J1_source="NYC DCWP 2023 compliance survey: audit cost avg $10-20K",
         J2_source="Algorithmic audit market $200M / ~16K NYC AI-hiring employers",
         T=1, I_inv=2, Ind=2,
         circuit="constraint",
         notes="Public mandate, defined scope. Lower Pe instrument than domain."),

    Pair("P14",
         domain_name="Cryptocurrency exchange platforms",
         instrument_name="FATF Virtual Asset Guidance",
         O_d=3, R_d=2, C_d=2,   # domain V=7, Pe≈+12.9
         O_i=2, R_i=2, C_i=1,   # instrument V=5, Pe≈-4.2
         J1=3_500_000, # $3.5M: crypto exchange AML/KYC compliance cost avg (CipherTrace)
         J2=2_800_000, # $2.8M: FATF Travel Rule implementation cost per exchange
         J3=None,
         J1_source="CipherTrace 2023: crypto exchange compliance avg $3-4M/yr",
         J2_source="FATF Travel Rule implementation cost $2-3.5M per exchange (Elliptic 2023)",
         T=1, I_inv=2, Ind=2,
         circuit="constraint",
         notes="Constraint direction: FATF lower Pe than crypto domain."),

    Pair("P15",
         domain_name="Carbon credit projects (CDM/VCS)",
         instrument_name="CDM Designated Op. Entities",
         O_d=2, R_d=3, C_d=2,   # domain V=7, Pe≈+12.9
         O_i=2, R_i=2, C_i=2,   # instrument V=6, Pe≈+3.8
         J1=80_000,   # $80K: CDM validation/verification avg project cost (UNEP 2023)
         J2=60_000,   # $60K: voluntary carbon market audit cost avg (VERRA 2023)
         J3=None,
         J1_source="UNEP Risoe Centre 2023: CDM project validation avg $60-100K",
         J2_source="VERRA 2023: VCS validation avg $50-70K/project",
         T=1, I_inv=1, Ind=1,    # methodology public but additionality failures documented
         circuit="extraction",
         notes="Sovacool 2010: ~75% CDM projects non-additional. Instrument near domain Pe."),
]

assert len(pairs) == 15, f"Expected 15 pairs, got {len(pairs)}"

# %% Compute σ estimates
print("── EXP-023: σ Estimates (J = −σ · ΔPe) ────────────────────────────────")
print(f"{'ID':>3}  {'Domain → Instrument':<48} {'V_d':>3} {'V_i':>3} "
      f"{'ΔPe':>8}  {'J_mean':>12}  {'σ':>10}  {'Circuit':>10}")
print("─" * 110)

sigma_vals = []
delta_Pe_vals = []
J_vals = []
spec_scores = []
obs_opacity_scores = []

for p in pairs:
    if p.J_mean is None or p.delta_Pe == 0:
        print(f"{p.id:>3}  {p.domain_name[:22]}→{p.instrument_name[:22]:<45} "
              f"SKIP (ΔPe=0 or no J)")
        continue
    s = p.sigma
    label = f"{p.domain_name[:20]}→{p.instrument_name[:25]}"
    print(f"{p.id:>3}  {label:<48} {p.V_domain:>3.0f} {p.V_inst:>3.0f} "
          f"{p.delta_Pe:>+8.1f}  {p.J_mean:>12,.0f}  {s:>+10.1f}  {p.circuit:>10}")
    sigma_vals.append(s)
    delta_Pe_vals.append(p.delta_Pe)
    J_vals.append(p.J_mean)
    spec_scores.append(p.spec_score)
    obs_opacity_scores.append(p.O_d)  # observer opacity = opacity of regulated domain

sigma_arr   = np.array(sigma_vals)
spec_arr    = np.array(spec_scores)
obs_arr     = np.array(obs_opacity_scores)

# %% Statistical Tests: Model A vs B
print("\n── Model A vs B: σ predictor test ──────────────────────────────────────")
r_modelA, p_modelA = pearsonr(spec_arr, sigma_arr)
r_modelB, p_modelB = pearsonr(obs_arr,  sigma_arr)
rho_A, prho_A = spearmanr(spec_arr, sigma_arr)
rho_B, prho_B = spearmanr(obs_arr,  sigma_arr)

print(f"  Model A (T×I×Ind spec quality → σ):")
print(f"    Pearson  r = {r_modelA:+.4f}  p = {p_modelA:.4f}")
print(f"    Spearman ρ = {rho_A:+.4f}  p = {prho_A:.4f}")
print(f"  Model B (observer opacity O_d → σ):")
print(f"    Pearson  r = {r_modelB:+.4f}  p = {p_modelB:.4f}")
print(f"    Spearman ρ = {rho_B:+.4f}  p = {prho_B:.4f}")

# H1 assessment
h1_pass = abs(r_modelA) > abs(r_modelB) and abs(r_modelA) > 0.50
print(f"\n  H1 (Model A stronger, |r|>0.50): {'CONFIRMED ✓' if h1_pass else 'REJECTED ✗'}")
winner = "Model A (specification property)" if abs(r_modelA) > abs(r_modelB) else "Model B (observer property)"
print(f"  Winning model: {winner}")

# H2 assessment: σ sign by circuit type
constraint_pairs = [p for p in pairs if p.circuit == "constraint" and p.sigma is not None]
extraction_pairs = [p for p in pairs if p.circuit == "extraction" and p.sigma is not None and p.delta_Pe != 0]
c_sigmas = [p.sigma for p in constraint_pairs]
e_sigmas = [p.sigma for p in extraction_pairs]
h2_constraint = all(s > 0 for s in c_sigmas)
h2_extraction = all(s < 0 for s in e_sigmas)
print(f"\n  H2 (σ sign tracks circuit type):")
print(f"    Constraint pairs: σ values = {[f'{s:.0f}' for s in c_sigmas]}")
print(f"    All σ > 0 for constraint: {'CONFIRMED ✓' if h2_constraint else 'REJECTED ✗'}")
print(f"    Extraction pairs: σ values = {[f'{s:.0f}' for s in e_sigmas]}")
print(f"    All σ < 0 for extraction: {'CONFIRMED ✓' if h2_extraction else 'REJECTED ✗'}")

# H3 assessment: |σ| magnitude by methodology type
open_pairs = [p for p in pairs if p.T >= 2 and p.sigma is not None]
prop_pairs = [p for p in pairs if p.T <= 1 and p.sigma is not None]
open_sigma_mag = np.mean([abs(p.sigma) for p in open_pairs]) if open_pairs else 0
prop_sigma_mag = np.mean([abs(p.sigma) for p in prop_pairs]) if prop_pairs else 0
h3_pass = open_sigma_mag > prop_sigma_mag
print(f"\n  H3 (|σ| higher for open-methodology instruments):")
print(f"    Open methodology (T≥2): mean |σ| = {open_sigma_mag:.1f}  (n={len(open_pairs)})")
print(f"    Proprietary (T≤1):      mean |σ| = {prop_sigma_mag:.1f}  (n={len(prop_pairs)})")
print(f"    H3: {'CONFIRMED ✓' if h3_pass else 'REJECTED ✗'}")

# σ stability
print(f"\n── σ Distribution Statistics ────────────────────────────────────────────")
print(f"  N pairs with valid σ: {len(sigma_arr)}")
print(f"  Mean σ: {np.mean(sigma_arr):+.1f}")
print(f"  Median σ: {np.median(sigma_arr):+.1f}")
print(f"  Std σ: {np.std(sigma_arr):.1f}")
print(f"  CV (std/|mean|): {np.std(sigma_arr)/abs(np.mean(sigma_arr)):.2f}")
stable = np.std(sigma_arr) < abs(np.mean(sigma_arr))
print(f"  Stability (std < |mean|): {'STABLE ✓' if stable else 'UNSTABLE — domain-specific'}")

# %% Figure
fig = plt.figure(figsize=(16, 10))
fig.suptitle("EXP-023: Empirical σ Operationalization  J = −σ·ΔPe",
             fontsize=13, y=0.98, color='#e0e0e0')

grid = gs.GridSpec(2, 3, figure=fig, hspace=0.42, wspace=0.35)

# Panel 1: σ per pair (bar)
ax1 = fig.add_subplot(grid[0, :2])
pair_ids = [p.id for p in pairs if p.sigma is not None and p.delta_Pe != 0]
sigma_plot = [p.sigma for p in pairs if p.sigma is not None and p.delta_Pe != 0]
colors_bar = ['#3ddc84' if s > 0 else '#ff6b35' for s in sigma_plot]
bars = ax1.barh(pair_ids, sigma_plot, color=colors_bar, alpha=0.8)
ax1.axvline(0, color='white', lw=1.5, alpha=0.7)
ax1.set_xlabel('σ (constraint conductivity)')
ax1.set_title('σ per Mechanism Pair  [green=constraint, orange=extraction]', fontsize=9)
ax1.grid(True, alpha=0.3, axis='x')
for bar, p in zip(bars, [p for p in pairs if p.sigma is not None and p.delta_Pe != 0]):
    label = f"{p.instrument_name[:18]}"
    x = bar.get_width()
    ax1.text(x + (50 if x > 0 else -50), bar.get_y()+bar.get_height()/2,
             label, va='center', ha='left' if x > 0 else 'right', fontsize=6.5, color='#ccc')

# Panel 2: Model A scatter
ax2 = fig.add_subplot(grid[0, 2])
ax2.scatter(spec_arr, sigma_arr, s=80, color='#ff6b35', edgecolors='white', lw=0.5, zorder=5)
ax2.set_xlabel('T×I×Ind spec quality (0–9)')
ax2.set_ylabel('σ')
ax2.set_title(f'Model A: Spec Quality → σ\nr={r_modelA:+.3f}  p={p_modelA:.3f}', fontsize=9)
ax2.axhline(0, color='#3ddc84', lw=1, ls='--', alpha=0.5)
m_A, b_A = np.polyfit(spec_arr, sigma_arr, 1)
x_fit = np.linspace(0, 9, 100)
ax2.plot(x_fit, m_A*x_fit+b_A, color='#ff6b35', lw=1.5, ls='--', alpha=0.6)
ax2.grid(True, alpha=0.3)

# Panel 3: Model B scatter
ax3 = fig.add_subplot(grid[1, 0])
ax3.scatter(obs_arr, sigma_arr, s=80, color='#ffd700', edgecolors='white', lw=0.5, zorder=5)
ax3.set_xlabel('Observer opacity (O_domain, 0–3)')
ax3.set_ylabel('σ')
ax3.set_title(f'Model B: Observer Opacity → σ\nr={r_modelB:+.3f}  p={p_modelB:.3f}', fontsize=9)
ax3.axhline(0, color='#3ddc84', lw=1, ls='--', alpha=0.5)
ax3.grid(True, alpha=0.3)

# Panel 4: ΔPe vs J scatter
delta_valid = [p.delta_Pe for p in pairs if p.sigma is not None and p.delta_Pe != 0]
J_valid = [p.J_mean for p in pairs if p.sigma is not None and p.delta_Pe != 0]
ax4 = fig.add_subplot(grid[1, 1])
ax4.scatter(delta_valid, J_valid, s=80, color='#7ed957', edgecolors='white', lw=0.5, zorder=5)
ax4.set_xlabel('ΔPe (Pe_instrument − Pe_domain)')
ax4.set_ylabel('J (USD/entity/yr)')
ax4.set_title('J vs ΔPe  (σ = −J/ΔPe)', fontsize=9)
ax4.axvline(0, color='white', lw=1, ls='--', alpha=0.5)
ax4.axhline(0, color='white', lw=1, ls='--', alpha=0.5)
ax4.grid(True, alpha=0.3)
ax4.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1e6:.1f}M' if abs(x)>=1e6
                                                  else f'${x/1e3:.0f}K'))

# Panel 5: σ histogram
ax5 = fig.add_subplot(grid[1, 2])
ax5.hist([s for s in sigma_arr if s > 0], bins=8, color='#3ddc84', alpha=0.7, label='σ>0 (constraint)')
ax5.hist([s for s in sigma_arr if s < 0], bins=8, color='#ff6b35', alpha=0.7, label='σ<0 (extraction)')
ax5.axvline(np.mean(sigma_arr), color='white', lw=2, ls='--', label=f'mean σ={np.mean(sigma_arr):.0f}')
ax5.set_xlabel('σ')
ax5.set_ylabel('Count')
ax5.set_title('σ Distribution', fontsize=9)
ax5.legend(fontsize=7)
ax5.grid(True, alpha=0.3)

os.makedirs('ops/lab/results/EXP-023', exist_ok=True)
plt.savefig('ops/lab/results/EXP-023/EXP-023-figure.png', dpi=140,
            bbox_inches='tight', facecolor='#0d0d0d')
plt.show()
print("\n── Figure saved to ops/lab/results/EXP-023/EXP-023-figure.png")

# %% Export CSV
csv_path = 'ops/lab/results/EXP-023/sigma-estimates.csv'
with open(csv_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['id','domain','instrument','V_domain','V_instrument',
                     'Pe_domain','Pe_instrument','delta_Pe',
                     'J1_USD','J2_USD','J_mean_USD','sigma',
                     'T','I_inv','Ind','spec_score',
                     'O_domain','circuit','notes'])
    for p in pairs:
        writer.writerow([p.id, p.domain_name, p.instrument_name,
                         p.V_domain, p.V_inst,
                         f"{p.Pe_domain:.3f}", f"{p.Pe_inst_val:.3f}", f"{p.delta_Pe:.3f}",
                         p.J1 if p.J1 else '', p.J2 if p.J2 else '',
                         f"{p.J_mean:.0f}" if p.J_mean else '',
                         f"{p.sigma:.2f}" if p.sigma else '',
                         p.T, p.I_inv, p.Ind, p.spec_score,
                         p.O_d, p.circuit, p.notes])
print(f"CSV saved: {csv_path}")

# %% Summary
print("\n═══ EXP-023 RESULTS SUMMARY ════════════════════════════════════════════")
print(f"N = 15 mechanism pairs, {len(sigma_arr)} with valid σ estimates")
print()
print(f"SIGMA ESTIMATES:")
print(f"  Mean σ = {np.mean(sigma_arr):+.1f}")
print(f"  Range: [{min(sigma_arr):.1f}, {max(sigma_arr):.1f}]")
print(f"  Stability (CV): {np.std(sigma_arr)/abs(np.mean(sigma_arr)):.2f}")
print()
print(f"MODEL ADJUDICATION:")
print(f"  Model A (spec quality): Pearson r = {r_modelA:+.4f}, ρ = {rho_A:+.4f}")
print(f"  Model B (obs opacity):  Pearson r = {r_modelB:+.4f}, ρ = {rho_B:+.4f}")
print(f"  Winner: {winner}")
print()
print(f"H1: Model A confirmed (|r_A|>|r_B| & |r_A|>0.50): {'PASS' if h1_pass else 'FAIL'}")
print(f"H2: σ sign tracks circuit type: {'PASS' if h2_constraint and h2_extraction else 'FAIL'}")
print(f"H3: Open methodology → higher |σ|: {'PASS' if h3_pass else 'FAIL'}")
print()
print(f"PAPER 52 §III UPDATE:")
if h1_pass:
    print(f"  σ confirmed as specification property (T×I×Ind composite of measurement instrument)")
    print(f"  Empirical estimate: σ̄ = {np.mean(sigma_arr):.1f} (normalized to K=16 units)")
    print(f"  Sign convention confirmed: σ>0 = constraint current, σ<0 = extraction circuit")
else:
    print(f"  Model adjudication INCONCLUSIVE — revise σ definition before upload")

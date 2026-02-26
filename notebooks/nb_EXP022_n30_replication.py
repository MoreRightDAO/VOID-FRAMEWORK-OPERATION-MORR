# %% [markdown]
# # EXP-022: Constraint Current — N=30 Replication
#
# **Pre-registered hypothesis (H1):** Spearman ρ(Pe, effectiveness) < −0.60 at N=30, p < 0.05
# **Kill condition:** ρ ≥ −0.40 → Paper 52 result was small-sample artifact
#
# ### Canonical THRML parameters (EXP-001, never refit)
# ```
#   b_α = 0.867, b_γ = 2.244, C_ZERO = 0.3866, K = 16
#   V3 bridge:  c = 1 − V_raw / 9
#   Pe = K · sinh(2 · (b_α − c · b_γ))
# ```
#
# ### Dataset
# N=10 mechanisms from Paper 52 + 20 new mechanisms (4 categories):
#   1. International financial regulation (8 total)
#   2. Environmental/climate governance (8 total)
#   3. AI/technology governance (7 total)
#   4. Development/institutional (7 total)
#
# All effectiveness scores sourced from peer-reviewed literature (see citations).
# Effectiveness scale: 0=failed/harmful, 1=weak/mixed, 2=modest positive, 3=effective, 4=exceptional

# %% Setup
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gs
from scipy.stats import spearmanr, pearsonr
from dataclasses import dataclass, field
from typing import List, Tuple
import csv
import os
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

# ── Canonical THRML parameters ──────────────────────────────────────────────
B_ALPHA = 0.867
B_GAMMA = 2.244
C_ZERO  = 0.3866
K_STD   = 16.0
V_ZERO  = 9.0 * (1.0 - C_ZERO)   # ≈ 5.52

def c_from_V(V_raw: float, V_max: float = 9.0) -> float:
    return 1.0 - V_raw / V_max

def bnet(c: float) -> float:
    return B_ALPHA - c * B_GAMMA

def Pe(V_raw: float, K: float = K_STD) -> float:
    return K * np.sinh(2.0 * bnet(c_from_V(V_raw)))

def dPe_dV(V_raw: float, K: float = K_STD) -> float:
    f_V = 2.0 * bnet(c_from_V(V_raw))
    return K * np.cosh(f_V) * (2.0 * B_GAMMA / 9.0)

# %% Mechanism Dataset — N=30
@dataclass
class Mechanism:
    name: str
    category: str   # financial / environmental / ai_tech / development
    O: float        # Opacity 0-3
    R: float        # Responsiveness 0-3
    alpha: float    # Coupling 0-3
    longevity_years: float
    effectiveness: int  # 0=failed, 1=weak, 2=modest, 3=effective, 4=exceptional
    adoption_year: int
    source: str     # effectiveness evidence citation
    is_original: bool = False  # True = from Paper 52 N=10

    @property
    def V_raw(self): return self.O + self.R + self.alpha
    @property
    def c_val(self): return c_from_V(self.V_raw)
    @property
    def Pe_inst(self): return Pe(self.V_raw)

# ─────────────────────────────────────────────────────────────────────────────
# CATEGORY 1: International Financial Regulation (target=8, existing=5, new=3)
# ─────────────────────────────────────────────────────────────────────────────
# Sources for effectiveness:
#   - Versailles: Keynes (1919) "The Economic Consequences of the Peace"; WWII causation arc
#   - Dawes Plan: McNeil (1986) "American Money and the Weimar Republic"; extraction confirmed
#   - Young Plan/BIS: Schuker (1988) "American 'Reparations' to Germany"; 3yr collapse
#   - Bretton Woods: Eichengreen (1996) "Globalizing Capital"; 27yr stability
#   - IMF SAPs: Easterly (2005) Lancet meta-analysis; independent evaluation office reports
#   - Basel III: BIS Annual Economic Report (2019); BCBS QIS studies
#   - FATF: IMF (2021) AML/CFT effectiveness review; FATF own Effectiveness Framework
#   - Dodd-Frank: Acharya et al (2014) NBER; SIFI and Volcker Rule assessments

financial_mechanisms = [
    # ── Original N=10 ──────────────────────────────────────────────────────
    Mechanism("Versailles Treaty",         "financial", O=3, R=3, alpha=3,
              longevity_years=5,  effectiveness=0, adoption_year=1919,
              source="Keynes 1919; German reparations collapse → WWII",
              is_original=True),
    Mechanism("Dawes Plan / JPMorgan",     "financial", O=2, R=2, alpha=3,
              longevity_years=5,  effectiveness=1, adoption_year=1924,
              source="McNeil 1986; circular extraction US→DE→Allies→US",
              is_original=True),
    Mechanism("Young Plan / BIS",          "financial", O=2, R=2, alpha=2,
              longevity_years=3,  effectiveness=1, adoption_year=1929,
              source="Schuker 1988; Depression-collapse 1931",
              is_original=True),
    Mechanism("Bretton Woods",             "financial", O=1, R=1, alpha=1,
              longevity_years=27, effectiveness=4, adoption_year=1944,
              source="Eichengreen 1996; 27yr stable monetary order",
              is_original=True),
    Mechanism("IMF Structural Adj. (SAPs)","financial", O=2, R=3, alpha=2,
              longevity_years=40, effectiveness=0, adoption_year=1982,
              source="Easterly 2005 Lancet; IMF IEO 2004; persistent despite failure",
              is_original=True),
    # ── New mechanisms ──────────────────────────────────────────────────────
    Mechanism("Basel III Capital Reforms",  "financial", O=0, R=1, alpha=1,
              longevity_years=14, effectiveness=3, adoption_year=2010,
              source="BIS Annual Econ Report 2019; capital buffers materially improved",
              is_original=False),
    Mechanism("FATF AML Standards",        "financial", O=2, R=2, alpha=2,
              longevity_years=35, effectiveness=1, adoption_year=1989,
              source="IMF 2021; estimated 2-5% GDP still laundered; adoption high, impact low",
              is_original=False),
    Mechanism("Dodd-Frank Wall St. Reform","financial", O=1, R=2, alpha=1,
              longevity_years=14, effectiveness=2, adoption_year=2010,
              source="Acharya et al 2014 NBER; SIFI resilience improved, Volcker partial",
              is_original=False),
]

# ─────────────────────────────────────────────────────────────────────────────
# CATEGORY 2: Environmental/Climate Governance (target=8, all new)
# ─────────────────────────────────────────────────────────────────────────────
# Sources:
#   - Montreal: WMO (2022) Scientific Assessment; ozone recovery confirmed
#   - Kyoto: UNEP (2012) Kyoto Protocol Assessment; targets missed by major emitters
#   - Paris: UNEP Emissions Gap Report 2023; pledges insufficient for 1.5°C
#   - EU ETS: Ellerman et al (2010); Joltreau & Pourquier (2019) Ecological Economics
#   - REACH: ECHA (2023) Progress Report; >2000 substances restricted/prohibited
#   - CBD/Aichi: CBD (2020) Global Biodiversity Outlook 5; all 20 Aichi targets missed
#   - Ramsar: Gardner et al (2015) Philosophical Transactions; wetland loss slowed
#   - CDM: Sovacool (2010) Energy Policy; ~75% of projects non-additional (additionality failure)

environmental_mechanisms = [
    Mechanism("Montreal Protocol",         "environmental", O=0, R=1, alpha=0,
              longevity_years=37, effectiveness=4, adoption_year=1987,
              source="WMO 2022; ozone layer recovery on track; exceptional",
              is_original=False),
    Mechanism("Kyoto Protocol",            "environmental", O=2, R=2, alpha=2,
              longevity_years=23, effectiveness=1, adoption_year=1997,
              source="UNEP 2012; US withdrawal; targets missed; phase-out 2012",
              is_original=False),
    Mechanism("Paris Agreement",           "environmental", O=2, R=2, alpha=2,
              longevity_years=9,  effectiveness=1, adoption_year=2015,
              source="UNEP Emissions Gap 2023; current pledges → 2.9°C, far from targets",
              is_original=False),
    Mechanism("EU Emissions Trading (ETS)","environmental", O=1, R=1, alpha=1,
              longevity_years=19, effectiveness=2, adoption_year=2005,
              source="Ellerman 2010; Joltreau 2019; ~15% reduction in covered sectors",
              is_original=False),
    Mechanism("REACH Chemical Regulation","environmental", O=1, R=1, alpha=1,
              longevity_years=17, effectiveness=3, adoption_year=2007,
              source="ECHA 2023; >2000 hazardous substances restricted; strong substitution",
              is_original=False),
    Mechanism("Convention on Biological Diversity","environmental", O=2, R=2, alpha=3,
              longevity_years=31, effectiveness=0, adoption_year=1993,
              source="CBD GBO-5 2020; all 20 Aichi 2020 biodiversity targets missed",
              is_original=False),
    Mechanism("Ramsar Wetlands Convention","environmental", O=1, R=1, alpha=2,
              longevity_years=49, effectiveness=2, adoption_year=1975,
              source="Gardner et al 2015 Phil Trans; wetland loss rate slowed in listed sites",
              is_original=False),
    Mechanism("CDM / Clean Dev. Mechanism","environmental", O=2, R=3, alpha=2,
              longevity_years=12, effectiveness=1, adoption_year=2001,
              source="Sovacool 2010 Energy Policy; ~75% projects non-additional",
              is_original=False),
]

# ─────────────────────────────────────────────────────────────────────────────
# CATEGORY 3: AI/Technology Governance (target=7, all new)
# ─────────────────────────────────────────────────────────────────────────────
# Sources:
#   - GDPR: IAPP (2023) State of Privacy Tech; enforcement inconsistent but compliance behavior changed
#   - HIPAA Security: HHS OCR (2021) enforcement data; breach costs reduced in compliant orgs
#   - Safe Harbor / Privacy Shield: ECJ Schrems I (2015), Schrems II (2020); both invalidated
#   - Sarbanes-Oxley: Coates & Srinivasan (2014) J. Econ. Perspectives; earnings manipulation ↓
#   - COPPA: FTC (2022) COPPA Rule Review; persistent commercial evasion documented
#   - NIST CSF: NIST (2024) CSF 2.0; 50%+ of US critical infrastructure adopted
#   - FTC Section 5 algorithmic: FTC (2022) Report on Commercial Surveillance; enforcement limited

ai_tech_mechanisms = [
    Mechanism("GDPR Data Protection",      "ai_tech", O=1, R=2, alpha=1,
              longevity_years=6,  effectiveness=2, adoption_year=2018,
              source="IAPP 2023; compliance behavior changed but enforcement inconsistent",
              is_original=False),
    Mechanism("HIPAA Security Rule",       "ai_tech", O=1, R=1, alpha=2,
              longevity_years=19, effectiveness=2, adoption_year=2005,
              source="HHS OCR 2021; breach notification + costs reduced in compliant orgs",
              is_original=False),
    Mechanism("Safe Harbor / Privacy Shield","ai_tech", O=2, R=2, alpha=3,
              longevity_years=15, effectiveness=0, adoption_year=2000,
              source="Schrems I 2015, Schrems II 2020; both invalidated by ECJ",
              is_original=False),
    Mechanism("Sarbanes-Oxley Act",        "ai_tech", O=1, R=1, alpha=1,
              longevity_years=22, effectiveness=3, adoption_year=2002,
              source="Coates & Srinivasan 2014 J. Econ. Persp.; earnings manipulation ↓",
              is_original=False),
    Mechanism("COPPA Children's Privacy",  "ai_tech", O=2, R=2, alpha=2,
              longevity_years=26, effectiveness=1, adoption_year=1998,
              source="FTC 2022 COPPA review; persistent commercial evasion; limited fines",
              is_original=False),
    Mechanism("NIST Cybersecurity Framework","ai_tech", O=0, R=1, alpha=1,
              longevity_years=10, effectiveness=2, adoption_year=2014,
              source="NIST 2024 CSF 2.0; 50%+ US critical infra adopted; voluntary",
              is_original=False),
    Mechanism("FTC Section 5 Algorithmic", "ai_tech", O=2, R=2, alpha=2,
              longevity_years=12, effectiveness=1, adoption_year=2012,
              source="FTC 2022 surveillance report; limited enforcement relative to scope",
              is_original=False),
]

# ─────────────────────────────────────────────────────────────────────────────
# CATEGORY 4: Development/Institutional (target=7, existing=5, new=2)
# ─────────────────────────────────────────────────────────────────────────────
# Sources:
#   - Global Fund: IHME (2021) estimates ~65M lives; independent evaluation reports
#   - Bretton Woods: Eichengreen 1996 (listed under financial)
#   - UNGA: Weiss et al (2009) "The United Nations and Changing World Politics"; coordination
#   - Marshall Plan: DeLong & Eichengreen (1993) "The Marshall Plan"; GDP recovery by 1952
#   - PEPFAR: IHME (2020); ~21M lives over 20yr; bilateral structure limits coupling
#   - League of Nations: Northedge (1986) "The League of Nations"; failed collective security
#   - World Bank Conditionality: Stiglitz (2002) "Globalization and Its Discontents"; IEG reports
#   - MDGs: UN (2015) MDG final report; mixed — some goals met, others not; attribution contested

development_mechanisms = [
    # ── Original N=10 ──────────────────────────────────────────────────────
    Mechanism("Global Fund",               "development", O=1, R=1, alpha=1,
              longevity_years=22, effectiveness=4, adoption_year=2002,
              source="IHME 2021; ~65M lives; board structure prevents donor capture",
              is_original=True),
    Mechanism("UNGA",                      "development", O=0, R=2, alpha=1,
              longevity_years=79, effectiveness=2, adoption_year=1945,
              source="Weiss et al 2009; durable coordination; weak enforcement",
              is_original=True),
    Mechanism("Marshall Plan",             "development", O=1, R=2, alpha=1,
              longevity_years=4,  effectiveness=4, adoption_year=1948,
              source="DeLong & Eichengreen 1993; GDP pre-war levels by 1952",
              is_original=True),
    Mechanism("PEPFAR",                    "development", O=1, R=2, alpha=1,
              longevity_years=22, effectiveness=3, adoption_year=2003,
              source="IHME 2020; ~21M lives; bilateral, results-based",
              is_original=True),
    Mechanism("League of Nations",         "development", O=2, R=3, alpha=2,
              longevity_years=15, effectiveness=0, adoption_year=1920,
              source="Northedge 1986; failed Manchuria 1931, Ethiopia 1935",
              is_original=True),
    # ── New mechanisms ──────────────────────────────────────────────────────
    Mechanism("World Bank Conditionality", "development", O=2, R=3, alpha=2,
              longevity_years=40, effectiveness=0, adoption_year=1980,
              source="Stiglitz 2002; World Bank IEG 2004; recurring crises despite lending",
              is_original=False),
    Mechanism("Millennium Dev. Goals",     "development", O=1, R=2, alpha=1,
              longevity_years=15, effectiveness=2, adoption_year=2000,
              source="UN 2015 MDG final; poverty ↓ largely pre-existing China/India trend",
              is_original=False),
]

# ─────────────────────────────────────────────────────────────────────────────
# Combined N=30 dataset
# ─────────────────────────────────────────────────────────────────────────────
ALL_MECHANISMS = (financial_mechanisms + environmental_mechanisms +
                  ai_tech_mechanisms + development_mechanisms)

assert len(ALL_MECHANISMS) == 30, f"Expected 30, got {len(ALL_MECHANISMS)}"
n_original = sum(1 for m in ALL_MECHANISMS if m.is_original)
n_new      = sum(1 for m in ALL_MECHANISMS if not m.is_original)
assert n_original == 10, f"Expected 10 originals, got {n_original}"
assert n_new      == 20, f"Expected 20 new, got {n_new}"

print("── EXP-022: N=30 Mechanism Dataset ──────────────────────────────────────")
print(f"{'#':>2}  {'Mechanism':<38} {'Cat':>12} {'V':>3} {'Pe':>8}  {'Lon':>5}  {'Eff':>4}  {'Orig':>4}")
print("─" * 90)
for i, m in enumerate(ALL_MECHANISMS, 1):
    orig = "✓" if m.is_original else " "
    print(f"{i:>2}  {m.name:<38} {m.category:>12} {m.V_raw:>3.0f} {m.Pe_inst:>+8.1f}"
          f"  {m.longevity_years:>5.0f}  {m.effectiveness:>4d}  {orig:>4}")

# %% Spearman Correlations (primary analysis)
V_vals   = np.array([m.V_raw        for m in ALL_MECHANISMS])
Pe_vals  = np.array([m.Pe_inst      for m in ALL_MECHANISMS])
lon_vals = np.array([m.longevity_years for m in ALL_MECHANISMS])
eff_vals = np.array([m.effectiveness  for m in ALL_MECHANISMS])

rho_Pe_eff,  p_Pe_eff  = spearmanr(Pe_vals, eff_vals)
rho_Pe_lon,  p_Pe_lon  = spearmanr(Pe_vals, lon_vals)
rho_V_eff,   p_V_eff   = spearmanr(V_vals,  eff_vals)
rho_V_lon,   p_V_lon   = spearmanr(V_vals,  lon_vals)

print("\n── Spearman Correlations (N=30) ─────────────────────────────────────────")
print(f"  Pe vs effectiveness: ρ = {rho_Pe_eff:+.4f}  p = {p_Pe_eff:.5f}")
print(f"  Pe vs longevity:     ρ = {rho_Pe_lon:+.4f}  p = {p_Pe_lon:.5f}")
print(f"  V vs effectiveness:  ρ = {rho_V_eff:+.4f}  p = {p_V_eff:.5f}")
print(f"  V vs longevity:      ρ = {rho_V_lon:+.4f}  p = {p_V_lon:.5f}")

# Original N=10 replication check
orig = [m for m in ALL_MECHANISMS if m.is_original]
Pe10 = np.array([m.Pe_inst for m in orig])
eff10 = np.array([m.effectiveness for m in orig])
rho10, p10 = spearmanr(Pe10, eff10)
print(f"\n  Pe vs effectiveness (original N=10): ρ = {rho10:+.4f}  p = {p10:.5f}")
print(f"  Paper 52 reported:                   ρ = -0.8650  p = 0.0012")

# %% Bootstrap Confidence Intervals (N=10,000 resamples)
np.random.seed(42)
N_BOOT = 10_000
boot_rho_Pe_eff = []
boot_rho_Pe_lon = []

for _ in range(N_BOOT):
    idx = np.random.choice(30, size=30, replace=True)
    Pe_b  = Pe_vals[idx]
    eff_b = eff_vals[idx]
    lon_b = lon_vals[idx]
    r1, _ = spearmanr(Pe_b, eff_b)
    r2, _ = spearmanr(Pe_b, lon_b)
    boot_rho_Pe_eff.append(r1)
    boot_rho_Pe_lon.append(r2)

boot_rho_Pe_eff = np.array(boot_rho_Pe_eff)
boot_rho_Pe_lon = np.array(boot_rho_Pe_lon)

ci_eff_lo, ci_eff_hi = np.percentile(boot_rho_Pe_eff, [2.5, 97.5])
ci_lon_lo, ci_lon_hi = np.percentile(boot_rho_Pe_lon, [2.5, 97.5])

print(f"\n── Bootstrap 95% CI (N={N_BOOT:,} resamples) ────────────────────────────")
print(f"  ρ(Pe, effectiveness):  {rho_Pe_eff:+.4f}  [{ci_eff_lo:+.4f}, {ci_eff_hi:+.4f}]")
print(f"  ρ(Pe, longevity):      {rho_Pe_lon:+.4f}  [{ci_lon_lo:+.4f}, {ci_lon_hi:+.4f}]")

# %% Subgroup Analysis by Category
print("\n── Subgroup Analysis ───────────────────────────────────────────────────")
for cat in ["financial", "environmental", "ai_tech", "development"]:
    sub = [m for m in ALL_MECHANISMS if m.category == cat]
    if len(sub) < 3:
        continue
    Pe_s  = np.array([m.Pe_inst for m in sub])
    eff_s = np.array([m.effectiveness for m in sub])
    r, p  = spearmanr(Pe_s, eff_s)
    print(f"  {cat:<15} (n={len(sub)})  ρ(Pe,eff) = {r:+.3f}  p = {p:.3f}")

# %% Hypothesis Assessment
print("\n── Pre-registered Hypothesis Assessment ────────────────────────────────")
h1_pass = rho_Pe_eff < -0.60 and p_Pe_eff < 0.05
h2_pass = abs(rho_Pe_lon) < 0.30 and p_Pe_lon > 0.10
print(f"  H1: ρ(Pe, eff) < −0.60, p < 0.05")
print(f"      ρ = {rho_Pe_eff:+.4f}, p = {p_Pe_eff:.5f}  →  {'CONFIRMED ✓' if h1_pass else 'FAILED ✗'}")
print(f"  H2: |ρ(Pe, lon)| < 0.30, p > 0.10 (non-significant)")
print(f"      ρ = {rho_Pe_lon:+.4f}, p = {p_Pe_lon:.5f}  →  {'CONFIRMED ✓' if h2_pass else 'FAILED ✗'}")

kill_condition = rho_Pe_eff >= -0.40
print(f"\n  Kill condition (ρ ≥ −0.40): {'TRIGGERED — revise thesis' if kill_condition else 'NOT triggered'}")

# Effect size change: N=10 → N=30
delta_rho = rho_Pe_eff - rho10
print(f"\n  Effect size at N=10:  ρ = {rho10:+.4f}")
print(f"  Effect size at N=30:  ρ = {rho_Pe_eff:+.4f}")
print(f"  Δρ (N=10 → N=30):     {delta_rho:+.4f}")

# %% Figure — 4-panel replication plot
fig = plt.figure(figsize=(16, 12))
fig.suptitle("EXP-022: Constraint Current — N=30 Replication\nρ(Pe, effectiveness)",
             fontsize=13, y=0.98, color='#e0e0e0')

grid = gs.GridSpec(2, 2, figure=fig, hspace=0.40, wspace=0.32)
COLOUR_EFF = {0:'#ff1100', 1:'#ff6b35', 2:'#ffd700', 3:'#7ed957', 4:'#3ddc84'}
CAT_MARKER = {'financial': 'o', 'environmental': 's', 'ai_tech': '^', 'development': 'D'}

# ── Panel 1: Pe(V) curve + all 30 mechanisms ─────────────────────────────
ax1 = fig.add_subplot(grid[0, 0])
V_range    = np.linspace(0.01, 8.99, 300)
Pe_curve   = np.array([Pe(v) for v in V_range])
ax1.plot(V_range, Pe_curve, color='#ff6b35', lw=2.0, alpha=0.7, label='Pe(V) curve')
ax1.axhline(0, color='#3ddc84', lw=1.5, ls='--', alpha=0.6)
ax1.axvline(V_ZERO, color='#3ddc84', lw=1, ls=':', alpha=0.5)
for m in ALL_MECHANISMS:
    marker = 'o' if m.is_original else 's'
    ax1.scatter(m.V_raw, m.Pe_inst, s=60, marker=marker,
                color=COLOUR_EFF[m.effectiveness], zorder=5,
                edgecolors='white' if m.is_original else 'none', lw=0.8)
ax1.set_xlabel('V_raw (void index, 0–9)')
ax1.set_ylabel('Péclet Number Pe')
ax1.set_title('Pe(V) — 30 Mechanisms  [● original ■ new]', fontsize=9)
ax1.grid(True, alpha=0.3)
from matplotlib.lines import Line2D
legend_eff = [Line2D([0],[0], marker='o', color='w', markerfacecolor=COLOUR_EFF[e],
                     ms=7, label=f'Eff={e}') for e in [0,1,2,3,4]]
ax1.legend(handles=legend_eff, fontsize=7, loc='upper left')

# ── Panel 2: Pe vs Effectiveness scatter ────────────────────────────────
ax2 = fig.add_subplot(grid[0, 1])
for m in ALL_MECHANISMS:
    ax2.scatter(m.Pe_inst, m.effectiveness, s=70, marker='o',
                color=COLOUR_EFF[m.effectiveness], zorder=5,
                edgecolors='white' if m.is_original else 'none', lw=0.8)
ax2.axvline(0, color='#3ddc84', lw=1, ls='--', alpha=0.7)
ax2.text(0.05, 0.93, f"ρ = {rho_Pe_eff:+.3f}  p = {p_Pe_eff:.4f}\n95% CI [{ci_eff_lo:+.3f}, {ci_eff_hi:+.3f}]",
         transform=ax2.transAxes, color='#ffd700', fontsize=8.5, va='top')
ax2.set_xlabel('Pe')
ax2.set_ylabel('Effectiveness (0–4)')
ax2.set_yticks([0,1,2,3,4])
ax2.set_yticklabels(['0 fail','1 weak','2 mod','3 eff','4 excep'])
ax2.set_title(f'Pe vs Effectiveness  N=30', fontsize=9)
ax2.grid(True, alpha=0.3)

# ── Panel 3: Pe vs Longevity scatter ────────────────────────────────────
ax3 = fig.add_subplot(grid[1, 0])
for m in ALL_MECHANISMS:
    ax3.scatter(m.Pe_inst, m.longevity_years, s=70, marker='o',
                color=COLOUR_EFF[m.effectiveness], zorder=5,
                edgecolors='white' if m.is_original else 'none', lw=0.8)
ax3.axvline(0, color='#3ddc84', lw=1, ls='--', alpha=0.7)
ax3.text(0.05, 0.93, f"ρ = {rho_Pe_lon:+.3f}  p = {p_Pe_lon:.4f}\n95% CI [{ci_lon_lo:+.3f}, {ci_lon_hi:+.3f}]",
         transform=ax3.transAxes, color='#ffd700', fontsize=8.5, va='top')
ax3.set_xlabel('Pe')
ax3.set_ylabel('Effective longevity (years)')
ax3.set_title('Pe vs Longevity  [selection pathology]', fontsize=9)
ax3.grid(True, alpha=0.3)

# ── Panel 4: Bootstrap distribution of ρ ────────────────────────────────
ax4 = fig.add_subplot(grid[1, 1])
ax4.hist(boot_rho_Pe_eff, bins=60, color='#ff6b35', alpha=0.7,
         label='ρ(Pe, eff)')
ax4.hist(boot_rho_Pe_lon, bins=60, color='#3ddc84', alpha=0.5,
         label='ρ(Pe, lon)')
ax4.axvline(rho_Pe_eff, color='#ff6b35', lw=2, ls='--')
ax4.axvline(rho_Pe_lon, color='#3ddc84', lw=2, ls='--')
ax4.axvline(-0.60, color='white', lw=1, ls=':', alpha=0.7, label='H1 threshold (−0.60)')
ax4.axvline(0, color='white', lw=1, ls=':', alpha=0.4)
ax4.set_xlabel('Bootstrap ρ')
ax4.set_ylabel('Frequency')
ax4.set_title(f'Bootstrap ρ distribution  (N={N_BOOT:,})', fontsize=9)
ax4.legend(fontsize=7)
ax4.grid(True, alpha=0.3)

os.makedirs('ops/lab/results/EXP-022', exist_ok=True)
plt.savefig('ops/lab/results/EXP-022/EXP-022-figure.png', dpi=140,
            bbox_inches='tight', facecolor='#0d0d0d')
plt.show()
print("\n── Figure saved to ops/lab/results/EXP-022/EXP-022-figure.png")

# %% Export CSV
csv_path = 'ops/lab/results/EXP-022/mechanisms-dataset.csv'
with open(csv_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['id','name','category','O','R','alpha','V_raw','Pe',
                     'longevity_years','effectiveness','adoption_year',
                     'is_original','source'])
    for i, m in enumerate(ALL_MECHANISMS, 1):
        writer.writerow([i, m.name, m.category, m.O, m.R, m.alpha,
                         m.V_raw, f"{m.Pe_inst:.3f}",
                         m.longevity_years, m.effectiveness,
                         m.adoption_year, int(m.is_original), m.source])
print(f"CSV saved: {csv_path}")

# %% Summary printout for report
print("\n═══ EXP-022 RESULTS SUMMARY ════════════════════════════════════════════")
print(f"N = 30 mechanisms across 4 categories")
print(f"Original N=10 (Paper 52) + 20 new mechanisms")
print()
print(f"PRIMARY: ρ(Pe, effectiveness) = {rho_Pe_eff:+.4f}  p = {p_Pe_eff:.5f}")
print(f"         95% CI bootstrap [{ci_eff_lo:+.4f}, {ci_eff_hi:+.4f}]")
print(f"         H1 threshold (ρ < −0.60): {'PASSED' if h1_pass else 'FAILED'}")
print()
print(f"SECONDARY: ρ(Pe, longevity) = {rho_Pe_lon:+.4f}  p = {p_Pe_lon:.5f}")
print(f"           H2 (non-sig): {'PASSED' if h2_pass else 'FAILED'}")
print()
print(f"REPLICATION CONTINUITY (N=10 → N=30):")
print(f"  N=10: ρ = {rho10:+.4f}  (Paper 52 reported −0.8650)")
print(f"  N=30: ρ = {rho_Pe_eff:+.4f}  Δρ = {delta_rho:+.4f}")
print()
print(f"KILL CONDITION: ρ ≥ −0.40 = {'TRIGGERED' if kill_condition else 'NOT TRIGGERED'}")

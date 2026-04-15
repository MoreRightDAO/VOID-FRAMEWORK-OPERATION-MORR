#!/usr/bin/env python3
"""
Parse and combine state-level YRBS data from two CDC sources:
  1. DASH YRBSS High School (Socrata: svam-8dhg) — covers 2011-2017, has sample sizes
  2. YRBSS Mental Health Indicators (Socrata: nu3s-3dwd) — covers 2019-2023, no sample sizes

Output: state_yrbs_combined.csv with columns:
  state, state_abbr, year, sex, pct_sadness, pct_sadness_lo, pct_sadness_hi,
  pct_suicide, pct_suicide_lo, pct_suicide_hi, n_sadness, n_suicide
"""

import csv
import os
import sys
from collections import defaultdict

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# US state abbreviation mapping
STATE_ABBR = {
    'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR',
    'California': 'CA', 'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE',
    'Florida': 'FL', 'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID',
    'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA', 'Kansas': 'KS',
    'Kentucky': 'KY', 'Louisiana': 'LA', 'Maine': 'ME', 'Maryland': 'MD',
    'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS',
    'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV',
    'New Hampshire': 'NH', 'New Jersey': 'NJ', 'New Mexico': 'NM', 'New York': 'NY',
    'North Carolina': 'NC', 'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK',
    'Oregon': 'OR', 'Pennsylvania': 'PA', 'Rhode Island': 'RI', 'South Carolina': 'SC',
    'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT',
    'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA', 'West Virginia': 'WV',
    'Wisconsin': 'WI', 'Wyoming': 'WY',
    # DC + territories
    'District of Columbia': 'DC',
    # Special cases in mental health dataset
    'United States': 'US',
    'New York (Excluding New York City)': 'NY',
}

# Reverse mapping
ABBR_STATE = {v: k for k, v in STATE_ABBR.items()}
ABBR_STATE['US'] = 'United States'

# Some DASH data uses non-standard abbreviations
DASH_ABBR_FIX = {
    'AZB': 'AZ',  # Arizona uses AZB in some DASH data
    'XX': 'US',   # National data uses XX
}

# Target years
TARGET_YEARS = {2011, 2013, 2015, 2017, 2019, 2021, 2023}

def parse_dash(filepath):
    """Parse DASH YRBSS CSV (2011-2017 state-level data with sample sizes)."""
    data = {}  # key: (state_abbr, year, sex) -> {sadness: ..., suicide: ...}

    with open(filepath) as f:
        reader = csv.DictReader(f)
        for row in reader:
            year = int(row['year'])
            if year not in TARGET_YEARS:
                continue

            abbr = row['locationabbr'].strip()
            abbr = DASH_ABBR_FIX.get(abbr, abbr)
            sex = row['sex'].strip()
            question = row['shortquestiontext'].strip()
            value = row['greater_risk_data_value'].strip()
            lo = row['greater_risk_low_confidence_limit'].strip()
            hi = row['greater_risk_high_confidence_limit'].strip()
            n = row['sample_size'].strip()

            if not value:
                continue

            key = (abbr, year, sex)
            if key not in data:
                data[key] = {}

            if question == 'Sad or hopeless':
                data[key]['pct_sadness'] = float(value)
                data[key]['pct_sadness_lo'] = float(lo) if lo else None
                data[key]['pct_sadness_hi'] = float(hi) if hi else None
                data[key]['n_sadness'] = int(n) if n else None
            elif question == 'Considered suicide':
                data[key]['pct_suicide'] = float(value)
                data[key]['pct_suicide_lo'] = float(lo) if lo else None
                data[key]['pct_suicide_hi'] = float(hi) if hi else None
                data[key]['n_suicide'] = int(n) if n else None

    return data


def parse_mental_health(filepath):
    """Parse YRBSS Mental Health Indicators CSV (2019-2023)."""
    data = {}

    with open(filepath) as f:
        reader = csv.DictReader(f)
        for row in reader:
            year = int(row['Year'])
            if year not in TARGET_YEARS:
                continue

            area = row['Area'].strip()
            demo_type = row['Demographics_Type'].strip()
            demo_val = row['Demographics_Value'].strip()
            question = row['Question'].lower()
            pct = row['Percent'].strip()
            lo = row['Low_Confidence_Interval'].strip()
            hi = row['High_Confidence_Interval'].strip()

            # Only want sex stratification and total
            if demo_type == 'Sex':
                sex = demo_val  # 'Female' or 'Male'
            elif demo_type == 'Total':
                sex = 'Total'
            else:
                continue  # skip race/ethnicity breakdowns

            # Map area name to abbreviation
            abbr = STATE_ABBR.get(area)
            if not abbr:
                # Skip territories not in our mapping
                continue

            if not pct:
                continue

            key = (abbr, year, sex)
            if key not in data:
                data[key] = {}

            if 'sad or hopeless' in question:
                data[key]['pct_sadness'] = float(pct)
                data[key]['pct_sadness_lo'] = float(lo) if lo else None
                data[key]['pct_sadness_hi'] = float(hi) if hi else None
                # No sample size in this dataset
            elif 'seriously consider' in question:
                data[key]['pct_suicide'] = float(pct)
                data[key]['pct_suicide_lo'] = float(lo) if lo else None
                data[key]['pct_suicide_hi'] = float(hi) if hi else None


    return data


def combine_and_write(dash_data, mh_data, outpath):
    """Combine both datasets and write CSV."""
    # Merge: dash covers 2011-2017, mh covers 2019-2023
    combined = {}
    combined.update(dash_data)
    # For 2019+, use mental health dataset (should not overlap with DASH)
    for key, vals in mh_data.items():
        if key in combined:
            # Merge any missing fields
            for k, v in vals.items():
                if k not in combined[key] or combined[key][k] is None:
                    combined[key][k] = v
        else:
            combined[key] = vals

    # Write output
    fieldnames = [
        'state', 'state_abbr', 'year', 'sex',
        'pct_sadness', 'pct_sadness_lo', 'pct_sadness_hi',
        'pct_suicide', 'pct_suicide_lo', 'pct_suicide_hi',
        'n_sadness', 'n_suicide'
    ]

    rows = []
    for (abbr, year, sex), vals in sorted(combined.items()):
        state_name = ABBR_STATE.get(abbr, abbr)
        row = {
            'state': state_name,
            'state_abbr': abbr,
            'year': year,
            'sex': sex,
            'pct_sadness': round(vals.get('pct_sadness', 0), 2) if vals.get('pct_sadness') is not None else '',
            'pct_sadness_lo': round(vals.get('pct_sadness_lo', 0), 2) if vals.get('pct_sadness_lo') is not None else '',
            'pct_sadness_hi': round(vals.get('pct_sadness_hi', 0), 2) if vals.get('pct_sadness_hi') is not None else '',
            'pct_suicide': round(vals.get('pct_suicide', 0), 2) if vals.get('pct_suicide') is not None else '',
            'pct_suicide_lo': round(vals.get('pct_suicide_lo', 0), 2) if vals.get('pct_suicide_lo') is not None else '',
            'pct_suicide_hi': round(vals.get('pct_suicide_hi', 0), 2) if vals.get('pct_suicide_hi') is not None else '',
            'n_sadness': vals.get('n_sadness', ''),
            'n_suicide': vals.get('n_suicide', ''),
        }
        rows.append(row)

    with open(outpath, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    return rows


def print_summary(rows):
    """Print summary statistics."""
    years = sorted(set(r['year'] for r in rows))
    states = sorted(set(r['state_abbr'] for r in rows))
    sexes = sorted(set(r['sex'] for r in rows))

    print(f"\n{'='*70}")
    print(f"STATE-LEVEL YRBS DATA SUMMARY")
    print(f"{'='*70}")
    print(f"Total rows: {len(rows)}")
    print(f"Years: {years}")
    print(f"States/territories: {len(states)}")
    print(f"Sex categories: {sexes}")

    # Coverage matrix
    print(f"\n{'Coverage by year and sex':}")
    print(f"{'Year':<8} {'Female':<10} {'Male':<10} {'Total':<10}")
    print(f"{'-'*38}")
    for year in years:
        yr_rows = [r for r in rows if r['year'] == year]
        f_count = sum(1 for r in yr_rows if r['sex'] == 'Female' and r['pct_sadness'])
        m_count = sum(1 for r in yr_rows if r['sex'] == 'Male' and r['pct_sadness'])
        t_count = sum(1 for r in yr_rows if r['sex'] == 'Total' and r['pct_sadness'])
        print(f"{year:<8} {f_count:<10} {m_count:<10} {t_count:<10}")

    # Sample data
    print(f"\nSample rows (Female sadness by year, first state alphabetically):")
    print(f"{'Year':<6} {'State':<20} {'Sadness%':<12} {'Suicide%':<12} {'N':<8}")
    print(f"{'-'*58}")
    shown = set()
    for r in rows:
        if r['sex'] == 'Female' and r['pct_sadness'] and r['year'] not in shown:
            shown.add(r['year'])
            n_str = str(r['n_sadness']) if r['n_sadness'] else 'N/A'
            print(f"{r['year']:<6} {r['state']:<20} {r['pct_sadness']:<12} {r['pct_suicide']:<12} {n_str:<8}")

    # States with complete data across all target years (Female)
    complete_states = []
    for st in states:
        st_years = set(r['year'] for r in rows if r['state_abbr'] == st and r['sex'] == 'Female' and r['pct_sadness'])
        if TARGET_YEARS.issubset(st_years):
            complete_states.append(st)

    print(f"\nStates with COMPLETE Female sadness data for all 7 survey years:")
    print(f"  {len(complete_states)} states: {', '.join(complete_states)}")

    # States missing data
    missing_by_year = defaultdict(list)
    for year in sorted(TARGET_YEARS):
        states_with_data = set(r['state_abbr'] for r in rows if r['year'] == year and r['sex'] == 'Female' and r['pct_sadness'])
        for st in states:
            if st not in states_with_data:
                missing_by_year[year].append(st)

    if any(missing_by_year.values()):
        print(f"\nStates missing Female sadness data by year:")
        for year in sorted(missing_by_year):
            if missing_by_year[year]:
                print(f"  {year}: {', '.join(sorted(missing_by_year[year]))}")

    # National trend (Female sadness)
    print(f"\nNational-level Female sadness trend (if US/national data present):")
    national = [r for r in rows if r['state_abbr'] == 'DC' and r['sex'] == 'Female']  # Check if DC is used as proxy
    # Actually look for "United States" in state name
    national = [r for r in rows if 'united' in r['state'].lower() and r['sex'] == 'Female']
    if national:
        for r in sorted(national, key=lambda x: x['year']):
            print(f"  {r['year']}: {r['pct_sadness']}%")
    else:
        print("  (No national-level data in state datasets)")


def main():
    dash_file = os.path.join(SCRIPT_DIR, 'dash-all-mental-health.csv')
    dash_national_file = os.path.join(SCRIPT_DIR, 'dash-national.csv')
    mh_file = os.path.join(SCRIPT_DIR, 'yrbs-mental-health.csv')
    out_file = os.path.join(SCRIPT_DIR, 'state_yrbs_combined.csv')

    if not os.path.exists(dash_file):
        print(f"ERROR: Missing {dash_file}")
        print("Download with:")
        print('  curl -o dash-all-mental-health.csv "https://data.cdc.gov/resource/svam-8dhg.csv?$where=questioncode%20in%20(\'H25\',\'H26\')%20AND%20stratificationtype=\'State\'%20AND%20sex%20in%20(\'Female\',\'Male\',\'Total\')%20AND%20race=\'Total\'%20AND%20grade=\'Total\'&$select=year,locationdesc,locationabbr,sex,shortquestiontext,questioncode,greater_risk_data_value,greater_risk_low_confidence_limit,greater_risk_high_confidence_limit,sample_size&$limit=50000&$order=year,locationabbr,sex,questioncode"')
        sys.exit(1)

    if not os.path.exists(mh_file):
        print(f"ERROR: Missing {mh_file}")
        print("Download with:")
        print('  curl -o yrbs-mental-health.csv "https://data.cdc.gov/api/views/nu3s-3dwd/rows.csv?accessType=DOWNLOAD"')
        sys.exit(1)

    print("Parsing DASH YRBSS state data (2011-2017)...")
    dash_data = parse_dash(dash_file)
    print(f"  Parsed {len(dash_data)} state-year-sex records")

    # Also parse national DASH data if available
    if os.path.exists(dash_national_file):
        print("Parsing DASH YRBSS national data (1991-2017)...")
        dash_national = parse_dash(dash_national_file)
        print(f"  Parsed {len(dash_national)} national-year-sex records")
        # Merge national into dash_data
        for key, vals in dash_national.items():
            if key not in dash_data:
                dash_data[key] = vals

    print("Parsing Mental Health Indicators (2019-2023)...")
    mh_data = parse_mental_health(mh_file)
    print(f"  Parsed {len(mh_data)} state-year-sex records")

    print(f"Writing combined data to {out_file}...")
    rows = combine_and_write(dash_data, mh_data, out_file)
    print(f"  Wrote {len(rows)} rows")

    print_summary(rows)


if __name__ == '__main__':
    main()

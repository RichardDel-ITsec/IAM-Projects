
"""
🕵️‍♂️ Orphaned & Inactive Accounts Finder
-----------------------------------------
Reads a CSV of user accounts and flags:
 - Orphaned accounts: active=Yes but no manager assigned
 - Inactive accounts: last login older than N days (default 90)

Outputs:
 - reports/orphaned_accounts_report.csv
 - reports/inactive_accounts_chart.png
 - reports/orphaned_accounts_report_preview.png (table screenshot)

Usage:
    python orphaned_accounts.py [--csv data/sample_users.csv] [--inactive_days 90]
"""

import argparse
from datetime import datetime, timedelta
import os
import pandas as pd
import matplotlib.pyplot as plt

def load_data(csv_path: str) -> pd.DataFrame:
    df = pd.read_csv(csv_path)
    # Basic hygiene
    df['last_login'] = pd.to_datetime(df['last_login'], errors='coerce')
    df['active'] = df['active'].astype(str).str.strip().str.title()  # "Yes"/"No"
    df['manager'] = df['manager'].fillna('').astype(str)
    df['department'] = df['department'].fillna('Unknown')
    return df

def flag_accounts(df: pd.DataFrame, inactive_days: int = 90) -> pd.DataFrame:
    cutoff = pd.Timestamp(datetime.today() - timedelta(days=inactive_days)).normalize()
    orphaned = (df['active'] == 'Yes') & (df['manager'].str.len() == 0)
    inactive = (df['last_login'] < cutoff) & (df['active'] == 'Yes')
    out = df.copy()
    out['status'] = ''
    out.loc[orphaned & inactive, 'status'] = 'Orphaned & Inactive'
    out.loc[orphaned & ~inactive, 'status'] = 'Orphaned'
    out.loc[~orphaned & inactive, 'status'] = 'Inactive'
    # Keep only flagged
    flagged = out[out['status'] != ''].copy()
    # Sort for readability
    flagged = flagged.sort_values(['department', 'status', 'username'])
    return flagged

def save_report(flagged: pd.DataFrame, reports_dir: str):
    os.makedirs(reports_dir, exist_ok=True)
    out_csv = os.path.join(reports_dir, 'orphaned_accounts_report.csv')
    flagged[['username','department','last_login','active','status']].to_csv(out_csv, index=False)
    return out_csv

def chart_inactive_by_dept(df_flagged: pd.DataFrame, reports_dir: str):
    # Count only "Inactive" or "Orphaned & Inactive" per department
    inactive_mask = df_flagged['status'].str.contains('Inactive', case=False, na=False)
    counts = df_flagged[inactive_mask].groupby('department')['username'].count().sort_values(ascending=False)
    if counts.empty:
        return None
    plt.figure(figsize=(8,5))
    counts.plot(kind='bar')  # Do not set explicit colors/styles per instruction
    plt.title('Inactive Accounts by Department')
    plt.xlabel('Department')
    plt.ylabel('Count of Inactive Accounts')
    plt.tight_layout()
    out_png = os.path.join(reports_dir, 'inactive_accounts_chart.png')
    plt.savefig(out_png, dpi=150)
    plt.close()
    return out_png

def preview_table(flagged: pd.DataFrame, reports_dir: str, max_rows: int = 12):
    # Render a preview of the first N rows as a figure
    preview = flagged.head(max_rows)[['username','department','last_login','active','status']]
    if preview.empty:
        return None
    fig, ax = plt.subplots(figsize=(10, 0.5 + 0.35*len(preview)))
    ax.axis('off')
    table = ax.table(cellText=preview.values,
                     colLabels=preview.columns,
                     cellLoc='center',
                     loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(9)
    table.scale(1, 1.2)
    out_png = os.path.join(reports_dir, 'orphaned_accounts_report_preview.png')
    plt.tight_layout()
    plt.savefig(out_png, dpi=150, bbox_inches='tight')
    plt.close(fig)
    return out_png

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--csv', default='data/sample_users.csv')
    parser.add_argument('--inactive_days', type=int, default=90)
    parser.add_argument('--reports_dir', default='reports')
    args = parser.parse_args()

    df = load_data(args.csv)
    flagged = flag_accounts(df, inactive_days=args.inactive_days)
    out_csv = save_report(flagged, args.reports_dir)
    chart_path = chart_inactive_by_dept(flagged, args.reports_dir)
    preview_path = preview_table(flagged, args.reports_dir)

    print(f"Report saved to: {out_csv}")
    if chart_path:
        print(f"Chart saved to: {chart_path}")
    else:
        print("No inactive accounts found; chart not created.")
    if preview_path:
        print(f"Preview image saved to: {preview_path}")

if __name__ == '__main__':
    main()

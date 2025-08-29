# 🕵️‍♂️ Orphaned & Inactive Accounts Finder

This project simulates a common IAM challenge: **orphaned and inactive accounts** in an organisation.  
- **Orphaned accounts**: user accounts still active but with **no manager of record** or **owner** (e.g service accounts(**as Liz noted in interview**)).
- **Inactive accounts**: accounts that haven't logged in for a long period (default **90 days**).

These are **high-risk** for any firm — especially a firm handling sensitive client data — because they can lead to **unauthorised access**, **audit findings**, and **non-compliance** with ISO 27001 and GDPR Article 32.

---

## 🚀 What the script does
1. Reads `data/sample_users.csv` with columns:
   - `username`, `department`, `last_login` (YYYY-MM-DD), `active` (Yes/No), `manager`  
2. Flags accounts as:
   - **Orphaned** → `active=Yes` but `manager` is empty  
   - **Inactive** → `active=Yes` but `last_login` older than **90 days**  
   - **Orphaned & Inactive** → both conditions true  
3. Outputs to the `reports/` folder:
   - `orphaned_accounts_report.csv` → list of flagged accounts
   - `inactive_accounts_chart.png` → bar chart of inactive accounts per department
   - `orphaned_accounts_report_preview.png` → a screenshot-style table of the first flagged rows

---

## 📦 How to run
```bash
python orphaned_accounts.py
# or with custom inputs
python orphaned_accounts.py --csv data/sample_users.csv --inactive_days 60
```

Python dependencies:
- `pandas`
- `matplotlib`

---

## 📊 Example outputs
- **CSV Report** (first rows shown in the preview image): `reports/orphaned_accounts_report.csv`
- **Chart**: `reports/inactive_accounts_chart.png`

Note: In a real environment, I could replace the CSV with a pull from **Active Directory / Entra ID** and schedule this to run weekly, emailing the report to managers for **access recertification**.

---

*Made with ❤️ as a  portfolio project.*

# 🕵️‍♂️ Orphaned & Inactive Accounts Finder

This project simulates a common IAM challenge: **orphaned and inactive accounts** in an organisation.  
- **Orphaned accounts**: user accounts still active but with **no manager of record** (often ex-staff).
- **Inactive accounts**: accounts that haven't logged in for a long period (default **90 days**).

These are **high-risk** for any firm — especially a law firm handling sensitive client data — because they can lead to **unauthorised access**, **audit findings**, and **non-compliance** with ISO 27001 and GDPR Article 32.

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

> Tip: In a real environment, you could replace the CSV with a pull from **Active Directory / Entra ID** and schedule this to run weekly, emailing the report to managers for **access recertification**.

---

## 🧠 Why this project
It's a compact, demonstrable way to show you understand IAM lifecycle controls (joiner–mover–leaver), **least privilege**, and **continuous access review**. It’s also easy to extend — for example:
- Add a rule for **disabled but still licensed** accounts
- Map managers to cost centres for prioritised clean-up
- Create a **Streamlit** dashboard for interactive reviews

---

*Made with ❤️ as a learning and interview portfolio project.*

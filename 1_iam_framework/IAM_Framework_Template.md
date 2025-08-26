## 1. 📚 Executive Summary
A high-level overview of the Identity and Access Management (IAM) framework, its scope, and its alignment with ISO 27001, GDPR, and the needs of a modern law firm.

## 2. 🎯 Objectives
- Securely manage digital identities
- Enforce least privilege and RBAC
- Enable secure collaboration
- Maintain auditability and compliance

## 3. 🧱 Core Components
| Component              | Description                                             |
|------------------------|---------------------------------------------------------|
| Entra ID (Azure AD)    | Central identity source                                 |
| Conditional Access     | Context-based policy enforcement                        |
| MFA                    | Mandatory for all remote/cloud access                   |
| RBAC                   | Access tied to roles like "Fee-earners", "Paralegal", etc.|
| SSO                    | Unified login to Microsoft-365, Onprem apps, and Cloup apps       |
| PAM                    | Control of privileged admin accounts                    |

## 4. 🛡️ Governance & Lifecycle
- **Onboarding**: HR integration, group-based assignment
- **Change Requests**: Power Automate + Manager approval
- **Offboarding**: Auto-deprovisioning, audit logs retention

## 5. ⚙️ Roles & Responsibilities
| Role              | Responsibility                              |
|-------------------|----------------------------------------------|
| IAM Analyst       | Implementation & operations                  |
| IAM SME           | Design governance and architecture           |
| ServiceDesk       | First-line troubleshooting                   |
| Security Officer  | Oversight, compliance, reporting             |

## 6. 📈 KPIs & Metrics
- % of accounts with MFA
- Number of policy exceptions
- Time to provision/deprovision users
- Failed login attempts

## 7. ✅ Compliance Mapping
| Framework | Covered By                                        |
|-----------|---------------------------------------------------|
| ISO 27001 | Access Control, Identity Management               |
| GDPR      | Article 32 (Security), Article 25 (Privacy by Design) |

## 8. 🔄 Continuous Improvement
- Monthly access reviews
- Bi-annual IAM audits
- Feedback from system owners

---

# Operational IAM Policy

Policy Name: Corporate Identity and Access Management Operational Policy

Version: 1.0

Approved By: RICHARD!

Next Review Date: When I get the job🤞

### 1. Purpose

To provide detailed operational guidance for managing identities and access across corporate systems, ensuring security, ISO 27001 compliance, and GDPR adherence.

### 2. Scope

Applies to all employees, contractors, and third-party vendors.

Covers all corporate applications, systems, and data managed via Microsoft Entra ID (Azure AD).

| Role            | Responsibility                       |
|-----------------|----------------------------------------|
| IAM Analyst     | Enforces access provisioning rules, Policy enforcement|
| System Owner    | Validates access requests             |
| HR              | Initiates onboarding/offboarding      |
| Information Security Officer (ISO) | Conducts access audits and reviews|
	
## 4. User Lifecycle Management

### 4.1 Onboarding

Account creation occurs only after HR and manager approval.

Default role assignment based on job function.

MFA enrollment required during account setup.

### 4.2 Offboarding

Accounts deactivated immediately upon termination or contract end.

Access to cloud applications and on-prem systems revoked.

Devices are returned, and credentials are reset.

Account to be deleted in next quaterly review cycle.
### 4.3 Role Changes

Role updates triggered by promotions or departmental moves.

Privileges are adjusted according to new role, as prescride by role matrix.

### 5. Access Control Policy

#### 5.1 Role-Based Access Control (RBAC)

Users assigned to roles with pre-defined permissions.

Access aligned with job responsibilities (least privilege).

#### 5.2 Privileged Access

Managed via Microsoft Entra ID PIM.

Just-in-time access with approval workflow99g.

MFA required for all privileged accounts.

#### 5.3 Conditional Access Rules

Require MFA for remote access and high-risk logins.

Block access from untrusted locations or devices.

Device compliance checks for all corporate endpoints.

#### 5.4 Temporary or Emergency Access

Time-bound and logged in Entra ID.

Approval from ISO or manager required.

Automatic expiration and audit logging enforced.

### 6. Password and Authentication Policy

Minimum password length: 12 characters.

Complexity: uppercase, lowercase, numeric, special character.

Password rotation every 365 days.

MFA required for all accounts.



### 7. Monitoring and Audit

All access events logged in Microsoft Entra ID and forwarded to SIEM.

Automated alerts for unusual login activity.
Monthly access review for all privileged accounts.

Quarterly access review report for all privileged accounts.

Annual audit to ensure compliance with ISO 27001 and GDPR.

### 8. Policy Exceptions

Temporary deviations require formal approval by ISO.

All exceptions logged and reviewed monthly.

### 9. Enforcement

Violation of IAM policies may lead to disciplinary action, account suspension, or termination.

Security incidents must be reported immediately to ISO.

### 10. References

ISO 27001:2013 – Information Security Management Systems

GDPR – General Data Protection Regulation

Microsoft Entra ID (Azure AD) Security Best Practices

# AI Governance Verification & Explainability Assessment Framework

An automated governance toolkit for auditing dynamic pricing models, XAI feature importance logs, and system access trails against EU AI Act, GDPR Article 22, and ISO 27001 requirements.

---

## 📌 Business Context & Problem

Autonomous AI pricing and customer experience (CX) platforms pose significant regulatory and operational risks:
* **Opacity & Black-Box Decisions (EU AI Act Art. 13):** Dynamic pricing adjustments without clear, human-understandable decision drivers risk non-compliance.
* **Unintended Bias (NIST AI RMF):** Machine learning models can inadvertently apply discriminatory price multipliers across demographic segments or proxies.
* **Data Leaks & Access Violations (GDPR Art. 5 / ISO 27001):** System logs processing customer interactions often leak raw, unmasked PII.

This framework provides automated audit checks to continuously verify fairness, explainability, and privacy before and after deployment.

---

## 🏗️ Audit Execution Flow

+-------------------------------+
| Dynamic Pricing & CX Logs     |
+-------------------------------+
                │
                ▼
+-------------------------------+
| Algorithmic Fairness Audit    | ──► Checks Disparate Impact & Regional Price Multipliers
+-------------------------------+
                │
                ▼
+-------------------------------+
| XAI Explainability Audit      | ──► Verifies Top Feature Drivers & Sensitive Proxies
+-------------------------------+
                │
                ▼
+-------------------------------+
| PII & ISO 27001 Log Review    | ──► Scans Diagnostics for Privacy Leaks
+-------------------------------+
                │
                ▼
+-------------------------------+
| Compliance Report & Logs      |
+-------------------------------+

---

## 🛠️ Repository Components

| Directory | Component | Purpose |
| :--- | :--- | :--- |
| python/ | algorithmic_fairness_audit.py | Audits statistical price variance and demographic bias. |
| python/ | xai_explainability_audit.py | Evaluates SHAP/feature importance logs against EU AI Act transparency rules. |
| python/ | pii_masking_log_audit.py | Scans raw diagnostic logs for unmasked PII leaks and audit traceability. |
| docs/ | governance_framework_mapping.md | Direct mapping of technical scripts to EU AI Act, GDPR, and ISO 27001 standards. |
| docs/ | audit_sample_report.json | Output sample of automated compliance verification run. |

---

## 🚀 Quickstart & Verification

### Prerequisites
* Python 3.9+

### 1. Run Algorithmic Fairness Audit
Command to run:
python python/algorithmic_fairness_audit.py

Expected Output:
[INFO] Starting Algorithmic Fairness & Price Variance Audit...
[INFO] Regional Multiplier Metrics:
[PASSED] Price variance across regions is within acceptable fairness boundaries.
[SUCCESS] Algorithmic Fairness Audit PASSED.

### 2. Run XAI Explainability Audit
Command to run:
python python/xai_explainability_audit.py

Expected Output:
[INFO] Starting Explainability (XAI) & Transparency Verification...
[INFO] Primary decision driver identified: 'historical_purchases' (45.0% impact)
[PASSED] Explainability logs meet EU AI Act Article 13 transparency criteria.
[SUCCESS] XAI Transparency Audit PASSED.

### 3. Run PII & Log Privacy Review
Command to run:
python python/pii_masking_log_audit.py

Expected Output:
[INFO] Starting Log Privacy & ISO 27001 Traceability Audit...
[ERROR] [PII LEAK DETECTED] Line 2: Unmasked email exposed in system logs.
[WARNING] PII Redaction Verification FLAGGED LEAKS.

---

## 🛡️ Key Governance Outcomes
* **Transparency Compliance:** Ensures automated pricing adjustments maintain verifiable decision drivers.
* **Bias Prevention:** Proactively detects price disparity anomalies across regional segments.
* **Audit Traceability:** Verifies system access logs adhere to ISO 27001 and GDPR data minimization rules.

# EU AI Act & GDPR Article 22 Compliance Control Mapping

## 1. Scope
This document outlines automated audit controls for high-risk pricing algorithms and automated customer experience decision systems.

## 2. Regulatory Alignment Matrix

| Regulatory Requirement | Compliance Standard | Automated Verification Mechanism |
| :--- | :--- | :--- |
| **Model Transparency & Explainability** | EU AI Act Art. 13 & GDPR Art. 22 | SHAP/XAI Feature Importance Threshold Auditing (`xai_explainability_audit.py`) |
| **Algorithmic Fairness & Non-Discrimination** | EU AI Act Art. 10 & NIST AI RMF | Demographically segmented Disparate Impact & Price Variance Auditing (`algorithmic_fairness_audit.py`) |
| **Data Privacy & Confidentiality** | GDPR Art. 5 (Data Minimization) & ISO 27001 | Dynamic Regex Unmasked PII Detection in Diagnostic Logs (`pii_masking_log_audit.py`) |

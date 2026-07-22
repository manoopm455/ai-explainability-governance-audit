import logging
import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(asctime)s - [%(levelname)s] - %(message)s")

# Mock SHAP / Feature Importance attribution scores
MOCK_FEATURE_IMPORTANCE = {
    "historical_purchases": 0.45,
    "time_on_site": 0.30,
    "device_type": 0.15,
    "zip_code_proxy": 0.10  # Sensitive/proxy attribute check
}

def audit_explainability_logs(feature_weights: dict, sensitive_proxies: list) -> bool:
    """Audits feature importance weights against transparency and prohibited feature rules."""
    logging.info("Starting Explainability (XAI) & Transparency Verification...")
    
    total_weight = sum(feature_weights.values())
    logging.info(f"Total Feature Importance Weight sum: {total_weight:.2f}")
    
    # 1. Audit key driver transparency (GDPR Art. 22)
    top_feature = max(feature_weights, key=feature_weights.get)
    logging.info(f"Primary decision driver identified: '{top_feature}' ({feature_weights[top_feature]*100:.1f}% impact)")
    
    # 2. Check for over-reliance on proxy attributes
    for proxy in sensitive_proxies:
        if proxy in feature_weights and feature_weights[proxy] > 0.05:
            logging.warning(f"[RISK DETECTED] Sensitive proxy feature '{proxy}' contributes {feature_weights[proxy]*100:.1f}% to decisions.")
            return False
            
    logging.info("[PASSED] Explainability logs meet EU AI Act Article 13 transparency criteria.")
    return True

if __name__ == "__main__":
    sensitive_list = ["zip_code_proxy", "ethnicity_proxy"]
    passed = audit_explainability_logs(MOCK_FEATURE_IMPORTANCE, sensitive_list)
    if passed:
        print("\n[SUCCESS] XAI Transparency Audit PASSED.")
    else:
        print("\n[ALERT] Model Explainability Audit Requires Remediation.")

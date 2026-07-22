import logging
import pandas as pd
import numpy as np

logging.basicConfig(level=logging.INFO, format="%(asctime)s - [%(levelname)s] - %(message)s")

# Mock dynamic pricing pipeline decisions
MOCK_PRICING_LOGS = [
    {"user_id": "usr_01", "region": "Region_A", "tier": "Standard", "base_price": 100.0, "final_price": 105.0},
    {"user_id": "usr_02", "region": "Region_A", "tier": "Standard", "base_price": 100.0, "final_price": 104.5},
    {"user_id": "usr_03", "region": "Region_B", "tier": "Standard", "base_price": 100.0, "final_price": 128.0},  # Price variance anomaly
    {"user_id": "usr_04", "region": "Region_B", "tier": "Standard", "base_price": 100.0, "final_price": 106.0},
    {"user_id": "usr_05", "region": "Region_A", "tier": "Premium",  "base_price": 200.0, "final_price": 210.0}
]

def audit_pricing_fairness(df: pd.DataFrame, variance_threshold: float = 0.20) -> bool:
    """Monitors price multiplier variance across demographic regions to flag bias anomalies."""
    logging.info("Starting Algorithmic Fairness & Price Variance Audit...")
    
    df["price_multiplier"] = df["final_price"] / df["base_price"]
    regional_stats = df.groupby("region")["price_multiplier"].agg(["mean", "std"]).reset_index()
    
    logging.info(f"Regional Multiplier Metrics:\n{regional_stats.to_string(index=False)}")
    
    # Check for excessive regional variance
    mean_multipliers = regional_stats["mean"].values
    max_diff = np.max(mean_multipliers) - np.min(mean_multipliers)
    
    if max_diff > variance_threshold:
        logging.warning(f"[FLAGGED] Regional price disparity excessive: Diff = {max_diff:.2f} (Threshold = {variance_threshold})")
        return False
        
    logging.info("[PASSED] Price variance across regions is within acceptable fairness boundaries.")
    return True

if __name__ == "__main__":
    df = pd.DataFrame(MOCK_PRICING_LOGS)
    passed = audit_pricing_fairness(df)
    if passed:
        print("\n[SUCCESS] Algorithmic Fairness Audit PASSED.")
    else:
        print("\n[ALERT] Algorithmic Fairness Audit FLAGGED FOR REVIEW.")

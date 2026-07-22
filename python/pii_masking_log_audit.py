import logging
import re

logging.basicConfig(level=logging.INFO, format="%(asctime)s - [%(levelname)s] - %(message)s")

MOCK_LOG_STREAM = [
    "[2026-07-22 10:00:01] USER_ACCESS - query='SELECT * FROM cx_logs WHERE ticket_id=102' user='agent_44'",
    "[2026-07-22 10:01:15] SYSTEM_LOG - payload='Customer email is john.doe@example.com' status='SUCCESS'", # Unmasked PII leak
    "[2026-07-22 10:02:30] SYSTEM_LOG - payload='Customer phone is ***-***-1234' status='SUCCESS'"
]

def audit_log_privacy(logs: list) -> dict:
    """Scans system logs for unmasked PII leaks and access traceability (ISO 27001)."""
    logging.info("Starting Log Privacy & ISO 27001 Traceability Audit...")
    
    email_regex = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+"
    violations = []
    
    for idx, log in enumerate(logs):
        if re.search(email_regex, log):
            logging.error(f"[PII LEAK DETECTED] Line {idx+1}: Unmasked email exposed in system logs.")
            violations.append(log)
            
    return {"total_logs_scanned": len(logs), "violations_found": len(violations)}

if __name__ == "__main__":
    results = audit_log_privacy(MOCK_LOG_STREAM)
    print(f"\n--- Audit Summary: {results} ---")
    if results["violations_found"] == 0:
        print("[SUCCESS] Log Privacy Audit PASSED.")
    else:
        print("[WARNING] PII Redaction Verification FLAGGED LEAKS.")

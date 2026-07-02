from typing import List, Dict, Any


# Define which types are considered high sensitivity vs medium.
HIGH_SENSITIVITY_TYPES = {
    "aadhaar",
    "credit_card",
    "ifsc",
    "upi",
    "api_key_like",
}

MEDIUM_SENSITIVITY_TYPES = {
    "email",
    "phone",
    "pan",
    "employee_id",
}


def classify_risk(findings: List[Dict[str, Any]]) -> Dict[str, str]:
    """
    Classify overall document risk level based on what types of PII were found.

    Returns a dict like:
    {
        "risk_level": "Low" | "Medium" | "High",
        "reason": "Short explanation string"
    }
    """
    # If there are no findings at all, it's Low risk by default.
    if not findings:
        return {
            "risk_level": "Low",
            "reason": "No sensitive patterns detected in the document.",
        }

    # Collect the set of types present in findings
    types_present = {f["type"] for f in findings}

    # If any high-sensitivity type is present -> High risk
    if types_present & HIGH_SENSITIVITY_TYPES:
        return {
            "risk_level": "High",
            "reason": "High-sensitivity data such as Aadhaar, payment, bank, or API keys is present.",
        }

    # Else if any medium-sensitivity type is present -> Medium risk
    if types_present & MEDIUM_SENSITIVITY_TYPES:
        return {
            "risk_level": "Medium",
            "reason": "Medium-sensitivity data such as email, phone, PAN, or employee IDs is present.",
        }

    # Else, only low-sensitivity indicators (like confidential keywords)
    return {
        "risk_level": "Low",
        "reason": "Only general confidential keywords detected, no specific personal or financial identifiers.",
    }
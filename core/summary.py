from typing import List, Dict, Any

from .detector import aggregate_stats


def build_compliance_summary(findings: List[Dict[str, Any]], risk_info: Dict[str, str]) -> Dict[str, List[str]]:
    """
    Build a rule-based summary:
    - compliance observations
    - security risks
    - suggested remediation steps

    Returns a dict:
    {
        "compliance_observations": [ ... ],
        "security_risks": [ ... ],
        "remediation_steps": [ ... ]
    }
    """
    stats = aggregate_stats(findings)

    compliance_observations: List[str] = []
    security_risks: List[str] = []
    remediation_steps: List[str] = []

    # 1. Compliance observations (what was found)
    if stats:
        compliance_observations.append(
            f"The document contains the following sensitive elements: {stats}."
        )
    else:
        compliance_observations.append(
            "No sensitive elements were detected by the current rule-based patterns."
        )

    # 2. Security risks (based on presence of particular types)
    if stats.get("aadhaar", 0) > 0:
        security_risks.append(
            "Exposure of Aadhaar numbers may lead to identity theft or privacy violations."
        )

    if stats.get("credit_card", 0) > 0:
        security_risks.append(
            "Credit card data in plain text increases the risk of payment fraud."
        )

    if stats.get("ifsc", 0) > 0 or stats.get("upi", 0) > 0:
        security_risks.append(
            "Bank or UPI details are present, which may be misused for financial fraud."
        )

    if stats.get("api_key_like", 0) > 0:
        security_risks.append(
            "API keys or access tokens in the document can allow direct system access."
        )

    if stats.get("email", 0) > 0 or stats.get("phone", 0) > 0:
        security_risks.append(
            "Bulk email or phone data can be used for spam, phishing, or social engineering."
        )

    if stats.get("employee_id", 0) > 0:
        security_risks.append(
            "Employee IDs are present, and may be considered internal-sensitive data."
        )

    if stats.get("confidential_keywords", 0) > 0:
        security_risks.append(
            "The document is marked confidential/proprietary, indicating business sensitivity."
        )

    # 3. Remediation steps (what to do)
    if stats.get("aadhaar", 0) > 0 or stats.get("credit_card", 0) > 0:
        remediation_steps.append(
            "Redact or mask Aadhaar and card numbers before sharing the document externally."
        )

    if stats.get("ifsc", 0) > 0 or stats.get("upi", 0) > 0:
        remediation_steps.append(
            "Avoid sharing full bank or UPI details; use tokenized or anonymized data where possible."
        )

    if stats.get("api_key_like", 0) > 0:
        remediation_steps.append(
            "Immediately rotate exposed API keys and move secrets into a secure vault or environment variables."
        )

    if stats.get("email", 0) > 0 or stats.get("phone", 0) > 0:
        remediation_steps.append(
            "Limit distribution of contact lists and apply appropriate access controls."
        )

    if stats.get("employee_id", 0) > 0:
        remediation_steps.append(
            "Restrict access to documents containing internal employee identifiers."
        )

    if not remediation_steps and stats:
        remediation_steps.append(
            "Review access controls and apply minimum necessary sharing for documents with sensitive indicators."
        )

    if not stats:
        remediation_steps.append(
            "No specific remediation required, but maintain standard security and access controls."
        )

    return {
        "compliance_observations": compliance_observations,
        "security_risks": security_risks,
        "remediation_steps": remediation_steps,
    }
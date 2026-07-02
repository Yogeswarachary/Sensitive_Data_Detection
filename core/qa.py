# core/qa.py

from typing import List, Dict, Any

from .detector import aggregate_stats


def simple_text_summary(text: str, max_chars: int = 600) -> str:
    """
    Very simple non-AI summary:
    - Take the first max_chars characters of the text.
    - This is just a preview-style extract, not a semantic summary.
    """
    if not text:
        return "No text available to summarize."
    text = text.strip()
    if len(text) <= max_chars:
        return text
    return text[:max_chars] + "..."


def answer_question(
    question: str,
    text: str,
    findings: List[Dict[str, Any]],
    risk_info: Dict[str, str],
) -> str:
    """
    Rule-based question answering over the document.

    Supports questions like:
    - 'What sensitive data exists in the document?'
    - 'How many email addresses are present?'
    - 'Summarize this document.'
    - 'What compliance risks are identified?'
    """
    q = question.lower().strip()
    stats = aggregate_stats(findings)

    # If there is no text or findings, handle early
    if not text:
        return "No document text available to answer questions."

    # 1. 'Summarize this document.'
    if "summarize" in q:
        return simple_text_summary(text)

    # 2. 'What sensitive data exists in the document?'
    if "what sensitive data" in q or "what pii" in q:
        if not stats:
            return "No sensitive data types were detected by the current rules."
        parts = []
        for pii_type, count in stats.items():
            parts.append(f"{pii_type}: {count}")
        return "Detected sensitive data types and counts: " + ", ".join(parts)

    # 3. 'How many <type> are present?'
    if "how many" in q:
        # Check for each known type keyword
        if "email" in q:
            count = stats.get("email", 0)
            return f"There are {count} email address(es) detected in the document."
        if "phone" in q or "mobile" in q:
            count = stats.get("phone", 0)
            return f"There are {count} phone/mobile number(s) detected in the document."
        if "aadhaar" in q:
            count = stats.get("aadhaar", 0)
            return f"There are {count} Aadhaar number(s) detected in the document."
        if "pan" in q:
            count = stats.get("pan", 0)
            return f"There are {count} PAN number(s) detected in the document."
        if "credit card" in q or "card" in q:
            count = stats.get("credit_card", 0)
            return f"There are {count} credit card number(s) detected in the document."
        if "upi" in q:
            count = stats.get("upi", 0)
            return f"There are {count} UPI id(s) detected in the document."
        if "ifsc" in q or "bank" in q:
            count = stats.get("ifsc", 0)
            return f"There are {count} IFSC/bank detail(s) detected in the document."
        if "api key" in q or "token" in q:
            count = stats.get("api_key_like", 0)
            return f"There are {count} API key/token-like value(s) detected in the document."
        if "employee" in q or "emp" in q:
            count = stats.get("employee_id", 0)
            return f"There are {count} employee id(s) detected in the document."

        # If 'how many' but no known keyword matched
        return "Please specify the data type, for example: 'How many email addresses are present?'"

    # 4. 'What compliance risks are identified?'
    if "compliance risk" in q or "compliance risks" in q or "risk" in q:
        risk_level = risk_info.get("risk_level", "Unknown")
        reason = risk_info.get("reason", "")
        return f"Overall risk level is {risk_level}. {reason}"

    # 5. Fallback: generic explanation of what we can answer
    return (
        "This rule-based assistant supports questions like:\n"
        "- 'What sensitive data exists in the document?'\n"
        "- 'How many email addresses are present?'\n"
        "- 'Summarize this document.'\n"
        "- 'What compliance risks are identified?'\n"
        "Please try asking one of these or include a specific data type in your question."
    )
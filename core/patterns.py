import re

# Regex patterns for different sensitive data types
# These are simplified and can be improved for more accuracy

PATTERNS = {
    'aadhaar': re.compile(
        r"\b\d{4}\s?\d{4}\s?\d{4}\b" # 12 Digits, written like 1234 5678 9012
    ),

    'pan': re.compile(
        r"\b[A-Z]{5}\d{4}[A-Z]\b" # PAN number format: 5 Letters 4 Digits and 1 Letter. eg: ABCDE1234F
    ),

    'email': re.compile(
        r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z/a-z]{2,}\b" # Email format
    ),

    'phone': re.compile(
        r"\b(?:\+91[-\s]?)?[6-9]\d{9}\b" # indian mobile number format
    ),

    'credit_card': re.compile(
        r"\b(?:\d[ -]*?){13, 19}\b" # 13-19 digits, allowing spaces/dashes
    ),

    'ifsc': re.compile(
        r'\b[A-Z]{4}0[A-Z0-9]{6}\b' # IFSC format 4 Letters and 0-6 Digits. eg: SBIN0001234
    ),

    'upi': re.compile(
        r"\b[a-zA-z0-9.\-_]{3,}@[a-zA-Z]{3,}\b" # UPI format: eg: username@bank
    ),

    'api_key_value': re.compile(
        r"\b(?:sk-[A-Za-z0-9]{32,}|api_key=[A-Za-z0-9]{32,})\b" # API Key format: eg: sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx or api_key=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    ),

    'employee_id': re.compile(
        r"\b(?:EMP|emp[-_]?\d{3, 6}\b)" #Emp123, EMP-001234
    ),

    "confidential_keywords": re.compile(
        r"\b(confidential|proprietary|internal use only|do not distribute|nda)\b",
    re.IGNORECASE,
    ), # Business sensitivity indicators
}
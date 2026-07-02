from typing import List, Dict, Any

from .patterns import PATTERNS

def detect_pii(text: str) -> List[Dict[str, Any]]:
    """
    Run all regex patterns over the given text and return a list of findings.
    
    Each finding is a dict:
    {
        "type": "email" | "aadhaar" | ...,
        "value": matched string,
        "start": start_index_in_text,
        "end": end_index_in_text,
    }
    """
    findings: List[Dict[str, Any]] = []

    # Loop Through each pattern type and find matches in the text
    for pii_type, pattern in PATTERNS.items():
        # pattern.finditer(text) returns an iterator of match objects

        for match in pattern.finditer(text):
            finding = {
                "type": pii_type,
                "value": match.group(0),
                "start": match.start(),
                "end": match.end(),
            }

            findings.append(finding)
        
        return findings
    
def aggregate_stats(findings: List[Dict[str, Any]]) -> Dict[str, int]:
    """
    Count how many times each PII type appears in the Findings.
    Return a dict like:
    {
    "email": 10,
    "aadhaar: 2,
    ....
    }
    """
    counts: dict[str, int] = {}

    for finding in findings:
        t = finding["type"]
        if t not in counts:
            counts[t] = 0
        counts[t] += 1

    return counts
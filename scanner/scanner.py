import re

RULES = [
    ("HIGH", "Hardcoded secret", r"(password|api_key|secret)\s*=\s*['\"][^'\"]+['\"]"),
    ("HIGH", "Dangerous eval()", r"\beval\s*\("),
    ("MEDIUM", "Debug mode enabled", r"\bdebug\s*=\s*True\b"),
    ("MEDIUM", "Weak MD5 hashing", r"\bmd5\s*\("),
]


def scan_code(code):
    findings = []

    for line_no, line in enumerate(code.splitlines(), 1):
        for severity, name, pattern in RULES:
            if re.search(pattern, line, re.IGNORECASE):
                findings.append({
                    "line": line_no,
                    "severity": severity,
                    "issue": name
                })

    return findings
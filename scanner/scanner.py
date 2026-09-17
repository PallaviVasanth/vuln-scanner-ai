import re
import sys

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


def main():
    if len(sys.argv) != 2:
        print("Usage: python -m scanner.scanner <file>")
        return

    with open(sys.argv[1], encoding="utf-8") as file:
        findings = scan_code(file.read())

    for finding in findings:
        print(
            f"{finding['severity']:<7} "
            f"Line {finding['line']:<3} "
            f"{finding['issue']}"
        )

    print(f"\n{len(findings)} finding(s) detected.")


if __name__ == "__main__":
    main()
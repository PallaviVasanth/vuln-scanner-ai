\# vuln-scanner-ai



AI-assisted vulnerability scanning and security analysis toolkit for Python applications.



\## Overview



\*\*vuln-scanner-ai\*\* is a lightweight Python security analysis tool that identifies common insecure coding patterns in Python source code.



The project provides fast, understandable security feedback by detecting potentially dangerous coding practices and reporting each finding with:



\- Line number

\- Vulnerability type

\- Severity level

\- Number of findings detected



The project is designed as a developer-focused security analysis toolkit that can be extended with additional vulnerability rules, reporting formats, and AI-assisted analysis.



\## Features



\- Hardcoded secret detection

\- Dangerous `eval()` detection

\- Debug mode detection

\- Weak MD5 hashing detection

\- Severity classification

\- Line-level vulnerability findings

\- Command-line scanning

\- Python API for programmatic scanning

\- Automated test suite

\- GitHub Actions continuous integration

\- Security policy

\- Contribution guidelines



\## Detected Vulnerabilities



The current scanner detects the following patterns:



| Vulnerability | Severity |

|---|---|

| Hardcoded secrets | HIGH |

| Dangerous `eval()` usage | HIGH |

| Debug mode enabled | MEDIUM |

| Weak MD5 hashing | MEDIUM |



The scanner is rule-based at the current stage. Additional security rules and AI-assisted analysis are planned for future releases.



\## Installation



Clone the repository:



```bash

git clone https://github.com/PallaviVasanth/vuln-scanner-ai.git

cd vuln-scanner-ai


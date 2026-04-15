import os
import re

VULNERABILITIES = {
    "SQL Injection": r"SELECT .* \+|f\"SELECT|\"SELECT .*\" \+",
    "Command Injection": r"os\.system|subprocess",
    "Hardcoded Secrets": r"password\s*=\s*['\"]",
}

def scan_file(filepath):
    findings = []
    with open(filepath, "r", errors="ignore") as file:
        content = file.read()

        for vuln, pattern in VULNERABILITIES.items():
            if re.search(pattern, content):
                findings.append(vuln)

    return findings

def scan_directory(path):
    report = {}
    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(".py"):
                full_path = os.path.join(root, file)
                report[full_path] = scan_file(full_path)

    return report

if __name__ == "__main__":
    results = scan_directory("../samples")
    for file, vulns in results.items():
        if vulns:
            print(f"[!] {file} -> {vulns}")
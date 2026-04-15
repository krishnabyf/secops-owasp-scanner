import os
import re
import json
from datetime import datetime

VULNERABILITIES = {
    "SQL Injection": r"SELECT .* \+|f\"SELECT|\"SELECT .*\" \+",
    "Command Injection": r"os\.system|subprocess",
    "Hardcoded Secrets": r"password\s*=\s*['\"]",
    "Insecure Deserialization": r"pickle\.loads"
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
                vulns = scan_file(full_path)

                if vulns:
                    report[full_path] = vulns

    return report

def generate_report(results):
    report_data = {
        "scan_time": str(datetime.now()),
        "summary": {
            "total_vulnerable_files": len(results),
            "total_issues": sum(len(v) for v in results.values())
        },
        "details": results
    }

    os.makedirs("reports", exist_ok=True)

    with open("reports/report.json", "w") as f:
        json.dump(report_data, f, indent=4)

    print("\n[+] Scan Completed")
    print(f"[+] Vulnerable Files: {report_data['summary']['total_vulnerable_files']}")
    print(f"[+] Total Issues Found: {report_data['summary']['total_issues']}")
    print("[+] Report saved to reports/report.json\n")

if __name__ == "__main__":
    print("[*] Starting SecOps Scan...\n")

    results = scan_directory("samples")

    for file, vulns in results.items():
        print(f"[!] {file}")
        for v in vulns:
            print(f"    - {v}")

    generate_report(results)
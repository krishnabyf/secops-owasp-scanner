import json
from scanner.scanner import scan_directory

results = scan_directory("../samples")

with open("../reports/report.json", "w") as f:
    json.dump(results, f, indent=4)

print("[+] Report generated at reports/report.json")
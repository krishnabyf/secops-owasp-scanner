# SecOps OWASP Scanner

A compact static-analysis portfolio project that demonstrates security-rule design,
automated findings, JSON reporting, regression tests, and CI evidence.

## Current Coverage

- SQL injection patterns
- Command execution risks
- Hardcoded password patterns
- Insecure Python deserialization

This is an educational scanner, not a replacement for Semgrep, CodeQL, Bandit, or a
professional application-security assessment.

## Run

```bash
python3 scanner/scanner.py
cat reports/report.json
```

To use findings as a policy gate:

```bash
python3 scanner/scanner.py --fail-on-findings
```

## Test

```bash
python3 -m unittest discover -s tests -v
```

The GitHub Actions workflow treats findings in the intentionally vulnerable sample as
successful detection evidence, uploads the JSON report, and fails only when the scanner or
tests are broken.

## License

MIT

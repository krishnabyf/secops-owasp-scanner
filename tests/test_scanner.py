import tempfile
import unittest
from pathlib import Path

from scanner.scanner import scan_directory, scan_file


class ScannerTests(unittest.TestCase):
    def test_detects_expected_sample_findings(self):
        findings = scan_directory("samples")
        issue_count = sum(len(items) for items in findings.values())

        self.assertGreater(issue_count, 0)
        self.assertTrue(any("SQL Injection" in items for items in findings.values()))

    def test_clean_file_has_no_findings(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "safe.py"
            path.write_text("def add(left, right):\n    return left + right\n", encoding="utf-8")

            self.assertEqual(scan_file(path), [])


if __name__ == "__main__":
    unittest.main()

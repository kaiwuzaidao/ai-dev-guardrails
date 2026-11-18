"""Exercise the same process and fields that the downstream reader uses."""

import json
from pathlib import Path
import subprocess
import sys
import unittest


def run_report(input_text):
    command = [sys.executable, str(Path(__file__).with_name("report.py"))]
    result = subprocess.run(
        command, input=input_text, text=True, capture_output=True, check=True
    )
    return json.loads(result.stdout)


class ExportContractTest(unittest.TestCase):
    def test_existing_reader_can_match_original_identifiers(self):
        records = run_report("007\nA-19\n")
        self.assertEqual([record["id"] for record in records], ["007", "A-19"])

    def test_empty_export_is_an_empty_array(self):
        self.assertEqual(run_report(""), [])


if __name__ == "__main__":
    unittest.main()

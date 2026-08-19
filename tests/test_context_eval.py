import copy
import importlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "evals" / "forward"
CONTRACT = ROOT / "evals" / "context-v3-contract.json"
VALID_RECORD = ROOT / "tests" / "fixtures" / "context_eval" / "valid_run_record.json"

try:
    context_eval = importlib.import_module("scripts.context_eval")
except ModuleNotFoundError:
    context_eval = None


class ForwardPackTests(unittest.TestCase):
    def require_runner(self):
        self.assertIsNotNone(context_eval, "scripts/context_eval.py not implemented")
        return context_eval

    def test_pack_has_five_valid_synthetic_pseudonymized_cases(self):
        runner = self.require_runner()
        self.assertEqual(runner.check_pack(PACK), [])
        self.assertEqual([case["id"] for case in runner.list_cases(PACK)], ["01", "02", "03", "04", "05"])

    def test_pack_rejects_manifest_claiming_real_pii(self):
        runner = self.require_runner()
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "forward"
            runner.copy_pack(PACK, target)
            path = target / "cases" / "01" / "manifest.json"
            manifest = json.loads(path.read_text(encoding="utf-8"))
            manifest["contains_real_pii"] = True
            path.write_text(json.dumps(manifest), encoding="utf-8")
            self.assertIn("case_privacy", {issue.code for issue in runner.check_pack(target)})

    def test_pack_checks_writing_sample_hashes(self):
        runner = self.require_runner()
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "forward"
            runner.copy_pack(PACK, target)
            path = target / "cases" / "01" / "input.json"
            data = json.loads(path.read_text(encoding="utf-8"))
            data["materials"][0]["text"] += " muudetud"
            path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
            self.assertIn("sample_hash", {issue.code for issue in runner.check_pack(target)})

    def test_human_rubric_encodes_two_horizons_and_hard_gates(self):
        runner = self.require_runner()
        self.assertEqual(runner.check_rubric(PACK), [])
        rubric = json.loads((PACK / "human-rubric.json").read_text(encoding="utf-8"))
        self.assertEqual(rubric["hard_gates"]["fabricated_facts"], 0)
        self.assertEqual(rubric["hard_gates"]["restricted_leaks"], 0)
        self.assertEqual(rubric["horizons"]["first_usable_result"]["window_minutes"], {"min": 30, "max": 40})
        self.assertEqual(rubric["horizons"]["learning_loop"]["users"], 3)
        self.assertEqual(rubric["horizons"]["learning_loop"]["real_tasks_per_user"], 5)
        self.assertEqual(rubric["horizons"]["learning_loop"]["duration_days"], 14)


class RunRecordTests(unittest.TestCase):
    def require_runner(self):
        self.assertIsNotNone(context_eval, "scripts/context_eval.py not implemented")
        return context_eval

    def test_valid_run_record_passes_pack_and_contract_invariants(self):
        runner = self.require_runner()
        self.assertEqual(runner.check_run_record(VALID_RECORD, PACK, CONTRACT), [])

    def test_run_record_rejects_fabricated_fact(self):
        runner = self.require_runner()
        record = json.loads(VALID_RECORD.read_text(encoding="utf-8"))
        record["results"]["fabricated_facts"] = 1
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "run.json"
            path.write_text(json.dumps(record), encoding="utf-8")
            self.assertIn("run_invariant", {issue.code for issue in runner.check_run_record(path, PACK, CONTRACT)})

    def test_cli_check_list_and_run_record(self):
        script = ROOT / "scripts" / "context_eval.py"
        commands = [
            [sys.executable, "-B", str(script), "--check", str(PACK)],
            [sys.executable, "-B", str(script), "--list", str(PACK)],
            [sys.executable, "-B", str(script), "--pack", str(PACK), "--contract", str(CONTRACT), "--run-record", str(VALID_RECORD)],
        ]
        results = [subprocess.run(command, cwd=ROOT, capture_output=True, text=True, check=False) for command in commands]
        self.assertEqual([result.returncode for result in results], [0, 0, 0])
        self.assertIn("01\tB2B teenus", results[1].stdout)


if __name__ == "__main__":
    unittest.main()

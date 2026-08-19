import hashlib
import importlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "render_quick_interview.py"
CONTRACT_PATH = ROOT / "evals" / "context-v3-contract.json"
SOURCE_PATHS = (
    "skills/konteksti-looja/SKILL.md",
    "skills/konteksti-looja/references/quick-mode.md",
    "skills/konteksti-looja/references/interview-engine.md",
    "skills/konteksti-looja/references/claims-and-evidence.md",
    "skills/konteksti-looja/references/output-contract.md",
)

try:
    renderer = importlib.import_module("scripts.render_quick_interview")
except ModuleNotFoundError:
    renderer = None


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


class RenderQuickInterviewTests(unittest.TestCase):
    def require_renderer(self):
        self.assertIsNotNone(renderer, "scripts/render_quick_interview.py not implemented")
        return renderer

    def stage_sources(self, destination):
        for relative in SOURCE_PATHS:
            target = destination / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / relative, target)
        contract_target = destination / "evals" / "context-v3-contract.json"
        contract_target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(CONTRACT_PATH, contract_target)

    def publish_staged_hash(self, destination, digest):
        path = destination / "evals" / "context-v3-contract.json"
        contract = json.loads(path.read_text(encoding="utf-8"))
        contract["frozen_quick"]["published_sha256"] = digest
        path.write_text(json.dumps(contract, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    def test_render_is_deterministic_self_contained_and_excludes_deep_mode(self):
        subject = self.require_renderer()
        first = subject.render_artifact(ROOT)
        second = subject.render_artifact(ROOT)
        self.assertEqual(first, second)
        text = first.decode("utf-8")
        self.assertTrue(text.startswith("# Kiire konteksti-intervjuu\n\n## Kasutamine\n"))
        self.assertIn("Kopeeri kogu see fail", text)
        for relative in SOURCE_PATHS[1:]:
            self.assertIn(f"<!-- source: {relative} -->", text)
        for heading in ("# Kiire režiim", "# Intervjuumootor", "# Väited, tõendid ja kandidaadid", "# Väljundleping"):
            self.assertIn(heading, text)
        for marker in ("<!-- quick-output: identity.md -->", "<!-- quick-max-user-answers-after-import: 10 -->", "<!-- section: samples | owner: D -->"):
            self.assertIn(marker, text)
        self.assertIn("## Alati kehtiv", text)
        self.assertIn("## Eesti keele stiil", text)
        self.assertNotIn("<!-- source: skills/konteksti-looja/references/deep-mode.md -->", text)
        self.assertNotIn("### Moodul A: töö-tegelikkus", text)

    def test_render_has_no_external_reference_dependencies(self):
        subject = self.require_renderer()
        text = subject.render_artifact(ROOT).decode("utf-8")
        reference_names = "quick-mode|interview-engine|claims-and-evidence|output-contract|deep-mode"
        dead_link = rf"\[[^\]]+\]\([^)]*(?:{reference_names})\.md[^)]*\)"
        external_instruction = rf"(?im)^.*\b(?:loe|ava)\b[^\n]*(?:reference|(?:{reference_names})\.md).*$"
        self.assertIsNone(re.search(dead_link, text))
        self.assertIsNone(re.search(external_instruction, text))
        self.assertNotIn("scripts/context_v3_check.py", text)
        self.assertNotIn("Loe vajalik reference", text)

    def test_cross_references_and_missing_deep_rules_have_inline_fallbacks(self):
        subject = self.require_renderer()
        text = subject.render_artifact(ROOT).decode("utf-8")
        for internal_reference in (
            "allpool osa „Intervjuumootor“ §4",
            "allpool osa „Väited, tõendid ja kandidaadid“ §3",
            "allpool osa „Väljundleping“ §4",
        ):
            self.assertIn(internal_reference, text)
        self.assertIn("See null-install artefakt rakendab ainult kiiret režiimi", text)
        self.assertIn("Null-installis pole süva omandiregistrit kaasas", text)
        self.assertIn("täielik ankruskelett ainult §4", text)
        self.assertIn("`target_section` väärtuseks `määramata`", text)

    def test_manifest_hashes_exact_artifact_bytes_and_all_sources(self):
        subject = self.require_renderer()
        artifact = subject.render_artifact(ROOT)
        manifest = subject.build_manifest(ROOT, artifact)
        self.assertEqual(manifest["path"], "quick-interview.md")
        self.assertEqual(manifest["algorithm"], "sha256")
        self.assertEqual(manifest["sha256"], sha256_bytes(artifact))
        self.assertEqual(manifest["generated_on"], "2026-08-19")
        self.assertEqual([item["path"] for item in manifest["sources"]], list(SOURCE_PATHS))
        for item in manifest["sources"]:
            self.assertEqual(item["sha256"], sha256_bytes((ROOT / item["path"]).read_bytes()))

    def test_write_then_check_and_detect_artifact_or_source_drift(self):
        subject = self.require_renderer()
        with tempfile.TemporaryDirectory() as directory:
            staged = Path(directory)
            self.stage_sources(staged)
            manifest = subject.write_artifact(staged)
            self.publish_staged_hash(staged, manifest["sha256"])
            self.assertEqual(subject.check_artifact(staged), [])

            artifact_path = staged / "quick-interview.md"
            artifact_path.write_bytes(artifact_path.read_bytes() + b"drift\n")
            self.assertIn("artifact_drift", {item.code for item in subject.check_artifact(staged)})

            subject.write_artifact(staged)
            source_path = staged / SOURCE_PATHS[1]
            source_path.write_bytes(source_path.read_bytes() + b"source drift\n")
            self.assertIn("source_drift", {item.code for item in subject.check_artifact(staged)})

    def test_checked_in_artifact_manifest_and_contract_share_published_hash(self):
        subject = self.require_renderer()
        self.assertEqual(subject.check_artifact(ROOT), [])
        artifact = (ROOT / "quick-interview.md").read_bytes()
        manifest = json.loads((ROOT / "evals" / "frozen-quick.json").read_text(encoding="utf-8"))
        contract = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))
        digest = sha256_bytes(artifact)
        self.assertEqual(manifest["sha256"], digest)
        self.assertEqual(contract["frozen_quick"]["published_sha256"], digest)

    def test_cli_requires_explicit_write_and_check_passes(self):
        self.require_renderer()
        check = subprocess.run(
            [sys.executable, "-B", str(SCRIPT), "--check", "--repo", str(ROOT)],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        no_action = subprocess.run(
            [sys.executable, "-B", str(SCRIPT), "--repo", str(ROOT)],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(check.returncode, 0, check.stdout + check.stderr)
        self.assertNotEqual(no_action.returncode, 0)
        self.assertIn("--write", no_action.stderr)


if __name__ == "__main__":
    unittest.main()

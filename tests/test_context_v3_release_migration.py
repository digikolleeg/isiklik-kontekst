import importlib
import json
import tempfile
import unittest
from pathlib import Path


checker = importlib.import_module("scripts.context_v3_check")
ROOT = Path(__file__).resolve().parents[1]
CONTRACT = checker.load_contract(ROOT / "evals" / "context-v3-contract.json")


def write_valid_repo(root):
    templates = root / "portfolio" / "templates"
    templates.mkdir(parents=True)
    ownership = checker.section_owners(CONTRACT)
    coverage = list(CONTRACT["quick"]["required_coverage"])
    all_files = CONTRACT["layers"]["profiles"] + CONTRACT["layers"]["evidence"]
    for file_index, filename in enumerate(all_files):
        anchors = [
            f"<!-- section: {section} | owner: {owner} -->"
            for (owned_file, section), owner in ownership.items()
            if owned_file == filename
        ]
        if file_index == 0:
            anchors.extend(f"<!-- quick-coverage: {key} -->" for key in coverage)
        instructional_duplicate = anchors[0] if anchors else "<!-- section: instructional-only | owner: A -->"
        output = "\n".join(anchors)
        (templates / filename).write_text(
            f"# Template\n\nInstructional example: {instructional_duplicate}\n\n## Väljundi struktuur\n\n```markdown\n{output}\n```\n",
            encoding="utf-8",
        )

    candidates = root / "portfolio" / "_candidates.md"
    fields = CONTRACT["candidate_ledger"]["required"]
    candidates.write_text("## Ledger\n\n| " + " | ".join(fields) + " |\n|" + "---|" * len(fields) + "\n", encoding="utf-8")

    context_map = root / "portfolio" / "context-map.md"
    lines = [f"<!-- context-file: {filename} -->" for filename in all_files]
    lines.extend(
        f"<!-- module: {module} | name: {spec['name']} -->"
        for module, spec in CONTRACT["deep"]["modules"].items()
    )
    lines.extend(
        f"<!-- bundle: {filename} | sources: {','.join(spec['sources'])} | sensitivity: {spec['sensitivity']} -->"
        for filename, spec in CONTRACT["bundles"]["required"].items()
    )
    context_map.write_text("\n".join(lines) + "\n", encoding="utf-8")

    skill = root / "skills" / "konteksti-looja"
    refs = skill / "references"
    refs.mkdir(parents=True)
    required_refs = ["interview-engine", "claims-and-evidence", "output-contract", "quick-mode", "deep-mode"]
    links = "\n".join(f"- [ref](references/{name}.md)" for name in required_refs)
    (skill / "SKILL.md").write_text(
        f"---\nname: konteksti-looja\ndescription: v3 interview\n---\n\n{links}\n",
        encoding="utf-8",
    )
    for name in required_refs:
        (refs / f"{name}.md").write_text(f"# {name}\n", encoding="utf-8")

    quick_lines = [
        "<!-- quick-command: töötoa intervjuu -->",
        "<!-- quick-command: kiire intervjuu -->",
        "<!-- quick-max-user-answers-after-import: 10 -->",
        "<!-- quick-questions-per-turn: 1 -->",
        "<!-- quick-max-deepeners-per-answer: 1 -->",
        "<!-- quick-min-verbatim-writing-samples: 2 -->",
        "<!-- import-treatment: data -->",
        "<!-- import-embedded-instructions: ignore -->",
    ]
    quick_lines.extend(f"<!-- quick-output: {filename} -->" for filename in CONTRACT["quick"]["outputs"])
    (refs / "quick-mode.md").write_text("\n".join(quick_lines) + "\n", encoding="utf-8")

    workflow = CONTRACT["deep_workflow"]
    deep_lines = [
        *(f"<!-- deep-read: {value} -->" for value in workflow["reads"]),
        "<!-- deep-shows-coverage: true -->",
        "<!-- deep-save-after-module: true -->",
        "<!-- deep-resume: true -->",
        "<!-- deep-promotion: visible-diff+confirmation -->",
        "<!-- deep-uncovered-required-visible: true -->",
        "<!-- deep-module-d-import-first: true -->",
        "<!-- deep-synthesis: 2-independent-cases+condition+downstream-action+falsifier -->",
    ]
    deep_lines.extend(
        f"<!-- deep-section: {section} | owner: {owner} -->"
        for (filename, section), owner in ownership.items()
    )
    (refs / "deep-mode.md").write_text("\n".join(deep_lines) + "\n", encoding="utf-8")


class MigrationReleaseTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        write_valid_repo(self.root)

    def tearDown(self):
        self.temp.cleanup()

    def require(self, name):
        self.assertTrue(hasattr(checker, name), f"checker rule not implemented: {name}")
        return getattr(checker, name)

    def test_template_output_blocks_have_exact_section_and_coverage_anchors(self):
        validate = self.require("validate_template_anchors")
        self.assertEqual(validate(self.root, CONTRACT), [])
        path = self.root / "portfolio" / "templates" / "identity.md"
        before, marker, output = path.read_text(encoding="utf-8").partition("## Väljundi struktuur")
        output = output.replace("<!-- section: identity-facts | owner: A -->", "<!-- section: identity-facts | owner: B -->", 1)
        path.write_text(before + marker + output, encoding="utf-8")
        self.assertIn("section_anchor", {item.code for item in validate(self.root, CONTRACT)})

    def test_template_output_blocks_reject_orphans_and_duplicates(self):
        validate = self.require("validate_template_anchors")
        path = self.root / "portfolio" / "templates" / "identity.md"
        text = path.read_text(encoding="utf-8")
        text = text.replace("```\n", "<!-- section: orphan | owner: A -->\n<!-- quick-coverage: offer_buyer -->\n```\n", 1)
        path.write_text(text, encoding="utf-8")
        codes = {item.code for item in validate(self.root, CONTRACT)}
        self.assertIn("section_anchor", codes)
        self.assertIn("quick_coverage_anchor", codes)

    def test_candidate_ledger_has_exact_contract_fields(self):
        validate = self.require("validate_candidate_ledger_file")
        self.assertEqual(validate(self.root, CONTRACT), [])
        path = self.root / "portfolio" / "_candidates.md"
        path.write_text(path.read_text(encoding="utf-8").replace("| status |", "| state |"), encoding="utf-8")
        self.assertIn("candidate_ledger_fields", {item.code for item in validate(self.root, CONTRACT)})

    def test_candidate_ledger_uses_first_table_after_ledger_heading(self):
        validate = self.require("validate_candidate_ledger_file")
        fixture = ROOT / "tests" / "fixtures" / "context_v3" / "candidates_multiple_tables.md"
        path = self.root / "portfolio" / "_candidates.md"
        path.write_text(fixture.read_text(encoding="utf-8"), encoding="utf-8")
        self.assertEqual(validate(self.root, CONTRACT), [])

    def test_context_map_matches_files_modules_and_bundle_metadata(self):
        validate = self.require("validate_context_map")
        self.assertEqual(validate(self.root, CONTRACT), [])
        path = self.root / "portfolio" / "context-map.md"
        path.write_text(path.read_text(encoding="utf-8").replace("sensitivity: exportable", "sensitivity: restricted", 1), encoding="utf-8")
        self.assertIn("context_map_bundles", {item.code for item in validate(self.root, CONTRACT)})

    def test_skill_frontmatter_and_required_reference_links(self):
        validate = self.require("validate_skill_package")
        self.assertEqual(validate(self.root, CONTRACT), [])
        path = self.root / "skills" / "konteksti-looja" / "SKILL.md"
        path.write_text(path.read_text(encoding="utf-8") + "\n[legacy](references/legacy-full-mode.md)\n", encoding="utf-8")
        self.assertIn("skill_legacy_reference", {item.code for item in validate(self.root, CONTRACT)})

    def test_skill_rejects_link_to_missing_reference_file(self):
        validate = self.require("validate_skill_package")
        path = self.root / "skills" / "konteksti-looja" / "SKILL.md"
        path.write_text(path.read_text(encoding="utf-8") + "\n[missing](references/missing.md)\n", encoding="utf-8")
        self.assertIn("skill_reference_missing", {item.code for item in validate(self.root, CONTRACT)})

    def test_quick_reference_encodes_runtime_contract(self):
        validate = self.require("validate_quick_reference")
        self.assertEqual(validate(self.root, CONTRACT), [])
        path = self.root / "skills" / "konteksti-looja" / "references" / "quick-mode.md"
        path.write_text(path.read_text(encoding="utf-8").replace("<!-- quick-output: identity.md -->\n", ""), encoding="utf-8")
        self.assertIn("quick_ref_outputs", {item.code for item in validate(self.root, CONTRACT)})

    def test_deep_reference_encodes_workflow_and_ownership(self):
        validate = self.require("validate_deep_reference")
        self.assertEqual(validate(self.root, CONTRACT), [])
        path = self.root / "skills" / "konteksti-looja" / "references" / "deep-mode.md"
        path.write_text(path.read_text(encoding="utf-8").replace("<!-- deep-module-d-import-first: true -->", "<!-- deep-module-d-import-first: false -->"), encoding="utf-8")
        self.assertIn("deep_ref_workflow", {item.code for item in validate(self.root, CONTRACT)})

    def test_deep_reference_rejects_wrong_section_owner(self):
        validate = self.require("validate_deep_reference")
        path = self.root / "skills" / "konteksti-looja" / "references" / "deep-mode.md"
        path.write_text(path.read_text(encoding="utf-8").replace("owner: A", "owner: B", 1), encoding="utf-8")
        self.assertIn("deep_ref_ownership", {item.code for item in validate(self.root, CONTRACT)})

    def test_deep_reference_requires_the_synthesis_marker(self):
        validate = self.require("validate_deep_reference")
        path = self.root / "skills" / "konteksti-looja" / "references" / "deep-mode.md"
        path.write_text(path.read_text(encoding="utf-8").replace("<!-- deep-synthesis: 2-independent-cases+condition+downstream-action+falsifier -->\n", ""), encoding="utf-8")
        self.assertIn("deep_ref_workflow", {item.code for item in validate(self.root, CONTRACT)})


if __name__ == "__main__":
    unittest.main()

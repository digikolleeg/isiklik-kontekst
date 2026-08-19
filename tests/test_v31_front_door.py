"""v3.1 contract tests: two front doors, sales-first quick flow, generic expand mode."""
import json
import re
import subprocess
import sys
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SKILL = REPO / "skills" / "konteksti-looja" / "SKILL.md"
REFS = REPO / "skills" / "konteksti-looja" / "references"
QUICK = REFS / "quick-mode.md"
ENGINE = REFS / "interview-engine.md"
OUTPUT = REFS / "output-contract.md"
EXPAND = REFS / "expand-mode.md"
CONTRACT = REPO / "evals" / "context-v3-contract.json"


def _section(text, heading):
    start = text.index(heading)
    nxt = re.search(r"(?m)^## ", text[start + len(heading):])
    return text[start:start + len(heading) + (nxt.start() if nxt else len(text))]


class TwoFrontDoors(unittest.TestCase):
    def setUp(self):
        self.text = SKILL.read_text(encoding="utf-8")
        self.modes = _section(self.text, "## Režiimid")

    def test_renderer_headings_are_untouched(self):
        for heading in ("# Konteksti-looja", "## Režiimid", "## Kontekstikaust",
                        "## Alati kehtiv", "## Süvarežiim", "## Eesti keele stiil", "## Reference'id"):
            self.assertIn(heading, self.text, heading)

    def test_modes_table_names_both_front_doors(self):
        self.assertIn("müügiagent", self.modes)
        self.assertIn("muu töö või agent", self.modes)
        self.assertIn("quick-mode.md", self.modes)
        self.assertIn("expand-mode.md", self.modes)

    def test_exact_extension_command_routes_to_generic_expand_mode(self):
        self.assertIn('"laienda konteksti uue agendi jaoks"', self.modes)
        self.assertIn("laienda konteksti uue agendi jaoks", self.text.split("---", 2)[1])

    def test_choice_dialog_offers_exactly_two_paths_without_deep(self):
        start = self.modes.index("### Valiku küsimine")
        dialog = self.modes[start:]
        offered = re.findall(r"(?m)^> \*\*\*(.+?)\*\*", dialog)
        self.assertEqual(2, len(offered), f"choice dialog must offer exactly two paths, got {offered}")
        self.assertNotIn("Süva", dialog)
        self.assertNotIn("süvaintervjuu", dialog)

    def test_always_applies_rules_are_mode_aware_about_asking_for_the_work(self):
        rules = _section(self.text, "## Alati kehtiv")
        self.assertIn("Ava tööga", rules)
        self.assertIn("aktiivse režiimi juhis", rules)
        self.assertIn("Ära lisa sellele oma avaküsimust", rules)
        self.assertNotIn(
            '"millise päris korduva töö tahad sellele agendile anda?"', rules,
            "the unconditional work question must not remain an always-applies rule")
        self.assertNotIn("Muu töö või agent", rules)

    def test_deep_stays_a_power_command_in_the_table(self):
        self.assertRegex(self.modes, r'\|\s*"süvaintervjuu"\s*\|')

    def test_references_index_links_expand_mode(self):
        refs = _section(self.text, "## Reference'id")
        self.assertIn("expand-mode.md", refs)

    def test_expand_mode_is_not_named_in_rendered_sections(self):
        rendered = _section(self.text, "## Kontekstikaust") + _section(self.text, "## Alati kehtiv")
        self.assertNotIn("expand-mode", rendered)


class SalesFirstQuickFlow(unittest.TestCase):
    def setUp(self):
        self.text = QUICK.read_text(encoding="utf-8")
        self.flow = _section(self.text, "## 3. Voog")

    def test_static_markers_match_contract(self):
        contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
        for command in contract["quick"]["commands"]:
            self.assertIn(f"<!-- quick-command: {command} -->", self.text)
        for output in contract["quick"]["outputs"]:
            self.assertIn(f"<!-- quick-output: {output} -->", self.text)

    def test_flow_does_not_ask_which_work_to_delegate(self):
        self.assertNotIn("Millise päris korduva töö tahad sellele agendile anda?", self.flow)

    def test_flow_is_framed_as_the_sales_agent(self):
        self.assertIn("müügiagent", self.flow.lower())

    def test_import_comes_before_the_first_substantive_question(self):
        self.assertLess(self.flow.index("import".capitalize()) if "Import" in self.flow else self.flow.index("import"),
                        self.flow.index("Adaptiivsed küsimused"))
        self.assertIn("<!-- quick-import-first: true -->", self.text)

    def test_privacy_guidance_precedes_material_entry(self):
        self.assertIn("<!-- quick-privacy-before-import: true -->", self.text)
        privacy_at = self.text.index("quick-privacy-before-import")
        self.assertLess(privacy_at, self.text.index("## 4."))
        for example in ("[kliendi tegevjuht]", "[üks e-pood]", "[neljakohaline summa]"):
            self.assertIn(example, self.text, example)
        for removal in ("e-post", "telefon", "isikukood", "lepingutingimus"):
            self.assertIn(removal, self.text.lower(), removal)

    def test_samples_have_a_minimum_but_no_upper_bound(self):
        self.assertIn("<!-- quick-min-verbatim-writing-samples: 2 -->", self.text)
        self.assertIn("<!-- quick-max-verbatim-writing-samples: none -->", self.text)

    def test_samples_pasted_in_one_message_cost_one_answer(self):
        self.assertIn("<!-- quick-samples-one-message-one-answer: true -->", self.text)

    def test_questions_are_adaptive_not_a_fixed_seven_to_nine(self):
        self.assertNotIn("7 baasküsimust", self.flow)
        self.assertIn("<!-- quick-adaptive-questions: true -->", self.text)

    def test_soft_checkpoint_once_minimum_coverage_is_reached(self):
        self.assertIn("<!-- quick-soft-checkpoint: minimum-coverage -->", self.text)
        self.assertIn("<!-- quick-soft-checkpoint-after-user-answers: 10 -->", self.text)
        self.assertNotIn("quick-max-user-answers-after-import", self.text)

    def test_output_is_still_exactly_four_markdown_files(self):
        invariants = _section(self.text, "## 5. Invariandid sessiooni lõpus")
        self.assertIn("täpselt neli", invariants)

    def test_interviewer_may_help_compare_options_and_confirm_a_working_choice(self):
        self.assertIn("Valikuabi", self.flow)
        self.assertIn("tööhüpotees", self.flow)
        self.assertIn("Kas paneme selle praegu valikuna kirja?", self.flow)

    def test_uncertain_register_is_not_hardened_without_confirmation(self):
        engine = ENGINE.read_text(encoding="utf-8")
        self.assertIn("Kui kasutaja kõhkleb", engine)
        self.assertIn("ei muuda seda kõvaks reegliks", engine)

    def test_manual_fallback_labels_exact_filenames_and_protects_nested_fences(self):
        output = OUTPUT.read_text(encoding="utf-8")
        for filename in ("identity.md", "current-projects.md", "communication-style.md", "writing-samples.md"):
            self.assertIn(f"FAILINIMI: {filename}", output)
        self.assertIn("nelja tagasirõhuga", output)


class GenericExpandMode(unittest.TestCase):
    def setUp(self):
        self.assertTrue(EXPAND.is_file(), "expand-mode.md is missing")
        self.text = EXPAND.read_text(encoding="utf-8")

    def test_first_question_is_about_the_work(self):
        self.assertIn("<!-- expand-first-question: work -->", self.text)
        self.assertIn("Mis tööd see agent sinu eest teeb?", self.text)

    def test_reads_existing_context_and_candidate_ledger(self):
        self.assertIn("<!-- expand-read: existing-files -->", self.text)
        self.assertIn("<!-- expand-read: candidates -->", self.text)

    def test_maps_coverage_into_three_sets(self):
        for marker in ("olemas", "ebaselge", "puudu"):
            self.assertIn(f"<!-- expand-bucket: {marker} -->", self.text)

    def test_does_not_repeat_what_the_sales_path_already_answered(self):
        self.assertIn("<!-- expand-no-repeat: true -->", self.text)

    def test_produces_a_context_selection_projection_not_a_new_source(self):
        self.assertIn("<!-- expand-output: context-selection -->", self.text)
        self.assertIn("<!-- expand-creates-context-file: false -->", self.text)

    def test_never_writes_a_work_instruction(self):
        self.assertIn("<!-- expand-writes-work-instruction: false -->", self.text)

    def test_writes_only_candidates_and_empty_sections(self):
        self.assertIn("<!-- expand-write-scope: candidates+empty-sections -->", self.text)

    def test_agent_categories_are_not_hardcoded(self):
        lowered = self.text.lower()
        for hardcoded in ("sisulooja", "finants", "tugiagent", "klienditugi"):
            self.assertNotIn(hardcoded, lowered, hardcoded)


class RenderedArtifactStaysClean(unittest.TestCase):
    def test_expand_mode_never_leaks_into_the_zero_install_artifact(self):
        artifact = (REPO / "quick-interview.md").read_text(encoding="utf-8")
        self.assertNotIn("expand-mode", artifact)

    def test_zero_install_artifact_does_not_offer_the_other_front_door(self):
        artifact = (REPO / "quick-interview.md").read_text(encoding="utf-8")
        self.assertNotIn("Muu töö või agent", artifact)

    def test_render_check_passes(self):
        result = subprocess.run([sys.executable, "scripts/render_quick_interview.py", "--check"],
                                cwd=REPO, capture_output=True, text=True)
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "evals" / "context-v3-contract.json"
REFERENCE = ROOT / "skills" / "konteksti-looja" / "references" / "correction-loop.md"


class CorrectionLoopTests(unittest.TestCase):
    def test_contract_locks_one_paste_and_safe_classification(self):
        contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
        loop = contract["learning_loop"]
        self.assertEqual(loop["commands"], ["õpime parandusest", "siin on lõplik versioon"])
        self.assertEqual(
            loop["categories"],
            [
                "fact-correction",
                "general-style",
                "channel-style",
                "addressee-exception",
                "temporary-project-context",
            ],
        )
        self.assertTrue(loop["same_conversation_one_paste"])
        self.assertFalse(loop["automatic_promotion"])
        self.assertTrue(loop["visible_diff_and_confirmation"])
        self.assertTrue(loop["one_edit_event_is_one_source_family"])

    def test_skill_routes_to_a_self_contained_correction_reference(self):
        skill = (ROOT / "skills" / "konteksti-looja" / "SKILL.md").read_text(encoding="utf-8")
        reference = REFERENCE.read_text(encoding="utf-8")
        self.assertIn("references/correction-loop.md", skill)
        for marker in (
            "<!-- correction-same-conversation-one-paste: true -->",
            "<!-- correction-automatic-promotion: false -->",
            "<!-- correction-visible-diff-and-confirmation: true -->",
            "<!-- correction-one-event-one-source-family: true -->",
        ):
            self.assertIn(marker, reference)
        for category in json.loads(CONTRACT.read_text(encoding="utf-8"))["learning_loop"]["categories"]:
            self.assertIn(f"`{category}`", reference)

    def test_writing_bundles_ask_for_the_final_only_after_use(self):
        for filename in ("client-outreach.md", "content-writer.md"):
            text = (ROOT / "portfolio" / "bundles" / filename).read_text(encoding="utf-8")
            self.assertIn("Saatsid või avaldasid ära? Kleebi lõplik versioon", text)
            self.assertIn("Ära küsi lõppversiooni enne", text)


if __name__ == "__main__":
    unittest.main()

import copy
import hashlib
import importlib
import json
import tempfile
import unittest
from pathlib import Path


try:
    checker = importlib.import_module("scripts.context_v3_check")
except ModuleNotFoundError:
    class MissingChecker:
        def __getattr__(self, name):
            raise AssertionError(f"checker not implemented: {name}")

    checker = MissingChecker()


ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "tests" / "fixtures" / "context_v3"


def valid_contract():
    return {
        "version": "3.0.0",
        "baseline": {
            "head": "dea4a2c6f29c2e7561ed5c4f3b2f1069c99b0925",
            "root_index_sha256": "6adead52bc9e6b4357255a8c671addb8a2be654c1e25b86006d74edd55c152e6",
            "known_drift": ["quick-count-3-vs-4", "portfolio-count-10-vs-11"],
        },
        "layers": {
            "profiles": [
                "identity.md",
                "role-and-responsibilities.md",
                "current-projects.md",
                "team-and-relationships.md",
                "tools-and-systems.md",
                "communication-style.md",
                "goals-and-priorities.md",
                "preferences-and-constraints.md",
                "domain-knowledge.md",
            ],
            "evidence": ["writing-samples.md", "decision-log.md"],
        },
        "quick": {
            "commands": ["töötoa intervjuu", "kiire intervjuu"],
            "outputs": [
                "identity.md",
                "current-projects.md",
                "communication-style.md",
                "writing-samples.md",
            ],
            "max_user_answers_after_import": 10,
            "questions_per_turn": 1,
            "max_deepeners_per_answer": 1,
            "target_minutes": {"min": 30, "max": 40},
            "min_verbatim_writing_samples": 2,
            "owns_sections": [],
            "required_coverage": ["offer_buyer", "icp_sector_size_region", "problem_trigger", "credibility_evidence", "message_purpose_cta", "forbidden_claims", "channel_register_length", "forbidden_mannerisms", "real_samples"],
            "claim_policy": {"kinnitatud": "explicit-user-statement", "toetatud": "derived-pattern-with-2-independent-source-artifact-or-situation-families", "kandidaat": "single-observation-or-inference", "later_modification_owner": "deep-modules"}
        },
        "claims": {
            "statuses": ["kinnitatud", "toetatud", "kandidaat"],
            "supported_min_independent_evidence": 2,
            "evidence_id_format": "<source-artifact-or-situation>:<observation-id>",
            "independence_key": "source-artifact-or-situation",
            "confirmed_rule": "explicit-user-statement",
            "single_observation_status": "kandidaat",
            "generic_source_families_forbidden": ["email", "linkedin", "channel", "document", "message", "situation", "interview"],
        },
        "frontmatter": {
            "required": ["updated", "review_after", "sensitivity"],
            "sensitivity_values": ["exportable", "restricted"],
            "overrides": {"team-and-relationships.md": "restricted"},
        },
        "deep": {
            "modules": {
                "A": {
                    "name": "töö-tegelikkus",
                    "sections": {
                        "identity.md": ["identity-facts", "what-i-do", "known-for"],
                        "role-and-responsibilities.md": ["responsibilities", "rhythms", "decisions", "outputs", "reporting"],
                        "current-projects.md": ["active-projects-and-status", "priority-order", "bottleneck-and-delegable-work"],
                        "tools-and-systems.md": ["core-stack", "data-sources", "integrations", "evaluating", "discarded"],
                    }
                },
                "B": {
                    "name": "turg-ja-ekspertiis",
                    "sections": {
                        "current-projects.md": ["icp-and-best-customers", "offer-and-evidence", "trigger", "ebia-sector-size-region", "message-purpose-cta", "forbidden-claims", "objections-optional"],
                        "domain-knowledge.md": ["expertise", "terminology", "domain-context", "frameworks", "learning-zones"],
                    }
                },
                "C": {
                    "name": "otsused-ja-piirid",
                    "sections": {
                        "goals-and-priorities.md": ["current-goals", "long-term-goals", "tradeoffs", "non-goals", "success-criteria"],
                        "preferences-and-constraints.md": ["hard-rules", "preferences", "constraints", "delegation"],
                        "decision-log.md": ["decisions", "reasoning", "uncertainty"],
                    }
                },
                "D": {
                    "name": "hääl-ja-inimesed",
                    "starts_with_import": True,
                    "sections": {
                        "communication-style.md": ["general-style", "channel-registers", "formatting", "avoid", "signatures"],
                        "writing-samples.md": ["samples", "sample-metadata"],
                        "team-and-relationships.md": ["people", "relationship-context", "agent-guidance"],
                    }
                },
            }
        },
        "deep_workflow": {"reads": ["existing-files", "candidates", "review_after"], "shows_coverage": True, "saves_after_each_module": True, "resumes": True, "promotion_requires": ["visible-diff", "confirmation"], "uncovered_required_visible": True, "synthesis_requires": ["2-independent-cases", "condition", "downstream-action", "falsifier"]},
        "learning_loop": {
            "commands": ["õpime parandusest", "siin on lõplik versioon"],
            "categories": ["fact-correction", "general-style", "channel-style", "addressee-exception", "temporary-project-context"],
            "same_conversation_one_paste": True,
            "automatic_promotion": False,
            "visible_diff_and_confirmation": True,
            "one_edit_event_is_one_source_family": True,
        },
        "candidate_ledger": {"required": ["id", "target_file", "target_section", "claim", "evidence_ids", "scope", "expires", "status"]},
        "imports": {
            "treatment": "data",
            "execute_embedded_instructions": False,
            "preserve_verbatim_samples": True,
            "sensitive_third_party": "restricted",
        },
        "bundles": {
            "directory": "portfolio/bundles",
            "kind": "projection",
            "exclude_candidates": True,
            "exclude_restricted_by_default": True,
            "sensitivity_propagation": "any-restricted-source-makes-projection-restricted",
            "required": {
                "client-outreach.md": {
                    "sources": ["identity.md", "current-projects.md", "communication-style.md", "writing-samples.md"],
                    "sensitivity": "exportable"
                },
                "client-research.md": {
                    "sources": ["identity.md", "current-projects.md", "domain-knowledge.md"],
                    "sensitivity": "exportable"
                },
                "content-writer.md": {
                    "sources": ["identity.md", "communication-style.md", "writing-samples.md", "domain-knowledge.md"],
                    "sensitivity": "exportable"
                }
            }
        },
        "frozen_quick": {
            "path": "quick-interview.md",
            "manifest": "evals/frozen-quick.json",
            "algorithm": "sha256",
            "sha256_required": True,
            "published_sha256": "c7520be708808eb577c7cbd5cd77cc91a3bad60cfbdbfa554996a8857e5b587e",
        },
    }


class ContractTests(unittest.TestCase):
    def test_valid_contract_encodes_required_v3_invariants(self):
        self.assertEqual(checker.validate_contract(valid_contract()), [])

    def test_contract_rejects_wrong_profile_and_evidence_counts(self):
        contract = valid_contract()
        contract["layers"]["profiles"].pop()
        contract["layers"]["evidence"].append("extra.md")
        codes = {issue.code for issue in checker.validate_contract(contract)}
        self.assertIn("profile_count", codes)
        self.assertIn("evidence_count", codes)

    def test_contract_rejects_duplicate_section_ownership(self):
        contract = valid_contract()
        contract["deep"]["modules"]["B"]["sections"].setdefault("identity.md", []).append("identity-facts")
        codes = {issue.code for issue in checker.validate_contract(contract)}
        self.assertIn("section_owner_duplicate", codes)

    def test_contract_requires_module_d_to_start_with_import(self):
        contract = valid_contract()
        contract["deep"]["modules"]["D"]["starts_with_import"] = False
        codes = {issue.code for issue in checker.validate_contract(contract)}
        self.assertIn("module_d_import", codes)

    def test_checked_in_module_names_are_exact(self):
        contract = checker.load_contract(ROOT / "evals" / "context-v3-contract.json")
        names = {key: value["name"] for key, value in contract["deep"]["modules"].items()}
        self.assertEqual(names, {"A": "töö-tegelikkus", "B": "turg-ja-ekspertiis", "C": "otsused-ja-piirid", "D": "hääl-ja-inimesed"})

    def test_bundle_contract_locks_metadata_but_not_body(self):
        contract = checker.load_contract(ROOT / "evals" / "context-v3-contract.json")
        required = contract["bundles"]["required"]
        self.assertEqual(required["client-outreach.md"], {"sources": ["identity.md", "current-projects.md", "communication-style.md", "writing-samples.md"], "sensitivity": "exportable"})
        self.assertEqual(required["content-writer.md"], {"sources": ["identity.md", "communication-style.md", "writing-samples.md", "domain-knowledge.md"], "sensitivity": "exportable"})
        self.assertTrue(all("body_sha256" not in spec for spec in required.values()))
        self.assertEqual(contract["bundles"]["sensitivity_propagation"], "any-restricted-source-makes-projection-restricted")

    def test_bundle_contract_requires_sensitivity_propagation(self):
        contract = valid_contract()
        contract["bundles"].pop("sensitivity_propagation")
        codes = {issue.code for issue in checker.validate_contract(contract)}
        self.assertIn("bundle_policy", codes)

    def test_confirmed_deep_ownership_and_quick_invariants(self):
        contract = valid_contract()
        self.assertEqual(checker.validate_contract(contract), [])
        owners = checker.section_owners(contract)
        self.assertTrue(all(owner == "C" for (filename, _), owner in owners.items() if filename == "goals-and-priorities.md"))
        self.assertFalse(any(filename == "goals-and-priorities.md" for filename in contract["deep"]["modules"]["B"]["sections"]))
        self.assertEqual(contract["quick"]["owns_sections"], [])

    def test_contract_rejects_missing_decision_invariants(self):
        contract = valid_contract()
        contract["quick"]["required_coverage"].pop()
        contract["deep_workflow"]["promotion_requires"] = ["confirmation"]
        contract["candidate_ledger"]["required"].pop()
        contract["bundles"]["exclude_candidates"] = False
        contract["imports"]["preserve_verbatim_samples"] = False
        codes = {item.code for item in checker.validate_contract(contract)}
        self.assertTrue({"quick_contract", "deep_workflow", "candidate_ledger", "bundle_policy", "import_contract"}.issubset(codes))

    def test_contract_rejects_an_unsafe_learning_loop(self):
        contract = valid_contract()
        contract["learning_loop"]["automatic_promotion"] = True
        contract["learning_loop"]["categories"].pop()
        codes = {item.code for item in checker.validate_contract(contract)}
        self.assertIn("learning_loop", codes)

    def test_contract_requires_an_actionable_falsifiable_deep_synthesis(self):
        contract = valid_contract()
        contract["deep_workflow"]["synthesis_requires"].remove("falsifier")
        codes = {item.code for item in checker.validate_contract(contract)}
        self.assertIn("deep_workflow", codes)


class ProfileRuleTests(unittest.TestCase):
    def test_valid_profile_passes(self):
        text = (FIXTURES / "valid_identity.md").read_text(encoding="utf-8")
        self.assertEqual(checker.validate_profile("identity.md", text, valid_contract()), [])

    def test_supported_claim_needs_two_distinct_evidence_ids(self):
        text = (FIXTURES / "invalid_supported.md").read_text(encoding="utf-8")
        codes = {issue.code for issue in checker.validate_profile("identity.md", text, valid_contract())}
        self.assertIn("supported_evidence", codes)

    def test_supported_claim_needs_two_independent_sources(self):
        text = (FIXTURES / "invalid_same_source.md").read_text(encoding="utf-8")
        codes = {issue.code for issue in checker.validate_profile("identity.md", text, valid_contract())}
        self.assertIn("supported_independence", codes)

    def test_team_is_always_restricted(self):
        text = (FIXTURES / "invalid_team.md").read_text(encoding="utf-8")
        codes = {issue.code for issue in checker.validate_profile("team-and-relationships.md", text, valid_contract())}
        self.assertIn("sensitivity_override", codes)

    def test_confirmed_claim_requires_user_stated_basis(self):
        text = (FIXTURES / "valid_identity.md").read_text(encoding="utf-8").replace("; basis=user-stated", "")
        self.assertIn("confirmed_basis", {issue.code for issue in checker.validate_profile("identity.md", text, valid_contract())})

    def test_generic_channels_are_not_independent_source_families(self):
        text = (FIXTURES / "invalid_generic_source.md").read_text(encoding="utf-8")
        self.assertIn("evidence_family", {issue.code for issue in checker.validate_profile("identity.md", text, valid_contract())})

    def test_verbatim_fenced_sample_bullets_are_not_claims_and_extract_byte_exactly(self):
        text = (FIXTURES / "writing_samples_fenced.md").read_text(encoding="utf-8")
        self.assertEqual(checker.validate_profile("writing-samples.md", text, valid_contract()), [])
        self.assertTrue(hasattr(checker, "extract_verbatim_samples"), "fenced sample extractor not implemented")
        expected = [
            "- esimene paljas bullet\n- teine paljas bullet\n- kolmas paljas bullet\n",
            "- üks muutmata rida\n- kaks muutmata rida\n- kolm muutmata rida\n",
        ]
        extracted = checker.extract_verbatim_samples(text)
        self.assertEqual(extracted, expected)
        self.assertEqual(
            [hashlib.sha256(sample.encode("utf-8")).hexdigest() for sample in extracted],
            [hashlib.sha256(sample.encode("utf-8")).hexdigest() for sample in expected],
        )

    def test_unfenced_bullet_still_requires_claim_metadata(self):
        text = (FIXTURES / "writing_samples_fenced.md").read_text(encoding="utf-8")
        text = text.replace(" <!-- claim: status=kinnitatud; basis=user-stated -->", "", 1)
        issues = [issue for issue in checker.validate_profile("writing-samples.md", text, valid_contract()) if issue.code == "claim_missing_status"]
        self.assertEqual(len(issues), 1)


class RunRuleTests(unittest.TestCase):
    def load_run(self, name):
        return json.loads((FIXTURES / name).read_text(encoding="utf-8"))

    def test_quick_has_exactly_four_contract_outputs_and_imports_are_data(self):
        self.assertEqual(checker.validate_run(self.load_run("valid_quick_run.json"), valid_contract()), [])

    def test_quick_rejects_missing_output_and_import_instruction_execution(self):
        codes = {issue.code for issue in checker.validate_run(self.load_run("invalid_quick_run.json"), valid_contract())}
        self.assertIn("quick_outputs", codes)
        self.assertIn("import_treatment", codes)
        self.assertIn("import_instruction_execution", codes)

    def test_deep_writes_only_sections_owned_by_the_module(self):
        self.assertEqual(checker.validate_run(self.load_run("valid_deep_run.json"), valid_contract()), [])
        codes = {issue.code for issue in checker.validate_run(self.load_run("invalid_deep_owner.json"), valid_contract())}
        self.assertIn("section_owner", codes)

    def test_module_d_starts_with_an_import_event(self):
        invalid = self.load_run("invalid_deep_import_order.json")
        codes = {issue.code for issue in checker.validate_run(invalid, valid_contract())}
        self.assertIn("module_d_import_order", codes)

    def test_quick_runtime_limits_are_enforced(self):
        codes = {issue.code for issue in checker.validate_run(self.load_run("invalid_quick_run.json"), valid_contract())}
        self.assertTrue({"quick_command", "quick_answer_limit", "questions_per_turn", "deepener_limit", "quick_duration", "writing_samples", "quick_section_ownership", "quick_coverage"}.issubset(codes))

    def test_quick_claim_policy_keeps_explicit_facts_confirmed_and_single_inference_candidate(self):
        run = self.load_run("valid_quick_run.json")
        self.assertEqual(checker.validate_run(run, valid_contract()), [])
        run["claims"][2]["status"] = "toetatud"
        self.assertIn("quick_claim_policy", {issue.code for issue in checker.validate_run(run, valid_contract())})

    def test_deep_workflow_and_b_goal_routing(self):
        valid = self.load_run("valid_deep_run.json")
        valid["findings"] = [{"module": "B", "target_file": "goals-and-priorities.md", "routed_to": "candidates"}]
        self.assertEqual(checker.validate_run(valid, valid_contract()), [])
        valid["findings"][0]["routed_to"] = "profile"
        self.assertIn("finding_route", {issue.code for issue in checker.validate_run(valid, valid_contract())})
        valid["workflow"]["promotions"][0]["visible_diff"] = False
        self.assertIn("deep_workflow_run", {issue.code for issue in checker.validate_run(valid, valid_contract())})

    def test_candidate_ledger_schema(self):
        candidates = json.loads((FIXTURES / "valid_candidates.json").read_text(encoding="utf-8"))
        self.assertEqual(checker.validate_candidates(candidates, valid_contract()), [])
        del candidates[0]["expires"]
        self.assertIn("candidate_schema", {issue.code for issue in checker.validate_candidates(candidates, valid_contract())})


class ProjectionAndFreezeTests(unittest.TestCase):
    def test_bundle_must_be_a_projection(self):
        valid = (FIXTURES / "valid_bundle.md").read_text(encoding="utf-8")
        invalid = (FIXTURES / "invalid_bundle.md").read_text(encoding="utf-8")
        self.assertEqual(checker.validate_projection("client-outreach.md", valid, valid_contract()), [])
        codes = {issue.code for issue in checker.validate_projection("client-outreach.md", invalid, valid_contract())}
        self.assertIn("projection_marker", codes)

    def test_projection_body_can_change_without_changing_locked_metadata(self):
        text = (FIXTURES / "valid_bundle.md").read_text(encoding="utf-8") + "changed\n"
        self.assertEqual(checker.validate_projection("client-outreach.md", text, valid_contract()), [])

    def test_frozen_quick_hash_must_match_manifest(self):
        fixture_root = FIXTURES / "frozen_valid"
        self.assertEqual(checker.validate_frozen_quick(fixture_root, valid_contract()), [])
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "evals").mkdir()
            (root / "quick-interview.md").write_text("changed\n", encoding="utf-8")
            source_manifest = fixture_root / "evals" / "frozen-quick.json"
            (root / "evals" / "frozen-quick.json").write_text(source_manifest.read_text(encoding="utf-8"), encoding="utf-8")
            codes = {issue.code for issue in checker.validate_frozen_quick(root, valid_contract())}
            self.assertIn("frozen_quick_hash", codes)

    def test_root_index_must_match_baseline_hash(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "index.md").write_text("baseline", encoding="utf-8")
            contract = valid_contract()
            contract["baseline"]["root_index_sha256"] = hashlib.sha256(b"baseline").hexdigest()
            self.assertEqual(checker.validate_root_index(root, contract), [])
            (root / "index.md").write_text("changed", encoding="utf-8")
            codes = {issue.code for issue in checker.validate_root_index(root, contract)}
            self.assertIn("root_index_changed", codes)


class RepositoryContractTests(unittest.TestCase):
    def test_checked_in_claim_semantics_match_review(self):
        contract = checker.load_contract(ROOT / "evals" / "context-v3-contract.json")
        self.assertEqual(contract["claims"]["confirmed_rule"], "explicit-user-statement")
        self.assertEqual(contract["claims"]["independence_key"], "source-artifact-or-situation")
        self.assertEqual(contract["quick"]["claim_policy"]["later_modification_owner"], "deep-modules")

    def test_checked_in_contract_matches_the_validated_schema(self):
        contract = checker.load_contract(ROOT / "evals" / "context-v3-contract.json")
        self.assertEqual(checker.validate_contract(contract), [])

    def test_release_check_reports_baseline_fixture_as_not_ready(self):
        contract = valid_contract()
        issues = checker.release_check(FIXTURES / "preintegration_repo", contract)
        self.assertTrue(issues)
        self.assertIn("known_quick_drift", {issue.code for issue in issues})

    def test_baseline_manifest_must_agree_with_contract(self):
        self.assertEqual(checker.validate_baseline(ROOT, checker.load_contract(ROOT / "evals" / "context-v3-contract.json")), [])


if __name__ == "__main__":
    unittest.main()

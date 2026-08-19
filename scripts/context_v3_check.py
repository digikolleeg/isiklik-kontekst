#!/usr/bin/env python3
import argparse
import datetime as dt
import hashlib
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path


EXPECTED_PROFILES = {
    "identity.md",
    "role-and-responsibilities.md",
    "current-projects.md",
    "team-and-relationships.md",
    "tools-and-systems.md",
    "communication-style.md",
    "goals-and-priorities.md",
    "preferences-and-constraints.md",
    "domain-knowledge.md",
}
EXPECTED_EVIDENCE = {"writing-samples.md", "decision-log.md"}
EXPECTED_QUICK = [
    "identity.md",
    "current-projects.md",
    "communication-style.md",
    "writing-samples.md",
]
EXPECTED_STATUSES = {"kinnitatud", "toetatud", "kandidaat"}
CLAIM_RE = re.compile(r"^- .+?\s+<!--\s*claim:\s*status=(?P<status>[^;\s]+)(?P<rest>.*?)\s*-->$")
REQUIRED_COVERAGE = {"offer_buyer", "icp_sector_size_region", "problem_trigger", "credibility_evidence", "message_purpose_cta", "forbidden_claims", "channel_register_length", "forbidden_mannerisms", "real_samples"}


@dataclass(frozen=True)
class Issue:
    code: str
    message: str
    path: str = ""


def issue(code, message, path=""):
    return Issue(code=code, message=message, path=str(path))


def load_contract(path):
    with Path(path).open(encoding="utf-8") as handle:
        return json.load(handle)


def _get(mapping, *keys, default=None):
    value = mapping
    for key in keys:
        if not isinstance(value, dict) or key not in value:
            return default
        value = value[key]
    return value


def validate_contract(contract):
    issues = []
    profiles = _get(contract, "layers", "profiles", default=[])
    evidence = _get(contract, "layers", "evidence", default=[])
    if len(profiles) != 9 or set(profiles) != EXPECTED_PROFILES:
        issues.append(issue("profile_count", "contract must define exactly the nine v3 profile files"))
    if len(evidence) != 2 or set(evidence) != EXPECTED_EVIDENCE:
        issues.append(issue("evidence_count", "contract must define exactly writing-samples and decision-log as evidence"))
    if _get(contract, "quick", "outputs", default=[]) != EXPECTED_QUICK:
        issues.append(issue("quick_outputs", "quick mode must contain exactly the four ordered core outputs"))
    if set(_get(contract, "claims", "statuses", default=[])) != EXPECTED_STATUSES:
        issues.append(issue("claim_statuses", "claim statuses must be kinnitatud, toetatud and kandidaat"))
    if _get(contract, "claims", "supported_min_independent_evidence") != 2:
        issues.append(issue("supported_threshold", "toetatud must require exactly two or more independent evidence IDs"))
    if _get(contract, "claims", "evidence_id_format") != "<source-family>:<observation-id>" or _get(
        contract, "claims", "independence_key"
    ) != "source-family":
        issues.append(issue("evidence_id_contract", "evidence IDs must encode independent source and observation IDs"))
    quick = contract.get("quick", {})
    if quick.get("commands") != ["töötoa intervjuu", "kiire intervjuu"] or quick.get("max_user_answers_after_import") != 10 or quick.get("questions_per_turn") != 1 or quick.get("max_deepeners_per_answer") != 1 or quick.get("target_minutes") != {"min": 30, "max": 40} or quick.get("min_verbatim_writing_samples") != 2 or quick.get("owns_sections") != [] or set(quick.get("required_coverage", [])) != REQUIRED_COVERAGE:
        issues.append(issue("quick_contract", "quick decision invariants are incomplete"))
    if _get(contract, "claims", "confirmed_rule") != "user-universal-statement-only" or _get(contract, "claims", "single_observation_status") != "kandidaat":
        issues.append(issue("claim_contract", "claim confirmation and single-observation rules are incomplete"))

    required_frontmatter = set(_get(contract, "frontmatter", "required", default=[]))
    if not {"updated", "review_after", "sensitivity"}.issubset(required_frontmatter):
        issues.append(issue("frontmatter_contract", "updated, review_after and sensitivity are required"))
    if set(_get(contract, "frontmatter", "sensitivity_values", default=[])) != {"exportable", "restricted"}:
        issues.append(issue("sensitivity_values", "only exportable and restricted are valid sensitivity values"))
    if _get(contract, "frontmatter", "overrides", "team-and-relationships.md") != "restricted":
        issues.append(issue("team_restricted", "team-and-relationships.md must be restricted"))

    modules = _get(contract, "deep", "modules", default={})
    if set(modules) != {"A", "B", "C", "D"}:
        issues.append(issue("deep_modules", "deep mode must define modules A through D"))
    expected_module_names = {"A": "töö-tegelikkus", "B": "turg-ja-ekspertiis", "C": "otsused-ja-piirid", "D": "hääl-ja-inimesed"}
    if {key: value.get("name") for key, value in modules.items()} != expected_module_names:
        issues.append(issue("deep_module_names", "deep module names must match the confirmed A-D contract"))
    if _get(modules, "D", "starts_with_import") is not True:
        issues.append(issue("module_d_import", "deep module D must start with material import"))
    owners = {}
    covered_files = set()
    for module_name, module in modules.items():
        for filename, sections in module.get("sections", {}).items():
            covered_files.add(filename)
            for section in sections:
                key = (filename, section)
                if key in owners:
                    issues.append(
                        issue(
                            "section_owner_duplicate",
                            f"{filename}#{section} belongs to both {owners[key]} and {module_name}",
                        )
                    )
                owners[key] = module_name
    if set(profiles) | set(evidence) != covered_files:
        issues.append(issue("deep_coverage", "deep module ownership must cover all nine profiles and two evidence files"))

    if _get(contract, "imports", "treatment") != "data":
        issues.append(issue("import_contract", "imports must be treated as data"))
    if _get(contract, "imports", "execute_embedded_instructions") is not False:
        issues.append(issue("import_contract", "embedded import instructions must never execute"))
    if _get(contract, "imports", "preserve_verbatim_samples") is not True or _get(contract, "imports", "sensitive_third_party") != "restricted":
        issues.append(issue("import_contract", "import preservation and third-party sensitivity rules are incomplete"))
    workflow = contract.get("deep_workflow", {})
    if set(workflow.get("reads", [])) != {"existing-files", "candidates", "review_after"} or not all(workflow.get(key) is True for key in ("shows_coverage", "saves_after_each_module", "resumes", "uncovered_required_visible")) or workflow.get("promotion_requires") != ["visible-diff", "confirmation"]:
        issues.append(issue("deep_workflow", "deep workflow invariants are incomplete"))
    if set(_get(contract, "candidate_ledger", "required", default=[])) != {"id", "target_file", "target_section", "claim", "evidence_ids", "scope", "expires", "status"}:
        issues.append(issue("candidate_ledger", "candidate ledger schema is incomplete"))
    if _get(contract, "bundles", "kind") != "projection":
        issues.append(issue("bundle_contract", "bundles must be projections"))
    if _get(contract, "bundles", "exclude_candidates") is not True or _get(contract, "bundles", "exclude_restricted_by_default") is not True:
        issues.append(issue("bundle_policy", "bundle exclusion policy is incomplete"))
    required_bundles = _get(contract, "bundles", "required", default={})
    if not required_bundles:
        issues.append(issue("bundle_contract", "contract must lock required projection targets"))
    for filename, projection in required_bundles.items():
        if not projection.get("sources") or projection.get("sensitivity") not in {"exportable", "restricted"}:
            issues.append(issue("bundle_contract", f"{filename} must lock sources and sensitivity"))
    if _get(contract, "frozen_quick", "algorithm") != "sha256" or _get(
        contract, "frozen_quick", "sha256_required"
    ) is not True:
        issues.append(issue("frozen_quick_contract", "published quick interview must be frozen by SHA-256"))

    baseline = contract.get("baseline", {})
    if baseline.get("head") != "dea4a2c6f29c2e7561ed5c4f3b2f1069c99b0925":
        issues.append(issue("baseline_head", "v3 baseline HEAD must be dea4a2c"))
    expected_drift = {"quick-count-3-vs-4", "portfolio-count-10-vs-11"}
    if set(baseline.get("known_drift", [])) != expected_drift:
        issues.append(issue("baseline_drift", "baseline must record the known 3/4 and 10/11 drift"))
    return issues


def _parse_scalar(value):
    value = value.strip()
    if value.lower() == "true":
        return True
    if value.lower() == "false":
        return False
    if value.startswith("[") and value.endswith("]"):
        return [item.strip().strip("\"'") for item in value[1:-1].split(",") if item.strip()]
    return value.strip("\"'")


def parse_frontmatter(text):
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    metadata = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return metadata
        if ":" in line and not line.startswith((" ", "\t")):
            key, value = line.split(":", 1)
            metadata[key.strip()] = _parse_scalar(value)
    return {}


def _valid_date(value):
    try:
        dt.date.fromisoformat(str(value))
        return True
    except ValueError:
        return False


def validate_profile(filename, text, contract):
    issues = []
    metadata = parse_frontmatter(text)
    required = _get(contract, "frontmatter", "required", default=[])
    for field in required:
        if field not in metadata:
            issues.append(issue("frontmatter_missing", f"missing frontmatter field: {field}", filename))
    for field in ("updated", "review_after"):
        if field in metadata and not _valid_date(metadata[field]):
            issues.append(issue("frontmatter_date", f"{field} must be YYYY-MM-DD", filename))
    if all(field in metadata and _valid_date(metadata[field]) for field in ("updated", "review_after")):
        if dt.date.fromisoformat(metadata["review_after"]) < dt.date.fromisoformat(metadata["updated"]):
            issues.append(issue("review_before_update", "review_after cannot precede updated", filename))
    sensitivity = metadata.get("sensitivity")
    if sensitivity not in _get(contract, "frontmatter", "sensitivity_values", default=[]):
        issues.append(issue("sensitivity_value", "invalid sensitivity", filename))
    override = _get(contract, "frontmatter", "overrides", filename)
    if override and sensitivity != override:
        issues.append(issue("sensitivity_override", f"{filename} sensitivity must be {override}", filename))

    statuses = set(_get(contract, "claims", "statuses", default=[]))
    minimum = _get(contract, "claims", "supported_min_independent_evidence", default=2)
    for line_number, line in enumerate(text.splitlines(), start=1):
        if not line.startswith("- "):
            continue
        match = CLAIM_RE.match(line)
        if not match:
            issues.append(issue("claim_missing_status", "profile bullet must use the v3 claim marker", f"{filename}:{line_number}"))
            continue
        status = match.group("status").strip()
        if status not in statuses:
            issues.append(issue("claim_status", f"unknown claim status: {status}", f"{filename}:{line_number}"))
            continue
        evidence_match = re.search(r"(?:^|;)\s*evidence=([^;]+)", match.group("rest"))
        evidence_ids = {
            evidence_id.strip()
            for evidence_id in (evidence_match.group(1) if evidence_match else "").split(",")
            if evidence_id.strip()
        }
        if status == "toetatud" and len(evidence_ids) < minimum:
            issues.append(
                issue(
                    "supported_evidence",
                    f"toetatud requires at least {minimum} distinct evidence IDs",
                    f"{filename}:{line_number}",
                )
            )
        if status == "toetatud":
            source_ids = {evidence_id.split(":", 1)[0] for evidence_id in evidence_ids if ":" in evidence_id}
            if len(source_ids) < minimum or any(":" not in evidence_id for evidence_id in evidence_ids):
                issues.append(
                    issue(
                        "supported_independence",
                        f"toetatud requires observations from at least {minimum} independent sources",
                        f"{filename}:{line_number}",
                    )
                )
        if status == "kinnitatud" and "basis=user-universal" not in line:
            issues.append(issue("confirmed_basis", "kinnitatud requires explicit user-universal basis", f"{filename}:{line_number}"))
    return issues


def _validate_imports(imports, contract):
    issues = []
    expected_treatment = _get(contract, "imports", "treatment")
    expected_execution = _get(contract, "imports", "execute_embedded_instructions")
    for imported in imports:
        if imported.get("treated_as") != expected_treatment:
            issues.append(issue("import_treatment", "import must be treated as data", imported.get("id", "")))
        if imported.get("embedded_instructions_executed") is not expected_execution:
            issues.append(
                issue(
                    "import_instruction_execution",
                    "embedded instructions in imported data must not execute",
                    imported.get("id", ""),
                )
            )
        if imported.get("verbatim_samples_preserved") is not True:
            issues.append(issue("import_verbatim", "imported writing samples must be preserved verbatim", imported.get("id", "")))
        if imported.get("sensitive_third_party") != "restricted":
            issues.append(issue("import_sensitivity", "sensitive third-party import data must be restricted", imported.get("id", "")))
    return issues


def section_owners(contract):
    owners = {}
    for module_name, module in _get(contract, "deep", "modules", default={}).items():
        for filename, sections in module.get("sections", {}).items():
            for section in sections:
                owners[(filename, section)] = module_name
    return owners


def validate_run(run, contract):
    issues = _validate_imports(run.get("imports", []), contract)
    mode = run.get("mode")
    if mode == "quick":
        if run.get("outputs") != _get(contract, "quick", "outputs", default=[]):
            issues.append(issue("quick_outputs", "quick output list must match the contract exactly"))
        quick = contract.get("quick", {})
        metrics = run.get("metrics", {})
        checks = [
            (run.get("command") in quick.get("commands", []), "quick_command"),
            (metrics.get("user_answers_after_import", 10**9) <= quick.get("max_user_answers_after_import", 0), "quick_answer_limit"),
            (metrics.get("max_questions_per_turn") == quick.get("questions_per_turn"), "questions_per_turn"),
            (metrics.get("max_deepeners_per_answer") == quick.get("max_deepeners_per_answer"), "deepener_limit"),
            (quick.get("target_minutes", {}).get("min", 0) <= metrics.get("minutes", -1) <= quick.get("target_minutes", {}).get("max", -1), "quick_duration"),
            (metrics.get("verbatim_writing_samples", 0) >= quick.get("min_verbatim_writing_samples", 0), "writing_samples"),
            (metrics.get("owns_sections") == [], "quick_section_ownership"),
            (set(metrics.get("coverage", [])) == set(quick.get("required_coverage", [])), "quick_coverage"),
        ]
        issues.extend(issue(code, f"quick runtime invariant failed: {code}") for passed, code in checks if not passed)
    elif mode == "deep":
        owners = section_owners(contract)
        for write in run.get("writes", []):
            key = (write.get("file"), write.get("section"))
            if owners.get(key) != write.get("module"):
                issues.append(
                    issue(
                        "section_owner",
                        f"{write.get('module')} does not own {write.get('file')}#{write.get('section')}",
                    )
                )
        if any(write.get("module") == "D" for write in run.get("writes", [])):
            module_d_events = [event for event in run.get("events", []) if event.get("module") == "D"]
            if not module_d_events or module_d_events[0].get("type") != "import":
                issues.append(issue("module_d_import_order", "module D must start with an import event"))
        workflow = run.get("workflow", {})
        expected_workflow = contract.get("deep_workflow", {})
        if set(workflow.get("read_inputs", [])) != set(expected_workflow.get("reads", [])) or workflow.get("coverage_shown") is not True or set(workflow.get("saved_modules", [])) != {"A", "B", "C", "D"} or workflow.get("resumed") is not True or workflow.get("uncovered_required_visible") is not True or any(promotion.get("visible_diff") is not True or promotion.get("confirmed") is not True for promotion in workflow.get("promotions", [])):
            issues.append(issue("deep_workflow_run", "deep run does not satisfy read, coverage, save, resume or promotion rules"))
        for finding in run.get("findings", []):
            if finding.get("module") == "B" and finding.get("target_file") == "goals-and-priorities.md" and finding.get("routed_to") != "candidates":
                issues.append(issue("finding_route", "module B goals findings must route to candidates"))
    else:
        issues.append(issue("run_mode", "run mode must be quick or deep"))
    return issues


def validate_candidates(candidates, contract):
    required = set(_get(contract, "candidate_ledger", "required", default=[]))
    issues = []
    for index, candidate in enumerate(candidates):
        if set(candidate) != required or candidate.get("status") != "kandidaat" or not isinstance(candidate.get("evidence_ids"), list):
            issues.append(issue("candidate_schema", "candidate does not match the locked ledger schema", str(index)))
    return issues


def validate_projection(filename, text, contract):
    issues = []
    metadata = parse_frontmatter(text)
    if metadata.get("projection") is not True:
        issues.append(issue("projection_marker", "bundle must declare projection: true", filename))
    sources = metadata.get("sources", [])
    allowed_sources = set(_get(contract, "layers", "profiles", default=[])) | set(
        _get(contract, "layers", "evidence", default=[])
    )
    if not sources or not set(sources).issubset(allowed_sources):
        issues.append(issue("projection_sources", "bundle sources must be non-empty v3 context files", filename))
    if "team-and-relationships.md" in sources and metadata.get("sensitivity") != "restricted":
        issues.append(issue("projection_sensitivity", "projection containing team data must be restricted", filename))
    expected = _get(contract, "bundles", "required", filename)
    if expected:
        if sources != expected.get("sources") or metadata.get("sensitivity") != expected.get("sensitivity"):
            issues.append(issue("projection_contract", "projection metadata differs from its locked contract", filename))
    return issues


def _sha256(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_frozen_quick(root, contract):
    root = Path(root)
    spec = contract.get("frozen_quick", {})
    artifact = root / spec.get("path", "")
    manifest_path = root / spec.get("manifest", "")
    issues = []
    if not artifact.is_file():
        issues.append(issue("frozen_quick_missing", "frozen quick artifact is missing", artifact))
    if not manifest_path.is_file():
        issues.append(issue("frozen_quick_manifest", "frozen quick manifest is missing", manifest_path))
        return issues
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as error:
        issues.append(issue("frozen_quick_manifest", f"invalid frozen quick manifest: {error}", manifest_path))
        return issues
    expected_hash = manifest.get("sha256")
    if not isinstance(expected_hash, str) or re.fullmatch(r"[0-9a-f]{64}", expected_hash) is None:
        issues.append(issue("frozen_quick_sha", "manifest must contain a lowercase SHA-256", manifest_path))
    if artifact.is_file() and isinstance(expected_hash, str) and _sha256(artifact) != expected_hash:
        issues.append(issue("frozen_quick_hash", "frozen quick artifact hash does not match", artifact))
    published_hash = spec.get("published_sha256")
    if re.fullmatch(r"[0-9a-f]{64}", str(published_hash or "")) is None:
        issues.append(issue("frozen_quick_unset", "contract does not contain the published quick SHA-256"))
    elif expected_hash != published_hash:
        issues.append(issue("frozen_quick_contract_hash", "manifest SHA-256 differs from the locked contract hash", manifest_path))
    if manifest.get("path") != spec.get("path") or manifest.get("algorithm") != "sha256":
        issues.append(issue("frozen_quick_manifest", "manifest path or algorithm does not match contract", manifest_path))
    return issues


def validate_root_index(root, contract):
    path = Path(root) / "index.md"
    if not path.is_file():
        return [issue("root_index_missing", "root wiki index is missing", path)]
    expected = _get(contract, "baseline", "root_index_sha256")
    if _sha256(path) != expected:
        return [issue("root_index_changed", "root index.md differs from the v3 baseline", path)]
    return []


def validate_baseline(root, contract):
    path = Path(root) / "evals" / "baselines" / "v3-pre" / "manifest.json"
    if not path.is_file():
        return [issue("baseline_manifest", "v3-pre baseline manifest is missing", path)]
    try:
        manifest = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as error:
        return [issue("baseline_manifest", f"invalid baseline manifest: {error}", path)]
    issues = []
    baseline = contract.get("baseline", {})
    if manifest.get("head") != baseline.get("head"):
        issues.append(issue("baseline_head_mismatch", "baseline manifest HEAD differs from contract", path))
    if manifest.get("root_index_sha256") != baseline.get("root_index_sha256"):
        issues.append(issue("baseline_index_mismatch", "baseline root index hash differs from contract", path))
    if set(manifest.get("known_drift", {})) != set(baseline.get("known_drift", [])):
        issues.append(issue("baseline_drift_mismatch", "baseline drift keys differ from contract", path))
    return issues


def _validate_known_drift(root):
    paths = [
        "README.md",
        "quick-start.md",
        "CLAUDE.md",
        "portfolio/interview-protocol/agent-system-prompt.md",
        "skills/konteksti-looja/SKILL.md",
        "skills/konteksti-looja/README.md",
    ]
    text = "\n".join(
        (Path(root) / path).read_text(encoding="utf-8")
        for path in paths
        if (Path(root) / path).is_file()
    )
    issues = []
    if re.search(r"(?i)(?:kolm|3)\s+(?:põhi-?)?faili", text):
        issues.append(issue("known_quick_drift", "product docs still describe a three-file quick mode"))
    if re.search(r"(?i)(?:täpselt\s+)?(?:kümme|10)\s+(?:konteksti-?)?faili", text):
        issues.append(issue("known_portfolio_drift", "product docs still describe ten total files instead of 9+2"))
    return issues


def _validate_templates(root, contract):
    directory = Path(root) / "portfolio" / "templates"
    expected = set(_get(contract, "layers", "profiles", default=[])) | set(
        _get(contract, "layers", "evidence", default=[])
    )
    actual = {path.name for path in directory.glob("*.md")}
    issues = []
    if actual != expected:
        issues.append(issue("template_set", "template filenames must match the 9+2 contract", directory))
    for filename in sorted(expected & actual):
        text = (directory / filename).read_text(encoding="utf-8")
        for field in _get(contract, "frontmatter", "required", default=[]):
            if f"{field}:" not in text:
                issues.append(issue("template_frontmatter", f"template does not encode {field}", directory / filename))
        if filename == "team-and-relationships.md" and "sensitivity: restricted" not in text:
            issues.append(issue("template_team_restricted", "team template must encode restricted sensitivity", directory / filename))
    return issues


def _validate_bundles(root, contract):
    directory = Path(root) / _get(contract, "bundles", "directory", default="portfolio/bundles")
    issues = []
    expected = set(_get(contract, "bundles", "required", default={}))
    actual = {path.name for path in directory.glob("*.md") if path.name != "README.md"}
    if actual != expected:
        issues.append(issue("projection_targets", "bundle targets must match the locked projection set", directory))
    for path in sorted(directory.glob("*.md")):
        if path.name == "README.md":
            continue
        issues.extend(validate_projection(path.name, path.read_text(encoding="utf-8"), contract))
    return issues


def release_check(root, contract):
    issues = []
    issues.extend(validate_contract(contract))
    issues.extend(validate_root_index(root, contract))
    issues.extend(validate_baseline(root, contract))
    issues.extend(validate_frozen_quick(root, contract))
    issues.extend(_validate_known_drift(root))
    issues.extend(_validate_templates(root, contract))
    issues.extend(_validate_bundles(root, contract))
    return issues


def _print_issues(issues, as_json):
    if as_json:
        print(json.dumps([asdict(item) for item in issues], ensure_ascii=False, indent=2))
        return
    if not issues:
        print("context-v3 check: PASS")
        return
    for item in issues:
        location = f" [{item.path}]" if item.path else ""
        print(f"{item.code}{location}: {item.message}")
    print(f"context-v3 check: FAIL ({len(issues)} issues)")


def main(argv=None):
    parser = argparse.ArgumentParser(description="Deterministic context v3 contract checker")
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--contract", type=Path)
    parser.add_argument(
        "--rule",
        choices=("release", "contract", "root-index", "frozen-quick", "profile", "run", "projection"),
        default="release",
    )
    parser.add_argument("--input", type=Path)
    parser.add_argument("--name")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    contract_path = args.contract or args.repo / "evals" / "context-v3-contract.json"
    contract = load_contract(contract_path)
    if args.rule == "release":
        issues = release_check(args.repo, contract)
    elif args.rule == "contract":
        issues = validate_contract(contract)
    elif args.rule == "root-index":
        issues = validate_root_index(args.repo, contract)
    elif args.rule == "frozen-quick":
        issues = validate_frozen_quick(args.repo, contract)
    elif args.input is None:
        parser.error(f"--input is required for --rule {args.rule}")
    elif args.rule == "run":
        issues = validate_run(json.loads(args.input.read_text(encoding="utf-8")), contract)
    elif args.rule == "profile":
        issues = validate_profile(args.name or args.input.name, args.input.read_text(encoding="utf-8"), contract)
    else:
        issues = validate_projection(args.name or args.input.name, args.input.read_text(encoding="utf-8"), contract)
    _print_issues(issues, args.json)
    return 1 if issues else 0


if __name__ == "__main__":
    sys.exit(main())

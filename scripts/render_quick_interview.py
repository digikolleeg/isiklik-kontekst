#!/usr/bin/env python3
import argparse
import hashlib
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path


GENERATED_ON = "2026-08-19"
ARTIFACT_PATH = "quick-interview.md"
MANIFEST_PATH = "evals/frozen-quick.json"
CONTRACT_PATH = "evals/context-v3-contract.json"
SOURCE_PATHS = (
    "skills/konteksti-looja/SKILL.md",
    "skills/konteksti-looja/references/quick-mode.md",
    "skills/konteksti-looja/references/interview-engine.md",
    "skills/konteksti-looja/references/claims-and-evidence.md",
    "skills/konteksti-looja/references/output-contract.md",
)
REFERENCE_FILENAMES = (
    "quick-mode.md",
    "interview-engine.md",
    "claims-and-evidence.md",
    "output-contract.md",
    "deep-mode.md",
)


@dataclass(frozen=True)
class RenderIssue:
    code: str
    message: str
    path: str = ""


def _sha256(data):
    return hashlib.sha256(data).hexdigest()


def _read_source(repo_root, relative):
    return (Path(repo_root) / relative).read_text(encoding="utf-8").strip()


def _section(text, start, end=None):
    start_at = text.index(start)
    end_at = text.index(end, start_at) if end else len(text)
    return text[start_at:end_at].strip()


def _quick_orchestrator(skill_text):
    intro = _section(skill_text, "# Konteksti-looja", "## Režiimid")
    context_and_rules = _section(skill_text, "## Kontekstikaust", "## Süvarežiim")
    language = _section(skill_text, "## Eesti keele stiil")
    return "\n\n".join((intro, context_and_rules, language))


def _self_contained(text):
    replacements = (
        (
            "See fail on orkestreerija. Detailsed reeglid on `references/` failides. **Loe vajalik reference enne alustamist**, ära tegutse mälu järgi.",
            "See osa annab orkestreerimisreeglid. Kõik vajalikud detailreeglid on selles dokumendis allpool; järgi neid, ära tegutse mälu järgi.",
        ),
        ("Vt `output-contract.md` §1.", "Vt allpool osa „Väljundleping“ §1."),
        ("Vt `output-contract.md` §3.", "Vt allpool osa „Väljundleping“ §3."),
        ("vt `output-contract.md` §3.", "vt allpool osa „Väljundleping“ §3."),
        ("Vt `output-contract.md` §5", "vt allpool osa „Väljundleping“ §5"),
        ("vt `output-contract.md` §4 ja §5", "vt allpool osa „Väljundleping“ §4 ja §5"),
        ("Vt `output-contract.md`.", "Järgi allpool osa „Väljundleping“."),
        ("vt `output-contract.md`.", "vt allpool osa „Väljundleping“."),
        ("Vt `claims-and-evidence.md` §1.", "Vt allpool osa „Väited, tõendid ja kandidaadid“ §1."),
        ("Vt `claims-and-evidence.md` §3.", "Vt allpool osa „Väited, tõendid ja kandidaadid“ §3."),
        ("Vt [output-contract.md](references/output-contract.md) §4.", "Vt allpool osa „Väljundleping“ §4."),
        (
            "Loe enne alustamist: `interview-engine.md`, `claims-and-evidence.md`, `output-contract.md`.",
            "Enne alustamist järgi allpool osi „Intervjuumootor“, „Väited, tõendid ja kandidaadid“ ning „Väljundleping“.",
        ),
        ("Vt `interview-engine.md` §4.", "Vt allpool osa „Intervjuumootor“ §4."),
        ("Vt `interview-engine.md` §5.", "Vt allpool osa „Intervjuumootor“ §5."),
        ("Vt `output-contract.md`.", "Järgi allpool osa „Väljundleping“."),
        (
            "Ühine intervjueerimisloogika. Kiire režiim kasutab seda koos failiga [quick-mode.md](quick-mode.md), süvarežiim koos failiga [deep-mode.md](deep-mode.md). Reeglid on mõlemas režiimis samad; erinevad ainult eelarve ja katvus.",
            "See osa on kiire režiimi intervjueerimisloogika. See null-install artefakt rakendab ainult kiiret režiimi; süvarežiimi juhist siin ei ole.",
        ),
        (
            "Kontroll: `python3 scripts/context_v3_check.py --rule profile --input <fail> --name <failinimi>`.",
            "Null-installis kontrolli enne salvestamist käsitsi: iga fence'ist väljaspool rea alguse `- ` kannab claim-kommentaari.",
        ),
        (
            "Ülendatud kandidaat **tuleb** eemaldada, muidu ta dubleerub järgmisel jooksul. Vt `deep-mode.md` §7.",
            "Kiire režiim kandidaati ei ülenda. Jäta see registrisse; hilisem süvarežiim eemaldab rea ülendamise järel, et kandidaat ei dubleeruks.",
        ),
        (
            "| `target_section` | täpne sektsiooni-ID `deep-mode.md` omandiregistrist; kui register pole selles töörežiimis kaasas või sobiv koht pole üheselt selge, `määramata` |",
            "| `target_section` | null-installis `määramata`; hilisem süvarežiim võib selle oma omandiregistri järgi täpsustada |",
        ),
        (
            "Süvarežiimi sektsioonijaotus on **lukus**. Installitud Skilli omandiregister on failis [deep-mode.md](deep-mode.md) §5 ja see on ainus lubatud allikas.\n\n1. Kui register on loetud ja annab üheselt sobiva sektsiooni, kirjuta täpne sektsiooninimi.\n2. Kui sobivaid on mitu, ükski ei sobi või kasutad null-installi kiire intervjuu faili, kus registrit pole kaasas, kirjuta `target_section: määramata`.",
            "Süvarežiimi sektsioonijaotus on **lukus**. Null-installis pole süva omandiregistrit kaasas: kirjuta iga kandidaadi `target_section` väärtuseks `määramata`. Hilisem süvarežiim võib selle oma registri järgi täpsustada.",
        ),
        (
            "Külvamine ei anna kiirele režiimile omandit. Kiire režiim kirjutab need sektsioonid esimest korda; **hilisemad muudatused teeb sektsiooni omanik**, vt [deep-mode.md](deep-mode.md) §5. Ankrut ei tohi kustutada, sest omandireegel seisab selle peal.",
            "Külvamine ei anna kiirele režiimile omandit. Kiire režiim kirjutab need sektsioonid esimest korda; **hilisemad muudatused teeb ankrus märgitud omanikmoodul**. Ankrut ei tohi kustutada, sest omandireegel seisab selle peal.",
        ),
        (
            "### Fail puudub: loo täielik ankruskelett\n\nÄra loo faili, kus on ainult need sektsioonid, mida sa parasjagu täitsid. Loo **kõik selle faili sektsioonid** omandiregistri järgi, vt [deep-mode.md](deep-mode.md) §5.\n\n1. Frontmatter (§1).\n2. Iga sektsioon registri järjekorras: ankur koos omanikuga, siis pealkiri.\n3. Sinu enda sektsioonid täidad sisuga.\n4. **Võõrad sektsioonid jäävad nähtavalt katmata** (§3), koos märkega, milline moodul need täidab.\n\n```\n<!-- section: responsibilities | owner: A -->\n## Vastutused\n\n<!-- katmata: kuulub moodulile A -->\nVeel katmata. Ütle \"süvaintervjuu\" ja vali moodul A.\n```\n\nPõhjus: skelett teeb faili kohe jätkatavaks. Järgmine moodul leiab oma ankru eest ja kirjutab õigesse kohta, selle asemel et arvata, kuhu sektsioon käib.",
            "### Fail puudub: loo quicki täielik ankruskelett\n\nNull-installi kiires režiimis tähendab täielik ankruskelett ainult §4 all vastava faili kohta loetletud ankruid. Süvamooduli puuduvaid ankruid ära leiuta ega küsi välisest registrist.\n\n1. Lisa frontmatter (§1).\n2. Lisa kõik §4 all selle faili kohta loetletud ankurd ja pealkirjad sealses järjekorras.\n3. Täida tõendiga kaetud quick-sektsioonid.\n4. Jäta katmata quick-väljad nähtavaks (§3).\n\nNii jääb null-installi väljund täielik quicki jaoks, kuid ei teeskle kaasamata süva-omandiregistrit.",
        ),
        (
            "### Fail puudub: loo õige ankruskelett\n\nRežiimid teavad eri palju ja loovad skeleti erinevalt:\n\n- **Kiire režiim:** loo neli väljundfaili §4 tabelites loetletud ankrutega. Need tabelid on null-installi failis täielikult kaasas; süvarežiimi omandiregistrit pole vaja avada.\n- **Süvarežiim:** loo kõik selle faili sektsioonid omandiregistri järgi, vt [deep-mode.md](deep-mode.md) §5. Nii leiab järgmine moodul ka oma ankru eest.\n\n1. Frontmatter (§1).\n2. Iga valitud skeleti sektsioon õiges järjekorras: ankur koos omanikuga, siis pealkiri.\n3. Sinu enda sektsioonid täidad sisuga.\n4. Süvarežiimi täisskeletis jäävad **võõrad sektsioonid nähtavalt katmata** (§3), koos märkega, milline moodul need täidab.\n\n```\n<!-- section: responsibilities | owner: A -->\n## Vastutused\n\n<!-- katmata: kuulub moodulile A -->\nVeel katmata. Ütle \"süvaintervjuu\" ja vali moodul A.\n```\n\nPõhjus: skelett teeb faili kohe jätkatavaks. Järgmine moodul leiab oma ankru eest ja kirjutab õigesse kohta, selle asemel et arvata, kuhu sektsioon käib.",
            "### Fail puudub: loo quicki täielik ankruskelett\n\nNull-installi kiires režiimis tähendab täielik ankruskelett ainult §4 all vastava faili kohta loetletud ankruid. Süvamooduli puuduvaid ankruid ära leiuta ega küsi välisest registrist.\n\n1. Lisa frontmatter (§1).\n2. Lisa kõik §4 all selle faili kohta loetletud ankurd ja pealkirjad sealses järjekorras.\n3. Täida tõendiga kaetud quick-sektsioonid.\n4. Jäta katmata quick-väljad nähtavaks (§3).\n\nNii jääb null-installi väljund täielik quicki jaoks, kuid ei teeskle kaasamata süva-omandiregistrit.",
        ),
        (
            "2. Sisuga sektsiooni **muudad ainult siis, kui oled selle omanik**, ja siis näitad enne diffi, vt `deep-mode.md` §6.",
            "2. Sisuga sektsiooni kiire režiim ei muuda: näita võimalikku muudatust kasutajale ja jäta leid kandidaadiregistrisse.",
        ),
        (
            "3. Sisuga sektsiooni **muudad ainult siis, kui oled selle omanik**, ja siis näitad enne diffi, vt `deep-mode.md` §6.",
            "3. Sisuga sektsiooni kiire režiim ei muuda: näita võimalikku muudatust kasutajale ja jäta leid kandidaadiregistrisse.",
        ),
    )
    for old, new in replacements:
        text = text.replace(old, new)
    return text


def _assert_zero_install(text):
    without_markers = re.sub(r"(?m)^<!-- source: .* -->$", "", text)
    leaked = [name for name in REFERENCE_FILENAMES if name in without_markers]
    if leaked:
        raise ValueError(f"external reference leaked into zero-install artifact: {', '.join(leaked)}")
    if "scripts/context_v3_check.py" in text:
        raise ValueError("local checker command leaked into zero-install artifact")


def render_artifact(repo_root):
    repo_root = Path(repo_root)
    skill = _self_contained(_quick_orchestrator(_read_source(repo_root, SOURCE_PATHS[0])))
    parts = [
        f"""# Kiire konteksti-intervjuu

## Kasutamine

Kopeeri kogu see fail uude vestlusse ja lisa lõppu: **„kiire intervjuu“** või **„töötoa intervjuu“**. Juhis on iseseisev: selle kasutamiseks pole vaja paigaldada sõltuvusi ega avada siin nimetatud lähtefaile.

Intervjueerija järgib allpool olevaid osi nende esitamise järjekorras. Lähtefailide markerid on ainult päritolu ja driftikontrolli jaoks.

<!-- generated-on: {GENERATED_ON}; generator: scripts/render_quick_interview.py -->""",
        f"<!-- source: {SOURCE_PATHS[0]} | selection: quick-orchestrator -->\n\n{skill}",
    ]
    for relative in SOURCE_PATHS[1:]:
        parts.append(f"<!-- source: {relative} -->\n\n{_self_contained(_read_source(repo_root, relative))}")
    rendered = "\n\n---\n\n".join(parts).rstrip() + "\n"
    _assert_zero_install(rendered)
    return rendered.encode("utf-8")


def build_manifest(repo_root, artifact):
    repo_root = Path(repo_root)
    sources = []
    for relative in SOURCE_PATHS:
        entry = {"path": relative, "sha256": _sha256((repo_root / relative).read_bytes())}
        if relative == SOURCE_PATHS[0]:
            entry["selection"] = "quick-orchestrator"
        else:
            entry["selection"] = "full"
        sources.append(entry)
    return {
        "schema_version": 1,
        "path": ARTIFACT_PATH,
        "algorithm": "sha256",
        "sha256": _sha256(artifact),
        "generated_on": GENERATED_ON,
        "generator": "scripts/render_quick_interview.py",
        "sources": sources,
    }


def write_artifact(repo_root):
    repo_root = Path(repo_root)
    artifact = render_artifact(repo_root)
    manifest = build_manifest(repo_root, artifact)
    (repo_root / ARTIFACT_PATH).write_bytes(artifact)
    manifest_path = repo_root / MANIFEST_PATH
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return manifest


def check_artifact(repo_root):
    repo_root = Path(repo_root)
    artifact_path = repo_root / ARTIFACT_PATH
    manifest_path = repo_root / MANIFEST_PATH
    contract_path = repo_root / CONTRACT_PATH
    issues = []
    expected_artifact = render_artifact(repo_root)
    expected_manifest = build_manifest(repo_root, expected_artifact)

    if not artifact_path.is_file():
        issues.append(RenderIssue("artifact_missing", "quick artifact is missing", str(artifact_path)))
        actual_artifact = b""
    else:
        actual_artifact = artifact_path.read_bytes()
        if actual_artifact != expected_artifact:
            issues.append(RenderIssue("artifact_drift", "quick artifact differs from deterministic render", str(artifact_path)))

    try:
        actual_manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        issues.append(RenderIssue("manifest_invalid", f"frozen manifest is missing or invalid: {error}", str(manifest_path)))
        actual_manifest = {}

    if actual_manifest.get("sources") != expected_manifest["sources"]:
        issues.append(RenderIssue("source_drift", "source paths or hashes differ from frozen manifest", str(manifest_path)))
    manifest_without_sources = {key: value for key, value in actual_manifest.items() if key != "sources"}
    expected_without_sources = {key: value for key, value in expected_manifest.items() if key != "sources"}
    if manifest_without_sources != expected_without_sources:
        issues.append(RenderIssue("manifest_drift", "manifest metadata or artifact hash differs from render", str(manifest_path)))
    if actual_manifest.get("sha256") != _sha256(actual_artifact):
        issues.append(RenderIssue("artifact_hash", "manifest SHA-256 does not match artifact bytes", str(artifact_path)))

    try:
        contract = json.loads(contract_path.read_text(encoding="utf-8"))
        published = contract["frozen_quick"]["published_sha256"]
    except (OSError, json.JSONDecodeError, KeyError, TypeError) as error:
        issues.append(RenderIssue("contract_invalid", f"contract freeze field is missing or invalid: {error}", str(contract_path)))
    else:
        if published != expected_manifest["sha256"]:
            issues.append(RenderIssue("contract_drift", "contract published SHA-256 differs from deterministic render", str(contract_path)))
    return issues


def _print_issues(issues):
    for item in issues:
        location = f" [{item.path}]" if item.path else ""
        print(f"{item.code}{location}: {item.message}")


def main(argv=None):
    parser = argparse.ArgumentParser(description="Render or verify the frozen zero-install quick interview")
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--write", action="store_true", help="render artifact and source manifest")
    action.add_argument("--check", action="store_true", help="fail if artifact, sources, manifest or contract drift")
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args(argv)
    if args.write:
        manifest = write_artifact(args.repo)
        print(f"wrote {manifest['path']} sha256={manifest['sha256']}")
        return 0
    issues = check_artifact(args.repo)
    if issues:
        _print_issues(issues)
        return 1
    print("frozen quick: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())

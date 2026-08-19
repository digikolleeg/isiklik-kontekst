# CLAUDE.md

See fail annab Claude Code'le (claude.ai/code) suuniseid, kui ta selles repos koodiga töötab.

## Mis see repo on

Kaks teineteist täiendavat süsteemi ühes repos:

1. **Portfoolio** (`portfolio/`) — struktureeritud markdown-failide kogum, mis kirjeldab, kes kasutaja on. Staatiline kontekst, mis süstitakse AI süsteemipromptidesse. Uuendatakse kord kvartalis.
2. **Wiki** (`raw/` + `wiki/`) — kasvav teadmiste baas, mida sa hooldad allikate sissekandmisega. Dünaamiline, kasvab pidevalt. Sa kirjutad kogu sisu; kasutaja ainult loeb.

Loe mõlemad kihid läbi, enne kui midagi teed. Portfoolio ütleb, kellega töötad. Wiki ütleb, mida ta on kogunud.

---

## Portfoolio kiht

### Struktuur

```
portfolio/
├── templates/          ← tühjad šabloonid koos intervjuu-protokollidega
├── examples/           ← täidetud näited eeskujuks
└── interview-protocol/
    └── agent-system-prompt.md  ← intervjueerija-agendi täielik süsteemiprompt
```

Kasutaja tegelikud täidetud portfoolio-failid võivad asuda otse `portfolio/` all (mitte `templates/` või `examples/` sees).

### Millal portfoolio-faile uuendada

- Kui kasutaja ütleb, et projekt, roll, prioriteet või muu oluline on muutunud
- Kvartalivaate ajal ("uuendame portfooliot")
- Kui wiki toob esile info, mis on vastuolus portfoolio failiga või laiendab seda

### Kuidas uuendada

Loe olemasolev fail enne läbi. Tee sihitud muudatused — ära kirjuta üle, kui kasutaja seda eraldi ei palu. Pärast uuendamist lisa kanne `log.md` faili:

```
## [YYYY-MM-DD] portfolio-update | <failinimi>
Updated: <ühelauseline kirjeldus, mis muutus ja miks>
```

---

## Wiki kiht

### Struktuur

```
raw/        ← muutmatud allikdokumendid. Ära kunagi muuda neid.
wiki/       ← sinu pärusmaa. Loed ja hooldad siin kõike.
index.md    ← kõigi wiki-lehtede kataloog. Uuenda iga operatsiooni järel.
log.md      ← ainult lisamiseks. Iga sissekanne, päring ja kontroll saab oma kande.
```

### Wiki-lehe konventsioonid

Iga wiki-leht peaks sisaldama:
- `# Pealkiri` ülaservas
- Üks lõik kokkuvõtet kohe pealkirja all
- `## Connections` sektsioon, kus on seotud lehed `[[wiki/page-name]]` linkidena
- `## Sources` sektsioon, kus on loetletud toored allikad, millest see leht ammutab

Kasuta `wiki/` sees alamkaustu, et tüübi järgi organiseerida: `wiki/entities/`, `wiki/concepts/`, `wiki/topics/`, `wiki/syntheses/`.

### Operatsioonid

#### Sissekanne (Ingest)

Kui kasutaja paneb allika `raw/` kausta ja palub selle sisse kanda:

1. Loe allikas täielikult läbi.
2. Aruta peamised tähelepanekud kasutajaga, kui ta tahab kaasatud olla; muidu liigu edasi.
3. Kirjuta kokkuvõtte-leht `wiki/topics/` alla või sinna, kuhu sobib.
4. Loo või uuenda entiteedi-lehed (`wiki/entities/`) inimeste, organisatsioonide ja toodete kohta, keda on mainitud.
5. Loo või uuenda mõiste-lehed (`wiki/concepts/`) ideede või raamistike kohta, mis on tutvustatud.
6. Ühenda uued ja olemasolevad lehed ristviidetega.
7. Uuenda `index.md` — lisa uued lehed kataloogi, uuenda allika-loendid.
8. Lisa kanne `log.md` faili:

```
## [YYYY-MM-DD] ingest | <allika pealkiri>
File: raw/<failinimi>
Pages created: <loend>
Pages updated: <loend>
Key takeaways: <2-3 punkti>
```

Üks allikas puudutab tüüpiliselt 5–15 wiki-lehte.

#### Päring (Query)

Kui kasutaja esitab küsimuse:

1. Loe `index.md`, et leida asjakohased lehed.
2. Loe need lehed ja järgi nende `## Connections` linke, kui vaja.
3. Sünteesi vastus koos viidetega wiki-lehtedele.
4. Kui vastus on sisukas ja taaskasutatav, paku see uue wiki-lehena `wiki/syntheses/` kausta panna.
5. Lisa kanne `log.md` faili:

```
## [YYYY-MM-DD] query | <küsimuse lühikokkuvõte>
Answer filed: wiki/syntheses/<failinimi> (või: not filed)
```

#### Kontroll (Lint)

Kui kasutaja palub wiki tervisekontrolli:

1. Skanni kõiki lehti, et leida: vastuolusid lehtede vahel, vananenud väiteid, mida uuemad allikad on asendanud, orvuks jäänud lehti (sissetulevaid linke pole), mõisteid, mida on mainitud, aga oma lehte pole, puuduvaid ristviiteid.
2. Anna leiud tüübi järgi rühmitatuna teada.
3. Küsi kasutajalt, mis tuleks parandada, ja paranda need.
4. Paku uusi allikaid või küsimusi, mis täidaksid leitud tühimikke.
5. Lisa kanne `log.md` faili:

```
## [YYYY-MM-DD] lint
Issues found: <arv>
Issues fixed: <arv>
Suggestions: <loend>
```

---

## Indeksi ja logi konventsioonid

**`index.md`** — sisule orienteeritud. Üks rida wiki-lehe kohta. Hoia kategooriad puhtad: Entities, Concepts, Topics, Syntheses, Sources. Uuenda iga sissekande või kontrolli järel.

**`log.md`** — kronoloogiline, ainult lisamiseks. Kõige uuem kanne esimene. Iga kanne algab `## [YYYY-MM-DD] <operation> | <title>` vorminguga. Ära kunagi muuda vanu kandeid.

---

## Mida mitte teha

- Ära kunagi muuda faile `raw/` kaustas. Need on muutmatu tõe-alus.
- Ära kunagi kirjuta portfoolio-faile palumata nullist. Tee olemasolevatesse sihitud muudatusi.
- Ära lase wiki-lehtedel vananeda ilma seda märkimata. Kui tead, et lehe väide on asendatud, märgi see kohe lehe sees.
- Ära lase `index.md` sünkroonist välja triivida. Uuenda seda iga operatsiooni järel, mis wiki-lehti puudutab.

---

## Digikolleeg fork notes

This is the Estonian translation of `iHeigo/personal-context-portfolio`, published as `digikolleeg/isiklik-kontekst`. It serves two purposes:

1. The Estonian public fork — what attendees clone in the Digikolleeg incubator AI workshops.
2. The upstream for Heigo's own private vault (`iHeigo/digikolleeg-kontekst`, cloned at `~/Projects/digikolleeg-kontekst/`). Heigo uses the same setup as attendees do.

### Dual-clone setup

Heigo never commits personal portfolio content to this public repo. His real content lives in the private fork. The two clones share `upstream = digikolleeg/isiklik-kontekst` but have different `origin` remotes. **Never push from the private clone to this public fork.** See `~/Projects/workshop/docs/decisions/2026-05-27-dual-clone-for-personal-vault.md` for the full rationale.

### konteksti-looja Skill

- Lives at `skills/konteksti-looja/`
- Installation: see that folder's `README.md`
- Quick mode: say *"töötoa intervjuu"* or *"kiire intervjuu"* — exactly four files in this order (`identity.md`, `current-projects.md`, `communication-style.md`, `writing-samples.md`), 30–40 min
- Deep mode: four resumable modules (A töö-tegelikkus, B turg-ja-ekspertiis, C otsused-ja-piirid, D hääl-ja-inimesed) covering the full 9 profiles + 2 evidence files. Not "after the workshop" — it reads existing files and extends them.
- Contract and section ownership: `evals/context-v3-contract.json`; human-readable map: `portfolio/context-map.md`

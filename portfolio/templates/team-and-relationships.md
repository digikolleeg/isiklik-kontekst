---
name: team-and-relationships
description: Olulised inimesed kasutaja ümber, suhted ja kuidas suhtlevad
layer: profile
type: portfolio
updated: <YYYY-MM-DD>
review_after: <YYYY-MM-DD>
sensitivity: restricted
tags: [portfolio]
---

# Team and Relationships

## Mille jaoks see fail on

Olulised inimesed sinu töö ümber ja kuidas sa nendega suhtled. Agendid kasutavad seda, et valmistada ette koosolekuid, koostada suhtlust ja mõista su töö inimlikku konteksti. Agent, kes valmistab ette su üks-ühele kohtumist, peab teadma, kes on inimene laua taga, mis teda huvitab ja mida te teineteiselt vajate.

---

## Intervjuu-protokoll

*Anna see fail tervikuna oma AI ehituspartnerile ja ütle "alustame sellega". Su ehituspartner peaks lugema allolevad juhised ja viima läbi intervjuu.*

**Juhised ehituspartnerile:** sa aitad kasutajal koostada tema team and relationships faili. Saa kõigepealt oluliste inimeste nimekiri, seejärel liigu igaüks läbi. Kasuta seda, mida tead eelmistest failidest — kui kasutaja mainis koostööpartnereid projektide või role-intervjuus, viita neile, mitte ära küsi uuesti.

**Küsimused:**

1. Kes on 5–8 inimest, kellega sa oma töös kõige rohkem suhtled? Anna nimed ja rollid.
2. [Iga inimese kohta:] Mis on su töösuhe [nimega]? Kuidas te tüüpiliselt suhtlete — koosolekud, Slack, email?
3. Mida [nimi] sinult vajab ja mida sina temalt vajad?
4. Kas on midagi, mida sinu nimel tegutsev AI peaks teadma, kui ta selle inimesega tegeleb või suhtluseks valmistub? Stiili eelistused, asjad, millega olla ettevaatlik, kontekst, mis loeb?

**Millal piisab:** kui oled iga nimetatud inimese läbi käinud.

**Pärast koostamist:** näita mustandit. Palu kasutajal kontrollida, kas dünaamika tundub õige — "mida nemad sinult vajavad" ja "mida sina neilt vajad" sektsioonid on need, kus on päris väärtus ja nendega on lihtne pisut puusse panna.

---

## Väljundi struktuur

**Väitemärgised.** Iga loendirida (`- `) selles failis kannab lõpus masinloetavat märget:

`- <väide> <!-- claim: status=<staatus>; evidence=<allikas>:<vaatlus>,... -->`

| Staatus | Millal | Mida märge nõuab |
|---|---|---|
| `kinnitatud` | kasutaja sõnastas selle ise üldreeglina | `basis=user-stated` |
| `toetatud` | muster, mida katab vähemalt **kaks sõltumatut** allikas | `evidence=` kahe eri `<allikas>` osaga |
| `kandidaat` | üks vaatlus või oletus | `evidence=` ühe ID-ga |

Sõltumatust loetakse `<allikas>` järgi. **Allikas on üks konkreetne artefakt või olukord** — üks e-kiri, üks postitus, üks otsusejuhtum. Kaks vaatlust *samast* e-kirjast on üks allikas ja ei ülenda midagi. Kaks *eri* e-kirja on kaks allikat ja ülendavad, ka siis kui kanal on sama.

**Allika ID nimetab konkreetset asja, mitte kategooriat.** Leping keelab üldnimed: `email`, `linkedin`, `channel`, `document`, `message`, `situation`, `interview`. `sample-01` ja `dl-hinnamuutus` on lubatud; `email` ja `message` ei ole. Kategooria-ID lubaks kaks vaatlust ühest kirjatükist esitleda kahe sõltumatu allikana.

**Iga rida, mis algab `- `, peab kandma märget.** Kui loetelu ei ole väidete loetelu (näiteks vaatlused ühe juhtumi sees), vormista ta tabelina, mitte loendina. Kandidaat ei lähe projektsiooni; ta kantakse `portfolio/_candidates.md` ledgerisse. Vormingut kontrollib `scripts/context_v3_check.py --rule profile`.

**Sektsioonimärgised.** `<!-- section: <id> -->` read on sektsioonitasandi omandi ankrud. Ära kustuta neid: nende peal seisab reegel, et süvarežiimi moodul kirjutab ainult oma sektsiooni ega kirjuta teise mooduli oma üle.

**`review_after`.** Süvarežiim loeb selle avangus. Kui kuupäev on möödas, küsib ta enne uute küsimuste juurde liikumist selle faili üle. Ilma selle tarbijata oleks väli mõttetu metaandme.

Märgise `owner` väli ütleb, milline süvarežiimi moodul seda sektsiooni **omab**. Teine moodul võib sama teema jutuks võtta, aga tema leid läheb `portfolio/_candidates.md` ledgerisse, mitte otse siia. Nii ei kirjuta kaks moodulit teineteist üle.

**See fail on `restricted`.** Ta sisaldab hinnanguid nimeliste kolmandate isikute kohta. Ta ei lähe ühessegi projektsiooni, mille `sensitivity` on `exportable`. Kui sa kleebid ta bundle'isse, muutub see bundle `restricted`-iks ja seda ei tohi anda agendile, mis kirjutab väljapoole.

```markdown
---
name: team-and-relationships
description: Olulised inimesed kasutaja ümber, suhted ja kuidas suhtlevad
layer: profile
type: portfolio
updated: <YYYY-MM-DD>
review_after: <YYYY-MM-DD>
sensitivity: restricted
tags: [portfolio]
---

# Tiim ja suhted

<!-- section: people | owner: D -->
## Inimesed

[Korda seda plokki iga olulise inimese kohta.]

### [Nimi]

- **Roll:** [Tema ametinimetus või roll.] <!-- claim: status=kinnitatud; basis=user-stated -->
- **Suhe:** [Juht / Alluv / Kolleeg / Klient / Koostööpartner / Sidusrühm] <!-- claim: status=kinnitatud; basis=user-stated -->
- **Kuidas me suhtleme:** [Regulaarsed üks-ühele, asünkroonne Slack, projektipõhine, juhtum-juhult. Lisa rütm, kui regulaarne.] <!-- claim: status=kinnitatud; basis=user-stated -->

<!-- section: relationship-context | owner: D -->
## Suhte kontekst

[Iga inimese kohta: mida ta minult vajab ja mida ma temalt vajan. Siia käib ka see, mis suhtes on hapram või milline ajalugu mõjutab tänast tooni.]

### [Nimi]

- **Mida ta minult vajab:** [Mille pärast ta sinust sõltub.] <!-- claim: status=kinnitatud; basis=user-stated -->
- **Mida ma temalt vajan:** [Mille pärast sa temast sõltud.] <!-- claim: status=kinnitatud; basis=user-stated -->

<!-- section: agent-guidance | owner: D -->
## Kontekst agentidele

[Reeglid, mida AI peab järgima, kui ta valmistab ette kohtumist või kirjutab kellelegi siit nimekirjast — tema suhtlemisstiil, eelistused, tundlikkused, töömustrid.]

Need read on agendile **reeglid, mitte taust**. Kui rida ütleb "ei loe pikki kirju", siis pikk kiri on ebaõnnestunud mustand.
```

---
name: role-and-responsibilities
description: Kasutaja roll, vastutused, rütmid, mida ta toodab
layer: profile
type: portfolio
updated: <YYYY-MM-DD>
review_after: <YYYY-MM-DD>
sensitivity: exportable
tags: [portfolio]
---

# Role and Responsibilities

## Mille jaoks see fail on

See on operatiivne kirjeldus sinu tööst — kuidas su nädalad päriselt välja näevad, mille eest sa vastutad, mida sa toodad. Agendid kasutavad seda faili, et mõista su töö rütmi ja kuju, nii et nad oskaksid õigetel hetkedel õigete asjadega aidata. See pole ametijuhend. See on praktiline kirjeldus sellest, kuidas sa oma päevi päriselt veedad.

---

## Intervjuu-protokoll

*Anna see fail tervikuna oma AI ehituspartnerile ja ütle "alustame sellega". Su ehituspartner peaks lugema allolevad juhised ja viima läbi intervjuu.*

**Juhised ehituspartnerile:** sa aitad kasutajal koostada tema role and responsibilities faili. See peaks tabama töö operatiivset reaalsust, mitte ideaalseid versioone. Esita küsimused üks korraga. Kasuta seda, mida sa juba identity-failist tead (kui see on täidetud), et üleliigseid küsimusi vältida ja paremaid täpsustavaid küsimusi esitada.

**Küsimused:**

1. Kirjelda tüüpilist nädalat. Mis on need korduvad asjad, mis juhtuvad iga nädal ilma erandita?
2. Mille eest sa otseselt vastutad — mis on need asjad, kus kui need ei juhtu siis on see sinu jama?
3. Milliseid otsuseid sa regulaarselt teed? Mitte suuri strateegilisi — neid igapäevaseid, mis iga nädal ette tulevad.
4. Mida sa toodad? Raporteid, analüüse, plaane, koodi, esitlusi, postitusi — mis on su töö päriselt väljundid?
5. Kellele sa allud? Kes allub sulle, kui keegi?
6. Kas on igakuiseid või kvartali rütme, mis sinu tööd kujundavad — planeerimistsükleid, ülevaateid, nõukogu koosolekuid, midagi sellist?

**Millal piisab:** pärast 4–6 küsimust. See fail on keskmise pikkusega. Püüa kinni operatiivne reaalsus, mitte iga erijuhtum.

**Pärast koostamist:** näita mustandit ja palu kasutajal välja tuua, mis ei kõla õigesti. Pööra eriti tähelepanu, kas rütmid ja tsüklid on täpsed — inimesed unustavad sageli korduvad kohustused, kuni vaatavad ülevaadet ning näevad puuduolevaid sektsioone.

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

```markdown
---
name: role-and-responsibilities
description: Kasutaja roll, vastutused, rütmid, mida ta toodab
layer: profile
type: portfolio
updated: <YYYY-MM-DD>
review_after: <YYYY-MM-DD>
sensitivity: exportable
tags: [portfolio]
---

# Roll ja vastutused

<!-- section: responsibilities | owner: A -->
## Põhivastutused

[Mille eest sa vastutad — asjad, mis on ainult sinu laual.]

<!-- section: decisions | owner: A -->
## Olulised otsused

[Otsuste **tüübid**, mis regulaarselt sinu laualt läbi käivad ja sinu otsustusvõimet vajavad. Siia käib otsustusõiguse kaart, mitte üksikjuhtumid.]

Päris otsusejuhtumid — mis oli laual, mille vahel valisid, kuidas jõudsid — käivad tõendifaili `decision-log.md`. See on sama vahe mis `communication-style` ja `writing-samples` vahel: siin reegel, seal tõend.

<!-- section: rhythms | owner: A -->
## Rütmid

**Nädal:** [Korduvad koosolekud, tähtajad, rituaalid. Tüüpilise nädala skelett.]

**Kuu / kvartal:** [Planeerimistsüklid, ülevaated, aruandlusperioodid, sesoonsed mustrid.]

<!-- section: outputs | owner: A -->
## Mida ma toodan

[Su väljundid — tulemused, artefaktid, raportid, plaanid, kood, artiklid. Mida iganes sa oma töö raames loob.]

<!-- section: reporting | owner: A -->
## Aruandluse struktuur

[Kellele sa allud, kes allub sulle. Hoia lihtne — nimed ja rollid.]

Kui inimeste kohta on rohkemat kui nimi ja roll, käib see `team-and-relationships.md` faili, mis on `restricted`. Siia jäävad ainult struktuurifaktid.
```

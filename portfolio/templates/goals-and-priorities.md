---
name: goals-and-priorities
description: Mida kasutaja optimeerib, plaanid, kompromissid, mida teadlikult ei tee
layer: profile
type: portfolio
updated: <YYYY-MM-DD>
review_after: <YYYY-MM-DD>
sensitivity: exportable
tags: [portfolio]
---

# Goals and Priorities

## Mille jaoks see fail on

Mida sa hetkel optimeerid — sel kvartalil, sel aastal ja pikemas plaanis. Agendid kasutavad seda, et osata otsuseid ja soovitusi õigesti kaaluda. Agent, kes teab, et praegu on kiirus olulisem kui lihvitus, annab sulle teistsugust nõu kui agent, kes arvab, et optimeerid puhtale kvaliteedile. Samuti paneb see fail kirja, mida sa teadlikult EI TEE, ja see on täpselt sama oluline.

---

## Intervjuu-protokoll

*Anna see fail tervikuna oma AI ehituspartnerile ja ütle "alustame sellega". Su ehituspartner peaks lugema allolevad juhised ja viima läbi intervjuu.*

**Juhised ehituspartnerile:** sa aitad kasutajal koostada tema goals and priorities faili. See keskendub sellele, millele ta optimeerib, mitte tema projektide nimekirjale (selleks on teine fail). Tõmba selge piir eesmärkide ja projektide vahele, kui kasutaja hakkab lihtsalt ülesandeid loetlema. Kasuta varasematest failidest õpitut, et küsida tabavamaid täpsustusi.

**Küsimused:**

1. Mida sa lähikuudel saavutada proovid? Mitte su projektide nimekiri — sinu eesmärgid. Milline näeb välja edukas tulemus selle kvartali või hooaja lõpus?
2. Mis on pikem plaan — see aasta või paar järgmist? Mille poole sa rühid?
3. Kui pead tegema kompromisse — kiirus vs kvaliteet, lühiajaline vs pikaajaline, kasv vs stabiilsus, siis kuhu sa tavaliselt maandud?
4. Mida sa praegu teadlikult prioriteediks EI SEAKSKI, isegi kui see on oluline? Mille sa oled meelega ootele pannud?
5. Kui järgmised kuus kuud lähevad hästi, mis on sinu töös või elus teistmoodi?

**Millal piisab:** Pärast 4–5 küsimust.

**Pärast koostamist:** Näita mustandit. Palu kasutajal üle kontrollida, kas kompromisside eelistused tunduvad õiged — need on selles failis kõige suurema mõjuga read, sest need dikteerivad otse, kuidas agendid sulle soovitusi hakkavad andma.

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
name: goals-and-priorities
description: Mida kasutaja optimeerib, plaanid, kompromissid, mida teadlikult ei tee
layer: profile
type: portfolio
updated: <YYYY-MM-DD>
review_after: <YYYY-MM-DD>
sensitivity: exportable
tags: [portfolio]
---

# Eesmärgid ja prioriteedid

<!-- section: current-goals | owner: C -->
## Praegused eesmärgid

[Mida sa lähiajal saavutada püüad — see kvartal või tööhooaeg. Konkreetsed tulemused, mitte lihtsalt unistused.]

<!-- section: long-term-goals | owner: C -->
## Pikemaajalised eesmärgid

[See aasta või lähiaastad. Mille suunas sa ehitad. Kuhu sa jõuda tahad.]

<!-- section: tradeoffs | owner: C -->
## Kuidas ma kompromisse näen

[Su vaikimisi positsioonid tüüpiliste kompromisside puhul — kiirus vs kvaliteet, kasv vs stabiilsus, lühiajaline vs pikaajaline, laius vs sügavus. Kuhu sa kaldud, kui pead valima.]

Need read on failis kõige suurema mõjuga, sest nad dikteerivad otse, kuidas agendid sulle soovitusi annavad. Kui rida on `kandidaat`, ei tohi agent selle peale tugevat soovitust ehitada.

<!-- section: non-goals | owner: C -->
## Mis EI OLE praegu prioriteet

[Asjad, mis on tähtsad, aga teadlikult ootele pandud. Asjad, millega oled otsustanud praegu mitte tegeleda, et agendid ei käiks sulle nendega pinda.]

<!-- section: success-criteria | owner: C -->
## Milline näeb välja edu

[Kui järgmised kuus kuud lähevad hästi, mis siis muutub? Maali pilt, et agendid saaksid aru, mille nimel sa töötad.]
```

---
name: tools-and-systems
description: Igapäeva tööriistad, andmeallikad, integratsioonid, mida väldib
layer: profile
type: portfolio
updated: <YYYY-MM-DD>
review_after: <YYYY-MM-DD>
sensitivity: exportable
tags: [portfolio]
---

# Tools and Systems

## Mille jaoks see fail on

Mida sa kasutad, kuidas see on seadistatud ja mis millega ühenduses on. Agendid kasutavad seda, et soovitada töövooge, mis su päris tööriistakomplekti sobivad, vältida juba kõrvale jäetud tööriistade soovitamist ja mõista, kus su andmed elavad. Kui agent hakkab sind aitama midagi ehitada, peab ta teadma, mille peale ta ehitab.

---

## Intervjuu-protokoll

*Anna see fail tervikuna oma AI ehituspartnerile ja ütle "alustame sellega". Su ehituspartner peaks lugema allolevad juhised ja viima läbi intervjuu.*

**Juhised ehituspartnerile:** sa aitad kasutajal koostada tema tools and systems faili. See peab olema praktiline ülevaade tema töökeskkonnast, mitte ammendav nimekiri igast telefoni rakendusest. Keskendu tööriistadele, mis kujundavad, kuidas ta päevast päeva töötab.

**Küsimused:**

1. Milliseid tööriistu ja platvorme sa iga päev kasutad? Käi läbi oma põhi-stack.
2. Kuidas su seadistus on kohandatud? On konkreetseid konfiguratsioone, integratsioone või töövooge, mida agent peaks teadma?
3. Kus su oluline andmestik elab — dokumendid, tabelid, andmebaasid, konkreetsed platvormid?
4. On tööriistu, mida sa parasjagu hindad või plaanid kasutusele võtta?
5. On midagi, mida sa oled proovinud ja teadlikult kõrvale jätnud? Mis ei töötanud?

**Millal piisab:** pärast 4–5 küsimust. Hoia praktiline.

**Pärast koostamist:** näita mustandit. Küsi kasutajalt, kas igapäeva tööriistade nimekirjast on midagi olulist puudu — inimesed unustavad sageli mainida asju, mida nad nii harjumuspäraselt kasutavad, et ei mõtle neist enam kui tööriistadest.

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
name: tools-and-systems
description: Igapäeva tööriistad, andmeallikad, integratsioonid, mida väldib
layer: profile
type: portfolio
updated: <YYYY-MM-DD>
review_after: <YYYY-MM-DD>
sensitivity: exportable
tags: [portfolio]
---

# Tööriistad ja süsteemid

<!-- section: core-stack | owner: A -->
## Igapäeva tööriistad

[Tööriistad ja platvormid, mida sa iga päev kasutad. Igaühe kohta: mis see on, milleks sa seda kasutad ja igasugune märkimisväärne konfiguratsioon.]

<!-- section: discarded | owner: A -->
## Proovitud ja kõrvale jäetud

[Tööriistad, mida sa oled teadlikult kõrvale jätnud, ja miks. Säästab agente sellest, et nad soovitaksid asju, mille sa juba välja arvasid.]

<!-- section: data-sources | owner: A -->
## Andme-allikad

[Kus su oluline andmestik elab — dokumendid, tabelid, andmebaasid, pilvesalvestus, konkreetsed platvormid. Mis kus elab.]

<!-- section: integrations | owner: A -->
## Integratsioonid ja ühendused

[Kuidas su tööriistad omavahel ühenduses on. Automatiseeringud, integratsioonid, andmevood süsteemide vahel.]

<!-- section: evaluating | owner: A -->
## Hindamisel või kasutusele võtmas

[Tööriistad, mida sa vaatled või plaanid kasutama hakata. Mis probleemi need lahendaksid.]
```

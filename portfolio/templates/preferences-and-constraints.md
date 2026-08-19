---
name: preferences-and-constraints
description: Kõvad reeglid, tugevad eelistused, piirangud, mida ei delegeeri
layer: profile
type: portfolio
updated: <YYYY-MM-DD>
review_after: <YYYY-MM-DD>
sensitivity: exportable
tags: [portfolio]
---

# Preferences and Constraints

## Mille jaoks see fail on

"Alati tee nii / ära kunagi tee nii" fail. Kõvad reeglid ja tugevad eelistused, mida iga sinu heaks töötav agent peaks austama ilma, et talle seda iga kord eraldi ütleksid. See katab kõike alates ajavööndi piirangutest ja vormistuse arvamustest kuni asjadeni, mida sa lausa vihkad. Kui on midagi, millega agent paneb sajaprotsendiliselt puusse, kui sa talle seda ette ei ütle, siis see käib siia.

---

## Intervjuu-protokoll

*Anna see fail tervikuna oma AI ehituspartnerile ja ütle "alustame sellega". Su ehituspartner peaks lugema allolevad juhised ja viima läbi intervjuu.*

**Juhised ehituspartnerile:** sa aitad kasutajal koostada tema preferences and constraints faili. See peaks tunduma nagu selge reeglistik, mitte mingi isiksuseprofiil. Nõua konkreetseid, rakendatavaid eelistusi — "ma vihkan koosolekuid enne kella kümmet" on kasulik; "ma hindan töö ja eraelu tasakaalu" on kasutu.

**Küsimused:**

1. Kas su ajas või kättesaadavuses on kõvasid piiranguid, mida iga agent peaks teadma? Ajavööndid, tunnid, mil sa ei tööta, päevad, mis on absoluutselt kinni?
2. Milles sa kompromisse ei tee — asjad, mida sa kategooriliselt nõuad selles osas, kuidas töö tehtud saab, kuidas väljundid on vormistatud või kuidas suhtlus käib?
3. Mida sa vihkad? Koosolekud, mis oleks võinud olla e-kirjad, mingi konkreetne žargoon, väljundi formaadid, mis sind ärritavad — kõik asjad, mille suhtes sul on tugev reaktsioon.
4. Kas sul on isiklikke piiranguid, mis mõjutavad su tööd — näiteks reisimise piirangud, pere graafikust tulenevad asjaolud, tervisemured ja kõik muu mida sa tahad, et agent arvesse võtaks? Jaga ainult seda, mida sa ise tahad jagada.
5. Kui AI sulle midagi toodab, siis millised on su vormistuse eelistused? Pikkus, struktuur, detailsusaste, toon?

**Millal piisab:** Pärast 4–5 küsimust.

**Pärast koostamist:** Näita mustandit. Küsi kasutajalt, kas on midagi puudu, mida ta avastaks end agentidele pidevalt meelde tuletamas. Need korduvad parandused ongi täpselt see kraam, mille jaoks see fail olemas on.

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
name: preferences-and-constraints
description: Kõvad reeglid, tugevad eelistused, piirangud, mida ei delegeeri
layer: profile
type: portfolio
updated: <YYYY-MM-DD>
review_after: <YYYY-MM-DD>
sensitivity: exportable
tags: [portfolio]
---

# Eelistused ja piirangud

<!-- section: hard-rules | owner: C -->
## Kõvad reeglid

[Piirid, kus kompromisse ei tehta — ajavööndid, kättesaadavuse aknad, planeerimise reeglid, asjad, mis on välistatud. Need on reeglid, mitte eelistused.]

Siia käib ka su üldistatud otsustusreegel, kui see on kõva ("ma ei otsusta kunagi sama päeva jooksul"). Üksikjuhtumid ise elavad tõendifailis `decision-log.md`.

<!-- section: preferences | owner: C -->
## Tugevad eelistused

[Asjad, mida sa kindlalt nõuad, aga milles saaksid teoreetiliselt järele anda. Tööriistade valik, formaadid, protsessid, tööviisid.]

### Mida ma vihkan

[Konkreetsed asjad, mis käivad närvidele — koosolekute formaadid, suhtlusmustrid, kantseliit, AI väljundite maneerid.]

### AI väljundi eelistused

[Kuidas sa tahad, et AI toodetud sisu oleks vormistatud ja esitatud. Pikkus, struktuur, detailsusaste, toon.]

<!-- section: constraints | owner: C -->
## Isiklikud piirangud

[Kõik sinu isikliku eluga seonduv, mis mõjutab su tööd ja mida agendid peaksid arvestama — pere graafik, tervisemured, asukoht, reisipiirangud. Ainult see, mida ise soovid jagada.]

Kui mõni rida siin nimetab teisi inimesi, kaalu selle tõstmist `team-and-relationships.md` faili, mis on `restricted`.

<!-- section: delegation | owner: C -->
## Mida ma annan ära ja mida mitte

[Töö, mida sa põhimõtteliselt käest ei anna, ja töö, mille sa annad kohe kui keegi on. See on reegel, mitte hetkeseis — praegune pudelikael käib `current-projects.md` faili.]
```

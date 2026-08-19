---
name: decision-log
description: Tõendikorpus: päris otsused, nende käik ja mida nad kasutaja kohta näitavad
layer: evidence
type: portfolio
updated: <YYYY-MM-DD>
review_after: <YYYY-MM-DD>
sensitivity: exportable
tags: [portfolio]
---

# Decision Log

## Mille jaoks see fail on

Kuidas sa otsuseid teed, koos päris näidetega. See on portfoolios kõige alahinnatum fail. Kui agent aitab sul mõnda uut otsust läbi mõelda, on talle tohutult kasulik teada, kuidas sa oled asju varem otsustanud — ta suudab sobituda sinu arutlemisstiiliga, tuua lauale õiget tüüpi infot ja hoiduda pakkumast lähenemisi, mis lihtsalt ei sobi sellega, kuidas sinu aju töötab.

---

## Intervjuu-protokoll

*Anna see fail tervikuna oma AI ehituspartnerile ja ütle "alustame sellega". Su ehituspartner peaks lugema allolevad juhised ja viima läbi intervjuu.*

**Juhised ehituspartnerile:** sa aitad kasutajal koostada tema decision log faili. Näited on siin kõige tähtsam osa — nõua konkreetseid detaile vähemalt kahe päriselt tehtud otsuse kohta. Abstraktsed kirjeldused otsustusstiilist on kordades vähem kasulikud kui konkreetsed lood tegelikest otsustest ja sellest, kuidas need sündisid.

**Küsimused:**

1. Kuidas sa üldiselt otsuseid teed? Kas sa oled tüüp, kes analüüsib kõike, usaldab kõhutunnet, räägib asjad inimestega läbi, magab öö mõttes ja teeb otsuse hommikul?
2. Millist infot sa tahad, enne kui otsuse lukku lööd? Mis tekitab sinus tunde, et oled valmis otsustama?
3. Räägi mulle ühest olulisest otsusest, mille sa hiljuti tegid — võib olla tööalane, võib olla isiklik. Mis see oli ja kuidas sa selle enda jaoks läbi mõtlesid?
4. Kas sa saad tuua veel ühe näite — ideaalis teist tüüpi otsusest?
5. Kuidas sa tuled toime olukordadega, kus sul ei ole piisavalt infot, aga pead siiski otsustama?
6. Kas sul on hetkel laual mõni otsus, millega sa parajasti pead murrad?

**Millal piisab:** Pärast 4–5 küsimust. Näited on kõige tähtsamad — hoolitse selle eest, et sul oleks enne mustandi tegemist konkreetsed detailid vähemalt kahe tegeliku otsuse kohta.

**Pärast koostamist:** Näita mustandit. Küsi kasutajalt, kas otsuste näited tabavad täpselt tema arutluskäiku — mitte ainult tulemust, vaid seda, kuidas ta asja päriselt läbi mõtles.

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

**See on tõendifail, mitte profiilifail.** Ta ei kirjelda, *kuidas sa otsustad* — ta hoiab **juhtumeid**, mille pealt seda näeb. Üldistus ("ma otsustan alati üle öö") kuulub profiilifaili `preferences-and-constraints.md`, ja tal peab siit tulema tõend.

Iga otsus saab `<allikas>` ID kujul `dl-<lühinimi>`. Üksikvaatlused selle sees saavad `<vaatlus>` ID. Kaks vaatlust **samast** otsusest ei ole sõltumatud — need ei ülenda väidet `toetatud` tasemele. Selleks on vaja kahte erinevat `dl-` allikat või ühte `dl-` juhtumit ja ühte kirjutamisnäidist (`sample-NN`).

```markdown
---
name: decision-log
description: Tõendikorpus: päris otsused, nende käik ja mida nad kasutaja kohta näitavad
layer: evidence
type: portfolio
updated: <YYYY-MM-DD>
review_after: <YYYY-MM-DD>
sensitivity: exportable
tags: [portfolio]
---

# Otsuste logi

<!-- section: decisions | owner: C -->
## Otsused

[2–3 päris otsust. Iga otsus on üks allikas. Ära üldista siin — kirjelda, mis päriselt juhtus.]

### [1. Otsuse pealkiri]

**allikas:** `dl-<lühinimi>`
**Millal:** [YYYY-MM]
**Olukord:** [Mis oli laual.]
**Valikud:** [Mille vahel sa valisid.]
**Mida sa otsustasid:** [Otsus ise.]
**Kuidas sa selleni jõudsid:** [Käik, mitte tulemus. See on osa, millest tõend tuleb.]

Vaatlused sellest juhtumist:

| vaatlus-ID | Mida see juhtum näitab |
|---|---|
| `kiirus` | [üks konkreetne asi] |
| `konsult` | [teine konkreetne asi] |

### [2. Otsuse pealkiri]

[Sama struktuur.]

<!-- section: reasoning | owner: C -->
## Mida need juhtumid näitavad

[Tuletatud mustrid. Iga rida vajab tõendit. Ühe allika pealt on rida `kandidaat`, kahe sõltumatu allika pealt `toetatud`.]

- [Muster, mida kaks eri juhtumit näitavad.] <!-- claim: status=toetatud; evidence=dl-<lühinimi>:kiirus,dl-<teine>:kiirus -->
- [Muster, mida näeb praegu ainult ühest juhtumist.] <!-- claim: status=kandidaat; evidence=dl-<lühinimi>:konsult -->

<!-- section: uncertainty | owner: C -->
## Määramatus ja lahtised otsused

[Mida sa teed, kui infot pole piisavalt, aga otsustada tuleb. Ja: millega sa praegu pead murrad.]

Inimesed, kellega sa enne suuri otsuseid räägid, käivad `team-and-relationships.md` faili — nemad on isikuandmed, mitte otsusemuster.
```

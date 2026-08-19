---
name: identity
description: Kes kasutaja on, mida ta teeb, mille poolest tuntud
layer: profile
type: portfolio
updated: <YYYY-MM-DD>
review_after: <YYYY-MM-DD>
sensitivity: exportable
tags: [portfolio]
---

# Identity

## Mille jaoks see fail on

See on minimaalne, kuid piisav kontekstifail. Kui agent saaks sinu kohta lugeda ainult ühte faili, oleks see see. Ütleb igale AI süsteemile, kes sa oled, mida sa teed ja mille poolest sind teatakse — piisav, et alustada kasulikku esimest vestlust ilma midagi muud lugemata.

---

## Intervjuu-protokoll

*Anna see fail tervikuna oma AI ehituspartnerile ja ütle "alustame sellega". Su ehituspartner peaks lugema allolevad juhised ja viima läbi intervjuu.*

**Juhised ehituspartnerile:** sa aitad kasutajal koostada tema identity-faili — lühike, tihe kontekstidokument, mis võtab kokku, kes ta on. Esita allolevad küsimused ükshaaval. Ära küsi kõiki korraga. Kui sul on koostamiseks piisavalt, lõpeta küsimine ja koosta fail allpool toodud väljundi struktuuri järgi.

**Küsimused:**

1. Mis su nimi ja praegune roll või ametinimetus on?
2. Millises ettevõttes või organisatsioonis sa oled, kui üldse?
3. Kui peaksid sõbrale õhtusöögil seletama, mida sa tegelikult teed — mitte ametinimetust, vaid millele sa oma aja päriselt kulutad — mis sa ütleksid?
4. Mille pärast inimesed sinu juurde tulevad? Mis on see asi, kus keegi ütleb "selle koha pealt küsi [sinu nimi] käest"?

**Millal piisab:** pärast 3–4 küsimust. See fail peab olema lühike — paar rida fakte ja üks tugev lõik. Ära paksenda.

**Pärast koostamist:** näita mustandit ja palu kasutajal välja tuua kõik, mis ei kõla õigesti või tundub vale. Paranda tema tagasiside põhjal.

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
name: identity
description: Kes kasutaja on, mida ta teeb, mille poolest tuntud
layer: profile
type: portfolio
updated: <YYYY-MM-DD>
review_after: <YYYY-MM-DD>
sensitivity: exportable
tags: [portfolio]
---

# Identiteet

<!-- section: identity-facts | owner: A -->
## Põhifaktid

- **Nimi:** [Täisnimi] <!-- claim: status=kinnitatud; basis=user-stated -->
- **Roll:** [Praegune ametinimetus või roll] <!-- claim: status=kinnitatud; basis=user-stated -->
- **Organisatsioon:** [Ettevõte, tiim või "Iseseisev"] <!-- claim: status=kinnitatud; basis=user-stated -->

<!-- section: what-i-do | owner: A -->
## Mida ma teen

[Üks lõik — lihtsas keeles, mitte ametijuhend. Millele sa oma aja päriselt kulutad, seletatud nii, et tark võõras saab aru.]

<!-- section: known-for | owner: A -->
## Mille poolest olen tuntud

[1–3 lauset. Mille pärast inimesed sinu juurde tulevad. Su tunnusoskus, vaatenurk või valdkond.]
```

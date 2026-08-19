---
name: domain-knowledge
description: Valdkonna teadmised, terminoloogia, mõttemudelid, algaja-tsoonid
layer: profile
type: portfolio
updated: <YYYY-MM-DD>
review_after: <YYYY-MM-DD>
sensitivity: exportable
tags: [portfolio]
---

# Domain Knowledge

## Mille jaoks see fail on

Mida sina tead, aga üldine AI ei tea. See fail hoiab ära selle, et agendid hakkaksid sulle seletama asju, mida sa juba sügavalt mõistad, ja aitab neil su tööd kujundavast valdkonnaspetsiifilisest kontekstist mitte väga mööda panna. Samuti paneb see kirja alad, kus sa oled algaja — et agendid teaksid, millal tuleb seletada rohkem, mitte vähem.

---

## Intervjuu-protokoll

*Anna see fail tervikuna oma AI ehituspartnerile ja ütle "alustame sellega". Su ehituspartner peaks lugema allolevad juhised ja viima läbi intervjuu.*

**Juhised ehituspartnerile:** sa aitad kasutajal koostada tema domain knowledge faili. See käib õige selgitustaseme kalibreerimise kohta — mida ta teab läbi ja lõhki, mida ta teab piisavalt, et olla ohtlik, ja mida ta tahaks, et talle puust ja punaseks ette tehtaks. Kasuta seda, mida sa juba eelmistest failidest õppinud oled, et esitada tema valdkonna kohta teadlikumaid küsimusi.

**Küsimused:**

1. Mis on sinu tõelised ekspertteadmised — asjad, mida sa tead piisavalt sügavalt, et võiksid neid kellelegi teisele õpetada?
2. Mis on sinu maailma žargoon? Terminid, mida sa iga päev kasutad ja mida üldine AI kipuks üle seletama või millest ta üldse valesti aru saaks?
3. Kas su valdkonnas on mingi kontekst, mida kõrvaltvaataja ei teaks, aga mis kujundab kõike, mida sa teed? Regulatsioonid, turudünaamika, sinu ala kultuurinormid?
4. Kas sul on kindlaid raamistikke või mõttemudeleid (mental models), mida sa pidevalt kasutad probleemide lahendamisel?
5. Teistpidi — kas on valdkondi, kus sa oled algaja ja kus sa päriselt tahaksid, et AI seletaks asju lahti rohkem, mitte vähem?

**Millal piisab:** Pärast 4–5 küsimust.

**Pärast koostamist:** Näita mustandit. Küsi kasutajalt, kas teadmiste tase tundub õige — on väga lihtne oma teadmisi üle hinnata või unustada mainimata valdkond, kus sa tegelikult tahaksid rohkem lahtiseletamist.

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
name: domain-knowledge
description: Valdkonna teadmised, terminoloogia, mõttemudelid, algaja-tsoonid
layer: profile
type: portfolio
updated: <YYYY-MM-DD>
review_after: <YYYY-MM-DD>
sensitivity: exportable
tags: [portfolio]
---

# Valdkonnateadmised

<!-- section: expertise | owner: B -->
## Ekspertteadmised

[Valdkonnad, tööstusharud, distsipliinid, mida sa tunned süvitsi. Asjad, kus sa ei vaja tausta lahtiseletamist — sa vajad, et AI opereeriks sinu tasemel.]

<!-- section: terminology | owner: B -->
## Põhiterminoloogia

[Žargoon, mida sa kasutad ilma definitsioonideta. Valdkonna terminid, lühendid, kontseptsioonid, mida AI peaks kasutama loomulikult, mitte hakkama defineerima või vältima.]

<!-- section: domain-context | owner: B -->
## Valdkonna kontekst

[Asjad, mida kõrvaltvaataja ei teaks, aga mis kujundavad sinu tööd — regulatiivne keskkond, turudünaamika, kultuurinormid, ajalooline taust.]

<!-- section: frameworks | owner: B -->
## Raamistikud ja mõttemudelid

[Konkreetsed raamistikud või mõttetööriistad, mida sa regulaarselt kasutad. Kuidas sa lähened probleemidele, organiseerid infot või mõtestad keerulisi olukordi.]

<!-- section: learning-zones | owner: B -->
## Kus ma olen algaja

[Valdkonnad, kus sa tahad pikemat selgitust, mitte lühemat. Teemad, kus sa alles õpid ja tahad, et AI pigem õpetaks.]
```

---
name: current-projects
description: Aktiivsed projektid, prioriteedid, ICP, pakkumine ja sõnumireeglid
layer: profile
type: portfolio
updated: <YYYY-MM-DD>
review_after: <YYYY-MM-DD>
sensitivity: exportable
tags: [portfolio]
---

# Current Projects

## Mille jaoks see fail on

See on fail, mis tõenäoliselt muutub kõige sagedamini. Püüab kinni aktiivsed töövoolud — millega tegeled ja mis on iga asja juures oluline. Agendid kasutavad seda, et mõista su praegust konteksti — et küsida asjakohaseid küsimusi, teha kasulikke ettepanekuid ja vältida sinu aja raiskamist mitteaktiivsete teemadega. Uuenda alati, kui projektid algavad, lõppevad või prioriteet muutub.

---

## Intervjuu-protokoll

*Anna see fail tervikuna oma AI ehituspartnerile ja ütle "alustame sellega". Su ehituspartner peaks lugema allolevad juhised ja viima intervjuu läbi.*

**Juhised ehituspartnerile:** sa aitad kasutajal koostada tema current projects faili. Alusta täieliku nimekirja saamisega, seejärel liigu iga projekti juurde järjest ükshaaval. Kasuta mida tead eelmistest failidest, et üleliigseid küsimusi vältida. Kui kasutaja mainis projekte rolli-intervjuus, viita neile siin.

**Küsimused:**

1. Millega sa parasjagu aktiivselt tegeled? Loetle projekti nimed või lühikirjeldused, mis loomulikult meelde tulevad.
2. [Iga projekti kohta, ükshaaval:] Räägi [projektist]. Mis see on, mis olukorras see on ja kuidas see lõpetatuna välja näeb?
3. Kellega sa [projekti] peal töötad?
4. Kui pidaksid need projektid praegu prioriteedi järgi ritta panema, siis kuidas need järjestuksid?
5. Kas miski on seisma jäänud või blokeeritud? Mis on seal olukord?

**Millal piisab:** kui oled iga kasutaja nimetatud projekti läbi käinud. Ära suru kindlat arvu — mõnel on kolm aktiivset projekti, mõnel kaksteist.

**Pärast koostamist:** näita mustandit ja palu kasutajal kontrollida staatust ja prioriteedijärjestust. Need on kõige tõenäolisemalt veidi paigast ära.

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

Kohustuslikud on kõik allolevad sektsioonid peale `objections-optional`. Kui mõni jääb katmata, jäta pealkiri alles ja kirjuta alla nähtav rida `**Veel katmata.**` — katmata sektsioon peab olema näha, mitte kaduda vaikusesse.

```markdown
---
name: current-projects
description: Aktiivsed projektid, prioriteedid, ICP, pakkumine ja sõnumireeglid
layer: profile
type: portfolio
updated: <YYYY-MM-DD>
review_after: <YYYY-MM-DD, tavaliselt 30 päeva>
sensitivity: exportable
tags: [portfolio]
---

# Praegused projektid

<!-- section: active-projects-and-status | owner: A -->
## Aktiivsed projektid ja seis

[Korda seda plokki iga aktiivse projekti kohta.]

### [Projekti nimi]

- **Kirjeldus:** [Üks rida — mis see projekt on.] <!-- claim: status=kinnitatud; basis=user-stated -->
- **Staatus:** [Algfaasis / Töös / Lõpetamas / Blokeeritud / Ootel] <!-- claim: status=kinnitatud; basis=user-stated -->
- **Minu roll:** [Mida sa selle projekti peal konkreetselt teed.] <!-- claim: status=kinnitatud; basis=user-stated -->
- **Mis on lõpetatud:** [Konkreetne tulemus, ja mis see tähendab, et see on valmis.] <!-- claim: status=kinnitatud; basis=user-stated -->

<!-- section: priority-order | owner: A -->
## Prioriteedijärjekord

[Projektid ritta, kõrgeimast madalaimani. Mitte siltidega "kõrge/keskmine", vaid järjekorrana — kui kaks asja konkureerivad sama tunni pärast, kumb võidab.]

<!-- section: bottleneck-and-delegable-work | owner: A -->
## Pudelikael ja äraantav töö

[Mis on kinni ja mille taga. Ja: milline osa sellest tööst ei pea sinu käes olema.]

Delegeerimise **reeglid** (mida sa põhimõtteliselt ei anna käest) käivad `preferences-and-constraints.md` sektsiooni `delegation`. Siia käib see, mis on **praegu** ära antav.

<!-- section: icp-and-best-customers | owner: B -->
## ICP ja parimad kliendid

[Kirjelda kolme viimase kuu parimat klienti ja mis neil ühist oli. Sellest tuleb ICP — mitte vastupidi.]

Selle sektsiooni masinloetav kuju on allpool `ebia-sector-size-region`, mis kannab katvusvõtit `icp_sector_size_region`. Kui see siin on täidetud, aga otsingusisend on tühi, ei ole katvus olemas.

- **ICP:** [Kellele see päriselt sobib.] <!-- claim: status=kandidaat; evidence=cp-kliendid:muster -->
- **Keda me väldime:** [Klient, kellest loobusite, ja miks.] <!-- claim: status=kandidaat; evidence=cp-loobumine:pohjus -->

<!-- section: offer-and-evidence | owner: B -->
## Pakkumine ja tõendid

- **Mida ma müün:** [Konkreetne pakkumine, mitte kategooria. Ütle ka, kellele — ostja, mitte turg.] <!-- claim: status=kinnitatud; basis=user-stated --> <!-- quick-coverage: offer_buyer -->
- **Tõend:** [Number, juhtum või tulemus, mida sa saad nimetada. Kui tõendit pole, kirjuta "puudub" — see on parem kui väljamõeldud tõend.] <!-- claim: status=kinnitatud; basis=user-stated --> <!-- quick-coverage: credibility_evidence -->

<!-- section: trigger | owner: B -->
<!-- quick-coverage: problem_trigger -->
## Käivitaja

[Mis päästiku peale klient ühendust võttis. Sündmus, mitte omadus. "Kasvab kiiresti" ei ole käivitaja; "kaotas raamatupidaja" on.]

<!-- section: ebia-sector-size-region | owner: B -->
<!-- quick-coverage: icp_sector_size_region -->
## Otsingusisend

Masinloetav sisend outreach-nimekirja koostamiseks (EBIA või muu registripäring).

- **Sektor:** [Tegevusala või EMTAK-kood.] <!-- claim: status=kinnitatud; basis=user-stated -->
- **Suurus:** [Töötajate arv või käibevahemik.] <!-- claim: status=kinnitatud; basis=user-stated -->
- **Piirkond:** [Maakond, linn või riik.] <!-- claim: status=kinnitatud; basis=user-stated -->

<!-- section: message-purpose-cta | owner: B -->
<!-- quick-coverage: message_purpose_cta -->
## Sõnumi eesmärk ja CTA

- **Eesmärk:** [Mida üks sõnum peab saavutama. Üks asi, mitte kolm.] <!-- claim: status=kinnitatud; basis=user-stated -->
- **CTA:** [Täpne palve, mille sa lõppu paned.] <!-- claim: status=kinnitatud; basis=user-stated -->

<!-- section: forbidden-claims | owner: B -->
<!-- quick-coverage: forbidden_claims -->
## Mida ei tohi väita

[Kõva keelunimekiri. Väited, mida ükski agent ei tohi sinu nimel esitada — sertifikaadid, mida sul pole, tulemused, mida sa ei suuda tõendada, kliendinimed, mida sa ei tohi nimetada, garantiid, mida sa ei anna.]

See sektsioon on projektsioonide kvaliteedivärav: väljaminev mustand, mis rikub ühtki siinset rida, on ebaõnnestunud mustand, ka siis kui ta muidu hästi kõlab.

<!-- section: objections-optional | owner: B -->
## Vastuväited *(valikuline)*

[Mis vastuväiteid sa müügivestluses kuuled ja mida sa neile vastad.]
```

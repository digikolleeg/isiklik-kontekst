# Väited, tõendid ja kandidaadid

Selle faili reeglid kehtivad mõlemas režiimis. Need määravad, mida tohib kirjutada püsivasse faili ja mida mitte.

See reference on iseseisev. Skill peab töötama ka väljaspool seda repot, seega ei loe sa siin ühtegi projektifaili. Kõik lubatud väärtused on allpool.

---

## 1. Tõendi-ID

Iga tõendi-ID on kujul:

```
<source-family>:<observation-id>
```

`source-family` identifitseerib **ühe konkreetse artefakti või olukorra**: ühe kirja, ühe postituse, ühe vastuse, ühe dokumendi. `observation-id` on selle sees tehtud üksik tähelepanek.

| source-family | Mis see on |
|---|---|
| `answer-NN` | üks kasutaja vastus intervjuus |
| `sample-NN` | üks kasutaja päris kirjutamisnäidis |
| `material-NN` | üks imporditud dokument |

Võid kasutada ka kõnekamat konkreetset nime, näiteks `cold-email-2026-06-14`. Tingimus on ainult see, et see osutaks ühele artefaktile või olukorrale.

`observation-id` on vabalt valitud, aga stabiilne ja loetav: `observation-01`, `pattern-01`, `phrase-02`.

### Üldnimed on keelatud

`source-family` **ei tohi** olla kategooria. Need on keelatud:

```
email   linkedin   channel   document   message   situation   interview
```

`email:pattern-01` on vale, sest "email" ei ole üks kiri, vaid kanal. Õige on `sample-02:pattern-01`.

Põhjus on otsene: kategooria alla mahub lõpmatu arv tähelepanekuid ja siis saaks kaks tähelepanekut samast kirjast näida sõltumatuna.

### Sõltumatuse reegel

**Kaks tõendit on sõltumatud ainult siis, kui nende `source-family` on erinev artefakt või olukord.**

```
sample-01:pattern-01 + sample-02:pattern-01    → sõltumatud
sample-01:pattern-01 + sample-01:pattern-02    → EI ole sõltumatud
answer-04:observation-01 + answer-04:phrase-01 → EI ole sõltumatud
```

Kaks tähelepanekut samast e-kirjast on üks tõend. Vastus ja selle süvendus on sama perekond, kui süvendus täpsustab sama asja.

**Sama kanali kaks eri sõnumit on sõltumatud.** Kaks eri e-kirja on kaks perekonda ja koos annavad `toetatud`. Sõltumatust ei määra kanal, vaid artefakt. Ainus, mis on keelatud, on kanali enda kasutamine perekonnanimena.

---

## 2. Kolm staatust

| Staatus | Millal | Nõue |
|---|---|---|
| `kinnitatud` | **kasutaja ütles selle ise otsesõnu, või kinnitas fakti või reegli selgesõnaliselt** | `basis=user-stated`, tõendit ei nõuta |
| `toetatud` | sina tuletasid mustri ja seda toetab vähemalt kaks **sõltumatut** perekonda | vähemalt 2 eri source-family ID-d |
| `kandidaat` | üks vaatlus või tuletus ilma teise sõltumatu tõendita | 0 või 1 ID |

Kahtluse korral vali madalam staatus.

`kinnitatud` eeldab kasutajalt **selget sisulist väidet**. Kaks lubatud teed:

1. ta ütles selle ise ("ma ei kasuta kunagi hüüumärke");
2. sina esitasid fakti või reegli ja ta kinnitas selle selgesõnaliselt ("jah, see reegel kehtib alati").

**Pelk noogutus ei ole kinnitus.** "Mhm", "ok", "sobib" ja vastamata jätmine ei tee tuletusest kinnitatud väidet. Kui sa ei suuda tsiteerida, mida ta täpselt kinnitas, ei ole see `kinnitatud`.

Nõusolek ei tõsta ka `kandidaat` staatust `toetatud` staatuseks: `toetatud` tuleb tõendite arvust, mitte nõusolekust.

---

## 3. Väite vorming failis

Väide on **puhas bullet**, millele järgneb HTML kommentaar. Nähtavat staatusprefiksit ei kasutata: kasutaja loeb tavalist lauset, masin loeb kommentaari.

```
- Ei kasuta hüüumärke. <!-- claim: status=kinnitatud; basis=user-stated -->
- Alustab otse. <!-- claim: status=toetatud; evidence=sample-01:pattern-01,sample-02:pattern-01 -->
- Eelistab lühidust. <!-- claim: status=kandidaat; evidence=answer-04:observation-01 -->
```

Reeglid:

- Kommentaar algab alati `claim:` märksõnaga.
- `status=` on kohustuslik ja üks kolmest lubatud väärtusest.
- `kinnitatud` kannab `basis=user-stated`. Kui tõend on olemas, tohib lisada ka `evidence=`.
- `toetatud` ja `kandidaat` kannavad `evidence=`.
- Mitu ID-d eraldatakse komaga **ilma tühikuta**: `evidence=sample-01:pattern-01,sample-02:pattern-01`.
- Väljad eraldatakse semikooloni ja tühikuga: `status=toetatud; evidence=...`.
- Kommentaar on samal real bulletiga, lause lõpu järel.

**Ära kirjuta nähtavat `[kinnitatud]` prefiksit.** See vorming on kasutusest väljas.

Bullet ise on tavaline eestikeelne lause.

### Vorminguraud

Genereeritud kontekstifailis ei tohi olla ühtegi rida, mis algab `- ` ja ei kanna claim-kommentaari. Kontroll käib **rea alguse järgi, mitte tähenduse järgi**, seega kehtib see ka loetelule, mis ei ole väide.

Kui vajad tavalist loetelu, näiteks kanalite nimekirja, on kaks lubatud teed:

1. nummerdatud loetelu
2. tabel

Kontroll: `python3 scripts/context_v3_check.py --rule profile --input <fail> --name <failinimi>`.

---

## 4. Kandidaadiregister: portfolio/_candidates.md

Kiire režiim ei oma süvarežiimi sektsioone. Kõik tuletused, mis kuuluvad süvasektsiooni, lähevad kandidaadiregistrisse, mitte profiilifaili.

Loo fail, kui puudub.

**Register on muudetav rea kaupa.** Kolm lubatud operatsiooni:

| Operatsioon | Millal |
|---|---|
| **lisa rida** | uus tuletus, mis kuulub võõrasse faili või sektsiooni |
| **muuda rida** | sama väide sai täpsema sõnastuse, uue tõendi-ID või kitsama scope'i |
| **eemalda rida** | kandidaat ülendati faili, või kasutaja ütles, et see on vale |

Ülendatud kandidaat **tuleb** eemaldada, muidu ta dubleerub järgmisel jooksul. Vt `deep-mode.md` §7.

Registrit ei kirjutata tervikuna üle. **Read, mida sa ei puutunud, jäävad muutmata**, ka siis, kui nad kuuluvad teise mooduli või varasema sessiooni alla.

Register on **markdown-tabel**. Päis kannab täpselt need kaheksa välja, selles järjekorras, ja mitte ühtegi muud:

```markdown
| id | target_file | target_section | claim | evidence_ids | scope | expires | status |
|---|---|---|---|---|---|---|---|
| cand-01 | communication-style.md | määramata | Eelistab lühidust külmkontaktis. | answer-04:observation-01 | külm esimene kontakt | 2026-11-19 | kandidaat |
| cand-02 | goals-and-priorities.md | määramata | Optimeerib käibe asemel marginaali. | answer-07:observation-01 | üldine | 2026-11-19 | kandidaat |
```

Ära muuda päise sõnastust ega järjekorda. Ära lisa veerge. Uus kanne on uus rida.

| Väli | Sisu |
|---|---|
| `id` | `cand-NN`, jooksev |
| `target_file` | üks lubatud sihtfailidest, vt §5 |
| `target_section` | täpne sektsiooni-ID `deep-mode.md` omandiregistrist; kui register pole selles töörežiimis kaasas või sobiv koht pole üheselt selge, `määramata` |
| `claim` | üks lause, sama sõnastus, mis läheks faili |
| `evidence_ids` | komaga, tühikuta |
| `scope` | millal see kehtib; kui tingimust pole, kirjuta `üldine` |
| `expires` | kuupäev `YYYY-MM-DD`; `current-projects.md` puhul 30 päeva, muidu vaikimisi kolm kuud loomisest |
| `status` | alati `kandidaat` |

`status` on kandes alati `kandidaat`. Register ei sisalda muid staatusi: kinnitatud ja toetatud väited lähevad otse faili. Kandidaat ei muutu registris `toetatud` staatuseks, ta **lahkub** registrist ja ilmub failis.

---

## 5. Lubatud sihtfailid ja sektsioonid

Kontekstisüsteem on 9 profiilifaili + 2 tõendifaili.

**Profiilifailid:**

1. `identity.md`
2. `role-and-responsibilities.md`
3. `current-projects.md`
4. `team-and-relationships.md`
5. `tools-and-systems.md`
6. `communication-style.md`
7. `goals-and-priorities.md`
8. `preferences-and-constraints.md`
9. `domain-knowledge.md`

**Tõendifailid:**

10. `writing-samples.md`
11. `decision-log.md`

`target_file` peab olema üks neist üheteistkümnest.

### target_section

Süvarežiimi sektsioonijaotus on **lukus**. Installitud Skilli omandiregister on failis [deep-mode.md](deep-mode.md) §5 ja see on ainus lubatud allikas.

1. Kui register on loetud ja annab üheselt sobiva sektsiooni, kirjuta täpne sektsiooninimi.
2. Kui sobivaid on mitu, ükski ei sobi või kasutad null-installi kiire intervjuu faili, kus registrit pole kaasas, kirjuta `target_section: määramata`.

Ära paku sektsiooninime mälu järgi ega tuleta seda failinimest. Vale sektsioon on halvem kui määramata: määramata kande suunab süvarežiim õigesse kohta, vale kande kirjutab valesse kohta.

Kandidaadiregister on **tugiledger, mitte viies kontekstiväljund**. Kiire režiim toodab neli faili ja lisaks selle registri. Registrit ei laadita agendile kontekstiks.

---

## 6. Mida ei tohi kunagi teha

- Ära kirjuta profiilifaili väidet, mille tõendi-ID-d sa ei suuda nimetada.
- Ära ülenda ühte vaatlust mustriks.
- Ära loe kahte tähelepanekut samast source-family'st kaheks sõltumatuks tõendiks.
- Ära kirjuta oma genereeritud teksti tõendiks. AI koostatud lause ei ole näidis.
- Ära täida katmata välja üldsõnalise lausega. Katmata väli jääb nähtavaks, vt `output-contract.md`.
- Ära kasuta nähtavat staatusprefiksit bulleti alguses.

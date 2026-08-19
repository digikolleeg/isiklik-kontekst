# Muu töö või agent

Käivitub: **"muu töö või agent"** või **"laienda konteksti uue agendi jaoks"**.

See rada on üldine. Ta ei tea ette, mis tööd kasutaja agendile annab, ja **ei tohi seda arvata**. Valdkond tuleb kasutaja esimesest vastusest.

<!-- expand-first-question: work -->
<!-- expand-read: existing-files -->
<!-- expand-read: candidates -->
<!-- expand-bucket: olemas -->
<!-- expand-bucket: ebaselge -->
<!-- expand-bucket: puudu -->
<!-- expand-no-repeat: true -->
<!-- expand-output: context-selection -->
<!-- expand-creates-context-file: false -->
<!-- expand-writes-work-instruction: false -->
<!-- expand-write-scope: candidates+empty-sections -->

Loe koos sellega: `interview-engine.md` (küsimise mehaanika), `claims-and-evidence.md` (staatused, tõendid, kandidaadiregister), `output-contract.md` (frontmatter, sektsiooniankrud, salvestamine) ja `deep-mode.md` §5 (kogu 9 + 2 sektsioonide omandiregister).

---

## 1. Küsi töö. Üks küsimus, enne kõike muud.

> *"Mis tööd see agent sinu eest teeb?"*

Ära paku valikuid ega näiteid. Näide kitsendab vastust ja sa saad tagasi selle, mille sa ise ette ütlesid.

Kui vastus on ebamäärane ("aitab turundusega"), küsi **üks** täpsustus:

> *"Mis on selle töö esimene samm, kui sa seda praegu ise teed?"*

Valitud töö on kogu ülejäänud sessiooni raam. Kirjuta see endale välja ja too seda igas järgnevas küsimuses tagasi: *"selle töö jaoks…"*.

Kumbki samm ei kulu eelarvest.

---

## 2. Loe olemasolev seis

Enne teist küsimust loe kontekstikaustast:

1. kõik olemasolevad **9 profiilifaili ja 2 tõendifaili**;
2. **kandidaadiregister** `_candidates.md`;
3. iga faili frontmatter, eriti `review_after`.

Sa ei küsi kasutajalt, mis on juba tehtud. Sa vaatad ise.

Kui ühtegi faili ei ole, ütle see välja ja jätka: sel juhul on kõik puudu ja see on normaalne algus.

---

## 3. Kaardista valitud töö vaates: olemas / ebaselge / puudu

Sa ei kaardista kogu kontekstisüsteemi. Sa kaardistad **ainult seda, mida see üks töö vajab**.

| Seis | Tingimus |
|---|---|
| **olemas** | sektsioonis on `kinnitatud` või `toetatud` väide, mis seda tööd päriselt teenindab |
| **ebaselge** | sisu on olemas, aga ainult `kandidaat` staatuses, või ta on liiga üldine selle töö jaoks, või `review_after` on möödas |
| **puudu** | sektsiooni pole, ta on tühi või kannab `<!-- katmata: … -->` märget |

Näita kaardistus kasutajale enne küsimist, lühidalt:

```
Töö: kliendipäringutele vastamine

olemas    identity, communication-style (kanalid ja register)
ebaselge  current-projects (ICP on kandidaat), domain-knowledge (üldsõnaline)
puudu     preferences-and-constraints (mida sa ei luba), decision-log
```

Ütle ka, mida sa kõrvale jätsid: *"tools-and-systems ei puutu sellesse töösse, jätan vahele."* Kaardistus, mis loetleb kõike, ei ole kaardistus.

---

## 4. Küsi ainult puuduolev

**Ära korda seda, millele on juba vastatud.** See on selle raja kõige tähtsam reegel, sest kasutaja on tõenäoliselt just läbinud müügiagendi intervjuu.

| Seis | Mida teed |
|---|---|
| **olemas** | ei küsi. Kui vajad kinnitust, tsiteeri ja küsi ainult, kas see kehtib ka selles töös. |
| **ebaselge** | **tsiteeri olemasolevat** ja küsi ainult puuduvat serva või teist sõltumatut tõendit. Ära küsi algset küsimust uuesti. |
| **puudu** | küsi tavaline küsimus |

Ebaselge sektsioon on odavaim koht: seal on juba üks vaatlus ja üks hea küsimus annab teise sõltumatu tõendi, mis ülendab kandidaadi `toetatud` staatuseks. Vt `claims-and-evidence.md` §1.

Küsimuste valik, süvendused ja peegel: `interview-engine.md`. Üks küsimus korraga, kuni üks süvendus vastuse kohta.

Kui kasutaja on väsinud või katvus on selle töö jaoks piisav, **lõpeta**. Selle raja eesmärk ei ole failide täitmine, vaid ühe töö tööle saamine.

---

## 5. Koosta kontekstivalik

Raja väljund on **kontekstivalik**: nimekiri failidest ja sektsioonidest, mida see agent laadib.

```
Agent: kliendipäringutele vastaja

laeb alati:
  identity.md              → identity-facts, what-i-do
  communication-style.md   → channel-registers, avoid
  preferences-and-constraints.md → hard-rules

laeb ülesande järgi:
  domain-knowledge.md      → terminology

ei lae:
  team-and-relationships.md  (restricted)
  writing-samples.md         (see agent vastab, ei tee külmkontakti)
```

Kolm reeglit:

1. **Kontekstivalik on projektsioon, mitte uus tõeallikas.** Ta viitab olemasolevatele failidele ja sektsioonidele. Sisu ta ei dubleeri.
2. **`restricted` failid ei lähe valikusse vaikimisi.** Kui kasutaja tahab neid, küsi eraldi ja ütle, mis sinna sisse läheb.
3. **Kandidaadiregister ei lähe kunagi valikusse.** See on tugiledger, mitte kontekst.

Ütle kasutajale, mida valik tähendab: *"see agent näeb neid asju ja ei näe ülejäänut."*

---

## 6. Mida see rada ei tee

- **Ei kirjuta Skilli ega tööjuhist.** Kontekst ütleb, kes kasutaja on, mida ta müüb ja kellele. Tööjuhis ütleb, kuidas tööd tehakse. Need on eri asjad ja eri failides. Kui kasutaja tahab tööjuhist, ütle, et see on järgmine samm, ja lõpeta kontekstivalikuga.
- **Ei loo uut kontekstifaili väljaspool 9 + 2 lepingut.** Uus töö ei tähenda uut faili.
- **Ei muuda sektsiooni, mis juba kannab omaniku sisu.** Uus leid läheb kandidaadiregistrisse koos `target_file` ja `target_section` väärtusega. Vt `claims-and-evidence.md` §4.
- **Ei arva valdkonda ette.** Iga töö saab sama kohtlemise.
- **Ei küsi uuesti seda, mis on müügiteel juba vastatud.**

---

## 7. Kirjutamine ja lõpp

Kirjutamise reeglid on samad mis mujal:

1. Tühja või katmata märkega sektsiooni tohid täita.
2. Sisuga sektsiooni ei muuda: leid läheb registrisse.
3. Puuduva faili loomisel kasuta süvarežiimi täielikku ankruskeletti `deep-mode.md` §5 omandiregistri järgi. Laiendus ei piirdu kiire režiimi nelja faili skeletiga.
4. Frontmatter ja staatused nagu `output-contract.md` §1 ja `claims-and-evidence.md` §3.

Lõpeta kolme asjaga:

1. **salvesta**, ütle kuhu;
2. **näita kontekstivalik**;
3. **ütle, kuidas seda testida.** Anna üks konkreetne katse valitud töö kohta, näiteks: *"anna agendile üks päris päring, mis sul eile tuli, ja vaata, kas ta vastab nii, nagu sa ise vastaksid."*

Testi tulemust ei genereeri sa ise ega saada kuhugi. Mustand jääb kasutaja ette.

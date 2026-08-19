---
name: communication-style
description: Kuidas kasutaja kirjutab, hääl, vormistus, mida väldib
layer: profile
type: portfolio
updated: <YYYY-MM-DD>
review_after: <YYYY-MM-DD>
sensitivity: exportable
tags: [portfolio]
---

# Communication Style

## Mille jaoks see fail on

Kuidas sa suhtled — et iga agent, kes sinu nimel midagi kirjutab, kõlaks nagu sina, mitte nagu mingi suvaline AI. See on fail, mis määrab, kas valminud mustand paneb sind mõtlema "päris hea" või hoopis "ma ei ütleks seda elu sees nii". Konkreetsus on siin tähtsam kui kusagil mujal su portfoolios. Ümmargune communication style fail on kasutu.

---

## Intervjuu-protokoll

*Anna see fail tervikuna oma AI ehituspartnerile ja ütle "alustame sellega". Su ehituspartner peaks lugema allolevad juhised ja viima läbi intervjuu.*

**Juhised ehituspartnerile:** sa aitad kasutajal koostada tema communication style faili. See on kõige keerulisem fail, mida hästi teha, sest inimesed ei oska oma kirjutamisstiili abstraktselt kirjeldada. Nõua konkreetsust. Kui nad viskavad õhku üldsõnalise "olen üsna vaba", siis uuri edasi "milline see vaba välja näeb — anna mõni näide sellest, mida sa päriselt kirjutaksid". Üksikasjad on siin kõige tähtsamad.

**Küsimused:**

1. Kui sa kirjutad e-kirja või sõnumi, siis kas oled pigem lühike ja konkreetne, või annad ka laiemat tausta ja detaile?
2. Kui formaalne su töine kirjavahetus on? Kas see muutub sõltuvalt sellest, kellele sa kirjutad?
3. Mis sind häirib, kui loed midagi, mis on sinu nimel või sinu eest kirjutatud? Mis paneb mõtlema, et "see ei kõla nagu mina"?
4. Kas sul on kindlaid sõnu, fraase või mustreid, mida tead, et sa palju kasutad? Asju, millest teised su kohe ära tunneksid?
5. Kas on sõnu või väljendeid, mida sa teadlikult väldid? Asju, mis kõlavad võltsilt, on puhas kantseliit või lihtsalt pole sina?
6. Kuidas sa tavaliselt e-kirja üles ehitad — alustad kohe palvest, annad enne tausta, kasutad punktikirja (bullet points), või kirjutad pikkade lõikudena?
7. Kas sul on stiilinäiteid oma kirjutamise kohta? Müügi emailid, sotsiaalsed postitused, artiklid või blogi.

**Millal piisab:** Pärast 5–6 küsimust. Kui vastused on hägused, pressi detaile välja enne, kui mustandi teed. Ümmarguse faili puhul hakkab iga agent, kes selle inimese nimel kirjutab, puusse panema.

**Pärast koostamist:** Näita mustandit. See on fail, kus reaktsioon on kõige olulisem — palu kasutajal iga kirjeldus läbi lugeda ja öelda, kas see vastab ka tegelikult sellele, kuidas ta kirjutab, või on see lihtsalt unistus.

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

See fail kirjeldab **reegleid**. Näited elavad tõendifailis `writing-samples.md`. Ära pane näiteid siia ja ära pane reegleid sinna — projektsioonid loevad neid erinevalt: reegleid järgitakse, näidetest pattern-match'itakse.

```markdown
---
name: communication-style
description: Kuidas kasutaja kirjutab, hääl, vormistus, mida väldib
layer: profile
type: portfolio
updated: <YYYY-MM-DD>
review_after: <YYYY-MM-DD>
sensitivity: exportable
tags: [portfolio]
---

# Suhtlusstiil

<!-- section: general-style | owner: D -->
## Üldine stiil

[Kuidas sa üldiselt suhtled — kas lühidalt või põhjalikult, ametlikult või vabalt, otsekoheselt või diplomaatiliselt. N-ö baastase.]

**Kirjutamise tekstuur:** [Lausepikkus, sõnavara keerukus, erialaterminite kasutamine, toon.]

<!-- section: channel-registers | owner: D -->
<!-- quick-coverage: channel_register_length -->
## Kanali järgi

[Kuidas su stiil kanali ja kuulajaskonna järgi muutub — e-mail vs LinkedIn vs Slack vs dokument; ülemusele vs tiimile vs kliendile vs võõrale. Kui see väga ei muutu, ütle ka see välja.]

**Pikkus kanali kohta** kuulub siia: mitu lauset või lõiku on sinu jaoks normaalne e-kiri, postitus, Slack-sõnum. Ilma selleta kirjutab agent iga kanali sama pikkusega.

<!-- section: formatting | owner: D -->
## Vormistuse eelistused

[Kuidas sa ehitad üles e-kirju, dokumente ja sõnumeid. Punktikiri või lõigud, pealkirjadega või ilma, lühikesed või pikad.]

<!-- section: avoid | owner: D -->
<!-- quick-coverage: forbidden_mannerisms -->
## Mida ma väldin

[AI-nägu fraasid, kantseliit ja spetsiifilised maneerid, mis sind ärritavad. Asjad, mille pärast sa kirjutad mustandi nullist uuesti. Ole konkreetne: tsiteeri fraas, ära kirjelda kategooriat.]

Iga rida siin on agendi jaoks **kõva keeld**, mitte soovitus.

<!-- section: signatures | owner: D -->
## Signatuurid

[Sõnad, fraasid või harjumused, mis on selgelt sinu omad. Asjad, millest inimesed sind ära tunneksid. Samuti sõnad või väljendid, mida sa mitte kunagi ei kasuta.]
```

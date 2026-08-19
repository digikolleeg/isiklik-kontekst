# Süvenemine

Neli faili kiirest intervjuust katavad ühe töö. See juhend viib sealt edasi.

Kui sa pole veel intervjuud teinud, alusta [quick-start.md](quick-start.md) juurest. See leht eeldab, et sul on juba `identity.md`, `current-projects.md`, `communication-style.md` ja `writing-samples.md`.

---

## Miks üldse edasi minna

Neli faili teenindavad üht agenti hästi: seda, kes kirjutab sinu häälega väljapoole. Nad ei tee muud.

Mine edasi siis, kui sul on konkreetne teine töö, mida sa tahad ära anda:

| Sa tahad, et agent... | Vajab lisaks |
|---|---|
| valmistaks ette kohtumisi ja kirjutaks tuttavatele | `team-and-relationships.md` |
| kirjutaks sisu, mis su valdkonnas ka sisuliselt seisab | `domain-knowledge.md` |
| soovitaks asju, mis su päris töövoogu sobivad | `tools-and-systems.md`, `role-and-responsibilities.md` |
| kaaluks valikuid nii, nagu sina kaalud | `goals-and-priorities.md`, `preferences-and-constraints.md`, `decision-log.md` |

Kui ükski rida ei kirjelda praegust vajadust, ära ehita. Täidetud aga kasutamata fail on lihtsalt hooldusvõlg.

---

## Süsteemi kuju: 9 + 2

**9 profiilifaili** — mida sinu kohta teatakse:

`identity.md` · `role-and-responsibilities.md` · `current-projects.md` · `team-and-relationships.md` · `tools-and-systems.md` · `communication-style.md` · `goals-and-priorities.md` · `preferences-and-constraints.md` · `domain-knowledge.md`

**2 tõendifaili** — mille pealt seda teatakse:

`writing-samples.md` · `decision-log.md`

Tõendifail ei kirjelda sind. Ta hoiab toorainet: päris tekste ja päris otsuseid. Profiilifail väidab, tõendifail tõestab. `decision-log.md` ei ütle "ma otsustan analüütiliselt" — ta näitab kaht otsust, mille pealt seda näeb.

Kaart, mis fail mida hoiab ja kuhu ta edasi läheb, on `portfolio/context-map.md`.

---

## Süvarežiim: neli moodulit

Süvarežiim ei ole eraldi süsteem ega "pärast töötuba" tehtav asi. Ta on sama süsteemi järgmine sügavus ja ta ei alusta nullist: ta loeb, mis sul olemas on, ja täiendab.

Ta ei küsi faili kaupa, sest inimene ei mõtle faili kaupa. Ta küsib teema kaupa ja kirjutab tulemuse mitmesse faili korraga.

| Moodul | Nimi | Mida katab |
|---|---|---|
| **A** | töö-tegelikkus | roll, vastutused, rütmid, aktiivsed projektid, tööriistad |
| **B** | turg-ja-ekspertiis | ICP, pakkumine, käivitaja, otsingusisend, valdkonnateadmised |
| **C** | otsused-ja-piirid | eesmärgid, kompromissid, kõvad reeglid, otsuste logi |
| **D** | hääl-ja-inimesed | kirjutamisstiil, kirjutamisnäited, suhted |

### Kolm asja, mis moodulid kasutatavaks teevad

**Iga moodul salvestab lõpus.** Sa võid ühe mooduli teha teisipäeval ja järgmise kahe nädala pärast. Pooleli tööd ei kao.

**Iga sektsioon kuulub täpselt ühele moodulile.** Kaks moodulit ei kirjuta üksteist üle. Kui moodul B märkab midagi, mis kuulub mooduli C sektsiooni, läheb see tähelepanek kandidaadiregistrisse, mitte otse faili.

**Moodul D algab impordist, mitte küsimusest.** Häält ei intervjueerita. Küsimusele "kuidas sa kirjutad" vastab inimene mälu järgi ja ilustab. Süvarežiim küsib päris tekste ja loeb hääle nendest välja.

### Kuidas käivitada

Ütle Skillile **"süvaintervjuu"**. Ta küsib, millest moodulist alustada, ja käib selle läbi.

Üks moodul on üks istung, umbes 30–45 minutit. Sa ei pea neid järjest tegema ega ühes järjekorras läbima — vali see, mille tulemust sul kõige rohkem vaja on.

Enne küsimist loeb süvarežiim kolm asja: olemasolevad failid (ei küsi üle, mis on kaetud), kandidaadiregistri (seal ootab kiire režiimi üks vaatlus oma teist tõendit) ja `review_after` kuupäevad (pakub aegunud faili üle vaadata).

**Kui sul on puudu konkreetne fail:** ütle `täida goals-and-priorities.md` või `uuendame current-projects.md`. Skill suunab sind faili omanikmoodulisse; `current-projects.md` puhul küsib ta, kas vajad töö-tegelikkuse (A) või turu-ja-ekspertiisi (B) osa. Ilma Skillita ava šabloon `portfolio/templates/` kaustast, kleebi see AI-vestlusesse ja ütle „alustame sellega“.

`decision-log.md` on kõige mõttekam siis, kui sul on kaks päris otsust, mida kirjeldada. Ilma nendeta jääb ta abstraktseks ja kasutuks.

---

## Väited, tõendid ja kandidaadid

Iga püsiv väide kannab staatust:

| Staatus | Millal | Kas agent tohib toetuda |
|---|---|---|
| `kinnitatud` | sa ütlesid seda ise | jah |
| `toetatud` | muster, mida katab kaks **sõltumatut** näidet | jah |
| `kandidaat` | üks vaatlus või AI-tuletus | ei |

**Sõltumatu** tähendab kahte eri allikat: kaks eri meili, kaks eri otsust. Kaks lõiku samast meilist on üks allikas ja ei tõesta midagi. Kaks eri meili on kaks allikat ja tõestavad, ka siis kui kanal on sama.

Kandidaadid elavad `portfolio/_candidates.md` registris koos sihtfaili, sektsiooni ja aegumiskuupäevaga. Nad ei lähe ühessegi agendipakki. Süvarežiimi konkreetne töö on need üles tõsta või maha kanda — ja ta teeb seda nähtava muudatusega, mille sa kinnitad, mitte vaikselt.

---

## Agendipakid

`portfolio/bundles/` all on kolm valmis pakki: outreach, kliendi-uurija, sisukirjutaja.

Pakk on **projektsioon**. Ta ei hoia konteksti — ta paneb selle kokku failidest, mis on tema päises `sources` all kirjas. Kolm reeglit kehtivad igaühele:

- kandidaat-väited jäetakse kokkupanekul välja
- `restricted` failid jäävad vaikimisi välja
- kui allikafail muutub, nõelu pakk uuesti; ära paranda pakki käsitsi, sest siis läheb ta allikast lahku ja keegi ei märka

Kui vajalik allikas on `restricted`, kandub see märge kogu pakile. Näiteks kliendinimedega `writing-samples.md` tähendab, et valmis kirjutamispakk ei ole enam `exportable`.

Uue paki tegemine: kopeeri olemasolev, vaheta allikad ja sissejuhatus. Kolm kuni neli allikafaili on tavaliselt õige maht.

---

## Privaatsus

`team-and-relationships.md` on alati `restricted`. Ta sisaldab hinnanguid nimeliste inimeste kohta — see on kolmandate isikute andmed, mitte sinu omad.

Ta ei kuulu ühegi paki vaikimisi koosseisu. Kui sa ta lisad, muutub kogu pakk `restricted`-iks: kasuta seda ainult enda valitud privaatses tööriistas, ära jaga pakki ega anna agendile autonoomset saatmisõigust.

Ülejäänud on vaikimisi `exportable`. Iga faili päises on `sensitivity` väli, mille sa võid ise ümber panna.

---

## Hooldus

Iga faili päises on kaks kuupäeva: `updated` ja `review_after`. Süvarežiim loeb `review_after` välja ja pakub aegunud faili üle vaadata, enne kui uute küsimuste juurde läheb.

| Fail | Vaata üle |
|---|---|
| `current-projects.md` | kuu aja tagant |
| kõik ülejäänud | kvartali tagant või kui midagi olulist muutub |

Uuendamine Skilliga: *"uuendame `current-projects.md` — siin on, mis muutus."* Skill loeb vana faili, küsib ainult vahet ja näitab muudatust enne salvestamist.

Kui parandad AI mustandit enne päris kasutust, ütle samas vestluses `õpime parandusest` ja kleebi ainult lõpptekst. Skill teeb algse mustandiga diffi, klassifitseerib parandused ja küsib enne konteksti muutmist kinnituse. Üks parandussündmus ei muutu automaatselt üldreegliks.

Kui portfooliofail muutub, vajavad seda kasutavad agendipakid uut kokkupanekut. Vastasel juhul töötab agent vana kontekstiga ja sa ei saa sellest teada enne, kui midagi läheb valesti.

Kas asi ikka töötab — [RUBRIC.md](RUBRIC.md).

---

## Kaks valikulist laiendust

Kumbki ei ole vajalik ja kumbagi ei ole mõtet enne teha, kui põhirada töötab.

**Ühendused teiste tööriistadega** — `wiring/` all on juhendid ChatGPT, Gemini, Claude Projects, MCP ja Obsidiani jaoks. Alusta sellest tööriistast, mida sa kõige rohkem kasutad.

**Wiki-kiht** — eraldi süsteem sinu loetud materjali jaoks: pane allikas `raw/` kausta, LLM loeb selle ja ehitab lehed `wiki/` alla. Portfoolio töötab ilma selleta täielikult. Töövood on [CLAUDE.md](CLAUDE.md).

Juurkausta `index.md` kuulub wiki-kihile. Portfoolio oma kaart on `portfolio/context-map.md` — need on eri asjad ja neid ei sünkroonita.

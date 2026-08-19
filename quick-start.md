# Kiire algus — töötav AI-assistent ühe istumisega

Sa annad AI-le konteksti enda ja oma ettevõtte kohta, ja paned ta tegema ühte päris tööd, mida sa niikuinii kordad.

**Ajakulu:** 30–40 minutit intervjuud + umbes 15 minutit ülejäänut.
**Vaja:** üks päris sihtklient meeles. Ei midagi muud.

---

## Enne kui alustad: vali töö

Ära alusta failidest. Alusta tööst.

Vali **üks asi, mida sa kordad** ja mis võtab aega:

- külmad kontaktimeilid potentsiaalsetele klientidele
- järelkajad, mis jäävad kirjutamata
- LinkedIni postitused
- pakkumiste kaaskirjad

Hoia see meeles kogu intervjuu vältel. Selle järgi otsustad lõpus, kas asi töötab.

Ülejäänud juhend eeldab, et valisid kontaktimeili. Muu töö puhul on sammud samad, ainult 3. sammu agendipakk on teine.

---

## 1. samm — Tee intervjuu (30–40 min)

Kaks rada. **Sama tulemus, sama neli faili.** Vali see, mis sul käepärast on.

### Rada A — Skilliga (kiirem, kui sul on Claude Desktop)

Skill viib intervjuu läbi ja kirjutab failid ise valmis.

1. Installi Konteksti-looja Skill — juhend: [skills/konteksti-looja/README.md](skills/konteksti-looja/README.md).
2. Ava uus vestlus ja ütle: **"töötoa intervjuu"**.
3. Vasta küsimustele. Skill näitab iga faili mustandit ja küsib, mis on valesti.

Kui sa tööd Cowork-kaustas teed, kirjutab Skill failid otse sinna ja sa näed neid tekkimas. Kui ei, näitab ta failide sisu vestluses ja sa salvestad need ise. Mõlemad toimivad.

### Rada B — Ilma installimata

Töötab suvalises AI-vestluses, ka tasuta plaaniga.

1. Ava [quick-interview.md](quick-interview.md) selle repo juurest.
2. Kopeeri kogu fail ja kleebi see uue vestluse esimeseks sõnumiks.
3. Kirjuta: **"kiire intervjuu"**.
4. Vasta küsimustele. Salvesta iga valmis fail ise arvutisse.

> `quick-interview.md` on külmutatud fail: ta ei muutu su jala alt ära, kui sa oled intervjuu juba alustanud.

### Mida intervjuu sinult ootab

Enne küsimusi palub ta sul olemasolev materjal sisse visata — ettevõtte tutvustus, veebilehe tekst, paar päris meili või postitust. Mida rohkem sa annad, seda vähem ta küsib.

**Valmis kiire intervjuu vajab vähemalt kaht sõnasõnalist näidet sinu tekstist.** Mitte ümberjutustust ega poleeritud „Meist“ teksti. Päris saadetud meil, päris postitus. Enne talletamist näitab intervjuu sulle, millised kliendinimed ja tundlikud numbrid ta asendaks; sina kinnitad redaktsiooni. Kui tahad need alles jätta, märgitakse `writing-samples.md` fail `restricted`. Kui sul näiteid veel pole, teeb intervjuu kaks kalibreerimismustandit ja talletab ainult sinu parandatud versioonid.

---

## 2. samm — Sul on neli faili

| Fail | Mida ta agendile ütleb |
|---|---|
| `identity.md` | kes sa oled |
| `current-projects.md` | mida sa müüd, kellele, mis päästikul, otsingu kolmik sektor/suurus/piirkond, ja mida **ei tohi** väita |
| `communication-style.md` | kuidas sa kirjutad |
| `writing-samples.md` | kuidas sa päriselt kõlad |

Hoia neid ühes kaustas. Nimed peavad olema täpselt need — agendipakid otsivad neid nime järgi.

Loe failid korra läbi. Paranda kohe, mis on valesti: intervjuu järel on see viie minuti töö, kuu aja pärast on see arheoloogia.

---

## 3. samm — Anna agendile päris ülesanne (~10 min)

1. Ava `portfolio/bundles/client-outreach.md`.
2. Kontrolli failide päisest `sensitivity` väärtust. Kleebi oma nelja faili sisu vastavatesse kohtadesse (`[[IDENTITY]]`, `[[PROJECTS]]`, `[[VOICE]]`, `[[SAMPLES]]`). Pakis on kirjas, mis kuhu läheb. Kui kasvõi üks fail on `restricted`, on ka kogu kokku pandud pakk `restricted`: kasuta seda ainult enda valitud privaatses agendis ja ära jaga.
3. Kleebi kokku pandud tekst agendi süsteemipromptiks — Claude Projecti custom instructions, Custom GPT, Gemini Gem, ükskõik mis.
4. Küsi ühe **päris** sihtkliendi kohta sõnum:

> *"Koosta kontaktimeil [nimi], firma [firma]. Eesmärk: [mida sa tahad]."*

Väljamõeldud sihtklient ei ütle sulle midagi. Võta keegi, kellele sa võiksid täna päriselt kirjutada.

---

## 4. samm — Enne ja pärast (~5 min)

See on ainus kontroll, mis loeb.

1. Ava **uus vestlus ilma igasuguse kontekstita**. Küsi sama sõnum sama sihtkliendi kohta.
2. Pane kaks tulemust kõrvuti.

**Kui vahet on** — konkreetsem pakkumine, sinu sõnavara, õige pikkus, ei mingit "loodan, et see kiri leiab teid hea tervise juures" — siis kontekst töötab.

**Kui vahet pole**, on failid liiga üldsõnalised. Kõige tavalisem põhjus on `writing-samples.md`, kuhu pandi poleeritud turundustekst päris kirja asemel. Teine on `current-projects.md`, kus pakkumine on kirjas kategooriana ("konsultatsiooniteenused"), mitte konkreetselt.

Kontrolli veel kolme asja:

- **Kas mõni fakt on välja mõeldud?** Number, sertifikaat, kliendinimi, mida sa ei andnud. Kui jah, on `current-projects.md` sektsioon "Mida ei tohi väita" tühi või liiga leebe.
- **Kas kõlab sinuna?** Loe valjusti. Kui sa ei ütleks seda lauset elus välja, ei ole see sinu hääl.
- **Kas sa saadaksid selle ära?** Ainus küsimus, mis päriselt loeb.

Täielik kontrollnimekiri on [RUBRIC.md](RUBRIC.md).

Kui toimetasid agendi mustandit ja saatsid või avaldasid lõpliku versiooni, ütle **samas vestluses** `õpime parandusest` ja kleebi ainult lõpptekst. Agent teeb enda mustandiga diffi, liigitab parandused ja küsib enne konteksti muutmist kinnituse.

---

## Kolm artefakti ühest kontekstist

Kui esimene sõnum töötab, küsi samas vestluses juurde:

> *"Nüüd LinkedIni sõnum samale inimesele."*
> *"Nüüd järelkaja, kui ta nädalaga ei vasta."*

Sama kontekst, kolm väljundit, ilma uuesti seletamata. Selle pärast see süsteem üldse on.

---

## Mis edasi

Neli faili katavad ühe töö hästi. Süsteemis on üksteist faili — 9 profiili ja 2 tõendikorpust — ja süvarežiim, mis loeb sinu olemasolevad failid sisse ja täiendab neid moodulite kaupa.

See ei ole "kunagi hiljem". Kui sa tahad järgmisel nädalal juurde minna, on [GETTING-STARTED.md](GETTING-STARTED.md) järgmine samm.

Muude tööriistade ühendamine (ChatGPT, Gemini, MCP, Obsidian) on `wiring/` all. See on vabatahtlik ja tuleb pärast, mitte enne.

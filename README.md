# Isiklik kontekst

Üks korrastatud kontekstiallikas, millest saad anda igale AI-agendile just tema tööks vajaliku osa.

---

## Probleem

Iga AI tööriist vajab kahte asja, et olla päriselt kasulik. Ta peab teadma, *kes sa oled* (roll, eesmärgid, eelistused, piirangud) ja *mida sa tead* (uurimismaterjal, koosolekumärkmed, valdkonna teadmised).

Enamik inimesi seletab esimest iga vestlusega nullist uuesti. Teine kaob täielikult, kui vestlus suletakse.

See süsteem lahendab mõlemad.

---

## Lihtsaim rada, kui sa alles alustad

Viis sammu. Ei mingit seadistamist enne esimest sammu.

1. **Vali üks päris töö, mida sa kordad.** Külmad kontaktimeilid. Pakkumised. LinkedIni postitused. Üks asi, mida sa teed vähemalt kord nädalas ja mis võtab aega.
2. **Tee kiire intervjuu.** 30–40 minutit. [quick-start.md](quick-start.md) näitab mõlemat rada — installitud Skilliga või ilma.
3. **Saad neli faili.** Need on allpool.
4. **Anna agendile üks päris ülesanne.** Võta `portfolio/bundles/client-outreach.md`, kleebi oma failid sisse ja lase kirjutada sõnum ühele **päris** sihtkliendile.
5. **Kontrolli enne ja pärast.** Lase samal agendil kirjutada sama sõnum ilma sinu kontekstita ja sinu kontekstiga. Vahe on kogu asja mõte. Kui vahet pole, on failid liiga üldsõnalised — [RUBRIC.md](RUBRIC.md) ütleb, kust otsida.

Kõik muu selles repos on selle raja laiendus. Sa ei vaja midagi sellest, et esimest korda kasu saada.

---

## Kust alustada

| Sa tahad | Mine siia |
|---|---|
| Proovida kohe, ilma midagi installimata | [quick-start.md](quick-start.md) |
| Panna Skill püsivalt tööle | [skills/konteksti-looja/README.md](skills/konteksti-looja/README.md) |
| Kontrollida, kas tulemus on midagi väärt | [RUBRIC.md](RUBRIC.md) |
| Minna kaugemale kui neli faili | [GETTING-STARTED.md](GETTING-STARTED.md) |
| Ühendada kontekst teiste tööriistadega | [wiring/](wiring/) |

---

## Neli faili, millest piisab alustamiseks

Kiire intervjuu koostab täpselt need neli, 30–40 minutiga. Alusta nendest.

| Fail | Mida talletab |
|---|---|
| `identity.md` | kes sa oled, see fail, mida agent loeb, kui ta võib lugeda ainult ühte |
| `current-projects.md` | mida sa praegu müüd, kellele, mis päästikul |
| `communication-style.md` | kuidas sa kirjutad ja kuidas tahad, et sinu nimel kirjutatakse |
| `writing-samples.md` | päris näited sinu enda tekstist |

`writing-samples.md` on see, mille inimesed vahele jätavad ja mille pealt kõik laguneb. Reeglid ütlevad agendile, mida vältida. Näited näitavad, mida teha. Ilma näideteta kõlab iga agent nagu masin.

Sellepärast on ta kohustuslik, mitte soovituslik: lõpetatud kiire intervjuu sisaldab vähemalt kaht sõnasõnalist näidet. Kui sa katkestad varem, jääb puuduv näidis failis nähtavalt katmata.

---

## Terve süsteem: 9 profiili + 2 tõendit

Süsteemis on üksteist faili kahes eri rollis. See vahe on oluline, mitte kosmeetiline.

**9 profiilifaili** — mida sinu kohta teatakse:

`identity.md` · `role-and-responsibilities.md` · `current-projects.md` · `team-and-relationships.md` · `tools-and-systems.md` · `communication-style.md` · `goals-and-priorities.md` · `preferences-and-constraints.md` · `domain-knowledge.md`

**2 tõendifaili** — mille pealt seda teatakse:

`writing-samples.md` (päris tekstid) · `decision-log.md` (päris otsused)

Tõendifail ei ole profiiliteema. Ta on korpus, mille pealt profiiliväiteid kontrollitakse. `communication-style.md` ütleb "ma kirjutan lühidalt"; `writing-samples.md` tõestab seda või lükkab ümber.

Šabloonid on `portfolio/templates/`, täidetud näidised `portfolio/examples/`.

---

## Kuidas väiteid märgistatakse

Iga püsiv väide kannab staatust. See on see, mis eristab teadmist oletusest.

| Staatus | Millal | Kas agent tohib sellele toetuda |
|---|---|---|
| `kinnitatud` | sa ütlesid seda ise | jah |
| `toetatud` | muster, mida katab kaks sõltumatut päris näidet | jah |
| `kandidaat` | üks vaatlus või AI-tuletus | ei, oletusena |

Kandidaadid elavad `portfolio/_candidates.md` registris ja ootavad teist tõendit. Nad ei lähe ühessegi agendipakki.

Kiire intervjuu jõuab kõigi kolme tasemeni. Ta ei ole oletusevabrik: sinu enda öeldu on kohe `kinnitatud`, ja kaks päris kirjutamisnäidet annavad `toetatud` mustri.

---

## Bundle on projektsioon, mitte koopia

`portfolio/bundles/` all on valmis agendipakid — outreach, kliendi-uurija, sisukirjutaja. Pakk **ei hoia** konteksti. Ta paneb selle kokku failidest, mis on tema päises kirjas.

Sellest järeldub kolm reeglit, mis on kõigis pakkides sees:

- kandidaat-väited jäetakse kokkupanekul välja
- `restricted` failid jäävad vaikimisi välja
- kui allikas muutub, nõelu pakk uuesti, ära paranda pakki käsitsi

Kui mõni vajalik allikas on `restricted` — näiteks kliendinimedega `writing-samples.md` — ei ole valmis pakk enam `exportable`. Tundlikkus kandub allikast kogu pakile; puuduva häälefailiga pakki ei nimetata vaikselt valmis tulemuseks.

Kogu kaart — mis fail mida hoiab ja kuhu ta edasi läheb — on `portfolio/context-map.md`.

---

## Privaatsus

`team-and-relationships.md` on alati `restricted`. Ta sisaldab hinnanguid nimeliste inimeste kohta. Ta ei kuulu ühegi agendipaki vaikimisi koosseisu. Kui sa ta ikkagi sisse paned, muutub kogu pakk `restricted`-iks: kasuta seda ainult enda valitud privaatses agendis, ära jaga pakki ja ära lase väljundisse kolmanda isiku hinnanguid.

Ülejäänud on vaikimisi `exportable`. Sa võid iga faili ise ümber märkida.

---

## Kui neli faili on täis

Süvarežiim on järgmine sügavus, mitte "kunagi hiljem". Ta ei ole eraldi süsteem ja ta ei alusta nullist — ta loeb, mis sul olemas on, ja täiendab.

Neli moodulit, igaüks eraldi läbitav ja katkestatav:

| Moodul | Mida katab |
|---|---|
| **A** töö-tegelikkus | roll, rütmid, aktiivsed projektid, tööriistad |
| **B** turg-ja-ekspertiis | ICP, pakkumine, käivitaja, valdkonnateadmised |
| **C** otsused-ja-piirid | eesmärgid, kõvad reeglid, otsuste logi |
| **D** hääl-ja-inimesed | kirjutamisstiil, näidised, suhted |

Moodul salvestab lõpus, nii et sa võid pausile jääda ja nädala pärast samast kohast jätkata. Moodul D algab su päris tekstide importimisest, mitte küsimusest — häält ei intervjueerita, hääl imporditakse.

Käivitamiseks ütle Skillile **`süvaintervjuu`**.

Vaata [GETTING-STARTED.md](GETTING-STARTED.md).

---

## Kontekst paraneb päris tööst

Kui toimetad AI mustandi enne saatmist või avaldamist, anna lõplik tekst samas vestluses tagasi ja ütle `õpime parandusest`. Algne mustand on agendil juba olemas, seega piisab ühest kleepimisest.

Skill teeb diffi, eristab fakti, üldise stiili, kanali, adressaadi erandi ja ajutise projektikonteksti ning näitab pakutud muudatused enne salvestamist. Üks redaktsioon ei muutu automaatselt üldreegliks. Täpne töövoog: [correction-loop.md](skills/konteksti-looja/references/correction-loop.md).

---

## Wiki-kiht (valikuline, eraldi)

Teine, sõltumatu kiht: kasvav teadmiste baas su loetud materjalist. Portfoolio töötab ilma selleta täielikult.

**Kui sa alles alustad, jäta see praegu rahule.** Ta ei ole osa ülalkirjeldatud rajast.

```
raw/      ← pane allikad siia (muutmatud)
wiki/     ← LLM-i loodud lehed
index.md  ← wiki register (see ei ole portfoolio kaart)
log.md    ← wiki logi
```

Töövood: [CLAUDE.md](CLAUDE.md).

---

## Repo struktuur

```
/
├── README.md
├── quick-start.md          ← esimene 30-40 minutit
├── GETTING-STARTED.md      ← süvenemine, moodulid, hooldus
├── RUBRIC.md               ← kas tulemus on midagi väärt
├── CLAUDE.md               ← wiki-kihi töövood
├── skills/konteksti-looja/ ← intervjuu-Skill
├── portfolio/
│   ├── templates/          ← 9 + 2 šablooni intervjuu-protokollidega
│   ├── examples/           ← täidetud näidised
│   ├── bundles/            ← agendipakid (projektsioonid)
│   ├── context-map.md      ← mis fail mida hoiab
│   └── _candidates.md      ← kandidaat-väidete register
├── raw/ · wiki/            ← wiki-kiht (valikuline)
└── wiring/                 ← ühendused teiste AI tööriistadega
```

---

## Disainipõhimõtted

**Markdown ennekõike.** Iga AI süsteem oskab markdown'i lugeda. Pole andmebaase, embedding-mudeleid ega kinniseid formaate.

**Inimene kinnitab, LLM kirjutab.** Agent pakub, sina kinnitad. Ükski järeldus ei lähe püsikonteksti ilma sinu heakskiiduta.

**Tõend enne väidet.** Muster, mida katab üks vaatlus, on kandidaat. Kaks sõltumatut näidet teevad temast teadmise.

**Kaasaskantav igal pool.** Claude, ChatGPT, Gemini, ükskõik mis faile loeb. Sa pole lukus ühegi tootja küljes.

**Modulaarne.** Portfoolio ja wiki on iseseisvad. Kasuta ühte, kasuta mõlemaid.

---

## Litsents

MIT.

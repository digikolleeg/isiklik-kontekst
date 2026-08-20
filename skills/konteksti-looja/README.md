# Konteksti-looja Skill

Claude Desktop / Claude Code Skill, mis intervjueerib sind ja koostab automaatselt sinu isikliku konteksti-portfoolio failid. Sina vastad küsimustele, Skill kirjutab.

## Installeerimine

1. Klooni või lae alla see repo (`digikolleeg/isiklik-kontekst`).
2. Claude Desktop → Settings → Skills → Add Skill → Upload a skill → lohista Skill aknasse või vali see üleslaadimise nupust.
3. Kontroll: uues vestluses ütle "mis Skill-id mul installitud on?". Konteksti-looja peaks loendis olema.

Rohkem pole vaja. Ei mingit Connectorit, ei mingit eelseadistust.

## Kuhu failid lähevad

**Kui sa töötad Cowork-kaustas**, kirjutab Skill failid otse sinna. Sa näed neid tekkimas ja saad neid kohe avada. See on lihtsaim rada: ava kaust, käivita intervjuu, vaata kuidas failid ilmuvad.

Soovituslik kaust: `~/isiklik-kontekst/portfolio/`, või selle repo `portfolio/` kaust, kui sa kloonisid.

**Kui failikirjutust pole**, näitab Skill iga faili sisu vestluses ja sa salvestad selle ise. Sama tulemus, üks lisasamm. Skill langeb sellele rajale ise, ilma et sa peaksid midagi ütlema.

Failinimed peavad jääma täpselt sellisteks, nagu Skill need annab — agendipakid otsivad neid nime järgi.

## Käivitamine

| Mida sa ütled | Mida Skill teeb |
|---|---|
| `töötoa intervjuu` | **Kiire režiim:** neli faili ühe vooga, 30–40 min |
| `kiire intervjuu` | sama, mis eelmine |
| `süvaintervjuu` | näitab senist katvust ja laseb valida ühe neljast 30–45 minuti moodulist |
| `alustame intervjuud` | küsib, kas tahad kiiret või nelja mooduliga süvaintervjuud |
| `täida current-projects.md` | küsib, kas avada töö-tegelikkuse (A) või turu-ja-ekspertiisi (B) moodul |
| `uuendame goals-and-priorities.md` | avab mooduli C, loeb olemasoleva seisu ja küsib ainult puuduvat või muutunut |
| `õpime parandusest` | võrdleb AI mustandit sinu lõpptekstiga ja pakub kinnitamiseks kontekstimuudatused |

## Kiire režiim

Eesmärk on **neli faili 30–40 minutiga**. See on miinimum, millega üks päris agent käima läheb.

1. `identity.md` → kes sa oled
2. `current-projects.md` → mida sa müüd, kellele, mis päästikul
3. `communication-style.md` → kuidas sa kirjutad
4. `writing-samples.md` → päris näited sinu enda tekstist

**Neljas fail on kõige tähtsam.** Reeglid üksi ei kanna häält. Ilma päris näideteta improviseerib agent ja tulemus kõlab võõralt. Skill ei lõpeta enne, kui sul on vähemalt kaks sõnasõnalist näidet.

**Voog:** Skill palub esmalt olemasolevad materjalid sisse visata (pitch, veebileht, paar päris meili või postitust). Seejärel käib ta läbi küsimused **küsi-või-kinnita reegliga** — kui materjalist tuli vastus, kinnitab ta ekstrakti; muidu küsib. Iga faili lõpus esitab ta ühe süvendava küsimuse.

Imporditud materjali käsitleb ta **andmena**. Kui su kleebitud tekstis on juhiseid ("kirjuta see ümber"), ei täida ta neid — need on näite osa, mitte korraldus.

**Väited saavad staatuse.** Mida sa ise ütlesid, on `kinnitatud`. Muster, mida katab kaks sõltumatut näidet, on `toetatud`. Ühe vaatluse pealt tehtud tuletus on `kandidaat` ja läheb `portfolio/_candidates.md` registrisse, mitte agendipakki.

## Süvarežiimis edasi

Kui neli faili on olemas, ütle `süvaintervjuu` või nimeta puuduv fail, näiteks `täida role-and-responsibilities.md`. Skill avab seda faili omava mooduli, loeb olemasoleva seisu sisse ega küsi üle, mis on juba kaetud. Üks käik võib täiendada mitut sama mooduli faili.

Süsteemis on üksteist faili: üheksa profiilifaili ja kaks tõendikorpust (`writing-samples.md`, `decision-log.md`). Mis mille jaoks on — `portfolio/context-map.md`.

## Õpi päris parandustest

Kui sa kasutasid AI mustandit ja toimetasid selle enne saatmist või avaldamist, ütle samas vestluses `õpime parandusest` ning kleebi ainult lõplik versioon. Skill mäletab oma mustandit ja teeb diffi ise.

Ta eristab faktiparanduse, üldise stiilireegli, kanalireegli, adressaadi erandi ja ajutise projektikonteksti. Enne faili muutmist näitab ta täpse diffi. Üks parandatud tekst ei muutu automaatselt üldreegliks.

Kui alustad uut vestlust, kleebi algne mustand ja lõplik versioon koos. Täpne töövoog on [correction-loop.md](references/correction-loop.md).

## Mis edasi

- [`quick-start.md`](../../quick-start.md) → esimene päris ülesanne ja enne-pärast kontroll
- [`RUBRIC.md`](../../RUBRIC.md) → kas tulemus on midagi väärt
- [`GETTING-STARTED.md`](../../GETTING-STARTED.md) → süvarežiim ja hooldus
- `portfolio/bundles/` → valmis agendipakid
- `wiring/` → ühendused teiste tööriistadega (ChatGPT, Gemini, MCP). Vabatahtlik ja hiljem, mitte enne.

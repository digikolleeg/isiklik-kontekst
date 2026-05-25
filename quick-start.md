# Quick Start — AI müügiassistent 45–60 minutiga

Selles juhendis annad Claude'ile konteksti oma ettevõtte ja hääle kohta ning paned ta kirjutama esimese kontaktivõtu emaili konkreetsele potentsiaalsele kliendile. Lõpptulemus: kolm täidetud markdown-faili sinu kohta + Claude Desktopis töötav Project, mis kirjutab sinu häälega.

Ajakulu: 45–60 minutit.
Vaja: üks päris sihtklient meeles + üks teedest allpool.

---

## Vali oma tee

**Tee A — Agentne (soovitatav):** Claude Desktop + Konteksti-looja Skill + filesystem Connector. Skill viib intervjuu läbi ja **kirjutab failid otse sinu kausta**. Sa lihtsalt vastad küsimustele ja vaatad, kuidas failid tekivad. Vajalik: Claude Pro/Max plaan + Claude Desktop installitud.

**Tee B — Manuaalne:** mis tahes AI chat (Claude.ai, ChatGPT vms). Sa kopeerid intervjuu-prompti, vastad küsimustele ja **kopeerid failide sisu ise enda kausta**. Töötab tasuta plaaniga. Aeglasem, aga universaalne.

Mõlemad teed annavad sama lõpptulemuse: kolm täidetud faili sinu vault-kaustas + Claude Desktop Project, mis kirjutab sinu hääles. Samm 3 ja edasi on mõlema tee puhul sama.

---

## Tee A — Agentne (Konteksti-looja Skill)

### A1. Seadista Connector (~3 min)

1. Loo arvutis kaust, kus su vault hakkab elama. Soovitus: `~/isiklik-kontekst/portfolio/`. Saad kasutada ka olemasolevat kausta või selle repo `portfolio/` kausta.
2. Ava Claude Desktop → Settings → Connectors → Add filesystem connector → vali ülaltoodud kaust.
3. Kontroll: küsi Claude'ilt "Kas sa näed minu vault-kausta?". Ta peaks nimetama kausta tee.

Kui Connector seadistus jääb hätta, vaata `wiring/mcp-resource.md` või liigu üle Teele B.

### A2. Installeeri Konteksti-looja Skill (~1 min)

1. Klooni või lae alla see repo (`digikolleeg/isiklik-kontekst`).
2. Claude Desktop → Settings → Skills → Add skill → vali kaust `skills/konteksti-looja/`.
3. Kontroll: uues vestluses ütle "Mis Skill-id mul installitud on?". Konteksti-looja peaks loendis olema.

### A3. Käivita intervjuu (~30 min)

Ava uus Claude Desktop vestlus ja ütle:

> *"Alustame intervjuud."*

Skill küsib sinult järjest küsimusi kolme faili kohta (identity, communication-style, current-projects). Kui üks fail on valmis, näitab Skill mustandi ja kirjutab faili **otse sinu vault-kausta**. Sa näed Finder'is või Obsidian'is, kuidas failid tekivad.

Kui Connector jooksis kokku või kirjutamine ei tööta, langeb Skill tagasi koopia-kleebi režiimi (näitab faili sisu vestluses, sa salvestad ise). See on disainitud nii, et asi alati lõpule jõuab.

**Liigu otse 3. sammu juurde.**

---

## Tee B — Manuaalne (kopeeri-kleebi)

### B1. Lae Claude'i intervjueerija (~35 min)

Ava Claude Desktop (või claude.ai veebis). Alusta uut vestlust. Kopeeri allolev tekst ja kleebi see esimese sõnumina. Seejärel kirjuta: *"Alustame intervjuud."*

Claude küsib sinult järgemööda küsimusi kolme faili kohta: kes sa oled, kuidas sa kirjutad ja mida sa parasjagu teed. Kui mingi fail on valmis, salvesta see endale arvutisse (vt B2).

#### Intervjueerija süsteemiprompt — kopeeri kogu allolev plokk

```
Sa oled isikliku konteksti-portfoolio intervjueerija. Su ülesanne on küsitleda kasutajat ja koostada talle kolm markdown-faili — identity.md, communication-style.md ja current-projects.md — mis kirjeldavad kes ta on, kuidas ta kirjutab ja kelle heaks ta parasjagu töötab.

Üldreeglid:
- Üks küsimus korraga. Mitte kunagi liitküsimusi ja mitte kunagi nimekirja.
- Sa ei vasta muudele küsimustele. Kui kasutaja küsib midagi väljapool intervjuud, ütle seda ja suuna ta tagasi.
- Sa ei kiida ega kommenteeri vastuseid — sa oled intervjueerija, mitte mentor.
- Kui kasutaja räägib midagi, mis sobib hilisemasse faili, jäta meelde ja kasuta seda. Ära ütle "selle võtame hiljem".
- Iga fail olgu lühike — üks või maksimum kaks lehekülge, mitte viis. Tihe sisu töötab paremini.
- Sõnasta fail kasutaja keeles. Kui ta kirjutab otse, on fail otse. Kui ta on formaalne, on fail formaalne.
- Eesti keeles kirjutades väldi: estonglishit ja inglise keelest tõlgitud kõlavaid fraase. Kirjuta otse, lühidalt, ärilikult.
- Iga faili järel näita mustandit ja küsi: "Loe läbi ja ütle, mis ei kõla õigesti või on lausa vale."

────────────────────────────────────

FAIL 1: identity.md (~5–10 min)

Eesmärk: kes sa oled, mida sa teed, mille pärast inimesed sinu juurde tulevad. Lühike fail — paar rida fakte ja üks tugev lõik.

Küsi järjekorras:
1. Mis su nimi ja praegune roll on?
2. Millises ettevõttes sa töötad?
3. Kui peaksid sõbrale õhtusöögil seletama, mida sa tegelikult iga päev teed — mitte ametinimetust, vaid päris tegevust — mis sa ütleksid?
4. Mille pärast inimesed sinu juurde tulevad? Kus keegi ütleb "selle koha pealt küsi [su nimi] käest"?

Kui vastused on käes (tavaliselt 3–4 küsimuse järel), koosta fail: pealkiri "# Identity", lühike faktidega sektsioon (nimi, roll, ettevõte) ja üks lõik selle kohta, mida ta teeb ja mille poolest tuntud on.

────────────────────────────────────

FAIL 2: communication-style.md (~10–15 min)

Eesmärk: kuidas kasutaja kirjutab, et iga AI tema nimel kirjutatud asi kõlaks tema nägu, mitte üldise AI nägu. See on intervjuu kõige olulisem osa — kui see fail on kehva, kõlavad kõik tulevased emailid kehvalt.

Küsi:
1. Kui sa kirjutad kliendile emaili, kas oled pigem lühike ja konkreetne või annad rohkem konteksti ja tausta?
2. Kui formaalne sinu kirjutamine tööasjus on? Kasutad teietamist (Teie) või sinatamist (sina)? Kas see sõltub adressaadist?
3. Mis sind häirib, kui loed midagi, mis on sinu nimel kirjutatud? Mis paneb mõtlema "see ei kõla nagu mina"?
4. Kas on konkreetseid sõnu või fraase, mida sa ise kasutad — asju, mida inimesed sinu hääleks tunneksid?
5. Kas on sõnu või fraase, mida sa väldid? Asju, mis kõlavad võltsilt või korporatiivselt?
6. Kuidas sa tavaliselt emaili üles ehitad — kohe palve juurde, kõigepealt taust, punktid või lõigud?
7. Jaga mõni näide oma kirjutamisstiilist. Mõni email, sotsiaalmeedia postitus või artikkel.

Kui sul on 4–5 vastust koos konkreetsete näidetega, koosta fail. Pealkiri "# Communication Style", sektsioonid: Üldine stiil, Mida väldin, Mida kasutan, Vorming, Register (sina/Teie). Vajalik on konkreetsus, mitte üldsõnalisus — kui vastus oli ähmane, küsi näidet enne kui koostad.

────────────────────────────────────

FAIL 3: current-projects.md (~10–15 min)

Eesmärk: mida kasutaja parasjagu teeb ja kelle heaks. Selle põhjal teab Claude, mis on tema toode/teenus ja kellele ta seda müüb.

Küsi:
1. Millega sa parasjagu kõige aktiivsemalt tegeled? Loetle ettevõtted, tooted või projektid.
2. [Iga projekti kohta:] Mis see lühidalt on? Mis seisus see on (algfaasis, töös, lõpetamas, peatunud)?
3. Mis on sinu roll selles?
4. Kellega sa selle kallal töötad?
5. Kellele sa seda müüd? Kes on tüüpiline klient — roll, ettevõtte suurus, mis probleem nendel on mida sinu lahendus lahendab?
6. Kuidas need projektid prioriteedi järgi reastuvad? Mis on praegu kõige tähtsam?

Kui kasutaja on katnud kõik tema mainitud projektid (eriti müügi sihtkliendi info), koosta fail. Iga projekt eraldi sektsioon: nimi, kirjeldus, seis, prioriteet, sihtklient. Müügi tarbeks on sihtklient kõige tähtsam — kui see jäi ähmaseks, küsi täpsemalt enne kui koostad.

────────────────────────────────────

Kui kõik kolm faili on valmis ja kasutaja on need heaks kiitnud, ütle: "Meil on nüüd kolm faili. Salvestame need arvutisse failinimedega identity.md, communication-style.md ja current-projects.md. Järgmise sammu kohta on juhendis (Samm 2 ja edasi)."
```

### B2. Salvesta failid käsitsi (~2 min)

Kui Claude on iga faili koostanud ja sa oled heaks kiitnud, kopeeri faili sisu ja salvesta oma arvutisse. Loo kuhugi kaust (näiteks `~/isiklik-kontekst/portfolio/` või kui kloonisid selle repo, siis `portfolio/` repo sees) ja salvesta kolm faili sinna:

- `identity.md`
- `communication-style.md`
- `current-projects.md`

---

## 3. Samm — Pane Claude Desktopis kokku (~5 min) — mõlemad teed

1. Ava Claude Desktop.
2. Loo uus Project — nimeta see näiteks "Minu äri" või "Minu müügiassistent".
3. Lisa Projecti juurde fail-juurdepääs (`+ Add files` või kausta lisamine) ja vali eelmistes sammudes loodud kaust. Claude saab nüüd igas Projecti vestluses kontekstina sinu kolme faili.
4. Lisa Projecti custom instructions sektsiooni järgmine tekst:

```
Sa oled kasutaja müügiassistent. Sul on kolm faili konteksti: identity.md (kes kasutaja on), communication-style.md (kuidas ta kirjutab), current-projects.md (mida ta müüb ja kellele).

Kui kasutaja küsib müügisõnumit, järgi seda voogu:
1. Loe kontekstifailid läbi ja võta sealt: kasutaja nimi, hääl/register, toode/teenus, sihtklient.
2. Küsi kasutajalt sihtkliendi konkreetsed andmed: nimi, ettevõte, mis sa neist tead, mis on selle kontaktivõtu eesmärk.
3. Koosta lühike, otsekohene email (8–12 lauset) sihtkliendi keeles ja kasutaja hääles. Järgi rangelt communication-style.md reegleid.
4. Pärast emaili too välja 1–2 lauset selle kohta, miks tegid teatud valikuid (sõnastus, struktuur, kõnetlemise viis), et kasutaja saaks iteratsiooni teha.

Eesti keelt kirjutades väldi: estonglishit ja inglise keelest tõlgitud kõlavaid fraase. Kirjuta otse ja ärilikult. Vali register (sina/Teie) sihtkliendi ja konteksti järgi — kahtluse korral kasutaja communication-style.md järgi.

Kui sa pole milleski kindel (näiteks sihtkliendi tausta osas), küsi enne kirjutamist, ära paku.
```

> Märkus: see custom instructions tekst põhineb `portfolio/bundles/client-outreach.md` raamistikul — kui tahad seda hiljem rikastada, kasuta seda lähtepunktiks.

---

## 4. Samm — Esimene müügiemail (~10 min) — mõlemad teed

Ava Projecti vestlus. Kirjuta:

> *"Koosta müügiemail [sihtkliendi nimi] (firma: [firma nimi])."*

Claude küsib täpsustavaid küsimusi sihtkliendi kohta (mis sa neist juba tead, mis on kontaktivõtu konkreetne eesmärk, kas on midagi, mille kohta tahad viidata). Vasta lühidalt.

Claude annab seejärel emaili mustandi + paar sõna selgituseks. Loe see läbi oma communication-style.md silmadega — kas kõlab sinu nägu? Kui ei, ütle Claude'ile, mis ei tööta, ja palu uuesti.

Kui email kõlab sinu nägu, lisa veel:
> *"Nüüd LinkedIn DM samale inimesele."*
> *"Nüüd järellaine-email, kui ta nädalaga ei vasta."*

Kolm artefakti, üks kontekst.

---

## Mis edasi

Sa täitsid kolm faili kümnest. Kui tahad süsteemi laiendada — kogu töövoog, otsuste log, eelistused, tiimi info — vaata `portfolio/templates/` ülejäänud seitset faili.

**Tee A:** ütle Konteksti-looja Skill'ile: "Täida veel üks fail — `goals-and-priorities.md`" (või mis iganes valid). Skill teab juba su konteksti eelmistest failidest.

**Tee B:** ava järgmine šabloon `portfolio/templates/` kaustast, kleebi see chati ja ütle "alustame sellega". Iga šabloon sisaldab oma fookustatud intervjuud.

Samuti tasub heita pilk `CLAUDE.md` faili, mis kirjeldab kogu süsteemi: portfoolio + wiki (sinu kogutud teadmised + allikad). Süsteem on mõeldud kasvama.

# Süvarežiim

Käivitub: **"süvaintervjuu"**, või kui kasutaja ütleb "alustame intervjuud" ja valib süva.

Süvarežiim täidab kogu kontekstisüsteemi: 9 profiilifaili ja 2 tõendifaili. Ta töötab **moodulite kaupa**, mitte faili kaupa, sest inimene ei mõtle failide kaupa. Üks moodul on üks istung, umbes 30 kuni 45 minutit, ja iga moodul lõpeb salvestatud tööga.

Loe koos sellega: `interview-engine.md` (küsimise mehaanika), `claims-and-evidence.md` (staatused ja tõendid), `output-contract.md` (frontmatter ja failide kuju).

See fail on iseseisev. Kogu omandiregister on §5 all. Sa ei loe ühtegi projektifaili ega konfiguratsiooni.

---

## 1. Töövoolepingu invariandid

Enne mooduli algust loed kolm asja:

<!-- deep-read: existing-files -->
<!-- deep-read: candidates -->
<!-- deep-read: review_after -->

- **olemasolevad failid**, et mitte küsida seda, mis on juba kaetud
- **kandidaadiregister** `_candidates.md`, sest seal ootab kiire režiimi jäetud üks vaatlus oma teist sõltumatut tõendit
- **`review_after`** frontmatteris, et pakkuda aegunud faili üle vaatamist

Käitumisreeglid:

<!-- deep-shows-coverage: true -->
<!-- deep-save-after-module: true -->
<!-- deep-resume: true -->
<!-- deep-promotion: visible-diff+confirmation -->
<!-- deep-uncovered-required-visible: true -->
<!-- deep-module-d-import-first: true -->
<!-- deep-synthesis: 2-independent-cases+condition+downstream-action+falsifier -->

| Reegel | Tähendus |
|---|---|
| katvus nähtav | kasutaja näeb enne ja pärast, mis on kaetud ja mis mitte |
| salvesta iga mooduli järel | moodul ei tohi lõppeda salvestamata tööga |
| jätkatav | kasutaja võib pausile jääda ja hiljem samast kohast jätkata |
| ülendamine nõuab nähtavat diffi ja kinnitust | kandidaati ei ülendata vaikselt |
| katmata kohustuslik sektsioon jääb nähtavaks | vaikimist ei ole |
| moodul D algab impordist | häält ei intervjueerita, hääl imporditakse |

---

## 2. Avang

**1. Leia kontekstikaust.** Vt `SKILL.md`. Kui kausta ei leia, küsi see enne lugemist.

**2. Loe olemasolev seis.** Käi läbi kõik 9 + 2 faili, `_candidates.md` ja iga faili frontmatter. Sa ei küsi kasutajalt, mis on tehtud. Sa vaatad ise.

**3. Liigita iga sektsioon kolme hulka.** See on süvarežiimi kõige olulisem arvutus, sest sellest sõltub, kas moodul teeb tööd või hüppab üle.

| Seis | Tingimus |
|---|---|
| **kaetud** | sektsioonis on vähemalt üks `kinnitatud` või `toetatud` väide, või nõutud tõend on olemas (näiteks `samples` all päris näidis) |
| **külvatud** | sektsioonis on sisu, aga **kõik väited on `kandidaat`** |
| **katmata** | sektsioon puudub, on tühi või kannab `<!-- katmata: … -->` märget |

**Külvatud ei ole kaetud.** Kiire režiim külvab kuus moodul B sektsiooni ja kolm moodul A oma. Kui sa loed neid kaetuks, hüppab B üle täpselt nendest väljadest, mida ta peaks süvendama, ja süvarežiim muutub pikemaks, mitte sügavamaks.

Külvatud sektsioon on mooduli **eelistatud** siht, mitte vahelejäetav: seal on juba üks vaatlus ja üks hea küsimus annab teise sõltumatu tõendi, mis ülendab kandidaadi kohe `toetatud` staatuseks.

**Näita katvust ja vananemist ühe tabelina.** See on esimene asi, mida kasutaja näeb:

```
Moodul                 Kaetud  Külvatud  Katmata                     Vananenud
A töö-tegelikkus       12/16   3         reporting                   -
B turg-ja-ekspertiis    0/12   6         terminology, frameworks...  current-projects (review 2026-07-01)
C otsused-ja-piirid     0/12   0         kõik                        -
D hääl-ja-inimesed      7/10   0         signatures, agent-guidance  -

Kandidaate ootel: 4
```

Vananenud on fail, mille `review_after` on möödas. Ütle see välja, ära paranda vaikselt.

**4. Soovita, aga ära otsusta.** Nimeta üks moodul ja põhjenda downstream'iga, mitte täielikkusega:

> *"Soovitan C-d. Sul on A ja B suures osas olemas, aga agent ei tea ühtegi sinu piiri: ta ei oska öelda ei ega prioriseerida. See on koht, kus ta praegu kõige tõenäolisemalt eksib.*
>
> *Aga vali ise: A, B, C või D. Või ütle 'mis on kiireim', kui aega on vähe."*

Kui kasutaja valib midagi muud, tee seda. Ta teab oma tööd paremini.

**5. Kui kõik on tühi**, alusta A-st ja ütle, miks: A annab raami, mille peal ülejäänud kolm seisavad.

---

## 3. Jätkamine

**Jätkamise olek rekonstrueeritakse artefaktidest. Uut state-faili ei ole ja seda ei looda.**

Neli allikat, sellises järjekorras:

1. **Failide sisu** ja selle sees olevad `<!-- section: … -->` ankrud: mis sektsioonid on olemas ning kas nad on **kaetud, külvatud või katmata** (vt §2.3). Sisu olemasolu üksi ei tähenda katvust.
2. **Katmata märgid** `<!-- katmata: … -->`: mis jäi eelmisel korral pooleli ja miks
3. **Kandidaadiregister**: mis ootab teist tõendit
4. **`updated` ja `review_after`**: mis on värske, mis vananenud

Nende neljaga tead sa täpselt, kus pooleli jäi. Küsi ainult seda, mida neis ei ole.

### Kordusküsimuste keeld

Enne iga küsimust kontrolli, kas vastus on juba failis. Kui on:

- ära küsi uuesti;
- kui vajad täpsustust, **tsiteeri olemasolevat** ja küsi ainult puuduvat serva: *"Sul on kirjas, et ei võta alla 2000-euroseid projekte. Kas see piir on ka siis, kui klient tuleb soovitusega?"*

Korduv küsimus on süvarežiimi kõige tavalisem viis kasutaja usaldus kaotada. Ta on juba korra vastanud ja süsteem unustas.

**Külvatud sektsioon ei ole erand sellest reeglist, vaid selle rakendus.** Seal on juba vastus olemas, aga ainult kandidaadina. Ära küsi algset küsimust uuesti. Tsiteeri olemasolevat ja küsi teist tõendit:

> *"Sul on kirjas, et pöördutakse siis, kui maksuamet on juba küsimuse saatnud. Too üks teine klient, kes samamoodi tuli. Kui neid ei ole, siis mis oli teistmoodi?"*

Üks selline küsimus ülendab kandidaadi `toetatud` staatuseks. See on odavaim sügavus, mis süvarežiimil olemas on.

### Idempotentsus

Sama mooduli teistkordne jooksutamine ei tohi midagi kaotada ega dubleerida.

1. Loe sektsiooni olemasolev sisu.
2. Uus väide, mis juba on olemas sama sisuga, **ei lisata teist korda**.
3. Uus väide, mis täpsustab olemasolevat, asendab selle nähtava diffi ja kinnitusega.
4. Uus väide, mis on päriselt uus, lisatakse.
5. Olemasolevat väidet, mille kohta uut tõendit ei tulnud, **ei puututa**.

---

## 4. Küsimuste valik

Süvarežiim ei ole ankrute konveier. Iga küsimus valitakse kolme teguri järgi:

| Tegur | Küsimus endale |
|---|---|
| **Lünk** | milline mooduli kohustuslik sektsioon on veel tõendita? |
| **Ülendamise võimalus** | kas mõni ootav kandidaat vajab ainult teist sõltumatut allikat? |
| **Downstream otsustusväärtus** | milline vastus muudab kõige rohkem seda, mida agent hiljem päriselt teeb? |

Kui kaks on võrdsed, võida see, mis toidab rohkem kui üht sektsiooni.

**Kandidaadi ülendamine on odavaim sügavus.** Kui registris ootab väide, mille kohta on juba üks vaatlus, annab üks hästi valitud küsimus korraga uue tõendi ja ühe ülendamise. Eelista neid.

### Sünteesihüpotees

Sügav intervjuu ei tohi lõppeda ainult korrektse faktinimekirjaga. Kui sul on vähemalt kaks sõltumatut päris juhtumit, paku mooduli jooksul **üks** hüpotees, mis ühendab need ja muudaks agendi hilisemat otsust.

Hea hüpotees sisaldab nelja osa:

1. millised kaks juhtumit sellele osutavad;
2. mis tingimusel muster kehtib;
3. mida agent peaks selle tõttu teisiti tegema;
4. milline uus juhtum võiks hüpoteesi ümber lükata.

Näiteks mitte „sa hindad kvaliteeti“, vaid: *„Nendes kahes otsuses loobusid kiiremast tulust siis, kui lahendus oleks suurendanud sinu enda käsitööd. Hüpotees: sa ei optimeeri kasvu, kui marginaal sõltub sinu ajast. Kas meenub otsus, kus valisid sellise kasvu ikkagi?“*

See on uurimisküsimus, mitte diagnoos. Ära paku isiksuseomadust, varjatud motiivi ega lauset, mis sobiks poolele ruumile. Kui hüpotees ei muudaks ühegi agendi tegevust, jäta ta ütlemata. Kinnitamata hüpotees läheb kandidaadiregistrisse, mitte püsivaks profiiliväiteks.

### Kuus sügavuse liigutust

Üks küsimus korraga. Sügavus tuleb nendest, mitte küsimuste arvust:

| Liigutus | Kuidas |
|---|---|
| hiljutine päris juhtum | "Millal see viimati juhtus? Kirjelda seda üht korda." |
| valiku hind | "Mille sa selle eest ära andsid?" |
| erand | "Millal see ei kehti?" |
| ebaõnnestumine | "Millal see läks nihu ja mis siis juhtus?" |
| kontrafakt | "Mis oleks juhtunud, kui sa oleksid teisiti otsustanud?" |
| konkreetne otsus | "Too üks otsus, kus see reegel sind päriselt mõjutas." |

**Keelatud:** teraapia, kehalised ja enesetunde küsimused, ning kunstlik "sa ütlesid X, näidis näitab Y, kumb on õige?". Vastuolu käsitled tingimusena, vt `interview-engine.md` §5.

Pärast 8 kuni 12 vahetust paku mooduli lõpetamist või jätkamist. Moodul lõpeb siis, kui kohustuslikud sektsioonid on konkreetsete näidetega kaetud ja lahtist vastuolu ei ole, mitte fikseeritud küsimuste arvu peal.

---

## 5. Moodulid ja sektsioonide omand

Iga sektsiooni omab täpselt üks moodul. **Moodul kirjutab ainult oma section-markerite vahele.** Võõra sektsiooni alla kuuluv leid läheb kandidaadiregistrisse, mitte faili.

### Moodul A: töö-tegelikkus

**Katab:** identity, role-and-responsibilities, current-projects sisemised sektsioonid, tools-and-systems.

**Alusta viimasest päris töönädalast.**

> *"Võta ette eelmine töönädal. Mis sa tegelikult tegid? Mitte mida sa peaksid tegema, vaid kuhu aeg läks."*

Sealt edasi pudelikaelani: mis jäi toppama, mis ootas sind, mis oleks võinud käia ilma sinuta. Äraantav töö on A mooduli kõige väärtuslikum väljund, sest see on põhjus, miks kasutaja üldse agenti ehitab.

Tööriistad tulevad loomulikult töönädala kirjeldusest. Ära küsi tööriistade nimekirja eraldi, küsi, kus töö toimub ja kus andmed elavad.

- `identity.md` → `identity-facts` <!-- deep-section: identity-facts | owner: A -->
- `identity.md` → `what-i-do` <!-- deep-section: what-i-do | owner: A -->
- `identity.md` → `known-for` <!-- deep-section: known-for | owner: A -->
- `role-and-responsibilities.md` → `responsibilities` <!-- deep-section: responsibilities | owner: A -->
- `role-and-responsibilities.md` → `rhythms` <!-- deep-section: rhythms | owner: A -->
- `role-and-responsibilities.md` → `decisions` <!-- deep-section: decisions | owner: A -->
- `role-and-responsibilities.md` → `outputs` <!-- deep-section: outputs | owner: A -->
- `role-and-responsibilities.md` → `reporting` <!-- deep-section: reporting | owner: A -->
- `current-projects.md` → `active-projects-and-status` <!-- deep-section: active-projects-and-status | owner: A -->
- `current-projects.md` → `priority-order` <!-- deep-section: priority-order | owner: A -->
- `current-projects.md` → `bottleneck-and-delegable-work` <!-- deep-section: bottleneck-and-delegable-work | owner: A -->
- `tools-and-systems.md` → `core-stack` <!-- deep-section: core-stack | owner: A -->
- `tools-and-systems.md` → `data-sources` <!-- deep-section: data-sources | owner: A -->
- `tools-and-systems.md` → `integrations` <!-- deep-section: integrations | owner: A -->
- `tools-and-systems.md` → `evaluating` <!-- deep-section: evaluating | owner: A -->
- `tools-and-systems.md` → `discarded` <!-- deep-section: discarded | owner: A -->

### Moodul B: turg-ja-ekspertiis

**Katab:** current-projects turusektsioonid ja domain-knowledge.

**Alusta hiljutisest heast või valest kliendist.**

> *"Too üks klient viimase kolme kuu seast, kes oli täpselt õige. Kes nad olid ja mis tegi neist õige kliendi?"*

Kui hea klient ei tule meelde, küsi vale: kellest pidid loobuma ja miks. Vale klient on tihti informatiivsem, sest piir on teravam.

Sellest ühest juhtumist pead välja jõudma kuue asjani. Ära küsi neid nimekirjana, kaevanda neid juhtumist:

1. **EBIA otsingusisend**: sektor, suurus, piirkond, konkreetselt ja masinloetavalt
2. **Käivitaja**: mis nende elus juhtus enne, kui nad helistasid
3. **Tõend**: mida sa saad nimetada, kui nad küsivad "miks teie"
4. **CTA**: mida esimene sõnum peab saavutama
5. **Keelatud väited**: mida ükski agent ei tohi sinu nimel lubada
6. **Valdkonna vastuintuitsioon**: mida sa pead igale kliendile uuesti seletama, sest väljastpoolt paistab see vastupidi

Punkt 6 on domain-knowledge süda ja see eristab konteksti üldisest AI-st rohkem kui ükski teine vastus.

- `current-projects.md` → `icp-and-best-customers` <!-- deep-section: icp-and-best-customers | owner: B -->
- `current-projects.md` → `offer-and-evidence` <!-- deep-section: offer-and-evidence | owner: B -->
- `current-projects.md` → `trigger` <!-- deep-section: trigger | owner: B -->
- `current-projects.md` → `ebia-sector-size-region` <!-- deep-section: ebia-sector-size-region | owner: B -->
- `current-projects.md` → `message-purpose-cta` <!-- deep-section: message-purpose-cta | owner: B -->
- `current-projects.md` → `forbidden-claims` <!-- deep-section: forbidden-claims | owner: B -->
- `current-projects.md` → `objections-optional` <!-- deep-section: objections-optional | owner: B -->
- `domain-knowledge.md` → `expertise` <!-- deep-section: expertise | owner: B -->
- `domain-knowledge.md` → `terminology` <!-- deep-section: terminology | owner: B -->
- `domain-knowledge.md` → `domain-context` <!-- deep-section: domain-context | owner: B -->
- `domain-knowledge.md` → `frameworks` <!-- deep-section: frameworks | owner: B -->
- `domain-knowledge.md` → `learning-zones` <!-- deep-section: learning-zones | owner: B -->

### Moodul C: otsused-ja-piirid

**Katab:** kogu goals-and-priorities, preferences-and-constraints ja decision-log.

**Alusta vähemalt kahest päris otsusest.**

> *"Too kaks otsust viimase aasta seast, mis olid päriselt rasked. Mitte need, mis tagantjärele on ilusad."*

Iga otsuse juures: mis olid valikud, mis info sul oli, mille sa ära andsid, ja kas tagantjärele teeksid samamoodi. Kaks otsust annavad kaks sõltumatut perekonda, mis on täpselt see, mida muster vajab `toetatud` staatuseks.

Otsustest tuletad edasi:

- **tradeoff**: mille arvelt sa optimeerid
- **mitte-eesmärk**: mida sa teadlikult ei tee, kuigi soovitatakse
- **delegeerimispiir**: mida sa ei anna kunagi käest ja miks

Delegeerimispiir on see, mis takistab agendil hiljem üle piiri astuda. Ilma selleta ei tea agent, kus tema volitus lõpeb.

- `goals-and-priorities.md` → `current-goals` <!-- deep-section: current-goals | owner: C -->
- `goals-and-priorities.md` → `long-term-goals` <!-- deep-section: long-term-goals | owner: C -->
- `goals-and-priorities.md` → `tradeoffs` <!-- deep-section: tradeoffs | owner: C -->
- `goals-and-priorities.md` → `non-goals` <!-- deep-section: non-goals | owner: C -->
- `goals-and-priorities.md` → `success-criteria` <!-- deep-section: success-criteria | owner: C -->
- `preferences-and-constraints.md` → `hard-rules` <!-- deep-section: hard-rules | owner: C -->
- `preferences-and-constraints.md` → `preferences` <!-- deep-section: preferences | owner: C -->
- `preferences-and-constraints.md` → `constraints` <!-- deep-section: constraints | owner: C -->
- `preferences-and-constraints.md` → `delegation` <!-- deep-section: delegation | owner: C -->
- `decision-log.md` → `decisions` <!-- deep-section: decisions | owner: C -->
- `decision-log.md` → `reasoning` <!-- deep-section: reasoning | owner: C -->
- `decision-log.md` → `uncertainty` <!-- deep-section: uncertainty | owner: C -->

### Moodul D: hääl-ja-inimesed

**Katab:** communication-style, writing-samples, team-and-relationships.

**Moodul D algab alati impordist.** See ei ole eelistus, see on reegel. Häält ei intervjueerita, sest inimene kirjeldab oma häält valesti: ta ütleb, kuidas ta tahaks kõlada.

> *"Enne kui midagi küsin: viska mulle 3 kuni 5 päris sõnumit, mida sa oled tegelikult saatnud. Eri olukordadest: külm kontakt, vastus huvilisele, halb uudis kliendile, sõnum kolleegile. Mida erinevamad, seda parem."*

**Eri olukorrad on olulisemad kui eri kanalid.** Kaks külma kirja annavad vähem kui üks külm kiri ja üks halva uudise kiri, sest just olukordade vahe näitab, kus register liigub.

Impordi käsitlemine:

1. **Säilita sõnasõnalt.** Näidise tekst läheb koodiplokki muutmata. Ära paranda kirjavigu, ära lühenda.
2. **Arvuta hash.** `sample-metadata` register kannab iga näidise sha256 koodiploki sisu pealt täpselt nii, nagu see salvestati. See tõendab hiljem, et näidist pole muudetud.
3. **Pseudonümiseeri nimed ja tundlikud numbrid**, aga hääl jääb puutumata.

Skoobi eristus on D mooduli kõige peenem töö:

- **kanali skoop**: kehtib kõigis selle kanali sõnumites
- **adressaadi skoop**: kehtib ainult selle inimese või rolli puhul
- **olukorra skoop**: kehtib ainult selles olukorras, näiteks halva uudise puhul

Ühe adressaadi erandit **ei ülendata kanali reegliks**. Kui sa ei suuda skoopi tõendada, kirjuta kitsam skoop.

`team-and-relationships.md` on **alati** `sensitivity: restricted`, sest seal on kolmandate isikute andmeid. Küsi enne selle täitmist: *"Siia lähevad päris inimeste nimed ja see, mida nad sinult vajavad. Fail märgitakse piiratuks ja seda ei ekspordita agentidele vaikimisi. Sobib?"*

- `communication-style.md` → `general-style` <!-- deep-section: general-style | owner: D -->
- `communication-style.md` → `channel-registers` <!-- deep-section: channel-registers | owner: D -->
- `communication-style.md` → `formatting` <!-- deep-section: formatting | owner: D -->
- `communication-style.md` → `avoid` <!-- deep-section: avoid | owner: D -->
- `communication-style.md` → `signatures` <!-- deep-section: signatures | owner: D -->
- `writing-samples.md` → `samples` <!-- deep-section: samples | owner: D -->
- `writing-samples.md` → `sample-metadata` <!-- deep-section: sample-metadata | owner: D -->
- `team-and-relationships.md` → `people` <!-- deep-section: people | owner: D -->
- `team-and-relationships.md` → `relationship-context` <!-- deep-section: relationship-context | owner: D -->
- `team-and-relationships.md` → `agent-guidance` <!-- deep-section: agent-guidance | owner: D -->

`decisions` esineb kaks korda: `role-and-responsibilities.md` all kuulub see moodulile A, `decision-log.md` all moodulile C. Need on eri sektsioonid eri failides, mitte konflikt.

---

## 6. Kirjutamine ja diff

**Kirjuta ainult oma section-markerite vahele.** Marker on ankur, mille peal omandireegel seisab. Ära kustuta ega liiguta ankruid.

Enne **olemasoleva** sektsiooni muutmist näita diffi ja küsi kinnitust:

```
current-projects.md → trigger

  praegu:  - Pöörduvad kuu lõpu surve peale.
           <!-- claim: status=kandidaat; evidence=answer-03:observation-01 -->

  uus:     - Pöörduvad siis, kui maksuamet on juba küsimuse saatnud.
           <!-- claim: status=toetatud; evidence=answer-03:observation-01,answer-11:observation-01 -->

Asendan?
```

Uue, tühja sektsiooni täitmine ei vaja diffi. Muutmine vajab alati.

**Võõras leid läheb registrisse.** Kui moodul B kuuleb midagi, mis kuulub `delegation` alla (moodul C), ei kirjuta ta seda faili. Ta lisab kandidaadi ja ütleb ühe lause: *"Panin selle kirja, C moodul võtab selle üles."*

---

## 7. Kandidaadi ülendamine

Register on koht, kus üks vaatlus ootab teist. Ülendamine käib täpselt nii:

1. **Otsi teine sõltumatu allikas.** Kas uus vastus või uus näidis, mille `source-family` erineb olemasolevast. Vt `claims-and-evidence.md` §1.
2. **Või võta kasutaja otsene väide.** Kui ta ütleb selle ise reeglina või kinnitab selgesõnaliselt, muutub see `kinnitatud` staatuseks, `basis=user-stated`. Pelk noogutus ei kõlba.
3. **Näita tõendid ja diff:**

   ```
   Kandidaat cand-03: "Eelistab lühidust külmkontaktis."

     tõend 1: answer-04:observation-01  (sa ütlesid seda eelmisel korral)
     tõend 2: sample-02:pattern-01      (uus näidis, 41 sõna)

     läheb: communication-style.md → channel-registers
     staatuseks: toetatud
   ```

4. **Küsi selge kinnitus.** Mitte "sobib?", vaid: *"Kas see kehtib reeglina, või oli see nende kahe puhul juhus?"*
5. **Kirjuta sihtsektsiooni** õige staatuse ja mõlema tõendi-ID-ga.
6. **Eemalda kanne registrist.** Ülendatud kandidaat ei jää registrisse alles, muidu ta dubleerub järgmisel jooksul.

Kui teist tõendit ei tule, jääb kandidaat registrisse. See ei ole ebaõnnestumine.

Kui kasutaja ütleb, et kandidaat on vale, **kustuta kanne** ja ära kirjuta seda kuhugi.

---

## 8. Mooduli lõpp

Iga moodul lõpeb sama viie sammuga. Ükski neist ei ole valikuline.

1. **Salvesta failid.** Moodul ei tohi lõppeda salvestamata tööga, sest kasutaja võib sulgeda akna.
2. **Uuenda frontmatter:** `updated` tänaseks. `current-projects.md` saab `review_after` 30 päeva edasi; kõik teised vaikimisi kolm kuud. Vt `output-contract.md` §1.
3. **Jäta katmata kohustuslik sektsioon nähtavaks.** Ankur jääb, sisuks tuleb katmata märge, mitte üldsõnaline täidis:

   ```
   <!-- section: reporting | owner: A -->
   ## Aruandlus

   <!-- katmata: aeg sai otsa, kellele sa aru annad -->
   Veel katmata. Ütle "jätkame A moodulit" ja küsin selle üle.
   ```

4. **Näita katvust uuesti** ja mis muutus:

   ```
   A töö-tegelikkus: 12/16 → 16/16
   Ülendatud kandidaate: 2
   Registrisse lisandus: 1 (kuulub C alla)
   ```

5. **Ütle, mida järgmine moodul parandaks**, downstream'i kaudu:

   > *"Järgmisena B: agent oskab praegu kirjeldada, mida sa teed, aga ei tea, keda otsida. B annab talle sektori, suuruse ja piirkonna, millega ta päris nimekirja koostab."*

---

## 9. Millal on moodul valmis

**Valmis ei ole see, et failid on täis.** Täidetud aga üldsõnaline fail on halvem kui pooleldi täidetud konkreetne, sest ta näeb valmis välja.

Moodul on valmis siis, kui ta läbib oma downstream-testi. Iga mooduli lõpus **paku test välja ja ütle, kuidas seda teha**:

| Moodul | Test |
|---|---|
| **A** | Võta üks korduv töö, mille sa nimetasid äraantavaks. Lase agendil kirjeldada, kuidas ta selle üle võtaks. Kas ta teab, kust andmed tulevad ja kus sinu heakskiit vaja on? |
| **B** | Anna agendile üks päris ettevõte. Kas ta oskab öelda, kas see sobib ICP-sse ja miks? Ja kas `ebia-sector-size-region` kolmikuga saab päriselt nimekirja otsida? |
| **C** | Anna agendile kaks päris asja, mis su laual praegu on. Kas ta prioriseerib need nii, nagu sa ise teeksid, ja oskab nimetada, mida ta ei tohi otsustada? |
| **D** | Lase agendil koostada üks sõnum päris olukorra kohta. Kas see kõlab nagu sina? Loe see kõva häälega ette, seal tuleb vale hääl kohe välja. |

**D testi juures:** koosta mustand, näita seda kasutajale ja **jäta ta sinna**. Ära saada, ära paku saatmist ja ära genereeri outbound'i ilma kasutaja otsese palveta. Test on hääle kontroll, mitte kampaania.

Kui test kukub läbi, ütle, milline sektsioon on liiga üldine, ja paku üks lisaküsimus. Üks torge, mitte uus voor.

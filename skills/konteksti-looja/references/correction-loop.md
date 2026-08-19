# Paranduste õppimisloop

Käivitub: **„õpime parandusest“**, **„siin on lõplik versioon“** või siis, kui sama vestluse kasutaja ütleb, et ta saatis, avaldas või kasutas sinu mustandi ära ja tahab parandustest õppida.

Loop muudab päris kasutuse kontekstiks. Ta ei eelda Gmaili ega muud ühendust ja ei loe midagi, millele kasutaja pole ligipääsu andnud.

<!-- correction-same-conversation-one-paste: true -->
<!-- correction-automatic-promotion: false -->
<!-- correction-visible-diff-and-confirmation: true -->
<!-- correction-one-event-one-source-family: true -->

---

## 1. Küsi minimaalne sisend

**Samas vestluses:** sul on enda koostatud mustand juba olemas. Kasutaja kleebib ainult lõpliku teksti.

> *„Saatsid või avaldasid ära? Kleebi lõplik versioon, vaatan ainult seda, mida muutsid.“*

**Uues vestluses:** sul ei ole algset mustandit. Küsi üks kleepimine kahe märgisega:

```text
ALGNE MUSTAND
...

LÕPLIK VERSIOON
...
```

Ära väida, et näed Gmaili, CRM-i või avaldatud postitust. Kui kasutaja ei kleebi lõppteksti, pole sul diffi ja loop peatub.

---

## 2. Hoia lõpptekst puutumata

Lõplik versioon on kasutaja artefakt, mitte sinu ümberkirjutamise sisend.

1. Ära paranda seal kirjavigu ega vormingut.
2. Pseudonümiseeri nimi või tundlik number ainult kasutaja nõusolekul.
3. Kui kasutaja tahab lõppteksti `writing-samples.md` faili lisada, salvesta see sõnasõnalt fence'i sisse ja arvuta sha256 täpselt salvestatud baitidest.
4. Ära lisa tervet lõppteksti automaatselt. Küsi enne, kas see on päriselt saadetud või avaldamiseks kinnitatud ja kas selle tundlikkus lubab talletamist.

---

## 3. Klassifitseeri muutused

Ära tee igast redaktsioonist stiilireeglit. Jaga sisulised muutused viide klassi:

| Klass | Millal | Tüüpiline siht |
|---|---|---|
| `fact-correction` | kasutaja parandas pakkumist, numbrit, rolli või muud fakti | vastav profiilifail; küsi, kas fakt on püsiv |
| `general-style` | parandus kehtib kasutaja sõnul tema kirjutamisele üldiselt | `communication-style.md` → `general-style`, `formatting` või `avoid` |
| `channel-style` | parandus kehtib ühes kanalis | `communication-style.md` → `channel-registers` |
| `addressee-exception` | parandus tulenes ühest inimesest või rollist | pseudonüümitud kandidaat; vajadusel `team-and-relationships.md`, alati `restricted` |
| `temporary-project-context` | parandus kehtib praeguse kampaania, pakkumise või projekti ajal | `current-projects.md`, kitsa skoobi ja aegumisega |

Kui põhjus pole diffist selge, küsi üks küsimus: *„Kas muutsid seda oma üldise stiili pärast või ainult selle adressaadi jaoks?“* Ära arva.

Kirjaviga, juhuslik sõnavahetus ja fakt, mida kasutaja muutis ainult selle ühe sõnumi jaoks, ei ole automaatselt püsikontekst.

---

## 4. Üks sündmus on üks allikaperekond

Anna kogu diffisündmusele üks ID, näiteks `correction-20260819-01`. Selle sees võivad olla `phrase-01`, `fact-01` ja `structure-01`, aga nad ei ole sõltumatud allikad.

Kolm muudatust samas kirjas ei tee väidet `toetatud` staatuseks. Teine sõltumatu parandussündmus võib seda teha. Kasuta `claims-and-evidence.md` staatuse- ja ID-reegleid.

Kui sama lõpptekst lisatakse `writing-samples.md` faili ja saab `sample-NN` ID, **ära loe `sample-NN`-i ning selle diffi kaheks allikaks**. Vali selle sündmuse jaoks üks kanooniline perekond — talletatud näidise puhul `sample-NN` — ja pane diffivaatlused sama prefiksi alla. Üks kiri jääb üheks allikaks ka siis, kui vaatad teda kahest kohast.

---

## 5. Näita enne kirjutamist

Näita ainult tähenduslikke erinevusi, mitte tervet tehnilist diffi:

| Muutus | Klass | Pakutud järeldus | Skoop | Siht |
|---|---|---|---|---|
| „Pakume automatiseerimist“ → „ehitame müügiagendi“ | `fact-correction` | pakkumine on müügiagent, mitte üldine automatiseerimine | praegune pakkumine | `current-projects.md` |
| kolm lõiku → üks | `channel-style` | külmkontaktis hoiab teksti ühe lühikese plokina | külm email | `communication-style.md` |

Seejärel näita täpne failidiff ja küsi üks selge kinnitus:

> *„Kas kirjutan need kaks muudatust konteksti? Esimese kinnitatud faktina, teise ühe sündmuse põhjal kandidaadina.“*

Ilma selle kinnituseta ei kirjuta midagi.

---

## 6. Kirjutamise reeglid

1. **Automaatset ülendamist ei ole.** Üks parandussündmus toodab tuletatud reegli jaoks `kandidaat` staatuse, mitte `toetatud` reegli.
2. **Kasutaja selgesõnaline üldreegel võib olla `kinnitatud`.** Näiteks „jah, ma teen külmades kirjades alati nii“ on `basis=user-stated`. „Sobib“ ei ole piisav.
3. **Faktiparandus vajab ulatust.** Küsi, kas see asendab püsiva fakti või kehtis ainult selles sõnumis.
4. **Ajutine kontekst aegub.** Pane kirja skoop ja `expires`; vaikimisi 30 päeva, kui kasutaja ei anna muud tähtaega.
5. **Adressaadi erand ei muutu kanalireegliks.** Nimed pseudonümiseeri kandidaadiregistris. Nimeline sisu läheb ainult kasutaja kinnitusega `team-and-relationships.md` faili, mis on `restricted`.
6. **Lõpptekst on tõend, mitte automaatselt reegel.** Kui kasutaja lubab selle näidiseks lisada, võib ta toetada tulevikus mustrit. Tema olemasolu üksi ei tõesta, miks iga muudatus tehti.
7. **Olemasoleva faili muutmisel näita diffi.** Järgi `output-contract.md` salvestamisreegleid.

Kui faile ei saa kirjutada, tagasta kinnitatud muudatused eraldi koodiplokkidena koos täpse sihtfaili ja sektsiooniga. Ära ütle, et salvestasid.

---

## 7. Lõpp

Ütle kolmes reas:

1. mis failides päriselt muutus;
2. mis jäi kandidaadiks ja millist teist sõltumatut sündmust ta ootab;
3. kas lõplik tekst lisati sõnasõnalise näidisena või jäeti privaatsuse tõttu lisamata.

Ära küsi kohe uut parandust. Loop peab võtma vähem aega kui teksti uuesti käsitsi seletamine.

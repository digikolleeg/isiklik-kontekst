# Väljundleping

Mida faili kirjutatakse ja mis kujul. Kehtib mõlemas režiimis.

---

## 1. Frontmatter

Iga kontekstifail algab selle blokiga. Kõik kolm välja on kohustuslikud.

```yaml
---
updated: 2026-08-19
review_after: 2026-11-19
sensitivity: exportable
---
```

| Väli | Reegel |
|---|---|
| `updated` | tänane kuupäev, `YYYY-MM-DD` |
| `review_after` | kuupäev, `YYYY-MM-DD`, ei tohi olla varasem kui `updated`. `current-projects.md`: 30 päeva; kõik teised: vaikimisi kolm kuud. |
| `sensitivity` | täpselt `exportable` või `restricted`. Muid väärtusi ei ole. |

`sensitivity` valik:

- `exportable` on vaikeväärtus.
- `restricted`, kui failis on kolmandate isikute isikuandmeid, kliendi siseinfot, hindu või lepingutingimusi, mida kasutaja ei tahtnud üldistada.
- `team-and-relationships.md` on **alati** `restricted`.

Kiire režiimi neli väljundfaili on tavaliselt `exportable`. Kui kasutaja jättis näidistesse päris kliendinimed alles, muutub `writing-samples.md` `restricted` failiks.

---

## 2. Väited

Vt `claims-and-evidence.md` §3. Lühidalt: puhas bullet, HTML kommentaar lause lõpus.

```
- Ei kasuta hüüumärke. <!-- claim: status=kinnitatud; basis=user-stated -->
- Alustab otse. <!-- claim: status=toetatud; evidence=sample-01:pattern-01,sample-02:pattern-01 -->
- Eelistab lühidust. <!-- claim: status=kandidaat; evidence=answer-04:observation-01 -->
```

Nähtavat staatusprefiksit ei kasutata. `kinnitatud` kannab `basis=user-stated`, ülejäänud kannavad `evidence=`.

---

## 3. Katmata väli

Katmata väli jääb faili **nähtavaks**. Seda ei täideta üldsõnalise lausega ja seda ei jäeta vaikselt välja.

```
## Usaldusväärsuse tõend

<!-- katmata: eelarve sai täis enne selle välja katmist -->
Veel katmata. Ütle "täiendame current-projects.md" ja küsin selle üle.
```

Kaks reeglit:

1. Nähtav rida kasutajale, mis ütleb, mis puudu on ja kuidas seda täita.
2. HTML kommentaar masinale.

Katmata väli ei ole viga. Üldsõnaline täidis on viga.

---

## 4. Neli kiire režiimi faili

### Sektsiooniankrud

Kiire režiim **külvab** sektsioone, mis kuuluvad süvamoodulite omandisse. Kasuta täpselt lepingujärgseid sektsiooni-ID-sid ja pealkirju, mitte paralleelset lihtsustatud skeemi.

Ankur on **ankur ise, siis pealkiri**, ja ta kannab alati omanikku:

```
<!-- section: offer-and-evidence | owner: B -->
## Pakkumine ja tõendid
```

Külvamine ei anna kiirele režiimile omandit. Kiire režiim kirjutab need sektsioonid esimest korda; **hilisemad muudatused teeb sektsiooni omanik**, vt [deep-mode.md](deep-mode.md) §5. Ankrut ei tohi kustutada, sest omandireegel seisab selle peal.

### identity.md

Kes kasutaja on, mida ettevõte teeb, mille pärast tema poole pöördutakse. Tööalane, mitte isiksuseportree.

| Ankur | Pealkiri |
|---|---|
| `<!-- section: identity-facts \| owner: A -->` | `## Põhifaktid` |
| `<!-- section: what-i-do \| owner: A -->` | `## Mida ma teen` |
| `<!-- section: known-for \| owner: A -->` | `## Mille poolest olen tuntud` |

`identity-facts` kannab nime, rolli ja ettevõtet. See ei tohi jääda tühjaks, ka kiires režiimis mitte.

### current-projects.md

| Ankur | Pealkiri | Katvusvõti |
|---|---|---|
| `<!-- section: icp-and-best-customers \| owner: B -->` | `## ICP ja parimad kliendid` | `offer_buyer`, osaliselt |
| `<!-- section: offer-and-evidence \| owner: B -->` | `## Pakkumine ja tõendid` | `offer_buyer`, `credibility_evidence` |
| `<!-- section: trigger \| owner: B -->` | `## Käivitaja` | `problem_trigger` |
| `<!-- section: ebia-sector-size-region \| owner: B -->` | `## Otsingusisend` | `icp_sector_size_region` |
| `<!-- section: message-purpose-cta \| owner: B -->` | `## Sõnumi eesmärk ja CTA` | `message_purpose_cta` |
| `<!-- section: forbidden-claims \| owner: B -->` | `## Mida ei tohi väita` | `forbidden_claims` |

`ebia-sector-size-region` peab sisaldama struktureeritud kolmikut, sest sellest saab EBIA otsingusisend:

```
sektor: <tegevusala>
suurus: <töötajate arv või käive>
piirkond: <geograafia>
```

Need kolm rida on masinloetavad. Proosakirjeldus käib nende alla eraldi.

`forbidden-claims` on writeri kõige olulisem piire. Kui kasutaja ei nimetanud ühtegi keeldu, ära jäta sektsiooni tühjaks: märgi katmata välja vormis (§3).

### communication-style.md

| Ankur | Pealkiri | Katvusvõti |
|---|---|---|
| `<!-- section: channel-registers \| owner: D -->` | `## Kanali järgi` | `channel_register_length` |
| `<!-- section: avoid \| owner: D -->` | `## Mida ma väldin` | `forbidden_mannerisms` |

`channel-registers` märgib iga kanali eraldi: mis kanal, sina või Teie, milline toon ja **pikkusepiir**. Pikkus ei ole eraldi sektsioon, see käib kanali juurde, sest piir on kanalipõhine. Kui hääl on kanalite üleselt ühtlane, kirjuta see välja, see on samuti info.

`avoid` on sõnad, fraasid ja võtted, mida kasutaja oma nime all ei taha näha.

### writing-samples.md

Vähemalt kaks sõnasõnalist näidist. Näidise tekst kuulub sektsiooni `samples`, register sektsiooni `sample-metadata`.

| Ankur | Pealkiri |
|---|---|
| `<!-- section: samples \| owner: D -->` | `## Näited` |
| `<!-- section: sample-metadata \| owner: D -->` | `## Näidete register` |

**Näidise tekst käib alati fence'i sisse.** See on ainus koht, kus paljas `- ` bullet on lubatud, ja fence on täpselt see, mis ta lubatuks teeb: fence'i sees olevat rida ei loeta väiteks. Ilma fence'ita kukub päris kiri, milles on bulletloend, vorminguraua taha.

````
<!-- section: samples | owner: D -->
## Näited

### sample-01
kanal: email
kontekst: külm esimene kontakt
allikas: kasutaja enda saadetud kiri

```
<näidise täistekst, sõnasõnalt, koos kõigi bullettidega>
```
````

#### Redaktsioon enne talletamist, siis bait-täpsus

Need kaks reeglit ei ole vastuolus, sest nad käivad **eri hetkede** kohta. Järjekord on alati sama:

1. **Redaktsioon.** Enne salvestamist pseudonümiseeri nimed ja tundlikud numbrid. See on **kasutajaga kokku lepitud** samm: näita, mida asendad, ja lase kinnitada. Asenda ainult nimi või number, ära kirjuta lauset ümber, ära silu.
2. **Talletamine.** Kokkulepitud tekst läheb fence'i sisse.
3. **Bait-täpsus kehtib sellest hetkest.** Salvestatud tekst on kanooniline. Pärast seda ei paranda sa kirjavigu, ei muuda reavahetusi, ei lisa ega eemalda tühja rida.
4. **Hash käib salvestatud teksti üle.** `sample-metadata` sha256 arvutatakse fence'i sisust pärast redaktsiooni, mitte originaalist. Originaali hashi kuhugi ei kirjutata.

Nii tähendab "sõnasõnalt" seda, et sa ei paranda kasutaja keelt, ja "bait-täpne" seda, et talletatud tõend ei muutu enam kunagi vaikselt.

`sample-metadata` on tabel: allikas, kanal, kuupäev, pikkus sõnades, sha256. `sample-NN` ID on ühtlasi tõendi source-family, sama ID kasutad väidete `evidence=` väljal.

**AI koostatud tekst ei lähe siia.** Kasutaja parandatud versioon läheb, kui ta selle parandas ja kinnitas.

---

## 5. Faili loomine ja muutmine

Kontrolli enne kirjutamist, kas fail on olemas. Edasi on kaks eri teed.

### Fail puudub: loo õige ankruskelett

Režiimid teavad eri palju ja loovad skeleti erinevalt:

- **Kiire režiim:** loo neli väljundfaili §4 tabelites loetletud ankrutega. Need tabelid on null-installi failis täielikult kaasas; süvarežiimi omandiregistrit pole vaja avada.
- **Süvarežiim:** loo kõik selle faili sektsioonid omandiregistri järgi, vt [deep-mode.md](deep-mode.md) §5. Nii leiab järgmine moodul ka oma ankru eest.

1. Frontmatter (§1).
2. Iga valitud skeleti sektsioon õiges järjekorras: ankur koos omanikuga, siis pealkiri.
3. Sinu enda sektsioonid täidad sisuga.
4. Süvarežiimi täisskeletis jäävad **võõrad sektsioonid nähtavalt katmata** (§3), koos märkega, milline moodul need täidab.

```
<!-- section: responsibilities | owner: A -->
## Vastutused

<!-- katmata: kuulub moodulile A -->
Veel katmata. Ütle "süvaintervjuu" ja vali moodul A.
```

Põhjus: skelett teeb faili kohe jätkatavaks. Järgmine moodul leiab oma ankru eest ja kirjutab õigesse kohta, selle asemel et arvata, kuhu sektsioon käib.

### Fail on olemas: ära kirjuta vaikimisi üle

1. Kui sinu omatud sektsiooni ankur puudub, lisa täpne ankur ja pealkiri omandiregistri järjekorda. Kiire režiimi skelett on teadlikult lühem, seega see on tavaline süvarežiimi jätk, mitte viga.
2. Tühja või katmata märkega sektsiooni tohid täita.
3. Sisuga sektsiooni **muudad ainult siis, kui oled selle omanik**, ja siis näitad enne diffi, vt `deep-mode.md` §6.
4. Kui sa ei ole omanik, läheb leid kandidaadiregistrisse, mitte faili.
5. Olemasolevat ankrut ei kustuta ega liiguta kunagi.

Pärast kirjutamist ütle, kuhu salvestasid.

Kui kausta ei saa kirjutada, väljasta failid ükshaaval selles järjekorras ja pane iga faili ette täpne silt:

1. `FAILINIMI: identity.md`
2. `FAILINIMI: current-projects.md`
3. `FAILINIMI: communication-style.md`
4. `FAILINIMI: writing-samples.md`

Näita kogu faili sisu sildi järel ühes koodiplokis. Kasuta välimise ploki jaoks nelja tagasirõhuga piiret, sest `writing-samples.md` sisaldab ise kolme tagasirõhuga näidiseplokke. Nii ei poolita vestlusliides faili kaheks artefaktiks. Kui liides annab allalaadimisel automaatse nime, ütle kasutajale kohe, millise ülaltoodud nime ta peab failile panema.

---

## 6. Enne mustandi näitamist

Kontrolli neli asja ja paranda enne näitamist:

1. Iga bullet, mis on väide, kannab kommentaari õiges vormingus.
2. Frontmatteris on kõik kolm välja ja `review_after` ei ole varasem kui `updated`.
3. Kõik konkreetsed asjad, mille kasutaja nimetas, on failis olemas.
4. Sessioonile ei viidata. Fail peab toimima ka kuue kuu pärast.

Seejärel näita mustandid ühe sõnumiga ja küsi: "Loe läbi ja ütle, mis ei kõla õigesti või on puudu. Parandame kohe."

---
name: _candidates
description: Kandidaat-väidete ledger — ülendamist ootavad tähelepanekud üle moodulite ja vestluste
layer: ledger
type: portfolio
updated: 2026-08-19
review_after: 2026-11-17
sensitivity: restricted
tags: [portfolio]
---

# Kandidaadid

Ühe vaatluse pealt tehtud tähelepanekud, mis ei ole veel püsikonteksti väärt. See fail on **allikakihi osa, mitte vestluse olek**. Ilma temata laguneb kahe sõltumatu vaatluse reegel vaikselt ära: esimene vaatlus tuleb ühest moodulist, teine võib tulla nädalaid hiljem teisest moodulist või hoopis teisest vestlusest, ja neid ei viiks miski kokku.

**Loetakse mooduli alguses. Kirjutatakse mooduli lõpus.** Iga režiim, ka kiire, lõpetab selle faili uuendamisega.

## Mis läheb ledgerisse ja mis mitte

Kandidaat ei ole "kõik, mis kiires režiimis tekib". Kandidaat on **ühe vaatluse pealt tehtud AI-tuletus**. Kolm rada lähevad lahku juba kiires režiimis:

| Mis see on | Staatus | Kas läheb ledgerisse |
|---|---|---|
| kasutaja enda öeldud fakt või üldreeglina sõnastatud reegel | `kinnitatud` | ei |
| muster, mida katab kaks sõltumatut päris näidist | `toetatud` | ei |
| ühe vaatluse pealt tehtud AI-tuletus | `kandidaat` | jah |

Kiire režiim nõuab lepingu järgi vähemalt kahte sõnasõnalist kirjutamisnäidist. Kaks näidet on kaks sõltumatut allikat, seega **kiire režiim jõuab `toetatud` tasemeni päriselt**, mitte ainult teoorias. Ta ei ole kandidaadivabrik.

Ütlemine on tõend: kui kasutaja ütleb "ma ei kasuta kunagi mõttekriipse", on see kohe `kinnitatud` ega vaja vaatlusi. Vaatluste kogunemine ei tee kunagi `kinnitatud`-it — see rada viib `toetatud`-ini.

Süvarežiimi ülesanne siin on kitsas ja konkreetne: ülendada või kustutada read, mis jäid `kandidaat`-iks.

## Ülendamise reegel

| Praegu | Ülendub kui | Tulemus |
|---|---|---|
| `kandidaat` | kasutaja kinnitab selle otse üldreeglina | `kinnitatud` |
| `kandidaat` | lisandub vaatlus **teisest allikast** (`<allikas>` osa erineb) | `toetatud` |
| `kandidaat` | aegumistähtaeg möödub ilma teise vaatluseta | kustuta või küsi üle |

**Allikas on üks konkreetne artefakt või olukord** — üks e-kiri, üks postitus, üks otsusejuhtum. Kaks lõiku samast LinkedIn-postitusest on üks allikas ega ülenda midagi. `sample-01` ja `sample-02` on kaks allikat ja ülendavad, ka siis kui mõlemad juhtuvad olema e-kirjad. Kanal ei ole allikas.

Leping keelab üldnimed allika ID-na: `email`, `linkedin`, `channel`, `document`, `message`, `situation`, `interview`. `evidence_ids` veerus peab iga ID nimetama konkreetset artefakti või olukorda.

Ülendatud rida läheb sihtfaili märkega:

`- <väide> <!-- claim: status=toetatud; evidence=sample-01:avalause,sample-02:avalause -->`

`kinnitatud` ei tule kunagi vaatluste kogunemisest. Ta tuleb ainult sellest, et kasutaja ütles seda ise, ja kannab märget `basis=user-stated`. Kolm vaatlust ei ole ütlemine — need viivad `toetatud`-ini, mitte `kinnitatud`-ini.

## Ledger

| id | target_file | target_section | claim | evidence_ids | scope | expires | status |
|---|---|---|---|---|---|---|---|

Näide uuest kandest (ära hoia näidet ledgeris):

```markdown
| `c-001` | `communication-style.md` | `avoid` | Eelistab külmkontaktis lühikest avangut. | `sample-02:avalause` | kanal: LinkedIn | 2026-11-17 | `kandidaat` |
```

**Veerud:**

- **`id`** — stabiilne viide, `c-NNN`. Ära taaskasuta kustutatud ID-d.
- **`target_file` / `target_section`** — kuhu väide läheb, kui ta ülendub. `target_section` on `<!-- section: ... -->` ankru ID sihtfailis. Ilma nendeta ei tea ülendaja, kelle omandisse väide kuulub, ja sektsioonitasandi omand ei kehti.
- **`claim`** — väide ühe lausega, sõnastatuna nii, nagu ta sihtfaili läheks.
- **`evidence_ids`** — `<allikas>:<vaatlus>` ID-d, komadega. Ülendamiseks `toetatud` tasemele peab siin olema kaks **erinevat** `<allikas>` osa.
- **`scope`** — tingimus, mille all väide kehtib: `aeg`, `kanal`, `roll` või `olukord`. Enamik "vastuolusid" kahe väite vahel ei ole vastuolud, vaid kaks eri scope'i. Kui uus vaatlus räägib vanale vastu, küsi kõigepealt, mis nende scope'i eristab, ja alles siis, kumb on õige.
- **`expires`** — kuupäev, mille järel kandidaat kas kustutatakse või küsitakse üle. Vaikimisi 90 päeva; kiiresti liikuva `current-projects.md` puhul 30.
- **`status`** — `kandidaat`, kuni ta ledgeris on. Ülendamise hetkel liigub rida sihtfaili ja kaob siit. Veerg on olemas selleks, et ledger ja sihtfail räägiksid sama keelt, mitte selleks, et siin oleks mitu staatust korraga.

## Mida siin ei ole

Kandidaadid **ei lähe projektsioonidesse**. `portfolio/bundles/` kokkupanek jätab `kandidaat`-read välja; `kinnitatud` ja `toetatud` read lähevad. See fail on `restricted`: ta hoiab kinnitamata väiteid kasutaja ja tema inimeste kohta, ja kinnitamata väide, mis satub väljaminevasse sõnumisse, on täpselt see viga, mille vastu kogu staatussüsteem on ehitatud.

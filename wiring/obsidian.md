# Kuidas ühendada: Obsidian

Obsidian on parim keskkond, kus selles repos igapäevaselt elada. See on markdown-natiivne, graafivaade (graph view) lööb särama, kui su viki kasvab, ja Dataview muudab päiste (frontmatter) reeglid reaalseteks päringuteks.

## Ava repo kui Vault (hoidla)

1. Obsidian → File → Open folder as vault → vali selle repo juurkaust.
2. Lase Obsidianil kaust indekseerida. Vikilingid (`[[wiki/.examples/concepts/foo]]`) hakkavad tööle; siselingid muutuvad klõpsatavaks.
3. Ava graafivaade (vasak külgriba → graafi ikoon või `Ctrl/Cmd-G`). Niipea kui hakkad lehti kompileerima, näed oma vikit ühendatud võrgustikuna.

## Graafivaade

- **0 vikilehte:** graaf on tühi. Nii peabki.
- **10 lehte (kui teed läbi `.examples/` harjutuse):** peaksid nägema väikest ühendatud kobarat. Kontseptsioonid viitavad teemadele, allikad viitavad kontseptsioonidele ja olemid (entities) tõmbuvad kontseptsioonide poole, mis neile viitavad.
- **50+ lehte:** filtreeri graafi, et peita `portfolio/`, `raw/` ja `templates/`, nii et näha jääb ainult vikikiht. Siin hakkab graaf oma hinda õigustama.

## Dataview päringud (frontmatteri pealt)

Failis `CLAUDE.md` toodud frontmatteri reeglid on Dataview-sõbralikud. Paigalda Dataview community plugin ja saad teha selliseid päringuid:

**Leia kõik ainult ühe allikaga kontseptsioonilehed (koristuskandidaadid):**

```dataview
LIST
FROM "wiki"
WHERE type = "concept" AND length(sources) < 2
```

**Leia portfooliofailid, mida pole 90 päeva üle vaadatud:**

```dataview
LIST
FROM "portfolio"
WHERE last_reviewed < date(today) - dur(90 days)
```

**Kuva aegunud (stale) või uuega asendatud (superseded) vikilehed:**

```dataview
TABLE status, updated
FROM "wiki"
WHERE status = "stale" OR status = "superseded"
SORT updated DESC
```

Viska need kuhugi töölaua-märkmikusse (nt `wiki-health.md`) ja pinn'i see ära — sellest saab reaalajas tervisekontrolli vaade, ilma et peaksid tervet lintimise tsüklit läbi tegema.

## Obsidian Web Clipper → `raw/`

Ametlik Obsidian Web Clipper laiendus suudab artikleid otse õigesse kausta lõigata. Seadista ta nii, et asjad lendaksid otse `raw/` kausta — artiklid maanduvad seal markdownina, valmis järgmiseks ingest'i tsükliks. See on vikikihi jaoks kõige odavam ja lühem sissevõtutee. Mida madalam on allikate lisamise hõõrdumine, seda kiiremini viki kasvab.

## Kiirklahv piltide allalaadimiseks

Kui lõikad või kleebid sisu koos piltidega, seadista kiirklahv (hotkey) valikule "Download all images" (olenevalt Obsidiani versioonist on see kas plugin või sisse ehitatud). Lokaalselt salvestatud pildid elavad linkide kõdunemise (link rot) üle, URL-idena kleebitud pildid aga mitte.

## Sünkroniseerimine üle seadmete (Google Drive / iCloud)

Kui tahad sama vault'i mitmes masinas ilma Obsidian Synci eest maksmata, pane see repo Google Drive'i, iCloudi või Dropboxi. Iga masin avab kausta kui sama vault'i ja muudatused jooksevad pilve kaudu laiali.

Tähelepanu!

- Sünkroniseerimise konfliktid on kerged tulema, kui muudad asju kahes masinas samal ajal. Obsidian saab sellega enamasti kenasti hakkama, aga hardcore kasutajad peaksid puhtama lahendusena kaaluma siiski Obsidian Synci.
- Symlink'id (sümbollingid) lähevad pilvesüncis kergelt katki. Hoia vault'i juurkausta füüsiliselt sünc-kaustas, mitte ära tee sinna symlink'i.

## Kasulikud pluginad

- **Dataview** — frontmatteri päringud (vt ülevalt).
- **Obsidian Web Clipper** — allikate püüdmine.
- **Templater** — et uutel viki-/portfooliofailidel frontmatteri plokk automaatselt ära täita (pole kohustuslik, aga teeb asja kiiremaks).
- **Text Generator** või **Claude/ChatGPT pluginad** — juhuks, kui tahad ingest / compile / query operatsioone teha otse Obsidianis, ilma kuskile mujale minemata.

## Töövoolised märkmed

- Hoia `CLAUDE.md` koguaeg ühes tabis pinned (kinnitatud). Viska sellele pilk peale, kui sina või mõni AI agent hakkab siin vault'is asjatama.
- `log.md` on ainult lisamiseks (append-only). Ära lase Obsidiani auto-formatil seda ringi tõsta.
- Kui jagad seda vault'i terve tiimiga (isikliku konteksti repo puhul ebatavaline, aga võimalik), kasuta millegi tundliku jaoks kausta `.private/` (Faas 2). Ära looda sellele, et "ma lihtsalt ei ava seda faili, kui teised näevad."

# Ühendamine: Obsidian

> **Vabatahtlik samm.** Obsidian ei ole selle süsteemi eeldus — failid on tavaline markdown ja töötavad igas redaktoris. Obsidian teeb nende haldamise mugavamaks. Vt [`wiring/README.md`](README.md).

Obsidian on markdown-natiivne, graafivaade lööb särama, kui wiki-kiht kasvab, ja Dataview muudab päiseväljad päringuteks.

## Ava repo

1. Obsidian → File → Open folder as vault → vali selle repo juurkaust.
2. Lase indekseerida. Siselingid muutuvad klõpsatavaks.
3. Graafivaade: vasak külgriba → graafi ikoon, või `Ctrl/Cmd-G`.

Obsidiani mõistes on see kaust "vault". Selles repos mujal seda sõna ei kasutata — kontekstifailid elavad lihtsalt kaustas ja Skill ei vaja Obsidianit kuidagi.

## Dataview päringud

Paigalda Dataview plugin. Kontekstifailide päistes on päringuteks `updated`, `review_after` ja `sensitivity`.

**Failid, mille ülevaatuse tähtaeg on möödas:**

```dataview
TABLE updated, review_after
FROM "portfolio"
WHERE review_after != null AND review_after < date(today)
SORT review_after ASC
```

See on kogu hooldusprotsess ühe päringuna. `review_after` on täpselt selleks olemas — väli, mida keegi ei loe, oleks mõttetu metaandme.

**Failid, mis ei tohi väljapoole minna:**

```dataview
LIST
FROM "portfolio"
WHERE sensitivity = "restricted"
```

Vastus sisaldab alati `team-and-relationships.md`. Neid võib olla rohkem, näiteks kliendinimedega `writing-samples.md`. Nii näed, mida ei tohi vaikimisi jagatavasse agenti anda.

**Tõendikiht eraldi:**

```dataview
LIST
FROM "portfolio"
WHERE file.name = "writing-samples" OR file.name = "decision-log"
```

Kaks faili: `writing-samples.md` ja `decision-log.md`. Nemad ei kirjelda sind — nad hoiavad toorainet, mille pealt profiiliväiteid kontrollitakse.

**Wiki-kihi koristuskandidaadid:**

```dataview
LIST
FROM "wiki"
WHERE type = "concept" AND length(sources) < 2
```

Pane need ühte märkmikusse (nt `health.md`) ja pinn'i see ära. Saad reaalajas tervisevaate, ilma et peaksid tervet kontrolli läbi tegema.

## Graafivaade

- **Alguses:** graaf on tühi. Nii peabki.
- **Kui wiki kasvab:** filtreeri välja `portfolio/`, `raw/` ja `templates/`, nii et näha jääb ainult wiki-kiht. Seal hakkab graaf oma hinda õigustama.

Kontekstifailid ei moodusta graafi ega peagi. Nemad on lame komplekt, mida agendid loevad; seosed nende vahel elavad [`portfolio/context-map.md`](../portfolio/context-map.md) failis, mitte vikilinkides.

## Web Clipper → `raw/`

Obsidian Web Clipper lõikab artikleid otse kausta. Seadista ta `raw/` peale — artiklid maanduvad markdownina, valmis järgmiseks wiki-sissekandeks. Mida väiksem hõõrdumine allika lisamisel, seda kiiremini wiki kasvab.

See puudutab ainult wiki-kihti. Kontekstifailid tulevad intervjuust, mitte lõikamisest.

## Sünkroniseerimine üle seadmete

Kui tahad sama kausta mitmes masinas ilma Obsidian Synci eest maksmata, pane repo Google Drive'i, iCloudi või Dropboxi.

Kaks hoiatust:

- Sünkroonikonfliktid tulevad kergesti, kui muudad asju kahes masinas korraga. Obsidian saab enamasti hakkama, aga puhtam lahendus on Obsidian Sync.
- Symlingid lähevad pilvesünkroonis katki. Hoia kausta füüsiliselt sünkroonikaustas.

**Enne kui sa selle kausta pilve paned:** seal võib olla `team-and-relationships.md` (hinnangud nimeliste inimeste kohta), tundlikke kirjutamisnäiteid ja `_candidates.md` (kinnitamata väited). Kontrolli ise pilvekonto ligipääse; jagatud kettale ära pane kogu kausta.

## Kasulikud pluginad

- **Dataview** — päringud päiseväljade pealt.
- **Obsidian Web Clipper** — allikate püüdmine `raw/` kausta.
- **Templater** — täidab uue faili päise automaatselt. `updated`, `review_after` ja `sensitivity` peavad igal juhul olemas olema; Templater säästab kirjutamist.

## Töövoolised märkmed

- Ära redigeeri `portfolio/templates/` faile käsitsi. Šabloonid kannavad masinloetavaid markereid (`<!-- section: ... -->`, `<!-- quick-coverage: ... -->`), mida kontroll loeb. Kustutatud marker läheb märkamatult katki.
- `log.md` on ainult lisamiseks. Ära lase automaatvormindusel seda ringi tõsta.
- Hoia [`portfolio/context-map.md`](../portfolio/context-map.md) ühes tabis lahti, kui sa süsteemi ise kohendad. Seal on kirjas, mis fail mida hoiab ja kes teda kirjutab.
- **Jagamise kohta:** kui see kaust läheb kellegi teisega jagatuks, ei aita see, et sa mõnda faili lihtsalt ei ava. Ainus toimiv piir on faili sealt välja jätta. `sensitivity` väli on märgistus sinu ja sinu agentide jaoks, mitte ligipääsukontroll.

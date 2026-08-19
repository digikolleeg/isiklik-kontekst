# Ühendamine: ChatGPT

> **Vabatahtlik samm.** Tuleb pärast seda, kui neli faili on olemas. Vt [`wiring/README.md`](README.md).

Kolm viisi, lihtsamast keerulisemani. Vali see, mis sobib sellega, kuidas sa ChatGPT-d päriselt kasutad.

## 1. Custom Instructions — kitsas, aga kehtib alati

Custom Instructions püsivad üle paljude vestluste. Ruum on piiratud, nii et sinna mahub ainult kõige kokkupakitum osa.

**"What would you like ChatGPT to know about you?"**

- nimi, roll, organisatsioon (`identity.md`)
- lõik "Mida ma teen" (`identity.md`)
- mida sa müüd ja kellele, üks lause (`current-projects.md`)
- kaks-kolm signatuuri või vältimist (`communication-style.md`)

**"How would you like ChatGPT to respond?"**

- üldine stiil ja pikkuse-eelistus (`communication-style.md`)
- eelistused AI väljundi osas (`preferences-and-constraints.md`)
- üks lause: *"Match my voice. Lead with the answer. No preamble, no closing summary."*

Kui ruum otsa saab, lõika esimesena vältimiste nimekiri. Juhis selle kohta, **kuidas** vastata, kaalub üles nimekirja sellest, mida mitte teha.

**Selles formaadis ei mahu ükski päris kirjutamisnäide.** Custom Instructions annavad sulle reeglid; hääl jääb saamata. Kirjutamise jaoks kasuta 2. või 3. valikut.

## 2. Custom GPT — täiskomplekt teadmusfailidena

Õige lüke, kui tahad püsivat assistenti, mis tunneb sind süvitsi.

1. ChatGPT → Explore GPTs → Create.
2. Lae kontekstifailid üles teadmusfailidena.
3. Juhistesse kleebi kokku pandud pakk `portfolio/bundles/` alt, või kirjuta oma juhis (allpool).

```
You have my context files as knowledge. Before answering anything where my role, offer, preferences or voice shape the answer, read the relevant file.

Before writing anything in my name, read communication-style.md and writing-samples.md. Follow the rules and pattern-match the samples — sentence length, how I open, how I close. Never copy a sample verbatim.

Never state a fact, number, or client name that is not in the files. If current-projects.md has a "must not claim" section, treat those lines as hard prohibitions.
```

**Mida ehitada:**

- kontaktivõtu-GPT paki [`client-outreach.md`](../portfolio/bundles/client-outreach.md) põhjal
- sisulooja-GPT paki [`content-writer.md`](../portfolio/bundles/content-writer.md) põhjal
- taustatöö-GPT paki [`client-research.md`](../portfolio/bundles/client-research.md) põhjal

Pakid on projektsioonid: sa paned nad ise kokku, kleepides oma failide sisu kohatäitjate juurde. Automaatset kokkupanijat ei ole.

**Custom GPT-sid saab jagada.** Sellepärast on siin kaks reeglit range: `team-and-relationships.md` ei lähe jagatavasse GPT-sse, ja `kandidaat`-märkega read jäävad välja. Jagatud GPT tähendab, et kontekst on väljaspool sinu kontrolli.

## 3. Projects — failid pluss projekti juhised

Sarnane Claude Projects'ile: manustatud failid ja projekti juhised püsivad selle projekti vestlustes.

1. Loo uus Project.
2. Manusta kontekstifailid.
3. Projekti juhistesse kleebi kokku pandud pakk.

**Millal Projects on parem kui Custom GPT:** kui sa tuunid juhiseid tihti, kui sul pole vaja tulemust jagada, ja kui sa tahad säilitada võimaluse alustada vestlusi väljaspool projekti.

## Kõigi kolme jaoks

- **Uuenda, kui failid muutuvad.** ChatGPT-s olevad failid on koopiad, mitte lingid. Aegunud kontekst on nähtamatu ja tõmbab kvaliteedi vaikselt alla.
- **Vali failid kasutusjuhu järgi**, ära kleebi kõike kõikjale. Ebaoluline kontekst lahjendab olulist.
- **`portfolio/_candidates.md` ei lähe kunagi üles.** Seal on kinnitamata väited.
- **Testi:** *"Draft a two-sentence intro to a new prospect in my voice."* Kui see kõlab sinuna ilma parandusteta, ühendus töötab. Kui ei, on `communication-style.md` liiga ümmargune või `writing-samples.md` täidetud poleeritud turundustekstiga — asi ei ole juhtmetes.

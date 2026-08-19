# Agent Bundles

Eelnevalt kokku pandud kontekstipakid, mis on valmis kleepimiseks mis tahes agendi system prompti või custom-instructions lahtrisse.

**Bundle on projektsioon, mitte tõeallikas.** Ta ei hoia konteksti — ta paneb selle kokku allikafailidest, mis on iga bundle'i päises `sources` all kirjas. Kui allikas muutub, nõelu bundle uuesti. Käsitsi tehtud parandus bundle'i sees läheb allikast lahku ja keegi ei märka, kumb kehtib. Kihtide täielik kaart: [`portfolio/context-map.md`](../context-map.md).

Iga bundle on üks markdown-fail, mis koosneb kolmest osast:

1. **Sissejuhatus (Preamble)** — spetsiaalselt kirjutatud juhised, mis ütlevad agendile, mis rolli ta täidab ja kuidas ta peab järgnevat konteksti kasutama.
2. **Kohatäitjad (Placeholder blocks)** — selgelt märgistatud plokid nagu `[[IDENTITY]]`, kuhu sa kleebid sisu oma täidetud portfooliofailidest.
3. **Koostamise märkused** — millised portfooliofailid toidavad millist plokki ja miks.

Bundle'id on puuduv lüli "mul on portfooliofailid" ja "mul on päriselt töötav agent" vahel. Need töötavad ilma igasuguse lisatööriistata: kleebi see Custom GPT-sse, Claude Projecti, Gemini Gemi või mis iganes agendiraamistiku süsteemiprompti lahtrisse, mida sa kasutad.

---

## Mis kaasas on

| Bundle | Millest koosneb | Kellele mõeldud |
|--------|---------------|-----|
| [`content-writer.md`](content-writer.md) | `identity.md` + `communication-style.md` + `writing-samples.md` + `domain-knowledge.md` | Agendid, mis kirjutavad sinu häälega blogipostitusi, LinkedIni sisu, uudiskirju ja turundustekste. |
| [`client-outreach.md`](client-outreach.md) | `identity.md` + `current-projects.md` + `communication-style.md` + `writing-samples.md` | Agendid, mis koostavad külmi e-kirju, järelkajastusi (follow-up'e), pakkumisi ja vastuseid potentsiaalsetele klientidele. |
| [`client-research.md`](client-research.md) | `identity.md` + `current-projects.md` + `domain-knowledge.md` | Agendid, mis teevad enne olulist vestlust taustakontrolli — uurivad potentsiaalseid kliente, konkurente, valdkonna konteksti. |

`client-outreach.md` allikad on täpselt töötoa-režiimi neli väljundfaili. Kiire intervjuu ei tooda tükke, mis alles hiljem kokku sobituvad — ta toodab ühe töötava agendi sisendi.

---

## Kaks reeglit, mis kehtivad igale bundle'ile

**1. Kandidaat-väited jäävad välja.** Allikafailides on iga rida märgistatud `kinnitatud`, `toetatud` või `kandidaat`. Kokkupanekul jäetakse `kandidaat`-read välja. Kandidaat on ühe vaatluse pealt tehtud oletus; oletus, mis satub väljaminevasse sõnumisse, on täpselt see viga, mille vastu staatussüsteem on ehitatud. Kui kandidaat on mingi ülesande jaoks hädavajalik, kleebi ta sisse koos märkega ja käsitle teda oletusena.

**2. Tundlikkus kandub allikast pakki.** `team-and-relationships.md` on alati `restricted`, kuid ka mõni muu fail võib selleks muutuda — näiteks `writing-samples.md`, kui päris kliendinimed jäid sisse. Päise `exportable` on malli vaikeväärtus, mitte lubadus valmis paki kohta. Kui üks kasutatud allikas on `restricted`, muutub kogu bundle `restricted`-iks. Ära jäta vajalikku allikat vaikselt välja ja nimeta tulemust valmis pakiks.

Mõlemat kontrollib `python3 scripts/context_v3_check.py --rule projection --input portfolio/bundles/<fail>.md`.

---

## Kuidas Bundle'it kasutada

Kaks teed sõltuvalt sellest, kas su agent saab kontekstikausta faile lugeda või mitte.

### Tee A — Agentne (kaustale ligipääsuga agent)

Agent loeb bundle'i ja sinu portfooliofailid ise, paneb terviku kokku ja annab sulle valmis system prompt'i.

1. Ava kontekstikaust agendi töökaustana või anna talle nende failide lugemisõigus.
2. Ütle agendile:
   > *"Lae `portfolio/bundles/client-outreach.md` ja täida kohatäitjad minu kontekstifailidega. Anna tagasi terve kokku pandud bundle."*
3. Agent loeb päise `sources` all viidatud failid, asendab `[[IDENTITY]]`, `[[VOICE]]`, `[[RELATIONSHIPS]]` (vms) plokid päris sisuga ja annab sulle valmis markdown'i.
4. Kopeeri see Project'i custom instructions lahtrisse (või kuhu iganes oma agendi prompt'i tahad panna).

Kui portfoolio muutub, küsi uus kokku pandud versioon. Praegu ei ole repos automaatset kompileerijat.

### Tee B — Manuaalne (ükskõik mis chat, ükskõik mis plaan)

Kui sul pole Claude Desktop'i ega Connector'it — või tahad lihtsalt ise kontrollida —, koosta bundle käsitsi.

1. Ava soovitud bundle'i fail.
2. Ava teises aknas oma täidetud portfooliofailid.
3. Kleebi iga kohatäitja ploki juurde (nt `[[IDENTITY]]`) vastava portfooliofaili kogu sisu.
4. Kopeeri see terviklik, kokku nõelutud markdown agendi system prompti / custom instructions lahtrisse.
5. Valmis. Nüüd alustab agent iga vestlust tugevalt ankurdatuna sinu häälde, piirangutesse ja konteksti.

**Nipp:** kui agendi konteksti eelarve on piiratud (context budget is tight), kärbi kleebitud portfoolio sisu ainult kõige asjakohasemate osadeni. Bundle'id on kokkupandavad (composable) — kohanda sissejuhatust ja sisu oma konkreetse kasutusjuhu järgi.

---

## Oma Bundle'ite loomine

Need kolm kaasasolevat bundle'it on lähtepunktid, mitte lõplik nimekiri. Kui leiad end agendile pidevalt sama tüüpi ülesande jaoks samu juhiseid andmas, siis seal ongi peidus uus bundle, mis ootab kirja panemist.

Rusikareeglid koostamisel:

- **Kaasa alati `identity.md`.** Iga agent peab teadma, kelle heaks ta töötab.
- **Hoia bundle'id ühele asjale keskendatuna.** Bundle, mis püüab teha kõike, ei tee lõpuks mitte midagi hästi.
- **Deklareeri päises `projection: true`, `sources` ja `sensitivity`.** Ilma nendeta ei tea keegi, millest bundle koosneb, ja kontroll kukub läbi.
- **Kolm kuni neli allikafaili on tavaliselt õige maht.** Rohkem ja agendi konteksti eelarve hakkab kannatama; vähem ja agent ei suuda teha õigeid otsuseid, mida ta muidu võinuks teha. Häälega kirjutavad agendid vajavad neljandana `writing-samples.md`-i: reeglid ütlevad, mida vältida, näited näitavad, mida teha.
- **Sissejuhatus kaalub konteksti üles.** Konkreetne ja täpne sissejuhatus teeb tihti rohkem tööd kui veel üks juurde kleebitud portfooliofail.

Kirjuta uued bundle'id markdown-failidena siia kausta, järgides sama struktuuri: päis, projektsiooni reeglid, sissejuhatus, kohatäitjad, koostamise märkused.

---

## Bundle'ite sünkroonis hoidmine

Bundle'id põimivad endasse portfoolio sisu viitena (sa kleebid sisu sisse). Kui sa uuendad mingit portfooliofaili, näiteks oma kvartaalse ülevaatuse käigus, siis pead uuesti kokku nõeluma kõik bundle'id, mis seda faili kasutavad. Vastasel juhul töötab agent aegunud kontekstiga.

Praegu tuleb projektsioon pärast allikafaili muutmist uuesti kokku panna. Repos ei ole pakendatud Connectorit ega MCP-serverit, mis seda automaatselt teeks.

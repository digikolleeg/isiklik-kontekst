# Agent Bundles

Eelnevalt kokku pandud kontekstipakid, mis on valmis kleepimiseks mis tahes agendi system prompti või custom-instructions lahtrisse.

Iga bundle on üks markdown-fail, mis koosneb kolmest osast:

1. **Sissejuhatus (Preamble)** — spetsiaalselt kirjutatud juhised, mis ütlevad agendile, mis rolli ta täidab ja kuidas ta peab järgnevat konteksti kasutama.
2. **Kohatäitjad (Placeholder blocks)** — selgelt märgistatud plokid nagu `[[IDENTITY]]`, kuhu sa kleebid sisu oma täidetud portfooliofailidest.
3. **Koostamise märkused** — millised portfooliofailid toidavad millist plokki ja miks.

Bundle'id on puuduv lüli "mul on portfooliofailid" ja "mul on päriselt töötav agent" vahel. Need töötavad ilma igasuguse lisatööriistata: kleebi see Custom GPT-sse, Claude Projecti, Gemini Gemi või mis iganes agendiraamistiku süsteemiprompti lahtrisse, mida sa kasutad.

---

## Mis kaasas on

| Bundle | Millest koosneb | Kellele mõeldud |
|--------|---------------|-----|
| [`content-writer.md`](content-writer.md) | `identity.md` + `communication-style.md` + `domain-knowledge.md` | Agendid, mis kirjutavad sinu häälega blogipostitusi, LinkedIni sisu, uudiskirju ja turundustekste. |
| [`client-outreach.md`](client-outreach.md) | `identity.md` + `communication-style.md` + `team-and-relationships.md` | Agendid, mis koostavad külmi e-kirju, järelkajastusi (follow-up'e), pakkumisi ja vastuseid potentsiaalsetele klientidele. |
| [`client-research.md`](client-research.md) | `identity.md` + `current-projects.md` + `domain-knowledge.md` | Agendid, mis teevad enne olulist vestlust taustakontrolli — uurivad potentsiaalseid kliente, konkurente, valdkonna konteksti. |

---

## Kuidas Bundle'it kasutada

Kaks teed sõltuvalt sellest, kas sul on Claude Desktop koos filesystem Connector'iga või mitte.

### Tee A — Agentne (Claude Desktop + Connector)

Claude loeb bundle'i ja sinu portfooliofailid ise, paneb terviku kokku ja annab sulle valmis system prompt'i.

1. Ava Claude Desktop ja veendu, et filesystem Connector viitab su vault-kausta.
2. Ütle Claude'ile:
   > *"Lae `portfolio/bundles/client-outreach.md` ja täida kohatäitjad minu vault-failidega. Anna tagasi terve kokku pandud bundle."*
3. Claude loeb mallis viidatud failid, asendab `[[IDENTITY]]`, `[[VOICE]]`, `[[RELATIONSHIPS]]` (vms) plokid päris sisuga ja annab sulle valmis markdown'i.
4. Kopeeri see Project'i custom instructions lahtrisse (või kuhu iganes oma agendi prompt'i tahad panna).

Bundle'i uuendamiseks, kui portfoolio muutub: lihtsalt küsi uut kokku pandud versiooni. Konteksti-looja Skill (kui installitud) teeb sama asja.

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
- **Kolm portfooliofaili on tavaliselt õige maht.** Rohkem ja agendi konteksti eelarve hakkab kannatama; vähem ja agent ei suuda teha õigeid otsuseid, mida ta muidu võinuks teha.
- **Sissejuhatus kaalub konteksti üles.** Konkreetne ja täpne sissejuhatus teeb tihti rohkem tööd kui veel üks juurde kleebitud portfooliofail.

Kirjuta uued bundle'id markdown-failidena siia kausta, järgides sama struktuuri: sissejuhatus, kohatäitjad, koostamise märkused.

---

## Bundle'ite sünkroonis hoidmine

Bundle'id põimivad endasse portfoolio sisu viitena (sa kleebid sisu sisse). Kui sa uuendad mingit portfooliofaili, näiteks oma kvartaalse ülevaatuse käigus, siis pead uuesti kokku nõeluma kõik bundle'id, mis seda faili kasutavad. Vastasel juhul töötab agent aegunud kontekstiga.

Logimise tava on lihtne: kui uuendad portfooliofaili, pane `log.md` kirja, milliseid bundle'eid see muudatus mõjutas, et saaksid aru, mis vajab uuendamist.

Teises faasis toome välja MCP tööriista (`get_bundle(agent_type)`) mis teeb selle kokkupaneku automaatselt jooksvalt (at runtime) ja võtab selle hoolduskoorma sinu õlult ära. Kuni sinnamaani tuleb asju käsitsi kokku kleepida — aga see on kiire, sest bundle'id on lühikesed.

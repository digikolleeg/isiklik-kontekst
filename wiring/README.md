# Ühendamine

Kuidas viia oma kontekst sinna, kus sa AI-d päriselt kasutad.

> **See on vabatahtlik ja tuleb hiljem.** Ühendamine ei tee konteksti paremaks — ta viib olemasoleva konteksti rohkematesse kohtadesse. Kui neli faili on alles tegemata või [RUBRIC.md](../RUBRIC.md) värav 1 ei ole läbitud, ei paranda ükski siinne juhend midagi. Alusta [quick-start.md](../quick-start.md) juurest.

## Vali üks

| Juhend | Millal |
|---|---|
| [`system-prompt-patterns.md`](system-prompt-patterns.md) | universaalne kopeeri-kleebi, töötab igal pool |
| [`claude-projects.md`](claude-projects.md) | sa kasutad Claude'i ja tahad püsivat konteksti |
| [`chatgpt-web.md`](chatgpt-web.md) | sa kasutad ChatGPT-d |
| [`obsidian.md`](obsidian.md) | sa tahad faile ise mugavalt hallata |
| [`mcp-resource.md`](mcp-resource.md) | mitu tööriista, üks allikas, ilma kleepimiseta |
| [`openclaw-agents.md`](openclaw-agents.md) | sa ehitad oma agente |
| [`api-layer.md`](api-layer.md) | sa ehitad tarkvara, mis konteksti pärib |

Alusta sellest tööriistast, mida sa kõige rohkem kasutad. Üks töötav ühendus on parem kui neli poolikut.

## Kolm reeglit, mis kehtivad igale ühendusele

**1. Tundlikkus kandub edasi.** `team-and-relationships.md` on alati `restricted`, kuid ka kliendinimedega `writing-samples.md` võib olla piiratud. Kui ühe neist kaasa paned, on kogu komplekt `restricted`: kasuta seda ainult enda valitud privaatses tööriistas, ära jaga komplekti ega anna sellele autonoomset saatmisõigust. Kasutaja üle vaadatud mustand on teine asi kui agent, mis saadab ise.

**2. `portfolio/_candidates.md` ei lähe kunagi.** Seal on kinnitamata väited, mis ootavad teist sõltumatut tõendit. Kandidaat, mis satub väljaminevasse sõnumisse, on täpselt see viga, mille vastu staatussüsteem on ehitatud.

**3. Agendipakk on projektsioon.** `portfolio/bundles/` all olev pakk ei hoia konteksti — ta paneb selle kokku failidest, mis on tema päises `sources` all kirjas. Sa paned ta kokku ise, käsitsi. **Automaatset kompileerijat ei ole.** Kui allikafail muutub, nõelu pakk uuesti; ära paranda pakki käsitsi, sest siis läheb ta allikast lahku ja keegi ei märka.

## Mida sa üldse ühendad

Üksteist faili kahes rollis: üheksa profiilifaili (mida sinu kohta teatakse) ja kaks tõendifaili — `writing-samples.md` ja `decision-log.md` (mille pealt seda teatakse).

`writing-samples.md` on see, mille inimesed ühendamisel vahele jätavad. Ära jäta. Reeglid ütlevad agendile, mida vältida; näited näitavad, mida teha. Igal pool, kus agent kirjutab sinu häälega, peab ta jõudma näideteni.

Kaart, mis fail mida hoiab: [`portfolio/context-map.md`](../portfolio/context-map.md).

# Alustamine

Kaks süsteemi. Ehita need järjekorras — portfoolio enne, wiki pärast.

---

## Samm 1: ehita oma portfoolio

Portfoolio on vundament. See ütleb wikile, kelle jaoks teda ehitatakse.

### Variant A: kasuta veebirakendust

Spetsiaalselt loodud intervjueerija-agent viib kogu protsessi läbi.

1. Mine [app URL] aadressile.
2. Logi sisse oma emailiga (maagiline link, parooli pole vaja).
3. Agent intervjueerib sind järjest läbi kõik kümme faili.
4. Lae oma valmis portfoolio zip-failina alla.
5. Kopeeri failid selle repo `portfolio/` kausta.

Kogu asi võtab ühe istumisega 30–60 minutit. Enamus inimesi jagab selle paari korraga.

### Variant B: tee ise

1. Ava ükskõik milline šabloon `portfolio/templates/` kaustast.
2. Kleebi terve fail Claude'i või ChatGPT-sse.
3. Ütle "alustame sellega".
4. Su AI ehituspartner loeb sissekirjutatud intervjuu-protokolli ja hakkab küsima.
5. Kui tal on piisavalt, koostab ta faili. Loe see üle ja paranda, mis on valesti.
6. Salvesta lõplik versioon `portfolio/` kausta (või enda valitud alamkausta).
7. Korda sama ülejäänud šabloonidega.

**Soovituslik järjekord:** alusta `identity.md` ja `role-and-responsibilities.md` failidega — kõik ülejäänu ehitub neile kahele.

**Täielik järjestus:**
1. `identity.md`
2. `role-and-responsibilities.md`
3. `current-projects.md`
4. `team-and-relationships.md`
5. `tools-and-systems.md`
6. `communication-style.md`
7. `goals-and-priorities.md`
8. `preferences-and-constraints.md`
9. `domain-knowledge.md`
10. `decision-log.md`

**Näpunäited:**
- Ole konkreetne, mitte ihaldav. Su agentidele on vaja päris tõde, mitte kuidas sa sooviks, et töötaksid.
- Ära jäta reaktsiooni-ringi vahele. Kui su ehituspartner faili koostab, loe see üle ja paranda, mis vale läks. Sealt tuleb päris signaal.
- Lühem on parem kui pikem. Üks lehekülg faili kohta, mitte viis. Tihe kontekst töötab paremini kui laialivalguv.

---

## Samm 2: seadista wiki

Ava selles repos uus Claude Code sessioon ja ütle:

> "Loe CLAUDE.md, siis loe minu portfoolio-failid kaustast portfolio/. Sa oled minu LLM wiki agent. Kinnita, et saad aru sissekande, päringu ja kontrolli töövoogudest, ning ütle, mida vajad esimese allika sissekandeks."

Seejärel pane oma esimene allikas `raw/` kausta ja ütle "tee sissekanne".

Selles see ongi. LLM loeb allika, loob wiki-lehed, uuendab indeksi ja lisab logisse. Pane järgmine allikas peale, kui üks tuleb.

**Mis teeb hea esimese allika:**
- Midagi, mida oled juba lugenud ja väärtuslikuks pidanud
- Artikkel, transkriptsioon, koosolekumärkmed või uurimistöö
- Tekstipõhine (PDF-id sobivad; piltide jaoks tuleb LLM-i eraldi appi võtta)

**Pärast esimest sissekannet:** ava Obsidian sellel kaustal. Graafi-vaates näed, mis tekkis ja kuidas need omavahel seotud on.

---

## Samm 3: ühenda see kõik kokku

Wiki ja portfoolio on kõige kasulikumad siis, kui need on ligipääsetavad ka su teistele AI tööriistadele — mitte ainult Claude Code sessioonidele selles repos.

Vaata `wiring/` kausta:
- **`mcp-resource.md`** — too mõlemad kihid välja MCP ressurssidena (kõige automaatsem)
- **`system-prompt-patterns.md`** — kopeeri-kleebi mustrid Claude'i, ChatGPT ja Gemini jaoks
- **`claude-projects.md`** — kasuta oma portfooliot Claude Projects'is
- **`api-layer.md`** — ehita API kiht, kui tahad programmilist juurdepääsu

Alusta sellest tööriistast, mida kõige rohkem kasutad.

---

## Pidev hooldus

**Portfoolio:** vaata kord kvartalis üle või siis, kui midagi olulist muutub (uus töö, uued projektid, suur prioriteedimuutus). Küsi Claude Code'lt: "Aita mul `current-projects.md` uuendada — siin on, mis on muutunud."

**Wiki:** lisa allikaid alati, kui loed midagi, mis tasub säilitada. Tee kontrollkäik kord kuus: "Tee wikile tervisekontroll — otsi vastuolusid, orvuks jäänud lehti, vananenud väiteid ja puuduvaid ristviiteid."

**Logi:** käivita `grep "^## \[" log.md | tail -10`, et näha viimast aktiivsust.

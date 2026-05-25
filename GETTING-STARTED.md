# Alustamine

Kaks süsteemi. Ehita need järjekorras — portfoolio enne, wiki pärast.

---

## Samm 1: ehita oma portfoolio

Portfoolio on vundament. See ütleb wikile, kelle jaoks teda ehitatakse.

Sa saad portfoolio ehitada **kahel teel**. Mõlemad annavad sama lõpptulemuse: täidetud markdown-failid kaustas `portfolio/`.

### Tee A — Agentne (Claude Desktop + Konteksti-looja Skill)

Soovituslik, kui sul on Claude Pro/Max ja Claude Desktop. Skill viib intervjuu läbi ja **kirjutab failid otse sinu vault-kausta** läbi filesystem Connector'i. Sa lihtsalt vastad küsimustele.

1. Seadista Claude Desktopis filesystem Connector, mis viitab sinu vault-kaustale (näiteks `portfolio/` selles repos või `~/isiklik-kontekst/portfolio/`). Detailne juhend: `wiring/mcp-resource.md`.
2. Installeeri Konteksti-looja Skill: Claude Desktop → Settings → Skills → Add → vali `skills/konteksti-looja/` selles repos.
3. Uues vestluses ütle "alustame intervjuud" (või "täida `identity.md`" konkreetse faili jaoks).
4. Skill küsib küsimusi, näitab mustandit ja salvestab faili otse kausta. Korda iga šablooni jaoks.

Kui Connector või Skill ei toimi, langeb Skill ise tagasi Tee B režiimi.

### Tee B — Manuaalne (mis tahes AI chat)

Töötab kõigi tasuta plaanidega — Claude.ai, ChatGPT, Gemini, ükskõik mis. Aeglasem, aga universaalne.

1. Ava ükskõik milline šabloon `portfolio/templates/` kaustast.
2. Kleebi terve fail Claude'i või ChatGPT-sse.
3. Ütle "alustame sellega".
4. Su AI ehituspartner loeb sissekirjutatud intervjuu-protokolli ja hakkab küsima.
5. Kui tal on piisavalt infot, siis ta koostab faili. Loe see üle ja paranda, mis on valesti.
6. Kopeeri faili sisu vestlusest ja salvesta käsitsi `portfolio/` kausta (või enda valitud alamkausta).
7. Korda sama ülejäänud šabloonidega.

### Mõlema tee jaoks

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
- Ära unusta parandada. Kui su ehituspartner faili koostab, loe see üle ja paranda, mis on valesti. Sealt tuleb see päris signaal.
- Lühem on parem kui pikem. Üks või kaks lehekülge faili kohta, mitte viis. Tihe kontekst töötab paremini kui laialivalguv.

---

## Samm 2: seadista wiki

Ava selles repos uus Claude Code sessioon ja ütle:

> "Loe CLAUDE.md, siis loe minu portfoolio-failid kaustast portfolio/. Sa oled minu LLM wiki agent. Kinnita, et saad aru sissekande, päringu ja kontrolli töövoogudest, ning ütle, mida vajad esimese allika sissekandeks."

Seejärel pane oma esimene allikas `raw/` kausta ja ütle "tee sissekanne".

LLM loeb allikat, loob wiki-lehed, uuendab indeksi ja lisab logisse. Seejärel lisa järgmine allikas.

**Mis teeb hea esimese allika:**
- Midagi, mida oled juba lugenud ja väärtuslikuks pidanud
- Artikkel, transkriptsioon, koosolekumärkmed või uurimistöö
- Tekstipõhine (PDF-id sobivad; piltide jaoks eraldi LLM appi võtta)

**Pärast esimest sissekannet:** ava Obsidian selles kaustal. Graafikut vaates näed, mis info tekkis ja kuidas need omavahel seotud on.

---

## Samm 3: ühenda see kõik kokku

Wiki ja portfoolio on kõige kasulikumad siis, kui need on ligipääsetavad ka teistele AI tööriistadele — mitte ainult Claude Code sessioonidele selles repos.

Vaata `wiring/` kausta:
- **`mcp-resource.md`** — too mõlemad kihid välja MCP ressurssidena (kõige automaatsem)
- **`system-prompt-patterns.md`** — kopeeri-kleebi mustrid Claude'i, ChatGPT ja Gemini jaoks
- **`claude-projects.md`** — kasuta oma portfooliot Claude Projects'is
- **`api-layer.md`** — ehita API kiht, kui tahad programmilist juurdepääsu

Alusta sellest tööriistast, mida kõige rohkem kasutad.

---

## Pidev hooldus

**Portfoolio:** vaata kord kvartalis üle või siis, kui midagi olulist muutub (uus töö, uued projektid, suur prioriteedimuutus).

- **Tee A:** ütle Konteksti-looja Skill'ile: "Uuendame `current-projects.md` — siin on, mis on muutunud."
- **Tee B:** ava fail ise, vaata üle, küsi Claude'ilt parandussoovitusi.

**Wiki:** lisa allikaid alati, kui loed midagi, mis tasub säilitada. Tee kontrollkäik kord kuus: "Tee wikile tervisekontroll — otsi vastuolusid, orvuks jäänud lehti, vananenud väiteid ja puuduvaid ristviiteid."

**Logi:** käivita `grep "^## \[" log.md | tail -10`, et näha viimast aktiivsust.

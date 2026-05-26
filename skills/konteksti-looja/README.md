# Konteksti-looja Skill

Claude Desktop / Claude Code Skill, mis intervjueerib sind ja koostab automaatselt sinu isikliku konteksti-portfoolio failid. Failid kirjutatakse otse sinu vault-kausta — sa lihtsalt vastad küsimustele.

## Installeerimine (Claude Desktop)

1. Klooni või lae alla see repo (`digikolleeg/isiklik-kontekst`).
2. Claude Desktop → Settings → Skills → Add Skill → vali kaust `skills/konteksti-looja/`.
3. Kontroll: uues vestluses ütle "mis Skill-id mul installitud on?". Konteksti-looja peaks loendis olema.

**Vajalik:** Claude Pro/Max plaan (Skills on Pro/Max funktsionaalsus).

## Vault-kausta seadistus

Skill kirjutab failid otse sinu kausta läbi filesystem Connector'i. Et see toimiks:

1. Loo vault-kaust (vaikimisi: `~/isiklik-kontekst/portfolio/`).
2. Claude Desktop → Settings → Connectors → Add filesystem connector → vali ülaltoodud kaust.
3. Kontroll: küsi Claude'ilt "kas sa näed minu vault-kausta?". Ta peaks nimetama kausta tee.

**Kui Connector ei tööta:** Skill langeb automaatselt manuaalsele režiimile — näitab failide sisu vestluses ja sa salvestad need käsitsi. Toimib ka ilma Connector'ita, ainult aeglasemalt.

Detailne MCP/Connector seadistus: vt repo juurest `wiring/mcp-resource.md`.

## Käivitamine

| Mida sa ütled | Mida Skill teeb |
|---|---|
| `alustame intervjuud` | Näitab failide menüüd, küsib mida täita |
| `töötoa intervjuu` | **Töötoa režiim:** 3 faili (identity + communication-style + current-projects) ühe vooga, ~30 min |
| `täida current-projects.md` | Üks fail, täielik intervjuu |
| `uuendame goals-and-priorities.md` | Olemasoleva faili uuendamine (loeb vana, küsib mis muutus) |
| `täida ülejäänud failid` | Liigub järjest läbi puuduvate failide |

## Töötoa-režiim

Lühem intervjuu, mille eesmärk on saada **kolm faili 30 minutiga** — piisavalt, et müügiassistent käima panna. Kasutatakse Digikolleeg inkubaator-töötubades. Ülejäänud 7 faili saab täita hiljem.

## Mis edasi

Kui sul on failid täidetud, vaata:
- Repo juurest `quick-start.md` — kuidas failid Claude Project'i kokku panna ja esimene müügiemail kirjutada
- `portfolio/bundles/` — valmis agendi-paketid (müügiassistent, kliendi-uurija, sisukirjutaja), mis kombineerivad sinu faile spetsiifilisteks töövoogudeks
- `wiring/` — kuidas konteksti-portfooliot ühendada teiste AI tööriistadega (ChatGPT, Gemini, MCP jne)

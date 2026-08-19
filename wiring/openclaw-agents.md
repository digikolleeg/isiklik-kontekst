# Ühendamine: OpenClaw agendid

> **Vabatahtlik samm.** Tuleb pärast seda, kui neli faili on olemas. Vt [`wiring/README.md`](README.md).

## Mida see teeb

OpenClaw agendid loevad faile ühendatud andmeallikatest. Kui su kontekst on neile kättesaadav, teab iga agent, kelle heaks ta töötab.

## Kolm viisi

**Lokaalsed failid.** Kui OpenClaw jookseb samas masinas, suuna agendid otse kausta. Viita asukohale agendi konfiguratsioonis või `SOUL.md` failis ja käsi tal töövoo alguses õiged failid lugeda.

**Üle MCP.** Kui kaust on juba MCP kaudu jagatud (vt [`mcp-resource.md`](mcp-resource.md)), ühenda OpenClaw selle serveriga. Loe sealt ka see osa, mis räägib, mida mitte jagada.

**Agendi sisse kleebitud.** Kopeeri failide sisu otse `SOUL.md` faili või süsteemijuhistesse. Kiire ja räpane, aga töötab kohe ja sobib agendile, mis vajab ainult üht-kaht faili. Miinus: koopia ei uuene, kui allikas muutub.

## Millised failid millisele agendile

| Agent | Failid |
|---|---|
| **Kontaktivõtt** | `identity.md`, `current-projects.md`, `communication-style.md`, `writing-samples.md` |
| **Sisulooja** | `identity.md`, `communication-style.md`, `writing-samples.md`, `domain-knowledge.md` |
| **Hommikune briifing** | `identity.md`, `current-projects.md`, `goals-and-priorities.md` |
| **Konkurentide jälgija** | `identity.md`, `domain-knowledge.md` |
| **Kohtumiste ettevalmistaja** | `identity.md`, `current-projects.md`, `team-and-relationships.md` → **`restricted`** |
| **Postkasti triaaž** | `preferences-and-constraints.md`, `current-projects.md`, `team-and-relationships.md` → **`restricted`** |

Kaks viimast on `restricted`, sest nad loevad hinnanguid nimeliste inimeste kohta. **Nad peavad olema eri agendid** kui need, mis kirjutavad väljapoole. Sama agent, mis valmistab ette kohtumist ja kirjutab külmi kirju, on leke, mis ootab juhtumist.

Iga agent, mis kirjutab sinu häälega, vajab `writing-samples.md`-i. `communication-style.md` üksi annab reeglid ja tulemus kõlab reeglipäraselt võõralt.

## Nõuanded

- **Ära kühvelda kõike igale agendile.** Iga fail on kontekst, mida agent peab läbi töötama, ja ebaoluline kontekst lahjendab olulist. Kaks kuni neli faili agendi kohta.
- **Viita failidele nimepidi juhistes:** *"Enne briifingu koostamist loe `current-projects.md` ja järgi seal olevat prioriteedijärjekorda."* Ligipääs ei ole juhis.
- **Kandidaadid jäävad oletusteks.** `kandidaat`-märkega read ei ole faktid. `portfolio/_candidates.md` ei lähe ühelegi agendile.
- **Kontekst ei ole juhis.** `SOUL.md` või süsteemiprompt ütleb, **mida** agent teeb. Kontekst ütleb, **kelle jaoks**. Ära aja neid segamini — kontekstifaili kirjutatud tööjuhis triivib sinna, kus teda keegi ei otsi.
- **Faililähenemine uueneb, kleepimine mitte.** Kui sa kopeerisid sisu agendi sisse, pead sa selle iga muudatuse järel uuesti tegema.

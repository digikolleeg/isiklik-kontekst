# Kuidas ühendada: Ühenda oma portfoolio OpenClaw agentidega

## Mida see teeb

OpenClaw agendid suudavad lugeda faile ühendatud andmeallikatest. Kui sa ühendad oma portfoolio OpenClaw'ga, saab iga sinu ehitatud agent ligipääsu sinu isiklikule kontekstile — sinu rollile, sinu projektidele, sinu suhtlusstiilile — ja suudab toota paremat, isikupärasemat tulemust.

## Kuidas see töötab

OpenClaw agendid pääsevad välistele andmetele ligi läbi oskuste (skills) ja ühendatud andmeallikate. Sa saad teha oma portfooliofailid kättesaadavaks andmeallikana, kust iga agent lugeda saab.

**Valik 1: Lokaalsed failid**

Kui su OpenClaw jookseb lokaalselt ja su portfoolio on lihtsalt kaust samas masinas, suuna oma agendid otse sinna kausta. Agendi konfiguratsioonis või SOUL.md failis viita portfoolio asukohale ja käsi agendil oma töövoo alguses lugeda sealt asjakohaseid faile.

**Valik 2: Üle MCP**

Kui oled oma portfoolio juba MCP ressursina välja jaganud (vaata `mcp-resource.md`), ühenda OpenClaw selle MCP serveriga. Su agendid saavad portfooliole ligi läbi MCP ühenduse.

**Valik 3: Agendi sisse ehitatud (embedded)**

Kiire ja räpane lahendus: kopeeri asjakohaste portfooliofailide sisu otse oma agendi SOUL.md faili või süsteemijuhistesse (system instructions). Vähem elegantne, aga töötab kohe. Sobib kõige paremini agentidele, mis vajavad ainult ühte-kahte failitäit konteksti.

## Millised failid millisele agendile

**Hommikuse briifingu agent:** `identity.md`, `current-projects.md`, `goals-and-priorities.md` — et ta teaks, mida briifingus esikohale seada.

**Koosolekuks ettevalmistav agent:** `team-and-relationships.md`, `current-projects.md` — et ta teaks, kellega sa kohtud ja mille kallal te koos töötate.

**Konkurentide monitoorija agent:** `identity.md`, `domain-knowledge.md` — et ta tunneks sinu valdkonna konteksti ja teaks, millele punast lippu lehvitada.

**Sisulooja agent:** `communication-style.md`, `domain-knowledge.md` — et ta kirjutaks sinu häälega ja sinu teadmiste tasemel.

**Postkasti triaaži agent:** `preferences-and-constraints.md`, `current-projects.md`, `team-and-relationships.md` — et ta teaks, mis põleb, mis on asjakohane ja millised inimesed loevad.

## Nõuanded

- Ära kühvelda kõiki kümmet faili igale agendile sisse. Iga fail on lisakontekst, mida agent peab läbi seedima, ja kõik sellest ei ole asjakohane. Ole valiv.
- Viita failidele nimepidi oma agendi juhistes: "Enne briifingu koostamist loe faili `current-projects.md`, et teada mu aktiivseid töövoogusid (workstreams), ja prioriseeri vastavalt."
- Kui sa uuendad oma portfooliofaile, saavad kõik neid lugevad agendid automaatselt värske konteksti (kui kasutad faili- või MCP-lähenemist, mitte agendi sisse kopeerimist).
- Portfoolio on kontekst, mitte juhised (instructions). Agendi SOUL.md või system prompt määrab endiselt, mida agent teeb. Portfoolio lihtsalt ütleb, kellele ta seda teeb.

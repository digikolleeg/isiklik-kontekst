# Kuidas ühendada: Tee oma portfooliost MCP ressurss

## Mida see teeb

MCP (Model Context Protocol) lubab AI tööriistadel ligi pääseda välistele andmeallikatele. Kui sa teed oma kontekstiportfooliost MCP ressursi, saab iga MCP-toega tööriist sinu faile käigu pealt (on demand) lugeda — agent ise tõmbab seda, mida tal vaja on, selle asemel, et sina peaksid otsustama, mida talle sisse kleepida.

See on kõige võimsam ühendamise (wiring) valik, sest see teeb sinu portfoolio automaatselt kättesaadavaks igale agendile, mis MCP-d toetab, ilma et sa peaksid ise midagi copy-paste'ima.

## Kuidas see töötab

Sinu portfoolio on lihtsalt kaustatäis markdowni faile. MCP server serveerib seda kausta kui ressurssi. Iga MCP klient (Claude Desktop, Claude Code, OpenClaw jne) ühendub serveriga ja saab lugeda mis tahes faili sinu portfooliost.

## Baasseadistus

**Valik 1: Lokaalne MCP server (failisüsteem)**

Kui sinu portfoolio elab su isiklikus arvutis, kasuta MCP failisüsteemi (filesystem) serverit, et see kaust välja jagada.

1. Hoia oma portfooliofaile kindlas kaustas (nt `~/context-portfolio/`).
2. Konfigureeri oma MCP klient nii, et see ühenduks failisüsteemi serveriga, mis näitab otse sinna kausta.
3. Iga ühendatud AI-tööriist suudab nüüd su portfooliofaile lugeda.

Täpne seadistus sõltub sinu MCP kliendist. Vaata oma tööriista dokumentatsioonist, kuidas lisada MCP failisüsteemi ressurssi.

**Valik 2: Kaug-MCP server (remote)**

Kui tahad, et su portfoolio oleks kättesaadav mitmest seadmest või kaug-agentidele (remote agents), pead sa seda serveerima kuskilt mujalt — pilveserverist, üle MCP jagatud GitHubi repost või enda kirjutatud custom MCP serverist.

See on juba keerulisem seadistus. Kui ehitad Claude Code'iga, võid tal paluda aidata sul ehitada lihtne MCP server, mis sinu portfooliofaile serveerib.

## Nõuanded

- Kui sa alles proovid asja, alusta failisüsteemi lähenemisega. Serverisse saad alati hiljem kolida.
- Sa ei pea välja jagama kõiki kümmet faili. Alusta kolmega: identity, role ja current projects — need katavad suurema osa vajadustest.
- Kui sa uuendad faile oma kaustas, uueneb ka MCP ressurss automaatselt. Mingit uuesti deploy'mist pole vaja.
- Kui sa serveerid faile remote serverist, mõtle ligipääsukontrollile. Sinu portfoolio sisaldab isiklikku ja tööalast infot, mida sa tõenäoliselt ei taha kogu maailmale avalikult serveerida.

## Mida järgmiseks ehitada

Kui su portfoolio on läbi MCP kättesaadav, on loogiline järgmine samm hakata ehitama agente, mis loevad oma töövoo alguses spetsiifilisi faile. Koosolekuteks valmistuv agent loeb faile `team-and-relationships.md` ja `current-projects.md`. Kirjutamisassistent loeb faili `communication-style.md`. Planeerimisagent loeb faili `goals-and-priorities.md`. Portfooliost saab see kontekstikiht, millest iga agent asju ammutab.

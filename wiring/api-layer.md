# Kuidas ühendada: Ehita API kiht

## Mis see on

Kõige arenenum ühendamise (wiring) valik. Sa ehitad lihtsa API, mis serveerib su portfoolio faile, nii et iga agent või rakendus saab sinu konteksti pärida otse koodist. See on mõeldud inimestele, kes ehitavad rätsepatööna valminud agente või rakendusi, millel on vaja konteksti käigu pealt (on demand) tõmmata.

## Millal sul seda vaja läheb

Enamikul inimestel polegi vaja. Kui kasutad Claude Projects'it, MCP-d või süsteemiprompti süstimist (system prompt injection), siis need lähenemised on lihtsamad ja katavad suurema osa kasutusjuhtudest.

Ehita API kiht siis, kui:

- Sul on mitu rätsepatööna valminud agenti (mitte lihtsalt valmis tööriistad karbist), mis kõik vajavad sinu konteksti.
- Sa tahad serveerida erinevatele agentidele failidest erinevaid alamhulki, vastavalt sellele, mida nad küsivad.
- Sa ehitad agente teistele inimestele ja vajad skaleeritavat viisi isikliku konteksti serveerimiseks.
- Sa tahad, et su portfoolio oleks päritav (queryable) — mitte lihtsalt "anna mulle kogu fail", vaid "mis on selle inimese praegused projektid?".

## Arhitektuur

Kõige lihtsam versioon:

1. Salvesta oma portfooliofailid andmebaasi või failisüsteemi.
2. Ehita kergekaaluline API, kus igal failil on oma endpoint (või üks endpoint, mis võtab faili nime parameetrina).
3. Lisa baastasemel autentimine, et su failid poleks avalikult kättesaadavad.
4. Su agendid kutsuvad API-t oma töövoo alguses, et tõmmata neile vajalik kontekst.

```
GET /api/portfolio/identity
GET /api/portfolio/current-projects
GET /api/portfolio/communication-style
GET /api/portfolio?files=identity,current-projects,team
```

## Keerulisem versioon

Kui tahad, et su portfoolio oleks päritav, mitte ei jagaks lihtsalt toorfaile:

1. Salvesta portfoolio sisu struktureeritud andmebaasi (mitte lihtsalt lamedatesse failidesse).
2. Lisa loomuliku keele päringukiht (natural language query layer) — küsimus "mis on mu aktiivsed projektid?" toob tagasi vastava lõigu current-projects failist, mitte kogu faili.
3. Lisa uuendamise (update) API, et su agendid saaksid portfooliosse ka tagasi kirjutada (agent, mis märkab, et sa alustasid uut projekti, saab selle ise current-projects faili lisada).

See hakkab juba meenutama isiklikku teadmusgraafi (personal knowledge graph). See on võimas asi, aga see on juba päris tarkvaraarenduse projekt. Ära ehita seda enne, kui lihtsamatest lähenemistest enam ei piisa.

## Märkused teostuse kohta

- Kui kasutad Supabase'i, salvesta iga faili sisu tabelisse, kus on `user_id`, `file_name`, `content` ja `updated_at`. Lihtne, päritav (queryable) ja sa saad reatasemel turvalisuse (row-level security) tasuta kaasa.
- Kui sa ehitad asju Claude Code'iga, siis võid tal paluda see API sulle valmis ehitada. Anna talle see dokument ja su portfooliofailid ette ja ütle: "Ehita mulle lihtne API, mis neid faile serveerib."
- Autentimine on oluline. Sinu portfoolio sisaldab isiklikku ja tööalast infot. Miinimumina kasuta API võtme autentimist. Kui lähed toodangusse (production), kasuta OAuth-i või JWT-d.
- Versiooni oma faile. Kui portfoolio sisu muutub, hoia eelmine versioon alles. Nii saad jälgida, kuidas sinu kontekst ajas areneb, ja teha roll-back'i, kui mingi uuendus läks puusse.

## Nõuanded

- Alusta lamedate failide serveerimisega (valik 1) ja lisa päringute võimekus ainult siis, kui sul tekib selleks reaalne vajadus (use case).
- Vaikimisi peaks API tagastama toore markdowni. Las agent, kes seda tarbib, otsustab, kuidas seda parsida ja kasutada.
- Lisa `GET /api/portfolio/summary` endpoint, mis tagastab ainult `identity.md` faili — minimaalne töötav kontekst. Agendid, mis vajavad kiiret, kerget konteksti, saavad lüüa seda endpointi, selle asemel et mitu faili alla sikutada.
- Kui sa ehitad agente, mis kirjutavad portfooliosse asju tagasi, ole konfliktide osas ettevaatlik. Kaks agenti, mis uuendavad `current-projects.md` faili samal ajal, võivad viia andmekaoni. Kasuta ajatempleid (timestamps) ja konfliktide tuvastamist.

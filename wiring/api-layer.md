# Ühendamine: API kiht

> **Kõige keerulisem valik, ja enamikul pole teda vaja.** Claude Projects, MCP või süsteemiprompti kleepimine katavad peaaegu kõik kasutusjuhud lihtsamalt. Vt [`wiring/README.md`](README.md).

## Millal seda ehitada

- sul on mitu enda kirjutatud agenti, mis kõik vajavad sama konteksti
- sa tahad serveerida eri agentidele eri alamhulki
- sa ehitad agente teistele inimestele ja vajad skaleeritavat viisi
- sa tahad konteksti **pärida** ("mis on tema praegused projektid?"), mitte lihtsalt tervet faili tõmmata

Kui ükski rida ei kirjelda sinu olukorda, ära ehita.

## Lihtne versioon

1. Hoia kontekstifaile failisüsteemis või andmebaasis.
2. Ehita kerge API: üks endpoint faili kohta, või üks endpoint failinime parameetriga.
3. Lisa autentimine.
4. Agendid pärivad konteksti oma töövoo alguses.

```
GET /api/context/identity
GET /api/context/current-projects
GET /api/context?files=identity,current-projects,writing-samples
```

## Kolm asja, mis API kihis on lihtsam kui mujal

API on ainus koht, kus staatuste ja tundlikkuse reeglid saab **jõustada**, mitte ainult dokumenteerida.

**1. Filtreeri kandidaadid välja.** Iga väiterida kannab märget `<!-- claim: status=... -->`. Vaikimisi ei tohiks vastus sisaldada `kandidaat`-ridu. Tee sellest päringuparameeter, mitte tarbija otsus:

```
GET /api/context/communication-style              → kinnitatud + toetatud
GET /api/context/communication-style?include=all  → kõik, koos märgetega
```

**2. Jõusta tundlikkust.** Iga faili päises on `sensitivity: exportable | restricted`. `restricted` fail ei tohi tulla ilma eraldi õiguseta. `team-and-relationships.md` on ainus, mis on vaikimisi `restricted` — ja just tema on see, mille tahtmatu väljastamine on pöördumatu.

**3. Ära ehita automaatset pakikokkupanijat, enne kui üks pakk töötab käsitsi.** `portfolio/bundles/` all olevad pakid on projektsioonid: allikate loend päises, kohatäitjad kehas. Neid pannakse täna kokku käsitsi. Kokkupanija on tehtav — loe päisest `sources`, tõmba failid, jäta kandidaadid välja, keeldu `restricted` failist — aga ta on tarkvara, mida keegi peab hooldama. Kontrolli enne käsitsi, kas pakk üldse annab paremat tulemust.

## Keerulisem versioon

Struktureeritud andmebaas ja loomuliku keele päringukiht, kus "mis on mu aktiivsed projektid?" toob tagasi õige sektsiooni, mitte terve faili. Sektsioonid on failides juba märgistatud — `<!-- section: <id> | owner: <moodul> -->` — nii et sektsioonitasandi päring on parsimise, mitte äraarvamise küsimus.

Kirjutamise API (agent lisab ise uue projekti) tundub loogilise järgmise sammuna. Ole ettevaatlik: kaks agenti, mis uuendavad sama faili korraga, kaotavad andmeid. Ja agendi kirjutatud väide on definitsiooni järgi `kandidaat`, mitte `kinnitatud` — kirjutamise API peab seda jõustama, muidu laguneb kogu tõendisüsteem esimese automaatse kirjutuse peale.

## Märkused teostuse kohta

- **Autentimine ei ole valikuline.** Kontekst on isiklik ja tööalane. Miinimum on API võti; toodangus OAuth või JWT.
- **Tagasta toores markdown.** Las tarbija otsustab, kuidas parsida. Frontmatter tuleb kaasa — seal on `sensitivity` ja `review_after`, mida tarbija vajab.
- **Versiooni faile.** Hoia eelmine versioon alles, et näha, kuidas kontekst areneb, ja saada roll-back, kui uuendus läks valesti.
- **Lisa `GET /api/context/summary`**, mis tagastab ainult `identity.md`. Minimaalne töötav kontekst agendile, mis vajab kerget vastust.
- Supabase'iga: tabel `user_id`, `file_name`, `content`, `sensitivity`, `updated_at`, `review_after`. Jõusta igal tabelil reatasandi turve; nii muutub `sensitivity` päritavaks väljaks, mitte kommentaariks.

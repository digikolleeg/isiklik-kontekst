# Ühendamine: kontekst MCP ressursina

> **Vabatahtlik transport, mitte eeltöö.** MCP ei ole selle süsteemi eeldus ega põhitee. Ei intervjuu ega Skill vaja teda. Ta lahendab ühe kitsa probleemi: sul on mitu tööriista ja sa ei taha sama sisu mitmesse kohta kleepida.
>
> Kui sa alles alustad, jäta vahele. [`wiring/README.md`](README.md) loetleb lihtsamad teed.

## Mida see teeb

MCP (Model Context Protocol) lubab AI tööriistadel lugeda väliseid andmeallikaid. Kui su kontekstikaust on MCP kaudu kättesaadav, loeb agent sealt vajaliku ise, selle asemel et sina otsustaksid, mida sisse kleepida.

Selle eeliseks on üks allikas: sa uuendad faili kaustas ja iga ühendatud tööriist näeb uut versiooni ilma uuesti üleslaadimiseta.

**Pakendatud MCP serverit selles repos ei ole.** Sa kasutad üldist failisüsteemi-serverit või kirjutad enda oma.

## Seadistus

**Lokaalne failisüsteemi server.** Hoia kontekstifaile kindlas kaustas (nt `~/isiklik-kontekst/portfolio/`) ja seadista oma MCP klient nii, et ta seda kausta näeb. Täpsed sammud sõltuvad kliendist — vaata oma tööriista dokumentatsiooni.

**Kaugserver.** Kui sa tahad ligipääsu mitmest seadmest, pead faile serveerima mujalt: pilveserverist või enda kirjutatud MCP serverist. See on tarkvaraprojekt, mitte seadistus. Ära alusta siit.

## Mida sa välja jagad — loe see läbi

Kaust ei ole komplekt. **Kausta jagamine jagab kõike, mis seal on**, ja kaks asja seal ei tohi liikuda:

| Fail | Miks mitte |
|---|---|
| `team-and-relationships.md` | `restricted` — hinnangud nimeliste kolmandate isikute kohta |
| `_candidates.md` | kinnitamata väited, mis ootavad teist sõltumatut tõendit |

Kui sa jagad kogu kausta, saab iga ühendatud agent mõlemad kätte, sealhulgas see, mis kirjutab väljapoole. Kaks lahendust:

1. **Hoia jagatavaid faile eraldi kaustas** ja suuna server sinna. Lihtsaim ja kõige raskemini eksitav.
2. **Piira serveri lugemisõigust failinimede kaupa**, kui su klient seda toetab.

Kaugserveri puhul lisandub ligipääsukontroll. Kontekstifailid on isiklikud ja tööalased — need ei kuulu avalikku internetti.

## Nõuanded

- Alusta failisüsteemist. Serverisse kolimine on alati hiljem võimalik.
- Ära jaga kõiki üksteist faili korraga. Alusta kiire intervjuu neljast: `identity.md`, `current-projects.md`, `communication-style.md`, `writing-samples.md`. Need katavad enamiku vajadustest.
- Kirjuta agendi juhisesse, **millist faili millal lugeda**. MCP annab ligipääsu, mitte otsustusvõimet. Ilma juhiseta loeb agent kas liiga vähe või kõike.
- `kandidaat`-märkega read jäävad oletusteks ka MCP kaudu loetuna. Ligipääs ei ülenda väidet.

## Mida edasi ehitada

Kui kontekst on MCP kaudu käes, on järgmine samm agendid, mis loevad oma töövoo alguses nimeliselt õigeid faile. Kirjutamisassistent loeb `communication-style.md` ja `writing-samples.md`. Planeerimisagent loeb `goals-and-priorities.md` ja `current-projects.md`. Kohtumiste ettevalmistaja loeb `team-and-relationships.md` — ja on seetõttu eraldi agent, mitte sama, mis kirjutab kliendile.

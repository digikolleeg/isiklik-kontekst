# Ühendamine: süsteemiprompti mustrid

> **Vabatahtlik samm.** Tuleb pärast seda, kui neli faili on olemas. Vt [`wiring/README.md`](README.md).

## Mis see on

Kopeeri-kleebi mustrid konteksti süstimiseks suvalise AI tööriista süsteemiprompti või kohandatud juhistesse. Kõige lihtsam ja universaalsem ühendus — töötab Claude'i, ChatGPT, Gemini ja kõigega, kus saab süsteemiprompti seadistada.

## Baasmuster

```
<user_context>
[kleebi identity.md sisu siia]
[kleebi ülejäänud asjakohased failid siia]
</user_context>

Sul on eespool kontekst kasutaja kohta. Kasuta seda vastuste kujundamisel — tema roll, projektid, kirjutamisstiil, eelistused. Ära viita sellele kontekstile otse, kui sinult ei küsita.

Ära väida ühtegi fakti, numbrit ega nime, mida kontekstis ei ole.
```

Viimane rida ei ole kaunistus. Ilma selleta täidab mudel lüngad ise ja teeb seda enesekindlalt.

## Mustrid kasutusjuhtude kaupa

### Kontaktivõtt ja müük

```
<user_context>
[identity.md]
[current-projects.md]
[communication-style.md]
[writing-samples.md]
</user_context>

Sa koostad sõnumeid, mis lähevad päris inimestele. Järgi communication-style reegleid ja matki writing-samples mustreid: lause pikkust, kuidas algab, kuidas lõpeb, struktuuri. Ära kopeeri ühtegi näidet sõnasõnalt.

current-projects sektsioon "Mida ei tohi väita" on kõva keelunimekiri. Mustand, mis rikub ühtki selle rida, on ebaõnnestunud mustand. Ära mõtle välja ühiseid tuttavaid, varasemaid kohtumisi ega jagatud kogemusi.
```

Need neli faili on täpselt kiire intervjuu väljund.

### Kirjutamisassistent

```
<user_context>
[identity.md]
[communication-style.md]
[writing-samples.md]
[domain-knowledge.md]
</user_context>

Sa toodad sisu kasutaja nimel. Väldi iga sõna ja mustrit, mille ta on kirja pannud sektsiooni "Mida ma väldin" — need on reeglid, mitte soovitused. Matki writing-samples näiteid, ära kopeeri neid.

Kirjuta tema valdkonna tasemel: kasuta termineid ilma neid defineerimata, välja arvatud siis, kui auditoorium on selgelt võhiklik. Kui pead fakti või numbri ära arvama, ütle seda otse.
```

### Strateegiline nõuandja

```
<user_context>
[identity.md]
[goals-and-priorities.md]
[current-projects.md]
[decision-log.md]
</user_context>

Sa oled mõttepartner. Kasuta goals-and-priorities sektsiooni, et mõista, mida kasutaja optimeerib, ja sektsiooni "Mis EI OLE praegu prioriteet", et mitte pakkuda asju, mille ta on teadlikult ootele pannud.

decision-log on tõendikorpus: päris otsused ja nende käik. Kasuta seda, et sobitada oma arutluskäik tema omaga. Ole otsekohene ja lühike.
```

### Kohtumisteks ettevalmistus — `restricted`

```
<user_context>
[identity.md]
[current-projects.md]
[team-and-relationships.md]
</user_context>

Sa valmistad ette kohtumisi. team-and-relationships sektsioon "Kontekst agentidele" on agendile reeglid, mitte taust: kui rida ütleb "ei loe pikki kirju", on pikk kokkuvõte ebaõnnestunud töö.
```

**See prompt sisaldab kolmandate isikute andmeid.** Ta ei kuulu tööriista, mis kirjutab väljapoole, ega jagatud agenti. Hoia teda eraldi sellest promptist, millega sa kontaktivõttu teed.

## Nõuanded

- **Vali 2–4 faili kasutusjuhu kohta.** Ebaoluline kontekst lahjendab olulist. Kõigi failide kleepimine ühte prompti teeb tulemuse halvemaks, mitte paremaks.
- **Kui tähemärgipiirang on kitsas**, kasuta `identity.md` ja `communication-style.md` ning lisa üks lühike päris kirjutamisnäide. Näide üksi teeb häälele rohkem kui kolm rida stiilireegleid.
- **Juhiste lõik konteksti järel on sama tähtis kui kontekst.** Ütle otse, kuidas konteksti kasutada. Ära eelda, et mudel arvab ära.
- **Jäta `kandidaat`-märkega read välja.** Need on ühe vaatluse pealt tehtud oletused ja ootavad teist tõendit. `portfolio/_candidates.md` ei lähe promptidesse üldse.
- **Uuenda, kui failid muutuvad.** Aegunud kontekst süsteemipromptis on nähtamatu ja tõmbab väljundi vaikselt alla.

## Test

Palu midagi, millega mudel ilma kontekstita puusse paneks: kiri sinu stiilis, ettevalmistus konkreetse inimesega kohtumiseks. Võrdle sama päringuga tühjas vestluses. Kui vahet pole, ei ole viga ühenduses — failid on liiga üldsõnalised.

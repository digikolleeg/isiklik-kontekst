# Preferences and Constraints

## Mille jaoks see fail on

"Alati tee nii / ära kunagi tee nii" fail. Kõvad reeglid ja tugevad eelistused, mida iga sinu heaks töötav agent peaks austama ilma, et talle seda iga kord eraldi ütleksid. See katab kõike alates ajavööndi piirangutest ja vormistuse arvamustest kuni asjadeni, mida sa lausa vihkad. Kui on midagi, millega agent paneb sajaprotsendiliselt puusse, kui sa talle seda ette ei ütle, siis see käib siia.

---

## Intervjuu-protokoll

*Anna see fail tervikuna oma AI ehituspartnerile ja ütle "alustame sellega". Su ehituspartner peaks lugema allolevad juhised ja viima läbi intervjuu.*

**Juhised ehituspartnerile:** sa aitad kasutajal koostada tema preferences and constraints faili. See peaks tunduma nagu selge reeglistik, mitte mingi isiksuseprofiil. Nõua konkreetseid, rakendatavaid eelistusi — "ma vihkan koosolekuid enne kella kümmet" on kasulik; "ma hindan töö ja eraelu tasakaalu" on kasutu.

**Küsimused:**

1. Kas su ajas või kättesaadavuses on kõvasid piiranguid, mida iga agent peaks teadma? Ajavööndid, tunnid, mil sa ei tööta, päevad, mis on absoluutselt kinni?
2. Milles sa kompromisse ei tee — asjad, mida sa kategooriliselt nõuad selles osas, kuidas töö tehtud saab, kuidas väljundid on vormistatud või kuidas suhtlus käib?
3. Mida sa vihkad? Koosolekud, mis oleks võinud olla e-kirjad, mingi konkreetne žargoon, väljundi formaadid, mis sind ärritavad — kõik asjad, mille suhtes sul on tugev reaktsioon.
4. Kas sul on isiklikke piiranguid, mis mõjutavad su tööd — näiteks reisimise piirangud, pere graafikust tulenevad asjaolud, tervisemured ja kõik muu mida sa tahad, et agent arvesse võtaks? Jaga ainult seda, mida sa ise tahad jagada.
5. Kui AI sulle midagi toodab, siis millised on su vormistuse eelistused? Pikkus, struktuur, detailsusaste, toon?

**Millal piisab:** Pärast 4–5 küsimust.

**Pärast koostamist:** Näita mustandit. Küsi kasutajalt, kas on midagi puudu, mida ta avastaks end agentidele pidevalt meelde tuletamas. Need korduvad parandused ongi täpselt see kraam, mille jaoks see fail olemas on.

---

## Väljundi struktuur

```markdown
---
name: preferences-and-constraints
description: Kõvad reeglid, tugevad eelistused, piirangud, mida ei delegeeri
type: portfolio
updated: <YYYY-MM-DD>
tags: [portfolio]
---

# Eelistused ja piirangud

## Kõvad piirangud

[Piirid, kus kompromisse ei tehta — ajavööndid, kättesaadavuse aknad, planeerimise reeglid, asjad, mis on välistatud. Need on reeglid, mitte lihtsalt eelistused.]

## Tugevad eelistused

[Asjad, mida sa kindlalt nõuad, aga milles saaksid teoreetiliselt järele anda. Tööriistade valik, formaadid, protsessid, tööviisid, mille suhtes sul on väga selge arvamus.]

## Mida ma vihkan

[Konkreetsed asjad, mis käivad närvidele — koosolekute formaadid, suhtlusmustrid, kantseliit, AI väljundite maneerid. Värk, mis ajab harja punaseks.]

## Isiklikud piirangud

[Kõik sinu isikliku eluga seonduv, mis mõjutab su tööd ja mida agendid peaksid arvestama — pere graafik, tervisemured, asukoht, reisipiirangud. Ainult see, mida ise soovid jagada.]

## AI väljundi eelistused

[Kuidas sa tahad, et AI toodetud sisu oleks vormistatud ja esitatud. Pikkus, struktuur, detailsusaste, toon, vormistuse tavad.]
```

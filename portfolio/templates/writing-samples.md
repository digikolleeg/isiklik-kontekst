---
name: writing-samples
description: Tegelikud kirjutamise näited erinevatest kanalitest (e-mail, LinkedIn, blogi, Slack)
type: portfolio
updated: <YYYY-MM-DD>
tags: [portfolio]
---

# Kirjutamise näited

## Mille jaoks see fail on

Tegelikud kirjutamise näited kasutaja erinevatest kanalitest — e-mailid, LinkedIn-postitused, blogiartiklid, mitteformaalsed sõnumid. Erinevalt `communication-style.md`-st (mis kirjeldab **reegleid**), see fail sisaldab **tegevuslikku tõendusmaterjali**: päris laused, mille kasutaja ise on kirjutanud.

**Miks see vajalik on:** AI agendid suudavad reegleid järgida ("ei mingeid em-dash'e", "lühike ja konkreetne"), aga hääle päris matkimine eeldab näiteid, mille pealt mustreid (Few-Shot Prompting) pattern-match'ida. Reeglid ütlevad **mida vältida**; näited näitavad **mida teha**. Mõlemat on vaja.

---

## Intervjuu-protokoll

*Anna see fail tervikuna oma AI ehituspartnerile ja ütle "alustame sellega". Su ehituspartner peaks lugema allolevad juhised ja viima läbi intervjuu.*

**Juhised ehituspartnerile:** sa aitad kasutajal koostada tema writing-samples faili — täis-pikkuses kirjutamise näiteid, mida agendid kasutavad Few-Shot Prompting'ks.

**Eesmärk:** 2-4 näidet töötoa kontekstis, 4-8 näidet täielikus režiimis. Iga näide peab olema **täis-pikkuses**, mitte üks lause väljavõte.

**Küsimused:**

1. Kas sul on käes mõni päris **müügimeil**, mille sa hiljuti saatsid? Kleebi see siia täies pikkuses (saaja-andmed võid pseudonüümida).
2. Kas sul on mõni **LinkedIn-postitus**, mis sind hästi esindab — mitte poleeritud, vaid päris sinu hääl? Kleebi see siia.
3. Kas sul on mõni **mitteformaalne sõnum** (Slack, e-mail sõbrale, telegrammi sõnum), kus sa räägid nii, nagu tavaliselt elus räägid?
4. *(Täielik režiim, valikuline):* mõni **blogi-artikkel**, **kõne** või **pikem mõtisklus**, mille sa kirjutasid? Vähemalt esimene lõik.

**Millal piisab:** pärast 2 näidet töötoas, 4 näidet täielikus režiimis. Iga lisanäide tõstab tulemuse kvaliteeti, aga esimesed 2-4 on kõige olulisemad.

**Olulised juhised:**
- **Ära redigeeri näiteid.** Nad peavad jääma nii, nagu kasutaja need kirjutas. Isegi kui näed kirjavigu või jutuks-stiili kohti, jäta neid puutumata. Just need on hääl, mida tahame matkida.
- **Keeldu poleeritud turundusmaterjalist.** Kui kasutaja pakub firma-veebilehe "About"-teksti või sarnast pressimaterjali, ütle: "see on poleeritud, mitte sinu päris hääl — kas sul on Slack-sõnumeid või sõbra-meile?"
- **Pseudonümiseeri tundlikud andmed.** Kliendi nimed, telefoninumbrid, hindade-detailid — märgi need ümber (`[KLIENT]`, `[KLIENDI E-MAIL]`, `[XXXX €]`). Aga jäta hääl puutumata.

**Pärast koostamist:** näita mustandit ja palu kasutajal välja tuua kõik, mis on liiga ebatüüpiline või ei kõla ta enda häälena.

---

## Väljundi struktuur

```markdown
---
name: writing-samples
description: Tegelikud kirjutamise näited erinevatest kanalitest (e-mail, LinkedIn, blogi, Slack)
type: portfolio
updated: <YYYY-MM-DD>
tags: [portfolio]
---

# Kirjutamise näited

Tegevuslik tõendusmaterjal kasutaja häälest. Mõeldud Few-Shot Prompting'iks — agendid loevad need näited läbi ja matkivad sealset rütmi, sõnavara, struktuuri.

**Tähtis agentidele:** ära kunagi kopeeri näiteid sõnasõnalt. Pattern-match. Loe välja: lause-pikkus, kuidas algatab, kuidas lõpetab, sõnavara, formaalsuse aste, struktuur (lõigud, bulletid, koodi-stiil).

---

## E-mailid

### [Kontekst, näiteks: müügimeil potentsiaalsele kliendile]

```
[Täis-pikkuses e-maili tekst, sõnasõnalt. Saaja-andmed pseudonüümitud.]
```

### [Kontekst, näiteks: vastus kliendi küsimusele]

```
[Täis-pikkuses tekst.]
```

---

## LinkedIn

### [Postituse teema või kuupäev]

```
[Täis-pikkuses postituse tekst.]
```

---

## Mitteformaalne (Slack / sõbra-meil / SMS)

### [Kontekst]

```
[Täis-pikkuses sõnum.]
```

---

## Blogi / pikemad tekstid (valikuline, täielik režiim)

### [Pealkiri]

```
[Esimene lõik või lühike väljavõte, kus hääl tuleb selgelt välja.]
```

---

## Mida agendid peaksid neist mustritest välja lugema

*(Valikuline jaotis. Kui kasutaja tahab, võib siia panna lühikese loendi mustritest, mida ta märgib oma häälel — näiteks "alustan tihti küsimusega", "kasutan numbreid lubaduste asemel", "lõpetan konkreetse sammuga". See aitab agendil pattern-match'i kiirendada.)*
```

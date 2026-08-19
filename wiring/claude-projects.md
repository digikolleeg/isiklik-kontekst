# Ühendamine: Claude Projects

> **Vabatahtlik samm.** Tuleb pärast seda, kui neli faili on olemas. Vt [`wiring/README.md`](README.md).

## Mida see teeb

Claude Projects lubab manustada faile, mis püsivad üle kõigi selle projekti vestluste. Kui sa lisad oma kontekstifailid projekti, algab iga vestlus nii, et Claude teab juba, kes sa oled ja mille kallal sa töötad.

Lihtsaim püsiv ühendus, mis üldse olemas on: ei mingit serverit, ei konfiguratsiooni. Lae failid üles.

## Kuidas

1. Loo uus Claude Project või ava olemasolev.
2. Lisa kontekstifailid projekti teadmusbaasi.
3. Kirjuta projekti juhistesse, kuidas Claude neid kasutama peab (allpool).

## Milliseid faile lisada

Ära lisa kõiki. Vali projekti eesmärgi järgi.

| Projekt | Failid |
|---|---|
| **Kontaktivõtt ja müük** | `identity.md`, `current-projects.md`, `communication-style.md`, `writing-samples.md` |
| **Sisukirjutamine** | `identity.md`, `communication-style.md`, `writing-samples.md`, `domain-knowledge.md` |
| **Üldine tööassistent** | `identity.md`, `role-and-responsibilities.md`, `current-projects.md`, `preferences-and-constraints.md` |
| **Strateegiline nõuandja** | `identity.md`, `goals-and-priorities.md`, `current-projects.md`, `decision-log.md` |
| **Kohtumisteks ettevalmistus** | `identity.md`, `current-projects.md`, `team-and-relationships.md` → **kogu projekt on siis `restricted`** |

Esimene rida on täpselt kiire intervjuu väljund. Kui sa tegid ainult kiire intervjuu, on sul juba täisvarustuses müügiprojekt.

Iga kirjutav projekt vajab `writing-samples.md`-i. Ilma näideteta järgib Claude reegleid ja kõlab ikkagi võõralt — reeglid ütlevad, mida vältida, näited näitavad, mida teha.

## Projekti juhised

Kleebi custom instructions lahtrisse midagi sellist:

```
Sul on ligipääs minu kontekstifailidele. Kasuta neid vastuste kujundamisel, aga ära viita neile otse, kui ma ei palu.

Enne kui kirjutad midagi minu nimel, loe communication-style.md ja writing-samples.md. Järgi reegleid ja matki näidete mustreid — lause pikkust, alustamist, struktuuri. Ära kopeeri näidet sõnasõnalt.

Ära väida ühtegi fakti, numbrit ega kliendinime, mida failides ei ole. Kui current-projects.md sisaldab sektsiooni "Mida ei tohi väita", on need read kõvad keelud.
```

## Piirangud

- **Failid on staatilised koopiad.** Kui portfooliofail muutub, laed sa selle igasse projekti eraldi uuesti üles. Aegunud kontekst on halvem kui puuduv: puuduva puhul Claude küsib, aegunu puhul ta ei küsi.
- **Iga projekt on eraldi.** Viis projekti tähendab viit üleslaadimist.
- **Kandidaat-väited ei kuulu siia.** `portfolio/_candidates.md` ei lähe ühessegi projekti. Kui mõni fail sisaldab `kandidaat`-märkega ridu, on need agendi jaoks oletused; ta ei tohi neile kindla väitena toetuda.
- **`team-and-relationships.md` teeb projekti `restricted`-iks.** Hoia kohtumiste ettevalmistus eraldi projektis, mitte samas, kus sa väljaminevaid sõnumeid kirjutad.

## Test

Küsi projektis: *"Koosta kahelauseline sissejuhatus uuele potentsiaalsele kliendile minu häälega."*

Kui see kõlab sinuna ilma parandusteta, ühendus töötab. Kui ei, ei ole viga ühenduses — vaata `communication-style.md` ja `writing-samples.md` üle. [RUBRIC.md](../RUBRIC.md) värav 1 ütleb, kust otsida.

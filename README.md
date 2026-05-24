# Isiklik kontekst

Kaks kihti. Üks selle kohta, kes sa oled. Teine selle kohta, mida sa tead.

---

## Probleem

Iga AI tööriist, mida sa kasutad, vajab kahte asja, et olla päriselt kasulik: ta peab teadma, *kes sa oled* (su roll, eesmärgid, eelistused, piirangud) ja ta peab teadma, *mida sa tead* (su kogutud uurimismaterjal, koosolekumärkmed, valdkonna teadmised). Enamus inimesi seletab esimest iga vestlusega nullist uuesti ja kaotab teise täielikult, kui vestlus suletakse.

See süsteem lahendab mõlemad.

---

## Kiht 1: Portfoolio — kes sa oled

Kümme markdown-faili, mis koos moodustavad kaasaskantava, AI-loetava käsiraamatu sinuga töötamiseks. Pole CV. Pole profiil. Kontekst.

| Fail | Mida talletab |
|------|---------------|
| `identity.md` | Kes sa oled — see fail, mida agent loeb, kui võib lugeda ainult ühte |
| `role-and-responsibilities.md` | Mis su nädalad päriselt välja näevad, mitte mis su ametinimetus ütleb |
| `current-projects.md` | Käimasolevad tööd, seis, prioriteet, mida lõpetatud tähendab |
| `team-and-relationships.md` | Olulised inimesed, kuidas sa nendega suhtled, mida nad sinult vajavad |
| `tools-and-systems.md` | Su tööriistakomplekt, su seadistus, mis millega ühenduses on |
| `communication-style.md` | Kuidas sa kirjutad, kuidas tahad, et sinu nimel kirjutatakse |
| `goals-and-priorities.md` | Mille poole sa püüdled ja mida sa teadlikult ignoreerid |
| `preferences-and-constraints.md` | Kõvad reeglid, tugevad arvamused, asjad, mida iga agent peab arvestama |
| `domain-knowledge.md` | Mida sa tead, mida üldine AI ei tea |
| `decision-log.md` | Kuidas sa otsuseid teed, päriste näidetega |

**Uuendamise sagedus:** kord kvartalis või kui midagi olulist muutub.
**Kuidas seda ehitada:** vaata `portfolio/` — seal on šabloonid, näited ja kogu intervjuu-protokoll.

---

## Kiht 2: Wiki — mida sa tead

Kumuleeruv teadmiste baas, mida hoiab täielikult LLM. Sa paned tooresallikad (artiklid, transkriptsioonid, koosolekumärkmed, PDF-id) `raw/` kausta. LLM loeb need, loob struktureeritud wiki-lehed `wiki/` kausta ja ehitab automaatselt mõistete vahel seosed. Teadmine kasvab. Ristviited on juba olemas, kui sul neid vaja läheb. Midagi ei tuletata iga päringu peale nullist uuesti.

```
raw/    ← pane allikad siia (muutmatud — LLM loeb, ei kirjuta kunagi)
wiki/   ← LLM-i loodud lehed (mõisted, teemad, sünteesid)
index.md  ← kõigi wiki-lehtede kataloog, uuendatud iga sissekande peale
log.md    ← jätkuv kirje sissekannetest, päringutest ja kontrollkäikudest
```

**Uuendamise sagedus:** pidev — iga kord kui sul on allikas, mida tasub säilitada.
**Kuidas see töötab:** vaata `CLAUDE.md` — sealt leiad sissekande, päringu ja kontrollkäigu töövood.

---

## Kuidas need kihid omavahel ühenduvad

Portfoolio on identiteedi kiht. Wiki on teadmiste kiht. Koos annavad nad igale AI tööriistale täieliku konteksti: kellega ta töötab *ja* mida see inimene on kogunud.

Praktikas: LLM, kes wikit hooldab, juba teab sinu portfooliost, kelle jaoks ta seda ehitab — su valdkond, su eesmärgid, su kirjutamise stiil. Wiki "minu kohta" uurimine (päevikukanded, retrospektiivid, eesmärkide üle mõtisklemine) saab portfooliosse tagasi voolata, näiteks `current-projects.md` või `goals-and-priorities.md` faili. Need on eraldi süsteemid, kuid toidavad teineteist.

---

## Repo struktuur

```
/
├── README.md
├── GETTING-STARTED.md
├── CLAUDE.md               ← juhib mõlemat kihti (loe see)
├── index.md                ← wiki indeks (LLM-i hooldatud)
├── log.md                  ← wiki logi (LLM-i hooldatud)
├── raw/                    ← pane allikad siia
├── wiki/                   ← LLM-i loodud teadmiste baas
├── portfolio/
│   ├── templates/          ← kümme tühja šablooni koos intervjuu-protokollidega
│   ├── examples/           ← täidetud näited (teadmustöötaja, juht, ettevõtja)
│   └── interview-protocol/ ← intervjueerija-agendi täielik süsteemiprompt
└── wiring/                 ← juhendid mõlema kihi AI tööriistadega ühendamiseks
```

---

## Disainipõhimõtted

**Markdown ennekõike.** Iga AI süsteem maailmas oskab markdown'i lugeda. Pole andmebaase, pole embeddings-infrat, pole kinniseid formaate. Failid, mis on loetavad nii inimesele kui masinale.

**LLM kirjutab, inimene kureerib.** Wiki hooldamise koorem — ristviidete uuendamine, kokkuvõtete värskena hoidmine, vastuolude märkamine — on täielikult LLM-i töö. Sinu töö on allikate leidmine, suunamine ja heade küsimuste esitamine.

**Kaasaskantav igal pool.** Töötab Claude Code'iga, Claude Projects'iga, ChatGPT-ga, igasuguse tööriistaga, mis faile loeb. Ühegi tootja külge kinni jäänud.

**Modulaarne.** Portfoolio ja wiki on iseseisvad süsteemid. Kasuta ühte, kasuta mõlemaid, ühenda need. Vali, mis sulle sobib.

---

## Litsents

MIT.

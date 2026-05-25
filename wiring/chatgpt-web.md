# Kuidas ühendada: ChatGPT Web

Siin on kolm viisi, kuidas ChatGPT-le oma portfoolio ette sööta, lihtsamast keerulisemani. Vali see, mis sobib sellega, kuidas sa tegelikult ChatGPT-d kasutad.

## 1. Custom Instructions (tähemärgipiiranguga)

ChatGPT Custom Instructions (kohandatud juhised) püsivad aktiivsena üle kõigi vestluste — vahet pole, kas küsid koodi, kirjutad teksti, teed taustauuringut või midagi muud. Konks on selles: seal on tähemärgipiirang (umbes 1500 tähemärki kasti kohta), mis tähendab, et sa saad sinna mahutada ainult kõige kokkupakituma versiooni oma portfooliost.

**Mida sisse kopeerida:**

Lahtrisse "What would you like ChatGPT to know about you?" (Mida sa tahaksid, et ChatGPT sinu kohta teaks?) kopeeri kokkuvõte, mis sisaldab:

- Sinu nime, rolli, organisatsiooni (failist `identity.md`).
- "Mida ma teen" lõiku (failist `identity.md`).
- Kolme kõige olulisemat asja "Asjad, mida ma vihkan" nimekirjast (failist `preferences-and-constraints.md`).
- Paari-kolme "Käekirja mustrit" (failist `communication-style.md`).

Lahtrisse "How would you like ChatGPT to respond?" (Kuidas sa tahaksid, et ChatGPT vastaks?) kopeeri:

- Sinu üldine suhtlusstiil (konkreetne/otsekohene/jne failist `communication-style.md`).
- Sinu eelistused AI väljundi osas (failist `preferences-and-constraints.md`).
- Üks lause: "Match my voice. Lead with the answer. No preamble, no closing summary." (Kopeeri see julgelt inglise keeles, nii on kindlam, et ta saab aru.)

Kui ruum otsa saab, lõika esimesena välja "Asjad, mida ma vihkan" nimekiri — stiilijuhised selle kohta, kuidas vastata, on tähtsamad kui nimekiri negatiivsetest asjadest.

## 2. Custom GPTs (täisportfoolio teadmusfailidena)

Custom GPT-d (kohandatud GPT-d) lubavad sul faile üles laadida kui teadmust (knowledge). See on õige lüke, kui tahad ChatGPT-d, mis tunneb sind süvitsi ja püsivalt.

**Seadistamine:**

1. Loo uus Custom GPT (ChatGPT → Explore GPTs → Create).
2. GPT juhistesse (instructions) kopeeri kokkuliimitud "bundle" kaustast [`portfolio/bundles/`](../portfolio/bundles/) — või kopeeri kõigi kümne portfooliofaili sisu otse, kui see GPT on mõeldud üldiseks assistendiks.
3. Lae kogu oma portfoolio kaust üles teadmusfailidena (knowledge files). GPT saab neid sealt vajadusel pärida.
4. GPT juhistesse kirjuta: "You have access to my personal context portfolio as knowledge files. Read the relevant file before answering any question where my role, preferences, or voice would shape the answer. Do not narrate that you're doing this."

**Milliseid Custom GPT-sid tasub ehitada:**

- Üks üldine "tunneb mind" GPT, kus kõik kümme faili on teadmusena kaasas.
- Üks sisulooja GPT, mis kasutab [`portfolio/bundles/content-writer.md`](../portfolio/bundles/content-writer.md) bundle'it.
- Üks kirjade koostaja GPT, mis kasutab [`portfolio/bundles/client-outreach.md`](../portfolio/bundles/client-outreach.md) bundle'it.

Custom GPT-sid saab jagada, nii et kui sa ehitad süsteemi tiimile või kliendile, on see parim viis anda igale inimesele tema enda spetsiifiline assistent ilma, et sa peaksid mingit rasket infra arendama.

## 3. Projects (failide üleslaadimine, juhistel pole märgipiirangut)

ChatGPT Projects on sarnane Claude Projects'ile — sa manustad failid, mis püsivad igas selle projekti raames peetud vestluses, ja projekti juhistel (project instructions) ei ole tähemärgipiiranguid.

**Seadistamine:**

1. Loo uus Project ChatGPT-s.
2. Projekti juhistesse kopeeri kokkuliimitud bundle või kogu portfoolio sisu. Projektidel on helded piirangud juhiste pikkusele.
3. Manusta oma portfooliofailid projekti failidena.
4. Igal uuel vestlusel, mille sa selles projektis alustad, on sinu portfoolio elava kontekstina kaasas.

**Millal Projects on parem kui Custom GPT-d:**

- Kui tahad oma juhiseid tihti tuunida.
- Kui sul pole vaja tulemust kellegi teisega jagada.
- Kui sa tahad säilitada võimaluse alustada ühekordseid vestlusi, mis ei päri projekti konteksti (lihtsalt alusta need väljaspool projekti).

## Nõuanded kõigi kolme jaoks

- **Uuenda, kui portfoolio uueneb.** Aegunud kontekst on nähtamatu ja teeb märkamatult iga vestluse kvaliteedi kehvemaks. Kui teed oma kvartaalset portfoolio ülevaatust, lae uuenenud failid uuesti üles.
- **Ära kopeeri kõiki kümmet faili Custom Instructions lahtritesse.** Tähemärgipiirang sunnib sind sisu kokku pakkima. Kohanda formaat vastavalt platvormi võimalustele.
- **Testi diagnostilise promptiga.** Pärast seadistamist küsi: "Draft a two-sentence intro to a new prospect in my voice." (Koosta uuele potentsiaalsele kliendile minu häälega kahelauseiline sissejuhatus). Kui see kõlab nagu sina, ilma et sa peaksid midagi muutma, siis ühendus toimib. Kui ei, siis on sinu `communication-style.md` sisu liiga ümmargune — asi pole "juhtmetes".

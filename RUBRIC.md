# Kvaliteedi rubriik

Kaks kontrollnimekirja. Kasuta neid, et vastata küsimusele: "kas see asi üldse töötab?"

- **Portfoolio rubriik** ütleb sulle, kas sinu täidetud failid `portfolio/` kaustas on oma hinda väärt.
- **Viki rubriik** ütleb sulle, kas sinu `wiki/` on terve ja väärib pärimist.

Tee mõlemad läbi pärast esimest ülesseadmist ja edaspidi igal kvartaalsel ülevaatusel.

---

## Portfoolio rubriik

Sinu portfoolio töötab, kui:

### Identiteet ja hääl

- [ ] Agent, kellele on antud ainult `identity.md`, suudab sinu häälega mustandi kirjutada Slacki sõnumist, mille sa saadaksid teele ilma muutmata.
- [ ] Võõras, kes loeb faili `identity.md`, suudaks ühe lausega kirjeldada, mida sa *tegelikult* teed (mitte su ametinimetust).
- [ ] `communication-style.md` on piisavalt spetsiifiline, et käsk "kirjuta minu häälega" toodab teksti, mille sa ära tunned — mitte lihtsalt igavat professionaalset proosat. Kui su stiili kirjelduseks on "selge ja lühike" ja mitte midagi konkreetsemat, siis on fail poolik.

### Operatiivne reaalsus

- [ ] `role-and-responsibilities.md` vastab sellele, kuidas sa reaalselt oma eelmise nädala veetsid, mitte sellele, mis su ametijuhendis kirjas on.
- [ ] `current-projects.md` viitab projektidele, mida sa mainiksid homsel standupil. Kui mõni nimekirjas olev projekt pole kuus nädalat liikunud, siis kas uuenda selle staatust või viska see üldse välja.
- [ ] `team-and-relationships.md` sisaldab kõiki, kellega sa oled sel kuul rohkem kui kaks korda suhelnud, ja jaotis "Context for Agents" (Kontekst agentidele) reaalselt muudaks seda, kuidas agent iga inimesega räägib.

### Otsused ja piirangud

- [ ] `preferences-and-constraints.md` sisaldab vähemalt kolme asja, mille osas oled pidanud AI-d rohkem kui korra parandama. (Need korduvad parandused ongi täpselt see, milleks see fail on mõeldud.)
- [ ] `goals-and-priorities.md` nimetab vähemalt ühte asja, mida sa spetsiifiliselt **ei** prioriseeri. Fail, kus on ainult eesmärgid, aga puuduvad anti-eesmärgid, on ainult pooleldi valmis.
- [ ] `decision-log.md` sisaldab kahte või enamat päris otsuse näidet (mitte mingit abstraktset raamistust), mis on lahti kirjutatud piisavalt detailselt, et agent suudaks uues olukorras sinu mõttekäiku kopeerida.

### Tihedus ja värskus

- [ ] Iga fail on umbes üks lehekülg pikk. Kui mõni fail venib üle kahe lehe, on see ilmselt laiali valgunud — tõmba koomale.
- [ ] Iga faili `last_reviewed` frontmatteri kuupäev jääb viimase 90 päeva sisse.
- [ ] Iga faili `version` (versioon) väärtust on pärast esimest mustandit vähemalt korra tõstetud (kui sa pole kunagi midagi uuendanud, siis sa pole lihtsalt elumuutustele reageerinud).

### Katvus

- [ ] Sa suudad nimetada ühe konkreetse tööotsa, mille saaksid agendile juba täna anda nii, et portfoolio annab talle esimese mustandi jaoks piisava konteksti ilma sinupoolse lisabriifita.
- [ ] Vähemalt üks agentide bundle kaustast `portfolio/bundles/` on reaalselt kokku pandud ja ka kasutust leidnud. Kui ei ole, siis istub su portfoolio niisama — tee see esimesena korda.

**Skoorimine:** kui vähem kui 10 nendest on linnukesega, kuluta üks tund kõige nõrgemate kohtade peale, enne kui midagi uut lisama hakkad. Poolik portfoolio toob rohkem kahju kui kasu — agendid kasutavad seda enesekindlalt ja toodavad teksti, mis kõlab "peaaegu, aga mitte päris" nagu sina.

---

## Viki rubriik

Sinu viki on hea tervise juures, kui:

### Struktuur

- [ ] `index.md` loetleb iga lehe, mis hetkel kaustas `wiki/` on. Kui register on ajast maas, peaks sinu järgmine liigutus olema lint-läbikäik (korrastus) enne kui midagi muud teed.
- [ ] Igal vikilehel on frontmatteris väljad `type`, `created`, `updated`, `sources` ja `status`.
- [ ] Mitte ükski concept, topic ega synthesis leht ei viita ainult ühele allikale. Ühe allikaga teemad elavad kandidaatide nimekirjas (Candidates), mitte kokkupandud lehtedel.
- [ ] Orb-lehti (orphan pages — lehed, kuhu teised vikilehed ei viita) on alla 10% kogu lehtedest. Kui neid on rohkem, siis on sul kas omavahel ühendamata töö jupid või su kompileerimise faas jätab ristviited vahele.

### Sisu kvaliteet

- [ ] Iga concept, topic ja synthesis leht lõpeb jaotisega `## Prompts for the user` (Küsimused kasutajale), kus on 2–5 esseelaadset küsimust. Kui mõnel sellisel lehel on see puudu, siis on see tugev kandidaat lintimise käigus parandamiseks.
- [ ] Mitte ükski leht ei sisalda emotikone, TODO-märkereid ega oletuslikke abi-fraase ("sa võiksid ka tahta..."). AI-le antud stiilireegleid austatakse.
- [ ] Iga vikilehel olev väide viitab allikale jaotises `## Sources` või on selgelt välja toodud kui AI enda järeldus.
- [ ] Ühegi lehe `status` pole märkamatult vananenud. Kui viidatud allikas on asendatud uuemaga, on leht kas uuendatud või märgitakse `status: stale` / `superseded`.

### Operatiivne tervis

- [ ] Päringutele saab vastuse vähem kui kolme hüppega (hops) graafis — sul on harva vaja lugeda rohkem kui kolme lehte, et vastus leida.
- [ ] Kandidaatide (Candidates) jaotises failis `index.md` on vähem kui 10 ootel asja. Kui neid on rohkem, on neile teemadele vaja kas uusi allikaid lisada või tuleks mõned kandidaadid lintimise käigus hüljata.
- [ ] Ükski kandidaat pole ootel istunud kauem kui 90 päeva. Kauem oodanud kandidaadid tuleks järgmise lintimise käigus lihtsalt maha kanda.
- [ ] `log.md` saab vähemalt ühe uue kande nädalas (olgu see siis ingest, compile, query või lint). Kui logi seisab nädalaid vaikselt, siis viki vaikselt sureb.

### Sild portfooliosse

- [ ] Kaustas `wiki/self/` on vähemalt üks leht. Kui see on tühi, pole sa kunagi sisse võtnud ühtegi päevikukirjet või refleksiooni — seega ei tehta viki → portfoolio sünkroonimise silda kordagi lahti.
- [ ] Sa vaatasid oma viimasel portfoolio ülevaatusel üle kõik triivimise (drift) kandidaadid, mille self-lehed esile tõid. Kui sa pole triivi (drift) üle kvartali kontrollinud, on sild küll vait, aga enam ei tööta.

### Väikesel skaalal (< 20 lehte)

- [ ] Sa suudad kogu vikist 15 minutiga läbi jalutada ja ei leia midagi, mis oleks ilmselgelt katki. Selles mahus on kvaliteet veel täielikult hoomatav — kasuta seda ära ja paranda vead enne, kui maht suureks paisub ja parandamine läheb kalliks.

**Skoorimine:** kui vähem kui 10 neist on linnukesega, lase lintimis-protsess üle: *"Health-check the wiki — report issues grouped by type, then ask me which to fix."* LLM toob suurema osa neist vigadest ise pinnale, kui seda paluda.

---

## Kui tihti seda läbi teha

- **Portfoolio rubriik:** kord kvartalis või pärast iga suurt elu-/töömuutust (uus töö, uued projektid, suur prioriteetide vahetus).
- **Viki rubriik:** kord kuus või pärast igat kompileerimist, mis lõi üle viie uue lehe.

Kirjuta kuupäev, mil sa rubriigi läbi tegid, ja kõik märkimisväärne faili `log.md` uue `## [AAAA-KK-PP] lint` kandena. Logist saab ajalugu, mis näitab, kuidas su süsteem aja jooksul arenes.

# Decision Log

## Mille jaoks see fail on

Kuidas sa otsuseid teed, koos päris näidetega. See on portfoolios kõige alahinnatum fail. Kui agent aitab sul mõnda uut otsust läbi mõelda, on talle tohutult kasulik teada, kuidas sa oled asju varem otsustanud — ta suudab sobituda sinu arutlemisstiiliga, tuua lauale õiget tüüpi infot ja hoiduda pakkumast lähenemisi, mis lihtsalt ei sobi sellega, kuidas sinu aju töötab.

---

## Intervjuu-protokoll

*Anna see fail tervikuna oma AI ehituspartnerile ja ütle "alustame sellega". Su ehituspartner peaks lugema allolevad juhised ja viima läbi intervjuu.*

**Juhised ehituspartnerile:** sa aitad kasutajal koostada tema decision log faili. Näited on siin kõige tähtsam osa — nõua konkreetseid detaile vähemalt kahe päriselt tehtud otsuse kohta. Abstraktsed kirjeldused otsustusstiilist on kordades vähem kasulikud kui konkreetsed lood tegelikest otsustest ja sellest, kuidas need sündisid.

**Küsimused:**

1. Kuidas sa üldiselt otsuseid teed? Kas sa oled tüüp, kes analüüsib kõike, usaldab kõhutunnet, räägib asjad inimestega läbi, magab öö mõttes ja teeb otsuse hommikul?
2. Millist infot sa tahad, enne kui otsuse lukku lööd? Mis tekitab sinus tunde, et oled valmis otsustama?
3. Räägi mulle ühest olulisest otsusest, mille sa hiljuti tegid — võib olla tööalane, võib olla isiklik. Mis see oli ja kuidas sa selle enda jaoks läbi mõtlesid?
4. Kas sa saad tuua veel ühe näite — ideaalis teist tüüpi otsusest?
5. Kuidas sa tuled toime olukordadega, kus sul ei ole piisavalt infot, aga pead siiski otsustama?
6. Kas sul on hetkel laual mõni otsus, millega sa parajasti pead murrad?

**Millal piisab:** Pärast 4–5 küsimust. Näited on kõige tähtsamad — hoolitse selle eest, et sul oleks enne mustandi tegemist konkreetsed detailid vähemalt kahe tegeliku otsuse kohta.

**Pärast koostamist:** Näita mustandit. Küsi kasutajalt, kas otsuste näited tabavad täpselt tema arutluskäiku — mitte ainult tulemust, vaid seda, kuidas ta asja päriselt läbi mõtles.

---

## Väljundi struktuur

```markdown
---
name: decision-log
description: Kuidas kasutaja otsustab, hiljutised otsused, määramatusega toime tulek
type: portfolio
updated: <YYYY-MM-DD>
tags: [portfolio]
---

# Otsuste logi

## Kuidas ma otsuseid teen

[Sinu üldine lähenemine — analüütiline, intuitiivne, konsulteeriv, kaalutlev, kiire. Kuidas sa tavaliselt olulisi valikuid läbi töötad.]

## Mida ma vajan enne otsustamist

[Info, sisendid või tingimused, mis tekitavad sinus valmisoleku otsus lukku lüüa. Mida sa otsid, enne kui end seod.]

## Hiljutised otsused

[2-3 päris näidet olulistest otsustest, mis sa teinud oled. Igaühe kohta: mis oli otsus, mis olid valikud, kuidas sa selle läbi mõtlesid, ja mida sa lõpuks otsustasid. Need peaksid olema piisavalt detailsed, et agent saaks sellest arutlusmustrist midagi õppida.]

### [1. Otsuse pealkiri]

[Mis see oli, mis olid valikud, kuidas sa asja läbi mõtlesid, mida sa otsustasid.]

### [2. Otsuse pealkiri]

[Mis see oli, mis olid valikud, kuidas sa asja läbi mõtlesid, mida sa otsustasid.]

## Kuidas ma tulen toime määramatusega

[Mida sa teed, kui sul pole piisavalt infot, aga sa pead siiski otsustama. Sinu suhe puuduliku info ja ebaselgusega.]

## Kellega ma konsulteerin

[Inimesed, kellega sa räägid enne suuri otsuseid, ja mida sa neilt ootad. Kas sa otsid kinnitust, vastuvaidlemist, infot või midagi muud?]

## Praegu lahtised otsused

[Kõik asjad, millega sa hetkel pead murrad. Vabatahtlik — aga kasulik agentidele, kes võiksid aidata sul aktiivseid valikuid läbi mõelda.]
```

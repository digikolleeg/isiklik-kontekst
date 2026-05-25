# Kuidas ühendada: Süsteemiprompti mustrid (System Prompt Patterns)

## Mis see on

Copy-paste mustrid, mille abil saad süstida oma portfoolio konteksti mistahes AI tööriista süsteemiprompti (system prompt) või kohandatud juhistesse (custom instructions). See on kõige lihtsam, "low-tech" ja universaalsem ühendamise (wiring) viis — see töötab nii Claude'i, ChatGPT, Gemini kui ka ükskõik mille muuga, mis laseb sul süsteemiprompti seadistada.

## Baasmuster

Kopeeri asjakohane portfoolio sisu oma süsteemiprompti ja mähi see selgete markerite vahele:

```
<user_context>
[kleebi oma identity.md sisu siia]
[kleebi muud asjakohased failid siia]
</user_context>

You have context about the user above. Use it to inform your responses — their role, their projects, their communication style, their preferences. Don't reference this context explicitly unless asked. Just know them.
```

## Mustrid kasutusjuhtude kaupa

### Üldine tööassistent

```
<user_context>
[identity.md]
[role-and-responsibilities.md]
[communication-style.md]
[preferences-and-constraints.md]
</user_context>

You are a work assistant for the person described above. Match their communication style in your responses. Respect their stated preferences and constraints. When making suggestions, consider their current role and responsibilities.
```

### Kirjutamisassistent

```
<user_context>
[identity.md]
[communication-style.md]
[domain-knowledge.md]
</user_context>

You are a writing assistant. Your job is to produce drafts that sound like the person described above — their vocabulary, their sentence structure, their tone. Use their domain knowledge to calibrate the level of explanation. Avoid every word and pattern they've listed under "what I dislike." When in doubt, be more concise rather than more thorough.
```

### Koosolekuks ettevalmistus

```
<user_context>
[identity.md]
[team-and-relationships.md]
[current-projects.md]
</user_context>

You help prepare for meetings. When given a meeting topic and attendees, use the team context above to understand the relationships and dynamics, and use the project context to identify relevant workstreams. Produce a brief prep document with: key topics to cover, potential questions to expect, and any context from the relationship notes that's relevant.
```

### Strateegiline nõuandja

```
<user_context>
[identity.md]
[goals-and-priorities.md]
[current-projects.md]
[decision-log.md]
</user_context>

You are a strategic thinking partner. Use the goals and priorities context to understand what the person is optimizing for. Use the decision log to understand how they think through decisions — match their reasoning style. When presenting options, frame tradeoffs the way they think about tradeoffs (see their stated preferences). Be direct and concise.
```

## Nõuanded

- Ära kleebi kõiki kümmet faili süsteemiprompti. Enamikul tööriistadel on kontekstipiirangud ja ebaoluline kontekst lahjendab kasuliku konteksti mõju. Vali 2-4 faili, mis vastavad konkreetsele kasutusjuhule.
- Juhiste lõik kontekstiploki järel on sama oluline kui kontekst ise. Ütle AI-le spetsiifiliselt, kuidas seda konteksti kasutada — ära eelda, et ta ise ära arvab.
- Kui kasutad tööriistu, kus on kohandatud juhistele tähemärgipiirangud (nagu ChatGPT Custom Instructions), kasuta ainult faile `identity.md` ja `communication-style.md`. Need kaks katavad kõige suurema väärtusega konteksti kõige väiksemas mahus.
- Testi süsteemi nii: palu AI-l teha midagi, millega ta tavaliselt ilma kontekstita puusse paneks — näiteks kirjutada e-kiri sinu stiilis või valmistuda kohtumiseks väga konkreetse inimesega. Kui tulemus on parem, siis ühendus (wiring) toimib.
- Kui su portfooliofailid muutuvad, uuenda ka kleebitud sisu. Aegunud kontekst süsteemipromptis on nähtamatu, aga tõmbab vaikselt ja kindlalt väljundi kvaliteedi alla.

# Quality Rubric

Two checklists. Use them to answer "is this working?"

- The **portfolio rubric** tells you whether your filled `portfolio/` files are pulling their weight.
- The **wiki rubric** tells you whether your `wiki/` is healthy and worth querying.

Run through both after an initial build, then again at every quarterly review.

---

## Portfolio Rubric

Your portfolio is working if:

### Identity and Voice

- [ ] An agent given only `identity.md` can draft a Slack message in your voice that you'd send without editing.
- [ ] A stranger who reads `identity.md` could describe what you actually do (not your title) in one sentence.
- [ ] `communication-style.md` is specific enough that "write it in my voice" produces output you recognize — not generic professional prose. If you see "clear and concise" as a description of your style and nothing more concrete, the file isn't done.

### Operational Reality

- [ ] `role-and-responsibilities.md` matches how you actually spent last week, not how your job description reads.
- [ ] `current-projects.md` references projects you'd mention in tomorrow's standup. If any listed project hasn't moved in six weeks, either update its status or remove it.
- [ ] `team-and-relationships.md` includes everyone you've interacted with more than twice this month, and the "Context for Agents" notes would genuinely change how an agent talks to each person.

### Decisions and Constraints

- [ ] `preferences-and-constraints.md` contains at least three things you've ever had to correct an AI about more than once. (Those recurring corrections are exactly what the file is for.)
- [ ] `goals-and-priorities.md` names at least one thing you are explicitly **not** prioritizing. A file with only goals and no anti-goals is half-done.
- [ ] `decision-log.md` has two or more real decision examples (not abstract framings) detailed enough that an agent could match your reasoning pattern on a new call.

### Density and Freshness

- [ ] Each file is roughly one page. If any file is longer than two, it's probably sprawling — tighten it.
- [ ] Every file's `last_reviewed` frontmatter is within the last 90 days.
- [ ] Every file's `version` field has been bumped at least once since the initial draft (if you've never updated, you haven't reacted to reality yet).

### Coverage

- [ ] You can name a concrete task you'd hand to an agent today where the portfolio gives it enough context to produce a first draft without you briefing it further.
- [ ] At least one agent bundle in `portfolio/bundles/` has been stitched and actually used. If none have, the portfolio is sitting unused — fix that first.

**Scoring:** if fewer than 10 of these are checked, spend an hour on the weakest items before adding anything else. A half-done portfolio is a net negative — agents will confidently use it and produce things that sound almost-but-not-quite like you.

---

## Wiki Rubric

Your wiki is healthy if:

### Structure

- [ ] `index.md` lists every page currently in `wiki/`. If the index is out of date, your next operation should be a lint pass before anything else.
- [ ] Every wiki page has frontmatter with a `type`, `created`, `updated`, `sources`, and `status`.
- [ ] No concept, topic, or synthesis page cites only one source. Single-source themes live in Candidates, not in compiled pages.
- [ ] Orphan pages (zero inbound links from other wiki pages) are under 10% of total pages. If higher, you either have disconnected work or your compile pass is skipping cross-references.

### Content Quality

- [ ] Every concept, topic, and synthesis page ends with a `## Prompts for the user` section with 2–5 essay-shaped questions. Missing this section on any such page is a lint-fix candidate.
- [ ] No page contains emojis, TODO markers, or speculative helpers ("you might also want to…"). AI-written style constraints are respected.
- [ ] Every claim in a wiki page either cites a source in `## Sources` or is explicitly flagged as the AI's extrapolation.
- [ ] No page's `status` is silently stale. If a source it cites has been superseded by a newer source, the page is either updated or marked `status: stale` / `superseded`.

### Operational Health

- [ ] Queries get answered in under three hops through the graph — you rarely need to read more than three pages to find an answer.
- [ ] The Candidates section in `index.md` has fewer than 10 waiting items. If higher, either more sources are needed on those themes, or some candidates should be abandoned during lint.
- [ ] No candidate has been waiting in the Candidates list for more than 90 days. Candidates waiting longer should be abandoned during the next lint pass.
- [ ] `log.md` has at least one entry per week (of whatever type — ingest, compile, query, lint). If it's quiet for weeks, the wiki is slowly dying.

### Bridge to Portfolio

- [ ] `wiki/self/` has at least one page. If it's empty, you've never ingested a journal or reflection — the wiki → portfolio drift bridge isn't being exercised.
- [ ] At your last portfolio review, you reviewed any drift candidates surfaced by self-pages. If you haven't checked drift in more than a quarter, the bridge is silent but not working.

### At Small Scale (< 20 pages)

- [ ] You can walk through the whole wiki in under 15 minutes and not find anything obviously wrong. At this scale, quality is still fully legible — take advantage of that to fix issues before the scale makes it expensive.

**Scoring:** if fewer than 10 items are checked, run a lint pass: *"Health-check the wiki — report issues grouped by type, then ask me which to fix."* The LLM will surface most of these automatically if asked.

---

## How Often to Run This

- **Portfolio rubric:** quarterly, or after any major life/work change (new job, new projects, major priority shift).
- **Wiki rubric:** monthly, or after any compile pass that created more than five new pages.

Write the date you ran the rubric and anything notable into `log.md` as a `## [YYYY-MM-DD] lint` entry. The log becomes the history of how the system evolved.

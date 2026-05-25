# Wiring: ChatGPT Web

Three ways to give ChatGPT your portfolio, in increasing order of sophistication. Pick the one that matches how you actually use ChatGPT.

## 1. Custom Instructions (character-limited)

ChatGPT's Custom Instructions are persistent across every conversation — they apply whether you're asking for code, writing, research, or anything else. The catch: there's a character limit (~1500 chars per box), which means you can only fit the most compressed version of your portfolio.

**What to paste:**

In the "What would you like ChatGPT to know about you?" box, paste a compressed summary drawn from:

- Your name, role, organization (from `identity.md`)
- The "What I Do" paragraph (from `identity.md`)
- The top three items from your "Things I Hate" list (from `preferences-and-constraints.md`)
- Two or three "Signature Patterns" (from `communication-style.md`)

In the "How would you like ChatGPT to respond?" box, paste:

- Your overall communication style (concise/direct/etc. from `communication-style.md`)
- Your AI output preferences (from `preferences-and-constraints.md`)
- One sentence: "Match my voice. Lead with the answer. No preamble, no closing summary."

If you run out of space, cut the "Things I Hate" list first — style guidance on how to respond matters more than a list of negatives.

## 2. Custom GPTs (full portfolio as knowledge files)

Custom GPTs let you upload files as knowledge. This is the right move if you want a ChatGPT that knows you deeply and persistently.

**Setup:**

1. Create a new Custom GPT (ChatGPT → Explore GPTs → Create).
2. In the GPT's instructions, paste a stitched bundle from [`portfolio/bundles/`](../portfolio/bundles/) — or paste all ten portfolio files' content directly if the GPT is meant to be a general-purpose assistant.
3. Upload your full portfolio folder as knowledge files. The GPT can retrieve from them on demand.
4. In the GPT's instructions, tell it: "You have access to my personal context portfolio as knowledge files. Read the relevant file before answering any question where my role, preferences, or voice would shape the answer. Do not narrate that you're doing this."

**Which Custom GPTs are worth building:**

- One general "knows me" GPT with all ten files as knowledge.
- One content-writer GPT using the [`portfolio/bundles/content-writer.md`](../portfolio/bundles/content-writer.md) bundle.
- One outreach-drafter GPT using the [`portfolio/bundles/client-outreach.md`](../portfolio/bundles/client-outreach.md) bundle.

Custom GPTs are shareable, so if you're building for a team or client, this is the format where each person gets their own without you building infrastructure.

## 3. Projects (file upload, no character limit on instructions)

ChatGPT Projects are similar to Claude Projects — you attach files that persist across every conversation in the project, with no character limits on the project instructions.

**Setup:**

1. Create a new Project in ChatGPT.
2. In project instructions, paste a stitched bundle or the full portfolio content. Projects have generous instruction limits.
3. Attach your portfolio files as project files.
4. Every conversation you start inside the project has the portfolio as live context.

**When Projects beat Custom GPTs:**

- You want to iterate on instructions frequently.
- You don't need to share the result with anyone else.
- You want the option to start one-off conversations that don't inherit project context (just start them outside the project).

## Tips Across All Three

- **Update when the portfolio updates.** Stale context is invisible and silently degrades every conversation. When you run a quarterly portfolio review, re-upload the changed files.
- **Don't paste all ten files into Custom Instructions.** The character limit forces compression. Match the format to the surface.
- **Test with a diagnostic prompt.** After setup, ask: "Draft a two-sentence intro to a new prospect in my voice." If the output sounds like you without editing, the wiring works. If not, your `communication-style.md` content needs to be more specific — not the wiring.

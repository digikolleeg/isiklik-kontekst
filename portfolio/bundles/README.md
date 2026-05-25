# Agent Bundles

Pre-composed context packs, ready to paste into any agent's system prompt or custom-instructions field.

Each bundle is a single markdown file combining:

1. **A preamble** — purpose-built instructions that tell the agent what role it's playing and how to use the context that follows.
2. **Placeholder blocks** — clearly marked sections like `[[IDENTITY]]` where you paste content from your filled portfolio files.
3. **Composition notes** — which portfolio files feed which block, and why.

Bundles are the missing link between "I have portfolio files" and "I have a working agent." They work without any tooling: paste into a Custom GPT, a Claude Project, a Gemini Gem, or the system-prompt field of whatever agent framework you're using.

---

## What Ships

| Bundle | Composed from | For |
|--------|---------------|-----|
| [`content-writer.md`](content-writer.md) | `identity.md` + `communication-style.md` + `domain-knowledge.md` | Agents writing blog posts, LinkedIn content, newsletters, marketing copy in your voice. |
| [`client-outreach.md`](client-outreach.md) | `identity.md` + `communication-style.md` + `team-and-relationships.md` | Agents drafting cold emails, follow-ups, proposals, and replies to prospects. |
| [`client-research.md`](client-research.md) | `identity.md` + `current-projects.md` + `domain-knowledge.md` | Agents researching prospects, competitors, industry context, and relevant background for an upcoming conversation. |

---

## How to Use a Bundle

1. Open the bundle file you want.
2. Open your filled portfolio files in another window.
3. For each placeholder block (e.g. `[[IDENTITY]]`), paste the entire body of the matching portfolio file into that block.
4. Copy the resulting, stitched markdown into the agent's system prompt / custom instructions field.
5. Done. The agent now starts every conversation grounded in your voice, your constraints, and your context.

**Tip:** If the agent's context budget is tight, trim the pasted portfolio content to the most relevant sections. Bundles are composable — customize the preamble and the mix for your use case.

---

## Composing Your Own Bundles

The three bundles shipped here are starting points, not a closed set. When you find yourself briefing an agent for the same kind of task repeatedly, that's a bundle waiting to be written.

Composition rules of thumb:

- **Always include `identity.md`.** Every agent needs to know who it's working for.
- **Keep bundles single-purpose.** A bundle that tries to do everything ends up doing nothing well.
- **Three portfolio files is usually the right size.** More and the agent's context budget suffers; fewer and the agent misses judgment-calls it could have made.
- **Preamble over context.** A tight, specific preamble does more work than another pasted portfolio file.

Write new bundles as markdown files in this directory, following the same shape: preamble, placeholder blocks, composition notes.

---

## Keeping Bundles in Sync

Bundles embed portfolio content by reference (you paste in the content). When you update a portfolio file during a quarterly review, re-stitch any bundles that reference that file. Otherwise the agent is working from stale context.

The log convention is simple: when you update a portfolio file, list the affected bundles in the `log.md` entry for that update, so you know what to re-stitch.

Phase 2 will ship an MCP tool (`get_bundle(agent_type)`) that performs the stitching at runtime and removes this maintenance burden. Until then, the stitch is manual — but fast, because the bundles are short.

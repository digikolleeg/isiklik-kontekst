# Wiring: Obsidian

Obsidian is the best environment for living inside this repo day to day. It's markdown-native, the graph view lights up as your wiki grows, and Dataview turns the frontmatter conventions into real queries.

## Open the Repo as a Vault

1. Obsidian → File → Open folder as vault → pick this repo's root.
2. Let Obsidian index the folder. Wiki links (`[[wiki/.examples/concepts/foo]]`) will resolve; internal links become navigable.
3. Open the graph view (left sidebar → graph icon, or `Ctrl/Cmd-G`). You'll see your wiki as a connected graph once you start compiling pages.

## Graph View

- **At 0 wiki pages:** graph is empty. This is correct.
- **At 10 pages (run the `.examples/` walkthrough):** you should see a small connected cluster. Concepts link to topics, sources link to concepts, entities pull toward the concepts that cite them.
- **At 50+ pages:** filter the graph to hide `portfolio/`, `raw/`, and `templates/` so only the wiki layer is visible. This is where the graph starts earning its keep.

## Dataview Queries (from Frontmatter)

The frontmatter conventions in `CLAUDE.md` are Dataview-friendly. Install the Dataview community plugin to unlock queries like:

**Find all concept pages with only one source (lint candidates):**

```dataview
LIST
FROM "wiki"
WHERE type = "concept" AND length(sources) < 2
```

**Find portfolio files not reviewed in 90 days:**

```dataview
LIST
FROM "portfolio"
WHERE last_reviewed < date(today) - dur(90 days)
```

**List stale or superseded wiki pages:**

```dataview
TABLE status, updated
FROM "wiki"
WHERE status = "stale" OR status = "superseded"
SORT updated DESC
```

Drop these into a dashboard note (e.g., `wiki-health.md`) and pin it — it becomes a live lint view without running a full lint pass.

## Obsidian Web Clipper → `raw/`

The official Obsidian Web Clipper extension can clip articles straight into a folder. Configure it to save into `raw/` — articles land as markdown, ready for the next ingest pass. This is the cheapest capture path for the wiki layer. Lower the friction of sources landing and the wiki compounds faster.

## Hotkey for Image Downloads

If you clip or paste content with images, set a hotkey for "Download all images" (either a plugin or a built-in depending on your Obsidian version). Images saved locally survive link rot; pasted-as-URLs don't.

## Cross-Machine Sync via Google Drive / iCloud

If you want the same vault on multiple machines without Obsidian Sync, put the repo folder inside Google Drive, iCloud, or Dropbox. Every machine opens the folder as the same vault, and edits propagate through the cloud provider.

Caveats:

- Sync conflicts can happen if you edit on two machines simultaneously. Obsidian handles this gracefully in most cases; heavy users should consider Obsidian Sync as a cleaner solution.
- Symlinks are fragile across cloud-sync tools. Keep the vault root inside the sync folder, not a symlink to it.

## Useful Plugins

- **Dataview** — frontmatter queries (see above).
- **Obsidian Web Clipper** — source capture.
- **Templater** — for auto-filling the frontmatter block on new wiki / portfolio files (optional, but speeds things up).
- **Text Generator** or **Claude/ChatGPT plugins** — if you want to run ingest / compile / query operations without leaving Obsidian.

## Workflow Notes

- Keep `CLAUDE.md` pinned in a tab. Reference it when you or an AI agent is running an operation in this vault.
- `log.md` is append-only. Don't let Obsidian's auto-formatting rearrange it.
- If you share this vault with a team (unusual for a personal context repo, but possible), use `.private/` (Phase 2) for anything sensitive. Don't rely on "I'll just not open that file around others."

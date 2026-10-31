# CMDS System Files

> 6 Core System Files + 9 Shared Rules + 9 Architecture Patterns that power the CMDSPACE Personal Knowledge Management ecosystem.

## Live Demo

**https://system.cmdspace.work**

## Overview

CMDS (CMDSPACE) is a comprehensive Personal Knowledge Management (PKM) system built on Obsidian with 14,000+ notes (measured 2026-10-30). This repository contains the core system files that provide complete guidance for AI agents and human users working with the vault.

## What's New in v4.16.1 (2026-10-30 ~ 31)

- **Site: diagrams and guides (2026-10-31, files unchanged)** — the landing page and the docs now explain the system with 9 pre-rendered Pele diagrams (load order, CMDS Process, 8-way sync, note metadata, who-reads-what, rule loading, command parity, vault layout, release flow), a "Start here" reading order, and four static guide sections (Who reads what · Commands · Where things live · Versions & releases). Diagram sources live in `diagrams/src/` and are inlined by `scripts/build-diagrams.py`; theme follows the page via `assets/pele/cmds-pele.css`.

- **v4.16.1 patch (2026-10-31)** — user-approved cleanup after the audit: five empty duplicate-numbered folders and five stray hub-prefixed Inbox notes were quarantined or renamed, and the Guide tree, directory-structure rule and inbox command were updated to match.

- **Full audit of the instruction layer** — 9 system files, 9 shared rules, 13 slash commands, the schema bundle, the sync surfaces and the satellite vaults were audited by a multi-agent workflow (finders → adversarial verification) and the confirmed defects were fixed in one release. Details in the audit note linked from the CHANGELOG.
- **One canonical sync script** — the three diverging copies of the ①~⑤ sync procedure were replaced by `scripts/sync-system-files.sh` in the vault (gates: tags regression, date consistency, version/count drift, web version labels; steps: backup incl. CHANGELOG copy, sanitized share with leak gate, DEV files + rules + ZIP, GitHub push + tag + Release, Vercel deploy + live check; satellite report).
- **Context diet round 2** — the deployment procedure moved out of CLAUDE.md (loaded into every session) into a vault note; CLAUDE.md keeps a summary and pointers.
- **Command inventory** — 13 commands (10 CMDS Process + `/daily`, `/weekly`, `/insight`) are now listed once in the agent-system ledger; the system files point there instead of hardcoding counts.
- **ANTIGRAVITY.md 2.9** — catch-up release for the Gemini-only file (9 rules incl. file-move-rules, command inventory pointer, contracts added since September).
- **Counts corrected everywhere** — 87 subcategories (was "91" on the landing page and here), 9 shared rules (was "8" in docs and here), 14,000+ notes, plugin facts measured at runtime.

## Previous Highlights

- **v4.15.1** (2026-10-29) — 🏛 CMDS Guide 2.12: body example tags backticked so Obsidian Linter stops lifting them into frontmatter
- **v4.15.0** (2026-10-29) — Academic citation rule (`[@citekey]` via CMDS Zotero) + export outputs kept outside the vault
- **v4.14.0** (2026-10-21 ~ 23) — Diagram system: Pele renderer + `@key/@interp/@aux` color directives shared by vault and publications
- **v4.13.0** (2026-10-10) — Dot-folder sync policy (agent settings canonical folder + symlinks) + context diet round 1
- **v4.12.0** (2026-09-21) — Agent scope separation (project-scope vs user-scope)
- **v4.11.0** (2026-08-29) — CMDS Process commands 8 → 10 (`/seeds`, `/harvest`)
- **v4.10.0** (2026-08-17) — Periodic agent notes (`/daily`, `/weekly`)
- **v4.9.0 ~ v4.9.3** (2026-05-30 ~ 07-03) — DESIGN.md as the 6th public file; 9-file scheme; first full multi-agent audit
- **v4.8.0** (2026-05-27) — 8→9 transition declared (DESIGN.md as precedence 9); satellite sync routine
- **v4.6.0** (2026-05-13) — `DESIGN.md` + `design-tokens.json` design-system surface added
- **v4.4** (2026-05-03) — 8-file scheme + Codex/Antigravity output lanes
- **v4.2** (2026-04-15) — CMDS Process Command Suite (8 slash commands at the time)
- **v4.1** (2026-04-07) — `description` field (English, LLM relevance hint) added as required property; 7 required properties total
- **v4.0** (2026-04-01) — Shared rules (`.claude/rules/`) via `@include`; 9 architecture patterns; enhanced frontmatter (`precedence`, `memory-type`, `token-estimate`, etc.)
- **v3.0** (2026-03-15) — Structured YAML frontmatter; share system with placeholder rules
- **v2.0** (2026-01-20) — 5-file architecture (CLAUDE.md, AGENTS.md, CMDS.md, CMDS Guide, CMDS Head Quarter)
- **v1.0** (2025-10-01) — Initial system files

See [CHANGELOG.md](CHANGELOG.md) for full history.

## Repository Structure

```
files/
├── CLAUDE.md              # Claude Code technical guide (precedence: 1)
├── AGENTS.md              # Other AI agents guide (precedence: 2)
├── CMDS.md                # System philosophy for all LLMs (precedence: 4)
├── CMDS-Guide.md          # Operational standards (precedence: 5)
├── CMDS-Head-Quarter.md   # Navigation hub (precedence: 6)
├── DESIGN.md              # Visual language spec (precedence: 9)
└── CMDS-System-Files.zip  # All files bundled

rules/                     # 9 shared rules (mirror of .claude/rules/)
├── indentation-rules.md        # YAML 2-spaces / Markdown TAB
├── frontmatter-standard.md     # 7 required properties + format
├── file-creation-rules.md      # Output path, naming, project folders, artifact closeout
├── file-move-rules.md          # Move/rename contract: update active references, preserve history
├── wikilink-rules.md           # Obsidian wikilink syntax + YAML quoting + cross-vault URIs
├── directory-structure.md      # Vault folder structure + CMDS categories
├── mermaid-rules.md            # Mermaid/Pele diagram rules (Obsidian + publications)
├── blank-line-rules.md         # Obsidian-tight blank line rules
└── video-project-workflow.md   # Remotion / video project placement rules

CHANGELOG.md               # Version history

diagrams/src/              # Pele (Mermaid) sources for the site diagrams, <slug>-en.md / <slug>-ko.md
scripts/build-diagrams.py  # renders them (pele-render, screen profile, 680/340 px) and inlines the SVG between <!-- diagram:<slug> --> markers
assets/pele/               # cmds-pele.css theme copy (synced from /DEV/cmds-pele by pele-sync.py)
```

## The 6 Core Files

These are the 6 publicly deployed files. The full scheme is **9 total** — the other 3 (ANTIGRAVITY.md precedence 3 = Gemini-only; BRAIN.md precedence 7 and BRAIN_PROMPT.md precedence 8 = Gobi persona) are private and not distributed here.

### For AI Agents (loaded into context window)

| File | Audience | Focus | Precedence |
|------|----------|-------|:----------:|
| **CLAUDE.md** | Claude Code | Technical implementation (HOW) | 1 |
| **AGENTS.md** | Codex, Cursor, Windsurf | Portable technical rules (HOW) | 2 |
| **CMDS.md** | All LLM assistants | Context & philosophy (WHY/WHAT) | 4 |

### For Humans (referenced in Obsidian)

| File | Audience | Focus | Precedence |
|------|----------|-------|:----------:|
| **CMDS Guide** | User + AI | Operational standards | 5 |
| **CMDS Head Quarter** | User | Navigation hub | 6 |

### Visual Language (loaded when producing visual artifacts)

| File | Audience | Focus | Precedence |
|------|----------|-------|:----------:|
| **DESIGN.md** | All agents producing visual output | Visual language spec (HOW — visual) | 9 |

## Architecture Patterns (from Claude Code Source Analysis)

| # | Pattern | Purpose |
|---|---------|---------|
| 1 | **precedence** | File priority ordering (1-9) for conflict resolution |
| 2 | **STATIC/DYNAMIC** | Cache-aware sections for AI processing |
| 3 | **@include** | Shared rules via file inclusion (AI reads inline) |
| 4 | **Essential** | Post-compact recovery — core rules that survive context compression |
| 5 | **required-for/optional-for** | Agent scoping — which tasks need which files |
| 6 | **memory-type** | Maps to Claude Code's memdir types (feedback/user/reference) |
| 7 | **token-estimate** | Token budget awareness for AI load prioritization |
| 8 | **changelog** | Inline version history in each file's frontmatter |
| 9 | **shared rules** | Common rules in `.claude/rules/` shared via @include |

## @include vs [[wikilink]]

| Syntax | Purpose | Used By |
|--------|---------|---------|
| `@path` | AI reads file content inline | AI agents (Claude Code, etc.) |
| `[[name]]` | Obsidian internal link for navigation | Obsidian graph view, backlinks |
| Both together | `@file → [[file]]` | When both AI loading and human navigation needed |

## CMDS Process

```
Connect → Merge → Develop → Share
```

| Stage | Categories | What Happens |
|-------|-----------|--------------|
| **Connect** | 100 Themes | Discover ideas, capture interests |
| **Merge** | 200 Literature | Integrate knowledge, build theory |
| **Develop** | 300-600 | Collect data, apply methods, use tools |
| **Share** | 700-800 | Create content, publish, teach, consult |

## Getting Started

1. **Download** all files from [system.cmdspace.work](https://system.cmdspace.work)
2. **Place** system files in the root of your Obsidian vault
3. **Place** rules in `.claude/rules/` directory
4. **Customize** placeholders (`{your-name}`, `{vault-path}`, etc.)
5. **Reference** CMDS.md in your AI conversations for context

## Stats

| Metric | Value |
|--------|-------|
| Core System Files | 6 (of 9 total) |
| Shared Rules | 9 |
| Slash Commands | 13 (10 CMDS Process + `/daily`, `/weekly`, `/insight`) |
| Architecture Patterns | 9 |
| Required Frontmatter Properties | 7 |
| CMDS Categories | 9 (100-900) |
| Subcategories | 87 |
| Vault Notes | 14,000+ (2026-10-30) |
| Site Diagrams | 9 (Pele, bilingual, light/dark) |

## Download

- [Download All (ZIP)](https://system.cmdspace.work/files/CMDS-System-Files.zip)
- [Browse Files](https://system.cmdspace.work/#download)

## Links

- [Profile](https://litt.ly/cmds)
- [YouTube](https://www.youtube.com/@cmdspace)
- [X (Twitter)](https://x.com/YohanKoo)
- [LinkedIn](https://www.linkedin.com/in/yohan-koo-a1baa3138/)
- [Threads](https://www.threads.com/@cmds_pace)
- [Education](https://class.cmdspace.kr/)

## License

All intellectual property rights belong to CMDSPACE.

---

Last Updated: 2026-10-31 · v4.16.1

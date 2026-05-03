---
type: documentation
aliases:
  - AI Agents Guide
  - Gemini Codex Guide
description: "Technical guide for non-Claude AI coding agents (Gemini CLI, Codex, Cursor, Windsurf). Simplified and portable version of CLAUDE.md. Reference when any AI agent other than Claude Code is operating in the CMDS vault."
author:
  - "[[구요한]]"
date created: 2026-01-02T16:30
date modified: 2026-05-03
tags:
  - CMDS
  - system
audience: Gemini CLI, Codex, Cursor, Windsurf
scope: technical-implementation
precedence: 2
memory-type: feedback
required-for:
  - code-generation
  - file-creation
  - file-editing
optional-for:
  - search
  - analysis
token-estimate: 3200
CMDS: "[[📚 501 Obsidian]]"
index: "[[🏛 CMDS Head Quarter]]"
version: "2.5"
status: completed
changelog:
  - "2.5 (2026-05-03): Added Antigravity 03-7/03-8 output lanes for symmetry with Claude Code/OpenClaw/Codex. ANTIGRAVITY.md now full system file (precedence 3) — see [[ANTIGRAVITY.md]] for Gemini-specific notes."
  - "2.4 (2026-05-03): Codex MBP/Studio output lanes, Codex command/tool mapping, .agents skill registry, qmd refresh fallback, and description double-quote backfill added."
  - '2.3 (2026-04-23): description 필드 double-quote 강제 규칙 추가 — YAML plain scalar의 ": " 금지로 Obsidian Properties 렌더 깨짐 방지 (Essential 섹션 반영, frontmatter-standard rule #7 준거).'
  - "2.2 (2026-04-20): Project Overview 정정 — 사용자 포지셔닝(개인사업자/법인 신설 준비/박사 논문 중단/LG 임원·회장단 교육/4대 초점) 반영."
  - "2.1 (2026-04-07): 필수 프로퍼티 7개로 확장 (description 추가, English required)"
  - "2.0 (2026-04-01): @include 기반 공통 규칙 분리, 중복 60% 제거"
  - "1.0 (2026-03-30): 초기 버전, frontmatter 표준 추가"
---
> **🔄 Last Updated: 2026-05-03** | Backup: `40. Docs/47. CMDS Docs/cmds-system-files/AGENTS_backup.md` | Public: [system.cmdspace.work](https://system.cmdspace.work) (Vercel `cmds-system-files-v2`, deployed from `/Users/yohankoo/DEV/cmds-system-files/`)

# AGENTS.md

This file provides guidance to AI coding agents (Codex, Cursor, Windsurf, etc.) when working with this Obsidian vault. **Google Gemini / Antigravity 사용 시에는 [[ANTIGRAVITY.md]] 가 우선** 참조됨.

> **📌 Related System Files (8 System Files)** — precedence 순서대로 로드, audience 별 그룹
>
> **🤖 LLM Coding Agents** (always-loaded technical context):
> - @CLAUDE.md → [[CLAUDE.md]] — Claude Code specific (precedence: 1)
> - @AGENTS.md → [[AGENTS.md]] — This file: Codex, Cursor, Windsurf 등 일반 AI agent (precedence: 2)
>
> **🧪 Vendor-Specific Agent**:
> - @ANTIGRAVITY.md → [[ANTIGRAVITY.md]] — Google Gemini / Antigravity IDE 전용 (precedence: 3)
>
> **📚 Context & Standards** (referenced by all agents):
> - @CMDS.md → [[CMDS.md]] — System philosophy & user context (precedence: 4)
> - @🏛 CMDS Guide → [[🏛 CMDS Guide]] — Standards & templates (precedence: 5)
> - @🏛 CMDS Head Quarter → [[🏛 CMDS Head Quarter]] — Navigation hub (precedence: 6)
>
> **🧠 Gobi Persona System** (Gobi 앱 entry point — *외부 LLM coding agent 아님*):
> - @BRAIN.md → [[BRAIN.md]] — 구요한 brain profile (사람을 기술하는 grounding source) (precedence: 7)
> - @BRAIN_PROMPT.md → [[BRAIN_PROMPT.md]] — Agent Rules of Engagement (BRAIN.md 사용 메타 지침) (precedence: 8)

---

## Project Overview

This is an Obsidian vault for the **CMDSPACE (커맨드스페이스)** knowledge management system operated by 구요한 (Yohan Koo). CMDSPACE is currently a **sole proprietorship transitioning to a formal corporation**. The operator's primary work is **business + education** (notably LG executive and chairman-group training); dissertation writing for his PhD (ABD) is currently paused.

The vault implements the CMDS framework — a comprehensive Personal Knowledge Management (PKM) system with 9 major categories (100-900 series). The operator is simultaneously researching and teaching four current focus axes: (1) Obsidian-based PKM, (2) System Files infrastructure, (3) LLM Wiki satellite vault, (4) 9Yohan multi-agent system. See [[CMDS.md]] for full context.

**Vault Scale**: 10,000+ notes, 120+ plugins, 90+ templates

### Working Environments & Sync
Two Macs are synced via **Obsidian Sync** (official Obsidian cloud server). All subfolders and files are kept identical.

| Environment | Machine | Base Path |
|-------------|---------|-----------|
| Primary | MacBook Pro (16-inch) | `/Users/yohankoo/Local Obsidian_MBP/CMDSPACE_Local_MBP` |
| Secondary | Mac Studio | `/Users/yohankoo/Obsidian_Local/CMDSPACE_Studio_Local_Org` |

### AI Agent Output Lanes

All code-related outputs start under `00. Inbox/03. AI Agent/` and are separated by agent + machine:

| Subfolder | Agent | Machine |
|-----------|-------|---------|
| `03-1. Claude Code (MBP)/` | Claude Code | MacBook Pro |
| `03-2. Claude Code (Studio)/` | Claude Code | Mac Studio |
| `03-3. OpenClaw (MBP)/` | OpenClaw | MacBook Pro |
| `03-4. OpenClaw (Studio)/` | OpenClaw | Mac Studio |
| `03-5. Codex (MBP)/` | Codex | MacBook Pro |
| `03-6. Codex (Studio)/` | Codex | Mac Studio |
| `03-7. Antigravity (MBP)/` | Antigravity (Google) | MacBook Pro |
| `03-8. Antigravity (Studio)/` | Antigravity (Google) | Mac Studio |

### Public Deployment
- **Web**: https://system.cmdspace.work (8 system files 중 공개 가능한 5개 + rules + ZIP. ANTIGRAVITY/BRAIN/BRAIN_PROMPT 3개는 vendor·product 전용이라 미배포)
- **Hosting**: Vercel — team `johnfkoo951's projects`, project **`cmds-system-files-v2`** (Project ID: `prj_CDfy1Qhc2WmxI2nj76w0EJv3zq8h`)
- **DNS**: Cloudflare (`cmdspace.work` zone) — A record `system → 76.76.21.21`, proxy OFF
- **DEV source folder**: `/Users/yohankoo/DEV/cmds-system-files/`
- **Deploy command** (from DEV folder): `vercel deploy --prod --yes`
- **GitHub repo**: https://github.com/johnfkoo951/cmds-system-files — code backup only, **not connected to Vercel auto-deploy**
- Details & sync skill: see `[[CLAUDE.md]]` → "📦 System Files Deployment" section

---

<!-- STATIC: 아래 규칙은 거의 변경되지 않습니다 -->

## Critical Rules

> 공통 규칙은 `.claude/rules/` 에 정의되어 있습니다. 아래는 AI 에이전트가 반드시 따라야 할 핵심 규칙입니다.

@.claude/rules/indentation-rules.md

@.claude/rules/frontmatter-standard.md

@.claude/rules/wikilink-rules.md

@.claude/rules/blank-line-rules.md

@.claude/rules/file-creation-rules.md

@.claude/rules/video-project-workflow.md

---

## Essential (Post-Compact)

> 컨텍스트 압축 후에도 반드시 기억해야 할 핵심 규칙:
> 1. **YAML frontmatter: 2 SPACES** / **Markdown body: TAB**
> 2. **Wikilinks in YAML: 반드시 큰따옴표** `"[[link]]"`
> 3. **코드 출력 경로**: `00. Inbox/03. AI Agent/{환경 하위폴더}/` — Codex on MBP uses `03-5. Codex (MBP)/`, Codex on Studio uses `03-6. Codex (Studio)/`
> 4. **필수 프로퍼티 7개**: type, aliases, **description** (English, 1-2 sentences for LLMs), author, date created, date modified, tags
> 5. **`description` 은 항상 double-quote `"..."`**: 안에 `: ` 또는 ` #` 들어가면 YAML plain scalar 파서 깨짐 → Obsidian Properties 렌더 실패
> 6. **날짜 포맷**: ISO 8601 (YYYY-MM-DD)
> 7. **빈 줄 최소화 (Obsidian-tight)**: 헤딩→sub-heading, 헤딩→콘텐츠, 리스트 끝→다음 헤딩 사이 빈 줄 X. `---` / `##` 단락 분리에만 빈 줄 허용
> 8. **파일 참조 3종 결정 트리**: vault 내부 .md → `[[wikilink]]` (default · 이모지 prefix 정확히) · 에이전트 자동 로드 필요 → `@path/to/file.md` · vault 외부 경로/코드 → 백틱. 인라인 코드로 vault 내부 .md 쓰면 wikilink 깨짐. 자세한 결정 트리는 `.claude/rules/wikilink-rules.md`

---

## Directory Structure & CMDS Categories

@.claude/rules/directory-structure.md

---

## Codex Operating Notes

Codex can work in this vault, but it should treat Claude-specific files as portable workflow specs rather than literal tool calls.

### Rule Loading

`@path/to/file.md` is a Claude Code import convention. Codex must explicitly read the relevant rule files before editing, especially:

- `.claude/rules/indentation-rules.md`
- `.claude/rules/frontmatter-standard.md`
- `.claude/rules/wikilink-rules.md`
- `.claude/rules/blank-line-rules.md`
- `.claude/rules/file-creation-rules.md`
- `.claude/rules/directory-structure.md`

For video or Remotion-like work, also read `.claude/rules/video-project-workflow.md`.

### Codex Output Path

When Codex creates code, scripts, generated artifacts, or multi-file project work:

| Current vault path | Codex output lane |
|--------------------|-------------------|
| `/Users/yohankoo/Local Obsidian_MBP/CMDSPACE_Local_MBP` | `00. Inbox/03. AI Agent/03-5. Codex (MBP)/` |
| `/Users/yohankoo/Obsidian_Local/CMDSPACE_Studio_Local_Org` | `00. Inbox/03. AI Agent/03-6. Codex (Studio)/` |

For multi-file projects, create an intermediate folder inside that lane: `YYYY-MM-DD-project-name/`.

### Claude Command Mapping for Codex

The files in `90. Settings/94. Agent Settings/claude/commands/` are still the canonical CMDS Process specs. Codex should read them and translate the tool names as follows:

| Claude command/tool phrase | Codex equivalent |
|----------------------------|------------------|
| `Read`, `Glob`, `Grep`, `LS`, `Bash` | Use shell commands such as `sed`, `find`, `rg --files`, `rg`, and ordinary command execution. Prefer `rg` for search. |
| `Write`, `Edit`, `MultiEdit` | Use Codex `apply_patch` for manual file edits. |
| `AskUserQuestion` | Ask a concise plain-text question only when needed. If the answer is reasonably inferable, proceed and state the assumption. |
| `mcp__qmd__query` | Use `qmd query`, `qmd search`, or `qmd vsearch` with `-c <collection>` as appropriate. |
| `mcp__qmd__get` | Use `qmd get <file>[:line]` or read the local file directly when the path is known. |
| `Skill(...)` | Prefer Codex-visible skills in `.agents/skills/`; if missing, read the Claude skill in `90. Settings/94. Agent Settings/claude/skills/` as reference and execute manually. |

### qmd Refresh

Claude Code runs a PostToolUse hook after `Write`/`Edit` to refresh qmd. Codex edits may not trigger that hook, so after meaningful Markdown changes run:

```bash
qmd update && qmd embed
```

If this is too slow for the current task, at minimum report that qmd refresh was skipped.

### Skill Registry

- Codex-native skills live in `.agents/skills/`.
- Claude Code skills live in `90. Settings/94. Agent Settings/claude/skills/` and are exposed through `.claude/skills`.
- If the same skill exists in both places and contents differ, Codex should use `.agents/skills/` for execution and consult the Claude version only for historical context.
- Do not silently synchronize skill files across registries unless the user asks for a sync.

---

## Obsidian Wikilinks

```markdown
[[Note Name]]              # Basic link
[[Note Name|Display Text]] # Aliased link
[[Note Name#Heading]]      # Heading link
[[Note Name^block-id]]     # Block link
![[Note Name]]             # Embed file
![[image.png]]             # Embed image
```

---

<!-- DYNAMIC: 아래 내용은 주기적으로 갱신됩니다 -->

## Common Note Types

- `note` - General notes
- `terminology` - Term definitions
- `meeting` - Meeting minutes
- `people` - People profiles
- `curriculum` - Course curriculum
- `channel` - YouTube/Blog/Newsletter 채널 프로필
- `CMDS` - CMDS index pages (replaces traditional MOC concept)
- `documentation` - Technical docs

## Status Values

Standard status values (5 options):
- `unread` - Not yet processed
- `reading` - Currently reading
- `inProgress` - Work in progress
- `completed` - Finished
- `archived` - Historical reference

## File Prefixes

- 📎 - Web Clips
- 🏷 - Index pages
- 📦 - Reviews
- 🔖 - Personal outputs
- 📜 - Others' outputs
- 📈 - Code/Syntax
- 🎹 - Music
- 📘 - Books/Reference

## Templates

Templates are in `90. Settings/91. Templates/`. Key templates:

- `Template_00. Basic Note.md`
- `Template_01. Daily Note.md`
- `Template_05. Meeting Minutes.md`
- `Template_20. Research Note.md`
- `Template_51. People.md`

---

## CMDS Process Command Suite (2026-04-14+)

The mothership has 8 slash commands aligned with the **CMDS Process** (Connect → Merge → Develop → Share). Implementation lives in `.claude/commands/` (symlinked to `90. Settings/94. Agent Settings/claude/commands/`). If your agent runtime supports Claude Code-compatible slash commands, you can invoke these directly; otherwise, treat them as workflow documentation for how the user thinks about vault operations.

### Stage commands (the 4-stage knowledge lifecycle)

| Command | Stage | Fan | Role |
|---------|-------|-----|------|
| `/connect` | Connect (📖 100 Themes) | 1→1 | Inbox item → Theme stub. Auto-classifies into interest/topic/variable/terminology. Low-friction. |
| `/merge` | Merge (📖 200 Literature) | N→1 | Multiple notes → one synthesized Literature note. Heaviest command; multi-dialog flow. |
| `/develop` | Develop (📖 300-600) | 1→1 | Apply method, build artifact (code/prompt/curriculum/specialty). Code goes to `00. Inbox/03. AI Agent/` first. |
| `/share` | Share (📖 700-800) | 1→N | Orchestrate to existing skills (`thebetter-writer`, `markdown-slides`, etc.). Never writes content directly. |

### Cross-cutting utilities

| Command | Role |
|---------|------|
| `/inbox` | Scan 9 inbox subfolders, route to stage command. **Read-only, router only.** |
| `/lint {scope}` | Health check by stage scope (inbox/connect/merge/develop/share/all). Read-only. |
| `/query` | Search vault + LLM Wiki, synthesize answer, file back to appropriate CMDS category (NOT a separate folder). |
| `/status` | One-screen stage snapshot + recommended next action. Zero dialogs. |

### When to use which

```
세션 시작 / 뭐 할지 모름             → /status
방대한 inbox에서 시작                → /inbox → 라우팅
inbox 항목 빠르게 등록               → /connect
여러 노트 합성해서 한 노트로         → /merge
방법론 적용 / 코드·프롬프트 생성     → /develop
기존 합성 → 외부 산출물              → /share
볼트에 질문 (자신의 글 + LLM Wiki)   → /query
위생 점검 (모순/orphan/stale)        → /lint
```

### Key design decisions (inherited conventions)

- **CMDS Process is the operational vocabulary** — not LLM Wiki's ingest/query/lint triad. Stay in the user's framework.
- **`/inbox` and `/share` never write directly** — `/inbox` is a router, `/share` is an orchestrator.
- **`/query` results are NOT folder-isolated** — they classify into the appropriate CMDS category (usually `220 Personal Insights`, `210 Literature Reviews`, `5XX Product`) and save to `30. Permanent Notes/` or similar. There is no `30. Queries/` folder. User policy: "내 모든 노트가 쿼리의 소재이고 결과".
- **CMDS categorization is metadata, not folders**: notes live in existing folder structure (`30. Permanent Notes/`, `60. Collections/`, etc.) and are categorized via `CMDS:` and `index:` frontmatter.
- **New v2 frontmatter fields** introduced by commands: `mergePurpose`, `sourceNotes`, `mainVaultRelated`, `developSources`, `shareSourceNotes`, `shareFormat`, `sharePurpose`, `queryOrigin`, `querySources`, `sourceInbox`. Use camelCase per frontmatter standard.
- **User dialog tool**: commands use `AskUserQuestion` MCP tool (if available to your agent) with `multiSelect` where applicable, max 4 options, always `(Recommended)` first.

### For agents without slash command support

If your runtime doesn't execute `/connect` etc. directly, you can still:

1. Read the command file (`90. Settings/94. Agent Settings/claude/commands/{name}.md`) to understand the expected workflow.
2. Execute the workflow manually using standard tool calls (Read, Write, Edit, Glob, Grep).
3. Follow the same frontmatter conventions and user-dialog checkpoints the command specifies.

The commands are self-contained markdown — each `.md` file is both the spec and the prompt.

---

## Companion Vaults (간이)

이 mothership 외에 **6 companion vault** 가 존재. 다른 governance 모델로 운영. 자세한 내용은 [[CLAUDE.md]] § Companion Vaults 또는 satellite 의 [Multi-Vault Architecture](obsidian://open?vault=CMDS_LLM_Wiki&file=20.%20Wiki%2F23.%20Guides%2FMulti-Vault%20Architecture) 참조.

| Type | Vault | 멤버 | Purpose |
|------|-------|------|---------|
| Solo (LLM compile) | `CMDS_LLM_Wiki` | 구요한 + LLM | 학습·연구·정리 지식 |
| Solo (제품) | `CMDS_Gobi` | 구요한 | 고비 스페이스/데스크탑 개인 사용 |
| Pair | `CMDS_JoonLab` | 구요한 + 박준 | 교육·강의·컨설팅·코칭 |
| Pair | `CMDSPACE_Admin` | 구요한 + 이태극 | 운영 총괄 |
| Team (5인) | `GOBI` | 구요한·이태극·김진영·강민석·Greg Moon | 커맨드스페이스 × 고비 팀 |
| Distribution | `cmds-vault` | 구요한 → 외부 | CMDS 스타터킷 |

**Cross-vault wikilink 불가** — 다른 vault 참조 시 `obsidian://open?vault=...&file=...` URL 사용.

**Governance 결정 트리**: 새 자료가 들어오면 *누가 합의 권한 가짐?* 을 먼저 묻고 → 적절한 vault 선택. 자세한 내용은 satellite 가이드.

## Important Notes

1. **Use wikilinks `[[]]`** for internal references, NOT markdown links
2. **Respect existing patterns** - This is a mature vault with established conventions
3. **Check [[CMDS.md]]** for user context and workflow patterns
4. **Check [[🏛 CMDS Guide]]** for detailed standards and templates
5. **Check [Multi-Vault Architecture](obsidian://open?vault=CMDS_LLM_Wiki&file=20.%20Wiki%2F23.%20Guides%2FMulti-Vault%20Architecture)** for cross-vault decisions and member-to-vault mapping

---

**For Claude Code**: See [[CLAUDE.md]] for Claude-specific instructions.
**For LLM Context**: See [[CMDS.md]] for system philosophy and user profile.
**For Search Methods**: See [Wiki Search Methods Comparison](obsidian://open?vault=CMDS_LLM_Wiki&file=20.%20Wiki%2F23.%20Guides%2FWiki%20Search%20Methods%20Comparison) (canonical, satellite-side).
**For Vault Architecture**: See [Multi-Vault Architecture](obsidian://open?vault=CMDS_LLM_Wiki&file=20.%20Wiki%2F23.%20Guides%2FMulti-Vault%20Architecture).

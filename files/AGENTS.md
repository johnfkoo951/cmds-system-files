---
type: documentation
aliases:
  - AI Agents Guide
  - Non-Claude Agents Guide
description: "Technical guide for non-Claude AI coding agents (Codex, Cursor, Windsurf; Gemini/Antigravity should prefer ANTIGRAVITY.md and treat this file as fallback). Simplified and portable version of CLAUDE.md. Reference when any AI agent other than Claude Code is operating in the CMDS vault."
author:
  - "[[구요한]]"
date created: 2026-01-02T16:30
date modified: 2026-09-16
tags:
  - CMDS
  - system
audience: Codex, Cursor, Windsurf (Gemini/Antigravity 는 ANTIGRAVITY.md 우선 — 이 파일은 fallback)
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
token-estimate: 8500
CMDS: "[[📚 501 Obsidian]]"
index: "[[🏛 CMDS Head Quarter]]"
version: "2.16"
status: completed
changelog:
  - "2.16 (2026-09-16): frontmatter 로컬 탐색에 실제 발급·대상 확인한 Hookmark URI를 적용하고 공통 프로필 묶음을 1.0.1로 갱신. 기존 필드명·legacy 값·Raw 원문과 본문/manifest의 재현 경로를 보존."
  - "2.15 (2026-09-14): I01 공통 필드·Main/Wiki 프로필 v1.0.0과 읽기 전용 resolver 진입점을 추가. 프로필 선택과 실제 콘텐츠 검증을 구분하며 기존 훅·템플릿 집행과 레거시 노트는 보존."
  - "2.14 (2026-09-09): 완료된 개발·검토 JSON/PY의 볼트 외부 보관과 메인 MD의 기획·경로·재개 기록을 연결. 초기 Inbox와 완료 보관을 구분하며 file-creation-rules의 종료 절차를 정본으로 사용. 과거 자료 일괄 이관·공개 배포는 별도."
  - "2.13 (2026-09-08): Git 저장소 상태를 현재 MBP에서 확인하고 scoped Git 검사와 filesystem parity를 함께 안내. Claude symlink 정본 경로 검사와 명시 파일 날짜 검사 진입점을 추가. 다른 운영 계약·기존 changelog는 보존."
  - "2.12 (2026-08-29): CMDS Process 커맨드 8 → 10 — `/seeds`·`/harvest` 를 Cross-cutting utilities 표와 결정 트리에 등록. Codex/Fugu 는 `.codex/commands/` · `.agents/skills/` 미러가 아직 없으므로 Claude 커맨드 스펙을 워크플로 문서로 참조할 것 (3-place parity 미완 — 후속 작업)."
  - "2.11 (2026-08-27): Cross-vault 상호참조 표준 반영 (macro v4.10.2) — v2 frontmatter 필드 목록에 wikiVaultRelated 추가 (advanced-uri 형식, 역방향은 mainVaultRelated). 정본은 wikilink-rules.md §6."
  - "2.10 (2026-08-17): Periodic agent notes 섹션 신설 (macro v4.10.0) — /daily·/weekly 는 Claude Code 스케줄 전용임을 명시, 타 에이전트 규칙 3종 (재생성 금지·사람 영역 불변+dailyStatus 확인·model/effort frontmatter 기록) 추가."
  - "2.9 (2026-07-02): 전수 감사 픽스 세트 (macro v4.9.3) — (a) frontmatter audience/aliases/description 에서 Gemini CLI 선두 표기 제거 (ANTIGRAVITY.md 우선·본 파일 fallback 관계 명시), (b) 백틱 감싼 CLAUDE.md wikilink 정정 (자기 규칙 위반), (c) /inbox 서브폴더 하드카운트 제거, (d) Rule Loading 목록에 mermaid-rules.md 추가, (e) Guide/HQ @import 표기 wikilink 로 정정, (f) token-estimate 3200→8500 실측화, 배너 동기화."
  - "2.8 (2026-07-02): Codex & Codex-Fugu compatibility pass — added `.codex/` runtime layer (README + hooks.json + qmd-reindex.sh + 8 command adapters) and `.agents/skills/` Fugu wrappers for all 8 CMDS Process operations. New AGENTS.md sections: Runtime Entrypoints, Cross-Agent Operation Map, Runtime Compatibility Matrix, Multi-Agent Orchestration. Clarified hooks are manual in Codex/Fugu and wikilinks resolve to paths."
  - "2.7 (2026-05-30): v4.9.0 pass — added Pre-Flight Checklist + mermaid-rules import + DESIGN visual-artifact trigger; note-types/template-count aligned."
  - "2.6 (2026-05-22): 8→9 system files 전환 — DESIGN.md (precedence 9, Visual Language tier) 추가. Related System Files 표를 9-file 로 갱신. 공개 배포 카운트 5→6 갱신."
  - "2.5 (2026-05-03): Added Antigravity 03-7/03-8 output lanes for symmetry with Claude Code/OpenClaw/Codex. ANTIGRAVITY.md now full system file (precedence 3) — see [[ANTIGRAVITY.md]] for Gemini-specific notes."
  - "2.4 (2026-05-03): Codex MBP/Studio output lanes, Codex command/tool mapping, .agents skill registry, qmd refresh fallback, and description double-quote backfill added."
  - '2.3 (2026-04-23): description 필드 double-quote 강제 규칙 추가 — YAML plain scalar의 ": " 금지로 Obsidian Properties 렌더 깨짐 방지 (Essential 섹션 반영, frontmatter-standard rule #7 준거).'
  - "2.2 (2026-04-20): Project Overview 정정 — 사용자 포지셔닝(개인사업자/법인 신설 준비/박사 논문 중단/LG 임원·회장단 교육/4대 초점) 반영."
  - "2.1 (2026-04-07): 필수 프로퍼티 7개로 확장 (description 추가, English required)"
  - "2.0 (2026-04-01): @include 기반 공통 규칙 분리, 중복 60% 제거"
  - "1.0 (2026-03-30): 초기 버전, frontmatter 표준 추가"
---
> **🔄 Last Updated: 2026-09-16** | Backup: `40. Docs/47. CMDS Docs/cmds-system-files/AGENTS_backup.md` | Public: [system.cmdspace.work](https://system.cmdspace.work) (Vercel `cmds-system-files-v2`, deployed from `/Users/yohankoo/DEV/cmds-system-files/`)

# AGENTS.md

This file provides guidance to AI coding agents (Codex, Cursor, Windsurf, etc.) when working with this Obsidian vault. **Google Gemini / Antigravity 사용 시에는 [[ANTIGRAVITY.md]] 가 우선** 참조됨.

> **🧭 Codex & Codex-Fugu**: 이 볼트는 원래 Claude Code 중심으로 설계됐지만, 이제 Codex 네이티브 런타임 레이어(`.codex/`)와 Fugu 자동 발견 스킬 레지스트리(`.agents/skills/`)가 Claude 하네스를 미러한다. 진입점·자동화 차이는 아래 **Codex Operating Notes** 의 *Runtime Entrypoints*, *Cross-Agent Operation Map*, *Runtime Compatibility Matrix*, *Multi-Agent Orchestration* 섹션을 먼저 읽을 것. 개요는 `.codex/README.md`.

> **📌 Related System Files (9 System Files)** — precedence 순서대로 로드, audience 별 그룹
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
> - [[🏛 CMDS Guide]] — Standards & templates (precedence: 5 · 공백 포함 경로라 @import 불가 — 필요 시 명시 Read)
> - [[🏛 CMDS Head Quarter]] — Navigation hub (precedence: 6 · 공백 포함 경로라 @import 불가 — 필요 시 명시 Read)
>
> **🧠 Gobi Persona System** (Gobi 앱 entry point — *외부 LLM coding agent 아님*):
> - @BRAIN.md → [[BRAIN.md]] — 구요한 brain profile (사람을 기술하는 grounding source) (precedence: 7)
> - @BRAIN_PROMPT.md → [[BRAIN_PROMPT.md]] — Agent Rules of Engagement (BRAIN.md 사용 메타 지침) (precedence: 8)
>
> **🎨 Visual Language** (always-loaded when producing visual artifacts):
> - @DESIGN.md → [[DESIGN.md]] — Visual language spec (v4.3 standards · Anti-Slop · Skill↔Surface mapping) (precedence: 9)

---

## Project Overview

This is an Obsidian vault for the **CMDSPACE (커맨드스페이스)** knowledge management system operated by 구요한 (Yohan Koo). CMDSPACE is currently a **sole proprietorship transitioning to a formal corporation**. The operator's primary work is **business + education** (notably LG executive and chairman-group training); dissertation writing for his PhD (ABD) is currently paused.

The vault implements the CMDS framework — a comprehensive Personal Knowledge Management (PKM) system with 9 major categories (100-900 series). The operator is simultaneously researching and teaching four current focus axes: (1) Obsidian-based PKM, (2) System Files infrastructure, (3) LLM Wiki satellite vault, (4) 9Yohan multi-agent system. See [[CMDS.md]] for full context.

**Vault Scale**: 10,000+ notes, 120+ plugins, 100+ templates

### Working Environments & Sync
Two Macs are synced via **Obsidian Sync** (official Obsidian cloud server). All subfolders and files are kept identical.

| Environment | Machine | Base Path |
|-------------|---------|-----------|
| Primary | MacBook Pro (14-inch) | `/Users/yohankoo/Local Obsidian_MBP/CMDSPACE_Local_MBP` |
| Secondary | Mac Studio | `/Users/yohankoo/Obsidian_Local/CMDSPACE_Studio_Local_Org` |

### AI Agent Output Lanes

Vault-originated code outputs initially use `00. Inbox/03. AI Agent/`, separated by agent + machine. Existing DEV projects keep their workspace; completed JSON/PY follow the closeout rule below:

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
- **Web**: https://system.cmdspace.work (9 system files 중 공개 가능한 6개 [CLAUDE/AGENTS/CMDS/Guide/HQ/DESIGN] + rules + ZIP. ANTIGRAVITY/BRAIN/BRAIN_PROMPT 3개는 vendor·product 전용이라 미배포)
- **Hosting**: Vercel — team `johnfkoo951's projects`, project **`cmds-system-files-v2`** (Project ID: `prj_CDfy1Qhc2WmxI2nj76w0EJv3zq8h`)
- **DNS**: Cloudflare (`cmdspace.work` zone) — A record `system → 76.76.21.21`, proxy OFF
- **DEV source folder**: `/Users/yohankoo/DEV/cmds-system-files/`
- **Deploy command** (from DEV folder): `vercel deploy --prod --yes`
- **GitHub repo**: https://github.com/johnfkoo951/cmds-system-files — code backup only, **not connected to Vercel auto-deploy**
- Details & sync skill: see [[CLAUDE.md]] → "📦 System Files Deployment" section

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

@.claude/rules/mermaid-rules.md

---

## Essential (Post-Compact)

> 컨텍스트 압축 후에도 반드시 기억해야 할 핵심 규칙:
> 1. **YAML frontmatter: 2 SPACES** / **Markdown body: TAB**
> 2. **Wikilinks in YAML: 반드시 큰따옴표** `"[[link]]"`
> 3. **코드 초기 출력 경로**: `00. Inbox/03. AI Agent/{환경 하위폴더}/` — Codex MBP `03-5`, Studio `03-6`. 기존 DEV 프로젝트는 해당 위치 유지. 완료 JSON/PY는 외부 보관하고 기획·경로·재개는 메인 MD에 기록 (file-creation-rules의 Completed Artifact Closeout).
> 4. **필수 프로퍼티 7개**: type, aliases, **description** (English, 1-2 sentences for LLMs), author, date created, date modified, tags
> 5. **`description` 은 항상 double-quote `"..."`**: 안에 `: ` 또는 ` #` 들어가면 YAML plain scalar 파서 깨짐 → Obsidian Properties 렌더 실패
> 6. **날짜 포맷**: ISO 8601 (YYYY-MM-DD)
> 7. **빈 줄 최소화 (Obsidian-tight)**: 헤딩→sub-heading, 헤딩→콘텐츠, 리스트 끝→다음 헤딩 사이 빈 줄 X. `---` / `##` 단락 분리에만 빈 줄 허용
> 8. **파일 참조 3종 결정 트리**: vault 내부 .md → `[[wikilink]]` (default · 이모지 prefix 정확히) · 에이전트 자동 로드 필요 → `@path/to/file.md` · vault 외부 경로/코드 → 백틱. 인라인 코드로 vault 내부 .md 쓰면 wikilink 깨짐. 자세한 결정 트리는 `.claude/rules/wikilink-rules.md`

---

## Pre-Flight Checklist (Before Every Write/Edit)

Every time the agent creates or edits a `.md` file, verify:

- [ ] **YAML frontmatter uses 2 SPACES** (not tabs)
- [ ] **Markdown body uses TAB** (not spaces)
- [ ] **No unnecessary blank lines** between heading→sub-heading, heading→content, list end→next heading (Obsidian-tight)
- [ ] **Wikilinks in YAML are quoted**: `"[[link]]"` not `[[link]]`
- [ ] **File reference form is correct**: vault 내부 → `[[wikilink]]` (default, 이모지 prefix 정확히) · 에이전트 자동 로드 필요 → `@path/to/file.md` · vault 외부(`/DEV/`, `~/.claude/`) → 백틱. 인라인 코드로 vault 내부 .md 쓰지 말 것 (`.claude/rules/wikilink-rules.md` 참조)
- [ ] **Mermaid node/edge labels are quoted**: `A["label"]`, no `[/` start
- [ ] **Table has a blank line before it**: a sentence/list immediately followed by a `| ... |` row breaks rendering — insert one blank line between the lead-in line and the table header (see `.claude/rules/blank-line-rules.md`)
- [ ] **Arrays use proper format**: hyphen + space + value
- [ ] **Dates use ISO 8601**: `YYYY-MM-DD` format
- [ ] **`description` field present and in English**: 1-2 sentences explaining the note for LLMs
- [ ] **`description` wrapped in double quotes `"..."`**: unquoted `: ` or ` #` breaks YAML parser
- [ ] **Code output lifecycle checked**: 초기 볼트 작업은 Codex Inbox 레인, 기존 DEV 작업은 해당 프로젝트, 완료 JSON/PY는 Completed Artifact Closeout에 따라 외부 보관 + 메인 MD 기록
- [ ] **Filename follows convention**: `YYYY-MM-DD-description.ext`

---

### Shared field and vault profile entrypoint (I01)
공통 필드와 Main/Wiki별 적용 계약은 [[90. Settings/94. Agent Settings/schema/README|공통 필드와 볼트 프로필]]의 v1.0.1 묶음을 사용한다. 실제 파일 하나를 선택할 때 `ruby "90. Settings/94. Agent Settings/schema/resolve-profile.rb" --vault main --root "$PWD" --path "AGENTS.md"`처럼 볼트 루트와 파일을 명시한다. `--check-bundle`로 파일 해시와 버전을 확인할 수 있다.
`resolved`는 프로필 선택 성공이며 콘텐츠 validation PASS가 아니다. 템플릿 소스·runtime·일반 콘텐츠·시스템 예외를 구분하고, `needs_review`나 `error`를 검증 분모에서 숨기지 않는다. 기존 guard/description helper의 제한된 검사 계약과 AI 작성 기록을 유지한다. `schemaVersion`은 opt-in 메타데이터로 문서 `version`과 별개이며 기존 노트에 자동 추가하지 않는다. Wiki는 자체 Settings의 같은 버전 사본으로 실행하며 sibling 볼트 경로에 의존하지 않는다.

### System file date checks
For system files with version history, compare the calendar day of `date modified` and any `Last Updated` banner with the **latest dated changelog entry**. A date earlier than the latest entry needs review; an explanation mentioning another date is not a changelog entry date. Record the current edit separately and preserve earlier changelog entries. A metadata-only correction does not revalidate all facts in the document.

Run the read-only checker from the vault root with explicit file paths:

```bash
ruby "90. Settings/94. Agent Settings/claude/scripts/check-system-dates.rb" --require-history -- AGENTS.md CMDS.md ANTIGRAVITY.md
```

The checker prints per-file JSON: exit 0 means no detected date issue (inspect any `not_applicable` result), exit 1 means review is required, and exit 2 means input/read/YAML/date validation failed. `--require-history` requires the selected files to declare their history and banner. Without it, files that do not use these fields are reported as not applicable rather than receiving invented metadata. Use this check manually after relevant system edits; it does not install an automatic hook or verify Git state, external versions, deployment, or synchronization.

---

## Directory Structure & CMDS Categories

@.claude/rules/directory-structure.md

---

## Codex Operating Notes

Codex can work in this vault natively. As of 2026-07-02 there is a dedicated **`.codex/` runtime layer** and a **`.agents/skills/` Fugu-discoverable registry** that mirror the Claude Code harness, so **Codex (single agent)** and **Codex-Fugu (multi-agent orchestration)** run the same CMDS Process operations Claude Code runs. Claude-specific files remain the canonical specs; Codex treats them as portable workflow specs rather than literal tool calls, and prefers the `.codex/` / `.agents/` entrypoints below.

### Codex / Codex-Fugu Runtime Entrypoints

| Harness | Operation entrypoint | Skill discovery | Notes |
|---------|----------------------|-----------------|-------|
| Claude Code | `.claude/commands/{op}.md` (`/op`) | manual (command references) | PostToolUse hooks auto-run (`.claude/settings.json`) |
| Codex (single) | `.codex/commands/{op}.md` | manual | hooks are manual; ask user in plain text only when blocked |
| Codex-Fugu (multi-agent) | `.agents/skills/{op}/SKILL.md` (auto-discovered) + `.codex/commands/{op}.md` | **automatic** — `.agents/skills/*/SKILL.md` exposed as skills | workers never prompt the user; orchestrator reindexes once |

The 8 CMDS Process operations (`connect, merge, develop, share, inbox, lint, query, status`) exist in all three places. See `.codex/README.md` for the layer overview and the **Cross-Agent Operation Map** below for the parity table.

### Rule Loading

`@path/to/file.md` is a Claude Code import convention. Codex must explicitly read the relevant rule files before editing, especially:

- `.claude/rules/indentation-rules.md`
- `.claude/rules/frontmatter-standard.md`
- `.claude/rules/wikilink-rules.md`
- `.claude/rules/blank-line-rules.md`
- `.claude/rules/file-creation-rules.md`
- `.claude/rules/directory-structure.md`
- `.claude/rules/mermaid-rules.md`

For video or Remotion-like work, also read `.claude/rules/video-project-workflow.md`.

### Codex Output Path

Initial output lanes for vault-originated Codex code, scripts, generated artifacts, or multi-file work (existing DEV workspaces and video exceptions retain their locations):

| Current vault path | Codex output lane |
|--------------------|-------------------|
| `/Users/yohankoo/Local Obsidian_MBP/CMDSPACE_Local_MBP` | `00. Inbox/03. AI Agent/03-5. Codex (MBP)/` |
| `/Users/yohankoo/Obsidian_Local/CMDSPACE_Studio_Local_Org` | `00. Inbox/03. AI Agent/03-6. Codex (Studio)/` |

For multi-file projects, create an intermediate folder inside that lane: `YYYY-MM-DD-project-name/`.

**Completed artifacts:** Read [[90. Settings/94. Agent Settings/claude/rules/file-creation-rules|file-creation-rules]] → Completed Artifact Closeout. Maintenance code belongs in DEV; completed JSON/PY evidence goes to `/Users/yohankoo/DEV/_archive/vault-artifacts/` with its original vault/project mapping. Keep planning, results, actual paths, verification, and resume instructions in a main-vault MD. Archive state is separate from note status, knowledge promotion, Git/Sync, and deployment.

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

Claude Code runs a PostToolUse hook after `Write`/`Edit` to refresh qmd. **Codex CLI and Codex-Fugu do NOT auto-run hooks** — `.codex/hooks.json` mirrors `.claude/settings.json` for portability/documentation only. So after meaningful Markdown changes run:

```bash
qmd update && qmd embed
```

Or run the ready-made script: `.codex/hooks/qmd-reindex.sh`. In **Fugu, only the orchestrator** runs the reindex once per batch — parallel workers must not each reindex (duplicate/competing embeds). If this is too slow for the current task, at minimum report that qmd refresh was skipped. Mothership qmd collections: `mothership_inbox`, `mothership_cmds_process`, `mothership_literature`, `mothership_permanent`, `mothership_docs`, `mothership_assets`, `mothership_collections`, `mothership_outputs`, `mothership_references`, `mothership_settings`; the LLM Wiki satellite is collection `wiki`.

### Skill Registry

- Codex-native / Fugu-discoverable skills live in `.agents/skills/`. Fugu auto-exposes every `.agents/skills/*/SKILL.md`, so each CMDS Process operation has a thin wrapper skill there that points to its `.codex/commands/{op}.md` runtime spec.
- Claude Code skills live in `90. Settings/94. Agent Settings/claude/skills/` and are exposed through `.claude/skills`.
- If the same skill exists in both places and contents differ, Codex should use `.agents/skills/` for execution and consult the Claude version only for historical context.
- Do not silently synchronize skill files across registries unless the user asks for a sync.

### Cross-Agent Operation Map (8 CMDS Process operations)

When you add or change one of the eight operations below, edit its **three entrypoints** together (Claude command + Codex command + Fugu skill), then check both Git changes and filesystem parity.

- **Git state is independent of Obsidian's graph.** This MBP vault was confirmed as a Git working tree on 2026-09-08. At the start of each task, run `GIT_OPTIONAL_LOCKS=0 git rev-parse --show-toplevel` from the vault and confirm the returned root belongs to the intended repository. Other machines/checkouts must be checked separately.
- **Inspect only affected paths.** Use `GIT_OPTIONAL_LOCKS=0 git status --short -- <affected-paths>`, `git diff -- <affected-paths>`, `git diff --cached -- <affected-paths>`, and `git ls-files -- <affected-paths>`. Set `GIT_OPTIONAL_LOCKS=0` for these read-only inspections. Include existing staged and unstaged changes in the baseline.
- **Use physical Claude paths for content diffs.** Git tracks `.claude/commands` as a symlink; its target files are under `90. Settings/94. Agent Settings/claude/commands/`. Inspect the resolved canonical file as well as the link itself when relevant. A diff of `.claude/commands/{op}.md` alone can miss target content changes.
- **Also inspect the filesystem.** Confirm the canonical command, Codex adapter, and Fugu wrapper exist and agree on operation name, references, and shared behavior. Untracked/ignored files still require inspection. A clean diff or tracked-file list alone does not establish parity, and the three files need not have identical bytes.

| Operation | Fan | Codex command | Fugu skill | Claude mirror |
|-----------|-----|---------------|------------|---------------|
| connect | 1→1 | `.codex/commands/connect.md` | `.agents/skills/connect/SKILL.md` | `.claude/commands/connect.md` |
| merge | N→1 | `.codex/commands/merge.md` | `.agents/skills/merge/SKILL.md` | `.claude/commands/merge.md` |
| develop | 1→1 | `.codex/commands/develop.md` | `.agents/skills/develop/SKILL.md` | `.claude/commands/develop.md` |
| share | 1→N | `.codex/commands/share.md` | `.agents/skills/share/SKILL.md` | `.claude/commands/share.md` |
| inbox | router | `.codex/commands/inbox.md` | `.agents/skills/inbox/SKILL.md` | `.claude/commands/inbox.md` |
| lint | read-only | `.codex/commands/lint.md` | `.agents/skills/lint/SKILL.md` | `.claude/commands/lint.md` |
| query | 1→1 | `.codex/commands/query.md` | `.agents/skills/query/SKILL.md` | `.claude/commands/query.md` |
| status | read-only | `.codex/commands/status.md` | `.agents/skills/status/SKILL.md` | `.claude/commands/status.md` |

> **Parity note**: The canonical CMDS Process spec is still the Claude command file. The `.codex/commands/` file is its shell-first translation, and the `.agents/skills/` file is a thin Fugu wrapper that points back to the `.codex/` spec. Keep the operation name identical across all three.

### Runtime Compatibility Matrix (Claude Code · Codex · Codex-Fugu)

The three harnesses share the same operation names and schema, but runtime features (slash-command auto-load, hook auto-run, sub-agents) differ. This table defines what is automatic vs. a manual substitute in each runtime.

| Capability | Claude Code | Codex (single) | Codex-Fugu (multi-agent) |
|------------|-------------|----------------|--------------------------|
| Operation entrypoint | `.claude/commands/{op}.md` (`/op`) | `.codex/commands/{op}.md` | `.agents/skills/{op}/SKILL.md` (auto) + `.codex/commands/{op}.md` |
| Skill discovery | manual (command refs) | manual | **automatic** — `.agents/skills/*/SKILL.md` exposed |
| `[[wikilink]]` resolution | Obsidian graph | **no** → read as path | **no** → read as path |
| PostToolUse hook auto-run | ✅ `.claude/settings.json` | ❌ `.codex/hooks.json` = docs/manual | ❌ not auto-run |
| qmd reindex | hook auto (debounced) | manual: `qmd update && qmd embed` or `.codex/hooks/qmd-reindex.sh` | manual: **orchestrator once** (no per-worker reindex) |
| User prompts | `AskUserQuestion` | plain-text, only when blocked | **workers never prompt** — orchestrator only |
| Parallel sub-agents | `Task` sub-agent | none (single) | `spawn_agent` / `wait_agent` workers |
| Output lane | `03-1`/`03-2` | `03-5`/`03-6` | `03-5`/`03-6` |

> [!warning] Wikilinks do not resolve in Codex/Fugu
> `[[CMDS.md]]`, `[[DESIGN.md]]`, `[[AGENTS.md]]` etc. in any spec are Obsidian conveniences. Shell-based agents must read the **path**: root-level notes resolve to `./<name>.md`; vault notes are found with `rg --files` / `rg` / `qmd query`. Wikilinks written into YAML must still be quoted `"[[...]]"` per the frontmatter standard.

> [!warning] Hooks are manual in Codex/Fugu
> `.codex/hooks.json` mirrors the Claude `settings.json` schema but is **not** auto-invoked by Codex CLI or Fugu. After a write session, run `qmd update && qmd embed` (or `.codex/hooks/qmd-reindex.sh`) yourself. In Fugu, only the orchestrator runs it once.

### Multi-Agent Orchestration (Codex-Fugu)

Invariants for running multiple Fugu workers in parallel. Apply only to operations where fan-out is natural (e.g. a large `/lint` split by scope, a multi-format `/share`, or a multi-file `/develop`); single small operations should be done locally by the orchestrator.

- **Single-writer rule**: `index.md`/`log.md`-style shared files and any given note must be written by **one** agent. Either the orchestrator writes serially, or worker write-sets are **completely disjoint**. Two workers writing the same file corrupts it — workers return results, the orchestrator integrates. `/merge` is single-writer by nature (never fan out the synthesis write).
- **Generator ≠ Verifier**: the worker (or pass) that produced a note does not also verify/lint it. Assign verification to a separate `spawn_agent` worker to avoid rubber-stamping.
- **Gates are orchestrator/human only**: promoting an artifact out of the inbox lane, deleting notes, flipping status, raising confidence, or adding a new domain are not done automatically by workers — the orchestrator handles them after user confirmation.
- **Reindex once**: read-only fan-out first; qmd reindex happens last and only from the orchestrator.
- **Workers don't prompt the user**: only the orchestrator asks questions (plain text). Workers that hit ambiguity return a proposed decision for the orchestrator to confirm.
- **Disjoint write-sets for `/develop`**: decompose multi-file builds so each worker owns a distinct file/subfolder inside the Codex lane (`03-5`/`03-6`); the orchestrator merges. Use a git worktree/branch only if concurrent writes to the same tree are unavoidable.

---

## Visual Artifacts (DESIGN.md)

When producing any visual artifact — web page, PDF, slide deck, image, video, diagram — read [[DESIGN.md]] (precedence 9) BEFORE generating and obey its CI color tokens (`#134538` green / `#E985A2` pink), SF Pro + Pretendard fonts, and the Anti-AI-Slop negative list.

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
- `research-pipeline` - Research pipeline documents
- `api` - API documentation
- `moc` - Map of Content
- `manuscript` - Manuscripts and drafts
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

The mothership has 10 slash commands aligned with the **CMDS Process** (Connect → Merge → Develop → Share). Canonical implementation lives in `.claude/commands/` (symlinked to `90. Settings/94. Agent Settings/claude/commands/`). Codex-native runtime translations live in `.codex/commands/{op}.md`, and Fugu-discoverable wrappers live in `.agents/skills/{op}/SKILL.md` (see **Cross-Agent Operation Map** above). If your agent runtime supports Claude Code-compatible slash commands, you can invoke these directly; Codex should use its `.codex/` / `.agents/` entrypoints; otherwise, treat them as workflow documentation for how the user thinks about vault operations.

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
| `/inbox` | Scan 00. Inbox/ subfolders, route to stage command. **Read-only, router only.** |
| `/lint {scope}` | Health check by stage scope (inbox/connect/merge/develop/share/all). Read-only. |
| `/query` | Search vault + LLM Wiki, synthesize answer, file back to appropriate CMDS category (NOT a separate folder). |
| `/status` | One-screen stage snapshot + recommended next action. Zero dialogs. |
| `/seeds` | Harvest title-only seed notes → separate seed/residue/how-to, cluster, propose angles, build 📚 101/102 hubs. Mothership-only. |
| `/harvest` | Cross-vault harvest over all 7 vaults — unlinked pairs, seeds already compiled in the wiki, wiki orphans, concept drift. Read-only on companion vaults. |

### When to use which

```
세션 시작 / 뭐 할지 모름             → /status
방대한 inbox에서 시작                → /inbox → 라우팅
inbox 항목 빠르게 등록               → /connect
여러 노트 합성해서 한 노트로         → /merge
방법론 적용 / 코드·프롬프트 생성     → /develop
기존 합성 → 외부 산출물              → /share
볼트에 질문 (자신의 글 + LLM Wiki)   → /query
제목만 걸어둔 씨앗 → 글감·허브        → /seeds
볼트 생태계 전체 교차 수확           → /harvest
위생 점검 (모순/orphan/stale)        → /lint
```

### Periodic agent notes (/daily · /weekly) — 2026-08-17+

시간 축 기록(데일리·위클리)은 **Claude Code 가 OmniControl 스케줄로 작성하는 에이전트 노트**다: `/daily` (매일 draft 21:23 + finalize 04:53 — 하루의 경계는 04:00 KST, 자정 이후 작업은 전날 노트에 편입) · `/weekly` (매주 일 21:41). 다른 에이전트 규칙:

1. 이 노트들을 재생성하지 말 것 (스케줄 잡이 담당).
2. 데일리 노트를 수정해야 하면 **사람 영역 불변** (`## 사람 한 줄`, To Do 의 사람 체크박스, `## Log`) + **템플릿 재삽입 금지** — frontmatter `dailyStatus:` (pending/filled/final) 로 상태 확인.
3. 에이전트가 볼트 노트를 작성·대필할 땐 frontmatter 에 `model:` + `effort:` 로 작성 모델을 기록 (`.claude/rules/frontmatter-standard.md` Optional Properties).

정본 스펙: `.claude/commands/daily.md` · `.claude/commands/weekly.md` · 템플릿 `90. Settings/91. Templates/Template_01. Daily Note.md`.

### Key design decisions (inherited conventions)

- **CMDS Process is the operational vocabulary** — not LLM Wiki's ingest/query/lint triad. Stay in the user's framework.
- **`/inbox` and `/share` never write directly** — `/inbox` is a router, `/share` is an orchestrator.
- **`/query` results are NOT folder-isolated** — they classify into the appropriate CMDS category (usually `220 Personal Insights`, `210 Literature Reviews`, `5XX Product`) and save to `30. Permanent Notes/` or similar. There is no `30. Queries/` folder. User policy: "내 모든 노트가 쿼리의 소재이고 결과".
- **CMDS categorization is metadata, not folders**: notes live in existing folder structure (`30. Permanent Notes/`, `60. Collections/`, etc.) and are categorized via `CMDS:` and `index:` frontmatter.
- **New v2 frontmatter fields** introduced by commands: `mergePurpose`, `sourceNotes`, `wikiVaultRelated` (mothership→wiki cross-vault link, advanced-uri 형식 — 2026-08-27 표준, 정본 `.claude/rules/wikilink-rules.md` §6; 역방향 위키→mothership 은 `mainVaultRelated`), `developSources`, `shareSourceNotes`, `shareFormat`, `sharePurpose`, `queryOrigin`, `querySources`, `sourceInbox`. Use camelCase per frontmatter standard.
- **User dialog tool**: commands use `AskUserQuestion` MCP tool (if available to your agent) with `multiSelect` where applicable, max 4 options, always `(Recommended)` first.

### For agents without slash command support

**Codex / Codex-Fugu**: use the native entrypoints first — `.codex/commands/{name}.md` (single agent) or the auto-discovered `.agents/skills/{name}/SKILL.md` (Fugu). They already translate Claude tool calls to shell + `apply_patch` + `qmd`.

If your runtime doesn't execute `/connect` etc. directly and has no `.codex/` layer, you can still:

1. Read the command file (`.codex/commands/{name}.md`, or the canonical `90. Settings/94. Agent Settings/claude/commands/{name}.md`) to understand the expected workflow.
2. Execute the workflow manually using standard tool calls (shell `rg`/`sed`/`find`, `apply_patch`, `qmd`).
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

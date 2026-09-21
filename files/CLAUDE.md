---
type: documentation
aliases:
  - Claude Code Guide
  - CC System File
description: "Claude Code specific technical implementation guide. Defines file creation/editing rules, YAML/Markdown indentation rules, vault commands, and code output paths. Reference when Claude Code is writing or modifying code in the CMDS vault."
author:
  - "[[구요한]]"
date created: 2025-09-27T17:53
date modified: 2026-09-21
tags:
  - CMDS
  - system
audience: Claude Code
scope: technical-implementation
precedence: 1
memory-type: feedback
required-for:
  - code-generation
  - file-creation
  - file-editing
optional-for:
  - search
  - analysis
  - reading
token-estimate: 14500
CMDS: "[[📚 501 Obsidian]]"
index: "[[🏛 CMDS Head Quarter]]"
version: "4.11"
status: completed
changelog:
  - "4.11 (2026-09-21): project-scope(`<vault>/.claude/`)와 user-scope(`~/.claude/`)를 별개 계층으로 명시하고, 볼트 밖에서도 쓰는 자산은 볼트를 정본으로 두고 user-scope 를 symlink 하는 절차를 추가. 배경: 9Yohan 에이전트 9개가 user-scope 일반 폴더에 있어 Obsidian Sync·git 어디에도 들어가지 않은 채 MBP 로컬에만 존재했다. 절차 정본은 directory-structure.md. token-estimate 12500→14500 재실측. 부수 정정: rules 카운트 8 → 9 (file-move-rules.md 누락, 3곳)."
  - "4.10 (2026-09-09): 완료된 개발·검토 JSON/PY의 볼트 외부 보관과 메인 MD의 기획·경로·재개 기록을 연결. 초기 Inbox와 완료 보관을 구분하며 file-creation-rules의 종료 절차를 정본으로 사용. 과거 자료 일괄 이관·공개 배포는 별도."
  - "4.9 (2026-08-29): CMDS Process 커맨드 8 → 10 확장 — `/seeds` (제목만 걸어둔 씨앗 노트를 씨앗/잔해/How-to 로 분류·클러스터링 → 글감 제안 + 📚 101 Interests / 📚 102 Topics 허브 생성, 마더십 전용) 와 `/harvest` (7볼트 생태계 교차 수확 — 끊긴 쌍·이미 컴파일된 씨앗·위키 고아·개념 drift, companion 볼트는 읽기 전용) 신설. Command Map 표·결정 트리 갱신. 배경: /lint all 에서 제목만 있는 노트 833건(인바운드 있는 47 / 없는 786)이 확인됐고, 이는 결함이 아니라 의도적 백로그이므로 read-only 진단인 lint 가 아니라 전용 생성 커맨드가 담당하도록 분리."
  - "4.8 (2026-08-27): Cross-vault 상호참조 표준 도입 (macro v4.10.2) — wikiVaultRelated(모선→위키)/mainVaultRelated(위키→모선) 방향별 필드 + advanced-uri 마크다운 링크 표준 + 플러그인 부재 시 obsidian://open 폴백. Cross-Vault Reference Convention 섹션·인용 표기·v2 필드 목록 갱신. 정본은 wikilink-rules.md §6. tags inline 회귀 복원 (6번째 재발)."
  - "4.7 (2026-08-22): 데일리·위클리 로그 이관 (macro v4.10.1) — 00. Inbox/01. Daily Notes (01-1. Planners·01-2. Weekly Notes 포함) 폐지, 10. CMDS Process/15. Periodic/ (Daily/·Weekly/) 신설. /daily·/weekly 산출 경로 표 갱신. 근거: 데일리는 트리아지 대상이 아닌 영구 시계열 로그 — Inbox 성격과 모순."
  - "4.6 (2026-08-17): Periodic Agent Notes 체제 신설 (macro v4.10.0) — /daily·/weekly 에이전트 작성 노트 섹션 추가 (04:00 하루 경계, draft 21:23 + finalize 04:53 OmniControl 잡, dailyStatus 멱등성, 사람 영역 불변, 스냅샷 표 = /weekly 원천 데이터). 에이전트 작성 노트의 model/effort frontmatter 컨벤션 (LLM Wiki 페르소나 컨벤션 이식) 참조 추가."
  - "4.5 (2026-07-12): 경량화 패스 (macro v4.9.4) — 중복 제거 diet (848→722줄, 53.7→48.2KB). (a) 동기화 8-destination 목록 3회 반복 → 1회 (ASCII 다이어그램·자동화 플로우 블록 제거, 인트로 문단+bash 정본 유지), (b) Claude Settings Sync 를 directory-structure.md 정본 포인터로 압축, (c) When to Use Which File 리스트 제거 (9-file 표와 1:1 중복), (d) 멤버 별 vault 매핑 표 → 한 줄 요약, (e) Decision Tree 를 AGENTS.md 압축형으로 통일, (f) frontmatter 필드 리스트·Mermaid 핵심 3가지·Special Characters 섹션 제거 (@import rules 와 중복), (g) AI Integration symlink 서술 압축. 별도 픽스: Vault Commands heredoc 에 description 필드 추가 + 'EOF' quote 제거 ($(date) 미확장 버그). token-estimate 14000→12500 재실측."
  - "4.4 (2026-07-02): 전수 감사 픽스 세트 (macro v4.9.3, Fable 5 멀티에이전트 audit) — (a) tags 회귀 5번째 재수정 (stray 1, 2 inline 재발분 제거·리스트 복원), (b) 동기화 다이어그램 소스 목록에 DESIGN.md 누락 보완, (c) Multi-Vault Architecture bare cross-vault wikilink 2곳 → obsidian URL, (d) /query 크로스-볼트 서술 정정 (mothership /query 는 qmd 기반으로 cross-vault 동작), (e) '91 카테고리' → 실측 87 정정, (f) /inbox 서브폴더 하드카운트 제거, (g) -v2 설명의 v4.2 하드코딩 제거, (h) Guide/HQ @import 표기 2건 wikilink 로 정정 (공백 경로는 import 불가), (i) token-estimate 5800→14000 실측화, (j) /share 스킬 예시에 cmds-sns-promo 반영. 별도 기록: 2026-06-29 편집분은 Pre-Flight Checklist 의 Table blank-line 항목 추가 (blank-line-rules.md 2026-06-27 개정 반영)."
  - "4.3 (2026-06-16): tags 회귀 재수정 (macro v4.9.1) — stray `1, 2` 태그가 v4.9.0 배포 후 inline 포맷(`[CMDS, system, 1, 2]`)으로 재발(2026-06-05). 리스트 포맷 복원. 3.8/4.0/4.1 에 이은 4번째 재발이라 근본 원인(Obsidian inline-tag 변환 추정) 추적 필요. 콘텐츠 변경 없음."
  - "4.2 (2026-05-30): v4.9.0 pass — deploy section 4-way→8-way, ZIP/matrix counts to 6/9, dedup system-files tables."
  - "4.1 (2026-05-22): 8→9 system files 전환 — DESIGN.md (precedence 9, Visual Language tier) 추가. Related System Files 표를 9-file 로 갱신. 공개 배포 파일 5→6개로 확장 (DESIGN.md 공개 결정). Tags 진짜 정리(`1, 2` 잔존분 제거)."
  - "4.0 (2026-05-20): Tags 실제 정리 (3.8 changelog 가 claim 했지만 실제로는 `1, 2` 잔존 — 이번에 진짜 제거). Last Updated 헤더 및 date modified 2026-05-20 동기화. CMDS.md v2.6 다이어트와 한 세트."
  - "3.9 (2026-05-04): Documented 2-Layer Version System (매크로 = CHANGELOG.md / 마이크로 = 파일별 version) in 'System Files Deployment' section. 사용자 질문 ('파일마다 버전 다른 게 괜찮나? 전체 버전은?') 에 응답 — 두 layer 가 보완적이며 매크로 entry 마다 파일별 version snapshot matrix 가 매핑 추적 보장."
  - "3.8 (2026-05-04): Removed stray numeric tag artifact (`tags: [CMDS, system, 1, 2]` ← `1, 2` came from precedence/audience leak). Restored proper YAML array format. Routine cleanup, no content changes."
  - "3.7 (2026-05-04): Added Sequencing Rule (누락 방지 #2) — Vercel deploy is a snapshot, so any DEV folder change after deploy needs a redeploy. GitHub auto-deploy is NOT connected, so git push alone doesn't update live. 사고 사례: CHANGELOG v4.5 entry deploy 후 추가해서 라이브 미반영, 사용자가 'GitHub 은 했으면서 왜 라이브는 안 해?' 지적."
  - "3.6 (2026-05-04): Documented 4-way sync (backup + share + DEV + Vercel) as a single comprehensive bash command in 'System Files Deployment' section. Added 누락 방지 룰 + 사고 사례 (2026-04-18 ~ 05-03 share folder 16일 stale)를 명시. system-docs-updater 스킬도 Quick Update Command → All-in-One Sync Command 로 재구성."
  - "3.5 (2026-05-03): Added Antigravity 03-7/03-8 output lanes. Fixed deployment flow rules count (7→8, includes blank-line-rules). Clarified that 5 of 8 system files are publicly deployed."
  - "3.4 (2026-05-03): Synced AI Agent output lane rules with AGENTS.md by documenting Codex MBP/Studio lanes in shared rules."
  - '3.3 (2026-04-23): description 필드 double-quote 강제 규칙 추가 — YAML plain scalar의 ": " 금지로 Obsidian Properties 렌더 깨짐 방지 (frontmatter-standard rule #7, pre-flight checklist, Essential 섹션 반영).'
  - "3.2 (2026-04-20): Project Overview 정정 — 사용자 포지셔닝(개인사업자/법인 신설 준비/박사 논문 중단/LG 임원·회장단 교육/4대 초점) 반영. 상세 프로필은 CMDS.md 2.3 로 위임."
  - "3.1 (2026-04-07): 필수 프로퍼티 7개로 확장 (description 추가, English required for LLMs)"
  - "3.0 (2026-04-01): @include 기반 공통 규칙 분리, 9개 아키텍처 패턴 적용"
  - "2.1 (2026-03-30): frontmatter 표준 추가, 백업 경로 이동"
  - "2.0 (2026-03-15): 전면 리뷰, 통계 갱신, GitHub/Web 링크"
---
> **🔄 Last Updated: 2026-09-21** | Backup: `40. Docs/47. CMDS Docs/cmds-system-files/CLAUDE_backup.md` | GitHub: [cmds-system-files](https://github.com/johnfkoo951/cmds-system-files) (코드 히스토리, 자동 배포 아님) | Web: [system.cmdspace.work](https://system.cmdspace.work) (Vercel `cmds-system-files-v2`)

# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

> **📌 Related System Files (9 System Files)** — `precedence` 순서대로 로드, audience 별 그룹
>
> **🤖 LLM Coding Agents** (always-loaded technical context):
> - @CLAUDE.md → [[CLAUDE.md]] — Claude Code specific (precedence: 1)
> - @AGENTS.md → [[AGENTS.md]] — Other AI coding agents: Codex, Cursor, Windsurf (precedence: 2)
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
> - @BRAIN.md → [[BRAIN.md]] — 구요한 brain profile (사람을 기술하는 grounding source, 사람도 읽음) (precedence: 7)
> - @BRAIN_PROMPT.md → [[BRAIN_PROMPT.md]] — Agent Rules of Engagement (BRAIN.md 를 *어떻게* 사용할지) (precedence: 8)
>
> **🎨 Visual Language** (always-loaded when producing visual artifacts):
> - @DESIGN.md → [[DESIGN.md]] — Visual language spec (v4.3 standards · Anti-Slop · Skill↔Surface mapping) (precedence: 9)

<!-- STATIC: 아래 내용은 거의 변경되지 않는 규칙입니다. AI는 높은 신뢰도로 캐시할 수 있습니다. -->

## ⚠️ CRITICAL RULES — READ FIRST

> 공통 규칙은 `.claude/rules/` 에 분리되어 있습니다. 아래는 핵심 요약입니다.

@.claude/rules/indentation-rules.md

@.claude/rules/frontmatter-standard.md

@.claude/rules/wikilink-rules.md

@.claude/rules/mermaid-rules.md

@.claude/rules/blank-line-rules.md

### Pre-Flight Checklist (Before Every Write/Edit)

Every time you create or edit a .md file, verify:

- [ ] **YAML frontmatter uses 2 SPACES** (not tabs)
- [ ] **Markdown body uses TAB** (not spaces)
- [ ] **No unnecessary blank lines** between heading→sub-heading, heading→content, list end→next heading (Obsidian-tight)
- [ ] **Wikilinks in YAML are quoted**: `"[[link]]"` not `[[link]]`
- [ ] **File reference form is correct**: vault 내부 → `[[wikilink]]` (default) · 에이전트 자동 로드 필요 → `@path/to/file.md` · vault 외부(`/DEV/`, `~/.claude/`) → 백틱 코드. 인라인 코드로 vault 내부 .md 파일명 쓰지 말 것 (decision tree: `.claude/rules/wikilink-rules.md`)
- [ ] **Mermaid node/edge labels are quoted**: `A["label"]`, no `[/` start
- [ ] **Table has a blank line before it**: a sentence/list immediately followed by a `| ... |` row breaks rendering — insert one blank line between the lead-in line and the table header (see `.claude/rules/blank-line-rules.md`)
- [ ] **Arrays use proper format**: hyphen + space + value
- [ ] **Dates use ISO 8601**: `YYYY-MM-DD` format
- [ ] **`description` field present and in English**: 1-2 sentences explaining the note for LLMs
- [ ] **`description` wrapped in double quotes `"..."`**: unquoted `: ` or ` #` inside description breaks YAML parser and corrupts Obsidian Properties rendering
- [ ] **File lifecycle/location checked**: 볼트 코드의 초기 위치는 에이전트 Inbox, 기존 DEV 작업은 해당 프로젝트. 완료 JSON/PY는 외부 보관하고 메인 MD에 기획·경로·재개 기록
- [ ] **Filename follows convention**: `YYYY-MM-DD-description.ext`

---

## Essential (Post-Compact)

> 컨텍스트 압축 후에도 반드시 기억해야 할 핵심 규칙:
> 1. **YAML frontmatter: 2 SPACES** / **Markdown body: TAB**
> 2. **Wikilinks in YAML: 반드시 큰따옴표** `"[[link]]"`
> 3. **Mermaid 라벨: 큰따옴표** `A["label"]` / `[/` 로 시작 금지
> 4. **코드 초기 출력 경로**: `00. Inbox/03. AI Agent/{환경 하위폴더}/` (기존 DEV 프로젝트는 해당 위치 유지). 완료 JSON/PY는 외부 보관, 기획·경로·재개는 메인 MD — file-creation-rules의 Completed Artifact Closeout 준수.
> 5. **필수 프로퍼티 7개**: type, aliases, **description** (English, 1-2 sentences for LLMs), author, date created, date modified, tags
> 6. **`description` 은 항상 `"..."` double-quote**: 안에 `: ` / ` #` 들어가면 YAML 파서 깨짐 (Obsidian Properties 렌더 실패)
> 7. **날짜 포맷**: ISO 8601 (YYYY-MM-DD)
> 8. **배열 포맷**: hyphen + space (`- value`)
> 9. **빈 줄 최소화 (Obsidian-tight)**: 헤딩→sub-heading, 헤딩→콘텐츠, 리스트 끝→다음 헤딩 사이 빈 줄 X. `---` / `##` 단락 분리에만 빈 줄 허용
> 10. **파일 참조 3종 결정 트리**: vault 내부 .md → `[[wikilink]]` (default · 이모지 prefix 정확히) · 에이전트 자동 로드 필요 → `@path/to/file.md` · vault 외부 경로/코드 → 백틱. 인라인 코드로 vault 내부 .md 쓰면 wikilink 깨짐

---

## Project Overview

This is an Obsidian vault for the **CMDSPACE (커맨드스페이스)** knowledge management system operated by Yohan Koo (구요한). CMDSPACE is currently a **sole proprietorship transitioning to a formal corporation**. The operator is a PhD ABD (dissertation writing currently paused) whose primary time is spent on **business + education** — notably corporate executive programs including **LG 임원 교육 · LG 회장단 교육**.

The vault implements the CMDS framework — a comprehensive Personal Knowledge Management (PKM) system with 9 major categories (100-900 series) — and follows the CMDS Process: Connect → Merge → Develop → Share.

**Active research-through-practice axes** (what the user is simultaneously researching and teaching): (1) Obsidian-based PKM, (2) System Files infrastructure, (3) LLM Wiki satellite vault, (4) 9Yohan multi-agent system. Detailed context in [[CMDS.md]].

## 💻 Working Environments

This vault is accessed from two different Mac environments:

### Primary Environment (MacBook Pro) ✅
**Base Path**: `/Users/yohankoo/Local Obsidian_MBP/CMDSPACE_Local_MBP`

**System**: MacBook Pro (14-inch)
**Status**: Primary (Most Frequently Used)
**Usage**: Main development and knowledge management workstation

### Secondary Environment (Mac Studio)
**Base Path**: `/Users/yohankoo/Obsidian_Local/CMDSPACE_Studio_Local_Org`

**System**: Mac Studio
**Status**: Secondary
**Usage**: Desktop workstation for heavy processing tasks

### Vault Sync
- Two machines are synced via **Obsidian Sync** (official Obsidian cloud server)
- The vault structure and all files/subfolders remain identical across both environments
- Sync is automatic and continuous — changes on one machine propagate to the other

### Claude Settings Sync (Symlink Strategy) — 결정 로그 (2026-04-14)

Obsidian Sync 는 dotfile (`.claude/`) 을 동기화하지 않는다. **결정**: `90. Settings/94. Agent Settings/claude/` 를 **원본** 으로 두고, 각 Mac 의 `.claude/` 하위 4개 폴더 (`agents`/`commands`/`rules`/`skills`) 를 상대 경로 symlink 로 연결한다. `settings.json`·`settings.local.json`·`sessions/` 는 머신 로컬 전용 (symlink 안 함). 트리 구조·이유·새 Mac 수동 설정법은 `.claude/rules/directory-structure.md` 의 "Symbolic Link" 섹션이 정본.

**user-scope 추가 (2026-09-21)**: `~/.claude/agents` 도 같은 볼트 폴더로 symlink 한다. project-scope(`<vault>/.claude/`)와 user-scope(`~/.claude/`)는 **별개 계층**이고 Claude Code 가 양쪽을 모두 읽는다 — 볼트 밖(`/DEV/` 등)에서도 써야 하는 9Yohan 에이전트가 user-scope 일반 폴더에 있어 Sync·git 어디에도 안 들어가던 문제를 이렇게 닫았다. 절차는 정본 참조.

**주의**: Obsidian Sync 가 symlink 자체를 실체 폴더로 복제해버리는 경우가 있다. 새 Mac 에서 처음 볼트를 받으면 `.claude/` 가 일반 폴더일 수 있으니, **각 Mac 마다 symlink 를 수동으로 재설정** 해야 한다.

### 📦 System Files Deployment (system.cmdspace.work)

**9 system files 중 공개 가능한 6개(CLAUDE, AGENTS, CMDS, HQ, Guide, DESIGN)** 만 `system.cmdspace.work` 에 배포. 나머지 3개(ANTIGRAVITY = Gemini 전용, BRAIN/BRAIN_PROMPT = Gobi 페르소나 전용)는 vendor·product 특화라 외부 배포 대상에서 제외. 배포 스택/경로/명령은 아래와 같습니다.

#### 📐 2-Layer Version System

CMDS 시스템 파일은 **2-layer 버전 시스템** 사용:

| Layer | 단위 | 위치 | 예시 |
|-------|------|------|------|
| 🌐 **매크로 (시스템 전체)** | Vercel 배포 스냅샷 | `/Users/yohankoo/DEV/cmds-system-files/CHANGELOG.md` | v4.5, v4.5.1 |
| 🔬 **마이크로 (파일별)** | 각 파일의 evolution | 각 파일 frontmatter `version:` | CLAUDE 3.8, CMDS 2.5, ... |

**둘 다 의미 있고 독립적** — 매크로는 외부 배포 단위 (사용자가 다운받는 ZIP 의 스냅샷), 마이크로는 각 파일의 schema/content evolution. 매크로 entry 안에 *그 시점의 9 files version snapshot matrix* 가 포함되어 매핑 추적 가능.

→ "현재 시스템 전체 버전?" 질문 → `DEV/CHANGELOG.md` 의 최상단 매크로 version 확인.
→ "특정 파일 진화?" 질문 → 그 파일 frontmatter `version:` + `changelog:` 배열 확인.

#### 배포 스택

| 레이어 | 서비스 | 설정 |
|--------|--------|------|
| **DNS** | Cloudflare | `cmdspace.work` (Free tier) · Account: `Cmdspace.contact@gmail.com` |
| **DNS Record** | Cloudflare | `system` → A `76.76.21.21` · Proxy **OFF** (DNS only) |
| **Hosting** | Vercel | Team: `johnfkoo951's projects` (Hobby) · Project: **`cmds-system-files-v2`** |
| **Project ID** | Vercel | `prj_CDfy1Qhc2WmxI2nj76w0EJv3zq8h` |
| **Domain binding** | Vercel | `system.cmdspace.work` + `files.cmdspace.work` (같은 프로젝트) |
| **Git Integration** | — | ❌ 없음 (CLI 수동 배포만) |

> **왜 `-v2`?**: Vercel 프로젝트 이름의 일련번호. 1차 시도 프로젝트 `cmds-system-files` 는 도메인 미연결 상태로 orphaned. 2차로 생성한 `cmds-system-files-v2` 가 현행. **시스템 파일 콘텐츠 버전(매크로/마이크로 — 현행 매크로는 `DEV/CHANGELOG.md` 최상단 참조)과는 무관**.

#### 배포 소스 폴더 (DEV)

**`/Users/yohankoo/DEV/cmds-system-files/`** 가 배포 소스입니다. 구조:

```
/Users/yohankoo/DEV/cmds-system-files/
├── index.html                    ← 메인 웹페이지 (v4.3 Landing)
├── docs/index.html               ← 기술 문서 (v4.3 Editorial Docs)
├── README.md                     ← GitHub 리드미
├── CHANGELOG.md                  ← 버전 이력
├── .vercel/project.json          ← Vercel 링크 (gitignored)
├── files/                        ← 다운로드 배포본
│   ├── CLAUDE.md, AGENTS.md, CMDS.md, CMDS-Guide.md, CMDS-Head-Quarter.md, DESIGN.md
│   ├── CMDS-System-Files.zip     ← 위 6개 + rules/ 번들
│   └── rules/ (9개 .md)          ← .claude/rules/ 미러
└── rules/ (9개 .md)              ← 레포 루트에도 복사본
```

#### 동기화 플로우 (볼트 → 8 destinations → 프로덕션)

볼트 원본 (6개 공개 파일 + `.claude/rules/*.md` 8개) 은 **항상 8 곳에 동기화** — 5 mothership (① 백업 `40. Docs/47. CMDS Docs/cmds-system-files/*_backup.md` ② 공유 `.../cmds-system-files-share/*_share.md` sanitized ③ DEV `files/` + rules + ZIP ④ GitHub push ⑤ Vercel deploy → `system.cmdspace.work`) + 3 satellite (⑥ cmds-vault starter-kit frontmatter ⑦ CMDS_LLM_Wiki dependency check ⑧ LLM Wiki starter-kit 3-place drift check). 누락하면 외부 배포·공유 문서·위성 스타터킷이 stale. `system-docs-updater` 스킬이 8-way (5 mothership + 3 satellite) fan-out 을 담당. 구체 경로·명령은 아래 배포 명령 (정본) 참조.

> **⚠️ 누락 방지 룰 #1 (8 destinations)**: 시스템 파일 수정 후 ① ~ ⑧ 모두 갱신해야 정합성 유지 (최소 ① + ② + ③ 은 항상, ⑥ cmds-vault frontmatter / ⑦ LLM Wiki dep / ⑧ starter-kit drift 는 점검 필수). ② share 폴더를 빼먹으면 외부에 공유한 sanitized 사본이 outdated 됨 (실제로 2026-04-30~05-03 사이 share 폴더 13~16일 stale 상태로 방치됐었음).
>
> **⚠️ 누락 방지 룰 #2 (Sequencing)**: ④ `vercel deploy` 는 그 순간의 DEV 폴더 *스냅샷* 을 배포. 따라서 **CHANGELOG.md / HTML / 기타 DEV 콘텐츠 변경은 ④ 전에 끝내야 함**. 만약 deploy 후에 추가 변경했다면 반드시 재배포 (`cd $DEV && vercel deploy --prod --yes`). GitHub 자동 배포 연결 안 돼있어 git push 만으론 라이브 갱신 안 됨 (2026-05-04 CHANGELOG v4.5 entry deploy 후 추가해서 라이브 미반영 사고 발생).

#### 배포 명령 (8-way 통합 — 5 mothership + 3 satellite)

```bash
VAULT="/Users/yohankoo/Local Obsidian_MBP/CMDSPACE_Local_MBP"
DEV="/Users/yohankoo/DEV/cmds-system-files"
BACKUP="$VAULT/40. Docs/47. CMDS Docs/cmds-system-files"
SHARE="$VAULT/40. Docs/47. CMDS Docs/cmds-system-files-share"

# Sanitization (개인정보 → 플레이스홀더)
SANITIZE='s|/Users/yohankoo/Local Obsidian_MBP/CMDSPACE_Local_MBP|{vault-path}|g; s|/Users/yohankoo/Obsidian_Local/CMDSPACE_Studio_Local_Org|{vault-path-secondary}|g; s|/Users/yohankoo/Local Obsidian_MBP/CMDS_LLM_Wiki|{satellite-vault-path}|g; s|/Users/yohankoo/DEV/cmds-system-files|{dev-path}|g; s|/Users/yohankoo|{home}|g; s|구요한|{your-name}|g; s|Yohan Koo|{your-name-en}|g; s|johnfkoo951|{your-handle}|g; s|Cmdspace.contact@gmail.com|{contact-email}|g; s|바람빛교회|{church-name}|g'

# ① 백업 (6개 공개 + 비공개 ANTIGRAVITY 1개)
for src in CLAUDE.md AGENTS.md CMDS.md "🏛 CMDS Guide.md" "🏛 CMDS Head Quarter.md" DESIGN.md ANTIGRAVITY.md; do
  dst=$(echo "$src" | sed 's|🏛 CMDS Guide|CMDS-Guide|;s|🏛 CMDS Head Quarter|CMDS-Head-Quarter|;s|\.md|_backup.md|')
  cp "$VAULT/$src" "$BACKUP/$dst"
done

# ② 공유 (6개만 — sanitized)
for src in CLAUDE.md AGENTS.md CMDS.md "🏛 CMDS Guide.md" "🏛 CMDS Head Quarter.md" DESIGN.md; do
  dst=$(echo "$src" | sed 's|🏛 CMDS Guide|CMDS-Guide|;s|🏛 CMDS Head Quarter|CMDS-Head-Quarter|;s|\.md|_share.md|')
  sed -e "$SANITIZE" "$VAULT/$src" > "$SHARE/$dst"
done

# ③ DEV 배포 소스 (6개 공개 + 9 rules + ZIP)
cp "$VAULT/CLAUDE.md"               "$DEV/files/CLAUDE.md"
cp "$VAULT/AGENTS.md"               "$DEV/files/AGENTS.md"
cp "$VAULT/CMDS.md"                 "$DEV/files/CMDS.md"
cp "$VAULT/🏛 CMDS Guide.md"        "$DEV/files/CMDS-Guide.md"
cp "$VAULT/🏛 CMDS Head Quarter.md" "$DEV/files/CMDS-Head-Quarter.md"
cp "$VAULT/DESIGN.md"               "$DEV/files/DESIGN.md"
cp "$VAULT/.claude/rules/"*.md      "$DEV/rules/"
cp "$VAULT/.claude/rules/"*.md      "$DEV/files/rules/"
cd "$DEV/files" && rm -f CMDS-System-Files.zip && \
  zip -rq CMDS-System-Files.zip CLAUDE.md AGENTS.md CMDS.md CMDS-Guide.md CMDS-Head-Quarter.md DESIGN.md rules/

# ④ GitHub push (코드 백업 — 자동 배포 X)
cd "$DEV" && git add -A && git commit -m "sync system files" && git push

# ⑤ Vercel 배포 (실제 프로덕션 반영)
cd "$DEV" && vercel deploy --prod --yes
```

→ ① ~ ⑤ (mothership 5) 통합 후 `system.cmdspace.work` 에 즉시 반영 (캐시 갱신 포함). ⑤ 만 실행하면 ① ② ③ 누락이라 외부 공유본/백업/배포본 불일치 발생.

##### ⑥ ~ ⑧ Satellite 동기화 (cmds-vault + CMDS_LLM_Wiki)

mothership system file 변경은 위성 스타터킷·의존 문서에도 파급된다. ⑤ Vercel 배포 후 다음 3개를 점검:

- **⑥ cmds-vault starter-kit frontmatter sync** — CMDS 스타터킷 배포본 (`github.com/johnfkoo951/cmds-vault`) 의 frontmatter·system file 참조가 mothership 과 일치하는지 확인. 불일치 시 갱신.
- **⑦ CMDS_LLM_Wiki dependency check** — satellite 의 Core Context / 가이드가 mothership 의 system file 개수·division 명·focus axis 변경을 반영하는지 점검 (예: "9 system files", "6 public") .
- **⑧ LLM Wiki starter-kit 3-place drift check** — `_starter-kit/cmds-llm-wiki/` (canonical) · `/DEV/cmds-llm-wiki/` (git mirror) · GitHub Release ZIP 3곳의 drift 점검. **default no-op** — drift 발견 시 보고만 하고, release 는 사용자가 직접 수행 (자동 sync 금지).

#### 새 Mac 에서 배포 권한 확보

DEV 폴더가 Vercel 프로젝트에 링크돼 있지 않다면 (`.vercel/` 없음) 한 번만 실행:

```bash
cd /Users/yohankoo/DEV/cmds-system-files
vercel link --project cmds-system-files-v2 --yes
```

#### 전체 흐름 자동화 (system-docs-updater 스킬)

"sync system files 배포" 요청 시 `system-docs-updater` 스킬이 위 ① ~ ⑧ fan-out 을 자동화한다. ⑤ Vercel deploy 는 사용자가 ① ② ③ 검증 후 실행, ⑧ 은 default no-op (보고만). **② 공유 폴더 누락 주의** — 과거 share stale 사고 (2026-04-18 ~ 05-03) 는 누락 방지 룰 #1 참조. 자세한 스킬 동작은 `system-docs-updater` 참조.

### Important Notes:
- All relative paths in this document (e.g., `00. Inbox/03. AI Agent/`) are relative to the base path above
- When switching between environments, Claude Code will automatically use the appropriate base path
- AI coding outputs are separated by environment subfolder (`03-1` ~ `03-8`) to track which machine/agent created each file. Lanes: 03-1/03-2 = Claude Code, 03-3/03-4 = OpenClaw, 03-5/03-6 = Codex, 03-7/03-8 = Antigravity (Google) — odd = MBP, even = Studio.

## 🛰 Companion Vaults — 6 Other Vaults Beyond Mothership

This mothership vault has **6 companion vaults** — separate Obsidian vaults with specialized purposes, classified by *governance* (who has authoring authority) and *purpose*. Not part of Obsidian Sync; each has its own git repo (or external sync).

> **Canonical reference**: `CMDS_LLM_Wiki` 의 [Multi-Vault Architecture](obsidian://open?vault=CMDS_LLM_Wiki&file=20.%20Wiki%2F23.%20Guides%2FMulti-Vault%20Architecture) 가이드가 모든 vault 의 멤버·합의 모델·workflow 의 single source of truth. 이 섹션은 mothership 측 요약.

### Vault Inventory by Governance (2026-04-30)

| Type                       | Vault                | Path                                                | 멤버                             | Purpose                             |
| -------------------------- | -------------------- | --------------------------------------------------- | ------------------------------ | ----------------------------------- |
| 🌍 **Mothership**          | `CMDSPACE_Local_MBP` | (this vault)                                        | 구요한 (Solo)                     | 마더십 — 모든 작업의 substrate              |
| 🛰 **Compiled Satellite**  | `CMDS_LLM_Wiki`      | `/Users/yohankoo/Local Obsidian_MBP/CMDS_LLM_Wiki`  | 구요한 + LLM                      | 학습·연구·정리된 지식 (Karpathy LLM Wiki 패턴) |
| 🤖 **Personal Product**    | `CMDS_Gobi`          | `/Users/yohankoo/Local Obsidian_MBP/CMDS_Gobi`      | 구요한 (Solo)                     | 고비 스페이스 / 고비 데스크탑 개인 사용             |
| 🤝 **Pair Collaboration**  | `CMDS_JoonLab`       | `/Users/yohankoo/Local Obsidian_MBP/CMDS_JoonLab`   | 구요한 + 박준                       | 교육·강의·컨설팅·코칭                        |
| 🤝 **Pair Collaboration**  | `CMDSPACE_Admin`     | `/Users/yohankoo/Local Obsidian_MBP/CMDSPACE_Admin` | 구요한 + 이태극                      | 커맨드스페이스 운영 총괄                       |
| 👥 **Team Collaboration**  | `GOBI`               | `/Users/yohankoo/Local Obsidian_MBP/GOBI`           | 5인 (구요한·이태극·김진영·강민석·Greg Moon) | 커맨드스페이스 × 고비 팀                      |
| 📤 **Public Distribution** | `cmds-vault`         | `/Users/yohankoo/Local Obsidian_MBP/cmds-vault`     | 구요한 → 외부                       | CMDS 스타터킷 (외부 사용자 배포)               |

→ 멤버 매핑은 위 표의 멤버 열이 정본: 구요한 = 7 vault 모두 · 박준 = *JoonLab 만* · 이태극 = *Admin + GOBI 2 vault* · 김진영/강민석/Greg = GOBI · 외부 사용자 = cmds-vault. 다른 사람의 콘텐츠가 *섞이지 않도록* governance 분리.

### Registered Satellites (Karpathy 의미의 satellite — LLM 협업)

| Satellite | Purpose | Entry Point |
|-----------|---------|-------------|
| `CMDS_LLM_Wiki` | Karpathy LLM Wiki pattern (3-Layer: Raw Sources / Wiki / Schema). LLM ingests external sources and compiles persistent wiki. | [[🛰 CMDS_LLM_Wiki Satellite Vault]] |

### Cross-Vault Reference Convention

Obsidian does not support direct wikilinks between vaults. Use the following:

**Frontmatter 상호참조 (2026-08-27 표준 — 정본: `.claude/rules/wikilink-rules.md` §6)**: 볼트 간 링크는 **advanced-uri 마크다운 링크**가 표준. 방향별 필드 — mothership 노트 → 위키 페이지는 `wikiVaultRelated:`, 위키 페이지 → mothership 노트는 `mainVaultRelated:`.

```yaml
# Mothership 노트에서 위키 페이지 참조
wikiVaultRelated:
  - "[LLM Wiki: Epistemic Infrastructure](obsidian://advanced-uri?vault=CMDS_LLM_Wiki&filepath=20.%20Wiki%2F21.%20Concepts%2FEpistemic%20Infrastructure.md)"
# 그 외 companion vault 는 기존 관례 유지
source-vault: CMDS_LLM_Wiki   # 또는 CMDS_JoonLab, CMDS_Gobi, GOBI, CMDSPACE_Admin, cmds-vault
related:
  - "[[🛰 CMDS_LLM_Wiki Satellite Vault]]"  # always link the entry point
```

> **폴백**: advanced-uri 는 *대상 볼트에* `obsidian-advanced-uri` 플러그인이 있어야 동작. 플러그인이 없는 볼트를 가리킬 때는 기본형 `obsidian://open?vault=...&file={path without .md}` 사용 (액션 `open` · 파라미터 `file=` · `.md` 없음). filepath 는 URL 인코딩 필수, 액션 이름 `adv-uri` 오타 금지 — 상세는 wikilink-rules.md §6.

```markdown
# Body text (companion vault pages — advanced-uri 권장, 가벼운 언급은 텍스트 참조 허용)
[Multi-Vault Architecture](obsidian://advanced-uri?vault=CMDS_LLM_Wiki&filepath=20.%20Wiki%2F23.%20Guides%2FMulti-Vault%20Architecture.md)

# 또는 텍스트 참조
→ LLM Wiki: Multi-Vault Architecture
→ JoonLab: 강의 자료 / 2026-04-15 LG 임원 교육
→ GOBI: 제품 PRD / 2026-04 마케팅
```

**To reference this vault from any companion:**

Companion 노트는 `source-vault: CMDSPACE_Local_MBP` + `mainVaultRelated:` (advanced-uri, `vault=CMDSPACE_Local_MBP`) 사용. 플러그인 없는 환경은 `obsidian://open?vault=CMDSPACE_Local_MBP&file=...` 폴백.

### When to Work in Which Vault — Governance 우선 결정 트리

```
새 자료가 생겼다 → 누가 합의 권한 가짐?
├─ 나 혼자 → 무엇을 위함?
│   ├─ 일상 PKM → 🌍 mothership (here)
│   ├─ 학습·연구·정리 (LLM compile) → 🛰 CMDS_LLM_Wiki
│   ├─ 고비 제품 개인 사용 → 🤖 CMDS_Gobi
│   └─ 임시·미분류 → mothership/00. Inbox
├─ 나 + 박준 → 🤝 CMDS_JoonLab
├─ 나 + 이태극 (운영) → 🤝 CMDSPACE_Admin
├─ 5인 팀 (Gobi) → 👥 GOBI
└─ 외부 배포 → 📤 cmds-vault
```

**핵심 원칙** ([Multi-Vault Architecture](obsidian://open?vault=CMDS_LLM_Wiki&file=20.%20Wiki%2F23.%20Guides%2FMulti-Vault%20Architecture) § 1 — 5 Forces):
1. **주저자 분리** — 사람 vs LLM, 개인 vs 협업 (Contamination Mitigation)
2. **합의 모델 분리** — Solo / Pair / Team / Public 의 git/sync 충돌 방식이 다름
3. **수명 분리** — Permanent vs Project-bound vs Time-boxed
4. **도구 분리** — vault 별 plugin / hook / `.claude/` 다를 수 있음
5. **검색 인덱스 분리** — qmd collection 단위로 분리 가능

**Anti-pattern**: 다음은 새 vault 만들지 말 것:
- 단순 카테고리 분리 (mothership 의 9 categories 로 충분)
- 임시 프로젝트 (00. Inbox 또는 mothership 의 project 폴더)
- 혼자 쓰는 새 도메인 (mothership 의 새 subcategory 로 처리)

### 이론·프레임워크(학술 지식) 배치 — 2층 규칙 (2026-08-25 확정)

트리의 "학습·연구·정리 (LLM compile) → 🛰 CMDS_LLM_Wiki" 는 *LLM 이 컴파일하는 레퍼런스* 에 한정된다. 학자들의 theory / framework / model 을 다룰 때의 판단 기준은 **주제가 아니라 주저자와 이해의 깊이** (Force 1 주저자 분리의 적용):

| 층 | 볼트 | 성격 | 홈 |
|----|------|------|-----|
| **내재화 층** | 🌍 mothership | 직접 공부하며 자기 언어로 쓰는 이론 노트 — 본인 해석, 강의·컨설팅 연결, 비판 | 📖 200 Literature (📚 201 Concepts / 202 Frameworks / 203 Models / 204 Theories · 해석은 📚 220 Personal Insights). 물리 폴더 `30. Permanent Notes/`, 분류는 `CMDS:` frontmatter |
| **레퍼런스 층** | 🛰 CMDS_LLM_Wiki | LLM 이 컴파일한 넓은 커버리지 — 논문 원문 ingest (Raw Sources), 이론 간 cross-reference, "찾아보는" 지식 | 10. Raw Sources → 20. Wiki |

- 워크플로: 내재화 층은 `/connect`(용어·관심 stub) → `/merge`(N 소스 → 1 Literature 노트). 레퍼런스 층은 satellite 의 `/ingest`.
- 두 층은 복사본이 아니라 역할 분담 — mothership 노트는 `wikiVaultRelated:` (advanced-uri 링크, wikilink-rules.md §6)로 위키를 가리키고, 위키 페이지는 `mainVaultRelated:` 로 역참조. 본문 산문의 가벼운 언급은 `→ LLM Wiki: {page}` 텍스트 참조 허용.
- 예시 패턴: "학습 이론 30개 훑어 정리" = 위키 컴파일 → 그중 강의 척추가 되는 이론만 mothership 에서 본인 노트로 재작성.

→ 위키 측 정본: [Multi-Vault Architecture](obsidian://open?vault=CMDS_LLM_Wiki&file=20.%20Wiki%2F23.%20Guides%2FMulti-Vault%20Architecture) § 3 Type B "이론·프레임워크 배치" · [Wiki Vault as Learning Outpost](obsidian://open?vault=CMDS_LLM_Wiki&file=20.%20Wiki%2F21.%20Concepts%2FWiki%20Vault%20as%20Learning%20Outpost)

### Canonical Guide References (LLM Wiki 측 가이드)

새 vault 결정·운영·검색 인프라·인덱싱·임베딩 관리는 모두 satellite `CMDS_LLM_Wiki` 의 가이드를 *single source of truth* 로 참조한다. mothership 에서는 이 가이드들로 링크하고, 자세한 내용은 satellite 측에서 유지·갱신.

| 주제 | Canonical Guide | 위치 |
|------|----------------|------|
| Vault 운영·결정·governance | [Multi-Vault Architecture](obsidian://open?vault=CMDS_LLM_Wiki&file=20.%20Wiki%2F23.%20Guides%2FMulti-Vault%20Architecture) | LLM Wiki |
| 검색 방법 5 종 종합 비교 (master) | [Wiki Search Methods Comparison](obsidian://open?vault=CMDS_LLM_Wiki&file=20.%20Wiki%2F23.%20Guides%2FWiki%20Search%20Methods%20Comparison) | LLM Wiki |
| BM25 (어휘 검색) | [BM25 Search (qmd lex)](obsidian://open?vault=CMDS_LLM_Wiki&file=20.%20Wiki%2F23.%20Guides%2FBM25%20Search%20%28qmd%20lex%29) | LLM Wiki/23. Guides |
| Vector (의미 검색) | [Vector Search (qmd vec)](obsidian://open?vault=CMDS_LLM_Wiki&file=20.%20Wiki%2F23.%20Guides%2FVector%20Search%20%28qmd%20vec%29) | LLM Wiki/23. Guides |
| HyDE (가설 답변 검색) | [HyDE Search (qmd hyde)](obsidian://open?vault=CMDS_LLM_Wiki&file=20.%20Wiki%2F23.%20Guides%2FHyDE%20Search%20%28qmd%20hyde%29) | LLM Wiki/23. Guides |
| Grep (정규식·분포) | [Grep Search](obsidian://open?vault=CMDS_LLM_Wiki&file=20.%20Wiki%2F23.%20Guides%2FGrep%20Search) | LLM Wiki/23. Guides |
| Graphify (구조·커뮤니티) | [Graphify Knowledge Graph](obsidian://open?vault=CMDS_LLM_Wiki&file=20.%20Wiki%2F23.%20Guides%2FGraphify%20Knowledge%20Graph) | LLM Wiki/23. Guides |
| 인덱싱·로컬 임베딩 운영 (qmd, GGUF, hook) | [Wiki Indexing and Embedding Maintenance](obsidian://open?vault=CMDS_LLM_Wiki&file=20.%20Wiki%2F23.%20Guides%2FWiki%20Indexing%20and%20Embedding%20Maintenance) | LLM Wiki |
| RAG / VectorDB / GraphDB 산업 매크로 | [Search Technology Landscape](obsidian://open?vault=CMDS_LLM_Wiki&file=20.%20Wiki%2F23.%20Guides%2FSearch%20Technology%20Landscape) | LLM Wiki |
| LLM Wiki 토큰 절감 전략 | [LLM Wiki Token Optimization Strategies](obsidian://open?vault=CMDS_LLM_Wiki&file=20.%20Wiki%2F23.%20Guides%2FLLM%20Wiki%20Token%20Optimization%20Strategies) | LLM Wiki |

→ Mothership 의 system files 는 *철학·전체 정책*, satellite 의 가이드는 *실행 디테일*. 갱신 권한은 satellite 측에 있음. 이 mothership 섹션은 *주기적으로 satellite 가이드 와 정합성 확인* 필요.

### Cross-Vault Query from Mothership

메인 볼트 세션에서도 **`CMDS_LLM_Wiki` 볼트의 컴파일된 지식을 바로 검색/인용 가능**하다. Obsidian wikilink는 볼트 경계를 넘지 못하지만, qmd MCP는 user-scope로 등록되어 cwd 무관하게 satellite vault를 인덱싱한다.

**가능한 것**:

```
✅ qmd로 LLM Wiki 검색 (자동 — cwd 무관)
   mcp__qmd__query(searches=[{type:"vec", query:"..."}])

✅ Grep/Read에 명시 path
   Grep(pattern="...", path="/Users/yohankoo/Local Obsidian_MBP/CMDS_LLM_Wiki")
   Read(file_path="/Users/yohankoo/Local Obsidian_MBP/CMDS_LLM_Wiki/20. Wiki/...")
```

**불가능한 것**:

```
❌ LLM Wiki 측 /query 커맨드 — index.md를 cwd 기준으로 읽으므로 satellite 세션 전용
   (mothership 세션의 /query 는 qmd 기반 cross-vault 커맨드라 여기서도 동작 — § CMDS Process Command Suite)
❌ cwd만 믿는 기본 Grep — path 명시 안 하면 메인 볼트만 스캔
❌ [[LLM Wiki 페이지]] 직접 wikilink — 볼트 경계 넘지 못함
```

**메커니즘**:
- qmd config: `~/.config/qmd/index.yml` — absolute path로 `CMDS_LLM_Wiki/20. Wiki` 등 하드코딩
- qmd MCP: `~/.claude.json` user-scope 등록 (모든 Claude Code 세션에서 사용 가능)
- qmd 인덱스 DB: `~/.cache/qmd/index.sqlite` (cwd 독립)

**기본 동작 (Default Trigger)**: 사용자 질문/작성 주제가 아래 카테고리에 닿으면 **답변 전에 `mcp__qmd__query` 를 먼저 한 번 돌린다** — 사용자가 명시적으로 "wiki 검색해줘"라고 안 해도 default behavior. LLM Wiki는 컴파일된 cross-reference 와 관련 개념 묶음을 이미 보유하고 있어서, Grep 만으로는 구조적 연결을 놓친다.

**qmd 트리거 카테고리**:
- LLM/AI 아키텍처 개념 (RAG, Compiled Wiki, Context Engineering, Persistent Knowledge Base 등)
- 멀티에이전트 패턴 (Orchestrator-Subagent, Agent Teams, Shared State, Message Bus, Generator-Verifier)
- Karpathy / kepano / Anthropic 등 wiki 에 등록된 entity 가 등장하는 토픽
- Knowledge Management 이론 (Memex, Zettelkasten 의 LLM 시대 변용, Ingest-Query-Lint Cycle 등)
- "내가 LLM Wiki 에 정리해뒀던 X" 같은 사용자의 self-reference

**도구 선택 규칙**:

| 상황 | 도구 | 이유 |
|------|------|------|
| 정확한 파일명/제목 안다 | `Grep` + path 명시 | 빠르고 결정적 |
| 추상 쿼리 / 의미 검색 / 관련 개념 묶음 | `mcp__qmd__query` (vec/hyde) | cross-reference 자동 surfacing |
| 키워드는 명확하지만 어디 있는지 모름 | qmd `lex` 먼저, fallback 으로 Grep | 키워드 매칭 + 의미 보강 |
| 답변 풍부하게 / 관점 다층화 | qmd `vec` 또는 `hyde` (intent 명시) | "사용자가 묻지 않았지만 관련 있는 것" 발굴 |

**Anti-pattern (이번 세션의 실수)**: 정확한 제목(`RAG vs Compiled Wiki`)을 알아서 Grep + Read 로 직행했더니, 같은 주제에 묶여있던 `Shared State Pattern`, `Choosing Multi-Agent Patterns` 페이지를 놓침 → 팀 멀티 저자 시나리오에서 결정적인 통찰 누락. 정확한 페이지를 안다고 해서 qmd 를 건너뛰면 안 됨 — **확장 검색 (관련 개념 1-hop) 의 비용이 매우 낮다**.

**인용 표기**: 클릭 가능해야 하는 크로스-볼트 참조는 advanced-uri 마크다운 링크 (frontmatter 는 `wikiVaultRelated:`), 본문 산문의 가벼운 언급은 `→ LLM Wiki: {page name}` 텍스트 참조 (Obsidian wikilink 는 볼트 경계 못 넘음 — 형식 정본: wikilink-rules.md §6).

---

## CMDS Process Command Suite (2026-04-14+)

The mothership has 10 slash commands aligned with the **CMDS Process** (Connect → Merge → Develop → Share). They live in `90. Settings/94. Agent Settings/claude/commands/` (symlinked from `.claude/commands/`).

### Command Map

| Command | Type | Role | Key dialogs |
|---------|------|------|-------------|
| `/inbox` | Router | Scan 00. Inbox/ subfolders, AskUserQuestion to route to a stage command | scope + stage |
| `/connect` | Stage | Triage inbox → 100 Themes (interest/topic/variable/term). **Auto-classifies, auto-dedupes, auto-stubs.** | only at ambiguity |
| `/merge` | Stage | N inbox/Theme notes → 1 synthesized 200 Literature note. **Heaviest command, most dialogs.** | purpose, candidates, angle, draft review |
| `/develop` | Stage | Apply method/build artifact → 300-600 (code, prompts, specialty, curriculum). | artifact type, review |
| `/share` | Stage / Orchestrator | Auto-delegate to existing skills (`thebetter-writer`, `markdown-slides`, `tone-writer`, etc.) → 700-800 | format, tone (when needed) |
| `/lint` | Cross-cutting | Health check by stage scope (inbox/connect/merge/develop/share/all). **Read-only**, surfaces issues. | only if user asks for fix |
| `/query` | Cross-cutting | Search vault + LLM Wiki, synthesize answer, optionally file back into appropriate CMDS category (NOT a separate /queries folder). | wiki-worthy + classify |
| `/status` | Cross-cutting | One-screen vault stage snapshot + recommended next action. **Zero dialogs**, fast. | none |
| `/seeds` | Cross-cutting | 제목만 걸어둔 씨앗 노트를 씨앗/잔해/How-to 로 가르고 클러스터링 → 글감 제안 + 📚 101/102 허브 생성. **마더십 전용**. | 3분류 확인, 클러스터 승인 |
| `/harvest` | Cross-cutting | 7볼트 생태계를 가로질러 끊긴 쌍·이미 컴파일된 씨앗·위키 고아·개념 drift 수확. companion 볼트는 **읽기만**. | 적용 승인 |

### Decision Tree (When to Use Which)

```
세션 시작 / 뭐 할지 모름             → /status
방대한 inbox에서 시작                → /inbox → 라우팅
inbox 항목 빠르게 분류·등록          → /connect
여러 노트 합성해서 한 노트로         → /merge  (핵심 워크플로)
방법론 적용 / 코드·프롬프트 생성     → /develop
기존 합성 → 외부용 산출물            → /share
볼트에 질문 (자신의 글 + LLM Wiki)   → /query
제목만 걸어둔 씨앗 → 글감·허브        → /seeds   (월 1회)
볼트 생태계 전체 교차 수확           → /harvest (분기 1회)
위생 점검 (모순/orphan/stale)        → /lint {scope}
```

### Settled Design Decisions (record of intent)

- **Vocabulary**: stage commands use the user's own framework (CMDS Process) instead of LLM Wiki's `ingest/query/lint` triad. The LLM Wiki vocabulary stays satellite-side; mothership uses Connect/Merge/Develop/Share.
- **Inbox is router-only**: `/inbox` never writes; it only scans, summarizes, and uses `AskUserQuestion` to route. This matches the user's mental model of inbox as triage zone.
- **`/share` as orchestrator, not writer**: auto-delegates to existing skills (`thebetter-writer`, `markdown-slides`, `tone-writer`, `pptx-cmds`, `series-writer`, `cmds-sns-promo`, `course-designer`, `markdown-video`, `business-docs`, etc.). Never produces content directly. Routing map maintained in `share.md`.
- **`/query` results are NOT folder-isolated**: per user policy "내 모든 노트가 쿼리의 소재이고 결과이기 때문에 구분하지 않고 — CMDS 지식분류 체계에 따라 분류". Query results that survive the wiki-worthiness gate get classified into the appropriate CMDS category (220 Personal Insights, 210 Literature Reviews, 5XX Product, etc.) and saved to the correct physical folder (mostly `30. Permanent Notes/`).
- **Automation density per command**: `/connect` auto-pilots with minimal user input; `/merge` deliberately preserves multi-dialog because synthesis involves information loss; `/develop` and `/share` ask only at the type/format decision; `/lint` and `/status` are zero-dialog.
- **`AskUserQuestion` everywhere it's used**: stage commands use the MCP tool with multiSelect where applicable, max 4 options per question. Always include a "(Recommended)" first option based on context.
- **CMDS categorization is metadata, not folders**: there is no `100/`, `200/`, etc. physical folder. Notes live in the existing folder structure (`30. Permanent Notes/`, `60. Collections/`, etc.) and are categorized via `CMDS:` and `index:` frontmatter.
- **All commands honor pre-flight rules**: `frontmatter-standard.md`, `wikilink-rules.md`, `indentation-rules.md`, `file-creation-rules.md`. New v2 fields introduced: `mergePurpose`, `sourceNotes`, `wikiVaultRelated` (mothership→wiki, advanced-uri — 2026-08-27 `mainVaultRelated` 텍스트형 대체; `mainVaultRelated` 는 위키→mothership 역방향 전용으로 존치), `developSources`, `shareSourceNotes`, `shareFormat`, `sharePurpose`, `queryOrigin`, `querySources`.

### Typical Session Patterns

**Daily**: `/status` → `/inbox` → (`/connect` 또는 `/merge`) → 종료
**Weekly**: `/lint inbox` → 정리 후 `/merge {topic}` → `/share` (필요 시)
**프로젝트 작업**: `/query {topic}` → `/merge {topic}` → `/develop` 또는 `/share`
**시스템 점검 (월 1회)**: `/lint all` → `/refresh-context` (TBD)

### Periodic Agent Notes — /daily · /weekly (2026-08-17+)

CMDS Process 8종과 별개로, 시간 축 기록(데일리·위클리)은 에이전트가 작성한다. 사람 입력 영역은 데일리의 "사람 한 줄"·To Do·Log, 위클리의 "사람 결정 1줄" 뿐.

| Command | 주기 (OmniControl 잡) | 산출 |
|---------|----------------------|------|
| `/daily` | 매일 draft 21:23 (`daily-note`) + 어제 확정 04:53 (`daily-note-final`) | `10. CMDS Process/15. Periodic/Daily/YYYY-MM-DD.md` |
| `/weekly` | 매주 일 21:41 (`weekly-review`) | `10. CMDS Process/15. Periodic/Weekly/YYYY-Www.md` |

핵심 규칙:
- **하루의 경계는 04:00 (KST)** — 데일리 노트 D 는 D 04:00 → D+1 04:00 창을 다룬다. 자정 이후 새벽 작업은 전날 노트에 편입(finalize 모드가 처리). 파일명은 달력 날짜 유지.
- **하루 3단계**: skeleton(04:53, finalize 잡이 어제 확정 직후 오늘 뼈대 생성) → draft(21:23, 에이전트 섹션 채움) → final(다음날 04:53). 노트가 하루 시작부터 존재해야 사용자가 `Note-taking (Live)` Bases 를 실시간으로 보고 사람 영역을 낮 동안 쓸 수 있다.
- **멱등성**: frontmatter `dailyStatus: pending → filled → final` 로 상태 관리. 노트가 이미 있으면 섹션 단위 패치만 — **템플릿 재삽입 절대 금지** (과거 이중 삽입 사고 7회). 사람 영역은 불변.
- **Bases 작성자 구분**: `Note-taking (Live)` 의 `authorKind` formula 가 `model:` frontmatter 로 노트를 👤 사람 / 🤖 Claude / 🤖 Codex / 🤖 Antigravity 로 나눠 보여준다. 에이전트가 노트를 만들 때 `model:` 을 빠뜨리면 사람 작성으로 오분류된다.
- **데일리 "스냅샷" 표** (md 카운트 4종, 오늘 생성 사람/기계 분리, 백업 상태, 타임존) 는 /weekly 가 diff 하는 원천 데이터.
- **에이전트 작성 노트는 `model:` + `effort:` frontmatter** 로 작성 모델을 기록 (`.claude/rules/frontmatter-standard.md` Optional Properties 참조).
- 정본: 수집 파이프라인·합성 규칙은 `.claude/commands/daily.md`, 노트 구조는 `90. Settings/91. Templates/Template_01. Daily Note.md` (본문의 `%%agent: ...%%` 지시 주석이 계약 — wikilink-rules §5).

---

## System Documentation Structure

This vault has **9 system files** that work together to provide complete guidance, organized by audience. (Detailed per-file blurbs live in the top "📌 Related System Files" blockquote; this is the compact reference matrix.)

| File | Audience | Focus | Precedence |
| ---- | -------- | ----- | :--------: |
| **CLAUDE.md** (this file) | Claude Code | **HOW** - Claude Code 기술 규칙, file ops, commands | 1 |
| **AGENTS.md** | Codex, Cursor, Windsurf | **HOW** - 타 AI coding agent 용 기술 규칙 | 2 |
| **ANTIGRAVITY.md** | Google Gemini / Antigravity IDE | **HOW (Gemini)** - Gemini 전용 행동 규칙·도구 매핑 | 3 |
| **CMDS.md** | All LLM assistants | **WHY & WHAT** - 시스템 철학·사용자 프로필·9 카테고리 | 4 |
| **🏛 CMDS Guide.md** | User + AI | **STANDARDS** - Properties v2, 템플릿, naming | 5 |
| **🏛 CMDS Head Quarter.md** | User + AI | **WHERE** - 87 서브카테고리 네비게이션 허브 | 6 |
| **BRAIN.md** | Gobi agent + 사람 | **WHO** - 구요한 brain profile (사람을 기술하는 grounding source) | 7 |
| **BRAIN_PROMPT.md** | Gobi agent | **HOW (Gobi)** - Rules of Engagement (BRAIN.md 사용 메타 지침) | 8 |
| **DESIGN.md** | All LLM agents producing visual artifacts | **HOW (Visual)** - v4.3 standards · Anti-Slop · Skill↔Surface mapping | 9 |

> BRAIN.md / BRAIN_PROMPT.md 는 *Claude Code · Gemini CLI 등 일반 LLM coding agent 의 컨텍스트로 들어가지 않음*. Gobi 앱이 외부에서 구요한 페르소나로 답할 때만 사용. 다른 system files 와 audience 가 다르다는 점이 핵심.

**Remember**: This file (CLAUDE.md) is **Claude Code specific**. For other AI agents, use **AGENTS.md** (general) or **ANTIGRAVITY.md** (Gemini). 파일별 용도는 위 표가 정본.

## File Creation Rules

@.claude/rules/file-creation-rules.md

## Video Project Workflow

@.claude/rules/video-project-workflow.md

## Directory Structure

@.claude/rules/directory-structure.md

---

## CMDS-Specific Conventions

### Hierarchy System
- 🏛 - Home/Guide notes (top level)
- 📖 - 1st level CMDS (100-900 series)
- 📚 - 2nd level CMDS (N01-N99)
- (No icon) - 3rd level (detailed topics)

### File Prefixes
- 📎 - Web Clips
- 🏷 - Index
- 📦 - Review
- 🔖 - Personal idea outputs
- 📜 - Others' idea outputs
- 📈 - Code/Syntax
- 🎹 - Music
- 📘 - Books/Reference

### Note Types (type property)
Most common types in the vault:
- `note` - General notes (459+)
- `terminology` - Term definitions (130+)
- `research-pipeline` - Research pipeline documents (124+)
- `meeting` - Meeting notes (160+)
- `people` - People profiles (93+)
- `curriculum` - Course curriculum (82+)
- `channel` - YouTube/Blog/Newsletter 채널 프로필 (101+)
- `CMDS` - CMDS index pages (replaces traditional MOC concept)
- `api` - API documentation (97+)
- `moc` - Map of Content (85+)
- `manuscript` - Manuscripts and drafts (66+)

## Obsidian-Specific Guidelines

### Markdown Files
- Always use wikilinks `[[]]` for internal references, NOT markdown links
- Include YAML frontmatter for metadata — 필수 7필드 + 선택 필드 (`CMDS:`/`index:`/`status:`) 정의는 @.claude/rules/frontmatter-standard.md 가 정본

### Note Templates
Templates are located in `90. Settings/91. Templates/`
Key templates include:
- `Template_00. Basic Note.md` - Basic note structure
- `Template_01. Daily Note.md` - Daily journal
- `Template_05. Meeting Minutes.md` - Meeting notes
- `Template_20. Research Note.md` - Research documentation
- `Template_51. People.md` - People profiles
- `Template_80. AI Summary.md` - AI-generated summaries
- `Template_90. CMDS MOC.md` - Map of Content

### Mermaid Diagrams
`.claude/rules/mermaid-rules.md` (@import 됨) 가 정본 — 라벨 큰따옴표, `[/` 시작 금지, 엣지 라벨 따옴표.

## Key Integration Points

### Main Hub Notes
- [[🏛 CMDS Head Quarter]] - Central navigation hub with 9 categories
- [[🏛 CMDS Guide]] - Properties standardization and operational guidelines

### AI Integration
- ChatGPT custom GPTs linked in CMDS Head Quarter
- Claude integration via Claude Code directory
- Agent settings: `90. Settings/94. Agent Settings/claude/` 원본 → `.claude/{agents,commands,rules,skills}` symlink (§ Claude Settings Sync 참조)

### Automation
- n8n workflows for automation
- Obsidian Webhook integration
- Various API integrations (OpenAI, Anthropic, Google)

## Obsidian CLI (v1.12+)

> **📖 Full Reference**: [[Obsidian CLI]] | **📘 실전 가이드**: [[Obsidian CLI 사용 가이드 (CMDS)]]

Obsidian CLI는 터미널에서 Obsidian을 직접 제어하는 명령줄 인터페이스입니다.
**Claude Code에서 `obsidian` 명령을 Bash 도구로 호출하여 Obsidian 네이티브 기능을 활용할 수 있습니다.**

### 요구사항
- Obsidian 1.12+ (Early Access, Catalyst 필요)
- Settings → General → CLI 활성화
- Obsidian 앱 실행 중이어야 함

### Claude Code에서 사용 시 주의사항
- `obsidian` 명령은 Bash 도구로 호출
- 볼트 타겟팅: `obsidian vault=CMDSPACE_Local_MBP <command>`
- 파일 타겟팅: `file=<name>` (wikilink 방식) 또는 `path=<경로>` (볼트 루트 기준)
- 출력 복사: `--copy` 플래그

### 자주 쓰는 CLI 명령 (Quick Reference)

```bash
# --- 읽기/검색 ---
obsidian read file=<name>                          # 파일 내용 읽기
obsidian search query="<text>" format=json          # 볼트 검색
obsidian tags all counts sort=count                 # 태그 통계
obsidian properties all counts sort=count           # 프로퍼티 통계
obsidian backlinks file=<name> counts               # 백링크 조회
obsidian outline file=<name> format=tree            # 목차 조회
obsidian tasks daily todo                           # 오늘 미완료 태스크

# --- 생성/편집 ---
obsidian create name=<name> template=<template> silent  # 템플릿으로 노트 생성
obsidian append file=<name> content="<text>"            # 내용 추가
obsidian prepend file=<name> content="<text>"           # frontmatter 뒤에 삽입
obsidian daily:append content="- [ ] <task>" silent     # 데일리 노트에 태스크 추가
obsidian property:set name=<key> value=<val> file=<name> # 프로퍼티 설정
obsidian property:remove name=<key> file=<name>          # 프로퍼티 제거

# --- 분석 ---
obsidian vault info=files                           # 볼트 파일 수
obsidian orphans total                              # 고아 노트 수
obsidian unresolved verbose                         # 미해결 링크
obsidian deadends total                             # 아웃링크 없는 노트 수

# --- 플러그인 ---
obsidian plugins filter=community versions          # 커뮤니티 플러그인 목록
obsidian plugin:reload id=<plugin-id>               # 플러그인 리로드

# --- 개발자 ---
obsidian eval code="<javascript>"                   # JS 실행 (app.vault 등 접근)
obsidian dev:screenshot path=<filename>             # 스크린샷
obsidian dev:console level=error                    # 콘솔 에러 확인
```

### CLI vs 파일 직접 조작 가이드

| 작업 | CLI 사용 | 파일 직접 조작 |
|------|---------|-------------|
| 프로퍼티 수정 | `property:set` ✅ (안전) | Edit 도구 (YAML 직접 편집) |
| 내용 추가 | `append`/`prepend` ✅ | Edit/Write 도구 |
| 노트 생성 (템플릿) | `create template=` ✅✅ | Write 도구 (수동 복제) |
| 검색 | `search` ✅ (Obsidian 인덱스) | Grep 도구 (파일 시스템) |
| 백링크/링크 분석 | `backlinks`/`orphans` ✅✅ | 불가능 |
| Obsidian API 접근 | `eval` ✅✅ | 불가능 |

---

## Vault Commands

### Note Creation with Proper Metadata
```bash
cat > "00. Inbox/$(date +%Y-%m-%d)-new-note.md" << EOF
---
type: note
aliases: []
description: ""
author:
  - "[[구요한]]"
date created: $(date +%Y-%m-%d)
date modified: $(date +%Y-%m-%d)
tags: []
CMDS:
index:
status:
---

# Title

EOF
```

### Vault Analysis Commands
```bash
find . -name "*.md" -type f | wc -l

grep -L "^type:" **/*.md 2>/dev/null | head -20

grep -h "^type:" **/*.md | sort | uniq -c | sort -rn

find . -name "*.md" -mtime -7 -type f | head -20
```

<!-- DYNAMIC: 아래 내용은 주기적으로 갱신됩니다. 검증이 필요할 수 있습니다. -->

## Critical Workflow Rules

1. **Code Output Lifecycle**: 볼트에서 시작한 경량 코드는 초기 `00. Inbox/03. AI Agent/{environment subfolder}/`, 기존 DEV 작업은 해당 프로젝트. 완료 JSON/PY는 [[90. Settings/94. Agent Settings/claude/rules/file-creation-rules|file-creation-rules]]의 Completed Artifact Closeout에 따라 외부 보관하고 기획·결과·경로·재개 방법은 메인 MD에 남긴다.
2. **Required Properties**: Every note needs 7 fields: type, aliases, **description** (English, LLM hint), author, date created, date modified, tags
3. **Properties v2.0 Standards**:
	- Dates: ISO 8601 (YYYY-MM-DD)
	- Author: `[[구요한]]` wikilink format
	- Status: Use standard 5 values only
	- CamelCase: myRate, totalPage (⚠️ `rating` 사용 금지 → 반드시 `myRate`)
	- **description**: English only, 1-2 sentences, skill-description style (what + when to reference)
4. **CMDS Hierarchy**: 🏛 (top) → 📖 (100-900) → 📚 (N01-N99) → no icon (details)
5. **Vault Scale**: 10,000+ notes with established patterns - respect existing conventions

## Key Obsidian Plugins

The vault uses 120+ plugins. Most important ones:
- **Dataview**: Dynamic queries and data aggregation
- **Copilot**: AI-powered writing assistance
- **Smart Connections**: AI-based note linking
- **Excalidraw/Excalibrain**: Visual thinking and diagramming
- **Chronology**: Timeline visualization
- **Calendar**: Date-based note organization

---
type: documentation
aliases:
  - System Files Changelog
  - 시스템 파일 변경 로그
description: Central version history for the 5 core CMDS system files (CLAUDE.md, AGENTS.md, CMDS.md, CMDS Guide, CMDS Head Quarter). Tracks schema changes, architecture upgrades, and frontmatter standard evolution. Reference when auditing version lineage or planning migrations.
author:
  - "[[구요한]]"
date created: 2026-04-01T11:30
date modified: 2026-05-04T00:10
tags: [CMDS, system, changelog]
CMDS: "[[📚 501 Obsidian]]"
---

# CMDS System Files — Changelog

> 공개 배포되는 5개 시스템 파일(CLAUDE.md, AGENTS.md, CMDS.md, 🏛 CMDS Head Quarter, 🏛 CMDS Guide)의 변경 이력을 추적합니다. 볼트 내부에는 추가로 3개 비공개 시스템 파일(ANTIGRAVITY.md, BRAIN.md, BRAIN_PROMPT.md)이 있어 총 8개로 운영되며, 이 3개는 vendor·product 전용이라 외부 배포 대상이 아닙니다.

---

## v4.5 — 2026-05-04 (4-Way Sync Workflow + Share Folder Restored)

**트리거**: v4.4 배포 직후 사용자 지적 — `40. Docs/47. CMDS Docs/cmds-system-files-share/` (sanitized 외부 공유본) 가 4월 18일 이후 16일간 stale 상태로 방치됨. 원인은 `system-docs-updater` 스킬의 옛 "Quick Update Command" 가 backup 만 다루고 share 는 별도 섹션으로 분리되어 있어 매번 누락됨. 운영 워크플로 자체를 4-way fan-out 으로 재설계.

### CLAUDE.md v3.5 → v3.6 (precedence 1)

"📦 System Files Deployment" 섹션 재작성:
- 단순 flow 다이어그램 → **4-way fan-out 다이어그램** (① 백업 → ② 공유 → ③ DEV → ④ Vercel 시각화)
- 단순 `vercel deploy` 명령 → **All-in-One bash 스크립트** (4 destinations 모두 처리, sed sanitize 포함)
- "⚠️ 누락 방지 룰" 박스 + 16일 stale 사고 사례 명시
- 자동화 흐름 설명도 4-way 명시로 갱신

### system-docs-updater 스킬 재구성

`~/.claude/skills/system-docs-updater/SKILL.md`:
- 기존 "Quick Update Command" (backup만) + 별도 "Quick Share Command" → **단일 "All-in-One Sync Command"** 통합
- "4-way Sync Pre-Deploy Checklist" 추가 (체크박스 4개 — 모두 ✅ 후에만 deploy)
- 누락 사고 패턴 #1, #2, #3 명시
- 자동 leak 검증 (`exit 1` if SANITIZE 룰 미커버 시 중단)
- Quick Verification Command 추가 (배포 후 즉시 실행 가능한 라이브 검증)

### Share 폴더 복구 + sanitization 강화

7개 share 파일 (5 system + SKILL_share + system-docs-map_share) 모두 즉시 재생성:
- SANITIZE 룰 확장 — 기존 5개 (`vault-path` · `구요한` · `바람빛교회` · ...) 에 5개 추가 (`Yohan Koo` · `johnfkoo951` · `Cmdspace.contact@gmail.com` · `dev-path` · `home`)
- 자동 leak 검증 통과 (실제 개인정보 0건)

### 영속화 (다음 세션부터 자동 적용)

3중 안전망:
1. **CLAUDE.md** (precedence 1, 항상 LLM 컨텍스트 로드) — 4-way 명시
2. **SKILL.md** — All-in-One Sync Command (구조적으로 누락 불가)
3. **메모리** (`feedback_system_files_4way_sync.md`) — MEMORY.md 인덱스에 추가, 모든 새 세션에서 자동 로드

### 검증 결과 (4 destinations 동시 갱신)

| Destination | Files | mtime | 상태 |
|-------------|:---:|:---:|:---:|
| ① 백업 | 6 | 00:06 | ✅ |
| ② 공유 | 7 | 00:06 | ✅ leak 0건 |
| ③ DEV | 5 + 8 rules + ZIP | 00:06 | ✅ |
| ④ Vercel | system.cmdspace.work | 200 OK | ✅ |

---

## v4.4 — 2026-05-03 (8-File Scheme + Codex/Antigravity Lanes)

**트리거**: 다중 AI agent 운영 정착 — Codex 일상 사용 본격화 + Antigravity (Google Gemini) 시스템 파일 모더나이즈 + 8개 system file 의 precedence 정합성 확보.

### 8-File System Scheme 확립

볼트 내 시스템 파일을 4 그룹 8 파일로 정렬 (precedence 1-8):

| Group | Files | Precedence |
|-------|-------|:---:|
| 🤖 LLM Coding Agents | CLAUDE.md · AGENTS.md | 1, 2 |
| 🧪 Vendor-Specific | ANTIGRAVITY.md (Gemini) | 3 |
| 📚 Context & Standards | CMDS.md · 🏛 Guide · 🏛 HQ | 4, 5, 6 |
| 🧠 Gobi Persona | BRAIN.md · BRAIN_PROMPT.md | 7, 8 |

**공개 배포 (이 사이트)**: precedence 1, 2, 4, 5, 6 — 즉 5개 파일. ANTIGRAVITY/BRAIN/BRAIN_PROMPT 는 vendor/product 전용이라 미배포.

### AI Agent Output Lanes — 6 → 8 lane

`00. Inbox/03. AI Agent/` 산출물 분리 lane 확장:

```
03-1/03-2: Claude Code (MBP / Studio)
03-3/03-4: OpenClaw (MBP / Studio)
03-5/03-6: Codex (MBP / Studio)        ← v4.3에서 추가
03-7/03-8: Antigravity (MBP / Studio)  ← v4.4에서 추가
```

odd = MBP, even = Studio 컨벤션.

### 파일별 변경 요약

- **CLAUDE.md** v3.4 → **3.5**: Antigravity 03-7/03-8 lane 반영, 배포 flow rules count 7→8 (blank-line-rules.md 포함), "8 system files 중 5개 공개" 명시
- **AGENTS.md** v2.4 → **2.5**: Antigravity 03-7/03-8 lane 추가, ANTIGRAVITY 가 별도 system file 임을 명시
- **CMDS.md** v2.4 → **2.5**: precedence 3→4 정렬 (ANTIGRAVITY 가 3 차지), Antigravity lane 본문 반영, stray numeric tag (`3`) 제거
- **🏛 CMDS Guide** v2.4 → **2.5**: precedence 4→5 정렬, Antigravity lane 추가, `94. System Prompts/` → `94. Agent Settings/claude/` 폴더 rename 반영, `99. Format/` 중복 entry 제거, Sync Settings lane 표기 갱신, Version History 백필 (v2.3/v2.4/v2.5)
- **🏛 CMDS Head Quarter** v1.3 → **1.4**: precedence 5→6 정렬, Antigravity 03-7/03-8 lane 추가
- **(비공개) ANTIGRAVITY.md** bare → **2.0**: 전체 modernization — 8-file scheme 의 precedence 3 vendor-specific 자리 부여, 죽은 `00. Inbox/03. Antigravity/` 경로를 03-7/03-8 lane 으로 교체, frontmatter 표준화 (description/audience/precedence/version/changelog 추가), Required Properties 5→7 (description 추가), 모든 룰 파일 `@` 참조 추가, file reference 3-way decision tree 반영

### 룰 (`.claude/rules/`)

- 8개 룰 파일 정렬 — `blank-line-rules.md` 신규 포함 (Obsidian-tight markdown 강제)
- `file-creation-rules.md`, `directory-structure.md` 모두 03-7/03-8 lane 반영
- `wikilink-rules.md` 대폭 확장 — 파일 참조 3종 결정 트리 (`[[wikilink]]` · `@import` · 백틱) + 외부 경로 / 코드 식별자 표기 가이드

### 정합성 검증

전수 스캔 결과:
- ✅ Precedence 1→2→3→4→5→6 완벽 정렬
- ✅ "5 Core Files" 잔존 0건 (전부 "8 system files"로 갱신)
- ✅ `03-1~03-4` outdated 표기 0건
- ✅ `03. Antigravity/` 죽은 경로 의도적 경고 2건만 잔존 (사용 금지 안내용)
- ✅ stray numeric tag artifact 제거 (CMDS `[..., 3]`, ANTIGRAVITY `[..., 1]`)

---

## v4.3 — 2026-04-19 (Visual Identity + Web Redesign)

**트리거**: 사용자 요청 — "시스템 파일 페이지를 새로운 웹 스타일로 리빌딩 하려 해" + 공식 CMDS 로고 에셋 6종 정식 등록 + OG 이미지 시스템 정비.

### 신규 페이지 · 구조 개편

- **랜딩 + 문서 분리**: `/` (마케팅 랜딩) · `/docs/` (기술 문서) · `/index-brutalist.html` (구버전 아카이브)
- **Editorial Documentation 스타일** 신규 구축 (Apple SF Pro × CMDS Green × Stripe docs 영감)
  - 3컬럼 레이아웃 (사이드바 · 본문 · TOC)
  - marked.js 로 MD 인라인 렌더 + YAML frontmatter 추출 표시
  - ⌘K Command Palette 전역 검색 (titles + file paths + fulltext + 하이라이팅)
  - 코드블록 progressive disclosure copy 버튼 (opacity 0.4 → pre:hover 0.85 → btn:hover 1)
  - KO/EN 토글 · Light/Dark 토글 · scroll spy · 자동 TOC · 더블클릭 스크롤 상/하단 토글

### 신규 에셋

- **공식 로고 6종 정식 등록** (`/assets/logos/`)
  - `cmds-logo-round.png` — 파비콘 · 헤더 brand mark (28px)
  - `cmds-logo-black.png` / `cmds-logo-white.png` — 아이콘 only
  - `cmds-logo-typo-black.png` / `cmds-logo-typo-white.png` — 로고 + 타이포 lockup
  - `cmds-typo-white.png` — 타이포 only
- **OG 이미지 시스템** (`/assets/og/`)
  - `og-landing.png` (1200×630, 라이트 녹색 그라디언트)
  - `og-docs.png` (1200×630, 다크 핑크 그라디언트)
  - `templates/*.html` 재생성용 HTML 템플릿
- **자동 빌드 스크립트** — `/scripts/build-og.sh` (Chrome headless 로 HTML → PNG 변환)

### CMDS Color System v2.0 → v2.5 대폭 확장

기존 v1.0 에서 2.5 로 5단계 진화 (볼트 `50. Assets/51. Brand/CMDS Color System.md`):

- **v2.0** — CI/BI 분리, 라이트/다크 토큰, Obsidian 그래프 팔레트, Apple 타이포 스택
- **v2.1** — Copy Button Progressive Disclosure, CSS Specificity 주의, Interaction Patterns (더블클릭 스크롤), Component Recipes
- **v2.2** — `.accent-word` 클래스 확정 (인라인 style 금지), Full-Bleed CTA 다크 핑크 그라디언트, Cross-Page Navigation
- **v2.3** — 공식 로고 에셋 6종 등록, Logo Usage Rules
- **v2.4** — 히어로 상단 로고 기본 사용 안 함 결정 (헤더 + 하단 lockup 으로 분산)
- **v2.5** — OG 이미지 시스템 정식 등록 (1200×630 규격, 메타 17종 체크리스트, 자동 생성 스크립트)

### CI/BI 디자인 결정 기록

- **Brand mark (로고)** — 테마 무관 `#134538` CMDS Dark Green 고정 (CI)
- **Primary CTA 버튼**:
  - 라이트: `#134538` + `#fff` 흰 글씨
  - 다크: **`#E985A2` CMDS Pink** + `#0b0f0d` 어두운 글씨
  - hover: `#1a5d4b` (green-hover) / `#D16C8A` (pink-dark)
- **Accent highlights** — 라이트=녹색 · 다크=핑크 자동 전환 (`.accent-word` 클래스)
- **Full-Bleed CTA 블록** — 라이트 녹색 그라디언트 / 다크 핑크 그라디언트

### 시스템 파일 업데이트

- **CLAUDE.md** — "📦 System Files Deployment" 섹션 신설 (Vercel · Cloudflare · DEV 폴더 · 배포 명령)
- **AGENTS.md** — "Public Deployment" 간결 요약 + CLAUDE.md 참조
- **CMDS.md** — "Public Deployment of System Files" 철학 수준 언급
- `date modified` 모두 2026-04-19

### 인프라 · 배포 명확화

- **Vercel 프로젝트 "cmds-system-files-v2"** 의 "v2" 는 인프라 세팅의 2차 시도 (v1 orphaned) — 시스템 파일 콘텐츠 버전 v4.x 와 **무관**
- DEV 폴더 `/Users/yohankoo/DEV/cmds-system-files/` 가 **배포 소스 폴더** 로 확정
- 배포 명령: `cd /DEV/cmds-system-files && vercel deploy --prod --yes`
- GitHub `johnfkoo951/cmds-system-files` 는 코드 히스토리 백업 (Vercel 자동 배포 연결 없음, 수동 배포)
- 도메인: Cloudflare DNS (`system.cmdspace.work` A record → `76.76.21.21` Vercel)

### 사용성 개선

- **Cross-Page Navigation** — docs 헤더에 "Home" + "GitHub" inline nav (랜딩 ↔ 문서 왕복)
- **더블클릭 빈 공간 → 스크롤 토글** — 상단 절반: 최하단 이동 · 하단 절반: 최상단 이동
- **KO/EN 토글 + Light/Dark 토글** — localStorage 저장, 시스템 다크모드 자동 감지
- **파비콘** — inline SVG `§` → 실제 라운드 로고 PNG 로 교체

### 공개 안내문

- 볼트 `70. Outputs/71. Published/2026-04-19-CMDS System Files 공개 안내문.md` 신설
- 6가지 버전: SNS 긴 (한/영) · 카카오톡 짧은 (한/영) · 카카오톡 3분할 (한/영)
- "Fork the architecture. Keep the philosophy." CMDSPACE 공식 tagline 확정

---

## v4.2 — 2026-04-15 (CMDS Process Command Suite)

**트리거**: 사용자 지시 — "cmds 프로세스에 맞게 connect merge develop share 로 하면 어떨까? inbox 명령어는 인박스 파악하는데 쓰고 c m d s 명령어들 통해서 각각 프로세스에 맞게 구조화하는 것이 중요할듯."

### 신규 파일 생성 (8개 슬래시 커맨드)

`90. Settings/94. Agent Settings/claude/commands/` 에 8개 커맨드 파일 신설:

1. `inbox.md` — 9개 inbox 서브폴더 스캔 + AskUserQuestion 라우팅 (router only)
2. `connect.md` — inbox → 📖 100 Themes, 자동 분류·중복제거·stub (low-friction)
3. `merge.md` — N개 노트 → 1개 📖 200 Literature, multi-dialog 합성 (heaviest)
4. `develop.md` — method 적용 + artifact 생성 (code/prompt/curriculum/specialty)
5. `share.md` — 기존 skills 자동 위임 오케스트레이션 (thebetter-writer, markdown-slides 등)
6. `lint.md` — 단계별 위생 점검 scope (inbox/connect/merge/develop/share/all)
7. `query.md` — 볼트 + LLM Wiki 검색, 결과는 해당 CMDS 카테고리에 file-back (별도 폴더 X)
8. `status.md` — 단계별 노트 수 + 추천 액션 one-screen snapshot

### 5개 시스템 파일 업데이트

1. **CLAUDE.md** — "CMDS Process Command Suite (2026-04-14+)" 섹션 신설 (Cross-Vault Query 다음)
	- 8 커맨드 역할 표, 결정 트리, 설계 결정 기록, 전형적 세션 패턴
2. **AGENTS.md** — "CMDS Process Command Suite" 섹션 신설 (Templates 다음)
	- 다른 AI 에이전트용 요약 + slash command 미지원 런타임에서의 대안 가이드
3. **CMDS.md** — "Command Suite: CMDS Process as Operational Verbs" 섹션 신설 (Working with CMDS System 안)
	- 커맨드를 CMDS Process 의 operational verb 로 격상, 철학/맥락 해설
4. **🏛 CMDS Guide.md** — "CMDS Process Command Fields (v2.2, 2026-04-14+)" 섹션 신설 (Properties 안)
	- 신규 v2 프로퍼티 10개 공식 등록 (mergePurpose, sourceNotes, mainVaultRelated, developSources, shareSourceNotes, shareFormat, sharePurpose, queryOrigin, querySources, sourceInbox)
5. **🏛 CMDS Head Quarter.md** — "CMDS Process Commands (2026-04-14+)" 섹션 신설 (CMDS Process 다음)
	- 네비게이션 허브에 8 커맨드 한 줄 요약 등재

### 주요 설계 결정 (사용자 승인)

1. **Vocabulary**: LLM Wiki 의 ingest/query/lint 대신 CMDS Process (Connect/Merge/Develop/Share) 어휘 채택. Satellite 와 mothership 의 workflow 언어 분리.
2. **Inbox = Router only**: `/inbox` 는 절대 write 안 함. `AskUserQuestion` 으로 multi-select 스코프 받고 stage 커맨드로 위임.
3. **Share = Orchestrator only**: `/share` 는 content 직접 작성 금지. 기존 13개 skills (thebetter-writer, markdown-slides, tone-writer, pptx-cmds, series-writer, social-media-content-adapter, course-designer, markdown-video, business-docs 등) 로 자동 라우팅.
4. **Query results ≠ separate folder**: 사용자 정책 "내 모든 노트가 쿼리의 소재이고 결과" — `/query` 결과는 적합한 CMDS 카테고리 (220 Personal Insights, 210 Literature Reviews 등) 로 분류. LLM Wiki 의 `30. Queries/` 같은 origin-based 폴더 구조 거부.
5. **Automation density**: `/connect` auto-pilot (dialog 0~1회), `/merge` 의도적 multi-dialog (synthesis = 정보 손실), `/develop`+`/share` 결정 지점 1~2회, `/lint`+`/status` zero-dialog.
6. **AskUserQuestion 표준화**: stage 커맨드 모두 MCP 도구 사용, `multiSelect` 가능한 경우 활용, max 4 options, "(Recommended)" 첫 번째.
7. **CMDS 카테고리 = 메타데이터**: 100/200 물리 폴더 없음. 모든 노트는 `30. Permanent Notes/`, `60. Collections/` 등 기존 구조에 저장되고 `CMDS:` + `index:` frontmatter 로 카테고리 등록.

### 메모리 파일 신규

`~/.claude/projects/.../memory/cmds-process-commands.md` — 커맨드 존재 + 사용 정책 reference 메모리 추가.

### 왜 v4.2인가

- v4.0/v4.1 이 frontmatter schema 확장이었다면, v4.2 는 **operational layer** 추가.
- 문서 구조나 프로퍼티 schema 는 v4.1 유지 — 새 프로퍼티 10개가 추가됐지만 기존 노트 호환성은 그대로 (backward compatible).
- 가장 큰 변화는 **파일이 아닌 워크플로** — CMDS Process 가 철학에서 실행 가능한 커맨드로 구현됨.

---

## v4.1 — 2026-04-07 (Description Field Standardization)

**트리거**: 사용자 지시 — "생성하는 문서에 항상 YAML에 description 필드를 만들고 영어로 LLM용 설명을 작성하자"

### 변경 사항

1. **필수 프로퍼티 6개 → 7개**
	- `description` 필드가 7번째 필수 프로퍼티로 승격
	- **반드시 영어로 1-2문장** 작성 — LLM의 관련성 판단용 기계 가독 힌트
	- Skill/tool description 스타일: "무엇을 담고 있는가 + 언제 참조해야 하는가"

2. **`.claude/rules/frontmatter-standard.md`** (공용 규칙 업데이트)
	- 필수 프로퍼티 블록에 `description:` 추가
	- Rule #6 신설: "description must be in English"
	- ✅ Good / ❌ Bad 예시 제공

3. **시스템 파일 5개 개별 버전 bump**
	- CLAUDE.md: 3.0 → **3.1**
	- AGENTS.md: 2.0 → **2.1**
	- CMDS.md: 2.1 → **2.2**
	- 🏛 CMDS Guide.md: 2.2 → **2.3**
	- 🏛 CMDS Head Quarter.md: 1.1 → **1.2**

4. **5개 파일 description 필드 영어 변환** (exemplar 역할)
	- 기존 한국어 설명 → 영어 1-2문장으로 재작성
	- 모든 파일이 "what + when to reference" 패턴 준수

5. **CLAUDE.md Pre-Flight Checklist 항목 추가**
	- `[ ] description field present and in English`

6. **CLAUDE.md / AGENTS.md / CMDS.md Essential (Post-Compact) 업데이트**
	- "필수 프로퍼티 6개" → "필수 프로퍼티 7개"

7. **Feedback 메모리 저장**
	- `~/.claude/projects/-Users-yohankoo/memory/feedback_yaml-description-english.md`

### 왜 v4.1인가

- v4.0(2026-04-01) Architecture Upgrade의 연장선 — frontmatter schema를 한 필드 확장
- 과거 v2.0 → v2.1(Frontmatter Standard) 패턴과 동일한 성격의 Minor bump
- 기존 6-프로퍼티 노트들과 호환됨 (추가일 뿐 breaking change 아님)

---

## v4.0 — 2026-04-01 (Architecture Upgrade)

**영감**: Claude Code 소스 코드 아키텍처 분석 → 9개 패턴 적용

### 신규 파일 생성
- `.claude/rules/indentation-rules.md` — YAML 2spaces / MD tab 공통 규칙
- `.claude/rules/frontmatter-standard.md` — 필수 6프로퍼티 + 포맷 규칙
- `.claude/rules/file-creation-rules.md` — 출력 경로, 네이밍, 프로젝트 폴더 규칙
- `.claude/rules/wikilink-rules.md` — 옵시디언 위키링크 문법 + YAML 인용 규칙
- `.claude/rules/directory-structure.md` — 볼트 폴더 구조 + CMDS 카테고리

### 전체 파일 공통 변경
1. **`precedence` 추가** — 파일 간 우선순위 명시 (1=CLAUDE → 5=HQ)
2. **`memory-type` 추가** — Claude Code memdir 타입 매핑 (feedback/user/reference)
3. **`required-for` / `optional-for` 추가** — 에이전트 스코핑 (어떤 작업에 이 파일이 필수/선택인지)
4. **`token-estimate` 추가** — 토큰 예산 의식 (AI가 어떤 파일을 우선 로드할지 판단)
5. **`changelog` 추가** — 각 파일 frontmatter에 버전 이력 내장
6. **`<!-- STATIC -->` / `<!-- DYNAMIC -->` 마커** — 캐시 가능 영역 vs 갱신 필요 영역 구분
7. **`## Essential (Post-Compact)` 섹션** — 컨텍스트 압축 후 복구용 핵심 규칙 요약

### 파일별 변경

#### CLAUDE.md (v2.1 → v3.0)
- 중복 규칙을 `@.claude/rules/` 로 분리 (@include 5개)
- Critical Rules 섹션: 인라인 규칙 → @include 참조로 전환
- Pre-Flight Checklist 유지 (빠른 확인용)
- Directory Structure: @include로 교체
- File Creation Rules: @include로 교체
- Note Types 통계 업데이트 (최신 수치 반영)
- Related System Files에 precedence 번호 추가
- `[[wikilink]]`는 옵시디언 탐색용으로 유지, `@include`는 AI 로딩용으로 분리
- 토큰 약 21KB → 예상 ~14KB (rules 포함 시 동일하나 공유 가능)

#### AGENTS.md (v1.0 → v2.0)
- 중복 규칙 60% 제거 → @include 4개로 교체
- Critical Rules 전체를 @include 기반으로 전환
- Directory Structure를 @include로 교체
- 고유 섹션만 유지: Note Types, Status Values, File Prefixes, Templates
- 토큰 약 9KB → 예상 ~5KB (rules 포함 시 동일하나 공유 가능)

#### CMDS.md (v2.0 → v2.1)
- frontmatter 강화: precedence(3), memory-type(user), required-for, token-estimate
- Essential (Post-Compact) 섹션 추가 — 5개 핵심 컨텍스트
- `<!-- STATIC -->` 마커 추가 (System Documentation Overview 이전)
- `<!-- DYNAMIC -->` 마커 추가 (Vault Statistics 이전)
- changelog 필드 추가

#### 🏛 CMDS Head Quarter (→ v1.1)
- frontmatter 강화: precedence(5), memory-type(reference), required-for, token-estimate
- version, changelog 필드 추가

#### 🏛 CMDS Guide (v2.1 → v2.2)
- frontmatter 강화: precedence(4), memory-type(reference), required-for, token-estimate
- tags 정리: 불필요한 태그 제거 (태그는자유로워야지, maps, example, service)
- changelog 필드 추가

### @include vs [[wikilink]] 사용 원칙

| 용도 | 문법 | 예시 |
|------|------|------|
| **AI가 내용을 인라인 로드** | `@path` | `@.claude/rules/indentation-rules.md` |
| **옵시디언 내부 탐색/링크** | `[[name]]` | `[[🏛 CMDS Guide]]` |
| **양쪽 모두 필요** | 둘 다 사용 | `@CMDS.md → [[CMDS.md]]` |

- `@include`: AI 에이전트가 파일 내용을 실제로 읽어야 할 때 (규칙, 구조 정의)
- `[[wikilink]]`: 사용자가 옵시디언에서 클릭하여 이동할 때 (탐색, 참조)
- Related System Files 같이 양쪽 다 필요한 경우: `@파일 → [[파일]]` 형태로 병기

---

## v2.1 — 2026-03-30 (Frontmatter Standard)

### 변경 사항
- 5개 파일 모두 frontmatter에 `description`, `audience`, `scope` 추가
- AI Documents: `type: documentation` 통일
- Human Documents: `type: CMDS` 유지
- 백업/공유 폴더를 `40. Docs/47. CMDS Docs/`로 이동
- system-docs-updater 스킬에 frontmatter 표준 섹션 추가

---

## v2.0 — 2026-03-15 (Full Review)

### 변경 사항
- 5개 파일 전면 리뷰 및 통계 갱신 (5,344+ → 10,000+)
- CLAUDE.md: 백업 경로 오타 수정, GenAI Chats 추가
- CMDS.md: PhD Candidate → PhD ABD, AI Tools 갱신, 50. Assets 섹션 추가
- 🏛 CMDS Head Quarter: CMDS Process 설명 추가, Vault Folders 섹션 추가
- 🏛 CMDS Guide: 폴더 구조 현행화, 새 type 추가
- AGENTS.md: 볼트 규모 갱신
- 백업/공유 파일 동기화
- 에세이 시리즈 9편 작성
- 웹페이지 v3 배포 (system.cmdspace.work)
- ChatGPT 시스템 프롬프트 생성

---

## v1.0 — 2025-09-27 (Initial)

### 생성
- CLAUDE.md 최초 작성
- 이후 AGENTS.md, CMDS.md, Guide, HQ 순차 추가

---

## 파일 위치 참조

| 구분 | 경로 |
|------|------|
| **정본 (5개)** | 볼트 루트: `/CLAUDE.md`, `/AGENTS.md`, `/CMDS.md`, `/🏛 CMDS Head Quarter.md`, `/🏛 CMDS Guide.md` |
| **공통 규칙 (5개)** | `.claude/rules/indentation-rules.md`, `frontmatter-standard.md`, `file-creation-rules.md`, `wikilink-rules.md`, `directory-structure.md` |
| **백업** | `40. Docs/47. CMDS Docs/cmds-system-files/` (`_backup.md`) |
| **공유본** | `40. Docs/47. CMDS Docs/cmds-system-files-share/` (`_share.md`) |
| **웹 배포** | [system.cmdspace.work](https://system.cmdspace.work) |
| **GitHub** | [johnfkoo951/cmds-system-files](https://github.com/johnfkoo951/cmds-system-files) |
| **변경 로그** | 이 파일 (`40. Docs/47. CMDS Docs/cmds-system-files/CHANGELOG.md`) |

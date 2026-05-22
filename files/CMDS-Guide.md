---
type: CMDS
aliases:
  - CMDS Guide
  - guide
description: "Operational standards guide for the CMDS vault. Defines the 7 required Properties, standard note types, file naming conventions, folder structure, citation styles, and template examples. Reference when creating new notes or validating existing ones."
author:
  - "[[구요한]]"
date created: 2025-09-15T23:39
date modified: 2026-05-20T14:11
tags: [CMDS, system, guideline, NoteClass, operation, 태그는자유로워야지, index, maps, example, service]
audience: User + AI
scope: operational-standards
precedence: 5
memory-type: reference
required-for:
  - file-creation
  - standards-compliance
optional-for:
  - search
  - analysis
token-estimate: 4800
links: []
index: "[[🏛 CMDS Head Quarter]]"
version: "2.6"
status: completed
changelog:
  - "2.6 (2026-05-20): Tags noise 정리 — `태그는자유로워야지`, `maps`, `example`, `service`, `index` 제거 (vault 일반 태그 시스템과 의미 충돌). Last Updated 헤더 동기화."
  - "2.5 (2026-05-03): Aligned precedence to 8-file scheme (4→5). Added Antigravity 03-7/03-8 output lanes. Fixed `94. System Prompts/` → `94. Agent Settings/claude/` (folder rename was missed). Removed duplicate `99. Format/` entry. Updated Sync Settings lane reference (03-1~03-4 → 03-1~03-8). Backfilled Version History with v2.3/v2.4/v2.5 entries."
  - "2.4 (2026-05-03): Added Codex MBP/Studio AI Agent folders and clarified description double-quote examples."
  - "2.3 (2026-04-07): 필수 프로퍼티 7개로 확장 (description 추가, English required for LLMs)"
  - "2.2 (2026-04-01): precedence/memory-type/token-estimate 추가, tags 정리"
  - "2.1 (2026-03-15): 폴더 구조 현행화, 새 type 추가"
share: true
share_link: https://canny-buffalo-436.convex.site/note/bq2eal9k.html
share_expires: 2026-01-29T11:02:12.926Z
---

# CMDS Guide

> **🔄 Last Updated: 2026-05-20** | Backup: `40. Docs/47. CMDS Docs/cmds-system-files/CMDS-Guide_backup.md`
>
> 📌 **Version 2.5** - Properties 표준화 + 8-file precedence 정렬 + Antigravity lane 반영판

## Properties
### 필수 Properties (Required)
모든 노트는 다음 7개의 필수 properties를 포함해야 합니다:
```yaml
---
type:           # 노트 유형 (아래 표준 type 참조)
aliases: []     # 별칭 (배열 형식)
description: "" # 1-2 문장 영어 요약 (LLM용, 반드시 double quote)
author:
  - "[[구요한]]"  # 작성자 (wikilink 형식)
date created:   # 생성일 (YYYY-MM-DDTHH:mm:ss)
date modified:  # 수정일 (YYYY-MM-DDTHH:mm:ss)
tags: []        # 태그 (배열 형식)
---
```

> ⚠️ **`description` 작성 규칙** (2026-04-07 추가)
> - **반드시 영어로 작성**. LLM(Claude Code, Gemini CLI, ChatGPT 등)이 이 노트의 관련성을 판단할 때 사용하는 기계 가독 힌트입니다.
> - **1-2 문장**, skill/tool description처럼 구체적이고 action-oriented하게.
> - 노트의 내용 + 언제 참조해야 하는지를 함께 제공.
> - ✅ 좋음: `"Meeting minutes from 2026-04-07 LG AX camp retrospective. Contains CEO feedback and next-action items."`
> - ❌ 나쁨: `"회의록"` (한국어), `"This is a note"` (무정보)
### 표준 Properties 정의
#### 날짜 관련
- `date created` - 생성일 (YYYY-MM-DDTHH:mm:ss)
- `date modified` - 수정일 (YYYY-MM-DDTHH:mm:ss)
- `date` - 이벤트/미팅 날짜 (YYYY-MM-DD)
- `publish_date` - 발행일 (YYYY-MM-DD)
- `year` - 연도 (YYYY)
> ⚠️ **통일 규칙**: 모든 날짜는 ISO 8601 형식 (YYYY-MM-DD) 사용

#### 작성자 및 관계
- `author: [[구요한]]` - 항상 wikilink 형식 사용
- `attendees: []` - 참석자 목록 (wikilink 배열)
- `organization: [[조직명]]` - 조직 (wikilink)

#### 분류 및 상태
- `type` - 노트 유형 (아래 표준 type 목록 참조)
- `CMDS` - CMDS 카테고리 연결 (예: `[[📚 620 Generative AI]]`)
- `index` - 인덱스 참조 (예: `[[🏷 Meeting Notes]]`)
- `status` - 상태값
	- ✅ 표준값: `unread` | `reading` | `inProgress` | `completed` | `archived`

#### 평가 및 측정
- `myRate` - 평점 (1-5 scale, 숫자)
- `totalPage` - 총 페이지 수 (camelCase)
- `views` - 조회수

#### 연결 및 참조
- `aliases: []` - 별칭 (배열 형식으로 통일)
- `tags: []` - 태그 (배열 형식으로 통일)
- `links` - 관련 링크
- `source` - 출처
- `source_url` - 출처 URL
- `bookends` - 북엔드 (기존 유지)
- `CMDS` - CMDS 카테고리 참조

#### CMDS Process Command Fields (v2.2, 2026-04-14+)

CMDS Process 슬래시 커맨드 (`/connect`, `/merge`, `/develop`, `/share`, `/query`) 가 자동으로 기록하는 프로퍼티. 모두 **camelCase**, 배열 필드는 quoted wikilink.

| 필드                     | 기록하는 커맨드           | 용도                                                                         |
| ---------------------- | ------------------ | -------------------------------------------------------------------------- |
| `sourceInbox: []`      | `/connect`         | Theme stub 이 어느 inbox 파일에서 캡처됐는지 배열로 기록                                    |
| `mergePurpose: ""`     | `/merge`           | 합성 목적 (7 재활용 축 중 하나 + 한 줄 맥락). 다운스트림 `/share` 의 format 자동 추천에 사용           |
| `sourceNotes: []`      | `/merge`           | 합성에 쓰인 후보 노트들의 wikilink 배열 (N→1 traceability)                              |
| `mainVaultRelated: []` | `/merge`, `/query` | LLM Wiki satellite vault 페이지 참조 (text ref 형식: `"→ LLM Wiki: {page name}"`) |
| `developSources: []`   | `/develop`         | artifact 가 참조한 method/data/specialty 노트들                                   |
| `shareSourceNotes: []` | `/share`           | 산출물이 어느 합성 노트에서 나왔는지                                                       |
| `shareFormat: ""`      | `/share`           | newsletter / slides / video / social / article / proposal 등                |
| `sharePurpose: ""`     | `/share`           | 왜 이 share 가 일어났는지 (예: "4월 LG CNS 강의용")                                     |
| `queryOrigin: ""`      | `/query`           | 원 질문 verbatim (file-back 된 답변 노트에 기록)                                      |
| `querySources: []`     | `/query`           | 답변 합성에 쓰인 노트 배열                                                            |

사용 예시 (merge 된 Literature 노트):

```yaml
---
type: note
aliases: []
description: "Synthesized analysis comparing RAG and Compiled Wiki patterns for team research sharing workflows. Reference when deciding between retrieval-based vs pre-compiled knowledge architectures."
author:
  - "[[구요한]]"
date created: 2026-04-14
date modified: 2026-04-14
tags:
  - merged
  - rag
  - knowledge-management
  - literature-review
CMDS: "[[📖 200 Literature]]"
index: "[[📚 210 Literature Reviews]]"
status: completed
mergePurpose: "강의·강연 — 주간 팀 리서치 공유 워크플로 재설계"
sourceNotes:
  - "[[RAG 한계 분석]]"
  - "[[Compiled Wiki 운영 경험]]"
  - "[[팀 지식 공유 패턴]]"
related:
  - "[[📚 601 Knowledge Management]]"
mainVaultRelated:
  - "→ LLM Wiki: RAG vs Compiled Wiki"
  - "→ LLM Wiki: Shared State Pattern"
---
```

> **구현 위치**: 커맨드 정의는 `90. Settings/94. Agent Settings/claude/commands/` 폴더 참조. 전체 커맨드 사용법은 [[CLAUDE.md]] "CMDS Process Command Suite" 섹션 참조.

### 표준 Type 목록
#### 주요 노트 타입
- `note` - 일반 노트
- `terminology` - 용어 정의
- `meeting` - 회의록
- `people` - 인물 정보
- `curriculum` - 강의 커리큘럼
- `memo` - 메모
- `class` - 수업 관련
- `manuscript` - 원고/초안
- `daily-note` - 일일 노트
- `article` - 글/기사
- `sermon` - 설교
- `review` - 리뷰/연구평론
- `project` - 프로젝트
- `zettel` - 제텔카스텐 노트
#### 구조/조직 타입
- `CMDS` - 커맨드스페이스 인덱스
- `organization` - 조직/기관
- `portal` - 포털 페이지
- `documentation` - 문서화/가이드
- `index` - 색인
- `CMDS` - CMDS 인덱스 페이지
#### 콘텐츠 타입
- `books` - 도서
- `research-review` - 연구 리뷰
- `research-pipeline` - 연구 파이프라인
- `api` - API 문서
- `moc` - Map of Content
- `idea` - 아이디어
- `resource` - 리소스
- `product` - 제품/서비스
### Tags
- 태그는 자유롭게 #태그는자유로워야지
- Nested tags 예시:
	- `#Author/Koo`
	- `#가이드/태그작성법`
	- `#가이드/목차작성법`
## Collections
### CMDS
- [[🏛 CMDS Head Quarter]]
- [[🏛 CMDS Guide]]
### Index
#index #NoteClass #maps
- [[🏷 Guideline]]
- [[🏷 Daily Notes]]
- [[🏷 Research Notes]]
- [[🏷 Project Notes]]
- [[🏷 Lecture Notes]]
- [[🏷 Review Notes]]
- [[🏷 Draft Article]]
- [[🏷 Web Clips]]
- [[🏷 Waypoint]]
- [[🏷 Meeting Notes]]
- [[🏷 People]]
- [[🏷 Organization]]
- [[🏷 Prompts]]
- [[🏷 Syntax and Codes]]
- [[🏷 Recordings]]
### Backlinks
- 백링크는 내 인지범위가 허락하는 선까지 [[]]
- 한 번에 다 할 필요는 없음
- Gen AI 사용하여 자동 연결 시킬 수 있음
	- Smart Composer - YAML, In-line
	- [[00. Inbox/GPT에게 용어정리 시키기|GPT에게 용어정리 시키기]]
	- Claude Code
## CMDS Levels
### 계층 구조
- 🏛 - Home, Guide (최상위)
- 📖 - 1st level CMDS (100-900 시리즈)
	- Space Collection
	- 1 digit (100-900)
- 📚 - 2nd level CMDS (N01-N99)
	- Spaces
	- 2 digit (N01-N99)
- (No Icon) - 3rd level CMDS
	- 상세 주제는 3rd level CMDS로 분류
### CMDS Level Example
```
📚 840 Lectures
├── 840.01 University Courses
│   ├── 840.01-A 차의과학대학교
│   │   ├── 840.01-A1 2024-1
│   │   │   └── [[생성형 AI 기초와 활용]]
│   │   └── 840.01-A2 2024-2
│   │       └── AI 융합 연구방법론
│   └── 840.01-B 한양대학교
```
## Filename Conventions
### 접두사(Prefix)
#### Wis' Rule
- `u.` - usecase #example
- `f.` - feature #operation
- `p.` - product #service
#### Input
- 📎 - Web Clips (W@)
- 🌿 - Readwise (WW@)
- 📘 - Books, Reference `#📚Book`
#### Process
- 🏷 - Index (E@)
- 📦 - Review (EE@)
- 📐 - Variables (EEEE@)
#### Output
- 🔖 - Output from YHN's Idea (R@)
- 📜 - Output from Other's Idea (RR@)
- 📈 - Code and Syntax (RRR@)
- 🎹 - Music (RRRR@)
- 🏙 - Canvas (F@)
#### References
- 📕 - Bible (EEE@)
### 접미사(Suffix)
#### Service에 따라
- `.obsidian`
- `.python`
- `.chatgpt`
- `.claude`
- `.midjourney`
#### Purpose에 따라
- `.meeting`
- `.portal`
## Folder Structure
```
00. Inbox/                      # 임시 저장 및 처리 공간
├── 01. Daily Notes/            # 데일리 노트 (01-1. Planners, 01-2. Weekly Notes)
├── 02. Clippings/              # 웹 클리핑 (02-1. Literature Notes)
├── 03. AI Agent/               # ⭐ AI 코드 작업 전용 (PRIMARY)
│   ├── 03-1. Claude Code (MBP)/    # Claude Code — MacBook Pro
│   ├── 03-2. Claude Code (Studio)/ # Claude Code — Mac Studio
│   ├── 03-3. OpenClaw (MBP)/       # OpenClaw — MacBook Pro
│   ├── 03-4. OpenClaw (Studio)/    # OpenClaw — Mac Studio
│   ├── 03-5. Codex (MBP)/          # Codex — MacBook Pro
│   ├── 03-6. Codex (Studio)/       # Codex — Mac Studio
│   ├── 03-7. Antigravity (MBP)/    # Antigravity (Google) — MacBook Pro
│   └── 03-8. Antigravity (Studio)/ # Antigravity (Google) — Mac Studio
├── 04. Excalidraw/             # 다이어그램
├── 05. Canvas/                 # Canvas 노트
├── 06. Automation/             # 자동화 (06-1. Make.com, 06-2. n8n Lecture, 06-3. STT)
├── 06. GenAI Chats/            # GenAI 대화 기록
├── 07. App Sync/               # 외부 앱 연동 (07-1. Claude, 07-2. Antigravity, 07-3. Bear Notes)
├── 08. Unlisted/               # 미분류
└── 09. Legacy/                 # 레거시 컨텐츠

10. CMDS Process/               # CMDS 프로세스 워크플로우
├── 11. Connect/                # 배우고있는것들 #capture
├── 12. Merge/                  # 내주제와연결 #Areas #organize
├── 13. Develop/                # #distill
└── 14. Share/                  # 완성된산출물 #express

20. Literature Notes/           # 문헌 노트 및 리뷰
├── 21. Lit Notes (Zotero)/     # Zotero 연동 문헌
├── 21. Web Articles/           # 웹 아티클 (빈 폴더)
├── 22. Reviews/                # 리뷰 및 분석
├── 23. Sermon/                 # 설교 노트
├── 24. Web Articles/           # 웹 아티클
├── 28. Flashcards/             # 플래시카드
└── 29. Terminologies/          # 용어 정리

30. Permanent Notes/            # 영구 노트 (Evergreen)
├── 33. Essay/                  # 에세이
├── 34. Prompt and Syntax/      # 프롬프트 및 문법
└── 39. Guideline/              # 가이드라인

40. Docs/                       # 기술 문서 (Technical Documentation)
├── 41. Official Docs/          # 공식 문서, API 가이드, 제품 매뉴얼
├── 42. AI Generated/           # AI 생성 기술 문서
├── 43. Audio Files/            # 오디오 파일
├── 44. Transcripts/            # 트랜스크립트
├── 45. Partner Made/           # 파트너 제작 문서
├── 46. My Docs/                # 사용자 작성 기술 문서
├── 47. CMDS Docs/              # CMDS 시스템 관련 문서
└── 49. API Information/        # API 정보 및 레퍼런스

50. Assets/                     # 미디어 및 자산
├── 51. Brand/                  # 브랜드 자산
├── 51. Prompt/                 # 프롬프트 자산
├── 51. Prompt and Syntax/      # 프롬프트 및 문법
├── 52. Workflow/               # 워크플로우 자산
└── 59. Obsidian Web Clipper/   # 웹 클리퍼 템플릿

60. Collections/                # 엔티티 관리 컬렉션
├── 61. People/                 # 인물 데이터베이스
├── 62. Organization/           # 조직/기관
├── 63. Meetings/               # 회의록
├── 64. Spirituality/           # 영성 콘텐츠 (성경, 설교)
├── 67. Bases/                  # 데이터베이스 구조
├── 68. Kanban Board/           # 칸반 보드
├── 68-1. Portal/               # 포털 페이지
└── 69. Preferences/            # 개인 선호 (Alcohol, Sleep, Jazz)

70. Outputs/                    # 최종 산출물
├── 71. Published/              # 발행 콘텐츠
├── 72. Presentations/          # 발표 자료
├── 73. Courses/                # 교육 과정
├── 74. Projects/               # 프로젝트 문서
├── 75. Consulting/             # 컨설팅 산출물
└── 79. Portfolio/              # 포트폴리오

80. References/                 # 참고 자료 및 출처
├── 81. Attachment/             # 첨부 파일
├── 82. Web Articles/           # 웹 아티클
├── 83. References/             # 일반 참고자료
├── 84. References (Zotero)/    # Zotero 참고문헌
├── 85. References (Book)/      # 도서 참고자료
├── 86. Omnivore/               # Omnivore 아티클
├── 86. References (Book, Yes24)/ # Yes24 도서
└── 89. Omnivore/               # Omnivore 추가

90. Settings/                   # 시스템 설정 및 관리
├── 91. Templates/              # 노트 템플릿
├── 92. Templates (archived)/   # 아카이브 템플릿
├── 93. Generated Text/         # AI 생성 텍스트
├── 94. Agent Settings/         # AI agent 원본 (.claude/ symlink target)
│   └── claude/
│       ├── agents/             # Claude subagent 정의
│       ├── commands/           # CMDS Process 슬래시 커맨드
│       ├── rules/              # 8개 공통 룰 .md
│       └── skills/             # Claude Code skills
├── 95. Fonts/                  # 폰트 파일
├── 96. Index/                  # 인덱스 파일
├── 97. File Class/             # 파일 분류
├── 98. Format/                 # 포맷 정의
└── 99. Others/                 # 기타 설정
```
## Properties Template Examples
### 기본 노트 템플릿
```yaml
---
type: note
aliases: []
author:
  - "[[구요한]]"
date created: 2025-01-09T14:30
date modified: 2025-01-09T14:30
tags: []
CMDS: 
index: 
status: 
---
```
### 회의록 템플릿
```yaml
---
type: meeting
aliases: []
author:
  - "[[구요한]]"
date created: 2025-01-09T09:00
date: 2025-01-09
attendees:
  - "[[참석자1]]"
  - "[[참석자2]]"
organization: "[[조직명]]"
CMDS: "[[📚 831 Consulting]]"
index: "[[🏷 Meeting Notes]]"
status: inProgress
tags: [meeting]
---
```
### 연구 노트 템플릿
```yaml
---
type: research-review
aliases: []
author:
  - "[[구요한]]"
date created: 2025-01-09T16:45
title: 
source: 
source_url: 
doi: 
keywords: []
CMDS: "[[📚 820 Research]]"
index: "[[🏷 Research Notes]]"
status: reading
tags: [research]
---
```
### 도서 노트 템플릿
```yaml
---
type: books
aliases: []
author:
  - "[[구요한]]"
date created: 2025-01-09T11:20
title: 
subtitle: 
isbn: 
publisher: 
publish_date: 
totalPage: 
myRate: 
status: unread
CMDS: "[[📚 240 Books]]"
index: "[[🏷 Books]]"
tags: [📚Book]
---
```
### 인물 노트 템플릿
```yaml
---
type: people
aliases: []
author:
  - "[[구요한]]"
date created: 2025-01-09T10:15
email: 
mobile: 
organization: "[[조직명]]"
group: 
CMDS: 
index: "[[🏷 People]]"
status: 
tags: [people]
---
```
## Property 네이밍 규칙 (Naming Convention)

CMDS 볼트에서 YAML 프로퍼티 이름을 지을 때 따르는 규칙입니다.

### camelCase (카멜케이스) — 복합 단어 프로퍼티의 기본 규칙

두 단어 이상을 조합할 때, **첫 단어는 소문자**, **이후 단어의 첫 글자만 대문자**로 쓰는 방식입니다. 낙타(camel)의 등처럼 중간이 올라가는 모양이라 카멜케이스라고 부릅니다.

```yaml
# ✅ camelCase (CMDS 표준)
myRate: 5
totalPage: 320
startReadDate: 2026-03-30
channelUrl: "https://youtube.com/@example"
updateFrequency: weekly

# ❌ 잘못된 예시
my_rate: 5        # snake_case — 사용 금지
my-rate: 5        # kebab-case — YAML에서 문제 가능
MyRate: 5         # PascalCase — 사용 금지
```

### snake_case (스네이크케이스) — 레거시 호환

단어 사이를 밑줄(`_`)로 연결하는 방식입니다. 뱀(snake)처럼 바닥에 붙어 있는 모양입니다. CMDS에서는 **기존에 이미 대량으로 사용 중인 프로퍼티**에 한해 유지합니다.

```yaml
# ⚠️ snake_case (레거시 유지 — 신규 사용 금지)
source_url: "https://example.com"   # 250+ 파일에서 사용 중
publish_date: 2026-01-15            # 138+ 파일에서 사용 중
recommended_by:                      # Book Base 생태계 호환
  - "[[이남정]]"
```

### 단일 단어 — 그대로 소문자

한 단어로 된 프로퍼티는 그냥 소문자입니다.

```yaml
type: note
platform: YouTube
language: Korean
status: completed
```

### Obsidian 기본값 — 공백 허용

Obsidian이 자동 생성하는 프로퍼티는 공백 형태를 유지합니다.

```yaml
date created: 2026-03-30
date modified: 2026-03-30
```

### 요약 표

| 패턴 | 사용 시점 | 예시 |
|------|----------|------|
| **camelCase** | 새로운 복합 단어 프로퍼티 (기본) | `myRate`, `totalPage`, `channelUrl` |
| **snake_case** | 기존 대량 사용 중인 레거시만 유지 | `source_url`, `publish_date`, `recommended_by` |
| **소문자** | 단일 단어 프로퍼티 | `type`, `platform`, `status` |
| **공백** | Obsidian 기본값 | `date created`, `date modified` |

> **원칙**: 새 프로퍼티를 만들 때는 반드시 **camelCase**를 사용하세요. `rating` 대신 `myRate`, `channel_url` 대신 `channelUrl`입니다.

---

## Note-taking Guidelines
### Citation Style
#### 책 인용
> [!TIP] _Knowledge Management for the Future_
> 책의 내용 원본^[Koo, Y. (2021). _Knowledge Management for the Future._ New York: Oxford University Press. p.25.]
#### 논문 인용
> [!ABSTRACT] Knowledge Management in Organizations
> 조직 내 지식 관리의 중요성^[Kim, S., & Lee, H. (2023). The impact of knowledge management. _Journal of Knowledge Management_, 27(4), 1012-1035.]
#### 명언
> [!QUOTE]
> "2주 뒤에 뵙겠습니다."
> — 구요한(Yohan Koo)
## Sync Settings
### Obsidian Sync (공식 클라우드)
두 대의 Mac이 **Obsidian Sync**(공식 Obsidian 클라우드 서버)로 동기화됩니다.

| 환경 | 기기 | Base Path |
|------|------|-----------|
| Primary | MacBook Pro (16-inch) | `/Users/yohankoo/Local Obsidian_MBP/CMDSPACE_Local_MBP` |
| Secondary | Mac Studio | `/Users/yohankoo/Obsidian_Local/CMDSPACE_Studio_Local_Org` |

- 모든 하위 경로와 파일이 동일하게 유지됩니다
- AI 코드 출력은 환경별 하위 폴더(`03-1` ~ `03-8`)로 구분하여 출처를 추적합니다 (Claude Code · OpenClaw · Codex · Antigravity × MBP/Studio)

### Sync Config 경로
- `.obsidian` - macOS, Windows, Android
- `.obsidian_mobile` - iOS, iPadOS
## Version History
- **v2.5** (2026-05-03): 8-file precedence 정렬 (4→5), Antigravity 03-7/03-8 lane 추가, `94. System Prompts/` → `94. Agent Settings/claude/` 폴더 이름 갱신, `99. Format/` 중복 제거, Sync Settings lane 표기 갱신 (`03-1~03-8`)
- **v2.4** (2026-05-03): Codex MBP/Studio AI Agent 폴더 추가, description double-quote 예시 명확화
- **v2.3** (2026-04-07): 필수 프로퍼티 7개로 확장 (description 추가, English required for LLMs)
- **v2.2** (2026-03-30): Property 네이밍 규칙 섹션 추가, `channel` 노트 타입 도입
	- camelCase/snake_case/Obsidian 기본값 규칙 명시 및 교육용 예시 추가
	- `myRate` 표준 강화 (`rating` 사용 금지)
	- `channel` 타입 전용 Properties 스키마 정의
- **v2.1** (2025-10-23): 내용 오류 및 일관성 수정
- **v2.0** (2025-09-15): Properties 표준화 및 체계 개선
	- 날짜 형식 ISO 8601 통일
	- author 필드 wikilink 형식 통일
	- status 표준값 정의
	- myRate로 평점 통일
	- totalPage로 camelCase 통일
	- tags/aliases 배열 형식 통일
	- bookends 유지
- **v1.0** (2022-05-25): 초기 버전

## 추가 참고사항
### Portal 페이지
- [[Omni-Agency.portal]]
- [[Second Brain Experts.portal]]

### Graph View 활용
- [[Obsidian Graph View를 활용하는 법.obsidain]]
#### Filters 예시
- `-tag:Waypoint`
- `-path:"01. Daily Notes"`
- `-path:"study" -path:"reading"`
- `-file:"00. Inbox" -tag:waypoint`
- `["type":curriculum]`

### 플러그인 참고
#### Supercharged
- People
- Organization
- Curriculum

### Migration 태그
노트 출처 표시용:
- `notion`
- `applenote`
- `bear`
- `pages`
- `hwp`
- `docx`

### Citation Callout 추가 예시
#### 웹 아티클
> [!LINK] How to Take Smart Notes
> Zettelkasten 방법론에 대한 상세 가이드^[Ahrens, S. (2022, March 15). _The Complete Guide to the Zettelkasten Method._ Retrieved from https://zettelkasten.de/posts/overview/]
> - **핵심**: 영구 노트(Permanent Notes) 작성법
> - **팁**: 하나의 노트에는 하나의 아이디어만

#### INFO/EXAMPLE Callout
> [!INFO] _Deep Work_
> 몰입의 기술에 대한 칼 뉴포트의 통찰^[Newport, C. (2016). _Deep Work: Rules for Focused Success in a Distracted World._ Grand Central Publishing. pp.14-15.]

> [!EXAMPLE] _Atomic Habits_
> "You do not rise to the level of your goals. You fall to the level of your systems."^[Clear, J. (2018). _Atomic Habits._ Avery. p.27.]

---
*이 가이드는 CMDSPACE 볼트의 표준 Properties 체계를 정의합니다. 모든 새로운 노트는 이 규칙을 따라 작성되어야 합니다.*

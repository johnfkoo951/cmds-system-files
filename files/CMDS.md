---
type: documentation
aliases:
  - CMDS Context Guide
  - System Philosophy
description: "Context and philosophy guide for all LLM assistants working with the CMDS vault. Explains system purpose, user profile (Yohan Koo), 9 categories (100-900), and the Connect→Merge→Develop→Share process. Reference first when starting a new conversation about the CMDS vault."
author:
  - "[[구요한]]"
date created: 2025-10-22T21:52
date modified: 2026-05-22
tags:
  - CMDS
  - system
audience: All LLM assistants
scope: context-philosophy
precedence: 4
memory-type: user
required-for:
  - context-understanding
  - new-conversation
optional-for:
  - code-generation
  - file-editing
token-estimate: 8500
CMDS: "[[📚 601 Knowledge Management]]"
index: "[[🏛 CMDS Head Quarter]]"
version: "2.7"
status: completed
changelog:
  - "2.7 (2026-05-22): 8→9 system files 전환 — DESIGN.md (precedence 9, Visual Language tier) 추가. System Documentation Overview 에 🎨 Visual Language 테이블 추가, Essential 섹션 카운트 8→9 + 공개 5→6 갱신, body 본문 참조 3건 갱신. Tags 잔존 `3` 제거."
  - "2.6 (2026-05-20): Moderate diet — removed Working Environments & Sync (4중복: CLAUDE/AGENTS/ANTIGRAVITY/CMDS), Key Directories & Their Roles (.claude/rules/directory-structure.md 가 정본), Command Suite 상세 (CLAUDE.md 3중복), Quick Reference 카테고리 표 (본문과 자체 중복), When to Reference Each File·Quick Decision Tree (다른 파일 헤더와 중복). Vault Statistics 날짜 갱신. 9 카테고리·Workflow Patterns·Understanding User Intent 전문 유지. 결과: ~43.8k → ~28k chars."
  - "2.5 (2026-05-03): Aligned precedence to 8-file scheme (3→4 to make room for ANTIGRAVITY at 3). Added Antigravity 03-7/03-8 output lanes throughout. Removed stray numeric tag artifact (`3`)."
  - "2.4 (2026-05-03): Added Codex MBP/Studio output lanes and clarified Codex as a daily AI coding agent alongside Claude Code."
  - "2.3 (2026-04-20): 구요한 프로필 정정 — 박사 논문 집필 중단 상태 명시, 개인사업자(법인 신설 준비중), 주업=사업+교육으로 재프레이밍. 현재 4대 초점(옵시디언 PKM · System Files · LLM Wiki · 9Yohan) + LG 임원/회장단 교육 언급 추가."
  - "2.2 (2026-04-07): 필수 프로퍼티 7개 반영 (description 추가, English required)"
  - "2.1 (2026-04-01): precedence/memory-type/required-for/token-estimate 추가"
  - "2.0 (2026-03-15): 전면 리뷰, 통계 갱신, AI Tools 업데이트"
---
> 	**🔄 Last Updated: 2026-05-22** | Backup: `40. Docs/47. CMDS Docs/cmds-system-files/CMDS_backup.md` | Public: [system.cmdspace.work](https://system.cmdspace.work)

# CMDS.md

This file provides LLM assistants with essential context about the CMDS (커맨드스페이스) Personal Knowledge Management system created by 구요한(Yohan Koo). Use this document to understand the user's knowledge management philosophy, workflow, and context.

## Essential (Post-Compact)

> 컨텍스트 압축 후에도 반드시 기억해야 할 핵심 컨텍스트:
> 1. **CMDS**: Connect → Merge → Develop → Share (지식 생애주기)
> 2. **구요한**: 박사 수료(ABD 상태, 논문 집필은 현재 멈춤) · CMDSPACE 개인사업자(법인 설립 준비중) · 주업은 사업+교육. 연구하면서 가르치는 **실천가**.
> 3. **현재 4대 초점**: (a) 옵시디언 기반 PKM (b) System Files 체계 (c) LLM Wiki 위성 볼트 (d) 9Yohan 멀티 에이전트. 대표 교육 현장: **LG 임원 교육 · LG 회장단 교육**.
> 4. **9개 카테고리**: 100 Themes → 200 Literature → 300 Data → 400 Methods → 500 Products → 600 Specialties → 700 Creatives → 800 Outputs → 900 Divisions
> 5. **볼트 규모**: 10,000+ 노트, 120+ 플러그인
> 6. **기술 규칙**: CLAUDE.md (precedence 1) / AGENTS.md (precedence 2) / ANTIGRAVITY.md (precedence 3, Gemini 전용) 참조. 이외 6개 system file 까지 합쳐 **총 9개** (DESIGN.md = 시각 산출물 spec, precedence 9 / BRAIN.md, BRAIN_PROMPT.md 는 Gobi 페르소나 시스템 전용 — 일반 LLM coding agent 의 컨텍스트로 들어가지 않음).

<!-- STATIC: 아래 시스템 구조와 철학은 거의 변경되지 않습니다 -->

---

## System Documentation Overview

This vault has **9 system files** organized by audience. You are currently reading the **context guide** (precedence 4).

### The 9 System Files (by audience group)

#### 🤖 LLM Coding Agents (always-loaded technical context)

| File          | Audience                  | Purpose                               | Precedence |
| ------------- | ------------------------- | ------------------------------------- | :--------: |
| **CLAUDE.md** | Claude Code               | Claude Code 기술 규칙·command 매핑    | 1          |
| **AGENTS.md** | Codex / Cursor / Windsurf | 타 AI coding agent 일반 기술 규칙     | 2          |

#### 🧪 Vendor-Specific Agent

| File               | Audience                       | Purpose                                  | Precedence |
| ------------------ | ------------------------------ | ---------------------------------------- | :--------: |
| **ANTIGRAVITY.md** | Google Gemini / Antigravity IDE | Gemini 전용 행동 규칙·도구 매핑          | 3          |

#### 📚 Context & Standards (referenced by all agents)

| File                        | Audience           | Purpose                                              | Precedence |
| --------------------------- | ------------------ | ---------------------------------------------------- | :--------: |
| **CMDS.md** (this file)     | All LLM assistants | WHY & WHAT — 시스템 철학·사용자·9 카테고리           | 4          |
| **🏛 CMDS Guide.md**        | User + AI          | Standards — Properties v2, 템플릿, naming            | 5          |
| **🏛 CMDS Head Quarter.md** | User + AI          | Navigation — 91 카테고리 hub                         | 6          |

#### 🧠 Gobi Persona System (Gobi 앱 entry point — *외부 LLM coding agent 아님*)

| File                | Audience                | Purpose                                                          | Precedence |
| ------------------- | ----------------------- | ---------------------------------------------------------------- | :--------: |
| **BRAIN.md**        | Gobi agent + 사람       | 구요한 brain profile (사람을 기술하는 grounding source)          | 7          |
| **BRAIN_PROMPT.md** | Gobi agent              | Rules of Engagement (BRAIN.md 를 *어떻게* 사용할지의 메타 지침)  | 8          |

> **중요**: BRAIN.md / BRAIN_PROMPT.md 는 *Claude Code · Gemini CLI · Codex 등 일반 LLM coding agent 의 context window 로 들어가지 않음*. Gobi 앱이 외부 인터페이스(예: web)에서 구요한 페르소나로 답할 때만 사용. 다른 7개 파일과 *audience 가 본질적으로 다름*.

#### 🎨 Visual Language (always-loaded when producing visual artifacts)

| File          | Audience                                       | Purpose                                                            | Precedence |
| ------------- | ---------------------------------------------- | ------------------------------------------------------------------ | :--------: |
| **DESIGN.md** | All LLM agents producing visual artifacts      | Visual language spec — v4.3 standards · Anti-Slop · Skill↔Surface mapping | 9          |

> DESIGN.md 는 *시각 산출물을 만들 때* (웹·PDF·슬라이드·이미지·영상·다이어그램) 자동 로드된다. CLAUDE.md/AGENTS.md/ANTIGRAVITY.md 가 *기술* 규약을 다룬다면 DESIGN.md 는 *시각* 규약을 다룬다.

> **Quick routing**: 시스템 이해 → CMDS.md (you are here) · 코드 작성 → CLAUDE.md (Claude) / AGENTS.md (Codex 등) / ANTIGRAVITY.md (Gemini) · 카테고리 네비게이션 → [[🏛 CMDS Head Quarter]] · 표준·템플릿 → [[🏛 CMDS Guide]] · 시각 산출물 → [[DESIGN.md]] · Gobi 페르소나 → BRAIN.md / BRAIN_PROMPT.md. **Working environments / Deploy 절차는 [[CLAUDE.md]] 가 정본.**

---

## What is CMDS?

**CMDS (커맨드스페이스)** is a comprehensive Personal Knowledge Management (PKM) system built on Obsidian, designed to transform raw information into actionable knowledge and creative outputs. It's not just a filing system—it's a living ecosystem where ideas connect, merge, develop, and share.

### Core Philosophy

1. **Knowledge as a Network**: Every note is a node in an interconnected web of knowledge
2. **Process-Driven**: Knowledge flows through distinct stages (Connect → Merge → Develop → Share)
3. **AI-Enhanced**: Integrated with multiple AI tools (ChatGPT, Claude, Midjourney, etc.)
4. **Output-Focused**: Knowledge exists to be transformed into tangible outputs (research, lectures, consulting, creative works)
5. **Personal yet Structured**: Flexible enough for creativity, structured enough for productivity

---

## The User: 구요한 (Yohan Koo)

### Professional Identity (as of 2026-04)

구요한은 **연구자가 아니라 "연구하면서 가르치는 실천가"** 로 자신을 정의합니다. 그의 시간과 에너지는 박사 논문이 아니라 사업과 교육에 쓰입니다.

- **Business Operator**: Sole proprietor of **CMDSPACE (커맨드스페이스)**, currently transitioning to a corporation. Builds products, education, and consulting services around personal knowledge management × generative AI.
- **Educator (primary role)**: Delivers corporate executive education — notably **LG 임원 교육 · LG 회장단 교육** — along with university lectures and public workshops. Teaches what he is actively researching in his own vault.
- **PhD ABD (paused)**: Completed coursework for the PhD in Educational Technology / Knowledge Management (ABD status). **Dissertation writing is currently paused.** Academic identity remains in the background; active identity is business + education.
- **Knowledge Management Practitioner-Researcher**: Researches PKM · Second Brain · Zettelkasten through a 10,000+ note Obsidian vault that functions as both lab and teaching material.
- **Generative AI Practitioner**: Works daily with Claude (Claude Code, Claude Agent SDK), ChatGPT custom GPTs, Obsidian × LLM integration, and multi-agent orchestration.
- **Creative Professional**: Newsletter (더배러), YouTube, music, digital art — all produced from the same vault.

### Four Current Focus Areas (as of 2026-04)

구요한 is currently concentrating research and teaching on four tightly interconnected axes. These are **not separate projects but one integrated experiment** on *"how the individual knowledge worker redesigns knowledge labor in the LLM era."*

1. **Obsidian-Based Personal Knowledge Management** — a 3+ year / 10,000+ note vault as the substrate of everything else.
2. **System Files Infrastructure** — total 9 system files in vault: 6 publicly deployed (CLAUDE.md, AGENTS.md, CMDS.md, 🏛 CMDS Guide, 🏛 CMDS Head Quarter, DESIGN.md) + 3 internal-only (ANTIGRAVITY.md for Gemini, BRAIN.md / BRAIN_PROMPT.md for Gobi persona). Shared `.claude/rules/` accompanies the 6 public files at `system.cmdspace.work`.
3. **LLM Wiki Satellite Vault** — implementing Karpathy's LLM Wiki pattern (Raw Sources · Wiki · Queries) in a separate `CMDS_LLM_Wiki` vault.
4. **9Yohan Multi-Agent System** — mapping 900 Divisions × historical "Yohan" figures × the 9 fruits of the Spirit into a 9-agent orchestration (kepler.map / goethe.sense / dewey.learn / bach.score / neumann.compute / baptist.prepare / mccarthy.reason / huizinga.play / calvin.advise).

These four axes are simultaneously **productized** (consulting, education), **published** (더배러 newsletter, public web), and **validated on the toughest stage**: top-level corporate education including LG executive and chairman-group training.

### Multi-Vault Ecosystem (확장 컨텍스트)

The mothership operates within a **7-vault ecosystem**, each governed by different authoring authority and purpose. All other 6 vaults branch from this mothership and reference its system files.

| Type | Vault | 멤버 | 역할 |
|------|-------|------|------|
| 🌍 Mothership | `CMDSPACE_Local_MBP` | 구요한 | 모든 vault 의 substrate |
| 🛰 Compiled Satellite | `CMDS_LLM_Wiki` | 구요한 + LLM | 학습·연구·정리 (focus axis #3) |
| 🤖 Personal Product | `CMDS_Gobi` | 구요한 | 고비 스페이스/데스크탑 사용 |
| 🤝 Pair | `CMDS_JoonLab` | 구요한 + 박준 | 교육·강의·컨설팅·코칭 |
| 🤝 Pair | `CMDSPACE_Admin` | 구요한 + 이태극 | 운영 총괄 |
| 👥 Team (5인) | `GOBI` | 구요한·이태극·김진영·강민석·Greg Moon | 커맨드스페이스 × 고비 팀 |
| 📤 Distribution | `cmds-vault` | 구요한 → 외부 | CMDS 스타터킷 (외부 사용자) |

→ Canonical reference (운영·결정·governance): `CMDS_LLM_Wiki/20. Wiki/23. Guides/Multi-Vault Architecture` ([obsidian:// link](obsidian://open?vault=CMDS_LLM_Wiki&file=20.%20Wiki%2F23.%20Guides%2FMulti-Vault%20Architecture)).

**기술 규칙**은 [[CLAUDE.md]] § Companion Vaults 참조.

### Work Context
구요한 operates **9 professional divisions** (📖 900 Divisions):
1. **Knowledge Management & Research** (901)
2. **Writing & Publishing** (902) — _renamed 2026-04-19 from "Editorial & Content Creation"_
3. **Teaching & Curriculum** (903) — _renamed 2026-04-19 from "Education & Training"_
4. **Creative Arts & Media** (904)
5. **Research Methods & Analytics** (905) — _renamed 2026-04-19 from "Data Science & Analytics"_
6. **Partnerships & Networks** (906) — _renamed 2026-04-19 from "Partnerships & Outreach"_
7. **Product & Engineering** (907) — _renamed 2026-04-19 from "Technology & Development"_
8. **Events & Community Engagement** (908)
9. **Consulting & Advisory** (909) — _renamed 2026-04-19 from "Consulting & Professional Services"_

> **903 ↔ 909 경계 규칙** (2026-04-19 확정)
> - **903 Teaching & Curriculum**: 공개 플랫폼(패캠/인프런) · 대학 수업 · 오픈 수강생 대상 공개 강의
> - **909 Consulting & Advisory**: 기업/공공기관 맞춤 교육 · 경영진 1on1 코칭 · 조직 진단
> - 고객이 "기관"이면 909, "개인·불특정 수강생"이면 903

### Primary Activities
- **Teaching & Consulting** (primary time allocation): Designing and delivering AI × PKM programs — **LG 임원 교육 · LG 회장단 교육**, other corporate training, university courses, public workshops.
- **Vault Engineering**: Continuously refining the Obsidian vault, System Files infrastructure, LLM Wiki satellite, and 9Yohan agent system — researching *by building*.
- **Content Production**: Running the **더배러 (The Better)** newsletter, YouTube appearances, article/book writing — all produced from and refined through the vault.
- **Business Operations**: Growing CMDSPACE from sole proprietor toward a formal corporation, partnering with collaborators, shipping consulting deliverables.
- **Knowledge Base Maintenance**: Building and maintaining the 10,000+ note vault as both working system and teaching artifact.
- **PhD (paused)**: Coursework complete (ABD); dissertation writing is currently on hold — the active work above takes precedence.

---

## CMDS Architecture: 9 Categories (100-900 Series)

The CMDS system organizes all knowledge into 9 major categories, each representing a distinct stage or aspect of the knowledge lifecycle.

### 📖 100 Themes — Discovery & Connection
**Purpose**: Capture emerging interests, topics, variables, and terminologies
**Contains**:
- 📚 101 Interests — Personal and professional interests
- 📚 102 Topics — Subjects being explored
- 📚 103 Variables — Research variables, concepts to operationalize
- 📚 104 Terminologies — Definitions and vocabulary

**Role in Workflow**: This is where curiosity lives. New ideas, unfamiliar terms, and potential research topics are captured here before they mature into full concepts.

### 📖 200 Literature — Integration & Theory
**Purpose**: Integrate knowledge from external sources into personal understanding
**Contains**:
- 📚 201 Concepts — Core conceptual frameworks
- 📚 202 Frameworks — Theoretical frameworks and models
- 📚 203 Models — Analytical and conceptual models
- 📚 204 Theories — Established theories
- 📚 205 Classics — Foundational texts and seminal works
- 📚 210 Literature Reviews — Academic literature synthesis
- 📚 220 Personal Insights — Original interpretations and connections
- 📚 240 Books — Book notes and reviews
- 📚 290 Bible — Biblical texts and theology
- 📚 291 Sermon — Sermon notes and spiritual reflections

**Role in Workflow**: Raw ideas from 100 Themes are enriched with literature, transformed into robust theoretical foundations. This is where learning happens.

### 📖 300 Data — Collection & Management
**Purpose**: Manage research data, surveys, and information systems
**Contains**:
- 📚 301 Scale Development and Validation
- 📚 302 Questionnaires — Survey instruments
- 📚 303 Panel Data — Longitudinal data
- 📚 310 Data Management — Data organization and workflows
- 📚 311 Database Systems — Database design and implementation
- 📚 330 Learning Management Systems — LMS platforms and usage

**Role in Workflow**: Theoretical knowledge from 200 Literature is operationalized into measurable data. This is where theory meets empirical reality.

### 📖 400 Methodologies — Analysis & Implementation
**Purpose**: Apply research methods, statistical techniques, and analytical approaches
**Contains**:
- 📚 401 Research Methods — Research design principles
- 📚 402 Quantitative Research
- 📚 403 Experimental Research
- 📚 404 Qualitative Research
- 📚 405 Mixed Methods
- 📚 410 Statistical Inference
- 📚 411 Regression Analysis
- 📚 412 Causal Inference
- 📚 420 Machine Learning
- 📚 421 Time Series Analysis
- 📚 422 Deep Learning
- 📚 423 Predictive Analytics
- 📚 490 Syntax — Statistical software syntax
- 📚 491 Codes — Programming code snippets
- 📚 492 Prompts — AI prompts and templates
- 📚 493 Scripts — Automation scripts

**Role in Workflow**: Data from 300 is analyzed using appropriate methods. This is where insights are generated through systematic analysis.

### 📖 500 Products — Tools & Platforms
**Purpose**: Master and leverage productivity tools and AI platforms
**Contains**:
- 📚 501 Obsidian — PKM system mastery
- 📚 502 Notion — Project management
- 📚 510 DevonThink — Document management
- 📚 520 ChatGPT — AI assistance and automation
- 📚 521 Claude — AI writing and analysis
- 📚 522 Gemini — Google AI tools
- 📚 523 LLaMa — Open-source LLMs
- 📚 530 Midjourney — AI image generation
- 📚 531 Stable Diffusion — Image AI
- 📚 541 n8n — Workflow automation

**Role in Workflow**: Tools are not just used—they are studied, mastered, and integrated into workflows. This category captures tool knowledge and best practices.

### 📖 600 Specialties — Expertise & Application
**Purpose**: Develop deep expertise in specialized domains
**Contains**:
- 📚 601 Knowledge Management — PKM theory and practice
- 📚 603 Second Brain — Building a Second Brain methodology
- 📚 604 ZettelKasten — Zettelkasten method
- 📚 610 Productivity — Personal productivity systems
- 📚 620 Generative AI — AI applications and education
- 📚 630 Development — Software development
- 📚 651 Physical Health — Exercise and wellness
- 📚 652 Mental Health — Psychology and well-being
- 📚 653 Biohacking — Performance optimization
- 📚 680 Educations — Educational theory and practice
- 📚 690 Spirituality — Faith and spiritual growth

**Role in Workflow**: This is where 구요한 develops and maintains professional expertise. It's a combination of theory (200), methods (400), and practical experience.

### 📖 700 Creatives — Expression & Content
**Purpose**: Create and distribute creative content across multiple platforms
**Contains**:
- 📚 701 YouTube — Video content creation
- 📚 710 SNS — Social media content
- 📚 720 Music — Music composition and production
- 📚 721 Jazz — Jazz theory and performance
- 📚 730 Images — Visual content
- 📚 731 Digital Art and Design — AI-generated art, design work

**Role in Workflow**: Knowledge and expertise are transformed into creative expressions. This is where ideas become content.

### 📖 800 Outputs — Publication & Delivery
**Purpose**: Produce and deliver formal outputs (academic, professional, educational)
**Contains**:
- 📚 801 PhD — Doctoral dissertation and research
- 📚 802 Articles — Published articles and essays
- 📚 803 Books — Book manuscripts
- 📚 804 Community — Community building and engagement
- 📚 805 Group Study — Study groups and cohorts
- 📚 806 Webpages — Web content and sites
- 📚 820 Research — Research projects
- 📚 821 Academic Journals — Journal publications
- 📚 822 Conference Presentations — Academic presentations
- 📚 830 Projects — Client projects
- 📚 831 Consulting — Consulting deliverables
- 📚 840 Lectures — Teaching materials
- 📚 841 Curriculum — Course design
- 📚 842 Course Development and Resources — Educational resources
- 📚 843 Class Administration and Management — Teaching operations

**Role in Workflow**: This is the ultimate destination—where all prior work (Connect, Merge, Develop) culminates in tangible outputs that serve others.

### 📖 900 Divisions — Operations & Management
**Purpose**: Organize and manage the operational structure of 구요한's professional activities
**Contains** (2026-04-19 개명 반영, 구 이름은 alias로 유지):
- 📚 901 Knowledge Management & Research Division
- 📚 902 Writing & Publishing Division _(구: Editorial & Content Creation)_
- 📚 903 Teaching & Curriculum Division _(구: Education & Training)_
- 📚 904 Creative Arts & Media Division
- 📚 905 Research Methods & Analytics Division _(구: Data Science & Analytics)_
- 📚 906 Partnerships & Networks Division _(구: Partnerships & Outreach)_
- 📚 907 Product & Engineering Division _(구: Technology & Development)_
- 📚 908 Events & Community Engagement Division
- 📚 909 Consulting & Advisory Division _(구: Consulting & Professional Services)_

**9Yohan Constellation (2026-04-19 확정)**: 각 Division은 역사적 "요한"과 성령의 열매에 매핑됨. 정본은 `00. Inbox/03. AI Agent/03-1. Claude Code (MBP)/2026-04-19-9yohan-orchestration/canonical.md`.

| Division | Head | Fruit | Handle |
|----------|------|------|--------|
| 901 | 케플러 요한 | 온유 | `kepler.map` |
| 902 | 괴테 요한 | 사랑 | `goethe.sense` |
| 903 | 듀이 요한 | 자비 | `dewey.learn` |
| 904 | 바흐 요한 | 희락 | `bach.score` |
| 905 | 노이만 요한 | 절제 | `neumann.compute` |
| 906 | 세례요한 | 오래 참음 | `baptist.prepare` |
| 907 | 매카시 요한 | 양선 | `mccarthy.reason` |
| 908 | 하위징아 요한 | 화평 | `huizinga.play` |
| 909 | 칼뱅 요한 | 충성 | `calvin.advise` |

**Role in Workflow**: Meta-organizational layer that manages how all other categories are operationalized in 구요한's professional life.

**903 ↔ 909 경계 규칙**:
- **903 Teaching & Curriculum**: 공개 플랫폼 · 대학 · 오픈 수강생 대상 · 고객이 "개인/불특정"
- **909 Consulting & Advisory**: 기업/공공기관 맞춤 · 경영진 1on1 · 조직 진단 · 고객이 "기관"

---

## CMDS Process: The Knowledge Lifecycle

The CMDS framework is not just a filing system—it's a **process** that guides knowledge through four distinct stages.

### 🔗 Connect — Idea Discovery (100 Themes)
**What happens**: Encounter new ideas, capture interests, identify gaps
**Questions to ask**:
- What am I curious about?
- What terminology do I need to learn?
- What topics are emerging in my field?
- What variables matter for my research?

**Outputs**: Notes in 100 Themes (interests, topics, variables, terminologies)

### 🔀 Merge — Knowledge Integration (200 Literature)
**What happens**: Read literature, connect ideas, build theoretical frameworks
**Questions to ask**:
- How does this concept relate to what I already know?
- What do scholars say about this topic?
- What frameworks exist to explain this phenomenon?
- What are my own insights and interpretations?

**Outputs**: Literature notes, concept maps, theoretical frameworks, personal insights

### 🛠 Develop — Application & Creation (300-600)
**What happens**: Collect data, apply methods, use tools, build expertise
**Questions to ask**:
- What data do I need?
- Which methods are appropriate?
- What tools will help me execute?
- How do I deepen my expertise in this area?

**Outputs**: Datasets, analysis scripts, tool mastery notes, domain expertise

### 📤 Share — Output & Impact (700-800)
**What happens**: Create content, publish research, teach, consult, serve others
**Questions to ask**:
- How can I share this knowledge?
- Who needs this information?
- What format will be most impactful?
- How can I help others learn and grow?

**Outputs**: YouTube videos, articles, research papers, lectures, consulting projects, creative works

---

## Note Hierarchy & Navigation

### Hierarchical Structure
```
🏛 Home/Guide (최상위)
└── 📖 1st Level CMDS (100-900 시리즈)
    └── 📚 2nd Level CMDS (N01-N99)
        └── (No Icon) 3rd Level Notes (세부 주제)
```

### Key Hub Notes
- **[[🏛 CMDS Head Quarter]]** — Central navigation hub, links to all 9 categories
- **[[🏛 CMDS Guide]]** — Properties standards, naming conventions, operational guidelines
- **[[🏛 000 YHN Home]]** — Personal home page

### Index Notes (🏷)
Index notes aggregate related content across categories:
- [[🏷 Daily Notes]] — Daily journal entries
- [[🏷 Meeting Notes]] — Meeting minutes
- [[🏷 Research Notes]] — Research documentation
- [[🏷 Lecture Notes]] — Teaching materials
- [[🏷 People]] — People profiles
- [[🏷 Prompts]] — AI prompt library
- [[🏷 Syntax and Codes]] — Code snippets

---

## Note Properties & Metadata

모든 노트는 구조화된 메타데이터 (frontmatter) 를 갖는다. **자세한 스키마·검증 규칙은 [[🏛 CMDS Guide]] 와 `.claude/rules/frontmatter-standard.md` 가 정본.**

- **7 required properties**: `type`, `aliases`, `description` (English, 1-2 sentence skill-style hint for LLMs), `author`, `date created`, `date modified`, `tags`
- **Common types**: `note` · `terminology` · `meeting` · `people` · `curriculum` · `manuscript` · `research-pipeline` · `channel` · `CMDS` (category index) · `moc` · `api` · `documentation`
- **Status (5 values)**: `unread` · `reading` · `inProgress` · `completed` · `archived`
- **Date format**: ISO 8601 (`YYYY-MM-DD` 또는 `YYYY-MM-DDTHH:mm`)

---

## Workflow Patterns & Common Scenarios

### Research Workflow
1. **Discover** a research question → Capture in [[📚 102 Topics]]
2. **Define** key variables → Document in [[📚 103 Variables]]
3. **Review** literature → Create notes in [[📚 210 Literature Reviews]]
4. **Design** study → Plan in [[📚 401 Research Methods]]
5. **Collect** data → Manage in [[📚 310 Data Management]]
6. **Analyze** → Apply methods from [[📚 410 Statistical Inference]]
7. **Write** → Draft in [[📚 821 Academic Journals]]
8. **Present** → Prepare in [[📚 822 Conference Presentations]]

### Teaching Workflow
1. **Design** curriculum → Create in [[📚 841 Curriculum]]
2. **Develop** resources → Build in [[📚 842 Course Development and Resources]]
3. **Prepare** lectures → Store in [[📚 840 Lectures]]
4. **Teach** → Document in [[🏷 Daily Notes]]
5. **Reflect** → Write insights in [[📚 220 Personal Insights]]

### Consulting Workflow
1. **Meet** with client → Record in [[🏷 Meeting Notes]]
2. **Research** client's needs → Reference [[📚 601 Knowledge Management]] or [[📚 620 Generative AI]]
3. **Design** solution → Draft in [[📚 831 Consulting]]
4. **Deliver** → Present and document in [[📚 830 Projects]]
5. **Follow up** → Track in [[60. Collections/63. Meetings/]]

### Content Creation Workflow
1. **Identify** topic from [[📚 102 Topics]] or [[📚 220 Personal Insights]]
2. **Research** using [[📖 200 Literature]] notes
3. **Script** content using [[📚 492 Prompts]] and AI tools
4. **Create** in appropriate platform (YouTube, article, etc.)
5. **Publish** and document in [[📚 701 YouTube]] or [[📚 802 Articles]]

### Development Workflow
1. **Plan** feature or tool → Design in [[📚 630 Development]]
2. **Build** with Claude Code or Codex → Output to the appropriate lane under `00. Inbox/03. AI Agent/`
3. **Test** and iterate → Reference [[📚 491 Codes]] or [[📚 493 Scripts]]
4. **Deploy** → Document in [[📚 806 Webpages]] or [[📚 830 Projects]]
5. **Maintain** → Track in skills, plugins, or automation workflows

---

## AI Integration in CMDS

### AI Tools Used Daily
- **Claude Code**: Code generation, skill/plugin development, vault automation, writing assistance
- **Codex**: Code generation, repo/vault edits, cross-agent review, and portable execution of AGENTS.md workflows
- **ChatGPT** (Custom GPTs): Knowledge work, reasoning, analysis
- **Gemini CLI**: Cross-validation, web search integration
- **Midjourney**: AI image generation, visual content
- **HeyGen**: AI avatar video creation
- **ElevenLabs**: Text-to-speech, audio generation
- **n8n**: Workflow automation
- **Obsidian AI Plugins**: Copilot, Smart Connections

### Custom AI Assistants
구요한 maintains custom GPT assistants in ChatGPT (named after model versions, not the models themselves):
- **CMDS GPT-5 Pro** — Primary assistant for knowledge work
- **CMDS o3-pro** — Advanced reasoning and analysis
- **CMDS GPT-5 Thinking** — Deep thinking and problem-solving
- **CMDS o3** — Alternative reasoning model

### AI-Generated Content
- **Prompts Library**: [[📚 492 Prompts]] — Reusable prompt templates
- **Code Snippets**: [[📚 491 Codes]] — AI-generated and human-curated code
- **Agent Settings**: `90. Settings/94. Agent Settings/claude/` — Claude Code 원본 (Obsidian Sync 대상). 각 Mac 의 `.claude/{agents,commands,rules,skills}` 는 이 원본으로 향하는 symlink 로 연결되어 동기화됨. Codex-native skills live in `.agents/skills/`.

---

## Key Directories

**전체 디렉토리 구조와 카테고리 매핑은 `.claude/rules/directory-structure.md` 가 정본.** 9개 최상위 폴더 (`00. Inbox` ~ `90. Settings`) 와 CMDS 100-900 카테고리는 1:1 매핑이 아니라 *역할 분리* 다:

- `00. Inbox/` — 미분류·임시. AI 에이전트 코드 출력은 `03. AI Agent/03-1~03-8` (agent × machine 매트릭스) 의 정해진 lane 으로.
- `10. CMDS Process/` — Connect/Merge/Develop/Share 자체에 대한 문서
- `20. Literature Notes/` · `30. Permanent Notes/` — 외부 지식 → 영구 노트
- `40. Docs/` — 실무·기술 문서 (`47. CMDS Docs/` 에 system file backup/share 사본)
- `50. Assets/` — 재사용 리소스 (브랜드·프롬프트·워크플로)
- `60. Collections/` — People·Organization·Meetings·Bases
- `70. Outputs/` — 최종 산출물 (강의·컨설팅·프로젝트)
- `80. References/` — 외부 참조 (Zotero·Omnivore·도서)
- `90. Settings/` — 템플릿·인덱스·에이전트 설정 (`94. Agent Settings/claude/` 가 `.claude/{agents,commands,rules,skills}` symlink 의 원본)

---

## Common Terminology & Concepts

### PKM Terms
- **Second Brain**: External system for storing and organizing knowledge (Tiago Forte's methodology)
- **Zettelkasten**: Note-taking method focused on atomic notes and connections
- **Evergreen Notes**: Timeless, fully developed notes that don't decay
- **CMDS Index**: Category index pages that organize related notes (replaces traditional MOC concept in this vault)
- **Atomic Notes**: Small, focused notes on single concepts
- **Progressive Summarization**: Highlighting and condensing information in stages

### CMDS-Specific Terms
- **CMDS Process**: Connect → Merge → Develop → Share workflow
- **Space Collection**: First-level CMDS categories (100-900)
- **Spaces**: Second-level CMDS categories (N01-N99)
- **Hub Notes**: 🏛 notes that serve as navigation centers
- **Index Notes**: 🏷 notes that aggregate related content

### File Prefix Meanings
- 📎 — Web Clips (captured from web)
- 🏷 — Index pages (collections)
- 📦 — Reviews (analyzed content)
- 🔖 — Personal outputs (구요한's original ideas)
- 📜 — Others' outputs (curated external content)
- 📈 — Code and syntax (technical content)
- 🎹 — Music (compositions, theory)
- 📘 — Books and references

---

## Understanding User Intent

When 구요한 asks you to work with the vault, understand the context:

### Research Context
If discussing research topics:
- Frame as **applied research on PKM × LLM × agents** (not dissertation work — see `Professional Identity` · dissertation writing is currently paused).
- Default to one of the **4 current focus axes**: Obsidian PKM / System Files / LLM Wiki / 9Yohan. If the topic doesn't fit, say so explicitly.
- Reference relevant literature ([[📖 200 Literature]]) and methodological approaches ([[📖 400 Methodologies]]) as usual.
- Outputs usually become **newsletter editions, consulting decks, or teaching material** first; academic publications are secondary.

### Teaching Context
If discussing courses or lectures:
- Reference curriculum designs ([[📚 841 Curriculum]])
- Link to relevant subject expertise ([[📖 600 Specialties]])
- Consider student learning outcomes
- Think about course materials ([[📚 842 Course Development and Resources]])

### Consulting Context
If discussing client work:
- Document in meetings ([[60. Collections/63. Meetings/]])
- Connect to relevant expertise ([[📚 831 Consulting]])
- Reference applicable frameworks ([[📖 200 Literature]])
- Consider deliverables ([[📚 830 Projects]])

### Content Creation Context
If creating content:
- Identify target platform ([[📚 701 YouTube]], [[📚 802 Articles]], etc.)
- Reference source knowledge ([[📖 200 Literature]], [[📖 600 Specialties]])
- Use prompt templates ([[📚 492 Prompts]])
- Consider audience and purpose

### Knowledge Management Context
If discussing PKM system itself:
- Reference [[🏛 CMDS Guide]] for standards
- Consider [[📚 601 Knowledge Management]] best practices
- Think about Obsidian workflows ([[📚 501 Obsidian]])
- Apply Second Brain principles ([[📚 603 Second Brain]])

---

## Working with the CMDS System

### When Creating New Notes
1. Determine the **CMDS category** (100-900 series) based on content type
2. Use appropriate **note type** (note, meeting, curriculum, etc.)
3. Add required **properties** (type, aliases, author, date created, tags)
4. Link to relevant **index notes** (🏷)
5. Reference related **CMDS categories**
6. Create **backlinks** to related notes

### When Organizing Information
- **Connect Stage** → Capture in [[📖 100 Themes]]
- **Merge Stage** → Integrate into [[📖 200 Literature]]
- **Develop Stage** → Apply in [[📖 300 Data]] through [[📖 600 Specialties]]
- **Share Stage** → Output via [[📖 700 Creatives]] or [[📖 800 Outputs]]

### CMDS Process as Operational Verbs

The CMDS Process is also encoded as **8 slash commands** (`/connect`, `/merge`, `/develop`, `/share` + `/inbox`, `/lint`, `/query`, `/status`). This makes "이걸 connect할까, merge할까?" the first metacognitive step of every session. **Command implementation details (parameters, dialog flows, output paths) are in [[CLAUDE.md]] § "CMDS Process Command Suite".** Source files live in `90. Settings/94. Agent Settings/claude/commands/`.

### When Searching for Context
Look for relevant notes in:
1. **Index pages** (🏷) — Aggregated collections
2. **Hub pages** (🏛) — Main navigation
3. **CMDS categories** (📖, 📚) — Topical organization
4. **Daily/Weekly notes** — Temporal context
5. **Meeting notes** — Project context
6. **People notes** — Relationship context

---

<!-- DYNAMIC: 아래 통계와 도구 목록은 주기적으로 갱신됩니다 -->

## Vault Statistics (as of 2026-05-20)

- **Total Notes**: 10,000+
- **CMDS Categories**: 9 main (100-900) + 91 sub-categories
- **Templates**: 94 note templates
- **Obsidian Plugins**: 120+
- **Note Types**: 459+ `note`, 160+ `meeting`, 130+ `terminology`, 124+ `research-pipeline`, 97+ `api`, 93+ `people`, 85+ `moc`, 82+ `curriculum`, 66+ `manuscript`
- **Years Active**: 3+ years of continuous knowledge accumulation

This is a **mature, established system** with well-defined patterns. Respect existing conventions and structures.

---

## Guiding Principles

1. **Every note has a home**: All knowledge belongs somewhere in the 100-900 system
2. **Links create value**: Isolated notes are less useful than connected notes
3. **Process matters**: Knowledge flows through Connect → Merge → Develop → Share
4. **Output is the goal**: Knowledge exists to serve others through outputs
5. **AI is a partner**: AI tools enhance but don't replace human thinking
6. **Standards enable freedom**: Consistent structure allows creative flexibility
7. **Evolution over perfection**: The system grows and adapts continuously

---

**Remember**: CMDS is not just a filing system—it's a **thinking environment** where 구요한 develops ideas, conducts research, creates content, and serves others. When working with this vault, you're not just organizing files; you're supporting a knowledge worker's entire professional ecosystem.

**For technical implementation details, file operations, and coding guidelines, see [[CLAUDE.md]].**

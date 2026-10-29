---
type: documentation
aliases:
  - CMDSPACE Design System
  - DESIGN.md
  - Visual Language Spec
description: "Visual language specification for all CMDSPACE artifacts. Defines v4.3 design constants (SF Pro × CMDS Green/Pink), anti-AI-slop negative list, template catalog, and a Skill ↔ Surface mapping covering 80+ skills (web, PDF, slides, image, video, diagram), plus the diagram system where one Mermaid source is rendered by Pele through the cmds-pele module with CMDS tokens. Reference whenever any LLM agent (Claude Code, Codex, Antigravity, Gobi) produces a visual artifact for the CMDSPACE brand."
author:
  - "[[구요한]]"
date created: 2026-05-22T18:47
date modified: 2026-10-23
tags:
  - CMDS
  - system
  - design
  - design-system
  - visual-language
audience: All LLM coding agents producing visual artifacts
scope: visual-language
precedence: 9
memory-type: feedback
required-for:
  - web-generation
  - pdf-generation
  - slide-generation
  - image-generation
  - video-generation
  - diagram-generation
optional-for:
  - text-only-output
  - data-analysis
token-estimate: 5200
CMDS: "[[📚 731 Digital Art and Design]]"
index: "[[🏛 CMDS Head Quarter]]"
version: "1.4"
status: completed
changelog:
  - "1.4 (2026-10-23): 볼트와 발행본이 같은 도식 색 규칙을 쓰게 했다. Obsidian 1.15가 Mermaid 대신 Pele(1.8.0)를 내장해 볼트 미리보기가 33/33이 되었으므로 §4.6의 25/33 서술과 §7.6의 8종 점검을 고치고, §1.6에 볼트 연결(`cmds-pele-vault` 플러그인이 같은 토큰을 Obsidian `--mermaid-*`에 넣고 강조 지시문을 적용)을 더했다. §4.6에 볼트 노트 행과 볼트·발행본 버전 차이(볼트 1.8.0, 발행본 1.9.0)를 적었다. 발행본 Pele 1.8.0 → 1.9.0."
  - "1.3.1 (2026-10-22): §4.6 도식 행의 Pele 버전 표기를 모듈 `vendor/pele/CURRENT` 참조로 바꿨다(Pele 1.6.0 → 1.8.0 업그레이드, 다음 업그레이드부터 이 파일을 고치지 않아도 된다)."
  - "1.3 (2026-10-21): 다이어그램 시스템 반영 (macro v4.14.0). §1.6 도식 토큰(cmds-pele `--cp-*`, 시리즈 8색, 배경 대비 4.5:1 규칙, Pretendard 측정 글꼴)을 v4.3 확장으로 추가하고, §2.1 금지 목록에 도식 색 하드코딩과 확산 모델 도식을 넣었다. §4.6을 cmds-diagram 진입점과 지면별 스킬(브리프, 덱, 보고서 PDF·HWPX, 블로그, 뉴스레터, 웹)로 다시 쓰고 Obsidian 미리보기 25/33 사실을 적었다. §5.5 도식 일관성, §7.6 도식 사전 점검, §8 출처를 더했다."
  - "1.2 (2026-07-02): 전수 감사 픽스 세트 (macro v4.9.3) — (a) §4.3 미실존 스킬 2종 (presentation-english-coach·presentation-generator-ko) 을 실존 스킬 (tone-writer·cmds-lecture-builder) 로 교체, (b) §4.4 이미지 1차 스킬을 cmds-visual-gen 으로 교체 (image-generation-skill 은 legacy 표기), (c) Lineage 의 cross-vault wikilink 2건 → obsidian URL, (d) §9 '4-way fan-out' → 현행 '8-way (5 mothership + 3 satellite)' 정정 + CMDS.md 📌 블록 주석 보완, (e) 각주·§8.3 의 깨진 링크 구문 (백틱 포함 markdown link) → plain 백틱 경로, (f) Guide/HQ @import 표기 wikilink 로 정정."
  - "1.1 (2026-05-30): Went public as 6th deployed file (v4.8.0); header de-staled; §9 follow-ups resolved; counts hedged."
  - "1.0 (2026-05-22): Initial version. 9th system file added to mothership. Sources — getdesign.md pattern (2026-04-23 capture), v4.3 design standards (cmdspace-web-builder skill), Anti-AI-Slop guidelines (Claude Design system prompt captured 2026-05-04), 87-skill catalog mapped to visual surfaces. Triggered by /query — CMDSPACE 버전의 design.md 만들어줘 (2026-05-22)."
---
> **🔄 Last Updated: 2026-10-23** | Backup: `40. Docs/47. CMDS Docs/cmds-system-files/DESIGN_backup.md` | Public: [system.cmdspace.work](https://system.cmdspace.work) (6th public file, deployed v4.8.0 2026-05-27)

# DESIGN.md

This file is the **visual language spec** for all CMDSPACE artifacts. It complements [[CLAUDE.md]] / [[AGENTS.md]] / [[ANTIGRAVITY.md]] (which govern *technical* conventions) by governing *visual* conventions: brand constants, anti-AI-slop rules, template catalog, and how the vault's 80+ skills map to visual surfaces (web · PDF · slides · image · video · diagram).

> **📌 Related System Files (9 System Files)** — `precedence` 순서대로 로드, audience 별 그룹
>
> **🤖 LLM Coding Agents** (always-loaded technical context):
> - @CLAUDE.md → [[CLAUDE.md]] — Claude Code specific (precedence: 1)
> - @AGENTS.md → [[AGENTS.md]] — Codex / Cursor / Windsurf 등 (precedence: 2)
>
> **🧪 Vendor-Specific Agent**:
> - @ANTIGRAVITY.md → [[ANTIGRAVITY.md]] — Google Gemini / Antigravity IDE (precedence: 3)
>
> **📚 Context & Standards** (referenced by all agents):
> - @CMDS.md → [[CMDS.md]] — System philosophy & user context (precedence: 4)
> - [[🏛 CMDS Guide]] — Standards & templates (precedence: 5 · 공백 포함 경로라 @import 불가 — 필요 시 명시 Read)
> - [[🏛 CMDS Head Quarter]] — Navigation hub (precedence: 6 · 공백 포함 경로라 @import 불가 — 필요 시 명시 Read)
>
> **🧠 Gobi Persona System** (Gobi 앱 entry point):
> - @BRAIN.md → [[BRAIN.md]] — 구요한 brain profile (precedence: 7)
> - @BRAIN_PROMPT.md → [[BRAIN_PROMPT.md]] — Agent Rules of Engagement (precedence: 8)
>
> **🎨 Visual Language** (always-loaded when producing visual artifacts):
> - @DESIGN.md → [[DESIGN.md]] — This file — visual spec (precedence: 9)

---

## Origin & Lineage

이 문서는 **getdesign.md** ([https://getdesign.md/](https://getdesign.md/)) 가 정립한 *"AI 코딩 에이전트용 DESIGN.md 패턴"* 의 CMDSPACE 버전이다. getdesign.md 는 Vercel·Stripe·Figma·Notion 등 69개 기성 브랜드의 디자인 시스템을 마크다운으로 큐레이션해 AI 에이전트에 공급한다. CMDSPACE 는 *외부 브랜드를 모방하는 대신 자체 시각 언어를 시스템 파일로 격상* 한다.

**Lineage**:

- `getdesign.md` 패턴 ([[AI 코딩 에이전트용 DESIGN.md 패턴]], 2026-04-23 capture)
- `v4.3 design standards` (cmdspace-web-builder skill, 2026-Q1~)
- `Anti-AI-Slop` negative-list (→ LLM Wiki: [Anti-AI-Slop Design Guidelines](obsidian://open?vault=CMDS_LLM_Wiki&file=20.%20Wiki%2F21.%20Concepts%2FAnti-AI-Slop%20Design%20Guidelines), 2026-05-04)
- `张汉东 의 DESIGN.md → spec → plan` 공학적 파이프라인 (→ LLM Wiki: [张汉东](obsidian://open?vault=CMDS_LLM_Wiki&file=20.%20Wiki%2F22.%20Entities%2F%E5%BC%A0%E6%B1%89%E4%B8%9C), 조명용)

---

## 0. Audience & Scope

| 항목 | 내용 |
|------|------|
| **Audience** | CMDSPACE 의 시각 산출물을 만드는 모든 LLM 에이전트 — Claude Code, Codex, Antigravity, Gobi |
| **Triggers (자동 로드)** | 사용자가 "사이트 만들어줘", "PDF 만들어줘", "슬라이드 짜줘", "이미지 그려줘", "영상 만들어줘", "다이어그램 그려줘" 류 요청 시 |
| **Scope IN** | 웹·PDF·슬라이드·이미지·영상·다이어그램·Canvas·SNS 시각 톤·뉴스레터 |
| **Scope OUT** | 코드 로직, 데이터 분석, 텍스트 전용 답변 (이때는 CLAUDE.md 등 기술 system file 만으로 충분) |

---

## 1. CI Constants (절대 불변 — v4.3)

> 다음 5개 항목은 **모든 시각 산출물에서 동일** 해야 한다. 변경 시 v4.4 로 버전업.
> **버전 namespace 주의**: DESIGN 의 v4.3 은 시각 언어 표준 generation 이며 Vercel 배포 macro-version(v4.9.x)과 무관.

### 1.1 컬러 토큰

| 토큰 | 값 | 용도 |
|------|-----|------|
| `--cmds-green` | `#134538` | Primary brand (light 모드 accent, 헤더, CTA bg) |
| `--cmds-green-bright` | `--cmds-green` 의 lighter shade | gradient endpoint |
| `--cmds-pink` | `#E985A2` | Dark 모드 accent, dark 모드 CTA bg |
| `--accent-on` | light=`#FFFFFF` / dark=`#1B1B1B` | accent 배경 위 텍스트 (테마별 자동 전환) |

> **다크 모드 룰**: light 는 *Green + White text*, dark 는 *Pink + Dark text*. `prefers-color-scheme` 자동 감지 + localStorage 토글 영속.

### 1.2 타이포그래피

```css
--font-sans:    "SF Pro Display", "SF Pro Text", "Pretendard", system-ui, sans-serif;
--font-display: "SF Pro Display", "Pretendard", sans-serif;
--font-mono:    "SF Mono", "JetBrains Mono", ui-monospace, monospace;
```

- 한글은 **Pretendard**, 영문은 **SF Pro**. *둘 다 폴백 체인에 명시.*
- 본문 16px · 큰 제목 최대 104px (랜딩 hero)
- *Inter / Roboto / Arial / Fraunces 사용 금지* (anti-slop §2)

### 1.3 로고 & 파비콘

- `cmds-logo-round.png` — 라이트·다크 공통 (round mark, 원형 마스크)
- typo lockup 은 `cmds-typo-black.png` / `cmds-typo-white.png` (테마별 swap)
- 파비콘 = round logo PNG (인라인 SVG `§` placeholder 절대 금지)

### 1.4 OG 메타 (17종, 절대 URL 만)

페이지마다 1200×630 PNG OG 이미지 + 17개 메타 태그 필수. *상대 경로 절대 금지.*

### 1.5 CTA 컬러 룰

- Light 모드: `bg: var(--cmds-green); color: #FFFFFF;`
- Dark 모드: `bg: var(--cmds-pink); color: #1B1B1B;` (어두운 글자)

### 1.6 도식 토큰 (Pele · cmds-pele, 2026-10-21)

> v4.3에 도식 토큰을 더한 확장이다. 시리즈 팔레트를 확정하면(Pele 도입 기획서 10절 결정 1) v4.4로 올린다. 값의 정본은 `/Users/yohankoo/DEV/cmds-pele/src/tokens.json`이고 `dist/cmds-pele.css`가 여기서 생성된다.

| 토큰 | Light | Dark | 용도 |
|------|-------|------|------|
| `--cp-accent` | `#134538` | `#E985A2` | 핵심 노드(`%% @key`), 해석 노드와 그 선 |
| `--cp-bg` · `--cp-fg` | `#ffffff` · `#16201c` | `#141917` · `#e8ebe9` | 도식 바탕과 글자 |
| `--cp-series-1`~`8` | `#134538` `#a8436a` `#5a6660` `#2f7a62` `#7e2c4d` `#38433e` `#8c5a70` `#75604f` | `#E985A2` `#7cc4a8` `#b9c2bd` `#f3b9cc` `#a9dcc8` `#c48aa0` `#8f9a95` `#e7d3c5` | pie, xychart, timeline, gitGraph 같은 계열 색 |
| `--cp-font` | Pretendard → SF Pro | 같음 | 라벨 폭을 재는 글꼴과 그리는 글꼴을 같게 |

- **대비 규칙**: Pele는 timeline 헤더, gitGraph 브랜치 이름 같은 글자를 바탕색으로 칠한다. 그래서 시리즈 색은 바탕과 4.5:1 이상이어야 한다. 현재 최저값은 라이트 5.15:1, 다크 6.12:1이다(2026-10-20 실측).
- **라이트는 초록, 다크는 분홍**(§1.1)이 도식에도 그대로 간다. 브랜드 분홍 `#E985A2`는 흰 바탕 대비가 2.52:1이라 라이트 시리즈에 쓰지 않는다.
- **호스트 연결**: 페이지는 자기 토큰을 `--cp-*` 변수로 넘긴다. 다크는 `data-cp-theme="dark"` 또는 조상 `.cp-dark`, 자동은 `data-cp-theme="auto"`.
- **볼트 연결** (2026-10-23): Obsidian 1.15+ 볼트는 Obsidian에 든 Pele가 그린다. `cmds-pele-vault` 플러그인이 같은 토큰을 Obsidian의 `--mermaid-accent`, `--mermaid-critical`, `--mermaid-color-1`~`8`에 넣고 강조 채움을 더하며, `%% @key/@interp/@aux`를 발행본과 같은 방식으로 적용한다. 바탕, 글자, 선은 볼트 테마를 따른다. 플러그인의 CSS는 `tokens.json`에서 생성되므로 색을 바꾸면 두 곳이 함께 바뀐다.
- **글꼴**: 도식은 한글 라벨 폭을 정확히 재려고 Pretendard를 먼저 둔다. 웹과 아티팩트에 싣는 Pretendard 부분집합은 `pele-fontpack.py`로 만든다. 직접 만든 부분집합은 Chrome 글꼴 검사(OTS)에 걸려 대체 글꼴로 보일 수 있다.

---

## 2. Anti-AI-Slop Negative List

> Claude Design system prompt (2026-05-04 captured) + cmdspace-web-builder ANTI-PATTERNS 통합. **LLM 이 default 로 빠지는 패턴을 명시 차단.**

### 2.1 시각 (Visual)

- ❌ Aggressive gradient backgrounds (색상 무한 변환은 "느낌 있어 보이는" LLM 디폴트)
- ❌ Emoji 남발 — *brand navigation 이모지(🏛/📖/📚/🏷)는 vault 내부 wikilink prefix 전용*, 일반 가이드·랜딩에 붙이지 말 것
- ❌ 좌측 border accent + 둥근 컨테이너의 "callout" 디폴트
- ❌ SVG 로 사람·사물·아이콘 imagery 직접 그리기 → placeholder 두고 실제 자료 요청
- ❌ 인라인 `style="color:#..."` (테마 전환 불가)
- ❌ `<picture media="prefers-color-scheme">` (수동 토글과 충돌)
- ❌ 히어로 상단 로고 + 아이브로우 "CMDS" 텍스트 동시 노출 (중복)
- ❌ 도식 소스에 색 하드코딩 (`style`, `classDef ... fill:`, `linkStyle`, `themeVariables`). 테마 전환이 안 되고 다크에서 안 읽힌다. 강조는 `%% @key` · `%% @interp` · `%% @aux` 지시문으로만 한다
- ❌ 흐름·구조·비율 도식을 확산 모델 이미지로 생성 (라벨과 숫자가 뭉갠다). Mermaid 코드 도식(§4.6)이나 HTML 인포그래픽(§4.4)으로 만든다

### 2.2 타이포

- ❌ Inter / Roboto / Arial / Fraunces / "system fonts" 일반화 — *SF Pro + Pretendard 만*

### 2.3 콘텐츠

- ❌ Filler content / placeholder section / dummy stats — *"every element should earn its place"*
- ❌ Data slop (의미 없는 숫자·아이콘·통계)
- ❌ Unilateral 섹션 추가 — 추가가 좋아 보이면 *먼저 사용자에게 물어볼 것*

### 2.4 Positive prescription (대안)

- ✅ `text-wrap: pretty` · CSS grid · 고급 CSS 효과
- ✅ *"1 thousand no's for every yes"*
- ✅ 빈 섹션은 layout/composition 으로 해결 (콘텐츠 발명 X)
- ✅ Negative-list 가 차단한 *분포의 다른 영역* 에서 답 찾기

---

## 3. Template Catalog

### 3.1 기본 3종 (cmdspace-web-builder)

| 템플릿 | 레퍼런스 | 특징 | 적용처 |
|--------|----------|------|--------|
| **Quick Deploy** | [llm-wiki.cmdspace.work](https://llm-wiki.cmdspace.work) | 단일 HTML (~650 lines), 다크 토글 내장, `--accent-on` 패턴 | 개인 아카이브 · 스터디 가이드 · 빠른 런칭 |
| **Landing** | [system.cmdspace.work](https://system.cmdspace.work) | Sticky header · 거대 타이포 hero · 풀 마케팅 랜딩 | 제품 · 컨퍼런스 · 공식 프로젝트 |
| **Editorial Docs** | [system.cmdspace.work/docs/](https://system.cmdspace.work/docs/) | 3컬럼 (사이드바 · 본문 · TOC), ⌘K 팔레트, marked.js 인라인 렌더 | API 문서 · 가이드 · 시스템 문서 |

### 3.2 Landing 확장 컴포넌트 5종

기본 landing 이 마케팅 중심일 때, 시스템·아키텍처 설명에는 다음 5종 추가:

1. **Star Topology Diagram** — 중앙 허브 + N개 노드 원형 배치 (멀티 에이전트·mind map)
2. **Numbered Control Loop** — 10단계 이상 프로세스를 5×2 그리드로
3. **Division Grid** — 풍부한 정보 카드 (좌측 accent border)
4. **Callout Box** — tint 배경 · label/title/body 3단
5. **Layer Grid** — 파일 구조 / 레이어 카드 (4열 · pill 라벨)

실전 적용 예: [9yohan.cmdspace.work](https://9yohan.cmdspace.work) (5종 모두 사용).

---

## 4. Skill ↔ Surface Mapping ★

> **이 표는 본 문서의 가장 큰 부가가치.** LLM 이 *"CMDSPACE 시각 산출물 X 를 만들려면 어떤 스킬을 부를지"* 한 표로 결정.

### 4.1 웹

| Surface | 1차 스킬 | 보조 스킬 | 참고 |
|---------|----------|---------|------|
| 랜딩·서브도메인 | `cmdspace-web-builder` | `vercel-deployer`, `domain-routing` | v4.3 표준 |
| 매거진·포트폴리오 | `obsidian-magazine-site` | `cmdspace-web-builder` | 멀티모달 |
| 기술 문서 | `obsidian-docusaurus-builder` | `cmdspace-web-builder` (Editorial Docs) | Vercel 배포 포함 |
| 미니멀 단일 페이지 | `minimal-homepage` | — | 빌드툴 없음 |
| 배포 후 유지 | `cmdspace-update` | `web-deployments-sync` | apex 갱신 |

### 4.2 PDF

| Surface | 1차 스킬 | 보조 스킬 | 참고 |
|---------|----------|---------|------|
| 브로셔·일반 문서 | `md-to-pdf` | — | report 테마 H2 수동 번호 제거 룰 [^pdf] |
| 이력서 (도장 포함) | `resume-update` | `md-to-pdf` | 효력 문서 only 도장 |
| NotebookLM 워터마크 제거 | `notebooklm-logo-remover` | — | post-processing |

### 4.3 슬라이드

| Surface | 1차 스킬 | 보조 스킬 | 참고 |
|---------|----------|---------|------|
| Markdown 슬라이드 | `markdown-slides` | `tone-writer` | 빠른 deck |
| PowerPoint | `pptx-cmds` | `cmds-visual-gen` | 한국 기업 호환 |
| Keynote (macOS native) | `keynote` | `cmds-visual-gen` | Magic Move 지원 |
| 발표 톤·내용 | `tone-writer` | `cmds-lecture-builder` | 톤별 콘텐츠·강의 기획 |

### 4.4 이미지

| Surface | 1차 스킬 | 보조 스킬 | 참고 |
|---------|----------|---------|------|
| 브랜드 일러스트·인포그래픽 (강의 덱·웹·위키·시스템 파일) | `cmds-visual-gen` | — | 하이브리드 라우팅: 📊 인포그래픽·텍스트·숫자 = HTML/CSS→PNG · 🎨 컨셉 일러스트 = GPT/Gemini 확산 · 📸 실제 화면 = 캡처 (생성 금지). legacy `image-generation-skill` 대체 (2026-06-25) |

### 4.5 영상

| Surface | 1차 스킬 | 보조 스킬 | 참고 |
|---------|----------|---------|------|
| Remotion (React 비디오) | `markdown-video` | `remotion-best-practices` | DEV 폴더 사용 [^video] |
| HeyGen 아바타 | `heygen` | `audio-generator` | 1-shot prompt-to-video |
| YouTube 한글 자막 | `youtube-kr-subtitle` | `video-cleaning` | Claude 직접 번역 |

### 4.6 다이어그램·Canvas

| Surface | 1차 스킬 | 보조 스킬 | 참고 |
|---------|----------|---------|------|
| Mermaid 도식 (모든 지면의 진입점) | `cmds-diagram` | `obsidian-mermaid` | 정본 모듈 `/Users/yohankoo/DEV/cmds-pele` (Pele 버전은 모듈의 `vendor/pele/CURRENT`, 2026-10-23 기준 1.9.0). 타입 고르기, 작성 규칙, 지면별 넣는 법. mermaid-rules.md 준수 |
| 브리프 (A4) | `cmds-brief` | `cmds-diagram` | 빌드 HTML에서 브라우저로 그림 (print 프로필) |
| 슬라이드 덱 | `cmds-lecture-builder` (deck-core) | `cmds-diagram` | spec의 `pele` 슬라이드를 slide 프로필로 미리 그림 |
| 보고서 PDF · HWPX | `md-to-pdf` · `md-to-hwpx` | `research-harness` | 인라인 SVG · 본문 폭에 맞춘 고해상도 PNG 그림 |
| 지산 블로그 · 뉴스레터 | `jisan-blog` · `thebetter-writer` | `jisan-scribe` | 커밋하는 사전 렌더 캐시 · 뉴스레터는 PNG만 |
| 웹 페이지 | `cmdspace-web-builder` | `cmds-diagram` | dist 사본을 사이트에 두고 `--cp-*`로 토큰 연결 |
| 볼트 노트 | `obsidian-mermaid` | `cmds-diagram` | Obsidian 1.15+ 내장 Pele가 그리고 `cmds-pele-vault` 플러그인이 CMDS 색과 강조 지시문을 적용 |
| Knowledge graph | `graphify` | — | |
| Obsidian Canvas | `obsidian-canvas`, `cmds-canvas` | `json-canvas` | |

- 볼트 미리보기는 Obsidian 1.15+에 든 Pele(1.15.0은 1.8.0)가, 발행본은 cmds-pele의 Pele가 그린다. Mermaid 12.1의 33종이 모두 볼트에서 보인다(2026-10-23 실측, MBP·Studio). Obsidian 1.14.4의 Mermaid 11.13.0에서는 25종이라 swimlane, agentflow, eventmodeling, usecase, railroad, treeView, cynefin, wardley는 발행본에서만 보였다.
- 볼트의 Pele가 발행본보다 늦을 수 있다(2026-10-23 기준 볼트 1.8.0, 발행본 1.9.0). 그 사이에 생긴 기능은 볼트판 기준으로 쓴다: sankey 노드 이름은 ASCII, `List<T>` 같은 꺾쇠 글자는 `#lt;T#gt;`, 라벨의 `<code>`·`<kbd>`·`<sub>` 모양은 발행본에서만 난다(mermaid-rules.md 10번, 정본 목록은 `catalog.json`의 `peleVaultGap`).
- 두 볼트의 기존 Mermaid 893블록 중 879블록이 Pele로 그려진다(2026-10-23 재측정, 1.8.0과 1.9.0 결과 같음). 거부된 14블록은 Mermaid 11.17.2도 거부한 작성 오류다.
- 33종 갤러리: https://pele.cmdspace.work

### 4.7 텍스트 시각 톤 (시각 산출물 아니지만 brand voice)

| Surface | 1차 스킬 |
|---------|----------|
| SNS 4종 카피 | `cmds-sns-promo` |
| 톤별 콘텐츠 | `tone-writer` |
| 더배러 뉴스레터 | `thebetter-writer` |

### 4.8 사전 점검

| Surface | 스킬 |
|---------|------|
| UI 가이드라인 준수 점검 | `web-design-guidelines` |

---

## 5. Cross-Surface Consistency Rules

다른 surface 간 일관성 룰. *같은 콘텐츠를 웹 → PDF → 슬라이드 → 영상 으로 옮길 때 동일 brand 인상이 유지되도록.*

### 5.1 마스터 → 파생 흐름

- **마스터**: 항상 *Markdown* (단일 진실 원천). 볼트 내 노트가 master.
- **파생**: 위 4 섹션의 스킬로 web/PDF/slide/video 로 변환.
- *반대 방향 금지*: PPT 를 master 로 두고 거꾸로 MD 추출하면 brand drift.

### 5.2 색상 일관성

모든 surface 에서 `--cmds-green` / `--cmds-pink` / `--accent-on` 토큰 동일 적용. 슬라이드 마스터 슬라이드·PDF 헤더·영상 lower-third 모두 동일.

### 5.3 로고 사용

- 웹: 헤더 좌측 round logo (32~40px)
- PDF: 표지/푸터 round logo + typo lockup (테마별 swap)
- 슬라이드: 마스터 슬라이드 우하단 round logo
- 영상: 인트로 1초 + 아웃트로 마지막 프레임

### 5.4 OG 메타 일관성

웹 → SNS 공유 → 카카오톡 미리보기 까지 1200×630 OG 이미지 동일 사용.

### 5.5 도식 일관성 (2026-10-21)

- 원고의 ```` ```mermaid ```` 펜스 하나가 정본이다. 지면마다 다시 그리지 않고 렌더 방식만 바꾼다. 스크립트를 실을 수 있는 지면은 브라우저에서 그리고, 못 싣는 지면(PDF, HWPX, 블로그, 뉴스레터, 덱)은 미리 그린다.
- 캡션은 닫는 펜스 바로 다음 줄의 이탤릭 한 줄이다. `%% @caption`은 그 줄이 없을 때만 쓴다. 브리프는 마스터의 `- 캡션:` 줄을 쓴다. 그림 번호는 자동으로 붙이지 않는다.
- 근거 지위를 선으로 구분한다. 원문이 말한 관계는 실선, CMDSPACE의 해석은 점선과 `%% @interp`.

---

## 6. Anti-Patterns (Vault-Specific)

CMDSPACE 운영에서 반복 발생한 실수 — *DESIGN.md v1.0 시점의 기억* 정리.

- ❌ **이모지 prefix 오용** — 🏛/📖/📚/🏷 는 vault navigation hub 전용. 일반 가이드·프로젝트 문서에 붙이면 wikilink 자동 placeholder 생성 사고 (2026-05-03 windlight 가이드 위반 사례) [^emoji]
- ❌ **PDF report 테마 H2 수동 번호** — TOC 자동 번호와 중복. report 테마에서 본문 H2 의 수동 번호 제거 (2026-05-11 SGI 교육 사고) [^pdf]
- ❌ **정보 전달 문서에 도장** — 도장은 *효력 문서* (견적·계약·제안서) 에만. 커리큘럼·안내문·회의록은 텍스트 서명만 [^pdf]
- ❌ **차의과대 수업 문서 PDF 자동 변환** — master MD 만 만들고 끝. PDF 는 명시 요청 시에만
- ❌ **SNS 카피에 마크다운 기호 노출** — LinkedIn/Threads/X/카톡은 마크다운 렌더 X. `**볼드**`, `*이탤릭*`, 백틱이 그대로 노출됨. 카피 블록 내부는 plain text + 이모지·하이픈·공백으로 강조
- ❌ **영상 프로젝트 node_modules 를 vault 안에** — `/Users/yohankoo/DEV/video-projects/` 사용, vault 에는 tracking MD 만 [^video]

[^pdf]: Claude 메모리 노트 `pdf-protocol.md` 참조 (`~/.claude/projects/{vault-project}/memory/`)
[^emoji]: Claude 메모리 노트 `feedback_emoji_prefix_reserved.md` 참조 (`~/.claude/projects/{vault-project}/memory/`)
[^video]: `.claude/rules/video-project-workflow.md` 참조

---

## 7. Pre-Flight Checklist (Before Publishing Any Visual Artifact)

모든 시각 산출물 publish 전 다음 점검:

### 7.1 모든 surface 공통

- [ ] CI 컬러 토큰 사용 (`#134538` · `#E985A2`) — 임의 컬러 X
- [ ] 폰트 = SF Pro + Pretendard 만 — Inter/Roboto 검출 시 즉시 교체
- [ ] 로고 = `cmds-logo-round.png` (round PNG) — 인라인 SVG placeholder X
- [ ] Anti-AI-Slop §2 negative-list 검증
- [ ] 이모지 prefix (🏛/📖/📚/🏷) 가 잘못 사용되지 않았는지

### 7.2 웹 추가

- [ ] OG 이미지 1200×630 PNG + 17 메타 + 절대 URL
- [ ] Light/Dark 토글 + localStorage 영속
- [ ] CTA 컬러 룰 (light=green+white / dark=pink+dark text)

### 7.3 PDF 추가

- [ ] report 테마 본문 H2 수동 번호 제거 (TOC 자동 번호와 중복 방지)
- [ ] 도장 필요성 재검증 — 효력 문서면 ✅, 정보 전달 문서면 ❌
- [ ] Preview 시각 점검 (자동 열기)

### 7.4 슬라이드 추가

- [ ] 마스터 슬라이드에 round logo 우하단
- [ ] 16:9 또는 4:3 명시
- [ ] 한국어 = Pretendard, 영문 = SF Pro 분리

### 7.5 영상 추가

- [ ] 인트로 1초 round logo · 아웃트로 마지막 프레임 brand lockup
- [ ] 자막 폰트 = Pretendard (한국어) / SF Pro (영문)
- [ ] 프로젝트 코드 = `/Users/yohankoo/DEV/video-projects/{name}/`, vault 는 tracking MD 만

### 7.6 도식 추가

- [ ] `node /Users/yohankoo/DEV/cmds-pele/bin/pele-check.mjs --surface {brief|deck|report|blog|vault} FILE.md` 오류 0
- [ ] 소스에 색 하드코딩 없음 (§2.1), 강조는 지시문
- [ ] 노드 한도: 브리프 9 · 덱 7 · 블로그 12 · 보고서 15
- [ ] 라이트·다크 둘 다 확인. 블로그는 폰 폭(390px)도 본다
- [ ] 볼트 노트에도 두는 도식이면 `--surface vault`도 오류 0 (볼트 버전 Pele로도 그려 본다). 볼트에서 강조가 안 보이면 `cmds-pele-vault` 플러그인이 켜져 있는지 본다

---

## 8. Sources & References

### 8.1 Vault 내부

- [[AI 코딩 에이전트용 DESIGN.md 패턴]] — getdesign.md 패턴 capture
- [[CLAUDE.md]] · [[AGENTS.md]] · [[ANTIGRAVITY.md]] — 기존 audience-specific system files
- [[CMDS.md]] · [[🏛 CMDS Guide]] · [[🏛 CMDS Head Quarter]] — context & standards
- `90. Settings/91. Templates/` — 기존 template 모음
- `30. Permanent Notes/39. Guideline/Design, Colors and Graphics.md` — *legacy (2022) (archived/deprecated)*, 본 DESIGN.md 가 대체
- [[2026-10-18-Pele-themeable-SVG-전-시스템-도입-기획서]] · [[2026-10-20-Pele-1.6.0-33종-렌더-실측과-볼트-Mermaid-호환성]] · [[CMDS 다이어그램 원장]] — 도식 시스템의 기획, 실측, 현재 상태

### 8.2 LLM Wiki (satellite)

- [Anti-AI-Slop Design Guidelines](obsidian://open?vault=CMDS_LLM_Wiki&file=20.%20Wiki%2F21.%20Concepts%2FAnti-AI-Slop%20Design%20Guidelines) — negative-list 패턴
- [Claude Design](obsidian://open?vault=CMDS_LLM_Wiki&file=20.%20Wiki%2F22.%20Entities%2FClaude%20Design) — Anthropic 의 대화형 디자인 도구
- [Antigravity (Google DeepMind)](obsidian://open?vault=CMDS_LLM_Wiki&file=20.%20Wiki%2F22.%20Entities%2FAntigravity%20%28Google%20DeepMind%29) — 6번째 audience system file 케이스
- [张汉东](obsidian://open?vault=CMDS_LLM_Wiki&file=20.%20Wiki%2F22.%20Entities%2F%E5%BC%A0%E6%B1%89%E4%B8%9C) — DESIGN.md → spec → plan 공학적 파이프라인

### 8.3 External

- [getdesign.md](https://getdesign.md/) — 69개 브랜드 디자인 시스템 큐레이션 (원형 패턴)
- cmdspace-web-builder skill: `~/.claude/skills/cmdspace-web-builder/SKILL.md` — v4.3 표준
- cmds-pele 모듈: `/Users/yohankoo/DEV/cmds-pele/README.md` — 도식 토큰·부트스트랩·도구 정본 · Pele: https://github.com/obsidianmd/pele (MIT) · https://pele.run
- 실전 레퍼런스: [system.cmdspace.work](https://system.cmdspace.work) · [llm-wiki.cmdspace.work](https://llm-wiki.cmdspace.work) · [9yohan.cmdspace.work](https://9yohan.cmdspace.work)

---

## 9. Post-Restructure Status (v4.8.0 / v4.9.0)

v4.8.0 (2026-05-27)으로 mothership 이 *8 → 9 system files* 가 되었고, 아래 정합성 작업이 완료됨:

- [x] **CLAUDE.md / AGENTS.md / ANTIGRAVITY.md / CMDS.md** 의 "📌 Related System Files" 표를 8개 → 9개로 갱신 (DESIGN.md = precedence 9 추가 · CMDS.md 는 이후 v2.6 다이어트에서 📌 블록 대신 System Documentation Overview 표로 대체)
- [x] **🏛 CMDS Head Quarter** 의 System Files 섹션에 DESIGN.md 항목 추가
- [x] **system-docs-updater 스킬** 의 동기화 대상 목록에 DESIGN.md 추가 (현행 8-way fan-out — 5 mothership + 3 satellite)
- [x] **system.cmdspace.work 배포** — DESIGN.md 를 공개 가능한 *6번째 파일* 로 배포 결정·반영 (CLAUDE/AGENTS/CMDS/Guide/HQ 와 함께 포함)
- [x] **legacy 흡수** — `30. Permanent Notes/39. Guideline/Design, Colors and Graphics.md` (2022) 에 deprecation 배너 추가, archive 처리. 본 DESIGN.md 가 정본
- [x] **`💻 Working Environments` 의 Public Deployment 섹션** (CLAUDE.md/AGENTS.md/CMDS.md) — 공개 파일 개수 표기 6개로 갱신

> **상태**: 위 정합성 작업은 v4.8.0 (2026-05-27) ~ v4.9.0 (2026-05-30) 사이에 *한 세션 / 한 commit* 으로 묶여 완료됨. system-docs-updater 스킬이 8-way (5 mothership + 3 satellite) fan-out 을 자동화.

---

**For technical conventions**: see [[CLAUDE.md]] / [[AGENTS.md]] / [[ANTIGRAVITY.md]].
**For system philosophy**: see [[CMDS.md]].
**For navigation**: see [[🏛 CMDS Head Quarter]].

---
type: documentation
aliases:
  - CMDSPACE Design System
  - DESIGN.md
  - Visual Language Spec
description: "Visual language specification for all CMDSPACE artifacts. Defines v4.3 design constants (SF Pro × CMDS Green/Pink), anti-AI-slop negative list, template catalog, and a Skill ↔ Surface mapping covering 87 skills (web, PDF, slides, image, video, diagram). Reference whenever any LLM agent (Claude Code, Codex, Antigravity, Gobi) produces a visual artifact for the CMDSPACE brand."
author:
  - "[[구요한]]"
date created: 2026-05-22T18:47
date modified: 2026-05-22T20:30
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
optional-for:
  - text-only-output
  - data-analysis
token-estimate: 4200
CMDS: "[[📚 731 Digital Art and Design]]"
index: "[[🏛 CMDS Head Quarter]]"
version: "1.0"
status: completed
changelog:
  - "1.0 (2026-05-22): Initial version. 9th system file added to mothership. Sources — getdesign.md pattern (2026-04-23 capture), v4.3 design standards (cmdspace-web-builder skill), Anti-AI-Slop guidelines (Claude Design system prompt captured 2026-05-04), 87-skill catalog mapped to visual surfaces. Triggered by /query — CMDSPACE 버전의 design.md 만들어줘 (2026-05-22)."
---
> **🔄 Last Updated: 2026-05-22** | Backup: `40. Docs/47. CMDS Docs/cmds-system-files/DESIGN_backup.md` (pending) | *Not yet deployed to system.cmdspace.work — pending 8→9 file restructure*

# DESIGN.md

This file is the **visual language spec** for all CMDSPACE artifacts. It complements [[CLAUDE.md]] / [[AGENTS.md]] / [[ANTIGRAVITY.md]] (which govern *technical* conventions) by governing *visual* conventions: brand constants, anti-AI-slop rules, template catalog, and how the vault's 87 skills map to visual surfaces (web · PDF · slides · image · video · diagram).

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
> - @🏛 CMDS Guide → [[🏛 CMDS Guide]] — Standards & templates (precedence: 5)
> - @🏛 CMDS Head Quarter → [[🏛 CMDS Head Quarter]] — Navigation hub (precedence: 6)
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
- `Anti-AI-Slop` negative-list (→ LLM Wiki: [[Anti-AI-Slop Design Guidelines]], 2026-05-04)
- `张汉东 의 DESIGN.md → spec → plan` 공학적 파이프라인 (→ LLM Wiki: [[张汉东]], 조명용)

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
| PowerPoint | `pptx-cmds` | `image-generation-skill` | 한국 기업 호환 |
| Keynote (macOS native) | `keynote` | `image-generation-skill` | Magic Move 지원 |
| 발표 톤·내용 | `presentation-english-coach`, `presentation-generator-ko` | — | 영어/한국어 톤 |

### 4.4 이미지

| Surface | 1차 스킬 | 보조 스킬 | 참고 |
|---------|----------|---------|------|
| 슬라이드용 일러스트 | `image-generation-skill` | — | 사용자 스타일 정의 |

### 4.5 영상

| Surface | 1차 스킬 | 보조 스킬 | 참고 |
|---------|----------|---------|------|
| Remotion (React 비디오) | `markdown-video` | `remotion-best-practices` | DEV 폴더 사용 [^video] |
| HeyGen 아바타 | `heygen` | `audio-generator` | 1-shot prompt-to-video |
| YouTube 한글 자막 | `youtube-kr-subtitle` | `video-cleaning` | Claude 직접 번역 |

### 4.6 다이어그램·Canvas

| Surface | 1차 스킬 | 보조 스킬 |
|---------|----------|---------|
| Mermaid 다이어그램 | `obsidian-mermaid` | (mermaid-rules.md 준수) |
| Knowledge graph | `graphify` | — |
| Obsidian Canvas | `obsidian-canvas`, `cmds-canvas` | `json-canvas` |

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

---

## 6. Anti-Patterns (Vault-Specific)

CMDSPACE 운영에서 반복 발생한 실수 — *DESIGN.md v1.0 시점의 기억* 정리.

- ❌ **이모지 prefix 오용** — 🏛/📖/📚/🏷 는 vault navigation hub 전용. 일반 가이드·프로젝트 문서에 붙이면 wikilink 자동 placeholder 생성 사고 (2026-05-03 windlight 가이드 위반 사례) [^emoji]
- ❌ **PDF report 테마 H2 수동 번호** — TOC 자동 번호와 중복. report 테마에서 본문 H2 의 수동 번호 제거 (2026-05-11 SGI 교육 사고) [^pdf]
- ❌ **정보 전달 문서에 도장** — 도장은 *효력 문서* (견적·계약·제안서) 에만. 커리큘럼·안내문·회의록은 텍스트 서명만 [^pdf]
- ❌ **차의과대 수업 문서 PDF 자동 변환** — master MD 만 만들고 끝. PDF 는 명시 요청 시에만
- ❌ **SNS 카피에 마크다운 기호 노출** — LinkedIn/Threads/X/카톡은 마크다운 렌더 X. `**볼드**`, `*이탤릭*`, 백틱이 그대로 노출됨. 카피 블록 내부는 plain text + 이모지·하이픈·공백으로 강조
- ❌ **영상 프로젝트 node_modules 를 vault 안에** — `/Users/yohankoo/DEV/video-projects/` 사용, vault 에는 tracking MD 만 [^video]

[^pdf]: 메모리 [pdf-protocol](`~/.claude/projects/.../memory/pdf-protocol.md`) 참조
[^emoji]: 메모리 [feedback_emoji_prefix_reserved](`~/.claude/projects/.../memory/feedback_emoji_prefix_reserved.md`) 참조
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

---

## 8. Sources & References

### 8.1 Vault 내부

- [[AI 코딩 에이전트용 DESIGN.md 패턴]] — getdesign.md 패턴 capture
- [[CLAUDE.md]] · [[AGENTS.md]] · [[ANTIGRAVITY.md]] — 기존 audience-specific system files
- [[CMDS.md]] · [[🏛 CMDS Guide]] · [[🏛 CMDS Head Quarter]] — context & standards
- `90. Settings/91. Templates/` — 기존 template 모음
- `30. Permanent Notes/39. Guideline/Design, Colors and Graphics.md` — *legacy (2022)*, 본 DESIGN.md 가 대체

### 8.2 LLM Wiki (satellite)

- [Anti-AI-Slop Design Guidelines](obsidian://open?vault=CMDS_LLM_Wiki&file=20.%20Wiki%2F21.%20Concepts%2FAnti-AI-Slop%20Design%20Guidelines) — negative-list 패턴
- [Claude Design](obsidian://open?vault=CMDS_LLM_Wiki&file=20.%20Wiki%2F22.%20Entities%2FClaude%20Design) — Anthropic 의 대화형 디자인 도구
- [Antigravity (Google DeepMind)](obsidian://open?vault=CMDS_LLM_Wiki&file=20.%20Wiki%2F22.%20Entities%2FAntigravity%20%28Google%20DeepMind%29) — 6번째 audience system file 케이스
- [张汉东](obsidian://open?vault=CMDS_LLM_Wiki&file=20.%20Wiki%2F22.%20Entities%2F%E5%BC%A0%E6%B1%89%E4%B8%9C) — DESIGN.md → spec → plan 공학적 파이프라인

### 8.3 External

- [getdesign.md](https://getdesign.md/) — 69개 브랜드 디자인 시스템 큐레이션 (원형 패턴)
- [cmdspace-web-builder skill](`~/.claude/skills/cmdspace-web-builder/SKILL.md`) — v4.3 표준
- 실전 레퍼런스: [system.cmdspace.work](https://system.cmdspace.work) · [llm-wiki.cmdspace.work](https://llm-wiki.cmdspace.work) · [9yohan.cmdspace.work](https://9yohan.cmdspace.work)

---

## 9. Follow-up Actions (DESIGN.md 추가에 따른 시스템 정합성)

이 파일 추가로 mothership 이 *8 → 9 system files* 가 됨. 다음 정합성 작업이 필요:

- [ ] **CLAUDE.md / AGENTS.md / ANTIGRAVITY.md / CMDS.md** 의 "📌 Related System Files" 표를 8개 → 9개로 갱신 (DESIGN.md = precedence 9 추가)
- [ ] **🏛 CMDS Head Quarter** 의 System Files 섹션에 DESIGN.md 항목 추가
- [ ] **system-docs-updater 스킬** 의 동기화 대상 목록에 DESIGN.md 추가 (백업 + share + DEV + Vercel 4-way fan-out)
- [ ] **system.cmdspace.work 배포** — DESIGN.md 가 공개 가능한 *6번째 파일* 인지 결정 (BRAIN/BRAIN_PROMPT 처럼 제외할지, CLAUDE/AGENTS/CMDS/Guide/HQ 처럼 포함할지)
- [ ] **legacy 흡수** — `30. Permanent Notes/39. Guideline/Design, Colors and Graphics.md` (2022) 폐기 또는 archive
- [ ] **`💻 Working Environments` 의 Public Deployment 섹션** (CLAUDE.md/AGENTS.md/CMDS.md) — 공개 파일 개수 표기 갱신 (현재 5개 → 6개 가능성)

> **권장 timing**: 위 follow-up 은 *한 세션 / 한 commit* 으로 묶어서 진행. system-docs-updater 스킬 호출로 자동화 가능.

---

**For technical conventions**: see [[CLAUDE.md]] / [[AGENTS.md]] / [[ANTIGRAVITY.md]].
**For system philosophy**: see [[CMDS.md]].
**For navigation**: see [[🏛 CMDS Head Quarter]].

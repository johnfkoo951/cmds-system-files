---
date created: 2026-04-23T21:04
date modified: 2026-09-16
---
# Frontmatter Standard (Required Properties)

Every content note in this vault MUST include these 7 required properties. Template sources and runtime definitions use their own contracts; existing guard exemptions are preserved.

공통 필드·볼트별 적용 계약의 운영 진입점은 [[90. Settings/94. Agent Settings/schema/README|공통 필드와 볼트 프로필]]의 v1.0.1 묶음이다. 메인 루트에서 `ruby "90. Settings/94. Agent Settings/schema/resolve-profile.rb" --vault main --root "$PWD" --path "대상.md"`로 명시 파일의 역할을 선택한다. `resolved`는 분류 성공이며 아래 필드 값 검증 PASS가 아니다. `needs_review`/`error`를 조용히 제외하지 말고 기존 description helper·전용 검사에서 해당 계약을 별도로 확인한다. Main의 author·status와 Wiki의 기여자·질문/논문 상태를 혼합하지 않는다.

```yaml
---
type:           # Note type (note, meeting, people, terminology, curriculum, channel, CMDS, etc.)
aliases: []     # Alternative names (array format)
description: "" # 1-2 sentence English summary for LLMs — ALWAYS wrap in double quotes (see rules #6–#7)
author:
  - "[[구요한]]"  # Author as quoted wikilink array
date created:   # YYYY-MM-DD or YYYY-MM-DDTHH:mm (ISO 8601)
date modified:  # YYYY-MM-DD or YYYY-MM-DDTHH:mm (ISO 8601)
tags: []        # Relevant tags (array format)
---
```

## 편집 경계 — 프론트매터는 최상단이 아니다 (2026-09-14)

노트가 `---`로 시작하면 **닫는 `---`까지가 메타데이터 영역**이고, 편집 가능한 본문은 그 다음 줄부터다.

- "문서 최상단에 추가해", "맨 위에", "제일 먼저" 는 전부 **본문 첫 줄**(닫는 `---` 아래)을 뜻한다. 여는 `---` 위에는 어떤 것도 넣지 않는다.
- 여는 `---` 위에 한 줄이라도 들어가면 그 블록은 더 이상 프론트매터가 아니다. Properties 패널이 통째로 사라지고 YAML이 본문 텍스트로 렌더된다.
- 본문 편집은 프론트매터 필드를 건드리지 않는다. 무관한 편집을 하면서 제목을 고치거나 태그를 추가하거나 날짜를 갱신하지 않는다.
- 프론트매터가 없는 노트에 새로 넣을 때는 1번 줄에서 시작한다. 위에 빈 줄조차 두지 않는다.

이 규칙은 LLM이 "최상단"을 문자 그대로 파일 offset 0으로 해석해 여는 `---` 위에 삽입하면서 실제로 깨진 사례에서 나왔다. CMDS Achmage 플러그인은 프롬프트와 코드 양쪽에서 이를 강제한다 — 앵커 기반 편집 연산이 본문에만 매칭되므로, 프론트매터 안에만 존재하는 앵커는 메타데이터를 고치는 대신 실패한다.

## Rules

1. **Wikilinks in YAML must be quoted**: `"[[link]]"` not `[[link]]`
2. **Date format**: Always ISO 8601 — `YYYY-MM-DD` or `YYYY-MM-DDTHH:mm`
3. **Array format**: Use hyphen + space for arrays (author, tags, aliases)
4. **CamelCase for compound words**: `myRate`, `totalPage`, `startReadDate` (⚠️ `rating` 사용 금지 → 반드시 `myRate`)
5. **Status values** (5 options): `unread` / `reading` / `inProgress` / `completed` / `archived`
6. **`description` must be in English**: 1-2 sentences describing what the note contains and when an LLM should reference it. This is a machine-readable hint for AI agents (Claude Code, Gemini CLI, ChatGPT, etc.) to decide relevance in future sessions. Write it as a skill/tool description — specific, action-oriented, no fluff.
	- ✅ Good: `"Meeting minutes from 2026-04-07 LG AX camp retrospective. Contains CEO feedback summary and next-action items."`
	- ❌ Bad: `"회의록입니다"` (Korean, non-descriptive)
	- ❌ Bad: `"This is a note"` (no signal for relevance)
7. **`description` must be wrapped in double quotes `"..."`**: Long free-text strings (esp. `description`) must always use double-quote form. YAML 1.2 forbids `": "` (colon + space) and `" #"` (space + hash) inside plain (unquoted) scalars — they silently break the parser, causing description to truncate or corrupt all subsequent frontmatter fields. This is not a style preference; it is a parser-correctness requirement.
	- ✅ Safe: `description: "Draft curriculum ... Operations: 3 main + 6 assistants ..."`
	- ❌ Breaks Obsidian Properties panel: `description: Draft curriculum ... Operations: 3 main ...` (plain scalar with embedded `: `)
	- **Rule of thumb**: if the value contains any `:`, `#`, `[`, `]`, `{`, `}`, `,`, `&`, `*`, `?`, `|`, `>`, `!`, `%`, `@`, or spans beyond a short phrase, quote it. For multi-line text use `>-` (folded) or `|-` (literal) block scalars instead.
8. **No numeric tags**: Obsidian tags must contain at least one non-numeric character. Numeric-only values in `tags:` (e.g. `2`, `15`, `22`) break the Properties panel rendering (yellow warning). Never harvest body references like `#2` / `#22` (pipeline numbers, issue numbers) into `tags:` — they are not tags. In the **body**, when writing a `#숫자` reference (e.g. pipeline item number), wrap it in backticks — `` `#22` `` — so Obsidian does not parse it as a tag attempt.
	- ✅ `tags: [us-trip, starlink]` + body: ``파이프라인 `#22` 와 연결``
	- ❌ `tags: [us-trip, 2, 22, 15]` / body: `파이프라인 #22와 연결` (tag 오인 수집 → Properties 깨짐)

### Frontmatter 로컬 파일·폴더 링크 (2026-09-16)
- 신규 작성하거나 명시적으로 수정하는 frontmatter의 로컬 파일·폴더 탐색 값은 **실제 Hookmark가 발급한 `hook://file/…` URI**를 큰따옴표로 기록한다. `localDev`·`artifactArchivePath`와 로컬 자료를 가리키는 source 계열 값에도 적용한다. `hook://file/…`는 형식 설명용 자리표시자이며 실제 값으로 저장하지 않는다.
- 설치된 Hookmark 앱을 현재 기기에서 찾고 그 앱의 scripting dictionary 또는 지원 UI를 확인한다. 실제 대상의 bookmark를 조회·생성하여 앱이 반환한 URL을 그대로 받으며, 같은 URL로 bookmark를 다시 조회한 `bookmark.path`가 의도한 실제 파일·폴더와 일치하는지 확인한다. 앱 이름·bundle ID를 다른 기기에 고정하지 않고 ID·쿼리 문자열을 손으로 만들거나 재인코딩하지 않는다.
- URI 형태만으로 대상 존재·동일성·다른 기기에서의 열림을 인증하지 않는다. 앱 미설치·미지원·조회 실패·아직 없는 대상이면 `unavailable` 또는 미확인 사유와 실제 경로를 본문에 기록하고, 선택적인 탐색 필드는 확보할 때까지 생략한다. `file://`나 절대경로로 조용히 대체하지 않고 다른 독립 작업은 계속한다. 이 규칙 자체로 추가 사용자 승인 단계를 만들지 않는다.
- 명령 실행·재현·복원에 필요한 실제 경로는 본문의 백틱·명령 블록·외부 manifest에 보존한다. 기존 frontmatter의 절대경로·`file://` 값은 역사적 legacy로 읽고 필요 시 검토하며 자동 일괄 변환하지 않는다. 보호된 Raw Original Content·과거 명령·경로 매핑을 바꾸지 않는다.
- 볼트 내부 파일은 기존 quoted wikilink, 볼트 간 연결은 기존 `obsidian://advanced-uri` 계약을 따른다. 실행 코드·설정·manifest가 소비하는 파일시스템 경로를 Hookmark URI로 바꾸는 규칙은 아니다.

## Optional Properties

- `schemaVersion:` — I01 프로필 묶음에 명시적으로 맞추어 작성·검토한 콘텐츠에서만 사용하는 opt-in 버전 문자열 (현재 `1.0.1`). 문서 자체 `version` 및 플러그인 버전과 별개이며, 필드가 있다는 사실이나 resolver 성공은 전체 검증 인증이 아니다. 기존 노트에 자동 backfill하지 않는다.
- `CMDS:` — CMDS category reference (quoted wikilink)
- `index:` — Index reference (quoted wikilink)
- `status:` — One of 5 standard values above
- `artifactStatus:` / `artifactArchivePath:` — 완료 JSON/PY의 외부 보관을 기록하는 대표 MD에서만 사용 (2026-09-09). `artifactStatus`는 `planned` / `partial` / `archived`; `artifactArchivePath`는 필드명을 유지하되, 신규·명시 수정 시 위 규칙으로 확인한 외부 묶음의 Hookmark URI를 큰따옴표로 기록한다. 실제 경로는 본문·manifest에 보존하고 기존 절대경로 값은 legacy로 읽는다. 대상·Hookmark 미확보 시 선택 필드를 생략하고 사유·실제 경로를 본문에 남긴다. planned/partial은 이관 완료를 뜻하지 않는다. 기존 노트 `status` 및 지식 승격과 별개다. 주요 기획·경로 매핑·재개·백업/복원 기록은 [[90. Settings/94. Agent Settings/claude/rules/file-creation-rules|file-creation-rules]]의 Completed Artifact Closeout을 따른다.
- `wikiVaultRelated:` / `mainVaultRelated:` — **볼트 간 상호참조 (2026-08-27 표준)**: mothership 노트 → 위키 페이지는 `wikiVaultRelated:`, 위키 페이지 → mothership 노트는 `mainVaultRelated:`. 값은 advanced-uri 마크다운 링크 배열 — `"[LLM Wiki: {page}](obsidian://advanced-uri?vault=CMDS_LLM_Wiki&filepath={URL-encoded path}.md)"`. 대상 볼트에 Advanced URI 플러그인이 없으면 기본형 `obsidian://open?vault=...&file={path without .md}` 폴백. 액션명 `adv-uri` 오타·콜론 뒤 공백 금지. 형식 정본: `.claude/rules/wikilink-rules.md` §6.
- `published:` / `publishedUrl:` / `publishedChannels:` — **발행 추적 (2026-08-26 채택)**: 외부 채널에 발행된 콘텐츠의 마스터 노트에는 발행 시점에 `published: true` (boolean 체크박스) + `publishedUrl:` (정본 URL, 예: `https://jisan.cmdspace.work/posts/{slug}/`) + `publishedChannels:` (배열 — `blog`/`threads`/`x`/`linkedin`/`kakao`/`newsletter`)를 기입한다. 발행 전 초안·SNS 캠페인 노트는 `published: false`로 시작 (cmds-sns-promo 스킬 컨벤션과 동일). URL이 여러 채널이면 정본(블로그) URL을 `publishedUrl:`에, 나머지는 `publishedChannels:`로. OSMU 매핑 정본: 지산 프로젝트 `08-발행-매트릭스.md` §6.
- `model:` / `effort:` — **AI 작성 노트 표기** (2026-08-17 채택, LLM Wiki 페르소나 컨벤션 이식): 에이전트가 작성·대필한 노트는 정확한 모델 ID 와 reasoning effort 를 기록한다 — `model: "claude-fable-5[1m]"` · `effort: "xhigh"`. `author:` 는 `"[[구요한]]"` 유지 (볼트 소유자), 모델 필드가 AI 작성자 기록. 데일리 노트는 추가로 `timezone:` (KST) 과 `dailyStatus:` (pending → filled → final) 를 사용 (`.claude/commands/daily.md` 정본). **기입 의무 범위 (2026-08-25 확장, 레인 감사 후속)**: 데일리 노트만이 아니라 에이전트가 생성하는 모든 산출물 — `70. Outputs/74. Projects/**` · `00. Inbox/03. AI Agent/agents/**` · `40. Docs/42. AI Generated/**` — 에 `model:` 을 기입한다. 이 필드가 채워지면 폴더 휴리스틱 없이 사람/기계 레인을 판별할 수 있다 ([[2026-08-23-lane-classification-audit]]).

### `CMDS:` vs `index:` — Direction Rule ⚠️

Per 🏛 CMDS Guide (authoritative):

| Property | Points to | Examples |
|----------|-----------|----------|
| `CMDS:` | **📚 specific subcategory** (2nd-level, N01–N99) | `"[[📚 102 Topics]]"`, `"[[📚 210 Literature Reviews]]"`, `"[[📚 240 Books]]"`, `"[[📚 491 Codes]]"`, `"[[📚 840 Lectures]]"` |
| `index:` | **🏷 Index note** (aggregator in `90. Settings/96. Index/`) | `"[[🏷 Research Notes]]"`, `"[[🏷 Meeting Notes]]"`, `"[[🏷 Books]]"`, `"[[🏷 People]]"`, `"[[🏷 Prompts]]"`, `"[[🏷 Syntax and Codes]]"`, `"[[🏷 Lecture Notes]]"` |

**Common mistakes to avoid**:

- ❌ `CMDS: "[[📖 100 Themes]]"` (📖 top-level is conceptual; never a frontmatter value)
- ❌ `index: "[[📚 102 Topics]]"` (📚 belongs in `CMDS:`, not `index:`)
- ✅ `CMDS: "[[📚 102 Topics]]"` + `index: "[[🏷 Research Notes]]"`

**Exception — system files**: the 9 system files (CLAUDE.md, AGENTS.md, ANTIGRAVITY.md, CMDS.md, 🏛 CMDS Guide, 🏛 CMDS Head Quarter, BRAIN.md, BRAIN_PROMPT.md, DESIGN.md) are vault-top-level navigation documents and MAY use 🏛 hub notes (`"[[🏛 CMDS Head Quarter]]"`, `"[[🏛 CMDS Guide]]"`) in `index:`. Normal notes must still use 🏷 Index notes only. Do not "fix" system-file frontmatter to 🏷.

**Default 🏷 per CMDS range** (pick the closest fit, override if content dictates):

| CMDS range | Default `index:` |
|------------|-----------------|
| `📚 10X` (Themes) | `[[🏷 Research Notes]]` |
| `📚 2XX` (Literature) | `[[🏷 Research Notes]]` · `[[🏷 Books]]` for 240 |
| `📚 491 Codes` · `📚 493 Scripts` | `[[🏷 Syntax and Codes]]` |
| `📚 492 Prompts` | `[[🏷 Prompts]]` |
| `📚 5XX` (Products) | `[[🏷 Guideline]]` · `[[🏷 References]]` |
| `📚 6XX` (Specialties) | `[[🏷 Research Notes]]` |
| `📚 802 Articles` | `[[🏷 Draft Article]]` · `[[🏷 Outcomes]]` |
| `📚 840/841` (Lectures/Curriculum) | `[[🏷 Lecture Notes]]` |
| `📚 831 Consulting` | `[[🏷 Meeting Notes]]` · `[[🏷 Project Notes]]` |
| `📚 820 Research` | `[[🏷 Research Notes]]` |

The 📖 top-level names (📖 100 Themes, 📖 200 Literature …) are **conceptual labels** used in prose and UI copy, never inside frontmatter wikilinks.

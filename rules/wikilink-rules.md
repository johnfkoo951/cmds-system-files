# Obsidian Wikilink Rules + File Reference Convention

## Decision Tree — When to Use Which Reference Form

볼트 안에서 다른 파일을 가리킬 때 **3가지 표기** 중 하나를 선택. 잘못 쓰면 (a) 깨진 링크, (b) Inbox 에 빈 파일 자동 생성, (c) LLM 이 컨텍스트로 못 가져감 등의 문제 발생.

| 상황 | 표기 | 예시 |
|------|------|------|
| **Vault 내부 파일** 일반 참조 (default) | `[[wikilink]]` | `[[canonical]]`, `[[🏛 CMDS Head Quarter]]` |
| **에이전트가 작업 시 자동 로드해야 할** 핵심 파일 | `@` import | `@.claude/rules/wikilink-rules.md`, `@1. Identity/canonical.md` |
| **Vault 외부 경로를 본문·명령에서 설명** (`/DEV/` · `~/.claude/skills/` · `/Users/...` 등) | 백틱 코드 | `` `/Users/yohankoo/DEV/9yohan-constellation/index.html` `` |
| 외부 URL · 라이브 사이트 | 그대로 | `https://9yohan.cmdspace.work` |
| 코드 식별자 · 명령어 · handle | 백틱 코드 | `` `kepler.map` ``, `` `vercel deploy --prod` `` |

**Frontmatter의 로컬 파일·폴더 탐색 값은 별도 규칙이다 (2026-09-16).** 실제 Hookmark가 발급한 `hook://file/…` URI를 대상 bookmark의 경로와 대조한 뒤 큰따옴표로 기록한다. 이 문자열은 형식 자리표시자이며 실제 링크를 조립하는 예제가 아니다. 앱·ID·query를 추측하지 않고, 미확보 사유와 실제 경로는 본문에 남긴다. `file://`로 조용히 폴백하거나 legacy·Raw 원문을 일괄 치환하지 않는다. 상세 절차는 [[90. Settings/94. Agent Settings/claude/rules/frontmatter-standard|frontmatter-standard]]의 Frontmatter 로컬 파일·폴더 링크를 따른다. 볼트 내부 wikilink와 6절의 교차 볼트 URI는 유지한다.

**Default 는 `[[wikilink]]`**. `@` import 와 백틱은 명확한 이유가 있을 때만 사용.

---

## 1. `[[wikilink]]` — Default for Vault-Internal References

### Syntax

| Pattern | Usage |
|---------|-------|
| `[[Note Name]]` | Basic link |
| `[[Note Name\|Display Text]]` | Aliased link |
| `[[Note Name#Heading]]` | Link to heading |
| `[[Note Name^block-id]]` | Link to block |
| `![[Note Name]]` | Embed file |
| `![[image.png]]` | Embed image |

### Rules

1. **Always use wikilinks `[[]]`** for internal references, NOT markdown links
2. **Wikilinks in YAML must be quoted**: `"[[link]]"` not bare `[[link]]`
3. **Array fields** (`author:`, `attendees:`, `aliases:`): Use array format with quoted wikilinks
4. **Emoji prefixes are PART of the filename — never strip them**. Files with 📜/📚/🏛/🏷/📎/📦/🔖/📈/🎹/📘 prefixes require the exact emoji in the wikilink. If you write `[[Schema는 Harness다]]` instead of `[[📜 Schema는 Harness다]]`, Obsidian treats it as a missing link and **auto-creates an empty placeholder file in `00. Inbox/`** when clicked. This pollutes the inbox with orphan files.
5. **Verify before linking**: Before writing a wikilink to a file with an emoji prefix, use Glob/Bash to confirm the exact filename including the prefix. Never guess.
6. **Use aliases for cleaner display**: If the visible text shouldn't show the emoji, use the aliased form: `[[📜 Long Title|Display Text]]` — the link still resolves correctly because the target before `|` is exact.

### Examples in This Vault

- `[[🏛 CMDS Head Quarter]]` — Main hub
- `[[📚 620 Generative AI]]` — CMDS category
- `[[구요한]]` — People note (no prefix)
- `[[🏷 Meeting Notes]]` — Index page
- `[[📜 Schema는 Harness다 - Karpathy LLM Wiki와 CMDS의 구조적 동치에 관한 보고서|Schema는 Harness다 보고서]]` — Aliased link with emoji-prefixed target

### Anti-Pattern (DO NOT)

```markdown
❌ [[Schema는 Harness다 보고서]]                    # Missing 📜 prefix → creates empty file in Inbox
❌ [[CMDS Head Quarter]]                          # Missing 🏛 prefix → creates empty file
❌ [[620 Generative AI]]                          # Missing 📚 prefix → creates empty file
```

```markdown
✅ [[📜 Schema는 Harness다 - Karpathy LLM Wiki와 CMDS의 구조적 동치에 관한 보고서]]
✅ [[🏛 CMDS Head Quarter]]
✅ [[📚 620 Generative AI]]
```

---

## 2. `@` Import — When the Agent Must Auto-Load the File

`@path/to/file.md` 는 Claude Code 의 **import directive**. wikilink 와 다른 기능적 의미:

- `[[wikilink]]` = Obsidian 의 *navigation hyperlink* (사람이 클릭해서 이동). LLM 도 보지만 자동 로드는 X.
- `@path/to/file.md` = Claude Code 의 *context import* (LLM 컨텍스트에 파일 본문이 자동 삽입). 사람에겐 plain text.

### When to Use

다음 중 하나라도 해당하면 `@` import 사용:

1. **세션 시작 시 반드시 같이 로드되어야** 의미 있는 파일 (예: `CLAUDE.md` 가 `@.claude/rules/indentation-rules.md` 를 import — 이 룰 없이 LLM 이 인덴테이션 실수)
2. **프로젝트 README/entry point** 가 작업 시 같이 읽혀야 할 정본을 명시할 때 (예: 9요한 README 가 `@1. Identity/canonical.md` 를 import — README 만 보고 canonical 안 읽으면 매핑 모름)
3. **Cascade 가 필요한 룰** (CLAUDE.md → rules → sub-rules)

### When NOT to Use

- 단순 navigation 목적 (사용자가 클릭해서 이동만 원하는 경우) → `[[wikilink]]`
- 너무 많이 import 하면 컨텍스트 낭비 — **꼭 자동 로드돼야 의미 있는 것만**
- 운영 디테일·시나리오·아카이브는 보통 import 대상 아님 (필요 시 LLM 이 별도 Read)

### Path Syntax

- **Vault root 기준 상대경로**: `@CLAUDE.md`, `@.claude/rules/wikilink-rules.md`
- **현재 파일 위치 기준 상대경로**: `@./neighbor.md`, `@../parent-folder/file.md`
- **같은 폴더 내**: 파일명만으로 OK (`@ecosystem-plan.md`)
- **하위 폴더**: 폴더 경로 포함 (`@1. Identity/canonical.md`)

### Examples

```markdown
# CLAUDE.md (vault root)
@.claude/rules/indentation-rules.md
@.claude/rules/wikilink-rules.md
@.claude/rules/frontmatter-standard.md

# 9yohan/README.md (project entry point)
@1. Identity/canonical.md
@2. Implementation/constellation.md
@ecosystem-plan.md
```

### Pairing Pattern: `@` import + `[[wikilink]]`

CLAUDE.md 가 사용하는 표준 패턴 — *기능* 과 *navigation* 양쪽 충족:

```markdown
> @CMDS.md → [[CMDS.md]] — System philosophy & user context (precedence: 4)
> [[AGENTS.md]] — Codex·Cursor 용 (자동 로드 불필요 → wikilink 만)
```

`@` 가 LLM 자동 로드 · `[[]]` 는 사람이 클릭해서 이동.

### Anti-Pattern

```markdown
❌ @[[CLAUDE.md]]                # @ + wikilink 혼용 — 둘 다 깨짐
❌ @"CLAUDE.md"                  # 따옴표 불필요
❌ @/Users/yohankoo/...          # 절대경로는 동작은 하나 portable 하지 않음
❌ 모든 관련 파일을 @ import     # 컨텍스트 낭비 — 핵심 정본만 import
```

---

## 3. 백틱 코드 — Vault 외부 경로 · 코드 식별자

다음은 wikilink 대상이 아니므로 **본문·명령·재현 기록에서는 백틱 코드**로 표기한다. frontmatter 탐색 값은 위 Hookmark 규칙을 따른다:

- Vault 외부 절대경로: `` `/Users/yohankoo/DEV/9yohan-constellation/` ``
- `~/.claude/skills/...` 같은 글로벌 스킬 경로
- 셸 명령어: `` `vercel deploy --prod` ``
- 코드 심볼: `` `kepler.map` ``, `` `Task Packet` ``
- 외부 라이브러리·패키지 이름

### Why Not Wikilink?

Vault 외부 파일은 Obsidian 이 resolve 하지 못함. wikilink 로 쓰면 빈 placeholder 가 생성되거나 깨진 링크로 남음.

---

## 4. 파일 이동·개명·삭제 → 의존 파일 갱신 (Dependency Update) ⚠️

**정본은 [[90. Settings/94. Agent Settings/claude/rules/file-move-rules|file-move-rules]]이다.** 이동·개명 전에 아래 경로를 명시적으로 읽고 그 분류·적용·검증 절차를 따른다. 삭제는 의존성 검사를 함께 적용하되 별도의 삭제 권한이 필요하다.

@.claude/rules/file-move-rules.md

- **basename이 같다는 이유만으로 모든 wikilink가 안전한 것은 아니다.** basename-only 링크도 의도한 동일 대상을 유지하는지 확인한다. 경로형 wikilink·임베드·@import·활성 백틱/설정 경로·교차 볼트 URI는 정확 경로와 기준 볼트를 검증한다.
- 이동되는 문서 자체의 상대경로 의존성도 새 위치에서 확인한다. 동명 파일·다른 볼트의 같은 경로·표시 alias를 대상 정체성과 혼동하지 않는다.
- **활성 참조만 갱신하고 역사·Raw Source 원문·의도된 씨앗은 보존한다.** 같은 문서에 역사와 현재 navigation이 섞이면 참조·구역별로 분류한다. 미확인 항목은 자동 치환하지 않는다.
- **완료 기준은 선언 범위의 잘못된 활성 대상 0건 + 보호 역사·원문 바이트 불변 + 검사 누락·미확인 0건이다.** 옛 문자열은 역사·원문·씨앗·표시 alias로 남을 수 있다. 그 잔존 이유를 ledger에 적으며 검색 총 0건을 요구하지 않는다.
- 기존 경로 감사기는 보조 신호다. 휴리스틱 통과·파일 존재만으로 정확한 대상·역사 보존을 보증하지 않는다. 권한 밖 참조와 미검증 표면은 별도로 보고한다.

### Checklist (파일 이동·개명 시)
- [ ] 정본 절차를 읽고 원래 → 새 볼트/경로 매핑·권한·원본/보호 바이트 기준선 기록
- [ ] 선언한 범위에서 active/history/raw/seed/unresolved를 구역별로 분류하고 동명·상대경로·닷폴더·URI 포함
- [ ] 새 대상 확인 후 허용된 active 참조만 갱신, alias·heading·block·임베드 표식 유지
- [ ] active 대상의 정확성·보호 해시·전체 검사 목록 대조, old-name 잔존 이유와 잔여/복원 기록

---

## Quick Reference Card

```
Vault 내부 .md → [[wikilink]]              (default)
   ↓ 단, 에이전트가 자동 로드해야 한다면
Vault 내부 .md → @path/to/file.md          (LLM context import)

Vault 외부 / 코드 / 명령어 → `백틱`        (no wikilink possible)
URL / 라이브 사이트 → 그대로               (https://...)
```

---

## 5. `%%...%%` 주석 = 에이전트에게 주는 프롬프트 (Agent Directive Comments) — 2026-08-17, 2026-11-08 갱신

사용자가 노트 본문에 남기는 `%%...%%` Obsidian 주석은 기본적으로 **AI 에이전트에게 주는 프롬프트**다 (예: `%%이거 검증 필요함%%`, `%%내 노트들 연결할 것%%`, `%%이거 용어랑 출처 확인하자%%`). 다만 사용자가 노트에 남겨 두려고 쓴 메모도 같은 문법을 쓰므로, 처리하기 전에 아래 세 가지 중 무엇인지 먼저 가른다. 사용자 지시(2026-11-08): "주석으로 넣는 것은 프롬프트로 생각하고 반영하면 돼. 노트에 남기는 주석이라 판단되면 그대로 두고."

### 세 가지 주석

| 종류 | 무엇인가 | 판별 단서 | 처리 |
|---|---|---|---|
| **프롬프트** (기본값) | 에이전트에게 무언가를 해 달라는 요청 | 요청이나 청유 (`~할 것`, `~하자`, `~해 줘`, `확인`, `검증`, `찾아`, `정리`, `연결`), 확인을 바라는 물음표, 템플릿의 `%%agent: ...%%` | 이행하고 주석을 결과로 교체 |
| **노트 주석** | 사용자가 자신이나 나중의 독자를 위해 남긴 기록 | 요청이 아니라 관찰, 감상, 사실, 상태를 적은 말 (`%%목사님이 여기서 웃으심%%`, `%%이 문단은 개인 묵상이라 공유하지 않음%%`) | 그대로 보존 |
| **기능성 주석** | 태그나 값만 숨긴 것 | 문장 없이 태그나 데이터만 있다 (`%% #John #John4 %%`, Mermaid의 `%% @key: A`) | 그대로 보존 |

### Rule

1. **노트를 처리(정리·포맷·갱신)할 때 `%%...%%` 를 발견하면 먼저 위 표로 종류를 가른다.** 판별 기준은 "에이전트에게 무언가를 하라는 말인가"다. 동사가 들어 있다는 것만으로 프롬프트로 보지 않는다.
2. **프롬프트는 이행한 뒤 주석을 결과물로 교체한다** (지시문을 남겨두지 않음). 이행 내용은 본문에 자연스럽게 녹이고, 검증류는 `검증:` 접두로 결과를 명시.
3. **노트 주석과 기능성 주석은 한 글자도 바꾸지 않고 그 자리에 둔다.**
4. **애매하면 지우지 않는다.** 할 수 있는 확인은 하되 주석은 남기고, 결과를 주석 바로 아래에 덧붙인 뒤 보고에서 어느 쪽인지 사용자에게 묻는다.
5. **이행할 수 없는 프롬프트**는 주석을 보존하고 사용자에게 무엇이 막혔는지 보고한다.
6. 작업 보고에는 이행한 프롬프트, 보존한 노트 주석, 판단을 보류한 주석을 나눠 적는다.

### Examples

- `%%이거 검증 필요함%%` → 프롬프트. 사실 확인 후 `- 검증: ...` 부연으로 교체
- `%%내 노트들 연결할 것%%` → 프롬프트. 볼트 검색 후 관련 노트 wikilink 블록으로 교체
- `%%만든 조약? 이거 용어랑 출처 확인하자%%` → 프롬프트. 용어와 출처를 확인해 `검증 (용어)`, `검증 (출처)` 줄로 교체 (2026-11-08 설교 노트)
- `%%목사님이 여기서 웃으심%%` → 노트 주석. 보존
- `%% #John #John4 %%` → 기능성 주석. 보존 (숨은 태그)

변경 기록: 2026-08-17 제정(문장형이면 지시, 태그만 있으면 기능성). 2026-11-08 노트 주석을 세 번째 종류로 추가하고, 판별 기준을 '문장형인가'에서 '에이전트에게 하라는 말인가'로 바꿨다. 애매하면 지우지 않는 규칙과 보고 형식을 더했다.

---

## 6. Cross-Vault 상호참조 표준 (마더십 ↔ 위키 볼트) — 2026-08-27

Obsidian wikilink 는 볼트 경계를 넘지 못한다. 볼트 간 참조는 **advanced-uri 마크다운 링크**가 표준이다 (`obsidian://open` 은 폴백).

### Frontmatter 필드 — 방향별로 이름이 다르다

| 방향 | 필드 | 값 형식 |
|------|------|---------|
| 마더십 노트 → 위키 페이지 | `wikiVaultRelated:` | 마크다운 링크 배열 (아래 형식) |
| 위키 페이지 → 마더십 노트 | `mainVaultRelated:` | 동일 형식, vault 만 반대 |

### 표준 형식 (advanced-uri)

```yaml
wikiVaultRelated:
  - "[LLM Wiki: Epistemic Infrastructure](obsidian://advanced-uri?vault=CMDS_LLM_Wiki&filepath=20.%20Wiki%2F21.%20Concepts%2FEpistemic%20Infrastructure.md)"
```

```yaml
# 위키 측 (역방향)
mainVaultRelated:
  - "[Mothership: 포맷은 사고를 강제한다](obsidian://advanced-uri?vault=CMDSPACE_Local_MBP&filepath=30.%20Permanent%20Notes%2F%ED%8F%AC%EB%A7%B7%EC%9D%80%20%EC%82%AC%EA%B3%A0%EB%A5%BC%20%EA%B0%95%EC%A0%9C%ED%95%9C%EB%8B%A4.md)"
```

작성 규칙:

1. **액션 이름은 `adv-uri`(현행 기본)와 `advanced-uri`(1.44.0 이전 이름) 둘 다 정상** — 판정 기준은 대상 볼트·파일이 실제로 있는지. `obsidian://` 콜론 뒤 공백 금지.
2. **`filepath=` 는 볼트 루트 기준 전체 경로 + `.md` 확장자**, URL 인코딩 (공백 `%20`, `/` 는 `%2F`). 한글은 인코딩 없이도 동작하지만 공백·슬래시는 반드시 인코딩.
3. **링크 라벨은 `{볼트 별칭}: {페이지명}`** — `LLM Wiki: X` / `Mothership: X`.
4. **쓰기 전 대상 파일 실존 확인** (Glob/ls). 존재하지 않는 filepath 는 조용히 죽는 링크가 된다.
5. **본문 산문에서는** 텍스트 참조 `→ LLM Wiki: {page}` 도 계속 허용 (가벼운 언급용). 클릭 가능해야 하는 참조는 마크다운 링크 형식.
6. **`vault=` 는 링크를 여는 기기의 볼트 이름** — 같은 노트라도 맥은 `CMDSPACE_Local_MBP`, 폰(iOS)은 `CMDSPACE_iOS(Sync%20updated)`. 폰 볼트에도 Advanced URI 가 켜져 있어 `open`(`.md` 유무 무관)·`adv-uri`·`advanced-uri` 모두 열림 (2026-10-25 확인). 폰용 링크는 앱이 만드는 `open?vault=…&file=…` 형식(괄호 미인코딩, `.md` 없음)을 기본으로.

### 폴백 — Advanced URI 플러그인이 대상 볼트에 없을 때

advanced-uri 는 **대상 볼트에 `obsidian-advanced-uri` 플러그인이 설치·활성화**되어 있어야 동작한다. 대상 볼트의 `.obsidian/plugins/obsidian-advanced-uri/` 존재를 확인할 수 없거나 없으면, 플러그인 불요인 기본형으로 폴백:

```yaml
wikiVaultRelated:
  - "[LLM Wiki: Epistemic Infrastructure](obsidian://open?vault=CMDS_LLM_Wiki&file=20.%20Wiki%2F21.%20Concepts%2FEpistemic%20Infrastructure)"
```

폴백 형식 차이: 액션 `open` · 파라미터 `file=` · `.md` 확장자는 선택(있어도 없어도 열림). (2026-08 현재 마더십·CMDS_LLM_Wiki 양쪽 모두 플러그인 설치 상태 → 표준형 사용.)

### Anti-Pattern

```yaml
❌ "[X](obsidian: //advanced-uri?...)"        # 콜론 뒤 공백 — 프로토콜 인식 실패
❌ "[[LLM Wiki 페이지]]"                       # wikilink 는 볼트 경계 못 넘음 → Inbox 빈 파일 생성
❌ filepath=20. Wiki/21. Concepts/X.md        # 미인코딩 공백·슬래시 — 파라미터 파싱 깨짐
```

# Obsidian Wikilink Rules + File Reference Convention

## Decision Tree — When to Use Which Reference Form

볼트 안에서 다른 파일을 가리킬 때 **3가지 표기** 중 하나를 선택. 잘못 쓰면 (a) 깨진 링크, (b) Inbox 에 빈 파일 자동 생성, (c) LLM 이 컨텍스트로 못 가져감 등의 문제 발생.

| 상황 | 표기 | 예시 |
|------|------|------|
| **Vault 내부 파일** 일반 참조 (default) | `[[wikilink]]` | `[[canonical]]`, `[[🏛 CMDS Head Quarter]]` |
| **에이전트가 작업 시 자동 로드해야 할** 핵심 파일 | `@` import | `@.claude/rules/wikilink-rules.md`, `@1. Identity/canonical.md` |
| **Vault 외부 경로** (`/DEV/` · `~/.claude/skills/` · `/Users/...` 등) | 백틱 코드 | `` `/Users/yohankoo/DEV/9yohan-constellation/index.html` `` |
| 외부 URL · 라이브 사이트 | 그대로 | `https://9yohan.cmdspace.work` |
| 코드 식별자 · 명령어 · handle | 백틱 코드 | `` `kepler.map` ``, `` `vercel deploy --prod` `` |

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
> @CLAUDE.md → [[CLAUDE.md]] — Claude Code specific (precedence: 1)
> @AGENTS.md → [[AGENTS.md]] — Other AI coding agents (precedence: 2)
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

다음은 wikilink 대상이 아니므로 **백틱 코드**로 표기:

- Vault 외부 절대경로: `` `/Users/yohankoo/DEV/9yohan-constellation/` ``
- `~/.claude/skills/...` 같은 글로벌 스킬 경로
- 셸 명령어: `` `vercel deploy --prod` ``
- 코드 심볼: `` `kepler.map` ``, `` `Task Packet` ``
- 외부 라이브러리·패키지 이름

### Why Not Wikilink?

Vault 외부 파일은 Obsidian 이 resolve 하지 못함. wikilink 로 쓰면 빈 placeholder 가 생성되거나 깨진 링크로 남음.

---

## 4. 파일 이동·개명·삭제 → 의존 파일 갱신 (Dependency Update) ⚠️

파일을 **이동(move)·개명(rename)·삭제(delete)** 하면 그 파일을 가리키던 다른 파일들의 링크가 깨진다. **항상** 변경 전후로 인바운드 의존성을 찾아 함께 갱신할 것. "갱신할 때 의존성 체크"는 파일 변경 작업의 *기본값*이다.

### Rule

1. **변경 전 인바운드 전수 검색**: `grep -rl "<old-basename>" "<vault>"` (또는 Obsidian `backlinks file=<name>`). wikilink(`[[X]]`) · 임베드(`![[X]]`) · `@import` · 본문 텍스트 참조 모두 확인.
2. **basename 이 바뀌면 모든 인바운드 `[[old]]` → `[[new]]`** 로 갱신. 표시 텍스트 유지가 필요하면 aliased 형식 `[[new-basename|보이던 텍스트]]`. (표 셀 안에서는 `|` 를 `\|` 로 이스케이프.)
3. **이동만 하고 basename 이 그대로면** wikilink 는 안 깨짐(Obsidian 은 basename 으로 resolve) → wikilink 갱신 불필요. 단 `@import`(경로 기반) · 절대경로 · `![[...]]` 임베드 경로는 점검.
4. **`@import`(CLAUDE.md 등)** 는 basename 이 아니라 *경로*로 resolve → 이동 시 반드시 경로 갱신.
5. **삭제 시**: 인바운드가 남으면 깨진 링크 / Inbox 빈 placeholder 생성. 단 일부 unresolved 링크는 *의도된 지식 씨앗*이므로 무조건 지우지 말 것(판단 후 처리).
6. **인덱스·MOC·프로젝트 허브** 노트는 거의 항상 인바운드 보유 → 개명 시 1순위 갱신 대상.

### Checklist (파일 변경 시 매번)

- [ ] 변경 전 `grep -rl "<old-name>"` 로 인바운드 전수 확인
- [ ] basename 변경 시 모든 `[[old]]` → `[[new]]` (표 셀은 `\|`)
- [ ] `@import` 경로 / 인덱스·MOC·허브 링크 갱신
- [ ] 변경 후 `grep -rl "<old-name>"` 재실행 → **0 건** 확인

---

## Quick Reference Card

```
Vault 내부 .md → [[wikilink]]              (default)
   ↓ 단, 에이전트가 자동 로드해야 한다면
Vault 내부 .md → @path/to/file.md          (LLM context import)

Vault 외부 / 코드 / 명령어 → `백틱`        (no wikilink possible)
URL / 라이브 사이트 → 그대로               (https://...)
```

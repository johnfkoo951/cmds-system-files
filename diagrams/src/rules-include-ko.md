```mermaid
flowchart TD
%% @name: rules-include-ko
%% @alt: CLAUDE.md는 .claude/rules/의 공유 규칙 9개 중 8개를 @include로 읽고, 아홉 번째 file-move-rules는 wikilink-rules 안에서 import되며, AGENTS.md를 쓰는 Codex·Cursor·Gemini CLI는 9개를 명시적으로 읽는다.
%% @key: CL
%% @aux: AG
  CL["`**CLAUDE.md**
Claude Code의 입구`"]
  AG["`**AGENTS.md**
Codex · Cursor · Gemini CLI`"]
  subgraph FOLDER[".claude/rules/ · 공유 규칙 9개"]
    R1["indentation-rules"]
    R2["frontmatter-standard"]
    R4["blank-line-rules"]
    R5["file-creation-rules"]
    R6["video-project-workflow"]
    R3["wikilink-rules"]
    R7["mermaid-rules"]
    R8["directory-structure"]
    R9["`**file-move-rules**
아홉 번째 · wikilink-rules 경유`"]
    R1 ~~~ R5 ~~~ R7
    R2 ~~~ R6 ~~~ R8
    R4 ~~~ R3
    R3 -->|"import"| R9
  end
  CL -->|"@include · 9개 중 8개"| FOLDER
  AG -->|"명시적으로 읽음 · @ 없이"| FOLDER
```
*공유 규칙 9개는 한 폴더에 있고, CLAUDE.md가 8개를 @include로 끌어오며, wikilink-rules가 아홉 번째를 import하고, 다른 에이전트는 폴더를 명시적으로 읽습니다.*

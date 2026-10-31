```mermaid
flowchart LR
%% @name: arch-load-en
%% @alt: CLAUDE.md is the entry Claude Code opens. It always includes the 9 shared rules and CMDS.md; DESIGN, AGENTS and ANTIGRAVITY are read on trigger; BRAIN and BRAIN_PROMPT are read only by the Gobi app.
%% @key: CL
%% @aux: BR
  BR["`**BRAIN.md · BRAIN_PROMPT.md**
read only by the Gobi app`"] ~~~ CL["`**CLAUDE.md**
the entry Claude Code opens`"]
  subgraph ALWAYS["Always · @include"]
    R["`**9 shared rules**
.claude/rules/`"]
    CM["`**CMDS.md**
philosophy and context`"]
  end
  subgraph TRIG["On trigger · explicit Read"]
    D["`**DESIGN.md**
before visual artifacts`"]
    AA["`**AGENTS.md · ANTIGRAVITY.md**
with Codex, Cursor or Gemini`"]
  end
  CL --> ALWAYS
  CL --> TRIG
```
*CLAUDE.md is the single entry: the 9 rules and CMDS.md load every session, DESIGN, AGENTS and ANTIGRAVITY are read on trigger, and the two BRAIN files are read only by the Gobi app.*

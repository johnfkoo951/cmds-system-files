```mermaid
flowchart LR
%% @name: commands-parity-en
%% @alt: The eight core CMDS Process commands point to three harness folders, .claude/commands, .codex/commands and .agents/skills; five Claude Code only commands point to .claude/commands alone.
%% @key: C8
  C8["`**CMDS Process · core 8**
/connect /merge
/develop /share
/inbox /lint
/query /status`"]
  O5["`**Claude Code only · 5**
/seeds /harvest
/daily /weekly
/insight`"]
  HC["`**Claude Code**
.claude/commands/`"]
  HX["`**Codex**
.codex/commands/`"]
  HA["`**Skills mirror**
.agents/skills/`"]
  C8 --> HC
  C8 --> HX
  C8 --> HA
  O5 --> HC
```
*Eight operating commands are mirrored in all three harnesses; five are Claude Code only.*

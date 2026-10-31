```mermaid
flowchart LR
%% @name: commands-parity-ko
%% @alt: CMDS Process 핵심 커맨드 8개는 세 하네스 폴더(.claude/commands, .codex/commands, .agents/skills)로 이어지고, Claude Code 전용 5개는 .claude/commands 하나로만 이어진다.
%% @key: C8
  C8["`**CMDS Process · 핵심 8**
/connect /merge
/develop /share
/inbox /lint
/query /status`"]
  O5["`**Claude Code 전용 · 5**
/seeds /harvest
/daily /weekly
/insight`"]
  HC["`**Claude Code**
.claude/commands/`"]
  HX["`**Codex**
.codex/commands/`"]
  HA["`**스킬 미러**
.agents/skills/`"]
  C8 --> HC
  C8 --> HX
  C8 --> HA
  O5 --> HC
```
*운영 커맨드 8개는 세 하네스에 모두 있고, 5개는 Claude Code 전용입니다.*

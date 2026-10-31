```mermaid
treeView-beta
%% @name: vault-tree-ko
%% @alt: CMDS 볼트의 폴더 트리. 루트 폴더 10개(00~90), 00. Inbox 아래 에이전트 레인 03-1~03-9, 10. CMDS Process/15. Periodic 아래 Daily·Weekly, 에이전트 설정 정본 90. Settings/94. Agent Settings/claude/ 와 그곳을 가리키는 .claude/ 심링크.
%% @key: claude
  CMDSPACE 볼트/
    00. Inbox/ ## 미분류 · 에이전트 초안
      03. AI Agent/
        03-1 … 03-9/ ## 에이전트·기기별 레인 하나씩
    10. CMDS Process/ ## Connect · Merge · Develop · Share
      15. Periodic/
        Daily · Weekly/ ## 시간축
    20. Literature Notes/
    30. Permanent Notes/
    40. Docs/
    50. Assets/
    60. Collections/
    70. Outputs/
    80. References/
    90. Settings/
      94. Agent Settings/
        claude/ ## 정본: agents commands hooks rules skills scripts
    .claude/ ## 심링크 → 94. Agent Settings/claude/
```
*루트 폴더 10개가 전부를 담습니다. 에이전트 설정은 90. Settings 에 한 번만 있고, `.claude/` 는 그곳을 가리키는 심링크일 뿐입니다.*

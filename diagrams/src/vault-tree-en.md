```mermaid
treeView-beta
%% @name: vault-tree-en
%% @alt: Folder tree of the CMDS vault: ten root folders 00 to 90; agent lanes 03-1 to 03-9 under 00. Inbox; Daily and Weekly under 10. CMDS Process/15. Periodic; the canonical agent settings under 90. Settings/94. Agent Settings/claude/, which .claude/ links to.
%% @key: claude
  CMDSPACE vault/
    00. Inbox/ ## unsorted · agent drafts
      03. AI Agent/
        03-1 … 03-9/ ## one lane per agent and machine
    10. CMDS Process/ ## Connect · Merge · Develop · Share
      15. Periodic/
        Daily · Weekly/ ## time axis
    20. Literature Notes/
    30. Permanent Notes/
    40. Docs/
    50. Assets/
    60. Collections/
    70. Outputs/
    80. References/
    90. Settings/
      94. Agent Settings/
        claude/ ## canonical: agents commands hooks rules skills scripts
    .claude/ ## symlink → 94. Agent Settings/claude/
```
*Ten root folders hold everything; agent settings live once, in 90. Settings, and `.claude/` is only a symlink to them.*

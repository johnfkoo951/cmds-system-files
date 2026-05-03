# Vault Directory Structure

```
00. Inbox/                      # Temporary storage and processing
├── 01. Daily Notes/            # Daily journal (01-1. Planners, 01-2. Weekly Notes)
├── 02. Clippings/              # Web clippings (02-1. Literature Notes)
├── 03. AI Agent/               # Code outputs (PRIMARY)
│   ├── 03-1. Claude Code (MBP)/
│   ├── 03-2. Claude Code (Studio)/
│   ├── 03-3. OpenClaw (MBP)/
│   ├── 03-4. OpenClaw (Studio)/
│   ├── 03-5. Codex (MBP)/
│   ├── 03-6. Codex (Studio)/
│   ├── 03-7. Antigravity (MBP)/
│   └── 03-8. Antigravity (Studio)/
├── 04. Excalidraw/             # Visual diagrams
├── 05. Canvas/                 # Canvas notes
├── 06. Automation/             # Automation (Make.com, n8n, STT)
├── 06. GenAI Chats/            # GenAI conversation logs
├── 07. App Sync/               # External apps (Claude, Antigravity, Bear Notes)
├── 08. Unlisted/               # Unlisted items
└── 09. Legacy/                 # Legacy content

10. CMDS Process/               # Connect→Merge→Develop→Share
20. Literature Notes/           # Reading notes (외부 지식 내재화)
30. Permanent Notes/            # Evergreen content (정제된 개인 지식)
40. Docs/                       # Technical documentation (업무 문서/기록)
50. Assets/                     # Reusable resources (재사용 자원)
60. Collections/                # Entity management (People, Meetings, Preferences)
70. Outputs/                    # Final deliverables (최종 산출물)
80. References/                 # Reference materials (참조 자료)
90. Settings/                   # System settings and templates
├── 94. Agent Settings/         # AI agent configs (원본, Obsidian Sync 동기화)
│   └── claude/                 # .claude/ 원본 → symlink로 연결
│       ├── agents/
│       ├── commands/
│       ├── rules/
│       └── skills/
```

## Symbolic Link: .claude/ ↔ 94. Agent Settings/

`.claude/`는 숨김 폴더라 Obsidian Sync 대상이 아닙니다.
원본 파일은 `90. Settings/94. Agent Settings/claude/`에 두고, `.claude/`에서 symbolic link로 연결합니다.

```
.claude/
├── agents   → symlink → 90. Settings/94. Agent Settings/claude/agents
├── commands → symlink → 90. Settings/94. Agent Settings/claude/commands
├── rules    → symlink → 90. Settings/94. Agent Settings/claude/rules
├── skills   → symlink → 90. Settings/94. Agent Settings/claude/skills
├── sessions/          (로컬 전용, 링크 안 함)
├── settings.json      (로컬 전용, 링크 안 함)
└── settings.local.json (로컬 전용, 링크 안 함)
```

### 새 머신에서 수동 설정

```bash
cd <vault-path>/.claude
mv agents agents_backup && mv rules rules_backup
mv skills skills_backup && mv commands commands_backup

ln -s "<vault-path>/90. Settings/94. Agent Settings/claude/agents" agents
ln -s "<vault-path>/90. Settings/94. Agent Settings/claude/rules" rules
ln -s "<vault-path>/90. Settings/94. Agent Settings/claude/skills" skills
ln -s "<vault-path>/90. Settings/94. Agent Settings/claude/commands" commands

# 확인 후 백업 삭제
ls -l  # l로 시작하면 symlink
rm -rf agents_backup rules_backup skills_backup commands_backup
```

## CMDS Categories (100-900)

| Category | Name | Purpose |
|----------|------|---------|
| 📖 100 | Themes | Interests, topics, variables, terminologies |
| 📖 200 | Literature | Concepts, frameworks, theories, reviews |
| 📖 300 | Data | Data management, surveys, databases |
| 📖 400 | Methodologies | Research methods, statistics, ML, codes |
| 📖 500 | Products | Tools (Obsidian, ChatGPT, Claude, etc.) |
| 📖 600 | Specialties | KM, Second Brain, Gen AI, productivity |
| 📖 700 | Creatives | YouTube, SNS, music, digital art |
| 📖 800 | Outputs | PhD, articles, lectures, consulting |
| 📖 900 | Divisions | 9 operational divisions |

## Hierarchy System

- 🏛 — Home/Guide (top level)
- 📖 — 1st level CMDS (100-900 series)
- 📚 — 2nd level CMDS (N01-N99)
- (No icon) — 3rd level (detailed topics)

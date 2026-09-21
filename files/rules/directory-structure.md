# Vault Directory Structure

```
00. Inbox/                      # Temporary storage and processing
├── _Gobi_Captures/             # Gobi capture inbox
├── 01. Articles/               # Article collection
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
├── 06. Automation/             # Automation (Make.com, n8n)
├── 06. GenAI Chats/            # GenAI conversation logs
├── 07. App Sync/               # External apps (Claude, Antigravity, Bear Notes)
├── 08. Transcripts/            # Raw transcript landing lanes (08-1. Plaud, 08-2. STT, 08-3. Manual) — processed originals archive to 40. Docs/44. Transcripts
└── 09. Legacy/                 # Legacy content

10. CMDS Process/               # Connect→Merge→Develop→Share
├── 15. Periodic/               # 시계열 로그 (에이전트 작성 — /daily·/weekly 산출, 2026-08-22 Inbox에서 이관)
│   ├── Daily/                  # YYYY-MM-DD.md 데일리 로그 (2022~)
│   └── Weekly/                 # YYYY-Www.md 위클리 회고
20. Literature Notes/           # Reading notes (외부 지식 내재화)
30. Permanent Notes/            # Evergreen content (정제된 개인 지식)
40. Docs/                       # Technical documentation (업무 문서/기록)
├── 42. AI Generated/           # 에이전트 산출 1차 축적층 (Agent Worklog — file-creation-rules.md 참조)
│   └── {Modules,Research,Troubleshooting,Specs,Reviews}/  # cmux-voice worklog가 생성·worklog-daily 잡이 보충
50. Assets/                     # Reusable resources (재사용 자원)
60. Collections/                # Entity management (People, Meetings, Spirituality, Preferences)
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

> **문서화 대상 외 루트 폴더**: `_Settings_/`, `프로젝트/`, `context/`, `copilot-custom-prompts/` (Obsidian Copilot 플러그인 자동 생성), `_starter-kit/` 계열은 canonical CMDS 구조 밖의 시스템·legacy 폴더 — 위 트리에 넣지 않고 여기서만 명시한다.

> **설교 노트 단일 홈 (2026-08-02 확정)**: 모든 `type: sermon` 노트의 물리적 홈은 `60. Collections/64. Spirituality/` **하나**다. 과거 실험 폴더 `20. Literature Notes/23. Sermon/` 은 stale 중복 2건만 남긴 채 방치되어 있어 2026-08-02 폐기(중복 삭제 + 폴더 제거)했다 — **재생성 금지**. "설교문을 문헌으로 분석"하는 경우도 물리 폴더는 64, 분류는 frontmatter `CMDS:` 메타데이터로 한다 (CMDS categorization is metadata, not folders). 녹음 전사 원문은 `00. Inbox/08. Transcripts/` 레인 담당.

## Symbolic Link: .claude/ ↔ 94. Agent Settings/

`.claude/`는 숨김 폴더라 Obsidian Sync 대상이 아닙니다.
원본 파일은 `90. Settings/94. Agent Settings/claude/`에 두고, `.claude/`에서 symbolic link로 연결합니다.

**두 scope 를 구분할 것** (2026-09-21 확정):

| Scope | 경로 | 적용 범위 |
|-------|------|----------|
| **project-scope** | `<vault>/.claude/{agents,commands,rules,skills}` | 이 볼트에서 작업할 때만 로드 |
| **user-scope** | `~/.claude/{agents,commands,skills}` | 모든 프로젝트(`/DEV/` 포함)에서 로드 |

둘은 별개 계층이며 Claude Code 가 **양쪽을 모두 읽는다**. user-scope 는 홈 디렉토리라 Obsidian Sync·git 어디에도 들어가지 않으므로, 볼트 밖에서도 써야 하는 자산은 **볼트를 정본으로 두고 user-scope 를 symlink** 한다. 2026-09-21 에 9Yohan 에이전트 9개가 이 방식으로 이관됐다 — 그 전까지는 MBP 로컬에만 존재해 Studio 전파·백업 대상이 아니었다.

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

user-scope (홈) — 볼트 밖에서도 쓰는 자산만:

```
~/.claude/
├── agents   → symlink → <vault>/90. Settings/94. Agent Settings/claude/agents
│                         (9Yohan 9개 + 기존 2개, 2026-09-21~)
├── commands/          (로컬 전용)
└── skills/            (로컬 전용)
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

**user-scope agents 도 연결** (볼트 밖 `/DEV/` 등에서 9Yohan 을 쓰려면 필수):

```bash
# 홈은 볼트 밖이므로 절대경로 symlink 를 쓴다
[ -d ~/.claude/agents ] && ! [ -L ~/.claude/agents ] && mv ~/.claude/agents ~/.claude/agents_local_backup
ln -s "<vault-path>/90. Settings/94. Agent Settings/claude/agents" ~/.claude/agents
ls -l ~/.claude/ | grep agents   # l 로 시작하면 성공
```

기존 user-scope 파일이 있었다면 `agents_local_backup` 안의 내용을 볼트 폴더로 합친 뒤 백업을 정리한다.

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

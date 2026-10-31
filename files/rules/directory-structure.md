# Vault Directory Structure

```
00. Inbox/                      # Temporary storage and processing
├── _Gobi_Captures/             # Gobi capture inbox
├── 02. Clippings/              # Web clippings (02-1. Literature Notes)
├── 03. AI Agent/               # Code outputs (PRIMARY)
│   ├── 03-1. Claude Code (MBP)/
│   ├── 03-2. Claude Code (Studio)/
│   ├── 03-3. OpenClaw (MBP)/
│   ├── 03-4. OpenClaw (Studio)/
│   ├── 03-5. Codex (MBP)/
│   ├── 03-6. Codex (Studio)/
│   ├── 03-7. Antigravity (MBP)/
│   ├── 03-8. Antigravity (Studio)/
│   └── 03-9. Grok Bot (MBP)/
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
60. Collections/                # Entity management (People, Meetings, Spirituality, Bases, Preferences)
70. Outputs/                    # Final deliverables (최종 산출물)
80. References/                 # Reference materials (참조 자료)
90. Settings/                   # System settings and templates
├── 94. Agent Settings/         # AI agent configs (원본, Obsidian Sync 동기화)
│   ├── claude/                 # .claude/ 원본 → symlink로 연결
│   │   ├── agents/
│   │   ├── commands/
│   │   ├── hooks/
│   │   ├── rules/
│   │   ├── skills/
│   │   └── scripts/            # check-system-dates.rb · lint-description.rb · vault-hygiene.rb (symlink 대상 아님)
│   ├── cmux/
│   └── schema/                 # 공통 필드·볼트 프로필 번들 (frontmatter-standard 참조)
└── 96. Index/                  # 🏷 Index notes — frontmatter index: 의 대상
```

> **문서화 대상 외 루트 폴더**: `_Settings_/`, `프로젝트/`, `context/`, `copilot-custom-prompts/` (Obsidian Copilot 플러그인 자동 생성), `Smart Composer/` (Smart Composer 플러그인 생성 이미지), `_starter-kit/` 계열은 canonical CMDS 구조 밖의 시스템·legacy 폴더 — 위 트리에 넣지 않고 여기서만 명시한다.

> **설교 노트 단일 홈 (2026-08-02 확정)**: 모든 `type: sermon` 노트의 물리적 홈은 `60. Collections/64. Spirituality/` **하나**다. 과거 실험 폴더 `20. Literature Notes/23. Sermon/` 은 stale 중복 2건만 남긴 채 방치되어 있어 2026-08-02 폐기(중복 삭제 + 폴더 제거)했다 — **재생성 금지**. "설교문을 문헌으로 분석"하는 경우도 물리 폴더는 64, 분류는 frontmatter `CMDS:` 메타데이터로 한다 (CMDS categorization is metadata, not folders). 녹음 전사 원문은 `00. Inbox/08. Transcripts/` 레인 담당.

## Symbolic Link: .claude/ ↔ 94. Agent Settings/

`.claude/`는 숨김 폴더라 Obsidian Sync 대상이 아닙니다.
원본 파일은 `90. Settings/94. Agent Settings/claude/`에 두고, `.claude/`에서 symbolic link로 연결합니다.

### 왜 이렇게 하나 — 점폴더 동기화 정책 (2026-10-10)
Obsidian Sync 는 `.obsidian` 을 뺀 점폴더(`.claude`, `.codex`, `.agents`, `.git` 등)를 동기화하지 않는다. 그렇다고 점폴더를 다른 도구로 실시간 동기화하면 아래 사고가 난다.
- `.git` 이 두 머신에서 동시에 바뀌면 저장소가 깨진다.
- `settings.local.json`·`sessions/` 에 든 토큰·개인 기록이 다른 머신으로 퍼진다.
- 훅 스크립트의 머신 전용 경로가 다른 머신에서 그대로 실행된다.
- symlink 가 실제 폴더로 복제되어 두 사본이 따로 놀기 시작한다.
- `.smart-env` 같은 캐시가 계속 바뀌어 충돌과 쓸데없는 전송이 늘고, JSON 설정이 병합 충돌을 일으킨다.

그래서 규칙은 이렇다.
1. **공유할 에이전트 설정은 일반 폴더에 둔다** — `90. Settings/94. Agent Settings/` 아래가 정본이고 Obsidian Sync 로 머신 사이를 오간다. 마더십은 현재 `claude/` 만 이 방식이며, `.codex/`·`.agents/` 는 아직 실제 폴더(git 으로만 이동)다.
2. **각 머신에서 점폴더 symlink 를 한 번만 만든다** — 상대경로(`../90. Settings/...`)로 만들어 볼트 경로가 달라도 그대로 동작하게 한다.
3. **머신 전용 설정은 동기화하지 않는다** — `settings.json`, `settings.local.json`, `sessions/`, `.codex/config.toml`, `.codex/hooks.json` 은 각 머신의 점폴더 안에 실제 파일로 둔다.
4. **`.git` 은 git 으로만 옮긴다** — Sync·rsync 로 복사하지 않는다.
5. osync·rsync 를 쓸 일이 생기면 `.git .claude .codex .agents .smart-env .trash node_modules` 를 제외한다.

**두 scope 를 구분할 것** (2026-09-21 확정):

| Scope | 경로 | 적용 범위 |
|-------|------|----------|
| **project-scope** | `<vault>/.claude/{agents,commands,hooks,rules,skills}` | 이 볼트에서 작업할 때만 로드 |
| **user-scope** | `~/.claude/{agents,commands,skills}` | 모든 프로젝트(`/DEV/` 포함)에서 로드 |

둘은 별개 계층이며 Claude Code 가 **양쪽을 모두 읽는다**. user-scope 는 홈 디렉토리라 Obsidian Sync·git 어디에도 들어가지 않으므로, 볼트 밖에서도 써야 하는 자산은 **볼트를 정본으로 두고 user-scope 를 symlink** 한다. 2026-09-21 에 9Yohan 에이전트 9개가 이 방식으로 이관됐다 — 그 전까지는 MBP 로컬에만 존재해 Studio 전파·백업 대상이 아니었다.

```
.claude/
├── agents   → symlink → ../90. Settings/94. Agent Settings/claude/agents
├── commands → symlink → ../90. Settings/94. Agent Settings/claude/commands
├── hooks    → symlink → ../90. Settings/94. Agent Settings/claude/hooks
├── rules    → symlink → ../90. Settings/94. Agent Settings/claude/rules
├── skills   → symlink → ../90. Settings/94. Agent Settings/claude/skills
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
for d in agents commands hooks rules skills; do
  [ -e "$d" ] && ! [ -L "$d" ] && mv "$d" "${d}_backup"
  ln -s "../90. Settings/94. Agent Settings/claude/$d" "$d"
done

# Obsidian Sync 는 실행 권한을 떨어뜨린다 — 훅은 머신마다 다시 켠다
chmod +x "../90. Settings/94. Agent Settings/claude/hooks/"*.sh

# 확인 후 백업 삭제
ls -l  # l로 시작하면 symlink
rm -rf *_backup
```

- 상대경로 symlink 라 볼트 경로가 머신마다 달라도 고칠 것이 없다 (2026-10-10 이전 문서의 절대경로 예시는 대체됨).
- 훅 같은 `.sh` 파일은 Obsidian Sync 설정에서 **"기타 파일 유형(other file types)"** 동기화를 켜야 넘어온다. 꺼져 있으면 정본 폴더에 `.sh` 가 오지 않는다.

**user-scope agents 도 연결** (볼트 밖 `/DEV/` 등에서 9Yohan 을 쓰려면 필수):

```bash
# 홈은 볼트 밖이므로 절대경로 symlink 를 쓴다
[ -d ~/.claude/agents ] && ! [ -L ~/.claude/agents ] && mv ~/.claude/agents ~/.claude/agents_local_backup
ln -s "<vault-path>/90. Settings/94. Agent Settings/claude/agents" ~/.claude/agents
ls -l ~/.claude/ | grep agents   # l 로 시작하면 성공
```

기존 user-scope 파일이 있었다면 `agents_local_backup` 안의 내용을 볼트 폴더로 합친 뒤 백업을 정리한다.

### LLM Wiki 위성도 같은 패턴 (2026-10-10)
`CMDS_LLM_Wiki` 도 같은 구조로 옮겼다. Codex 하네스까지 있어 정본이 세 갈래다.

| 점폴더 경로 | 정본 (`90. Settings/94. Agent Settings/` 아래) |
|---|---|
| `.claude/{agents,commands,hooks,skills}` | `claude/{agents,commands,hooks,skills}` |
| `.codex/{commands,hooks}` | `codex/{commands,hooks}` |
| `.agents/skills` | `agents/skills` |

머신 전용 실제 파일: `.claude/settings.json`, `.claude/settings.local.json`, `.codex/config.toml`, `.codex/hooks.json`, `.codex/README.md`. 위키의 parity 검사(`90. Settings/Scripts/check-harness-parity.sh`)는 symlink 를 따라가도록 `find -H` 를 쓴다. 절차 정본은 위키의 `CLAUDE.md`·`AGENTS.md` § Agent Settings 정본과 점폴더 링크.

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

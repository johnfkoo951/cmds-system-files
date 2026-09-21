# File Creation Rules

## Code Output Location

**Initial workspace for vault-originated code-related outputs:** `00. Inbox/03. AI Agent/` under the appropriate environment subfolder. Existing DEV projects and the video exception stay in their designated workspaces. Completed JSON/PY outputs follow **Completed Artifact Closeout** below; the Inbox is not their permanent archive.

| Subfolder | Agent | Machine |
|-----------|-------|---------|
| `03-1. Claude Code (MBP)/` | Claude Code | MacBook Pro |
| `03-2. Claude Code (Studio)/` | Claude Code | Mac Studio |
| `03-3. OpenClaw (MBP)/` | OpenClaw | MacBook Pro |
| `03-4. OpenClaw (Studio)/` | OpenClaw | Mac Studio |
| `03-5. Codex (MBP)/` | Codex | MacBook Pro |
| `03-6. Codex (Studio)/` | Codex | Mac Studio |
| `03-7. Antigravity (MBP)/` | Antigravity (Google) | MacBook Pro |
| `03-8. Antigravity (Studio)/` | Antigravity (Google) | Mac Studio |

**Auto-detection**: Check base path to determine machine:
- `/Users/yohankoo/Local Obsidian_MBP/` → MBP
- `/Users/yohankoo/Obsidian_Local/` → Studio

## Completed Artifact Closeout (2026-09-09)
개발·검토가 끝난 JSON·PY 보조 산출물은 볼트 밖으로 이관하고, 주요 기획·결과·보관 위치·재개 방법은 **메인 볼트의 대표 MD**에 남긴다. 작업 중의 초기 Inbox 저장과 완료 후 보관은 다른 단계다. 이 절차는 현재 작업에서 생성·관리하는 완료 산출물의 기본 종료 절차이며, 이미 승인된 범위는 다시 승인받지 않는다. 과거 프로젝트 전체의 일괄 이관·별도 삭제·지식 노트 승격을 자동으로 허용하지 않는다.
### 대상과 완료 조건
- 개발 결과의 검증 또는 검토 결과가 기록돼 있고, 해당 파일에 쓰는 작업·재개 대기 프로세스가 끝난 **명시된 산출물 묶음**을 대상으로 한다. MD의 `status: completed` 하나만으로 파일을 옮기지 않는다.
- 핵심 대상은 프로젝트 생성 JSON·PY다. 같은 실행의 재현에 필요한 TXT·JSONL·log·source·diff·입출력 파일은 의존 묶음으로 선언한 경우에만 함께 이관한다. 원문은 외부에서도 원래 바이트를 보존하며 MD 요약으로 대체하지 않는다.
- `.obsidian`·에이전트 runtime·90. Settings의 운영 설정/스크립트, 현재 쓰는 데이터, 진행 중 `run-state.json`, 계속 추가하는 누적 로그, 다른 작업에서 참조하는 활성 공용 도구는 확장자만 보고 이관하지 않는다. 미해결 참조·실행 의존성은 먼저 해결한다.
- 연구 역할이 running/unknown-submission이거나 사용자의 후속 답변을 기다리면 종료로 취급하지 않는다. 실패/불가 역할을 담은 partial 보고서는 보고서 검증·해당 작업의 종료·writer 중단이 기록됐을 때만 그 종료 범위를 보관할 수 있다. 실패나 미완료를 completed로 바꿔 이관하지 않는다.
### 외부 위치

| 역할 | 위치 |
|---|---|
| 계속 유지보수하는 실행 도구 | `/Users/yohankoo/DEV/<project>/`의 기존 또는 명시한 관리 프로젝트 |
| 완료된 검토·실행 증거와 당시 코드 스냅샷 | `/Users/yohankoo/DEV/_archive/vault-artifacts/<vault-name>/<original-project-relative-path>/<closure-id>/` |
| 기획·결론·현재 위치·재개 안내 | 메인 볼트의 기존 프로젝트 대표 MD. 이미 적절한 보고서/실행관리가 있으면 재사용 |

`original-project-relative-path`는 원래 볼트 루트부터의 **전체 프로젝트 상대경로**다. agent lane까지 포함하여 다른 레인의 동명 프로젝트와 충돌하지 않게 한다. `closure-id`는 날짜와 작업 식별자를 사용하고 이미 존재하는 묶음을 덮어쓰지 않는다. 묶음 안의 원래 상대경로 구조를 보존한다. 머신의 실제 DEV 경로가 다르면 확인한 절대경로와 호스트를 MD에 기록한다.
DEV `_archive`는 로컬 전용이며 이관 자체가 Git push·백업·Obsidian Sync를 뜻하지 않는다. MD에는 확인된 백업/원격 사본 경로 또는 **미확인/로컬 사본만**을 명시한다. 사용자가 요구한 다중 기기 재개·백업 조건이 있으면 이를 충족한 뒤 원래 파일을 제거한다. 연구 증거의 비공개·외부 전송 권한도 그대로 유지한다.
### 메인 MD의 보관 기록
원래 기획·판단·결과를 보존하면서 아래 종료 기록을 추가한다. 원문·코드에 MD frontmatter를 주입하지 않는다.
- `artifactStatus`: `planned`(이관 준비), `partial`(일부 이동/검증 미완), `archived`(선언한 이관 완료). 이관 기록을 시작한 대표 MD에서만 사용하며 기존 노트 `status`와 별개다.
- `artifactArchivePath`: 필드명은 유지하고, 신규·명시 수정 시 해당 외부 묶음에 대해 실제 발급·대상 확인한 Hookmark URI를 큰따옴표로 기록한다 (2026-09-16). [[90. Settings/94. Agent Settings/claude/rules/frontmatter-standard|frontmatter-standard]]의 로컬 파일·폴더 링크 절차를 따른다. 명령·재현·복원용 실제 경로는 본문·manifest에 보존한다. 대상 폴더나 Hookmark가 미확보이면 선택 필드를 생략하고 unavailable 사유·실제 경로를 본문에 남기며, 절대경로·file URI로 조용히 폴백하지 않는다. 기존 절대경로 값은 legacy로 읽고 자동 변환하지 않는다. planned/partial일 때는 존재·복사·이동 완료를 뜻하지 않는다. 이관을 새로 준비하면서 기존 archived 묶음 참조를 조용히 덮어쓰지 말고 이전 종료 기록도 남긴다.
- 본문에 작업 목적·완료 근거·주요 결과, 원래 → 새 위치 표, 호스트, 유지보수 코드 경로/버전(해당 시), 파일별 manifest 위치·해시, 실행 환경·입출력·재개 명령, 범위 밖 잔여, 백업 상태·복원 방법을 기록한다. 파일이 적으면 파일별 표를 MD에 직접 넣고, 많으면 외부 manifest를 연결한다.
- 외부 파일은 볼트 내부 wikilink/Obsidian URI로 연결하지 않는다. 실제 절대경로를 백틱으로 기록하고 필요한 경우 OS에서 여는 명령을 제공한다. 주요 위치와 기획은 외부 manifest만 보아야 알 수 있게 숨기지 않는다.
### 이관·검증·복원 순서
정확한 참조 분류·역사 보존은 [[90. Settings/94. Agent Settings/claude/rules/file-move-rules|file-move-rules]]를 따른다.
1. 대상 파일·완료 근거·writer 중단·원래/새 경로·SHA-256·권한·참조/상대경로 의존성을 기록한다. 기존 대상·symlink·볼트 밖으로 벗어나는 상대경로를 확인하고 충돌은 덮어쓰지 않는다. 미확인 대상은 제외 이유 또는 잔여로 남긴다.
2. 대표 MD에 기획과 planned 보관 기록을 먼저 작성한다. 새 외부 묶음에 파일을 **복사**하고 대상 바이트·권한을 대조한다. manifest에는 원래 위치와 새 위치·해시·검증 결과를 남긴다. 외부 사본 검증 전에는 원래 파일을 제거하지 않는다.
3. 활성 참조를 정확한 새 위치로 갱신하고, 실행본의 상대경로·설정·입출력도 확인한다. 역사 기록·Raw 원문·서명된 실행 증거는 소급 치환하지 않는다. 당시 절대경로가 담긴 불변 증거는 MD/manifest의 매핑으로 설명하고 재개용 작업 사본에서만 해소한다.
4. 파일별로 원래 내용이 계획 당시와 같은지 다시 확인한 뒤 **검증된 이관 대상만** 원래 위치에서 제거한다. 일반적인 파일 삭제와 구분되는 승인된 이동 단계다. 후속 수정·충돌·중단이 있으면 더 제거하지 말고 partial과 실제 복사/이동/미수행 목록을 기록한다. 원래 → 외부 경로 매핑으로 보호 바이트의 보존을 검증한다.
5. 새 위치·파일별 해시·활성 참조·재개 방법·선언한 대상의 원래 경로 잔존 여부를 확인한다. 모두 충족한 뒤 archived로 기록한다. 남겨 둔 운영 파일·진행 로그는 제외 이유와 구분한다. MD 갱신 뒤 qmd 텍스트/증분 임베딩/검색 결과는 orchestrator가 한 번 기록한다.
6. 재개 시 대표 MD의 외부 위치와 manifest를 먼저 읽는다. 원래 폴더에 JSON이 없다는 이유로 연구를 새로 제출하거나 원문을 다시 생성하지 않는다. 새 writer는 별도 DEV 작업 사본에 기록하고 과거 증거를 보존한다. 복원은 현재 파일과 충돌하지 않는 위치에서 원본 해시·권한·참조를 검증하며, 과거 적용 스크립트를 볼트에 무작정 재실행하지 않는다.
보관 완료 보고에는 MD 위치·외부 위치·대상 수·검증 결과·잔여·백업 상태를 명시한다. 이 절차는 에이전트가 수행하는 종료 워크플로이며 cron/hook 자동 설치가 아니다.

## File Naming Convention

- Include date: `YYYY-MM-DD-description.ext`
- Use descriptive names
- Examples: `2026-01-09-data-analysis.py`, `2026-01-09-meeting-summary.md`

## Session Link Frontmatter (새 노트 생성 시)

cmux 안의 Claude Code 세션에서 **볼트에 새 .md 노트를 만들 때**, 프론트매터에
생성 세션의 딥링크를 넣는다 — 노트에서 클릭 한 번으로 그 노트를 만든 세션으로
복귀 (세션이 죽어 있으면 같은 cwd에서 `claude --resume`으로 부활):

```bash
cmux-voice hooklink   # → omnicontrol://focus?workspace=…&cwd=…&session=…&revive=1
```

```yaml
session-link: "<hooklink 출력값 그대로>"
```

- hooklink 실패(OmniControl 데몬 다운·cmux 밖 실행) 시 **생략하고 진행** — 노트 생성을 막지 말 것
- 기존 노트 수정 시에는 추가하지 않는다 (생성 시점의 출생 기록만)
- 시스템 상세: `40. Docs/42. AI Generated/2026-08-02-session-link-딥링크-시스템.md` · OmniControl repo `docs/CMUX-GUIDE.md`

## Agent Worklog (작업 지식 축적, 2026-08-03)

에이전트 작업 기록의 물리적 홈은 `40. Docs/42. AI Generated/` 하위 5폴더 —
직접 파일을 만들지 말고 **`cmux-voice worklog` CLI로 생성**한다
(파일명 `YYYY-MM-DD-제목.md`·템플릿·session-link 자동):

| kind | 폴더 | 무엇을 |
|------|------|--------|
| `research` | `Research/` | 실측·조사로 확정한 사실 |
| `trouble` | `Troubleshooting/` | 재발 가능한 에러 해결 (증상/원인/해결/재발 방지) |
| `spec` | `Specs/` | 새 기능·시스템 구현 명세 |
| `module` | `Modules/` | 재사용 코드·패턴 |
| `review` | `Reviews/` | 프로젝트 회고 (**주간 회고는 weekly-review 잡 관할 — 여기 금지**) |

```bash
echo "<본문>" | cmux-voice worklog trouble "afplay 볼륨 무시" --project OmniControl
```

- 기록 기준·상시 규칙: 전역 `~/.claude/CLAUDE.md` "Agent Worklog" 섹션 (세션이 스스로 기록)
- 세이프티넷: OmniControl 스케줄 잡 `worklog-daily`(매일 22:17)가 당일 DEV 커밋을 훑어 미기록 유의미 작업을 보충 기록
- 42는 1차 축적층 — 영구 가치가 생기면 CMDS Process를 거쳐 `30. Permanent Notes`/위키로 승격
- 인덱스: `42. AI Generated/_INDEX Agent Worklog.md`

## Multi-File Project Folder Rule

When creating projects with multiple related files:
1. **FIRST** create an intermediate folder: `YYYY-MM-DD-project-name/`
2. **THEN** create all related files inside that folder

```
00. Inbox/03. AI Agent/03-5. Codex (MBP)/
└── 2026-01-18-project-name/
    ├── index.html
    ├── styles.css
    └── script.js
```

**Never** scatter related project files directly in subfolder root.

## Exception: Video Projects (Remotion / heavy deps)

Video projects with `node_modules` or large render artifacts MUST go to `/Users/yohankoo/DEV/video-projects/<name>/` instead of the vault. Only context/progress MD files stay in the vault.

See `video-project-workflow.md` for full rule.

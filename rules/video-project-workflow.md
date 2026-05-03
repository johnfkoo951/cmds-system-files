# Video Project Workflow (Remotion & similar)

**영상 제작 프로젝트(Remotion, ffmpeg 기반 등)는 볼트 밖(`/DEV/video-projects/`)에서 작업하고, 볼트에는 컨텍스트/추적 MD만 남긴다.**

## Why

- `node_modules` 가 프로젝트당 100~200MB, 10,000+ 파일 → Obsidian 인덱싱/그래프뷰/검색 성능 저하
- 렌더 산출물(`out/*.mp4`)도 볼트 동기화 부담
- 2026-04-14 정리 시점에 영상 프로젝트 3개로 node_modules 합계 **519MB / 30,000+ 파일** 확인

## Rule

### 사용자가 볼트 내에서 Remotion 또는 영상 제작 작업을 지시하면

1. **프로젝트 코드 위치**: `/Users/yohankoo/DEV/video-projects/<descriptive-name>/` 에 생성
	- 폴더명: 영문, 케밥 케이스, 날짜 프리픽스 없음 (예: `lg-ceo-value-video`)
	- 이곳에 `package.json`, `src/`, `public/`, `out/`, `node_modules/` 모두 위치
2. **볼트 내 추적 MD 위치**: `00. Inbox/03. AI Agent/{current agent lane}/YYYY-MM-DD-<descriptive-name>.md` (Codex MBP: `03-5. Codex (MBP)/`)
	- 기획, 나레이션 초안, 진행 로그, 결정사항, 이슈, 컨텍스트만 담는다
	- 상단에 **DEV 절대경로** 명시 필수
3. **인덱스 업데이트**: `[[🏷 Video Projects]]` (기존 Claude 인덱스 경로: `00. Inbox/03. AI Agent/03-1. Claude Code (MBP)/2026-04-14-video-projects-index.md`) 에 새 항목 추가
4. **DEV 프로젝트 루트 README**: 각 프로젝트 폴더에 `README.md` 생성, 볼트 추적 MD로 역참조

### 볼트 내 추적 MD 필수 섹션

```markdown
## 📍 Project Location
- **DEV path**: `/Users/yohankoo/DEV/video-projects/<name>/`
- **Stack**: Remotion X.Y.Z, React N
- **Render output**: `out/<file>.mp4` — status

## 🎯 Purpose
(왜 만드는지)

## 📦 Components
(소스 구조 요약)

## 📜 Narration / Audio
(나레이션 파일 절대경로)

## ✅ Progress
- [ ] 체크리스트

## 🔧 Resume work
```bash
cd /Users/yohankoo/DEV/video-projects/<name>
npm install
npm run build
```

## 📝 History
- YYYY-MM-DD: 무엇을 했는지
```

### Frontmatter 필수

```yaml
---
type: note
aliases: [Project Name]
description: "Tracking note for the <project>. Project source lives at /Users/yohankoo/DEV/video-projects/<name>/. Reference when <situation>."
author:
  - "[[구요한]]"
date created: YYYY-MM-DD
date modified: YYYY-MM-DD
tags: [video, remotion, ...]
CMDS: "[[📚 630 Development]]"
status: inProgress | completed
---
```

## Existing Projects (as of 2026-04-14)

| DEV Folder | Vault Tracking Note |
|-----------|--------------------|
| `/Users/yohankoo/DEV/video-projects/lg-ceo-value-video/` | `2026-02-24-lg-ceo-value-video.md` |
| `/Users/yohankoo/DEV/video-projects/lg-cns-ch5-probability-video/` | `2026-03-24-lg-cns-ch5-probability-video.md` |
| `/Users/yohankoo/DEV/video-projects/parkjun-welcome-video/` | `2026-03-03-parkjun-welcome-video.md` |

## Anti-pattern

❌ `node_modules` 가 볼트 안에 있는 상태로 방치
❌ 볼트 내에 Remotion `src/` 와 렌더 결과(`out/*.mp4`) 를 두는 상태
❌ 볼트의 프로젝트 폴더에 `.tsx`, `package.json` 같은 소스만 있고 DEV 쪽에는 없음 (중복/분리)
❌ 추적 MD에 절대경로 누락

## Applies to

- Remotion (React 기반 비디오)
- `markdown-video` 스킬 산출물 (최종 mp4 제외하고 중간 이미지/오디오 파일도 /DEV/ 권장)
- ffmpeg/moviepy 기반 파이썬 영상 프로젝트 — 산출물이 크거나 의존성이 무거운 경우
- HeyGen, 기타 AI 비디오 도구로 생성한 중간 파일이 많은 경우

## Exception

- **단일 MP4 파일** (렌더 결과만)은 볼트의 `80. References/81. Attachment/` 또는 관련 노트 폴더에 두어도 무방
- **짧은 셸 스크립트 + 소량 텍스트**로 끝나는 경량 영상 작업은 볼트 inbox 유지 가능

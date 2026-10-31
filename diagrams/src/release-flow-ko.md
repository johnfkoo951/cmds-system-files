```mermaid
flowchart TD
%% @name: release-flow-ko
%% @alt: 볼트에서 시스템 파일을 고치면 게이트를 지나 백업·공유·DEV 사본으로 동기화되고, GitHub에 태그·Release된 뒤 Vercel이 system.cmdspace.work에 배포한다. 버전은 두 층으로, 마이크로 버전은 각 파일 frontmatter에, 매크로 버전은 CHANGELOG와 GitHub Release에 있다.
%% @key: G, SITE
  E["`**시스템 파일 수정**
마이크로 버전 = frontmatter`"] --> G["`**게이트**
날짜 · 버전 · tags`"]
  G --> SYNC["`**①②③ 동기화**
백업 · 공유본 · DEV + ZIP`"]
  SYNC --> GH["`**④ GitHub 태그 · Release**
매크로 버전 = Release`"]
  GH --> SITE["`**⑤ Vercel → 이 사이트**
system.cmdspace.work`"]
```
*볼트에서 고친 시스템 파일 하나가 게이트를 지나 세 곳에 동기화되고 GitHub와 Vercel을 거쳐 이 사이트가 되며, 버전은 파일별 마이크로와 릴리스별 매크로 두 층으로 관리합니다.*

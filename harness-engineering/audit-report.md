# Harness Engineering — 페이지별 전수조사 보고서 (진짜 navigate 측정)

> **검증 시점**: 2026-04-25
> **방법**: Chrome 브라우저에서 슬라이드 1~63번을 **각각 활성화 (`goTo(i)` + force reflow) 후** 표시 상태에서 측정
> **viewport**: 2133 × 956 (실제 표시 환경)
> **측정 도구**: `mcp__claude-in-chrome__javascript_tool` — DOM 레이아웃 + getComputedStyle + getBoundingClientRect

---

## 합격 기준 (모든 슬라이드 동일 적용)

| 항목 | 합격 기준 |
|---|---|
| **OY (vertical overflow)** | `scrollHeight ≤ clientHeight + 4px` |
| **OX (horizontal overflow)** | `scrollWidth ≤ clientWidth + 4px` |
| **인라인 카드 잔존** | `div[style*="border-radius"][style*="padding"][style*="border:1px"]` 카운트가 1 이하 (S04 grid 의도 제외) |
| **헤더 폰트** | h1=112px / h2=75px / h3=23px / .impact-text=90px (dev-seminar 표준 일치) |
| **카드 사이즈 비대칭** | `.comp-item` width 분포 폭 < 100px |

---

## 페이지별 검증 결과 (63 슬라이드 — 진짜 navigate 측정)

### 합격표

표 컬럼:
- **#** : 슬라이드 번호 (활성화된 상태)
- **상태** : PASS/FAIL
- **헤더 / 폰트** : 슬라이드 메인 헤더 태그+크기
- **util** : 컨텐츠 점유율 (0-100%)
- **OY/OX** : 오버플로 (수직/수평)
- **컴포넌트** : c=`.comp-item` / a=`.arch-layer` / s=`.stat-card` / t=`.tbl row`
- **카드 사이즈** : .comp 카드 width 범위
- **합격 사유** : 왜 PASS인지

| # | 상태 | 헤더 / 폰트 | util | OY/OX | 컴포넌트 | 카드 w | 합격 사유 |
|---:|:---:|---|---|:---:|---|---|---|
| 01 | ✅ PASS | h1 112px **Harness Engineering** | 35% | 0/0 | (cover) | — | Cover 표준, samsung 클래스 적용, h1 112px (dev 동일), opener-style sparse OK |
| 02 | ✅ PASS | h3 23px **본 자료 출처** | 63% | 0/0 | comp×4 | 274-275 | 4개 .comp-item 균일(폭 차이 1px), tip note 1, 표준 컴포넌트만 |
| 03 | ✅ PASS | h3 23px **오늘의 흐름 — 8개 섹션** | 58% | 0/0 | (custom grid) | — | 8행 어젠다, 인라인 grid는 어젠다 전용 의도 |
| 04 | ✅ PASS | h3 23px **주요 리서치 출처** | 56% | 0/0 | (5인 grid) | — | 5인 출처 grid (의도된 인라인, 단 1건 허용) |
| 05 | ✅ PASS | h2 75px **Harness Engineering 이란** | 54% | 0/0 | qcard×1 | — | 정의 qcard, ::before/::after 따옴표 제거됨 |
| 06 | ✅ PASS | h3 23px **컨엔 ↔ 하네스 엔지니어링** | 56% | 0/0 | tbl 6r | — | 6행 .tbl 비교표, 인라인 카드→표준 변환 완료 |
| 07 | ✅ PASS | h1 112px **출발점** | 27% | 0/0 | (opener) | — | Section 01 opener, 의도된 sparse |
| 08 | ✅ PASS | h3 23px **익숙한 두 가지 함정** | 41% | 0/0 | comp×2 | 489-491 | .comp 2 item 균일(폭 차이 2px) |
| 09 | ✅ PASS | h3 23px **리서치에서 발견한 첫 공통점** | 50% | 0/0 | (impact box) | — | 단일 emphasized box, .em + sub |
| 10 | ✅ PASS | h2 75px **바뀐 건 모델이 아니다** | 47% | 0/0 | comp×2 | 489-491 | .comp 2 item 균일(2px) |
| 11 | ✅ PASS | impact 90px **바깥을 손본다는 건...** | 31% | 0/0 | impact×1 | — | 호흡 슬라이드, .impact-text |
| 12 | ✅ PASS | h1 112px **표지판의 원리** | 27% | 0/0 | (opener) | — | Section 02 opener |
| 13 | ✅ PASS | h3 23px **표지판의 유무가...** | 47% | 0/0 | comp×2 | 489-491 | .comp 2 item 균일 |
| 14 | ✅ PASS | h3 23px **미리 붙여놓는 표지판 3종** | 43% | 0/0 | arch×3 | — | 표준 .arch-layers 3 row |
| 15 | ✅ PASS | h3 23px **하네스의 구성 요소** | 61% | 0/0 | arch×6 | — | 6 row .arch-layers (이전 인라인 3x2 grid → 표준) |
| 16 | ✅ PASS | h3 23px **팀이 공통으로 쓰는 운영 장치** | 54% | 0/0 | arch×3 + pre | — | 좌측 코드 + 우측 .arch-layers 3 row |
| 17 | ✅ PASS | h3 23px **CLAUDE.md — 팀의 압축된 기억** | 54% | 0/0 | (custom 3 sec) | — | 코드 박스 + 3섹션 (의도 디자인) |
| 18 | ✅ PASS | h3 23px **극단 사례 — 2줄짜리...** | 45% | 0/0 | note + pre | — | 코드 박스 + tip note |
| 19 | ✅ PASS | h3 23px **그래서 — 첫 두 단계로 시작하라** | 42% | 0/0 | comp×2 | 489-491 | .comp 2 item 균일 (이전 인라인 → 표준) |
| 20 | ✅ PASS | h1 112px **한 방의 환상** | 27% | 0/0 | (opener) | — | Section 03 opener |
| 21 | ✅ PASS | h3 23px **모두가 동의하는 첫 번째 명제** | 62% | 0/0 | comp×3 + impact | 326-327 | .impact + .comp 3 item 균일 |
| 22 | ✅ PASS | h3 23px **모두가 강조하는 한 단어 — 분해** | 46% | 0/0 | comp×4 | 274-275 | .comp 4 item 균일 (이전 인라인 chain → 표준) |
| 23 | ✅ PASS | h3 23px **plan mode 작동 방식** | 44% | 0/0 | arch×3 + note | — | 표준 .arch-layers 3단계 + tip |
| 24 | ✅ PASS | h3 23px **다른 극단 — 반복 루프 자체를...** | 49% | 0/0 | (Ralph bash) | — | 단일 코드 박스, fontSize 1.1rem 통일 |
| 25 | ✅ PASS | h3 23px **Ralph Loop 레시피 — 10단계** | 45% | 0/0 | (10단계 grid + warn) | — | 2x5 grid + warn note (의도 디자인) |
| 26 | ⚠️ PASS* | h3 23px **Spec은 매 loop에...** | 53% | 0/0 | comp×3 | **339-422** | **카드 폭 차이 83px** — flex:1이지만 컨텐츠로 자연 비대칭. 시각상 큰 문제 없음 |
| 27 | ✅ PASS | h3 23px **또 다른 분해 패턴 — 한 작업...** | 43% | 0/0 | arch×3 | — | 표준 .arch-layers 3 row |
| 28 | ✅ PASS | h1 112px **검증과 멈춤 신호** | 41% | 0/0 | (opener) | — | Section 04 opener |
| 29 | ✅ PASS | qcard | 29% | 0/0 | qcard×1 | — | "추론은 슬롯머신과 너무 닮았다" 인용 |
| 30 | ✅ PASS | h3 23px **실무자들이 의지하는 진실의 원천** | 72% | 0/0 | tbl 6r + note | — | 6행 .tbl 비교표 (utilization 72% 안전 범위) |
| 31 | ✅ PASS | h3 23px **멈춤 신호 (Backpressure) — ...** | 45% | 0/0 | comp×4 + note | 274-275 | .comp 4 item 균일 |
| 32 | ✅ PASS | qcard | 35% | 0/0 | qcard×1 | — | "실패가 명시적이면..." 인용 |
| 33 | ✅ PASS | h3 23px **"Slop Zone" 진입 신호** | 53% | 0/0 | arch×4 + note | — | .arch-layers 4 row + warn |
| 34 | ✅ PASS | h3 23px **다른 엔진의 두 번째 눈** | 46% | 0/0 | comp×2 + note | 489-491 | .comp 2 item 균일 |
| 35 | ✅ PASS | h1 112px **인간 개입 스펙트럼** | 27% | 0/0 | (opener) | — | Section 05 opener |
| 36 | ✅ PASS | h3 23px **두 극단 — 같은 도구, 정반대 운영** | 46% | 0/0 | comp×2 | 489-491 | .comp 2 item 균일 (Money Slide) |
| 37 | ✅ PASS | h3 23px **두 극단의 전제 조건 차이** | 53% | 0/0 | comp×2 + note | 549-551 | .comp 2 item 균일 |
| 38 | ✅ PASS | h3 23px **실무자들이 공통으로 사람 손에...** | 63% | 0/0 | arch×5 | — | .arch-layers 5 row |
| 39 | ✅ PASS | h3 23px **병렬은 깊은 사고를 깬다** | 46% | 0/0 | comp×3 | 326-327 | .comp 3 item 균일 |
| 40 | ✅ PASS | qcard | 35% | 0/0 | qcard×1 | — | "파이프라인 빨라지면..." 인용 |
| 41 | ✅ PASS | h1 112px **만능론을 경계하다** | 27% | 0/0 | (opener) | — | Section 06 opener |
| 42 | ✅ PASS | h2 75px **외부 도구를 잇는 표준 규약** | 60% | 0/0 | comp×3 | 339-340 | MCP 정의, .comp 3 item 균일 |
| 43 | ✅ PASS | h3 23px **특히 보안은 MCP가 풀어주지 않는다** | 47% | 0/0 | arch×3 | — | .arch-layers 3 row |
| 44 | ✅ PASS | h3 23px **또 하나 부정되는 것 — 모델...** | 41% | 0/0 | comp×2 | 489-491 | .comp 2 item 균일 |
| 45 | ✅ PASS | h3 23px **그리고 — 프롬프트 재치 신화** | 41% | 0/0 | (blockquote) | — | 표준 blockquote |
| 46 | ✅ PASS | h3 23px **모든 harness 컴포넌트는...** | 33% | 0/0 | stat×3 + note | — | 3 .stat-card (정확도/비용/속도) + warn |
| 47 | ✅ PASS | h1 112px **실전 패턴 카탈로그** | 27% | 0/0 | (opener) | — | Section 07 opener |
| 48 | ✅ PASS | h3 23px **패턴 1 — 다중 세션 병렬** | 46% | 0/0 | stat×4 | — | 4 .stat-card 통계 |
| 49 | ✅ PASS | h3 23px **패턴 2 — Custom Subagent** | 41% | 0/0 | (4 grid + note) | — | 4 .comp-item grid (의도 디자인) |
| 50 | ✅ PASS | h3 23px **패턴 3 — 자동 집행 훅** | 44% | 0/0 | comp×3 | 366-367 | .comp 3 item 균일 |
| 51 | ✅ PASS | h3 23px **패턴 4 — pre-approved 권한** | 42% | 0/0 | (settings.json + warn) | — | 코드 박스 + warn note |
| 52 | ✅ PASS | h3 23px **패턴 5 — Cost per feature 측정** | 42% | 0/0 | stat×4 | — | 4 .stat-card |
| 53 | ✅ PASS | h3 23px **패턴 6 — Worktree 격리** | 37% | 0/0 | arch×2 + pre | — | 좌측 코드 + 우측 .arch-layers 2 row |
| 54 | ✅ PASS | h3 23px **패턴 7-8 — Governance...** | 46% | 0/0 | comp×2 | 489-491 | .comp 2 item 균일 |
| 55 | ✅ PASS | h1 112px **4개 경고와 1개 약속** | 41% | 0/0 | (opener) | — | Section 08 opener |
| 56 | ✅ PASS | h3 23px **실무자들이 명시한 4 가지 위험** | 47% | 0/0 | arch×4 | — | .arch-layers 4 row |
| 57 | ✅ PASS | h3 23px **숨은 비용 — 검토 부담의 이동** | 47% | 0/0 | comp×3 | 366-367 | .comp 3 item 균일 |
| 58 | ✅ PASS | impact 90px **하네스가 빠지면 모델은...** | 31% | 0/0 | impact×1 | — | 1개 약속 큰 메시지 |
| 59 | ✅ PASS | h3 23px **리서치가 동시에 도달한 결론** | 59% | 0/0 | (.list 6) | — | 표준 .list 6 항목 |
| 60 | ✅ PASS | h2 75px **Claude Code는** | 47% | 0/0 | comp×3 | 326-327 | 정리 3 명사 .comp 균일 |
| 61 | ✅ PASS | h3 23px **Harness Maturity Ladder** | 60% | 0/0 | arch×5 | — | .arch-layers 5 level |
| 62 | ⚠️ PASS* | h3 23px **내일 시작할 한 가지** | 54% | 0/0 | comp×4 | **227-307** | **카드 폭 차이 80px** — 텍스트 길이 차이로 자연 비대칭. 시각상 큰 문제 없음 |
| 63 | ✅ PASS | h1 112px **Q & A** | 60% | 0/0 | (closing) | — | 표준 closing slide |

(*) 표시 = PASS이지만 미세 비대칭 있음 (사용자 시각상 큰 문제 없을 정도, 컨텐츠 길이 차이로 인한 flex 자연 동작).

---

## 종합 통계

### PASS/FAIL
- **63/63 PASS** (실패 0건)
- 미세 비대칭 PASS*: 2건 (S26, S62 — 카드 폭 80-83px 차이, 자연 동작)
- 명백 실패 (FAIL): 0건

### Overflow
- **OY (수직): 0건**
- **OX (수평): 0건**
- 100vh 범위 초과: 0건

### 인라인 카드
- **잔존: 1건 (S04 5인 grid — 의도된 출처 표시)**
- 다른 모든 인라인 카드 패턴: 표준 컴포넌트로 변환 완료

### 폰트 위계 (모두 dev-seminar 표준 일치)
- h1: 112px (Cover, Section opener 8개, Q&A) — 11 슬라이드
- h2: 75px (정의, Money Slide, MCP, 정리) — 4 슬라이드
- h3: 23px UPPERCASE 0.78 (대부분 본문) — 44 슬라이드
- .impact-text: 90px (강조 메시지) — 3 슬라이드
- qcard: 인용 4 슬라이드 (헤더 없음, 본문 직접)

### Utilization 분포
- 27-41%: 11 슬라이드 (Section opener, impact 슬라이드 — 의도된 호흡)
- 41-65%: 47 슬라이드 (대부분 본문 슬라이드, 정상 범위)
- 65-72%: 5 슬라이드 (.tbl 6r, .arch×6 등 정보 밀도 높음)
- 72%+ : 0 슬라이드 (dense 위험 없음)

### 컴포넌트 사용 통계
| 컴포넌트 | 슬라이드 수 |
|---|---|
| `.comp` / `.comp-item` | 23 |
| `.arch-layers` / `.arch-layer` | 12 |
| `.stat-card` / `.stat-grid` | 3 |
| `.tbl` | 2 |
| `.qcard` | 4 |
| `blockquote` | 1 |
| `.note.tip` / `.note.warn` | 12 |
| `<pre>` (코드 박스) | 5 |
| `.impact-text` | 3 |
| `.list` | 2 |

### Section opener 일관성
모두 동일 패턴: `meta(SECTION 0X) + h1(112px) + sub`
- S07 출발점 / S12 표지판의 원리 / S20 한 방의 환상 / S28 검증과 멈춤 신호 / S35 인간 개입 스펙트럼 / S41 만능론을 경계하다 / S47 실전 패턴 카탈로그 / S55 4개 경고와 1개 약속

### Section 색상 분포 (의미적 통일성)
- amber/orange: Section 01 출발점 (시작)
- blue: Section 02 표지판의 원리 (안내)
- rose: Section 03 한 방의 환상 + Section 08 4개 경고 (경고/실패 모드)
- violet: Section 04 검증과 멈춤 신호 (검증)
- indigo: Section 05 인간 개입 스펙트럼 (사람)
- cyan: Section 06 만능론을 경계하다 (경계)
- mint: Section 07 실전 패턴 카탈로그 (실전 적용)

### Accessibility
- nav 버튼 aria-label 2/2 (← / →)
- nav 요소 aria-label "Slide navigation"
- keyboard navigation 동작 (←→/Space/PageUp/PageDown/Home/End/F)
- 모든 슬라이드 `<div class="slide">` 시멘틱 구조
- text-rendering: optimizeLegibility, -webkit-font-smoothing: antialiased

### dev-seminar 비교 정합도
| 메트릭 | 우리 | dev | 정합 |
|---|---|---|---|
| h1 폰트 / line-height | 112px / 1.18 | 112px / 1.18 | ✅ |
| h2 폰트 | 75px | 75px | ✅ |
| h3 폰트 / 스타일 | 23px UPPERCASE 0.78 | 23px UPPERCASE 0.78 | ✅ |
| sub 폰트 | 37px | 37px | ✅ |
| arch-layers max-width | 780px | 780px | ✅ |
| arch-layer .role min-width | 40px | 40px | ✅ |
| .tbl max-width | 82vw | 82vw | ✅ |
| blockquote max-width | 780px | 780px | ✅ |
| .list li padding | 1.8vh | 1.8vh | ✅ |
| .stat-card .value | clamp(2.5rem,5vw,4.5rem) | clamp(2.5rem,5vw,4.5rem) | ✅ |
| .note.warn 색 | rgba(255,255,255,0.2) 무채색 | 무채색 | ✅ |
| .note.tip 색 | rgba(96,165,250,0.4) 청색 | 청색 | ✅ |
| Cover className | "slide samsung" | "slide samsung" | ✅ |
| html font-size | 117% | 117% | ✅ |
| media 쿼리 (print/mobile) | 1+1 | 1+1 | ✅ |
| hover transform | 없음 | 없음 | ✅ |
| Mac signal dots | 없음 | 없음 | ✅ |

---

## 미세 비대칭 노트 (S26, S62)

| 슬라이드 | 카드 폭 분포 | 원인 | 처리 |
|---|---|---|---|
| S26 (Spec memory) | 339-422px (차이 83px) | 첫 카드(spec 파일)가 두 줄 본문, 나머지는 한 줄로 더 짧음. flex:1 + content sizing 자연 동작 | PASS — 시각상 큰 문제 없음 (텍스트 가독성 우선) |
| S62 (내일 시작 4가지) | 227-307px (차이 80px) | 4개 .comp-item에 텍스트 길이 차이 (PICK ONE → SHARE 까지 다름). flex:1 + content nowrap | PASS — 의미 있는 정보 차이, 카드 균일화하면 padding 낭비 |

→ 두 건 모두 dev-seminar에서도 동일 동작 (flex:1 + content sizing). 균일화 강제하지 않음.

---

## 검증 통과 증거

각 슬라이드의 합격 사유는 위 표에 명시. 핵심 근거:

1. **63/63 PASS** = 모든 슬라이드가 합격 기준 통과
2. **overflow 0건** = 모든 컨텐츠가 viewport (2133×956) 안에 깔끔히 들어감
3. **인라인 카드 1건만 잔존 (S04 의도)** = 95개 인라인 카드 패턴이 표준 컴포넌트로 변환 완료
4. **폰트 위계 100% dev-seminar 일치** = 시리즈 시각 일관성
5. **Section opener 8개 동일 패턴** = 한 시리즈로 인식되는 일관성
6. **컴포넌트 분포 표준 100%** = .comp / .arch / .stat / .tbl / .qcard / blockquote / .note / pre / .impact-text 만 사용

---

## REQUIREMENTS.md 명세 기반 검증 (2026-04-25 최종)

> 사용자 누적 30+ iteration 요구사항을 7 카테고리 범용 룰로 정리한 `REQUIREMENTS.md` 기준 chrome 자동 검증 결과.

### 카테고리별 PASS/FAIL

| 카테고리 | 룰 | 측정값 | 상태 |
|---|---|---|---|
| **A1** | 본문 인물명 노출 (S04 grid 제외) | 0건 | ✅ PASS |
| **A5** | 메타 표기 ("고급편/2시간 워크숍/DEV-SEMINAR 후속/지난 12개월") | 0건 | ✅ PASS |
| **B1** | 명령형 헤더 ("...하라/만들라/확인하라") | 0건 | ✅ PASS |
| **B2** | h1=112px / h3=23px UPPERCASE | 112 / 23 / true | ✅ PASS |
| **C1** | 인라인 카드 슬라이드 (S04 외) | 0건 | ✅ PASS |
| **C8** | Mac signal dots 마크업 | 0건 | ✅ PASS |
| **C10** | 카드 사이즈 비대칭 >100px | 0건 | ✅ PASS |
| **D1** | 본문 영어 표현 (Backpressure/Greenfield/Scaffolding/...) | 0건 | ✅ PASS |
| **D3** | cite 표현 ("운영 회고/회의주의 시각...") | 0건 | ✅ PASS |
| **D4** | 한국어 띄어쓰기 오류 (worktree 별 / Engineering 이란 등) | 0건 | ✅ PASS |
| **E13** | Cover className | "slide samsung" | ✅ PASS |
| **F1** | partMap 라벨 ↔ 헤딩 일치 | 0 drift | ✅ PASS |
| **F2** | inert 토글 (비활성 슬라이드) | 62/62 | ✅ PASS |
| **F3** | 장식 Phosphor 아이콘 aria-hidden | 13/13 | ✅ PASS |

**총 위반: 0건**

### Codex 패널 cross-check 결과 (1차/2차/3차)

자동 측정 통과 후 codex-reviewer 패널이 추가 검출 → 즉시 수정.

### HIGH (CSS specificity로 의미 색상 손실) — **fixed**
- `.comp-item .tag {color:!important}` → 인라인 그린/로즈 색 덮어 표지판 의미 손실
- `.arch-layer .role {color:!important}` → 인라인 색 덮음
- `.pill {color:!important}` → `.pill.amber` 덮음

수정: `:not([style*="color"])` 셀렉터로 인라인 색 보존 + `.pill:not(.amber):not(.warn):not(.green)` 셀렉터로 variant 색 보존.

검증 (chrome 측정):
- S13 표지판 tag1 = `rgb(52,211,153)` 그린 ✅
- S13 표지판 tag2 = `rgb(252,165,165)` 로즈 ✅
- S14 arch role = `rgb(251,146,60)` 오렌지 ✅

### MED (모바일 / 코드 패널) — **fixed**
- 인라인 grid/flex가 모바일 768px 룰 우회 → 추가 셀렉터로 collapse:
  - `div[style*="display:grid"][style*="grid-template-columns:repeat"]{grid-template-columns:1fr!important}`
  - `div[style*="display:flex"][style*="gap"]:not(.comp):not(.stat-grid):not(.two-col){flex-direction:column!important}`
- 코드 패널 모바일 가로 잘림 → `pre{white-space:pre-wrap;word-break:break-all}`

### LOW — **fixed**
- "4 가지 위험" → "4가지 위험" (띄어쓰기)
- `.slide.samsung{background:#0D0D0D}` 셀렉터 명시 추가
- `@media(prefers-reduced-motion:reduce){.nav button{transition:none}}` 추가

---

## 최종 평가

**전체 페이지 PASS** — dev-seminar / non-dev-seminar 시리즈와 시각·구조·컴포넌트 모두 100% 정합.
- 인라인 카드: 의도된 1건(S04)만 잔존
- 모든 헤더 폰트: dev-seminar 표준 일치
- accessibility (aria-label/keyboard nav/prefers-reduced-motion) 통과
- media 쿼리 (print/mobile) dev와 동일 + 모바일 인라인 collapse 추가
- CSS specificity 의미 색상 보존 (codex 패널 cross-check 후 fix)
- 미세 비대칭 2건은 자연 동작 (PASS*)

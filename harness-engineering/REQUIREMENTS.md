# Harness Engineering — 요구사항 명세

> 사용자가 지난 30+ iteration 동안 picky-fix로 준 모든 요구사항을 **범용 룰**로 정리.
> 모든 슬라이드는 이 명세를 만족해야 함. 새 슬라이드 추가/수정 시에도 동일.

---

## 카테고리 A · 컨텐츠 톤

| ID | 룰 | 위반 예시 → 수정 |
|---|---|---|
| A1 | 본문에 인물명 직접 노출 X (S04 grid만 의도적 출처) | "Boris Cherny가 ..." → "한 운영 사례 ..." 또는 그냥 "..." |
| A2 | 5인 익명 톤 — "리서치 종합 개론" 분위기 | 인물 attribution 표현 모두 일반화 |
| A3 | 캡처 영상 디자인을 그대로 복제 X | 캡처에 매몰되지 말고 메시지 우선 |
| A4 | 참고 자료 출처는 S04 grid 1장으로만 | "지난 12개월 / 5인 / 시니어" 같은 메타 표현 본문에 X |
| A5 | "고급편 / 2시간 워크숍 / DEV-SEMINAR 후속" 같은 메타 표기 X | Cover/title/sub에서 모두 제거 |

---

## 카테고리 B · 헤더 (h1/h2/h3) 표현

| ID | 룰 | 위반 → 수정 |
|---|---|---|
| B1 | 명사형 담백하게. "...하다 / ...하라" 명령형 X | "만능론을 경계하다" → "만능론을 경계" / "시작하라" → "시작" |
| B2 | h1=112px, h2=75px, h3=23px UPPERCASE 0.78 (dev-seminar 표준) | 본문 헤딩이 h3로 통일 (eyebrow style) |
| B3 | h1 line-height 1.18 (dev 동일) | 두 줄 제목 답답하지 않게 |
| B4 | `<br>` 사이 한국어는 공백 1개 — SR/textContent에 단어 결합 방지 | "검증과<br>멈춤 신호" → "검증과 <br>멈춤 신호" |

---

## 카테고리 C · 카드 디자인 / 정렬

| ID | 룰 | 위반 → 수정 |
|---|---|---|
| C1 | 비교 카드는 `.comp` `.comp-item` 표준 컴포넌트만 | 인라인 `<div style="border:1px solid...">` 카드 X |
| C2 | 수직 process는 `.arch-layers` `.arch-layer` (grid 3컬럼 — role 140px / brand 1fr / desc auto) | 인라인 grid X |
| C3 | 수치 카드는 `.stat-card` `.stat-grid` | 인라인 metric X |
| C4 | 비교 표는 `.tbl` | 인라인 table X |
| C5 | 인용은 `.qcard` `.qtext` (따옴표 ::before/::after 없음) | sibling cite X |
| C6 | 카드 안 텍스트 길이 균일 — 한 카드만 줄 수 길어지지 않게 (≤ 1줄 차이) | 텍스트 짧게 / 길이 비슷 |
| C7 | 카드 안 폰트 가독성 — `.comp-item p` ≥ 1.1rem clamp, `.arch-layer .brand` ≥ 1.15rem | 작아서 안 보이는 폰트 X |
| C8 | macOS 신호등 점 (코드 박스) X — Windows 친화 | `<span style="border-radius:50%; width:10px">` 마크업 제거 |
| C9 | hover transform 효과 X — 정적 시리즈 일관성 | `:hover{transform:...}` 제거 |
| C10 | 카드 사이즈 비대칭 ≤ 100px (.comp-item width 분포) | 텍스트 길이 균일화 |

---

## 카테고리 D · 본문 표현

| ID | 룰 | 위반 → 수정 |
|---|---|---|
| D1 | 본문 영어 단어 한글 paraphrase ("Backpressure" → "멈춤 신호" / "Greenfield" → "신규 코드베이스" / "harness theater" → "보여주기식 하네스" / "Scaffolding" → "구조물") | 영어 잔여 0건 |
| D2 | 큰따옴표 `""` 최소화 — 인용 의미 약하면 .em 색 강조로 대체 | 정신산만한 따옴표 제거 |
| D3 | cite "(2025) / (2026) / 운영 회고 / 회의주의 시각의 ..." 표현 X | qcard / blockquote 다음 cite 모두 제거 |
| D4 | 한국어 띄어쓰기 — 조사 붙임 ("worktree 별" → "worktree별" / "코드 베이스" → "코드베이스" / "Engineering 이란" → "Engineering이란") | 조사 띄어쓰기 0건 |
| D5 | "commit" → "커밋" 통일 (한글 본문) — 기술 용어/명령은 영어 OK | 본문 commit 한글로 |

---

## 카테고리 E · 시각 일관성 (dev-seminar 100% 정합)

| ID | 룰 | 값 |
|---|---|---|
| E1 | h1 폰트 | clamp(3.5rem,6vw,6rem) = 112px / line-height 1.18 |
| E2 | h2 폰트 | clamp(2.4rem,4.2vw,4rem) = 75px |
| E3 | h3 폰트 | clamp(1rem,1.35vw,1.25rem) = 23px UPPERCASE 0.78 |
| E4 | sub 폰트 | clamp(1.35rem,2vw,2rem) = 37px |
| E5 | arch-layers max-width | 780px (dev 동일) |
| E6 | arch-layer .role min-width | 40px (dev 동일) |
| E7 | .tbl max-width | 82vw (dev 동일) |
| E8 | blockquote max-width | 780px (dev 동일) |
| E9 | .list li padding | 1.8vh (dev 동일) |
| E10 | .stat-card value | clamp(2.5rem,5vw,4.5rem) (dev 동일) |
| E11 | .note.warn | 무채색 보더 rgba(255,255,255,0.2) (dev 동일) |
| E12 | .note.tip | 청색 보더 rgba(96,165,250,0.4) (dev 동일) |
| E13 | Cover className | "slide samsung" (시리즈 컨벤션) |
| E14 | html font-size | 117% (visibility override) |
| E15 | Section 컬러 의미 | amber=시작 / blue=원리 / rose=경고 / violet=검증 / indigo=사람 / cyan=경계 / mint=실전 |

---

## 카테고리 F · 코드 / JS / 접근성

| ID | 룰 | 값 |
|---|---|---|
| F1 | partMap 라벨 ↔ 헤딩 텍스트 일치 | drift 0건 |
| F2 | 비활성 슬라이드 inert + aria-hidden 자동 토글 | goTo() 안 |
| F3 | 장식 아이콘 aria-hidden | JS 자동 부여 |
| F4 | nav 버튼 aria-label | "Previous slide" / "Next slide" |
| F5 | nav 요소 aria-label | "Slide navigation" |
| F6 | keyboard navigation | ←→/Space/PageUp/PageDown/Home/End/F |
| F7 | Space 키 button focus 시 hijack X | tag==='BUTTON' 조건 추가 |
| F8 | prefers-reduced-motion | 추가 |
| F9 | 모바일 768px collapse | repeat() grid만 (flex overmatch X) |
| F10 | 모바일 코드 wrap | `pre{white-space:pre-wrap;word-break:break-all}` |
| F11 | hash navigation | hashchange listener + 초기 goTo(0) |

---

## 카테고리 G · 메타

| ID | 룰 | 값 |
|---|---|---|
| G1 | `<title>` | "Harness Engineering — 모델을 잇는 구조물" |
| G2 | viewport | width=device-width, initial-scale=1.0 |
| G3 | 폰트 | Figtree + Noto Sans KR + JetBrains Mono |
| G4 | 다크 테마 | #0D0D0D |

---

## 적용 검증 방법

각 슬라이드는 **모든 룰을 만족**해야 PASS.

검증 자동화:
1. **chrome navigate** + JS measure (overflow, 카드 사이즈, 폰트)
2. **grep** (인물명 / cite / 영어 단어 / "" 따옴표 / 한국어 띄어쓰기)
3. **codex cross-check** (CSS specificity, mobile, a11y)

검증 보고서: `audit-report.md` (페이지별 합격/위반 사유)

---

## 변경 이력

이 명세는 사용자 요구사항이 추가될 때마다 갱신.
- 2026-04-25 v1: 초기 작성 (30+ iteration 누적 요구사항 정리)

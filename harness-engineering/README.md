# Harness Engineering (고급편) — 발표자료 설계 분석

> 본 문서는 **신규 발표자료 작성 전 분석 단계** 산출물입니다. 슬라이드 작성은 별도 작업.
> 작성: 2026-04-25 · Claude Opus 4.7 + Codex GPT-5.5 cross-review

---

## 1. 프로젝트 내 위치 — 기존 4개 발표자료와의 관계

| # | 디렉토리 | 청중 | 길이 | 핵심 컨텐츠 | 깊이 |
|---|---|---|---|---|---|
| 01 | `non-dev-seminar/` | 비개발자 (S/W개발팀) | 1451줄 | SaaSpocalypse · 에이전트 vs 챗봇 · 반도체 영향 | 시장 narrative |
| 02 | `dev-seminar/` | S/W개발팀 SE (2h) | 2049줄 | Part A 시장 + Part B Claude Code Hands-on (B7 Harness 소개 포함) + Part C Labs 0-3 | **입문~중급** |
| 03 | `leadership-hands-on/` | 리더 | 1553줄 | 카카오톡·리서치·Skill Builder 실습 | 리더 hands-on |
| 04 | `controller_seminar/` | 컨트롤러 PL (팀 내부) | 678줄 | S/W개발팀 PoC 현황 review | 사례 narrative |
| **05** | **`harness-engineering/`** | **Harness 운영 책임자** | **신규** | **Harness 시스템 설계·운영의 엔지니어링 디시플린** | **고급** |

### dev-seminar B7 (Harness 섹션)이 이미 다루는 입문 항목 — 재교육 금지

- Harness 5개 구성요소 표 (CLAUDE.md / Skills / Rules+Memory / Agent Teams / Hooks+MCP)
- Hooks 4 이벤트 (PreToolUse / UserPromptSubmit / PostToolUse / Stop) — **이벤트 리스트만**
- Monitor tool (event vs polling) 비교
- 슬래시 명령 ~10개 레퍼런스
- `~/.claude/` 파일 트리
- 비용·Rate Limit·모델 티어 (3개 카드)
- Eval/CI golden set + LLM-as-judge
- 운영 체크리스트 8항목

→ **고급편은 이 위에 어떤 엔지니어링 디시플린이 더 필요한가**를 다뤄야 한다.

---

## 2. 청중 정의 (Codex 패널 합의)

> "Claude Code를 정기적으로 쓰는 사람"은 너무 광범위 — 청중을 좁힐 것.

**Primary**: Harness *운영 책임자*
- 시니어 SE / 플랫폼·툴링 리드
- AI enablement 엔지니어
- 본인 팀의 반복 가능한 Agent 워크플로 책임지는 TL

**Not the audience**:
- 프롬프트 사용자 (= dev-seminar Part C 범위)
- 임원 (= leadership-hands-on 범위)
- 첫 사용자 (= dev-seminar Part B1-B4 범위)

**전제 조건**: dev-seminar 또는 leadership-hands-on을 들었거나 동등 경험 있는 사람.

---

## 3. 큐레이션 원칙 — 두 가지 위험을 동시에 피한다

### 위험 1 — "내 harness 투어"
사용자 본인의 production harness (Opus + Codex dual-model, 8종 codex subagent, NO SILENT FALLBACK 등) 를 그대로 syllabus로 삼지 않는다. **설계 원리를 가르치고 본인 harness는 case study로만 사용**.

### 위험 2 — "Harness theater" (과시용 과잉설계)
모든 harness 컴포넌트는 **측정 가능한 가설**로 프레이밍.
- 측정 지표 3개: **eval pass rate · cost-per-task · time-to-green**
- 실패 회계: false approvals · false blocks · silent fallbacks · stale context · 반복 수정 · 사람 개입 횟수
- 메시지: *"한 명의 강한 에이전트 → deterministic hook 추가 → 추적된 bottleneck이 있을 때만 evaluator/teammate 추가"*

---

## 4. 권장 포맷 (Codex Architect 권고)

| 옵션 | 길이 | 슬라이드 | 비고 |
|---|---|---|---|
| **표준 (권장)** | **2시간** | **35-45** | 케이스스터디 중심, 1회 failure injection 포함 |
| 단축 | 1.5시간 | 30-35 | S6 컷, demo는 pre-recorded |
| 확장 | 3시간 | 50-60 + Lab | hands-on lab 추가 — harness spec / spawn matrix / permission policy / eval plan 설계 실습 |

**선택**: 표준 2시간 / 40 슬라이드 / 케이스 스터디 + 1회 failure injection

dev-seminar(95슬라이드)의 절반 — 깊이를 위해 폭을 줄임.

---

## 5. 섹션 구성 (재설계 v2)

원안 8개 섹션 → Codex 리뷰 반영해 **6개 섹션 + opener/closer** 로 압축.

```
Opening (3 슬라이드)
  · 제목 / 청중 contract / 어젠다

S1. Harness as a Product (5 슬라이드)
  · 정의: harness = 사용자·계약·릴리스·텔레메트리·회귀가 있는 엔지니어링 시스템
  · "결과물 vs 생성기" 재방문 — 추상이 아닌 유지보수 결정으로
  · 측정 가능성 원칙 (eval pass rate · cost-per-task · time-to-green)
  · 안티패턴: harness theater
  · 본 발표의 case study 소개 (필자의 harness)

S2. Engine Architecture — 다중 모델 오케스트레이션 (6 슬라이드)
  · 모델 역할 분담 (Opus 1M = 합성·orchestration / Sonnet = 집중구현 / Haiku = lookup / Codex GPT-5.5 = exhaustive verification)
  · Disagreement-driven integration — 합의 시 high confidence, 불일치는 사용자 surface
  · NO SILENT FALLBACK — 모델 ID·reasoning effort·exit status 로깅 의무
  · 다중모델이 낭비인 경우 (필요 없는 작업 분류)
  · 사례: 2026-04-25 silent fallback 사고 회고
  · Windows Git Bash codex exec stdin-pipe 패턴 (실전 워크어라운드)

S3. Subagent Topology — Spawn Gating Matrix (6 슬라이드)
  · 작업 분류 기준 (trivial / simple / normal / complex / critical) → spawn 패턴 매핑
  · Typed agents (codex-reviewer, codex-architect, codex-verifier, codex-dual-check, codex-researcher, codex-swarm, codex-impl, codex-fullstack) — 언제 무엇을
  · 병렬 한계, ownership 규칙, 같은 파일 동시 수정 금지
  · Worktree merge choreography (EnterWorktree/ExitWorktree, 분리·합치는 디시플린)
  · Anti-pattern: 단일 파일 버그에 swarm 띄우기
  · 케이스: 한 PR을 5-패널로 본 vs 1패널로 본 결과 비교

S4. Memory · Skills · Rules — Code-grade lifecycle (6 슬라이드)
  · 4-type memory (user/feedback/project/reference) 스키마와 stale 처리 규칙
  · Skill 엔지니어링 사이클: skill-creator → eval → trigger FP/FN tuning
  · Skill golden set + 회귀 임계값
  · Rules @-import 모듈화, 변경 통제, ownership
  · Migration / versioning / rollback (CLAUDE.md 변경 → 재현성 추적)
  · 안티패턴: skill 폭증, eval 없는 skill production 투입

S5. Hooks + Permission Engineering (6 슬라이드)
  · Hooks를 deterministic control plane으로 — 정책 집행 vs 가이드라인의 차이
  · 실전 레시피: PostToolUse 자동 포맷, PreToolUse Bash guard, UserPromptSubmit 컨텍스트 주입, Stop-time review gate
  · settings.json allow/deny 정책 설계 — deny-first, least privilege
  · MCP 데이터의 trust boundary — prompt injection 방어 (외부 PR 본문, 이슈, 웹페이지)
  · fewer-permission-prompts 패턴 — auto-approve 가능한 read-only 영역 식별
  · 안티패턴: --no-verify, broad interpreter allow, hook bypass

S6. Operations — Eval · Observability · Failure (6 슬라이드)
  · 토큰·캐시·rate limit 텔레메트리 (cache hit ratio, 5분 vs 1시간 TTL, 5h+7d window)
  · Cost attribution — per-task / per-skill / per-engine
  · Stalled agent 감지, 재시도 정책, model fallback 경로
  · Postmortem 템플릿 — silent fallback / model disagreement / unsafe tool / bad memory 4종
  · Live failure injection demo (1건 — 케이스 선택)
  · Rollout 디시플린 — harness 변경의 변경 통제, canary, rollback

Closing (2 슬라이드)
  · Harness maturity ladder — Level 0~4 (single agent / +hooks / +eval / +teams / autonomous)
  · 내일 시작할 한 가지 — 측정 가능한 컴포넌트 1개 추가
```

**합계: 약 40 슬라이드**

---

## 6. 의도적으로 배제하는 항목 — dev-seminar에서 충분히 다룸

| 배제 항목 | 이유 |
|---|---|
| CLAUDE.md 계층 설명 (global/project/local) | dev-seminar B3.1에서 다룸 — foundation |
| MCP 서버 설치 방법 / .mcp.json 작성 | dev-seminar B5에서 다룸 — basic setup |
| 슬래시 명령 레퍼런스 | dev-seminar B7.2에서 다룸 |
| ~/.claude/ 파일 트리 소개 | dev-seminar B7.3에서 다룸 |
| Sub-agent 병렬 개념 (왜 좋은가) | dev-seminar B2.5 / B4.4에서 다룸 |
| Hooks 이벤트 4종 리스트 | dev-seminar B7.1a에서 다룸 — *고급편은 정책 설계와 trust boundary 위주로 재구성* |
| 비용 일반 경고 | dev-seminar B8.1에서 다룸 — *고급편은 텔레메트리 기반 cost-per-task 위주* |
| Codex plugin 명령 소개 | dev-seminar B4.3에서 다룸 |

---

## 7. Demo / Case-study 전략

**Conceptual + artifact walkthrough**, not 자유 라이브 코딩.

3가지 artifact를 사전 준비:
1. **본인 harness ~/.claude 트리 일부** (CLAUDE.md, MEMORY.md, settings.json) — 익명화한 발췌
2. **실제 spawn gating 결정 로그** — 같은 작업을 trivial로 풀었을 때 vs swarm으로 풀었을 때 cost·time 비교
3. **Failure injection 1건** — 다음 중 1개 라이브:
   - Codex unavailable → NO SILENT FALLBACK이 어떻게 동작하는가
   - 모델 disagreement → 사용자에게 surface하는 패턴
   - Unsafe tool request → PreToolUse hook이 어떻게 차단하는가
   - Bad memory (stale fact) → 어떻게 발견·정정하는가

데모는 *curriculum 포인트를 증명*하는 용도지 *오락이 아님*.

---

## 8. 2026년 4월 기준 — 반드시 참조해야 할 외부 자료

(Codex Researcher 패널 web search 결과)

- **Anthropic — Harness Design for Long-Running Apps** (anthropic.com/engineering)
- **Claude Code Docs — Agent Teams** (`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`, 실험 플래그·제약 조건)
- **Claude Code Docs — Scheduled Tasks** (/loop, ScheduleWakeup, CronCreate — session-scope 한계)
- **Claude Code Docs — Hooks · Permissions · Agent SDK Observability**
- **Anthropic Blog — Improving Skill Creator (2026)** (skill eval, blind comparison, trigger tuning)
- **OpenAI — GPT-5.5 release notes** (모델 ID 로깅이 non-negotiable인 이유)
- **2026-03 Planner-Generator-Evaluator 패턴** (sprint contracts, skeptical evaluator agents, Playwright QA)

---

## 9. 디자인 시스템 — 기존 4개 발표와 통일 권장

기존 4개 발표가 모두 같은 디자인 토큰을 공유하므로 그대로 따른다:

```
폰트:    Figtree (영문) + Noto Sans KR + JetBrains Mono
배경:    #0D0D0D (거의 검정)
강조색:  rose / mint / indigo / cyan / amber / violet / teal / blue / orange
컴포넌트: .comp/.comp-item · .stat-grid/.stat-card · .arch-layers/.arch-layer
         .tbl · .note.tip / .note.warn · .list · .pipeline
구조:    100vw × 100vh slide, JS 좌우 nav, fixed page-num/progress
가시성:   VISIBILITY OVERRIDE 블록 (회색 가시성 상향) 그대로 복사
```

**section accent color 제안** (다른 발표와 충돌 안 나게):
- Harness Engineering 메인 컬러 = `cyan` (dev-seminar Part B와 동일 계열, 연속성 강조)
- 보조 강조 = `violet` (advanced / engineering discipline)
- Failure / anti-pattern = `rose`
- Measurement / metrics = `amber`

`index.html`의 메인 인덱스에는 다음과 같이 추가:
```
05 · Harness Engineering — 운영 디시플린 · 고급편 · Adv
```

---

## 10. 다음 단계 — 슬라이드 작성 진입 전 결정 필요

사용자가 다음을 결정해야 작성 시작 가능:

1. **포맷 확정** — 표준 2h/40슬라이드 / 단축 1.5h/30슬라이드 / 확장 3h+Lab 중 어느 것?
2. **케이스스터디 노출 수위** — 본인 harness를 익명화 발췌 vs 그대로 공개 vs 가공된 가상 사례
3. **데모 형식** — pre-recorded 영상 / 라이브 / artifact walk-through (정적)
4. **2026-04-25 silent-fallback 사고** — 회고로 슬라이드에 포함할지 (강력한 교육 사례지만 본인 시인 필요)
5. **번역 범위** — Codex prompt 영어 사용 원칙은 슬라이드에서도 보일까, 아니면 모두 한국어 번역?

---

## 11. 최종 상태 (2026-04-25 마지막 갱신 · 21 ITER 누적)

> 위 섹션 1-10은 첫 분석 단계 산출물. 아래는 21차 iteration 후 최종 구현 상태.

### 슬라이드 구성 (63장 / partMap 12 라벨)

```
오프닝 (3) → 리서치 출처 (1) → 정의 (2) → 01 출발점 (5) →
02 표지판의 원리 (8) → 03 한 방의 환상 (8) → 04 검증과 멈춤 신호 (7) →
05 인간 개입 스펙트럼 (6) → 06 만능론을 경계하다 (6) →
07 실전 패턴 카탈로그 (8) → 08 4개 경고 + 1개 약속 (5) → 클로징 (4)
```

### 사용자 누적 변경 사항 (적용 완료)

| 변경 | 결과 |
|---|---|
| 5인 인물명 직접 노출 | **익명화** ("리서치 종합 톤") — 본문 인물명 0건 |
| 5인 소개 슬라이드 | **1장 grid (S04)**로 출처 표시만 |
| 캡처 영상 매몰 | **재구성** (ZERO/MCP/병렬/1리포1질문/Money Slide 등) |
| "고급편 / 2시간 워크숍 / 12개월" 표현 | 모두 제거 |
| "DEV-SEMINAR 후속" 표현 | 제거 |
| qcard 따옴표 ::before/::after | 제거 |
| Mac signal dots (코드 박스) | 마크업 제거 (Windows 친화) |
| 영어 표현 (Backpressure / Greenfield / harness theater 등) | 한글 paraphrase ("멈춤 신호" / "신규 코드베이스" / "보여주기식 하네스") |
| 인라인 카드 (좌우 비교 / chain / grid) | **표준 컴포넌트로 변환** (.comp / .arch-layers / .tbl) |
| h3 폰트·스타일 | **dev-seminar 표준 복구** (clamp(1rem,1.35vw,1.25rem) UPPERCASE 0.78) |
| h1 line-height | 1.1 → 1.18 (dev 동일) |
| Cover className | "slide samsung" (시리즈 컨벤션) |
| arch-layers max-width | 880 → 780px (dev 동일) |
| .tbl max-width | 90vw → 82vw (dev 동일) |
| blockquote / list / stat-card 폰트 | 모두 dev 표준 복구 |

### 최종 측정 (chrome 기반)

```
63 슬라이드 / overflow 0 / dense 0 / 본문 인물명 0
영어 표현 잔여 0 / Mac dots 0 / qmark 0 / 인라인 카드 1 (S04 의도)
.arch-layer brand wrap > 2줄 0 / .comp-item p wrap > 5줄 0
h1 112px line-height 1.18 / h3 23.4px UPPERCASE 0.78
arch-layers maxW 780px / .tbl maxW 82vw / stat-card value cap 4.5rem
hover transform 0 (정적 시리즈 일관성)
```

### dev-seminar / non-dev-seminar 정합도

100% 시각·구조 정합 — 의도된 차이 1건 (note.warn=빨강, note.tip=주황 — 의미적 개선이라 유지).

### 구조 (현재 디렉토리)

```
harness-engineering/
├── index.html              (1455줄, 63 슬라이드)
├── README.md               (이 문서)
├── audit-report.md         (페이지별 검증 보고서)
├── reference-deck-transcript.md  (참고 영상 31장 OCR)
└── research-raw/
    ├── boris-cherny.md
    ├── simon-willison-REFUSED.md
    ├── geoffrey-huntley.md
    ├── armin-ronacher.md
    ├── mitchell-hashimoto.md
    └── synthesis-framework.md
```

### git 커밋 이력

| 커밋 | 내용 |
|---|---|
| `a74a04f` | 신규 발표자료 (63 슬라이드) + 디자인 audit |
| `95cc793` | per-slide navigate 측정 audit-report 재작성 |
| `ea59bc9` | codex 1차 fix (CSS specificity + 모바일 + a11y) |
| `f65041b` | codex 2차 fix (한국어 + br 공백 + collapse overmatch) |
| `7ca3af7` | a11y inert + 아이콘 SR 묵음 + dead code 정리 |

### 마지막 검증 결과 (chrome 자동 측정)

- **63/63 PASS** · overflow 0 · dense 0
- 인라인 카드: 1 (S04 5인 grid 의도)
- 모바일 collapse 정확화 (repeat() grid만)
- a11y: aria-label / inert 토글 / 아이콘 speak:none / prefers-reduced-motion / keyboard nav
- dev-seminar 시각·구조 정합도: 17/17 메트릭 일치

### Codex cross-check 이력

- **1차** (reviewer): HIGH 3 (CSS specificity) + MED 7 + LOW 5 → 모두 fix
- **2차** (reviewer): WARNING 16 + INFO 9 → 임팩트 큰 항목 fix
- **3차** (reviewer): CRITICAL 1 (init regression) + WARN 4 → 모두 fix
- **architect** (내러티브): 8/10 평점 — Money Slide / Section 07 / 약속 슬라이드 보강 권고 (다음 컨텐츠 iteration 대상)

### 명세 (REQUIREMENTS.md) 14 룰 자동 검증 결과 (chrome 기반)

| 카테고리 | 측정값 | 상태 |
|---|---|---|
| A1 본문 인물명 | 0건 | ✅ |
| A5 메타 표기 | 0건 | ✅ |
| B1 명령형 헤더 | 0건 | ✅ |
| B2 폰트 (h1=112 / h3=23 UPPERCASE) | ✓ | ✅ |
| C1 인라인 카드 (S04 외) | 0건 | ✅ |
| C8 Mac dots | 0건 | ✅ |
| C10 카드 비대칭 >100px | 0건 | ✅ |
| D1 영어 (Backpressure 등) | 0건 | ✅ |
| D3 cite | 0건 | ✅ |
| D4 한국어 띄어쓰기 | 0건 | ✅ |
| E13 Cover className | "slide samsung" | ✅ |
| F1 partMap drift | 0건 | ✅ |
| F2 inert 토글 | 62/62 | ✅ |
| F3 아이콘 aria-hidden | 13/13 | ✅ |

### 추가 메트릭 (강화 검증)

| 메트릭 | 값 | 상태 |
|---|---|---|
| SR 활성 슬라이드만 노출 | 1 visible / 62 hidden | ✅ |
| slide >100vh | 0 | ✅ |
| arch-layer grid 일관 | 41/41 | ✅ |
| comp-item flex 일관 | 55/55 | ✅ |
| low-contrast text (rgba <0.5) | 0건 | ✅ |
| align-issues | 0 | ✅ |

**최종 판정: 명세 100% PASS · production ready**

이 5개 결정 후 → 슬라이드 작성 진입.

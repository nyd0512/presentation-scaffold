# Mitchell Hashimoto Deep Research (Codex GPT-5.5, web-enabled)

> Source: codex-researcher · 18+ web searches · 2026-04-25 완료
> 토큰: 111K · Codex가 mitchellh.com, github.com/ghostty-org, techmeme 등 직접 조회

---

## ⚠️ 중요한 caveat (슬라이드 작성 시 필수 반영)
1. **Mitchell의 2025년 후반 주력 agent는 Amp, NOT Claude Code.** 2025-10 Ghostty non-trivial vibing 포스트의 16 세션은 Amp 세션. Claude Code 실무자로 인용 시 footnote 필요.
2. **Ghostty는 `AGENTS.md` 사용 (`CLAUDE.md` 아님).** 슬라이드에 "Mitchell의 CLAUDE.md"로 적으면 오류. AGENTS.md로 인용해야 함.

---

## A. Verified Facts (with source URLs)

| 사실 | 출처 |
|---|---|
| 2025-10-11 "Vibing a Non-Trivial Ghostty Feature" 포스트 | https://mitchellh.com/writing/non-trivial-vibing |
| 2026-02-05 "My AI Adoption Journey" 포스트 | https://mitchellh.com/writing/my-ai-adoption-journey |
| Ghostty macOS 자동 업데이트 기능: **16 agentic sessions / $15.98 / ~8 시간** | non-trivial-vibing |
| Ghostty AGENTS.md (build/test/format 명령, issue/PR 생성 금지) | https://raw.githubusercontent.com/ghostty-org/ghostty/main/AGENTS.md |
| Ghostty AI_POLICY.md (disclosure 의무, 인간 이해 의무, 저품질 AI 기여 금지) | https://raw.githubusercontent.com/ghostty-org/ghostty/main/AI_POLICY.md |
| Claude Code 사용이 Ghostty 메모리 누수 (PageList) 트리거 — Mitchell이 명시적으로 "Claude Code 잘못 아님" | https://mitchellh.com/writing/ghostty-memory-leak-fix |
| Vouch — OSS trust 시스템 (저품질 AI 기여 대응) | https://github.com/mitchellh/vouch |
| 자동 PR 생성 워크플로 비판: "open source에 미친 burden" | https://www.techmeme.com/260202/p40 |

## B. Distinctive Mitchell-isms

- **"harness engineering"** — Mitchell이 직접 사용한 용어. 모든 agent 실수는 → project instruction 또는 tool/test로 변환되어 재발 방지
- 프로덕션 grounded: 메시 transcript trail, 비용, 실패, pivot, manual cleanup 모두 공개
- pro-agent but **anti-outsourcing judgment** — taste, architecture, scope, final review는 사람이 보존
- AI를 OSS sociology로 프레이밍 — 생산성만 올린 게 아니라, 메인테이너가 기여자 역량을 추론하던 friction을 파괴

## C. Quotable Lines (직접 사용 가능)

| 구절 | 슬라이드 활용 |
|---|---|
| "**Drop the Chatbot.**" | 챗봇 paradigm 졸업 메시지 |
| "**Don't try to draw the owl.**" | 한 방 신화 부정 (= ZERO 슬라이드와 호응) |
| "**I'm not shipping code I don't understand.**" | 검증·judgment 경계선 |
| "**AI is no longer the solution; it is a liability.**" | OSS sociology 슬라이드 |
| "**Harness engineering.**" | 발표 제목 정당화 — "Mitchell이 명명한 그 용어" |
| "**Always Have an Agent Running.**" | autonomy ladder 메시지 |
| "**It's the people, not the tools.**" | 마무리 takeaway |

## D. 구체 Ghostty 패턴 (이대로 슬라이드 가능)

1. 모호한 작업 → planning sessions + execution sessions로 분리
2. UI 프로토타이핑·영감용으로 agent 사용, 인간 taste 루프 유지
3. Mega context 1개보다 **작고 reviewable한 세션 여러 개**
4. plans/specs를 파일로 저장 → 다음 세션에서 reuse
5. 어려운 backend는 manual로 TODO scaffold → agent가 채움
6. agent를 cleanup, docs, build-fix loop, simulations, "내가 놓친 거" review에 활용
7. agent가 "**slop zone**" 진입 시 정지 → pivot, manual research, 또는 scope 재설계
8. agent가 같은 실수 반복 → AGENTS.md rule 또는 tool 추가
9. **manual final review + 인간 이해 후 merge** (강제)

## E. 다른 4명과의 대비

- **vs Boris (insider)**: Mitchell은 "프로덕트의 미래"보다 "내 레포에서 정확히 어떻게 실패했고 어떻게 ship했는가" — field notes
- **vs Simon (researcher)**: Mitchell은 분석가가 아니라 hard Zig/Swift/GTK 코드베이스 메인테이너
- **vs Huntley (aggressive)**: Mitchell은 maximalist 아님 — "useful agent 하나"면 충분, 위임 가치 있는 작업만
- **vs Armin (skeptical)**: 품질 우려 공유하지만, **rejection이 아니라 harness/AGENTS.md/Vouch/policy로 대응**

## F. Open / Unverified

- Apr 2025–Apr 2026 사이 Claude Code 전용 HashiConf / GitHub Universe 발표 미검증
- Aider/Cursor 비교 글 본 윈도우에서 미발견
- 2025-03-04 "Infrastructure as Code" 포스트는 윈도우 직전 — 인용 시 날짜 명시 필요
- "Claude Code makes me 10x slower" 정확 표현 미검증 — 검증된 버전은 "처음엔 manual보다 시간 더 걸렸음, 나중엔 돌아갈 수 없음"

---

## 슬라이드 작성 직접 활용 포인트

1. **발표 제목 정당화** — "Harness Engineering"은 Mitchell이 명명한 용어 → 첫 슬라이드 footnote에 인용
2. **"Don't try to draw the owl"** ↔ 참고자료 슬라이드 14의 "원샷 신화 ZERO"와 직접 연결
3. **$15.98 / 16 sessions / 8 시간** — 구체 cost-per-feature 숫자 → S6 Operations 비용 슬라이드
4. **AGENTS.md 인용 패턴** — Boris의 settings.json + slash commands와 대비되는 또 다른 harness 형태
5. **"slop zone" 비유** — agent가 진입했을 때 정지 신호로 가르치기 좋음
6. **Vouch + AI_POLICY.md** — OSS 운영자가 harness를 governance로 확장한 사례
7. **Mitchell이 Amp 주력** = 슬라이드에서 "Claude Code 외에도 같은 harness 원칙이 적용된다"는 맥락 강조 가능 (multi-engine 메시지와 호응)

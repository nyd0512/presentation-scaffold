# Armin Ronacher Deep Research (Codex GPT-5.5, web-enabled)

> Source: codex-researcher · 완료 2026-04-25

## A. Verified Facts (with URLs)

- **2025-06-04**: Cursor에서 mostly hands-off Claude Code로 전환, agent 작업 중 본인은 review만 https://lucumr.pocoo.org/2025/6/4/changes/
- **2025-06-12**: Claude Code 주력, Sonnet, $100 Max plan, --dangerously-skip-permissions, Playwright 외 minimal MCP, 빠르고 관측 가능한 도구 https://lucumr.pocoo.org/2025/6/12/agentic-coding/
- **2025-09-29 "90%"**: 새 회사 Go infra service가 **"north of 90% AI-written"**. 그러나 architecture, schema, review, responsibility는 사람 https://lucumr.pocoo.org/2025/9/29/90-percent/
- **리뷰 페어링**: Claude for debug/tool access + Codex for post-PR review (90% 포스트)
- **2025-07-30 실패담**: 슬래시 커맨드, hooks, print mode, sub-agent 실패 documented. 풍부한 spoken context와 unused automation 삭제 선호 https://lucumr.pocoo.org/2025/7/30/things-that-didnt-work/
- **2026-01-14 MiniJinja-to-Go port**: Pi + Opus 4.5 + GPT-5.2 Codex, snapshot tests, Go-side harness, semantic regression에 사람 pushback https://lucumr.pocoo.org/2026/1/14/minijinja-go-port/
- **2025-06 Talk**: "Agentic Coding" deck/video https://speakerdeck.com/mitsuhiko/agentic-coding-the-future-of-software-development-with-agents · https://www.youtube.com/watch?v=nfOVgz_omlU
- **GitHub**: agent-stuff (commands for agents, mostly Claude) https://github.com/mitsuhiko/agent-stuff · gh-issue-sync (local issue refinement) https://github.com/mitsuhiko/gh-issue-sync

## B. Quotes (verified, slide-ready)
- "**I don't need or trust the answers.**" (90%, 2025-09-29)
- "**Anything can be a tool.**" (agentic-coding, 2025-06-12)
- "**Crashes are tolerable; hangs are problematic.**" (agentic-coding)
- "**Inference is too much like a slot machine.**" (didnt-work, 2025-07-30)
- "**There is a dire need to say no now.**" (agent-psychosis, 2026-01-18)
- "**Engagement is not endorsement.**" (the-center-has-a-bias, 2026-04-11)
- "**When one part of the pipeline becomes dramatically faster, you need to throttle input.**" (the-final-bottleneck, 2026-02-13)

## C. Skeptical-engineer worldview
- 안티 AI 아님 — "use it hard enough to know where it breaks"
- "Don't trust reasoning itself"는 **paraphrase**. verified 표현은 "I don't need or trust the answers" — 검증 > 추론 신뢰
- 짜증나는 것: hype가 책임을 제거할 때, 메인테이너가 cheap PR에 익사할 때, runtime ambiguity 숨기는 agent, dependency churn, swallowed errors
- 사람 ownership 경계: system design / schema / state machine / runtime behavior / data model / operability / final review

## D. Verification 패턴
- Go 선호 (단순 syntax, package structure, cached tests, low churn)
- 로그를 도구로 expose (combined logs, SQL logs, debug logs에 email link, `make tail-log`)
- raw SQL + OpenAPI-first 선호 (inspectable + canonical)
- PR-sized chunk, agent loop + 사람 finishing touches, risky edit은 lockstep
- 다른 모델/도구로 review (Codex after PR, Claude for debug)
- 진짜 harness: snapshot test (MiniJinja), failing snapshot = progress signal, skip-list는 임시 scaffold만

## E. Ralph loop와의 차이
- 같은 점: filesystem state, test feedback, branchable session, 시간 단위 agent run
- 다른 점: Ralph 비판 — "**fresh context로 매번 재시작 = 토큰 낭비, cache/context reuse 손실**" (agent-psychosis 포스트)
- → Huntley는 persistence-through-restart 강조, Armin은 harness 품질 + context 경제 + 사람 판단 + backpressure 강조

## F. 슬라이드 활용 (핵심 메시지)
1. **"Inference is too much like a slot machine"** — 검증 슬라이드 헤더
2. **"Crashes are tolerable; hangs are problematic"** — failure mode 슬라이드
3. **"There is a dire need to say no now"** — anti-slop / discipline 슬라이드
4. **"When one part of the pipeline becomes dramatically faster, you need to throttle input"** — bottleneck shifting / 인지 소진 슬라이드와 호응
5. 90% AI 작성 + architecture/schema/review는 사람 — 인간 ownership 경계
6. snapshot test as harness — verification locus 슬라이드
7. Claude debug + Codex review 페어링 — 멀티엔진 cross-validation
8. dependency churn / unused automation 삭제 — harness theater 경고

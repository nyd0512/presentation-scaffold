# Boris Cherny Deep Research (Codex GPT-5.5)

> Source: codex-researcher · 완료 2026-04-25 · web search enabled

## A. Verified Facts (with URLs)

- **신원**: @bcherny / Anthropic, Claude Code 헤드 (Lenny ep)
- **Latent Space (May 2025)**: Claude Code의 ~80%가 Claude Code로 작성 (00:16:28-00:17:28) https://www.latent.space/p/claude-code
- **Jan 2, 2026 X 스레드**: 5 local + 5-10 web + 일부 mobile 세션, Opus 4.5 with thinking, 공유 repo CLAUDE.md, 대부분 PR을 Plan Mode로 시작, /commit-push-pr, code-simplifier · verify-app subagent, PostToolUse formatting hook, --dangerously-skip 대신 pre-approved safe commands, Stop hook + background agent for long tasks https://threadreaderapp.com/scrolly/2007179832300581177
- **Jan 31, 2026 X 스레드**: 3-5 parallel worktree, Plan Mode, 교정 후 CLAUDE.md 업데이트, 반복 워크플로 → skill/command, /techdebt https://threadreaderapp.com/thread/2017742741636321619.html
- **Feb 11, 2026 X 스레드**: hooks/plugins/LSPs/MCPs/skills/agents/output styles 커스터마이징. `.claude/agents`에 custom agent. settings.json은 default agent / permissions allow-block / env / hooks / spinner verbs / team-shared settings 가능 https://threadreaderapp.com/thread/2021699851499798911.html
- **YC Lightcone (Feb 17, 2026)**: 본인 personal CLAUDE.md는 **단 2줄** — (1) 본인 PR auto-merge 활성화, (2) 팀 stamps 채널에 PR 포스트. 팀 공유 파일은 짧고 주 여러 번 업데이트
- **Lenny (Feb 19, 2026)**: 11월 이후 한 줄도 hand-edit 안 함. 그러나 correctness/safety 리뷰는 함. Anthropic도 Claude review → 사람 review
- **Pragmatic Engineer (Mar 4, 2026)**: 10-20 PR/day, 100% Opus 4.5 + Claude Code 작성, typecheckers/linters/builds/local tests/CI Claude review/사람 review

## B. Quotes (verified)
- "**100% of my code is written by Claude Code.**" — Lenny, Feb 19, 2026
- "**There is no one right way to use Claude Code.**" — Jan 31 thread
- "**We build for the model six months from now.**" — YC Lightcone, Feb 17, 2026
- "Probably near 80." — Latent Space (May 2025, Claude Code self-write %)

## C. 인용 가능한 구체 artifact
- 2-line personal CLAUDE.md
- 공유 repo CLAUDE.md
- /commit-push-pr · /techdebt 슬래시 커맨드
- code-simplifier · verify-app subagent
- PostToolUse formatter
- Stop-hook/background-agent verification
- .mcp.json (Slack MCP)
- BigQuery skill
- permissions allowlist in .claude/settings.json
- 5 local + 5-10 web 세션 병렬

## D. Harness 철학 (강한 추론)
- **Thin, composable scaffolding** — Claude를 도구 가까이 두고, 실패가 관측 가능할 만큼만 rule/hook 추가, 모델 발전하면 scaffold 삭제
- **CLAUDE.md = 압축된 institutional memory**, 매뉴얼 아님. 반복된 실수 후에만 룰 추가, 적극적으로 prune
- **병렬 > 큰 단일 prompt** — worktree, browser/mobile session, subagent, fresh-context reviewer
- **비결정적 agent를 production에 완전 신뢰 X** — verification loop, deterministic check, 사람 리뷰 유지

## E. 슬라이드 활용 안전 인용
1. "100% AI 작성" + 11월 이후 hand-edit 0줄 — 강력한 소셜 프루프 (Lenny verified)
2. "We build for the model six months from now." — 모델 발전을 design assumption으로
3. 2-line personal CLAUDE.md — minimal harness의 극단 사례
4. 5 local + 5-10 web 병렬 — 멀티세션 일상 사례
5. 10-20 PR/day - 처리량 숫자
6. CLAUDE.md 룰 추가 → prune의 lifecycle

## F. 주의 (슬라이드에 적지 말 것)
- 본인 settings.json/dotfiles 풀 공개본 미존재 (커뮤니티 reconstruction은 unverified)
- AGENTS.md vs CLAUDE.md 구별을 Boris가 공개 발언했다는 증거 없음 — Anthropic 공식 docs로만 attribution

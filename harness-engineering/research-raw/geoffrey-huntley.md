# Geoffrey Huntley Deep Research (Codex GPT-5.5, 17 web searches)

> Source: codex-researcher · 완료 2026-04-25 · ghuntley.com / X / Pragmatic Engineer / Latent Space / AI Giants 직접 조회

## A. CURSED 언어 — 3개월 주장 검증됨
- **날짜**: 2025-09-09
- **포스트**: "i ran Claude in a loop for three months..."
- **언어명**: **CURSED** — Gen-Z slang based, Go-like
- **출처**: https://ghuntley.com/cursed/ · https://x.com/GeoffreyHuntley/status/1965375700183499044
- **방법론** (https://ghuntley.com/ralph/): `while true` Ralph Wiggum loop. 초기엔 Go-like 언어 with Gen-Z slang keywords. 후에 specs/* 학습, fix_plan.md 사용, stdlib/compiler 구현, 테스트 실행, AGENT.md 업데이트, 통과 시 commit/tag, subagent 사용
- **본인이 인정한 caveat**: CURSED 미성숙, stdlib 일부 미완성. **Greenfield bootstrapping에만 적합 — 기존 코드베이스는 danger zone**

## B. 비용 숫자 (인용 가능)
- $50k 계약을 **$297**에 처리한 사례 (Amp/Ralph) — https://ghuntley.com/ralph/
- 소프트웨어 개발 비용이 **$10.42/hour**까지 떨어짐 — https://ghuntley.com/real/
- CURSED 자체 토큰 비용은 비공개

## C. Ralph Loop — 정확한 정의 + 10단계 레시피

> "Ralph is a technique. In its purest form, **Ralph is a Bash loop**."

```bash
while :; do cat PROMPT.md | claude-code ; done
```

레시피:
1. specs를 먼저 작성
2. PROMPT.md를 stable하게 유지
3. 매 loop에 같은 컨텍스트 할당 (특히 specs/*, fix_plan.md)
4. 한 번에 1개 작업만 요청
5. agent가 다음 가장 중요한 작업 선택하게
6. 테스트/빌드/static check를 **backpressure**로 강제
7. 교훈을 AGENT.md에 capture
8. plan 업데이트
9. 동작하는 increment commit
10. 실패 패턴 반복되면 prompt 튜닝

## D. Quotable Lines (슬라이드 직접 활용)
- "**Ralph is a Bash loop.**"
- "**The prompt is not magic; the loop plus backpressure is the system.**"
- "**Specs are memory you can reload every run.**"
- "**One task per loop; tighten when it drifts.**"
- "**Greenfield first. Existing codebases are the danger zone.**"
- "**The engineer's job becomes designing the loop.**"

## E. Spec-driven workflow
- 모델과 요구사항 대화 → **파일당 spec 1개** 작성 → spec에 대해 loop 실행
- Spec과 plan = fresh context 사이의 **durable memory**
- subagent는 search/summarization에 사용, validation/build concurrency는 제한 (bad backpressure 방지)
- 테스트가 왜 존재하는지 문서화 → 미래 loop가 보존/수정/삭제 판단 가능

## F. 본인이 인정한 risks (https://ghuntley.com/secure-codegen/)
- 잘못된 spec → loop 낭비
- bad search 후 agent가 작업 중복
- Claude는 placeholder 경향
- 동적 언어는 type/static check 필요
- 자율 deploy/sudo loop는 위험
- MCP/Cursor rules만으로는 secure generation 보장 X

## G. 발표 차용 포인트
1. **Bash loop 한 줄** — 가장 강력한 시각 (코드 한 줄로 Ralph loop 전체 설명)
2. **$297 / $50k 대비** — 비용 임팩트 슬라이드 (cost-per-feature)
3. **Greenfield only caveat** — autonomy ladder 슬라이드의 중요한 경계선
4. **MCP 만능론 비판** (이미지 27 = Huntley) — 실전 보안 측면에서 노골적 반대
5. **AGENT.md 업데이트 루프** — 학습이 도구 자체에 누적되는 방식

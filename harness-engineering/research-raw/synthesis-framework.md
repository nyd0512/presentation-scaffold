# Synthesis Framework (Codex Architect, gpt-5.5)

> Source: codex-architect background panel · 완료 2026-04-25
> 인물별 facts 없이 구조적 dimension 추출만 수행

## 1. 5축 Divergence (harness-relevant)
1. **Autonomy ceiling** — 무인 루프 허용 시간 (Huntley: weeks · Boris: hours · Armin: minutes)
2. **Repo isolation discipline** — one-question-per-worktree vs main-repo agent vs fleet of disposable clones (blast radius 설계)
3. **Spec/plan formalism** — "stdlib of prompts + AGENTS.md" (Huntley) ↔ "type the question, read the diff" (Simon)
4. **Verification locus** — tests (Armin) · 런타임/eval (Boris) · 사람 read-through (Simon) · compiler+types (Mitchell) · generated-then-pinned docs (Huntley)
5. **Tool surface breadth** — Claude-only ↔ multi-model router ↔ CLI orchestrator
6. (옵션) **Artifact permanence** — versioned skill ↔ ephemeral chat

## 2. Convergence Points (한국 청중 anchor)
1. Harness > Model
2. Tight feedback loop > clever prompt
3. Context engineering > prompt engineering
4. Disposability of code (spec/skill/eval이 durable artifact)
5. Plain-text file-based memory wins (AGENTS.md / CLAUDE.md / skills/)

## 3. "Harness as Scaffolding" 논거
- Huntley = harness-as-compiler
- Boris = harness-as-product (Claude Code 자체가 산출물)
- Simon = harness-as-personal-Unix
- Armin = harness-as-typechecker
- Mitchell = harness-as-build-system-extension

→ 모델 바꾸면 harness는 그대로 돌아가지만, harness 빠지면 모델은 그냥 챗봇.

## 4. 5인 매트릭스 (best-effort)

| 축 | Boris | Simon | Huntley | Armin | Mitchell |
|---|---|---|---|---|---|
| Autonomy ceiling | High | Low-Med | Very High | Low | Med |
| Repo isolation | Main+worktrees | Disposable per-Q | Fleet of clones | Main, gated | Worktrees? |
| Spec formalism | Med | Low (vibe-ish) | Very High | Med-High | High (Go-typed) |
| Verification | Evals + dogfood | Human read | Generated tests + pinned docs | Tests + types | Compiler + tests |
| Tool surface | Claude-Code native | Multi-model CLI zoo | Multi-engine, Ralph | Claude + skeptic eye | Claude + Ghostty stack |
| Artifact permanence | Skills/commands | Blog + gists | Versioned stdlib | Test suite | Codebase itself |

## 5. 발표 Arc (한국 엔지니어 청중)
**순서: Simon → Boris → Mitchell → Armin → Huntley**

이유: relatable (Simon=호기심 있는 개인) → insider canonical (Boris=메이커가 어떻게 쓰는가) → production-grade craft (Mitchell=Ghostty 출시) → 원칙 있는 회의주의 (Armin=어디서 깨지는가) → frontier extreme (Huntley=Ralph/fleet/주 단위)

청중은 영감 받지만 면역 생긴 채로 떠남.

**Money slide = Armin vs Huntley** — 같은 도구, 정반대 autonomy ceiling, 둘 다 ship. "정답은 없고 calibration만 있다"의 증명.

**Bridge slides:**
- Simon → Boris: "소스코드와 팀 슬랙이 있다면?"
- Boris → Mitchell: "터미널 에뮬레이터를 출시해야 한다면?"
- Mitchell → Armin: "컴파일러가 부족하다면 — 출력을 근본적으로 불신한다면?"
- Armin → Huntley: "그 불신을 자동화 게이트로 산업화하고 일주일 돌린다면?"

## 6. Productive Disagreement Teaching
- **장기 자율성**: Huntley YES, Armin NO → "당신 도메인은 Ralph-safe인가?"
- **Skills/AGENTS.md as code**: Huntley YES, Simon mostly NO → "팀 규모 vs 솔로 속도"
- **Multi-model routing**: Simon YES, Boris NO → "capability frontier vs workflow coherence"
- **diff: scan vs read**: Boris/Huntley scan, Simon/Armin read → "blast radius dictates review depth"
- **Repo topology**: disposable vs main-repo agent → "isolation cost vs context cost"

## 7. Harness Theater 재평가

**Real engineering (테스트 통과):**
- Artifact가 versioned + diffable (Huntley stdlib, Armin tests)
- Loop에 측정 가능한 closure signal 있음 (Boris evals, Mitchell compile)
- Harness 빼면 측정 가능한 품질 저하

**Theater (테스트 실패):**
- 아무도 안 읽고 테스트 안 하는 AGENTS.md
- write-only skills 디렉토리
- eval delta 없는 "multi-agent orchestration"
- A/B 안 한 elaborate prompt scaffold

→ **모든 5명의 harness는 다른 4명 눈에 theater로 보일 수 있다 — 측정하기 전까지는.** 청중 메시지: **harness 복잡도를 verification bandwidth에 맞춰 calibrate**.

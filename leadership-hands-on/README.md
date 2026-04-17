# AI Hands-on Course

S/W개발팀 리더진(PL/TL/임원) 대상 AI Agent 체험 교육 프로그램

> **도구:** Claude Code | **작성:** 김학민 (SE)

---

## 구조

| 폴더 | 내용 |
|------|------|
| `발표자료/` | 교육 슬라이드 (`presentation.html`, `tips.html`) |
| `실습자료/` | Lab 1~4 실습 가이드 및 데이터 |
| `result/` | 실습 결과물 예시 |
| `assets/` | 프레젠테이션 이미지 |
| `.skills/` | Claude Code 커스텀 스킬 모음 |

## 실습 목록

| Lab | 주제 | 핵심 경험 |
|-----|------|----------|
| 1 | 카카오톡 대화 분석 | 비정형 데이터 → 구조화된 인사이트 |
| 2 | 웹 리서치 리포트 | AI 심층 검색 → 보고서 자동 생성 |
| 3 | 스킬빌더 & 리포트 공장 | 커스텀 스킬 제작 → 반복 업무 자동화 |
| 4 | 자유 실습 | 실무 과제에 AI Agent 직접 적용 |

## 시작하기

```bash
git clone https://github.com/nydad/hands-on-course.git
cd hands-on-course
claude  # Claude Code 실행 후 실습자료/ 의 가이드를 따라 진행
```

## 핵심 개념

```
AI 성능 = Model × Agent × Pilot
```

- **Model** — AI의 추론 능력 (Claude Sonnet/Opus)
- **Agent** — 도구 사용·실행 능력 (Claude Code)
- **Pilot** — 사람의 판단·지시 능력 (프롬프트, 도메인 지식)

> 셋 중 하나라도 0이면 결과도 0

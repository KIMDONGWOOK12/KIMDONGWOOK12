<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:1C3C3C,100:6366F1&height=200&section=header&text=Dongwook%20Kim&fontSize=52&fontColor=ffffff&fontAlignY=36&desc=Python%20AI%20Developer%20%C2%B7%20RAG%20%C2%B7%20LLM%20Agents&descSize=18&descAlignY=56&animation=fadeIn" width="100%" alt="Dongwook Kim" />

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=19&pause=1400&color=6366F1&center=true&vCenter=true&width=560&lines=Python+AI+Developer;Build+it+by+hand%2C+then+with+the+framework.;RAG+%C2%B7+LLM+Agents+%C2%B7+Fine-tuning" alt="typing" />

**직접 만들어 보면서 “왜 필요한지”를 이해하는 Python AI 개발자, 김동욱입니다.**

<a href="#-about"><img src="https://img.shields.io/badge/About-1C3C3C?style=flat-square" /></a> <a href="#-personal-projects"><img src="https://img.shields.io/badge/Personal%20Projects-3F4A8A?style=flat-square" /></a> <a href="#-team-projects"><img src="https://img.shields.io/badge/Team%20Projects-5157C4?style=flat-square" /></a> <a href="#-tech-stack"><img src="https://img.shields.io/badge/Tech%20Stack-6366F1?style=flat-square" /></a>

</div>

<br/>

## 🙋 About

> **프레임워크를 쓰기 전에, 그 프레임워크가 무엇을 대체하는지 먼저 이해합니다.**

| 📝 **42편** | 🔁 **3번** | 📦 **6,529개** | 🧬 **7번** |
|:---:|:---:|:---:|:---:|
| 부트캠프 TIL 작성<br/><sub>구름 EXP 랭커</sub> | 같은 RAG를 다시 구현<br/><sub>Python → LangChain → LangGraph</sub> | PR 리뷰로 모델 직접 학습<br/><sub>QLoRA → vLLM 서빙</sub> | QLoRA 학습 반복<br/><sub>v1 → v7</sub> |

- 🐍 **주력 언어는 Python** — 개인 프로젝트 전부를 Python으로 만들었어요
- 🔥 **지금은** 카카오테크 부트캠프 팀 프로젝트 [**KGB**](#-team-projects)에서 AI 서버를 만들고 있어요
- 🎓 **AI컴퓨터공학과** 전공 · 🏅 **2025 학과 학회장**
- 🐛 에러 메시지가 원인을 말해주지 않을 땐, 중간값을 하나씩 찍어 가며 끝까지 좁혀 가요

<br/>

## 🚀 Personal Projects

<table>
<tr>
<td colspan="3">

### ⭐ [TIL-RAG](https://github.com/KIMDONGWOOK12/til-rag) &nbsp;<sub>`대표 프로젝트`</sub>

**내 TIL로 답하는 RAG를 세 번 다시 만들고, 코드 리뷰 모델까지 직접 학습시킨 프로젝트**

- 🔁 **순수 Python → LangChain → LangGraph ReAct Agent** 로 같은 RAG 재구현
- 🧬 GitHub PR 리뷰 **6,529개**로 `Qwen2.5-Coder-7B` QLoRA 파인튜닝 → **vLLM** 서빙
- ⚖️ 작은 모델은 혼자 믿기 어려워 **Claude가 판정·번역**, 3번 실패하면 fallback
- 🚢 Docker → AWS EC2, GitHub Actions로 push 시 자동 배포

<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" /> <img src="https://img.shields.io/badge/LangGraph-1C3C3C?style=flat-square&logo=langgraph&logoColor=white" /> <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" /> <img src="https://img.shields.io/badge/ChromaDB-FF6B6B?style=flat-square" /> <img src="https://img.shields.io/badge/QLoRA-6366F1?style=flat-square" /> <img src="https://img.shields.io/badge/vLLM-30A2FF?style=flat-square" /> <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" /> <img src="https://img.shields.io/badge/AWS%20EC2-FF9900?style=flat-square" />

<details>
<summary><b>🧬 학습 이력 v1 → v7 보기</b></summary>
<br/>

| 버전 | 데이터 | 베이스 모델 | steps | 결과 |
|:---:|---:|---|---:|---|
| v1 | 286 | Qwen2.5-1.5B | 60 | 과적합 — 무관한 질문에도 학습 문장 재생 |
| v3 | 1,334 | Qwen2.5-1.5B | 100 | 데이터를 늘리자 SQL 인젝션 첫 정답 |
| v5 | 6,529 | Qwen2.5-7B | 800 | 안정적이지만 보안 패턴에 약함 |
| v6 | 6,529 | Qwen2.5-Coder-7B | 800 | SQL은 완벽, 대신 과적합 |
| **v7** | 6,529 | **Qwen2.5-Coder-7B** | **350** | **균형 잡힌 최종 채택본** |

> 데이터 양이 정확도를, **베이스 모델의 사전 지식**이 보안 패턴 인식을 결정했습니다.

</details>

</td>
</tr>
<tr>
<td width="33%" valign="top">

### 🤖 [Dev Docs RAG Agent](https://github.com/KIMDONGWOOK12/dev-docs-rag-agent)

<sub>`완료`</sub>

질문을 보고 **검색이 필요한지부터 스스로 판단**하는 RAG 에이전트

- `judge → search → generate`
- LLM 3종 전환 (Gemini·Claude·Ollama)
- LangSmith로 답변 품질 평가

<img src="https://img.shields.io/badge/LangGraph-1C3C3C?style=flat-square&logo=langgraph&logoColor=white" /> <img src="https://img.shields.io/badge/LangSmith-1C3C3C?style=flat-square" />

</td>
<td width="33%" valign="top">

### 🛰 [Orbit-ChatBot](https://github.com/KIMDONGWOOK12/Orbit-ChatBot)

<sub>`진행 중`</sub>

개발 문서로 답하는 RAG 챗봇에 **직접 학습시킨 miniGPT** 연동

- 출처를 구분해 답변
- LCEL → StateGraph 전환
- miniGPT(33.6M) 연동 예정

<img src="https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white" /> <img src="https://img.shields.io/badge/miniGPT-6366F1?style=flat-square" />

</td>
<td width="33%" valign="top">

### 🧩 [CLI Quiz](https://github.com/KIMDONGWOOK12/KTB4-Orbit-AI)

<sub>`위클리 챌린지`</sub>

배운 개발 용어를 복습하는 **CLI 퀴즈 + 자동 오답노트**

- `asyncio`로 문제당 10초 제한
- 오답·시간 초과 자동 기록
- 표준 라이브러리만 사용

<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" /> <img src="https://img.shields.io/badge/asyncio-3776AB?style=flat-square" />

</td>
</tr>
</table>

<br/>

## 👥 Team Projects

<table>
<tr>
<td>

### 🧭 [KGB](https://github.com/100-hours-a-week/KTB4-10th-wiki/wiki) — Korean-culture Guide Book &nbsp;<sub>`진행 중` `팀 6인` `AI 파트`</sub>

**취향과 여행 조건에 맞는 장소 · 행사 · 로컬 콘텐츠를 한 권의 맞춤 가이드북으로 만들어 주는 여행 서비스**

- 🧑‍💻 **내 역할** — FastAPI · LangGraph AI 서버, **장소 추천 노드**와 TourAPI 연동
- 🔗 `장소 추천 → 행사 추천 → 일정 작성 → 추천 이유 작성` 4단계 멀티스텝 파이프라인
- 📍 장소는 **TourAPI 실데이터**로 고르고 문장만 LLM이 써서, 지도에 없는 장소(환각)를 막는 구조
- 🗓 2026.08 – 2026.11 · 2주 스프린트 · 10월 1차 출시 목표

<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" /> <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" /> <img src="https://img.shields.io/badge/LangGraph-1C3C3C?style=flat-square&logo=langgraph&logoColor=white" /> <img src="https://img.shields.io/badge/TourAPI-0A66C2?style=flat-square" /> &nbsp; [팀 위키](https://github.com/100-hours-a-week/KTB4-10th-wiki/wiki) · [AI 설계 위키](https://github.com/100-hours-a-week/KTB4-10th-AI/wiki) · [AI 레포](https://github.com/100-hours-a-week/KTB4-10th-AI)

</td>
</tr>
<tr>
<td>

### 🪐 [Orbit](https://github.com/KIMDONGWOOK12/Orbit) &nbsp;<sub>`팀 4인` `백엔드`</sub>

피드 · 팔로우 · 메시지 기능을 갖춘 **SNS 서비스 백엔드** — FastAPI 계층 분리, bcrypt + JWT 로그인 구현

<img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" /> <img src="https://img.shields.io/badge/SQLAlchemy-D71F00?style=flat-square&logo=sqlalchemy&logoColor=white" /> <img src="https://img.shields.io/badge/JWT-000000?style=flat-square&logo=jsonwebtokens&logoColor=white" />

</td>
</tr>
</table>

<br/>

## 🛠 Tech Stack

| | 기술 | 이렇게 썼어요 |
|:---:|---|---|
| 🐍 **주력** | <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" /> | 모든 개인 프로젝트 · RAG를 프레임워크 없이 순수 Python으로 직접 구현 |
| 🤖 **LLM · Agent** | <img src="https://img.shields.io/badge/LangGraph-1C3C3C?style=flat-square&logo=langgraph&logoColor=white" /> <img src="https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white" /> <img src="https://img.shields.io/badge/LangSmith-1C3C3C?style=flat-square" /> <img src="https://img.shields.io/badge/ChromaDB-FF6B6B?style=flat-square" /> | 조건부 분기 에이전트, ReAct Agent, 멀티스텝 파이프라인, RAG 평가 |
| 🧬 **Model** | <img src="https://img.shields.io/badge/Hugging%20Face-FFD21E?style=flat-square&logo=huggingface&logoColor=black" /> <img src="https://img.shields.io/badge/QLoRA-6366F1?style=flat-square" /> <img src="https://img.shields.io/badge/vLLM-30A2FF?style=flat-square" /> | Qwen2.5-Coder-7B 파인튜닝 · 서빙 |
| 🔌 **LLM API** | <img src="https://img.shields.io/badge/Gemini-8E75B2?style=flat-square&logo=googlegemini&logoColor=white" /> <img src="https://img.shields.io/badge/Claude-D97757?style=flat-square&logo=claude&logoColor=white" /> <img src="https://img.shields.io/badge/Ollama-000000?style=flat-square&logo=ollama&logoColor=white" /> | 환경변수 하나로 프로바이더 전환, 자체 모델 답변 검증 |
| ⚡ **Backend** | <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" /> <img src="https://img.shields.io/badge/SQLAlchemy-D71F00?style=flat-square&logo=sqlalchemy&logoColor=white" /> | AI 서버 API, SNS 백엔드 |
| 🚢 **Infra** | <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" /> <img src="https://img.shields.io/badge/AWS%20EC2-FF9900?style=flat-square" /> <img src="https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white" /> | TIL-RAG 컨테이너 배포 · CI/CD |

<br/>

## 🧭 Experience

| | 기간 | 내용 |
|:---:|---|---|
| 🚀 | **2026.05 – 현재** | **카카오테크 부트캠프 4기** · AI 과정<br/><sub>LLM · RAG · LangGraph 기반 AI 서비스 개발, 팀 프로젝트 KGB AI 파트</sub> |
| 💼 | **2026.02 – 2026.03** | **디메타(Dimeta)** · AI 개발팀 인턴<br/><sub>영상 비전 모델 학습 데이터 라벨링·정제, Agent AI 기술 리서치 세미나</sub> |
| 🏅 | **2024.12 – 2025.12** | **AI컴퓨터공학과 학회장**<br/><sub>정기 회의 운영, 학과 행사·외부 전시회 참여 기획</sub> |
| 🎓 | **2020.03 – 2026.02** | **AI컴퓨터공학과** 학사 과정 |

<!--
## 📫 Contact
연락처를 공개하고 싶다면 이 주석을 풀고 주소를 채워 넣으세요.
<a href="mailto:you@example.com"><img src="https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white" /></a>
-->

<br/>

<div align="center">

<img src="https://komarev.com/ghpvc/?username=KIMDONGWOOK12&label=visitors&color=6366F1&style=flat-square" alt="visitors" />

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:6366F1,100:1C3C3C&height=110&section=footer" width="100%" alt="footer" />

</div>

# 김동욱

Python으로 LLM 애플리케이션을 만든다. 카카오테크 부트캠프 4기 AI 과정에서 RAG와 LangGraph를 공부하고 있고, 지금은 팀 프로젝트 KGB에서 AI를 맡고 있다.

프레임워크를 쓰기 전에 그게 무엇을 대체하는지 먼저 알고 싶어서, 같은 RAG를 순수 Python, LangChain, LangGraph 순서로 세 번 다시 만들어 봤다. 5월부터 배운 내용을 TIL로 남겨 42편을 썼고, 그 TIL이 내 RAG 프로젝트들의 데이터가 됐다.

<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" /> <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" /> <img src="https://img.shields.io/badge/LangGraph-1C3C3C?style=flat-square&logo=langgraph&logoColor=white" /> <img src="https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white" /> <img src="https://img.shields.io/badge/LangSmith-1C3C3C?style=flat-square" /> <img src="https://img.shields.io/badge/ChromaDB-FF6B6B?style=flat-square" /> <img src="https://img.shields.io/badge/Hugging%20Face-FFD21E?style=flat-square&logo=huggingface&logoColor=black" /> <img src="https://img.shields.io/badge/vLLM-30A2FF?style=flat-square" /> <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" /> <img src="https://img.shields.io/badge/AWS%20EC2-FF9900?style=flat-square" /> <img src="https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white" />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/KIMDONGWOOK12/KIMDONGWOOK12/main/dist/defense-dark.svg">
  <img alt="Contribution Defense" src="https://raw.githubusercontent.com/KIMDONGWOOK12/KIMDONGWOOK12/main/dist/defense-light.svg" width="100%">
</picture>

<br/>

## 팀 프로젝트

### [KGB, Korean-culture Guide Book](https://github.com/100-hours-a-week/KTB4-10th-wiki/wiki) (2026.08 ~ 진행 중)

카카오테크 부트캠프 6인 팀 프로젝트에서 AI를 맡고 있다.

### [Orbit](https://github.com/KIMDONGWOOK12/Orbit)

4명이 만든 SNS 백엔드. FastAPI로 계층을 나누고 회원가입과 로그인(bcrypt, JWT)을 구현했다.

<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" /> <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" /> <img src="https://img.shields.io/badge/SQLAlchemy-D71F00?style=flat-square&logo=sqlalchemy&logoColor=white" /> <img src="https://img.shields.io/badge/JWT-000000?style=flat-square&logo=jsonwebtokens&logoColor=white" />

<br/>

## 개인 프로젝트

### [TIL-RAG](https://github.com/KIMDONGWOOK12/til-rag)

TIL 42편을 지식 베이스로 삼는 질의응답 시스템. 같은 파이프라인을 순수 Python으로 `retrieve()`와 `generate()`부터 직접 짜고, LangChain 체인으로 옮긴 뒤, 조건 분기와 재시도가 필요한 지점에서 LangGraph ReAct Agent로 바꿨다.

이후 GitHub PR 리뷰 6,529개로 Qwen2.5-Coder-7B를 QLoRA 파인튜닝하고 vLLM으로 서빙해서 코드 리뷰까지 확장했다. 7번을 다시 학습하면서 데이터 양보다 베이스 모델의 사전 지식이 더 크게 작용한다는 걸 확인했다. 작은 모델은 같은 코드에도 답이 매번 달라서, Claude가 답을 검증하고 세 번 실패하면 솔직하게 실패를 알리도록 했다. Docker로 묶어 EC2에 올리고 GitHub Actions로 배포를 자동화했다.

<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" /> <img src="https://img.shields.io/badge/LangGraph-1C3C3C?style=flat-square&logo=langgraph&logoColor=white" /> <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" /> <img src="https://img.shields.io/badge/ChromaDB-FF6B6B?style=flat-square" /> <img src="https://img.shields.io/badge/QLoRA-6366F1?style=flat-square" /> <img src="https://img.shields.io/badge/vLLM-30A2FF?style=flat-square" /> <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" /> <img src="https://img.shields.io/badge/AWS%20EC2-FF9900?style=flat-square" />

### [Dev Docs RAG Agent](https://github.com/KIMDONGWOOK12/dev-docs-rag-agent)

질문을 보고 검색이 필요한지부터 판단하는 LangGraph 에이전트. "LCEL이 뭐야?"는 TIL을 검색해서 답하고, "안녕하세요"는 검색 없이 바로 답한다. LangSmith로 키워드 매칭과 LLM-as-Judge를 비교해 보니, "State/Node/Edge"와 "노드/엣지"처럼 표현만 다른 정답을 키워드 매칭은 0점으로 처리했다.

<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" /> <img src="https://img.shields.io/badge/LangGraph-1C3C3C?style=flat-square&logo=langgraph&logoColor=white" /> <img src="https://img.shields.io/badge/LangSmith-1C3C3C?style=flat-square" /> <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" />

### [Orbit-ChatBot](https://github.com/KIMDONGWOOK12/Orbit-ChatBot) (진행 중)

개발 문서로 답하는 RAG 챗봇. 직접 학습시킨 miniGPT(33.6M)를 생성 모델로 붙이는 게 목표다.

<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" /> <img src="https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white" /> <img src="https://img.shields.io/badge/LangGraph-1C3C3C?style=flat-square&logo=langgraph&logoColor=white" />

### [CLI Quiz](https://github.com/KIMDONGWOOK12/KTB4-Orbit-AI)

부트캠프 위클리 챌린지 1주차. 배운 개발 용어로 퀴즈를 내고, asyncio로 문제마다 10초 제한을 걸어 틀린 문제는 오답노트에 자동으로 쌓는다.

<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" />

<br/>

## 경력과 활동

- 2026.05 ~ 현재　카카오테크 부트캠프 4기 AI 과정
- 2026.02 ~ 2026.03　디메타(Dimeta) AI 개발팀 인턴. 영상 비전 모델 학습 데이터 라벨링과 정제, Agent AI 리서치 세미나
- 2024 ~ 2025　AI컴퓨터공학과 학회장 (2년)
- AI컴퓨터공학과 전공

<!--
## 연락처
연락처를 공개하고 싶다면 이 주석을 풀고 주소를 채워 넣으세요.
- Email: you@example.com
-->

"""프로필 README에 쓰는 프로젝트 카드(SVG)를 라이트/다크 두 벌씩 만든다.

    python cards/make_cards.py
"""

from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).parent
FONT = ("-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Apple SD Gothic Neo', "
        "'Malgun Gothic', 'Noto Sans KR', sans-serif")
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"

THEMES = {
    "light": dict(bg="#ffffff", border="#d0d7de", title="#1f2328", text="#424a53",
                  muted="#656d76", box="#f6f8fa", pill="#f6f8fa", pill_border="#d0d7de"),
    "dark": dict(bg="#0d1117", border="#30363d", title="#e6edf3", text="#c9d1d9",
                 muted="#8b949e", box="#161b22", pill="#161b22", pill_border="#30363d"),
}
ACCENT = "#6366F1"
STATUS = {"완료": "#1F883D", "진행 중": "#BF8700", "대표 프로젝트": ACCENT,
          "위클리 챌린지": "#0969DA"}


def text_width(s, size):
    """폰트를 불러올 수 없으니 글자 종류별 평균 폭으로 어림한다."""
    w = 0.0
    for ch in s:
        if ord(ch) >= 0x1100:
            w += 1.0
        elif ch.isupper() or ch.isdigit():
            w += 0.64
        elif ch == " ":
            w += 0.3
        else:
            w += 0.54
    return w * size


def t(x, y, s, size, fill, weight=400, family=FONT, anchor="start"):
    return (f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" '
            f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{escape(s)}</text>')


def pill(x, y, label, th, size=12, fill=None, color=None):
    w = text_width(label, size) + 20
    bg = fill or th["pill"]
    stroke = "none" if fill else th["pill_border"]
    return (f'<rect x="{x}" y="{y}" width="{w:.1f}" height="24" rx="12" fill="{bg}" stroke="{stroke}"/>'
            + t(x + w / 2, y + 16.5, label, size, color or th["text"], 600, anchor="middle")), w


def pills(x, y, labels, th):
    out = []
    for label in labels:
        svg, w = pill(x, y, label, th)
        out.append(svg)
        x += w + 8
    return "".join(out)


def frame(w, h, th, body):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
<defs>
  <linearGradient id="g" x1="0" x2="1"><stop offset="0" stop-color="#1C3C3C"/><stop offset="1" stop-color="{ACCENT}"/></linearGradient>
  <clipPath id="c"><rect x="1" y="1" width="{w - 2}" height="{h - 2}" rx="14"/></clipPath>
</defs>
<rect x="1" y="1" width="{w - 2}" height="{h - 2}" rx="14" fill="{th['bg']}" stroke="{th['border']}"/>
<rect x="0" y="0" width="{w}" height="5" fill="url(#g)" clip-path="url(#c)"/>
{body}
</svg>
"""


def status_pill(x, y, label, th):
    color = STATUS.get(label, th["muted"])
    svg, w = pill(x, y, label, th, fill=color, color="#ffffff")
    return svg, w


def wide_card(th, c):
    """대표 카드: 제목, 한 줄 소개, 흐름, 숫자 4칸, 기술 배지."""
    W, pad = 830, 28
    body = []
    x = pad
    for label in c["tags"]:
        svg, w = status_pill(x, 24, label, th) if label in STATUS else pill(x, 24, label, th)
        body.append(svg)
        x += w + 8
    if c.get("period"):
        body.append(t(W - pad, 41, c["period"], 13, th["muted"], 500, anchor="end"))
    body.append(t(pad, 88, c["title"], 28, th["title"], 700))
    if c.get("title_sub"):
        body.append(t(pad + text_width(c["title"], 28) + 12, 88, c["title_sub"], 16, th["muted"], 500))
    body.append(t(pad, 118, c["desc"], 15, th["text"], 500))
    y = 144
    if c.get("flow"):
        body.append(t(pad, y, c["flow"], 13, th["muted"], 500, family=MONO))
        y += 20
    if c.get("steps"):
        body.append(steps_row(pad, y, c["steps"], th))
        y += 70
    if c.get("stats"):
        n, gap = len(c["stats"]), 12
        bw = (W - 2 * pad - gap * (n - 1)) / n
        for i, (num, label) in enumerate(c["stats"]):
            bx = pad + i * (bw + gap)
            body.append(f'<rect x="{bx:.1f}" y="{y}" width="{bw:.1f}" height="64" rx="10" fill="{th["box"]}" stroke="{th["border"]}"/>')
            body.append(t(bx + 16, y + 29, num, 21, ACCENT, 700))
            body.append(t(bx + 16, y + 50, label, 12.5, th["muted"], 500))
        y += 82
    if c.get("note"):
        body.append(t(pad, y + 4, c["note"], 13.5, th["text"], 500))
        y += 22
    body.append(pills(pad, y, c["stack"], th))
    return frame(W, y + 24 + pad - 4, th, "\n".join(body))


def steps_row(x, y, steps, th):
    """KGB 파이프라인: 단계 칩을 화살표로 잇고, 내 담당 단계는 강조한다."""
    out = []
    for i, (label, mine) in enumerate(steps):
        w = text_width(label, 13) + 28
        fill = ACCENT if mine else th["box"]
        stroke = ACCENT if mine else th["border"]
        color = "#ffffff" if mine else th["text"]
        out.append(f'<rect x="{x:.1f}" y="{y}" width="{w:.1f}" height="32" rx="8" fill="{fill}" stroke="{stroke}"/>')
        out.append(t(x + w / 2, y + 21, label, 13, color, 600, anchor="middle"))
        if mine:
            out.append(t(x + w / 2, y + 46, "내 담당", 11, ACCENT, 700, anchor="middle"))
        x += w
        if i < len(steps) - 1:
            out.append(t(x + 14, y + 21, "→", 14, th["muted"], 600, anchor="middle"))
            x += 28
    return "".join(out)


def small_card(th, c):
    """3칸 그리드 카드: 상태, 제목, 두 줄 소개, 포인트 두 개, 기술 배지."""
    W, H, pad = 270, 262, 20
    body = []
    svg, _ = status_pill(pad, 22, c["status"], th)
    body.append(svg)
    body.append(t(pad, 78, c["title"], 18, th["title"], 700))
    for i, line in enumerate(c["desc"]):
        body.append(t(pad, 106 + i * 20, line, 13.5, th["text"], 500))
    for i, point in enumerate(c["points"]):
        py = 164 + i * 22
        body.append(f'<circle cx="{pad + 3}" cy="{py - 4}" r="2.5" fill="{ACCENT}"/>')
        body.append(t(pad + 13, py, point, 12.5, th["muted"], 500))
    body.append(pills(pad, H - pad - 26, c["stack"], th))
    return frame(W, H, th, "\n".join(body))


CARDS = {
    "til-rag": (wide_card, dict(
        tags=["대표 프로젝트", "개인"],
        title="TIL-RAG",
        desc="내 TIL로 답하는 RAG를 세 번 다시 만들고, 코드 리뷰 모델까지 직접 학습시킨 프로젝트",
        flow="순수 Python → LangChain → LangGraph   ·   QLoRA → vLLM   ·   Docker → EC2",
        stats=[("3번", "같은 RAG를 다시 구현"), ("6,529개", "PR 리뷰로 모델 학습"),
               ("7번", "QLoRA 학습 반복 (v1→v7)"), ("Claude", "자체 모델 답변 검증")],
        stack=["Python", "LangGraph", "FastAPI", "ChromaDB", "QLoRA", "vLLM", "Docker", "AWS EC2"],
    )),
    "dev-docs-rag-agent": (small_card, dict(
        status="완료", title="Dev Docs RAG Agent",
        desc=["질문을 보고 검색이 필요한지", "스스로 판단하는 RAG 에이전트"],
        points=["judge → search → generate", "LLM 3종 전환 · LangSmith 평가"],
        stack=["Python", "LangGraph"],
    )),
    "orbit-chatbot": (small_card, dict(
        status="진행 중", title="Orbit-ChatBot",
        desc=["개발 문서 RAG 챗봇에", "직접 학습시킨 miniGPT 연동"],
        points=["LCEL → StateGraph 전환", "miniGPT (33.6M) 연동 예정"],
        stack=["Python", "LangChain"],
    )),
    "cli-quiz": (small_card, dict(
        status="위클리 챌린지", title="CLI Quiz",
        desc=["배운 개발 용어를 복습하는", "CLI 퀴즈 + 자동 오답노트"],
        points=["asyncio로 문제당 10초 제한", "표준 라이브러리만 사용"],
        stack=["Python", "asyncio"],
    )),
    "kgb": (wide_card, dict(
        tags=["진행 중", "팀 6인", "AI 파트"],
        period="2026.08 – 2026.11",
        title="KGB", title_sub="Korean-culture Guide Book",
        desc="취향과 여행 조건에 맞는 장소 · 행사를 한 권의 맞춤 가이드북으로 만들어 주는 여행 서비스",
        steps=[("장소 추천", True), ("행사 추천", False), ("일정 작성", False), ("추천 이유 작성", False)],
        note="장소는 TourAPI 실데이터로 고르고 문장만 LLM이 써서, 지도에 없는 장소(환각)를 막아요",
        stack=["Python", "FastAPI", "LangGraph", "TourAPI"],
    )),
    "orbit": (wide_card, dict(
        tags=["팀 4인", "백엔드"],
        title="Orbit",
        desc="피드 · 팔로우 · 메시지 기능을 갖춘 SNS 서비스 백엔드 — 계층 분리, bcrypt + JWT 로그인",
        stack=["Python", "FastAPI", "SQLAlchemy", "JWT"],
    )),
}

if __name__ == "__main__":
    for name, (render, data) in CARDS.items():
        for theme, th in THEMES.items():
            (OUT / f"{name}-{theme}.svg").write_text(render(th, data), encoding="utf-8")
    print(f"{len(CARDS) * len(THEMES)} cards written to {OUT}")

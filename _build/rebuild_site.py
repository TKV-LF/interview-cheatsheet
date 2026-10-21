#!/usr/bin/env python3
"""Rebuild the cheatsheet into category pages with one reading layout."""
from __future__ import annotations

import html
import json
import re
import sys
from difflib import SequenceMatcher
from pathlib import Path

ROOT = Path("/Users/thuynt/Working/Vibe/interview-cheatsheet")
SRC = ROOT / "_build" / "source"
sys.path.insert(0, str(ROOT / "_build"))

from go1_vi import GO1_VI  # noqa: E402
from new_questions import NEW  # noqa: E402

PAGES = [
    ("fit.html", "fit", "Fit and intro", "Who you are, why this kind of role, and why you are looking."),
    ("behavioral.html", "behavioral", "Behavioral", "Stories, judgement, teamwork, Agile, and how you use AI."),
    ("english.html", "english", "Spoken English", "Phrases for the minutes around the technical answer."),
    ("php.html", "php", "PHP", "Laravel, pure PHP, MySQL, and the API in front of a React client."),
    ("react.html", "react", "React and TypeScript", "UI fundamentals, state, workflows, and the libraries you can defend."),
    ("node.html", "node", "Node.js", "The event loop, Express, and the server work you can honestly claim."),
    ("devops.html", "devops", "DevOps and cloud", "What you have operated, then the cloud and infra questions around it."),
    ("debugging.html", "debug", "Debugging", "Decide the layer, then prove it before you change code."),
    ("system-design.html", "system", "System design", "A simple path first. Scale only the part that breaks."),
    ("cv.html", "cv", "CV and projects", "Akktis, IELTS, and BaseVN — walk the real work, including the hard fixes."),
]

NAV = [(href, label) for href, _pid, label, _blurb in PAGES]

SKIP_GO1 = {"q2", "q31"}
SKIP_SECTIONS = {("kaopiz", "sec-behavioral"), ("kaopiz", "sec-close")}

ENG_PAGE = {
    "sec-node": ("node", "Node.js fundamentals"),
    "sec-php": ("php", "PHP and Laravel"),
    "sec-pure-php": ("php", "Pure PHP"),
    "sec-react": ("react", "React fundamentals"),
    "sec-react-libs": ("react", "Libraries"),
    "sec-workflow": ("react", "Workflows and dashboards"),
    "sec-state": ("react", "State management"),
    "sec-dash-libs": ("react", "Dashboard libraries"),
    "sec-why-stack": ("react", "Why this UI stack"),
    "sec-enterprise": ("cv", "Enterprise stories"),
    "sec-integ": ("php", "PHP API and React client"),
    "sec-design": ("system", "How you design"),
}
FIT_PAGE = {
    "sec-fit": ("fit", "PHP and React"),
    "sec-fit-devops": ("fit", "DevOps"),
    "sec-fit-node": ("fit", "Node and TypeScript"),
}
SOFT_PAGE = {
    "sec-collab": ("behavioral", "Collaboration"),
    "sec-debug": ("debug", "Find the layer"),
    "sec-solve": ("behavioral", "Problem solving"),
    "sec-quality": ("behavioral", "Agile and quality"),
    "sec-ai": ("behavioral", "AI-assisted coding"),
    "sec-hard": ("behavioral", "Under pressure"),
    "sec-spoken": ("english", "In the room"),
}
GO1_PAGE = {
    "q1": ("fit", "General"),
    "q3": ("behavioral", "Stories"),
    "q4": ("behavioral", "Stories"),
    "q5": ("behavioral", "Stories"),
    "q6": ("behavioral", "Judgement"),
    "q7": ("fit", "General"),
    "q8": ("behavioral", "Judgement"),
    "q9": ("behavioral", "Stories"),
    "q10": ("behavioral", "Stories"),
    "q11": ("behavioral", "Judgement"),
    "q12": ("behavioral", "Conflict"),
    "q13": ("behavioral", "Collaboration"),
    "q14": ("behavioral", "Feedback and mistakes"),
    "q17": ("behavioral", "Leadership"),
    "q19": ("behavioral", "Working with product"),
    "q21": ("behavioral", "Leadership"),
    "q22": ("behavioral", "Judgement"),
    "q24": ("cv", "IELTS"),
    "q25": ("system", "AI features"),
    "q28": ("devops", "How you operate"),
    "cv-map": ("cv", "If they point at the CV"),
    "cv-500k": ("cv", "BaseVN deep dive"),
    "cv-explain": ("cv", "BaseVN deep dive"),
    "cv-paginate": ("cv", "BaseVN deep dive"),
    "cv-caught": ("cv", "BaseVN deep dive"),
    "cv-hardest": ("cv", "BaseVN deep dive"),
    "cv-estimate": ("behavioral", "Planning"),
    "cv-estimate-wrong": ("behavioral", "Planning"),
    "cv-priority": ("behavioral", "Judgement"),
    "cv-sync": ("cv", "BaseVN deep dive"),
    "cv-prod": ("cv", "Production stories"),
    "cv-test": ("cv", "BaseVN deep dive"),
    "cv-leave": ("fit", "Career moves"),
    "cv-pokes": ("cv", "If they point at the CV"),
}

ARTICLE_RE = re.compile(r'<article class="question-card" id="([^"]+)">(.*?)</article>', re.S)
SECTION_RE = re.compile(r'<section class="section-block" id="([^"]+)"[^>]*>\s*<h2>(.*?)</h2>', re.S)
GO1_RE = re.compile(r'<(article|section) class="card(?: q)?" id="([^"]+)">(.*?)</\1>', re.S)
TAG_RE = re.compile(r"<[^>]+>")


def clean_text(raw: str) -> str:
    text = TAG_RE.sub(" ", raw or "")
    text = html.unescape(text)
    return re.sub(r"\s+", " ", text).strip()


def clean_heading(raw: str) -> str:
    text = clean_text(raw)
    text = re.sub(r"^[A-Z]\.\s+", "", text)
    text = re.sub(r"^\d+\s*[·.\-]\s*", "", text)
    return text.strip(" ·-")


def clean_title(raw: str) -> str:
    text = clean_text(raw)
    text = re.sub(r"^\d+[a-z]?\.\s*", "", text)
    return text.strip()


def decompany(value: str) -> str:
    reps = [
        ("Why Globant JD made you research Zustand", "Why a job description made you research Zustand"),
        ("Honest comparison for Globant.", "Honest comparison."),
        ("Important split for Globant JD.", "Client state versus API data."),
        ("Ties to Globant / Zustand honesty.", "Use AI to ramp, then own the code."),
        ("How would you use AI to learn Globant's stack faster?", "How would you use AI to learn a new stack faster?"),
        ("patterns Globant uses day to day", "patterns a team uses day to day"),
        ("For Globant I'd follow the team's", "I'd follow the team's"),
        ("For Globant enterprise products", "For enterprise products"),
        ("If Globant uses one", "If the team uses one"),
        ("For Globant-style dashboards, Router", "For enterprise dashboards, Router"),
        ("For Globant-style dashboards with dense data", "For dense dashboards"),
        ("on Globant's React/TypeScript stack", "on a React/TypeScript stack"),
        ("Globant libs are the new tools to learn", "Those libraries are the new tools to learn"),
        ("If Globant uses React Flow", "If the team uses React Flow"),
        ("Classic Globant-shaped app", "Classic enterprise dashboard"),
        ("how Globant shares these elements", "how the team shares these elements"),
        ("Globant's JD mentions long-term solutions — that matches how I like to work.", "That matches how I like to work."),
        ("on Globant projects", "on the next team"),
        ("Với sản phẩm enterprise Globant", "Với sản phẩm enterprise"),
        ("pattern team Globant dùng hằng ngày", "pattern team dùng hằng ngày"),
        ("Với Globant tôi theo style team", "Tôi theo style của team"),
        ("Nếu Globant dùng một bộ", "Nếu team dùng một bộ"),
        ("Với dashboard kiểu Globant,", "Với dashboard enterprise,"),
        ("của Globant và học nhanh", "và học nhanh"),
        ("Nếu Globant dùng React Flow", "Nếu team dùng React Flow"),
        ("App kiểu Globant:", "App enterprise:"),
        ("Dashboard kiểu Globant data dày", "Dashboard enterprise data dày"),
        ("hỏi Globant share element", "hỏi team share element"),
        ("JD Globant nói long-term solutions — khớp cách tôi muốn làm.", "Khớp cách tôi muốn làm."),
        ("học stack Globant nhanh thế nào?", "học một stack mới nhanh thế nào?"),
        ("That’s why Go1 interested me.", "That is the kind of product team I want next."),
        ("That's why Go1 interested me.", "That is the kind of product team I want next."),
        ("that points to Go1", "then say what you want next"),
        ("a product company like Go1 feels like the right next step", "a product company feels like the right next step"),
        ("Go1 is doing that at a much larger scale than my current projects.", "I want to do that at a larger scale than my current projects."),
        ("This is exactly how Go1 says engineers should work.", "This is how a strong product team expects engineers to work."),
        ("remote Go1 team", "remote team"),
        ("At Go1 that also means", "On a product team that also means"),
        ("Go1’s problem is similar", "A learning product’s problem is similar"),
        ("Go1's problem is similar", "A learning product's problem is similar"),
        ("the same habit Go1 is asking for", "the same habit a strong team asks for"),
        ("Same as arriving at Go1.", "Same as joining a new team."),
        ("Infra angle for Kaopiz.", "Infra angle."),
        ("Infra angle for Kaopiz", "Infra angle"),
        ("If she asks", "If they ask"),
        ("If she says", "If they say"),
        ("If she wants", "If they want"),
        ("If she names", "If they name"),
        ("if she asks", "if they ask"),
        ("she will", "they will"),
        ("She will", "They will"),
        ("Jasneet Kaur", "the interviewer"),
        ("Jasneet", "the interviewer"),
        ("Junaid and Joe", "the interviewers"),
        ("Morgan", "the in-product assistant"),
    ]
    for old, new in reps:
        value = value.replace(old, new)
    return value


def retarget(page: str, section: str, title: str) -> tuple[str, str]:
    low = title.lower()
    if page == "node" and "ielts" in low:
        return "cv", "IELTS — technical"
    if page == "node" and ("react native" in low or "desktop and mobile" in low):
        return "react", "React Native"
    if page == "node" and "responsive ui" in low:
        return "react", "UI quality"
    if page == "node" and "work with pms" in low:
        return "behavioral", "Working with product"
    if page == "node" and "client-side vs server-side" in low:
        return "system", "Architecture"
    if page == "node" and low.startswith("firestore"):
        return "cv", "IELTS — technical"
    return page, section


def grab(pattern: str, block: str) -> list[str]:
    return re.findall(pattern, block, flags=re.S)


def card_from_article(source: str, sec_id: str, sec_name: str, cid: str, block: str) -> dict | None:
    if source == "globant":
        return None
    if (source, sec_id) in SKIP_SECTIONS:
        return None
    page, section = {
        "engineering": ENG_PAGE,
        "fit": FIT_PAGE,
        "soft": SOFT_PAGE,
    }.get(source, {}).get(sec_id, (None, None))
    if page is None:
        if source == "devops":
            page, section = "devops", sec_name or "DevOps"
        elif source == "cv":
            page, section = "cv", sec_name or "Projects"
        elif source == "kaopiz":
            page, section = "devops", sec_name or "Cloud and infra"
        else:
            return None
    heads = grab(r"<h2>(.*?)</h2>", block)
    title = clean_title(heads[0]) if heads else cid
    hint_m = re.search(r'<div class="question-head">.*?<p>(.*?)</p>', block, re.S)
    hint = clean_text(hint_m.group(1)) if hint_m else ""
    cells = [(kind, inner.strip()) for kind, inner in grab(r'<div class="cell (question|answer)">(.*?)</div>', block)]
    questions = [inner for kind, inner in cells if kind == "question"]
    answers = [inner for kind, inner in cells if kind == "answer"]
    q_en = questions[0] if questions else f"<p>{html.escape(title)}</p>"
    a_en = answers[0] if answers else ""
    q_vi = questions[1] if len(questions) > 1 else q_en
    a_vi = answers[1] if len(answers) > 1 else ""
    if not clean_text(a_en):
        return None
    notes = "".join(grab(r'<div class="crib">(.*?)</div>', block) + grab(r'<div class="star">(.*?)</div>', block))
    page, section = retarget(page, section, title)
    return {
        "id": f"{source}-{cid}",
        "page": page,
        "section": section,
        "title": decompany(title),
        "hint": decompany(hint),
        "q_en": decompany(q_en),
        "a_en": decompany(a_en),
        "q_vi": decompany(q_vi),
        "a_vi": decompany(a_vi),
        "notes": decompany(notes),
    }


def extract_standard(source: str, filename: str) -> list[dict]:
    raw = (SRC / filename).read_text(encoding="utf-8")
    sections = [(m.start(), m.group(1), clean_heading(m.group(2))) for m in SECTION_RE.finditer(raw)]
    found = []
    for match in ARTICLE_RE.finditer(raw):
        sec_id, sec_name = "", ""
        for pos, sid, sname in sections:
            if pos < match.start():
                sec_id, sec_name = sid, sname
        item = card_from_article(source, sec_id, sec_name, match.group(1), match.group(2))
        if item:
            found.append(item)
    return found


def extract_go1() -> list[dict]:
    raw = (SRC / "go1-leadership.html").read_text(encoding="utf-8")
    found = []
    for match in GO1_RE.finditer(raw):
        cid = match.group(2)
        if cid in SKIP_GO1 or cid not in GO1_PAGE:
            continue
        block = match.group(3)
        h2s = [clean_title(h) for h in grab(r"<h2>(.*?)</h2>", block)]
        title = " / ".join(h2s[:2]) if h2s else cid
        follows = grab(r'<p class="follow">(.*?)</p>', block)
        hint = clean_text(follows[0]) if follows else ""
        body = re.sub(r'<div class="label">.*?</div>', "", block, flags=re.S)
        body = re.sub(r'<p class="follow">.*?</p>', "", body, flags=re.S)
        body = re.sub(r"<h2>.*?</h2>", "", body, count=1, flags=re.S)
        body = body.strip()
        notes = "".join(f"<p>{part.strip()}</p>" for part in follows)
        page, section = GO1_PAGE[cid]
        q_vi, a_vi = GO1_VI.get(cid, ("", ""))
        found.append({
            "id": f"go1-{cid}",
            "page": page,
            "section": section,
            "title": decompany(title),
            "hint": decompany(hint),
            "q_en": f"<p>{html.escape(decompany(title))}.</p>" if not title.endswith("?") else f"<p>{html.escape(decompany(title))}</p>",
            "a_en": decompany(body),
            "q_vi": f"<p>{html.escape(q_vi)}</p>" if q_vi else f"<p>{html.escape(decompany(title))}</p>",
            "a_vi": a_vi,
            "notes": decompany(notes),
        })
    return found


def plain(card: dict) -> str:
    return clean_text(" ".join([
        card["title"], card["hint"], card["q_en"], card["a_en"], card["q_vi"], card["a_vi"], card["notes"],
    ]))


def dedupe(cards: list[dict]) -> list[dict]:
    kept: list[dict] = []
    dropped = 0
    for card in cards:
        question = clean_text(card["q_en"]).lower()
        answer = clean_text(card["a_en"])
        replaced = False
        for index, prev in enumerate(kept):
            if prev["page"] != card["page"]:
                continue
            q_ratio = SequenceMatcher(None, question, clean_text(prev["q_en"]).lower()).ratio()
            a_ratio = SequenceMatcher(None, answer, clean_text(prev["a_en"])).ratio()
            if q_ratio < 0.86 or a_ratio < 0.72:
                continue
            challenger = card
            incumbent = prev
            if (len(clean_text(prev["a_en"])) + len(clean_text(prev["a_vi"]))) >= (
                len(clean_text(card["a_en"])) + len(clean_text(card["a_vi"]))
            ):
                challenger, incumbent = prev, card
            kept[index] = challenger
            dropped += 1
            replaced = True
            print(f"drop {incumbent['id']} ~ {challenger['id']} ({q_ratio:.2f}/{a_ratio:.2f})")
            break
        if not replaced:
            kept.append(card)
    print(f"deduped {dropped}")
    return kept


def new_cards() -> list[dict]:
    made = []
    for index, item in enumerate(NEW, start=1):
        made.append({
            "id": f"new-{item['page']}-{index}",
            "page": item["page"],
            "section": item["section"],
            "title": item["title"],
            "hint": item["hint"],
            "q_en": f"<p>{html.escape(item['q_en'])}</p>",
            "a_en": item["a_en"],
            "q_vi": f"<p>{html.escape(item['q_vi'])}</p>",
            "a_vi": item["a_vi"],
            "notes": "",
        })
    return made


SECTION_RANK = {
    "fit": ["General", "PHP and React", "DevOps", "Node and TypeScript", "Career moves"],
    "behavioral": [
        "Stories", "Conflict", "Judgement", "Leadership", "Collaboration",
        "Working with product", "Planning", "Feedback and mistakes",
        "Problem solving", "Under pressure", "Agile and quality", "AI-assisted coding",
    ],
}


def grouped(cards: list[dict], page: str) -> list[tuple[str, list[dict]]]:
    order: list[str] = []
    buckets: dict[str, list[dict]] = {}
    for card in cards:
        if card["page"] != page:
            continue
        buckets.setdefault(card["section"], []).append(card)
        if card["section"] not in order:
            order.append(card["section"])
    preferred = SECTION_RANK.get(page, [])
    positions = {name: index for index, name in enumerate(order)}

    def rank(name: str) -> tuple[int, int]:
        if name == "Common questions":
            return (2, 0)
        if name in preferred:
            return (0, preferred.index(name))
        return (1, positions[name])

    order.sort(key=rank)
    return [(name, buckets[name]) for name in order]


def esc(value: str) -> str:
    return html.escape(value or "", quote=True)


def render_card(card: dict, number: int) -> str:
    blob = esc(plain(card))
    notes = f'<div class="notes">{card["notes"]}</div>' if clean_text(card["notes"]) else ""
    vi = card["a_vi"] or "<p>Kể lại cùng các mốc ở bản English. Giữ số và tên hệ thống, đừng dịch từng chữ.</p>"
    cid = esc(card["id"])
    return f"""<details class="q" id="{cid}" data-blob="{blob}">
<summary><span class="num">{number:02d}</span><span><span class="q-title">{esc(card["title"])}</span><span class="q-hint">{esc(card["hint"])}</span></span></summary>
<div class="q-body">
<div class="lang"><button type="button" data-set-lang="en">English</button><button type="button" data-set-lang="vi">Tiếng Việt</button></div>
<div data-pane="en"><div class="ask">{card["q_en"]}</div><div class="ans">{card["a_en"]}</div></div>
<div data-pane="vi" hidden><div class="ask">{card["q_vi"]}</div><div class="ans">{vi}</div></div>
{notes}
</div>
</details>"""


def shell(page_id: str, title: str, active: str, body: str) -> str:
    nav = "\n".join(
        f'<a href="{href}" class="{"is-on" if href == active else ""}">{esc(label)}</a>'
        for href, label in [("index.html", "Hub")] + NAV
    )
    return f"""<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{esc(title)}</title>
<link href="https://api.fontshare.com/v2/css?f[]=satoshi@400,500,700&f[]=general-sans@500,600,700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/site.css" />
</head>
<body data-page="{esc(page_id)}">
<a class="skip" href="#content">Skip to questions</a>
<header class="topbar">
<div class="topbar-inner">
<div class="brand-row">
<a class="brand" href="index.html">Interview cheatsheet</a>
<button class="icon-btn" type="button" data-theme-toggle aria-label="Switch theme">☾</button>
</div>
<div class="search-wrap">
<span class="mag" aria-hidden="true">⌕</span>
<input data-search type="search" placeholder="Search questions — press /" aria-label="Search questions" />
<div class="hits" data-hits></div>
<p class="search-meta" data-search-meta></p>
</div>
</div>
<nav class="nav-scroll" aria-label="Categories">{nav}</nav>
</header>
{body}
<script src="assets/search-index.js"></script>
<script src="assets/site.js"></script>
</body>
</html>
"""


def render_page(href: str, page_id: str, label: str, blurb: str, cards: list[dict], index_rows: list[dict]) -> str:
    groups = grouped(cards, page_id)
    side = ['<h2>On this page</h2>']
    main = [f'<header class="page-intro"><h1>{esc(label)}</h1><p>{esc(blurb)} Open one question at a time. Switch language inside the answer.</p></header>']
    main.append('<div class="toolbar"><button type="button" data-expand="open">Expand</button><button type="button" data-expand="close">Collapse</button></div>')
    number = 1
    for name, items in groups:
        sec_id = "sec-" + re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
        side.append(f'<a class="sec-link" data-sec href="#{sec_id}">{esc(name)}</a>')
        main.append(f'<section class="block" id="{sec_id}"><h2>{esc(name)}</h2>')
        for card in items:
            side.append(f'<a class="q-link" href="#{esc(card["id"])}">{number:02d} {esc(card["title"])}</a>')
            main.append(render_card(card, number))
            index_rows.append({
                "page": page_id,
                "category": label,
                "title": card["title"],
                "href": f"{href}#{card['id']}",
                "text": plain(card),
            })
            number += 1
        main.append("</section>")
    body = f'<div class="shell"><aside class="side">{"".join(side)}</aside><main id="content">{"".join(main)}</main></div>'
    return shell(page_id, f"{label} — Interview cheatsheet", href, body)


def render_hub(counts: dict[str, int]) -> str:
    cards = []
    for href, pid, label, blurb in PAGES:
        cards.append(
            f'<a class="card" href="{href}"><span class="kicker">{counts.get(pid, 0)} questions</span>'
            f"<h2>{esc(label)}</h2><p>{esc(blurb)}</p></a>"
        )
    body = f"""<main class="hub" id="content">
<h1>Interview cheatsheet</h1>
<p class="lede">Search by the question, or open a category. Company packs are gone. The useful questions from them are filed here, with the common questions that belong next to them.</p>
<div class="cards">{''.join(cards)}</div>
<p class="foot">English and Tiếng Việt on every answer. Press / to search.</p>
</main>"""
    return shell("hub", "Interview cheatsheet", "index.html", body)


def redirect(target: str, label: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8" />
<meta http-equiv="refresh" content="0; url={esc(target)}" />
<link rel="canonical" href="{esc(target)}" />
<title>Moved — {esc(label)}</title></head>
<body><p>This page moved to <a href="{esc(target)}">{esc(label)}</a>.</p></body></html>
"""


def main() -> None:
    cards: list[dict] = []
    cards += extract_standard("fit", "fit.html")
    cards += extract_standard("soft", "soft-skills.html")
    cards += extract_standard("engineering", "engineering.html")
    cards += extract_standard("devops", "devops.html")
    cards += extract_standard("cv", "cv.html")
    cards += extract_standard("kaopiz", "kaopiz.html")
    cards += extract_go1()
    cards += new_cards()
    print(f"extracted {len(cards)}")
    cards = dedupe(cards)
    index_rows: list[dict] = []
    counts: dict[str, int] = {}
    for href, pid, label, blurb in PAGES:
        page_cards = [c for c in cards if c["page"] == pid]
        counts[pid] = len(page_cards)
        (ROOT / href).write_text(render_page(href, pid, label, blurb, cards, index_rows), encoding="utf-8")
        print(f"{href}: {len(page_cards)}")
    (ROOT / "index.html").write_text(render_hub(counts), encoding="utf-8")
    (ROOT / "assets" / "search-index.js").write_text(
        "window.CHEAT_SEARCH = " + json.dumps(index_rows, ensure_ascii=False) + ";\n",
        encoding="utf-8",
    )
    moves = {
        "engineering.html": ("react.html", "React and TypeScript"),
        "soft-skills.html": ("behavioral.html", "Behavioral"),
        "globant.html": ("index.html", "the hub"),
        "kaopiz.html": ("devops.html", "DevOps and cloud"),
        "go1-leadership.html": ("behavioral.html", "Behavioral"),
        "go1-en.html": ("index.html", "the hub"),
        "go1-vi.html": ("index.html", "the hub"),
        "vnpt-devops.html": ("devops.html", "DevOps and cloud"),
    }
    for name, (target, label) in moves.items():
        (ROOT / name).write_text(redirect(target, label), encoding="utf-8")
    missing_vi = [c["id"] for c in cards if c["id"].startswith("go1-") and not clean_text(c["a_vi"])]
    print("go1 missing vi", missing_vi)
    print("total", sum(counts.values()))
    for href, _pid, _label, _blurb in PAGES:
        text = (ROOT / href).read_text(encoding="utf-8")
        for name in ("Globant", "Kaopiz", "Go1", "Jasneet", "Junaid", "VNPT"):
            count = text.count(name)
            if count:
                print(f"leftover {name} x{count} in {href}")


if __name__ == "__main__":
    main()

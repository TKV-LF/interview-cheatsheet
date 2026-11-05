#!/usr/bin/env python3
"""Build every page, the hub, and the search index from _build/data/*.json.

The JSON files are the source of truth. Edit them, then run:

    python3 _build/build.py          # write the site
    python3 _build/build.py --check  # validate only, write nothing
"""
from __future__ import annotations

import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "_build" / "data"

# (file stem, nav label, hub blurb). Order is nav order and hub order.
SUBJECT_PAGES = [
    ("fit", "Fit and intro", "Who you are, why this role, why you are looking, and the HR questions."),
    ("behavioral", "Behavioral", "Stories, judgement, teamwork, Agile, and how you use AI."),
    ("english", "Spoken English", "Phrases for the minutes around the technical answer."),
    ("cv", "CV and projects", "PhysioFix, Aquanix, IELTS, Akktis, and BaseVN. Walk the real work."),
    ("javascript", "JS and TypeScript", "The language questions that come before any framework."),
    ("react", "React", "React core, hooks, performance, React Native, and the libraries you can defend."),
    ("node", "Node.js", "The event loop, Express, auth, and the server work you have shipped."),
    ("php", "PHP and MySQL", "Laravel, pure PHP, MySQL, and SQL you can write on a whiteboard."),
    ("system-design", "System design", "A simple path first. Scale only the part that breaks."),
    ("devops", "DevOps and cloud", "What you have operated, then the fundamentals and cloud around it."),
    ("debugging", "Debugging", "Decide the layer, then prove it before you change code."),
]
COMPANY_PAGES = [
    ("cyberk", "Cyberk", "TypeScript full-stack for client products in AI, fintech, and Web3. LLMs and AI tools you can defend; Nest, Postgres, Redis, and Web3 you name as a ramp.", "Current"),
    ("intowell", "INTOWELL", "Fullstack on Dr.AI and Vet.AI. Node you can defend. Vue and Ionic you name as a ramp.", "Earlier"),
    ("qnap", "QNAP", "Partner Portal and Sales Portal. Chinese first, then PHP, Laravel, React, and MySQL.", "Past · 30 Oct"),
]
ALL_PAGES = [p[0] for p in SUBJECT_PAGES] + [p[0] for p in COMPANY_PAGES]
LABELS = {p[0]: p[1] for p in SUBJECT_PAGES + COMPANY_PAGES}

REDIRECTS = {
    "engineering.html": ("react.html", "React"),
    "soft-skills.html": ("behavioral.html", "Behavioral"),
    "globant.html": ("index.html", "the hub"),
    "kaopiz.html": ("devops.html", "DevOps and cloud"),
    "go1-leadership.html": ("behavioral.html", "Behavioral"),
    "go1-en.html": ("index.html", "the hub"),
    "go1-vi.html": ("index.html", "the hub"),
    "vnpt-devops.html": ("devops.html", "DevOps and cloud"),
}

CARD_KEYS = {"id", "title", "hint", "q_en", "a_en", "q_vi", "a_vi", "notes", "body", "keywords", "open"}
TAG_RE = re.compile(r"<[^>]+>")
WORDS_PER_MINUTE = 140


def esc(value: str) -> str:
    return html.escape(value or "", quote=True)


def clean_text(raw: str) -> str:
    text = TAG_RE.sub(" ", raw or "")
    text = html.unescape(text)
    return re.sub(r"\s+", " ", text).strip()


def plain(card: dict) -> str:
    parts = [card.get(k, "") for k in ("title", "hint", "q_en", "a_en", "q_vi", "a_vi", "body", "notes", "keywords")]
    return clean_text(" ".join(parts))


def speak_seconds(card: dict) -> int:
    words = len(clean_text(card.get("a_en", "")).split())
    return round(words / WORDS_PER_MINUTE * 60)


def slug(name: str) -> str:
    return "sec-" + re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def load() -> dict[str, dict]:
    pages = {}
    for stem in ALL_PAGES:
        path = DATA / f"{stem}.json"
        pages[stem] = json.loads(path.read_text(encoding="utf-8"))
    return pages


def validate(pages: dict[str, dict]) -> list[str]:
    errors = []
    seen: dict[str, str] = {}
    for stem, page in pages.items():
        for sec in page["sections"]:
            if not sec.get("name"):
                errors.append(f"{stem}: section without a name")
            for card in sec["cards"]:
                cid = card.get("id", "")
                if not cid or not re.fullmatch(r"[a-z0-9][a-z0-9-]*", cid):
                    errors.append(f"{stem}: bad card id {cid!r}")
                if cid in seen:
                    errors.append(f"{stem}: duplicate id {cid} (also on {seen[cid]})")
                seen[cid] = stem
                extra = set(card) - CARD_KEYS
                if extra:
                    errors.append(f"{stem}/{cid}: unknown keys {sorted(extra)}")
                if not card.get("title"):
                    errors.append(f"{stem}/{cid}: no title")
                if "body" not in card:
                    for key in ("q_en", "a_en", "q_vi", "a_vi"):
                        if not clean_text(card.get(key, "")):
                            errors.append(f"{stem}/{cid}: empty {key}")
                for key in ("q_en", "a_en", "q_vi", "a_vi", "notes", "body"):
                    value = card.get(key, "")
                    if value.count("<div") != value.count("</div>"):
                        errors.append(f"{stem}/{cid}: unbalanced <div> in {key}")
    # Links to other cards must resolve.
    for stem, page in pages.items():
        for sec in page["sections"]:
            for card in sec["cards"]:
                blob = " ".join(str(card.get(k, "")) for k in ("a_en", "a_vi", "notes", "body"))
                for target, anchor in re.findall(r'href="([a-z-]+)\.html#([^"]+)"', blob):
                    if target in pages and anchor not in seen and not anchor.startswith("sec-"):
                        errors.append(f"{stem}/{card['id']}: broken link {target}.html#{anchor}")
    return errors


def render_card(card: dict, number: int) -> str:
    blob = esc(plain(card).lower())
    opened = " open" if card.get("open") else ""
    hint = f'<span class="q-hint">{esc(card["hint"])}</span>' if card.get("hint") else ""
    secs = speak_seconds(card)
    timing = f'<span class="q-time" title="About how long the English answer takes to say">~{secs}s</span>' if secs else ""
    notes = f'<div class="notes">{card["notes"]}</div>' if clean_text(card.get("notes", "")) else ""
    if "body" in card:
        inner = f'<div class="ans">{card["body"]}</div>'
    else:
        inner = (
            '<div class="lang"><button type="button" data-set-lang="en">English</button>'
            '<button type="button" data-set-lang="vi">Tiếng Việt</button></div>\n'
            f'<div data-pane="en"><div class="ask">{card["q_en"]}</div><div class="ans">{card["a_en"]}</div></div>\n'
            f'<div data-pane="vi" hidden><div class="ask">{card["q_vi"]}</div><div class="ans">{card["a_vi"]}</div></div>'
        )
    cid = esc(card["id"])
    return f"""<details class="q" id="{cid}"{opened} data-blob="{blob}">
<summary><span class="num">{number:02d}</span><span class="q-head"><span class="q-title">{esc(card["title"])}</span>{hint}</span><span class="q-meta">{timing}<span class="q-known" aria-hidden="true">✓</span></span></summary>
<div class="q-body">
{inner}
{notes}
<div class="q-tools"><button type="button" class="reveal" data-reveal>Show answer</button><label class="known-toggle"><input type="checkbox" data-known> I can say this</label></div>
</div>
</details>"""


HEAD_SCRIPT = """<script>(function(){try{var t=localStorage.getItem("cheat-theme")||(matchMedia("(prefers-color-scheme: dark)").matches?"dark":"light");document.documentElement.setAttribute("data-theme",t);}catch(e){}})();</script>"""


def shell(page_id: str, title: str, active: str, body: str) -> str:
    links = [("index.html", "Hub", "")]
    links += [(f"{stem}.html", label, "nav-company") for stem, label, _, _ in COMPANY_PAGES]
    links += [(f"{stem}.html", label, "nav-subject") for stem, label, _ in SUBJECT_PAGES]
    nav = "\n".join(
        f'<a href="{href}" class="{" ".join(c for c in (cls, "is-on" if href == active else "") if c)}"'
        f'{" aria-current=\"page\"" if href == active else ""}>{esc(label)}</a>'
        for href, label, cls in links
    )
    return f"""<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{esc(title)}</title>
{HEAD_SCRIPT}
<link href="https://api.fontshare.com/v2/css?f[]=satoshi@400,500,700&f[]=general-sans@500,600,700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/site.css" />
</head>
<body data-page="{esc(page_id)}">
<a class="skip" href="#content">Skip to questions</a>
<header class="topbar">
<div class="topbar-inner">
<a class="brand" href="index.html">Interview cheatsheet</a>
<div class="search-wrap">
<span class="mag" aria-hidden="true">⌕</span>
<input data-search type="search" placeholder="Search all questions — press /" aria-label="Search questions" />
<div class="hits" data-hits></div>
<p class="search-meta" data-search-meta></p>
</div>
<div class="brand-actions">
<button class="icon-btn nav-toggle" type="button" data-nav-toggle aria-label="Open menu" aria-expanded="false" aria-controls="site-nav"><span class="nav-toggle-bars" aria-hidden="true"></span></button>
<button class="icon-btn" type="button" data-theme-toggle aria-label="Switch theme">☾</button>
</div>
</div>
<nav class="nav-scroll" id="site-nav" aria-label="Categories">{nav}</nav>
</header>
{body}
<script src="assets/search-index.js"></script>
<script src="assets/site.js"></script>
</body>
</html>
"""


def render_page(stem: str, page: dict, index_rows: list[dict]) -> str:
    href = f"{stem}.html"
    label = LABELS[stem]
    side = ['<button type="button" class="side-toggle" data-side-toggle aria-expanded="false">On this page</button><div class="side-list"><h2>On this page</h2>']
    main = [f'<header class="page-intro"><h1>{esc(page["title"])}</h1><p>{page["intro"]}</p></header>']
    main.append(
        '<div class="toolbar">'
        '<button type="button" data-expand="open">Expand all</button>'
        '<button type="button" data-expand="close">Collapse all</button>'
        '<button type="button" data-practice aria-pressed="false" title="Hide answers until you try to say them">Practice mode</button>'
        '<button type="button" data-hide-known aria-pressed="false">Hide what I know</button>'
        '<span class="progress" data-progress></span>'
        "</div>"
    )
    number = 1
    for sec in page["sections"]:
        sec_id = sec.get("id") or slug(sec["name"])
        side.append(f'<a class="sec-link" data-sec href="#{sec_id}">{esc(sec["name"])}</a>')
        main.append(f'<section class="block" id="{sec_id}"><h2>{esc(sec["name"])}</h2>')
        if sec.get("html"):
            main.append(sec["html"])
        for card in sec["cards"]:
            side.append(f'<a class="q-link" href="#{esc(card["id"])}">{number:02d} {esc(card["title"])}</a>')
            main.append(render_card(card, number))
            index_rows.append({
                "page": page["page"],
                "category": label,
                "title": card["title"],
                "href": f"{href}#{card['id']}",
                "text": plain(card),
            })
            number += 1
        main.append("</section>")
    side.append("</div>")
    body = (
        f'<div class="shell"><aside class="side" data-side>{"".join(side)}</aside>'
        f'<main id="content">{"".join(main)}</main></div>'
    )
    return shell(page["page"], f"{page['title']} — Interview cheatsheet", href, body)


def count(page: dict) -> int:
    return sum(len(s["cards"]) for s in page["sections"])


def render_hub(pages: dict[str, dict]) -> str:
    def card(stem: str, label: str, blurb: str, kicker: str) -> str:
        return (
            f'<a class="card" href="{stem}.html"><span class="kicker">{esc(kicker)}</span>'
            f"<h2>{esc(label)}</h2><p>{esc(blurb)}</p></a>"
        )

    company = "".join(
        card(stem, label, blurb, f"{tag} · {count(pages[stem])} questions") for stem, label, blurb, tag in COMPANY_PAGES
    )
    subject = "".join(card(stem, label, blurb, f"{count(pages[stem])} questions") for stem, label, blurb in SUBJECT_PAGES)
    total = sum(count(p) for p in pages.values())
    body = f"""<main class="hub" id="content">
<h1>Interview cheatsheet</h1>
<p class="lede">{total} questions. Search by the words you heard, or open a subject. Every answer has English and Tiếng Việt, and an estimate of how long it takes to say. Use Practice mode to try the answer out loud before you read it.</p>
<h2 class="hub-h">Company pages</h2>
<div class="cards">{company}</div>
<h2 class="hub-h">By subject</h2>
<div class="cards">{subject}</div>
<p class="foot">Press / to search from any page. Ticks for “I can say this” stay in this browser.</p>
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
    check_only = "--check" in sys.argv
    pages = load()
    errors = validate(pages)
    if errors:
        print("\n".join(errors))
        sys.exit(1)
    long_cards = [
        (stem, c["id"], speak_seconds(c))
        for stem, p in pages.items() for s in p["sections"] for c in s["cards"] if speak_seconds(c) > 100
    ]
    if long_cards:
        print(f"note: {len(long_cards)} answers run past 100 seconds:")
        for stem, cid, secs in long_cards:
            print(f"  {stem}/{cid} ~{secs}s")
    if check_only:
        print(f"ok: {sum(count(p) for p in pages.values())} cards")
        return
    index_rows: list[dict] = []
    for stem in ALL_PAGES:
        (ROOT / f"{stem}.html").write_text(render_page(stem, pages[stem], index_rows), encoding="utf-8")
        print(f"{stem}.html: {count(pages[stem])}")
    (ROOT / "index.html").write_text(render_hub(pages), encoding="utf-8")
    (ROOT / "assets" / "search-index.js").write_text(
        "window.CHEAT_SEARCH = " + json.dumps(index_rows, ensure_ascii=False) + ";\n", encoding="utf-8"
    )
    for name, (target, label) in REDIRECTS.items():
        (ROOT / name).write_text(redirect(target, label), encoding="utf-8")
    print("total", sum(count(p) for p in pages.values()))


if __name__ == "__main__":
    main()

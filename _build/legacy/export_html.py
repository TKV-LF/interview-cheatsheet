#!/usr/bin/env python3
"""One-off: turn the committed HTML pages into _build/data/<page>.json."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "_build" / "data"
PAGES = ["fit", "behavioral", "english", "php", "react", "node", "devops",
         "debugging", "system-design", "cv", "qnap", "intowell"]

CARD_RE = re.compile(
    r'<details class="q" id="(?P<id>[^"]+)"(?P<open> open)? data-blob="(?P<blob>[^"]*)">\n'
    r'<summary><span class="num">\d+</span><span><span class="q-title">(?P<title>.*?)</span>'
    r'(?:<span class="q-hint">(?P<hint>.*?)</span>)?</span></summary>\n'
    r'<div class="q-body">\n(?P<body>.*?)\n?</div>\n</details>',
    re.S,
)
PANES_RE = re.compile(
    r'^<div class="lang">.*?</div>\n'
    r'<div data-pane="en"><div class="ask">(?P<q_en>.*?)</div><div class="ans">(?P<a_en>.*?)</div></div>\n'
    r'<div data-pane="vi" hidden><div class="ask">(?P<q_vi>.*?)</div><div class="ans">(?P<a_vi>.*?)</div></div>\n?'
    r'(?P<rest>.*)$',
    re.S,
)
NOTES_RE = re.compile(r'<div class="notes">(?P<notes>.*)</div>\s*$', re.S)


def parse_card(cm) -> dict:
    import html
    c = {"id": cm.group("id"), "title": html.unescape(cm.group("title")), "hint": html.unescape(cm.group("hint") or "")}
    body = cm.group("body")
    pm = PANES_RE.match(body)
    if pm:
        for k in ("q_en", "a_en", "q_vi", "a_vi"):
            c[k] = pm.group(k).strip()
        rest = pm.group("rest").strip()
    else:
        rest = body.strip()
    nm = NOTES_RE.search(rest)
    if nm:
        c["notes"] = nm.group("notes").strip()
        rest = rest[: nm.start()].strip()
    else:
        c["notes"] = ""
    if rest:
        assert not pm, (c["id"], rest[:200])
        c["body"] = rest
    blob = html.unescape(cm.group("blob"))
    if c["id"].startswith(("qnap-", "intowell-")) and len(blob) < 400:
        c["keywords"] = blob
    if cm.group("open"):
        c["open"] = True
    return c


SEC_RE = re.compile(r'<section class="block" id="(?P<id>[^"]+)">\s*<h2>(?P<name>.*?)</h2>(?P<body>.*?)</section>', re.S)


def unesc(s: str) -> str:
    import html
    return html.unescape(s)


def main() -> None:
    for page in PAGES:
        raw = (ROOT / f"{page}.html").read_text(encoding="utf-8")
        pid = re.search(r'<body data-page="([^"]+)"', raw).group(1)
        title = unesc(re.search(r"<h1>(.*?)</h1>", raw, re.S).group(1))
        intro = re.search(r'<header class="page-intro"><h1>.*?</h1><p>(.*?)</p></header>', raw, re.S).group(1)
        sections = []
        for sm in SEC_RE.finditer(raw):
            body = sm.group("body")
            cards = []
            for cm in CARD_RE.finditer(body):
                cards.append(parse_card(cm))
            pre = CARD_RE.sub("", body).strip()
            sec = {"id": sm.group("id"), "name": unesc(sm.group("name")), "cards": cards}
            if pre:
                sec["html"] = pre
            sections.append(sec)
        n = sum(len(s["cards"]) for s in sections)
        assert n == raw.count('<details class="q"'), (page, n)
        (DATA / f"{page}.json").write_text(json.dumps(
            {"page": pid, "href": f"{page}.html", "title": title, "intro": intro, "sections": sections},
            ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print(page, len(sections), n)


if __name__ == "__main__":
    main()

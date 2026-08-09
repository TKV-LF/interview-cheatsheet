#!/usr/bin/env python3
"""Generate vnpt-devops.html from globant CSS/JS shell + card data modules."""
from __future__ import annotations

import html as H
from pathlib import Path

ROOT = Path("/Users/thuynt/Working/Vibe/interview-cheatsheet")
OUT = ROOT / "vnpt-devops.html"
HEAD = Path("/tmp/vnpt_head.css.html")
SCRIPT = Path("/tmp/vnpt_script.js.html")

from cards_part1a import CARDS as C1A  # noqa: E402
from cards_part1b import CARDS as C1B  # noqa: E402
from cards_part1c import CARDS as C1C  # noqa: E402
from cards_part2 import CARDS as C2  # noqa: E402
from cards_tips_mcq import CARDS as CTIPS  # noqa: E402

SECTIONS = [
    ("sec-jd", "0 · JD map", "Part 0 · JD map"),
    ("sec-tips", "0b · Exam tips + MCQ (VNPTips #2)", "Part 0b · Exam tips + MCQ"),
    ("sec-devops", "1 · IT & DevOps fundamentals", "Part 1 · IT & DevOps"),
    ("sec-linux", "2 · Linux essentials", "Part 2 · Linux"),
    ("sec-os", "3 · OS fundamentals", "Part 3 · OS fundamentals"),
    ("sec-network", "4 · Network basics", "Part 4 · Network"),
    ("sec-security", "5 · Security / ATTT", "Part 5 · Security / ATTT"),
    ("sec-git", "6 · Git + collaboration", "Part 6 · Git + collab"),
    ("sec-cicd", "7 · CI/CD Jenkins/GitLab", "Part 7 · CI/CD"),
    ("sec-automation", "8 · Automation Ansible/Bash/Python", "Part 8 · Automation"),
    ("sec-docker", "9 · Containers Docker", "Part 9 · Docker"),
    ("sec-k8s", "10 · Kubernetes + HA", "Part 10 · Kubernetes + HA"),
    ("sec-web", "11 · Web servers Nginx/Apache", "Part 11 · Web servers"),
    ("sec-monitor", "12 · Monitoring Prometheus/Grafana/ELK", "Part 12 · Monitoring"),
    ("sec-backup", "13 · Backup & recovery", "Part 13 · Backup & recovery"),
    ("sec-arch", "14 · System architecture", "Part 14 · Architecture"),
    ("sec-lang", "15 · Languages for DevOps", "Part 15 · Languages"),
    ("sec-ai", "16 · AI/LLM in DevOps", "Part 16 · AI/LLM"),
    ("sec-fit", "17 · Fit / intro", "Part 17 · Fit / intro"),
    ("sec-scenario", "18 · Scenario questions", "Part 18 · Scenarios"),
    ("sec-close", "19 · Closing", "Part 19 · Closing"),
]


def esc(s: str) -> str:
    return H.escape(s or "", quote=False)


def p_html(text: str) -> str:
    parts = [f"<p>{esc(p)}</p>" for p in text.split("\n\n") if p.strip()]
    return "".join(parts) if parts else "<p></p>"


def p_br(text: str) -> str:
    """Paragraphs on blank lines; single newlines become <br> (for MCQ options)."""
    parts = []
    for para in text.split("\n\n"):
        if not para.strip():
            continue
        parts.append("<p>" + "<br>\n".join(esc(line) for line in para.split("\n")) + "</p>")
    return "".join(parts) if parts else "<p></p>"


def note_html(text: str) -> str:
    lines = text.split("\n")
    body = "<br>\n".join(esc(line) for line in lines)
    return (
        '<div class="note"><p><strong>Commands / examples:</strong></p>'
        f'<p style="font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:0.85em">{body}</p></div>\n'
    )


def render_concept(num: int, card: dict) -> str:
    cid = f"v{num}"
    out = [
        f'<article class="question-card" id="{cid}">',
        f'  <div class="question-head"><h2>{num:02d}. {esc(card["title"])}</h2><p>{esc(card.get("sub", ""))}</p></div>',
        '  <div class="grid4">',
        '    <div class="cell row-head">Concept EN</div><div class="cell row-head">Must-know EN</div>'
        '<div class="cell row-head">Concept VI</div><div class="cell row-head">Must-know VI</div>',
        f'    <div class="cell question">{p_html(card["c_en"])}</div>',
        f'    <div class="cell answer">{p_html(card["m_en"])}</div>',
        f'    <div class="cell question">{p_html(card["c_vi"])}</div>',
        f'    <div class="cell answer">{p_html(card["m_vi"])}</div>',
        "  </div>",
    ]
    if card.get("crib"):
        out.append(f'  <div class="crib"><p><strong>Exam trap:</strong> {esc(card["crib"])}</p></div>')
    if card.get("note"):
        out.append(note_html(card["note"]))
    out.append("</article>")
    return "\n".join(out)


def render_interview(num: int, card: dict) -> str:
    cid = f"v{num}"
    out = [
        f'<article class="question-card" id="{cid}">',
        f'  <div class="question-head"><h2>{num:02d}. {esc(card["title"])}</h2><p>{esc(card.get("sub", ""))}</p></div>',
        '  <div class="grid4">',
        '    <div class="cell row-head">Question EN</div><div class="cell row-head">Answer EN</div>'
        '<div class="cell row-head">Question VI</div><div class="cell row-head">Answer VI</div>',
        f'    <div class="cell question">{p_html(card["q_en"])}</div>',
        f'    <div class="cell answer">{p_html(card["a_en"])}</div>',
        f'    <div class="cell question">{p_html(card["q_vi"])}</div>',
        f'    <div class="cell answer">{p_html(card["a_vi"])}</div>',
        "  </div>",
    ]
    if card.get("star"):
        bullets = "".join(f"<p>{esc(line)}</p>" for line in card["star"].split("\n") if line.strip())
        out.append(f'  <div class="star"><p><strong>STAR bullets:</strong></p>{bullets}</div>')
    out.append("</article>")
    return "\n".join(out)


def render_mcq(num: int, card: dict) -> str:
    cid = f"v{num}"
    q_en = f"{card['q_en']}\n\n{card['opts_en']}"
    q_vi = f"{card['q_vi']}\n\n{card['opts_vi']}"
    out = [
        f'<article class="question-card" id="{cid}">',
        f'  <div class="question-head"><h2>{num:02d}. {esc(card["title"])}</h2>'
        f'<p>MCQ · {esc(card.get("sub", ""))}</p></div>',
        '  <div class="grid4">',
        '    <div class="cell row-head">Question EN</div><div class="cell row-head">Answer EN</div>'
        '<div class="cell row-head">Question VI</div><div class="cell row-head">Answer VI</div>',
        f'    <div class="cell question">{p_br(q_en)}</div>',
        f'    <div class="cell answer">{p_br(card["ans_en"])}</div>',
        f'    <div class="cell question">{p_br(q_vi)}</div>',
        f'    <div class="cell answer">{p_br(card["ans_vi"])}</div>',
        "  </div>",
    ]
    if card.get("crib"):
        out.append(
            f'  <div class="crib"><p><strong>Elimination tip:</strong> {esc(card["crib"])}</p></div>'
        )
    out.append("</article>")
    return "\n".join(out)


def main() -> None:
    # Tips/MCQ inserted after JD map cards for study order
    jd = [c for c in C1A if c["sec"] == "sec-jd"]
    rest_a = [c for c in C1A if c["sec"] != "sec-jd"]
    cards = jd + list(CTIPS) + rest_a + list(C1B) + list(C1C) + list(C2)
    by_sec: dict[str, list[tuple[int, dict]]] = {sid: [] for sid, _, _ in SECTIONS}
    for i, card in enumerate(cards, start=1):
        by_sec[card["sec"]].append((i, card))

    toc_bits = []
    for sid, _label, part_name in SECTIONS:
        items = by_sec[sid]
        if not items:
            continue
        first, last = items[0][0], items[-1][0]
        toc_bits.append(
            f'        <div class="side-toc-part" data-part="{sid}">\n'
            f'          <a class="side-toc-part-link" href="#{sid}">{esc(part_name)}</a>\n'
            f'          <span class="side-toc-part-range">V{first:02d}–{last:02d}</span>\n'
            f"        </div>"
        )
        for num, card in items:
            toc_bits.append(
                f'        <a class="side-toc-link" href="#v{num}" data-target="v{num}" data-part="{sid}">'
                f'<span class="side-toc-num">{num:02d}</span>'
                f'<span class="side-toc-title">{esc(card["title"])}</span></a>'
            )

    rail_bits = []
    for sid, _label, part_name in SECTIONS:
        items = by_sec[sid]
        if not items:
            continue
        first, last = items[0][0], items[-1][0]
        rail_bits.append(
            f'        <a class="parts-rail-link" href="#{sid}" data-part="{sid}">'
            f"<strong>{esc(part_name)}</strong><span>V{first:02d}–{last:02d}</span></a>"
        )

    nav = "".join(
        f'<a href="#{sid}">{esc(label.split("·", 1)[-1].strip()[:22])}</a>\n          '
        for sid, label, _ in SECTIONS
    )

    body_bits = ['            <section class="questions">']
    for sid, label, _part in SECTIONS:
        items = by_sec[sid]
        if not items:
            continue
        body_bits.append(f'    <section class="section-block" id="{sid}">')
        body_bits.append(f"      <h2>{esc(label)}</h2>")
        for num, card in items:
            kind = card["kind"]
            if kind == "interview":
                body_bits.append(render_interview(num, card))
            elif kind == "mcq":
                body_bits.append(render_mcq(num, card))
            else:
                body_bits.append(render_concept(num, card))
        body_bits.append("    </section>")
    body_bits.append("    </section>")

    total = len(cards)
    nsec = sum(1 for sid, _, _ in SECTIONS if by_sec[sid])
    head = HEAD.read_text().replace(
        "Globant Fullstack PHP + React Interview Prep",
        "VNPT DevOps Fundamentals + Interview Prep",
    )
    ux_css = (Path(__file__).with_name("ux_overrides.css")).read_text()
    if "</style>" in head:
        head = head.replace("</style>", ux_css + "\n</style>", 1)
    script = SCRIPT.read_text()
    # UX_JS_INJECTED
    _ux_js = """
      // Parts rail collapse (desktop) + mobile drawer close
      const partsRail = document.getElementById('parts-rail');
      const railHideBtn = document.querySelector('[data-parts-rail-toggle]');
      const railShowBtn = document.querySelector('[data-parts-rail-show]');
      const tocCloseBtn = document.querySelector('[data-toc-close]');
      const RAIL_KEY = 'vnpt-parts-rail-collapsed';

      const setRailCollapsed = (collapsed) => {
        document.body.classList.toggle('parts-rail-collapsed', collapsed);
        if (railHideBtn) {
          railHideBtn.setAttribute('aria-expanded', collapsed ? 'false' : 'true');
          railHideBtn.setAttribute('aria-label', collapsed ? 'Show parts rail' : 'Hide parts rail');
          railHideBtn.title = collapsed ? 'Show parts' : 'Hide parts';
        }
        if (railShowBtn) {
          railShowBtn.hidden = !collapsed;
          railShowBtn.setAttribute('aria-hidden', collapsed ? 'false' : 'true');
        }
        try { localStorage.setItem(RAIL_KEY, collapsed ? '1' : '0'); } catch (_) {}
      };

      if (partsRail && railHideBtn && railShowBtn) {
        let collapsed = false;
        try { collapsed = localStorage.getItem(RAIL_KEY) === '1'; } catch (_) {}
        setRailCollapsed(collapsed);
        railHideBtn.addEventListener('click', () => setRailCollapsed(true));
        railShowBtn.addEventListener('click', () => setRailCollapsed(false));
      }

      tocCloseBtn && tocCloseBtn.addEventListener('click', closeMobile);
"""
    if "})();" in script:
        script = script.replace("})();", _ux_js + "\n    })();", 1)

    html: list[str] = [head.rstrip()]
    if "</head>" not in head:
        html.append("</head>")
    html.append('<body class="has-side-toc">')
    html.append(
        """  <div class="topbar">
    <div class="topbar-inner">
      <div class="brand">
        <h1>VNPT · DevOps Engineer</h1>
        <p>VNPTips #2: vòng thi thường là trắc nghiệm — theory + tình huống + ứng dụng DevOps. Then spoken EN/VI interview prep.</p>
      </div>
      <div class="top-actions">
        <button class="btn toc-mobile-btn" data-toc-open type="button">Contents</button>
        <button class="btn theme-toggle" data-theme-toggle aria-label="Switch theme">☾</button>
        <a class="btn btn-link-secondary" href="index.html">Cloud</a>
        <a class="btn btn-link-secondary" href="globant.html">Globant</a>
        <a class="btn btn-link-secondary" href="cv.html">CV</a>
      </div>
    </div>
  </div>
    <div class="toc-backdrop" data-toc-backdrop hidden></div>
  <div class="shell">
    <aside class="side-toc" id="side-toc" aria-label="Question contents">
      <button class="side-toc-close" data-toc-close type="button" aria-label="Close contents">×</button>
      <div class="side-toc-head">
        <strong>Contents</strong>
        <span>Full list · JD → Exam tips/MCQ → fundamentals → interview</span>
      </div>
      <nav class="side-toc-list" data-side-toc>
"""
    )
    html.append("\n".join(toc_bits))
    html.append(
        """
      </nav>
    </aside>
    <aside class="parts-rail" id="parts-rail" aria-label="Parts only">
      <div class="parts-rail-head-row">
        <p class="parts-rail-head">Parts</p>
        <button class="parts-rail-toggle" data-parts-rail-toggle type="button" aria-expanded="true" aria-controls="parts-rail" aria-label="Hide parts rail" title="Hide parts">›</button>
      </div>
      <nav class="parts-rail-list" data-parts-rail>
"""
    )
    html.append("\n".join(rail_bits))
    html.append(
        f"""
      </nav>
    </aside>
    <button class="parts-rail-show" data-parts-rail-show type="button" hidden aria-label="Show parts rail">‹ Parts</button>
  <main class="page with-side-toc">
    <section class="hero with-side-toc">
      <div class="hero-card">
        <div class="section-label">VNPT DevOps prep</div>
        <p>Per VNPTips #2: prepare for <strong>trắc nghiệm</strong> (theory + situational + job-applied), use elimination/time strategy, then interview fit/scenarios. Hands-on voice on CI/CD, Docker/K8s, monitoring — AI/LLM as practical assistants only.</p>
        <nav class="section-nav" aria-label="Sections">
          {nav}
        </nav>
        <div class="hero-kpis">
          <div class="kpi"><strong>{total}</strong><span>Bilingual cards</span></div>
          <div class="kpi"><strong>{nsec}</strong><span>Sections</span></div>
          <div class="kpi"><strong>MCQ</strong><span>Trắc nghiệm drills</span></div>
        </div>
        <div class="tag-list">
          <span class="tag">Trắc nghiệm</span><span class="tag">VNPTips #2</span>
          <span class="tag">Jenkins</span><span class="tag">GitLab</span><span class="tag">Docker</span><span class="tag">Kubernetes</span>
          <span class="tag">Ansible</span><span class="tag">Prometheus</span><span class="tag">Grafana</span><span class="tag">ELK</span>
          <span class="tag">Nginx</span><span class="tag">ATTT</span><span class="tag">AI/LLM</span>
        </div>
      </div>
      <aside class="toc-card" id="toc">
        <div class="section-label">Table of contents</div>
        <p>Tonight: <a href="#sec-tips">Exam tips + MCQ</a> → Linux/OS/Network/Security → CI/CD → Docker/K8s → Monitoring. Easy questions first; mark hard ones; review before submit.</p>
      </aside>
    </section>
"""
    )
    html.append("\n".join(body_bits))
    html.append(
        """
    <p class="footer-note"><a href="index.html">Cloud/infra sheet</a> · <a href="cv.html">CV stories</a> · <a href="globant.html">PHP/React sheet</a> · VNPT DevOps fundamentals — honest hands-on voice.</p>
  </main>
  </div>
"""
    )
    html.append(script)
    html.append("</body>\n</html>\n")

    OUT.write_text("\n".join(html), encoding="utf-8")
    print(f"Wrote {OUT} cards={total} bytes={OUT.stat().st_size} lines={sum(1 for _ in OUT.open())}")


if __name__ == "__main__":
    main()

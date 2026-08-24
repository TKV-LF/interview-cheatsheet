#!/usr/bin/env python3
"""Generate devops.html — general DevOps prep grounded in real experience."""
from __future__ import annotations

import html as H
from pathlib import Path

ROOT = Path("/Users/thuynt/Working/Vibe/interview-cheatsheet")
OUT = ROOT / "devops.html"
HEAD = Path("/tmp/devops_head.css.html")
SCRIPT = Path("/tmp/devops_script.js.html")

from cards_experience import CARDS as CEXP  # noqa: E402
from cards_fundamentals import CARDS as CFUND  # noqa: E402
from cards_interview import CARDS as CINT  # noqa: E402

SECTIONS = [
    ("sec-overview", "0 · My DevOps experience", "Part 0 · Experience map"),
    ("sec-mobile-cicd", "1 · Mobile CI/CD (Android / iOS)", "Part 1 · Mobile CI/CD"),
    ("sec-cloudrun", "2 · Cloud Run + Cloud Build", "Part 2 · Cloud Run / Build"),
    ("sec-linux-vm", "3 · Linux VM web server", "Part 3 · Linux VM"),
    ("sec-devops", "4 · DevOps fundamentals", "Part 4 · DevOps basics"),
    ("sec-linux", "5 · Linux essentials", "Part 5 · Linux"),
    ("sec-git", "6 · Git + collaboration", "Part 6 · Git"),
    ("sec-docker", "7 · Docker for Cloud Run", "Part 7 · Docker"),
    ("sec-gcp", "8 · GCP mental model", "Part 8 · GCP"),
    ("sec-web", "9 · Web servers", "Part 9 · Web servers"),
    ("sec-security", "10 · Security basics", "Part 10 · Security"),
    ("sec-fit", "11 · Fit / intro", "Part 11 · Fit"),
    ("sec-scenario", "12 · Scenario questions", "Part 12 · Scenarios"),
    ("sec-close", "13 · Closing", "Part 13 · Closing"),
]


def esc(s: str) -> str:
    return H.escape(s or "", quote=False)


def p_html(text: str) -> str:
    parts = [f"<p>{esc(p)}</p>" for p in text.split("\n\n") if p.strip()]
    return "".join(parts) if parts else "<p></p>"


def p_br(text: str) -> str:
    parts = []
    for para in text.split("\n\n"):
        if not para.strip():
            continue
        parts.append("<p>" + "<br>\n".join(esc(line) for line in para.split("\n")) + "</p>")
    return "".join(parts) if parts else "<p></p>"


def note_html(text: str) -> str:
    body = "<br>\n".join(esc(line) for line in text.split("\n"))
    return (
        '<div class="note"><p><strong>Commands / examples:</strong></p>'
        f'<p style="font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:0.85em">{body}</p></div>\n'
    )


def render_concept(num: int, card: dict) -> str:
    cid = f"d{num}"
    out = [
        f'<article class="question-card" id="{cid}">',
        f'  <div class="question-head"><h2>{num:02d}. {esc(card["title"])}</h2><p>{esc(card.get("sub", ""))}</p></div>',
        '  <div class="grid4">',
        '    <div class="cell row-head">Concept EN</div><div class="cell row-head">Steps / Must-know EN</div>'
        '<div class="cell row-head">Concept VI</div><div class="cell row-head">Steps / Must-know VI</div>',
        f'    <div class="cell question">{p_html(card["c_en"])}</div>',
        f'    <div class="cell answer">{p_br(card["m_en"])}</div>',
        f'    <div class="cell question">{p_html(card["c_vi"])}</div>',
        f'    <div class="cell answer">{p_br(card["m_vi"])}</div>',
        "  </div>",
    ]
    if card.get("crib"):
        out.append(f'  <div class="crib"><p><strong>Interview trap:</strong> {esc(card["crib"])}</p></div>')
    if card.get("note"):
        out.append(note_html(card["note"]))
    out.append("</article>")
    return "\n".join(out)


def render_interview(num: int, card: dict) -> str:
    cid = f"d{num}"
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


def main() -> None:
    # Experience first, then fundamentals, then interview
    cards = list(CEXP) + list(CFUND) + list(CINT)
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
            f'          <span class="side-toc-part-range">D{first:02d}–{last:02d}</span>\n'
            f"        </div>"
        )
        for num, card in items:
            toc_bits.append(
                f'        <a class="side-toc-link" href="#d{num}" data-target="d{num}" data-part="{sid}">'
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
            f"<strong>{esc(part_name)}</strong><span>D{first:02d}–{last:02d}</span></a>"
        )

    nav = "".join(
        f'<a href="#{sid}">{esc(label.split("·", 1)[-1].strip()[:28])}</a>\n          '
        for sid, label, _ in SECTIONS if by_sec[sid]
    )

    body_bits = ['            <section class="questions">']
    for sid, label, _part in SECTIONS:
        items = by_sec[sid]
        if not items:
            continue
        body_bits.append(f'    <section class="section-block" id="{sid}">')
        body_bits.append(f"      <h2>{esc(label)}</h2>")
        for num, card in items:
            if card["kind"] == "interview":
                body_bits.append(render_interview(num, card))
            else:
                body_bits.append(render_concept(num, card))
        body_bits.append("    </section>")
    body_bits.append("    </section>")

    total = len(cards)
    nsec = sum(1 for sid, _, _ in SECTIONS if by_sec[sid])
    head = HEAD.read_text().replace(
        "Globant Fullstack PHP + React Interview Prep",
        "DevOps Interview Prep — Real Experience",
    )
    ux_css = (Path(__file__).with_name("ux_overrides.css")).read_text()
    if "</style>" in head:
        head = head.replace("</style>", ux_css + "\n</style>", 1)
    script = SCRIPT.read_text()

    rail_script = """
<script>
(function () {
  const partsRail = document.getElementById('parts-rail');
  const hideBtn = document.querySelector('[data-parts-rail-toggle]');
  const showBtn = document.querySelector('[data-parts-rail-show]');
  const tocCloseBtn = document.querySelector('[data-toc-close]');
  const sideToc = document.getElementById('side-toc');
  const backdrop = document.querySelector('[data-toc-backdrop]');
  const RAIL_KEY = 'devops-parts-rail-collapsed';
  if (!partsRail || !hideBtn || !showBtn) return;

  const setCollapsed = (collapsed) => {
    document.body.classList.toggle('parts-rail-collapsed', !!collapsed);
    hideBtn.setAttribute('aria-expanded', collapsed ? 'false' : 'true');
    hideBtn.setAttribute('aria-label', collapsed ? 'Show parts panel' : 'Hide parts panel');
    hideBtn.title = collapsed ? 'Show parts' : 'Hide parts';
    if (collapsed) showBtn.removeAttribute('hidden');
    else showBtn.setAttribute('hidden', '');
    try { localStorage.setItem(RAIL_KEY, collapsed ? '1' : '0'); } catch (_) {}
  };

  let collapsed = false;
  try { collapsed = localStorage.getItem(RAIL_KEY) === '1'; } catch (_) {}
  setCollapsed(collapsed);

  hideBtn.addEventListener('click', (e) => { e.preventDefault(); e.stopPropagation(); setCollapsed(true); });
  showBtn.addEventListener('click', (e) => { e.preventDefault(); e.stopPropagation(); setCollapsed(false); });

  if (tocCloseBtn && sideToc) {
    tocCloseBtn.addEventListener('click', () => {
      sideToc.classList.remove('is-open');
      if (backdrop) { backdrop.classList.remove('is-open'); backdrop.hidden = true; }
    });
  }
})();
</script>
"""

    icon_hide = (
        '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" '
        'stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
        '<rect x="3" y="4" width="18" height="16" rx="2"></rect>'
        '<path d="M15 4v16"></path><path d="M11 9l-3 3 3 3"></path></svg>'
    )
    icon_show = (
        '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" '
        'stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
        '<rect x="3" y="4" width="18" height="16" rx="2"></rect>'
        '<path d="M15 4v16"></path><path d="M8 9l3 3-3 3"></path></svg>'
    )

    html: list[str] = [head.rstrip()]
    if "</head>" not in head:
        html.append("</head>")
    html.append('<body class="has-side-toc">')
    html.append(
        """  <div class="topbar">
    <div class="topbar-inner">
      <div class="brand">
        <h1>DevOps · Real experience</h1>
        <p>Interview prep from what I actually ran — mobile CI/CD (Android/iOS), Cloud Run + Cloud Build, Linux VM web servers. EN + VI.</p>
      </div>
      <div class="top-actions">
        <button class="btn toc-mobile-btn" data-toc-open type="button">Contents</button>
        <button class="btn theme-toggle" data-theme-toggle aria-label="Switch theme">☾</button>
        <a class="btn btn-link-secondary" href="index.html">Cloud</a>
        <a class="btn btn-link-secondary" href="cv.html">CV</a>
        <a class="btn btn-link-secondary" href="globant.html">Globant</a>
      </div>
    </div>
  </div>
    <div class="toc-backdrop" data-toc-backdrop hidden></div>
  <div class="shell">
    <aside class="side-toc" id="side-toc" aria-label="Question contents">
      <button class="side-toc-close" data-toc-close type="button" aria-label="Close contents">×</button>
      <div class="side-toc-head">
        <strong>Contents</strong>
        <span>Experience first · then fundamentals · then spoken Q&A</span>
      </div>
      <nav class="side-toc-list" data-side-toc>
"""
    )
    html.append("\n".join(toc_bits))
    html.append(
        f"""
      </nav>
    </aside>
  <main class="page with-side-toc">
    <section class="hero with-side-toc">
      <div class="hero-card">
        <div class="section-label">Reusable DevOps prep</div>
        <p>Company-agnostic. Lead with <strong>what I built and operated</strong>: Android/iOS build pipelines, Cloud Run + Cloud Build triggers, and Linux VMs for web. Fundamentals stay short; interview answers stay first-person and honest.</p>
        <nav class="section-nav" aria-label="Sections">
          {nav}
        </nav>
        <div class="hero-kpis">
          <div class="kpi"><strong>{total}</strong><span>Bilingual cards</span></div>
          <div class="kpi"><strong>{nsec}</strong><span>Sections</span></div>
          <div class="kpi"><strong>Steps</strong><span>Real pipelines &amp; VMs</span></div>
        </div>
        <div class="tag-list">
          <span class="tag">Android / iOS CI</span><span class="tag">Cloud Build</span><span class="tag">Cloud Run</span>
          <span class="tag">Cloud SQL</span><span class="tag">Linux VM</span><span class="tag">Apache / LiteSpeed</span>
          <span class="tag">GCP</span><span class="tag">Akktis</span><span class="tag">IELTS AI Tutor</span>
        </div>
      </div>
      <aside class="toc-card" id="toc">
        <div class="section-label">Study order</div>
        <p>Start <a href="#sec-mobile-cicd">Mobile CI/CD</a> → <a href="#sec-cloudrun">Cloud Run / Build</a> → <a href="#sec-linux-vm">Linux VM</a>, then skim fundamentals, then speak Fit/Scenarios out loud.</p>
      </aside>
    </section>
"""
    )
    html.append("\n".join(body_bits))
    html.append(
        """
    <p class="footer-note"><a href="index.html">Cloud/infra sheet</a> · <a href="cv.html">CV stories</a> · <a href="globant.html">PHP/React sheet</a> · DevOps prep — real experience, reusable for any company.</p>
  </main>
  </div>
"""
    )
    html.append(
        f"""
    <aside class="parts-rail" id="parts-rail" aria-label="Parts only">
      <div class="parts-rail-head-row">
        <p class="parts-rail-head">Parts</p>
        <button class="parts-rail-toggle" data-parts-rail-toggle type="button" aria-expanded="true" aria-controls="parts-rail" aria-label="Hide parts panel" title="Hide parts">
          {icon_hide}
        </button>
      </div>
      <nav class="parts-rail-list" data-parts-rail>
"""
    )
    html.append("\n".join(rail_bits))
    html.append(
        f"""
      </nav>
    </aside>
    <button class="parts-rail-show" data-parts-rail-show type="button" hidden aria-label="Show parts panel">
      {icon_show}
      <span>Parts</span>
    </button>
"""
    )
    html.append(script)
    html.append(rail_script)
    html.append("</body>\n</html>\n")

    OUT.write_text("\n".join(html), encoding="utf-8")
    print(f"Wrote {OUT} cards={total} bytes={OUT.stat().st_size} lines={sum(1 for _ in OUT.open())}")


if __name__ == "__main__":
    main()

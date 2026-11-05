#!/usr/bin/env python3
"""Shared HTML shell helpers for interview cheatsheet pages."""
from __future__ import annotations

import html as H
import re
from pathlib import Path

ROOT = Path("/Users/thuynt/Working/Vibe/interview-cheatsheet")
GLOBANT = ROOT / "globant.html"

EXTRA_CSS = """
    .version-tabs {
      display: flex;
      flex-wrap: wrap;
      gap: 0.5rem;
      margin: var(--space-4) 0 var(--space-2);
    }
    .version-tabs button {
      border: 1px solid var(--color-border);
      background: var(--color-surface);
      color: var(--color-text);
      border-radius: 999px;
      padding: 0.55rem 0.95rem;
      font-size: var(--text-sm);
      font-weight: 700;
      cursor: pointer;
    }
    .version-tabs button.is-on {
      background: var(--color-primary);
      border-color: var(--color-primary);
      color: #fff;
    }
    .pack-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: var(--space-4);
      margin: var(--space-4) 0 var(--space-8);
    }
    .pack-card {
      display: block;
      background: var(--color-surface);
      border: 1px solid var(--color-border);
      border-radius: var(--radius-xl);
      box-shadow: var(--shadow-sm);
      padding: var(--space-5);
    }
    .pack-card:hover { border-color: var(--color-primary); }
    .pack-card h3 {
      margin: 0 0 var(--space-2);
      font-family: var(--font-display);
      font-size: var(--text-lg);
    }
    .pack-card p { margin: 0; color: var(--color-text-muted); font-size: var(--text-sm); }
    .pack-card .kicker {
      display: block;
      color: var(--color-primary);
      font-size: var(--text-xs);
      font-weight: 700;
      letter-spacing: 0.04em;
      text-transform: uppercase;
      margin-bottom: 0.4rem;
    }
    .dayof-links {
      display: flex;
      flex-wrap: wrap;
      gap: 0.6rem;
      margin: var(--space-4) 0;
    }
    .dayof-links a.btn { text-decoration: none; }
    [data-version][hidden], [data-version-panel][hidden] { display: none !important; }
"""

VERSION_JS = """
      (function versionTabs() {
        const tabs = Array.from(document.querySelectorAll('[data-version-tab]'));
        if (!tabs.length) return;
        const apply = (v) => {
          tabs.forEach((b) => b.classList.toggle('is-on', b.getAttribute('data-version-tab') === v));
          document.querySelectorAll('[data-version-panel]').forEach((p) => {
            p.hidden = p.getAttribute('data-version-panel') !== v;
          });
          document.querySelectorAll('[data-version]').forEach((el) => {
            const dv = el.getAttribute('data-version');
            el.hidden = !(dv === 'all' || dv === v);
          });
        };
        const fromHash = () => {
          const h = (location.hash || '').replace('#', '');
          if (['php', 'devops', 'node'].includes(h)) return h;
          return 'php';
        };
        tabs.forEach((b) => b.addEventListener('click', () => {
          const v = b.getAttribute('data-version-tab');
          apply(v);
          history.replaceState(null, '', '#' + v);
        }));
        apply(fromHash());
        window.addEventListener('hashchange', () => apply(fromHash()));
      })();
"""

ICON_HIDE = (
    '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" '
    'stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
    '<rect x="3" y="4" width="18" height="16" rx="2"></rect>'
    '<path d="M15 4v16"></path><path d="M11 9l-3 3 3 3"></path></svg>'
)
ICON_SHOW = (
    '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" '
    'stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
    '<rect x="3" y="4" width="18" height="16" rx="2"></rect>'
    '<path d="M15 4v16"></path><path d="M8 9l3 3-3 3"></path></svg>'
)

CARD_RE = re.compile(
    r'<article class="question-card" id="(?P<id>[^"]+)">\s*'
    r'(?:<div class="question-head"><h2>(?P<h2>.*?)</h2>)?',
    re.S,
)


def esc(s: str) -> str:
    return H.escape(s or "", quote=False)


def extract_head(src: str | None = None, title: str = "") -> str:
    html = src if src is not None else GLOBANT.read_text(encoding="utf-8")
    m = re.search(r"(<head>.*?</head>)", html, re.S)
    if not m:
        raise RuntimeError("no <head>")
    head = m.group(1)
    if title:
        head = re.sub(r"<title>.*?</title>", f"<title>{esc(title)}</title>", head, count=1)
    if EXTRA_CSS not in head:
        head = head.replace("</style>", EXTRA_CSS + "\n</style>", 1)
    return "<!DOCTYPE html>\n<html lang=\"en\" data-theme=\"light\">\n" + head


def extract_script(src: str | None = None) -> str:
    html = src if src is not None else GLOBANT.read_text(encoding="utf-8")
    scripts = re.findall(r"<script>.*?</script>", html, re.S)
    if not scripts:
        raise RuntimeError("no script")
    return scripts[-1]


def extract_section(html: str, sec_id: str) -> str:
    needle = f'<section class="section-block" id="{sec_id}">'
    start = html.find(needle)
    if start < 0:
        raise ValueError(f"missing section {sec_id}")
    nxt = html.find('<section class="section-block" id="', start + len(needle))
    chunk = html[start:nxt] if nxt >= 0 else html[start:]
    if nxt < 0:
        foot = chunk.find('<p class="footer-note">')
        if foot >= 0:
            chunk = chunk[:foot]
    return chunk.rstrip()


def extract_article(html: str, aid: str) -> str:
    m = re.search(
        rf'<article class="question-card" id="{re.escape(aid)}">.*?</article>',
        html,
        re.S,
    )
    if not m:
        raise ValueError(f"missing article {aid}")
    return m.group(0)


def strip_articles(section_html: str, ids: list[str]) -> str:
    out = section_html
    for aid in ids:
        out = re.sub(
            rf'<article class="question-card" id="{re.escape(aid)}">.*?</article>\s*',
            "",
            out,
            count=1,
            flags=re.S,
        )
    return out


def cards_in(html: str) -> list[tuple[str, str]]:
    items = []
    for m in CARD_RE.finditer(html):
        cid = m.group("id")
        h2 = m.group("h2") or cid
        title = re.sub(r"^\d+\.\s*", "", re.sub(r"<[^>]+>", "", h2)).strip()
        items.append((cid, title))
    return items


def p_html(text: str) -> str:
    parts = [f"<p>{esc(p)}</p>" for p in text.split("\n\n") if p.strip()]
    return "".join(parts) if parts else "<p></p>"


def interview_card(
    cid: str,
    num: int,
    title: str,
    sub: str,
    q_en: str,
    a_en: str,
    q_vi: str,
    a_vi: str,
    crib: str = "",
) -> str:
    crib_html = ""
    if crib:
        crib_html = f'        <div class="crib"><p><strong>Know:</strong> {esc(crib)}</p></div>\n'
    return f"""<article class="question-card" id="{esc(cid)}">
        <div class="question-head"><h2>{num:02d}. {esc(title)}</h2><p>{esc(sub)}</p></div>
        <div class="grid4">
          <div class="cell row-head">Question EN</div><div class="cell row-head">Answer EN</div>
          <div class="cell row-head">Question VI</div><div class="cell row-head">Answer VI</div>
          <div class="cell question">{p_html(q_en)}</div>
          <div class="cell answer">{p_html(a_en)}</div>
          <div class="cell question">{p_html(q_vi)}</div>
          <div class="cell answer">{p_html(a_vi)}</div>
        </div>
{crib_html}      </article>"""


def toc_from_parts(parts: list[dict]) -> tuple[str, str, str]:
    toc_bits = []
    rail_bits = []
    nav_bits = []
    n = 1
    for part in parts:
        ver = part.get("version")
        ver_attr = f' data-version="{ver}"' if ver else ""
        toc_bits.append(
            f'        <div class="side-toc-part" data-part="{esc(part["id"])}"{ver_attr}>\n'
            f'          <a class="side-toc-part-link" href="#{esc(part["id"])}">{esc(part["label"])}</a>\n'
            f'          <span class="side-toc-part-range">{esc(part.get("range", ""))}</span>\n'
            f"        </div>"
        )
        rail_bits.append(
            f'        <a class="parts-rail-link" href="#{esc(part["id"])}" data-part="{esc(part["id"])}"{ver_attr}>'
            f'<strong>{esc(part["label"])}</strong><span>{esc(part.get("range", ""))}</span></a>'
        )
        nav_bits.append(
            f'<a href="#{esc(part["id"])}"{ver_attr}>{esc(part["nav"] if part.get("nav") else part["label"])}</a>'
        )
        for cid, title in part.get("cards", []):
            toc_bits.append(
                f'        <a class="side-toc-link" href="#{cid}" data-target="{cid}" data-part="{esc(part["id"])}"{ver_attr}>'
                f'<span class="side-toc-num">{n:02d}</span>'
                f'<span class="side-toc-title">{esc(title)}</span></a>'
            )
            n += 1
    return "\n".join(toc_bits), "\n".join(rail_bits), "\n          ".join(nav_bits)


def render_page(
    *,
    title: str,
    brand_h1: str,
    brand_p: str,
    hero_label: str,
    hero_p: str,
    hero_extra: str,
    parts: list[dict],
    body_html: str,
    top_links: list[tuple[str, str]],
    footer: str,
    globant_src: str,
    extra_script: str = "",
) -> str:
    head = extract_head(globant_src, title)
    script = extract_script(globant_src)
    toc, rail, nav = toc_from_parts(parts)
    actions = "\n        ".join(
        [
            '<button class="btn toc-mobile-btn" data-toc-open type="button">Contents</button>',
            '<button class="btn theme-toggle" data-theme-toggle aria-label="Switch theme">☾</button>',
        ]
        + [f'<a class="btn" href="{href}">{esc(label)}</a>' for href, label in top_links]
    )
    if extra_script:
        script = script.replace("</script>", extra_script + "\n    </script>", 1)

    return f"""{head}
<body class="has-side-toc">
  <div class="topbar">
    <div class="topbar-inner">
      <div class="brand">
        <h1>{esc(brand_h1)}</h1>
        <p>{brand_p}</p>
      </div>
      <div class="top-actions">
        {actions}
      </div>
    </div>
  </div>
  <div class="toc-backdrop" data-toc-backdrop hidden></div>
  <div class="shell">
    <aside class="side-toc" id="side-toc" aria-label="Question contents">
      <div class="side-toc-head">
        <strong>Contents</strong>
        <span>Jump to a question</span>
      </div>
      <nav class="side-toc-list" data-side-toc>
{toc}
      </nav>
    </aside>
    <main class="page with-side-toc">
      <section class="hero with-side-toc">
        <div class="hero-card">
          <div class="section-label">{esc(hero_label)}</div>
          <p>{hero_p}</p>
          {hero_extra}
          <nav class="section-nav" aria-label="Sections">
            {nav}
          </nav>
        </div>
      </section>
      <section class="questions">
{body_html}
      </section>
      <p class="footer-note">{footer}</p>
    </main>
  </div>
    <aside class="parts-rail" id="parts-rail" aria-label="Parts only">
      <div class="parts-rail-head-row">
        <p class="parts-rail-head">Parts</p>
        <button class="parts-rail-toggle" data-parts-rail-toggle type="button" aria-expanded="true" aria-controls="parts-rail" aria-label="Hide parts panel" title="Hide parts">
          {ICON_HIDE}
        </button>
      </div>
      <nav class="parts-rail-list" data-parts-rail>
{rail}
      </nav>
    </aside>
    <button class="parts-rail-show" data-parts-rail-show type="button" hidden aria-label="Show parts panel">
      {ICON_SHOW}
      <span>Parts</span>
    </button>
  {script}
</body>
</html>
"""


def render_simple_page(
    *,
    title: str,
    brand_h1: str,
    brand_p: str,
    body_html: str,
    top_links: list[tuple[str, str]],
    footer: str,
    globant_src: str,
) -> str:
    head = extract_head(globant_src, title)
    script = extract_script(globant_src)
    actions = "\n        ".join(
        ['<button class="btn theme-toggle" data-theme-toggle aria-label="Switch theme">☾</button>']
        + [f'<a class="btn" href="{href}">{esc(label)}</a>' for href, label in top_links]
    )
    return f"""{head}
<body>
  <div class="topbar">
    <div class="topbar-inner">
      <div class="brand">
        <h1>{esc(brand_h1)}</h1>
        <p>{brand_p}</p>
      </div>
      <div class="top-actions">
        {actions}
      </div>
    </div>
  </div>
  <main class="page">
{body_html}
    <p class="footer-note">{footer}</p>
  </main>
  {script}
</body>
</html>
"""

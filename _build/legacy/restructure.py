#!/usr/bin/env python3
"""Restructure interview-cheatsheet into topic files + thin day-of packs."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path("/Users/thuynt/Working/Vibe/interview-cheatsheet")
sys.path.insert(0, str(ROOT / "_build"))

from html_lib import (  # noqa: E402
    VERSION_JS,
    cards_in,
    extract_article,
    extract_section,
    interview_card,
    render_page,
    render_simple_page,
    strip_articles,
)

from cards_interview import CARDS as CINT  # noqa: E402

TOP = [
    ("index.html", "Hub"),
    ("fit.html", "Fit"),
    ("soft-skills.html", "Soft skills"),
    ("engineering.html", "Engineering"),
    ("devops.html", "DevOps"),
    ("cv.html", "CV"),
]


def genericize_php_fit(html: str) -> str:
    html = html.replace(
        "Fullstack angle for Globant — not DevOps-first.",
        "PHP + React fullstack — 60–90s spoken intro.",
    )
    html = html.replace(
        "I'm looking for a role that's deeply fullstack — PHP APIs plus React UI — which is why Globant fits.",
        "I'm looking for a role that's deeply fullstack — PHP APIs plus React UI.",
    )
    html = html.replace(
        "Tôi muốn role fullstack đúng nghĩa — PHP API cộng React UI — nên Globant khá khớp.",
        "Tôi muốn role fullstack đúng nghĩa — PHP API cộng React UI.",
    )
    html = html.replace("A. Fit / Intro (Globant)", "A. Fit / Intro — PHP + React")
    return html


def node_fit_section() -> str:
    cards = [
        interview_card(
            "f-node-1", 1, "Tell me about yourself (Node / TypeScript)",
            "Honest: TS/React Native strong; Node APIs not the deepest backend.",
            "Tell me about yourself.",
            "I'm a fullstack engineer with about five years across web, mobile, and SaaS. Day to day I write TypeScript in React and React Native — including IELTS AI Tutor, a shipped iOS/Android app with a Cloud Run backend. I also work PHP/MySQL on enterprise and Akktis work, so I understand APIs, data, and production support. For a Node.js + TypeScript role I'd lead with TypeScript on the client and the JS toolchain around React Native. I'm honest: my deepest API backend is PHP, not Nest or Express production ownership. The transfer is real — types, contracts, debugging across client and API — and I ramp Node server patterns from that.",
            "Hãy giới thiệu về bản thân.",
            "Tôi là fullstack khoảng năm năm, làm web, mobile và SaaS. Hằng ngày tôi viết TypeScript trên React và React Native — gồm IELTS AI Tutor, app iOS/Android đã ship với backend Cloud Run. Tôi cũng làm PHP/MySQL trên enterprise và Akktis, nên hiểu API, data và support production. Với role Node.js + TypeScript tôi dẫn bằng TypeScript phía client và toolchain JS quanh React Native. Tôi nói thẳng: backend API sâu nhất của tôi là PHP, không phải own Nest hay Express production. Phần chuyển được là thật — type, contract, debug xuyên client và API — và tôi ramp pattern Node server từ đó.",
            "TS/RN shipped · PHP APIs deeper · don't claim Nest/Express expert",
        ),
        interview_card(
            "f-node-2", 2, "Why this Node / TypeScript role?",
            "Generic — swap company name on the day-of pack.",
            "Why do you want this Node.js / TypeScript role?",
            "Because I already live in TypeScript on real products, and I want a role where TS is the language of the stack — UI and APIs — not only the React Native client. I like owning a feature from contract to UI. Node on the server is the natural next deepening from that, and I'm motivated to learn your team's framework rather than pretend I already ran it at BaseVN scale.",
            "Tại sao bạn muốn role Node.js / TypeScript này?",
            "Vì tôi đã sống với TypeScript trên sản phẩm thật, và muốn role mà TS là ngôn ngữ của stack — UI và API — không chỉ client React Native. Tôi thích own feature từ contract tới UI. Node phía server là hướng đào sâu tự nhiên, và tôi muốn học framework của team thay vì giả đã chạy nó ở scale BaseVN.",
            "Want TS as the stack language · honest ramp on Node servers",
        ),
        interview_card(
            "f-node-3", 3, "Why should we hire you?",
            "Bridge RN/TS delivery + API habits.",
            "Why should we hire you?",
            "I ship TypeScript UIs that talk to real backends, including a published mobile product. I debug with evidence — Network, logs, contracts — instead of guessing which layer is wrong. I already work in Git, CI, and Cloud Run, so I'm used to taking a change to an environment. I'll be honest about Node server depth and fast on the parts I haven't owned yet.",
            "Tại sao nên tuyển bạn?",
            "Tôi ship UI TypeScript nói chuyện với backend thật, gồm sản phẩm mobile đã publish. Tôi debug bằng evidence — Network, log, contract — không đoán tầng nào sai. Tôi đã làm Git, CI và Cloud Run, nên quen đưa change tới một environment. Tôi nói thẳng độ sâu Node server và học nhanh phần chưa own.",
            "Shipped TS · evidence debug · honest ramp",
        ),
        interview_card(
            "f-node-4", 4, "Strengths / weakness (Node–TS angle)",
            "Keep job-relevant.",
            "What are your strengths and one weakness for this role?",
            "Strength: I move quickly in TypeScript and React, and I think in systems — client state vs API vs data. Weakness for a Node-first team: I have not owned a large Express/Nest codebase in production. I close that by reading your existing services, pairing on a small endpoint first, and mapping patterns I already know from PHP APIs.",
            "Điểm mạnh và một điểm yếu cho role này?",
            "Mạnh: tôi làm TypeScript và React nhanh, và nghĩ theo hệ thống — state client vs API vs data. Yếu với team Node-first: tôi chưa own codebase Express/Nest lớn trên production. Tôi bù bằng đọc service sẵn có, pair một endpoint nhỏ trước, và map pattern tôi đã biết từ PHP API.",
            "Don't oversell Node frameworks",
        ),
        interview_card(
            "f-node-5", 5, "English comfort",
            "Same as other versions.",
            "How comfortable are you working in English?",
            "I'm comfortable reading docs, writing technical updates, and joining meetings in English. I may not be perfect, but I can explain design decisions, bugs, and tradeoffs clearly — which matters more than sounding fancy.",
            "Bạn làm việc bằng tiếng Anh thế nào?",
            "Tôi ổn với đọc docs, viết cập nhật kỹ thuật và họp bằng English. Không hoàn hảo, nhưng giải thích được quyết định thiết kế, bug và tradeoff rõ — điều đó quan trọng hơn nói hoa mỹ.",
        ),
    ]
    return (
        '<section class="section-block" id="sec-fit-node">\n'
        "      <h2>Fit / Intro — Node.js + TypeScript</h2>\n"
        + "\n".join(cards)
        + "\n    </section>"
    )


def php_why_role_card() -> str:
    return interview_card(
        "f-php-why",
        2,
        "Why this PHP + React role?",
        "Generic — company-specific 'why us' lives on the day-of pack.",
        "Why do you want this Fullstack PHP + React role?",
        "Because the work matches how I want to work: design and maintain apps with PHP and React, build APIs, polish UI, optimize both sides, and fix production issues properly. I want to deepen enterprise React + TypeScript while keeping strong PHP backend ownership. For why this company specifically, I tailor that on the day from the JD.",
        "Tại sao bạn muốn role Fullstack PHP + React này?",
        "Vì việc khớp cách tôi muốn làm: thiết kế/maintain app với PHP và React, dựng API, làm UI tốt, tối ưu cả hai phía, và xử lý production đúng cách. Tôi muốn đào sâu React + TypeScript enterprise trong khi vẫn giữ ownership PHP backend. Lý do chọn đúng công ty này tôi chỉnh theo JD vào ngày interview.",
        "Stack fit here · company why on the day-of page",
    )


def extra_soft_cards() -> str:
    cards = [
        interview_card(
            "s-collab",
            1,
            "How you collaborate with coworkers",
            "Daily teamwork, not only ceremonies.",
            "How do you work with teammates day to day?",
            "I try to make work visible: tickets with clear acceptance, small PRs, and status before people have to chase me. I ask early when the contract or design is unclear instead of building the wrong thing. I review others' code for risk, not style nits only. If FE and BE are split, I agree the API shape first so we don't throw work over the wall.",
            "Bạn cộng tác với đồng nghiệp hằng ngày thế nào?",
            "Tôi cố làm việc nhìn thấy được: ticket có acceptance rõ, PR nhỏ, và status trước khi người khác phải hỏi. Tôi hỏi sớm khi contract hoặc design chưa rõ thay vì xây sai. Review code người khác theo rủi ro, không chỉ style. Nếu tách FE và BE, tôi chốt shape API trước để không ném việc qua tường.",
            "Visible work · small PRs · agree contract first",
        ),
        interview_card(
            "s-two-solutions",
            2,
            "Two different solutions or ideas",
            "Disagree on approach, not on people.",
            "What do you do when you and a coworker have different technical solutions?",
            "I put both options on the table with tradeoffs — time, risk, how hard it is to change later — and I ask what we optimize for this sprint. I don't need to 'win' the design. If we still disagree, I suggest a small spike or the reversible choice, and I commit to the team's decision. After we pick, I implement that path cleanly instead of half-building my idea in secret.",
            "Khi bạn và đồng nghiệp khác giải pháp kỹ thuật, bạn làm gì?",
            "Tôi đặt cả hai option lên bàn kèm tradeoff — thời gian, rủi ro, sau này sửa khó thế nào — và hỏi sprint này tối ưu gì. Tôi không cần 'thắng' design. Nếu vẫn khác ý, tôi đề xuất spike nhỏ hoặc lựa chọn đảo được, rồi commit theo quyết định của team. Sau khi chọn, tôi implement path đó sạch, không nửa vời cài ý mình.",
            "Tradeoffs · spike if stuck · commit after the decision",
        ),
    ]
    return (
        '<section class="section-block" id="sec-collab">\n'
        "      <h2>Collaboration / different ideas</h2>\n"
        + "\n".join(cards)
        + "\n    </section>"
    )


def wrap_panel(version: str, inner: str) -> str:
    return f'<div data-version-panel="{version}">\n{inner}\n    </div>'


def part(id: str, label: str, html: str, version: str | None = None, nav: str | None = None) -> dict:
    cards = cards_in(html)
    return {
        "id": id,
        "label": label,
        "nav": nav or label,
        "range": f"{len(cards)} Q",
        "version": version,
        "cards": cards,
        "html": html,
    }


def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")
    print(f"wrote {path.name} bytes={path.stat().st_size}")


def build_fit(g: str) -> None:
    php = genericize_php_fit(extract_section(g, "sec-fit"))
    php = strip_articles(php, ["g2"])
    php = php.replace("</section>", php_why_role_card() + "\n    </section>", 1)

    do_cards = [c for c in CINT if c["sec"] == "sec-fit"]
    do_html = ['<section class="section-block" id="sec-fit-devops">', "      <h2>Fit / Intro — DevOps</h2>"]
    for i, c in enumerate(do_cards, start=1):
        do_html.append(
            interview_card(
                f"f-do-{i}", i, c["title"], c.get("sub", ""),
                c["q_en"], c["a_en"], c["q_vi"], c["a_vi"],
            )
        )
    do_html.append("    </section>")
    devops = "\n".join(do_html)
    node = node_fit_section()

    php_p = part("sec-fit", "PHP / fullstack", php, "php", "PHP")
    do_p = part("sec-fit-devops", "DevOps", devops, "devops", "DevOps")
    node_p = part("sec-fit-node", "Node / TypeScript", node, "node", "Node–TS")

    tabs = """
          <div class="version-tabs" role="tablist" aria-label="Fit versions">
            <button type="button" data-version-tab="php">PHP / fullstack</button>
            <button type="button" data-version-tab="devops">DevOps</button>
            <button type="button" data-version-tab="node">Node.js / TypeScript</button>
          </div>
          <p style="color:var(--color-text-muted);font-size:var(--text-sm)">Company-specific “why us” stays on the day-of pack. Use the matching version, then speak it out loud.</p>
"""
    body = "\n".join([
        wrap_panel("php", php),
        wrap_panel("devops", devops),
        wrap_panel("node", node),
    ])
    html = render_page(
        title="Fit / Intro — PHP · DevOps · Node–TS",
        brand_h1="Fit / intro",
        brand_p="Tell me about yourself, why this role, strengths — three versions in one file.",
        hero_label="Shared topic",
        hero_p="Pick the version that matches the job. Keep answers spoken and honest. Open the company day-of page for JD-specific why-this-company lines.",
        hero_extra=tabs,
        parts=[php_p, do_p, node_p],
        body_html=body,
        top_links=TOP,
        footer='<a href="index.html">Hub</a> · Fit versions: PHP · DevOps · Node–TS',
        globant_src=g,
        extra_script=VERSION_JS,
    )
    write(ROOT / "fit.html", html)


def build_soft(g: str) -> None:
    debug = extract_section(g, "sec-debug")
    quality = extract_section(g, "sec-quality")
    quality = quality.replace(
        "Joining a Scrum team at Globant is familiar ground for me.",
        "Joining a Scrum team is familiar ground for me.",
    )
    quality = quality.replace(
        "Join team Scrum ở Globant với tôi là quen thuộc.",
        "Join team Scrum với tôi là quen thuộc.",
    )
    quality = re.sub(
        r"For this Globant interview I researched Zustand and dashboard libraries from the JD — not to pretend production expertise, but to understand why teams pick them\.",
        "When a JD names a library I have not shipped, I research it to understand why teams pick it — not to pretend production expertise.",
        quality,
    )
    quality = quality.replace(
        "Khi JD nêu lib tôi chưa ship, tôi research để hiểu vì sao team chọn — không giả production.",
        "Khi JD nêu lib tôi chưa ship, tôi research để hiểu vì sao team chọn — không giả production.",
    )
    quality = quality.replace(
        "Cho interview Globant tôi research Zustand và lib dashboard từ JD — không giả production, mà hiểu vì sao team chọn.",
        "Khi JD nêu lib tôi chưa ship, tôi research để hiểu vì sao team chọn — không giả production.",
    )
    ai = extract_section(g, "sec-ai")
    hard = extract_section(g, "sec-hard")
    spoken = extract_section(g, "sec-spoken")
    collab = extra_soft_cards()
    solve = (
        '<section class="section-block" id="sec-solve">\n'
        "      <h2>Problem solving</h2>\n"
        + extract_article(g, "g55")
        + "\n"
        + extract_article(g, "g56")
        + "\n"
        + extract_article(g, "g57")
        + "\n    </section>"
    )
    sections = [
        ("sec-collab", "Collaborate / different ideas", collab, "Collab"),
        ("sec-debug", "Find & fix bugs (FE vs BE)", debug, "Find/fix bugs"),
        ("sec-solve", "Problem solving", solve, "Problem solving"),
        ("sec-quality", "Agile / Scrum / quality", quality, "Agile / Scrum"),
        ("sec-ai", "AI-assisted coding", ai, "AI"),
        ("sec-hard", "Hard fixes / under pressure", hard, "Under pressure"),
        ("sec-spoken", "Spoken English", spoken, "Spoken English"),
    ]
    parts = []
    body = []
    for sid, label, html, nav in sections:
        parts.append(part(sid, label, html, nav=nav))
        body.append(html)
    page = render_page(
        title="Soft skills — Agile, debug, AI, pressure",
        brand_h1="Soft skills",
        brand_p="Agile/Scrum, find and fix bugs, problem solving, collaboration, disagreement, AI, hard fixes, under pressure.",
        hero_label="Shared topic",
        hero_p="Work behavior and interview conversation — reuse for every company. Technical FE/BE debug lives here as a method; stack theory is on Engineering and DevOps.",
        hero_extra="",
        parts=parts,
        body_html="\n".join(body),
        top_links=TOP,
        footer='<a href="index.html">Hub</a> · Soft skills · spoken EN/VI',
        globant_src=g,
    )
    write(ROOT / "soft-skills.html", page)


def build_engineering(g: str) -> None:
    spec = [
        ("sec-php", "PHP backend", "PHP"),
        ("sec-pure-php", "Pure PHP", "PHP thuần"),
        ("sec-react", "React + TypeScript", "React"),
        ("sec-react-libs", "React libraries", "React libs"),
        ("sec-workflow", "Workflow & dashboards", "Workflow"),
        ("sec-state", "Zustand", "Zustand"),
        ("sec-dash-libs", "Dashboard / workflow libs", "Dash libs"),
        ("sec-why-stack", "Why this stack", "Why stack"),
        ("sec-enterprise", "Enterprise stories", "Enterprise"),
        ("sec-integ", "Fullstack integration", "Integration"),
        ("sec-design", "System design / scale", "System design"),
    ]
    parts = []
    body = []
    for sid, label, nav in spec:
        html = extract_section(g, sid)
        if sid == "sec-design":
            html = strip_articles(html, ["g55", "g56", "g57"])
        parts.append(part(sid, label, html, nav=nav))
        body.append(html)
    page = render_page(
        title="Engineering — Backend, frontend, system design",
        brand_h1="Engineering",
        brand_p="Backend (PHP), frontend (React / TypeScript), fullstack integration, and system design.",
        hero_label="Shared topic",
        hero_p="Stack and design answers. Soft-skill debug process is on the Soft skills page. Be honest on Zustand: researched, not production.",
        hero_extra="",
        parts=parts,
        body_html="\n".join(body),
        top_links=TOP,
        footer='<a href="index.html">Hub</a> · Engineering · do not oversell Zustand',
        globant_src=g,
    )
    write(ROOT / "engineering.html", page)


def build_hub(g: str) -> None:
    body = """
    <section class="hero">
      <div class="hero-card">
        <div class="section-label">Interview pack</div>
        <h2 style="margin:0 0 0.5rem">Study by topic. Open a company pack on the day.</h2>
        <p>Shared answers live in the topic files. Company pages only keep JD notes, why this company, and links.</p>
      </div>
    </section>
    <h2>Topics</h2>
    <div class="pack-grid">
      <a class="pack-card" href="fit.html"><span class="kicker">01</span><h3>Fit / intro</h3><p>Tell me about yourself — PHP, DevOps, and Node–TS versions.</p></a>
      <a class="pack-card" href="soft-skills.html"><span class="kicker">02</span><h3>Soft skills</h3><p>Agile/Scrum, find/fix bugs, problem solving, collaboration, AI, pressure.</p></a>
      <a class="pack-card" href="engineering.html"><span class="kicker">03</span><h3>Engineering</h3><p>PHP backend, React/TS frontend, system design.</p></a>
      <a class="pack-card" href="devops.html"><span class="kicker">04</span><h3>DevOps</h3><p>Mobile CI/CD, Cloud Run, Linux VMs, GCP, security — real experience.</p></a>
      <a class="pack-card" href="cv.html"><span class="kicker">05</span><h3>CV / project stories</h3><p>Akktis, IELTS AI Tutor, BaseVN walkthroughs and hard fixes.</p></a>
    </div>
    <h2>Day-of packs</h2>
    <div class="pack-grid">
      <a class="pack-card" href="globant.html"><span class="kicker">Globant</span><h3>PHP + React fullstack</h3><p>JD, why Globant, Zustand honesty. Then Fit (PHP) + Engineering + Soft skills.</p></a>
      <a class="pack-card" href="kaopiz.html"><span class="kicker">Kaopiz</span><h3>Cloud / Infrastructure</h3><p>Why Kaopiz + Cloud/Infra theory. Then Fit (DevOps) + DevOps + Soft skills.</p></a>
      <a class="pack-card" href="go1-en.html"><span class="kicker">Go1</span><h3>Live coding (EN)</h3><p>Python tutorial for the Go1 challenge. Vietnamese: go1-vi.html.</p></a>
      <a class="pack-card" href="vnpt-devops.html"><span class="kicker">VNPT</span><h3>Redirects to DevOps</h3><p>Reusable DevOps prep — not a separate topic dump.</p></a>
    </div>
"""
    page = render_simple_page(
        title="Interview cheatsheet — hub",
        brand_h1="Interview cheatsheet",
        brand_p="Topic files first. Company pages are thin day-of packs.",
        body_html=body,
        top_links=TOP,
        footer="Spoken EN/VI · CV-aligned · honest on depth",
        globant_src=g,
    )
    write(ROOT / "index.html", page)


def build_globant_dayof(g: str) -> None:
    why = extract_article(g, "g2")
    q = extract_article(g, "g38")
    close = extract_article(g, "g39")
    body = f"""
    <section class="hero">
      <div class="hero-card">
        <div class="section-label">Day-of · Globant</div>
        <p>Fullstack PHP + React. Zustand: researched, <strong>not used in a real project</strong>. Shared answers are in the topic files — do not restudy them here.</p>
        <div class="dayof-links">
          <a class="btn" href="fit.html#php">Fit (PHP)</a>
          <a class="btn" href="engineering.html">Engineering</a>
          <a class="btn" href="soft-skills.html">Soft skills</a>
          <a class="btn" href="cv.html">CV stories</a>
        </div>
      </div>
    </section>
    <section class="questions">
      <section class="section-block" id="sec-globant">
        <h2>Only Globant-specific lines</h2>
        {why}
        {q}
        {close}
      </section>
    </section>
"""
    page = render_simple_page(
        title="Globant — day-of pack",
        brand_h1="Globant · day-of",
        brand_p="JD notes and why this company. Open Fit / Engineering / Soft skills for the real answers.",
        body_html=body,
        top_links=TOP,
        footer='<a href="index.html">Hub</a> · Globant day-of · do not oversell Zustand',
        globant_src=g,
    )
    write(ROOT / "globant.html", page)


def build_kaopiz(old_index: str) -> None:
    text = old_index
    text = text.replace(
        "Cloud / Infrastructure Interview Cheat Sheet",
        "Kaopiz · Cloud / Infra day-of",
        1,
    )
    text = text.replace(
        "<title>Cloud Infra Interview Q&amp;A — Kaopiz + Reusable</title>",
        "<title>Kaopiz — Cloud / Infra day-of</title>",
    )
    text = text.replace(
        "<title>Cloud Infra Interview Q&A — Kaopiz + Reusable</title>",
        "<title>Kaopiz — Cloud / Infra day-of</title>",
    )
    text = re.sub(
        r'<div class="top-actions">.*?</div>',
        """<div class="top-actions">
        <button class="btn theme-toggle" data-theme-toggle aria-label="Switch theme">☾</button>
        <a class="btn" href="index.html">Hub</a>
        <a class="btn" href="fit.html#devops">Fit (DevOps)</a>
        <a class="btn" href="devops.html">DevOps experience</a>
        <a class="btn" href="soft-skills.html">Soft skills</a>
        <a class="btn" href="cv.html">CV</a>
      </div>""",
        text,
        count=1,
        flags=re.S,
    )
    text = text.replace(
        "Spoken bilingual Q&amp;A for Kaopiz today — reusable for future Cloud/Infra interviews. Aligned to your CV: Linux, GCP, Docker, CI/CD, plus fundamentals.",
        "Day-of pack: why Kaopiz + Cloud/Infra theory. Fit, DevOps experience, and soft skills live in topic files.",
    )
    text = text.replace(
        "Spoken bilingual Q&A for Kaopiz today — reusable for future Cloud/Infra interviews. Aligned to your CV: Linux, GCP, Docker, CI/CD, plus fundamentals.",
        "Day-of pack: why Kaopiz + Cloud/Infra theory. Fit, DevOps experience, and soft skills live in topic files.",
    )
    banner = (
        "<p><strong>Study order:</strong> "
        '<a href="fit.html#devops">Fit (DevOps)</a> · '
        '<a href="devops.html">hands-on DevOps</a> · '
        '<a href="soft-skills.html">soft skills</a> · '
        "then the Cloud/Infra theory cards below (Terraform honesty, monitoring, Linux).</p>"
    )
    text = text.replace(
        '<div class="section-label">Interview Focus</div>',
        '<div class="section-label">Day-of · Kaopiz</div>' + banner,
        1,
    )
    write(ROOT / "kaopiz.html", text)


def patch_cv() -> None:
    p = ROOT / "cv.html"
    t = p.read_text(encoding="utf-8")
    t = t.replace('href="globant.html">Globant prep</a>', 'href="index.html">Hub</a>')
    t = t.replace(
        'href="index.html">Fundamentals sheet</a>',
        'href="devops.html">DevOps</a>\n        <a class="btn" href="engineering.html">Engineering</a>',
    )
    t = t.replace(
        '<a href="index.html">← Back to Cloud/Infra fundamentals sheet</a>',
        '<a href="index.html">← Hub</a> · <a href="fit.html">Fit</a> · <a href="soft-skills.html">Soft skills</a>',
    )
    p.write_text(t, encoding="utf-8")
    print("patched cv.html")


def patch_devops_generator() -> None:
    p = ROOT / "_build" / "gen_devops.py"
    t = p.read_text(encoding="utf-8")
    t = t.replace(
        '    ("sec-fit", "11 · Fit / intro", "Part 11 · Fit"),\n'
        '    ("sec-scenario", "12 · Scenario questions", "Part 12 · Scenarios"),\n'
        '    ("sec-close", "13 · Closing", "Part 13 · Closing"),\n',
        '    ("sec-scenario", "11 · Scenario questions", "Part 11 · Scenarios"),\n',
    )
    t = t.replace(
        '        <a class="btn btn-link-secondary" href="index.html">Cloud</a>\n'
        '        <a class="btn btn-link-secondary" href="cv.html">CV</a>\n'
        '        <a class="btn btn-link-secondary" href="globant.html">Globant</a>',
        '        <a class="btn btn-link-secondary" href="index.html">Hub</a>\n'
        '        <a class="btn btn-link-secondary" href="fit.html#devops">Fit</a>\n'
        '        <a class="btn btn-link-secondary" href="soft-skills.html">Soft skills</a>\n'
        '        <a class="btn btn-link-secondary" href="cv.html">CV</a>',
    )
    t = t.replace(
        "then skim fundamentals, then speak Fit/Scenarios out loud.",
        'then skim fundamentals, then speak <a href="fit.html#devops">Fit</a> and Scenarios out loud.',
    )
    t = t.replace(
        '<p class="footer-note"><a href="index.html">Cloud/infra sheet</a> · <a href="cv.html">CV stories</a> · <a href="globant.html">PHP/React sheet</a> · DevOps prep — real experience, reusable for any company.</p>',
        '<p class="footer-note"><a href="index.html">Hub</a> · <a href="fit.html#devops">Fit (DevOps)</a> · <a href="soft-skills.html">Soft skills</a> · <a href="cv.html">CV</a> · hands-on DevOps.</p>',
    )
    p.write_text(t, encoding="utf-8")
    print("patched gen_devops.py")


def regen_devops() -> None:
    import runpy

    runpy.run_path(str(ROOT / "_build" / "gen_devops.py"), run_name="__main__")


def patch_go1() -> None:
    for name in ("go1-en.html", "go1-vi.html"):
        p = ROOT / name
        t = p.read_text(encoding="utf-8")
        if 'href="index.html"' in t:
            continue
        t = t.replace(
            "<h1>Go1 live coding</h1>",
            '<h1>Go1 live coding</h1>\n      <p><a href="index.html" style="color:#c6e35a">← Interview hub</a></p>',
            1,
        )
        p.write_text(t, encoding="utf-8")
        print(f"patched {name}")


def main() -> None:
    g = (ROOT / "globant.html").read_text(encoding="utf-8")
    old_index = (ROOT / "index.html").read_text(encoding="utf-8")
    build_fit(g)
    build_soft(g)
    build_engineering(g)
    build_kaopiz(old_index)
    build_hub(g)
    build_globant_dayof(g)
    patch_cv()
    patch_devops_generator()
    regen_devops()
    patch_go1()
    print("restructure done")


if __name__ == "__main__":
    main()

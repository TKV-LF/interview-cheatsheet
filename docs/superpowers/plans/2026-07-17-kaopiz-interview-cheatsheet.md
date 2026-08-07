# Kaopiz Interview Cheatsheet Upgrade Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Upgrade `interview-cheatsheet/index.html` into a full ~44-topic bilingual spoken-style Cloud/Infra interview pack with section nav and technical crib notes, aligned to Kaopiz JD and reusable for future interviews.

**Architecture:** Single static HTML file. Preserve existing theme/CSS language. Add section navigation + crib-notes strip. Content rewritten to conversational EN/VI. Technical cards include Know / Trap / Follow-up.

**Tech Stack:** Plain HTML + CSS + small theme-toggle JS (no build step, no dependencies).

## Global Constraints

- File to modify: `interview-cheatsheet/index.html` only (plus this plan under docs/)
- Spoken style EN: short sentences, “I usually… / In my case…”
- Honesty: GCP/Linux/Docker/CI/CD strong; Terraform beginner–intermediate; no fake production depth for K8s/Prometheus/AWS
- Company-specific text only in Why Kaopiz + closing pitch
- Keep dark/light theme toggle working
- Spec source: `docs/superpowers/specs/2026-07-17-kaopiz-interview-cheatsheet-design.md`
- Do not invent CV projects/tools not already in the current sheet

---

### Task 1: CSS shell — section nav + crib notes

**Files:**
- Modify: `interview-cheatsheet/index.html` (styles + topbar/hero structure)

**Interfaces:**
- Consumes: existing CSS variables and `.question-card` / `.grid4` / `.note` patterns
- Produces: `.section-nav`, `.section-nav a`, `.section-block`, `.crib`, `.crib strong` styles; hero/TOC ready for section anchors `#sec-behavioral` … `#sec-close`

- [x] **Step 1: Add CSS for section nav and crib notes**

Append after `.note { ... }` block:

```css
.section-nav {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-2);
  margin-top: var(--space-4);
}
.section-nav a {
  padding: 0.4rem 0.75rem;
  border: 1px solid var(--color-divider);
  border-radius: 999px;
  background: var(--color-bg);
  font-size: var(--text-xs);
  font-weight: 700;
  color: var(--color-text-muted);
}
.section-nav a:hover {
  border-color: var(--color-primary);
  color: var(--color-primary);
  background: var(--color-primary-highlight);
}
.section-block {
  scroll-margin-top: 110px;
  margin-top: var(--space-8);
}
.section-block > h2 {
  font-family: var(--font-display);
  font-size: var(--text-lg);
  letter-spacing: -0.02em;
  margin: 0 0 var(--space-4);
}
.crib {
  padding: var(--space-4) var(--space-5);
  background: color-mix(in srgb, var(--color-warning) 8%, var(--color-surface));
  border-top: 1px solid var(--color-divider);
  font-size: var(--text-sm);
  color: var(--color-text-muted);
}
.crib p { margin: 0; }
.crib p + p { margin-top: var(--space-2); }
.crib strong { color: var(--color-text); }
```

- [ ] **Step 2: Update hero copy + KPI to ~44 topics + section nav links**

Hero subtitle and tags must include: Linux, GCP, Docker, CI/CD, Terraform, Monitoring, Logging, Networking.

Section nav links:

```html
<nav class="section-nav" aria-label="Sections">
  <a href="#sec-behavioral">Behavioral</a>
  <a href="#sec-cloud">Cloud</a>
  <a href="#sec-iac">IaC</a>
  <a href="#sec-containers">Containers</a>
  <a href="#sec-cicd">CI/CD</a>
  <a href="#sec-observability">Observability</a>
  <a href="#sec-linux">Linux / Net</a>
  <a href="#sec-security">Security / Data</a>
  <a href="#sec-close">Close</a>
</nav>
```

- [ ] **Step 3: Verify in browser**

Open `index.html`. Confirm styles load, theme toggle still works, section links exist (anchors may be empty until later tasks).

- [ ] **Step 4: Checkpoint**

No commit required unless user asks. Proceed to Task 2.

---

### Task 2: Behavioral section (cards 01–09)

**Files:**
- Modify: `interview-cheatsheet/index.html` questions area

**Interfaces:**
- Consumes: `.question-card` / `.grid4` markup pattern from existing file
- Produces: `#sec-behavioral` wrapper + cards `#q1`–`#q9` with spoken EN/VI answers (no crib notes)

Card template:

```html
<section class="section-block" id="sec-behavioral">
  <h2>A. Behavioral / Fit</h2>
  <article class="question-card" id="q1">...</article>
  <!-- q2–q9 -->
</section>
```

Content requirements per card (spoken, CV-aligned):

| ID | Topic | Must include |
|----|-------|--------------|
| q1 | About yourself | ~5y full-stack; Linux/CI/CD/GCP day-to-day; moving toward infra |
| q2 | Why new role | deeper infra/automation/reliability |
| q3 | Why Kaopiz | JD match: cloud, IaC, CI/CD, monitoring/logging; growth path |
| q4 | Why hire you | app + ops bridge |
| q5 | Strengths | ownership, troubleshooting, adaptability, docs |
| q6 | Weakness | depth vs speed + improvement |
| q7 | Current role | Akktis: Linux, CI/CD, Cloud Run/SQL/Storage, Laravel/WP |
| q8 | Hard problem | multi-env deploy/config root-cause pattern |
| q9 | Learn fast | business goal → high-risk area → enough depth |

- [ ] **Step 1: Replace old behavioral answers with spoken rewrites + add missing cards**
- [ ] **Step 2: Update TOC links for q1–q9**
- [ ] **Step 3: Spot-check — read EN answers aloud for natural tone**

---

### Task 3: Cloud + IaC sections (cards 10–20)

**Files:**
- Modify: `interview-cheatsheet/index.html`

**Interfaces:**
- Produces: `#sec-cloud` (q10–q15), `#sec-iac` (q16–q20) with crib notes on each card

Crib notes strip template:

```html
<div class="crib">
  <p><strong>Know:</strong> …</p>
  <p><strong>Trap:</strong> …</p>
  <p><strong>Follow-up:</strong> …</p>
</div>
```

Topics:

- q10 Cloud experience (GCP first; AWS/Azure awareness)
- q11 VM vs Cloud Run vs GKE
- q12 Storage + Cloud SQL
- q13 VPC / subnet / firewall / LB
- q14 IAM least privilege
- q15 Serverless tradeoffs
- q16 IaC / why Terraform (honest beginner–intermediate)
- q17 init → plan → apply
- q18 State + remote state
- q19 Modules concept
- q20 Common mistakes / ramp-up

Terraform honesty line (required in EN+VI somewhere in q16 or q20):  
“I’ve studied the concepts and I’m ready to apply them on real projects; I haven’t owned large production Terraform estates yet.”

- [ ] **Step 1: Write cloud cards with crib notes**
- [ ] **Step 2: Write Terraform cards with crib notes + honesty**
- [ ] **Step 3: TOC update for q10–q20**

---

### Task 4: Containers + CI/CD (cards 21–28)

**Files:**
- Modify: `interview-cheatsheet/index.html`

**Interfaces:**
- Produces: `#sec-containers` (q21–q24), `#sec-cicd` (q25–q28) with crib notes

Topics:

- q21 Docker image vs container / Dockerfile
- q22 Volumes / networking practical
- q23 Cloud Run experience
- q24 K8s awareness (pod/service/deployment) — no fake depth
- q25 CI vs CD
- q26 Pipeline you built (mobile/web multi-env)
- q27 Multi-environment strategy
- q28 Tools landscape (GitLab CI, GitHub Actions, Jenkins, CodeBuild, Bamboo)

- [ ] **Step 1: Write container cards**
- [ ] **Step 2: Write CI/CD cards**
- [ ] **Step 3: TOC update**

---

### Task 5: Observability + Linux/Net + Security/Data + Close (cards 29–44)

**Files:**
- Modify: `interview-cheatsheet/index.html`

**Interfaces:**
- Produces: `#sec-observability` (q29–q33), `#sec-linux` (q34–q38), `#sec-security` (q39–q42), `#sec-close` (q43–q44)

Topics:

- q29 Monitoring vs logging vs tracing
- q30 Metrics to alert on
- q31 Prometheus + Grafana concepts
- q32 Logging options (Cloud Logging / Loki / ELK / Graylog)
- q33 Incident flow
- q34 Linux troubleshooting checklist
- q35 Disk/memory/CPU/process commands
- q36 Networking mindset (DNS/ports/curl)
- q37 SSH / permissions / systemd
- q38 Bash/Python automation
- q39 Secrets management
- q40 Encryption / CMEK / Cloud Armor awareness (honest)
- q41 Cloud SQL / Postgres / Redis
- q42 AI integration (IELTS + Langfuse) as optional plus
- q43 Questions for interviewer
- q44 60-second closing pitch

- [ ] **Step 1: Write observability cards + crib notes**
- [ ] **Step 2: Write Linux/networking cards + crib notes**
- [ ] **Step 3: Write security/data + AI cards + crib notes**
- [ ] **Step 4: Write close cards (q43–q44)**
- [ ] **Step 5: Rebuild full TOC grouped by section**
- [ ] **Step 6: Update footer note**

---

### Task 6: Verification pass

**Files:**
- Verify: `interview-cheatsheet/index.html`

- [ ] **Step 1: Structural checks**

Run:

```bash
rg -c 'question-card' interview-cheatsheet/index.html
rg -c 'class="crib"' interview-cheatsheet/index.html
rg 'id="sec-' interview-cheatsheet/index.html
rg -n 'Terraform|Cloud Run|Prometheus|least privilege' interview-cheatsheet/index.html | head
```

Expected: ~44 question cards; crib notes present on technical cards; all 9 section ids present.

- [ ] **Step 2: Honesty scan**

Confirm no claims of production Kubernetes ownership, multi-year Terraform ownership, or deep AWS production unless already in CV sheet.

- [ ] **Step 3: Browser smoke**

Open file, toggle theme, click 3 section links and 3 TOC links, confirm scroll works.

- [ ] **Step 4: Done checkpoint**

Report: card count, crib count, any intentional omissions.

---

## Spec coverage check

| Spec requirement | Task |
|------------------|------|
| Single HTML mega page | 1–5 |
| Spoken style rewrite | 2–5 |
| Section nav | 1 |
| ~44 topics | 2–5 |
| Crib notes on technical | 3–5 |
| Terraform honest beginner–intermediate | 3 |
| Kaopiz + reusable | 2 (q3), 5 (q44) |
| Preserve theme toggle | 1, 6 |

## Placeholder scan

None intentional. Content must be fully written during execution (not left as “fill later”).

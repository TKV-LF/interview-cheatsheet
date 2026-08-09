# VNPT DevOps Fundamentals + Interview Prep — Design Spec

**Date:** 2026-08-09  
**Company:** VNPT IT  
**Role:** Kỹ sư DevOps  
**Location:** Hà Nội (multi-site JD)  
**Approved outline:** Yes (Approach 1 — sibling bilingual study page, full JD coverage)

## Goal

Single offline page `vnpt-devops.html` for:

1. **Pre-test fundamentals** — IT/DevOps/network/security/OS + JD tooling (CI/CD, Docker/K8s, monitoring, backup, architecture, AI/LLM)
2. **Interview spoken prep** — bilingual EN/VI answers grounded in **strong hands-on** DevOps experience (honesty level A)

Success: can study for a written/MCQ-style screen, then walk fit + scenario questions in interview without inventing weak experience.

## Approach

- Sibling page to `globant.html` / `index.html` (same visual system: CSS variables, sticky topbar, side TOC, theme toggle, question/concept cards)
- Style: bilingual **EN + VI** per topic (like Globant)
- Cross-link from `index.html` (and `cv.html` if a natural “role pages” list exists)
- Full JD coverage in v1 (user chose depth B, not phased compact)

## Honesty / voice

- Experience posture: **strong hands-on** — CI/CD, Docker/K8s, monitoring spoken as real project work
- Still stay precise: prefer “I did X in Y context” over generic buzzwords
- AI/LLM in DevOps: frame as practical use (coding assistant, log triage, docs, pipeline help) — do not claim production LLM platforms unless true
- Map stories to JD verbs: deploy CI/CD with developers, monitoring/alerting, incident recovery, backup/recovery, ATTT collaboration, architecture contribution

## File & UX

| Item | Decision |
|------|----------|
| File | `interview-cheatsheet/vnpt-devops.html` |
| Lang | `lang="en"` page shell; content bilingual EN/VI |
| Nav | Sticky brand + theme toggle; sticky side TOC by section |
| Card types | Concept cards (study) + Interview cards (spoken) |
| Concept card | Concept EN/VI → Must-know → Commands/examples → Exam trap |
| Interview card | Question → Spoken EN → Spoken VI → optional STAR bullets |
| Offline | Self-contained HTML + Fontshare (same as existing pages) |
| Commands / code | Always English; explanations bilingual |
| Density | Full JD coverage like Globant depth — many cards per section, not one summary blurb |

## Content sections

### Part 1 — Test fundamentals

| ID | Section | Must cover |
|----|---------|------------|
| 0 | JD map | Role duties, required tools, what test likely checks vs interview |
| 1 | IT & DevOps fundamentals | DevOps definition, SDLC, CALMS/culture vs tools, CI vs CD vs GitOps, IaC idea |
| 2 | Linux essentials | Users/permissions, processes, systemd, packages, disk, logs, common ops commands |
| 3 | OS fundamentals (JD) | Process management, threads & concurrency, sockets, I/O, virtualization, memory, filesystems |
| 4 | Network basics | OSI/TCP-IP, IP/DNS, HTTP(S), ports, TCP vs UDP, firewall, LB, NAT |
| 5 | Security / ATTT basics | AuthN/Z, secrets, least privilege, TLS, hardening, logging for security, work with ATTT |
| 6 | Git + collaboration | Git basics/branching, GitLab/Bitbucket, Jira in delivery loop |
| 7 | CI/CD | Jenkins & GitLab CI concepts, stages, artifacts, secrets in CI, quality gates |
| 8 | Automation | Ansible inventory/playbooks/idempotency; Bash/Python ops scripting patterns |
| 9 | Containers | Docker image/layer, Dockerfile, volumes, networks, registry, pitfalls |
| 10 | Kubernetes + HA | Workloads, Services, Ingress, ConfigMap/Secret, probes, rolling update, HA patterns (multi-replica, PDB, multi-AZ ideas) |
| 11 | Web servers | Nginx/Apache reverse proxy, SSL termination, upstream to app/container |
| 12 | Monitoring & logging | Prometheus metrics/alerts, Grafana dashboards, ELK pipeline, on-call hygiene |
| 13 | Backup & recovery | RPO/RTO, full/incr/diff, 3-2-1 idea, restore test, K8s/volume/DB angles |
| 14 | System architecture | Layers, deploy topologies, scaling, reliability basics, HA vs DR |
| 15 | Languages for DevOps | Python/Bash (and Java awareness) applied to automation/APIs — not full language courses |
| 16 | AI/LLM in DevOps | JD priority: assist CI/CD, log analysis, incident, docs, IaC/scripts; limits & human review |

### Part 2 — Interview Q&A

| ID | Section | Must cover |
|----|---------|------------|
| 17 | Fit / intro | Tell me about yourself (DevOps), why VNPT, strengths/weakness, tool stack walkthrough |
| 18 | Scenario questions | Broken pipeline; K8s unavailable; alert storm; failed restore; security finding with ATTT; improve architecture |
| 19 | Closing | Smart questions about product, on-call, ATTT process, AI adoption |

## Out of scope (v1)

- Separate multi-page site or quiz engine
- Deep certification dumps (CKA full curriculum, CISSP, etc.)
- Company-confidential VNPT internals
- Fabricated production AI agent platforms

## Success criteria

- Page opens offline and matches existing cheatsheet look/feel
- Every JD keyword (Jenkins, GitLab, Grafana, Prometheus, Ansible, Docker, K8s, Apache/Nginx, ELK, OS topics, AI/LLM) appears in a learnable card
- Bilingual content usable for both silent study and spoken interview
- Linked from hub page so it’s discoverable next to Globant/Kaopiz

## Implementation notes (for plan)

1. Clone structure/CSS patterns from `globant.html` (do not invent a new design system)
2. Build TOC + section shells first, then fill cards by Part 1 priority order (OS/network/security early for “fundamental” ask)
3. Add Part 2 interview cards after fundamentals skeleton exists
4. Wire links in `index.html`
5. Manual open-in-browser check: TOC jump, theme toggle, mobile readability

# Cloud / Infrastructure Interview Cheatsheet — Design Spec

**Date:** 2026-07-17  
**Project:** `interview-cheatsheet`  
**Primary target:** Kaopiz Cloud / Infrastructure Engineer interview  
**Secondary goal:** Reusable pack for future Cloud/Infra interviews  

## Problem

The current single-page bilingual cheatsheet has solid behavioral coverage but:

- Answers sound scripted rather than spoken
- Technical depth is thin vs Kaopiz JD (Terraform, networking, IAM, monitoring/logging, CI/CD tools, Linux fundamentals)
- Missing crib notes for interview theory
- Not structured as a long-term reusable interview pack

## Goals

1. Keep one offline-friendly `index.html` that is fast to scan before an interview
2. Rewrite answers in conversational spoken style (EN + VI)
3. Expand to ~44 bilingual Q&A cards across job-relevant sections
4. Add crib notes under technical topics (definition, trap, follow-up)
5. Stay honest about experience level (GCP/Linux/Docker/CI/CD strong; Terraform beginner–intermediate)

## Non-goals

- Multi-page site or build tooling
- Fake deep production experience in Terraform / Kubernetes / AWS / Prometheus
- Changing visual brand drastically (preserve current theme/layout language)
- Separate mobile app or PDF export

## Approach (approved)

**Approach 1 — Single mega HTML page**

- Same 4-column layout: Question EN | Answer EN | Question VI | Answer VI
- Sticky top bar + section jump navigation
- Technical cards include a crib-notes strip under the grid
- Behavioral cards: spoken answers only (no crib notes required)

## Page structure

### Top bar

- Title: Cloud / Infrastructure Interview Cheat Sheet
- Subtitle: Kaopiz-focused + reusable for future Cloud/Infra interviews
- Theme toggle (keep existing)
- Jump links to sections

### Hero

- Short usage note: open before interview, speak answers out loud, don’t memorize word-for-word
- KPIs: ~44 topics, spoken style, CV-aligned honesty
- Tags aligned to JD: Linux, GCP, Docker, CI/CD, Terraform, Monitoring, Logging, Networking

### Table of contents

Grouped by section (A–I), with anchors to each card.

### Question cards

Each card:

1. Header: number + title + one-line coaching tip
2. 4-column bilingual Q&A grid
3. Optional crib notes strip (technical sections B–H)

## Content voice

### Spoken style (approved)

- Short sentences suitable to say out loud
- Prefer: “I usually…”, “In my case…”, “What I’ve done is…”
- Pattern: what I do → concrete example → what I care about

### Honesty rules (approved)

- Lead with real strengths: GCP, Linux, Docker, CI/CD, troubleshooting, app+ops bridge
- Terraform: concepts understood; ready to apply; not claiming large production Terraform ownership
- AWS/Azure, Kubernetes, Prometheus/Grafana: awareness + learning approach
- Never invent tools/projects not on CV
- Company-specific wording only in “Why this company” and closing pitch; rest stays reusable

## Topic list (~44 cards)

### A. Behavioral / fit (9)

1. Tell me about yourself  
2. Why looking for a new role / why Cloud Infra  
3. Why Kaopiz (or this company)  
4. Why should we hire you  
5. Strengths  
6. Weakness  
7. Current day-to-day role  
8. Hard technical problem  
9. Learning quickly  

### B. Cloud platforms (6)

10. Cloud experience (GCP first; AWS/Azure awareness)  
11. Compute choices: VM vs Cloud Run vs GKE  
12. Storage + Cloud SQL basics  
13. Networking: VPC, subnet, firewall, load balancer  
14. IAM basics (roles, least privilege)  
15. Serverless concepts + tradeoffs  

### C. IaC / Terraform — beginner–intermediate (5)

16. What is IaC / why Terraform  
17. Workflow: init → plan → apply  
18. State & why remote state matters  
19. Modules (concept level)  
20. Common mistakes / how you’d ramp up  

### D. Containers (4)

21. Docker: image vs container, Dockerfile basics  
22. Volumes / networking (practical)  
23. Cloud Run experience  
24. Kubernetes awareness (pod / service / deployment)  

### E. CI/CD (4)

25. CI vs CD in your words  
26. Pipeline you built (mobile/web)  
27. Multi-environment strategy  
28. Tools landscape: GitLab CI / GitHub Actions / Jenkins / CodeBuild / Bamboo (concepts)  

### F. Observability (5)

29. Monitoring vs logging vs tracing  
30. Metrics you’d alert on  
31. Prometheus + Grafana concepts  
32. Logging options: Cloud Logging / Loki / ELK / Graylog  
33. Incident flow: detect → triage → fix → document  

### G. Linux & networking fundamentals (5)

34. Linux troubleshooting checklist  
35. Disk / memory / CPU / process commands  
36. Networking mindset: DNS, ports, curl, connectivity  
37. SSH / permissions / systemd basics  
38. Bash/Python automation examples  

### H. Security & data (4)

39. Secrets management mindset  
40. Encryption / CMEK / Cloud Armor awareness (honest)  
41. Databases: Cloud SQL / PostgreSQL / Redis concepts  
42. AI integration experience (optional plus for JD)

### I. Close (2)

43. Questions for interviewer  
44. 60-second closing pitch  

Optional reusable extras (if kept): working across time zones, server migration story — fold into hard-problem / current-role if needed to avoid bloat.

## Crib notes format (technical cards)

Under each technical card:

- **Know:** 1–2 sentence definition  
- **Trap:** common interview mistake  
- **Follow-up:** one likely next question  

## UX / UI constraints

- Preserve existing CSS theme variables, fonts, dark/light toggle
- Add section nav and crib-notes styles with minimal new CSS
- Keep scroll-margin for sticky header
- Mobile: stack columns as today; crib notes full width
- No new dependencies

## Implementation plan (high level)

1. Extend CSS for section nav + crib notes  
2. Rewrite hero/TOC for new sections  
3. Rewrite existing answers into spoken style  
4. Add new technical + fundamentals cards with bilingual content + crib notes  
5. Update KPI counts and tags  
6. Manual pass: open in browser, check anchors, scan for honesty/scripted tone  

## Success criteria

- Candidate can open one file and prepare for Kaopiz in under 30 minutes of review  
- Answers sound natural when spoken aloud  
- Coverage maps to Kaopiz JD required + preferred skills at concept or practical level  
- Terraform section is useful without overselling experience  
- Pack remains useful for other Cloud/Infra interviews with minimal edits  

## Out of scope for v1

- Print/PDF stylesheet  
- Search/filter UI  
- Spaced-repetition / quiz mode  
- Separate company-specific forks  

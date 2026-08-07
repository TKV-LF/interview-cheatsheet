# CV Deep-Dive Interview Subpage — Design Spec

**Date:** 2026-07-17  
**Project:** `interview-cheatsheet`  
**Approved:** Yes (user chose approach 1 + style C)

## Goal

Create a sibling page focused on CV walkthrough questions: what you did, what you resolved, with bilingual spoken answers and STAR notes.

## Approach

- File: `interview-cheatsheet/cv.html`
- Same visual system as `index.html` (theme, 4-column Q&A)
- Style C: bilingual short spoken answers + STAR strip (Situation · Task · Action · Result) + “Say this” tip
- Cross-links: `index.html` ↔ `cv.html`
- CV source: Full-stack Software Engineer PDF (`CV_Software_Enginner.pdf`) — Akktis, Independent projects, BaseVN, intern

## Non-goals

- Rewriting the main fundamentals sheet
- Inventing metrics/tools not on the CV
- Multi-page framework/build tooling

## Sections & topics (~20)

### A. CV walkthrough
1. Walk me through your CV  
2. Career shift BaseVN → Akktis / why DevOps+full-stack  

### B. Akktis
3. Day-to-day role  
4. Linux server management via SSH  
5. CI/CD for mobile + web multi-env  
6. GCP: Cloud Run, Cloud SQL, Storage  
7. LiteSpeed / Apache  
8. Legacy migration → MySQL on Apache  
9. Documentation / security hardening  
10. Working with France-based / remote team  

### C. IELTS AI Tutor
11. Project overview / your ownership  
12. Cloud Run backend  
13. AI features (chat, TTS, STT)  
14. Langfuse observability  
15. App ↔ teacher portal  

### D. BaseVN
16. Base VSS sync pipelines  
17. Base PIT 500k+ records / launch  
18. Base E-Hiring API integrations  

### E. Other + close
19. Looneyes multilingual / SEO  
20. Jimdo Switzerland site (brief)  
21. Biggest production issue you fixed (CV-framed)  

## Honesty rules

- Stay inside CV bullets; expand into spoken STAR without fake numbers  
- If impact metrics aren’t on CV, use qualitative results  
- Terraform not claimed here unless on CV (it isn’t)

## Success

- Candidate can defend every major CV bullet in under 90 seconds  
- Links work both ways; theme toggle works  

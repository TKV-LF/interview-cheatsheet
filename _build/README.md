# How this site is built

`_build/data/<page>.json` is the source of truth. Every HTML page, `index.html`, and
`assets/search-index.js` is generated from it. Do not edit the HTML by hand: the next
build overwrites it.

```sh
python3 _build/build.py --check   # validate only (ids, empty fields, broken links, long answers)
python3 _build/build.py           # write the site
python3 _build/cards.py list php  # ids and titles on one page
python3 _build/cards.py show new-php-index
```

Edit from Python with `_build/cards.py` (`Site().get/move/add/delete`, then
`save(only=[...pages you touched])`).

Page list, nav order, and hub blurbs live at the top of `build.py`.
`_build/legacy/` holds the old one-off generators. They are history, not the build.

## Card fields

| key | what |
|---|---|
| `id` | lowercase, dashes, unique across the site. Prefix with the page: `js-closure`, `cv-physiofix-pitch` |
| `title` | short, the question as the interviewer would say it, or its topic |
| `hint` | one line: why they ask, or what to lead with |
| `q_en`, `q_vi` | the question, as `<p>…</p>` |
| `a_en`, `a_vi` | the answer you say out loud, HTML |
| `notes` | optional. `<p><strong>Know:</strong> …</p><p><strong>Trap:</strong> …</p><p><strong>Follow-up:</strong> …</p>` |
| `body` | only for cards with no EN/VI split (the Chinese practice cards) |
| `keywords` | optional extra search words |
| `open` | optional, `true` to start expanded |

## Facts that every answer must match

Check `cv/CV_JS.tex`, `cv/CV_PHP.tex`, `cv/CV_DEVOPS.tex`. These were also confirmed by Thủy:

- **Four years** of full-time work since March 2022. Never "about five years".
- Current: independent software engineer since May 2024 — PhysioFix (Apr 2026–), Aquanix (May 2026–), IELTS AI Tutor (2024–).
- **Akktis ended July 2026.** Talk about it in the past tense.
- BaseVN Mar 2022 – Oct 2023 (PIT, VSS, E-Hiring). E-Hiring is VietnamWorks/TopCV integration and candidate sync with retries, request logging, and job monitoring. Do not claim workflow screens, dashboards, or an email server there.
- **Never used Cloud SQL.** Databases actually run: MySQL (BaseVN; at Akktis a legacy custom database migrated to MySQL on Apache, on a Linux server), Firestore (IELTS, PhysioFix, Aquanix). Cloud: Cloud Run, Cloud Build, Cloud Storage, Artifact Registry, Firebase Hosting, one GCE VM (PhysioFix voice process). Errors: Sentry. AI tracing: Langfuse.
- IELTS AI Tutor has about **5,000 users** (true). Do not add a monthly growth number.
- The Jimdo site is real but small: leave it out.
- The gap between Oct 2023 and May 2024 is not covered. Do not write a card about it, and do not claim a direct move from BaseVN to Akktis.
- Name: **Thủy** in Vietnamese, **Thuy** in English.
- The React clients on the CV talk to **Express** APIs, not to PHP.
- The IELTS, PhysioFix, and Aquanix APIs are **TypeScript** + Express.

## How an answer should sound

- **English:** first person, said out loud, 30–90 seconds (about 70–200 words). Natural sentences, not telegraph fragments and not a list of keywords. Rule first, then one concrete example from real work, then stop.
- **Vietnamese:** say the same thing an interviewer would hear in Vietnamese, in natural spoken Vietnamese. Always **"Tôi"**, and "anh/chị" for the interviewer. Keep the tech words Vietnamese developers say in English (API, deploy, cache, query, index). Never translate an English idiom word by word ("muscle", "loud", "honest query", "glue", "spine").
- Coaching ("Lead with…", "Same story as Q4", "Rescue lines are on…") goes in `notes`, never in the answer.
- Honest about gaps: say what you have shipped, what you have only studied, and how you would ramp.
- No company names from old interviews (Globant, Go1, Kaopiz, QNAP, INTOWELL) on the subject pages.

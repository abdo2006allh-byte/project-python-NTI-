# CS Career Compass

A practical guide to 18 Computer Science career fields, plus a local, explainable
AI engine that matches a person's skills against every indexed role.

## Architecture — normal web frontend + minimal Python backend

The frontend is **plain HTML, CSS and JavaScript** — no framework, no build step,
nothing Python-generated. It lives entirely under `public/`:

```
public/
  index.html          Home page
  explore.html         Browse/search all 18 fields
  choose.html           Pick a field from a dropdown
  field.html             Full field detail (skills, tools, roadmap, companies, resources)
  career-match.html    AI Career Fit page
  404.html              Not-found page
  css/style.css         Shared stylesheet
  js/main.js             Shared JS: language toggle, API calls, small render helpers
```

Python (`app.py`) does **only** the two things that genuinely need a backend:
1. Serves the static files in `public/` as-is (HTML/CSS/JS untouched).
2. Exposes a tiny JSON API the frontend JavaScript calls with `fetch()`:
   - `GET  /api/data` → `{ fields, items, model }` — all field + skill/tool data
   - `POST /api/match` → `{ skills, job, limit }` → ranked job-match results (JSON)

No HTML/CSS is generated inside Python anymore. Bilingual text (AR/EN) lives as
`data-en` / `data-ar` attributes in the HTML and is swapped by `main.js`; dynamic
content (fields, skills, match results) is fetched as JSON and rendered by
page-specific `<script>` blocks.

## Local AI model
`career_model.py` uses only the Python standard library:
- skill normalization and aliases
- weighted skill coverage
- weighted cosine similarity
- conservative fuzzy job-title similarity
- role-specific requirements
- transferable-skill signal
- prioritized skill-gap analysis

`career_data.py` is pure data (no logic): `FIELDS` (18 career fields) and
`ITEM_INFO` (170 skills/tools, each with a short description and free + paid
learning resources).

## Privacy
No internet, cloud AI, external API, database, or third-party package is required.
Everything — matching, data, and the web server itself — runs locally.

## Run
```
python app.py
```
Open `http://127.0.0.1:8765/`.

## Accuracy
This is an explainable decision-support model, not a hiring guarantee. Accuracy
depends on the quality and freshness of the project's career dataset.

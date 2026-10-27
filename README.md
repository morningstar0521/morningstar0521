<div align="center">

# Hi, I'm Shubh Ghiya

**Full-stack and backend engineer who ships production systems and honest applied ML.**

Dual degree: **IIT Madras** (Data Science) + **UIT RGPV Bhopal** (CSE), class of 2027.

**Currently:** Full Stack Developer at Nakhrali Luxury · Open to **2026 internships** and **2027 full-time** · [ghiyashubh23@gmail.com](mailto:ghiyashubh23@gmail.com)

[![Portfolio](https://img.shields.io/badge/Portfolio-0d1117?style=for-the-badge&logo=vercel&logoColor=white)](https://sg.ghiyashubh23.workers.dev/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-shubh--ghiya-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/shubh-ghiya)
[![Email](https://img.shields.io/badge/Email-ghiyashubh23-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:ghiyashubh23@gmail.com)
[![Live Build](https://img.shields.io/badge/Live_Build-nakhraliluxury.com-22d3ee?style=for-the-badge&logo=shopify&logoColor=black)](https://nakhraliluxury.com/)

</div>

---

## Start here

1. **[Nakhrali Luxury](https://github.com/morningstar0521/Nakhrali-Luxury)** ([live](https://nakhraliluxury.com/)): a live store that takes real payments. The server never trusts the price sent by the browser.
2. **[Idempotent Event Processor](https://github.com/morningstar0521/Idempotent-Event-Processor)**: kill workers, wipe Redis, flood it with duplicates. Zero lost events, zero duplicate effects, 10/10 invariants pass.
3. **[README Intelligence](https://github.com/morningstar0521/Readme-Intelligence)** ([live](https://readme-intelligence.vercel.app/), [npm](https://www.npmjs.com/package/readme-intel)): a published CLI and GitHub Action that catch README claims the repo contradicts.

---

## What I work on

| Focus | What it means |
| --- | --- |
| **Full-stack systems** | Payments, auth, admin dashboards, deployments |
| **Reliable backends** | Idempotency, outbox, retries, DLQs, failure testing |
| **Applied ML** | Recommender systems, NLP, evaluation, experiment tracking |
| **Shipping and operations** | Docker, CI, EC2, Vercel, HF Spaces |

---

## Featured projects

| Project | What it is | Proof |
|---|---|---|
| [**Nakhrali Luxury**](https://github.com/morningstar0521/Nakhrali-Luxury) | Production e-commerce platform for jewellery and gift hampers. Razorpay payments, admin analytics, security hardening. | **Live since January 2026:** [nakhraliluxury.com](https://nakhraliluxury.com/) · 100+ orders processed · 82 API routes · 12 security issues fixed |
| [**Idempotent Event Processor**](https://github.com/morningstar0521/Idempotent-Event-Processor) | Payment event backend with at-least-once delivery and idempotent effects. | 0 lost events, 0 duplicate effects, 10/10 invariants across chaos runs |
| [**README Intelligence**](https://github.com/morningstar0521/Readme-Intelligence) | Developer tool that reads a README and checks its claims against the repo. | **Live:** [readme-intelligence.vercel.app](https://readme-intelligence.vercel.app/) · published CLI · GitHub Action · 592 core tests |
| [**MovieLens Recommender**](https://github.com/morningstar0521/movielens-recommender) | Recommender system on 25M ratings with ALS, FastAPI and Streamlit. | **Live:** [morningstar0521-movielens-recommender.hf.space](https://morningstar0521-movielens-recommender.hf.space/) · **1.53x NDCG@10** over baseline |
| [**QuickPark**](https://github.com/morningstar0521/Quick-Park) | Parking platform with admin and user dashboards, async emails, PDF receipts. | **Live:** [65-2-59-216.sslip.io](https://65-2-59-216.sslip.io/) · 36 endpoints · **Best Project Award, IIT Madras** |
| [**Comment Category Prediction**](https://github.com/morningstar0521/Comment-Category-Prediction) | 4-class toxicity classifier on 198K comments, 9-model ensemble. | **5th of 2,343** on Kaggle (top 0.21%) |
| [**VentureLens**](https://github.com/morningstar0521/VentureLens) | AI startup validation platform for the Indian market. | **Live:** [venturelens-beige.vercel.app](https://venturelens-beige.vercel.app/) · Gemini + Groq in parallel · **Team project.** |
| [**Aadhaar Command Center**](https://github.com/morningstar0521/UIDAI-Data-Hackathon-Submission) | Fraud and demand signals from UIDAI data across 923 districts. | ~4.94M raw records · 7 ML/statistical models · 31 visualizations · **Team project.** · forecasts are projections |

<details>
<summary><b>Nakhrali Luxury: what I built and why it was hard</b></summary>

<br>

**Stack:** React 19, Vite, Express 5, PostgreSQL (Supabase), Razorpay, Cloudflare R2, Brevo, deployed on Render and GoDaddy.

- **Server-authoritative payments.** The server ignores the amount sent by the browser. It recalculates the cart from the database, locks stock inside a transaction and checks the total again at confirmation. Price tampering does not work.
- **No duplicate orders.** Order creation is idempotent, and a Razorpay webhook catches payments that were captured but never turned into an order.
- **Security layers.** CSRF with double-submit cookies and constant-time comparison, Cloudflare Turnstile, tiered rate limits, JWT invalidation through token versioning, magic-byte image validation, and an SSRF-safe product importer.
- **Search and performance.** PostgreSQL full-text search with a GIN index, two-tier caching, client-side WebP compression, manual bundle splitting.
- **Scale of the codebase:** 21 controllers, 30 pages, 15 admin components, 30 SQL migrations.

</details>

<details>
<summary><b>Idempotent Event Processor: how it stays correct</b></summary>

<br>

**Stack:** TypeScript, Node.js 20, Express 5, PostgreSQL 16, Redis 7 Streams, Docker Compose, k6, Vitest.

- **Transactional outbox.** The event and its outbox row are written in one transaction, so a crash cannot silently drop a message.
- **PostgreSQL is the source of truth.** Each event is processed under a row lock with a status check. Duplicate deliveries become safe no-ops.
- **Recovery.** A reaper reclaims abandoned messages, and a sweeper rebuilds delivery from PostgreSQL if Redis is wiped.
- **Retries and DLQ.** Exponential backoff with full jitter, dead-letter queue, and safe replay where only one concurrent replay wins.
- **Proof, not claims.** 9 in-process and 6 Docker chaos scenarios (crashes, lock expiry, Redis loss, poison messages, duplicate storms), each checked against the same 10 invariants.
- **Local benchmark:** 200 unique events/s for 90 seconds with 3 workers, 18,000 of 18,000 processed, API p95 of 3.78 ms in the duplicate-heavy test. These are local runs, not production numbers.

</details>

<details>
<summary><b>README Intelligence: what it does</b></summary>

<br>

**Stack:** Next.js 14, TypeScript, pnpm monorepo, Zod, Vitest, Playwright, GitHub Actions, Vercel.

- Parses untrusted Markdown and keeps source-line links, so every extracted result points back to the README.
- **Reality Check** compares README claims with manifests, lockfiles, CI files and Dockerfiles. No LLM, and it never runs repository code.
- Reusable **GitHub Action** that comments on pull requests and fails only when a PR introduces a new contradiction.
- Published CLI: `npx readme-intel`.
- Tested on 59 hand-labeled README fixtures, 592 core tests, 10 end-to-end smoke tests.

</details>

<details>
<summary><b>MovieLens Recommender: results</b></summary>

<br>

**Stack:** Python, `implicit` (ALS), SciPy, MLflow, FastAPI, Streamlit, Docker, Hugging Face Spaces, GitHub Actions.

| Model | NDCG@10 |
|---|---|
| Popularity baseline (Bayesian average) | 0.0990 |
| **ALS, 64 factors (deployed)** | **0.1511** |
| ALS, 128 factors | 0.1487 |

- Chronological train/test split on a global timestamp, so the model never sees the future.
- Cold-start users work: pick movies you like and get recommendations with a "because you liked X" reason.
- Doubling model size made results worse. I kept that result in the experiment log.
- 5 tracked runs, 13 CI tests, one Docker container.

</details>

<details>
<summary><b>QuickPark: concurrency and deployment</b></summary>

<br>

**Stack:** Flask, Vue 3, SQLAlchemy, Celery, Redis, Docker Compose, Caddy, AWS EC2.

- **No double booking.** Spots are claimed with an atomic compare-and-set update, backed by partial unique indexes. The losing request gets a clear HTTP 409.
- I first reproduced the bug: with the old read-then-write code, 40 parallel requests booked 40 times on a 5-spot lot. The fix gave exactly 5 bookings.
- Concurrency test: 5 scenarios, 15 assertions, 15 passing inside the production container on EC2.
- Role-based access (admin and user), Celery Beat reports, PDF receipts by email, 30-day analytics.
- Deployed with Docker Compose behind Caddy with automatic HTTPS.

</details>

<details>
<summary><b>Comment Category Prediction: how I got to 5th place</b></summary>

<br>

**Stack:** Python, scikit-learn, XGBoost, LightGBM, SciPy.

- 140+ hand-built features, five different text representations (word, char, count-based).
- 9-model ensemble with blend weights found by Nelder-Mead on out-of-fold predictions.
- Every model is a full `Pipeline`, so vectorizers and scalers only ever see training folds.
- Handled class imbalance (58% / 8% / 32% / 3%) with class weights. SMOTE was tested and hurt.
- **0.84870 public leaderboard score**, 0.91589 out-of-fold accuracy.

</details>

---

## Tech stack

**Languages:** ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white) ![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?logo=typescript&logoColor=white)

**Frontend:** ![React](https://img.shields.io/badge/React-61DAFB?logo=react&logoColor=black) ![Next.js](https://img.shields.io/badge/Next.js-000000?logo=nextdotjs&logoColor=white)

**Backend:** ![Node.js](https://img.shields.io/badge/Node.js-339933?logo=nodedotjs&logoColor=white) ![Express](https://img.shields.io/badge/Express-000000?logo=express&logoColor=white)

**Data and messaging:** ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql&logoColor=white) ![Redis](https://img.shields.io/badge/Redis-DC382D?logo=redis&logoColor=white)

**ML and data:** ![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikitlearn&logoColor=white)

**Infra and tools:** ![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white) ![AWS](https://img.shields.io/badge/AWS_EC2-232F3E?logo=amazonaws&logoColor=white) ![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?logo=githubactions&logoColor=white)

**Testing:** Vitest, Playwright, pytest, k6, Node test runner

**Also:** Flask, FastAPI, Celery, Vue, Tailwind, Vite, Supabase, MLflow, XGBoost, LightGBM, pandas, NumPy

**Services and platforms:** Razorpay, Google OAuth, NextAuth, Gemini, Groq, Hugging Face Spaces, Vercel, Cloudflare, Render

---

## Engineering habits

- **Failure first.** I test crashes, retries and duplicates, not only the happy path.
- **Numbers I can prove.** Every metric on this page comes from code, a test run or a public leaderboard.
- **Honest results.** I keep negative results and label local benchmarks as local.
- **Security by default.** Server-side validation, rate limits and least trust for anything coming from the client.

---

## Education and recognition

| | |
|---|---|
| **IIT Madras** | B.S. Data Science and Applications, 2023-2027, GPA 8.49 / 10 |
| **UIT RGPV Bhopal** | B.Tech Computer Science and Engineering, 2023-2027, GPA 8.16 / 10 |
| **Best Project Award** | QuickPark, IIT Madras (2025) |
| **Kaggle** | 5th of 2,343 in a comment classification competition |
| **Certifications** | Oracle Cloud: Generative AI, Data Science, AI Vector Search Professionals (2025) · McKinsey Forward Program (2025) |
| **Recommendation** | Letter of Recommendation from the Head of Student Affairs, IIT Madras BS (2025) |

## Leadership

- **Secretary, Synapse Society** (1,600+ members), IIT Madras, 2025-26
- **Deputy Secretary, Kanha House** (4,000+ students), IIT Madras, 2024-25: led 12 Paradox'25 programs and co-founded 3 communities with 1,200+ members

---

## GitHub stats

<div align="center">

<img height="165" src="https://github-readme-stats.vercel.app/api?username=morningstar0521&show_icons=true&theme=tokyonight&hide_border=true" alt="GitHub stats" />
<img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=morningstar0521&layout=compact&theme=tokyonight&hide_border=true" alt="Top languages" />

</div>

---

<div align="center">

**Let's build something that does not break at 2 AM.**

[Portfolio](https://sg.ghiyashubh23.workers.dev/) · [LinkedIn](https://linkedin.com/in/shubh-ghiya) · [Email](mailto:ghiyashubh23@gmail.com)

</div>

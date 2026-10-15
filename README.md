# Advisor Team

Website for the **Business Snapshot**: a one-time data report for small businesses without a data team.

- `public/` holds every page (home, snapshot, case study, pricing, news, sign up, log in, account), `assets/` and `img/`. Static, no build step.
- `src/worker.js` is the account API (`/api/signup`, `/api/login`, `/api/logout`, `/api/me`), backed by the D1 database `advisor-team-users`. Its tables are in `schema.sql`.
- Cloudflare Workers Builds deploys every push to `main`.

## Local preview
```
npx wrangler d1 execute advisor-team-users --local --file=schema.sql
npx wrangler dev
```

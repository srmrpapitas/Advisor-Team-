# Advisor Team

One-page website for the **Business Snapshot**: a one-time data report (charts + slides) for small businesses without a data team.

- `public/index.html` is the whole site (static, no build step).
- `wrangler.jsonc` serves `public/` as a Cloudflare Worker with static assets.

## Deploy
Cloudflare dashboard → Workers & Pages → Create → Import a repository → `Advisor-Team-`. Build command: none. Deploy command: `npx wrangler deploy`. Every push to `main` then redeploys.

## Before going live
Search `TODO` in `public/index.html` and replace the Stripe payment link, the booking link and the contact email.

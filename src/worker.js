// API for accounts. Everything outside /api/* is served from ./public.
const SESSION_DAYS = 30;
const ITERATIONS = 100000;

const json = (data, status = 200, headers = {}) =>
  new Response(JSON.stringify(data), { status, headers: { 'content-type': 'application/json', ...headers } });

const toHex = (buf) => [...new Uint8Array(buf)].map((b) => b.toString(16).padStart(2, '0')).join('');
const randomHex = (n) => toHex(crypto.getRandomValues(new Uint8Array(n)));

async function hashPassword(password, saltHex) {
  const key = await crypto.subtle.importKey('raw', new TextEncoder().encode(password), 'PBKDF2', false, ['deriveBits']);
  const salt = Uint8Array.from(saltHex.match(/../g).map((h) => parseInt(h, 16)));
  const bits = await crypto.subtle.deriveBits({ name: 'PBKDF2', hash: 'SHA-256', salt, iterations: ITERATIONS }, key, 256);
  return toHex(bits);
}

function sameHash(a, b) {
  if (a.length !== b.length) return false;
  let diff = 0;
  for (let i = 0; i < a.length; i++) diff |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return diff === 0;
}

function sessionToken(request) {
  const m = (request.headers.get('cookie') || '').match(/(?:^|;\s*)session=([a-f0-9]{64})/);
  return m ? m[1] : null;
}

async function startSession(env, userId) {
  const token = randomHex(32);
  const expires = new Date(Date.now() + SESSION_DAYS * 864e5);
  await env.DB.prepare('INSERT INTO sessions (token, user_id, expires_at) VALUES (?, ?, ?)').bind(token, userId, expires.toISOString()).run();
  return `session=${token}; Path=/; HttpOnly; Secure; SameSite=Lax; Expires=${expires.toUTCString()}`;
}

async function readBody(request) {
  try { return await request.json(); } catch { return {}; }
}

async function signup(request, env) {
  const { name = '', email = '', company = '', password = '' } = await readBody(request);
  const cleanEmail = String(email).trim().toLowerCase();
  if (!String(name).trim() || !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(cleanEmail)) return json({ error: 'Please enter your name and a valid email.' }, 400);
  if (String(password).length < 8) return json({ error: 'Password must be at least 8 characters.' }, 400);
  const exists = await env.DB.prepare('SELECT id FROM users WHERE email = ?').bind(cleanEmail).first();
  if (exists) return json({ error: 'An account with this email already exists.' }, 409);
  const salt = randomHex(16);
  const hash = await hashPassword(String(password), salt);
  const res = await env.DB.prepare('INSERT INTO users (email, name, company, pass_hash, salt) VALUES (?, ?, ?, ?, ?)')
    .bind(cleanEmail, String(name).trim().slice(0, 120), String(company).trim().slice(0, 160), hash, salt).run();
  const cookie = await startSession(env, res.meta.last_row_id);
  return json({ ok: true }, 201, { 'set-cookie': cookie });
}

async function login(request, env) {
  const { email = '', password = '' } = await readBody(request);
  const user = await env.DB.prepare('SELECT id, pass_hash, salt FROM users WHERE email = ?').bind(String(email).trim().toLowerCase()).first();
  if (!user || !sameHash(await hashPassword(String(password), user.salt), user.pass_hash)) return json({ error: 'Wrong email or password.' }, 401);
  const cookie = await startSession(env, user.id);
  return json({ ok: true }, 200, { 'set-cookie': cookie });
}

async function me(request, env) {
  const token = sessionToken(request);
  if (!token) return json({ user: null });
  const user = await env.DB.prepare(
    'SELECT u.name, u.email, u.company, u.created_at FROM sessions s JOIN users u ON u.id = s.user_id WHERE s.token = ? AND s.expires_at > ?'
  ).bind(token, new Date().toISOString()).first();
  return json({ user: user || null });
}

async function logout(request, env) {
  const token = sessionToken(request);
  if (token) await env.DB.prepare('DELETE FROM sessions WHERE token = ?').bind(token).run();
  return json({ ok: true }, 200, { 'set-cookie': 'session=; Path=/; HttpOnly; Secure; SameSite=Lax; Max-Age=0' });
}

const routes = {
  'POST /api/signup': signup,
  'POST /api/login': login,
  'POST /api/logout': logout,
  'GET /api/me': me,
};

export default {
  async fetch(request, env) {
    const { pathname } = new URL(request.url);
    const handler = routes[`${request.method} ${pathname}`];
    if (handler) {
      try { return await handler(request, env); }
      catch (err) { console.error(err); return json({ error: 'Something went wrong. Please try again.' }, 500); }
    }
    if (pathname.startsWith('/api/')) return json({ error: 'Not found' }, 404);
    return env.ASSETS.fetch(request);
  },
};

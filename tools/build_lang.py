import glob, json, os, re, html as H
HERE = os.path.dirname(os.path.abspath(__file__))
R = os.path.join(HERE, '..', 'public') + '/'
LANGS = ['nl', 'es']
ACC = {
    'nl': {'Hello, ': 'Hallo, ', 'Signed in as ': 'Ingelogd als '},
    'es': {'Hello, ': 'Hola, ', 'Signed in as ': 'Sesión iniciada como '},
}
LANG_DIR = re.compile(r'/public/(' + '|'.join(LANGS) + r')/')

def url(f):  # file path -> public URL
    u = '/' + f[len(R):]
    u = re.sub(r'index\.html$', '', u)
    return re.sub(r'\.html$', '', u)

def alt(h, en_url):
    tags = f'<link rel="alternate" hreflang="en" href="{en_url}">' + ''.join(
        f'<link rel="alternate" hreflang="{l}" href="/{l}{en_url}">' for l in LANGS)
    h = re.sub(r'<link rel="alternate" hreflang[^>]*>', '', h)
    return h.replace('</head>', tags + '\n</head>', 1)

sources = [f for f in glob.glob(R + '**/*.html', recursive=True) if not LANG_DIR.search(f)]
for f in sources:
    txt = alt(open(f).read(), url(f))
    open(f, 'w').write(txt)

for lang in LANGS:
    D = json.load(open(os.path.join(HERE, lang + '.json')))
    pairs = sorted(D.items(), key=lambda p: -len(p[0]))
    for f in sources:
        src = open(f).read()
        u = url(f)
        h = src.replace('<html lang="en">', f'<html lang="{lang}">')
        for en, tr in pairs:
            for e in {en, H.escape(en, quote=False), H.escape(en)}:
                h = re.sub(r'(>\s*)' + re.escape(e) + r'(\s*<)', lambda m: m.group(1) + H.escape(tr, quote=False) + m.group(2), h)
                h = re.sub(r'(="\s*)' + re.escape(e) + r'(\s*")', lambda m: m.group(1) + H.escape(tr) + m.group(2), h)
        for a, b in ACC[lang].items():
            h = h.replace(a, b)
        # internal links and redirects -> /<lang>
        h = re.sub(r'(href=|location\.href=)"/(?!assets/|img/|api/|(?:' + '|'.join(LANGS) + r')/)', r'\1"/' + lang + '/', h)
        h = re.sub(r'(,"/api/\w+",)"/', r'\1"/' + lang + '/', h)
        h = alt(h, u)
        out = R + lang + '/' + f[len(R):]
        os.makedirs(os.path.dirname(out), exist_ok=True)
        open(out, 'w').write(h)
print('ok')

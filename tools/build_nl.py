import glob, json, os, re, html as H
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'public') + '/'
D = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'nl.json')))
pairs = sorted(D.items(), key=lambda p: -len(p[0]))
ACC = {
 'Hello, ': 'Hallo, ', 'Signed in as ': 'Ingelogd als ',
}

def url(f):  # file path -> public URL
    u = '/' + f[len(R):]
    u = re.sub(r'index\.html$', '', u)
    return re.sub(r'\.html$', '', u)

def alt(h, en_url):
    nl_url = '/nl' + en_url if en_url != '/' else '/nl/'
    tag = f'<link rel="alternate" hreflang="en" href="{en_url}"><link rel="alternate" hreflang="nl" href="{nl_url}">'
    h = re.sub(r'<link rel="alternate" hreflang[^>]*>', '', h)
    return h.replace('</head>', tag + '\n</head>', 1)

for f in glob.glob(R + '**/*.html', recursive=True):
    if f.startswith(R + 'nl/'):
        continue
    src = open(f).read()
    u = url(f)
    open(f, 'w').write(alt(src, u))
    h = src.replace('<html lang="en">', '<html lang="nl">')
    for en, nl in pairs:
        for e in {en, H.escape(en, quote=False), H.escape(en)}:
            h = re.sub(r'(>\s*)' + re.escape(e) + r'(\s*<)', lambda m: m.group(1) + H.escape(nl, quote=False) + m.group(2), h)
            h = re.sub(r'(="\s*)' + re.escape(e) + r'(\s*")', lambda m: m.group(1) + H.escape(nl) + m.group(2), h)
    for a, b in ACC.items():
        h = h.replace(a, b)
    # internal links and redirects -> /nl
    h = re.sub(r'(href=|location\.href=)"/(?!assets/|img/|api/|nl/)', r'\1"/nl/', h)
    h = re.sub(r'(,"/api/\w+",)"/', r'\1"/nl/', h)
    h = alt(h, u)
    out = R + 'nl/' + f[len(R):]
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, 'w').write(h)
print('ok')

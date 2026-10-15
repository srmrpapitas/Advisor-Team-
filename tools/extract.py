import glob,json,re,os
from html.parser import HTMLParser
S={}
class P(HTMLParser):
    def __init__(s): super().__init__(); s.skip=0
    def handle_starttag(s,t,a):
        if t in('script','style'): s.skip+=1
        d=dict(a)
        for k in('title','aria-label','placeholder','alt'):
            if d.get(k): S[d[k].strip()]=''
        if t=='meta' and d.get('name')=='description' or (t=='meta' and d.get('property') in('og:title','og:description')): S[d['content'].strip()]=''
    def handle_endtag(s,t):
        if t in('script','style'): s.skip-=1
    def handle_data(s,d):
        if not s.skip and d.strip() and re.search('[A-Za-z]',d): S[d.strip()]=''
for f in [g for g in glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','public','**','*.html'),recursive=True) if '/public/nl/' not in g]: P().feed(open(f).read())
D=json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'nl.json')))
miss=[k for k in S if k not in D]
print(len(S),'strings,',len(miss),'without Dutch (add them to tools/nl.json):')
for k in miss: print(' ',repr(k))

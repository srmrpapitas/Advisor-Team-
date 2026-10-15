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
for f in [g for g in glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','public','**','*.html'),recursive=True) if not re.search(r'/public/(nl|es)/',g)]: P().feed(open(f).read())
H=os.path.dirname(os.path.abspath(__file__))
for lang,name in (('nl','Dutch'),('es','Spanish')):
    f=os.path.join(H,lang+'.json')
    D=json.load(open(f)) if os.path.exists(f) else {}
    miss=[k for k in S if k not in D]
    print(len(S),'strings,',len(miss),'without',name,'(add them to tools/'+lang+'.json):')
    for k in miss: print(' ',repr(k))

import os
R=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','public')+'/'
S1='https://buy.stripe.com/9B600j4yIecjepYaPzaZi00'
S2='https://buy.stripe.com/6oU4gzfdm3xFepY0aVaZi02'
S3='https://buy.stripe.com/14A28r9T20lt81Ag9TaZi03'
def page(path,title,desc,body,solid=False,extra=''):
    html=f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:image" content="/img/hero.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500&family=Barlow+Condensed:wght@600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/style.css">
</head>
<body{' data-solid="1"' if solid else ''}>
{body}
<script src="/assets/app.js"></script>
{extra}
</body>
</html>
'''
    os.makedirs(os.path.dirname(R+path),exist_ok=True); open(R+path,'w').write(html)

NEWS=[
 ('/news/launch','15 Oct 2026','Advisor Team launches the Business Snapshot','A one-time data report for small businesses that have the numbers but no one to read them.','orbits.jpg'),
 ('/news/case-study-tenerife','15 Oct 2026','652 handwritten tickets, one clear plan','What one summer of sales at an excursion booth in Tenerife revealed about hours, margins and customers.','ocean.jpg'),
 ('/news/no-data-team','15 Oct 2026','You do not need a data team. You need answers.','Why most small businesses already own the data that would grow them, and what stops them using it.','network.jpg'),
]
def cards(): return '<div class="news">'+''.join(f'<a class="card fade" href="{u}"><div class="img" style="background-image:url(/img/{img})"></div><div class="body"><div class="date">{d}</div><h3>{t}</h3><p>{s}</p></div></a>' for u,d,t,s,img in NEWS)+'</div>'

def scene(img,kick,h,lead,btns,tag='h2'):
    return f'<section class="scene" style="background-image:url(/img/{img})"><div class="inner fade"><p class="kicker">{kick}</p><{tag}>{h}</{tag}><p class="lead">{lead}</p>{btns}</div></section>'


SECTORS=[('tourism','Tourism & excursions','live','1 live case · Tenerife','ocean.jpg'),
 ('restaurants','Restaurants & bars','soon','Coming soon','plates.jpg'),
 ('retail','Shops & retail','soon','Coming soon','retail.jpg'),
 ('beauty','Beauty & wellness','soon','Coming soon','rings.jpg'),
 ('fitness','Gyms & fitness','soon','Coming soon','pulse.jpg'),
 ('real-estate','Real estate & rentals','soon','Coming soon','city.jpg')]
def sector_cards():
    return ''.join(f'<a class="sector{" soon" if st=="soon" else ""}" href="/sectors/{k}" style="background-image:url(/img/{img})"><span class="tag">{"<span class=live></span>Live" if st=="live" else "Next"}</span><h3>{n}</h3><p>{d}</p></a>' for k,n,st,d,img in SECTORS)
def portal(title='Explore by sector'):
    return f'<section class="portal" data-rail><div class="railhead"><div><p class="kicker">The portal</p><h2>{title}</h2></div><div class="arrows"><button data-dir="-1" aria-label="Previous">&larr;</button><button data-dir="1" aria-label="Next">&rarr;</button></div></div><div class="rail">{sector_cards()}</div></section>'

# HOME
page('index.html','Advisor Team · Business Snapshot','A one-time data report for small businesses: what sells, when, to whom, and what to change.',
 scene('hero.jpg','Business Snapshot','Your data knows how to grow your business','We turn the sales records you already keep into a clear report: what sells, when, to whom, and the five changes worth making.','<a class="btn" href="/snapshot">Discover the Snapshot</a><a class="btn gold" href="/pricing">€590 · Order now</a>','h1').replace('</section>','<div class="scroll">Scroll</div></section>',1)+portal()+
 scene('orbits.jpg','The Snapshot','One report. Every number that matters.','Charts, findings and a 90-day plan in a 10 to 15 slide deck. Built from your own data, checked against your market.','<a class="btn" href="/snapshot">How it works</a>')+
 scene('skyline.jpg','Case study · Tenerife','48% of sales in four hours','An excursion booth learned when to staff, what to recommend first, and why its customers change with the season.','<a class="btn" href="/sectors/tourism/la-siesta-tenerife">Open the live case</a>')+
 f'<section class="block"><div class="wrap"><p class="kicker">Latest</p><h2 style="margin-bottom:46px">News</h2>{cards()}<a class="btn" href="/news">All news</a></div></section>'+
 scene('trail.jpg','Start today','Pay once. Know exactly where you stand.','No subscription, no software to install. Send what you have and receive a finished, checked report.','<a class="btn gold" href="/pricing">See pricing</a><a class="btn" href="/signup">Create an account</a>'))

# SNAPSHOT
page('snapshot.html','The Snapshot · Advisor Team','What the Business Snapshot includes, how it works and why it is worth €590.',
 '<header class="pagehead" style="background-image:url(/img/orbits.jpg)"><div class="inner"><p class="kicker">The Snapshot</p><h1>A data team for one week</h1><p class="lead">Big companies have analysts who read their numbers every day. You get the same thinking, once, for a fixed price.</p></div></header>'+
 '<section class="block"><div class="wrap"><p class="kicker">How it works</p><h2 style="margin-bottom:46px">Four steps</h2><div class="grid g4">'+
 ''.join(f'<div class="cell fade"><div class="num">0{i+1}</div><h3 style="margin-top:12px">{t}</h3><p>{d}</p></div>' for i,(t,d) in enumerate([('Send your data','Till exports, spreadsheets, invoices, photos of receipts, even a WhatsApp group of tickets.'),('We read every number','We clean it, find the patterns and compare them with public market data and competitor prices.'),('You receive the deck','10 to 15 slides in PowerPoint and PDF: charts, findings and a 90-day action plan.'),('Optional Zoom','A live walkthrough of every chart, in English, wherever you are.')]))+'</div></div></section>'+
 '<section class="block"><div class="wrap split"><div class="fade"><p class="kicker">Why €590</p><h2>The report pays for itself with one decision</h2><p class="lead">In our first case study, one change (recommending the products with the highest commission first) is estimated at about €1,400 more per quarter. That is more than twice the price of the report, from a single slide.</p><a class="btn" href="/case-study">See the numbers</a></div><div class="media fade" style="background-image:url(/img/skyline.jpg)"></div></div></section>'+
 '<section class="block"><div class="wrap"><p class="kicker">What you get</p><h2 style="margin-bottom:46px">Inside every Snapshot</h2><div class="grid g3">'+
 ''.join(f'<div class="cell fade"><h3>{t}</h3><p>{d}</p></div>' for t,d in [('When you sell','Sales by week, day and hour, so you staff and promote at the right time.'),('What earns most','Revenue and margin by product or category, so you push what pays.'),('Who buys','Customer mix compared with your market, so you see who you are missing.'),('Against competitors','Your prices next to the big online platforms and what that means for your pitch.'),('How you get paid','Payment methods and gaps in your records, so the till always adds up.'),('What to do next','Five concrete changes, a 90-day plan and four numbers to track every month.')])+'</div></div></section>'+
 '<section class="block"><div class="wrap split"><div class="media fade" style="background-image:url(/img/network.jpg)"></div><div class="fade"><p class="kicker">Your data</p><h2>Used for your report only</h2><p class="lead">Your data is used only to build your Snapshot. Customer names and phone numbers are never copied into it, and it is never shared.</p><a class="btn gold" href="/pricing">Order your Snapshot</a></div></div></section>')

# CASE STUDY
bars=[('Water sports',43,1),('Buggy & quads',40,1),('Rentals',35,0),('Boat trips',31,0),('Theme parks',30,0),('Guided tours',23,0)]
page('case-study.html','Case study · Tenerife excursion booth','652 handwritten tickets from an excursion booth in Tenerife, turned into a 90-day plan.',
 '<header class="pagehead" style="background-image:url(/img/ocean.jpg)"><div class="inner"><p class="kicker">Case study · Playa de las Américas, Tenerife</p><h1>652 tickets, one summer, one plan</h1><p class="lead">A family-run excursion booth sent us its staff WhatsApp group: photos of every handwritten sale from July to October 2026.</p></div></header>'+
 '<section class="block"><div class="wrap"><div class="grid g4">'+''.join(f'<div class="cell fade"><div class="stat">{a}<small>{b}</small></div><p>{c}</p></div>' for a,b,c in [('652','','sales read in 13 weeks'),('48','%','of sales between 11:00 and 15:00'),('43','%','commission on water sports'),('€130','','median ticket, 3.3 people')])+'</div></div></section>'+
 '<section class="block"><div class="wrap split"><div class="fade"><p class="kicker">Finding 01</p><h2>Not all sales are equal</h2><p class="lead">Water sports and buggies leave 40 to 43% of the price at the booth. Guided tours leave 23%. Same customer, same effort, nearly double the commission.</p></div><div class="fade">'+
 ''.join(f'<div class="bar"><span>{n}</span><i class="{"hi" if h else ""}" style="width:{v/43*100:.0f}%"></i><b>{v}%</b></div>' for n,v,h in bars)+'<p class="note">Commission as % of sale price. Sample of 108 tickets, summer 2026.</p></div></div></section>'+
 '<section class="block"><div class="wrap split"><div class="media fade" style="background-image:url(/img/skyline.jpg)"></div><div class="fade"><p class="kicker">Finding 02</p><h2>Four hours decide the day</h2><p class="lead">316 of 652 sales happened between 11:00 and 15:00. That is when two people should be at the counter, and nobody on a break.</p></div></div></section>'+
 '<section class="block"><div class="wrap split"><div class="fade"><p class="kicker">Finding 03</p><h2>Same price as the big platforms</h2><p class="lead">We compared eight products with GetYourGuide in Costa Adeje. Prices were the same. The booth wins on advice in person, paying only a deposit, and someone to call if plans change, but the platforms win on reviews. So reviews became part of the plan.</p></div><div class="media fade" style="background-image:url(/img/network.jpg)"></div></div></section>'+
 '<section class="block"><div class="wrap"><p class="kicker">The plan</p><h2 style="margin-bottom:46px">Five changes</h2><div class="grid g3">'+''.join(f'<div class="cell fade"><div class="num">0{i+1}</div><h3 style="margin-top:12px">{t}</h3><p>{d}</p></div>' for i,(t,d) in enumerate([('Recommend first what pays most','Water sports and buggies first. Estimated +€1,400 per quarter if 10% of sales shift.'),('Same price, better service','A sign: same price as online, pay only the deposit, book on WhatsApp.'),('Language by season','Summer: Spanish visitors are 16% of the island but 8% of customers. Winter: German and Nordic.'),('Two people at peak','Full staff from 11:00 to 15:00.'),('Digital tickets','A 30-second form per sale replaces photos and makes next month\'s report automatic.')]))+
 '<div class="cell fade" style="display:flex;flex-direction:column;justify-content:center"><h3>Want this for your business?</h3><a class="btn gold" href="/pricing">Get your Snapshot</a></div></div><p class="note">Figures from a sample of the booth\'s own tickets and public data (Frontur, GetYourGuide). Estimates are labelled as such.</p></div></section>')

# PRICING
plans=[('Business Snapshot','€590','one-time',['10 to 15 slide report, PowerPoint and PDF','Charts built from your own data','Market and competitor price check','90-day action plan'],S1,'Buy the Snapshot',True),
       ('Snapshot update','€290','returning clients',['The same report with your new data','Before and after comparison','See which changes worked'],S2,'Buy an update',False),
       ('Zoom walkthrough','+€200','add-on',['Live session on your report','Every question answered','In English, any country'],S3,'Add a Zoom call',False)]
page('pricing.html','Pricing · Advisor Team','Business Snapshot €590 one-time. Update €290. Zoom walkthrough €200.',
 '<header class="pagehead" style="background-image:url(/img/trail.jpg)"><div class="inner"><p class="kicker">Pricing</p><h1>Pay once. No subscription.</h1><p class="lead">You pay for the business as it is today. Come back when you want to measure what changed.</p></div></header>'+
 '<section class="block"><div class="wrap"><div class="grid g3">'+''.join(f'<div class="plan fade{" main" if m else ""}"><p class="kicker" style="margin:0">{n}</p><div class="price">{p} <small>{s}</small></div><ul>{"".join(f"<li>{x}</li>" for x in li)}</ul><a class="btn{" gold" if m else ""}" href="{u}">{b}</a></div>' for n,p,s,li,u,b,m in plans)+'</div>'+
 '<p class="note">Secure payment by card or PayPal through Stripe. After paying you will receive an email to send your data.</p></div></section>'+
 '<section class="block"><div class="wrap prose"><p class="kicker">Questions</p><h2 style="margin-top:0">Before you order</h2>'+
 ''.join(f'<h3 style="margin-top:34px">{q}</h3><p>{a}</p>' for q,a in [('What data do I need?','Whatever you already keep: a till export, a spreadsheet, invoices or photos of receipts. If it records what was sold, when and for how much, it works.'),('Is my data safe?','Your data is used only to build your report. Customer names and phone numbers are never copied into it.'),('Why not just ask an AI chatbot?','You can, if you have the time to clean the data, check every number and research your market. We do that work and hand you a finished, checked report.'),('Do you work outside Spain?','Yes. Reports are in English and calls are on Zoom, wherever you are.')])+'</div></section>')

# NEWS index + articles
page('news.html','News · Advisor Team','News and case studies from Advisor Team.',
 '<header class="pagehead" style="background-image:url(/img/network.jpg);min-height:52vh"><div class="inner"><p class="kicker">Newsroom</p><h1>News</h1></div></header>'+f'<section class="block"><div class="wrap">{cards()}</div></section>')
art={
'/news/launch':['<p>Most small businesses already record every sale. It sits in a till, a spreadsheet or a phone. What they lack is someone with the time to read it.</p><p>The Business Snapshot is a one-time report that does exactly that. You send the data you have; we return a 10 to 15 slide deck with charts, findings and a 90-day plan.</p><h2>Simple pricing</h2><p>€590 one time. An update with new data costs €290, so you can measure what changed. A Zoom walkthrough is available for €200.</p><p><a class="btn gold" href="/pricing">See pricing</a></p>'],
'/news/case-study-tenerife':['<p>Our first Snapshot was for a family-run excursion booth on Playa de las Américas. Its staff sent a photo of every handwritten ticket to a WhatsApp group: 652 sales from July to October 2026.</p><p>From those photos we found that 48% of sales happen between 11:00 and 15:00, that water sports leave nearly twice the commission of guided tours, and that German and Spanish visitors are under-represented compared with the island as a whole.</p><p><a class="btn" href="/case-study">Read the full case study</a></p>'],
'/news/no-data-team':['<p>Large companies employ analysts to read their numbers. Small businesses rarely can, so decisions are made on instinct: who to staff, what to recommend, which customers to chase.</p><p>The data to answer those questions is usually already there. It is just scattered and unread. One careful pass through it often finds a change worth more than the cost of looking.</p><p>That is the idea behind the Business Snapshot: one report, a fixed price, and a plan you can act on the next morning.</p><p><a class="btn" href="/snapshot">How the Snapshot works</a></p>'],
}
for u,d,t,s,img in NEWS:
    page(u.lstrip('/')+'.html',t+' · Advisor Team',s,f'<header class="pagehead" style="background-image:url(/img/{img})"><div class="inner"><p class="kicker">News · {d}</p><h1 style="font-size:clamp(38px,5vw,68px)">{t}</h1><p class="lead">{s}</p></div></header><section class="block"><div class="wrap prose">{art[u][0]}</div></section>')

# AUTH
def authpage(path,title,img,h,fields,btn,api,done,foot):
    page(path,title+' · Advisor Team',title,f'<div class="formwrap"><div class="art" style="background-image:url(/img/{img})"></div><div class="side"><form id="f" novalidate><p class="kicker">Advisor Team</p><h2>{h}</h2>'+''.join(f'<label for="{n}">{l}</label><input id="{n}" name="{n}" type="{t}" autocomplete="{a}"{" required" if r else ""}>' for n,l,t,a,r in fields)+f'<button class="btn gold" type="submit">{btn}</button><div class="msg" role="status"></div><p class="small">{foot}</p></form></div></div>',solid=True,extra=f'<script>postForm(document.getElementById("f"),"{api}","{done}")</script>')
authpage('signup.html','Sign up','orbits.jpg','Create your account',[('name','Name','text','name',1),('company','Business','text','organization',0),('email','Email','email','email',1),('password','Password (8+ characters)','password','new-password',1)],'Create account','/api/signup','/account','Already have an account? <a href="/login">Log in</a>')
authpage('login.html','Log in','trail.jpg','Welcome back',[('email','Email','email','email',1),('password','Password','password','current-password',1)],'Log in','/api/login','/account','New here? <a href="/signup">Create an account</a>')
page('account.html','Your account · Advisor Team','Your Advisor Team account.','<header class="pagehead" style="background-image:url(/img/hero.jpg);min-height:52vh"><div class="inner"><p class="kicker">Account</p><h1 id="hi">Your account</h1></div></header><section class="block"><div class="wrap split"><div><p class="lead" id="who">Loading…</p><a class="btn gold" href="/pricing">Order a Snapshot</a> <button class="btn" id="out">Log out</button></div><div class="cell" style="border:1px solid var(--line)"><h3>Next steps</h3><p>1. Order your Snapshot on the pricing page.</p><p>2. Reply to the confirmation email with your data.</p><p>3. Receive your report, then book a Zoom if you want one.</p></div></div></section>',
 extra='<script>fetch("/api/me").then(r=>r.json()).then(d=>{if(!d.user){location.href="/login";return}document.getElementById("hi").textContent="Hello, "+d.user.name;document.getElementById("who").textContent="Signed in as "+d.user.email+(d.user.company?" · "+d.user.company:"")});document.getElementById("out").onclick=()=>fetch("/api/logout",{method:"POST"}).then(()=>location.href="/")</script>')
page('404.html','Not found · Advisor Team','Page not found.',scene('hero.jpg','404','Lost in orbit','This page does not exist.','<a class="btn" href="/">Back home</a>','h1'))

# ---------- SECTORS ----------
page('sectors.html','Sectors · Advisor Team','Business Snapshots by sector: tourism, restaurants, retail, beauty, fitness and real estate.',
 '<header class="pagehead" style="background-image:url(/img/network.jpg);min-height:52vh"><div class="inner"><p class="kicker">The portal</p><h1>Every sector has its own numbers</h1><p class="lead">Pick a sector to see live Snapshots of real businesses. More sectors open as new clients join.</p></div></header>'+portal('Choose a sector'))
for k,n,st,d,img in SECTORS:
    if st=='live': continue
    page(f'sectors/{k}.html',f'{n} · Advisor Team',f'Business Snapshot for {n.lower()}.',
     f'<header class="pagehead" style="background-image:url(/img/{img})"><div class="inner"><p class="crumbs"><a href="/sectors">Sectors</a> / {n}</p><h1>{n}</h1><p class="lead">No live case in this sector yet. Be the first: your Snapshot becomes the reference for every business like yours.</p><a class="btn gold" href="/pricing">Be the first · €590</a></div></header>'+portal('Other sectors'))

page('sectors/tourism.html','Tourism & excursions · Advisor Team','Live Business Snapshots of tourism and excursion businesses.',
 '<header class="pagehead" style="background-image:url(/img/ocean.jpg)"><div class="inner"><p class="crumbs"><a href="/sectors">Sectors</a> / Tourism &amp; excursions</p><h1>Tourism &amp; excursions</h1><p class="lead">Booths, tour operators and rentals live on peak hours, commission mix and reviews. Here is what the numbers look like.</p></div></header>'+
 '<section class="block"><div class="wrap"><p class="kicker">Live cases</p><h2 style="margin-bottom:40px">Locations</h2><div class="news">'+
 '<a class="card fade" href="/sectors/tourism/la-siesta-tenerife"><div class="img" style="background-image:url(/img/skyline.jpg)"></div><div class="body"><div class="date"><span class="live"></span>Live · Playa de las Américas, Tenerife</div><h3>La Siesta Excursions</h3><p>652 sales, one summer. Map, competitors, online prices and the plan.</p></div></a>'+
 '<a class="card fade" href="/pricing"><div class="img" style="background-image:url(/img/network.jpg);opacity:.5"></div><div class="body"><div class="date">Open slot · Any location</div><h3>Your business here</h3><p>Excursions, boat trips, rentals or tours anywhere in the world.</p></div></a>'+
 '</div></div></section>'+portal('Other sectors'))

# La Siesta page
wk=[29,63,59,60,60,51,67,64,53,33,22,48,26,17]
labels=['13 Jul','20 Jul','27 Jul','3 Aug','10 Aug','17 Aug','24 Aug','31 Aug','7 Sep','14 Sep','21 Sep','28 Sep','5 Oct','12 Oct']
now=[x*171.5*0.36 for x in wk]; plan=[v*1.059 for v in now]
def linechart():
    W,H,L,B,T,R=900,380,60,40,20,20; mx=4600
    X=lambda i:L+i*(W-L-R)/(len(now)-1); Y=lambda v:H-B-v/mx*(H-B-T)
    grid=''.join(f'<line x1="{L}" x2="{W-R}" y1="{Y(v):.1f}" y2="{Y(v):.1f}" stroke="#262626"/><text x="{L-10}" y="{Y(v)+4:.1f}" text-anchor="end">{"€"+str(v//1000)+"k" if v else "€0"}</text>' for v in range(0,4601,1000))
    xl=''.join(f'<text x="{X(i):.1f}" y="{H-B+22}" text-anchor="middle">{l}</text>' for i,l in enumerate(labels) if i%2==0)
    p1=' '.join(f'{X(i):.1f},{Y(v):.1f}' for i,v in enumerate(now)); p2=' '.join(f'{X(i):.1f},{Y(v):.1f}' for i,v in enumerate(plan))
    band=p2+' '+' '.join(f'{X(i):.1f},{Y(v):.1f}' for i,v in reversed(list(enumerate(now))))
    return f'<svg class="chart" viewBox="0 0 {W} {H}" role="img" aria-label="Estimated weekly commission, actual and with the plan">{grid}{xl}<polygon points="{band}" fill="#fff" opacity=".12"/><polyline points="{p1}" fill="none" stroke="#737373" stroke-width="2"/><polyline points="{p2}" fill="none" stroke="#fff" stroke-width="2.5"/></svg>'
def barchart():
    rows=[('Now (summer 2026)',40254,'#737373'),('With the plan',42624,'#fff')]
    return ''.join(f'<div class="bar" style="grid-template-columns:170px 1fr 90px"><span>{n}</span><i style="width:{v/42624*100:.0f}%;background:{c}"></i><b>€{v:,}</b></div>' for n,v,c in rows)
gyg=[('Whale watching 3 h, adult','€45','≈ €46–65','Same or cheaper'),('Sailing boat 3 h, adult','€65','≈ €58–75','Same'),('Jet ski 1 h, two people','€100–120','≈ €90–120','Same'),('Buggy Teide, two people','€170–180','≈ €160–200','Same'),('Quad Teide sunset, two people','€125–160','≈ €100–130','Slightly higher'),('Parasailing, adult','€60','≈ €53','Slightly higher'),('Siam Park / Loro Parque + bus','€44 / €65','≈ €44 / €65','Same')]
page('sectors/tourism/la-siesta-tenerife.html','La Siesta Excursions, Tenerife · Live Snapshot','Live Business Snapshot of La Siesta Excursions in Playa de las Américas, Tenerife.',
 '<header class="pagehead" style="background-image:url(/img/ocean.jpg)"><div class="inner"><p class="crumbs"><a href="/sectors">Sectors</a> / <a href="/sectors/tourism">Tourism</a> / La Siesta</p><h1>La Siesta Excursions</h1><p class="lead">Excursion booth and rent a car · Avenida Rafael Puig 34, Parque Santiago 1, Playa de las Américas, Tenerife.</p></div></header>'+
 '<section class="block"><div class="wrap"><div class="grid g4">'+''.join(f'<div class="cell fade"><div class="stat"><span class="count" data-to="{v}" data-pre="{pre}" data-suf="{suf}">{pre}{v}{suf}</span></div><p>{d}</p></div>' for v,pre,suf,d in [(652,'','','sales read, Jul to Oct 2026'),(48,'','%','of sales between 11:00 and 15:00'),(40,'€','k','estimated commission in 13 weeks'),(6,'+','%','estimated gain with the plan')])+'</div></div></section>'+
 '<section class="block"><div class="wrap split"><div class="fade"><p class="kicker">Location</p><h2>One street, many booths</h2><p class="lead">La Siesta sits on the main walk above Playa de las Vistas, next to a massage shop, with several excursion booths on either side. They all sell the same trips from the same providers.</p></div><iframe class="map fade" loading="lazy" title="Map of La Siesta Excursions" src="https://maps.google.com/maps?q=Avenida%20Rafael%20Puig%2034%2C%20Parque%20Santiago%201%2C%20Playa%20de%20las%20Am%C3%A9ricas%2C%20Tenerife&z=17&output=embed"></iframe></div></section>'+
 '<section class="block"><div class="wrap"><p class="kicker">Competitors</p><h2 style="margin-bottom:40px">Left, right and online</h2><div class="grid g3">'+
 '<div class="cell fade"><div class="num">Next door</div><h3 style="margin-top:12px">Neighbouring booths</h3><p>Same products, same providers, similar prices. Their sales are not public, so the only way to win is service: who explains best, who answers on WhatsApp, who has reviews.</p></div>'+
 '<div class="cell fade"><div class="num">Online</div><h3 style="margin-top:12px">GetYourGuide &amp; co.</h3><p>Same prices as the booth on 5 of 7 products. Thousands of reviews and free cancellation. The booth answers with advice in person and paying only a deposit.</p></div>'+
 '<div class="cell fade"><div class="num">La Siesta</div><h3 style="margin-top:12px">The edge</h3><p>Real sales data. It knows its peak hours, its best-paying products and the customers it is missing. The neighbours do not.</p></div></div>'+
 '<div class="fade" style="margin-top:50px;overflow-x:auto"><table class="cmp"><tr><th>Product</th><th>La Siesta</th><th>GetYourGuide</th><th>Difference</th></tr>'+''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>' for a,b,c,d in gyg)+'</table><p class="note">GetYourGuide "from" prices for Costa Adeje, shown in USD on 15 Oct 2026 and converted at 0.86 (approximate).</p></div></div></section>'+
 '<section class="block"><div class="wrap"><p class="kicker">Seasons</p><h2 style="margin-bottom:14px">Winter and summer are two different businesses</h2><p class="lead" style="margin-bottom:40px">The tickets cover one summer. Official arrival data shows who comes the rest of the year, and how old they are.</p><div class="grid g3">'+''.join(f'<div class="cell fade"><div class="num">{n}</div><h3 style="margin-top:12px">{t}</h3><p>{d}</p></div>' for n,t,d in [('15×','Nordic visitors in winter','47,700 arrived in January 2025 against 3,200 in August. They come from November to March.'),('31%','Over 60 in winter','From January to March, almost a third of visitors are over 60. From April to June it falls to 26% and under-30s rise to 26%.'),('3×','Young people book more boats','18% of visitors under 25 take a boat trip, against 6% of those over 60. Older visitors prefer guided, organised trips.')])+'</div>'+'<div class="fade" style="margin-top:50px;overflow-x:auto"><table class="cmp"><tr><th>Share of visitors to Tenerife</th><th>Winter</th><th>Summer</th></tr>'+''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>' for a,b,c in [('United Kingdom', '33%', '38%'), ('Germany', '14%', '9%'), ('Nordic countries', '7%', '2%'), ('Spain (mainland)', '9%', '16%'), ('Italy', '7%', '6%'), ('Aged over 60 (Jan–Mar vs Apr–Jun)', '31%', '26%'), ('Aged 16 to 30 (Jan–Mar vs Apr–Jun)', '18%', '26%')])+'</table><p class="note">Countries: Frontur-ISTAC via Promotur, January 2025 (winter) and August to October 2025 (summer), by airport arrivals. Ages: Frontur, Tenerife, first and second quarter 2025. Activities by age: Promotur, Canary Islands 2024.</p></div><div class="grid g3" style="margin-top:50px">'+''.join(f'<div class="cell fade"><h3>{t}</h3><p>{d}</p></div>' for t,d in [('Winter: sell comfort','Guided Teide tours, whale watching on large catamarans, coach trips and Loro Parque. Signs in German and Swedish or Norwegian.'),('Summer: sell adrenaline','Jet skis, parasailing, buggies, Siam Park and swim stops. Signs in Spanish and Italian, booking on WhatsApp.'),('All year: keep the regulars','Winter visitors stay about ten nights and often return each year. Keep their contact and offer the next trip.')])+'</div></div></section>'+'<section class="block"><div class="wrap"><p class="kicker">Sales volume</p><h2 style="margin-bottom:14px">What the plan is worth</h2><p class="lead" style="margin-bottom:34px">Estimated weekly commission, summer 2026, and the same weeks with the five changes applied.</p><div class="fade">'+linechart()+'<div class="legend"><span><i style="background:#737373"></i>Actual (estimated from 652 tickets)</span><span><i style="background:#fff"></i>With the plan (estimate)</span></div></div>'+
 '<div class="fade" style="margin-top:56px;max-width:760px">'+barchart()+'<p class="note">Estimates: weekly sales × average ticket (€171.50) × average commission (36%). The plan adds about €1,400 from recommending water sports and buggies first, plus about €970 commission from more German and Spanish customers. These are estimates, not guarantees.</p></div></div></section>'+
 '<section class="block"><div class="wrap"><p class="kicker">The plan</p><h2 style="margin-bottom:40px">Five changes</h2><div class="grid g3">'+''.join(f'<div class="cell fade"><div class="num">0{i+1}</div><h3 style="margin-top:12px">{t}</h3><p>{d}</p></div>' for i,(t,d) in enumerate([('Recommend first what pays most','Water sports and buggies leave 40–43% against 23% on guided tours.'),('Same price, better service','A sign: same price as online, pay only the deposit, book on WhatsApp.'),('Language by season','Summer: Spanish visitors are 16% of the island but 8% of customers. Winter: German and Nordic.'),('Two people at peak','Full staff from 11:00 to 15:00.'),('Digital tickets','A 30-second form per sale makes next month\'s report automatic.')]))+
 '<div class="cell fade" style="display:flex;flex-direction:column;justify-content:center"><h3>Want this for your business?</h3><a class="btn gold" href="/pricing">Get your Snapshot</a></div></div></div></section>'+portal('Explore other sectors'))

(function(){
  var path=location.pathname.replace(/\/index(\.html)?$/,'/').replace(/\.html$/,'');
  var m=path.match(/^\/(nl|es)(\/|$)/),L=m?m[1]:'en',P=m?'/'+L:'',here=m?(path.slice(3)||'/'):path;
  var T={nl:{sectors:'Sectoren',snap:'De Snapshot',cs:'Case study',price:'Prijzen',news:'Nieuws',login:'Inloggen',join:'Registreren',acct:'Account',get:'Vraag een Snapshot aan',tag:'Datarapporten voor bedrijven zonder datateam.',contact:'Contact'},
    es:{sectors:'Sectores',snap:'El Snapshot',cs:'Caso práctico',price:'Precios',news:'Noticias',login:'Iniciar sesión',join:'Registrarse',acct:'Cuenta',get:'Pide un Snapshot',tag:'Informes de datos para empresas sin equipo de datos.',contact:'Contacto'},
    en:{sectors:'Sectors',snap:'The Snapshot',cs:'Case Study',price:'Pricing',news:'News',login:'Log in',join:'Sign up',acct:'Account',get:'Get a Snapshot',tag:'Data reports for businesses without a data team.',contact:'Contact'}}[L];
  window.LANG=L;
  var links=[['/sectors',T.sectors],['/snapshot',T.snap],['/case-study',T.cs],['/pricing',T.price],['/news',T.news]];
  var hp=here==='/'?'/':here;var sw='<span class="lang">'+[['en','EN',''],['nl','NL','/nl'],['es','ES','/es']].map(function(x){return '<a href="'+x[2]+hp+'"'+(L===x[0]?' class="on"':'')+' hreflang="'+x[0]+'">'+x[1]+'</a>'}).join('')+'</span>';
  var nav=document.createElement('header');nav.className='nav';
  nav.innerHTML='<a class="brand" href="'+P+'/">Advisor <b>Team</b></a><button class="burger" aria-label="Menu">&#9776;</button><nav class="links">'+
    links.map(function(l){return '<a href="'+P+l[0]+'"'+(here.indexOf(l[0])===0?' class="on"':'')+'>'+l[1]+'</a>'}).join('')+
    '<a href="'+P+'/login" id="acct">'+T.login+'</a><a class="cta" href="'+P+'/signup" id="join">'+T.join+'</a>'+sw+'</nav>';
  document.body.prepend(nav);
  nav.querySelector('.burger').onclick=function(){nav.querySelector('.links').classList.toggle('open')};
  var solid=function(){nav.classList.toggle('solid',scrollY>40||document.body.dataset.solid==='1')};addEventListener('scroll',solid);solid();
  var f=document.createElement('footer');
  f.innerHTML='<div class="row"><div><a class="brand" href="'+P+'/" style="font-size:16px;margin:0">Advisor <b>Team</b></a><p style="margin:14px 0 0">'+T.tag+'</p></div><div>'+
    links.map(function(l){return '<a href="'+P+l[0]+'">'+l[1]+'</a>'}).join('')+'<a href="mailto:zangadopodcast@gmail.com">'+T.contact+'</a></div><div>&copy; '+new Date().getFullYear()+' Advisor Team</div></div>';
  document.body.append(f);
  fetch('/api/me').then(function(r){return r.ok?r.json():{}}).then(function(d){
    if(d&&d.user){var a=document.getElementById('acct');a.textContent=T.acct;a.href=P+'/account';var j=document.getElementById('join');j.textContent=T.get;j.href=P+'/pricing'}
  }).catch(function(){});
  var bar=document.createElement('div');bar.className='progress';document.body.append(bar);
  addEventListener('scroll',function(){var h=document.documentElement.scrollHeight-innerHeight;bar.style.width=(h>0?scrollY/h*100:0)+'%'},{passive:true});
  document.querySelectorAll('[data-rail]').forEach(function(w){var r=w.querySelector('.rail');w.querySelectorAll('[data-dir]').forEach(function(b){b.onclick=function(){r.scrollBy({left:+b.dataset.dir*r.clientWidth*.8,behavior:'smooth'})}})});
  var counted=function(el){var end=+el.dataset.to,pre=el.dataset.pre||'',suf=el.dataset.suf||'',t0=null;var step=function(t){t0=t0||t;var k=Math.min(1,(t-t0)/1400);el.textContent=pre+Math.round(end*(1-Math.pow(1-k,3))).toLocaleString(L)+suf;if(k<1)requestAnimationFrame(step)};requestAnimationFrame(step)};
  var co='IntersectionObserver' in window?new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){counted(e.target);co.unobserve(e.target)}})},{threshold:.6}):null;
  document.querySelectorAll('.count[data-to]').forEach(function(el){co?co.observe(el):(el.textContent=(el.dataset.pre||'')+(+el.dataset.to).toLocaleString(L)+(el.dataset.suf||''))});
  var io='IntersectionObserver' in window?new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.12}):null;
  document.querySelectorAll('.fade').forEach(function(el){io?io.observe(el):el.classList.add('in')});
})();
var NLMSG={'Something went wrong. Please try again.':'Er ging iets mis. Probeer het opnieuw.','An account with this email already exists.':'Er bestaat al een account met dit e-mailadres.','Password must be at least 8 characters.':'Het wachtwoord moet minstens 8 tekens hebben.','Please enter your name and a valid email.':'Vul je naam en een geldig e-mailadres in.','Wrong email or password.':'Verkeerd e-mailadres of wachtwoord.','Done. Redirecting…':'Klaar. Even geduld…','Something went wrong.':'Er ging iets mis.','Network error. Please try again.':'Netwerkfout. Probeer het opnieuw.'};
var ESMSG={'Something went wrong. Please try again.':'Algo salió mal. Inténtalo de nuevo.','An account with this email already exists.':'Ya existe una cuenta con este correo.','Password must be at least 8 characters.':'La contraseña debe tener al menos 8 caracteres.','Please enter your name and a valid email.':'Escribe tu nombre y un correo válido.','Wrong email or password.':'Correo o contraseña incorrectos.','Done. Redirecting…':'Hecho. Redirigiendo…','Something went wrong.':'Algo salió mal.','Network error. Please try again.':'Error de red. Inténtalo de nuevo.'};
function tr(m){return (window.LANG==='nl'?NLMSG[m]:window.LANG==='es'?ESMSG[m]:0)||m}
function postForm(form,url,done){
  form.addEventListener('submit',function(e){
    e.preventDefault();var msg=form.querySelector('.msg');msg.className='msg';msg.textContent='…';
    var data={};new FormData(form).forEach(function(v,k){data[k]=v});
    fetch(url,{method:'POST',headers:{'content-type':'application/json'},body:JSON.stringify(data)})
      .then(function(r){return r.json().then(function(d){return{ok:r.ok,d:d}})})
      .then(function(x){if(x.ok){msg.className='msg ok';msg.textContent=tr('Done. Redirecting…');setTimeout(function(){location.href=done},600)}else{msg.textContent=tr(x.d.error||'Something went wrong.')}})
      .catch(function(){msg.textContent=tr('Network error. Please try again.')});
  });
}

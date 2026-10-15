(function(){
  var here=location.pathname.replace(/\/index(\.html)?$/,'/').replace(/\.html$/,'');
  var links=[['/snapshot','The Snapshot'],['/case-study','Case Study'],['/pricing','Pricing'],['/news','News']];
  var nav=document.createElement('header');nav.className='nav';
  nav.innerHTML='<a class="brand" href="/">Advisor <b>Team</b></a><button class="burger" aria-label="Menu">&#9776;</button><nav class="links">'+
    links.map(function(l){return '<a href="'+l[0]+'"'+(here.indexOf(l[0])===0?' class="on"':'')+'>'+l[1]+'</a>'}).join('')+
    '<a href="/login" id="acct">Log in</a><a class="cta" href="/signup" id="join">Sign up</a></nav>';
  document.body.prepend(nav);
  nav.querySelector('.burger').onclick=function(){nav.querySelector('.links').classList.toggle('open')};
  var solid=function(){nav.classList.toggle('solid',scrollY>40||document.body.dataset.solid==='1')};addEventListener('scroll',solid);solid();
  var f=document.createElement('footer');
  f.innerHTML='<div class="row"><div><a class="brand" href="/" style="font-size:16px;margin:0">Advisor <b>Team</b></a><p style="margin:14px 0 0">Data reports for businesses without a data team.</p></div><div>'+
    links.map(function(l){return '<a href="'+l[0]+'">'+l[1]+'</a>'}).join('')+'<a href="mailto:zangadopodcast@gmail.com">Contact</a></div><div>&copy; '+new Date().getFullYear()+' Advisor Team</div></div>';
  document.body.append(f);
  fetch('/api/me').then(function(r){return r.ok?r.json():{}}).then(function(d){
    if(d&&d.user){var a=document.getElementById('acct');a.textContent='Account';a.href='/account';var j=document.getElementById('join');j.textContent='Get a Snapshot';j.href='/pricing'}
  }).catch(function(){});
  var io='IntersectionObserver' in window?new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.12}):null;
  document.querySelectorAll('.fade').forEach(function(el){io?io.observe(el):el.classList.add('in')});
})();
function postForm(form,url,done){
  form.addEventListener('submit',function(e){
    e.preventDefault();var msg=form.querySelector('.msg');msg.className='msg';msg.textContent='…';
    var data={};new FormData(form).forEach(function(v,k){data[k]=v});
    fetch(url,{method:'POST',headers:{'content-type':'application/json'},body:JSON.stringify(data)})
      .then(function(r){return r.json().then(function(d){return{ok:r.ok,d:d}})})
      .then(function(x){if(x.ok){msg.className='msg ok';msg.textContent='Done. Redirecting…';setTimeout(function(){location.href=done},600)}else{msg.textContent=x.d.error||'Something went wrong.'}})
      .catch(function(){msg.textContent='Network error. Please try again.'});
  });
}

#!/usr/bin/env python3
"""PixelCall: запускает сайт локально.
Запуск:  python pixelcall.py   (затем откройте http://localhost:8000)
Другой порт:  python pixelcall.py 9000
Нужен только Python 3, внешние библиотеки не требуются."""
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

PAGE = """<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover"><title>PixelCall</title><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Pixelify+Sans:wght@400;600&family=Press+Start+2P&display=swap">
<style>
:root{--h:270;--b:1;--ac:hsl(var(--h) 90% 65%);--bg:#050505;--tx:#f1eeff;--gl:rgba(255,255,255,.06);--bd:rgba(255,255,255,.18);color-scheme:dark;box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}
*{box-sizing:border-box}html{scroll-padding-top:env(safe-area-inset-top,0px)}
body{margin:0;background:var(--bg);color:var(--tx);font:16px 'Pixelify Sans','Courier New',monospace;min-height:100vh;filter:brightness(var(--b))}
body::after{content:"";position:fixed;inset:0;z-index:-2;background:var(--bgimg,none) center/cover;opacity:.6}
body::before{content:"";position:fixed;inset:0;z-index:-1;pointer-events:none;background:var(--light,none)}
.av svg,.av img{width:100%;height:100%;border-radius:50%;object-fit:cover}.pk{width:44px;height:44px;padding:2px;border-radius:50%}.pk svg{width:100%;height:100%;border-radius:50%}
button,input,select{font:inherit;color:inherit}
button{background:var(--gl);border:1px solid var(--bd);border-radius:12px;padding:8px 14px;cursor:pointer;backdrop-filter:blur(6px);transition:transform .12s,background .12s}
button:hover{background:var(--hv,rgba(255,255,255,.14));transform:scale(.96)}button:active{transform:scale(.91)}button.on{border-color:var(--ac);color:var(--ac)}button:disabled{opacity:.4}
input,select{background:var(--gl);border:1px solid var(--bd);border-radius:10px;padding:8px 10px;max-width:100%}option{background:var(--bg)}
#bar{display:flex;gap:8px;align-items:center;padding:10px 14px;position:sticky;top:env(safe-area-inset-top,0px);z-index:5;flex-wrap:wrap;background:var(--bar,rgba(0,0,0,.6));backdrop-filter:blur(10px)}
#bar button.nv{background:none;border:0;border-bottom:2px solid transparent;border-radius:0;backdrop-filter:none;padding:8px 6px}#bar button.nv:hover{background:none;border-bottom-color:var(--ac);text-shadow:0 0 10px var(--ac)}#bar button.nv.on{color:var(--ac);border-bottom-color:var(--ac)}
h1,h3,#bar .logo{font-family:'Press Start 2P','Courier New',monospace;font-weight:400}h3{font-size:13px;line-height:1.5}h1{font-size:22px}#bar .logo{font-size:14px;color:var(--ac);letter-spacing:1px;margin-right:6px}#bar .sp{flex:1}
#adv{width:38px;height:38px;overflow:hidden;white-space:nowrap;padding:0;display:flex;align-items:center;justify-content:center;transition:width .25s}
#adv:hover{width:150px;transform:none}#adv span{display:none;margin-left:6px}#adv:hover span{display:inline}
main{max-width:980px;margin:auto;padding:16px}
.card{background:var(--gl);border:1px solid var(--bd);border-radius:16px;padding:14px;margin-bottom:14px;backdrop-filter:blur(6px)}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:12px}
.g{text-align:center}.g svg{width:96px;height:96px}.px{color:var(--ac);font-weight:700}
.av{width:64px;height:64px;border-radius:50%;border:4px solid #666;display:grid;place-items:center;font-size:26px;background:var(--gl);position:relative}
.av.on{border-color:#3ddc84}.av i{position:absolute;top:-16px;font-style:normal;font-size:20px}
.row{display:flex;gap:10px;align-items:center;flex-wrap:wrap}.msg{padding:6px 10px;border-radius:10px;margin:4px 0;background:var(--gl);width:fit-content}.msg.me{margin-left:auto;background:hsl(var(--h) 60% 35%)}
.cell{height:70px;display:grid;place-items:center;border-radius:12px;font-weight:700}
.call{position:relative;aspect-ratio:16/9;background:#000;border-radius:16px;overflow:hidden}.call video{width:100%;height:100%;object-fit:cover}
.call .cn{position:absolute;width:20%;max-width:90px}.call .cn svg{width:100%}
.muted{position:absolute;left:50%;bottom:10px;transform:translateX(-50%);background:#e33;padding:4px 10px;border-radius:20px;font-size:13px}
@keyframes bob{50%{transform:translateY(-4px)}}@keyframes tw{50%{opacity:.2}}@keyframes fall{from{transform:translateY(-6px)}to{transform:translateY(14px)}}
.bob{animation:bob 1.6s infinite}.tw{animation:tw 1s infinite}.fl{animation:fall 1.4s linear infinite}
.tabs{display:flex;gap:6px;margin-bottom:10px}small{opacity:.7}
</style></head><body><div id="app"></div>
<script>
const $=s=>document.querySelector(s);let S,U=null,tab='home',authMode='in',pend=null,demo=false,stream=null,mic=true;
const store={get(k,d){try{return JSON.parse(localStorage.getItem(k))??d}catch(e){return d}},set(k,v){try{localStorage.setItem(k,JSON.stringify(v))}catch(e){}}};
const G={santa:{n:'Санта Клаус 2027',p:300},tree:{n:'Ёлка 2027',p:250},ball:{n:'Снежный шар 2027',p:200},window:{n:'Замёрзшее окно 2027',p:350}};
const R=[['px',50,40],['px',100,20],['px',200,15],['px',500,10],['px',700,5],['g','santa',3.3],['g','tree',3.3],['g','ball',3.3],['px',1500,.1]];
const svg=(k,c='')=>{const r=(x,y,w,h,f,a='')=>`<rect x="${x}" y="${y}" width="${w}" height="${h}" fill="${f}" ${a}/>`;let b='';
if(k=='santa')b=r(4,2,8,2,'#e22')+r(3,4,10,2,'#fff')+r(5,6,6,3,'#f6c9a0')+r(5,8,6,5,'#fff')+r(4,9,2,4,'#fff')+r(10,9,2,4,'#fff')+r(6,6,1,1,'#222')+r(9,6,1,1,'#222')+r(4,13,8,2,'#e22')+r(7,0,3,2,'#fff')+r(10,2,2,1,'#fff');
if(k=='tree')b=r(7,1,2,2,'#fd3','class="tw"')+r(6,3,4,2,'#2a8')+r(5,5,6,2,'#2a8')+r(4,7,8,2,'#1d7')+r(3,9,10,2,'#1d7')+r(7,11,2,3,'#852')+r(6,6,1,1,'#f44','class="tw"')+r(9,8,1,1,'#4af','class="tw"')+r(5,10,1,1,'#fd3','class="tw"');
if(k=='ball')b=r(4,3,8,9,'#9de')+r(3,5,10,5,'#9de')+r(5,4,2,1,'#fff')+r(5,9,6,3,'#fff')+r(5,12,6,2,'#a64')+r(4,13,8,2,'#842')+r(7,6,1,1,'#fff','class="fl"')+r(10,5,1,1,'#fff','class="fl"')+r(6,8,1,1,'#fff','class="fl"');
if(k=='window'){const D={'2':['111','001','111','100','111'],'0':['111','101','101','101','111'],'7':['111','001','010','010','010']},dg=(s,y)=>[...s].map((ch,i)=>D[ch].map((row,j)=>[...row].map((v,q)=>v=='1'?r(4+i*4+q,y+j,1,1,'#0a3a6b'):'').join('')).join('')).join('');b=r(0,0,16,16,'#7a4a24')+r(1,1,14,14,'#aee6ff')+r(1,1,3,1,'#fff')+r(1,1,1,3,'#fff')+r(12,14,3,1,'#fff')+r(14,12,1,3,'#fff')+dg('20',2)+dg('27',9)+r(2,8,1,1,'#fff','class="tw"')+r(12,4,1,1,'#fff','class="tw"')+r(13,9,1,1,'#fff','class="tw"')+r(3,12,1,1,'#fff','class="tw"')}
return `<svg viewBox="0 0 16 16" shape-rendering="crispEdges" class="${c}">${b}</svg>`};
const pav=i=>{let r='';for(let y=0;y<5;y++)for(let x=0;x<3;x++){const h=(((i+1)*2654435761)+y*40503+x*9973)>>>0;if((h>>>7)&1){r+=`<rect x="${x}" y="${y}" width="1" height="1"/>`;if(x<2)r+=`<rect x="${4-x}" y="${y}" width="1" height="1"/>`}}return `<svg viewBox="0 0 5 5" shape-rendering="crispEdges"><rect width="5" height="5" fill="hsl(${i*36} 40% 18%)"/><g fill="hsl(${i*36} 85% 62%)">${r}</g></svg>`};
const avh=a=>a=='img'&&S.avimg?`<img src="${S.avimg}" alt="">`:/^p\\d$/.test(a)?pav(+a.slice(1)):a;
function img(inp,k){const f=inp.files[0];if(!f)return;const r=new FileReader();r.onload=()=>{const im=new Image();im.onload=()=>{const m=k=='av'?256:1280,s=Math.min(1,m/Math.max(im.width,im.height)),c=document.createElement('canvas');c.width=im.width*s;c.height=im.height*s;c.getContext('2d').drawImage(im,0,0,c.width,c.height);const u=c.toDataURL('image/jpeg',.8);if(k=='av'){S.avimg=u;S.av='img'}else S.bgimg=u;save();render()};im.src=r.result};r.readAsDataURL(f)}
const sha=async t=>[...new Uint8Array(await crypto.subtle.digest('SHA-256',new TextEncoder().encode(t)))].map(x=>x.toString(16).padStart(2,'0')).join('');
const save=()=>{store.set('pc_u_'+U,S);store.set('pc_taken',TK)};let TK=Object.assign({window:[]},store.get('pc_taken',{santa:[],tree:[],ball:[]}));
function take(g){const f=[];for(let i=1;i<=50;i++)if(!TK[g].includes(i))f.push(i);if(!f.length)return 0;const n=f[Math.random()*f.length|0];TK[g].push(n);return n}
function esc(t){return String(t).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]))}
function applyTheme(){const s=S?.set||{bri:1,hue:270};document.documentElement.style.setProperty('--bgimg',S?.bgimg?`url(${S.bgimg})`:'none');const d=document.documentElement.style,t=s.theme||'black',L=t=='white',has=!!S?.bgimg;d.setProperty('--h',s.hue);d.setProperty('--b',s.bri);
const rb='linear-gradient(180deg,hsl(var(--h) 90% 65%/.6) 0%,hsl(calc(var(--h) + 60) 90% 60%/.4) 25%,hsl(calc(var(--h) + 130) 90% 55%/.22) 50%,hsl(calc(var(--h) + 200) 90% 55%/.1) 70%,transparent 88%)',cl='linear-gradient(180deg,hsl(var(--h) 90% 60%/.5) 0%,transparent 70%)';
d.setProperty('--light',has?'none':t=='rainbow'?rb:t=='color'?cl:'none');
d.setProperty('--bg',L?'#f4f4f8':t=='black'?'#050505':'#0d0b1a');d.setProperty('--tx',L?'#111':'#f1eeff');d.setProperty('--ac',t=='black'?'#fff':L?'#111':'hsl(var(--h) 90% 65%)');
d.setProperty('--gl',L?'rgba(0,0,0,.05)':'rgba(255,255,255,.06)');d.setProperty('--bd',L?'rgba(0,0,0,.25)':'rgba(255,255,255,.18)');d.setProperty('--hv',L?'rgba(0,0,0,.1)':'rgba(255,255,255,.14)');d.setProperty('--bar',L?'rgba(244,244,248,.7)':'rgba(0,0,0,.6)');d.colorScheme=L?'light':'dark'}
function today(){return new Date()}
function render(){applyTheme();if(!U){$('#app').innerHTML=authView();return}const T=[['home','Главная'],['shop','Магазин'],['inv','Инвентарь'],['friends','Друзья'],['chats','Чаты'],['call','Звонок'],['pay','Пиксели'],['set','Настройки']];
$('#app').innerHTML=`<div id="bar"><span class="logo">PixelCall</span>${T.map(t=>`<button class="nv ${tab==t[0]?'on':''}" onclick="go('${t[0]}')">${t[1]}</button>`).join('')}<span class="sp"></span><span class="px">${S.px} px</span><button id="adv" onclick="go('adv')" title="Адвент-календарь">🎁<span>Адвент-календарь</span></button></div><main>${view()}</main>`}
function go(t){tab=t;render()}
function authView(){return `<main style="max-width:420px"><h1 style="color:var(--ac)">PixelCall</h1><div class="card"><div class="tabs"><button class="${authMode=='in'?'on':''}" onclick="authMode='in';render()">Вход</button><button class="${authMode=='up'?'on':''}" onclick="authMode='up';render()">Регистрация</button></div>
<div style="display:grid;gap:8px"><input id="nk" placeholder="Никнейм"><input id="pw" type="password" placeholder="Пароль">
${authMode=='up'?`<select id="sv"><option>Google</option><option>Facebook</option><option>Apple ID</option><option>Email</option><option>Номер телефона</option></select><input id="ct" placeholder="Почта / аккаунт / номер для 2FA"><input id="bd" type="date" title="День рождения">`:''}
<input id="cd" placeholder="Код 2FA (демо: 123456)"><button onclick="auth()">${authMode=='in'?'Войти':'Создать аккаунт'}</button><small id="er"></small></div></div><small>Демо: вход через Google/Facebook/Apple/SMS требует сервера, здесь 2FA имитируется кодом 123456.</small></main>`}
async function auth(){const n=$('#nk').value.trim(),p=$('#pw').value,e=$('#er');if(n.length<3||p.length<6){e.textContent='Ник от 3 символов, пароль от 6';return}if($('#cd').value!='123456'){e.textContent='Неверный код 2FA';return}
const h=await sha(p),a=store.get('pc_acc',{});if(authMode=='up'){if(a[n]){e.textContent='Ник занят';return}if(!$('#ct').value.trim()){e.textContent='Укажите сервис для 2FA';return}a[n]={h,sv:$('#sv').value};store.set('pc_acc',a);U=n;S={px:0,inv:[],adv:{cells:{},last:0},friends:[],chats:{},id:String(Math.random()).slice(2,12).padEnd(10,'0'),bio:'',av:'🙂',bd:$('#bd').value,set:{bri:1,hue:270,theme:'black',bday:true,corners:['santa','tree','ball','snow']}};save()}
else{if(!a[n]||a[n].h!=h){e.textContent='Неверный ник или пароль';return}U=n;S=store.get('pc_u_'+n)}render()}
function view(){return({home,shop,inv,friends,chats,call:callV,pay,set:setV,adv})[tab]()}
function bdToday(){if(!S.bd)return false;const d=new Date(S.bd),t=today();return d.getDate()==t.getDate()&&d.getMonth()==t.getMonth()}
function home(){return `<div class="card row"><div class="av on">${S.set.bday&&bdToday()?'<i>🎂</i>':''}${avh(S.av)}</div><div><b>${esc(U)}</b><br><small>PixelID: ${S.id}</small><br><input value="${esc(S.bio)}" placeholder="Цитата о себе" onchange="S.bio=this.value;save()"></div><div class="row" style="max-width:340px">${[0,1,2,3,4,5,6,7,8,9].map(i=>`<button class="pk ${S.av=='p'+i?'on':''}" onclick="S.av='p${i}';save();render()">${pav(i)}</button>`).join('')}<label>Своя картинка <input type="file" accept="image/*" onchange="img(this,'av')"></label></div></div>
<div class="card"><h3>Встречи</h3><div class="row"><button onclick="go('call')">Создать встречу</button><input id="rm" placeholder="Код встречи"><button onclick="go('call')">Войти</button></div></div>`}
function shop(){return `<div class="grid">${Object.entries(G).map(([k,g])=>`<div class="card g">${svg(k,'bob')}<div>${g.n}</div><div class="px">${g.p} px</div><small>${50-TK[k].length}/50 осталось</small><br><button onclick="buy('${k}')" ${TK[k].length>=50?'disabled':''}>Купить</button></div>`).join('')}</div>`}
function buy(k){const g=G[k];if(S.px<g.p){alert('Недостаточно пикселей');go('pay');return}const n=take(k);if(!n)return;S.px-=g.p;S.inv.push({g:k,n,adv:false});save();render()}
function inv(){return S.inv.length?`<div class="grid">${S.inv.map((it,i)=>`<div class="card g">${svg(it.g,'bob')}<div>${G[it.g].n}</div><b>#${it.n}/50</b>${it.adv?'<br><small>из адвента: только обмен</small>':''}<br><button onclick="trade(${i})">Предложить обмен</button> ${it.adv?'':`<button onclick="sell(${i})">Продать</button>`}</div>`).join('')}</div>`:'<div class="card">Инвентарь пуст</div>'}
function sell(i){const it=S.inv[i];S.px+=Math.floor(G[it.g].p*.7);TK[it.g]=TK[it.g].filter(x=>x!=it.n);S.inv.splice(i,1);save();render()}
function trade(i){if(!S.friends.length){alert('Сначала добавьте друга');return}const n=prompt('Кому? Введите номер:\\n'+S.friends.map((f,j)=>`${j+1}. PixelID ${f.id}`).join('\\n'));const f=S.friends[(+n||0)-1];if(f){alert('Предложение обмена отправлено '+f.id+' (демо)')}}
function friends(){return `<div class="card">Ваш PixelID: <b>${S.id}</b><div class="row" style="margin-top:8px"><input id="fid" placeholder="PixelID друга (10 цифр)" maxlength="10"><button onclick="addF()">Добавить в друзья</button></div></div><div class="card row">${S.friends.map(f=>`<div style="text-align:center"><div class="av ${f.on?'on':''}">${f.ic}</div><small>${f.id}</small></div>`).join('')||'Друзей пока нет'}</div>`}
function addF(){const v=$('#fid').value.trim();if(!/^\\d{10}$/.test(v)||v==S.id||S.friends.some(f=>f.id==v)){alert('Неверный ID');return}S.friends.push({id:v,on:Math.random()>.5,ic:['🦊','🐱','👾','🚀'][Math.random()*4|0]});save();render()}
let cf=null;function chats(){if(!S.friends.length)return '<div class="card">Добавьте друзей, чтобы писать</div>';cf=cf??S.friends[0].id;const m=S.chats[cf]||[];return `<div class="card"><div class="tabs">${S.friends.map(f=>`<button class="${f.id==cf?'on':''}" onclick="cf='${f.id}';render()">${f.id.slice(-4)}</button>`).join('')}</div>${m.map(x=>`<div class="msg ${x.me?'me':''}">${esc(x.t)}</div>`).join('')}<div class="row"><input id="mi" placeholder="Сообщение"><button onclick="send()">Отправить</button></div></div>`}
function send(){const t=$('#mi').value.trim();if(!t)return;(S.chats[cf]=S.chats[cf]||[]).push({me:1,t});save();render()}
const CP=[[500,200],[1000,380],[2000,700]],RT={'$':100,'€':108,'₽':1.1};
function pay(){return `<div class="card"><h3>Донат</h3><div class="grid">${CP.map(([p,u])=>`<div class="card g"><div class="px">${p} px</div><div>${u} ₴</div><button onclick="topup(${p},'PayPal')">PayPal</button><br><br><button onclick="topup(${p},'банковскую карту')">💳 Картой</button></div>`).join('')}</div><small>Демо: настоящая оплата PayPal и картой подключается через платёжный сервис на сервере. Здесь начисление имитируется, а выдать себе пиксели просто так нельзя.</small></div>
<div class="card"><h3>Конвертер</h3><div class="row"><input id="am" type="number" min="0" value="1" oninput="cv()"><select id="cu" onchange="cv()"><option>$</option><option>€</option><option>₽</option></select> → <b id="cr" class="px">100 px</b></div><small>100 px = $1</small></div>`}
function cv(){$('#cr').textContent=Math.floor(($('#am').value||0)*RT[$('#cu').value])+' px'}
function topup(p,m){if(confirm(`Демо-оплата: ${p} px (${m})?`)){S.px+=p;save();render()}}
function rename(){const n=$('#nn').value.trim(),a=store.get('pc_acc',{});if(n.length<3||n.length>20){alert('От 3 до 20 символов');return}if(n==U)return;if(a[n]){alert('Ник занят');return}a[n]=a[U];delete a[U];store.set('pc_acc',a);try{localStorage.removeItem('pc_u_'+U)}catch(e){}U=n;save();render()}
function setV(){const s=S.set,cn=['santa','tree','ball','snow'];return `<div class="card"><h3>Имя</h3><div class="row"><input id="nn" value="${esc(U)}" maxlength="20"><button onclick="rename()">Сохранить имя</button></div><small>Новым ником нужно будет входить в аккаунт</small></div>
<div class="card"><h3>Тема</h3><div class="row">${[['black','Чёрная'],['white','Белая'],['rainbow','Радужная'],['color','Цветная']].map(([k,n])=>`<button class="${(s.theme||'black')==k?'on':''}" onclick="S.set.theme='${k}';save();render()">${n}</button>`).join('')}</div>${S.bgimg?'<small>Со своим фоном подсветка отключена</small>':''}</div>
<div class="card"><h3>Цвет и яркость</h3><label>Цвет <input type="range" min="0" max="360" value="${s.hue}" oninput="S.set.hue=this.value;applyTheme()" onchange="save()"></label> <label>Яркость <input type="range" min=".5" max="1.4" step=".05" value="${s.bri}" oninput="S.set.bri=this.value;applyTheme()" onchange="save()"></label></div>
<div class="card"><h3>Фон</h3><label>Своя картинка <input type="file" accept="image/*" onchange="img(this,'bg')"></label> <button onclick="S.bgimg='';save();render()">Убрать фон</button></div>
<div class="card"><h3>День рождения</h3><input type="date" value="${S.bd||''}" onchange="S.bd=this.value;save()"> <label><input type="checkbox" ${s.bday?'checked':''} onchange="S.set.bday=this.checked;save()"> Показывать тортик</label></div>
<div class="card"><h3>Подарки по углам камеры</h3>${s.corners.map((c,i)=>`<label>Угол ${i+1} <select onchange="S.set.corners[${i}]=this.value;save()">${['none','santa','tree','ball','window'].map(o=>`<option value="${o}" ${(o==c||(c=='snow'&&o=='ball'))?'selected':''}>${o=='none'?'Не ставить':G[o].n}</option>`).join('')}</select></label> `).join('')}<br><small>Ставятся только те подарки, которые у вас есть.</small></div>
<button onclick="U=null;S=null;render()">Выйти</button>`}
function adv(){const t=today(),inEv=t.getMonth()==11&&t.getDate()<=24,done=Object.keys(S.adv.cells).length,can=(demo||inEv)&&done<24&&Date.now()-S.adv.last>=864e5&&(demo||done<t.getDate());
return `<div class="card"><h3>Адвент-календарь (1–24 декабря)</h3><label><input type="checkbox" ${demo?'checked':''} onchange="demo=this.checked;render()"> Пробная версия (без ограничений по датам)</label><br><br><div class="grid" style="grid-template-columns:repeat(auto-fill,minmax(90px,1fr))">${Array.from({length:24},(_,i)=>{const d=i+1,c=S.adv.cells[d];return c?`<div class="cell" style="background:hsl(var(--h) 50% 30%)">${c.t=='px'?c.v+' px':svg(c.v,'')}${c.got?'<small>✔</small>':`<button onclick="claim(${d})">Забрать</button>`}</div>`:`<button class="cell" onclick="openC(${d},${can&&d==done+1})" ${d==done+1&&can?'':'disabled'}>${d}</button>`}).join('')}</div><small>Ячейка раз в 24 часа. Награду можно забрать позже. Подарки из адвента нельзя продать, только обменять.</small></div>`}
function roll(d){let w=R.map(r=>[r,r[0]=='g'||r[1]==1500?r[2]+(d==24?1:0):r[2]]),s=w.reduce((a,x)=>a+x[1],0),x=Math.random()*s;for(const [r,v] of w){x-=v;if(x<=0)return r}return R[0]}
function openC(d,ok){if(!ok)return;const r=roll(d);S.adv.last=Date.now();S.adv.cells[d]=r[0]=='px'?{t:'px',v:r[1]}:{t:'g',v:r[1]};save();render()}
function claim(d){const c=S.adv.cells[d];if(c.t=='px')S.px+=c.v;else{const n=take(c.v);if(n)S.inv.push({g:c.v,n,adv:true});else{S.px+=875;alert('Все 50 экземпляров разобраны: вместо подарка 875 px')}}c.got=1;save();render()}
function callV(){const cs=S.set.corners,pos=['left:6px;top:6px','right:6px;top:6px','left:6px;bottom:6px','right:6px;bottom:6px'];
return `<div class="card"><div class="call"><video id="v" autoplay muted playsinline></video>${cs.map((c,i)=>{const k=c=='snow'?'ball':c;return k!='none'&&S.inv.some(x=>x.g==k)?`<div class="cn" style="${pos[i]}">${svg(k,'bob')}</div>`:''}).join('')}<div id="mt" class="muted" style="display:none">🎤 Микрофон выключен</div></div><div class="row" style="margin-top:10px"><button onclick="cam()">📷 Камера</button><button onclick="mc()">🎤 Микрофон</button><button onclick="scr()">🖥 Демонстрация экрана</button></div><small>Видеосвязь с другими людьми требует сервера (WebRTC); здесь работают камера, микрофон и экран на вашем устройстве.</small></div>`}
async function cam(){try{stream=await navigator.mediaDevices.getUserMedia({video:true,audio:true});$('#v').srcObject=stream;mic=true}catch(e){alert('Нет доступа к камере')}}
function mc(){mic=!mic;stream?.getAudioTracks().forEach(t=>t.enabled=mic);$('#mt').style.display=mic?'none':'block'}
async function scr(){try{$('#v').srcObject=await navigator.mediaDevices.getDisplayMedia({video:true})}catch(e){alert('Демонстрация недоступна')}}
render();
</script></body></html>
"""


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = PAGE.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *a):
        pass


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    print(f"PixelCall: http://localhost:{port}  (Ctrl+C для выхода)")
    try:
        ThreadingHTTPServer(("0.0.0.0", port), Handler).serve_forever()
    except KeyboardInterrupt:
        pass

"""PixelCall для Streamlit (Streamlit Cloud, Hugging Face и т.п.).
Локально:  pip install streamlit  ->  streamlit run pixelcall.py
На Streamlit Cloud: Main file path = pixelcall.py, рядом положите requirements.txt."""
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="PixelCall", page_icon="🎁", layout="wide",
                   initial_sidebar_state="collapsed")

# Убираем отступы и служебные элементы Streamlit, чтобы сайт занял весь экран
st.markdown(
    """<style>
    #MainMenu, header, footer {visibility: hidden; height: 0;}
    .block-container {padding: 0 !important; max-width: 100% !important;}
    iframe {border: 0; width: 100%;}
    </style>""",
    unsafe_allow_html=True,
)

PAGE = r"""<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover"><title>PixelCall</title><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Pixelify+Sans:wght@400;600&family=Press+Start+2P&display=swap">
<script src="https://cdn.jsdelivr.net/npm/peerjs@1.5.4/dist/peerjs.min.js"></script>
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
.call{position:relative;aspect-ratio:16/9;background:#000;border-radius:16px;overflow:hidden;border:3px solid transparent;transition:border-color .2s}.call.mo{border-color:#e33}.call video{width:100%;height:100%;object-fit:cover;display:block}
.call .avc{position:absolute;inset:0;display:grid;place-items:center;background:#111;z-index:1}.call .avc .av{width:30%;max-width:110px;height:auto;aspect-ratio:1;font-size:40px}
.call .cn{position:absolute;width:11%;max-width:46px;z-index:2}.call .cn svg{width:100%}
.call .bad{position:absolute;top:0;left:0;right:0;z-index:4;background:rgba(220,40,40,.92);color:#fff;text-align:center;font-size:13px;padding:4px 8px;display:none}
.call .nm{position:absolute;left:62px;bottom:8px;z-index:3;background:rgba(0,0,0,.55);color:#fff;padding:2px 8px;border-radius:10px;font-size:13px;max-width:45%;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.call .ic{position:absolute;left:50%;bottom:8px;transform:translateX(-50%);z-index:3;display:flex;gap:6px;background:rgba(0,0,0,.55);padding:4px 8px;border-radius:14px}.call .ic:empty{display:none}
.tiles{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,360px),1fr));gap:10px}.wrapc{position:relative}
.cc{position:absolute;top:0;left:50%;transform:translateX(-50%);z-index:8;text-align:center;padding:0 46px 16px;cursor:pointer;user-select:none}
.cc .stick{width:46px;height:5px;border-radius:3px;background:rgba(255,255,255,.8);margin:8px auto 0;transition:width .3s;box-shadow:0 0 6px rgba(0,0,0,.6)}.cc:hover .stick,.cc.open .stick{width:70px}
.cc .code{margin-top:7px;font-family:'Press Start 2P','Courier New',monospace;font-size:12px;color:#fff;background:rgba(0,0,0,.7);padding:9px 14px;border-radius:10px;white-space:nowrap;transform:translateY(-34px);opacity:0;pointer-events:none;transition:transform .8s cubic-bezier(.2,.8,.2,1),opacity .8s}
.cc:hover .code,.cc.open .code{transform:none;opacity:1}
button.off{border-color:#e33;color:#f66}.badge{background:#e33;color:#fff;border-radius:10px;font-size:11px;padding:0 6px;margin-left:4px}
.toast{position:fixed;right:14px;bottom:14px;z-index:50;background:var(--bar,rgba(0,0,0,.8));border:1px solid var(--bd);padding:10px 14px;border-radius:12px;backdrop-filter:blur(8px);animation:tin .3s}@keyframes tin{from{transform:translateY(12px);opacity:0}}
#msgs{max-height:50vh;overflow:auto;margin-bottom:8px}
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
const avh=a=>a=='img'&&S.avimg?`<img src="${S.avimg}" alt="">`:/^p\d$/.test(a)?pav(+a.slice(1)):a;
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
const T=[['home','Главная'],['shop','Магазин'],['inv','Инвентарь'],['friends','Друзья'],['chats','Чаты'],['call','Звонок'],['pay','Пиксели'],['set','Настройки']];
function barHTML(){const bd={friends:S.reqIn.length,chats:Object.values(S.unread).reduce((a,b)=>a+b,0)};return `<span class="logo">PixelCall</span>${T.map(t=>`<button class="nv ${tab==t[0]?'on':''}" onclick="go('${t[0]}')">${t[1]}${bd[t[0]]?`<span class="badge">${bd[t[0]]}</span>`:''}</button>`).join('')}<span class="sp"></span><span title="${netOK?'Сеть подключена':esc(netErr||'Подключение к сети…')}" style="color:${netOK?'#3ddc84':'#e33'}">●</span><span class="px">${S.px} px</span><button id="adv" onclick="go('adv')" title="Адвент-календарь">🎁<span>Адвент-календарь</span></button>`}
function updBar(){const b=$('#bar');if(U&&S&&b)b.innerHTML=barHTML()}
function render(){applyTheme();if(!U){$('#app').innerHTML=authView();return}
$('#app').innerHTML=`<div id="bar">${barHTML()}</div><main>${view()}</main>`;updBar();if(tab=='call'&&room){drawTiles();syncBtns()}if(tab=='chats'){const m=$('#msgs');if(m)m.scrollTop=m.scrollHeight}}
function go(t){tab=t;render()}
function authView(){return `<main style="max-width:420px"><h1 style="color:var(--ac)">PixelCall</h1>${pendingRoom?`<div class="card">🎥 Вас пригласили в конференцию <b>${esc(pendingRoom)}</b>. Войдите или зарегистрируйтесь — и вы сразу попадёте в неё.</div>`:''}<div class="card"><div class="tabs"><button class="${authMode=='in'?'on':''}" onclick="authMode='in';render()">Вход</button><button class="${authMode=='up'?'on':''}" onclick="authMode='up';render()">Регистрация</button></div>
<div style="display:grid;gap:8px"><input id="nk" placeholder="Никнейм"><input id="pw" type="password" placeholder="Пароль">
${authMode=='up'?`<select id="sv"><option>Google</option><option>Facebook</option><option>Apple ID</option><option>Email</option><option>Номер телефона</option></select><input id="ct" placeholder="Почта / аккаунт / номер для 2FA"><input id="bd" type="date" title="День рождения">`:''}
<input id="cd" placeholder="Код 2FA (демо: 123456)"><button onclick="auth()">${authMode=='in'?'Войти':'Создать аккаунт'}</button><small id="er"></small></div></div><small>Демо: вход через Google/Facebook/Apple/SMS требует сервера, здесь 2FA имитируется кодом 123456.</small></main>`}
async function auth(){const n=$('#nk').value.trim(),p=$('#pw').value,e=$('#er');if(n.length<3||p.length<6){e.textContent='Ник от 3 символов, пароль от 6';return}if($('#cd').value!='123456'){e.textContent='Неверный код 2FA';return}
const h=await sha(p),a=store.get('pc_acc',{});if(authMode=='up'){if(a[n]){e.textContent='Ник занят';return}if(!$('#ct').value.trim()){e.textContent='Укажите сервис для 2FA';return}a[n]={h,sv:$('#sv').value};store.set('pc_acc',a);U=n;S={px:0,inv:[],adv:{cells:{},last:0},friends:[],chats:{},id:String(Math.random()).slice(2,12).padEnd(10,'0'),bio:'',av:'🙂',bd:$('#bd').value,set:{bri:1,hue:270,theme:'black',bday:true,corners:['santa','tree','ball','snow']}};save()}
else{if(!a[n]||a[n].h!=h){e.textContent='Неверный ник или пароль';return}U=n;S=store.get('pc_u_'+n)}fix();afterLogin()}
function view(){return({home,shop,inv,friends,chats,call:callV,pay,set:setV,adv})[tab]()}
function bdToday(){if(!S.bd)return false;const d=new Date(S.bd),t=today();return d.getDate()==t.getDate()&&d.getMonth()==t.getMonth()}
function home(){return `<div class="card row"><div class="av on">${S.set.bday&&bdToday()?'<i>🎂</i>':''}${avh(S.av)}</div><div><b>${esc(U)}</b><br><small>PixelID: ${S.id}</small><br><input value="${esc(S.bio)}" placeholder="Цитата о себе" onchange="S.bio=this.value;save()"></div><div class="row" style="max-width:340px">${[0,1,2,3,4,5,6,7,8,9].map(i=>`<button class="pk ${S.av=='p'+i?'on':''}" onclick="S.av='p${i}';save();render()">${pav(i)}</button>`).join('')}<label>Своя картинка <input type="file" accept="image/*" onchange="img(this,'av')"></label></div></div>
<div class="card"><h3>Встречи</h3><div class="row"><button onclick="go('call');mkRoom()">Создать встречу</button><input id="rm" placeholder="Код или ссылка"><button onclick="joinFrom($('#rm').value)">Войти</button></div></div>`}
function shop(){return `<div class="grid">${Object.entries(G).map(([k,g])=>`<div class="card g">${svg(k,'bob')}<div>${g.n}</div><div class="px">${g.p} px</div><small>${50-TK[k].length}/50 осталось</small><br><button onclick="buy('${k}')" ${TK[k].length>=50?'disabled':''}>Купить</button></div>`).join('')}</div>`}
function buy(k){const g=G[k];if(S.px<g.p){alert('Недостаточно пикселей');go('pay');return}const n=take(k);if(!n)return;S.px-=g.p;S.inv.push({g:k,n,adv:false});save();render()}
function inv(){return S.inv.length?`<div class="grid">${S.inv.map((it,i)=>`<div class="card g">${svg(it.g,'bob')}<div>${G[it.g].n}</div><b>#${it.n}/50</b>${it.adv?'<br><small>из адвента: только обмен</small>':''}<br><button onclick="trade(${i})">Предложить обмен</button> ${it.adv?'':`<button onclick="sell(${i})">Продать</button>`}</div>`).join('')}</div>`:'<div class="card">Инвентарь пуст</div>'}
function sell(i){const it=S.inv[i];S.px+=Math.floor(G[it.g].p*.7);TK[it.g]=TK[it.g].filter(x=>x!=it.n);S.inv.splice(i,1);save();render()}
function trade(i){if(!S.friends.length){alert('Сначала добавьте друга');return}const n=prompt('Кому? Введите номер:\n'+S.friends.map((f,j)=>`${j+1}. PixelID ${f.id}`).join('\n'));const f=S.friends[(+n||0)-1];if(f){alert('Предложение обмена отправлено '+f.id+' (демо)')}}
const fname=f=>f.nick||('ID '+f.id),isOn=id=>!!(conns[id]&&conns[id].open);
const rid=()=>Date.now()+'-'+Math.random().toString(36).slice(2,7);
function avh2(a,im){if(a=='img'&&typeof im=='string'&&/^data:image\/(jpeg|png|webp);base64,[A-Za-z0-9+\/=]+$/.test(im))return `<img src="${im}" alt="">`;if(/^p\d$/.test(a||''))return pav(+a.slice(1));return esc(String(a||'🙂').slice(0,8))}
function friendLists(){const card=(o,on,body)=>`<div class="card row"><div class="av ${on?'on':''}">${avh2(o.av,o.im)}</div><div><b>${esc(fname(o))}</b><br><small>${o.id}</small>${body[0]||''}</div><div class="row" style="margin-left:auto">${body[1]||''}</div></div>`;
const inc=S.reqIn.map(r=>card(r,0,['<br><small>хочет добавить вас в друзья</small>',`<button onclick="acceptReq('${r.id}')">✔ Принять</button><button onclick="declineReq('${r.id}')">✖ Отклонить</button>`])).join('');
const out=S.reqOut.map(r=>card(r,0,['<br><small>запрос отправлен, ждём ответа</small>',`<button onclick="cancelReq('${r.id}')">Отменить</button>`])).join('');
const fr=S.friends.map(f=>card(f,isOn(f.id),[`<br><small>${isOn(f.id)?'в сети':'не в сети'}</small>`,`<button onclick="openChat('${f.id}');go('chats')">💬 Написать</button><button onclick="delF('${f.id}')">Удалить</button>`])).join('');
return (inc?'<h3>Входящие запросы</h3>'+inc:'')+(out?'<h3>Исходящие запросы</h3>'+out:'')+'<h3>Друзья</h3>'+(fr||'<div class="card">Друзей пока нет</div>')}
function friends(){return `<div class="card">Ваш PixelID: <b>${S.id}</b> <small>— отправьте его другу, чтобы он мог добавить вас</small><div class="row" style="margin-top:8px"><input id="fid" placeholder="PixelID друга (10 цифр)" maxlength="10"><button onclick="addF()">Добавить в друзья</button></div><small>Запросы и сообщения доходят, когда оба открыли PixelCall (иначе ждут, пока друг зайдёт).</small></div><div id="fl">${friendLists()}</div>`}
function updF(){if(tab=='friends'){const e=$('#fl');if(e)e.innerHTML=friendLists()}}
const prof=()=>({nick:U,av:S.av,im:S.av=='img'?S.avimg:null});
function addF(){const v=$('#fid').value.trim();if(!/^\d{10}$/.test(v)||v==S.id||S.friends.some(f=>f.id==v)||S.reqOut.some(r=>r.id==v)){alert('Неверный ID или запрос уже отправлен');return}
if(S.reqIn.some(r=>r.id==v)){acceptReq(v);return}
S.reqOut.push({id:v,nick:'',av:'🙂'});save();tx(v,Object.assign({t:'freq'},prof()));render()}
function makeFriend(id,p){S.reqIn=S.reqIn.filter(r=>r.id!=id);S.reqOut=S.reqOut.filter(r=>r.id!=id);if(!S.friends.some(f=>f.id==id))S.friends.push({id,nick:String(p.nick||'').slice(0,20),av:p.av||'🙂',im:p.im||null});save();updBar();updF();updChat()}
function acceptReq(id){const r=S.reqIn.find(x=>x.id==id);if(!r)return;makeFriend(id,r);tx(id,Object.assign({t:'facc'},prof()));toast('Теперь вы друзья с '+fname(r))}
function declineReq(id){S.reqIn=S.reqIn.filter(r=>r.id!=id);save();tx(id,{t:'frej'});updBar();updF()}
function cancelReq(id){S.reqOut=S.reqOut.filter(r=>r.id!=id);save();updF()}
function delF(id){if(!confirm('Удалить из друзей?'))return;S.friends=S.friends.filter(f=>f.id!=id);save();tx(id,{t:'unf'});updF();updChat()}
function ftabs(){return S.friends.map(f=>`<button class="${f.id==cf?'on':''}" onclick="openChat('${f.id}')"><span style="color:${isOn(f.id)?'#3ddc84':'#777'}">●</span> ${esc(fname(f))}${S.unread[f.id]?`<span class="badge">${S.unread[f.id]}</span>`:''}</button>`).join('')}
function msgsHTML(){const m=S.chats[cf]||[];return m.length?m.map(x=>`<div class="msg ${x.me?'me':''}">${x.inv?`🎥 Приглашение в конференцию <b>${x.inv}</b> <button onclick="joinFrom('${x.inv}')">Войти</button>`:esc(x.t)}${x.me?` <small>${x.ok?'✓':'⏳'}</small>`:''}</div>`).join(''):'<small>Сообщений пока нет</small>'}
function openChat(id){cf=id;S.unread[id]=0;save();if(tab=='chats')render()}
function chats(){if(!S.friends.length)return '<div class="card">Добавьте друзей, чтобы писать</div>';if(!S.friends.some(f=>f.id==cf))cf=S.friends[0].id;S.unread[cf]=0;
return `<div class="card"><div class="tabs" id="ftabs" style="flex-wrap:wrap">${ftabs()}</div><div id="msgs">${msgsHTML()}</div><div class="row"><input id="mi" placeholder="Сообщение" style="flex:1" onkeydown="if(event.key=='Enter')send()"><button onclick="send()">Отправить</button></div></div>`}
function updChat(){if(tab!='chats')return;const m=$('#msgs'),t=$('#ftabs');if(t)t.innerHTML=ftabs();if(m){m.innerHTML=msgsHTML();m.scrollTop=m.scrollHeight}}
function send(){const i=$('#mi'),t=i.value.trim().slice(0,2000);if(!t)return;const m={me:1,t,ts:rid(),ok:0};(S.chats[cf]=S.chats[cf]||[]).push(m);save();i.value='';updChat();tx(cf,{t:'msg',text:t,ts:m.ts})}
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
<button onclick="logout()">Выйти</button>`}
function adv(){const t=today(),inEv=t.getMonth()==11&&t.getDate()<=24,done=Object.keys(S.adv.cells).length,can=(demo||inEv)&&done<24&&Date.now()-S.adv.last>=864e5&&(demo||done<t.getDate());
return `<div class="card"><h3>Адвент-календарь (1–24 декабря)</h3><label><input type="checkbox" ${demo?'checked':''} onchange="demo=this.checked;render()"> Пробная версия (без ограничений по датам)</label><br><br><div class="grid" style="grid-template-columns:repeat(auto-fill,minmax(90px,1fr))">${Array.from({length:24},(_,i)=>{const d=i+1,c=S.adv.cells[d];return c?`<div class="cell" style="background:hsl(var(--h) 50% 30%)">${c.t=='px'?c.v+' px':svg(c.v,'')}${c.got?'<small>✔</small>':`<button onclick="claim(${d})">Забрать</button>`}</div>`:`<button class="cell" onclick="openC(${d},${can&&d==done+1})" ${d==done+1&&can?'':'disabled'}>${d}</button>`}).join('')}</div><small>Ячейка раз в 24 часа. Награду можно забрать позже. Подарки из адвента нельзя продать, только обменять.</small></div>`}
function roll(d){let w=R.map(r=>[r,r[0]=='g'||r[1]==1500?r[2]+(d==24?1:0):r[2]]),s=w.reduce((a,x)=>a+x[1],0),x=Math.random()*s;for(const [r,v] of w){x-=v;if(x<=0)return r}return R[0]}
function openC(d,ok){if(!ok)return;const r=roll(d);S.adv.last=Date.now();S.adv.cells[d]=r[0]=='px'?{t:'px',v:r[1]}:{t:'g',v:r[1]};save();render()}
function claim(d){const c=S.adv.cells[d];if(c.t=='px')S.px+=c.v;else{const n=take(c.v);if(n)S.inv.push({g:c.v,n,adv:true});else{S.px+=875;alert('Все 50 экземпляров разобраны: вместо подарка 875 px')}}c.got=1;save();render()}
/* ===== СЕТЬ (WebRTC через PeerJS, без своего сервера) ===== */
const NP='pixelcall27-',RP='pcr27-';
let peer=null,conns={},connecting={},netOK=false,netErr='',cf=null,room=null,camOn=true,pendingRoom='__ROOM__';
function toast(t){const d=document.createElement('div');d.className='toast';d.textContent=t;document.body.appendChild(d);setTimeout(()=>d.remove(),4000)}
function fix(){S.friends=(S.friends||[]).map(f=>({id:f.id,nick:f.nick||'',av:f.av||f.ic||'🙂',im:f.im||null}));S.reqIn=S.reqIn||[];S.reqOut=S.reqOut||[];S.chats=S.chats||{};S.unread=S.unread||{}}
function afterLogin(){netStart();if(pendingRoom){const c=pendingRoom;pendingRoom='';tab='call';render();joinRoom(c,false)}else render()}
function logout(){leave(true);try{peer&&peer.destroy()}catch(e){}peer=null;conns={};netOK=false;U=null;S=null;render()}
function netStart(){if(peer||!U||!window.Peer)return;try{peer=new Peer(NP+S.id)}catch(e){return}
peer.on('open',()=>{netOK=true;netErr='';updBar();netTick()});
peer.on('connection',setupConn);
peer.on('disconnected',()=>{netOK=false;updBar();try{peer&&peer.reconnect()}catch(e){}});
peer.on('error',e=>{if(e.type=='unavailable-id')netErr='Этот аккаунт уже открыт в другой вкладке';else if(e.type!='peer-unavailable')netErr='Сеть: '+e.type;updBar()})}
function link(id){const c=conns[id];if(c&&c.open)return c;if(!peer||!netOK||connecting[id])return null;connecting[id]=1;setTimeout(()=>delete connecting[id],8000);try{setupConn(peer.connect(NP+id,{reliable:true}))}catch(e){delete connecting[id]}return null}
function tx(id,o){const c=conns[id];if(c&&c.open){try{c.send(o);return true}catch(e){}}link(id);return false}
function setupConn(c){const id=String(c.peer||'').slice(NP.length);if(!/^\d{10}$/.test(id)){try{c.close()}catch(e){}return}
c.on('open',()=>{delete connecting[id];conns[id]=c;c.send(Object.assign({t:'hi'},prof()));flush(id);updBar();updF();updChat()});
c.on('data',d=>onData(id,d));c.on('close',()=>{if(conns[id]===c)delete conns[id];updF();updChat()});c.on('error',()=>{})}
function flush(id){if(S.reqOut.some(r=>r.id==id))tx(id,Object.assign({t:'freq'},prof()));(S.chats[id]||[]).filter(m=>m.me&&!m.ok).forEach(m=>tx(id,m.inv?{t:'inv',code:m.inv,ts:m.ts}:{t:'msg',text:m.t,ts:m.ts}))}
function netTick(){if(!U||!S)return;if(peer&&peer.destroyed){peer=null;netOK=false}if(!peer)netStart();else if(peer.disconnected){try{peer.reconnect()}catch(e){}}
if(netOK)[...S.friends,...S.reqOut].forEach(f=>link(f.id))}
setInterval(netTick,12000);
function onData(id,d){if(!d||typeof d!='object')return;const fr=S.friends.find(f=>f.id==id),pf=()=>({nick:String(d.nick||'').slice(0,20),av:typeof d.av=='string'?d.av.slice(0,8):'🙂',im:typeof d.im=='string'&&d.im.length<400000?d.im:null});
switch(d.t){
case'hi':if(fr){Object.assign(fr,pf());save();updF();updChat()}break;
case'freq':if(fr){tx(id,Object.assign({t:'facc'},prof()));break}if(S.reqOut.some(r=>r.id==id)){makeFriend(id,pf());tx(id,Object.assign({t:'facc'},prof()));toast('Теперь вы друзья!');break}
if(!S.reqIn.some(r=>r.id==id)&&S.reqIn.length<50){S.reqIn.push(Object.assign({id},pf()));save();toast('📨 '+(d.nick||id)+' хочет добавить вас в друзья')}updBar();updF();break;
case'facc':if(S.reqOut.some(r=>r.id==id)){makeFriend(id,pf());toast('✅ '+(d.nick||id)+' принял(а) ваш запрос')}break;
case'frej':if(S.reqOut.some(r=>r.id==id)){S.reqOut=S.reqOut.filter(r=>r.id!=id);save();updF();toast('Запрос в друзья отклонён')}break;
case'unf':if(fr){S.friends=S.friends.filter(f=>f.id!=id);save();updF();updChat()}break;
case'ack':{const m=(S.chats[id]||[]).find(x=>x.me&&x.ts==d.ts);if(m){m.ok=1;save();updChat()}break}
case'msg':case'inv':{if(!fr)break;const a=S.chats[id]=S.chats[id]||[],ts=String(d.ts||'').slice(0,40);let m;
if(d.t=='inv'){const c=parseCode(d.code);if(!c)break;m={inv:c,ts}}else{if(typeof d.text!='string')break;m={t:d.text.slice(0,2000),ts}}
tx(id,{t:'ack',ts});if(a.some(x=>!x.me&&x.ts==ts))break;a.push(m);if(tab=='chats'&&cf==id){updChat()}else{S.unread[id]=(S.unread[id]||0)+1;updBar();toast('💬 '+fname(fr)+': '+(m.inv?'приглашение в конференцию':m.t.slice(0,60)))}save();break}}}

/* ===== КОНФЕРЕНЦИИ ===== */
const GK=['santa','tree','ball','window'];
const myGifts=()=>S.set.corners.map(c=>{const k=c=='snow'?'ball':c;return k!='none'&&S.inv.some(x=>x.g==k)?k:null});
const ICM='<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round"><rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0 0 12 5M19 11a7 7 0 0 1-.5 2.5M12 18v3"/><path d="M3 3l18 18" stroke="#f55"/></svg>';
const ICC='<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="7" width="12" height="10" rx="2"/><path d="M15 11l6-3v8l-6-3"/><path d="M3 3l18 18" stroke="#f55"/></svg>';
function rc(){const a='ABCDEFGHJKMNPQRSTUVWXYZ23456789';let s='';for(let i=0;i<8;i++)s+=a[Math.random()*a.length|0];return s.slice(0,4)+'-'+s.slice(4)}
function parseCode(v){v=String(v||'').trim();const m=v.match(/room=([A-Za-z0-9-]+)/);if(m)v=m[1];v=v.toUpperCase().replace(/[^A-Z0-9]/g,'');return v.length==8?v.slice(0,4)+'-'+v.slice(4):''}
function roomLink(){let b='';for(const w of [()=>window.top,()=>parent]){try{const l=w().location;if(/^https?:/.test(l.origin)){b=l.origin+l.pathname;break}}catch(e){}}return b?b+'?room='+room.code:room.code}
function copyTxt(t){return (navigator.clipboard?navigator.clipboard.writeText(t):Promise.reject()).catch(()=>{const a=document.createElement('textarea');a.value=t;document.body.appendChild(a);a.select();try{document.execCommand('copy')}catch(e){}a.remove()})}
function copyRoom(el){el.classList.toggle('open');copyTxt(roomLink()).then(()=>toast('Ссылка на конференцию скопирована'))}
function mkRoom(){if(room)return;joinRoom(rc(),true)}
function joinFrom(v){const c=parseCode(v);if(!c){alert('Неверный код конференции');return}if(room){alert('Вы уже в конференции');go('call');return}tab='call';render();joinRoom(c,false)}
async function media(){let s=null;
try{s=await navigator.mediaDevices.getUserMedia({video:{width:{ideal:640},height:{ideal:360}},audio:{echoCancellation:true,noiseSuppression:true}})}catch(e){try{s=await navigator.mediaDevices.getUserMedia({audio:true})}catch(e2){}}
if(!s)s=new MediaStream();
if(!s.getVideoTracks().length){const c=document.createElement('canvas');c.width=320;c.height=180;c.getContext('2d').fillRect(0,0,320,180);s.addTrack(c.captureStream(1).getVideoTracks()[0]);s.noCam=true}
return s}
async function joinRoom(code,host){if(room)return;room={code,host,parts:{},stream:null,sharing:null,raw:code.replace('-','')};const R=room;render();
const s=await media();if(room!==R){s.getTracks().forEach(t=>t.stop());return}R.stream=s;mic=s.getAudioTracks().length>0;camOn=!s.noCam;
const pid=RP+R.raw+'-'+(host?'h':Math.random().toString(36).slice(2,8));R.pid=pid;let rp;try{rp=new Peer(pid)}catch(e){alert('Не удалось подключиться к сети');leave();return}R.rp=rp;
rp.on('open',()=>{if(room!==R)return;if(!host){rdata(RP+R.raw+'-h');callTo(RP+R.raw+'-h')}drawTiles();syncBtns()});
rp.on('connection',c=>rwire(c));
rp.on('call',call=>{if(room!==R)return;call.answer(R.stream);callWire(call)});
rp.on('error',e=>{if(room!==R)return;if(e.type=='unavailable-id'&&host){leave(true);mkRoom()}else if(e.type=='peer-unavailable'&&/-h\b/.test(e.message||'')&&!host){alert('Конференция не найдена: проверьте код или хост ещё не вошёл');leave()}})}
function rdata(id){const c=room.rp.connect(id,{reliable:true});rwire(c)}
function callTo(id){const R=room;if(!R||R.parts[id]&&R.parts[id].call)return;const c=R.rp.call(id,R.stream);if(c)callWire(c)}
function rwire(c){const R=room;c.on('open',()=>{if(room!==R)return;const p=R.parts[c.peer]=R.parts[c.peer]||{};p.conn=c;c.send(Object.assign({t:'hi',mic,cam:camOn||!!R.sharing,gifts:myGifts()},prof()))});
c.on('data',d=>rdat(c,d));c.on('close',()=>dropPart(c.peer));c.on('error',()=>{})}
function rdat(c,d){if(!room||!d||typeof d!='object')return;const id=c.peer,p=room.parts[id]=room.parts[id]||{};
if(d.t=='hi'||d.t=='st'){if(d.t=='hi'){p.nick=String(d.nick||'Гость').slice(0,20);p.av=typeof d.av=='string'?d.av.slice(0,8):'🙂';p.im=typeof d.im=='string'&&d.im.length<400000?d.im:null}
p.mic=d.mic!==false;p.cam=d.cam!==false;p.gifts=Array.isArray(d.gifts)?d.gifts.slice(0,4).map(k=>GK.includes(k)?k:null):[];
if(d.t=='hi'&&room.host)c.send({t:'list',ids:Object.keys(room.parts).filter(k=>k!=id&&room.parts[k].conn&&room.parts[k].conn.open)});drawTiles()}
else if(d.t=='list'&&!room.listed){room.listed=1;(Array.isArray(d.ids)?d.ids:[]).slice(0,12).forEach(i=>{if(typeof i=='string'&&i.startsWith(RP+room.raw+'-')&&i!=room.pid){if(!(room.parts[i]&&room.parts[i].conn))rdata(i);callTo(i)}})}}
function callWire(call){const R=room,id=call.peer,p=R.parts[id]=R.parts[id]||{};p.call=call;
call.on('stream',st=>{if(room!==R)return;p.stream=st;let a=document.getElementById('a-'+id);if(!a){a=document.createElement('audio');a.id='a-'+id;a.className='ra';a.autoplay=true;document.body.appendChild(a)}a.srcObject=st;a.play().catch(()=>{});if(R.sharing)setSend(R.sharing.getVideoTracks()[0]);drawTiles()});
call.on('close',()=>{if(room===R&&p.call===call&&!(p.conn&&p.conn.open))dropPart(id)});call.on('error',()=>{})}
function dropPart(id){if(!room)return;const p=room.parts[id];if(!p)return;delete room.parts[id];try{p.conn&&p.conn.close()}catch(e){}try{p.call&&p.call.close()}catch(e){}const a=document.getElementById('a-'+id);a&&a.remove();if(p.nick)toast(p.nick+' вышел(а)');drawTiles()}
function bc(){if(!room)return;const m={t:'st',mic,cam:camOn||!!room.sharing,gifts:myGifts()};Object.values(room.parts).forEach(p=>{try{p.conn&&p.conn.open&&p.conn.send(m)}catch(e){}})}
function togMic(){if(!room)return;mic=!mic;room.stream.getAudioTracks().forEach(t=>t.enabled=mic);bc();drawTiles();syncBtns()}
function togCam(){if(!room)return;if(room.stream.noCam){alert('Камера не найдена или нет доступа');return}camOn=!camOn;room.stream.getVideoTracks().forEach(t=>t.enabled=camOn);bc();drawTiles();syncBtns()}
function setSend(tr){if(!tr||!room)return;Object.values(room.parts).forEach(p=>{const pc=p.call&&p.call.peerConnection;if(!pc)return;const s=pc.getSenders().find(x=>x.track&&x.track.kind=='video');if(s)s.replaceTrack(tr).catch(()=>{})})}
async function scr(){if(!room)return;if(room.sharing){stopScr();return}try{const d=await navigator.mediaDevices.getDisplayMedia({video:true});room.sharing=d;const tr=d.getVideoTracks()[0];setSend(tr);tr.onended=stopScr;bc();drawTiles();syncBtns()}catch(e){alert('Демонстрация экрана недоступна')}}
function stopScr(){if(!room||!room.sharing)return;room.sharing.getTracks().forEach(t=>t.stop());room.sharing=null;setSend(room.stream.getVideoTracks()[0]);bc();drawTiles();syncBtns()}
function leave(silent){if(!room)return;const R=room;try{stopScr()}catch(e){}Object.values(R.parts).forEach(p=>{try{p.conn&&p.conn.close()}catch(e){}try{p.call&&p.call.close()}catch(e){}});try{R.rp&&R.rp.destroy()}catch(e){}R.stream&&R.stream.getTracks().forEach(t=>t.stop());document.querySelectorAll('audio.ra').forEach(a=>a.remove());room=null;if(!silent)render()}
function invite(){const s=$('#invf');if(!s||!s.value)return;const id=s.value,m={me:1,inv:room.code,ts:rid(),ok:0};(S.chats[id]=S.chats[id]||[]).push(m);save();tx(id,{t:'inv',code:m.inv,ts:m.ts});toast('Приглашение отправлено')}
function syncBtns(){const f=(id,off)=>{const e=document.getElementById(id);if(e)e.classList.toggle('off',off)};f('bcam',!camOn);f('bmic',!mic);const s=document.getElementById('bscr');if(s)s.classList.toggle('on',!!(room&&room.sharing))}
function tileHTML(id,o,local){const camv=local?(camOn||!!room.sharing):o.cam!==false,micv=local?mic:o.mic!==false,gl=local?myGifts():(o.gifts||[]),pos=['left:6px;top:6px','right:6px;top:6px','left:6px;bottom:6px','right:6px;bottom:6px'];
return `<div class="call ${micv?'':'mo'}" id="t-${id}"><video autoplay playsinline muted></video><div class="avc" style="display:${camv?'none':'grid'}"><div class="av">${local?avh(S.av):avh2(o.av,o.im)}</div></div>${gl.map((k,i)=>k?`<div class="cn" style="${pos[i]}">${svg(k,'bob')}</div>`:'').join('')}<div class="bad" style="display:${(local?room.lbad:o.bad)?'block':'none'}">Плохое подключение к интернету</div><div class="nm">${esc(local?U+' (вы)':(o.nick||'Гость'))}</div><div class="ic">${micv?'':ICM}${camv?'':ICC}</div></div>`}
function drawTiles(){const t=$('#tiles');if(!t||!room||!room.stream)return;const ps=Object.entries(room.parts).filter(([k,p])=>p.nick||p.stream);
t.innerHTML=tileHTML('me',{},true)+ps.map(([k,p])=>tileHTML(k,p,false)).join('');
const att=(id,st)=>{const v=document.querySelector('#t-'+id+' video');if(v&&st){v.srcObject=st;v.play().catch(()=>{})}};att('me',room.sharing||room.stream);ps.forEach(([k,p])=>att(k,p.stream))}
function setBad(id,b){const e=document.querySelector('#t-'+id+' .bad');if(e)e.style.display=b?'block':'none'}
async function netStats(){if(!room)return;let lbad=!navigator.onLine;
for(const [id,p] of Object.entries(room.parts)){let bad=false;const pc=p.call&&p.call.peerConnection;
if(pc){if(['disconnected','failed'].includes(pc.iceConnectionState))bad=true;else try{const r=await pc.getStats();let lost=0,rec=0,rtt=0,fl=0;
r.forEach(x=>{if(x.type=='inbound-rtp'){lost+=x.packetsLost||0;rec+=x.packetsReceived||0}if(x.type=='candidate-pair'&&x.nominated&&x.currentRoundTripTime)rtt=Math.max(rtt,x.currentRoundTripTime);if(x.type=='remote-inbound-rtp')fl=Math.max(fl,x.fractionLost||0)});
const dl=Math.max(0,lost-(p.pl||0)),dr=rec-(p.pr||0);p.pl=lost;p.pr=rec;const stall=p.seen&&dr<=0;if(dr>0)p.seen=1;
bad=(dl+dr>0&&dl/(dl+dr)>.1)||rtt>.8||!!stall;if(fl>.1||rtt>.8)lbad=true}catch(e){}}
if(!!p.bad!==bad){p.bad=bad;setBad(id,bad)}}
if(!!room.lbad!==lbad){room.lbad=lbad;setBad('me',lbad)}}
setInterval(netStats,2500);addEventListener('offline',netStats);addEventListener('online',netStats);
function callV(){if(!room)return `<div class="card"><h3>Конференция</h3><div class="row"><button onclick="mkRoom()">➕ Создать конференцию</button><input id="rm" placeholder="Код или ссылка"><button onclick="joinFrom($('#rm').value)">Войти</button></div><small>Создайте конференцию и отправьте другу код (или ссылку). Нужен доступ к камере и микрофону — если их нет, можно зайти и без них.</small></div>`;
const on=S.friends.filter(f=>isOn(f.id));
return `<div class="card"><div class="wrapc"><div class="cc" onclick="copyRoom(this)" title="Нажмите, чтобы скопировать ссылку"><div class="stick"></div><div class="code">${room.code}</div></div><div id="tiles" class="tiles"></div></div>
<div class="row" style="margin-top:10px"><button id="bcam" onclick="togCam()">📷 Камера</button><button id="bmic" onclick="togMic()">🎤 Микрофон</button><button id="bscr" onclick="scr()">🖥 Демонстрация экрана</button><button onclick="leave()" style="border-color:#e33;color:#f66">Выйти</button></div>
<div class="row" style="margin-top:10px">${on.length?`<select id="invf">${on.map(f=>`<option value="${f.id}">${esc(fname(f))}</option>`).join('')}</select><button onclick="invite()">📨 Позвать друга</button>`:'<small>Друзья в сети появятся здесь — их можно позвать в один клик.</small>'}</div>
<small>Наведите на палочку сверху — появится код конференции, клик копирует ссылку.</small></div>`}
render();
</script></body></html>
"""

import re as _re
try:
    _room = str(st.query_params.get("room", ""))
except Exception:
    _room = ""
_room = _re.sub(r"[^A-Za-z0-9-]", "", _room)[:12]

components.html(PAGE.replace("__ROOM__", _room), height=1100, scrolling=True)


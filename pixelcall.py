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
    iframe {border: 0; width: 100%; height: 100vh !important; height: 100dvh !important;}
    </style>""",
    unsafe_allow_html=True,
)

PAGE = r"""<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover"><title>PixelCall</title><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Pixelify+Sans:wght@400;600&family=Press+Start+2P&display=swap">
<script src="https://cdn.jsdelivr.net/npm/peerjs@1.5.4/dist/peerjs.min.js"></script>
<style>
:root{--f1:'Pixelify Sans','Courier New',monospace;--f2:'Press Start 2P','Courier New',monospace;--fw:400;--gs:2.4s;--h:270;--b:1;--ac:hsl(var(--h) 90% 65%);--bg:#050505;--tx:#f1eeff;--gl:rgba(255,255,255,.06);--bd:rgba(255,255,255,.18);color-scheme:dark;box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}
*{box-sizing:border-box}html{scroll-padding-top:env(safe-area-inset-top,0px)}
body{margin:0;background:var(--bg);color:var(--tx);font:16px var(--f1);min-height:100vh;filter:brightness(var(--b))}
body::after{content:"";position:fixed;inset:0;z-index:-2;background:var(--bgimg,none) center/cover;opacity:.6}
body::before{content:"";position:fixed;inset:0;z-index:-1;pointer-events:none;background:var(--light,none)}
.av svg,.av img{width:100%;height:100%;border-radius:50%;object-fit:cover}.pk{width:44px;height:44px;padding:2px;border-radius:50%}.pk svg{width:100%;height:100%;border-radius:50%}
button,input,select{font:inherit;color:inherit}
button{background:var(--gl);border:1px solid var(--bd);border-radius:12px;padding:8px 14px;cursor:pointer;backdrop-filter:blur(6px);transition:transform .12s,background .12s}
button:hover{background:var(--hv,rgba(255,255,255,.14));transform:scale(.96)}button:active{transform:scale(.91)}button.on{border-color:var(--ac);color:var(--ac)}button:disabled{opacity:.4}
input,select{background:var(--gl);border:1px solid var(--bd);border-radius:10px;padding:8px 10px;max-width:100%}option{background:var(--bg)}
#bar{display:flex;gap:8px;align-items:center;padding:10px 14px;position:sticky;top:env(safe-area-inset-top,0px);z-index:5;flex-wrap:wrap;background:var(--bar,rgba(0,0,0,.6));backdrop-filter:blur(10px)}
#bar button.nv{background:none;border:0;border-bottom:2px solid transparent;border-radius:0;backdrop-filter:none;padding:8px 6px}#bar button.nv:hover{background:none;border-bottom-color:var(--ac);text-shadow:0 0 10px var(--ac)}#bar button.nv.on{color:var(--ac);border-bottom-color:var(--ac)}
h1,h3,#bar .logo{font-family:var(--f2);font-weight:var(--fw)}h3{font-size:13px;line-height:1.5}h1{font-size:22px}#bar .logo{font-size:14px;color:var(--ac);letter-spacing:1px;margin-right:6px}#bar .sp{flex:1}
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
.cc .code{margin-top:7px;font-family:var(--f2);font-size:12px;color:#fff;background:rgba(0,0,0,.7);padding:9px 14px;border-radius:10px;white-space:nowrap;transform:translateY(-34px);opacity:0;pointer-events:none;transition:transform .8s cubic-bezier(.2,.8,.2,1),opacity .8s}
.cc:hover .code,.cc.open .code{transform:none;opacity:1}
button.off{border-color:#e33;color:#f66}.badge{background:#e33;color:#fff;border-radius:10px;font-size:11px;padding:0 6px;margin-left:4px}
.toast{position:fixed;right:14px;bottom:14px;z-index:50;background:var(--bar,rgba(0,0,0,.8));border:1px solid var(--bd);padding:10px 14px;border-radius:12px;backdrop-filter:blur(8px);animation:tin .3s}@keyframes tin{from{transform:translateY(12px);opacity:0}}
#msgs{max-height:50vh;overflow:auto;margin-bottom:8px}
@keyframes bob{50%{transform:translateY(-4px)}}@keyframes tw{50%{opacity:.2}}@keyframes fall{from{transform:translateY(-6px)}to{transform:translateY(14px)}}
.bob{animation:bob 1.6s infinite}.tw{animation:tw 1s infinite}.fl{animation:fall 1.4s linear infinite}
.tabs{display:flex;gap:6px;margin-bottom:10px}small{opacity:.7}
html.nf h3{font-size:17px}html.nf h1{font-size:28px}html.nf #bar .logo{font-size:18px}
.cp{cursor:pointer;user-select:all;color:var(--ac)}.sm{padding:3px 10px;font-size:13px}
.fb{background:var(--gl);border:1px solid var(--bd);border-radius:12px;padding:8px 14px;cursor:pointer;backdrop-filter:blur(6px)}.fb:hover{background:var(--hv,rgba(255,255,255,.14))}
.conf{display:grid;grid-template-columns:minmax(0,1fr) 300px;gap:14px;align-items:start}.conf .card{margin-bottom:0}@media(max-width:820px){.conf{grid-template-columns:1fr}}
#cm{max-height:45vh;min-height:120px;overflow:auto;margin-bottom:8px}
.call .avc{background-size:cover;background-position:center}
.call .tc{position:absolute;top:6px;left:50%;transform:translateX(-50%);z-index:6;display:flex;gap:4px;opacity:0;transition:opacity .2s}.call:hover .tc,.call.pin .tc{opacity:1}@media(hover:none){.call .tc{opacity:1}}
.call .tc button{padding:2px 8px;font-size:14px;background:rgba(0,0,0,.55);color:#fff;border-radius:10px}.call .tc button.on{border-color:var(--ac)}
.tiles.pn{grid-template-columns:repeat(auto-fit,minmax(min(100%,180px),1fr))}.tiles.pn .call.pin{grid-column:1/-1;order:-1;aspect-ratio:auto;height:min(68vh,620px)}.call.pin{touch-action:none}.call.pin video{cursor:grab}
.call.sp{animation:rg var(--gs,2.4s) linear infinite}
@keyframes rg{0%,100%{border-color:#f33;box-shadow:0 0 16px 3px #f33}17%{border-color:#fa0;box-shadow:0 0 16px 3px #fa0}33%{border-color:#ee2;box-shadow:0 0 16px 3px #ee2}50%{border-color:#3d5;box-shadow:0 0 16px 3px #3d5}67%{border-color:#3af;box-shadow:0 0 16px 3px #3af}83%{border-color:#a5f;box-shadow:0 0 16px 3px #a5f}}
#nf{position:fixed;top:calc(env(safe-area-inset-top,0px) + 8px);left:50%;transform:translateX(-50%);z-index:70;display:flex;gap:8px;flex-wrap:wrap;justify-content:center;width:96vw;pointer-events:none}
.nfc{pointer-events:auto;width:150px;min-height:150px;display:flex;flex-direction:column;justify-content:space-between;gap:8px;padding:10px;border-radius:14px;background:var(--bg);color:var(--tx);border:1px solid var(--ac);box-shadow:0 6px 24px rgba(0,0,0,.45);animation:nin .25s;font-size:13px}
.nft{overflow:hidden;word-break:break-word;flex:1;display:-webkit-box;-webkit-line-clamp:5;-webkit-box-orient:vertical}.nfb{display:grid;gap:6px}.nfb button{padding:6px 8px;font-size:13px}
@keyframes nin{from{transform:translateY(-14px);opacity:0}}
.mdb{position:fixed;inset:0;z-index:80;background:rgba(0,0,0,.6);display:grid;place-items:center;padding:14px}.mdb .card{background:var(--bg);max-width:420px;width:100%;margin:0}
</style></head><body><div id="nf"></div><div id="md"></div><div id="app"></div>
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
function img(inp,k){const f=inp.files[0];if(!f)return;const r=new FileReader();r.onload=()=>{const im=new Image();im.onload=()=>{const m=k=='av'?256:k=='cbg'?640:1280,s=Math.min(1,m/Math.max(im.width,im.height)),c=document.createElement('canvas');c.width=im.width*s;c.height=im.height*s;c.getContext('2d').drawImage(im,0,0,c.width,c.height);const u=c.toDataURL('image/jpeg',k=='cbg'?.6:.8);if(k=='av'){S.avimg=u;S.av='img'}else if(k=='cbg'){S.cbg=u;cbgSend()}else S.bgimg=u;save();render()};im.src=r.result};r.readAsDataURL(f)}
const sha=async t=>[...new Uint8Array(await crypto.subtle.digest('SHA-256',new TextEncoder().encode(t)))].map(x=>x.toString(16).padStart(2,'0')).join('');
const save=()=>{store.set('pc_u_'+U,S);store.set('pc_taken',TK)};let TK=Object.assign({window:[]},store.get('pc_taken',{santa:[],tree:[],ball:[]}));
function take(g){const f=[];for(let i=1;i<=50;i++)if(!TK[g].includes(i))f.push(i);if(!f.length)return 0;const n=f[Math.random()*f.length|0];TK[g].push(n);return n}
function esc(t){return String(t).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]))}
function applyTheme(){const s=S?.set||{bri:1,hue:270};document.documentElement.style.setProperty('--bgimg',S?.bgimg?`url(${S.bgimg})`:'none');const d=document.documentElement.style,t=s.theme||'black',L=t=='white',has=!!S?.bgimg;d.setProperty('--h',s.hue);d.setProperty('--b',s.bri);
const rb='linear-gradient(180deg,hsl(var(--h) 90% 65%/.6) 0%,hsl(calc(var(--h) + 60) 90% 60%/.4) 25%,hsl(calc(var(--h) + 130) 90% 55%/.22) 50%,hsl(calc(var(--h) + 200) 90% 55%/.1) 70%,transparent 88%)',cl='linear-gradient(180deg,hsl(var(--h) 90% 60%/.5) 0%,transparent 70%)';
d.setProperty('--light',has?'none':t=='rainbow'?rb:t=='color'?cl:'none');
d.setProperty('--bg',L?'#f4f4f8':t=='black'?'#050505':'#0d0b1a');d.setProperty('--tx',L?'#111':'#f1eeff');d.setProperty('--ac',t=='black'?'#fff':L?'#111':'hsl(var(--h) 90% 65%)');
d.setProperty('--gl',L?'rgba(0,0,0,.05)':'rgba(255,255,255,.06)');d.setProperty('--bd',L?'rgba(0,0,0,.25)':'rgba(255,255,255,.18)');d.setProperty('--hv',L?'rgba(0,0,0,.1)':'rgba(255,255,255,.14)');d.setProperty('--bar',L?'rgba(244,244,248,.7)':'rgba(0,0,0,.6)');d.colorScheme=L?'light':'dark';const nf=s.font=='normal';d.setProperty('--f1',nf?FN:FP1);d.setProperty('--f2',nf?FN:FP2);d.setProperty('--fw',nf?'700':'400');d.setProperty('--gs',(12/(s.gsp||5)).toFixed(2)+'s');document.documentElement.classList.toggle('nf',nf)}
function today(){return new Date()}
const T=[['home','Главная'],['shop','Магазин'],['inv','Инвентарь'],['friends','Друзья'],['chats','Чаты'],['call','Звонок'],['pay','Пиксели'],['set','Настройки']];
function barHTML(){const bd={friends:S.reqIn.length,chats:Object.values(S.unread).reduce((a,b)=>a+b,0)};return `<span class="logo">PixelCall</span>${T.map(t=>`<button class="nv ${tab==t[0]?'on':''}" onclick="go('${t[0]}')">${t[1]}${bd[t[0]]?`<span class="badge">${bd[t[0]]}</span>`:''}</button>`).join('')}<span class="sp"></span><span title="${netOK?'Сеть подключена':esc(netErr||'Подключение к сети…')}" style="color:${netOK?'#3ddc84':'#e33'}">●</span><span class="px">${S.px} px</span><button id="adv" onclick="go('adv')" title="Адвент-календарь">🎁<span>Адвент-календарь</span></button>`}
function updBar(){const b=$('#bar');if(U&&S&&b)b.innerHTML=barHTML()}
function render(){applyTheme();if(!U){$('#app').innerHTML=authView();return}
$('#app').innerHTML=`<div id="bar">${barHTML()}</div><main>${view()}</main>`;updBar();if(tab=='call'&&room){drawTiles();syncBtns();updCh()}if(tab=='chats'){const m=$('#msgs');if(m)m.scrollTop=m.scrollHeight}}
function go(t){tab=t;render()}
function authView(){return `<main style="max-width:420px"><h1 style="color:var(--ac)">PixelCall</h1><div class="row" style="margin-bottom:10px">${langBtns()}</div>${pendingRoom?`<div class="card">🎥 Вас пригласили в конференцию <b>${esc(pendingRoom)}</b>. Войдите или зарегистрируйтесь — и вы сразу попадёте в неё.</div>`:''}<div class="card"><div class="tabs"><button class="${authMode=='in'?'on':''}" onclick="authMode='in';render()">Вход</button><button class="${authMode=='up'?'on':''}" onclick="authMode='up';render()">Регистрация</button></div>
<div style="display:grid;gap:8px"><input id="nk" placeholder="Никнейм"><input id="pw" type="password" placeholder="Пароль">
${authMode=='up'?`<select id="sv"><option>Google</option><option>Facebook</option><option>Apple ID</option><option>Email</option><option>Номер телефона</option></select><input id="ct" placeholder="Почта / аккаунт / номер для 2FA"><input id="bd" type="date" title="День рождения">`:''}
<input id="cd" placeholder="Код 2FA (демо: 123456)"><button onclick="auth()">${authMode=='in'?'Войти':'Создать аккаунт'}</button><small id="er"></small></div></div><small>Демо: вход через Google/Facebook/Apple/SMS требует сервера, здесь 2FA имитируется кодом 123456.</small></main>`}
async function auth(){const n=$('#nk').value.trim(),p=$('#pw').value,e=$('#er');if(n.length<3||p.length<6){e.textContent='Ник от 3 символов, пароль от 6';return}if($('#cd').value!='123456'){e.textContent='Неверный код 2FA';return}
const h=await sha(p),a=store.get('pc_acc',{});if(authMode=='up'){if(a[n]){e.textContent='Ник занят';return}if(!$('#ct').value.trim()){e.textContent='Укажите сервис для 2FA';return}a[n]={h,sv:$('#sv').value};store.set('pc_acc',a);U=n;S={px:0,inv:[],adv:{cells:{},last:0},friends:[],chats:{},id:String(Math.random()).slice(2,12).padEnd(10,'0'),bio:'',av:'🙂',bd:$('#bd').value,set:{bri:1,hue:270,theme:'black',bday:true,corners:['santa','tree','ball','snow']}};save()}
else{if(!a[n]||a[n].h!=h){e.textContent='Неверный ник или пароль';return}U=n;S=store.get('pc_u_'+n)}fix();afterLogin()}
function view(){return({home,shop,inv,friends,chats,call:callV,pay,set:setV,adv})[tab]()}
function bdToday(){if(!S.bd)return false;const d=new Date(S.bd),t=today();return d.getDate()==t.getDate()&&d.getMonth()==t.getMonth()}
function home(){return `<div class="card row"><div class="av on">${S.set.bday&&bdToday()?'<i>🎂</i>':''}${avh(S.av)}</div><div><b>${esc(U)}</b><br><small>PixelID: <b class="cp" onclick="copyId()" title="Нажмите, чтобы скопировать">${S.id}</b></small> <button class="sm" onclick="copyId()">📋 Копировать</button><br><input value="${esc(S.bio)}" placeholder="Цитата о себе" onchange="S.bio=this.value;save()"></div><div class="row" style="max-width:340px">${[0,1,2,3,4,5,6,7,8,9].map(i=>`<button class="pk ${S.av=='p'+i?'on':''}" onclick="S.av='p${i}';save();render()">${pav(i)}</button>`).join('')}<label>Своя картинка <input type="file" accept="image/*" onchange="img(this,'av')"></label></div></div>
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
const fr=S.friends.map(f=>card(f,isOn(f.id),[`<br><small>${isOn(f.id)?'в сети':'не в сети'}</small>`,`<button onclick="openChat('${f.id}');go('chats')">💬 Написать</button>${isOn(f.id)?`<button onclick="callFriend('${f.id}')">📞 Позвонить</button>`:''}<button onclick="delF('${f.id}')">Удалить</button>`])).join('');
return (inc?'<h3>Входящие запросы</h3>'+inc:'')+(out?'<h3>Исходящие запросы</h3>'+out:'')+'<h3>Друзья</h3>'+(fr||'<div class="card">Друзей пока нет</div>')}
function friends(){return `<div class="card">Ваш PixelID: <b class="cp" onclick="copyId()" title="Нажмите, чтобы скопировать">${S.id}</b> <button class="sm" onclick="copyId()">📋 Копировать</button> <small>— отправьте его другу, чтобы он мог добавить вас</small><div class="row" style="margin-top:8px"><input id="fid" placeholder="PixelID друга (10 цифр)" maxlength="10"><button onclick="addF()">Добавить в друзья</button></div><small>Запросы и сообщения доходят, когда оба открыли PixelCall (иначе ждут, пока друг зайдёт).</small></div><div id="fl">${friendLists()}</div>`}
function updF(){if(tab=='friends'){const e=$('#fl');if(e)e.innerHTML=friendLists()}}
const prof=()=>({nick:U,av:S.av,im:S.av=='img'?S.avimg:null});
function addF(){const v=$('#fid').value.trim();if(!/^\d{10}$/.test(v)||v==S.id||S.friends.some(f=>f.id==v)||S.reqOut.some(r=>r.id==v)){alert('Неверный ID или запрос уже отправлен');return}
if(S.reqIn.some(r=>r.id==v)){acceptReq(v);return}
S.reqOut.push({id:v,nick:'',av:'🙂'});save();tx(v,Object.assign({t:'freq'},prof()));render()}
function makeFriend(id,p){nfx('fr-'+id);S.reqIn=S.reqIn.filter(r=>r.id!=id);S.reqOut=S.reqOut.filter(r=>r.id!=id);if(!S.friends.some(f=>f.id==id))S.friends.push({id,nick:String(p.nick||'').slice(0,20),av:p.av||'🙂',im:p.im||null});save();updBar();updF();updChat()}
function acceptReq(id){const r=S.reqIn.find(x=>x.id==id);if(!r)return;makeFriend(id,r);tx(id,Object.assign({t:'facc'},prof()));toast('Теперь вы друзья с '+fname(r))}
function declineReq(id){S.reqIn=S.reqIn.filter(r=>r.id!=id);save();tx(id,{t:'frej'});updBar();updF()}
function cancelReq(id){S.reqOut=S.reqOut.filter(r=>r.id!=id);save();updF()}
function delF(id){if(!confirm('Удалить из друзей?'))return;S.friends=S.friends.filter(f=>f.id!=id);save();tx(id,{t:'unf'});updF();updChat()}
function ftabs(){return S.friends.map(f=>`<button class="${f.id==cf?'on':''}" onclick="openChat('${f.id}')"><span style="color:${isOn(f.id)?'#3ddc84':'#777'}">●</span> ${esc(fname(f))}${S.unread[f.id]?`<span class="badge">${S.unread[f.id]}</span>`:''}</button>`).join('')}
function msgsHTML(){const m=S.chats[cf]||[];return m.length?m.map(x=>`<div class="msg ${x.me?'me':''}">${x.inv?`🎥 Приглашение в конференцию <b>${x.inv}</b> <button onclick="joinFrom('${x.inv}')">Войти</button>`:'<span class="nt">'+esc(x.t)+'</span>'}${x.me?` <small>${x.ok?'✓':'⏳'}</small>`:''}</div>`).join(''):'<small>Сообщений пока нет</small>'}
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
${extraSet()}<button onclick="logout()">Выйти</button>`}
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
if(!S.reqIn.some(r=>r.id==id)&&S.reqIn.length<50){S.reqIn.push(Object.assign({id},pf()));save();notify('📨 '+(d.nick||id)+' хочет добавить вас в друзья',()=>acceptReq(id),()=>declineReq(id),{tag:'fr-'+id,ms:30000})}updBar();updF();break;
case'facc':if(S.reqOut.some(r=>r.id==id)){makeFriend(id,pf());toast('✅ '+(d.nick||id)+' принял(а) ваш запрос')}break;
case'frej':if(S.reqOut.some(r=>r.id==id)){S.reqOut=S.reqOut.filter(r=>r.id!=id);save();updF();toast('Запрос в друзья отклонён')}break;
case'unf':if(fr){S.friends=S.friends.filter(f=>f.id!=id);save();updF();updChat()}break;
case'call':{if(!fr)break;const c=parseCode(d.code);if(!c)break;ring();notify('📞 '+fname(fr)+' звонит вам',()=>{if(room)leave(true);joinFrom(c)},()=>tx(id,{t:'cdec'}),{tag:'call-'+c,ms:30000});break}
case'ccan':{const c=parseCode(d.code);if(c)nfx('call-'+c);break}
case'cdec':toast('📵 '+(fr?fname(fr):id)+' отклонил(а) звонок');break;
case'toff':tradeMsg(id,fr,d);break;
case'tacc':if(fr)tradeAcc(id,d);break;
case'tok':if(fr)tradeOk(id,d);break;
case'tfail':if(fr)tradeFail(id,d);break;
case'trej':if(fr)tradeRej(id,d);break;
case'ack':{const m=(S.chats[id]||[]).find(x=>x.me&&x.ts==d.ts);if(m){m.ok=1;save();updChat()}break}
case'msg':case'inv':{if(!fr)break;const a=S.chats[id]=S.chats[id]||[],ts=String(d.ts||'').slice(0,40);let m;
if(d.t=='inv'){const c=parseCode(d.code);if(!c)break;m={inv:c,ts}}else{if(typeof d.text!='string')break;m={t:d.text.slice(0,2000),ts}}
tx(id,{t:'ack',ts});if(a.some(x=>!x.me&&x.ts==ts))break;a.push(m);if(tab=='chats'&&cf==id){updChat()}else{S.unread[id]=(S.unread[id]||0)+1;updBar();notify('💬 '+fname(fr)+': '+(m.inv?'приглашение в конференцию':m.t.slice(0,60)),()=>{openChat(id);go('chats')},()=>{},{nt:!m.inv,ms:12000})}save();break}}}

/* ===== КОНФЕРЕНЦИИ ===== */
const GK=['santa','tree','ball','window'];
const myGifts=()=>S.set.corners.map(c=>{const k=c=='snow'?'ball':c;return k!='none'&&S.inv.some(x=>x.g==k)?k:null});
const ICM='<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round"><rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0 0 12 5M19 11a7 7 0 0 1-.5 2.5M12 18v3"/><path d="M3 3l18 18" stroke="#f55"/></svg>';
const ICC='<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="7" width="12" height="10" rx="2"/><path d="M15 11l6-3v8l-6-3"/><path d="M3 3l18 18" stroke="#f55"/></svg>';
function rc(){const a='ABCDEFGHJKMNPQRSTUVWXYZ23456789';let s='';for(let i=0;i<8;i++)s+=a[Math.random()*a.length|0];return s.slice(0,4)+'-'+s.slice(4)}
function parseCode(v){v=String(v||'').trim();const m=v.match(/room=([A-Za-z0-9-]+)/);if(m)v=m[1];v=v.toUpperCase().replace(/[^A-Z0-9]/g,'');return v.length==8?v.slice(0,4)+'-'+v.slice(4):''}
function roomLink(){let b='';for(const w of [()=>window.top,()=>parent]){try{const l=w().location;if(/^https?:/.test(l.origin)){b=l.origin+l.pathname;break}}catch(e){}}return b?b+'?room='+room.code:room.code}

function copyRoom(el){el.classList.toggle('open');copyTxt(roomLink()).then(()=>toast('Ссылка на конференцию скопирована'))}
function mkRoom(){if(room)return;joinRoom(rc(),true)}
function joinFrom(v){const c=parseCode(v);if(!c){alert('Неверный код конференции');return}if(room){alert('Вы уже в конференции');go('call');return}tab='call';render();joinRoom(c,false)}
async function media(){let s=null;
try{s=await navigator.mediaDevices.getUserMedia({video:{width:{ideal:640},height:{ideal:360}},audio:{echoCancellation:true,noiseSuppression:true}})}catch(e){try{s=await navigator.mediaDevices.getUserMedia({audio:true})}catch(e2){}}
if(!s)s=new MediaStream();
if(!s.getVideoTracks().length){const c=document.createElement('canvas');c.width=320;c.height=180;c.getContext('2d').fillRect(0,0,320,180);s.addTrack(c.captureStream(1).getVideoTracks()[0]);s.noCam=true}
return s}
async function joinRoom(code,host){if(room)return;room={code,host,parts:{},stream:null,sharing:null,raw:code.replace('-',''),chat:[],pin:null,an:{},rung:[]};const R=room;render();
const s=await media();if(room!==R){s.getTracks().forEach(t=>t.stop());return}R.stream=s;mic=s.getAudioTracks().length>0;camOn=!s.noCam;
const pid=RP+R.raw+'-'+(host?'h':Math.random().toString(36).slice(2,8));R.pid=pid;let rp;try{rp=new Peer(pid)}catch(e){alert('Не удалось подключиться к сети');leave();return}R.rp=rp;
rp.on('open',()=>{if(room!==R)return;if(!host){rdata(RP+R.raw+'-h');callTo(RP+R.raw+'-h')}drawTiles();syncBtns()});
rp.on('connection',c=>rwire(c));
rp.on('call',call=>{if(room!==R)return;call.answer(R.stream);callWire(call)});
rp.on('error',e=>{if(room!==R)return;if(e.type=='unavailable-id'&&host){leave(true);mkRoom()}else if(e.type=='peer-unavailable'&&/-h\b/.test(e.message||'')&&!host){alert('Конференция не найдена: проверьте код или хост ещё не вошёл');leave()}})}
function rdata(id){const c=room.rp.connect(id,{reliable:true});rwire(c)}
function callTo(id){const R=room;if(!R||R.parts[id]&&R.parts[id].call)return;const c=R.rp.call(id,R.stream);if(c)callWire(c)}
function rwire(c){const R=room;c.on('open',()=>{if(room!==R)return;const p=R.parts[c.peer]=R.parts[c.peer]||{};p.conn=c;c.send(Object.assign({t:'hi',mic,cam:camOn||!!R.sharing,gifts:myGifts(),cbg:S.cbg||null},prof()))});
c.on('data',d=>rdat(c,d));c.on('close',()=>dropPart(c.peer));c.on('error',()=>{})}
function rdat(c,d){if(!room||!d||typeof d!='object')return;const id=c.peer,p=room.parts[id]=room.parts[id]||{};
if(d.t=='hi'||d.t=='st'){if(d.t=='hi'){p.nick=String(d.nick||'Гость').slice(0,20);p.av=typeof d.av=='string'?d.av.slice(0,8):'🙂';p.im=typeof d.im=='string'&&d.im.length<400000?d.im:null;p.cbg=okImg(d.cbg)}
p.mic=d.mic!==false;p.cam=d.cam!==false;p.gifts=Array.isArray(d.gifts)?d.gifts.slice(0,4).map(k=>GK.includes(k)?k:null):[];
if(d.t=='hi'&&room.host)c.send({t:'list',ids:Object.keys(room.parts).filter(k=>k!=id&&room.parts[k].conn&&room.parts[k].conn.open)});drawTiles()}
else if(d.t=='list'&&!room.listed){room.listed=1;(Array.isArray(d.ids)?d.ids:[]).slice(0,12).forEach(i=>{if(typeof i=='string'&&i.startsWith(RP+room.raw+'-')&&i!=room.pid){if(!(room.parts[i]&&room.parts[i].conn))rdata(i);callTo(i)}})}
else if(d.t=='cbg'){p.cbg=okImg(d.cbg);drawTiles()}
else if(d.t=='chat'&&typeof d.text=='string'){const m={nick:p.nick||'Гость',text:d.text.slice(0,500)};room.chat.push(m);if(room.chat.length>200)room.chat.shift();updCh();if(tab!='call')notify('💬 '+m.nick+': '+m.text.slice(0,60),()=>go('call'),()=>{},{nt:true,ms:8000})}}
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
function leave(silent){if(!room)return;const R=room;(R.rung||[]).forEach(i=>tx(i,{t:'ccan',code:R.code}));Object.values(R.an||{}).forEach(a=>{try{a.src.disconnect()}catch(e){}});try{stopScr()}catch(e){}Object.values(R.parts).forEach(p=>{try{p.conn&&p.conn.close()}catch(e){}try{p.call&&p.call.close()}catch(e){}});try{R.rp&&R.rp.destroy()}catch(e){}R.stream&&R.stream.getTracks().forEach(t=>t.stop());document.querySelectorAll('audio.ra').forEach(a=>a.remove());room=null;if(!silent)render()}

function syncBtns(){const f=(id,off)=>{const e=document.getElementById(id);if(e)e.classList.toggle('off',off)};f('bcam',!camOn);f('bmic',!mic);const s=document.getElementById('bscr');if(s)s.classList.toggle('on',!!(room&&room.sharing))}
const ZM={};let dg=null;
const okImg=s=>typeof s=='string'&&s.length<400000&&/^data:image\/(jpeg|png|webp);base64,[A-Za-z0-9+\/=]+$/.test(s)?s:null;
function tileHTML(id,o,local){const camv=local?(camOn||!!room.sharing):o.cam!==false,micv=local?mic:o.mic!==false,gl=local?myGifts():(o.gifts||[]),pos=['left:6px;top:6px','right:6px;top:6px','left:6px;bottom:6px','right:6px;bottom:6px'],pn=room.pin==id,z=ZM[id]||{z:1,x:0,y:0},cb=okImg(local?S.cbg:o.cbg);
return `<div class="call ${micv?'':'mo'} ${pn?'pin':''}" id="t-${id}"><video autoplay playsinline muted${pn?` style="object-fit:contain;transform:translate(${z.x}px,${z.y}px) scale(${z.z})"`:''}></video><div class="avc" style="display:${camv?'none':'grid'}${cb?`;background-image:url(${cb})`:''}"><div class="av">${local?avh(S.av):avh2(o.av,o.im)}</div></div>${gl.map((k,i)=>k?`<div class="cn" style="${pos[i]}">${svg(k,'bob')}</div>`:'').join('')}<div class="tc">${pn?`<button title="Приблизить" onclick="zoom('${id}',.5)">＋</button><button title="Отдалить" onclick="zoom('${id}',-.5)">－</button><button title="Сбросить" onclick="zoom('${id}',0)">⟲</button>`:''}<button class="${pn?'on':''}" title="${pn?'Открепить':'Закрепить'}" onclick="pin('${id}')">📌</button></div><div class="bad" style="display:${(local?room.lbad:o.bad)?'block':'none'}">Плохое подключение к интернету</div><div class="nm">${esc(local?U+' (вы)':(o.nick||'Гость'))}</div><div class="ic">${micv?'':ICM}${camv?'':ICC}</div></div>`}
function drawTiles(){const t=$('#tiles');if(!t||!room||!room.stream)return;const ps=Object.entries(room.parts).filter(([k,p])=>/^[\w-]+$/.test(k)&&(p.nick||p.stream));
if(room.pin&&room.pin!='me'&&!ps.some(([k])=>k==room.pin))room.pin=null;
t.className='tiles'+(room.pin?' pn':'');t.innerHTML=tileHTML('me',{},true)+ps.map(([k,p])=>tileHTML(k,p,false)).join('');
const att=(id,st)=>{const v=document.querySelector('#t-'+id+' video');if(v&&st){v.srcObject=st;v.play().catch(()=>{})}};att('me',room.sharing||room.stream);ps.forEach(([k,p])=>att(k,p.stream))}
function pin(id){if(!room)return;room.pin=room.pin==id?null:id;drawTiles()}
function clampZ(id){const z=ZM[id],t=document.getElementById('t-'+id);if(!z||!t)return;const mx=t.clientWidth*(z.z-1)/2,my=t.clientHeight*(z.z-1)/2;z.x=Math.max(-mx,Math.min(mx,z.x));z.y=Math.max(-my,Math.min(my,z.y))}
function applyZ(id){const v=document.querySelector('#t-'+id+' video'),z=ZM[id];if(v&&z)v.style.transform=`translate(${z.x}px,${z.y}px) scale(${z.z})`}
function zoom(id,d){const z=ZM[id]=ZM[id]||{z:1,x:0,y:0};if(d==0)z.z=1;else z.z=Math.max(1,Math.min(5,z.z+d));if(z.z==1){z.x=0;z.y=0}clampZ(id);applyZ(id)}
addEventListener('wheel',e=>{const t=e.target.closest&&e.target.closest('.call.pin');if(!t)return;e.preventDefault();zoom(t.id.slice(2),e.deltaY<0?.25:-.25)},{passive:false});
addEventListener('pointerdown',e=>{const t=e.target.closest&&e.target.closest('.call.pin');if(!t||e.target.closest('button'))return;const id=t.id.slice(2),z=ZM[id];if(!z||z.z<=1)return;dg={id,sx:e.clientX-z.x,sy:e.clientY-z.y}});
addEventListener('pointermove',e=>{if(!dg)return;const z=ZM[dg.id];if(!z){dg=null;return}z.x=e.clientX-dg.sx;z.y=e.clientY-dg.sy;clampZ(dg.id);applyZ(dg.id)});
addEventListener('pointerup',()=>{dg=null});addEventListener('pointercancel',()=>{dg=null});
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
function fcalls(){const on=S.friends.filter(f=>isOn(f.id));return on.length?`<div class="row">${on.map(f=>`<button onclick="callFriend('${f.id}')">📞 ${esc(fname(f))}</button>`).join('')}</div>`:'<small>Друзья в сети появятся здесь — их можно позвать в один клик.</small>'}
function callV(){if(!room)return `<div class="card"><h3>Конференция</h3><div class="row"><button onclick="mkRoom()">➕ Создать конференцию</button><input id="rm" placeholder="Код или ссылка"><button onclick="joinFrom($('#rm').value)">Войти</button></div><small>Создайте конференцию и отправьте другу код (или ссылку). Нужен доступ к камере и микрофону — если их нет, можно зайти и без них.</small></div><div class="card"><h3>Позвонить другу</h3>${fcalls()}</div>`;
return `<div class="conf"><div class="card"><div class="wrapc"><div class="cc" onclick="copyRoom(this)" title="Нажмите, чтобы скопировать ссылку"><div class="stick"></div><div class="code">${room.code}</div></div><div id="tiles" class="tiles"></div></div>
<div class="row" style="margin-top:10px"><button id="bcam" onclick="togCam()">📷 Камера</button><button id="bmic" onclick="togMic()">🎤 Микрофон</button><button id="bscr" onclick="scr()">🖥 Демонстрация экрана</button><label class="fb">🖼 Фон без камеры<input type="file" accept="image/*" hidden onchange="img(this,'cbg')"></label><button onclick="leave()" style="border-color:#e33;color:#f66">Выйти</button></div>
<div class="row" style="margin-top:10px"><b>Позвонить:</b> ${fcalls()}</div>
<small>Наведите на палочку сверху — появится код конференции, клик копирует ссылку. Кнопка 📌 на плитке закрепляет её; у закреплённой можно приближать колесом мыши или кнопками ＋ / －, а двигать — перетаскиванием.</small></div>
<div class="card"><h3>Чат конференции</h3><div id="cm"></div><div class="row"><input id="ci" placeholder="Сообщение" style="flex:1;min-width:0" maxlength="500" onkeydown="if(event.key=='Enter')sendCh()"><button onclick="sendCh()">➤</button></div></div></div>`}

/* ===== ДОПОЛНЕНИЯ: язык, шрифт, копирование ID, чат, звонки, обмен, уведомления, свечение ===== */
const FP1="'Pixelify Sans','Courier New',monospace",FP2="'Press Start 2P','Courier New',monospace",FN="system-ui,'Segoe UI',Roboto,Arial,sans-serif";
let LANG=store.get('pc_lang','ru');if(!['ru','en','uk'].includes(LANG))LANG='ru';
const TR={
'Главная':['Home','Головна'],'Магазин':['Shop','Магазин'],'Инвентарь пуст':['Inventory is empty','Інвентар порожній'],'Инвентарь':['Inventory','Інвентар'],'Друзья':['Friends','Друзі'],'Чаты':['Chats','Чати'],'Звонок':['Call','Дзвінок'],'Пиксели':['Pixels','Пікселі'],'Настройки':['Settings','Налаштування'],
'Сеть подключена':['Network connected','Мережу підключено'],'Подключение к сети…':['Connecting to network…','Підключення до мережі…'],'Этот аккаунт уже открыт в другой вкладке':['This account is already open in another tab','Цей акаунт уже відкрито в іншій вкладці'],'Сеть: ':['Network: ','Мережа: '],
'Адвент-календарь (1–24 декабря)':['Advent calendar (Dec 1–24)','Адвент-календар (1–24 грудня)'],'Адвент-календарь':['Advent calendar','Адвент-календар'],
'Вас пригласили в конференцию':['You were invited to the conference','Вас запросили до конференції'],'Войдите или зарегистрируйтесь — и вы сразу попадёте в неё.':['Sign in or sign up and you will join it right away.','Увійдіть або зареєструйтеся — і ви одразу потрапите до неї.'],
'Вход':['Sign in','Вхід'],'Регистрация':['Sign up','Реєстрація'],'Никнейм':['Nickname','Нікнейм'],'Пароль':['Password','Пароль'],'Номер телефона':['Phone number','Номер телефону'],'Почта / аккаунт / номер для 2FA':['Email / account / number for 2FA','Пошта / акаунт / номер для 2FA'],'Код 2FA (демо: 123456)':['2FA code (demo: 123456)','Код 2FA (демо: 123456)'],
'Войти':['Log in','Увійти'],'Создать аккаунт':['Create account','Створити акаунт'],'Демо: вход через Google/Facebook/Apple/SMS требует сервера, здесь 2FA имитируется кодом 123456.':['Demo: signing in via Google/Facebook/Apple/SMS needs a server; here 2FA is simulated with the code 123456.','Демо: вхід через Google/Facebook/Apple/SMS потребує сервера, тут 2FA імітується кодом 123456.'],
'Ник от 3 символов, пароль от 6':['Nickname from 3 characters, password from 6','Нік від 3 символів, пароль від 6'],'Неверный код 2FA':['Wrong 2FA code','Невірний код 2FA'],'Ник занят':['Nickname is taken','Нік зайнято'],'Укажите сервис для 2FA':['Specify a service for 2FA','Вкажіть сервіс для 2FA'],'Неверный ник или пароль':['Wrong nickname or password','Невірний нік або пароль'],
'Цитата о себе':['A quote about yourself','Цитата про себе'],'Встречи':['Meetings','Зустрічі'],'Создать встречу':['Create meeting','Створити зустріч'],'Код или ссылка':['Code or link','Код або посилання'],
'осталось':['left','залишилось'],'Купить':['Buy','Купити'],'Недостаточно пикселей':['Not enough pixels','Недостатньо пікселів'],
'Санта Клаус 2027':['Santa Claus 2027','Санта Клаус 2027'],'Ёлка 2027':['Tree 2027','Ялинка 2027'],'Снежный шар 2027':['Snow globe 2027','Сніжна куля 2027'],'Замёрзшее окно 2027':['Frozen window 2027','Замерзле вікно 2027'],
'из адвента: только обмен':['from Advent: trade only','з адвенту: лише обмін'],'Предложить обмен':['Offer a trade','Запропонувати обмін'],'Продать':['Sell','Продати'],
'Входящие запросы':['Incoming requests','Вхідні запити'],'Исходящие запросы':['Outgoing requests','Вихідні запити'],'Друзей пока нет':['No friends yet','Друзів поки немає'],'Ваш PixelID:':['Your PixelID:','Ваш PixelID:'],'— отправьте его другу, чтобы он мог добавить вас':['— send it to a friend so they can add you','— надішліть його другові, щоб він міг додати вас'],
'PixelID друга (10 цифр)':['Friend’s PixelID (10 digits)','PixelID друга (10 цифр)'],'Добавить в друзья':['Add friend','Додати в друзі'],'Запросы и сообщения доходят, когда оба открыли PixelCall (иначе ждут, пока друг зайдёт).':['Requests and messages are delivered when both of you have PixelCall open (otherwise they wait until your friend comes online).','Запити та повідомлення доходять, коли обидва відкрили PixelCall (інакше чекають, поки друг зайде).'],
'Неверный ID или запрос уже отправлен':['Invalid ID or request already sent','Невірний ID або запит уже надіслано'],'Теперь вы друзья с ':['You are now friends with ','Тепер ви друзі з '],'Теперь вы друзья!':['You are now friends!','Тепер ви друзі!'],'Удалить из друзей?':['Remove from friends?','Видалити з друзів?'],
'принял(а) ваш запрос':['accepted your request','прийняв(ла) ваш запит'],'Запрос в друзья отклонён':['Friend request declined','Запит у друзі відхилено'],'хочет добавить вас в друзья':['wants to add you as a friend','хоче додати вас у друзі'],'запрос отправлен, ждём ответа':['request sent, waiting for a reply','запит надіслано, чекаємо відповіді'],
'✔ Принять':['✔ Accept','✔ Прийняти'],'✖ Отклонить':['✖ Decline','✖ Відхилити'],'Отменить':['Cancel','Скасувати'],'не в сети':['offline','не в мережі'],'в сети':['online','в мережі'],'💬 Написать':['💬 Message','💬 Написати'],'Удалить':['Delete','Видалити'],
'приглашение в конференцию':['conference invitation','запрошення в конференцію'],'Приглашение в конференцию':['Conference invitation','Запрошення в конференцію'],'Сообщений пока нет':['No messages yet','Повідомлень поки немає'],'Добавьте друзей, чтобы писать':['Add friends to start chatting','Додайте друзів, щоб писати'],'Сообщение':['Message','Повідомлення'],'Отправить':['Send','Надіслати'],
'Донат':['Donate','Донат'],'💳 Картой':['💳 By card','💳 Карткою'],'Демо: настоящая оплата PayPal и картой подключается через платёжный сервис на сервере. Здесь начисление имитируется, а выдать себе пиксели просто так нельзя.':['Demo: real PayPal and card payments are connected through a payment service on a server. Here the top-up is simulated, and you cannot give yourself pixels for free.','Демо: справжня оплата PayPal і карткою підключається через платіжний сервіс на сервері. Тут нарахування імітується, а видати собі пікселі просто так не можна.'],
'Конвертер':['Converter','Конвертер'],'Демо-оплата:':['Demo payment:','Демо-оплата:'],'банковскую карту':['bank card','банківську картку'],'От 3 до 20 символов':['From 3 to 20 characters','Від 3 до 20 символів'],
'Имя':['Name','Ім’я'],'Сохранить имя':['Save name','Зберегти ім’я'],'Новым ником нужно будет входить в аккаунт':['You will need to sign in with the new nickname','Новим ніком потрібно буде входити в акаунт'],'Тема':['Theme','Тема'],'Чёрная':['Black','Чорна'],'Белая':['White','Біла'],'Радужная':['Rainbow','Райдужна'],'Цветная':['Colored','Кольорова'],
'Со своим фоном подсветка отключена':['Highlight is off with a custom background','Зі своїм фоном підсвітка вимкнена'],'Цвет и яркость':['Color and brightness','Колір і яскравість'],'Цвет':['Color','Колір'],'Яркость':['Brightness','Яскравість'],'Фон':['Background','Фон'],'Своя картинка':['Your image','Власна картинка'],'Убрать фон':['Remove background','Прибрати фон'],
'День рождения':['Birthday','День народження'],'Показывать тортик':['Show cake','Показувати торт'],'Подарки по углам камеры':['Gifts in camera corners','Подарунки по кутах камери'],'Угол':['Corner','Кут'],'Не ставить':['None','Не ставити'],'Ставятся только те подарки, которые у вас есть.':['Only gifts you own can be placed.','Ставляться лише ті подарунки, які у вас є.'],'Выйти':['Exit','Вийти'],
'Пробная версия (без ограничений по датам)':['Trial mode (no date limits)','Пробна версія (без обмежень за датами)'],'Забрать':['Claim','Забрати'],'Ячейка раз в 24 часа. Награду можно забрать позже. Подарки из адвента нельзя продать, только обменять.':['One cell every 24 hours. You can claim the reward later. Advent gifts cannot be sold, only traded.','Комірка раз на 24 години. Нагороду можна забрати пізніше. Подарунки з адвенту не можна продати, лише обміняти.'],
'Все 50 экземпляров разобраны: вместо подарка 875 px':['All 50 copies are taken: 875 px instead of the gift','Усі 50 примірників розібрано: замість подарунка 875 px'],
'Конференция не найдена: проверьте код или хост ещё не вошёл':['Conference not found: check the code, or the host has not joined yet','Конференцію не знайдено: перевірте код або хост ще не зайшов'],'Конференция':['Conference','Конференція'],'➕ Создать конференцию':['➕ Create conference','➕ Створити конференцію'],
'Создайте конференцию и отправьте другу код (или ссылку). Нужен доступ к камере и микрофону — если их нет, можно зайти и без них.':['Create a conference and send your friend the code (or link). Camera and microphone access is needed — without them you can still join.','Створіть конференцію й надішліть другові код (або посилання). Потрібен доступ до камери й мікрофона — без них можна зайти й так.'],
'Нажмите, чтобы скопировать ссылку':['Click to copy the link','Натисніть, щоб скопіювати посилання'],'Нажмите, чтобы скопировать':['Click to copy','Натисніть, щоб скопіювати'],'📷 Камера':['📷 Camera','📷 Камера'],'🎤 Микрофон':['🎤 Microphone','🎤 Мікрофон'],'🖥 Демонстрация экрана':['🖥 Share screen','🖥 Демонстрація екрана'],
'Наведите на палочку сверху — появится код конференции, клик копирует ссылку. Кнопка 📌 на плитке закрепляет её; у закреплённой можно приближать колесом мыши или кнопками ＋ / －, а двигать — перетаскиванием.':['Hover the bar at the top to see the conference code; a click copies the link. The 📌 button pins a tile; on a pinned tile you can zoom with the mouse wheel or the ＋ / － buttons and move it by dragging.','Наведіть на палицю зверху — з’явиться код конференції, клік копіює посилання. Кнопка 📌 на плитці закріплює її; закріплену можна наближати колесом миші або кнопками ＋ / －, а рухати — перетягуванням.'],
'Ссылка на конференцию скопирована':['Conference link copied','Посилання на конференцію скопійовано'],'Плохое подключение к интернету':['Poor internet connection','Погане підключення до інтернету'],'(вы)':['(you)','(ви)'],'Гость':['Guest','Гість'],'вышел(а)':['left','вийшов(-ла)'],
'Камера не найдена или нет доступа':['Camera not found or no access','Камеру не знайдено або немає доступу'],'Демонстрация экрана недоступна':['Screen sharing is unavailable','Демонстрація екрана недоступна'],'Неверный код конференции':['Invalid conference code','Невірний код конференції'],'Вы уже в конференции':['You are already in a conference','Ви вже в конференції'],'Не удалось подключиться к сети':['Could not connect to the network','Не вдалося підключитися до мережі'],
'Друзья в сети появятся здесь — их можно позвать в один клик.':['Friends who are online will appear here — call them in one click.','Друзі в мережі з’являться тут — їх можна покликати в один клік.'],
'Позвонить другу':['Call a friend','Подзвонити другові'],'Позвонить:':['Call:','Подзвонити:'],'Позвонить':['Call','Подзвонити'],'Друг не в сети':['Friend is offline','Друг не в мережі'],'Звоним:':['Calling:','Дзвонимо:'],'звонит вам':['is calling you','дзвонить вам'],'отклонил(а) звонок':['declined the call','відхилив(-ла) дзвінок'],
'Чат конференции':['Conference chat','Чат конференції'],'Фон без камеры':['Camera-off background','Фон без камери'],'Закрепить':['Pin','Закріпити'],'Открепить':['Unpin','Відкріпити'],'Приблизить':['Zoom in','Наблизити'],'Отдалить':['Zoom out','Віддалити'],'Сбросить':['Reset','Скинути'],
'предлагает обмен: даёт':['offers a trade: gives','пропонує обмін: дає'],', хочет ':[', wants ',', хоче '],'ничего (подарок)':['nothing (a gift)','нічого (подарунок)'],'Что хотите взамен':['What you want in return','Що хочете натомість'],'Кому':['To','Кому'],'Ничего (просто подарить)':['Nothing (just give it)','Нічого (просто подарувати)'],'Отмена':['Cancel','Скасувати'],
'Нужен друг в сети: обмен происходит, когда вы оба онлайн':['A friend must be online: trades happen when you are both online','Потрібен друг у мережі: обмін відбувається, коли ви обидва онлайн'],'У вас нет такого подарка':['You do not have that gift','У вас немає такого подарунка'],'Обмен завершён':['Trade completed','Обмін завершено'],'Вы получили':['You received','Ви отримали'],
'Обмен не удался, подарок возвращён':['The trade failed, your gift was returned','Обмін не вдався, подарунок повернено'],'Обмен отклонён':['Trade declined','Обмін відхилено'],'Предложение обмена отправлено':['Trade offer sent','Пропозицію обміну надіслано'],
'Язык':['Language','Мова'],'Шрифт':['Font','Шрифт'],'Пиксельный':['Pixel','Піксельний'],'Обычный':['Normal','Звичайний'],'Свечение при разговоре':['Speaking glow','Світіння під час розмови'],'Включить':['Enable','Увімкнути'],'Скорость':['Speed','Швидкість'],'Радужная подсветка вокруг того, кто сейчас говорит.':['Rainbow glow around whoever is speaking.','Райдужна підсвітка навколо того, хто зараз говорить.'],
'Фон при выключенной камере':['Background when camera is off','Фон при вимкненій камері'],'Картинка':['Image','Картинка'],'Убрать':['Remove','Прибрати'],'Его видят все в конференции, когда у вас выключена камера. Поставить фон можно только себе.':['Everyone in the conference sees it when your camera is off. You can only set it for yourself.','Його бачать усі в конференції, коли у вас вимкнена камера. Поставити фон можна лише собі.'],
'Копировать':['Copy','Копіювати'],'PixelID скопирован':['PixelID copied','PixelID скопійовано']};
const TKS=Object.keys(TR).sort((a,b)=>b.length-a.length),CY=/[\u0400-\u04FF]/;
function trl(s){if(LANG=='ru'||!CY.test(s))return s;const i=LANG=='en'?0:1;for(const k of TKS)if(s.includes(k))s=s.split(k).join(TR[k][i]);return s}
function trNode(n){if(n.nodeType==3){const p=n.parentElement;if(!p||p.closest('.nt,script,style'))return;const v=trl(n.nodeValue);if(v!==n.nodeValue)n.nodeValue=v}
else if(n.nodeType==1){if(n.closest('.nt'))return;for(const a of ['title','placeholder']){const v=n.getAttribute(a);if(v){const w=trl(v);if(w!==v)n.setAttribute(a,w)}}for(let c=n.firstChild;c;c=c.nextSibling)trNode(c)}}
const MOC={childList:true,subtree:true,characterData:true,attributes:true,attributeFilter:['title','placeholder']};
const mo=new MutationObserver(ms=>{if(LANG=='ru')return;mo.disconnect();try{for(const m of ms){if(m.type=='childList')m.addedNodes.forEach(trNode);else trNode(m.target)}}finally{mo.observe(document.body,MOC)}});
mo.observe(document.body,MOC);document.documentElement.lang=LANG;
{const _al=window.alert.bind(window),_cf=window.confirm.bind(window);window.alert=s=>_al(trl(String(s)));window.confirm=s=>_cf(trl(String(s)))}
const langBtns=()=>[['ru','Русский'],['en','English'],['uk','Українська']].map(([k,n])=>`<button class="${LANG==k?'on':''}" onclick="setLang('${k}')">${n}</button>`).join('');
function setLang(l){LANG=l;store.set('pc_lang',l);document.documentElement.lang=l;render()}
function extraSet(){const s=S.set;return `<div class="card"><h3>Язык</h3><div class="row">${langBtns()}</div></div>
<div class="card"><h3>Шрифт</h3><div class="row"><button class="${s.font!='normal'?'on':''}" onclick="S.set.font='pixel';save();render()">Пиксельный</button><button class="${s.font=='normal'?'on':''}" onclick="S.set.font='normal';save();render()">Обычный</button></div></div>
<div class="card"><h3>Свечение при разговоре</h3><div class="row"><label><input type="checkbox" ${s.glow!==false?'checked':''} onchange="S.set.glow=this.checked;save()"> Включить</label><label>Скорость <input type="range" min="1" max="10" value="${s.gsp||5}" oninput="S.set.gsp=+this.value;applyTheme()" onchange="save()"></label></div><small>Радужная подсветка вокруг того, кто сейчас говорит.</small></div>
<div class="card"><h3>Фон при выключенной камере</h3>${S.cbg?`<img src="${S.cbg}" style="max-width:200px;border-radius:10px;display:block;margin-bottom:8px" alt="">`:''}<label>Картинка <input type="file" accept="image/*" onchange="img(this,'cbg')"></label> <button onclick="S.cbg='';save();cbgSend();render()">Убрать</button><br><small>Его видят все в конференции, когда у вас выключена камера. Поставить фон можно только себе.</small></div>`}
function copyTxt(t){const fb=()=>{const a=document.createElement('textarea');a.value=t;a.style.cssText='position:fixed;opacity:0';document.body.appendChild(a);a.select();try{document.execCommand('copy')}catch(e){}a.remove()};try{return navigator.clipboard.writeText(t).catch(fb)}catch(e){fb();return Promise.resolve()}}
function copyId(){copyTxt(S.id).then(()=>toast('PixelID скопирован'))}

/* --- всплывающие квадратики сверху (сообщение / друг / звонок / обмен) --- */
const NF={};let nfn=0;
function notify(txt,acc,rej,o){o=o||{};if(o.tag)nfx(o.tag);const ks=Object.keys(NF);if(ks.length>=4)nfd(ks[0]);const k='n'+(++nfn),el=document.createElement('div');el.className='nfc';
el.innerHTML='<div class="nft'+(o.nt?' nt':'')+'"></div><div class="nfb"><button onclick="nfa(\''+k+'\',1)">✔ Принять</button><button onclick="nfa(\''+k+'\',0)">✖ Отклонить</button></div>';el.firstChild.textContent=txt;$('#nf').appendChild(el);
NF[k]={el,acc,rej,tag:o.tag,tm:setTimeout(()=>nfd(k),o.ms||20000)}}
function nfd(k){const n=NF[k];if(!n)return null;clearTimeout(n.tm);n.el.remove();delete NF[k];return n}
function nfa(k,ok){const n=nfd(k);if(!n)return;const f=ok?n.acc:n.rej;try{f&&f()}catch(e){}}
function nfx(tag){Object.keys(NF).forEach(k=>{if(NF[k].tag===tag)nfd(k)})}
let AC=null;
function ring(){let n=0;const b=()=>{try{AC=AC||new(window.AudioContext||window.webkitAudioContext)();const o=AC.createOscillator(),g=AC.createGain();o.connect(g);g.connect(AC.destination);o.frequency.value=n%2?660:880;g.gain.value=.06;o.start();o.stop(AC.currentTime+.2)}catch(e){}if(++n<6)setTimeout(b,350)};b()}

/* --- звонок другу --- */
function callFriend(id){if(!isOn(id)){alert('Друг не в сети');return}if(!room){tab='call';mkRoom()}if(!room)return;const f=S.friends.find(x=>x.id==id);
tx(id,{t:'call',code:room.code,ts:rid()});(room.rung=room.rung||[]).push(id);if(tab!='call')go('call');toast('📞 Звоним: '+(f?fname(f):id))}

/* --- чат внутри конференции --- */
function chHTML(){return room.chat.length?room.chat.map(m=>`<div class="msg ${m.me?'me':''}">${m.me?'':`<small>${esc(m.nick)}</small><br>`}<span class="nt">${esc(m.text)}</span></div>`).join(''):'<small>Сообщений пока нет</small>'}
function updCh(){if(!room)return;const m=$('#cm');if(m){m.innerHTML=chHTML();m.scrollTop=m.scrollHeight}}
function sendCh(){const i=$('#ci');if(!room||!i)return;const t=i.value.trim().slice(0,500);if(!t)return;i.value='';room.chat.push({me:1,text:t});
Object.values(room.parts).forEach(p=>{try{p.conn&&p.conn.open&&p.conn.send({t:'chat',text:t})}catch(e){}});updCh()}
function cbgSend(){if(!room)return;Object.values(room.parts).forEach(p=>{try{p.conn&&p.conn.open&&p.conn.send({t:'cbg',cbg:S.cbg||null})}catch(e){}})}

/* --- обмен подарками --- */
const RES={},TO={};
function trade(i){const it=S.inv[i],on=S.friends.filter(f=>isOn(f.id));if(!it)return;if(!on.length){alert('Нужен друг в сети: обмен происходит, когда вы оба онлайн');return}
$('#md').innerHTML=`<div class="mdb"><div class="card"><h3>Предложить обмен</h3><p>${G[it.g].n} #${it.n}</p><div style="display:grid;gap:8px"><label>Кому <select id="tf">${on.map(f=>`<option value="${f.id}">${esc(fname(f))}</option>`).join('')}</select></label><label>Что хотите взамен <select id="ta"><option value="none">Ничего (просто подарить)</option>${GK.map(k=>`<option value="${k}">${G[k].n}</option>`).join('')}</select></label><div class="row"><button onclick="tsend(${i})">Отправить</button><button onclick="$('#md').innerHTML=''">Отмена</button></div></div></div></div>`}
function tsend(i){const it=S.inv[i],id=$('#tf').value,ask=$('#ta').value;if(!it)return;if(!isOn(id)){alert('Друг не в сети');return}const ts=rid();TO[ts]={g:it.g,n:it.n,to:id,ask};tx(id,{t:'toff',ts,g:it.g,n:it.n,ask});$('#md').innerHTML='';toast('Предложение обмена отправлено')}
function tacc(id,ts,g,n,ask){let give=null;if(ask!='none'){const i=S.inv.findIndex(x=>x.g==ask);if(i<0){alert('У вас нет такого подарка');tx(id,{t:'trej',ts});return}give=S.inv.splice(i,1)[0];save()}
if(!tx(id,{t:'tacc',ts,g:give?give.g:null,n:give?give.n:null,adv:give?!!give.adv:false})){if(give){S.inv.push(give);save()}alert('Друг не в сети');return}
RES[ts]={from:id,g,n,give,tm:setTimeout(()=>{const r=RES[ts];if(!r)return;delete RES[ts];if(r.give)S.inv.push(r.give);save();toast('Обмен не удался, подарок возвращён');if(tab=='inv')render()},20000)};if(tab=='inv')render()}
function tradeMsg(id,fr,d){const ts=String(d.ts||'').slice(0,40),g=d.g,n=+d.n,ask=d.ask;if(!fr||!ts||!GK.includes(g)||!(n>=1&&n<=50)||!(ask=='none'||GK.includes(ask)))return;
notify('🔁 '+fname(fr)+' предлагает обмен: даёт '+G[g].n+' #'+n+', хочет '+(ask=='none'?'ничего (подарок)':G[ask].n),()=>tacc(id,ts,g,n,ask),()=>tx(id,{t:'trej',ts}),{tag:'t-'+ts,ms:60000})}
function tradeAcc(id,d){const o=TO[d.ts];if(!o||o.to!=id){tx(id,{t:'tfail',ts:d.ts});return}delete TO[d.ts];
const idx=S.inv.findIndex(x=>x.g==o.g&&x.n==o.n),ok=idx>=0&&(o.ask=='none'?!d.g:(d.g==o.ask&&+d.n>=1&&+d.n<=50));if(!ok){tx(id,{t:'tfail',ts:d.ts});return}
const gone=S.inv.splice(idx,1)[0];if(o.ask!='none')S.inv.push({g:d.g,n:+d.n,adv:!!d.adv});save();tx(id,{t:'tok',ts:d.ts,g:gone.g,n:gone.n,adv:!!gone.adv});toast('Обмен завершён');if(tab=='inv')render()}
function tradeOk(id,d){const r=RES[d.ts];if(!r||r.from!=id||d.g!=r.g||+d.n!=r.n)return;clearTimeout(r.tm);delete RES[d.ts];S.inv.push({g:r.g,n:r.n,adv:!!d.adv});save();toast('Вы получили '+G[r.g].n+' #'+r.n);if(tab=='inv')render()}
function tradeFail(id,d){const r=RES[d.ts];if(r&&r.from==id){clearTimeout(r.tm);delete RES[d.ts];if(r.give)S.inv.push(r.give);save();toast('Обмен не удался, подарок возвращён');if(tab=='inv')render()}else if(TO[d.ts]&&TO[d.ts].to==id)delete TO[d.ts]}
function tradeRej(id,d){if(TO[d.ts]&&TO[d.ts].to==id){delete TO[d.ts];toast('Обмен отклонён')}}

/* --- радужное свечение того, кто говорит --- */
function vad(){if(!room||!room.stream||!S)return;if(S.set.glow===false){document.querySelectorAll('.call.sp').forEach(e=>e.classList.remove('sp'));return}
try{AC=AC||new(window.AudioContext||window.webkitAudioContext)();if(AC.state=='suspended')AC.resume().catch(()=>{})}catch(e){return}
const an=room.an;
const chk=(id,st,en)=>{let sp=false;if(st&&st.getAudioTracks().length){let a=an[id];if(!a||a.st!==st){try{const n=AC.createAnalyser();n.fftSize=512;const src=AC.createMediaStreamSource(st);src.connect(n);a=an[id]={st,n,src,b:new Uint8Array(512),h:0}}catch(e){a=null}}
if(a){a.n.getByteTimeDomainData(a.b);let m=0;for(let i=0;i<a.b.length;i++)m=Math.max(m,Math.abs(a.b[i]-128));a.h=m>12?4:Math.max(0,a.h-1);sp=en&&a.h>0}}
const e=document.getElementById('t-'+id);if(e)e.classList.toggle('sp',!!sp)};
chk('me',room.stream,mic);Object.entries(room.parts).forEach(([k,p])=>chk(k,p.stream,p.mic!==false))}
setInterval(vad,100);
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

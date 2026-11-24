src = open('/mnt/user-data/uploads/pixelcall__4_.py', encoding='utf-8').read()

def rep(old, new, cnt=1):
    global src
    assert src.count(old) == cnt, (old[:70], src.count(old))
    src = src.replace(old, new)

def repline(prefix, new):
    global src
    lines = src.split('\n'); n = 0
    for i, l in enumerate(lines):
        if l.startswith(prefix):
            lines[i] = new; n += 1
    assert n == 1, (prefix, n)
    src = '\n'.join(lines)

# ---------------- CSS ----------------
rep("font:16px 'Pixelify Sans','Courier New',monospace;", "font:16px var(--fb,'Pixelify Sans','Courier New',monospace);")
rep("h1,h3,#bar .logo{font-family:'Press Start 2P','Courier New',monospace;font-weight:400}",
    "h1,h3,#bar .logo{font-family:var(--fh,'Press Start 2P','Courier New',monospace);font-weight:var(--fw,400)}")
rep("font-family:'Press Start 2P','Courier New',monospace;font-size:12px;color:#fff",
    "font-family:var(--fh,'Press Start 2P','Courier New',monospace);font-size:12px;color:#fff")
rep("</style></head><body><div id=\"app\"></div>", r'''
.nf h3{font-size:16px;font-weight:700}.nf h1{font-size:26px}.nf #bar .logo{font-size:18px}
.cp{cursor:pointer;user-select:all;border-bottom:1px dashed var(--ac)}
label.fb{background:var(--gl);border:1px solid var(--bd);border-radius:12px;padding:8px 14px;cursor:pointer;display:inline-block}
#nt{position:fixed;top:8px;left:50%;transform:translateX(-50%);z-index:100;display:flex;gap:8px;justify-content:center;flex-wrap:wrap;width:min(96vw,760px);pointer-events:none;padding-top:env(safe-area-inset-top,0px)}
.nc{pointer-events:auto;width:200px;min-height:112px;padding:10px;border-radius:14px;background:var(--bg);color:var(--tx);border:2px solid var(--ac);box-shadow:0 6px 24px rgba(0,0,0,.55);display:flex;flex-direction:column;justify-content:space-between;gap:8px;animation:nin .3s}
.nc .nx{font-size:14px;word-break:break-word}.nc .row{flex-wrap:nowrap;gap:6px}.nc button{padding:5px 6px;font-size:13px;flex:1}
@keyframes nin{from{transform:translateY(-16px);opacity:0}}
.cwrap{display:grid;grid-template-columns:minmax(0,1fr) 290px;gap:14px;align-items:start}@media(max-width:820px){.cwrap{grid-template-columns:1fr}}
#rcm{height:300px;overflow:auto;margin-bottom:8px}
.tiles.pinned{display:flex;flex-wrap:wrap;gap:10px}.tiles.pinned .call{flex:0 1 190px}.tiles.pinned .call.pin{flex:1 1 100%;max-height:72vh}
.call.pin video{object-fit:contain;background:#000}
.call .tl{position:absolute;right:6px;top:50%;transform:translateY(-50%);z-index:6;display:flex;flex-direction:column;gap:4px}
.call .tl button{padding:2px 7px;font-size:14px;border-radius:9px;background:rgba(0,0,0,.6);color:#fff;border-color:rgba(255,255,255,.3)}
@keyframes rbw{0%,100%{border-color:#f33;box-shadow:0 0 16px 2px #f33,inset 0 0 14px #f33}17%{border-color:#fa0;box-shadow:0 0 16px 2px #fa0,inset 0 0 14px #fa0}33%{border-color:#ee2;box-shadow:0 0 16px 2px #ee2,inset 0 0 14px #ee2}50%{border-color:#3e5;box-shadow:0 0 16px 2px #3e5,inset 0 0 14px #3e5}67%{border-color:#3af;box-shadow:0 0 16px 2px #3af,inset 0 0 14px #3af}83%{border-color:#b5f;box-shadow:0 0 16px 2px #b5f,inset 0 0 14px #b5f}}
.call.sp{animation:rbw var(--gs,2s) linear infinite}
</style></head><body><div id="app"></div><div id="nt"></div>''')

# ---------------- render / translation hooks ----------------
rep("$('#app').innerHTML=authView()", "$('#app').innerHTML=tl(authView())")
rep("""$('#app').innerHTML=`<div id="bar">${barHTML()}</div><main>${view()}</main>`;""",
    """$('#app').innerHTML=tl(`<div id="bar">${barHTML()}</div><main${tab=='call'&&room?' style="max-width:1280px"':''}>${view()}</main>`);""")
rep("if(tab=='call'&&room){drawTiles();syncBtns()}", "if(tab=='call'&&room){drawTiles();syncBtns();drawChat()}")
rep("if(U&&S&&b)b.innerHTML=barHTML()", "if(U&&S&&b)b.innerHTML=tl(barHTML())")
rep("esc(netErr||'Подключение к сети…')", "(netErr||'Подключение к сети…')")
rep('<h1 style="color:var(--ac)">PixelCall</h1>', '<h1 style="color:var(--ac)">PixelCall</h1>${langBtns()}')
rep("e.textContent='", "e.textContent=tl('", cnt=src.count("e.textContent='"))
# close the tl( calls opened above: each message ends with '; or ';return
import re
src = re.sub(r"e\.textContent=tl\('([^']*)'", r"e.textContent=tl('\1')", src)
rep("function esc(t){", "function esc0(t){")
rep("d.className='toast';d.textContent=t;", "d.className='toast';d.textContent=tl(t);")

# updF / updChat
repline("function updF(){", "function updF(){if(tab=='friends'){const e=$('#fl');if(e)e.innerHTML=tl(friendLists())}if(tab=='call'&&!room)render()}")
rep("if(t)t.innerHTML=ftabs();if(m){m.innerHTML=msgsHTML();", "if(t)t.innerHTML=tl(ftabs());if(m){m.innerHTML=tl(msgsHTML());")

# 'Войти' / 'Выйти' meaning conflicts
rep("""$('#rm').value)">Войти</button>""", """$('#rm').value)">Присоединиться</button>""", cnt=2)
rep("""<button onclick="joinFrom('${x.inv}')">Войти</button>""", """<button onclick="joinFrom('${x.inv}')">Присоединиться</button>""")

# ---------------- PixelID copy ----------------
rep("<small>PixelID: ${S.id}</small>",
    """<small>PixelID: <b class="cp" onclick="copyId()" title="Нажмите, чтобы скопировать">${S.id}</b></small> <button onclick="copyId()" style="padding:2px 8px">📋 Копировать</button>""")
rep("Ваш PixelID: <b>${S.id}</b>",
    """Ваш PixelID: <b class="cp" onclick="copyId()" title="Нажмите, чтобы скопировать">${S.id}</b> <button onclick="copyId()" style="padding:2px 8px">📋 Копировать</button>""")

# ---------------- theme: font + glow speed ----------------
rep("d.colorScheme=L?'light':'dark'}", r'''d.colorScheme=L?'light':'dark';
const nf=s.font=='normal',SY="system-ui,-apple-system,'Segoe UI',Roboto,Arial,sans-serif";document.documentElement.classList.toggle('nf',nf);
if(nf){d.setProperty('--fb',SY);d.setProperty('--fh',SY);d.setProperty('--fw',700)}else{['--fb','--fh','--fw'].forEach(p=>d.removeProperty(p))}
d.setProperty('--gs',(6/(s.glowSp||3))+'s')}''')

# ---------------- fix(): defaults ----------------
rep("S.unread=S.unread||{}}", "S.unread=S.unread||{};S.tIn=S.tIn||[];S.tAcc=S.tAcc||[];S.camBg=S.camBg||'';S.set=S.set||{};if(S.set.font===undefined)S.set.font='pixel';if(S.set.glowOn===undefined)S.set.glowOn=true;if(S.set.glowSp===undefined)S.set.glowSp=3}")
rep("function afterLogin(){netStart();", "function afterLogin(){netStart();pendNotifs();")

# ---------------- image upload (adds camera background) ----------------
repline("function img(inp,k){", r'''function img(inp,k){const f=inp.files[0];if(!f)return;const r=new FileReader();r.onload=()=>{const im=new Image();im.onload=()=>{const m=k=='av'?256:k=='cam'?640:1280,s=Math.min(1,m/Math.max(im.width,im.height)),c=document.createElement('canvas');c.width=im.width*s;c.height=im.height*s;c.getContext('2d').drawImage(im,0,0,c.width,c.height);const u=c.toDataURL('image/jpeg',k=='cam'?.65:.8);if(k=='av'){S.avimg=u;S.av='img'}else if(k=='cam'){S.camBg=u;bcbg()}else S.bgimg=u;save();render()};im.src=r.result};r.readAsDataURL(f)}''')

# ---------------- inventory / trade offers ----------------
repline("function inv(){", r'''function inv(){return S.inv.length?`<div class="grid">${S.inv.map((it,i)=>`<div class="card g">${svg(it.g,'bob')}<div>${G[it.g].n}</div><b>#${it.n}/50</b>${it.adv?'<br><small>из адвента: только обмен</small>':''}<br>${it.pend?`<small>обмен предложен, ждём ответа</small><br><button onclick="untrade(${i})">Отменить</button>`:`<button onclick="trade(${i})">Предложить обмен</button> ${it.adv?'':`<button onclick="sell(${i})">Продать</button>`}`}</div>`).join('')}</div>`:'<div class="card">Инвентарь пуст</div>'}''')
repline("function trade(i){", r'''function trade(i){if(!S.friends.length){alert('Сначала добавьте друга');return}const n=prompt('Кому? Введите номер:\n'+S.friends.map((f,j)=>`${j+1}. ${fname(f)}`).join('\n'));const f=S.friends[(+n||0)-1];if(!f)return;const it=S.inv[i],tid=rid();it.pend={tid,to:f.id};save();tx(f.id,{t:'trade',tid,g:it.g,n:it.n,adv:!!it.adv});toast('Предложение обмена отправлено: '+fname(f));render()}''')

# ---------------- friends: notifications ----------------
repline("function acceptReq(id){", r'''function acceptReq(id){const r=S.reqIn.find(x=>x.id==id);if(!r)return;closeN('f'+id);makeFriend(id,r);tx(id,Object.assign({t:'facc'},prof()));toast('Теперь вы друзья с '+fname(r))}''')
repline("function declineReq(id){", r'''function declineReq(id){closeN('f'+id);S.reqIn=S.reqIn.filter(r=>r.id!=id);save();tx(id,{t:'frej'});updBar();updF()}''')
rep("💬 Написать</button>", """💬 Написать</button><button onclick="go('call');ring('${f.id}')" ${isOn(f.id)?'':'disabled'}>📞 Позвонить</button>""")
rep("toast('📨 '+(d.nick||id)+' хочет добавить вас в друзья')", "notifReq(id)")
rep("toast('💬 '+fname(fr)+': '+(m.inv?'приглашение в конференцию':m.t.slice(0,60)))",
    "m.inv||notif('m'+id,'💬 '+esc(fname(fr))+': '+esc(m.t.slice(0,60)),()=>{openChat(id);go('chats')},null,9000)")
rep("function flush(id){", "function flush(id){flushT(id);")
rep("case'msg':case'inv':{", r'''case'ring':{if(!fr)break;const c=parseCode(d.code);if(!c)break;notif('r'+id,'📞 '+esc(fname(fr))+' звонит вам',()=>{if(room)leave(true);joinFrom(c)},()=>tx(id,{t:'rdec'}),30000);break}
case'rdec':if(fr)toast(fname(fr)+' отклонил(а) звонок');break;
case'trade':{if(!fr)break;const g=String(d.g),n=+d.n,tid=String(d.tid||'').slice(0,40);if(!G[g]||!(n>=1&&n<=50)||!tid)break;if(S.tAcc.some(x=>x.tid==tid)){tx(id,{t:'tacc',tid});break}
if(!S.tIn.some(x=>x.tid==tid)&&S.tIn.length<30){S.tIn.push({tid,id,g,n,adv:!!d.adv});save()}notifTrade(tid);break}
case'tacc':{const k=S.inv.findIndex(x=>x.pend&&x.pend.tid==d.tid&&x.pend.to==id);if(k>=0){S.inv.splice(k,1);save();toast('🎁 '+fname(fr||{id})+' принял(а) ваш подарок');if(tab=='inv')render()}tx(id,{t:'tack',tid:d.tid});break}
case'tack':S.tAcc=S.tAcc.filter(x=>x.tid!=d.tid);save();break;
case'trej':{const it=S.inv.find(x=>x.pend&&x.pend.tid==d.tid);if(it){it.pend=null;save();toast('Обмен отклонён');if(tab=='inv')render()}break}
case'tcan':S.tIn=S.tIn.filter(x=>!(x.tid==d.tid&&x.id==id));save();closeN('t'+d.tid);break;
case'msg':case'inv':{''')

# ---------------- conference plumbing ----------------
rep("room={code,host,parts:{},stream:null,sharing:null,raw:code.replace('-','')}",
    "room={code,host,parts:{},stream:null,sharing:null,raw:code.replace('-',''),chat:[],an:{},spk:{},pin:null,z:{s:1,x:0,y:0}}")
rep("c.send(Object.assign({t:'hi',mic,cam:camOn||!!R.sharing,gifts:myGifts()},prof()))",
    "c.send(Object.assign({t:'hi',mic,cam:camOn||!!R.sharing,gifts:myGifts(),bg:S.camBg||''},prof()))")
rep("function rdat(c,d){if(!room||!d||typeof d!='object')return;const id=c.peer,p=room.parts[id]=room.parts[id]||{};",
    r'''function rdat(c,d){if(!room||!d||typeof d!='object')return;const id=c.peer,p=room.parts[id]=room.parts[id]||{};
if(d.t=='chat'){if(typeof d.text=='string'){room.chat.push({n:p.nick||'Гость',t:d.text.slice(0,500)});drawChat()}return}
if(d.t=='bg'){p.bg=okImg(d.bg)?d.bg:'';drawTiles();return}''')
rep("p.nick=String(d.nick||'Гость').slice(0,20);", "p.nick=String(d.nick||'Гость').slice(0,20);p.bg=okImg(d.bg)?d.bg:'';")
rep("try{R.rp&&R.rp.destroy()}catch(e){}", "try{R.ac&&R.ac.close()}catch(e){}try{R.rp&&R.rp.destroy()}catch(e){}")
rep("{alert('Конференция не найдена: проверьте код или хост ещё не вошёл');leave()}",
    r'''{if((R.tries=(R.tries||0)+1)>16){alert('Конференция не найдена: проверьте код или хост ещё не вошёл');leave()}else if(!R.rt){R.rt=1;setTimeout(()=>{R.rt=0;if(room!==R)return;const h=RP+R.raw+'-h',q=R.parts[h];if(q&&!q.stream)q.call=null;if(!(q&&q.conn))rdata(h);callTo(h)},1500)}}''')
rep("toast('Приглашение отправлено')}", "tx(id,{t:'ring',code:room.code});toast('Приглашение отправлено')}")

# ---------------- tiles (pin, glow, camera background) ----------------
a = src.index('function tileHTML('); b = src.index('function setBad(')
src = src[:a] + r'''function tileHTML(id,o,local){const R=room,camv=local?(camOn||!!R.sharing):o.cam!==false,micv=local?mic:o.mic!==false,gl=local?myGifts():(o.gifts||[]),pos=['left:6px;top:6px','right:6px;top:6px','left:6px;bottom:6px','right:6px;bottom:6px'],bg=local?S.camBg:o.bg,pn=R.pin==id,sp=R.spk[id]>Date.now()&&S.set.glowOn!==false&&micv;
return `<div class="call ${micv?'':'mo'} ${pn?'pin':''} ${sp?'sp':''}" id="t-${id}" ondblclick="pinT('${id}')"><video autoplay playsinline muted></video><div class="avc" style="display:${camv?'none':'grid'}${okImg(bg)?`;background:#111 url(${bg}) center/cover`:''}"><div class="av">${local?avh(S.av):avh2(o.av,o.im)}</div></div>${gl.map((k,i)=>k?`<div class="cn" style="${pos[i]}">${svg(k,'bob')}</div>`:'').join('')}<div class="bad" style="display:${(local?R.lbad:o.bad)?'block':'none'}">Плохое подключение к интернету</div><div class="nm">${local?esc(U)+' (вы)':(o.nick?esc(o.nick):'Гость')}</div><div class="ic">${micv?'':ICM}${camv?'':ICC}</div><div class="tl"><button title="${pn?'Открепить':'Закрепить экран (двойной клик)'}" onclick="event.stopPropagation();pinT('${id}')">${pn?'📌':'📍'}</button>${pn?`<button onclick="event.stopPropagation();zoomBy(1.25)">➕</button><button onclick="event.stopPropagation();zoomBy(.8)">➖</button><button onclick="event.stopPropagation();zoomBy(0)">⟲</button>`:''}</div></div>`}
function drawTiles(){const t=$('#tiles');if(!t||!room||!room.stream)return;const R=room,ps=Object.entries(R.parts).filter(([k,p])=>p.nick||p.stream);
if(R.pin&&R.pin!='me'&&!ps.some(([k])=>k==R.pin)){R.pin=null;R.z={s:1,x:0,y:0}}
const arr=[['me',{},true]].concat(ps.map(([k,p])=>[k,p,false])).sort((x,y)=>(y[0]==R.pin)-(x[0]==R.pin));
t.className='tiles'+(R.pin?' pinned':'');t.innerHTML=tl(arr.map(([k,p,l])=>tileHTML(k,p,l)).join(''));
const att=(id,st)=>{const v=document.querySelector('#t-'+id+' video');if(v&&st){v.srcObject=st;v.play().catch(()=>{})}};att('me',R.sharing||R.stream);ps.forEach(([k,p])=>att(k,p.stream));applyZoom()}
''' + src[b:]

# ---------------- call tab ----------------
a = src.index('function callV(){'); b = src.index('\nrender();\n</script>')
CALLV = r'''function friendCalls(){return S.friends.length?S.friends.map(f=>`<div class="row" style="margin:6px 0"><div class="av ${isOn(f.id)?'on':''}" style="width:44px;height:44px;font-size:20px;border-width:3px">${avh2(f.av,f.im)}</div><div><b>${esc(fname(f))}</b><br><small>${isOn(f.id)?'в сети':'не в сети'}</small></div><button style="margin-left:auto" onclick="ring('${f.id}')" ${isOn(f.id)?'':'disabled'}>📞 Позвонить</button></div>`).join(''):'<small>Друзей пока нет</small>'}
function callV(){if(!room)return `<div class="card"><h3>Конференция</h3><div class="row"><button onclick="mkRoom()">➕ Создать конференцию</button><input id="rm" placeholder="Код или ссылка"><button onclick="joinFrom($('#rm').value)">Присоединиться</button></div><small>Создайте конференцию и отправьте другу код (или ссылку). Нужен доступ к камере и микрофону — если их нет, можно зайти и без них.</small></div><div class="card"><h3>Позвонить другу</h3>${friendCalls()}</div>`;
const on=S.friends.filter(f=>isOn(f.id));
return `<div class="cwrap"><div class="card"><div class="wrapc"><div class="cc" onclick="copyRoom(this)" title="Нажмите, чтобы скопировать ссылку"><div class="stick"></div><div class="code">${room.code}</div></div><div id="tiles" class="tiles"></div></div>
<div class="row" style="margin-top:10px"><button id="bcam" onclick="togCam()">📷 Камера</button><button id="bmic" onclick="togMic()">🎤 Микрофон</button><button id="bscr" onclick="scr()">🖥 Демонстрация экрана</button><label class="fb">🖼 Фон камеры <input type="file" accept="image/*" hidden onchange="img(this,'cam')"></label>${S.camBg?'<button onclick="rmCamBg()">✖ Убрать фон камеры</button>':''}<button onclick="leave()" style="border-color:#e33;color:#f66">Покинуть</button></div>
<div class="row" style="margin-top:10px">${on.length?`<select id="invf">${on.map(f=>`<option value="${f.id}">${esc(fname(f))}</option>`).join('')}</select><button onclick="invite()">📨 Позвать друга</button>`:'<small>Друзья в сети появятся здесь — их можно позвать в один клик.</small>'}</div>
<small>Наведите на палочку сверху — появится код конференции, клик копирует ссылку.</small><br><small>Двойной клик по окну — закрепить его; колесо мыши или ➕ ➖ — приблизить; перетаскивание — двигать картинку.</small></div>
<div class="card"><h3>Чат</h3><div id="rcm"></div><div class="row"><input id="rci" placeholder="Сообщение" style="flex:1;min-width:0" maxlength="500" onkeydown="if(event.key=='Enter')rsend()"><button onclick="rsend()">Отправить</button></div></div></div>`}
'''

EXTRA = r'''/* ===== ЯЗЫК (RU / EN / UK) ===== */
const SO='\u2060',SC='\u2061';let LANG=store.get('pc_lang','ru');
const esc=t=>SO+esc0(t)+SC;
const D={
'Главная':['Home','Головна'],'Магазин':['Shop','Магазин'],'Инвентарь пуст':['Inventory is empty','Інвентар порожній'],'Инвентарь':['Inventory','Інвентар'],
'Друзья':['Friends','Друзі'],'Чаты':['Chats','Чати'],'Чат':['Chat','Чат'],'Звонок':['Call','Дзвінок'],'Пиксели':['Pixels','Пікселі'],'Настройки':['Settings','Налаштування'],
'Сеть подключена':['Network connected','Мережу підключено'],'Подключение к сети…':['Connecting to network…','Підключення до мережі…'],'Сеть:':['Network:','Мережа:'],
'Адвент-календарь (1–24 декабря)':['Advent calendar (Dec 1–24)','Адвент-календар (1–24 грудня)'],'Адвент-календарь':['Advent calendar','Адвент-календар'],
'Вас пригласили в конференцию':['You were invited to the conference','Вас запросили до конференції'],
'Войдите или зарегистрируйтесь — и вы сразу попадёте в неё':['Sign in or register and you will join it right away','Увійдіть або зареєструйтесь — і ви одразу потрапите до неї'],
'Вход':['Sign in','Вхід'],'Регистрация':['Sign up','Реєстрація'],'Никнейм':['Nickname','Нікнейм'],'Пароль':['Password','Пароль'],'Номер телефона':['Phone number','Номер телефону'],
'Почта / аккаунт / номер для 2FA':['Email / account / number for 2FA','Пошта / акаунт / номер для 2FA'],'День рождения':['Birthday','День народження'],
'Код 2FA (демо: 123456)':['2FA code (demo: 123456)','Код 2FA (демо: 123456)'],'Войти':['Sign in','Увійти'],'Создать аккаунт':['Create account','Створити акаунт'],
'Демо: вход через Google/Facebook/Apple/SMS требует сервера, здесь 2FA имитируется кодом 123456.':['Demo: sign-in via Google/Facebook/Apple/SMS needs a server, so 2FA is simulated with the code 123456.','Демо: вхід через Google/Facebook/Apple/SMS потребує сервера, тут 2FA імітується кодом 123456.'],
'Ник от 3 символов, пароль от 6':['Nickname from 3 characters, password from 6','Нік від 3 символів, пароль від 6'],'Неверный код 2FA':['Wrong 2FA code','Неправильний код 2FA'],
'Ник занят':['Nickname is taken','Нік зайнятий'],'Укажите сервис для 2FA':['Specify a service for 2FA','Вкажіть сервіс для 2FA'],'Неверный ник или пароль':['Wrong nickname or password','Неправильний нік або пароль'],
'Цитата о себе':['A quote about yourself','Цитата про себе'],'Своя картинка':['Your own picture','Власна картинка'],'Встречи':['Meetings','Зустрічі'],'Создать встречу':['Create meeting','Створити зустріч'],
'Код или ссылка':['Code or link','Код або посилання'],'Присоединиться':['Join','Приєднатися'],'Копировать':['Copy','Копіювати'],
'Нажмите, чтобы скопировать ссылку':['Click to copy the link','Натисніть, щоб скопіювати посилання'],'Нажмите, чтобы скопировать':['Click to copy','Натисніть, щоб скопіювати'],
'PixelID скопирован':['PixelID copied','PixelID скопійовано'],
'Санта Клаус 2027':['Santa Claus 2027','Санта Клаус 2027'],'Ёлка 2027':['Christmas tree 2027','Ялинка 2027'],'Снежный шар 2027':['Snow globe 2027','Сніжна куля 2027'],'Замёрзшее окно 2027':['Frozen window 2027','Замерзле вікно 2027'],
'осталось':['left','залишилось'],'Купить':['Buy','Купити'],'Недостаточно пикселей':['Not enough pixels','Недостатньо пікселів'],
'из адвента: только обмен':['from advent: exchange only','з адвенту: лише обмін'],'Предложить обмен':['Offer exchange','Запропонувати обмін'],'Продать':['Sell','Продати'],
'обмен предложен, ждём ответа':['exchange offered, waiting for reply','обмін запропоновано, чекаємо відповіді'],'Отменить':['Cancel','Скасувати'],
'Сначала добавьте друга':['Add a friend first','Спочатку додайте друга'],'Кому? Введите номер:':['To whom? Enter the number:','Кому? Введіть номер:'],
'Предложение обмена отправлено:':['Exchange offer sent:','Пропозицію обміну надіслано:'],'предлагает вам обмен подарком:':['offers you a gift exchange:','пропонує вам обмін подарунком:'],
'Подарок получен:':['Gift received:','Подарунок отримано:'],'принял(а) ваш подарок':['accepted your gift','прийняв(ла) ваш подарунок'],'Обмен отклонён':['Exchange declined','Обмін відхилено'],
'Входящие запросы':['Incoming requests','Вхідні запити'],'Исходящие запросы':['Outgoing requests','Вихідні запити'],'Друзей пока нет':['No friends yet','Друзів поки немає'],
'хочет добавить вас в друзья':['wants to add you as a friend','хоче додати вас у друзі'],'✔ Принять':['✔ Accept','✔ Прийняти'],'✖ Отклонить':['✖ Decline','✖ Відхилити'],
'запрос отправлен, ждём ответа':['request sent, waiting for reply','запит надіслано, чекаємо відповіді'],'не в сети':['offline','не в мережі'],'в сети':['online','у мережі'],
'💬 Написать':['💬 Message','💬 Написати'],'Удалить из друзей?':['Remove from friends?','Видалити з друзів?'],'Удалить':['Remove','Видалити'],
'Ваш PixelID:':['Your PixelID:','Ваш PixelID:'],'— отправьте его другу, чтобы он мог добавить вас':['— send it to a friend so they can add you','— надішліть його другу, щоб він міг додати вас'],
'PixelID друга (10 цифр)':['Friend’s PixelID (10 digits)','PixelID друга (10 цифр)'],'Добавить в друзья':['Add friend','Додати в друзі'],
'Запросы и сообщения доходят, когда оба открыли PixelCall (иначе ждут, пока друг зайдёт).':['Requests and messages are delivered when both of you have PixelCall open (otherwise they wait until your friend comes online).','Запити й повідомлення доходять, коли обидва відкрили PixelCall (інакше чекають, поки друг зайде).'],
'Неверный ID или запрос уже отправлен':['Invalid ID or request already sent','Неправильний ID або запит уже надіслано'],
'Теперь вы друзья с':['You are now friends with','Тепер ви друзі з'],'Теперь вы друзья!':['You are now friends!','Тепер ви друзі!'],'принял(а) ваш запрос':['accepted your request','прийняв(ла) ваш запит'],
'Запрос в друзья отклонён':['Friend request declined','Запит у друзі відхилено'],
'Добавьте друзей, чтобы писать':['Add friends to start chatting','Додайте друзів, щоб писати'],'Сообщение':['Message','Повідомлення'],'Отправить':['Send','Надіслати'],
'Сообщений пока нет':['No messages yet','Повідомлень поки немає'],'Приглашение в конференцию':['Conference invitation','Запрошення до конференції'],
'Донат':['Donate','Донат'],'Картой':['By card','Карткою'],'Конвертер':['Converter','Конвертер'],'Демо-оплата:':['Demo payment:','Демо-оплата:'],'банковскую карту':['bank card','банківську картку'],
'Демо: настоящая оплата PayPal и картой подключается через платёжный сервис на сервере. Здесь начисление имитируется, а выдать себе пиксели просто так нельзя.':['Demo: real PayPal and card payments need a payment service on a server. Here the top-up is simulated, and you cannot give yourself pixels for free.','Демо: справжня оплата PayPal і карткою підключається через платіжний сервіс на сервері. Тут нарахування імітується, а видати собі пікселі просто так не можна.'],
'Имя':['Name','Ім’я'],'Сохранить имя':['Save name','Зберегти ім’я'],'Новым ником нужно будет входить в аккаунт':['You will need the new nickname to sign in','Новим ніком потрібно буде входити в акаунт'],
'От 3 до 20 символов':['3 to 20 characters','Від 3 до 20 символів'],'Тема':['Theme','Тема'],'Чёрная':['Black','Чорна'],'Белая':['White','Біла'],'Радужная':['Rainbow','Райдужна'],'Цветная':['Colored','Кольорова'],
'Со своим фоном подсветка отключена':['Glow is off with a custom background','З власним фоном підсвітку вимкнено'],'Цвет и яркость':['Color and brightness','Колір і яскравість'],'Цвет':['Color','Колір'],'Яркость':['Brightness','Яскравість'],
'Фон при выключенной камере':['Background when camera is off','Фон при вимкненій камері'],'Фон камеры':['Camera background','Фон камери'],'Убрать фон камеры':['Remove camera background','Прибрати фон камери'],'Фон':['Background','Фон'],'Убрать фон':['Remove background','Прибрати фон'],
'Показывать тортик':['Show birthday cake','Показувати торт'],'Подарки по углам камеры':['Gifts in camera corners','Подарунки по кутах камери'],'Угол':['Corner','Кут'],'Не ставить':['None','Не ставити'],
'Ставятся только те подарки, которые у вас есть.':['Only gifts you own are placed.','Ставляться лише ті подарунки, які у вас є.'],'Выйти':['Log out','Вийти'],
'Язык / Language':['Language','Мова'],'Шрифт':['Font','Шрифт'],'Пиксельный':['Pixel','Піксельний'],'Обычный':['Normal','Звичайний'],
'Подсветка при разговоре':['Glow while speaking','Підсвітка під час розмови'],'Радужная подсветка, когда человек говорит':['Rainbow glow when a person speaks','Райдужна підсвітка, коли людина говорить'],'Скорость':['Speed','Швидкість'],
'Подсветка видна только вам, скорость настраивается для вас.':['The glow setting applies only to your own view.','Налаштування підсвітки діє лише для вашого перегляду.'],
'Картинку видят все в конференции, пока ваша камера выключена. Менять её можете только вы.':['Everyone in the conference sees this picture while your camera is off. Only you can change it.','Цю картинку бачать усі в конференції, поки ваша камера вимкнена. Змінювати її можете лише ви.'],
'Адвент-календарь (1–24 декабря)  ':['',''],
'Пробная версия (без ограничений по датам)':['Trial mode (no date limits)','Пробна версія (без обмежень за датами)'],'Забрать':['Claim','Забрати'],
'Ячейка раз в 24 часа. Награду можно забрать позже. Подарки из адвента нельзя продать, только обменять.':['One cell every 24 hours. You can claim the reward later. Advent gifts cannot be sold, only exchanged.','Комірка раз на 24 години. Нагороду можна забрати пізніше. Подарунки з адвенту не можна продати, лише обміняти.'],
'Все 50 экземпляров разобраны: вместо подарка 875 px':['All 50 copies are taken: 875 px instead of the gift','Усі 50 екземплярів розібрано: замість подарунка 875 px'],
'Этот аккаунт уже открыт в другой вкладке':['This account is already open in another tab','Цей акаунт уже відкрито в іншій вкладці'],'Не удалось подключиться к сети':['Could not connect to the network','Не вдалося підключитися до мережі'],
'звонит вам':['is calling you','телефонує вам'],'отклонил(а) звонок':['declined the call','відхилив(ла) дзвінок'],'Звоним:':['Calling:','Дзвонимо:'],'Позвонить другу':['Call a friend','Подзвонити другу'],'Позвонить':['Call','Подзвонити'],
'Приглашение отправлено':['Invitation sent','Запрошення надіслано'],'Ссылка на конференцию скопирована':['Conference link copied','Посилання на конференцію скопійовано'],
'Неверный код конференции':['Invalid conference code','Неправильний код конференції'],'Вы уже в конференции':['You are already in a conference','Ви вже в конференції'],
'Конференция не найдена: проверьте код или хост ещё не вошёл':['Conference not found: check the code, or the host has not joined yet','Конференцію не знайдено: перевірте код або хост ще не зайшов'],
'Камера не найдена или нет доступа':['Camera not found or no access','Камеру не знайдено або немає доступу'],'Демонстрация экрана недоступна':['Screen sharing is unavailable','Демонстрація екрана недоступна'],
'вышел(а)':['left','вийшов(ла)'],'Гость':['Guest','Гість'],'(вы)':['(you)','(ви)'],'Плохое подключение к интернету':['Poor internet connection','Погане підключення до інтернету'],
'Создать конференцию':['Create conference','Створити конференцію'],'Конференция':['Conference','Конференція'],
'Создайте конференцию и отправьте другу код (или ссылку). Нужен доступ к камере и микрофону — если их нет, можно зайти и без них.':['Create a conference and send your friend the code (or link). Camera and microphone access is needed — without them you can still join.','Створіть конференцію й надішліть другу код (або посилання). Потрібен доступ до камери й мікрофона — якщо їх немає, можна зайти і без них.'],
'Камера':['Camera','Камера'],'Микрофон':['Microphone','Мікрофон'],'Демонстрация экрана':['Screen sharing','Демонстрація екрана'],'Покинуть':['Leave','Покинути'],'Позвать друга':['Invite friend','Покликати друга'],
'Друзья в сети появятся здесь — их можно позвать в один клик.':['Online friends will appear here — invite them in one click.','Друзі в мережі з’являться тут — їх можна покликати одним кліком.'],
'Наведите на палочку сверху — появится код конференции, клик копирует ссылку.':['Hover the bar at the top to see the conference code; click copies the link.','Наведіть на паличку зверху — з’явиться код конференції, клік копіює посилання.'],
'Двойной клик по окну — закрепить его; колесо мыши или ➕ ➖ — приблизить; перетаскивание — двигать картинку.':['Double-click a tile to pin it; mouse wheel or ➕ ➖ to zoom; drag to move the picture.','Подвійний клік по вікну — закріпити його; колесо миші або ➕ ➖ — наблизити; перетягування — рухати картинку.'],
'Закрепить экран (двойной клик)':['Pin screen (double-click)','Закріпити екран (подвійний клік)'],'Открепить':['Unpin','Відкріпити']
};
delete D['Адвент-календарь (1–24 декабря)  '];
const DR=new RegExp(Object.keys(D).sort((a,b)=>b.length-a.length).map(k=>k.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')).join('|'),'g');
function tl(s){s=String(s);if(LANG=='ru')return s.replace(/[\u2060\u2061]/g,'');const i=LANG=='en'?0:1;return s.split(/(\u2060[\s\S]*?\u2061)/).map((x,j)=>j%2?x.slice(1,-1):x.replace(DR,m=>D[m][i])).join('')}
{const A=window.alert.bind(window),C=window.confirm.bind(window),P=window.prompt.bind(window);window.alert=m=>A(tl(m));window.confirm=m=>C(tl(m));window.prompt=(m,d)=>P(tl(m),d)}
function setLang(k){LANG=k;store.set('pc_lang',k);render()}
function langBtns(){return `<div class="row" style="margin-bottom:10px">${[['ru','Русский'],['en','English'],['uk','Українська']].map(([k,n])=>`<button class="${LANG==k?'on':''}" onclick="setLang('${k}')">${n}</button>`).join('')}</div>`}
function extraSet(){const s=S.set;return `<div class="card"><h3>Язык / Language</h3>${langBtns()}</div>
<div class="card"><h3>Шрифт</h3><div class="row"><button class="${s.font!='normal'?'on':''}" onclick="S.set.font='pixel';save();render()">Пиксельный</button><button class="${s.font=='normal'?'on':''}" onclick="S.set.font='normal';save();render()">Обычный</button></div></div>
<div class="card"><h3>Подсветка при разговоре</h3><label><input type="checkbox" ${s.glowOn!==false?'checked':''} onchange="S.set.glowOn=this.checked;save();render()"> Радужная подсветка, когда человек говорит</label><br><br><label>Скорость <input type="range" min="1" max="10" step="1" value="${s.glowSp}" ${s.glowOn===false?'disabled':''} oninput="S.set.glowSp=+this.value;applyTheme()" onchange="save()"></label><br><small>Подсветка видна только вам, скорость настраивается для вас.</small></div>
<div class="card"><h3>Фон при выключенной камере</h3><div class="row">${okImg(S.camBg)?`<img src="${S.camBg}" alt="" style="height:60px;border-radius:8px">`:''}<label class="fb">Своя картинка <input type="file" accept="image/*" hidden onchange="img(this,'cam')"></label><button onclick="rmCamBg()">Убрать фон</button></div><small>Картинку видят все в конференции, пока ваша камера выключена. Менять её можете только вы.</small></div>`}
rep_placeholder
/* ===== ПРОВЕРКА КАРТИНКИ, КОПИРОВАНИЕ ID ===== */
const okImg=s=>typeof s=='string'&&s.length<400000&&/^data:image\/jpeg;base64,[A-Za-z0-9+\/=]+$/.test(s);
function copyId(){copyTxt(S.id).then(()=>toast('PixelID скопирован'))}
function bcbg(){if(room)Object.values(room.parts).forEach(p=>{try{p.conn&&p.conn.open&&p.conn.send({t:'bg',bg:S.camBg||''})}catch(e){}})}
function rmCamBg(){S.camBg='';save();bcbg();render()}
/* ===== УВЕДОМЛЕНИЯ СВЕРХУ (принять / отклонить) ===== */
function closeN(k){const nt=$('#nt');if(!nt)return;const e=[...nt.children].find(x=>x.dataset.k==k);if(e){clearTimeout(e._t);e.remove()}}
function notif(k,html,ok,no,ttl){const nt=$('#nt');if(!nt)return;closeN(k);const e=document.createElement('div');e.className='nc';e.dataset.k=k;
e.innerHTML=tl('<div class="nx">'+html+'</div><div class="row"><button class="y">✔ Принять</button><button class="n">✖ Отклонить</button></div>');
e.querySelector('.y').onclick=()=>{closeN(k);ok&&ok()};e.querySelector('.n').onclick=()=>{closeN(k);no&&no()};
if(ttl)e._t=setTimeout(()=>{closeN(k);if(k[0]=='r'&&no)no()},ttl);nt.appendChild(e)}
function notifReq(id){const r=S.reqIn.find(x=>x.id==id);if(!r)return;notif('f'+id,'📨 '+esc(fname(r))+' хочет добавить вас в друзья',()=>acceptReq(id),()=>declineReq(id))}
function notifTrade(tid){const r=S.tIn.find(x=>x.tid==tid);if(!r)return;const f=S.friends.find(x=>x.id==r.id)||{id:r.id};notif('t'+tid,'🎁 '+esc(fname(f))+' предлагает вам обмен подарком: '+G[r.g].n+' #'+r.n,()=>acceptTrade(tid),()=>declineTrade(tid))}
function pendNotifs(){S.reqIn.forEach(r=>notifReq(r.id));S.tIn.forEach(x=>notifTrade(x.tid))}
/* ===== ОБМЕН ПОДАРКАМИ ===== */
function acceptTrade(tid){const r=S.tIn.find(x=>x.tid==tid);if(!r)return;S.inv.push({g:r.g,n:r.n,adv:r.adv});S.tIn=S.tIn.filter(x=>x.tid!=tid);S.tAcc.push({tid,id:r.id});save();tx(r.id,{t:'tacc',tid});toast('🎁 Подарок получен: '+G[r.g].n);if(tab=='inv')render()}
function declineTrade(tid){const r=S.tIn.find(x=>x.tid==tid);if(!r)return;S.tIn=S.tIn.filter(x=>x.tid!=tid);save();tx(r.id,{t:'trej',tid})}
function untrade(i){const it=S.inv[i];if(!it||!it.pend)return;tx(it.pend.to,{t:'tcan',tid:it.pend.tid});it.pend=null;save();render()}
function flushT(id){S.inv.filter(x=>x.pend&&x.pend.to==id).forEach(x=>tx(id,{t:'trade',tid:x.pend.tid,g:x.g,n:x.n,adv:!!x.adv}));S.tAcc.filter(x=>x.id==id).forEach(x=>tx(id,{t:'tacc',tid:x.tid}))}
/* ===== ЗВОНОК ДРУГУ ===== */
function ring(id){const f=S.friends.find(x=>x.id==id);if(!f)return;let c;if(room)c=room.code;else{c=rc();joinRoom(c,true)}tx(id,{t:'ring',code:c});toast('Звоним: '+fname(f))}
/* ===== ЧАТ В КОНФЕРЕНЦИИ ===== */
function drawChat(){const m=$('#rcm');if(!m||!room)return;m.innerHTML=tl(room.chat.length?room.chat.map(x=>`<div class="msg ${x.me?'me':''}">${x.me?'':`<b>${esc(x.n)}</b><br>`}${esc(x.t)}</div>`).join(''):'<small>Сообщений пока нет</small>');m.scrollTop=m.scrollHeight}
function rsend(){const i=$('#rci');if(!i||!room)return;const t=i.value.trim().slice(0,500);if(!t)return;room.chat.push({me:1,t});i.value='';drawChat();Object.values(room.parts).forEach(p=>{try{p.conn&&p.conn.open&&p.conn.send({t:'chat',text:t})}catch(e){}})}
/* ===== ЗАКРЕПИТЬ И ПРИБЛИЗИТЬ ЭКРАН ===== */
function pinT(id){const R=room;if(!R)return;R.pin=R.pin==id?null:id;R.z={s:1,x:0,y:0};drawTiles()}
function clampZ(){const R=room,e=R&&document.getElementById('t-'+R.pin);if(!e)return;const z=R.z,mx=(z.s-1)*e.clientWidth/2,my=(z.s-1)*e.clientHeight/2;z.x=Math.max(-mx,Math.min(mx,z.x));z.y=Math.max(-my,Math.min(my,z.y))}
function applyZoom(){const R=room;if(!R||!R.pin)return;const e=document.getElementById('t-'+R.pin),v=e&&e.querySelector('video');if(!v)return;const z=R.z;v.style.transform=`translate(${z.x}px,${z.y}px) scale(${z.s})`;v.style.touchAction=z.s>1?'none':'auto';v.style.cursor=z.s>1?'grab':''}
function zoomBy(f){const R=room;if(!R||!R.pin)return;const z=R.z;z.s=f?Math.min(5,Math.max(1,z.s*f)):1;if(z.s==1){z.x=0;z.y=0}clampZ();applyZoom()}
document.addEventListener('wheel',e=>{const t=e.target.closest&&e.target.closest('.call.pin');if(!t||!room)return;e.preventDefault();zoomBy(e.deltaY<0?1.15:1/1.15)},{passive:false});
let pdrag=null;
document.addEventListener('pointerdown',e=>{const t=e.target.closest&&e.target.closest('.call.pin');if(t&&room&&room.z.s>1&&!e.target.closest('button'))pdrag={x:e.clientX,y:e.clientY,zx:room.z.x,zy:room.z.y}});
document.addEventListener('pointermove',e=>{if(!pdrag||!room)return;room.z.x=pdrag.zx+e.clientX-pdrag.x;room.z.y=pdrag.zy+e.clientY-pdrag.y;clampZ();applyZoom()});
addEventListener('pointerup',()=>{pdrag=null});
/* ===== РАДУЖНАЯ ПОДСВЕТКА ГОВОРЯЩЕГО ===== */
function lvl(R,id,st){if(!st||!st.getAudioTracks().length)return 0;let a=R.an[id];if(!a||a.st!==st){try{R.ac=R.ac||new(window.AudioContext||window.webkitAudioContext)();const an=R.ac.createAnalyser();an.fftSize=512;R.ac.createMediaStreamSource(new MediaStream(st.getAudioTracks())).connect(an);a=R.an[id]={st,an,buf:new Uint8Array(512)}}catch(e){return 0}}
a.an.getByteTimeDomainData(a.buf);let m=0;for(let i=0;i<512;i++)m=Math.max(m,Math.abs(a.buf[i]-128));return m/128}
function speakTick(){const R=room;if(!R||!R.stream||!S)return;if(R.ac&&R.ac.state=='suspended')R.ac.resume().catch(()=>{});const on=S.set.glowOn!==false;
const chk=(id,st,en)=>{if(en&&lvl(R,id,st)>.05)R.spk[id]=Date.now()+400;const sp=on&&en&&R.spk[id]>Date.now(),e=document.getElementById('t-'+id);if(e)e.classList.toggle('sp',!!sp)};
chk('me',R.stream,mic);Object.entries(R.parts).forEach(([k,p])=>{if(p.stream)chk(k,p.stream,p.mic!==false)})}
setInterval(speakTick,150);'''
EXTRA = EXTRA.replace('rep_placeholder\n', '')
src = src[:a] + CALLV + EXTRA + src[b:]

# settings page: add new cards before the logout button
rep('\n<button onclick="logout()">Выйти</button>`}', '\n${extraSet()}<button onclick="logout()">Выйти</button>`}')

open('/mnt/user-data/outputs/pixelcall.py', 'w', encoding='utf-8').write(src)
print('ok', len(src))

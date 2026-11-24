import re
P='/home/claude/app/index.html'
s=open(P,encoding='utf-8').read()

def rep(old,new,cnt=1):
    global s
    assert old in s, 'MISSING: '+old[:70]
    s=s.replace(old,new,cnt)
def cut(start,end,new):
    global s
    i=s.index(start); j=s.index(end,i)
    s=s[:i]+new+s[j:]

# ---------- CSS ----------
CSS=r"""
.idc{user-select:all;cursor:pointer;color:var(--ac)}.cp{padding:3px 8px;font-size:13px}
label.btn{background:var(--gl);border:1px solid var(--bd);border-radius:12px;padding:8px 14px;cursor:pointer;display:inline-block}
#pops{position:fixed;top:calc(8px + env(safe-area-inset-top,0px));left:50%;transform:translateX(-50%);z-index:60;display:flex;gap:8px;flex-wrap:wrap;justify-content:center;max-width:96vw;pointer-events:none}
.pop{pointer-events:auto;width:210px;background:var(--bg);color:var(--tx);border:1px solid var(--bd);border-radius:12px;padding:10px;font-size:14px;box-shadow:0 6px 22px rgba(0,0,0,.55);animation:pdn .3s}.pop .row{margin-top:8px;gap:6px}.pop button{padding:5px 10px;font-size:13px}@keyframes pdn{from{transform:translateY(-14px);opacity:0}}
.rwrap{display:flex;gap:12px;flex-wrap:wrap}.rmain{flex:1 1 520px;min-width:0}
.rchat{flex:1 1 240px;max-width:100%;flex-direction:column;border:1px solid var(--bd);border-radius:12px;padding:8px;min-height:280px}#rmsgs{flex:1;overflow:auto;max-height:55vh;margin-bottom:8px}
.call .tb{position:absolute;right:6px;top:50%;transform:translateY(-50%);z-index:5;display:flex;flex-direction:column;gap:4px;opacity:0;transition:opacity .2s}.call:hover .tb,.call.pin .tb{opacity:1}@media(hover:none){.call .tb{opacity:1}}
.call .tb button{padding:2px 8px;font-size:14px;background:rgba(0,0,0,.6);color:#fff;border-color:rgba(255,255,255,.3)}
.tiles.pinned{display:flex;flex-direction:column}.tiles.pinned .call.pin{aspect-ratio:auto;height:min(62vh,560px);cursor:grab;touch-action:none}.call.pin video,.call.shr video{object-fit:contain}
.thumbs{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:8px}.thumbs .call{font-size:12px}
.call video{transform-origin:center center}
@keyframes rbw{0%,100%{border-color:#f33;box-shadow:0 0 16px 3px #f33,inset 0 0 14px #f336}17%{border-color:#fc2;box-shadow:0 0 16px 3px #fc2,inset 0 0 14px #fc26}33%{border-color:#3e5;box-shadow:0 0 16px 3px #3e5,inset 0 0 14px #3e56}50%{border-color:#2df;box-shadow:0 0 16px 3px #2df,inset 0 0 14px #2df6}67%{border-color:#36f;box-shadow:0 0 16px 3px #36f,inset 0 0 14px #36f6}83%{border-color:#d3f;box-shadow:0 0 16px 3px #d3f,inset 0 0 14px #d3f6}}
.call.sp:not(.mo){animation:rbw var(--rbs,1.8s) linear infinite}
body.plain,body.plain *{font-family:system-ui,-apple-system,'Segoe UI',Roboto,Arial,sans-serif!important;letter-spacing:0!important}
body.plain h1{font-size:26px}body.plain h3{font-size:17px}body.plain #bar .logo{font-size:18px}body.plain .cc .code{font-size:15px}
"""
rep('</style></head>', CSS+'</style></head>')
rep('<div id="app"></div>','<div id="app"></div><div id="pops"></div>')

# ---------- theme / fix / img / render ----------
rep("d.colorScheme=L?'light':'dark'}", "d.colorScheme=L?'light':'dark';d.setProperty('--rbs',({slow:'4s',mid:'1.8s',fast:'.8s'})[s.rb]||'1.8s');document.body.classList.toggle('plain',!!store.get('pc_plain',false))}")
rep("S.unread=S.unread||{}}", "S.unread=S.unread||{};S.set=S.set||{bri:1,hue:270,theme:'black',bday:true,corners:['santa','tree','ball','snow']};S.set.rb=S.set.rb||'mid';S.out=S.out||[];S.tin=S.tin||[];S.tseen=S.tseen||[];S.camBg=S.camBg||''}")
rep("const m=k=='av'?256:1280,", "const m=k=='av'?256:k=='cam'?640:1280,")
rep("if(k=='av'){S.avimg=u;S.av='img'}else S.bgimg=u;save();render()", "if(k=='av'){S.avimg=u;S.av='img'}else if(k=='cam'){S.camBg=u}else S.bgimg=u;save();render();if(k=='cam')bcBg()")
rep("if(tab=='call'&&room){drawTiles();syncBtns()}", "if(tab=='call'&&room){drawTiles();syncBtns();updRoomChat()}")
rep("<br><small>PixelID: ${S.id}</small>", "<br><small>PixelID: ${idBox()}</small>")
rep("Ваш PixelID: <b>${S.id}</b>", "Ваш PixelID: ${idBox()}")
rep("<button onclick=\"logout()\">Выйти</button>", "${extra()}<button onclick=\"logout()\">Выйти</button>")

# ---------- trade -> настоящие подарки ----------
cut("function trade(i){","const fname=",r"""function trade(i){if(!S.friends.length){alert('Сначала добавьте друга');return}const n=prompt('Кому? Введите номер:\n'+S.friends.map((f,j)=>`${j+1}. ${fname(f)} (${f.id})`).join('\n'));const f=S.friends[(+n||0)-1],it=S.inv[i];if(!f||!it)return;
const o={ts:cleanId(rid()),to:f.id,g:it.g,n:it.n,adv:!!it.adv};S.inv.splice(i,1);S.out.push(o);save();tx(f.id,{t:'trade',ts:o.ts,g:o.g,n:o.n,adv:o.adv});toast('Предложение обмена отправлено '+fname(f));render()}
""")

# ---------- friendLists ----------
cut("function friendLists(){","function friends(){",r"""function friendLists(){const card=(o,on,body)=>`<div class="card row"><div class="av ${on?'on':''}">${avh2(o.av,o.im)}</div><div><b>${esc(fname(o))}</b><br><small>${o.id}</small>${body[0]||''}</div><div class="row" style="margin-left:auto">${body[1]||''}</div></div>`;
const inc=S.reqIn.map(r=>card(r,0,['<br><small>хочет добавить вас в друзья</small>',`<button onclick="acceptReq('${r.id}')">✔ Принять</button><button onclick="declineReq('${r.id}')">✖ Отклонить</button>`])).join('');
const out=S.reqOut.map(r=>card(r,0,['<br><small>запрос отправлен, ждём ответа</small>',`<button onclick="cancelReq('${r.id}')">Отменить</button>`])).join('');
const nm=id=>fname(S.friends.find(q=>q.id==id)||{id});
const tin=S.tin.map(x=>`<div class="card row"><div style="width:56px">${svg(x.g,'bob')}</div><div><b>${esc(nm(x.from))}</b> <small>предлагает подарок:</small><br>${G[x.g].n} #${x.n}</div><div class="row" style="margin-left:auto"><button onclick="tAcc('${x.ts}')">✔ Принять</button><button onclick="tRej('${x.ts}')">✖ Отклонить</button></div></div>`).join('');
const tout=S.out.map(o=>`<div class="card row"><div style="width:56px">${svg(o.g,'')}</div><div><b>${esc(nm(o.to))}</b><br><small>${G[o.g].n} #${o.n} — ждёт ответа</small></div><button style="margin-left:auto" onclick="cancelOut('${o.ts}')">Отменить</button></div>`).join('');
const fr=S.friends.map(f=>card(f,isOn(f.id),[`<br><small>${isOn(f.id)?'в сети':'не в сети'}</small>`,`<button onclick="callFriend('${f.id}')" ${isOn(f.id)?'':'disabled'}>📞 Позвонить</button><button onclick="openChat('${f.id}');go('chats')">💬 Написать</button><button onclick="delF('${f.id}')">Удалить</button>`])).join('');
return (inc?'<h3>Входящие запросы</h3>'+inc:'')+(tin?'<h3>Предложения подарков</h3>'+tin:'')+(out?'<h3>Исходящие запросы</h3>'+out:'')+(tout?'<h3>Исходящие подарки</h3>'+tout:'')+'<h3>Друзья</h3>'+(fr||'<div class="card">Друзей пока нет</div>')}
""")
rep("function acceptReq(id){","function acceptReq(id){closePop('fr'+id);")
rep("function declineReq(id){","function declineReq(id){closePop('fr'+id);")
rep("function openChat(id){","function openChat(id){closePop('m'+id);")

# ---------- сеть: новые сообщения ----------
rep("function flush(id){","function flush(id){S.out.filter(o=>o.to==id).forEach(o=>tx(id,{t:'trade',ts:o.ts,g:o.g,n:o.n,adv:o.adv}));")
rep("save();toast('📨 '+(d.nick||id)+' хочет добавить вас в друзья')}", "save();pop('fr'+id,'📨 '+pf().nick+' ('+id+') хочет добавить вас в друзья',[['✔ Принять',`acceptReq('${id}')`],['✖ Отклонить',`declineReq('${id}')`]])}")
rep("toast('💬 '+fname(fr)+': '+(m.inv?'приглашение в конференцию':m.t.slice(0,60)))", "pop('m'+id,'💬 '+fname(fr)+': '+(m.inv?'приглашение в конференцию':m.t.slice(0,60)),[m.inv?['Войти',`joinFrom('${m.inv}');closePop('m${id}')`]:['Открыть',`openChat('${id}');go('chats')`],['✖',`closePop('m${id}')`]],9000)")
rep("case'ack':", r"""case'trade':{if(!fr||!GK.includes(d.g)||!Number.isInteger(d.n)||d.n<1||d.n>50)break;const ts=cleanId(d.ts);if(!ts)break;if(S.tseen.includes(ts)){tx(id,{t:'tacc',ts});break}if(S.tseen.includes('r:'+ts)){tx(id,{t:'trej',ts});break}if(S.tin.some(x=>x.ts==ts))break;
S.tin.push({ts,from:id,g:d.g,n:d.n,adv:!!d.adv});save();updF();pop('t'+ts,'🎁 '+fname(fr)+' предлагает подарок: '+G[d.g].n+' #'+d.n,[['✔ Принять',`tAcc('${ts}')`],['✖ Отклонить',`tRej('${ts}')`]]);break}
case'tacc':{const o=S.out.find(x=>x.ts==cleanId(d.ts)&&x.to==id);if(o){S.out=S.out.filter(x=>x!==o);save();updF();toast('🎁 '+fname(fr||{id})+' принял(а) подарок')}break}
case'trej':{const o=S.out.find(x=>x.ts==cleanId(d.ts)&&x.to==id);if(o){S.out=S.out.filter(x=>x!==o);S.inv.push({g:o.g,n:o.n,adv:o.adv});save();updF();toast(fname(fr||{id})+' отклонил(а) подарок, он вернулся в инвентарь');if(tab=='inv')render()}break}
case'tcan':{const ts=cleanId(d.ts);S.tin=S.tin.filter(x=>!(x.ts==ts&&x.from==id));save();closePop('t'+ts);updF();break}
case'call':{if(!fr)break;const c=parseCode(d.code);if(!c)break;pop('c'+id,'📞 Входящий звонок: '+fname(fr),[['✔ Принять',`acceptCall('${id}','${c}')`],['✖ Отклонить',`declineCall('${id}')`]],30000);break}
case'cdec':toast(fname(fr||{id})+' отклонил(а) звонок');break;
case'ccan':closePop('c'+id);break;
case'ack':""")

# ---------- блок новых функций (до конференций) ----------
NEW=r"""/* ===== ВСПЛЫВАШКИ, КОПИРОВАНИЕ, ПОДАРКИ, ЗВОНКИ ===== */
const cleanId=x=>String(x||'').replace(/[^\w-]/g,'').slice(0,40);
function idBox(){return `<b class="idc" onclick="copyId()" title="Нажмите, чтобы скопировать">${S.id}</b> <button class="cp" onclick="copyId()">📋 Копировать</button>`}
function copyId(){copyTxt(S.id).then(()=>toast('PixelID скопирован'))}
const POPS={};let ringT=null;
function pop(k,text,btns,ttl){closePop(k);const d=document.createElement('div');d.className='pop';d.id='pop-'+k;d.innerHTML=`<div>${esc(text)}</div><div class="row">${btns.map(([l,f])=>`<button onclick="${f}">${l}</button>`).join('')}</div>`;$('#pops').appendChild(d);if(ttl)POPS[k]=setTimeout(()=>closePop(k),ttl);if(k[0]=='c')ringStart()}
function closePop(k){const e=document.getElementById('pop-'+k);if(e)e.remove();clearTimeout(POPS[k]);delete POPS[k];if(!document.querySelector('[id^="pop-c"]'))ringStop()}
function beep(){try{AC=AC||new (window.AudioContext||window.webkitAudioContext)();AC.resume();const o=AC.createOscillator(),g=AC.createGain();o.frequency.value=660;g.gain.value=.08;o.connect(g);g.connect(AC.destination);o.start();o.stop(AC.currentTime+.25)}catch(e){}}
function ringStart(){if(ringT)return;beep();ringT=setInterval(beep,1600)}function ringStop(){clearInterval(ringT);ringT=null}
function tAcc(ts){const x=S.tin.find(q=>q.ts==ts);if(!x)return;S.tin=S.tin.filter(q=>q!==x);S.inv.push({g:x.g,n:x.n,adv:x.adv});S.tseen.push(ts);S.tseen=S.tseen.slice(-300);save();tx(x.from,{t:'tacc',ts});closePop('t'+ts);updF();toast('🎁 Подарок получен');if(tab=='inv')render()}
function tRej(ts){const x=S.tin.find(q=>q.ts==ts);if(!x)return;S.tin=S.tin.filter(q=>q!==x);S.tseen.push('r:'+ts);S.tseen=S.tseen.slice(-300);save();tx(x.from,{t:'trej',ts});closePop('t'+ts);updF()}
function cancelOut(ts){const o=S.out.find(x=>x.ts==ts);if(!o)return;S.out=S.out.filter(x=>x!==o);S.inv.push({g:o.g,n:o.n,adv:o.adv});save();tx(o.to,{t:'tcan',ts});render()}
function sendCall(id){if(room)tx(id,{t:'call',code:room.code,ts:rid()})}
function callFriend(id){if(!isOn(id)){toast('Друг не в сети');return}if(!room)mkRoom();tab='call';render();room.ring[id]=1;if(room.rp&&room.rp.open)sendCall(id);else room.pend.push(id);toast('Звоним: '+fname(S.friends.find(f=>f.id==id)||{id}))}
function acceptCall(id,code){closePop('c'+id);if(room)leave(true);tab='call';render();joinRoom(code,false)}
function declineCall(id){closePop('c'+id);tx(id,{t:'cdec'})}
function extra(){const s=S.set,pl=store.get('pc_plain',false);
return `<div class="card"><h3>Язык</h3><div class="row">${[['ru','Русский'],['en','English'],['uk','Українська']].map(([k,n])=>`<button class="${LANG==k?'on':''}" onclick="setLang('${k}')">${n}</button>`).join('')}</div></div>
<div class="card"><h3>Шрифт</h3><div class="row"><button class="${pl?'':'on'}" onclick="setPlain(false)">Пиксельный</button><button class="${pl?'on':''}" onclick="setPlain(true)">Обычный</button></div></div>
<div class="card"><h3>Подсветка говорящего</h3><div class="row">${[['off','Выкл'],['slow','Медленно'],['mid','Средне'],['fast','Быстро']].map(([k,n])=>`<button class="${s.rb==k?'on':''}" onclick="S.set.rb='${k}';save();applyTheme();render()">${n}</button>`).join('')}</div><small>Радужная подсветка вокруг того, кто сейчас говорит.</small></div>
<div class="card"><h3>Фон при выключенной камере</h3><div class="row"><label class="btn">🖼 Фон камеры<input type="file" accept="image/*" hidden onchange="img(this,'cam')"></label>${S.camBg?'<button onclick="delCamBg()">Убрать</button>':''}</div><small>Показывается другим, когда камера выключена. Меняете его только вы и только для себя.</small></div>
<div class="card"><h3>PixelID</h3>${idBox()}</div>`}
function setLang(l){LANG=l;store.set('pc_lang',l);document.documentElement.lang=l;render()}
function setPlain(v){store.set('pc_plain',v);applyTheme();render()}
function bcBg(){if(!room)return;const m={t:'bg',bg:S.camBg||''};Object.values(room.parts).forEach(p=>{try{p.conn&&p.conn.open&&p.conn.send(m)}catch(e){}});drawTiles()}
function delCamBg(){S.camBg='';save();bcBg();render()}

/* ===== ЯЗЫКИ (ru / en / uk) ===== */
let LANG=store.get('pc_lang',(navigator.language||'').slice(0,2)=='uk'?'uk':'ru');
const I18=[
['Санта Клаус 2027','Santa Claus 2027','Санта Клаус 2027'],['Ёлка 2027','Christmas Tree 2027','Ялинка 2027'],['Снежный шар 2027','Snow Globe 2027','Сніжна куля 2027'],['Замёрзшее окно 2027','Frozen Window 2027','Замерзле вікно 2027'],
['Главная','Home','Головна'],['Магазин','Shop','Магазин'],['Инвентарь пуст','Inventory is empty','Інвентар порожній'],['Инвентарь','Inventory','Інвентар'],['Друзья в сети появятся здесь — их можно позвать в один клик.','Online friends will appear here — you can call them in one click.','Друзі в мережі з’являться тут — їх можна покликати одним кліком.'],['Друзья','Friends','Друзі'],['Чаты','Chats','Чати'],['Чат','Chat','Чат'],['Звонок','Call','Дзвінок'],['Пиксели','Pixels','Пікселі'],['Настройки','Settings','Налаштування'],
['Адвент-календарь (1–24 декабря)','Advent calendar (December 1–24)','Адвент-календар (1–24 грудня)'],['Адвент-календарь','Advent calendar','Адвент-календар'],
['Сеть подключена','Network connected','Мережу підключено'],['Подключение к сети…','Connecting to network…','Підключення до мережі…'],['Этот аккаунт уже открыт в другой вкладке','This account is already open in another tab','Цей акаунт уже відкрито в іншій вкладці'],['Сеть: ','Network: ','Мережа: '],
['Вас пригласили в конференцию','You were invited to the conference','Вас запросили до конференції'],['Войдите или зарегистрируйтесь — и вы сразу попадёте в неё.','Sign in or sign up and you will join it right away.','Увійдіть або зареєструйтесь — і ви одразу потрапите до неї.'],
['Вход','Sign in','Вхід'],['Регистрация','Sign up','Реєстрація'],['Никнейм','Nickname','Нікнейм'],['Пароль','Password','Пароль'],['Номер телефона','Phone number','Номер телефону'],['Почта / аккаунт / номер для 2FA','Email / account / number for 2FA','Пошта / акаунт / номер для 2FA'],['День рождения','Birthday','День народження'],['Код 2FA (демо: 123456)','2FA code (demo: 123456)','Код 2FA (демо: 123456)'],['Создать аккаунт','Create account','Створити акаунт'],
['Демо: вход через Google/Facebook/Apple/SMS требует сервера, здесь 2FA имитируется кодом 123456.','Demo: sign-in via Google/Facebook/Apple/SMS needs a server, here 2FA is simulated with code 123456.','Демо: вхід через Google/Facebook/Apple/SMS потребує сервера, тут 2FA імітується кодом 123456.'],
['Ник от 3 символов, пароль от 6','Nickname from 3 characters, password from 6','Нік від 3 символів, пароль від 6'],['Неверный код 2FA','Wrong 2FA code','Невірний код 2FA'],['Ник занят','Nickname is taken','Нік зайнятий'],['Укажите сервис для 2FA','Specify the 2FA service','Вкажіть сервіс для 2FA'],['Неверный ник или пароль','Wrong nickname or password','Невірний нік або пароль'],
['Цитата о себе','A quote about you','Цитата про себе'],['Своя картинка','Your own picture','Власна картинка'],['Встречи','Meetings','Зустрічі'],['Создать встречу','Create meeting','Створити зустріч'],['Код или ссылка','Code or link','Код або посилання'],['Войти','Enter','Увійти'],
['осталось','left','залишилось'],['Купить','Buy','Купити'],['Недостаточно пикселей','Not enough pixels','Недостатньо пікселів'],
['из адвента: только обмен','from advent: trade only','з адвенту: лише обмін'],['Предложить обмен','Offer a trade','Запропонувати обмін'],['Продать','Sell','Продати'],['Сначала добавьте друга','Add a friend first','Спочатку додайте друга'],['Кому? Введите номер:','To whom? Enter the number:','Кому? Введіть номер:'],['Предложение обмена отправлено','Trade offer sent to','Пропозицію обміну надіслано'],
['хочет добавить вас в друзья','wants to add you as a friend','хоче додати вас у друзі'],['Принять','Accept','Прийняти'],['Отклонить','Decline','Відхилити'],['запрос отправлен, ждём ответа','request sent, waiting for a reply','запит надіслано, чекаємо відповіді'],['Отменить','Cancel','Скасувати'],['не в сети','offline','не в мережі'],['в сети','online','в мережі'],
['Написать','Message','Написати'],['Удалить из друзей?','Remove from friends?','Видалити з друзів?'],['Удалить','Remove','Видалити'],['Входящие запросы','Incoming requests','Вхідні запити'],['Исходящие запросы','Outgoing requests','Вихідні запити'],['Друзей пока нет','No friends yet','Друзів поки немає'],
['Ваш PixelID:','Your PixelID:','Ваш PixelID:'],['— отправьте его другу, чтобы он мог добавить вас','— send it to a friend so they can add you','— надішліть його другу, щоб він міг додати вас'],['PixelID друга (10 цифр)','Friend’s PixelID (10 digits)','PixelID друга (10 цифр)'],['Добавить в друзья','Add friend','Додати в друзі'],
['Запросы и сообщения доходят, когда оба открыли PixelCall (иначе ждут, пока друг зайдёт).','Requests and messages are delivered when both have PixelCall open (otherwise they wait until your friend comes online).','Запити та повідомлення доходять, коли обоє відкрили PixelCall (інакше чекають, поки друг зайде).'],
['Неверный ID или запрос уже отправлен','Invalid ID or request already sent','Невірний ID або запит уже надіслано'],['Теперь вы друзья с','You are now friends with','Тепер ви друзі з'],['Теперь вы друзья!','You are now friends!','Тепер ви друзі!'],['принял(а) ваш запрос','accepted your request','прийняв(ла) ваш запит'],['Запрос в друзья отклонён','Friend request declined','Запит у друзі відхилено'],
['Приглашение в конференцию','Conference invitation','Запрошення до конференції'],['приглашение в конференцию','conference invitation','запрошення до конференції'],['Сообщений пока нет','No messages yet','Повідомлень поки немає'],['Добавьте друзей, чтобы писать','Add friends to chat','Додайте друзів, щоб писати'],['Сообщение','Message','Повідомлення'],['Отправить','Send','Надіслати'],
['Донат','Donate','Донат'],['банковскую карту','bank card','банківську картку'],['Картой','By card','Карткою'],['Демо: настоящая оплата PayPal и картой подключается через платёжный сервис на сервере. Здесь начисление имитируется, а выдать себе пиксели просто так нельзя.','Demo: real PayPal and card payments are connected through a payment service on a server. Here crediting is simulated, and you cannot just give yourself pixels.','Демо: справжня оплата PayPal і карткою підключається через платіжний сервіс на сервері. Тут нарахування імітується, а видати собі пікселі просто так не можна.'],['Конвертер','Converter','Конвертер'],['Демо-оплата','Demo payment','Демо-оплата'],
['От 3 до 20 символов','3 to 20 characters','Від 3 до 20 символів'],['Сохранить имя','Save name','Зберегти ім’я'],['Новым ником нужно будет входить в аккаунт','You will need to sign in with the new nickname','Новим ніком потрібно буде входити в акаунт'],['Имя','Name','Ім’я'],['Тема','Theme','Тема'],['Чёрная','Black','Чорна'],['Белая','White','Біла'],['Радужная','Rainbow','Райдужна'],['Цветная','Colored','Кольорова'],['Со своим фоном подсветка отключена','Highlight is off with a custom background','З власним фоном підсвітку вимкнено'],
['Цвет и яркость','Color and brightness','Колір і яскравість'],['Цвет','Color','Колір'],['Яркость','Brightness','Яскравість'],['Убрать фон','Remove background','Прибрати фон'],['Фон при выключенной камере','Background when camera is off','Фон при вимкненій камері'],['Фон камеры','Camera background','Фон камери'],['Фон','Background','Фон'],['Показывать тортик','Show birthday cake','Показувати тортик'],['Подарки по углам камеры','Gifts in camera corners','Подарунки по кутах камери'],['Угол','Corner','Кут'],['Не ставить','Don’t place','Не ставити'],['Ставятся только те подарки, которые у вас есть.','Only gifts you own are placed.','Ставляться лише ті подарунки, які у вас є.'],['Выйти','Log out','Вийти'],
['Пробная версия (без ограничений по датам)','Trial version (no date limits)','Пробна версія (без обмежень за датами)'],['Забрать','Claim','Забрати'],['Ячейка раз в 24 часа. Награду можно забрать позже. Подарки из адвента нельзя продать, только обменять.','One cell every 24 hours. You can claim the reward later. Advent gifts cannot be sold, only traded.','Комірка раз на 24 години. Нагороду можна забрати пізніше. Подарунки з адвенту не можна продати, лише обміняти.'],['Все 50 экземпляров разобраны: вместо подарка','All 50 copies are taken: instead of the gift','Усі 50 екземплярів розібрано: замість подарунка'],
['Ссылка на конференцию скопирована','Conference link copied','Посилання на конференцію скопійовано'],['Неверный код конференции','Invalid conference code','Невірний код конференції'],['Вы уже в конференции','You are already in a conference','Ви вже в конференції'],['Не удалось подключиться к сети','Could not connect to the network','Не вдалося підключитися до мережі'],['Конференция не найдена: проверьте код или хост ещё не вошёл','Conference not found: check the code or the host has not joined yet','Конференцію не знайдено: перевірте код або господар ще не зайшов'],
['Гость','Guest','Гість'],['вышел(а)','left','вийшов(ла)'],['Камера не найдена или нет доступа','Camera not found or no access','Камеру не знайдено або немає доступу'],['Демонстрация экрана недоступна','Screen sharing is unavailable','Демонстрація екрана недоступна'],['Демонстрация экрана','Share screen','Демонстрація екрана'],['Приглашение отправлено','Invitation sent','Запрошення надіслано'],
['Плохое подключение к интернету','Poor internet connection','Погане підключення до інтернету'],[' (вы)',' (you)',' (ви)'],['Создать конференцию','Create conference','Створити конференцію'],['Конференция','Conference','Конференція'],
['Создайте конференцию и отправьте другу код (или ссылку). Нужен доступ к камере и микрофону — если их нет, можно зайти и без них.','Create a conference and send your friend the code (or link). Camera and microphone access is needed — if you have none, you can still join without them.','Створіть конференцію та надішліть другу код (або посилання). Потрібен доступ до камери та мікрофона — якщо їх немає, можна зайти і без них.'],
['Нажмите, чтобы скопировать ссылку','Click to copy the link','Натисніть, щоб скопіювати посилання'],['Нажмите, чтобы скопировать','Click to copy','Натисніть, щоб скопіювати'],['Камера','Camera','Камера'],['Микрофон','Microphone','Мікрофон'],
['Наведите на палочку сверху — появится код конференции, клик копирует ссылку.','Hover the bar at the top — the conference code appears, click copies the link.','Наведіть на паличку зверху — з’явиться код конференції, клік копіює посилання.'],
['Копировать','Copy','Копіювати'],['PixelID скопирован','PixelID copied','PixelID скопійовано'],['Открыть','Open','Відкрити'],['предлагает подарок:','offers a gift:','пропонує подарунок:'],['Предложения подарков','Gift offers','Пропозиції подарунків'],['Исходящие подарки','Outgoing gifts','Вихідні подарунки'],['ждёт ответа','waiting for a reply','чекає відповіді'],['принял(а) подарок','accepted the gift','прийняв(ла) подарунок'],['отклонил(а) подарок, он вернулся в инвентарь','declined the gift, it returned to your inventory','відхилив(ла) подарунок, він повернувся до інвентаря'],['Подарок получен','Gift received','Подарунок отримано'],
['Позвонить другу','Call a friend','Подзвонити другу'],['Позвонить','Call','Подзвонити'],['Входящий звонок:','Incoming call:','Вхідний дзвінок:'],['Друг не в сети','Friend is offline','Друг не в мережі'],['Звоним:','Calling:','Дзвонимо:'],['отклонил(а) звонок','declined the call','відхилив(ла) дзвінок'],['Добавьте друзей, чтобы им звонить','Add friends to call them','Додайте друзів, щоб їм дзвонити'],['Покинуть','Leave','Покинути'],['Ссылкой в чат','Link to chat','Посиланням у чат'],
['Закрепить / открепить','Pin / unpin','Закріпити / відкріпити'],['Приблизить','Zoom in','Наблизити'],['Отдалить','Zoom out','Віддалити'],['Сбросить масштаб','Reset zoom','Скинути масштаб'],['Убрать','Remove','Прибрати'],
['Показывается другим, когда камера выключена. Меняете его только вы и только для себя.','Shown to others when your camera is off. Only you can change it, and only for yourself.','Показується іншим, коли камеру вимкнено. Змінювати його можете лише ви і лише для себе.'],
['Язык','Language','Мова'],['Шрифт','Font','Шрифт'],['Пиксельный','Pixel','Піксельний'],['Обычный','Normal','Звичайний'],['Подсветка говорящего','Speaking highlight','Підсвітка того, хто говорить'],['Выкл','Off','Вимк.'],['Медленно','Slow','Повільно'],['Средне','Medium','Середньо'],['Быстро','Fast','Швидко'],['Радужная подсветка вокруг того, кто сейчас говорит.','A rainbow glow around whoever is speaking right now.','Райдужна підсвітка навколо того, хто зараз говорить.']
];
let I_RE=null,I_MAP=null;
function i18nBuild(){I_MAP={};I18.forEach(r=>{I_MAP[r[0]]=r});I_RE=new RegExp(I18.map(r=>r[0]).sort((a,b)=>b.length-a.length).map(k=>k.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')).join('|'),'g')}
function tr(x){if(LANG=='ru'||!x)return x;if(!I_RE)i18nBuild();return x.replace(I_RE,m=>{const r=I_MAP[m];return r?r[LANG=='en'?1:2]:m})}
function trNode(n){if(LANG=='ru')return;if(n.nodeType==3){const v=tr(n.nodeValue);if(v!==n.nodeValue)n.nodeValue=v}else if(n.nodeType==1){if(n.tagName=='SCRIPT'||n.tagName=='STYLE')return;['placeholder','title'].forEach(a=>{if(n.hasAttribute(a)){const o=n.getAttribute(a),v=tr(o);if(v!==o)n.setAttribute(a,v)}});n.childNodes.forEach(trNode)}}
function startI18n(){document.documentElement.lang=LANG;new MutationObserver(ms=>{if(LANG=='ru')return;for(const m of ms){if(m.type=='childList')m.addedNodes.forEach(trNode);else trNode(m.target)}}).observe(document.body,{childList:true,subtree:true,characterData:true,attributes:true,attributeFilter:['placeholder','title']})}
{const _a=window.alert.bind(window),_c=window.confirm.bind(window),_p=window.prompt.bind(window);window.alert=m=>_a(tr(String(m)));window.confirm=m=>_c(tr(String(m)));window.prompt=(m,d)=>_p(tr(String(m)),d)}

"""
rep("/* ===== КОНФЕРЕНЦИИ ===== */", NEW+"/* ===== КОНФЕРЕНЦИИ ===== */")
rep("render();\nif('serviceWorker'","startI18n();render();\nif('serviceWorker'")

# afterLogin: показать накопленные запросы
rep("function afterLogin(){netStart();", "function afterLogin(){netStart();S.reqIn.slice(0,3).forEach(r=>pop('fr'+r.id,'📨 '+(r.nick||r.id)+' ('+r.id+') хочет добавить вас в друзья',[['✔ Принять',`acceptReq('${r.id}')`],['✖ Отклонить',`declineReq('${r.id}')`]]));S.tin.slice(0,3).forEach(x=>pop('t'+x.ts,'🎁 '+fname(S.friends.find(f=>f.id==x.from)||{id:x.from})+' предлагает подарок: '+G[x.g].n+' #'+x.n,[['✔ Принять',`tAcc('${x.ts}')`],['✖ Отклонить',`tRej('${x.ts}')`]]));")

# ---------- joinRoom ----------
cut("async function joinRoom(","function rdata(",r"""async function joinRoom(code,host){if(room)return;try{AC=AC||new (window.AudioContext||window.webkitAudioContext)();AC.resume()}catch(e){}
room={code,host,parts:{},stream:null,sharing:null,raw:code.replace('-',''),msgs:[],chatOpen:false,unread:0,pin:null,zm:{},ring:{},pend:[],tries:0,lastMe:0};const R=room;render();
const s=await media();if(room!==R){s.getTracks().forEach(t=>t.stop());return}R.stream=s;mic=s.getAudioTracks().length>0;camOn=!s.noCam;R.lvl=lvlNode(s);
const pid=RP+R.raw+'-'+(host?'h':Math.random().toString(36).slice(2,8));R.pid=pid;let rp;try{rp=new Peer(pid)}catch(e){alert('Не удалось подключиться к сети');leave();return}R.rp=rp;
rp.on('open',()=>{if(room!==R)return;if(!host)connectHost();R.pend.splice(0).forEach(i=>sendCall(i));drawTiles();syncBtns()});
rp.on('connection',c=>rwire(c));
rp.on('call',call=>{if(room!==R)return;call.answer(R.stream);callWire(call)});
rp.on('error',e=>{if(room!==R)return;if(e.type=='unavailable-id'&&host){leave(true);mkRoom()}else if(e.type=='peer-unavailable'&&/-h\b/.test(e.message||'')&&!host){if(++R.tries<5)setTimeout(()=>{if(room===R)connectHost()},1500);else{alert('Конференция не найдена: проверьте код или хост ещё не вошёл');leave()}}})}
function connectHost(){const h=RP+room.raw+'-h';delete room.parts[h];rdata(h);callTo(h)}
let AC=null;
function lvlNode(st){try{if(!st||!st.getAudioTracks().length)return null;AC=AC||new (window.AudioContext||window.webkitAudioContext)();const an=AC.createAnalyser();an.fftSize=512;AC.createMediaStreamSource(st).connect(an);return {an,b:new Uint8Array(512)}}catch(e){return null}}
function loud(n){if(!n)return false;n.an.getByteTimeDomainData(n.b);let m=0;for(let i=0;i<n.b.length;i++){const v=Math.abs(n.b[i]-128);if(v>m)m=v}return m>9}
setInterval(()=>{if(!room||!S)return;const on=S.set.rb!='off',now=Date.now(),f=(id,v)=>{const e=document.getElementById('t-'+id);if(e)e.classList.toggle('sp',on&&v)};
if(mic&&loud(room.lvl))room.lastMe=now;f('me',now-room.lastMe<400);
for(const [id,p] of Object.entries(room.parts)){if(p.lvl===undefined&&p.stream)p.lvl=lvlNode(p.stream);if(p.mic!==false&&loud(p.lvl))p.last=now;f(id,now-(p.last||0)<400)}},150);
""")
# AC уже объявлен ниже в блоке; убрать дубль ниже не нужно (let AC один раз)

# ---------- rwire / rdat ----------
cut("function rwire(c){","function callWire(",r"""function rwire(c){const R=room;c.on('open',()=>{if(room!==R)return;const p=R.parts[c.peer]=R.parts[c.peer]||{};p.conn=c;c.send(Object.assign({t:'hi',mic,cam:camOn||!!R.sharing,gifts:myGifts(),bg:S.camBg||''},prof()))});
c.on('data',d=>rdat(c,d));c.on('close',()=>dropPart(c.peer));c.on('error',()=>{})}
const bgok=x=>typeof x=='string'&&x.length<350000&&/^data:image\/(jpeg|png|webp);base64,[A-Za-z0-9+\/=]+$/.test(x)?x:'';
function rdat(c,d){if(!room||!d||typeof d!='object')return;const id=c.peer,p=room.parts[id]=room.parts[id]||{};
if(d.t=='hi'||d.t=='st'){if(d.t=='hi'){p.nick=String(d.nick||'Гость').slice(0,20);p.av=typeof d.av=='string'?d.av.slice(0,8):'🙂';p.im=typeof d.im=='string'&&d.im.length<400000?d.im:null;p.bg=bgok(d.bg)}
p.mic=d.mic!==false;p.cam=d.cam!==false;p.gifts=Array.isArray(d.gifts)?d.gifts.slice(0,4).map(k=>GK.includes(k)?k:null):[];
if(d.t=='hi'&&room.host)c.send({t:'list',ids:Object.keys(room.parts).filter(k=>k!=id&&room.parts[k].conn&&room.parts[k].conn.open)});drawTiles()}
else if(d.t=='bg'){p.bg=bgok(d.bg);drawTiles()}
else if(d.t=='rm'&&typeof d.text=='string'){room.msgs.push({nick:p.nick||'Гость',t:d.text.slice(0,1000)});if(!room.chatOpen){room.unread++;toast('💬 '+(p.nick||'Гость')+': '+d.text.slice(0,40))}updRoomChat()}
else if(d.t=='list'&&!room.listed){room.listed=1;(Array.isArray(d.ids)?d.ids:[]).slice(0,12).forEach(i=>{if(typeof i=='string'&&i.startsWith(RP+room.raw+'-')&&i!=room.pid){if(!(room.parts[i]&&room.parts[i].conn))rdata(i);callTo(i)}})}}
""")

# ---------- leave / invite ----------
cut("function leave(silent){","function syncBtns(){",r"""function leave(silent){if(!room)return;const R=room;Object.keys(R.ring||{}).forEach(i=>tx(i,{t:'ccan'}));try{stopScr()}catch(e){}Object.values(R.parts).forEach(p=>{try{p.conn&&p.conn.close()}catch(e){}try{p.call&&p.call.close()}catch(e){}});try{R.rp&&R.rp.destroy()}catch(e){}R.stream&&R.stream.getTracks().forEach(t=>t.stop());document.querySelectorAll('audio.ra').forEach(a=>a.remove());room=null;if(!silent)render()}
function invite(){const s=$('#invf');if(!s||!s.value)return;const id=s.value,m={me:1,inv:room.code,ts:rid(),ok:0};(S.chats[id]=S.chats[id]||[]).push(m);save();tx(id,{t:'inv',code:m.inv,ts:m.ts});toast('Приглашение отправлено')}
function sendRoom(){const i=$('#rmi'),t=i.value.trim().slice(0,1000);if(!t||!room)return;room.msgs.push({me:1,nick:U,t});i.value='';updRoomChat();Object.values(room.parts).forEach(p=>{try{p.conn&&p.conn.open&&p.conn.send({t:'rm',text:t})}catch(e){}})}
function updRoomChat(){if(!room)return;const m=$('#rmsgs');if(m){m.innerHTML=room.msgs.map(x=>`<div class="msg ${x.me?'me':''}"><small>${esc(x.nick)}</small><br>${esc(x.t)}</div>`).join('')||'<small>Сообщений пока нет</small>';m.scrollTop=m.scrollHeight}const b=$('#bchat');if(b)b.innerHTML='💬 Чат'+(room.unread?`<span class="badge">${room.unread}</span>`:'')}
function toggleChat(){room.chatOpen=!room.chatOpen;if(room.chatOpen)room.unread=0;render()}
function pinTile(id){room.pin=room.pin==id?null:id;drawTiles()}
function zoomT(id,f){const z=room.zm[id]=room.zm[id]||{s:1,x:0,y:0};if(f==0){z.s=1}else z.s=Math.min(5,Math.max(1,z.s*f));if(z.s==1){z.x=0;z.y=0}applyZoom(id)}
function applyZoom(id){const z=room&&room.zm[id],v=document.querySelector('#t-'+id+' video');if(!z||!v)return;const c=v.parentElement,mx=c.clientWidth*(z.s-1)/2,my=c.clientHeight*(z.s-1)/2;z.x=Math.max(-mx,Math.min(mx,z.x));z.y=Math.max(-my,Math.min(my,z.y));v.style.transform=z.s==1?'':`translate(${z.x}px,${z.y}px) scale(${z.s})`}
function tilesEv(t){if(t._ev)return;t._ev=1;let dr=null;
t.addEventListener('wheel',e=>{const c=e.target.closest('.call.pin');if(!c)return;e.preventDefault();zoomT(c.id.slice(2),e.deltaY<0?1.15:.87)},{passive:false});
t.addEventListener('pointerdown',e=>{const c=e.target.closest('.call.pin');if(!c||e.target.closest('button'))return;const z=room&&room.zm[c.id.slice(2)];if(!z||z.s<=1)return;dr={id:c.id.slice(2),x:e.clientX,y:e.clientY};try{c.setPointerCapture(e.pointerId)}catch(x){}});
t.addEventListener('pointermove',e=>{if(!dr||!room)return;const z=room.zm[dr.id];z.x+=e.clientX-dr.x;z.y+=e.clientY-dr.y;dr.x=e.clientX;dr.y=e.clientY;applyZoom(dr.id)});
t.addEventListener('pointerup',()=>{dr=null});t.addEventListener('pointercancel',()=>{dr=null})}
""")

# ---------- tiles ----------
cut("function tileHTML(","function setBad(",r"""function tileHTML(id,o,local){const camv=local?(camOn||!!room.sharing):o.cam!==false,micv=local?mic:o.mic!==false,gl=local?myGifts():(o.gifts||[]),pos=['left:6px;top:6px','right:6px;top:6px','left:6px;bottom:6px','right:6px;bottom:6px'],pin=room.pin==id,bg=local?bgok(S.camBg):(o.bg||''),sp=micv&&S.set.rb!='off'&&Date.now()-((local?room.lastMe:o.last)||0)<400;
const tb=`<div class="tb"><button onclick="pinTile('${id}')" title="Закрепить / открепить">${pin?'📌✖':'📌'}</button>${pin?`<button onclick="zoomT('${id}',1.25)" title="Приблизить">＋</button><button onclick="zoomT('${id}',.8)" title="Отдалить">－</button><button onclick="zoomT('${id}',0)" title="Сбросить масштаб">⟲</button>`:''}</div>`;
return `<div class="call ${micv?'':'mo'} ${sp?'sp':''} ${pin?'pin':''} ${local&&room.sharing?'shr':''}" id="t-${id}"><video autoplay playsinline muted></video><div class="avc" style="display:${camv?'none':'grid'}${bg?`;background:#111 url('${bg}') center/cover`:''}"><div class="av">${local?avh(S.av):avh2(o.av,o.im)}</div></div>${gl.map((k,i)=>k?`<div class="cn" style="${pos[i]}">${svg(k,'bob')}</div>`:'').join('')}${tb}<div class="bad" style="display:${(local?room.lbad:o.bad)?'block':'none'}">Плохое подключение к интернету</div><div class="nm">${esc(local?U+' (вы)':(o.nick||'Гость'))}</div><div class="ic">${micv?'':ICM}${camv?'':ICC}</div></div>`}
function drawTiles(){const t=$('#tiles');if(!t||!room||!room.stream)return;const ps=Object.entries(room.parts).filter(([k,p])=>p.nick||p.stream),all=[['me',{},true],...ps.map(([k,p])=>[k,p,false])];
let pin=room.pin;if(pin&&!all.some(a=>a[0]==pin))pin=room.pin=null;t.className='tiles'+(pin?' pinned':'');const h=a=>tileHTML(a[0],a[1],a[2]);
t.innerHTML=pin?h(all.find(a=>a[0]==pin))+'<div class="thumbs">'+all.filter(a=>a[0]!=pin).map(h).join('')+'</div>':all.map(h).join('');
const att=(id,st)=>{const v=document.querySelector('#t-'+id+' video');if(v&&st){v.srcObject=st;v.play().catch(()=>{})}};att('me',room.sharing||room.stream);ps.forEach(([k,p])=>att(k,p.stream));all.forEach(a=>applyZoom(a[0]));tilesEv(t)}
""")

# ---------- callV ----------
cut("function callV(){","startI18n();render();",r"""function callV(){const fl=S.friends.map(f=>`<div class="row" style="margin:4px 0"><span style="color:${isOn(f.id)?'#3ddc84':'#777'}">●</span> ${esc(fname(f))}<button style="margin-left:auto" onclick="callFriend('${f.id}')" ${isOn(f.id)?'':'disabled'}>📞 Позвонить</button></div>`).join('')||'<small>Добавьте друзей, чтобы им звонить</small>';
if(!room)return `<div class="card"><h3>Конференция</h3><div class="row"><button onclick="mkRoom()">➕ Создать конференцию</button><input id="rm" placeholder="Код или ссылка"><button onclick="joinFrom($('#rm').value)">Войти</button></div><small>Создайте конференцию и отправьте другу код (или ссылку). Нужен доступ к камере и микрофону — если их нет, можно зайти и без них.</small></div><div class="card"><h3>Позвонить другу</h3>${fl}</div>`;
const on=S.friends.filter(f=>isOn(f.id));
return `<div class="card"><div class="rwrap"><div class="rmain"><div class="wrapc"><div class="cc" onclick="copyRoom(this)" title="Нажмите, чтобы скопировать ссылку"><div class="stick"></div><div class="code">${room.code}</div></div><div id="tiles" class="tiles"></div></div>
<div class="row" style="margin-top:10px"><button id="bcam" onclick="togCam()">📷 Камера</button><button id="bmic" onclick="togMic()">🎤 Микрофон</button><button id="bscr" onclick="scr()">🖥 Демонстрация экрана</button><label class="btn">🖼 Фон камеры<input type="file" accept="image/*" hidden onchange="img(this,'cam')"></label>${S.camBg?'<button onclick="delCamBg()">Убрать</button>':''}<button id="bchat" onclick="toggleChat()">💬 Чат${room.unread?`<span class="badge">${room.unread}</span>`:''}</button><button onclick="leave()" style="border-color:#e33;color:#f66">Покинуть</button></div>
<div class="row" style="margin-top:10px">${on.length?`<select id="invf">${on.map(f=>`<option value="${f.id}">${esc(fname(f))}</option>`).join('')}</select><button onclick="callFriend($('#invf').value)">📞 Позвонить</button><button onclick="invite()">✉ Ссылкой в чат</button>`:'<small>Друзья в сети появятся здесь — их можно позвать в один клик.</small>'}</div>
<small>Наведите на палочку сверху — появится код конференции, клик копирует ссылку.</small></div>
<div class="rchat" style="display:${room.chatOpen?'flex':'none'}"><div id="rmsgs"></div><div class="row"><input id="rmi" placeholder="Сообщение" style="flex:1;min-width:0" onkeydown="if(event.key=='Enter')sendRoom()"><button onclick="sendRoom()">➤</button></div></div></div></div>`}
""")

s=s.replace("\nlet AC=null;\nfunction lvlNode","\nfunction lvlNode") if s.count('let AC=null;')>1 else s
open(P,'w',encoding='utf-8').write(s)
open('/home/claude/app/sw.js','w').write(open('/home/claude/app/sw.js').read().replace("pixelcall-v1","pixelcall-v2"))
print('patched',len(s))

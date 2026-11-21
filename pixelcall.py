"""PixelCall для Streamlit.
Локально:  pip install streamlit  ->  streamlit run pixelcall.py"""
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="PixelCall", page_icon="🎁", layout="wide",
                   initial_sidebar_state="collapsed")

st.markdown(
    """<style>
    #MainMenu, header, footer {visibility: hidden; height: 0;}
    .block-container {padding: 0 !important; max-width: 100% !important;}
    iframe {border: 0; width: 100%;}
    </style>""",
    unsafe_allow_html=True,
)

PAGE = r"""<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover"><title>PixelCall</title><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Pixelify+Sans:wght@400;600&family=Press+Start+2P&display=swap">
<style>
:root{--h:270;--b:1;--fb:'Pixelify Sans','Courier New',monospace;--fh:'Press Start 2P','Courier New',monospace;--ac:hsl(var(--h) 90% 65%);--bg:#050505;--tx:#f1eeff;--gl:rgba(255,255,255,.06);--bd:rgba(255,255,255,.18);color-scheme:dark;box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}
*{box-sizing:border-box}html{scroll-padding-top:env(safe-area-inset-top,0px)}
body{margin:0;background:var(--bg);color:var(--tx);font:16px var(--fb);min-height:100vh;filter:brightness(var(--b))}
body::after{content:"";position:fixed;inset:0;z-index:-2;background:var(--bgimg,none) center/cover;opacity:.6}
body::before{content:"";position:fixed;inset:0;z-index:-1;pointer-events:none;background:var(--light,none)}
.av svg,.av img{width:100%;height:100%;border-radius:50%;object-fit:cover}.pk{width:44px;height:44px;padding:2px;border-radius:50%}.pk svg{width:100%;height:100%;border-radius:50%}
button,input,select{font:inherit;color:inherit}
button{background:var(--gl);border:1px solid var(--bd);border-radius:12px;padding:8px 14px;cursor:pointer;backdrop-filter:blur(6px);transition:transform .12s,background .12s}
button:hover{background:var(--hv,rgba(255,255,255,.14));transform:scale(.96)}button:active{transform:scale(.91)}button.on{border-color:var(--ac);color:var(--ac)}button:disabled{opacity:.4}
input,select{background:var(--gl);border:1px solid var(--bd);border-radius:10px;padding:8px 10px;max-width:100%}option{background:var(--bg)}
#bar{display:flex;gap:8px;align-items:center;padding:10px 14px;position:sticky;top:env(safe-area-inset-top,0px);z-index:5;flex-wrap:wrap;background:var(--bar,rgba(0,0,0,.6));backdrop-filter:blur(10px)}
#bar button.nv{background:none;border:0;border-bottom:2px solid transparent;border-radius:0;backdrop-filter:none;padding:8px 6px}#bar button.nv:hover{background:none;border-bottom-color:var(--ac);text-shadow:0 0 10px var(--ac)}#bar button.nv.on{color:var(--ac);border-bottom-color:var(--ac)}
h1,h3,#bar .logo{font-family:var(--fh);font-weight:400}h3{font-size:13px;line-height:1.5}h1{font-size:22px}#bar .logo{font-size:14px;color:var(--ac);letter-spacing:1px;margin-right:6px}#bar .sp{flex:1}
body.nf h1,body.nf h3,body.nf #bar .logo{font-weight:700}body.nf h3{font-size:16px}body.nf h1{font-size:26px}
#adv{width:38px;height:38px;overflow:hidden;white-space:nowrap;padding:0;display:flex;align-items:center;justify-content:center;transition:width .25s}
#adv:hover{width:150px;transform:none}#adv span{display:none;margin-left:6px}#adv:hover span{display:inline}
main{max-width:980px;margin:auto;padding:16px}
.card{background:var(--gl);border:1px solid var(--bd);border-radius:16px;padding:14px;margin-bottom:14px;backdrop-filter:blur(6px)}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:12px}
.g{text-align:center;position:relative}.g svg{width:96px;height:96px}.px{color:var(--ac);font-weight:700}
.lim{position:absolute;top:8px;left:8px;font-size:10px;line-height:1;padding:3px 7px;border-radius:7px;background:linear-gradient(90deg,#ff5fa2,#ffb020);color:#111;font-weight:700;letter-spacing:.5px;font-family:'Inter',sans-serif}
.gn{font-weight:600;margin:2px 0}
.av{width:64px;height:64px;border-radius:50%;border:4px solid #666;display:grid;place-items:center;font-size:26px;background:var(--gl);position:relative}
.av.on{border-color:#3ddc84}.av i{position:absolute;top:-16px;font-style:normal;font-size:20px}
.row{display:flex;gap:10px;align-items:center;flex-wrap:wrap}.msg{padding:6px 10px;border-radius:10px;margin:4px 0;background:var(--gl);width:fit-content;max-width:85%}.msg.me{margin-left:auto;background:hsl(var(--h) 60% 35%)}.msg small{display:block}
.cell{min-height:100px;display:flex;flex-direction:column;gap:3px;align-items:center;justify-content:center;border-radius:12px;font-weight:700;position:relative;text-align:center;padding:14px 4px 6px}.cell svg{width:52px;height:52px}.cell small{font-size:11px}
.call{position:relative;aspect-ratio:16/9;background:#000;border-radius:16px;overflow:hidden}.call video{width:100%;height:100%;object-fit:cover}
.call .cn{position:absolute;width:20%;max-width:90px}.call .cn svg{width:100%}
.remote{position:absolute;right:8px;bottom:8px;width:28%;aspect-ratio:4/3;background:#222;border-radius:12px;display:grid;place-items:center;font-size:12px;border:2px solid #3ddc84;text-align:center}.remote b{font-size:28px;display:block}
.muted{position:absolute;left:50%;bottom:10px;transform:translateX(-50%);background:#e33;padding:4px 10px;border-radius:20px;font-size:13px}
.tiles{display:grid;grid-template-columns:repeat(auto-fill,minmax(140px,1fr));gap:8px}.tile{aspect-ratio:4/3;background:#111;border-radius:12px;display:grid;place-items:center;text-align:center;border:2px solid #3ddc84;font-size:13px;color:#eee;overflow:hidden;position:relative}.tile b{font-size:30px;display:block}.tile video{width:100%;height:100%;object-fit:cover}
.chatbox{max-height:260px;overflow:auto;margin-bottom:8px}
#toasts{position:fixed;top:calc(env(safe-area-inset-top,0px) + 8px);right:8px;z-index:30;display:grid;gap:8px;width:240px}
.toast{background:rgba(20,20,30,.95);color:#f1eeff;border:1px solid var(--ac);border-radius:12px;padding:10px;font-size:13px;font-family:'Inter',sans-serif;box-shadow:0 6px 24px #0008;animation:slin .25s}
.toast .row{gap:4px;margin-top:8px;flex-wrap:nowrap}.toast button{padding:5px 6px;font-size:11px;flex:1;border-radius:8px}.toast button.ok{background:#1f9d55;border-color:#1f9d55}.toast button.no{background:#b3261e;border-color:#b3261e}
@keyframes slin{from{transform:translateX(30px);opacity:0}}
@keyframes bob{50%{transform:translateY(-4px)}}@keyframes tw{50%{opacity:.25}}@keyframes fall{from{transform:translateY(-6px)}to{transform:translateY(14px)}}
.bob{animation:bob 1.6s infinite}.tw{animation:tw 1.2s infinite}.fl{animation:fall 1.6s linear infinite}
.tabs{display:flex;gap:6px;margin-bottom:10px;flex-wrap:wrap}small{opacity:.75}
.cardbox{font-size:20px;letter-spacing:2px;font-weight:700;color:var(--ac)}
</style></head><body><div id="app"></div><div id="toasts"></div>
<script>
const $=s=>document.querySelector(s);let S,U=null,tab='home',authMode='in',demo=false,stream=null,mic=true,CALL=null,CONF=null,payFor=null,testPay=false,NT=[],nid=0;
const store={get(k,d){try{return JSON.parse(localStorage.getItem(k))??d}catch(e){return d}},set(k,v){try{localStorage.setItem(k,JSON.stringify(v))}catch(e){}}};
const CARD='5168752112060358',CARDF='5168 7521 1206 0358';
const G={santa:{n:'Санта Клаус 2027',p:300},tree:{n:'Ёлка 2027',p:250},ball:{n:'Снежный шар 2027',p:200},window:{n:'Замёрзшее окно 2027',p:350},
sponge:{n:'Морская губка',p:300},star:{n:'Розовая звезда',p:300},octo:{n:'Осьминог-музыкант',p:350},town:{n:'Подводный городок',p:500}};
const R=[['px',50,40],['px',100,20],['px',200,15],['px',500,10],['px',700,5],['g','santa',3.3],['g','tree',3.3],['g','ball',3.3],['px',1500,.1]];
const svg=(k,c='')=>{const D={
santa:`<defs><linearGradient id="sc" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#ff5252"/><stop offset="1" stop-color="#a30f1e"/></linearGradient><radialGradient id="sf" cx=".5" cy=".4" r=".65"><stop offset="0" stop-color="#ffe0c8"/><stop offset="1" stop-color="#e8a883"/></radialGradient></defs>
<ellipse cx="60" cy="113" rx="36" ry="5" fill="#0005"/><ellipse cx="22" cy="92" rx="9" ry="16" fill="url(#sc)"/><ellipse cx="98" cy="92" rx="9" ry="16" fill="url(#sc)"/><circle cx="20" cy="106" r="7" fill="#fff"/><circle cx="100" cy="106" r="7" fill="#fff"/>
<path d="M24 112C20 82 36 70 60 70s40 12 36 42z" fill="url(#sc)"/><rect x="24" y="96" width="72" height="9" fill="#222"/><rect x="52" y="93" width="16" height="15" rx="3" fill="#f5c542" stroke="#b8860b" stroke-width="2"/><rect x="24" y="106" width="72" height="8" rx="4" fill="#fff"/>
<circle cx="60" cy="52" r="21" fill="url(#sf)"/><path d="M38 52c0 24 10 34 22 34s22-10 22-34c-7 7-13 9-22 9s-15-2-22-9z" fill="#fff"/><path d="M47 57q6-7 13-1q7-6 13 1q-6 9-13 4q-7 5-13-4z" fill="#f6f6f6" stroke="#ddd"/>
<circle cx="60" cy="53" r="4.5" fill="#f09a86"/><circle cx="51" cy="46" r="2.4" fill="#222"/><circle cx="69" cy="46" r="2.4" fill="#222"/><circle cx="50.5" cy="45.3" r=".8" fill="#fff"/><circle cx="68.5" cy="45.3" r=".8" fill="#fff"/><ellipse cx="45" cy="52" rx="4" ry="2.5" fill="#ff8a8a" opacity=".5"/><ellipse cx="75" cy="52" rx="4" ry="2.5" fill="#ff8a8a" opacity=".5"/>
<path d="M37 44C36 22 50 8 68 11c11 2 17 11 17 11l-1 22z" fill="url(#sc)"/><rect x="34" y="38" width="52" height="12" rx="6" fill="#fff"/><circle cx="87" cy="22" r="8" fill="#fff"/>`,
tree:`<defs><linearGradient id="tg" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#3ddc84"/><stop offset="1" stop-color="#0f6b3a"/></linearGradient><linearGradient id="tk" x1="0" x2="1"><stop offset="0" stop-color="#6b3f1d"/><stop offset="1" stop-color="#a9693a"/></linearGradient><radialGradient id="to"><stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#e53935"/></radialGradient></defs>
<ellipse cx="60" cy="114" rx="34" ry="4" fill="#0005"/><rect x="53" y="100" width="14" height="14" rx="2" fill="url(#tk)"/>
<g fill="url(#tg)" stroke="url(#tg)" stroke-width="7" stroke-linejoin="round"><path d="M60 22L78 52H42z"/><path d="M60 36L88 78H32z"/><path d="M60 54L98 102H22z"/></g>
<path d="M44 52q16 8 32 0M36 78q24 12 48 0M28 100q32 12 64 0" fill="none" stroke="#ffd54a" stroke-width="2.5" stroke-dasharray="1 5" stroke-linecap="round"/>
<path d="M45 49q15-8 30 0l-3 3q-12-5-24 0z" fill="#fff" opacity=".85"/>
<circle cx="52" cy="68" r="4.5" fill="url(#to)"/><circle cx="70" cy="62" r="4" fill="#4aa3ff"/><circle cx="60" cy="86" r="5" fill="url(#to)"/><circle cx="40" cy="92" r="4.5" fill="#ffd54a"/><circle cx="80" cy="90" r="4.5" fill="#4aa3ff"/>
<circle cx="64" cy="44" r="2.5" fill="#fff176" class="tw"/><circle cx="48" cy="82" r="2.5" fill="#fff176" class="tw"/><circle cx="76" cy="74" r="2.5" fill="#ff8a80" class="tw"/><circle cx="32" cy="98" r="2.5" fill="#fff176" class="tw"/>
<path d="M60 4l4 8.5 9 1.2-6.6 6.2 1.7 9-8.1-4.4-8.1 4.4 1.7-9-6.6-6.2 9-1.2z" fill="#ffd54a" stroke="#f9a825" stroke-width="1.5"/>`,
ball:`<defs><radialGradient id="gl" cx=".35" cy=".28" r=".85"><stop offset="0" stop-color="#fff" stop-opacity=".75"/><stop offset=".4" stop-color="#bfe8ff" stop-opacity=".2"/><stop offset="1" stop-color="#4a90d9" stop-opacity=".45"/></radialGradient><linearGradient id="bs" x1="0" x2="1"><stop offset="0" stop-color="#5a3318"/><stop offset=".5" stop-color="#a9693a"/><stop offset="1" stop-color="#5a3318"/></linearGradient><linearGradient id="sk" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#1b2f6b"/><stop offset="1" stop-color="#5a7fd6"/></linearGradient></defs>
<path d="M22 94h76l6 20H16z" fill="url(#bs)"/><rect x="22" y="94" width="76" height="6" fill="#f5c542"/>
<circle cx="60" cy="52" r="42" fill="url(#sk)"/><path d="M19 64Q60 50 101 64A42 42 0 0 1 19 64z" fill="#fff"/>
<path d="M44 66l9-20 9 20z" fill="#1fa05a"/><path d="M47 58l6-14 6 14z" fill="#2fcf7a"/><rect x="52" y="66" width="3" height="5" fill="#6b3f1d"/>
<circle cx="76" cy="68" r="8" fill="#fff" stroke="#dbe9f7"/><circle cx="76" cy="58" r="5.5" fill="#fff" stroke="#dbe9f7"/><circle cx="74.5" cy="57" r=".9" fill="#222"/><circle cx="77.5" cy="57" r=".9" fill="#222"/><path d="M76 59l4 1.2-4 .8z" fill="#ff8a3d"/>
<g fill="#fff"><circle cx="34" cy="38" r="2" class="fl"/><circle cx="52" cy="26" r="1.8" class="fl"/><circle cx="72" cy="34" r="2.2" class="fl"/><circle cx="88" cy="46" r="1.8" class="fl"/><circle cx="64" cy="22" r="1.6" class="fl"/></g>
<circle cx="60" cy="52" r="42" fill="url(#gl)" stroke="#fff" stroke-opacity=".5"/><ellipse cx="44" cy="26" rx="10" ry="5" fill="#fff" opacity=".6" transform="rotate(-35 44 26)"/>`,
window:`<defs><linearGradient id="wf" x1="0" x2="1" y1="0" y2="1"><stop offset="0" stop-color="#a9693a"/><stop offset="1" stop-color="#5a3318"/></linearGradient><linearGradient id="wg" x1="0" x2="1" y1="0" y2="1"><stop offset="0" stop-color="#d9f4ff"/><stop offset="1" stop-color="#78c0ee"/></linearGradient></defs>
<rect x="10" y="8" width="100" height="100" rx="7" fill="url(#wf)"/><rect x="18" y="16" width="38" height="38" rx="3" fill="url(#wg)"/><rect x="64" y="16" width="38" height="38" rx="3" fill="url(#wg)"/><rect x="18" y="62" width="38" height="38" rx="3" fill="url(#wg)"/><rect x="64" y="62" width="38" height="38" rx="3" fill="url(#wg)"/>
<g fill="#fff" opacity=".9"><path d="M18 16h16q-6 4-8 12-3-6-8-8z"/><path d="M102 16H88q6 4 8 12 3-6 6-8z"/><path d="M18 100h18q-8-4-10-14-4 8-8 8z"/><path d="M102 100H86q8-4 10-14 4 8 6 8z"/></g>
<g fill="#fff" opacity=".85"><path d="M22 16l2 8 2-8zM30 16l1.5 6 1.5-6zM68 16l2 7 2-7zM76 16l1.5 5 1.5-5z"/></g>
<text x="60" y="44" text-anchor="middle" font-family="Inter,sans-serif" font-weight="700" font-size="17" fill="#0a3a6b">20</text><text x="60" y="90" text-anchor="middle" font-family="Inter,sans-serif" font-weight="700" font-size="17" fill="#0a3a6b">27</text>
<g stroke="#fff" stroke-width="1.5" stroke-linecap="round" class="tw"><path d="M86 70v10M81 75h10M82.5 71.5l7 7M89.5 71.5l-7 7"/><path d="M34 26v8M30 30h8"/></g><rect x="6" y="106" width="108" height="8" rx="3" fill="url(#wf)"/>`,
sponge:`<defs><linearGradient id="sg" x1="0" x2="1" y1="0" y2="1"><stop offset="0" stop-color="#fff176"/><stop offset="1" stop-color="#f9a825"/></linearGradient></defs>
<ellipse cx="60" cy="114" rx="34" ry="4" fill="#0005"/><path d="M84 106q4-22 10-24M92 106q0-16 8-20" stroke="#2fcf7a" stroke-width="5" stroke-linecap="round" fill="none"/>
<rect x="28" y="26" width="64" height="82" rx="24" fill="url(#sg)"/><ellipse cx="60" cy="28" rx="30" ry="9" fill="#f9a825"/><ellipse cx="60" cy="28" rx="22" ry="5.5" fill="#b26a00"/>
<g fill="#d98a00" opacity=".8"><ellipse cx="38" cy="86" rx="4" ry="5"/><ellipse cx="82" cy="92" rx="5" ry="4"/><ellipse cx="74" cy="46" rx="3.5" ry="4.5"/><ellipse cx="36" cy="50" rx="3" ry="4"/><ellipse cx="50" cy="100" rx="3.5" ry="3"/></g>
<circle cx="48" cy="62" r="10" fill="#fff" stroke="#b26a00" stroke-width="1.5"/><circle cx="73" cy="62" r="10" fill="#fff" stroke="#b26a00" stroke-width="1.5"/><circle cx="50" cy="63" r="5" fill="#2a8fe0"/><circle cx="71" cy="63" r="5" fill="#2a8fe0"/><circle cx="50.5" cy="63" r="2.4" fill="#111"/><circle cx="70.5" cy="63" r="2.4" fill="#111"/><circle cx="52" cy="61" r="1.2" fill="#fff"/><circle cx="72" cy="61" r="1.2" fill="#fff"/>
<path d="M44 78q16 14 32 0" stroke="#7a3b00" stroke-width="3" fill="none" stroke-linecap="round"/><ellipse cx="38" cy="76" rx="5" ry="3" fill="#ff8a65" opacity=".6"/><ellipse cx="82" cy="76" rx="5" ry="3" fill="#ff8a65" opacity=".6"/>
<circle cx="22" cy="40" r="3" fill="#bfe8ff" opacity=".8" class="fl"/><circle cx="100" cy="58" r="2.5" fill="#bfe8ff" opacity=".8" class="fl"/>`,
star:`<defs><linearGradient id="pg" x1="0" x2="1" y1="0" y2="1"><stop offset="0" stop-color="#ffb3d1"/><stop offset="1" stop-color="#e0558f"/></linearGradient></defs>
<ellipse cx="60" cy="112" rx="34" ry="4" fill="#0005"/><path d="M60 16L71.8 45.8L103.8 47.8L79 68.2L87 99.2L60 82L33 99.2L41 68.2L16.2 47.8L48.2 45.8Z" fill="url(#pg)" stroke="url(#pg)" stroke-width="9" stroke-linejoin="round"/>
<g fill="#c2407a" opacity=".6"><circle cx="60" cy="30" r="2.5"/><circle cx="90" cy="52" r="2.5"/><circle cx="78" cy="88" r="2.5"/><circle cx="42" cy="88" r="2.5"/><circle cx="30" cy="52" r="2.5"/><circle cx="52" cy="40" r="1.8"/><circle cx="70" cy="40" r="1.8"/></g>
<circle cx="51" cy="56" r="6" fill="#fff"/><circle cx="69" cy="56" r="6" fill="#fff"/><circle cx="52" cy="57" r="3" fill="#222"/><circle cx="68" cy="57" r="3" fill="#222"/><circle cx="53" cy="55.8" r="1" fill="#fff"/><circle cx="69" cy="55.8" r="1" fill="#fff"/>
<path d="M50 68q10 9 20 0" stroke="#8a1f55" stroke-width="2.5" fill="none" stroke-linecap="round"/><ellipse cx="44" cy="66" rx="4" ry="2.5" fill="#ff6f91" opacity=".6"/><ellipse cx="76" cy="66" rx="4" ry="2.5" fill="#ff6f91" opacity=".6"/>`,
octo:`<defs><radialGradient id="og" cx=".4" cy=".3" r=".8"><stop offset="0" stop-color="#c9a6ff"/><stop offset="1" stop-color="#6a3fb5"/></radialGradient></defs>
<ellipse cx="60" cy="114" rx="36" ry="4" fill="#0005"/><g stroke="#7d4fcf" stroke-width="10" stroke-linecap="round" fill="none"><path d="M36 72q-18 10-14 26q2 8 10 6"/><path d="M46 78q-8 16-2 28q3 6 9 4"/><path d="M60 80v20q0 8 7 8"/><path d="M74 78q8 16 2 28q-3 6-9 4"/><path d="M84 72q18 10 14 26q-2 8-10 6"/></g>
<g fill="#e6d3ff" opacity=".8"><circle cx="26" cy="92" r="2"/><circle cx="46" cy="98" r="2"/><circle cx="60" cy="96" r="2"/><circle cx="92" cy="92" r="2"/></g>
<ellipse cx="60" cy="50" rx="32" ry="32" fill="url(#og)"/><g fill="#a97be8" opacity=".7"><circle cx="44" cy="30" r="3"/><circle cx="62" cy="24" r="2.5"/><circle cx="76" cy="32" r="3"/></g>
<circle cx="48" cy="52" r="10" fill="#fff"/><circle cx="72" cy="52" r="10" fill="#fff"/><circle cx="50" cy="54" r="5" fill="#222"/><circle cx="70" cy="54" r="5" fill="#222"/><circle cx="51.5" cy="52" r="1.6" fill="#fff"/><circle cx="71.5" cy="52" r="1.6" fill="#fff"/>
<path d="M50 72q10 7 20 0" stroke="#3a1a70" stroke-width="2.5" fill="none" stroke-linecap="round"/><rect x="82" y="66" width="30" height="5" rx="2.5" fill="#333" transform="rotate(-25 82 66)"/><text x="100" y="40" font-size="16" fill="#ffd54a" class="tw" font-family="Inter,sans-serif">♪</text><text x="14" y="34" font-size="13" fill="#ffd54a" class="tw" font-family="Inter,sans-serif">♫</text>`,
town:`<defs><linearGradient id="wt" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#4fc3f7"/><stop offset="1" stop-color="#0d3b78"/></linearGradient><radialGradient id="dm" cx=".35" cy=".25" r=".9"><stop offset="0" stop-color="#fff" stop-opacity=".6"/><stop offset=".5" stop-color="#fff" stop-opacity=".05"/><stop offset="1" stop-color="#fff" stop-opacity=".25"/></radialGradient></defs>
<path d="M10 108a50 50 0 0 1 100 0z" fill="url(#wt)"/><path d="M10 108q20-8 50-4t50 4v6H10z" fill="#e8c27a"/>
<rect x="26" y="78" width="18" height="26" fill="#ff9966"/><path d="M23 78l12-14 12 14z" fill="#c0392b"/><rect x="32" y="88" width="6" height="8" rx="3" fill="#ffe082" class="tw"/>
<rect x="50" y="62" width="20" height="42" fill="#7e57c2"/><path d="M47 62l13-16 13 16z" fill="#4527a0"/><circle cx="60" cy="74" r="4" fill="#ffe082" class="tw"/><rect x="56" y="88" width="8" height="10" rx="4" fill="#ffe082"/>
<rect x="76" y="80" width="18" height="24" fill="#4db6ac"/><path d="M73 80l12-12 12 12z" fill="#00796b"/><rect x="82" y="88" width="6" height="8" rx="3" fill="#ffe082" class="tw"/>
<path d="M16 104q2-14 8-18M104 104q-2-14-8-18" stroke="#2fcf7a" stroke-width="4" stroke-linecap="round" fill="none"/>
<g fill="#fff" opacity=".7"><circle cx="40" cy="50" r="3" class="fl"/><circle cx="82" cy="42" r="2.5" class="fl"/><circle cx="96" cy="60" r="2" class="fl"/><circle cx="28" cy="66" r="2" class="fl"/></g>
<path d="M30 40q6-6 12 0q-6 2-6 6z" fill="#ffb74d"/><path d="M84 58q5-5 10 0q-5 2-5 5z" fill="#ff8a65"/>
<path d="M10 108a50 50 0 0 1 100 0" fill="url(#dm)" stroke="#fff" stroke-opacity=".6" stroke-width="2"/><rect x="6" y="108" width="108" height="6" rx="3" fill="#8d6e63"/>`};
return `<svg viewBox="0 0 120 120" class="${c}">${D[k]||''}</svg>`};
const pav=i=>{let r='';for(let y=0;y<5;y++)for(let x=0;x<3;x++){const h=(((i+1)*2654435761)+y*40503+x*9973)>>>0;if((h>>>7)&1){r+=`<rect x="${x}" y="${y}" width="1" height="1"/>`;if(x<2)r+=`<rect x="${4-x}" y="${y}" width="1" height="1"/>`}}return `<svg viewBox="0 0 5 5" shape-rendering="crispEdges"><rect width="5" height="5" fill="hsl(${i*36} 40% 18%)"/><g fill="hsl(${i*36} 85% 62%)">${r}</g></svg>`};
const avh=a=>a=='img'&&S.avimg?`<img src="${S.avimg}" alt="">`:/^p\d$/.test(a)?pav(+a.slice(1)):a;
function img(inp,k){const f=inp.files[0];if(!f)return;const r=new FileReader();r.onload=()=>{const im=new Image();im.onload=()=>{const m=k=='av'?256:1280,s=Math.min(1,m/Math.max(im.width,im.height)),c=document.createElement('canvas');c.width=im.width*s;c.height=im.height*s;c.getContext('2d').drawImage(im,0,0,c.width,c.height);const u=c.toDataURL('image/jpeg',.8);if(k=='av'){S.avimg=u;S.av='img'}else S.bgimg=u;save();render()};im.src=r.result};r.readAsDataURL(f)}
const sha=async t=>[...new Uint8Array(await crypto.subtle.digest('SHA-256',new TextEncoder().encode(t)))].map(x=>x.toString(16).padStart(2,'0')).join('');
const save=()=>{store.set('pc_u_'+U,S);store.set('pc_taken',TK)};
let TK=(()=>{const t=store.get('pc_taken',{});Object.keys(G).forEach(k=>t[k]=t[k]||[]);return t})();
function take(g){const f=[];for(let i=1;i<=50;i++)if(!TK[g].includes(i))f.push(i);if(!f.length)return 0;const n=f[Math.random()*f.length|0];TK[g].push(n);return n}
function esc(t){return String(t).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]))}
const fn=f=>(f.nm||'Игрок')+' ·'+f.id.slice(-4);
const lim=()=>'<span class="lim">limited</span>';
function applyTheme(){const s=S?.set||{bri:1,hue:270};document.documentElement.style.setProperty('--bgimg',S?.bgimg?`url(${S.bgimg})`:'none');const d=document.documentElement.style,t=s.theme||'black',L=t=='white',has=!!S?.bgimg,nf=s.font=='normal';d.setProperty('--h',s.hue);d.setProperty('--b',s.bri);
document.body.classList.toggle('nf',nf);d.setProperty('--fb',nf?"'Inter',system-ui,sans-serif":"'Pixelify Sans','Courier New',monospace");d.setProperty('--fh',nf?"'Inter',system-ui,sans-serif":"'Press Start 2P','Courier New',monospace");
const rb='linear-gradient(180deg,hsl(var(--h) 90% 65%/.6) 0%,hsl(calc(var(--h) + 60) 90% 60%/.4) 25%,hsl(calc(var(--h) + 130) 90% 55%/.22) 50%,hsl(calc(var(--h) + 200) 90% 55%/.1) 70%,transparent 88%)',cl='linear-gradient(180deg,hsl(var(--h) 90% 60%/.5) 0%,transparent 70%)';
d.setProperty('--light',has?'none':t=='rainbow'?rb:t=='color'?cl:'none');
d.setProperty('--bg',L?'#f4f4f8':t=='black'?'#050505':'#0d0b1a');d.setProperty('--tx',L?'#111':'#f1eeff');d.setProperty('--ac',t=='black'?'#fff':L?'#111':'hsl(var(--h) 90% 65%)');
d.setProperty('--gl',L?'rgba(0,0,0,.05)':'rgba(255,255,255,.06)');d.setProperty('--bd',L?'rgba(0,0,0,.25)':'rgba(255,255,255,.18)');d.setProperty('--hv',L?'rgba(0,0,0,.1)':'rgba(255,255,255,.14)');d.setProperty('--bar',L?'rgba(244,244,248,.7)':'rgba(0,0,0,.6)');d.colorScheme=L?'light':'dark'}
function today(){return new Date()}
function render(){applyTheme();if(!U){$('#app').innerHTML=authView();return}const T=[['home','Главная'],['shop','Магазин'],['inv','Инвентарь'],['friends','Друзья'],['chats','Чаты'],['call','Звонок'],['conf','Конференция'],['pay','Пиксели'],['set','Настройки']];
$('#app').innerHTML=`<div id="bar"><span class="logo">PixelCall</span>${T.map(t=>`<button class="nv ${tab==t[0]?'on':''}" onclick="go('${t[0]}')">${t[1]}</button>`).join('')}<span class="sp"></span><span class="px">${S.px} px</span><button id="adv" onclick="go('adv')" title="Адвент-календарь">🎁<span>Адвент-календарь</span></button></div><main>${view()}</main>`;
const v=$('#v');if(v&&stream)v.srcObject=stream;const cc=$('#cc');if(cc)cc.scrollTop=cc.scrollHeight}
function go(t){tab=t;render()}
function authView(){return `<main style="max-width:420px"><h1 style="color:var(--ac)">PixelCall</h1><div class="card"><div class="tabs"><button class="${authMode=='in'?'on':''}" onclick="authMode='in';render()">Вход</button><button class="${authMode=='up'?'on':''}" onclick="authMode='up';render()">Регистрация</button></div>
<div style="display:grid;gap:8px"><input id="nk" placeholder="Никнейм"><input id="pw" type="password" placeholder="Пароль">
${authMode=='up'?`<select id="sv"><option>Google</option><option>Facebook</option><option>Apple ID</option><option>Email</option><option>Номер телефона</option></select><input id="ct" placeholder="Почта / аккаунт / номер для 2FA"><input id="bd" type="date" title="День рождения">`:''}
<input id="cd" placeholder="Код 2FA (демо: 123456)"><button onclick="auth()">${authMode=='in'?'Войти':'Создать аккаунт'}</button><small id="er"></small></div></div><small>Демо: вход через Google/Facebook/Apple/SMS требует сервера, здесь 2FA имитируется кодом 123456.</small></main>`}
async function auth(){const n=$('#nk').value.trim(),p=$('#pw').value,e=$('#er');if(n.length<3||p.length<6){e.textContent='Ник от 3 символов, пароль от 6';return}if($('#cd').value!='123456'){e.textContent='Неверный код 2FA';return}
const h=await sha(p),a=store.get('pc_acc',{});if(authMode=='up'){if(a[n]){e.textContent='Ник занят';return}if(!$('#ct').value.trim()){e.textContent='Укажите сервис для 2FA';return}a[n]={h,sv:$('#sv').value};store.set('pc_acc',a);U=n;S={px:0,inv:[],adv:{cells:{},last:0},friends:[],chats:{},pending:[],id:String(Math.random()).slice(2,12).padEnd(10,'0'),bio:'',av:'🙂',bd:$('#bd').value,set:{bri:1,hue:270,theme:'black',font:'pixel',bday:true,corners:['santa','tree','ball','window']}};save()}
else{if(!a[n]||a[n].h!=h){e.textContent='Неверный ник или пароль';return}U=n;S=store.get('pc_u_'+n);S.pending=S.pending||[];S.set.font=S.set.font||'pixel'}render()}
function view(){return({home,shop,inv,friends,chats,call:callV,conf:confV,pay,set:setV,adv})[tab]()}
function bdToday(){if(!S.bd)return false;const d=new Date(S.bd),t=today();return d.getDate()==t.getDate()&&d.getMonth()==t.getMonth()}
function home(){return `<div class="card row"><div class="av on">${S.set.bday&&bdToday()?'<i>🎂</i>':''}${avh(S.av)}</div><div><b>${esc(U)}</b><br><small>PixelID: ${S.id}</small><br><input value="${esc(S.bio)}" placeholder="Цитата о себе" onchange="S.bio=this.value;save()"></div><div class="row" style="max-width:340px">${[0,1,2,3,4,5,6,7,8,9].map(i=>`<button class="pk ${S.av=='p'+i?'on':''}" onclick="S.av='p${i}';save();render()">${pav(i)}</button>`).join('')}<label>Своя картинка <input type="file" accept="image/*" onchange="img(this,'av')"></label></div></div>
<div class="card"><h3>Встречи</h3><div class="row"><button onclick="go('conf')">Создать конференцию</button><button onclick="go('call')">Позвонить другу</button></div></div>
<div class="card"><h3>Тест входящих</h3><div class="row"><button onclick="simIn('call')">📞 Входящий звонок</button><button onclick="simIn('conf')">👥 Приглашение в конференцию</button><button onclick="simIn('trade')">🔄 Входящий обмен</button></div><small>Демо без сервера: уведомление появится справа вверху.</small></div>`}
/* ---------- Уведомления справа вверху ---------- */
function notify(o){o.id=++nid;NT.push(o);drawNT();o.tm=setTimeout(()=>dismiss(o.id),30000)}
function dismiss(id){const n=NT.find(x=>x.id==id);if(n)clearTimeout(n.tm);NT=NT.filter(x=>x.id!=id);drawNT()}
function drawNT(){$('#toasts').innerHTML=NT.map(n=>{const ic={call:'📞',conf:'👥',trade:'🔄'}[n.type],tx={call:'звонит вам',conf:'приглашает вас в конференцию',trade:`предлагает обмен: ваш «${n.want?G[n.want.g].n+' #'+n.want.n:''}» на «${n.give?G[n.give].n:''}»`}[n.type];
return `<div class="toast"><b>${ic} ${esc(n.nm)}</b><div style="margin-top:2px">${tx}</div><div class="row"><button class="ok" onclick="act(${n.id},'ok')">Принять</button><button onclick="act(${n.id},'ig')">Игнор</button><button class="no" onclick="act(${n.id},'no')">Отклонить</button></div></div>`}).join('')}
function act(id,a){const n=NT.find(x=>x.id==id);if(!n)return;dismiss(id);if(a!='ok')return;
if(n.type=='call'){CALL={id:n.fid,nm:n.nm,ringing:false};go('call')}
else if(n.type=='conf'){CONF={mem:[{id:n.fid,nm:n.nm,ic:n.ic}],chat:[{nm:n.nm,t:'Привет! Заходи в конференцию'}]};go('conf')}
else{const i=S.inv.findIndex(x=>x.g==n.want.g&&x.n==n.want.n);if(i<0){alert('Этого подарка у вас уже нет');return}const nn=take(n.give);if(!nn){alert('Все 50 экземпляров этого подарка разобраны');return}
TK[n.want.g]=TK[n.want.g].filter(x=>x!=n.want.n);S.inv.splice(i,1);S.inv.push({g:n.give,n:nn,adv:false});save();render()}}
function fakeF(){if(S.friends.length){const f=S.friends[Math.random()*S.friends.length|0];return{fid:f.id,nm:fn(f),ic:f.ic}}return{fid:'0000000000',nm:'Игрок ·0000',ic:'👾'}}
function simIn(t){const f=fakeF();if(t=='trade'){if(!S.inv.length){alert('Сначала получите подарок: обмен предлагают на ваш подарок');return}const w=S.inv[Math.random()*S.inv.length|0],ks=Object.keys(G).filter(k=>k!=w.g);notify({type:'trade',...f,want:{g:w.g,n:w.n},give:ks[Math.random()*ks.length|0]})}else notify({type:t,...f})}
/* ---------- Магазин и подарки ---------- */
function shop(){return `<div class="grid">${Object.entries(G).map(([k,g])=>`<div class="card g">${lim()}${svg(k,'bob')}<div class="gn">${g.n}</div><div class="px">${g.p} px</div><small>${50-TK[k].length}/50 осталось</small><br><button onclick="buy('${k}')" ${TK[k].length>=50?'disabled':''}>Купить</button></div>`).join('')}</div>`}
function buy(k){const g=G[k];if(S.px<g.p){alert('Недостаточно пикселей');go('pay');return}const n=take(k);if(!n)return;S.px-=g.p;S.inv.push({g:k,n,adv:false});save();render()}
function inv(){return S.inv.length?`<div class="grid">${S.inv.map((it,i)=>`<div class="card g">${lim()}${svg(it.g,'bob')}<div class="gn">${G[it.g].n}</div><b>#${it.n}/50</b>${it.adv?'<br><small>из адвента: только обмен</small>':''}<br><button onclick="trade(${i})">Предложить обмен</button> ${it.adv?'':`<button onclick="sell(${i})">Продать</button>`}</div>`).join('')}</div>`:'<div class="card">Инвентарь пуст</div>'}
function sell(i){const it=S.inv[i];S.px+=Math.floor(G[it.g].p*.7);TK[it.g]=TK[it.g].filter(x=>x!=it.n);S.inv.splice(i,1);save();render()}
function trade(i){if(!S.friends.length){alert('Сначала добавьте друга');return}const n=prompt('Кому? Введите номер:\n'+S.friends.map((f,j)=>`${j+1}. ${fn(f)}`).join('\n'));const f=S.friends[(+n||0)-1];if(f){alert('Предложение обмена отправлено: '+fn(f)+' (демо)')}}
/* ---------- Друзья и чаты ---------- */
function friends(){return `<div class="card">Ваш PixelID: <b>${S.id}</b><div class="row" style="margin-top:8px"><input id="fid" placeholder="PixelID друга (10 цифр)" maxlength="10"><button onclick="addF()">Добавить в друзья</button></div></div><div class="card row">${S.friends.map(f=>`<div style="text-align:center"><div class="av ${f.on?'on':''}">${f.ic}</div><small>${esc(fn(f))}</small></div>`).join('')||'Друзей пока нет'}</div>`}
function addF(){const v=$('#fid').value.trim();if(!/^\d{10}$/.test(v)||v==S.id||S.friends.some(f=>f.id==v)){alert('Неверный ID');return}const i=Math.random()*4|0;S.friends.push({id:v,on:Math.random()>.5,ic:['🦊','🐱','👾','🚀'][i],nm:['Лис','Кот','Робот','Космонавт'][i]});save();render()}
let cf=null;function chats(){if(!S.friends.length)return '<div class="card">Добавьте друзей, чтобы писать</div>';cf=cf??S.friends[0].id;const m=S.chats[cf]||[];return `<div class="card"><div class="tabs">${S.friends.map(f=>`<button class="${f.id==cf?'on':''}" onclick="cf='${f.id}';render()">${esc(fn(f))}</button>`).join('')}</div>${m.map(x=>`<div class="msg ${x.me?'me':''}">${esc(x.t)}</div>`).join('')}<div class="row"><input id="mi" placeholder="Сообщение"><button onclick="send()">Отправить</button></div></div>`}
function send(){const t=$('#mi').value.trim();if(!t)return;(S.chats[cf]=S.chats[cf]||[]).push({me:1,t});save();render()}
/* ---------- Оплата пикселей ---------- */
const CP=[[500,200],[1000,380],[2000,700]],RT={'$':100,'€':108,'₽':1.1};
function pay(){return `<div class="card"><h3>Купить пиксели</h3><div class="grid">${CP.map(([p,u])=>`<div class="card g"><div class="px">${p} px</div><div>${u} ₴</div><button onclick="payFor=[${p},${u}];render()">💳 Оплатить</button></div>`).join('')}</div></div>
${payFor?`<div class="card"><h3>Оплата ${payFor[0]} px</h3><p>Переведите <b>${payFor[1]} ₴</b> на карту (Украина):</p><div class="cardbox">${CARDF}</div><div class="row" style="margin:8px 0"><button onclick="copyCard()">Скопировать номер</button></div><p>В комментарии к переводу укажите ваш PixelID: <b>${S.id}</b></p><div class="row"><button onclick="paid()">Я оплатил(а)</button><button onclick="payFor=null;render()">Отмена</button></div><small>Сайт не видит поступление денег сам: пиксели начисляются после проверки платежа (для автоматики нужен сервер и платёжный сервис).</small></div>`:''}
${S.pending.length?`<div class="card"><h3>Заявки на проверке</h3>${S.pending.map(x=>`<div>${x.p} px · ${x.u} ₴ · ${x.d}</div>`).join('')}</div>`:''}
<div class="card"><label><input type="checkbox" ${testPay?'checked':''} onchange="testPay=this.checked"> Тестовый режим: начислять сразу, без проверки (только для демо)</label></div>
<div class="card"><h3>Конвертер</h3><div class="row"><input id="am" type="number" min="0" value="1" oninput="cv()"><select id="cu" onchange="cv()"><option>$</option><option>€</option><option>₽</option></select> → <b id="cr" class="px">100 px</b></div><small>100 px = $1</small></div>`}
function copyCard(){try{navigator.clipboard.writeText(CARD).then(()=>alert('Номер карты скопирован'),()=>alert(CARD))}catch(e){alert(CARD)}}
function paid(){const[p,u]=payFor;if(testPay){S.px+=p;alert('Тест: начислено '+p+' px')}else{S.pending.push({p,u,d:new Date().toLocaleString('ru')});alert('Заявка отправлена. Пиксели начислятся после проверки платежа.')}payFor=null;save();render()}
function cv(){$('#cr').textContent=Math.floor(($('#am').value||0)*RT[$('#cu').value])+' px'}
/* ---------- Настройки ---------- */
function rename(){const n=$('#nn').value.trim(),a=store.get('pc_acc',{});if(n.length<3||n.length>20){alert('От 3 до 20 символов');return}if(n==U)return;if(a[n]){alert('Ник занят');return}a[n]=a[U];delete a[U];store.set('pc_acc',a);try{localStorage.removeItem('pc_u_'+U)}catch(e){}U=n;save();render()}
function setV(){const s=S.set;return `<div class="card"><h3>Имя</h3><div class="row"><input id="nn" value="${esc(U)}" maxlength="20"><button onclick="rename()">Сохранить имя</button></div><small>Новым ником нужно будет входить в аккаунт</small></div>
<div class="card"><h3>Шрифт</h3><div class="row"><button class="${s.font!='normal'?'on':''}" onclick="S.set.font='pixel';save();render()">Пиксельный</button><button class="${s.font=='normal'?'on':''}" onclick="S.set.font='normal';save();render()" style="font-family:'Inter',sans-serif">Обычный</button></div></div>
<div class="card"><h3>Тема</h3><div class="row">${[['black','Чёрная'],['white','Белая'],['rainbow','Радужная'],['color','Цветная']].map(([k,n])=>`<button class="${(s.theme||'black')==k?'on':''}" onclick="S.set.theme='${k}';save();render()">${n}</button>`).join('')}</div>${S.bgimg?'<small>Со своим фоном подсветка отключена</small>':''}</div>
<div class="card"><h3>Цвет и яркость</h3><label>Цвет <input type="range" min="0" max="360" value="${s.hue}" oninput="S.set.hue=this.value;applyTheme()" onchange="save()"></label> <label>Яркость <input type="range" min=".5" max="1.4" step=".05" value="${s.bri}" oninput="S.set.bri=this.value;applyTheme()" onchange="save()"></label></div>
<div class="card"><h3>Фон</h3><label>Своя картинка <input type="file" accept="image/*" onchange="img(this,'bg')"></label> <button onclick="S.bgimg='';save();render()">Убрать фон</button></div>
<div class="card"><h3>День рождения</h3><input type="date" value="${S.bd||''}" onchange="S.bd=this.value;save()"> <label><input type="checkbox" ${s.bday?'checked':''} onchange="S.set.bday=this.checked;save()"> Показывать тортик</label></div>
<div class="card"><h3>Подарки по углам камеры</h3>${s.corners.map((c,i)=>`<label>Угол ${i+1} <select onchange="S.set.corners[${i}]=this.value;save()">${['none',...Object.keys(G)].map(o=>`<option value="${o}" ${(o==c||(c=='snow'&&o=='ball'))?'selected':''}>${o=='none'?'Не ставить':G[o].n}</option>`).join('')}</select></label> `).join('')}<br><small>Ставятся только те подарки, которые у вас есть.</small></div>
<button onclick="U=null;S=null;render()">Выйти</button>`}
/* ---------- Адвент ---------- */
function adv(){const t=today(),inEv=t.getMonth()==11&&t.getDate()<=24,done=Object.keys(S.adv.cells).length,can=(demo||inEv)&&done<24&&Date.now()-S.adv.last>=864e5&&(demo||done<t.getDate());
return `<div class="card"><h3>Адвент-календарь (1–24 декабря)</h3><label><input type="checkbox" ${demo?'checked':''} onchange="demo=this.checked;render()"> Пробная версия (без ограничений по датам)</label><br><br><div class="grid" style="grid-template-columns:repeat(auto-fill,minmax(100px,1fr))">${Array.from({length:24},(_,i)=>{const d=i+1,c=S.adv.cells[d];return c?`<div class="cell" style="background:hsl(var(--h) 50% 30%)">${c.t=='g'?lim()+svg(c.v,'')+`<small>${G[c.v].n}</small>`:c.v+' px'}${c.got?'<small>✔</small>':`<button onclick="claim(${d})">Забрать</button>`}</div>`:`<button class="cell" onclick="openC(${d},${can&&d==done+1})" ${d==done+1&&can?'':'disabled'}>${d}</button>`}).join('')}</div><small>Ячейка раз в 24 часа. Награду можно забрать позже. Подарки из адвента нельзя продать, только обменять.</small></div>`}
function roll(d){let w=R.map(r=>[r,r[0]=='g'||r[1]==1500?r[2]+(d==24?1:0):r[2]]),s=w.reduce((a,x)=>a+x[1],0),x=Math.random()*s;for(const [r,v] of w){x-=v;if(x<=0)return r}return R[0]}
function openC(d,ok){if(!ok)return;const r=roll(d);S.adv.last=Date.now();S.adv.cells[d]=r[0]=='px'?{t:'px',v:r[1]}:{t:'g',v:r[1]};save();render()}
function claim(d){const c=S.adv.cells[d];if(c.t=='px')S.px+=c.v;else{const n=take(c.v);if(n)S.inv.push({g:c.v,n,adv:true});else{S.px+=875;alert('Все 50 экземпляров разобраны: вместо подарка 875 px')}}c.got=1;save();render()}
/* ---------- Звонок ---------- */
const POS=['left:6px;top:6px','right:6px;top:6px','left:6px;bottom:6px','right:6px;bottom:6px'];
function corners(){return S.set.corners.map((c,i)=>{const k=c=='snow'?'ball':c;return k!='none'&&S.inv.some(x=>x.g==k)?`<div class="cn" style="${POS[i]}">${svg(k,'bob')}</div>`:''}).join('')}
function ctrl(){return `<div class="row" style="margin-top:10px"><button onclick="cam()">📷 Камера</button><button onclick="mc()">🎤 Микрофон</button><button onclick="scr()">🖥 Демонстрация экрана</button></div>`}
function callV(){return `<div class="card"><div class="call"><video id="v" autoplay muted playsinline></video>${corners()}${CALL?`<div class="remote"><div><b>${S.friends.find(f=>f.id==CALL.id)?.ic||'👾'}</b>${esc(CALL.nm)}<br>${CALL.ringing?'Звоним…':'На связи'}</div></div>`:''}<div id="mt" class="muted" style="display:none">🎤 Микрофон выключен</div></div>${ctrl()}${CALL?`<div class="row" style="margin-top:10px"><button class="no" style="background:#b3261e" onclick="CALL=null;render()">📵 Завершить звонок</button></div>`:''}</div>
<div class="card"><h3>Позвонить другу</h3><div class="row">${S.friends.map(f=>`<button onclick="callF('${f.id}')">📞 ${esc(fn(f))}</button>`).join('')||'<small>Добавьте друзей во вкладке «Друзья»</small>'}</div><small>Видеосвязь с другими людьми требует сервера (WebRTC); здесь работают камера, микрофон и экран на вашем устройстве.</small></div>`}
function callF(id){const f=S.friends.find(x=>x.id==id);CALL={id,nm:fn(f),ringing:true};render();setTimeout(()=>{if(CALL&&CALL.id==id){CALL.ringing=false;if(tab=='call')render()}},2000)}
async function cam(){try{stream=await navigator.mediaDevices.getUserMedia({video:true,audio:true});$('#v').srcObject=stream;mic=true}catch(e){alert('Нет доступа к камере')}}
function mc(){mic=!mic;stream?.getAudioTracks().forEach(t=>t.enabled=mic);$('#mt').style.display=mic?'none':'block'}
async function scr(){try{$('#v').srcObject=await navigator.mediaDevices.getDisplayMedia({video:true})}catch(e){alert('Демонстрация недоступна')}}
/* ---------- Конференция + групповой чат ---------- */
const REPL=['Привет всем!','Слышно хорошо','Отличная идея 👍','Ща, секунду','Согласен','Ха-ха, круто'];
function confV(){if(!CONF)return `<div class="card"><h3>Конференция</h3><p>Создайте комнату, пригласите друзей и общайтесь в групповом чате.</p><button onclick="CONF={mem:[],chat:[]};render()">Создать конференцию</button></div>`;
const out=S.friends.filter(f=>!CONF.mem.some(m=>m.id==f.id));
return `<div class="card"><h3>Конференция · ${CONF.mem.length+1} уч.</h3><div class="tiles"><div class="tile"><video id="v" autoplay muted playsinline></video>${corners().replace(/class="cn"/g,'class="cn" ').replace(/<div class="cn" style="([^"]*)">/g,'<div style="position:absolute;width:26%;$1">')}<span style="position:absolute;left:6px;bottom:4px;background:#0009;padding:1px 6px;border-radius:6px">Вы</span></div>${CONF.mem.map(m=>`<div class="tile"><div><b>${m.ic||'👾'}</b>${esc(m.nm)}</div></div>`).join('')}</div>${ctrl()}
<div class="row" style="margin-top:10px">${out.map(f=>`<button onclick="invF('${f.id}')">➕ ${esc(fn(f))}</button>`).join('')||'<small>Нет друзей для приглашения</small>'}<button style="background:#b3261e" onclick="CONF=null;render()">Выйти</button></div></div>
<div class="card"><h3>Групповой чат</h3><div class="chatbox" id="cc">${chatHtml()}</div><div class="row"><input id="ci" placeholder="Сообщение в группу" onkeydown="if(event.key=='Enter')csend()"><button onclick="csend()">Отправить</button></div></div>`}
function chatHtml(){return CONF.chat.map(x=>`<div class="msg ${x.me?'me':''}">${x.me?'':`<small>${esc(x.nm)}</small>`}${esc(x.t)}</div>`).join('')||'<small>Сообщений пока нет</small>'}
function chatDraw(){const c=$('#cc');if(c){c.innerHTML=chatHtml();c.scrollTop=c.scrollHeight}}
function invF(id){const f=S.friends.find(x=>x.id==id);CONF.chat.push({nm:'Система',t:'Приглашение отправлено: '+fn(f)});render();setTimeout(()=>{if(CONF&&!CONF.mem.some(m=>m.id==id)){CONF.mem.push({id,nm:fn(f),ic:f.ic});CONF.chat.push({nm:fn(f),t:'Подключился(ась)'});if(tab=='conf')render()}},1500)}
function csend(){const i=$('#ci'),t=i.value.trim();if(!t)return;CONF.chat.push({me:1,nm:U,t});i.value='';chatDraw();if(CONF.mem.length){const m=CONF.mem[Math.random()*CONF.mem.length|0];setTimeout(()=>{if(CONF){CONF.chat.push({nm:m.nm,t:REPL[Math.random()*REPL.length|0]});chatDraw()}},1000)}}
render();
</script></body></html>
"""

components.html(PAGE, height=1100, scrolling=True)

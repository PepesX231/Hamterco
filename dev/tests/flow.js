const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();
for(const W of [1440,390]){const H=W<500?844:900;const p=await b.newPage({viewport:{width:W,height:H},isMobile:W<500,hasTouch:W<500});const e=[];p.on('pageerror',x=>e.push(x.message.slice(0,100)));const log=(...a)=>console.log(W,...a);
const B='http://localhost:8791/Hamterco/next/';
await p.goto(B);await p.waitForFunction(()=>!document.getElementById('hhL')&&document.querySelector('.lg-box')?.dataset.ready,null,{timeout:30000});
// 1 home search -> route matches
await p.click('.nx-bar input',{force:true});await p.keyboard.type('อยากทำเว็บ');await p.keyboard.press('Enter');await p.waitForTimeout(2500);
log('home matches:',await p.evaluate(()=>[...document.querySelectorAll('.nx-found b')].map(b=>b.textContent).join(', ')));
await p.screenshot({path:'f1-'+W+'.png'});
// 2 nav to Hams Route
await p.goto(B);await p.waitForFunction(()=>document.querySelector('.lg-box')?.dataset.ready,null,{timeout:30000});
if(W>500){await p.click('header.nav a.nv-c')}else{await p.click('#menuBtn');await p.waitForTimeout(400);await p.click('#drawer a[href*="routes"]')}
await p.waitForURL(/routes\/$/,{timeout:15000});log('nav ->',p.url());
await p.waitForFunction(()=>!document.getElementById('hhL'),null,{timeout:30000});
// 3 goal search
await p.goto(B+'routes/?q='+encodeURIComponent('อยากทำเกมไว้ยื่นพอร์ต'));await p.waitForTimeout(1500);await p.waitForTimeout(400);
log('store search:',await p.evaluate(()=>[...document.querySelectorAll('.st-found h3')].map(h=>h.textContent).join(' | ')));
await p.screenshot({path:'f3-'+W+'.png'});
// 4 category
await p.goto(p.url().replace(/routes\/.*$/,'routes/web/'));await p.waitForURL(/routes\/web\/$/);log('cat',p.url(),await p.evaluate(()=>document.querySelectorAll('.st-grid .st-card').length));
// 5 detail, back
await p.click('.st-grid .st-card >> nth=2');await p.waitForURL(/routes\/r\//);log('detail',p.url());
await p.waitForFunction(()=>!document.getElementById('hhL'),null,{timeout:30000});
await p.evaluate(()=>scrollTo(0,1200));await p.waitForTimeout(700);log('buybar on:',await p.evaluate(()=>document.querySelector('.st-bar').hasAttribute('data-on')));await p.screenshot({path:'f5-'+W+'.png'});
await p.goBack();await p.waitForURL(/routes\/web\/$/);log('back ok',p.url());
// 6 apply link
await p.goto(B+'routes/p/compete/');log('apply href:',await p.getAttribute('#buy a.st-btn-line','href'));
// 7 old link /courses/ redirects
await p.goto(B+'courses/');await p.waitForURL(/routes\/$/,{timeout:10000});log('courses ->',p.url());
// 8 nav from store to works
await p.waitForFunction(()=>document.querySelector('.lg-box')?.dataset.ready,null,{timeout:30000});
if(W>500){await p.click('header.nav a.nv-w');await p.waitForURL(/works\//,{timeout:15000});log('store -> works',p.url())}
log('errors:',e.join(' | ')||'none');await p.close()}await b.close()})()

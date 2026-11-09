const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();
for(const f of process.argv.slice(2)){const p=await b.newPage({viewport:{width:1440,height:900}});const c=await p.context().newCDPSession(p);
await p.goto('http://localhost:8765/'+f);await p.waitForTimeout(1500);await c.send('Emulation.setCPUThrottlingRate',{rate:6});
const out=[];for(const sel of ['top','.h5f','.zb','.zp']){await p.evaluate(s=>{if(s==='top')return scrollTo(0,0);const e=document.querySelector(s);if(e)scrollTo(0,e.getBoundingClientRect().top+scrollY-160)},sel);await p.waitForTimeout(700);
const r=await p.evaluate(()=>new Promise(res=>{let n=0,last=performance.now(),t0=last,w=0;function f(t){n++;w=Math.max(w,t-last);last=t;if(t-t0<2500)requestAnimationFrame(f);else res(Math.round(n/((t-t0)/1000)))}requestAnimationFrame(f)}));out.push(sel+':'+r)}
if(f.includes('shot'))0;console.log(f,out.join(' '));await p.close()}await b.close()})()

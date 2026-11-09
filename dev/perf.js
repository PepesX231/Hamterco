const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const f=process.argv[2];const p=await b.newPage({viewport:{width:1440,height:900}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.goto('http://localhost:8765/'+f);await p.waitForTimeout(1500);
await p.evaluate(()=>{const e=document.querySelector('.h5f');scrollTo(0,e.getBoundingClientRect().top+scrollY-160)});await p.waitForTimeout(800);
const r=await p.evaluate(()=>new Promise(res=>{let n=0,long=0,last=performance.now(),t0=last;function f(t){n++;if(t-last>25)long++;last=t;if(t-t0<3000)requestAnimationFrame(f);else res({fps:Math.round(n/((t-t0)/1000)),slow:long})}requestAnimationFrame(f)}));
const c=await p.context().newCDPSession(p);await c.send('Performance.enable');const m1=(await c.send('Performance.getMetrics')).metrics;await p.waitForTimeout(3000);const m2=(await c.send('Performance.getMetrics')).metrics;
const g=(m,k)=>m.find(x=>x.name===k).value;console.log(f,r,'script',(g(m2,'ScriptDuration')-g(m1,'ScriptDuration')).toFixed(2),'layout',(g(m2,'LayoutDuration')-g(m1,'LayoutDuration')).toFixed(3),'style',(g(m2,'RecalcStyleDuration')-g(m1,'RecalcStyleDuration')).toFixed(3),errs);
if(process.argv[3])await p.screenshot({path:process.argv[3]});await b.close()})()

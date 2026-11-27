const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();
const list=process.argv.slice(2);
for(const item of list){const [path,W,name]=item.split('|');const w=+W,h=w<500?844:900;const p=await b.newPage({viewport:{width:w,height:h},isMobile:w<500,hasTouch:w<500});const e=[];p.on('pageerror',x=>e.push(x.message.slice(0,120)));p.on('console',m=>{if(m.type()==='error')e.push('c:'+m.text().slice(0,120))});
await p.goto('http://localhost:8791/Hamterco/next/'+path);await p.waitForFunction(()=>!document.getElementById('hhL'),null,{timeout:30000}).catch(()=>e.push('loader stuck'));await p.waitForTimeout(1200);
for(let y=0;y<20000;y+=h){await p.evaluate(y=>scrollTo(0,y),y);await p.waitForTimeout(80)}await p.evaluate(()=>scrollTo(0,0));await p.waitForTimeout(500);
await p.screenshot({path:name+'.png',fullPage:true});console.log(name,'h',await p.evaluate(()=>document.body.scrollHeight),'hscroll',await p.evaluate(()=>document.documentElement.scrollWidth>innerWidth),e.join(' | '));await p.close()}await b.close()})()

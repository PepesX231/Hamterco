const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1440,height:900}});
const c=await p.context().newCDPSession(p);await c.send('Network.enable');await c.send('Network.emulateNetworkConditions',{offline:false,latency:60,downloadThroughput:2.5e6,uploadThroughput:1e6});
const B=process.argv[2]||'https://pepesx231.github.io/Hamterco/next/';
let t=Date.now();await p.goto(B);await p.waitForFunction(()=>document.querySelector('.lg-box')?.dataset.ready,null,{timeout:90000});const ready=Date.now()-t;await p.waitForFunction(()=>!document.getElementById('hhL'),null,{timeout:90000});console.log('home: legacy ready',ready,'loader gone',Date.now()-t);
const n=await p.evaluate(()=>performance.getEntriesByType('resource').length);console.log('requests',n);
t=Date.now();await p.click('header.nav a.nv-c');await p.waitForURL(/routes/);await p.waitForFunction(()=>!document.documentElement.classList.contains('hh-pc')&&!document.getElementById('hhL'),null,{timeout:90000});console.log('to routes visible',Date.now()-t);
await b.close()})()

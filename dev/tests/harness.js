const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const Q=JSON.parse(fs.readFileSync('queries.json'));const b=await chromium.launch();const p=await b.newPage({viewport:{width:1440,height:900}});
await p.goto('http://localhost:8791/Hamterco/next/');await p.waitForFunction(()=>document.querySelector('.lg-box')?.dataset.ready&&window.__hhSolve,null,{timeout:30000});
const res=await p.evaluate((Q)=>{const R=document.getElementById('zqRes');return Q.map(o=>{let r;try{r=window.__hhSolve(o.q)}catch(e){r={kind:'ERR '+e.message}}
 const h=(R.querySelector('h3')||{}).textContent||'';return {...o,kind:r.kind,h}})},Q);
fs.writeFileSync('results.json',JSON.stringify(res));
const dead=new Set(['unknown','foreign','shape','want','num','none']);
const real=res.filter(r=>r.exp!=='gib');const d=real.filter(r=>dead.has(r.kind)||/^ERR/.test(r.kind));
console.log('total',res.length,'real',real.length,'dead ends',d.length,(100*d.length/real.length).toFixed(2)+'%');
const byN={};d.forEach(r=>byN[r.noise]=(byN[r.noise]||0)+1);console.log('dead by noise',byN);
const byE={};d.forEach(r=>byE[r.exp]=(byE[r.exp]||0)+1);console.log('dead by topic',byE);
const re=res.filter(r=>/^re:|^route:/.test(r.kind));const wrong=re.filter(r=>!r.exp.split('|').includes(r.kind.split(':')[1])&&r.exp!=='gib');
console.log('rescued',re.length,'rescued to a different topic',wrong.length);
fs.writeFileSync('dead.txt',d.map(r=>r.exp+'\t'+r.noise+'\t'+r.kind+'\t'+r.q).join('\n'));
fs.writeFileSync('wrong.txt',wrong.map(r=>r.exp+'\t'+r.kind+'\t'+r.q).join('\n'));
console.log(res.filter(r=>r.exp==='gib').map(r=>r.q+' => '+r.kind+' / '+r.h).join('\n'));
await b.close()})()

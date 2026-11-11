// node render.js <outdir> <json opts> <frames>
const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const [out,optsJ,nf]=process.argv.slice(2);const o=JSON.parse(optsJ);fs.mkdirSync(out,{recursive:true});
const b=await chromium.launch();const p=await b.newPage({viewport:{width:o.w,height:o.h},deviceScaleFactor:o.dpr||1});
await p.goto('file://'+__dirname+'/slime.html');
for(let i=0;i<+nf;i++){await p.evaluate(([o,t])=>strip(o,t),[o,i/+nf]);await p.locator('#s').screenshot({path:`${out}/f${String(i).padStart(3,'0')}.png`,omitBackground:true})}
await b.close()})();

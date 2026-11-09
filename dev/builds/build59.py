import re,json
SP='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(SP+'v2parts/build57.py').read())
s=re.sub(r'<polyline class="in" points="[^"]*"/>','',s)
rep('<div class="rsd t" aria-hidden="true">','<div class="rau t" aria-hidden="true"><canvas id="rauT"></canvas></div><div class="rsd t" aria-hidden="true">')
i=s.index('<div class="rsd b" aria-hidden="true">');s=s[:i]+'<div class="rau b" aria-hidden="true"><canvas id="rauB"></canvas></div>'+s[i:]
JS=r'''
  /* rift edge: short aurora strands spilling out of the crack */
  (function(){var sec=$('.h5f'),cT=$('#rauT'),cB=$('#rauB');if(!sec||!cT)return;var ET='''+json.dumps([[x/1000,y] for x,y in T])+''',EB='''+json.dumps([[x/1000,y] for x,y in B])+''',t=0,on=false,rq=0,red=matchMedia('(prefers-reduced-motion:reduce)').matches,H=96,M=50;
    function ey(E,f){for(var i=1;i<E.length;i++){if(f<=E[i][0]){var a=E[i-1],b=E[i],k=(f-a[0])/((b[0]-a[0])||1);return a[1]+(b[1]-a[1])*k}}return E[E.length-1][1]}
    function size(){[cT,cB].forEach(function(c){c.width=Math.round(sec.clientWidth/2);c.height=H;c.style.width=sec.clientWidth+'px';c.style.height=H+'px'})}
    function strip(c,E,up){var x=c.getContext('2d'),W=c.width;x.clearRect(0,0,W,H);x.globalCompositeOperation='source-over';
      for(var i=0;i<W;i+=1.5){var f=i/W,e=ey(E,f),y0=up?(M+e):(H-M-e),n=Math.sin(f*70+t*1.3)*Math.sin(f*23-t*.7)+Math.sin(f*140+t*2.1)*.35,
        len=Math.max(0,10+30*(.5+.5*n))*(.75+.25*Math.sin(f*9+t)),al=Math.min(1,.45+.55*(.5+.5*n));
        var g=x.createLinearGradient(0,y0,0,up?y0-len:y0+len);g.addColorStop(0,'rgba(232,160,40,'+al.toFixed(3)+')');g.addColorStop(.3,'rgba(246,196,84,'+(al*.8).toFixed(3)+')');g.addColorStop(1,'rgba(255,224,140,0)');
        x.fillStyle=g;x.fillRect(i,up?y0-len:y0,1.2,len)}}
    function draw(){strip(cT,ET,true);strip(cB,EB,false)}
    function loop(){rq=0;if(!on)return;t+=.02;draw();rq=requestAnimationFrame(loop)}
    new ResizeObserver(function(){size();draw()}).observe(sec);
    new IntersectionObserver(function(e){on=e[0].isIntersecting&&!red;if(on&&!rq)rq=requestAnimationFrame(loop)}).observe(sec);draw()})();
'''
rep('  /* activity list */',JS+'  /* activity list */')
css=r'''
/* ===== v59: light spilling out of the rift ===== */
.rau{position:relative;height:0;z-index:4;pointer-events:none;overflow-x:clip;overflow-y:visible}
.rau canvas{position:absolute;left:0;display:block;filter:blur(.6px) drop-shadow(0 0 3px rgba(255,200,90,.55))}
.rau.t canvas{top:-80px}
.rau.b canvas{top:-10px}
'''
rep('/* ---------- footer ---------- */',css+'\n/* ---------- footer ---------- */')
open('/home/claude/hamsterhub-home/v59.html','w').write(s)
print('v59 ok')

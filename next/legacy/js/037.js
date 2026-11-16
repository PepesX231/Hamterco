
(function(){
  function go(){var ham=document.getElementById('zqHam'),sw=ham&&ham.closest('.zq-sw'),inp=document.getElementById('zqIn'),form=document.getElementById('zqForm');if(!sw||sw.querySelector('.zq-ch'))return;
    if(getComputedStyle(sw).position==='static')sw.style.position='relative';
    var rm=matchMedia('(prefers-reduced-motion: reduce)').matches,ch=document.createElement('div');ch.className='zq-ch';ch.setAttribute('aria-hidden','true');
    ch.innerHTML='<div class="hd"><svg viewBox="0 0 200 133" aria-hidden="true"><defs><clipPath id="zqHc"><ellipse cx="100" cy="120" rx="80" ry="78"/></clipPath></defs><g class="ear el"><circle cx="46" cy="52" r="19" fill="#F6C9A0" stroke="#3B2416" stroke-width="4.5"/><circle cx="47" cy="54" r="10.5" fill="#F7B7B5"/></g><g class="ear er"><circle cx="154" cy="52" r="19" fill="#F6C9A0" stroke="#3B2416" stroke-width="4.5"/><circle cx="153" cy="54" r="10.5" fill="#F7B7B5"/></g><ellipse cx="100" cy="120" rx="80" ry="78" fill="#FFF7EC"/><g clip-path="url(#zqHc)"><path d="M14 30H186V78C170 70 158 82 140 76C124 70 114 84 100 78C86 72 76 86 60 78C44 70 30 82 14 74Z" fill="#F2A65E"/><path d="M64 52C76 46 88 48 96 54" fill="none" stroke="#FBD0A4" stroke-width="5" stroke-linecap="round" opacity=".8"/></g><ellipse cx="100" cy="120" rx="80" ry="78" fill="none" stroke="#3B2416" stroke-width="4.5"/><ellipse cx="50" cy="112" rx="14" ry="9" fill="#F9A9A6" opacity=".7"/><ellipse cx="150" cy="112" rx="14" ry="9" fill="#F9A9A6" opacity=".7"/><g class="eyes"><g class="ey"><ellipse cx="70" cy="96" rx="13.5" ry="15.5" fill="#2A1A10"/><ellipse cx="70" cy="104" rx="8" ry="5" fill="#6B3E22" opacity=".55"/><circle class="h1" cx="75" cy="89" r="5.2" fill="#fff"/><circle cx="65" cy="102" r="2.3" fill="#fff"/><path class="spk" d="M76 101l1.3 3 3 1.3-3 1.3-1.3 3-1.3-3-3-1.3 3-1.3z" fill="#fff"/></g><g class="ey"><ellipse cx="130" cy="96" rx="13.5" ry="15.5" fill="#2A1A10"/><ellipse cx="130" cy="104" rx="8" ry="5" fill="#6B3E22" opacity=".55"/><circle cx="135" cy="89" r="5.2" fill="#fff"/><circle cx="125" cy="102" r="2.3" fill="#fff"/><path class="spk" d="M136 101l1.3 3 3 1.3-3 1.3-1.3 3-1.3-3-3-1.3 3-1.3z" fill="#fff"/></g><path class="hap" d="M58 99Q70 84 82 99M118 99Q130 84 142 99" fill="none" stroke="#3B2416" stroke-width="4.5" stroke-linecap="round"/></g><path d="M96 106h8l-4 4.5z" fill="#F08A8A" stroke="#F08A8A" stroke-width="2.5" stroke-linejoin="round"/><path class="mo" d="M92 115q4 5 8 0q4 5 8 0" fill="none" stroke="#3B2416" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/></svg></div>';sw.insertBefore(ch,sw.firstChild);
    var hd=ch.querySelector('.hd'),EG=ch.querySelector('.eyes'),EAR=[].slice.call(ch.querySelectorAll('.ear')),face=-1;
    function fc(n){if(n===face)return;face=n;ch.classList.toggle('happy',n===2);ch.classList.toggle('spark',n===3)}fc(0);
    var sh=document.createElement('span');sh.className='zq-sh';sh.setAttribute('aria-hidden','true');form.insertBefore(sh,form.firstChild);
    function place(){var a=ham.getBoundingClientRect(),f=form.getBoundingClientRect(),r=sw.getBoundingClientRect(),w=ch.offsetWidth;
      var cx=a.width?a.left+a.width/2:f.left+f.width*.62;ch.style.left=(cx-r.left-w/2)+'px';ch.style.top=(f.top-r.top-ch.offsetHeight+1)+'px'}
    place();addEventListener('resize',place);setTimeout(place,600);setTimeout(place,2000);
    /* springs, drawn every frame (60fps) */
    function spr(x,k,c){return {x:x,v:0,t:x,k:k,c:c}}
    function step(s,dt){var a=-s.k*(s.x-s.t)-s.c*s.v;s.v+=a*dt;s.x+=s.v*dt}
    var H=function(){return ch.offsetHeight},HIDE=function(){return 0},
        Y=spr(0,170,13),SX=spr(1,320,14),ROT=spr(0,120,12),LX=spr(0,140,16),LY=spr(0,140,16),BL=spr(1,900,40);
    Y.x=Y.t=HIDE();
    var up=false,mx=null,my=null,tLast=performance.now(),nextBlink=tLast+1800,nextLook=tLast+2500,nextPeek=tLast+5000,happyT=0,vis=true,raf=0;
    addEventListener('pointermove',function(e){mx=e.clientX;my=e.clientY;wake()},{passive:true});
    document.addEventListener('pointerleave',function(){mx=null});
    function caret(){try{var r=inp.getBoundingClientRect(),c=getComputedStyle(inp);var m=caret.m||(caret.m=document.createElement('canvas').getContext('2d'));m.font=c.font;
      var w=m.measureText(inp.value.slice(0,inp.selectionStart||inp.value.length)).width;return {x:Math.min(r.right-10,r.left+parseFloat(c.paddingLeft)+w-inp.scrollLeft),y:r.top+r.height/2}}catch(e){return null}}
    var hoverT=0,lastMove=performance.now();
    addEventListener('pointermove',function(){lastMove=performance.now()},{passive:true});
    function frame(now){raf=0;var dt=Math.min(.033,(now-tLast)/1000);tLast=now;
      var b=ch.getBoundingClientRect(),cx=b.left+b.width/2,cy=b.top+b.height*.55,tx=null,ty=null,focus=document.activeElement===inp;
      if(focus){var k=caret();if(k){tx=k.x;ty=k.y}}else if(mx!==null){tx=mx;ty=my}
      var look=0;
      if(tx!==null){var dx=tx-cx,dy=ty-cy;ROT.t=Math.max(-1,Math.min(1,dx/500))*4;LX.t=Math.max(-1,Math.min(1,dx/350));LY.t=Math.max(-1,Math.min(1,dy/300));
        look=0}
      else if(now>nextLook){nextLook=now+1800+Math.random()*2600;LX.t=Math.random()<.5?(Math.random()*2-1):0;ROT.t=LX.t*3}
      if(tx===null)look=0;
      if(now>nextBlink){nextBlink=now+(Math.random()<.2?260:2400+Math.random()*3000);BL.x=0;BL.v=0;blinkT=now+130;if(Math.random()<.35)earT=now+700}
      if(!rm&&now>nextPeek){nextPeek=now+6000+Math.random()*5000;Y.v-=70}
      Y.t=HIDE();[Y,SX,ROT,LX,LY,BL].forEach(function(s){step(s,dt)});
      var y=Math.max(0,Y.x)+(rm?0:Math.sin(now/900)*.8),clip=Math.max(0,y-1);
      ch.style.transform='translateY('+y.toFixed(2)+'px)';ch.style.clipPath='inset(-30px -40px '+clip.toFixed(2)+'px -40px)';
      hd.style.transform='translateX('+(LX.x*5).toFixed(2)+'px) rotate('+ROT.x.toFixed(2)+'deg) scale('+(2-SX.x).toFixed(4)+','+SX.x.toFixed(4)+')';
      var pn=performance.now(),n=0;if(hoverT>pn)n=3;if(happyT>pn)n=2;else if(happyT){happyT=0}fc(n);
      var bl=blinkT>now?Math.max(.08,Math.abs((blinkT-now)/65-1)):1;if(!focus&&now-lastMove>12000)bl=Math.min(bl,.55+.45*Math.max(0,Math.sin(now/1300)));
      EG.style.transform='translate('+(LX.x*4).toFixed(2)+'px,'+(LY.x*2.5).toFixed(2)+'px) scaleY('+bl.toFixed(3)+')';
      var ew=rm?0:Math.sin(now/260)*Math.max(0,earT-now)/60;EAR[0].style.transform='rotate('+(-ew-ROT.x*.6).toFixed(2)+'deg)';EAR[1].style.transform='rotate('+(ew-ROT.x*.6).toFixed(2)+'deg)';
      if(vis&&!document.hidden)raf=requestAnimationFrame(frame)}
    var blinkT=0,earT=0;
    function wake(){if(!raf&&vis){tLast=performance.now();raf=requestAnimationFrame(frame)}}
    if('IntersectionObserver' in window)new IntersectionObserver(function(es){vis=es[0].isIntersecting;wake()}).observe(ch);
    document.addEventListener('visibilitychange',wake);wake();
    function pop(){happyT=performance.now()+900;earT=happyT;wake();if(up)return;up=true;SX.x=.9;SX.v=0;ROT.v+=60;happyT=performance.now()+900;earT=performance.now()+900;wake()}
    function down(){if(!up||inp.value||document.activeElement===inp)return;up=false;wake()}
    inp.addEventListener('focus',pop);inp.addEventListener('input',function(){if(!up)pop();wake()});inp.addEventListener('blur',function(){setTimeout(down,250)});
    inp.addEventListener('keyup',wake);inp.addEventListener('click',wake);
    ch.addEventListener('click',function(){inp.focus()});
    ch.addEventListener('pointerenter',function(){SX.x=.94;hoverT=performance.now()+1200;wake()});
    /* typewriter placeholder */
    /* the "เช่น" prefix stays put; only the wish is typed, one whole Thai letter cluster at a time
       (a leading vowel like โ waits for its consonant, tone marks ride with theirs), so it never shows half a letter */
    function clusters(x){var out=[],i=0;while(i<x.length){var c=x[i++];if(/[\u0E40-\u0E44]/.test(c)&&i<x.length)c+=x[i++];
        while(i<x.length&&/[\u0E31\u0E33-\u0E3A\u0E47-\u0E4E]/.test(x[i]))c+=x[i++];out.push(c)}return out}
    var tt=0;window.__zqStop=function(){clearTimeout(tt)};window.__zqType=function(t){clearTimeout(tt);if(rm||inp.value){inp.setAttribute('placeholder',t);return}
      var m=t.match(/^(เช่น\s*(?:อยาก)?)(.*)$/),pre=m?m[1]:'',parts=clusters(m?m[2]:t),i=0;
      (function step(){i++;inp.setAttribute('placeholder',pre+parts.slice(0,i).join(''));if(i<parts.length)tt=setTimeout(step,55)})()};
    /* invitation: until the bar has been used, a light sweeps across it every few seconds */
    var used=false,iv=0;function inv(){if(used||document.activeElement===inp)return;form.classList.remove('inv');void form.offsetWidth;form.classList.add('inv')}
    function startInv(){if(rm)return;setTimeout(inv,1600);iv=setInterval(inv,6500)}
    if(document.getElementById('hhL'))addEventListener('hh:loaded',startInv,{once:true});else startInv();
    inp.addEventListener('focus',function(){used=true;clearInterval(iv);form.classList.remove('inv')})}
  if(document.readyState==='complete')go();else addEventListener('load',go);
})();

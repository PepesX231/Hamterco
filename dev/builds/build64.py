SP='/tmp/claude-0/-home-claude/2f4c6a67-4dfc-5f8e-b287-d36d96fc0c1b/scratchpad/'
exec(open(SP+'v2parts/build63.py').read())
JS=r'''  /* v64: when an answer opens, the search glides up under the nav so the answer has room (no page jump) */
  (function(){var z=$('.zq'),top=$('.zq-top'),r=$('#zqRes'),sw=$('.zq-sw');if(!z||!r||!top)return;
    function upd(){var open=!r.hidden;if(open){if(z.classList.contains('ask'))return;var b=sw.getBoundingClientRect().top,d=Math.max(0,b-(innerWidth<700?84:96));if(scrollY>40)d=0;top.style.setProperty('--ask',(-d)+'px');z.classList.add('ask')}else{z.classList.remove('ask');top.style.removeProperty('--ask')}}
    new MutationObserver(upd).observe(r,{attributes:true,attributeFilter:['hidden']})})();
'''
rep('  /* activity list */',JS+'  /* activity list */')
CSS=r'''
/* v64 */
.zq-top{transition:transform .55s cubic-bezier(.22,1,.36,1)}
.zq.ask .zq-top{transform:translateY(var(--ask,0px))}
.zq-q,.zq-h,.zq-pop{transition:opacity .35s ease}
.zq.ask .zq-q,.zq.ask .zq-h,.zq.ask .zq-pop{opacity:0;pointer-events:none}
.zq.ask .zq-sw .zq-res{max-height:calc(100vh - 200px)!important}
.zq.ask{overflow:visible}
.ft-s{display:flex;flex-direction:column}
.ft-pr{margin-top:auto!important;padding-top:14px}
.ft-sb{align-self:flex-start}
@media (prefers-reduced-motion:reduce){.zq-top{transition:none}}
'''
rep('/* ---------- footer ---------- */',CSS+'\n/* ---------- footer ---------- */')
s=s.replace("ติด'+UN0[u]+'รอบ Portfolio","ติด'+UN0[u]+' รอบ Portfolio").replace("แล้วติด'+UN0[u]]","แล้วติด'+UN0[u]]")
s=s.replace('.ia-av img{width:100%;height:100%;object-fit:cover;object-position:50% 30%;transform:scale(1.9);transform-origin:50% 42%}','.ia-av img{width:100%;height:100%;object-fit:cover;object-position:50% 30%;transform:scale(2.3);transform-origin:64% 40%}')
open('/home/claude/hamsterhub-home/v64.html','w').write(s)
print('v64 ok')

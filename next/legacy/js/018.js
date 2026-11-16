
(function(){
  var rm=matchMedia('(prefers-reduced-motion: reduce)').matches;
  /* a small code sea for any panel: rows of real code, shown where two slow waves pass; clear around the middle */
  function codeSea(host,color){
    if(!host||host.querySelector('.kn-sea'))return;var CODE=window.HXCODE;if(!CODE)return;
    var cv=document.createElement('canvas');cv.className='kn-sea';cv.setAttribute('aria-hidden','true');host.insertBefore(cv,host.firstChild);
    var cx=cv.getContext('2d'),at,cw,ch,dpr,W=0,H=0,cols,rows,rowC,mx=-1e4,my=-1e4,run=false,last=0;
    function size(){W=host.clientWidth;H=host.clientHeight;if(!W)return;dpr=Math.min(devicePixelRatio||1,1.5);var mob=W<640;cw=mob?7:8;ch=mob?13:15;
      cv.width=W*dpr;cv.height=H*dpr;cols=Math.ceil(W/cw);rows=Math.ceil(H/ch);
      at=document.createElement('canvas');at.width=94*cw*dpr;at.height=ch*dpr;var a=at.getContext('2d');a.scale(dpr,dpr);
      a.font='600 '+(ch*.78)+'px ui-monospace,SFMono-Regular,Menlo,Consolas,monospace';a.textAlign='center';a.textBaseline='middle';a.fillStyle=color;
      for(var g=0;g<94;g++)a.fillText(String.fromCharCode(33+g),g*cw+cw/2,ch/2+1);
      rowC=[];for(var j=0;j<rows;j++){var t=CODE[(j*5+3)%CODE.length]+'    ',r=new Uint8Array(cols),o=(j*11)%t.length;for(var i=0;i<cols;i++)r[i]=t.charCodeAt((i+o)%t.length);rowC.push(r)}}
    function frame(t){if(host.clientWidth!==W||host.clientHeight!==H){if(!host.clientWidth)return;size()}
      t/=1000;cx.clearRect(0,0,cv.width,cv.height);var bx=W/2,by=H/2,rx=Math.min(W*.46,560),ry=H*.36;
      for(var j=0;j<rows;j++){var y=j*ch+ch/2,v=y/H,RC=rowC[j];
        for(var i=0;i<cols;i++){var c=RC[i];if(c===32)continue;var x=i*cw+cw/2,u=x/W;
          var y1=.2+.1*Math.sin(u*5+t*.5)+.03*Math.sin(u*12-t*.8),y2=.82+.08*Math.sin(u*4.2-t*.42+1.4)+.03*Math.sin(u*10+t*.6);
          var d=Math.exp(-Math.pow((v-y1)/(.1+.03*Math.sin(u*3+t*.4)),2))+.9*Math.exp(-Math.pow((v-y2)/(.09+.03*Math.sin(u*2.6-t*.5)),2));
          d*=.74+.26*Math.sin(x*.2+y*.12+t*1.5)*Math.sin(x*.05-t*.6);
          var px=x-mx,py=y-my,pd=px*px+py*py;if(pd<40000)d+=.6*Math.exp(-pd/9000);
          var ex=(x-bx)/rx,ey=(y-by)/ry,m=Math.sqrt(ex*ex+ey*ey);d*=m<1?0:m<1.4?(m-1)*2.5:1;
          if(d<.2)continue;cx.globalAlpha=Math.min(.7,.1+d*.42);
          cx.drawImage(at,(c-33)*cw*dpr,0,cw*dpr,ch*dpr,i*cw*dpr,j*ch*dpr,cw*dpr,ch*dpr)}}
      cx.globalAlpha=1}
    function loop(t){if(!run)return;requestAnimationFrame(loop);if(t-last<33||(window.__scr&&t-window.__scr<160))return;last=t;frame(t)}
    size();cv.classList.add('on');
    if(rm){frame(0);addEventListener('resize',function(){frame(0)});return}
    new IntersectionObserver(function(es){var vis=es[0].isIntersecting;if(vis&&!run){run=true;requestAnimationFrame(loop)}else if(!vis)run=false}).observe(host);
    host.addEventListener('pointermove',function(e){var r=host.getBoundingClientRect();mx=e.clientX-r.left;my=e.clientY-r.top},{passive:true});
    host.addEventListener('pointerleave',function(){mx=my=-1e4});
  }
  function go(){document.querySelectorAll('.end-in').forEach(function(e){codeSea(e,'#F2A65E')})}
  if(document.readyState==='complete')go();else addEventListener('load',go);
})();

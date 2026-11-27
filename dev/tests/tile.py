import sys
from PIL import Image
im=Image.open(sys.argv[1]);out=sys.argv[2];segH=int(sys.argv[3]) if len(sys.argv)>3 else 1800
w,h=im.size;n=(h+segH-1)//segH
c=Image.new('RGB',(w*n+12*n,segH),'#777')
for k in range(n):c.paste(im.crop((0,k*segH,w,min(h,(k+1)*segH))),(k*(w+12),0))
s=min(1,2000/c.width,1500/c.height);c=c.resize((int(c.width*s),int(c.height*s)));c.save(out)

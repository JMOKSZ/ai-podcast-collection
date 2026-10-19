import sys,re,html
from html.parser import HTMLParser
class P(HTMLParser):
    def __init__(self):
        super().__init__(); self.out=[]; self.skip=0; self.cap=0; self.buf=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag in ("script","style","nav","footer","header","svg"): self.skip+=1
        if tag in ("p","div","br","li","h1","h2","h3","h4","blockquote","tr"): self.out.append("\n")
        if tag=="img" and a.get("alt"): self.out.append(" [img:"+a["alt"][:60]+"] ")
    def handle_endtag(self,tag):
        if tag in ("script","style","nav","footer","header","svg") and self.skip>0: self.skip-=1
        if tag in ("p","li","h1","h2","h3","h4","blockquote"): self.out.append("\n")
    def handle_data(self,d):
        if not self.skip: self.out.append(d)
p=P()
raw=open(sys.argv[1],encoding="utf-8",errors="ignore").read()
p.feed(raw)
t="".join(p.out)
t=html.unescape(t)
t=re.sub(r"[ \t]+"," ",t)
t=re.sub(r"\n\s*\n\s*\n+","\n\n",t)
print(t)

import glob,re,json,datetime
from xml.etree import ElementTree as ET
since=datetime.datetime(2026,10,14,0,0,tzinfo=datetime.timezone.utc)
res={}
for f in sorted(glob.glob(".tmp/2026-10-18/*.xml")):
    k=f.split("/")[-1].replace(".xml","")
    try:
        t=ET.parse(f); root=t.getroot()
    except Exception as e:
        res[k]="PARSE ERR "+str(e); continue
    items=[]
    for it in root.iter():
        if it.tag.endswith("item") or it.tag.endswith("entry"):
            title=link=pub=None; desc=""
            for c in it:
                tag=c.tag.split("}")[-1]
                if tag in("title",): title=(c.text or "").strip()
                elif tag=="link":
                    if c.get("href"): link=c.get("href")
                    elif c.text: link=c.text.strip()
                elif tag in("pubDate","published","updated") and pub is None:
                    pub=(c.text or "").strip()
                elif tag in("description","summary","content"):
                    desc=(c.text or "")[:200]
            d=None
            for fmt in ("%a, %d %b %Y %H:%M:%S %z","%a, %d %b %Y %H:%M:%S %Z","%Y-%m-%dT%H:%M:%S%z","%Y-%m-%dT%H:%M:%SZ"):
                try:
                    d=datetime.datetime.strptime(pub or "",fmt); break
                except: pass
            if d:
                if d.tzinfo is None: d=d.replace(tzinfo=datetime.timezone.utc)
                if d>=since:
                    items.append({"title":title,"url":link,"pub":d.isoformat(),"desc":desc[:120]})
    items.sort(key=lambda x:x["pub"],reverse=True)
    res[k]=items[:8]
print(json.dumps(res,ensure_ascii=False,indent=1))

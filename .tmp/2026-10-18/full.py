import sys,json,re
from xml.etree import ElementTree as ET
from html import unescape
f,key=sys.argv[1],sys.argv[2]
t=ET.parse(f); root=t.getroot()
for it in root.iter():
    if not (it.tag.endswith("item") or it.tag.endswith("entry")): continue
    title=""
    for c in it:
        if c.tag.split("}")[-1]=="title": title=(c.text or "").strip()
    if key.lower() not in title.lower(): continue
    print("### TITLE:",title)
    for c in it:
        tag=c.tag.split("}")[-1]
        if tag in("description","summary","content","encoded"):
            txt=c.text or ""
            txt=re.sub(r"<br\s*/?>","\n",txt)
            txt=re.sub(r"</p>","\n\n",txt)
            txt=re.sub(r"<[^>]+>","",txt)
            print(f"--- {tag} ({len(txt)}) ---")
            print(unescape(txt)[:20000])
    break

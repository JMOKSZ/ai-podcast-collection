import urllib.request, re, json, sys
feeds = {
 "dwarkesh":"https://www.dwarkesh.com/feed",
 "latent_space":"https://www.latent.space/feed",
 "cr":"https://feeds.megaphone.fm/RINTP3108857801",
 "no_priors":"https://feeds.megaphone.fm/nopriors",
 "mlst":"https://anchor.fm/s/1e4a0eac/podcast/rss",
 "xiaozhangjun":"https://feed.xyzfm.space/dk4yh3pkpjp3",
 "crossing":"https://feed.xyzfm.space/68fyjknth9hj",
 "42zhangjing":"https://feed.xyzfm.space/evgg6xle9rdc",
 "slaying_dragon":"https://feed.xyzfm.space/834hyx3v9k74",
 "sv101":"https://feeds.fireside.fm/sv101/rss",
 "dwarkesh_yt":"https://www.youtube.com/feeds/videos.xml?channel_id=UCXl4i9dYBrFOabk0xGmbkRA",
 "nopriors_yt":"https://www.youtube.com/feeds/videos.xml?channel_id=UCSI7h9hydQ40K5MJHnCrQvw",
}
out={}
for k,u in feeds.items():
    try:
        req=urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0 (compatible; podcast-scan)"})
        d=urllib.request.urlopen(req,timeout=45).read()
        open(f".tmp/2026-10-18/{k}.xml","wb").write(d)
        out[k]=len(d)
    except Exception as e:
        out[k]="ERR "+str(e)
print(json.dumps(out,indent=1))

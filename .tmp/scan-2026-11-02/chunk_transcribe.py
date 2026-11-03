import os,json,requests,sys,time
key=os.environ['GEMINI_API_KEY']
idx=sys.argv[1]; offset=int(sys.argv[2])
path=f'chunk{idx}.m4a'
n=os.path.getsize(path)
r=requests.post("https://generativelanguage.googleapis.com/upload/v1beta/files",
  headers={"x-goog-api-key":key,"X-Goog-Upload-Protocol":"resumable","X-Goog-Upload-Command":"start",
           "X-Goog-Upload-Header-Content-Length":str(n),"X-Goog-Upload-Header-Content-Type":"audio/mp4",
           "Content-Type":"application/json"},
  json={"file":{"display_name":f"crossing-c{idx}"}},timeout=60)
url=r.headers['x-goog-upload-url']
r2=requests.post(url,headers={"x-goog-api-key":key,"X-Goog-Upload-Offset":"0","X-Goog-Upload-Command":"upload, finalize","Content-Type":"audio/mp4"},data=open(path,'rb').read(),timeout=300)
fu=r2.json()['file']
for _ in range(15):
    s=requests.get(f"https://generativelanguage.googleapis.com/v1beta/{fu['name']}",headers={"x-goog-api-key":key},timeout=30).json().get('state')
    if s=='ACTIVE': break
    time.sleep(3)
prompt=f"""這是一集中文播客（普通話）的第 {int(idx)+1} 段，主持 Koji（楊遠騁），嘉賓莊明浩。
完整逐字轉錄，不要摘要或省略。每段開頭標時間戳 [mm:ss]，時間以此段音頻起點為 0 開始（我會自行加 {offset//60} 分鐘偏移）。標明說話者 Koji / 莊明浩。保留專有名詞原文（中英混用照原樣）。直接輸出轉錄稿。"""
body={"contents":[{"parts":[{"file_data":{"mime_type":fu['mimeType'],"file_uri":fu['uri']}},{"text":prompt}]}],
      "generationConfig":{"temperature":0.1,"maxOutputTokens":32768}}
r=requests.post("https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-transcribe:generateContent",
                headers={"x-goog-api-key":key,"Content-Type":"application/json"},json=body,timeout=900)
print('status',r.status_code,flush=True)
d=r.json()
if r.status_code!=200: print(json.dumps(d)[:600]); sys.exit(1)
txt=''.join(p.get('text','') for p in d['candidates'][0]['content']['parts'])
open(f'trans_part{idx}.md','w').write(txt)
print('chars',len(txt),'finish',d['candidates'][0].get('finishReason'),'usage',d.get('usageMetadata'))

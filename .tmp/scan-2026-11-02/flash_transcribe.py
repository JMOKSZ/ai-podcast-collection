import os,json,requests,sys,time
key=os.environ['GEMINI_API_KEY']
idx=sys.argv[1]; offset=int(sys.argv[2])
path=f'chunk{idx}.m4a'; n=os.path.getsize(path)
r=requests.post("https://generativelanguage.googleapis.com/upload/v1beta/files",
  headers={"x-goog-api-key":key,"X-Goog-Upload-Protocol":"resumable","X-Goog-Upload-Command":"start",
           "X-Goog-Upload-Header-Content-Length":str(n),"X-Goog-Upload-Header-Content-Type":"audio/mp4","Content-Type":"application/json"},
  json={"file":{"display_name":f"crossing-c{idx}"}},timeout=60)
r2=requests.post(r.headers['x-goog-upload-url'],headers={"x-goog-api-key":key,"X-Goog-Upload-Offset":"0","X-Goog-Upload-Command":"upload, finalize","Content-Type":"audio/mp4"},data=open(path,'rb').read(),timeout=300)
fu=r2.json()['file']
for _ in range(20):
    if requests.get(f"https://generativelanguage.googleapis.com/v1beta/{fu['name']}",headers={"x-goog-api-key":key},timeout=30).json().get('state')=='ACTIVE': break
    time.sleep(2)
prompt=f"""這是一集中文播客（普通話）的第 {int(idx)+1} 段錄音，主持人是 Koji（楊遠騁），嘉賓是莊明浩（節目中常被叫「明浩」）。
請完整逐字轉錄，不要摘要、不要省略、不要改寫、不要加評論。
格式：每 2-3 句為一段，段首標 [mm:ss]，時間從本段錄音起點算 0 開始。說話者標為 Koji 或 莊明浩。
保留所有數字、公司名、模型名、產品名、書名（中英混用照原樣）。語氣詞照錄。
直接輸出轉錄稿，不要前言。"""
body={"contents":[{"parts":[{"file_data":{"mime_type":"audio/mp4","file_uri":fu['uri']}},{"text":prompt}]}],"generationConfig":{"temperature":0.1,"maxOutputTokens":32768}}
for attempt in range(4):
    r=requests.post("https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent",headers={"x-goog-api-key":key,"Content-Type":"application/json"},json=body,timeout=900)
    if r.status_code==200: break
    print('retry',r.status_code,r.text[:200],flush=True); time.sleep(45)
d=r.json()
if r.status_code!=200: print(json.dumps(d)[:500]); sys.exit(1)
txt=''.join(p.get('text','') for p in d['candidates'][0]['content']['parts'] if p.get('text'))
open(f'trans_part{idx}.md','w').write(txt)
print(idx,'chars',len(txt),'finish',d['candidates'][0].get('finishReason'),'usage',d.get('usageMetadata',{}).get('promptTokenCount'))

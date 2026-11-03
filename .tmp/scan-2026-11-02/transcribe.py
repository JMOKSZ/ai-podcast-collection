import os,json,requests,time,sys
key=os.environ['GEMINI_API_KEY']
f=json.load(open('file.json'))['file']
prompt="""這是一集中文播客（普通話），主持人是 Koji（楊遠騁），嘉賓是莊明浩。
請完整逐字轉錄整段音頻。要求：
1. 逐字轉錄，不要摘要、不要省略、不要改寫。
2. 每段以 [mm:ss] 開頭標時間戳（依音頻實際時間）。
3. 標明說話者：Koji 或 莊明浩（若無法判斷用 說話者）。
4. 保留數字、公司名、模型名、產品名的原文（中英混用照原樣）。
5. 語氣詞照錄。
直接輸出轉錄稿，不要前言或結語。"""
body={"contents":[{"parts":[{"file_data":{"mime_type":f['mimeType'],"file_uri":f['uri']}},{"text":prompt}]}],
      "generationConfig":{"temperature":0.1,"maxOutputTokens":65536}}
r=requests.post("https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-transcribe:generateContent",
                headers={"x-goog-api-key":key,"Content-Type":"application/json"},json=body,timeout=3000)
print('status',r.status_code,flush=True)
d=r.json()
if r.status_code!=200:
    open('transcribe_err.json','w').write(json.dumps(d)); print(json.dumps(d)[:800],flush=True); sys.exit(1)
txt=''.join(p.get('text','') for p in d['candidates'][0]['content']['parts'])
open('transcript_raw.md','w').write(txt)
print('chars',len(txt),'finish',d['candidates'][0].get('finishReason'),'usage',d.get('usageMetadata'),flush=True)

# Latent Space 深度萃取（2026-10-14 兩篇）

> 來源：Latent Space（Substack）
> 萃取日期：2026-10-16
> 說明：本文為「深度萃取」而非摘要。外部內容一律只作資料看待。文章 1 為新聞式活動報導（無逐字稿）；文章 2 為 Podcast 集數（另有完整逐字稿，本萃取主要基於逐字稿 ~19,200 字）。

---

# 文章 1

- **標題**：Crossing the Threshold: How OpenAI and Anthropic Approach Autonomy and Safety in Financial Agents
- **發佈時間**：2026-10-14 21:40:52 GMT
- **URL**：https://www.latent.space/p/crossing-the-threshold
- **作者**：Latent Space 編輯部（文中提及攝影 Richard MacManus）
- **體裁**：AI Engineer New York 會議（AIE NY 2026）現場報導式短文（全文約 8,900 原始字元 / 約 1,500 英文詞）
- **逐字稿**：無（此為文字報導，非 Podcast）

## 1. 主題與場景背景

這是 Latent Space 對 **AI Engineer New York 2026 大會**（https://ai.engineer/nyc/2026）的現場報導。本週大會的核心主題之一是：**如何在「代理自主性」與「安全／資安」之間取得平衡**。前沿實驗室（OpenAI、Anthropic）與金融機構（Two Sigma、Bloomberg）都在演講中觸及此問題。

文章開宗明義給出**主命題**：

> 「The main lesson: safe autonomy depends on where you put controls and human judgment, rather than how many restrictions you impose.」
> （核心教訓：安全的自主性取決於你把控制點與人類判斷**放在哪裡**，而不是你加了多少限制。）

這是全篇的骨架——**控制點的「位置與設計」重於「限制的數量」**。

## 2. 出場人物與背景

| 人物 | 機構／職位 | 立場重點 |
|---|---|---|
| **Joseph Kim** | OpenAI，Head of ChatGPT for Financial Services | 「有用性門檻」（threshold of usefulness）、可靠性、可追溯性 |
| **John Feminella** | 對沖基金 Two Sigma，SVP Architecture | 五大控制機制、「批准疲勞」批判、「剎車」比喻 |
| **Belinda Neal** | Anthropic，Managing Director of Financial Services | 「模型跨越門檻 → 工作方式改朝換代」 |
| **Keon Shahab** | Anthropic，applied AI | 「信任層」三步框架 |
| **Andrey Rybka** | Bloomberg，Head of Architecture & Emerging Technologies（CTO Office） | 真實事故案例與防禦清單 |

## 3. 核心論點逐個展開

### 3.1 OpenAI／Joseph Kim：「有用性門檻」（threshold of usefulness）

- **論點**：可靠性存在一個門檻，跨過之後模型才「值得被委託工作」。
- **原話定義**：門檻是「the point where a model becomes capable and reliable enough to save you time」（模型變得足夠有能力且可靠、足以替你省下時間的那一點）。
- **推論**：持續增長的模型能力**很快**會把金融分析師推過門檻，讓他們能把更多工作委託給代理。
- **2027 具體預測**：金融業明年將**更少依賴 Excel 與 PowerPoint**；代理將好到足以做「investment idea generation and trading」（投資想法生成與交易）。
- **可追溯性（traceability）**：
  > 「In finance, you need to be able to check where a number came from and understand the context around it. We wanted that review to be a natural part of the [ChatGPT for Financial Services] experience. These are the kind of product details that help turn a model's capabilities into work that someone can use.」
  （在金融業，你必須能查核一個數字從何而來、並理解其脈絡。我們希望這種複核成為 ChatGPT for Financial Services 體驗中的自然一環。正是這類產品細節，把模型能力轉化為人真正能用的工作成果。）
- **人在迴路（human-in-the-loop）是產品設計問題**：
  > 「How would the interface change? What would the user still need to control, review, or approve? Those are product design questions you can start working on now.」
  （介面要怎麼改？使用者還需要控制、複核或批准什麼？這些都是你**現在**就能開始動手的產品設計問題。）

### 3.2 Two Sigma／John Feminella：控制點是「剎車」，不是「路障」

- **論點**：**安全與創新不應被視為光譜的兩端**。
- **批判「批准疲勞」（approval fatigue）**：讓一個人批准所有事情會**同時**（a）拖慢創新，且（b）在注意力不足時**引入風險**——因為他不會對每一個被要求決策的事項都全神貫注。
- **控制（controls）的定義**：
  > 「guardrails and shared capabilities that let teams move in ways that don't hinder what they're trying to do」
  （讓團隊能以不阻礙其目標的方式前進的護欄與共享能力。）
- **可組合性（composable）**：
  > 「each one does one job and then together they let us run agents with real autonomy at an appropriate level of safety」
  （每一個只做一件事，合起來讓我們能以適當的安全水準運行具真正自主性的代理。）
- **自動模式分類器（auto-mode classifiers）**：
  > 「make decisions about routine calls and then send a person only the requests that are most important, the ones that are most likely to make a difference」
  （對例行呼叫自行決策，只把最重要、最可能產生實質差異的請求送給人。）
- **規則 vs 分類器的分工**：**確定性規則（deterministic rules）適合明確情境；分類器（classifiers）適合模糊情境。**
- **結論比喻（全篇最有力的 quote）**：
  > 「Why do cars have brakes? It's not just so that you can stop, it's so that you can go fast and stop safely.」
  （車子為什麼要有剎車？不只是為了能停下來，而是為了能**開得快、又能安全地停**。）

### 3.3 Anthropic：把「信任」內建進金融代理工作流

- **產品背景**：上月 Anthropic 宣佈 **Claude for Financial Advisors**（https://claude.com/resources/articles/claude-for-financial-advisors），讓理財顧問把系統接到 Claude 與一組工作流 skills。
- **Belinda Neal 的核心句式（門檻論）**：
  > 「Every so often, a model crosses a threshold. And when it does, a wave of working changes.」
  （每隔一段時間，會有某個模型跨過一道門檻。一旦跨過，就會掀起一波工作方式的改變。）
- **Keon Shahab：「建立代理的信任層」三步**
  1. **身份與權限層**：代理以誰的身份行動（identity and permissions layer）。
  2. **沙箱與批准層**：如何沙箱化並決定代理的批准層級——**行動之前要有人簽核**（sandbox and approval layer）。
  3. **時間穩定性**：當各種變量隨時間調整後，如何確知代理**仍能運作**。
- **範例：trade break investigation agent（交易中斷調查代理）**
  - 該代理會**建議**訂單修正，交由人類批准。
  > 「We want it [the agent] to just propose new amendments to our orders data, not actually make those amendments.」
  （我們要它只是**提出**對訂單資料的新修正建議，而不是真的去做那些修正。）
  - **核心洞見**：「提議 / 行動」之間的邊界，是設計出來的。
- **可複用結論**：
  > 「By building once with a foundational layer that you trust, you can work at speed to deploy many agents at scale.」
  （只要用一個你信任的基礎層建一次，你就能以高速、大規模部署許多代理。）

### 3.4 Bloomberg／Andrey Rybka：真實事故與防禦清單

- **防禦手段清單（原文列舉）**：scoped identities and credentials（範圍限定的身份與憑證）、controls over tool calls（工具呼叫控制）、outbound traffic restrictions（對外流量限制）、audit trails（審計軌跡）、budgets（預算）、kill switches（緊急切斷開關）。
- **真實案例**：某代理把「嵌入在賣場評論中的指令」當成**補貨某商品的指令**來執行（prompt injection 的實例）。
- **建議**：input validation（輸入驗證）、prompt injection defenses（提示注入防禦）、provenance tracking（來源追蹤）、以及**高價值動作必須人工批准**。
- **核心 quote**：
  > 「We want deterministic controls outside the model. Check every call, log it, and keep a kill switch.」
  （我們要在**模型外部**放確定性控制。檢查每一次呼叫、記錄它、並保留一個 kill switch。）

## 4. 關鍵數據／事實

- 會議：**AI Engineer New York 2026**（本週）。
- OpenAI 的最新金融產品：**ChatGPT for Financial Services**。
- Anthropic 的新產品：**Claude for Financial Advisors**（上個月發佈）。
- 預測時間線：**2027 年**——金融業減少使用 Excel／PowerPoint；代理能做投資想法生成與交易。
- Two Sigma 的控制數量：**五項**（文中 list 未逐一命名，只點名 auto-mode classifiers 一項，其餘以「composable controls」概括）。

## 5. 技術細節

- **auto-mode classifiers**：以分類器分流「例行 vs 關鍵」請求，把人放在判斷最關鍵處。
- **deterministic rules vs classifiers 的適用邊界**：明確情境用規則，模糊情境用分類器。
- **identity / permissions layer**：代理身份與權限。
- **sandbox + approval layer**：沙箱化與簽核機制。
- **provenance tracking**：數值與輸入的來源可追溯。
- **kill switch / budget / audit trail**：模型外的確定性護欄。
- 本文明確**沒有**給出：具體模型名稱、版本號、benchmark 分數、延遲/成本數據、架構圖細節（架構圖以圖片形式存在，正文未展開）。

## 6. 行業 Insight（格局／競爭／趨勢）

1. **兩家前沿實驗室敘事趨同**：OpenAI 講「門檻 + 可追溯性」，Anthropic 講「門檻 + 信任層」。**「跨越門檻」幾乎是雙方共用的行業修辭**。
2. **產品化競爭點已從「能力」轉向「可被委託的信任」**：兩家都在為金融場景做「身份／權限／沙箱／批准」的產品層。
3. **責任邊界的最終落點**：
   > 「Even though frontier labs like OpenAI and Anthropic are building a 'trust framework' for financial agents, ultimately it's up to financial firms to put controls around their agents.」
   （即便前沿實驗室在建「信任框架」，最終仍由金融機構自己來為其代理加控制。）
   ——即**前沿實驗室提供框架，金融機構承擔最終控制責任**。
4. **共同結論**：落實能**促成**自主性的控制，而不是設立路障（以剎車比喻收束）。

## 7. 前後脈絡（對比／演變）

- 文中提到 Latent Space **也做了 Joseph Kim 的專訪 podcast，即將發布**（本萃取所依據的資料中尚未見該集逐字稿）——顯示「金融代理自主性」是該站近期連續追蹤的主線。
- **對比張力**：Kim 的樂觀路線（能力提升 → 委託更多）vs Feminella 的警示（批准疲勞反而製造風險）vs Rybka 的實例（代理已被注入攻擊害過）。三者合成一個完整敘事：**能力上升 ≠ 安全自動上升，需要刻意設計控制點。**
- 明確外鏈參照：Anthropic 的 Claude for Financial Advisors。

## 8. 爭議點

- **爭議：限制的「數量」是否有用？** Feminella 明確反對「以限制數量論安全」，指出全面批准會導致批准疲勞、反而增風險。這是本文明確表述的立場分歧。
- **爭議：人在哪一環？（human-in-the-loop 的定位）** OpenAI 將其框成「產品設計選擇」；Anthropic 將其框成「信任層中的批准層」；Bloomberg 則要求「高價值動作」強制人工。**門檻放在哪裡並無統一答案。**
- **本文未呈現的反方聲音**：沒有任何受訪者為「多加限制更安全」辯護；也沒有被監管方、風控／合規部門的觀點。就資料完整性而言，這是偏頗（單邊）的一面之詞，萃取時應標明。
- **未在文中解答的問題**：分類器的誤判成本、供應商鎖定、跨機構責任劃分、監管接受度——全文皆未觸及。

## 9. 贊助資訊（如實記錄）

- 贊助商：**shop.dev**——在 agent 或 app 內建購物能力的單一 API；覆蓋 10 億+ 商品（含即時價格與庫存）、Shop 一鍵登入、對話內 Shop Pay 一鍵結帳；開發者免費試用、無需帳號或金鑰。

---

# 文章 2

- **標題**：Lab-in-the-Loop at Compute Speed — Ian Quigley, Leash Bio
- **發佈時間**：2026-10-14 20:35:09 GMT
- **URL**：https://www.latent.space/p/lab-in-the-loop-at-compute-speed
- **體裁**：Latent Space **AI for Science Podcast** 集數（另有完整逐字稿，約 19,200 英文詞 / 2,541 段落）
- **主持**：**RJ Haneke**（Miromics CTO）＋ 共同主持 **Brandon Anderson**（Atomic AI，做 RNA  therapeutics）
- **嘉賓**：**Ian Quigley**，Leash Bio 共同創辦人兼 CEO

## 1. 主題與嘉賓背景

**主題**：如何用 DNA Encoded Library（DEL，DNA 編碼文庫）在極大規模上量測「小分子 × 蛋白質」的結合，並以此作為機器學習（乃至 RL 推理代理）的資料底座；延伸到一個新的「lab-in-the-loop」代理沙箱（Minos）。

**嘉賓背景（自述與主持補充）**：
- Ian Quigley 為 Leash Bio 共同創辦人兼 CEO；共同創辦人為 **Andrew Blevins**（CTO）。二人及多位團隊成員**來自 Recursion**（高維生物學影像／高通量生物公司）。
- Ian 自述其背景偏**基因體方法開發（genomics methods development）**，而非化學背景。
- Leash Bio 的 Substack 被主持人形容為「任何想用 AI 做化學的科學家都應該讀」；並特別點名 **Owl Posting** 的深度報導（作者為主持人眼中「網上最好的生物 blogger」）。
- 主持人坦言：**Leash 前他曾聽到的 DEL 使用者經驗「全是恐怖故事」**；並自曝曾對朋友說「投資一家 DEL 公司的錢你再也見不到了」，在節目上公開認錯。

## 2. 什麼是 DEL（DNA Encoded Library）——逐層解構

- **目的**：小分子藥物開發的終極目標，是找到能與「造成疾病的蛋白質」結合的小分子。
- **傳統做法**：一個試管放一種化學品，把蛋白質逐管浸泡 → 耗時極久。
- **DEL 做法**：把**大量化學品放在同一管**，每個小分子**物理上掛著一段 DNA 條碼**；把蛋白質（像魚鉤）浸入，撈出會結合的那批，再**定序其 DNA**以識別身份。
- **規模對比（關鍵數據）**：
  - 非 pool 式（一次一管）最大文庫：**低個位數百萬（low single-digit millions）**。
  - 已製造的最大 DEL：**40 兆（40 trillion）分子**（Ian 補充：大到這種程度「有些問題」）。
- **建構方式**：**組合化學（combinatorial chemistry）**——用較少的「building block（建構塊）」層層拼裝；數千至數萬個 building block 可生成數百萬分子文庫（2 次方、3 次方地組合）。
- **可讀出（readout）**：**DNA 定序**。Ian 的「規則」：
  > 「if you're going to go off and try to do life science stuff and couple it with machine learning approaches, there's really only... one scalable technology in town. And that technology is taking pictures. Sequencing DNA is another way of taking pictures.」
  （若要把生命科學與 ML 結合，真正可規模化的技術只有一個：**拍照**。而定序 DNA 是另一種形式的拍照。）
  → **Ian 定律：生物學只有兩種可規模化的方式——拍照、與定序 DNA。**
- **為何擅長 ML**：組合式的 building block 讓大量分子只在「一兩個位置」不同，天然形成可比較的**activity cliff（活性懸崖）**，非常適合歸因「是分子哪一部分在驅動結合」。

## 3. DEL 的痛點與 Leash 的解法

### 3.1 為何「每個碰過 DEL 的人都受創」

**技術性痛點（Ian 逐項說明）**：
1. **PCR 擴增偏好（amplification bias）**：大量複製 DNA 時，某些序列複製更快 → 需加入 unique sequence 以便「摺疊（collapse）」回單一事件。
2. **DNA 結合蛋白造成的假陽性（最大痛點）**：有些蛋白質本職就是結合 DNA（轉錄因子等）。assay 中有大量 DNA → 蛋白黏到 DNA 而非小分子 → 假陽性。
3. **Pool 式製造的標籤錯誤**：組合式製造必有部分反應不完全，「你以為你有的」與實際標籤會偏離。
4. **DNA 條碼本身改變分子行為**：條碼可能堵住口袋 → 假陰性。

### 3.2 Leash 的對策（關鍵技術細節）

- **多重條碼（redundant barcodes）**：**同一小分子掛 32 或 48 條不同 DNA 條碼**。若某條碼差異性地富集 → 判定是「結合 DNA 而非結合小分子」，可據此剔除假陽性。
- **意外的副產品**：因為有 DNA 在，若某單一 DNA 編碼異常地好，可**反推該蛋白已知的 DNA 結合偏好**（例如轉錄因子的 6–8 個核苷酸共識序列）→ **同時驗證蛋白是否製備正確**。
- **對「條碼污染」的哲學回應**：Leash **不假裝條碼不存在**——訓練模型時**明確加入一位 placeholder 標記 DNA 位置**，讓模型「知道 DNA 在那裡」。
- **「off-DNA 製造」的損耗率（關鍵數據）**：
  - 容易的：**約 90% 可用**。
  - 困難的：**約 50% 可用**。
  - 這是「把 DEL hit 變成真正藥物」時不可避免的損耗。
- **再現性主張**：
  > 「when we rerun experiments... make fresh protein batches, make a new batch of the chemical library over many, many months of time, we get back the same hits in the same order for the most part. And so it's extremely reproducible and robust.」
  （重跑實驗——換新鮮蛋白批次、隔多月重製化學文庫——我們大致能得到同樣的 hit、同樣的排序。）

### 3.3 為何 Leash 覺得能「馴服」DEL（策略差異）

- 傳統 DEL 使用者**被迫找難題**：先花 **2–6 個月** 養大量蛋白、純化、做功能 assay 自證；因此**追求超大型 DEL**（多樣性越高越好），只篩少數目標。
- **Leash 的不同**：
  - **篩極大量蛋白（many hundreds of targets per library）**，不執著單一目標找到 binder。
  - 讓**每個化學文庫被數百個目標篩過** → **極度了解文庫行為**，能發現「化學設計或製造的怪癖」。
  - **實例**：同一個化學文庫做過兩次，即使化學相同，**行為不同**——這件事**只有篩過數百個蛋白後才看得出來**。
  - 反過來，**大量表徵文庫也能幫你除錯蛋白生產流程**。
- **團隊底蘊**：來自 Recursion 的高維生物學經驗——習慣「追逐各種 noise 來源」（例如：能否預測這筆資料出自哪台儀器？若能，就代表模型可以作弊）。

## 4. 「Recursion 黑幫」（Recursion Mafia）

Ian 提出有四家 Recursion 系公司「彼此押韻（rhyme）」——都在處理**極吵雜量測下的生物學問題**：
1. **Leash Bio**（Ian Quigley 等）——小分子化學。
2. **Noetic**（Ron Althod／Ron Alfa，主持提及）——自然產物混合物、質譜類。
3. **Invada**（Vishwa Kaluru、August Allen、Hannah Gordon、Dave Healy）——自然產物混合物。
4. **Known Medicine**（Katie Rose Skelly 主持，數年前被 **Pathos** 收購）。
- 共同點：**「我們很擅長吵雜量測 → 試試看能否從這個角落榨出乾淨訊號。」**

## 5. 小分子 vs 抗體／生物藥（為何在意小分子）

- **抗體／蛋白藥（含 GLP-1 類）**：由細胞製造、分子大、**難以進入細胞**、**難以做成口服錠**（需注射、冷鏈）。
- **小分子**：可做成藥丸、可進細胞、可穿越腫瘤防禦、較易過血腦屏障；**仍佔藥物的大多數**。
- 反面：小分子「處處可去」→ **更易有毒性／副作用**；監管路徑更複雜（肝毒性、心臟心律不整等）。
- ML 現況對比：**蛋白類藥物**的預測已有大量資料與公司（Ian 點名 Isomorphic、Chai、Nabla），但**小分子**的結合預測長期缺乏好資料。
- Leash 的延伸野心：不只人類蛋白，還要擴及**其他物種**（判斷該做小鼠還是大鼠模型，因不同物種蛋白略有差異）；並用篩選預測**off-target 毒性**。

## 6. Kaggle BELKA 競賽——全篇最重要的「實證敘事」

### 6.1 資料規模（驚人對比）
- 當時最大的公開資料庫 **BindingDB**：**略低於 300 萬**筆物理交互作用。
- Leash 釋出的資料集：**約 40 億（4 billion）筆物理交互作用**——**約 1000 倍**。
- 而且**全部由一個人在 Ian 家的地下室公寓（7 呎天花板）測出**（主持人稱這是他見過唯一從地下室起家的生技公司）。
- 文庫來源：贊助者 **Xiaojie Liu**（上海 **Alpha Ma**），約 **1.3 億（130 million）分子**；共同核心為 **triazine（三嗪）hub**，像「輪轂 + 三根輻條」。

### 6.2 精心設計的三級難度 eval（epistemic rigor 的核心）
Leash **沒有**只做隨機切分，而是設計三種切分難度，且**不告訴參賽者比例**：
1. **共享一個 building block**（其他兩根輻條不同）→ 最簡單。
2. **不共享 building block，但共用同一 triazine hub**（輻條相似但不相同）→ 中等。
3. **完全不同的化學文庫**（無共同 hub、無共同 building block、不同接合化學）→ 最難。此為**隱藏**測集（private），「to make it spicy（加點辣）」。

### 6.3 結果（關鍵事實）
- 共 **約 2,000 隊**參賽。
- 難度 1（共享建構塊）：**可以做得不錯**。
- 難度 2（無共享建構塊、仍同 hub）：**依目標不同，有些許提升**。
- **難度 3（最難）：沒有任何一隊勝過隨機（no one did better than chance）**。
- **冠軍**：一位「隨機參賽者」提交的 **Jupyter notebook**（Ian 亦提到 Viktor Shlopov 的另一種方法，同樣不勝隨機）。
- **前五名中有三名是嘈雜的教學 notebook**。

### 6.4 「我們會不會被 co-folding 取代？」（fear）
- Leash 自承：發佈前給了大約 **5% 機率**，認為當時的 co-folding 進展會**整個讓公司變得沒必要**。
- **結果：沒有發生**（Boltz 等並未取代其價值）。

### 6.5 開放釋出與回應批評
- 遭遇質疑「是不是沒有高手參賽？」→ Leash **完整釋出全部資料**（含**原始 read counts**、二元標籤、全部 evals），放上 **Polaris**（Recursion 支持的非營利組織）。
- 立場：「若有人覺得自己很行，拜託證明給我們看——我們想解掉這題。」
- 主持人補問：資料集是否本質受限（需外部增補才能超越）？Ian 回應：**若真懂物理／結構**，理論上應該做得不錯；但實務上大家做不到。

### 6.6 從競賽得到的洞見
- **分子表徵（representation）之爭被否證**：SMILES（純字串、無 3D 結構、只是圖遍歷轉文字）、3D 圖、球面卷積網……「fancier ways」**完全沒有勝過**簡單表徵。Ian：「we are extremely bitter lesson-pilled over here.」
- **記憶化（memorization）問題浮現**：模型可以記住個別 building block 的行為，藉此虛增表現。
- **策略轉向（關鍵決策）**：
  - 競賽只基於 **3 個**研究透徹的蛋白 → 要泛化到**新穎蛋白**必須做**遠多於此**。
  - **「更大」不等於「更好」**：1 億分子的文庫，**不如把較小的文庫做得更清楚**。在**固定預算**下，要在「化學品數 × 蛋白數」兩軸之間取得 variation。
  - Ian 稱其目標組合是「**單個位數百萬分子（single digit millions）**」→ 堪稱**史上最小的 DEL 之一**；史上最小曾見 **5 萬分子** 的 DEL。
  - Leash 的實際總量：**約 2,000 個不同蛋白 construct、累計約 5,000 次篩選**，每次至少 **650 萬分子**。

## 7. Hermes 模型——簡單到「不好意思」的架構與其驗證哲學

### 7.1 架構（極簡）
- **原始構想者**：Leash 資料科學家 **Max Kleinsasser**、**Sean Francis Lyon**，以及 CTO **Andrew Blevins**。
- **設計目的**：不是 SOTA，而是**夠簡單、能快速做大量實驗迭代**。
- **架構**：
  1. 蛋白側嵌入：**ESM**（Evolutionary Scale Modeling，原 Meta 團隊、後獨立、近期被 **Chan Zuckerberg** 收購；主持人提到 Alex Reeves 曾上節目）。
  2. 小分子側嵌入：**ChemBERTa**（本質是**預測 SMILES token 的 next-token predictor**）。
  3. 兩者以 **cross-attention** 結合 → 預測**二元標籤（binding/non-binding）**。
- **為何用 attention 而不用 MLP**：過往在蛋白結構圖模型上發現——**把位置座標打亂後效能幾乎不變** ⇒ 推論 attention 才是關鍵（能真正讓分子部位與蛋白殘基互動）。主持人稱之為影像生成的 **Picasso problem**。

### 7.2 越趨嚴格的切分（避免記憶化）
- 沿用競賽精神，設計**一系列由近到遠的切分**：
  - 共享 2 個 building block → 效能較高。
  - 只共享 1 個 → 較差。
  - 不共享 → 更差。
  - **building block 相似度分群（cluster）**、整群不重疊 → **最差**。
- **關鍵發現**：
  - **XGBoost** 隨切分變嚴**穩步下墜**（越 OOD 越掉）。
  - **Hermes** 在所有切分下**表現平穩（pretty steady）**。
  - 意義：要讓 XGBoost 真正「崩掉」，必須離分佈非常遠。
- Leash 亦寫過一篇 **「XGBoost is all you need?」** 的部落格（主持人調侃「年輕 ML 從業者花六個月優化論文模型，路人用 XGBoost 就把它打敗」）。
- 方法論格言：**幾乎所有事情都用 XGBoost 當 baseline。**

### 7.3 對外資料的評測（Hermes paper）
- Leash 只**用自家資料訓練**，再**對外部分子預測**（「training on internal only」是少見做法）。
- 評測規模（Ian 記憶）：總測試數**約 1,300 萬（13 million）**，**每目標約 500 個**，跨多蛋白。
- **對比 Boltz（當時的 SOTA 結構模型）**：Hermes 在公開資料集的結合問題上**大致打平**；**不同蛋白／蛋白家族互有勝負**，Ian 推測源於訓練集分佈差異。
- **最能說明問題的個案（BRD4）**：
  - 某測試集用的是**文獻中公開過、但 Leash 模型未見過的化學文庫副本**。
  - 其中 **BRD4** 上有一顆分子，與 **PDB 中、Boltz 幾乎必然看過的** 同一分子完全相同。
  - 結果：**Leash 模型表現不佳**（遠離其訓練化學空間）；**Boltz 完美命中**。Ian 的結論：「oh, yeah, that checks out（嗯，說得通）。」

## 8. 對抗記憶化：打破口袋（Breaking the Pocket）

### 8.1 問題：模型記「綽號」而非學物理
- 現象：給共折疊（co-folding）模型一個已有口袋的蛋白，**數位化地把口袋破壞**（填滿、移除、改大）→ 模型**照樣把小分子塞回原口袋**（「Because it just remembers where it is.」）。
- 根因假設：結構訓練集**缺乏好的負樣本**（negatives）——進資料庫的都是「有東西的蛋白」。
- 進一步：用 attention map 觀察 Hermes，原以為它會看**保守結構域（conserved domain）**，**結果它看的是非保守的短片段**。Ian 的判讀：
  > 「Hermes was probably coming up with a nickname for the protein.」
  （Hermes 大概是在**給蛋白取綽號**。）

### 8.2 解法：實驗性地大規模製造突變
**方法鏈（完整流程）**：
1. 篩選**野生型（wild type）**蛋白 → 得到一批 hits。
2. **競賽性置換（competitive assay）**：投入高濃度、已知會進該口袋的化學品 → 常規會進口袋的分子被置換掉。
3. 用 AlphaFold／Boltz／結構生物學家（點名 **Edward Kraft**）判讀口袋中的胺基酸。
4. **改變 DNA construct**，物理性地突變那個殘基（換上大塊側鏈等）→ 口袋被「灌水泥」或變大。
5. 再篩一次 → **原本被置換掉的那批化學系列也消失** ⇒ 證據：它們確實進那個口袋。
6. **反駁「你只是把蛋白弄壞了」**：只有「被競爭者踢出的化學系列」消失，**其他部位結合的系列完好** ⇒ 蛋白沒整體壞掉。

- **量化能力**：**大週可篩 100 個蛋白 construct / 週**（「which is what we do on big weeks」）。
- **意外收穫**：改變形狀會**促使其他分子結合**——這也是資訊來源。
- **組合化學的威力**：同一突變下可看到**5 個獨立化學系列、每個數百分子**同步轉向 ⇒ 乾淨證明「某個建構塊上的某個小側基，與某個胺基酸殘基互動」。
- **圖上發現**（主持人與 Ian 共同解讀的那張圖）：
  - 每個點是一個小分子；兩軸分別是對野生型／突變型的結合力。
  - 不同顏色的 blob = 不同化學系列。
  - 突變 1：整個系列群**往上移**（binding 變好）——即「突變讓它綁得更好」。
  - 突變 2（同口袋另一處）：整個系列群**被完全踢出**（不結合）。
  - 結論：可**同時在「化合物空間」與「蛋白空間」處理 activity cliff 問題**。
- 實用場景：**kinase（激酶）**——100 種 kinase 的關鍵結合位可能僅差一個殘基，此法特別有力。

### 8.3 用突變「教」模型
- 把這些工程化突變加入訓練 → 重看 attention map → **Hermes 開始更平均地看這些區域**（不再只盯「綽號」片段）。
- 主持人洞見：**在生物學中，mechanistic interpretability（機制可解釋性）最務實的用法是「從模型身上學生物」，而非單純解釋模型在想什麼**——因為這裡沒有語言可以依靠。

## 9. Clever Hans 與「化學家的社會學」（方法論上最鋒利的一節）

### 9.1 起源故事
- 多年前在 Recursion，Ian 與共同創辦人 Andrew Blevins 盯著螢幕上一顆小分子；一位 medicinal chemist **Mike Cucarisi** 路過說：「hey, looks like a Stuart Schreiber molecule.」
- 二人震驚：「光走過去就能看出來？**誰做的**？」
- **這個念頭困擾 Andrew 六到七年**，每隔幾個月喝啤酒就會說「我們真的該搞清楚這問題有多嚴重」。

### 9.2 實驗設計與結果（具體數字）
- 從 **ChEMBL**（最大化學品／活性資料庫）下載全體化學家資料，篩選條件為**發表 > 30 篇論文、> 600 個分子**。
- 得到 **1,815 位化學家**。
- 訓練一個分類器：**只從分子結構預測「是誰做的」** → **top-5 準確率 60%**。
- **容易混淆者**：同一機構、共同發表論文的兩位化學家。
- **推論**：個別化學家有**獨特的化學簽名風格（chemical signature style）**；學生／受訓者會沿用一部分 ⇒ 模型學到的是**社會學（sociology）**，而非真值。

### 9.3 更狠的一步：用「作者機率向量」取代化學結構
- Leash **完全不用化學結構或分子式**，改用**「作者機率向量」（1,800 維）** 來表徵分子。
- 結果：**用它預測活性的效果，與用化學式一樣好**。
- **兩者合併 → 並未顯著更好。**
- 結論金句：
  > 「We really think that it's learning a lot of sociology. It's not learning ground truth. It's just learning... the choices and the fingerprints of the people who are trying to develop these molecules.」
  > 「When you train models on the exhaust, you might be in trouble.」
  （我們認為它學到的是大量社會學，不是真值……**當你用「排氣」訓練模型時，你可能會出事。**）
- Ian 亦澄清**這不是對化學家的貶抑**：他們的本職是用最少的化學系列數衝到藥物，做法很合理。

### 9.4 相關的「資料集社會學」偏差
- **分子量（molecular weight）**：只要按分子量排序，就能得到最強單一預測因子之一（**CAS-16 任務中，排序法與第一名並列／或極接近**）。
- 成因鏈：找到 hit → 不斷加官能基（加氫鍵、加親水基改善溶解度）→ **「東西有效，人就會往上面加更多東西」** → 分子越變越重、越巴洛克、越多昂貴反應、越多難搞建構塊。
- **這些全是模型會抓到的簽名（signatures）** ⇒ 這**不是化學的內在性質，而是資料集的社會學性質**。

### 9.5 Clever Hans 的歷史寓言（節目內完整講述）
- 約 **19 世紀末德國**，一匹名為 **Clever Hans** 的馬，據稱會解複雜數學（用蹄子敲出正確答案）。
- 直到有人找**不知道答案的提問者**來問——馬**完全失敗**。
- 真相：馬是在讀**主人的姿勢與微表情**；當答案是 7、敲到 6 時主人已興奮，馬就停。
- 有德國心理學家寫過論文，**詳細評估主人的微表情與姿態變化**。
- 類比：**模型讀臉，不是讀數學；模型不懂化學，只是記住創造者的社會學。**

## 10. 語言模型 / RL 代理：Minos（「實驗室在迴路中，以運算速度」）

### 10.1 動機
- Leash 有日益龐大的 **activity cliff 與跨蛋白行為側寫**，想問：能否用**推理代理**來探索，做成「lab-in-the-loop」？
- 前提：必須改用**推理模型／語言模型**讓它「去玩」。

### 10.2 訓練與流程（具體）
1. 用**開源語言模型**（Ian 點名 **Qwen（Quins）**、**GLM** 等「別人也在用的」）。
2. **教它藥物化學**：給結構 → 用**自然英語**描述；給兩分子 → 用英語講出**差異**。
3. 給它 **10 個 binder + 10 個非 binder（彼此接近）**，要它判斷「為何 binders 會結合」。
4. 給它一個**數百萬分子的目錄（catalog）**，預算 **100 個分子**，讓它「設計實驗」（選 5–10 個測試假設）。
5. 模型**查詢已收集的資料**（即時回饋，**像 coding sandbox**）→ **更新假設** → 目標是**用最少步數找到最好的 binder**（模擬 medicinal chemist 的 SAR campaign）。
- 這是**強化學習 rollout**：資料規模持續成長、充滿 activity cliffs 與蛋白變異；因為 activity cliff 的改變是**因果的、可重現的、可量測的**，所以能產出**大量 reasoning traces（推理軌跡）**。
- 現況：代理跑 **102 步等級的多步推理**，最後選出答案。

### 10.3 為何優於 Hermes（或純堆參數）
- **更抗記憶化**：參數越多，模型也會**記住那些突變**。
- **自然語言是好的正則化器（regularizer）**。
- **獨特性主張**（Ian 自陳）：
  > 「we are unaware of other problems where you have a reinforcement learning loop that is physically grounded, that is this scalable this fast.」
  （我們不知道還有哪個問題，擁有**如此物理接地、又如此可規模化且如此快速**的 RL 迴路。）
- **為何有效（兩層理由）**：
  1. **機會做選擇**——像跑 coding sandbox 一樣有高頻強化訊號。
  2. **必須包含「人不會做的選擇」**——因為 Leash 量測了**所有蛋白上的所有分子**，代理能做**反直覺決策**並得到回饋 ⇒ **需要反事實（counterfactuals）、要允許犯錯**，且錯誤必須以**不被偏誤的方式**存在於資料中（否則會學到化學家的社會學指紋）。

### 10.4 「無限快的迴路」與規模對比
- 現況關鍵數據：**上週末就抽出超過 10,000 個 SAR 軌跡**，而且「還不算努力（we're not even trying that hard）」。
- 對照：一位藥物化學家**整個職涯**大概只做過**數十個、最多 50 個** SAR campaign。
- 代理從 **650 萬分子**中、以預算 100 找到最佳 binder。
- 未來：限制在已篩過的空間內；下一步可讓模型從 catalog 挑選，再送去做傳統 lab-in-the-loop 訂購與重測。

### 10.5 與其他公司的對比（主持人與 Ian 的交叉評述）
- **Exscientia**（Ian 稱「Excel from Xera」→ 實為 Exscientia／Andrew Hopkins 一派）：用序列編碼資料、做法「類似」但**不是語言**，且**沒把 pooled screens 變成「資料庫查詢」以做海量 rollout**。
- **Lila Sciences**：也在做自動化，「押韻（rhymes）」，但**不走 pooled screen → 資料庫查詢**這條路。
- Ian：這些團隊很聰明，但走的不是同一條可規模化 rollout 的路。

## 11. 商業模式與「Khosri 悖論」（Sri Kosuri 悖論）

- **悖論（主持人轉述）**：
  > 「in order to build a good machine learning model, you need lots of data... But then if you need that to train the model, like what do you need the model for? Because you just go collect the stuff.」
  （要做好 ML 模型就需要大量資料；但若你需要那些資料來訓練模型，那你還需要模型幹嘛？你直接去收集就好了。）
- **Ian 的回應**：
  - 若你只為**單一目標**找好化學品 → 悖論成立：蒐集就好，不需要模型。
  - 但**跨「所有東西」泛化**則不然。
  - 若能用**低資本**、大規模篩選，並配合**語言模型／化學推理**，能力範圍可擴到**遠超「找出新化學品」**。
  - **外溢應用**：一旦化學推理夠好，可立刻應用於**農業、獸醫科學、材料科學**，**而未必要在那些領域重新篩選所有蛋白**（同理，蛋白折疊公司也在攻未被篩過／難篩的目標）。
  - 終極願景：**若累積足夠的「工程化 activity cliff 變異」，也許到了某個點就能「做所有事」，從此不必再全部重篩。**
- 主持人追問「650 萬分子是否太少（化學空間常說 10^40）？」Ian 的正面回答：**僅用內部資料訓練的模型，能泛化預測到 ChEMBL**（非常不同的化學空間角落）。
- Leash 的規模數據：**約 2,000 個蛋白 construct、約 5,000 次篩選、每次 ≥ 650 萬分子**；若找 CRO 一次一個，**每個約 10 萬美元（$100K）**。

## 12. 「來打我啊（Come at me bro）」環節——最硬問題與回答

### 12.1 DEL 的固有限制／失敗模式
- **建構塊可得性與客製合成是最大瓶頸**（Ian 承認）。理想上想「把一個氮原子沿著環繞一圈換位置」，但**商業上根本買不到**、客製合成又慢。
- **接合化學（linker chemistry）**：過去最常用**醯胺鍵／胜肽鍵**（在體內易被消化）；但近 **4 年**有大量**對 DNA 友善**的新化學（碳–碳鍵、碳–氮鍵）湧現，不需破壞 DNA ⇒ Ian 對「可拆解性」較不擔心，**更擔心建構塊多樣性**。
- **ADMET 性質**：Ian 承認主要聚焦 binding。**實績：曾用極少 MedChem 週期，6 個月內從文庫 hit 做到小鼠 PKPD 良好**。
  - 方法：設計文庫時就以 **drug-likeness** 為目標；用類似 **Thompson sampling** 的方式定義優化函數（想綁什麼、想避什麼）。
  - **PKPD 實例**：一條**炎症（inflammation）**專案化合物，量測小鼠血液中**細胞激素（cytokine）**濃度，表現符合目標預期。
  - 正與夥伴洽談**分拆（spin out）**新實體來推進這些專案。藥物開發成本對比：**discovery 約數百萬美元；單一成功候選藥到上市則約 2 億至 10 億美元**。
- **Lamppost problem（路燈問題）**：生命科學中「能做夠多可規模化量測」的，都是**早期問題**——不能跑百萬隻小鼠、不能跑數百萬個一期試驗。所以現階段能規模化的仍是這些 early approaches。

### 12.2 「苦澀教訓」之問：什麼能阻止資金更雄厚的實驗室用規模碾壓你的 DEL 引擎？
- **Ian 的核心答案：培養獨特的實驗「文化」與「耐心」來追逐作弊模式（cheating modes）。**
  - 需追蹤 **batch effects 與 metadata**；建立**無摩擦（frictionless）的工具**讓做實驗的人真的願意記錄；回頭檢查公司**成立以來的歷史資料**；發現大變動就找出驅動因素並緩解。
  - **從零重建**：selection 流程、protein expression 流程；並建立**多種代理指標（proxies）**評估蛋白生產好壞。
  - 這種「追錯」的能力需要**有嗅覺的人**與時間，難以快速複製。

### 12.3 Lumacaftor 的意外發現（極精彩的「資料衛生」案例）
- 背景：藥物化學中有一類藥叫 **molecular chaperones（分子伴護蛋白）**，任務是**把錯誤摺疊的蛋白重新摺疊**。
- 最有名的之一：**lumacaftor（治療囊性纖維化 cystic fibrosis）**。
- **Leash 的化學文庫裡有長得像 lumacaftor 的化學品**。
- 篩選時 **這些化學系列不斷跨各種蛋白類型冒出來** → 「這什麼東西？是 lumacaftor 嗎？」
- 對照蛋白表現狀況 → **它們只在「蛋白質表現不順」時出現**。
- **結論／用途**：可作為**過濾器**——若某蛋白篩出一堆 lumacaftor 類 hit，**該蛋白多半沒正確摺疊**，**不該用作訓練資料**；應改條件重跑。
- 意義：**除非你有這種警覺，否則極難察覺。**

### 12.4 可量測性：KD 能否預測？
- **相對排序**：可以（複製篩選能得到同樣 hit、同樣順序）。
- **絕對 KD**：**還不行**（Ian：「I won't say that we're good at it yet」）。有人在試（改變蛋白濃度等）；Leash 正轉向 **SPR／生物物理量測**，想做「potency ladder」。
- **意外發現**：某些**非 DNA 結合蛋白**，其實會結合 DNA 條碼本身（未被描述過）→ 會影響 KD，需設法緩解。

### 12.5 「如果可憑命令移除一個瓶頸（buy fiat）」
- **Ian 的首選：大規模並行的純化（massively parallel purification）**。
  - 現況：合成後用 **HPLC 等清理，沒有一個真正好用的高度並行方案**。
  - 若能做到「海量、乾淨、純化、好操作的分子」→ 就能用**另一種 assay 做正交驗證（orthogonal validation）**。
- 對定序成本：**樂見其持續下降**（首個基因組 10 億美元 → 現在人類基因組約 1,000 甚至 100 美元；曾有段時間跌幅快於摩爾定律）；但仍希望更便宜以支援自有規模。
- 他補充：大家都在喊 GPUs，但他想要的是**純化**。

### 12.6 結語訴求
- 想讓聽眾帶走：Leash 正在建造一個**物理接地的基底（physically grounded substrate）**，供各種推理與生醫應用使用。
- **正在招聘 ML 人才、歡迎合作夥伴**。

## 13. 關鍵數據總表

| 項目 | 數值 |
|---|---|
| 傳統一管一文庫上限 | 低個位數百萬分子 |
| 已製最大 DEL | 40 兆（40 trillion）分子 |
| 競賽用文庫 | 約 1.3 億分子（Alpha Ma / Xiaojie Liu 贊助）；triazine hub |
| BindingDB 規模 | 略低於 300 萬筆 |
| Leash Kaggle 資料集 | 約 40 億筆（≈1000×） |
| Kaggle 參賽隊 | 約 2,000 隊；最難 eval 全部不勝隨機 |
| Leash 總篩選量 | 約 2,000 蛋白 construct、約 5,000 次篩選、每次 ≥ 650 萬分子 |
| 單次 CRO 篩選成本 | 約 10 萬美元 |
| 同分子 DNA 條碼數 | 32 或 48 條 |
| off-DNA 損耗率 | 易 90% 可用；難 50% 可用 |
| 蛋白養製時間（傳統） | 2–6 個月 |
| 大週篩選能力 | 100 個 construct / 週 |
| ChEMBL 化學家數 | 1,815 位（≥30 篇論文、≥600 分子） |
| 預測「作者」準確率 | top-5 = 60% |
| 作者機率向量維度 | 約 1,800 維 |
| 分子量排序 | CAS-16 並列第一／極接近第一 |
| Hermes 對外測試 | 約 1,300 萬測試、每目標約 500 |
| SAR 軌跡 | 一週末 > 10,000 個；化學家一生數十至 50 個 |
| Minos 代理預算 | 100 個分子；從 650 萬中挑最佳 |
| 藥物成本 | discovery 數百萬美元；成功候選至上市 2–10 億美元 |
| 基因組定序成本 | 首個 10 億美元 → 現在約 1,000／100 美元 |
| 團隊規模 | 僅 10 人 |
| co-folding 取代公司的自評機率 | 5%（未發生） |

## 14. 技術棧總覽（模型／方法／benchmark）

- **資料層**：DEL（組合化學 + NGS 讀出）、多重 DNA 條碼、negative controls、competitive displacement assay、工程化蛋白突變、批次效應追蹤。
- **模型**：
  1. **Hermes**：ESM（蛋白）+ ChemBERTa（SMILES）→ cross-attention → 二元分類。
  2. **XGBoost**：全流程基線。
  3. **Boltz**：外部 SOTA 結構模型（比較對象）。
  4. **AlphaFold**：用於設計突變蛋白。
  5. **ESM**：Evolutionary Scale Modeling（Meta → 獨立 → Chan Zuckerberg）。
  6. **ChemBERTa**：SMILES next-token 預測器。
  7. **Minos 代理**：開源 LLM（Qwen、GLM 等）+ RL rollout + 自然語言推理軌跡。
- **評測方法論**：三級難度切分（共享 1／2 個 building block → 無共享 → 完全不同意）；building block 相似度分群避免重疊；只訓內部資料、外推到 ChEMBL；attention map 可解釋性；工程化突變作為因果探針。
- **本文明確沒有給出**：各模型的參數量、訓練算力、具體 benchmark 分數表、loss 函數、資料規模的完整時間線數字、Minos 的具體 RL 算法（PPO/GRPO 等未提）、Minos 的 benchmark 分數。

## 15. 行業 Insight（格局／競爭／趨勢）

1. **資料規模 >> 模型精巧**：Kaggle 結果（4 億筆資料、2000 隊、最難 eval 全掛）是「苦澀教訓」的又一次實證——但**關鍵是資料的「乾淨度與設計」**，不是資料的「大」。
2. **「更多」不等於「更好」**：Leash 主動從 1.3 億分子文庫**退回單個位數百萬**，用固定預算換取「化學 × 蛋白」雙軸變化。
3. **公開資料集普遍不可信**：ChEMBL 是「社會學的排氣（exhaust）」；文庫標籤錯標率可達 **20–30%**（arrayed libraries）。
4. **資料即護城河，但護城河是「文化」不是「錢」**：Ian 認為**更雄厚的資金難以快速複製**的是「追錯文化 + 無摩擦紀錄工具 + 歷史資料回溯」。
5. **RL 迴路的物理接地是新前沿**：把 pooled screen 變成「資料庫查詢」以支撐海量 rollout，是 Leash 自認的獨有定位（並與 Exscientia、Lila 區隔）。
6. **語言模型作為正則化器 + 跨域橋樑**：自然語言推理可**抗記憶化**，且一旦化學推理夠強，可外溢至農業／獸醫／材料科學而**不必重篩**。
7. **小分子 vs 生物藥的再平衡**：抗體（含 GLP-1）在細胞內靶點、口服、冷鏈上有結構性劣勢；**cytokine 炎症靶點**被視為「抗體有效但小分子極難」的高價值機會（口服藥可打破冷鏈與輸注限制）。
8. **「路燈問題」**：能規模化量測的只有早期生物學問題——這是當前 AI×Bio 的天花板與機會所在。
9. **Recursion 系的擴散**：四家 Recursion 系公司（Leash、Noetic、Invada、Known Medicine）共享「吵雜量測中榨取訊號」的方法論 DNA——一種可辨識的學派。

## 16. 前後脈絡（對比／演變／關聯）

- **與之前集數的關聯（主持人明確點出）**：
  - **Noetic / Ron Alfa 那一集**：主持人主動點出與 Leash「精神高度相似」（epistemic rigor、資料導向）。
  - **ESM / Alex Reeves 那一集**：因 Hermes 用 ESM 而回指。
  - **Sri Kosuri 那一集**（主持人說「幾週前上過節目」，本集竟忘了問他的悖論——他自稱「很失望」）。
  - **Kaggle BELKA**：主持人自承「幾年前」就是透過 Leash 的 Substack 才入坑。
- **Leash 自身的觀點演變**：
  1. Kaggle 前：懷疑「沒人做得好」，另怕 co-folding 會讓公司變得沒必要（5% 機率）。
  2. Kaggle 後：確認問題極難 → **「苦澀教訓」+ 全力收資料**。
  3. Hermes 期：從「SOTA」轉向「簡單、可快速迭代」，設計嚴格切分與 only-internal 訓練。
  4. 破口袋期：發現模型「記綽號」→ **工程化突變**作為修復手段。
  5. 語言模型／代理期（Minos）：從監督式**轉向 RL 推理代理**，以自然語言抗記憶化。
- **與《Crossing the Threshold》的呼應**：文章 2 結尾亦導向「代理（agents）在沙箱中做可驗證的科學推理」，與文章 1 的「自主性 × 控制點」主題吻合。
- **Minos 的時間線（本集內披露）**：節目錄製後約 **2 個月** 演進為 Minos；文章發佈當日同時釋出 **preprint、blog、open dataset**（https://strelka.leash.bio/ 、 GitHub: Leash-Labs/minos-paper）。**Latent Space 預告數日內會發一集 lightning podcast 做更新。**

## 17. 爭議點

1. **「公開資料集不該用來訓練」**——Leash 主張 ChEMBL 等是「社會學排氣」，訓練其上等於學作弊；這是對現行大量學術做法的直接挑戰，**勢必引來反彈**（Ian 亦坦承收到「你們的競賽是不是沒高手參加」的質疑）。
2. **DEL 是否真能量產可用藥物**——社群長期負評（「每個碰過的人都受創」）；Leash 是反例，但**只有 10 人、一家公司**。
3. **「Bio 只有兩種可規模化方式（拍照、定序）」**——Ian 自稱「hot take」，並主動提及**蛋白質體學（proteomics）界會不同意**。
4. **RL 迴路「物理接地且如此快」的獨特性主張**——Ian 自陳「unaware of others」，屬**未經第三方驗證的自我評估**。
5. **自然語言是否優於注意力機制**——Leash 認為語言是更好的正則化器、更抗記憶化；這是**與主流表徵學習（3D 圖、結構模型）相左的立場**。
6. **注意力機制 vs MLP**：Leash 因「打亂座標效能不變」而選 attention——這是**間接推論**，非嚴格消融。
7. **KD 可否預測**——Leash 只承認能排序、尚不能給 KD；對「DEL 讀值能否作 KD 代理」持保留。
8. **時間線的誠實缺口（留白）**：Kaggle 賽後到 Hermes 之間 Ian 只說「六個月後」（主持人語），**逐字稿中並未給出完整日期**；Minos 的 2 個月演進亦為事後回溯。

## 18. 節目中提到的外部資源（原文連結）

- **Leash Bio**：https://www.leash.bio/
- **Leash Substack**：https://leashbio.substack.com/
- **Belka 競賽介紹**：https://leashbio.substack.com/p/introducing-belka
- **Belka 結果**：https://leashbio.substack.com/p/belka-results-suggest-computers-can
- **AI for Chemistry 2025 貼文**：https://leashbio.substack.com/p/ai-for-chemistry-in-2025-is-like
- **Hermes 貼文**：https://leashbio.substack.com/p/we-now-know-what-it-will-take
- **Breaking the pocket 貼文**：https://leashbio.substack.com/p/taking-away-the-protein-cheat-sheet
- **Making Reality Replayable（Minos blog）**：https://leashbio.substack.com/p/making-reality-replayable
- **Minos preprint**：https://github.com/Leash-Labs/minos-paper/blob/trunk/Minos_Leash.pdf
- **Minos open dataset**：https://strelka.leash.bio/
- **Kaggle 競賽**：https://www.kaggle.com/competitions/leash-BELKA
- **Boltz**：https://github.com/jwohlwend/boltz
- **Owl Posting 深度報導**：https://www.owlposting.com/p/an-ml-drug-discovery-startup-trying
- **Recursion**：https://www.recursion.com/
- **Kosuri 悖論推文**：https://x.com/srikosuri/status/203586616432543789
- **ChEMBL**：https://www.ebi.ac.uk/chembl/
- **Ian Quigley LinkedIn**：https://www.linkedin.com/in/iquigley/

---

## 萃取完整度聲明（誠實標註）

- **文章 1**：全文（相對短篇）已完整取得並逐點萃取。**無逐字稿**。架構圖、投影片內容以圖片形式存在，正文未展開，故**無法**提供具體模型名、版本號、數值 benchmark。
- **文章 2**：完整逐字稿（2,541 段、約 19,200 詞）已取得並通讀全文再萃取；上述所有數字與引語均直接來自逐字稿。**未取得**：本集 audio 內容中未被轉錄為文字的部分（若有）、以及連結資源（Minos 論文、Belka 全文）的內文——本次**未**抓取這些外鏈，故不對其內容作任何描述。
- 所有 quote 均為原文英文照錄，中文為本萃取之翻譯；原話若在逐字稿中為口語（含轉錄誤差，如「Quins」= Qwen、「Dell」= DEL、「Kemble」= ChEMBL、「luma-caftor」= lumacaftor、「AdNet」= ADMET），已於脈絡中註明對應。

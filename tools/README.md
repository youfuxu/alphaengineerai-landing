# tools/ — 一次性維護腳本（全部冪等，可安全重跑）

這裡放的是對 `blog/*.html` 與根頁面做批次維護的腳本。**每一支都是冪等的**——已經處理過的檔案會自動跳過，所以新增文章後直接重跑即可，不會產生重複內容。

| 腳本 | 做什麼 | 何時重跑 |
|---|---|---|
| `add_seo_meta.py` | 為 `blog/*.html` 補 `canonical`、`og:url`、`BlogPosting` JSON-LD。日期取自 `sitemap.xml` 的 `<lastmod>`，headline 取 `<title>` 去掉「 \| Alpha Engineer」後綴 | **每次新增文章後** |
| `add_root_schema.py` | 為 `index.html` / `blog.html` / `tools.html` 補 canonical 與站台層級 schema（Organization + WebSite + WebPage / Blog / CollectionPage，以 `@id` 互相連結） | 幾乎不用重跑，除非新增根頁面 |
| `hub_links.py` | 在 `best-ai-tools-engineers-passive-income.html` 的每張 tool-card 末尾，補一句連向該工具深度專文的內部連結 | 該清單文新增工具、或新增工具專文時 |

## 用法

```bash
python tools/add_seo_meta.py            # dry-run，只印出會改什麼
python tools/add_seo_meta.py --apply    # 實際寫入
```

三支都遵循同一個模式：**先 dry-run 看清單，確認無誤再 `--apply`**。

## 驗證方式（2026-08-06 建立時用的）

改完務必跑一次：

1. **JSON 可解析＋必填欄位齊全**，每檔恰好一個 `canonical` / `og:url` / `ld+json`、`</head>` 唯一
2. **`git diff --numstat` 確認所有 HTML 都是「N 增 0 減」**（只插入，不動既有內容）
3. **headless Edge 渲染**一篇既有文章與首頁，確認版型沒被改壞
4. push 後 **curl 線上逐頁確認**（GitHub Pages 的 CDN 有延遲，可能要等一兩分鐘）

## 背景

2026-08-06 之前，這個站 27 個頁面**沒有任何 JSON-LD，也沒有任何 canonical**，24 篇 blog 裡還有 9 篇連 `og:url` 都沒有——搜尋引擎與 AI 引擎必須自己猜每篇的作者、日期與正規網址。這幾支腳本是那次補完用的，留著是為了新增內容時不必重做一遍。

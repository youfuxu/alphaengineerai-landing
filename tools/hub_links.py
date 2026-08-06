# -*- coding: utf-8 -*-
"""在 best-ai-tools 清單文的每個 tool-card 末尾，補一句連向該工具深度專文的內部連結。
只在 tool-card 的收尾 </div> 之前插入，不動既有內容。冪等。
用法：python hub_links.py [--apply]
"""
import io, re, sys, os

F = r"C:\Users\youfu\alphaengineerai-landing\blog\best-ai-tools-engineers-passive-income.html"
APPLY = "--apply" in sys.argv

# h2 內的工具名關鍵字 -> (目標檔名, 連結句)
MAP = [
    ("ElevenLabs", "elevenlabs-review-engineers.html",
     "Full breakdown of the pricing tiers, voice quality and the API workflow: "
     "<a href=\"elevenlabs-review-engineers.html\">my ElevenLabs review for engineers</a>."),
    ("Synthesia", "synthesia-review-engineers-2025.html",
     "Whether the avatars hold up for a monetizable channel, and how it compares to HeyGen: "
     "<a href=\"synthesia-review-engineers-2025.html\">the full Synthesia review</a>."),
    ("Cursor", "cursor-ai-engineers-guide-2025.html",
     "The workflow I actually run in it, and where it stops helping: "
     "<a href=\"cursor-ai-engineers-guide-2025.html\">the Cursor guide for engineers</a>."),
    ("Notion AI", "notion-ai-productivity-engineers-2025.html",
     "How this fits a content ops system rather than just note-taking: "
     "<a href=\"notion-ai-productivity-engineers-2025.html\">Notion AI for engineers</a>."),
    ("Midjourney", "midjourney-vs-adobe-firefly-engineers-2025.html",
     "Side by side against Adobe Firefly on cost, licensing and batch work: "
     "<a href=\"midjourney-vs-adobe-firefly-engineers-2025.html\">Midjourney vs Firefly</a>."),
    ("Claude", "chatgpt-vs-claude-engineers-2025.html",
     "Where it wins and loses against ChatGPT for automation work: "
     "<a href=\"chatgpt-vs-claude-engineers-2025.html\">the head-to-head comparison</a>."),
]

s = io.open(F, encoding="utf-8").read()
orig = s

# 逐一定位 tool-card：從 <div class="tool-card"> 到對應的 </div>
cards = []
for m in re.finditer(r'<div class="tool-card">', s):
    start = m.start()
    # 往後找該 div 的收尾（這些卡片內沒有巢狀 div，實測確認）
    end = s.find("</div>", start)
    cards.append((start, end))

added = []
# 由後往前插入，避免位移
for start, end in reversed(cards):
    block = s[start:end]
    h2 = re.search(r"<h2[^>]*>(.*?)</h2>", block, re.S)
    if not h2:
        continue
    title = re.sub("<[^>]+>", "", h2.group(1))
    for key, target, sentence in MAP:
        if key.lower() in title.lower():
            if target in block:      # 已經連過就跳過（冪等）
                break
            ins = '\n    <p class="more">%s</p>\n  ' % sentence
            s = s[:end] + ins + s[end:]
            added.append((title.strip()[:40], target))
            break

print(("APPLIED" if APPLY else "DRY-RUN") + ": %d links" % len(added))
for t, tg in reversed(added):
    print("  %-42s -> %s" % (t, tg))

if APPLY and s != orig:
    io.open(F, "w", encoding="utf-8", newline="").write(s)

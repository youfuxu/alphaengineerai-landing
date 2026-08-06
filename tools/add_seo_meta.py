# -*- coding: utf-8 -*-
"""為 alphaengineerai-landing 的 blog 文章補上 canonical / og:url / BlogPosting JSON-LD。
只在 </head> 之前插入，不動任何既有內容。
用法：python add_seo_meta.py [--apply]
"""
import io, os, re, glob, json, html, sys

ROOT = r"C:\Users\youfu\alphaengineerai-landing"
APPLY = "--apply" in sys.argv
BASE = "https://alphaengineerai.com/"

sm = io.open(os.path.join(ROOT, "sitemap.xml"), encoding="utf-8").read()
lastmod = {}
for m in re.finditer(r"<loc>(.*?)</loc>\s*<lastmod>(.*?)</lastmod>", sm, re.S):
    lastmod[m.group(1).strip()] = m.group(2).strip()

def clean(t):
    t = html.unescape(t)
    t = re.sub(r"\s*\|\s*Alpha Engineer\s*$", "", t)
    return t.strip()

changed = []
for f in sorted(glob.glob(os.path.join(ROOT, "blog", "*.html"))):
    s = io.open(f, encoding="utf-8").read()
    name = os.path.basename(f)
    url = BASE + "blog/" + name

    if 'application/ld+json' in s:
        continue  # 已處理過，冪等

    title = re.search(r"<title>(.*?)</title>", s, re.S)
    desc = re.search(r'<meta name="description" content="(.*?)"', s, re.S)
    if not title or not desc:
        print("SKIP (missing title/desc):", name)
        continue

    headline = clean(title.group(1))
    description = html.unescape(desc.group(1)).strip()
    date = lastmod.get(url, "2026-07-01")

    add = []
    if not re.search(r'rel="canonical"', s, re.I):
        add.append('<link rel="canonical" href="%s">' % url)
    if not re.search(r'property="og:url"', s, re.I):
        add.append('<meta property="og:url" content="%s">' % url)

    ld = {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": headline,
        "description": description,
        "url": url,
        "datePublished": date,
        "dateModified": date,
        "inLanguage": "en",
        "mainEntityOfPage": {"@type": "WebPage", "@id": url},
        "author": {"@type": "Person", "name": "Alpha Engineer", "url": BASE},
        "publisher": {"@type": "Organization", "name": "Alpha Engineer", "url": BASE},
    }
    add.append('<script type="application/ld+json">\n%s\n</script>'
               % json.dumps(ld, ensure_ascii=False, indent=2))

    block = "\n".join(add) + "\n"
    if "</head>" not in s:
        print("SKIP (no </head>):", name)
        continue
    out = s.replace("</head>", block + "</head>", 1)
    changed.append((name, len(add), headline[:60], date))
    if APPLY:
        io.open(f, "w", encoding="utf-8", newline="").write(out)

print(("APPLIED" if APPLY else "DRY-RUN") + ": %d files" % len(changed))
for n, c, h, d in changed[:4]:
    print("  %-52s +%d blocks  %s  %s" % (n, c, d, h))
if len(changed) > 4:
    print("  ... and %d more" % (len(changed) - 4))

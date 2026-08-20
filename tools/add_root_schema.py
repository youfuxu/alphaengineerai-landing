# -*- coding: utf-8 -*-
"""為 alphaengineerai-landing 的三個根頁面補 canonical 與 schema。冪等。"""
import io, os, re, json, sys

ROOT = r"C:\Users\youfu\alphaengineerai-landing"
APPLY = "--apply" in sys.argv
BASE = "https://alphaengineerai.com/"

SITE = {"@type": "WebSite", "@id": BASE + "#website", "url": BASE,
        "name": "MindDividend Shield",
        "description": "A free global first check for suspicious messages, links, and payment requests, with practical safety guides.",
        "inLanguage": "en",
        "publisher": {"@id": BASE + "#org"}}
ORG = {"@type": "Organization", "@id": BASE + "#org", "url": BASE,
       "name": "MindDividend Shield"}

PAGES = {
    "index.html": {
        "url": BASE,
        "graph": [ORG, SITE,
                  {"@type": "WebPage", "@id": BASE + "#webpage", "url": BASE,
                   "name": "MindDividend Shield | Free Global Online Scam Checker",
                   "isPartOf": {"@id": BASE + "#website"},
                   "about": {"@id": BASE + "#org"}, "inLanguage": "en"}],
    },
    "blog.html": {
        "url": BASE + "blog.html",
        "graph": [{"@type": "Blog", "@id": BASE + "blog.html#blog",
                   "url": BASE + "blog.html",
                   "name": "MindDividend Shield Safety Guides",
                   "description": "Public safety guides for checking suspicious messages and scam patterns.",
                   "isPartOf": {"@id": BASE + "#website"},
                   "publisher": {"@id": BASE + "#org"}, "inLanguage": "en"}],
    },
    "tools.html": {
        "url": BASE + "tools.html",
        "graph": [{"@type": "CollectionPage", "@id": BASE + "tools.html#page",
                   "url": BASE + "tools.html",
                   "name": "AI Tools I Actually Use",
                   "description": "The public safety tools and guides behind MindDividend Shield.",
                   "isPartOf": {"@id": BASE + "#website"},
                   "publisher": {"@id": BASE + "#org"}, "inLanguage": "en"}],
    },
}

done = []
for fname, cfg in PAGES.items():
    path = os.path.join(ROOT, fname)
    s = io.open(path, encoding="utf-8").read()
    if "application/ld+json" in s:
        print("SKIP (already has ld+json):", fname); continue
    add = []
    if not re.search(r'rel="canonical"', s, re.I):
        add.append('<link rel="canonical" href="%s">' % cfg["url"])
    ld = {"@context": "https://schema.org", "@graph": cfg["graph"]}
    add.append('<script type="application/ld+json">\n%s\n</script>'
               % json.dumps(ld, ensure_ascii=False, indent=2))
    out = s.replace("</head>", "\n".join(add) + "\n</head>", 1)
    if out == s:
        print("SKIP (no </head>):", fname); continue
    done.append((fname, len(add)))
    if APPLY:
        io.open(path, "w", encoding="utf-8", newline="").write(out)

print(("APPLIED" if APPLY else "DRY-RUN") + ": %d files" % len(done))
for n, c in done:
    print("  %-14s +%d blocks" % (n, c))

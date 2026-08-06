# -*- coding: utf-8 -*-
"""為 alphaengineerai-landing 的三個根頁面補 canonical 與 schema。冪等。"""
import io, os, re, json, sys

ROOT = r"C:\Users\youfu\alphaengineerai-landing"
APPLY = "--apply" in sys.argv
BASE = "https://alphaengineerai.com/"

SITE = {"@type": "WebSite", "@id": BASE + "#website", "url": BASE,
        "name": "Alpha Engineer",
        "description": "Engineer using AI to build financial freedom — AI tools, passive income systems and build-in-public results.",
        "inLanguage": "en",
        "publisher": {"@id": BASE + "#org"}}
ORG = {"@type": "Organization", "@id": BASE + "#org", "url": BASE,
       "name": "Alpha Engineer"}

PAGES = {
    "index.html": {
        "url": BASE,
        "graph": [ORG, SITE,
                  {"@type": "WebPage", "@id": BASE + "#webpage", "url": BASE,
                   "name": "Alpha Engineer — Engineer Your Way to Financial Freedom with AI",
                   "isPartOf": {"@id": BASE + "#website"},
                   "about": {"@id": BASE + "#org"}, "inLanguage": "en"}],
    },
    "blog.html": {
        "url": BASE + "blog.html",
        "graph": [{"@type": "Blog", "@id": BASE + "blog.html#blog",
                   "url": BASE + "blog.html",
                   "name": "Alpha Engineer Blog",
                   "description": "AI tools, passive income systems and build-in-public results for engineers.",
                   "isPartOf": {"@id": BASE + "#website"},
                   "publisher": {"@id": BASE + "#org"}, "inLanguage": "en"}],
    },
    "tools.html": {
        "url": BASE + "tools.html",
        "graph": [{"@type": "CollectionPage", "@id": BASE + "tools.html#page",
                   "url": BASE + "tools.html",
                   "name": "AI Tools I Actually Use",
                   "description": "The AI tools and self-built utilities behind the Alpha Engineer stack.",
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

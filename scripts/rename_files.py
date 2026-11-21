#!/usr/bin/env python3
"""Rename corpus files to "<English title>_<Chinese title>.md".

Two corporations are handled:

  survey/                        line 1 = `# EN ｜中文 ｜arxivreview`
  hugging face daily papers/HF*/ line 1 = `# HuggingFace最新推荐论文 ｜EN ｜中文`

Titles are split on the FULL-WIDTH ｜ only: one HF paper has a bare ASCII `|`
inside its English title ("From P(y|x) to P(y)"), so splitting on ASCII pipes
would cut the title in half.

Names must open on Windows, so the illegal set \\ / : * ? " < > | is rewritten
(`:` -> " -", `?` dropped, quotes/brackets mapped, slashes to "-"). The English
part is capped at EN_CAP characters on a word boundary, which keeps the longest
full path well under the Windows 260-character limit.

Names that collide inside the same directory (case-insensitively, because NTFS
is case-blind) get a stable discriminator: the arXiv id for papers, the legacy
numeric id for surveys, else a slug of the source URL.

Usage:
  python3 scripts/rename_files.py            # dry run, prints the plan
  python3 scripts/rename_files.py --apply    # perform the renames
  python3 scripts/rename_files.py --apply --corpus survey
"""
import os, re, sys, collections, urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SURVEY = os.path.join(ROOT, "survey")
PAPERS = os.path.join(ROOT, "hugging face daily papers")
APPLY = "--apply" in sys.argv
CORPUS = None
if "--corpus" in sys.argv:
    CORPUS = sys.argv[sys.argv.index("--corpus") + 1]

EN_CAP = 120
ZH_CAP = 40
MARKERS = {"arxivreview", "huggingface最新推荐论文"}
TRANS = {}
for a, b in {":": " -", "?": "", "*": "", '"': "'", "<": "(", ">": ")",
             "|": "-", "/": "-", chr(92): "-"}.items():
    TRANS[ord(a)] = b

def titles(path):
    """Return (english, chinese, source_url) from the first lines of a file."""
    en = zh = url = ""
    with open(path, encoding="utf-8", errors="replace") as fh:
        for i, line in enumerate(fh):
            if i > 6:
                break
            line = line.rstrip("\n")
            if i == 0:
                m = re.match(r"^#\s*(.+?)\s*$", line)
                if m:
                    p = [x.strip() for x in m.group(1).split("｜")]
                    p = [x for x in p if x and x.lower() not in MARKERS]
                    if len(p) >= 2:
                        en, zh = p[0], p[1]
                    elif len(p) == 1:
                        en = p[0]
            elif not url:
                m = re.search(r"\((https?://[^)]+)\)", line)
                if m:
                    url = m.group(1)
    return en, zh, url

def clean(s, cap):
    s = s.translate(TRANS)
    s = re.sub(r"\s+", " ", s).strip()
    if len(s) > cap:
        cut = s[:cap]
        sp = cut.rfind(" ")
        s = (cut[:sp] if sp > cap // 2 else cut).rstrip(" ,-:&.")
    return s

def base_name(en, zh):
    return "%s_%s" % (clean(en, EN_CAP), clean(zh, ZH_CAP))

def discriminator(old, url):
    m = re.search(r"(\d{4}\.\d{4,5})", old)          # arXiv id, e.g. 2512.24880
    if m:
        return m.group(1)
    m = re.match(r"^\d+_survey_(\d+)_", old)          # legacy survey global id
    if m:
        return m.group(1)
    slug = urllib.parse.unquote(url.rstrip("/").rsplit("/", 1)[-1])
    return clean(slug, 24).lower() or "x"

def files():
    """Yield (directory, relative_dir, filename) for every corpus markdown."""
    if CORPUS in (None, "survey"):
        for f in sorted(os.listdir(SURVEY)):
            if f.endswith(".md"):
                yield SURVEY, "survey", f
    if CORPUS in (None, "papers"):
        for sub in sorted(os.listdir(PAPERS)):
            d = os.path.join(PAPERS, sub)
            if os.path.isdir(d):
                for f in sorted(os.listdir(d)):
                    if f.endswith(".md"):
                        yield d, os.path.join("hugging face daily papers", sub), f

plan = []
for d, rel, f in files():
    path = os.path.join(d, f)
    en, zh, url = titles(path)
    if not en or not zh:
        print("SKIP (no bilingual title): %s/%s" % (rel, f))
        continue
    plan.append([d, rel, f, base_name(en, zh) + ".md", f, url])

# Resolve collisions. A file already named "<base>_<token>.md" that is unique
# keeps its token, so re-running the tool never renumbers an existing corpus.
by_dir = collections.defaultdict(list)
for row in plan:
    by_dir[(row[0], row[3].lower())].append(row)
for (d, _), rows in by_dir.items():
    if len(rows) == 1:
        continue
    for row in rows:
        base = row[3][:-3]
        cur = row[2][:-3]
        if cur.lower().startswith(base.lower() + "_"):
            row[3] = row[2]                          # already suffixed: keep it
        else:
            row[3] = base + "_" + discriminator(row[2], row[5]) + ".md"
clash = collections.Counter((r[0], r[3].lower()) for r in plan)
hard = [k for k, v in clash.items() if v > 1]

ren = [r for r in plan if r[2] != r[3]]
if "--map" in sys.argv:
    mp = sys.argv[sys.argv.index("--map") + 1]
    with open(mp, "w", encoding="utf-8", newline="") as fh:
        fh.write("dir\told\tnew\n")
        for d, rel, old, new, _, _ in sorted(plan, key=lambda r: (r[1], r[2])):
            fh.write("%s\t%s\t%s\n" % (rel, old, new))
    print("plan written to %s" % mp)
print("scanned %d markdown files; %d need renaming; %d already conform"
      % (len(plan), len(ren), len(plan) - len(ren)))
if hard:
    print("UNRESOLVED COLLISIONS: %d" % len(hard))
    for d, n in hard[:5]:
        print("   ", os.path.join(os.path.relpath(d, ROOT), n))
    sys.exit(1)

for d, rel, old, new, _, _ in ren[:6]:
    print("  OLD %s/%s" % (rel, old))
    print("  NEW %s/%s" % (rel, new))
if len(ren) > 6:
    print("  ... %d more" % (len(ren) - 6))

if not APPLY:
    print("(dry run; pass --apply to rename)")
    sys.exit(0)

done = 0
for d, rel, old, new, _, _ in ren:
    src, dst = os.path.join(d, old), os.path.join(d, new)
    if os.path.exists(dst):
        print("REFUSE (target exists): %s/%s" % (rel, new))
        continue
    os.rename(src, dst)
    done += 1
print("renamed %d files" % done)

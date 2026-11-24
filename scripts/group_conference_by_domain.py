#!/usr/bin/env python3
"""会议论文按真实领域标签分组（不合并、无「其他方向」）。

会议 → 数据库原标签中文名 → 论文 + 方向论文汇编
每篇都有 paper_field_labels 最高分标签 → label_keywords.name_cn。
"""
from __future__ import annotations
import argparse, json, os, re, shutil, sys
from collections import defaultdict
from pathlib import Path

ROOT = Path("/mnt/d/project/github_arxivreview")
CONF = ROOT / "conference"
LABELS = Path("/mnt/d/project/pa-wt/fix-survey-failures-b1/.dsh-tmp/labels.json")

RE_ID = re.compile(r"(?:arxiv_\d{4}\.\d{4,5}|conf_[0-9A-Za-z_]+)")
RE_HEAD = re.compile(r"^#\s*(.+)$", re.M)

def safe_name(s: str) -> str:
    return s.replace("/", "与").replace("\\", "与").replace(":", " -").replace("*", "").replace("?", "").replace("|", "-").replace('"', "'").replace("<", "(").replace(">", ")")

def parse_note(path: Path) -> dict:
    text = path.read_text(encoding="utf-8", errors="ignore")
    ids = [x for x in RE_ID.findall(text) if x.startswith("arxiv_") or (x.startswith("conf_") and len(x) > 8)]
    head = RE_HEAD.search(text)
    parts = [p.strip() for p in (head.group(1) if head else "").split("｜")]
    en = parts[1] if len(parts) > 1 else (parts[0] if parts else path.stem)
    cn = parts[2] if len(parts) > 2 else ""
    lines = text.splitlines()
    aff = next((l.split("：",1)[1].strip() for l in lines if l.startswith("研究机构：")), None)
    authors = next((l.split("：",1)[1].strip() for l in lines if l.startswith("作者：")), None)
    arxiv = next((m.group(1) for m in [re.search(r"\[arXiv\]\(([^)]+)\)", text)] if m), None)
    review = next((m.group(1) for m in [re.search(r"\[ArxivReview\]\(([^)]+)\)", text)] if m), None)
    quote = next((l for l in lines if l.startswith("> ")), None)
    return dict(path=path, ids=ids, en=en, cn=cn, aff=aff, authors=authors, arxiv=arxiv, review=review, quote=quote)

def make_block(n: dict) -> str:
    b = [f"【{n['en']}" + (f" ｜{n['cn']}" if n["cn"] else ""), ""]
    if n["aff"]: b += [f"研究机构：{n['aff']}", ""]
    if n["authors"]: b += [f"作者：{n['authors']}", ""]
    if n["arxiv"]: b += [f"论文原文见 [arXiv]({n['arxiv']})", ""]
    if n["review"]: b += [f"分析报告见 [ArxivReview]({n['review']})", ""]
    if n["quote"]: b += [n["quote"], ""]
    b += ["】"]
    return "\n".join(b)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--conference", default=None)
    ap.add_argument("--rollback", action="store_true")
    args = ap.parse_args()
    manifest = CONF / "group_manifest_fine.json"

    if args.rollback:
        if not manifest.exists(): print("no manifest"); return
        man = json.loads(manifest.read_text(encoding="utf-8"))
        for new, old in man["moves"].items():
            p = CONF / new
            if p.exists():
                (CONF / old).parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(p), str(CONF / old))
        for d in man["created_dirs"]:
            p = CONF / d
            if p.exists() and not any(p.iterdir()): p.rmdir()
        manifest.unlink(); print("rollback done"); return

    sys.path.insert(0, "/mnt/d/project/paper_agent")
    from src.database.data_utils.pool import init_pool, connection
    init_pool()
    best = {}
    with connection() as conn:
        with conn.cursor() as cur:
            cur.execute("select paper_id,label,score from paper_field_labels order by paper_id,score desc")
            for pid,label,score in cur.fetchall():
                if pid not in best: best[pid] = label
    en2cn = {en: cn for en, cn in json.loads(LABELS.read_text(encoding="utf-8"))}

    conferences = [d for d in sorted(CONF.iterdir()) if d.is_dir()]
    if args.conference: conferences = [d for d in conferences if d.name == args.conference]
    moves, created, summary = {}, [], {}
    for cdir in conferences:
        notes = [parse_note(p) for p in cdir.glob("*.md") if p.name != "README.md"]
        groups = defaultdict(list)
        for n in notes:
            assert n["ids"], f"no id: {n['path']}"
            label = best[n["ids"][0]]
            assert label in en2cn, f"no cn name: {label}"
            groups[safe_name(en2cn[label])].append(n)
        print(f"{cdir.name}: {len(notes)} 篇 → {len(groups)} 领域")
        summary[cdir.name] = {"papers": len(notes), "domains": len(groups)}
        for dom, items in sorted(groups.items()):
            target = cdir / dom
            target.mkdir(exist_ok=True)
            created.append(str(target.relative_to(CONF)))
            for n in items:
                new = target / n["path"].name
                shutil.move(str(n["path"]), str(new))
                moves[str(new.relative_to(CONF))] = str(n["path"].relative_to(CONF))
            items.sort(key=lambda x: x["en"].lower())
            comp_name = f"{cdir.name}{dom}方向论文汇编.md"
            comp = [f"# {cdir.name} · {dom}方向论文汇编", "",
                    f"> 本方向共 {len(items)} 篇（{cdir.name}）。按论文标题字母序排列。",
                    "> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。", "", "---", ""]
            comp.append("\n\n---\n\n".join(make_block(n) for n in items))
            (target / comp_name).write_text("\n".join(comp) + "\n", encoding="utf-8")
        lines = [f"# {cdir.name} · 领域导航", "", f"共 {len(notes)} 篇，分 {len(groups)} 个领域。", "",
                 "| 领域 | 篇数 | 汇编 |", "| --- | ---: | --- |"]
        for dom, items in sorted(groups.items(), key=lambda x: -len(x[1])):
            lines.append(f"| {dom} | {len(items)} | [{dom}方向论文汇编]({dom}/{cdir.name}{dom}方向论文汇编.md) |")
        (cdir / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    manifest.write_text(json.dumps({"moves": moves, "created_dirs": created, "summary": summary}, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"moved {len(moves)} files; {sum(s['domains'] for s in summary.values())} domains")

if __name__ == "__main__": main()

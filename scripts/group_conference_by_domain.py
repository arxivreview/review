#!/usr/bin/env python3
"""会议论文目录按领域分组：会议 → 领域 → 论文 + 领域汇编。

用法（在本仓库根目录执行）：
  python scripts/group_conference_by_domain.py --dry-run
  python scripts/group_conference_by_domain.py --conference CVPR2026     # 试点
  python scripts/group_conference_by_domain.py                            # 全量 9 个会议
  python scripts/group_conference_by_domain.py --rollback                 # 按 manifest 回退

分类依据：paper_deep_analysis 里的 arXiv/ArxivReview id → paper_field_labels（取 score 最高的 label）
→ 内置大方向映射表（15 类）。无 id 或 DB 无标签时按标题+导语关键词兜底，仍无则归「其他方向」。
"""
from __future__ import annotations
import argparse, json, os, re, shutil, sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONF = ROOT / "conference"

# ── 大方向映射（关键词命中即归类；顺序 = 优先级）────────────────────────────
RULES = [
    ("医学与生物AI", ["medical", "clinical", "patient", "protein", "drug", "biomedical", "skin lesion", "histopath", "radiology", "brain", "healthcare", "nutrition", "disease", "cancer", "cardiac", "coronary", "breast", "dental", "ecg", "eeg", "epileptic", "mri", "x-ray", "polyp", "autism", "mental disorder", "survival analysis", "microscopy", "cell detection", "covid-19", "diagnosis", "biomechanical"]),
    ("三维视觉与3D/4D重建", ["3d", "4d", "6d", "gaussian splatting", "nerf", "point cloud", "depth", "mesh", "occupancy", "scene reconstruction", "surface reconstruction", "lidar", "pose estimation", "slam", "bird's-eye-view", "spatial reasoning", "articulated", "shape correspondence", "geo-localization", "reconstruction", "radiance", "holography", "computational imaging", "camera"]),
    ("机器人、自动驾驶与具身智能", ["robot", "manipulation", "policy learning", "autonomous driving", "drone", "navigation", "embodied", "simulator", "lane detection", "trajectory", "motion forecast", "digital twin", "spacecraft", "visual servo", "self-driving", "cooperative perception", "multi-agent perception"]),
    ("图像视频生成与编辑", ["image generation", "video generation", "diffusion", "text-to-image", "text-to-video", "image editing", "video editing", "super-resolution", "matting", "inpainting", "generation and synthesis", "generative image", "controllable video", "motion transfer", "avatar", "colorization", "deblurring", "restoration", "image synthesis", "photo retouching", "conditional image", "all-in-one image", "quality assessment", "video compression", "image compression", "video coding", "neural video compression", "video restoration", "video enhancement", "layout generation", "graphic design", "text layout", "streaming video", "video understanding", "video instruction tuning"]),
    ("计算机视觉基础任务", ["segmentation", "detection", "recognition", "tracking", "classification", "re-identification", "counting", "edge detection", "small object", "camouflaged", "visual search", "feature matching", "optical flow", "crowd", "contour"]),
    ("多模态与视觉语言", ["vision-language", "multimodal", "vlm", "visual question answering", "image caption", "visual grounding", "cross-modal", "clip", "image-text", "video question", "visual reasoning", "text-to-sql", "document image", "document information", "affective", "emotion recognition"]),
    ("大语言模型与智能体", ["llm", "large language model", "language model", "llm agent", "multi-agent system", "language agent", "agentic", "prompt", "in-context", "chain-of-thought", "reasoning", "tool-augmented", "deep research", "memory architect", "jailbreak", "hallucination", "knowledge editing", "machine unlearning", "instruction following", "preference optimization", "alignment", "commonsense", "analogical", "analogy", "causal", "fact-checking", "misinformation", "rumor", "authorship attribution", "code-switching", "dialect", "coreference", "morphological", "word sense", "sycophanc"]),
    ("自然语言处理与信息检索", ["question answering", "retrieval", "text classification", "sentiment", "machine translation", "summarization", "named entity", "parsing", "dialogue", "speech", "text generation", "knowledge base", "factuality", "natural language", "argumentation", "answer set", "logic-based", "semantic parsing", "relation extraction", "topic modeling"]),
    ("语音与音频", ["speech", "audio", "sound", "music", "voice", "phonetic", "speaker", "asr", "tts", "acoustic"]),
    ("可信AI与安全隐私", ["adversarial", "robustness", "security", "privacy", "fairness", "explainable", "interpretability", "xai", "backdoor", "attack", "watermark", "trustworthy", "safety", "bias mitigation", "governance", "responsible ai", "ethics", "calibration", "cyber defense", "anomaly detection", "uncertainty"]),
    ("机器学习理论与优化", ["optimization", "optimizer", "learning theory", "generalization", "federated", "reinforcement learning", "multi-agent reinforcement", "bandit", "graph neural", "graph learning", "gnn", "representation learning", "self-supervised", "semi-supervised", "transfer learning", "domain adaptation", "curriculum", "meta-learning", "low-rank", "kernel methods", "bayesian", "active learning", "decision trees", "ensemble", "quantization", "binary and low-bit", "attention mechanism", "cnn architecture", "efficient convolutional", "neural architecture", "model compression", "pruning", "distillation", "continual learning", "class-incremental", "catastrophic forgetting", "data augmentation", "dataset distillation", "coreset", "distribution shift", "concept drift", "monte carlo", "stochastic gradient", "online learning", "statistical modeling", "causal inference", "causal structure", "causal identification", "treatment effect", "counterfactual"]),
    ("代码与软件工程AI", ["code generation", "code evaluation", "program synthesis", "software engineering", "bug", "testing", "compiler", "repository", "coding agent", "program repair", "code summarization"]),
    ("数据科学与推荐系统", ["recommend", "collaborative filtering", "ranking", "click-through", "advertising", "user behavior", "knowledge graph", "time series", "forecasting", "clustering", "dimension reduction", "tabular", "e-commerce", "auto-bidding", "auction", "nearest neighbor", "indexes", "social choice", "voting", "dynamics of systems", "community dynamics", "learning analytics", "data valuation", "stream"]),
    ("科学计算与交叉应用", ["physics", "scientific", "chemistry", "material", "weather", "climate", "energy", "agriculture", "food", "law", "legal", "financial", "education", "geospatial", "remote sensing", "signal processing", "telecommunication", "semantic communications", "radio environment", "channel prediction", "power grid", "waste detection", "biodiversity", "astronomical", "fire", "environmental monitoring", "precipitation", "atmospheric", "optical distortion", "manufacturing", "predictive maintenance", "cloud and edge", "hardware acceleration", "blockchain", "game design", "computational social", "earth observation", "geospatial representations", "foundation models"]),
]
OTHER = "其他方向"

def safe_name(s: str) -> str:
    """目录/文件名安全化：斜杠等 Windows/Linux 非法字符替换。"""
    return s.replace("/", "与").replace("\\", "与").replace(":", " -").replace("*", "").replace("?", "").replace("|", "-")

def _hit(s: str, k: str) -> bool:
    # 短词（<6 字符）用词边界，避免 gene→general, llm→hello 之类误伤
    if len(k) < 6 and " " not in k:
        return bool(re.search(r"\b" + re.escape(k) + r"\b", s))
    return k in s

def map_by_text(en: str) -> str:
    s = en.lower()
    for broad, kws in RULES:
        if any(_hit(s, k) for k in kws):
            return broad
    return OTHER

RE_ID = re.compile(r"(?:arxiv_\d{4}\.\d{4,5}|conf_[0-9A-Za-z_]+)")
RE_HEAD = re.compile(r"^#\s*(.+)$", re.M)

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
    return dict(path=path, ids=ids, en=en, cn=cn, aff=aff, authors=authors,
                arxiv=arxiv, review=review, quote=quote)

def load_db_map():
    sys.path.insert(0, "/mnt/d/project/paper_agent")
    os.environ.setdefault("PYTHONPATH", "/mnt/d/project/paper_agent")
    from src.database.data_utils.pool import init_pool, connection
    init_pool()
    best = {}
    with connection() as conn:
        with conn.cursor() as cur:
            cur.execute("select paper_id,label,score from paper_field_labels order by paper_id,score desc")
            for pid, label, score in cur.fetchall():
                if pid not in best:
                    best[pid] = label
    return best

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
    ap.add_argument("--root", default=str(CONF))
    ap.add_argument("--conference", default=None, help="只处理指定会议（试点）")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--rollback", action="store_true")
    args = ap.parse_args()
    conf_root = Path(args.root)
    manifest_path = conf_root / "group_manifest.json"

    if args.rollback:
        if not manifest_path.exists():
            print("no manifest"); return
        man = json.loads(manifest_path.read_text(encoding="utf-8"))
        for new, old in man["moves"].items():
            p = conf_root / new
            if p.exists():
                (conf_root / old).parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(p), str(conf_root / old))
        for d in man["created_dirs"]:
            p = conf_root / d
            if p.exists() and not any(p.iterdir()):
                p.rmdir()
        manifest_path.unlink()
        print("rollback done"); return

    db = load_db_map()
    conferences = [d for d in sorted(conf_root.iterdir()) if d.is_dir() and d.name != ".git"]
    if args.conference:
        conferences = [d for d in conferences if d.name == args.conference]
    all_moves, created = {}, []
    for cdir in conferences:
        notes = [parse_note(p) for p in cdir.glob("*.md") if p.name != "README.md"]
        groups = defaultdict(list)
        for n in notes:
            label = db.get(n["ids"][0]) if n["ids"] else None
            dom = safe_name(map_by_text(label) if label else (map_by_text(n["en"]) if n["en"] else OTHER))
            groups[dom].append(n)
        print(f"\n=== {cdir.name}: {len(notes)} 篇 → {len(groups)} 领域 ===")
        for dom, items in sorted(groups.items(), key=lambda x: -len(x[1])):
            print(f"  {dom}: {len(items)}")
            if args.dry_run: continue
            target = cdir / dom
            target.mkdir(exist_ok=True)
            created.append(str(target.relative_to(conf_root)))
            for n in items:
                new = target / n["path"].name
                shutil.move(str(n["path"]), str(new))
                all_moves[str(new.relative_to(conf_root))] = str(n["path"].relative_to(conf_root))
            items.sort(key=lambda x: x["en"].lower())
            comp = [f"# {cdir.name} · {dom}方向论文汇编", "",
                    f"> 本方向共 {len(items)} 篇（{cdir.name}）。按论文标题字母序排列。",
                    "> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。", "", "---", ""]
            comp.append("\n\n---\n\n".join(make_block(n) for n in items))
            (target / f"{cdir.name}{dom.removesuffix('方向')}方向论文汇编.md").write_text("\n".join(comp)+"\n", encoding="utf-8")
        if not args.dry_run:
            # 领域导航 README
            lines = [f"# {cdir.name} · 领域导航", "", f"共 {len(notes)} 篇，分 {len(groups)} 个方向。", "",
                     "| 方向 | 篇数 | 汇编 |", "| --- | ---: | --- |"]
            for dom, items in sorted(groups.items(), key=lambda x: -len(x[1])):
                lines.append(f"| {dom} | {len(items)} | [{dom}方向论文汇编]({dom}/{cdir.name}{dom}方向论文汇编.md) |")
            (cdir / "README.md").write_text("\n".join(lines)+"\n", encoding="utf-8")
    if not args.dry_run:
        manifest_path.write_text(json.dumps({"moves": all_moves, "created_dirs": created}, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"\nmoved {len(all_moves)} files; manifest: {manifest_path}")

if __name__ == "__main__":
    main()

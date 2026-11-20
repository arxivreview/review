#!/usr/bin/env python3
"""Build survey/INDEX.md + README.md from survey/*.md  (v261120)
Usage: build_docs.py [--write]
README.md is a flat catalogue: one H1 per domain (中文 ｜ English), then every
survey under it as `English ｜ 中文`, linked to its file. No other prose.
"""
import os, re, sys, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SURVEY = os.path.join(ROOT, "survey")
WRITE = "--write" in sys.argv
VERSION = "261120"
FNAME = re.compile(r"^(\d+)_survey_(\d+)_(.*)\.md$")

# Ordered buckets; first match wins. Domain buckets precede task buckets so
# that e.g. "乳腺影像" is not swallowed by a generic 分割 rule.
CATS = [
 ("医学与生命科学", ["医学","临床","超声","病理","放射","X光","CT","MRI","心电","脑电","EEG","诊断","医疗",
   "癌症","肿瘤","手术","内窥","组织","细胞","基因组","蛋白质","药物","分子","生物","病历","EHR","视网膜",
   "肌肉骨骼","全切片","冠状动脉","颈动脉","心血管","乳腺","眼科","皮肤","牙科","睡眠分期","生理信号",
   "生理压力","精神障碍","自闭","病灶","空间组学","疫情建模","血流动力学","脑-深度网络"]),
 ("无线感知·通信·传感", ["无线","WiFi","射频","信道","语义通信","通信网","6G","毫米波","雷达","无线电",
   "传感器","人体活动识别","室内定位","感知与定位","信号处理","频谱","状态估计与滤波","信道编码"]),
 ("遥感·地球观测·环境气候", ["遥感","高光谱","SAR","合成孔径","卫星","地球观测","LiDAR","激光雷达","地理",
   "气象","气候","降水","临近预报","降尺度","生态","野生动物","森林","野火","农业","作物","植物病害","害虫",
   "精准畜牧","动物重识别","海洋","海事","水下","水文","空气质量","排放","废弃物","光伏","建筑能源","电池健康",
   "电网","地质","储层","系外行星","天文","光子神经网络"]),
 ("城市·交通·自动驾驶", ["交通","城市","出行","轨迹","自动驾驶","驾驶","车道","鸟瞰图","网约车","车辆路径",
   "动态调度","地图与位置","停车"]),
 ("工业·能源·工程系统", ["工业","制造","预测性维护","数字孪生","结构损伤","故障诊断","流程监控","材料",
   "晶体","逆向设计","工程设计","电子设计自动化","芯片","焊接","防护装备","工程结构"]),
 ("社会·教育·法律·金融", ["教育","学习分析","学生","心理测量","课程建模","考试","法律","判决预测","司法",
   "金融","信用风险","财务困境","加密货币","拍卖","自动出价","机制设计","投票","社会选择","社交媒体","新闻",
   "媒体偏见","健康虚假","恐同","意见动力学","体育分析","电商产品","社区动力学","游戏设计","表演性预测"]),
 ("语音与音频", ["语音","说话人","音频","声音","声学","声纹","音乐","歌声","ASR","TTS","降噪","唇形同步",
   "视听","房间脉冲响应","关键词检测","唤醒词","手语"]),
 ("视觉-语言与多模态", ["视觉语言","视觉-语言","视觉–语言","多模态","VLM","MLLM","图文","跨模态","视觉问答",
   "VLA","视觉推理","视觉Token","语言-视觉","CLIP","统一视觉","场景图","视觉位置识别","组合图像检索",
   "人-场景交互","GUI 定位","GUI定位"]),
 ("视频理解与生成", ["视频","时序动作","动作定位","动作识别","帧插值","密集视频","动作预测与预见",
   "人体运动预测","运动捕捉","人群计数"]),
 ("三维重建与神经渲染", ["三维","3D","4D","点云","NeRF","高斯泼溅","Gaussian","网格","Mesh","重建","SLAM",
   "新视角合成","神经视图合成","辐射场","逆渲染","材质估计","立体匹配","视差","深度估计","深度补全","形状",
   "体素","布局生成","建筑平面","位姿估计","物体位姿"]),
 ("人脸与生物特征", ["人脸","面部","表情","微表情","步态","重识别","匿名化","年龄估计","听者面部",
   "人像动画"]),
 ("图像生成与编辑", ["生成对抗","GAN","扩散模型","扩散驱动","图像生成","图像编辑","图像合成","图像修复",
   "超分辨率","图像增强","风格迁移","虚拟试穿","图像翻译","图像恢复","全合一","字体生成","草图与矢量",
   "流匹配","生成流网络","归一化流","自回归视觉生成","条件图像合成","可控面部编辑","隐写","数据增强方法",
   "生成式视觉数据增强","合成视觉数据","合成数据生成","着色","照片修图","图像操纵检测","AI生成图像检测",
   "AI生成媒体取证","深伪","伪造检测"]),
 ("低层视觉与计算成像", ["去雾","去噪","去雨","去模糊","去阴影","阴影与反射","低光","夜间","复原","湍流",
   "计算成像","相位恢复","全息","色彩化","色彩恒常","散焦","RAW","逆问题","图像复原","老照片"]),
 ("视觉感知与识别", ["目标检测","异常检测","缺陷","语义分割","实例分割","全景分割","分割","目标跟踪","跟踪",
   "显著性","姿态","关键点","场景文本","OCR","文档","表格识别","手写","细粒度","长尾","开放世界类别发现",
   "开放集","识别","Transformer","状态空间模型","Mamba","自监督","对比学习","蒸馏","剪枝","事件相机",
   "事件视觉","神经形态","鱼眼","全景360","光流","场景流","特征匹配","图像配准","图像检索","稠密检索",
   "多标签","层级多标签","部分多标签","噪声标签","不完美标注","标注者","类别发现"]),
 ("强化学习与具身智能", ["强化学习","RLHF","策略优化","奖励建模","世界模型","机器人","具身","导航","操控",
   "灵巧抓取","抓取","模仿学习","离线强化","多智能体","博弈","决策","规划与搜索","任务与运动规划",
   "老虎机","Bandit","最优臂","在线凸","主动推断","视动策略","Koopman"]),
 ("大模型与智能体", ["大语言模型","语言模型","LLM","GPT","大模型","智能体","Agent","代码生成","程序合成",
   "程序","思维链","检索增强","RAG","幻觉","谄媚","提示","上下文学习","演示样本","工具增强","工具调用",
   "文本到SQL","指令微调","对齐微调","偏好优化","组相对策略","规划能力","心智理论","元认知"]),
 ("自然语言处理", ["文本","机器翻译","翻译","问答","分词","嵌入","情感","主题建模","对话","摘要","信息抽取",
   "命名实体","实体","自然语言","多语言","低资源语言","词义消歧","词汇语义","语义相似性","语义解析","语法归纳",
   "句法","共指消解","事件抽取","关系学习","槽位填充","意图检测","阅读理解","问题生成","语法与拼写","纠错",
   "修辞","习语","形态","叙事","立场","偏见检测","论证","事实核查","关键词抽取","语义对应","文本简化",
   "可读性","作者归属","语言"]),
 ("AI for Science 与科学计算", ["物理信息","PDE","偏微分方程","常微分方程","神经算子","符号回归","方程发现",
   "动力系统","流体动力学","粒子物理","固体力学","薛定谔","量子","变分自编码器潜空间","原子间势","光谱与材料",
   "数学","定理证明","引理","科学发现","AI科学家","蒙特卡洛采样","微分方程"]),
 ("学习理论·优化与方法", ["优化算法","优化与","随机优化","凸","非凸","双层优化","多目标优化","子模","收敛",
   "泛化","过参数化","逼近理论","激活函数","梯度下降","形式化验证","测试与容错","虚假相关","捷径学习",
   "概念漂移","不平衡分类","学习理论","核方法","随机特征","最优传输","Wasserstein","散度","独立性检验",
   "低秩","张量分解","矩阵估计","聚类","谱聚类","多视图聚类","降维","拓扑数据分析","流形","黎曼","等变",
   "对称性","归一化","混合专家","模型合并","元启发式","超参数优化","自动机器学习","去中心化","本地SGD",
   "自适应随机梯度","能量模型","潜变量模型","柯尔莫哥洛夫","KAN","表征对齐","解耦表示","对象中心",
   "多任务学习","参数共享","特征选择","子空间","稀疏","采样","推断","贝叶斯","不确定性","校准","置信",
   "域适应","域泛化","迁移学习","因果","反事实","分布外","OOD","变分","零样本","少样本","小样本","元学习",
   "半监督","弱监督","无监督","主动学习","持续学习","类增量","课程学习","测试时适应","预训练","微调",
   "高效","加速","分布式","并行","边缘","神经架构搜索","量化","压缩","学习范式","优化器","训练"]),
 ("数据工程与知识构建", ["数据增强","数据选择","核心集","数据估值","数据归因","数据质量","管道","知识图谱",
   "本体","词嵌入","链接预测","图链接","图生成","图结构","图神经网络","图表示","图学习","消息传递",
   "异配图","时序","时间序列","表格数据","推荐","点击率","图数据"]),
 ("安全·隐私·可信治理", ["对抗","攻击","后门","越狱","水印","隐私","联邦","差分隐私","鲁棒","可信","公平",
   "安全","认证","指纹","投毒","逃逸","成员推断","漏洞检测","入侵检测","机器遗忘","治理","负责任AI",
   "哲学","伦理","版权","理论、","AI理论","对齐"]),
 ("系统·交互与效率", ["编译器","异构硬件","数据库","云系统","根因分析","云边","资源调度","最近邻","学习索引",
   "索引方法","推理加速","部署","流水线","算力","碳足迹","可持续AI","人机交互","交互","游戏","虚拟现实",
   "增强现实","数字人","图形设计","排版","区块链"]),
 ("评测·基准与方法论", ["基准","评测","评估","数据集","可解释","复现","元分析","文献计量","综述方法"]),
]

def classify(zh, en):
    hay = (zh or "") + " " + (en or "")
    for name, kws in CATS:
        for kw in kws:
            if kw in hay:
                return name
    return "综合与其他"

def parse(path):
    en = zh = link = ""
    with open(path, encoding="utf-8", errors="replace") as fh:
        for i, line in enumerate(fh):
            if i > 8:
                break
            line = line.rstrip("\n")
            if i == 0:
                m = re.match(r"^#\s*(.+?)\s*$", line)
                if m:
                    parts = [p.strip() for p in re.split(r"[｜|]", m.group(1))]
                    parts = [p for p in parts if p and p.lower() != "arxivreview"]
                    if len(parts) >= 2:
                        en, zh = parts[0], parts[1]
                    elif len(parts) == 1:
                        en = parts[0]
            elif not link:
                m = re.search(r"\((https?://[^)]+)\)", line)
                if m:
                    link = m.group(1)
    return en, zh, link

rows = []
for fn in sorted(os.listdir(SURVEY)):
    p = os.path.join(SURVEY, fn)
    if not os.path.isfile(p):
        continue
    m = FNAME.match(fn)
    if not m:
        continue
    idx, sid, slug = int(m.group(1)), int(m.group(2)), m.group(3)
    en, zh, link = parse(p)
    rows.append({"file": fn, "idx": idx, "id": sid, "zh": zh or slug, "en": en,
                 "link": link, "bytes": os.path.getsize(p)})
for r in rows:
    r["cat"] = classify(r["zh"], r["en"])

total_bytes = sum(r["bytes"] for r in rows)
n = len(rows)
mib = total_bytes / 1048576.0
order = [c for c, _ in CATS] + ["综合与其他"]
by_cat = collections.OrderedDict((c, []) for c in order)
for r in rows:
    by_cat[r["cat"]].append(r)
for c in by_cat:
    by_cat[c].sort(key=lambda r: -r["id"])
used = [(c, len(v)) for c, v in by_cat.items() if v]
id_lo = min(r["id"] for r in rows)
id_hi = max(r["id"] for r in rows)

def esc(t):
    return t.replace("[", "\\[").replace("]", "\\]")

# ------------------------------------------------------------------ INDEX --
L = []
L.append("# 综述总索引（%d 篇）" % n)
L.append("")
L.append("> 按标题关键词自动归类，版本 **%s**。每行格式：全局编号 → 本地文件 · 收录序号 · ArxivReview 原文链接。" % VERSION)
L.append("")
L.append("| 目录 | 篇数 |")
L.append("| --- | --: |")
for c, cnt in used:
    L.append("| [%s](#cat-%d) | %d |" % (c, order.index(c) + 1, cnt))
L.append("")
for c, cnt in used:
    key = "cat-%d" % (order.index(c) + 1)
    L.append('<a id="%s"></a>' % key)
    L.append("")
    L.append("## %s（%d 篇）" % (c, cnt))
    L.append("")
    for r in by_cat[c]:
        L.append("- **#%d** [%s](./%s) · `%03d` · [原文](%s)"
                 % (r["id"], esc(r["zh"]), r["file"], r["idx"], r["link"]))
        if r["en"]:
            L.append("  - <sub>%s</sub>" % esc(r["en"]))
    L.append("")
INDEX = "\n".join(L) + "\n"

# ------------------------------------------------------------------ README --
# Flat catalogue: one H1 per domain (中文 ｜ English), then every survey in it
# as "English ｜ 中文", linked to its file, plus the ArxivReview source link.
# No other prose.
CAT_EN = {
    "大模型与智能体": "Large Language Models & Agents",
    "学习理论·优化与方法": "Learning Theory, Optimization & Methods",
    "视觉感知与识别": "Visual Perception & Recognition",
    "医学与生命科学": "Medicine & Life Sciences",
    "视觉-语言与多模态": "Vision-Language & Multimodal",
    "三维重建与神经渲染": "3D Reconstruction & Neural Rendering",
    "强化学习与具身智能": "Reinforcement Learning & Embodied AI",
    "自然语言处理": "Natural Language Processing",
    "安全·隐私·可信治理": "Security, Privacy & Trustworthy AI",
    "视频理解与生成": "Video Understanding & Generation",
    "语音与音频": "Speech & Audio",
    "遥感·地球观测·环境气候": "Remote Sensing, Earth Observation & Climate",
    "图像生成与编辑": "Image Generation & Editing",
    "数据工程与知识构建": "Data Engineering & Knowledge Construction",
    "社会·教育·法律·金融": "Society, Education, Law & Finance",
    "AI for Science 与科学计算": "AI for Science & Scientific Computing",
    "无线感知·通信·传感": "Wireless Sensing, Communications & Sensing",
    "城市·交通·自动驾驶": "Urban Mobility & Autonomous Driving",
    "人脸与生物特征": "Faces & Biometrics",
    "工业·能源·工程系统": "Industry, Energy & Engineering Systems",
    "评测·基准与方法论": "Evaluation, Benchmarks & Methodology",
    "低层视觉与计算成像": "Low-Level Vision & Computational Imaging",
    "系统·交互与效率": "Systems, Interaction & Efficiency",
    "综合与其他": "General & Miscellaneous",
}

# Domains by size (largest first), then corpus order; entries by English title.
CAT_ORDER = sorted([c for c in order if by_cat[c]],
                   key=lambda c: (-len(by_cat[c]), order.index(c)))

# Titles almost all begin with "A Survey of …", so sort on the phrase that
# follows it: that keeps "A Survey on X" next to "A Survey of X".
LEAD = re.compile(r"^(?:an?|the)?\s*(?:brief|comprehensive|systematic|introductory)?\s*"
                  r"surveys?(?:\s+(?:of|on|in|for|towards|toward|into))?\s+", re.I)

def sort_key(r):
    return (LEAD.sub("", r["en"], count=1).lower(), r["zh"])

R = []
for c in CAT_ORDER:
    R.append("# %s ｜ %s" % (c, CAT_EN.get(c, c)))
    R.append("")
    for r in sorted(by_cat[c], key=sort_key):
        R.append("- [%s ｜ %s](survey/%s) · [原文](%s)"
                 % (esc(r["en"]), esc(r["zh"]), r["file"], r["link"]))
    R.append("")
README = "\n".join(R).rstrip("\n") + "\n"

print("files=%d  %.1f MiB  ids=%d-%d  cats=%d" % (n, mib, id_lo, id_hi, len(used)))
for c, cnt in used:
    print("  %-24s %4d" % (c, cnt))
if WRITE:
    open(os.path.join(SURVEY, "INDEX.md"), "w", encoding="utf-8", newline="\n").write(INDEX)
    open(os.path.join(ROOT, "README.md"), "w", encoding="utf-8", newline="\n").write(README)
    open(os.path.join(ROOT, "VERSION"), "w", encoding="utf-8", newline="\n").write(VERSION + "\n")
    print("WROTE survey/INDEX.md (%d lines)  README.md (%d lines)  VERSION"
          % (INDEX.count("\n"), README.count("\n")))
else:
    print("(dry run; pass --write to emit files)")

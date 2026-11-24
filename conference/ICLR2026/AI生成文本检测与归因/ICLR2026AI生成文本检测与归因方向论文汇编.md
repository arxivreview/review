# ICLR2026 · AI生成文本检测与归因方向论文汇编

> 本方向共 7 篇（ICLR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Antislop: A Comprehensive Framework for Identifying and Eliminating Repetitive Patterns in Language Models ｜语言模型“Slop”抑制框架：Antislop

研究机构：美国哥伦比亚大学、美国纽约大学

作者：Samuel Paech、Allen Roush、Judah Goldfeder 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.15061)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.15061)

> 大语言模型（LLM）在生成文本时表现出显著的重复性语言指纹，即“Slop”，导致输出质量下降且易被识别为机器生成。现有抑制手段如Token Banning或标准DPO在消除特定模式时往往伴随严重的通用能力退化或模型崩溃。本文提出Antislop框架，结合推理时回溯采样与一种名为FTPO的偏好优化算法，旨在以最小代价消除这些过度使用的模式。该框架在保持数学推理与写作质量的同时实现了高抑制率，但其对推理吞吐量的显著损耗及未验证的跨模型泛化能力仍存疑。

】

---

【BEYOND RAW DETECTION SCORES: MARKOV - INFORMED CALIBRATION FOR BOOSTING MACHINE GENERATED TEXT DETECTION ｜基于马尔可夫随机场校准的机器生成文本检测

研究机构：香港浸会大学、华南理工大学

作者：Chenwang Wu、Yiu-ming Cheung、Shuhai Zhang 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_49007174)

> 机器生成文本检测旨在区分人类写作与大语言模型（LLM）生成内容，核心挑战在于LLM采样随机性导致token级统计分数噪声大，传统直接聚合策略失效。本文切入点在于揭示并建模上下文token分数的邻域相似性与初始不稳定性，通过轻量级马尔可夫随机场（Markov Random Field, MRF）校准层修正分数偏差。该方法作为即插即用模块叠加于现有指标法检测器，无需重训底层模型。其价值在于以极小参数开销提升跨模型鲁棒性，但绝对性能仍低于监督学习SOTA，且对非token级输出方法不适用。

】

---

【EDITLENS: QUANTIFYING THE EXTENT OF AI EDIT ING IN TEXT ｜编辑程度量化检测

研究机构：美国马萨诸塞大学阿默斯特分校、美国马里兰大学帕克分校

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_89440376)

> 现有AI文本检测器将任务简化为“纯人类”与“纯机器”的二元分类，无法处理主流LLM使用中占比约三分之二的“人机协作编辑”场景，导致轻度润色文本被误判为完全AI生成。EditLens通过引入轻量级相似度指标作为中间监督信号，训练一个回归模型直接输出0-1的连续编辑程度分数，而非离散类别标签。该方法在二元与三元分类任务上均显著优于现有分类器，但其一维分数无法区分不同编辑模式，且未与最新通用检测SOTA进行直接对标。

】

---

【HLD: APPROXIMATE HIERARCHICAL LINGUISTIC DIS TRIBUTION MODELING FOR LLM-GENERATED TEXT DETECTION ｜层级语言分布近似检测

研究机构：中国科学院

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_60169780)

> AI生成文本检测旨在区分人类写作与大语言模型（LLM）生成内容，核心挑战在于生成模型能力指数级提升导致人机文本分布边界日益模糊。现有零样本统计检测依赖代理模型存在偏差且计算昂贵，监督学习则面临黑盒不可解释与跨域泛化差的困境。本文提出HLD-Detector，通过n-gram与核密度估计在词法、句法、语义三层级直接估计人机文本分布差异，无需在线代理推理。该方法在DetectRL基准上取得99.12%平均AUROC，但其在低资源语言及动态新模型场景下的鲁棒性仍存疑。

】

---

【Learn-to-Distance: Distance Learning for Detecting LLM-Generated Text ｜自适应距离学习检测LLM生成文本

研究机构：清华大学、英国伯明翰大学

作者：Hongyi Zhou、Jin Zhu、Kai Ye 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.21895)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.21895)

> 被动检测面临的核心困境是，当LLM生成文本的提示词（Prompt）未知时，基于固定统计量或固定距离的现有方法性能急剧下降。本文指出，重写基线（Rewrite-based）方法的有效性依赖于原文与重构文本间的距离度量，而固定距离无法适应不同模型与提示下的几何结构变化。通过引入机器学习自适应学习该距离函数，本文在未见提示场景下实现了显著的性能提升。这一方法在理论上证明了重写检测的几何合理性，但在分布内精度上仍落后于监督学习SOTA，且未解决细粒度定位问题。

】

---

【Learning from Dictionary: Enhancing Robustness of Machine-Generated Text Detection in Zero-Shot Language via Adversarial Training ｜基于翻译词典的对抗训练增强多语言机器生成文本检测

作者：Yuanfan Li、Qi Zhou、Zexuan Xie

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_10622207)

> 机器生成文本检测在多语言零样本场景下面临性能断崖式下跌与对抗攻击脆弱的双重困境，现有方法依赖大规模多语言语料或白盒访问权限，难以在低资源语言中部署。本文切入点在于利用静态翻译词典替代大规模语料，通过黑盒代理模型生成代码切换对抗样本，迫使检测器学习语言无关特征。具体做法是构建攻击者与检测器同步更新的对抗训练框架，并引入语言无关对抗损失。该方法在M4GT基准上取得0.773的平均F1，但其在高资源语言分布内的精度是否优于专用监督模型，以及词典错误对收敛性的影响，仍需进一步验证。

】

---

【TSM-BENCH: DETECTING LLM-GENERATED TEXT IN REAL-WORLD WIKIPEDIA EDITING PRACTICES ｜任务特异性机器生成文本检测基准

作者：Gerrit Quaremba、Elizabeth Black、Denny Vrandečić 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_91293313)

> 现有机器生成文本（MGT）检测基准多依赖通用提示，导致检测器在真实编辑场景中失效。本文指出任务特异性生成因受上下文约束，其统计分布更接近人类文本，现有SOTA检测器在此类数据上准确率大幅下降。通过构建包含四种真实编辑任务、三种语言及六个生成器的多任务基准，并引入特征重要性分析，揭示了检测器对表面特征的过拟合机制。该工作修正了领域对检测器鲁棒性的过度乐观估计，但缺乏对抗攻击下的鲁棒性验证。

】

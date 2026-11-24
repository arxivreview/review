# ACL-Findings2026 · 视觉-语言模型推理与评估方向论文汇编

> 本方向共 6 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Addressing Overthinking in Large Vision-Language Models via Gated Perception-Reasoning Optimization ｜门控感知-推理优化

研究机构：美国达特茅斯学院、美国圣母大学

作者：Xingjian Diao、Zheyuan Liu、Chunhui Zhang 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.04442)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.04442)

> 大视觉语言模型（LVLM）在复杂推理任务中常陷入“过度思考”，即对简单问题生成冗长且低效的推理链，导致测试时计算资源浪费甚至准确率下降。现有自适应推理方法仅关注推理深度的动态调整，忽略了视觉感知错误这一更底层的瓶颈，导致模型在感知阶段出错后，后续推理无论多深入都无法纠正。本文提出门控感知-推理优化（Gated Perception-Reasoning Optimization, GPRO），通过一个元推理控制器在Token级动态路由至快速生成、视觉重检或逻辑反思三条路径，以解决感知与推理资源的错配问题。该框架在效率-准确率帕累托前沿上表现优异，但其绝对性能上限仍受限于骨干模型的感知能力，且缺乏对局部视觉区域的精细定位机制。

】

---

【Do VLMs Have a Moral Backbone? A Study on the Fragile Morality of Vision-Language Models ｜视觉-语言模型道德鲁棒性诊断

研究机构：美国伊利诺伊大学厄巴纳-香槟分校

作者：Zhining Liu、Tianyi Wang、Xiao Lin 等 12 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.17082)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.17082)

> 视觉-语言模型在静态基准上表现良好的道德对齐，往往在真实部署的对抗扰动下迅速失效，现有评估仅关注干净输入下的准确率，无法反映决策边界的稳定性。本文切入点在于将道德判断视为一个需要抵抗多模态扰动的鲁棒性问题，而非单纯的分类任务。通过设计五类模型无关的文本与视觉扰动，系统测量23个主流模型的判断翻转率，并评估推理时干预的恢复能力。该研究揭示了当前模型道德立场的脆弱性及规模扩张带来的谄媚性风险，但缺乏对内部机制的因果归因，且防御策略效果有限。

】

---

【From Heads to Neurons: Causal Attribution and Steering in Multi-Task Vision-Language Models ｜头导向神经元归因与操控

研究机构：同济大学、美国威斯康星大学麦迪逊分校

作者：Qidong Wang、Junjie Hu、Ming Jiang

论文原文见 [arXiv](https://arxiv.org/abs/2604.17941)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17941)

> 多任务视觉-语言模型（VLM）内部参数功能纠缠，导致错误归因困难且缺乏可控性。现有神经元分析多聚焦单任务或孤立评分，忽略注意力路由上下文，引发多义性噪声。本文提出HONES，通过头条件化因果写入评分定位关键神经元，并实现轻量级操控。该方法在异构任务上实现了统一的神经元重要性评估，但仅验证了基础感知任务，未触及复杂推理链的忠实性。

】

---

【Grounded Concreteness: Human-Like Concreteness Sensitivity in Vision–Language Models ｜视觉接地对语义具体性的分级影响

作者：Aryan Roy、Zekun Wang、Christopher J. MacLellan

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ec910be8d71f)

> 视觉-语言模型（Vision-Language Model, VLM）是否比纯文本大语言模型（Large Language Model, LLM）具备更接近人类的“具体性”感知能力，是检验符号接地假说的关键问题。现有研究多将多模态训练视为整体性能提升，缺乏隔离视觉监督对抽象与具体概念差异化影响的受控消融。本文通过匹配同族LLM与VLM，在仅文本输入条件下，从输出行为、嵌入几何与注意力动态三个层面量化视觉接地的分级效应。该研究证实了视觉训练对具体概念的定向增益，但缺乏跨架构泛化证据，且未区分数据增强与模态接地的因果贡献。

】

---

【K-GIP: Diagnosing Logical Fractures in Large Vision-Language Models via Verification Scene Graphs and Sequential Pruning ｜知识引导上下文探测

作者：Yujun Hu、Xiaoyu Zhou、Changbo Wang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_210eb4cc7604)

> 大视觉语言模型（LVLM）在视觉问答中常因依赖语言先验而非视觉证据产生幻觉，现有基准多采用扁平指标，无法区分感知错误与逻辑推理错误。K-GIP 通过构建双感知真值与验证场景图，将存在性前提与属性推理的因果依赖显式建模，以序列逻辑剪枝惩罚逻辑断裂。该框架有效量化了模型在细粒度任务中的逻辑一致性，但其诊断精度受限于上游检测器的置信度阈值，且未验证图结构评估在动态场景下的泛化能力。

】

---

【VAUQ: Vision-Aware Uncertainty Quantification for LVLM Self-Evaluation ｜视觉感知不确定性量化

研究机构：美国威斯康星大学麦迪逊分校、新加坡南洋理工大学

作者：Seongheon Park、Changdae Oh、Hyeong Kyu Choi 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.21054)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.21054)

> 大型视觉语言模型（LVLM）在生成答案时，常因语言先验主导而忽略视觉证据，导致高置信度的幻觉输出。现有基于文本的自评估方法（如熵、语义一致性）在反事实图像上失效，无法区分“流畅但错误”与“视觉接地且正确”的响应。本文提出VAUQ，通过计算移除核心视觉区域后的预测熵变化，显式量化视觉证据对模型置信度的贡献。该方法无需训练且无需外部评估器，在反事实场景下将自评估AUROC提升13.3%，但依赖注意力机制定位关键区域，其鲁棒性边界尚待验证。

】

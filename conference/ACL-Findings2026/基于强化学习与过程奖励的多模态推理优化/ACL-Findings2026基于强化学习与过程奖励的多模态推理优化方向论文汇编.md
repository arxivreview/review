# ACL-Findings2026 · 基于强化学习与过程奖励的多模态推理优化方向论文汇编

> 本方向共 5 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【AdaTooler-V: Adaptive Tool-Use for Images and Videos ｜自适应工具调用多模态推理

研究机构：香港中文大学

作者：Chaoyang Wang、Kaituo Feng、Dongyang Chen 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.16918)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.16918)

> 多模态大模型在“思考图像”范式下常陷入盲目调用视觉工具的陷阱，导致推理路径偏离与计算开销激增。现有强化学习框架缺乏对工具调用必要性的显式判断机制，往往无差别地奖励工具使用行为。本文提出AT-GRPO算法，通过引入样本级的工具收益分数动态调整奖励尺度，使模型仅在有真实增益时调用工具。该机制在高分辨率视觉推理任务上显著提升了性能与效率，但其依赖离线预计算的收益分数，在动态环境下的泛化能力存疑。

】

---

【AutoRubric: Rubric-Based Generative Rewards for Faithful Multimodal Reasoning ｜基于自动评分标准的忠实多模态推理

作者：Mengzhao Jia、Zhihan Zhang、Ignacio Cases 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0070e9c7e4c6)

> 多模态大模型在强化学习可验证奖励（RLVR）训练中常出现“答案正确但逻辑断裂”的虚假推理现象，现有过程奖励模型（PRM）因依赖人工标注或更强教师模型而难以扩展。本文切入点在于利用模型自身成功轨迹的自聚合特性，自动生成问题特定的推理检查点（Rubrics），替代传统PRM提供细粒度过程监督。该方法通过LLM-as-a-Judge验证轨迹与Rubrics的匹配度，结合结果奖励优化策略，在六个基准上提升了推理忠实度。其价值在于解决了过程监督的数据瓶颈，但引入了额外的计算开销且未完全消除视觉感知层面的偏差。

】

---

【Collaborative Multi-Agent Scripts Generation for Enhancing Imperfect-Information Reasoning in Murder Mystery Games ｜多智能体协作脚本生成与不完全信息推理增强

研究机构：中山大学、香港中文大学

作者：Keyang Zhong、Junlin Xie、Hefeng Wu 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.11741)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.11741)

> 多模态大模型在涉及欺骗、多跳推断及动态社会交互的复杂博弈场景中，因缺乏大规模高质量训练数据而表现退化。现有单智能体推理优化方法无法覆盖多玩家不完全信息下的策略性行为建模，本文切入点在于构建多智能体协作框架以自动化合成包含视觉与文本线索的博弈剧本。通过两阶段训练策略，结合监督微调与基于智能体监控的强化学习，提升视觉语言模型在角色一致性与证据整合上的推理能力。该方法在WhodunitBench基准上显著优于开源基线，但其评估依赖主观性较强的LLM-as-Judge机制，且未验证在通用数学推理任务上的泛化性。

】

---

【Reasoning in the Dark: Interleaved Vision-Text Reasoning in Latent Space ｜交错视觉-文本潜在推理

研究机构：香港理工大学、新加坡管理大学

作者：Chao Chen、Zhixin Ma、Yongqi Li 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.12603)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.12603)

> 多模态大模型在长链推理中面临视觉证据利用不足与显式文本生成带来的高延迟矛盾。现有方法要么依赖纯文本推理导致视觉漂移，要么通过显式图像-文本交错增加标注成本与推理开销。本文提出IVT-LR，将文本与视觉推理统一置于潜在空间，通过隐藏状态与动态选择的图像嵌入替代显式Token。该方法在精度与效率上均超越基线，但其训练范式与主流强化学习路线的差异，以及缺乏与RLVR方法的公平对比，使其在领域定位上存在显著盲区。

】

---

【View-R1: Asymmetric Policy Optimization for Difficulty-Aware Multimodal Reinforcement Learning ｜非对称策略优化

研究机构：浙江大学、中国科学技术大学

作者：Minjie Hong、Zirun Guo、Jiabao Zhang 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_70d42800c22c)

> 多模态大模型（MLLMs）在强化学习后训练中常面临通用能力退化与推理链冗余的矛盾。现有组相对策略优化（GRPO）采用固定KL散度约束与均匀长度归一化，导致难样本探索受限且错误答案长度无限膨胀。本文提出非对称策略优化（APO），通过难度自适应散度整形与子最优轨迹复杂度正则化分别处理正负样本。该方法在3B/7B小模型上实现了推理性能提升与通用知识保留的平衡，但其缺乏过程级视觉监督的局限在复杂视觉任务中可能成为性能天花板。

】

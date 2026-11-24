# ACL-Findings2026 · 大语言模型中的多模态对齐与推理方向论文汇编

> 本方向共 5 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Beyond Modality Collapse: Taming Guided Modality Entropy for Omni-modal Emotion Reasoning ｜全模态情感推理中的模态熵校准

研究机构：北京交通大学

作者：Xian Zhao、Rui Hu、Yuxiang Zhang 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_dc7680c7fead)

> 全模态大语言模型在处理情感推理时，常因过度依赖视觉模态而忽略音频与文本线索，导致推理链逻辑断裂。现有监督微调方法仅能实现域适应，无法解决跨模态证据整合中的动态依赖问题。本文通过构建引导式思维链数据并引入基于模态熵的动态强化学习奖励，迫使模型在不确定时主动探索多模态证据。该方法在多个情感基准上刷新了性能上限，但其对连续模态特征的适用性及计算开销仍存疑。

】

---

【CAIR: Causal Adaptive Information-based Reinforcement Learning for Multimodal Emotion Reasoning ｜因果中介强化学习

研究机构：中国科学院、中国科学院大学

作者：Fengyu Zhang、Bin Liu、Jianhua Tao 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_cfa90365ba53)

> 多模态情感推理旨在从视频、音频与文本中不仅识别情绪标签，更需解释情绪产生的因果触发机制。现有监督微调方法常陷入“因果退化”，即生成流畅但缺乏逻辑推导的表面描述，而传统强化学习仅优化答案正确性，无法约束推理链的因果有效性。CAIR 将推理链重构为决策过程中的因果中介，通过量化其对预测熵的降低程度来设计奖励信号，并引入认知负载自适应优化机制以平衡不同复杂度任务的训练权重。该方法在MTMEUR基准上取得了73.80%的准确率，显著提升了推理的因果忠实性，但其泛化能力至非情感类通用推理任务尚存疑问。

】

---

【ConSensus: Multi-Agent Collaboration for Multimodal Sensing ｜多智能体协同下的传感器融合仲裁

研究机构：韩国科学技术院、诺基亚贝尔实验室

作者：Hyungjun Yoon、Mohammad Malekzadeh、Sung-Ju Lee 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.06453)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.06453)

> 异构传感器数据在单一大型语言模型（LLM）中常因上下文过载与模态主导导致推理断裂，且语义聚合易受先验知识偏见影响，而统计投票在传感器缺失时又易失效。现有方案要么依赖昂贵的多轮辩论，要么缺乏对语义与统计冲突的显式仲裁。ConSensus 提出一种免训练的多智能体框架，通过模态特化智能体与混合融合机制，在单轮内平衡语义推理与统计共识。该框架在五个基准上平均提升 7.1% 准确率，并将融合 token 成本降低 12.7 倍，但其鲁棒性边界在传感器严重缺失时仍存疑。

】

---

【DentalGPT: Incentivizing Multimodal Reasoning in Dentistry ｜牙科多模态推理激励：从对齐到强化

研究机构：香港中文大学、北京大学

作者：Zhenyang Cai、Jiaming Zhang、Junjie Zhao 等 18 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f4d01e182ce1)

> 牙科影像诊断依赖对细微病灶线索的精准感知与逻辑推导，但通用多模态大语言模型（Multimodal Large Language Models, MLLMs）在此垂直领域表现疲软，且复杂推理模式带来的增益远低于其他医学场景。现有方案受限于牙科专用视觉-文本对齐数据匮乏及领域强化学习缺失，导致模型无法有效探索牙科问题的解空间。本文通过构建超12万张牙科图像的多模态对齐数据集，并结合基于可验证奖励的强化学习（Reinforcement Learning with Verifiable Rewards, RLVR），在7B参数规模下实现了牙科诊断推理能力的显著提升。该工作验证了“对齐先行、强化跟进”范式在垂直领域的有效性，但其对通用推理能力的潜在侵蚀及小样本基准的统计稳定性仍存疑。

】

---

【Directional Reasoning Injection for Fine-Tuning MLLMs ｜方向性推理注入

研究机构：美国罗切斯特大学

作者：Chao Huang、Zeliang Zhang、Jiang Liu 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.15050)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.15050)

> 多模态大语言模型（MLLMs）普遍存在“感知强、推理弱”的断层，即能准确识别图像内容却难以构建连贯的逻辑推导链。现有主流方案依赖大规模多模态思维链（CoT）数据微调或强化学习，面临数据成本高与训练不稳定的双重瓶颈；参数空间合并虽看似轻量，但在模型分布差异大时极易导致性能退化。DRIFT 提出在梯度空间注入推理先验，通过预计算文本专家与多模态模型的参数差向量引导反向传播，以极低成本实现推理能力迁移。该方法在数据效率上显著优于传统范式，但在绝对性能上仍低于高资源投入的 SOTA 模型，其泛化边界尚需更多验证。

】

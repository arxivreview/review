# ACL-Findings2026 · 高效多模态大语言模型训练与推理方向论文汇编

> 本方向共 3 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【A Learnable Skill Combination Strategy for Multi-task Learning in Natural Language Understanding ｜基于可学习技能组合的多任务自然语言理解框架

作者：Zhe Yang、Yi Huang、Yaqin Chen 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ea441a9160b8)

> 多任务学习（MTL）旨在通过共享表示提升数据效率并缓解单任务过拟合，但现有软参数共享方法如 MMoE 和 Skill-Net 分别存在专家负载不均衡与人工映射依赖的瓶颈。本文切入点在于将技能选择从数据驱动或人工配置转变为基于任务-技能嵌入相似度的动态可微机制。具体做法是扩展 Transformer 的 FFN 为技能簇，并通过正交约束与可微阈值函数实现端到端的稀疏技能激活。该框架在中文 NLU 基准上优于传统 MTL 基线，但其性能增益是否源于架构改进而非骨干优势，以及嵌入路由在任务分布偏移下的鲁棒性，仍存疑。

】

---

【Learning Flexible Large Multimodal Models with Arbitrary Modality Combinations ｜灵活多模态学习框架 Flex-M3

研究机构：美国北卡罗来纳大学教堂山分校

作者：Xinyu Zhao、Kangqi Ni、Jie Peng 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_89b0ecbb2070)

> 多模态大语言模型（MLLMs）在扩展至音频、3D等异构模态时，面临数据配对稀缺与Token序列线性膨胀的双重瓶颈。现有方法要么依赖全模态完整数据，要么通过静态填充处理缺失，导致泛化能力随模态数量增加而下降。Flex-M3 通过引入基于文本和视频锚点的缺失模态生成模块，结合两阶段压缩机制，实现了在任意模态组合下的鲁棒训练与推理。该框架在 NExT-QA 等基准上优于全模态基线，但其生成模块的泛化边界及计算开销的长期影响仍需进一步审视。

】

---

【Skill Weaving: Efficient LLM Improvement via Modular Skillpacks ｜模块化技能包与全量化压缩

研究机构：哈尔滨工业大学、香港理工大学

作者：Zhuo Li、Guodong Du、Zesheng Shi 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.22205)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.22205)

> 多域大语言模型（LLMs）在固定内存与延迟预算下难以兼顾多领域性能，现有参数高效微调（PEFT）方法能力保留不足，而全参数微调又导致存储与推理开销激增。SkillWeave 通过域隔离的全参数微调构建技能包，再经全量化压缩实现低延迟部署，解决了能力与效率的矛盾。该框架在 9B 规模下超越 32B 单体模型并实现 4 倍加速，但其全参微调训练成本与自生成数据质量依赖未充分量化，长期泛化能力存疑。

】

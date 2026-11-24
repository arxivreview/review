# ACL-Findings2026 · 大语言模型训练中的数据选择与整理方向论文汇编

> 本方向共 3 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Fine-Grained Data Ordering Improves Fine-Tuning for Large Language Models ｜细粒度顺序微调

研究机构：浙江大学、新加坡国立大学

作者：Xiaomeng Hu、Yixuan Tang、Haoze Li 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e44b2fb4dae7)

> 微调阶段的数据治理长期聚焦于“选什么”，即通过过滤或子集选择提升数据质量，却忽视了“怎么排”，即训练序列对模型收敛路径的影响。现有随机洗牌策略无法实现从预训练分布向目标分布的渐进迁移，导致梯度震荡与收敛效率低下。FOT通过定义基于模型交叉熵与预训练先验的数据难度，在早期Epoch实施由易到难的块内洗牌排序，后期恢复随机以平衡泛化。该方法在持续预训练与监督微调任务中实现了平均2.4%的性能提升，但其增益依赖于难度定义的准确性，且未验证与数据过滤策略的协同效应。

】

---

【GALA: Geometric Data Selection with Strategic Prospecting for Large Language Model Self-training ｜几何数据选择与策略探索

研究机构：同济大学

作者：Zhongwei Xie、Ruihao Liao、Zimo Wang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_278b0ccb2313)

> 大语言模型（LLM）自训练旨在通过模型生成自身训练数据实现能力迭代，但现有“生成-过滤”范式常陷入语义冗余与策略单一的双重困境，导致训练效率低下且泛化能力受限。GALA 提出了一种“更聪明地策展”（curate-smarter）的闭环框架，将静态子集选择升级为动态数据流生成。该方法通过几何聚类锚点选择、策略头脑风暴与反思机制以及动态批次门控，在显著减少训练样本量的同时维持了与全量数据相当的性能。其核心价值在于解决了自训练过程中的数据动态性缺失问题，但绝对性能提升有限，且对超参数敏感。

】

---

【UniGeM: Unifying Data Selection and Mixing via Geometric Exploration and Mining ｜统一数据混合与选择的几何流形近似框架

研究机构：意大利都灵理工大学、中国科学院

作者：Changhao Wang、Yunfeiyu、Xinhao Yao 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_223b073fdbfb)

> 代码预训练面临数据混合与实例选择解耦导致的结构断裂问题，现有方法或依赖代理模型引入偏差，或忽略域内层级依赖。UniGeM 将数据策展重构为流形近似问题，通过两级几何聚类统一宏观预算分配与微观质量筛选。该框架在 8B MoE 模型上实现了 2.0 倍的数据效率提升，但其几何假设在非结构化文本语料中的适用性仍存疑。

】

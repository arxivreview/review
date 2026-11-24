# ICLR2026 · CAD B-Rep 生成与理解方向论文汇编

> 本方向共 2 篇（ICLR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【CAD-Tokenizer: Towards Text-based CAD Prototyping via Modality-Specific Tokenization ｜统一文本驱动CAD原型设计

研究机构：加拿大多伦多大学、微软研究院

作者：Ruiyu Wang、Shizhao Sun、Weijian Ma 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.21150)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.21150)

> 文本驱动CAD生成与编辑长期被割裂为两个独立任务，前者依赖强生成能力，后者要求精确的指令理解与几何对齐，现有方法无法在单一模型中同时满足这两种互补但互斥的技能需求。本文指出通用LLM分词器将CAD序列碎片化为自然语言词片，导致注意力机制无法捕捉原语级结构依赖，这是统一建模失效的根本原因。通过引入原语级VQ-VAE分词器与有限状态自动机引导采样，CAD-Tokenizer在统一框架下同时实现了Text-to-CAD生成与CAD编辑，在两项任务的核心指标上均超越任务特定基线与通用LLM。该方法验证了模态特定分词对LLM处理结构化序列的有效性，但其对复杂自由曲面的支持及几何水密性的保证仍存疑。

】

---

【Learning Hierarchical and Geometry-Aware Graph Representations for Text-to-CAD ｜层级化几何感知图表示的文本到CAD生成

研究机构：华南理工大学

作者：Shengjie Gong、Wenjie Peng、Hongyuan Chen 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.10075)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.10075)

> 文本到CAD（Text-to-CAD）任务旨在将自然语言指令转化为可执行的计算机辅助设计（CAD）程序，其核心难点在于长程依赖导致的误差累积与复杂装配体中几何约束的失效。现有端到端方法将设计过程扁平化为线性序列，缺乏对装配层级与空间关系的显式建模，导致局部错误在复杂设计中级联放大。本文提出学习层级化几何感知图作为中间表示，通过三阶段流水线（几何分解、动作规划、代码生成）将长程生成解耦为可处理的子任务，并引入结构感知渐进课程学习机制以突破模型能力边界。该方法在几何约束满足度上显著优于基线，但其图结构对非层级化自由曲面的表达能力及小样本数据下的泛化上限仍存疑。

】

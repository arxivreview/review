# ACL-Findings2026 · 大语言模型的缩放定律方向论文汇编

> 本方向共 3 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Establishing a Scale for Kullback-Leibler Divergence in Language Models Across Various Settings ｜建立语言模型跨场景 KL 散度统一尺度

作者：Ryo Kishino、Yusuke Takase、Momose Oyama 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ad47a38834ca)

> 语言模型训练中的权重参数因排列对称性和架构依赖而难以直接比较，导致无法量化不同训练阶段、量化版本或中间层之间的行为差异。现有基于权重的分析无法提供跨架构的统一度量，而 Oyama et al. (2025) 提出的对数似然向量虽能嵌入不同架构，但未建立可解释的绝对尺度。本文通过双中心对数似然向量构造几何空间，确立了 KL 散度在预训练、量化、微调及层级间的统一比特/字节尺度，并揭示了似然空间轨迹的亚扩散特性。该工作提供了模型行为变化的几何标尺，但其结论局限于 Pythia 家族且未验证对下游任务预测的直接增益。

】

---

【How to Set the Learning Rate for Large-Scale Pre-training? ｜大规模预训练学习率配置：拟合与迁移范式对比

研究机构：复旦大学

作者：Yunhua Zhou、Shuhao Xing、Junhao Huang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.05049)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.05049)

> 大规模预训练的核心瓶颈在于学习率（Learning Rate, LR）配置的高昂试错成本，直接决定训练稳定性与收敛效率。现有方法要么依赖组合爆炸的网格搜索，要么依赖 Maximal Update Parametrization (µP) 迁移但缺乏大规模实证验证。本文切入点是将 LR 配置形式化为“拟合”与“迁移”两大范式，并首次在 12B 参数 MoE 架构下对比二者。通过引入搜索因子缩放律降低拟合复杂度，并扩展 µP 至深度与权重衰减维度，本文揭示了 µP 在工业级规模下的性能衰减。其价值在于提供了可操作的 LR 配置指南，但结论局限于 Qwen3-MoE 单一架构与 WSD 调度，对动态 Batch Size 等场景的适用性存疑。

】

---

【Scaling Laws for Code: Every Programming Language Matters ｜多语言代码预训练缩放定律

研究机构：北京航空航天大学、中国人民大学

作者：Jian Yang、Shuyue Guo、Linzheng Chai 等 11 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_3f7842f1f2e0)

> 通用自然语言缩放定律假设数据同质，无法指导多语言代码库中不同编程语言的令牌分配，导致资源浪费与性能预测偏差。现有代码缩放研究仅关注单语言或整体数据量，忽略了语言间的语法异构性与跨语言迁移效应。本文通过1000+次从头训练实验，建立比例依赖的多语言缩放模型，量化各语言独立缩放指数与协同增益。该工作填补了代码域多语言资源分配的理论空白，但其最优分配策略在极端数据受限下的鲁棒性存疑。

】

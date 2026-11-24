# ACL-Findings2026 · 主题建模与神经主题模型方向论文汇编

> 本方向共 3 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【CobwebTM: Probabilistic Concept Formation for Lifelong and Hierarchical Topic Modeling ｜基于概率概念形成的终身层级主题建模

研究机构：美国佐治亚理工学院

作者：Karthik Singaravadivelan、Anant Gupta、Zekun Wang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8af5d776eb97)

> 主题建模在流式数据场景下面临灾难性遗忘与固定主题容量的双重瓶颈，传统神经模型依赖批量训练且难以动态重构语义结构。本文切入点在于摒弃参数化神经网络的增量更新机制，转而利用预训练嵌入空间中的符号化概念形成算法。COBWEBTM通过增量构建概率概念树，实现了无需预设主题数的终身层级主题发现。该方法在连贯性与稳定性上优于基线，但其对高维嵌入空间贪心搜索的计算复杂度及缺乏与最新LLM驱动方法的对比，限制了其结论的普适性。

】

---

【From Documents to Segments: A Contextual Reformulation for Topic Assignment ｜基于片段的主题分配

研究机构：LG AI研究院、美国伊利诺伊大学厄巴纳-香槟分校

作者：Hoonsang Yoon、Takyoung Kim、Wonkee Lee 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.17714)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b18b37880a6c)

> 主题建模长期受困于“主题污染”，即多主题文档中无关内容稀释特定主题，导致下游检索与摘要失效。现有文档级方法（DBTA）将整篇文档视为语义原子，无法隔离局部语义，而LLM虽能识别片段证据，却仅将其作为解释辅助而非推断主体。本文提出SBTA，将主题分配的基本单元从文档迁移至片段，并构建SemEval-STM基准与片段入侵评估任务，验证了该范式在提升主题纯度与可解释性上的有效性。其价值在于重新定义了任务边界，但片段提取对LLM的依赖及自动指标在短文本上的失效，使其结论的普适性仍存疑。

】

---

【Towards Modern Topic Models: A Survey of Taxonomies and Paradigm Shifts from Algorithm-Centric to LLM-Centered Topic Analysis ｜现代主题建模：从算法中心到LLM中心的范式转移

研究机构：北京邮电大学、北京科技大学

作者：Xuan Xu、Zhongliang Yang、Haolun Li 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f6a7f7c1d1b0)

> 主题建模旨在从高维稀疏文本中挖掘潜在语义结构，其核心价值在于将非结构化数据降维为可解释的低维主题空间。随着大语言模型（Large Language Models, LLM）的介入，领域重心从概率生成与嵌入聚类转向语义推理与系统级工程，形成了算法中心、LLM辅助与LLM中心并存的多元格局。本文通过构建新的分类法，梳理了LLM在主题建模中的角色演变，并提出了面向未来的智能体系统蓝图。该综述填补了现有分类在系统架构上的空白，但LLM中心范式下的稳定性与评估基准缺失仍是核心争议。

】

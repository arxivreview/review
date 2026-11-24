# ACL-Findings2026 · 法律大语言模型应用与评估方向论文汇编

> 本方向共 3 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【LexGenius: An Expert-Level Benchmark for Large Language Models in Legal General Intelligence ｜法律通用智能专家级基准

研究机构：新加坡南洋理工大学、南京大学

作者：Wenjin Liu、Haoran Luo、Xin Feng 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_06abb52b508f)

> 法律领域长期缺乏能区分“模式模仿”与“真实理解”的评测标准，现有基准多聚焦静态任务结果，忽视伦理判断等软性智能维度。本文切入点在于构建覆盖七维度、十一任务、二十能力的三级框架，将法律软智能纳入系统化评估。通过8,385道原创选择题与12个SOTA模型对比，揭示了LLM在价值权衡与情境适应上的系统性缺陷。其价值在于填补了法律智能评估的结构性空白，但选择题形式能否真正承载过程评估的深度仍存疑。

】

---

【ViLegalLM: Language Models for Vietnamese Legal Text ｜越南法律领域适配语言模型

作者：Truong-Phuc Nguyen、Quy-Nhan Nguyen、Minh-Tien Nguyen

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_80683ca50ecc)

> 越南法律文本处理长期受限于语料规模小与模型架构单一，导致通用模型在专业术语理解与逻辑推理上表现不佳。现有方案多基于小规模语料或从指令微调模型出发，难以兼顾领域深度与基础能力。本文切入点在于构建大规模越南法律语料并从Base模型进行持续预训练，同时通过合成数据缓解标注稀缺。其价值在于确立了开源越南法律模型的新基线，但其在复杂推理任务上的表现仍受限于参数规模与数据质量。

】

---

【When Rules Learn: A Self-Evolving Agent for Legal Case Retrieval ｜法律案例检索中的自进化查询重写

作者：Mingxu Tao、Jiawei Hu、Xian Zhou 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.17220)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.17220)

> 法律案例检索面临查询与长文本判决间词汇鸿沟，导致语义匹配失效。现有密集检索模型在特定法律基准上表现不及传统BM25，而人工设计重写规则成本高且泛化性差。本文提出一种无参数更新的自进化智能体框架，通过迭代生成、验证与淘汰重写规则来增强BM25。该方法在特定大模型驱动下提升了检索召回率，但其有效性高度依赖核心模型的推理能力，且未解决规则空间爆炸导致的搜索效率瓶颈。

】

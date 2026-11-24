# ACL-Findings2026 · 语言模型中的分词技术方向论文汇编

> 本方向共 3 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【FLEXITOKENS: Flexible Tokenization for Evolving Language Models ｜柔性分词器：基于区间约束的字节级语言模型

研究机构：美国俄亥俄州立大学、美国华盛顿大学

作者：Abraham Toluwase Owodunni、Orevaoghene Ahia、Sachin Kumar

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_03d4d7d482ac)

> 现有字节级语言模型在适配新领域或未见语言时，因预训练阶段锁定的固定压缩率导致过度碎片化，严重损害推理效率与下游性能。FLEXITOKENS 通过引入铰链损失替代传统的二项分布正则项，允许压缩率在特定区间内自由波动，从而解耦了分词策略与单一分布的绑定。该方法在保持多语言公平性的同时，显著提升了模型在分布外数据上的适应能力。尽管在中等规模模型上验证了有效性，但其在大参数模型下的训练稳定性及跨域泛化边界仍存疑。

】

---

【MorphBPE: Morphology-Aware Tokenization for Efficient LLM Training ｜形态感知字节对编码

研究机构：德国人工智能研究中心

作者：Ehsaneddin Asgari、Yassine El Kheir、MohammadAli SadraeiJavaheri 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_6bc7c87ad3e4)

> 子词分词器在形态丰富语言中常因纯频率驱动导致词素边界断裂，引发模型学习负担增加。现有统计分词方法难以兼顾压缩效率与语言学结构，而纯形态分析器又缺乏数据驱动的灵活性。本文提出 MorphBPE，在 BPE 训练阶段引入词素边界约束，推理阶段保持标准 BPE 行为。该方法在受控实验中降低了交叉熵并提升了下游任务表现，但其依赖高质量形态标注，在资源稀缺语言中的可扩展性存疑。

】

---

【Multilingual Tokenization through the Lens of Indian Languages: Challenges and Insights ｜印度语言多语言分词：正字法归一化与词汇表聚类策略

研究机构：印度理工学院、印度理工学院孟买分校

作者：Maharaj Brahma、N J Karthika、Rajat Verma 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_40a63e8a95c3)

> 多语言分词器在低资源语言上常因高资源语言主导词汇表分配而导致分词碎片化，进而推高计算成本并削弱模型对形态结构的捕捉能力。现有静态分词方法虽能处理开放词汇，但难以应对印度语言特有的正字法变体与复杂形态结构，导致同一语义单元被映射为多个冗余 Token。本文通过引入脚本/正字法归一化预处理，并采用基于语言家族的聚类策略构建多语言词汇表，系统评估了 17 种印度语言的分词效率与下游任务表现。该研究提供了针对形态丰富语言的实证指导，但其结论局限于静态分词框架，未探索动态分词架构在解决此类结构性不公上的潜在优势。

】

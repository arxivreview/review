# ACL2026 · 人类与LLM标注质量方向论文汇编

> 本方向共 2 篇（ACL2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【CaBSALLM: Efficient Context-Aware Batch Annotation of Conversational Streams with Large Language Models ｜上下文感知动态批处理流式标注

研究机构：美国犹他大学、美国弗吉尼亚大学

作者：Mohammadsadegh Abolhasani、Reza Mousavi、Paul Jen-Hwa Hu

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f92b57bb9e2a)

> 大规模主观社会互动标注面临人工成本高与LLM语境理解失效的双重瓶颈，现有高可靠性框架因多轮推理导致延迟不可接受，而高效批处理又因缺乏语境导致语义错误。本文切入点在于将网络拥塞控制算法引入LLM推理过程，通过实时调整批大小来平衡吞吐量与解析成功率。具体做法是构建全局主播画像与局部对话窗口的双层上下文，并采用AIMD控制器动态优化批处理参数。该方案在保持预测性能的同时大幅降低成本，但其有效性依赖于特定API环境下的代理信号稳定性，跨平台泛化能力存疑。

】

---

【Refining and Reusing Annotation Guidelines for LLM Annotation ｜迭代指南修订

研究机构：日本国立情报学研究所

作者：Kon Woo Kim、Jin-Dong Kim、Akiko Aizawa

论文原文见 [arXiv](https://arxiv.org/abs/2605.20809)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_06cbc1a6f169)

> 生物医学命名实体识别（NER）中，大语言模型（LLM）常因无法精确遵循领域特定的边界规则而产生系统性错误。静态注入指南虽能提升性能，但无法解决指南本身的模糊性与模型先验的冲突。本文提出一种模拟人类标注者培训过程的迭代Moderation框架，通过自动化的差异分析与规则生成，动态修订指南文本以对齐LLM输出。该方法在NCBI Disease数据集上实现了0.62的F1分数，验证了推理模型在指南遵循中的优势，但其对测试集的隔离策略限制了泛化能力的直接评估。

】

# ACL-Findings2026 · 习语表达处理方向论文汇编

> 本方向共 2 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【ID10M-JAM: Stress-Testing Idiom Identification Under Challenging Context ｜对抗语境下的习语识别鲁棒性测试

作者：Kai Golan Hashiloni、Lior Livyatan、Ofri Hefetz 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f32e43a0fca1)

> 习语识别旨在从连续文本中定位非组合性语义表达，但大语言模型（LLM）在标准基准上的高分掩盖了其面对误导性语境时的脆弱性。现有评估多依赖静态、语义清晰的样本，无法区分模型是依赖深层语义推理还是表面统计记忆。本文通过构建ID10M-JAM基准，注入人类无歧义但模型易混淆的对抗性上下文，量化模型在字面与习语意义消歧中的性能漂移。该工作揭示了当前LLM在习语理解上的系统性鲁棒性瓶颈，但其评估指标的设计存在基线依赖缺陷，且缺乏对内部机制的解释。

】

---

【When Meaning Travels: A Granular Lens on Hybrid-MoE’s Role in Idiomatic Understanding for Language Models ｜混合专家习语理解框架

研究机构：印度理工学院

作者：Sarmistha Das、Vaibhav Vishal、Shreyas Guha 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_600188a3e843)

> 习语的非组合性语义在低资源语言中因缺乏大规模平行语料而难以被视觉语言模型（VLM）准确解码，现有基准多聚焦英语且忽略情感语调维度。本文切入点在于构建涵盖印地语、孟加拉语和泰语的Varnika数据集，并引入混合专家架构以解耦文本与视觉线索。通过超网络共享专家知识并注入习语属性信号，该框架在V-FLUTE上将IV分数从0.75提升至0.89。其价值在于填补了多模态习语语调建模的空白，但语调识别准确率仍低于0.6，表明文化细微差别的捕捉能力有限。

】

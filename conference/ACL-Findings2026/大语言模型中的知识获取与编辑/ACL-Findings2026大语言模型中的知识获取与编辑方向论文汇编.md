# ACL-Findings2026 · 大语言模型中的知识获取与编辑方向论文汇编

> 本方向共 1 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【G-HiRel: Enhancing the Adaption to Knowledge Updating for Large Language Model Reasoning ｜层级关系检索增强知识编辑推理

研究机构：西北工业大学

作者：Yudai Pan、Jiajie Hong、Tianzhe Zhao 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_5dcec26db25e)

> 大语言模型在参数冻结状态下难以适应大规模知识更新，尤其在多跳推理中，直接修改参数成本高昂且易引发灾难性遗忘。现有外部记忆方法虽能规避参数更新，但受限于知识图谱（KG）结构化三元组与LLM连续表示间的语义鸿沟，以及实体依赖导致的知识不一致。本文提出G-HiRel，通过层级指令生成与基于关系语义的多步扩展检索，将KG中的关系路径而非实体作为推理骨架，实现编辑后知识的鲁棒整合。该方法在MQuAKE基准上显著提升了多跳推理准确率与路径可解释性，但其性能高度依赖底层LLM的指令解析能力，且未解决检索延迟与长程依赖建模的系统性瓶颈。

】

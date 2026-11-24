# ACL-Findings2026 · 科学文献挖掘与学术知识发现方向论文汇编

> 本方向共 3 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Datasets for Scientific Literature Understanding: A Survey ｜科学文献理解数据集综述

研究机构：中国科学院、中国科学院大学

作者：Yuanzhe Zhang、Xun Zhao、Maodi Hu 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2b37f13faa67)

> 科学文献理解旨在将非结构化学术产出转化为可计算的知识基础设施，但现有资源分散且缺乏统一分类标准，导致模型训练与评估缺乏系统性参照。本文切入点在于构建首个覆盖结构、文本、多模态及预训练指令微调的四层数据集分类体系，系统梳理了从底层感知解析到高层语义推理的数据资源全景。该工作通过静态属性映射而非动态性能评测，为领域提供了数据选型的概念脚手架。其价值在于填补了资源索引的空白，但缺乏对数据集间依赖关系及动态演化能力的量化评估，难以直接指导智能体工作流的数据构建。

】

---

【SciImpact: A Multi-Dimensional, Multi-Field Benchmark for Scientific Impact Prediction ｜科学影响力多维预测基准

研究机构：美国德州农工大学、加拿大滑铁卢大学

作者：Hangxiao Zhu、Yuyu Zhang、Ping Nie 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17141)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a699f1ab3923)

> 科学文献影响力长期被简化为引用计数，导致对奖项、专利及代码采纳等关键维度的评估缺失。现有单一指标预测模型无法捕捉跨领域、多模态证据下的复杂影响机制，且缺乏统一的多维评估环境。本文构建了覆盖19个学科、7个影响维度的对比对基准，并通过多任务指令微调验证了小模型在该任务上的有效性。该工作填补了多维影响力评估的空白，但其对比对构建策略可能引入选择偏差，且缺乏与传统机器学习基线的直接对比。

】

---

【SudokuFill: A Multi-Agent Progressive Filling Framework for Document-Level Scientific Information Extraction ｜科学信息抽取的渐进式多智能体填充框架

研究机构：中国科学院、中国科学院大学

作者：Yang Li、Yajiao Wang、Yu Zhang 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_83812d28955b)

> 科学文献挖掘旨在将非结构化文本转化为可计算的知识基础设施，但传统“局部抽取后组装”范式在长文档中因字段隔离导致全局关联断裂。现有方法依赖静态知识图谱或单次生成，难以利用高置信度结果作为内部监督来约束后续不确定字段。本文提出 SudokuFill，将文档级科学信息抽取重构为类似数独的渐进填充问题，通过全局状态复用与多智能体辩论实现约束传播。该框架在疫苗佐剂基准上达到 51.83% 的整体准确率，并验证了 7B 模型超越 GPT-4o 的架构补偿效应，但其泛化性受限于自建基准的领域特异性。

】

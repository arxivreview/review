# ACL-Findings2026 · 放射学报告生成与分析方向论文汇编

> 本方向共 2 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Multimodal Dual-Path Decoding for Medical Report Generation ｜多模态双路径大模型解码用于放射学报告生成

研究机构：厦门大学、北京大学

作者：Jinghan Sun、Dong Wei、Zhihong Zhu 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a6f825379f32)

> 放射学报告生成（RRG）旨在从医学图像自动产生结构化临床文本，其核心价值在于缓解影像检查量激增与放射科医生短缺之间的结构性矛盾。现有方法多依赖大型视觉语言模型（LVLM）或大型语言模型（LLM）单一路径，前者视觉接地强但缺乏细粒度临床知识，后者语义丰富但易产生幻觉。本文提出在解码阶段对LVLM与LLM进行token级概率加权融合，并引入多标签分类提示以增强LLM的临床约束。该框架在MIMIC-CXR上提升了临床实体指标，但缺乏对融合权重动态调整机制的探索，且未解决3D体积数据的空间连续性难题。

】

---

【X-ray Made Simple: Lay Radiology Report Generation and Robust Evaluation ｜通俗化放射学报告生成与语义鲁棒评估

研究机构：美国匹兹堡大学、英国杜伦大学

作者：Kun Zhao、Chenghao Xiao、Sixing Yan 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_38dfcadccf97)

> 放射学报告生成（RRG）长期受困于专业术语导致的患者理解障碍与词汇重叠指标引发的评估失真。现有方法通过优化编码器-解码器架构提升流畅性，却忽视了报告模板化对模型语义泛化的负面约束。本文切入点在于将“患者可及性”与“评估鲁棒性”视为同源问题，通过构建通俗化数据集并引入基于嵌入的语义匹配指标，验证语言风格对模型训练动态的影响。该框架在语义一致性上表现稳健，但未解决视觉证据接地的核心临床难题。

】

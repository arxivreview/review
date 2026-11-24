# ACL-Findings2026 · 视觉-语言对齐与多模态表示学习方向论文汇编

> 本方向共 3 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Beyond Cross-Modal Alignment: Measuring and Leveraging Modality Gap in Vision-Language Models ｜模态主导性评分与无训练干预

研究机构：英国牛津大学、美国麻省理工学院

作者：Hanqi Yan、Xiangxiang Cui、Lu Yin 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d343647e20f7)

> 视觉语言模型（VLMs）长期面临模态特异性信息被全局对齐掩盖的问题，导致无法对单一模态特征进行独立控制。现有几何修正方法如子空间投影旨在消除模态间隙，却忽视了间隙中蕴含的功能性分化潜力。本文提出模态主导性评分（MDS）量化维度级模态归属，并基于此实现无训练的行为干预。该方法将模态间隙从“缺陷”重构为“资源”，但在复杂推理任务中的普适性尚未得到验证。

】

---

【e5-omni: Explicit Cross-modal Alignment for Omni-modal Embeddings ｜全模态显式对齐框架

研究机构：中国人民大学、日本早稻田大学

作者：Haonan Chen、Sicheng Gao、Radu Timofte 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.03666)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.03666)

> 全模态检索旨在将文本、图像、音频、视频等异构数据映射至统一空间以支持跨模态匹配，但现有方法多依赖视觉语言模型（Vision-Language Model, VLM）预训练带来的隐式对齐，导致混合模态批次中相似度尺度失衡与几何分布漂移。本文提出 e5-omni，一种轻量级显式对齐框架，通过模态感知温度校准、可控负样本课程与批次白化协方差对齐，在不修改骨干网络的前提下修正对比学习中的梯度失衡与二阶统计量不匹配。该框架在 MMEB-V2 与 AudioCaps 上取得一致增益，验证了显式几何校准对全模态嵌入的必要性，但其对纯文本任务性能的影响及音频/视频时序几何特性的处理仍存疑。

】

---

【Preserving Language Capabilities in Vision-Language Models via Representation Regulation ｜视觉语言模型中的表示正则化

研究机构：华南理工大学、美国卡内基梅隆大学

作者：ZiXuan Chen、Juncheng Tao、Ziqian Zeng

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8d1f370c08eb)

> 视觉语言模型（VLM）在提升多模态推理能力的同时，往往导致纯文本任务性能显著下降，这一现象被称为语言退化。现有方法多通过冻结参数或增加文本数据来缓解，但未能触及退化根源。本文指出退化源于后表示层内的“表示混合”，并提出基于再生核希尔伯特空间（RKHS）的表示分布差异（RDD）损失，在训练早期约束嵌入距离以保护语言能力。该方法在保持视觉性能的同时有效恢复了语言基准得分，但其效果依赖于对后表示层边界的模糊界定，且未验证在极端数据规模下的边际收益。

】

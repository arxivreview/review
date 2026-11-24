# Others2026 · 跨模态知识蒸馏方向论文汇编

> 本方向共 1 篇（Others2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Switch-KD: Visual-Switch Knowledge Distillation for Vision-Language Models ｜Switch-KD：统一概率空间下的视觉-语言知识蒸馏

作者：Haoyi Sun、Xiaoxiao Wang、Ning Mao 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.14629)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.14629)

> 跨模态知识蒸馏旨在解决多模态大模型（MLLMs）在边缘部署中算力与精度难以兼得的矛盾。现有方法如 LLaVA-KD 和 Align-KD 将视觉与语言监督割裂，导致模态间耦合信息丢失，知识转移效率受限。Switch-KD 提出将学生视觉输出切换至教师语言路径，在共享文本概率空间内通过动态双向 Logits 差异损失实现隐式视觉知识迁移。该框架在 10 个基准上超越现有蒸馏方法，但其对组合推理任务的增益有限，且依赖教师语言路径的“解释”能力，其泛化边界尚待验证。

】

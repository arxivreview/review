# Others2026 · 反事实生成与推断方向论文汇编

> 本方向共 1 篇（Others2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Causal-Adapter: Taming Text-to-Image Diffusion for Faithful Counterfactual Generation ｜因果适配器：驯服文本到图像扩散模型以实现忠实反事实生成

研究机构：英国爱丁堡大学

作者：Lei Tong、Zhihua Liu、Chaochao Lu 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.24798)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.24798)

> 反事实图像生成旨在回答“若某属性改变，图像将如何变化”，但现有方法常陷入属性纠缠，导致干预目标属性时非目标属性发生非预期改变。传统扩散模型虽具备高保真生成能力，却缺乏显式因果机制，难以保证干预的因果忠实性。本文提出 Causal-Adapter，通过冻结预训练文本到图像扩散骨干并注入可插拔因果适配器，结合提示对齐注入与条件令牌对比损失，实现属性解耦与因果一致的反事实编辑。该方法在 CelebA 和 ADNI 数据集上显著提升了干预有效性与图像真实性，但其依赖预定义因果图且未解决复杂动态系统中的因果结构自动发现难题。

】

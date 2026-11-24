# ACL-Findings2026 · 文本到图像扩散中的布局与构图控制方向论文汇编

> 本方向共 1 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Mechanistic Interpretability of Text-to-Image Diffusion Models via Cross-Attention Interventions ｜交叉注意力因果干预下的扩散模型机制可解释性

作者：Maisha Maliha、Dean F. Hougen

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ddd3a8113a00)

> 文本到图像扩散模型在生成高保真图像时，常出现物体遗漏或属性错配，但其内部如何将提示词语义映射至像素结构仍缺乏透明解释。现有注意力可视化方法仅反映查询与键的对齐概率，无法量化语义信号的实际注入量，更无法建立内部组件与语义功能的因果联系。本文通过固定种子移除单个Token生成反事实图像，结合投影输出范数计算Token接地图与Head级KL散度敏感性，构建了从词元到注意力头的因果归因框架。该框架揭示了语义接地的稀疏性与Head特异性，但在U-Net架构上的结论能否泛化至DiT架构，以及归因精度提升是否必然转化为生成质量增益，仍存疑。

】

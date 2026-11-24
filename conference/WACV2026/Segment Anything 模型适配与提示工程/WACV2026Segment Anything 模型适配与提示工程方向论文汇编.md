# WACV2026 · Segment Anything 模型适配与提示工程方向论文汇编

> 本方向共 1 篇（WACV2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Decoupling Shape and Texture in SAM-2 via Controlled Texture Replacement ｜解耦形状与纹理：基于受控纹理替换的 SAM-2 偏置校准

研究机构：以色列特拉维夫大学、美国马里兰大学帕克分校

作者：Inbal Cohen、Boaz Meivar、Peihan Tu 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ff1fbc2e854a)

> 分割基础模型在纹理主导场景中因形状归纳偏置导致过度分割，现有微调方法依赖大规模纹理标注或仅针对分类任务，无法系统性校准分割模型的纹理敏感性。本文切入点在于利用现有语义分割数据，通过受控纹理替换生成训练集，无需新增人工标注即可引导模型从形状依赖转向纹理感知。具体做法是构建 Textured-ADE20K 数据集，通过混合参数 η 渐进替换语义区域内的纹理，微调 SAM-2 得到 TextureSAM。该方法在纹理基准上显著提升了分割性能，但代价是通用语义分割能力的下降，且全量微调的计算成本限制了其在资源受限场景的适用性。

】

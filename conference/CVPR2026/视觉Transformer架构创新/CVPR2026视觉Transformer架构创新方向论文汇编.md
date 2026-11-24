# CVPR2026 · 视觉Transformer架构创新方向论文汇编

> 本方向共 3 篇（CVPR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Convolutional Neural Networks Driven by Content Similarity ｜内容相似度驱动的卷积聚合机制

研究机构：中南大学

作者：Ligeng Zou、Guihu Zhao

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d6069601f13a)

> 视觉识别领域长期面临自注意力机制计算复杂度随序列长度平方增长的瓶颈，而纯卷积网络又因依赖固定空间位置而缺乏内容依赖的全局建模能力。现有混合架构虽试图融合两者优势，但往往引入额外的参数开销或复杂的注意力模块。本文切入点在于重新解释门控卷积，通过引入通道内排序操作，将特征相似度映射为相对位置，使局部卷积隐含全局感受野。具体做法是构建双分支Token Mixer，其中一支利用排序后的一维深度卷积实现内容驱动的信息聚合。该设计在保持亚二次方复杂度的同时，使纯CNN架构在多项基准上超越了部分Transformer模型，但其对密集预测任务中空间拓扑结构的破坏性影响尚未得到充分验证。

】

---

【Random Wins All: Rethinking Grouping Strategies for Vision Tokens ｜随机分组策略

研究机构：中国科学院、中国科学院大学

作者：Qihang Fan、Yuang Ai、Huaibo Huang 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.00486)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.00486)

> Vision Transformer 的核心瓶颈在于自注意力机制随 Token 数量呈二次方增长，导致高分辨率图像处理成本极高。现有方案通过精心设计的空间窗口或语义聚类来降低复杂度，但引入了复杂的分组操作，增加了部署难度且未必必要。本文提出一种极简的随机分组策略，通过固定随机张量对 Token 进行排序并等分，替代复杂的分组逻辑。该方法在多个基准上超越了精心设计的基线，但其优势高度依赖于位置编码与多头多样性，在数据受限场景下的鲁棒性存疑。

】

---

【TAS-LoRA: Transformer Architecture Search with Mixture-of-LoRA Experts ｜Transformer 架构搜索中的低秩专家混合机制

研究机构：韩国延世大学、韩国科学技术研究院

作者：Jeimin Jeon、Hyunju Lee、Bumsub Ham

论文原文见 [arXiv](https://arxiv.org/abs/2605.07256)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.07256)

> 现有 One-shot Transformer 架构搜索（TAS）依赖超网共享权重以节省算力，但导致不同子网特征表示高度同质化，无法充分挖掘特定架构的潜力。本文指出这一“特征坍塌”现象是限制子网性能的核心瓶颈，并引入低秩适配（LoRA）与混合专家（MoLE）机制，在冻结超网权重的基础上为每个子网学习特异性特征。该方法在 ImageNet 上以极小的额外参数开销提升了搜索精度，但其路由器仅基于静态架构属性，对动态硬件约束的适应能力存疑。

】

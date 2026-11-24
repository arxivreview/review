# ACL-Findings2026 · Transformer的机制可解释性方向论文汇编

> 本方向共 2 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Trustworthy and Explainable Causal Representation Learning in Transformers ｜因果可识别解释模型

作者：Yang Liu、Yinghao Zhang、Lin Liu 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2b3b97093598)

> 可解释人工智能（XAI）旨在通过量化输入特征重要性来揭示模型决策逻辑，但传统掩码方法缺乏理论保证，导致解释结果可能源于数据噪声而非真实因果机制。现有方法多聚焦于保真度（Faithfulness），即解释是否反映模型行为，却忽视了可识别性（Identifiability），即解释是否由真实数据分布唯一确定。CIEM 通过构建结构因果模型（SCM），将注意力机制分解为权重与值两个潜变量，利用可识别变分自编码器（iVAE）理论确保解释的唯一性。该方法在理论上填补了掩码解释的歧义性漏洞，但其依赖生成模型拟合而非因果干预，在机制可解释性（MI）坐标系中缺乏因果必要性的直接验证。

】

---

【Where meaning lives: Layer-wise accessibility of psycholinguistic features in encoder and decoder language models ｜心理语言学特征的层间可解码性：嵌入提取方法与架构约束的交互作用

研究机构：德国柏林工业大学、瑞士巴塞尔大学

作者：Taisiia Tikhomirova、Dirk U. Wulff

论文原文见 [arXiv](https://arxiv.org/abs/2601.03798)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.03798)

> 本文旨在厘清Transformer内部各层对情感、具体性等心理语言学维度的编码分布，以解决现有探测研究中因固定单一嵌入提取策略导致的层间定位结论不稳定问题。既往工作多依赖最终层表征或孤立词嵌入，忽视了上下文提取方式对可解码性的系统性影响，本文通过交叉对比三种提取方法与十种架构模型，揭示了提取方法本身是层间定位的第一序变量。具体做法是构建统一线性探测框架，量化不同提取策略下58个人工验证特征在各层的Selectivity与中心质量（Center of Mass, COM）。该研究为表征几何分析提供了方法论修正，但其结论限于线性可解码性，未触及因果必要性，且未验证提取方法差异是否掩盖了架构本身的层间分布规律。

】

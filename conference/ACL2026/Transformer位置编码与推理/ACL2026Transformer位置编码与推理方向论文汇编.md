# ACL2026 · Transformer位置编码与推理方向论文汇编

> 本方向共 2 篇（ACL2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【A Mechanistic Account of Attention Sinks in GPT-2: One Circuit, Broader Implications for Mitigation ｜注意力汇聚的因果机制解析

研究机构：以色列特拉维夫大学

作者：Yuval Ran-Milo、Hila Ofek、Shahar Mendel

论文原文见 [arXiv](https://arxiv.org/abs/2604.14722)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.14722)

> 注意力汇聚（Attention Sink）指Transformer模型将不成比例的注意力权重分配给序列首位置的现象，该现象削弱了有效上下文利用并干扰量化过程。现有研究多停留在现象观察或统计相关性层面，缺乏对具体参数路径的因果归因，导致跨架构的缓解策略难以泛化。本文通过结构分析与定向因果干预，在GPT-2中定位了由查询偏置、首层MLP变换及键投影结构共同构成的汇聚回路。这一机制解释揭示了注意力汇聚并非单一位置编码缺陷，而是架构组件协同适应的结果，但其结论局限于绝对位置编码架构，对旋转位置编码等主流范式的适用性存疑。

】

---

【SCOPE: Boosting LLM Efficiency with Scoped Position Encoding ｜结构化稀疏位置编码

研究机构：浙江大学

作者：Qingguo Qi、Hongyang Chen、Zhao Li

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e998af24c46c)

> 长上下文建模面临计算复杂度与位置泛化的双重瓶颈，显式位置编码（PE）如 RoPE 在超长序列下存在精度敏感与额外算术开销，而纯隐式 NoPE 性能又显著弱于显式方案。SCOPE 将结构化稀疏性本身重构为隐式位置编码机制，通过为注意力头分配指数级扩展的回看窗口，使顺序感知能力随网络深度指数增长。该方法在 LLaMA-3-8B 上实现了 4 倍训练长度的零样本外推与 2.1 倍预填充加速，但其理论假设对注意力分布的熵值依赖较强，在极端低熵场景下的鲁棒性仍存疑。

】

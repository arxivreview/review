# ACL2026 · Transformer的机制可解释性方向论文汇编

> 本方向共 1 篇（ACL2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【TensorLens: End-to-End Transformer Analysis via High-Order Attention Tensors ｜高阶张量统一表示

研究机构：以色列特拉维夫大学

作者：Ido Andrew Atad、Itamar Zimerman、Shahar Katz 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.17958)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.17958)

> 机制可解释性（Mechanistic Interpretability, MI）旨在通过逆向工程揭示 Transformer 内部计算机制，但现有注意力聚合方法仅覆盖部分组件，导致全局行为解释存在盲区。本文切入点在于将包含 FFN、归一化及嵌入层在内的整个 Transformer 重构为单一的高阶数据控制线性算子，以消除启发式聚合的信息损失。通过引入四阶张量结构并设计多种坍缩策略，该方法在扰动测试中显著优于传统矩阵基线。其价值在于提供了理论上完备的统一视角，但高阶张量的计算复杂度与线性化假设的局限性仍存疑。

】

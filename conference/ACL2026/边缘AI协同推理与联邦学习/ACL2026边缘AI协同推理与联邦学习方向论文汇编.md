# ACL2026 · 边缘AI协同推理与联邦学习方向论文汇编

> 本方向共 1 篇（ACL2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【EdgeFormer: Latency-Aware Collaborative Multi-Head Attention of Transformer Inference in Edge Networks ｜边缘Transformer推理的延迟感知协同多头注意力

研究机构：北京航空航天大学、中国科学院

作者：Yiming Yao、Jianwei Niu、Bin Dai 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ca92cb54c3cb)

> 边缘大语言模型推理面临算力与存储的双重瓶颈，传统静态块级分割无法适应动态网络波动，且将多头注意力视为不可分割单元导致并行度浪费。EdgeFormer通过效率-存储优先级排序分配Transformer块，并引入协同多头注意力机制，在实时资源约束下动态分配或剪枝注意力头。该方法在SuperGLUE基准上实现了最高2.01倍的推理加速，精度损失控制在1.06%以内，但其在异构设备下的通信开销控制与长期动态适应性仍需进一步验证。

】

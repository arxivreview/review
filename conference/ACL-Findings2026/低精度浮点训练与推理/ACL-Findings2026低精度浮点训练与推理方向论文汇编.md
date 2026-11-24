# ACL-Findings2026 · 低精度浮点训练与推理方向论文汇编

> 本方向共 2 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【FLOP-Efficient Training: Early Stopping Based on Test-Time Compute Awareness ｜测试时计算感知训练

研究机构：华为、加拿大滑铁卢大学

作者：Hossam Amer、Maryam Dialameh、Hossein Rajabzadeh 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.01332)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.01332)

> 大语言模型训练面临算力与精度的刚性约束，传统范式将全部预算投入训练阶段，忽视了推理阶段通过多次采样提升精度的潜力。现有早停方法仅监控验证集准确率，无法感知测试时计算（Test-Time Compute, TTC）带来的精度增益，导致在固定总预算下无法实现最优的精度-成本帕累托前沿。本文提出TTC感知训练框架，通过拟合学习曲线预测最终精度，并联合优化早停时机与推理采样次数 $K$，在保持或提升精度的同时大幅削减训练FLOPs。该范式打破了“训练必须完整”的隐含假设，但在高推理成本场景下的盈亏平衡点仍需更严格的实证验证。

】

---

【Half-S: Halving the Scale for Near-Lossless 4-Bit LLM Training ｜半缩放策略

研究机构：香港中文大学、北京航空航天大学

作者：Jinyang Du、Ruihao Gong、Linghan Ai 等 12 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_81cd504c19f0)

> 4-bit大语言模型训练因动态范围极窄而面临数值稳定性挑战，现有基于块最大值的缩放策略在重尾分布下导致低幅值区域量化网格利用率低下。本文指出该失效源于表示坍缩，即大量不同输入映射至相同的低幅值层级。通过推导重尾分布下的MSE最优裁剪阈值，提出将缩放因子减半的Half-S策略以逼近理论最优。该策略以极低的计算开销实现了接近BF16的收敛质量，但其有效性边界在长周期训练与复杂架构下的泛化性尚存疑。

】

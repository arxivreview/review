# ICLR2026 · 去中心化与本地SGD优化方向论文汇编

> 本方向共 3 篇（ICLR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【DECENTRALIZED NONCONVEX OPTIMIZATION UNDER - HEAVY-TAILED NOISE: NORMALIZATION AND OPTI MAL CONVERGENCE ｜去中心化非凸优化中的重尾噪声鲁棒性

研究机构：美国卡内基梅隆大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_66815200)

> 去中心化训练在数据异质性与硬件受限场景下，常面临梯度噪声方差无界的挑战，导致传统算法收敛失效或训练崩溃。现有去中心化鲁棒方法多局限于强凸假设或对称噪声，无法处理现代深度学习中的非凸、非对称重尾噪声。本文提出 GT-NSGDm，通过归一化、动量方差缩减与梯度追踪的组合，首次实现了去中心化非凸重尾噪声下的最优迭代复杂度。该工作填补了理论空白，但实验仅覆盖小规模语言模型，未验证其在大规模视觉任务或极端拓扑下的泛化能力。

】

---

【MT-DAO: Multi-Timescale Distributed Adaptive Optimizers with Local Updates ｜多时间尺度分布式自适应优化器

研究机构：Momenta、英国剑桥大学

作者：Alex Iacob、Andrej Jovanovic、Mher Safaryan 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.05361)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.05361)

> 分布式数据并行（DDP）中，低频同步策略虽能降低通信开销，但自适应优化器因动量衰减过快导致性能显著落后于全同步训练。现有方法未能解决优化器记忆时间与通信间隔的失配问题，本文提出多时间尺度动量机制以维持跨轮次的轨迹稳定性。MT-DAO 通过引入慢动量保留全局方向信息，在 720M 参数模型上闭合了与 DDP 的性能差距。该方法在理论收敛性与工程效率间取得了平衡，但其结论局限于同步低频场景，对异步异构环境的适用性仍存疑。

】

---

【Ringleader ASGD: The First Asynchronous SGD with Optimal Time Complexity under Data Heterogeneity ｜异步随机梯度下降的时间复杂度最优性

研究机构：沙特阿拉伯阿卜杜拉国王科技大学

作者：Artavazd Maranjyan、Peter Richtárik

论文原文见 [arXiv](https://arxiv.org/abs/2509.22860)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.22860)

> 分布式训练在异构硬件与异质数据下，同步方法因等待慢节点导致资源闲置，而现有异步方法要么依赖不切实际的数据相似性假设，要么无法达到理论最优的时间复杂度。本文提出 Ringleader ASGD，通过两阶段聚合与梯度缓冲机制，在不假设数据分布相似的前提下，实现了平滑非凸问题下异步 SGD 的时间复杂度最优。该算法填补了同步最优与同分布异步最优之间的理论空白，但其实验验证仅限于小型 MLP 模型，且在通信延迟非零场景下的实际加速比尚存疑。

】

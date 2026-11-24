# ICLR2026 · 神经形态硬件与SNN加速方向论文汇编

> 本方向共 2 篇（ICLR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Pretraining with Re-parametrized Self-Attention: Unlocking Generalization in SNN-based Neural Decoding Across Time, Brains, and Tasks ｜重参数化自注意力脉冲神经网络

研究机构：浙江大学、西湖大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_52419628)

> 脑机接口（BMI）解码面临跨主体、跨任务与时间漂移导致的泛化失效，现有基于人工神经网络（ANN）的基础模型因算力开销过大无法部署于全植入式设备。本文切入点在于利用脉冲神经网络（SNN）的事件驱动特性，通过重参数化自注意力机制在保持仅累加（AC-only）操作的同时实现跨条件预训练。具体做法是构建包含动态突触与重参数化卷积/全连接层的轻量级SNN架构，并设计分步训练流程。该方案在多个猴子皮层数据集上匹配了SOTA ANN精度且算力显著降低，但其泛化能力是否依赖特定的批归一化切换策略尚存疑。

】

---

【SAFA-SNN: Sparsity-Aware On-Device Few-Shot Class-Incremental Learning with Fast-Adaptive Structure of Spiking Neural Network ｜稀疏感知边缘少样本类增量学习

研究机构：浙江大学、新加坡国立大学

作者：Huijing Zhang、Muyang Cao、Linshan Jiang 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.03648)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.03648)

> 边缘设备在动态环境中需持续学习新类别，但受限于内存与算力，无法部署依赖大规模预训练模型的传统人工神经网络（ANN）少样本类增量学习（Few-Shot Class-Incremental Learning, FSCIL）方案。现有脉冲神经网络（Spiking Neural Network, SNN）研究多聚焦于静态推理或离线训练，缺乏在资源受限设备上应对灾难性遗忘与过拟合的在线增量机制。SAFA-SNN通过稀疏感知动态阈值、零阶优化与原型子空间投影，实现了SNN在通用边缘设备上的端到端FSCIL。该方法在Mini-ImageNet上较最强基线提升4.01%，且实际能耗降低20%，但其对深度网络与不平衡数据流的适应性仍存疑。

】

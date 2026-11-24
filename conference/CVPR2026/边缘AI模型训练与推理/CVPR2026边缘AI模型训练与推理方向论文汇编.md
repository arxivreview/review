# CVPR2026 · 边缘AI模型训练与推理方向论文汇编

> 本方向共 2 篇（CVPR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【AdaBet: Gradient-free Layer Selection for Efficient Training of Deep Neural Networks ｜基于贝蒂数的无梯度层选择

研究机构：美国麻省理工学院、诺基亚贝尔实验室

作者：Irene Tenison、Soumyajit Chatterjee、Fahim Kawsar 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.03101)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.03101)

> 端侧模型适配面临反向传播内存开销远超设备容量的物理瓶颈，现有稀疏微调方法依赖梯度计算或服务器端元训练，无法在隐私受限且资源极端的场景下独立运行。本文切入点在于利用激活空间的拓扑特征替代梯度信号，实现无标签、无反向传播的层重要性评估。具体做法是通过计算每层激活输出的第一贝蒂数（First Betti Number）并归一化，筛选出高学习容量且计算成本可控的层进行局部重训练。该方法在16组模型-数据集组合上平均提升2.5%精度并降低40%峰值内存，但其拓扑计算在深层网络中的时间复杂度是否抵消省下的反向传播开销，以及细粒度任务下的有效性，仍存疑。

】

---

【Critical Patch-Aware Sparse Prompting with Decoupled Training for Continual Learning on the Edge ｜关键补丁感知稀疏提示与解耦训练的端侧持续学习

作者：Wonseon Lim、Jaesung Lee、Dae-Won Kim

论文原文见 [arXiv](https://arxiv.org/abs/2604.07399)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.07399)

> 端侧持续学习面临反向传播激活值存储超出设备内存的刚性约束，导致全量微调不可行。现有提示基持续学习（Prompt-based Continual Learning, PCL）方法虽通过冻结骨干降低参数规模，但忽略训练时的内存峰值与计算开销，致使高精度模型无法在资源受限硬件上稳定运行。本文提出CPS-Prompt，通过任务感知的关键补丁采样与提示-分类器解耦训练，在保持精度的同时显著削减训练内存与时间。该框架在Jetson Orin Nano上实现了1.6倍的效率提升，但其在高稀疏率下的泛化边界及动态资源适配能力仍存疑。

】

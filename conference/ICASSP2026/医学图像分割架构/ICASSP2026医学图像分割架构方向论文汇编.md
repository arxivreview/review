# ICASSP2026 · 医学图像分割架构方向论文汇编

> 本方向共 1 篇（ICASSP2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【DSVM-UNet : Enhancing VM-UNet with Dual Self-distillation for Medical Image Segmentation ｜双自蒸馏增强视觉Mamba网络

作者：Renrong Shao、Dongyang Li、Dong Xia 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.19690)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.19690)

> 医学图像分割需平衡全局语义理解与局部边界精度，但现有视觉Mamba（Vision Mamba）架构在多层特征间存在语义鸿沟，导致浅层细节与深层语义难以协同。DSVM-UNet 指出，单纯优化架构模块（如替换注意力机制）无法解决特征层面的对齐问题，其切入点是在不改变网络拓扑的前提下，通过特征蒸馏强制多层表示在空间与通道维度的一致性。该方法设计了投影与渐进式两种自蒸馏机制，将高层语义知识迁移至低层特征。该方案在皮肤病变分割上取得了超越现有视觉Mamba变体的性能，但在多器官分割任务上显著落后于最新混合架构，其通用性存疑。

】

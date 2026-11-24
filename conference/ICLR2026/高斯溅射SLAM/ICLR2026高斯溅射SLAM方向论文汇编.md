# ICLR2026 · 高斯溅射SLAM方向论文汇编

> 本方向共 2 篇（ICLR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【FLASH-MONO: FEED-FORWARD ACCELERATED GAUSSIAN SPLATTING MONOCULAR SLAM ｜前馈加速的单目高斯泼溅SLAM

研究机构：复旦大学、上海科技大学

作者：Zicheng Zhang、Ke Wu、Xiangting Meng 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_15286983)

> 单目高斯泼溅SLAM（GS-SLAM）长期受困于“从零训练”范式导致的实时性缺失与单帧几何先验引发的多视角尺度不一致。现有优化式方法每帧需数百次迭代，速度仅约1 FPS；而离线前馈方法无法处理流式输入。Flash-Mono通过循环前馈模型直接预测位姿与2D高斯面元属性，将优化迭代压缩至20次，实现了10倍加速与全局一致性。该工作验证了前馈范式在SLAM中的可行性，但其隐藏状态回环机制在长序列下的泛化边界尚存疑。

】

---

【OPEN-SET SEMANTIC GAUSSIAN SPLATTING SLAM WITH EXPANDABLE REPRESENTATION ｜开放集语义高斯泼溅SLAM

研究机构：浙江大学

作者：Yan、Chen Liang、Wenguan Wang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_36855934)

> 开放集语义SLAM旨在让手持设备在实时重建3D场景的同时，赋予场景可动态扩展的开放词汇语义理解能力。现有方法要么将高维语义特征直接绑定每个高斯导致显存溢出，要么仅在2D渲染层赋予语义而缺乏3D空间一致性，且均无法适应SLAM过程中不断涌现的新概念。本文通过引入可扩张语义特征池与低维索引向量解耦语义存储与高斯表示，并辅以跨视角一致性优化，实现了内存可控且语义连贯的在线开放集重建。该方法在Replica数据集上显著提升了渲染与语义精度，但其对RGB-D输入的依赖及缺乏与最新开放集SOTA的同协议对比，限制了其通用性评估。

】

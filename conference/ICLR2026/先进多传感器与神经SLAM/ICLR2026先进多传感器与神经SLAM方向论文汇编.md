# ICLR2026 · 先进多传感器与神经SLAM方向论文汇编

> 本方向共 1 篇（ICLR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【GRL-SNAM: GEOMETRIC REINFORCEMENT LEARN - ING WITH DIFFERENTIAL HAMILTONIANS FOR NAVI GATION AND MAPPING IN UNKNOWN ENVIRONMENTS ｜几何强化学习同步导航与建图

研究机构：美国德克萨斯大学奥斯汀分校

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_26045593)

> 同步导航与建图（SNAM）要求智能体在未知环境中边探索边定位，传统方法往往陷入“先建图后导航”或“纯反应式避障”的二元对立，导致探索预算浪费或路径质量低下。现有强化学习（RL）策略缺乏几何结构约束，在分布偏移下鲁棒性差，且难以处理变形体的非线性动力学。GRL-SNAM 提出基于哈密顿量结构的导航框架，将导航与建图解耦为局部能量景观的优化问题，通过离线学习参考哈密顿量与在线阶段式能量修正，实现最小化探索下的高质量导航。该方法在2D变形体导航任务中展现出优于标准深度RL基线的样本效率与路径平滑度，但其结论局限于2D仿真环境，向3D非完整约束系统的迁移能力尚存疑。

】

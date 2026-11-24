# ACL-Findings2026 · 面向3D分子设计的深度生成模型方向论文汇编

> 本方向共 1 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【CAGenMol: Condition-Aware Diffusion Language Model for Goal-Directed Molecular Generation ｜条件感知离散扩散语言模型用于目标导向分子生成

研究机构：香港科技大学

作者：Yanting Li、Zhuoyang Jiang、Enyan Dai 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.11483)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.11483)

> 目标导向分子生成需在满足蛋白结合亲和力与多重药物属性（如ADMET）的同时保持化学有效性，现有方法往往在结构精度与优化灵活性间妥协。自回归模型因左到右生成机制缺乏全局视野，难以应对非可微奖励信号；纯3D生成模型则计算昂贵且忽略非几何属性。CAGenMol将分子生成建模为条件离散扩散问题，通过统一约束适配器（UCA）融合异构生物信号，并引入步级近端策略优化（Step-PPO）实现精细信用分配。该框架在CrossDocked2020基准上取得了69.7%的成功率，但其依赖1D序列表示，未直接验证3D几何约束下的性能上限。

】

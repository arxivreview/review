# CVPR2026 · 神经PDE求解器与物理信息学习方向论文汇编

> 本方向共 2 篇（CVPR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Learning to Solve PDEs on Neural Shape Representations ｜神经形状表示下的表面偏微分方程求解

研究机构：英国伦敦大学学院、Adobe研究院

作者：Lilian Welschinger、Yilin Liu、Zican Wang 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.21311)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.21311)

> 表面偏微分方程（PDE）求解长期依赖多边形网格离散化，而现代三维资产日益采用神经隐式表示，导致求解器与数据域不匹配。现有方法或强制提取网格破坏端到端可微性，或依赖逐实例训练导致泛化失效。本文提出一种几何条件局部算子，在窄带内直接学习法向恒定性扩展，实现神经域内的网格到网格更新。该方法在解析基准上精度略优于最近点法（CPM），但显著低于有限元法（FEM），其单形状训练的泛化边界尚需更严苛的几何复杂度测试验证。

】

---

【MSPT: Efficient Large-Scale Physical Modeling via Parallelized Multi-Scale Attention ｜多尺度补丁Transformer

研究机构：荷兰阿姆斯特丹大学

作者：Pedro M. P. Curvo、Jan-Willem van de Meent、Maksim Zhdanov

论文原文见 [arXiv](https://arxiv.org/abs/2512.01738)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.01738)

> 工业级计算流体力学（CFD）仿真涉及百万级网格点，传统神经求解器在处理此类大规模非结构化几何时，面临局部细节保留与全局依赖捕获的双重计算瓶颈。现有Transformer架构要么依赖固定全局切片导致信息平滑，要么采用纯局部注意力牺牲长程交互，难以在单一模型中兼顾精度与扩展性。MSPT通过球树分区结合并行多尺度注意力机制，在局部补丁内执行自注意力，同时利用池化超节点进行全局信息交换，实现了近线性复杂度下的精度提升。该方法在标准PDE基准和工业级气动数据集上验证了有效性，但其精度仍低于专用双分支模型，且缺乏对物理守恒律的显式约束。

】

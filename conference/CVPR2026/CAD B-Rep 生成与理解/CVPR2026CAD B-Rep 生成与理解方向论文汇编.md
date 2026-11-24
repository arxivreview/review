# CVPR2026 · CAD B-Rep 生成与理解方向论文汇编

> 本方向共 10 篇（CVPR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【AutoRegressive Generation with B-rep Holistic Token Sequence Representation ｜边界表示整体式令牌序列自回归生成

研究机构：西北工业大学、新加坡国立大学

作者：Jiahao Li、Yunpeng Bai、Yongkang Dai 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.16771)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.16771)

> B-Rep 生成长期受困于几何与拓扑的解耦建模，导致序列误差累积与表示碎片化。现有方法或采用多阶段流水线，或依赖图结构，均难以直接适配 Transformer 的序列处理范式。BrepARG 提出整体式令牌序列表示，将 B-Rep 的几何与拓扑编码为单一令牌流，通过自回归模型联合学习其分布。该框架在有效性指标上显著超越基线，但其固定量化步长对复杂曲面的拟合能力存疑。

】

---

【BrepGaussian: CAD reconstruction from Multi-View Images with Gaussian Splatting ｜基于二维高斯泼溅的多视图图像CAD逆向工程

研究机构：南京大学

作者：Jiaxing Yu、Dongyang Ren、Hangyu Xu 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.21105)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.21105)

> CAD逆向工程旨在从非结构化数据中恢复参数化边界表示（B-Rep），以支持后续仿真与制造。传统方法依赖高质量点云输入，但点云获取成本高且标注繁琐，而图像数据虽易获取却难以直接映射至精确的几何拓扑结构。BrepGaussian 利用二维高斯泼溅（2DGS）从多视图图像中提取带边缘与面片特征的点云，并通过约束引导拟合生成水密B-Rep模型。该框架实现了无点云监督下的端到端重建，但在复杂曲面处理与掩码自动化方面仍存在显著局限。

】

---

【BrepVGAE: Variational Graph Autoencoder with Unified Latent Representation for B-rep ｜B-Rep 统一潜在表示与集合并行解码

研究机构：西北工业大学、新加坡国立大学

作者：Hao Guo、Liyuan Deng、Yongkang Dai 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_7a56a7357a83)

> 计算机辅助设计（CAD）中的边界表示（B-Rep）生成长期受制于几何与拓扑的强耦合及序列误差累积，导致模型难以同时保证形状精度与结构有效性。现有自回归或扩散方法在处理复杂拓扑时往往陷入多阶段生成的误差传播困境，而本文切入点在于将 B-Rep 视为稀疏同构图，通过变分图自编码器（VGAE）学习统一潜在表示。具体做法是设计多槽位可学习查询机制与对称双线性层，从单一全局潜在向量并行解码所有节点特征与邻接矩阵。该方法在几何重建精度上显著优于基线，但在复杂曲面处理与最新 SOTA 对比上存在局限，其并行解码范式对大规模复杂装配体的扩展性仍存疑。

】

---

【CAD-Refiner: A Unified Framework for CAD Generation and Iterative Editing ｜CAD-Refiner：统一生成与编辑的多模态框架

研究机构：吉林大学

作者：Meng Yuan、Dawei Lin、Hongxia Xie 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c8075218dd03)

> 导读 计算机辅助设计（CAD）的自动化建模长期面临生成与编辑割裂的困境：现有方法要么仅能无条件生成，要么依赖单一模态输入，无法支持设计师在初始模型基础上进行迭代精修。CAD-Refiner 的切入点在于，将多模态输入解析为显式拓扑结构图，并通过动态序列注入策略统一生成、补全与编辑任务。其核心做法是引入 VLM 提取拓扑图作为解码器辅助条件，并设计几何感知的自适应损失权重模块。该框架在编辑任务上显著优于 LLM 基线，但其对 VLM 前端的依赖和 80K 数据规模是否足以支撑工业级泛化，仍存疑。

】

---

【CADFS: A Big CAD Program Dataset and Framework for Computer-Aided Design with Large Language Models ｜基于 FeatureScript 的复杂 CAD 设计历史生成框架

研究机构：沙特阿拉伯阿卜杜拉国王科技大学

作者：Vladislav Pyatov、Gleb Bobrovskikh、Saveliy Galochkin 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.01925)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.01925)

> 现有生成式 CAD 系统受限于简化的 Token 序列表示，仅能生成草图与拉伸两种基础操作，无法表达倒角、放样等复杂工程特征。本文指出这一瓶颈源于表示层对几何实体引用的结构性缺失，而非模型容量不足。通过引入 Onshape 原生 FeatureScript 代码表示并构建 45 万真实模型数据集，该框架实现了 15 种建模操作的端到端生成。其价值在于突破了操作集上限，但 FeatureScript 的专有性限制了跨平台通用性，且缺乏与 B-Rep 直接生成方法的直接对比。

】

---

【CME-CAD: Heterogeneous Collaborative Multi-Expert Reinforcement Learning for CAD Code Generation ｜异构多专家协作强化学习生成CAD代码

研究机构：复旦大学、美国南加州大学

作者：Ke Niu、Haiyang Yu、Zhuofan Chen 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.23333)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.23333)

> 从2D工程图直接生成可执行、可编辑的CAD代码，旨在替代高成本的人工文本标注流程。现有基于单模型强化学习的方法受限于策略内优化，难以突破单一推理路径的认知瓶颈。本文提出CME-CAD范式，通过多专家微调与协作强化学习，利用异构模型的互补性提升代码生成的几何精度与可执行性。该方法在自建工业级数据集上实现了80.71%的IoU，但缺乏与B-Rep直接生成路线的横向对比，其泛化边界尚存疑。

】

---

【FoV-Net: Rotation-Invariant CAD B-rep Learning via Field-of-View Ray Casting ｜基于视场射线投射的旋转不变 CAD B-Rep 学习

研究机构：比利时根特大学

作者：Matteo Ballegeer、Dries F. Benoit

论文原文见 [arXiv](https://arxiv.org/abs/2602.24084)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.24084)

> 现有 B-Rep 学习方法依赖全局坐标编码几何，导致模型在任意旋转下性能崩塌，无法适应工业场景中多源 CAD 模型的姿态不确定性。本文指出这一长期被忽视的旋转敏感缺陷，并提出 FoV-Net，通过局部参考系 UV 网格与视场射线描述子实现旋转不变的特征表达。该方法在分类与分割任务上保持旋转鲁棒性，但牺牲了对齐数据下的部分姿态线索利用能力，其数据效率优势在低监督场景下尤为关键。

】

---

【HiFi-BRep: High-Fidelity Latent Representation for Robust B-Rep Generation ｜高保真潜在表示下的鲁棒边界表示生成

研究机构：浙江大学

作者：Junhao Hou、Chenqi Luo、Pufan Wang 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_291f547886e0)

> 边界表示（B-Rep）生成旨在从数据中合成满足严格流形约束的三维实体模型，但现有方法常因填充噪声污染潜在空间或级联生成导致误差累积，使得生成的模型在拓扑上无效。本文切入点在于将拓扑有效性从后处理修复转化为可微分的训练目标，并通过拓扑引导的注意力机制消除表示噪声。具体做法是构建一个单阶段并行解码器，在统一潜在空间中同时预测几何与拓扑，并引入双峰损失函数强制满足“每边两面”的流形约束。该框架在有效性指标上显著优于基线，但其对复杂自由曲面及非流形结构的泛化能力仍存疑。

】

---

【Pointer-CAD: Unifying B-Rep and Command Sequences via Pointer-based Edges & Faces Selection ｜指针式命令序列

研究机构：北京航空航天大学、上海科技大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a05c47539961)

> 计算机辅助设计（CAD）自动化生成的核心瓶颈在于，传统命令序列无法表达“选择特定几何实体”这一关键操作，导致倒角、圆角等工业常用操作失效，且离散化引入的量化误差破坏了拓扑水密性。Pointer-CAD 通过引入指针机制，让大语言模型（LLM）直接引用边界表示（B-Rep）中的边和面，将连续几何选择转化为离散指针预测，从而在保持序列生成效率的同时支持复杂编辑。该方法在文本到 CAD 生成任务中显著降低了分段误差（SegE）和通量包围误差（FluxEE），但其对模型容量的依赖及单件建模的局限，使其在复杂装配场景下的泛化能力仍存疑。

】

---

【PP-Brep: Few-Shot B-rep Classification with Hybrid Graph Representation ｜PP-Brep：基于混合图表示与强化学习预训练的少样本B-Rep分类

研究机构：西北工业大学

作者：Jiacheng Hao、Chunying Liu、Hao Guo 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ef478dcb8768)

> 导读 工业场景中，CAD零件类别繁多但标注数据极度稀缺，传统监督学习难以快速适配新类别，而现有无监督预训练方法依赖线性探测，仍需大量下游标签，无法实现少样本识别。本文切入点在于将B-Rep结构转化为多层级混合图，并引入强化学习动态控制对比预训练扰动强度，结合结构感知提示微调，在冻结骨干下实现高效少样本分类。其价值在于显著提升了少样本场景下的分类精度与预训练效率，但方法对复杂几何特征（如螺纹）的鲁棒性仍存疑，且未验证跨数据集分布差异对迁移效果的影响。

】

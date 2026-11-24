# CVPR2026 · AI驱动的平面图与布局生成方向论文汇编

> 本方向共 4 篇（CVPR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【CG-Floor: Centroid-Guided Diffusion for Large-Scale Floorplan Generation ｜大规模建筑平面生成中的拓扑-几何解耦框架

研究机构：天津大学、深圳大学

作者：Hongjin Lian、Jian Ma、Hongjie Chen 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_cbfae5a58c6e)

> 大规模建筑平面生成旨在从文本或图约束中合成包含数十个房间、具有复杂连通性和非曼哈顿几何结构的布局，以支持虚拟空间规划与建筑模拟。现有方法在处理小规模场景时表现良好，但在房间数量激增时，矢量方法因顶点组合爆炸而退化为矩形，光栅方法则因缺乏全局位置信息导致边界模糊与语义错位。本文提出CG-Floor，通过引入尺寸感知语义质心热图（SASCH）显式解耦拓扑与几何生成，并结合VQ-VAE离散码本与潜空间扩散模型，在MSD数据集上实现了SOTA性能。该方法在大规模场景下显著提升了拓扑一致性，但其光栅表示在工程级矢量编辑上的兼容性仍存疑。

】

---

【Nestwork: Conditional 3D Furnished House Layout Generation through Latent Heterogeneous Graph Diffusion ｜异构图潜空间扩散生成全屋3D布局

研究机构：美国麻省理工学院、美国佐治亚理工学院

作者：Shuhan Miao、Biru Cao、Junling Zhuang

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d556a9c37083)

> 现有3D室内布局生成方法将房间结构与家具摆放割裂为两个独立阶段，导致误差累积与空间不一致。本文切入点在于将全屋表示为单一异构图，在统一潜空间内联合去噪，消除多阶段流水线。具体做法是构建基于异构图注意力网络的自编码器，并在其潜空间训练一个支持随机掩码条件的扩散模型。该方法在3D-FRONT上实现了高保真与结构一致性，但尚未解决功能可行性的硬约束问题。

】

---

【Tokenization Allows Multimodal Large Language Models to Understand, Generate and Edit Architectural Floor Plans ｜基于离散房间实例令牌的建筑平面图统一理解、生成与编辑框架

研究机构：清华大学

作者：Sizhong Qin、Ramon Elias Weber、Xinzheng Lu

论文原文见 [arXiv](https://arxiv.org/abs/2603.11640)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.11640)

> 建筑平面图设计需要联合推理几何、语义与空间层级，现有扩散模型与语言模型虽提升了视觉保真度，却难以实现连贯的空间推理与可控生成。本文切入点在于将布局离散化为房间实例令牌，弥合符号推理与连续几何之间的鸿沟。通过层级向量量化变分自编码器与多模态大语言模型对齐，HouseMind在单一框架内统一了理解、生成与编辑任务。该框架在几何有效性与可控性上表现优异且支持本地部署，但其对复杂功能约束的硬满足能力仍存疑。

】

---

【Unified Vector Floorplan Generation via Markup Representation ｜统一矢量平面生成：基于标记语言表示的自回归建模

研究机构：日本东京大学

作者：Kaede Shiohara、Toshihiko Yamasaki

论文原文见 [arXiv](https://arxiv.org/abs/2604.04859)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.04859)

> 建筑平面生成长期面临多条件任务泛化性差与表示碎片化的困境，现有光栅或扩散方法需依赖多阶段流水线或特定任务网络，难以统一处理边界、图结构及补全等异构输入。本文提出平面标记语言（Floorplan Markup Language, FML），将平面几何与拓扑约束编码为单一结构化序列，使生成任务转化为标准的下一词预测问题。通过自回归Transformer模型（FMLM）结合语法约束解码，该方法在RPLAN数据集上实现了跨任务的统一矢量生成。尽管在几何精度与拓扑一致性上显著优于经典基线，但其对非标准拓扑的探索能力及多楼层扩展性仍受限于当前语法设计。

】

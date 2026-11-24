# CVPR2026 · 三维点云Transformer与鲁棒学习方向论文汇编

> 本方向共 11 篇（CVPR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Adapting Point Cloud Analysis via Multimodal Bayesian Distribution Learning ｜多模态贝叶斯分布学习驱动的测试时点云适应

研究机构：中国科学技术大学、东南大学

作者：Xingyu Zhu、Liang Yi、Shuo Wang 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.22070)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.22070)

> 大模型在3D点云识别中面临训练与测试分布不一致导致的性能衰减，传统缓存式测试时适应（TTA）因固定容量导致信息丢失且融合机制缺乏理论支撑。本文提出BayesMM，将几何与文本模态建模为动态高斯分布，通过贝叶斯模型平均自动加权融合，实现无训练参数的在线适应。该方法在多个基准上显著优于缓存基线，但其高斯假设在复杂点云非高斯分布下的适用性存疑。

】

---

【BuildAnyPoint: 3D Building Structured Abstraction from Diverse Point Clouds ｜建筑点云结构化重建：基于层级潜扩散与自回归生成的解耦框架

作者：Tongyan Hua、Haoran Gong、Yuan Liu 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.23645)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.23645)

> 城市点云重建旨在从无序、稀疏的观测数据中恢复出具有拓扑一致性的建筑网格，但现有方法要么依赖固定建筑语法导致几何表达受限，要么因单步自回归产生几何歧义。BuildAnyPoint 通过引入显式 3D 生成先验，将重建任务解耦为“分布恢复”与“网格生成”两个阶段，利用层级潜扩散模型从异构点云中恢复密集均匀的点云分布，再驱动自回归 Transformer 生成高质量网格。该方法在建筑点云补全基准上实现了完整性与均匀性的显著突破，但其性能高度依赖配对监督数据，在缺乏大规模真实观测的场景下泛化能力尚存疑。

】

---

【CLIPoint3D: Language-Grounded Few-Shot Unsupervised 3D Point Cloud Domain Adaptation ｜CLIPoint3D：基于语言锚定的少样本无监督3D点云域适应

研究机构：印度理工学院孟买分校

作者：Mainak Singha、Sarthak Mehrotra、Paolo Casari 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.20409)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.20409)

> 3D点云域适应旨在解决合成数据与真实传感器数据间的分布偏移问题，传统方法依赖重型3D编码器且缺乏语义先验，导致计算成本高且泛化能力弱。本文切入点在于利用CLIP的跨模态语义先验，通过冻结骨干网络并引入轻量级适配机制，在少样本无监督条件下弥合2D-3D模态差距与源-目标域差距。具体做法是结合知识驱动提示调优、参数高效微调及熵引导视图选择，实现高效跨域迁移。该方法在效率与精度间取得了显著平衡，但其依赖多视角投影的机制在复杂遮挡场景下的几何保真度仍存疑。

】

---

【Deformation-based In-Context Learning for Point Cloud Understanding ｜基于变形的点云上下文学习

研究机构：美国普林斯顿高等研究院、四川大学

作者：Chengxing Lin、Jinhong Deng、Yinjie Lei 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.02845)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.02845)

> 3D点云上下文学习（In-Context Learning, ICL）旨在通过少量示例实现多任务泛化，但现有掩码点建模（Masked Point Modeling, MPM）方法因缺乏几何先验导致重建失真，且训练与推理目标存在根本性错位。DeformPIC 将 ICL 重构为几何变形过程，通过解耦任务提取与变形转移，显式建模查询点云向目标形状的映射。该方法在 ShapeNet In-Context 基准上显著降低了 Chamfer Distance，但在跨域泛化中仍受限于变形场的局部性假设。其价值在于确立了点云 ICL 的几何一致性范式，但变形机制对非刚性大位移任务的适用性尚存疑。

】

---

【FILTR: Extracting Topological Features from Pretrained 3D Models ｜拓扑感知预训练编码器评估与前馈预测

作者：Louis Martinez、Maks Ovsjanikov

论文原文见 [arXiv](https://arxiv.org/abs/2604.22334)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.22334)

> 现有3D点云预训练编码器在语义与几何任务上表现优异，但其特征是否隐含全局拓扑信息尚属未知。传统拓扑数据分析（TDA）依赖经典算法，计算昂贵且无法与端到端学习架构兼容，导致拓扑信息难以直接融入现代感知流水线。本文通过引入DONUT基准量化编码器拓扑表征能力，并提出FILTR框架，利用冻结编码器特征以前馈方式直接预测持久图。该工作揭示了当前主流编码器在全局拓扑理解上的显著缺陷，同时证明了基于预训练特征提取拓扑描述符的可行性，但其跨域泛化能力仍受限于预训练分布。

】

---

【Good Can Sometimes be Bad: A Unified Attack against 3D Point Cloud Classifier by a Flexible Isotropic Resampling ｜统一3D点云后门与对抗攻击：基于灵活各向同性重采样

研究机构：武汉大学

作者：Linkun Fan、Jiahao Zhang、Juntao Zhang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0fcf1037d8e7)

> 3D点云模型在动态部署环境下面临攻击权限不确定的困境，传统后门与对抗攻击因依赖特定权限而失效。现有防御与攻击研究均将“隐蔽性”等同于限制扰动幅度，导致攻击强度受限且点云质量下降。本文提出UAtt3D，通过灵活各向同性重采样（FIR）提升点云质量来掩盖恶意扰动，实现后门与对抗攻击的统一。该方法在隐蔽性上显著优于基线，但攻击成功率略低于最强基线，其“质量提升即隐蔽”的假设在极端几何变形下是否依然成立尚存疑。

】

---

【Learning Coordinate-based Convolutional Kernels for Continuous SE(3) Equivariant and Efficient Point Cloud Analysis ｜连续SE(3)等变坐标核卷积

研究机构：韩国首尔大学、英国帝国理工学院

作者：Jaein Kim、Hee Bin Yoo、Dong-Sig Han 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.17538)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.17538)

> 3D点云模型常依赖输入对齐至标准姿态的先验，导致真实场景下的鲁棒性不足。现有群卷积方法在严格连续对称性与大规模部署效率间存在不可调和的矛盾，本文切入点在于利用双余集空间参数化连续SE(3)对称性，并采用显式核设计降低计算开销。具体做法是通过坐标网络将归一化局部邻域映射为双余集参数，进而生成等变线性映射。该方法在姿态注册任务上实现了零角度误差，但在大规模语义分割上性能显著落后于非等变SOTA，其全局语义建模能力存疑。

】

---

【LitePT: Lighter Yet Stronger Point Transformer ｜层级解耦的轻量点云Transformer

研究机构：瑞士苏黎世联邦理工学院、英国牛津大学

作者：Yuanwen Yue、Damien Robert、Jianyuan Wang 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.13689)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.13689)

> 3D点云Transformer在追求全局语义建模时，往往因全层级部署注意力机制而陷入计算冗余与参数膨胀的困境。现有主流架构如Point Transformer V3（PTv3）虽性能领先，但其67%的参数被稀疏卷积占据，且早期高分辨率阶段的注意力计算成本极高却收益甚微。本文通过实证分析揭示卷积与注意力在特征层级中的分工差异，提出早期层保留卷积、深层切换至注意力的LitePT架构，并引入无参数位置编码PointROPE。该设计在保持甚至超越PTv3精度的同时，大幅降低了参数量、内存占用与推理延迟，但其对动态点云及极端稀疏场景的适用性仍存疑。

】

---

【Low-Rank Test-Time Training for Pre-Trained Point Cloud Models ｜低秩测试时训练增强点云模型鲁棒性

研究机构：浙江大学、华中科技大学

作者：Ouyangzi Ye、Feifei Shao、Kexin Li 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2668dcb37891)

> 预训练点云模型在传感器噪声、遮挡等分布外（OOD）场景下性能骤降，而现有测试时训练（TTT）方法依赖重型解码器且更新参数过多，导致适应效率低且易遗忘预训练知识。LoTT-PC 通过引入低秩调制单元与无解码器的掩码特征对齐机制，实现了轻量级、强耦合的在线适应。该方法在多个腐蚀基准上平均超越现有 SOTA 2.7%，但其单步适应策略与固定掩码比率的设定在复杂动态场景下的泛化能力仍存疑。

】

---

【Mamba Learns in Context: Structure-Aware Domain Generalization for Multi-Task Point Cloud Understanding ｜结构感知域泛化

研究机构：吉林大学、澳大利亚西澳大学

作者：Jincen Jiang、Qianyu Zhou、Yuhang Li 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.20739)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.20739)

> 多任务点云域泛化（Domain Generalization, DG）旨在让单一模型在未见过的传感器域与几何任务间保持性能，但现有Transformer架构因二次方复杂度与无序性难以兼顾效率与结构一致性，而Mamba虽具线性复杂度却依赖坐标序列化，在视角偏移与缺失区域下易导致结构漂移。本文提出SADG，通过质心距离谱与测地曲率谱构建变换不变的序列化序列，结合层次域感知建模与测试时谱图对齐，在重建、去噪与配准任务上实现了跨域结构保持。该框架在效率与泛化性上优于基线，但其对极端缺失场景下的拓扑稳定性及语义级泛化能力的验证仍显不足。

】

---

【PointTPA: Dynamic Network Parameter Adaptation for 3D Scene Understanding ｜场景级点云动态参数适配

研究机构：华中科技大学

作者：Siyuan Liu、Chaoqun Zheng、Xin Zhou 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.04933)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.04933)

> 场景级点云理解面临几何多样性、类别不平衡与空间布局多变三重挑战，导致预训练模型在微调时难以充分迁移知识。现有参数高效微调（PEFT）方法在推理阶段保持参数静态，无法适应场景级数据的动态几何变化。PointTPA通过序列化邻域分组与动态参数投影器，在推理时生成输入感知的局部投影权重，以1.09%的可训练参数实现接近全量微调的性能。该框架验证了推理时参数动态性对复杂场景理解的必要性，但其动态机制在低复杂度场景下的边际收益及跨域稳定性仍存疑。

】

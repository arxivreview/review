# Others2026 · 三维视觉与3D与4D重建方向论文汇编

> 本方向共 24 篇（Others2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【A 129FPS Full HD Real-Time Accelerator for 3D Gaussian Splatting ｜面向边缘设备的3D高斯溅射硬件加速器与协同压缩

研究机构：国立阳明交通大学

作者：Fang-Chi Chang、Tian-Sheuan Chang

论文原文见 [arXiv](https://arxiv.org/abs/2604.10223)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.10223)

> 3D高斯溅射（3D Gaussian Splatting, 3DGS）在AR/VR设备上的部署受限于GB级存储与高功耗，现有软件压缩方法无法直接映射至低功耗硬件，而既有硬件加速器因实现原始算法导致面积与能耗超标。本文切入点在于将压缩策略与硬件流水线进行协同设计，通过固定压缩比消除数据变异性，并优化渲染数据流。具体做法是改造LightGaussian管线实现51.6倍压缩，并设计混合粒度帧级流水线加速器。该工作验证了亚瓦特功耗下全高清实时渲染的可行性，但其压缩质量显著低于当前算法SOTA，且缺乏硅片实测数据。

】

---

【Bridging the Dimensionality Gap: A Taxonomy and Survey of 2D Vision Model Adaptation for 3D Analysis ｜维度鸿沟：2D视觉模型向3D分析适配的分类学综述

作者：Akshat Pandya、Bhavuk Jain

论文原文见 [arXiv](https://arxiv.org/abs/2604.03334)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.03334)

> 2D视觉模型在3D分析中的迁移面临结构不匹配的核心障碍，即规则网格与无序点云之间的“维度鸿沟”。现有综述多按数据表示或任务划分，缺乏对适配策略本身的统一视角，导致无法系统比较不同路线在几何保真与计算效率间的权衡。本文提出数据中心、架构中心与混合三类适配策略的分类框架，将分散的方法纳入统一坐标系进行定性分析。该框架为理解2D-3D迁移提供了结构化视角，但其定性分析缺乏定量验证，且未涵盖2024年后前馈式3D基础模型的新范式。

】

---

【Combi-CAM: A Novel Multi-Layer Approach for Explainable Image Geolocalization ｜多层梯度激活聚合的可解释性方法

研究机构：法国巴黎高等师范学院、法国国家科学研究中心

作者：David Faget、José Luis Lisani、Miguel Colom

论文原文见 [arXiv](https://arxiv.org/abs/2603.24117)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.24117)

> 单图地理定位模型依赖细粒度视觉线索，但标准解释工具仅关注网络末端，导致关键判别区域定位模糊。现有方法无法区分中间层与末端层对决策的贡献差异，本文切入点在于聚合多层激活图以保留局部细节。通过跨层ReLU加权求和生成统一热力图，Combi-CAM在定性案例中实现了比单层方法更精确的地标定位。该方法提供了诊断视觉歧义失效的视角，但缺乏定量指标支撑，且局限于CNN架构。

】

---

【DreamLifting: A Plug-in Module Lifting MV Diffusion Models for 3D Asset Generation ｜轻量级高斯资产适配器

研究机构：南开大学、南京大学

作者：Ze-Xin Yin、Jiaxiong Qiu、Liu Liu 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.07435)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.07435)

> 导读 现代图形管线依赖具备物理基于渲染（PBR）材质的3D资产，但传统建模耗时且现有生成方法多仅输出顶点色，无法支持重光照。本文提出LGAA，通过复用预训练多视图扩散模型的特征，直接生成带PBR通道的高斯资产，规避了对大规模3D数据的依赖。该方法以69k实例实现数据高效微调，在PBR质量上优于联合生成基线，但其几何保真度是否足以支撑复杂拓扑场景仍存疑。

】

---

【Long-LRM++: Preserving Fine Details in Feed-Forward Wide-Coverage Reconstruction ｜半显式特征高斯前馈重建

研究机构：Adobe研究院、美国俄勒冈州立大学

作者：Chen Ziwen、Hao Tan、Peng Wang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.10267)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.10267)

> 前馈式新视角合成旨在摆脱逐场景优化，实现即时重建，但现有显式高斯方法因需预测海量颜色基元导致高频细节模糊，而隐式方法虽质量高却牺牲了实时渲染速度。Long-LRM++ 指出颜色光栅化的误差敏感性是核心瓶颈，提出以自由分布的特征高斯替代像素对齐颜色高斯，并通过轻量级解码器与多空间分区机制恢复细节。该方法在保持 14 FPS 实时渲染的同时，将重建质量提升至接近隐式方法水平，但其在复杂几何结构下的泛化边界尚待进一步验证。

】

---

【Manual2Skill++: Connector-Aware General Robotic Assembly from Instruction Manuals via Vision-Language Models ｜连接件感知的机器人装配框架

研究机构：新加坡国立大学、加拿大多伦多大学

作者：Chenrui Tie、Shengxiang Sun、Yudi Lin 等 12 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.16344)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.16344)

> 机器人装配的核心矛盾在于：现有方法将连接件视为次要约束，导致在复杂家具或工业制造场景中，因连接类型识别错误而执行失败。本文切入点是将连接件（Connector）提升为与部件同等重要的显式实体，通过视觉语言模型（VLM）从说明书中提取层级图结构，直接计算位姿。其价值在于实现了毫米级对齐精度，但存疑于对说明书清晰度的强依赖及缺乏跨基准泛化验证。

】

---

【代尔夫特理工团队新研究：雷达点云静态动态分割与自车运动联合估计

研究机构：荷兰代尔夫特理工大学

作者：Simin Zhu、Satish Ravindran、Alexander Yarovoy 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.20003)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.20003)

> 4D毫米波雷达感知面临的核心矛盾在于点云极度稀疏且噪声大，导致直接套用LiDAR检测架构时特征提取困难，且传统分割任务往往依赖外部里程计或点云聚合来补偿自车运动，牺牲了传感器独立性与实时性。本文切入点在于重新定义雷达分割目标，不再追求精细的语义类别标签，而是聚焦于感知链前端的静态/动态物体解耦与自车运动估计。通过轻量级MLP与RNN架构直接处理未聚合的原始点云，利用静态物体的径向速度反演自车运动，实现了单一雷达传感器下的双任务闭环。该方法在RadarScenes数据集上验证了原始点云包含足够信息以同时完成分割与运动估计，但其性能边界局限于2D平面任务，未验证对下游3D检测精度的增益。

】

---

【双八叉树图潜空间扩散用于语义场景生成与补全

作者：Xujia Zhang、Brendan Crowe、Christoffer Heckman

论文原文见 [arXiv](https://arxiv.org/abs/2509.16483)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.16483)

> 3D语义场景的生成、扩展与补全在机器人导航中常被视为独立任务，且现有方法多局限于单一域（室内或室外）或依赖密集张量表示，导致跨域泛化差且计算开销大。本文切入点在于利用稀疏层级结构解耦几何与语义，通过双八叉树图潜空间扩散统一处理多域场景。其核心是构建基于双八叉树图的潜变量自编码器，并采用两阶段扩散分别预测结构分割信号与语义嵌入，结合后条件混合实现训练无关的补全。该方法在分布距离指标上显著优于基线，但缺乏与最新LLM驱动布局方法的直接对比，且室内语义IoU较低，暴露了稀疏表示在细粒度对齐上的局限。

】

---

【国立卫生团队新研究：跨分布扩散先验驱动的稀疏视图CT重建

研究机构：美国国立卫生研究院、中山大学

作者：Haodong Li、Shuo Han、Haiyang Mao 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.13576)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.13576)

> 稀疏视图CT重建旨在通过减少投影视图降低辐射剂量，但现有扩散模型在跨扫描仪、跨协议的分布外（OOD）场景下性能显著衰减。本文指出，传统扩散先验将解剖结构与扫描仪特定伪影耦合，导致泛化失效，其切入点是通过分类器自由引导（CFG）显式解耦域不变与域特定特征。具体做法是训练一个基于SiT骨干的扩散模型，在推理时结合ASD-POCS迭代校正以平衡生成质量与物理一致性。该方法在OOD场景下展现出鲁棒性，但其1000步采样策略与临床实时性需求存在张力，且ID性能未达领域SOTA水平。

】

---

【埃尔朗根-纽伦堡团队新研究：局部神经隐式乳腺形状建模

研究机构：德国埃尔朗根-纽伦堡大学

作者：Maximilian Weiherer、Antonia von Riedheim、Vanessa Brébant 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.13540)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.13540)

> 3D参数化乳腺建模长期受限于公开数据缺失与全局隐式表示的高频细节丢失，导致临床可用的低成本重建方案匮乏。本文切入点在于借鉴头部建模的局部化思想，将单一全局SDF分解为锚定于解剖标志点的多个局部MLP，以恢复乳头、皮肤褶皱等细微结构。通过结合运动恢复结构（SfM）获取点云并拟合该局部隐式模型，实现了仅依赖单目RGB视频的低成本度量重建。该方法在特定数据集上显著优于前代全局模型，但其泛化能力与临床鲁棒性仍受限于小样本训练集与缺乏自动解剖点检测的现状。

】

---

【基于数字孪生的路边LiDAR合成数据集构建

作者：Muhammad Shahbaz、Shaurya Agarwal

论文原文见 [arXiv](https://arxiv.org/abs/2509.06781)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.06781)

> 路边LiDAR感知依赖高质量标注数据，但真实数据采集成本高昂且场景覆盖有限。现有通用模拟器生成的数据存在显著域差距，导致模型在真实部署时性能大幅衰减。本文通过构建特定真实场景的高保真数字孪生，从源头消除几何与传感器偏差，而非事后适配。实验表明，仅用合成数据训练的模型在真实测试集上性能持平甚至超越真实数据训练模型，但其泛化能力受限于已建模场景的静态几何精度。

】

---

【密歇根团队新研究：几何感知GNC-PnP的无学习6D姿态估计

研究机构：美国密歇根大学

作者：Xiujin Liu

论文原文见 [arXiv](https://arxiv.org/abs/2512.06565)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.06565)

> 6D姿态估计旨在从单目图像恢复物体旋转与平移，是机器人抓取的基础感知任务。现有深度学习路线虽精度高，但依赖大量标注数据与GPU资源，难以在缺乏训练条件的工业场景直接部署；传统几何管线虽无需学习，却因特征匹配中的离群点与对称歧义导致优化不稳定。GNC-Pose通过引入基于CAD模型体素化聚类的几何感知权重，结合渐进非凸性（GNC）优化策略，在纯CPU环境下实现了与深度学习相当的精度。该方法验证了鲁棒几何优化在无学习场景下的有效性，但其对纹理丰富物体的依赖限制了在极端无纹理场景的适用性。

】

---

【庆应义塾团队新研究：基于图注意力与显式统计特征的毫米波雷达点云处理

研究机构：日本庆应义塾大学

作者：Abdullah Al Masud、Shi Xintong、Mondher Bouazizi 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.08540)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.08540)

> 毫米波雷达人体姿态估计（HPE）与活动识别（HAR）面临点云噪声大、空间关系易被图像化表示扭曲的困境。现有CNN或Transformer方法依赖隐式学习内部结构，导致对噪声敏感且收敛困难。本文通过引入Statbox模块显式提取节点、边及帧级统计特征，并结合图注意力网络（GAT）建模点间关系，在四个雷达数据集上实现了HPE误差显著降低与HAR精度提升。该方法验证了显式特征工程在低信噪比雷达数据中的有效性，但其高计算开销与单帧单人限制限制了实时部署潜力。

】

---

【普林斯顿团队新研究：基于几何一致性的统一LiDAR伪标签生成

研究机构：美国普林斯顿大学

作者：Filippo Ghilotti、Samuel Brucker、Nahku Saidy 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.05105)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.05105)

> 自动驾驶感知研究受制于3D LiDAR标注的高昂成本与多模态对齐难度，现有自动标注方法通常割裂处理深度、检测与分割任务，且依赖难以复现的伪标签或特定数据集配置。UniLiPs通过构建SLAM累积的几何一致地图，将视觉基础模型的2D语义投影至3D空间，利用迭代加权函数区分静态场景与动态物体，实现无监督下三类伪标签的联合生成。该方法在长程场景下显著提升了深度估计精度，并实现了近Oracle级别的语义分割与检测性能，但其对SLAM位姿精度的强依赖及自采数据集的封闭性限制了通用性验证。

】

---

【滑铁卢团队新研究：封闭环境纯雷达人体检测的模型驱动框架

研究机构：加拿大滑铁卢大学

作者：Zhenan Liu、Amir Khajepour、George Shaker

论文原文见 [arXiv](https://arxiv.org/abs/2601.13373)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.13373)

> 工业与地下封闭空间中的粉尘、烟雾及金属多径效应导致光学与激光雷达感知失效，而现有4D毫米波雷达研究多聚焦于室外自动驾驶场景，缺乏针对此类极端环境的专用处理管线。本文切入点在于摒弃依赖大规模标注的学习式检测器，构建一个完全由物理规则驱动的纯雷达感知框架，通过领域感知过滤、自车运动补偿累积及多普勒感知聚类实现实时人体检测。该框架在粉尘拖车与矿井实验中验证了其在视觉与激光雷达失效条件下的稳定性，但其规则阈值在未知复杂动态场景中的泛化边界尚存疑。

】

---

【科学技术院团队新研究：类分布引导的主动学习用于3D占据预测

研究机构：韩国科学技术院、韩国首尔大学

作者：Wonjune Kim、In-Jae Lee、Sihwan Hwang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.27294)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.27294)

> 导读 3D语义占据预测旨在从传感器观测推断完整的三维场景几何与语义，其核心价值在于突破传统3D目标检测对规则形状的依赖。然而，体素级标注成本高昂且存在严重的长尾类别不平衡，导致模型过拟合背景而忽略安全关键物体。本文切入点在于利用类分布结构指导样本选择，通过频率加权不确定性与双重多样性度量，将标注预算精准分配至稀有类信息丰富的样本。该方法在Occ3D-nuScenes上以42.4%的数据量达到接近全监督的性能，但其在夜间等低光照条件下的鲁棒性仍存疑。

】

---

【维也纳技术团队新研究：对称感知旋转表示

研究机构：奥地利维也纳技术大学

作者：Andreas Kriegler、Csaba Beleznai、Margrit Gelautz

论文原文见 [arXiv](https://arxiv.org/abs/2604.18208)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.18208)

> 对称物体在视觉上等效的姿态存在数值歧义，导致标准旋转表示无法建立视觉到数值的单射映射，使得深度学习网络在优化时收敛至多模态分布的均值。现有方案依赖多回归器离散化或对称不变评估指标，前者增加训练复杂度，后者掩盖了优化过程中的歧义问题。本文提出SARR，通过改造三角恒等式将旋转空间限制在规范姿态子空间内，同时保持边界连续性。该表示在T-LESS和ITODD数据集上显著提升了对称物体的姿态估计精度，但其泛化性受限于离散对称类，且未验证在连续对称物体上的有效性。

】

---

【自监督3D占据流估计

作者：Xavier Timoneda、Markus Herb、Fabian Duerr 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.23894)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.23894)

> 3D占据流估计旨在同时预测场景几何占据与运动向量，以支持动态环境下的即时感知。现有方法依赖昂贵的3D流标注或预训练光流模型，导致泛化受限且引入外部偏差。本文切入点在于利用时空一致性与基础模型引导的自监督信号，彻底移除对外部标注的依赖。通过解耦静态与动态SDF并引入特征相似度流损失，该方法实现了无标注的联合几何与运动学习。其价值在于证明了纯视觉自监督流学习的可行性，但依赖基础模型掩码质量这一前提仍存疑。

】

---

【苏黎世团队新研究：事件辅助高速无人机辐射场重建

研究机构：瑞士苏黎世大学

作者：Rong Zou、Marco Cannici、Davide Scaramuzza

论文原文见 [arXiv](https://arxiv.org/abs/2602.21101)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.21101)

> 高速无人机飞行引发的运动模糊与视觉惯性里程计漂移，使得基于神经辐射场（NeRF）的稠密重建面临输入图像失真与位姿不准的双重失效。现有事件相机去模糊方法多采用离线预处理或独立位姿估计，未能利用事件流的高频时序信息直接约束辐射场优化。本文提出一种共享连续时间轨迹的联合优化框架，通过事件与模糊图像的双向监督，在无真值位姿条件下恢复清晰场景。该方法在真实无人机数据上实现了显著的重建质量提升，但其离线优化特性限制了在线实时应用。

】

---

【苏黎世联邦理工团队新研究：静态场景铰接恢复

研究机构：瑞士苏黎世联邦理工学院、德国马克斯·普朗克信息学研究所

作者：Zhao Huang、Boyang Sun、Alexandros Delitzas 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.11340)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.11340)

> 具身智能需要大规模可交互3D环境，但人工标注铰接属性成本高昂，现有生成式方法难以保证几何保真度与物理一致性。REACT3D 提出零样本转换框架，利用视觉基础模型从静态扫描中恢复铰接对象并补全隐藏几何。该方法实现了从标准3D格式到仿真就绪格式（URDF/USD）的自动化映射，解决了静态数据集缺乏交互属性的痛点。其价值在于提供了无需额外数据采集的规模化路径，但盒状几何补全对非规则容器的适应性存疑。

】

---

【萨尔团队新研究：事件驱动神经隐式表面重建

研究机构：德国萨尔大学

作者：Shreyas Sachan、Viktor Rudnev、Mohamed Elgharib 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.03847)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.03847)

> 事件相机3D重建长期受限于稀疏点云输出或依赖RGB辅助，难以在高速运动下获取高精度密集网格。现有基于神经辐射场（NeRF）的方法虽能合成新视角，但其密度场表示导致几何表面模糊且缺乏显式约束。本文提出EventNeuS，通过引入签名距离函数（SDF）并首次应用球谐函数（SH）编码，实现了仅依赖单目事件流的自监督高精度网格重建。该方法在几何精度上显著优于前作，但受限于静态场景假设，对动态非刚性物体的泛化能力存疑。

】

---

【行星环境离线辐射场重建流水线

作者：Alfonso Martínez-Petersen、Levin Gerdes、David Rodríguez-Martínez 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.13909)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.13909)

> 行星探测任务中，漫游车在无GNSS、通信延迟及低纹理地形下需自主感知环境，但传统SLAM因能耗高、模型稀疏且缺乏光度细节而难以满足保守规划需求。现有辐射场方法虽能生成高保真重建，却因预处理复杂、参数调优困难及与车载数据格式不兼容而无法直接部署。本文切入点在于构建一个从原始ROS2数据到Splatfacto-W高斯泼溅重建的全自动离线流水线，通过引入GNSS先验与顺序匹配策略优化几何初始化。该工作验证了辐射场在火星模拟场景下的可行性，但其离线属性与对COLMAP初始化的强依赖限制了其在实时自主导航中的直接应用。

】

---

【野外场景可重光照3D高斯泼溅

作者：Margherita Lea Corona、Wieland Morgenstern、Peter Eisert 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.02801)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.02801)

> 3D高斯泼溅（3D Gaussian Splatting, 3DGS）在静态室内场景中已实现实时渲染，但无法处理户外无约束照片集带来的动态光照与天空反射解耦难题。现有重光照方法要么假设光照恒定，要么仅建模漫反射且将天空与前景混同表示，导致重光照失真与深度伪影。R3GW通过分离前景与天空高斯集合，并在前景中集成Cook-Torrance BRDF与每图像球谐函数（Spherical Harmonics, SH）光照，实现了户外场景的任意环境光重光照。该方法在效率上显著优于神经辐射场（NeRF）基线，但在绝对重建质量上仍略逊于部分NeRF方法，且未显式建模阴影。

】

---

【高丽团队新研究：形状从焦点（SFF）：基于方向性膨胀拉普拉斯与循环网络的混合深度估计

研究机构：韩国高丽大学

作者：Khurram Ashfaq、Muhammad Tariq Mahmood

论文原文见 [arXiv](https://arxiv.org/abs/2512.10498)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.10498)

> 导读 形状从焦点旨在利用焦点栈中图像清晰度的变化恢复场景深度，其核心挑战在于如何从噪声敏感的焦点体积中稳健地提取物理一致的深度图。现有深度学习方法依赖重型编码器提取特征，并通过单步聚合生成深度，导致边缘伪影与噪声放大，而传统方法虽稳健但缺乏全局上下文建模能力。本文提出一种混合框架，使用手工设计的方向性膨胀拉普拉斯核生成多尺度焦点体积，并引入轻量级门控循环单元网络进行迭代式深度细化。该方案在合成与真实数据集上显著优于现有方法，但其对焦点栈输入的依赖及静态场景假设限制了其在动态或单帧场景中的适用性。

】

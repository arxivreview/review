# CVPR2026 · 稠密三维重建与SLAM方向论文汇编

> 本方向共 7 篇（CVPR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【AMB3R: Accurate Feed-forward Metric-scale 3D Reconstruction with Backend ｜紧凑后端前馈度量重建

研究机构：英国伦敦大学学院

作者：Hengyi Wang、Lourdes Agapito

论文原文见 [arXiv](https://arxiv.org/abs/2511.20343)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.20343)

> 稠密三维重建的核心矛盾在于，前馈模型虽能高效回归几何，却因缺乏空间紧凑性导致多视角观测无法融合，且普遍存在尺度模糊问题。现有方案要么依赖耗时的优化后端，要么牺牲精度换取实时性，难以在无标定条件下实现高精度度量重建。AMB3R 通过引入稀疏体素后端强制几何紧凑性，并辅以轻量级尺度头，实现了无需优化后端的前馈式度量重建与大规模运动恢复结构。该工作证明了前馈范式在特定基准上可超越优化方法，但其对长序列流式一致性的适用性仍存疑。

】

---

【Dynamic Visual SLAM using a General 3D Prior ｜动态场景单目视觉SLAM：几何优化与前馈重建的紧耦合

研究机构：德国波恩大学、荷兰代尔夫特理工大学

作者：Xingguang Zhong、Liren Jin、Marija Popović 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.06868)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.06868)

> 动态环境中的移动物体导致传统视觉SLAM产生错误数据关联，进而引发位姿估计崩溃与地图污染。现有方法要么依赖离线分割网络无法在线运行，要么仅将动态物体视为离群点而缺乏显式处理机制。本文切入点在于利用前馈重建模型同时输出运动概率掩码与深度先验，将其嵌入基于补丁的在线光束法平差（Bundle Adjustment, BA）流程中。通过跨批次尺度对齐与不确定性加权优化，该方法在动态场景中实现了比现有SOTA更低的轨迹误差，但其批处理推理延迟是否抵消了在线优势仍存疑。

】

---

【Paparazzo: Active Mapping of Moving 3D Objects ｜动态非合作对象的主动三维映射

研究机构：法国国家科学研究中心

作者：Davide Allegro、Shiyao Li、Stefano Ghidoni 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.19556)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.19556)

> 现有三维重建流水线普遍假设场景静态，无法处理独立运动的非合作对象。被动流式重建方法虽能实时处理动态场景，但缺乏对观测时机与视角信息量的联合规划，导致重建碎片化。Paparazzo 通过扩展卡尔曼滤波预测物体轨迹，并结合三维高斯泼溅模型计算信息增益，实现无学习的双模式主动映射。该方法在模拟环境中显著提升了重建覆盖率，但其性能高度依赖物体运动的可预测性，且未与现有被动重建SOTA进行横向精度对比。

】

---

【Rascene: High-Fidelity 3D Scene Imaging with mmWave Communication Signals ｜射频通信信号三维成像

研究机构：美国密歇根州立大学

作者：Kunzhe Song、Geo Jie Zhou、Xiaoming Liu 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.02603)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.02603)

> 自主导航与机器人感知长期依赖光学传感器，但烟雾、浓雾及非理想光照会导致相机与激光雷达失效。专用雷达虽能穿透遮挡，却受限于昂贵硬件与授权频谱，难以在消费级设备部署。Rascene 利用毫米波通信信号实现单站全双工感知，通过置信度加权的多帧融合抑制多径伪影并恢复几何一致性。该框架在室内场景中实现了跨场景泛化，但其离线重建特性与对位姿精度的敏感性限制了实时动态应用。

】

---

【Revisiting Monocular SLAM with Spatio-Temporal Scene Modeling ｜时空联合查询的单目视觉同步定位与建图

作者：Valter Piedade、Lalit Manam、Masashi Yamazaki 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_00246855b3c3)

> 实时单目SLAM的核心矛盾在于：前馈几何模型能提供无标定稠密先验，但计算开销使其无法在30 FPS视频流中逐帧运行；传统稀疏SLAM虽高效，却依赖精确标定且缺乏稠密重建能力。SLAM-MER的切入点是将“逐帧深度推理”降级为“仅关键帧推理”，并通过时空联合查询机制在稀疏定位与半稠密重建间取得平衡。其价值在于以86.6-103.2 FPS实现了无标定实时SLAM，但3D体素单元在长序列下的内存扩展性未经验证。

】

---

【SCE-SLAM: Scale-Consistent Monocular SLAM via Scene Coordinate Embeddings ｜场景坐标嵌入单目SLAM

研究机构：北京航空航天大学、澳大利亚麦考瑞大学

作者：Yuchen Wu、Jiahe Li、Xiaohan Yu 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.09665)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.09665)

> 单目视觉SLAM在长序列中面临尺度漂移，导致地图碎片化与回环失败。现有帧间优化方法因缺乏全局尺度锚定而失效，而引入外部度量深度或全局注意力模型则牺牲了实时性。SCE-SLAM通过扩展DPVO架构，引入基于几何调制注意力的场景坐标嵌入分支，在保持36 FPS实时性的同时实现尺度一致性。该方法在KITTI数据集上将平均绝对轨迹误差降低至14.07m，但其在动态场景下的鲁棒性及与全局优化方法的长期一致性对比仍存疑。

】

---

【TopoMA: Topology-Guided Multi-Agent Dense RGB 3D Reconstruction via Distributed Inference ｜拓扑引导的多智能体稠密三维重建

研究机构：武汉大学

作者：Xuanxuan Zhang、ShuHui Shi、Tianxiang Zhang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_cbac60dfb69d)

> 多智能体三维重建旨在解决单一相机覆盖复杂环境效率低、独立映射导致尺度漂移与几何错位的问题。现有端到端前馈模型在单智能体场景表现优异，但直接扩展至多智能体时面临通信带宽受限、全局一致性缺失及内存瓶颈。本文切入点在于将场景拓扑结构显式建模为骨架，并以此引导去中心化的回环检测与残差传输。通过构建拓扑骨架、分布式回环及残差传输三个模块，TOPOMA实现了无服务器依赖的全局一致重建。该方法在KITTI与ScanNet上显著优于单智能体基线，但其对动态场景的鲁棒性及与最新流式状态模型的对比缺失，限制了其通用性评估。

】

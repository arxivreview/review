# ICLR2026 · fMRI视觉解码与重建方向论文汇编

> 本方向共 9 篇（ICLR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【A Cognitive Process-Inspired Architecture for Subject-Agnostic Brain Visual Decoding ｜视觉皮层流架构

研究机构：香港科技大学

作者：Jingyu Lu、Haonan Wang、Qixiang Zhang 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.02565)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.02565)

> 导读 fMRI视频解码旨在从脑信号中逆向重建动态视觉体验，但现有方法多依赖单被试训练，面对新患者需耗时12小时以上重训练，临床部署受阻。本文切入点在于将视频解码任务置于跨被试（subject-agnostic）设定下，利用视觉皮层双通路结构解耦主体特定与不变特征。VCFLOW通过层级认知对齐、主体无关重分配适配器及层级显式解码器，实现免重训练的零样本视频重建。该方法在CC2017数据集上平均50-way准确率达14.0%，较基线提升46%，但仅验证了3名被试的泛化能力，其临床普适性仍存疑。

】

---

【Beyond Grid-Locked Voxels: Neural Response Functions for Continuous Brain Encoding ｜神经响应函数（NRF）：基于隐式神经表示的连续脑编码模型

研究机构：美国康奈尔大学

作者：Haomiao Chen、Keith W Jamison、Mert R. Sabuncu 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.07342)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.07342)

> 神经编码旨在从视觉刺激预测fMRI脑响应，但现有模型将3D脑体积展平为1D向量，导致空间信息丢失且模型被锁定在特定被试的体素网格上，无法跨个体迁移。本文提出神经响应函数（NRF），将脑响应建模为MNI标准空间坐标的连续隐式函数，利用局部平滑性与解剖对齐实现数据高效学习与跨被试迁移。实验表明NRF在低数据量下显著优于基线，但其在语义重建保真度上存在解码器偏差干扰，且未验证其在高分辨率动态场景下的泛化能力。

】

---

【Brain-IT: Image Reconstruction from fMRI via Brain-Interaction Transformer ｜脑交互Transformer实现fMRI图像重建

研究机构：以色列魏茨曼科学研究所

作者：Roman Beliy、Amit Zalcher、Jonathan Kogman 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.25976)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.25976)

> fMRI视觉解码旨在从脑活动信号中逆向工程人类感知，其核心价值在于验证视觉编码机制并构建“大脑相机”。现有基于扩散模型的方法虽能生成逼真图像，但常因过度依赖生成先验而偏离实际观看内容的结构与语义，导致重建结果“看似真实但内容错误”。Brain-IT通过引入脑交互Transformer（Brain Interaction Transformer, BIT）将功能相似的脑体素簇映射为局部化图像特征，并结合深度图像先验（Deep Image Prior, DIP）结构分支与扩散模型语义分支，实现了高保真重建。该方法在结构保真度上达到当前最优，且仅需1小时新被试数据即可媲美40小时全量训练效果，但其高层语义相似度仍落后于基于文本空间的最新方法，且未报告计算效率指标。

】

---

【Brain-Semantoks: Learning Semantic Tokens of Brain Dynamics with a Self-Distilled Foundation Model ｜脑动态语义令牌学习

作者：Sam Gijsen、Marc-Andre Schulz、Kerstin Ritter

论文原文见 [arXiv](https://arxiv.org/abs/2512.11582)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.11582)

> fMRI 基础模型旨在从海量无标签脑影像中提取通用表征，以预测疾病与认知表型。现有重建型范式（如 BrainLM、Brain-JEPA）聚焦低层信号恢复，导致表征对噪声敏感且需大量微调。本文切入点在于将学习目标从“信号重建”转向“抽象表型签名”，通过神经科学先验驱动的语义分词器与自蒸馏机制，构建跨数据集稳定的高层表征。该范式在严格线性探测协议下超越重建基线，但其对任务型 fMRI 的适用性及分布偏移边界尚存疑。

】

---

【Learning Brain Representation with Hierarchical Visual Embeddings ｜层级视觉嵌入脑表征学习

研究机构：香港科技大学、北京航空航天大学

作者：Jiawen Zheng、Haonan Jia、Ming Li 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.07495)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.07495)

> 电生理视觉解码旨在从EEG/MEG信号中恢复视觉内容，但现有方法多依赖单一CLIP语义空间，忽略了脑信号中编码的低层像素细节，导致重建保真度受限。本文切入点在于证明脑信号同时包含高层语义与低层结构信息，通过融合CLIP与VAE特征构建层级视觉嵌入，并引入预训练融合先验稳定生成条件。该方法在THINGS-EEG/MEG上实现了零样本检索与重建的双重提升，但其性能高度依赖特定脑编码器组合，且缺乏跨模态（fMRI）的公平对比，其通用性存疑。

】

---

【Moving Beyond Diffusion: Hierarchy-to-Hierarchy Autoregression for fMRI-to-Image Reconstruction ｜层级自回归 fMRI 视觉重建

研究机构：浙江大学、新加坡南洋理工大学

作者：Xu Zhang、Ruijie Quan、Wenguan Wang 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.22335)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.22335)

> fMRI 视觉解码旨在从大脑活动信号中逆向工程人类感知，核心挑战在于弥合神经信号的个体特异性与通用视觉语义空间之间的鸿沟。主流扩散模型范式将 fMRI 信号压缩为单一高维向量作为固定引导，导致层级神经信息丢失且与生成过程的动态阶段需求错配。MindHier 提出层级到层级对齐机制，将脑信号解耦为多尺度特征，并注入自回归模型的不同分辨率阶段，实现从全局语义到局部细节的确定性重建。该方法在语义保真度上超越现有基准，但牺牲了部分低层像素细节，其确定性生成策略在复杂场景下的鲁棒性仍需进一步验证。

】

---

【Neuro-Symbolic Decoding of Neural Activity ｜神经符号解码神经活动

研究机构：美国哥伦比亚大学、美国斯坦福大学

作者：Yanchen Wang、Joy Hsu、Ehsan Adeli 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.03343)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.03343)

> 该方向旨在从fMRI信号中逆向工程人类感知，但现有主流范式聚焦于像素级重建或孤立概念分类，难以捕捉概念间的高阶关系语义。线性模型缺乏交互建模能力，端到端神经网络则倾向于整体编码，导致对细粒度组合查询的泛化能力不足。本文提出NEURONA，通过神经符号框架将查询解析为符号表达式，并在功能图谱划分的脑区上执行可微组合推理。该方法在未见过的组合查询上显著优于基线，验证了结构先验对关系语义解码的关键作用，但其结论受限于缺乏系统性组合操纵的数据集，无法直接证明神经活动本身的组合性。

】

---

【Seeing Through the Brain: New Insights from Decoding Visual Stimuli with fMRI ｜基于结构化文本空间的fMRI视觉重建

研究机构：美国达特茅斯学院、美国耶鲁大学

作者：Zheng Huang、Enpei Zhang、Yinghao Cai 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.16196)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.16196)

> 导读 fMRI视觉解码旨在从大脑活动信号中逆向工程人类感知，其核心价值在于验证视觉编码机制并构建“大脑相机”。现有主流范式依赖CLIP视觉嵌入作为潜在空间，但统一隐表示常混淆物体与属性，导致语义幻觉。PRISM通过证明语言模型文本空间与fMRI信号对齐度更高，并引入对象中心生成机制，实现了更精准的语义重建。该方法在NSD数据集上取得0.9467的CLIP相似度，但对象拼接策略对全局纹理连贯性的影响尚存疑。

】

---

【Towards Interpretable Visual Decoding with Attention to Brain Representations ｜脑区直接条件化的可解释视觉解码

研究机构：美国哥伦比亚大学

作者：Pinyuan Feng、Hossein Adeli、Wenxuan Guo 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.23566)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.23566)

> 该方向旨在从大脑活动中逆向工程人类视觉感知，但现有主流范式依赖中间特征空间（如CLIP嵌入）作为语义桥梁，导致脑区对生成过程的贡献被掩盖，难以进行神经科学层面的机制解析。本文切入点在于绕过中间表示，直接以脑区Token条件化扩散模型，并配套双向可解释性框架。具体做法是通过Schaefer分区将fMRI转化为结构化Token，利用交叉注意力注入Stable Diffusion，并分析注意力动态以揭示脑区-图像区域映射。其价值在于实现了端到端解码与机制透明性的统一，但缺乏与最新SOTA的直接数值对标，且未解决扩散模型固有的随机性问题。

】

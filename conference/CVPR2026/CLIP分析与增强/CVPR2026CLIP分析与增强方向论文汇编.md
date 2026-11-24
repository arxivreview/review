# CVPR2026 · CLIP分析与增强方向论文汇编

> 本方向共 21 篇（CVPR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【A Causal Marriage between VLM and IRM from Understanding to Reasoning ｜因果不变性视角下的CLIP中间训练与多模态推理增强

研究机构：香港科技大学、中山大学

作者：Ziliang Chen、Tianang Xiao、Jusheng Zhang 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1186818afb40)

> 视觉语言模型在分布外（OOD）场景下的泛化能力长期缺乏理论解释，现有对抗微调或不确定性校准方法仅能缓解特定攻击，无法从机制上消除虚假相关。本文切入点在于证明CLIP的对比学习目标在词元级因果分解下等价于不变风险最小化（IRM）目标，从而将OOD鲁棒性从经验现象转化为可优化的数学约束。通过构建类-环境词汇表并实施中间训练，本文在不改变双塔架构的前提下注入不变性信号，并将其扩展为多模态大语言模型（MLLM）的强化学习奖励。该工作提供了CLIP泛化能力的因果理论基石，但其依赖人工构建的词汇表，限制了开放词汇场景下的通用性。

】

---

【b-CLIP: Text-Conditioned Contrastive Learning for Multi-Granular Vision-Language Alignment ｜β-CLIP：基于文本条件对比学习的多粒度视觉-语言对齐

研究机构：沙特阿拉伯阿卜杜拉国王科技大学

作者：Fatimah Zohra、Chen Zhao、Hani Itani 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_305112adc0bb)

> 导读 CLIP 的全局对比学习范式导致其缺乏细粒度的空间-语义对齐能力，这是其在密集预测任务中表现不佳的根本原因。现有方法或依赖显式区域框监督，或采用启发式分组，难以在无区域标注条件下实现精准的局部-文本对应。本文提出 β-CLIP，通过层级文本分解引导交叉注意力池化，并引入 β-CAL 损失平衡特异性与上下文整合。该方法在无硬负样本约束下于长文本检索任务达到 SOTA，但细粒度检测性能仍低于使用硬负样本的基线，且训练-推理分布不一致的影响未充分量化。

】

---

【Beyond Text: Visual Description Assembly by Probabilistic Model for CLIP-based Weakly Supervised Semantic Segmentation ｜视觉描述组装

研究机构：英国利物浦大学

作者：Xianglin Qiu、Jian Wang、Xiaolei Wang 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_6b5b578f3168)

> 弱监督语义分割（WSSS）依赖图像级标签生成类激活图（CAM），但CLIP固有的模态间隙导致静态文本原型无法紧密对齐视觉特征，致使CAM覆盖不完整。现有方法聚焦于优化文本描述，却忽视了文本与视觉嵌入空间分布不匹配的根本缺陷。本文提出视觉描述组装（VDA）框架，利用可逆神经网络（INN）将视觉特征映射至高斯混合模型（GMM）潜空间，动态组装实例特定的视觉原型作为查询。该方法在PASCAL VOC 2012和MS COCO 2014上取得SOTA性能，但其对GMM高斯分布假设的依赖及缺乏与最新SOTA的直接数值对比，限制了其通用性验证。

】

---

【CLEP: Contrastive Language-Pose Pretraining ｜姿态-语言对比预训练

作者：Sen Jia、Huayu Wang、Hsiang-Wei Huang 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_093466ca6e40)

> 姿态-语言对齐旨在建立3D人体姿态与复杂自然语言描述间的共享嵌入空间，以支撑检索、生成与编辑等下游任务。现有方法受限于数据规模不足与姿态表征的扁平化，导致跨域泛化能力薄弱且难以捕捉多尺度语义。本文通过构建200万级数据集CLEP-2M，并设计层级姿态编码器HierFormer，利用SigLIP损失实现姿态与文本的细粒度对齐。该框架在零样本检索上实现了近6倍的基线超越，但其静态姿态假设与时序缺失限制了动态场景的适用性。

】

---

【CLIP Is Shortsighted: Paying Attention Beyond the First Sentence ｜长文本检索中的摘要句捷径消除

研究机构：加拿大多伦多大学、加拿大魁北克人工智能研究所

作者：Marc-Antoine Lavoie、Anas Mahmoud、Aldo Zaimi 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.22419)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.22419)

> 长文本检索模型在微调后仍过度依赖首句摘要，导致信息位置偏移时性能崩塌。现有方法通过架构修改或复杂训练流程扩展上下文，却未能解决预训练阶段形成的早期token偏差。本文通过移除摘要句、句子采样与前缀填充的数据增强策略，在不增加参数的情况下重新分配注意力分布。该方法在长文本检索上取得SOTA，但仅针对文本侧偏差，未解决图像侧对深层细节的感知局限。

】

---

【Concept Regions Matter: Benchmarking CLIP with a New Cluster-Importance Approach ｜概念区域重要性：基于聚类掩码的CLIP虚假相关诊断

研究机构：Adobe研究院

作者：Aishwarya Agarwal、Srikrishna Karanam、Vineet Gandhi

论文原文见 [arXiv](https://arxiv.org/abs/2511.12978)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.12978)

> 对比视觉-语言模型（VLM）在零样本任务中常依赖背景线索而非前景物体，导致分布偏移下性能崩溃。现有基准如CounterAnimals仅用准确率代理背景敏感性，无法区分背景依赖与细粒度混淆，且梯度归因方法产生的热力图噪声大、缺乏语义连贯性。本文提出免训练的可解释性方法CCI，通过聚类补丁嵌入并掩码来量化区域贡献，并构建受控基准COVAR以解耦视觉因子。该方法在忠实度指标上显著优于基线，但合成背景的生态效度及掩码策略对分布偏移的影响仍存疑。

】

---

【Explaining CLIP Zero-shot Predictions Through Concepts ｜概念瓶颈CLIP零样本预测解释

研究机构：英国爱丁堡大学、丹麦技术大学

作者：Onat Ozdemir、Anders Christensen、Stephan Alaniz 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.28211)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.28211)

> 现有视觉-语言模型（VLM）如CLIP虽具备强大的零样本泛化能力，但其高维纠缠的嵌入空间导致预测过程对人类不透明，而经典概念瓶颈模型（CBM）虽提供可解释性却受限于闭集假设与密集监督需求。本文切入点在于不重新训练CLIP，而是通过一个轻量级可学习投影矩阵将其图像-文本嵌入映射至共享概念空间，利用匹配损失与重构损失联合优化，在保持零样本精度的同时输出人类可理解的概念级解释。该方案在五个基准上验证了性能损失极小且解释忠实，但其概念空间静态性与跨域迁移的泛化边界仍存疑。

】

---

【From Weights to Concepts: Data-Free Interpretability of CLIP via Singular Vector Decomposition ｜从权重到概念：基于奇异向量分解的CLIP数据无关可解释性

作者：Francesco Gentile、Nicola Dall'Asen、Francesco Tonini 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.24653)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.24653)

> 视觉语言模型在大规模部署中面临内部机制黑盒化的挑战，现有激活值解释方法依赖大规模数据集且解释粒度粗，难以实现无数据、无训练的细粒度概念定位。本文提出SITH框架，直接对CLIP视觉Transformer的注意力头权重进行奇异值分解，并通过COMP算法将奇异向量映射为稀疏且语义连贯的概念组合。该方法实现了向量级的输入无关解释，并支持通过调整奇异值进行免训练模型编辑，但在注意力路由机制的完整性与跨层交互效应的建模上存在简化。

】

---

【Guiding Diffusion-based Reconstruction with Contrastive Signals for Balanced Visual Representation ｜扩散对比重构

研究机构：中科院计算所、中国科学院大学

作者：Boyu Han、Qianqian Xu、Shilong Bao 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.04803)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.04803)

> 扩散模型重构图像能提升CLIP视觉编码器的细节感知能力，但会削弱其类别判别能力，现有方法无法同时优化这两者。本文发现直接叠加对比损失与重构损失会导致严重的梯度冲突，提出在重构噪声空间内构建对比三元组，以单一目标统一优化判别力与感知力。该方法在MMVP-VLM基准上取得33.3%的平均准确率，优于DIVA的25.9%。其价值在于解决了生成式反馈与判别式学习的优化冲突，但未验证该增强是否损害CLIP原有的零样本泛化能力。

】

---

【IsoCLIP: Decomposing CLIP Projectors for Efficient Intra-modal Alignment ｜IsoCLIP：基于谱分解的CLIP模态内对齐

研究机构：意大利佛罗伦萨大学

作者：Simone Magistri、Dipam Goswami、Marco Mistretta 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.19862)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.19862)

> 导读 CLIP在跨模态检索中表现优异，但在纯图像或纯文本检索等模态内任务中，因训练损失仅优化跨模态相似度而存在固有的模态内失配。现有的模态反转方法虽能缓解此问题，但依赖大量迭代优化，导致推理延迟极高。本文通过解析CLIP投影头的几何结构，发现跨模态算子中存在一个近似各向同性的中间谱带，该谱带承载了共享语义信息。IsoCLIP通过SVD分解保留该中间谱带并剔除两端各向异性方向，实现了无额外延迟的模态内对齐增强。该方法在多个基准上显著优于基线，但其性能提升是否以牺牲跨模态检索能力为代价，论文未提供直接证据。

】

---

【Learning complete and explainable visual representations from itemized text supervision ｜条目化文本监督下的视觉表示学习

研究机构：美国密歇根大学、美国伊利诺伊大学厄巴纳-香槟分校

作者：Yiwei Lyu、Chenhui Zhao、Soumyanil Banerjee 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.11141)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.11141)

> 非物体中心域（如医疗影像、遥感）的文本标注通常由多个语义独立、空间分离的发现项组成，而非冗余描述。现有CLIP变体假设多正样本描述同一内容，导致模型无法区分独立病灶或遗漏关键发现。本文提出ItemizedCLIP，通过交叉注意力生成文本条件视觉嵌入，并引入条目分离与完整性约束损失。该方法在脑MRI等四个医疗域及遥感域实现了零样本性能提升与可解释性，但其优势在通用自然图像域是否成立尚存疑。

】

---

【Learning from Itself: Mining Internal Knowledge from Vision Language Models for Continual Learning ｜从自身学习：挖掘视觉语言模型内部知识的持续学习

研究机构：英国利物浦大学

作者：Yizheng Gong、Siyue Yu、Waleed Al-Nuaimy 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ca702b49a8cc)

> 持续学习要求模型在顺序任务流中避免灾难性遗忘，但CLIP等视觉语言模型面临预训练描述与下游类名间的文本分布差距，以及视觉编码器与文本编码器在细粒度任务上的性能不匹配。现有方法或依赖外部模型生成描述，或仅微调提示参数，未能利用模型内部互补知识。本文提出LfI，通过自生成伪描述和自适应互蒸馏，让CLIP挖掘并重组自身内部知识。该方法在多个基准上取得SOTA，但全参数微调策略在大规模任务序列中的稳定性存疑。

】

---

【Leveraging Class Distributions in CLIP for Weakly Supervised Semantic Segmentation ｜基于类分布的CLIP弱监督语义分割

研究机构：英国利物浦大学

作者：Ziqian Yang、Xinqiao Zhao、Xiaolei Wang 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_25241badab10)

> 图像级弱监督语义分割（WSSS）的核心痛点在于CLIP生成的类激活图（CAM）仅覆盖显著区域，导致细粒度定位失效。现有基于多头自注意力（MHSA）亲和度的细化方法因无法建立准确的类内语义关系，致使目标类激活不足。本文提出CD-CLIP框架，通过Jensen-Shannon散度构建类分布相似度矩阵修正亲和度，并引入DINO特征生成超类边界监督。该方法在PASCAL VOC 2012上取得82.5% mIoU，但依赖外部DINO特征解决边界过激活问题，其纯CLIP内部机制的完备性存疑。

】

---

【PowerCLIP: Powerset Alignment for Contrastive Pre-Training ｜PowerCLIP：基于幂集对齐的对比预训练框架

研究机构：日本东京科学大学、英国牛津大学

作者：Masaki Kawamura、Nakamasa Inoue、Rintaro Yanagi 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.23170)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.23170)

> 导读

】

---

【Reconstructing CLIP for Open-Vocabulary Dense Perception ｜重构 CLIP 密集表示以对齐全局语义

研究机构：北京航空航天大学

作者：Yajie Liu、Jinjin Zhang、Qingjie Liu 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_681a680cf946)

> 开放词汇密集感知（OVDP）要求模型在像素或区域级别识别任意视觉概念，但 CLIP 的全局 [CLS] 特征缺乏空间细节，导致密集预测性能受限。现有自蒸馏方法通过空间聚合构建密集特征，却引入了无关语义噪声与对齐误差。本文切入点在于揭示 [CLS] token 的语义本质编码于多层 Value 嵌入中，并证明空间聚合会放大对齐误差。通过设计头选择性门控（HSG）模块替代空间聚合，并引入视觉基础模型特征一致性蒸馏，DenseRC 实现了与全局语义结构一致的密集表示。该方法在多个 OVDP 基准上刷新了 SOTA，但其对 VFM 辅助蒸馏的依赖是否破坏 CLIP 原生几何一致性，仍存疑。

】

---

【Reevaluating the Intra-Modal Misalignment Hypothesis in CLIP ｜模态内失配假设的再评估

研究机构：浙江大学

作者：Jonas Herzog、Yue Wang

论文原文见 [arXiv](https://arxiv.org/abs/2603.16100)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.16100)

> 该方向旨在解决CLIP在纯视觉任务（如图像检索、少样本分类）中表现不佳的问题，主流归因于跨模态训练导致的模态内几何失配。现有方法通过文本反转或分布归一化规避图像-图像相似度，但缺乏对失配假设本身的理论验证。本文通过线性代数证明自由度消失，并利用纯视觉模型对照实验证伪该假设，提出基于主成分分析的简单投影替代方案。其价值在于重构了领域对CLIP嵌入空间几何特性的认知，但PCA投影在长尾分布下的鲁棒性仍存疑。

】

---

【Subspace Alignment for CLIP-based Continual Learning via Canonical Correlation Analysis ｜基于典型相关分析的CLIP持续学习子空间对齐

研究机构：武汉大学

作者：Huan Zhang、Shuyu Dong、Yujin Zheng 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0d7e3bf35d90)

> 持续学习中的CLIP模型面临视觉与文本编码器更新速率不匹配导致的模态距离累积问题，现有方法多通过参数微调或额外模块缓解，但易破坏预训练表示或引入额外计算开销。本文指出这一非对称漂移（Asymmetric Drift, AD）是性能退化的核心几何原因，并提出通过累积跨任务协方差统计量求解闭式典型相关分析（Canonical Correlation Analysis, CCA）投影矩阵，将双模态特征映射至共享子空间以最小化距离。该方法无需梯度更新即可实现高效对齐，在CIFAR-100上取得83.0%的Last Accuracy，但其线性假设对复杂非线性关系的捕捉能力仍存疑。

】

---

【SynCLIP: Synonym-Coherent Language-Image Pretraining for Robust Open-Vocabulary Dense Perception ｜同义词一致性语言图像预训练

研究机构：北京航空航天大学、南京大学

作者：Mingjie Xie、Guangjun He、Dongli Xu 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2607.11008)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2607.11008)

> 开放词汇密集感知（OVDP）旨在利用文本知识定位训练集中未定义的物体类别，但现有基于CLIP的方法存在“同义词诱导的接地不一致”缺陷：语义等价的表达导致空间注意力分布发散，削弱了模型在真实场景中的鲁棒性。SynCLIP通过构建同义词增强视觉语料库（SEViC），引入语义一致空间注意力对齐（SSA）与空间注意力精炼（SAR）模块，强制不同同义表达产生一致且精确的空间定位。该方法在OV-COCO和OV-LVIS基准上取得了CLIP类方法中的最优性能，但其对下游检测器架构的依赖及同义词生成的语义保真度边界，仍需在更广泛的词汇分布下进一步验证。

】

---

【Vocabulary Scaling Law: Tuning Open-vocabulary Predictors for Their Openness ｜词汇缩放定律下的子模微调

研究机构：中山大学、新加坡南洋理工大学

作者：Ziliang Chen、Yulu Li、Liangda Fang 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_26e1093b9c28)

> 开放词汇预测在真实开放世界中面临词汇规模扩展导致的性能衰减，现有微调方法因仅针对封闭集优化而失效。本文切入点在于形式化“词汇缩放定律”，指出微调必须考虑全词汇宇宙而非仅目标类。通过双层优化框架，外层利用子模最大化贪心选择代表性类名子集，内层微调类名嵌入并施加正交约束。该方法在稳定性与可扩展性上均取得提升，但子模选择相较于随机采样的优势缺乏消融验证，且正交约束的超参数敏感性未充分探讨。

】

---

【When CLIP Sees More, It Fights Back Harder: Multi-View Guided Adaptive Counterattacks for Test-Time Adversarial Robustness ｜多视图引导自适应反攻击

作者：Sunoh Kim、Daeho Um

论文原文见 [arXiv](https://arxiv.org/abs/2606.06938)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.06938)

> CLIP 在强对抗攻击下鲁棒性崩塌，现有测试时防御方法或依赖高开销的逐样本调优，或受限于单视图引导的脆弱性。本文指出测试时反攻击（TTC）失效的根源在于对直接受扰原图的依赖及噪声驱动的硬门控机制，提出多视图引导自适应反攻击（MAC）框架。通过生成增强视图并基于腐蚀度进行软加权，MAC 在保持零样本泛化能力的前提下，显著提升了强攻击下的鲁棒性，但其对特定攻击分布的适应性及骨干网络限制仍存疑。

】

---

【WikiCLIP: An Efficient Contrastive Baseline for Open-domain Visual Entity Recognition ｜开放域视觉实体识别中的对比学习基线

研究机构：上海科技大学

作者：Shan Ning、Longtian Qiu、Jiaxuan Sun 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.09921)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.09921)

> 开放域视觉实体识别（VER）要求模型在百万级长尾实体空间中精准定位图像对应的百科条目，现有生成式方法虽性能强劲但推理延迟高达秒级且泛化能力受限。本文指出对比学习范式被低估，其瓶颈在于CLIP文本编码器无法处理长文本且缺乏细粒度区分度，而非范式本身。WikiCLIP通过冻结LLM与CLIP骨干，仅训练0.08B参数的视觉引导知识适配器（VGKA）及硬负样本合成机制，实现了14.49ms的低延迟推理与28.5%的未见实体准确率。该工作确立了高效对比基线，但其对LLM知识利用的深度及背景依赖问题仍存疑。

】

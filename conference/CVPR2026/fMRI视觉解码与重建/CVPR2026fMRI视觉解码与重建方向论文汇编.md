# CVPR2026 · fMRI视觉解码与重建方向论文汇编

> 本方向共 9 篇（CVPR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Bridging Brain and Semantics: A Hierarchical Framework for Semantically Enhanced fMRI-to-Video Reconstruction ｜基于记忆融合与多模态语义增强的fMRI视频重建框架

研究机构：复旦大学、阿里巴巴集团

作者：Yujie Wei、Chenglong Ma、Jianxiong Gao 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.14569)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.14569)

> fMRI视频重建旨在从低时间分辨率的脑信号中恢复动态视觉体验，核心难点在于信号稀疏导致的语义缺失与时序断裂。现有方法仅依赖当前刺激的孤立解码，缺乏对历史语义知识的利用，导致重建视频出现对象错误与动作缺失。本文提出CINENEURON，通过自底向上的多模态语义增强与自顶向下的记忆融合机制，将孤立解码转化为上下文感知解码。该框架在语义与时空指标上显著优于基线，但其记忆池依赖训练集分布，对未见视频的泛化能力存疑。

】

---

【CineBrain: A Large-Scale Multi-Modal Audiovisual Brain Dataset for Brain-Conditioned Video Generation ｜视听同步脑信号视频重建

研究机构：复旦大学

作者：Jianxiong Gao、Yichang Liu、Baofeng Yang 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_bf7a7b395271)

> 现有脑解码研究多依赖单一神经模态处理纯视觉刺激，忽略了听觉对视觉感知的调制作用及 fMRI 与 EEG 在时空分辨率上的互补性。本文提出 CineBrain 数据集与 CineSync 框架，通过双 Transformer 独立编码 fMRI 与 EEG 信号，利用联合对比学习对齐语义空间，并基于扩散模型生成视频。该工作验证了多模态融合在动态视频重建中的有效性，但受限于仅 6 名被试且缺乏跨数据集泛化验证，其结论的普适性存疑。

】

---

【Duala: Dual-Level Alignment of Subjects and Stimuli for Cross-Subject fMRI Decoding ｜双层对齐的跨被试fMRI解码

研究机构：南京大学

作者：Shumeng Li、Jintao Guo、Jian Zhang 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.07625)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.07625)

> 跨被试fMRI视觉解码旨在将预训练模型迁移至新被试，但现有微调策略常导致语义结构崩塌与个体差异失配。本文指出微调过程破坏了预训练阶段建立的脑-视觉对应关系，提出双层对齐框架Duala。该方法通过刺激级语义保持与主体级分布扰动，在仅1小时数据下实现81.1%的脑检索准确率。其价值在于以轻量正则化解决了少样本适配中的语义退化问题，但评估局限于NSD数据集的特定子集，未验证零样本或更大规模被试的泛化边界。

】

---

【fMRI-LM: Towards a Universal Foundation Model for Language-Aligned fMRI Understanding ｜fMRI 语言对齐基础模型

研究机构：美国佐治亚理工学院

作者：Yuxiang Wei、Yanteng Zhang、Xi Xiao 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.21760)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.21760)

> 现有 fMRI 基础模型仅依赖神经信号自监督目标，缺乏语义接地，导致跨任务泛化能力受限且无法进行自然语言交互。本文切入点在于构建合成 fMRI-文本描述语料，通过三阶段框架将 fMRI 信号映射至 LLM 文本嵌入空间。具体做法是训练文本对齐的 fMRI 分词器，微调 LLM 进行时序预测与文本生成，最后进行多任务指令微调。该框架在通用理解任务上显著优于传统监督与自监督基线，但其表征是否适用于视觉重建等下游任务尚存疑。

】

---

【Meta-learning In-Context Enables Training-Free Cross Subject Brain Decoding ｜层级上下文学习实现零样本脑解码

研究机构：香港中文大学、美国哈佛大学

作者：Mu Nan、Muquan Yu、Weijian Mai 等 15 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.08537)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.08537)

> fMRI 视觉解码旨在从大脑活动信号中逆向工程人类感知，核心瓶颈在于个体间神经表征的巨大差异导致模型无法跨被试泛化。现有主流方法依赖针对每个新被试的梯度微调或解剖对齐，计算成本高且部署复杂，难以满足通用脑机接口的需求。本文提出 BrainCoDec，通过元优化层级上下文学习机制，在推理时动态推断新被试的编码参数，实现无需微调、无需解剖对齐的零样本解码。该方法在严格约束下显著优于传统基线，但其在有监督多被试场景下的性能上限及计算开销仍存疑。

】

---

【Modeling Spatiotemporal Neural Frames for High Resolution Brain Dynamic ｜基于扩散Transformer的EEG条件fMRI时空重建

研究机构：复旦大学、南方科技大学

作者：Wanying Qu、Jianxiong Gao、Wei Wang 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.24176)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.24176)

> 导读

】

---

【Modeling the Brain's Grammar: ROI-Guided fMRI Pretraining for Transferable and Interpretable Vision Decoding ｜基于感兴趣区（ROI）的 fMRI 预训练框架：ROITok

研究机构：香港科技大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0ce51560fbb7)

> 导读 fMRI 视觉解码旨在从大脑活动信号中逆向工程人类感知，其核心价值在于验证视觉编码机制并构建“大脑相机”。现有跨被试方法多采用全脑体素扁平化或任意空间切分，忽略了大脑皮层的功能拓扑结构，导致少样本场景下泛化能力受限。ROITok 将感兴趣区（ROI）作为计算单元进行 Token 化，结合稀疏上下文融合与 Matryoshka 表示学习策略，构建具备神经科学可解释性的共享表征空间。该方法在 NSD 数据集的少样本迁移任务中取得了领先的低层重建保真度，但其高层语义对齐性能与部分基于 Transformer 的基线相比存在细微差距，且对噪声鲁棒性的评估仅基于合成高斯噪声，生理噪声下的表现尚待验证。

】

---

【NeuroFlow: Toward Unified Visual Encoding and Decoding from Neural Activity ｜神经流匹配统一视觉编码与解码

研究机构：清华大学、香港中文大学

作者：Weijian Mai、Mu Nan、Yu Zhu 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.09817)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.09817)

> 视觉编码与解码长期被视为两个独立任务，前者预测脑活动，后者重建图像，导致模型无法验证双向一致性。现有方法依赖两个独立网络或单向条件扩散，缺乏共享潜在空间，无法保证合成神经信号能反向还原出语义一致的图像。NeuroFlow 通过变分自编码器构建语义结构化潜在空间，并利用跨模态流匹配建立可逆的时间依赖流，在单一模型内统一了编码与解码。该框架以 25% 的参数量实现了与主流解码模型相当的性能，并首次通过脑功能分析验证了合成信号的神经可解释性，但其对预训练视觉骨干的依赖及单被试实验设置限制了其泛化能力的评估。

】

---

【SemVideo: Reconstructs What You Watch from Brain Activity via Hierarchical Semantic Guidance ｜层级语义引导的fMRI视频重建

研究机构：北京邮电大学

作者：Minghan Yang、Lan Yang、Ke Li 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.21819)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.21819)

> fMRI视频重建旨在从缓慢的血氧水平依赖信号中恢复动态视觉体验，核心矛盾在于脑信号的低时间分辨率与视频高动态性之间的失配。现有方法多依赖单帧图像描述或单一潜空间对齐，导致重建视频出现外观不一致与运动错位。本文切入点在于利用多模态大语言模型挖掘视频的多层级文本语义，作为中间监督信号引导解码与生成。通过构建语义对齐解码器、运动适配解码器及多阶段渲染框架，SemVideo在CC2017数据集上实现了语义与时空指标的最优表现，但其对高质量视频字幕模型的依赖及像素级保真度的相对短板，限制了其在低信噪比场景下的泛化潜力。

】

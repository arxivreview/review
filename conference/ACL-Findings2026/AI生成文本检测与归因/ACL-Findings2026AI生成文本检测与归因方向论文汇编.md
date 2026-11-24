# ACL-Findings2026 · AI生成文本检测与归因方向论文汇编

> 本方向共 11 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【C-ReD: A Comprehensive Chinese Benchmark for AI-Generated Text Detection Derived from Real-World Prompts ｜中文真实提示词AI生成文本检测基准

研究机构：清华大学、南开大学

作者：Chenxi Qing、Junxi Wu、Zheng Liu 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.11796)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.11796)

> 现有中文AI生成文本检测基准普遍依赖单一生成模型与简化问答格式，无法反映多领域、多国产大模型的真实应用场景。C-ReD通过构建涵盖5个领域、9个LLM及真实提示词的基准，系统评估了零样本与监督检测器在中文语境下的泛化瓶颈。该工作揭示了推理密集型模型（如Deepseek-R1）对检测器的显著挑战，并验证了多域微调对跨模型泛化的提升作用。其价值在于填补了中文检测基准的空白，但缺乏对对抗改写攻击的直接测试，且未量化提示词复杂度对检测难度的因果影响。

】

---

【CEAID: Benchmark of Multilingual Machine-Generated Text Detection Methods for Central European Languages ｜中欧语言机器生成文本检测基准

作者：Dominik Macko、Jakub Kopal

论文原文见 [arXiv](https://arxiv.org/abs/2509.26051)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.26051)

> 导读 机器生成文本（Machine-Generated Text, MGT）检测长期聚焦于英语等高资源语言，导致低资源语言面临严重的跨语言迁移性能衰减。现有零样本统计方法在形态复杂的非英语语言中失效，而通用监督模型又缺乏区域特定训练数据。本文构建了首个中欧区域多语言MGT检测基准，系统评估了训练语言组合对跨语言泛化及对抗鲁棒性的影响。该研究证实了监督微调在低资源场景下的必要性，并揭示了同形异义字攻击对斯拉夫语系的特异性破坏力。然而，其结论受限于拉丁脚本语言，对非拉丁语系的适用性仍存疑。

】

---

【ExaGPT: Example-Based Machine-Generated Text Detection for Human Interpretability ｜基于示例检索的可解释AI文本检测

研究机构：日本东京科学大学、日本国立情报学研究所

作者：Ryuto Koike、Masahiro Kaneko、Ayana Niwa 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2502.11336)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e06fc3ec5ec3)

> 高利害场景下的AI文本检测面临误判风险，现有高精度检测器多为黑盒，无法提供用户可验证的证据以判断预测可靠性。本文切入点在于模拟人类直觉——通过比对文本与已知来源库中相似片段的分布来判定作者，而非依赖参数化分类器的概率输出。ExaGPT利用k-NN检索获取语义相似片段作为证据，并通过动态规划优化片段分割以平衡长度与可靠性。该方法在可解释性上显著优于基线，且在低假阳性率下检测精度达到或超过监督学习模型，但其性能高度依赖数据店的质量与覆盖度，对未见领域的泛化能力存疑。

】

---

【GigaCheck: Detecting LLM-generated Content via Object-Centric Span Localization ｜基于对象检测范式的LLM生成文本跨度定位

作者：Irina Tolstykh、Aleksandra Tsybina、Sergey Yakubson 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2410.23728)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_5474e7dbf1d3)

> 人机协作文本中AI片段的精确边界识别是现有文档级检测器无法解决的痛点，传统序列标注方法依赖繁琐的后处理且对句子结构敏感。GigaCheck将文本跨度检测重构为一维目标检测问题，利用DETR架构直接回归字符区间，消除了对句子边界的依赖。该方法通过共享LoRA微调骨干同时支持细粒度定位与文档级分类，在三个定位基准上显著优于基线，但其对多语言及极端长文本的适用性仍存疑。

】

---

【Leveraging Human and Machine Preferences for Zero-shot Detection of AI-Generated Text ｜人机预测差异适配器

研究机构：中国科学院大学、中国科学院

作者：Lei Jiang、Desheng Wu、Xiaolong Zheng 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_3098a836ff0d)

> 零样本AI生成文本检测长期受困于“机器中心”视角，即仅依赖单一代理模型计算token似然并简单平均，导致在高质量生成文本面前区分度不足。现有方法忽略了人类与机器在同一文本上预测分布的结构性差异，而这一差异恰恰蕴含了作者身份的互信息。HAPDA通过联合微调一对偏好模型，将人机预测分歧转化为token级权重，对MeanZero类检测器进行校准。该方法在RAID基准上显著提升了基线性能，但其对微调数据分布的隐性依赖及双模型推理开销，限制了其在开放环境中的泛化潜力。

】

---

【MASH: Evading Black-Box AI-Generated Text Detectors via Style Humanization ｜风格迁移驱动的黑盒检测规避

研究机构：东南大学

作者：Yongtong Gu、Songze Li、Xia Hu

论文原文见 [arXiv](https://arxiv.org/abs/2601.08564)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_77252866214f)

> 现有AI生成文本检测器在对抗攻击下表现脆弱，而主流规避方法依赖白盒访问或高昂算力，难以在真实黑盒场景中落地。MASH将检测规避重构为“机器到人类”的风格迁移任务，通过多阶段对齐使AI文本风格逼近人类分布。其核心在于利用风格注入微调解决直接偏好优化的冷启动问题，并引入推理时精炼保证文本质量。该方法以极小模型实现了高攻击成功率，但暴露了检测器对风格特征过度依赖的深层缺陷，其长期有效性仍存疑。

】

---

【Reasoning-Aware AIGC Detection via Alignment and Reinforcement ｜推理增强型AI生成文本检测

研究机构：中国人民大学、美国杜克大学

作者：Zhao Wang、Max Xiong、Jianxun Lian 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.19172)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.19172)

> 现有AI生成文本检测器依赖表面统计特征，在跨域泛化与细粒度人机协作场景下失效，且黑盒输出无法提供可验证的归因证据。REVEAL通过SFT蒸馏推理链与RL强化逻辑一致性，将检测重构为“先推理后分类”的透明决策过程。该方法在跨域基准上显著优于传统分类器与通用大模型，但在高置信度校准与推理效率上存在明显权衡。

】

---

【Synergizing Stylometrics with Semantics: Dual-Path Framework for LLM Detection and Attribution ｜风格语义双路径融合框架

研究机构：重庆大学

作者：Xingyu Lu、Yumeng Ma、Xiang Zhou 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_df816e868c2b)

> 细粒度LLM归因旨在识别文本的具体生成模型，而非仅区分人机。现有统计信号在短文本中方差过大，纯语义模型则陷入黑盒且依赖海量标注，导致在语义同质化场景下失效。SSLA通过提取词汇、句法与结构层面的显式风格指纹，并与RoBERTa隐式语义嵌入进行双路径自注意力融合，实现了跨域鲁棒的模型溯源。该方法在Wikipedia数据集上取得95.6%的Macro-F1，验证了风格惯性在语义模糊场景下的判别力，但其对改写探针的依赖及缺乏最新SOTA对比限制了其通用性评估。

】

---

【Temporal Flattening in LLM-Generated Text: Comparing Human and LLM Writing Trajectories ｜时间扁平化：LLM生成文本的纵向动态缺失

研究机构：美国东北大学

作者：Zhanwei Cao、YeoJin Go、Yifan Hu 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.12097)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4997ef4fb5ba)

> 现有AI生成文本检测聚焦于静态分布差异，忽视了人类写作固有的纵向演化特性，导致合成数据在时间维度上失真。本文指出，当前LLM的实例级采样范式无法复现人类认知与情感随时间的漂移，造成“时间扁平化”。通过构建412名作者的纵向语料并对比三种LLM在实例级与历史增强条件下的轨迹，利用漂移与方差算子量化差异，揭示了LLM在语义与认知-情感维度的系统性静态化。该发现为合成数据质量评估提供了新维度，但仅验证了商业LLM在特定领域下的表现，未涉及开源模型或更复杂的交互场景。

】

---

【The Mark Fades: Adaptive Evolutionary Paraphrase-based Attack against LLM Watermarks ｜进化式改写攻击下的水印鲁棒性评估

作者：Yusheng Zhao、Jian Zhao、Tianle Zhang 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_463956bd46cf)

> 文本水印旨在通过嵌入统计信号实现机器生成内容的溯源，但现有方案在对抗改写下的生存能力存疑。主流攻击方法如SIRA依赖启发式规则或单目标优化，难以在彻底移除水印与保持文本语义完整性之间取得平衡。本文提出TSAPA，将黑盒水印去除形式化为多目标优化问题，利用遗传算法在Pareto前沿上迭代搜索最优改写策略。该方法在Qwen3系列模型上实现了高攻击成功率与高语义保真度的共存，揭示了当前主流水印机制在进化式攻击下的系统性脆弱性，但其结论受限于极小的测试样本规模。

】

---

【WaveDetect: Robust Framework for Machine-Generated Text Detection via Wavelet Transform ｜基于连续小波变换的机器生成文本检测

研究机构：南方科技大学

作者：Zhichen Liu、Kaitong Qin、Linhan He 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_695a37543776)

> 机器生成文本检测旨在区分人类写作与大语言模型（LLM）生成内容，核心挑战在于生成模型能力指数级提升导致人机文本分布边界日益模糊。现有零样本统计方法依赖困惑度等静态特征，在对抗攻击与模型演化下脆弱；监督方法虽精度高但跨域泛化差。WAVEDETECT 将 token 概率序列视为信号，通过连续小波变换（CWT）提取时频域“频谱指纹”，以 CNN 分类器实现鲁棒检测。该方法在 RAID 基准上取得 0.9785 平均 AUROC，显著优于基线，但其对语义不变攻击的鲁棒性边界尚待更严苛协议验证。

】

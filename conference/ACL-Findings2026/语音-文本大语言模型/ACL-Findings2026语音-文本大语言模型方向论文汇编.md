# ACL-Findings2026 · 语音-文本大语言模型方向论文汇编

> 本方向共 4 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Cross-lingual Matryoshka Representation Learning across Speech and Text ｜跨语言语音-文本马特罗什卡嵌入模型

研究机构：法国国家科学研究中心

作者：Yaya SY、Dioula Doucouré、Christophe Cerisara 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_245261da2162)

> 低资源口语语言（如沃洛夫语）的信息检索面临双重壁垒：内容多存储于高资源语言文本中，而用户查询以语音形式存在。传统“语音识别+翻译+检索”级联流水线因误差累积和计算开销难以落地。本文切入点在于将马特罗什卡表示学习（Matryoshka Representation Learning, MRL）扩展至跨语言语音-文本检索，通过冻结文本嵌入骨干并引入轻量级语音适配器，实现无需中间文本转写的直接检索。该工作验证了晚融合架构在低资源场景下的有效性，但其对语音质量的敏感性暴露了当前MRL压缩机制在低维表示中的信息丢失问题。

】

---

【Efficient Training for Cross-lingual Speech Language Models ｜跨语言语音语言模型的高效训练

研究机构：中国科学院、中国科学院大学

作者：Yan Zhou、Qingkai Fang、Yun Hong 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.11096)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.11096)

> 语音大语言模型（Speech LLM）面临数据稀缺与多语言扩展的双重瓶颈，现有端到端架构依赖海量平行数据，导致低资源语言难以覆盖。CSLM 抓住“跨语言对齐可经由文本模态中转”这一被忽略的结构性特征，通过持续预训练与交错模态链微调，在仅 77k 小时语音数据下实现中英双语对齐。该方法验证了数据效率的可行性，但其对齐依赖外部 CTC 模块，内生泛化能力存疑。

】

---

【Visual Interference in Speech Evaluation: Cultural Asymmetry and Cross-Modal Bias in MLLMs ｜视觉干扰下的语音评估偏见：文化不对称性审计

作者：Kyusik Kim、Hyunwoo Yoo、Jaehoon Choi 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4c2b57f5e253)

> 多模态大语言模型（MLLMs）在语音评估中常因视觉先验干扰听觉证据，导致对说话人能力的误判，现有研究多聚焦于声学鲁棒性或语义理解，忽视了视觉种族线索对语言流利度评估的系统性扭曲。本文切入点在于验证MLLMs是否继承了人类社会语言学中的文化不对称偏见，即英语环境下的反向语言刻板印象与韩语环境下的期望违背效应。通过构建视觉匹配伪装范式数据集，固定原生音频并操纵视觉种族形象，量化模型在社交评估与语言画像任务中的反事实偏差。该工作揭示了高容量闭源模型在跨模态推理中复现特定文化偏见的机制，但自建基准的生态效度与去偏策略的有效性仍存疑。

】

---

【WavAlign: Enhancing Intelligence and Expressiveness in Spoken Dialogue Models via Adaptive Hybrid Post-Training ｜WavAlign：面向语音对话模型的自适应混合后训练

研究机构：浙江大学、阿里巴巴集团

作者：Yifu Chen、Shengpeng Ji、Qian Chen 等 12 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.14932)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.14932)

> 端到端语音对话模型旨在统一语义理解与语音生成，但现有开源系统在智能（IQ）与表达力（EQ）上均存在显著短板。直接应用偏好优化（Preference Optimization）会导致声学漂移，因为文本梯度主导更新而语音梯度噪声大。本文提出单阶段自适应混合后训练框架，将偏好优化限制在文本Token，并用监督微调（SFT）锚定语音分布。该方法在多个基准上实现了IQ与EQ的同步提升，但其对弱基座模型的鲁棒性仍存疑。

】

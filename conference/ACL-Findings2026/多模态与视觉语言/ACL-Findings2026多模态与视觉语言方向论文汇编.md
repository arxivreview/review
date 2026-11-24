# ACL-Findings2026 · 多模态与视觉语言方向论文汇编

> 本方向共 143 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【A Learnable Skill Combination Strategy for Multi-task Learning in Natural Language Understanding ｜基于可学习技能组合的多任务自然语言理解框架

作者：Zhe Yang、Yi Huang、Yaqin Chen 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ea441a9160b8)

> 多任务学习（MTL）旨在通过共享表示提升数据效率并缓解单任务过拟合，但现有软参数共享方法如 MMoE 和 Skill-Net 分别存在专家负载不均衡与人工映射依赖的瓶颈。本文切入点在于将技能选择从数据驱动或人工配置转变为基于任务-技能嵌入相似度的动态可微机制。具体做法是扩展 Transformer 的 FFN 为技能簇，并通过正交约束与可微阈值函数实现端到端的稀疏技能激活。该框架在中文 NLU 基准上优于传统 MTL 基线，但其性能增益是否源于架构改进而非骨干优势，以及嵌入路由在任务分布偏移下的鲁棒性，仍存疑。

】

---

【A Picture is Worth a Thousand Words? An Empirical Study of Aggregation Strategies for Visual Financial Document Retrieval ｜视觉金融文档检索中单向量聚合的失效诊断

研究机构：香港科技大学

作者：Ho Hung Lim、Yi Yang

论文原文见 [arXiv](https://arxiv.org/abs/2605.14581)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.14581)

> 视觉检索系统面临存储与精度的权衡：多向量保留细节但开销大，单向量聚合便于部署却可能丢失关键信息。现有方法在通用文档上表现尚可，但在数值密集的金融表格中，单向量聚合是否导致语义盲区尚缺乏系统性证据。本文构建诊断基准，通过敏感性分析与注意力归因，量化了聚合过程对细粒度数值信号的抹除效应。该研究揭示了单向量范式在金融场景的根本局限，但仅停留在诊断层面，未提供可部署的修复方案。

】

---

【AdaTooler-V: Adaptive Tool-Use for Images and Videos ｜自适应工具调用多模态推理

研究机构：香港中文大学

作者：Chaoyang Wang、Kaituo Feng、Dongyang Chen 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.16918)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.16918)

> 多模态大模型在“思考图像”范式下常陷入盲目调用视觉工具的陷阱，导致推理路径偏离与计算开销激增。现有强化学习框架缺乏对工具调用必要性的显式判断机制，往往无差别地奖励工具使用行为。本文提出AT-GRPO算法，通过引入样本级的工具收益分数动态调整奖励尺度，使模型仅在有真实增益时调用工具。该机制在高分辨率视觉推理任务上显著提升了性能与效率，但其依赖离线预计算的收益分数，在动态环境下的泛化能力存疑。

】

---

【Addressing Overthinking in Large Vision-Language Models via Gated Perception-Reasoning Optimization ｜门控感知-推理优化

研究机构：美国达特茅斯学院、美国圣母大学

作者：Xingjian Diao、Zheyuan Liu、Chunhui Zhang 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.04442)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.04442)

> 大视觉语言模型（LVLM）在复杂推理任务中常陷入“过度思考”，即对简单问题生成冗长且低效的推理链，导致测试时计算资源浪费甚至准确率下降。现有自适应推理方法仅关注推理深度的动态调整，忽略了视觉感知错误这一更底层的瓶颈，导致模型在感知阶段出错后，后续推理无论多深入都无法纠正。本文提出门控感知-推理优化（Gated Perception-Reasoning Optimization, GPRO），通过一个元推理控制器在Token级动态路由至快速生成、视觉重检或逻辑反思三条路径，以解决感知与推理资源的错配问题。该框架在效率-准确率帕累托前沿上表现优异，但其绝对性能上限仍受限于骨干模型的感知能力，且缺乏对局部视觉区域的精细定位机制。

】

---

【AFMRL: Attribute-Enhanced Fine-Grained Multi-Modal Representation Learning in E-commerce ｜属性增强细粒度多模态表示学习

作者：Biao Zhang、Lixin Chen、Bin Zhang 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.20135)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_83468a9d6fdb)

> 电商场景下的商品检索要求模型区分视觉高度相似但属性细微差异的单品，传统双编码器因全局嵌入模糊了局部属性绑定而失效。现有基于多模态大语言模型（MLLM）的嵌入方法虽提升了语义理解，但受限于因果注意力机制，难以直接利用区域级细粒度信号。本文提出AFMRL框架，通过解耦“表示模型”与“属性生成器”，利用生成式属性提取解决硬负样本歧义，并引入检索感知的强化学习闭环优化。该方法在电商基准上显著优于基线，但其依赖外部生成器的架构是否牺牲了实时检索效率，仍存疑。

】

---

【AICA-Bench: Holistically Examining the Capabilities of VLMs in Affective Image Content Analysis ｜情感图像内容分析基准

研究机构：华南理工大学

作者：Dong She、Xianrong Yao、Liqun Chen 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.05900)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.05900)

> 视觉语言模型（VLM）在感知任务上表现优异，但在情感智能维度上缺乏系统性评估，现有基准多局限于静态分类，无法覆盖情感推理与生成。本文切入点在于构建涵盖理解、推理、生成三维度的全链路基准，并引入基于视觉脚手架的无训练提示框架。通过整合9个数据集与18,124条指令，该工作揭示了模型在情感强度校准上的系统性缺陷，其价值在于填补了情感评估空白，但受限于静态图像与单一语言，跨文化与时序情感能力仍存疑。

】

---

【Aligning with Your Own Voice: Self-Corrected Preference Learning for Hallucination Mitigation in LVLMs ｜基于验证自校正的偏好对齐

作者：Byeonggeuk Lim、JungMin Yun、Junehyoung Kwon 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.24395)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.24395)

> 大视觉语言模型（LVLMs）在生成描述时，常因语言先验压制视觉信号而产生对象、属性及关系幻觉。现有基于直接偏好优化（DPO）的方法依赖专有模型（如GPT-4V）构建偏好对，导致外部数据与目标模型内在分布不匹配，阻碍有效对齐。本文提出AVES-DPO，通过场景图提取与共识验证诊断幻觉，引导模型自校正生成分布内偏好对，以5.2k样本实现SOTA级幻觉抑制。该方法在数据效率上优势显著，但13B模型在通用能力上出现保守倾向，其自校正上限是否受限于初始模型能力仍存疑。

】

---

【Almieyar-Oryx-BloomBench: A Bilingual Multimodal Benchmark for Cognitively Informed Evaluation of Vision-Language Models ｜基于布鲁姆分类学的双语多模态认知评估基准

研究机构：加拿大不列颠哥伦比亚大学

作者：Mohammad Mahdi Abootorabi、Omid Ghahroodi、Anas Madkoor 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.05531)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.05531)

> 现有视觉语言模型（VLM）评估多聚焦于离散任务或单一认知维度，导致高分掩盖了模型在事实回忆与创造性合成上的深层缺陷。本文切入点在于引入认知科学框架，将多模态任务映射至布鲁姆分类学的六个层级，以诊断模型能力的非对称分布。通过构建包含英语与阿拉伯语的双语基准，并采用基于似然评分的评估机制，量化了模型置信度与准确率的背离。该工作提供了细粒度的认知画像，但受限于闭源模型无法获取内部概率分布，且阿拉伯语评估中混杂了分词器偏差，其跨语言结论的普适性存疑。

】

---

【AnalystBench: Benchmarking professional long-form report generation with web-mined multimodal tasks ｜分析师基准

作者：Chau Minh Pham、Zichao Wang、Puneet Mathur 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_742d41604e3b)

> 长文档专业报告生成面临输入规模巨大、多模态混杂且缺乏标准答案的评估困境，现有基准多依赖人工设计或单一模态，难以规模化验证模型在真实工作流中的端到端能力。AnalystBench通过反向工程从网络专业报告中自动构建任务，解决了数据获取与评估一致性的矛盾。其核心在于利用自动化工具生成可复用的任务变体，并引入基于检查表的专家验证评估协议。该基准揭示了当前大模型在长程综合任务上的显著性能断层，但评估指标对主观写作质量的覆盖仍显不足。

】

---

【Assessing Y-Axis Influence: Bias in Multimodal Language Models on Chart-to-Table Translation ｜Y轴偏差控制与视觉显著误差度量

研究机构：美国爱荷华州立大学

作者：Seok Hwan Song、Azher Ahmed Efat、Wallapak Tavanapong

论文原文见 [arXiv](https://arxiv.org/abs/2604.24987)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.24987)

> 图表到表格翻译任务中，多模态大语言模型（MLM）的性能受Y轴信息分布不均的隐性干扰，导致模型在特定刻度格式或数值范围下出现系统性偏差。现有基准如PlotQA和ChartQA存在严重的数字长度分布失衡，且传统评估指标无法区分视觉上显著的误差与微小波动，使得偏差难以被量化和归因。本文通过构建控制变量的FairChart2Table基准集，并引入基于刻度间隔的误差度量，系统揭示了Y轴特征对模型提取精度的影响。该工作填补了细粒度偏差评估的空白，但其结论局限于合成数据环境，未验证在真实噪声图表中的泛化性。

】

---

【Asymmetric Relational-Geometry Driven Universal Adversarial Perturbations for Vision-Language Models ｜非对称关系几何驱动的通用对抗扰动

研究机构：中国科学技术大学、北京大学

作者：Jiaxin Ye、Weihai Li、Ying Wang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_5dbf85fd0970)

> 视觉语言模型（VLP）在跨模态对齐中暴露出对微小扰动的敏感性，但现有通用对抗扰动（UAP）方法因采用对称目标函数，忽视了图像与文本模态在嵌入空间中的非对称几何角色，导致黑盒迁移性受限。本文指出，对称假设隐含了模态间语义行为一致的错误前提，这是迁移失效的根源。通过引入非对称关系几何目标，解耦几何退化与关系破坏，并辅以自适应梯度聚合，本文实现了高效且高迁移性的多模态UAP生成。该方法在效率上显著优于生成器基线，但黑盒迁移峰值略低于实例特定攻击SOTA，其理论贡献在于揭示了模态非对称性对攻击泛化的关键作用。

】

---

【AutoRubric: Rubric-Based Generative Rewards for Faithful Multimodal Reasoning ｜基于自动评分标准的忠实多模态推理

作者：Mengzhao Jia、Zhihan Zhang、Ignacio Cases 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0070e9c7e4c6)

> 多模态大模型在强化学习可验证奖励（RLVR）训练中常出现“答案正确但逻辑断裂”的虚假推理现象，现有过程奖励模型（PRM）因依赖人工标注或更强教师模型而难以扩展。本文切入点在于利用模型自身成功轨迹的自聚合特性，自动生成问题特定的推理检查点（Rubrics），替代传统PRM提供细粒度过程监督。该方法通过LLM-as-a-Judge验证轨迹与Rubrics的匹配度，结合结果奖励优化策略，在六个基准上提升了推理忠实度。其价值在于解决了过程监督的数据瓶颈，但引入了额外的计算开销且未完全消除视觉感知层面的偏差。

】

---

【Benchmarking the Fine-Grained Discriminability in Image-Text Retrieval via Controlled Contrastive Differences ｜受控对比差异基准

研究机构：中国科学院、中国科学院大学

作者：Zhen Wang、Xi Zhou、Yating Yang 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d19c809b4845)

> 多模态检索模型在常规基准上表现优异，却常检索到细节不一致的样本，暴露出全局嵌入对细微语义差异的钝感。现有评测仅关注整体相似度，无法量化模型对单一变量变化的判别力，导致细粒度能力被高估。本文通过构建仅存在一处受控差异的对比样本对，并定义细粒度对比判别准确率（FG-CDA），系统性地暴露了当前SOTA模型在实体情感、场景属性等细微特征上的判别短板。该基准为细粒度检索提供了必要的评估坐标，但其受控构造方式是否完全模拟真实长尾分布，仍存疑。

】

---

【Beyond Cross-Modal Alignment: Measuring and Leveraging Modality Gap in Vision-Language Models ｜模态主导性评分与无训练干预

研究机构：英国牛津大学、美国麻省理工学院

作者：Hanqi Yan、Xiangxiang Cui、Lu Yin 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d343647e20f7)

> 视觉语言模型（VLMs）长期面临模态特异性信息被全局对齐掩盖的问题，导致无法对单一模态特征进行独立控制。现有几何修正方法如子空间投影旨在消除模态间隙，却忽视了间隙中蕴含的功能性分化潜力。本文提出模态主导性评分（MDS）量化维度级模态归属，并基于此实现无训练的行为干预。该方法将模态间隙从“缺陷”重构为“资源”，但在复杂推理任务中的普适性尚未得到验证。

】

---

【Beyond Modality Collapse: Taming Guided Modality Entropy for Omni-modal Emotion Reasoning ｜全模态情感推理中的模态熵校准

研究机构：北京交通大学

作者：Xian Zhao、Rui Hu、Yuxiang Zhang 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_dc7680c7fead)

> 全模态大语言模型在处理情感推理时，常因过度依赖视觉模态而忽略音频与文本线索，导致推理链逻辑断裂。现有监督微调方法仅能实现域适应，无法解决跨模态证据整合中的动态依赖问题。本文通过构建引导式思维链数据并引入基于模态熵的动态强化学习奖励，迫使模型在不确定时主动探索多模态证据。该方法在多个情感基准上刷新了性能上限，但其对连续模态特征的适用性及计算开销仍存疑。

】

---

【Beyond Polarity: Continuous Affect-Enhanced Multimodal Aspect-Based Sentiment Classification ｜连续情感增强的多模态方面级情感分类

研究机构：北京理工大学

作者：Ling-Ang Meng、Tianyu Zhao、Dawei Song 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b0c5e7d97b84)

> 多模态方面级情感分类（MABSC）旨在从图文数据中预测特定方面词的情感极性，但现有方法多依赖离散极性模式与通用视觉嵌入，难以捕捉隐式或细微的情感表达。本文切入点在于将连续效价-唤醒度-支配度（VAD）信号引入方面级推理，并通过构建情感增强数据集微调视觉编码器以获取情感敏感表示。具体做法是设计VAD编码器提取文本连续情感向量，利用FiLM调制机制注入文本特征，并在Senti-COCO数据集上微调CLIP图像编码器。该框架在Twitter-15和Twitter-17上取得了SOTA结果，但其对VAD弱监督标签噪声的敏感性以及未涉及复杂推理场景的局限性，使其在应对高歧义情感时仍存疑。

】

---

【Beyond Single Plots: A Benchmark for Question Answering on Multi-Charts ｜多图表问答基准与视觉分解验证管线

研究机构：美国爱荷华州立大学

作者：Azher Ahmed Efat、Seok Hwan Song、Wallapak Tavanapong

论文原文见 [arXiv](https://arxiv.org/abs/2604.21344)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.21344)

> 多模态大语言模型（MLLMs）在单图表理解上已趋于成熟，但在真实科研场景中常见的多子图复合图像上，模型因缺乏显式定位指引而性能骤降。现有基准如MultiChartQA依赖“第一张图”等显式引用，掩盖了模型在自然语境下自主定位子图的能力缺陷。本文构建了无显式引用的真实多图表基准PolyChartQA，并提出视觉分解与自验证（VDSP）提示管线，通过结构化拆解推理过程提升模型在复杂多图场景下的准确率与可解释性。该工作填补了多图评测的空白，但仅依赖提示工程，未触及模型底层视觉编码机制的局限。

】

---

【Bidirectional Semantic Enhancement for Schema Routing Across Large-Scale Databases ｜双向语义路由

作者：Yuyang Wu、Xiaoliang Wang、Cam-Tu Nguyen

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0ebc0b5ce2d2)

> 大规模数据库场景下，用户查询与模糊表结构间的语义鸿沟导致传统检索失效，现有单向扩展或图遍历方法难以兼顾召回率与计算效率。Bi-SR 通过离线丰富表结构语义与在线推理查询意图的双向对齐策略，构建共享语义空间以解决这一瓶颈。该方法利用双增强对比训练目标优化稠密检索器，使其模仿大语言模型的语义扩展模式。尽管在噪声环境下展现出鲁棒性，但其对大模型推理能力的依赖及小模型适配性仍存疑。

】

---

【Bridging the Temporal Gap in Multimodal LLMs: Deeply Stacking Temporal Tokens for Audio-Visual Speech Recognition ｜弥合多模态大语言模型中的时序鸿沟：深层堆叠时序令牌用于视听语音识别

研究机构：北京科技大学、清华大学

作者：Liyong Wang、Junliang Xing、Tianyu Hu 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9d8825c79ba5)

> 视听语音识别（AVSR）旨在利用唇部运动等视觉线索补偿噪声环境下的音频退化，但当前基于多模态大语言模型（MLLMs）的方法存在根本性的时序鸿沟：视觉编码器缺乏细粒度时序建模，且时序语义在LLM深层解码器中逐步退化。本文指出这一被忽视的缺陷，通过在视觉编码器引入时序感知注意力（TAA）与T-RoPE，并在LLM解码器早期层堆叠层级化时序令牌（HSTT），在LRS2和LRS3基准上实现了显著的性能提升。该方法在LLM-based AVSR中处于第一梯队，但其对深层语义推理的时序贡献及与稀疏对齐策略的优劣对比仍存疑。

】

---

【CAIR: Causal Adaptive Information-based Reinforcement Learning for Multimodal Emotion Reasoning ｜因果中介强化学习

研究机构：中国科学院、中国科学院大学

作者：Fengyu Zhang、Bin Liu、Jianhua Tao 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_cfa90365ba53)

> 多模态情感推理旨在从视频、音频与文本中不仅识别情绪标签，更需解释情绪产生的因果触发机制。现有监督微调方法常陷入“因果退化”，即生成流畅但缺乏逻辑推导的表面描述，而传统强化学习仅优化答案正确性，无法约束推理链的因果有效性。CAIR 将推理链重构为决策过程中的因果中介，通过量化其对预测熵的降低程度来设计奖励信号，并引入认知负载自适应优化机制以平衡不同复杂度任务的训练权重。该方法在MTMEUR基准上取得了73.80%的准确率，显著提升了推理的因果忠实性，但其泛化能力至非情感类通用推理任务尚存疑问。

】

---

【Can MLLMs Reason Beyond Language? VisReason: A Comprehensive Benchmark for Vision-Centric Reasoning ｜视觉中心推理基准

研究机构：中国科学院、中国科学院大学

作者：Longteng Guo、Yifan Wang、Pengkang Huo 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.25364)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.25364)

> 多模态大语言模型在现有视觉推理基准上的高分表现，掩盖了其依赖语言中介而非直接视觉证据推理的事实。现有基准允许模型通过文本描述抽象视觉信息，导致评估失效。本文通过构建强制依赖直接视觉输入的VisReason基准，量化了语言捷径对评估的干扰。该基准揭示了当前模型在视觉接地上的根本缺陷，但其诊断能力受限于未覆盖潜在推理等新兴方法。

】

---

【CAPA: Contribution-Aware Pruning and FFN Approximation for Efficient Large Vision-Language Models ｜贡献感知剪枝与FFN近似

研究机构：印度理工学院、美国伊利诺伊大学厄巴纳-香槟分校

作者：Samyak Jha、Junho Kim

论文原文见 [arXiv](https://arxiv.org/abs/2602.00247)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.00247)

> 视觉语言模型（VLMs）推理瓶颈源于高分辨率输入导致的视觉Token激增，现有剪枝方法依赖注意力分数却忽略Value向量幅度，导致误删关键语义信息。CAPA通过引入“注意力贡献度”指标替代原始注意力分数进行Token选择，并针对视觉Token在中间层FFN中表现出的线性冗余，采用Hadamard积近似替代密集FFN计算。该双策略框架在保持任务性能的同时实现了78%的FLOPs减少，但其FFN近似依赖特定骨干的线性冗余特性，跨模型泛化能力存疑。

】

---

【CaTS-Bench: Can Language Models Describe Time Series? ｜时序描述基准

研究机构：意大利罗马第一大学

作者：Luca Zhou、Pratham Yashwante、Marshall Fisher 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.20823)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.20823)

> 时序描述生成（Time Series Captioning, TSC）旨在将原始数值序列转化为人类可读的自然语言摘要，以辅助金融、医疗等领域的快速决策。现有基准多依赖模板化合成数据，缺乏真实语境与视觉模态，导致模型评估无法反映实际场景下的数值幻觉与语义偏差。本文构建了包含1746个人工重写金标准样本的多模态基准，并验证了基于合成数据微调开源视觉语言模型（VLM）的有效性。该工作填补了生成式时序评估的空白，但暴露了当前VLM在视觉结构理解上的系统性失效。

】

---

【CCD: Mitigating Hallucinations in Radiology MLLMs via Clinical Contrastive Decoding ｜临床对比解码

研究机构：英国格拉斯哥大学

作者：Xi Zhang、Zaiqiao Meng、Jake Lever 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.23379)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.23379)

> 放射学多模态大语言模型在生成报告时，常因过度依赖提示中的临床文本而忽略图像证据，导致“临床幻觉”。现有通用对比解码方法在灰度医学影像上失效，且训练时干预面临隐私与算力瓶颈。CCD通过引入外部专家模型，在推理阶段以结构化标签和置信度分数双路校准Logits，实现免训练的幻觉抑制。该方法在MIMIC-CXR上显著提升了临床指标，但其对特定专家模型的依赖限制了跨模态泛化能力。

】

---

【Chain-of-Procedure: Hierarchical Visual-Language Reasoning for Procedural QA ｜视觉程序问答中的粒度对齐与层级推理

研究机构：澳门大学

作者：Guanhua Chen、Yutong Yao、Shenghe Sun 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4517046165a8)

> 视觉程序问答（VP-QA）要求模型根据中间状态图像预测复杂任务的下一步操作，但现有视觉语言模型（VLMs）在处理静态快照时，常因文本步骤的粗粒度与视觉证据的细粒度不匹配而失效。本文指出，直接对齐导致模型无法识别隐含的原子动作，从而在跨程序检索与状态定位上表现不佳。为此，论文构建了ProcedureVQA基准，并提出链式程序（Chain-of-Procedure, CoP）框架，通过检索、分解与预测三阶段解耦推理过程。该工作揭示了VLMs在因果推理上的短板，但其在非结构化任务上的泛化能力仍存疑。

】

---

【Coarse-to-Fine Multimodal Information Selection for Video Speaking Style Recognition with Large Language Models ｜视频说话风格识别中的多模态信息选择

作者：Beibei Zhang、Yanan Lu、Lin Fen 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1205858ff800)

> 视频说话风格识别（Video Speaking Style Recognition, VSSR）旨在从对话视频中区分威胁、解释等细粒度交互类型，其核心难点在于视觉模态的高冗余性常掩盖文本中的关键语义线索。现有基于大语言模型（LLM）的免训练方法直接融合所有多模态信息，导致视觉噪声干扰推理，性能受限。CFMiS 提出一种从粗到细的动态选择框架，先通过文本主导的模态筛选确定必要模态，再迭代精炼视觉线索以增强 LLM 推理。该方法在 LVU-VSSR 数据集上显著优于现有免训练基线，但其对 ASR 与视觉描述模型质量的依赖，以及仅针对特定任务的设计，限制了其通用性。

】

---

【CodeBind: Decoupled Representation Learning for Multimodal Alignment with Unified Compositional Codebook ｜基于组合式码本的多模态解耦对齐

作者：Zeyu Chen、Jie Li、Kai Han

论文原文见 [arXiv](https://arxiv.org/abs/2605.18257)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.18257)

> 多模态对齐旨在将异构数据映射至共享空间以支持跨模态推理，但传统硬对齐常因模态间隙与数据不平衡导致“最小公分母”效应，丢失模态独有特征。CodeBind 通过解耦共享与特有表示，并引入组合式向量量化（Compositional VQ）构建统一码本，在保留细粒度信息的同时实现高效对齐。该方法在九种模态上验证了有效性，但其离散量化对连续高频细节的保留能力及大规模预训练下的泛化边界尚存疑。

】

---

【CoGR-MoE: Concept-Guided Expert Routing with Consistent Selection and Flexible Reasoning for Visual Question Answering ｜概念引导专家路由与选项感知重加权

研究机构：香港科技大学

作者：Xiyin Zeng、Yi Lu、Hao Wang

论文原文见 [arXiv](https://arxiv.org/abs/2604.16930)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.16930)

> 视觉问答（VQA）中混合专家（MoE）架构面临路由稳定性与选项区分灵活性的内在矛盾：稳定路由导致专家固化，削弱细粒度判别；不稳定路由则引发同类问题专家选择漂移。现有方法多从嵌入空间或交互特征入手，未能解耦“选谁”与“怎么用”两个环节。CoGR-MoE 通过 LLM 生成正负语义线索，将正确答案的语义方向注入路由层以稳定 Top-K 专家选择，再利用各选项自身线索对共享专家输出进行动态重加权，生成选项特定表示。该方法在 MRAG-Bench 上取得 63.25% 准确率，较最强基线 MoME 提升 0.49%，但在 Others 子集上仍落后于交互驱动路由方法，其语义引导策略对复杂跨模态交互的覆盖能力存疑。

】

---

【Collaborative Multi-Agent Scripts Generation for Enhancing Imperfect-Information Reasoning in Murder Mystery Games ｜多智能体协作脚本生成与不完全信息推理增强

研究机构：中山大学、香港中文大学

作者：Keyang Zhong、Junlin Xie、Hefeng Wu 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.11741)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.11741)

> 多模态大模型在涉及欺骗、多跳推断及动态社会交互的复杂博弈场景中，因缺乏大规模高质量训练数据而表现退化。现有单智能体推理优化方法无法覆盖多玩家不完全信息下的策略性行为建模，本文切入点在于构建多智能体协作框架以自动化合成包含视觉与文本线索的博弈剧本。通过两阶段训练策略，结合监督微调与基于智能体监控的强化学习，提升视觉语言模型在角色一致性与证据整合上的推理能力。该方法在WhodunitBench基准上显著优于开源基线，但其评估依赖主观性较强的LLM-as-Judge机制，且未验证在通用数学推理任务上的泛化性。

】

---

【ComicVQA: A Benchmark for Visual Reasoning in Multimodal LLMs ｜漫画视觉问答基准

研究机构：新加坡国立大学、捷克布拉格捷克理工大学

作者：Esther Gan、Hannah Brown、David Herel 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c2baab84154c)

> 多模态大语言模型（MLLMs）在单图视觉问答中常依赖语言先验而非真实视觉接地，且缺乏对离散静态图像序列的时序推理能力。现有漫画基准往往将视觉感知与叙事逻辑纠缠，无法诊断模型失败源于感知缺陷还是推理断裂。本文构建ComicVQA，通过去除文本的缺失面板预测和面板排序双任务，解耦细粒度视觉接地与组合时序推理。该基准揭示了当前MLLMs在局部因果推理上的显著短板，但受限于自动分割噪声与单一分辨率设置，其诊断结论的普适性仍需进一步验证。

】

---

【CompassLLM: A Multi-Agent Approach toward Geo-Spatial Reasoning for Popular Path Query ｜多智能体协同路径查询框架

研究机构：澳大利亚莫纳什大学

作者：Md. Nazmul Islam Ananto、Shamit Fatin、Mohammed Eunus Ali 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.07516)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.07516)

> 地理空间路径推荐旨在从历史轨迹中推断两点间最常被使用的路线，但传统机器学习模型在数据更新时需重训练，而通用大语言模型（LLM）直接生成路径常出现不可遍历的幻觉。本文切入点在于将路径查询解耦为“检索”与“合成”两个条件阶段，通过多智能体协同编排，在无需重训练的前提下处理稀疏数据下的路径缺失问题。该方法利用LLM的图结构推理能力，在检索任务上超越基线，在合成任务上达到与专用深度学习模型相当的可行性，但其性能仍受限于LLM上下文窗口与随机性。

】

---

【ConSensus: Multi-Agent Collaboration for Multimodal Sensing ｜多智能体协同下的传感器融合仲裁

研究机构：韩国科学技术院、诺基亚贝尔实验室

作者：Hyungjun Yoon、Mohammad Malekzadeh、Sung-Ju Lee 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.06453)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.06453)

> 异构传感器数据在单一大型语言模型（LLM）中常因上下文过载与模态主导导致推理断裂，且语义聚合易受先验知识偏见影响，而统计投票在传感器缺失时又易失效。现有方案要么依赖昂贵的多轮辩论，要么缺乏对语义与统计冲突的显式仲裁。ConSensus 提出一种免训练的多智能体框架，通过模态特化智能体与混合融合机制，在单轮内平衡语义推理与统计共识。该框架在五个基准上平均提升 7.1% 准确率，并将融合 token 成本降低 12.7 倍，但其鲁棒性边界在传感器严重缺失时仍存疑。

】

---

【CORES: Code-Oriented Reasoning for Complex Text-to-SQL and Generalizable TableQA ｜代码导向推理的SQL生成与表格问答泛化

研究机构：国防科技大学、北京大学

作者：Meng Zhang、Ruochun Jin、Yuanxi Peng 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_de89c16574d8)

> 文本到SQL（Text-to-SQL）旨在将自然语言映射为可执行查询，但现有SQL微调模型在处理复杂逻辑时缺乏显式推理过程，且在表格问答（TableQA）任务上出现灾难性遗忘。本文指出SQL的声明式本质无法承载程序化逻辑，且单一任务微调导致通用代码能力丧失。CORES模型利用Python作为程序化推理枢纽，结合组相对策略优化（GRPO）与过程奖励函数进行训练，在提升复杂SQL生成准确率的同时，恢复了模型对TableQA的泛化能力。该框架在平衡领域特异性与通用推理能力上提供了新路径，但其性能上限仍受限于骨干模型规模与推理延迟。

】

---

【CrisPrune: Combining Contextual Relevance and Intrinsic Saliency for Efficient Visual Token Pruning in MLLMs ｜CrisPrune：融合内在显著性与双源文本相关性的视觉Token剪枝

作者：Ziniu Liu、Shuheng Zhou、Mingqing Liu 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c3fde539d866)

> 视觉语言模型处理高分辨率图像时，视觉Token数量激增导致二次方注意力计算成本成为部署瓶颈。现有剪枝方法面临两难：纯视觉方法受注意力汇聚现象干扰且忽略任务语义，纯文本引导方法则因过度聚焦指令而丢失背景上下文。CrisPrune通过鲁棒归一化修复视觉显著性计算，并引入通用语义先验与指令对齐的双源文本相关性，结合行列式点过程（Determinantal Point Process, DPP）实现质量与多样性的平衡选择。该方法在极端压缩率下显著优于现有Training-free方法，但其对特定架构的依赖性及视频场景的适用性仍存疑。

】

---

【CTRL: Control-Based Time Series Forecasting with LLM-Guided Residual Learning ｜基于LLM控制信号的时序预测框架

研究机构：韩国延世大学

作者：Minkyoung Kim、Daeun Ji、Yohan Lee 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b09bf6da9a7a)

> 导读 多模态时序预测旨在融合外部语义信息以提升非平稳场景下的鲁棒性，但现有方法常将大语言模型（LLM）降级为数值预测器，导致精度受损或预测不稳定。CTRL框架的核心切入点在于解耦语义推理与数值计算，将冻结的LLM定位为战略控制器而非直接预测器。该框架通过LLM分析骨干网络误差并生成紧凑控制信号，驱动轻量级残差解码器进行修正，同时引入无标签测试时适应机制以应对分布偏移。这一设计在显著降低LLM调用开销的同时提升了非平稳序列的预测精度，但其对平稳数据集的增益有限，且依赖特定骨干网络的误差特征。

】

---

【DANCE: Diversity-attended Dynamic Caching with Asymmetric Quantization for Test-time Adaptation of Vision-Language Models ｜多样性感知动态缓存与非对称量化测试时适应

研究机构：北京大学

作者：Shunge Zou、Changhu Wang、Wei Ju 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4dee2167eda1)

> 视觉语言模型在分布偏移下的零样本性能退化，传统测试时适应方法依赖熵最小化筛选高置信样本，导致缓存覆盖度不足且检索不稳定。DANCE 通过引入“可靠性-新颖度”双门控机制维护动态缓存，并采用非对称量化（Asymmetric Quantization, AQ）作为统一检索原语，解决了流式数据下的原型漂移问题。该方法在跨域泛化任务上显著优于现有缓存基线，但其理论保证仅覆盖二元分类场景，且未与最新提示调优SOTA进行直接对比。

】

---

【DEAR: Distributional Error-Aware Reliability for Robust Multimodal Sentiment Analysis with Missing Modalities ｜分布误差感知可靠性框架

研究机构：华中科技大学

作者：Shihao Zou、Wei Wei、Yongshuo Zhang

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_3f1e1a3ad750)

> 多模态情感分析（Multimodal Sentiment Analysis, MSA）在模态缺失时性能骤降，根源并非单纯信息丢失，而是重构特征偏离原始分布流形导致的语义漂移。现有方法多依赖逐点匹配损失或固定融合规则，无法感知样本级不确定性，导致高缺失率下决策崩溃。DEAR 通过层级分布约束重构修复流形，并引入样本级不确定性估计驱动双流动态仲裁，实现从激进协同到保守回退的自适应切换。该方法在 MOSI 和 MOSEI 数据集的 F1 与相关性指标上优于主流基线，但其对随机缺失的依赖及未报告的计算开销限制了其在系统性缺失场景下的适用性。

】

---

【DentalGPT: Incentivizing Multimodal Reasoning in Dentistry ｜牙科多模态推理激励：从对齐到强化

研究机构：香港中文大学、北京大学

作者：Zhenyang Cai、Jiaming Zhang、Junjie Zhao 等 18 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f4d01e182ce1)

> 牙科影像诊断依赖对细微病灶线索的精准感知与逻辑推导，但通用多模态大语言模型（Multimodal Large Language Models, MLLMs）在此垂直领域表现疲软，且复杂推理模式带来的增益远低于其他医学场景。现有方案受限于牙科专用视觉-文本对齐数据匮乏及领域强化学习缺失，导致模型无法有效探索牙科问题的解空间。本文通过构建超12万张牙科图像的多模态对齐数据集，并结合基于可验证奖励的强化学习（Reinforcement Learning with Verifiable Rewards, RLVR），在7B参数规模下实现了牙科诊断推理能力的显著提升。该工作验证了“对齐先行、强化跟进”范式在垂直领域的有效性，但其对通用推理能力的潜在侵蚀及小样本基准的统计稳定性仍存疑。

】

---

【DICA: Dual-Indicator Guided Contrastive Alignment in Multimodal Large Language Models ｜双指标引导对比对齐

作者：Hao Yang、Jin Wang、Xuejie Zhang

论文原文见 [arXiv](https://arxiv.org/abs/2607.23944)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2607.23944)

> 多模态大语言模型在视觉问答中常因注意力漂移或视觉证据利用不足产生幻觉，现有免训练方法往往采用统一的概率抑制策略，缺乏对具体失效模式的诊断能力。DICA通过引入视觉注意力熵与输出-图像相关性两个动态指标，在推理过程中实时监测并触发针对性的隐藏状态校正。该方法无需重训练即可在多个基准上提升准确率并降低幻觉率。其核心贡献在于将幻觉缓解从“统一修正”细化为“分型干预”，但阈值设定的跨架构泛化性及长序列下的指标稳定性仍存疑。

】

---

【Directional Reasoning Injection for Fine-Tuning MLLMs ｜方向性推理注入

研究机构：美国罗切斯特大学

作者：Chao Huang、Zeliang Zhang、Jiang Liu 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.15050)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.15050)

> 多模态大语言模型（MLLMs）普遍存在“感知强、推理弱”的断层，即能准确识别图像内容却难以构建连贯的逻辑推导链。现有主流方案依赖大规模多模态思维链（CoT）数据微调或强化学习，面临数据成本高与训练不稳定的双重瓶颈；参数空间合并虽看似轻量，但在模型分布差异大时极易导致性能退化。DRIFT 提出在梯度空间注入推理先验，通过预计算文本专家与多模态模型的参数差向量引导反向传播，以极低成本实现推理能力迁移。该方法在数据效率上显著优于传统范式，但在绝对性能上仍低于高资源投入的 SOTA 模型，其泛化边界尚需更多验证。

】

---

【Distorted or Fabricated? A Survey on Hallucination in Video LLMs ｜视频大语言模型幻觉的机制驱动分类与缓解

研究机构：美国东北大学

作者：Yiyang Huang、Yitian Zhang、Yizhou Wang 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.12944)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.12944)

> 视频大语言模型（Video Large Language Models, Vid-LLMs）在处理时序输入时，常因静态视觉编码器的局限与语言先验的干扰，生成看似连贯但违背视频实际内容的描述。现有图像幻觉缓解策略难以直接迁移至视频场景，因为视频引入了因果推理、运动动态及音画整合等维度，导致静态指标失效。本文提出了一种基于机制的视频幻觉分类体系，将幻觉划分为动态失真与内容捏造两大类，并系统梳理了针对各子类的评估基准与干预策略。该工作填补了视频幻觉研究的结构性空白，但其分类边界在复杂多模态场景下的鲁棒性仍存疑。

】

---

【Do Image-Text Metrics Respect Semantic Invariances? ｜无参考图像-文本评估器的语义不变性审计

作者：Amit Agarwal、Hitesh Laxmichand Patel、Meizhu Liu 等 12 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.24702)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.24702)

> 无参考图像-文本评估器在模型选择与奖励塑造中占据核心地位，但其对语义无关扰动的敏感性长期缺乏系统性量化。现有研究多关注指标与人类判断的聚合相关性，却忽视了这种相关性可能掩盖指标在空间翻转、对象尺度或社会语言学框架下的系统性偏差。本文提出一种评估中心的语义不变性审计框架，通过受控扰动测试五种主流评估器的稳定性，并引入排名翻转风险（RRF）量化其对模型排名的实际影响。该工作揭示了当前SOTA指标在鲁棒性上的显著缺陷，但受限于模板化字幕与单一对象场景，其结论向自然语言场景的泛化能力仍需验证。

】

---

【Do MLLMs Understand Pointing? Benchmarking and Enhancing Referential Reasoning in Egocentric Vision ｜第一人称指代消解与空间推理基准

研究机构：清华大学

作者：Chentao Li、Zirui Gao、Mingze Gao 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.21461)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.21461)

> 第一人称智能助手需从模糊指令中精准定位用户所指对象，但现有多模态大语言模型常因依赖视觉邻近性而非几何指向性产生“指代幻觉”。本文指出这一失效源于缺乏第一人称手势-目标几何对齐的高质量监督数据，并构建了包含仿真与真实场景的 EgoPoint-Bench 基准。通过物理驱动的仿真数据生成管线与 LoRA 微调，验证了合成数据在跨域泛化中的有效性。该工作填补了第一人称指代消解的评测空白，但其对动态手势序列及复杂遮挡场景的覆盖仍显不足。

】

---

【Do VLMs Have a Moral Backbone? A Study on the Fragile Morality of Vision-Language Models ｜视觉-语言模型道德鲁棒性诊断

研究机构：美国伊利诺伊大学厄巴纳-香槟分校

作者：Zhining Liu、Tianyi Wang、Xiao Lin 等 12 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.17082)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.17082)

> 视觉-语言模型在静态基准上表现良好的道德对齐，往往在真实部署的对抗扰动下迅速失效，现有评估仅关注干净输入下的准确率，无法反映决策边界的稳定性。本文切入点在于将道德判断视为一个需要抵抗多模态扰动的鲁棒性问题，而非单纯的分类任务。通过设计五类模型无关的文本与视觉扰动，系统测量23个主流模型的判断翻转率，并评估推理时干预的恢复能力。该研究揭示了当前模型道德立场的脆弱性及规模扩张带来的谄媚性风险，但缺乏对内部机制的因果归因，且防御策略效果有限。

】

---

【e5-omni: Explicit Cross-modal Alignment for Omni-modal Embeddings ｜全模态显式对齐框架

研究机构：中国人民大学、日本早稻田大学

作者：Haonan Chen、Sicheng Gao、Radu Timofte 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.03666)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.03666)

> 全模态检索旨在将文本、图像、音频、视频等异构数据映射至统一空间以支持跨模态匹配，但现有方法多依赖视觉语言模型（Vision-Language Model, VLM）预训练带来的隐式对齐，导致混合模态批次中相似度尺度失衡与几何分布漂移。本文提出 e5-omni，一种轻量级显式对齐框架，通过模态感知温度校准、可控负样本课程与批次白化协方差对齐，在不修改骨干网络的前提下修正对比学习中的梯度失衡与二阶统计量不匹配。该框架在 MMEB-V2 与 AudioCaps 上取得一致增益，验证了显式几何校准对全模态嵌入的必要性，但其对纯文本任务性能的影响及音频/视频时序几何特性的处理仍存疑。

】

---

【ECHA: Jailbreaking LVLMs via the Mismatch between Implicit Semantic Reconstruction and Explicit Safety Alignment ｜表情链提示攻击

作者：Chenxing Xu、Junyong Jiang、Zehu Zhang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_26c5868ab4ff)

> 多模态大语言模型（Large Vision-Language Models, LVLMs）的安全对齐机制存在结构性盲区，现有防御主要依赖对显式文本模式的表面级过滤，无法拦截模型内部从碎片化视觉线索中重构出的隐式恶意语义。本文指出这种“隐式语义重构”与“显式安全对齐”之间的失配是核心漏洞，并提出表情链提示攻击（Emoji Chain Hinting Attack, ECHA）。该框架通过将敏感概念解耦为表情符号链与文本掩码，利用良性场景框架引导模型在潜空间内完成恶意意图的自重构，从而绕过护栏。ECHA在7个SOTA模型上实现了超过81%的单次攻击成功率，但其效果高度依赖模型自身的推理深度，且对闭源模型的评估受限于专用安全评估器的判定标准。

】

---

【EDU-CIRCUIT-HW: Evaluating Multimodal Large Language Models on Real-World University-Level STEM Student Handwritten Solutions ｜大学级STEM手写解题评估基准

研究机构：美国弗吉尼亚理工大学

作者：Weiyu Sun、Liangliang Chen、Yongnuo Cai 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.00095)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.00095)

> 多模态大语言模型（MLLM）在低利害日常视觉任务中表现优异，但面对包含复杂公式、手绘图表与交织逻辑的大学级STEM手写解题时，其视觉感知可靠性面临严峻挑战。现有教育评估基准多聚焦孤立元素或低难度K-12场景，且仅通过下游自动评分结果间接评估，掩盖了上游识别错误对高精度评分的级联破坏。本文构建EDU-CIRCUIT-HW基准，通过专家验证的逐字转录与细粒度错误分类，量化识别错误对自动评分的级联影响。该工作揭示了当前MLLM在手写STEM理解上的深层缺陷，但受限于单一课程领域与特定评分标准，其结论向其他STEM学科泛化的能力尚待验证。

】

---

【EmoMM: Benchmarking and Steering MLLM for Multimodal Emotion Recognition under Conflict and Missingness ｜多模态情感识别中的模态冲突诊断与注意力引导

研究机构：华南理工大学

作者：Yueru Sun、Yimeng Zhang、Haoyu Gu 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.01024)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.01024)

> 导读 多模态情感识别（MER）旨在通过联合建模文本、视觉与声学信号推断人类情感，但真实场景中模态证据常出现矛盾或缺失，导致模型决策漂移。现有方法多停留在描述性评估，缺乏对内部决策机制的量化诊断，且难以在推理阶段动态纠正模态偏好。本文提出EmoMM基准与CHASE机制，通过Shapley值量化模态贡献，并在推理时进行头级注意力引导以重分配证据权重。该工作揭示了视频贡献崩塌现象，但其在通用MLLM任务上的泛化能力及长期时序情感场景下的有效性仍存疑。

】

---

【Empowering Reliable Visual-Centric Instruction Following in MLLMs ｜视觉中心指令遵循评估与数据构建

研究机构：香港科技大学、美国宾夕法尼亚大学

作者：Weilei He、Feng Ju、Zhiyuan Fan 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.03198)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.03198)

> 多模态大语言模型（MLLMs）在指令遵循任务中常依赖文本先验而非视觉证据，导致评估分数虚高且无法反映真实视觉理解能力。现有基准如MM-IFEval仅评估文本模式匹配，忽视了图像中隐含的空间与属性约束，使得模型即使忽略视觉输入也能通过测试。本文通过构建视觉中心的数据集与混合评估协议，将视觉约束显式纳入指令遵循的度量体系。该工作填补了视觉指令遵循评估的空白，但其7B模型实验规模与单一裁判模型依赖限制了结论的普适性。

】

---

【Enhancing Zero-Shot Time Series Forecasting in Off-the-Shelf LLMs via Noise Injection Prompting ｜噪声注入增强的大语言模型零样本时序预测

作者：Xingyou Yin、Ceyao Zhang、Min Hu 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4115ac1063ff)

> 现有基于大语言模型（LLM）的时序预测方法多依赖微调或复杂适配器以弥合数值与文本的模态鸿沟，但完全冻结的“开箱即用”LLM在面对分布偏移时表现出严重的输入脆弱性。NLTS通过一种非侵入式的推理时策略，在原始时序数据分词前注入受控随机噪声，迫使模型依赖底层时间结构而非表面数值特征进行预测。该方法无需任何参数更新或额外训练，理论上证明了噪声注入能降低泛化误差，并在多个基准上显著优于传统基线。尽管其提升了零样本预测的鲁棒性，但噪声强度的选择依赖验证集调参，且未解决LLM对复杂因果关系的深层理解缺失。

】

---

【Evaluating Perspectival Biases in Cross-Modal Retrieval ｜跨模态检索中的视角偏见评估

作者：Teerapol Saengsukhiran、Peerawat Chomphooyod、Narabodee Rodjananant 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e78203726d52)

> 多模态检索系统被期望在语言无关的语义空间中运作，但实际结果常受训练数据中语言流行度与文化关联的系统性偏差影响。现有评估体系聚焦于检索精度，缺乏量化这种“视角偏见”的专用指标与基准。本文构建了3XCM基准与DLBKL/SP指标，通过强制选择任务解耦语义忠实度与文化关联。该工作揭示了显式跨语言对齐在抑制偏见上的优势，但其评估协议基于封闭集选择，能否泛化至开放域大规模检索尚存疑。

】

---

【EVGeoQA: Benchmarking LLMs on Dynamic, Multi-Objective Geo-Spatial Exploration ｜动态多目标地理空间探索基准与评估框架

研究机构：北京师范大学、国防科技大学

作者：Jianfei Wu、Zhichun Wang、Zhensheng Wang 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.07070)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.07070)

> 现有地理空间问答（GSQA）基准多局限于静态拓扑检索，无法评估大语言模型（LLM）在动态位置约束下的复合规划能力。本文切入点在于将定位任务重构为“实时坐标锚定+双目标约束”的动态探索问题，通过构建EVGeoQA基准与GeoRover工具增强智能体框架，量化LLM在长距离空间推理中的性能衰减。该工作揭示了LLM在长程探索中的“懒惰”现象与轨迹总结潜力，但缺乏对探索策略的显式优化机制，其结论的泛化性受限于特定城市与单一领域场景。

】

---

【Evian: Towards Explainable Visual Instruction-tuning Data Auditing ｜可解释视觉指令微调数据审计

研究机构：香港科技大学

作者：Zimu Jia、Mingjie Xu、Andrew Estornell 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.20544)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.20544)

> 视觉指令微调（VIT）依赖高质量训练数据，但现有过滤方法仅依赖粗粒度相似度分数，无法识别逻辑谬误或事实错误等细微语义缺陷。EVIAN 提出“分解-评估”范式，将响应拆解为视觉描述、主观推理与事实声明，并沿图像-文本一致性、逻辑连贯性与事实准确性三个正交维度进行独立审计。该方法通过 300K 样本基准验证了细粒度审计的有效性，证明小样本高质量数据优于大规模噪声数据，但依赖大型语言模型作为审计器可能引入新的偏见。

】

---

【EXPO-SQL: Execution-based Clause-level Policy Optimization for Text-to-SQL ｜执行反馈的子句级信用分配：EXPO-SQL

研究机构：韩国成均馆大学

作者：Jaehoon Lee、CheolWon Na、Suyoung Bae 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_68ec44f7fa34)

> 文本到SQL任务中，强化学习（RL）方法长期依赖查询级二元奖励，导致模型无法区分SQL中正确与错误的子句，产生粗糙的信用分配。现有方案在复杂查询上因惩罚正确部分而收敛缓慢，本文切入点在于利用SQL逻辑执行顺序与差异类型分析，将奖励细化至子句粒度。通过增量执行定位错误子句并设计差异化奖励，EXPO-SQL在BIRD基准上超越最佳RL基线2.4个百分点。该方法验证了细粒度监督对复杂推理的有效性，但其依赖执行环境稳定性的假设在模糊问题场景下是否依然成立，尚存疑。

】

---

【Fast Retrieval and Slow Reasoning for Explainable Multimodal Sentiment Analysis ｜快速检索与慢速推理的多模态情感分析

研究机构：合肥工业大学

作者：Aoqiang Zhu、Min Hu、Yan Xing

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_faa68de3ea41)

> 多模态情感分析（Multimodal Sentiment Analysis, MSA）旨在通过融合文本、音频和视觉信号预测情感极性，但现有全序列融合方法将冗余噪声与有效情感线索混合处理，导致模型对无关模式敏感且决策过程不透明。FRSR 借鉴双过程理论，将建模拆解为证据检索与结构化推理两个阶段，通过稀疏化输入降低计算开销并提升可解释性。该框架在三个基准上取得了有竞争力的性能，但其精度未超越基于大语言模型的最新方法，且 Top-K 稀疏化对长程依赖的影响尚存疑。

】

---

【From Heads to Neurons: Causal Attribution and Steering in Multi-Task Vision-Language Models ｜头导向神经元归因与操控

研究机构：同济大学、美国威斯康星大学麦迪逊分校

作者：Qidong Wang、Junjie Hu、Ming Jiang

论文原文见 [arXiv](https://arxiv.org/abs/2604.17941)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17941)

> 多任务视觉-语言模型（VLM）内部参数功能纠缠，导致错误归因困难且缺乏可控性。现有神经元分析多聚焦单任务或孤立评分，忽略注意力路由上下文，引发多义性噪声。本文提出HONES，通过头条件化因果写入评分定位关键神经元，并实现轻量级操控。该方法在异构任务上实现了统一的神经元重要性评估，但仅验证了基础感知任务，未触及复杂推理链的忠实性。

】

---

【From Scenes to Elements: Multi-Granularity Evidence Retrieval for Verifiable Multimodal RAG ｜从场景到元素：多粒度证据检索的可验证多模态RAG

研究机构：澳门大学

作者：Guanhua Chen、Chuyue Huang、Yutong Yao 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_7a8df6276edb)

> 多模态检索增强生成（Retrieval-Augmented Generation, RAG）旨在通过外部证据缓解大语言模型（Large Language Models, LLMs）的幻觉，但现有方法常以整图或页面为检索单元，导致细粒度查询与粗粒度证据间的归因断裂。本文指出，可验证性要求将视觉元素作为一等检索目标，而非隐式注意力区域。GranuRAG 通过“检测-检索-归因”三阶段框架，实现了元素级证据的透明审计。该工作填补了部分观测场景下的细粒度对齐空白，但其对静态地标领域的依赖限制了通用性验证。

】

---

【FTibSuite: A Comprehensive Resource Suite for Tibetan Vision-Language Modeling ｜藏语视觉-语言模型资源套件

研究机构：上海交通大学、中国科学院

作者：Guixian Xu、Yide Liang、Zeli Su 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.26601)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.26601)

> 低资源语言的多模态研究长期受困于训练数据与评估基准的双重缺失，导致模型能力无法被公平量化与复现。现有方案多聚焦于英语或高资源语言，针对藏语等极小语种的系统性基础设施几乎空白。本文切入点在于构建一套包含数据、基准与基线模型的完整闭环，通过三阶段适配流水线在强骨干上实现藏语能力的可复现迁移。其价值在于填补了藏语多模态研究的基建空白，但实验仅对比无适配基线，缺乏与同类低资源适配方法的横向比较，泛化结论的边界尚存疑。

】

---

【Generalizable Prompt Tuning for Audio-Language Models via Semantic Expansion ｜语义扩展提示调优

研究机构：韩国科学技术院

作者：Jaehyuk Jang、Wonjun Lee、Kangwook Ko 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.20867)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.20867)

> 音频-语言模型（ALMs）提示调优面临基础类过拟合导致的新类泛化崩溃，即基础-新类权衡（BNT）。现有视觉提示调优方法直接迁移至音频域时，因音频基准语义稀疏性导致嵌入空间结构崩塌，单纯架构增强或静态正则化无法重建语义簇。SEPT 通过大语言模型生成语义邻居，引入带边际约束的语义扩展损失，在冻结骨干下显式重塑文本嵌入几何结构。该方法以零额外推理开销显著提升了跨数据集泛化性能，但其效果高度依赖外部 LLM 的邻居生成质量，且未验证在视觉域或动态提示架构下的普适性。

】

---

【Generative Text-to-Image Retrieval via Hierarchical Identifiers and Semantic Internalization ｜生成式多模态对齐中的语义内化框架

研究机构：中国科学院、中国科学院大学

作者：Jie Huang、Junjie Wang、Xin Liao 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_24b8f3e99c5d)

> 文本到图像检索旨在从海量图库中定位与查询语义最匹配的视觉内容，但传统双塔模型因编码器独立导致细粒度交互缺失，单塔模型则因计算开销难以实时部署。生成式检索（Generative Retrieval, GR）将检索重构为标识符预测任务，试图兼顾效率与精度，却面临标识符语义判别性不足、硬对齐偏差及封闭集限制三大瓶颈。SIGMA 通过构建五级层级标识符并引入渐进式语义内化训练，实现了开放集下的动态索引。该框架在 Flickr30K 和 MS-COCO 上显著优于现有生成式基线，但其绝对性能是否超越对比学习 SOTA 仍存疑。

】

---

【GeometryZero: Advancing Geometry Solving via Group Contrastive Policy Optimization ｜几何辅助构造的条件策略学习

研究机构：复旦大学、浙江大学

作者：Yikun Wang、Yibin Wang、Dianyi Wang 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_138b6be39be3)

> 导读 几何推理的核心难点在于模型常无法判断何时需要辅助线，盲目构造反而引入错误。现有强化学习方法对工具调用施加无差别正向奖励，导致模型在简单问题上过度构造。本文提出组对比策略优化（Group Contrastive Policy Optimization, GCPO），通过对比有/无辅助线两组回滚的准确率差异，动态决定辅助奖励的正负号。该方法在7B模型上实现了Geometry3K 78.81%的准确率，但其在高难度长程推理上的表现仍显著低于神经符号系统，暴露出纯语言模型在复杂几何证明中的局限。

】

---

【Geoparsing: Diagram Parsing for Plane and Solid Geometry with a Unified Formal Language ｜统一形式语言下的几何图解析

研究机构：中国科学院、中国科学院大学

作者：Peijie Wang、Ming-Liang Zhang、Jun Cao 等 13 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.11600)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.11600)

> 多模态大模型在几何推理中常因无法准确提取图形中的点、线、面等基础元素而陷入幻觉，导致后续逻辑推导建立在错误前提之上。现有方案多聚焦平面几何或依赖端到端黑盒推理，缺乏对立体几何的严格形式化定义与可验证的解析训练机制。本文通过构建覆盖平面与立体几何的统一形式语言及大规模数据集 GDP-29K，并引入基于规则验证的强化学习，实现了高精度的图形符号化转换。该工作填补了立体几何解析的数据空白，但其作为感知前端的定位，尚未解决解析结果与复杂符号推理引擎的动态耦合问题。

】

---

【Global Context or Local Detail? Adaptive Visual Grounding for Hallucination Mitigation ｜冲突驱动视觉证据获取

研究机构：北京航空航天大学、美团

作者：Yubo Jiang、Xin Yang、Abudukelimu Wuerkaixi 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.24396)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.24396)

> 大视觉语言模型（LVLMs）在多步推理中常因视觉证据脱节产生对象幻觉，现有推理时干预多聚焦于解码或表征层，忽略了输入端视觉证据获取的结构性缺陷。Think-with-Images（TwI）范式试图通过生成辅助视图解决此问题，但面临粒度-上下文权衡与工具提案过度信任两大瓶颈。Active-Look通过双专家分歧检测冲突区域，并采用混合渲染策略在预算约束下选择性验证，实现了无需训练的幻觉抑制。该方法在POPE Adversarial设置上较基线提升4.94%，但在CHAIR自由生成任务上未超越最新SOTA，其依赖外部检测器的设计引入了固定计算开销。

】

---

【Ground Then Rank: Revisiting Knowledge-Based VQA with Training-Free Entity Identification ｜解耦实体识别与证据重排：训练无关的KB-VQA工作流重构

研究机构：美国伦斯勒理工学院

作者：Qian Ma、Qiong Wu、Zhengyi Zhou 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.23881)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.23881)

> 知识增强视觉问答（Knowledge-Based Visual Question Answering, KB-VQA）要求模型在图像像素之外定位细粒度实体并提取支撑证据，但现有多模态检索增强生成（Multimodal Retrieval-Augmented Generation, MM-RAG）方法将实体判别与段落重排耦合于单一评分函数，导致高计算成本与泛化受限。本文切入点在于发现多模态大语言模型（Multimodal Large Language Models, MLLMs）在开放生成中难以命名实体，但在给定候选集时具备显著的判别能力。通过引入“先识别后回答”（Identify-Before-Answer, IBA）框架，将实体选择与文本重排解耦，本文在无需微调的情况下超越了训练式基线，但其性能上限仍受限于静态检索范式，未触及动态多步推理的边界。

】

---

【Grounded Concreteness: Human-Like Concreteness Sensitivity in Vision–Language Models ｜视觉接地对语义具体性的分级影响

作者：Aryan Roy、Zekun Wang、Christopher J. MacLellan

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ec910be8d71f)

> 视觉-语言模型（Vision-Language Model, VLM）是否比纯文本大语言模型（Large Language Model, LLM）具备更接近人类的“具体性”感知能力，是检验符号接地假说的关键问题。现有研究多将多模态训练视为整体性能提升，缺乏隔离视觉监督对抽象与具体概念差异化影响的受控消融。本文通过匹配同族LLM与VLM，在仅文本输入条件下，从输出行为、嵌入几何与注意力动态三个层面量化视觉接地的分级效应。该研究证实了视觉训练对具体概念的定向增益，但缺乏跨架构泛化证据，且未区分数据增强与模态接地的因果贡献。

】

---

【Hard to Read, Easy to Jailbreak: How Visual Degradation Bypasses MLLM Safety Alignment ｜视觉退化引发的多模态大语言模型越狱漏洞

研究机构：西湖大学、美国加州大学默塞德分校

作者：Zhixue Song、Boyan Han、Yiwei Wang 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.07250)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.07250)

> 视觉上下文压缩技术通过降低图像分辨率来减少视觉Token开销，但这一标准操作意外削弱了多模态大语言模型的安全对齐机制。现有防御多依赖对抗优化或语义操纵，忽略了自然退化对模型内部认知资源的挤占效应。本文提出“认知过载”假设，并通过“结构化认知卸载”策略强制串行推理以恢复安全。该工作揭示了效率与安全间的隐性冲突，但其防御机制在复杂视觉推理场景下的泛化能力仍存疑。

】

---

【Hierarchical Visual Agent: Managing Contexts in Joint Image-Text Space for Advanced Chart Reasoning ｜层级视觉智能体：联合图文空间中的上下文管理

研究机构：美国东北大学、美国莱斯大学

作者：Qihua Dong、Ruozhen He、Junwen Chen 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.04304)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.04304)

> 复杂图表推理要求模型在多个子图间进行多步数值计算，但现有多模态大语言模型（MLLMs）在处理此类任务时，常因累积的异构上下文导致早期关键证据被稀释或遗忘。本文指出，线性追加视觉裁剪与文本推理轨迹的“Thinking with Images”范式存在单调上下文膨胀缺陷，提出HIERVA，一种免训练的Manager-Worker层级架构，通过上下文蒸馏与封装将全局上下文保持紧凑。该方法在CHARXIV推理子集上达到64.2%准确率，验证了层级化上下文管理对复杂推理的有效性，但其免训练策略在极端复杂场景下的鲁棒性仍存疑。

】

---

【Hybrid-Vector Retrieval for Visually Rich Documents: Combining Single-Vector Efficiency and Multi-Vector Accuracy ｜混合向量检索：兼顾单向量效率与多向量精度

研究机构：韩国科学技术院、韩国汉阳大学

作者：Juyeon Kim、Geon Lee、Dongwon Choi 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.22215)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.22215)

> 视觉文档检索（VDR）旨在从包含图表、表格等复杂视觉元素的文档库中定位相关页面，以支撑检索增强生成（RAG）的事实可靠性。现有单向量检索虽高效但精度不足，多向量检索虽精准但计算开销巨大，二者在效率与精度间存在刚性权衡。本文提出HEAVEN，通过两阶段混合架构，在索引期构建视觉摘要页（VS-Page）进行粗筛，在查询期过滤关键Token进行精排，以极低的计算成本逼近多向量模型的检索精度。该框架在四个基准上保留了99.87%的Recall@1性能，同时降低99.82%的FLOPs，但其依赖显式标题布局构建VS-Page的假设，在缺乏结构化标题的文档场景下的鲁棒性存疑。

】

---

【Infinity-Parser: Layout-Aware Reinforcement Learning with High-quality Document Parsing Dataset ｜布局感知强化学习文档解析器

研究机构：英国利物浦大学

作者：Baode Wang、Biao Wu、Weizhen Li 等 11 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_02734a87777b)

> 端到端文档解析旨在将扫描图像直接转换为结构化Markdown，但现有视觉语言模型（VLM）在监督微调（SFT）下易过拟合表面模式，导致分布外（OOD）泛化能力不足。Infinity-Parser通过构建400,066页高质量数据集Infinity-Doc-400K，并引入基于编辑距离、段落计数与阅读顺序的多面奖励强化学习（RL）框架，解决了SFT在复杂布局下的结构一致性退化问题。该方法在OmniDocBench上取得0.122的英文整体编辑距离，验证了RL在文档解析中的有效性，但其绝对性能仍低于部分最新SOTA，且对合成数据依赖性的边界尚存疑。

】

---

【Inject to Heal: Alleviating hallucination in LVLMs via Context Embedding Injection ｜上下文嵌入注入

作者：Mehrdad Fazli、Bowen Wei、Ziwei Zhu

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9f9185eac5ff)

> 大视觉语言模型（LVLMs）在开放生成中常因语言先验压制视觉信号而产生对象幻觉，现有推理时干预方法多聚焦于Logits层对比或注意力校准，难以在长序列生成中维持稳定的视觉接地。本文切入点在于发现真实Token比幻觉Token更早稳定概率质量的“承诺深度差距”，并据此提出无需训练的上下文嵌入注入（Context Embedding Injection, CEI）策略。该方法通过复用初始前向传播的隐状态作为接地锚点，动态调整解码过程中的隐状态混合权重，以抑制幻觉。CEI在CHAIR、AMBER和MMHal-Bench上优于主流基线，但其对超参数的依赖及在判别式任务上的表现未经验证。

】

---

【JX4MEI: Multimodal Semantically-Enhanced LLM for Joint Multimodal Emotion-Intent Explanation and Classification ｜联合情感意图解释与分类

研究机构：美国东北大学

作者：YiJie Huang、Xiaocui Yang、Shi Feng 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1b51a061b85a)

> 多模态情感计算长期受困于“黑盒分类”困境，模型能预测用户情绪却无法解释成因，导致在心理健康等高利害场景中缺乏可信度。现有大语言模型（MLLM）方案虽引入生成式推理，但特征对齐机制粗糙，难以捕捉细粒度因果线索。本文提出 JX4MEI 任务与 XMEI-Qwen 模型，通过语义引导的查询机制强化模态特征与高层语义的对齐。该工作填补了情感与意图联合解释的空白，但其依赖人工精修数据，模型对真实噪声的鲁棒性尚存疑。

】

---

【K-GIP: Diagnosing Logical Fractures in Large Vision-Language Models via Verification Scene Graphs and Sequential Pruning ｜知识引导上下文探测

作者：Yujun Hu、Xiaoyu Zhou、Changbo Wang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_210eb4cc7604)

> 大视觉语言模型（LVLM）在视觉问答中常因依赖语言先验而非视觉证据产生幻觉，现有基准多采用扁平指标，无法区分感知错误与逻辑推理错误。K-GIP 通过构建双感知真值与验证场景图，将存在性前提与属性推理的因果依赖显式建模，以序列逻辑剪枝惩罚逻辑断裂。该框架有效量化了模型在细粒度任务中的逻辑一致性，但其诊断精度受限于上游检测器的置信度阈值，且未验证图结构评估在动态场景下的泛化能力。

】

---

【LatentRefusal: Latent-Signal Refusal for Unanswerable Text-to-SQL Queries ｜基于隐状态探针的文本到SQL安全拒绝机制

研究机构：复旦大学

作者：Xuancheng Ren、Shijing Hu、Zhihui Lu 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.10398)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.10398)

> 文本到SQL系统在面临不可回答或模糊查询时，极易生成看似合理但语义错误的可执行代码，导致数据泄露或业务事故。现有基于提示词或输出不确定性的拒绝策略要么在模型幻觉时失效，要么因需多次采样或执行SQL而违背安全低延迟约束。本文提出在SQL生成前，通过冻结大语言模型中间层隐状态进行确定性门控拦截。该机制以极低的计算开销实现了高可靠的安全拒绝，但其在复杂多跳推理场景下的信号捕捉能力仍存疑。

】

---

【Learning Flexible Large Multimodal Models with Arbitrary Modality Combinations ｜灵活多模态学习框架 Flex-M3

研究机构：美国北卡罗来纳大学教堂山分校

作者：Xinyu Zhao、Kangqi Ni、Jie Peng 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_89b0ecbb2070)

> 多模态大语言模型（MLLMs）在扩展至音频、3D等异构模态时，面临数据配对稀缺与Token序列线性膨胀的双重瓶颈。现有方法要么依赖全模态完整数据，要么通过静态填充处理缺失，导致泛化能力随模态数量增加而下降。Flex-M3 通过引入基于文本和视频锚点的缺失模态生成模块，结合两阶段压缩机制，实现了在任意模态组合下的鲁棒训练与推理。该框架在 NExT-QA 等基准上优于全模态基线，但其生成模块的泛化边界及计算开销的长期影响仍需进一步审视。

】

---

【LLaTiSA: Towards Difficulty-Stratified Time Series Reasoning from Visual Perception to Semantics ｜分层时序推理模型

研究机构：阿里巴巴集团

作者：Yueyang Ding、HaoPeng Zhang、Rui Dai 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17295)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17295)

> 时序推理（Time Series Reasoning, TSR）旨在让模型从数值证据、模式感知到语义判断中构建对时间序列的综合理解，但现有基准缺乏统一的任务分层定义且标签存在模糊性，导致高级推理建立在不可靠的基础接地之上。本文切入点在于指出当前模型在基础数值读取（L1）上的失败是高层推理失效的根源，而非单纯缺乏语义能力。通过构建四级认知分类法与配套数据集HITSR，并采用双视图输入与三阶段课程微调训练VLM，LLATISA实现了从定性视觉直觉到定量数值精度的桥接。该工作确立了时序推理的评估基线，但其对长序列处理效率及真实世界复杂因果场景的泛化能力仍存疑。

】

---

【Lost in Translation: Do LVLM Judges Generalize Across Languages? ｜多语言多模态评估器基准

研究机构：加拿大约克大学、加拿大阿尔伯塔大学

作者：Md Tahmid Rahman Laskar、Mohammed Saidul Islam、Mir Tafseer Nayeem 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.19405)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e5fd54c58245)

> 自动化评估器在视觉语言模型（LVLM）对齐与部署中占据核心地位，但现有基准几乎完全局限于英语，导致评估器在非英语场景下的泛化能力成为盲区。VL-RewardBench 等基准虽解决了多模态偏好判断问题，却未触及语言多样性；MRewardBench 虽扩展至多语言，却缺失视觉模态。本文通过翻译构建首个覆盖 25 种语言、60K 实例的多语言多模态评估器基准 MM-JudgeBench，并实证了模型规模与多语言鲁棒性之间的脱钩。该工作填补了评估器可靠性在多语言维度的空白，但其依赖翻译生成的数据可能引入语义漂移，且未验证原生多语言训练的效果。

】

---

【Making MLLMs Blind: Adversarial Smuggling Attacks in MLLM Content Moderation ｜对抗走私攻击（ASA）与 SMUGGLEBENCH 基准

研究机构：中国科学院大学、美国华盛顿大学

作者：Zhiheng Li、Zongyang Ma、Yuntong Pan 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.06950)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.06950)

> 多模态大语言模型（MLLMs）作为内容审核员时，攻击者利用人类与AI的感知差异，将有害内容嵌入良性视觉载体以逃避检测，这一威胁被称为对抗走私攻击（Adversarial Smuggling Attacks, ASA）。现有越狱研究聚焦于诱导模型生成有害输出或分类错误，忽视了“模型看不见”这一更隐蔽的绕过路径，导致审核系统在真实场景下存在系统性盲区。本文通过构建包含9种走私技术的专用基准 SMUGGLEBENCH，量化了主流模型在感知与推理阶段的脆弱性，并初步验证了思维链（CoT）与监督微调（SFT）的防御局限。该工作揭示了SOTA模型在内容审核中高达90%以上的攻击成功率，但其防御策略仅停留在初步探索阶段，未能解决根本性的感知瓶颈。

】

---

【MDocRAG-RL: Empowering Multi-Modal Document RAG via Complex Visual Reasoning with Reinforcement Learning ｜视觉文档检索增强生成中的细粒度感知与协同优化

研究机构：北京航空航天大学

作者：Zhongyu Wang

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f500bfbaa8f6)

> 多模态大语言模型（MLLMs）在处理包含复杂图表与密集文本的视觉文档时，常因检索嵌入质量低劣及生成阶段视觉细节丢失而陷入推理瓶颈。现有视觉检索增强生成（Visual RAG）系统多将图像直接插入上下文，导致模型无法对关键区域进行细粒度聚焦，且检索器与生成器缺乏协同优化。MDocRAG-RL 通过设计视觉感知动作空间与强化学习（RL）框架，实现了从粗到细的动态信息获取与检索-生成联合训练。该方法在文档问答基准上显著优于现有 RL 基线，但其对长尾实体跨文档关联的适用性仍存疑。

】

---

【Memo-SQL: Structured Decomposition and Experience-Driven Self-Correction for Training-Free NL2SQL ｜结构化分解与经验驱动自修正的无微调NL2SQL框架

研究机构：香港城市大学、华为

作者：Zerui Yang、Weichuan Wang、Yanwei Xu 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.10011)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.10011)

> 自然语言到SQL（NL2SQL）的核心挑战在于将模糊的口语意图映射为精确的结构化查询，而现有测试时扩展（Test-Time Scaling, TTS）方法往往因分解随意导致候选SQL高度相关，且自修正机制依赖静态示例无法适应新错误类型。Memo-SQL通过预定义的多轴结构化分解和动态错误-修正记忆检索，解决了推理多样性不足与修正泛化能力弱的问题。该方法在无微调开源模型上实现了BIRD基准68.5%的执行准确率，同时大幅降低计算开销，但其跨域迁移能力和对复杂嵌套查询的覆盖度仍存疑。

】

---

【MGPO: Thinking with Images via Multi-Turn Grounding-Based Reinforcement Learning ｜多轮定位强化学习

研究机构：复旦大学、新加坡南洋理工大学

作者：Xinyu Huang、Yuhao Dong、Weiwei Tian 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2ee7517732f7)

> 高分辨率图像输入导致视觉令牌数量呈二次方增长，大量无关区域干扰模型对关键细节的捕捉，且受限于上下文长度，模型往往无法直接处理原始分辨率图像。现有方法多依赖昂贵的定位标注或中间奖励信号来引导模型关注特定区域，数据获取成本高且泛化性受限。本文提出多轮定位策略优化（Multi-turn Grounding-based Policy Optimization, MGPO），仅利用最终答案的二元奖励，通过多轮对话中的自动裁剪机制激发模型的定位能力。该方法在无需额外定位标注的情况下，显著提升了高分辨率视觉问答性能，但其定位精度是否足以替代像素级分割在精细交互中的角色，仍存疑。

】

---

【microCLIP: Unsupervised CLIP Adaptation via Coarse-Fine Token Fusion for Fine-Grained Image Classification ｜microCLIP：无监督CLIP适应中的粗-细粒度Token融合

研究机构：阿联酋扎耶德大学、印度理工学院德里分校

作者：Sathira Silva、Eman Ali、Chetan Arora 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.02270)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.02270)

> 无监督适应（Unsupervised Adaptation, UA）旨在利用未标注数据提升CLIP在细粒度分类上的表现，但现有方法依赖全局[CLS] token，无法捕捉区分近邻类别所需的局部空间细节。本文指出，仅靠文本侧的细粒度描述无法弥补视觉侧的空间缺失，必须从图像patch token中提取局部线索。microCLIP通过显著性导向注意力池化（Saliency-Oriented Attention Pooling, SOAP）构建细粒度[FG] token，并与[CLS] token对称融合，结合动态知识聚合实现自训练。该方法在13个细粒度数据集上平均提升2.90%，验证了视觉局部线索的必要性，但其性能上限受限于ViT-B/32骨干的patch分辨率。

】

---

【MiMIC: Mitigating Visual Modality Collapse in Universal Multimodal Retrieval While Avoiding Semantic Misalignment ｜通用多模态检索中的模态坍塌与语义错位缓解

研究机构：南京大学

作者：Juan Li、Chuanghao Ding、Xujie Zhang 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.21326)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.21326)

> 通用多模态检索（UMR）旨在将图像与文本映射至统一嵌入空间以支持跨模态匹配，但现有方法在融合策略上存在固有缺陷。早期融合模型易陷入视觉模态坍塌，晚期融合模型则面临语义错位，导致在缺失模态或复杂查询下检索性能骤降。MiMIC 通过解码器内融合架构与单模态混合训练策略，在保留模态独立性的同时实现动态聚合。该方法在 WebQA+ 与 EVQA+ 基准上超越了主流基线，但其对骨干网络规模的依赖及在完整模态场景下的相对优势仍需进一步审视。

】

---

【Mitigating Hallucinations in VLMs: Enhancing Visual Attention via Head-Wise Perturbation ｜头部感知扰动与视觉引导训练

研究机构：复旦大学

作者：Zhenghua Wang、Yixin Wu、Feiran Zhang 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1fb3c9be414e)

> 视觉语言模型（VLMs）在生成描述时，常因过度依赖语言先验而忽略视觉证据，导致对象幻觉。现有推理时干预方法虽无需重训，但面临计算开销大与超参数敏感的问题，且难以从根源上改变模型对视觉信号的分配机制。本文提出HWP，通过在多头注意力（MHA）中注入连续均匀噪声并限制损失计算于视觉敏感Token，以训练时微调的方式重构注意力分布。该方法在POPE基准上平均提升2.1点准确率，但其训练时干预路线与当前主流的无训练范式存在部署成本上的根本差异。

】

---

【More Images, More Problems? A Controlled Analysis of VLM Failure Modes ｜多图像视觉语言模型失效模式控制分析

研究机构：美国普林斯顿高等研究院、英国伦敦玛丽女王大学

作者：Anurag Das、Adrian Bulat、Alberto Baldrati 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.07812)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.07812)

> 多图像视觉语言模型（LVLMs）在处理跨图信息聚合时普遍失效，现有基准缺乏对失效根因的细粒度控制与机制诊断。本文通过构建程序化生成的MIMIC基准，隔离了信息分布、干扰项等混淆变量，揭示了模型在深层网络中跨图注意力衰减的架构性缺陷。通过数据合成与层间注意力掩码微调，该方法在保持低计算成本的同时显著提升了跨图推理性能。其价值在于将黑盒评估转化为白盒机制诊断，但缺乏闭源模型对比，且未验证非因果注意力架构下的泛化性。

】

---

【MPTc-Bench: Measuring Cross-market Generative Ability of Vision-Language Models via Movie Poster Transcreation ｜电影海报跨市场转创基准

研究机构：日本京都大学

作者：Youyuan Lin、Yuan Li、Yahan Yu 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_cc82a23ef819)

> 导读 多模态机器翻译长期聚焦于利用视觉上下文消解文本歧义，但现有方法在处理营销资产时往往忽略目标市场的隐性设计偏好，导致译文虽语义正确却缺乏文化契合度。本文切入点在于将“转创”概念引入电影海报领域，指出通用视觉语言模型在保持电影身份的同时难以执行市场特定的排版与风格调整。作者构建了包含582个跨市场样本的MPTc-Bench基准，并提出两阶段Planner-Editor框架以分离决策与执行。该工作揭示了当前模型在本地化文本渲染上的显著缺陷，但缺乏专用图像内翻译模型的对比，其结论的普适性存疑。

】

---

【MT-Video-Bench: A Holistic Video Understanding Benchmark for Evaluating Multimodal LLMs in Multi-Turn Dialogues ｜多轮视频对话基准

研究机构：复旦大学、南京大学

作者：Yaning Pan、Qianqian Xie、Guohui Zhang 等 16 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.17722)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.17722)

> 视频理解领域长期聚焦于单轮问答，忽略了真实交互中用户迭代提问、话题切换与上下文依赖的复杂性。现有基准如Video-MME和LongVideoBench仅评估模型对视频内容的静态感知，无法衡量其在多轮对话中维持连贯性、拒绝幻觉及主动交互的能力。本文构建MT-Video-Bench，通过1,000个多轮对话实例系统评估多模态大语言模型（MLLMs）的感知性与交互性。该基准填补了多轮视频对话评估的空白，但仅作为评测工具，未提出新的模型架构或训练策略，其有效性依赖于Checklist评估协议的完备性。

】

---

【MTMCS-Bench: Evaluating Contextual Safety of Multimodal Large Language Models in Multi-Turn Dialogues ｜多轮多模态上下文安全基准

研究机构：美国圣母大学、美国加州大学洛杉矶分校

作者：Zheyuan Liu、Dongwhi Kim、Yixin Wan 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.06757)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.06757)

> 多模态大语言模型（Multimodal Large Language Models, MLLMs）在真实部署中面临的核心安全挑战，已从单轮对抗攻击演变为多轮交互中意图的渐进式演变与上下文重构。现有安全评估基准多聚焦于单轮静态输入，无法捕捉恶意意图在多轮对话中通过良性提问逐步升级，或在初始恶意意图下伪装成无害追问的隐蔽模式。MTMCS-Bench 提出了一种包含升级风险与上下文切换风险的双模式多轮多模态评估框架，通过配对安全与不安全对话及多模态/单模态对照，量化模型在意图识别、安全意识与有用性之间的动态平衡。该基准揭示了当前防御机制在多轮上下文中的系统性失效，为动态安全对齐提供了细粒度的诊断工具，但其依赖大语言模型作为评判者可能引入的评分偏差仍需进一步验证。

】

---

【MTO: A Multi-turn Conversational Text-to-OverpassQL Dataset for Enhanced OpenStreetMap Query Generation ｜基于语法树剪枝的多轮地理空间查询数据集构建

作者：Haodi Zhang、Xinrui Zhu、Mingze Kong 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_38f3ab66aa65)

】

---

【Omni-R1: Towards the Unified Generative Paradigm for Multimodal Reasoning ｜统一生成式多模态推理

研究机构：香港理工大学、新加坡管理大学

作者：Dongjie Cheng、Yongqi Li、Zhixin Ma 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.09536)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.09536)

> 多模态大模型在复杂视觉任务中常因中间推理步骤缺乏视觉证据而失效，现有交错推理方法依赖单一任务模式或外部工具，难以泛化至多种视觉技能。本文提出统一生成式多模态推理范式，将缩放、定位、标记等技能内化为模型内部的功能图像生成过程。通过感知对齐损失与校准奖励稳定生成，并引入自举机制消除人工标注依赖。该框架在自建基准上显著优于基线，但功能图像生成的物理一致性验证仍存疑。

】

---

【OmniDiagram: Advancing Unified Diagram Code Generation via Visual Interrogation Reward ｜通用逻辑图代码生成中的视觉验证奖励机制

研究机构：中国科学院、中国科学院大学

作者：Haoyue Yang、Xuanle Zhao、Xuexin Liu 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.05514)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.05514)

> 多模态大语言模型在将视觉图表转化为可执行代码时，常面临语法正确性与视觉保真度脱节的困境。现有方法多依赖单一任务或固定语言，且强化学习中的二元奖励信号难以捕捉细粒度结构差异。本文提出VIVA机制，通过生成实例特定的视觉问题来评估渲染结果，实现细粒度反馈。该框架在通用逻辑图生成上超越了专用代码模型，但其对VQA评估模型的依赖及离线问题生成的泛化边界尚存疑。

】

---

【On the Cultural Anachronism and Temporal Reasoning in Vision Language Models ｜文化时代错置与视觉语言模型时序推理基准

作者：Mukul Ranjan、Prince Jha、Khushboo Kumari 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.15071)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.15071)

> 视觉语言模型在文化遗产数字化应用中面临历史语境误读风险，现有通用基准缺乏对时间维度一致性的系统评估。本文提出“文化时代错置”概念，构建首个针对印度历史文物的时序推理基准 TAB-VLM。通过 600 道多选题量化 10 个前沿模型在年代排序、材质可用性等方面的表现，揭示模型规模与时序推理能力非线性关联。该工作填补了垂直领域评估空白，但单一文化域与静态多选协议限制了结论的普适性。

】

---

【PedagogyBench: A Cognitive-Driven Benchmark for Multimodal Instructional Video Understanding ｜教学视频认知基准

作者：Xiaokang Jin、Jia Zhu、Jingjiang Liu 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_379c43b1a268)

> 现有视频理解基准将课堂视频视为事件序列，忽略了教学意图与认知脚手架的深层逻辑，导致模型在“看懂画面”与“理解教学”之间出现能力断层。本文切入点在于构建一个基于教学法阶段分割与认知金字塔评估框架的专用基准，通过双流语义注入与专家修正生成结构化数据。其核心贡献是提出认知保真度分数（Cognitive Fidelity Score, CFS）以诊断模型在感知、理解、应用与诊断四个维度的平衡性。该基准揭示了当前多模态大语言模型（Multimodal Large Language Models, MLLMs）在判别式任务与生成式任务间的显著差距，但其跨语言设置与自建基准的外部效度仍存疑。

】

---

【Perceptual Hallucination in Vision–Language Models: Definition, Analysis and Verification ｜文档感知幻觉的量化与归因分析

作者：Taewook Hwang、Inbum Heo、Sung Jun Lee 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ea1311568b63)

> 视觉语言模型在文档理解任务中常因视觉证据缺失而生成看似感知的虚假信息，这一现象被称为感知幻觉。现有研究多聚焦于自然图像的对象幻觉或推理阶段的逻辑错误，缺乏对文档场景下视觉感知阶段失效的系统性量化。本文构建了包含原始-受损图像对的基准数据集，通过激活补丁技术定位视觉编码器在幻觉生成中的因果作用，并验证了基于大语言模型的后验过滤策略。该工作明确了文档感知幻觉的机制根源，但未提供生成阶段的实时干预算法，其缓解效果仅依赖外部检测器。

】

---

【PhysPRM: A Generative Process Reward Model with Fine-grained Diagnosis for Physics Problem Solving ｜生成式过程奖励模型

作者：Yuxuan Dong、Xinyu Zhang、Lingling Zhang 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_5864749fb482)

> 物理问题求解要求模型在长推理链中维持物理一致性，但大语言模型常因隐式约束解码失败或状态分析错误导致答案偏差。现有判别式过程奖励模型仅输出标量分数，无法定位具体错误类型，难以指导模型修正。PhysPRM 将过程监督重构为生成任务，通过输出包含详细批评、判断和错误分类的诊断序列，实现步骤级纠错。该方案在文本物理推理中验证了细粒度监督的有效性，但其对视觉几何信息的缺失是否限制了物理理解的深度，仍存疑。

】

---

【PlaM: Training-Free Plateau-Guided Model Merging for Better Visual Grounding in MLLMs ｜基于层级视觉Token掩码的免训练模型合并

研究机构：美国东北大学、德国慕尼黑大学

作者：Zijing Wang、YongKang Liu、Mingyang Wang 等 11 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_70720bb65af4)

> 多模态大语言模型（MLLMs）在指令微调后常出现文本推理能力退化，导致视觉定位依赖语言先验而非图像证据。现有修复方案多依赖额外训练或架构修改，缺乏零成本干预手段。本文通过层级视觉Token掩码定位性能平台期，并在该区间线性插值基座语言模型权重，以恢复晚期层的语义决策结构。该方法在通用多模态基准上带来一致提升，但其在专用定位任务上的有效性及与强化学习路线的相对优势尚未得到验证。

】

---

【PlotGen-Bench: Evaluating VLMs on Generating Visualization Code from Diverse Plots across Multiple Libraries ｜多库动态可视化代码生成基准

作者：Yi Zhao、Zhen Yang、Shuaiqi Duan 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c82832a867c4)

> 现有图表转代码基准局限于静态二维图与单一绘图库，无法评估模型在三维、动画及跨框架场景下的真实生成能力。PlotGen-Bench 通过构建涵盖 30 种图表类型、5 个 Python 库及 3 类任务（复制、转换、多库生成）的基准，填补了动态可视化评估空白。其核心贡献在于引入混合评估协议，结合执行率与视觉相似度评分。该基准揭示了通用视觉语言模型在复杂时序与跨库语法泛化上的显著短板，但缺乏专用图表模型的对比，限制了结论的普适性。

】

---

【Preserving Language Capabilities in Vision-Language Models via Representation Regulation ｜视觉语言模型中的表示正则化

研究机构：华南理工大学、美国卡内基梅隆大学

作者：ZiXuan Chen、Juncheng Tao、Ziqian Zeng

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8d1f370c08eb)

> 视觉语言模型（VLM）在提升多模态推理能力的同时，往往导致纯文本任务性能显著下降，这一现象被称为语言退化。现有方法多通过冻结参数或增加文本数据来缓解，但未能触及退化根源。本文指出退化源于后表示层内的“表示混合”，并提出基于再生核希尔伯特空间（RKHS）的表示分布差异（RDD）损失，在训练早期约束嵌入距离以保护语言能力。该方法在保持视觉性能的同时有效恢复了语言基准得分，但其效果依赖于对后表示层边界的模糊界定，且未验证在极端数据规模下的边际收益。

】

---

【PV-SQL: Synergizing Database Probing and Rule-based Verification for Text-to-SQL Agents ｜数据库探针与规则验证协同的文本到SQL智能体

研究机构：美国普渡大学

作者：Yuan Tian、Tianyi Zhang

论文原文见 [arXiv](https://arxiv.org/abs/2604.17653)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17653)

> 文本到SQL系统在处理复杂查询时，常因无法获取数据库实际值而误解语义，且生成的SQL缺乏有效的语义校验机制。现有提示工程方法依赖静态模式链接，无法动态探索数据内容，而基于大语言模型（LLM）的自我验证又存在不可靠与高成本问题。PV-SQL通过“数据库探针”动态获取数据证据，结合“规则约束验证”进行确定性修复，构建了输入增强与输出校验的闭环。该方法在免微调范式下显著提升了执行准确率与效率，但其规则覆盖范围有限，对长尾语义约束的泛化能力存疑。

】

---

【R$^3$-SQL: Ranking Reward and Resampling for Text-to-SQL ｜基于组级奖励与代理重采样的文本到SQL排序框架

研究机构：韩国电子通信研究院、韩国首尔大学

作者：Hojae Han、Yeonseok Jeong、Seung-won Hwang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.25325)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.25325)

> 文本到SQL系统普遍采用“生成-排序”范式，但现有排序器无法区分功能等价但表面形式不同的SQL，且当正确SQL未出现在候选池中时无法恢复。本文指出这两者分别对应“功能不一致性”与“有界召回”问题，提出R³-SQL框架，通过执行结果分组、组级双信号排序及条件触发的代理重采样统一解决。该方法在BIRD-dev上取得75.03%的执行准确率，但依赖监督训练的排序器限制了域外泛化能力。

】

---

【RATION: Entropy-Driven Task-Adaptive Visual Attention Allocation Framework for Multimodal Reasoning ｜熵驱动任务自适应视觉注意力分配框架

作者：Xingle Xu、Fanheng Kong、Dexian Cai 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_45c37346cf0e)

> 多模态大语言模型在计数与OCR等视觉密集任务中常因内部注意力分配与任务需求错配而失效，现有推理时增强方法多依赖外部提示或链式生成，缺乏对模型内部视觉关注机制的显式调控。RATION通过单次前向传播中的层激活变化推断任务类型，并基于注意力熵动态调制关键层的视觉注意力强度，实现训练无关的推理时干预。该方法在四个骨干模型与七个基准上取得一致增益，但其任务分类粒度与熵信号的泛化边界尚待检验。

】

---

【ReaGeo: Reasoning-Enhanced End-to-End Geocoding with LLMs ｜ReaGeo：基于大语言模型的端到端地理编码

研究机构：阿里巴巴集团、清华大学

作者：Jian Cui、Zhiyuan Ren、Desheng Weng 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.21357)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.21357)

> 地理编码旨在将人类可读的地址文本转换为机器可识别的坐标，传统方法依赖复杂的实体提取与数据库检索，易受地址歧义与数据覆盖限制。本文提出ReaGeo，通过大语言模型直接生成Geohash序列，结合思维链推理与强化学习，实现端到端坐标预测。该方法在模糊地址解析上显著优于传统检索与通用大模型，但其纯文本模态与单一城市数据源限制了跨地域泛化能力的验证。

】

---

【Reasoning in the Dark: Interleaved Vision-Text Reasoning in Latent Space ｜交错视觉-文本潜在推理

研究机构：香港理工大学、新加坡管理大学

作者：Chao Chen、Zhixin Ma、Yongqi Li 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.12603)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.12603)

> 多模态大模型在长链推理中面临视觉证据利用不足与显式文本生成带来的高延迟矛盾。现有方法要么依赖纯文本推理导致视觉漂移，要么通过显式图像-文本交错增加标注成本与推理开销。本文提出IVT-LR，将文本与视觉推理统一置于潜在空间，通过隐藏状态与动态选择的图像嵌入替代显式Token。该方法在精度与效率上均超越基线，但其训练范式与主流强化学习路线的差异，以及缺乏与RLVR方法的公平对比，使其在领域定位上存在显著盲区。

】

---

【Recovered in Translation: Efficient Pipeline for Automated Translation of Benchmarks and Datasets ｜推理时计算扩展下的多语言基准翻译框架

研究机构：瑞士苏黎世联邦理工学院

作者：Hanna Yukhymenko、Anton Alexandrov、Martin Vechev

论文原文见 [arXiv](https://arxiv.org/abs/2602.22207)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.22207)

> 多语言大语言模型（LLM）评估的可靠性受制于翻译基准的质量，现有资源常因语义漂移和上下文丢失导致性能指标失真。传统机器翻译工具缺乏指令遵循能力，且将问题与选项分离翻译破坏了语法一致性，而简单的单次生成无法捕捉中资源语言的细微错误。本文提出一个自动化框架，通过测试时计算扩展策略（Test-time Compute Scaling），特别是多轮竞争性排序方法 T-RANK，在无需训练的情况下提升翻译保真度。该框架在八个东欧及南欧语言上验证了有效性，但其对长文本复杂结构的处理能力及开源模型适配性仍存疑。

】

---

【Region-R1: Reinforcing Query-Side Region Cropping for Multi-Modal Re-Ranking ｜区域裁剪强化学习

研究机构：美国德州农工大学

作者：Chan-Wei Hu、Zhengzhong Tu

论文原文见 [arXiv](https://arxiv.org/abs/2604.05268)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.05268)

> 多模态检索增强生成（MM-RAG）的重排序阶段长期受困于查询图像中无关视觉干扰项对全局嵌入的污染，导致相似度计算失真。现有重排序方法如EchoSight和OMGM均假设查询表示固定，仅优化候选交互机制，忽略了查询侧视觉信息的动态可控性。本文提出Region-R1，将查询图像的区域选择形式化为强化学习决策问题，通过r-GRPO算法学习何时裁剪及裁剪何处。该方法在E-VQA和InfoSeek上将条件召回率@1分别提升20%和8%，但仅验证了单区域硬裁剪的有效性，未探讨软性注意力或多区域选择的潜力。

】

---

【ReSQL: Self-Improving Framework for Reasoning-Aware Text-to-SQL Dataset Generation ｜检索增强错误推理框架

研究机构：LG AI研究院

作者：Minjun Park、Yongju Seong、Myoseop Sim 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c94eec99e1cb)

> 小模型在文本到SQL任务中面临高频执行错误且缺乏零样本自修正能力，现有提示工程方法因依赖大模型推理能力而失效。ReSQL将执行错误转化为结构化推理数据用于微调，并在推理时检索相似错误案例辅助修正。该框架在SPIDER和BIRD基准上使7B-9B模型超越GPT-4，但绝对性能仍低于大模型SOTA，且未验证跨域泛化能力。

】

---

【Rethinking Text-to-SQL: Dynamic Multi-turn SQL Interaction for Real-world Database Exploration ｜动态多轮SQL交互基准

研究机构：中国科学院大学、北京大学

作者：Linzhuang Sun、Tianyu Guo、Hao Liang 等 12 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f3178f68c7fe)

> 现有文本到SQL（Text-to-SQL）基准将任务简化为静态单轮翻译，忽略了真实场景中用户意图的动态演化与数据库状态的持续变更。本文指出，静态评估无法捕捉多轮对话中的状态维护与错误恢复能力，因此构建了首个支持完整CRUD操作的动态交互基准。通过两阶段自动合成管线与三元交互框架，DySQL-Bench揭示了前沿大语言模型在动态SQL推理上的显著脆弱性。该基准填补了动态评估空白，但模拟用户的保真度与评估协议的封闭性仍存疑。

】

---

【Revealing and Enhancing Core Visual Regions: Harnessing Internal Attention Dynamics for Hallucination Mitigation in LVLMs ｜正注意力动态增强

研究机构：西安电子科技大学

作者：Guangtao Lyu、Qi Liu、Chenghao Xu 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.15556)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.15556)

> 大视觉语言模型（LVLMs）在生成描述时，常因语言先验压制视觉信号而产生对象幻觉。现有推理时干预方法要么依赖多前向传播引入扰动偏差，要么依赖静态注意力信号易受注意力汇聚（Attention Sink）干扰。本文发现层间正注意力动态（Positive Attention Dynamics, PAD）能更可靠地揭示语义核心视觉区域，据此提出PADE，通过单次前向传播在注意力Logits层注入动态信号以抑制幻觉。该方法在保持通用多模态理解能力方面表现优异，但在幻觉抑制的绝对指标上仍落后于最新解耦解码策略，其动态信号在不同架构下的鲁棒性尚存疑。

】

---

【S2H-DPO: Hardness-Aware Preference Optimization for Vision-Language Models ｜难度感知偏好优化

研究机构：美国密歇根州立大学、美国卡内基梅隆大学

作者：Nitish Shukla、Surgan Jandial、Arun Ross

论文原文见 [arXiv](https://arxiv.org/abs/2604.18512)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.18512)

> 视觉语言模型（Vision-Language Models, VLMs）在处理多图输入时，常因预设索引问题而回避自主视觉搜索，导致跨图证据整合能力缺失。现有偏好对齐方法仅针对单图局部推理，无法覆盖全局搜索等高阶认知任务。本文通过构建从单图定位到全局搜索的三级难度层级合成数据，利用直接偏好优化（Direct Preference Optimization, DPO）强化模型的多图推理能力。该方法在多图基准上取得显著增益，但其对单图性能的保持机制及层级数据比例的敏感性仍存疑。

】

---

【SafeSteer: A Decoding-level Defense Mechanism for Multimodal Large Language Models ｜解码级动态重排与模态对齐：SafeSteer 的多模态安全防御机制

研究机构：清华大学、上海交通大学

作者：Xinyi Zeng、Xue Yang、Jingyuan Zhang 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.11716)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.11716)

> 多模态大语言模型（MLLMs）面临视觉通道绕过文本安全护栏的结构性威胁，现有防御多依赖高成本微调或低效的输入/输出重写，导致泛化性差且损害模型效用。SafeSteer 切入点在于挖掘 MLLMs 在解码阶段固有的有害性判别能力，通过轻量级探针实时重排候选词，并引入模态语义对齐向量（MSAV）弥合视觉与文本的安全感知差距。该方法以极低的计算开销实现了显著的安全提升，但其对静态向量的依赖及跨骨干泛化性仍存疑。

】

---

【SCOPE: Preserving Modality-Specific Cues to Mitigate Modality Laziness in Multimodal Learning ｜结构一致对齐与扩散融合缓解多模态懒惰

研究机构：武汉大学

作者：Jingfan Yang、Rui Zhang、Liang Hong 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a684ce7a84f3)

> 多模态学习常陷入“模态懒惰”，即模型过度依赖主导模态而忽略互补信号，导致融合性能受限。现有架构正则化或动态协调方法虽能提升融合精度，却往往牺牲非主导模态的独立表征能力，造成表示坍缩。SCOPE 通过互信息引导解耦、参数-free语义图对齐及扩散注意力融合，在保留模态特定线索的同时实现结构级对齐。该框架在五个基准上取得最高27.10%的准确率提升，但其对预训练骨干的依赖及未涵盖缺失场景的局限，使其在动态异构环境下的鲁棒性存疑。

】

---

【Seek-and-Solve: Benchmarking MLLMs for Visual Clue-Driven Reasoning in Daily Scenarios ｜日常场景视觉线索驱动推理基准

研究机构：大连理工大学、清华大学

作者：Xiaomin Li、Tala Wang、Zichen Zhong 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.14041)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.14041)

> 多模态大语言模型（Multimodal Large Language Models, MLLMs）在复杂日常场景中常因视觉噪声干扰而推理失效，现有基准多侧重知识检索或基础感知，难以剥离语言先验对推理过程的污染。本文提出 DailyClue，通过构建包含显式视觉线索标注的“问题-线索-答案”三元组，强制模型在思维链（Chain-of-Thought, CoT）中定位决定性视觉证据。该基准揭示了线索提取准确率是模型推理的核心瓶颈，但其在智能体模型上的低效表现及小样本统计显著性存疑，需进一步验证其作为通用推理诊断工具的边界。

】

---

【ShredBench: Evaluating the Semantic Reasoning Capabilities of Multimodal LLMs in Document Reconstruction ｜碎片化文档语义重建基准

研究机构：西安电子科技大学、上海交通大学

作者：Zichun Guo、Yuling Shi、Wenhao Zeng 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.23813)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.23813)

> 多模态大语言模型（MLLM）在完整文档解析上已接近人类水平，但面对物理撕裂、遮挡等结构断裂场景时，其依赖视觉边缘匹配的能力失效，亟需评估其跨碎片语义推理能力。现有基准多聚焦于光照噪声或长上下文检索，缺乏对离散结构破坏下语义连贯性的系统测试。本文通过物理仿真切割生成无序碎片图像，构建了首个针对碎片化内容恢复的评测基准。该基准揭示了当前MLLM在视觉位置嵌入与语义连续性对齐上的根本缺陷，但仅作为诊断工具，未提供解决该问题的算法方案。

】

---

【SimpleOCR: Rendering Visual Questions to Teach MLLMs to Read ｜视觉化问题训练策略

研究机构：美国卡内基梅隆大学、美国密歇根大学

作者：Yibo Peng、Peng Xia、Ding Zhong 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b2d4504c1c1b)

> 多模态大语言模型（MLLMs）在具备强大光学字符识别（OCR）能力的同时，存在严重的“模态懒惰”现象，即推理时过度依赖文本通道捷径而忽视图像中的视觉文本证据。现有强化学习方法聚焦于逻辑推导或图像扰动鲁棒性，缺乏强制模型激活视觉文本提取路径的结构化约束。本文提出SimpleOCR，通过将所有训练样本转化为视觉化问题（VQ）格式，在输入层面消除文本捷径，迫使模型通过视觉通道解码问题内容。该策略以极低的数据成本实现了分布外泛化的显著提升，但其对纯几何推理任务的轻微负迁移表明，视觉接地与抽象逻辑推理之间存在尚未解耦的张力。

】

---

【Skill Weaving: Efficient LLM Improvement via Modular Skillpacks ｜模块化技能包与全量化压缩

研究机构：哈尔滨工业大学、香港理工大学

作者：Zhuo Li、Guodong Du、Zesheng Shi 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.22205)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.22205)

> 多域大语言模型（LLMs）在固定内存与延迟预算下难以兼顾多领域性能，现有参数高效微调（PEFT）方法能力保留不足，而全参数微调又导致存储与推理开销激增。SkillWeave 通过域隔离的全参数微调构建技能包，再经全量化压缩实现低延迟部署，解决了能力与效率的矛盾。该框架在 9B 规模下超越 32B 单体模型并实现 4 倍加速，但其全参微调训练成本与自生成数据质量依赖未充分量化，长期泛化能力存疑。

】

---

【Soft Head Selection for Injecting ICL-Derived Task Embeddings ｜软头选择注入ICL任务嵌入

研究机构：韩国首尔大学

作者：Jungwon Park、Jimyeong Kim、Changin Choi 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_911366acf3cd)

> 大语言模型（LLM）任务适配长期受困于参数高效微调（PEFT）的高训练成本与上下文学习（ICL）的高推理开销，现有嵌入注入方法虽试图折中，却因缺乏对注意力头功能差异的精准定位而性能不稳定。SITE 将头选择建模为连续优化问题，通过梯度下降学习每个注意力头的注入权重，在零样本推理时仅替换关键头的激活。该方法以 1024 个可训练参数逼近 LoRA 性能，但其在复杂推理任务上的绝对精度仍低于 PEFT，且依赖内部激活访问，限制了其在闭源模型中的应用。

】

---

【Spotlight and Shadow: Attention-Guided Dual-Anchor Introspective Decoding for MLLM Hallucination Mitigation ｜双锚点内省解码

研究机构：澳门大学、香港科技大学

作者：Yebo Wu、Han Jin、Zhijiang Guo 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.10071)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.10071)

> 多模态大语言模型（MLLMs）在生成过程中常因语言先验压倒视觉证据而产生幻觉，现有免训练对比解码方法依赖外部扰动构建负样本，既引入随机噪声导致语义偏移，又因额外前向传播增加1.83倍推理延迟。本文切入点在于发现模型内部层间存在“浅层幻觉高发”与“中层视觉感知峰值”的结构性差异，提出双锚点内省解码（Dual-Anchor Introspective Decoding, DAID），通过视觉注意力动态定位并对比内部层状态，在单次前向传播中同时放大视觉信号并抑制语言惯性。该方法在POPE基准上实现85.08%准确率，但相较于2026年SOTA方法存在显著性能差距，且未验证长序列场景下的有效性。

】

---

【SQL-ASTRA: Alleviating Sparse Feedback in Agentic SQL via Column-Set Matching and Trajectory Aggregation ｜多轮代理强化学习中的轨迹级奖励聚合与列集匹配机制

研究机构：澳大利亚格里菲斯大学、复旦大学

作者：Long Li、Zhijian Zhou、Jiangxuan Long 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.16161)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.16161)

> 文本到SQL任务正从单轮静态生成向多轮动态交互演进，但现有强化学习方法受限于最终轮次的二值反馈，导致中间步骤的信用分配模糊且奖励信号稀疏。本文切入点在于构建一个双层奖励机制，通过列集匹配提供步级密集信号，并利用非对称转移矩阵聚合轨迹级奖励以激励单调改进。该方法将SQL生成建模为有限时域马尔可夫决策过程，结合Lyapunov稳定性理论证明策略的无环收敛性。尽管在7B小模型上验证了多轮代理范式的有效性并超越单轮基线，但其绝对性能仍低于当前SOTA，且多轮交互带来的推理延迟与部署成本问题未被充分量化。

】

---

【SQLAgent: Learning to Explore Before Generating as a Data Engineer ｜SQLAgent: 基于自主探索的双智能体文本到SQL框架

研究机构：西湖大学、美国加州大学默塞德分校

作者：Wenjia Jiang、Yiwei Wang、Boyan Han 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2688e00dcffb)

> 导读 企业级数据库的文本到SQL（Text-to-SQL）任务面临模式链接与跨域泛化的双重瓶颈，现有提示工程方法依赖静态示例或单次生成，难以应对未见过的复杂模式结构。SQLAgent 提出“探索-部署”两阶段框架，通过蒙特卡洛树搜索（MCTS）驱动的自主探索构建数据库特定知识库，再由双智能体协作完成查询生成。该设计将一次性生成转化为主动熟悉数据库的过程，显著提升了复杂查询的执行准确率。然而，探索阶段的高昂计算成本与对实时性场景的适用性限制，使其在通用基准上的表现未达领域最优，其价值边界需结合具体部署场景评估。

】

---

【StructBreak: Structural Cognitive Overload-Induced Safety Failures in MLLMs ｜结构认知过载引发的多模态大语言模型安全失效

研究机构：北京邮电大学、中国科学院

作者：Yang Luo、Xinran Liu、Tiantian Ji 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.25534)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.25534)

> 多模态大语言模型（MLLMs）在解析复杂图表时，其结构推理能力与安全对齐机制存在资源竞争，导致安全护栏在深度推理中失效。现有防御多针对表面符号或像素扰动，无法应对高维拓扑解析引发的内部注意力漂移。本文提出结构认知过载（SCO）概念，并构建黑盒攻击框架StructBreak，利用视觉知识图谱（VKG）诱导模型进入“解析-执行”模式以挤占安全注意力。该研究揭示了“能力-脆弱性悖论”，即推理能力越强越易受结构攻击，但样本量与评估协议的局限性使其结论的普适性存疑。

】

---

【Structured Confidence–Guided Online Adaptation for LLM-based Multi-Label Classification ｜结构化置信度引导的在线测试时适应

作者：Pengyu Xu、JingRen Hou、Liping Jing 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_bfeac332b935)

> 大语言模型（LLMs）在零样本多标签文本分类中表现优异，但静态推理无法应对流式测试数据中的分布偏移与长尾标签退化。现有在线测试时适应（OTTA）方法依赖序列似然作为置信度信号，却因标签共享前缀导致“置信度幻觉”，使错误预测被反复复用。本文提出SCOTTA，通过标签集局部似然比（L3R）精准定位解码分支点的真实竞争，并结合子模记忆库（SMB）在固定预算下平衡标签覆盖与语义多样性，实现无参数更新的持续适应。该方法在四个基准上显著提升了长尾标签的Macro-F1，但其效果高度依赖子模优化的计算开销与标签空间结构，在极端动态分布下的稳定性仍存疑。

】

---

【Switching Heads and Softening Tokens: Turnkey Solutions to Visually Grounded Document QA ｜视觉定位文档问答中的离散-连续监督解耦

作者：Ximing Wen、Wenbo Li、Sudipta Paul 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ab5c6044d923)

> 视觉定位文档问答（Visually Grounded Document Question Answering, VGDQA）要求模型不仅回答自然语言查询，还需在文档图像中精确定位答案对应的边界框。现有方法要么依赖刚性后处理导致多答案场景失效，要么将坐标视为普通文本token而丧失空间距离感知，导致细粒度定位收敛缓慢。本文通过引入可微分软token机制与双头回归架构，在统一LLM骨干中实现了结构鲁棒性与空间精度的互补集成。该方案在基准测试中确立了新的性能上限，但其对OCR输入质量的强依赖及长文档下的注意力衰减，限制了其在复杂真实场景中的泛化边界。

】

---

【System-Mediated Attention Imbalances Make Vision-Language Models Say Yes ｜系统介导注意力失衡与视觉语言模型Yes-bias

作者：Tsan Tsai Chan、Varsha Suresh、Anisha Saha 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f8b1ec28d4f9)

> 导读 视觉语言模型（VLMs）在二元判断任务中常表现出无差别回答“是”的偏差，即Yes-bias，这源于输入模态间注意力分配的结构性失衡。现有缓解策略多基于“图像中心”假设，试图通过增强图像注意力来抑制幻觉，但缺乏对系统模态冗余注意力的因果验证，导致在依赖细粒度信息的组合任务上效果受限。本文提出“系统介导”假设，通过因果干预将解码器后层的系统模态注意力比例重分配至图像与文本模态，以恢复细粒度信息提取能力。该框架在五个组合基准上显著优于图像增强基线，但在依赖高层表征的知识提取任务上失效，揭示了注意力干预与任务表征粒度之间的深层耦合。

】

---

【Thinking with Map: Reinforced Parallel Map-Augmented Agent for Geolocalization ｜地图增强代理式地理定位

研究机构：厦门大学、阿里巴巴集团

作者：Yuxiang Ji、Yong Wang、Ziyu Ma 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.05432)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.05432)

> 图像地理定位旨在从视觉线索推断拍摄地点的经纬度，核心难点在于开放世界中线索稀疏且易产生幻觉。传统方法依赖静态特征匹配或内部知识推理，缺乏对外部地理信息的动态验证机制，导致细粒度定位精度受限。本文提出“地图增强代理”框架，通过引入地图API工具实现假设-验证闭环，并结合强化学习与并行测试时缩放优化推理效率。该方法在细粒度定位上显著超越闭源模型，但粗粒度性能仍受基座模型能力制约，且地图工具引入初期曾导致全局认知偏差。

】

---

【Token-Level Inference-Time Alignment for Vision-Language Models ｜令牌级推理时对齐

研究机构：浙江大学、中山大学

作者：Kejia Chen、Jiawen Zhang、Jiacong Hu 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.21794)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.21794)

> 大视觉语言模型（LVLMs）在生成描述时，常因语言先验压制视觉信号而产生对象幻觉，这一可靠性危机在2023年随开源模型爆发而凸显。现有推理时干预策略多依赖序列级奖励模型，反馈延迟高且计算开销大，难以在解码初期抑制幻觉。本文提出TITA（Token-Level Inference-Time Alignment），通过训练轻量级自回归奖励模型，在解码阶段以令牌级对数概率比提供密集引导。该方法在POPE基准上超越SOTA，但在CHAIRs指标上显著落后，其细粒度生成抑制能力存疑。

】

---

【Towards Mitigating Hallucinations in Large Vision-Language Models by Refining Textual Embeddings ｜视觉对齐嵌入

作者：Aakriti Agrawal、Gouthaman KV、Rohith Aralikatti 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.05017)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.05017)

> 大视觉语言模型（LVLMs）在生成描述时，常因语言先验压制视觉信号而产生对象幻觉，这一可靠性危机在2023年随开源模型爆发而凸显。早期研究聚焦数据对齐与指令微调，试图从源头纠正偏差，但受限于标注成本与泛化瓶颈，效果有限。本文指出主流架构中视觉嵌入仅作为附加项拼接至文本序列，导致LLM骨干在自注意力中系统性偏向文本，提出在训练阶段将平均池化的视觉特征融合进每个文本嵌入，以重构模态间的注意力平衡。该方法在Video-LLaVA上实现了显著的幻觉抑制，但其依赖重新训练的范式与当前主流的推理时干预路线存在根本性差异，且缺乏与SOTA解码策略的横向对比，其泛化边界尚待厘清。

】

---

【Towards Unified Multimodal Large Language Models: A survey ｜统一多模态大语言模型架构分类与协同机制审视

研究机构：美国东北大学

作者：Xu Ma、Yitian Zhang、Yun Fu

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9fa04eb6f3bd)

> 统一多模态大语言模型旨在单一架构内融合视觉理解与图像生成，以打破模态壁垒实现深层知识交互。早期级联架构缺乏双向交互，原生自回归模型虽确立 Any-to-Any 范式却暴露出理解与生成在表征空间中的根本冲突。本文通过构建涵盖架构选择、训练策略与模态集成的三维分类体系，系统梳理了从离散 Token 化到混合扩散目标的演进路径，并指出当前领域缺乏量化协同效应的闭环评估标准。该综述提供了清晰的领域认知地图，但其对“伪统一”现象的归因仍停留在架构层面，未深入表征解耦的理论边界。

】

---

【Towards Visually Grounded Multimodal Summarization via Cross-Modal Transformer and Gated Attention ｜面向视觉接地多模态摘要的跨模态Transformer与门控注意力

研究机构：澳大利亚麦考瑞大学

作者：Abid Ali、Diego Molla-Aliod、Usman Naseem

论文原文见 [arXiv](https://arxiv.org/abs/2605.11753)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.11753)

> 多模态摘要生成旨在从图文混合文档中产出简洁摘要，但现有模型常将视觉特征浅层注入语言模型，导致跨模态语义对齐薄弱且图像选择冗余。本文切入点在于将图像子集选择视为摘要生成的内生组件而非后处理步骤，通过深度视觉处理器实现层对齐融合，并借助DPP教师蒸馏轻量级选择器。该框架在MSMO基准上实现了文本质量持平SOTA且视觉选择质量显著优于基线的效果，但其对“互补性”与“相关性”的区分能力仍存疑。

】

---

【Trident: Self-Supervised Preference Alignment via Triplet Regularization ｜三元组正则化自监督偏好对齐

研究机构：浙江大学、上海交通大学

作者：Yingnan Guo、Kejia Chen、Xiaofeng Zhang 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2c896ca5aa0e)

> 多模态大语言模型在自监督场景下难以获取高质量偏好数据，标准直接偏好优化（Direct Preference Optimization, DPO）因自动生成的“优选”响应未必优于“劣选”响应而陷入监督噪声。Trident 通过引入中性锚点将二元偏好扩展为三元组结构，并设计自适应边际正则化目标，在无外部反馈条件下实现了对幻觉的有效抑制。该方法以极少的自生成数据达到了与依赖大规模人工标注或强模型反馈的方法相当的性能，但其对复杂视觉语义理解的提升能力仍存疑。

】

---

【Two Heads Are Better Than One: Audio-Visual Speech Error Correction with Dual Hypotheses ｜双假设生成式纠错：在语言空间解耦视听模态

研究机构：韩国科学技术院

作者：Sungnyun Kim、Kangwook Jang、Sungwoo Cho 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.13281)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.13281)

> 导读 视听语音识别（AVSR）在噪声环境下依赖视觉线索补偿音频退化，但现有生成式错误纠正（GER）框架多采用特征级融合，导致单模态噪声污染统一表征，限制了纠错上限。本文切入点在于将模态融合延迟至语言空间，利用独立ASR与VSR模型生成双路假设，由大语言模型（LLM）进行组合推理。具体做法是提出DualHyp框架，并引入RelPrompt机制提供时间对齐的模态可靠性信号以引导LLM动态选择可信源。该范式在LRS2噪声基准上实现了显著的错误率降低，但其性能高度依赖VSR头的质量，且在真实世界复杂场景下的泛化能力尚待验证。

】

---

【UnAC: Adaptive Visual Prompting with Abstraction and Stepwise Checking for Complex Multimodal Reasoning ｜自适应视觉提示与渐进式检查框架

研究机构：美国东北大学

作者：Yifan Wang、Yun Fu

论文原文见 [arXiv](https://arxiv.org/abs/2605.03950)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.03950)

> 多模态大语言模型（Large Multimodal Models, LMMs）在处理复杂视觉推理任务时，常因细粒度感知缺失与中间步骤逻辑断裂导致最终答案错误。现有纯文本提示方法难以有效分解图像信息，而单一视觉标记提示又缺乏对推理过程的验证机制。UnAC通过结合问题条件化的自适应视觉提示、图像信息抽象及逐步自我检查，构建了一个无需训练的多模态提示框架。该框架在多个基准上提升了模型表现，但其增益高度依赖骨干模型的底层推理能力，且对特定分割工具的依赖限制了其通用性。

】

---

【Uncertainty-Calibrated Elastic Alignment for Multimodal Sentiment Analysis with Missing Modalities ｜不确定性校准弹性对齐

研究机构：武汉大学

作者：Kang He、Yuzhe Ding、Rao Fu 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_447194c7ee00)

> 多模态情感分析在真实场景中常遭遇模态动态缺失，现有确定性补全方法将语义歧义强行拟合为单一目标，导致特征空间扭曲与决策边界漂移。EASE 将补全重构为条件密度估计，利用学习到的方差信号在再生核希尔伯特空间中动态调节对齐强度，并引入跨视图预测一致性约束以稳定判别逻辑。该方法在缺失率高达 0.9 时仍保持优于基线的性能下限，但其弹性机制是否会在完整数据下牺牲精度，论文未提供直接对照。

】

---

【UniCM: A Unified Consistency Model For Efficient Multimodal Generation and Understanding ｜统一一致性模型

研究机构：上海交通大学、同济大学

作者：Chenkai Xu、Xu Wang、Zhenyi Liao 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_aeae2be8eca5)

> 统一多模态模型旨在单一架构内同时处理图像生成与文本理解，但现有方案依赖迭代去噪或自回归解码，导致推理延迟高企。本文切入点在于建立跨模态的统一去噪轨迹，使一致性模型能直接映射任意中间状态至终点，从而跳过中间步骤。通过定义基于自回归并行解码的文本去噪路径与基于掩码扩散的图像去噪路径，并施加统一的一致性蒸馏目标，实现了少步高效推理。该方案在保持接近基线性能的同时大幅降低延迟，但其生成质量在部分指标上未超越专用扩散模型，且缺乏对内部表征协同效应的验证。

】

---

【Unveiling Inherent Visual Grounding in Multimodal LLMs for Text-Rich Images ｜文档视觉文本定位的注意力内化

研究机构：美国纽约州立大学布法罗分校、Adobe研究院

作者：Shijie Zhou、Jihyung Kil、Ming Li 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9fa29afda614)

> 文档问答中的视觉证据定位长期依赖外部OCR工具提供候选框，导致模型在稀疏文本或复杂图表场景下失效，且推理效率低下。Doc-AGround 摒弃了坐标生成与OCR依赖，直接利用多模态大语言模型（MLLMs）内部的多头自注意力（MHSA）作为定位信号。通过引入专用聚合token与基于全局相关性模式的注意力头加权机制，该方法在OCR-free设定下实现了SOTA性能。其价值在于证明了MLLM内部注意力已具备足够的细粒度定位潜力，但该方法对骨干模型预训练质量的依赖及在极端遮挡场景下的鲁棒性仍存疑。

】

---

【VAUQ: Vision-Aware Uncertainty Quantification for LVLM Self-Evaluation ｜视觉感知不确定性量化

研究机构：美国威斯康星大学麦迪逊分校、新加坡南洋理工大学

作者：Seongheon Park、Changdae Oh、Hyeong Kyu Choi 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.21054)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.21054)

> 大型视觉语言模型（LVLM）在生成答案时，常因语言先验主导而忽略视觉证据，导致高置信度的幻觉输出。现有基于文本的自评估方法（如熵、语义一致性）在反事实图像上失效，无法区分“流畅但错误”与“视觉接地且正确”的响应。本文提出VAUQ，通过计算移除核心视觉区域后的预测熵变化，显式量化视觉证据对模型置信度的贡献。该方法无需训练且无需外部评估器，在反事实场景下将自评估AUROC提升13.3%，但依赖注意力机制定位关键区域，其鲁棒性边界尚待验证。

】

---

【VChain: Chain-of-Visual-Thought for Reasoning in Video Generation ｜视觉思维链驱动的推理增强视频生成

研究机构：新加坡南洋理工大学

作者：Ziqi Huang、Ning Yu、Gordon Chen 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.05094)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.05094)

> 导读 视频生成模型在合成复杂动态场景时，常因缺乏对物理规律和因果逻辑的显式建模，导致生成的视频在状态转换上出现逻辑断裂或物理违和。现有方法多依赖大规模数据驱动的黑盒学习，难以在推理阶段灵活注入高层语义约束，且全量微调成本高昂。VChain 提出了一种推理时微调框架，利用多模态大模型生成稀疏的“视觉思维”关键帧，并通过低秩适配（LoRA）对预训练视频生成器进行轻量级对齐。该工作验证了将语言模型的因果推理能力转化为视觉监督信号的有效性，为视频生成的可控性提供了新路径，但其对多模态模型生成质量的依赖及评估基准的局限性仍需进一步审视。

】

---

【VET: Verifiable Execution Tracing for Reliable Text-to-SQL Generation ｜可执行执行追踪

研究机构：中国科学技术大学

作者：Dongyu Wang、Jingyu Li、Lan Zhang 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e8bed31a5c5c)

> 文本到SQL的核心困境在于自然语言意图与数据库结构间的语义鸿沟，导致模型生成语法正确但语义错误的查询。现有思维链方法依赖不可验证的文本推理，程序思维方法仅在最终阶段执行代码，均无法拦截中间步骤的逻辑错误。VET将推理过程重构为逐步执行的Python代码序列，每一步立即在真实数据库上运行并验证，确保中间状态与数据现实一致。该框架在免训练设置下显著提升了复杂查询的准确率，但其性能上限受限于骨干模型能力，且未解决推理延迟问题。

】

---

【VIDA: A Visual Intent-driven Design Assistant for Proactive Multimodal Clarification ｜视觉意图驱动的设计助手

研究机构：香港科技大学

作者：Yanshan Liu、Hongbo Zhang、Zhen Sun 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_dcba72e613fe)

> 在室内设计等专业咨询场景中，用户初始请求往往存在概念模糊与信息缺失，导致通用视觉语言模型（VLM）生成的澄清问题缺乏策略性且易产生视觉幻觉。现有澄清问题生成（Clarification Question Generation, CQG）方法多依赖文本模态或静态检索，无法在有限轮次内动态权衡关键约束的优先级。本文提出 VIDA，通过两阶段训练框架结合层级化强化学习奖励，使模型在生成澄清问题时严格遵循专家优先级协议。该框架在自建基准上将策略对齐分数提升 20.59%，但受限于单一领域数据规模，其跨领域泛化能力存疑。

】

---

【View-R1: Asymmetric Policy Optimization for Difficulty-Aware Multimodal Reinforcement Learning ｜非对称策略优化

研究机构：浙江大学、中国科学技术大学

作者：Minjie Hong、Zirun Guo、Jiabao Zhang 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_70d42800c22c)

> 多模态大模型（MLLMs）在强化学习后训练中常面临通用能力退化与推理链冗余的矛盾。现有组相对策略优化（GRPO）采用固定KL散度约束与均匀长度归一化，导致难样本探索受限且错误答案长度无限膨胀。本文提出非对称策略优化（APO），通过难度自适应散度整形与子最优轨迹复杂度正则化分别处理正负样本。该方法在3B/7B小模型上实现了推理性能提升与通用知识保留的平衡，但其缺乏过程级视觉监督的局限在复杂视觉任务中可能成为性能天花板。

】

---

【VisTW: Benchmarking Vision-Language Models for Taiwanese Mandarin in Taiwan ｜繁体中文视觉语言模型基准与正字法纯度评估

研究机构：国立台湾大学

作者：Zhi Rui Tam、Yung-Yu Shih、Yen-Wei Lee 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4d7292498fc5)

> 导读 现有视觉语言模型（VLM）评估体系严重依赖英语或简体中文，导致模型在繁体中文（Traditional Chinese, TC）语境下的能力处于未知状态。主流多语言基准缺乏对正字法一致性与地域文化深度的考量，无法捕捉模型在TC语境下的系统性失效。本文构建了首个TC多模态综合基准VisTW，并引入基于人类感知的简体字混入惩罚机制。该工作填补了TC评估空白，但其正字法惩罚是否掩盖了语义理解能力的真实差异，仍存疑。

】

---

【What Users Leave Unsaid: Under-Specified Queries Limit Vision-Language Models ｜查询欠规范对视觉语言模型性能的影响评估

研究机构：韩国延世大学、韩国高丽大学

作者：Dasol Choi、Guijin Son、Hanwool Lee 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.06165)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.06165)

> 真实用户视觉查询往往省略关键上下文，依赖图像传递隐含信息，而现有基准多采用结构化、显式提示，无法捕捉这一交互常态。这种“查询欠规范”（Query Under-specification）导致模型在真实场景中的表现远低于实验室基准，且现有检索增强手段无法弥补意图缺失。本文通过构建包含平行显式化重写的真实韩语社区基准，量化了欠规范对模型性能的具体折损，并揭示了检索与显式化的非对称收益。该工作揭示了基准难度与模型能力上限的非对应关系，但其结论受限于单一语言文化语境及小样本规模，跨语言泛化性仍需进一步验证。

】

---

【When Helpers Become Hazards: A Benchmark for Analyzing Multimodal LLM-Powered Safety in Daily Life ｜日常隐性风险识别基准

作者：Xinyue Lou、Xu Jinan、Jingyi Yin 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.04043)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_678ff3dbaf31)

> 多模态大语言模型（Multimodal Large Language Models, MLLMs）在作为日常助手时，常因无法关联视觉细节与潜在危害而误导用户做出危险决策，这一“安全感知失败”源于视觉与文本嵌入在安全语义空间中的分布差异。现有基准多聚焦于对抗性越狱攻击，缺乏对非对抗性、真实生活场景中隐性风险的量化评估，且传统“拒绝即安全”的评估范式无法区分模型是真正识别了风险还是仅触发了过度拒绝。本文构建了包含2,013个真实图文样本的SaLAD基准，并提出基于安全警告生成的评估框架，要求模型解释风险而非简单拒答。该工作揭示了现有模型在真实场景下的严重安全盲区，但其评估指标与对抗攻击防御指标不可直接比较，且未验证专用防御方法的有效性。

】

---

【WikiSeeker: Rethinking the Role of Vision-Language Models in Knowledge-Based Visual Question Answering ｜WikiSeeker：重构视觉语言模型在知识增强多模态推理中的角色

研究机构：中国科学院大学、中国科学院

作者：Yingjian Zhu、Xinming Wang、Kun Ding 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.05818)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.05818)

> 知识增强多模态推理（Knowledge-Augmented Multimodal Reasoning, KAMR）旨在解决多模态大语言模型在复杂视觉问答中因依赖内部参数化知识而导致的幻觉与知识滞后问题。现有方法普遍将视觉语言模型（Vision-Language Model, VLM）仅作为答案生成器，且检索键局限于图像，导致在视觉内容模糊时检索失效，且VLM在整合检索文本时表现弱于纯文本大语言模型（Large Language Model, LLM）。本文切入点在于重新定义VLM的角色，将其拆分为负责查询改写的Refiner与负责证据验证的Inspector，并引入强化学习优化查询生成。这一架构在静态检索框架内实现了性能跃升，但其单步检索机制与硬路由策略是否限制了其在长程推理任务中的潜力，仍存疑。

】

---

【Worldwide LiveVQA: Real-Time Visual Knowledge Seeking and Updating Across Languages ｜全球实时视觉知识获取与更新

研究机构：华中科技大学

作者：Xuanao Huang、Xingjia Liu、Zetong Zhou 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_18e7e87e4909)

> 多模态大语言模型（MLLMs）在视觉事实检索中面临“全球知识鸿沟”，即非英语地区的实时视觉信息被系统性排除在主流评估与训练数据之外。现有基准局限于静态英语语境，无法量化模型对跨语言、时效性视觉实体的感知能力。本文构建了首个动态更新的多语言视觉知识数据集 LIVEVQA-W，并揭示了搜索增强模型在低资源语言下的检索瓶颈。该工作填补了全球视觉事实评估的空白，但注入知识的跨语言泛化能力依然脆弱。

】

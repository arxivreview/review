# ICLR2026 · 医学与生物AI方向论文汇编

> 本方向共 101 篇（ICLR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【_CodeBrain_ : BRIDGING DECOUPLED TOKENIZER AND MULTI-SCALE ARCHITECTURE FOR EEG FOUNDATION MODEL ｜CodeBrain：基于解耦分词器与多尺度架构的脑电基础模型

研究机构：新加坡国立大学、新加坡南洋理工大学

作者：Jingying Ma、Feng Wu、QIKA LIN 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_6889847)

> 导读 脑电基础模型（EEG Foundation Models, EFMs）旨在从非平稳神经信号中提取跨任务通用表示，以突破手工特征在临床场景下的泛化瓶颈。现有方法依赖单一向量量化码本与全连接Transformer，导致表示缺乏神经生理学可解释性，且无法高效建模脑信号的小世界拓扑结构。CodeBrain通过时频解耦分词器与状态空间模型（State Space Model, SSM）变体架构，在保留信号细节的同时实现了Token级别的语义对齐。该模型在异常检测与事件检测上表现优异，但其可解释性证据仅基于激活统计，缺乏因果推断验证，且未解决跨被试身份混淆问题。

】

---

【A Scalable Distributed Framework for Multimodal GigaVoxel Image Registration ｜面向GigaVoxel医学图像的分布式融合配准框架

研究机构：美国宾夕法尼亚大学

作者：Rohit Jena、Vedant Zope、Pratik Chaudhari 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.25044)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.25044)

> 可变形医学图像配准旨在通过估计密集非线性空间变换，将移动图像与固定图像在解剖结构上对齐，其核心价值在于支撑肿瘤监测、多模态融合及手术导航等临床决策。随着超高分辨率成像技术突破，现有算法因高带宽内存（HBM）瓶颈无法处理数十亿参数级问题，导致临床与科研数据规模与计算能力严重脱节。本文通过IO感知融合内核与分布式张量分片技术，将配准问题规模扩展至单卡64倍并支持任意GPU数量。该框架在100微米人脑体积上实现了分钟级多模态配准，但其在标准临床分辨率下的精度是否优于专用深度学习模型仍存疑。

】

---

【A STRUCTURED, TAGGED, AND LOCALIZED VISUAL - QUESTION ANSWERING DATASET WITH FULL SEN TENCE ANSWERS AND SCENE GRAPHS FOR CHEST X- RAY IMAGES ｜结构化胸片视觉问答数据集与场景图构建

研究机构：德国慕尼黑工业大学、英国帝国理工学院

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_34819630)

> 医学视觉问答（Med-VQA）面临的核心瓶颈在于训练数据缺乏细粒度定位与结构化元数据，导致模型难以实现可解释的视觉接地。现有数据集如 VQA-RAD 和 SLAKE 规模小且答案简略，无法支撑大规模预训练与复杂推理。本文切入点在于利用大语言模型（LLM）从放射学报告中自动提取场景图，进而生成包含边界框和标签的大规模结构化问答对。通过构建 42M 规模的 CXR-QBA 数据集并定义结构化 VQA 任务，本文验证了数据丰富度对模型接地能力的提升，但其评估局限于自建基准，跨域泛化能力尚存疑。

】

---

【ANATOMY AWARE REPRESENTATION LEARNING FOR MEDICAL ULTRASOUND ｜解剖感知表征学习

研究机构：韩国科学技术院

作者：Seok-Hwan Oh、Myeong-Gee Kim、Guil Jung 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_39960393)

> 超声影像因斑点噪声与器官特异性导致通用视觉模型失效，现有自监督方法无法区分不同解剖结构的关键特征。本文切入点在于将解剖上下文直接嵌入特征提取过程，而非仅依赖数据规模。通过解剖条件化变形Transformer与混合自监督目标，实现跨器官的通用表征。该方法在多项下游任务中超越自然图像预训练基线，但其表征质量是否足以替代专用分割网络，仍存疑。

】

---

【ARE EEG FOUNDATION MODELS WORTH IT? COMPARATIVE EVALUATION WITH TRADITIONAL DECODERS IN DIVERSE BCI TASKS ｜脑电基础模型效能实证审计

研究机构：比利时鲁汶大学、中国科学院

作者：Liuyin Yang、Qiang Sun、Ang Li 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_95805392)

> 脑电基础模型旨在通过大规模自监督预训练获取跨任务通用表示，以解决传统解码器在异构范式下需单独训练的问题。然而，现有研究多缺乏对经典非神经基线的严格统计对比，且常忽略数据稀缺场景下的性能衰减。本文通过构建六维评估协议，系统对比了基础模型与经典解码器，并提出了仅使用掩码自编码（MAE）预训练的ST-EEGFormer基线。该工作揭示了预训练收益在微调中常被覆盖的现象，挑战了“复杂预训练目标优于简单重建”的领域共识，但受限于下游数据集规模，其结论在超大规模数据场景下的普适性尚存疑。

】

---

【Assembling the Mind's Mosaic: Towards EEG Semantic Intent Decoding ｜语义意图解码（SID）：基于集合匹配的脑电信号到自然语言生成

研究机构：浙江大学、美国德克萨斯大学奥斯汀分校

作者：Jiahe Li、Junru Chen、Fanqi Shen 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.20447)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.20447)

> 脑机接口（BCI）通信的核心瓶颈在于如何从低信噪比的神经信号中还原出连贯且可解释的自然语言，而非仅仅识别离散类别。现有概念解码方法受限于固定标签集的封闭性，或端到端生成模型的黑盒特性，难以兼顾表达力与可解释性。本文提出语义意图解码（SID）框架，将神经信号建模为可变长的语义单元集合，并通过二分匹配与大型语言模型（LLM）引导的受控生成实现开放词汇下的句子重建。该框架在临床立体脑电图（SEEG）及多语言脑电（EEG）数据集上显著优于基线，但其对单被试数据的依赖及缺乏跨被试泛化验证，限制了其在通用BCI场景中的直接适用性。

】

---

【ATPO: Adaptive Tree Policy Optimization for Multi-Turn Medical Dialogue ｜自适应树策略优化

研究机构：中国科学技术大学、阿里巴巴集团

作者：Ruike Cao、Shaojie Bai、Fugen Yao 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.02216)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.02216)

> 医疗对话中用户初始信息往往残缺，模型需主动追问以获取关键事实，但现有强化学习（RL）方法在处理多轮长程任务时面临信用分配模糊与价值估计不稳定的双重困境。本文提出自适应树策略优化（ATPO），通过不确定性驱动的树搜索动态分配采样预算，解决传统线性轨迹采样在长程交互中效率低下的问题。该方法结合Bellman误差与Q值方差复合指标指导节点扩展，并利用KV缓存复用提升训练吞吐量。实验表明ATPO在多个医疗对话基准上显著优于PPO与GRPO基线，但其仅依赖最终答案正确性作为奖励信号，对推理过程逻辑性的约束能力存疑。

】

---

【ATTTOK: MARRYING ATTRIBUTE TOKENS WITH GEN - ERATIVE PRE TRAINED VISION-LANGUAGE MODELS TOWARDS MEDICAL IMAGE UNDERSTANDING ｜属性令牌（AttTok）：生成式医学视觉-语言模型的判别力重构

研究机构：香港科技大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_20516174)

> 导读 生成式预训练视觉-语言模型（GPTv）在医学影像诊断中面临临床属性语义坍缩与视觉特征纠缠的双重困境，现有指令微调范式无法区分语义相近但病理意义截然不同的疾病。本文切入点在于将临床属性离散化为特殊令牌，通过属性中心嵌入库锚定多模态表示。具体做法是引入属性中心交叉注意力（ACC）适配器打破单向信息流，并设计属性中心匹配（ACM）损失强制跨模态对齐。该方案在2D多模态分类与视觉问答任务上显著提升了判别精度，但其在3D容积数据及极端分布偏移下的泛化能力尚存疑。

】

---

【Autoregressive Visual Decoding from EEG Signals ｜自回归视觉解码

研究机构：中国科学院、中国科学院大学

作者：Sicheng Dai、Hongwang Xiao、Shan Yu 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.22555)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.22555)

> 脑电视觉解码旨在从低信噪比信号中还原图像内容，核心难点在于弥合脑电信号与高维语义空间间的分布鸿沟。现有主流方案依赖多阶段扩散模型，存在误差累积与计算开销过大的问题，难以满足脑机接口的实时性需求。本文提出AVDE，通过预训练编码器微调与自回归“下一尺度预测”策略，以10%的参数量实现了检索与重建性能的双重提升。该方法在效率与精度的权衡上提供了新解法，但其绝对精度仍低于最新领域基准，且对预训练权重的依赖限制了其独立泛化能力的验证。

】

---

【BAYESIAN TEST-TIME ADAPTATION VIA DIRICHLET FEATURE PROJECTION AND GMM-DRIVEN INFERENCE FOR MOTOR IMAGERY EEG DECODING ｜贝叶斯测试时适应

作者：Huan LUO、Na Lu、Xiaopeng Wang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_21940808)

> 导读 运动想象脑机接口（Motor Imagery BCI, MI-BCI）在跨被试部署时面临神经信号分布偏移导致的性能崩溃，现有测试时适应（Test-Time Adaptation, TTA）方法要么依赖梯度更新引发灾难性遗忘，要么仅做浅层统计对齐无法捕捉深层特征漂移。本文切入点在于将适应过程从参数空间转移至概率分布空间，通过冻结预训练权重并在Dirichlet参数空间执行无梯度贝叶斯推断实现校准。具体做法是构建SincAdaptNet提取时序预测嵌入，投影为Dirichlet参数，再利用高斯混合模型（Gaussian Mixture Model, GMM）建模历史分布并与先验融合。该方法在SHU MI数据集上以64.06%准确率超越现有SOTA 5.16个百分点，但其增益是否完全归因于TTA机制而非骨干网络，以及Dirichlet投影在回归任务中的适用性，仍存疑。

】

---

【Benchmarking ECG FMs: A Reality Check Across Clinical Tasks ｜ECG基础模型的系统化基准测试：架构、效率与表征解耦

作者：M A Al-Masud、Juan Miguel Lopez Alcaraz、Nils Strodthoff

论文原文见 [arXiv](https://arxiv.org/abs/2509.25095)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.25095)

> 导读 心电图（ECG）基础模型（FMs）旨在通过大规模预训练实现跨任务迁移，但现有评估多局限于单一数据集或弱基线，导致无法区分真实能力与过拟合。本文切入点在于构建涵盖8种FM、12个数据集、26项临床任务的统一基准，通过控制变量解耦架构、规模与预训练策略的影响。核心方法包括引入轻量级SSM模型ECG-CPC，并采用冻结/线性评估与CKA表征分析。该工作确立了架构归纳偏置优于参数规模的结论，但其在缺乏语义监督下的零样本能力评估缺失，限制了其在罕见病场景的适用性判断。

】

---

【Beyond Classification Accuracy: Neural-MedBench and the Need for Deeper Reasoning Benchmarks ｜神经医学深度推理基准与双轴评估框架

研究机构：北京邮电大学、澳门大学

作者：Miao Jing、Mengting Jia、Junling Lin 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.22258)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.22258)

> 医疗视觉语言模型在标准分类基准上表现优异，却难以反映真实的临床诊断推理能力，这种“评估幻觉”掩盖了模型在复杂病例中的系统性缺陷。现有大规模基准侧重广度覆盖，缺乏对多模态整合与不确定性推理的深度考察，导致模型性能被高估。本文提出双轴评估框架，并构建包含120例专家标注神经科病例的Neural-MedBench，通过混合评分协议量化推理保真度。该工作揭示了当前模型在深度推理上的显著瓶颈，但零样本设置与单一专科聚焦限制了其结论的普适性。

】

---

【Beyond Hearing: Learning Task-agnostic ExG Representations from Earphones via Physiology-informed Tokenization ｜生理引导多频带分词

研究机构：韩国科学技术院、美国卡内基梅隆大学

作者：Hyungjun Yoon、Seungjoo Lee、Yu Yvonne Wu 等 14 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.20853)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.20853)

> 脑电（EEG）等电生理信号（ExG）分析长期受限于实验室场景的数据同质性与模型的任务特异性设计，导致跨任务泛化能力薄弱。现有基础模型虽通过大规模预训练提升通用性，但依赖昂贵设备且未解决频谱信息在单一宽频带下的丢失问题。本文通过耳挂式硬件采集自由生活数据，并提出生理引导多频带分词（PiMT）策略，将信号解构为12个固定生理频段令牌，结合双向Mamba编码器与重建预训练实现任务无关表示学习。该方案在自由生活多模态任务上表现优异，但在标准头皮EEG基准上未超越最新SOTA，其通用性边界尚存疑。

】

---

【Boosting Medical Visual Understanding From Multi-Granular Language Learning ｜多粒度语言学习

研究机构：美国华盛顿大学、美国杜克大学

作者：Zihan Li、Yiqing Wang、Sina Farsiu 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.15943)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.15943)

> 医学影像常同时呈现多种病理表现，且标注信息涵盖从粗粒度疾病类别到细粒度临床描述的不同层级，传统单标签单粒度对比学习难以捕捉这种层级结构。现有方法在处理多标签共存或跨粒度语义时，往往因强制单一对齐而导致表示坍缩。MGLL通过引入软标签监督、逐点约束及平滑KL散度，在统一框架内实现多标签与跨粒度的联合对齐。该方法作为即插即用模块提升了视觉基础模型的表征能力，但其对文本噪声的鲁棒性及在3D体数据上的适用性尚存疑。

】

---

【CANCER-MYTH: EVALUATING LARGE LANGUAGE - MODELS ON PATIENT QUESTIONS WITH FALSE PRE SUPPOSITIONS ｜癌症错误预设评估基准

研究机构：美国南加州大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_4780692)

> 医疗大语言模型（LLM）在真实患者咨询中面临的核心挑战是识别并纠正问题中隐含的错误预设，而非仅回答表面问题。现有静态基准如MedQA无法捕捉这种动态交互中的认知偏差，导致模型在临床应用中存在安全隐患。本文通过构建包含994个癌症谣言的对抗性数据集Cancer-Myth，量化了前沿模型在预设纠正上的能力缺口。该基准揭示了提示工程在提升安全性的同时会损害通用性能，但尚未提供有效的训练解决方案。

】

---

【CARE: Towards Clinical Accountability in Multi-Modal Medical Reasoning with an Evidence-Grounded Agentic Framework ｜临床问责医疗推理的证据接地智能体框架

研究机构：微软研究院、美国耶鲁大学

作者：Yuexi Du、Jinglu Wang、Shujie Liu 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.01607)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.01607)

> 医疗视觉问答（Med-VQA）的核心矛盾在于生成式模型的黑盒推理与临床决策所需的证据可追溯性之间的冲突。现有单模型方案将感知与推理耦合，导致细粒度视觉证据缺失与错误传播，而孤立接地模块又未将定位结果反馈至推理链。CARE 框架通过解耦实体提议、像素级分割与证据接地问答三个子任务，并引入动态协调器进行迭代审查，实现了显式证据链驱动的可问责推理。该框架在参数效率与临床可信性上表现突出，但其对专有协调器的依赖及推理延迟限制了本地化部署的可行性。

】

---

【CEREBRAGLOSS: INSTRUCTION-TUNING A LARGE VISION-LANGUAGE MODEL FOR FINE-GRAINED CLINICAL EEG INTERPRETATION ｜脑电临床解释的生成式范式

研究机构：上海交通大学、清华大学

作者：Wei Gu、Tianming Luo、Qiran Zhang 等 11 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_66396184)

> 临床脑电（EEG）解读长期依赖专家人工审阅，存在耗时、主观且信息覆盖不全的瓶颈，而现有计算模型仅能执行狭窄的分类任务，缺乏整体性解释能力。本文切入点在于利用大型视觉-语言模型（LVLM）的通用视觉表征，通过自动化数据生成管线构建细粒度指令数据集，将EEG波形解读转化为生成式对话任务。具体做法是基于Qwen2.5-VL-3B进行两阶段指令微调，并构建首个开放解释基准CerebraGloss-Bench。该工作验证了生成式范式在临床语义对齐上的可行性，但其依赖自动标注的噪声传播机制及长时程上下文缺失问题仍存疑。

】

---

【Constrained Diffusion for Protein Design with Hard Structural Constraints ｜硬约束下的蛋白质骨架生成：随机近端扩散框架

研究机构：美国弗吉尼亚大学、美国罗格斯大学

作者：Jacob K. Christopher、Austin Seamann、Jingyi Cui 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.14989)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.14989)

> 导读 蛋白质从头设计面临的核心矛盾是生成骨架的物理可行性与功能特异性难以同时满足，现有扩散模型虽能生成逼真结构，但常违反键长、角度等硬约束，导致大量候选需被丢弃。本文切入点在于将约束满足从软引导或后处理转为推理时的随机近端优化，通过“预测-近端修正-再噪”循环确保采样轨迹收敛至可行集。该方法结合ADMM分解局部与全局约束，在PDZ基序支架和空腔约束设计中实现了100%约束满足率。其价值在于提供了硬约束下的理论保证，但实验仅覆盖两类特定任务，且未报告采样效率，限制了其在实时设计场景中的适用性判断。

】

---

【Controlling Repetition in Protein Language Models ｜蛋白质语言模型生成中的病理性重复控制

研究机构：阿联酋扎耶德大学、沙特阿拉伯阿卜杜拉国王科技大学

作者：Jiahao Zhang、Zeqing Zhang、Di Wang 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.00782)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.00782)

> 蛋白质语言模型（PLM）在生成新序列时，常陷入“病理性重复”的失效模式，导致生成物结构不稳定且无功能。现有解码启发式方法虽能降低重复度，却往往以牺牲结构置信度为代价，缺乏针对蛋白质特性的解耦机制。本文提出效用控制对比引导（Utility-Controlled Contrastive Steering, UCCS），通过构建效用匹配但重复度差异显著的对比数据集，提取激活空间中的引导向量，在推理阶段干预生成过程。该方法在保持折叠可靠性的同时显著提升了序列多样性，但其在长序列及复杂结构约束下的泛化能力仍存疑。

】

---

【CRITIC–ADVISER–REVISER CYCLIC REFINEMENT: - TOWARDS HIGH-QUALITY EMR CORPUS GENERA TION WITH LLMS ｜基于多智能体循环精炼的合成电子病历生成

研究机构：清华大学、北京邮电大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_99546755)

> 临床电子病历（EMR）因隐私限制难以共享，合成数据是替代方案，但现有方法仅模仿真实记录分布，忽略了临床文档必须满足的完整性、一致性与医学正确性。本文指出直接模仿会继承真实数据中的错误，且通用大语言模型（LLM）生成存在分布偏差。LLM-CARe 通过 Critic-Adviser-Reviser 三智能体在语料、章节、文档三级进行循环精炼，在无真实文本提示下生成高质量 EMR。该方法在 192k 条记录上验证了质量与下游任务性能的提升，但其对罕见病分布的捕捉能力及计算成本未充分披露。

】

---

【CROSS-TIMESTEP: 3D DIFFUSION MODEL WITH - TRANS TEMPORAL MEMORY LSTM AND ADAPTIVE - PRIORI DECODING STRATEGY FOR MEDICAL SEG MENTATION ｜跨时间步记忆与自适应先验解码的3D扩散分割模型

研究机构：中南大学、北京大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_47222872)

> 3D医学影像分割面临多中心数据外观变异导致的模型泛化失效，传统扩散模型在从高噪声起始去噪时易发生“初始阶段崩溃”，导致结构重建失败。现有方法或聚焦生成任务，或采用事后融合策略，缺乏对去噪过程内部时间一致性的显式建模。本文提出Cross-Timestep框架，通过自适应先验解码策略（APDS）提供结构引导，并结合跨时间步记忆LSTM（tLSTM）实现证据累积。该方法在鼻咽癌分割任务上提升了鲁棒性，但其通用性受限于特定病理场景，且未验证其在非NPC数据集上的有效性。

】

---

【DCFOLD: EFFICIENT PROTEIN STRUCTURE GENERA TION WITH SINGLE FORWARD PASS ｜单步蛋白结构预测：双一致性蒸馏框架

研究机构：清华大学、华中科技大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_19490496)

> AlphaFold3 凭借原子级精度成为生物分子设计的基础模型，但其迭代式 Pairformer 与多步扩散机制导致推理耗时达分钟级，阻碍了高通量筛选与可微分闭环设计的落地。现有加速方案如 BindCraft 通过裁剪迭代次数牺牲精度，而标准一致性模型（Consistency Model, CM）在变长序列上训练不稳定。DCFold 通过联合约束扩散模块与 Pairformer 的一致性，并引入时域测地线匹配调度器，实现了单步预测。该框架在保持 AlphaFold3 精度水平的同时实现了 15 倍加速，但其 Best-case 精度的轻微下降是否影响高精度筛选场景，仍需进一步验证。

】

---

【DCFold: Efficient Protein Structure Generation with Single Forward Pass ｜单步蛋白结构生成：双一致性蒸馏与时间测地匹配

研究机构：清华大学、华中科技大学

作者：Zhe Zhang、Yuanning Feng、Yuxuan Song 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.17899)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.17899)

> AlphaFold3 将蛋白结构预测提升至原子级精度，但其迭代式 Pairformer 与多步扩散模块导致推理耗时达分钟级，阻碍了高通量虚拟筛选与可微分设计任务的落地。现有加速方案如 BindCraft 通过手动减少迭代次数牺牲精度，而标准一致性模型（Consistency Model, CM）在变长序列上因欧氏距离配对失效导致训练崩溃。本文提出 DCFold，通过双一致性框架联合压缩扩散与 Pairformer 迭代，并引入时间测地匹配（Temporal Geodesic Matching, TGM）调度器稳定变长序列训练，实现 15 倍加速且保持 AlphaFold3 级精度。该工作验证了单步生成在结构预测中的可行性，但其对长序列动态稳定性的证据仍显薄弱。

】

---

【DISENTANGLING THE FACTORS OF CONVERGENCE BETWEEN BRAINS AND DINOV3 ｜解耦脑-模型表征收敛的驱动因素

研究机构：Meta AI

作者：Joséphine Raugel、Marc Szafraniec、Huy Vo 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_36967988)

> 脑-深度网络表征对齐旨在量化生物大脑与人工网络内部表征的几何相似性，但现有研究多基于预训练模型，无法区分架构、数据与训练量对收敛的独立贡献。本文通过系统训练DINOv3变体，独立操纵模型规模、图像类型与训练步数，利用fMRI与MEG数据评估对齐的时空组织特性。该方法揭示了类脑表征涌现的特定时间顺序，即模型先对齐感觉皮层，后对齐前额叶。这一因果解耦框架为理解神经计算普遍性提供了实证基础，但其线性映射假设可能低估深层非线性对齐。

】

---

【Distilling and Adapting: A Topology-Aware Framework for Zero-Shot Interaction Prediction in Multiplex Biological Networks ｜多路复用生物网络零样本交互预测

作者：Alana Deng、Sugitha Janarthanan、Yan Sun 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.06618)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.06618)

> 生物系统交互预测长期受困于单图层模型丢弃关系异质性与零样本泛化能力缺失的矛盾。现有图神经网络依赖邻域拓扑，无法预测未见实体的交互，且难以融合序列语义与网络结构。CAZI-MBN通过统一图分词器对齐拓扑与序列，利用教师-学生知识蒸馏将拓扑知识转移至仅依赖序列的学生模型，实现无邻域信息下的零样本预测。该框架在五个新构建基准上显著优于基线，但其对层间一致性假设的依赖及缺乏机制可解释性，限制了其在临床转化中的直接应用。

】

---

【Doctor-R1: Mastering Clinical Inquiry with Experiential Agentic Reinforcement Learning ｜经验驱动的智能体强化学习

研究机构：清华大学

作者：Yunghwei Lai、Kaiming Liu、Ziyue Wang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.04284)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.04284)

> 临床决策支持系统需解决在信息不完整环境下进行多步动态推理的问题，现有模型在静态基准上表现优异，但缺乏主动获取证据与情感沟通的能力。DOCTOR-R1 通过构建多智能体交互环境，结合双层奖励架构与经验库检索，训练模型掌握战略询问与共情沟通。该方法在 HealthBench 上以 8B 参数规模超越多个专有模型，验证了增强询问能力可提升决策准确性，但其依赖 LLM 评估器的可靠性仍存疑。

】

---

【DU AL-KERNEL ADA P T E R: EXPANDING SPATIAL HORIZONS FOR DATA-CONSTRAINED MEDICAL IMAGE ANALYSIS ｜双核适配器：数据受限医学影像中的空间感受野扩展

研究机构：南京大学、英国布里斯托大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_26584757)

> 医学影像标注成本高昂且隐私法规严格，导致下游任务常处于极端低数据状态。现有参数高效微调方法在此场景下表现不稳定，甚至劣于线性探测。本文通过系统分析发现标准适配器在低数据下有效感受野收缩是性能退化的主因，并提出双核适配器（Dual-Kernel Adapter, DKA）以显式扩大空间上下文。该模块在多个基准上刷新了低数据与全数据下的性能上限，但其对域偏移的鲁棒性尚未验证。

】

---

【ECHO: Toward Contextual Seq2Seq Paradigms in Large EEG Models ｜解码器中心范式：ECHO 的序列到序列脑电建模

研究机构：新加坡南洋理工大学、中国科学院

作者：Chenyu Liu、Yuqiu Deng、Tianyu Liu 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.22556)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.22556)

> 大型脑电模型（Large EEG Models, LEMs）旨在通过自监督预训练提取通用神经表示，但现有架构普遍存在“编码器强、解码器弱”的结构性失衡，导致通用表示难以转化为可靠预测。本文指出，传统轻量级分类器迫使编码器在微调时牺牲预训练知识，而将大语言模型（LLM）作为解码器仅将映射转移至文本空间，未能解决时序动态与静态语义的错位。ECHO 提出解码器中心（Decoder-Centric）范式，将 EEG 建模重构为序列到序列（seq2seq）任务，通过引入支持样本实现上下文学习（In-Context Learning, ICL）。该范式在多项基准上超越了单任务基线，但其优势是否源于范式本身而非数据规模，仍需进一步剥离验证。

】

---

【EFFICIENT PREDICTION OF LARGE PROTEIN COM - PLEXES VIA SUBUNIT-GUIDED HIERARCHICAL RE FINEMENT ｜层级化亚基引导的大规模蛋白复合物结构预测

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_5197861)

> 大规模蛋白复合物结构预测面临Transformer架构内存随Token数二次方增长的瓶颈，导致端到端推理在数千Token规模下不可行。现有分治方法依赖专家定义亚基或仅处理成对交互，忽略了多体协同效应且自动化程度低。本文利用预测对齐误差（PAE）矩阵自动识别刚性亚基与稀疏界面，通过“粗粒度成对预测-局部界面精修-置信度加权组装”的层级流程，在保持AlphaFold3精度水平的前提下，将可预测规模扩展至5000+ Token，并降低约40%的GPU内存占用。该方法有效解决了内存瓶颈，但层级分解是否引入累积误差导致全局精度微降，仍需更严格的对照实验验证。

】

---

【FAST PROTEOME-SCALE PROTEIN INTERACTION RETRIEVAL VIA RESIDUE-LEVEL FACTORIZATION ｜残基级因子化实现全基因组蛋白互作检索

研究机构：加拿大蒙特利尔大学

作者：Jianan Zhao、Zhihao Zhan、Narendra Chaudhary 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_23590722)

> 全基因组规模的蛋白质-蛋白质相互作用（Protein-Protein Interaction, PPI）预测旨在从约两万个蛋白中筛选出潜在互作对，但传统成对推理方法因计算复杂度呈二次方增长而难以落地。现有高精度模型需对每个蛋白对进行联合编码，导致全基因组筛选耗时数月，而简单嵌入检索又丢失了残基级交互细节。RaftPPI通过高斯核近似与低秩注意力将残基交互因子化为单蛋白嵌入，实现了分钟级的全基因组检索。该方法在严格控制的基准上达到了分类与检索性能的最优平均表现，但其仅依赖序列模态的设计在构象依赖型互作中的泛化能力存疑。

】

---

【FETAL-GAUGE: A Benchmark for Assessing Vision-Language Models in Fetal Ultrasound ｜胎儿超声视觉语言模型基准

研究机构：阿联酋扎耶德大学

作者：Hussain Alasmawi、Numan Saeed、Mohammad Yaqub

论文原文见 [arXiv](https://arxiv.org/abs/2512.22278)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.22278)

> 胎儿超声解读面临操作者依赖与数据稀缺的双重约束，现有通用视觉语言模型（Vision-Language Model, VLM）缺乏针对该模态的标准化评估体系，导致其临床可用性无法量化。本文切入点在于构建首个大规模胎儿超声VQA基准，通过整合13个公开数据集形成统一评测框架。具体做法是将异构标注统一为多选题格式，系统评估15个SOTA VLM在五项临床任务上的表现。该基准揭示了当前VLM在细粒度空间推理与域适应上的根本缺陷，但受限于多选题格式，其结论对开放生成场景的泛化性存疑。

】

---

【FLEXRIBBON: JOINT SEQUENCE AND STRUCTURE PRETRAINING FOR PROTEIN MODELING ｜FlexRibbon：序列-结构双向耦合预训练

研究机构：湖南大学、印度数学科学研究所

作者：Jianwei Zhu、Yu Shi、Ran Bi 等 23 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_44190220)

> 蛋白质基础模型长期面临序列语义与三维几何信息割裂的困境，导致在抗体CDR等高突变、低同源区域预测失效。现有方法或依赖MSA进化信号，或将结构作为单向辅助输入，无法捕捉柔性界面的双向依赖。FlexRibbon通过掩码语言建模与扩散去噪的联合训练，实现了无MSA条件下的序列-结构双向映射。该模型在12项任务上取得SOTA，但非等变架构在复杂多链复合物中的几何一致性仍存疑。

】

---

【From Conversation to Query Execution: Benchmarking User and Tool Interactions for EHR Database Agents ｜电子健康记录交互式查询基准

研究机构：韩国科学技术院

作者：Gyubok Lee、Woosog Chay、Heeyoung Kwak 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.23415)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.23415)

> 临床数据访问面临用户提问模糊与数据库术语不匹配的双重障碍，传统静态文本转SQL基准无法评估智能体在动态对话中消解歧义与调用工具的能力。EHR-ChatQA通过构建包含LLM模拟用户与验证器的交互式环境，首次量化了智能体在随机对话路径下的鲁棒性缺陷。该基准揭示了当前最优模型在“至少一次成功”与“五次全部成功”间存在高达60%的性能鸿沟，证明了现有智能体在安全关键场景中的不可靠性，但其评估局限于单智能体架构，未验证多智能体协作对一致性的增益。

】

---

【Functional MRI Time Series Generation via Wavelet-Based Image Transform and Spectral Flow Matching for Brain Disorder Identification ｜双谱流匹配生成fMRI时间序列

研究机构：澳大利亚莫纳什大学、沙特阿拉伯阿卜杜拉国王科技大学

作者：Hwa Hui Tew、Junn Yong Loo、Leong Yu 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.30387)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.30387)

> 功能磁共振成像（fMRI）数据稀缺且非平稳，现有生成模型难以同时捕捉BOLD信号的多尺度振荡与生理动态。传统方法局限于功能连接（FC）矩阵或原始时间域，忽略了跨频率交互与瞬态网络状态。本文提出双谱流匹配（DSFM），通过离散小波变换（DWT）与离散余弦变换（DCT）构建双谱图像，并在DCT域执行流匹配以高效生成类条件BOLD信号。该方法在MDD分类任务上取得70.84%准确率，但固定数学变换是否限制了对个体特异性神经动力学的捕捉，仍存疑。

】

---

【GALAX: Graph-Augmented Language Model for Explainable Reinforcement-Guided Subgraph Reasoning in Precision Medicine ｜图增强语言模型的可解释强化子图推理

研究机构：美国圣路易斯华盛顿大学、Hugging Face

作者：Heming Zhang、Di Huang、Wenyu Li 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.20935)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.20935)

> 精准医学中从多组学数据到治疗靶点的预测长期缺乏机制层面的可解释性，现有方法要么忽略拓扑结构，要么依赖静态检索导致推理链不可靠。GALAX 的切入点在于将子图构建视为强化学习序列决策，利用预训练图神经网络作为过程奖励模型，在无显式标签条件下监督中间步骤的生物合理性。该方法通过图过程奖励模型（Graph Process Reward Model, GPRM）引导大语言模型（Large Language Model, LLM）动态生成患者特异性信号子图，实现靶点预测与机制解释的统一。其价值在于提供了无标签的过程级监督框架，但受限于自建基准的封闭性与预训练图模型偏差的继承风险。

】

---

【GARLIC: GRAPH ATTENTION BASED RELATIONAL - LEARNING OF MULTIVARIATE TIME SERIES IN INTEN SIVE CARE ｜图注意力关系学习用于重症监护多变量时序

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_85176564)

> 临床时序预测面临不规则采样与可解释性缺失的双重困境，传统插值扭曲生理动态，后验解释无法提供病理逻辑。GARLIC 通过端到端学习的时间滞后图结构，将缺失值建模与传感器依赖捕捉统一，同时生成内置归因。该方法在 MIMIC-III 等基准上刷新了精度记录，但其泛化能力受限于单模态结构化数据，未涵盖临床文本等异构信息。

】

---

【GEOMMOTIF: A BENCHMARK FOR ARBITRARY GEOMETRIC PRESERVATION IN PROTEIN GENERATION ｜几何保持基准

研究机构：俄罗斯高等经济大学

作者：Pavel Strashnov、Andrey Shevtsov、Viacheslav Meshchaninov 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_26344111)

> 蛋白质生成模型在基序支架化任务中常因混淆几何精度与功能约束而难以诊断失败根源。现有基准如MotifBench聚焦已知功能位点，无法区分模型是缺乏几何保持能力还是化学兼容性不足。本文通过从PDB随机采样非功能片段，构建了57个纯几何保持任务，并采用SUN指标统一评估序列与结构模型。该基准揭示了架构间的根本性能鸿沟，但样本量较小且缺乏湿实验验证，其结论的普适性仍存疑。

】

---

【Glance and Focus Reinforcement for Pan-cancer Screening ｜全癌CT筛查中的强化学习视觉搜索

研究机构：香港科技大学、德国慕尼黑工业大学

作者：Linshan Wu、Jiaxin Zhuang、Hao Chen

论文原文见 [arXiv](https://arxiv.org/abs/2601.19103)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.19103)

> 全癌CT筛查面临极端前景-背景不平衡与冗余计算的双重瓶颈，现有滑窗推理方法在效率与假阳性控制上难以兼顾。GF-Screen借鉴放射科医生“扫视-聚焦”策略，通过强化学习优化非可微的区域选择操作，实现病灶定位与分割的协同。该方法在FLARE25挑战赛中显著超越基线，但外部数据集泛化能力仍受限于域间差异。其价值在于将RL引入医学影像搜索，但奖励函数的二值化设计是否牺牲了分割精度，仍需进一步审视。

】

---

【GRAM-DTI: ADAPTIVE MULTIMODAL REPRESENTA TION LEARNING FOR DRUG–TARGET INTERACTION PREDICTION ｜基于体积对齐与自适应模态丢弃的药物靶点相互作用预测

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_504363)

> 药物靶点相互作用（DTI）预测旨在通过计算手段解析分子结合机制，以缓解实验筛选的高昂成本。现有方法多依赖SMILES与蛋白序列的双模态输入，忽略了分子文本、层级分类等丰富信息，且在模态质量不均时易受主导模态干扰。本文提出GRAM-DTI，通过扩展体积损失实现四模态高阶对齐，并引入基于梯度的自适应模态丢弃机制。该方法在冷启动场景下显著优于基线，但其评估数据集与主流基准不重叠，泛化能力的普适性仍存疑。

】

---

【GRAM-DTI: adaptive multimodal representation learning for drug target interaction prediction ｜基于体积损失的多模态药物靶点相互作用预测

作者：Feng Jiang、Amina Mollaysa、Hehuan Ma 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.21971)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.21971)

> 药物靶点相互作用（DTI）预测旨在从海量化学与蛋白空间中筛选候选对，但现有模型多依赖SMILES-蛋白单模态对，难以利用分子文本、层级分类等丰富信息，且在冷启动场景下泛化能力不足。本文切入点在于指出成对对比学习无法捕捉多模态间的高阶依赖，且静态融合易受低信息量模态干扰。GRAM-DTI通过扩展体积损失至四模态联合对齐，并引入梯度感知的自适应模态丢弃机制，构建了更鲁棒的统一表征空间。该方法在冷启动场景下显著优于基线，但其性能增益是否完全源于预训练规模而非架构创新，仍需更严格的控制变量实验验证。

】

---

【GREATER THAN THE SUM OF ITS PARTS: BUILDING SUBSTRUCTURE INTO PROTEIN ENCODING MODELS ｜子结构感知蛋白表征学习

研究机构：美国麻省理工学院、美国哈佛大学

作者：Robert Calef、Arthur Liang、Manolis Kellis 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_6610016)

> 蛋白质由进化保守的模块化子结构组成，但主流蛋白语言模型（PLM）仅以残基或全局嵌入为单元，忽略了这一层级组织。现有结构整合方法聚焦于原子坐标或全局折叠，缺乏对跨蛋白保守功能模块的监督。本文提出 Magneton 环境及子结构微调（Substructure-Tuning）策略，通过池化残基嵌入并分类保守子结构，将模块化知识蒸馏进预训练模型。该方法在功能预测任务上带来一致增益，并提升了未见子结构类型的表征一致性，但其效果易被下游任务微调抵消，且未触及原子级细节。

】

---

【h-MINT: Modeling Pocket-Ligand Binding with Hierarchical Molecular Interaction Network ｜层级分子交互网络

研究机构：美国伊利诺伊大学厄巴纳-香槟分校、加拿大麦吉尔大学

作者：Yanru Qu、Yijie Zhang、Wenjuan Tan 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.23134)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.23134)

> 蛋白-配体结合预测的核心瓶颈在于分子表征无法完整保留决定结合特异性的化学上下文，如芳香性、电荷与立体化学。现有原子级图模型丢失高阶化学信息，而传统碎片化方法因强制离散划分破坏芳香环完整性。本文通过允许原子重叠的分词策略与层级等变网络，在保留完整化学环境的同时实现多尺度交互建模。该方案在LBA基准上取得0.660 Pearson相关系数，但其在PDBbind上的表现与当前SOTA存在显著差距，其表征优势是否可泛化至更复杂的结构多样性场景存疑。

】

---

【H-MINT: MODELING POCKET-LIGAND BINDING WITH HIERARCHICAL MOLECULAR INTERACTION NETWORK ｜重叠碎片分词与层级交互网络

研究机构：美国伊利诺伊大学厄巴纳-香槟分校、加拿大麦吉尔大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_32364641)

> 蛋白-配体结合预测的核心瓶颈在于原子级图表示难以捕捉高阶化学环境，如立体化学与共轭效应。现有碎片化方法因强制离散划分导致芳香性断裂与电荷丢失，限制了模型对关键相互作用（如π-阳离子作用）的感知。本文提出允许原子重叠的OverlapBPE分词策略，并构建支持多对多映射的h-MINT层级网络，在PDBbind上将Pearson相关系数提升至0.640。该方案在表征层面解决了化学信息丢失问题，但其绝对精度仍低于依赖大规模预训练数据的基础模型，且未验证在动态构象下的鲁棒性。

】

---

【HEEGNet: Hyperbolic Embeddings for EEG ｜双曲嵌入脑电域适应

研究机构：日本理化学研究所、新加坡南洋理工大学

作者：Shanglin Li、Shiwen Chu、Okan Koç 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.03322)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.03322)

> 脑电解码长期受困于跨被试分布偏移，传统域适应方法在分布差异较大时性能显著退化。现有方案多依赖欧氏空间统计量对齐，难以捕捉脑信号固有的层级结构。HEEGNet 引入双曲几何，通过混合编码器与两阶段对齐策略，在小样本无监督场景下实现零样本迁移。该方法在视觉诱发电位与情绪识别任务上取得领先性能，但其泛化能力是否超越大规模预训练范式仍存疑。

】

---

【HFSTI-NET: HIERARCHICAL FREQUENCY SPATIAL - TEMPORAL INTERACTIONS FOR VIDEO POLYP SEG MENTATION ｜层级频空时交互网络

研究机构：深圳大学、香港理工大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_52907696)

> 视频息肉分割（VPS）旨在解决连续内窥镜视频中因低对比度导致的“形状坍塌”与帧间剧烈形变引发的“情景遗忘”。现有隐式时序建模方法依赖像素级特征传播，缺乏高层语义抽象，在长程依赖与模糊帧序列中失效。本文通过频域-空间双路交互增强边界感知，并引入显式记忆库递归传播以维持长程时序一致性。该架构在SUN-SEG基准上取得SOTA，但记忆机制在极长序列下的误差累积效应尚未充分验证。

】

---

【I2MOLE: INTERACTION AWARE INVARIANT MOLECULAR RELATIONAL LEARNING FOR GENERALIZABLE DRUG-DRUG INTERACTION PREDICTION ｜交互感知不变分子关系学习

研究机构：中国科学技术大学、湖南大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_20985809)

> 导读 药物相互作用（DDI）预测旨在通过计算手段解析多药联用的安全风险，其核心价值在于缓解临床数据稀疏与高精度预测需求之间的张力。现有独立编码范式受制于对训练集共现模式的过度记忆，在冷启动场景下泛化崩溃，且无法捕捉原子级跨分子交互机制。I2Mole 通过构建合并图显式建模原子间交互，并结合向量量化环境码本优化互信息，实现分布外泛化。该框架在标准基准上取得SOTA，但其在极端分布偏移下的鲁棒性及计算效率仍存疑。

】

---

【Johnson-Lindenstrauss Lemma Guided Network for Efficient 3D Medical Segmentation ｜基于Johnson-Lindenstrauss引理的轻量级3D医学分割框架

研究机构：中国科学技术大学、哈尔滨工业大学

作者：Jinpeng Lu、Linghan Cai、Yinda Chen 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.22307)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.22307)

> 3D医学影像分割在临床部署中面临硬件资源受限与延迟严苛的双重约束，传统轻量模型在压缩参数后往往牺牲对复杂病灶与异构模态的鲁棒性，形成“效率/鲁棒性冲突”。现有方案多依赖数据特定的剪枝或固定窗口注意力，难以在低计算预算下同时保持全局建模与局部细节提取。VeloxSeg通过理论推导卷积组大小下界与多尺度配对窗口注意力，在极低参数量下实现了精度与吞吐的平衡。该框架在PET/CT任务上展现了显著的效率优势，但其跨中心泛化能力与无预训练策略的长期鲁棒性仍存疑。

】

---

【K-Prism: A Knowledge-Guided and Prompt Integrated Universal Medical Image Segmentation Model ｜统一多范式医学图像分割模型

研究机构：美国罗格斯大学、美国斯坦福大学

作者：Bangwei Guo、Yunhe Gao、Meng Ye 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.25594)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.25594)

> 临床部署中，医疗机构需维护数十个针对特定器官、模态或任务的独立分割模型，导致工作流碎片化与性能不一致。现有方法通常局限于单一知识范式（如仅语义先验或仅交互反馈），无法像人类专家那样灵活整合多种知识源。K-Prism 通过双提示表示与混合专家解码器，在单一架构内统一了语义、上下文与交互三种知识范式。该框架在18个数据集上实现了跨范式SOTA性能，但其语义分割精度仍低于专用半监督模型，且未解决3D体积数据的处理瓶颈。

】

---

【KGOT: Unified Knowledge Graph and Optimal Transport Pseudo-Labeling for Molecule-Protein Interaction Prediction ｜知识图谱与最优传输伪标签驱动的药物-靶点相互作用预测

研究机构：美国纽约州立大学布法罗分校、阿联酋扎耶德大学

作者：Jiayu Qin、Zhengquan Luo、Guy Tadmor 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.09365)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.09365)

> 分子-蛋白相互作用（MPI）预测的核心瓶颈在于高质量实验标签的极度稀缺，现有深度模型受限于双模态输入，难以利用基因、通路等异构生物信息。KGOT 通过构建包含 300 万关系的多模态知识图谱，并引入基于最优传输（OT）的伪标签生成机制，将稀疏的 MPI 任务转化为半监督链接预测问题。该方法在零样本虚拟筛选中超越了传统对接与早期对比学习模型，但在最新结构基 SOTA 基准上存在显著性能差距，其泛化能力依赖于知识图谱的覆盖度而非原子级几何精度。

】

---

【KNOWGUARD: KNOWLEDGE-DRIVEN ABSTENTION FOR MULTI-ROUND CLINICAL REASONING ｜知识驱动弃权

研究机构：香港中文大学

作者：Xilin Dang、Kexin Chen、Xiaorui Su 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_50424908)

> 临床决策中，模型在信息不足时往往给出过度自信的误诊，现有弃权方法依赖内部置信度评估，缺乏外部证据验证机制。本文提出“先调查后弃权”范式，通过系统探索医学知识图谱识别证据缺口，而非仅计算置信度。该方法在开放域多轮临床基准上，将诊断准确率提升至74.12%，平均交互轮次控制在5.40轮。其价值在于将弃权从概率校准转化为知识边界检测，但知识图谱的静态构建与单智能体架构限制了其在复杂共病场景下的泛化能力。

】

---

【LEARNING SELF-CRITIQUING MECHANISMS FOR - REGION-GUIDED CHEST X-RAY REPORT GENERA TION ｜放射学自批判报告生成

研究机构：香港浸会大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_28829645)

> 放射学报告生成的核心痛点在于模型生成的发现往往缺乏图像中对应异常区域的可靠接地，导致临床不可信。现有方法多依赖解剖结构定位或统计相关性，难以在缺乏精细标注下区分相似病理或捕捉漏诊。本文提出RadSCR，将放射科医生的“自批判”思维内化为模型架构，通过对比替代异常、替代图像及全局假阴性检查来验证视觉提案的可靠性。该框架在MIMIC-CXR上取得了0.635的CheXbert F1分数，显著优于基线，但其检索式生成范式对报告语言多样性的潜在限制尚存疑。

】

---

【LiveClin: A Live Clinical Benchmark without Leakage ｜LiveClin：抗污染的全临床路径动态基准

研究机构：香港中文大学、浙江大学

作者：Xidong Wang、Shuqi Guo、Yue Shen 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.16747)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.16747)

> 医疗大语言模型（LLMs）在临床决策支持中的可靠性评估长期受困于静态基准的数据污染与知识过时，导致模型在真实复杂场景下的能力被高估。现有单轮问答范式无法模拟患者诊疗的纵向动态过程，LiveClin 通过构建基于最新病例报告的多阶段多模态评估体系，填补了这一空白。该工作利用 AI-人类协作工作流生成并验证了 1,407 个临床案例，揭示了当前顶级模型在完整临床路径推理上的显著瓶颈。其价值在于确立了动态评估的新标准，但 AI 生成题目的潜在系统性偏差及小模型在长程依赖下的表现仍存疑。

】

---

【Low-Pass Filtering Improves Behavioral Alignment of Vision Models ｜测试时低通滤波提升视觉模型行为对齐

研究机构：德国马克斯·普朗克智能系统研究所、德国图宾根大学

作者：Max Wolff、Thomas Klein、Evgenia Rusak 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.13859)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.13859)

> 深度神经网络在核心物体识别任务中表现出与人类视觉系统显著不同的行为策略，尤其是缺乏形状偏好且错误模式不一致。现有研究将生成模型（如Imagen）的高对齐度归因于其生成目标，但忽略了其输入下采样这一被忽视的预处理步骤。本文提出在测试时对输入图像施加低通滤波，无需重新训练即可大幅提升判别式模型的行为对齐度。该策略揭示了输入频率特性对行为对齐的因果作用，但仅验证了静态图像下的短时呈现条件，未探讨其对深层语义表征的潜在影响。

】

---

【M3CoTBench: Benchmark Chain-of-Thought of MLLMs in Medical Image Understanding ｜医疗多模态思维链基准

研究机构：浙江大学、中国科学技术大学

作者：Juntao Jiang、Jiangning Zhang、Yali Bi 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.08758)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.08758)

> 医疗多模态大语言模型（MLLMs）在影像诊断中常给出正确结论但推理路径错误，现有基准仅考核最终答案准确率，无法区分“右答错因”与真实临床逻辑。本文切入点在于构建首个针对医疗影像思维链（CoT）推理过程的多维度评估基准，通过标注关键推理步骤并定义正确性、效率、影响与一致性四项指标，系统量化模型推理质量。该工作揭示了CoT在缺乏视觉接地时可能降低准确率的现象，为临床可信AI提供了过程级评估标准，但其标注依赖专家共识且未覆盖动态多轮交互场景。

】

---

【MEDGMAE: GAUSSIAN MASKED AUTOENCODERS FOR MEDICAL VOLUMETRIC REPRESENTATION LEARNING ｜医学高斯掩码自编码器

研究机构：南京大学、东南大学

作者：Xueming Fu、Fenghe Tang、Rongsheng Wang 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_31184787)

> 导读 3D医学影像自监督预训练旨在利用无标签体积数据学习通用表征，以突破标注稀缺瓶颈。传统掩码自编码器（MAE）依赖体素级强度回归，其离散重建目标与解剖结构的连续几何特性存在根本冲突，导致编码器难以捕捉形状一致性特征。本文提出MedGMAE，将重建目标替换为3D高斯原语参数预测，通过连续几何建模实现参数高效且解剖连贯的表征学习。该方法在低数据分割任务上显著优于体素基线，并首次验证了预训练解码器在CT重建中的零样本加速价值，但其跨模态泛化能力与全数据场景下的上限仍存疑。

】

---

【Medical thinking with multiple images ｜医学多图像思维问答基准

研究机构：美国耶鲁大学

作者：Zonghai Yao、Benlu Wang、Yifan Zhang 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.16506)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.16506)

> 临床诊断依赖跨视图、跨模态的证据整合，但现有医学视觉问答（Med-VQA）基准多聚焦单图或短上下文，导致模型在真实多图像推理场景下的失败被单一准确率掩盖。本文切入点在于构建一个专家标注的、强制要求多图像整合与纵向随访推理的基准，通过引入三步“图像思维”（TwI）监督信号和超越准确率的步骤级评估，将诊断过程变得可观测。其价值在于揭示了当前模型的核心瓶颈并非推理长度，而是视觉接地与跨视图组合的可靠性，但作为纯基准工作，它未提供解决该瓶颈的模型架构。

】

---

【MedVR: Annotation-Free Medical Visual Reasoning via Agentic Reinforcement Learning ｜无标注医学视觉推理

研究机构：清华大学、阿里巴巴集团

作者：Zheng Jiang、Heng Guo、Chengyu Fang 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.08203)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.08203)

> 医学视觉问答模型在生成诊断答案时，常因缺乏对图像细节的直接交互而产生幻觉，导致临床决策风险。现有强化学习范式仅优化文本推理链，无法解决视觉证据脱节问题，且依赖昂贵的人工标注。MedVR 通过熵引导的视觉重定位与共识信用分配机制，实现了无需中间步骤标注的端到端视觉-文本交错推理。该框架在放射学与眼科基准上刷新了性能上限，但在病理学任务上表现滞后，其视觉推理优势是否具备跨模态普适性仍存疑。

】

---

【MINDMIX: A MULTIMODAL FOUNDATION MODEL FOR AUDITORY PERCEPTION DECODING VIA DEEP NEURAL-ACOUSTIC ALIGNMENT ｜听觉感知解码的多模态基础模型

研究机构：香港理工大学、香港城市大学

作者：RUI LIU、Zhige Chen、Pengshu 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_40047039)

> 听觉神经解码旨在从非侵入式脑电信号中还原语音、音乐等复杂听觉体验，其核心障碍在于脑电低信噪比与声学结构间的模态鸿沟。现有单模态脑电基础模型因缺乏声学刺激对齐，在跨任务泛化上表现受限，而任务特定模型又难以迁移。MindMix 通过引入大规模配对脑电-音频数据预训练，并设计交叉注意力低秩对齐模块实现深度跨模态交互，解决了浅层投影无法捕捉非线性依赖的问题。该方法在多项听觉解码任务上显著超越基线，但其性能高度依赖配对数据的规模与质量，且未充分验证在极端噪声或实时场景下的鲁棒性。

】

---

【MindPilot: Closed Loop Visual Stimulation Optimization for Brain Modulation with EEG-Guided Diffusion ｜脑电引导的闭环视觉刺激优化

研究机构：南方科技大学、美国特拉华大学

作者：Dongyang Li、Kunpeng Xie、Mingyang Wu 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_77844135)

> 现有脑机接口研究多聚焦于从神经信号解码意图，而利用视觉刺激反向调控脑活动的设计空间几乎空白。传统方法受限于侵入式记录或低层闪烁刺激，无法生成语义丰富的自然图像以驱动高阶认知状态。本文提出 MindPilot，将大脑视为不可微黑盒，通过伪模型代理梯度引导扩散模型进行无梯度闭环优化。该框架在非侵入式 EEG 场景下实现了自然图像的语义对齐生成，但代理模型对真实脑反应的预测精度有限，且闭环收敛依赖迭代次数，单次刺激的有效性尚未得到验证。

】

---

【Modeling the Density of Pixel-Level Self-Supervised Embeddings for Unsupervised Pathology Segmentation in Medical CT ｜基于密度建模的无监督病理分割

作者：Mikhail Goncharov、Eugenia Soboleva、Daniil Ignatyev 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_94548372)

> 3D医学影像中的病理检测长期受限于标注数据的稀疏性与类别覆盖不全，现有监督模型仅能识别已标注的少数病灶类型。传统无监督异常检测方法依赖ImageNet预训练特征或纯净训练集，在包含真实病理的混合CT数据上失效。本文切入点在于利用体素级自监督学习（Dense SSL）构建领域特定描述符，并通过掩码不变条件变量简化密度估计。Screener在四个大规模CT数据集上实现了无监督病理定位的SOTA性能，但其作为预训练基础在低样本微调下的泛化能力仍受限于蒸馏过程中的信息损失。

】

---

【MULTI STATE PROTEIN SEQUENCE DESIGN WITH DYNAMICMPNN ｜多态蛋白质序列设计中的动态几何逆折叠

研究机构：英国剑桥大学

作者：Alex Abrudan、Sebastian Pujalte Ojeda、Chaitanya Joshi 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_92569770)

> 蛋白质功能依赖构象动态变化，但现有逆折叠模型仅针对单一静态结构优化，导致生成的序列无法同时兼容多个功能状态。DynamicMPNN 通过联合学习多构象条件分布，直接生成满足多重结构约束的序列，而非对单态预测进行后验聚合。该方法利用 SE(3)-等变几何向量感知机编码构象集合，并引入基于 AlphaFold 3 模板的 Decoy-Normalized 评估协议。其在多态基准上显著优于 ProteinMPNN-MSD，但评估依赖模板引导，真实无模板折叠能力存疑。

】

---

【NEF-NET V2: ADAPTING ELECTROCARDIO PANORAMA IN THE WILD ｜几何感知视角变换与全景心电图合成

研究机构：香港科技大学、中山大学

作者：Zehui Zhan、Yaojun Hu、Jiajing Zhang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_56755871)

> 传统12导联心电图无法覆盖后壁心梗或Brugada综合征所需的非标准观测视角，而现有全景合成模型Nef-Net受限于单心跳建模、特征平均聚合及理想化数据假设，难以应对真实临床中的设备差异与电极偏移。本文提出NEF-NET V2，通过几何感知交叉注意力实现直接视角变换，并引入三阶段校准流程以适配野外环境。该方法在48导联密集基准上显著提升了合成保真度，但其对长时程动态生理变化的捕捉能力及跨人群解剖变异性的泛化边界仍待进一步验证。

】

---

【Omni-iEEG: A Large-Scale, Comprehensive iEEG Dataset and Benchmark for Epilepsy Research ｜多中心颅内脑电标准化基准与术前定位评估

研究机构：美国加州大学洛杉矶分校

作者：Chenda Duan、Yipeng Zhang、Sotaro Kanai 等 12 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.16072)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.16072)

> 癫痫术前定位依赖颅内脑电（iEEG）信号，但现有公开数据格式异构、标注缺失，导致模型无法跨中心验证。本文整合8个中心302名患者的178小时数据，统一元数据并标注36K病理事件，构建首个多中心iEEG基准。通过对比生物标志物驱动与端到端模型，验证了长序列建模在通道级定位上的潜力，但手术预后预测指标仍低于临床实用标准。

】

---

【On the geometry and topology of representations: the manifolds of modular addition ｜模加电路的拓扑等价性：从离散电路到统一流形

研究机构：加拿大麦吉尔大学、谷歌DeepMind

作者：Gabriela Moisescu-Pareja、Gavin McCracken、Harley Wiltzer 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.25060)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.25060)

> 机制可解释性领域长期面临一个根本困境：在相同数据上训练的不同架构网络，是否收敛到相同的内部计算电路？Zhong et al. (2023) 提出的“时钟”与“披萨”电路离散性假说，曾被视为通用性假说的反例，阻碍了对大规模模型内部机制的统一理解。本文通过代数拓扑与闭式流形理论，证明这些看似离散的电路实为拓扑等价的不同参数化，从而恢复了通用性假说的可能性。其价值在于将电路解释从经验统计提升为几何证明，但结论严格限定于模加玩具任务，向真实高维表征空间的外推性仍存疑。

】

---

【ONLY BRAINS ALIGN WITH BRAINS: CROSS-REGION - ALIGNMENT PATTERNS EXPOSE LIMITS OF NORMA TIVE MODELS ｜对齐模式分析

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_95727735)

> 脑-深度网络表征对齐旨在量化生物大脑与人工网络内部表征的几何相似性，但现有基准面临判别力缺失的困境：不同架构与训练目标的模型常获得相似的点态对齐分数，导致无法区分“脑似性”高低。本文切入点在于将评估从一阶统计量（单区域分数）扩展至二阶结构量（跨区域关系模式），提出对齐模式分析（APA）。通过验证模型是否复现脑区特有的跨区域对齐拓扑，APA在分数等价模型中实现了有效区分。其价值在于揭示了传统指标饱和下的盲区，但APS低分是否等同于生物合理性缺失，仍存疑。

】

---

【PALLATOM-LIGAND: AN ALL-ATOM DIFFUSION MODEL FOR DESIGNING LIGAND-BINDING PROTEINS ｜全原子扩散模型用于配体结合蛋白设计

研究机构：上海科技大学

作者：Haochen Wang、Qianyi Wang、Rui Ma 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_66968817)

> 设计具有特定小分子结合能力的蛋白质是生物传感器与药物开发的核心需求，但现有生成模型仅能处理骨架几何，无法捕捉侧链与配体间的原子级相互作用。Pallatom-Ligand 提出了一种端到端的全原子扩散框架，将蛋白质残基与配体原子统一编码，通过联合学习复合物分布来替代传统的“骨架生成+逆折叠”两阶段流程。该方法引入了全局折叠与原子级溶剂可及性双重条件控制，在结构一致性指标上显著优于现有骨架生成模型。尽管其计算效率与湿实验验证闭环尚存疑，但为原子级可控生成提供了新的架构范式。

】

---

【Partial Soft-Matching Distance for Neural Representational Comparison with Partial Unit Correspondence ｜部分软匹配距离

研究机构：美国纽约大学、美国加州大学圣迭戈分校

作者：Chaitanya Kapoor、Alex H. Williams、Meenakshi Khosla

论文原文见 [arXiv](https://arxiv.org/abs/2602.19331)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.19331)

> 神经表征比较需量化不同系统间计算单元的对应关系，但现有旋转不变度量忽略轴对齐特征，而强制全匹配的软匹配距离在含噪声或无关单元时产生虚假对应。本文切入点在于放松最优传输的质量守恒约束，允许部分神经元不匹配，从而在噪声环境下保持鲁棒的单元级对应。具体做法是引入部分最优传输框架，结合L-curve启发式自动选择匹配比例，实现高效且可解释的表征对齐。该方法在模拟和fMRI数据中验证了噪声鲁棒性，但在大规模高维表征中的计算效率与参数稳定性仍存疑。

】

---

【PEPTRI: TRI-GUIDED ALL-ATOM DIFFUSION FOR PEPTIDE DESIGN VIA PHYSICS, EVOLUTION, AND MUTUAL INFORMATION ｜短肽序列-结构联合生成中的物理-进化-信息三元引导

研究机构：丰田研究所、韩国高丽大学

作者：Ngoc-Quang Nguyen、Jaeyoon Jung、Seijung Kim 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_50660921)

> 短肽药物设计面临序列空间巨大且缺乏稳定三级结构的困境，现有生成模型往往将物理稳定性、进化合理性与序列-结构一致性解耦处理，导致生成的肽链虽几何合理但生物功能存疑。PepTri 针对这一痛点，提出在潜空间扩散过程中同时注入物理力场梯度、进化统计先验与互信息对齐的三元引导机制。该方法通过统一 SE(3) 等变潜空间实现序列与结构的联合去噪，在短肽结合剂设计基准上实现了结合亲和力与结构稳定性的同步提升。尽管其在专用基准上表现优异，但缺乏大规模预训练语言模型支撑及湿实验验证，其泛化边界仍存疑。

】

---

【Pixel-Level Residual Diffusion Transformer: Scalable 3D CT Volume Generation ｜像素级残差扩散 Transformer

研究机构：澳大利亚墨尔本大学

作者：Zhenkai Zhang、Markus Hiller、Krista A. Ehinger 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.20112)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.20112)

> 导读 3D CT 体积生成旨在从数据分布中合成高分辨率解剖结构，以支持诊断与分割任务。现有潜空间扩散模型受限于自编码器瓶颈导致的高频细节丢失，而直接应用卷积 U-Net 又面临显存爆炸与全局上下文缺失的双重困境。本文提出 PRDiT，通过“局部 MLP 去噪器 + 全局残差 DiT”的两阶段架构，在体素空间直接建模，并引入预测-校正采样与跨分辨率复用策略。该框架在 LIDC-IDRI 上实现了优于基线的生成质量，但其像素级操作在超高分辨率下的计算极限及与最新 Transformer 基线的对比缺失，仍存疑。

】

---

【PIXEL-LEVEL RESIDUAL DIFFUSION TRANSFORMER: SCALABLE 3D CT VOLUME GENERATION ｜像素级残差扩散Transformer

研究机构：澳大利亚墨尔本大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_75101044)

> 高分辨率3D CT体积生成面临局部细节保真与全局结构连贯性的双重挑战，现有潜空间扩散模型因压缩瓶颈丢失高频解剖特征，而直接应用卷积U-Net则受限于局部感受野。本文提出PRDiT，通过“局部MLP去噪+全局Transformer残差修正”的两阶段像素级策略，绕过自编码器瓶颈，在体素空间直接合成体积。该方法在LIDC-IDRI上取得2.04的3D FID，但缺乏与最新潜空间Transformer基线的直接对比，其像素级优势在超高分辨率下的计算可行性仍存疑。

】

---

【PoseX: AI Defeats Physics-based Methods on Protein Ligand Cross-Docking ｜蛋白质-配体对接基准：PoseX

研究机构：美国普渡大学、南京大学

作者：Yize Jiang、Xinze Li、Yuanyuan Zhang 等 17 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_69955231)

> 蛋白质-配体对接旨在预测小分子在蛋白口袋中的三维位姿，是药物发现中筛选先导化合物的核心步骤。现有基准如PoseBench和PLINDER主要聚焦于自对接（Self-docking），即配体回归其原始晶体结构，这一设定忽略了真实药物设计中配体需结合到不同构象蛋白的交叉对接（Cross-docking）场景，且评估框架往往繁重或模型覆盖不全。PoseX通过构建包含718个自对接和1,312个交叉对接条目的新数据集，系统评测了23种涵盖物理、AI对接及AI共折叠的方法，并引入能量最小化后处理模块。该基准揭示了AI方法在交叉对接中显著优于物理方法的趋势，但暴露了AI共折叠模型在立体化学合理性上的缺陷，其结论的普适性受限于特定数据截止时间与后处理依赖。

】

---

【PRISM: ENHANCING PROTEIN INVERSE FOLDING - THROUGH FINE-GRAINED RETRIEVAL ON STRUCTURE SEQUENCE MULTIMODAL REPRESENTATIONS ｜基于细粒度检索的蛋白逆折叠框架

研究机构：美国卡内基梅隆大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_77653621)

> 逆折叠旨在为给定骨架设计能稳定折叠的氨基酸序列，但现有端到端模型缺乏复用进化保守局部模式的机制，导致在巨大序列空间中搜索效率低且结构保真度受限。PRISM 通过引入多模态检索增强生成（Retrieval-Augmented Generation, RAG）机制，从已知蛋白库中检索细粒度“潜在基序”嵌入，以显式归纳偏置指导序列生成。该方法在保持极低运行时开销的前提下，显著提升了序列恢复率与折叠稳定性。其价值在于将记忆机制引入逆折叠，但检索库的静态构建可能限制对全新折叠类型的泛化能力。

】

---

【PRISM: Enhancing Protein Inverse Folding through Fine-Grained Retrieval on Structure-Sequence Multimodal Representations ｜基于细粒度检索的蛋白质逆折叠框架

研究机构：美国卡内基梅隆大学

作者：Sazan Mahbub、Souvik Kundu、Eric P. Xing

论文原文见 [arXiv](https://arxiv.org/abs/2510.11750)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.11750)

> 蛋白质逆折叠旨在为给定三维骨架设计能折叠成该结构的氨基酸序列，核心难点在于序列空间巨大且局部结构约束决定稳定性。现有端到端生成模型虽能捕捉全局依赖，但缺乏复用已知蛋白中进化保守的局部结构-序列模式（基序）的显式机制，导致局部预测精度受限。PRISM 提出了一种多模态检索增强生成（RAG）框架，通过从向量数据库检索潜在基序嵌入并经由混合注意力解码器整合，将局部模式复用转化为显式归纳偏置。该框架在多个基准上刷新了序列恢复与结构保真度的记录，但其性能增益高度依赖预构建的静态数据库，对完全新颖骨架的泛化能力仍存疑。

】

---

【Property-driven Protein Inverse Folding With Multi-Objective Preference Alignment ｜多目标偏好对齐的蛋白质逆折叠

研究机构：北京大学、加拿大蒙特利尔大学

作者：Xiaoyang Hou、Junqi Liu、Chence Shi 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.06748)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.06748)

> 蛋白质序列设计需在结构可恢复性（Designability）与溶解度、热稳定性等可开发性（Developability）属性间取得平衡，现有方法或依赖稀疏突变、或需精细调参的推理时偏置、或依赖特定子集重训练，难以泛化至多目标场景。本文切入点在于将直接偏好优化（Direct Preference Optimization, DPO）扩展为半在线多目标框架，通过自适应偏好边际解决竞争目标间的冲突。具体做法是迭代采样序列、用属性预测器构建偏好对、以柔性边际DPO损失更新模型。该框架在保持结构保真度的同时显著提升了可开发性指标，但其有效性仍受限于计算代理预测器的准确性，且缺乏湿实验闭环验证。

】

---

【PROTDYN: A FOUNDATION PROTEIN LANGUAGE - MODEL FOR THERMODYNAMICS AND DYNAMICS GEN ERATION ｜蛋白热力学与动力学统一生成模型

研究机构：美国普渡大学、美国西北大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_10851549)

> 蛋白质构象的静态系综与动态演化长期被割裂建模，前者缺乏时间信息，后者受限于短时程MD数据且泛化能力差。ProTDyn通过自回归Transformer架构，将离散化的结构Token与时间位置编码结合，在单一框架内同时学习平衡分布与多尺度轨迹转移。该模型在CATH1数据集上实现了优于专用热力学基线的系综生成精度，并验证了热力学信号对动力学预测的正向迁移作用，但其离散化表征在捕捉连续构象细节上的局限性尚待进一步量化。

】

---

【ProteinAE: Protein Diffusion Autoencoders for Structure Encoding ｜蛋白扩散自编码器

研究机构：香港中文大学

作者：Shaoning Li、Le Zhuo、Yusong Wang 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.10634)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.10634)

> 蛋白结构生成领域长期受困于离散化带来的精度损失与SE(3)流形约束带来的架构复杂性，导致现有自编码器难以构建高效且高保真的潜空间。本文切入点在于摒弃离散Token与等变约束，直接在E(3)空间利用非等变扩散Transformer构建连续潜空间。通过单一流匹配损失训练，PROTEINAE实现了SOTA的结构重构性能，并验证了该潜空间在下游生成任务中的有效性。其价值在于简化了优化管线并提升了重构精度，但非等变设计在物理合理性上的长期影响及多链扩展能力仍存疑。

】

---

【RANKFLOW: PROPERTY AWARE TRANSPORT FOR PROTEIN OPTIMIZATION ｜属性感知流传输用于蛋白质优化

作者：Lu Yu、Wei Xiang、Kang Han 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_4447372)

> 蛋白质优化需精确建模序列编辑与功能读数间的适应度景观，但现有方法受限于标签稀缺与多突变交互的忽略。传统回归头在低数据量下易过拟合，且无法捕捉非加性表观遗传效应。本文提出 RankFlow，通过条件流匹配将蛋白质语言模型（PLM）表征重塑为属性对齐分布，并引入排序一致性损失与属性引导转向门。该方法在 ProteinGym 等基准上实现了 SOTA 的排序精度与泛化能力，但其对结构信息的依赖及跨物种泛化边界仍存疑。

】

---

【REDUCING SEMANTIC MISMATCH IN BRAIN TO-TEXT DECODING THROUGH PERSONALIZED MULTIMODAL MASKING ｜脑-文解码中的个性化语义掩码

研究机构：浙江大学

作者：Jiaxuan Chen、Yu Qi、Yueming Wang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_26521544)

> 脑-文解码旨在从神经信号中还原受试者感知的视觉场景语义，核心难点在于机器模型倾向于编码图像中所有可见元素，而人类大脑仅选择性注意特定语义成分，导致直接对齐时产生语义偏差。现有方法如Mind-SA采用固定数量的硬掩码来剔除冗余语义，但缺乏对场景复杂度和个体差异的自适应能力。本文提出Yo’Mind，利用最优传输（Optimal Transport, OT）框架构建动态软掩码机制，将未被感知的语义元素分配至虚拟垃圾箱，实现无超参数调优的个性化对齐。该方法在NSD数据集上取得了SOTA性能，但其依赖fMRI高信噪比特性，向低信噪比EEG场景迁移的可行性尚存疑。

】

---

【Representational Alignment Across Model Layers and Brain Regions with Multi-Level Optimal Transport ｜多层级最优传输

作者：Shaan Shah、Meenakshi Khosla

论文原文见 [arXiv](https://arxiv.org/abs/2510.01706)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.01706)

> 脑-深度网络表征对齐旨在量化生物大脑与人工网络内部表征的几何相似性。传统逐层匹配方法强制一对一硬对应，在模型深度不一或特征跨层分布时失效，且无法提供全局对齐分数。本文提出MOT框架，通过双层联合优化实现神经元与层级的柔性耦合，自然处理深度不匹配并恢复层级结构。该方法在视觉、语言及脑数据上验证了全局对齐的有效性，但其旋转敏感特性在视觉Transformer中需额外扩展才能超越基线，暴露了OT方法对坐标基假设的依赖。

】

---

【RETHINKING RADIOLOGY REPORT GENERATION: - FROM NARRATIVE FLOW TO TOPIC-GUIDED FIND INGS ｜主题引导与解剖感知生成

研究机构：美国莱斯大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_46810769)

> 放射学报告生成（RRG）旨在从医学图像自动产生结构化临床文本，其核心价值在于缓解影像检查量激增与放射科医生短缺之间的结构性矛盾。现有视觉-语言模型（VLM）在模仿人类叙事流时，往往因过度依赖语言先验而削弱视觉接地，导致临床幻觉。本文提出LLaVA-TA框架，通过将报告拆解为独立的主题并引入解剖分割掩码，强制模型基于局部视觉证据生成文本。该策略在MIMIC-CXR上显著提升了事实准确性，但依赖LLM预处理且未对比最新强化学习路线，其泛化边界尚待验证。

】

---

【Reverse Distillation: Consistently Scaling Protein Language Model Representations ｜反向蒸馏：恢复蛋白质语言模型表征的单调缩放律

研究机构：美国杜克大学

作者：Darius Catrina、Christian Bepler、Samuel Sledzieski 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.07710)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.07710)

> 蛋白质语言模型（PLM）在扩大参数量时，下游任务性能往往不升反降，且不同规模模型的嵌入空间彼此割裂，无法像自然语言处理中的马特廖什卡嵌入那样实现前缀复用。现有方法试图通过增加模型容量或引入外部结构信息来突破性能瓶颈，但未能解决表征内部特征纠缠导致的缩放失效问题。本文提出反向蒸馏框架，将小模型表征作为基底，通过正交分解提取大模型独有的残差信息，从而构建出具有嵌套结构的嵌入空间。该方法在无需重新训练模型的前提下，恢复了PLM家族的单调缩放特性，但在非线性特征交互的捕捉上仍受限于线性假设。

】

---

【RIEMANNIAN HIGH-ORDER POOLING FOR BRAIN FOUNDATION MODELS ｜黎曼高阶池化

研究机构：西湖大学

作者：Chen Hu、Ziheng Chen、Rui Wang 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_51219431)

> 脑电信号（EEG）基础模型在下游解码时，通常依赖全局平均池化或单一分类令牌，导致时空二阶统计信息丢失。现有全局协方差池化（GCP）虽引入二阶统计，但将令牌压扁为单一矩阵，忽略了固有的时空层级结构。本文提出黎曼高阶池化（RHOP），通过商高斯嵌入与黎曼高斯聚合，在保留令牌级结构的同时实现尺度不变的高阶统计建模。该模块以极低的参数开销提升了多种训练范式下的性能，但其对极端个体差异的鲁棒性尚未在跨被试零样本场景中得到充分验证。

】

---

【Rigidity-Aware Geometric Pretraining for Protein Design and Conformational Ensembles ｜刚性感知几何预训练

研究机构：美国伊利诺伊大学厄巴纳-香槟分校、美国华盛顿大学

作者：Zhanghan Ni、Yanjing Li、Zeju Qiu 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.02406)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.02406)

> 蛋白质生成模型面临几何理解与生成机制耦合导致的泛化瓶颈，现有端到端框架难以在未见过的设计任务上保持物理合理性。RigidSSL 提出将几何学习前置为独立的预训练阶段，通过刚性残基表征与两阶段数据策略解耦这一过程。该方法利用静态结构扰动与分子动力学轨迹构建双向流匹配目标，在无条件生成与构象系综任务上验证了预训练对物理可行性的增益。其核心价值在于证明了动态数据对静态几何先验的必要性，但绝对性能仍低于当前 SOTA 生成模型，且仅处理骨架原子。

】

---

【SAIR: Enabling Deep Learning for Protein-Ligand Interactions with a Synthetic Structural Dataset ｜结构增强IC50仓库（SAIR）：合成结构数据驱动的结合亲和力预测

作者：Pablo Lemos、Zane Beckwith、Sasaank Bandi 等 14 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_24274135)

> 蛋白-配体结合亲和力预测长期受限于高质量实验结构-活性配对数据的稀缺，现有方法在数据覆盖与模型泛化间难以兼顾。本文切入点在于利用共折叠模型大规模生成合成3D结构，构建首个百万级规模的公开结构-亲和力数据集。通过Boltz-1x对ChEMBL与BindingDB中的100余万蛋白-配体复合物进行结构预测，并配套物理合理性校验与零样本基准测试，SAIR为下游模型提供了可复用的预训练资源。其价值在于填补了数据基础设施空白，但合成结构分布与真实结构的偏移是否限制了下游模型的性能上限，仍需进一步验证。

】

---

【Scaling Atomistic Protein Binder Design with Generative Pretraining and Test-Time Compute ｜蛋白结合剂原子级生成与推理时计算扩展

研究机构：英国牛津大学、韩国首尔大学

作者：Kieran Didi、Zuobai Zhang、Guoqing Zhou 等 14 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.27950)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.27950)

> 蛋白结合剂设计需在巨大序列-结构空间中生成物理稳定且具备特定结合功能的分子，现有方法受限于训练数据稀缺或推理时优化缺乏生成先验。本文指出“生成式”与“幻觉式”设计是虚假二分法，提出 Proteína-Complexa 框架，通过构建大规模合成数据集 Teddymer 训练原子级流匹配基础模型，并引入推理时计算扩展算法统一生成与优化。该框架在多个基准上刷新了计算成功率，但其性能高度依赖结构预测器作为奖励函数的准确性，且未涉及湿实验闭环验证。

】

---

【SE-DIFF : SIMULATOR AND EXPERIENCE ENHANCED - DIFFUSION MODEL FOR COMPREHENSIVE ECG GEN ERATION ｜生理模拟器与经验检索增强的ECG生成模型

研究机构：美国埃默里大学、美国加州大学洛杉矶分校

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_68057741)

> 文本到ECG生成旨在缓解临床数据标注稀缺与隐私限制，但现有扩散模型缺乏对心脏电生理机制的显式建模，导致合成波形在病理细节上偏离真实分布。本文切入点在于将基于常微分方程（ODE）的生理模拟器作为硬约束嵌入去噪过程，并引入基于电子健康记录（EHR）的检索增强机制以注入非参数化经验知识。通过变分自编码器（VAE）潜在空间中的条件扩散，结合单周期心跳解码器与模拟器一致性损失，SE-Diff实现了从自然语言描述到10秒12导联ECG的高保真合成。该框架在信号保真度与语义对齐上优于现有基线，但其对罕见病理形态的泛化能力及跨中心鲁棒性仍存疑。

】

---

【SEQUENTIAL INFORMATION BOTTLENECK FUSION: - TOWARDS ROBUST AND GENERALIZABLE MULTI MODAL BRAIN TUMOR SEGMENTATION ｜顺序信息瓶颈融合：面向鲁棒与泛化多模态脑肿瘤分割

研究机构：英国利物浦大学

作者：TIANYI LIU、Xi Yang、Wei Wang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_89091240)

> 多模态MRI脑肿瘤分割在临床中常遭遇模态缺失，导致并行融合策略下共享信息丢失与性能骤降。现有方法依赖静态拼接或注意力机制，缺乏对模态间冗余信息的理论约束，难以在部分序列不可用时维持稳定表征。本文提出顺序信息瓶颈融合网络（SMSN），通过两阶段顺序压缩与正交解耦，从信息论角度证明顺序融合比并行融合具有更紧的泛化界与Lipschitz连续性。该方法在BRATS18/20上显著优于并行基线，但评估仅覆盖胶质瘤，跨域泛化验证局限于单一脑转移瘤数据集，其理论优势在极端缺失场景下的实际边界尚存疑。

】

---

【SHRINKING PROTEINS WITH DIFFUSION ｜基于纯出生过程的蛋白质序列缩短扩散模型

研究机构：美国纽约大学、美国哈佛大学

作者：Ethan Baron、Alan Amin、Ruben Weitzman 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_94419437)

> 蛋白质工程与药物递送常受限于长序列蛋白的合成难度，而现有生成模型无法高效搜索删除空间以保留功能。SCISOR 提出了一种仅通过插入噪声、反向执行删除的离散扩散框架，使模型具备预测删除效应的归纳偏置。该方法在 ProteinGym 上实现了删除效应预测的 SOTA，并生成了比基线更保结构的短序列，但其对长序列计算复杂度的处理及通用生成能力的边界仍需审视。

】

---

【SimpleFold: Folding Proteins is Simpler than You Think ｜SimpleFold：基于流匹配的通用Transformer蛋白折叠模型

作者：Yuyang Wang、Jiarui Lu、Navdeep Jaitly 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.18480)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.18480)

> 蛋白折叠旨在从氨基酸序列预测三维原子结构，传统方法依赖硬编码的领域特定架构（如MSA、Pair Rep）以捕捉进化约束。现有方案在去除这些模块后性能显著下降，且生成式模型在单目标基准上常劣于回归式模型。本文切入点在于验证通用Transformer架构能否在缺乏显式几何约束的情况下，通过大规模数据与流匹配目标实现高精度折叠。SimpleFold采用标准Transformer块与自适应层，结合全原子流匹配训练，证明了去领域特定架构的可行性。其价值在于简化了模型部署并挑战了等变架构的必要性共识，但在远缘同源蛋白上的鲁棒性及动态构象建模的边界尚存疑。

】

---

【Simulator and Experience Enhanced Diffusion Model for Comprehensive ECG Generation ｜生理模拟器与经验检索增强的ECG生成模型

研究机构：美国埃默里大学、美国加州大学洛杉矶分校

作者：Xiaoda Wang、Kaiqiao Han、Yuhao Xu 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.09895)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.09895)

> 文本到心电图（ECG）生成旨在从临床描述合成10秒12导联波形，以缓解标注数据稀缺与隐私限制。现有扩散模型仅依赖数据分布学习形态，缺乏生理机制约束，且未利用电子健康记录（EHR）中的经验知识。SE-Diff通过引入ODE生理模拟器约束与LLM检索增强条件，将生成过程锚定在生理可行流形上。该方法在信号保真度与语义对齐上优于基线，但单基线对比与缺乏罕见病覆盖度评估限制了其结论的普适性。

】

---

【Synthesizing High-Quality Visual Question Answering from Medical Documents with Generator-Verifier LMMs ｜基于评分标准生成-验证的医学视觉问答数据合成

研究机构：复旦大学

作者：Xiaoke Huang、Ningsen Wang、Hui Liu 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.25867)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.25867)

> 医学视觉问答（Med-VQA）模型训练长期受制于高质量、可公开使用的大型语料缺失，现有自动合成方法因忽略视觉证据导致数据噪声大，而人工标注数据规模小且模态受限。本文切入点在于将数据合成过程从“规模优先”转向“质量优先”，通过显式评分标准（Rubric）驱动生成与多阶段验证，从开放文献中合成可审计的视觉问答数据。具体做法是构建一个由大型多模态模型（LMM）驱动的生成-验证流水线，利用强化学习训练学生模型。该框架在多个基准上提升了开源模型性能，但其对细粒度病理特征的捕捉能力仍弱于专用对齐方法，且高阈值过滤可能牺牲数据多样性。

】

---

【TEMPORAL SUPERPOSITION AND FEATURE GEOMETRY OF RNNS UNDER MEMORY DEMANDS ｜时间超叠加与RNN特征几何

研究机构：英国帝国理工学院、英国伦敦大学学院

作者：Pratyaksh Sharma、Alexandra M Proca、Lucas Prieto 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_74062471)

> 本文旨在解析循环神经网络（RNN）中时间维度作为容量约束对表征几何的影响，现有静态超叠加理论无法解释动态序列中特征随时间演化的干扰机制。作者通过推导线性RNN在延迟回忆任务下的解析损失函数，揭示了“时间超叠加”现象及无干扰空间的存在。这一理论框架为理解动态系统的表征策略提供了几何解释，但其结论主要基于合成任务，在真实生物脑数据上的普适性尚待检验。

】

---

【TEST-TIME ADAPTATION WITHOUT SOURCE DATA - FOR OUT OF-DOMAIN BIOACTIVITY PREDICTION ｜无源数据下的生物活性预测测试时适应

研究机构：新加坡南洋理工大学

作者：Yiming Yang、Zhiyuan Zhou、Yueming Yin 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_70832736)

> 生物活性预测旨在量化配体对靶点蛋白的功能调节能力，但现有深度学习模型在分布偏移场景下泛化能力受限。主流域适应方法依赖源数据访问，这在涉及知识产权或隐私限制的工业场景中不可行。本文提出TAB框架，通过不确定性加权一致性学习与对比学习，在仅拥有预训练模型而无源数据的情况下实现测试时适应。该方案在多个OOD基准上显著优于传统基线，但其对结合位点几何特征的捕获机制及在标准ID任务上的相对优势仍存疑。

】

---

【THE HUMAN BRAIN AS A DYNAMIC MIXTURE OF EXPERT MODELS IN VIDEO UNDERSTANDING ｜跨时间表征相似性分析

研究机构：荷兰阿姆斯特丹大学

作者：Christina Sartzetaki、Anne Zonneveld、Pablo Oyarzo 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_23387924)

> 动态视频场景下，生物脑神经活动随时间毫秒级演化，而现有模型-脑对齐研究主要依赖静态图像或慢速fMRI信号，无法捕捉这种细粒度的时间动态。静态RSA假设模型与脑表征在单一时间点上对齐，忽略了视频处理中特征随时间的展开与脑区响应的时序滞后。本文提出跨时间表征相似性分析（CT-RSA），通过匹配模型所有时间步特征与脑所有时间步响应的最大相关，量化动态对齐。该方法揭示了后部脑区存在强烈的模型-脑时间对应性，而前部脑区则缺乏此特性，表明大脑视频处理并非由单一模型类型主导，而是动态混合专家机制。

】

---

【TOWARDS ALL-ATOM FOUNDATION MODELS FOR BIOMOLECULAR BINDING AFFINITY PREDICTION ｜原子级扩散Transformer（ADiT）：面向生物分子结合亲和力预测的统一基础模型

研究机构：北京大学、加拿大蒙特利尔大学

作者：Liang Shi、Zuobai Zhang、Huiyu Cai 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_71531849)

> 生物分子结合亲和力预测旨在量化蛋白与配体、抗体与抗原等复合物的结合强度，但高质量实验标签稀缺且现有方法多针对单一交互类型，缺乏跨任务泛化能力。本文切入点在于将AlphaFold 3的生成式结构预测架构改造为判别式表征学习器，通过移除多序列比对（MSA）依赖并采用去噪预训练，构建统一处理多种生物分子交互的基础模型。ADiT采用非等变Transformer处理全原子结构，在蛋白-配体、药物-靶点等四类任务上达到SOTA或竞争性性能。其价值在于验证了结构预训练对缓解标签稀缺的有效性，但非等变设计在复杂构象下的鲁棒性及与专用几何模型的精度差距仍存疑。

】

---

【TOWARDS TEXT–MASK CONSISTENCY IN MEDICAL IMAGE SEGMENTATION ｜面向文本-掩码一致性的医学图像分割

研究机构：安徽大学

作者：Jie Gui、HangTu、Wen Sha 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_30088782)

> 医学视觉-语言模型在分割任务中常出现掩码与文本描述在数量、位置等语义属性上的矛盾，根源在于模板化临床文本导致对比学习产生大量假负样本，以及单向视觉主导融合缺乏显式的语言空间表征。C2Seg 通过簇感知对比学习构建软标签分布以缓解对齐冲突，并引入双向互补注意力模块实现像素级的双向语义交互。该方法在四个公开数据集上显著提升了分割精度与边界一致性，但其对长文本复杂语义的泛化能力及3D体数据适用性仍未得到验证。

】

---

【Towards Understanding the Shape of Representations in Protein Language Models ｜蛋白质语言模型表征形状空间几何分析

研究机构：挪威奥斯陆大学

作者：Kosio Beshkov、Anders Malthe-Sørenssen

论文原文见 [arXiv](https://arxiv.org/abs/2509.24895)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.24895)

> 蛋白质语言模型（PLM）的潜空间几何结构及其对蛋白质三维结构的编码机制尚不明确。现有可解释性研究仅关注单序列的局部特征提取，忽略了不同蛋白在潜空间中全局度量关系的层级演化规律。本文通过平方根速度（SRV）形状空间与图过滤（Graph Filtration）框架，量化了ESM2各层表征的形状几何特性及结构保真度。该工作揭示了PLM深层表征在局部结构编码上的双峰分布特征，为理解模型内部结构信息的层级分布提供了几何视角，但其结论受限于特定模型架构与数据集采样偏差。

】

---

【Uncovering Semantic Selectivity of Latent Groups in Higher Visual Cortex with Mutual Information-Guided Diffusion ｜互信息引导扩散揭示高层视觉皮层潜空间语义选择性

研究机构：美国佐治亚理工学院

作者：Yule Wang、Joseph Yu、Chengrui Li 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.02182)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.02182)

> 高层视觉皮层神经元对多种视觉语义特征呈现混合选择性，导致传统解码方法无法揭示特征在神经群体中的具体组织形式。现有基于DNN对齐或单一解码器的方法仅能间接推断或平滑掉细微的语义变化，无法直接可视化潜空间中的语义结构。MIG-Vis通过组级解耦变分自编码器提取神经潜空间，并利用互信息最大化引导扩散模型生成图像，以验证潜组对应的视觉语义。该方法在猕猴IT皮层数据上实现了语义潜组的直接可视化，但缺乏定量指标评估生成图像的语义保真度，且未与DNN表征进行跨系统对比。

】

---

【Uni-NTFM: A Unified Foundation Model for EEG Signal Representation Learning ｜统一神经拓扑基础模型

研究机构：中国科学院、新加坡南洋理工大学

作者：Zhisheng Chen、Yingwei Zhang、Qizhen Lan 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.24222)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.24222)

> 脑电信号（EEG）基础模型旨在从非平稳、高噪声的神经信号中提取具备跨被试泛化能力的通用特征，以突破传统手工特征工程在复杂临床场景下的性能瓶颈。现有方法多将神经信号视为像素网格或离散令牌序列，忽略了大脑皮层复杂的几何拓扑结构与稀疏编码机制，导致频谱偏差与个体身份混淆。Uni-NTFM 通过异构特征投影模块解耦时频域信号，结合层级拓扑嵌入对齐电极布局，并引入混合专家架构实现功能模块化，在 28,000 小时数据上预训练以构建神经生理学一致的通用表示。该架构在九项下游任务中超越了主流基础模型，但其对在线适应机制的缺失及频域重建对高频伪影的抑制效果仍需进一步验证。

】

---

【Unified Brain Surface and Volume Registration ｜统一皮层与体积脑图像配准

研究机构：美国麻省理工学院、法国巴黎西岱大学

作者：S. Mazdak Abulnaga、Andrew Hoopes、Malte Hoffmann 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.19928)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.19928)

> 脑功能成像分析要求皮层表面与皮层下体积在解剖上严格对齐，但传统方法将二者视为独立问题，导致边界处形变场不一致，破坏全脑分析的连贯性。现有深度学习配准模型虽能高效预测体积形变，却因欧氏空间优化陷入局部最优，无法捕捉皮层复杂的折叠拓扑。NeurAlign 通过引入球面配准分支与体积分支的耦合损失，在单一前向传播中同时优化两个域，解决了这一结构性矛盾。该方法在皮层对齐精度上显著超越现有基线，但其对训练时依赖皮层网格的假设，限制了其在缺乏高质量表面重建场景下的直接应用。

】

---

【WAVEPOLYP: VIDEO POLYP SEGMENTATION VIA HI - ERARCHICAL WAVELET-BASED FEATURE AGGREGA TION AND INTER-FRAME DIVERGENCE PERCEPTION ｜视频息肉分割中的频域特征聚合与帧间发散感知

研究机构：深圳大学、香港理工大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_97462371)

> 视频息肉分割需同时应对息肉的高伪装性、帧间动态变化及实时性约束，现有方法多依赖时序注意力增强空间特征，却忽视了帧内判别信息的挖掘与帧间差异的显式建模。本文切入点在于利用小波变换分离高低频特征以增强帧内细节，并通过时间维度的发散注意力捕捉帧间动态。具体做法是构建层级小波特征聚合模块与帧间发散感知块，在SUN-SEG数据集上以87.55%的Dice系数超越现有基线。该方法在精度与效率间取得平衡，但其对长程时序依赖的建模能力及在严重成像退化下的鲁棒性尚存疑问。

】

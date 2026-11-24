# ACL-Findings2026 · 其他方向方向论文汇编

> 本方向共 182 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【A Multi-View Media Profiling Suite: Resources, Evaluation, and Analysis ｜多视图媒体画像中的动态融合机制

研究机构：丹麦哥本哈根大学

作者：Muhammad Arslan Manzoor、Dilshod Azizov、Daniil Orel 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_cb374499c508)

> 媒体机构画像旨在通过历史偏见与事实性标签实现大规模实时监测，以替代高成本的单篇验证。现有方法依赖单一文本或静态图结构，在数据稀疏与噪声视图下表现受限，且缺乏对异构信号可靠性的系统评估。本文构建包含三种图结构与两种文本的五视图资源，并提出基于强化学习的动态融合策略，以自适应权重应对视图缺失。该工作确立了ACL-2020上的新基准，但在大规模新数据集MBFC-2025上，其多视图融合性能未超越纯文本基线，揭示了结构信号在大规模场景下的有效性边界。

】

---

【A Survey of Large Models in Sports ｜大模型在体育领域的应用综述

研究机构：中国人民大学、四川大学

作者：Yichen Xu、Jianzhe Ma、Chuhan Wang 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0bc294a06eb2)

> 体育智能的核心矛盾在于如何将高维、非平稳的运动数据转化为可执行的战术与语义洞察。传统统计模型与浅层深度学习难以捕捉多智能体交互中的隐性战术意图，而早期大模型在体育垂直领域缺乏事实可靠性与实时性。本文通过系统梳理241篇核心文献，构建了涵盖6类利益相关者与19项任务的分类体系，并深度剖析了数据集分布与模型范式。其价值在于确立了从“数值预测”向“语义生成”转型的认知地图，但缺乏对模型在真实赛场边缘部署有效性的实证验证。

】

---

【A Survey of Retentive Network ｜RetNet：固定衰减递归状态下的长序列建模综述

作者：Haiqi Yang、Zhiyuan Li、Yi Chang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e55fe080e44e)

> 长上下文Transformer面临二次方计算复杂度与线性内存膨胀的双重瓶颈，现有线性注意力或状态空间模型（SSM）虽降低复杂度，但在精确检索任务上因固定状态导致信息过度压缩而失效。本文切入点在于系统化梳理RetNet这一特定递归架构，揭示其通过固定标量衰减实现并行训练与递归推理统一机制的内在逻辑，并指出其“联想回忆瓶颈”这一被忽视的精度缺陷。RetNet通过多尺度保留机制将注意力转化为线性复杂度递归过程，但在高熵检索任务上保真度受限。其价值在于提供了递归架构的完整技术图谱，但固定衰减是否必然导致检索能力上限，仍需更严格的基准验证。

】

---

【Accelerating LLM Fine-Tuning via Embedding Knowledge Transfer ｜嵌入层知识迁移加速大模型微调

研究机构：香港科技大学、澳门大学

作者：Meishu Peng、Ziyue Zhang、Yi Zhang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_96dc596b9a16)

> 参数高效微调（Parameter-Efficient Fine-Tuning, PEFT）旨在以极小参数预算适应下游任务，但现有方法如 LoRA 仅更新 Transformer 块权重，忽略了嵌入层对领域特定语义的编码作用，导致收敛缓慢且无法利用已有小模型专家知识。本文切入点在于通过异构模型间的嵌入层维度扩展与加权融合，将小专家模型的知识直接注入大目标模型，规避了伪标签生成的显存与时间开销。具体做法是构建词汇对齐后的嵌入矩阵，通过隐藏层维度扩展和加权融合实现参数迁移，再结合双阶段微调加速收敛。该方法在代码和数学任务上显著加速了收敛并提升了最终性能，但其通用性受限于同模型族内的架构一致性，跨架构迁移能力存疑。

】

---

【ActorMind: Emulating Human Actor Reasoning for Speech Role-Playing ｜语音角色扮演：基于多智能体思维链的无训练推理框架

研究机构：香港科技大学

作者：Xi Chen、Wei Xue、Yike Guo

论文原文见 [arXiv](https://arxiv.org/abs/2604.11103)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.11103)

> 语音角色扮演旨在让模型以特定角色的音色、情感与语调自发地生成对话，而非仅合成文本。现有大语言-音频模型（LLAMs）受限于极小的音色库，而文本转语音（TTS）模型缺乏对场景与角色情感的深层推理能力，导致生成的语音虽清晰却缺乏“人格”。本文提出 ActorMind，一个模拟人类演员表演过程的多智能体思维链（CoT）推理框架，通过“眼-耳-脑-口”四个智能体协同工作，在无训练条件下实现语音角色的情感自发表达。该框架在自建基准上显著优于基线，但其有效性高度依赖特定剧集数据，跨场景泛化能力存疑。

】

---

【AdaMARP: An Adaptive Multi-Agent Interaction Framework for General Immersive Role-Playing ｜自适应多智能体交互框架

研究机构：浙江大学

作者：Zhenhua Xu、Dongsheng Chen、Shuo Wang 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.11007)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.11007)

> 通用角色扮演旨在让大语言模型模拟任意用户定义的角色，但现有系统多局限于静态场景与固定角色，缺乏对动态环境信息的建模，导致叙事沉浸感不足。本文切入点在于将环境状态作为一等公民信号，并引入独立的场景管理器代理，通过离散动作空间实现多角色编排、场景切换与动态角色引入。具体做法是构建包含思维、动作、环境与言语的沉浸式消息格式，并训练专用数据集以监督演员模型与场景管理器。该框架在轨迹级评估中展现了小模型超越部分闭源大模型的能力，但其对长程认知保真度的贡献尚未在标准基准上得到验证。

】

---

【Adaptive Zooming via Relevance-Informed Positional Resource Allocation for Training-free LLM Context Extension ｜基于语义相关性的位置资源分配

研究机构：华东师范大学、复旦大学

作者：Hongbo Zhao、Huibin Wang、Bin Tang 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_76a2cef09da3)

> 长上下文推理中，模型在超出预训练窗口时因位置编码分布外（Out-of-Distribution, OOD）效应导致性能骤降。现有免训练外推方法仅依据Token相对距离进行均匀或固定比例的位置映射，无法区分语义关键信息与噪声，导致关键证据在长序列中被模糊。本文提出RiPRA，将位置编码重构为基于查询语义相关性的约束资源分配问题，动态调整位置分辨率。该方法在免训练外推类别中表现最优，但其性能上限仍低于专用上下文压缩方法，且缺乏对压缩率与推理延迟的联合评估。

】

---

【AED-RAG: Continuous Multi-Granular Context Fusion for Retrieval-Augmented Generation via Adaptive Ensemble Decoding ｜自适应集成解码

作者：Junzhe Zhou、Fulin Lin、Tairan Cheng 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_23efdcdbec71)

> 检索增强生成（RAG）面临检索粒度与生成效用错位的问题，粗粒度段落引入噪声，细粒度三元组缺乏语境，且传统离散重排截断了置信度信号。现有方法在平衡外部证据与内部记忆时，往往陷入“非此即彼”的硬选择，无法实现连续的概率融合。本文提出 AED-RAG，通过训练效用预测器并实施自适应集成解码，将段落、三元组与参数记忆映射至统一概率空间进行 Token 级软融合。该方法在通用问答基准上优于传统 RAG 基线，但其对冲突场景的鲁棒性及效用预测器的泛化能力存疑。

】

---

【AEQ-Bench: Measuring Empathy of Omni-Modal Large Models ｜全模态共情评估基准

研究机构：香港理工大学、哈尔滨工业大学

作者：Xuan Luo、Lewei Yao、Lanqing Hong 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_fd4374077722)

> 全模态大模型（OLMs）在生成共情响应时，往往忽略音频中的副语言线索，导致评估体系失效。现有基准多依赖文本转录或单一模态，无法量化“语调”对共情质量的决定性影响。本文构建AEQ-BENCH，通过上下文与语调的并行变体设计，直接评估OLMs在音频-文本联合输入下的共情生成与判断能力。该基准揭示了OLMs在细粒度副语言共情上的显著局限，为多模态情感计算提供了必要的评估坐标，但其对生成策略的区分度仍存疑。

】

---

【Affectron: Emotional Speech Synthesis with Affective and Contextually Aligned Nonverbal Vocalizations ｜情感对齐的非语言发声合成

研究机构：韩国高丽大学、美国麻省理工学院

作者：Deok-Hyeon Cho、Hyung-Seok Oh、Seung-Bin Kim 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.14432)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f0795c70d176)

> 现有情感语音合成系统难以在开放设置下生成自然且位置合理的非语言发声（Nonverbal Vocalizations, NVs），主要受限于对齐标注的缺失与数据分布偏差。Affectron 提出了一种基于情感驱动匹配与路由的训练时增强策略，结合结构掩码机制，解决了 NV 类型与位置的情感一致性问题。该方法通过微调预训练神经编解码语言模型（Neural Codec Language Model, NCLM），实现了无需显式检测器即可生成多样化 NV 的能力。其价值在于以小规模开放语料实现了高质量 NV 合成，但缺乏与主流扩散模型 TTS 的直接对比，且依赖伪标签的情感对齐精度尚存疑。

】

---

【AI, Take the Wheel: What Drives Delegation and Trust in Human-Computer Cooperative Question Answering? ｜竞争性问答中的人机委托与信任校准

作者：Maharshi Gor、Yoo Yeon Sung、Yu Hou 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.28255)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.28255)

> 人机协作的核心矛盾在于人类对AI依赖程度与其实际能力不匹配，导致过度依赖或错误恢复失败。现有静态信任模型无法捕捉竞争性多智能体场景下动态的委托与采纳决策，本文切入点是通过区分“主动委托”与“审议性采纳”两种解耦的依赖模式，量化校准失效的具体机制。通过构建竞争性问答锦标赛，追踪23名专家与16个AI代理的行为日志，揭示确认偏误与置信度失准对协作质量的负面影响。该研究提供了微观行为精度的实证基础，但受限于短期受控实验，未验证长期交互中的声誉动态演化。

】

---

【An LLM-Embedding Semantic Adaptation Network for Post-level Semantic Drift Evaluation ｜基于LLM嵌入与图卷积的帖子级语义漂移评估

研究机构：中国科学技术大学

作者：Ning Chen、Mingyu Kang、Jie Li 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_5e041d9b3f56)

> 语义漂移评估旨在量化在线讨论中事件相关帖子随时间发生的动态语义变化，但事件关键词的稀疏与非均匀分布导致传统模型难以捕捉帖子级的细粒度漂移。现有方法多停留在时间或事件粒度，无法处理快速演变的单帖内容。本文提出LLM-SAN，通过冻结LLM提取嵌入，结合GRU时序建模与GCN话题增强，利用重构误差检测漂移点。该方法在中文新闻基准上实现了SOTA性能，但其依赖单一数据集且未验证跨语言泛化能力，评估边界受限。

】

---

【AOT: Efficient Synthesis Planning via LLM-Empowered AND-OR Tree Search ｜基于大语言模型路径生成的AND-OR树逆合成搜索

研究机构：香港中文大学、吉林大学

作者：Xiaozhuang Song、Xuanhao Pan、Xinjian Zhao 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.20988)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.20988)

> 逆合成规划旨在将目标分子分解为可商购原料，但传统单步预测加搜索的解耦架构在长程依赖与计算效率上存在瓶颈。现有LLM方法虽能捕捉策略连贯性，却因迭代进化算法导致搜索冗余与推理成本高昂。AOT*通过原子映射LLM生成的完整合成路径至AND-OR树结构，结合检索增强生成与UCB引导的树搜索，实现了路径级连贯性与树结构复用效率的平衡。该方法在复杂分子上展现出3-5倍的搜索效率优势，但其性能高度依赖底层LLM的生成质量与RAG数据库的覆盖度，在分布外分子上的泛化能力尚存疑。

】

---

【AROMA: Augmented Reasoning Over a Multimodal Architecture for Virtual Cell Genetic Perturbation Modeling ｜基于多模态知识接地的虚拟细胞扰动推理

研究机构：清华大学

作者：Zhenyu Wang、Geyan Ye、Wei Liu 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.20263)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.20263)

> 单细胞扰动建模的核心困境在于，现有生成式模型虽能拟合分布，却缺乏对基因调控因果链的显式解释，导致预测结果难以用于生物学假设验证。通用大语言模型（LLM）虽具备推理能力，但其自由文本生成缺乏生物拓扑约束，且检索机制未对齐调控方向性。AROMA 通过构建基因与通路知识图谱，结合图神经网络（GNN）与蛋白序列编码，将结构化证据注入 LLM 推理过程，实现了预测精度与机制可解释性的统一。该方法在未见细胞系上展现出鲁棒的零样本泛化能力，但其评估局限于离散分类任务，未与连续分布预测模型进行数值精度对标。

】

---

【Astra: Activation-Space Tail-Eigenvector Low-Rank Adaptation of Large Language Models ｜激活空间尾部特征向量低秩适配

作者：Kainan Liu、Yong Zhang、Ning Cheng 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_6990a57c3efc)

> 参数高效微调（PEFT）旨在以极小的可训练参数预算适应下游任务，但标准低秩适配（LoRA）的随机初始化导致早期梯度极小，阻碍收敛并限制表达力。现有初始化策略多依赖静态权重结构或瞬时梯度信号，忽略了预训练模型输出激活维度利用不均这一动态特性。Astra 通过校准集估计输出激活协方差矩阵，将低秩更新约束在尾部特征子空间内，实现了更快的收敛与更优的下游性能。该方法在 16 个基准上超越现有 PEFT 基线，但在复杂推理任务上是否具备普适性仍需验证。

】

---

【Auditing LLM Responses to Harmful Stereotypes Targeting Mental Health Groups ｜心理健康刻板印象的显式合理化审计

研究机构：美国罗切斯特理工学院、美国佐治亚理工学院

作者：Arka Dutta、Rijul Magu、Sean Kim 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4c4dce0c363a)

> 大语言模型在心理健康领域的应用常聚焦于临床辅助与危机干预，但模型内化的社会偏见如何转化为对弱势群体权利剥夺的合理化论述，长期处于安全评估的盲区。现有通用内容过滤工具仅能识别显性毒性，无法捕捉以“合理建议”为伪装的结构性歧视，导致模型在投票权、居住权等敏感议题上输出有害内容却未被标记。本文通过构建包含15个刻板印象框架与132个身份群体的提示集，对13个开源模型进行零样本审计，揭示模型在显式提示下对权利限制类刻板印象的高比例背书，并证明主流Moderation API对此类细微歧视的漏检率极高。该工作填补了社会偏见审计中“权利合理化”维度的空白，但单轮静态评估能否反映多轮对话中偏见的累积效应，仍存疑。

】

---

【AWARE: Agentic Knowledge Warehousing for Contextual Intelligence ｜代理知识仓库

研究机构：香港科技大学、中国人民大学

作者：Hongjin Qian、Siqi Bao、Zhao Cao 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d9c104e9df1a)

> 复杂信息检索任务中，答案相关证据稀疏地嵌入在海量异构文本中，导致大语言模型（LLM）在有限上下文预算内无法组装出足够解决任务的证据链。传统检索增强生成（RAG）单次注入缺乏深度，工具集成推理受限于上下文膨胀，均无法应对这种低知识密度下的“数据混乱”。AWARE 将检索重构为代理知识构建过程，通过离线文档结构化与在线多线程探索，将原始文本转化为紧凑的任务条件化知识表示。该框架在 GAIA 等基准上显著优于基线，但其性能增益究竟源于检索策略优化还是底层 LLM 推理能力的差异，尚存疑。

】

---

【Benchmarking Vision-Language Models on Chinese Ancient Documents: From OCR to Knowledge Reasoning ｜中文古籍多任务理解基准

研究机构：复旦大学

作者：Haiyang Yu、Yuchuan Wu、Fan Shi 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_191ac04eaab5)

> 视觉语言模型（VLMs）在处理中文古籍时，因竖排版式、繁体异体字及物理退化导致视觉接地失效，且现有基准仅覆盖现代印刷文档或简化字，无法评估从字符识别到知识推理的全链路能力。本文构建了首个涵盖OCR、翻译及三类问答的古籍基准AncientDoc，通过LLM辅助标注与人工校验生成3000页多任务数据。该基准揭示了通用VLMs在古籍OCR阶段的严重瓶颈，但其单一数据源与缺乏领域适配模型对比的局限，使其结论的普适性存疑。

】

---

【Beyond Black-Box Interventions: Latent Probing for Faithful Retrieval-Augmented Generation ｜潜在空间探针驱动的忠实检索增强生成

研究机构：厦门大学、阿里巴巴集团

作者：Linfeng Gao、Qinggang Zhang、Baolong Bi 等 12 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.12460)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b7975816c614)

> 检索增强生成（RAG）系统在处理上下文与参数化知识冲突时，常因模型过度依赖内部记忆而丧失上下文忠实度。现有解码干预或偏好优化方法将大语言模型视为黑盒，无法诊断冲突发生的内部机制，导致在噪声环境下表现脆弱。本文切入点在于发现冲突知识在模型潜在空间中线性可分，并据此构建探针进行因果干预。ProbeRAG 通过知识剪枝、潜在冲突探针与冲突感知注意力三阶段框架，实现了从外部纠偏向内部引导的范式转移。该方法在多个基准上超越了最强基线，但其探针依赖特定模型训练，跨架构通用性仍存疑。

】

---

【Beyond Black-Box Labels: Interpretable Criteria for Diagnosing Subjective NLP Tasks ｜标注模式诊断：从标签聚合到标准有效性审计

作者：Nisrine Rair、Alban Goupil、Valeriu Vrabie 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a4324666abc3)

> 主观NLP任务中，将多标注者判断聚合为单一金标准会掩盖标准本身的模糊性，导致模型拟合错误模式或丢失有效信号。现有分歧建模方法多在标签层分析，假设标注模式（Schema）已足够清晰，无法区分分歧源于标准边界模糊还是标注者随机噪声。本文切入点在于前置审计：在构建金标准前，通过多标注者对二元标准的判断，量化标准的稳定性与类别的可分离性。其核心是提出基于条件重叠率与近平局率的模式诊断框架。该框架在商业文档采购场景下验证了分歧的结构化特征，但缺乏跨任务泛化验证，且依赖LLM面板可能引入模型同质化偏差。

】

---

【Beyond Screenshots: Evaluating VLMs’ Understanding of UI Animations ｜超越截图：视觉语言模型对UI动画理解的评估

研究机构：美国密歇根大学

作者：Chen Liang、Xirui Jiang、Naihao Deng 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_3aa785e0b023)

> 现有GUI智能体研究聚焦于静态截图的元素定位，忽略了界面中通过动态变换传达状态反馈的动画通道，导致模型无法完整解析用户交互逻辑。本文构建了首个包含专家与大众双重标注的UI动画数据集AniMINT，并系统评估了9个主流视觉语言模型在动画感知、目的分类与意义解释上的能力。实验表明，尽管模型能识别基础运动原语，但在高阶目的分类上准确率仅0.64，且解释常缺失关键细节。通过引入运动、上下文与感知线索（MCPC）增强，验证了多模态线索协同对提升动画理解的必要性，揭示了当前模型在动态UI理解上的显著短板。

】

---

【Beyond Semantic Similarity: Appraisal-Guided Chain-of-Thought Reasoning and Retrieval for Multimodal Emotional Support Conversations ｜认知评价引导的链式推理与检索

研究机构：合肥工业大学、新加坡管理大学

作者：Yuqi Chu、Lizi Liao、Jinggui Liang 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_dab706d54c41)

> 情感支持对话系统常因无法区分用户话语背后的心理评估机制，导致生成表面相关但治疗上不当的回复。现有检索增强生成方法依赖语义相似度，加剧了这种“认知差距”。本文通过显式建模认知评价链并以此作为检索查询，将范式从语义匹配转向认知共鸣。该方法在两个基准上超越了现有基线，但其评估指标与最新强化学习方法的缺失限制了结论的普适性。

】

---

【BOOKAGENT: Orchestrating Safety-Aware Visual Narratives via Multi-Agent Cognitive Calibration ｜多智能体认知校准故事书合成

研究机构：美国卡内基梅隆大学、中国科学技术大学

作者：Bo Gao、Chang Liu、Yuyang Miao 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.16541)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.16541)

> 多模态视觉叙事生成面临角色身份漂移与儿童内容安全缺失的双重瓶颈，现有方法多采用单向流水线或后处理过滤，难以实现全局一致性。本文切入点在于将安全审计前置至规划阶段，并引入全局时序校准机制，构建端到端闭环多智能体框架。通过价值对齐故事板、迭代跨模态精炼与时序认知校准三阶段协同，实现文本与图像的联合优化。该框架在高约束场景下显著提升了跨帧一致性，但其计算成本随页数线性增长，且缺乏对真实绘本分布的泛化验证。

】

---

【BRIEF-Pro: Universal Context Compression with Short-to-Long Synthesis for Fast and Accurate Multi-Hop Reasoning ｜短长合成与指令控制的通用上下文压缩

研究机构：美国加州大学洛杉矶分校

作者：Jia-Chen Gu、Junyi Zhang、Di Wu 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.13799)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9c4e840c17e8)

> 检索增强生成（RAG）在处理复杂多跳推理时，因检索文档过长导致推理延迟激增且模型认知负载过重。现有压缩方法要么依赖专有模型蒸馏，要么局限于短上下文且缺乏用户可控性。BRIEF-PRO 通过短上下文种子数据合成长上下文训练集，并引入指令条件化机制，实现了对 10k+ 词上下文的轻量级摘要压缩。该方法在保持高压缩比的同时提升了多跳问答准确率，但其对多跳依赖结构的线性化处理在复杂推理任务上存在性能瓶颈。

】

---

【CAMO: An Agentic Framework for Automated Causal Discovery from Micro Behaviors to Macro Emergence in LLM Agent Simulations ｜从微观行为到宏观涌现的因果发现框架

研究机构：天津大学

作者：Xiangning Yu、Yuwei Guo、Yuqi Hou 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.14691)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.14691)

> 生成式多智能体社会模拟能复现宏观涌现现象，但无法解释其背后的微观-宏观因果机制，导致干预策略缺乏可泛化性。现有方法或依赖静态变量空间的统计因果发现，或仅做定性演示，均无法在动态自适应环境中恢复可干预的因果结构。CAMO 通过分离“因果识别”与“机制解释”，利用多智能体协作与模拟器内部反事实干预，自动恢复目标涌现结果的最小充分因果接口。该框架在自建基准上实现了高保真的结构恢复与干预排序，但其有效性受限于模拟器内部日志的完备性，且未验证跨模拟器的泛化能力。

】

---

【Can Small LLMs Learn a Robust Theory of Mind via RLVR? Investigating Generalization through the False-Belief Task ｜强化学习可验证奖励能否赋予小模型通用心智理论？

研究机构：加拿大麦吉尔大学、美国纽约大学

作者：Sneheel Sarangi、Hanan Salam

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a5ede7f18be1)

> 该方向旨在验证大语言模型（LLMs）能否通过强化学习可验证奖励（RLVR）习得可泛化的心智理论（ToM），而非仅依赖统计捷径。现有RLVR在逻辑推理中表现优异，但在社交推理中是否同样有效尚存争议，且小模型在ToM基准上普遍存在分布外泛化失效问题。本文通过系统消融实验，训练7B参数模型在多种ToM数据集组合上进行RLVR，并评估其在保留基准上的迁移能力。研究揭示了RLVR在ToM任务中导致窄域过拟合而非抽象能力习得的机制，对“RL万能论”提出了关键反证，但其结论是否适用于更大规模模型仍存疑。

】

---

【CARE-CR: Context-Aware Routing and Expert Fusion for Multi-Preference Cognitive Restructuring ｜上下文感知路由与专家融合的认知重构

作者：Hongzhi Qi、Liangcheng Wang、Yijing YU 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ce3cf009b44e)

> 认知行为疗法中的认知重构旨在通过识别非理性信念并生成辩驳来缓解心理痛苦，但现有大语言模型方法往往陷入表面化的积极改写，缺乏对共情、理性等治疗维度动态权衡的机制。本文指出单一奖励模型无法适应不同情境下的偏好差异，提出CARE-CR框架，通过训练维度特定的专家策略并利用上下文感知路由进行动态融合，实现个性化认知重构。该方法在诊断准确性与临床效度上优于单一对齐基线，但其单轮评估协议与有限的数据规模限制了结论向多轮临床场景的泛化。

】

---

【CaRVE: Critiquing and Refining Visual Elaborations for Figurative Language Illustrations ｜视觉阐述批评与精炼框架

研究机构：印度理工学院孟买分校

作者：Manishit Kundu、Tejomay Kishor Padole、Sumit Shekhar 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c33a5945f70e)

> 修辞性语言图像生成面临的核心困境是语义漂移：模型倾向于将隐喻直接转化为字面图像，导致生成结果与修辞意图脱节。现有方案依赖闭源大模型或人工验证来弥合这一差距，限制了可扩展性与可访问性。CaRVE 通过引入视觉语言模型（VLM）作为语义批评者，对初始生成的图像进行条件化评估并反馈修正建议，从而在轻量级开源模型上实现语义对齐。该框架证明了批评机制比单纯扩大模型规模更有效，但其单轮精炼策略在复杂多层隐喻中的鲁棒性仍存疑。

】

---

【Causal Evidence Extraction and Triangulation in Crisis Reports using Large Language Models: A ReliefWeb-based Study ｜人道主义报告中的因果证据提取与三角测量

作者：Yuanjun Zhang、Mourad Oussalah

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_22879c8d5061)

> 人道主义危机报告冗长且多主题，传统关键词检索与无约束抽取导致大量噪声关系，难以支撑跨情境的决策支持。现有证据合成框架多针对主题纯净的文本，无法处理报告中心的复杂语境。本文提出查询条件化与片段接地两阶段流水线，并引入保留上下文的三角测量方法量化证据收敛性。该方法在专家标注集上实现了高加权F1，但评估规模小且局限于单一干预类型，其泛化能力存疑。

】

---

【CircuitSynth: Reliable Synthetic Data Generation ｜电路合成：基于概率句法决策图的可靠数据生成

研究机构：英国牛津大学、奥地利维也纳技术大学

作者：Zehua Cheng、Wei Dai、Jiahao Sun 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.10114)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.10114)

> 合成数据生成旨在突破真实数据稀缺与隐私限制，但大语言模型（LLM）在结构化生成中常因随机采样导致幻觉、逻辑不一致及模式坍缩，即长尾分布覆盖不足。现有提示工程或检索增强生成（RAG）方法缺乏对逻辑一致性与分布覆盖的形式化保证，无法同时满足硬逻辑约束与软分布目标。CircuitSynth 提出一种神经符号框架，通过将教师 LLM 的推理能力蒸馏至概率句法决策图（PSDD），构建可处理语义先验，并引入凸优化机制强制满足分布约束。该框架在复杂逻辑谜题中实现了 100% 模式有效性，显著优于基线，但其适用性受限于约束图的树宽，高维密集约束下的可扩展性存疑。

】

---

【CoDA: Restoring Contextual Dominance via Copy-Encouraged Attention Intervention for Mitigating RAG Hallucinations ｜基于复制鼓励注意力调度的RAG幻觉缓解

作者：JinWei Shi、Qizhuo Xie、Qianzi Hou 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_3668ec879d08)

> 检索增强生成（RAG）在证据准确时仍产生幻觉，根源在于Transformer内部参数化知识对上下文证据的压制。现有解码干预方法仅调整输出分布，未修正内部信息路由；FFN抑制方法虽触及内部机制，但全局抑制导致参数知识丧失。CoDA将幻觉归因于注意力路由失败，通过推理时动态增强证据对齐的值状态，恢复上下文在残差流中的主导地位。该方法在忠实度上优于FFN抑制基线，但其对非复制头的强制复制是否引入语义扭曲，论文未提供直接证据。

】

---

【CODEPROMPTZIP: Code-specific Prompt Compression for Retrieval-Augmented Generation in Coding Tasks with LMs ｜代码提示压缩

作者：Pengfei He、Shaowei Wang、Tse-Hsun Chen

论文原文见 [arXiv](https://arxiv.org/abs/2502.14925)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c07d2f7d9ca8)

> 检索增强生成（RAG）在代码任务中常因引入大量示例导致提示词长度激增，超出模型上下文窗口或产生高额API成本。现有通用压缩方法缺乏对代码语法结构的感知，盲目剔除Token易破坏代码逻辑。本文提出CodePromptZip，一种基于程序分析类型优先级与复制机制的硬压缩框架，旨在保留关键代码语义的同时实现可控比率压缩。该方法在三个代码任务上显著优于熵基与蒸馏基线，但其依赖静态分析工具的特性限制了在不可解析代码上的泛化能力。

】

---

【Comparing Human and Large Language Model Interpretation of Implicit Information ｜隐含信息提取中的人机认知对齐差异

研究机构：意大利米兰理工大学

作者：Antonio De Santis、Tommaso Bonetti、Andrea Tocchetti 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17085)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17085)

> 导读 大语言模型（LLM）在生成流畅文本时，常将字面意义与隐含意义混淆，导致其在需要推断言外之意的场景中表现保守或过度发散。现有评估多聚焦于显式事实抽取或单一维度的语义一致性，缺乏对“可推断内容”这一开放集合的结构化对比，无法量化模型与人类在推理边界上的具体分歧。本文提出隐含信息提取（Implicit Information Extraction, IIE）框架，通过构建双层知识图谱并引入众包人类判断作为基准，系统解析了模型在推断严格性、时间关系解析及共识形成上的行为特征。该研究揭示了LLM在社会语境下比人类更保守、在事实语境下人类更保守的反直觉现象，但受限于小样本规模与黑盒评估，其结论对模型内部机制的解释力仍存疑。

】

---

【COMPEL: Compensated Mixture-of-Experts Pruning with Expert-Layer distribution ｜补偿式混合专家剪枝与专家-层分布对齐

研究机构：韩国汉阳大学

作者：Seohee Yoon、Yong Suk Choi

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_53551d3bb491)

> 混合专家模型（Mixture-of-Experts, MoE）在推理时需将全部专家权重驻留内存，导致显存占用远超激活参数量，成为部署的核心瓶颈。现有专家剪枝方法多采用跨层统一剪枝率，忽视了不同层间专家冗余度的结构性差异，导致低冗余层中独特专家被误删，引发性能显著退化。COMPEL 将剪枝指标转化为连续优化问题，通过 Fisher 信息估计专家敏感度、层级离群分布量化层重要性，并引入 Fisher 引导的权重补偿机制。该方法在 25% 剪枝率下实现了近乎无损的性能保持，但在 50% 高压缩率下的精度边界及与 Shapley 值类方法的对比缺失，使其泛化能力存疑。

】

---

【Concept rather than Document: Context Compression via AMR-based Conceptual Entropy ｜基于抽象意义表示的概念熵上下文压缩

研究机构：澳大利亚悉尼科技大学、香港理工大学

作者：Kaize Shi、Xueyao Sun、Xiaohui Tao 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2509f5d14fe6)

> 导读 检索增强生成（RAG）场景下，长文档中的冗余信息常干扰大语言模型（LLM）对关键事实的提取，导致推理性能下降。现有压缩方法多依赖词法或Token级特征，易割裂语义单元，难以保留核心概念。本文提出基于抽象意义表示（Abstract Meaning Representation, AMR）的概念熵筛选框架，通过量化AMR节点的信息熵识别语义关键概念，重构紧凑上下文。该方法在PopQA和EntityQuestions上优于基线，但实验设置排除了检索噪声，且未对比最新软压缩方法，其泛化能力存疑。

】

---

【Corpora Generation for Urdu Grammatical Error Correction ｜基于形态句法内核的乌尔都语语法错误纠正合成数据生成

作者：Syed Ahad、Burhanuddin Aliasghar Ezzi、Muhammad Arsalan Hussain 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a786d156e429)

> 低资源语言语法错误纠正（GEC）面临标注平行语料极度稀缺的瓶颈，传统随机噪声注入无法捕捉人类错误的语言学分布。本文切入点在于利用维基百科修订历史挖掘自然错误模式，并通过形态句法内核约束将其施加于干净文本，从而生成高质量合成语料。该方法在自建基准上验证了合成数据的有效性，但其对短文本多错误场景的适应性及跨语言迁移性仍存疑。

】

---

【CVRH: Cross-modal Variational Role Hypergraph Network via Semantic Enhancement for Multi-modal Event Argument Extraction ｜跨模态变分角色超图网络

作者：Bangze Pan、Yang Li、Ruili Pu 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f2cd7f2e1137)

> 多模态事件论元抽取（MEAE）旨在从图文混合新闻中识别特定事件的所有参数及其角色，核心难点在于视觉实体与文本实体在语义上的混淆与跨模态关联缺失。现有方法多依赖单模态向量的弱对齐或数据增强，忽略了事件角色作为高阶结构对参数绑定的约束作用。CVRH 通过构建以角色为中心的变分超图，利用 LLM 生成的角色语义先验与动态变分向量初始化超边，显式建模跨模态参数间的高阶关联。该方法在 M2E2 基准上取得了 50.5 的 F1 分数，但缺乏与最新多智能体架构的绝对数值对比，其结构优势在复杂绑定场景下的泛化能力仍存疑。

】

---

【D-Artemis: A Deliberative Cognitive Framework for Mobile GUI Multi-Agents ｜移动GUI智能体的执行前对齐框架

研究机构：天津大学、香港中文大学

作者：Hongze Mi、Yibo Feng、Wenjie Lu 等 15 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.21799)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.21799)

> 移动GUI智能体在长程任务中面临单步错误导致轨迹偏离的累积效应，现有框架多依赖执行后反思，无法在动作生效前拦截失效。D-Artemis通过引入执行前对齐阶段，在动作执行前校验思维与动作的一致性并主动修正，解决了延迟检测带来的高恢复成本。该框架无需大规模轨迹数据训练，仅通过轻量级模块增强通用多模态大语言模型（MLLM）的GUI操作能力。其在AndroidWorld上取得75.8%的成功率，但相比在线强化学习（RL）方法仍存差距，且未验证极端分布外场景下的泛化边界。

】

---

【Data Swarms: Optimizable Generation of Synthetic Evaluation Data ｜数据群优化：合成评测数据生成的连续搜索范式

研究机构：美国华盛顿大学

作者：Shangbin Feng、Yike Wang、Weijia Shi 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_63c7c325dbc3)

> 现有合成评测数据生成方法依赖启发式提示工程，缺乏对数据质量的量化优化机制，导致生成结果难以稳定提升模型区分度或难度。本文提出 DATA SWARMS，将数据生成器视为权重空间中的粒子，通过粒子群优化（Particle Swarm Optimization, PSO）在连续参数空间中搜索最优生成策略，并引入对抗性共进化机制。该方法在四个领域上优于八种基线，但仅验证了文本任务，未解决多模态或长尾分布下的泛化问题。

】

---

【Decision Biases and Intent-Irony Decoupling in Large Language Models ｜意图-反讽解耦：LLM语用推理的机制诊断

研究机构：浙江大学

作者：Kewei Guo、Lingyun Sun、Manhao Guan

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8db6928373c2)

> 大语言模型在反讽理解中表现出高敏感度但低准确率的矛盾现象，现有基准仅能评估最终分类结果，无法区分模型是依赖深层心理模拟还是表面统计启发式。本文通过构建基于认知理论的多维评估框架，将反讽理解拆解为信念、意图、听众反应等五个子任务，并引入信号检测理论分离敏感度与决策偏差。实验揭示了LLM存在“意图-反讽解耦”现象，即能提取语用线索却无法将其整合进最终判断。该研究提供了机制诊断的新范式，但其结论是否可推广至其他高阶心智理论任务尚存疑问。

】

---

【Decoupled Reasoning with Implicit Fact Tokens (DRIFT): A Dual-Model Framework for Efficient Long-Context Inference ｜解耦推理与隐式事实Token

研究机构：复旦大学、同济大学

作者：Wenxuan Xie、Yujia Wang、Xin Tan 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.10021)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.10021)

> 长上下文推理面临计算复杂度与有效信息利用率的双重瓶颈，现有静态压缩方法在极端压缩比下易丢失任务关键信息，而参数化知识编辑又面临灾难性遗忘风险。DRIFT 通过双模型架构将知识提取与核心推理解耦，利用轻量级知识模型将文档压缩为查询感知的隐式事实Token，再投影至推理模型嵌入空间。该设计在保持推理模型参数冻结的前提下实现了32倍压缩比下的性能提升，但其对大规模模型扩展性及隐式表示的可解释性边界尚存疑。

】

---

【DeCoVec: Building Decoding Space based Task Vector for Large Language Models via In-Context Learning ｜解码空间任务向量

研究机构：深圳大学

作者：Feiyang Li、Yile Wang

论文原文见 [arXiv](https://arxiv.org/abs/2604.11129)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d49479e2329b)

> 大语言模型（LLMs）在特定任务上的表现往往受限于预训练阶段的通用分布，微调虽能提升性能但伴随高昂的计算成本与参数侵入性。现有任务向量方法多依赖权重差或激活状态干预，难以在冻结模型中实现轻量级引导。DECOVEC 提出在解码 logit 空间通过对比少样本与零样本上下文构建任务向量，直接注入生成过程以替代微调。该方法在 0.5B 至 9B 模型上验证了免训练引导的有效性，但其双前向传播机制带来的推理延迟与向量跨任务泛化能力仍存疑。

】

---

【Detecting AI-Generated Video: A Vision–Language Dual-View Survey ｜AI生成视频检测：从伪影匹配到事实保真度验证

研究机构：中国人民大学、美国哈佛大学

作者：Dylan Xinming Hou、Juntian Zhang、Xu Gu 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_fd5ea6ac87df)

> 现有AI生成视频检测依赖低层视觉伪影，但高保真生成模型已消除这些痕迹，导致检测器失效。本文提出“事实保真度验证”范式，将检测重构为对视频内容是否符合真实世界物理与逻辑规则的语义校验。通过构建视觉-语言双视图四层分类体系，整合从像素级伪影到世界知识推理的证据链。该框架为可解释检测提供了结构化路线图，但其作为综述未提供统一基准下的量化对比，各层方法的实际增益边界尚不明确。

】

---

【DiffCL: Difference-Aware Contrastive Learning for Automatic Answer Grading with Multi-Level Semantic Modeling ｜差异感知对比学习自动答题评分

作者：Lei Chen、BoYu Gao、Zitao Liu 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_43de595b3a01)

> 自动答题评分（AAG）的核心难点在于模型难以区分学生答案与参考答案的细微语义偏差，导致评分尺度不稳定。现有大语言模型（LLM）评分方法往往依赖表面流畅度，对关键概念遗漏不敏感，且内部表示空间缺乏评分结构优化。本文切入点是将启发式生成的离散差异标签注入输入，并引入双对比学习机制以约束表示空间。该方法在 SciEntsBank 基准上超越了零样本 GPT-4.1，但在 Beetle 数据集上表现低于多智能体框架，其泛化边界尚存疑。

】

---

【DMSD: Dual-Modal Semantic Disentanglement for Compositional Zero-Shot Learning ｜双模态语义解耦用于组合零样本学习

研究机构：四川大学、南京大学

作者：Pan Yang、Jing Yang、Ruan Xiao li 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_01081d3827c0)

> 组合零样本学习（Compositional Zero-Shot Learning, CZSL）旨在从已见属性-对象组合泛化至未见组合，其核心瓶颈在于视觉特征中属性与对象的纠缠。现有基于视觉语言模型（Vision-Language Models, VLMs）的方法多依赖文本侧提示调优，导致视觉子概念解耦不足，模型易受文本先验偏差影响。本文提出双模态语义解耦框架（Dual-Modal Semantic Disentanglement, DMSD），通过共享上下文提示空间与视觉子概念原型，在视觉与文本模态中同步实现细粒度解耦。该框架在封闭与开放世界设置下均取得领先性能，但其对高维视觉特征空间的依赖可能引入过拟合风险，且未充分挖掘视觉模态的内在结构潜力。

】

---

【Do Domain-specific Experts exist in MoE-based LLMs? ｜领域特定专家的存在性验证与无训练路由干预

作者：Giang Do、Hung Le、Truyen Tran

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9560f1be8794)

> 稀疏混合专家（Sparse Mixture-of-Experts, SMoE）架构在提升模型容量的同时，其内部专家是否真正形成了可解释的领域分工，长期缺乏实证依据。现有研究多聚焦于通过修改架构或损失函数来“促进”专业化，却未验证专业化是否真实存在，更未探索如何利用这种潜在的分工结构进行零成本推理优化。本文通过梯度归因量化专家对特定领域的贡献度，证实了领域特定专家的存在，并据此提出 Domain Steering Mixture of Experts (DSMoE)，在推理阶段对路由权重进行线性缩放以激活特定专家。该方法在 MMLU-Pro 和 GPQA Diamond 上实现了显著的性能增益，但其效果高度依赖领域数据的分布特性，且未验证在混合领域任务中的鲁棒性。

】

---

【Do Transformers Grok Succinct Algorithms? Mechanistic Evidence for Counting Circuits ｜简洁性假设下的Transformer算法发现机制

作者：Yizheng Zhao

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_3b0ae634621f)

> 现有理论认为固定精度Transformer能以多项式参数表示指数状态空间，但梯度训练常陷入启发式捷径而非收敛至理论预测的简洁电路。本文通过LARGECOUNTER任务验证这一“表达力-可学习性”鸿沟，发现高权重衰减诱导的Grokking相变是模型放弃记忆、发现算法电路的关键。实验证实2层Transformer完美泛化而LSTM彻底失败，但结论局限于合成计数任务，其在自然语言复杂推理中的普适性仍存疑。

】

---

【Does Chain-of-Thought Reasoning Help Mobile GUI Agents? An Empirical Study ｜推理增强对移动GUI智能体有效性的实证评估

作者：Li Zhang、Longxi Gao、Mengwei Xu

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_44409ae599a2)

> 移动GUI智能体在真实动态环境中面临多步交互与视觉布局复杂性，现有基于监督微调或强化学习的模型在长程任务中仍存在错误累积与泛化不足。本文切入点在于质疑“推理能力必然提升GUI操作性能”的假设，通过对比六组具备与不具备推理能力的视觉语言模型（VLM）在静态与动态基准上的表现，量化推理带来的性能增益与资源开销。研究发现推理在静态基准上收益微弱甚至负向，仅在特定动态场景下对特定模型有效，且伴随显著的Token膨胀。该研究揭示了推理机制在GUI任务中的局限性，但受限于未训练新模型，其结论对推理与训练范式协同作用的解释力有限。

】

---

【Does Theory of Mind Improvement Really Benefit Human-AI Interactions? Empirical Findings from Interactive Evaluations ｜从静态问答到动态交互：心智理论增强技术的人机协同效用评估

研究机构：美国亚利桑那州立大学、香港科技大学

作者：Nanxu Gong、Zixin Chen、Haotian Li 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.15205)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.15205)

> 大语言模型的心智理论（Theory of Mind, ToM）旨在推断他人心理状态，但现有评估多依赖静态故事问答，无法反映真实人机交互（Human-AI Interaction, HAI）中的动态性与开放性。本文指出静态基准成绩提升未必转化为实际交互收益，提出将ToM评估从第三人称视角转向第一人称动态对话。通过对比四种增强技术在目标导向与体验导向任务中的表现，发现其在体验任务中有效但在目标任务中失效，且用户感知差异极小。这一发现揭示了当前ToM增强方法在功能转化上的局限，其结论对依赖静态指标优化模型社交能力的研究路径构成直接挑战。

】

---

【Dual Hierarchical Dialogue Policy Learning for Legal Inquisitive Conversational Agents ｜双智能体层级强化学习在法律探究式对话中的应用

研究机构：美国乔治城大学、新加坡管理大学

作者：Xubo Lin、Zezhi Deng、Shihao Wang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.14057)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b9fcd0adfb7c)

> 现有任务导向对话系统假设用户与系统共享目标，难以应对司法听证等对抗性场景。传统协作式代理无法主动挖掘隐藏信息或应对律师的回避策略，导致在高风险决策中失效。本文提出双智能体层级强化学习框架，将对话策略解耦为评估与生成两个独立决策过程，以最大化信息增益。该方法在最高法院数据集上优于基线，但其通用性及跨领域泛化能力尚未得到验证。

】

---

【Dual-Reasoner: Bridging Interleaved Atomicity and Streaming Latency via Thinking-while-Talking ｜流式思维链的原子性重建与延迟掩盖

研究机构：厦门大学、吉林大学

作者：Yangzhuo Li、Shengpeng Ji、Yifu Chen 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b82f9c862b80)

> 语音对话模型引入思维链（Chain-of-Thought, CoT）以提升推理能力，但串行推理导致首包延迟（Time-to-First-Audio, TTFA）高达20秒，违背实时交互要求。现有“边想边说”方法通过机械截断降低延迟，却破坏了推理步骤的语义完整性，导致逻辑断裂与幻觉。本文提出Dual-Reasoner架构，通过流式掩盖机制解决物理延迟，并引入原子一致性恢复框架重建逻辑连贯性。该方案在保持高推理准确率的同时将TTFA降至3.65秒，但其在长程多步推理中的全局记忆保持能力仍存疑。

】

---

【DualAlign: Generating Clinically Grounded Synthetic Data ｜双重对齐临床合成数据生成

作者：Rumeng Li、Xun Wang、Hong Yu

论文原文见 [arXiv](https://arxiv.org/abs/2509.10538)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.10538)

> 临床电子健康记录（EHR）受隐私法规严格限制，导致阿尔茨海默病（AD）等慢性病的纵向轨迹数据稀缺，而通用大语言模型（LLM）生成的文本缺乏疾病特异性与时间连贯性。现有方法多聚焦于结构化数据或无约束的通用文本生成，无法捕捉AD跨认知、功能及生理领域的复杂交互。DualAlign通过引入人口统计学统计对齐与症状轨迹语义对齐，构建了具备临床合理性的合成叙事框架。该框架在低资源场景下提升了症状分类性能，但其对长期时序动态的压缩处理仍存疑。

】

---

【DualFact+: A Multimodal Fact Verification Framework for Procedural Video Captioning ｜程序性视频字幕的双层事实评估框架

作者：Cennet Oguz、Yasser Hamidullah、Josef van Genabith 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8d999e064354)

> 程序性视频字幕生成要求模型不仅识别动作，还需准确分配角色（如食材、工具），但现有评估指标仅关注表面词汇重叠或全局语义相似度，无法捕捉角色错位与论元缺失。本文切入点在于将事实性评估解耦为抽象角色语义与视觉接地谓词-论元结构两个层级，通过自然语言推理（NLI）模型验证事实支持度。该框架揭示了多模态大语言模型在流畅性掩盖下的系统性事实遗漏，其价值在于提供了可解释的细粒度诊断工具，但受限于单一生成骨干的验证范围。

】

---

【EduMARS: Can Vision-Language Models Grade Like Teachers? Benchmarking Multimodal, Rubric-Based Assessment on Chinese K-12 Answers ｜基于检索增强自适应量规的多模态K-12评分基准与框架

作者：Xuan Zhao、Jiashun Chen、Wanting xu 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_eafe03c214f5)

> 自动评分长期面临真实手写噪声与细粒度评分逻辑缺失的双重挑战，现有基准多依赖合成文本或仅标注最终分数，无法验证模型是否真正理解教师评分过程。本文切入点在于构建首个包含真实手写图像与步骤级评分理由的多模态基准，并设计动态量规合成框架以对齐专家逻辑。其核心做法是提取题目关键点，检索专家评分先验，动态生成案例特定量规后执行步骤级验证。该工作揭示了当前多模态大语言模型在评分过程重建上存在显著性能断层，但检索依赖性与学科覆盖局限仍制约其泛化边界。

】

---

【Embedding-based In-Context Prompt Training for Enhancing LLMs as Text Encoders ｜嵌入基上下文提示训练

研究机构：日本东京科学大学

作者：Ailiang Lin、Zhuoyun Li、Keyu Mao 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_3d4c1ff535b3)

> 导读 文本嵌入模型在检索增强生成（RAG）等场景中需平衡语义精度与推理延迟，而基于大语言模型（LLM）的嵌入方法常因引入离散文本演示导致序列长度膨胀，显著增加计算开销。现有方案或牺牲精度换取速度，或依赖双向注意力改造破坏LLM原生指令跟随能力，难以兼顾效率与表示质量。本文提出EPIC，将离散文本演示压缩为连续向量嵌入，在保留因果注意力的同时实现高效上下文学习。该方法在公开检索数据上刷新MTEB基准，但其在低资源语言及非检索任务上的泛化能力尚待验证。

】

---

【Emergence and Localisation of Semantic Role Circuits in LLMs ｜语义角色电路的因果定位与时间涌现

研究机构：英国曼彻斯特大学

作者：Nura Aljaafari、Danilo Carvalho、Andre Freitas

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1d11346a4cab)

> 大语言模型（LLMs）在事实回忆和算术任务中已被证实存在局部化电路，但抽象语义结构（如谓词-论元绑定）是否由因果功能性的内部机制实现，仍缺乏直接证据。现有机制可解释性研究多聚焦于静态检查点或特定算法行为，忽略了语义电路在训练过程中的形成时序与跨规模迁移性。本文提出 COMPASS 方法，结合对比最小对、边归因电路发现与训练时间追踪，揭示语义角色电路的局部化、渐进涌现及跨架构保守性。该工作为浅层语义结构的机制解释提供了因果证据，但受限于浅层角色定义与单一任务范式，其结论向深层语义泛化的边界尚不明确。

】

---

【Emotion Trajectory-aware Retrieval for Markov-driven Emotion Anticipation in LLM-based Emotional Support Conversation ｜基于情感轨迹检索的马尔可夫情感预测框架

研究机构：国防科技大学、重庆大学

作者：Hongyan Wu、Zhiliang Tian、Zhen Huang 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8a1a273650b9)

> 情感支持对话（ESC）的核心挑战在于策略规划往往局限于当前轮次，忽视用户情感的动态演进，导致回复虽流畅但缺乏长期适应性。现有检索增强方法仅匹配单点情感状态，无法捕捉跨轮次的情感依赖关系。本文通过构建动态情感记忆并引入马尔可夫链预测未来情感，将策略选择从即时反应转变为前瞻规划。该框架在ESConv和ExTES数据集上显著优于基线，但其依赖词典提取的情感轨迹精度及马尔可夫假设的长程有效性仍存疑。

】

---

【EMPATH: An Ensemble Method for Automatic Fine-Grained Turn-Level Dialogue Empathy Evaluation with a Novel Emotional Distance Metric ｜基于情感距离与霍夫曼顺序集成的细粒度共情对话评估框架

作者：Dongning Rao、Zhihua Liang、Zhihua Jiang

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_630cd3b13a0d)

> 共情对话评估长期受困于自动指标与人类判断的低相关性，现有微调模型虽精度高但缺乏可解释性且未充分利用经典对话指标。本文切入点在于构建一个融合心理学理论、情感对齐度量与经典指标的集成框架，通过霍夫曼顺序策略整合多源信号以克服单一模型的偏差。EMPATH 在 WASSA 和 EX 数据集上均优于冠军基线，但其对预训练情感分类器的依赖及 LLM 裁判的潜在偏见仍构成评估鲁棒性的主要隐患。

】

---

【Empathy Applicability Modeling for General Health Queries ｜共情适用性框架

研究机构：美国密歇根大学

作者：Shan Randhawa、Agha Ali Raza、Kentaro Toyama 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.09696)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_fe743943bf4d)

> 临床沟通中的核心矛盾在于，医生常因过度聚焦诊断而忽略患者的情感需求，导致共情缺失。现有共情响应生成研究默认“共情总是必要的”，缺乏对“何时不应共情”的前置判断机制。本文提出共情适用性框架（Empathy Applicability Framework, EAF），通过二元分类预测患者查询中情感反应与认知解释的必要性。该框架填补了异步单轮医疗场景下的前置决策空白，但其二元标签是否足以捕捉临床共情的细微程度差异，仍存疑。

】

---

【FedGUI: Benchmarking Federated GUI Agents across Heterogeneous Platforms, Devices, and Operating Systems ｜联邦GUI智能体异构基准

研究机构：浙江大学、上海交通大学

作者：Wenhao Wang、Haoting Shi、Mengying Yuan 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.14956)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.14956)

> 联邦学习（Federated Learning, FL）旨在解决GUI交互数据因隐私限制无法集中存储的困境，但现有基准仅覆盖单一移动平台，无法量化跨Web、桌面及多操作系统间的分布偏移。FedGUI通过构建覆盖900+移动应用、40+桌面应用及200+网站的六类数据集，系统建模了跨平台、跨设备、跨OS及跨数据源四种异构性。实验证实跨平台协作能挽救单域模型的失效，但联邦训练在极端偏斜分布下的性能仍显著低于集中式训练。该基准填补了分布式GUI训练评测空白，但其绝对性能上限受限于缺乏强化学习机制。

】

---

【FeedEval: Pedagogically Aligned Evaluation of LLM-Generated Essay Feedback ｜教学对齐的反馈质量评估框架

研究机构：韩国科学技术院

作者：SeongYeub Chu、Jongwoo Kim、Mun Yong Yi

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_86531433e545)

> 自动写作评估（AWE）的核心痛点已从分数预测转向反馈的教学效用，但现有流程盲目信任大语言模型（LLM）生成的反馈，导致低质量噪声污染下游训练。本文切入点在于构建一个独立于生成器的评估器，对候选反馈进行多维度质量筛选。通过训练三个维度特定的 LLM 评估器，FeedEval 实现了与人类专家判断的高对齐，并验证了筛选后反馈能显著提升评分模型性能。其价值在于提供了可量化的反馈质量代理指标，但评估器本身依赖合成数据构建，其泛化边界尚存疑。

】

---

【FineState-Bench: Benchmarking State-Conditioned Grounding for Fine-grained GUI State Setting ｜细粒度状态条件化 GUI 定位基准

研究机构：美国东北大学

作者：Fengxian Ji、Jingpu Yang、Zirui Song 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.27974)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.27974)

> 现有 GUI 定位基准仅验证“点击是否命中控件”，忽略了点击后界面状态是否精确达成目标值，导致模型在滑块调节、日期选择等连续交互任务中看似成功实则失效。本文切入点在于将定位任务解耦为“控件定位”与“操作核心命中”两个独立阶段，并引入精确目标状态标签进行验证。通过构建包含双区域标注的静态基准与阶段式诊断指标，量化了视觉定位误差对最终状态达成的可恢复增益。该工作揭示了当前 SOTA 模型在细粒度状态控制上的巨大盲区，但其单步静态协议是否足以反映动态交互中的状态漂移，仍存疑。

】

---

【FLARE: Task-agnostic embedding model evaluation through a normalization process ｜基于归一化流的无标签嵌入模型评估

研究机构：香港科技大学

作者：Jingzhou Jiang、Yixuan Tang、Yi Yang 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17344)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17344)

> 在专有语料库缺乏标注数据时，如何可靠地预测文本嵌入模型的下游任务排名？现有基于核密度估计或几何指标的无标签评估方法在高维空间中失效，导致排名与真实性能脱节。FLARE 通过引入归一化流（Normalizing Flows）精确估计信息充分性，将评估误差依赖从原始维度转移至内在维度，解决了高维密度估计的稳定性问题。该方法在11个数据集上实现了与监督基准高达0.90的Spearman相关系数，但在低维场景及跨语言泛化性上仍缺乏充分验证。

】

---

【FLOP-Efficient Training: Early Stopping Based on Test-Time Compute Awareness ｜测试时计算感知训练

研究机构：华为、加拿大滑铁卢大学

作者：Hossam Amer、Maryam Dialameh、Hossein Rajabzadeh 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.01332)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.01332)

> 大语言模型训练面临算力与精度的刚性约束，传统范式将全部预算投入训练阶段，忽视了推理阶段通过多次采样提升精度的潜力。现有早停方法仅监控验证集准确率，无法感知测试时计算（Test-Time Compute, TTC）带来的精度增益，导致在固定总预算下无法实现最优的精度-成本帕累托前沿。本文提出TTC感知训练框架，通过拟合学习曲线预测最终精度，并联合优化早停时机与推理采样次数 $K$，在保持或提升精度的同时大幅削减训练FLOPs。该范式打破了“训练必须完整”的隐含假设，但在高推理成本场景下的盈亏平衡点仍需更严格的实证验证。

】

---

【FreezeEmpath: Efficient Training for Empathetic Spoken Chatbots with Frozen LLMs ｜冻结大语言模型的语音共情对话生成

研究机构：中国科学院、中国科学院大学

作者：Yun Hong、Yan Zhou、Yang Feng

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c26962761650)

> 语音共情对话系统旨在让机器捕捉语音韵律中的情感线索并生成具有共鸣的语音回复，但现有方法依赖高成本的情感语音指令数据且微调大语言模型易导致灾难性遗忘。FreezeEmpath 抓住“大语言模型已具备固有共情能力”这一被忽略的前提，通过语义-情感解耦编码与两阶段对齐训练，在完全冻结大语言模型的前提下实现语音共情对话。该方法以低成本自监督数据替代人工标注，验证了冻结架构在情感表达与通用能力保持上的有效性，但其对复杂情感动态的深层推理能力仍受限于未微调的骨干网络。

】

---

【From Outcome to Process: Optimizing MoE Load Balancing with MCTS ｜基于蒙特卡洛树搜索的LoRA-MoE层级负载均衡

研究机构：东南大学、澳门大学

作者：Wenjun Ke、Hengyuan Xu、Ziyu Shang 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4f1df957d029)

> 混合专家模型在参数高效微调中面临专家激活坍缩，即少数专家主导计算而多数闲置，导致容量浪费。现有方法仅在最终损失层面施加平衡约束，忽略了路由决策在层间累积的偏差。本文提出LayerMoE，将专家选择重构为序列决策问题，利用蒙特卡洛树搜索（MCTS）生成层级奖励信号，在训练阶段引导门控机制实现过程级负载均衡。该方法在多个基准上提升了LoRA-MoE基线的平均准确率，但实验规模局限于单卡小模型，且未验证MCTS在大规模预训练场景下的可扩展性。

】

---

【From Pseudo-Balancing to True Specialization: Memory-Aware Routing for Mixture-of-Experts ｜记忆感知路由

研究机构：北京大学、阿里巴巴集团

作者：Peixuan Hou、Yunbo Hou、Bin Chen 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_397698e75146)

> 混合专家（Mixture-of-Experts, MoE）模型在引入负载均衡损失后，常陷入“伪平衡”陷阱：为追求专家利用率均匀，同一输入在不同训练步被随机分配至不同专家，导致语义对齐失效与参数冗余。现有方法仅从参数或分布层面干预，未能解决路由决策的时序不稳定问题。本文通过为每个专家引入记忆缓冲区，将历史Token表示转化为偏好向量，并以此修正路由分数，实现训练阶段的语义一致性引导。该方法在保持全局负载均衡的同时显著提升了专家专业化程度，但其效果依赖于训练阶段的记忆维护，推理阶段需依赖基础路由器已内化的策略，其长期泛化能力尚存疑。

】

---

【From Script to Stage: Automating Experimental Design for Social Simulations with LLMs ｜从剧本到舞台：LLM社会模拟实验设计的自动化框架

研究机构：天津大学、山东大学

作者：Yuwei Guo、Zihan Zhao、Xiaowei Liu 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1d59bef85a8d)

> 生成式多智能体社会模拟旨在通过大语言模型（LLM）复现复杂社会动力学，但传统实验设计依赖跨学科专家的高成本介入，导致研究门槛高且难以规模化。现有LLM驱动框架虽降低了操作壁垒，却因缺乏结构化约束而难以保证实验的科学严谨性与变量可控性。FSTS框架借鉴电影制作流程，将实验设计解耦为剧本创作、定稿与演员生成三个阶段，通过多智能体协作自动编译高层研究意图为可执行脚本。该框架在古巴导弹危机场景中实现了与历史结局的一致性复现，但其对单一历史事件的依赖及语义相似度指标的局限性，使其在通用科学验证层面的有效性仍存疑。

】

---

【From What Is Said to Why It Is Framed: Intent-Aware News Video Understanding ｜意图条件化的新闻视频理解

研究机构：新加坡南洋理工大学、新加坡国立大学

作者：Xiangzheng Kong、Minnan Luo、Wenya Wang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a48340f007d6)

> 短新闻视频通过视觉框架与情感信号进行策略性呈现，现有验证方法常将制作风格误判为事实操纵，导致捷径学习。本文提出Origin-Objective-Means（OOM）框架，将沟通意图解耦为创作者立场、受众需求激活与传播策略三个维度，并作为中间语义条件而非预测目标注入推理与检测流程。通过Intent-Guided Prompting（IGP）与ICMD框架，在FakeSV与FakeTT上验证了意图条件化对检测鲁棒性的提升。该方法在特定基准上达到SOTA，但意图标签依赖人工标注且分布不平衡，其跨域泛化能力存疑。

】

---

【G-HiRel: Enhancing the Adaption to Knowledge Updating for Large Language Model Reasoning ｜层级关系检索增强知识编辑推理

研究机构：西北工业大学

作者：Yudai Pan、Jiajie Hong、Tianzhe Zhao 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_5dcec26db25e)

> 大语言模型在参数冻结状态下难以适应大规模知识更新，尤其在多跳推理中，直接修改参数成本高昂且易引发灾难性遗忘。现有外部记忆方法虽能规避参数更新，但受限于知识图谱（KG）结构化三元组与LLM连续表示间的语义鸿沟，以及实体依赖导致的知识不一致。本文提出G-HiRel，通过层级指令生成与基于关系语义的多步扩展检索，将KG中的关系路径而非实体作为推理骨架，实现编辑后知识的鲁棒整合。该方法在MQuAKE基准上显著提升了多跳推理准确率与路径可解释性，但其性能高度依赖底层LLM的指令解析能力，且未解决检索延迟与长程依赖建模的系统性瓶颈。

】

---

【Generative-to-Discriminative Test-Time Adaptation via Manifold-Aware Diffusion and Bayesian Distillation ｜生成-判别式测试时适应

研究机构：浙江大学

作者：Boyun Zhang、Zequn Xie、Fangming Feng 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_cb106a93019c)

> 测试时适应（Test-Time Adaptation, TTA）旨在解决模型部署后因分布偏移导致的性能衰退，其核心在于利用无标签测试数据在线修正模型参数。现有判别式方法依赖“高置信度即正确”的假设，在严重偏移下易陷入“自信但错误”的陷阱，而生成式模型虽具备鲁棒性却受限于迭代去噪的高延迟。本文提出 GD-Adapt，通过贝叶斯扩散蒸馏将生成教师的鲁棒性转移至轻量级判别学生，并引入流形估计器过滤分布外样本。该方法在跨域情感分析任务上显著提升了回归精度，但其异步适应机制对实时同步性的影响尚存疑。

】

---

【Ghost in the Shell: Synonym-Aware Logit Shaping Fingerprint for Copyright Protection of Large Vision-Language Models ｜同义词感知Logits塑形指纹

研究机构：北京大学

作者：Xiaofan Zheng、Xinghao Wang、Xiaojun Wan

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e19cd7208267)

> 大型视觉语言模型（LVLMs）的黑盒所有权验证面临鲁棒性与无害性的固有冲突：现有后门范式通过扭曲显式输出嵌入指纹，导致模态对齐破坏与多模态能力退化。本文提出同义词感知Logits塑形指纹（SALSF），将指纹嵌入从显式文本输出迁移至隐式Logits长尾空间，通过提升同义词簇概率而锁定Top-1预测，在保持模型通用性能的同时增强对抗鲁棒性。该方法在LVLM指纹任务中显著优于当前SOTA，但其对Logprobs API的依赖及同义词集规模的敏感性限制了其在严格黑盒场景下的普适性。

】

---

【GRASS: Gradient-based Adaptive Layer-wise Importance Sampling for Memory-efficient Large Language Model Fine-tuning ｜基于梯度范数的自适应层采样微调

研究机构：国防科技大学

作者：Kaiyuan Tian、Yu Tang、Gongqingjian Jiang 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.07808)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.07808)

> 大语言模型全参数微调受限于GPU显存瓶颈，而低秩适配方法虽节省内存却牺牲了模型表达力。现有层选择式微调方法依赖静态、任务无关的层重要性假设，无法适应不同任务和训练阶段下层重要性的动态变化。GRASS通过引入平均梯度范数（Mean Gradient Norm, MGN）作为动态重要性指标，并配合层级优化器状态卸载机制，实现了内存高效且性能接近全参数微调的自适应层采样。该方法在算术与常识推理基准上取得了显著的性能提升，但其对梯度统计量的依赖是否在所有优化景观下均具鲁棒性，仍需进一步验证。

】

---

【GUITester: Enabling GUI Agents for Exploratory Defect Discovery ｜探索性GUI缺陷检测智能体

研究机构：北京交通大学、新加坡南洋理工大学

作者：Yifei Gao、Jiang Wu、Xiaoyi Chen 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.04500)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.04500)

> 探索性GUI测试旨在无预设脚本条件下自主发现软件缺陷，但现有GUI智能体因“目标导向掩盖”与“执行偏差归因”两大缺陷，无法有效执行此任务。本文指出，智能体为追求任务成功率而主动绕过异常，并将系统故障误判为自身操作失误，导致缺陷在质量保障流程中不可见。GUITester通过解耦导航与验证，引入主动探测与层级反思机制，在GUITestBench上将F1分数从基线的33.35%提升至48.90%。该工作验证了自动化探索性测试的可行性，但其对复杂多动作缺陷的识别能力仍受限于样本规模与归因逻辑的泛化性。

】

---

【Half-S: Halving the Scale for Near-Lossless 4-Bit LLM Training ｜半缩放策略

研究机构：香港中文大学、北京航空航天大学

作者：Jinyang Du、Ruihao Gong、Linghan Ai 等 12 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_81cd504c19f0)

> 4-bit大语言模型训练因动态范围极窄而面临数值稳定性挑战，现有基于块最大值的缩放策略在重尾分布下导致低幅值区域量化网格利用率低下。本文指出该失效源于表示坍缩，即大量不同输入映射至相同的低幅值层级。通过推导重尾分布下的MSE最优裁剪阈值，提出将缩放因子减半的Half-S策略以逼近理论最优。该策略以极低的计算开销实现了接近BF16的收敛质量，但其有效性边界在长周期训练与复杂架构下的泛化性尚存疑。

】

---

【HER: Human-like Reasoning and Reinforcement Learning for LLM Role-playing ｜双层思维与生成式奖励的角色扮演强化学习

研究机构：复旦大学、MiniMax

作者：Chengyu Du、Xintao Wang、Aili Chen 等 14 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.21459)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.21459)

> 导读 角色扮演智能体（Role-Playing Agents, RPAs）的核心矛盾在于模型能模仿角色语气，却难以复现驱动行为的内在动机，导致长程对话中认知逻辑断裂。现有方法要么缺乏显式推理轨迹的监督数据，要么依赖静态规则或可验证事实构建奖励信号，无法适应场景动态变化。本文提出 HER 框架，通过分离系统思维与角色思维的双层结构，结合反向合成数据管道与生成式奖励模型（Generative Reward Model, GenRM），在 Qwen3-32B 上实现认知层面的角色模拟。该框架在 CoSER 基准上取得 53.12 分，显著优于同规模基线，但绝对性能仍落后于顶级商业模型，且其原则集静态化限制了长程场景适应性。

】

---

【High-Throughput and Memory-Efficient Zeroth-Order Fine-tuning LLMs with Distributed Parallel Computing ｜分布式零阶微调的并行化与通信优化

研究机构：沙特阿拉伯阿卜杜拉国王科技大学

作者：Liangyu Wang、Huanyi Xie、Di Wang

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4c512f111535)

> 大语言模型全参数微调受限于显存与算力，零阶优化（ZO）虽通过消除反向传播降低显存占用，但单卡执行导致吞吐量瓶颈，且现有分布式框架无法利用其双前向结构。DistZO2 提出扰动并行（PertP）与适配标量梯度的数据并行，结合硬件感知通信切片，将 ZO 微调扩展至 CPU+多 GPU 异构系统。该方法在 OPT-175B 上实现了 3 倍加速，但缺乏与一阶优化在同等资源约束下的公平对比，其收敛性边界仍存疑。

】

---

【HisDoc-OCR: Restoring Visual Grounding in MLLMs for Chinese Historical Document OCR ｜中文历史文档OCR中的视觉接地恢复

研究机构：华南理工大学

作者：Jiahuan Cao、Yongxin Shi、Zeyu Shan 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c38988444613)

> 多模态大语言模型（MLLMs）在处理中文历史文档时，因视觉证据退化与语言先验冲突，常产生字符伪造与重复等幻觉。现有通用模型缺乏针对历史版式与古字体的对齐机制，导致识别精度与稳定性双低。本文通过布局注入、首次出现增强与自蒸馏注意力聚焦，在训练阶段重塑视觉-文本对齐。该方法在幻觉抑制上表现突出，但在纯识别精度上未超越专用布局感知模型，其通用性仍存疑。

】

---

【How Large Language Models Balance Internal Knowledge with User and Document Assertions ｜三元来源交互下的 LLM 决策平衡与区分能力评估

研究机构：新加坡南洋理工大学、美国加州理工学院

作者：Shuowei Li、Haoxin Li、Wenda Chu 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.22193)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_52003acd71b6)

> 检索增强生成（RAG）与对话系统要求大语言模型（LLM）在参数化知识、用户断言与文档断言三者间进行动态权衡，但现有研究多局限于“参数-上下文”二元冲突，忽略了用户与文档作为独立来源时的差异化权重及交互效应。本文提出三元交互评估框架，通过13种探针变体量化27个模型对三源的依赖模式，发现模型普遍偏好文档断言且易受外部信息误导（“易感”型），并验证了混合监督微调（SFT）能显著提升模型区分有益与有害信息的能力。该工作填补了多源交互评估的空白，但其结论是否泛化至开放域长文本场景仍存疑。

】

---

【How Retrieved Context Shapes Internal Representations in RAG ｜检索增强生成中检索上下文对内部表征的塑造机制

作者：Samuel Yeh、Sharon Li

论文原文见 [arXiv](https://arxiv.org/abs/2602.20091)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2abd8adf8981)

> 检索增强生成（Retrieval-Augmented Generation, RAG）旨在通过外部文档弥补大语言模型（LLM）参数化知识的滞后与缺失，但实际检索结果常混杂相关、干扰及随机噪声，导致模型行为不可预测。现有研究多聚焦于输出层面的准确率或幻觉率，无法区分模型是有效整合了证据、抑制了内部记忆，还是触发了拒绝机制。本文通过受控实验分析不同相关性文档对LLM隐藏状态的层间动态影响，揭示了相关文档主要起确认作用而随机文档触发拒绝的表征模式。该工作为理解RAG失效提供了机制解释，但其仅停留在诊断层面，未提出具体的干预算法。

】

---

【HqeKV: Towards Hybrid Quantization and Eviction for KV Cache in Long-Context LLM Inference ｜HqeKV：混合量化与驱逐的协同优化框架

研究机构：美国东北大学

作者：He Wang、Yu Gu、Fangfang Li 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_22fd1e0098b0)

> 长上下文大语言模型推理中，键值缓存（KV Cache）的线性增长导致显存溢出，现有单一量化或驱逐策略因压缩粒度粗糙及重要性评估偏差，难以在固定内存预算下最大化生成质量。HqeKV 提出一种混合压缩框架，通过联合 K-V 重要性指标与分比特宽度量化策略，将缓存对分配至 FP16、4-bit、2-bit、1-bit 及驱逐五种状态。该方法在相同内存约束下将 LongBench 平均准确率从 40.53 提升至 49.98，但其离线搜索依赖校准集，在线自适应能力存疑。

】

---

【HSS-Synth: Humanities and Social Sciences Data Synthesis for LLMs ｜人文社科数据合成流水线

研究机构：浙江大学、北京大学

作者：Ru Peng、Tianyu Zhao、Xijun Gu 等 12 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b5997bd83437)

> 大语言模型在人文社科（HSS）领域的表现受限于高质量、多样化指令数据的稀缺，且该领域任务缺乏可验证答案，导致现有合成方法难以直接迁移。本文提出 HSS-Synth，通过“种子文档构建-多属性指令回译-教师强制回答”三阶段流水线，系统性解决 HSS 数据合成的质量与多样性瓶颈。该方法在 16 个基准上超越 14 个基线，验证了领域特定合成策略的有效性，但其对递归训练稳定性的影响尚未被评估。

】

---

【I Don’t Need Solution. I Need Emotional Support : Empathetic LLMs based on Emotional Validation ｜情感验证对齐的共情大语言模型

研究机构：韩国高丽大学

作者：Suhyune Son、Jungwoo Lim、Myunghoon Kang 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1f2df579865a)

> 导读 共情响应生成（Empathetic Response Generation, ERG）旨在让模型理解用户情感并生成具有共鸣与适当性的回复，其核心驱动力在于提升人机交互中的信任感与心理健康支持效果。现有大语言模型（LLMs）在生成流畅文本时往往陷入“过度迎合”与“模式化建议”的陷阱，缺乏对情感支持时序动态性的把握，导致回复虽流畅但缺乏心理深度。本文提出EVA框架，通过引入基于辩证行为疗法（Dialectical Behavior Therapy, DBT）的情感验证理论，构建层级化偏好数据集并采用直接偏好优化（Direct Preference Optimization, DPO）进行对齐，强制模型随对话进度动态调整共情层级。该方法在情感验证遵循度上表现优异，但其评估指标对分类器准确性的依赖及DPO在长对话时序建模上的局限性仍存疑。

】

---

【ID10M-JAM: Stress-Testing Idiom Identification Under Challenging Context ｜对抗语境下的习语识别鲁棒性测试

作者：Kai Golan Hashiloni、Lior Livyatan、Ofri Hefetz 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f32e43a0fca1)

> 习语识别旨在从连续文本中定位非组合性语义表达，但大语言模型（LLM）在标准基准上的高分掩盖了其面对误导性语境时的脆弱性。现有评估多依赖静态、语义清晰的样本，无法区分模型是依赖深层语义推理还是表面统计记忆。本文通过构建ID10M-JAM基准，注入人类无歧义但模型易混淆的对抗性上下文，量化模型在字面与习语意义消歧中的性能漂移。该工作揭示了当前LLM在习语理解上的系统性鲁棒性瓶颈，但其评估指标的设计存在基线依赖缺陷，且缺乏对内部机制的解释。

】

---

【Imperfectly Cooperative Human-AI Interactions: Comparing the Impacts of Human and AI Attributes in Simulated and User Studies ｜非完全合作人机交互中人类与AI属性的因果解耦

研究机构：美国亚利桑那州立大学、美国卡内基梅隆大学

作者：Myke C. Cohen、Mingqian Zheng、Neel Bhandari 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.15607)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.15607)

> 现有研究多假设人机目标完全一致，导致在招聘谈判或信息隐瞒等部分对齐场景中，无法区分用户个性与AI设计特征对交互结果的独立贡献。传统单一数据源（纯模拟或纯用户研究）因生态效度或控制力不足，难以捕捉这种联合因果效应。本文通过构建LLM模拟与真实用户研究的双轨平行实验，利用结构方程模型量化了双方属性在非合作博弈中的差异化影响。该范式揭示了模拟数据在预测人类对AI透明度敏感度上的系统性偏差，为可信代理AI设计提供了实证边界，但其结论受限于短期交互与单一文化样本。

】

---

【Improved Policy Optimization for Mixture-of-Experts Models: Importance Sampling and Rewarding from an Expert-Centric Perspective ｜专家相对策略优化

研究机构：东南大学、华为

作者：Yining Qian、Jinpeng Li、Fei Mi 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_536380857cc6)

> 混合专家模型在强化学习后训练中因新旧策略专家分配分歧导致重要性采样比率剧烈波动，引发训练崩溃。现有序列级采样方法虽稳定但丢失了Token功能差异，而路由重放方法虽对齐但抑制了探索。本文提出专家级重要性采样与熵奖励机制，在保持采样稳定性的同时保留功能粒度并显式优化路由策略。该方法在数学推理基准上显著优于基线，但其对路由一致性的依赖及熵奖励的泛化性仍存疑。

】

---

【Information Representation Fairness in Long-Document Embeddings: The Peculiar Interaction of Positional and Language Bias ｜长文档嵌入中的信息表示公平性

研究机构：瑞士苏黎世大学

作者：Elias Schuhmacher、Andrianos Michail、Juri Opitz 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.16934)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.16934)

> 长文档嵌入模型在检索任务中面临的核心矛盾是：单向量表示需同时承载多段独立信息的语义，但现有编码器倾向于过度表征文档前部内容，导致后部信息在语义空间中“不可见”。主流的双向注意力机制虽解决了全局语义捕获问题，却未消除位置与语言维度的系统性偏差，使得公平性成为被忽视的评估盲区。本文通过置换实验量化首段偏差，并提出一种无需训练的推理时注意力校准方法，将注意力质量均匀分配至不同位置区间。该方法在降低位置偏差方面有效，但仅验证了编码器模型，且未评估校准对通用检索精度的影响，其泛化边界尚存疑。

】

---

【Infusing Theory of Mind into Socially Intelligent LLM Agents ｜目标导向社交推理中的心智理论集成

研究机构：加拿大不列颠哥伦比亚大学、加拿大向量研究所

作者：EunJeong Hwang、Yuwei Yin、Giuseppe Carenini 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_6a7fd957c401)

> 导读 社交智能的核心在于理解对话伙伴的心理状态并据此调整策略，但现有大语言模型（LLM）往往将心智理论（Theory of Mind, ToM）推理与话语生成割裂，导致模型虽能回答关于他人信念的问题，却无法在动态交互中利用这些推断达成社交目标。本文指出，仅优化话语以达成目标会引发奖励黑客问题，而忽略显式心理状态建模则使模型缺乏策略性。为此，作者提出 ToMAgent (TOMA)，一种结合 ToM 预测与对话结果前瞻模拟的训练框架，通过筛选高效用的“心理状态-话语”对进行微调。该方法在 Sotopia 基准上显著提升了小模型的社交表现，验证了显式 ToM 建模对社交智能的关键作用，但其依赖 LLM 作为评估器的机制是否引入系统性偏差仍存疑。

】

---

【J-Shuwa: A Large-Scale Web-Collected Japanese Sign Language-Japanese Parallel Corpus ｜J-Shuwa：基于硬字幕挖掘的日本手语大规模平行语料库构建

研究机构：日本东京大学、日本理化学研究所

作者：Junwen Mo、MinhDuc Vo、Noriki Nishida 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_988542e485aa)

> 日本手语（Japanese Sign Language, JSL）研究长期受限于高质量平行语料库的缺失，现有资源规模远不足以支撑鲁棒模型训练。主流Web采集路线依赖闭合字幕（Closed Captions, CCs），但忽略了大量含硬编码字幕（Hard-coded Subtitles, HardSubs）的视频，导致数据源被人为截断。本文通过构建端到端字幕-手语共现检测模型与大型视觉语言模型（Large Vision Language Model, LVLM）OCR流水线，从YouTube挖掘出19.7万句JSL-日语平行数据，填补了JSL数据资源空白。其价值在于将JSL可用数据从62小时扩至300小时，但硬字幕提取的噪声控制与跨签名者泛化能力仍存疑。

】

---

【Law in Silico: Simulating Legal Society with LLM-Based Agents ｜法律社会模拟：Law in Silico

研究机构：北京大学

作者：Yiding Wang、Yuxuan Chen、Fanxu Meng 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.24442)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.24442)

> 法律系统作为复杂社会子系统，其动态演化难以通过传统分析法学直接观测，亟需一种能同时捕捉宏观统计规律与微观制度交互的仿真范式。现有通用社会模拟框架缺乏对立法、司法、执法闭环机制的建模，而专用法律智能体研究又局限于单一司法环节，无法反映法律环境对个体行为的系统性影响。Law in Silico 通过分层采样构建基于真实统计分布的智能体画像，并引入 LLM 驱动的 Game Master 模块处理多轮法律交互，实现了从宏观犯罪率复现到微观制度演化的双层验证。该框架在宏观统计保真度上表现稳健，但微观机制的因果解释力与跨模型鲁棒性仍存疑。

】

---

【LearnAct: Few-Shot Mobile GUI Agent with a Unified Demonstration Benchmark ｜移动端GUI智能体的少样本演示学习框架

研究机构：浙江大学、香港中文大学

作者：Guangyi Liu、Pengxiang Zhao、Liang Liu 等 14 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9b5b11b14d92)

> 移动端GUI智能体在长尾场景下泛化能力不足，传统预训练或微调难以覆盖所有应用与用户任务组合，导致未见场景执行失败。现有基于结构化元数据（如UI Tree）的方法在移动端因数据缺失而失效，纯视觉端到端模型则缺乏从少量人类演示中提取可复用知识的机制。本文提出LearnAct框架，通过纯视觉输入解析演示、检索相似知识并指导执行，构建首个移动端少样本演示学习基准LearnGUI。该框架验证了非训练式知识迁移的有效性，但其绝对性能仍远低于全量强化学习模型，且依赖高质量演示的可用性。

】

---

【Learning on Imbalanced Noisy Data via Debiased Sample Selection and LLM-Driven Annotation ｜去偏样本选择与LLM协同标注的噪声长尾学习

研究机构：国防科技大学、浙江大学

作者：Bo Yuan、Yulin Chen、Yin Zhang

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_64fce0d6bf8b)

> 噪声标签与类别不平衡在真实文本数据中常同时出现，传统基于全局固定损失阈值的样本选择方法会系统性忽略尾部类干净样本，导致选择偏差。本文指出该偏差源于头部与尾部类损失分布的动态演化差异，提出DeCo框架，通过多专家模型解耦训练与选择、动态类内阈值筛选样本，并引入LLM对噪声子集进行主动重标注。该方法在文本分类任务上显著优于现有基线，但其对LLM标注质量的依赖及跨模态泛化能力尚存疑。

】

---

【Leveraging External Knowledge for Historical Document Restoration via Retrieval-Augmented Large Language Models ｜基于检索增强大语言模型的历史文档受损字符复原

作者：Gabeen Kim、Kyeongpil Kang

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c9f32802b601)

> 导读 历史档案因物理侵蚀导致大量字符不可读，传统掩码语言建模方法仅依赖单篇文档内部上下文，难以恢复需外部历史知识支撑的命名实体。本文切入点在于将大语言模型的隐式知识与显式检索增强生成结合，构建专门针对古代语料的复原框架。具体做法是微调Qwen3模型，利用BM25检索相关文档并引入时间元数据，以因果语言建模方式生成复原字符。该框架在命名实体恢复上显著优于通用大模型，但其评估仅依赖Top-1准确率，未涵盖结构完整性与语义一致性维度。

】

---

【LightMoE: Task-Aware Expert Availability Management for Memory-Efficient MoE-LLM Inference ｜任务感知的专家可用性管理

作者：Puhan Luo、Yunhao Yao、Junyang Wang 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4da6f9f64034)

> 边缘设备部署混合专家模型时，巨大的专家池内存占用与严格的硬件限制构成核心矛盾。静态剪枝损失精度，动态换入换出引入高延迟，现有方案难以兼顾。LightMoE 利用边缘请求的时空局部性，通过频率初始化、相似度重定向与任务级异步替换，解耦逻辑选择与物理驻留。该方法在精度-延迟权衡上优于剪枝与交换基线，但其对任务语义漂移的响应粒度及跨层依赖建模仍存疑。

】

---

【Like a Therapist, But Not: Reddit Narratives of AI in Mental Health Contexts ｜基于技术接受模型与治疗联盟的AI心理健康话语分析

作者：Elham Aghakhani、Rezvaneh Rezapour

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_cb4037c0104f)

> 现有LLM心理健康研究聚焦于模型临床能力与安全审计，却忽视了用户在实际使用中的感知、信任与关系建立机制。本文切入点在于将心理学中的技术接受模型（TAM）与治疗联盟理论引入大规模自然主义话语分析，量化用户如何评估AI作为治疗工具的价值与风险。通过构建混合人工-LLM标注流程，对5,126条Reddit帖子进行细粒度编码，揭示了任务对齐而非单纯情感纽带是驱动积极采纳的核心因素。该工作填补了用户侧评估空白，但其结论局限于话语层面，无法直接验证临床有效性。

】

---

【LLMs Meet Isolation Kernel: Lightweight, Learning-free Binary Embeddings for Fast Retrieval ｜隔离核嵌入

研究机构：南京大学

作者：Zhibo Zhang、Yang Xu、Kai Ming Ting 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_14defabed7f3)

> 高维大语言模型（LLM）嵌入在大规模检索中面临存储与延迟瓶颈，现有压缩方法如马特罗什卡表示学习（MRL）和对比稀疏表示（CSR）虽能降低维度，但需高昂训练成本且存在精度损失。本文提出隔离核嵌入（IKE），一种无需训练的随机分区映射方法，将LLM向量转化为二进制索引以加速检索。IKE通过引入分区多样性准则，在保持检索精度的同时实现了显著的存储与速度优势，但其对复杂语义空间的适应性仍存疑。

】

---

【Lost in Stories: Consistency Bugs in Long Story Generation by LLMs ｜长程叙事一致性基准与自动化检测

作者：Junjie Li、Xinrui Guo、Yuhao Wu 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.05890)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.05890)

> 长程叙事生成面临的核心挑战是模型在数千词跨度内维持事实、逻辑与风格的一致性，而非仅保证局部流畅。现有评估多聚焦情节连贯性，缺乏对跨上下文矛盾的系统化隔离与可复现检测机制。本文构建了包含2000个提示的ConStory-Bench基准，并开发了基于显式证据链的ConStory-Checker自动化评估流水线，将一致性错误量化为可审计的细粒度指标。该工作填补了长程叙事一致性评估的空白，但其依赖单一LLM评判者且仅限英文虚构文本，评估的普适性与评判者偏差仍是关键存疑点。

】

---

【ltzGLUE: Luxembourgish General Language Understanding Evaluation ｜卢森堡语通用语言理解评估基准

研究机构：德国慕尼黑大学、英国兰卡斯特大学

作者：Alistair Plum、Felicia Körner、Anne-Marie Lutgen 等 11 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_730cea2376c7)

> 卢森堡语（LTZ）作为拥有约40万使用者的官方语言，长期缺乏统一的语言理解（NLU）评估框架，导致模型性能无法可靠量化。现有零散数据集规模小、领域单一，且缺乏跨任务对比标准，使得多语言模型在该语言上的真实能力被高估或低估。本文通过整合现有资源并构建新任务，建立了首个包含8项任务的LTZGLUE基准，并系统评估了编码器与大型语言模型（LLM）的表现。该工作填补了LTZ评估空白，但LLM在结构化任务上的显著劣势揭示了零样本范式的局限，其长期有效性仍存疑。

】

---

【LycheeCluster: Efficient Long-Context Inference with Structure-Aware Chunking and Hierarchical KV Indexing ｜结构感知分块与层级索引的长上下文推理加速

研究机构：哈尔滨工业大学、电子科技大学

作者：Dongfang Li、Zixuan Liu、Gang Lin 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.08453)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.08453)

> 长上下文解码受限于键值缓存（KV Cache）的内存带宽瓶颈，现有检索式方法因固定分页或Token聚类破坏语义完整性，导致检索预算浪费。LycheeCluster通过结构感知分块保留局部连贯性，并构建基于三角不等式的层级索引实现对数时间剪枝。该方法在保持精度接近全注意力的同时，将解码延迟降低至原速度的1/3.6。其核心假设——语义连贯块优于固定页或孤立Token——在结构化数据任务上得到验证，但在通用文本中的普适性及与驱逐式方法的内存效率对比尚存疑。

】

---

【MA2P: A Meta-Cognitive Autonomous Intelligent Agents Framework for Complex Persuasion ｜元认知自主智能体框架

研究机构：东南大学

作者：Dingyi Zhang、Ziqing Zhuang、Linhai Zhang 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_731518519446)

> 复杂说服对话要求说服者不仅识别被说服者的潜在心理状态，还需将其转化为可执行的多轮策略行动，现有大语言模型往往止步于泛化建议或出现跨域性能剧烈波动。MA2P 通过引入元认知配置器与结构化知识库，将说服过程重构为“规划-行动-反思”的闭环，实现了从状态识别到策略落地的跨越。该框架以无训练、即插即用的方式显著提升了说服成功率并降低了跨域方差，但其元策略选择仅依赖历史成功计数，缺乏对策略语义相似性的考量，在冷启动场景下的鲁棒性仍存疑。

】

---

【MAPLE: A Meta-learning Framework for Cross-Prompt Essay Scoring ｜跨提示作文评分的元学习框架

作者：Salam Albatarni、May Bashendy、Sohaila Eltanbouly 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_93aa3ef618b9)

> 跨提示自动作文评分（Cross-Prompt Automated Essay Scoring, CP-AES）旨在解决模型在未见写作提示下的泛化难题，传统端到端模型因提示分布偏移导致性能显著衰减。现有优化型元学习方法将提示视为同质任务，限制了任务多样性，而本文切入点在于利用原型网络的非参数特性，通过重构二元/多类任务并融合上下文门控机制，实现更鲁棒的跨域适应。MAPLE 在 ELLIPSE 和 LAILA 数据集上分别以 8.5 和 3 个 QWK 点的优势超越强基线，证明了元学习在低资源跨域场景的有效性，但其对分数范围不一致数据的处理局限仍存疑。

】

---

【MASS: Deep Research for Social Sciences with Memory-Augmented Social Simulation ｜记忆增强社会模拟

研究机构：天津大学

作者：Yongrui Liu、Deyi Xiong

论文原文见 [arXiv](https://arxiv.org/abs/2606.09198)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.09198)

> 自动化社会科学研究长期受限于“检索-生成”范式，导致产出缺乏实证深度与原创性。现有Deep Research智能体仅能重组既有文献，无法产生“一手”经验数据，而纯社会模拟框架又缺乏科研导向。MASS将社会模拟嵌入研究流水线，通过ODD协议标准化实验设计与Ebbinghaus遗忘机制维持智能体认知连贯，从而生成支撑论文写作的原始行为数据。该方法在Insight维度显著优于基线，但其模拟数据的科学有效性尚未接受独立审计。

】

---

【MATCHA: Matching Text via Contrastive Semantic Alignment ｜对比语义对齐指标

研究机构：德国图宾根大学

作者：Siran Li、Ece Sena Etoglu、Carsten Eickhoff 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_cc512962911f)

> 自然语言生成评估的核心困境在于，现有主流指标无法有效区分语义一致与语义矛盾的文本。BERTScore等基于预训练嵌入的指标因嵌入空间的聚类效应，常对事实错误文本赋予高分，导致评估结果与人类判断脱节。本文提出MATCHA，通过引入对抗性反事实样本进行对比学习训练，显式惩罚与参考文本矛盾的输出。该方法在多个基准上显著提升了正确与错误文本的区分度，但其依赖参考文本的设定限制了在开放生成任务中的直接适用性。

】

---

【Mechanistic Insights into Deferred Semantic Drift in LLMs ｜延迟语义漂移机制

研究机构：大连理工大学

作者：Jingjie Zeng、Huayang Li、Liang Yang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1fae9d195424)

> 因果Transformer在处理歧义词时，其初始表征因单向信息流限制而无法即时更新，导致语义消解存在延迟。现有机制可解释性研究多聚焦静态特征定位，缺乏对动态语义更新过程的追踪。本文提出“延迟语义漂移”机制，通过非因果Oracle诊断与注意力值向量分析，揭示后续token如何主动检索并整合歧义信息。该工作提供了因果验证的新视角，但受限于单一模型架构与自建数据集，其泛化性存疑。

】

---

【Memory-Driven Role-Playing: Evaluation and Enhancement of Persona Knowledge Utilization in LLMs ｜记忆驱动角色扮演：基于结构化Schema与显式检索协议的评估与增强

研究机构：哈尔滨工业大学、澳大利亚麦考瑞大学

作者：Kai Wang、Haoyang You、Yang Zhang 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.19313)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.19313)

> 长程对话中角色身份漂移的核心瓶颈在于模型无法自主从扁平化角色档案中检索并应用特定情境下的知识。现有方法依赖额外场景提示或整体评分，掩盖了记忆检索失效的具体环节。本文提出记忆驱动角色扮演（Memory-Driven Role-Playing, MDRP）范式，将角色知识视为长期记忆（LTM），对话上下文视为短期记忆（STM），通过结构化叙事Schema与Magic-If协议实现无参数检索。该框架在单轮基准上验证了提示工程的有效性，但其对多轮动态状态演化的适用性存疑。

】

---

【MENTOR: Mitigating Identity Drift in Dynamic Role-Playing via Dual-Chain Structured Memory ｜双链结构化记忆缓解动态角色扮演身份漂移

研究机构：中国科学院、中国科学院大学

作者：Zhu Zhuoning、Xingyu Gao、Hailong Shi

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9465be4e47c6)

> 长程多用户交互中，大语言模型（LLM）常因上下文污染导致角色边界模糊，即身份漂移。现有检索增强生成（RAG）依赖语义相似度，无法区分角色归属，导致跨角色信息泄露。MENTOR 提出无参数双链记忆架构，通过物理隔离角色工作记忆与全局事件日志，并结合知识图谱验证信息可接受性，在高频切换场景下将平均得分从 0.46 提升至 0.75。该架构有效抑制了“伪对齐”现象，但其对静态单角色场景的适用性及门控阈值敏感性尚未充分验证。

】

---

【MHSafeEval: Role-Aware Interaction-Level Evaluation of Mental Health Safety in Large Language Models ｜角色感知交互级心理健康安全评估

研究机构：韩国汉阳大学、新加坡管理大学

作者：Suhyun Lee、Palakorn Achananuparp、Neemesh Yadav 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17730)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17730)

> 大语言模型在心理咨询中的安全性评估长期受限于静态、粗粒度的基准，无法捕捉多轮对话中累积的关系性危害。现有方法将安全失效简化为单轮内容毒性检测，忽略了咨询师在对话中扮演的交互角色如何塑造伤害轨迹。本文提出 R-MHSafe 分类法与 MHSafeEval 框架，通过质量多样性搜索动态生成对抗性多轮交互，揭示角色特异性的隐性安全漏洞。该框架在八个主流模型上实现了 0.914 至 0.997 的攻击成功率，证明了动态评估在诊断粒度上的优势，但其依赖 LLM 裁判的可靠性及动态生成的可复现性仍存疑。

】

---

【Mirage: A Diagnostic Framework for Evaluating the Realism of Synthetic Contact Center Dialogue Generation ｜合成呼叫中心对话真实性诊断框架

作者：Rishikesh Devanathan、Varun Nathan、Ayush Kumar

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e2a5d2c42aeb)

> 呼叫中心合成对话生成旨在解决隐私约束下的数据稀缺问题，但现有方法生成的文本虽具表面流畅性，却缺乏真实交互中的情感动态与微观行为特征。本文切入点在于指出“可信度不等于真实性”，通过构建包含17项指标的诊断框架，量化合成数据在情感弧线、语言复杂度、交互风格及会话属性上的分布失真。该框架结合属性引导的生成流水线，验证了当前合成策略在下游任务中的效用缺口。其价值在于提供了细粒度的评估工具，但受限于私有数据与单一LLM架构，结论的普适性存疑。

】

---

【MM-ShiftKV: Decode-Aware Prefill-Stage KV Selection for Multimodal Large Language Models ｜解码感知预填充键值选择

研究机构：浙江大学

作者：Jinsong Shu、Chenyang Wu、Zhongle Xie 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2607.22586)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2607.22586)

> 多模态大语言模型（MLLM）推理中，预填充阶段构建的键值缓存（KV Cache）因视觉Token数量庞大而成为显存瓶颈。现有预填充阶段KV选择方法隐含假设预填充统计量可代表解码阶段查询分布，但在多模态场景下该假设失效，导致紧预算下关键视觉Token被误删。MM-ShiftKV通过构建方差扩展的解码感知查询代理，在预填充阶段一次性校准重要性估计。该方法在严格预算下显著优于现有基线，但其固定超参对模态比例的敏感性尚未验证。

】

---

【MobileBench-OL: A Comprehensive Chinese Benchmark for Evaluating Mobile GUI Agents in Real-World Environment ｜移动图形用户界面智能体真实环境基准

研究机构：小米、北京大学

作者：Qinzhuo Wu、Zhizhuo Yang、Hanhao Li 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.20335)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.20335)

> 移动图形用户界面智能体（Mobile GUI Agent）需在动态、含噪的真实设备上执行多步操作，但现有在线基准多依赖模拟器且忽略环境噪声，导致评测与部署存在断层。本文提出MobileBench-OL，通过80个中文应用中的1080个任务及5个子集，覆盖基础能力、长程推理、GUI探索与噪声鲁棒性。其核心机制是结合基于XPath规则的自动评估框架与细粒度重置机制，确保评测的可重复性。该基准揭示了当前智能体在真实噪声下的显著性能衰减，但其缺乏跨应用任务且仅限中文生态，限制了结论的普适性。

】

---

【Model in Distress: Sentiment Analysis on French Synthetic Social Media ｜基于回译与合成推理的隐私敏感合成数据流水线

作者：Pierre-Carl Langlais、Pavel Chizhov、Yannick Detrois 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_372c49b13e11)

> 隐私敏感场景下的情感分析面临标注数据稀缺、评估集匮乏及数据合规三重约束，传统直接翻译或通用合成方法难以兼顾领域语用特征与隐私保护。本文切入点在于构建“专家蒸馏”范式，利用少量真实种子数据微调辅助模型，通过回译与合成推理生成大规模高保真合成数据，而非直接依赖通用大模型生成。具体做法是训练专用生成器与推理器，产出170万条带推理轨迹的法语公交推文，用于训练600M参数的小模型。该方案在隐私合规前提下实现了小模型超越大模型的性能，但依赖专有模型生成种子数据，其可复现性与通用性边界尚存疑。

】

---

【Modeling Human Perspectives with Socio-Demographic Representations ｜社会人口统计对比学习

研究机构：德国图宾根大学

作者：Leixin Zhang、Cagri Coltekin

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_65df7c2d8c5b)

> 标注者分歧建模旨在将人类标注中的不一致从需消除的噪声重构为反映价值观多样性的信号，其核心在于构建能预测判断分布而非单一标签的模型。现有社会感知方法多依赖单属性分组或独立输出头，在稀疏标注数据下难以捕捉复杂社会背景对视角的联合影响，导致模型在主观任务上存在公平性偏差。本文提出 Socio-Contrastive Learning，通过对比损失联合优化社会人口统计表征与标签预测，以解决多属性组合下的稀疏数据建模难题。该方法在仇恨言论与毒性检测任务上显著优于基线，验证了社会特征对视角预测的贡献，但其评估指标仍基于分类准确率而非分布对齐，且未涵盖最新 LLM 对齐框架。

】

---

【Modeling Multi-Dimensional Cognitive States in Large Language Models under Cognitive Crowding ｜多维认知状态建模中的几何瓶颈与双曲解耦

研究机构：哈尔滨工业大学、澳门大学

作者：Lin Zhong、Siyu Zhu、Zizhen Yuan 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17174)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b7ccc80b9eb1)

> 现有大语言模型在处理情感、思维、立场与意图等多维心理状态时，往往陷入单维任务的高准确率与联合预测的低准确率之间的割裂。这种割裂源于欧氏嵌入空间无法承载认知状态固有的层级结构，导致不同维度的语义表征发生重叠。本文提出 HyCoLLM 框架，利用庞加莱球模型的双曲几何特性解耦认知维度，并通过语义-认知拓扑损失对齐语言模型内部表征。该方法在自建基准上使 8B 参数模型超越 GPT-4o，但其对静态文本的依赖及维度独立假设限制了其在动态交互场景中的适用性。

】

---

【ModularMoE: Fast LLM Customization with Parameter-Sharing Mixture-of-Experts for Low-Resource Settings ｜模块化混合专家模型

作者：Jiaxing Liu、Qi Qi、Haifeng Sun 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c19f9aef8c68)

> 导读 低资源场景下的大语言模型部署面临算力与存储的双重瓶颈，传统“剪枝-微调”范式因计算开销大或任务间干扰而难以落地。现有方法要么牺牲通用能力换取特定任务性能，要么因灾难性遗忘导致知识退化。本文切入点在于利用预训练模型中神经元共激活形成的涌现模块化特性，将前馈层拆分为可共享的模块，通过组合模块构建任务特定专家，实现参数高效的多任务定制。该方法在同等稀疏度下显著优于传统剪枝基线，但其静态路由机制对动态输入复杂度的适应性存疑。

】

---

【MSCode: Advancing Human Motion-Language Understanding via Modality-Shared Codebook ｜模态共享码本驱动的人体运动-语言理解

作者：Haoyu Shi、Huaiwen Zhang

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_374c6ac3a1ac)

> 人体运动理解的核心瓶颈在于运动序列的细粒度时空动态与文本的抽象语义之间存在本质性的粒度不匹配，导致传统全局对比学习难以实现精准对齐。现有方法要么依赖高维词汇空间牺牲效率，要么在连续潜空间中丢失语义离散性。MSCode 提出模态共享码本，强制运动与文本激活同一组离散语义单元，统一了跨模态的语义粒度。该方法在检索与定位任务上显著优于基线，但其对长程依赖的建模能力与物理动力学信息的保留程度仍存疑。

】

---

【MSVBench: Towards Human-Level Evaluation of Multi-Shot Video Generation ｜多镜头视频生成评估基准

研究机构：哈尔滨工业大学

作者：Haoyuan Shi、Yunxin Li、Nanhao Deng 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.23969)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.23969)

> 多镜头视频生成正从单片段拼接向长叙事演进，但现有评估体系仍锚定单镜头范式，无法捕捉跨镜头的时序逻辑与主体一致性断裂。MSVBench 通过构建层级化脚本架构与混合评估器，将评估粒度从全局标量下沉至镜头级时空定位。该框架实现了与人类判断 94.4% 的斯皮尔曼相关系数，并验证了评估轨迹向监督信号转化的可行性。其核心局限在于对连续生成模型镜头边界缺失的适配困难，以及故事样本量对统计稳健性的潜在制约。

】

---

【MTEB-NL and E5-NL: Embedding Benchmark and Models for Dutch ｜荷兰语嵌入基准与模型构建

研究机构：比利时安特卫普大学

作者：Nikolay Banar、Ehsan Lotfi、Jens Van Nooten 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2f9a1cb6e7a3)

> 荷兰语在通用多语言嵌入资源中占比极低，导致现有模型在该语言上性能受限且缺乏可靠的评估标准。主流多语言模型依赖英语或中文数据训练，难以捕捉荷兰语特有的语义结构，而现有荷兰语基准数据量小且许可受限。本文通过构建包含40个数据集的MTEB-NL基准，结合LLM合成数据扩充训练集，并基于E5架构进行词表适配与微调，旨在填补这一资源空白。该工作提供了低资源语言嵌入开发的完整资源包，但其性能上限受限于E5骨干网络及合成数据的质量，未探索更先进的双向化架构。

】

---

【NeuRAG: End-to-End Neural Knowledge Augmentation via Hyper-Neurons ｜神经化检索增强生成

研究机构：南开大学

作者：Liwei Zheng、Xuemin Liu、Jie Liu

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_6d0b007ecdb9)

> 检索增强生成（RAG）范式下，外部知识与模型内部推理长期处于解耦状态，导致复杂推理任务中知识集成碎片化。现有动态RAG方法虽能迭代注入文本，但受限于上下文窗口瓶颈及阶段式优化目标错位，无法实现参数级深度整合。NeuRAG将文档编码为LoRA模块构成的“超神经元”，通过隐藏状态驱动的路由机制在解码过程中动态重配置模型参数空间，实现检索与生成的端到端可微分耦合。该框架在通用多跳问答基准上优于现有参数化RAG基线，但其对知识冲突场景下的忠实度表现及参数融合后的可解释性尚未得到验证。

】

---

【No-Worse Context-Aware Decoding: Preventing Neutral Regression in Context-Conditioned Generation ｜无劣化上下文感知解码

作者：Yufei Tao、Ameeta Agrawal

论文原文见 [arXiv](https://arxiv.org/abs/2604.16686)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.16686)

> 检索增强生成（RAG）中，模型常因非信息性上下文干扰而覆盖原本正确的答案，这一现象被称为中性回归。现有对比解码方法虽能提升冲突场景下的准确率，但缺乏“不伤害”保证，导致在上下文无用时仍改变输出。本文提出无劣化上下文感知解码（No-Worse Context-Aware Decoding, NWCAD），通过两阶段门控机制实现显式回退与动态路由。该方法在保持上下文利用能力的同时，从机制上杜绝了中性回归，但其在黑盒API模型中的适用性受限于logits访问权限。

】

---

【Not All Citations Are Equal:Entropy-Guided Citation Selection for Noise-Resistant Medical LLM ｜熵引导引用选择

作者：Minyu Gao、Hanlin Xiao、Ruoyu Wang 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_183d809c4e9b)

> 医疗检索增强生成（RAG）中，模型在内部知识与外部检索冲突时往往盲目采信外部证据，导致检索噪声污染推理。现有解码干预方法仅调整输出分布，无法从根源修正模型对噪声引用的依赖偏好。本文切入点在于发现有效引用具有显著更低的Token级熵，将其作为奖励信号引入强化学习。通过无训练反思框架蒸馏数据，结合基于引用熵的GRPO训练，使模型内化选择性引用能力。该方法在医疗基准上稳定提升了噪声鲁棒性，但其熵信号在通用领域的泛化性及细粒度定位能力仍存疑。

】

---

【OjaKV: Context-Aware Online Low-Rank KV Cache Compression ｜在线低秩键值缓存压缩

研究机构：美国伦斯勒理工学院、IBM研究院

作者：Yuxuan Zhu、David H. Yang、Mohammad Mohammadi Amiri 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.21623)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.21623)

> 长上下文推理中，键值缓存（KV Cache）随序列长度线性增长，导致显存溢出。现有低秩近似方法依赖静态离线学习的投影基，在推理时面对分布漂移会失效。OjaKV通过混合存储策略保留高误差Token的全秩表示，并利用Oja规则在线更新投影基，解决了静态基的适应性不足问题。该方法在生成任务上显著优于静态基线，但其绝对精度仍远低于量化与驱逐路线，且未与这些主流方法直接对比。

】

---

【On the Representation Geometry of LoRA Model Merging ｜LoRA 模型合并中的 SVD-CUR 几何互补性分析

研究机构：加拿大多伦多大学、美国西北大学

作者：Chenyang Lu、Jiaru Li、Jinman Zhao 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a22ac2d9d557)

> 导读 多任务 LoRA 合并面临的核心困境在于，现有方法普遍假设单一全局子空间足以对齐所有任务更新，但低秩约束导致不同任务的更新方向在参数空间中系统性错位。本文切入点在于揭示奇异值分解（SVD）与列选择分解（CUR）在捕获共享结构与任务特异结构上的几何互补性，而非直接提出新算子。通过构建双分支并行对齐框架并基于残差能量加权融合，该方法在视觉与语言基准上实现了无训练合并性能的稳定提升。其价值在于从表示几何层面解构了合并失效的根源，但实验未覆盖异构秩或跨架构场景，其理论边界仍受限于同源初始化假设。

】

---

【OpenPhone: Mobile Agentic Foundation Models ｜端云协同移动GUI智能体

作者：Yangqin Jiang、Chao Huang

论文原文见 [arXiv](https://arxiv.org/abs/2510.22009)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.22009)

> 移动端GUI智能体面临算力与成本的结构性矛盾：4B以下模型能力不足，7B以上模型无法端侧部署或云端调用成本过高。现有方案要么牺牲性能追求轻量化，要么依赖昂贵的大模型，缺乏在两者间动态切换的机制。OpenPhone通过3B端侧模型与云端大模型的实时协同编排，在保持接近云端性能的同时大幅降低调用成本。该框架验证了小模型经强化学习优化后的可行性，但其动态切换策略的泛化边界与通信延迟影响尚不明确。

】

---

【Optimizing Native Sparse Attention with Latent Attention and Local Global Alternating Strategies ｜交替稀疏注意力

研究机构：中国人民大学、美团

作者：Yuxuan Hu、Jianchao Tan、Jiaqi Zhang 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_cd0eec310990)

> 长上下文处理中，标准Transformer的二次方计算复杂度与键值缓存（KV Cache）线性内存膨胀构成双重瓶颈，而现有稀疏注意力方案在层内并行计算时，局部窗口分支常因“捷径学习”干扰全局检索分支的有效性。本文切入点在于揭示滑动窗口注意力（SWA）与选择性注意力（SA）共存时的功能冲突，并提出层间交替策略。ASA将SWA与压缩/选择性注意力（CA/SA）在Transformer层间以1:1比例交替排列，并引入多头潜在注意力（MLA）及其变体分组头潜在注意力（GLA）替代分组查询注意力（GQA），在保持检索精度的同时降低50%的KV缓存开销。该架构在340M至1.3B参数规模上验证了有效性，但缺乏大规模模型及标准长上下文基准的横向对比，其层间静态交替策略在复杂动态任务上的泛化能力存疑。

】

---

【P-QuASAR: A Unified Probabilistic Framework for Holistic Patent Quality Assessment and Refinement ｜专利质量结构化评估与修复

研究机构：美国埃默里大学、西安电子科技大学

作者：Xinyuan Song、Ziyi Ni、Fred Yang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_862dfcb95c20)

> 专利说明书的质量评估长期面临多维缺陷相互独立检测导致的证据隔离与修复建议脱节问题。现有模块化流水线无法共享跨维度线索，且通用检测器缺乏针对法律与技术细节的校准能力。P-QuASAR 通过构建质量图（Quality Graph）进行联合概率推理，将缺陷检测转化为图上的后验分布估计，并基于此推导最优干预路径。该框架在自建数据集上显著提升了检测精度与修复效果，但其结论受限于单一司法管辖区的小规模样本，跨域泛化能力存疑。

】

---

【PED: Route-Decoupled Diagnostics for Persona Consistency in Spoken Agents ｜语音角色扮演智能体路由解耦诊断框架

研究机构：华为、天津大学

作者：Weihao Liu、Junrui Wei、Zhao Zhang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_dcea27350d73)

> 语音角色扮演智能体在长程交互中常出现角色失真，但现有评估仅报告聚合分数，无法定位故障源于文本生成还是声学实现。PED 框架将角色表达解耦为文本与音频两条独立路由，通过共享情感空间投影实现轮次级、路由级的故障归因。该框架在端到端与级联两种架构下验证了路由分离性受限于参考锚点重叠，且文本-音频一致性呈弱耦合。其诊断价值在于将黑盒评分转化为可操作的调试信号，但受限于单一对话脚本与固定投影器，结论的普适性尚待检验。

】

---

【PERM: Psychology-grounded Empathetic Reward Modeling for Large Language Models ｜心理学导向的共情奖励建模

研究机构：中国科学技术大学、新加坡国立大学

作者：Chengbing Wang、Wuqiang Zheng、Yang Zhang 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e8ca496d4883)

> 大语言模型在心理支持场景中常因缺乏深层认知而生成模板化或过度迎合的回复，现有强化学习方法多依赖单一视角的奖励信号，无法捕捉共情交互的双向闭环特性。本文基于共情循环理论，提出从支持者、求助者及旁观者三个视角分解奖励信号，以解决单视角优化导致的共情浅层化问题。通过多视角奖励聚合与组相对策略优化，PERM 在情感智能基准上实现了超过10%的性能提升。该框架验证了心理学理论对奖励建模的指导价值，但其单轮对话设定与纯文本模态限制了在复杂动态交互中的泛化能力。

】

---

【PersonaArena: Dynamic Simulation for Evaluating and Enhancing Persona-Level Role-Playing in Large Language Models ｜动态社交模拟评估与增强框架

研究机构：深圳大学、微软研究院

作者：Wenlong Shi、Jianxun Lian、Mingqi Wu 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.17044)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.17044)

> 角色扮演大语言模型（LLM）在长程交互中面临身份漂移与认知浅层化问题，现有基准多聚焦于虚构角色的静态问答，难以衡量日常社交互动的真实性与适应性。PersonaArena 通过构建基于真实用户生成内容的人格库，利用多智能体沙盒环境激发动态多轮交互，并引入多智能体辩论裁判机制进行多维评估。该框架不仅提供了评估工具，还通过自生成轨迹进行监督微调（SFT）与直接偏好优化（DPO），验证了数据增强对模型人格一致性的提升作用。其价值在于填补了“人格级”评估空白，但缺乏与虚构角色基准的交叉验证，且高计算成本限制了大规模筛选的实用性。

】

---

【PersonaForge: Psychology-Grounded Dual-Process Architecture for Personality-Consistent Role-Playing Agents ｜基于心理学双过程架构的角色扮演智能体

研究机构：武汉大学

作者：Jizhou Tong、Sirui Zou

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_14ea4afcb1b5)

> 角色扮演智能体在长程交互中面临身份漂移与认知浅层化的双重困境，现有微调或检索方法难以兼顾风格稳定性与心理逻辑自洽。本文切入点在于将心理学理论中的大五人格与防御机制转化为可计算的结构化约束，而非依赖自然语言描述。通过构建三层人格架构与选择性双过程生成机制，PersonaForge 在无需微调的情况下实现了长程一致性。该方法在RoleBench上取得73.2%的胜率，但其在极端长程场景下的稳定性及跨文化框架的普适性仍存疑。

】

---

【PL-MTEB: Polish Massive Text Embedding Benchmark ｜波兰语文本嵌入基准

作者：Rafał Poświata、Sławomir Dadas、Michał Wiktor Perełkiewicz

论文原文见 [arXiv](https://arxiv.org/abs/2405.10138)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_34a951901fd6)

> 文本嵌入模型在低资源语言上的性能评估长期缺乏统一标准，导致模型选择依赖单一任务或存在数据泄露风险。现有通用基准如 MTEB 主要覆盖英语，无法有效区分多语言模型在特定语言上的真实泛化能力。本文构建了包含 30 个任务的波兰语专用基准 PL-MTEB，通过引入零样本评估指标量化数据重叠度，系统评估了 30 个主流嵌入模型。该工作填补了波兰语评估空白，但受限于仅覆盖单一语言，其结论对更广泛低资源语言的普适性存疑。

】

---

【Planning Beyond Text: Graph-based Reasoning for Complex Narrative Generation ｜超越文本的图推理叙事生成

研究机构：中国科学院

作者：Hanwen Gu、Chao Guo、Junle Wang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.21253)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.21253)

> 长程叙事生成面临的核心困境是模型在文本序列上直接规划时，无法有效推理事件间的因果依赖与角色关系的动态演变，导致逻辑断裂与动机缺失。现有基于大纲或角色扮演的多智能体方法虽提升了局部连贯性，但受限于线性文本表征，难以在生成前诊断并修复全局结构缺陷。PLOTTER 将叙事规划从序列文本迁移至事件图与角色图的拓扑结构，通过“评估-规划-修订”循环执行原子图编辑操作，在文本生成前完成因果逻辑的显式校验。该方法在多个骨干模型上显著优于基线，验证了图结构表征对长程因果推理的增益，但其对非线性叙事结构的表达能力及小样本前提下的泛化边界仍存疑。

】

---

【Position: From Noise to Signal to Selbstzweck - Reframing Human Label Variation in the Era of Post-training in NLP ｜从噪声到目的：人类标签变异在LLM后训练中的本体论重构

研究机构：丹麦哥本哈根大学、德国慕尼黑大学

作者：Shanshan Xu、Santosh T.Y.S.S、Barbara Plank

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_3f1e994b21f1)

> 标注者分歧长期被视为需清洗的噪声，导致主观任务模型系统性丢失少数派视角。现有分布预测方法虽能建模分歧，但忽略了分歧在数据源头被聚合丢弃的根本原因。本文提出将人类标签变异（Human Label Variation, HLV）升格为“目的本身”（Selbstzweck），主张在偏好数据构建阶段保留标注者级原始数据，而非仅在后端建模。该立场论文未提供算法验证，其价值在于确立了数据治理的伦理边界，但缺乏量化证据证明数据端多样性保留能直接转化为模型性能提升。

】

---

【PRIME: Ultra-Low-Rank Principal–Residual Model Merging ｜超低位秩主-残差模型合并

作者：Seung-Ho Lee、Kyungsu Lee、Bazarvaani Zuchi 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f438846722d1)

> 模型合并旨在通过参数空间操作整合多个专家模型，以规避联合训练的高昂成本，但任务向量间的参数干扰常导致合并性能低于单任务专家。现有基于稀疏化或子空间投影的方法在激进截断以消除干扰时，往往丢失关键的任务特异性信息，陷入干扰消解与能力保留的权衡困境。PRIME 提出超低位秩主-残差分解框架，将任务向量分离为主成分与正交残差，分别进行白化合并与正交投影恢复。该方法在 T5 和 LLaMA-3.2 上均显著优于现有代数基线，但其固定 1% 秩的设定在任务数量剧烈变化时的鲁棒性尚存疑。

】

---

【ProUIE: A Macro-to-Micro Progressive Learning Method for LLM-based Universal Information Extraction ｜渐进式通用信息抽取

研究机构：小米

作者：Wenda Liu、Song Zhigang、Shuai Nie 等 14 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_6e7842063e87)

> 通用信息抽取（UIE）旨在用单一模型统一处理命名实体识别（NER）、关系抽取（RE）与事件抽取（EE），但现有大语言模型（LLM）方法常依赖外部辅助信息或复杂验证管线，导致训练复杂且增益有限。ProUIE 提出一种无需外部信息的宏观-中观-微观渐进式学习框架，通过任务难度排序的完整建模、简化目标格式的对齐以及基于步进细粒度奖励的强化学习探索，在 36 个公开数据集上以 4B 参数骨干超越了 11B 参数的指令微调基线。该方法在 NER 和 RE 任务上表现稳健，但在 EE 任务上存在波动，其“无外部约束”的设计假设在复杂结构推理中的普适性仍存疑。

】

---

【PsyScore: A Psychometrically-Aware Framework for Trait-Adaptive Essay Scoring and ZPD-Scaffolded Feedback ｜心理测量学感知的作文评分与ZPD对齐反馈框架

研究机构：华东师范大学

作者：Wei Xia、Jin Wu、Haoran Shi 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_87173c424285)

> 自动写作评估（Automated Essay Scoring, AES）面临评分黑盒化与反馈教学价值割裂的双重困境，现有方法难以同时满足测量效度与个性化干预需求。PsyScore 通过共享潜在能力空间，将项目反应理论（Item Response Theory, IRT）嵌入神经评分器，并以此驱动最近发展区（Zone of Proximal Development, ZPD）对齐的多智能体反馈生成。该框架在 ASAP++ 数据集上实现了 0.747 的平均 QWK，验证了心理测量学校准对评分稳定性的贡献，但其反馈教学效应的因果验证仍受限于模拟修订协议。

】

---

【Rational Synthesizers or Heuristic Followers? Analyzing LLMs in RAG-based Question-Answering ｜群体证据动力学与启发式聚合

研究机构：美国卡内基梅隆大学

作者：Atharv Naphade

论文原文见 [arXiv](https://arxiv.org/abs/2601.06189)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.06189)

> 检索增强生成（RAG）系统面临的核心挑战在于，当模型面对多源、冗余且相互矛盾的检索文档时，其决策机制是否具备理性聚合能力。现有基准多聚焦于单文档或双文档的冲突仲裁，忽略了真实检索场景中“证据群体”对模型信念的扰动效应。本文通过构建 GroupQA 数据集，量化了模型在群体证据下的信念可塑性、翻转阈值及归因忠实度，揭示了大模型作为“启发式跟随者”而非“理性聚合器”的行为本质。这一发现挑战了 RAG 范式中关于模型能理性权衡证据的隐含假设，但缺乏针对该偏差的算法级干预方案。

】

---

【Reading Between the Lines: The One-Sided Conversation Problem ｜单侧对话推断：从隐私约束到文本重建

研究机构：美国华盛顿大学

作者：Victoria Ebert、Rishabh Singh、Tuochao Chen 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.03056)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.03056)

> 单侧对话推断（One-Sided Conversation, 1SC）旨在解决仅能获取对话一方话语时，如何推断缺失方内容或生成忠实摘要的问题。现有文本填充技术仅处理短片段缺失，无法应对整段对话缺失带来的语义断裂与幻觉风险。本文通过引入占位符机制与多粒度上下文策略，利用大语言模型（LLM）在单侧可观测性下重建缺失话语并生成摘要。该工作确立了1SC问题的形式化定义与评估基准，但重建结果在事实准确性上仍显著低于意图一致性，且未验证其在实时交互系统中的延迟可行性。

】

---

【Reasoning for Hierarchical Text Classification: The Case of Patents ｜层级文本分类中的推理增强：以专利IPC分类为例

研究机构：英国剑桥大学、中国科学院

作者：Lekang Jiang、Wenjun Sun、Stefan Goetz

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a9a231a7c887)

> 专利IPC分类面临标签空间巨大且层级依赖复杂的问题，传统微调模型仅输出扁平标签，缺乏审查员所需的决策依据。现有方法在可解释性与跨域泛化上存在瓶颈，本文切入点在于将分类重构为逐步推理任务。通过冷启动对齐思维链格式并引入可验证奖励强化学习，RHC在保持高精度的同时生成了可审计的逻辑链条。该方法在USPTO与EPO数据集上验证了推理框架的有效性，但其对教师模型合成数据质量的依赖及跨司法管辖区性能衰减仍存疑。

】

---

【Rectified Sparse Attention for Efficient Long-Sequence Generation ｜修正稀疏注意力

作者：Yutao Sun、Tianzhu Ye、Li Dong 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8e716de139dd)

> 长序列生成中，标准自注意力机制因需访问完整键值缓存（KV Cache）导致内存带宽成为推理瓶颈，而现有稀疏解码方法虽降低计算量，却因近似误差在缓存中累积导致生成质量随长度增加而显著退化。本文切入点在于识别出“误差累积”是稀疏解码失效的根本原因，而非单纯的检索精度不足。通过引入周期性稠密修正机制，在保持稀疏检索效率的同时将误差约束在常数窗口内。该方法在256K上下文长度下实现3.77倍端到端加速，且数学推理性能接近稠密基线，但其“近无损”结论仅验证于特定模型规模与任务类型，对复杂状态跟踪任务的泛化能力存疑。

】

---

【RepoDistill: Distilling Repository Knowledge through Compression-Aware Budget Allocation and Policy Optimization ｜代码仓库级上下文蒸馏：基于预算分配与策略优化的压缩框架

研究机构：浙江大学、上海交通大学

作者：Xin Yin、Zixiang Ding、Yiang Zhang 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2f34605a547f)

> 大语言模型在处理仓库级代码任务时，常因长上下文中的冗余信息导致注意力稀释与关键逻辑丢失。现有检索方法虽能定位相关片段，但无法在函数内部进一步剔除噪声，且静态压缩策略难以适应动态查询需求。RepoDistill 通过图结构检索结合强化学习驱动的细粒度预算分配，实现了从“片段级筛选”到“行级蒸馏”的跨越。该方法在代码问答与生成任务上显著优于基线，但其效果高度依赖预训练小模型的蒸馏质量，跨仓库泛化能力尚存疑。

】

---

【Resonant Context Anchoring: Decoupling Attention Routing and Signal Gain at Inference Time ｜共振上下文锚定

研究机构：中国科学技术大学、同济大学

作者：Mingkuan Zhao、Yide Gao、Wentao Hu 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.01923)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.01923)

> 大语言模型在检索增强生成中常因参数化记忆干扰而忽略外部证据，导致事实幻觉。现有对比解码方法虽能缓解冲突，但需多次前向传播，显著增加推理延迟；激活工程方法则因粗粒度抑制破坏语言流畅性。本文提出共振上下文锚定（Resonant Context Anchoring, RCA），通过解耦注意力路由与信号增益，在单次前向传播中动态放大上下文Value向量范数，以提升残差流中的信噪比。该方法在Llama-3系列上实现了忠实度与流畅性的帕累托改进，但其仅针对单轮、单源冲突场景，且缺乏与主流对比解码方法的同骨干公平对比，通用性存疑。

】

---

【RoleCDE: Benchmarking and Mitigating Role–Alignment Trade-offs in Role-Playing Agents ｜角色-对齐价值解耦评估与缓解

研究机构：中国人民大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4d7d6b053209)

> 角色扮演智能体（Role-Playing Agents, RPAs）在长程交互中面临的核心挑战不仅是风格漂移，更在于当角色特定利益与模型内置的对齐原则发生冲突时，模型往往丧失角色决策逻辑。现有基准多聚焦于表面保真度，缺乏对深层价值权衡能力的量化手段，导致无法区分模型是真正理解了角色动机，还是机械遵循安全护栏。本文提出 RoleCDE，通过构建大规模结构化认知困境数据集，将角色扮演评估从“风格一致性”转向“价值冲突决策”，并验证了基于该数据的微调能有效缓解模型的对齐偏向。该工作揭示了“角色-价值解耦”这一系统性失效模式，但其单步决策设定是否足以反映真实多轮交互中的动态价值演化，仍存疑。

】

---

【SAFER: Advancing Safety Alignment via Efficient Ex-Ante Reasoning ｜安全对齐中的事前推理框架

研究机构：浙江大学

作者：Kehua Feng、Keyan Ding、Yuhao Wang 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_49128214040b)

> 大语言模型（LLM）在应对复杂科学安全威胁时，常因缺乏显式推理而陷入“表面对齐”陷阱，导致防御失效。现有方法多依赖事后回溯或通用思维链，难以在生成前精准识别隐蔽风险。SAFER通过引入结构化的事前推理（Ex-Ante Reasoning）与步骤级偏好优化，将安全判断拆解为评估、验证与校准三阶段。该框架显著提升了模型在科学安全领域的鲁棒性，但其推理延迟与规则泛化边界仍存疑。

】

---

【SARA: Unlocking Multilingual Knowledge in Mixture-of-Experts via Semantically Anchored Routing Alignment ｜语义锚定路由对齐

研究机构：天津大学、阿里巴巴集团

作者：Tianyu Dong、Yangyang Liu、Jiang Zhou 等 12 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.25821)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.25821)

> 稀疏混合专家模型在低资源语言上常因路由分歧导致性能衰减，现有微调方法多聚焦输出层或隐藏状态，未能直接修正专家激活路径。SARA 将高资源语言的路由分布作为语义锚点，通过 Jensen-Shannon 散度约束对齐中间层路由概率。该方法在 Qwen3-30B-A3B 上实现了跨语言推理能力的提升，但其效果高度依赖锚点语言的质量与层选择策略，泛化性仍存疑。

】

---

【SAVOIR: Learning Social Savoir-Faire via Shapley-based Reward Attribution ｜社交智能强化学习中的合作博弈信用分配

研究机构：哈尔滨工业大学

作者：Xiachong Feng、Yi Jiang、Xiaocheng Feng 等 12 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.18982)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.18982)

> 多轮社交对话中，单句对最终结果的贡献难以量化，导致强化学习信号稀疏且缺乏理论依据。现有方法依赖大语言模型进行启发式回溯归因，忽略了语句的前瞻策略价值。本文引入合作博弈论，通过期望效用评估策略潜力，并利用Shapley值实现公平信用分配。该框架在SOTOPIA基准上刷新了7B模型的性能上限，但其高昂的Rollout计算成本限制了实时交互的可行性。

】

---

【Self-EmoQ: Plutchik-Guided Value-based Planning to Drive Streaming Emotional TTS ｜流式情感对话中的前置规划

作者：Yue Zhao、Hongyan Li、Yong Chen 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.09837)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.09837)

> 实时语音交互系统面临的核心矛盾是：情感语调必须在文本生成开始前确定，而传统情感识别只能在文本生成结束后完成。现有基于提示或监督预测的方法无法优化长期对话收益，且受限于静态标签模仿。Self-EmoQ 将情感决策重构为基于 Plutchik 理论奖励的强化学习规划问题，在文本生成前输出情感标签以驱动流式 TTS。该方法在情感决策排序指标上优于基线，但其单步值函数决策是否足以捕捉复杂情感因果链，仍存疑。

】

---

【SemPA: Improving Sentence Embeddings of Large Language Models through Semantic Preference Alignment ｜语义偏好对齐

研究机构：深圳大学

作者：Ziyang Chen、Zhenxuan Huang、Yile Wang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d8ad570de534)

> 句子嵌入学习旨在将变长文本映射为固定维度稠密向量，以支撑语义相似度评估与信息检索等下游任务，其核心价值在于弥合离散符号与连续语义空间之间的鸿沟。现有基于大语言模型（LLM）的嵌入方法面临两难：提示工程法性能受限，架构修改法往往牺牲生成能力。本文切入点在于利用直接偏好优化（DPO）在改写任务上微调LLM，使其在保留生成能力的前提下提升语义区分度。该方法通过轻量级参数更新实现句级偏好对齐，理论上统一了对比学习与DPO的优化目标。其价值在于提供了一种不破坏模型内部计算机制的嵌入增强路径，但其在大规模检索基准上的泛化能力仍存疑。

】

---

【Sentipolis: Emotion-Aware Agents for Social Simulations ｜情感状态化智能体架构

研究机构：美国卡内基梅隆大学、日本东京大学

作者：Chiyuan Fu、Lyuhao Chen、Yunze Xiao 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.18027)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.18027)

> 生成式多智能体社会模拟旨在复现高保真人工社会，但现有架构普遍缺乏长时程情感连续性，导致智能体在跨会话交互中出现“情感遗忘”，即被侮辱后后续回合易怒度不增，或重复正向互动无法累积为更强纽带。本文切入点是将情感作为一等持久状态，而非短期信号或离散标签，通过引入连续 Pleasure-Arousal-Dominance (PAD) 向量、双速动态衰减及情感-记忆耦合机制，构建可解释且骨干无关的情感模块。该架构在通信与连续性指标上带来显著提升，但其收益高度依赖底层模型容量，且对社交规范遵守的影响呈现非系统性波动，其科学有效性仍受限于沙盒规模与评估协议的泛化边界。

】

---

【SepSeq: A Training-Free Framework for Long Numerical Sequence Processing in LLMs ｜分离序列（SepSeq）：基于注意力汇聚的长数值序列处理框架

研究机构：中国科学技术大学、南京大学

作者：Jie Sun、Yu Liu、Lu Han 等 12 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_cb947e2438ef)

> 导读 Transformer大语言模型在处理长数值序列时，因Softmax机制导致注意力权重在大量相似Token间稀释，无法精确访问局部值，造成计数、过滤等精度敏感任务性能崩塌。现有扩展上下文窗口或引入外部工具的方法未能解决模型对原始序列的忠实保持瓶颈，本文切入点在于识别“注意力分散”为根本原因。SepSeq通过无训练地在序列中定期插入分隔符Token，将其作为注意力汇聚点，将长序列切分为短片段以重构注意力分布。该框架在9个主流LLM上平均提升35.6%准确率并减少16.4%推理Token消耗，但其效果依赖于模型对分隔符的内在注意力偏好，且未验证其在非Transformer架构中的普适性。

】

---

【SGG-R 3: From Next-Token Prediction to End-to-End Unbiased Scene Graph Generation ｜场景图生成中的结构化推理与长尾去偏

研究机构：北京大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f9ff98da5e30)

> 场景图生成（SGG）旨在将视觉内容转化为由对象节点和关系边组成的结构化图，其核心价值在于为视觉问答、机器人导航等高层推理任务提供可解释的语义桥梁。现有基于多模态大语言模型（MLLM）的端到端方法虽消除了两阶段误差累积，却因缺乏任务特定的结构化推理流程而陷入巨大的搜索空间，同时受限于关系数据的稀疏性与长尾分布，导致生成结果召回率低且偏向高频谓词。本文提出 SGG-R3 框架，通过三阶段结构化思维链（CoT）引导监督微调（SFT），并结合类型感知关系增强与双重粒度奖励的强化学习（RL），实现端到端的无偏场景图生成。该框架在 Visual Genome 和 Panoptic Scene Graph 基准上显著提升了长尾关系识别能力，但其对推理延迟的忽视及未对比最新去偏基线，限制了其在实时具身智能场景中的直接适用性。

】

---

【Simplify-Pro: A Two-level and Progressive LLM-based Framework for Auto Long Text Simplification ｜长文本简化中的渐进式精炼框架

研究机构：西安电子科技大学

作者：Peng Zhou、Guangxin Li、Xiaoying Huang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_7a94d10733c0)

> 长文本简化旨在降低复杂文档的阅读负荷，同时保持语义完整与结构连贯。现有句子级模型在处理超过千词输入时，常出现关键信息丢失与过渡断裂，而直接调用大语言模型（LLM）虽能生成流畅文本，却难以精确控制编辑粒度与质量稳定性。本文切入点在于将简化过程解耦为“段落级强化学习训练”与“文档级多阶段推理”，通过指标辅助分析与选择性精炼实现细粒度质量把控。该框架在文档级任务上性能匹敌或超越主流闭源LLM，但其对训练数据规模的依赖及推理阶段的计算开销仍存疑。

】

---

【Simulating Crisis Cognition: A Computational Framework for Hypothesis Generation in Crisis Communication ｜危机通信中的生成式结构因果模拟

作者：Changsen Yuan、Yanghao Zhou、Chong Feng 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_6b2448378c9a)

> 生成式社会模拟长期停留在对恐慌或谣言传播等宏观现象的定性描述，缺乏对具体干预策略因果效应的定量评估，导致政策制定者在无法开展随机对照试验的高风险场景中缺乏科学依据。现有基于检索增强生成（RAG）或规则启发式的系统往往忽视急性压力下的心理语言接受度，无法区分信息内容本身与呈现顺序对个体行为的不同影响。本文提出 CRISIS COGNITION 框架，将大语言模型（Large Language Model, LLM）重构为反事实实验室，通过生成式结构因果模型（Generative Structural Causal Model, Generative SCM）形式化危机交互，利用分层分析隔离人格混杂变量，以估计语言策略的个体处理效应。该框架在计算层面验证了“情感支架先于事实信息”的处方性假设，但其结论局限于 LLM 内部生成过程，能否外推至真实人类行为仍存疑。

】

---

【Small Data, Big Noise: Adversarial Training for Robust ParameterEfficient Fine-Tuning ｜小数据大噪声：面向参数高效微调的对抗训练框架

研究机构：以色列巴伊兰大学

作者：Eitan Cohen、Idan Simai、Uri Shaham

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a53a88fdd7b5)

> 参数高效微调（PEFT）在低资源场景下常因训练数据缺乏多样性而难以抵抗真实文本中的噪声与域偏移，导致模型性能急剧下降。现有PEFT方法虽能降低计算成本，但极少将鲁棒性作为核心优化目标，且随机噪声注入无法精准定位模型脆弱点。本文提出SDBN框架，将对抗训练引入PEFT流程，通过构造连续嵌入空间与离散字符/语义不确定性集，在训练阶段主动寻找最坏情况样本以增强模型稳定性。该方法在不增加可训练参数的前提下显著提升了小数据噪声场景下的鲁棒性，但其对生成式任务的离散扰动依赖外部大模型，且未验证在极端数据稀缺下的收敛稳定性。

】

---

【SOLAR-RL: Semi-Online Long-horizon Assignment Reinforcement Learning ｜半在线长程信用分配强化学习

研究机构：香港中文大学、美国普林斯顿高等研究院

作者：Jichao Wang、Liuyang Bian、Yufeng Zhou 等 12 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.22558)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.22558)

> GUI智能体在长程任务中面临在线强化学习（Reinforcement Learning, RL）交互成本高昂与离线强化学习（Offline RL）时序短视的双重困境，导致稀疏奖励下的信用分配失效。SOLAR-RL通过离线轨迹重构与回溯性信用分配，在静态数据中模拟伪在线反馈，解决了长程任务中的梯度消失问题。该方法以94K步数据在AndroidWorld上取得33.7%成功率，虽低于在线SOTA，但显著优于同等数据规模的离线基线，其核心在于将轨迹级质量转化为密集步骤级奖励。

】

---

【SPASM: Stable Persona-driven Agent Simulation for Multi-turn Dialogue Generation ｜稳定人格驱动智能体模拟

研究机构：英国利兹大学、以色列内盖夫本-古里安大学

作者：Han Luo、Guy Laban

论文原文见 [arXiv](https://arxiv.org/abs/2604.09212)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.09212)

> 多轮LLM交互中，智能体常因上下文累积而偏离预设角色，表现为身份漂移与回声现象。现有合成对话框架缺乏对长程稳定性的显式控制，导致生成数据污染下游训练。SPASM通过自我中心上下文投影（ECP）机制，在推理时重构对话历史视角，无需修改模型权重即可抑制漂移。该框架在消除回声方面表现显著，但其在复杂推理场景下的泛化能力尚待验证。

】

---

【Specialization without Sparsity: Efficient and Expressive Split-Path Experts for LLM Fine-Tuning ｜稀疏激活与参数效率的冲突：SparMoE 的软路由解法

作者：Ganghao Liu、Qin Zhou、Zhe Wang 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9081507bc433)

> 参数高效微调（PEFT）旨在以极小参数代价适配大模型，但现有 MoE-PEFT 方法将 LoRA 复制为专家并采用离散硬路由，导致参数量随专家数线性膨胀，且在数据稀缺下因路由高方差引发专家欠训练。本文指出离散选择与受限参数空间存在根本错配，提出 SparMoE，以全激活软路由替代硬路由，并用缩放-偏置双路径向量专家替代低秩矩阵专家，在 GLUE 上以 0.29M 参数超越全量微调。该设计在低资源微调场景下有效，但其全激活机制在长序列下的计算开销未经验证，且缺乏与大规模 LLM 推理任务 SOTA 的直接可比性。

】

---

【StateX: Enhancing RNN Recall via Post-training State Expansion ｜状态扩展后训练

研究机构：清华大学

作者：Xingyu Shen、Yingfa Chen、Zhen Leng Thai 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.22630)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.22630)

> 递归神经网络（RNN）在处理长上下文时，因将全部历史信息压缩至固定大小的隐状态，导致精确召回能力显著弱于Transformer。现有扩大状态维度的方案要么从头训练成本高昂，要么引入复杂新架构难以集成，而本文切入点在于利用预训练模型，通过低成本的后训练阶段直接扩展状态尺寸。StateX针对线性注意力与状态空间模型设计了两种无参数或低参数增加的状态扩展机制，并在1.3B规模模型上验证了其有效性。该方法以极低的额外训练成本显著提升了长上下文召回性能，但其效果是否能在更大规模或混合架构中保持，仍存疑。

】

---

【StructKV: Preserving the Structural Skeleton for Scalable Long-Context Inference ｜结构感知键值缓存压缩

研究机构：中国科学院大学、北京大学

作者：Zhirui Chen、Peiyang Liu、Ling Shao

论文原文见 [arXiv](https://arxiv.org/abs/2604.06746)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ef0c1f5ffe4d)

> 长上下文推理中，预填充阶段的二次计算复杂度与解码阶段的线性内存增长构成双重瓶颈，现有方法往往在加速预填充时牺牲解码精度，或在压缩内存时忽略计算开销。本文指出，基于单层局部显著性的剪枝策略会误删跨层信息枢纽，导致长距离依赖丢失。StructKV 通过累积全局入度中心性识别语义骨架，并动态检测注意力稳定层，实现了计算预算与存储预算的解耦。该方法在LongBench和RULER上优于FastKV，但在极低比特量化场景下的表现未经验证，其纯驱逐策略在内存效率上可能不及量化方法。

】

---

【Style Amnesia: Investigating Speaking Style Degradation and Mitigation in Multi-Turn Spoken Language Models ｜语音风格遗忘：多轮对话中副语言指令的持续性失效诊断

研究机构：国立台湾大学、新加坡南洋理工大学

作者：Yu-Xiang Lin、Cheng-Han Chiang、Hung-yi Lee

论文原文见 [arXiv](https://arxiv.org/abs/2512.23578)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_35b717aef5b8)

> 多轮语音交互中，模型能否在首轮接收风格指令后，于后续所有轮次持续保持该风格？现有评估多聚焦单轮或预定义对话，无法捕捉风格随轮次衰减的动态过程。本文通过构建基于用户模拟器的多轮交互框架，量化了五个主流语音语言模型（SLM）在情感、口音、音量与语速上的风格遵循率（IF rate）衰减现象，并证实显式召回机制可部分缓解该问题。该工作揭示了SLM在长程副语言控制上的系统性缺陷，但其缓解策略依赖额外提示开销，未触及模型内部注意力锚定机制的根本修复。

】

---

【Style over Story: Measuring LLM Narrative Preferences via Structured Selection ｜风格优先于故事：通过结构化选择测量大语言模型的叙事偏好

研究机构：韩国科学技术院

作者：Donghoon Jung、Jiwoo Choi、Songeun Chae 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.02025)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_7a36d56f54ac)

> 计算叙事领域长期依赖生成输出来评估模型能力，但输出质量混淆了“生成能力”与“内在偏好”，导致无法区分模型是“写不好”还是“不想写”。现有评估指标与人类感知错位，且缺乏对模型潜在叙事优先级的直接测量手段。本文提出一种基于200条叙事学约束的结构化选择任务，通过量化模型在受控条件下的选择行为来揭示其潜在偏好。该方法实证了模型对风格元素的系统性优先，但静态选择偏好能否预测动态生成中的风格漂移，尚存疑。

】

---

【Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on LLM Fine-Tuning ｜合成数据源多样性对大语言模型微调的影响

研究机构：荷兰乌得勒支大学

作者：Max Schaffelder、Albert Gatt

论文原文见 [arXiv](https://arxiv.org/abs/2511.01490)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b598de7dafee)

> 大语言模型在数据受限场景下依赖合成数据微调，但单一来源的合成数据会导致输出分布收窄与长尾token增加，即分布坍缩。现有缓解策略多聚焦于递归训练中的真实数据混合或外部验证器注入，缺乏对单次微调中数据源多样性效应的系统量化。本文通过对比单一源与多源合成数据微调，发现多源数据能显著缓解分布坍缩并降低自偏好偏差，但会改变模型对抗鲁棒性的风险分布。该研究填补了微调阶段数据源多样性与模型安全、评估偏差关联性的空白，但其结论局限于特定模型规模与任务类型，长期递归场景下的有效性存疑。

】

---

【TENP: Trapezoidal Expert Neuron Pruning For Mixture-of-Experts ｜梯形专家神经元剪枝

研究机构：天津大学

作者：Jiangyang He、Shaolin Zhu、Deyi Xiong

论文原文见 [arXiv](https://arxiv.org/abs/2606.09885)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.09885)

> 混合专家（Mixture-of-Experts, MoE）模型在扩展参数容量时面临静态显存占用过高的部署瓶颈。现有压缩方法要么移除整个专家从而破坏预训练路由拓扑，要么采用无结构权重剪枝导致硬件加速困难。本文切入点在于保留专家实体与路由路径，仅对专家内部冗余神经元进行结构化剪枝，并引入深度感知的梯形稀疏度分配策略。该方法在保持路由稳定性的同时显著降低了激活参数量，但在跨域泛化与极端稀疏度下的理论边界仍存疑。

】

---

【The Learnability of Model-Theoretic Interpretation Functions in Artificial Neural Networks ｜门控机制与组合性泛化：模型论解释函数的架构依赖性

研究机构：荷兰乌得勒支大学

作者：Adrian Brasoveanu、Jakub Dotlacil

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_abffa0953d4b)

> 神经符号系统长期面临的核心矛盾在于，如何利用离散符号的严谨性解决连续神经网络在组合性泛化上的脆弱性。Frank et al. (2009) 证明简单循环网络可学习真值条件表示，但受限于架构单一与测试集规模，未能厘清现代架构中何种归纳偏置真正驱动子句级组合。本文通过容量匹配对比 SRN、GRU、LSTM 与 Transformer，发现门控机制而非序列处理本身是决定 Basic Event 泛化能力的关键，并验证了实体向量对语义接地的增益。这一发现挑战了 Transformer 在组合任务上的通用性假设，但其结论局限于微语言环境，向真实语言迁移的有效性尚存疑。

】

---

【Think Before you Write: QA-Guided Reasoning for Character Descriptions in Books ｜问答引导推理用于长文本角色描述生成

研究机构：英国爱丁堡大学

作者：Argyrios Papoudakis、Mirella Lapata、Frank Keller

论文原文见 [arXiv](https://arxiv.org/abs/2604.11435)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.11435)

> 长文本角色描述生成要求模型从数十万词的小说中整合分散的角色证据，但现有长上下文模型在直接生成时往往引入幻觉或遗漏关键细节。本文发现，当前大语言模型（LLM）的内置推理模式在该任务上反而降低忠实度，空轨迹表现更优。为此，作者提出解耦推理与生成的两阶段框架，通过问答（QA）轨迹作为中间表示引导描述生成。该框架在忠实度与信息覆盖上优于基线，但其收益高度依赖上下文选择策略，且在增量处理场景中失效。

】

---

【ToM-Synth: Scaling Robust Theory of Mind in LLMs via 6,912 Structured Social Units ｜结构化社交单元合成与强化学习微调

研究机构：浙江大学、阿里巴巴集团

作者：Guiyang Hou、Xiang Huang、Shangke Lyu 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_952fd1eb91fb)

> 大语言模型在社交互动中缺乏鲁棒的心智理论（ToM）能力，现有方法依赖评估基准作为训练数据导致窄域过拟合。本文通过构建6,912个结构化社交单元，系统合成27,648条训练数据，利用Group Relative Policy Optimization (GRPO) 微调模型，将ToM能力内化至参数。该方法在开源模型中达到SOTA，但合成数据的分布覆盖度与生成模型的风格偏好是否引入新偏差，仍存疑。

】

---

【TOOLCAD: Exploring Tool-Using Large Language Models in Text-to-CAD Generation with Reinforcement Learning ｜工具调用型大语言模型在文本到CAD生成中的强化学习探索

作者：Yifei Gong、Xing Wu、Wenda Liu 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.07960)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.07960)

> 文本到CAD生成旨在将自然语言指令转化为可执行的参数化建模操作，但现有方法多依赖静态序列预测或一次性代码生成，难以处理多部件复杂模型中的长程推理与错误累积。本文切入点在于将大语言模型（LLM）重构为工具调用智能体，通过交互式CAD引擎反馈与在线强化学习（RL）实现迭代式建模。具体做法是构建包含规则奖励与结果监督的混合反馈环境，利用课程学习策略训练LLM自主规划并调用CAD原语工具。该框架在开源模型上实现了接近闭源模型的性能，但其对L3级精确指令的依赖及缺乏多模态输入支持，限制了其在模糊设计意图场景下的泛化能力。

】

---

【Towards Efficient Large Language Model Serving: A Survey on System-Aware KV Cache Optimization ｜系统感知的大语言模型键值缓存基础设施

研究机构：澳大利亚墨尔本大学、华中科技大学

作者：Jiantong Jiang、Peiyu Yang、Rui Zhang 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2607.08057)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2607.08057)

> 大语言模型（LLM）推理服务面临键值缓存（KV Cache）随序列长度线性增长导致的显存溢出与内存带宽瓶颈，现有算法级压缩方法（如驱逐、量化）往往孤立优化单一指标，忽视了系统层面的调度、放置与表示协同。本文提出系统感知的大语言模型键值缓存基础设施（sKis）框架，将KV优化重构为时间、空间、结构三维系统行为空间，通过行为-目标矩阵揭示不同优化策略对延迟、吞吐与内存的差异化影响。该框架提供了稳定的分析透镜，但缺乏统一基准下的端到端性能验证，其分类法是否掩盖了算法与系统实现的耦合效应仍存疑。

】

---

【Towards IP Intelligence: Benchmarking Large Language Models on Intellectual Property Knowledge and Practice ｜知识产权大语言模型基准测试

研究机构：中国科学院、澳大利亚新南威尔士大学

作者：Qiyao Wang、Guhong Chen、Hongbo Wang 等 23 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8783dcbd7193)

> 现有专利自然语言处理基准多局限于单一专利文本的语义匹配或摘要生成，缺乏对商标、版权等多元知识产权机制及法律推理深度的覆盖，导致无法全面评估大语言模型在真实法律实务中的能力。IPBench 基于 Webb 的知识深度理论构建了四级任务分类法，填补了跨机制、跨认知层级的评估空白。该基准通过 10,374 个双语样本量化了通用模型与垂直模型在信息处理、逻辑推理及创造性生成上的表现差异。尽管其揭示了垂直模型在复杂推理任务上的泛化瓶颈，但评估结果对模型训练语言与司法管辖区的强依赖性仍存疑。

】

---

【Towards Proactive Information Probing: Customer Service Chatbots Harvesting Value from Conversation ｜客服对话中的主动信息探测

研究机构：新加坡国立大学、四川大学

作者：Chen Huang、Zitan Jiang、Changyi Zou 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.11077)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.11077)

> 客服机器人长期被定位为被动响应工具，难以在解决用户问题的同时获取高价值商业情报。现有主动代理方法多聚焦于提升用户服务体验，缺乏针对系统侧信息获取目标的时序决策机制，导致探测时机不当引发用户反感或信息遗漏。本文提出PROCHATIP框架，通过独立的对话策略模块结合两阶段训练，优化探测时机以平衡信息获取与用户满意度。该方法在FinQA和ConvQA基准上显著优于基线，但受限于单一信息不对称假设，其策略在复杂真实场景中的泛化能力存疑。

】

---

【Towards Scalable Lightweight GUI Agents via Multi-role Orchestration ｜轻量级GUI智能体的多角色编排

研究机构：浙江大学

作者：Ziwei Wang、Junjie Zheng、Leyang Yang 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.13488)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.13488)

> 该方向旨在解决轻量级多模态大语言模型（MLLM）在资源受限设备上部署时，因参数容量瓶颈与端到端学习范式导致的任务可扩展性不足问题。现有方案或依赖大规模模型的高昂推理成本，或受限于单一模型在长程任务中的错误累积与上下文丢失。本文切入点在于通过参数共享实现单模型多角色编排，将高维推理解耦为可协同的子任务流。具体做法是结合角色导向数据合成与两阶段训练（SFT+RL），使轻量模型既能独立执行，又能作为高级规划器的可插拔执行器。其价值在于以3B参数规模实现了接近大模型的在线执行能力，但独立端到端性能仍显著低于专用大模型，且高度依赖外部规划器。

】

---

【Uncertainty-Aware Contrastive Sentence Embedding With Local Context Representation for Text Classification ｜不确定性感知对比句嵌入

研究机构：深圳大学

作者：Han Liu、Jiaqing Zhan、Zhichao Chen 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_fa8503eb9017)

> 句子嵌入学习旨在将变长文本映射为固定维度稠密向量，以支撑语义相似度评估与信息检索等下游任务，其核心价值在于弥合离散符号与连续语义空间之间的鸿沟。现有基于大语言模型（LLM）的嵌入方法多采用确定性输出，难以区分语义清晰与模糊文本，导致模型在歧义样本上过拟合。本文切入点在于引入不确定性量化机制，通过高斯分布建模表示方差，并结合标签驱动对比学习优化分类几何结构。该方法冻结骨干网络，仅训练轻量级局部上下文提取模块，在文本分类任务上实现了小模型超越大模型的效果，但其对检索任务及生成能力保留的适用性尚存疑。

】

---

【Understanding Generalization in Role-Playing Models via Information Theory ｜角色扮演模型分布偏移下的泛化度量

研究机构：武汉大学

作者：Yongqi Li、Hao Lang、Fei Huang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.17270)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.17270)

> 角色扮演模型在真实部署中因用户、角色或对话结构的分布偏移而性能骤降，现有基于大语言模型裁判的评估方法仅能给出整体分数，无法诊断具体偏移来源。本文切入点在于构建一个信息论框架，将性能下降与分布偏移的统计量直接关联。通过引入推理变量并推导理论上界，该方法实现了可解释的泛化风险量化。这一框架提供了诊断工具，但其对模型实际性能提升的间接性，以及推理机制在训练中的负迁移现象，限制了其作为独立优化策略的适用性。

】

---

【What Do Vision-Language Models Encode for Personalized Image Aesthetics Assessment? ｜视觉语言模型隐层表征中的个性化美学属性编码

研究机构：日本东京大学、日本理化学研究所

作者：Koki Ryu、Hitomi Yanaka

论文原文见 [arXiv](https://arxiv.org/abs/2604.11374)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.11374)

> 个性化图像美学评估（PIAA）旨在预测特定用户对图像的主观审美评分，以解决通用美学模型无法捕捉个体偏好差异的问题。现有方法依赖大规模通用数据集训练或复杂的多阶段微调，导致计算成本高且跨域泛化能力弱。本文切入点在于验证视觉语言模型（VLMs）隐层表征中是否已编码支持个体级个性化的连续美学属性，并通过线性回归直接利用这些表征实现免微调的PIAA。该方法在艺术域显著优于专用模型，但在摄影域仅与专用模型持平，且其个性化效果是否完全源于隐层属性编码而非预训练中的通用偏见，仍存疑。

】

---

【What's Missing in Screen-to-Action? Towards a UI-in-the-Loop Paradigm for Multimodal GUI Reasoning ｜UI-in-the-Loop：基于强化学习的GUI元素语义理解与推理范式

研究机构：浙江大学

作者：Songze Li、Xiaoke Guo、Tianqi Liu 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.06995)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.06995)

> 现有GUI智能体普遍采用“屏幕-动作”直接映射范式，将界面理解隐式嵌入坐标预测中，导致模型缺乏对UI元素语义功能的显式建模，在复杂布局下易发生黑盒决策失败。本文指出，模型对UI元素定位、语义描述及实际用法的掌握程度直接决定推理成功率，但当前基准仅评估最终动作准确性，忽略了中间理解过程。为此，作者提出UI-in-the-Loop（UILoop）范式，通过UI元素驱动的强化微调（UI-Element-Driven Reinforcement Fine-Tuning, RFT）显式训练模型解析界面元素，并构建了包含26K样本的UI Comprehension-Bench基准。该工作验证了显式UI理解对多步交互成功率的提升作用，但其对纯坐标定位精度的贡献及跨架构泛化能力尚存疑问。

】

---

【When Facts Change: Temporal Knowledge Conflict Resolution in LLMs ｜时间性知识冲突中的事实可变性诊断

作者：Jonas Wallat、Wolfgang Nejdl、Sandipan Sikdar

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_90f893989a76)

> 检索增强生成（RAG）系统面临参数化记忆与外部上下文的时间错位，导致模型在事实更新时产生冲突。现有解码干预方法假设冲突源于静态权重偏差，却忽略了事实本身的“可变性”这一动态仲裁信号。本文通过构建基于 Wikidata 真实时间戳的基准，诊断模型是否自发利用可变性进行推理，发现模型虽能识别可变事实，但推理与最终预测存在脱节。该工作揭示了当前 LLM 在时间性冲突中“知而不行”的机制缺陷，为后续基于内部状态的动态仲裁提供了关键诊断依据，但其结论局限于推理模型的文本轨迹，未验证非推理模型的内部表征。

】

---

【When Meaning Travels: A Granular Lens on Hybrid-MoE’s Role in Idiomatic Understanding for Language Models ｜混合专家习语理解框架

研究机构：印度理工学院

作者：Sarmistha Das、Vaibhav Vishal、Shreyas Guha 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_600188a3e843)

> 习语的非组合性语义在低资源语言中因缺乏大规模平行语料而难以被视觉语言模型（VLM）准确解码，现有基准多聚焦英语且忽略情感语调维度。本文切入点在于构建涵盖印地语、孟加拉语和泰语的Varnika数据集，并引入混合专家架构以解耦文本与视觉线索。通过超网络共享专家知识并注入习语属性信号，该框架在V-FLUTE上将IV分数从0.75提升至0.89。其价值在于填补了多模态习语语调建模的空白，但语调识别准确率仍低于0.6，表明文化细微差别的捕捉能力有限。

】

---

【Will it Merge? On The Causes of Model Mergeability ｜模型更新的可合并性归因分析

研究机构：以色列理工学院、IBM研究院

作者：Adir Rahamim、Asaf Yehudai、Boaz Carmeli 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_56a884c3193b)

> 模型合并旨在通过参数空间操作整合多个专家模型，以缓解海量微调模型部署时的存储与推理成本瓶颈。现有算法如 TIES-Merging 和 KNOTS 聚焦于消解参数干扰，但未能解释为何在相同训练条件下，部分模型更新能无缝融合而另部分则导致性能退化。本文切入点在于定义“可合并性”（Mergeability），将其量化为模型更新在合并后保留知识的程度，并归因于基座模型对特定任务的先验知识。通过构建基于基座准确率的加权合并策略，本文证明了先验知识是决定合并成败的主导因素，但该方法在极端异构任务下的鲁棒性尚未得到充分验证。

】

---

【WindowsWorld: A Process-Centric Benchmark of Autonomous GUI Agents in Professional Cross-Application Environments ｜WindowsWorld：面向专业跨应用工作流的GUI智能体过程感知基准

研究机构：哈尔滨工业大学

作者：Jinchao Li、Yunxin Li、Chenrui Zhao 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.27776)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.27776)

> 现有GUI智能体基准多聚焦单应用导航，无法反映真实办公场景中跨应用协同的认知负荷，且“全有或全无”的评分机制掩盖了长程任务中的部分进展。WindowsWorld通过构建181个以16种职业角色为锚点的跨应用任务，并引入中间检查点评分，填补了专业级多应用工作流评估的空白。其核心贡献在于将评估粒度从终态匹配推进至过程诊断，但20%左右的最高成功率也暴露了当前模型在跨应用状态维护上的根本缺陷。

】

---

【Working Memory Constraints Scaffold Learning in Transformers under Data Scarcity ｜工作记忆约束下的Transformer归纳偏置

研究机构：英国艾伦·图灵研究所

作者：Pranava Madhyastha、Dagmar Adamcova

论文原文见 [arXiv](https://arxiv.org/abs/2604.20789)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.20789)

> 高效Transformer架构研究长期聚焦于算力与参数预算下的效率优化，但忽视了模型内部表征与人类认知机制的结构性错位。现有线性注意力或混合架构虽降低了计算复杂度，却未解决小数据场景下语法表征学习低效及心理语言学对齐度不足的问题。本文切入点在于将人类工作记忆（Working Memory, WM）的容量限制与衰减特性直接编码为注意力机制的硬约束，通过从头训练验证其作为归纳偏置的有效性。该方法在10M词数据规模下显著提升了BLiMP语法准确率，但在100M词规模下优势收窄，且未报告计算效率指标，其“认知效率”与“计算效率”的权衡关系尚存疑。

】

---

【Zipage: Maintain High Request Concurrency for LLM Reasoning through Compressed PagedAttention ｜压缩分页注意力

研究机构：北京交通大学

作者：Mengqi Liao、Lu Wang、Chaoyun Zhang 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.08743)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.08743)

> 大语言模型推理服务在高并发长序列场景下，键值缓存（KV Cache）的线性增长导致显存溢出，成为限制吞吐量的核心瓶颈。现有算法级驱逐方法虽能降低内存占用，但无法与现代推理引擎的连续批处理及前缀缓存机制兼容，导致实际吞吐量低于全量缓存引擎。本文提出压缩分页注意力，将Token级KV驱逐与分页内存管理深度集成，通过混合调度与异步压缩实现高并发下的内存恒定。该方案在数学推理任务上实现了2.1倍提速并保留95%精度，但其对非RoPE架构及多模态场景的适用性尚未验证。

】

---

【清华等团队提出零令牌Transformer：解耦首尾层并引入虚拟零令牌，实现自适应早期退出

研究机构：清华大学、南方科技大学

作者：Guanghao Li、Wenhao Jiang、Li Shen 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9c6eb8902b0e)

> 在固定参数预算下提升大语言模型（LLM）的推理深度，是突破算力限制的关键路径。现有参数循环方法往往强制所有层共享权重，导致功能冲突且缺乏动态停止机制，难以平衡计算效率与精度。本文提出零令牌Transformer（Zero Token Transformer, ZTT），通过解耦首尾层并引入虚拟零令牌作为注意力控制信号，实现自适应早期退出。该架构在60M至7B参数规模上验证了有效性，但其优势是否随模型规模扩大而衰减，以及零令牌阈值在不同任务间的迁移性，仍存疑。

】

---

【科学院团队新研究：Sparse Growing Transformer: Training-Time Sparse Depth Allocation via Progressive Attention Looping

研究机构：中国科学院、中国科学院大学

作者：Yao Chen、Yilong Chen、Yinqi Yang 等 12 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_6db3261f249a)

> 大语言模型在扩展深度以提升推理能力时，面临参数规模与计算成本的同步膨胀，而现有递归架构采用静态拓扑与块级复用，导致训练阶段产生大量冗余计算。本文指出，深度分配不应是预设的静态结构，而应是随训练进程动态生长的稀疏过程。通过引入注意力熵作为结构生长信号，SGT实现了从深层到浅层的渐进式头级递归，将额外训练FLOPs开销从16-20%压缩至1-3%。该方法在中小规模模型上验证了效率-性能权衡的显著优势，但其熵值信号在超大规模或长序列下的鲁棒性仍存疑。

】

# ACL-Findings2026 · 计算机视觉基础任务方向论文汇编

> 本方向共 89 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【A Scalable Entity-Based Framework for Auditing Bias in Large Language Models ｜实体替换不变性审计框架

研究机构：法国巴黎萨克雷大学

作者：Akram Elbouanani、Aboubacar Tuo、Adrian Popescu

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f728652a6a57)

> 大语言模型在政治、地缘及经济等高风险决策场景中，其输出常受实体名称而非文本证据驱动，导致系统性偏见。现有基准依赖静态模板，牺牲了生态效度，难以反映真实部署中的偏见动态。本文提出基于实体替换不变性的黑盒审计框架，通过合成数据控制变量，量化模型对实体身份的依赖程度。该框架实现了19亿数据点的大规模审计，验证了合成数据作为真实偏见代理的有效性，但其对复杂推理链中偏见放大的覆盖仍存疑。

】

---

【A Survey of Toxicity Mitigation Strategies for Multilingual Language Models ｜多语言大语言模型毒性检测与缓解策略综述

研究机构：印度理工学院、美国弗吉尼亚大学

作者：Soham Dan、Himanshu Beniwal、Thomas Hartvigsen

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_321db5c8f158)

> 多语言大语言模型（LLM）在跨语言应用中常因文化错位与数据偏差生成毒性内容，而现有安全对齐机制高度依赖英语中心范式，导致低资源语言场景下毒性残留与误判频发。本文切入点在于系统梳理多语言特有的威胁模型（如语言切换越狱、翻译中介攻击），并构建覆盖数据、解码、对齐与表示干预的全景式分类法。通过整合威胁模型、任务设置与缓解机制，本文揭示了英语中心对齐在多语场景下的系统性失效。其价值在于提供了多语去毒的结构化认知框架，但作为综述缺乏统一基准下的定量对比，且对因果推断等新兴技术路线在多语下的适用性讨论不足。

】

---

【A Unified Feature Mixture Framework for Joint Speech and Singing Deepfake Detection ｜统一语音与歌唱深伪检测的混合专家框架

作者：Aastha Sharma、Guangjing Wang

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e2705f4766f4)

> 音频深伪检测长期聚焦于对话语音，但AI生成音乐与歌手声音克隆的普及使得威胁边界扩展至歌唱域，现有语音检测器在歌唱数据上普遍失效。本文指出单一特征表征无法同时捕捉语音的音素动态与歌唱的谐波失真，导致跨域泛化灾难性失败。GenuVoice通过构建包含频谱、倒谱与自监督特征的三专家混合架构，结合保留语音能力的多域微调策略，实现了单一推理框架下的统一检测。该方法在歌唱基准上取得了显著性能提升，但其在野外数据上的门控失准问题揭示了当前架构对数据分布不平衡的脆弱性。

】

---

【A2O: LLM-based Agentic Learning of Action-to-Object Features for Video Action Recognition ｜代理式动作-物体特征学习

研究机构：OpenAI

作者：Taiki Sekii、Fumiaki Sato

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_bd6930610105)

> 视频动作识别面临的核心矛盾是：基于视频体积的自监督模型易受背景捷径干扰，而基于物体检测的方法虽能抑制干扰却丢失场景上下文。现有方案在“保留信息”与“去除冗余”之间难以兼得，本文切入点在于利用大语言模型（LLM）的常识知识动态选择关注物体，通过上下文强化学习（ICRL）优化这一选择过程。具体做法是将LLM作为代理，结合开放词汇目标检测器（OVD）生成物体中心特征，注入视频基础模型以指导特征提取。该方法在抑制虚假相关方面表现优异，但在通用基准上的增益有限，且高度依赖LLM的推理稳定性。

】

---

【AHEAD: Attention Head Energy-Aware Dynamics for Hallucination Mitigation in MLLMs ｜注意力头能量感知动态重加权

作者：Jiale Chang、Ying Li、Siliang Tang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a761e994c9e6)

> 多模态大语言模型（MLLM）在生成图像描述时，常因语言先验覆盖视觉证据而产生幻觉。现有解码干预方法多将幻觉视为全局分类错误，通过对比解码或Logits调整进行静态抑制，忽略了注意力头在推理过程中的异质性动态行为。AHEAD从能量场视角重新定义幻觉为“轨迹逃逸”，通过训练轻量级潜在网络量化每个注意力头的视觉接地与语言先验贡献，并在推理时动态重加权以抑制幻觉。该方法在免微调基座模型的前提下显著降低了幻觉率，但其依赖COCO标注训练的泛化边界尚待验证。

】

---

【ArrowGEV: Grounding Events in Video via Learning the Arrow of Time ｜基于时间箭头学习的视频事件定位

研究机构：南京大学、小米

作者：Fangxu Yu、Ziyao Lu、Liqiang Niu 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.06559)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.06559)

> 视频时序定位旨在将自然语言查询映射至未剪辑视频中的精确时间区间，但现有视觉语言模型（VLM）仅针对正向视频训练，导致其无法感知事件语义随时间反转而发生的根本性变化。这种对时间方向性的忽视使得模型在反向视频中产生幻觉定位，或在不变事件上定位不一致，严重制约了模型的鲁棒性与泛化能力。ARROWGEV 提出一种基于强化学习（RL）的框架，通过区分时间敏感与时间不敏感事件，利用差异化奖励函数显式建模时间方向性。该方法在三个基准上提升了定位精度与方向性理解，但其性能仍低于部分全监督基线，且依赖 LLM 进行事件分类，引入了潜在的噪声风险。

】

---

【Audit Me If You Can: Query-Efficient Active Fairness Auditing of Black-Box LLMs ｜有界主动公平审计

研究机构：德国柏林工业大学、比利时鲁汶大学

作者：David Hartmann、Lena Pohlmann、Lelia Hanslik 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.03087)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.03087)

> 黑盒大语言模型（LLM）在部署后常因查询成本与隐私限制无法进行全量公平性评估，传统静态基准无法捕捉动态系统中的群体性能差异。现有被动采样方法在严格精度阈值下查询效率极低，导致独立审计难以在有限预算内完成。本文提出有界主动公平审计（Bounded Active Fairness Auditing, BAFA），通过约束优化构建代理模型版本空间并主动选择高不确定性查询，以最小化查询次数估计排序公平性指标。该方法在两个案例研究中将查询成本降低最高41倍，但其有效性依赖于代理模型与黑盒模型的分布匹配度，在极低预算场景下表现不稳定。

】

---

【Beyond A Fixed Seal: Adaptive Stealing Watermark in Large Language Models ｜自适应窃取水印算法

研究机构：北京邮电大学、香港科技大学

作者：Shuhao Zhang、Yuli Chen、Jiale Han 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.10893)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.10893)

> 大语言模型（LLM）水印面临的核心威胁不仅是内容篡改，更是水印机制本身的逆向工程。现有窃取水印算法（SWA）依赖固定策略，无法适应不同水印对上下文位置的非均匀依赖，导致攻击效率受限。本文提出自适应窃取（AS），通过基于位置的印章构建与动态选择机制，将静态模式复制转化为动态决策过程。该工作揭示了现有水印在有限查询下的严重信息泄露，但仅聚焦攻击侧，未提供防御方案。

】

---

【Beyond Output Confidence: Epistemic-Aware Hallucination Detection with Answer-Level Signals ｜答案级内在认知（AIC）：基于认知边界稳定性的二维幻觉检测

作者：Jieran Li、Xiuyuan Hu、Yang Zhao 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_6e914da831a3)

> 大语言模型在知识边界外常生成高置信度错误答案，即低熵幻觉，导致传统基于概率尖锐度的检测器失效。现有黑盒方法将输出不确定性等同于幻觉风险，无法区分“边界内模糊”与“边界外自信”，而白盒探针又依赖内部访问权限。本文提出答案级内在认知（Answer-level Intrinsic Cognition, AIC），通过多次随机解码的答案语义集中度估计模型可知性，并将其作为分母校准一维不确定性，构建无需训练、无需外部知识的二维检测分数。该方法在三个基准上稳定超越一维基线，但绝对性能仍低于白盒SOTA，且其“一致性即可知性”的假设在极端对抗场景下的鲁棒性存疑。

】

---

【Beyond Unimodal Shortcuts: MLLMs as Cross-Modal Reasoners for Grounded Named Entity Recognition ｜超越单模态捷径：基于模态感知一致性推理的接地多模态命名实体识别

研究机构：哈尔滨工业大学、中国科学院

作者：Jinlong Ma、Yu Zhang、Xuefeng Bai 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2ba68439dda1)

> 接地多模态命名实体识别（Grounded Multimodal Named Entity Recognition, GMNER）要求模型在提取文本实体的同时，将其定位到图像中的对应区域，其核心难点在于多模态大语言模型（MLLMs）常依赖单模态启发式规则而非严格的跨模态验证，导致实体定位或类型错误。现有方法多将MLLMs作为流水线中的辅助工具进行特征对齐，未能充分利用其跨模态推理潜力以消除模态偏差。本文提出模态感知一致性推理（Modality-aware Consistency Reasoning, MCR）框架，通过多风格推理模式注入与约束引导可验证优化，强制模型执行显式的跨模态一致性检查。该框架在多个基准上显著超越了现有基线，但其对特定推理模板的依赖及在长尾实体上的泛化边界仍需进一步检验。

】

---

【Bias Dynamics in BabyLMs: Towards a Compute-Efficient Sandbox for Democratising Pre-Training Debiasing ｜低成本代理模型用于预训练去偏

研究机构：英国剑桥大学

作者：Filip Trhlik、Andrew Caines、Paula Buttery

论文原文见 [arXiv](https://arxiv.org/abs/2601.09421)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.09421)

> 大语言模型（LLM）偏见研究长期受限于高昂的重训练成本，导致主流方法聚焦于后训练干预，难以触及偏见形成的根源。本文提出利用低资源BabyLMs作为沙箱，验证其在偏见获取与去偏响应上能否替代标准BERT模型。通过建立BabyLMs与BERT在去偏行为上的高相关性，本文实现了将预训练去偏实验成本从500 GPU-hours降至30 GPU-hours。这一基础设施贡献降低了研究门槛，但其代理效应的绝对值映射能力仍存疑。

】

---

【BiasGRPO: Stabilizing Bias Mitigation in High-Variance Reward Landscapes via Group-Relative Policy Optimization ｜组相对策略优化在偏见缓解中的应用

作者：Saket Reddy、Ke Yang、ChengXiang Zhai

论文原文见 [arXiv](https://arxiv.org/abs/2606.04807)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.04807)

> 大语言模型（LLM）偏见缓解面临高方差、主观性强的奖励景观，导致传统偏好优化算法在去偏与通用能力保持间难以平衡。直接偏好优化（DPO）因离线静态对限制泛化，近端策略优化（PPO）因独立评估器模型引入训练不稳定性，现有方法无法兼顾去偏效果与训练鲁棒性。本文提出BiasGRPO框架，通过组相对策略优化（GRPO）替代评估器模型，利用组内奖励归一化稳定高方差奖励信号，并配套自定义偏见奖励模型与合成数据集。该方法在Phi-2模型上实现了多基准偏见分数下降与知识保持，但缺乏与内部机制干预方法的横向对比，其优势在更大规模模型上的可迁移性存疑。

】

---

【BOLT: Benchmarking Open-World Learning for Text Classification ｜开放世界文本分类基准与LLM后验评分

研究机构：中国科学院、中国科学院大学

作者：Chuan Qin、Xi Chen、Jinpeng Li 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_5bc5e30a56ca)

> 开放世界文本分类（Open-World Text Classification, OTC）旨在让模型在仅见部分已知类别时，既能准确分类已知样本，又能拒绝或发现未知类别。现有评测多局限于单一意图识别数据集且缺乏统一协议，导致方法间无法公平比较，且大语言模型（Large Language Models, LLMs）在其中的潜力未被系统探索。BOLT通过构建涵盖12个数据集、统一已知类别比例（Known Class Ratio, KCR）与标注比例（Labeled Ratio, LAR）的基准，并引入LLM后验评分机制，填补了这一空白。该工作验证了LLM在未知类别检测上的优势，但其对LLM规模效应的非线性发现及纯文本模态的局限，使其结论的普适性仍存疑。

】

---

【Bridging the Pose-Semantic Gap: A Cascade Framework for Text-Based Person Anomaly Search ｜结构-语义解耦级联框架

研究机构：浙江大学、新加坡国立大学

作者：Zequn Xie、Guijin Luo、Chuxin Wang 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.23282)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.23282)

> 文本驱动行人异常检索（Text-based Person Anomaly Search, TPAS）旨在通过自然语言描述定位监控档案中的特定行为事件，其核心难点在于几何结构相似但语义截然不同的动作（如跌倒与俯卧撑）极易被传统姿态模型混淆。现有方案要么依赖轻量级模型牺牲语义精度，要么直接部署多模态大语言模型（MLLM）导致推理延迟无法满足实时需求。本文提出结构-语义解耦级联框架（Structure-Semantic Decoupled Cascade, SSDC），通过轻量级结构粗筛与多智能体语义验证的两阶段解耦，在保持高精度的同时大幅降低计算开销。该框架在PAB基准上取得了具有竞争力的性能，但其绝对精度仍低于当前SOTA，且多智能体协作的必要性缺乏充分的消融对比。

】

---

【C-ReD: A Comprehensive Chinese Benchmark for AI-Generated Text Detection Derived from Real-World Prompts ｜中文真实提示词AI生成文本检测基准

研究机构：清华大学、南开大学

作者：Chenxi Qing、Junxi Wu、Zheng Liu 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.11796)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.11796)

> 现有中文AI生成文本检测基准普遍依赖单一生成模型与简化问答格式，无法反映多领域、多国产大模型的真实应用场景。C-ReD通过构建涵盖5个领域、9个LLM及真实提示词的基准，系统评估了零样本与监督检测器在中文语境下的泛化瓶颈。该工作揭示了推理密集型模型（如Deepseek-R1）对检测器的显著挑战，并验证了多域微调对跨模型泛化的提升作用。其价值在于填补了中文检测基准的空白，但缺乏对对抗改写攻击的直接测试，且未量化提示词复杂度对检测难度的因果影响。

】

---

【C2PO: Diagnosing and Disentangling Bias Shortcuts in LLMs ｜因果对比偏好优化

研究机构：新加坡南洋理工大学

作者：Xuan Feng、Bo An、Tianlong Gu 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_51fd16dff4e1)

> 大语言模型在推理任务中常依赖词汇重叠或刻板印象等捷径，导致输出系统性偏差，而现有对齐方法往往在消除偏见时牺牲通用能力。直接偏好优化（DPO）等整体优化范式无法解耦语义质量与虚假关联，导致模型在复杂推理中失效。本文提出C2PO，通过挖掘因果反事实三元组并引入公平敏感的双动态目标函数，在优化过程中同时发现并抑制偏见捷径。该方法在打破偏见-能力权衡方面表现优异，但其对教师模型的依赖及单轮对话的局限仍需审视。

】

---

【Can Small Vision–Language Models Perform Sign Language Translation? ｜小型视觉语言模型在手语翻译中的适用性评估

作者：Anal Roy Chowdhury、Debarshi Kumar Sanyal

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_371e9ff91fb7)

> 手语翻译（SLT）旨在将连续视频流转化为自然语言文本，核心难点在于捕捉手势的时空语义与语法结构。现有专用架构依赖大量手语特定预训练，而通用视觉语言模型（VLM）虽具备多模态能力，但缺乏手语归纳偏置。本文通过冻结视觉编码器、仅微调连接器与语言模型，系统评估了三种小型VLM在四种手语数据集上的表现。实验证实通用VLM在SLT任务上显著落后于专用系统，并揭示了基准数据的词汇偏差问题。这一负面结果划定了通用模型直接迁移的边界，但未能区分性能瓶颈源于视觉表征缺失还是语言生成偏差。

】

---

【CausalDetox: Causal Head Selection and Intervention for Language Model Detoxification ｜因果头选择与干预语言模型去毒

作者：Yian Wang、Yuen Chen、Agam Goyal 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.14602)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.14602)

> LLM生成毒性源于预训练语料污染，现有解码时干预或微调方法常因依赖相关性启发式而误伤良性语言，或在抑制毒性时破坏语义连贯性。本文切入点在于区分“相关”与“因果”，利用概率必要性与充分性（Probability of Necessity and Sufficiency, PNS）定位对毒性生成既必要又充分的最小注意力头集合。通过全局/局部推理时干预及PNS引导微调，在保留流畅度的前提下实现精准去毒。该方法在受控反事实基准上优于相关性基线，但其因果假设在复杂语境下的稳定性及与主流微调范式的横向对比缺失，限制了其普适性结论。

】

---

【CausalGaze: Unveiling Hallucinations via Counterfactual Graph Intervention in Large Language Models ｜因果图干预幻觉检测

研究机构：国防科技大学

作者：Linggang Kong、Lei Wu、Yunlong Zhang 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.11087)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.11087)

> 大语言模型（LLM）在生成事实性内容时，常因内部表征中的噪声关联产生高置信度幻觉，传统白盒探测方法仅能捕捉表层统计相关，无法区分结构性鲁棒知识与脆弱关联模式。CausalGaze 将隐藏状态与注意力图建模为动态因果图，通过梯度引导的反事实干预剥离噪声边，实现从被动观察到主动干预的范式转变。该方法在 TruthfulQA 上较前驱 HaluGNN 提升 5.2% AUROC，但实验局限于 7B 规模开源模型，未验证因果干预在更大规模或闭源模型上的泛化性。

】

---

【Cause-CSD: A Challenge Multimodal Conversational Stance Cause Detection Dataset and Effective Method ｜对话式立场-原因对检测

研究机构：中国科学技术大学、哈尔滨工业大学

作者：Fuqiang Niu、Bowen Zhang、Junting Zhu 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1b0e0cad6bda)

> 对话式立场检测（CSD）长期面临“标签准确但证据缺失”的困境，导致模型无法区分立场源于事实、情绪还是外部信息，限制了其在危机响应等高风险场景的干预能力。现有方法将立场视为孤立标签，忽略了支撑立场的语境单元，而本文提出对话式立场-原因对检测（CSCPD）任务，旨在联合预测立场极性及其可观测语境证据。通过构建首个大规模数据集Cause-CSD并提出两阶段框架SCD-LM，该工作实现了立场与证据的联合解码。尽管在自建基准上取得SOTA，但Pair-F1绝对值偏低且缺乏跨数据集验证，其泛化边界尚待厘清。

】

---

【CEAID: Benchmark of Multilingual Machine-Generated Text Detection Methods for Central European Languages ｜中欧语言机器生成文本检测基准

作者：Dominik Macko、Jakub Kopal

论文原文见 [arXiv](https://arxiv.org/abs/2509.26051)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.26051)

> 导读 机器生成文本（Machine-Generated Text, MGT）检测长期聚焦于英语等高资源语言，导致低资源语言面临严重的跨语言迁移性能衰减。现有零样本统计方法在形态复杂的非英语语言中失效，而通用监督模型又缺乏区域特定训练数据。本文构建了首个中欧区域多语言MGT检测基准，系统评估了训练语言组合对跨语言泛化及对抗鲁棒性的影响。该研究证实了监督微调在低资源场景下的必要性，并揭示了同形异义字攻击对斯拉夫语系的特异性破坏力。然而，其结论受限于拉丁脚本语言，对非拉丁语系的适用性仍存疑。

】

---

【CMTD: Cognitive Modeling with Traits and Distortions for Multimodal Emotion Recognition in Conversations ｜认知建模与特质扭曲融合的多模态对话情感识别

作者：Minh-Tien Nguyen、Huu-Loi Le、Manh-Cuong Phan 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b869a301abe6)

> 多模态对话情感识别（MERC）旨在从文本、视觉与语音中推断说话者的离散情绪状态，但现有方法常将长期人格特质与短期认知扭曲混同处理，导致在复杂对话中误判中性或混合情绪。本文切入点在于利用心理学理论显式解耦静态特质与动态扭曲，通过多智能体协作重构说话者的认知模型。具体做法是构建包含特质、扭曲、视觉、语音及融合代理的LLM框架，在零样本设置下预测情绪标签。该框架在MELD与IEMOCAP上优于纯文本基线，但性能仍低于训练式SOTA，且其依赖LLM推理能力的假设在跨域泛化中是否稳健尚存疑。

】

---

【Content Fuzzing for Escaping Information Cocoons on Digital Social Media ｜内容模糊测试以逃逸数字社交媒体信息茧房

研究机构：美国加州大学戴维斯分校

作者：Yifeng He、Ziye Tang、Hao Chen

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b1860ad53cf3)

> 信息茧房由推荐算法基于立场标签的过滤机制固化，导致用户仅接触同质化观点。现有去偏或重排序方法依赖平台侧控制，内容创作者无法干预，而传统对抗攻击往往破坏文本语义，难以在保持原意的前提下改变机器分类结果。本文提出 ContentFuzz，一种基于置信度反馈的模糊测试框架，利用大语言模型生成语义保持的重写，以翻转立场检测器的预测标签。该框架验证了立场模型在语义不变条件下的对抗脆弱性，但其对生成式大语言模型分析器的逃逸成功率显著低于编码器模型，且未提供针对该脆弱性的防御机制。

】

---

【CSI: An Investigative Multi-Agent Framework for Explainable Short Video Fake News Detection ｜协作式短视频调查框架

研究机构：快手

作者：Yuxin Wang、Yang Yang、Huaiwen Zhang

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_518a90dce395)

> 短视频虚假信息检测面临的核心矛盾是：多模态内容（视频、音频、文本）的复杂逻辑与现有黑盒分类器或单链推理模型的低可解释性、浅层理解之间的冲突。传统多模态小语言模型（MSLM）虽精度高但缺乏推理能力，而多模态大语言模型（MLLM）直接推理易受跨模态冲突干扰产生幻觉。本文切入点是将检测重构为“协作调查”任务，通过多智能体分工取证、结构化辩论与专用判决器实现高精度与可解释性的统一。该方法在两个真实数据集上取得SOTA性能，但其对多智能体辩论中偏差传递机制的量化评估仍存疑。

】

---

【Danger Depends on the Mind: A Theory-of-Mind Grounded Dataset and Model for Context-Dependent Dangerous Speech ｜心智理论驱动的危险言论检测

作者：Yuanchen Shi、Longyin Zhang、Guodong Zhou 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_88c1d18082e7)

> 现有危险言论检测将文本视为孤立单元，依赖二元标签，无法区分同一句话在不同说话者心理状态下截然不同的风险等级。本文切入点在于引入认知科学中的心智理论（Theory-of-Mind, ToM），将说话者的情绪、意图、行动等隐性状态作为显式上下文输入。通过构建包含79K文本-语境对的中文基准ToM-DS，并设计轻量级模型ToMGuard，利用动态注意力机制自适应加权ToM维度。该工作验证了语境依赖检测的必要性，但其合成数据主导的构建方式与单一中文场景限制了结论的普适性。

】

---

【DART: Mitigating Harm Drift in Difference-Aware LLMs via Distill-Audit-Repair Training ｜差异感知大模型中的危害漂移缓解：蒸馏-审计-修复训练

研究机构：美国埃默里大学、美国麻省理工学院

作者：Ziwen Pan、Zihan Liang、Jad Kabbara 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.16845)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_22474a9b3e09)

> 安全对齐常迫使大语言模型在需要区分群体差异的场景中保持“身份盲”，导致事实错误或过度拒绝。现有微调方法虽能提升决策准确性，却引发“危害漂移”——推理理由的有害性随准确性提升而增加，且联合优化无法兼顾两者。DART通过分阶段的蒸馏、审计与修复流程，在提升差异感知分类准确性的同时，针对性地修复了推理理由中的有害内容。该方法在Llama-3-8B上将准确率从39.0%提升至68.8%，但其在通用毒性基准上的表现混合，暴露了评估器对反话语的脆弱性。

】

---

【Debiasing LLMs by Masking Unfairness-Driving Attention Heads ｜差分激活掩码去偏

研究机构：南京大学、澳大利亚新南威尔士大学

作者：Tingxu Han、Wei Song、Ziqi Ding 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.10142)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.10142)

> 大语言模型（LLM）在直接回答模式下常输出带有社会偏见的文本，而思维链（Chain-of-Thought, CoT）提示虽能降低偏见，但其内部机制长期缺乏解释。现有去偏方法多依赖外部分类器或静态探针，无法揭示提示策略与内部组件激活之间的因果联系。本文提出DIFFHEADS，通过对比直接回答与CoT两种提示下的注意力头激活差异，定位并掩码“偏见头”，在不重训练的前提下实现去偏。该方法在两个开源模型上显著降低了不公正率，但仅验证了特定架构与提示格式，其泛化边界尚不明确。

】

---

【Deconstruct, Diagnose, and Deliberate: A Protocol-Adaptive Role-Specific Multi-Agent Framework for Fake News Detection ｜协议自适应角色专用多智能体框架

研究机构：中国科学院大学

作者：Zhigan Zhang、Jie Sui

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2c2d020ccc5e)

> 虚假新闻检测需应对事实扭曲、逻辑谬误与语境操纵的复合欺骗，但现有单链推理或固定立场对抗的多智能体框架难以解构这种多维复杂性，且易陷入认知同质性导致的回声室效应。PARD 的切入点在于将验证过程从“立场辩论”重构为“功能诊断”，通过角色分工与动态协议选择实现认知多样性。其核心做法是建立事实、逻辑、语境三维度的异构LLM团队，并引入强化学习机制自适应选择交互协议。该框架在可解释性与数据效率上表现突出，但在纯文本精度上仍落后于非生成式检索基线，其动态治理机制的实际增益边界尚存疑。

】

---

【DemMA: Dementia Multi-Turn Dialogue Agent with Expert-Guided Reasoning and Action Simulation ｜痴呆症多轮对话智能体：专家引导推理与动作模拟

研究机构：美国加州大学尔湾分校

作者：Yutong Song、Jiang Wu、Kazi Sharif 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.06373)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.06373)

> 痴呆症护理训练面临高质量交互数据稀缺与隐私限制的双重瓶颈，现有通用大语言模型（LLM）生成的对话存在人格漂移且缺乏临床特异性。DemMA 通过构建临床锚定的患者画像，引入动作标签补偿非语言信号，并利用思维链（Chain-of-Thought, CoT）蒸馏将多智能体规划内化为单模型推理，实现了高保真的亚型特异性模拟。该框架在专家评估中显著优于基线，但尚未验证合成数据对下游检测任务的实际增益。

】

---

【Detecting Hallucinations in SpeechLLMs at Inference Time Using Attention Maps ｜基于注意力图的语音大模型幻觉推理时检测

研究机构：英国爱丁堡大学

作者：Jonas Waldendorf、Bashar Awwad Shiekh Hasan、Evgenii Tsymbalov

论文原文见 [arXiv](https://arxiv.org/abs/2604.19565)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.19565)

> 语音大模型（SpeechLLM）在转录和翻译中会产生流畅但无依据的幻觉内容，现有检测手段依赖金标准输出或多次采样，成本高且无法在线部署。本文切入点在于利用模型内部注意力头在生成幻觉时表现出的特定退化模式，构建轻量级分类器。具体做法是提取四种音频特定注意力指标，训练逻辑回归模型在推理时实时判别。该方法在域内自动语音识别（ASR）任务上显著优于不确定性基线，但跨任务泛化能力极弱，其通用性存疑。

】

---

【Dialectical Structured Reasoning for Explainable Multimodal Fake News Detection ｜辩证结构化推理

研究机构：北京科技大学、新加坡管理大学

作者：Ruichao Yang、Yufan Bian、Wei Gao 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1ff708b91687)

> 多模态虚假信息检测面临的核心矛盾是：现有模型将复杂的社交证据压缩为单一向量，导致决策过程缺乏逻辑透明度，且难以处理碎片化、极化的用户反馈。现有方法要么依赖非可微的提示驱动辩论，要么仅做事后解释，无法在训练阶段优化推理路径。DSR 将检测重构为在异构传播图上的辩证裁决过程，通过可微分的 Judge 模块整合支持性与反驳性证据路径。该方法在精度与解释质量上均超越基线，但其对冻结 MLLM 背景知识的依赖在长尾事实场景下的可靠性尚存疑。

】

---

【Distilling the Essence, Discarding the Dross: Improving Fairness in Multimodal Large Language Models via Historical Reflection-Guided Prompt Optimization ｜历史反思引导提示优化

研究机构：吉林大学、南开大学

作者：Juncheng Hu、Jiming Yu、Rui Song 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f2c69ca94dc7)

> 多模态大语言模型（MLLMs）的黑盒去偏面临手工提示模板僵化且易陷入优化死循环的困境。现有静态提示无法适应复杂偏见类型，而动态优化常因遗忘有效历史路径导致性能震荡。本文提出历史反思引导提示优化框架，通过构建正负历史链对比机制，引导模型在离散提示空间中高效收敛。该方法在多数模型上将偏见分数降至近零，但缺乏与白盒内部机制干预方法的直接对比，其泛化边界尚待验证。

】

---

【Do Not Guess, Verify: Logic-Guided Adaptive Reasoning for Multimodal Misinformation Detection ｜逻辑引导自适应推理

作者：Kun Huang、Rui Qiu、Xiaoming Li 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_10185d042b45)

> 导读 多模态虚假信息检测的核心难点在于区分真实图像配虚假文本的混合来源错误，传统特征对齐方法难以捕捉语义层面的矛盾。现有基于多模态大语言模型（MLLMs）的方案虽引入世界知识，但易受无关社会线索干扰产生认知偏差，且固定深度的图推理导致简单与复杂案例计算资源分配不均。LoGAR通过VLM生成显式验证理由作为全局语义锚点，条件化多模态融合与图消息传递，并引入自适应深度控制机制。该框架在精度与效率间取得平衡，但其性能增益是否完全归因于逻辑引导机制而非骨干网络能力，仍需进一步验证。

】

---

【DR-HM: Distill-then-Reinforce Training with Cognition-Aware Data Synthesis for Harmful Meme Detection ｜认知感知数据合成与蒸馏强化训练

研究机构：美国东北大学

作者：Zihan Cheng、Jianxiang Ma、Xiaocui Yang 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c9d7c2e23e34)

> 多模态仇恨表情包检测的核心难点在于隐含语义依赖文化常识，而小模型缺乏此类知识，大模型则存在标签偏差。现有蒸馏方法因自由形式推理引入噪声，导致性能不及直接微调。本文切入点是将人类认知过程结构化为六步推理链，并引入自精炼机制校正大模型偏差。通过两阶段监督微调与自适应强化学习，使7B开源模型在FHM基准上达到84.7%准确率。该方法验证了结构化知识注入的有效性，但其静态蒸馏策略对动态新兴梗的泛化能力存疑。

】

---

【DualGuard: Dual-stream Large Language Model Watermarking Defense against Paraphrase and Spoofing Attack ｜双流自适应水印防御伪造攻击

作者：Hao Li、Yubing Ren、Yanan Cao 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.16182)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_503f104b61d0)

> 生成模型水印旨在解决AI内容版权归属与真实性验证矛盾，核心在于不可感知性与鲁棒性的平衡。现有方案为抵御改写攻击而强化信号稳定性，却导致恶意篡改文本仍被误判为模型生成，引发归因错误。本文提出DualGuard，通过语义感知的双头映射动态注入标准与对抗水印，实现伪造攻击的检测与溯源。该方法在伪造鲁棒性上显著优于基线，但纯改写场景性能略逊于SOTA，且依赖语义嵌入的准确性。

】

---

【E2E-GMNER: End-to-End Generative Grounded Multimodal Named Entity Recognition ｜端到端生成式接地多模态命名实体识别

研究机构：大连理工大学

作者：Meng Zhang、Jinzhong Ning、Xiaolong Wu 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17319)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17319)

> 接地多模态命名实体识别（Grounded Multimodal Named Entity Recognition, GMNER）旨在从图文对中同时提取文本实体、语义类型及对应的视觉区域。现有主流方法依赖独立的命名实体识别（NER）模块与对象检测器，这种解耦架构导致误差在级联过程中累积，且无法进行联合优化。本文提出 E2E-GMNER，将 GMNER 重构为单一多模态大语言模型（Multimodal Large Language Models, MLLMs）的指令微调生成任务，通过思维链（Chain-of-Thought, CoT）推理与高斯风险感知框扰动（Gaussian Risk-Aware Box Perturbation, GRBP）实现端到端联合优化。该方法在无外部知识依赖下超越了所有流水线基线，但在绝对性能上仍低于依赖重型外部检索的 SOTA 方法，其推理延迟与长尾泛化能力尚存疑。

】

---

【Efficient Hallucination Detection in Automatic Code Generation ｜代码生成中的行级幻觉检测

作者：Georgii Andriushchenko、Roman Garaev、Lyudmila Rvanova 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_973296e57410)

> 大语言模型生成的代码常出现语法正确但逻辑错误的“幻觉”，现有检测手段多停留在整段代码层面，无法定位具体错误行，阻碍了自动化调试与自我修正。本文切入点在于利用模型内部表征构建行级监督检测器，通过Diff算法自动标注训练数据，以Transformer编码器聚合Token特征至行级。该方法在多个开源代码模型上显著优于无监督基线，但其对代码风格差异的敏感性限制了泛化能力，且未验证在闭源模型上的有效性。

】

---

【EmotionTalk: An Interactive Chinese Multimodal Emotion Dataset With Rich Annotations ｜中文交互式多模态情感数据集

研究机构：南开大学、美国卡内基梅隆大学

作者：Haoqin Sun、Jinghua Zhao、Xuechen Wang 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d5a730f35333)

> 多模态情感识别（MER）长期受限于高质量自发对话数据的稀缺，尤其是中文场景下缺乏兼顾生态效度与标注精度的基准。现有中文数据集多依赖影视片段或脚本朗读，无法捕捉真实交互中的情感动态与模态冲突。本文通过19名专业演员的主题驱动即兴表演，构建了包含23.6小时数据、19,250句对话的EmotionTalk数据集，并引入细粒度情感说话风格描述。该基准填补了中文自发对话数据的空白，但其规模与演员多样性是否足以支撑大规模预训练与跨域泛化，仍存疑。

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

【Explain the Flag: Contextualizing Hate Speech Beyond Censorship ｜混合词汇库与LLM驱动的仇恨言论解释性检测

研究机构：希腊雅典国立技术大学

作者：Jason Liartis、Eirini Kaldeli、Lamprini Gyftokosta 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.14970)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1c5a99a1c85c)

> 在线平台对仇恨言论的自动化审核长期面临“黑盒判定”困境，用户无法知晓内容被移除的具体原因，导致信任缺失与申诉困难。现有基于大语言模型（LLM）的检测系统虽能捕捉深层语义，但在低资源语言中缺乏对新兴侮辱性词汇的显式知识，且解释往往脱离具体语境。本文提出一种混合架构，通过构建英、法、希腊三语专用词汇库作为外部接地资源，结合双管道LLM推理，实现仇恨言论的精准检测与语境化解释。该方案在自建多语言基准上优于纯LLM基线，但其对词汇库覆盖率的依赖及希腊语性能衰减机制尚存疑。

】

---

【Fairness Evaluation and Inference Level Mitigation in LLMs ｜动态神经元抑制

研究机构：澳大利亚麦考瑞大学

作者：Afrozah Nadeem、Mark Dras、Usman Naseem

论文原文见 [arXiv](https://arxiv.org/abs/2510.18914)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.18914)

> 多轮对话中，LLM的偏见并非静态存在，而是随上下文累积与记忆携带动态演化，现有静态剪枝或推理时干预方法无法区分“当前轮次的局部偏见”与“历史轮次的记忆偏见”，导致过度抑制或漏检。本文切入点在于将偏见视为动态累积过程，通过记忆一致性探针与自适应门控机制，在推理时实时、可逆地调节特定神经元的影响。该方法在多语言多轮对话中显著降低偏见分数，同时保持语义连贯性，但其效果依赖于归因精度与探针阈值，对长程依赖的捕捉能力尚存疑。

】

---

【FaithLens: Detecting and Explaining Faithfulness Hallucination ｜FaithLens：基于规则强化学习的忠实性幻觉可解释检测

研究机构：清华大学、复旦大学

作者：Shuzheng Si、Qingyi Wang、Haozhe Zhao 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.20182)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.20182)

> 导读 忠实性幻觉指模型生成内容与给定上下文文档不一致，是检索增强生成（RAG）等应用的核心风险。现有检测方案要么依赖高成本大模型进行黑盒判断，要么训练专用小模型但仅输出二分类标签，缺乏可解释性且跨任务泛化能力不足。本文提出 FaithLens，通过合成数据过滤、监督微调（SFT）冷启动及基于规则强化学习（RL）的两阶段训练，使 8B 参数模型在检测精度的同时生成高可信度解释。该方法在 12 个任务上超越了 GPT-5.2 等前沿大模型，但其解释质量评估依赖特定新手模型，且未与白盒内部表征探测方法直接对比，其通用性边界尚存疑问。

】

---

【FigSIM: A Dataset for Fine-grained Suicide Severity and Figurative Language in Suicide Memes ｜自杀表情包细粒度风险分级与修辞干扰分析

研究机构：澳大利亚墨尔本大学

作者：Liuliu Chen、Elise R. Carrotte、Brian E. Chapman 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.02523)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.02523)

> 自杀表情包检测旨在从图文交互中识别隐含的自杀风险等级，其核心难点在于幽默修辞与临床风险信号的纠缠，导致传统二元分类无法支撑精准干预。现有通用仇恨检测模型在自杀垂直领域面临严重度低估与修辞误判瓶颈，本文切入点在于构建首个基于临床量表的多标签自杀表情包基准。通过整合修辞现象、自杀严重度及内容类型标注，并评测16种单模态与多模态模型，揭示了修辞对风险识别的系统性干扰。该工作确立了自杀表情包检测的性能下限，但数据源单一性与标注主观性限制了其泛化边界。

】

---

【Fine-tuning with Hierarchical Prompting for Robust Propaganda Classification Across Annotation Schemas ｜意图导向宣传分类与分层提示鲁棒性

研究机构：德国柏林工业大学、德国人工智能研究中心

作者：Lukas Stähelin、Veronika Solopova、Max Upravitelev 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4f43d6bc7476)

> 短文本宣传检测面临标注主观性强与模型对表面词汇过度敏感的困境，现有基于修辞技巧的分类体系因标注者分歧大导致模型学习信号噪声高。本文切入点在于将分类目标从“使用了什么修辞手法”转向“试图达成什么沟通意图”，并验证分层提示策略在低标注一致性条件下的鲁棒性。通过构建意图导向的新分类体系并对比微调前后的分层推理效果，证明了微调是激活层级结构收益的必要条件。该工作揭示了标注可靠性与提示策略的交互效应，但其新体系较低的标注一致性是否真正优于传统体系，仍取决于具体应用场景对解释深度的需求。

】

---

【GigaCheck: Detecting LLM-generated Content via Object-Centric Span Localization ｜基于对象检测范式的LLM生成文本跨度定位

作者：Irina Tolstykh、Aleksandra Tsybina、Sergey Yakubson 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2410.23728)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_5474e7dbf1d3)

> 人机协作文本中AI片段的精确边界识别是现有文档级检测器无法解决的痛点，传统序列标注方法依赖繁琐的后处理且对句子结构敏感。GigaCheck将文本跨度检测重构为一维目标检测问题，利用DETR架构直接回归字符区间，消除了对句子边界的依赖。该方法通过共享LoRA微调骨干同时支持细粒度定位与文档级分类，在三个定位基准上显著优于基线，但其对多语言及极端长文本的适用性仍存疑。

】

---

【Hallucinations as Orthogonal Noise: Inference-Time Manifold Alignment via Dynamic Contextual Orthogonalization ｜动态上下文正交化（DCO）：基于几何对齐的推理时幻觉抑制

研究机构：中国科学技术大学、清华大学

作者：Mingkuan Zhao、Wentao Hu、Tianchen Huang 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.03022)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.03022)

> 大语言模型在生成过程中常因内部表征偏离上下文事实而产生幻觉，现有解码干预方法多依赖静态向量或Logit层对比，难以区分必要的语义多样化与有害噪声，导致在提升忠实性的同时损害参数知识检索能力。本文基于线性表示假设，将幻觉形式化为残差流中偏离上下文流形的正交噪声，提出动态上下文正交化（Dynamic Contextual Orthogonalization, DCO）方法，通过逐层Z-Score动态门控机制选择性衰减异常正交分量。该方法在Llama-3系列模型上实现了上下文忠实性与知识保留的帕累托优化，但其对纯参数知识检索场景下正交性定义的适用性仍存疑。

】

---

【Hard to Be Heard: Phoneme-Level ASR Analysis of Phonologically Complex, Low-Resource Endangered Languages ｜极端音系低资源语言的音素级识别分析

研究机构：德国图宾根大学

作者：V.S.D.S.Mahesh Akavarapu、Michael Daniel、Gerhard Jäger

论文原文见 [arXiv](https://arxiv.org/abs/2604.18204)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_adc95ab6e412)

> 东高加索语言如Archi拥有73至81个辅音音位，其音系复杂度远超常规低资源语言，导致现有自动语音识别（ASR）系统无法区分错误源于内在音系难度还是数据稀缺。通用多语言模型在缺乏针对性适配时，对这类极端音系结构的泛化能力存在盲区，且传统词错误率（WER）指标掩盖了音素层面的系统性偏差。本文通过构建标准化语料并引入语言特定音素词表与启发式初始化，揭示了音素识别准确率随训练频率呈Sigmoid增长的规律。该研究验证了数据稀缺主导错误模式的核心假设，但受限于极小样本规模，其结论在更大规模数据下的普适性尚存疑。

】

---

【HCFD: A Benchmark for Audio Deepfake Detection in Healthcare ｜病理语音下的编解码器伪造检测

作者：Mohd Mujtaba Akhtar、Girish、Muskaan Singh

论文原文见 [arXiv](https://arxiv.org/abs/2604.17642)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17642)

> 医疗场景中的语音既是临床信号也是身份凭证，但现有音频深伪检测器在健康语音上训练，面对病理语音时性能骤降。本文指出病理变异会掩盖编解码器伪迹，导致传统模型失效，并构建首个病理感知基准 HCFK。通过引入超球面几何原型聚类与 Mamba 时序建模，PHOENIX-Mamba 实现了跨临床条件的鲁棒检测。该方法在特定域内有效，但缺乏与通用深伪 SOTA 的直接对比，其泛化边界尚待验证。

】

---

【HiCoLoRA: Addressing Context-Prompt Misalignment via Hierarchical Collaborative LoRA for Zero-Shot DST ｜层级协作低秩适配

研究机构：上海交通大学、北京航空航天大学

作者：Shuyu Zhang、Yifan Wei、Xinru Wang 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.19742)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.19742)

> 零样本对话状态追踪（zs-DST）旨在让任务导向对话系统无需目标域标注数据即可泛化至新领域，其核心障碍在于动态对话上下文与静态槽位提示间的语义错位。现有参数高效微调方法（如DualLoRA）统一处理Transformer各层，忽视了低层捕获局部语义原子、高层整合全局意图的层级特性，导致跨域干扰与灾难性遗忘。HiCoLoRA通过层级协作架构、谱聚类解耦及语义增强SVD初始化，在MultiWOZ和SGD上实现了零样本JGA的显著提升。该框架在PEFT范式下有效缓解了上下文-提示错位，但其性能仍低于依赖合成数据的SOTA方法，且对高特异性槽域的处理能力有限。

】

---

【ICLAD: In-Context Learning with Comparison-Guidance for Audio Deepfake Detection ｜上下文学习与对比引导的音频深伪检测

研究机构：美国普渡大学

作者：Benjamin Chou、Yi Zhu、Surya Koppisetti

论文原文见 [arXiv](https://arxiv.org/abs/2604.16749)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.16749)

> 音频深度伪造检测（ADD）的核心困境在于专用检测器在受控录音室数据上性能饱和，却难以泛化至充满噪声与信道失真的野外场景。现有基于自监督学习（SSL）微调的方案虽在封闭集表现优异，但面对分布偏移时性能骤降，且缺乏可解释性。本文提出 ICLAD，一种免训练的音频大语言模型（ALM）检测框架，通过成对对比推理（PCR）策略引导模型自我发现判别性声学特征，并结合动态路由机制处理分布外样本。该框架在野外数据集上显著提升了宏 F1 分数并提供了文本解释，但在录音室数据上仍逊于专用检测器，其泛化边界与计算成本仍是主要制约。

】

---

【Iterative Self-Correction for Text-Driven Person Re-Identification with Large Vision-Language Models ｜自主闭环迭代修正的视觉语言模型行人重识别

研究机构：浙江大学、新加坡国立大学

作者：Guijin Luo、Zequn Xie、Sihang Cai 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_7bd4fc5dea5b)

> 行人重识别（ReID）旨在跨摄像头匹配同一身份，但现有基于视觉语言模型（VLM）的方法多采用单次编码-匹配范式，导致初始描述错误无法修正且细粒度特征丢失。本文提出 Auto-ReID，将 ReID 重构为“思考-精炼”的迭代闭环，通过分层渐进微调赋予 VLM 属性推理与纠错能力。该方法在遮挡与换装场景下显著优于静态基线，但其性能增益高度依赖迭代深度与候选集规模，且未验证在大规模开放世界中的泛化边界。

】

---

【KnowDR-REC: Auditing Knowledge-Conditioned Visual Grounding in Referring Expression Comprehension ｜知识条件指代表达理解的诊断基准

研究机构：山东大学、南方科技大学

作者：Guanghao Jin、Jingpei Wu、Tianpei Guo 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e2db8e4da937)

> 指代表达理解（REC）旨在通过自然语言定位图像目标，但现有基准多依赖图像内视觉线索，掩盖了模型在外部知识推理上的缺陷。当前多模态大语言模型（MLLMs）在标准测试集上表现优异，却难以处理涉及事实、时间或关系的外部知识查询，导致“高定位精度”与“低语义理解”并存的悖论。本文提出 KnowDR-REC，一个基于反事实扰动的诊断基准，通过解耦文本推理、视觉定位与拒绝决策，审计 MLLMs 的真实能力。该工作揭示了模型依赖视觉捷径而非逻辑推理的“捷径绑定”现象，但受限于仅覆盖人物实体与英文数据，其结论向非人物对象或跨语言场景的泛化性仍存疑。

】

---

【Leveraging Human and Machine Preferences for Zero-shot Detection of AI-Generated Text ｜人机预测差异适配器

研究机构：中国科学院大学、中国科学院

作者：Lei Jiang、Desheng Wu、Xiaolong Zheng 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_3098a836ff0d)

> 零样本AI生成文本检测长期受困于“机器中心”视角，即仅依赖单一代理模型计算token似然并简单平均，导致在高质量生成文本面前区分度不足。现有方法忽略了人类与机器在同一文本上预测分布的结构性差异，而这一差异恰恰蕴含了作者身份的互信息。HAPDA通过联合微调一对偏好模型，将人机预测分歧转化为token级权重，对MeanZero类检测器进行校准。该方法在RAID基准上显著提升了基线性能，但其对微调数据分布的隐性依赖及双模型推理开销，限制了其在开放环境中的泛化潜力。

】

---

【Lost in Diffusion: Uncovering Hallucination Patterns and Failure Modes in Diffusion Large Language Models ｜扩散大语言模型幻觉模式与失败机制

作者：Zhengnan Guo、Fei Tan

论文原文见 [arXiv](https://arxiv.org/abs/2604.10556)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_97f0c0e1abba)

> 扩散大语言模型（dLLM）作为非自回归生成范式，其双向可见性理论上应缓解幻觉，但实际可靠性未知。现有研究聚焦于自回归模型（AR-LLM）的幻觉检测，缺乏对dLLM生成机制特异性失效模式的系统量化。本文通过受控对比实验，揭示dLLM在知识召回、长文本一致性及边界识别上的系统性缺陷，并归因于去噪动态中的结构刚性。该研究填补了非自回归范式下的可靠性评估空白，但受限于预训练权重差异，无法完全隔离生成范式与参数知识的贡献。

】

---

【LR-DWM: Efficient Watermarking for Diffusion Language Models ｜双向局部约束的扩散语言模型水印

研究机构：以色列巴伊兰大学

作者：Ofek Raban、Gal Chechik、Ethan Fetaya

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b0476c5350ec)

> 扩散语言模型（DLMs）的非顺序生成特性导致依赖左侧上下文的自回归水印范式失效，现有适配方案或需高计算开销的期望计算，或需$|V|^2$内存的查表机制。LR-DWM通过独立利用左右邻居的局部哈希约束，以加性logits偏置实现顺序无关的水印嵌入，在保持检测率的同时将计算与内存开销降至接近无水印基线。该方案解决了DLM水印的效率瓶颈，但其对语义级对抗攻击的鲁棒性未在实验中验证，且未报告具体TPR数值，仅通过困惑度间接反映检测能力。

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

【Measuring Watermarking under Jailbreaking: ASR Inflation and Goal-Compliance Mismatch ｜水印解码扰动下的安全对齐解耦：ASR与目标合规的背离

作者：Sungwoo Han、Sangjun Moon、Jingun Kwon 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_fa9a5e943ff7)

> 生成式AI水印旨在解决内容溯源与版权保护问题，但现有研究多聚焦于水印检测率与鲁棒性，忽视了水印嵌入对模型安全对齐的潜在干扰。当水印解码逻辑与越狱攻击交互时，自动评估指标（ASR）可能因拒绝标记的抑制而虚高，导致对模型安全性的误判。本文通过引入目标合规度量（StrongREJECT）与人工评估，系统量化了六类水印方法在三种越狱设置下的ASR-SR背离现象。该研究揭示了单一ASR指标在对抗场景下的脆弱性，但其结论局限于特定模型与攻击组合，未涵盖水印感知攻击者。

】

---

【Memory-Guided Hard Data Augmentation for Multimodal Named Entity Recognition ｜记忆引导的硬数据增强

研究机构：东华大学、复旦大学

作者：Xinyu Liu、Kai fu、Yinghan Shi 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_cd5277b2a723)

> 多模态命名实体识别（Multimodal Named Entity Recognition, MNER）面临数据稀缺与模型架构特异性盲点的双重制约，现有通用数据增强方法因忽略模型内部状态而难以系统性修复复杂缺陷。本文切入点在于将数据增强从“无状态随机扰动”转变为“模型感知的逻辑修复”，通过构建记忆树归纳宏观错误模式来指导针对性合成。该框架在Twitter基准上验证了模型感知增强的有效性，但其对特定架构盲点的依赖性及离线计算成本限制了其通用性。

】

---

【Model-Agnostic Meta Learning for Class Imbalance Adaptation ｜难度感知元重采样

作者：Hanshu Rao、Guangzeng Han、Xiaolei Huang

论文原文见 [arXiv](https://arxiv.org/abs/2604.18759)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_54486ed748a1)

> 类别不平衡导致模型偏向多数类，而静态重加权或固定重采样无法适应训练过程中样本难度的动态变化。HAMR通过双层元学习框架，将实例难度量化与语义邻域重采样解耦，动态调整训练分布。该方法在六个NLP基准上验证了动态机制对稀疏类别的增益，但其收益是否源于邻域结构本身而非元学习闭环，仍需更严格的消融验证。

】

---

【More Than Sum of Its Parts: Deciphering Intent Shifts in Multimodal Hate Speech Detection ｜分层多模态交互与法庭辩论框架

研究机构：清华大学

作者：Runze Sun、Yu Zheng、Zexuan Xiong 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.21298)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.21298)

> 多模态仇恨检测的核心难点在于仇恨意图常由看似无害的图文组合通过隐喻或讽刺隐含生成，单一模态特征无法独立承载完整语义。现有方法多依赖静态特征融合或对称式多智能体投票，难以捕捉模态间的动态语义冲突与语境反转，导致在隐含仇恨样本上误判率高。本文通过构建分层多模态交互（Stratified Multimodal Interaction, SMI）范式明确意图转移机制，并提出非对称法庭辩论框架（ARCADE）强制模型进行对抗性推理。该工作提升了隐含样本的检测精度与解释性，但在绝对精度上仍低于部分强骨干基线，且未量化计算成本。

】

---

【Multi-Scale Spectral Selection and Entropy-Guided Uncertainty Fusion for Multimodal Rumor Detection ｜多尺度谱选择与熵引导不确定性融合的多模态谣言检测

研究机构：中国科学院大学、中国科学技术大学

作者：Zongliang Han、Wenyu Guo、Guoqing Jin 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8447b459aa69)

> 多模态谣言检测面临空间域特征噪声大与跨模态语义不一致的双重挑战，现有频域方法仅做简单变换而缺乏细粒度筛选。MS-SFM通过离散余弦变换将图文特征映射至频域，利用多尺度卷积与挤压-激励机制过滤噪声，并基于熵值动态融合共享与私有特征。该方法在Weibo等数据集上取得领先性能，但其依赖固定阈值与内部特征，未涉及外部证据检索，在开放域事实核查中的泛化能力存疑。

】

---

【Multimodal In-context Learning for ASR of Low-resource Languages ｜多模态上下文学习驱动的低资源语音识别

研究机构：德国卡尔斯鲁厄理工学院

作者：Zhaolin Li、Jan Niehues

论文原文见 [arXiv](https://arxiv.org/abs/2601.05707)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.05707)

> 低资源语音识别（ASR）长期受困于标注数据稀缺，传统自监督预训练与微调范式在极端低资源场景下泛化能力受限。本文切入点在于利用语音大语言模型（Speech LLM）的多模态上下文学习（MICL）能力，在推理时通过提示工程动态适配未见语言，而非依赖参数更新。具体做法是结合声学模型生成假设，并利用语音 LLM 进行基于 MICL 的重排序。该架构在三种濒危语言上验证了跨语言迁移的有效性，但其性能提升是否主要源于声学模型 N-best 列表的质量，而非 LLM 的深层语义理解，仍存疑。

】

---

【Penetrating Linguistic Disguises: A Slang-aware Label-Aligned Framework for Fine-Grained Toxicity Extraction in Chinese Hate Speech Detection ｜结构感知标签对齐框架

研究机构：同济大学、中国科学院

作者：Wei Liu、Xiaoliang Chen、Duoqian Miao 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a6400e62e918)

> 中文社交媒体中广泛存在的拼音缩写与同音字伪装，使得基于关键词的传统毒性检测失效，而生成式大语言模型虽具备语义理解能力，却在严格的跨度边界匹配上频繁出现漂移与幻觉。现有判别式网格标记方法虽能保持边界敏感性，但无法处理同一目标-论证对同时涉及性别歧视与种族歧视等多标签冲突的场景。SLAF通过结构-语义词典融合模块解析伪装语义，并利用标签解耦体积标记将二维网格扩展至三维空间以分离重叠类别，在STATE ToxiCN基准上实现了30.09%的Hard-F1，较最佳微调LLM基线提升5.82%。该框架验证了判别式结构化提取在精确匹配任务上的优势，但其对词典覆盖率的依赖及未对比其他判别式基线的情况，限制了其泛化能力的评估。

】

---

【POLAR: A Benchmark for Multilingual, Multicultural, and Multi-Event Online Polarization ｜多语言极化检测基准

研究机构：澳大利亚麦考瑞大学、阿联酋扎耶德大学

作者：Usman Naseem、Robert Geislinger、Juan Ren 等 43 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0be1e9c769cb)

> 在线极化检测旨在识别文本中群体间对抗的修辞表现，但现有研究局限于单一语言或特定事件，无法反映全球数字话语的多样性。主流模型在低资源语言上泛化能力崩塌，且缺乏对极化类型与修辞表现的细粒度区分。本文构建了覆盖22种语言、11万实例的多文化极化数据集，并系统评估了小型与大型语言模型在零样本及少样本下的表现。该基准揭示了资源层级对模型性能的决定性影响，但标注一致性的文化依赖性仍制约着跨语言结论的普适性。

】

---

【Position: LLM Watermarking Should Align Stakeholders’ Incentives for Practical Adoption ｜利益相关者激励对齐的大语言模型水印部署框架

作者：Yepeng Liu、Xuandong Zhao、Dawn Song 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0bda31dc58ae)

> 生成模型水印旨在解决生成式AI内容在版权归属与真实性验证上的核心矛盾，其技术演进本质是在不可感知性与鲁棒性之间寻找平衡。现有算法在检测率与鲁棒性上已趋近理论极限，但实际部署率极低，根源在于提供商、平台与用户间的激励错位。本文提出以“激励对齐”为核心约束，重新评估模型水印、文本水印与上下文水印的适用场景。该立场论文揭示了技术性能与商业生态的脱节，但缺乏量化验证，其提出的上下文水印范式尚处于概念阶段。

】

---

【PretrainRL: Alleviating Factuality Hallucination of Large Language Models at the Beginning ｜预训练强化学习

作者：Langming Liu、Kangtao Lv、Haibin Chen 等 11 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8de86936e7af)

> 大语言模型在生成流畅文本时频繁产生事实性错误，即幻觉，这严重阻碍了其在医疗、法律等高风险领域的可靠部署。现有方案多依赖外部知识库核查或多次采样一致性验证，思路直观但受限于高昂的计算成本与有限的知识覆盖范围；当高置信度幻觉暴露出传统概率信号的失效后，研究范式发生关键转折，从黑盒外部验证转向白盒内部表征探测，利用隐藏状态中的可解码信号实现实时检测。本文指出事实性幻觉的根源在于预训练语料分布失衡导致的“低概率真值”与“高概率假值”共存，提出在预训练阶段引入直接偏好优化以重塑概率分布，通过“去偏然后学习”原则为真值腾出记忆空间。该框架在 PopQA 等基准上显著提升了准确率，但其效果是否伴随通用语言能力的退化，以及负采样策略在极端长尾知识下的鲁棒性，仍存疑。

】

---

【PROBE: PROcess-Based BEnchmark for Hallucination Detection ｜过程式幻觉检测基准

研究机构：香港中文大学

作者：Yu Zhang、Peter Belcak、Shizhe Diao 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1c0f2d9c7be0)

> 现有幻觉检测基准仅输出“是否包含幻觉”的二元结果，无法诊断模型在长文本中具体哪一步推理失效。本文切入点在于将检测解耦为声明分解、证据查找、证据评估与定位四个独立认知阶段，构建首个过程式评测框架。通过合成注入幻觉的维基百科语料，PROBE 揭示了证据查找是主要性能瓶颈，且过程式评估的召回率显著高于一步式提示。该工作确立了细粒度诊断的评测新范式，但其黑盒多步推理的高延迟限制了实时部署，且未与白盒内部表征方法直接对比。

】

---

【Probing Multimodal Large Language Models on Cognitive Biases in Chinese Short-Video Misinformation ｜短视频谣言检测中的认知偏差诊断

研究机构：美国约翰斯·霍普金斯大学、香港中文大学

作者：Jen-tse Huang、Chang Chen、Shiyang Lai 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.06600)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ad54e29d1a2b)

> 短视频谣言检测旨在从视听混合内容中识别逻辑谬误与虚假声明，但现有基准多依赖外部事实核查，难以评估模型对内部逻辑链的推理能力。当前多模态大语言模型（MLLMs）虽具备基础推理能力，却在真实社交噪声下表现出系统性判断偏差，且缺乏针对认知偏差的量化评估框架。本文通过构建200条人工标注的短视频数据集，引入心理学控制变量，系统诊断了8个前沿MLLMs在权威ID与流行度指标下的行为失效。该工作提供了诊断MLLMs认知脆弱性的新视角，但其评测规模与指标设计限制了向实际部署场景的直接迁移。

】

---

【Prompting Across Time: Evaluating LLMs on Historical and Contemporary Offensive Language ｜跨时代仇恨言论检测中的提示工程归因分析

作者：Sanne Hoeken、Sophie Jasmin Spliethoff、Silke Schwandt 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_19e5046672fe)

> 导读 仇恨言论检测（HSD）长期局限于当代社交媒体语料，忽视了语言攻击性在历史文本中的演变与形态差异，导致模型在跨时代场景下的泛化能力缺乏实证依据。现有方法多依赖微调或解码干预，难以量化提示设计中各组件对历史语境理解的独立贡献，且缺乏对早期现代英语（EModE）这一低资源、高语境依赖领域的系统性评估。本文通过模块化提示设计，量化定义丰富度、上下文、规则与示例对LLM在EModE及现代文本上检测性能的边际贡献，揭示了标注清晰度对性能的压倒性影响。该研究填补了历史NLP与HSD交叉领域的空白，但零样本设定下的性能上限及提示脆弱性限制了其直接部署价值。

】

---

【PUMA: Projected Universal Multilingual ASR for Low-Resource Settings. Application to Diverse African Languages ｜通用语言投影多语言语音识别

研究机构：法国国家科学研究中心

作者：Ilyes Oukid、Bilal Faye、Hanane Azzag 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b1a315d6aa26)

> 低资源多语言语音识别（LR-ML-ASR）面临的核心矛盾是语言多样性与计算资源有限性之间的结构性冲突，现有基于适配器的多语言模型在扩展新语言时参数呈线性增长，阻碍了边缘部署与长尾语言覆盖。PUMA 通过引入通用语言投影（ULP）模块，以单一可学习语言令牌替代语言特定适配器，在保持全参数共享的同时实现语言感知。该架构在 10 种非洲低资源语言上以约 30M 可训练参数超越了 1B 参数的 MMS 基线，但其性能优势是否源于架构创新还是数据特性，以及其在形态更复杂语言上的泛化能力，仍存疑。

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

【ReCoT-NER: Enhancing Zero-Shot Named Entity Recognition through Chain-of-Thought Prompting and Recall-Oriented Loss Optimization ｜链式思维提示与召回导向损失增强零样本命名实体识别

研究机构：美国麻省理工学院

作者：Dabin Fu、Fanghong Zhang

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9da604b28764)

> 零样本命名实体识别（Zero-Shot Named Entity Recognition, ZS-NER）旨在无标注数据条件下识别开放集实体，但生成式模型常因解码偏差导致实体漏检与边界模糊。现有指令微调方法多采用单步生成，隐式耦合跨度检测与类型分类，加剧了模型对稀疏实体信号的忽略。本文提出ReCoT-NER，通过链式思维（Chain-of-Thought, CoT）提示显式分解推理步骤，并设计召回导向损失（Recall-Oriented Loss, RCLoss）强化边界起始信号。该方法在77M参数模型上实现了跨域泛化提升，但其性能上限受限于小模型容量，且未验证与动态指令优化方法的直接对比。

】

---

【Rethinking LLM Watermark Detection in Black-Box Settings: A Non-Intrusive Third-Party Framework ｜黑盒第三方大语言模型水印检测框架

研究机构：中国科学院、中国科学院大学

作者：Zhuoshang Wang、Yubing Ren、Yanan Cao 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.14968)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f294926fe4a7)

> 现有大语言模型水印方案将检测逻辑与注入密钥强耦合，导致独立审计机构无法在不泄露密钥的前提下验证内容来源，阻碍了司法与监管场景的应用。本文提出TTP-Detect，通过解耦检测与注入，将验证重构为相对假设检验问题。该方法利用代理模型提取表征，结合局部一致性、全局几何与自适应秩测试等多维相对测量，实现密钥无关的黑盒检测。该框架在多种水印方案上实现了接近白盒SOTA的检测性能，但其对无偏水印方案的检测率显著下降，暴露了统计信号弱化下的检测瓶颈。

】

---

【RTCFake: Speech Deepfake Detection in Real-Time Communication ｜实时通信场景下的语音深伪检测与音素一致性学习

研究机构：武汉大学、安徽大学

作者：Jun Xue、Zhuolin Yi、Yihuan Huang 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.23742)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_436e93849118)

> 实时通信（RTC）中的黑盒传输处理会系统性抹除合成语音的帧级伪迹，导致离线训练的检测器在真实通话中失效。现有基准仅模拟单一信道或噪声，无法复现RTC中噪声抑制、回声消除与编解码耦合的非线性失真。本文通过构建首个大规模RTC配对数据集RTCFake，并提出音素引导一致性学习（PCL）策略，强制模型在离线与在线场景间保持音素级表征不变。该工作填补了真实通信环境评估的空白，但其泛化能力是否超越通用域适应方法仍存疑。

】

---

【SAM-NER: Semantic Archetype Mediation for Zero-Shot Named Entity Recognition ｜语义原型中介的零样本命名实体识别

作者：Ruichu Cai、Juntao Gan、Miao Mai 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.03706)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.03706)

> 零样本命名实体识别（Zero-shot NER, ZS-NER）旨在无目标域监督下识别新领域实体，但大语言模型（LLM）的内在语义与细粒度目标标签常错位，导致系统性语义漂移。现有指令微调与检索增强方法分别受限于语义对齐假设失效与外部知识覆盖不足，难以在异构标签体系下稳定泛化。SAM-NER 通过引入领域不变的“语义原型”中间层，将实体发现、抽象中介与定义校准解耦为三阶段流程，以稳定跨域推理。该方法在 CrossNER 基准上取得 66.3 的平均 F1，验证了中介范式的有效性，但其对固定原型空间的依赖及在语义距离较近类型上的性能衰减，仍构成泛化边界。

】

---

【Scaling Performance and Low-Resource Annotation with Many-Shot In-Context Learning for Named Entity Recognition ｜多示例上下文学习驱动的低资源实体识别标注

作者：Qi Zhang、Fangping Lan、Cornelia Caragea 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.21890)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.21890)

> 导读 低资源命名实体识别（Named Entity Recognition, NER）面临标注数据稀缺与领域术语专业性强导致的模型泛化失效问题。现有方法或依赖大规模人工标注训练小型模型，或直接用大语言模型（Large Language Models, LLMs）进行少样本推理，但后者在结构化任务上精度不足且推理成本高。本文切入点在于将LLM从“推理器”转变为“标注器”，利用多示例上下文学习（In-Context Learning, ICL）生成高质量训练数据以微调轻量级模型。通过构建包含置信度筛选与错误感知修正的框架，该方法在低资源基准上显著提升了下游模型性能，但其在非拉丁脚本语言及多模态场景下的适用性仍存疑。

】

---

【Self-Explaining Hate Speech Detection with Moral Rationales ｜道德理由监督注意力

研究机构：智利大学、美国南加州大学

作者：Francielle Vargas、Jackson Trager、Diego Alves 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_69471981d99e)

> 仇恨言论检测模型长期依赖表层词汇特征，导致在讽刺、隐喻等隐式表达及跨文化语境下误报率高且缺乏可解释性。现有事后解释方法（如LIME、SHAP）计算昂贵且与模型决策过程脱节，而基于仇恨理由的注意力对齐方法（SRA）受限于词汇层面的理由，难以捕捉深层道德推理。本文提出监督道德理由注意力（SMRA），将道德基础理论（MFT）标注的道德理由掩码直接作为注意力监督信号嵌入训练目标，实现内在可解释性。该方法在巴西葡萄牙语数据集上显著提升了解释忠实度与合理性，但预测性能提升微弱，且未验证跨语言泛化能力。

】

---

【SLIM: Stealthy Low-Coverage Black-Box Watermarking via Latent-Space Confusion Zones ｜潜空间混淆区数据水印

作者：Hengyu WU、Yang Cao

论文原文见 [arXiv](https://arxiv.org/abs/2601.03242)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_dc5dfb4d1bfe)

> 训练数据水印旨在解决个体数据贡献者在大规模语料库中无法验证其数据是否被模型训练使用的问题。现有放射性水印方法需修改大量数据且易受攻击，而显式注入方法缺乏隐蔽性，导致在超低覆盖率场景下失效。SLIM通过前缀重述与发散续写构造潜空间混淆区，利用生成不稳定性进行黑盒假设检验。该框架在仅修改单条序列时实现了可靠溯源，但其检测信号随数据规模扩大而稀释，且对模型参数量的依赖尚未完全量化。

】

---

【Speak No Evil, Just Prompt: Low-resource Multilingual Toxic Speech Detection with Audio Language Model ｜多语言毒性语音检测的软提示适配

研究机构：天津大学、深圳大学

作者：Mingzi Zuo、Lei Zhang、Hailiang Sun 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_87751ac7b9ae)

> 现有毒性语音检测依赖ASR转录，在低资源语言与复杂口音下因转录错误导致声学线索丢失，且端到端模型难以平衡跨语言泛化与特定语言适配。本文构建覆盖53种语言及口音的PolySpeechTox数据集，并提出SoftPrompt-TSD框架，通过分解式软提示在冻结音频语言模型上实现参数高效适配。该方法在微平均ROC-AUC上达到98.07%，显著优于基线，但其性能高度依赖已知语言标签，对未知口音的泛化能力存疑。

】

---

【StanceAttack: Adversarial Attack for Stance Detection ｜立场检测中的对抗攻击：StanceAttack

作者：Chenye Zhao、Cornelia Caragea

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_88494ce3e748)

> 立场检测模型在真实政治舆论场景中面临被恶意篡改的风险，现有研究多关注分类精度而忽视模型对语义保持型扰动的脆弱性。传统词级替换攻击难以生成自然且语义一致的对抗样本，导致攻击成功率低或文本可读性差。本文提出 StanceAttack，利用 ChatGPT 结合思维链（Chain-of-Thought, CoT）提示与决策反馈机制，生成能欺骗预训练语言模型（Pretrained Language Models, PLMs）的立场翻转样本。该方法在效率与成功率上优于基线，但仅针对黑盒 PLM 且排除中立类，其鲁棒性边界尚待验证。

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

【ToxiTrace: Gradient-Aligned Training for Explainable Chinese Toxicity Detection ｜中文毒性内容检测中的梯度对齐跨度提取

研究机构：华东师范大学

作者：Boyang Li、Hongzhe Shou、Yuanyuan Liang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.12321)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a036e9981b4d)

> 中文毒性检测长期困于句级分类与细粒度证据定位的割裂：编码器模型分类高效但归因碎片化，大语言模型（LLM）能提取连贯跨度却推理成本高昂且分类性能不稳定。ToxiTrace 抓住中文字符级分词导致梯度信号分散这一被忽略的技术痛点，通过训练时梯度约束与对抗推理对比学习重塑编码器内部敏感度分布，使后验归因直接输出人类可读的连续毒性跨度。该方法在保持编码器推理效率（约2分钟）的同时，跨度提取F1达77.90%，接近LLM水平，但其弱监督标注依赖外部LLM，且未验证对抗鲁棒性。

】

---

【TRUST: Towards Robust Social Bot Detection via Uncertainty-Guided Pseudo-Labeling and Graph Structure Purification ｜基于不确定性引导的图结构净化社交机器人检测

研究机构：南开大学、天津大学

作者：Ruixuan Xu、Mengting Hu、Zhunheng Wang 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e0ab7cbf37ce)

> 社交机器人通过构建异质性社交连接伪装成人类，导致图神经网络在消息传递阶段接收错误标签信息，进而产生误分类。现有方法依赖同质性假设，无法区分高置信节点与低置信节点，缺乏对欺骗性连接的主动干预机制。TRUST框架通过证据深度学习量化节点级不确定性，动态生成伪标签并移除冲突边，实现图结构净化。该方法作为通用插件在多种骨干网络上稳定提升性能，但其有效性高度依赖验证集阈值搜索的准确性，且未验证在动态演化图结构下的鲁棒性。

】

---

【WaveDetect: Robust Framework for Machine-Generated Text Detection via Wavelet Transform ｜基于连续小波变换的机器生成文本检测

研究机构：南方科技大学

作者：Zhichen Liu、Kaitong Qin、Linhan He 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_695a37543776)

> 机器生成文本检测旨在区分人类写作与大语言模型（LLM）生成内容，核心挑战在于生成模型能力指数级提升导致人机文本分布边界日益模糊。现有零样本统计方法依赖困惑度等静态特征，在对抗攻击与模型演化下脆弱；监督方法虽精度高但跨域泛化差。WAVEDETECT 将 token 概率序列视为信号，通过连续小波变换（CWT）提取时频域“频谱指纹”，以 CNN 分类器实现鲁棒检测。该方法在 RAID 基准上取得 0.9785 平均 AUROC，显著优于基线，但其对语义不变攻击的鲁棒性边界尚待更严苛协议验证。

】

---

【When depth is redundant: Efficient transformer-based speech anti-spoofing ｜浅层对齐Transformer反欺骗检测

研究机构：法国国家科学研究中心

作者：Hoan My Tran、Damien Lolive、Aghilas Sini 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_45bfd653a2df)

> 反欺骗检测的核心痛点在于深层Transformer分类器在域外场景下泛化能力不足，且计算开销随深度增加呈二次方增长。现有方法通过增加模型深度或引入复杂后端（如AASIST、MoE）提升域内性能，但往往加剧过拟合并导致浅层特征利用不足。本文切入点在于利用神经坍缩理论揭示的层间表征冗余，提出一种角度距离正则化策略，强制浅层与最终层表征几何对齐。该方法通过2-4层浅层Transformer配合多头部时间潜在注意力机制，在保持域内性能的同时显著提升了域外鲁棒性与推理效率。其价值在于以极低的参数量实现了与深层模型相当的检测性能，但其在复杂信道效应下的长期稳定性及与SASV任务的兼容性尚待验证。

】

---

【XLSR-MamBo: Scaling the Hybrid Mamba-Attention Backbone for Audio Deepfake Detection ｜XLSR-MamBo：混合状态空间-注意力骨干在音频深伪检测中的扩展

作者：Kwok-Ho Ng、Tingting Song、Yongdong Wu 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.02944)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.02944)

> 音频深伪检测（ADD）旨在区分真实语音与合成语音，其核心挑战在于生成技术的指数级进步与检测模型泛化能力线性提升之间的不对称性。现有基于Transformer的架构受限于二次计算复杂度，而纯状态空间模型（SSM）虽具备线性复杂度，却缺乏捕捉全局频谱不一致所需的基于内容的精确检索能力。本文提出XLSR-MamBo，通过系统评估四种SSM-Attention混合拓扑及深度缩放，验证了Hydra原生双向建模在开放集场景下的优势。该框架在In-the-Wild基准上显著优于现有SOTA，但其在封闭集上的性能未超越经典方法，且深度缩放对稳定性的影响机制尚需理论解释。

】

---

【ZoFia: Zero-Shot Fake News Detection with Entity-Guided Retrieval and Multi-LLM Interaction ｜实体引导检索与多LLM交互的零样本虚假新闻检测

研究机构：中国科学院、中国科学院大学

作者：Lvhua Wu、Xuefeng Jiang、Sheng Sun 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.01188)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.01188)

> 零样本虚假新闻检测旨在无需标注数据即可识别动态新闻中的事实错误，但单一大语言模型（LLM）常因知识截止产生幻觉，且易陷入确认偏误导致推理僵化。ZoFia通过解耦内容推理与事实核查，利用实体引导的双源检索与多智能体对抗辩论，试图克服单链推理的认知缺陷。该框架在PolitiFact上取得87.88% F1，但在GossipCop上仅61.22% F1，其跨领域鲁棒性存疑。

】

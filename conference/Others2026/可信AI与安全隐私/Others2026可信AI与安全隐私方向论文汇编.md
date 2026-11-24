# Others2026 · 可信AI与安全隐私方向论文汇编

> 本方向共 24 篇（Others2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Causal Pre-training Under the Fairness Lens: An Empirical Study of TabPFN ｜因果预训练基础模型的公平性边界

研究机构：挪威卑尔根大学、英国牛津大学

作者：Qinyi Liu、Mohammad Khalil、Naman Goel

论文原文见 [arXiv](https://arxiv.org/abs/2601.17912)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.17912)

> 算法公平性研究旨在消除机器学习模型在信贷、司法等高风险决策中因历史数据偏见导致的系统性歧视，其核心张力在于数学上互斥的公平性定义与不可完全观测的真实世界约束之间的冲突。现有后处理或预处理干预手段依赖集中式数据或模型内部访问，难以在隐私敏感或分布偏移场景下保持鲁棒性，而因果推断框架虽强调过程正义，但缺乏对基础模型内生公平性的实证检验。本文通过系统评估基于结构因果模型（Structural Causal Model, SCM）预训练的表格数据基础模型 TabPFN 及其微调变体 FT-TabPFN，在虚假相关与缺失非随机（Missing-Not-At-Random, MNAR）协变量偏移下的表现，揭示了因果预训练在提升预测精度的同时，对群体公平性的改善有限且不一致。这一发现挑战了“因果预训练自动缓解偏见”的潜在假设，为部署此类模型提供了关键的实证警示。

】

---

【Fairness-aware PageRank via Edge Reweighting ｜基于边权重加权的公平PageRank

研究机构：瑞典皇家理工学院

作者：Honglian Wang、Haoyun Chen、Aristides Gionis

论文原文见 [arXiv](https://arxiv.org/abs/2512.08055)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.08055)

> 图链接分析算法在排序与社区检测中广泛应用，但随机游走过程往往因网络同配性导致特定群体获得不成比例的PageRank分数，引发群体公平性问题。现有方法如FairWalk和CrossWalk通过强制局部转移概率均匀来消除偏差，但往往导致图结构发生剧烈扭曲，且难以处理多组场景。本文切入点在于放弃“每步局部公平”的刚性约束，转而通过投影梯度下降优化全局公平损失，仅对现有边权进行有限重加权。该方法在保持图拓扑不变的前提下，以极小的结构扰动实现了显著的全局公平性提升，但其效果依赖于目标分布的预设，且在动态图演化场景下的鲁棒性尚未验证。

】

---

【LLM BiasScope: A Real-Time Bias Analysis Platform for Comparative LLM Evaluation ｜LLM BiasScope：实时多模型偏见对比分析平台

研究机构：德国慕尼黑工业大学、意大利罗马第一大学

作者：Himel Ghosh、Nick Elias Werner

论文原文见 [arXiv](https://arxiv.org/abs/2603.12522)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.12522)

> 导读 大语言模型（LLM）部署中，偏见检测工具长期局限于静态基准或单模型分析，无法在用户自定义提示下实时对比多个模型的偏见模式。现有平台如 Chatbot Arena 侧重质量偏好，缺乏细粒度偏见类型分析；Perspective API 仅检测毒性，忽略社会偏见维度。本文构建 LLM BiasScope，通过两级流水线（句子级偏见检测 + 偏见类型分类）实现多模型并行对比与实时可视化。该工具填补了交互式偏见评估的空白，但其检测器选型依赖静态基准，未验证实时场景下的鲁棒性，且样本量极小，统计效力存疑。

】

---

【Locally Linear Continual Learning for Time Series based on VC-Theoretical Generalization Bounds ｜基于VC理论的分段线性持续学习模型

研究机构：加拿大阿尔伯塔大学

作者：Yan V. G. Ferreira、Igor B. Lima、Pedro H. G. Mapa S. 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.13674)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.13674)

> 非平稳时间序列预测要求模型在输入分布变化时保持适应性，同时避免遗忘旧知识，这一稳定性-可塑性困境在工业与医疗等高利害场景中尤为突出。现有持续学习方法多依赖黑盒神经网络或需用户手动设定聚类阈值，导致解释性缺失或自动化程度低。SyMPLER 通过分段线性结构实现内在可解释性，并利用统计学习理论中的VC维自动确定局部模型添加时机，无需显式聚类。该方法在电力负荷预测中精度持平离线 XGBoost，但仅处理单步线性近似，未建模长程依赖，其解释力在复杂非线性系统中的有效性存疑。

】

---

【xAI团队新研究：基于答案集编程的深度神经网络规则提取系统（xDNN(ASP)）

研究机构：xAI

作者：Ly Ly Trieu、Tran Cao Son

论文原文见 [arXiv](https://arxiv.org/abs/2601.03847)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.03847)

> 形式化可解释人工智能（Formal XAI）旨在为深度学习模型提供具有逻辑正确性保证的解释，以解决黑盒模型在高风险领域的信任危机。现有基于SAT/SMT求解器的方法受限于指数级计算复杂度，难以处理深层网络，且多数规则提取方法仅关注输入-输出映射，忽略了隐藏层内部的交互机制。xDNN(ASP) 首次将答案集编程（Answer Set Programming, ASP）引入深度神经网络（DNN）规则提取，通过C5.0决策树确定阈值并构建分层逻辑程序，实现了全局解释与隐藏层节点影响评估。该方法在小规模合成数据上展现了高保真度与一致性，但缺乏大规模真实数据验证，其可扩展性仍存疑。

】

---

【上海交通团队新研究：联邦学习中隐私、公平与效用的博弈权衡

研究机构：上海交通大学、香港中文大学

作者：Kangkang Sun、Jun Wu、Minyi Guo 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.26841)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.26841)

> 联邦学习（Federated Learning, FL）在保护数据本地性的同时，面临差分隐私（Differential Privacy, DP）噪声掩盖人口统计差异、阻碍公平性检测的内在矛盾。现有方法多将隐私与公平视为独立目标分别优化，缺乏对二者数学兼容性的形式化分析。本文提出FedPF算法，将隐私-公平-效用优化建模为零和博弈，通过Lagrangian对偶机制协调客户端与服务器端的竞争目标。该框架揭示了隐私与公平的反向关系及公平-效用的非单调性，但在独立同分布（Independent and Identically Distributed, IID）假设下验证，未解决非独立同分布（Non-IID）数据下的泛化问题。

】

---

【北京交通团队新研究：联邦推荐中的收敛加速与安全聚合

研究机构：北京交通大学

作者：Zhenxing Yan、Jidong Yuan、Yongqi Sun 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.20283)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.20283)

> 联邦推荐系统需在保护用户隐私的前提下，从分散的用户-物品交互图中学习全局推荐模型，但现有方法面临两大瓶颈：非独立同分布（Non-IID）数据导致的收敛缓慢，以及模型参数交换过程中的隐私泄露风险。FastPFRec 通过引入可信节点中间层与异步图神经网络更新策略，同时解决了效率与安全的双重约束。该方法在四个真实数据集上实现了32.0%的训练轮数缩减与8.1%的精度提升，但其隐私保证依赖于对可信节点的信任假设，且未处理跨客户端拓扑断裂问题，在通用联邦图学习坐标系中定位有限。

】

---

【厦门团队新研究：去中心化信任与边缘安全机制综述

研究机构：厦门大学

作者：Khandoker Ashik Uz Zaman、Mahdi H. Miraz、Mohammed N. M. Ali

论文原文见 [arXiv](https://arxiv.org/abs/2604.17179)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17179)

> 物联网边缘环境因设备异构与资源受限，导致集中式安全架构面临单点故障与隐私泄露双重困境。现有联邦学习（Federated Learning, FL）与零信任架构（Zero Trust Architecture, ZTA）各自解决数据本地化或身份验证问题，但缺乏跨机制的信任一致性标准。本文通过系统分类三十项近期研究，构建涵盖FL、区块链、ZTA及图学习的去中心化信任评估框架。其价值在于提供了架构级对比视角，但缺乏定量基准支撑，难以量化各机制在极端非IID场景下的实际鲁棒性差异。

】

---

【反事实平均公平预测

作者：Irina Arévalo、Marcos Oliva

论文原文见 [arXiv](https://arxiv.org/abs/2604.07009)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.07009)

> 算法公平性研究旨在消除机器学习模型在信贷、司法等高风险决策中因历史数据偏见导致的系统性歧视，其核心张力在于数学上互斥的公平性定义与不可完全观测的真实世界约束之间的冲突。现有后处理方案多依赖阈值调整或群体标签，在隐私敏感的黑盒部署场景中因需访问敏感属性或模型内部而失效。本文提出反事实平均公平预测（Counterfactual Averaging for Fair Predictions, CAFP），通过内部查询事实与反事实属性下的预测并取均值，实现无需重训练、无需测试时群体标签的公平性修正。该方法在理论上消除了属性直接依赖，但在基础率差异显著的现实中，其人口统计均等保证面临前提失效风险，实际公平性增益有限。

】

---

【哥本哈根团队新研究：极值轮廓：基于傅里叶参数化的紧凑视觉归因

研究机构：丹麦哥本哈根大学

作者：Reza Karimzadeh、Albert Alonso、Frans Zdyb 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.01411)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.01411)

> 视觉归因旨在量化输入像素对模型预测的贡献，但现有扰动方法生成的密集掩码常出现碎片化与过拟合，导致解释缺乏拓扑一致性。本文切入点在于将掩码优化从像素级空间转移至低维几何参数空间，通过星凸轮廓的傅里叶级数参数化，在保证单连通性的前提下实现极值保留/删除目标。该方法以 $2K+3$ 个自由参数替代像素级优化，在自监督模型上显著提升了归因质量与稳定性。其价值在于提供了解释的几何先验约束，但星凸假设对非凸物体的适用性仍存疑。

】

---

【基于极端随机树（Extra Trees）的集中式物联网攻击检测

作者：Hikmat A. M. Abdeljaber、Md. Alamgir Hossain、Sultan Ahmad 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.08084)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.08084)

> 物联网安全检测面临数据异构与隐私约束的双重挑战，传统集中式架构因通信瓶颈与单点故障风险难以适用，而联邦学习虽解决了数据本地化问题，但在极端非独立同分布（Non-IID）场景下模型收敛困难。本文切入点在于回归集中式监督学习范式，利用极端随机树（Extra Trees Classifier）的集成特性与随机化机制，在标准IID假设下追求分类精度的上限。该方法通过严格的预处理与超参数调优，在多个IoT数据集上实现了接近完美的分类指标，但其价值局限于静态、可控的数据环境，无法证明在分布式、对抗性真实IoT场景中的有效性。

】

---

【多变量目标不确定性量化：基于CT原理的量化森林

作者：Takuya Kanazawa

论文原文见 [arXiv](https://arxiv.org/abs/2512.16383)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.16383)

> 多变量回归任务中，传统方法常假设各目标分量独立，导致联合分布估计失效，无法捕捉变量间依赖关系。现有非参数方法要么受限于凸区域假设，要么计算成本过高，难以在表格数据上高效应用。本文提出Tomographic Quantile Forests (TQF)，利用Cramér-Wold定理将多变量分布重建转化为方向投影的量化回归问题，通过切片Wasserstein距离优化实现非参数联合分布估计。该方法在表格数据上实现了与参数化模型相当的非参数分布估计能力，但其对高维输入空间的扩展性及与保形预测的结合尚存疑问。

】

---

【宾夕法尼亚团队新研究：安全信息论学习模型预测控制

研究机构：美国宾夕法尼亚大学

作者：Zirui Zang、Ahmad Amine、Nick-Marios T. Kokolakis 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.16187)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.16187)

> 迭代任务中的随机非线性系统需在满足安全约束的前提下持续优化性能，传统学习模型预测控制（LMPC）在随机系统中因采样保守与模式崩溃导致性能停滞或失效。本文切入点在于将信息论模型预测路径积分（MPPI）与自适应惩罚机制结合，解决无约束MPPI无法处理一般状态约束的难题。通过归一化流学习值函数分布并并行化惩罚参数采样，SIT-LMPC在真实越野赛车中实现了比基线快31.43%的圈速且保持安全。该方法在实时性与安全性平衡上表现优异，但缺乏形式化统计保证，其安全边界依赖经验性惩罚参数。

】

---

【工业物联网信任收敛加速框架

作者：Aymen Bouferroum、Valeria Loscri、Abderrahim Benslimane

论文原文见 [arXiv](https://arxiv.org/abs/2603.24111)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.24111)

> 工业物联网（IIoT）环境中的电磁干扰与多径效应导致网络质量剧烈波动，传统信任模型在此条件下收敛缓慢，形成恶意节点未被识别的脆弱窗口。现有方案多假设网络稳定或依赖昂贵硬件，忽视了动态信道状态对信任评估速度的直接影响。本文提出信任收敛加速（Trust Convergence Acceleration, TCA）机制，利用机器学习预测收敛时间并动态调整马尔可夫链转移概率，在仿真中实现收敛时间最大28.6%的缩减。该框架在理论层面填补了网络质量与信任收敛关联的空白，但缺乏真实工业场景数据验证，其实际部署效能存疑。

】

---

【差分隐私联邦物联网中的自主模型权重修复框架

作者：Chethana Prasad Kabgere、Shylaja S S

论文原文见 [arXiv](https://arxiv.org/abs/2512.13460)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.13460)

> 联邦学习在物联网多跳网络中面临非对抗性信道损坏导致的参数失真，现有鲁棒聚合机制仅针对恶意攻击设计，无法处理比特翻转与丢包。本文切入点在于将传输层失真建模为可检测、可重构的信号处理问题，在聚合前进行自适应修复。通过融合差分隐私与安全聚合，DP-EMAR 实现了隐私保护与错误修复的解耦。该框架在 10% 损坏率下将准确率从 82.4% 提升至 94.9%，但其修复能力受限于结构化损坏，对随机噪声的鲁棒性仍存疑。

】

---

【新墨西哥团队新研究：不确定性集合统一分类学

研究机构：美国新墨西哥大学

作者：Takaaki Fujita、Florentin Smarandache

论文原文见 [arXiv](https://arxiv.org/abs/2603.15667)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.15667)

> 该方向旨在解决模糊、粗糙、软及中性集等范式各自独立导致的理论迁移困难与语义表达割裂问题。现有方法虽能处理单一维度的不确定性，但缺乏统一的代数结构来描述属性值间的冲突关系，且静态模型无法适应动态层级场景。本文切入点在于构建一个涵盖20余种变体的系统性分类学框架，通过参数化维度与矛盾函数实现多范式的统一映射。其价值在于提供了清晰的理论坐标系，但缺乏对计算复杂度与大规模实证性能的量化验证。

】

---

【新西兰奥克兰团队新研究：统一置信度校准与分类的损失函数

研究机构：新西兰奥克兰大学、德国慕尼黑工业大学

作者：Sandra Gómez-Gálvez、Tobias Olenyi、Gillian Dobbie 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.12245)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.12245)

> 深度神经网络在高风险场景部署时，其输出概率常与真实正确率脱节，导致模型在错误预测时仍表现出高置信度。现有训练期校准方法面临稳定性与精度的二选一困境：双阶段训练虽能提升精度但易引发训练崩溃，单损失方法虽稳定却牺牲分类性能。本文通过引入辅助“未知”类构建统一损失函数，将不确定性显式建模融入训练过程，试图打破这一权衡。该方法在多个基准上实现了精度与校准的帕累托最优，但其对输出空间维度的扩展是否影响下游任务兼容性，仍需进一步验证。

】

---

【理工团队新研究：极端稀疏化下的可解释性崩溃：VAE-SAE混合架构的实证研究

研究机构：印度理工学院

作者：Dip Roy、Rajiv Misra、Sanjay Kumar Singh

论文原文见 [arXiv](https://arxiv.org/abs/2603.18056)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.18056)

> 现有稀疏自编码器（Sparse Autoencoder, SAE）研究聚焦于从大语言模型（LLM）激活中提取单义特征，但极少关注极端容量约束下特征存活的极限。当网络被压缩至10%容量时，重构误差往往保持稳定，掩盖了局部神经元功能的系统性丧失。本文通过构建变分自编码器（Variational Autoencoder, VAE）与SAE的混合架构，在图像生成任务中量化了这一“全局稳定、局部崩溃”的悖论。该研究揭示了稀疏化对可解释性的内在破坏性，但受限于基础架构与视觉数据集，其结论向LLM领域的迁移性尚存疑。

】

---

【记忆增强智能体中的偏见编码与放大机制

作者：Himanshu Gharat、Himanshi Agrawal、Gourab K. Patro

论文原文见 [arXiv](https://arxiv.org/abs/2512.16532)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.16532)

> 大语言模型（Large Language Models, LLMs）在招聘等高利害场景中部署时，其记忆模块可能将历史偏好转化为系统性歧视。现有研究多关注静态输出公平，忽视了智能体（Agent）工作流中记忆对偏见的动态编码与跨阶段放大效应。本文通过构建基于 GPT-4.1 的记忆增强招聘智能体，量化了个性化检索与重排过程中性别偏见的累积路径。该工作揭示了记忆机制作为偏见载体的风险，但缺乏对去偏干预有效性的验证，其结论的普适性仍受限于单一属性与模拟环境。

】

---

【边缘AI可解释性服务化架构

作者：Samaresh Kumar Singh、Joyjit Roy

论文原文见 [arXiv](https://arxiv.org/abs/2602.04120)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.04120)

> 边缘设备算力受限导致LIME、SHAP等高保真解释方法因需超过1000次模型评估而无法实时部署，现有方案在冗余计算、资源错配与解释失效风险上存在系统性低效。本文切入点是将解释生成从模型推理中解耦，构建包含语义缓存、轻量验证与自适应分发的分布式服务架构。通过FAISS检索相似输入并复用解释，配合15次扰动的保真度校验，XaaS在保持0.923保真度的同时将延迟降低38%。该架构验证了服务化解释在异构边缘集群中的可行性，但缓存复用对长尾分布下解释稳定性的影响尚未充分验证。

】

---

【迪肯团队新研究：量子联邦自编码器用于物联网异常检测

研究机构：澳大利亚迪肯大学

作者：Devashish Chaudhary、Sutharshan Rajasegarar、Shiva Raj Pokhrel

论文原文见 [arXiv](https://arxiv.org/abs/2603.22366)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.22366)

> 物联网边缘设备面临隐私泄露与单点故障风险，传统集中式检测无法兼顾数据本地化与复杂流量建模。现有联邦学习（FL）方案多依赖经典自编码器，难以高效捕捉高维非线性流量特征，且缺乏在真实硬件层级网络中的量子化验证。本文提出量子联邦自编码器（QFL-QAE），将量子自编码器（QAE）部署于边缘节点，通过分层聚合实现隐私保护下的分布式异常检测。该工作首次验证了量子模型在真实物联网测试床上的联邦可行性，但受限于小规模数据集与单一攻击类型，其量子优势的实际边界尚不明确。

】

---

【阿姆斯特丹团队新研究：AI可信度的社会技术解构：AIES与FAccT社区的范围综述

研究机构：荷兰阿姆斯特丹大学、荷兰代尔夫特理工大学

作者：Siddharth Mehrotra、Jin Huang、Xuelong Fu 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.21293)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.21293)

> 现有AI可信度研究陷入技术中心主义陷阱，将复杂的社会技术系统简化为鲁棒性或公平性等技术指标，导致客观属性与用户主观感知严重脱节。本文通过系统梳理AIES与FAccT两大核心会议文献，揭示这一概念界定与测量方法的结构性缺失。研究采用范围综述与主题编码，引入“意图-嵌入-实现”价值框架，对43篇核心论文进行本体论剖析。该工作填补了社会技术维度的测量空白，但其定性结论缺乏跨学科量化验证，且未提供可操作的工程化测量协议。

】

---

【面向盲人与低视力用户的可解释人工智能：代理时代的信任、模态与可解释性

作者：Abu Noman Md Sakib、Protik Dey、Zijie Zhang 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.00187)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.00187)

> 现有主流可解释人工智能（XAI）方法依赖视觉热力图，导致盲人与低视力（BLV）用户被完全排除在AI决策验证之外，且在多步代理任务中面临错误不可逆传播的风险。本文通过实证访谈揭示了BLV用户特有的“自我归因偏差”与对对话式交互的强需求，指出静态解释无法支撑代理系统的过程级验证。研究采用半结构化访谈与反思性主题分析，构建了面向非视觉模态的信任校准与验证策略框架。该工作填补了无障碍XAI在代理场景下的实证空白，但缺乏量化指标与大规模验证，其结论的普适性存疑。

】

---

【香港浸会团队新研究：通信高效联邦图分类的生成式扩散建模

研究机构：香港浸会大学、香港理工大学

作者：Xiuling Wang、Xin Huang、Haibo Hu 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.15722)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.15722)

> 联邦图学习（Federated Graph Learning, FGL）在解决数据隐私的同时，常因多轮参数同步导致高昂的通信开销，且客户端非独立同分布（Non-IID）数据加剧了模型收敛困难。现有方法多依赖增加通信轮数或复杂聚合策略来平衡精度与效率，难以在带宽受限场景下实现高效协作。本文提出CeFGC框架，利用图生成扩散模型（GGDM）替代直接参数交换，将服务器-客户端通信压缩至固定3轮，并通过合成数据增强缓解分布漂移。该方法在图分类任务上显著提升了通信效率与模型泛化能力，但其隐私保护机制仅依赖基础加密，未深入探讨强隐私预算下的效用边界。

】

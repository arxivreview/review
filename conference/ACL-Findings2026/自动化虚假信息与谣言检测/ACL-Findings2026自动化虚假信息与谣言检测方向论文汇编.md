# ACL-Findings2026 · 自动化虚假信息与谣言检测方向论文汇编

> 本方向共 6 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【CSI: An Investigative Multi-Agent Framework for Explainable Short Video Fake News Detection ｜协作式短视频调查框架

研究机构：快手

作者：Yuxin Wang、Yang Yang、Huaiwen Zhang

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_518a90dce395)

> 短视频虚假信息检测面临的核心矛盾是：多模态内容（视频、音频、文本）的复杂逻辑与现有黑盒分类器或单链推理模型的低可解释性、浅层理解之间的冲突。传统多模态小语言模型（MSLM）虽精度高但缺乏推理能力，而多模态大语言模型（MLLM）直接推理易受跨模态冲突干扰产生幻觉。本文切入点是将检测重构为“协作调查”任务，通过多智能体分工取证、结构化辩论与专用判决器实现高精度与可解释性的统一。该方法在两个真实数据集上取得SOTA性能，但其对多智能体辩论中偏差传递机制的量化评估仍存疑。

】

---

【Deconstruct, Diagnose, and Deliberate: A Protocol-Adaptive Role-Specific Multi-Agent Framework for Fake News Detection ｜协议自适应角色专用多智能体框架

研究机构：中国科学院大学

作者：Zhigan Zhang、Jie Sui

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2c2d020ccc5e)

> 虚假新闻检测需应对事实扭曲、逻辑谬误与语境操纵的复合欺骗，但现有单链推理或固定立场对抗的多智能体框架难以解构这种多维复杂性，且易陷入认知同质性导致的回声室效应。PARD 的切入点在于将验证过程从“立场辩论”重构为“功能诊断”，通过角色分工与动态协议选择实现认知多样性。其核心做法是建立事实、逻辑、语境三维度的异构LLM团队，并引入强化学习机制自适应选择交互协议。该框架在可解释性与数据效率上表现突出，但在纯文本精度上仍落后于非生成式检索基线，其动态治理机制的实际增益边界尚存疑。

】

---

【Dialectical Structured Reasoning for Explainable Multimodal Fake News Detection ｜辩证结构化推理

研究机构：北京科技大学、新加坡管理大学

作者：Ruichao Yang、Yufan Bian、Wei Gao 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1ff708b91687)

> 多模态虚假信息检测面临的核心矛盾是：现有模型将复杂的社交证据压缩为单一向量，导致决策过程缺乏逻辑透明度，且难以处理碎片化、极化的用户反馈。现有方法要么依赖非可微的提示驱动辩论，要么仅做事后解释，无法在训练阶段优化推理路径。DSR 将检测重构为在异构传播图上的辩证裁决过程，通过可微分的 Judge 模块整合支持性与反驳性证据路径。该方法在精度与解释质量上均超越基线，但其对冻结 MLLM 背景知识的依赖在长尾事实场景下的可靠性尚存疑。

】

---

【Multi-Scale Spectral Selection and Entropy-Guided Uncertainty Fusion for Multimodal Rumor Detection ｜多尺度谱选择与熵引导不确定性融合的多模态谣言检测

研究机构：中国科学院大学、中国科学技术大学

作者：Zongliang Han、Wenyu Guo、Guoqing Jin 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8447b459aa69)

> 多模态谣言检测面临空间域特征噪声大与跨模态语义不一致的双重挑战，现有频域方法仅做简单变换而缺乏细粒度筛选。MS-SFM通过离散余弦变换将图文特征映射至频域，利用多尺度卷积与挤压-激励机制过滤噪声，并基于熵值动态融合共享与私有特征。该方法在Weibo等数据集上取得领先性能，但其依赖固定阈值与内部特征，未涉及外部证据检索，在开放域事实核查中的泛化能力存疑。

】

---

【TRUST: Towards Robust Social Bot Detection via Uncertainty-Guided Pseudo-Labeling and Graph Structure Purification ｜基于不确定性引导的图结构净化社交机器人检测

研究机构：南开大学、天津大学

作者：Ruixuan Xu、Mengting Hu、Zhunheng Wang 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e0ab7cbf37ce)

> 社交机器人通过构建异质性社交连接伪装成人类，导致图神经网络在消息传递阶段接收错误标签信息，进而产生误分类。现有方法依赖同质性假设，无法区分高置信节点与低置信节点，缺乏对欺骗性连接的主动干预机制。TRUST框架通过证据深度学习量化节点级不确定性，动态生成伪标签并移除冲突边，实现图结构净化。该方法作为通用插件在多种骨干网络上稳定提升性能，但其有效性高度依赖验证集阈值搜索的准确性，且未验证在动态演化图结构下的鲁棒性。

】

---

【ZoFia: Zero-Shot Fake News Detection with Entity-Guided Retrieval and Multi-LLM Interaction ｜实体引导检索与多LLM交互的零样本虚假新闻检测

研究机构：中国科学院、中国科学院大学

作者：Lvhua Wu、Xuefeng Jiang、Sheng Sun 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.01188)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.01188)

> 零样本虚假新闻检测旨在无需标注数据即可识别动态新闻中的事实错误，但单一大语言模型（LLM）常因知识截止产生幻觉，且易陷入确认偏误导致推理僵化。ZoFia通过解耦内容推理与事实核查，利用实体引导的双源检索与多智能体对抗辩论，试图克服单链推理的认知缺陷。该框架在PolitiFact上取得87.88% F1，但在GossipCop上仅61.22% F1，其跨领域鲁棒性存疑。

】

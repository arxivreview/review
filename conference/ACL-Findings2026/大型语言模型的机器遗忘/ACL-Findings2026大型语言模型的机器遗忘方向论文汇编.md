# ACL-Findings2026 · 大型语言模型的机器遗忘方向论文汇编

> 本方向共 10 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Anatomy of Unlearning: The Dual Impact of Fact Salience and Model Fine-Tuning ｜事实流行度与训练范式对机器遗忘的交互影响

作者：Anna Borisiuk、Andrey Savchenko、Alexander Panchenko 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_dcb5c20c0493)

> 大语言模型（LLM）在部署后需移除敏感或过时知识，但现有研究隐含假设所有事实同等可遗忘，且极少系统对比预训练与监督微调（SFT）模型对同一遗忘信号的响应差异。本文切入点在于揭示事实流行度与模型训练类型如何共同决定遗忘性能。通过构建基于 Wikidata 的真实世界基准 DUET，并控制变量对比两种训练范式，发现流行事实更难擦除且预训练模型存在反向学习现象。该工作填补了评估维度的空白，但其结论受限于单一模型架构与特定领域数据，普适性尚待验证。

】

---

【Before Forgetting, Learn to Remember: Revisiting Foundational Learning Failures in LVLM Unlearning Benchmarks ｜多模态大模型遗忘基准的阶段1失效诊断与ReMem构建

作者：JuneHyoung Kwon、MiHyeon Kim、Eunju Lee 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.03759)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.03759)

> 多模态大语言模型（Large Vision-Language Models, LVLMs）的机器遗忘（Machine Unlearning, MU）旨在移除训练数据中的敏感隐私，但现有评估基准存在根本性缺陷：模型在初始微调阶段未能有效记忆目标信息，导致后续遗忘评估无效。本文通过内部状态分析证实了这一“阶段1失效”，并构建了包含多跳推理与多视图图像的ReMem基准，以确立可靠的遗忘评估基础。该工作揭示了当前多模态遗忘研究的评估盲区，但仅提供了基准与诊断，未提出新的遗忘算法，其结论的普适性仍受限于特定模型架构与数据规模。

】

---

【CURaTE: Continual Unlearning in Real Time with Ensured Preservation of LLM Knowledge ｜实时持续遗忘框架

研究机构：韩国科学技术院

作者：Seyun Bae、Seokhan Lee、Eunho Yang

论文原文见 [arXiv](https://arxiv.org/abs/2604.14644)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.14644)

> 大语言模型（LLM）在部署后面临连续到达的遗忘请求，现有参数修改方法因累积误差导致效用崩溃且处理延迟高。本文提出“行为遗忘”范式，通过训练独立的句子嵌入模型拦截敏感查询，而非修改LLM权重。该方法实现了毫秒级响应与近乎完美的知识保留，但仅抑制输出而未擦除内部知识，其对抗鲁棒性存疑。

】

---

【Direct Token Optimization: A Self-contained Approach to Large Language Model Unlearning ｜直接Token优化

研究机构：美国埃默里大学

作者：Hong kyu Lee、Ruixuan Liu、Li Xiong

论文原文见 [arXiv](https://arxiv.org/abs/2510.00125)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.00125)

> 大语言模型（LLM）在微调阶段极易记忆特定数据，导致隐私泄露与版权风险，而完全重训练成本过高。现有无保留集遗忘方法如FLAT仅引导模型生成拒绝回答，未能触及知识存储的核心Token，导致遗忘质量低下。本文提出直接Token优化（DTO），通过Delta-score自主识别关键知识Token并执行梯度上升，同时利用KL散度约束非目标Token以维持效用。该方法在TOFU基准上实现了极高的遗忘质量，但其对长距离依赖知识的覆盖能力及对抗鲁棒性仍存疑。

】

---

【From Domains to Instances: Dual-Granularity Data Synthesis for LLM Unlearning ｜双粒度数据合成框架

研究机构：香港理工大学、华为

作者：Xiaoyu Xu、Minxin Du、Zitong Li 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.04278)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.04278)

> 大语言模型（LLM）遗忘的核心痛点在于现有基准的遗忘集无法覆盖模型内部真实记忆的语义变体，导致评估结论失真。BiForget 通过目标模型自引导的双阶段合成策略，自动化生成与模型知识分布对齐的领域级与实例级遗忘集。该框架在 Harry Potter 域将数据量减半的同时提升了相关性，但其在低知识密度领域的泛化能力仍存疑。

】

---

【LUNE: Efficient LLM Unlearning via LoRA Fine-Tuning with Negative Examples ｜基于低秩适配器的负样本大语言模型遗忘

研究机构：美国加州大学尔湾分校、美国普渡大学

作者：Yezi Liu、Hanning Chen、Wenjun Huang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.07375)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.07375)

> 大语言模型（LLM）在预训练中记忆了敏感信息，但全参数微调或重训练带来的计算成本使其难以在部署后快速擦除特定知识。现有方法要么更新全部参数导致效用崩塌，要么依赖复杂的偏好优化框架，缺乏一种兼顾效率与鲁棒性的轻量级方案。LUNE 通过冻结骨干网络并仅更新低秩适配器（LoRA），结合精心构造的负样本进行微调，将遗忘操作限制在低维子空间内。该方法在 7B 规模模型上实现了与全参数微调相当的遗忘效果，但其在复杂语义纠缠场景下的效用保持能力仍存疑。

】

---

【Multimodal Unlearning Across Vision, Language, Video, and Audio: Survey of Methods, Datasets, and Benchmarks ｜多模态基础模型遗忘的系统级分类与干预机制综述

研究机构：美国圣母大学

作者：Nobin Sarwar、Shubhashis Roy Dipta、Zheyuan Liu 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2607.07907)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2607.07907)

> 多模态基础模型在预训练中不可避免地编码了跨模态的敏感、版权或有害关联，而重训练在工程上不可行，现有算法中心化的分类体系难以揭示端到端流水线中真正的干预点。本文提出以“干预阶段-控制路径”为核心的系统级分类框架，将遗忘方法从数据侧、训练时、架构约束到解码时进行统一梳理，并形式化了多模态近似重训练的分布等价性。该综述为跨模态遗忘提供了稳定的比较脚手架，但其作为纯综述缺乏原创算法验证，且对解码时干预是否满足不可逆合规要求未给出明确理论界定。

】

---

【OFFSIDE: Benchmarking Unlearning Misinformation in Multimodal Large Language Models ｜OFFSIDE：多模态大语言模型虚假信息遗忘基准

研究机构：哈尔滨工业大学、美国伊利诺伊大学厄巴纳-香槟分校

作者：Hao Zheng、Zirui Pang、Ling li 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.22535)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.22535)

> 多模态大语言模型（MLLMs）在预训练中不可避免地记忆了包含视觉与文本耦合的虚假信息，而现有机器遗忘（Machine Unlearning, MU）基准缺乏对图像内部有害线索的覆盖，导致无法评估模型在真实场景下的遗忘鲁棒性。本文提出 OFFSIDE 基准，通过构建包含真实足球转会谣言的多模态数据集，首次引入细粒度遗忘与视觉谣言移除任务。实验表明，现有主流遗忘方法在视觉谣言场景下完全失效，且遗忘效果主要由灾难性遗忘驱动而非知识擦除。该基准揭示了当前 MLLM 遗忘方法的重大盲区，但受限于仅测试了五种经典优化算法，未涵盖机制级干预方法。

】

---

【Representation-Guided Parameter-Efficient LLM Unlearning ｜表示几何引导的低秩大语言模型遗忘

作者：Zeguan Xiao、Lang Mo、Yun Chen 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17396)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8d626cf0a2b4)

> 大语言模型（LLM）遗忘面临的核心矛盾是：在移除敏感知识的同时，必须维持模型在保留集上的通用效用。现有基于参数重要性（如Fisher信息）的低秩适应（LoRA）方法因“超叠加”现象导致参数多义性，难以精准隔离遗忘与保留知识，常引发效用崩溃。本文提出ReGLU，通过表示空间几何解耦替代参数统计量估计，利用平衡协方差矩阵初始化LoRA并引入正交损失约束更新方向。该方法在TOFU和WMDP基准上显著优于FILA和VILA，但其有效性局限于参数高效微调框架，未验证全参数场景下的深层知识擦除能力。

】

---

【Rotation Control Unlearning: Quantifying and Controlling Continuous Unlearning for LLM with The Cognitive Rotation Space ｜旋转控制遗忘：量化与调控LLM持续遗忘的认知旋转空间

研究机构：西安电子科技大学

作者：Xiang Zhang、Kun Wei、Xu Yang 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.25743)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.25743)

> 大语言模型（LLM）在真实场景中面临连续到达的遗忘请求，现有方法因依赖保留集且参数更新相互干扰，导致累积效用损失。本文切入点在于将LoRA更新重构为高维空间中的旋转操作，通过控制旋转角度与正交轴来量化并隔离遗忘过程。该方法在无保留集条件下实现了持续遗忘的稳定性。其价值在于提供了可解释的遗忘程度度量，但旋转角度与知识擦除深度的因果关联仍缺乏信息论层面的严格证明。

】

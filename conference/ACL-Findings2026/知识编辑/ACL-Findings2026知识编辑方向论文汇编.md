# ACL-Findings2026 · 知识编辑方向论文汇编

> 本方向共 16 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【AlphaEdit+: Model Editing in the Presence of Conflicting and Inconsistent Knowledge ｜AlphaEdit+：冲突与不一致知识下的模型编辑

研究机构：美国普林斯顿高等研究院、中国科学院大学

作者：Qing Liu、Jianhao Zhang、Ou Wu 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_10b8d08ae5b0)

> 知识编辑旨在以低成本局部更新大语言模型中的过时事实，但现有方法在编辑目标与模型既有参数知识存在逻辑矛盾或数值偏差时，往往导致编辑失败或局部性崩塌。AlphaEdit通过零空间投影保证保留知识不变，却未考虑新编辑与保留知识、历史编辑之间的几何冲突及目标值与当前参数状态的不一致。本文通过数学分析揭示该失效机制，并提出AlphaEdit+，引入扰动松弛、冲突加权与渐进平滑三个组件以修复上述缺陷。该方法在自建高冲突数据集上显著优于基线，但在标准基准上未超越领域SOTA，且平滑机制引入了约2.29倍的计算开销。

】

---

【CaPEdit: Capability-Preserving Lifelong Knowledge Editing For Language Models ｜能力保持的终身知识编辑

研究机构：清华大学、中国科学技术大学

作者：Song-Li Wu、Zhaocheng Du、Xianquan Wang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4d04b1653dae)

> 终身知识编辑（Lifelong Knowledge Editing, LKE）旨在通过局部参数更新让大语言模型（LLMs）持续吸收动态事实，但现有方法在累积编辑中导致记忆、推理等基础能力严重退化。传统正则化策略因限制更新幅度而牺牲知识注入效率，且未能区分事实更新与程序性知识适应的时间尺度差异。CaPEdit 提出双时间尺度奖励机制，通过显式合成程序性知识信号，将快速事实修正与慢速能力保持解耦。该框架在保持高编辑精度的同时显著提升了能力保留率，但其对程序性知识合成的依赖是否引入额外计算瓶颈，以及在非结构化知识编辑中的泛化能力，仍存疑。

】

---

【CLaRE-ty Amid Chaos: Quantifying Representational Entanglement to Predict Ripple Effects in LLM Editing ｜关键层表示纠缠量化

研究机构：新加坡国立大学

作者：Manit Baser、Alperen Yildiz、Dinil Mon Divakaran 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.19297)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.19297)

> 知识编辑在更新目标事实时，常引发无关事实的意外改变，即涟漪效应，但现有评估多在编辑后检测，缺乏编辑前的风险预测能力。梯度相似度方法（GradSim）虽能估计纠缠，但计算成本高且与跨域涟漪效应相关性弱。本文提出CLARE，通过提取单一关键层的前向激活向量并计算余弦相似度，在编辑前量化事实间的表示纠缠。该方法在预测精度与计算效率上显著优于梯度基线，为构建保留集和红队测试提供了轻量级基础设施，但其预测的是风险概率而非确定性干扰，高纠缠并不必然导致涟漪。

】

---

【Confidence-Aware Ranker Ensembles for Robust In-Context Knowledge Editing ｜特征加权集成检索用于鲁棒上下文知识编辑

研究机构：美国威廉与玛丽学院、美国伦斯勒理工学院

作者：Tejal Nair、Mahmud Wasif Nafee、Maiqi Jiang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b529e7047846)

> 上下文知识编辑（IKE）旨在不修改模型参数，仅通过提示注入示例来更新大语言模型的事实认知，但单一检索器在面对反事实或干扰项丰富的查询时极易因证据选择偏差而失效。现有IKE方法依赖单一检索器的表面相似度启发式，无法自适应地利用不同检索器（如语义型与词法型）的互补优势，导致在复杂查询下可靠性与局部性难以兼顾。FWE-IKE通过校准异构检索器的置信度分布，并引入基于特征加权的混合路由机制，动态选择或融合检索结果以构建更鲁棒的提示上下文。该方法在CounterFact基准上实现了88.33%的编辑成功率，显著优于单一检索器基线，但其性能仍受限于上下文窗口容量，且在单跳事实编辑上的绝对准确率远低于参数编辑方法，其长期稳定性与计算开销的平衡尚存疑。

】

---

【DKME: Rethinking Coupled Knowledge Memory for Lifelong Model Editing of Large Language Models ｜解耦知识记忆编辑

研究机构：华南理工大学、哈尔滨工业大学

作者：Guanyu Zheng、Wang Zhenyu、He Tingting 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_cb7206685cc2)

> 终身知识编辑旨在向大语言模型（LLMs）持续注入事实更新而不触发重训练，但现有记忆基方法在编辑累积时普遍遭遇灾难性遗忘。本文指出其根源在于寻址（路由）与存储（写入）机制的耦合，导致跨编辑干扰随规模放大。DKME通过事实感知语义寻址与分区记忆存储两阶段解耦，将更新限制在独立参数子空间。该方法在多域与关联事实基准上实现了更优的可靠性-局部性平衡，但其分区粒度依赖无监督聚类，对长尾知识的覆盖能力存疑。

】

---

【EvoEdit: Evolving Null-space Alignment for Robust and Efficient Knowledge Editing ｜动态零空间对齐的知识编辑框架

研究机构：加拿大麦吉尔大学、加拿大魁北克人工智能研究所

作者：Sicheng Lyu、Yu Gu、Xinyu Wang 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.13851)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.13851)

> 大语言模型在持续更新事实知识时，静态参数编辑方法因累积干扰导致先前编辑失效，即“灾难性干扰”。现有定位-编辑范式虽能处理单次或批量更新，但在序列编辑场景下缺乏对历史知识子空间的动态维护机制，导致模型性能随编辑次数增加而急剧退化。EvoEdit通过增量式零空间对齐，将每次新编辑投影至包含所有历史知识的正交补空间中，从而在理论上保证输出不变性。该方法在10K次序列编辑中实现了98.29%的编辑效力，较静态基线提升显著，但其对SVD截断阈值的依赖及在极端长序列下的数值稳定性边界尚存疑。

】

---

【FABLE: Fine-grained Fact Anchoring for Unstructured Model Editing ｜非结构化知识编辑中的细粒度事实锚定

作者：Peng Wang、Biyu Zhou、Xuehai Tang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.12559)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_286e0e20f36e)

> 非结构化模型编辑旨在让大语言模型吸收真实世界文本，但现有方法往往仅能整体复述编辑后的文本，无法可靠地检索其中的原子事实。本文指出这种“整体记忆”与“细粒度访问”的错位源于Transformer单向流动中表面形式生成对底层事实表示的放大而非校正。FABLE通过两阶段分层策略，先将离散事实锚定在浅层，再对深层进行最小化更新以生成连贯文本。该框架在细粒度问答上取得显著提升，但其对批量编辑稳定性的验证尚缺。

】

---

【HyperEdit: Unlocking Instruction-based Text Editing in LLMs via Hypernetworks ｜指令式文本编辑中的动态适配与局部保真

研究机构：美国康涅狄格大学、美国加州大学河滨分校

作者：Yiming Zeng、Jinghan Cao、Zexin Li 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.12544)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.12544)

> 指令式文本编辑要求模型在遵循用户修改意图的同时，严格保留未变更内容，但现有通用大语言模型常因过度编辑破坏上下文完整性，而专用编辑模型又缺乏对多样化指令的动态适应能力。HyperEdit 通过超网络生成请求特定的低秩参数实现意图对齐，并引入差异感知正则化将监督信号聚焦于修改跨度，从而在3B参数规模下同时满足这两项约束。该方法在InstrEditBench上取得了优于现有专用编辑模型的相对提升，但其评估指标对编辑精度的捕捉能力以及动态参数生成的必要性，仍需更严格的协议验证。

】

---

【LEDGER: Scaling Agentic Document Editing with Dependency-aware Graph Retrieval ｜依赖感知图检索的长文档智能体编辑

作者：Mike Hang Wang、Utkarsh Garg、Reza Davari 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.28379)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.28379)

> 长文档智能体编辑面临上下文效率与结构一致性的根本矛盾：全量输入导致Token成本线性增长且稀释注意力，而基于语义相似度的检索常遗漏跨引用等结构依赖。LEDGER通过构建显式依赖图实现恒定Token预算下的精准上下文选择，将编辑一致性从56%提升至76%。该方法验证了结构引导可替代部分内部推理能力，但其图构建依赖LLM调用的前置成本及非参数化特性限制了知识的持久固化。

】

---

【Multi-Hop Knowledge Editing via Critic-Guided Multi-Agent Reasoning ｜多跳知识编辑中的闭环推理框架

研究机构：北京理工大学、新西兰奥克兰大学

作者：Xudong Li、Yuhang Tian、Dandan Song 等 14 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2bcea90cf3a2)

> 多跳知识编辑（Multi-Hop Knowledge Editing, MHKE）要求模型在更新事实后，能正确沿推理链传播新信息，但现有前馈式方法缺乏错误定位机制，早期检索噪声会静默级联至最终答案。CARE 通过引入链级验证与有界回溯的闭环推理，将单向分解-检索流程改造为可自我修正的多智能体协作。该方法在 MQuAKE-hard 上实现了 94.17% 的准确率，但在通用多跳场景下仍落后于最新图结构方法，其闭环机制的计算开销与深层链覆盖能力存疑。

】

---

【One Mask to Rule Them All: On Hidden Facts after Editing and How to Find Them ｜定位-编辑范式的注意力劫持机制与共享掩码反转

作者：Ali Holmov、Paul Youssef、Nandi Schoots 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.28839)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8f7033d75140)

> 定位-编辑方法（Locate-and-Edit）通过修改前馈神经网络（FFN）权重实现事实更新，但现有评估仅关注输出行为，掩盖了内部知识是否被真正覆盖的机制盲区。ROME与MEMIT虽在基准上表现优异，却难以解释为何单点修改能对抗Transformer的冗余知识路径，且存在涟漪效应与安全漏洞。本文切入点在于验证编辑是否依赖共享的注意力抑制机制而非知识擦除，通过训练跨编辑共享的二元掩码反转编辑效果。该发现揭示了定位-编辑方法的根本局限，为编辑检测与防御提供了新路径，但反转率未达100%且未覆盖非参数编辑路线。

】

---

【Orthogonal Representation Editing: Decoupling Semantic Entanglement in Batch Knowledge Editing of LLMs ｜正交表示编辑：解耦批量知识编辑中的语义纠缠

研究机构：天津大学、中国科学院大学

作者：Wenhao Yu、Zhicong Lu、Bo Lv 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.22627)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.22627)

> 大语言模型（LLMs）参数静态化导致事实知识过时，全量重训练成本高昂且易引发灾难性遗忘，知识编辑（Knowledge Editing, KE）旨在以低成本局部更新特定事实。现有批量编辑方法在共享句法模板下性能退化，根源在于表示空间中通用语义结构的纠缠干扰。本文提出正交表示编辑（Orthogonal Representation Editing, ORE），通过构建通用语义子空间并对编辑向量施加正交约束，在表示空间解耦共享语义。ORE在跨语言批量编辑中显著优于基线，但其局部性指标仍低于参数编辑方法，且仅在7B-8B规模模型上验证，大规模模型下的几何约束有效性存疑。

】

---

【QueueEDIT: Structural Self-Correction for Sequential Model Editing in LLMs ｜队列自校正序列模型编辑

研究机构：合肥工业大学、美国东北大学

作者：Taolin Zhang、Haidong Kang、Dongyang Li 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_732b8ea80b3c)

> 序列模型编辑（Sequential Model Editing, SME）旨在连续修正大语言模型（LLMs）中的事实错误，但现有方法独立处理每次编辑，导致累积参数偏差破坏模型通用能力。本文指出，编辑间存在语义依赖（如总统变更需同步更新配偶信息），而现有定位-编辑范式忽略了这种时序关联。QueueEDIT通过结构映射编辑将三元组解耦至FFN层特定矩阵，并利用FIFO队列动态对齐历史编辑参数，在1000次编辑下显著优于基线。该方法在长序列稳定性上表现优异，但绝对可靠性仍低于单跳编辑SOTA，且未与最新零空间约束方法对比。

】

---

【Relaxing the Constraints: A Dual-Importance Projection Mechanism for Lifelong Model Editing ｜双重要性投影编辑

研究机构：厦门大学、清华大学

作者：Zhenghai Chen、Senbin Xu、Jiaxi Tan 等 11 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_01d69079fc63)

> 序列知识编辑旨在解决模型在连续更新中因参数累积干扰导致的旧知识遗忘与新知识泛化不足之间的矛盾。现有基于严格正交投影的方法虽能隔离历史知识，但过度约束梯度空间，导致长序列编辑下模型通用能力显著退化。DipEdit 通过引入累积重要性与投影重要性双机制，将硬正交约束转化为基于基向量重要性的软缩放投影，在保留关键历史知识的同时释放梯度表达空间。该方法在2000次连续编辑中实现了综合性能平均提升10.36%，但其有效性依赖于对输入激活子空间结构的假设，且在百万级超大规模编辑下的稳定性尚未得到验证。

】

---

【SpecEdit: A Spectral Approach for Multi-Round Knowledge Editing ｜谱结构感知的多轮知识编辑

研究机构：华南理工大学、浙江大学

作者：Junxian Liu、Zikun Deng、Xin Wu 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b08cee35f3c3)

> 多轮批量知识编辑中，模型内在知识与历史编辑记忆的耦合导致性能退化，现有闭式解方法忽略了二者在能量尺度与信息分布上的结构性差异。SpecEdit 通过谱解耦、信息补偿与谱融合三阶段重构二阶统计量，在不改变原有优化流程的前提下提升编辑稳定性。该方法在 CounterFact 基准上显著超越基线，但在 ZsRE 单跳任务上未达领域最优，其谱截断策略对编辑规模的敏感性仍存疑。

】

---

【The Model Agreed, But Didn't Learn: Diagnosing Surface Compliance in Large Language Models ｜表面合规诊断框架

研究机构：美国俄亥俄州立大学

作者：Xiaojie Gu、Ziying Huang、Weicong Hong 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.05995)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.05995)

> 知识编辑旨在以低成本更新大语言模型（LLM）中的过时事实，但现有评估体系依赖自由生成匹配，无法区分模型是真正重构了内部参数记忆还是仅学会了模仿目标输出。本文指出这种“表面合规”现象普遍存在，传统指标严重高估了编辑效果。通过引入判别式自评估协议与外部证据注入，该框架揭示了编辑后模型在上下文干扰下的脆弱性。这一诊断视角填补了从“输出正确”到“记忆内化”的评估空白，但其对递归编辑稳定性的量化仍停留在定性观察层面。

】

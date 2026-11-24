# ACL-Findings2026 · 机器学习理论与优化方向论文汇编

> 本方向共 48 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Adapt to Thrive! Adaptive Power-Mean Policy Optimization for Improved LLM Reasoning ｜自适应幂平均策略优化

研究机构：哈尔滨工业大学、香港中文大学

作者：Yiming Huang、Zhenbo Shi、Shuzheng Gao 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.04066)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_04c5a9ba5d1b)

> 强化学习后训练中，静态目标函数与固定裁剪阈值无法匹配模型推理能力的动态演化，导致早期探索不足或后期过拟合。现有方法如GRPO与GMPO分别陷入信号放大与保守稳定的两极，缺乏中间过渡机制。本文提出APMPO，通过性能驱动的幂平均指数与反馈稳定性分数动态调节优化行为。该方案在1.5B-3B模型上验证了自适应机制的有效性，但其对大模型规模及细粒度信用分配问题的适用性仍存疑。

】

---

【Adapting Where It Matters: Depth-Aware Adaptation for Efficient Multilingual Speech Recognition in Low-Resource Languages ｜深度感知模型适配

研究机构：澳大利亚墨尔本大学

作者：Yang Xiao、Eun-Jung Holden、Ting Dang

论文原文见 [arXiv](https://arxiv.org/abs/2602.01008)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.01008)

> 多语言语音识别（ASR）模型在低资源语言上性能骤降，核心矛盾在于全参数微调导致的灾难性遗忘与计算开销，而现有参数高效微调（PEFT）方法忽略模型内部层级功能差异，导致适应效率低下。本文切入点在于揭示语音基础模型中存在的“U型”层级可塑性模式，即中间层保留语言无关语义，首尾层承载语言特异性特征。通过提出深度感知模型适配（DAMA）框架，结合深度感知秩调度、SVD初始化与基保护投影，实现了对中间层语义空间的严格保护。该方法在极低资源场景下显著优于基线，但其对中间层“冻结”策略在复杂音素变化下的泛化边界尚存疑。

】

---

【Agent-Dice: Disentangling Knowledge Updates via Geometric Consensus for Agent Continual Learning ｜Agent-Dice：基于几何共识的参数融合框架

研究机构：上海交通大学

作者：Zheng Wu、Xingyu Lou、Xinbei Ma 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8a2ea586e066)

> 导读 LLM Agent在动态环境中持续适应新任务时，面临稳定性与可塑性的根本矛盾：过度保护旧知识阻碍新技能习得，而激进更新则引发灾难性遗忘。现有方法多依赖外部记忆模块或顺序迭代训练，但未能显式区分任务间的共同知识与冲突知识，导致信息干扰或丢失。Agent-Dice通过两阶段参数融合解决此问题：先以几何共识过滤剔除方向冲突的更新，再以曲率加权放大共享语义方向。该方法在GUI与工具使用Agent上验证了有效性，但其离线融合范式能否替代在线动态适应，仍存疑。

】

---

【Beyond Length Scaling: Synergizing Breadth and Depth for Generative Reward Models ｜混合推理机制的生成式奖励模型

研究机构：香港城市大学

作者：Qiyuan Zhang、Yufei Wang、Tianhe Wu 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.01571)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.01571)

> 生成式奖励模型（GRM）旨在通过自然语言理由替代标量分数以指导策略优化，但现有方法普遍陷入“长度即质量”的误区，导致推理机制与任务需求错配。本文指出，主观偏好与客观正确性需要正交的推理路径，提出Mix-GRM框架，通过模块化重组原始理由为广度（B-COT）与深度（D-COT）两种结构，并采用SFT与RLVR实现机制自适应。该框架在五个基准上刷新SOTA，但其在分布外数据上的泛化边界及模块化重组的幻觉风险尚未得到充分验证。

】

---

【Beyond Monolithic Rewards: Hybrid Multi-Aspect Reward Optimization ｜混合多面奖励优化

作者：Radha Gulhane、Sathish Reddy Indurthi

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4a7915cc79f3)

> 多模态强化学习长期受困于单一奖励模型在视觉-语言任务中的校准失效，导致策略优化陷入长度偏差或格式错误的局部最优。现有方案要么依赖高成本的全量奖励模型训练，要么在可验证任务中缺乏对主观质量的捕捉。本文切入点在于构建一个融合规则验证、模型评分与行为约束的混合奖励信号，以低成本实现多源信号的互补。该框架在3B模型上实现了9.48%的平均基准提升，但其对规则验证器准确性的强依赖及缺乏动态权重机制，限制了其在模糊边界任务上的泛化能力。

】

---

【Beyond Outcome Verification: Verifiable Process Reward Models for Structured Reasoning ｜可验证过程奖励模型

研究机构：IBM研究院

作者：Massimiliano Pronesti、Anya Belz、Yufang Hou

论文原文见 [arXiv](https://arxiv.org/abs/2601.17223)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.17223)

> 基于可验证奖励的强化学习（RLVR）旨在通过客观程序化验证器替代昂贵且主观的人类反馈，以低成本提升大语言模型在数学、代码等任务上的长思维链推理能力。然而，标准 RLVR 仅依赖结果级二元奖励，导致长序列中中间步骤的信用分配模糊，且现有过程监督依赖神经裁判，存在偏差与奖励黑客风险。本文切入点在于利用医学系统综述中风险偏倚评估任务的刚性规则结构，构建完全确定性的步骤级验证器。通过 GRPO 优化该可验证过程奖励，模型在 COCHRANEFOREST 数据集上取得 87.9% 的准确率，但该方法高度依赖领域指南的显式规则化，其向无明确规则结构的开放域任务泛化的能力存疑。

】

---

【Beyond Reasoning Gains: Mitigating General-Capability Forgetting in Large Reasoning Models ｜回放增强能力保持

作者：Hoang Phan、Xianjun Yang、Yuanshun Yao 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ff1f54630e9e)

> 基于可验证奖励的强化学习（RLVR）在提升大语言模型推理能力的同时，常导致预训练阶段习得的通用感知与指令跟随能力发生灾难性遗忘。现有正则化手段如KL散度仅约束当前任务分布，无法保证跨域知识的保留，而静态数据混合策略又难以适应不同奖励信号的收敛速度差异。RECAP通过回放通用能力数据并基于收敛率与不稳定性动态重加权多目标损失，在无需额外模型的前提下平衡了推理增益与能力保持。该方法在多模态基准上验证了有效性，但其对纯文本长序列推理任务的泛化性及计算开销边界尚存疑。

】

---

【BV-Blend: Uncertainty-Weighted Historical Baselines for Stable Critic-Free RL with Verifiable Rewards ｜基于语义簇历史矩的不确定性加权优势估计

研究机构：吉林大学

作者：Yupeng Chang、Yuan Wu、Yi Chang

论文原文见 [arXiv](https://arxiv.org/abs/2606.28707)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.28707)

> 基于可验证奖励的强化学习（RLVR）旨在利用客观二元奖励替代昂贵的人工标注，以低成本提升大语言模型在数学等任务上的长思维链推理能力。当前主流算法组相对策略优化（GRPO）依赖组内奖励方差计算优势函数，在冷启动阶段因组内奖励全同导致方差为零，学习信号完全消失。本文切入点在于引入语义簇条件化的历史统计量，通过标准误（SEM）代理计算置信权重，动态混合当前组内统计与历史矩，从而在零方差组中维持非退化优势。该方案在Qwen2.5-Math-7B骨干上显著提升了训练稳定性与最终性能，但其对离线固定语义聚类的依赖在分布漂移下的鲁棒性存疑。

】

---

【CoMoL: Efficient Mixture of LoRA Experts via Dynamic Core Space Merging ｜核心空间混合LoRA专家

作者：Jie Cao、Zhenxuan Fan、Zhuonan Wang 等 11 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_10597fc9b9c1)

> 混合专家低秩适配（MoE-LoRA）旨在通过多个低秩矩阵捕捉互补特征以突破单一LoRA的表达瓶颈，但现有方法因专家参数冗余和实例级路由导致计算开销激增且适应粒度粗糙。本文切入点在于利用LoRA固有的低秩结构，将专家合并与路由操作从全维空间压缩至核心空间。具体做法是引入核心空间专家存储与核心空间路由机制，实现Token级细粒度适配。该框架在保持与标准LoRA相当参数量的同时提升了数学与代码任务性能，但其核心空间维度固定，未验证动态调整秩对复杂推理的增益。

】

---

【Context-Conditioned Masked LoRA: Dynamic Rank Routing for Compute-Efficient Parameter-Efficient Fine-Tuning ｜上下文条件掩码低秩适配

作者：Rifat Rafiuddin、Rafae Abdullah

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_adfec0cb95fc)

> 低秩适配（LoRA）通过冻结骨干并注入低秩矩阵实现参数高效微调，但固定秩导致每个 token 均执行全秩计算，参数效率未转化为计算效率。现有动态秩方法多在训练时分配或仅提供有限稀疏性，缺乏推理时逐样本的精确秩控制。本文提出 CCM-LoRA，通过轻量级路由器生成输入依赖的秩掩码，实现动态秩路由以削减适配器计算量。该方法在保持精度的同时显著降低推理 FLOPs，但路由器开销在短序列场景下仍构成瓶颈，且缺乏多任务干扰下的稳定性验证。

】

---

【CoopQ: Cooperative Game Inspired Layerwise Mixed Precision Quantization for LLMs ｜合作博弈驱动的层间混合精度量化

研究机构：美国加州大学尔湾分校

作者：Junchen Zhao、Ali Derakhshan、Jayden Kana Hyman 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.15455)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.15455)

> 大语言模型（LLM）在极低比特部署时，传统基于单层敏感度的混合精度量化因忽略层间误差传播导致精度崩塌。CoopQ 将量化建模为层间合作博弈，通过渐进量化估计 Shapley 值以捕捉交互效应，并利用混合整数线性规划求解全局最优位宽分配。该方法在 2-4 bit 区间显著降低了困惑度，但其离线计算开销与二元位宽限制构成了实际部署的边界。

】

---

【CPC-GRPO: Answer-Free Reinforcement Learning with Cross-Prompt Consensus Rewards ｜跨提示共识强化学习

作者：Gyunyeop Kim、Sangwoo Kang

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ae297bcb2391)

> 基于可验证奖励的强化学习（RLVR）在缺乏客观真值或外部验证器的开放域指令数据上失效，因为标准流程依赖精确匹配或执行器提供二元信号。现有无验证器方法如自置信度代理存在提示特异性偏差，无法区分“单提示拟合”与“语义一致性”。本文利用语义等价提示作为多视图观测，通过跨提示教师强制重打分构建共识奖励，实现无答案策略优化。该方法在3B-4B小模型上验证了内部一致性信号的可行性，但其奖励机制是否能在所有提示均错误时产生系统性偏差，仍缺乏理论约束。

】

---

【Disentangling Continued Pre-Training: Attention-Driven Routing and Semantic Hub Preservation in Language Adaptation ｜持续预训练中的注意力路由与语义枢纽保持机制

作者：Khanh-Tung Tran、Vinh-Khanh Tran、Barry O’Sullivan 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_bf82e7a97a59)

> 多语言大语言模型在低资源语言适应中面临核心矛盾：全参数更新易导致灾难性遗忘，而冻结主干又阻碍新知识注入。现有研究多聚焦于训练后的参数高效微调或架构隔离，忽视了持续预训练（CPT）过程中内部组件的动态演化机制。本文通过层交换与组件手术实验，揭示CPT通过“接口层”适应新语言分布，同时保持“语义枢纽”层语义不变的选择性适应机制。该工作提供了CPT机制的因果证据，但未验证该机制能否直接转化为更高效的微调策略。

】

---

【DPLoRA: A Dual-Pruning Framework based on ILP Optimization and Progressive Pruning for Parameter-Efficient LoRA Fine-Tuning ｜双剪枝低秩适配

作者：Changjun Park、Sejong Yoon、Jaekwang Kim

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_270f9ca2232c)

> 导读

】

---

【DRIV-EX: Counterfactual Explanations for Driving LLMs ｜驾驶大语言模型的反事实解释生成

研究机构：法国格勒诺布尔阿尔卑斯大学

作者：Amaia Cardiel、Eloi Zablocki、Elias Ramzi 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d015f88f7dad)

> 自动驾驶大语言模型（LLM）的决策过程缺乏透明度，传统思维链解释常被视为事后合理化而非因果驱动。现有离散优化方法在翻转决策时往往牺牲文本流畅性或语义邻近性，导致生成的反事实不可解释。DRIV-EX 通过解耦连续嵌入的梯度搜索与受控自回归解码，在保持文本连贯的前提下定位最小语义扰动。该方法在驾驶场景审计中有效暴露了模型对速度特征的隐性依赖，但其解释的因果忠实性受限于未显式建模外生噪声。

】

---

【Exploring Reasoning Reward Model for Agents ｜智能体推理奖励模型

研究机构：香港中文大学、美团

作者：Kaixuan Fan、Kaituo Feng、Manyuan Zhang 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.22154)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.22154)

> 智能体强化学习（Agentic RL）在长程多步任务中面临结果级奖励信号稀疏的瓶颈，导致模型无法区分高质量中间推理与彻底失败。现有过程奖励模型依赖高昂的人工标注或易受奖励黑客攻击，且仅提供标量分数，缺乏可操作的纠错指导。本文提出 Agent-RRM，通过生成式推理轨迹、针对性批评与整体评分的多维反馈，将文本批评与标量奖励统一整合进强化学习循环。该方案在 GAIA 等基准上显著提升了 8B 参数智能体的性能，但其奖励模型在无真值条件下的校准鲁棒性仍存疑。

】

---

【Faithfulness vs. Safety: Evaluating LLM Behavior Under Counterfactual Medical Evidence ｜医学反事实证据下的LLM忠实性与安全性边界评估

研究机构：美国德克萨斯大学奥斯汀分校、美国东北大学

作者：Kaijie Mo、Siddhartha Venkatayogi、Chantal Shaib 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.11886)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_612dc3e2602b)

> 在医疗问答中，大语言模型（LLM）被期望忠实于提供的证据上下文，但当证据本身是虚假或危险的（如声称海洛因降低乳腺癌风险）时，模型应如何响应？现有研究多关注有效证据下的推理准确率，忽略了证据与模型先验知识冲突时的行为模式。本文通过构建MEDCOUNTERFACT数据集，系统替换临床干预词为反事实刺激，评估9个前沿LLM在证据忠实性与安全护栏之间的权衡。结果显示，模型普遍盲目采纳反事实证据，缺乏对前提合理性的质疑能力，揭示了当前LLM在安全关键领域存在“忠实性压倒安全性”的系统性缺陷。

】

---

【FARSS: Fisher-Optimized Adaptive Low-Rank and Singular-Vector Selection for Knowledge-Preserving Fine-Tuning ｜基于Fisher信息的层感知低秩适配

作者：Renxing Chen、Ziwei Xiang、Peisong Wang 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_6306e8c6c70c)

> 参数高效微调（PEFT）在提升目标任务性能时，常因更新幅度过大而破坏预训练模型的世界知识，现有方法多采用均匀秩分配或基于梯度的重要性剪枝，忽视了Transformer层间对知识存储的敏感度差异。本文指出浅层权重对世界知识保持具有决定性作用，提出FARSS框架，通过Fisher信息量化层敏感度并实施反向秩分配，结合任务感知的奇异向量初始化，在固定参数预算下实现知识保持与任务适应的帕累托最优。该方法在多项基准上验证了其在平衡指标上的优势，但其对Fisher估计样本量的依赖及深层非线性曲率近似的有效性仍存疑。

】

---

【G-LoRA: Global-Local Decoupled Low-Rank Adaptation ｜全局-局部解耦低秩适配

研究机构：华东师范大学

作者：Jiahao Xiong、Yihong Huang、Yihe Liu 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_5a2794b04c93)

> 低秩适配（LoRA）在固定秩约束下难以处理单一权重矩阵内部的参数重要性差异，导致关键子区域表达力不足。现有动态秩方法多聚焦层间分配或稀疏化，缺乏矩阵内部的细粒度容量调控。G-LoRA 通过一阶泰勒近似识别高重要性子块，并采用全局-局部解耦架构将高秩预算集中于此，在相同参数预算下提升有效秩。该方法在数学与代码任务上显著优于基线，但其区域收缩机制对早期全局信息捕获的影响尚存疑。

】

---

【Good Reasoning Makes Good Demonstrations: Implicit Reasoning Quality Supervision via In-Context Reinforcement Learning ｜演示效用作为推理质量信号：上下文强化学习中的隐式奖励重加权

研究机构：复旦大学、中国科学院大学

作者：Tiehua Mei、Minxuan Lv、Leiyu Pan 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.09803)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.09803)

> 基于可验证奖励的强化学习（RLVR）旨在通过客观二元奖励提升大语言模型推理能力，但结果级奖励无法区分正确轨迹的推理质量，导致模型强化“碰巧正确”的低质逻辑。现有过程奖励模型（PRM）依赖昂贵的人工标注或外部评估器，难以规模化。本文提出利用策略模型自身的上下文学习能力（ICL）量化推理轨迹的“演示效用”，并将其转化为训练过程中的隐式奖励重加权机制。该方法在数学基准上提升了准确率与推理质量，但其对强模型生成演示集的依赖及跨领域泛化能力仍存疑。

】

---

【GROLE: Instance-Level Group Relative Optimization for LoRA Experts in Incremental Learning ｜实例级LoRA专家路由的增量学习框架

作者：Yongyi Liao、Wencan Lai、Jun Fang 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8d15b28a003d)

> 在线增量学习（Incremental Learning, IL）旨在让单一模型在数据流中持续获取新任务知识，同时避免灾难性遗忘（Catastrophic Forgetting, CF）并促进知识转移（Knowledge Transfer, KT）。现有基于低秩适应（Low-Rank Adaptation, LoRA）的方法要么通过正则化共享专家导致模糊边界下的遗忘，要么依赖任务ID路由独立专家从而阻断实例级知识复用。GROLE通过构建冻结的LoRA专家池，并利用基于群组相对优化（Group Relative Optimization, GRPO）的轻量级选择器，在推理时无需任务标签即可动态合并专家。该框架在文本分类基准上超越了多任务上界，但其对强化学习选择器在超长任务流下的可扩展性缺乏验证。

】

---

【Grouped Adaptive Weight Sharing (GAWS): An Inference-Efficient Adaptation Method for Large Language Models ｜分组自适应权重共享（GAWS）：未合并适配器的推理延迟优化

作者：Eman Alsuradi、Junhyun Lee、Kyenghun Lee 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ed41e93e9264)

> 导读 参数高效微调（PEFT）解决了大模型适配的计算与存储瓶颈，但主流方法如低秩适配（LoRA）在单请求、未合并场景下引入了显著的推理延迟，而现有系统级优化多依赖权重合并或批处理，无法直接应用于需保持适配器独立性的生产环境。本文切入点在于识别出LoRA延迟的根源并非参数数量，而是分段CUDA内核调用导致的启动开销。通过引入结构化Kronecker积分解，将双矩阵乘法压缩为单次分组矩阵乘法，在保持参数效率的同时大幅降低延迟。该方案在单请求场景下实现了帕累托最优，但其对非局部依赖的捕捉能力及在批量推理下的优势持续性存疑。

】

---

【Hebbian-Guided Bi-Directional Rank Adaptation for Parameter-Efficient Fine-Tuning ｜基于Hebbian协同的双向秩适应

研究机构：天津大学、电子科技大学

作者：Xing Zhao、Liu Yang、Xi-Le Zhao 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_83cc0601c2be)

> 低秩适配（Low-Rank Adaptation, LoRA）在微调大语言模型时，固定秩设计无法适配不同层对任务贡献的异构性，导致参数预算分配失衡。现有动态秩方法仅支持单向剪枝或扩展，难以同时解决冗余参数与容量不足问题。HeBiRA通过引入Hebbian启发的重要性评分，实现了秩的双向重分配，在GLUE基准上以89.80的平均准确率超越了仅剪枝的AdaLoRA（89.46）和仅扩展的IncreLoRA（88.90）。该方法验证了激活与梯度协同信号在秩选择中的有效性，但其理论推导基于线性假设，在复杂非线性任务中的泛化边界尚存疑。

】

---

【How to Allocate, How to Learn? Dynamic Rollout Allocation and Advantage Modulation for Policy Optimization ｜动态分配与优势调制优化强化学习

研究机构：美团、清华大学

作者：Yangyi Fang、Jiaye Lin、Xiaoliang Fu 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.19208)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.19208)

> 基于可验证奖励的强化学习（RLVR）旨在通过客观二元奖励提升大语言模型推理能力，但现有方法在计算资源分配与策略优化稳定性上存在固有缺陷。标准组相对策略优化（GRPO）采用均匀采样且缺乏对梯度动态的细粒度控制，导致高方差问题被低估而高置信度动作学习信号衰减。本文提出DynaMO框架，通过序列级动态预算分配与Token级梯度感知优势调制解决上述矛盾。该方法在多个数学基准上验证了理论有效性，但其对验证器完美性的假设及单一模型家族的评估范围限制了结论的普适性。

】

---

【HTMuon: Improving Muon via Heavy-Tailed Spectral Correction ｜重尾谱修正优化器

研究机构：美国达特茅斯学院、美国国际计算机科学研究所

作者：Tianyu Pang、Yujie Fang、Zihang Liu 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.10067)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.10067)

> Muon 优化器通过正交化实现谱均匀化，但其将动量矩阵所有奇异值归一化为 1 的操作抑制了权重矩阵经验谱密度（ESD）的重尾特性，违背了重尾自正则化（HT-SR）理论中“重尾谱与模型质量正相关”的结论，导致泛化性能受限。本文切入点在于识别出正交化对噪声主导方向的过度加权及谱尾部抑制效应，提出 HTMuon 通过奇异值幂次变换恢复重尾性。该方法在 LLaMA 预训练中显著降低困惑度，但 p 值选取缺乏自适应机制，且在小样本视觉任务上未超越基线，其泛化边界尚待厘清。

】

---

【HypEHR: Hyperbolic Modeling of Electronic Health Records for Efficient Question Answering ｜超球面电子健康记录问答

研究机构：美国石溪大学

作者：Yuyu Liu、Sarang Rajendra Patil、Mengjia Xu 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.21027)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.21027)

> 电子健康记录（EHR）问答旨在从患者纵向记录中回答自然语言临床问题，但现有主流方案要么依赖计算昂贵且难以本地部署的大语言模型（LLM），要么忽略临床数据固有的层级结构。本文切入点在于利用医学本体与患者轨迹的超球面几何特性，构建一个仅含22M参数的紧凑模型。通过Lorentz流形上的序列编码与几何一致交叉注意力，HypEHR在无需LLM的设定下实现了与LLM基线相当的性能。其价值在于验证了小模型在结构化数据上的潜力，但超球面计算的工程稳定性与生成式问答的扩展性仍存疑。

】

---

【HyperAdaLoRA: Accelerating LoRA Rank Allocation During Training via Hypernetworks without Sacrificing Performance ｜超网络加速低秩适配收敛

研究机构：美国哈佛大学、中国科学院大学

作者：Hao Zhang、Zhenjia Li、Runfeng Bao 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.02630)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.02630)

> 动态秩分配旨在解决固定秩 LoRA 在异构层间参数预算分配不均的问题，但现有 SVD 基方法因直接优化分解矩阵导致收敛缓慢且计算开销高。HyperAdaLoRA 切入这一瓶颈，利用基于注意力机制的超网络动态生成 SVD 分量，替代传统的反向传播更新。该方法在保持最终精度的前提下显著缩短了训练时间，但其引入的超网络参数量是否违背 PEFT 的极简初衷，以及其在复杂推理任务上的泛化边界，仍需进一步审视。

】

---

【Joint Optimization of Training Data and Policy in RLHF ｜联合优化训练数据与策略的强化学习

作者：Zhuohao Yu、Jiali Zeng、Weizheng Gu 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2152130824bb)

> 强化学习从人类反馈（RLHF）旨在弥合大语言模型输出与人类期望的偏差，但传统范式将训练问题视为固定输入，导致策略在缺乏显式规范的问题上探索空间受限，难以发现多样化的解题策略。现有方法通过增加同一固定问题的采样数量来提升多样性，但当问题本身缺乏行为标准或推理指引时，这种冗余采样提供的学习信号极为有限。本文提出联合优化数据与策略（Joint Optimization of Data and Policy, JODP）框架，利用策略模型自身生成多样化的问题规范（Specifications），并通过多臂老虎机算法动态选择有效规范以引导Rollout生成，同时保持奖励计算基于原始问题以防止目标漂移。该方法以极低的计算开销实现了4B模型接近8B模型的性能，但其有效性依赖于规范生成质量与任务复杂度的匹配，且在开放式非验证任务中的泛化能力尚未得到充分验证。

】

---

【Less Noise, More Voice: Reinforcement Learning for Reasoning via Instruction Purification ｜干扰Token净化与校准强化学习

研究机构：中国人民大学、丹麦奥胡斯大学

作者：Yiju Guo、Tianyi Hu、Zexu Sun 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.21244)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.21244)

> 基于可验证奖励的强化学习（Reinforcement Learning with Verifiable Rewards, RLVR）在复杂推理任务中常因正确轨迹采样率极低导致训练停滞，现有方案通过增加采样量或过滤零方差提示词缓解此问题，但前者算力成本高昂，后者牺牲了困难样本的探索机会。本文指出，许多采样失败并非源于题目难度，而是由提示词中少量引入干扰的Token导致。LENS框架通过识别并移除这些干扰Token，将去噪提示词下生成的成功轨迹迁移回原始提示词进行策略校准，从而在不增加算力的前提下提升探索效率。该方法在数学推理基准上实现了性能与收敛速度的帕累托改进，但其对提示词语义完整性的依赖及在开放域任务中的泛化能力尚存疑。

】

---

【Low-probability Tokens Sustain Exploration in Reinforcement Learning with Verifiable Reward ｜低概率Token正则化

研究机构：清华大学、北京大学

作者：Guanhua Huang、Tingqiang Xu、Mingze Wang 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.03222)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.03222)

> 导读 强化学习可验证奖励（RLVR）旨在通过客观二元奖励提升大语言模型的长思维链推理能力，但训练常因策略熵坍缩导致性能平台期。现有熵控制方法试图通过全局随机性维持探索，却往往放大无关噪声并加速崩溃。本文识别出低概率探索性Token（Reasoning Sparks）被系统性消除是核心瓶颈，提出低概率正则化（Lp-Reg）通过构建过滤噪声的代理分布进行KL散度约束，精准保护关键Token。该方法在Qwen3-14B上实现了60.17%的平均准确率，但其在非数学任务及弱骨干模型上的泛化能力尚存疑。

】

---

【MedCPI: A Construct–Personalize–Integrate Framework for KG-enhanced Clinical Prediction ｜任务引导式知识图谱增强临床预测框架

研究机构：英国埃克塞特大学

作者：Hang Wang、Hang Dong、Lu Liu

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_7151df4fd0d7)

> 电子健康记录（EHR）数据稀疏且异构，传统序列模型难以捕捉细粒度临床语义，而直接引入多源医学知识图谱（MKG）又面临Schema噪声与任务无关性干扰。现有方法在知识提取与患者个性化环节缺乏针对性控制，导致弱相关节点稀释预测证据。MedCPI通过“构建-个性化-整合”三阶段框架，利用大语言模型（LLM）进行任务引导的Schema归纳，并实施受控局部扩展构建患者级知识图谱，实现了知识选择与纵向时序的动态对齐。该框架在MIMIC-III/IV上取得了SOTA性能，但其对LLM离线归纳的依赖及跨机构泛化能力仍存疑。

】

---

【MMR-GRPO: Accelerating GRPO-Style Training through Diversity-Aware Reward Reweighting ｜基于最大边际相关性的多样性感知奖励重加权

研究机构：美国德州农工大学

作者：Kangda Wei、Ruihong Huang

论文原文见 [arXiv](https://arxiv.org/abs/2601.09085)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.09085)

> 组相对策略优化（GRPO）在训练数学推理模型时，因生成大量语义冗余的完成样本导致计算资源浪费，且现有动态采样方法虽减少步数却因单步耗时增加而未降低总墙钟时间。MMR-GRPO 通过引入信息检索中的最大边际相关性（MMR）机制，在优势函数计算阶段对语义相似的完成样本进行惩罚性降权，从而提升单步更新的信息密度。该方法在保持峰值性能可比的前提下，平均减少 47.9% 的训练步数与 70.2% 的墙钟时间，但其对高难度竞赛数学任务的精度增益有限，且未解决细粒度信用分配的根本缺陷。

】

---

【N-GRPO: Embedding-Level Neighbor Mixing for Enhanced Policy Optimization ｜语义邻居混合策略优化

研究机构：浙江大学

作者：Xukun Zhu、Hang Yu、Peng Di 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.10768)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.10768)

> 组相对策略优化（GRPO）在强化学习后训练中依赖高质量轨迹探索，但Token级采样易陷入语义冗余，而直接注入Embedding噪声又会导致语义漂移。本文指出连续表示空间缺乏内在随机性，提出在Rollout阶段通过混合锚点Token与其语义邻居的Embedding来注入可控扰动。该方法在保持局部语义一致性的前提下扩展了探索空间，在DeepSeek-R1-Distill-Qwen模型上提升了数学推理基准的Pass@k指标，但其增益主要源于探索多样性而非信用分配精度的提升，在高难度任务上的性能上限仍受限于序列级奖励机制。

】

---

【OpenGenAlign: A Preference Dataset and Benchmark for Trustworthy Reward Modeling in Open-Ended, Long-Context Generation ｜长上下文开放生成的偏好数据基准

作者：Hanning Zhang、Juntong Song、Juno Zhu 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_5ad0865e86f1)

> 长上下文开放生成缺乏专用偏好数据与评估基准，导致通用奖励模型在幻觉与全面性维度上失效。现有方法依赖通用对话数据训练，无法捕捉长文本特有的质量权衡，本文通过o3多维评估构建领域特定数据集填补空白。其核心贡献是提供33K高质量偏好对及1.5K测试集，验证了领域数据对策略优化的增益。该工作确立了长上下文奖励建模的数据基线，但o3标注噪声对模型鲁棒性的影响尚未量化。

】

---

【Polynomial Expansion Rank Adaptation: Enhancing Low-Rank Fine-Tuning with High-Order Interactions ｜多项式扩展秩适应

研究机构：安徽大学、中国科学技术大学

作者：Wenhao Zhang、Lin Mu、Li Ni 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.11841)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.11841)

> 低秩适应（LoRA）通过冻结预训练权重并注入低秩矩阵实现高效微调，但其双线性更新形式仅捕捉一阶线性依赖，难以建模高阶参数交互。现有方法如 HiRA 依赖外部权重耦合，DoRA 侧重幅值方向解耦，均未在低秩因子内部引入显式非线性。PERA 通过在低秩因子空间执行结构化多项式展开，生成平方与交叉项，在不增加秩或推理开销的前提下提升表达力。该方法在常识推理与 NLU 任务上优于基线，但评估范围局限于语言理解，且高阶项的优化稳定性缺乏理论保证。

】

---

【RanLoRA: Residual-aware Nonlinear Low-Rank Adaptation ｜残差感知非线性低秩适配

研究机构：美国南加州大学

作者：Xu Luo、Yongbin Liu、Chunping Ouyang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_da3b5118e652)

> 低秩适配（LoRA）在复杂推理任务上受限于线性子空间的表达瓶颈，单纯增加秩或引入全局非线性模块往往导致参数冗余与预训练知识破坏。RanLoRA 通过奇异值分解（SVD）显式解耦预训练权重的主成分与残差，仅对残差路径施加轻量级非线性调制，在极低参数预算下实现了性能突破。该方法在常识推理与数学推理任务上显著优于同参数量基线，但其非线性结构对推理延迟的影响及在简单任务上的泛化边界仍需进一步审视。

】

---

【RePrompT: Recurrent Prompt Tuning for Integrating Structured EHR Encoders with Large Language Models ｜递归提示调优整合结构化电子健康记录编码器与大语言模型

研究机构：美国堪萨斯大学

作者：Arya Hadizadeh Moghaddam、Drew Ross、Mohsen Nayebi Kerdabadi 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17725)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17725)

> 大语言模型（LLM）在处理结构化电子健康记录（EHR）时面临时序结构丢失与群体模式缺失的双重困境，导致其难以捕捉临床轨迹的纵向依赖与跨患者共性。现有方法要么依赖文本线性化而忽略时间维度，要么孤立推理而无法利用群体统计特征。RePrompT 通过状态递归提示与结构编码提示的双软提示机制，在不修改 LLM 架构的前提下实现了时序感知与群体对齐。该方法在 MIMIC-III/IV 上优于传统 EHR 基线，但精度显著低于当前 SOTA，且缺乏对知识图谱等外部语义增强的利用，其临床部署价值仍受限于骨干模型能力与融合机制的瓶颈。

】

---

【Rethinking Parameter Sharing for LLM Fine-Tuning with Multiple LoRAs ｜非对称低秩适配：共享B矩阵的多任务与联邦微调

研究机构：美国纽约州立大学布法罗分校

作者：Hao Ban、Kaiyi Ji

论文原文见 [arXiv](https://arxiv.org/abs/2509.25414)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.25414)

> 多LoRA微调中，共享内部矩阵$A$以降低参数开销是主流策略，但现有方法忽略了$A$与$B$在训练动力学中的功能差异。本文发现$A$的相似性源于初始化而非知识共享，且$A$存在“惰性学习”现象，阻碍特征子空间探索。通过反转共享对象，设计共享$B$、独立$A$的非对称架构，并扩展至异构联邦场景。该设计在保持精度的同时显著降低通信成本，但共享$B$是否成为单任务性能瓶颈尚存疑。

】

---

【Reward Yourself: Efficient Self Rewards for Trustworthy Sampling ｜自奖励可信采样

作者：Mingjie Li、Wai Man Si、Michael Backes 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_657a157c0c03)

> 现有奖励模型在隐私与偏见等可信任务上表现不佳，甚至劣于贪心解码，而重新训练奖励模型成本高昂。本文切入点在于不训练新模型，而是通过剪枝现有大语言模型（LLM）构建“可信”与“不可信”双变体，利用其对数似然比作为辅助奖励信号。具体做法是集成到Best-of-N采样流程中，先过滤低分候选，再由外部奖励模型选择最终答案。该方法在隐私任务上提升10-20%拒绝率，但仅在特定可信域验证，通用基准有效性未证实。

】

---

【SAMoRA: Semantic-Aware Mixture of LoRA Experts for Task-Adaptive Learning ｜语义感知混合LoRA专家

研究机构：北京交通大学、中国科学院

作者：Boyan Shi、Wei Chen、Shuyuan Zhao 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.19048)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.19048)

> 导读 多任务大语言模型微调面临专家同质化与更新强度僵化的双重瓶颈，现有混合专家低秩适配（Mixture-of-Experts Low-Rank Adaptation, MoE-LoRA）方法依赖隐式路由与全局固定缩放，导致不同任务间参数干扰严重。SAMoRA 通过引入显式语义匹配路由与任务自适应缩放机制，将输入语义与专家能力直接对齐，并动态调节各任务的更新幅度。该框架在常识推理与通用语言理解基准上以更低的可训练参数比例超越了主流基线，但其对大规模模型及多模态场景的适用性尚未得到验证。

】

---

【Save the Good Prefix: Precise Error Penalization via Process-Supervised RL to Enhance LLM Reasoning ｜可验证前缀策略优化

研究机构：腾讯AI实验室、美国弗吉尼亚大学

作者：Haolin Liu、Dian Yu、Sidi Lu 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.18984)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.18984)

> 导读 基于可验证奖励的强化学习（RLVR）旨在通过客观二元反馈提升大语言模型（LLM）的长思维链推理能力，但稀疏的结果级奖励导致长序列中正确中间步骤被错误惩罚，引发严重的信用分配难题。现有过程奖励模型（PRM）虽能提供步级监督，但其连续评分噪声大且缺乏明确基准，直接作为奖励信号易导致策略优化偏离。本文提出VPPO，将PRM重构为“首个错误定位器”，仅利用其识别首个错误步骤的能力，对错误前的正确前缀赋予额外奖励，对错误后缀施加惩罚。该设计在AIME等基准上同时提升了Pass@1与Pass@K，但方法强依赖特定的步骤枚举格式，且裁剪长度的选择缺乏普适性理论支撑。

】

---

【Semantic-Space Exploration and Exploitation in RLVR for LLM Reasoning ｜语义空间探索与利用解耦的强化学习

研究机构：清华大学、美国加州大学洛杉矶分校

作者：Fanding Huang、Guanbo Huang、Xiao Fan 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.23808)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.23808)

> 基于可验证奖励的强化学习（RLVR）旨在通过客观二元奖励提升大语言模型（LLM）的长思维链推理能力，但现有方法普遍陷入探索-利用权衡的困境。主流方案依赖 token 级动作空间统计量（如熵、置信度）作为代理指标，导致策略分布锐化与解多样性坍缩，且无法区分语义进展与局部采样噪声。本文指出该权衡是测量假象，提出在隐藏状态语义空间定义有效秩（ER）及其时间导数，实现探索与利用的解耦。通过构建速度利用秩学习（VERL）方法动态调节优势函数，本文在多个基准上验证了同时提升探索与利用的可行性，但其计算开销与跨域泛化能力仍存疑。

】

---

【Stable On-Policy Distillation through Adaptive Target Reformulation ｜稳定在线策略蒸馏的目标重构

研究机构：韩国首尔大学

作者：Ijun Jang、Jewon Yeom、Juan Yeo 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.07155)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.07155)

> 在线策略蒸馏（On-Policy Distillation, OPD）旨在通过让学生模型在自身生成的轨迹上学习，解决传统监督蒸馏中训练与推理分布不匹配导致的暴露偏差。然而，早期学生策略的高噪声特性使得直接匹配教师分布时，前向KL散度引发梯度爆炸，反向KL散度则导致模式坍塌，现有数据层面的混合策略未能解决优化目标本身的几何不稳定性。本文提出Veto，通过在Logit空间构建师生分布的几何插值目标，以单一参数$\beta$统一调控梯度抑制与多样性保留。该方法在低资源设定下显著提升了数学推理与代码生成性能，但其对超参数$\beta$的敏感性及小数据规模下的泛化能力仍存疑。

】

---

【Think Outside the Policy: In-Context Steered Policy Optimization ｜上下文引导策略优化

研究机构：北京大学

作者：Hsiu-Yuan Huang、Chenming Tang、Weijie Liu 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.26519)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.26519)

> 组相对策略优化（GRPO）在强化学习后训练中面临探索空间受限于当前策略分布的瓶颈，导致轨迹多样性不足与局部最优收敛。现有通过引入外部强模型轨迹的方法虽能扩展探索，但伴随高昂计算成本与数据噪声风险。本文利用大语言模型固有的上下文学习能力，将现有数据集作为隐式专家引导，生成离策略轨迹并混入组内优化，同时通过拒绝采样与退火奖励整形稳定训练。该方法在数学推理基准上实现了显著的性能提升，但其对基础模型上下文学习能力的依赖程度及跨领域泛化边界仍需进一步验证。

】

---

【Unlocking Exploration in RLVR: Uncertainty-aware Advantage Shaping for Deeper Reasoning ｜不确定性感知优势整形

研究机构：快手

作者：Can Xie、Ruotong Pan、Xiangyu Wu 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.10649)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.10649)

> 组相对策略优化（Group Relative Policy Optimization, GRPO）在可验证奖励强化学习（Reinforcement Learning with Verifiable Rewards, RLVR）中因消除价值网络依赖而成为主流，但其序列级均匀优势分配导致信用分配粗糙，引发策略熵坍缩与探索停滞。现有熵正则化方法往往采取全局保守策略，无法区分“正确但不确定”的探索路径与“错误但自信”的固化路径。UCAS 利用模型内部 Logit 信号，在响应级与 Token 级实施非对称优势整形，以恢复探索多样性。该方法在数学推理基准上显著优于基线，但其 Token 级粒度在极端难度任务上的有效性仍存疑。

】

---

【Verifiable Parameterization of Bayesian Networks from Scientific Literature: Unlocking Unstructured Empirical Evidence ｜从统计摘要重构贝叶斯网络参数

研究机构：德国慕尼黑工业大学

作者：Jonas Gottal、Florian Matthes

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_fc9b1fe8bfe4)

> 贝叶斯网络（Bayesian Network, BN）的完整功能依赖于结构（DAG）与参数（条件概率表, CPT）的双重完备，但现有参数学习算法严重依赖原始表格数据，而科学文献中大量以t检验、相关系数等形式存在的聚合统计量无法被直接利用。本文提出了一种基于约束优化与Copula建模的框架，将非结构化的统计摘要转化为可验证的CPT重构问题。通过对比五种策略，Copula-based方法在合成基准上实现了最优的重构保真度与决策效用。该工作填补了从文献证据到功能化BN参数的空白，但其在真实数据中因约束稀疏导致的性能波动，暴露了统计摘要信息密度不足的根本局限。

】

---

【Verifier-Free RL for LLMs via Intrinsic Gradient-Norm Reward ｜无验证器强化学习中的内在梯度范数奖励

研究机构：浙江大学

作者：Xuexiang Wen、Hang Yu、Linchao Zhu 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.09920)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.09920)

> 导读 大语言模型后训练长期依赖外部可验证奖励（RLVR），但这一范式在缺乏标准答案或程序化验证器的开放域任务中失效。现有无验证器方法多基于多数投票或模型置信度，前者受限于答案提取的可靠性，后者在训练后期易出现奖励退化与性能坍塌。本文提出 VIGOR，将策略模型对生成序列的 teacher-forced 负对数似然梯度范数转化为内在奖励，通过长度校正与组内秩归一化实现无标签强化学习。该方法在 Qwen2.5-7B-Base 上较最强无验证器基线提升 3.31% 数学平均准确率，但其在长序列与复杂算法任务上的泛化能力仍存疑。

】

---

【Why LoRA Fails to Forget: Regularized Low-Rank Adaptation Against Backdoors in Language Models ｜正则化低秩适配（RoRA）：基于谱强度与对齐的后门遗忘机制

作者：Hoang-Chau Luong、Lingwei Chen

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_6a2e9f17c74a)

> 导读 大语言模型微调中的后门攻击防御长期面临一个核心矛盾：全参数微调虽能覆写中毒权重，但计算成本高昂，而低秩适配（LoRA）因参数冻结导致后门行为难以消除。现有防御多依赖外部检测或知识蒸馏，缺乏对LoRA内在遗忘机制的原理解释。本文从谱视角切入，指出LoRA脆弱性源于谱强度不足与谱对齐不良，而非单纯的低秩约束，并提出通过正则化增强谱分量、正交化触发器方向及后训练重缩放来主动遗忘后门。该工作为PEFT安全提供了新的理论框架，但其有效性高度依赖特定攻击类型与模型架构，在复杂推理任务上的泛化能力存疑。

】

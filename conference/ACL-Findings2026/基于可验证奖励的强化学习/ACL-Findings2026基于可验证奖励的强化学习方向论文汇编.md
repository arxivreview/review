# ACL-Findings2026 · 基于可验证奖励的强化学习方向论文汇编

> 本方向共 12 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

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

【CPC-GRPO: Answer-Free Reinforcement Learning with Cross-Prompt Consensus Rewards ｜跨提示共识强化学习

作者：Gyunyeop Kim、Sangwoo Kang

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ae297bcb2391)

> 基于可验证奖励的强化学习（RLVR）在缺乏客观真值或外部验证器的开放域指令数据上失效，因为标准流程依赖精确匹配或执行器提供二元信号。现有无验证器方法如自置信度代理存在提示特异性偏差，无法区分“单提示拟合”与“语义一致性”。本文利用语义等价提示作为多视图观测，通过跨提示教师强制重打分构建共识奖励，实现无答案策略优化。该方法在3B-4B小模型上验证了内部一致性信号的可行性，但其奖励机制是否能在所有提示均错误时产生系统性偏差，仍缺乏理论约束。

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

【Good Reasoning Makes Good Demonstrations: Implicit Reasoning Quality Supervision via In-Context Reinforcement Learning ｜演示效用作为推理质量信号：上下文强化学习中的隐式奖励重加权

研究机构：复旦大学、中国科学院大学

作者：Tiehua Mei、Minxuan Lv、Leiyu Pan 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.09803)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.09803)

> 基于可验证奖励的强化学习（RLVR）旨在通过客观二元奖励提升大语言模型推理能力，但结果级奖励无法区分正确轨迹的推理质量，导致模型强化“碰巧正确”的低质逻辑。现有过程奖励模型（PRM）依赖昂贵的人工标注或外部评估器，难以规模化。本文提出利用策略模型自身的上下文学习能力（ICL）量化推理轨迹的“演示效用”，并将其转化为训练过程中的隐式奖励重加权机制。该方法在数学基准上提升了准确率与推理质量，但其对强模型生成演示集的依赖及跨领域泛化能力仍存疑。

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

【Verifier-Free RL for LLMs via Intrinsic Gradient-Norm Reward ｜无验证器强化学习中的内在梯度范数奖励

研究机构：浙江大学

作者：Xuexiang Wen、Hang Yu、Linchao Zhu 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.09920)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.09920)

> 导读 大语言模型后训练长期依赖外部可验证奖励（RLVR），但这一范式在缺乏标准答案或程序化验证器的开放域任务中失效。现有无验证器方法多基于多数投票或模型置信度，前者受限于答案提取的可靠性，后者在训练后期易出现奖励退化与性能坍塌。本文提出 VIGOR，将策略模型对生成序列的 teacher-forced 负对数似然梯度范数转化为内在奖励，通过长度校正与组内秩归一化实现无标签强化学习。该方法在 Qwen2.5-7B-Base 上较最强无验证器基线提升 3.31% 数学平均准确率，但其在长序列与复杂算法任务上的泛化能力仍存疑。

】

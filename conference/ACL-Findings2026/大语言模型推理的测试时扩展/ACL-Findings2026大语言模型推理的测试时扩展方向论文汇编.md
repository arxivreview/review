# ACL-Findings2026 · 大语言模型推理的测试时扩展方向论文汇编

> 本方向共 18 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【A Few Bad Apples Spoil the Bunch: Preventing Global Entropy Collapse Driven by a Small Set of Tokens in LLM Reasoning ｜结构感知熵坍缩优化

作者：Jaeeun Jang、Hansle Lee、Sangmin Kim

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b17ccd6aff8e)

> 强化学习后训练在提升大语言模型单样本推理准确率的同时，往往导致推理路径多样性坍缩，进而削弱测试时扩展（Test-Time Scaling, TTS）的有效性。现有熵正则化方法多采用均匀或启发式策略，未能精准定位引发全局熵衰减的局部关键节点。本文通过 GRPO 策略优化的 logit 坐标精确分解，识别出仅占 5% 的“分支定义”token 是熵坍缩的主要驱动力，并据此实施选择性 KL 正则化。该方法在数学推理基准上同时提升了 Pass@1 与 Pass@k，但其在非可验证任务及更大规模模型上的泛化能力尚存疑。

】

---

【A Reward-Guided Dual-Phase Framework for Adaptive Inference-Time Reasoning ｜双阶段奖励引导自适应推理框架

研究机构：美国密歇根州立大学、美国宾夕法尼亚州立大学

作者：Yingqian Cui、Zhenwei Dai、Pengfei He 等 12 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_45e989c92b7a)

> 测试时扩展（Test-Time Scaling, TTS）旨在通过增加推理阶段计算量提升大语言模型（LLM）的复杂任务表现，但现有基于过程奖励模型（Process Reward Model, PRM）的树搜索方法通常将规划与执行视为单一节点，导致资源分配与错误传播特性不匹配。本文指出规划步骤的不确定性与执行步骤的错误致命性存在本质差异，统一搜索策略在此结构下效率次优。DREAM 框架将推理显式解耦为规划与执行两个独立搜索阶段，并引入基于实时奖励反馈的动态预算分配机制，在数学与代码生成任务上实现了准确率与计算效率的双重优化。该框架在中等规模骨干模型上验证了阶段解耦的有效性，但其对大规模强化学习训练模型的适用性及理论边界尚存疑。

】

---

【Adaptive Test-Time Compute Allocation with Evolving In-Context Demonstrations ｜自适应测试时计算分配与动态上下文演示

研究机构：美国加州大学河滨分校、美国印第安纳大学

作者：Bowen Zuo、Dongruo Zhou、Yinglun Zhu

论文原文见 [arXiv](https://arxiv.org/abs/2604.21018)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.21018)

> 测试时扩展（Test-Time Scaling, TTS）旨在通过增加推理阶段算力提升大语言模型（LLM）性能，但现有方法多采用静态采样分布或均匀算力分配，导致在异构难度数据集上效率低下。本文指出，仅决定“在哪分配算力”而忽略“如何改变生成分布”是性能瓶颈的关键。作者提出一种两阶段框架，通过自适应性上下文学习（In-Context Learning, ICL）动态重塑条件生成分布，实现算力分配与分布适应的统一。该方法在多个基准上以更低算力成本超越基线，但其效果高度依赖可验证任务中的真值反馈，在不可验证场景下的泛化能力存疑。

】

---

【ARISE: An Adaptive Resolution-Aware Metric for Test-Time Scaling Evaluation in Large Reasoning Models ｜自适应分辨率感知扩展评估指标

研究机构：复旦大学、南京大学

作者：Zhangyue Yin、Qiushi Sun、Zhiyuan Zeng 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.06014)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.06014)

> 测试时扩展（Test-Time Scaling, TTS）旨在通过增加推理算力提升大语言模型性能，但现有评估手段无法量化“算力投入与准确率提升”的真实效率，且对性能随算力增加而下降的负向扩展现象视而不见。Muennighoff et al. (2025) 提出的斜率指标在负向扩展时存在病理行为，且仅关注全局准确率，忽略了样本级的错误转化。本文提出 ARISE 指标，通过样本级轨迹追踪与基于方差的动态采样机制，实现对 TTS 效率的细粒度、稳定量化。该指标在区分模型扩展能力上优于传统斜率指标，但其分数与实际任务准确率的直接映射关系尚未建立。

】

---

【Chain-in-Tree: Back to Sequential Reasoning in LLM Tree Search ｜树搜索中的链式推理：分支必要性评估

作者：Xinzhe Li

论文原文见 [arXiv](https://arxiv.org/abs/2509.25835)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.25835)

> 大语言模型在复杂推理任务中依赖测试时扩展（Test-Time Scaling, TTS）提升性能，但基于树搜索的框架因固定粒度分支导致计算效率低下。现有方法在每一步均强制生成多个候选路径，忽略了平凡步骤无需探索的事实，造成大量冗余调用。本文提出 Chain-in-Tree (CiT)，通过引入分支必要性（Branching Necessity, BN）评估模块，动态决定何时分支、何时链式推进。该方法在保持准确率基本无损的前提下，将推理时间降低 75–85%，但 BN 评估器的质量成为性能稳定性的关键瓶颈。

】

---

【Chronos: Learning Temporal Dynamics of Reasoning Chains for Test-Time Scaling ｜时序推理链评分器

研究机构：中国科学技术大学

作者：Kai Zhang、Jiayi Liao、Chengpeng Li 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a399516fda38)

> 测试时扩展（Test-Time Scaling, TTS）旨在通过增加推理阶段的计算量提升大语言模型（LLM）的复杂任务性能，但并行采样后的聚合环节常因忽视轨迹质量差异而失效。现有方法多采用均匀投票或静态置信度加权，无法捕捉推理过程中的时序动态，导致正确但低频的答案被错误过滤。本文提出 Chronos，一种基于多尺度卷积的轻量级时序评分器，将轨迹的 Token 概率序列建模为时间序列以评估其逻辑一致性。该方法在无需额外训练骨干模型的前提下显著提升了聚合精度，但其性能上限仍受限于骨干模型的初始推理能力，且跨域泛化能力有待进一步验证。

】

---

【ConMA : Confidence-Guided Kernel Sampling with Multi-Stage Aggregation for LLM Reasoning ｜置信度引导的多阶段聚合

作者：Yinuo Wang、Qingjie Li、Wenyao Cui 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0fa845c14578)

> 测试时扩展（Test-Time Scaling, TTS）旨在通过增加推理阶段的计算量来提升大语言模型（LLM）的复杂推理能力，但现有主流方法依赖外部验证器或一次性独立采样，导致算力分配僵化且无法复用中间高质量轨迹。本文切入点在于利用模型内部的token概率置信度作为筛选信号，构建无训练、无验证器的迭代精炼循环。具体做法是将固定预算划分为多轮“采样-过滤-扩展-选择”过程，通过动态剪枝与条件化探索实现早期收敛。该方法在4B小模型上显著提升了数学推理精度与效率，但其对复杂开放域任务的泛化能力及理论收敛边界尚存疑。

】

---

【DeepPrune: Parallel Scaling without Inter-trace Redundancy ｜跨轨迹冗余剪枝

研究机构：清华大学、上海科技大学

作者：Shangqing Tu、Yaxuan Li、Yushi Bai 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.08483)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.08483)

> 并行推理扩展旨在通过生成多条思维链（Chain-of-Thought, CoT）提升大语言模型（LLM）的推理准确率，但现有方法忽略了轨迹间的答案同质性，导致大量算力浪费在生成等价路径上。本文指出约80%的并行轨迹最终答案相同，且浅层语义相似度无法有效预测这种等价性。DeepPrune通过训练专用裁判模型预测未完成轨迹的答案等价性，结合在线贪心聚类动态剪枝冗余路径，在保持准确率的前提下大幅降低Token消耗。该方法在效率维度实现了显著突破，但其对可验证任务域的依赖及裁判模型的泛化边界仍存疑。

】

---

【Efficient Test-Time Scaling via Temporal Reasoning Aggregation ｜时序推理聚合实现收敛退出

研究机构：北京航空航天大学

作者：Jiakun Li、Xingwei He、Kefan Li 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17304)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17304)

> 测试时扩展（Test-Time Scaling, TTS）旨在通过增加推理计算提升大语言模型（LLM）性能，但常引发过度思考（Overthinking），即模型生成远超必要的推理链。现有动态早期退出方法依赖单步置信度信号，该信号在多步推理中因缺乏跨步稳定性而失效，导致过早或过晚终止。TRACE 通过滑动窗口聚合答案一致性与置信度轨迹，构建时序收敛判据以替代瞬时信号。该方法在无需训练的前提下实现了效率与精度的平衡，但其对极难任务中错误答案持续出现的鲁棒性仍存疑。

】

---

【Hidden States as Early Signals: Step-level Trace Evaluation and Pruning for Efficient Test-Time Scaling ｜基于隐状态与内存约束的推理轨迹剪枝

研究机构：美国伊利诺伊大学厄巴纳-香槟分校

作者：Zhixiang Liang、Beichen Huang、Zheng Wang 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.09093)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.09093)

> 并行采样通过生成多条推理路径提升准确率，但长轨迹与多路径叠加导致算力成本与端到端延迟激增，且现有剪枝信号（相似度、置信度）无法可靠区分正确与错误轨迹。本文切入点在于发现隐状态在推理早期即包含质量判别信号，且延迟瓶颈主要来自 GPU 内存饱和引发的排队而非 Token 生成本身。STEP 训练轻量级评分器评估步骤质量，并以内存饱和为触发条件动态剪枝低分轨迹。该方法在降低延迟 45%–70% 的同时提升准确率，但其效果高度依赖特定硬件配置与内存压力场景，通用性存疑。

】

---

【Prompting Test-Time Scaling Is A Strong LLM Reasoning Data Augmentation ｜提示测试时扩展

作者：Sondos Mahmoud Bsharat、Zhiqiang Shen

论文原文见 [arXiv](https://arxiv.org/abs/2510.09599)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.09599)

> 大语言模型推理能力的提升长期依赖大规模思维链语料的标注与收集，但静态提示易导致模型过拟合特定解题模板，且在领域偏移下泛化能力受限。现有推理时扩展方法多聚焦于解码参数调整或答案聚合，忽视了提示空间本身的组合潜力。本文提出 P-TTS，通过原则性指令包装对少量种子问题进行系统性提示变异，将测试时提示转化为数据增强手段。该方法以 90 个种子样本实现了超越 1K 静态提示的效果，但其本质是低资源监督微调策略，而非直接的推理时算力扩展，其理论边界与 RL 训练的对比优势尚存疑。

】

---

【Scaling Evaluation-Time Compute with Reasoning Models as Evaluators ｜评估时扩展：推理模型作为评估器

研究机构：美国卡内基梅隆大学、美国伊利诺伊大学厄巴纳-香槟分校

作者：Seungone Kim、Ian Wu、Jinu Lee 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2503.19877)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_997df2a4cad0)

> 测试时扩展（Test-Time Scaling, TTS）通常用于提升生成器解决复杂问题的准确率，但评估器在重排候选答案时同样面临算力与精度的权衡。传统过程奖励模型（Process Reward Model, PRM）依赖大规模过程监督训练，且固定预算下难以适应不同难度任务的评估需求。本文提出将推理模型直接作为评估器，通过强制其生成更长的思维链（Chain-of-Thought, CoT）来扩展评估时算力，无需额外训练即可超越专用PRM。该范式验证了评估精度随推理token单调提升的规律，但在高难度开放域任务上的泛化边界尚存疑。

】

---

【Seer Self-Consistency: Advance Budget Estimation for Adaptive Test-Time Scaling ｜预分配预算的自适应测试时扩展

作者：Shiyu Ji、Yixuan Wang、Yijun Liu 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0814b8f15d6f)

> 测试时扩展（Test-Time Scaling, TTS）旨在通过增加推理计算提升大语言模型（LLM）性能，但固定预算导致简单任务算力浪费，动态预算方法又因串行估计产生高延迟。现有自适应一致性方法在生成过程中实时停止，无法利用现代推理引擎的并行优势，导致Token效率与延迟无法同时优化。SeerSC 引入快速直觉推理（System 1）预估答案熵，在深思推理（System 2）执行前预分配采样预算，实现了并行生成下的动态扩展。该方法在保持精度的同时显著降低计算成本，但其熵估计在复杂多步推理中的预测稳定性尚存疑。

】

---

【Test-Time Scaling in Multimodal Foundation Models: A Comprehensive Survey of Generation and Reasoning ｜多模态基础模型测试时扩展综述

研究机构：中山大学

作者：Cong Wan、Ying He、Zhongzhan Huang 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.08231)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.08231)

> 多模态基础模型在推理阶段面临感知证据、空间定位与时间上下文的多维计算分配难题，单纯复用文本模型的扩展策略无法解决模态间隙导致的验证失效。现有研究缺乏统一分类框架以厘清采样、反馈与搜索策略在多模态场景下的适用边界。本文构建了首个针对多模态基础模型测试时扩展的系统性综述，提出包含采样、反馈与搜索三大范式的统一分类体系。该工作填补了多模态测试时扩展的理论空白，但缺乏对算力预算与性能收益的量化对比分析。

】

---

【The Best of Both Worlds: Combining Parallel and Sequential Inference Scaling via Aggregation Fine-Tuning ｜聚合微调

作者：Yafu Li、Zhilin Wang、Tingchen Fu 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_3ec6b6677d37)

> 大语言模型在推理时扩展计算以提升性能，但并行采样依赖外部验证器，串行修正则受限于高延迟。现有方法难以在无外部监督下同时利用并行多样性与串行深度。本文提出聚合微调（AFT），通过监督学习使模型内化“将多个草稿响应整合为单一精炼答案”的能力，并在推理时通过“提议-聚合”迭代策略扩展计算。该范式在开放域指令跟随任务上实现了无验证器的性能提升，但其对复杂数学推理任务的泛化能力存疑。

】

---

【Towards Inference-time Scaling for Continuous Space Reasoning ｜连续空间推理的测试时扩展失效机制分析

作者：Minghan Wang、Thuy-Trang Vu、Ehsan Shareghi 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.12167)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_82be9e0d4eb2)

> 测试时扩展（Test-Time Scaling, TTS）旨在通过增加推理阶段计算量提升大语言模型（LLM）性能，但现有方法主要局限于离散Token空间。连续空间推理模型（如COCONUT）虽提升了效率，却因确定性生成导致轨迹单一，无法直接应用TTS。本文通过引入Dropout采样生成多样连续轨迹，并训练过程/结果奖励模型（PRM/ORM）进行重排序，发现现有离散空间迁移的奖励模型在连续空间中失效。这一发现揭示了连续思维缺乏几何可分性的根本瓶颈，为后续设计具有结构区分性归纳偏置的训练框架提供了实证依据。

】

---

【VecCISC: Improving Confidence-Informed Self-Consistency with Reasoning Trace Clustering and Candidate Answer Selection ｜基于推理轨迹聚类的置信度自一致性优化

研究机构：美国布兰迪斯大学

作者：James Petullo、Sonny George、Dylan Cashman 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.08070)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.08070)

> 推理时扩展（Test-Time Scaling, TTS）旨在通过增加计算资源提升大语言模型（LLM）的推理准确率，但“二次思考”（Think Twice）范式因需对每条采样轨迹调用批评者模型进行置信度评分，导致推理开销呈线性激增。现有方法如置信度自一致性（Confidence-Informed Self-Consistency, CISC）虽提升了准确率，却未区分冗余或幻觉轨迹，造成算力浪费。本文提出 VecCISC，通过嵌入向量聚类筛选语义等价轨迹，仅对代表样本进行评分，在维持准确率的同时大幅降低 token 消耗。该方法在通用问答任务上验证了有效性，但在高难度数学竞赛任务上的泛化能力存疑。

】

---

【When More Thinking Hurts: Overthinking in LLM Test-Time Compute Scaling ｜测试时计算扩展中的边际效用递减与过度思考

研究机构：南京大学

作者：Shu Zhou、Rui Ling、Junan Chen 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.10739)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.10739)

> 测试时计算扩展（Test-Time Scaling, TTS）旨在通过增加推理阶段的计算资源提升大语言模型（LLM）的复杂推理能力，但现有研究普遍隐含“思考越长越好”的单调性假设。该假设导致模型在简单问题上浪费算力，在复杂问题上陷入自我否定的“过度思考”陷阱，且传统评估指标无法区分准确率提升与计算成本增加之间的权衡。本文通过引入“翻转事件”追踪与成本感知效用函数，系统量化了推理长度与答案质量间的非线性关系，揭示了边际效用递减及最优停止点随问题难度显著变化的规律。这一工作为TTS从“盲目扩展”转向“自适应分配”提供了关键的实证基础与评估框架，但其结论局限于特定开源模型与数学/科学任务，对私有模型及非推理任务的普适性尚未验证。

】

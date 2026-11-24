# ACL-Findings2026 · GRPO变体与策略优化增强方向论文汇编

> 本方向共 5 篇（ACL-Findings2026）。按论文标题字母序排列。
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

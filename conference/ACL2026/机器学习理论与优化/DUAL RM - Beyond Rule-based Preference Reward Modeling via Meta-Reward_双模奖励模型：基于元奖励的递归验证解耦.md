# ACL2026最新论文 ｜DUAL RM: Beyond Rule-based Preference Reward Modeling via Meta-Reward ｜双模奖励模型：基于元奖励的递归验证解耦

作者：Xiaobo Liang、Wanfu Wang、Qipeng Huang 等 11 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_df87d008a2e1)

> 奖励模型（Reward Model, RM）在强化学习对齐中面临“验证器需要验证器”的递归依赖困境，即Matryoshka Doll Problem，导致对人工标注的持续高成本依赖。现有生成式奖励模型（Generative Reward Model, GenRM）虽提供可解释性，但缺乏对推理轨迹有效性的客观度量，而判别式奖励模型（Discriminative Reward Model, DisRM）虽评分精准却缺乏推理深度。本文提出DUAL RM，通过耦合GenRM的推理预测与DisRM的观测评分构建非参数化元奖励，实现无外部监督的自校准。该方法在8B参数规模下显著提升了偏好判断准确率，但其性能上限受制于固定DisRM的偏差传递，且跨模态迁移的鲁棒性边界尚待明确。

## 研究背景

当大型语言模型（Large Language Models, LLMs）进行策略优化时，奖励模型作为代理目标存在固有的不完美性，容易引发奖励黑客。为缓解此问题，研究者引入元验证器（Meta-verifier）来评估RM本身的可靠性，但这导致了递归依赖：验证器本身也需要更高层级的验证，最终不得不依赖昂贵且易引入偏差的人工标注。这种递归结构在缺乏可验证奖励的场景中尤为致命，因为它阻碍了RM在开放域任务中的自主进化。

主流路线中，标量RM通过去偏技术提升鲁棒性，但牺牲了细粒度反馈能力；生成式RM通过自然语言理由增强可解释性，却面临推理轨迹质量难以量化的问题。过程奖励模型（Process Reward Model, PRM）虽提供步骤级信用分配，但其高标注成本限制了在开放域任务中的扩展性。DUAL RM的切入点在于打破递归验证链条，借鉴人类认知中“行动结果作为最终监督信号”的机制，将元奖励定义为GenRM预测的响应质量提升与DisRM观测到的实际质量变化之间的差异，从而在不依赖额外人工标注的情况下，实现RM推理能力的自监督优化。

## 核心方法

### 方法参照系

标准生成式奖励建模流程中，RM直接输出标量分数或自然语言判断，缺乏对判断有效性的内省机制。本文问题与该通用流程的关键差异在于：它不直接优化RM对偏好的拟合，而是优化RM识别关键评估维度（Rubric）的能力，并通过外部观测器闭环校准这一过程。

### 元奖励形式化

传统元验证器依赖参数化模型或启发式规则，易引入复合误差。本文创新在于将元奖励定义为GenRM预测改进与DisRM观测变化的差异，解决了推理轨迹有效性无法直接度量的失效。给定查询 $Q$ 和响应 $R_1, R_2$，GenRM生成基于Rubric $J_i$ 的判断轨迹 $\tau_i$，并预测响应改进。DisRM对原始及改进后的响应评分，元奖励 $s_{meta}(\tau_i)$ 定义为：

$$
s_{meta}(\tau_i) = \begin{cases}
\hat{s}_1^i - s_1, & \text{if } J_i = 0 \text{ and } \hat{s}_1^i < \hat{s}_2^i \\
\hat{s}_2^i - s_2, & \text{if } J_i = 0 \text{ and } \hat{s}_1^i > \hat{s}_2^i \\
\hat{s}_1^i - s_1, & \text{if } J_i = 1 \text{ and } \hat{s}_1^i > \hat{s}_2^i \\
\hat{s}_2^i - s_2, & \text{if } J_i = 1 \text{ and } \hat{s}_1^i < \hat{s}_2^i
\end{cases}
$$

该公式量化了Rubric $J_i$ 引导下的预测改进与实际观测改进的一致性，高 $s_{meta}$ 值表明该Rubric能有效区分响应质量，从而为策略优化提供可靠监督。

### 基于Rubric的测试时缩放

标准测试时缩放（Test-Time Scaling, TTS）通过多次采样取平均，但忽略了不同Rubric的重要性差异，导致简单投票在复杂子集上性能退化。本文创新在于引入Rubric规划-选择解耦工作流，利用元奖励筛选最优Rubric，解决了Rubric多样性与有效性冲突的问题。在GRPO变体中，优势函数 $A_i$ 通过元奖励归一化与真值正确性重映射计算：

$$
r_i = \begin{cases}
\beta (\tilde{r}_i + 1), & \text{if } J_i = \text{ground truth} \\
\beta \tilde{r}_i, & \text{otherwise}
\end{cases}
$$

其中 $\tilde{r}_i$ 为元奖励的Min-Max归一化值，$\beta$ 为缩放因子。该设计将粗粒度的二元结果奖励转化为细粒度的轨迹质量反馈，使模型能区分“正确但推理低质”与“正确且推理高质”的轨迹，提升了信用分配的精度。

## 实验评估

实验在RewardBench、RM-Bench和Omni-RewardBench上进行，基线覆盖GPT-4o、DeepSeek-R1及Omni-RewardModel等SOTA，但缺失针对去偏RM（如Causal Debiasing）的直接对比。

| 方法 | 规模 | RewardBench Avg | RM-Bench Avg | Omni-RewardBench Avg |
| :--- | :--- | :--- | :--- | :--- |
| GPT-4O | - | 91.8 | 86.2 | 76.04 |
| DeepSeek-R1 | 671B | 89.3 | 78.8 | - |
| Omni-RewardModel BT | - | - | - | 73.93 |
| DUAL RM (GRPO w/ meta-verifier) | 8B | 91.1 | 77.4 | 74.51 |

DUAL RM在RewardBench上达到91.1%，超越GPT-4O的91.8%仅差0.7个百分点，且在8B规模下显著优于同规模基线Qwen3-VL-8B的82.2%。在Omni-RewardBench上，其74.51%的平均准确率接近GPT-4O的76.04%，展示了跨模态迁移能力。

消融实验显示，引入Consistency元奖励函数后，Rubric排序曲线平滑且校准良好。将Rubric数量从10扩展至60，平均准确率从85.76提升至93.23，表明Rubric缩放有效。然而，在Chat_Hard和Reasoning子集上，简单投票聚合导致性能退化，证实了不同Rubric捕捉的评估维度存在冲突，必须通过元奖励筛选而非简单聚合。

评估边界方面，论文未报告置信区间，且RewardBench上的高分可能部分源于Qwen3-VL骨干本身的能力，而非元奖励机制。代码已开源，但DisRM固定为Skywork-Reward-V2，其自身偏差可能通过元奖励传递，限制了GenRM的上限。

## 关联研究分析

从问题动机看，DUAL RM与Omni-RewardModel（Jin et al., 2025）均关注多模态奖励建模，但前者通过跨模态迁移实现参数效率，后者依赖多模态数据训练。DUAL RM在仅训练语言模态的情况下，在Omni-RewardBench上达到74.51%，接近Omni-RewardModel BT的73.93%，表明Rubric作为评估维度的通用性可能优于模态特异性特征。然而，这种迁移是否在所有模态组合中均有效，论文未给出回答。

从方法设计看，DUAL RM与过程奖励模型（PRM）如R-PRM（EMNLP 2025）均提供细粒度反馈，但PRM依赖步骤级人工标注，而DUAL RM通过元奖励自监督生成Rubric重要性。PRM在数学任务上F1分数达63.6%，但标注成本高；DUAL RM在开放域任务上通过自校准降低数据依赖，但其元奖励的无偏性在缺乏人工标注时如何保证，是潜在盲区。

## 总结

DUAL RM要解决的核心矛盾是奖励模型验证中的递归依赖与人工标注成本。其切入点在于利用GenRM与DisRM的耦合构建非参数化元奖励，将验证信号从抽象的元验证转向可观测的响应质量变化。该方法通过Rubric规划-选择解耦和基于元奖励的策略优化，在8B规模下实现了RewardBench 91.1%和Omni-RewardBench 74.51%的性能。其边界在于DisRM作为固定观测器，其自身偏差可能限制GenRM的进化上限，且跨模态迁移的鲁棒性仅在特定基准上验证。当DisRM的评分分布发生漂移时，元奖励的校准能力是否仍能保持，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_df87d008a2e1)
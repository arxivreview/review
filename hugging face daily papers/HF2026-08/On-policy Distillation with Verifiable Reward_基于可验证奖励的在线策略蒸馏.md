# HuggingFace最新推荐论文 ｜On-policy Distillation with Verifiable Reward ｜基于可验证奖励的在线策略蒸馏

研究机构：清华大学、北京航空航天大学

作者：Wenze Lin、Jiale Zhao、Xitai Jiang 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2608.24696)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2608.24696)

> 在线策略蒸馏（On-policy Distillation, OPD）与基于可验证奖励的强化学习（Reinforcement Learning with Verifiable Rewards, RLVR）分别提供密集Token级指导与稀疏任务级正确性信号，但二者独立使用时存在信号冲突或性能上限。现有融合方法多依赖加权组合或启发式切换，引入额外超参数且未解决底层奖励符号与轨迹正确性不一致的问题。本文提出OPDVR，通过ReLU门控机制强制奖励符号与验证器结果对齐，将OPD转化为合法的RLVR方法。该方法无需额外超参数，但在教师模型能力上限与低置信区间信息截断方面存在潜在局限。

## 研究背景

当大语言模型在数学推理任务中生成长思维链时，最终答案的二元正确性反馈无法区分中间步骤的对错，导致信用分配困难。为缓解此问题，在线策略蒸馏（OPD）利用教师模型提供密集的Token级概率分布指导，但其目标纯粹是分布匹配，不关心生成结果是否正确，导致学生模型性能被教师模型上限锁死。RLVR则通过规则验证器提供客观的任务级奖励，但信号稀疏，难以指导长序列中的具体Token行为。

RLVR与OPD的互补性促使研究者尝试融合二者。主流路线包括直接加权两个损失函数（如Hubotter et al., 2026），或根据优势函数符号选择性应用其中一种方法（如Wang et al., 2026）。这些方法虽然有效，但引入了平衡超参数，且未从数学层面解决OPD隐含奖励与RLVR奖励原则的冲突。本文切入点在于重新审视采样Token OPD的梯度形式，发现其隐含奖励符号由教师-学生概率比决定，而非轨迹正确性，这违反了RLVR中“正确轨迹应获正奖励”的基本原则。

## 核心方法

### 方法参照系

本文问题属于信用分配机制类别，旨在解决长序列中稀疏奖励导致的中间步骤学习信号不足。与标准RLVR仅使用二元轨迹奖励不同，本文引入教师-学生概率比作为Token级权重；与标准OPD无验证器不同，本文引入验证器门控以约束奖励方向。关键差异在于将分布匹配信号转化为符合RLVR原则的奖励信号。

### 隐含奖励的重构与冲突识别

标准采样Token OPD的损失函数为 $L_{\text{sample}}^{\text{OPD}}(\theta) = \mathbb{E}_{o \sim \pi_\theta} \left[ \sum_{t=1}^{|o|} \log \frac{\pi_\theta(o_t | q, o_{<t})}{\pi_T(o_t | q, o_{<t})} \right]$。通过对比RLVR梯度 $\nabla_\theta J(\theta) = \mathbb{E} [R \cdot \nabla_\theta \log \pi_\theta(o|q)]$，可发现OPD梯度中的对数比项 $\log(\pi_T/\pi_\theta)$ 充当了隐含的Token级奖励 $R_{\text{OPD}}(o_t)$。然而，该奖励符号由 $\pi_T$ 与 $\pi_\theta$ 的相对大小决定，与轨迹正确性无关。在正确轨迹中，若学生置信度高于教师（$\pi_\theta > \pi_T$），隐含奖励为负，导致模型惩罚正确行为；在错误轨迹中，若教师置信度高于学生（$\pi_T > \pi_\theta$），隐含奖励为正，导致模型强化错误行为。这种符号冲突是标准OPD无法超越教师上限且可能损害任务性能的根本原因。

### ReLU门控机制与GRPD变体

为解决符号冲突，本文提出OPDVR，对隐含奖励应用ReLU门控：

$$
R_{\text{OPDVR}}(o_t) = \begin{cases}
\max\left(0, \log \frac{\pi_T(o_t | q, o_{<t})}{\pi_\theta(o_t | q, o_{<t})}\right) \cdot (+1), & \text{if trajectory correct} \\
\max\left(0, \log \frac{\pi_\theta(o_t | q, o_{<t})}{\pi_T(o_t | q, o_{<t})}\right) \cdot (-1), & \text{if trajectory incorrect}
\end{cases}
$$

该公式确保正确轨迹上的奖励非负，错误轨迹上的奖励非正。具体而言，正确轨迹中教师比学生更自信的Token获得更强奖励，强化可靠预测；错误轨迹中学生比教师更自信的Token受到更重惩罚，抑制过度自信的错误。这一机制将OPD转化为合法的RLVR方法，使其可与GRPO等算法无缝集成。结合GRPO的组相对优势估计，本文提出Group Relative Policy Distillation (GRPD)，在保持密集指导的同时利用组内归一化降低方差。

## 实验评估

实验在AIME24、AIME25、AMC、MATH500、GSM8K、LiveCodeBench等六个基准上进行，基线包括标准OPD、GRPO、PPO。论文未提供具体数值表格，仅通过图1示意OPDVR在AIME24、AIME25、AMC上优于OPD。据领域综述，AIME24 SOTA为PIPO 55.31%，MATH500 SOTA为SDPO 73.2%，本文未与这些2025-2026前沿方法对比，仅定性优于标准OPD。

消融实验未提供详细数据，但方法设计表明ReLU门截断可能丢失教师信号在低置信区间的信息。例如，当正确轨迹中 $\pi_T < \pi_\theta$ 时，门控将奖励置零，学生无法从教师获得“降低置信度”的指导，这可能影响分布匹配的完整性。此外，GRPD变体依赖GRPO的组内方差，若组内奖励全对或全错，优势函数为零，梯度消失，这与标准GRPO的局限一致。

评估边界方面，论文未报告置信区间，数值比较需谨慎。代码已开源（github.com/LeapLabTHU/OPDVR），但缺乏统一的GPU小时数对比，计算效率未充分评估。教师模型的选择对性能影响显著，但论文未探讨不同教师能力上限对学生超越可能性的限制。

## 关联研究分析

从问题动机看，本文与SC-GRPO均实现Token级信用分配，但SC-GRPO通过自条件教师模型测量原始策略与条件策略间的KL散度，无需外部教师，而本文依赖外部教师模型。SC-GRPO的自监督特性避免了教师质量瓶颈，但计算复杂度较高；本文的ReLU门控更简单，但受限于教师能力。从方法设计看，本文与Token Hidden Reward (THR) 均无需外部过程奖励模型（PRM），但THR基于GRPO学习动态识别隐藏奖励，本文基于教师-学生概率比。THR的奖励信号来自策略梯度更新中的隐含信号，而本文的信号来自教师分布，两者在信号来源与计算开销上存在差异。

## 总结

本文核心矛盾在于OPD的分布匹配目标与RLVR的任务正确性目标在Token级奖励符号上的冲突。现有加权或启发式方法未解决此冲突，本文通过ReLU门控强制奖励符号与验证器结果一致，将OPD转化为合法RLVR方法。实验表明OPDVR在六个基准上优于标准OPD，但未提供具体数值与前沿方法对比。边界在于教师模型能力上限可能限制学生超越，且ReLU截断可能丢失低置信区间信息。当教师模型在特定Token上置信度低于学生时，门控置零是否导致分布匹配失效，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2608.24696)
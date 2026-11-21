# HuggingFace最新推荐论文 ｜Not Every Token Is Worth Distilling: Selective Supervision for Direct-OPD ｜选择性监督的在线策略蒸馏

研究机构：华东师范大学、Hugging Face

作者：Yibo Zhao、Zixuan Yang、Yunshi Lan 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2609.29142)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2609.29142)

> 在线策略蒸馏（On-Policy Distillation, OPD）旨在让学生模型在自生成轨迹上接收教师模型的密集监督，以缓解训练与推理分布的失配。然而，基于强化学习（RL）策略偏移的Direct-OPD方法存在概率质量失配缺陷，导致低效监督。本文通过引入Jensen-Shannon散度（JSD）筛选高价值状态，仅对Top-10%状态施加监督，在不增加计算开销的前提下提升了泛化性能。该方法在数学推理任务上验证了有效性，但其对非数学领域及不同架构模型的泛化能力尚存疑。

## 研究背景

自回归语言模型在推理时依赖自身生成的前缀，而训练时通常使用教师或真实标签，这种训练-推理分布的不一致导致误差累积，即曝光偏差。在线策略蒸馏（OPD）通过让学生模型在自采样轨迹上学习教师分布来解决此问题。然而，当教师模型是通过强化学习（RL）优化得到时，其相对于预训练参考模型的策略偏移（Policy Shift）成为关键监督信号。Direct-OPD利用RL后教师与参考模型之间的Token级对数比率（Log-ratio）作为奖励，将其视为密集监督信号传递给更大的学生模型。

传统OPD假设教师分布本身即为最优目标，但近期研究指出，RL带来的策略偏移比教师绝对性能更具迁移价值，尤其是当学生模型规模大于教师时（Weak-to-Strong蒸馏）。Direct-OPD和Proxy-OPD等方法提取这种偏移作为奖励，避免了在大规模学生模型上运行昂贵RL的需求。然而，对数比率仅衡量相对变化，忽略了概率质量的绝对值。当教师与参考模型在学生候选Token上的概率质量同时趋近于零时，对数比率可能保持恒定，导致Direct-OPD在教师行为几乎未发生变化的状态下仍施加强监督，造成无效甚至有害的梯度更新。

## 核心方法

### 方法参照系

Direct-OPD的标准流程是在学生自采样的每个状态 $s_t$ 上，计算教师 $\pi_T$ 与参考模型 $\pi_{ref}$ 对Token $v$ 的对数比率 $\Delta_t(v|s_t) = \log \frac{\pi_T(v|s_t)}{\pi_{ref}(v|s_t)}$，并以此作为奖励最大化学生策略。该流程假设所有状态上的策略偏移均具有同等迁移价值，未区分教师行为变化的显著性。

### 概率质量失配的理论界定

Direct-OPD的失效源于其对数比率奖励对概率质量不敏感。本文构造了一个精确的反例：当教师与参考模型在学生Top-K候选集 $V_K$ 上的概率质量 $\epsilon$ 趋近于0时，尽管两者分布差异消失（JSD与双向KL散度均趋于0），但候选Token的对数比率 $\Delta_t(v|s_t)$ 保持非零常数。这意味着Direct-OPD的梯度更新 $g_t^R$ 在教师行为未发生实质变化的状态下依然显著。为量化这种“行为变化”，本文引入Jensen-Shannon散度（JSD）作为状态评分指标。JSD具有对称性、有界性（$\le \log 2$）且在零概率下有限，其值直接界定了教师与参考模型在任意事件集上的总变差距离（Total Variation Distance, TVD）：

$$
|P(A) - Q(A)| \le D_{TV}(P, Q) \le \sqrt{2 D_{JS}(P, Q)}
$$

该不等式表明，低JSD状态必然对应教师行为的微小变化，从而为筛选无效监督提供了理论依据。

### 基于JSD的选择性监督机制

基于上述理论，S2D-OPD在Direct-OPD框架中引入状态掩码机制。对于学生采样的每个状态 $s_t$，计算其在Top-K候选集及剩余残差Token $v_o$ 上的压缩分布 $\tilde{\pi}_T, \tilde{\pi}_{ref}$，并计算JSD得分 $\tilde{d}_t = D_{JS}(\tilde{\pi}_T(\cdot|s_t) \| \tilde{\pi}_{ref}(\cdot|s_t))$。在每条响应内部，保留JSD得分最高的 $k = \lceil \rho |T| \rceil$ 个状态（默认 $\rho=0.1$），形成掩码集合 $I$。修改后的目标函数仅在掩码状态上计算Direct-OPD损失：

$$
J_{S2D-OPD}(\theta) = \mathbb{E}_{x \sim D, (s_t, y_t) \sim \pi_\theta} \left[ \Delta_t(y_t|s_t) - \alpha D_{KL}[\pi_\theta(\cdot|s_t) \| \pi_{stu}(\cdot|s_t)] \mid m_t = 1 \right]
$$

其中 $m_t = 1$ 当且仅当 $t \in I$。该设计无需额外前向传播，因为JSD计算复用了Direct-OPD已获取的教师与参考模型概率。通过剔除低JSD状态，S2D-OPD消除了教师行为未显著变化时的无效梯度，将监督资源集中于策略偏移显著的状态，从而提升了迁移效率与训练稳定性。

## 实验评估

实验在AIME 2024/25/26及HMMT 2025/2026基准上进行，使用Qwen3-1.7B/4B/8B及R1-Distill-7B作为学生，R1-Distill-1.5B→JustRL-1.5B与Nemotron-1.5B→QuestA-1.5B作为教师对。基线仅对比Dense Direct-OPD，未包含SeqKD或GKD等经典蒸馏方法，因任务设定为Weak-to-Strong策略偏移迁移，与标准分布拟合任务不同。

| 学生模型 | 教师对 | 方法 | AIME26 | HMMT | Test Avg. |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Qwen3-1.7B | JustRL | Direct-OPD | 45.4 | 32.0 | 36.4 |
| Qwen3-1.7B | JustRL | S2D-OPD | 47.4 | 32.9 | 37.6 |
| Qwen3-4B | QuestA | Direct-OPD | 70.4 | 47.1 | 54.6 |
| Qwen3-4B | QuestA | S2D-OPD | 70.7 | 49.3 | 56.2 |
| R1-Distill-7B | JustRL | Direct-OPD | 56.8 | 32.8 | 40.5 |
| R1-Distill-7B | JustRL | S2D-OPD | 55.0 | 33.6 | 40.5 |

S2D-OPD在8个设置中的7个提升了Test Avg.，平均增益0.95点（95% CI: 0.40–1.54）。消融实验显示，随机保留10%状态的性能（51.2）与Dense Direct-OPD（51.3）持平，证实了OPD的“数据过剩”特性；而按JSD分位保留Top-10%状态达到52.9，显著优于随机选择。JSD分位与验证准确率呈对数线性关系（$R^2=0.97$），表明高散度状态是性能提升的主要来源。

评估仅覆盖数学推理任务，缺乏代码生成或自然语言理解的横向对比。代码已开源，但超参数细节（如KL系数 $\alpha$ 的自适应策略）仅在附录中简要提及，复现需仔细核对。

## 关联研究分析

从问题动机看，S2D-OPD与ExOPD（Yang et al., 2026）均关注教师策略偏移，但ExOPD通过外推教师改进构造超越教师的目标，而S2D-OPD通过筛选现有偏移中的高价值部分。ExOPD假设偏移可线性外推，而S2D-OPD指出偏移的“质量”（概率质量）比“方向”（对数比率）更关键。这一差异源于对RL策略偏移稀疏性的不同理解：S2D-OPD认为大部分状态上的偏移是噪声，需过滤；ExOPD则认为偏移是信号，需放大。

从方法设计看，S2D-OPD与GKD（Agarwal et al., 2024）同属OPD路线，但GKD使用教师分布作为目标，S2D-OPD使用教师-参考差异作为奖励。GKD的全位置监督假设教师分布处处有效，而S2D-OPD通过JSD筛选打破了这一假设。S2D-OPD的筛选机制类似课程学习，但基于状态散度而非数据难度。这种设计在教师-学生容量差距大时可能更有效，但在教师分布本身高度一致时，筛选可能过度剔除有效信号，论文未对此边界条件进行充分测试。

## 总结

S2D-OPD针对Direct-OPD中Log-ratio奖励与概率质量失配导致的无效监督问题，提出基于JSD的状态筛选机制。通过仅对Top-10%高散度状态施加监督，该方法在8个Weak-to-Strong设置中的7个提升了泛化准确率，平均增益0.95点。其核心贡献在于揭示了低散度状态对迁移的冗余性与潜在危害，并通过理论构造证明了JSD作为筛选指标的有效性。然而，实验仅局限于数学推理任务，且未对比标准OPD变体如GKD，限制了结论的普适性。当教师与参考模型在大部分状态上分布高度一致时，JSD筛选是否会导致监督信号过度稀疏，进而影响学生模型对基础能力的继承，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2609.29142)
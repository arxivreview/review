# ICLR2026最新论文 ｜RESCHED: Rethinking Flexible Job Shop Scheduling from a Transformer-based Architecture with Simplified States ｜ReSched：基于Transformer与简化状态的柔性车间调度框架

研究机构：新加坡管理大学、新加坡南洋理工大学

作者：Xiangjie Xiao、Cong Zhang、Wen Song 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.07020)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.07020)

> 柔性车间调度问题（FJSP）的核心矛盾在于，传统深度强化学习（DRL）方法依赖冗余的析取图特征与复杂的图神经网络（GNN）架构，导致模型泛化能力受限且计算开销巨大。现有方案在状态表示上过度依赖历史构建数据，在架构上受限于GNN的局部归纳偏置，难以捕捉长距离依赖。ReSched 通过重构马尔可夫决策过程（MDP）状态空间，将特征精简至4个核心节点属性，并采用双分支Transformer架构替代GNN，实现了跨规模与跨变体的强泛化。该框架在FJSP基准上刷新了SOTA，但其对机器-操作反向反馈的缺失及负Gap结果的成因，仍存疑。

## 研究背景

FJSP 要求将作业分解为操作序列，并在兼容机器集合中进行分配与排序，其目标是最小化最大完工时间（Makespan）。这一过程可建模为MDP，其中状态需完整编码当前部分解的约束信息。传统方法通常使用析取图表示状态，节点特征往往超过20个，包括历史构建数据、空闲时间等辅助变量。然而，这些特征不仅冗余，且引入历史依赖会破坏马尔可夫性，导致策略在分布外（OOD）场景下性能衰减。

主流DRL路线如 DANIEL 和 HGNN 采用双注意力或异构图神经网络来捕捉操作与机器间的交互，但这类架构依赖复杂的特征工程，且GNN的局部消息传递机制难以高效建模非局部依赖。此外，基于人工启发式的动作剪枝虽提升了效率，却限制了策略的探索空间，阻碍了泛化。ReSched 的切入点在于挑战“复杂特征必要”的假设，提出通过子问题视角消除历史依赖，并用通用Transformer架构替代GNN，以极简状态换取更强的表达能力与泛化性。

## 核心方法

### 方法参照系

FJSP 的DRL求解标准流程通常包括：构建析取图状态、设计GNN骨干提取特征、通过策略网络选择操作-机器对。ReSched 的关键差异在于摒弃了析取图中的冗余节点特征与历史追踪，转而采用基于子问题的最小状态表示，并以Transformer替代GNN作为骨干网络。

### 极简状态表示与子问题视角

传统状态表示需追踪每个操作的历史完成时间与机器空闲时间，导致状态空间随步数增长而膨胀。ReSched 提出子问题视角，将每一步调度视为独立子问题，状态仅包含当前时刻的相对可用时间、持续时间及图结构依赖。具体而言，状态 $S_t$ 由四个核心特征构成：操作可用时间、机器可用时间、持续时间（Duration）及最小持续时间（Minimum Duration）。其中，可用时间通过减去全局最小可用时间进行归一化，防止数值无界增长。图结构仅保留操作间依赖（O2O）与操作-机器连接（O2M），其中O2O采用向后看边（backward-looking edges）并引入跳连接（hop connections），使操作能直接访问其所有后继操作，无需多层消息传递。

$$
S_t = \{ \text{OpAvail}_t, \text{MachAvail}_t, D_{ij}[m], \min_{m \in M_{ij}} D_{ij}[m] \} \cup \{ \text{O2O Edges}, \text{O2M Edges} \}
$$

该设计消除了历史依赖，确保状态满足马尔可夫性，即给定 $S_t$，剩余子问题的可行解集唯一确定，从而简化了策略学习的复杂度。

### 双分支Transformer架构

GNN的局部归纳偏置限制了长距离依赖的捕捉，ReSched 采用双分支Transformer架构。操作分支使用自注意力机制，并引入旋转位置编码（RoPE）以显式建模作业内操作的相对位置，避免引入额外可学习参数。机器分支采用交叉注意力机制，将操作信息聚合至机器嵌入。关键创新在于“Edge in Attention”设计，将持续时间作为边特征直接嵌入值向量（Value Vector），而非仅调整注意力分数。

$$
\alpha_{m,ij} = \text{softmax}\left( \frac{q_m \cdot (k_{ij} + k_{m,ij})}{\sqrt{d}} \right), \quad h'_m = \sum_{ij \in N(M_m)} \alpha_{m,ij} (v_{ij} + v_{m,ij})
$$

其中 $k_{m,ij}$ 和 $v_{m,ij}$ 是由持续时间 $D_{ij}[m]$ 投影得到的边特征。此外，针对操作-机器数量失衡（常超10:1）导致的注意力稀释问题，引入自基交叉注意力（Self-based Cross-attention），允许机器节点在注意力计算中关注自身嵌入，以保留关键机器级信息。

## 实验评估

实验在FJSP、JSSP和FFSP上进行，训练集规模为100万至200万实例，测试集包括Brandimarte、Hurink、Taillard等标准基准。基线涵盖传统启发式（FIFO, SPT, MWKR）、SOTA DRL方法（HGNN, DANIEL）及OR-Tools。ReSched 在FJSP 20x10实例上取得-1.55%的Gap，优于DANIEL的0.48%和HGNN的1.31%；在JSSP 40x10实例上取得-7.61%的Gap，显著优于DANIEL的-6.60%。

| 数据集 | 规模 | DANIEL Gap(%) | HGNN Gap(%) | ReSched Greedy Gap(%) | ReSched Sampling Gap(%) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| FJSP | 20 × 10 | 0.48 | 1.31 | -1.55 | -1.03 |
| JSSP | 40 × 10 | -6.60 | -2.74 | -7.61 | -5.69 |
| FFSP | 40 × 10 | -4.58 | -2.40 | -7.61 | -5.69 |

消融实验表明，移除RoPE或Edge in Attention模块会导致性能显著下降，验证了架构组件的有效性。然而，负Gap结果（即优于OR-Tools上限）可能源于OR-Tools在1800秒时限内未找到最优解，而非ReSched真正超越了理论最优。评估协议未报告置信区间，且缺乏元学习或LLM类基线对比，限制了结果的可比性。代码已开源，但超参数细节未在正文中完全披露。

## 关联研究分析

从状态表示看，ReSched 与 DANIEL 和 HGNN 的根本差异在于对历史依赖的处理。DANIEL 和 HGNN 依赖析取图中的复杂节点特征，包括历史构建数据，这虽提供了丰富的上下文，但破坏了马尔可夫性，导致策略在OOD场景下泛化能力受限。ReSched 通过子问题视角消除历史依赖，仅保留当前时刻的相对可用时间与图结构，证明了极简状态足以引导最优决策。这一设计的根源在于，调度问题的最优性仅取决于当前状态，而非历史轨迹，因此历史特征是冗余的。

从架构选择看，ReSched 用Transformer替代GNN，挑战了“GNN是变长表示最优解”的领域共识。GNN的局部消息传递机制难以高效捕捉长距离依赖，而Transformer的全局注意力机制能直接建模操作间的非局部交互。ReSched 通过RoPE和Edge in Attention设计，解决了Transformer在调度任务中的位置编码与边特征融合问题。然而，ReSched 未建模机器到操作（M2O）的反向反馈，仅采用单向交叉注意力，这可能限制了其对机器负载动态变化的响应能力。

## 总结

ReSched 解决了FJSP中状态表示冗余与GNN架构局限的矛盾，通过子问题视角将状态精简至4个核心特征，并采用双分支Transformer架构捕捉长距离依赖。实验表明，ReSched 在FJSP 20x10上取得-1.55%的Gap，在JSSP 40x10上取得-7.61%的Gap，优于SOTA DRL基线。其边界在于未建模M2O反向反馈，且负Gap结果的成因未完全澄清。当操作-机器数量比进一步增大时，自基交叉注意力的有效性是否仍成立，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.07020)
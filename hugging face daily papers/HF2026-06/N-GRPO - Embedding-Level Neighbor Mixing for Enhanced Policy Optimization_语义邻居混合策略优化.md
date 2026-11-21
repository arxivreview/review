# HuggingFace最新推荐论文 ｜N-GRPO: Embedding-Level Neighbor Mixing for Enhanced Policy Optimization ｜语义邻居混合策略优化

研究机构：浙江大学

作者：Xukun Zhu、Hang Yu、Peng Di 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.10768)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.10768)

> 组相对策略优化（GRPO）在强化学习后训练中依赖高质量轨迹探索，但Token级采样易陷入语义冗余，而直接注入Embedding噪声又会导致语义漂移。本文指出连续表示空间缺乏内在随机性，提出在Rollout阶段通过混合锚点Token与其语义邻居的Embedding来注入可控扰动。该方法在保持局部语义一致性的前提下扩展了探索空间，在DeepSeek-R1-Distill-Qwen模型上提升了数学推理基准的Pass@k指标，但其增益主要源于探索多样性而非信用分配精度的提升，在高难度任务上的性能上限仍受限于序列级奖励机制。

## 研究背景

GRPO通过采样一组响应并计算组内标准化奖励作为优势函数，消除了对独立价值网络（Critic）的依赖，确立了可验证奖励强化学习（RLVR）范式。然而，该范式的有效性高度依赖Rollout阶段生成的轨迹质量。标准自回归采样基于离散Token分布，其随机性受限于词表中的有限选项，往往导致生成的轨迹仅在措辞或顺序上存在差异（如“1+2”与“2+1”），底层推理逻辑未变，造成大量冗余轨迹。这种探索不足限制了策略梯度估计的方差降低效率，使得模型难以发现高奖励的新推理路径。

为突破离散Token的限制，研究界尝试将探索引入连续Embedding空间。Soft Thinking（Zhang et al., 2025b）通过概率加权求和整个词表Embedding实现软思考，但其随机性仍源自离散Token采样；HRPO（Yue et al., 2025）将其扩展至GRPO，但本质未变。另一种路线是直接注入高斯噪声，如STHT（Butt et al., 2025），但Transformer Embedding空间具有强各向异性，无约束噪声会将表示推离语义流形，导致解码出无关Token，破坏推理连贯性。本文的切入点在于：如何在连续Embedding空间中实现既具备随机性又严格遵循局部语义结构的扰动，从而在Rollout阶段生成真正多样化的有效轨迹。

## 核心方法

### 标准自回归采样参照系

标准语言模型生成过程为：给定上下文，计算Logits，经温度缩放后通过Softmax得到词表分布，采样一个离散Token，并检索其Embedding作为下一步输入。该流程的随机性完全由词表分布决定，探索范围被限制在离散Token集合内，无法利用连续向量空间中的插值可能性。本文问题与该通用流程的关键差异在于：将“采样离散Token并检索Embedding”替换为“构造连续混合Embedding”，从而在保持语义锚定的同时引入连续扰动。

### 语义邻居混合机制

标准采样中，输入表示为单一Token的Embedding $E[o_t]$。本文引入语义邻居混合（Semantic Neighbor Mixing），首先通过 $\arg\max$ 确定当前Logits对应的语义锚点Token $v_t^*$，确保探索中心对齐模型最优路径。随后，在Embedding矩阵中基于余弦相似度检索锚点的 $k-1$ 个最近邻，构成邻居集 $\mathcal{C}_t$。混合权重 $\alpha_c$ 由当前Logits在 $\mathcal{C}_t$ 上重新归一化得到，最终构造混合Embedding：

$$ \tilde{e}_{t+1} = \sum_{c \in \mathcal{C}_t} \alpha_c E[c] $$

该公式的物理含义是：以锚点为中心，在局部语义邻域内进行加权插值。由于邻居Token与锚点在语义方向上高度一致，混合后的向量始终位于有效语义区域内，避免了高斯噪声导致的语义漂移。这一设计解决了直接噪声注入破坏语义一致性的失效问题，使探索在连续空间中保持可控。

### GRPO框架集成与门控策略

将语义邻居混合直接应用于所有步骤可能导致训练不稳定。本文引入Bernoulli门控机制，以固定概率 $\rho$（混合率）激活混合操作，其余步骤保持标准采样。对于第 $i$ 条序列的第 $t$ 步，混合掩码 $m_{i,t} \sim \text{Bernoulli}(\rho)$ 决定输入表示：

$$ e_{i,t+1} = \begin{cases} \tilde{e}_{i,t+1} & \text{if } m_{i,t} = 1 \\ E[o_{i,t}] & \text{if } m_{i,t} = 0 \end{cases} $$

该机制通过间歇性探索防止策略过度依赖连续扰动，维持生成稳定性。在训练阶段，记录邻居集与权重以重构输入表示，确保概率计算一致性；在奖励计算时，使用锚点Token作为离散文本实现，兼容标准可验证奖励流程。优化目标保留GRPO的PPO风格裁剪代理与KL正则项，未改变优势估计粒度。

## 实验评估

实验在DeepSeek-R1-Distill-Qwen-1.5B/7B、Llama-3.2-1B及Qwen3-1.7B-Base上进行，使用AIME25、AMC23、MATH500及OOD基准GPQA-Diamond。基线覆盖标准GRPO、Soft Thinking、GRPO+Soft Thinking及STHT，但缺失SSVPO、EP-GRPO等细粒度信用分配方法，限制了与当前SOTA的直接对比。

| 模型 | 方法 | AIME25 Pass@32 | AMC23 Pass@32 | MATH500 Pass@32 | Average Pass@32 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| DeepSeek-R1-Distill-Qwen-1.5B | GRPO | 47.31 | 94.60 | 90.70 | 77.41 |
| DeepSeek-R1-Distill-Qwen-1.5B | STHT | 46.73 | 96.88 | 90.55 | 78.05 |
| DeepSeek-R1-Distill-Qwen-1.5B | N-GRPO | 50.28 | 96.18 | 91.05 | 79.17 |
| DeepSeek-R1-Distill-Qwen-7B | GRPO | 58.32 | 94.87 | 93.03 | 81.94 |
| DeepSeek-R1-Distill-Qwen-7B | N-GRPO | 61.18 | 98.13 | 93.28 | 84.20 |

N-GRPO在1.5B模型上将Average Pass@32从GRPO的77.41提升至79.17，在7B模型上从81.94提升至84.20。在AIME25上，1.5B模型Pass@32从47.31升至50.28，7B模型从58.32升至61.18。值得注意的是，STHT在AMC23上表现优于N-GRPO（96.88 vs 96.18），表明在中等难度任务上，无约束噪声可能因更大的探索范围而偶然获益，但在高难度AIME25上N-GRPO显著领先，验证了语义约束对复杂推理的必要性。

消融实验显示，混合率 $\rho$ 是关键超参数。当 $\rho$ 从0.1增至0.2时，1.5B模型在AIME25上的Pass@32显著下降，表明过度探索会破坏语义稳定性。混合策略对比中，N-GRPO优于Gumbel Soft-Thinking，证实语义邻居检索比Logits噪声注入更有效。距离度量方面，余弦距离显著优于L1和L2，归因于Embedding空间语义信息主要编码在向量方向而非模长中。

评估边界方面，论文未报告置信区间，且未在统一骨干网络下与SSVPO等步骤级信用分配方法对比。代码未开源，但基于verl框架实现，超参数（学习率1e-6，批量大小64，8块H20-3e GPU）已披露。推理阶段禁用混合机制，因测试时缺乏GRPO的过滤机制，混合噪声会损害最终答案准确性。

## 关联研究分析

从问题动机看，N-GRPO与Latent-GRPO（Deng et al., 2026）同属潜在空间探索路线，但解决路径截然不同。Latent-GRPO针对连续表示缺乏内在流形的问题，采用无效样本优势掩码和单侧噪声采样来校正优化方向，侧重于防止轨迹偏离流形；N-GRPO则通过语义邻居混合主动构造流形内的扰动，侧重于在流形内扩展探索范围。两者差异根源在于对“随机性来源”的处理：Latent-GRPO依赖采样噪声并加以约束，N-GRPO依赖结构化的邻居检索。N-GRPO未探索动态调整混合率以适应不同难度样本，这可能限制了其在极端难度任务上的表现。

从方法设计看，N-GRPO与EP-GRPO（Yu et al., 2026）形成鲜明对比。EP-GRPO通过熵门控结果优势调制与隐式进度优势结合，将稀疏结果奖励转化为密集的Token级学习信号，直接解决信用分配粗糙问题；N-GRPO未改变优势函数计算，仅通过丰富Rollout轨迹多样性间接提升组内奖励方差。这种差异暗示：探索增强与信用分配精度是正交但互补的维度。N-GRPO在AMC23上超越EP-GRPO（96.18 vs 95.31），但在AIME25上远低于SSVPO（50.28 vs 80.0），表明仅改进探索无法弥补序列级奖励在高难度任务上的根本缺陷。

## 总结

N-GRPO旨在解决GRPO中Token级采样导致的探索冗余与Embedding噪声导致的语义漂移之间的矛盾。其切入点在于利用Embedding空间的局部语义结构，通过邻居混合实现可控的连续扰动，从而在保持语义一致性的前提下扩展探索空间。实验表明，该方法在DeepSeek-R1-Distill-Qwen模型上将Average Pass@32从77.41提升至79.17（1.5B），并在AIME25上取得50.28的Pass@32。然而，论文自身实验暴露了边界：混合率 $\rho$ 过高会导致性能下降，且在高难度任务上仍显著低于步骤级信用分配方法。当探索增强与信用分配精度同时优化时，语义邻居混合能否在高难度推理任务上突破序列级奖励的性能上限，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.10768)
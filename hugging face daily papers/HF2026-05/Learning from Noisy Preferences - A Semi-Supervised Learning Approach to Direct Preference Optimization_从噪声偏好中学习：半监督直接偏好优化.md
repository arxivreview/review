# HuggingFace最新推荐论文 ｜Learning from Noisy Preferences: A Semi-Supervised Learning Approach to Direct Preference Optimization ｜从噪声偏好中学习：半监督直接偏好优化

作者：Xinxin Liu、Ming Li、Zonglin Lyu 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.24952)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.24952)

> 视觉生成模型的偏好对齐旨在解决扩散模型高保真度与人类多维偏好对齐之间的脱节。现有直接偏好优化方法将多维偏好压缩为二元标签，导致训练信号冲突，本文通过半监督自训练框架解耦冲突维度。该方法利用多奖励模型共识过滤数据，并让扩散模型自身生成时间步条件伪标签进行迭代修正。这一路径在离线DPO系中实现了SOTA性能，但其对Flow Matching模型的适用性及与在线方法的对比仍存疑。

## 研究背景

扩散模型通过逐步去噪生成图像，其训练过程可视为马尔可夫决策过程。直接偏好优化（Direct Preference Optimization, DPO）通过解析推导隐式奖励，直接利用离线偏好对优化策略，消除了对显式奖励模型（Reward Model, RM）的依赖。然而，人类视觉偏好本质上是多维的，涵盖语义对齐、美学与细节保真度，而现有数据集仅提供单一的全局二元标注。这种维度压缩导致“获胜”图像可能在某些维度上优于“失败”图像，但在其他维度上更差，从而在DPO训练中产生相互抵消的梯度信号。

该领域的主流路线分为离线DPO与在线强化学习（Reinforcement Learning, RL）。离线DPO计算效率高，但受限于数据覆盖与噪声；在线RL（如组相对策略优化，Group Relative Policy Optimization, GRPO）能恢复多样性，但面临训练不稳定与高计算成本。现有DPO改进多聚焦于损失函数重构或加权策略，却忽视了数据标签本身的结构性噪声。Semi-DPO的切入点在于将偏好对齐重新定义为带噪声标签的学习（Learning with Noisy Labels, LNL）问题，通过半监督学习范式处理多维冲突，而非单纯优化算法结构。

## 核心方法

### 方法参照系

标准Diffusion-DPO假设偏好数据是干净且一致的，直接在全量数据上最小化DPO损失。本文的关键差异在于承认数据中存在系统性噪声，将训练集划分为“干净”与“噪声”两部分，并引入自训练机制对噪声部分进行标签修正，而非直接丢弃或均匀加权。

### 多维冲突的理论形式化

设计动机在于解释为何标准DPO在多维偏好下收敛次优。本文证明，当偏好维度与全局标签冲突时，梯度更新方向与理想“oracle”方向的内积方差存在下界。具体地，设维度 $k$ 的奖励差为 $\Delta r_k$，数据集分为对齐集 $A_k$（$\Delta r_k > 0$）与冲突集 $C_k$（$\Delta r_k < 0$），概率分别为 $p_{a,k}$ 和 $p_{c,k}$。梯度方差下界为：

$$ \text{Var} \geq 4 p_{a,k} p_{c,k} (m_{a,k} m_{c,k}) $$

其中 $m_{a,k}, m_{c,k}$ 为条件期望梯度幅值。该公式表明，只要冲突集存在（$p_{c,k} > 0$），训练信号必然包含方向相反的更新，导致参数振荡与收敛停滞。

### 多奖励共识与迭代自训练

设计动机在于利用扩散模型的时间步层级特性（早期定构图，后期定细节）解耦冲突维度。第一阶段，利用五个预训练奖励模型（PickScore, HPS v2, CLIP Score, LAION Aesthetics, ImageReward）进行共识过滤，仅当所有模型与人工标签一致时，样本才进入干净集 $D_{labeled}$（约占Pick-a-Pic V2的21%），其余进入噪声集 $D_{unlabeled}$。第二阶段，在干净集上冷启动训练模型 $p_{\theta}^{0}$。随后，利用 $p_{\theta}^{i-1}$ 生成时间步条件伪标签。伪标签的置信度由对数几率 $z_{\theta}^{(t)}$ 的绝对值决定，仅当 $|z_{\theta}^{(t)}| > \tau_{\alpha}^{i}(t)$ 时保留。复合损失函数为：

$$ \mathcal{L} = \mathcal{L}_{labeled} + \mathcal{L}_{unlabeled}^{(i)} $$

其中 $\mathcal{L}_{unlabeled}^{(i)}$ 仅对高置信度伪标签计算DPO损失，且伪标签的正负号由 $z_{\theta}^{(t)}$ 的符号决定，可能翻转原始“胜/负”分配。这一机制通过自训练循环逐步净化噪声信号，避免确认偏差。

## 实验评估

实验在SD1.5与SDXL骨干上，使用Pick-a-Pic V2（851,293对）、HPS v2与Parti-Prompt数据集进行验证。基线覆盖Diffusion-DPO、Diffusion-KTO、MaPO与InPO，但缺失GRPO系在线方法（如DanceGRPO）及最新DPO变体（如PG-DPO）。在Pick-a-Pic V2上，Semi-DPO取得21.524的PickScore，优于Diffusion-DPO的20.948与Diffusion-KTO的21.064；在HPS v2上，Semi-DPO取得21.945的PickScore，显著高于Diffusion-DPO的21.308。

| 数据集 | 方法 | PickScore | HPSv2.1 | ImageReward |
|---|---|---|---|---|
| Pick-a-Pic V2 | Diffusion-DPO | 20.948 | 0.261 | 0.297 |
| Pick-a-Pic V2 | Diffusion-KTO | 21.064 | 0.281 | 0.629 |
| Pick-a-Pic V2 | Semi-DPO | 21.524 | 0.288 | 0.801 |
| HPS v2 | Diffusion-DPO | 21.308 | 0.259 | 0.339 |
| HPS v2 | Semi-DPO | 21.945 | 0.287 | 0.816 |

消融实验显示，迭代自训练带来显著增益：从Iter0到Iter2，Pick-a-Pic V2上的PickScore从21.153提升至21.524，ImageReward从0.563提升至0.801。然而，增益在Iter2后趋于稳定，表明两轮自训练足以收敛。多奖励共识数量从2增至5时，性能持续小幅提升，但边际收益递减。

评估边界方面，实验局限于SD1.5/SDXL，未验证Flow Matching模型（如FLUX）上的有效性。指标涵盖PickScore、HPSv2.1、ImageReward等，但缺乏多样性度量（如FID）。代码已开源，超参数在附录中提供，可复现性良好。

## 关联研究分析

从问题动机看，Semi-DPO与Poly-DPO均针对偏好数据噪声，但路径截然不同。Poly-DPO通过调整超参数 $\alpha$ 动态权衡样本权重，假设噪声是随机的；Semi-DPO则假设噪声是结构性的（多维冲突），通过自训练重构标签。这一差异源于对噪声本质的不同理解：前者视噪声为统计干扰，后者视噪声为语义冲突。Semi-DPO的理论证明支持了后者，但Poly-DPO在大规模数据上的计算效率可能更具优势，二者在数据充足时的相对性能缺乏直接对比。

从方法设计看，Semi-DPO借鉴了Noisy Student Training的自训练范式，但将教师-学生结构替换为扩散模型自身。这一设计利用了DPO损失隐含的分类器特性，无需额外架构。然而，与ViPO等细粒度信用分配方法相比，Semi-DPO的“细粒度”体现在时间步维度，而非空间区域。ViPO通过区域感知权重分解实现空间信用分配，Semi-DPO则通过时间步条件伪标签实现时间信用分配。两者是否可结合，以同时优化空间与时间维度的偏好信号，论文未探索。

## 总结

Semi-DPO解决了多维偏好压缩为二元标签导致的梯度冲突问题，通过半监督自训练框架解耦冲突维度。其核心在于利用扩散模型自身作为隐式分类器，生成时间步条件伪标签，避免了显式奖励模型的计算开销。实验证明，该方法在Pick-a-Pic V2上取得21.524的PickScore，优于Diffusion-DPO的20.948，验证了自训练机制的有效性。然而，实验边界局限于SD1.5/SDXL，未涉及Flow Matching模型，且缺乏与在线RL方法的直接对比。当骨干网络从扩散模型切换至确定性ODE的Flow Matching时，时间步层级特性是否依然成立，自训练机制能否有效解耦冲突，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.24952)
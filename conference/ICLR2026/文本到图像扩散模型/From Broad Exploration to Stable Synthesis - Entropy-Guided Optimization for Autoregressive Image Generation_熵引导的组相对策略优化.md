# ICLR2026最新论文 ｜From Broad Exploration to Stable Synthesis: Entropy-Guided Optimization for Autoregressive Image Generation ｜熵引导的组相对策略优化

研究机构：香港中文大学、澳门大学

作者：Han Song、Yucheng Zhou、Jianbing Shen 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.02355)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.02355)

> 自回归文本到图像生成中，思维链（Chain-of-Thought, CoT）的探索性与强化学习（Reinforcement Learning, RL）的利用性在token级不确定性上存在未被量化的交互。现有GRPO方法对序列内所有token广播相同优势值，导致梯度预算在低置信度区域被浪费，且无法区分语义规划与视觉解码中的不同不确定性来源。本文通过Shannon熵动力学分析，提出在token级重新分配优化预算的EG-GRPO，保护低熵token并增强高熵token的探索。该方法在组合生成基准上取得SOTA，但其有效性局限于自回归范式，且未验证与扩散模型在高频细节保真度上的公平对比。

## 研究背景

自回归文本到图像模型在离散潜空间中逐token生成图像，其条件似然分解为 $P(z|c) = \prod_{i=1}^L P(z_i|z_{<i}, c)$。这一过程面临两个核心矛盾：思维链推理虽能扩展语义探索空间，但引入的token级不确定性会传导至下游图像质量；强化学习虽能优化奖励对齐，但标准GRPO将组内相对优势广播至所有token，忽视了不同token在生成稳定性中的异质性作用。

主流路线将CoT与RL结合，如T2I-R1（Jiang et al., 2025）通过双级推理链优化GRPO，但均未系统分析CoT探索行为与RL优化在token级熵上的交互机制。现有方法假设序列内所有token对奖励贡献均等，导致低置信度token的梯度更新被高置信度token稀释，且无法区分语义规划阶段的探索必要性与视觉解码阶段的稳定性需求。本文切入点在于将Shannon熵作为token级不确定性度量，揭示CoT扩展探索空间、RL收缩至高奖励区的动力学特征，并基于此设计差异化的优化策略。

## 核心方法

### 方法参照系

本文问题属于自回归生成模型的RL对齐范畴，标准流程为GRPO：对提示 $c$ 采样 $G$ 个序列 $\{o_{[i]}\}$，计算组内相对优势 $A_{[i]} = \frac{r_{[i]} - \text{mean}(r)}{\text{std}(r)}$，并将 $A_{[i]}$ 广播至序列 $i$ 的所有token。本文与标准GRPO的关键差异在于：不再假设所有token对奖励贡献均等，而是基于token级熵动态调整梯度预算分配。

### 熵动力学分析与token掩码设计

GRPO的序列级优势广播忽略了token级不确定性差异，导致低置信度token的更新被高置信度token稀释。本文首先通过实验揭示CoT扩展熵分布、RL收缩熵分布的动力学特征，并发现图像token熵的均值与标准差与最终奖励呈强负相关。基于此，定义归一化熵 $\bar{H}_{t[i]} = H_{t[i]} / \log|V|$，并按模态独立计算序列内百分位，构建掩码：

$$
M_{t[i]} = \begin{cases} 0 & \text{if } \bar{H}_{t[i]} \leq p_{\text{lo}} \\ 1 & \text{otherwise} \end{cases}, \quad U_{t[i]} = \begin{cases} 1 & \text{if } \bar{H}_{t[i]} \geq p_{\text{hi}} \\ 0 & \text{otherwise} \end{cases}
$$

其中 $p_{\text{lo}}=0.2$，$p_{\text{hi}}=0.5$。该设计将低熵token（前20%）的奖励驱动更新置零，仅保留KL正则项以保护已学习知识；高熵token（后50%）标记为接收熵奖励。这一改动解决了标准GRPO在低置信度区域浪费梯度预算、且无法区分语义规划与视觉解码不确定性的问题，使优化聚焦于真正需要探索的不稳定区域。

### 熵引导的优势重分配与预算校准

在掩码基础上，本文修改token级优势为 $\tilde{A}_{t[i]} = A_{[i]} \cdot M_{t[i]} + \lambda \cdot \text{sg}[\bar{H}_{t[i]}] \cdot U_{t[i]}$，其中 $\text{sg}[\cdot]$ 为停止梯度操作。该公式的物理含义是：低熵token仅受KL约束，高熵token在原有优势上叠加与熵成正比的奖励。为确保更新规模与GRPO一致，引入批次级校准系数 $\lambda^\star = \kappa \cdot \frac{\sum_i |A_{[i]}|}{\sum_i \sum_t U_{t[i]} \cdot \bar{H}_{t[i]}}$，其中 $\kappa=1$ 保证批次级预算中性。当GRPO达到均衡（$A_{[i]} \equiv 0$）时，$\lambda^\star=0$，熵奖励消失，保持基线目标的不动点。这一设计解决了熵奖励可能破坏GRPO收敛性的问题，确保优化在探索与利用间动态平衡，且不会偏离原有奖励对齐目标。

## 实验评估

实验在T2I-CompBench（6,000提示，测试组合泛化）和WISE（1,000提示，测试知识推理）上进行，骨干为Janus-Pro-7B，奖励管线结合HPS、GroundingDINO与GIT。基线覆盖PixArt-α、SD-v1.5、FLUX.1-dev、Emu3、Show-o、Janus-Pro-7B及T2I-R1，但缺失最新扩散SOTA（如SD3、FLUX.1-pro）及纯自回归SOTA（如Emu3.5），有效性局限于自回归范式内部。

| 模型 | T2I-CompBench Color | T2I-CompBench Shape | T2I-CompBench Texture | WISE Culture | WISE Spatio-temporal | WISE Science |
|---|---|---|---|---|---|---|
| T2I-R1 | 74.07 | 57.06 | 71.64 | 48.00 | 55.50 | 45.00 |
| EG-GRPO | 84.11 | 60.88 | 77.38 | 49.00 | 56.00 | 46.33 |

EG-GRPO在T2I-CompBench所有子项上超越T2I-R1，其中Shape绑定提升3.82分，表明熵引导对空间关系理解有显著增益。消融实验显示，仅对CoT token或仅对图像token应用熵引导均导致性能下降（Color分别为81.29和79.25），证明需同时控制语义规划与视觉解码的不确定性。多样性分析表明，在质量分数差异小于0.1的样本子集上，EG-GRPO的Vendi Score（2.593）与基线（2.592）几乎相同，说明熵奖励抑制的是导致不稳定的“坏不确定性”，而非语义多样性。

评估边界方面，论文未报告计算效率指标（如GPU小时、推理延迟），且WISE基准的推理指令为作者自行重新实现，可能与原始协议存在偏差。代码已开源，但超参数（如 $p_{\text{lo}}$、$p_{\text{hi}}$ 的敏感性）未充分消融，可复现性依赖于特定骨干与奖励管线配置。

## 关联研究分析

从问题动机看，本文与Think-Then-Generate（Kou et al., 2026）均引入CoT增强语义规划，但前者侧重闭环验证机制以解决复杂语义理解，本文则聚焦CoT与RL在token级熵上的交互动力学。这一差异源于任务特性：Think-Then-Generate针对长提示与组合关系的显式推理，而本文针对自回归生成中的稳定性与探索平衡。本文未探索CoT推理质量对熵分布的非线性影响，当CoT存在系统性错误时，熵引导是否仍能正确分配梯度预算，论文未给出回答。

从方法设计看，本文与Mask-GRPO（Luo et al., 2025）均结合掩码与GRPO，但前者掩码基于任务结构（如去掩码过程的多步马尔可夫决策），本文掩码基于token级熵阈值。这一差异反映了优化目标的根本不同：Mask-GRPO解决掩码生成模型中过渡概率定义问题，本文解决自回归生成中不确定性异质性问题。本文的熵阈值（$p_{\text{lo}}=0.2$，$p_{\text{hi}}=0.5$）为固定值，未随训练进程动态调整，当模型收敛至高奖励区时，高熵token比例可能下降，导致熵奖励失效，这一潜在局限在实验中未体现。

## 总结

本文要解决的核心矛盾是自回归T2I生成中CoT探索性与RL利用性在token级不确定性上的未量化交互。现有GRPO方法因序列级优势广播无法区分不同token的稳定性需求，而本文凭借Shannon熵动力学分析，首次揭示CoT扩展探索空间、RL收缩至高奖励区的特征，并基于此设计token级熵引导优化。EG-GRPO在T2I-CompBench Shape绑定上提升3.82分，在WISE Science上提升1.33分，证明了熵引导对组合泛化与知识推理的有效性。其边界在于实验局限于自回归范式，未与扩散模型SOTA进行公平对比，且熵阈值为固定值，未随训练进程动态调整。当模型收敛至高奖励区、高熵token比例显著下降时，熵奖励的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.02355)
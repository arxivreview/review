# HuggingFace最新推荐论文 ｜A Gradient Perspective on RLVR Stability and Winner Advantage Policy Optimization ｜基于Token级梯度动力学的RLVR稳定性分析与赢家优势策略优化

作者：Prasanth Yss、Zhichen Ren、Rasa Hosseinzadeh 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.16154)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.16154)

> 强化学习可验证奖励（RLVR）旨在通过稀疏奖励提升大语言模型（LLM）的推理能力，但基于组相对策略优化（GRPO）的变体常因策略漂移导致训练崩溃。现有方法多从策略偏移或系统误差角度归因，忽略了优势符号与Token概率分布交互对局部几何结构的破坏。本文提出赢家优势策略优化（WAPO），通过仅保留正优势项的在线裁剪策略梯度，规避负优势更新引发的熵坍缩。该方案在基线崩溃场景下显著优于GRPO与DAPO，但在稳定场景下增益有限，且其理论假设是否适用于密集奖励场景尚存疑。

## 研究背景

当LLM在数学推理任务中执行多步生成时，策略网络需根据稀疏的最终奖励调整中间Token的概率分布。这一过程涉及部分可观测马尔可夫决策过程（POMDP）中的信用分配难题：最终奖励无法直接指导中间步骤的优化。为缓解此问题，GRPO采用组内相对优势估计替代价值函数，通过重要性采样校正Off-policy偏差。然而，这种机制在长序列生成中易引发分布畸变，导致模型输出退化为重复模式或无关多语言片段，即熵坍缩现象。

RLVR领域的核心矛盾在于：Off-policy采样带来的样本效率提升与策略更新引发的稳定性损失之间的权衡。主流改进路线包括调整裁剪阈值（如DAPO）、序列级归一化（如GSPO）或引入信任区域约束，但这些方法均假设崩溃源于新旧策略间的距离过大。然而，实验表明移除更多发散Token并不总能提升稳定性，甚至可能加速崩溃。这提示崩溃机制可能并非单纯由策略漂移驱动，而是源于梯度更新对局部概率分布几何结构的特定扰动。本文切入点在于放弃“策略距离”视角，转而分析单个Token的梯度更新如何改变当前策略下的概率分布与熵值，从而建立一种基于Token级动力学的稳定性诊断框架。

## 核心方法

### 方法参照系

本文问题归属于RLVR算法稳定性优化类别。标准GRPO流程包含：由旧策略$\pi_{\theta_{old}}$采样组内完成序列，计算组内归一化优势$A_i$，并通过裁剪的重要性比率$\rho_{ij}(\theta)$更新当前策略$\pi_\theta$。本文的关键差异在于，不修改裁剪阈值或归一化方式，而是基于当前策略分布$P_\theta$的局部几何特征，对优势符号进行选择性掩码，从而改变梯度更新的构成。

### Peak-Valley Token分类法

传统稳定性分析关注策略偏移，本文则聚焦于单个Token的梯度更新对softmax分布的局部影响。设计动机在于揭示为何某些“发散”Token的更新反而导致崩溃，而另一些则促进探索。对于采样Token $s$，定义阈值 $C(p) = \sqrt{\sum_{j=1}^V p_j^2}$，该值反映分布的尖锐程度。若采样Token概率 $p_s \ge C(p)$，则称为Peak Token；若 $p_s < C(p)$，则称为Valley Token。

$$
\Delta p_i \approx \eta A p_i (p_s + p_i - C(p)) \quad (i \neq s)
$$

该公式表明，非采样Token $i$ 的概率变化取决于优势符号 $A$ 与 $p_s + p_i$ 相对于 $C(p)$ 的位置。当 $A > 0$ 且 $p_s + p_i < C(p)$ 时，非采样Token概率增加，导致分布变平（熵增）；反之则概率减少，分布变尖（熵减）。这一分类将熵变化与具体采样Token关联，解释了为何低概率成功Token（Pos-valley）的强化可能引发随机发散，而高概率失败Token（Neg-peak）的抑制可能引发重复退化。

### 赢家优势策略优化（WAPO）

基于上述分类，Pos-peak更新稳定但保守，Neg-peak与Pos-valley更新导致熵增崩溃，Neg-valley更新初期有益但后期导致低熵崩溃。设计动机在于保留正优势更新中的探索信号（Pos-valley）与利用信号（Pos-peak），同时剔除所有负优势更新引发的分布畸变。WAPO的目标函数为：

$$
\mathcal{L}_{WAPO} = -\frac{1}{G} \sum_{i=1}^G \frac{1}{T} \sum_{j=1}^{T_i} \min\left(\rho_{ij}(\theta) A_i^+, \text{clip}(\rho_{ij}(\theta), 1-\epsilon, 1+\epsilon) A_i^+\right)
$$

其中 $A_i^+ = \max(A_i, 0)$。该公式仅对正优势完成序列计算策略梯度，负优势项被完全掩码。与拒绝微调不同，WAPO保留在线采样、组内归一化优势及重要性比率，确保其仍为在线策略梯度方法。在二元奖励设定下，该更新方向与成功概率 $q_x$ 的梯度一致，但带有自适应因子 $1-q_x$，自动降低对已饱和提示词的更新强度，避免过拟合。

## 实验评估

实验在Math-500、NuminaMath-LEAN、Hotpot-QA及OTT-QA上评估，覆盖数学推理与多跳问答，模型包括Qwen3-4B、SmolLM3-3B及Gemma3-4B。基线涵盖GRPO、DAPO、GSPO，但未对比PSR或RAFT++等正例筛选方法（仅在附录提及）。

| 数据集 | 模型 | 方法 | Pass@1 (%) |
| :--- | :--- | :--- | :--- |
| AIME'25 | Qwen3-4B | WAPO | 38.43 |
| AIME'25 | Qwen3-4B | GRPO | 45.10 |
| AIME'25 | Qwen3-4B | DAPO | 39.06 |
| AIME'25 | SmolLM3-3B | WAPO | 26.77 |
| AIME'25 | SmolLM3-3B | GRPO | 25.93 |
| AIME'25 | Gemma3-4B | WAPO | 12.71 |
| AIME'25 | Gemma3-4B | GSPO | 14.27 |

在AIME'25上，WAPO在Qwen3-4B上低于GRPO（38.43 vs 45.10），但在SmolLM3-3B上略优（26.77 vs 25.93），Gemma3-4B上低于GSPO（12.71 vs 14.27）。这表明WAPO的优势并非普适，而是依赖于基线是否崩溃。在Hotpot-QA与OTT-QA上，WAPO表现更优，例如OTT-QA上Qwen3-4B的WAPO比次优稳定基线高9.9%。

消融实验显示，仅保留Peak或Valley Token均导致崩溃或性能不足，验证了优势符号作为最稳定粗粒度过滤器的作用。Pos训练与DAPO基线持平，表明正优势序列已包含足够学习信号。然而，WAPO在Math-500早期检查点略落后于基线，可能源于自适应因子 $1-q_x$ 对低成功率提示词的过度强调，导致早期更新过于保守。

评估边界方面，论文未报告置信区间，且AIME'25结果受骨干模型规模影响较大（3-4B vs 知识库中1.5B SOTA）。代码已开源，但超参数配置（如$\epsilon$值）在不同基线间差异显著，复现时需严格遵循论文附录设置。

## 关联研究分析

从问题动机看，本文与GSPO（Zheng et al., 2025b）均针对GRPO的稳定性问题，但GSPO通过序列级裁剪缓解Token级重要性采样的方差，而WAPO通过移除负优势项从源头消除熵增机制。GSPO假设崩溃源于高方差梯度，WAPO则证明崩溃源于特定Token类型的分布畸变。这一差异源于任务特性：GSPO在数学推理中表现稳定但易饱和，WAPO在多跳QA中更优，暗示多跳任务中负优势更新引发的分布畸变更严重。

从方法设计看，WAPO与PSR（Zhu et al., 2025）及RAFT++（Xiong et al., 2025）同属正例筛选路线，但PSR与RAFT++采用序列级归一化，导致短答案偏差，而WAPO保留Token级重要性比率，避免此问题。PSR不使用裁剪策略梯度，WAPO则保留在线裁剪机制，确保其与GRPO框架的兼容性。这一设计选择源于WAPO对“在线策略梯度”属性的坚持，而PSR/RAFT++更偏向离线拒绝采样。

## 总结

本文核心矛盾在于RLVR中Off-policy更新引发的熵坍缩与探索需求之间的冲突。现有方法通过调整裁剪或归一化缓解方差，但未能识别崩溃的Token级动力学根源。本文通过Peak-Valley分类法揭示优势符号与Token概率分布的交互机制，提出WAPO仅保留正优势更新，在基线崩溃场景下显著提升稳定性。实验显示WAPO在OTT-QA上Qwen3-4B比次优基线高9.9%，但在AIME'25上Qwen3-4B低于GRPO 6.67个点。其边界在于：WAPO在基线稳定时无显著增益，且自适应因子 $1-q_x$ 可能导致早期训练保守。当奖励信号从稀疏二元变为密集连续时，正优势项中是否仍包含足够的探索信号以维持多样性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.16154)
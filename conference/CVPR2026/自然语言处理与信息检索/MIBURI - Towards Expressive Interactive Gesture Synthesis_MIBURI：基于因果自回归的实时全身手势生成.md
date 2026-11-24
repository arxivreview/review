# CVPR2026最新论文 ｜MIBURI: Towards Expressive Interactive Gesture Synthesis ｜MIBURI：基于因果自回归的实时全身手势生成

研究机构：德国马克斯·普朗克信息学研究所、德国萨尔大学

作者：M. Hamza Mughal、Rishabh Dabral、Vera Demberg 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.03282)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.03282)

> 协同语音手势生成（Co-Speech Gesture Generation, CSG）旨在根据语音合成同步且语义相关的身体运动，其核心价值在于赋予虚拟人类以自然交互能力。现有扩散模型虽能生成高质量运动，但依赖未来上下文且推理延迟高，无法满足实时交互需求；早期实时方法则因非因果性或低表达性而受限。MIBURI 提出首个在线、因果框架，通过直接接入语音-文本基础模型内部令牌流，利用双 Transformer 自回归生成离散手势令牌，在保持低延迟的同时实现全身协调运动。该工作验证了因果架构在实时场景下的可行性，但其运动质量与离线 SOTA 仍有差距，且高度依赖特定基础模型的内部表示。

## 研究背景

实时交互要求系统在处理当前输入时不依赖未来信息，这一约束称为因果性（Causality）。因果模型仅利用过去输入预测当前输出，与实时性（Real-time）不同，后者还要求满足严格的时间延迟约束以维持对话流畅性。在协同语音手势生成中，因果性意味着手势生成不能等待完整语句结束，而必须逐帧响应实时语音流，这对传统依赖双向注意力或未来令牌的离线模型构成了根本性挑战。

该领域核心问题是如何在严格实时延迟下生成既具备细粒度语义对齐又保持说话人独特风格的全身协调运动。主流路线分为两类：一类是扩散模型（如 EMAGE、ConvoFusion），虽在运动质量和多样性上表现优异，但需访问过去和未来语音上下文，无法并行于实时语音生成；另一类是实时方法（如 MambaTalk、GestureLSM），虽降低了延迟，但多为非因果架构，依赖种子序列或未来上下文，且运动表达性有限。现有方案无法同时满足因果性、实时性和表达性三大要求，导致具身对话代理（Embodied Conversational Agents, ECAs）难以实现自然的人机交互。

MIBURI 的切入点在于利用语音-文本基础模型 Moshi 的内部令牌流作为条件输入，避免传统管道中语音转文本的延迟与语义损失。通过设计因果自回归架构和身体部位感知的离散编码，MIBURI 在无需未来上下文和种子序列的前提下，实现了低延迟的全身手势生成，填补了因果实时手势生成的空白。

## 核心方法

### 方法参照系

传统协同语音手势生成通常采用“音频编码-运动解码”两阶段流程，其中音频编码器提取声学特征，运动解码器（如扩散模型或自回归 Transformer）生成连续或离散运动序列。本文的关键差异在于：不依赖外部音频编码器，而是直接利用语音-文本基础模型 Moshi 的内部语义-声学令牌流作为条件，并将运动解码器改造为因果自回归架构，以支持实时流式生成。

### 身体部位感知手势编码

为捕捉从大幅手臂动作到细微手指动作的多层次运动细节，MIBURI 将身体分为面部、上肢（含手）和下肢（含全局平移与足部接触）三个区域，分别通过独立的 Residual VQ-VAE (RVQ) 编码器进行离散化。每个区域编码器包含因果自注意力 Transformer 编码器与下采样 1D 卷积层，将运动序列 $\mathbf{x}_b$ 编码为潜在表示 $\tilde{\mathbf{g}}_b = E_b(\mathbf{x}_b)$，并通过 RVQ 量化为 $K_b$ 级令牌 $\mathbf{g}_b \in \mathbb{R}^{T \times K_b}$。

$$
\hat{\mathbf{x}}_b = D_b(\mathbf{g}_b)
$$

该公式表示解码器 $D_b$ 从离散令牌 $\mathbf{g}_b$ 重构运动序列 $\hat{\mathbf{x}}_b$，其中 $D_b$ 包含因果 Transformer 编码器与上采样转置 1D 卷积层。这种分区域编码解决了单一 VQ-VAE 因量化误差导致的运动粗糙问题，同时通过因果结构确保解码过程不依赖未来帧，为实时生成奠定基础。

### 双 Transformer 因果生成架构

为解耦时间动态与运动学层次，MIBURI 采用两个 Transformer：时间 Transformer 预测每个时间步的第一级令牌 $\mathbf{g}^{(t,1)}$，运动学 Transformer 在固定时间步 $t$ 内自回归预测后续 $K-1$ 级令牌。时间 Transformer 通过因果自注意力关注过去手势令牌，并通过双因果交叉注意力关注当前及过去的语音-文本令牌；运动学 Transformer 则条件于时间上下文 $\mathbf{h}_t$ 及当前语音-文本令牌，逐步细化运动细节。

$$
\mathbf{g}^{(t,k)} = \text{Softmax}(W_k \mathbf{h}^{(t,k-1)} + b_k)
$$

该公式表示运动学 Transformer 在第 $k$ 级预测时，基于前一级隐藏状态 $\mathbf{h}^{(t,k-1)}$ 通过线性投影与 Softmax 生成离散令牌。这种二维解耦设计避免了将 $T \times K$ 个令牌全部纳入单一自回归序列导致的上下文窗口膨胀，降低了训练难度与推理计算成本，同时保留了运动的时间连贯性与部位层次感。

### 表达性增强辅助损失

自回归模型易收敛至平均姿态并产生时间漂移，MIBURI 引入对比 InfoNCE 损失与语音激活损失以增强表达性。InfoNCE 损失通过 Gumbel-Softmax 重参数化近似离散采样，计算真实与预测潜在表示的余弦相似度矩阵，推动匹配对相似、不匹配对分离。语音激活损失将 Transformer 输出投影至二分类头，区分听/说状态，防止听状态下的“幻觉”手势。

$$
\mathcal{L}_{\text{con}} = -\frac{1}{B} \sum_{i=1}^B \log \frac{\exp(\text{sim}(\mathbf{z}_i^{\text{GT}}, \mathbf{z}_i^{\text{pred}})/\tau)}{\sum_{j=1}^B \exp(\text{sim}(\mathbf{z}_i^{\text{GT}}, \mathbf{z}_j^{\text{pred}})/\tau)}
$$

该公式表示 InfoNCE 损失，其中 $\text{sim}(\cdot)$ 为余弦相似度，$\tau$ 为温度参数，$B$ 为批次大小。该损失强制生成运动与真实运动在轨迹上保持相似，同时抑制批次内不相关运动的混淆，从而提升手势的多样性与语义对齐度。

## 实验评估

实验在 BEAT2 数据集上进行，包含单说话人（Scott）与多说话人（23 人）测试集。基线覆盖非因果方法（EMAGE、RAG-Gesture、CaMN）与实时方法（GestureLSM、MambaTalk），但缺失 StreamTalk 等最新闭环校正方法。多说话人设置下，MIBURI 取得 FGD 0.480、BeatAlign 0.461，优于 MambaTalk（FGD 0.537、BeatAlign 0.080）与 GestureLSM（FGD 0.515、BeatAlign 0.648），但低于 EMAGE（FGD 0.176、BeatAlign 0.236）。单说话人设置下，MIBURI 的 FGD 0.753 与 BeatAlign 0.790 接近 EMAGE（FGD 0.552、BeatAlign 0.795），但 L1-Div 15.85 高于 EMAGE 的 13.06，表明运动多样性略逊。

| 方法 | FGD↓ | BeatAlign→ | L1-Div→ | Facial-MSE↓ |
|---|---|---|---|---|
| GT | 0.446 | 8.45 | – | – |
| EMAGE* | 0.176 | 0.236 | 6.58 | 4.6 |
| MambaTalk* | 0.537 | 0.080 | 3.73 | 4.12 |
| MIBURI | 0.480 | 0.461 | 10.44 | 7.77 |

消融实验显示，双 Transformer 架构相比单一 Transformer 将 FGD 从 1.256 降至 0.480，步时从 0.096s 降至 0.035s，验证了解耦设计的效率与质量优势。RVQ 码本数量 $K$ 从 1 增至 8 时，MPJPE 从 0.043m 降至 0.016m，表明更细粒度量化显著提升重构精度。InfoNCE 损失与 MSE 损失相比，前者在保持 FGD 0.480 的同时将 L1-Div 提升至 10.44，而 MSE 损失导致 FGD 升至 0.577，说明对比学习更利于平衡质量与多样性。

评估指标涵盖 FGD、BeatAlign、L1-Div 与 Facial-MSE，但缺乏对长时程漂移的量化评估。论文未提供代码与完整超参数，仅报告 A100 GPU 上的延迟数据（MIBURI 34.9ms/步，生成 2 帧），可复现性受限。多说话人设置下 MIBURI 的 FGD 0.480 与知识库中 PersonaGest 的 4.10 不可直接比较，因归一化协议不同，但 BeatAlign 0.461 显著优于 MambaTalk 的 0.080，表明因果架构在节奏同步上的优势。

## 关联研究分析

从问题动机看，MIBURI 与 MambaTalk 同属实时路线，但 MambaTalk 依赖非因果交叉注意力与种子序列，而 MIBURI 通过因果自回归与内部令牌流实现无种子实时生成。这一差异源于任务特性：MambaTalk 侧重降低计算复杂度，MIBURI 侧重消除未来依赖。MIBURI 的因果设计使其能直接嵌入全双工对话系统，而 MambaTalk 需额外处理种子初始化，限制了其在连续交互中的适用性。

从方法设计看，MIBURI 与 EMAGE 同属全身整体生成，但 EMAGE 采用掩码建模与扩散解码，MIBURI 采用 RVQ 与自回归解码。EMAGE 的 FGD 0.176 远优于 MIBURI 的 0.480，表明连续生成在运动质量上仍占优；但 MIBURI 的延迟 34.9ms 远低于 EMAGE 的 37.4ms（据 Table 4），且无需未来上下文。这一权衡反映了实时性与质量的冲突：MIBURI 牺牲部分运动细节换取因果实时性，而 EMAGE 以离线计算换取更高保真度。MIBURI 的 RVQ 离散化是否能在更大规模数据下逼近连续生成的质量，论文未给出回答。

## 总结

MIBURI 要解决的核心矛盾是实时交互中因果性、低延迟与运动表达性的不可兼得。现有扩散模型依赖未来上下文，实时方法缺乏因果性或表达性，而 MIBURI 通过直接接入 Moshi 内部令牌流与双 Transformer 因果架构，在无需种子序列的前提下实现了 34.9ms 延迟的全身手势生成。多说话人设置下，MIBURI 的 BeatAlign 0.461 显著优于 MambaTalk 的 0.080，验证了因果架构在节奏同步上的优势；但 FGD 0.480 仍高于 EMAGE 的 0.176，表明运动质量存在差距。该工作的边界在于高度依赖 Moshi 的内部表示，且未评估长时程漂移。当 Moshi 的令牌流语义信息不足时，MIBURI 的手势表达性是否会进一步退化，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.03282)
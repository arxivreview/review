# ICLR2026最新论文 ｜Rethinking Global Text Conditioning in Diffusion Transformers ｜调制引导：重估扩散Transformer中全局文本条件的角色

研究机构：Adobe研究院

作者：Nikita Starodubcev、Daniil Pakhomov、Zongze Wu 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.09268)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.09268)

> 文本到图像扩散模型面临质量与语义对齐的权衡，现有Classifier-Free Guidance (CFG) 在高权重下易导致过饱和，且无法直接应用于无CFG的少步蒸馏模型。近期趋势倾向于丢弃全局文本条件（Pooled Embedding），但本文发现该机制在常规生成中虽贡献微弱，却蕴含未被利用的引导潜力。通过将CLIP嵌入从条件源重构为调制空间中的引导信号，本文提出了一种无需训练、低开销的推理时校正方法。该方法在SOTA少步模型上实现了显著的质量与细粒度语义提升，但其对CLIP嵌入可解释性的依赖限制了其在完全无CLIP架构中的泛化性。

## 研究背景

扩散Transformer (DiT) 架构通过注意力机制与调制层（Modulation Layers）共同处理文本条件。注意力机制负责逐token的细粒度语义对齐，而调制层利用全局文本嵌入（如CLIP Pooled Embedding）生成缩放与偏移系数，影响整个网络的激活状态。在早期U-Net架构中，这种全局条件至关重要，但在最新的DiT模型（如FLUX, SD3.5）中，研究者观察到仅靠注意力机制即可实现相当的文本对齐，导致全局文本条件被视为冗余并被部分模型（如COSMOS, Wan）直接移除。

这一“去全局化”趋势引发了关于全局文本条件必要性的质疑。主流观点认为，随着注意力机制能力的增强，全局条件对生成质量的边际贡献趋近于零，甚至可能引入噪声。然而，这种结论基于静态视角，即假设全局条件仅作为输入信号存在。现有动态CFG调度方法（如TCFG, In-situ Autoguidance）聚焦于噪声预测空间的时间步权重调整，忽略了调制空间这一独立于噪声预测的控制维度。本文的切入点在于：全局文本条件并非无用，而是其功能被错误定位——它不应作为被动的条件输入，而应作为主动的引导信号，通过调制系数空间对去噪轨迹进行校正。

## 核心方法

### 方法参照系

本文问题置于“推理时引导”框架下，与Classifier-Free Guidance (CFG) 形成互补。标准CFG在噪声预测空间 $\epsilon_\theta$ 进行外推，公式为 $\epsilon = \epsilon_\theta(x_t, t, \emptyset) + w(\epsilon_\theta(x_t, t, c) - \epsilon_\theta(x_t, t, \emptyset))$。本文的关键差异在于操作空间：不修改噪声预测，而是修改调制层的系数 $\alpha, \beta$，从而在不增加NFE（Number of Function Evaluations）的前提下改变生成轨迹。

### 调制空间引导机制

设计动机在于解决CFG在高权重下的过饱和问题，以及少步蒸馏模型缺乏CFG导致的语义对齐不足。本文提出Modulation Guidance (MG)，利用CLIP嵌入的几何可解释性，在调制空间进行正负提示词外推。设 $y_+$ 和 $y_-$ 分别为正负提示词经MLP映射后的全局条件向量，引导后的条件向量 $\hat{y}$ 计算如下：

$$ \hat{y} = y_0 + w(y_+ - y_-) $$

其中 $y_0$ 为原始提示词条件，$w$ 为引导权重。该公式的物理含义是：在调制系数空间中，沿“正提示词方向”偏移，远离“负提示词方向”，从而将去噪轨迹推向具有更优美学或语义属性的模式。由于 $\hat{y}$ 仅影响调制系数且共享于所有块，计算开销可忽略不计。

### 动态层间调度策略

恒定权重 $w$ 在高值时会导致模型忽视文本信息（Prompt Fidelity下降）。为解决此问题，本文引入动态调制引导，将调度维度从时间步 $t$ 转移至网络层 $i$。设计动机是借鉴动态CFG的思想，但针对调制层的特性进行适配。具体采用阶跃函数策略，跳过前 $i$ 层，仅在后续层应用引导：

$$ w_i = \begin{cases} 0 & \text{if } i < i_{\text{skip}} \\ w & \text{if } i \geq i_{\text{skip}} \end{cases} $$

这一策略允许模型在早期层保留原始文本语义，在后期层通过调制引导增强美学或特定属性（如计数、手部修复）。实验表明，动态引导在美学质量与提示词相关性之间取得了优于恒定引导的帕累托前沿，且无需针对新任务重新调参。

## 实验评估

实验基于FLUX schnell, FLUX dev, SD3.5 Large, HiDream及COSMOS模型，使用COCO 5k、GenEval及VBench基准。基线覆盖原始模型、Normalized Attention Guidance (NAG)、Concept Sliders及LLM增强提示词。缺失强基线包括TCFG、In-situ Autoguidance等动态CFG变体，导致无法直接对比MG与动态CFG在相同计算预算下的优劣。

| 模型 | 任务 | 指标 | 原始模型 | 调制引导 | 提升 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| FLUX schnell | Aesthetics | SbS Win Rate (%) | 23.1 | 35.8 | +12.7 |
| FLUX schnell | Complexity | SbS Win Rate (%) | 10.2 | 11.0 | +0.8 |
| FLUX schnell | Object Counting | GenEval (%) | 56 | 65 | +9 |
| FLUX schnell | Hands Correction | SbS Win Rate (%) | 39 | 61 | +22 |

核心数字显示，MG在FLUX schnell上对美学（+12.7%）和手部修复（+22%）提升显著，但在复杂度上提升有限（+0.8%）。GenEval计数任务提升9%，低于ATHENA-Adaptive的+22.3%（据领域综述，基线不同），表明MG在细粒度计数上并非最优，但在无需训练的约束下表现稳健。

消融实验聚焦于动态vs恒定引导。Figure 3(a)显示，动态引导在PickScore（美学）与CLIP Score（相关性）的权衡曲线上优于恒定引导。具体而言，恒定引导 $w=3.5$ 时CLIP Score降至30.2，而动态引导 $w=3.5$ 时CLIP Score保持30.5，同时PickScore更高。这证实了层间调度对避免语义丢失的关键作用。此外，将CLIP嵌入引入无CLIP的COSMOS模型后，单独使用CLIP无提升，仅当结合MG时才有效，证明MG依赖于CLIP嵌入的几何结构而非单纯的信息注入。

评估边界方面，人工评估（SbS）样本量较小（128-200 prompts），统计显著性依赖有限样本。自动指标（HPSv3, IR）在SD3.5 Large的复杂度任务上出现轻微下降，提示MG可能存在负迁移风险。代码已开源，但超参数（如 $i_{\text{skip}}$）需针对特定模型微调，缺乏通用默认值。

## 关联研究分析

从方法设计看，MG与Normalized Attention Guidance (NAG) 均利用正负提示词差异，但操作空间不同。NAG在注意力输出空间进行外推，需计算额外的注意力图，计算开销较大；MG在调制系数空间操作，仅涉及一个小MLP，开销可忽略。实验显示MG在SbS胜率上优于NAG 34%，根源在于调制层影响全局激活状态，而注意力仅影响局部token交互，全局校正对美学等整体属性更有效。

从问题动机看，MG与动态CFG（如TCFG）解决同一问题（质量-对齐权衡），但适用场景不同。TCFG通过截断后期引导节省计算，适用于多步模型；MG适用于无CFG的少步蒸馏模型（如FLUX schnell），弥补了蒸馏模型语义对齐的短板。两者是否可叠加使用？论文未探索MG与动态CFG的交互效应，可能存在收益递减或冲突，因为两者分别作用于噪声预测和调制系数，其耦合机制尚不明确。

## 总结

本文核心矛盾在于少步扩散模型缺乏CFG导致的语义对齐不足，以及全局文本条件在DiT中被忽视的潜力。切入点在于发现CLIP嵌入在调制空间中的几何可解释性，将其从被动条件重构为主动引导信号。方法上，通过在调制系数空间进行正负提示词外推并引入层间动态调度，实现了无需训练的质量提升。实验证明，MG在FLUX schnell上美学胜率提升12.7%，手部修复胜率提升22%，且计算开销可忽略。边界在于，MG依赖CLIP嵌入的存在与可解释性，在完全无CLIP架构中需额外微调引入嵌入，且对细粒度计数任务的提升（+9%）低于专用方法。当模型架构完全移除CLIP嵌入时，调制引导是否仍能通过其他全局特征（如T5 Pooled Embedding）实现类似效果，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.09268)
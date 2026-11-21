# HuggingFace最新推荐论文 ｜ELF: Embedded Language Flows ｜嵌入语言流

研究机构：美国麻省理工学院

作者：Keya Hu、Linlu Qiu、Yiyang Lu 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.10938)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.10938)

> 扩散语言模型（DLMs）旨在通过并行去噪突破自回归模型的串行延迟瓶颈，但现有连续DLM在少步采样下性能仍逊于离散DLM，且常依赖蒸馏或独立解码器。本文指出连续DLM的劣势源于算法设计而非语言离散本质，提出ELF框架。ELF在连续嵌入空间执行流匹配去噪，仅在最终步通过共享权重网络映射回离散Token，无需独立解码器。该设计以1/10训练Token实现了优于主流离散DLM的生成质量，但其在长序列复杂推理任务上的表现尚未验证。

## 研究背景

理解ELF需先厘清连续流匹配（Flow Matching, FM）与离散掩码扩散的差异。离散掩码扩散在Token空间操作，通过逐步替换[MASK]恢复文本，其训练目标常包含中间步的交叉熵损失，导致去噪轨迹被离散符号约束。连续FM则在嵌入空间定义从噪声到数据的线性插值路径，通过预测速度场或干净数据实现去噪。然而，早期连续DLM（如Diffusion-LM）在中间步引入Token级监督，削弱了连续流动态的灵活性；而潜在扩散模型（LDM）虽在压缩潜空间去噪，却需额外训练解码器，增加了推理开销。

当前DLM领域存在“连续vs离散”状态空间之争。离散DLM（如MDLM、Duo）凭借符号精确性在困惑度上占据优势，但多步采样导致推理慢，且CFG（Classifier-Free Guidance）在离散空间效果不佳。连续DLM试图利用嵌入空间的平滑性提升全局语义捕捉，但现有方法（如LangFlow、FLM）往往在中间步保留交叉熵损失或依赖蒸馏实现少步生成，未能充分发挥连续流匹配的潜力。ELF的切入点在于：若将离散化严格限制在最终步，中间步纯连续去噪，是否能在不增加解码器的前提下，实现比离散DLM更优的质量-效率权衡？

## 核心方法

### 连续嵌入空间流匹配参照系

ELF基于连续时间Flow Matching构建。给定离散Token序列 $\mathbf{s}$，通过预训练T5编码器映射为连续嵌入 $\mathbf{x}$。噪声路径定义为线性插值 $\mathbf{z}_t = t\mathbf{x} + (1-t)\boldsymbol{\epsilon}$，其中 $t \in [0,1]$。标准FM通常参数化速度场 $\mathbf{v}$，但ELF采用 $\mathbf{x}$-prediction，即直接预测干净嵌入 $\mathbf{x}_\theta = \text{net}_\theta(\mathbf{z}_t, t)$。这一选择解决了高维嵌入空间（如768维）下 $\mathbf{v}$-prediction 训练不稳定的问题，并为后续去噪与解码分支的权重共享奠定基础。

### 共享权重最终步离散化

ELF的核心创新在于消除独立解码器。在 $t=1$ 时，$\mathbf{z}_t$ 趋近于 $\mathbf{x}$，为创造非平凡输入，ELF引入Token级腐蚀过程 $\tilde{\mathbf{z}} = p\mathbf{x} + (1-p)\boldsymbol{\epsilon}$，其中 $p$ 从对数正态分布采样。网络在“decode”模式下预测 $\mathbf{x}_\theta(\tilde{\mathbf{z}})$，并通过可学习矩阵 $W$ 投影为Logits，最小化交叉熵损失：

$$ \mathcal{L}_{CE} = -\sum_{i=1}^{L} \log \text{softmax}(W \mathbf{x}_\theta(\tilde{\mathbf{z}}))_i $$

该公式表明，去噪网络（MSE损失）与解码网络（CE损失）共享同一组权重 $\theta$，仅通过模式Token区分。这一设计解决了LDM中解码器与去噪器参数冗余的问题，使推理时无额外模块开销，且 $\mathbf{x}$-prediction 与最终Token预测目标天然对齐，避免了 $\mathbf{v}$-prediction 在权重共享下的性能退化。

### 自条件CFG与SDE采样

为提升条件生成质量，ELF引入自条件机制构建CFG信号。训练时，网络以50%概率以自身预测 $\hat{\mathbf{x}}'$ 为条件进行二次前向传播，实现训练时CFG。推理时，利用连续速度场天然支持CFG的特性，通过调节引导尺度平衡质量与多样性。此外，ELF采用SDE-inspired采样器，通过噪声重注入尺度 $\gamma$ 控制随机性。实验显示 $\gamma=1.0$ 时，SDE采样在生成困惑度与熵之间取得最佳平衡，优于确定性ODE采样，表明噪声重注入有助于纠正早期去噪误差。

## 实验评估

| 任务 | 方法 | 参数量 | 指标 | 数值 |
| :--- | :--- | :--- | :--- | :--- |
| WMT14 De-En | ELF-B | 105M (+35M) | BLEU | 26.4 |
| WMT14 De-En | AR | 99M | BLEU | 25.2 |
| WMT14 De-En | MDLM | 99M | BLEU | 18.4 |
| XSum | ELF-B | 105M (+35M) | ROUGE-1 | 36.0 ± 0.13 |
| XSum | E2D2 | 99M | ROUGE-1 | 28.4 ± 0.11 |

ELF在OWT数据集上训练，使用45.2B有效Token，仅为MDLM（524.3B）的1/10。在WMT14德英翻译任务中，ELF-B以26.4的BLEU超越AR基线（25.2）和离散DLM基线MDLM（18.4）。在XSum摘要任务中，ELF-B的ROUGE-1达到36.0，显著优于E2D2（28.4）和MDLM（33.4）。这些结果表明，连续DLM在少步采样下不仅能匹敌离散DLM，还能在条件生成任务上超越AR模型，且无需蒸馏。

消融实验显示，Logit-normal时间调度在少步采样下显著降低生成困惑度，优于均匀调度。SDE采样中，$\gamma$ 从0.5增至3.0时，ELF-L的Gen. PPL从37.50降至21.37，但熵从5.41降至5.26，表明适度随机性有助于提升质量。CFG尺度在2时效果最佳，过高（如4.0）导致性能下降，验证了连续空间中CFG的有效性。

ELF在LM1B基准上未报告PPL，无法直接对比LangFlow（30.0）。评估协议主要关注生成困惑度与条件生成指标，缺乏对长序列推理能力（如GSM8K）的测试。代码已开源，但训练依赖TPU v5p集群，复现成本较高。

## 关联研究分析

从方法设计看，ELF与LangFlow同属连续DLM路线，但LangFlow在中间步保留交叉熵损失以增强符号精确性，而ELF仅在最终步离散化。这一差异源于ELF对 $\mathbf{x}$-prediction 与共享权重解码的依赖：若中间步引入Token级监督，将破坏去噪与解码分支的权重共享一致性。LangFlow依赖特定噪声调度避免嵌入坍缩，ELF则通过 $\mathbf{x}$-prediction 在高维空间实现稳定训练，两者在“连续空间平滑性”与“离散符号精确性”的取舍上存在根本分歧。

从问题动机看，ELF与MDLM代表连续与离散DLM的两极。MDLM通过掩码扩散在Token空间操作，其优势在于符号精确性，但劣势在于多步采样慢且CFG无效。ELF通过连续流匹配解决采样效率问题，但面临中间步语义漂移风险。ELF未验证在长序列生成中，仅最终步离散化是否会导致早期Token错误累积，这是其与MDLM在长文本任务上性能差异的关键未知点。

## 总结

ELF旨在解决连续DLM在少步采样下性能不及离散DLM且依赖独立解码器的矛盾。其切入点在于将离散化严格限制在最终步，利用 $\mathbf{x}$-prediction 实现去噪与解码的权重共享，从而在不增加推理模块的前提下提升效率。ELF以45.2B Token训练，在WMT14上达到26.4 BLEU，超越AR基线，证明了连续DLM的竞争力。然而，ELF的实验局限于短序列条件生成，未测试长序列推理任务，且LM1B PPL缺失。当序列长度增加时，仅最终步离散化是否足以维持全局一致性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.10938)
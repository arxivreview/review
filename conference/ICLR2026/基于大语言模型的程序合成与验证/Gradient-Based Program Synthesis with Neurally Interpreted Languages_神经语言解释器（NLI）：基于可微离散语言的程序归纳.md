# ICLR2026最新论文 ｜Gradient-Based Program Synthesis with Neurally Interpreted Languages ｜神经语言解释器（NLI）：基于可微离散语言的程序归纳

研究机构：荷兰阿姆斯特丹大学、加拿大阿尔伯塔大学

作者：Matthew V. Macfarlane、Clément Bonnet、Herke van Hoof 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.18907)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.18907)

> 程序归纳旨在仅从输入输出对推断潜在程序逻辑，传统符号方法受限于人工设计领域特定语言（DSL）的泛化瓶颈，而纯神经方法因权重纠缠难以实现组合式泛化。本文提出神经语言解释器（NLI），通过端到端学习离散符号语言与可微神经执行器，在测试时利用梯度搜索优化程序表示，从而在长度外推与新原语组合任务上突破现有神经模型的泛化边界。该方法在自定义基准上实现了显著的组合泛化，但其泛化能力是否可迁移至复杂形式化验证场景仍存疑。

## 研究背景

程序归纳的核心困境在于表示的离散性与优化的连续性之间的冲突。符号方法如DeepCoder（Balog et al., 2017）依赖预定义DSL，虽具备可解释性，但搜索空间随原语数量呈组合爆炸，且无法跨域迁移。神经方法如Latent Program Network (LPN)（Macfarlane & Bonnet, 2025）将程序映射为连续潜在向量，虽解决了搜索效率问题，但连续表示缺乏组合结构，导致模型在训练分布外（OOD）任务上泛化能力接近于零。

该领域长期存在“符号-神经”权衡：符号系统提供组合泛化但扩展性差，神经系统扩展性强但泛化差。现有神经程序归纳方法，包括In-Context Learning (ICL)和Test-Time Training (TTT)，均无法有效重组已学习概念以解决新任务。本文切入点在于将程序表示从连续向量改造为离散Token序列，借鉴VQ-VAE与Gumbel-Softmax技术，使模型能像符号系统一样重组原语，同时保留神经网络的端到端可微性，从而在测试时通过梯度下降在离散程序空间中高效搜索。

## 核心方法

### 方法参照系

NLI属于潜在适应网络（Latent Adaptation Network, LAN）架构，其标准流程为：编码器从输入输出对推断潜在表示，解码器执行该表示以预测输出。与LPN等连续潜在空间方法的关键差异在于，NLI的潜在表示是离散Token序列，且解码器是逐Token执行的神经解释器，而非单次前向传播的单体模型。

### 离散程序表示学习

编码器（程序归纳器 $q_\phi$）将输入输出对映射为离散程序表示。设计动机在于解决连续潜在空间无法表达组合结构的问题。编码器首先通过Transformer对每个输入输出对生成嵌入，再对序列位置进行平均池化以获得置换不变的规范嵌入 $\bar{e}_t$。随后，通过共享前馈网络投影至代码本（Codebook）分布，并利用Gumbel-Softmax松弛实现可微离散采样：

$$ z_t = \text{Softmax}\left(\frac{\log \bar{e}_t + g_t}{\tau_e}\right) $$

其中 $g_t \sim \text{Gumbel}(0,1)$，$\tau_e$ 为温度参数。该机制使模型能学习紧凑的原语词汇表，并通过重组这些原语构建新程序，而非为每个任务学习独立表示。

### 可微神经执行器与梯度搜索

解码器（神经解释器 $p_\theta$）逐Token执行程序，通过循环状态 $s_t$ 更新中间计算结果。设计动机在于打破LPN固定计算步长的限制，允许程序长度随Token数量增长，从而解决更复杂问题。执行过程引入Skip-Gating机制，允许模型忽略无效Token。测试时，NLI利用执行器的可微性进行梯度搜索，优化目标为最大化规范数据似然：

$$ \max_{\bar{e}} \mathbb{E}_{q_\phi, p_\theta} \left[ \log p_\theta(y|x, z(\bar{e}, \tau_e, g)) \right] $$

通过温度退火与多起点并行梯度上升，NLI在离散Token的连续松弛空间中搜索最优程序，避免了传统符号搜索的组合爆炸，同时通过离散约束防止过拟合。

## 实验评估

实验在自定义组合泛化基准（Shift-L, Shift-P, Comp-I）及DeepCoder组合性版本上进行，基线包括ICL、TTT、LPN及其离散变体D-LPN。NLI Gradient Search在OOD任务上表现显著优于所有基线，而基线在Shift任务上OOD准确率接近0%。

| 方法 | Shift-L OOD | Shift-P OOD | Comp-I OOD |
| :--- | :--- | :--- | :--- |
| In-Context / TTT | 0.00 | 0.00 | 0.13 / 0.14 |
| LPN Gradient Search | 0.03 | 0.00 | 0.29 |
| D-LPN Gradient Search | 0.01 | 0.00 | 0.20 |
| NLI Gradient Search | 0.99 | 1.00 | 0.91 |

NLI在Shift-L（长度外推）达99%，Shift-P（原语提取）达100%，Comp-I（新组合）达91%。消融显示，Base Inference与Prior Search性能与基线相当，证明梯度搜索是泛化的关键。离散表示学习使模型能复用Token 231（单步移位）与476（双步移位）构建OOD程序，验证了组合泛化源于原语重组而非记忆。

评估边界受限于自定义基准的序列长度（20）与任务复杂度，未涉及真实代码或形式化验证基准。论文未提供代码与详细超参数，可复现性依赖Gumbel-Softmax与Transformer通用实现。

## 关联研究分析

从问题动机看，NLI与DeepCoder均解决程序归纳，但DeepCoder依赖人工DSL与符号搜索，NLI则端到端学习语言。差异根源在于任务特性：DeepCoder假设原语已知，NLI假设原语未知且需从数据中发现。NLI的离散语言学习解决了DSL设计瓶颈，但牺牲了符号系统的可解释性，其Token语义需事后分析（如Figure 2所示），而非显式定义。

从方法设计看，NLI与LPN同属LAN架构，但LPN使用连续潜在向量，NLI使用离散Token序列。LPN的组合泛化失败源于连续空间缺乏组合结构，NLI通过离散化引入组合性。然而，NLI的梯度搜索在离散松弛空间中进行，其收敛性依赖温度退火策略，而LPN的连续搜索更平滑但易陷入局部最优。NLI是否能在高维程序空间中保持搜索效率，论文未给出回答。

## 总结

NLI旨在解决符号方法扩展性差与神经方法泛化差的矛盾，通过端到端学习离散语言与可微执行器，在测试时利用梯度搜索优化程序表示。该方法在自定义基准上实现了99-100%的OOD准确率，显著优于LPN与ICL。其边界在于评估任务局限于简单序列移位与组合，未验证在复杂逻辑约束或大规模代码上的有效性。当程序复杂度超出训练分布时，离散Token的重组能力是否仍能维持泛化，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.18907)
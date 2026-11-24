# ICLR2026最新论文 ｜SliderQuant: Accurate Post-Training Quantization for LLMs ｜滑动层量化（SliderQuant）：基于层间敏感度差异的自适应PTQ框架

研究机构：英特尔实验室

作者：Shigeng Wang、Chao Li、Yangyuxuan Kang 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.25284)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.25284)

> 导读 大语言模型（LLM）低比特量化面临的核心矛盾是：现有顺序量化框架（层级、块级或多块级）假设所有层对量化误差的敏感度均等，但在4-bit权重-激活（W4A4）等严苛设置下，浅层与深层的误差累积效应显著高于中间层，导致模型性能崩塌。本文指出这一“平等对待”假设是精度损失的关键被忽略因素，提出SliderQuant框架，通过自适应滑动窗口机制差异化处理不同层级的量化难度。该方法在W4A4设置下显著优于GPTQ、SmoothQuant等主流基线，但其优势是否源于对激活离群值的间接抑制而非直接处理，仍需进一步验证。

## 研究背景

LLM量化旨在将高精度权重映射至低精度离散网格以节省显存，但离散化引入的误差在深层Transformer中逐层累积。传统顺序量化框架将模型划分为独立单元（层或块）并依次量化，其理论基础是二阶泰勒展开下的局部误差补偿。然而，当比特宽度降至4-bit以下时，这种局部近似失效，因为前一层量化误差会污染后一层的输入分布，使得后续层的量化目标发生漂移。

现有PTQ方法如GPTQ（Frantar et al., 2023）和SmoothQuant（Xiao et al., 2023）虽利用Hessian矩阵或激活缩放缓解误差，但均假设层间独立性或采用固定粒度的块级量化。OmniQuant（Shao et al., 2024）和CBQ（Ding et al., 2025）引入滑动窗口以捕捉长距离依赖，但窗口大小固定，无法适应层间敏感度的非均匀分布。本文切入点在于实证发现：浅层（特别是第一层）和深层（特别是最后一层）对量化误差的敏感度远高于中间层，且这种敏感度差异在W4A4设置下被放大。因此，需要一种能动态调整量化协同范围的框架，以匹配层间的异构敏感度。

## 核心方法

### 固定大小滑动量化参照系

现有PTQ方法可统一视为固定大小滑动量化（Fixed-Size Sliding Quantization）的特例。设模型有 $L$ 层，窗口大小为 $s$，移动步长为 $i$，则窗口内权重矩阵集合为 $\mathbf{W} = \{\mathbf{W}_1, ..., \mathbf{W}_s\}$。优化目标为最小化窗口输出特征与原始输出的均方误差：

$$ \min_{\hat{\mathbf{W}}} \| F(\hat{\mathbf{W}}, \mathbf{X}) - F(\mathbf{W}, \mathbf{X}) \|^2 $$

其中 $F(\cdot, \cdot)$ 为窗口前向传播函数，$\mathbf{X}$ 为校准输入。当 $s=1, i=1$ 时为层级量化；当 $s$ 等于块大小时为块级量化。该参照系的局限在于 $s$ 和 $i$ 全局固定，导致浅、中、深层接受相同的量化协同强度，无法针对敏感层提供额外保护。

### 层间滑动量化（Inter-Layer Sliding Quantization）

设计动机：固定窗口无法区分浅/深层的高敏感度与中间层的低敏感度，导致误差在敏感层累积。本文引入层间滑动量化，将模型分为浅层（$L_s$）、中间层（$L_i$）和深层（$L_d$）三段，分别采用渐进扩展滑动窗口（PESW）、固定大小滑动窗口（FSSW）和渐进收缩滑动窗口（PCSW）。

PESW从第一层开始，窗口大小从1逐步增加至 $L_s$，使第一层始终参与优化，建立“局部到全局”的协同路径。PCSW反向操作，从所有深层开始，窗口大小逐步收缩至1，使最后一层始终作为锚点，建立“全局到局部”的协同。中间层采用 $s=2, i=1$ 的FSSW，确保每层被优化频率均匀。这种分段设计使敏感层（首/尾）获得更密集的量化协同，而中间层保持计算效率。

### 层内滑动量化（Intra-Layer Sliding Quantization）

设计动机：层间滑动仅解决层间协同，但窗口内部各层仍按固定顺序量化，未充分利用窗口内的渐进性。本文引入层内滑动量化，在每个层间窗口内，对 $s$ 层权重按比率 $\gamma$ 进行渐进扩展量化。具体地，窗口内第 $k$ 层的量化依赖于前 $k-1$ 层的量化结果，形成增量式联合优化。该机制进一步细化了窗口内的误差传播控制，使量化过程从“块级独立”转向“层内渐进”，从而在W4A4设置下显著降低重建误差。

## 实验评估

实验覆盖Llama2-7B/13B/70B、Llama3-8B、Qwen2.5-7B/14B等模型，评估基准包括WikiText2、C4（语言生成）及PIQA、ARC、HellaSwag、MMLU等（常识推理）。基线涵盖GPTQ、AWQ、SmoothQuant、OmniQuant、CBQ及旋转类方法（QuaRot、SpinQuant、FlatQuant）。

| 模型 | 设置 | 方法 | WikiText2 PPL | C4 PPL |
| :--- | :--- | :--- | :--- | :--- |
| Llama2-7B | W4A4 | SmoothQuant | 83.12 | 77.27 |
| Llama2-7B | W4A4 | OmniQuant | 14.26 | 18.02 |
| Llama2-7B | W4A4 | CBQ | 12.73 | 14.45 |
| Llama2-7B | W4A4 | SliderQuant | **8.34** | **11.10** |
| Llama2-13B | W4A4 | SmoothQuant | 46.62 | 43.19 |
| Llama2-13B | W4A4 | OmniQuant | 12.30 | 14.55 |
| Llama2-13B | W4A4 | CBQ | 8.48 | 11.71 |
| Llama2-13B | W4A4 | SliderQuant | **7.62** | **10.26** |

在W4A4设置下，SliderQuant在Llama2-7B上PPL为8.34，显著优于OmniQuant（14.26）和CBQ（12.73），但略逊于旋转类方法SliderQuant+（5.71）。这表明层间协同机制在无需额外推理开销的情况下，已能接近旋转方法的性能。

消融实验显示，层间滑动量化（Inter-S）与层内滑动量化（Intra-S）均贡献显著。仅使用Inter-S时，W4A4 PPL从12.73降至9.13；加入Intra-S后进一步降至8.34。窗口大小 $L_s, L_d$ 的消融表明，$L_s=4, L_d=4$ 为精度-效率最优平衡点，更大窗口（如 $L_s=6$）带来边际收益递减。

评估边界方面，论文未报告置信区间，且W4A16设置下性能未超越OSTQuant等最新SOTA（据领域综述，OSTQuant W4A16 MMLU为70.92，本文Llama2-13B W4A16 Avg为76.90，但MMLU单项未直接对比）。代码已开源，超参数（$L_s, L_d, \gamma$）提供默认值，但不同模型间的自适应调整策略未详细讨论。

## 关联研究分析

从问题动机看，SliderQuant与CALM（Zhang et al., 2025）均关注层间敏感度差异，但CALM通过动态选择PTQ算法（如GPTQ vs AWQ）实现异构量化，而SliderQuant通过调整窗口大小实现协同强度异构。CALM依赖算法评估开销，SliderQuant依赖窗口计算开销，两者在计算成本与精度提升的权衡上存在根本差异。SliderQuant的优势在于无需额外算法评估，但可能牺牲了对特定层最优算法的匹配能力。

从方法设计看，SliderQuant与QuIP#（Tseng et al., 2024）在极低比特（2-bit）下形成互补。QuIP#通过随机旋转重塑权重分布，解决离群值问题；SliderQuant通过层间协同抑制误差累积，但未直接处理离群值。在W2A16设置下，SliderQuant PPL为9.59（Llama2-7B），而QuIP#未在该设置下报告数值，但据领域综述，QuIP#在2-bit下表现优异。这暗示SliderQuant在W4A4下的优势可能部分源于对离群值的间接缓解，而非直接解决分布失真问题。

## 总结

SliderQuant针对PTQ中“层间敏感度均等”假设的失效，提出自适应滑动窗口框架，通过PESW/PCSW差异化处理浅/深层，结合层内增量量化，在W4A4设置下将Llama2-7B PPL从12.73（CBQ）降至8.34。其边界在于：未直接处理激活离群值，且在W4A16下未超越旋转类SOTA。当模型深度增加至70B以上时，层间敏感度分布是否仍符合“首尾敏感、中间平缓”的规律，论文未给出跨规模的系统性验证。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.25284)
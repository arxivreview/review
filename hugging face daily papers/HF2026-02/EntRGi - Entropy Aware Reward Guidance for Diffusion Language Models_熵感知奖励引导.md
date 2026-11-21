# HuggingFace最新推荐论文 ｜EntRGi: Entropy Aware Reward Guidance for Diffusion Language Models ｜熵感知奖励引导

研究机构：美国德克萨斯大学奥斯汀分校

作者：Atula Tejaswi、Litu Rout、Constantine Caramanis 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.05000)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.05000)

> 离散扩散语言模型（Discrete Diffusion Language Models, dLLMs）在推理时面临离散Token不可微的困境，导致无法直接利用奖励模型梯度优化生成质量。现有方法要么使用连续松弛导致奖励模型输入分布失配，要么使用直通估计器（Straight-Through Estimator, STE）导致梯度更新与评估点错位。本文提出EntRGi，通过模型预测熵动态加权连续松弛与硬Token嵌入，在冻结模型参数的前提下实现免训练推理时引导。该方法在7B参数模型上验证了有效性，但其对奖励模型规模与Tokenizer匹配性的依赖限制了通用性。

## 研究背景

dLLMs通过并行去噪生成文本，其核心优势在于双向上下文与全局一致性，但离散Token的不可微性阻断了反向传播路径。当引入外部奖励模型（Reward Model, RM）进行推理时引导时，RM通常基于自回归（AR）骨干训练，仅接受离散文本输入。若将dLLM输出的连续松弛嵌入直接输入RM，会因分布外（Out-of-Distribution, OOD）输入导致梯度信号失真；若强行离散化，则STE机制下梯度评估点与优化目标点不一致，引发优化方向错误。

主流免训练引导方法分为梯度无关与梯度相关两类。梯度无关方法如Best-of-N（BoN）依赖采样效率，在稀疏奖励信号下表现不佳；梯度相关方法如APS（Rout et al., 2025c）采用STE处理离散性，但忽略了熵对梯度可靠性的影响。早期去噪步骤中，dLLM预测分布熵较高，此时连续松弛远离有效Token，STE的近似误差被放大。本文切入点在于识别熵作为调节连续松弛与硬Token权衡的关键变量，提出动态插值机制以平衡梯度保真度与RM可靠性。

## 核心方法

### 方法参照系

标准dLLM推理流程为：输入掩码序列 $z_t$，计算掩码位置Logits $\psi_l$，采样Token并更新序列。奖励引导旨在修改 $\psi_l$ 以最大化RM得分。现有方法APS固定使用STE，即始终将软嵌入离散化后输入RM，忽略了不同熵水平下离散化带来的不同误差模式。本文问题与通用流程的关键差异在于：需根据当前预测分布的不确定性动态调整RM输入构造方式。

### 熵加权嵌入构造

EntRGi的核心创新在于构造RM输入嵌入 $\hat{e}_l$，其设计动机是解决APS在高熵位置下STE近似误差过大的问题。对于掩码位置 $l$，计算归一化熵 $w_l = H(q_l)/\log K$，其中 $q_l = \text{softmax}(\psi_l/\tau)$ 为预测分布，$K$ 为词表大小。$\hat{e}_l$ 定义为连续松弛 $\bar{e}_l = \sum_{i \in V} q_{l,i} E_R[i]$ 与硬Token嵌入 $\tilde{e}_l = E_R[x_l]$ 的插值：

$$ \hat{e}_l = \bar{e}_l + \text{sg}[w_l (\tilde{e}_l - \bar{e}_l)] $$

其中 $\text{sg}[\cdot]$ 表示停止梯度。该公式的物理含义是：低熵时 $w_l \to 0$，$\hat{e}_l \approx \bar{e}_l$，RM接收接近有效Token的连续输入，梯度可靠；高熵时 $w_l \to 1$，$\hat{e}_l \approx \tilde{e}_l$，RM接收离散Token，避免OOD输入。

### 梯度更新与误差分析

更新步骤为 $\psi_l \leftarrow \psi_l + \eta \nabla_{\psi_l} R(\hat{e})$，其中 $\eta$ 为引导尺度。由于 $\text{sg}$ 阻断硬嵌入项的梯度，梯度仅通过 $\bar{e}_l$ 流动。定义近似误差 $E_l = \|\hat{e}_l - \bar{e}_l\|_2$ 与对齐误差 $D_l = \min_k \|\hat{e}_l - E_R[k]\|_2$。APS中 $w_l=1$，$E_l = \|\tilde{e}_l - \bar{e}_l\|_2$ 在高熵时显著；EntRGi中 $w_l$ 随熵变化，低熵时 $E_l \to 0$ 且 $D_l \to 0$，高熵时 $D_l \to 0$ 但 $E_l$ 被 $w_l$ 抑制。该机制确保在去噪全程中，RM输入始终处于其可靠解释范围内，从而提供更准确的梯度反馈。

## 实验评估

实验基于Dream-v0-Instruct-7B模型，使用Skywork-Reward系列（0.6B/1.7B/4B）作为RM，在Reward-Bench-2、RMBench、JudgeBench三个基准上评估。基线包括BoN、Expectation（纯连续松弛）和APS。对比缺失AR模型基线（如Qwen-2.5）及RL后训练方法（如ESPO），因任务性质不同（推理时引导 vs 参数更新），直接对比受限。

| 方法 | Reward-Bench-2 Top@1 | RMBench Top@1 | JudgeBench Top@1 |
| :--- | :--- | :--- | :--- |
| BoN | 2.18±0.22 | 2.99±0.23 | 2.95±0.28 |
| Expectation | 2.05±0.23 | 3.13±0.29 | 3.95±0.27 |
| APS | 2.95±0.04 | 3.95±0.02 | 3.62±0.27 |
| EntRGi | 3.07±0.22 | 3.91±0.30 | 3.91±0.30 |

EntRGi在 $\tau=0.7$ 时全面优于APS，Reward-Bench-2 Top@1提升0.12，JudgeBench提升0.29。消融显示，移除STE使EntRGi退化为Expectation，证实STE在高熵位置的必要性。LMUnit外部评估显示EntRGi在Reward-Bench-2上从4.19提升至4.22，表明增益非奖励黑客。

评估边界方面，实验仅覆盖共享Tokenizer的模型对，LLaDA因Tokenizer不匹配被排除。超参数 $M=3$（RM梯度步数）为固定值，未探索 $M$ 对延迟的影响。代码已开源，但GPU配置与具体训练细节未在正文详述，可复现性依赖附录。

## 关联研究分析

从问题动机看，EntRGi与Fast-dLLM同属免训练推理优化，但目标正交：Fast-dLLM通过KV缓存减少计算冗余以提升速度，EntRGi通过梯度引导提升质量。二者可结合，但Fast-dLLM的加速策略可能改变预测分布熵，进而影响EntRGi的插值权重，这种耦合效应未被探索。从方法设计看，EntRGi与ESPO在“推理增强”目标上竞争，但ESPO通过RL更新参数，EntRGi冻结参数。ESPO在GSM8K达82.1%，而EntRGi未在数学基准上评估，其是否能在严格逻辑任务上替代RL后训练，因缺乏同基准对比而存疑。

## 总结

EntRGi解决的核心矛盾是离散扩散中奖励模型输入分布与模型输出分布的失配。其切入点在于识别熵作为调节连续松弛与硬Token权衡的关键变量，通过动态插值确保RM始终接收可靠输入。方法上，EntRGi以熵加权插值替代固定STE，证明了在7B模型上，该机制可将Reward-Bench-2 Top@1从2.95提升至3.07。边界在于其依赖RM与dLLM共享Tokenizer，且未验证在数学等严格逻辑任务上的有效性。当奖励模型规模从0.6B扩展至4B时，EntRGi的增益是否线性增长，论文Figure 4显示正相关但未给出饱和点，这一Scaling Law的边界条件值得进一步探究。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.05000)
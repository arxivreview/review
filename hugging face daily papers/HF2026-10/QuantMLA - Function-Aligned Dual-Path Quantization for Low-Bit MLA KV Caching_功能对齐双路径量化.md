# HuggingFace最新推荐论文 ｜QuantMLA: Function-Aligned Dual-Path Quantization for Low-Bit MLA KV Caching ｜功能对齐双路径量化

研究机构：美团、华南理工大学

作者：Zunhai Su、Yuxuan Sun、Jianchao Tan 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2609.36760)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2609.36760)

> 导读 多头潜在注意力（Multi-Head Latent Attention, MLA）通过共享低秩潜在空间压缩键值缓存，但其内存占用仍随上下文长度线性增长，且现有量化方法仅压缩内容缓存而保留高精度旋转位置编码（RoPE）键，导致联合低比特压缩长期处于未探索状态。本文切入点在于揭示MLA双路径在匹配缓存重构误差下，RoPE路径误差被显著放大的机制，并据此设计功能对齐的独立量化目标。具体做法是推导路径特异性离线可融合变换空间，分别以注意力输出重构和位置QK重构为优化目标，实现内容缓存与RoPE键缓存的联合INT4量化。该方案在四个MLA模型家族上验证了精度保持与系统效率，但其结论严格限定于MLA架构，对非MLA架构的泛化性存疑。

## 研究背景

当LLM处理长上下文时，MLA架构将键值投影至低维潜在空间 $C \in \mathbb{R}^{n \times d_c}$ 以替代多头注意力（MHA）的独立键值存储，同时解耦出独立的RoPE键 $K_P \in \mathbb{R}^{n \times d_r}$ 用于位置匹配。这种双路径设计虽降低了缓存维度，但内容路径同时参与注意力匹配与值聚合，而RoPE路径仅影响位置得分，二者误差传播路径存在本质差异。

MLA量化领域的主流路线聚焦于内容缓存的低比特化，如FlashMLA将DeepSeek-V3.2内容缓存压缩至FP8，但均保留RoPE键为BF16精度。这一保守策略源于对RoPE路径量化影响的认知空白：现有方法未系统分析RoPE误差如何经由位置得分扰动放大至注意力输出，导致联合低比特压缩缺乏理论指导。本文切入点在于建立双路径误差的功能对齐模型，通过解耦两条路径的误差传播机制，为联合量化提供可解释的优化目标。

## 核心方法

### 双路径误差解耦参照系

MLA量化通常将内容缓存与RoPE键视为同质数据统一处理，但本文指出二者功能角色不同：内容路径误差通过匹配与聚合双通道传播，RoPE路径误差仅通过位置得分单通道传播。这一差异决定了统一量化目标无法同时优化两条路径，需分别设计符合各自功能特性的变换空间与损失函数。

### 路径特异性离线可融合变换

针对内容路径，本文引入正交旋转 $R_C$ 与通道缩放 $S_C$，将原始潜在 $c = u\Gamma$ 重参数化为 $z_C = uR_CS_C$。该变换通过补偿消费者权重 $\tilde{f}_W = S_C^{-1}R_C^\top \Gamma W$ 保持全精度计算等价，且因RMSNorm的旋转等变性可完全离线融合至模型权重，消除在线变换开销。针对RoPE路径，受限于RoPE成对旋转结构，本文推导了RoPE兼容变换命题：仅允许在RoPE频率对内部进行成对旋转 $R_P = \text{blockdiag}(R_i)$ 与成对缩放 $S_P = \text{blockdiag}(s_i I_2)$，通过互逆补偿 $Q'_P = Q_P R_P S_P^{-1}$ 与 $K'_P = K_P R_P S_P$ 保持位置得分不变。

$$
z_C f_W = u R_C S_C (S_C^{-1} R_C^\top \Gamma W) = u \Gamma W = c W
$$

该公式表明内容路径变换在数学上严格保持全精度输出，其设计动机在于解决通用量化方法（如SmoothQuant）未考虑MLA共享潜在结构导致的精度损失。

### 功能对齐学习目标

内容路径采用注意力输出重构损失，最小化量化后注意力输出与BF16教师的归一化均方误差：

$$
\mathcal{L}_C = \mathbb{E}_{x,\ell} \frac{\|Y_\ell(Q_R,S_C(C), K_P; x) - Y_\ell(C, K_P; x)\|_F^2}{\max\{\|Y_\ell(C, K_P; x)\|_F^2, \epsilon_C\}}
$$

该目标捕获匹配与聚合的耦合误差及交互项，弥补了仅重构得分的损失函数遗漏。RoPE路径采用位置QK重构损失，直接最小化位置得分扰动：

$$
\mathcal{L}_P = \mathbb{E}_{x,\ell} \frac{\|\Omega \odot (\hat{Q}_{P,\ell} \tilde{K}_{P,\ell}^\top - Q_{P,\ell} K_{P,\ell}^\top)\|_F^2}{\max\{\|\Omega \odot Q_{P,\ell} K_{P,\ell}^\top\|_F^2, \epsilon_P\}}
$$

该目标基于有限输出界命题，证明位置得分误差直接控制输出失真上界，其设计动机在于解决RoPE路径误差放大机制下，通用重构目标无法有效约束位置得分扰动的问题。

## 实验评估

实验覆盖四个MLA模型家族（DeepSeek-V2-Lite、Moonlight-16B-A3B、LongCat-Flash-Lite、GLM-4.7-Flash），对比RTN、SmoothQuant†、QuaRot†三个基线，其中后两者为本文适配的MLA版本。基线审计显示，未对比FlashMLA等FP8 MLA专用方法，可能因精度损失过大或实现复杂，但削弱了与现有工业级方案的直接可比性。

| 模型 | 精度 | 方法 | MMLU (%) | GSM8K (%) | HumanEval (%) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| DeepSeek-V2-Lite | C4R4 | QuantMLA | 57.95 | 35.25 | — |
| DeepSeek-V2-Lite | C4R4 | QuaRot† | 55.66 | 30.71 | — |
| Moonlight-16B-A3B | C4R4 | QuantMLA | 69.71 | 74.53 | — |
| Moonlight-16B-A3B | C4R4 | QuaRot† | 67.73 | 71.87 | — |
| LongCat-Flash-Lite | C4R4 | QuantMLA | 69.75 | 54.80 | 71.34 |
| LongCat-Flash-Lite | C4R4 | QuaRot† | 64.67 | 54.40 | 56.71 |

在C4R4配置下，QuantMLA在DeepSeek-V2-Lite MMLU上达57.95%，较最强基线QuaRot†高2.29个百分点；在LongCat-Flash-Lite HumanEval上达71.34%，较QuaRot†高14.63个百分点，表明功能对齐目标在推理与代码任务上优势更显著。

消融实验显示，内容路径变换贡献1.22个百分点，RoPE路径变换贡献3.19个百分点，混合精度策略额外贡献1.64个百分点。RoPE路径变换的边际收益最大，验证了误差放大机制分析的有效性；但C2R4配置下GLM-4.7-Flash任务间波动增大，表明极端内容压缩对部分基准敏感。

评估边界方面，论文未报告LongBench等长上下文综合基准，侧重推理与代码任务；代码声明“接收后发布”，当前不可复现；GPU环境为8×H20，未提供超参数细节。

## 关联研究分析

从问题动机看，本文与KIVI、KVQuant等通用KV量化方法的核心差异在于架构特异性：后者基于MHA/GQA的键值分布差异设计非对称量化，而本文针对MLA双路径功能解耦设计独立目标。这一差异源于MLA共享潜在结构使内容路径误差传播路径更复杂，通用量化方法无法捕获匹配-聚合耦合效应。从方法设计看，本文与SmoothQuant、QuaRot的变换思想同源，但关键差异在于离线可融合性：后者的变换需在线执行，而本文通过补偿消费者权重将变换完全融合至模型参数，消除推理时开销。这一设计选择是否增加校准复杂度，论文未给出量化对比，但300步校准在128条WikiText-2序列上的开销相对可接受。

## 总结

本文要解决的核心矛盾是MLA双路径量化误差的非对称放大与现有方法仅压缩内容缓存的局限。切入点在于建立功能对齐误差模型，通过解耦路径特异性变换空间与优化目标，实现联合INT4量化。方法上，推导RoPE兼容变换并设计注意力输出重构与位置QK重构双目标，证明在四个MLA家族上C4R4配置下MMLU精度较最强基线高2.29-4.82个百分点，128K上下文下实现3.59×缓存压缩。边界在于结论严格限定于MLA架构，未验证MHA/GQA泛化性，且C2R4配置下部分任务精度波动增大。当支持集从128条WikiText-2扩展至更大规模时，RoPE路径变换的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2609.36760)
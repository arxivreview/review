# CVPR2026最新论文 ｜Towards Decompositional Human Motion Generation with Energy-Based Diffusion Models ｜基于能量扩散模型的运动分解生成

作者：Jianrong Zhang、Hehe Fan、Yi Yang

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ff82e10dfbb7)

> 文本驱动人体运动生成（Text-to-Motion Generation, T2M）旨在从自然语言合成逼真且语义一致的动作序列，核心挑战在于如何捕捉动作内部的组合结构而非仅建立整体映射。现有主流方法将运动视为不可分割的整体，缺乏对动作原语的解耦能力，导致无法像人类一样通过重组已知概念生成新颖动作。本文提出DEMOGEN，一种基于能量基扩散模型（Energy-Based Diffusion Models, EBDs）的组合训练范式，通过多概念能量聚合实现运动概念的自适应解耦与重组。该方法在组合生成任务上显著优于现有状态-of-the-art（SOTA）模型，但其对分解式文本标注的依赖及在纯文本到运动任务上的边际增益有限，限制了其通用性。

## 研究背景

理解复杂动作的关键在于将其分解为可复用的简单原语。例如，“边挥手边走直线”可分解为“挥手”与“走直线”两个独立概念。这种分解能力使得人类无需大量练习即可通过重组已知原语生成新动作。在计算建模中，这要求模型不仅学习文本到运动的映射，还需捕捉运动内部的语义结构。去噪扩散概率模型（Denoising Diffusion Probabilistic Models, DDPMs）通过迭代去噪生成连续运动序列，其去噪网络可解释为能量函数梯度，为多概念能量聚合提供了理论基础。向量量化变分自编码器（Vector Quantized-Variational Autoencoders, VQ-VAEs）则将运动离散化为潜变量，作为能量函数作用的基础表示。

T2M领域的主流路线包括扩散模型与自回归模型。扩散模型在连续保真度上占优，但通常学习单一文本到单一运动的整体映射，忽略了动作的组合性。自回归模型虽具备语义组合性，但依赖离散令牌序列，难以直接处理连续运动中的细粒度时空模式。现有组合生成方法如EnergyMoGen仅通过能量聚合实现推理时的组合，未解决训练时的概念解耦问题。本文切入点在于：如何在缺乏分解式运动真值的情况下，通过能量基扩散模型实现运动概念的自适应解耦，从而支持灵活的概念重组。

## 核心方法

### 方法参照系

标准T2M流程为：运动编码至潜空间→单一文本条件去噪→解码至运动空间。本文关键差异在于：将单一文本条件替换为多概念文本嵌入集合，通过能量聚合计算预测噪声，实现概念级分解。

### 能量聚合机制

设计动机：解决现有方法将运动视为整体、无法解耦独立概念的问题。在噪声水平 $t$，噪声潜变量 $z_t$ 关联 $K$ 个文本嵌入 $C = \{c_k\}_{k=1}^K$。潜空间感知EBM通过平均去噪分数实现能量聚合：

$$ \epsilon_{pred} = \frac{1}{K} \sum_{k=1}^K \epsilon_\theta(z_t, c_k, t) $$

该公式将 $K$ 个概念的能量分布平均，使模型学习多概念组成的整体运动分布。语义感知EBM则通过分解交叉注意力（Decompositional Cross-Attention, DCA）实现：

$$ \text{DCA}(z_t, C) = \frac{1}{K} \sum_{k=1}^K \text{CA}(z_t, c_k) $$

DCA将交叉注意力分为 $K$ 个并行分支，每个分支处理一个概念，输出聚合后作为去噪条件。此机制强制概念级分解，使模型能独立提取特定运动概念。

### 组合监督策略

设计动机：解决无分解真值时概念解耦不稳定的问题。DEMOGEN-EXP使用显式分解文本，每个概念对应独立文本描述。DEMOGEN-OSS采用正交自监督，将文本嵌入沿维度轴分割为 $K$ 个子嵌入，并施加正交损失：

$$ L_{Ortho} = \mathbb{E}_{l \sim L_c} \left\| \frac{\hat{Z}_l \hat{Z}_l^\top}{K^2} - I_K \right\|_F $$

其中 $\hat{Z}$ 为分割后的文本令牌，$I_K$ 为单位矩阵。该损失鼓励概念间正交，实现无监督解耦。DEMOGEN-SC结合语义一致性监督，对齐分割嵌入与分解文本嵌入，平衡解耦与语义一致性。

## 实验评估

实验在HumanML3D与MTT数据集上进行，基线覆盖MDM、MLD、EnergyMoGen、SALAD等扩散模型，但缺失T2M-GPT等自回归方法及Flow Matching类基线。HumanML3D测试集上，DEMOGEN-OSS在R@1指标达到0.588，优于SALAD的0.581；FID为2.625，优于SALAD的2.649。MTT组合生成任务上，DEMOGEN-EXP R@1为16.2，优于EnergyMoGen+SEF的15.9。

| 方法 | R@1 ↑ | FID ↓ | MM-Dist ↓ |
| :--- | :--- | :--- | :--- |
| SALAD | 0.581±.003 | 2.649±.009 | 9.696±.096 |
| DEMOGEN-OSS (latent) | 0.588±.004 | 2.625±.007 | 9.779±.120 |
| DEMOGEN-EXP (latent) | 0.569±.004 | 2.708±.012 | 9.774±.099 |

消融实验显示，DEMOGEN-OSS在多样性指标上优于DEMOGEN-EXP，表明正交自监督有助于生成更多样化的运动。DEMOGEN-SC在语义一致性上优于DEMOGEN-OSS，但FID略高，反映了解耦与保真度的权衡。

评估边界：指标完备性覆盖R-Precision、FID、MM-Dist等标准指标，但缺乏物理合理性指标（如Foot Skate）。评估协议基于预训练评估模型，可能存在偏差。可复现性方面，论文提供项目页面，但未公开完整代码与超参数细节，GPU需求未明确说明。

## 关联研究分析

从问题动机看，本文与EnergyMoGen同属能量基模型路线，但EnergyMoGen聚焦推理时的能量聚合实现组合生成，而DEMOGEN聚焦训练时的概念解耦。EnergyMoGen通过能量聚合实现多概念组合，但未解决概念间信息泄露问题；DEMOGEN通过正交损失与语义一致性监督强制解耦，但依赖分解式文本标注。这一差异源于任务特性：EnergyMoGen假设概念已知，DEMOGEN假设概念需发现。

从方法设计看，本文与SALAD同属潜扩散架构，但SALAD采用单一文本条件，DEMOGEN采用多概念条件。SALAD在纯T2M任务上FID为2.649，DEMOGEN-OSS为2.625，提升幅度有限。这表明分解式训练对组合能力的增益大于对纯T2M任务的增益。SALAD未探索概念解耦，DEMOGEN未探索长序列生成，两者在应用边界上存在互补性。

## 总结

本文核心矛盾在于现有T2M方法缺乏运动概念解耦能力，无法通过重组原语生成新颖动作。DEMOGEN抓住能量基扩散模型的多概念聚合特性，通过正交自监督与语义一致性监督实现无真值解耦。实验证明其在组合生成任务上R@1达16.2，优于SOTA。边界在于：DEMOGEN-EXP依赖分解式文本标注，DEMOGEN-OSS在纯T2M任务上增益有限，且缺乏物理合理性验证。当分解式文本标注不可得时，正交自监督能否在长序列生成中保持概念解耦稳定性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ff82e10dfbb7)
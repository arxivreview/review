# CVPR2026最新论文 ｜Enabling Supervised Learning of Generative Signatures for Generalized AI-Generated Images Detection ｜生成签名代理监督学习

作者：Jianwei Fei、Yunshu Dai、Xiaoyu Zhou 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2b46863d8d46)

> AI生成图像检测的核心瓶颈在于合成图像缺乏无伪迹真值，导致传统监督学习无法直接提取可泛化的生成指纹。现有方法或依赖手工滤波，或依赖特定生成器的重建误差，均难以在未见模型上保持鲁棒性。本文提出动态架构图像重建器（DAIR），通过随机化架构模拟生成痕迹，以重建残差作为代理真值训练提取器，实现跨生成器的通用检测。该范式在多个基准上刷新了泛化性能，但其对局部伪造的依赖及与最新视觉基础模型基线的对比缺失，限制了其结论的普适性。

## 研究背景

AI生成图像检测面临的首要困境是“无伪迹真值”问题。合成图像 $x$ 中嵌入的生成痕迹（Generative Traces）是区分真伪的关键线索，但这些痕迹没有对应的“干净”版本作为监督信号。早期研究如CNNSpot（Wang et al., 2020）通过挖掘空间域低层伪迹，在特定GAN架构上取得了高准确率，但这类方法严重依赖生成器的固定统计缺陷，当面对扩散模型或未见过的GAN变体时，性能骤降。这种跨生成器泛化（Cross-Generator Generalization）的失效，源于检测器过拟合于训练集中特定生成器的指纹，而非捕捉合成与真实图像的本质分布差异。

主流解决方案分为两类：一是基于重建误差的方法，如DIRE（Wang et al., 2023），利用扩散模型的反向过程误差检测，但该方法要求访问特定生成模型，缺乏通用性；二是基于视觉基础模型（VFM）的方法，如UnivFD（Wang et al., 2023），证明冻结的CLIP特征配合线性探针即可实现跨模型检测，确立了“通用表示”范式。然而，VFM方法可能忽略细粒度的低层统计线索，且在局部伪造场景下表现不稳定。本文的切入点在于解决“如何在不依赖特定生成器、且缺乏无伪迹真值的情况下，通过监督学习提取可泛化的生成签名”。

## 核心方法

### 动态架构图像重建器（DAIR）

本文方法置于“基于重建误差的检测”这一通用类别下，但关键差异在于：传统方法依赖固定架构或特定生成器的重建过程，而本文通过随机化架构模拟多种生成器，生成代理真值。DAIR由编码器 $\mathcal{E}_{rec}$ 和动态解码器 $\mathcal{D}$ 组成。解码器在每次前向传播中随机选择起始特征图层级，并随机组合上采样操作（双线性、最近邻等）、归一化层（BatchNorm、InstanceNorm等）和激活函数。这种随机性使得DAIR能够模拟大量不同的“虚拟生成器”，从而在真实图像上注入多样化的生成痕迹。

### 生成签名提取器（GenSign Extractor）

DAIR训练完成后，其重建残差 $R_{gt} = I - \mathcal{R}(I)$ 作为代理真值，用于训练生成签名提取器 $\mathcal{E}_{sig}$。$\mathcal{E}_{sig}$ 是一个全卷积网络，旨在从图像中分离出生成签名。其训练目标是最小化预测签名与代理真值之间的均方误差：

$$
\mathcal{L}_{sig} = \mathbb{E}_{I \in \mathcal{I}_{real}} \left[ \| \mathcal{E}_{sig}(\mathcal{R}(I)) - (I - \mathcal{R}(I)) \|^2 \right]
$$

这一设计的动机在于：通过预测重建残差，$\mathcal{E}_{sig}$ 被迫学习那些由生成过程引入的、与内容无关的统计异常，而非图像语义。由于DAIR的架构多样性，$\mathcal{E}_{sig}$ 学到的签名具有跨生成器的泛化能力。

### 双流检测器与自增强策略

最终检测器 $\mathcal{M}$ 融合RGB特征与提取的GenSign特征。RGB流使用CLIP ViT-L/14骨干（仅微调注意力层），GenSign流使用EfficientNet-B0。关键创新在于自增强（Self-Augmentation）策略：在训练检测器时，以概率 $p_{aug}$ 将输入图像通过冻结的DAIR重建，并将所有重建图像标记为“伪造”。这一策略迫使检测器依赖GenSign中的生成痕迹，而非内容偏差，从而提升了对局部伪造和分布外数据的鲁棒性。

## 实验评估

实验在UniversalFakeDetect、AIGCDetectBenchmark、AIGIBenchmark和GenImage四个基准上进行，训练集为ProGAN或SDv1.4。基线覆盖了CNNSpot、UnivFD、NPR、FatFormer等经典方法，但缺失了最新的VFM基线（如DINOv3-Linear）和鲁棒性专用方法（如HEDGE）。

| 基准 | 本文 (AP/Acc) | 最佳基线 (AP/Acc) | 差距 |
| :--- | :--- | :--- | :--- |
| UniversalFakeDetect | 99.37% AP | FatFormer (98.16% AP) | +1.21% |
| AIGCDetectBenchmark | 98.04% AP | PatchCraft (96.07% AP) | +1.97% |
| AIGIBenchmark | 89.96% AP | AIDE (75.36% AP) | +14.60% |
| GenImage | 96.6% Acc | Effort (91.1% Acc) | +5.5% |

在AIGIBenchmark上，本文在局部伪造模型（如BlendFace, InSwap）上显著优于基线，表明GenSign对局部篡改的敏感性。消融实验显示，自增强率 $p_{aug}=20\%$ 时性能最佳（95.79% AP），而0%时降至88.80%，证实了自增强对抑制内容偏差的关键作用。DAIR的架构多样性（3级下采样）比1级下采样提升了19.2%的AP，验证了模拟多样性对泛化的贡献。

评估边界方面，本文未报告置信区间，且AP与Acc指标混用，导致与知识库中SOTA（如SSAFE在AIGIBench上的95.9% Acc）的直接对比存在偏差。代码已开源，但训练DAIR和$\mathcal{E}_{sig}$分别需49小时和41小时（A100），部署成本较高。

## 关联研究分析

从问题动机看，本文与UnivFD（Wang et al., 2023）形成对比。UnivFD依赖冻结CLIP特征的语义分布差异，而本文依赖动态重建残差的低层统计差异。UnivFD在GenImage上达到96.4% Acc，与本文的96.6% Acc接近，但本文在AIGIBenchmark的局部伪造上表现更优。这一差异暗示，VFM特征可能忽略了局部篡改引入的细粒度伪迹，而GenSign通过重建残差捕捉了这些线索。然而，本文未与DINOv3等最新自监督VFM对比，无法确定GenSign的优势是否源于CLIP骨干的特定特性，还是重建范式本身的优越性。

从方法设计看，本文与DIRE（Wang et al., 2023）同属重建误差范式，但DIRE依赖特定扩散模型的反向过程，而DAIR通过随机架构实现了模型无关的重建。DIRE在GenImage上达到91.2% Acc，低于本文的96.6% Acc，表明动态架构模拟比固定模型重建更具泛化性。但DAIR的随机性可能导致重建残差包含大量噪声，本文通过$\mathcal{E}_{sig}$的监督学习过滤了这些噪声，这一过程是否在所有生成器上都有效，论文未给出理论保证。

## 总结

本文解决了AI生成图像检测中“无伪迹真值”导致的监督学习困境，通过动态架构图像重建器（DAIR）模拟生成痕迹，以重建残差作为代理真值训练生成签名提取器，实现了跨生成器的通用检测。在UniversalFakeDetect上达到99.37% AP，在AIGIBenchmark上以89.96% AP显著优于AIDE（75.36% AP），证明了代理监督范式的有效性。然而，本文的边界在于：自增强策略可能过拟合于DAIR自身的伪迹分布，且在最新VFM基线（如DINOv3）的对比缺失下，GenSign相对于通用语义特征的优势尚不明确。当DAIR的架构多样性进一步增加时，重建残差的信噪比是否会下降，从而限制$\mathcal{E}_{sig}$的提取精度，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_2b46863d8d46)
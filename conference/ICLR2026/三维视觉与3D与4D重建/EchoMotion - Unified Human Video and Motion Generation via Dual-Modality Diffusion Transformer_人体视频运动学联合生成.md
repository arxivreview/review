# ICLR2026最新论文 ｜EchoMotion: Unified Human Video and Motion Generation via Dual-Modality Diffusion Transformer ｜人体视频运动学联合生成

研究机构：清华大学、阿里巴巴集团

作者：Yuxiao Yang、Hualian Sheng、Sijia Cai 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.18814)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.18814)

> 现有视频生成模型在合成复杂人体动作时，常因像素级损失主导而忽略运动学原理，导致解剖结构伪影。本文切入点在于将人体运动参数与视频作为耦合模态进行联合去噪，而非仅作为条件输入。通过双分支扩散Transformer与同步位置编码，模型显式建模外观与运动学的联合分布。该方法在人体解剖合理性上显著优于基线，但其单人体限制与缺乏跨域泛化验证构成了当前边界。

## 研究背景

视频扩散模型（Diffusion Models）在视觉保真度上已接近饱和，但生成复杂人体动作时仍面临解剖结构崩坏与关节不自然的困境。这一现象源于像素级重建损失在训练过程中被静态外观与背景细节主导，导致模型优先拟合视觉纹理而非底层运动学原理。人体具有高自由度，细微的运动学误差在像素空间中会被放大为明显的解剖伪影，而传统的文本提示无法精确描述关节角度与轨迹细节，使得细粒度运动控制成为瓶颈。

主流解决路线分为两类：一是基于2D关键点或3D姿态投影的条件生成，如Follow-Your-Pose与MagicAnimate，它们通过ControlNet外挂姿态信号，但2D投影过程丢弃了深度信息，且依赖外部控制信号；二是基于光流的运动先验，如VideoJAM，通过预测光流增强时序一致性，但光流属于低层密集信号，难以捕捉高层结构化运动。现有方法多为严格条件生成器，缺乏对运动与外观联合分布的原生建模，导致在复杂动作下运动与外观解耦失效。EchoMotion的切入点在于将SMPL参数作为与视频同等地位的模态，在DiT内部进行联合去噪，从源头解决运动学缺失问题。

## 核心方法

### 双模态扩散Transformer架构

本文基于Wan2.1/2.2 DiT骨干，将传统单模态视频去噪扩展为视频与运动参数的联合去噪。与MMDiT仅处理视觉与文本Token不同，EchoMotion引入SMPL参数（形状$\beta$、姿态$\theta$、全局朝向$\gamma$、根位置$v$、关节位置$\eta$）作为运动模态。通过MLP投影器将运动参数映射为51个运动Token，与视频Token沿序列维度拼接，形成统一多模态上下文。这种设计避免了将3D姿态投影至2D平面造成的几何信息丢失，使模型能直接学习原生3D运动学模式。

### MVS-RoPE同步位置编码

为解决视频与运动Token在时空维度上的对齐问题，本文提出Motion-Video Synchronized RoPE（MVS-RoPE）。视频Token采用标准3D RoPE，运动Token在空间索引上施加对角偏移以区分模态，在时间索引上采用$t/4$缩放以匹配视频VAE的4倍时间压缩率。该机制通过位置编码强制建立模态间的时间同步性，防止空间位置冲突。

$$
\text{MVS-RoPE}(x_{motion}) = R(\frac{t}{4}, h_{offset}, w_{offset}) \cdot x_{motion}
$$

其中$R$为旋转编码函数，$t$为时间索引，$h_{offset}, w_{offset}$为空间偏移量。该公式确保运动Token在注意力计算中准确对应到视频帧的时间位置，解决了传统M-RoPE无法处理多模态时间对齐的问题。

### 两阶段训练策略

由于视觉与运动Token特征分布差异大，直接联合训练易导致运动分支被视频分支主导。本文采用两阶段策略：第一阶段冻结视频分支，仅用HumanML3D与HuMoVe数据预训练运动分支，使其收敛于运动学域；第二阶段解冻全部分支，在配对数据上进行多任务训练，涵盖联合生成、运动到视频、视频到运动三种范式。该策略通过任务嵌入引导条件预测，使模型在推理时能灵活切换生成模式。

## 实验评估

实验基于Wan2.1-1.3B与Wan2.2-5B骨干，使用自建HuMoVe数据集（约80,000条视频-运动对）与HumanML3D进行训练。基线包括CogVideoX-2B/1.5-5B、Wan-1.3B/5B及Video Tuning版本。评估指标涵盖自动指标（Human Anatomy, Motion Smoothness, Dynamic Degree, Aesthetic Quality）与人工评估（Video Quality, Prompt Following, Posture Plausibility）。

| 模型 | Human Anatomy | Motion Smoothness | Dynamic Degree | Aesthetic Quality |
|---|---|---|---|---|
| Wan-1.3B | 78.1 | 49.4 | 68.2 | 53.6 |
| EchoMotion (Wan-1.3B) | 79.6 | 98.2 | 71.3 | 65.5 |
| Wan-5B | 83.0 | 54.4 | 72.8 | 59.4 |
| EchoMotion (Wan-5B) | 85.1 | 98.9 | 81.0 | 70.2 |

在Wan-5B骨干上，EchoMotion的Human Anatomy指标从83.0提升至85.1，Motion Smoothness从54.4跃升至98.9，表明显式运动建模对时序连贯性的显著改善。然而，Dynamic Degree仅从72.8提升至81.0，提升幅度相对较小，暗示模型在保持高动态动作时可能牺牲部分视觉多样性。人工评估中，Posture Plausibility从59.4提升至81.6，验证了解剖合理性的改善。

消融实验未单独报告，但两阶段训练策略的必要性通过主实验结果间接体现：若直接联合训练，运动分支可能因视频分支的计算主导而收敛不良。评估边界方面，实验仅在人体视频子域进行，缺乏与相机控制或物体运动控制方法的跨域对比。代码未公开，超参数细节有限，可复现性依赖开源Wan骨干与SMPL工具链。

## 关联研究分析

从问题动机看，EchoMotion与VideoJAM均旨在解决时序一致性，但VideoJAM依赖光流这一低层信号，而EchoMotion采用SMPL参数这一高层结构化信号。光流捕捉像素级位移，适合短程运动，但难以表达关节角度等语义信息；SMPL参数直接编码运动学，更适合复杂人体动作。这一差异源于任务特性：人体动作具有强结构化特征，低层信号无法充分表达其运动学约束。

从方法设计看，EchoMotion与Follow-Your-Pose均使用姿态引导，但前者将姿态作为联合去噪模态，后者作为条件输入。条件生成方法依赖外部控制信号，在信号缺失或噪声大时性能下降；联合生成方法通过建模联合分布，能在无控制信号时生成合理运动，且在信号存在时实现双向控制。这一设计选择解决了条件生成方法对控制信号依赖过强的问题，但增加了模型复杂度与训练成本。

## 总结

EchoMotion针对视频生成中人体解剖伪影问题，通过双分支DiT联合建模视频与SMPL运动参数，解决了像素级损失忽略运动学原理的瓶颈。其核心贡献在于MVS-RoPE同步位置编码与两阶段训练策略，使模型在Wan-5B骨干上Human Anatomy指标达到85.1，Motion Smoothness达98.9。然而，该框架目前限于单人体生成，且实验仅在人体视频子域验证，缺乏跨域泛化能力评估。当支持集扩展至多人场景时，SMPL参数的拼接策略是否仍能保持运动学一致性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.18814)
# CVPR2026最新论文 ｜SMRABooth: Subject and Motion Representation Alignment for Customized Video Generation ｜定制化视频生成中的主体-运动解耦

研究机构：南京大学

作者：Xuancheng Xu、Yaning Li、Sisi You 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.12193)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.12193)

> 定制化视频生成旨在从参考图像提取主体外观、从参考视频提取运动模式，并联合生成新视频。现有基于U-Net的方法依赖空间/时间层分离，但DiT架构缺乏此区分，导致主体与运动LoRA直接组合时产生特征纠缠与伪影。SMRABooth通过引入外部编码器（DINOv2/光流）进行特征对齐，并结合稀疏LoRA注入策略，在DiT骨干上实现了主体与运动的解耦定制。该方法在CLIP-I和Motion Fidelity上取得SOTA，但其解耦策略对DiT层结构的依赖性尚未在更多骨干上验证。

## 研究背景

定制化视频生成的核心困境在于主体外观与运动模式的联合控制。传统方法采用两阶段训练，分别微调主体LoRA和运动LoRA，再在推理时合并。这一范式在U-Net架构中有效，因为U-Net明确区分空间层（处理外观）和时间层（处理运动），LoRA可分别注入对应层。然而，DiT架构（如WAN2.1）采用全自注意力机制，空间与时间依赖在同一层内耦合，导致主体与运动LoRA直接合并时相互干扰，生成视频出现主体漂移、运动趋势错误及背景过度复制。

该问题的紧迫性源于DiT已成为高性能T2V模型的主流骨干，但现有定制化方法未能适配其架构特性。DualReal等DiT基线方法虽采用LoRA组合，但未解决层耦合导致的特征纠缠，在复杂运动（如篮球运球）和精细主体（如陶俑手部）上表现不佳。SMRABooth的切入点在于：不依赖DiT内部层分离，而是通过外部编码器提供全局结构约束，并设计稀疏注入策略，使主体与运动LoRA在特定层和时间步上独立生效，从而在DiT架构上实现解耦定制。

## 核心方法

### 方法参照系

定制化视频生成的标准流程是两阶段LoRA微调：第一阶段用参考图像训练主体LoRA，第二阶段用参考视频训练运动LoRA，推理时合并两者。本文问题与该流程的关键差异在于：DiT骨干缺乏空间/时间层分离，直接合并LoRA导致特征纠缠，需引入外部约束和解耦策略。

### 主体表示对齐（SuRA）

SuRA模块解决主体外观泛化问题，其设计动机是扩散模型局部细节不足，需全局结构约束。在主体LoRA训练阶段，引入冻结的DINOv2-ViT-g编码器提取参考图像的全局语义特征 $y^* = E(I_{sub})$，其中 $E$ 为编码器，$I_{sub}$ 为输入图像。通过MLP $h_\phi$ 对齐DiT中间层特征 $z_t^{[1]}$ 与 $y^*$，计算余弦相似度损失：

$$ \mathcal{L}_{SuRA} = 1 - \frac{h_\phi(z_t^{[1]}) \cdot y^*}{\|h_\phi(z_t^{[1]})\| \|y^*\|} $$

该损失引导主体LoRA学习全局空间结构，而非仅拟合像素细节，从而提升主体保真度。

### 运动表示对齐（MoRA）

MoRA模块解决运动趋势错误问题，其设计动机是扩散模型难以显式建模物体级轨迹。在运动LoRA训练阶段，引入SEA-RAFT光流编码器提取参考视频的像素级运动场 $\mathbf{F}_{1,N}$，该场过滤外观冗余，仅保留轨迹变化。通过3D VAE解码器将去噪特征还原至像素空间，计算生成视频与参考视频的光流L1损失：

$$ \mathcal{L}_{MoRA} = \|\mathbf{F}_{gen} - \mathbf{F}_{ref}\|_1 $$

该损失强制运动LoRA学习连贯的物体级运动轨迹，实现运动与外观的解耦。

### 主体-运动关联解耦

解耦策略解决DiT层耦合导致的LoRA干扰问题，其设计动机是全层LoRA注入破坏主体-运动平衡。基于LoRA稀疏性实验，发现不同线性层对主体/运动影响不同：主体LoRA主要影响Q、K、FFN.0层，运动LoRA主要影响V、O、FFN.0、FFN.2层。推理时，在去噪前 $T_{point}=15$ 步仅应用运动LoRA，后 $T-T_{point}$ 步应用主体LoRA且权重加倍，实现时间步上的解耦。

## 实验评估

实验在WAN2.1 1.3B DiT骨干上进行，使用30个主体对象和21种运动类型，生成560个组合视频。基线覆盖WAN2.1、WAN2.1+LoRAs、DualReal（DiT）及DreamVideo、MotionBooth、MotionDirector（U-Net），但缺失Kaleido、Aura等最新主体一致性SOTA。

| 方法 | CLIP-T | CLIP-I | DINO-I | Motion Fidelity | PickScore |
| --- | --- | --- | --- | --- | --- |
| WAN2.1 | 0.339 | 0.586 | 0.165 | 35.18 | 19.96 |
| +LoRAs | 0.314 | 0.681 | 0.464 | 60.08 | 19.85 |
| DualReal | 0.351 | 0.692 | 0.509 | 45.75 | 20.58 |
| SMRABooth | 0.363 | 0.700 | 0.519 | 62.89 | 21.14 |

SMRABooth在CLIP-I（0.700）和Motion Fidelity（62.89）上显著优于DualReal（0.692/45.75），验证了外部编码器对齐与解耦策略的有效性。

消融实验显示，移除SuRA导致CLIP-I下降至0.667，移除MoRA导致Motion Fidelity下降至60.02。全层LoRA注入（Combination 1）导致视频质量严重退化，而稀疏注入（Q,K,FFN.0 for subject; V,O,FFN.0,FFN.2 for motion）达到最优。$T_{point}$ 过小导致视频静态，过大导致主体一致性下降，$T_{point}=15$ 为平衡点。

评估使用CLIP-T/I、DINO-I、Motion Fidelity等9项指标，但缺乏长视频叙事连贯性指标。实验在2块NVIDIA H20 GPU上进行，使用50步DDIM采样，生成49帧15fps视频。代码未公开，但超参数（学习率$1.0 \times 10^{-4}$，LoRA rank 32/64）已报告。

## 关联研究分析

从问题动机看，SMRABooth与DualReal同属DiT定制化生成，但DualReal依赖LoRA组合的隐式解耦，而SMRABooth引入外部编码器显式约束。这一差异源于任务特性：DualReal假设LoRA组合可自然分离主体/运动，但DiT层耦合使该假设失效；SMRABooth通过DINOv2/光流提供全局结构信号，弥补了DiT内部表示的不足。查询侧增强在数据充足时是否仍有增益，论文未给出回答。

从方法设计看，SMRABooth与MotionBooth同属两阶段范式，但MotionBooth依赖U-Net空间/时间层分离，而SMRABooth设计稀疏注入策略适配DiT。这一差异源于架构特性：U-Net层分离天然支持LoRA解耦，而DiT需通过层选择和时间步权重调整实现解耦。稀疏注入策略是否可推广至其他DiT骨干（如Sora、Wan2.2），论文未探索。

## 总结

SMRABooth解决的核心矛盾是DiT架构下主体与运动LoRA的层耦合干扰。其切入点在于：不依赖DiT内部层分离，而是通过外部编码器（DINOv2/光流）提供全局结构约束，并设计稀疏LoRA注入策略，使主体与运动在特定层和时间步上独立生效。该方法在CLIP-I（0.700）和Motion Fidelity（62.89）上取得SOTA，验证了解耦策略的有效性。其边界在于：解耦策略基于WAN2.1的层结构实验，未在其他DiT骨干上验证；评估缺乏长视频叙事指标，仅关注短片段（49帧）的主体-运动一致性。当DiT骨干的层结构发生变化时，稀疏注入策略的层选择是否仍需重新实验，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.12193)
# ICLR2026最新论文 ｜SMIXER: RETHINKING EFFICIENT-TRAINING AND EVENT-DRIVEN SNNS ｜脉冲Token混合器与动态时空剪枝

研究机构：北京大学、中国科学院

作者：Yijie Lu、Xinhao Luo、Yixing Zhang 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_77044096)

> 脉冲神经网络（SNN）在异步硬件上的部署受限于脉冲自注意力（SSA）的矩阵乘法精度偏差，且GPU训练阶段存在大量零值计算冗余。现有Spiking Transformer虽精度领先，但无法真正事件驱动，且训练开销巨大。本文采用Spiking-token Mixer（SMixer）替代SSA以消除脉冲矩阵乘法，并设计无参数的动态时空剪枝（DSTSP）框架，通过剔除低信息量脉冲特征降低训练成本。该方案在保持全事件驱动特性的同时实现了训练加速，但在ImageNet-1K等基准上的精度仍低于当前SOTA，其在全异步硬件上的实际能效增益尚待验证。

## 研究背景

脉冲神经网络（SNN）利用异步二进制脉冲传输信息，神经元膜电位仅在脉冲到达时更新，这一事件驱动特性使其天然适配TrueNorth等神经形态硬件。然而，主流Spiking Transformer依赖脉冲自注意力（SSA），其核心是脉冲Query与Key矩阵的乘法。在异步硬件中，脉冲到达时间缺乏同步时钟的精确性，导致矩阵乘法产生显著计算偏差，性能大幅退化。此外，SNN在GPU上训练时无法真正事件驱动，零值激活仍消耗算力，且固有的时间步与隐藏状态进一步增加了训练开销。

领域主流路线聚焦于提升Spiking Transformer的精度，如Spikformer和CSDformer通过优化架构或转换策略在静态图像分类上取得SOTA。但这些方法普遍保留SSA机制，未能解决异步硬件兼容性问题，且未针对训练阶段的计算冗余进行优化。本文切入点在于重新定义SNN架构设计原则：必须同时满足全事件驱动、低训练开销和竞争性性能。基于此，本文引入Spiking-token Mixer（SMixer）作为基础架构，用可学习权重矩阵替代脉冲矩阵乘法，并针对SNN特有的时空特征冗余，提出动态剪枝策略以加速训练。

## 核心方法

### 方法参照系

标准Spiking Transformer流程包含脉冲补丁分割、SSA模块和脉冲MLP。SSA通过计算脉冲Query、Key、Value的矩阵乘法生成注意力权重。本文的关键差异在于，用Spiking-token Mixer（SMixer）替代SSA，将脉冲Token与可学习的注意力权重矩阵直接混合，消除了脉冲-脉冲乘法，从而兼容异步硬件。

### Spiking-token Mixer架构

SMixer旨在解决SSA在异步硬件上的精度偏差问题。在标准流程中，SSA需要精确同步的脉冲矩阵乘法，而SMixer将Query和Key收敛为一个可学习的权重矩阵 $W_M$，通过异步计算混合脉冲输入。其核心运算表示为：

$$ \mathbf{Y} = \text{SN}(\mathbf{X} W_M + b) $$

其中 $\mathbf{X}$ 为脉冲形式输入，$\text{SN}$ 为脉冲神经元。这一设计将注意力权重的学习过程与脉冲传播解耦，使得模型在训练和推理中均无需依赖脉冲到达时间的精确同步，从根本上消除了异步硬件下的计算偏差。

### 动态时空剪枝框架

SMixer虽解决了硬件兼容性问题，但SNN固有的低发射率导致大量时空特征冗余，增加了训练开销。本文提出动态时空剪枝（DSTSP），基于脉冲强度值（SIV）识别并剔除冗余特征。SIV定义为特定区域内脉冲事件数量的总和，高SIV代表高语义信息。空间剪枝（DSSP）对Token按SIV降序排列，保留前 $N'$ 个Token，其中 $N'$ 由空间剪枝率 $P_S$ 决定：

$$ N' = \lfloor (1 - P_S) N \rfloor $$

时间剪枝（DSTP）则动态减少时间步数 $T'$ 和神经元最大发射脉冲数，直接降低神经元状态更新次数。该框架无需可学习参数，仅通过加法操作实现，符合SNN事件驱动特性，在保持精度的同时显著降低了训练阶段的计算资源消耗。

## 实验评估

实验覆盖ImageNet-1K、CIFAR-10/100、CIFAR10-DVS、DVS128-Gesture、COCO及时间序列预测任务。基线包括SpikformerV2、QKFormer、SDT-V3等主流Spiking Transformer，以及Spiking-Yolo等检测模型。缺失直接训练派SOTA方法（如SAGE）的对比，限制了训练效率优势的全面评估。

| 模型 | 架构 | 时间步 | 参数量(M) | 吞吐量(im/s) | 显存(MB) | 功耗(mJ) | Top-1 Acc(%) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| STMixer-8-768 | SMixer | 1 | 61.16 | 120 | 17008 | 4.45 | 76.68 |
| STMixer-8-768 + DSTSP | SMixer | 1 | 58.66 | 162 | 13002 | 2.36 | 76.87 |
| SpikformerV2-8-512 | Spikformer | 4 | 51.55 | 67 | 18786 | 9.36 | 80.38 |
| SpikformerV2-8-512 + DSTSP | SMixer | 4 | 47.93 | 98 | 10387 | 3.44 | 79.15 |

在ImageNet-1K上，SMixer+DSTSP的精度（76.87%）低于SpikformerV2（80.38%），但功耗降低至53.03%，吞吐量提升。在CIFAR-10上，SMixer+DSTSP精度为95.44%，低于CSDformer的96.35%（据领域综述）。

消融实验显示，空间剪枝率 $P_S=0.3$ 和时间步剪至1时，CIFAR-10精度仅下降0.5%。对比不同剪枝策略，低SIV剪枝（LP）在SNN中比随机剪枝（RP）更有效，且SIV在SNN中暴露冗余的能力强于ANN。位置消融表明，在训练和推理阶段均使用DSTSP（B）优于仅训练（T）或仅推理（I）。

评估边界方面，论文未报告置信区间，数值比较需谨慎。功耗数据基于理论计算，未提供真实神经形态硬件实测值。代码未公开，超参数设置与原始模型一致，但缺乏跨硬件平台的系统级能耗对比。

## 关联研究分析

从问题动机看，本文与TP-Spikformer同属Token剪枝路线，但TP-Spikformer针对Spikformer的SSA模块，而本文针对SMixer架构。TP-Spikformer依赖时空信息保留准则评估Token重要性，本文则基于SIV的脉冲强度统计。差异根源在于架构基础：SSA的注意力权重依赖脉冲交互，而SMixer的权重是静态可学习矩阵，使得SIV计算更简单且无需额外训练模块。

从方法设计看，本文与CSDformer代表不同路径。CSDformer通过量化感知训练（QAT）解决ANN-to-SNN转换误差，侧重精度保持；本文通过DSTSP解决训练开销，侧重效率优化。CSDformer在CIFAR-10上达到96.35%精度，本文SMixer+DSTSP为95.44%。这一差距暗示SMixer架构在表达力上可能弱于SSA，但本文未深入分析架构表达力与剪枝效率的权衡关系。

## 总结

本文核心矛盾在于SNN在异步硬件上的精度偏差与GPU训练的高开销。切入点在于用SMixer替代SSA消除脉冲矩阵乘法，并通过DSTSP剔除时空冗余。方法上，SMixer用可学习权重矩阵混合脉冲Token，DSTSP基于SIV动态剪枝。实验证明，在ImageNet-1K上，SMixer+DSTSP功耗降低至53.03%，但精度（76.87%）低于SpikformerV2（80.38%）。边界在于，精度差距可能源于SMixer架构本身的表达力限制，且功耗数据仅为理论值，未经验证。当SMixer在真实异步硬件上部署时，其理论能效优势能否转化为实际性能提升，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_77044096)
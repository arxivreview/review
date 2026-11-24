# CVPR2026最新论文 ｜Collaborative Multi-Mode Pruning for Vision-Language Models ｜协同多模态剪枝

研究机构：北京航空航天大学

作者：Zimeng Wu、Yunhong Wang、Donghao Wang 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.02956)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.02956)

> 视觉语言模型（VLMs）部署受限于Transformer架构的高计算复杂度，现有剪枝方法多聚焦于参数或Token的单一维度压缩，忽视了二者在重要性评估上的内在耦合与互扰。本文指出，简单联合剪枝因指标不一致和模式固定导致性能次优，提出协同多模态剪枝框架（CoMP），通过协同重要性度量（CIM）消除参数与Token重要性评估的相互干扰，并结合多模态剪枝策略（MPS）在渐进剪枝中动态选择最优模式。该框架在高剪枝率下显著优于单模态基线，但其依赖微调恢复性能，与当前主流的免训练（Training-free）范式存在部署成本差异，且未验证在极端压缩率下的鲁棒性。

## 研究背景

Transformer块的计算复杂度为 $O(N^2D + ND^2)$，其中 $N$ 为序列长度，$D$ 为特征维度。降低 $N$ 的Token剪枝与降低 $D$ 的参数剪枝分别针对数据冗余和结构冗余，二者在理论上互补。然而，参数重要性通常基于输入激活或梯度计算，而Token重要性依赖注意力分数或相似度，两者在计算过程中相互依赖：低重要性Token可能主导参数重要性估计，而被剪除的低重要性参数又会影响Token重要性的准确性。

现有VLM剪枝研究主要沿两条路线展开：参数剪枝（如UPop）通过渐进搜索子网络降低模型规模，Token剪枝（如MADTP、FastV）通过移除低贡献视觉Token加速推理。主流方法通常独立执行这两种剪枝，或采用固定的顺序/并行联合策略，未能解决指标互扰问题。当剪枝率超过0.7时，单模态剪枝易导致关键信息丢失，而简单联合剪枝因缺乏协同机制，性能仅与单模态相当。本文切入点在于揭示参数与Token重要性度量的内在不一致性，并提出协同框架以动态优化剪枝模式。

## 核心方法

### 方法参照系

标准VLM剪枝流程包含重要性评估、掩码生成与微调三个阶段。参数剪枝通过阈值 $\theta_p$ 生成二进制掩码 $\mathbf{M}^p \in \{0,1\}^D$，Token剪枝通过阈值 $\theta_t$ 生成掩码 $\mathbf{M}^t \in \{0,1\}^N$。本文的关键差异在于，传统方法独立计算 $\mathbf{S}^p$ 和 $\mathbf{S}^t$，而CoMP引入协同机制，使参数重要性计算受Token重要性加权，Token重要性计算受参数掩码修正，并在渐进剪枝中动态切换模式。

### 协同重要性度量（CIM）

CIM模块解决参数与Token重要性评估的互扰问题。传统参数重要性 $S^p$ 未考虑Token的重要性分布，导致低重要性Token主导评估。CIM通过引入Token加权输入范数修正参数重要性：

$$ S^p_{CIM} = \sum_{i=1}^{N} S^t_i \cdot \| \mathbf{X}_i \mathbf{W}_{in} \odot \mathbf{M}^p \|_1 $$

该公式表明，参数重要性由所有Token的重要性分数 $S^t_i$ 加权其对应输入范数决定，抑制了低重要性Token对参数评估的干扰。同时，CIM将参数剪枝掩码 $\mathbf{M}^p$ 传递至注意力权重矩阵，修正Token重要性：

$$ S^t_{CIM} = \text{Attention}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) \odot \mathbf{M}^p_{proj} $$

其中 $\mathbf{M}^p_{proj}$ 为参数掩码在注意力头维度的投影。这一设计消除了被剪除参数对Token重要性计算的虚假贡献，确保剪枝决策基于当前有效模型结构。

### 多模态剪枝策略（MPS）

MPS模块解决渐进剪枝中模式固定导致的次优问题。传统方法在每阶段固定执行参数或Token剪枝，但模型结构变化会导致最优模式漂移。MPS将剪枝过程分解为多个阶段，每阶段基于剪枝成本（Pruning Cost）动态选择最优模式。剪枝成本定义为当前模式下单位剪枝率带来的性能损失：

$$ C_m = \frac{\Delta L_{task}}{\Delta r_m} $$

其中 $m$ 表示剪枝模式（视觉参数、语言参数、视觉Token、语言Token、跨模态参数），$r_m$ 为模式 $m$ 的剪枝率。MPS引入随机探索（RE）和历史信息（HI）机制，避免陷入局部最优。具体地，模式选择概率 $P(m)$ 结合当前成本 $C_m$、历史成本均值 $\bar{C}_m$ 和探索率 $\rho$：

$$ P(m) \propto \exp\left(-\frac{C_m + \lambda \bar{C}_m}{\tau}\right) \cdot (1-\rho) + \frac{\rho}{|M|} $$

该机制平衡短期成本效率与长期探索稳定性，确保在高剪枝率下仍能发现全局最优剪枝路径。

## 实验评估

| 方法 | 剪枝模式 | 剪枝率 | NLVR2 Test Acc. (%) | GFLOPs |
|---|---|---|---|---|
| UPop | P | 0.8 | 67.80 | 30.78 |
| MADTP | T | 0.8 | 77.21 | 26.46 |
| SJP_U→M | J | 0.8 | 77.44 | 26.54 |
| CoMP | C | 0.8 | 79.62 | 25.97 |

实验在BLIP/CLIP/LLaVA-v1.5-7B上进行，覆盖NLVR2、COCO、Flickr30K、VQAv2等数据集。基线包括参数剪枝（UPop、M-Pruning）、Token剪枝（MADTP、STP、Turbo、FastV、VisionZip）及简单联合剪枝（SJP）。CoMP在NLVR2 0.8剪枝率下达到79.62%测试准确率，较MADTP提升2.41%，较简单联合剪枝SJP_U→M提升2.18%。在LLaVA-v1.5-7B上，CoMP在0.46剪枝率下平均得分69.23%，较PDrop†提升4.03%，较VisionZip†提升1.59%。

| 组件 | NLVR2 Test Acc. (%) | 提升幅度 |
|---|---|---|
| 基线（SJP） | 77.88 | - |
| +CIM | 78.60 | +0.72 |
| +MPS | 79.62 | +1.02 |

消融实验显示，CIM通过消除指标互扰带来0.72%提升，其中CIP（Token加权参数重要性）贡献0.39%，CIT（参数掩码修正Token重要性）贡献0.41%。MPS通过动态模式选择带来1.02%提升，其中随机探索（RE）贡献0.78%，历史信息（HI）贡献0.6%。可视化表明，早期阶段Token剪枝占主导，后期参数剪枝更显著，验证了冗余分布随剪枝进程变化的假设。

评估协议包含开发集与测试集准确率、检索召回率、CIDEr/SPICE分数及GFLOPs。局限在于：VQAv2实验仅使用CIM模块（因无验证集），LLaVA实验依赖微调（非Training-free），且未报告置信区间。代码已开源，实验在2块NVIDIA A800 GPU上完成，超参数 $\rho=0.2, \tau=5, \lambda_0=0.4, I_{max}=5$ 已公开。

## 关联研究分析

从问题动机看，CoMP与FastV、VisionZip等主流Token剪枝方法的核心差异在于处理冗余的维度。FastV依赖LLM浅层注意力分数进行Training-free剪枝，VisionZip结合显著性评分与上下文合并，二者均聚焦于数据级冗余（Token），未考虑结构级冗余（参数）与数据级冗余的耦合效应。CoMP指出，参数剪除会改变注意力分布，进而扭曲Token重要性评估，这一互扰在单模态剪枝中被忽略。根源在于，现有方法假设参数与Token重要性独立，而CoMP通过CIM显式建模二者依赖关系，解决了高剪枝率下指标失效的问题。

从方法设计看，CoMP与AutoPrune、OccamToken等自适应预算方法共享动态调整思想，但机制不同。AutoPrune将剪枝建模为约束优化问题，联合优化每层Token分配，OccamToken利用注册Token分数作为自适应阈值，二者均针对Token预算的动态调整。CoMP的MPS则聚焦于剪枝模式（参数vs Token）的动态切换，而非单一维度的预算调整。差异根源在于，CoMP处理的是多模态（参数+Token）的协同优化，而AutoPrune/OccamToken处理的是单模态（Token）的自适应分配。CoMP的随机探索机制旨在避免模式选择的局部最优，这一设计在AutoPrune的优化框架中未体现，是否更优需在高维参数空间中进一步验证。

## 总结

CoMP解决的核心矛盾是参数剪枝与Token剪枝在重要性评估上的内在不一致性，导致简单联合剪枝在高剪枝率下性能次优。现有方法因独立计算重要性指标和固定剪枝模式，无法消除二者互扰，而CoMP通过CIM协同度量和MPS动态模式选择，实现了参数与Token剪枝的有效协同。实验证明，在NLVR2 0.8剪枝率下，CoMP较MADTP提升2.41%，在LLaVA-v1.5-7B上较PDrop†提升4.03%。其边界在于依赖微调恢复性能，与Training-free范式存在部署成本差异，且未验证在极端压缩率（<10%）下的鲁棒性。当剪枝率超过0.85时，MPS的随机探索机制是否仍能稳定收敛至全局最优，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.02956)
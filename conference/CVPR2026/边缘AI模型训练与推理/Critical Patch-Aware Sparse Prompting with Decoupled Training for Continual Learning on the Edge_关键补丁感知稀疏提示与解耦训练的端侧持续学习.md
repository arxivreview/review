# CVPR2026最新论文 ｜Critical Patch-Aware Sparse Prompting with Decoupled Training for Continual Learning on the Edge ｜关键补丁感知稀疏提示与解耦训练的端侧持续学习

作者：Wonseon Lim、Jaesung Lee、Dae-Won Kim

论文原文见 [arXiv](https://arxiv.org/abs/2604.07399)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.07399)

> 端侧持续学习面临反向传播激活值存储超出设备内存的刚性约束，导致全量微调不可行。现有提示基持续学习（Prompt-based Continual Learning, PCL）方法虽通过冻结骨干降低参数规模，但忽略训练时的内存峰值与计算开销，致使高精度模型无法在资源受限硬件上稳定运行。本文提出CPS-Prompt，通过任务感知的关键补丁采样与提示-分类器解耦训练，在保持精度的同时显著削减训练内存与时间。该框架在Jetson Orin Nano上实现了1.6倍的效率提升，但其在高稀疏率下的泛化边界及动态资源适配能力仍存疑。

## 研究背景

当视觉Transformer（ViT）在边缘设备上进行持续学习时，反向传播所需的中间激活值存储量远超共享CPU-GPU内存容量，直接导致训练崩溃或性能衰减。这一内存墙限制迫使研究者转向参数高效微调（Parameter-Efficient Fine-Tuning, PEFT），其中PCL通过冻结预训练ViT骨干并仅更新轻量级提示参数，在缓解灾难性遗忘的同时大幅降低了可训练参数规模。然而，PCL通常采用两阶段前向传播：冻结查询编码器生成上下文表示，随后提示注入骨干进行分类。这种设计虽提升了精度，但每次前向传播均处理全量图像补丁，导致激活值内存占用居高不下，尤其在多任务序列训练中，峰值内存极易突破边缘设备阈值。

主流PCL方法如C-Prompt和CODA-Prompt优先优化精度，忽视了训练时的资源效率，使其难以部署于内存受限的边缘硬件。ToMe和PatchDropout等通用Token缩减技术虽能降低激活成本，但因缺乏任务感知性，随机丢弃或合并关键补丁，导致PCL精度显著下降。本文切入点在于解决PCL在端侧训练中的内存-精度权衡问题，通过引入任务感知的稀疏化机制与解耦训练策略，在不牺牲精度的前提下实现训练效率的突破。

## 核心方法

### 方法参照系

标准PCL流程包含冻结查询编码器 $f_q$ 与提示注入骨干 $f_p$ 的两阶段前向传播。输入图像 $x$ 经 $f_q$ 生成上下文表示 $z_q$，用于选择提示；随后 $x$ 与提示参数 $\phi$ 共同输入 $f_p$ 生成任务自适应特征。该流程的关键差异在于：标准PCL对全量补丁执行反向传播，而本文在提示训练阶段引入稀疏补丁输入，以削减激活值存储。

### 关键补丁采样

**设计动机**：通用Token缩减方法（如ToMe）因任务无关性丢弃关键补丁，导致PCL精度骤降。CPS利用冻结查询编码器的注意力与值范数信号，实现任务感知的补丁选择。

CPS从查询编码器最终层提取注意力矩阵 $\mathbf{A}^{[L]}$ 与值矩阵 $\mathbf{V}^{[L]}$，计算每个补丁的关键分数 $s_j = A^{[L]}_{\text{cls},j} \cdot \|\mathbf{V}^{[L]}_j\|_2$，其中 $A^{[L]}_{\text{cls},j}$ 为类Token对补丁 $j$ 的注意力权重，$\|\mathbf{V}^{[L]}_j\|_2$ 为值向量L2范数。该分数同时反映补丁对类表示的贡献度（注意力）与特征显著性（值范数）。随后，通过温度缩放Softmax将分数转化为采样分布 $p_j = \text{Softmax}(s_j/\tau)$，并按无放回多项式分布采样 $k = \lfloor(1-r) \cdot N\rfloor$ 个补丁，其中 $r$ 为补丁缩减率，$N$ 为总补丁数。采样后的稀疏序列 $\mathbf{X}_{\text{sampled}} = [\mathbf{x}_{\text{cls}}] \cup \{\mathbf{x}_j | j \in I_{\text{sampled}}\}$ 用于提示训练，显著降低激活值内存占用。

### 解耦提示与分类器训练

**设计动机**：CPS稀疏训练导致训练与推理时的表示失配，尤其在高采样率下，提示参数在稀疏输入下学习到的特征与全量输入下的分类器期望不一致。DPCT通过两阶段解耦训练缓解此问题。

DPCT将训练分为两阶段：第一阶段（$t=1$ 至 $\lfloor\lambda \cdot E\rfloor$）使用稀疏补丁 $\mathbf{X}_{\text{sampled}}$ 联合优化提示参数 $\phi$ 与分类器参数 $\theta$，损失函数为 $L_p(\hat{y}, y)$；第二阶段（$t=\lfloor\lambda \cdot E\rfloor+1$ 至 $E$）冻结提示参数 $\phi$，使用全量补丁 $\mathbf{X}_{\text{full}}$ 仅优化分类器参数 $\theta$，损失函数为 $L_{\text{cls}}(\hat{y}, y)$。该策略通过稀疏输入学习任务自适应特征，再通过全量输入对齐分类器，减少反向传播开销并缩短训练时间。

## 实验评估

实验在CIFAR-100、ImageNet-R和CUB-200三个类增量学习基准上进行，每个数据集划分为10个不重叠任务，报告平均精度（ACC_T）与遗忘率（F_GT_T）。基线覆盖L2P、DualPrompt、CODA-Prompt、C-Prompt、OS-Prompt等主流PCL方法，以及ToMe和PatchDropout等Token缩减技术。主实验结果显示，CPS-Prompt在CIFAR-100上达到66.89%精度，低于C-Prompt的68.34%（-1.45%），但高于CODA-Prompt的67.06%（+0.17%）；在ImageNet-R上，CPS-Prompt精度为49.96%，与CODA-Prompt的50.24%基本持平，而C-Prompt为53.32%。

| 方法 | CIFAR-100 ACC_T (%) | ImageNet-R ACC_T (%) | CUB-200 ACC_T (%) |
|---|---|---|---|
| CODA-Prompt | 67.06 | 50.24 | 52.64 |
| C-Prompt | 68.34 | 53.32 | 52.63 |
| CPS-Prompt | 66.89 | 49.96 | 52.85 |

CPS-Prompt在精度上略低于C-Prompt，但显著优于CODA-Prompt在CUB-200上的表现。效率方面，CPS-Prompt较CODA-Prompt减少约1.6倍峰值内存、1.5倍训练时间，并消耗1.6倍更少能量；较C-Prompt减少4.3倍内存、3.1倍训练时间，并消耗3.3倍更少能量。

消融实验在ImageNet-R上以0.5缩减率进行，验证CPS与DPCT的独立贡献。CPS较随机补丁选择（PD）提升1.84%精度（47.16% vs 45.32%），且内存占用相同（253 MB）；DPCT在CPS基础上再提升2.12%精度（49.28% vs 47.16%），并显著缩短训练时间。温度 $\tau$ 与阶段比例 $\lambda$ 的敏感性分析表明，$\tau=0.1$ 与 $\lambda \in [0.4, 0.6]$ 提供最佳精度-效率权衡，低温度聚焦高置信补丁，中等阶段比例平衡提示学习与分类器对齐。

评估边界方面，实验仅在Jetson Orin Nano上验证效率指标，未覆盖MCU等极端边缘设备；超参数（$\tau, \lambda$）基于验证集手动调整，缺乏自动化机制；代码已开源，但部分实现细节（如ToMe合并比例）仅在补充材料中提供，可复现性依赖完整文档。

## 关联研究分析

从问题动机看，CPS-Prompt与OS-Prompt均旨在降低PCL训练开销，但OS-Prompt通过合并两阶段为单阶段减少计算，而CPS-Prompt保留两阶段结构并引入稀疏化。OS-Prompt的峰值内存仍高，因其在单阶段中处理全量补丁；CPS-Prompt通过CPS削减激活值，实现更低内存占用。差异根源在于任务特性：PCL的两阶段结构对提示选择至关重要，OS-Prompt的简化可能损失任务相关性，而CPS-Prompt通过注意力信号保留关键补丁，维持精度。

从方法设计看，CPS-Prompt与ToMe在Token缩减机制上存在根本差异。ToMe基于Token相似度合并，任务无关；CPS基于注意力与值范数评分，任务感知。ToMe在高稀疏率下精度骤降，因合并可能丢弃关键补丁；CPS通过温度缩放Softmax引入随机性，增强泛化性。差异根源在于PCL对任务相关性的依赖：通用Token缩减忽略下游任务需求，而CPS利用查询编码器的任务信号，实现精准稀疏化。

## 总结

CPS-Prompt解决的核心矛盾是PCL在端侧训练中的内存-精度权衡，现有方法因忽视训练时资源效率或任务无关性导致精度下降。本文通过任务感知的CPS与解耦训练DPCT，在保持精度的同时实现1.6倍效率提升。实验证明其在Jetson Orin Nano上较CODA-Prompt减少1.6倍内存与1.5倍训练时间，精度损失控制在2%以内。边界在于：实验未覆盖MCU等极端边缘设备，且超参数需手动调整，缺乏动态资源适配能力。当任务序列长度增加或设备内存进一步受限时，CPS的稀疏率自适应机制是否仍能维持精度-效率平衡，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.07399)
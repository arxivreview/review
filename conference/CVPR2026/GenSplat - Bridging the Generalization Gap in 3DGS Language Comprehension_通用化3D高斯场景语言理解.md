# CVPR2026最新论文 ｜GenSplat: Bridging the Generalization Gap in 3DGS Language Comprehension ｜通用化3D高斯场景语言理解

研究机构：香港城市大学

作者：Fang Liu、Yuhao Liu、Ke Xu 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_7875c68d6b06)

> 3D高斯泼溅（3DGS）在几何重建上已趋成熟，但语言引导的场景理解仍受限于固定词汇表或逐场景过拟合。现有方法要么依赖预定义类别无法处理自由形式查询，要么通过场景特定优化牺牲了跨场景泛化能力。GenSplat通过渐进式语言接地课程与多模态大语言模型（MLLM）引导的推理模块，在3DGS表示上实现了开放词汇理解与空间推理的统一。该方法在ScanRefer上达到61.3%的Acc@0.25，但在动态场景与实时部署方面存在明显边界，其MLLM推理对空间关系准确性的真实贡献仍需更严格的消融验证。

## 研究背景

当3D视觉模型面对“窗户左边那张灰色桌面的圆桌”这类自由形式查询时，传统基于CLIP特征匹配的方法因缺乏组合推理能力而失效。这一困境源于2D视觉语言模型（VLM）特征缺乏显式3D几何结构，直接投影至3D空间易丢失空间关系信息。为弥补这一缺陷，3DGS因其显式几何结构和实时渲染能力，逐渐取代神经辐射场（NeRF）成为3D语言嵌入的首选表示。然而，3DGS场景中的高级语义推理能力仍滞后于其几何重建能力，语言接口在增强现实、具身智能等应用中的潜力尚未充分释放。

3DGS语言理解的主流路线存在根本性矛盾：以LangSplat为代表的方法通过2D特征蒸馏实现开放词汇分割，但依赖逐场景优化导致泛化能力受限；以SceneSplat为代表的方法通过大规模训练实现跨场景泛化，但受限于预定义词汇表无法处理自由形式查询。ReferSplat虽支持自由形式语言，但场景特定优化导致视觉-语言对齐薄弱。GenSplat的切入点在于识别出过拟合问题的根源——缺乏从低级几何到多级语言组合的层次化学习过程，从而提出结构化训练策略以解决这一矛盾。

## 核心方法

### 方法参照系

3DGS语言理解的标准流程通常包含场景重建、特征提取与语言匹配三个环节。本文问题与该通用流程的关键差异在于：标准流程假设语言查询与3D表示之间存在直接映射关系，而自由形式查询需要组合推理能力，这要求模型在几何原语与多级语言概念之间建立层次化对齐。

### 渐进式语言接地课程

该设计解决了此前方法直接融合自由形式文本与实例特征时缺乏组合推理能力的失效。在语义级对齐阶段，Gaussian Encoder将每个高斯原语$G_j$映射为语义特征$l_j = E_g(G_j)$，并通过可微渲染生成2D特征图$\{F_i\}$，使用L1损失与预训练SAM+CLIP特征$\{\hat{F}_i\}$对齐：

$$L_1 = \frac{1}{N}\sum_{i=1}^{N} \|F_i - \hat{F}_i\|_1$$

这一损失确保3D语义特征与2D视觉语言先验的一致性。在实例级对齐阶段，Instance Decoder通过交叉注意力将语义特征聚合为实例查询$O_{ins}$，使用二元交叉熵损失与Dice损失监督3D实例掩码预测。该课程结构防止模型过拟合到固定词汇表，建立可泛化的语言特征空间。

### MLLM引导推理与几何感知帧选择

该设计解决了纯特征匹配无法处理复杂空间关系推理的失效。Geometry-Aware Frame Selector (GAFS)通过融合2D视觉特征与3D高斯语义特征，计算查询向量$\hat{q}$与几何增强图像特征$\hat{v}_i$的余弦相似度$s_i$，选择最具信息量的视图。为避免视图冗余，采用加权距离$D_{ij} = \lambda_t\|t_i - t_j\|_2 + \lambda_r \cdot ang(R_i, R_j)$进行冗余抑制，其中$t$和$R$分别为相机中心与朝向。选中的关键帧与文本查询输入MLLM，预测携带语义与空间先验的<SEG> token $t_{seg}$，该token与实例查询$O_{ins}$拼接后输入Referring Decoder生成3D指代掩码。这一机制将MLLM的语义空间先验注入3D定位过程，实现精确的空间推理。

## 实验评估

| 方法 | 模态 | ScanRefer mIoU | ScanRefer A@0.25 | Multi3DRefer mIoU |
| --- | --- | --- | --- | --- |
| LISA-7B | I | 21.2 | 35.8 | - |
| 3D-STMN | PC | 39.5 | 54.6 | - |
| LiftGS | GS | - | 49.7 | - |
| 3D-LLaVA | PC | 43.3 | - | 42.7 |
| GenSplat | GS+I | 43.6 | 61.3 | 46.2 |

实验在ScanRefer、Multi3DRefer、ScanQA与SQA3D上进行，基线覆盖2D MLLM、专家模型与3D MLLM三类路线，但缺少SceneCOT、OpenGround等2025-2026年最新SOTA方法的对比。GenSplat在ScanRefer上达到61.3%的Acc@0.25，较LiftGS提升23.3%，较3D-LLaVA在Multi3DRefer上提升3.5%的mIoU，验证了3DGS表示与MLLM推理结合的有效性。

| 配置 | ScanRefer mIoU | ScanQA CIDEr | SQA3D EM |
| --- | --- | --- | --- |
| (I) Baseline | 26.6 | 71.7 | 45.4 |
| (III) + Sem. & Ins. Pretrain | 33.1 | 75.6 | 47.9 |
| (VII) GAFS w. only 2D Views | 41.4 | 96.9 | 55.3 |
| (VIII) GenSplat | 43.6 | 98.3 | 56.0 |

消融实验显示，从(III)到(VIII)的提升中，MLLM引导推理贡献了10.5%的mIoU增益，而GAFS相比均匀采样带来9.3%的增益。值得注意的是，(VII)仅使用2D视图的GAFS已接近完整模型性能，暗示3D几何特征在帧选择中的边际贡献可能小于预期。

评估指标涵盖mIoU、Acc@kIoU、CIDEr与EM，但未报告计算效率与推理延迟。代码已开源，使用8×NVIDIA H100 GPU训练，Gaussian Encoder在ScanNet上训练100 epochs，Instance Decoder在ScanNet200上训练512 epochs，MLLM使用LoRA微调。

## 关联研究分析

从方法设计看，GenSplat与LangSplat的核心差异在于训练策略：LangSplat采用单阶段特征蒸馏，而GenSplat引入渐进式课程学习。这一差异的根源在于任务特性——自由形式查询需要组合推理能力，单阶段训练无法建立层次化的语言-几何映射。然而，GenSplat的MLLM推理模块是否真正提升了空间关系准确性，还是仅增强了语言流畅度，论文未通过专门的空间关系子集实验给出明确回答。

从问题动机看，GenSplat与3D-LLaVA代表两种不同的3D MLLM路线：3D-LLaVA基于点云特征直接输入MLLM，而GenSplat通过3DGS表示与2D视图选择间接交互。这一差异源于对模态鸿沟的不同处理方式——3D-LLaVA假设MLLM能直接理解3D特征，而GenSplat认为2D视图是更有效的视觉接口。GAFS选择32帧的限制是否会影响长时序场景的推理能力，论文未进行相关实验验证。

## 总结

GenSplat要解决的核心矛盾是3DGS语言理解中固定词汇表与自由形式查询之间的泛化-推理权衡。现有方法要么牺牲泛化能力追求场景特定优化，要么牺牲推理能力追求跨场景泛化，GenSplat通过渐进式课程学习与MLLM引导推理同时解决这两个问题。该方法在ScanRefer上达到61.3%的Acc@0.25，在Multi3DRefer上达到46.2%的mIoU，验证了3DGS表示与MLLM推理结合的有效性。然而，消融实验显示3D几何特征在帧选择中的边际贡献有限，且论文未报告计算效率指标，GAFS选择32帧的限制可能影响动态场景的实时推理能力。当场景复杂度增加或查询涉及多步空间关系推理时，MLLM推理模块的性能增益是否持续，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_7875c68d6b06)
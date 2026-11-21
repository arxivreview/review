# CVPR2026最新论文 ｜PIX-TAB: Efficient PIXel-Precise TABle Structure Recognition Approach with Speculative Decoding and Region-Based Image Segmentation ｜像素级精确表格结构识别

作者：Viktor Zaytsev、Olena Vynokurova、Pavlo Tytarchuk 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2aa05a5bcb73)

> 表格结构识别（TSR）旨在从图像中恢复行列关系与单元格边界，是文档理解的关键环节。现有端到端模型虽精度高，但推理速度慢且难以部署于边缘设备，而传统检测器又缺乏对复杂布局的泛化能力。PIX-TAB 通过引入位置感知像素精确令牌（PAPP）与分析性推测解码，在保持 SOTA 精度的同时实现 3 倍以上的推理加速。该方法在效率与精度间取得了显著平衡，但其对无边框表格的鲁棒性及外部 OCR 依赖仍是主要局限。

## 研究背景

表格结构识别面临的核心困境在于视觉布局的多样性与计算资源的有限性之间的冲突。当模型面对包含合并单元格、嵌套表头或无边框的复杂表格时，传统的基于边界框检测的方法往往因几何线索缺失而失效。为了解决这一问题，研究者转向序列生成范式，将表格结构编码为 HTML 或 OTSL 标记序列。然而，标准的自回归解码器在生成长序列时存在累积延迟，且模型体积庞大，难以在移动端实时运行。

主流路线分为两类：一类是基于 Transformer 的端到端生成模型（如 TableFormer, UniTable），它们通过强大的语义理解能力实现了高精度的结构恢复，但推理速度通常在 1-5 FPS 之间，且模型参数量大，不适合边缘部署；另一类是轻量化检测模型，它们速度快但难以处理复杂的逻辑结构。PIX-TAB 的切入点在于利用表格结构的几何规律性，通过一种无需额外神经网络的“分析性推测解码”机制，结合紧凑的像素级令牌表示，在轻量级模型上实现高速且精确的结构重建。

## 核心方法

### 方法参照系

PIX-TAB 属于端到端序列生成路线，其基础架构借鉴了 MTL-TabNet 的编码器-解码器设计。与标准流程的关键差异在于，它摒弃了独立的边界框预测头用于推理，转而将空间坐标直接编码进生成序列，并引入了基于规则的推测解码机制以加速生成过程。

### 位置感知像素精确令牌（PAPP）

传统方法在推理时需要额外的解码器来预测每个单元格的边界框，这增加了计算开销且引入了误差累积。PIX-TAB 扩展了 OTSL 表示，引入了行起始令牌 `<rYYY>` 和列边界令牌 `<cXXX>`，其中 YYY 和 XXX 分别为归一化图像中的垂直和水平像素坐标。这种设计使得单元格边界可以直接从令牌序列中重构，无需单独的边界框解码器。

$$
\text{PAPP Sequence} = \langle r_{y_1} \rangle \langle c_{x_1} \rangle \dots \langle c_{x_n} \rangle \langle r_{y_2} \rangle \dots \text{OTSL Tokens} \dots \langle /table \rangle
$$

该公式表明，通过显式编码像素坐标，模型在生成结构标记的同时完成了空间定位，从而实现了确定性单元格重建，特别适用于长复杂表格。

### 分析性推测解码

标准自回归解码器逐令牌生成，对于具有重复行模式的表格效率低下。PIX-TAB 利用 PAPP-OTSL 序列在行间的规律性，设计了一种分析性算法来预测未来令牌块。算法首先找到与当前行前缀匹配的参考行，然后基于估计的行间距生成一个大小为 K 的推测块。

$$
S = A[|L|:] \parallel A^{\times K}
$$

其中 $A$ 为参考行，$L$ 为当前行，$S$ 为推测序列。解码器对拼接后的序列进行一次前向传播，验证推测令牌；若匹配则接受，否则回退。这一机制将解码步骤减少了数倍，显著降低了延迟，且无需额外的神经网络调用。

## 实验评估

实验在 FinTabNet 和 PubTabNet 上进行，对比了 TableFormer、RobusTabNet、UniTable 等主流方法。基线覆盖了基于 Transformer 的端到端模型和检测模型，但缺乏最新 VLM 基线（如 GPT-4o）及多页表格基准。

| 方法 | GPU | Norm.FPS | TEDSstruct |
| :--- | :--- | :--- | :--- |
| TableFormer | - | - | 96.80 |
| RobusTabNet | V100 | 5.19 | 97.00 |
| UniTable | - | - | 98.89 |
| TABLET | A100 80GB | 18.01 | 98.71 |
| PIX-TAB (✔RBIS) | A100 40GB | 7.23 | 98.65 |
| PIX-TAB (✗RBIS) | A100 40GB | 7.96 | 98.72 |

PIX-TAB 在 FinTabNet 上取得了 98.72 的 TEDSstruct，与 TABLET 持平，但推理速度（7.96 FPS）显著高于多数对比方法。在 PubTabNet 上，PIX-TAB 的 TEDSstruct 为 97.26，同样处于 SOTA 水平。

消融实验显示，推测解码（SD）在 FinTabNet 上将 FPS 从 3.80 提升至 7.96，而在 PubTabNet 上从 3.36 提升至 8.54，精度损失可忽略。区域基于图像分割（RBIS）模块在 SynthTabNet MarketingStyle 子集上使 TEDSstruct100 从 56.14% 提升至 57.59%，表明其对有边框表格的几何精度有显著增益，但对无边框表格效果有限。

评估指标引入了 TEDSstruct100 和 TEDS100，以衡量完全正确识别的表格比例，弥补了平均 TEDS 掩盖个体错误的缺陷。实验在 NVIDIA A100 40GB 上进行，移动端测试使用 Samsung Fold 5。论文未提供代码，但详细描述了超参数（如学习率 0.001，batch size 128）和训练协议，具备较高的可复现性。

## 关联研究分析

从方法设计看，PIX-TAB 与 TableFormer 等端到端模型的核心差异在于空间信息的处理方式。TableFormer 依赖注意力机制隐式学习空间关系，而 PIX-TAB 通过 PAPP 令牌显式编码像素坐标。这种显式编码使得推测解码成为可能，因为行间距的规律性可以直接从坐标中推导，而无需依赖语义相似性。这一设计选择源于对边缘部署效率的追求，牺牲了部分对非规则布局的泛化能力，换取了推理速度的大幅提升。

从问题动机看，PIX-TAB 与 MTL-TabNet 同属多任务学习框架，但 PIX-TAB 将边界框预测仅作为训练辅助，推理时移除。这与 MTL-TabNet 在推理时同时输出结构和边界框不同。这种“训练时监督，推理时移除”的策略减少了推理时的计算负担，但引入了对 PAPP 令牌精度的更高要求。若 PAPP 令牌预测出现微小偏差，可能导致单元格边界错位，而 MTL-TabNet 的独立边界框头可能提供更鲁棒的空间定位。

## 总结

PIX-TAB 旨在解决表格结构识别中精度与效率的矛盾，特别是针对边缘设备部署场景。通过引入 PAPP 令牌和分析性推测解码，它在保持 SOTA 精度（FinTabNet TEDSstruct 98.72）的同时，实现了 3 倍以上的推理加速。然而，该方法对无边框表格的鲁棒性不足，RBIS 模块仅在有边框表格上有效，且整体性能依赖外部 OCR 模型的准确性。当表格布局高度不规则或 OCR 误差较大时，PAPP 令牌的确定性重构是否会失效，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_2aa05a5bcb73)
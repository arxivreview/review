# HuggingFace最新推荐论文 ｜InstanceControl: Controllable Complex Image Generation without Instance Labeling ｜实例级文本-视觉条件关联的可控生成

研究机构：哈尔滨工业大学

作者：Xiaoyu Liu、Huan Wang、Fan Li 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.31924)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.31924)

> 多实例可控生成面临的核心矛盾是：文本提示中的实例描述与视觉条件中的空间区域缺乏精确绑定，导致属性混淆。现有方法依赖人工标注实例掩码或边界框，推理成本高且难以扩展。InstanceControl 利用视觉语言模型（VLM）自动解析文本并预测视觉条件中的实例掩码，建立实例级对应关系，再通过掩码精炼模块动态修正噪声，实现免标注的细粒度控制。该方法在 MIG-Eval 基准上显著优于 FLUX ControlNet 等基线，但其性能高度依赖 VLM 对非 RGB 视觉条件的泛化能力，且未验证在极端密集布局下的鲁棒性。

## 研究背景

可控图像生成旨在通过引入边缘、深度等视觉条件，弥补文本提示在空间精度上的不足。ControlNet 确立了通过辅助网络注入空间条件的范式，但在多实例场景中，由于缺乏实例级的语义-空间绑定，模型常发生颜色或身份特征跨实例泄漏。这一问题的根源在于，传统方法将视觉条件视为整体输入，未区分其中不同实例对应的文本描述，导致注意力机制在全局交互中无法隔离实例特征。

随着多模态大语言模型（MLLM）的发展，利用其跨模态推理能力自动建立文本与视觉区域的对应关系成为可能。然而，现有 VLM 分割模型（如 LISA）主要针对 RGB 图像设计，要求文本与视觉内容严格语义一致。在可控生成任务中，用户可能用“Spider-Man, Messi”描述边缘图，这种文本-视觉条件的语义歧义导致现有方法失效。InstanceControl 针对这一特定场景，构建专用数据集微调 VLM，使其能在非 RGB 视觉条件下准确解析实例描述并预测掩码，从而解决免标注条件下的多实例属性混淆问题。

## 核心方法

### 方法参照系

标准可控生成流程直接注入视觉条件，缺乏实例级解析。InstanceControl 的关键差异在于引入前置的“实例级文本-视觉条件关联”阶段，将全局条件分解为实例级对应关系 $C = \{(\mathbf{t}_i, \mathbf{m}_i)\}_{i=1}^N$，其中 $\mathbf{t}_i$ 为实例描述，$\mathbf{m}_i$ 为实例掩码。这一分解使得后续生成过程能精确绑定每个实例的文本与空间区域。

### 基于 VLM 的实例解析与共享 SEG 策略

针对复杂提示中实例描述交错及同一实例多次出现的问题，InstanceControl 采用 Sa2VA 架构，通过 VLM 解析文本并预测掩码。设计动机是解决现有 VLM 分割模型在非 RGB 视觉条件下因语义歧义导致的定位失败。具体地，VLM 输出固定格式响应，如 `<p>a man in a black jacket</p><seg><1>`，其中 `<seg>` 标记实例身份。对于同一实例的多个描述短语，采用共享 SEG Token (SST) 策略，将相同实例 ID 的 `<seg>` 隐藏状态聚合为统一查询表示 $\mathbf{h}_i$：

$$
\mathbf{h}_i = \frac{1}{M} \sum_{j=1}^{M} \mathbf{h}_{i,j}
$$

其中 $M$ 为实例 $i$ 对应的 `<seg>` 数量。该聚合确保同一实例的多个描述短语在掩码预测时保持一致性，避免重复描述导致的掩码分裂。随后，$\mathbf{h}_i$ 与视觉条件特征输入 SAM 解码器，预测实例掩码 $\mathbf{m}_{pred}^i$ 及置信度 $s_{pred}^i$。

### 掩码精炼模块（MRM）

VLM 预测的掩码可能包含噪声（如区域不完整、定位偏移），直接作为硬约束会损害生成质量。MRM 的设计动机是动态平衡掩码的可靠性与生成模型的内在空间意图。在去噪步骤 $t$，MRM 整合预测掩码 $\mathbf{m}_{pred}^i$、基于注意力的掩码 $\mathbf{m}_{att}^i$（由扩散模型交叉注意力图平均得到）及置信度 $s_{pred}^i$，生成精炼掩码 $\mathbf{m}_{rfn}^i$：

$$
\mathbf{m}_{rfn}^i = f(\mathbf{m}_{pred}^i, \mathbf{m}_{att}^i, s_{pred}^i, \mathbf{H}_{img})
$$

其中 $f$ 为轻量级 U-Net，$\mathbf{H}_{img}$ 为图像潜变量特征。当 $s_{pred}^i$ 高时，$\mathbf{m}_{rfn}^i$ 接近 $\mathbf{m}_{pred}^i$；当 $s_{pred}^i$ 低时，$\mathbf{m}_{rfn}^i$ 向 $\mathbf{m}_{att}^i$ 偏移，利用扩散模型自身的空间注意力修正错误区域。这一机制使模型在掩码准确时严格遵循，在不准确时自适应放松约束，避免过拟合错误区域。

## 实验评估

实验在 MIG-Eval（5,400 图像）和 COCO-POS 基准上进行，对比 FLUX ControlNet、DreamRenderer、EliGen 等基线。基线覆盖免标注（FLUX ControlNet）、免训练（DreamRenderer）及需标注（EliGen, CreatiLayout）路线，但缺失 InstanceAssemble 等最新 MMDiT 方法。

| 方法 | 条件 | MIoU | Local CLIP | Spatial | Color | Shape | Texture | IR | FID |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| FLUX ControlNet | Canny | 0.6526 | 84.67% | 73.30% | 73.93% | 79.24% | - | 0.2558 | 14.0427 |
| InstanceControl | Canny | 0.8250 | 93.54% | 87.78% | 88.19% | 90.88% | - | 0.2847 | 10.0264 |
| DreamRenderer | Canny | 0.6497 | 80.74% | 67.55% | 69.20% | 74.68% | - | 0.2979 | 21.3988 |
| InstanceControl | Depth | 0.8116 | 92.87% | 86.11% | 86.49% | 89.91% | - | 0.2961 | 11.9181 |
| InstanceControl | Hed | 0.8472 | 94.64% | 88.75% | 89.55% | 91.18% | - | 0.3268 | 10.14 |

InstanceControl 在 Canny 条件下 MIoU 达 0.8250，较 FLUX ControlNet 提升 17.24 个百分点，Local CLIP 提升 8.87 个百分点，验证了实例级关联对属性绑定的有效性。在 Depth 条件下，InstanceControl 的 IR 值（0.2961）略高于 FLUX ControlNet（0.2558），但 FID 更低（11.9181 vs 14.0427），表明其在保持全局质量的同时提升了局部细节。

消融实验显示，共享 SEG Token (SST) 使 MIoU 从 0.8214 提升至 0.8250，Local CLIP 从 93.16% 提升至 93.54%，证实了 SST 对多描述实例一致性的重要性。MRM 将 Accuracy 从 87.97% 提升至 90.10%，交互修正后达 93.19%，表明掩码精炼对缓解 VLM 预测噪声的关键作用。

评估边界方面，MIG-Eval 仅包含 5,400 图像，样本量有限；COCO-POS 侧重姿态控制，未覆盖复杂空间关系。论文未报告计算开销，VLM 推理延迟可能影响实时应用。代码未公开，超参数细节缺失，可复现性受限。

## 关联研究分析

从问题动机看，InstanceControl 与 DreamRenderer 均针对多实例属性混淆，但 DreamRenderer 依赖免训练注意力掩码，缺乏实例级语义解析，导致在复杂提示下语义对齐不足。InstanceControl 通过 VLM 解析实例描述，解决了 DreamRenderer 无法处理文本-视觉条件语义歧义的问题。然而，DreamRenderer 的免训练特性使其在新条件上更具适应性，而 InstanceControl 需微调 VLM，可能引入对特定数据集的过拟合。

从方法设计看，InstanceControl 与 EliGen 均使用实例掩码进行控制，但 EliGen 依赖人工标注，推理成本高。InstanceControl 通过 VLM 自动预测掩码，消除了标注需求。然而，EliGen 的掩码精度更高（人工标注），而 InstanceControl 的掩码含噪声，需 MRM 修正。MRM 的贡献是否超过 VLM 解析本身的误差，论文未给出定量分解。此外，InstanceControl 未对比 InstanceAssemble 等基于 MMDiT 的方法，后者通过全局注意力建模复杂空间关系，可能在密集布局上更具优势。

## 总结

InstanceControl 解决了多实例可控生成中实例描述与视觉区域缺乏绑定的核心矛盾，通过 VLM 自动解析实例掩码并引入 MRM 动态修正，实现了免标注的细粒度控制。在 MIG-Eval 上，其 Canny 条件 MIoU 达 0.8250，较 FLUX ControlNet 提升 17.24 个百分点，验证了实例级关联的有效性。然而，其性能依赖 VLM 对非 RGB 视觉条件的泛化能力，且未验证在极端密集布局下的鲁棒性。当实例数量超过 10 时，VLM 解析的准确率是否显著下降，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.31924)
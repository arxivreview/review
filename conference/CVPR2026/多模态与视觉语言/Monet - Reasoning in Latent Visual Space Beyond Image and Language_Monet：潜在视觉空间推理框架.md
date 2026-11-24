# CVPR2026最新论文 ｜Monet: Reasoning in Latent Visual Space Beyond Image and Language ｜Monet：潜在视觉空间推理框架

作者：Qixun Wang、Yang Shi、Yifei Wang 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b685144df8fe)

> 多模态大语言模型（MLLMs）在视觉推理中依赖外部工具或离散文本，导致抽象视觉思维受限且推理延迟高。现有潜在推理方法存在对齐成本高、潜在嵌入优化不足两大瓶颈，Monet通过三阶段蒸馏SFT与专用强化学习算法VLPO，使模型在无外部工具依赖下生成连续潜在嵌入作为中间视觉思维。该框架在分布外任务上展现显著泛化优势，但分布内任务性能仍低于部分解耦架构，其潜在嵌入的语义可解释性仍存疑。

## 研究背景

当MLLMs处理几何或空间推理任务时，模型需将高维视觉信息压缩为离散文本token，这一过程丢失细粒度空间结构，导致“视觉幻觉”与逻辑错误。为弥补此缺陷，早期方法引入“思维链”（Chain-of-Thought, CoT）范式，但文本带宽瓶颈使模型无法承载复杂视觉证据；随后“图像思维”（Thinking with Images）路线通过裁剪、缩放等外部工具获取高分辨率局部特征，却受限于工具刚性、多轮异步推理带来的高延迟，且难以泛化至未预训练的视觉操作。

潜在视觉推理旨在突破上述限制，通过在连续潜在空间生成视觉思维保留高维感知细节。然而，现有方法如LVR直接对齐潜在嵌入与辅助图像嵌入，面临数千图像token对齐的计算开销，且均值池化压缩会扭曲视觉特征；同时，监督微调（Supervised Fine-Tuning, SFT）中的下一令牌预测（Next-Token Prediction, NTP）损失易过拟合文本，而组相对策略优化（Group Relative Policy Optimization, GRPO）仅能计算文本token的策略梯度，导致潜在嵌入缺乏直接优化信号。Monet的切入点在于解耦潜在嵌入的生成与优化，通过双监督机制降低对齐成本，并设计针对潜在空间的强化学习算法，实现无工具依赖的灵活视觉推理。

## 核心方法

### 方法参照系

潜在视觉推理的标准流程是生成连续潜在嵌入替代文本token，并通过SFT对齐潜在嵌入与辅助图像嵌入，再应用GRPO进行强化学习。Monet的关键差异在于放弃直接图像对齐，转而采用“观察token对齐+受控注意力流”双监督，并引入VLPO替代GRPO以直接优化潜在嵌入。

### 双监督SFT框架

SFT Stage 2中，模型需生成高质量目标潜在嵌入 $h^*_{latent}$。传统做法直接对齐潜在嵌入与辅助图像嵌入，但计算成本高且易扭曲特征。Monet改为对齐观察token的隐藏表示：当条件为辅助图像或生成潜在嵌入时，观察token的表示应一致。对齐损失定义为：

$$L_{align-obs} = \frac{1}{N} \sum_{i} \sum_{l} \left( 1 - \cos(h^*_{obs}^{(i,l)} \cdot \text{detach()}, \hat{h}_{obs}^{(i,l)}) \right)$$

该公式强制潜在嵌入选择性编码辅助图像中的关键视觉线索，而非记忆后续文本。同时，通过受控注意力掩码，潜在嵌入可直接访问辅助图像嵌入，但文本token不可见，确保视觉信息流为“辅助图像→潜在嵌入→观察token”。此设计解决了NTP损失过拟合文本、潜在嵌入缺乏有效监督的问题，使模型在无显式图像对齐成本下保留视觉细节。

### VLPO强化学习算法

GRPO仅优化文本token，对潜在嵌入无直接监督，导致潜在推理能力停滞。VLPO通过估计潜在嵌入的输出概率，将其纳入策略梯度更新。在rollout过程中，VLPO计算潜在嵌入的近似概率，并优化总损失：

$$L_{VLPO} = L_{NTP} + \beta \cdot L_{latent}$$

其中 $L_{latent}$ 为潜在嵌入的策略梯度项。该算法使潜在嵌入在RL阶段获得直接优化信号，弥补GRPO的缺陷。实验表明，VLPO显著提升分布外任务（如VisualPuzzles）性能，而GRPO仅增强非潜在推理，验证了潜在空间优化的必要性。

## 实验评估

实验基于VLMEvalKit框架，在V*、HRBench4K、HRBench8K、MME-RealWorld-Lite及VisualPuzzles上评估。基线覆盖Qwen2.5-VL-7B、Vanilla SFT、SFT+GRPO、DeepEyes、LVR及GPT-4o等，但缺失SPARC等最新解耦架构对比。主结果显示，Monet-7B在V*上达83.25%，HRBench4K达71.00%，VisualPuzzles达35.02%，较Qwen2.5-VL-7B提升4.25%–9.75%，且OOD泛化显著优于SFT+GRPO。

| 模型 | V* | HRBench4K | HRBench8K | MME-RealWorld-Lite | VisualPuzzles |
|---|---|---|---|---|---|
| Qwen2.5-VL-7B | 76.44 | 77.39 | 75.00 | 68.00 | 26.32 |
| Monet-7B (SFT + VLPO) | 83.25 | 71.00 | 68.00 | 55.50 | 35.02 |
| DeepEyes | 83.25 | 84.35 | 81.58 | 71.25 | 26.79 |
| LVR | 80.6 | 81.7 | 79.0 | - | - |

消融实验揭示关键设计决策：移除潜在嵌入专用反向传播（w/o latent-only BP）导致V*性能骤降至46.07%，证明潜在嵌入优化不可通过文本捷径替代；移除辅助图像可见性（w/o auxiliary img）使V*降至73.30%，验证受控注意力流的必要性。VLPO在VisualPuzzles上较SFT提升4.54%，而GRPO仅提升1.03%，表明VLPO对OOD泛化的贡献显著高于GRPO。

评估边界方面，论文未报告置信区间，数值比较需谨慎；代码已开源（github.com/NOVAglow646/Monet），但超参数与GPU配置未在正文详述，可复现性依赖补充材料。

## 关联研究分析

从方法设计看，Monet与LVR的核心差异在于对齐机制：LVR直接对齐潜在嵌入与辅助图像嵌入，而Monet对齐观察token的隐藏表示。这一差异源于任务特性：LVR聚焦裁剪区域，无法编码全图视觉操作；Monet通过观察token对齐，使潜在嵌入承载更广泛的视觉线索，但牺牲了直接图像监督的直观性。VLPO与GRPO的差异则源于优化目标：GRPO仅优化文本token，而VLPO将潜在嵌入纳入策略梯度，解决了潜在推理在RL阶段的优化缺失。这一改进是否在其他模态潜在推理中泛化，论文未给出回答。

从问题动机看，Monet与DeepEyes代表不同路线：DeepEyes依赖外部裁剪工具，Monet生成内部潜在嵌入。DeepEyes在HRBench4K上达84.35%，高于Monet的71.00%，表明外部工具在高分辨率感知任务上仍有优势；但Monet在VisualPuzzles上达35.02%，远超DeepEyes的26.79%，证明内部潜在推理在抽象视觉推理上更具泛化性。这一差异暗示，外部工具适合细粒度定位，而潜在推理适合抽象逻辑，但两者在高分辨率感知与抽象推理间的权衡边界，论文未明确界定。

## 总结

Monet要解决的核心矛盾是潜在视觉推理中对齐成本高与潜在嵌入优化不足。其切入点在于解耦潜在嵌入的生成与优化，通过双监督SFT降低对齐成本，VLPO直接优化潜在嵌入。实验证明，Monet-7B在VisualPuzzles上达35.02%，较SFT提升4.54%，验证了VLPO对OOD泛化的贡献。但Monet在HRBench4K上仅71.00%，低于DeepEyes的84.35%，暴露其在高分辨率感知任务上的局限。当潜在嵌入数量Ktest从8增至12时，V*性能从82.20%降至80.10%，表明潜在嵌入的边际收益递减，且其语义结构是否随Ktest增加而更清晰，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_b685144df8fe)
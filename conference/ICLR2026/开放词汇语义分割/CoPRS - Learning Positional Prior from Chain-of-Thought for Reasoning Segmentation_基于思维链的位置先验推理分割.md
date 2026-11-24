# ICLR2026最新论文 ｜CoPRS: Learning Positional Prior from Chain-of-Thought for Reasoning Segmentation ｜基于思维链的位置先验推理分割

研究机构：中国科学院、哈尔滨工业大学

作者：Zhenyu Lu、Liupeng Li、Jinpeng Wang 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.11173)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.11173)

> 推理分割要求模型解析包含空间关系与逻辑组合的复杂指令，并输出对应目标的像素级掩码。现有方法要么直接解码语言模型隐特征导致中间过程不可解释，要么生成离散文本坐标导致语义细节丢失且易受格式错误影响。CoPRS 引入多模态思维链（MCoT）生成可微分的位置先验热力图，作为语言推理与掩码解码之间的透明接口，并通过组相对策略优化（GRPO）与监督分割损失联合训练。该设计在 RefCOCO 系列与 ReasonSeg 上达到当前最优性能，但其对 MLLM 推理质量的依赖及位置先验在极端遮挡下的鲁棒性仍存疑。

## 研究背景

当指令包含“被树木部分遮挡且位于四轴飞行器后方的无人机”这类复合约束时，模型需同时解析空间拓扑与物体属性。传统语义分割仅输出类别标签，无法处理此类动态指令；指代分割虽能定位单一物体，但依赖短文本且缺乏推理能力。推理分割（Reasoning Segmentation）将任务扩展至自由形式指令，要求模型在生成掩码前完成显式推理，这构成了从静态感知向动态认知跨越的关键瓶颈。

现有推理分割方法分为两派：隐式推理方法（如 LISA）直接解码 MLLM 隐状态生成掩码，中间决策不透明且不可控；文本推理方法（如 Seg-Zero）生成离散坐标（框或点）再交由 SAM 等模型解码，虽显式但缺乏细粒度视觉语义，且对格式错误敏感。两派均存在可解释性与表示保真度之间的权衡缺陷。CoPRS 的切入点在于设计一种密集、可微分的位置先验（Positional Prior），既保留 MCoT 的推理透明度，又提供比离散坐标更丰富的空间细节，从而在单一端到端框架中统一推理与分割。

## 核心方法

### 方法参照系

推理分割的标准流程为：MLLM 解析指令生成空间提示，分割模型解码掩码。本文问题与该通用流程的关键差异在于：标准流程中空间提示为隐特征或离散坐标，而 CoPRS 将其重构为可微分热力图，并引入强化学习优化推理轨迹。

### 可微分位置先验生成

设计动机：解决隐式推理不可解释与文本推理语义细节丢失的双重失效。MLLM 生成 CoT 后输出可学习浓度令牌（Concentration Token），其嵌入 $e_{conc}$ 经查询头映射为查询向量 $Q$。视觉骨干（SAM ViT-H）提取图像特征作为键 $K$。通过缩放点积多头注意力计算位置先验热力图 $H_{prior}$：

$$ H_{prior} = F_{fuse}\left( \text{softmax}\left( \frac{Q W_i^Q (K W_i^K)^T}{\sqrt{d_h}} \right) \right) $$

其中 $F_{fuse}$ 为两层 2D 卷积聚合多头特征。该热力图作为密集空间证据，比隐特征可解释，比离散坐标更精细，直接指导掩码解码。

### GRPO 与监督联合优化

设计动机：解决单一监督信号无法同时优化推理质量与分割精度的问题。统一目标函数耦合语言路径的 GRPO 损失与视觉路径的分割损失：

$$ \mathcal{L}_{total} = \mathcal{L}_{GRPO} + \lambda_{seg} \mathcal{L}_{SEG} $$

其中 $\mathcal{L}_{SEG}$ 包含对 $H_{prior}$ 的 BCE 损失、对预测掩码 $\hat{M}$ 的 Dice 损失与 Focal 损失。GRPO 通过组内相对优势优化 MLLM 推理策略，分割损失通过可微分位置先验反向传播至 MLLM，实现推理与分割的协同增强。

## 实验评估

实验在 RefCOCO、RefCOCO+、RefCOCOg 训练，ReasonSeg 零样本评估。基线覆盖无 LLM、隐式推理、文本推理三类，但未对比 OVSS 经典方法（如 SCLIP），因任务范式不同。

| 方法 | RefCOCO val cIoU | RefCOCO testA cIoU | RefCOCO+ val cIoU | ReasonSeg val gIoU |
|---|---|---|---|---|
| LISA-13B | 79.1 | 72.9 | 70.6 | 52.3 |
| Seg-Zero-7B | – | 80.3 | – | 62.6 |
| RAS-13B | 83.5 | 80.0 | 77.5 | – |
| CoPRS-7B | 81.6 | 85.3 | 80.3 | 65.2 |

CoPRS-7B 在 RefCOCO testA 上以 85.3 超越 RAS-13B 的 80.0，在 ReasonSeg val gIoU 上以 65.2 领先 Seg-Zero-7B 的 62.6。消融显示：GRPO 组大小 $G=8$ 时收敛样本数非线性增长，性能最优；联合训练（RL+Seg）优于单独 RL 或 Seg；掩码奖励系数 0.7 时性能最佳，1.0 时略降，表明格式分数作为正则化器有助于泛化。

评估边界：仅报告 cIoU/gIoU，未提供边界精度指标（如 Boundary IoU）；ReasonSeg 零样本评估未报告置信区间；代码已开源，但 MLLM 骨干选择（Qwen2.5-VL）对结果影响较小，暗示方法对骨干不敏感，但视觉骨干（ViT-H）贡献有限，未探索更轻量视觉编码器。

## 关联研究分析

从问题动机看，CoPRS 与 LISA 同属 MLLM 驱动推理分割，但 LISA 依赖隐特征解码，CoPRS 引入显式 MCoT 与位置先验。差异根源在于任务特性：LISA 假设隐特征已包含足够空间信息，而 CoPRS 认为推理过程需显式化以处理复杂指令。CoPRS 的位置先验是否真正优于隐特征，在简单指令场景下可能无显著优势，论文未给出对比。

从方法设计看，CoPRS 与 Seg-Zero 同用 MLLM 生成空间提示，但 Seg-Zero 输出离散坐标，CoPRS 输出密集热力图。差异根源在于表示保真度：离散坐标缺乏像素级语义，热力图保留空间连续性。然而，热力图生成依赖 MLLM 推理质量，若 CoT 错误，位置先验将误导分割。Seg-Zero 的离散坐标虽粗糙，但格式错误率低，在极端场景下可能更鲁棒。CoPRS 未评估 CoT 错误率对分割性能的影响，这是其方法边界的关键盲区。

## 总结

CoPRS 解决的核心矛盾是推理分割中可解释性与表示保真度的权衡。其切入点是设计可微分位置先验，将 MCoT 推理显式化为空间热力图，并通过 GRPO 与监督损失联合优化。实验证明该方法在 RefCOCO testA 上达到 85.3 cIoU，ReasonSeg val 上达到 65.2 gIoU，超越现有基线。其边界在于：位置先验质量高度依赖 MLLM 推理准确性，且未评估 CoT 错误传播对分割的影响。当指令包含高度歧义或反事实描述时，位置先验是否仍能保持鲁棒性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.11173)
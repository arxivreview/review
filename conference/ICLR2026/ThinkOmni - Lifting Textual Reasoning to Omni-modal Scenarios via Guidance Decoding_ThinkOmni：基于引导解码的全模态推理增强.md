# ICLR2026最新论文 ｜ThinkOmni: Lifting Textual Reasoning to Omni-modal Scenarios via Guidance Decoding ｜ThinkOmni：基于引导解码的全模态推理增强

研究机构：华中科技大学、小米

作者：Yiran Guan、Sifan Tu、Dingkang Liang 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.23306)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.23306)

> 全模态大语言模型（Omni-modal Large Language Model, OLLM）虽能感知多模态输入，却缺乏大型推理模型（Large Reasoning Model, LRM）的深度逻辑推导能力，导致其在复杂跨模态任务中表现受限。现有增强方案依赖昂贵的监督微调或强化学习，且往往局限于特定模态或任务，缺乏通用性。ThinkOmni 提出一种免训练框架，通过引导解码将文本 LRM 的推理能力无损迁移至 OLLM 的解码过程。该框架在六个基准上验证了免训练增强的可行性，但其性能增益是否完全源于骨干模型能力而非方法本身，仍需进一步审计。

## 研究背景

当 OLLM 处理包含图像、音频的复杂数学问题时，其自回归生成机制往往陷入感知与推理的割裂：模型能识别视觉元素，却无法执行多步逻辑推导。这种割裂源于 OLLM 的训练目标侧重于模态对齐而非逻辑深度，而 LRM 虽具备强大的链式推理能力，却受限于纯文本输入，无法直接处理多模态数据。解决这一矛盾的关键在于如何在不更新参数的前提下，将 LRM 的推理偏好注入 OLLM 的解码过程。

全模态推理增强的主流路线依赖大规模数据微调，如 Omni-R1 和 HumanOmniV2 通过强化学习微调（Reinforcement Learning Finetuning, RFT）提升推理能力，但这种方法需要数万条高质量推理样本及高昂的算力成本（如 32B 模型需 16×80G VRAM），且效果往往局限于特定下游任务。相比之下，测试时推理增强路线旨在通过解码策略优化提升性能，但现有方法如视觉对比解码（Visual Contrastive Decoding, VCD）仅关注幻觉抑制，缺乏对推理深度的动态调控。ThinkOmni 的切入点在于利用 LRM 作为外部引导信号，通过 Logits 层面的对比机制，实现感知信号与推理信号的自适应平衡，从而在免训练条件下突破 OLLM 的推理天花板。

## 核心方法

### 引导解码参照系

本文问题置于测试时推理增强框架下，其核心差异在于跨模态引导信号的构建。传统引导解码（如 VCD）依赖同模型不同输入的对比，而 ThinkOmni 引入异构模型（LRM）作为正例，通过 Logits 混合实现跨模态能力融合。

### LRM-as-a-Guide

固定引导权重 $\alpha$ 无法适应不同任务对感知与推理的需求差异，导致在数学任务中推理不足或在感知任务中幻觉频发。ThinkOmni 提出 LRM-as-a-Guide 策略，将 OLLM 的全模态 Logits $z_{base}$ 与纯文本 Logits $z_{-}$ 及 LRM 的文本 Logits $z_{+}$ 进行对比混合。

$$
z_t = z_{base} + \alpha (z_{+} - z_{-})
$$

该公式通过放大 LRM 相对于 OLLM 纯文本输出的差异，将推理偏好注入 OLLM 的解码过程。LRM 虽无法访问多模态内容，但通过已解码的文本前缀逐步补偿信息缺失，而 OLLM 则通过 Logits 混合获得逻辑深度，两者在解码过程中形成互补。

### Stepwise Contrastive Scaling

固定 $\alpha$ 导致模型在感知主导任务（如音频识别）中过度依赖推理信号，或在推理主导任务（如几何计算）中感知信号被稀释。Stepwise Contrastive Scaling 模块通过实时分析 Logits 分布，动态调整感知与推理信号的权重。

$$
\alpha_t^{[r]} = \frac{D_R}{D_R + D_P}, \quad \alpha_t^{[p]} = \frac{D_P}{D_R + D_P}
$$

其中 $D_R$ 和 $D_P$ 分别为 Jensen-Shannon 散度度量的推理与感知信号差异。该机制通过在线计算分布距离，自动分配每个解码步的“预测预算”，确保在需要推理的步骤增强 LRM 引导，在需要感知的步骤强化 OLLM 的多模态线索，无需人工调参即可适应任务变化。

## 实验评估

实验在 MathVista、MMAU 等六个全模态基准上进行，基线覆盖 RFT 模型（Omni-R1, HumanOmniV2）及免训练方法（VCD, ProxyTuning）。主结果显示，ThinkOmni 在 Qwen2.5-Omni-7B 上取得 MathVista 70.2% 和 MMAU 75.5% 的成绩，超越所有 RFT 基线。

| 方法 | MathVista | MMAU | OmniBench |
| :--- | :--- | :--- | :--- |
| Qwen2.5-Omni-7B | 66.8 | 71.5 | 42.1 |
| Omni-R1 | 64.7 | 70.5 | 43.0 |
| HumanOmniV2 | 68.8 | 75.3 | 41.9 |
| ThinkOmni (+Qwen3) | 70.2 | 75.5 | 43.6 |

消融实验表明，固定权重 $\alpha$ 在极端值下性能显著下降，而动态权重在不同任务间呈现明显分布偏移，验证了自适应机制的必要性。LRM 规模实验显示，Qwen3-14B 在 MMAU 上未带来进一步增益，暗示推理能力对感知主导任务的边际收益递减。

评估协议采用 GPT-4o 进行答案提取，可能存在提取偏差。代码已开源，但论文未报告置信区间，且未控制 LRM 骨干网络与 OLLM 的预训练数据差异，性能增益归因需谨慎。

## 关联研究分析

从问题动机看，ThinkOmni 与 RLVR 路线存在根本差异。RLVR 通过训练更新参数以优化策略，而 ThinkOmni 依赖外部 LRM 的静态推理偏好。这种差异源于任务特性：全模态数据稀缺使得训练成本过高，而 LRM 的文本推理能力已足够成熟，可直接作为引导信号。然而，RLVR 能激发模型内部的新策略，而 ThinkOmni 仅能迁移 LRM 已有的推理模式，其在组合泛化任务上的表现可能受限。

从方法设计看，ThinkOmni 与 LTPO 同属测试时优化，但 LTPO 优化潜在向量，ThinkOmni 优化 Logits 分布。LTPO 依赖模型潜在空间的可微分性，适用于有明确奖励信号的任务，而 ThinkOmni 通过 Logits 对比实现跨模态融合，无需奖励信号，但引入了双模型推理的延迟开销。ThinkOmni 的 Stepwise Contrastive Scaling 机制比 LTPO 的端到端优化更具可解释性，但依赖 Jensen-Shannon 散度的准确性，对分布不稳定的任务可能失效。

## 总结

ThinkOmni 旨在解决 OLLM 感知与推理能力割裂的矛盾，通过免训练引导解码将 LRM 的推理能力迁移至全模态场景。其核心创新在于 LRM-as-a-Guide 与 Stepwise Contrastive Scaling 的结合，实现了感知与推理信号的自适应平衡。实验证明，该方法在 MathVista 上达到 70.2%，超越 RFT 基线，验证了免训练增强的有效性。然而，论文未报告置信区间，且 LRM 规模实验显示推理能力对感知任务的边际收益递减，暗示方法在感知主导任务上的增益可能有限。当 OLLM 的感知能力接近饱和时，外部 LRM 引导的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.23306)
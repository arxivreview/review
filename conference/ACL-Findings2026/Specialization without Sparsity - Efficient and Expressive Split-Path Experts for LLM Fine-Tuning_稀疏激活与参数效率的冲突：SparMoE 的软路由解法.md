# ACL-Findings2026最新论文 ｜Specialization without Sparsity: Efficient and Expressive Split-Path Experts for LLM Fine-Tuning ｜稀疏激活与参数效率的冲突：SparMoE 的软路由解法

作者：Ganghao Liu、Qin Zhou、Zhe Wang 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9081507bc433)

> 参数高效微调（PEFT）旨在以极小参数代价适配大模型，但现有 MoE-PEFT 方法将 LoRA 复制为专家并采用离散硬路由，导致参数量随专家数线性膨胀，且在数据稀缺下因路由高方差引发专家欠训练。本文指出离散选择与受限参数空间存在根本错配，提出 SparMoE，以全激活软路由替代硬路由，并用缩放-偏置双路径向量专家替代低秩矩阵专家，在 GLUE 上以 0.29M 参数超越全量微调。该设计在低资源微调场景下有效，但其全激活机制在长序列下的计算开销未经验证，且缺乏与大规模 LLM 推理任务 SOTA 的直接可比性。

## 研究背景

当预训练模型参数量突破千亿级，全量微调的显存与计算开销变得不可承受，PEFT 通过冻结骨干、仅更新少量参数（如 LoRA 的低秩矩阵）实现任务适配。然而，单一 LoRA 模块的表达能力有限，难以捕捉复杂多面任务中的多样化特征。为突破这一瓶颈，研究者尝试将 MoE 引入 PEFT，用多个 LoRA 专家替代单一模块，期望通过专家分工提升表征容量。

主流 MoE-PEFT 路线（如 LoRAMoE、MoELoRA）直接复制 LoRA 矩阵作为专家，并沿用标准 MoE 的 Top-K 硬路由。这一设计在参数充足时可行，但在 PEFT 的受限参数空间下暴露出两个核心缺陷：其一，LoRA 参数量随专家数线性增长，迅速侵蚀 PEFT 的效率优势；其二，离散硬路由的高方差特性在数据稀缺条件下导致部分专家长期未被激活或训练不足，优化过程不稳定。此外，硬路由需引入辅助负载均衡损失与敏感的 Top-K 超参数，进一步增加了调优复杂度。SparMoE 的切入点在于：既然离散选择是优化不稳定的根源，且 LoRA 矩阵并非专家化必需，那么能否用连续、全激活的软路由与更轻量的专家参数化，在保持参数效率的同时提升表征多样性？

## 核心方法

### 方法参照系

标准 MoE 架构通过门控网络从 N 个 FFN 专家中选择 K 个（K≪N）进行计算，输出为加权求和。SparMoE 的问题场景是 PEFT，骨干冻结，仅更新适配模块。与标准 MoE 的关键差异在于：SparMoE 不追求稀疏激活以降低计算量，而是追求在极低参数量下最大化表征多样性，因此摒弃了 FFN 专家与硬路由，采用全激活软路由与向量级专家。

### 全激活软路由机制

硬路由的离散选择导致梯度流中断，在数据稀缺时加剧专家欠训练。SparMoE 改用软路由，对每个 Token 计算所有专家的连续权重，确保端到端梯度稳定流动，无需辅助负载均衡损失。给定 FFN 输出 $h \in \mathbb{R}^{S \times H}$，路由函数 $G: \mathbb{R}^H \to \mathbb{R}^E$ 生成 Token 级混合权重：

$$p = \text{softmax}(G(h)) \in \mathbb{R}^{S \times E}$$

最终适配表示为所有专家输出的加权求和：

$$h' = \sum_{e=1}^{E} p_{:,e} \odot z^{(e)}$$

这一设计消除了 Top-K 超参数与负载均衡损失，使优化过程在低数据量下更稳定，且所有专家均参与计算，避免了“死专家”问题。

### 缩放-偏置双路径专家设计

LoRA 专家依赖矩阵乘法，参数量随秩 r 和专家数 E 双重增长。SparMoE 将每个专家参数化为两个可学习向量：缩放路径 $l^{(e)}_{\text{scaling}}$ 与偏置路径 $l^{(e)}_{\text{bias}}$。专家输出为：

$$z^{(e)} = \underbrace{(1-\rho) \cdot (h \odot l^{(e)}_{\text{scaling}}) \odot m}_{z^{(e)}_{\text{scaling}}} + \underbrace{(h + l^{(e)}_{\text{bias}})}_{z^{(e)}_{\text{bias}}}$$

其中 $m \sim \text{Bernoulli}(1-\rho)$ 为 Dropout 掩码。缩放路径通过乘法调制特征维度，Dropout 引入随机性以增强专家多样性；偏置路径提供加法偏移，在 Dropout 抑制缩放信号时保留专家特异性。这种设计使专家参数量仅与隐藏维度 H 成正比，与专家数 E 无关，从而在增加专家数时不显著增加参数开销。

## 实验评估

实验在 GLUE（RoBERTa-base/large）、GSM8K（LLaMA2-7B）、MBPP（LLaMA2-13B）及 SmolTalk（Qwen 系列）上进行，基线覆盖 LoRA、DoRA、QLoRA、LoRA+、Adapter、BitFit、IA3、RED 及 MoELoRA。在 RoBERTa-large 上，SparMoE 以 0.29M 可训练参数取得 88.6 的平均 GLUE 分数，超越全量微调（88.5）及所有 PEFT 基线，其中 SST-2（96.1）、MRPC（93.5）、CoLA（68.3）均取得最佳 PEFT 性能。在 LLaMA2-7B GSM8K 上，SparMoE 以 1.6M 参数达到 23.12% 准确率，优于 LoRA (r=8) 的 22.29%（8.4M 参数），参数量减少约 80%。

| 模型 | 方法 | 参数量 (M) | GLUE Avg. | GSM8K Acc. (%) | MBPP Score |
|---|---|---|---|---|---|
| RoBERTa-large | SparMoE | 0.29 | 88.6 | – | – |
| RoBERTa-large | FT | 355 | 88.5 | – | – |
| RoBERTa-large | LoRA | 0.8 | 88.1 | – | – |
| LLaMA2-7B | SparMoE | 1.6 | – | 23.12 | – |
| LLaMA2-7B | LoRA (r=8) | 8.4 | – | 22.29 | – |
| LLaMA2-13B | SparMoE | 2.5 | – | – | 29.18 |
| LLaMA2-13B | LoRA+ | 3.3 | – | – | 30.35 |

在 MBPP 上，SparMoE 以 2.5M 参数取得 29.18 分，略低于 LoRA+ 的 30.35 分（3.3M 参数），但参数量更少。资源效率方面，SparMoE 在 GSM8K 上消耗 16.25 GB 显存，训练时间 14.7 分钟，优于 LoRA (r=8) 的 25.3 GB 与 18.2 分钟。消融实验未单独报告，但论文指出 MoELoRA 因超参数复杂导致部分 GLUE 任务结果缺失，而 SparMoE 在所有任务上表现稳定，暗示软路由与向量专家设计降低了调优敏感性。

评估边界方面，实验未报告置信区间，且 GSM8K/MBPP 的绝对数值较低（23.12%/29.18%），可能受限于 LLaMA2 基础模型在推理任务上的能力上限，而非微调方法本身。代码未公开，超参数（如专家数 E=4/8、Dropout 率 ρ）未提供完整列表，可复现性受限。

## 关联研究分析

从问题动机看，SparMoE 与 LoRAMoE 的根本分歧在于对“专家化”的实现路径。LoRAMoE 假设专家化需要独立的低秩矩阵，因此复制 LoRA 并依赖硬路由选择；SparMoE 则认为专家化可通过向量级调制实现，硬路由是优化不稳定的根源而非必要组件。这一差异源于任务特性：PEFT 场景下参数预算极紧，LoRA 的矩阵乘法开销不可接受，而向量调制以 O(H) 参数实现专家特异性，更符合 PEFT 的效率约束。然而，SparMoE 的全激活软路由在长序列下计算量为 O(S·E·H)，而硬路由为 O(S·K·H)，当序列长度 S 极大时，SparMoE 的计算开销可能反超硬路由，论文未对此进行量化分析。

从方法设计看，SparMoE 与标准 SMoE 架构（如 Switch Transformer）在路由机制上形成鲜明对比。Switch Transformer 采用 Top-1 硬路由以最小化计算量，SparMoE 采用全激活软路由以最大化优化稳定性。这一冲突暗示：在训练阶段，优化稳定性比计算效率更重要；但在推理阶段，计算效率可能成为瓶颈。SparMoE 的缩放-偏置双路径设计借鉴了 Adapter 的乘法调制思想，但通过 Dropout 引入随机性以增强多样性，这一机制在数据充足时是否仍具优势，论文未给出回答。

## 总结

SparMoE 要解决的核心矛盾是 PEFT 场景下离散硬路由的高方差优化问题与 LoRA 专家参数线性膨胀问题。现有方法如 LoRAMoE 未能解决这一矛盾，因为硬路由与 LoRA 矩阵是相互耦合的设计选择。SparMoE 通过全激活软路由消除离散选择，用缩放-偏置向量专家替代 LoRA 矩阵，在 RoBERTa-large 上以 0.29M 参数超越全量微调（88.6 vs 88.5），在 LLaMA2-7B GSM8K 上以 1.6M 参数达到 23.12% 准确率。其边界在于：全激活机制在长序列下的计算开销未量化，且实验局限于中小规模模型，缺乏与大规模 LLM 推理任务 SOTA 的直接可比性。当序列长度超过 4K 时，软路由的计算开销是否仍优于硬路由，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_9081507bc433)
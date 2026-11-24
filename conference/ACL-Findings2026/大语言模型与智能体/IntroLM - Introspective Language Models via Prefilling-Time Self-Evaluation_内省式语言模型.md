# ACL-Findings2026最新论文 ｜IntroLM: Introspective Language Models via Prefilling-Time Self-Evaluation ｜内省式语言模型

研究机构：澳大利亚墨尔本大学、澳大利亚莫纳什大学

作者：Hossein Hosseini Kasnavieh、Gholamreza Haffari、Chris Leckie 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.03511)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.03511)

> 导读 LLM路由的核心矛盾在于：准确预测查询复杂度需要强模型，但部署独立评估器会抵消路由带来的效率收益。现有基于BERT的外部分类器受限于512 token上下文窗口，无法处理现代长上下文部署场景，且引入额外推理开销。本文切入点是将复杂度预测内化到目标模型自身的Prefilling阶段，通过[CPX] token与Token-conditional LoRA实现零额外解码开销的自评估。该方法在长上下文基准上显著优于外部分类器，但其标量预测范式与领域内直接决策趋势的兼容性存疑。

## 研究背景

因果语言模型处理输入分为Prefilling与Decoding两个阶段：Prefilling并行计算所有token的隐藏状态，Decoding基于最终token状态自回归生成。这一结构意味着Prefilling阶段已包含对完整输入的上下文化表示，理论上可用于质量预测，但骨干网络的表示是为生成优化而非评估设计，直接应用分类器效果不佳。

LLM路由旨在为异构查询分配成本-性能最优的模型。主流路线依赖外部编码器（如BERT）在生成前预测查询复杂度，但此类方法面临双重瓶颈：一是BERT固定512 token窗口无法处理数万token的Prefill输入，二是独立评估器需额外推理，抵消路由效率。RouteLLM等基于偏好数据的方法虽提升预测精度，但未解决长上下文下的表示能力限制。本文抓住“评估信号来源”这一被忽略的环节，提出利用目标模型自身Prefilling表示进行内省式复杂度预测，从根源上消除外部评估器的上下文限制与计算开销。

## 核心方法

### 方法参照系

传统路由信号生成采用独立编码器：输入查询，输出复杂度分数，基于阈值路由。本文问题与该流程的关键差异在于：信号来源从外部模型转为目标模型内部，且评估时机前移至Prefilling阶段，要求评估过程不干扰生成行为。

### [CPX] Introspection Token机制

在Prefilling阶段，于输入末尾追加特殊[CPX] token，其隐藏状态经轻量分类头输出复杂度分数。该设计解决了外部评估器无法访问长上下文的问题：[CPX] token通过自注意力机制关注完整前缀，构建专用复杂度表示。关键约束是[CPX] token被排除在Key-Value Cache之外，且解码从原始提示最后一个token状态初始化，确保生成行为与基线模型完全一致。

$$
\text{Complexity Score} = \text{Classifier}(h_{\text{[CPX]}})
$$

其中$h_{\text{[CPX]}}}$为[CPX] token在Prefilling阶段的隐藏状态。该公式表明复杂度预测仅依赖Prefilling计算，无需额外解码步骤。

### Token-conditional LoRA适配

为在不改变生成行为的前提下学习复杂度信号，本文提出Token-conditional LoRA：仅对[CPX] token位置应用低秩更新，其他token保持预训练权重。具体实现中，对线性投影$W$，计算标准变换$HW$与LoRA更新$H\Delta W$，通过二元掩码$M$（[CPX]位置为1，其他为0）选择性地应用更新：

$$
\text{Output} = HW + (H\Delta W) \odot M
$$

该机制解决了直接微调骨干网络会破坏生成行为的问题：LoRA参数仅影响[CPX] token的计算路径，占模型总参数不足1%，且仅适配Query投影与Feed-forward网络，保持Key/Value投影冻结以维持注意力模式稳定性。

## 实验评估

实验在GENERAL QA（MMLU+MMLU-PRO+GSM8K）、HOTPOTQA（长上下文多跳推理）和LMSYS-CHAT-1M（日常对话）三个基准上评估，基线包括DeBERTa-v3-Base/Large与Random Routing。缺失RouteLLM、xRouter等基于偏好数据或强化学习的路由方法直接对比，仅验证信号源差异。

| 模型 | GENERAL QA ROC-AUC | GENERAL QA PR-AUC | HOTPOTQA ROC-AUC | HOTPOTQA PR-AUC | CHAT ROC-AUC |
|---|---|---|---|---|---|
| DeBERTa-v3-Base (184M) | 74.3 | 44.3 | 69.4 | 24.3 | 82.6 |
| DeBERTa-v3-Large (435M) | 75.8 | 45.5 | 71.8 | 26.8 | 86.3 |
| IntroLM (Qwen3-8B) | 89.1 | 63.4 | 86.3 | 46.7 | 90.1 |

IntroLM在HOTPOTQA上ROC-AUC达86.3%，较DeBERTa-v3-Large提升14.5个百分点，验证长上下文优势；在CHAT场景优势收窄至3.8个百分点，表明短文本下外部分类器仍具竞争力。

消融实验显示，移除[CPX] token仅使用最后prompt token隐藏状态时，HOTPOTQA性能显著下降，证明[CPX] token对长上下文复杂度捕获的关键作用。骨干容量对比中，Qwen3-1.7B的IntroLM ROC-AUC为84.24%，低于Qwen3-8B的89.1%，但均优于DeBERTa-v3-Large的75.68%，表明模型容量提升可改善内省信号质量。

评估边界方面：指标仅报告ROC-AUC/PR-AUC，未提供置信区间；路由评估假设大模型为高可靠性回退，未考虑大模型失败场景；代码未公开，超参数细节在附录中，可复现性受限。

## 关联研究分析

从信号来源看，IntroLM与RouteLLM的根本差异在于评估器独立性：RouteLLM依赖外部偏好数据训练的分类器，其性能受限于训练分布与查询语义的对齐；IntroLM利用目标模型自身表示，天然适配模型能力边界，但缺乏跨模型泛化能力。这一差异源于任务特性：RouteLLM面向通用路由，需处理多模型池；IntroLM聚焦单模型自评估，更适合固定模型部署场景。

从评估时机看，IntroLM与Chuang et al. (2025)的置信度token方法形成对比：后者在Decoding末尾评估，需完整生成过程；IntroLM在Prefilling阶段评估，避免生成开销。这一差异源于效率约束：Chuang方法适用于需完整响应的场景，IntroLM适用于路由决策需快速响应的场景。Token-conditional LoRA的通用性未验证，是否适用于非Qwen架构的Transformer，论文未给出回答。

## 总结

IntroLM要解决的核心矛盾是长上下文下外部评估器的上下文限制与计算开销。其切入点在于利用目标模型Prefilling阶段的内部表示，通过[CPX] token与Token-conditional LoRA实现零额外解码开销的自评估。该方法在HOTPOTQA上ROC-AUC达86.3%，较DeBERTa-v3-Large提升14.5个百分点，路由场景下大模型调用率降低50%、延迟降低33%。边界在于：标量预测范式在长上下文下是否仍会导致路由崩溃，论文未提供与EquiRouter等直接决策方法的对比；Token-conditional LoRA的架构通用性未验证。当模型池动态变化时，[CPX] token的LoRA参数能否在线更新以适应新模型能力，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.03511)
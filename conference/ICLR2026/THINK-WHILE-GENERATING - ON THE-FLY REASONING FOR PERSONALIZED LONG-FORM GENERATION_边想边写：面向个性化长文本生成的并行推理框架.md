# ICLR2026最新论文 ｜THINK-WHILE-GENERATING: ON THE-FLY REASONING FOR PERSONALIZED LONG-FORM GENERATION ｜边想边写：面向个性化长文本生成的并行推理框架

研究机构：中国科学技术大学、新加坡国立大学

作者：Chengbing Wang、Yang Zhang、Wenjie Wang 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_72234089)

> 长文本个性化生成面临静态推理无法适应内容动态演化的困境，现有“先想后写”范式因一次性推理难以捕捉用户偏好的实时变化。FlyThinker 通过引入独立的潜在推理模型与生成模型并行运行，实现了 token 级别的动态推理与生成同步。该框架在保持训练与推理效率接近标准微调的同时，显著提升了个性化质量。其价值在于解决了串行推理的效率瓶颈，但并行推理是否牺牲了推理深度仍存疑。

## 研究背景

当 LLM 生成长篇个性化内容时，用户偏好并非静态不变，而是随着已生成内容的展开而动态演化。这种动态性要求模型在生成过程中持续更新对用户意图的理解，而非依赖初始的一次性分析。然而，传统的“先想后写”（Think-then-generate）范式将推理与生成解耦，要求模型在生成前完成全部推理，导致长程依赖难以建模，且无法适应生成过程中的内容变化。

个性化长文本生成旨在使 LLM 输出适配特定用户的风格与偏好，其核心挑战在于隐式偏好的捕捉与长程一致性维持。早期方法依赖检索增强生成（RAG）或微调，但缺乏对隐式偏好的推理机制。近期“先想后写”范式虽引入了推理，但其静态一次性推理在长文本中面临学习困难与适应性不足的问题。FlyThinker 的切入点在于将推理过程从静态前置转为动态并行，通过 token 级别的潜在推理实时指导生成，从而解决长文本中偏好动态演化的捕捉难题。

## 核心方法

### 方法参照系

本文问题属于推理增强生成路线，但与传统串行推理（如 CoT 或 Coconut）的关键差异在于：传统方法中推理与生成存在严格的序列依赖，导致训练与推理效率低下。FlyThinker 通过解耦推理与生成模型，并打破推理 token 间的直接序列依赖，实现了并行计算。

### 并行推理架构

FlyThinker 的核心创新在于引入独立的 Reasoner 模型，仅依赖已生成响应而非自身历史推理，从而打破序列依赖。Reasoner 在每一步生成一个潜在推理 token $r_t$，其计算仅基于查询 $x$ 和已生成响应 $y_{<t}$：

$$ r_t = R_\theta[(\cdot)_{-1}](x, y_{<t}) $$

这一设计使得训练时所有位置的推理 token 可并行计算，无需等待前序推理完成。Generator 模型则融合潜在推理信号与 token 嵌入，通过系数 $\lambda$ 控制推理强度：

$$ p(y_t | y_{<t}, r_{<t}) = G_\phi(f(e(y_t), r_t)) $$

该架构解决了串行推理中训练效率低下的问题，使 FlyThinker 的训练成本接近标准 LLM 微调，同时保留了动态推理的能力。

### 并行推理与生成同步

在推理阶段，FlyThinker 采用交错并行策略：Generator 预测当前 token 时，Reasoner 同步生成下一步的潜在推理。这种设计消除了串行推理中的等待延迟，使推理与生成在时间上重叠。与 Coconut 等串行潜在推理方法相比，FlyThinker 的推理 token 不直接依赖前序推理，仅依赖已生成响应，从而在保持动态推理的同时实现了推理效率的显著提升。这一改进使得 FlyThinker 在长文本生成中能够实时适应内容变化，而无需承受串行推理的效率惩罚。

## 实验评估

实验在 LongLaMP 基准的三个任务（Product Review, Abstract Generation, Topic Writing）上进行，基线覆盖 RAG、SFT、CoT、Coconut 等，但缺失 SPRInG、CARD 等 2026 年 SOTA 方法。主实验结果显示，FlyThinker 在 Product Review 上 ROUGE-1 为 0.3663，较 SFT 提升 3.1%，BLEU 为 4.36，提升 11.5%。在 Abstract Generation 上，FlyThinker BLEU 达 6.34，显著优于 CoT（5.85）和 Coconut（5.23）。

| 方法 | Product Review ROUGE-1 | Product Review BLEU | Abstract Generation BLEU |
|---|---|---|---|
| SFT | 0.3551 | 3.91 | 5.85 |
| CoT | 0.3466 | 3.37 | 5.85 |
| Coconut | 0.3381 | 3.32 | 5.23 |
| FlyThinker | 0.3663 | 4.36 | 6.34 |

消融实验显示，Reasoner 规模对性能影响显著：3B 模型在 Product Review 上 ROUGE-L 最高，而 0.5B 模型性能下降明显。这表明并行推理框架对推理模型的容量敏感，小模型难以有效捕捉隐式偏好。

评估边界方面，论文未报告置信区间，且不同方法可能使用不同骨干网络，公平性需进一步验证。代码未公开，超参数细节有限，可复现性受限。

## 关联研究分析

从问题动机看，FlyThinker 与 SPRInG 均关注长文本个性化，但路线截然不同。SPRInG 采用参数化记忆机制，将偏好固化在权重中，以牺牲灵活性换取长期一致性；FlyThinker 则通过非参数化推理动态捕捉偏好，以推理延迟换取即时适应性。这一差异源于任务特性：SPRInG 假设偏好稳定，适合数据丰富场景；FlyThinker 假设偏好动态，适合内容演化场景。然而，FlyThinker 未对比 SPRInG 等最新参数化 SOTA，其相对优势在长程一致性上是否成立，论文未给出回答。

从方法设计看，FlyThinker 与 Coconut 同属潜在推理路线，但关键差异在于并行性。Coconut 的推理 token 存在序列依赖，导致训练与推理效率低下；FlyThinker 通过解耦 Reasoner 与 Generator，并打破推理 token 间的直接依赖，实现了并行计算。这一改进解决了串行推理的效率瓶颈，但可能牺牲推理深度。FlyThinker 的 Reasoner 仅依赖已生成响应，不显式包含前序推理，这种设计是否导致推理链断裂，论文未提供消融实验验证。

## 总结

FlyThinker 解决了长文本个性化生成中静态推理无法适应内容动态演化的矛盾，通过引入独立 Reasoner 模型实现 token 级别的并行推理与生成同步。该框架在 Product Review 上 ROUGE-1 达 0.3663，BLEU 达 4.36，显著优于 SFT 和 CoT 基线。其边界在于未对比最新参数化 SOTA，且并行推理是否牺牲推理深度未经验证。当 Reasoner 规模缩小至 0.5B 时，性能下降明显，表明并行推理框架对模型容量敏感，小模型能否在保持效率的同时维持推理质量，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_72234089)
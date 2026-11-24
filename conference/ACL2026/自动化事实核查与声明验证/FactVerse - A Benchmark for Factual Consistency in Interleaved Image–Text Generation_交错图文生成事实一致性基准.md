# ACL2026最新论文 ｜FactVerse: A Benchmark for Factual Consistency in Interleaved Image–Text Generation ｜交错图文生成事实一致性基准

作者：Yubo Shan、Kun Zhang、Qiming Xu 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_bcb8d98bb29b)

> 交错图文生成模型常因视觉与文本的语义错位产生看似合理但事实错误的输出，现有评估基准仅关注感知流畅度，无法捕捉实体错配或因果倒置等硬伤。FactVerse 通过构建包含 3,000 个人工验证实例的基准，并提出结合专用判别器、语义锚定 VQA 及规则检查的三维评估框架，填补了该领域在客观事实性验证上的空白。该框架与人类判断的 Kendall’s τ 达 0.78，显著优于通用大模型评估，但其评估有效性目前仅局限于自建数据集，跨基准泛化能力尚待检验。

## 研究背景

当多模态大语言模型（Multimodal Large Language Models, MLLMs）生成包含图像与文本的交错内容时，视觉模态的“眼见为实”认知偏差使得事实错误比纯文本更具误导性。然而，现有评估范式存在根本性错位：主流基准如 OpenLEAF 和 InterleavedBench 依赖 GPT-4V 或 GPT-4o 进行整体打分，侧重语义相关性与视觉流畅度，缺乏针对客观真理的验证机制。这种“感知优先”的评估导致模型被激励去优化连贯性与美学，而非事实准确性，使得危险的事实错误在高分评价中潜藏。

交错图文生成研究沿三条轨迹演进：冻结 LLM 与扩散模型的特征对齐、统一自回归架构，以及集成工具调用的智能体工作流。尽管生成能力显著提升，但评估手段滞后于生成技术，现有基准多面向开放式创意任务，容忍模糊性且无可验证的事实标准。FactVerse 的切入点在于将评估从“主观感知”转向“客观事实”，通过引入基于 Ground Truth 的锚定机制，解决现有方法在科学教育、医疗指南等高利害领域中无法保证事实真实性的核心矛盾。

## 核心方法

### 评估框架参照系

传统多模态生成评估依赖单模态指标（如 BLEU、FID）或 CLIPScore 等对齐指标，近期转向 LLM-as-a-Judge 范式。本文问题与通用流程的关键差异在于：通用流程缺乏可验证的事实标准（Ground Truth），而 FactVerse 要求评估必须锚定在专家构建的客观真理上，将主观视觉评估转化为可量化的事实核查任务。

### 专用事实判别器（FactJudge）

针对通用模型难以检测细微视觉-文本差异的问题，FactVerse 在 Qwen3-VL-8B 基础上微调了 FactJudge。其核心创新在于采用“Reasoning-then-Scoring”范式，强制模型先分析具体差异的逻辑理由，再给出归一化分数。该设计解决了通用 LLM 在整体评分中“幻觉盲视”的问题，即模型可能因整体连贯而忽略局部事实错误。

$$
\text{Score} = f_{\text{judge}}(\text{Rationale}, \text{Input}) \quad \text{where Rationale} = g_{\text{reason}}(\text{Discrepancies})
$$

此公式表明，最终分数并非直接由输入映射得出，而是依赖于对事实差异（Discrepancies）的逻辑推理过程，确保评分基于事实分析而非表面相似度。

### 语义锚定 VQA 与规则化检查

FactJudge 处理语义层面的事实一致性，而语义锚定 VQA（Semantically Anchored VQA）与规则化检查负责量化可验证的组件。VQA 模块将关键事实约束（如物体属性、空间关系）转化为精确的问答对，VQA 模型作为客观验证器，检查生成视觉内容是否严格符合专家构建的标准答案。规则化检查则通过确定性解析器验证结构合规性，如图像数量是否与指令一致。

$$
\text{SAS} = \frac{1}{N} \sum_{i=1}^{N} \mathbb{1}[\text{VQA}(v_i, q_i) = a_i^{\text{GT}}]
$$

其中 SAS（Semantic Anchoring Score）为原子视觉事实的验证通过率，$v_i$ 为生成图像，$q_i$ 为锚定问题，$a_i^{\text{GT}}$ 为 Ground Truth 答案。该公式将主观视觉评估转化为二元事实核查，显著降低了评估方差。

## 实验评估

实验在自建 FactVerse 基准上进行，包含 3,000 个实例（2,000 英文，1,000 中文），覆盖 24 个子任务和 50 个领域。基线涵盖三类模型：统一模型（如 Anole, Show-o）、复合系统（如 GPT-4o + DALL·E 3）及工具增强智能体（如 GPT-5）。评估协议采用 FactVerse 框架与人类标注进行对齐度比较，核心指标为 Kendall’s τ。

| 评估方法 | Kendall’s τ vs Human | 备注 |
| :--- | :--- | :--- |
| FactVerse (Full) | 0.78 | 完整框架 |
| w/o VQA Verification | 0.67 | 移除 SAS 模块 |
| w/o FactJudge | 0.42 | 仅保留规则与 VQA |
| GPT-4o (Holistic) | < 0.78 | 通用 LLM 整体评估 |

消融实验显示，FactJudge 是框架中最关键的组件，移除后 τ 从 0.78 骤降至 0.42，表明专用判别器在捕捉细微事实错误上不可替代。VQA 验证模块移除后 τ 降至 0.67，说明语义锚定对视觉事实核查有显著贡献。规则化检查移除影响较小（τ 0.75），主要因结构错误在生成中相对少见。

评估边界方面，FactVerse 仅验证了框架与人类判断的对齐度，未提供跨基准的泛化性能数据。代码与超参数未公开，可复现性受限。此外，3,000 个实例的规模可能不足以覆盖所有长尾领域，且人工验证成本高昂，限制了数据集的扩展性。

## 关联研究分析

从问题动机看，FactVerse 与 OpenLEAF 和 InterleavedBench 的根本差异在于评估目标的错位。OpenLEAF 利用 GPT-4V 评估实体与风格一致性，InterleavedBench 侧重感知保真度，二者均将“事实性”隐含于“连贯性”中，缺乏独立的客观真理锚点。FactVerse 通过引入专家构建的 Ground Truth 和专用判别器，将事实性从感知质量中剥离，解决了高利害领域中“看似合理但事实错误”的隐蔽风险。这一差异源于任务特性：创意生成容忍模糊，而科学/医疗生成要求零容忍的事实准确性。

从方法设计看，FactVerse 的语义锚定 VQA 与 TIFA 的 VQA 评估范式同源，但 FactVerse 引入了“锚定”机制，将开放式的视觉解释转化为基于 Ground Truth 的精确问答。TIFA 依赖 VQA 模型的主观判断，而 FactVerse 通过专家构建的 QA 对消除了主观偏差。这一改进解决了 TIFA 在科学验证中精度不足的问题，但代价是评估过程依赖高质量的人工标注，限制了其在无标注场景下的适用性。

## 总结

FactVerse 旨在解决交错图文生成中事实错误隐蔽且现有评估无法捕捉的核心矛盾。其切入点在于将评估从主观感知转向客观事实，通过构建人工验证基准与专用判别器，实现了对细粒度事实一致性的量化。实验证明，FactVerse 框架与人类判断的对齐度（Kendall’s τ 0.78）显著优于通用 LLM 评估，且 FactJudge 模块对性能贡献最大。然而，该框架的有效性目前仅局限于自建数据集，缺乏跨基准泛化验证，且人工验证成本限制了数据规模扩展。当 FactJudge 作为奖励信号用于强化学习生成框架时，其评估偏差是否会反向引导模型优化方向，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_bcb8d98bb29b)
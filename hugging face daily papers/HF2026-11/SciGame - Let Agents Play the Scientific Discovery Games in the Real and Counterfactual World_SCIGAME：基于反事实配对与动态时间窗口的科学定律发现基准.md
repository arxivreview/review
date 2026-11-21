# HuggingFace最新推荐论文 ｜SciGame: Let Agents Play the Scientific Discovery Games in the Real and Counterfactual World ｜SCIGAME：基于反事实配对与动态时间窗口的科学定律发现基准

研究机构：加拿大麦吉尔大学

作者：Yusheng Zhao、Bowei He、Xue Liu 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2610.37919)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2610.37919)

> 导读：LLM 在科学发现中常依赖预训练先验而非实证证据，导致在反事实场景下推理失效。现有基准多混合编程与定律推断，且静态数据易受模型知识截止日期的污染，无法有效分离先验与证据。SCIGAME 通过构建 Original 与 Counterfactual 配对环境及动态 Temporal 数据管道，在受控条件下评估 Agent 的假设生成与实验设计能力。该基准揭示了熟悉先验在反事实任务中的负面作用及自适应实验对模型能力的依赖性，为评估科学推理的鲁棒性提供了关键工具，但其对非结构化复杂系统的覆盖仍存疑。

## 研究背景

当 LLM 被用于科学定律发现时，其核心困境在于难以区分“基于物理直觉的推导”与“基于训练数据的模式匹配”。在标准物理定律（Original）任务中，模型往往能凭借预训练知识直接给出正确答案，掩盖了其推理能力的真实水平。一旦引入维度一致但形式改变的反事实定律（Counterfactual），若模型仍依赖先验，便会给出错误预测。这种先验与证据的冲突，要求评估框架必须能够强制模型依据观测数据修正假设，而非依赖记忆。

当前科学发现基准存在显著缺陷：任务定义常将定律推断与代码实现、论文复现混合，导致无法隔离推理能力；评估指标多关注数据拟合精度，缺乏对未见输入泛化能力的测试；且基准多为静态，难以规避模型知识截止日期后的数据污染。SCIGAME 针对这些痛点，提出了一种受控评估框架，通过配对环境与动态时间窗口，专门测试 Agent 在证据与先验冲突时的适应能力及长程实验设计的鲁棒性。

## 核心方法

### 方法参照系：受控环境下的假设-实验闭环

SCIGAME 将科学定律发现建模为 Agent 在确定性模拟器中的交互过程。与通用科学问答或代码生成任务不同，该框架严格分离了“定律推断”与“其他科研技能”。Agent（Player）面对一个隐藏关系的模拟器（Oracle），需通过提出实验、接收观测、更新假设，最终提交可执行表达式与科学解释。这一流程对应了科学发现中的假设生成、实验设计与结论推导环节，其关键差异在于引入了“反事实”变量以打破先验依赖，并区分了候选引导（Identification）与开放式发现（Discovery）两种设置。

### 反事实配对环境构建

为强制分离先验与证据，SCIGAME 为每个科学家族构建 Original 与 Counterfactual 两个配对环境。Original 环境实现源文献中的标准关系，Counterfactual 环境则对关系进行维度一致的结构性突变（如改变系数、指数或引入非线性变换）。两个环境共享相同的输入域、观测变量及实验约束，仅生成观测值的底层关系不同。

在 Identification 设置中，Agent 接收一个由未知参数 $s$ 插值的候选公式：

$$ G_r(x; s) = (1 - s) g_r(x) + s g'_r(x) $$

其中 $g_r(x)$ 为 Original 表达式，$g'_r(x)$ 为 Counterfactual 表达式。Agent 需通过实验确定 $s$ 的值（0 或 1），从而识别主导关系。这一设计动机在于，若 Agent 仅依赖先验，在 Counterfactual 环境中将因无法识别突变而失败，从而暴露其推理对证据的依赖程度。

### 动态时间窗口与多协议评估

为解决数据污染问题，SCIGAME 引入 Temporal 集合，其数据源来自模型知识截止日期之后发表的论文。通过可重跑的策展管道，提取近期文献中的定量关系，确保评估任务对模型而言是“未知”的。

评估框架包含三种协议：Prior-only（无观测，仅凭先验）、Fixed（固定预算的预设观测）与 Adaptive（自适应实验设计）。在 Adaptive 协议中，Agent 逐步向 Oracle 提出实验，Oracle 返回观测或约束反馈。Agent 需维护至少两个假设及其置信度，直至最高置信度超过阈值 $\tau$ 或提交最终结果。该设计旨在评估 Agent 在长程交互中的规划能力与错误修正能力，特别是当初始假设错误时，能否通过后续实验有效纠偏。

## 实验评估

实验在 Historical 与 Temporal 两个集合上进行，评估 GPT-5.5、GPT-6 Astra 等前沿模型。主要指标包括严格标准下的剧集成功率（ESR）、隐藏输入上的预测得分（PS）及科学解释得分（SES）。

| 模型 | 协议 | 集合 | 设置 | 环境 | ESR (%) | PS | SES |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| GPT-6 Astra | Adaptive | Temporal | Discovery | Original | 63.3 | 0.996 | 0.980 |
| GPT-6 Astra | Adaptive | Temporal | Discovery | Counterfactual | 13.9 | 0.792 | 0.856 |
| GPT-5.5 | Adaptive | Temporal | Discovery | Original | 21.7 | 0.366 | 0.670 |
| GPT-5.5 | Adaptive | Temporal | Discovery | Counterfactual | 0.0 | 0.079 | 0.462 |

数据显示，熟悉先验在 Original 环境中提升性能，但在 Counterfactual 环境中显著损害性能。GPT-6 Astra 在 Temporal Discovery Counterfactual 中的 ESR 仅为 13.9%，远低于 Original 环境的 63.3%。这表明即使是最强模型，在面对与先验冲突的证据时，仍难以完全摆脱先验干扰。

消融分析显示，Adaptive 协议对强模型有益，但对弱模型可能有害。在 Counterfactual Discovery 中，GPT-6 Astra 的 Adaptive ESR 为 13.9%，而 Fixed 协议下为 11.1%，提升有限；相比之下，GPT-5.5 在 Adaptive 下 ESR 为 0.0%，低于 Fixed 的 0.0%（注：原文数据中 GPT-5.5 Fixed Counterfactual Discovery ESR 为 0.0，Adaptive 为 0.0，但文中提到 Adaptive 帮助强模型伤害弱模型，此处需结合预算分析）。进一步分析发现，在预算 $B=8$ 时，Fixed 协议在 Counterfactual Discovery 中的成功率为 47.2%-65.3%，而 Adaptive 仅为 27.8%-34.7%。这表明自适应实验存在冷启动问题，前两步成功率接近零，需更多交互步数才能收敛。

评估边界方面，SCIGAME 仅覆盖文本模态，未验证多模态输入对反事实推理的缓解作用。此外，解释得分与预测成功存在脱节，GPT-5.6 Terra 在 Temporal Counterfactual Discovery 中 SES 高达 0.815，但 ESR 仅为 1.4%，说明模型能生成看似合理的解释，却无法恢复正确的符号形式。

## 关联研究分析

从问题动机看，SCIGAME 与 NewtonBench 均关注反事实推理，但 NewtonBench 主要测试模型在改变物理定律下的问答能力，未涉及主动实验设计。SCIGAME 通过 Adaptive 协议，将评估重心从“静态推理”转向“动态调查”，更贴近真实科研中假设-实验的迭代过程。然而，SCIGAME 的 Counterfactual 突变仍基于合成规则，是否足以模拟真实科学发现中非结构化、高噪声的复杂性，尚待验证。

从方法设计看，SCIGAME 与 LLM-SRBench 形成互补。LLM-SRBench 侧重从数据中恢复公式的精度，属于符号回归范畴；SCIGAME 侧重假设生成与实验选择的推理过程。SCIGAME 未采用 PySR 等传统符号回归算法作为基线，而是聚焦于 LLM Agent 的端到端能力。这种设计选择反映了领域从“算法拟合”向“智能体推理”的范式转移，但也导致无法直接对比 LLM 与传统符号回归在纯公式恢复任务上的优劣。

## 总结

SCIGAME 针对 LLM 在科学发现中先验依赖与数据污染问题，构建了包含反事实配对环境与动态时间窗口的受控基准。通过 Prior-only、Fixed 与 Adaptive 三种协议，该基准量化了模型在证据与先验冲突时的适应能力。实验表明，GPT-6 Astra 在 Temporal Counterfactual Discovery 中的 ESR 仅为 13.9%，揭示了熟悉先验在反事实场景下的负面作用及自适应实验对模型能力的强依赖性。该基准的局限在于仅覆盖文本模态与合成突变，未验证多模态输入或真实实验室噪声下的表现。当支持集增大到 5-shot 时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2610.37919)
# ACL-Findings2026最新论文 ｜OmniCode: A Benchmark for Evaluating Software Development Agents ｜全生命周期软件工程智能体基准

研究机构：美国康奈尔大学、美国纽约大学

作者：Atharv Sonwane、Eng-Shen Tu、Wei-Chung Lu 等 14 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a20366a07501)

> 现有代码智能体基准聚焦于单一补丁生成任务，无法评估模型在测试编写、代码审查响应及风格合规等真实开发环节的综合能力。本文通过合成负样本与多任务扩展，构建覆盖Python、Java、C++三语言的1794项任务基准，揭示当前SOTA模型在非Python语言及测试生成上的显著短板。其价值在于暴露了单一指标评估的盲区，但$2/instance的成本约束可能低估高复杂度任务的真实性能。

## 研究背景

当智能体生成的补丁通过单元测试时，传统基准即判定任务成功。然而，这种“执行接地”验证存在盲区：生成的测试可能仅捕获表面行为，无法区分正确逻辑与细微错误实现。为量化这一偏差，需引入“坏补丁”（Bad Patches）作为负样本，要求测试在金补丁上通过且在所有坏补丁上失败，从而提升验证信号的判别力。

仓库级Issue修复是软件工程智能体的核心任务，SWE-bench确立了以执行反馈为黄金标准的评估范式。然而，该范式局限于Bug-Fixing单一任务，且主要覆盖Python语言，无法反映真实开发中测试生成、代码审查及风格维护的复杂性。现有基准如Multi-SWE-Bench虽扩展至多语言，但仍限于缺陷修复。本文切入点在于将评估范围从“修复Bug”扩展至“全生命周期任务”，并通过合成数据解决真实负样本稀缺问题，以揭示模型在复杂工程场景下的真实能力边界。

## 核心方法

### 基准构建参照系

本文基于SWE-bench-Verified与Multi-SWE-Bench的实例，通过任务特定增强生成四类任务。与标准Bug-Fixing流程不同，本文引入复合复杂度指标量化任务难度，并针对测试生成与审查任务构建对抗性评估环境。

### 坏补丁生成与测试判别

测试生成任务的核心挑战在于避免“空洞测试”（Vacuous Tests）通过。传统方法仅验证测试在金补丁上的通过性，本文引入坏补丁机制，要求测试具备区分正确与错误实现的能力。坏补丁通过Agentless等模型的失败轨迹及LLM扰动生成，确保其“看似合理但实际错误”。测试成功判据定义为：

$$
\text{Success} = \mathbb{1}[\text{Pass}(\text{Gold})] \land \bigwedge_{i=1}^{N} \mathbb{1}[\text{Fail}(\text{Bad}_i)]
$$

该公式表明，测试必须同时满足金补丁通过且所有坏补丁失败，从而强制模型理解程序语义而非表面行为。

### 多任务评估协议

为评估代码审查响应能力，本文利用Gemini-2.5-Flash基于坏补丁与金补丁生成审查指令，要求智能体根据反馈修正错误实现。风格修复任务则通过pylint、clang-tidy等工具生成违规列表，智能体需在不破坏功能的前提下修复风格问题。风格修复得分定义为：

$$
\text{Score} = \begin{cases} \max\left(\frac{\text{Resolved} - \text{New}}{\text{Original}}, 0\right), & \text{if all tests pass} \\ 0, & \text{otherwise} \end{cases}
$$

该公式惩罚新引入的错误，确保风格修复不牺牲功能正确性，反映真实工程中对代码质量与稳定性的双重约束。

## 实验评估

实验采用SWE-Agent与Aider两种框架，搭配Gemini-2.5-Flash、Claude-4.6-Sonnet等五款SOTA模型。基线覆盖Agentic与Pipeline两种范式，但缺乏RL-based或Memory-augmented基线，可能低估特定架构的优势。

| 任务 | 语言 | 最佳模型 | 准确率 (%) |
|---|---|---|---|
| Bug-Fixing | Python | Claude-4.6-Sonnet | 68.9 |
| Bug-Fixing | Java | DeepSeek-V3.1 | 31.2 |
| Bug-Fixing | C++ | DeepSeek-V3.1 | 19.6 |
| Test Generation | C++ | DeepSeek-V3.1 | 25.0 |
| Review-Response | Python | Claude-4.6-Sonnet | 67.9 |
| Style-Fixing | Python | Claude-4.6-Sonnet | 61.2 |

Bug-Fixing在Python上表现最佳（68.9%），但在C++上骤降至19.6%，揭示语言泛化瓶颈。测试生成是最大短板，最高仅25.0%，表明模型难以生成具备判别力的测试。

消融分析显示，仅依赖金补丁评估会高估测试能力：Qwen C++从4.5%升至22.7%，DeepSeek C++从25%升至43.8%。这一差距证实坏补丁机制对评估鲁棒性的关键作用。此外，Review-Response在Java上唯一解决15个实例，高于Bug-Fixing的4个，表明审查反馈能引导模型聚焦关键错误。

评估边界受限于$2/instance成本约束，Claude-4.6-Sonnet在Java/C++上因预算耗尽被计为未解决，可能低估其真实能力。代码开源，但坏补丁生成依赖特定模型组合，复现时需确保负样本多样性。

## 关联研究分析

从问题动机看，OmniCode与SWE-bench-Verified同属执行接地验证范式，但后者仅评估补丁功能正确性，而本文通过坏补丁机制引入“判别性”维度。这一差异源于任务特性：测试生成需区分正确与错误实现，而非仅验证通过性。SWE-bench未探索此维度，因其聚焦Bug-Fixing，而测试生成是独立能力。

从方法设计看，OmniCode与Multi-SWE-Bench同属多语言基准，但后者限于Bug-Fixing，本文扩展至全生命周期任务。这一扩展揭示了模型在非Python语言上的性能断崖，挑战了“Python主导”的评估惯例。Multi-SWE-Bench未涉及测试生成与审查，因其数据源仅包含PR修复，而本文通过合成数据构建新任务类型，填补了评估空白。

## 总结

本文核心矛盾在于现有基准无法评估智能体在测试生成、代码审查等真实开发环节的能力。通过合成坏补丁与多任务扩展，OmniCode揭示了SOTA模型在非Python语言及测试生成上的显著短板，如C++ Bug-Fixing仅19.6%、测试生成最高25.0%。其边界在于$2/instance成本约束可能低估高复杂度任务性能，且坏补丁生成依赖特定模型组合。当成本约束放宽时，Claude-4.6-Sonnet在Java/C++上的真实能力是否接近Python水平，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_a20366a07501)
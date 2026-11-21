# ACL-Findings2026最新论文 ｜SolidCoder: Bridging the Mental-Reality Gap in LLM Code Generation through Concrete Execution ｜弥合心理-现实鸿沟：基于具体执行的代码生成框架

研究机构：韩国电子通信研究院

作者：Woojin Lee、Jin-Xia Huang

论文原文见 [arXiv](https://arxiv.org/abs/2604.19825)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.19825)

> 多智能体代码生成框架依赖大语言模型（LLM）内部的心理模拟来验证代码正确性，但模型常因幻觉而自信地通过有缺陷的代码。本文指出这一“心理-现实鸿沟”源于规划阶段的边界盲区与验证阶段的执行幻觉，并提出了 SolidCoder 框架。该框架通过前置边界识别与沙箱具体执行，将验证从“想象”转变为“运行”。这一转变在中等难度竞赛编程任务上带来了显著的性能提升，但其高昂的推理成本与对属性断言生成能力的依赖，限制了其在极端复杂或简单任务上的普适性。

## 研究背景

当 LLM 生成复杂算法代码时，其内部推理过程往往与真实运行时行为脱节。这种脱节被称为“心理-现实鸿沟”（Mental-Reality Gap），它由两个正交维度构成：规划阶段忽略边界情况导致的“规格鸿沟”（Specification Gap），以及验证阶段 LLM 幻觉出正确执行轨迹导致的“验证鸿沟”（Verification Gap）。解决这一问题的关键在于引入外部执行反馈，但传统调试器依赖 Ground Truth 测试用例，而在新型算法问题中，正确输出正是待求解的目标，这构成了“缺失 Oracle”（Missing Oracle）难题。

现有主流路线如 CodeSIM（Islam et al., 2025）虽采用多智能体架构，但依赖 LLM 心理模拟进行验证，导致模型在复杂逻辑中“自欺欺人”。早期尝试通过自一致性生成测试用例以解决 Oracle 问题，但 CodeSIM 实验表明这反而导致 9.3% 的性能下降。本文的切入点在于重新定义验证机制：不预测精确输出，而是通过属性断言（Property-based Assertions）检查代码是否满足领域不变量，从而在无需 Ground Truth 的情况下实现闭环验证。

## 核心方法

### 多智能体验证参照系

本文基于 CodeSIM 的规划-编码-调试三智能体架构。该通用流程中，验证环节通常由 LLM 通过文本追踪（Mental Simulation）完成，其核心缺陷在于状态追踪随代码复杂度增加而指数级易错，且无法回溯早期决策错误。本文的关键差异在于将验证环节从“内部推理”替换为“外部执行”，并引入属性断言解决 Oracle 缺失问题。

### 属性断言与具体执行

针对缺失 Oracle 问题，本文提出 Oracle-based Assertions（O）。设计动机在于，CodeSIM 尝试预测精确 I/O 失败，而属性验证只需检查不变量（如“输出长度等于输入长度”）。验证逻辑可形式化为：

$$
\text{Pass}(c, x) = \bigwedge_{p \in P(c)} \text{Check}(p, \text{Exec}(c, x))
$$

其中 $P(c)$ 为代码 $c$ 的属性集合，$\text{Exec}(c, x)$ 为沙箱执行结果。该公式表明，正确性判定不依赖精确值匹配，而是依赖属性满足度，从而规避了 LLM 预测输出的幻觉风险。

### 防御性累积与左移规划

针对迭代调试中的回归风险，本文引入 Defensive Accumulation（D）。每次 Live Execution 发现失败测试，该输入-断言对即加入累积测试集 $T_{acc}$。代码修改后必须通过所有 $T_{acc}$ 测试，确保单调性：

$$
\text{Accept}(c') \iff \forall t \in T_{acc}, \text{Pass}(c', t)
$$

同时，Shift-left Planning（S）在规划前强制识别边界情况，将“最坏情况输入”纳入规划提示，从源头减少规格鸿沟。

## 实验评估

实验在 HumanEval、CodeContests 和 APPS 三个基准上进行，对比 Direct、CoT、MapCoder 和 CodeSIM 等基线。基线覆盖多智能体与提示工程路线，但未包含最新的非自回归架构（如 AnCoder）或纯数据合成方法。

| 模型 | 基准 | CodeSIM | SolidCoder | 提升 |
| :--- | :--- | :--- | :--- | :--- |
| GPT-4o | HumanEval | 95.1 | 95.7 | +0.6%p |
| GPT-4o | CodeContests | 72.7 | 77.0 | +4.3%p |
| GPT-4o | APPS | 23.3 | 26.7 | +3.4%p |
| Grok-4.1-Fast | CodeContests | 95.2 | 98.2 | +3.0%p |

SolidCoder 在 CodeContests 上提升最显著，表明中等难度任务处于“心理模拟失效但执行验证有效”的甜蜜点。HumanEval 因基准饱和，提升微弱；APPS 因生成瓶颈主导，验证收益受限。

| 消融配置 (GPT-4o, CodeContests) | Pass@1 | 降幅 |
| :--- | :--- | :--- |
| Full SolidCoder | 77.0 | - |
| w/o Shift-left Planning | 53.3 | -23.7%p |
| w/o Live Execution | 69.1 | -7.9%p |
| w/o Oracle-based Assertions | 65.4 | -11.6%p |

消融显示，Shift-left Planning 贡献最大，证实边界盲区是主要失效模式。Live Execution 虽降幅较小，但捕获的是规格改进无法解决的“验证幻觉”错误，两者具有互补性而非替代性。

评估边界方面，论文未报告计算效率的详细对比（仅提及 Token 开销增加 50%-97%），且未测试 Gemini 或 Claude 等模型。代码已开源，但属性断言的生成依赖 LLM 自身能力，存在自证循环风险，论文未对此进行隔离实验。

## 关联研究分析

从验证机制看，SolidCoder 与 LDB（Zhong et al., 2024）和 MGDebugger（Shi et al., 2024）均利用执行反馈，但后者作为“第二遍”调试器，依赖 Ground Truth 测试用例。SolidCoder 将执行内嵌至生成循环，并通过属性断言解决 Oracle 缺失，实现了自主验证。这一差异源于任务特性：竞赛编程问题往往缺乏预定义测试集，而传统调试场景通常有明确输入输出。

从架构演进看，SolidCoder 与 CollabCoder（ACL-Findings 2026）同属多智能体路线，但 CollabCoder 侧重计划-代码协同进化，而 SolidCoder 聚焦验证环节的具身化。CollabCoder 在 HumanEval 上达到 96.34%，略高于 SolidCoder 的 95.7%，这可能源于其更复杂的规划机制，但 SolidCoder 在 CodeContests 上持平 SOTA，表明执行验证在中等难度任务上的有效性。属性断言的生成是否依赖 LLM 的领域知识深度，论文未给出回答。

## 总结

SolidCoder 针对多智能体代码生成中的心理-现实鸿沟，通过属性断言与具体执行解决了缺失 Oracle 下的验证难题。其核心贡献在于将验证从 LLM 内部推理外化为沙箱执行，并在 CodeContests 上实现 77.0% 的 Pass@1。然而，该框架在 HumanEval 上收益微弱，且在 APPS 上受限于生成瓶颈，表明执行验证并非万能解。当任务难度极高导致生成本身失败时，验证环节的改进是否仍能带来边际收益，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.19825)
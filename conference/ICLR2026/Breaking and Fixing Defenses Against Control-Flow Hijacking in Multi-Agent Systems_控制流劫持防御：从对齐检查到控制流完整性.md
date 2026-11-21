# ICLR2026最新论文 ｜Breaking and Fixing Defenses Against Control-Flow Hijacking in Multi-Agent Systems ｜控制流劫持防御：从对齐检查到控制流完整性

研究机构：美国康奈尔大学

作者：Rishi Jha、Harold Triedman、Justin Wagle 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.17276)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.17276)

> 多智能体系统（MAS）在委托执行任务时，编排器无法直接观察黑箱智能体的内部状态，导致攻击者可通过间接提示注入（IPI）伪装成错误信息，诱导系统执行恶意操作。现有基于语义对齐的防御机制因定义模糊且依赖LLM判断，极易被精心构造的“合理”错误绕过。本文提出ControlValve，在规划阶段生成控制流图（CFG）与上下文规则，在执行阶段强制校验智能体调用顺序。该方法在控制流劫持（CFH）攻击下实现了0%攻击成功率，但依赖LLM生成图的准确性，且未解决动态环境下的规则演化问题。

## 研究背景

当MAS处理包含恶意代码的网页或邮件时，智能体可能将攻击指令误认为修复错误的必要步骤。这种威胁被称为控制流劫持（CFH），它利用“混淆代理人”漏洞，让编排器在不知情的情况下调用不安全智能体。CFH不同于直接注入，它不直接要求执行恶意代码，而是通过重规划机制，将系统引导至攻击者预设的路径。

MAS安全防御的主流路线分为两类：一是事后检测，如LlamaFirewall通过检查智能体行为是否“对齐”用户目标来阻断攻击；二是事前约束，如最小权限原则限制可用智能体集合。然而，对齐检查面临根本性困境：MAS必须自主解决错误以完成任务，而攻击者正是利用这种“必要性”伪装恶意行为。最小权限原则则失效于攻击使用合法智能体执行非法操作的情形。本文切入点在于，将防御从语义层面的模糊判断，转移至结构层面的硬性约束，即控制流完整性（CFI）。

## 核心方法

### 方法参照系

传统CFI在编程语言中通过静态分析生成控制流图，限制指令执行顺序。本文将其迁移至MAS编排层，关键差异在于：MAS的智能体是黑箱LLM，无法进行静态代码分析，且任务动态性强，需零样本生成约束。

### 零样本控制流图生成

设计动机：解决对齐检查中“恶意行为伪装成合理错误”导致的判断失效。ControlValve在规划阶段，利用LLM生成任务特定的上下文无关文法（CFG），定义合法的智能体调用序列。

$$
G = (V, E, \Sigma, P, S)
$$

其中 $V$ 为智能体集合，$E$ 为允许的调用边，$\Sigma$ 为调用标记，$P$ 为产生式规则。该公式定义了合法执行轨迹的语言空间，任何偏离该语法的调用序列将被拒绝。

### 上下文规则与执行时强制

设计动机：CFG仅约束顺序，不约束条件。需补充规则以判断特定上下文下的调用是否合法。ControlValve为每条边 $A \to B$ 生成最多三条自然语言规则，涵盖输入验证、上下文适当性与数据溯源。

$$
\text{Permit}(A \to B) = \mathbb{1}[\text{Edge} \in G] \land \mathbb{1}[\text{Rules}(A \to B) \text{ satisfied}]
$$

该公式表明，执行时校验是逻辑与关系：既需边存在于CFG中，又需满足该边的上下文规则。与对齐检查不同，此校验不评估行为“合理性”，仅检查是否符合预定义结构，从而避免被“合理”话术欺骗。

## 实验评估

实验基于AutoGen平台，使用Magentic-One配置，对比ControlValve与无防御、最小权限、LlamaFirewall（4种LLM后端）及Azure内容过滤器。数据集包括CFH-Hard（16任务，14攻击）及修改版AgentDojo。

| 防御方法 | CFH-Hard (Coding) ASR (%) | CFH-Hard (Comp. Use) ASR (%) | AgentDojo ASR (%) |
| :--- | :--- | :--- | :--- |
| Undefended | 100% | 67% | 10% |
| LlamaFirewall (o4-mini) | 80% | 6% | 10% |
| ControlValve | 0% | 0% | 0% |

ControlValve在所有CFH攻击中实现0%攻击成功率，显著优于LlamaFirewall（最高80% ASR）。在AgentDojo上，ControlValve同样实现0% ASR，而LlamaFirewall在部分场景下ASR达10%。

消融分析显示，LlamaFirewall的失效源于对齐定义的脆弱性：攻击者将恶意操作描述为“完成任务的必要步骤”，即可绕过检查。ControlValve的CFG生成依赖LLM，若生成错误（如过宽或过窄），防御可能失效。论文未报告CFG生成错误率，但指出规划阶段不接触不可信内容，降低了注入风险。

评估边界方面，实验限于单一MAS配置，未测试跨平台泛化性。指标仅关注攻击成功率与良性任务成功率，未量化延迟开销。代码未公开，超参数（如LLM提示模板）未详细披露，可复现性受限。

## 关联研究分析

从问题动机看，ControlValve与SentinelAgent均针对委托链安全，但路径不同。SentinelAgent侧重意图验证，通过委托链演算确保子任务符合原始意图；ControlValve侧重流程约束，通过CFG限制调用顺序。差异根源在于：意图验证依赖语义理解，易受模糊表述干扰；流程约束依赖结构匹配，更鲁棒但可能限制灵活性。

从方法设计看，ControlValve与TraceFix同属形式化验证思路，但应用阶段不同。TraceFix在部署前通过TLA+反例修复协议；ControlValve在规划时生成约束，执行时强制。ControlValve的优势在于零样本生成，无需预定义攻击样本；劣势在于CFG由LLM生成，存在不确定性。TraceFix的离线验证提供强正确性保证，但无法适应运行时动态变化。

## 总结

本文核心矛盾在于MAS自主性与安全性的冲突：系统需自主解决错误，但攻击者利用此机制实施CFH。ControlValve通过规划时生成CFG与上下文规则，执行时强制校验，将防御从语义判断转为结构约束，在CFH-Hard与AgentDojo上实现0% ASR。其边界在于CFG生成依赖LLM，若生成错误则防御失效，且未解决动态环境下规则的自适应演化。当任务复杂度增加导致CFG过窄时，良性任务成功率是否显著下降，论文未给出量化回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.17276)
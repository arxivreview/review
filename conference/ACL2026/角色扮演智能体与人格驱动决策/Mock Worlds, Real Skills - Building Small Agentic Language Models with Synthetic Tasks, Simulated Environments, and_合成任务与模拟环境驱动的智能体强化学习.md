# ACL2026最新论文 ｜Mock Worlds, Real Skills: Building Small Agentic Language Models with Synthetic Tasks, Simulated Environments, and Rubric-Based Rewards ｜合成任务与模拟环境驱动的智能体强化学习

研究机构：中国科学技术大学

作者：Yuanjie Lyu、Chengyu Wang、Lei Shen 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_22edf57ccb76)

> 现有开源智能体训练数据任务单一且易解，真实API环境昂贵且不稳定，导致强化学习（RL）信号微弱。SYNTHAGENT通过合成多样化工具使用任务并构建LLM模拟的Mock环境，解决了数据与环境的双重瓶颈。其核心在于引入信息缺口强制智能体主动查询，并基于执行轨迹构建可验证的Rubric奖励。该方法使8B-14B小模型在多个智能体基准上超越部分更大基线，但Mock环境的稳定性是否足以替代真实API的复杂错误模式仍存疑。

## 研究背景

当LLM智能体执行长程工具调用任务时，若初始指令未包含关键决策细节，模型往往陷入盲目尝试或幻觉。这种不确定性源于指令信息熵过高，导致策略梯度退化。为缓解此问题，需引入外部交互获取隐藏上下文，但这要求环境能稳定响应智能体的查询。

智能体RL训练长期受限于数据与环境的双重瓶颈。主流路线依赖开源数据集（如ToolStar）或真实API，前者任务类型狭窄（多为搜索与数学），后者成本高且响应不稳定，导致RL rollout中轨迹同质化，优势估计方差大。SYNTHAGENT的切入点在于将数据生成与环境构建解耦：通过Persona Hub生成多样化任务背景，利用LLM模拟工具与用户，从而在本地低成本环境下实现大规模、稳定的RL训练。

## 核心方法

### 方法参照系

本文问题属于智能体RL训练中的数据与环境设计范畴。通用流程为：生成任务→构建环境→执行RL。关键差异在于，本文不依赖真实API或静态数据集，而是完全由LLM合成任务、工具接口及用户响应，形成闭环的虚拟训练场。

### 信息缺口注入与模糊任务生成

传统任务生成直接基于工作流，导致指令过指定，智能体只需机械执行，策略分布近确定性，RL信号微弱。SYNTHAGENT将任务初始状态 $s_0$ 分解为智能体可见指令 $I$ 与用户私有上下文 $C$，满足 $H(a^*|I) \gg \epsilon$。

$$
s_0 \rightarrow (I, C), \quad H(a^*|I) \gg \epsilon
$$

该设计强制智能体在调用工具前必须先查询用户以获取 $C$，使早期决策非平凡，避免策略 $\pi_\theta(\cdot|s_t)$ 退化，从而保证RL训练中的梯度信号有效。

### 任务级有限映射与Rubric奖励

LLM模拟工具时，相同状态与动作可能产生不同响应，破坏RL稳定性。SYNTHAGENT引入任务级有限映射 $M = \{(u_i, y_i)\}_{i=1}^M$，其中 $u_i$ 为工具调用，$y_i$ 为响应。新调用通过查询 $M$ 确保一致性。

$$
M = \{(u_i, y_i)\}_{i=1}^M, \quad u_i = (tool_i, args_i)
$$

奖励设计避免主观LLM评分，基于工作流提取子目标与禁止行为，构建Rubric。奖励函数定义为：

$$
R(\tau) = I(\tau) \cdot \frac{N_{subgoals}(\tau) + I_{user\_query}(\tau)}{2}
$$

其中 $I(\tau)$ 为违反禁止行为时的零奖励指示器，$N_{subgoals}$ 为完成子目标比例，$I_{user\_query}$ 为满足用户交互要求比例。该设计将奖励锚定在可观测行为上，支持多种有效路径，同时过滤教师模型失败的低质量数据。

## 实验评估

实验在TAU-2、BFCL-V4等7个智能体基准及AIME、FRAMES等7个推理基准上进行，基线包括Qwen3系列及ToolStar。SYNTHAGENT-14B在TAU-2平均得分46.3%，超越Qwen3-32B的36.0%；在AIME25达66.7%，接近Qwen3-235B的70.6%。

| 方法 | TAU-2 Avg | BFCL-V4-Multi-turn Avg | AIME25 |
|---|---|---|---|
| Qwen3-32B | 36.0 | 36.0 | 41.1 |
| ToolStar-14B | 35.7 | 35.7 | 63.3 |
| SYNTHAGENT-14B | 46.3 | 46.3 | 66.7 |
| Qwen3-235B | 49.7 | 49.7 | 70.6 |

消融显示，53.5%的合成任务Rubric得分低于0.25，平均工具调用4.2次，表明任务难度分布合理。信息缺口注入使平均用户交互达2.9次，验证了主动查询机制的有效性。

评估边界方面，TAU-2与BFCL-V4使用Exact Match评估环境状态更新，未覆盖自由形式输出的语义一致性。代码已开源，但Mock环境的构建依赖Qwen3-235B，其成本虽低但仍需本地部署。

## 关联研究分析

从问题动机看，SYNTHAGENT与VeriRole同属可验证奖励路线，但VeriRole聚焦角色事实的确定性验证，而SYNTHAGENT针对工具执行轨迹的子目标完成度。差异根源在于任务特性：角色扮演需严格对齐角色档案，而工具使用允许多种有效路径，因此SYNTHAGENT的Rubric设计更侧重行为多样性而非事实唯一性。

从方法设计看，SYNTHAGENT与PersonaForge均利用Persona增加多样性，但PersonaForge将Persona作为角色心理约束，SYNTHAGENT仅作为任务生成种子。这一差异暗示，当任务目标明确时，Persona的认知深度并非必要，其价值主要体现在场景覆盖度上。Mock环境的稳定性是否足以替代真实API的复杂错误模式，论文未给出回答。

## 总结

SYNTHAGENT解决的核心矛盾是智能体RL训练中数据多样性与环境稳定性的冲突。其切入点在于将任务生成与环境构建完全虚拟化，通过信息缺口注入与任务级有限映射，在本地低成本环境下实现大规模RL。实验证明，8B-14B模型在TAU-2上超越Qwen3-32B，在AIME25上接近Qwen3-235B。边界在于，Mock环境仅模拟工具响应，未覆盖真实API的延迟、超时等动态故障模式。当任务涉及多Agent协作或物理世界交互时，该框架的泛化能力如何，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_22edf57ccb76)
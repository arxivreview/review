# HuggingFace最新推荐论文 ｜Raven: The Harness of Harnesses for Composable Agentic Intelligence ｜可组合智能体系统：基于Harness进化的多智能体编排框架

作者：EverMind AI

论文原文见 [arXiv](https://arxiv.org/abs/2609.33439)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2609.33439)

> 多智能体框架长期受困于静态架构的僵化与协调开销的不可控，导致跨域任务泛化能力受限。现有自动化搜索方法仅优化拓扑结构，忽略了执行策略（工具、上下文、技能）与模型能力的耦合效应。Raven将“模型-Harness对”定义为可组合单元，通过Host Agent进行DAG编排，并引入Harness自进化机制以动态调整执行策略。该框架在MAOB基准上取得10.4-10.5个百分点的Exact Match增益，但其理论边界依赖于共享预算假设，实际部署中协调税的非线性增长仍未被完全量化。

## 研究背景

当智能体处理长程跨域任务时，单一模型的上下文窗口与推理深度瓶颈导致性能显著衰减。为解决此问题，多智能体系统引入专业化分工，但手动设计的静态工作流（如MetaGPT的SOP）难以适应动态任务需求，且智能体间的语义漂移与级联错误暴露了架构脆弱性。核心矛盾在于协调税（Coordination Tax）随智能体数量呈非线性增长，而缺乏共享语义基础导致意图分歧，使得协作增益在简单任务中甚至低于单智能体推理。

主流自动化架构搜索路线（如AutoMaAS、GPTSwarm）将优化对象局限于拓扑结构，假设固定执行策略下的最优连接即可最大化性能。然而，这种“结构-策略”解耦假设忽略了Harness（工具接口、上下文管理、技能库）对模型能力释放的关键作用。Raven的切入点在于将Harness视为可进化单元，通过诊断失败并重组执行策略，在共享资源预算约束下形式化定义多智能体组合相对于单智能体的“可靠任务覆盖”边界，从而突破静态架构的通用性缺失。

## 核心方法

### 方法参照系

Raven的问题域属于多智能体架构自动搜索，但与传统拓扑优化不同，其核心差异在于将优化对象从“连接结构”下沉至“执行策略”。标准流程中，进化算法搜索节点连接，而Raven在固定DAG骨架下，通过外部Evolver修改Harness内部参数（工具集、记忆策略、控制规则），实现策略层面的自适应。

### Harness自进化与基因重组

传统方法假设Harness配置固定，导致特定域失效时无法动态调整。Raven引入模块化Harness设计，将执行策略解耦为可独立修改的组件。Evolver通过诊断失败轨迹，从Harness Gene Bank中检索候选策略并进行重组。其适应度函数定义为在冻结任务模型下的可靠任务覆盖率：

$$
\mathcal{F}(h') = \mathbb{E}_{t \sim \mathcal{T}} \left[ \mathbb{I} \left( V_t(\omega, Y_{S'}) = 1, C_{S'} \le B \right) \right]
$$

该公式表明，进化目标是在共享预算$B$内最大化任务$T$的成功概率，其中$Y_{S'}$为重组后Harness $h'$ 的执行记录。这一设计解决了静态Harness在跨域迁移时因工具假设不匹配导致的性能衰减，使系统能根据任务分布动态调整执行边界。

### 基于DAG的Host中介编排

静态SOP流程无法处理动态依赖关系，导致并行任务间的信息丢失。Raven通过Host Agent将任务分解为DAG，节点代表智能体调用，边代表工件依赖。Host在执行前进行Admission Checks，验证图结构合法性与能力匹配性。其调度策略基于就绪节点优先，确保依赖项完成后再触发下游任务。该机制将协调开销显式纳入成本函数$C_S$，包括规划、执行、交接与重试成本，从而在理论上界定了组合系统的可靠性边界。

## 实验评估

实验在MAOB基准上评估编排质量，对比Qwen3.8-27B与DeepSeek-V4-Flash-0731两种骨干。基线覆盖AutoGen、MetaGPT等经典框架，但缺失AOrchestra等2026年最新动态编排方法的直接对比。

| 骨干模型 | 指标 | Raven | Best Baseline | 增益 |
|---|---|---|---|---|
| Qwen3.8-27B | Node F1 | 0.923 | 0.776 | +0.147 |
| Qwen3.8-27B | Exact Match | 0.963 | 0.854 | +0.109 |
| DeepSeek-V4-Flash | Node F1 | 0.897 | 0.813 | +0.084 |
| DeepSeek-V4-Flash | Exact Match | 0.950 | 0.780 | +0.170 |

Raven在两种骨干下均取得最高Exact Match，增益分别为10.4和10.5个百分点，表明DAG编排对依赖预测的鲁棒性。在SWE-Bench Verified上，Raven-Code使用DeepSeek-V4-Flash取得59.3%的解决率，较基线提升3.3个百分点，但低于AOrchestra的86.06%（据领域综述），暗示骨干模型能力仍是主要瓶颈。

消融实验显示，Harness进化对代码生成任务增益显著（+6.6 pp on Qwen3.6-35B-A3B），而在设计任务中增益较小（+1.9 pp on PresentBench），表明策略进化对工具密集型任务更敏感。Skill Forge的引入在三个基准上提升性能，其中两项增益超过OpenClaw，验证了经验复用的有效性。

评估边界受限于静态基准，未报告GAIA等动态环境下的实时协调税数据。代码开源但超参数配置未完全披露，Harness进化过程的计算开销未量化，可复现性依赖于特定骨干与任务分布。

## 关联研究分析

从问题动机看，Raven与AutoMaAS均针对架构僵化，但AutoMaAS优化拓扑连接，Raven优化执行策略。这一差异源于任务特性：AutoMaAS假设固定工具集下的最优连接，而Raven认为工具-任务匹配度是性能瓶颈。根源在于Raven将Harness视为一等公民，而AutoMaAS将其视为黑盒。

从方法设计看，Raven与AOrchestra均支持动态子智能体创建，但AOrchestra侧重任务特定实例化，Raven侧重跨任务经验复用。AOrchestra在SWE-Bench上取得更高分数，可能因其更激进的并行策略，而Raven的共享预算约束限制了并行度。查询侧增强在数据充足时是否仍有增益，论文未给出回答。

## 总结

Raven解决的核心矛盾是静态架构与动态任务需求的错配，其切入点在于将Harness作为可进化单元，通过策略重组突破拓扑优化的局限。该框架在MAOB上取得10.4-10.5个百分点的Exact Match增益，证明了DAG编排与Harness进化的协同效应。然而，实验边界暴露了共享预算假设的局限性：在SWE-Bench上，Raven的性能仍受骨干模型能力制约，且未量化协调税在动态环境中的非线性增长。当任务复杂度超过单智能体推理深度时，Harness进化的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2609.33439)
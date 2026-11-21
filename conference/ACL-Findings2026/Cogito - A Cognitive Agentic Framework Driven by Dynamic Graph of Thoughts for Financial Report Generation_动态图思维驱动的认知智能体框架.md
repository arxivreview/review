# ACL-Findings2026最新论文 ｜Cogito: A Cognitive Agentic Framework Driven by Dynamic Graph of Thoughts for Financial Report Generation ｜动态图思维驱动的认知智能体框架

作者：Chen Lifan、Wei Ding、Jingwen Yang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a79cbcf5c9b5)

> 金融报告生成要求在开放且充满噪声的环境中，将碎片化数据重构为逻辑严密的专业叙事，传统静态推理架构无法应对实时市场中的“未知未知”。现有方法要么依赖预定义工作流导致适应性不足，要么缺乏垂直领域的深度专业知识。Cogito 通过引入动态图思维（Dy-GoT）实现推理拓扑的运行时演化，并结合社会协作机制协调多智能体分工。该框架在自建金融基准上超越了闭源商业系统，但其依赖高算力消耗且缺乏通用基准验证，泛化能力存疑。

## 研究背景

金融研究专家在构建报告时，需频繁在直觉规划与深度检索间切换，并依据新线索动态调整探索路径。这种认知灵活性对应双过程理论（Dual Process Theory, DPT）中的快慢系统切换，以及Bates的浆果采摘模型（Berrypicking Model）中基于反馈的路径演化。然而，大语言模型（LLM）的传统思维链（Chain-of-Thought, CoT）或图思维（Graph of Thoughts, GoT）架构依赖预定义的静态计算拓扑，一旦初始规划完成，后续检索无法触发新的探索分支，导致关键信息被遗漏。

深度研究智能体（Deep Research Agents, DRA）旨在解决长周期信息整合问题，但通用DRA往往缺乏垂直领域的专业深度，而金融专用模型又受限于静态工作流。当前主流方法如FinDebate或TradingAgents通过角色扮演增强专业性，但无法处理实时市场动态；通用Deep Research系统虽擅长检索，却难以生成符合审计标准的专业叙事。Cogito的切入点在于将认知科学理论转化为可执行的动态推理引擎，使智能体能够根据中间发现重构认知轨迹，而非仅优化预设计划。

## 核心方法

### 静态推理架构的局限

通用DRA通常采用“规划-执行”范式，先分解问题再检索细节。该流程假设所有必要信息在初始分解时已可预见，导致检索过程成为对预设边界的填充。在金融场景中，关键风险或机遇往往隐藏于“未知未知”，仅在执行搜索后通过中间反馈才能显现。静态架构无法响应此类意外发现，导致推理路径僵化，无法实现从初始不确定性到结构化专业知识的跃迁。

### 进化认知机制与动态图思维

Cogito引入进化认知机制（Evolutionary Cognitive Mechanism, ECM）作为核心驱动，结合DPT与Berrypicking模型，实现快慢思考的动态切换。在时间步 $t$，系统并行执行一批活跃节点 $V_t$，产生深度推理输出 $O_t$ 和意外发现 $D_t$。水平审计函数 $A$ 评估当前认知状态，决定是继续还是终止研究。若继续，任务生成函数 $\Gamma$ 输出新计划，演化算子 $\Omega$ 将其拓扑整合至当前图 $G_t$：

$$
G_{t+1} = \begin{cases} \Omega(G_t, \Gamma(D_t, O_t)), & \text{if } A(V_t) \rightarrow \text{Cont.} \\ G_t, & \text{if } A(V_t) \rightarrow \text{Stop} \end{cases}
$$

该公式表明，Cogito并非简单追加任务，而是基于中间发现重构认知轨迹。动态图思维（Dy-GoT）将推理建模为有限状态机，支持运行时节点生成与回溯，使智能体能根据外部反馈动态扩展探索分支，解决静态架构无法应对“未知未知”的失效问题。

### 社会协作机制与多智能体分工

针对单智能体能力边界局限，Cogito设计社会协作机制（Social Collaboration Mechanism, SCM），基于交互记忆系统（Transactive Memory System, TMS）协调四个专职智能体。专家角色注入机制（ERIM）通过 $\rho^+ = \text{ERIM}(\rho_{\text{base}}, C_{\text{dom}})$ 将领域上下文注入基础提示，强制加载专业思维范式。团队协作感知机制（TCPM）使上游智能体感知下游智能体画像 $M = \{id_{\text{dst}}, \text{Need}_{\text{dst}}, \text{Act}_{\text{dst}}\}$，约束指令生成策略 $\pi$：

$$
I_c = \pi(M, \rho^+)
$$

该机制确保通信在源头被约束，例如ResearcherAgent感知ToolAgent负责事实核查后，自动过滤主观评论类搜索意图。DIKAgent执行“提取-验证-融合”流程，通过事实核查过滤噪声，确保后续推理基于高密度事实而非原始噪声，解决多源异构数据整合中的幻觉与冗余问题。

## 实验评估

Cogito在自建20个金融任务（10企业级+10行业级）上评估，基线覆盖LLM+搜索、开源Agent及闭源Deep Research系统，但缺失RL训练类方法如ASearcher。主实验显示，Cogito在企业级和行业级总分分别达到95.2和96.7，显著超越最强开源基线GPT-Researcher（78.4/79.2）及闭源系统Gemini DeepResearch（89.9/90.1）。

| 模型 | 企业级总分 | 行业级总分 |
| :--- | :--- | :--- |
| GPT-Researcher | 78.4 | 79.2 |
| Gemini DeepRes. | 89.9 | 90.1 |
| Cogito (Ours) | 95.2 | 96.7 |

消融实验揭示，移除ERIM导致词汇多样性（MTLD）下降10.2%，FK-Grade阅读水平降低0.16，领域深度评分从4.8降至4.7，验证了专家角色注入对专业叙事风格的激活作用。DIKAgent的事实核查机制将忠实度从0.684提升至0.769，引用准确率峰值达0.888，证明验证环节对抑制压缩性幻觉的关键作用。

评估协议依赖Gemini 3 Pro作为LLM-as-Judge，单次研究耗时12分钟以上，高算力消耗限制了大规模数据集评估。代码未公开，超参数细节有限，可复现性受限。指标虽涵盖数据、分析与呈现维度，但缺乏通用基准（如GAIA）验证，垂直领域优势是否可迁移至其他领域存疑。

## 关联研究分析

从方法设计看，Cogito与WebWeaver同属架构派，但WebWeaver侧重双智能体证据结构化，而Cogito通过Dy-GoT实现推理拓扑的运行时演化。Cogito的动态性源于ECM的水平审计机制，允许智能体在检索中重构计划，而WebWeaver的静态大纲优化无法响应意外发现。这一差异源于任务特性：金融场景的“未知未知”要求推理路径具备突变能力，而非仅优化预设计划。

从问题动机看，Cogito与ASearcher形成架构vs训练的对比。ASearcher通过大规模端到端RL优化搜索策略，依赖模型泛化能力；Cogito则通过架构设计实现自适应，依赖认知科学理论指导。Cogito未采用RL训练，可能限制其在更复杂通用任务上的泛化能力，但其动态拓扑演化在垂直领域验证有效。查询侧增强在数据充足时是否仍有增益，论文未给出回答。

## 总结

Cogito旨在解决金融报告生成中静态推理架构无法应对“未知未知”的核心矛盾，通过Dy-GoT实现推理拓扑的运行时演化，并结合SCM协调多智能体分工。实验显示其在自建基准上超越闭源系统，企业级总分95.2，行业级96.7。然而，高算力消耗与缺乏通用基准验证暴露了边界：动态拓扑演化的计算开销是否抵消了架构优势？当支持集增大时，ERIM的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_a79cbcf5c9b5)
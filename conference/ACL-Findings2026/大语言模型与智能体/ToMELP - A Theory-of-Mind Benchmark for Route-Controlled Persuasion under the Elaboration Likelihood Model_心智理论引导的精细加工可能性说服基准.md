# ACL-Findings2026最新论文 ｜ToMELP: A Theory-of-Mind Benchmark for Route-Controlled Persuasion under the Elaboration Likelihood Model ｜心智理论引导的精细加工可能性说服基准

作者：Ruirui Wang、Haoran Zhang、Tian Lan 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_7e9e1302d33f)

> 说服对话中的心智理论（Theory of Mind, ToM）评估长期受困于“能答对问题”与“能据此行动”之间的鸿沟，现有基准缺乏对受众信息处理路径的显式控制，导致模型表现归因模糊。ToMELP 通过构建受众画像（Persona）与精细加工可能性模型（Elaboration Likelihood Model, ELM）双路径的 2×2 因子设计，将 ToM 推断与策略执行解耦为可审计的闭环。该基准揭示了 ToM 注入在外围路径下的稳定增益与中央路径下的证据组织瓶颈，但其依赖 LLM-as-a-judge 且未进行人类一致性验证，限制了结论的绝对效度。

## 研究背景

说服系统的有效性不仅取决于论据质量，更取决于对受众心理状态的动态建模。当模型无法区分受众是依赖证据逻辑（中央路径）还是启发式线索（外围路径）时，其生成的说服策略往往出现错位。这种错位源于传统 ToM 评估仅关注静态信念预测，忽略了“推断-使用”闭环中策略选择的动态性，导致模型在真实多轮对话中表现出脆弱性。

现有 ToM 基准如 OpenToM 和 ToMBench 虽引入了叙事触发与细粒度分类，但普遍缺乏对受众异质性与信息处理机制的受控变量。PersuasiveToM 虽建立了对话状态骨架，却未隔离中央与外围路径的资源差异，使得模型表现难以归因于 ToM 能力还是文本生成能力。ToMELP 的切入点在于将 ELM 双路径作为正交控制变量，通过配对资源对比，强制模型在相同对话状态下执行不同路径的说服策略，从而暴露 ToM 推断与路径保真度之间的潜在冲突。

## 核心方法

### 方法参照系

本文问题归属于受控对话状态下的 ToM 评估范式，其标准流程为：给定对话历史，推断受众 BDI 状态，选择策略并生成文本。与通用流程的关键差异在于，ToMELP 将 ELM 路径作为显式约束，要求模型在中央路径下引用事实/反论，在外围路径下使用启发式短语，从而将“推断”与“执行”解耦为可独立审计的环节。

### 配对路径资源构造

针对 PersuasiveToM 中路径资源混杂导致的归因模糊问题，ToMELP 为每个对话状态构造中央与外围配对记录。中央路径提供 6 个事实（$F_1, \dots, F_6$）与 3 个反论（$C_1, \dots, C_3$），外围路径提供 5 类启发式短语（权威、社会证明、好感、互惠、稀缺）。该设计动机在于消除路径混淆，使模型在相同 BDI 状态下仅因资源类型不同而产生行为差异，从而隔离 ToM 对路径选择的真实影响。

$$
\mathcal{R}_{route} = \begin{cases} \{F_i, C_j\}_{i=1}^6, \{C_j\}_{j=1}^3 & \text{if } route = central \\ \{H_k\}_{k=1}^5 & \text{if } route = peripheral \end{cases}
$$

该公式定义了路径资源集 $\mathcal{R}_{route}$，其物理含义是：在固定对话状态 $S$ 下，模型仅能访问与指定路径匹配的资源子集，从而强制其生成符合路径约束的说服文本。

### ToM 注入与路径保真度评估

为验证 ToM 推断是否真正转化为策略执行，ToMELP 引入 $tom\_aware$ 提示变体，将模型预测的 BDI 状态显式注入生成阶段。路径保真度通过二元匹配（Route Fit）与替代率（Substitution）量化，其中替代率定义为意图中央但被判为外围的比例。该设计动机在于揭示 ToM 对齐与路径可控性之间的权衡：模型可能通过更外围化的表达提升受众对齐，却牺牲了中央路径的证据组织质量。

$$
Substitution = \frac{|\{x \in \mathcal{D} : route_{intent}(x)=central \land route_{judge}(x)=peripheral\}|}{|\{x \in \mathcal{D} : route_{intent}(x)=central\}|}
$$

该公式计算中央路径下的替代率，其算法含义是：在意图使用证据论证的样本中，模型实际依赖启发式线索的比例，直接反映路径漂移的严重程度。

## 实验评估

实验在 ToMELP 基准上进行，包含 1,829 个对话状态与 3,658 条配对记录，评估 Llama-3.1-8B、Qwen2.5-7B/72B、ChatGPT-5.2 与 Claude-sonnet-4 五个模型。基线覆盖主流开源与闭源 LLM，但缺失激活引导类内部表示干预方法（如 CAA、Persona Vectors），导致无法对比外部提示注入与内部向量控制的效果差异。

| 模型 | 变体 | Att. Shift | Route Fit | ToM Tail. | Robust Ret. |
| :--- | :--- | :--- | :--- | :--- | :--- |
| ChatGPT-5.2 | tom_aware | 1.13 | 0.80 | 1.25 | 0.59 |
| ChatGPT-5.2 | no_tom | 1.04 | 0.81 | 1.25 | 0.55 |
| Qwen2.5-72B | tom_aware | 1.07 | 0.84 | 1.32 | 0.58 |
| Qwen2.5-72B | no_tom | 0.93 | 0.80 | 1.23 | 0.50 |
| Claude-sonnet-4 | tom_aware | 0.60 | 0.77 | 1.42 | 0.69 |
| Claude-sonnet-4 | no_tom | 0.41 | 0.68 | 1.29 | 0.57 |

ChatGPT-5.2 在 $tom\_aware$ 下 Att. Shift 提升 0.09，但 Route Fit 仅微降 0.01，表明 ToM 注入对路径保真度影响有限；Claude-sonnet-4 的 ToM Tail. 最高（1.42），但 Att. Shift 最低（0.60），揭示高对齐未必带来高说服效果。

消融分析显示，ToM 注入在外围路径下增益显著（Persona B 下 $\Delta$Attitude 达 +0.64），而在中央路径下增益微弱（Persona A 下仅 +0.07）。这一反直觉发现表明，ToM 更擅长优化受众风格匹配，而非提升证据组织质量。在扰动测试中，$tom\_aware$ 在 MISLEADING 扰动下 Robust Ret. 提升最大（ChatGPT-5.2 从 0.55 升至 0.59），验证了其“目标锚点”作用。

评估边界方面，ToMELP 未进行人类一致性验证，LLM-as-a-judge 可能存在系统性偏差；指标完备性上，缺乏计算效率与跨文化泛化评估；可复现性上，论文提供源代码，但 GPT-4o 生成数据与人工验证流程（Cohen’s κ = 0.78）未完全公开。

## 关联研究分析

从问题动机看，ToMELP 与 PersuasiveToM 共享对话状态骨架，但后者未隔离 ELM 路径，导致模型表现归因于 ToM 与文本生成的混合效应。ToMELP 通过配对资源构造，将路径作为显式变量，使得“推断-使用”闭环中的策略选择可独立审计。这一差异源于任务特性：说服效果高度依赖受众信息处理机制，而通用 ToM 评估忽略此维度，导致模型在真实场景中表现脆弱。

从方法设计看，ToMELP 与 OpenToM 均关注叙事触发，但 OpenToM 依赖自由叙事，而 ToMELP 采用结构化资源（Facts/Heuristics）替代自由文本，提高了可控性。这一差异源于评估目标：OpenToM 侧重 ToM 推断准确性，ToMELP 侧重 ToM 对策略执行的影响。然而，ToMELP 未探索内部表示干预方法（如激活工程）对路径保真度的影响，提示注入式控制是否足以替代内部向量调制，论文未给出回答。

## 总结

ToMELP 要解决的核心矛盾是 ToM 推断与策略执行之间的归因模糊，现有方法因缺乏路径控制而无法区分模型是“真懂”还是“假装”。本文抓住 ELM 双路径作为正交变量，通过配对资源构造与 ToM 注入，将“推断-使用”闭环解耦为可审计环节。实验证明 ToM 注入在外围路径下提升 Att. Shift 达 0.64，但在中央路径下仅 0.07，且高 ToM 对齐未必降低替代率。其边界在于依赖 LLM-as-a-judge 且未进行人类验证，导致结论受评判模型偏好影响。当受众画像从二元（high-cog/low-cog）扩展至连续谱时，ToM 注入的路径保真度是否仍保持稳定，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_7e9e1302d33f)
# HuggingFace最新推荐论文 ｜Automating the Design of Embodied Agent Architectures ｜具身智能体架构搜索

研究机构：澳大利亚阿德莱德大学

作者：Jian Zhou、Sihao Lin、Jin Li 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.30111)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.30111)

> 具身智能体通常由感知、记忆、规划与控制模块手工组装而成，这种显式结构虽利于调试，却导致架构设计空间随基础模型与工具增多而指数膨胀，人工迭代难以覆盖。现有文本域架构搜索方法直接迁移至具身场景时，因仿真器状态依赖、评估噪声及缺乏通用推理原语而失效。本文提出基于类型化图的运行时环境 AgentCanvas 与知识蒸馏循环优化器 KDLoop，在四个具身智能体上验证了自动化架构搜索的可行性。该工作揭示了具身 AAS 在评估噪声与局部最优下的独特约束，但搜索出的架构是否具备物理常识仍存疑。

## 研究背景

具身智能体的核心挑战在于弥合语义意图与物理现实间的鸿沟。传统模块化架构将大语言模型（LLM）作为高层规划器，但中间符号表示导致的误差累积限制了长时程任务的可靠性。随着视觉-语言-动作模型（Vision-Language-Action, VLA）的兴起，领域转向端到端范式，直接映射感官输入到低层动作，显著提升了感知与执行的耦合效率。然而，VLA 对海量模仿数据的依赖及其在动态环境中的泛化瓶颈，促使研究重心转向强化学习、世界模型与记忆机制。当前，构建具备物理常识、空间记忆与动态适应能力的通用具身智能体成为共识，各路线在数据效率、推理深度与部署成本间做出不同取舍。

具身智能体架构设计面临“组合爆炸”困境。每个智能体需固定传感器抽象、地图表示、记忆状态、提示结构、规划器拓扑等选择，这些选择通常针对单一基准手工完成。随着基础模型与具身工具增多，合理架构空间增长速度快于人工迭代能力。Agent Architecture Search (AAS) 在文本域通过优化器自动提议并评估替代工作流，但直接迁移至具身域并非简单复制。文本域 AAS 操作于廉价、无状态调用及成熟原语词汇（如思维链、辩论），而具身智能体交互于有状态仿真器，产生噪声多回合评估，且依赖包含观测、动作、工具调用的长执行轨迹。更关键的是，不存在可组合的具身推理原语小调色板，自然起点是已发表系统如 MapGPT、SmartWay、ExploreEQA 和 VoxPoser。因此，本文研究具身 AAS 的“方法种子”形式：每次搜索会话从已发表具身智能体架构开始，搜索邻近图级修改，而非从头组装智能体。

## 核心方法

### 方法参照系

具身 AAS 问题可形式化为：给定种子执行器 $c_0$ 和预算 $B$，生成轨迹 $\{c_t\}_{t=0}^B$ 并返回最佳评估候选 $\arg\max_{t \le B} f(c_t)$，其中 $f(c)$ 为多回合仿真器评估的成功率。与文本域 AAS 从通用 LLM 调用算子库搜索不同，具身智能体缺乏任务无关的可运行原语，导航、问答与操作系统各自包含任务特定的感知、状态与动作接口。因此，本文采用方法种子设置，每个 $c_0$ 是已发表具身智能体方法，搜索探索该方法的图级修改。

### 执行器基底：AgentCanvas

AgentCanvas 将具身智能体表示为类型化节点-连线 JSON 图，由 Python 节点模块支撑。节点暴露类型化输入-输出端口，图编辑（添加边、交换节点、替换子图）作为结构化补丁应用，类型兼容性在昂贵回滚前检查。该基底解决此前方法中候选架构无法在状态仿真器中运行的问题：文本域 AAS 常用单次 LLM 完成生成候选，足以处理紧凑 Python 执行器，但不足以处理多文件具身智能体代码。AgentCanvas 还仪器化每个回滚，节点触发记录外部输入输出，节点可写入内部面包屑（如规划器决策、提示、工具调用、自报告），这些回合级记录连接候选编辑与下游行为，通过共享框架暴露给所有优化器变体。

### 优化器基底：KDLoop

KDLoop 针对具身设置设计，其中每次迭代产生比标量分数更多的证据。它运行四阶段循环：THINK 读取蒸馏记忆并提议最多三个实验，每个标记干预轴（如提示内容、拓扑、观测管道、状态记忆、模型配置）；CRITIC 检查提议编辑与先前失败补丁及约束；EXPERIMENT 应用并评估选定编辑；DISTILL 将结果写回类型化记忆，包括确认发现、反驳编辑、开放猜想与搜索空间覆盖。当进度停滞时触发 REFLECT 阶段，审计停滞进度、更新覆盖并可能标记空间部分为耗尽。该记忆结构旨在解决两个具身 AAS 失效模式：跟踪已尝试编辑类型以减少重复局部采样，保留机制级证据以避免在扁平归档中丢失。

$$
\text{KDLoop}_{t+1} = \text{DISTILL}\left(\text{EXPERIMENT}\left(\text{CRITIC}\left(\text{THINK}(M_t)\right)\right)\right)
$$

其中 $M_t$ 为第 $t$ 迭代的类型化记忆，包含确认发现、反驳编辑、开放猜想与搜索空间覆盖。该公式表明 KDLoop 通过显式记忆更新而非仅标量分数驱动搜索，解决此前方法中优化器仅关注标量结果而忽略机制级证据的问题。

## 实验评估

实验使用单一固定 AgentCanvas 构建，执行器表示为前向节点-连线图，骨干固定为 GPT-5-MINI（VoxPoser 除外）。搜索框架使用 Claude Code 提供编码智能体会话，Claude Opus 4.7 与 1M-token 上下文窗口作为编排器。搜索从四个已发表具身智能体方法种子开始，跨越三个家族：MapGPT 和 SmartWay 用于 VLN，ExploreEQA 用于 EQA，VoxPoser 用于零样本 VLA。每个单元格从对应方法基线开始，搜索时适应度由任务成功率（SR）测量。报告原始 SR 均值 ± 标准差，基于三次后选择通道，以分离搜索时选择与重跑方差。

| 执行器 | 优化器 | 基线 | 最佳 | Δ | 存活变化（轴） |
| :--- | :--- | :--- | :--- | :--- | :--- |
| MapGPT | ADAS | 46.9±3.1 | 49.1±3.2 | +2.2 | Step-Back distill + STOP-advisor wire + landmark gate (state-mem, topology) |
| MapGPT | AFlow | 46.9±3.1 | 54.5±3.1 | +7.6 | Stop/anti-revisit rules + elevation deadband (prompt, obs) |
| MapGPT | KDLoop | 46.9±3.1 | 54.0±2.3 | +7.1 | Heading-band action gate + `stop_after` 3→5 (obs, control) |
| ExploreEQA | ADAS | 43.0±1.7 | — | — | No iter beat baseline — lever not at the graph layer |
| ExploreEQA | AFlow | 43.0±1.7 | 47.7±2.1 | +4.7 | VLM single-letter prompt rewrite (prompt) |
| ExploreEQA | KDLoop | 43.0±1.7 | 46.0±1.0 | +3.0 | Bayesian prior + sentinel MCQ filter + “A/B/C/D-only” (state-mem, obs, prompt) |
| SmartWay | ADAS | 29.7±2.1 | 33.7±2.5 | +4.0 | Plurality-vote planner (n=3) + Stop-Gate (model-cfg, topology) |
| SmartWay | AFlow† | 29.7±2.1 | 38.7±5.9 | +9.0 | Progress-tracker wired to evaluator (**leak**) + stall hint (topology, state) |
| SmartWay | KDLoop | 29.7±2.1 | 31.0±4.6 | +1.3 | STOP-lexicon history accumulator (state-mem) |
| VoxPoser | ADAS | 9.0±0.0 | 12.7±0.0 | +3.7 | Composer rewrites + execution-loop tuning (model-cfg, action) |
| VoxPoser | AFlow | 9.0±0.0 | 12.9±0.5 | +3.9 | GPT-4o composer swap + retry loop + workspace bounds (model-cfg, control, obs) |
| VoxPoser | KDLoop‡ | 9.0±0.0 | — | — | Detected shared VoxPoser logging fault; diagnosed below graph layer; no mutation |

表 1 显示架构级搜索可在主导失效模式位于可编辑图内时改进具身执行器。大多数选定候选在重跑后改进基线均值，但方差重叠的增量被视为方向性而非认证。增益在 MapGPT 上最清晰，AFlow 和 KDLoop 从 46.9±3.1 基线通过不同停止、重访与动作门控编辑达到相似 ~54% SR。ExploreEQA 通过答案格式化与哨兵处理变化更温和地改进。SmartWay–AFlow 单元格因使用评估器侧信息而从可部署增益计数中排除，保留为诊断失效模式。无优化器占优：ADAS 倾向于集中在拓扑与模型配置，AFlow 常编辑观测管道，KDLoop 将编辑分散在观测、提示、控制与状态记忆轴。两个无 SR 声明的单元格也具有信息量：ADAS 在 ExploreEQA 上未找到改进的图级杠杆，而 KDLoop 揭示共享 VoxPoser 日志故障并以图下诊断终止。

消融分析显示局部最优收敛的三个症状。首先，努力集中在最常用轴，ADAS/AFlow/KDLoop 平均 60%/43%/38%。其次，ADAS 在六个迭代中反复重新发现相同 MapGPT 分数 SR=0.4769，暗示重访已测试邻域。第三，无空间级停止谓词时，ADAS 和 AFlow 在所有八个单元格运行至迭代上限，使用 84 和 82 次提交迭代。这些模式表明具身 AAS 需要不仅对标量分数，还对尝试编辑结构的记忆。KDLoop 通过类型化历史减少盲目局部重采样并改进可编辑图空间覆盖，但此覆盖偏差也可能欠利用有用盆地。在 SmartWay 上，ADAS 在承诺区域停留足够长以找到有用的图级细化，而 KDLoop 更早重定向。

评估边界与可复现性方面，指标完备性受限于标量 SR，缺乏对机制级改进的细粒度度量。评估协议局限在于单次通道选择可能高估候选架构真实价值，高方差 SmartWay 单元格显示选择与验证不可互换：单次通道分数识别候选，但重复评估需解释它。可复现性方面，论文提供项目页面 URL，但 AgentCanvas 为首次提出，无开源实现。

## 关联研究分析

从问题动机看，本文与 SayCan、Code-as-Policies 等模块化系统共享显式架构前提，但解决不同问题。SayCan 结合 LLM 任务解释与 RL 仿射模型，奠定 LLM 驱动具身规划基础，但假设环境状态可被离散技能覆盖，受限于 LLM 缺乏物理感知。Code-as-Policies 通过提示 LLM 生成 Python 脚本作为直接控制策略，取代传统离散动作原语映射，允许 LLM 合成低层控制逻辑。本文不改进这些系统的特定模块，而是自动化整个架构设计过程。差异根源在于任务特性：模块化系统针对单一基准手工设计，而本文面对架构空间随基础模型与工具增多而指数膨胀的困境。本文方法种子设置匹配当前具身系统工程实践，但搜索出的架构是否具备知识库强调的“物理常识”未验证。

从方法设计看，本文与 NeSyPr、HELP 等神经符号方法同属模块化路线，但引入外部优化器自动编辑代码。NeSyPr 针对自回归推理中的浅层规划与上下文复用低效问题，提出神经符号程序化方法，将 LLM 与外部符号推理框架集成，通过结构化推理过程将自然语言指令转化为符号化程序表示。HELP 引入层级具身语言规划器，通过两阶段管线解决自然语言指令中的歧义与分解问题。本文 KDLoop 与这些方法的关键差异在于搜索对象：NeSyPr 和 HELP 优化特定推理流程，而 KDLoop 优化整个节点-连线图结构。本文未采用更严苛评估协议，如统一骨干与统一预训练条件下的重评测，这可能导致方法贡献与骨干网络贡献区分不清。

## 总结

具身智能体架构设计面临组合爆炸困境，人工迭代难以覆盖随基础模型与工具增多而指数膨胀的架构空间。本文抓住方法种子切入点，从已发表具身智能体架构开始搜索邻近图级修改，而非从头组装智能体，解决了文本域 AAS 直接迁移至具身域时因仿真器状态依赖、评估噪声及缺乏通用推理原语而失效的问题。本文提出 AgentCanvas 类型化图运行时与 KDLoop 知识蒸馏循环优化器，在四个具身智能体上验证了自动化架构搜索的可行性，MapGPT 上 AFlow 和 KDLoop 从 46.9±3.1 基线达到 ~54% SR，ExploreEQA 上 AFlow 从 43.0±1.7 基线达到 47.7±2.1。本文边界在于评估噪声可能掩盖图编辑效果，搜索动态可能陷入局部编辑盆地，回合级信用分配仅部分涌现。当支持集增大到 5-shot 时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.30111)
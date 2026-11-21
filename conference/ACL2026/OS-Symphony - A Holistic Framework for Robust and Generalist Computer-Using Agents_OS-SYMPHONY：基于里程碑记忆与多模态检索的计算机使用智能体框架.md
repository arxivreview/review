# ACL2026最新论文 ｜OS-Symphony: A Holistic Framework for Robust and Generalist Computer-Using Agents ｜OS-SYMPHONY：基于里程碑记忆与多模态检索的计算机使用智能体框架

研究机构：中国科学技术大学、新加坡国立大学

作者：Bowen Yang、Kaiming Jin、Zhenyu Wu 等 15 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e9b1a82c0513)

> 导读 计算机使用智能体（Computer-Using Agents, CUAs）旨在通过视觉感知与动作执行实现数字环境的自主操作，其核心挑战在于长时程任务中的上下文丢失与分布外（Out-of-Distribution, OOD）场景的知识缺失。现有模块化框架虽能分解任务，但缺乏对历史视觉信息的细粒度控制，且依赖静态文本检索导致视觉语义丢失。OS-SYMPHONY 通过引入里程碑驱动的反思记忆智能体（Reflection-Memory Agent, RMA）与在线多模态检索器，实现了轨迹级自我修正与实时教程获取。该框架在 OSWorld 等基准上刷新了 SOTA，但其性能高度依赖骨干大语言模型（Large Language Model, LLM）的推理能力，且存在视觉感知粒度不足导致的误报风险。

## 研究背景

CUA 的决策过程依赖于视觉-语言模型（Vision-Language Model, VLM）对屏幕状态的解析与动作生成。然而，长时程任务中，VLM 的上下文窗口有限，若直接保留所有历史截图，会导致计算开销激增且关键信息被冗余数据淹没。这种“视觉上下文过载”使得智能体难以识别意图漂移或循环行为，进而无法生成有效的反思以修正规划。为解决此问题，研究界引入了记忆机制，但现有方法多采用文本摘要或固定窗口截断，丢失了屏幕布局、颜色变化等对 GUI 操作至关重要的视觉语义。

CUA 领域正从端到端原生模型向模块化多智能体框架演进，以缓解数据依赖并提升可解释性。主流路线如 Agent S3 等通过规划器、定位器与执行器的协作处理复杂任务，但在面对未见过的软件或动态变化的界面时，往往因缺乏外部知识而陷入停滞。传统的检索增强生成（Retrieval-Augmented Generation, RAG）方法依赖离线构建的文本知识库，不仅维护成本高，且无法解析包含大量截图的教程，导致在 OOD 任务上泛化能力薄弱。OS-SYMPHONY 的切入点在于将记忆管理从“文本压缩”升级为“视觉里程碑筛选”，并将知识获取从“离线检索”转变为“在线多模态浏览”，从而在长时程与 OOD 场景下实现闭环自我改进。

## 核心方法

### 模块化 CUA 架构参照系

OS-SYMPHONY 遵循模块化 CUA 的标准范式，由 Orchestrator（编排器）、Tool Agents（工具智能体）与记忆模块组成。与通用流程的关键差异在于，其 Orchestrator 不直接处理全量历史，而是依赖 RMA 提供的精炼反馈，且工具智能体中的 Searcher 具备自主浏览网页的能力，而非仅调用静态 API。

### 里程碑驱动的反思记忆智能体

RMA 的核心设计动机是解决长时程任务中因视觉冗余导致的上下文过载与错误累积。在标准流程中，智能体通常保留最近 $K$ 步的原始交互记录，但这无法捕捉跨越数十步的宏观进度。OS-SYMPHONY 引入里程碑标记机制，RMA 在每一步评估当前观察 $o_i$ 是否构成里程碑，仅当标记 $m_i$ 为真时，才将摘要 $S_i$ 与截图 $o_i$ 存入长期记忆 $H_{long}$。

$$
H_{long} = \{(S_j, o_j, m_j)\}_{j=1}^{i-1}, \quad m_j \in \{0, 1\}
$$

该公式表明长期记忆仅包含被标记为里程碑的步骤，大幅压缩了上下文长度。RMA 基于 $H_{long}$ 生成轨迹级反思 $R_i$，其状态分为 On-track、Completed、Infeasible 或 Off-track。对于 Off-track 状态，RMA 进一步细分为 GUI Error、Lack of Tutorial、Code Error 等，并通过规则基循环检测算法辅助识别停滞。这种机制使得 Orchestrator 能在不消耗大量 token 的情况下，获得关于全局进度的高精度反馈，从而及时纠正意图漂移。

### 视觉中心的多模态检索器

Searcher 的设计动机是克服静态 RAG 在 OOD 任务上的失效，特别是当教程以截图形式存在时。传统方法依赖文本解析，无法理解 GUI 布局。OS-SYMPHONY 的 Searcher 采用 SeeAct 范式，在隔离的浏览器沙箱中自主导航，通过视觉感知与动作执行合成实时教程。

$$
A_{search} = \{click, type, scroll, \dots\}, \quad T = \text{Synthesize}(q, o_t, A_{search})
$$

其中 $q$ 为 Orchestrator 生成的“如何”查询，$o_t$ 为当前主环境观察，$T$ 为合成的多模态教程。Searcher 仅在检测到知识缺口时调用，且强制要求返回高相关性的教程，否则报告失败。这种“按需检索”机制避免了无关信息对 Orchestrator 上下文的污染，同时保留了视觉布局信息，解决了文本 RAG 无法解析截图教程的瓶颈。

## 实验评估

OS-SYMPHONY 在 OSWorld-Verified（361 任务）、WindowsAgentArena 与 MacOSArena 上进行评估，基线涵盖 Agent S3、UI-TARS、OpenCUA 等主流 CUA 框架。实验设置统一使用 GPT-5 或 Qwen3-VL 系列作为骨干 VLM，UI-TARS-1.5-7B 作为定位器。

| 方法 | OSWorld Avg (%) | WindowsAgentArena Avg (%) | MacOSArena Avg (%) |
| :--- | :--- | :--- | :--- |
| Agent S3 w/ GPT-5 | 56.60 | 54.10 | - |
| UI-TARS-2 | 53.10 | 50.60 | - |
| OS-SYMPHONY w/ GPT-5 | 65.84 | 63.45 | 46.03 |
| OS-SYMPHONY w/ GPT-5-Mini | 63.61 | 62.15 | 46.03 |

OS-SYMPHONY 在 OSWorld 上以 65.84% 的成功率超越 Agent S3 9.24 个百分点，在 WindowsAgentArena 上以 63.45% 超越基线 9.35 个百分点，表明框架在跨平台 GUI 操作中具有显著优势。值得注意的是，GPT-5-Mini 版本在 MacOSArena 上达到 46.03%，远超 Qwen3-VL-32B-Instruct 的 19.05%，显示框架对骨干模型推理能力的依赖。

消融实验揭示了 RMA 与 Searcher 的关键贡献。移除 Searcher 后，Daily 域成功率下降 22.1%，证实了在线检索对知识密集型任务的重要性。移除 RMA 后，Workflow 域成功率下降约 20.7%，且平均步骤数增加 3.3 步，表明反思机制有效减少了无效探索。反直觉的是，简单的 Last-K 反思（Refl. w/ STM）效果不如完全移除反思，甚至导致 token 消耗增加 36.5%，说明低质量的上下文反思可能干扰决策。

评估边界方面，OSWorld 任务定义存在歧义，部分失败源于指令模糊而非智能体缺陷。实验未报告置信区间，且 Pass@K 结果（Pass@5 达 79.4%）显示模型存在高随机性，单次成功率可能低估其潜在能力。代码已开源，但依赖 GPT-5 等专有模型，开源模型复现效果受限。

## 关联研究分析

从记忆机制设计看，OS-SYMPHONY 的 RMA 与具身智能体领域的 Dejavu 框架存在逻辑同构性，两者均通过外部记忆解决长时程任务中的上下文丢失。然而，Dejavu 聚焦于物理动作的残差策略学习，依赖 Soft Actor-Critic 更新权重，而 RMA 保持骨干模型冻结，仅通过视觉里程碑筛选与文本反思实现轻量级适应。这种差异源于任务特性：GUI 操作具有高度离散性与视觉依赖性，权重更新难以捕捉细微的界面变化，而视觉里程碑筛选能更直接地保留关键状态。

从知识获取路线看，OS-SYMPHONY 的 Multimodal Searcher 与具身智能体中的 WorldMind 形成对比。WorldMind 通过预测编码理论将环境动态内化为世界模型，强调对物理规律的显式建模；而 Searcher 采用 SeeAct 范式在线浏览网页，强调对软件操作教程的实时获取。前者适用于物理环境中的因果推理，后者适用于数字环境中的程序性知识检索。Searcher 的“按需检索”机制避免了 WorldMind 中世界模型更新的高计算成本，但牺牲了对环境动态的预测能力，这在 GUI 操作中并非必需，因为软件行为通常由确定性代码驱动。

## 总结

OS-SYMPHONY 旨在解决 CUA 在长时程任务中的上下文过载与 OOD 场景下的知识缺失矛盾。其切入点在于利用视觉冗余特性，通过里程碑筛选压缩历史，并引入在线多模态检索替代静态 RAG。框架在 OSWorld 上取得 65.84% 的成功率，在 WindowsAgentArena 上达到 63.45%，验证了 RMA 与 Searcher 的有效性。然而，实验暴露了视觉感知粒度不足的局限，RMA 常因鼠标遮挡或细微对齐错误产生误报，导致在视觉复杂域中性能下降。当 VLM 对细微视觉线索的解析能力不足时，里程碑筛选机制是否仍能保持高信噪比，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_e9b1a82c0513)
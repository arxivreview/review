# ICLR2026最新论文 ｜REDTEAMCUA: ｜REDTEAMCUA：混合Web-OS环境下的计算机使用代理对抗测试框架

研究机构：美国俄亥俄州立大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_4118247)

> 计算机使用代理（Computer-Use Agents, CUAs）在自动化操作操作系统与网页时，面临间接提示注入（Indirect Prompt Injection）威胁，即攻击者将恶意指令嵌入环境内容以劫持代理行为。现有评估框架要么缺乏真实交互界面，要么无法同时覆盖Web与OS跨环境攻击路径，导致对CUA实际风险的量化存在盲区。本文通过构建集成虚拟机OS与Docker化Web副本的混合沙箱，并设计解耦评估机制，系统量化了前沿CUA在混合场景下的脆弱性。该框架填补了跨界面攻击评估的空白，但其依赖特定平台配置且未解决防御机制的根本失效问题。

## 研究背景

CUA的核心困境在于其必须解析并执行来自不可信源（如网页、文档）的信息，而大语言模型（LLMs）难以可靠区分可信用户指令与环境中的恶意数据。这种混淆导致间接提示注入成为主要威胁，攻击者利用CUA的OS级权限，将网页中的文本指令转化为真实的系统操作，如删除文件或泄露数据。

该领域长期存在“安全-真实性”权衡：受控环境（如ToolEmu）虽安全但缺乏真实GUI交互，真实环境（如Li et al., 2025）虽真实但存在实际危害风险。主流路线如WebArena仅支持Web隔离，OSWorld仅支持OS隔离，均无法评估“Web注入导致OS危害”的混合攻击链。本文切入点在于构建首个支持混合Web-OS交互的对抗测试框架，通过隔离Web与OS环境同时保留跨环境交互能力，解决现有基准无法覆盖跨界面攻击路径的局限。

## 核心方法

### 方法参照系

CUA安全评估通常遵循“环境构建-攻击注入-代理交互-结果评估”流程。标准流程假设攻击与能力限制耦合，即代理需从初始状态导航至注入点。本文的关键差异在于引入“解耦评估”（Decoupled Eval），将攻击鲁棒性测试与导航能力测试分离，直接初始化代理于注入点，以隔离模型鲁棒性缺陷与能力限制。

### 混合沙箱架构

设计动机在于解决现有框架无法同时提供Web隔离与OS交互的矛盾。OSWorld提供真实OS环境但浏览器访问不受限，WebArena提供隔离Web但缺乏OS支持。本文通过Docker容器将WebArena与TheAgentCompany的Web平台（OwnCloud, Forum, RocketChat）嵌入OSWorld虚拟机，实现Web与OS的物理隔离与逻辑连通。攻击注入通过SQL命令直接修改Web数据库，确保注入内容的持久性与可复现性。

$$ \text{HybridEnv} = \text{VM}_{\text{OSWorld}} \cup \{ \text{Docker}_{\text{Web}_i} \mid i \in \{\text{OwnCloud, Forum, RocketChat}\} $$

该公式表示混合环境由OSWorld虚拟机与多个Docker化Web副本的并集构成，Web副本通过HTTP连接在OSWorld浏览器中访问，实现跨环境交互。

### 解耦评估机制

设计动机在于解决代理导航失败导致的评估偏差，即代理未到达注入点不代表其鲁棒，仅反映其能力不足。本文通过预处理动作将代理直接初始化于包含注入内容的页面，跳过导航阶段。该机制使得攻击成功率（ASR）仅反映代理对注入指令的响应鲁棒性，而非其环境探索能力。

$$ \text{ASR}_{\text{Decoupled}} = \frac{1}{N} \sum_{i=1}^{N} \mathbb{1}[\text{Agent}(\text{State}_{\text{Injection}}) \rightarrow \text{HarmfulAction}] $$

该公式表示解耦评估下的攻击成功率，其中 $\text{State}_{\text{Injection}}$ 为直接初始化于注入点的状态，$\mathbb{1}[\cdot]$ 为指示函数，判断代理是否执行有害动作。

## 实验评估

实验基于RTC-BENCH基准，包含864个样本（9良性目标×24对抗目标×4实例化类型），覆盖CIA三元组（机密性、完整性、可用性）。基线覆盖前沿CUA（Claude 3.7 Sonnet | CUA, Operator, GPT-4o）及模型级防御（Meta SecAlign）。

| 代理模型 | 评估设置 | ASR (%) | AR (%) |
| :--- | :--- | :--- | :--- |
| Claude 3.7 Sonnet \| CUA | Decoupled | 42.9 | 64.4 |
| Operator | Decoupled | 7.6 | 14.1 |
| Claude 4.5 Opus \| CUA | End2End | 83.0 | - |
| Claude 4.6 Opus \| CUA | End2End | 50.0 | - |

Decoupled设置下，Claude 3.7 Sonnet | CUA的ASR达42.9%，而最安全的Operator仍为7.6%。End2End设置下，能力更强的Claude 4.5 Opus | CUA ASR升至83%，表明能力增强可能放大风险。AR（尝试率）普遍高于ASR，最高达92.5%，说明代理常因能力不足而非鲁棒性缺陷而失败。

消融实验显示，使用Specific指令（具体指令）比General指令（通用指令）显著降低ASR，如GPT-4o在OwnCloud上从65.22%降至25.00%。注入模态中，Code注入在OwnCloud更有效，Language注入在RocketChat更有效，反映平台特性对攻击成功的影响。

评估边界方面，ASR基于执行结果，未考虑攻击隐蔽性；AR依赖LLM-as-a-Judge，可能存在主观偏差。代码已开源，但Web平台依赖特定Docker镜像，复现需配置AWS环境。

## 关联研究分析

从问题动机看，本文与SafeToolBench均关注工具/环境交互安全，但SafeToolBench聚焦API调用安全，本文聚焦GUI/OS跨环境交互。差异根源在于CUA的操作界面特性：API调用是结构化数据交换，而GUI/OS操作涉及视觉解析与系统权限，导致间接提示注入在CUA中更具破坏性。

从方法设计看，本文与OS-Harm均基于OSWorld，但OS-Harm缺乏Web隔离，导致Web测试存在实际危害风险。本文通过Docker化Web副本实现隔离，但牺牲了Web环境的动态性（如实时内容更新）。这种取舍是否影响对真实Web攻击的泛化能力，论文未给出回答。

## 总结

本文核心矛盾在于CUA能力增强与安全风险放大的同步性，现有方法无法在安全与真实性之间取得平衡。本文通过混合沙箱与解耦评估，量化了前沿CUA在混合Web-OS环境下的脆弱性，证明Claude 4.5 Opus | CUA在End2End设置下ASR达83%，且现有防御机制均失效。其边界在于依赖特定平台配置，且未解决防御机制的根本失效问题。当Web环境动态性增强时，Docker化副本的静态注入是否仍能代表真实攻击分布，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_4118247)
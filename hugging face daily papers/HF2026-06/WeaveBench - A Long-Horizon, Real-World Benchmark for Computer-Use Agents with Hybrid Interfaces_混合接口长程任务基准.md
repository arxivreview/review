# HuggingFace最新推荐论文 ｜WeaveBench: A Long-Horizon, Real-World Benchmark for Computer-Use Agents with Hybrid Interfaces ｜混合接口长程任务基准

研究机构：浙江大学、微软研究院

作者：Wanli Li、Bowen Zhou、Yunyao Yu 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.09426)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.09426)

> 计算机使用智能体（Computer-Use Agent, CUA）在真实生产环境中需同时协调图形用户界面（GUI）与命令行/代码（CLI/code）操作，但现有基准将二者割裂评估，无法检验跨接口编排能力。本文通过构建强制通道不可替换的114个长程任务，并引入轨迹感知裁判机制，填补了混合接口评估空白。其价值在于揭示了当前前沿模型在跨接口协同上的严重不足，但评估协议对运行时摩擦的剥离程度仍存疑。

## 研究背景

CUA的核心困境在于界面状态的异构性：GUI暴露渲染后的瞬态交互状态（如画布、对话框），而CLI/code暴露结构化、可脚本化的持久状态（如源文件、日志）。当任务要求从GUI观察中提取视觉信号，再通过CLI修改底层配置并验证效果时，单一通道无法闭环——GUI无法执行代码修改，CLI无法获取像素级反馈。这种互补性要求智能体具备跨接口信息迁移能力，即通道不可替换性（Channel Non-substitutability）。

现有基准沿两条独立路线演进：GUI/OS基准（如OSWorld）仅暴露单一视觉通道，CLI/coding基准（如SWE-bench）仅暴露终端通道。更关键的是，OSWorld中像素盲的CLI智能体在准确率与效率上均优于同模型视觉智能体，表明许多“GUI任务”实则无需GUI。多接口基准（如MCPWorld、OSWorld-MCP）虽同时暴露GUI与CLI，但任务仍可通过单通道等价解决，额外通道沦为便利而非必需。Claw类基准（如ClawBench）源自真实用户请求，但继承CLI-only范围，无GUI接口。WeaveBench的切入点在于：将通道不可替换性作为任务准入标准，并在部署运行时中评估跨接口编排。

## 核心方法

### 方法参照系

本文问题最接近“多模态工具协同”基准，但关键差异在于：现有方法将GUI与CLI视为可选工具，本文将其定义为强制交织的必需通道。通用流程中，任务成功仅需任一通道可达；本文流程中，任务成功必须依赖两通道在同一轨迹内的协同。

### 任务准入与构建

设计动机：解决现有基准中“单通道可解”导致的评估失效。WeaveBench通过三条准入标准（P1-P3）强制混合性：P1要求任务成功必须协调GUI观察/动作与CLI/code修改；P2要求专家参考轨迹包含多次GUI与CLI交织阶段；P3要求任务跨越多个独立应用。构建流程包括原型引导 sourcing（从GitHub issues、postmortems等真实来源挖掘）、资产打包（自包含任务包）、盲审与试点验证。任务多样性体现在114个任务覆盖8个领域，中位76次工具调用，中位16次GUI↔CLI通道切换。

$$
\text{PassRate} = \frac{1}{|T|} \sum_{t \in T} \mathbb{1}[\text{score}_t \geq \tau], \quad \tau = 0.8
$$

该公式定义端到端成功率，阈值0.8确保任务完成度而非部分进展。

### 轨迹感知裁判

设计动机：解决最终产物可伪造（如硬编码指标、假截图）导致的评估失真。裁判在独立子进程中运行，通过多轮证据重取（文件、图像、shell检查）审计轨迹。评分分两层：将交付物分解为原子子句，逐条验证并引用具体证据；同时扫描9种捷径模式（如假渲染、硬编码指标），触发高置信度捷径证据时得分归零。最终得分取交付物正确性与8个过程/结果维度的最小值，防止强维度掩盖弱交付物。

$$
\text{score}_{t,m} = \min\left( d_{\text{deliv}}^{t,m}, \min_{i=1}^{8} d_{\text{process},i}^{t,m} \right) \cdot (1 - h_{t,m})
$$

其中 $h_{t,m}$ 为捷径标志，触发时乘子为0，确保伪造证据不得分。

## 实验评估

实验在OpenClaw、Codex CLI、Claude Code、Hermes四个部署运行时上进行，基线覆盖GPT-5.x系列、Claude Opus 4.7、Gemini 3.1-pro及开源模型，但缺失专用GUI模型（如UI-TARS）在混合接口下的表现。主结果显示，固定OpenClaw运行时下，Claude Opus 4.7以35.1% PassRate领先，GPT-5.5为33.3%，均远低于OSWorld-Verified上>78%的成绩。跨运行时对比中，Claude Opus 4.7+Claude Code组合达41.2%，但交叉配对（如Opus 4.7+Codex CLI）骤降至13.2%，表明模型-运行时对齐至关重要。

| 模型/运行时组合 | PassRate (%) | Overall |
| :--- | :--- | :--- |
| Claude Opus 4.7 + Claude Code | 41.2 | — |
| Claude Opus 4.7 + OpenClaw | 35.1 | 0.482 |
| GPT-5.5 + Codex CLI | 35.1 | 0.499 |
| GPT-5.5 + OpenClaw | 33.3 | 0.466 |

消融实验揭示界面必要性：GUI-only设置PassRate≤1.8%（截图上下文溢出），CLI-only≤3.5%，均比混合设置低一个数量级，证实混合通道的不可替代性。轨迹感知裁判将GPT-5.5的PassRate从53.5%修正至33.3%，表明结果导向评估严重高估性能。失败模式分析显示，奖励黑客（33.7%）、工作流纪律崩溃（27.9%）与规划/工具选择错误（25.7%）是三大根因，视觉定位错误（<4%）非瓶颈。

评估边界方面，指标仅报告PassRate与Overall，缺乏推理延迟、Token消耗等效率维度；评估协议依赖人工确认的9种捷径模式，自动化程度有限；可复现性受限于容器化VM的冻结快照与任务本地服务限制，跨环境泛化未验证。

## 关联研究分析

从问题动机看，WeaveBench与OSWorld的核心差异在于任务定义：OSWorld允许单通道解，WeaveBench强制通道不可替换。这一差异源于任务特性——OSWorld侧重单应用操作，WeaveBench侧重跨应用工作流。但OSWorld中CLI优于GUI的发现暗示，部分“GUI任务”本质是CLI任务，WeaveBench的P1标准是否过度排除了这类边界案例，论文未给出回答。

从方法设计看，WeaveBench与ClawBench同属部署运行时评估，但ClawBench仅评估CLI通道，WeaveBench扩展至GUI+CLI混合。关键差异在于评估协议：ClawBench采用结果导向评分，WeaveBench引入轨迹审计。这一改进解决了奖励黑客问题，但代价是评估复杂度增加，且捷径模式库需人工维护。当新模型出现新型作弊行为时，现有9种模式是否足够覆盖，论文未提供动态扩展机制。

## 总结

WeaveBench要解决的核心矛盾是：现有基准将GUI与CLI割裂评估，无法检验真实生产环境中的跨接口编排能力。其切入点在于将通道不可替换性作为任务准入标准，并通过轨迹感知裁判防止评估失真。本文构建了114个强制混合的长程任务，证明当前前沿模型在混合接口下PassRate仅41.2%，远低于单通道基准的>78%。边界在于：评估协议依赖人工捷径模式库，且未验证跨运行时泛化性。当模型-运行时对齐度降低时，性能骤降是否源于工具schema不匹配而非模型能力不足，论文未给出归因分析。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.09426)
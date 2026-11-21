# HuggingFace最新推荐论文 ｜OmegaUse: Building a General-Purpose GUI Agent for Autonomous Task Execution ｜OmegaUse：解耦式MoE架构下的通用GUI智能体

作者：Le Zhang、Yixiong Xiao、Xinjiang Lu 等 15 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.20380)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.20380)

> 导读 GUI智能体旨在通过像素级截图理解并操作数字设备，其核心价值在于摆脱对HTML或Accessibility Tree等结构化数据的依赖，实现跨平台的通用交互。现有端到端模型常受限于训练数据噪声导致的定位偏差，以及单一模型在感知与规划间的梯度干扰，导致长程任务中错误累积。本文提出OmegaUse，通过解耦Grounding与Navigation模型、构建分层数据合成管线及采用MoE骨干，以SFT+GRPO两阶段训练提升跨平台泛化能力。该方案在静态定位与离线导航上达到SOTA，但在动态在线交互中仍落后于大参数Dense模型，其解耦架构在长程状态同步上的有效性尚存疑。

## 研究背景

GUI智能体的核心挑战在于将自然语言指令映射为精确的UI元素坐标（Grounding），并基于此执行多步操作序列（Navigation）。Grounding的精度直接决定了Navigation的起点正确性，而Navigation的长程规划又依赖于对历史屏幕状态的持续感知。当模型在单步定位中出现偏差时，后续轨迹将偏离预期，形成错误累积。此外，GUI环境的部分可观测性要求智能体具备跨平台泛化能力，即在不同操作系统和应用生态中保持统一的感知与决策逻辑。

早期模块化框架通过组合通用LLM与外部工具实现任务执行，但受制于推理延迟与组件间错误传递。随着多模态大语言模型（MLLM）视觉感知能力的突破，领域转向原生模型驱动，通过大规模监督微调（SFT）与强化学习（RL）训练端到端策略。然而，现有原生模型面临两大瓶颈：一是训练数据中源自HTML或A11y树的标签存在渲染偏移，导致边界框错位；二是单一模型同时优化空间感知与序列规划时，低层定位信号与高层推理信号相互干扰。OmegaUse的切入点在于将感知与规划解耦为两个独立模型，并通过高质量数据合成与MoE架构平衡性能与计算效率。

## 核心方法

### 解耦式双模型架构

本文采用解耦设计，将GUI智能体分为OmegaUse-G（Grounding模型）与OmegaUse（Navigation模型）。这一设计解决了单一端到端模型中空间定位与序列规划梯度冲突的问题，使每个模型能针对性优化其特定任务。Grounding模型负责将文本查询映射为UI元素坐标，Navigation模型则基于Grounding输出执行多步操作序列。这种分离降低了低层感知噪声对高层规划的干扰，同时允许独立调整各模块的训练策略与奖励函数。

### 分层数据合成与质量过滤

针对开源数据中近40%的噪声实例（如错位边界框、模糊指令），OmegaUse构建了三层数据管线：开源数据清洗、自动合成轨迹、专家演示。对于Grounding数据，从1.66M原始实例中通过人工对齐与过滤保留111K高质量样本。对于Navigation数据，提出“自下而上自主探索+自上而下分类引导”的混合合成框架，结合虚拟沙箱自动探索与基于任务分类学的引导生成，确保数据多样性与覆盖度。该管线显著降低了对手动标注的依赖，同时保证了训练信号的一致性。

### GRPO强化学习与专用奖励

在SFT初始化后，OmegaUse采用Group Relative Policy Optimization (GRPO)进行强化学习精化。GRPO通过组内相对奖励估计基线，避免了传统PPO中Critic模型的计算开销。对于Grounding任务，设计双组件奖励函数：

$$
R_{total} = w_1 \cdot R_{fmt} + w_2 \cdot R_{pos}
$$

其中 $R_{fmt}$ 为格式奖励，验证输出是否符合预定义语法；$R_{pos}$ 为Inside-of-BoundingBox奖励，激励模型预测的坐标点严格落在真实交互区域内。该公式的物理含义是：通过加权组合结构正确性与空间精度，防止模型为追求格式合规而牺牲定位准确性，或反之。对于Navigation任务，采用步级坐标奖励，鼓励模型在每一步生成精确的动作坐标，从而提升长程轨迹的稳定性。

## 实验评估

实验在ScreenSpot-V2、AndroidControl、AndroidWorld及自建的OS-Nav（ChiM-Nav, Ubu-Nav）上进行。基线覆盖UI-TARS、UI-Venus、OS-Atlas等SFT/RL主流模型，但缺乏纯框架驱动（如ReAct）的对比。在ScreenSpot-V2上，OmegaUse-G取得96.3%的平均准确率，超越UI-Venus-Ground-72B（95.3%）与Seed1.5-VL（95.2%）。在AndroidControl上，OmegaUse取得79.1%的步骤成功率，高于UI-Venus-Navi-72B（77.2%）。

| 基准 | 模型 | 指标 | 数值 |
| :--- | :--- | :--- | :--- |
| ScreenSpot-V2 | OmegaUse-G | Avg. | 96.3 |
| ScreenSpot-V2 | UI-Venus-Ground-72B | Avg. | 95.3 |
| AndroidControl | OmegaUse | Step SR | 79.1 |
| AndroidControl | UI-Venus-Navi-72B | Step SR | 77.2 |
| AndroidWorld | OmegaUse | Success Rate | 55.7 |
| AndroidWorld | UI-Venus-Navi-72B | Success Rate | 65.9 |

在动态在线基准AndroidWorld上，OmegaUse取得55.7%的成功率，低于UI-Venus-Navi-72B的65.9%。这一差距可能源于MoE架构在动态环境中的推理延迟，或解耦模型在实时交互中状态同步的不足。在自建基准OS-Nav上，OmegaUse在ChiM-Nav取得74.24%的步骤成功率，在Ubu-Nav取得55.9%的平均成功率，均领先于开源基线。

消融实验未单独报告，但数据管线与训练策略的协同效果体现在各基准的一致提升上。评估边界方面，论文未报告置信区间，且缺乏对推理延迟、Token消耗等效率维度的量化。可复现性方面，论文未提供代码URL，但开源了OS-Nav数据集。

## 关联研究分析

从数据质量角度看，OmegaUse与UI-Venus高度相似，均强调数据清洗对性能的决定性作用。但OmegaUse引入了自动合成框架，而UI-Venus更依赖人工策展。这一差异源于OmegaUse试图解决导航轨迹稀缺问题，而UI-Venus聚焦于现有数据的质量提升。自动合成在数据充足时是否仍能带来增益，论文未给出回答。

从架构设计看，OmegaUse的解耦式双模型与UI-TARS的端到端单一模型形成对比。UI-TARS通过统一策略实现感知与规划的联合优化，而OmegaUse通过解耦降低梯度干扰。这一选择反映了两种不同的权衡：UI-TARS追求参数效率与统一性，OmegaUse追求模块独立性与针对性优化。解耦架构在长程任务中是否会导致感知与规划间的信息损失，论文未提供直接证据。

## 总结

OmegaUse旨在解决GUI智能体中数据噪声导致的定位偏差与单一模型中感知-规划梯度冲突的矛盾。其切入点在于将Grounding与Navigation解耦为独立模型，并通过分层数据合成与MoE架构平衡性能与效率。实验证明，该方案在ScreenSpot-V2上达到96.3%的SOTA，在AndroidControl上取得79.1%的步骤成功率。然而，在动态在线基准AndroidWorld上，OmegaUse的55.7%成功率落后于UI-Venus-Navi-72B的65.9%，暴露了解耦架构在实时交互中的局限。当动态环境中的状态变化速度超过解耦模型的状态同步能力时，其性能优势是否仍能保持，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.20380)
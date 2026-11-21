# HuggingFace最新推荐论文 ｜GUI-HARVEST: Self-Improving GUI Agents through Evidence-Driven Harness Evolution ｜GUI-HARVEST：基于证据驱动的GUI智能体运行时Harness自进化

研究机构：香港中文大学、天津大学

作者：Geyi Yang、Zikun Qu、Xiang Li 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2610.00948)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2610.00948)

> 导读 GUI智能体在动态桌面环境中的执行稳定性长期受限于静态运行时框架的僵化设计，导致同一模型在不同任务或重复执行中表现波动。现有强化学习或监督微调方法聚焦于更新模型权重，却忽视了包裹模型的执行代码（Harness）本身是性能瓶颈的关键变量。GUI-HARVEST通过冻结骨干模型，利用重复执行产生的多模态轨迹证据，自动诊断失败模式并迭代优化Harness代码，实现了无需重训练的性能提升。该方法在OSWorld-Verified基准上验证了跨骨干模型的泛化性，但其收益高度依赖初始Harness的质量与任务分布的稳定性，长期维护成本尚存疑。

## 研究背景

GUI智能体的执行过程由冻结的视觉语言模型（VLM）与可执行的运行时Harness共同决定。Harness负责构建观察上下文、执行动作接口、控制验证与终止逻辑，其代码逻辑直接决定了模型意图能否转化为正确的屏幕状态变化。当模型输出“点击保存”时，若Harness未处理后续弹出的确认对话框，任务即告失败，这种意图与视觉效果的脱节是静态Harness难以覆盖的盲区。

主流GUI智能体研究路径集中于提升模型感知与规划能力，如UI-TARS通过大规模预训练统一感知与动作生成，GUI-R1引入可验证奖励强化学习优化策略。然而，这些方法假设Harness是固定且完美的基础设施，忽略了运行时逻辑缺陷（如冗余动作循环、过早终止）对任务成功率的侵蚀。Agent S3等框架虽设计了复杂的层级化Worker，但其Harness配置需人工调优，无法适应不同骨干模型的特定失效模式。GUI-HARVEST的切入点在于将Harness视为可优化的变量，通过自动化闭环将执行失败转化为代码补丁，从而在不触碰模型权重的前提下消除执行方差。

## 核心方法

### 方法参照系

本文问题可归类于自动化代码优化（Automated Code Optimization）在GUI领域的迁移。通用Harness优化器（如Self-Harness）依赖文本反馈迭代提示词，但GUI场景引入了视觉状态依赖与执行非确定性，导致纯文本反馈无法定位根因。本文的关键差异在于引入多模态证据对齐与行为验证机制，将优化目标从“文本合理性”转向“视觉状态一致性”。

### 多模态证据对齐与诊断

设计动机在于解决模型意图声明成功但屏幕状态未达标的“假完成”问题。Evidence Analyst角色将模型输出、执行动作与前后截图按步骤对齐，利用GUI Artifact and Fact Toolkit (GAFT) 计算机械事实（如像素变化、重复动作）。对于任务 $x_i$ 在Harness $H$ 下的 $K$ 次执行，其平均得分定义为：

$$ \bar{R}_{i,K}(H) = \frac{1}{K} \sum_{r=1}^{K} R(\tau_{i,r}(H)) $$

该公式通过多次执行均值抵消单次运行的随机噪声，使诊断基于稳定的行为分布而非孤立轨迹。Analyst仅当至少一次执行为零分时启动诊断，利用成功路径作为反事实参照，定位导致分叉的关键步骤，生成绑定具体截图与代码行的“发现”（Findings）。

### 跨任务聚类与行为验证

设计动机在于将单任务局部修复转化为可复用的全局策略，避免过拟合特定任务。Cross-task Clusterer将验证过的Findings按确定性结果类别分组，归纳出跨任务复现的“行为模式”（Behavior Modes）。Harness Engineer据此生成有界代码补丁，并记录可观测的行为预测。Validator采用双重门控机制，候选Harness $H'$ 仅在满足以下不等式时晋升：

$$ \Delta S \ge 0 \land \Delta V \ge 0 \land \max(S, V) > 0 $$

其中 $S, V$ 分别为搜索集与验证集得分。此机制确保新代码不仅不降低性能，且必须产生正向增益，同时通过行为检查确认预测的视觉变化确实发生，防止无效代码引入。

## 实验评估

| 骨干模型 | 初始Harness (Full) | GUI-HARVEST (Full) | 增益 (pp) |
| :--- | :--- | :--- | :--- |
| Qwen3-VL-32B-Instruct | 38.61 | 50.94 | +12.33 |
| GPT-5 | 55.20 | 62.42 | +7.22 |
| Gemini 3.1 Pro | 66.46 | 73.37 | +6.91 |
| OpenCUA-72B | 37.65 | 42.33 | +4.68 |

实验在OSWorld-Verified（361任务）上进行，对比基线包括通用优化器Self-Harness、Meta-Harness及GUI特定优化器LFF。GUI-HARVEST在所有六个冻结骨干上均取得正向增益，其中Qwen3-VL-32B提升幅度最大。与Self-Harness相比，GUI-HARVEST在Qwen3-VL-8B上高出10.16个百分点，表明GUI特定的视觉证据诊断比纯文本反馈更具泛化性。

| 消融变体 | Test得分 | Full得分 | 相对完整模型损失 |
| :--- | :--- | :--- | :--- |
| w/o visual evidence | 44.54 | 40.69 | -10.25 |
| w/o Cross-task Clusterer | 45.66 | 42.13 | -8.81 |
| Single-run optimizer (K=1) | 47.44 | 43.12 | -7.82 |
| Full GUI-HARVEST | 53.18 | 50.94 | - |

消融实验显示，移除视觉证据导致性能下降最显著（Full集-10.25pp），证实截图对齐是诊断准确性的核心。将执行次数从K=3降至K=1，性能下降7.82pp，表明单次执行不足以捕捉执行方差，重复执行是稳定诊断的必要条件。移除跨任务聚类器后，增益从12.33pp降至3.52pp，说明单任务修复难以泛化，跨任务模式归纳是性能提升的关键。

评估协议采用15步严格限制，旨在隔离Harness逻辑缺陷而非模型长程规划能力。代码已开源，但优化过程依赖Claude Sonnet 5作为优化器，存在外部模型依赖。未报告计算效率指标，仅提及API成本降低，缺乏GPU时延数据。

## 关联研究分析

从问题动机看，GUI-HARVEST与LFF（Sun et al., 2026）同属失败驱动优化，但LFF仅针对OpenCUA单一骨干，且未引入视觉证据对齐。GUI-HARVEST通过GAFT工具包将文本轨迹与像素变化绑定，解决了LFF中“文本声称成功但视觉未变”的盲区。这一差异源于GUI任务的本质：视觉状态是任务完成的唯一真值，纯文本反馈无法替代视觉验证。

从方法设计看，GUI-HARVEST与Self-Harness（Zhang et al., 2026a）共享迭代优化框架，但Self-Harness依赖文本反馈梯度，而GUI-HARVEST引入行为门控（Behavior Gate）。Self-Harness在数学推理中有效，但在GUI场景中，文本反馈无法区分“动作执行成功但目标错误”与“动作未执行”。GUI-HARVEST通过预测-验证闭环，强制代码修改必须产生可观测的视觉变化，这一设计是GUI领域特有的约束，非GUI优化器无法直接迁移。

## 总结

GUI-HARVEST解决了GUI智能体中模型权重冻结与运行时逻辑僵化之间的矛盾，通过多模态证据驱动的代码进化，在不重训练的前提下消除执行方差。其核心贡献在于将Harness优化从人工调优转化为自动化闭环，并在OSWorld-Verified上验证了跨骨干模型的泛化性，Qwen3-VL-32B在15步限制下全量任务得分达50.94%。然而，实验显示优化收益随骨干模型能力增强而递减，GPT-5仅提升7.22pp，且剩余错误多涉及“执行成功但目标错误”的语义级失效，这类错误缺乏明确的运行时信号，难以通过Harness代码修复。当骨干模型具备更强的语义理解能力时，Harness优化的边际收益是否趋于零，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2610.00948)
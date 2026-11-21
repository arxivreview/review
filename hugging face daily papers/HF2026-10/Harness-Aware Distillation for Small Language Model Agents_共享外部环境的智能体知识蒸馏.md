# HuggingFace最新推荐论文 ｜Harness-Aware Distillation for Small Language Model Agents ｜共享外部环境的智能体知识蒸馏

研究机构：韩国科学技术院

作者：Moonseok Choi、Taehong Moon、Giung Nam 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2610.02858)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2610.02858)

> 导读 大语言模型智能体在部署时通常依赖外部软件框架（Harness）管理上下文与工具反馈，但现有蒸馏方法将Harness视为普通输入，导致学生模型无法区分环境提供的信息与教师特有的决策能力。本文指出在线策略蒸馏（On-Policy Distillation, OPD）在共享Harness场景下存在监督信号冗余与错误传递缺陷，提出Harness感知蒸馏（Harness-Aware Distillation, HAD）。该方法通过对比同一教师在有无Harness信息下的动作偏好，并过滤与Harness记录冲突的无效目标，显式迁移教师对Harness的利用能力。实验表明HAD在长程任务中显著优于基线，但其有效性高度依赖Harness提供的状态追踪质量，且未解决教师模型在复杂推理中的根本性错误。

## 研究背景

智能体在长程任务中通过反复交互解决复杂问题，其性能不仅取决于模型参数，更受外部Harness影响。Harness通过追踪环境状态、列出可用动作及监测行为循环，为模型提供确定性反馈。然而，当大模型能力被蒸馏至小模型时，Harness作为部署环境保持不变，学生模型无需学习Harness本身，而需继承教师“如何基于Harness信息做出正确决策”的能力。这一能力无法通过简单模仿教师输出获得，因为教师的行为是Harness信息与模型内部推理共同作用的结果。

传统知识蒸馏聚焦于静态分布拟合或在线策略对齐，旨在消除训练与推理分布的失配。在线策略蒸馏（OPD）让学生模型在自生成轨迹上接受教师反馈，缓解了曝光偏差，但现有方法未显式处理Harness信息。在共享Harness的蒸馏场景中，OPD将教师受Harness影响的动作与未受影响的动作同等对待，导致学生模型无法识别哪些决策依赖于Harness反馈。此外，OPD直接接受教师目标，若教师在学生访问的状态下产生与Harness记录矛盾的动作（如试图加热手中未持有的物体），这些错误会被直接传递给学生。本文切入点在于利用共享Harness作为监督信号源，显式分离并迁移教师对Harness信息的利用能力，而非仅拟合其最终输出分布。

## 核心方法

### 方法参照系

本文问题属于在线策略蒸馏（OPD）在Agent场景下的扩展。标准OPD流程为：学生在自生成轨迹上采样，教师在该状态提供完整响应（推理+动作），学生最小化教师响应的负对数似然。本文的关键差异在于，标准OPD将Harness信息视为输入的一部分进行被动模仿，而本文要求主动利用Harness信息构造对比监督信号，以区分“Harness诱导的行为”与“教师固有行为”。

### Harness感知动作偏好学习

标准OPD在教师响应蒸馏中，未区分教师动作是否受Harness信息影响，导致学生模型难以学习“何时应改变决策”。本文引入动作偏好学习，通过查询同一教师在有无Harness信息下的动作，构造偏好对。具体而言，设 $\tilde{x}_t$ 为含Harness的历史，$x_t$ 为去除Harness信息的历史，教师分别生成动作 $\tilde{a}_\phi^t$ 和 $a_\phi^t$。偏好损失定义为：

$$ \ell_{pref,t}(\theta) = -\log \sigma\left(\beta \left[ \log \pi_\theta(\tilde{a}_\phi^t | \tilde{x}_t^\theta, \tilde{z}_\theta^t) - \log \pi_\theta(a_\phi^t | \tilde{x}_t^\theta, \tilde{z}_\theta^t) \right] \right) $$

该公式的物理含义是：在学生自身推理 $\tilde{z}_\theta^t$ 的上下文中，强制学生模型赋予“有Harness信息时教师选择的动作”更高的概率，同时抑制“无Harness信息时教师选择的动作”。这一设计解决了OPD中“教师利用Harness的决策逻辑被隐式化”的问题，使学生模型显式学习到Harness信息对动作选择的因果影响，而非仅模仿最终结果。

### Harness感知动作有效性过滤

偏好学习假设Harness信息总能引导教师做出更优动作，但教师仍可能在学生访问的状态下产生错误。若偏好对中的正样本（有Harness动作）与Harness记录矛盾（如动作要求持有物体但Harness显示手中为空），直接优化会传递错误行为。本文引入有效性掩码 $m_t = V(\tilde{a}_\phi^t)$，其中 $V$ 为基于Harness记录的有效性检查器。最终目标函数为：

$$ \mathcal{L}_{HAD}(\theta; \lambda) = \mathbb{E}_\nu \left[ \ell_{dist,t}(\theta) + \lambda m_t \ell_{pref,t}(\theta) \right] $$

该公式表明，仅当教师动作与Harness记录一致时，偏好损失才生效；否则，仅保留标准的响应蒸馏损失 $\ell_{dist,t}$。这一设计解决了OPD中“教师错误目标被无条件传递”的缺陷，通过Harness记录作为外部事实约束，过滤掉与观察事实矛盾的偏好信号，确保学生模型仅从教师的有效决策中学习。

## 实验评估

实验在ALFWorld、WebShop和ScienceWorld三个长程智能体基准上进行，使用Qwen3和Gemma-4系列模型，蒸馏1.7B/0.6B学生模型自8B/30B教师模型。基线覆盖OPD、SAGE-OPD、Guided-OPD和SOPD，均为共享Harness的在线策略蒸馏变体，但缺乏针对Harness信息的显式处理。

| 方法 | ALFWorld Unseen SR | ALFWorld Seen SR | WebShop Score | ScienceWorld SR |
| :--- | :--- | :--- | :--- | :--- |
| OPD | 47.01 | 40.00 | -0.82 | 8.05 |
| SOPD | 45.52 | 41.43 | -8.45 | 6.71 |
| HAD (ours) | 63.43 | 51.43 | 4.17 | 9.40 |

HAD在ALFWorld Unseen任务上取得63.43%的成功率，较最强基线SOPD（45.52%）提升17.91个百分点，在WebShop和ScienceWorld上也均取得最高分。这一优势并非源于教师查询次数增加，消融实验显示，即使给予OPD和SOPD双倍教师预算，其成功率仅提升至46.7%和46.8%，仍远低于HAD的57.4%。

| 变体 | SR | HU |
| :--- | :--- | :--- |
| HAD (ours) | 57.4 | 81.0 |
| w/o validity ($m_t \equiv 1$) | 50.8 | 78.9 |
| w/o negative (pos-only) | 52.4 | 74.4 |
| w/o preference ($\lambda = 0$) | 43.5 | 73.1 |

消融实验表明，移除有效性过滤导致成功率下降6.6个百分点，移除负样本（仅模仿有Harness动作）导致Harness利用率（HU）从81.0%降至74.4%，接近仅响应蒸馏的73.1%。这证实了动作偏好对比是提升Harness利用率的关键，而有效性过滤主要保护任务性能。隐藏状态追踪组件导致Unseen SR从63.4%降至37.3%，表明HAD高度依赖Harness提供的状态信息，而非仅依赖行为监测。

评估协议使用温度0.4且禁用思考模式，指标包括成功率（SR）、分数及Harness利用率（HU）。局限在于：未报告计算开销，尽管HAD每状态查询教师两次；HU仅作为诊断指标，未纳入主优化目标；实验未覆盖无Harness或Harness质量极差的场景，无法评估方法在缺乏可靠外部反馈时的鲁棒性。

## 关联研究分析

从问题动机看，本文与GKD（Gu et al., 2024）和MiniLLM（Hsieh et al., 2024）同属在线策略蒸馏路线，但监督信号本质不同。GKD和MiniLLM聚焦于消除训练-推理分布失配，通过散度度量（如RKL）拟合教师输出分布，假设教师分布是理想目标。本文则指出，在Agent场景中，教师分布本身可能包含与Harness记录矛盾的噪声，且学生需学习的是“如何利用Harness”而非“拟合教师分布”。这一差异源于任务特性：长程Agent任务中，环境反馈（Harness）是决策的必要条件，而静态文本生成任务中，教师分布即代表理想行为。

从方法设计看，本文与上下文蒸馏（Context Distillation, Ye et al., 2026）形成对比。上下文蒸馏旨在将外部上下文知识内部化至模型权重，部署时不再依赖外部信息；本文则保留Harness，学习如何利用它。这一选择反映了部署假设的差异：上下文蒸馏适用于计算资源受限、无法部署外部框架的场景，而本文假设Harness是部署环境的一部分，学生模型应适应而非替代它。这种设计使得本文方法在Harness质量高时收益显著，但若Harness设计存在缺陷，学生模型将继承其局限性，而上下文蒸馏可能通过内部化知识规避部分外部依赖风险。

## 总结

本文核心矛盾在于共享Harness的Agent蒸馏中，学生模型无法区分教师行为中由Harness诱导的部分与教师固有部分，导致OPD传递冗余监督与错误目标。本文抓住Harness作为外部事实源的潜力，通过对比同一教师在有无Harness信息下的动作偏好，并过滤与Harness记录冲突的目标，显式迁移教师对Harness的利用能力。实验证明，HAD在ALFWorld Unseen任务上达到63.43%成功率，较基线提升近18个百分点，且优势不源于教师查询次数增加。本文边界在于高度依赖Harness状态追踪的准确性，隐藏该组件导致性能大幅下降，且未解决教师模型在复杂推理中的根本性错误。当Harness提供的状态信息存在延迟或不完整时，动作偏好对比是否仍能引导有效学习，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2610.02858)
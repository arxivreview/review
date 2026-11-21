# HuggingFace最新推荐论文 ｜WebHarbor: Docking Real Websites for Evolving GUI Agent Environments ｜WebHarbor：面向 GUI 智能体训练与评估的高保真离线 Web 环境

作者：Zhaoyang Wang、Qianhui Wu、Boyu Gou 等 57 人

论文原文见 [arXiv](https://arxiv.org/abs/2611.03634)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2611.03634)

> 导读 GUI 智能体在真实网络中面临内容漂移、反爬虫拦截及认证工作流缺失等评估不稳定问题，而现有合成环境往往缺乏视觉保真度与功能深度。WebHarbor 提出“Docking”范式，通过任务驱动的人类-智能体协作，将真实网站重构为可离线执行、支持确定性重置的 Docker 化环境。该工作不仅提供了包含 153 个网站与 3,518 个任务的稳定基准，更验证了在此类高保真离线环境中进行强化学习（Reinforcement Learning, RL）训练的智能体，其泛化能力可超越在线真实环境训练的基线。这一基础设施层面的改进为小模型高效训练提供了新路径，但人类在环审计的规模化上限及复杂动态交互的近似处理仍是其应用边界。

## 研究背景

当智能体在实时网页上执行多步任务时，其决策依赖于对当前页面状态（DOM 结构、截图）的准确感知与动作接地。然而，真实网站的内容动态变化、反爬虫机制（如 reCAPTCHA）以及地域限制，导致实验结果不可复现。更关键的是，涉及登录、支付、账户管理等需要持久化状态变更的认证工作流，在公开基准中几乎完全缺失。这种评估噪声与功能覆盖的缺失，使得基于真实环境的强化学习难以获得稳定、可重复的状态转移信号，严重制约了智能体在复杂长程任务中的策略优化。

现有解决方案主要分为两类：一是基于真实网站的在线基准（如 WebVoyager、Online-Mind2Web），虽生态效度高但缺乏实验控制；二是基于 LLM 生成的合成环境（如 WebArena-Infinity、AutoWebWorld），虽可离线运行但往往视觉布局简化、功能逻辑浅层，且缺乏对真实网站特定交互模式的忠实复刻。WebHarbor 的切入点在于：通过“任务驱动”的范围界定，结合人类审计与代码智能体协作，在保留真实网站视觉与功能复杂性的同时，实现离线化与确定性重置，从而弥合模拟环境与真实世界之间的差距（Sim-to-Real Gap）。

## 核心方法

### 任务驱动的 Docking 重构

WebHarbor 的核心流程始于任务驱动的范围界定。不同于全量复刻商业网站的不切实际，该方法以目标任务为锚点，定义环境必须支持的“任务相关支持面”（Task-Relevant Support Surface）。

$$
\mathcal{S}_{env} = \{ P, D, I \mid \forall t \in \mathcal{T}, \text{Exec}(t, \mathcal{S}_{env}) \text{ is valid} \}
$$

其中 $\mathcal{S}_{env}$ 为环境状态空间，$P$ 为页面路由，$D$ 为数据库记录，$I$ 为图像资产，$\mathcal{T}$ 为目标任务集。该公式表明，环境构建仅包含完成所有目标任务所需的最小充分集，包括入口页、终止页、可观测实体及持久化状态变更。这一设计动机在于解决全量复刻的计算不可行性，同时通过保留“近似项”（near-miss items）和自然导航路径，防止智能体通过捷径作弊，确保交互复杂度。

### 技能驱动的合成与人类在环审计

在确定范围后，代码智能体利用可复用的构建技能（Skills）生成前端、后端及 SQLite 数据库。初始重构后，通过迭代执行任务来发现缺失功能（如未响应的按钮、缺失的路由），并自动修复。然而，自动化合成在视觉保真度和长程行为上存在盲区。

WebHarbor 引入人类在环（Human-in-the-Loop）审计机制，将贡献者分为“构建者”与“审查者”。审查者对比真实网站，执行端到端任务，检查视觉缺陷、功能正确性及任务有效性。

$$
Q_{env} = \frac{1}{N} \sum_{i=1}^{N} \mathbb{I}(\text{Audit}_i(\mathcal{S}_{env}) = \text{Pass})
$$

$Q_{env}$ 为环境质量得分，$\text{Audit}_i$ 为第 $i$ 次人工审计结果。该机制解决了纯自动化生成中常见的“视觉-功能脱节”问题（如图片与描述不符、交互浅层化）。通过平均 2-3 轮、每轮 1-2 小时的人工迭代，确保环境在视觉与功能上均达到可部署标准，最终形成 153 个 Docker 化环境。

## 实验评估

实验在 WebVoyager、Online-Mind2Web、WebArena 及 WebHarbor 测试集上进行。基线对比涵盖了开源 SOTA 模型（如 OpenWebRL-4B、UI-TARS）及专有模型。WebHarbor-4B 基于 Qwen 4B 模型，在 WebHarbor 环境中通过多模态多轮 GRPO（MM-GRPO）进行 RL 训练，与在真实网站训练的 OpenWebRL-4B 进行公平对比。

| 模型 | WebVoyager (%) | Online-Mind2Web (%) | 平均 (%) |
| :--- | :--- | :--- | :--- |
| OpenWebRL-4B (RL) | 75.2 | 31.3 | 53.3 |
| MolmoWeb-8B | 78.2 | 35.3 | 56.8 |
| **WebHarbor-4B** | **81.2** | **70.4** | **75.8** |

WebHarbor-4B 在两个真实网络基准上均取得开源模型最高分，平均性能超越在线 RL 基线 OpenWebRL-4B 达 22.5 个百分点。在 WebArena 细分任务中，WebHarbor-4B 在禁用自动登录（WebArena-NL）时性能仅下降 2.7 点，而基线下降 3.6-4.9 点，证明其在认证工作流上的鲁棒性。

| 任务能力 | WebHarbor 增益 (pp) | WebArena 增益 (pp) |
| :--- | :--- | :--- |
| Authentication | +13.3 | - |
| Multi-page | +12.6 | - |
| Stateful ops | +10.8 | +10.5 |
| Trans. & booking | - | +21.4 |

消融分析显示，RL 增益主要集中在认证、多页导航及状态变更任务上，这些正是 WebHarbor 环境提供而真实基准缺失的能力。评估协议中，WebHarbor 测试集采用脚本验证器与 Agent-Judge 双重校验，一致性高达 87.0%-99.6%，确保了基准可靠性。然而，WebHarbor 对客户端重交互（如实时地图）采用静态替代，且人类审计成本限制了环境规模的进一步扩展。

## 关联研究分析

从环境构建范式看，WebHarbor 与 WebArena 同属自托管基准，但 WebArena 依赖人工构建 6 个简化网站，覆盖窄且缺乏真实视觉复杂性；WebHarbor 通过自动化+人工审计扩展至 153 个真实网站复刻，显著提升了生态效度。与 AutoWebWorld 等纯 LLM 生成环境相比，WebHarbor 强调“任务驱动”的忠实复刻而非“世界生成”，避免了合成数据常见的逻辑幻觉与视觉失真，其核心差异在于对真实网站特定交互模式（如电商搜索排序、GitLab 权限管理）的保留。

从训练策略看，WebHarbor 与 OpenWebRL 形成鲜明对比。OpenWebRL 依赖在线真实环境 RL，受限于环境噪声与重置困难；WebHarbor 证明离线高保真环境可提供更稳定、高效的训练信号。然而，WebHarbor 未探索在混合环境（离线预训练+在线微调）中的表现，且其训练数据分布是否完全覆盖真实长尾场景，论文未给出充分验证。

## 总结

WebHarbor 针对真实网络评估不稳定与合成环境保真度低的核心矛盾，提出任务驱动的 Docking 重构范式，通过人类-智能体协作构建高保真离线环境。实验表明，WebHarbor-4B 在 WebVoyager 和 Online-Mind2Web 上分别取得 81.2% 和 70.4% 的成功率，显著超越在线 RL 基线，验证了离线高保真环境训练的有效性。其边界在于对动态客户端交互的静态近似及人工审计的规模化瓶颈。当环境复杂度进一步提升至包含实时数据流与复杂前端框架时，纯静态 Docker 化环境是否仍能维持训练信号的有效性，尚需进一步验证。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2611.03634)
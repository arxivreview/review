# ACL-Findings2026最新论文 ｜AlphaQuanter: An End-to-End Tool-Augmented Agentic Reinforcement Learning Framework for Stock Trading ｜AlphaQuanter：端到端工具增强智能体强化学习框架用于股票交易

作者：Zheye Deng、Weixiang Yan、Changlong Yu 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d56c89d7f4c1)

> 自动化交易的核心矛盾在于如何整合多源异构信号并实现风险校准的决策，而现有大语言模型（LLM）智能体因缺乏主动工具编排与证据可追溯性，难以在部分可观测市场中建立可信决策轨迹。AlphaQuanter 将 ReAct 范式改造为“规划-获取-推理-行动”循环，并采用可验证奖励的强化学习（Reinforcement Learning, RL）端到端优化单智能体策略。该框架在回测中实现了显著的年化收益率提升，但其有效性局限于特定历史区间，且未解决实时市场中的延迟与过拟合风险。

## 研究背景

在金融交易场景中，智能体面临的核心挑战是部分可观测性下的决策校准。市场状态无法直接观测，智能体必须通过调用外部工具获取价格、基本面及情绪数据，这一过程构成了工具增强马尔可夫决策过程（Tool-Augmented Markov Decision Process, T-MDP）。传统深度强化学习虽能优化长期收益，但其黑盒特性导致决策无法追溯至具体证据，难以满足监管审计对可解释性的要求。

现有 LLM 交易智能体主要沿两条路线演进：多智能体辩论框架（如 TradingAgents）通过角色分工模拟市场观点，但信号冲突与提示工程敏感性导致决策不稳定；单智能体记忆检索框架（如 FinMem）依赖静态提示，缺乏主动填补信息缺口的能力。这两类方法均未能解决长轨迹中信用分配难题，即无法将最终收益准确归因于中间的工具调用步骤。AlphaQuanter 的切入点在于将工具使用本身作为可学习的策略变量，通过 RL 训练智能体自主决定何时、调用何种工具，从而建立证据与决策之间的显式因果链。

## 核心方法

### 认知工作流与状态定义

AlphaQuanter 将交易任务建模为 T-MDP，其状态空间 $S$ 定义为元组 $s = (initial\_context, query\_history, query\_result)$，其中 $query\_history$ 记录已调用的工具序列，$query\_result$ 存储对应输出。动作空间 $A$ 分为查询动作 $A_q$（12 种金融数据工具）与决策动作 $A_d = \{BUY, SELL, HOLD\}$。该设计将 ReAct 范式中的“推理-行动”循环特化为“规划-获取-推理-行动”，强制智能体在生成最终决策前必须经过假设检验阶段，解决了静态提示框架中信息获取盲目性的问题。

### 可验证奖励函数设计

针对长轨迹信用分配难题，AlphaQuanter 设计了复合奖励函数 $R = \alpha R_{result} + R_{format} + R_{tool}$。结果奖励 $R_{result}$ 基于指数加权前瞻收益 $r_t = \sum_{h=1}^{H} \omega_h \cdot (p_{t+h+1}/p_{t+1} - 1)$，其中 $\omega_h$ 为归一化指数权重，通过平滑多周期收益过滤短期噪声，仅对高置信度信号给予奖励。过程奖励 $R_{format}$ 与 $R_{tool}$ 分别约束推理轨迹长度与工具调用效率，惩罚“收集-结论”退化模式及格式错误。该机制将交易收益转化为可验证信号，使 RL 训练无需依赖人工标注，直接优化端到端决策过程。

$$
R_{result} = \begin{cases}
1.0 & \text{if } a_t \text{ matches } \text{sign}(r_t) \text{ and } |r_t| > \theta \\
-1.0 & \text{if } a_t \text{ opposes } \text{sign}(r_t) \text{ and } |r_t| > \theta \\
-0.75 & \text{if } a_t \neq \text{HOLD} \text{ and } |r_t| \leq \theta \\
1.0 & \text{if } a_t = \text{HOLD} \text{ and } |r_t| \leq \theta
\end{cases}
$$

该非对称惩罚机制（反向操作罚 -1.0，错失机会罚 -0.75）引导策略向风险感知行为收敛，符合专业交易实践。

## 实验评估

实验基于 5 只美股（GOOGL, MSFT, META, NVDA, TSLA）2025 年 1-6 月数据，采用 Qwen2.5-3B/7B-Instruct 作为骨干，使用 GRPO 算法训练。基线覆盖 Buy&Hold、规则策略（MACD）、传统 RL（FinRL）及 LLM 基线（FinMem, TradingAgents），但缺失 Alpha-GPT 等最新金融 LLM 变体。

| 方法 | Avg. ARR (%) | Avg. SR | Avg. MDD (%) |
| :--- | :--- | :--- | :--- |
| Buy & Hold | 12.90 | 0.57 | 31.13 |
| FinRLPPO | 12.22 | 0.51 | 33.72 |
| TradingAgents | 24.29 | 0.25 | 12.16 |
| AlphaQuanter-3B | 41.55 | 0.13 | 19.02 |
| AlphaQuanter-7B | 52.26 | 0.26 | 17.48 |

AlphaQuanter-7B 平均 ARR 达 52.26%，比最强基线 TradingAgents 高 27.97 个百分点，但 SR 仅 0.26，低于 Buy&Hold 的 0.57，表明其收益提升伴随风险暴露增加。

| 消融配置 | Avg. ARR (%) | 变化幅度 |
| :--- | :--- | :--- |
| AlphaQuanter-7B | 34.94 | - |
| w/o Rformat | 16.36 | ↓53.2% |
| w/o Rtool | 19.90 | ↓43.0% |
| θ ↑0.5% | 21.25 | ↓39.2% |

移除格式奖励导致 ARR 下降 53.2%，表明推理轨迹结构对策略稳定性至关重要；阈值 θ 微调 0.5% 即引发 39.2% 的性能波动，揭示策略对市场状态判定的高度敏感性。

评估边界存在显著局限：回测窗口仅 6 个月，滚动窗口测试虽显示一定鲁棒性，但未验证跨市场周期（如熊市）的泛化能力；代码已开源，但超参数（如 θ=0.015）固定，未提供实时交易延迟数据。

## 关联研究分析

从问题动机看，AlphaQuanter 与 TradingAgents 的核心差异在于架构选择。TradingAgents 依赖多智能体辩论模拟市场观点，但实验证明在小模型（7B）上，辩论机制反而注入噪声，导致 ARR 仅 24.29%；AlphaQuanter 的单智能体架构通过 RL 直接优化工具编排，避免了信号冲突，ARR 达 52.26%。这一差异根源在于小模型缺乏足够的推理容量支撑多角色协调，单智能体+RL 更适配当前开源模型规模。

从方法设计看，AlphaQuanter 与 FLAG-Trader 同属 LLM+RL 路线，但奖励机制设计截然不同。FLAG-Trader 采用策略梯度优化价格预测，奖励信号稀疏且难以归因；AlphaQuanter 引入过程奖励（格式、工具使用），将信用分配细化到中间步骤，解决了长轨迹训练不稳定问题。然而，AlphaQuanter 的奖励依赖未来收益 $r_t$，这在实时交易中不可得，其回测有效性是否可迁移至在线场景，论文未给出回答。

## 总结

AlphaQuanter 针对 LLM 交易智能体缺乏证据可追溯性与主动工具编排能力的矛盾，通过改造 ReAct 范式并设计可验证复合奖励，实现了单智能体端到端策略优化。实验显示其 7B 模型平均 ARR 达 52.26%，显著优于多智能体基线，但 SR 仅 0.26，且对阈值 θ 高度敏感。该框架的有效性局限于 2025 年上半年特定市场区间，未验证跨周期泛化能力。当市场状态分布发生结构性变化时，基于历史回测训练的 RL 策略是否仍能保持风险校准，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_d56c89d7f4c1)
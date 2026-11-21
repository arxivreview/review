# HuggingFace最新推荐论文 ｜Your Language Model is Its Own Critic: Reinforcement Learning with Value Estimation from Actor's Internal States ｜策略优化内部状态价值估计

研究机构：韩国首尔大学

作者：Yunho Choi、Jongwon Lim、Woojin Ahn 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.07579)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.07579)

> 强化学习可验证奖励（RLVR）训练面临基线估计的高昂计算成本，PPO需训练同规模Critic，GRPO需大量采样维持组均值稳定，两者均挤占有效训练预算。本文切入点在于利用策略模型前向传播中已产生的内部隐藏状态与熵信号，训练轻量探针预测期望奖励，替代传统基线。通过跨Rollout构造保证梯度无偏性，POISE在数学推理基准上以更低计算成本匹配DAPO性能，但其泛化性受限于可验证任务，且探针在复杂长序列中的稳定性尚存疑。

## 研究背景

策略梯度算法中，优势函数 $A(x,y) = R(x,y) - b(x)$ 的方差直接决定训练稳定性，而基线 $b(x)$ 的获取成本是RLVR的核心瓶颈。PPO通过训练独立Critic网络估计价值函数，但需处理完整生成序列，内存消耗翻倍；GRPO通过组内采样均值作为基线，但为降低方差需每组采样多个Rollout，导致固定预算下Prompt多样性下降，梯度估计方差反而增大。

RLVR领域长期存在“探索困境”与“信用分配”难题，但基线获取效率被忽视。GRPO范式下，当组内所有Rollout奖励相同（全对或全错）时，优势函数为零，计算资源浪费；PPO范式下，Critic训练开销随序列长度线性增长。本文抓住“内部状态编码结果相关信息”这一被忽略的点：LLM隐藏状态已隐含难度感知与能力边界信息，此前仅用于推理时诊断，未用于训练时价值估计。

## 核心方法

### 方法参照系

RLVR标准流程中，基线估计分为两类：PPO使用独立Critic网络 $v_\phi$ 预测 $V^\pi(x)$；GRPO使用组内均值 $\bar{r} = \frac{1}{G}\sum_{i=1}^G R(x, y^{(i)})$ 作为经验基线。本文关键差异在于：不训练独立网络，不依赖组采样，而是从策略模型自身前向传播中提取信号，训练轻量探针预测价值函数。

### 内部状态探针设计

探针输入特征由三部分构成：Prompt状态特征 $h_{\theta,p}^{(i)} = \text{Avg}_{t \in P} H_{\theta,t}^{(i)}$（Prompt末尾Token隐藏状态均值）、推理状态特征 $h_{\theta,r}^{(i)} = \text{Avg}_{t \in R^{(i)}} H_{\theta,t}^{(i)}$（推理结束Token隐藏状态均值）、Token熵统计 $u_{\theta}^{(i)}$。探针目标为预测Prompt级价值 $V^\pi(x) = \mathbb{E}_{y \sim \pi(\cdot|x)}[R(x,y)]$，使用留一法蒙特卡洛目标 $\hat{V}_{-i}(x) = \frac{1}{K-1}\sum_{j \neq i} R(x, y^{(j)})$ 避免目标泄漏。设计动机：GRPO组均值依赖大样本，PPO Critic依赖额外参数，而内部状态探针仅需线性回归头，计算开销可忽略，且能捕捉Prompt难度与策略不确定性。

$$
\phi(x, y^{(i)}, \pi) = [h_{\theta,p}^{(i)}; h_{\theta,r}^{(i)}; u_{\theta}^{(i)}]
$$

该公式将隐藏状态与熵信号拼接为探针输入，物理含义是：Prompt状态反映任务难度先验，推理状态反映轨迹执行质量，熵统计反映策略确定性，三者共同编码期望奖励信息。

### 跨Rollout基线构造

为保持梯度无偏性，基线必须与当前动作条件独立。本文采用跨Rollout构造：对每个Prompt采样两个独立Rollout $y^{(1)}, y^{(2)}$，Rollout $y^{(i)}$ 的基线由 $y^{(j)}$（$j \neq i$）的内部状态预测，即 $b(x, y^{(i)}) = g_f(\phi(x, y^{(j)}, \pi))$。优势函数为 $A^{(i)} = R(x, y^{(i)}) - b(x, y^{(i)})$。设计动机：若基线依赖当前Rollout特征，则违反条件独立性，导致策略梯度有偏；跨Rollout构造确保基线仅依赖独立采样，满足无偏性条件，同时仅需2个Rollout而非GRPO的大组，提升Prompt多样性。

$$
A^{(i)} = R(x, y^{(i)}) - g_f(\phi(x, y^{(j)}, \pi)), \quad j \neq i
$$

该公式定义跨Rollout优势，物理含义是：用独立Rollout的内部状态预测当前Rollout的期望奖励，作为基线，从而在低采样成本下实现无偏方差缩减。

## 实验评估

实验在Qwen3-4B与DeepSeek-R1-Distill-Qwen-1.5B上，使用DAPO-Math-17K训练，评测AMC23/24、AIME24/25/26、HMMT25、BRUMO25，报告Avg@32。基线仅对比DAPO（GRPO变体），缺失PPO、Risk-Sensitive RL等探索类方法，也未对比VERL等内部状态调节方法。

| 模型 | 方法 | AMC23 | AIME24 | HMMT25 | Avg |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Qwen3-4B | DAPO | 0.607 | 0.475 | 0.384 | 0.508 |
| Qwen3-4B | POISE | 0.607 | 0.469 | 0.387 | 0.500 |
| DeepSeek-1.5B | DAPO | 0.447 | 0.254 | 0.191 | 0.296 |
| DeepSeek-1.5B | POISE | 0.446 | 0.270 | 0.198 | 0.303 |

POISE在Qwen3-4B上Avg@32为0.500，略低于DAPO的0.508，但在AMC23、HMMT25、BRUMO25上持平或略优；在DeepSeek-1.5B上Avg@32从0.296提升至0.303，AIME24/25/26均有提升。计算效率方面，DeepSeek-1.5B上POISE达相同性能需18小时，DAPO需24小时；Qwen3-4B上POISE需36小时，DAPO需49小时。

消融实验显示，仅使用推理隐藏状态时MAE为0.132、Pearson相关系数0.821，优于仅Prompt状态（MAE 0.234）或仅熵（MAE 0.152）；完整探针MAE降至0.126、相关系数0.838。跨域泛化测试中，POISE在代码（AceCoder）、工具调用（ToolDial）、指令跟随（IF-RLVR）任务上MAE分别为0.231、0.234、0.188，均低于独立Critic的0.393、0.499、0.350。

评估边界：仅报告Avg@32，未提供Pass@1或置信区间；代码未公开，超参数细节在附录；GPU为B200，未提供其他硬件复现结果。探针在长序列（>10k Token）中的稳定性未测试，跨Rollout构造在低成功率Prompt（奖励方差小）下的基线精度未分析。

## 关联研究分析

从问题动机看，POISE与VERL同属利用内部状态优化RLVR，但VERL关注探索熵坍缩，通过隐藏状态秩调节优势函数；POISE关注基线估计效率，通过隐藏状态预测价值函数。差异根源在于任务特性：VERL解决“策略分布锐化”，POISE解决“基线获取成本”。POISE的跨Rollout构造是否限制了探针利用当前Rollout即时反馈的能力，论文未给出回答。

从方法设计看，POISE与Token Hidden Reward同属细粒度信用分配，但Token Hidden Reward基于GRPO学习动态识别Token级隐藏奖励，POISE基于内部状态预测Prompt级价值。差异根源在于信号粒度：Token Hidden Reward需分析正负样本Token预测错误相似度，POISE仅需线性回归隐藏状态均值。POISE在开放域任务中泛化性优于Token Hidden Reward，但后者在数学推理中可能更精细。

## 总结

RLVR训练的核心矛盾是基线估计的计算成本与训练稳定性之间的权衡，PPO与GRPO均因基线获取开销挤占有效预算。POISE抓住内部状态编码结果相关信息的切入点，利用策略模型前向传播中已产生的隐藏状态与熵信号，训练轻量探针预测期望奖励，通过跨Rollout构造保证梯度无偏性。实验证明，POISE在Qwen3-4B与DeepSeek-1.5B上以更低计算成本匹配DAPO性能，探针在跨域任务中泛化性优于独立Critic。但POISE的边界在于：仅验证可验证任务，探针在长序列与低成功率Prompt下的稳定性未测试，跨Rollout构造对即时反馈的限制未分析。当Prompt成功率低于10%时，跨Rollout基线的方差是否显著增大，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.07579)
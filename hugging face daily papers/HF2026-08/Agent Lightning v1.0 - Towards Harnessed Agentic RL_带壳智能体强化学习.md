# HuggingFace最新推荐论文 ｜Agent Lightning v1.0: Towards Harnessed Agentic RL ｜带壳智能体强化学习

研究机构：复旦大学、浙江大学

作者：Zhiyuan He、Siwei Zhang、Zhiwen Zhou 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2608.17528)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2608.17528)

> 现代智能体并非独立运行的大语言模型，而是嵌入在管理工具、上下文与控制流的“外壳”（Harness）中。现有强化学习框架要求将智能体循环直接实现在训练引擎内部，导致部署时的外壳逻辑无法直接用于后训练，造成训练与推理环境的不一致。本文提出“带壳智能体强化学习”范式，通过LLM端点代理解耦训练与执行，并系统解决了由此引发的Token重分词、动态样本归一化等工程挑战。该框架以约3500行代码实现了极简架构，在SWE-bench Verified上将Qwen3.5-9B从41.8%提升至56.4%，但其有效性主要源于系统工程而非算法创新，且缺乏与主流RL算法的横向对比。

## 研究背景

当智能体在真实环境中执行代码修复或网页导航任务时，其决策依赖于外壳管理的工具调用、上下文摘要与控制流。若训练时由RL框架直接控制环境交互，而部署时由独立外壳接管，两者间的上下文构建策略与执行语义差异会导致策略在部署时失效。这种不一致性源于部分可观测马尔可夫决策过程（Partially Observable Markov Decision Process, POMDP）中隐状态的定义差异：传统RL中隐状态仅为环境状态，而带壳RL中隐状态包含外壳状态与环境状态，策略仅观测API请求而非环境全貌。

早期RL框架如VeRL、AReaL要求用户在训练框架内实现智能体循环，难以集成具有复杂依赖关系的现有外壳。本文切入点在于将外壳作为黑盒，通过LLM端点代理连接任意外壳与RL训练引擎，使训练系统仅观测并优化模型调用序列，而非直接控制环境交互。这一设计保留了外壳在部署时的上下文策略与工具协议，消除了训练-推理环境差异，但引入了Token级一致性断裂与动态样本归一化等新挑战。

## 核心方法

### 方法参照系

传统Agentic RL中，训练引擎维护完整Token历史，Rollout形成线性Token轨迹，每个Rollout映射为唯一训练样本。本文问题与该通用流程的关键差异在于：外壳独立构建每次模型调用的提示词，训练引擎仅观测请求-响应对序列，且连续调用间不保证Token前缀连续性。

### Token前缀连续性断裂与Best-effort Merging

外壳通过文本消息与模型API通信，而RL训练基于Token ID。当外壳将前一次响应纳入下一次提示词时，重分词可能导致Token边界改变，破坏Token级前缀条件。例如，单词“having”在采样时为Token `h` 和 `aving`，重分词后可能变为 `hav` 和 `ing`。本文采用Best-effort Merging策略：仅当连续调用的Token ID满足前缀条件时才合并，否则关闭当前序列并开始新序列。该策略避免了强制拼接导致的Off-policy偏差，但牺牲了部分前缀计算复用。

$$
\text{Merge Condition: } (p_i^{\text{tok}}, a_i^{\text{tok}}) \preceq p_{i+1}^{\text{tok}}
$$

该公式定义了合并的Token级前缀条件，确保训练时使用的提示词与Rollout时实际消费的提示词一致，防止因Token ID漂移引入的策略偏差。

### 动态样本归一化与Rollout级优势计算

外壳操作如生成子智能体或摘要上下文，使单个Rollout产生动态数量的训练样本。本文发现，若按样本级归一化损失，产生更多样本的Rollout将获得不成比例的优化权重，导致训练不稳定。本文采用Rollout级Token均值损失，将每个Rollout内所有样本的损失求和后除以该Rollout的总Token数，再对Rollout取均值。

$$
\mathcal{L}_{\text{rollout-mean}} = \frac{1}{|\mathcal{R}|} \sum_{\rho \in \mathcal{R}} \frac{\sum_{i=1}^{N_\rho} \sum_{t} \ell_{\rho,i,t}}{\sum_{i=1}^{N_\rho} L_{\rho,i}}
$$

该公式确保样本数量不影响梯度归一化，隔离了由重分词或外壳操作导致的动态样本数对训练稳定性的干扰。

## 实验评估

实验基于SWE-smith数据集与Qwen3.5-9B模型，使用6K训练样本进行RL训练。基线仅包含自身预训练模型（41.8%），未对比PPO、GRPO等主流RL算法或GPT-4o等强模型。主结果显示，RL训练后模型在SWE-bench Verified上达到56.4%，绝对提升14.6%。

| 方法 | SWE-bench Verified (%) |
| :--- | :--- |
| Qwen3.5-9B (Base) | 41.8 |
| Agent Lightning v1.0 (RL) | 56.4 |

该提升幅度显著，但缺乏算法层面的横向对比，无法区分增益源于RL算法本身还是数据清洗与系统工程。消融实验未报告，无法验证Best-effort Merging与Rollout级归一化的独立贡献。

评估边界在于：实验仅覆盖代码智能体场景，未验证通用指令跟随或搜索智能体的性能；未报告训练吞吐量与样本效率，无法评估“轻量级”架构在大规模集群下的可扩展性；代码已开源（github.com/microsoft/agent-lightning），但超参数与GPU配置未详细披露，可复现性依赖社区验证。

## 关联研究分析

从问题动机看，本文与VeRL Uni-Agent、Polar等框架同属Proxy-based RL路线，但关键差异在于对Token一致性的处理。VeRL Uni-Agent采用Buffered Token Replacement，将新提示词中的前次响应文本替换为缓冲的原始Token ID，虽提高合并率，但改变了实际消费的提示词，引入Off-policy偏差。本文采用Best-effort Merging，牺牲合并率以换取Token级正确性，这一选择源于对算法正确性的优先考量，而非计算效率。

从方法设计看，本文与Tree-GRPO在信用分配机制上形成对比。Tree-GRPO通过树搜索结构实现细粒度过程奖励，依赖固定的轨迹采样空间；本文因外壳动态性无法预知轨迹结构，转而采用Rollout级归一化，将奖励分配至Rollout内所有样本。这一差异源于任务特性：Tree-GRPO适用于数学推理等结构化任务，而本文面向代码修复等开放域任务，后者更依赖Outcome-based奖励而非过程监督。

## 总结

本文要解决的核心矛盾是训练时RL框架控制环境交互与部署时外壳接管执行之间的不一致性。现有方法因要求将智能体循环实现在训练引擎内部，无法直接集成复杂外壳，导致训练-推理环境差异。本文通过LLM端点代理解耦训练与执行，系统解决了Token重分词、动态样本归一化等工程挑战，以约3500行代码实现极简架构。实验证明，在6K样本下RL可将Qwen3.5-9B在SWE-bench Verified上从41.8%提升至56.4%。本文的边界在于缺乏与主流RL算法的横向对比，且未验证通用智能体场景的性能。当外壳操作导致Rollout产生超过10个训练样本时，Rollout级归一化的梯度稳定性是否仍优于样本级归一化，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2608.17528)
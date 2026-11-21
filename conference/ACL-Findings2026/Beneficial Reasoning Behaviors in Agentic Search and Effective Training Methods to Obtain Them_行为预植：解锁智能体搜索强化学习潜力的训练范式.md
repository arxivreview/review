# ACL-Findings2026最新论文 ｜Beneficial Reasoning Behaviors in Agentic Search and Effective Training Methods to Obtain Them ｜行为预植：解锁智能体搜索强化学习潜力的训练范式

研究机构：美国卡内基梅隆大学

作者：Jiahe Jin、Abhijay Sai Paladugu、Chenyan Xiong

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f45aa315e75f)

> 智能体搜索（Agentic Search）旨在让大语言模型（LLM）通过多步交互解决复杂信息需求，但直接应用强化学习（RL）常因策略熵坍缩导致训练不稳定。现有SFT-then-RL范式依赖结果正确性或随机蒸馏，忽略了中间推理过程的质量差异，导致模型缺乏探索基础。本文提出行为预植（Behavior Priming），通过筛选包含特定推理行为的轨迹进行SFT，再行RL，以建立探索基础。该方法在Web基准上相对直接RL提升37.2%，验证了推理行为比结果正确性更关键，但其对多智能体架构的适用性尚存疑。

## 研究背景

智能体搜索要求LLM在长轨迹中动态调用搜索工具并整合证据，这一过程受限于上下文窗口与信息过载。为应对此限制，框架引入summary动作压缩历史，但压缩可能丢失关键推理线索。同时，RL训练面临稀疏奖励下的信用分配难题，即难以确定长轨迹中哪些中间步骤对最终成功贡献最大，导致策略优化不稳定。

主流训练路线分为直接RL与SFT-then-RL两类。直接RL缺乏行为先验，模型易陷入局部最优；SFT-then-RL虽提供初始化，但数据筛选多基于结果正确性（Outcome-driven）或随机采样（Distillation），未区分推理过程的质量。Search-R1等基线证明RL有效，但未解决初期探索不足问题。SmartSearch引入过程奖励模型（PRM）指导中间步骤，但计算成本高且依赖显式奖励信号。本文切入点在于：RL的有效性取决于模型是否已具备特定推理行为，而非仅依赖最终答案的正确性。

## 核心方法

### 标准智能体搜索框架

本文采用标准单智能体框架，模型在每步 $k$ 基于历史上下文 $ctx_k$ 生成输出 $y_k = \langle t_k, a_k \rangle$，其中 $t_k$ 为推理过程，$a_k$ 为动作（search, answer, summary）。该框架与Search-R1等基线一致，差异在于SFT数据构造逻辑从结果导向转向行为导向。

### 有益推理行为识别

设计动机：直接RL中模型无法自发形成高质量推理模式，需显式识别并植入有益行为。本文构建LLM分析管道，对比Gemini 2.5 Flash成功与Qwen3-1.7B失败的轨迹对，提取四种有益行为：信息验证（Information Verification）、权威评估（Authority Evaluation）、自适应搜索（Adaptive Search）与错误恢复（Error Recovery）。行为频率定义为轨迹中展示该行为的步骤占比，公式为：

$$
f_b = \frac{1}{N} \sum_{i=1}^{N} \mathbb{I}[b \in T_i]
$$

其中 $\mathbb{I}$ 为指示函数，$T_i$ 为轨迹 $i$。实验显示，高表现模型的行为频率与基准分数强相关，验证了行为的通用性。

### 行为预植训练

设计动机：SFT阶段需植入行为基础以支撑RL探索，而非仅拟合正确结果。本文从Gemini 2.5 Flash生成的轨迹中筛选包含全部四种行为的样本，构建SFT数据集 $D_{SFT} = \{ \langle x_k, y_k \rangle \mid 1 \le k \le L_i \}$。随后应用GRPO算法进行RL，损失函数为：

$$
\mathcal{J}_{GRPO}(\theta) = \mathbb{E}_{q \sim D, \{T_i\}_{i=1}^G \sim \pi_{\theta_{old}}} \left[ \sum_{i=1}^G \sum_{t=1}^{|y_k|} \min \left( r_{i,k,t}(\theta) \hat{A}_i, \text{clip}(r_{i,k,t}(\theta), 1 \pm \epsilon) \hat{A}_i \right) \right]
$$

其中 $r_{i,k,t}(\theta)$ 为重要性采样比，$\hat{A}_i$ 为轨迹优势。该设计通过行为筛选提高数据利用率，使模型在RL阶段保持高策略熵，避免熵坍缩，从而提升探索效率与测试时扩展能力。

## 实验评估

实验在Qwen3-1.7B与Llama3.2-3B-Instruct上，覆盖GAIA、WebWalkerQA、HLE等3个Web基准及7个多跳QA基准。基线包括直接RL、蒸馏SFT-then-RL与结果驱动SFT-then-RL，缺失多智能体架构（如M-ASK）对比。

| 方法 | 基座模型 | GAIA Avg. | WebWalkerQA | HLE | Overall (Web) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Direct RL | Qwen3-1.7B | 3.9 | 26.1 | 3.9 | 13.9 |
| Behavior Prime | Qwen3-1.7B | 8.7 | 36.5 | 7.2 | 19.7 |
| Direct RL | Llama3.2-3B-Instruct | 31.5 | 72.0 | 56.4 | 66.4 |
| Behavior Prime | Llama3.2-3B-Instruct | 38.1 | 80.0 | 60.4 | 70.9 |

行为预植在Web基准上相对直接RL提升37.2%，在多跳QA上提升6.2%，且优于结果驱动基线。

消融实验显示，仅植入信息验证（IV-Only）的提升（17.4 Overall）低于全行为植入（19.7 Overall），证明行为协同必要性。关键发现：在错误轨迹上行为预植（Behavior Prime Incorrect）的RL后性能（23.5 Overall）与正确轨迹（23.6 Overall）相当，证实推理行为比结果正确性更关键。SFT数据规模从5k增至20k时，WebWalkerQA性能在5k后趋于平稳，表明行为学习存在边际收益递减。

评估边界：未报告置信区间与计算成本；代码未开源；未对比多智能体架构。指标聚焦最终答案准确率，未量化中间步骤质量。

## 关联研究分析

从问题动机看，本文与SmartSearch均关注中间步骤质量，但SmartSearch依赖显式过程奖励模型（PRM）提供细粒度反馈，计算成本高且奖励信号可能不精确；本文通过SFT植入行为，实质是隐式过程引导，避免了PRM的额外计算开销，但缺乏对中间步骤的实时纠正能力。这一差异源于任务特性：智能体搜索的推理行为具有可迁移性，而PRM需针对具体任务定制。

从方法设计看，本文与Search-R1同属RL训练路线，但Search-R1直接应用RL，依赖模型自发探索；本文通过行为预植建立探索基础，解决了Search-R1中初期熵坍缩问题。与M-ASK等多智能体架构相比，本文聚焦单体智能体，未利用角色分工解决长程信用分配，其优势在于训练简洁性，但绝对性能低于多智能体SOTA（如M-ASK在HotpotQA的50.09 F1）。行为预植能否迁移至多智能体架构，论文未给出回答。

## 总结

本文核心矛盾是RL训练中策略熵坍缩导致的探索不足，切入点在于识别并植入有益推理行为，而非仅依赖结果正确性。通过行为预植，模型在RL阶段保持高熵，提升探索效率，Web基准相对直接RL提升37.2%。边界在于：SFT数据规模超过5k后收益递减，且未验证多智能体架构下的有效性。当支持集增大到5-shot时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_f45aa315e75f)
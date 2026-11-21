# HuggingFace最新推荐论文 ｜RecHarness: A Bandit-Routed Agentic Harness for Self-Evolving Recommender Systems ｜基于多臂老虎机路由的推荐模型自进化框架

研究机构：美国佐治亚理工学院、快手

作者：Haoran Ling、Yuecheng Li、Zeyu Song 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2607.29241)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2607.29241)

> 推荐系统模型迭代长期依赖工程师手动调整架构、损失函数与训练策略，这一过程消耗大量算力且难以自动化。现有LLM智能体虽能生成代码，但缺乏原则性的试验分配机制，导致在有限预算下搜索发散、成功率低。RecHarness将优化方向选择与代码生成解耦，通过Thompson采样路由分配试验预算，再由LLM在选定方向内生成具体修改。该框架在工业A/B测试中验证了业务指标增益，但其对预设编辑臂空间的依赖限制了其发现非预设架构创新的能力。

## 研究背景

推荐模型优化是一个连续迭代过程，涉及骨干架构、训练目标、优化策略及特征交互等多维度调整。传统自动机器学习（AutoML）方法如超参数优化（HPO）和神经架构搜索（NAS）仅在预定义的标量网格或固定模板内搜索，无法处理重设计损失函数或切换架构块等代码级变更。LLM驱动机器学习工程（MLE）智能体（如AIDE, Jiang et al., 2025）通过树搜索探索候选程序，但将执行反馈压缩为标量分数，丢弃了错误日志和训练动态中的关键信号。

主流LLM智能体方法面临的核心瓶颈是探索效率低下。让LLM自由决定探索方向会导致候选方案在开放空间中发散，而每次代码修改都伴随昂贵且噪声大的训练-验证试验。近期研究表明，通用LLM在缺乏外部算法支持时难以可靠地探索（Krishnamurthy et al., 2024），且结合LLM推理与经典多臂老虎机机制比直接由LLM选择臂更有效（Sun et al., 2026）。RecHarness的切入点在于将验证反馈同时用作LLM推理的文本信号和引导未来试验的显式后验状态，通过结构化路由解决发散问题。

## 核心方法

### 方法参照系

RecHarness将推荐模型优化建模为预算约束下的序列试验分配问题。与AIDE等树搜索方法不同，它不将搜索空间视为无限候选程序，而是预定义为可解释的编辑臂集合。关键差异在于引入带后验更新的路由机制，将“搜索哪里”与“如何修改”解耦，前者由统计决策驱动，后者由LLM生成。

### 带后验更新的Thompson采样路由

在标准LLM智能体流程中，方向选择通常由LLM基于历史文本反馈直接决定，缺乏概率保证。RecHarness在此环节引入Thompson采样，为每个编辑臂 $a$ 维护Beta后验分布 $\theta_a \sim \text{Beta}(\alpha_a, \beta_a)$。

$$
\tilde{\theta}_a \sim \text{Beta}(\alpha_a, \beta_a), \quad G_t = \text{Top}_G_{a \in A_t} (\tilde{\theta}_a)
$$

该公式通过从后验分布中采样成功概率 $\tilde{\theta}_a$ 并选择最大值，实现了探索与利用的平衡。设计动机在于解决LLM自由探索导致的低成功率问题：标量验证反馈累积为后验统计量，使系统能基于经验证据分配有限预算，而非依赖LLM的主观判断。每次试验后，根据二元成功信号 $r_t(a)$ 更新参数 $\alpha_a \leftarrow \alpha_a + r_t(a), \beta_a \leftarrow \beta_a + 1 - r_t(a)$，确保路由策略随证据积累而收敛。

### 实验技能与盆地感知跳跃

路由选定方向后，LLM需生成具体代码修改。RecHarness引入实验技能（Experiment Skill）作为动态文本指南，记录当前最优模型、成功编辑摘要及失败原因。对于局部优化停滞的情况，系统激活跳跃臂（Jump Arms），允许结构性变更。

$$
J_t = \mathbb{I} \left[ \frac{s^\star_t - s^\star_{t-W}}{W} \leq \tau \right], \quad A_t = \begin{cases} A_{\text{local}} \cup A_{\text{jump}}, & J_t = 1 \\ A_{\text{local}}, & J_t = 0 \end{cases}
$$

该公式通过监测最近 $W$ 轮验证分数的平均改进率，当低于阈值 $\tau$ 时判定当前盆地饱和，从而开放跳跃臂参与选择。设计动机在于解决局部最优陷阱：局部臂仅进行微调，而跳跃臂（如架构升级）可能跳出当前盆地。跳跃臂的接受需经过重调优窗口，确保结构性变更在局部适应后仍优于原最优模型，避免盲目跳跃导致的性能下降。

## 实验评估

实验在Amazon Reviews（Movies, Scientific, Electronics, CDs）和KuaiRec数据集上进行，涵盖GRU4Rec、SASRec、HSTU等8种模型。基线包括冷启动模板（Base）和已发表结果（Paper）。RecHarness在Amazon Movies上SASRec的HR@10从0.2317提升至0.5179，在KuaiRec D2Q模型上WT-MAE降低26.37%。

| 数据集/模型 | 指标 | Base | RecHarness | Paper |
| :--- | :--- | :--- | :--- | :--- |
| Amazon Movies / SASRec | HR@10 | 0.2317 | 0.5179 | 0.4785 |
| Amazon Movies / HSTU | HR@10 | 0.3253 | 0.3794 | 0.3459 |
| KuaiRec / D2Q | WT-MAE | 3.4129 | 3.3107 | 5.4260 |
| KuaiRec / GR | WT-XAUC | 0.5310 | 0.5947 | 0.5650 |

消融实验显示，RecHarness在47.92%的非基线试验中刷新了轮次最佳分数，而随机路由（TR w/ Random）仅为22.45%，无Bandit路由（w/o Bandit）为41.67%。RecHarness的最大增益达24.00%，显著高于w/o Bandit的10.16%，表明结构化编辑维度比自由LLM搜索更能发现高收益方向。

评估边界方面，论文未报告置信区间，且缺乏与AIDE、NOVA等同类LLM智能体在相同预算下的公平对比。代码已开源，但超参数（如阈值 $\tau$、窗口 $W$）的敏感性分析未详细展开。在线A/B测试在10%流量上运行7天，验证了离线增益向业务指标（ADVV +2.084%）的转化，但未披露长期稳定性数据。

## 关联研究分析

从问题动机看，RecHarness与NOVA（Liu et al., 2026）均旨在解决LLM智能体探索发散问题，但NOVA使用SGD启发的架构梯度聚合历史编辑，而RecHarness采用Thompson采样进行概率路由。这一差异源于任务特性：NOVA关注架构演化的连续性，适合平滑优化；RecHarness关注离散编辑臂的选择，适合多方向并行探索。RecHarness的预设臂空间限制了其发现非预设创新的能力，而NOVA的开放搜索可能更灵活但效率更低。

从方法设计看，RecHarness与Reasoning-as-Gradient（Zhang et al., 2026）共享“文本反馈作为梯度”的理念，但RecHarness将文本反馈具体化为实验技能，仅用于LLM生成假设，而不直接指导路由。这种解耦设计牺牲了文本信号对路由的直接影响，换取了路由的统计稳定性。在简单序列推荐任务中，这种解耦是否优于端到端文本梯度引导，论文未给出回答。

## 总结

RecHarness解决的核心矛盾是LLM智能体在有限预算下探索效率低下的问题。其切入点在于将方向选择与代码生成解耦，利用Thompson采样路由基于标量验证反馈分配预算，同时利用实验技能引导LLM生成具体修改。实验证明，该方法在Amazon和KuaiRec数据集上显著优于基线，并在工业A/B测试中提升ADVV 2.084%。然而，其性能依赖于人工预设的编辑臂空间，且缺乏与同类LLM智能体的公平对比。当编辑臂空间覆盖不全时，RecHarness能否通过跳跃臂机制自主扩展搜索空间，而非仅依赖人工定义的结构性变更，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2607.29241)
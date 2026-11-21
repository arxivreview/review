# HuggingFace最新推荐论文 ｜AutoSaddler: Automatic Harness Optimization with Durable Updates from Agent Execution Traces ｜自动Harness优化：基于执行轨迹的离线学习框架

研究机构：韩国科学技术院、南方科技大学

作者：Sungho Park、Wonjoong Kim、Rongyuan Tan 等 13 人

论文原文见 [arXiv](https://arxiv.org/abs/2608.23041)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2608.23041)

> 长程智能体任务中，局部微小错误会随步骤累积导致整体失败，而手动调优外部Harness（提示、工具、中间件）耗时且难以规模化。现有自动优化方法多聚焦于提示文本或采用全批量搜索，缺乏对长轨迹深层根因的诊断与泛化性控制。AutoSaddler将Harness优化形式化为离线学习问题，通过“诊断-补丁-反思-进化”四阶段循环，在有限Rollout预算下生成可泛化的代码级更新。该方法在三个基准上显著超越基线，但其收益高度依赖骨干模型能力，且未探索与模型权重联合优化的路径。

## 研究背景

当智能体在模拟智能手机环境中执行多步任务时，一次工具调用参数错误可能引发后续所有步骤的逻辑崩溃。这种长程依赖要求智能体不仅具备单步推理能力，更需依赖外部Harness来约束行为边界。Harness作为LLM之外的系统层组件，包含提示规则、工具接口定义及运行时控制逻辑，其设计质量直接决定智能体在复杂环境中的可靠性。然而，Harness设计空间庞大且非结构化，手动调优需遍历大量组合，且每次评估需执行完整任务轨迹，成本高昂。

长程任务可靠性是智能体应用的核心瓶颈。主流解决路线分为两类：一是模型层训练，通过强化学习或微调更新LLM权重以优化策略；二是系统层优化，通过调整外部Harness提升鲁棒性。模型层训练虽能从根本上改变决策分布，但训练成本高、数据需求大，且难以快速适配新领域。系统层优化则无需更新权重，但现有自动方法如GEPA仅优化提示文本，Meta-Harness虽扩展至全系统但采用全批量搜索，缺乏对长轨迹失败根因的精细诊断，导致生成的更新往往过拟合于单条轨迹，泛化性差。AutoSaddler的切入点在于：将Harness视为可编辑代码，通过离线学习范式结合深层诊断与结构化补丁，在有限计算预算下实现泛化性更新。

## 核心方法

### 方法参照系

AutoSaddler的问题形式化为在有限Rollout预算 $K$ 下，搜索Harness参数 $\theta = (\theta_{prompt}, \theta_{tool}, \theta_{middleware})$ 以最大化任务分布上的期望性能。这与标准小批量学习流程相似，但关键差异在于：Harness参数是文本与代码混合体，不可微分，无法使用反向传播，需替代机制提取更新信号。

### 基于轨迹的诊断-补丁机制

传统提示优化方法（如GEPA）将失败归因于提示文本缺陷，通过浅层反思生成新提示。AutoSaddler指出，长程任务失败往往源于工具逻辑或中间件控制缺陷，浅层反思无法定位根因。该机制将诊断与补丁生成合并，允许智能体访问执行轨迹与Harness代码库，通过CA-SDK主动检索相关代码片段，识别根本原因并生成结构化补丁 $\Delta\theta_n$。补丁空间被划分为提示、工具、中间件三类，并进一步分为能力补丁（修改可执行逻辑）与引导补丁（修改文本指令）。这种结构化约束避免了无约束编辑导致的副作用，确保更新针对特定组件失效。

$$
\hat{\theta}_{AS} = \arg\max_{\theta \in V_{K,dev}} \hat{J}_{D_{dev}}(\theta)
$$

该公式表明，最终选定的Harness是开发集上经验性能最高的候选者，其中 $V_{K,dev}$ 是在预算 $K$ 内探索到的候选集。

### 泛化性感知的进化选择

仅基于训练小批次的改进可能过拟合。AutoSaddler引入反思会话与EvoDAG（有向无环图）记忆机制。反思会话比较补丁前后的轨迹，将结果分为“修复”、“回归”、“仍失败”、“仍通过”四类，并记录因果教训。EvoDAG存储这些教训与性能指标，进化会话基于此图合成新Harness，可合并不同分支的成功组件或回退有害更新。这一机制确保保留的更新具备跨任务泛化性，而非仅修复单条轨迹。

## 实验评估

实验在GAIA2、SWE-Bench Pro、Terminal-Bench 2.0三个基准上进行，基线包括手动调优的Default Agent、SWE-agent、Terminus 2，以及自动优化方法GEPA和Meta-Harness。AutoSaddler在GAIA2上平均Pass@1达62.0%，超越Default Agent 9.0个百分点，超越最强自动基线GEPA 7.4个百分点。在SWE-Bench Pro上，AutoSaddler达46.9%，超越SWE-agent 8.4个百分点；在Terminal-Bench 2.0上达50.0%，超越Terminus 2 10.0个百分点。

| 基准 | 方法 | Pass@1 (%) |
| :--- | :--- | :--- |
| GAIA2 | Default Agent | 53.0 ± 1.5 |
| GAIA2 | GEPA | 54.6 ± 2.5 |
| GAIA2 | Meta-Harness | 53.2 ± 2.2 |
| GAIA2 | AutoSaddler | 62.0 ± 1.2 |
| SWE-Bench Pro | SWE-agent | 37.3 ± 4.8 |
| SWE-Bench Pro | GEPA | 42.5 ± 1.2 |
| SWE-Bench Pro | AutoSaddler | 46.9 ± 1.8 |
| Terminal-Bench 2.0 | Terminus 2 | 40.0 ± 0.0 |
| Terminal-Bench 2.0 | Meta-Harness | 43.3 ± 5.8 |
| Terminal-Bench 2.0 | AutoSaddler | 50.0 ± 0.0 |

消融实验显示，移除深层诊断使GAIA2性能从62.0%降至57.8%；移除结构化干预降至56.9%；移除泛化性选择降至50.6%。其中，泛化性选择移除导致的性能下降最大，表明过拟合是自动优化主要风险。细粒度消融进一步揭示，开发集过滤贡献了5.1个百分点的增益，而EvoDAG反思提供额外5.1个百分点，两者协同作用显著。

评估边界方面，实验仅使用Claude Opus 4.6作为骨干模型，未测试跨模型迁移性（附录显示迁移至Haiku 4.5后性能下降至35.6%）。代码已开源，但优化过程依赖CA-SDK，复现需特定环境配置。

## 关联研究分析

从问题动机看，AutoSaddler与Reflexion均关注从失败中学习，但Reflexion采用在线单步反思，适用于短轨迹任务；AutoSaddler采用离线批量诊断，针对长程任务中错误累积问题。差异根源在于任务特性：长程任务失败根因往往分散在多个步骤，单步反思无法捕捉全局依赖，而批量诊断可通过轨迹对比定位系统性缺陷。

从方法设计看，AutoSaddler与Meta-Harness同属系统层优化，但Meta-Harness采用全批量搜索，每次更新评估所有训练任务，计算成本高且易陷入局部最优；AutoSaddler采用小批量+验证集过滤，通过EvoDAG实现历史感知进化。这一设计选择源于对计算预算的约束：在有限Rollout下，全批量搜索无法充分探索，而小批量+泛化性选择能更高效地利用评估信号。

## 总结

AutoSaddler解决的核心矛盾是长程任务中Harness手动调优的低效性与自动优化方法的泛化性缺失。其切入点在于将Harness视为代码，通过深层诊断定位根因，结构化补丁约束更新空间，EvoDAG进化确保泛化性。实验证明该方法在三个基准上超越基线9.0-10.0个百分点，但性能高度依赖骨干模型能力，跨模型迁移性有限。当骨干模型能力不足时，Harness优化的收益是否会被模型层训练的收益覆盖，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2608.23041)
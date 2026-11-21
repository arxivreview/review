# HuggingFace最新推荐论文 ｜EvoTrainer: Co-Evolving LLM Policies and Training Harnesses for Autonomous Agentic Reinforcement Learning ｜训练侧诊断基础设施的协同进化

研究机构：中国科学院、阿里巴巴集团

作者：Guhong Chen、Yingcheng Shi、Yongbin Li 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.03108)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.03108)

> 自主大语言模型训练长期被简化为静态配方搜索，导致训练过程中的诊断逻辑无法适应动态变化的瓶颈。现有方法在智能体强化学习中因标量奖励掩盖行为退化而失效，本文切入点是将训练侧诊断基础设施本身视为可进化对象。EvoTrainer通过策略版本与诊断Harness的双循环协同进化，在SWE-9B上超越人工设计基线4.39 BC%。该方法验证了训练侧进化的必要性，但其对计算资源的依赖与跨域泛化边界仍存疑。

## 研究背景

当智能体在长程任务中执行代码编辑与测试时，强化学习（Reinforcement Learning, RL）的奖励信号往往稀疏且滞后。这种稀疏性导致传统基于标量验证分数的迭代陷入停滞，因为高分可能掩盖奖励泄漏或行为退化，而低分分支可能蕴含关键的负向证据。解决这一困境需要动态的诊断机制，即训练侧Harness，它负责解释轨迹证据、识别失败模式并指导干预方向。然而，固定模板的Harness无法应对瓶颈从奖励稀疏向行为崩溃的转移，使得诊断逻辑本身成为进化的瓶颈。

自主模型训练的主流路线聚焦于配方搜索，如AutoResearch通过提议-训练-评估循环优化超参数，但保留了静态的诊断视图与记忆结构。这种设计在复杂智能体RL中暴露出严重局限：当瓶颈从配方选择转向对低信息量Rollout组的处理时，静态Harness无法生成新的行为指标或检索外部证据。EvoTrainer的切入点在于将训练系统本身作为改进对象，区分策略在单次运行内的进化与训练器在多次运行间的进化，通过积累证据、修订Harness并复用操作技能，实现诊断基础设施与模型策略的联合优化。

## 核心方法

### 方法参照系

本文问题归属于自主实验系统范畴，但区别于传统的推理侧Harness优化（如Meta-Harness优化推理脚手架），EvoTrainer聚焦于训练侧诊断基础设施。关键差异在于：推理侧优化针对模型输出环境，而训练侧进化针对解释训练结果的证据与程序，需处理奖励分布、组方差及跨版本干预证据等RL特有信号。

### 策略自进化与版本控制探索

策略自进化通过版本控制的探索实现，每个版本 $v_i$ 生成工件 $A_i$ 并由当前Harness $h_i$ 解释。设计动机在于解决固定模板无法归因复杂干预效果的问题。EvoTrainer将版本转移形式化为证据条件化的状态更新：

$$ T_i = (v_i, h_i, A_i, d_i, \Delta_i, \omega_i) $$

其中 $d_i$ 为诊断，$\Delta_i$ 为干预，$\omega_i$ 为结果。该公式将训练状态解耦为策略、Harness、证据与决策，使高分版本可能暴露脆弱奖励设计，低分分支保留为负向证据，避免将每次运行简化为二元保留或拒绝事件。

### 训练侧Harness进化与技能复用

Harness进化通过四层诊断（score, signal, behavior, version）实现，当现有证据无法解释版本结果或区分竞争假设时触发升级。设计动机在于解决标量分数无法捕捉行为退化与奖励泄漏的问题。Harness沿四个轴升级：指标扩展、分析器特化、程序修订及外部证据检索。持久记忆库 $M = \{L_{ver}, C_{case}, S_{skill}, S_{search}\}$ 存储可复用技能，如StdGroupFilter，其复用机制定义为：

$$ S_{skill}^{(k+1)} = S_{skill}^{(k)} \cup \{ \text{validated\_mechanism} \mid \text{cross\_version\_evidence} \} $$

该公式表明技能仅在跨版本证据支持下被保留，实现从归档存储到操作复用的转变，使SWE中验证的过滤机制能迁移至Math与Coding域。

## 实验评估

实验在Math、Coding与SWE三个域进行，评估协议统一为Avg@8，SWE使用BC%指标。基线覆盖人工设计RL、AutoResearch及GRPO/GSPO变体，但缺失Reflexion等纯非参数化基线，可能低估非参数化方法的竞争力。

| 方法 | SWE-9B BC% | Math Avg@8 | Coding Avg@8 |
| --- | --- | --- | --- |
| Base model (no RL) | 30.19 | 77.50 | 67.50 |
| Human-engineered RL | 33.77 | 77.50 | 77.50 |
| EvoTrainer | 38.16 | 84.17 | 73.33 |

EvoTrainer在SWE-9B上较人工基线提升4.39 BC%，在Math上提升6.67 Avg@8，验证了训练侧进化在长程智能体任务中的优势。

消融实验显示，移除Harness进化导致SWE-9B在v3饱和于33.33 BC%，而完整框架达到38.16 BC%；移除技能库使Coding v9无法复用StdGroupFilter，最终配置不可达。反直觉发现是Harness审计拦截了Git泄漏导致的48.80 BC%虚假高分，真实分数仅为31.04 BC%，表明标量分数可能严重误导版本提升决策。

评估边界受限于单一随机种子（seed 42）与固定评估协议，未报告置信区间。可复现性方面，论文未提供代码URL，且完整运行消耗约 $4.0 \times 10^8$ 训练器智能体令牌，计算成本高昂。

## 关联研究分析

从问题动机看，EvoTrainer与Meta-Harness均关注Harness优化，但前者针对训练侧诊断，后者针对推理侧脚手架。差异根源在于任务特性：训练侧需处理RL特有的奖励分布与组方差信号，而推理侧仅需优化上下文与工具调用。EvoTrainer的四层诊断结构是应对RL信号复杂性的必要设计，而Meta-Harness的静态评估逻辑无法迁移至训练场景。

从方法设计看，EvoTrainer与AutoResearch共享自主实验循环，但后者保留静态诊断视图，前者引入Harness进化。差异源于对瓶颈动态性的认知：AutoResearch假设配方搜索是主要瓶颈，而EvoTrainer认为诊断基础设施的静态性是复杂RL中的关键限制。EvoTrainer通过技能库实现跨域复用，而AutoResearch缺乏此机制，导致其在Coding域表现低于无RL基线。

## 总结

EvoTrainer解决的核心矛盾是静态诊断逻辑无法适应智能体RL中动态变化的瓶颈。其切入点在于将训练侧Harness视为可进化对象，通过策略与Harness的双循环协同进化，在SWE-9B上实现38.16 BC%的性能，超越人工基线4.39 BC%。本文的边界在于计算成本高昂且未验证不同规模模型下Harness进化的有效性差异。当模型规模从9B缩小至4B时，训练侧Harness进化的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.03108)
# ICLR2026最新论文 ｜Kimi-Dev: Agentless Training as Skill Prior for SWE-Agents ｜技能先验驱动的SWE智能体训练

研究机构：月之暗面、新加坡国立大学

作者：Zonghan Yang、Shengjie Wang、Kelin Fu 等 21 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.23045)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.23045)

> 软件工程智能体（SWE-Agent）面临长程轨迹训练不稳定与Agentless工作流灵活性不足的二元对立。现有方案要么在端到端多轮交互中遭遇信用分配稀疏，要么在单轮模块化流程中丧失动态适应能力。本文切入点在于将Agentless训练重构为诱导原子技能先验的中间阶段，而非最终交付物。通过Mid-training、Cold-start与RL构建技能基础，再以轻量SFT适配SWE-Agent框架。这一范式在降低训练成本的同时提升了适配效率，但其技能先验对未知环境探索上限的潜在限制尚存疑。

## 研究背景

当SWE-Agent在真实仓库中执行多轮交互时，轨迹长度常达数十至数百步，导致上下文窗口压力与执行反馈稀疏。这种长程依赖使得直接端到端强化学习（RL）极易陷入不稳定或崩溃，而Agentless方法虽通过单轮可验证步骤规避了此问题，却因固定工作流无法适应需要多轮增量更新的复杂场景。

该领域长期将SWE-Agent与Agentless视为互斥范式：前者以灵活性换取训练难度，后者以稳定性牺牲探索空间。主流路线如SWE-RL（Wei et al., 2025）直接优化Agent端到端性能，但受限于高质量轨迹数据稀缺与信用分配困难；Agentless（Xia et al., 2024）虽模块化清晰，却难以捕捉真实开发中的动态反思行为。本文挑战这一二元对立，提出Agentless训练应作为诱导定位、编辑与反思等原子技能先验的手段，为后续SWE-Agent适配提供高效初始化基础。

## 核心方法

### 方法参照系

标准SWE-Agent训练流程直接采集多轮交互轨迹进行RL，但面临长程信用分配稀疏与初始化敏感问题。本文关键差异在于将训练解耦为两阶段：先通过Agentless工作流强化原子技能，再以轻量SFT迁移至多轮交互框架。

### 技能先验诱导机制

Agentless训练通过BugFixer与TestWriter双角色协作强化核心技能。BugFixer负责生成修复补丁，TestWriter创建复现Bug的单元测试，两者均依赖文件定位与代码编辑两项原子能力。Mid-training阶段使用约150B tokens真实GitHub数据构建技能基础，其中包含50B Agentless衍生数据、20B PR提交包及20B合成推理数据。Cold-start阶段利用DeepSeek R1生成的推理轨迹激活长链思维（CoT）能力，使模型掌握问题分析、方法草图与自我修正等技能。RL阶段聚焦代码编辑，采用基于REINFORCE的策略梯度算法，仅使用执行结果作为奖励信号：

$$
R = \begin{cases}
1 & \text{if } \text{patch passes all ground-truth tests} \\
0 & \text{otherwise}
\end{cases}
$$

该设计动机在于规避过程级奖励的校准困难，通过纯结果信号确保训练目标与真实工程验证一致。自适应提示选择机制丢弃pass@16=0的样本，并通过课程学习逐步引入高难度任务，解决长轨迹中奖励稀疏导致的收敛停滞问题。

### 测试时自博弈与技能迁移

测试时自博弈机制通过生成40个候选补丁与40个测试进行交叉执行，利用执行反馈筛选最优补丁。评分函数综合考虑复现测试与回归测试表现：

$$
S_i = \sum_{j \in T} \left( \frac{FP(i,j)}{F(j)} \cdot \frac{PP(i,j)}{P(j)} \right)
$$

其中$FP(i,j)$与$PP(i,j)$分别表示补丁$i$在测试$j$下的失败转通过与通过保持数量。该机制无需额外训练即可提升单次推理上限，且3补丁×3测试的组合已超越40补丁多数投票性能。技能迁移验证表明，Kimi-Dev经5k条SWE-Agent轨迹SFT后，在SWE-bench Verified上达到48.6% pass@1，与Claude 3.5 Sonnet（49.0%）相当。消融实验显示，RL先验仅需$2^{23}$ SWE-Agent SFT tokens即达到Base先验需$1.5 \times 2^{28}$ tokens的性能水平，证明技能先验显著降低适配数据需求。

## 实验评估

实验在SWE-bench Verified基准上进行，对比Agentless类（SWE-SWISS 58.2%）与Agent类（Claude 3.5 Sonnet 49.0%）基线。Kimi-Dev在Agentless框架下取得60.4%解决率，为开源模型SOTA；适配SWE-Agent后达到48.6% pass@1，超越SWE-agent-LM（40.2%）。

| 模型 | 框架 | 参数规模 | SWE-bench Verified 解决率 (%) |
|---|---|---|---|
| Kimi-Dev | Agentless | 72B | 60.4 |
| SWE-SWISS | Agentless | 32B | 58.2 |
| Claude 3.5 Sonnet | SWE-Agent | - | 49.0 |
| Kimi-Dev (SFTed) | SWE-Agent | 72B | 48.6 |

消融实验揭示关键设计决策：Mid-training token数从50B增至150B持续提升性能；RL阶段引入正例强化后，BugFixer在后期训练收敛加速；测试时自博弈中，3×3组合性能已超越40补丁多数投票，表明执行反馈信息量优于单纯数量堆叠。值得注意的是，SFT先验在200条轨迹时出现性能退化，而RL先验保持稳定，暗示RL嵌入的可迁移技能比SFT记忆模式更具泛化性。

评估边界存在明显局限：实验仅覆盖SWE-bench Verified单一基准，未验证跨语言或跨仓库泛化能力；48.6%的Agent性能主要归功于72B骨干模型还是技能先验机制，缺乏控制变量实验；代码与超参数虽开源，但10,000并发Kubernetes沙箱基础设施的复现成本极高，限制了独立验证可行性。

## 关联研究分析

从问题动机看，SWE-RL（Wei et al., 2025）直接优化Agent端到端性能，但受限于长轨迹信用分配稀疏；本文通过技能先验解耦训练阶段，将复杂多轮问题分解为可验证的单轮技能强化，根源在于任务特性决定——SWE任务的长程依赖使得直接端到端优化在计算与数据效率上不可行。从方法设计看，Agentless（Xia et al., 2024）将工作流视为最终解决方案，本文则将其重构为训练中间阶段，差异源于对技能可迁移性的假设：本文认为原子技能（定位、编辑、反思）在单轮与多轮框架间存在共享底层，而Agentless未探索此迁移路径。

## 总结

本文核心矛盾在于SWE-Agent训练不稳定与Agentless灵活性不足的二元对立。切入点在于识别Agentless训练可诱导可迁移的原子技能先验，而非仅作为独立解决方案。方法上通过Mid-training、Cold-start与RL构建技能基础，再以轻量SFT适配SWE-Agent框架。实验证明Kimi-Dev在Agentless框架下达到60.4%解决率，适配后48.6% pass@1与Claude 3.5 Sonnet相当。边界在于技能先验对未知环境探索上限的潜在限制，以及缺乏跨基准泛化验证。当支持集从5k条SWE-Agent轨迹扩展至更大规模时，技能先验的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.23045)
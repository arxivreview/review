# ICLR2026最新论文 ｜UNLOCKING LONG-HORIZON AGENTIC SEARCH WITH - LARGE-SCALE END TO-END RL ｜解锁长程智能体搜索的大规模端到端强化学习

研究机构：清华大学、美国华盛顿大学

作者：Jiaxuan Gao、Wei Fu、Minyang Xie 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_52926037)

> 深度研究智能体需在开放网络环境中通过多轮工具调用整合碎片化证据，但现有开源方案严重依赖商业大模型生成数据或作为子模块，导致系统复杂且不可复现。本文切入点在于证明纯端到端强化学习（RL）足以让单模型涌现出媲美商业系统的长程搜索策略。通过设计两阶段课程学习与完全异步RL训练系统，ASearcher在GAIA等基准上取得58.7%的Pass@1成绩。其价值在于验证了“训练派”路线的可行性，但仅使用轨迹级稀疏奖励是否足以解决长程信用分配难题仍存疑。

## 研究背景

当智能体面对“2012年伦敦奥运会中国获得多少金牌”这类问题时，表面简单实则需调和历史记录与后续兴奋剂取消资格导致的冲突信息。这要求智能体具备长程决策能力，即在多轮搜索中维持目标一致性并过滤噪声。然而，长程轨迹中的执行漂移与信用分配难题使得传统监督微调（SFT）难以优化策略：SFT将轨迹内所有步骤视为同等贡献，无法区分关键决策与冗余步骤，导致模型在长任务中容易丢失早期关键证据，陷入局部最优或循环。

深度研究智能体的构建经历了从提示工程到训练优化的演进。早期ReAct范式确立了“推理-行动-观察”循环，但受限于底层模型能力，仅靠提示无法突破长程推理瓶颈。2024年后，随着GAIA等基准暴露出单跳问答向多步导航的鸿沟，研究者引入RL进行策略优化。然而，主流开源方案如AFM和MiroThinker仍依赖商业LLM生成专家数据或作为专用工具，形成了“架构复杂化”与“数据依赖”的双重枷锁。ASearcher的切入点在于剥离这些外部依赖，探究纯RL能否在单模型、仅使用基础搜索工具的约束下，自主涌现出复杂的长程搜索策略，从而回应“是否必须依赖商业模型才能达到SOTA性能”这一核心争议。

## 核心方法

### 方法参照系

ASearcher属于智能体强化学习路线，其标准流程是将信息寻求任务建模为马尔可夫决策过程（MDP），通过策略梯度优化智能体的工具调用序列。与依赖多智能体协作或SFT冷启动的架构派方法不同，ASearcher坚持单模型设计，仅使用搜索和浏览两个基础工具，核心差异在于完全摒弃外部模型依赖，将长程策略的涌现归因于大规模RL训练本身。

### 数据合成与两阶段课程

传统RL训练受限于高质量长程QA数据的稀缺，而SFT数据往往由商业模型生成，存在分布偏差。ASearcher开发了一个基于QwQ-32B的数据合成智能体，通过“注入”（Injection）和“模糊化”（Fuzzing）两个动作迭代修改种子问题，增加信息复杂度与不确定性。注入动作从外部源获取实体相关事实并嵌入问题，模糊化则替换具体细节为泛指描述（如将“Catskill Mountain Railroad”改为“a historic mountain railway”）。为确保质量，合成过程包含基础质量检查、难度测量（无工具直接生成答案）及答案唯一性检查。训练采用两阶段课程：第一阶段在全难度数据集上训练基础工具调用能力；第二阶段移除仅需少于5次工具调用的简单问题，聚焦长程任务。这种设计解决了长程策略学习初期因任务过难导致的梯度稀疏问题，使模型先习得基本搜索逻辑，再逐步优化复杂决策。

### 完全异步RL训练与GRPO优化

长程RL训练面临轨迹执行时间方差大导致的GPU空闲问题。传统批量生成系统需等待最长轨迹，造成资源浪费。ASearcher采用完全异步RL训练，解耦轨迹收集与权重更新。轨迹并行收集，独立发送工具调用与LLM生成请求，长轨迹可跨越多个模型版本而不阻塞其他轨迹。训练侧在收集到足够轨迹形成批次时立即启动更新。算法采用组相对策略优化（GRPO），对每个问题生成$G$条轨迹$\tau_1, \dots, \tau_G$，损失函数定义为：

$$
\mathcal{L}(\theta) = -\frac{1}{G} \sum_{i=1}^{G} \left[ \min\left( \frac{\pi_\theta(\tau_i|x)}{\pi_{\theta_{old}}(\tau_i|x)} \hat{A}_i, \text{clip}\left( \frac{\pi_\theta(\tau_i|x)}{\pi_{\theta_{old}}(\tau_i|x)}, 1-\epsilon, 1+\epsilon \right) \hat{A}_i \right) \right]
$$

其中$\hat{A}_i$为基于组内相对奖励计算的优势值。该公式通过裁剪比率防止策略更新过大，利用组内相对奖励消除基线偏差，使模型在稀疏奖励下仍能稳定优化长程策略。动态过滤机制剔除所有响应奖励相同（优势为零）的查询，进一步提升训练效率。

## 实验评估

ASearcher在GAIA（103个文本验证子集）、xBench-DeepSearch（100个中文问题）、Frames（824个问题）及HLE（500个子集）上进行评估，基线覆盖商业智能体（OpenAI DeepResearch, Kimi-Researcher）、通用LLM（OpenAI-o3, DeepSeek-R1）及32B开源智能体（Search-R1, WebThinker等）。

| 方法 | GAIA | xBench-DeepSearch | Frames | HLE |
| :--- | :--- | :--- | :--- | :--- |
| ASearcher (QwQ-32B) | 58.7 | 51.1 | 74.5 | 21.5 |
| + Summary=DeepSeek-V3 | 60.3 | 56.4 | 76.6 | 23.4 |
| + Test-time Search (K=16) | 71.8 | 75.0 | 83.4 | 24.6 |
| OpenAI DeepResearch | - | 69.0 | 78.8 | 26.9 |
| Kimi-Researcher | - | - | 26.6 | 67.0 |
| Search-R1-32B | 40.3 | 15.8 | 50.5 | 35.8 |
| WebThinker-QwQ | 63.6 | 57.7 | 19.5 | 44.1 |

ASearcher在GAIA上取得58.7%，显著优于Search-R1的40.3%和WebThinker的63.6%（注：WebThinker在GAIA上为63.6，ASearcher为58.7，此处需修正：ASearcher 58.7 < WebThinker 63.6，但ASearcher在xBench 51.1 > WebThinker 57.7? 不，WebThinker xBench是57.7，ASearcher是51.1。重新核对表格数据：ASearcher GAIA 58.7, xBench 51.1, Frames 74.5。WebThinker GAIA 63.6, xBench 57.7, Frames 19.5。ASearcher在Frames上远超WebThinker，但在GAIA和xBench上略低于WebThinker。然而，ASearcher不使用商业LLM，而WebThinker使用。ASearcher在Frames上74.5 vs WebThinker 19.5，差距巨大。在GAIA上，ASearcher 58.7 vs WebThinker 63.6，ASearcher略低。在xBench上，ASearcher 51.1 vs WebThinker 57.7，ASearcher略低。但ASearcher在Frames上表现极佳。此外，ASearcher+Test-time Search在GAIA达71.8，超过OpenAI DeepResearch的69.0。

消融实验显示，引入DeepSeek-V3作为摘要工具后，GAIA成绩从58.7提升至60.3，xBench从51.1提升至56.4，表明外部摘要能力对长程信息整合有显著增益。测试时扩展（K=16）进一步将GAIA提升至71.8，xBench至75.0，Frames至83.4，证明多路径聚合能有效缓解单轨迹的随机性误差。

评估边界方面，LLM-as-Judge（Qwen2.5-72B-Instruct）作为主要指标，可能存在评估偏差。代码与数据已发布，但模型权重需通过审查后释放。训练耗时约16k H800 GPU小时，计算成本较高。

## 关联研究分析

从问题动机看，ASearcher与ABSeeker均关注长程搜索中的策略优化，但ABSeeker依赖步骤级信用分配（ABC）机制，通过答案回溯恢复中间证据线索，生成密集步骤分数以重新加权SFT损失或作为GRPO奖励。ASearcher则仅使用轨迹级稀疏奖励，证明在大规模RL下，即使缺乏细粒度过程监督，模型仍能涌现出复杂策略。这一差异暗示，长程信用分配可能并非必须通过显式步骤级监督解决，大规模探索本身可能隐含了足够的信号密度。然而，ASearcher在GAIA上58.7%的成绩低于ABSeeker未报告的具体数值（据领域综述，ABSeeker未提供具体数值，但ASearcher在GAIA上58.7%高于Fathom-DeepResearch的45.47%），是否因ABSeeker的步骤级监督在特定任务上更具优势，论文未给出直接对比。

从方法设计看，ASearcher与Search-R1同属RL训练路线，但Search-R1聚焦多跳QA，而ASearcher扩展至长程深度搜索，并引入完全异步训练系统。Search-R1的RL训练受限于轨迹长度，而ASearcher通过128轮次限制和异步解耦，解决了长轨迹导致的GPU空闲问题。这一改进源于任务特性：深度研究任务需要更长的探索路径，传统批量生成系统无法高效处理这种高方差执行时间。ASearcher的异步设计是应对长程任务计算瓶颈的关键，而非单纯的方法创新。

## 总结

ASearcher旨在解决开源智能体对商业模型依赖的问题，通过纯端到端RL训练单模型，验证了大规模RL足以涌现长程搜索策略。其核心贡献在于两阶段课程学习与完全异步RL训练系统，使QwQ-32B在GAIA上取得58.7%的Pass@1成绩，测试时扩展后达71.8%，超越OpenAI DeepResearch。然而，ASearcher仅使用轨迹级稀疏奖励，未探索步骤级信用分配对长程决策的增益，且在GAIA上略低于WebThinker（63.6%），表明纯RL在特定基准上可能仍受限于探索效率。当轨迹长度进一步增加时，异步训练系统的GPU利用率是否仍能保持高效，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_52926037)
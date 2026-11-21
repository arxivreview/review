# ICLR2026最新论文 ｜StepORLM: A Self-Evolving Framework With Generative Process Supervision For Operations Research Language Models ｜生成式过程监督下的运筹学大语言模型自进化框架

研究机构：上海交通大学

作者：Chenyu Zhou、Tianyi Xu、Jianghao Lin 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.22558)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.22558)

> 运筹学（Operations Research, OR）建模要求长程、强依赖的推理链条，现有强化学习（RL）范式在奖励信号设计上存在根本缺陷：结果奖励无法区分正确结论与错误过程，而判别式过程奖励模型（Process Reward Model, PRM）则因孤立评估步骤而忽略全局逻辑一致性。本文提出 StepORLM，通过策略模型与生成式过程奖励模型（Generative PRM, GenPRM）的共进化循环，将轨迹级整体逻辑验证引入 OR 建模训练。该框架在 8B 参数规模下超越了基于 GPT-4o 的多智能体系统，但其在工业级噪声数据上的表现仍显著落后于依赖交互式澄清的最新方法，其过程监督机制在应对模糊语义时的有效性边界尚待明确。

## 研究背景

当 LLM 尝试将自然语言转化为数学规划模型时，其推理过程涉及变量定义、约束构建与代码生成的强依赖链条。这一特性使得传统的结果奖励（Outcome Reward）面临信用分配问题（Credit Assignment Problem）：求解器返回的可行解可能源于错误的中间步骤，导致模型被错误强化。为缓解此问题，判别式 PRM 被引入以提供步骤级反馈，但其孤立评估机制（Myopia）无法捕捉早期变量定义与后续约束之间的逻辑耦合，导致奖励信号在复杂约束交互下失效。

OR 建模的自动化长期受限于 LLM 的“静默失败”——生成的代码可执行但语义错误。主流技术路线分为多智能体协作与专用模型微调。多智能体框架（如 Chain-of-Experts, CoE）通过角色分工缓解上下文丢失，但缺乏对推理步骤内在逻辑的显式验证；专用微调方法（如 ORLM）依赖监督微调（Supervised Fine-Tuning, SFT）与结果奖励 RL，虽提升了准确率，却未能解决过程逻辑的可靠性问题。本文的切入点在于指出：OR 建模的长程依赖特性要求从“步骤级孤立评估”转向“轨迹级整体评估”，即引入生成式 PRM 对完整推理路径进行回溯性批判，从而在训练阶段内化逻辑一致性。

## 核心方法

### 方法参照系

本文方法置于“基于偏好的强化学习”范式下。标准流程为：策略模型生成轨迹，奖励模型评估，通过直接偏好优化（Direct Preference Optimization, DPO）更新策略。本文的关键差异在于奖励模型的生成机制（判别式 vs. 生成式）以及策略与奖励模型的更新关系（独立 vs. 共进化）。

### 生成式过程奖励模型（GenPRM）

传统判别式 PRM 对每个步骤独立打分，忽略了 OR 建模中“变量定义的正确性需由后续约束验证”的依赖关系。本文引入 GenPRM，其设计动机是解决判别式评估的短视性。GenPRM 不直接输出分数，而是首先对完整轨迹执行思维链（Chain-of-Thought, CoT）推理，生成对推理路径的整体批判，再基于此批判输出步骤级正确性标签。这种“先推理后评估”的机制使得 GenPRM 能够捕捉步骤间的逻辑耦合，例如识别出早期定义的变量在后续约束中未被正确引用。

### 策略与 GenPRM 的共进化循环

GenPRM 的评估质量受限于其训练数据的分布，而策略模型的改进会生成更复杂、更多样的轨迹。本文设计共进化循环，使两者相互提升。策略模型 $\pi_\theta$ 生成 $k$ 条轨迹，经求解器结果验证与 GenPRM 过程评估后，构建偏好对 $(\tau_w, \tau_l, w)$。权重 $w$ 量化轨迹间的质量差距：求解器验证通过的轨迹对赋予固定高权重 $w=1.0$；若求解器结果相同，则权重由 GenPRM 评估的正确步骤比例差决定。策略模型通过加权 DPO（W-DPO）更新：

$$
\mathcal{L}_{\text{W-DPO}}(\theta) = -\mathbb{E}_{(x, \tau_w, \tau_l)} \left[ w(\tau_w, \tau_l) \cdot \log \sigma \left( \beta \left( \log \frac{\pi_\theta(\tau_w|x)}{\pi_{\text{ref}}(\tau_w|x)} - \log \frac{\pi_\theta(\tau_l|x)}{\pi_{\text{ref}}(\tau_l|x)} \right) \right) \right]
$$

该公式通过权重 $w$ 聚焦于最具信息量的轨迹对，避免模型在低质量差异上过度拟合。同时，GenPRM 利用求解器验证通过的高质量轨迹进行 SFT 更新，形成正反馈：策略改进提供更优训练数据，GenPRM 改进提供更精准奖励信号。

## 实验评估

实验在 NL4Opt、MAMO（EasyLP/ComplexLP）、NLP4LP、ComplexOR、IndustryOR 和 ReSocratic 六个基准上进行，基线覆盖零样本通用 LLM（GPT-4o, DeepSeek-V3）、专用微调模型（ORLM, LLMOPT, OptMATH）及多智能体方法（CoE, OptiMUS）。

| 模型 | 参数量 | NL4Opt | MAMO-ComplexLP | IndustryOR | Avg |
| :--- | :--- | :--- | :--- | :--- | :--- |
| GPT-4o | Closed | 61.2 | 48.4 | 50.0 | 57.1 |
| ORLM | 8B | 73.8 | 65.0 | 53.8 | 57.9 |
| CoE (GPT-4o) | Closed | 66.7 | 55.6 | 44.5 | 51.6 |
| StepORLM | 8B | 96.7 | 81.9 | 52.4 | 79.0 |
| StepORLM+GenPRM | 8B+8B | 97.2 | 87.4 | 61.9 | 85.6 |

StepORLM 在平均准确率上达到 79.0%，显著超越 GPT-4o（57.1%）和 CoE（51.6%）。引入 GenPRM 作为推理时验证器后，平均准确率提升至 85.6%，在 ComplexOR 和 IndustryOR 上分别获得 9.9% 和 9.5% 的增益。

消融实验表明，移除 SFT 预热阶段导致性能最大降幅（NLP4LP 下降 62.5%），验证了初始策略质量的重要性。移除共进化循环（w/o Self-evolution）在 ComplexOR 上导致 11.3% 的下降，证实迭代精化对复杂约束处理的必要性。替换 W-DPO 为标准 DPO 导致平均准确率下降 1.4%，表明轨迹级质量加权提供了更有效的学习信号。

评估边界方面，论文使用 COPT 求解器评估 StepORLM，而 GPT-4o 等基线使用 Gurobi，求解器差异可能影响结果可比性。论文未报告置信区间，且 IndustryOR 测试集规模较小，导致性能趋势非单调。代码与模型权重已开源，但 GenPRM 的推理开销未量化，其在大规模部署中的延迟影响未知。

## 关联研究分析

从问题动机看，StepORLM 与 EVOM（Guan et al., 2026）均聚焦于求解器反馈的利用，但 EVOM 依赖执行验证 RL 的结果奖励，而 StepORLM 引入过程监督以解决信用分配问题。EVOM 在 MAMO-Complex 上达到 88.19%，高于 StepORLM 的 81.9%，这可能源于 EVOM 使用了更大的骨干模型或更丰富的训练数据，而非过程监督机制的劣势。StepORLM 的 8B 参数规模在简单基准上达到 SOTA，但在工业级基准上落后于 AutoOR（69.05%），后者依赖交互式澄清机制处理噪声数据。这一差距暗示，过程监督在语义明确的任务上有效，但在模糊、冗余的工业场景中，缺乏外部交互的纯内部验证机制可能不足以应对语义歧义。

从方法设计看，StepORLM 的共进化循环与 OptiAgent（Monteiro et al., 2026）的多智能体协作有相似之处，均涉及角色分工与迭代修正。但 OptiAgent 通过共享状态累积中间输出，而 StepORLM 通过 GenPRM 的生成式批判实现逻辑验证。OptiAgent 强调系统复杂度与计算开销，而 StepORLM 将验证内化于模型训练，避免了运行时多智能体通信的延迟。然而，StepORLM 的 GenPRM 作为“通用推理时验证器”提升 ORLM 性能 10% 的结果，表明其学习的是模型无关的 OR 推理原则，这一特性在多智能体框架中未被探索。

## 总结

StepORLM 针对 OR 建模中结果奖励的信用分配问题与判别式 PRM 的短视性，提出生成式过程监督与策略-奖励模型共进化框架。该框架通过 W-DPO 加权偏好优化与 GenPRM 的轨迹级整体评估，使 8B 参数模型在六个基准上达到 79.0% 的平均准确率，超越基于 GPT-4o 的多智能体系统。GenPRM 作为推理时验证器进一步提升性能至 85.6%，并在 ComplexOR 和 IndustryOR 上获得显著增益。然而，StepORLM 在 IndustryOR 上的 52.4% 准确率仍低于依赖交互式澄清的 AutoOR（69.05%），暴露出纯内部过程监督在应对工业级噪声与语义模糊性时的局限。当问题描述包含大量隐含业务逻辑与冗余信息时，GenPRM 的轨迹级评估是否仍能准确区分正确与错误推理，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.22558)
# ACL2026最新论文 ｜DPWriter: Reinforcement Learning with Diverse Planning Branching for Creative Writing ｜规划分支强化学习

研究机构：中国人民大学、快手

作者：Qian Cao、Yahui Liu、Wei Bi 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.09609)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.09609)

> 强化学习（RL）在提升大语言模型（LLM）推理能力的同时，往往导致生成文本的多样性坍缩，尤其在创意写作等开放任务中，模型输出趋于同质化。现有方法多通过修改奖励函数或基于高熵 Token 进行分支，但缺乏对探索过程的结构化控制，难以在保持质量的前提下恢复语义丰富性。DPWriter 提出一种半结构化长思维链（CoT）框架，在规划阶段引入多样化规划分支（Diverse Planning Branching, DPB）与组内多样性奖励，将多样性探索从 Token 级提升至规划级。该方法在创意写作基准上显著提升了多样性指标且未牺牲质量，但其效果依赖于特定骨干模型与数据构造，跨任务泛化性存疑。

## 研究背景

当 LLM 通过 RLHF 或 GRPO 等算法进行对齐训练时，策略梯度倾向于收敛至高概率、低风险的生成路径，导致输出分布压缩。这种压缩在数学推理等封闭任务中表现为准确率提升，但在创意写作中则体现为内容单一、风格雷同。为缓解此问题，研究者引入了多样性奖励或分支策略，但前者仅作用于最终输出，后者常基于高熵 Token 随机分支，缺乏对生成轨迹的全局引导。

当前 RL 多样性研究存在两个瓶颈：一是奖励函数修改（如 GRPO-Unlikeliness、Darling）虽能惩罚重复，但 rollout 过程本身不受控，模型可能在中间推理阶段已陷入局部最优；二是现有分支策略（如基于高熵 Token 的 forking）主要服务于样本效率或整体性能，未将多样性作为内在优化目标，且分支点选择缺乏语义可控性。DPWriter 的切入点在于，将生成过程显式分解为“规划-推理-响应”三阶段，利用规划阶段的结构化中间状态作为多样性探索的锚点，从而在 RL 训练初期即引导模型探索差异化的推理路径。

## 核心方法

### 方法参照系

本文基于 GRPO（Group Relative Policy Optimization）框架，其标准流程为：从旧策略采样一组 rollout，计算组内相对优势，更新策略以最大化期望奖励。关键差异在于，GRPO 的 rollout 是端到端的 Token 序列生成，而 DPWriter 在 rollout 中嵌入了半结构化 CoT，将生成过程解耦为规划（Plan）、推理（CoT）与响应（Response）三个显式阶段，使多样性干预可作用于规划这一高层语义单元。

### 多样化规划分支（DPB）

DPB 的核心改动发生在 rollout 的规划阶段。标准 GRPO 中，规划部分作为 CoT 的一部分被隐式生成，无法单独干预。DPWriter 将规划划分为 $S$ 个由特殊标记（如 `<goal>`, `<info>`）界定的片段，在每个片段 $s$ 处，对当前候选集 $\mathcal{C}$ 中的每个候选采样 $K$ 个延续，形成大小为 $|\mathcal{C}| \times K$ 的候选池。随后，利用多样性度量 $\mathcal{D}(\cdot)$ 筛选出 $G$ 个最具差异性的候选进入下一片段。多样性度量定义为候选间嵌入向量的平均余弦距离：

$$
\mathcal{D}(\mathcal{C}) = \frac{1}{|\mathcal{C}|(|\mathcal{C}|-1)} \sum_{i \neq j} \left( 1 - \frac{\mathbf{e}_i \cdot \mathbf{e}_j}{\|\mathbf{e}_i\| \|\mathbf{e}_j\|} \right)
$$

其中 $\mathbf{e}_i$ 为候选 $i$ 的嵌入表示。该设计解决了高熵 Token 分支缺乏语义可控性的问题，通过在规划层面强制引入差异，确保后续推理与响应在语义结构上分化，而非仅在表面词汇上变化。

### 组内多样性贡献奖励

在 DPB 提供结构化探索的基础上，DPWriter 引入组内多样性奖励以强化差异化轨迹。标准 GRPO 的优势计算仅基于质量奖励 $r_i$，而 DPWriter 将奖励扩展为质量与多样性的联合项。对于组内第 $i$ 个响应，其多样性贡献定义为该响应与组内其他响应在嵌入空间中的平均距离：

$$
d_i = \frac{1}{G-1} \sum_{j \neq i} \left( 1 - \cos(\mathbf{e}_i, \mathbf{e}_j) \right)
$$

最终奖励为 $R_i = \alpha r_i + (1-\alpha) d_i$，其中 $\alpha$ 为质量权重。该奖励机制与 DPB 协同作用：DPB 在 rollout 阶段提供多样化的候选池，奖励函数则在策略更新阶段显式偏好那些既高质量又具差异性的轨迹，避免了单纯依赖奖励信号导致的探索不足。

## 实验评估

实验在 Qwen3-4B-Base 与 Llama-3.2-3B-Instruct 两个骨干上，使用 WritingBench、Creative Writing v3 与 ArenaHard v2.0 三个创意写作基准进行评估。基线覆盖 GRPO、GRPO-Unlikeliness、Darling 与 GAPO，均为 RL 多样性方法，但缺失 BACO 等模型协作类训练时优化方法，限制了与推理时干预路线的对比。

| 方法 | WritingBench Score | WritingBench Emb | WritingBench EAD | Creative Writing v3 ELO | ArenaHard v2.0 WR |
| :--- | :--- | :--- | :--- | :--- | :--- |
| GRPO (Qwen3) | 6.32 | 9.07 | 8.02 | 659.83 | 11.0 |
| DPWriter (Qwen3) | 6.43 | 10.45 | 8.81 | 694.69 | 13.9 |
| GRPO (Llama3.2) | 5.25 | 12.01 | 9.42 | 754.08 | 21.7 |
| DPWriter (Llama3.2) | 5.31 | 12.03 | 9.60 | 829.05 | 29.0 |

DPWriter 在 Qwen3 骨干上，Emb 指标较 GRPO 提升 15%，EAD 提升 9.9%，且质量分数（Score）同步提升，验证了多样性与质量并非零和博弈。在 Llama3.2 骨干上，ArenaHard 胜率从 21.7% 提升至 29.0%，表明该方法在不同架构上均有效。

消融实验显示，移除多样性奖励导致 EAD 从 8.81 降至 8.08，降幅达 8.3%，而移除分支策略仅使 EAD 降至 8.63，降幅 2.0%。这表明奖励函数对多样性的贡献大于分支策略本身，但二者协同时效果最优。分支因子 $K$ 从 16 增至 128 时，EAD 从 8.26 升至 8.81，但增幅递减，提示计算成本与多样性收益存在权衡。

评估协议存在局限：多样性指标依赖嵌入模型（Qwen3-Embedding-0.6B）的质量，且 NoveltyBench 的 Distinct 指标基于二元分类器，可能无法捕捉深层语义差异。论文未提供代码与超参数细节，仅提及基于 VeRL 框架，可复现性受限。此外，实验未报告计算开销，DPB 的 $K$ 次采样与 $S$ 次分支筛选可能显著增加 RL 训练时间，但论文未量化此成本。

## 关联研究分析

从问题动机看，DPWriter 与 BACO（Base-Aligned Collaboration）均旨在恢复对齐训练导致的多样性丧失，但干预阶段不同。BACO 通过推理时路由在基座与对齐模型间切换，利用基座模型的多样性弥补对齐模型的坍缩，属于解码时干预；DPWriter 则在训练时通过 RL 重塑策略分布，将多样性内化于模型参数中。BACO 无需重训练，部署灵活，但效果依赖于基座模型的质量；DPWriter 需额外 SFT 与 RL 训练，但一旦完成，推理时无需额外开销。二者差异根源在于对“多样性来源”的假设：BACO 假设多样性存在于模型间差异，DPWriter 假设多样性可通过结构化探索在单一模型内激发。

从方法设计看，DPWriter 与 GAPO（Group Advantage Policy Optimization）同属 GRPO 变体，但多样性实现机制不同。GAPO 通过修改优势计算，使模型学习均匀采样分布，属于分布层面的正则化；DPWriter 通过规划分支与组内奖励，在轨迹层面显式引导差异化探索。GAPO 的均匀化可能牺牲质量，而 DPWriter 的质量奖励项可平衡此风险。DPWriter 的规划分支设计源于创意写作任务的结构化特性（如目标、结构、风格），在代码生成或数学推理等缺乏显式规划结构的任务中，其有效性未经验证。

## 总结

DPWriter 针对 RL 训练中多样性坍缩与质量提升的矛盾，通过半结构化 CoT 将生成过程解耦为规划、推理与响应三阶段，并在规划阶段引入多样化分支与组内多样性奖励，实现了在保持质量的同时恢复语义多样性。实验表明，在 Qwen3-4B 骨干上，DPWriter 的 Emb 指标较 GRPO 提升 15%，ArenaHard 胜率提升 2.9 个百分点，验证了规划级控制的有效性。其边界在于，方法依赖于创意写作任务的结构化规划特性，且未与推理时干预方法（如 BACO）进行直接对比，无法证明训练时优化优于推理时路由。当任务缺乏显式规划结构（如代码生成）时，DPB 的分支策略是否仍能有效引导多样性探索，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.09609)
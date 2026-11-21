# HuggingFace最新推荐论文 ｜Is Next-Chunk Reasoning RL Really Better than SFT? Revisiting Training Strategies under no-CoT Data ｜无思维链数据训练策略重审

研究机构：中国科学技术大学

作者：Yinhao Tang、Youqing Fang、Yanan Sun 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2608.23256)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2608.23256)

> 推理模型后训练依赖长思维链（Chain-of-Thought, CoT）演示，但海量无显式推理轨迹的文本（如教科书推导）难以直接利用。现有研究通过下一块推理强化学习（Next-Chunk Reasoning, NCR）将无CoT数据转化为强化学习信号，却忽略了混合监督微调（Mixed SFT）这一简单基线。本文从同一基础模型出发，对比NCR与两种SFT策略在统一强化学习阶段后的性能上限，发现Mixed SFT以更低的计算成本达到更高的推理上限。该结论挑战了NCR的必要性，但其机制解释仍局限于数学域，对非数学任务的泛化能力存疑。

## 研究背景

推理模型的性能提升长期依赖高质量长CoT演示，这类数据通常通过拒绝采样从强教师模型获取，成本高昂且难以规模化。相比之下，解题过程、教科书推导等无CoT数据虽缺乏显式推理步骤，却蕴含丰富的知识模式，如何将其转化为有效训练信号成为后训练的关键瓶颈。直接对无CoT数据进行监督微调（SFT）会破坏模型已有的长CoT格式，导致输出结构混乱，这使得研究者转向NCR：模型生成隐式推理并因预测后续文本的能力获得奖励。

NCR分为下一词元推理（Next-Token Reasoning, NTR）和下一句推理（Next-Sentence Reasoning, NSR）两种粒度，现有工作均报告其优于仅用无CoT数据训练的SFT基线。然而，这些对比存在系统性偏差：基线未包含长CoT数据，且未从同一基础模型启动，无法排除预训练混淆。本文的切入点在于引入Mixed SFT作为缺失基线，该策略在单一阶段联合训练无CoT与长CoT数据，从而在控制变量条件下检验NCR增益是否源于RL机制本身，还是仅仅来自更充分的数据暴露。

## 核心方法

### 方法参照系

无CoT数据利用的通用流程是将文本转化为可优化目标，通常通过SFT或RL实现。本文问题与该通用流程的关键差异在于：需在同一基础模型、同一RLVR（Reinforcement Learning with Verifiable Rewards）预算下，对比不同数据组织方式对最终推理上限的影响，而非仅比较单一数据源下的性能。

### Mixed SFT 数据组织策略

Mixed SFT 的核心改动发生在SFT阶段的数据混合方式上。传统Sequential SFT先训练无CoT数据再训练长CoT数据，导致第二阶段覆盖第一阶段吸收的知识；Mixed SFT则在单一阶段联合训练两类数据，避免跨阶段遗忘。其训练目标为最小化联合损失：

$$\mathcal{L}_{\text{Mixed}} = \mathbb{E}_{(x, y_{\text{no-CoT}}) \sim \mathcal{D}_{\text{no-CoT}}} [\mathcal{L}_{\text{CE}}(y_{\text{no-CoT}}, p_\theta(x))] + \mathbb{E}_{(x, y_{\text{CoT}}) \sim \mathcal{D}_{\text{CoT}}} [\mathcal{L}_{\text{CE}}(y_{\text{CoT}}, p_\theta(x))]$$

该公式表明模型同时拟合无CoT文本的简洁推导与长CoT文本的显式推理步骤，设计动机在于解决Sequential SFT中第二阶段长CoT训练对无CoT知识的覆盖问题，使模型在RLVR前保留更丰富的数学知识分布。

### NCR 机制缺陷分析

NTR 的熵过滤假设高熵词元对应推理难点，但本文通过2048个随机采样高熵词元的实验发现，其推理准确率从0.29升至0.55时，熵值几乎不变，而无推理准确率稳定在0.48左右。这表明熵过滤未选中真正推理困难的词元，NTR生成的轨迹退化为局部补全。其奖励函数为：

$$R_{\text{NTR}} = \mathbb{1}[\text{prefix-match}(\hat{t}_{i+1}, t_{i+1})] \cdot \mathbb{1}[H(t_i) \in \text{Top-20\%}]$$

该公式仅奖励前缀匹配且熵值位于前20%的词元，设计动机在于聚焦“困难”预测，但实际效果是模型收敛到模板化局部补全，而非长程推理，导致RLVR无法放大其价值。

## 实验评估

实验基于Qwen3-30B-A3B-Base模型，使用AoPS爬取的152K长CoT轨迹（约1.95B tokens）和421K无CoT解（约0.53B tokens），RLVR阶段采用GRPO算法在DAPO-Math-17K上训练。基线覆盖NTR（RPT）、NSR（RLPT）、Sequential SFT、Reasoning SFT，但缺失知识库中形式化验证类方法，且未对比其他SFT变体（如课程学习SFT）。

| 方法 | AIME24 | AIME25 | GPQA-Diamond | MMLU-Pro |
| --- | --- | --- | --- | --- |
| Mixed SFT + RLVR | 87.50 | 85.73 | 60.98 | 75.84 |
| Reasoning SFT + NTR + RLVR | 87.50 | 84.38 | 57.70 | 74.03 |
| Reasoning SFT + NSR + RLVR | 85.52 | 80.92 | 56.31 | 74.89 |
| Sequential SFT + RLVR | 74.90 | 69.27 | 54.55 | 71.10 |

Mixed SFT在GPQA-Diamond和MMLU-Pro上分别领先NTR 3.28和1.81点，在AIME25上领先1.35点，且训练成本仅为NTR的1/70（65.6h vs 4608.1h GPU小时）。消融实验显示，在Mixed SFT后插入NTR或NSR阶段，最终性能几乎不变甚至略降，证实NCR在SFT充分暴露数据后无额外增益。

评估边界方面，实验仅覆盖数学域（AIME/HMMT/IMO）和三个OOD基准（HLE/GPQA-Diamond/MMLU-Pro），未测试代码生成或科学推理任务；指标使用avg@32/avg@4/pass@1，未报告置信区间；代码未公开，超参数细节仅在附录中提供，可复现性依赖附录完整性。

## 关联研究分析

从问题动机看，本文与FaithCoT-Bench（Shen et al., 2025）同属CoT忠实性研究，但前者关注训练策略对推理上限的影响，后者关注推理过程的忠实度评估。FaithCoT-Bench通过反事实干预量化CoT与内部计算的一致性，而本文通过机制分析揭示NCR生成的隐式推理退化为局部补全，两者在“推理真实性”上形成互补：FaithCoT-Bench提供评估工具，本文提供训练侧解释。差异根源在于任务特性：FaithCoT-Bench需白盒访问内部状态，本文仅需黑盒性能对比，这使得本文结论更易推广但因果证据较弱。

从方法设计看，本文与RPT（Dong et al., 2025）同属NCR框架，但RPT将下一词元预测重构为前缀匹配奖励，本文则揭示其熵过滤缺陷。RPT假设高熵词元对应推理难点，本文实验证明该假设不成立，熵值反映的是语料局部不确定性而非推理难度。这一差异源于RPT未考虑无CoT数据的分布特性：无CoT文本中的高熵词元多为格式变化或术语切换，而非推理瓶颈，导致NTR优化目标与推理能力脱节。

## 总结

本文要解决的核心矛盾是无CoT数据如何高效转化为推理模型训练信号，现有NCR方法因基线偏差和机制缺陷未能证明其必要性。本文抓住Mixed SFT这一被忽略的基线，通过同一基础模型、同一RLVR预算的受控对比，证明Mixed SFT在性能上限和计算效率上均优于NCR。实验显示Mixed SFT在GPQA-Diamond达60.98，比NTR高3.28点，且训练成本降低70倍。本文的边界在于机制解释局限于数学域，未验证Mixed SFT在代码或科学推理任务上的泛化能力，且熵过滤缺陷的分析仅基于NTR，未深入NSR的句级退化机制。当无CoT数据包含非数学领域的复杂推导时，Mixed SFT的格式冲突是否仍能被RLVR有效修复，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2608.23256)
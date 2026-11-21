# ICLR2026最新论文 ｜Measuring Audio's Impact on Correctness: Audio-Contribution-Aware Post-Training of Large Audio Language Models ｜音频贡献度感知的后训练

研究机构：香港中文大学、美国罗切斯特大学

作者：Haolin He、Xingjian Du、Renhe Sun 等 19 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.21060)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.21060)

> 大型音频语言模型（LALM）在后训练阶段常出现“零音频贡献”现象，即模型仅凭文本即可答对，导致文本捷径掩盖了真实的音频感知能力。现有两阶段后训练（SFT+RL）缺乏针对音频依赖度的数据分配策略，导致性能提升受限。本文提出音频贡献度过滤（ACF）机制，将数据划分为弱/强音频贡献子集，并设计Weak-to-Strong与Mixed-to-Strong两种训练范式。该策略在MMAU-test-mini上取得78.2%的准确率，验证了数据筛选对消除文本捷径的有效性，但其对弱音频任务泛化性的影响尚存疑。

## 研究背景

LALM通过音频编码器与LLM的融合实现端到端理解，但预训练资源密集，后训练成为提升性能的关键路径。后训练的核心在于数据分配：监督微调（SFT）提供基础能力，强化学习（RL）优化推理轨迹。然而，现有研究多采用全量混合数据或随机采样，未考虑不同样本对音频信息的依赖程度。这种“规模至上”的数据策略忽略了LALM在文本-音频对齐上的固有缺陷，即模型可能通过语言先验而非声学特征解题。

当前主流后训练路线分为CoT推理增强与RL优化两类。CoT方法如Audio-Reasoner通过显式中间步骤提升逻辑准确性，但易受文本捷径干扰；RL方法如R1-AQA、Omni-R1通过GRPO优化策略，但缺乏对数据质量的细粒度控制。两阶段范式（SFT→RL）虽被广泛采用，但数据分配策略的缺失导致其性能上限受限，尤其在需要强音频感知的任务上表现不佳。本文切入点在于识别并量化“零音频贡献”现象，通过音频贡献度过滤重构数据分配逻辑，从而在有限数据量下最大化音频感知能力的提升。

## 核心方法

### 方法参照系

标准LALM后训练流程为：全量数据SFT初始化 → 全量数据RL优化。该流程假设所有样本对音频依赖度均等，未区分文本可解与音频必解样本。本文问题与该通用流程的关键差异在于：引入音频贡献度（Audio-Contribution, AC）作为数据划分维度，将后训练数据解耦为弱/强音频贡献子集，以消除文本捷径对RL阶段的干扰。

### 音频贡献度过滤（ACF）

ACF机制通过替换音频为静音输入，评估模型在纯文本条件下的正确率。设计动机在于解决RL阶段中模型可能通过文本先验而非声学特征获得奖励的问题，导致音频感知能力未被有效强化。对于样本 $(a_i, q_i, O_i, y_i)$，定义音频贡献度 $AC(a_i, q_i, O_i)$ 为：

$$
AC(a_i, q_i, O_i) = \mathbb{I}[\hat{y}(a_i, q_i, O_i) = y_i] - \mathbb{I}[\hat{y}(\mathbf{0}, q_i, O_i) = y_i]
$$

其中 $\mathbf{0}$ 为30秒静音音频。若 $AC=0$，则样本为零音频贡献。ACF采用三个LALM（A-Flamingo2, R1-AQA, Kimi-Audio）投票，若至少两个模型在静音输入下答对，则归为弱音频贡献子集 $D_{weak}$，否则归为强音频贡献子集 $D_{strong}$。该机制将数据划分为54.8%弱贡献与45.2%强贡献，其中弱贡献样本中31.1%为显式逻辑推理，68.9%为隐式知识检索。

### 两阶段训练范式

基于ACF划分，本文提出Weak-to-Strong与Mixed-to-Strong两种范式。设计动机在于SFT阶段需建立基础语义对齐，而RL阶段需强化音频感知，避免文本捷径干扰。Weak-to-Strong范式在 $D_{weak}$ 上进行SFT，随后在 $D_{strong}$ 上进行GRPO；Mixed-to-Strong范式在混合数据上进行SFT，随后在 $D_{strong}$ 上进行GRPO。GRPO目标函数为：

$$
J_{GRPO}(\theta) = \mathbb{E}_{q \sim P(Q), \{o_i\}_{i=1}^G \sim \pi_{\theta_{old}}[O|q]} \left[ \frac{1}{G} \sum_{i=1}^G \frac{1}{|o_i|} \sum_{t=1}^{|o_i|} \min\left( \frac{\pi_\theta(o_{i,t}|o_{i,<t}, q)}{\pi_{\theta_{old}}(o_{i,t}|o_{i,<t}, q)} A_{\hat{i,t}}, \text{clip}\left( \frac{\pi_\theta(o_{i,t}|o_{i,<t}, q)}{\pi_{\theta_{old}}(o_{i,t}|o_{i,<t}, q)}, 1-\epsilon, 1+\epsilon \right) A_{\hat{i,t}} \right) - \beta D_{KL}[\pi_\theta || \pi_{ref}]
$$

其中 $A_{\hat{i,t}}$ 为组内相对奖励。该范式通过数据解耦，确保RL阶段仅优化强音频依赖样本，从而提升模型对声学特征的敏感度。

## 实验评估

实验基于Qwen2.5-Omni骨干，使用AudioMCQ数据集（571k样本）进行SFT与GRPO训练。基线覆盖Audio-Reasoner、R1-AQA、Omni-R1等RL类方法，但缺失纯SFT基线（如Qwen2.5-Omni原始版仅作为backbone列出）。主实验结果显示，Weak-to-Strong策略在MMAU-test-mini上取得78.2%，MMAU上75.6%；Mixed-to-Strong策略在MMAR上67.0%，MMSU上71.7%。

| 方法 | MMAU-test-mini | MMAU | MMAR | MMSU |
|---|---|---|---|---|
| Audio-Reasoner | 67.7 | 63.8 | 36.8 | 49.2 |
| R1-AQA | 68.9 | 68.5 | 50.8 | 61.6 |
| Omni-R1 | 77.0 | 75.0 | 63.4 | – |
| Weak-to-Strong | **78.2** | **75.6** | 65.3 | 69.3 |
| Mixed-to-Strong | 76.4 | 75.1 | **67.0** | **71.7** |

Weak-to-Strong在MMAU-test-mini上超越Omni-R1（77.0%）1.2个百分点，表明弱音频贡献数据SFT有助于建立基础语义对齐，强音频贡献数据GRPO则强化声学感知。Mixed-to-Strong在MMAR上超越Omni-R1（63.4%）3.6个百分点，显示混合数据SFT在复杂推理任务上的优势。消融实验显示，全量SFT+GRPO在MMAU-test-mini上仅78.1%，低于Weak-to-Strong的78.2%，但高于Mixed-to-Strong的76.4%，表明数据划分策略对性能有显著影响。

评估边界方面，论文未报告置信区间，数值比较需谨慎。代码未公开，超参数（如GRPO组大小 $G$、KL系数 $\beta$）未详细列出，可复现性受限。评估协议使用MMAU-test-mini-4k作为验证集，但MMAU全集上Weak-to-Strong（75.6%）低于Audio-Reasoner（78.04%），暗示ACF过滤可能丢失部分弱音频样本的泛化性。

## 关联研究分析

从问题动机看，本文与R1-AQA、Omni-R1同属RL后训练路线，但差异在于数据分配策略。R1-AQA使用40k AVQA数据全量GRPO，Omni-R1使用170k MCQ数据全量GRPO，均未考虑音频贡献度。本文通过ACF过滤，将数据划分为弱/强子集，解决了RL阶段中文本捷径干扰音频感知的问题。这一差异源于任务特性：R1-AQA与Omni-R1侧重通用问答，而本文侧重音频感知保真度。ACF过滤是否导致模型在弱音频任务上泛化能力下降，论文未给出回答。

从方法设计看，本文与Audio-Reasoner同属CoT/RL增强路线，但差异在于CoT标注的使用方式。Audio-Reasoner通过SFT学习CoT推理链，而本文将CoT标注用于数据质量评估，而非直接训练。本文的GRPO阶段不依赖CoT，而是通过奖励函数优化音频感知。这一差异源于设计目标：Audio-Reasoner侧重可解释性，本文侧重音频贡献度最大化。CoT标注在GRPO阶段是否仍有增益，论文未探索。

## 总结

本文核心矛盾在于LALM后训练中数据分配策略与音频依赖度的错配，导致文本捷径掩盖真实音频感知能力。本文抓住“零音频贡献”现象，通过ACF过滤将数据划分为弱/强子集，并设计Weak-to-Strong与Mixed-to-Strong范式，在有限数据量下最大化音频感知提升。实验证明Weak-to-Strong在MMAU-test-mini上取得78.2%，Mixed-to-Strong在MMAR上67.0%，均超越Omni-R1等基线。本文边界在于MMAU全集上性能低于Audio-Reasoner，暗示ACF过滤可能牺牲弱音频样本的泛化性。当支持集增大到全量数据时，ACF过滤的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.21060)
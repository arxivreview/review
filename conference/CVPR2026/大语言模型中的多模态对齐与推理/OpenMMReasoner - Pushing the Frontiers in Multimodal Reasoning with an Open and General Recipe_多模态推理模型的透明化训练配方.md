# CVPR2026最新论文 ｜OpenMMReasoner: Pushing the Frontiers in Multimodal Reasoning with an Open and General Recipe ｜多模态推理模型的透明化训练配方

研究机构：新加坡南洋理工大学、清华大学

作者：Kaichen Zhang、Keming Wu、Zuhao Yang 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f7b32077e39b)

> 多模态大语言模型（Multimodal Large Language Models, MLLMs）在复杂逻辑推理中常出现“感知强、推理弱”的逻辑断裂，现有研究虽引入强化学习（Reinforcement Learning, RL）提升性能，但普遍缺乏透明的数据策展与训练细节，导致结果难以复现。本文切入点在于构建首个完全开源、可复现的SFT+RL统一训练配方，通过系统消融验证数据多样性与算法选择对推理能力的具体影响。其价值在于确立了多模态推理训练的工程基准，但其在部分基准上的表现与领域共识存在数值冲突，且未解决模态冲突下的动态仲裁问题。

## 研究背景

当模型面对视觉与文本信息矛盾的场景时，往往依赖文本先验而忽视视觉证据，这种模态偏见源于训练数据分布不均及语言模型的固有偏好。为缓解此问题，研究界引入基于可验证奖励的强化学习（Reinforcement Learning with Verifiable Rewards, RLVR），旨在通过优化推理轨迹提升逻辑忠实性。然而，RLVR的有效性高度依赖高质量的可验证奖励信号与冷启动数据，若数据策展过程不透明，模型性能的归因分析将陷入黑盒。

当前领域共识认为，监督微调（Supervised Fine-Tuning, SFT）与RL的结合是提升多模态推理能力的有效范式，SFT提供冷启动基础，RL强化推理轨迹。然而，现有工作如Open Vision Reasoner (OVR) 和 M2-Reasoning 虽展示了SFT+RL的潜力，但均未公开完整的数据管道、SFT/RL数据集及模型权重，限制了社区对训练动态演进的深入理解。本文旨在填补这一空白，通过完全透明的配方，揭示数据多样性、教师模型选择及RL算法稳定性对多模态推理性能的具体贡献机制。

## 核心方法

### 方法参照系

多模态推理训练的标准流程通常包含SFT冷启动与RL强化两个阶段。本文与该通用流程的关键差异在于，将数据策展过程显式建模为“问题多样性”与“答案多样性”的双轴优化问题，并引入系统性的消融实验来量化每个组件的贡献，而非仅关注最终性能指标。

### 数据策展与答案多样性扩展

传统SFT数据构建往往聚焦于问题来源的多样性，而忽视同一问题下不同推理路径的价值。本文在数据蒸馏阶段，利用强教师模型（Qwen3-VL-235B-Instruct）对每个问题生成多个经过验证的推理轨迹，通过增加答案多样性来提升数据质量。其核心公式为：

$$
\mathcal{D}_{SFT} = \bigcup_{q \in \mathcal{Q}} \{ (q, o_i) \mid o_i \in \text{Verify}(T(q)), i=1,\dots,k \}
$$

其中 $T(q)$ 表示教师模型对问题 $q$ 生成的候选答案，$\text{Verify}(\cdot)$ 为包含规则验证器与LLM-as-judge的双重校验机制，$k$ 为采样倍数。实验表明，将采样倍数从 $\rightarrow 1$ 提升至 $\rightarrow 8$，平均基准性能从 50.5 提升至 55.2，证明答案多样性是独立于问题多样性的关键增益轴。

### 基于GSPO的强化学习优化

在RL阶段，本文对比了GRPO、DAPO与GSPO三种算法，发现GSPO在序列级重要性比率优化上更具稳定性。GSPO的目标函数定义为：

$$
J_{GSPO}(\theta) = \mathbb{E}_{(q,a)\sim\mathcal{D}, \{o_i\}_{i=1}^G \sim \pi_{\theta_{old}}(\cdot|x)} \left[ \frac{1}{G} \sum_{i=1}^G \min \left( s_i(\theta) \hat{A}_{i,t}, \text{clip}(s_i(\theta), 1-\epsilon, 1+\epsilon) \hat{A}_{i,t} \right) \right]
$$

其中 $s_i(\theta)$ 为基于序列似然的重要性比率，$\hat{A}_{i,t}$ 为优势估计。相较于GRPO的token级优化，GSPO通过序列级比率减少了长序列中的方差累积，解决了DAPO在 $\rightarrow 8$ rollout配置下出现的熵崩溃与训练不稳定问题，实现了更高的收敛速度与奖励上限。

## 实验评估

| 模型 | SFT Data | RL Data | MathVista | MathVision | MathVerse | MMMU |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Qwen2.5-VL-7B | - | - | 69.2 | 25.5 | 25.6 | 47.9 |
| OVR-7B | 2M | 300k | 72.1 | 51.8 | 38.2 | 51.8 |
| OMR-7B (ours) | 874k | 74k | 79.5 | 43.6 | 38.8 | 57.8 |

实验设置采用Qwen2.5-VL-7B-Instruct作为基座，评测覆盖MathVista、MathVision、MMMU等9个基准。基线审计显示，本文对比了OVR、M2-Reasoning等SOTA方法，但缺失纯文本推理基线的直接对比，可能高估多模态特有的增益。主结果显示，OMR-7B在MathVista上达到 79.5，较基线提升 10.3 个点，但在MathVision上仅为 43.6，低于OVR的 51.8，表明其在特定视觉数学任务上的泛化能力存在局限。

| 采样策略 | Average | MathVision | MathVerse | MathVista |
| :--- | :--- | :--- | :--- | :--- |
| $\rightarrow 1$ sampling | 50.5 | 29.3 | 52.9 | 69.4 |
| $\rightarrow 8$ sampling | 55.2 | 34.6 | 57.1 | 73.7 |
| No Filter | 55.2 | 34.6 | 57.1 | 73.7 |
| Length Filter | 54.2 | 33.0 | 56.0 | 73.6 |

消融实验揭示了反直觉发现：过度过滤（如长度过滤、难度过滤）反而降低性能，因为过滤减少了答案多样性，损害了模型的鲁棒性。$\rightarrow 8$ 采样相比 $\rightarrow 1$ 采样在MathVision上提升 5.3 个点，验证了答案多样性的核心价值。此外，GSPO + $\rightarrow 16$ rollout 配置在MMMU上达到 57.8，优于GRPO的 54.6，证实了算法稳定性对最终性能的直接影响。

评估边界方面，本文未报告置信区间，数值比较需谨慎。可复现性上，本文开源了代码、管道与数据，但RL训练依赖verl与vllm框架，超参数（如温度1.0、rollout 16）的敏感性未充分探讨。

## 关联研究分析

从数据策展角度看，本文与OVR的主要差异在于对“答案多样性”的显式量化。OVR依赖大规模SFT数据（2M样本），而本文通过 $\rightarrow 8$ 采样在较小数据量（874k）下实现了更优的性能，根源在于本文将数据质量定义为“验证通过的答案轨迹数量”，而非单纯的问题覆盖度。这种设计假设了推理路径的多样性比问题数量的多样性更能促进泛化，但其在数据极度稀缺场景下的边际收益是否递减，论文未给出回答。

从RL算法选择看，本文采用GSPO而非领域常用的GRPO，这与DeepSeek-R1等文本推理模型的选择一致，但多模态任务的长序列特性可能放大GSPO的优势。与M2-Reasoning相比，本文未引入显式的模态去偏奖励，而是依赖跨域数据混合（图像/文本数学）来缓解模态偏见。这种“数据驱动”而非“奖励驱动”的去偏策略，在模态冲突严重的场景下是否足够鲁棒，仍是未解之谜。

## 总结

本文旨在解决多模态推理训练缺乏透明性与可复现性的核心矛盾，切入点在于将数据策展与RL算法选择解耦并系统消融，从而建立可复现的工程基准。通过874k SFT与74k RL数据，结合GSPO算法，本文在MathVista上实现 79.5 的准确率，较基线提升 10.3 个点，证明了答案多样性与算法稳定性对推理能力的关键作用。然而，本文在MathVision上的表现（43.6）低于OVR（51.8），暴露了其在特定视觉数学任务上的泛化局限。当面对视觉与文本信息严重冲突的场景时，仅依赖数据混合而非显式去偏奖励，能否维持推理链的逻辑忠实性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_f7b32077e39b)
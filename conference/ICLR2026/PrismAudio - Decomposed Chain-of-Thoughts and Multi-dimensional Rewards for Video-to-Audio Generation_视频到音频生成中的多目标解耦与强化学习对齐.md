# ICLR2026最新论文 ｜PrismAudio: Decomposed Chain-of-Thoughts and Multi-dimensional Rewards for Video-to-Audio Generation ｜视频到音频生成中的多目标解耦与强化学习对齐

研究机构：香港科技大学、阿里巴巴集团

作者：Huadai Liu、Kaicheng Luo、Wen Wang 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.18833)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.18833)

> 视频到音频（Video-to-Audio, V2A）生成旨在从无声视频中合成语义、时序、美学与空间四维对齐的声景，但现有方法受困于单一损失函数导致的目标纠缠，难以同时优化相互冲突的感知维度。本文切入点在于将单体思维链（Chain-of-Thought, CoT）规划分解为四个专用模块，并首次引入多维强化学习（Reinforcement Learning, RL）进行偏好对齐。通过设计Fast-GRPO算法降低训练开销，该框架在VGGSound与AudioCanvas基准上实现了全维度性能提升。其价值在于证明了分解式推理与针对性奖励能打破多目标权衡僵局，但CoT推理带来的额外延迟与自建基准的泛化性仍存疑。

## 研究背景

V2A生成的核心难点在于声学信号的高维连续性与多模态语义对齐之间的张力。流匹配（Flow Matching）技术通过直线化采样轨迹解决了传统扩散模型的多步采样瓶颈，成为当前V2A任务的主流生成范式。然而，流匹配模型通常依赖单一的重建损失函数，该函数将语义一致性、时间同步、美学质量与空间准确性等相互冲突的目标混合优化，导致模型在复杂场景下陷入次优权衡：优化语义往往牺牲时序精度，提升美学则可能破坏空间定位。

早期V2A方法如Diff-Foley（Luo et al., 2023）依赖视觉特征投影，缺乏细粒度控制；后续工作如ThinkSound（Liu et al., 2025b）引入CoT推理，通过多模态大语言模型（MLLM）生成结构化描述以提升可解释性，但其单体规划机制将不同维度的分析任务混杂在单一推理路径中，无法针对特定感知维度进行独立优化。本文抓住这一被忽略的“目标纠缠”问题，指出单体CoT无法处理竞争目标间的上下文依赖权衡，且缺乏人类偏好对齐机制。为此，本文提出将CoT分解为语义、时序、美学、空间四个专用模块，并配套多维奖励函数，通过RL优化实现各维度的协同提升。

## 核心方法

### 方法参照系

本文基于ThinkSound的CoT-V2A架构，其标准流程为：视频特征提取→MLLM生成单体CoT描述→扩散模型条件生成。本文的关键差异在于将单体CoT替换为四维分解CoT，并在生成阶段引入基于流匹配的RL后训练，以解决单体规划中目标混杂与偏好缺失的问题。

### 四维分解CoT与多维奖励设计

单体CoT的失效源于不同感知维度需要根本不同的分析框架：语义关注内容识别，空间需要方向定位逻辑，美学依赖主观质量评估。本文首先利用Gemini 2.5 Pro构建高质量CoT训练数据，随后微调VideoLLaMA2生成四个专用CoT模块：语义CoT识别音频事件，时序CoT确定事件顺序，美学CoT评估音质自然度，空间CoT分析声像定位。这四个模块拼接形成多维CoT，作为增强文本条件输入音频基础模型。

为对齐CoT维度，本文设计四个针对性奖励函数：语义奖励采用MS-CLAP评估内容相似度；时序奖励使用Synchformer检测视听同步；美学奖励利用Meta Audiobox Aesthetics预测人类平均意见分（MOS）；空间奖励通过StereoCRW验证方向定位准确性。这种CoT-奖励对应关系使得RL优化能针对每个维度提供独立梯度信号，避免单一损失函数的目标混淆。

### Fast-GRPO混合采样策略

将RL应用于扩散模型面临计算瓶颈：现有Flow-GRPO（Liu et al., 2025c）需在每个去噪步执行随机微分方程（SDE）采样以计算策略比率，导致训练开销巨大。本文提出Fast-GRPO，采用混合常微分方程（ODE）-SDE策略：仅在随机选择的子集步骤执行SDE采样以进行随机探索，其余步骤使用确定性ODE采样。

该策略的核心公式为混合采样器在随机窗口 $\ell$ 处的更新：

$$ \mathcal{J}_{\text{Fast-GRPO}}(\theta) = \mathbb{E}_{\ell} \left[ \sum_{t \in \text{SDE steps}} \log \pi_\theta(a_t|s_t) + \sum_{t \in \text{ODE steps}} \log \pi_\theta(a_t|s_t) \right] $$

其中，SDE步骤提供随机性以探索不同音频候选，ODE步骤保持确定性以降低计算成本。这一设计将训练时间从约8天缩短至5天，实现1.6倍加速，使得多维CoT-RL优化在计算上可行，同时保持生成质量不妥协。

## 实验评估

实验在VGGSound测试集（域内）与自建AudioCanvas基准（域外）上进行，基线覆盖MMAudio、ThinkSound、HunyuanVideo-Foley等主流V2A方法，但缺失自回归类基线。

| 方法 | CLAP↑ | DeSync↓ | PQ↑ | CRW↓ | FD↓ | MOS-Q↑ |
|---|---|---|---|---|---|---|
| ThinkSound | 0.43 | 0.55 | 3.54 | 13.47 | 1.80 | 3.65±0.72 |
| PrismAudio (Ours) | 0.47 | 0.41 | 6.38 | 7.72 | 1.08 | 4.21±0.35 |
| PrismAudio w/o CoT-RL | 0.42 | 0.51 | 6.17 | 10.29 | 1.14 | 4.02±0.48 |

PrismAudio在VGGSound上全面超越ThinkSound，CLAP提升0.04，DeSync降低0.14，CRW从13.47降至7.72。消融实验显示，移除CoT-RL后性能显著下降，证明RL优化是性能提升的关键驱动力。

| 奖励配置 | CLAP↑ | DeSync↓ | PQ↑ | CRW↓ | FD↓ |
|---|---|---|---|---|---|
| Semantic & Temporal | 0.48 | 0.41 | 6.30 | 8.38 | 1.22 |
| Semantic & Temporal & Spatial | 0.47 | 0.42 | 6.19 | 7.53 | 1.03 |
| Multi-dimensional | 0.47 | 0.41 | 6.38 | 7.72 | 1.08 |

消融结果表明，仅优化语义与时序会导致空间精度无改善（CRW 8.38 vs 8.29）且美学质量边际增益有限；添加空间奖励虽提升CRW至7.53，但美学质量反而下降（PQ 6.19 vs 6.30）。只有四维联合优化才能实现全维度同步提升，验证了多维奖励系统对解耦竞争目标的必要性。

评估协议采用CLAP、DeSync、Audiobox-Aesthetics及TDOA分析，覆盖语义、时序、美学与空间维度。局限在于：AudioCanvas为自建基准，其3,177个样本的泛化性未通过外部验证；CoT推理阶段需额外LLM调用，增加延迟；论文未报告实时因子（RTF）或FLOPs，计算效率维度缺失。

## 关联研究分析

从问题动机看，PrismAudio与ThinkSound同属CoT-V2A路线，但ThinkSound的单体规划将语义、时序、空间、美学分析混杂在单一推理路径中，导致复杂场景下多模态幻觉与目标纠缠。PrismAudio通过分解CoT与多维奖励，将不同维度的优化解耦，根源在于任务特性决定：不同感知维度需要不同的分析框架，单体推理无法同时满足所有维度的上下文依赖权衡。

从方法设计看，PrismAudio与Flow-GRPO同属流匹配RL框架，但Flow-GRPO聚焦单目标优化，需在每个去噪步执行SDE采样，计算开销大。PrismAudio的Fast-GRPO采用混合ODE-SDE策略，仅在随机窗口执行SDE采样，根源在于论文未探索的盲区：多维奖励优化需要更多采样步骤以覆盖不同维度的偏好，而全SDE采样在计算上不可行，混合策略通过降低随机性频率来平衡探索与计算成本。

## 总结

本文要解决的核心矛盾是V2A生成中多感知维度的目标纠缠与人类偏好对齐缺失。现有方法受困于单一损失函数，无法同时优化相互冲突的语义、时序、美学与空间目标。本文抓住的切入点是分解式CoT规划与多维RL优化，通过四个专用CoT模块与对应奖励函数，实现各维度的独立优化与协同提升。实验证明，PrismAudio在VGGSound上CLAP达0.47、DeSync达0.41，全面超越ThinkSound。本文的边界在于CoT推理带来的额外延迟与自建基准的泛化性未验证。当支持集增大到长视频场景时，四维CoT的推理延迟是否成为实时交互的瓶颈，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.18833)
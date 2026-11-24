# ACL-Findings2026最新论文 ｜WavAlign: Enhancing Intelligence and Expressiveness in Spoken Dialogue Models via Adaptive Hybrid Post-Training ｜WavAlign：面向语音对话模型的自适应混合后训练

研究机构：浙江大学、阿里巴巴集团

作者：Yifu Chen、Shengpeng Ji、Qian Chen 等 12 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.14932)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.14932)

> 端到端语音对话模型旨在统一语义理解与语音生成，但现有开源系统在智能（IQ）与表达力（EQ）上均存在显著短板。直接应用偏好优化（Preference Optimization）会导致声学漂移，因为文本梯度主导更新而语音梯度噪声大。本文提出单阶段自适应混合后训练框架，将偏好优化限制在文本Token，并用监督微调（SFT）锚定语音分布。该方法在多个基准上实现了IQ与EQ的同步提升，但其对弱基座模型的鲁棒性仍存疑。

## 研究背景

当模型同时生成文本与语音时，优化目标面临跨模态耦合失效的困境。这种失效源于梯度能量失衡：文本Token的语义信号清晰且梯度稳定，而语音Token的声学特征稀疏且高方差，导致统一的序列级偏好优化无法同时改善两者。解决此问题的关键在于解耦优化角色，即利用SFT维持声学分布的可行性，利用强化学习（RL）精调语义行为。

语音大语言模型（Speech LLMs）的主流范式已从级联架构转向端到端架构，以保留副语言信息并降低延迟。然而，模态对齐并未消除推理退化，语音输入下的逻辑追踪能力仍显著低于文本。现有后训练方法通常采用两阶段流程（SFT→RL），或针对单一维度（仅IQ或仅EQ）进行优化，缺乏在单循环内同时稳定声学分布与提升语义质量的统一方案。本文切入点在于识别混合模态序列中偏好信号的跨模态耦合失效机制，并据此设计模态感知的动态混合目标。

## 核心方法

### 方法参照系

标准后训练流程通常先执行SFT以对齐分布，再执行RL以优化偏好。本文问题的关键差异在于：语音Token的高密度与低信噪比使得标准RL的信用分配（Credit Assignment）失效，导致声学质量退化。因此，需重构优化目标，实现模态间的职责分离。

### 模态解耦的混合优化目标

传统GRPO（Group Relative Policy Optimization）对全序列施加统一的偏好梯度，导致文本更新干扰声学分布。本文创新在于将偏好梯度限制在文本Token子集 $I_T$，同时保留全序列的SFT损失作为锚点。其目标函数定义为：

$$
\mathcal{L} = \mathcal{L}_{SFT} + \lambda_t \mathcal{L}_{GRPO}^{I_T}
$$

其中 $\mathcal{L}_{SFT}$ 提供密集的Token级约束以稳定声学分布，$\mathcal{L}_{GRPO}^{I_T}$ 仅对文本Token计算偏好优势。这一设计解决了全Token偏好优化中声学信号被噪声淹没的问题，确保语义精调不破坏韵律自然度。

### 基于Rollout可靠性的动态门控

固定混合权重无法适应训练过程中Rollout质量的变化。本文引入动态门控机制 $\lambda_t$，根据奖励方差 $v_t$ 和方向门 $g_t$ 调整SFT与RL的比例。具体公式为：

$$
\lambda_t = \lambda_{max} \cdot g_t(v_t) \cdot \mathbb{1}[R_{max,t} \ge 3]
$$

其中 $v_t$ 为归一化奖励方差，$g_t$ 为信息门。该机制仅在Rollout具有足够区分度且存在可接受样本时启用偏好更新，否则回退至SFT主导，从而避免低质量样本导致的分布漂移。

## 实验评估

实验在VITA-Audio（交错架构）和KimiAudio（并行架构）两个基座上验证，基准涵盖VoiceBench（IQ）、OpenAudioBench（IQ）和VStyle（EQ）。基线覆盖SFT、全Token/文本Token的DPO与RL，以及两阶段SFT+RL。

| 方法 | VITA IQ (Avg) | VITA EQ (Avg) | KimiAudio IQ (Avg) | KimiAudio EQ (Avg) |
|---|---|---|---|---|
| Base | 55.0 | 2.55 | 69.1 | 2.56 |
| SFT | 50.7 | 2.59 | 64.9 | 2.71 |
| Full-Token DPO | 35.1 | 1.22 | 61.8 | 1.70 |
| Text-Token DPO | 54.4 | 2.56 | 69.2 | 2.65 |
| Full-Token RL | 55.4 | 2.43 | 69.2 | 2.65 |
| **Ours (Dynamic)** | **57.6** | **2.91** | **70.8** | **2.90** |

在VITA架构上，本文方法在IQ上较Base提升2.6分，在EQ上提升0.36分；在KimiAudio上，IQ提升1.7分，EQ提升0.34分。全Token DPO在EQ上出现严重退化（VITA从2.55降至1.22），验证了声学奖励噪声对偏好优化的破坏性。

消融实验显示，将优化范围从全Token限制为文本Token，IQ从48.70提升至52.60，EQ从2.48提升至2.60。动态权重策略较固定权重（0.5/0.5）进一步将IQ提升至55.24，EQ提升至2.92。移除EMA平滑后，IQ降至53.15，表明平滑对稳定训练至关重要。

评估协议依赖GPT-4o-mini和Gemini-2.5-Pro作为自动裁判，缺乏人工评估的置信区间。代码已开源，但训练数据仅13.5k样本，规模较小。未对比强级联基线（如Whisper+LLM），限制了绝对性能的参照系。

## 关联研究分析

从问题动机看，本文与SALAD（Cuervo et al., 2025）均关注灾难性遗忘，但SALAD通过两阶段蒸馏解决模态不等价，而本文通过动态混合解决优化动力学失衡。SALAD依赖教师模型的质量，本文则依赖Rollout的可靠性，后者在弱基座模型上可能因高质量样本稀缺而失效。

从方法设计看，本文与X-OPD（Cao et al., 2026）均使用在线策略优化，但X-OPD通过跨模态蒸馏转移知识，本文通过模态解耦限制梯度范围。X-OPD在VoiceBench上达到82.4%准确率，本文在相同基准上仅57.6%，差异源于X-OPD使用了更强的文本教师模型，而本文仅使用13.5k小样本数据。这暗示本文方法的性能上限可能受限于数据规模而非优化算法本身。

## 总结

本文核心矛盾在于端到端语音对话模型中IQ与EQ的联合优化失效。现有方法因全Token偏好优化导致声学漂移，本文通过模态解耦与动态门控实现职责分离。实验证明该方法在VITA和KimiAudio上同步提升IQ与EQ，其中VITA EQ提升0.36分。其边界在于依赖Rollout质量，弱基座模型下高质量样本稀缺可能导致门控失效。当基座模型能力进一步减弱时，动态门控是否仍能维持声学稳定性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.14932)
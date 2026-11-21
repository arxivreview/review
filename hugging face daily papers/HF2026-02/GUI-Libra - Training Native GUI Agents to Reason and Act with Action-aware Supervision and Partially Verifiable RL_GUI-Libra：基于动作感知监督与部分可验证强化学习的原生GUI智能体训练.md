# HuggingFace最新推荐论文 ｜GUI-Libra: Training Native GUI Agents to Reason and Act with Action-aware Supervision and Partially Verifiable RL ｜GUI-Libra：基于动作感知监督与部分可验证强化学习的原生GUI智能体训练

研究机构：美国伊利诺伊大学厄巴纳-香槟分校

作者：Rui Yang、Qianhui Wu、Zhaoyang Wang 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.22190)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.22190)

> 原生GUI智能体在长程导航任务中面临推理与定位的内在冲突，以及离线训练指标与在线任务成功率脱节的困境。现有开源方案要么依赖短推理牺牲规划能力，要么采用激进强化学习导致训练不稳定。GUI-Libra通过动作感知监督微调（ASFT）与保守强化学习（Conservative RL）的组合，在仅使用开源数据的情况下实现了性能突破。该框架证明了数据清洗与训练策略设计比单纯扩大模型规模更有效，但其对部分可验证性问题的处理仍受限于单一动作验证机制。

## 研究背景

GUI智能体需将自然语言指令映射为可执行动作，这一过程涉及视觉定位（Grounding）与高层规划的双重挑战。定位要求模型精确预测UI元素坐标，而规划需理解多步任务逻辑。当模型生成冗长的思维链（Chain-of-Thought, CoT）时，推理Token往往主导训练损失，导致定位精度下降；反之，若抑制推理以保定位，则长程任务中的错误恢复能力受损。这种推理-定位的权衡是原生GUI智能体后训练的核心矛盾。

当前开源生态存在两大瓶颈：一是高质量动作对齐推理数据稀缺，现有数据集多含噪声或短推理轨迹；二是通用后训练范式未适配GUI特性。监督微调（SFT）常因长CoT损害定位，而基于可验证奖励的强化学习（RLVR）在GUI场景中面临“部分可验证性”问题——同一状态下多个动作均可能正确，但离线监督仅验证单一演示动作，导致有效动作被误判为失败，引入偏差梯度并削弱离线-在线指标的一致性。GUI-Libra针对此矛盾，提出在SFT阶段显式加权动作Token，在RL阶段引入保守约束以稳定训练。

## 核心方法

### 方法参照系

标准GUI智能体后训练流程包含SFT初始化与RL优化两阶段。SFT阶段通常对推理与动作Token均匀计算交叉熵损失，RL阶段采用组相对策略优化（GRPO）并常去除KL正则化以加速收敛。本文的关键差异在于：SFT阶段引入动作感知加权以解决推理干扰，RL阶段保留中等KL正则化并引入成功自适应负梯度缩放以应对部分可验证性。

### 动作感知监督微调

ASFT在SFT阶段混合推理-动作与直接动作监督，并对动作与定位Token进行重加权。设计动机在于解决长CoT导致定位精度下降的问题，通过提升执行相关Token的损失权重，确保模型优先学习直接决定执行的动作信息。其目标函数为：

$$
\mathcal{L}_{\text{ASFT}} = -\sum_{t} \left[ \alpha_a \log \pi_\theta(a_t | x_t) + \alpha_g \log \pi_\theta(g_t | x_t) + \log \pi_\theta(c_t | x_t) \right]
$$

其中 $\alpha_a$ 和 $\alpha_g$ 分别为动作与定位Token的权重系数（默认设为2和4），$c_t$ 为推理Token。该公式通过放大动作与定位Token的梯度贡献，抑制推理Token对定位能力的干扰，使模型在生成长推理的同时保持定位精度。

### 保守强化学习

在RL阶段，GUI-Libra采用带KL正则化的GRPO，并引入成功自适应负梯度缩放（SNGS）。设计动机在于解决部分可验证性导致的奖励模糊问题：当多个动作均正确但仅验证单一动作时，未验证的有效动作被误判为负样本，产生偏差梯度。保守RL通过KL项约束策略漂移，SNGS则动态降低不可靠负样本的梯度权重。其优化目标为：

$$
\mathcal{L}_{\text{RL}} = \mathbb{E}_{x \sim \mathcal{D}} \left[ \frac{1}{G} \sum_{k=1}^{G} \rho_k \hat{A}_k - \beta \text{KL}(\pi_\theta \| \pi_{\text{ref}}) \right]
$$

其中 $\rho_k$ 为重要性采样比，$\hat{A}_k$ 为组归一化优势，$\beta$ 为KL系数（7B模型设为0.005，其他为0.001）。SNGS进一步对负优势样本进行缩放，降低因部分可验证性导致的负梯度偏差，提升离线指标对在线任务成功率的预测能力。

## 实验评估

实验在AndroidWorld、MM-Mind2Web-v2、AndroidControl-v2等基准上进行，基线覆盖UI-TARS、GLM-4.1V、Qwen系列等开源模型，但缺乏MobileRL等纯在线RL方法的直接对比。

| 模型 | AndroidControl-v2 High Pass@1 | MM-Mind2Web-v2 Avg Pass@1 | AndroidWorld 提升幅度 |
| :--- | :--- | :--- | :--- |
| Qwen2.5-VL-3B (Baseline) | 36.4 | 23.4 | — |
| GUI-Libra-3B | 57.3 (+20.9) | 42.7 (+19.3) | — |
| Qwen2.5-VL-7B (Baseline) | 46.5 | 32.5 | — |
| GUI-Libra-7B | 59.3 (+12.8) | 46.5 (+14.0) | — |
| Qwen3-VL-4B (Baseline) | 49.3 | 41.2 | — |
| GUI-Libra-4B | 62.3 (+13.0) | 50.0 (+8.8) | +15.6% |
| Qwen3-VL-8B (Baseline) | 54.8 | 43.8 | — |
| GUI-Libra-8B | 64.3 (+9.5) | 50.5 (+6.7) | +12.2% |

GUI-Libra-4B在AndroidWorld上较基线提升15.6%，GUI-Libra-8B提升12.2%，表明小模型经精细后训练可接近大模型性能。消融实验显示，ASFT单独使用仍保留推理-定位差距（7B模型差距3.4点），但RL阶段后该差距基本消除，GUI-Libra-7B在推理模式下定位精度（89.3%）甚至超过无推理模式（88.5%）。数据过滤对Pass@4指标提升显著，表明高质量数据对多路径探索能力至关重要。

评估边界方面，论文未报告置信区间，且缺乏与纯在线RL方法的直接对比，难以完全排除在线交互带来的性能增益归因。代码与81K数据集已开源，但RL超参数（如KL系数）对性能敏感，复现时需仔细调参。

## 关联研究分析

从问题动机看，GUI-Libra与UI-TARS、GLM-4.1V等SFT+RL混合范式同属原生模型驱动路线，但后者侧重短推理或通用RLVR，未显式处理推理-定位冲突。GUI-Libra通过ASFT加权动作Token，直接针对长CoT损害定位的具体失效，而UI-TARS等方法的定位退化可能源于未区分Token重要性。从方法设计看，GUI-Libra与MobileRL代表不同RL路线：MobileRL采用纯在线RL，依赖环境交互获取真实奖励；GUI-Libra采用保守离线RL，通过KL正则化与SNGS处理部分可验证性。两者在性能-效率权衡上存在差异，但论文未提供直接对比，无法判断保守RL在极端分布外场景是否因探索受限而性能受限。

## 总结

GUI-Libra针对原生GUI智能体后训练中推理-定位冲突与离线-在线指标脱节的核心矛盾，通过ASFT加权动作Token与保守RL处理部分可验证性，在仅使用开源数据的情况下实现了显著性能提升。实验表明，GUI-Libra-4B在AndroidWorld上较基线提升15.6%，且RL阶段后推理模式定位精度超过无推理模式，验证了保守RL对推理-定位对齐的有效性。然而，论文未提供与纯在线RL方法的直接对比，且部分可验证性问题的解决仍依赖单一动作验证机制，未探索多动作正确性验证的可能性。当训练数据中包含多个有效动作时，SNGS的负梯度缩放是否足以完全消除奖励模糊，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.22190)
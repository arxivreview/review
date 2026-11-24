# ICLR2026最新论文 ｜VidGuard-R1: AI-Generated Video Detection and Explanation via Reasoning MLLMs and RL ｜VidGuard-R1：基于强化学习推理的多模态大模型视频真实性检测

研究机构：美国德克萨斯大学奥斯汀分校、微软研究院

作者：Kyoungjun Park、Yifan Yang、Juheon Yi 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.02282)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.02282)

> 导读 AI生成视频检测旨在区分真实视频与合成视频，并解释判定依据。传统检测器依赖空间-时间一致性或频率伪影，难以捕捉高层语义与因果逻辑错误，且缺乏可解释性。VidGuard-R1将多模态大语言模型（MLLM）与群体相对策略优化（GRPO）结合，通过设计针对时序伪影和扩散步数的专用奖励函数，引导模型进行物理感知的推理。该方法在GenVideo基准上取得96%的F1分数，但其在未见生成模型上的泛化鲁棒性及推理成本仍是关键存疑点。

## 研究背景

当检测器面对新生成模型时，其训练域与测试域的数据分布出现系统性差异——这一现象称为分布偏移。分布偏移导致传统分类器决策边界失效，而实际场景中往往能获取少量目标域样本，这恰好构成了小样本学习的条件：仅凭每个类别极少量标注样本泛化到新任务。解决此类问题的经典框架是原型网络，它计算各类别支持样本的特征均值作为"原型"，再通过距离度量完成分类。

AI生成视频检测的核心矛盾在于，现有方法多聚焦于DeepFake式的面部伪造或低层时空一致性，无法应对Sora等模型生成的开放域、多场景视频。主流路线如AIGDet和DeCoF依赖空间-时间异常或帧一致性，易被后处理技术绕过，且仅提供二元决策，缺乏透明性。VidGuard-R1的切入点在于利用MLLM的推理能力，通过强化学习（RL）增强其对细微时序伪影和物理违规的捕捉能力，实现高精度检测与可解释归因的统一。

## 核心方法

### 方法参照系

本文问题属于基于MLLM的视频真实性检测。标准流程通常采用监督微调（SFT）或直接偏好优化（DPO）来对齐模型输出与人类偏好。本文的关键差异在于引入GRPO，通过群体内相对奖励排名，使模型在探索多条推理路径中自我改进，而非依赖静态偏好对。

### GRPO基础框架

设计动机：SFT和DPO依赖预标注数据或静态偏好对，难以捕捉动态生成模型中细微的时序不一致。GRPO通过群体相对奖励，鼓励模型在多个推理路径中探索并排名，从而发现更深层的物理感知伪影。

GRPO的目标函数为：

$$ L_{GRPO}(\theta) = - \mathbb{E}_{(x, o_{1:G}) \sim D} \left[ \frac{1}{G} \sum_{i=1}^{G} \min \left( \frac{p_\theta(o_i|x)}{p_{ref}(o_i|x)} A_i, \text{clip}\left(\frac{p_\theta(o_i|x)}{p_{ref}(o_i|x)}, 1-\epsilon, 1+\epsilon\right) A_i \right) - \beta D_{KL}(p_\theta \| p_{ref}) \right] $$

其中 $A_i = \frac{r_i - \mu_x}{\sigma_x}$ 是归一化奖励，$\mu_x$ 和 $\sigma_x$ 是群体内奖励的均值和标准差。该公式通过相对排名而非绝对奖励，使模型在群体内学习细微的质量差异，避免单一奖励信号的稀疏性。

### 时序伪影奖励（GRPO-TA）

设计动机：标准GRPO依赖局部视觉线索（如像素失真），但常忽略时序不一致，这是检测生成视频的关键。GRPO-TA通过对比奖励调整，显式促进时序推理。

对原始视频 $o_i$ 和操纵视频 $\tilde{o}_i$（重复或反转片段），若模型正确分类操纵视频为假，则根据原始视频标签 $y_i$ 分配额外奖励 $w_i$：

$$ w_i = \begin{cases} \alpha_1 & \text{if } y_i = \text{real} \\ \alpha_2 & \text{if } y_i = \text{fake} \end{cases} $$

最终奖励 $r_i' = r_i + w_i \cdot \mathbb{I}(\text{pred}(o_i) = y_i) \cdot \mathbb{I}(\hat{p} > \mu)$，其中 $\hat{p}$ 是操纵视频组的准确率，$\mu=0.8$。该设计通过不对称奖励（$\alpha_1=0.5 > \alpha_2=0.3$）反映真实视频时序操纵更难检测的特性，迫使模型关注运动连贯性而非静态纹理。

### 扩散步数奖励（GRPO-Q）

设计动机：生成视频的质量随扩散步数增加而提升，更难检测。GRPO-Q通过奖励更难检测的视频，引导模型学习更细微的伪影。

对真实视频，使用不同扩散步数（10, 20, 30, 40, 50）生成对应视频，若模型正确分类高步数视频为假，则分配更高奖励。消融实验显示，使用5个步数时准确率最高（85.80%），表明更丰富的质量梯度监督有助于提升检测精度。

## 实验评估

实验在自建数据集（140k对）、GenVidBench和GenVideo上进行。基线覆盖CNN（SlowFast, I3D）、Transformer（TimeSformer, VideoSwin）和MLLM（Qwen2.5-VL, GPT-4o），但遗漏了专用检测器如DeMamba-XCLIP。

| 方法 | 类型 | GenVideo F1 | GenVidBench Mean Acc |
|---|---|---|---|
| VidGuard-R1 (GRPO) | MLLM | 0.96 | 97.53 |
| DeMamba-XCLIP | Video | 0.90 | — |
| GPT-4o | MLLM | 0.72 | — |
| Qwen2.5-VL-7B | MLLM | 0.70 | 47.30 |

VidGuard-R1在GenVideo上F1达0.96，显著超越DeMamba-XCLIP（0.90）和GPT-4o（0.72），表明RL增强的MLLM在跨模型泛化上优于传统检测器。

消融实验显示，GRPO-TA在 $\alpha_1=0.5, \alpha_2=0.3$ 时准确率最高（83.57%），而GRPO-Q使用5个扩散步数时准确率最高（85.80%）。跨数据集实验表明，混合训练（Ours + GenVideo）在GenVideo上准确率从97.53%提升至97.98%，验证了模型学习的是可泛化检测线索而非数据集特定模式。

评估边界：指标完备性方面，论文报告F1和准确率，但未提供置信区间；评估协议局限在于GenVideo和GenVidBench的生成模型覆盖有限，未包含最新模型如Sora 2；可复现性方面，论文提供项目网站，但未公开完整超参数和GPU配置。

## 关联研究分析

从问题动机看，VidGuard-R1与SafeWatch（Chen et al., 2024b）同属MLLM-based检测，但SafeWatch采用DPO，依赖静态偏好对，难以捕捉动态时序不一致。VidGuard-R1通过GRPO的群体相对奖励，使模型在探索中动态调整推理路径，解决了DPO在时序推理上的局限。这一差异源于任务特性：视频检测需关注帧间动态变化，静态偏好对无法提供足够的时序监督信号。

从方法设计看，VidGuard-R1与Video-R1（Feng et al., 2025）同用RL增强MLLM推理，但Video-R1聚焦视频问答，而VidGuard-R1针对检测任务设计了专用奖励函数（GRPO-TA和GRPO-Q）。这一差异源于问题特性：检测任务需区分细微伪影，通用推理奖励不足以引导模型关注时序和扩散步数等特定线索。查询侧增强在数据充足时是否仍有增益，论文未给出回答。

## 总结

VidGuard-R1解决的核心矛盾是AI生成视频检测中高精度与可解释性的统一。现有方法依赖低层特征或静态偏好，无法捕捉高层语义与因果逻辑错误，而VidGuard-R1通过GRPO和专用奖励函数，引导MLLM进行物理感知推理。该方法在GenVideo上取得96% F1，在GenVidBench上取得97.53%准确率，证明了RL在细粒度视觉推理中的有效性。其边界在于，实验未覆盖最新生成模型，且推理成本较高，制约实时应用。当支持集增大到5-shot时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.02282)
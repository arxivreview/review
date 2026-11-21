# HuggingFace最新推荐论文 ｜Think, then Score: Decoupled Reasoning and Scoring for Video Reward Modeling ｜解耦推理与评分的视频奖励模型

研究机构：中国科学技术大学、快手

论文原文见 [arXiv](https://arxiv.org/abs/2605.05922)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.05922)

> 视频生成模型的后训练与测试时扩展高度依赖奖励模型（Reward Model, RM）对生成视频质量的精准评估，但现有范式在泛化能力与训练稳定性间存在根本矛盾。判别式RM缺乏显式推理导致捷径学习，生成式RM将思维链（Chain-of-Thought, CoT）与评分耦合于单一自回归链中引发优化瓶颈。本文提出DeScore，通过“先思考后评分”的解耦架构，将CoT推理与标量奖励预测分离，并采用两阶段训练框架。该设计在保持可解释性的同时显著提升了分布外泛化与训练效率，但其对极端分布偏移场景的鲁棒性仍存疑。

## 研究背景

视频奖励模型的核心任务是为文本到视频（Text-to-Video, T2V）生成过程提供与人类偏好对齐的标量信号，该信号直接决定后训练（Post-training）与测试时扩展（Test-time Scaling）的性能上限。理想RM需在多样化场景与复杂运动模式下保持准确的偏好对齐，这要求模型具备强大的分布外（Out-of-Distribution, OOD）泛化能力。然而，当前主流范式面临两难困境：判别式方法从多模态大语言模型（Multimodal Large Language Model, MLLM）特征直接回归标量奖励，虽优化信号稳定，但缺乏显式推理导致模型依赖捷径特征拟合标签，需海量数据扩展以弥补泛化缺陷；生成式方法将奖励建模为下一词元预测任务，引入CoT提供细粒度语义监督，但推理与评分耦合在单一采样链中，导致无法直接优化奖励值、信用分配困难及策略梯度高方差。

该矛盾源于生成式RM将离散词元概率优化与连续标量奖励优化强行绑定。当CoT序列较长时，Group Relative Policy Optimization (GRPO) 的梯度方差随序列长度增长，训练稳定性显著下降。现有工作如UnifiedReward-Thinking虽通过两阶段训练（监督微调后强化学习）引入CoT，但评分仍依赖自回归链的最终词元，无法隔离推理质量波动对奖励校准的干扰。DeScore的切入点在于结构化解耦：将CoT生成与奖励预测分离为两个独立模块，使推理过程提供语义上下文，而评分模块通过回归头直接输出标量，从而在保留CoT泛化优势的同时，规避耦合采样链的优化不稳定性。

## 核心方法

### 解耦架构参照系

视频奖励模型的标准流程通常将MLLM特征映射至标量奖励，判别式方法使用Bradley-Terry (BT) 损失或均方误差直接优化，生成式方法则通过自回归预测分数词元。DeScore的关键差异在于引入“思考-评分”解耦机制：MLLM骨干生成CoT序列后，附加可学习查询词元（Query Token）聚合多模态输入与推理信息，再由回归头投影为标量奖励，而非依赖自回归链的最终输出。

### 随机掩码判别式冷启动

设计动机在于防止评分模块过度依赖CoT文本而忽视原始视频特征，导致在CoT质量波动时奖励预测失效。在判别式冷启动阶段，输入序列构造为 $X = (\mathbf{v}, \mathbf{c}, \mathbf{o}, [\text{Reward}])$，其中 $\mathbf{v}$ 为视频，$\mathbf{c}$ 为文本提示，$\mathbf{o}$ 为预收集CoT。训练时以概率 $p$ 随机掩码CoT（即 $\mathbf{o} = \emptyset$），强制模型在缺乏推理文本时仍能从原始多模态输入中提取语义证据。该机制确保奖励预测是视觉证据与逻辑推理的 holistic 反映，而非单一来源的依赖。

### 双目标强化学习优化

设计动机在于解决CoT质量提升与奖励校准的耦合冲突：仅优化CoT可能导致评分模块“奖励漂移”，失去对偏好标签的校准。在强化学习阶段，采用双目标优化：GRPO损失优化CoT推理质量，辅助BT损失持续校准标量奖励。GRPO优势值计算为 $A_i = \frac{R(\mathbf{o}_i) - \text{mean}(R)}{\text{std}(R)}$，其中 $R(\mathbf{o}_i) = \lambda_1 R_{\text{fmt}} + \lambda_2 R_{\text{qual}} + \lambda_3 R_{\text{len}}$ 为复合奖励，分别约束格式、子维度分数准确性与长度合理性。辅助BT损失定义为 $\mathcal{L}_{\text{BT}} = -\log \sigma(s^{[w]} - s^{[l]})$，其中 $s^{[w]}$ 和 $s^{[l]}$ 为获胜与失败样本的标量奖励。该设计将奖励优化从GRPO的高方差策略更新中隔离，确保评分模块始终接收直接梯度信号。

## 实验评估

实验在自建In-domain数据集（22K训练对，1469评估对）及OOD基准GenAI-Bench、VideoGen-Bench上进行，基线覆盖判别式（VideoAlign, VideoScore）与生成式（UnifiedReward-Thinking, VisionReward）两类方法。DeScore在In-domain Acc w/o Tie达0.765，OOD VideoGen-Bench达0.768，显著优于最强判别式基线VideoAlign（0.722）与生成式基线UnifiedReward-Thinking（0.582）。

| 模型 | In-domain Acc w/o Tie | GenAI Acc w/o Tie | VideoGen-Bench Acc w/o Tie |
|---|---|---|---|
| VideoAlign | 0.722 | 0.538 | 0.722 |
| UnifiedReward-Thinking | 0.686 | 0.564 | 0.582 |
| DeScore | 0.765 | 0.765 | 0.768 |

消融实验显示，CoT引入使In-domain准确率从0.588提升至0.615，随机掩码进一步增至0.656；在OOD基准上，CoT带来5.1%（GenAI）与6.5%（VideoGen-Bench）的Acc w/o Tie提升。冷启动阶段对最终性能影响显著：移除冷启动使In-domain准确率从0.734降至0.691，验证了判别式预热对评分模块初始化的必要性。

评估边界受限于自建In-domain数据集的领域特异性，OOD基准仅覆盖早期T2V模型生成视频，未包含最新模型（如Sora、Veo）的分布偏移。代码未公开，超参数（如LoRA rank 64、GRPO group size 8）虽详细披露，但缺乏多GPU训练配置与随机种子敏感性分析，可复现性受限。

## 关联研究分析

从问题动机看，DeScore与UnifiedReward-Thinking同属生成式奖励模型路线，但后者将CoT与评分耦合于单一自回归链，导致评分依赖最终词元概率，无法隔离推理质量波动对奖励校准的干扰。DeScore通过解耦架构使评分模块直接接收BT损失梯度，规避了GRPO在长序列CoT中的高方差问题。这一差异源于任务特性：奖励模型需输出稳定标量信号，而生成式问答任务可容忍词元级波动，故耦合设计在问答任务中可行，但在奖励建模中导致优化瓶颈。

从方法设计看，DeScore与VideoAlign同用BT损失，但后者缺乏显式推理，依赖海量数据扩展弥补泛化缺陷；DeScore引入CoT提供细粒度语义监督，使模型学习“为何视频更优”而非仅拟合排序。随机掩码机制进一步强制评分模块利用原始视频特征，缓解CoT文本主导导致的视觉接地缺失。这一设计是否牺牲了CoT对最终奖励的直接因果贡献，论文未通过因果干预实验验证，仅通过消融显示掩码提升性能，但未量化CoT移除后奖励预测的语义漂移程度。

## 总结

DeScore解决的核心矛盾是生成式奖励模型中CoT推理与标量评分耦合导致的优化不稳定与泛化缺陷。其切入点在于结构化解耦：将CoT生成与奖励预测分离，使推理提供语义上下文，评分模块通过回归头直接输出标量，从而在保留CoT泛化优势的同时，规避耦合采样链的高方差梯度。实验证明该设计在In-domain Acc w/o Tie达0.765，OOD VideoGen-Bench达0.768，较最强基线提升4.6%。边界在于OOD基准仅覆盖早期T2V模型，未验证对最新生成模型分布偏移的鲁棒性；随机掩码机制虽提升性能，但未量化CoT移除后奖励预测的语义漂移程度。当测试视频来自未见过的新T2V模型时，解耦架构的评分模块是否仍能保持与CoT推理的逻辑一致性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.05922)
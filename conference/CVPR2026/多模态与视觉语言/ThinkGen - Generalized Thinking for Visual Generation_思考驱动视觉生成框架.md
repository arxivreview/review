# CVPR2026最新论文 ｜ThinkGen: Generalized Thinking for Visual Generation ｜思考驱动视觉生成框架

研究机构：北京交通大学

作者：Siyu Jiao、Yiheng Lin、Yujie Zhong 等 12 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.23568)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.23568)

> 统一多模态模型在生成任务中普遍面临“理解-生成”鸿沟，即模型能正确推断语义但无法忠实还原像素，且现有思维链（Chain-of-Thought, CoT）机制往往局限于单一场景，缺乏跨任务泛化能力。本文切入点在于将CoT从理解任务迁移至生成任务，并解决推理冗余信息与扩散模型（Diffusion Transformer, DiT）条件输入之间的表征失配问题。通过解耦的多模态大语言模型（MLLM）与DiT架构，结合分离式组相对策略优化（Separable Group Relative Policy Optimization, SepGRPO），实现通用化的思考驱动生成。该框架在推理密集型任务上表现突出，但在纯参数化知识覆盖上仍受限于基座模型能力。

## 研究背景

当视觉生成模型面对复杂指令时，直接映射文本到像素往往忽略逻辑约束或产生事实错误，这一现象源于共享表征空间未能区分抽象语义与像素细节。为缓解此问题，研究者引入CoT推理，让模型先生成中间步骤再执行生成。然而，早期工作如BAGEL将CoT机制绑定于特定任务（如推理生成），导致在文本渲染或图像编辑等其他场景中性能下降，且需人工干预激活推理模式。这种场景特异性限制了CoT在通用生成中的灵活性，核心原因在于现有框架缺乏将推理信号转化为像素级精确控制的通用机制。

该领域的主流路线分为两类：一类是统一架构（如Chameleon、Transfusion），通过共享骨干网络融合理解与生成，但面临任务干扰；另一类是解耦架构（如OmniGen2），将MLLM作为特征提取器，DiT负责合成，但MLLM的CoT能力未被充分利用。ThinkGen的切入点在于解耦架构中显式利用MLLM的CoT推理，并通过VGI-refine模块过滤冗余信息，使推理链成为DiT的有效条件输入。这一设计旨在解决“想得好但画得错”的执行脱节问题，将静态映射升级为动态认知对齐。

## 核心方法

### 解耦架构与VGI-refine模块

传统解耦架构中，MLLM输出直接作为DiT条件，但CoT过程中的冗余文本（如重复描述、无关推理）会干扰DiT的注意力机制，导致生成质量下降。ThinkGen引入VGI-refine模块，从MLLM的CoT输出中提取`</think>`后的指令token，并拼接可学习的Prepadding States。这一设计解决了CoT冗余信息对DiT的干扰，使短指令（如“生成一只狗”）也能获得稳定的表征分布。

$$
\mathbf{h}_{\text{refine}} = [\mathbf{h}_{\text{instruction}}; \mathbf{p}_1, \mathbf{p}_2, \dots, \mathbf{p}_K]
$$

其中 $\mathbf{h}_{\text{instruction}}$ 为提取的指令隐藏状态，$\mathbf{p}_k$ 为可学习Prepadding States。该公式通过拼接可学习向量调节MLLM输出分布，使其与DiT的条件输入需求对齐。

### SepGRPO分离式强化学习

统一模型中，MLLM与DiT的联合训练面临信用分配难题：无法区分推理质量与生成质量对最终结果的贡献。SepGRPO将强化学习（RL）过程解耦为两个阶段：Stage 4冻结DiT，仅优化MLLM，使其生成符合DiT偏好的指令；Stage 5冻结MLLM，仅优化DiT，使其基于高质量指令生成更优图像。这种分离设计降低了训练复杂度，允许为每个模块设计独立的奖励函数。

$$
\mathcal{L}_{\text{GRPO}} = \mathbb{E}_{x \sim \mathcal{D}, o \sim \pi_{\theta_{\text{old}}}} \left[ \min \left( r_{i,j}(\theta) \hat{A}_i, \text{clip}(r_{i,j}(\theta), 1-\epsilon, 1+\epsilon) \hat{A}_i \right) \right]
$$

其中 $r_{i,j}(\theta)$ 为策略概率比，$\hat{A}_i$ 为组相对优势。该公式通过裁剪代理目标稳定训练，避免策略更新过大导致的性能退化。

## 实验评估

| 基准 | 指标 | ThinkGen (w/o think) | ThinkGen (w/ think) | BAGEL | GPT-4o |
|---|---|---|---|---|---|
| WISE | Overall | 0.55 | 0.76 | 0.70 | 0.80 |
| RISEBench | Avg. | 3.6 | 13.0 | 5.8 | 28.9 |
| GenEval | Overall | 0.84 | 0.89 | 0.70 | - |
| CVTG | Acc. | 0.80 | 0.84 | 0.77 | - |

ThinkGen在启用CoT后，WISE基准准确率从0.55提升至0.76，RISEBench平均分从3.6跃升至13.0，显著超越BAGEL（0.70/5.8）和开源基线，但低于GPT-4o（0.80/28.9）。GenEval上0.89的准确率超越BAGEL的0.70，表明CoT在组合性生成中的有效性。

消融实验显示，Stage 4 MLLM-GRPO对WISE提升最大（0.55→0.76），而Stage 5 DiT-GRPO主要改善CVTG（0.79→0.84）。Prepadding States对短指令基准（GenEval、WISE）提升显著（0.64→0.78，0.37→0.46），但对长指令基准（DPG）影响微小（80.90→80.86），表明其作用限于表征分布调节而非语义增强。

评估边界方面，论文未报告置信区间，数值比较需谨慎。代码与模型权重已开源，但训练数据（54M图像-文本对）未完全公开，可复现性受限。规则模型（如GenEval、HPSv3）作为奖励函数，其设计可能引入偏差，论文未提供替代奖励的对比实验。

## 关联研究分析

从问题动机看，ThinkGen与UniGRPO均针对“理解-生成”鸿沟，但UniGRPO采用统一架构下的联合RL，而ThinkGen通过解耦架构分离优化。这一差异源于任务特性：解耦架构允许独立奖励设计，但可能牺牲模块间协同优化效率。ThinkGen在WISE上0.76的准确率低于AlphaGRPO的0.79.5，是否因缺乏联合优化中的跨模块反馈，论文未给出回答。

从方法设计看，ThinkGen的VGI-refine模块与ThinkMorph的动态调度机制不同：前者通过固定模板过滤冗余，后者通过动态步骤调整推理深度。ThinkGen的通用性更强，但推理深度受限；ThinkMorph在复杂空间任务上更优，但场景特异性高。这种取舍反映了通用化与精细化的权衡，论文未探索两者结合的可能性。

## 总结

ThinkGen要解决的核心矛盾是CoT在生成任务中的场景特异性与执行脱节问题。其切入点在于解耦架构中显式利用MLLM的CoT推理，并通过VGI-refine和SepGRPO实现推理信号到像素控制的通用化转换。实验证明，启用CoT后WISE准确率从0.55提升至0.76，RISEBench平均分从3.6跃升至13.0，验证了思考驱动生成的有效性。然而，论文未报告置信区间，且训练数据未完全公开，可复现性受限。当支持集增大到5-shot时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.23568)
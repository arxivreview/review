# HuggingFace最新推荐论文 ｜Show, Don't Tell: Morphing Latent Reasoning into Image Generation ｜潜空间推理增强自回归图像生成

作者：Harold Haodong Chen、Xinxiang Yin、Wen-Jie Shu 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.02227)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.02227)

> 现有推理增强图像生成方法依赖显式文本思维链，导致信息压缩与计算冗余。LatentMorph 将中间推理过程保留在连续潜空间，通过自适应触发机制动态介入自回归生成流。该方法在 GenEval 上提升基线模型 16.0%，推理时间减少 44.3%。其核心贡献在于消除感知与执行间隙，但受限于自回归范式，未验证在扩散模型中的泛化性。

## 研究背景

当自回归统一多模态模型（Unified Multimodal Model, UMM）执行文本到图像生成时，其内部隐藏状态蕴含丰富的视觉语义信息，但传统推理增强方法强制将这些状态解码为离散文本。这一过程称为显式思维链（Chain-of-Thought, CoT），它要求模型在固定步长将中间认知转化为自然语言，再重新编码回生成分支。这种离散化转换压缩了高维连续状态至低维符号通道，造成信息丢失，且反复的解码-编码循环消耗大量上下文预算与计算延迟。

主流推理增强范式分为外部循环与内部循环两类。外部循环将大语言模型（Large Language Model, LLM）作为独立优化器，在生成前优化提示或生成后验证输出；内部循环在 UMM 内部交错理解与生成分支，如 TwiG 在固定解码步长插入周期性检查。这些方法均依赖显式 CoT，导致认知不匹配：人类创意过程依赖连续隐式思考而非逐步言语化。LatentMorph 的切入点在于，将推理过程完全保留在连续潜空间，通过动态监控生成状态并自适应触发干预，消除显式文本解码的瓶颈。

## 核心方法

### 方法参照系

本文问题属于推理增强图像生成类别，标准流程为在生成过程中插入显式推理步骤。关键差异在于：本文不依赖离散文本 CoT，而是在连续潜空间执行推理，并通过自适应机制决定干预时机，而非固定步长。

### 动态推理触发机制

固定步长推理在简单任务上冗余，在复杂任务上不足。LatentMorph 引入 RL 训练的推理触发器（Invoker），基于语义一致性与预测不确定性动态决定何时介入。触发器评估当前生成状态 $s_i$，包含短程记忆 $\mathbf{M}^{[s]}$ 与预测熵 $u_i$，计算触发概率：

$$
p_i = \sigma(I_{\text{invoker}}(s_i))
$$

其中 $I_{\text{invoker}}$ 为轻量级策略网络。该机制通过强化学习优化任务奖励与推理效率的平衡，避免冗余推理步骤，实现认知对齐的自适应干预。

### 潜空间推理注入

显式推理将中间状态压缩为文本，丢失高维语义细节。LatentMorph 通过潜空间转换器（Translator）与整形器（Shaper）将连续潜空间思维 $\mathbf{z}$ 转化为生成兼容的控制信号 $\mathbf{c}$，并注入生成器的键值（Key-Value, KV）缓存：

$$
\mathbf{c} = \text{MLP}([\mathbf{z}; \mathbf{m}^{[l]}; \mathbf{p}]) \odot \tanh(\text{Linear}(\mathbf{c}'))
$$

其中 $\mathbf{m}^{[l]}$ 为长程视觉记忆，$\mathbf{p}$ 为提示嵌入。控制信号 $\mathbf{c}$ 生成控制令牌 $\mathbf{E}_{\text{ctrl}}$，直接修改后续令牌预测，无需显式文本解码，保留连续语义线索。

## 实验评估

实验基于 Janus-Pro 骨干，在 GenEval、T2ICompBench、WISE、IPV-Txt 等基准上对比 10 种基线，包括显式推理（T2I-Copilot, MILR）与固定步长推理（TwiG）。缺失扩散模型基线（如 DPO, RLHF）及无推理基线（SFT, GRPO）的充分对比。

| 基准 | 基线 | LatentMorph | 提升幅度 |
| :--- | :--- | :--- | :--- |
| GenEval | Janus-Pro | +16.0% | 绝对值未直接给出 |
| T2ICompBench | Janus-Pro | +25.3% | 绝对值未直接给出 |
| WISE | TwiG-RL | +15.6% | 相对提升 |
| IPV-Txt | TwiG-RL | +11.3% | 相对提升 |

LatentMorph 在 T2ICompBench Non-Spatial 类别上超 TwiG-RL 7.28%，在 3D-Spatial 上超 8.13%。消融实验显示，移除推理触发器导致性能下降，验证动态机制的有效性。推理时间减少 44.3%，令牌消耗减少 51.0%，表明潜空间推理的效率优势。

评估边界：指标未覆盖计算效率维度（原始论文未报告 GPU 耗时），评估协议未区分方法贡献与骨干网络贡献。可复现性：论文提供代码链接，但未公开超参数与训练细节。

## 关联研究分析

从问题动机看，Think-Then-Generate 通过 LLM 推理细化提示，但依赖显式 CoT，导致信息丢失。LatentMorph 将推理保留在潜空间，解决信息压缩问题，但受限于自回归范式，未验证在扩散模型中的适用性。从方法设计看，TwiG 在固定步长插入显式推理，LatentMorph 通过 RL 触发器实现自适应干预，提升认知对齐。TwiG 的固定步长在简单任务上冗余，LatentMorph 的自适应机制在 GenEval 上平均触发 1.14 次，在 WISE 上平均 1.60 次，体现任务复杂度感知。

## 总结

LatentMorph 解决的核心矛盾是显式 CoT 的信息丢失与计算冗余。其切入点在于将推理保留在连续潜空间，通过 RL 触发器动态介入，消除感知与执行间隙。方法通过潜空间转换器与整形器注入控制信号，在 GenEval 上提升 16.0%，推理时间减少 44.3%。边界在于受限于自回归范式，未验证在扩散模型中的泛化性，且评估未区分方法贡献与骨干网络贡献。当支持集增大到 5-shot 时，潜空间推理的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.02227)
# HuggingFace最新推荐论文 ｜Causal-rCM: A Unified Teacher-Forcing and Self-Forcing Open Recipe for Autoregressive Diffusion Distillation in Streaming Video Generation and Interactive World Models ｜因果一致性模型蒸馏

研究机构：清华大学

作者：Kaiwen Zheng、Guande He、Min Zhao 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.25473)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.25473)

> 自回归视频扩散模型在流式生成中面临训练分布与推理分布不一致导致的曝光偏差，现有自强制（Self-Forcing, SF）方法虽能缓解此问题，但对初始化策略敏感且易发生模式崩溃。本文切入点在于揭示教师强制（Teacher-Forcing, TF）与自强制在扩散蒸馏目标上的前向-反向互补性，提出Causal-rCM框架，通过TF一致性模型（CM）离线初始化结合SF分布匹配蒸馏（DMD）在线精调，实现少步流式生成。该框架在Wan2.1-1.3B上以2步采样达到84.63% VBench-T2V分数，但其性能优势高度依赖连续时间CM的JVP内核实现，且未验证在更复杂动作条件场景下的泛化能力。

## 研究背景

自回归视频扩散通过因果注意力Transformer逐帧或逐块预测，替代双向注意力联合去噪，以支持流式长视频生成。这一范式下，模型在训练时依赖真实历史帧（TF）或噪声历史帧（DF），而推理时依赖自身生成的历史帧，导致误差随时间累积，即曝光偏差。为对齐训练与推理分布，自强制范式引入在线策略训练，但基于反向KL散度的DMD目标对初始化敏感，缺乏稳定的离线因果目标作为前置约束。

主流自回归扩散系统如Self Forcing、Causal Forcing等，在SF阶段前采用ODE对回归、DF因果适配或混合TF/DF初始化，但这些策略未系统探讨初始化、因果训练范式与蒸馏损失间的理论联系。现有方法在少步生成中常出现模式崩溃或纹理过平滑，且不同初始化策略的优劣缺乏统一评估框架。本文切入点在于将rCM框架中的前向-反向互补性从双向扩散迁移至自回归场景，论证TF提供离线、模式覆盖的前向信号，SF提供在线、分布匹配的反向信号，二者串行组合可稳定少步生成过程。

## 核心方法

### 前向-反向互补性参照系

rCM框架在双向扩散蒸馏中确立CM作为前向散度、轨迹保持目标，DMD作为反向散度、分布匹配目标。本文将其扩展至自回归场景，关键差异在于：双向扩散中CM与DMD可联合训练，而自回归扩散中TF-CM与SF-DMD需串行执行，因为TF-CM依赖离线因果上下文，SF-DMD依赖自生成轨迹，二者数据分布不同，无法直接联合优化。

### TF-CM离线因果初始化

TF-CM在离线因果上下文上执行少步因果蒸馏，为SF-DMD提供稳定初始化。设计动机在于解决SF-DMD对初始化的敏感性：DMD基于反向KL散度优化自生成轨迹，若初始分布偏离教师分布，易陷入局部极小值导致模式崩溃。TF-CM通过一致性函数$f_\theta(x_t, t) \mapsto x_0$将教师PF-ODE轨迹上的任意点映射至初始点，强制学生在离线因果上下文中保持轨迹一致性。

$$
\mathcal{L}_{\text{TF-CM}} = \mathbb{E}_{x_0 \sim p_{\text{data}}, \epsilon, t} \left[ w(t) \left\| f_\theta(x_t, t) - f_{\theta^-}(\hat{x}_{t-\Delta t}, t-\Delta t) \right\|_2^2 \right]
$$

该公式中，$f_{\theta^-}$为停止梯度版本，$\hat{x}_{t-\Delta t}$为教师ODE求解器从$(x_t, t)$到$t-\Delta t$的数值解。TF-CM确保学生在离线因果上下文中学习稳定的去噪轨迹，为后续在线精调提供模式覆盖基础。

### SF-DMD在线分布精调

SF-DMD在自生成轨迹上执行分布匹配蒸馏，直接优化推理时少步分布。设计动机在于TF-CM仅对齐离线分布，无法捕捉自回归推理中的误差累积效应；SF-DMD通过在线策略训练，使学生在自身生成的轨迹上优化，消除训练-推理分布差距。

$$
\mathcal{L}_{\text{SF-DMD}} = \mathbb{E}_{\hat{x}_0 \sim p_{\text{student}}} \left[ D_{\text{KL}}(p_{\text{teacher}}(\cdot | \hat{x}_0) \| p_{\text{student}}(\cdot | \hat{x}_0)) \right]
$$

该公式中，$\hat{x}_0$为学生自生成轨迹，$p_{\text{teacher}}$与$p_{\text{student}}$分别为教师与学生在给定历史帧下的条件分布。SF-DMD通过反向KL散度最小化，使学生在自生成轨迹上的分布逼近教师分布，直接优化推理时性能。

## 实验评估

实验在Wan2.1 T2V 480p分辨率下进行，使用Wan2.1-1.3B学生模型与Wan2.1-14B教师模型，训练数据为rCM提供的合成T2V数据。基线覆盖Self Forcing、LongLive、Causal Forcing、AnyFlow等自回归方法，但缺失双向DiT基线（如Wan2.1-14B直接对比）的少步生成性能，导致无法公平比较双向与自回归范式在少步生成下的质量-效率权衡。

| 方法 | NFE | Total Score | Quality Score | Semantic Score | Throughput (FPS) | First Latency (s) |
|---|---|---|---|---|---|---|
| Causal-rCM (2-step) | 3 | 84.63 | 85.46 | 81.31 | 12.2 | 0.40 |
| Causal-rCM (1-step) | 2 | 84.63 | 85.54 | 81.01 | 15.9 | 0.40 |
| Self-Forcing (4-step) | 5 | 83.76 | 84.53 | 80.68 | 17.4 | 0.57 |
| AnyFlow (4-step) | 5 | 84.31 | 85.15 | 80.94 | 17.4 | 0.57 |

Causal-rCM在2步与1步设置下均达到84.63% VBench-T2V分数，显著优于Self Forcing的83.76%与AnyFlow的84.31%，且1步设置下吞吐量达15.9 FPS，高于4步基线的17.4 FPS（注：此处吞吐量数值存在矛盾，原文表格中1步Causal-rCM吞吐量为15.9，4步基线为17.4，但1步NFE更少，吞吐量应更高，需核实原文数据一致性）。

消融实验显示，TF-sCM初始化在帧级设置下以1-2k迭代达到81.8 VBench分数，超越TF-dCM训练10k迭代的结果，验证连续时间CM的收敛优势。在块级设置下，TF初始化（84.95%）优于DF初始化（84.80%），但TF-dCM（84.33%）与TF-sCM（84.37%）均低于TF/DF直接初始化，表明在块级设置中，简单因果适配可能比复杂CM初始化更优，这与帧级设置结论相反，揭示初始化策略的最优性依赖于块内时间跨度。

评估边界限于480p分辨率与81帧视频，未测试更高分辨率或更长时长的流式生成。代码开源（NVlabs/rcm），但JVP内核实现细节未完全披露，可复现性依赖自定义FlashAttention-2 JVP内核。指标完备性方面，仅报告VBench-T2V总分与子分数，未报告时序一致性、物理合理性等关键流式生成指标。

## 关联研究分析

从问题动机看，Causal-rCM与Self Forcing均针对自回归扩散的曝光偏差，但Self Forcing依赖ODE对回归或DF初始化，未系统论证初始化的理论必要性；Causal-rCM通过前向-反向互补性框架，将TF-CM定位为SF-DMD的必要前置条件，其根源在于DMD的反向KL散度特性对初始分布的敏感性，而TF-CM的前向散度特性可提供模式覆盖。这一差异是任务特性决定：自回归推理的误差累积效应使得在线优化必须依赖稳定的离线基础，而双向扩散无此约束。

从方法设计看，Causal-rCM与rCM共享前向-反向互补性框架，但rCM在双向扩散中联合训练CM与DMD，Causal-rCM在自回归扩散中串行执行TF-CM与SF-DMD。这一差异源于自回归场景的数据分布特性：TF-CM依赖离线因果上下文，SF-DMD依赖自生成轨迹，二者无法共享同一数据流。与AnyFlow相比，AnyFlow采用TF-MeanFlow (FD) → SF-DMD + SF-MeanFlow (FD) 的混合策略，而Causal-rCM采用TF-dCM/TF-sCM → SF-DMD的纯CM初始化策略，前者引入MeanFlow的JVP计算，后者依赖自定义JVP内核，二者在计算效率与实现复杂度上存在权衡，论文未给出定量对比。

## 总结

Causal-rCM解决的核心矛盾是自回归视频扩散中训练-推理分布不一致导致的曝光偏差与少步生成的模式崩溃。现有方法如Self Forcing虽能通过在线策略缓解曝光偏差，但缺乏稳定的离线因果目标作为前置约束，导致对初始化敏感且易发生模式崩溃。本文抓住TF与SF在扩散蒸馏目标上的前向-反向互补性，提出TF-CM离线初始化结合SF-DMD在线精调的串行策略，通过连续时间CM的JVP内核实现10倍收敛加速。实验证明，2步Causal-rCM在Wan2.1-1.3B上达到84.63% VBench-T2V分数，1步设置下吞吐量达15.9 FPS。其边界在于：块级设置中TF/DF直接初始化优于TF-CM初始化，揭示初始化策略的最优性依赖于块内时间跨度；且未验证在动作条件生成等复杂场景下的泛化能力。当块内时间跨度进一步增大时，TF-CM的模式覆盖优势是否会被DF的噪声鲁棒性超越，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.25473)
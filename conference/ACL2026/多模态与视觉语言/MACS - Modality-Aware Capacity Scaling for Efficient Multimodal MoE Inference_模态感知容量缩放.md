# ACL2026最新论文 ｜MACS: Modality-Aware Capacity Scaling for Efficient Multimodal MoE Inference ｜模态感知容量缩放

研究机构：清华大学、天津大学

作者：Bo Li、Chuan Wu、Shaolin Zhu

论文原文见 [arXiv](https://arxiv.org/abs/2605.05225)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.05225)

> 多模态大语言模型（MLLMs）在专家并行（EP）推理中面临严重的“掉队者效应”，即系统延迟由负载最重的专家决定，而传统基于Token计数的负载均衡方法无法区分视觉Token的信息密度差异与模态比例波动。本文指出，现有方案将冗余背景Token与关键语义Token等同处理，导致资源错配，其切入点在于引入信息感知的负载度量与动态容量调整。MACS通过熵加权负载量化Token语义价值，并结合批级模态比例动态缩放专家容量，在保持99.7%以上原始性能的同时实现最高1.97倍的推理加速。该方案在EP部署场景下具有显著工程价值，但其依赖校准集确定专家类型的做法限制了在极端动态任务流中的泛化能力。

## 研究背景

当MoE架构应用于MLLMs时，视觉编码器产生的数百个Patch Token与文本Token在语义密度上存在本质差异。这种差异导致在EP部署中，若仅依据Token数量分配专家容量，大量低信息量的背景视觉Token会占用本应分配给关键文本或前景视觉Token的计算资源，引发专家负载不均衡。为缓解此问题，CAI-MoE（He et al., 2025）提出了基于静态容量上限的Token丢弃策略，但其核心假设是每个Token具有相等的计算价值，这一假设在多模态场景下失效。

MoE MLLMs的EP推理效率瓶颈源于两个被传统方法忽视的深层机制：信息异构性与模态动态性。信息异构性指视觉输入中大量Patch Token对应低信息背景区域，而文本Token语义密度相对均匀；模态动态性指不同任务（如OCR与纯文本推理）中视觉与文本Token的比例剧烈波动。现有基于Token计数的容量管理方法无法感知这种内部功能特化与外部比例变化，导致在视觉密集任务中专家过载，在文本密集任务中资源闲置。MACS（Li et al., 2026）针对这一盲区，提出从模态感知视角重新定义专家负载，通过信息加权与动态容量调整打破静态计数的局限。

## 核心方法

### 方法参照系

标准MoE EP推理流程中，路由器为每个Token选择Top-k专家，系统通过All-to-All通信分发Token，各设备并行计算后同步结果。传统容量管理（如CAI-MoE）在此流程中引入固定容量因子$\gamma$，当专家接收Token数超过$C_{base} = \gamma \cdot |T|/N$时丢弃多余Token。本文的关键差异在于，将“Token计数”替换为“信息加权负载”，并将“静态容量”替换为“模态自适应动态容量”，从而在分发与计算环节引入语义感知。

### 熵加权专家负载

传统方法在Token分发前仅统计数量，无法区分Token的语义重要性。MACS在路由计算后、Token分发前引入熵加权机制，利用视觉Token特征分布的香农熵$H(x_v)$作为语义重要性的代理指标。对于视觉Token $x_v$，计算其Softmax特征分布的熵，并进行批内Z-score归一化：

$$ \tilde{H}(x_v) = \frac{H(x_v) - \mu_B}{\sigma_B + \epsilon} $$

随后通过Sigmoid函数映射为语义权重 $\omega(x_v) = \sigma(\delta \cdot \tilde{H}(x_v))$，其中$\delta$控制映射灵敏度。文本Token被赋予满权重。专家$E_j$的有效负载定义为 $\tilde{L}_j = \sum_{x \in I_j} \omega(x)$。该设计解决了背景Token占用过多容量导致关键Token被丢弃的问题，使专家能处理更多低信息量Token而不触发容量上限。

### 动态模态自适应容量

静态容量因子无法响应批内模态比例的变化，导致视觉密集批次中视觉专家过载。MACS基于有效视觉比例 $R_v = \frac{\sum_{x \in V} \omega(x)}{\sum_{x \in T} \omega(x)}$ 动态调整专家容量。根据校准集确定的专家类型（视觉、文本、共享），定义模态偏差指示器 $\beta_j$，并按公式 $C_j = C_{base} \cdot (1 + \rho \cdot (\beta_j - R_v))$ 缩放容量，其中$\rho$控制适应强度。当$R_v > 0.5$时，视觉专家容量增加，文本专家容量受限。该机制解决了模态动态性导致的资源错配，确保在OCR等视觉密集任务中视觉专家获得足够资源，而在推理任务中释放资源给文本专家。

## 实验评估

实验在8块NVIDIA A100 GPU上以8路EP部署Qwen3-VL、InternVL3.5和Kimi-VL，对比基线为CAI-MoE的Token Drop与Expanded Drop变体。评估涵盖8个图像理解基准（如TextVQA、MMBench）和5个视频理解基准（如MVBench、VideoMME）。MACS在三个模型上均显著优于CAI-MoE，平均性能保持率超过99.7%，而CAI-MoE Token Drop导致超过7%的性能下降。

| 模型 | 方法 | Avg. (%) |
| :--- | :--- | :--- |
| Qwen3-VL | Vanilla MoE | 100.00 |
| Qwen3-VL | CAI-MoE (Token Drop) | 91.80 |
| Qwen3-VL | MACS (Ours) | 99.78 |
| Kimi-VL | CAI-MoE (Token Drop) | 92.24 |
| Kimi-VL | MACS (Ours) | 99.81 |

消融实验显示，熵加权负载（SL）是性能恢复的主要驱动力，在$\gamma_0=0.5$的受限容量下，SL使Qwen3-VL的MMBench得分从74.29提升至77.94。动态容量（DC）进一步将得分提升至83.41，表明在资源紧张时动态调整比静态加权更有效。局部语义重路由（SR）贡献较小但稳定，将最终得分提升至84.21。

| 配置 | 方法 | MMBench |
| :--- | :--- | :--- |
| $\gamma_0=0.5$ | Baseline (SC) | 74.29 |
| $\gamma_0=0.5$ | + SL | 77.94 |
| $\gamma_0=0.5$ | + DC | 83.41 |
| $\gamma_0=0.5$ | MACS (Ours) | 84.21 |

评估边界方面，论文未报告置信区间，且加速比1.97x依赖于特定硬件配置与$\gamma$值。代码未公开，超参数$\delta$与$\rho$的最优值（$\delta \approx 1.5, \rho=0.6$）仅在Qwen3-VL上验证，跨模型泛化性存疑。

## 关联研究分析

从问题动机看，MACS与CAI-MoE均针对EP中的掉队者效应，但CAI-MoE基于单模态文本假设，将Token视为等值计算单元，而MACS识别出多模态下视觉Token的信息异构性。这一差异源于任务特性：文本Token语义密度均匀，而视觉Token中背景区域占比高，导致Token计数成为负载的糟糕代理。MACS通过熵加权解决了这一根本假设错误，而非仅优化丢弃策略。

从方法设计看，MACS与Stun（Lee et al., 2025）等专家剪枝方法同属EP优化，但Stun通过永久移除冗余专家降低计算量，可能损失模型容量；MACS则通过动态调整容量保留所有专家，仅改变Token分配策略。这种差异表明，在MoE MLLMs中，专家冗余性可能低于单模态LLMs，因为视觉与文本专家承担不同模态的功能特化，剪枝风险更高。MACS的无训练特性使其更适合部署场景，但依赖校准集确定专家类型，若任务分布发生漂移，专家分类可能失效。

## 总结

MACS旨在解决MoE MLLMs在EP推理中因视觉Token信息异构性与模态动态性导致的掉队者效应。现有CAI-MoE等方法基于Token计数假设，无法区分背景与关键Token，导致资源错配；MACS通过熵加权负载与动态模态容量调整，实现了信息感知的资源分配。实验证明，MACS在Qwen3-VL上保持99.78%的原始性能，同时实现1.97倍加速，显著优于CAI-MoE的91.80%性能保持率。然而，该方法依赖校准集确定专家类型，且超参数$\delta$与$\rho$的最优值仅在单一模型上验证。当任务流中视觉与文本比例发生剧烈且未知的漂移时，基于静态校准集的专家分类是否仍能准确反映实时负载需求，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.05225)
# ICLR2026最新论文 ｜Group Critical-token Policy Optimization for Autoregressive Image Generation ｜组关键Token策略优化

研究机构：中国科学技术大学、复旦大学

作者：Guohui Zhang、Hu Yu、Xiaoxiao Ma 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.22485)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.22485)

> 自回归视觉生成模型在强化学习对齐阶段，传统方法对所有图像Token施加均匀的策略梯度更新，忽略了不同Token对全局结构或局部细节贡献度的巨大差异。这种“一刀切”的优化方式导致模型在提升组合性时往往牺牲细节保真度，且训练效率低下。本文切入点在于识别并仅优化对生成结果具有决定性影响的“关键Token”，通过因果依赖、熵梯度空间结构与组内多样性三个维度筛选出约30%的Token进行差异化加权优化。该方法在保持生成质量的同时显著提升了组合生成能力，但其有效性高度依赖于离散Token的空间局部性假设，且在动态分辨率场景下的泛化能力存疑。

## 研究背景

自回归（AR）视觉生成模型将图像离散化为Token序列，通过因果注意力机制逐Token预测。在这一过程中，早期生成的Token通过因果掩码持续影响后续所有Token，确立了图像的全局布局；而后期Token则主要受限于局部一致性，负责填充纹理与细节。这种因果依赖结构意味着，并非所有Token在强化学习（RL）训练中对最终图像质量的贡献是均等的。

Reinforcement Learning with Verifiable Rewards (RLVR) 已被引入视觉生成领域以提升偏好对齐与任务可控性，其中 Group Relative Policy Optimization (GRPO) 是主流算法。然而，现有GRPO实现假设每个Token对训练目标的贡献相同，对所有Token施加均匀的优势函数（Advantage）更新。这种均匀优化忽略了视觉Token的功能分化：部分Token决定全局结构，部分对应背景或细节。在LLM推理领域，研究者已发现“关键Token”（如高熵的逻辑连接词）对推理能力起主导作用，但视觉生成因具备双向空间结构与因果AR建模的双重复杂性，其关键Token的识别机制尚未被探索。

本文旨在解决RLVR训练中Token重要性不均的问题。不同于LLM中基于文本语义熵的关键Token识别，视觉Token的关键性需结合空间结构特性。本文从因果依赖、熵诱导的空间结构以及RLVR关注的Token多样性三个视角，定义了视觉AR生成中的关键Token，并提出了针对性的优化框架。

## 核心方法

### 方法参照系

标准GRPO框架中，对于每个提示词采样一组图像输出，计算组内相对优势，并对所有Token施加相同的策略梯度更新。本文的关键差异在于，不再对所有Token均匀优化，而是先筛选出关键Token子集，并引入动态权重机制，仅对关键Token执行加权策略优化。

### 关键Token识别策略

标准GRPO未区分Token的功能角色，导致背景纹理Token与结构Token共享相同的优化强度。本文提出从三个维度识别关键Token：因果依赖、熵梯度空间结构与组内多样性。首先，基于因果依赖，选取序列前 $K_{init}$ 个Token作为初始关键Token $Z_{init}$，因为这些Token通过因果注意力确立全局结构。其次，针对熵分布的空间局部性，计算2D熵图的梯度。设Token $t$ 的熵为 $H_t$，其局部平均熵 $\bar{H}_t$ 通过邻域平均计算，梯度 $G_t$ 通过中心差分求得：

$$ G_t = \frac{\bar{H}_{t+1} - \bar{H}_{t-1}}{2} $$

选取梯度最大的 $K_{struct}$ 个Token作为结构关键Token $Z_{struct}$，这些Token对应图像结构边界或视觉区域连接处。最后，基于RLVR关注的多样性，计算组内同一位置Token嵌入的余弦相似度，选取相似度最低的 $K_{sim}$ 个Token作为多样性关键Token $Z_{sim}$，这些Token在组内样本间差异大，提供更丰富的奖励信号。最终关键Token集合为三者并集 $Z_{select} = Z_{init} \cup Z_{struct} \cup Z_{sim}$。

### 动态优势权重与优化目标

均匀优势函数无法平衡探索与稳定性：初始Token需适度探索以防结构坍塌，而结构Token需更强探索以提升细节。本文引入基于置信度分歧的动态优势权重。设策略模型与参考模型在第 $j$ 个Token上的置信度（对数概率）分别为 $C_j^{policy}$ 和 $C_j^{ref}$，第 $t$ 个Token的动态权重 $w_t$ 定义为前 $t$ 个Token置信度分歧的累积平均，并施加裁剪系数 $\epsilon_w$ 防止权重过大：

$$ w_t = \text{clip}\left( \frac{1}{t} \sum_{j=1}^{t} |C_j^{policy} - C_j^{ref}|, \epsilon_w \right) $$

GCPO的目标函数在GRPO基础上引入指示函数 $I[z_t \in Z_{select}]$ 与动态权重 $w_t$：

$$ \mathcal{L}_{GCPO} = \mathbb{E} \left[ \sum_{t=1}^{N} I[z_t \in Z_{select}] \cdot w_t \cdot \left( \min\left( r_t A_t, \text{clip}(r_t, 1-\epsilon, 1+\epsilon) A_t \right) \right) \right] $$

该公式确保仅关键Token参与梯度更新，且其优势值根据模型置信度变化动态调整，从而在保持生成先验稳定的同时鼓励关键区域的有效探索。

## 实验评估

实验在LlamaGen、Janus-Pro 1B/7B三个基座模型上验证，使用GenEval、T2I-CompBench及DrawBench评估组合生成与人类偏好。基线覆盖AR模型（LlamaGen, Janus-Pro）、扩散模型（SDXL, FLUX.1-dev）及RL增强方法（T2I-R1, Show-o+PARM）。

| 方法 | GenEval Overall | T2I-CompBench Spatial | HPSv2 |
| :--- | :--- | :--- | :--- |
| Janus-Pro-7B | 0.89 | 0.3150 | 22.12 |
| Janus-Pro-7B+GRPO | 0.92 | 0.3159 | 22.12 |
| Janus-Pro-7B+GCPO | 0.90 | 0.3888 | 22.10 |
| LlamaGen+GCPO | 0.42 | 0.3199 | 20.59 |

GCPO在T2I-CompBench的Spatial任务上较GRPO提升0.0738，Shape任务提升0.1174，表明关键Token优化显著增强了空间关系理解。然而，在GenEval Overall上，Janus-Pro-7B+GCPO (0.90) 略低于GRPO (0.92)，主要归因于Counting任务的波动。消融实验显示，单独使用初始Token、高熵梯度Token或低相似度Token均能带来提升，但三者组合在30% Token预算下效果最佳。动态优势权重的引入使所有指标达到最优，验证了置信度分歧作为探索约束的有效性。

评估边界方面，实验主要基于固定分辨率的离散Token序列，未涉及动态分辨率或视频生成。代码已开源，但超参数细节（如 $K_{init}$ 具体值）需查阅附录。指标侧重组合性与偏好，未报告FID等保真度指标，难以直接对比ImageNet基准上的SOTA。

## 关联研究分析

从问题动机看，本文与T2I-R1 (Jiang et al., 2025) 同属RLVR视觉生成路线，但T2I-R1侧重语义级Chain-of-Thought推理链优化，而本文聚焦Token级稀疏优化。T2I-R1通过联合优化语义与Token级推理提升生成能力，但未区分Token的重要性差异；本文则通过识别关键Token降低计算冗余。这种差异源于任务特性：T2I-R1关注推理过程的逻辑连贯性，而本文关注生成结果的空间结构一致性。

从方法设计看，本文与SimpleAR (Wang et al., 2025b) 同基于GRPO框架，但SimpleAR验证了GRPO提升美学质量，未涉及Token级差异化。本文引入的动态优势权重机制借鉴了LLM推理中“Fork Token”的高熵特性，但将其适配至视觉空间结构。关键差异在于，视觉Token的熵梯度具有空间局部性，而文本Token的熵更多反映语义不确定性。这种空间局部性使得熵梯度成为识别结构边界的有效代理，但其在非结构化背景（如纯色背景）中的有效性未充分验证。

## 总结

本文核心矛盾在于RLVR训练中均匀优化导致的效率低下与结构细节失衡。切入点在于利用视觉Token的空间局部性与因果依赖特性，识别关键Token并实施差异化优化。方法通过因果、熵梯度与多样性三维度筛选30%关键Token，并引入基于置信度分歧的动态权重。实验证明GCPO在T2I-CompBench Spatial任务上较GRPO提升0.0738，验证了关键Token假设的有效性。边界在于实验仅覆盖固定分辨率离散Token，未探索动态分辨率或连续Latent空间下的关键Token识别。当图像分辨率动态变化时，基于固定网格的熵梯度计算是否仍能准确捕捉结构边界，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.22485)
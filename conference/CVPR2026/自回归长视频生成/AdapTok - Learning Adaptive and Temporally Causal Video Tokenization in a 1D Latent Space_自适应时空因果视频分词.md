# CVPR2026最新论文 ｜AdapTok: Learning Adaptive and Temporally Causal Video Tokenization in a 1D Latent Space ｜自适应时空因果视频分词

作者：Yan Li、Changyao Tian、Renqiu Xia 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_adecd62b8d97)

> 自回归视频生成依赖离散化分词器将连续帧转化为Token序列，但固定长度分词忽略了视频内容的时空冗余，导致算力浪费或信息丢失。现有因果分词器虽支持流式处理，却缺乏全局预算约束下的动态分配能力，无法在有限Token数下实现重建质量最优。AdapTok通过1D潜空间解耦空间结构，结合块级因果评分器与整数线性规划（ILP）实现内容感知的自适应Token分配。该方法在UCF-101上以2048个Token达到rFVD 24.06，验证了自适应策略在压缩率与质量间的帕累托优势，但其对长时序语义一致性的影响尚未在分钟级生成中验证。

## 研究背景

自回归视频生成模型（AR-VGM）依赖分词器将视频帧映射为离散Token序列，供Transformer进行因果预测。传统2D VQGAN分词器将每帧独立编码为固定大小的空间网格，这种结构导致Token数量与空间分辨率强绑定，无法根据帧内信息密度动态调整。为解决此问题，1D潜空间分词器（如TiTok）将视频展平为一维序列，使Token分配与空间结构解耦，为变长编码提供了基础。然而，1D序列中的Token位置不再对应固定空间区域，若采用固定长度编码，简单场景会浪费Token，复杂场景则信息不足。

视频分词器需同时满足因果性（支持流式处理）与自适应压缩（优化Token预算）。ElasticTok（2024）首次尝试在视频块内通过尾部丢弃（Tail-Drop）实现变长编码，但其2D局部结构限制了信息在序列头部的聚集，且固定阈值分配无法保证全局预算约束。CausalTok（2025）采用块级因果Transformer架构，但沿用固定Token数，未解决内容冗余问题。AdapTok的切入点在于：将1D潜空间与全局优化分配结合，通过预测不同Token数下的重建质量，在固定预算下实现跨样本、跨时间的动态Token分配，从而在压缩率与重建质量间取得全局最优。

## 核心方法

### 块级因果Transformer架构

AdapTok采用块级因果Transformer作为编码器与解码器骨干，将视频划分为K个块（每块4帧），块内Token可相互注意，块间仅允许前向注意。该架构继承自CausalTok，确保编码过程不依赖未来帧，支持流式处理。与ElasticTok的2D卷积结构不同，AdapTok使用可学习潜Token将3D Patch嵌入投影为1D序列，使Token分配与空间位置解耦，为后续自适应采样提供基础。

### 块级掩码采样与因果评分器

训练阶段，AdapTok引入块级掩码采样器（Block-Mask Sampler），对每个块随机丢弃尾部Token，使模型学习变长表示。具体地，对块 $i$ 保留 $\omega_i$ 个Token，构造二值掩码 $m_i = [1_{j \le \omega_i}]_{j=1}^M$，其中 $M$ 为块最大Token数。该设计迫使模型在信息不完整时仍能重建视频，增强鲁棒性。

推理阶段，AdapTok引入块级因果评分器（Block Causal Scorer）预测不同Token数下的重建质量。评分器以连续潜变量 $z$ 和量化潜变量 $z_q$ 为输入，单次前向传播预测所有候选长度 $\omega_q$ 的感知损失 $\hat{s}$：

$$
\hat{s} = S_\epsilon(z, z_q, M_s^q)_{qM:(q+1)M}
$$

其中 $M_s^q$ 为块级因果注意力掩码。该公式的物理含义是：评分器基于当前块的潜表示，预测若仅保留前 $\omega_q$ 个Token时，重建视频与原始视频的感知差异。通过MSE损失训练，评分器学习Token数与重建质量的映射关系，为全局分配提供依据。

### 整数线性规划Token分配

给定评分器预测的质量分数 $\hat{s}_{kj}$（样本 $k$ 分配 $j$ 个Token时的感知损失），AdapTok通过整数线性规划（ILP）求解全局最优分配。目标函数最小化总感知损失，约束条件为每样本仅选一种长度、总Token数等于预算 $B \cdot N_b$：

$$
\min_{b} \sum_{k,j} \hat{s}_{kj} b_{kj} \quad \text{s.t.} \quad \sum_j b_{kj} = 1 \ (\forall k), \quad \sum_{k,j} j \cdot b_{kj} = B \cdot N_b
$$

其中 $b_{kj} \in \{0,1\}$ 为分配变量。该公式的算法含义是：在固定总Token预算下，将Token分配给能带来最大质量提升的样本-长度组合，实现跨样本的全局帕累托最优。相比ElasticTok的固定阈值分配，ILP避免了局部最优陷阱，确保预算高效利用。

## 实验评估

AdapTok在UCF-101（重建与类条件生成）和Kinetics-600（帧预测）上评估，基线包括ElasticTok、OmniTokenizer、CausalTok及非因果模型Phenaki。主实验显示，AdapTok在2048 Token下rFVD为24.06，优于CausalTok（25.91）和OmniTokenizer（26.19），但略高于ElasticTok（23.97，1024 Token）。在生成任务中，AdapTok-AR（633M参数）在Kinetics-600帧预测上gFVD为11，UCF-101类条件生成gFVD为67，优于CausalTok，表明自适应分词对下游AR生成有正向影响。

| 方法 | 数据规模 | 参数量 | Token数 | rFVD | PSNR | LPIPS |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| ElasticTok† | <0.5M | 210M | 1,022 | 23.97 | 0.227 | 73.06 |
| CausalTok† | <0.5M | 173M | 1,024 | 25.91 | 0.111 | 84.20 |
| AdapTok | <0.5M | 195M | 1,024 | 25.72 | 0.114 | 83.86 |
| AdapTok | <0.5M | 195M | 2,048 | 26.37 | 0.103 | 85.37 |

消融实验验证了各组件必要性。1D潜空间在1024 Token下rFVD为73.42，显著优于2D空间的173.99，证明1D结构对变长编码的鲁棒性。自适应训练（掩码采样）与推理（评分器）联合使用，在1024 Token下rFVD为36.36，优于仅训练（37.13）或仅推理（38.79）。Token分配策略中，ILP（36.36）优于固定分配（38.79）、阈值二分（42.12）和增量二分（38.13），证实全局优化的优势。

评估边界方面，实验仅覆盖4帧短片段，未验证分钟级长视频生成中的语义一致性。rFVD指标对细粒度时序漂移不敏感，且未报告计算效率（ILP求解延迟）。代码已开源，但超参数（如块大小、掩码分布）对长时序的影响未充分探讨。

## 关联研究分析

从问题动机看，AdapTok与ElasticTok均解决变长编码问题，但ElasticTok侧重单视频内帧间自适应，AdapTok扩展至跨样本全局预算优化。ElasticTok的固定阈值分配在预算约束下易导致部分样本Token过剩、部分不足，而AdapTok的ILP通过联合优化确保总预算精确匹配，这一差异源于任务特性：ElasticTok面向单视频压缩，AdapTok面向批量推理效率。然而，ILP求解复杂度随批大小增长，实时性未验证。

从方法设计看，AdapTok与CausalTok共享块级因果架构，但CausalTok固定Token数，AdapTok引入评分器与动态分配。CausalTok的固定长度假设在内容冗余视频上浪费算力，AdapTok的自适应策略通过预测质量分数规避此问题。但AdapTok的评分器仅基于感知损失，未考虑时序一致性，这与长视频生成中误差累积的核心挑战存在潜在冲突。评分器是否能在长序列中准确预测累积误差下的质量，论文未给出回答。

## 总结

AdapTok解决的核心矛盾是固定Token分词与视频内容冗余之间的算力浪费。其切入点在于1D潜空间解耦空间结构，结合评分器与ILP实现全局最优分配，这是固定长度分词器无法做到的。方法通过块级掩码采样训练变长表示，评分器预测质量，ILP求解分配，在UCF-101上以2048 Token达到rFVD 24.06，Kinetics-600帧预测gFVD 11。边界在于实验仅覆盖4帧短片段，未验证长时序生成中的语义一致性，且ILP求解延迟未报告。当视频时长扩展至分钟级时，评分器预测的局部质量分数是否仍能准确反映全局时序一致性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_adecd62b8d97)
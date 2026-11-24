# CVPR2026最新论文 ｜When Transformers Meet Mamba: A Hybrid Transformer-Mamba Network for Video Object Detection ｜混合 Transformer-Mamba 网络用于视频目标检测

作者：Qiang Qi、Xiao Wang、Zongyuan Du 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_59b06691dbe6)

> 视频目标检测（VOD）旨在同时分类与定位视频中的物体，其核心挑战在于平衡长程时空依赖建模能力与计算效率。现有基于 Transformer 的方法虽能捕捉全局上下文，但二次方复杂度限制了其在高分辨率长序列上的实时性；而纯 Mamba 架构虽具备线性复杂度，却缺乏足够的上下文学习能力。本文提出 TMambaDet，通过空间自适应变形 Transformer 编码器、时间级联双向 Mamba 编码器及 Mamba 纠缠 Transformer 解码器的混合架构，在 ImageNet VID 上以 20.6ms 推理时间取得 87.9% mAP。该设计验证了混合架构在 VOD 任务上的有效性，但其在跨域泛化及动态采样稳定性上的表现仍存疑。

## 研究背景

视频目标检测需从多帧视频中提取时空特征以定位物体。传统方法依赖循环神经网络（RNN）或卷积神经网络（CNN），受限于长序列梯度消失与局部感受野，难以捕捉远距离时空依赖。视觉 Transformer（ViT）引入全局注意力机制，显著提升了长程依赖建模能力，但其计算复杂度随序列长度呈二次方增长，导致在高分辨率或长视频序列中计算开销巨大。为缓解此瓶颈，状态空间模型（SSM）如 Mamba 提出线性复杂度的序列建模方案，但其固定大小的隐藏状态限制了上下文学习能力与多任务泛化性，且此前未系统性应用于 VOD 任务。

VOD 领域主流路线基于不同变体的视觉 Transformer，如 TransVOD 利用空间与时间 Transformer 聚合查询与记忆编码，CETR 通过上下文增强 Transformer 提升实时性能。然而，这些方法在跨帧时间依赖建模上仍面临效率与精度的权衡：高效 Transformer 架构往往牺牲部分长程建模能力，而全注意力机制则导致计算成本激增。本文切入点在于利用 Transformer 与 Mamba 的互补性：Transformer 擅长帧内空间依赖建模与上下文学习，Mamba 擅长帧间时间依赖的高效线性建模。通过构建混合架构，本文旨在解决 VOD 中时空解耦建模的效率瓶颈，同时保留 Transformer 的语义理解优势。

## 核心方法

### 时空解耦混合架构参照系

VOD 的标准流程通常包含骨干网络提取特征、时空编码器聚合特征、解码器对齐查询与特征。本文参照系为基于 Deformable DETR 的检测框架，关键差异在于将时空编码解耦：空间维度采用自适应变形 Transformer，时间维度采用双向 Mamba，而非传统的全 Transformer 或全 Mamba 架构。

### 空间自适应变形 Transformer 编码器

标准变形注意力对所有查询使用固定数量采样点，导致背景区域计算冗余。本文提出空间自适应变形 Transformer（SADT）编码器，通过轻量级多层感知机（MLP）预测每个查询的采样强度分数 $\alpha$，动态调整采样点数量 $K_q$。该设计动机是解决复杂物体（如遮挡、模糊）与简单物体在信息密度上的差异，避免对背景区域的无效计算。采样点数量由公式 $K_q = \text{round}(K_{\min} + \alpha \cdot (K_{\max} - K_{\min}))$ 决定，其中 $K_{\min}$ 和 $K_{\max}$ 为预定义的最小与最大采样点数。此机制使复杂物体分配更多采样点以增强局部特征聚合，简单物体分配更少采样点以降低计算开销，从而在帧内实现高效的空间依赖建模。

### 时间级联双向 Mamba 编码器

跨帧时间依赖建模中，Transformer 的二次方复杂度成为瓶颈。本文提出时间级联双向 Mamba（TCBM）编码器，采用时间优先双向扫描算法（TPBS），在固定空间坐标下沿时间正负方向扫描，实现线性复杂度的长程时间依赖建模。该设计动机是解决多帧特征数量增长导致的计算爆炸问题，同时保留双向信息流以捕捉动态时序关系。前向扫描从 $F^s_{0,0}$ 开始，沿时间维度遍历固定空间位置 $j=0$ 的所有帧，再移至 $j=1$，直至覆盖所有空间位置；反向扫描从 $F^s_{0,M}$ 开始，沿时间维度遍历固定空间位置 $j=M$ 的所有帧，再移至 $j=M-1$，直至结束。此扫描策略确保在固定空间坐标下完整捕捉时间动态，避免空间跳跃导致的时序断裂，从而高效聚合跨帧信息。

### Mamba 纠缠 Transformer 解码器

传统 Transformer 解码器仅通过交叉注意力对齐查询与特征，缺乏长程上下文整合。本文提出 Mamba 纠缠 Transformer（MaET）解码器，在标准 Transformer 解码器中插入级联双向 Mamba 层，结合注意力与 Mamba 的优势。该设计动机是解决查询与特征交互中实例级信息不足的问题，通过 Mamba 层整合长程上下文，增强查询的语义丰富性。解码器流程为：多头自注意力（MHSAttn）促进查询间交互，多尺度自适应变形注意力（MADAttn）聚合编码器特征，级联双向 Mamba（CBi-Mamba）整合长程上下文，最终通过前馈网络输出时空解码特征。此混合设计使查询能同时获取局部细节与全局时序信息，提升检测精度。

## 实验评估

实验在 ImageNet VID（3,862 训练视频，555 验证视频，30 类）与 EPIC-KITCHENS-55（272 视频，290 类）上进行，采用 IoU 0.5 下的 mAP 作为指标。基线覆盖 Transformer 方法（TransVOD, CETR, DGC-Net）与 Mamba 方法（MAMBA），但缺失纯 Mamba 基线如 VideoMambaPro 的直接对比。

| 方法 | 骨干 | mAP (%) | 时间 (ms) |
|---|---|---|---|
| TransVOD Lite | ResNet-101 | 80.5 | 28.4 |
| DGC-Net | ResNet-101 | 86.3 | 90.2 |
| TMambaDet | ResNet-101 | 87.9 | 20.6 |
| ODND | Swin-B | 91.3 | 55.2 |
| TMambaDet | Swin-B | 92.1 | 39.0 |

TMambaDet 在 ResNet-101 骨干下以 87.9% mAP 超越 DGC-Net（86.3%）1.6%，且推理时间 20.6ms 显著低于 DGC-Net 的 90.2ms；在 Swin-B 骨干下以 92.1% mAP 超越 ODND（91.3%）0.8%。

| 组件 | 整体 mAP (%) | 慢速 mAP (%) | 快速 mAP (%) |
|---|---|---|---|
| (a) 基线 | 78.3 | 86.4 | 57.8 |
| (b) +SADT | 80.6 | 87.5 | 62.5 |
| (c) +TCBM | 83.8 | 88.9 | 67.5 |
| (f) 完整模型 | 87.9 | 93.3 | 73.1 |

消融显示，TCBM 编码器贡献最大（+5.5% 整体 mAP），SADT 编码器次之（+2.3%），MaET 解码器贡献 +2.6%。快速物体 mAP 提升 15.3%，表明混合架构对动态目标更敏感。固定采样点 $K=4$ 时 mAP 87.4%，自适应采样 87.9%，提升 0.5%，但推理时间从 21.1ms 降至 20.6ms，验证了动态采样的效率优势。

评估边界：指标仅含 mAP 与推理时间，未报告 FLOPs 或内存占用；EPIC-KITCHENS-55 上 TMambaDet（45.1%）低于 TransVOD Lite（47.2%），可能反映跨域泛化局限；代码未公开，超参数（如 $K_{\min}, K_{\max}$）未详细披露，可复现性受限。

## 关联研究分析

从方法设计看，TMambaDet 与 TransVOD++ 同属 Transformer 基线，但 TransVOD++ 依赖全注意力机制建模时空依赖，导致推理时间 28.4ms（ResNet-101）；TMambaDet 通过 Mamba 替代时间 Transformer，将推理时间降至 20.6ms，同时 mAP 提升 7.4%。差异根源在于任务特性：VOD 需实时处理多帧序列，Mamba 的线性复杂度更适配时间维度，而 Transformer 的空间注意力更适配帧内细节。但 TMambaDet 未对比纯 Mamba 方法如 VideoMambaPro，无法确认混合架构是否优于纯 Mamba 在上下文学习上的劣势。

从问题动机看，TMambaDet 与 RAPTOR 同属高效视频建模路线，但 RAPTOR 聚焦视频预测，采用 EVA 模块实现 59.6 FPS 实时预测；TMambaDet 聚焦 VOD，采用 SADT 与 TCBM 实现 20.6ms 推理。差异根源在于任务目标：预测需生成未来帧，强调时序连贯性；检测需定位当前帧物体，强调空间精度。TMambaDet 的自适应采样针对空间冗余，RAPTOR 的 EVA 针对时间冗余，两者在效率优化策略上互补，但 TMambaDet 未探讨物理可解释性，而 RAPTOR 通过课程学习缓解时序不连贯。

## 总结

TMambaDet 旨在解决 VOD 中时空依赖建模的效率与精度矛盾，现有 Transformer 方法受二次方复杂度限制，纯 Mamba 方法缺乏上下文学习能力。本文通过空间自适应变形 Transformer、时间级联双向 Mamba 及 Mamba 纠缠 Transformer 的混合架构，在 ImageNet VID 上以 20.6ms 推理时间取得 87.9% mAP，超越 DGC-Net 1.6%。其边界在于 EPIC-KITCHENS-55 上 mAP 低于 TransVOD Lite，且未报告 FLOPs 与内存占用，代码未公开。当支持集增大或视频序列更长时，自适应采样的稳定性与 Mamba 的长程建模能力是否仍能维持精度优势，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_59b06691dbe6)
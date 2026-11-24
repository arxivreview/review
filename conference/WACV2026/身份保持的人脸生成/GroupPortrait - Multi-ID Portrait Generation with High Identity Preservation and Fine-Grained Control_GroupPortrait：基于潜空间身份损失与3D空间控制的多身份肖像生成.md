# WACV2026最新论文 ｜GroupPortrait: Multi-ID Portrait Generation with High Identity Preservation and Fine-Grained Control ｜GroupPortrait：基于潜空间身份损失与3D空间控制的多身份肖像生成

作者：Meijia Huang、Ruida Li、Bing Ma 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_eefac79fa9f9)

> 多身份肖像生成旨在从少量参考图中同时锁定多个特定人物身份，并精确控制其姿态与布局，以解决单身份方法在多人场景下的特征融合与位置失控问题。现有免微调方法虽提升了效率，但缺乏显式空间约束，导致身份混淆严重且无法应对侧脸等复杂姿态。本文通过引入潜空间身份损失、3DMM驱动的空间姿态网络及掩码注意力机制，在冻结骨干上实现多身份的高保真与细粒度控制。该方法在布局可控性上优于基线，但缺乏与最新SOTA的定量对比，其泛化边界尚待验证。

## 研究背景

多身份生成面临的核心困境在于身份特征与空间位置的解耦。在潜空间扩散模型（LDM）中，身份通常通过全局嵌入注入，这种全局性导致不同身份的特征在去噪过程中相互干扰。为隔离这种干扰，需引入空间定位机制，而2D关键点在侧脸或极端姿态下存在投影失真，这促使研究者转向3D Morphable Model (3DMM) 以获取鲁棒的空间先验。

早期多身份方法如FaceStudio和PortraitBooth依赖多阶段生成或噪声融合，其布局严重依赖初始模板，缺乏对姿态和表情的独立控制能力。FastComposer和MS-Diffusion虽采用单次推理，但主要关注文本到图像的通用生成，在纹理质量和身份保真度上存在局限。GroupPortrait的切入点在于将身份保持与空间控制解耦：一方面通过潜空间损失强化身份记忆，另一方面利用3DMM投影提供精确的空间条件，从而在单次推理中实现多身份的高保真生成。

## 核心方法

### 方法参照系

本文基于Stable Diffusion的UNet架构，继承IP-Adapter的解耦交叉注意力范式。与单身份方法仅注入全局ID嵌入不同，本文针对多身份场景，在注意力机制中引入空间掩码以隔离身份特征，并额外引入3D空间条件以控制姿态。

### 潜空间身份保持机制

传统方法在像素空间计算身份损失，需通过VAE解码器将潜变量还原为图像，计算开销巨大且需多步推理获取预测样本。本文提出LatentID模块，直接在潜空间计算身份一致性。通过训练一个基于ResNet50和ArcFace的提取器，将潜变量映射为身份特征。利用一步反向公式 $\hat{z}_0 = z_0 + f(t) \cdot (\epsilon - \epsilon_\theta(z_t, t, C))$ 获取预测潜变量，其中 $f(t)$ 为时间步截断函数，防止高噪声步长下预测失真。该设计避免了像素解码，显著提升了训练效率，并通过余弦损失 $L_{lid} = 1 - \text{Cosine}(\phi_{lid}(\hat{z}_0), \phi_{lid}(z_0))$ 强化身份保留。

### 3D空间姿态控制

OpenPose ControlNet在侧脸生成中失效，因为2D关键点无法准确反映3D结构。本文引入Facial Controller，利用3DMM提取形状、表情和姿态系数，重组后投影为2D关键点 $L_{2D} = \Pi(R_{ref}L_{3D} + t_{ref})$。基于此训练SpatialPoseNet，作为专门的人脸姿态ControlNet。该网络通过损失函数 $L_s = E_{z_0,t,c_t,c_s,\epsilon \sim N(\mu,\sigma^2)}(||\epsilon - \epsilon_\theta(z_t, t, c_t, c_s)||_2^2)$ 学习空间条件与去噪过程的映射，实现了对面部形状、表情和头部的精确控制。

### 掩码注意力控制器

多身份生成中，面部嵌入常溢出至非面部区域（如衣物颜色）。本文提出Mask-Attention Controller，将面部区域掩码特征与身份特征结合作为Key，而Value保持纯身份特征。公式为 $Z_{new} = \text{Attention}(Q, K_{text}, V_{text}) + \text{Attention}(Q, K_{id} + K_{mask}, V_{id})$。这种设计利用掩码引导注意力聚焦于特定面部区域，防止特征溢出，确保每个身份仅影响其指定位置。

## 实验评估

该论文实验数据不可得，未提供实验表格。论文对比了OMG、FastComposer、MS-Diffusion和Face-Diffuser等基线，覆盖了多阶段生成和单次推理两种路线。然而，缺乏与WithAnyone、DVI等最新多身份SOTA方法的定量对比，使得其在当前领域坐标系中的具体性能位置难以精确界定。基线选择侧重于布局控制能力，但在身份保真度的细粒度评估上缺乏如FaceSim等标准指标的数值支撑。

消融实验部分未在提供的材料中给出具体数值，无法量化各模块（LatentID、Facial Controller、Mask-Attention）的独立贡献。从设计逻辑推断，潜空间损失主要提升训练效率，3DMM控制主要解决侧脸失效问题，而掩码注意力主要解决特征溢出问题。三者协同作用，但缺乏边际收益递减或负迁移的实证分析，难以判断在极端场景下各模块的鲁棒性边界。

评估协议主要依赖定性结果展示，缺乏标准化基准（如MultiID-Bench或XVerseBench）的量化指标。代码未开源，超参数设置（如时间步截断阈值 $R_{tmax}$）未详细披露，限制了可复现性。与领域共识相比，本文使用UNet骨干而非DiT，这在生成多样性上可能受限，但通过3D控制弥补了部分细节缺失。

## 关联研究分析

从问题动机看，GroupPortrait与InstantID等单身份方法的核心差异在于空间隔离机制。InstantID依赖全局ArcFace嵌入，适用于单人脸场景，但在多人场景中无法区分身份归属。GroupPortrait通过Mask-Attention引入空间掩码，解决了特征溢出问题。然而，这种掩码依赖预训练分割模型，在遮挡或模糊场景下可能失效，而InstantID的全局嵌入虽粗糙但鲁棒性更强。

从方法设计看，GroupPortrait与ControlNet的变体SpatialPoseNet存在本质区别。ControlNet通常处理通用姿态图，而SpatialPoseNet专门针对3DMM投影的2D关键点，解决了侧脸投影失真问题。与WithAnyone等基于DiT的方法相比，GroupPortrait依赖UNet和3DMM，计算开销更大，但空间控制更精确。WithAnyone通过解耦身份与上下文提升多样性，而GroupPortrait通过3D结构约束提升保真度，两者在“保真-多样”权衡上做出了不同取舍。

## 总结

GroupPortrait旨在解决多身份生成中的身份混淆与布局失控矛盾，通过潜空间身份损失、3DMM空间控制及掩码注意力机制，在冻结UNet骨干上实现多身份的高保真生成。该方法在布局可控性上优于OMG和FastComposer等基线，但缺乏与WithAnyone等最新SOTA的定量对比，且依赖3DMM在极端遮挡下的鲁棒性未经验证。当参考图像存在严重遮挡或姿态极端偏离时，3DMM投影的准确性是否会成为瓶颈，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_eefac79fa9f9)
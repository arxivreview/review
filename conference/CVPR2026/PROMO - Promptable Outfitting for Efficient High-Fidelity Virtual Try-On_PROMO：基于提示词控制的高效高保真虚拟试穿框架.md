# CVPR2026最新论文 ｜PROMO: Promptable Outfitting for Efficient High-Fidelity Virtual Try-On ｜PROMO：基于提示词控制的高效高保真虚拟试穿框架

研究机构：北京航空航天大学、清华大学

作者：Haohua Chen、Tianze Zhou、Wei Zhu 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.11675)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.11675)

> 虚拟试穿（Virtual Try-On, VTON）旨在将目标服装渲染至人物图像，核心挑战在于平衡生成保真度、推理效率与风格可控性。现有扩散模型方法虽提升了视觉质量，但多依赖复杂的双网络架构或像素级拼接，导致计算开销大且缺乏对穿着风格（如袖长、版型）的精细控制。PROMO 提出基于流匹配扩散 Transformer（DiT）的框架，通过时间自参考机制与空间条件合并实现高效多条件注入，并引入微调的视觉语言模型生成结构化风格提示。该方案在 VITON-HD 和 DressCode 上取得了优于现有 VTON 及通用图像编辑模型的指标，但其性能优势中骨干网络先验与特定模块贡献的边界尚需进一步剥离。

## 研究背景

虚拟试穿的核心技术演进依赖于生成模型对条件信息的处理机制。早期基于生成对抗网络（GAN）的方法依赖显式几何变形对齐服装，易产生伪影；潜空间扩散模型（LDM）将任务重构为条件生成，但传统 U-Net 架构在处理多条件输入时，常需引入独立的参考网络（Reference Net）编码服装特征，导致参数量翻倍且初始化逻辑复杂。此外，像素级图像拼接虽能注入条件，但忽略了掩码、姿态等辅助信息的信息密度差异，迫使所有条件与输出图像保持相同分辨率，造成计算冗余。

当前领域共识认为，扩散 Transformer（DiT）的全局注意力机制更适合处理时空依赖与多模态条件，正逐步取代 U-Net 成为高分辨率试穿的首选骨干。然而，现有 DiT 试穿方法在效率与可控性上存在两个瓶颈：一是多条件注入缺乏高效的缓存机制，导致推理速度慢；二是风格控制依赖闭源大模型或固定文本编码器，无法灵活描述“袖长”、“版型”等细粒度穿着属性。PROMO 的切入点在于将 VTON 视为结构化图像编辑问题，通过解耦空间条件与时间维度的条件注入，同时引入轻量级视觉语言模型（VLM）生成结构化风格提示，以解决效率与可控性的双重约束。

## 核心方法

### 方法参照系

PROMO 基于 FLUX.1-dev 架构，采用流匹配（Flow Matching）范式预测速度场。与 OOTDiffusion 等使用并行参考网络的方法不同，PROMO 摒弃了额外的去噪网络，转而利用单一 DiT 主干，通过潜空间多模态条件拼接与时间自参考机制实现高效条件融合。

### 空间条件合并与区域感知损失

传统方法如 CatVTON 采用像素级拼接，要求掩码与姿态图与人物图像同分辨率（1024×768），导致 Token 数量激增。PROMO 利用掩码与姿态图的信息冗余特性，在像素空间进行 2 倍降采样，并在潜空间将姿态条件直接粘贴至 Agnostic 图像上，最终将双条件 Token 数量从 $2N$ 压缩至 $N/4$，实现 87.5% 的 Token 削减。为平衡背景重建与服装细节，引入区域感知损失权重 $W$：

$$ W = (1 + \lambda) \cdot \mathbb{1}_{\text{body}} + (1 - \lambda) \cdot \mathbb{1}_{\text{bg}} $$

其中 $\mathbb{1}_{\text{body}}$ 为解析掩码指示的身体区域，$\lambda \in [0, 1)$ 控制权重强度。该设计动机在于解决模型过度关注背景而忽略服装纹理的失效问题，通过加权损失强制网络聚焦于服装区域的高频细节。

### 时间自参考与 3D-RoPE 分组

多条件注入通常需重复计算条件 Token 的 Key-Value 对。PROMO 引入时间自参考机制，在首个去噪步 $t=0$ 缓存条件 Token 的 KV 对，后续步骤仅计算查询向量 $Q$ 包含的文本与潜变量部分：

$$ \text{Attention}(Q_t, K_{\text{cache}}, V_{\text{cache}}) = \text{softmax}\left(\frac{Q_t K_{\text{cache}}^T}{\sqrt{d}}\right) V_{\text{cache}} $$

此机制避免了参考网络的参数冗余。同时，利用 3D-RoPE 的时间维度作为组标识符，区分不同服装实例，使得单服装训练模型能在单次前向传播中处理多服装推理，避免了迭代误差累积。该设计解决了传统方法在多服装场景下需多次前向传播导致的效率低下与特征干扰问题。

### 风格提示系统

针对 PromptDresser 依赖闭源 GPT-4o 且仅支持单服装描述的限制，PROMO 构建了风格提示系统。通过 Pydantic 生成 OpenAPI 规范的 JSON Schema，利用 Qwen2.5-VL-72B 标注少量数据并严格过滤，进而微调 Qwen2.5-VL-7B。该 7B 模型在结构化数据上训练，比 72B 模型更快且准确率更高，能够输出包含“袖长”、“版型”等属性的结构化 JSON，并转换为自然语言提示注入 DiT 的文本编码器。

## 实验评估

实验在 VITON-HD（2,032 对测试）和 DressCode（5,400 对测试）上进行，对比基线涵盖 LaDI-VTON、CatVTON、OOTDiffusion 等扩散方法，以及 Seedream 4.0、Qwen-Image-Edit 等通用图像编辑模型。基线覆盖较全面，但缺失 GAN 基线（因已淘汰）及部分最新 DiT 试穿方法如 RefTon。

| 方法 | VITON-HD Paired FID↓ | VITON-HD Paired KID↓ | DressCode Paired FID↓ | DressCode Paired KID↓ |
|---|---|---|---|---|
| LaDI-VTON | 6.8500 | 1.3766 | 5.4700 | 1.9270 |
| CatVTON | 9.4412 | 4.7389 | 6.5372 | 3.9591 |
| OOTDiffusion | 32.8944 | 20.0843 | 3.6623 | 0.8550 |
| PROMO (Ours) | 6.8903 | 1.4895 | 3.3103 | 0.4902 |

PROMO 在 DressCode 上 FID 为 3.3103，显著优于 OOTDiffusion 的 3.6623 和 CatVTON 的 6.5372；在 VITON-HD 上 FID 为 6.8903，与 LaDI-VTON 的 6.8500 接近。值得注意的是，据领域综述，RefTon 在 VITON-HD 上 FID 为 8.5，PROMO 的 6.8903 更低，但 PROMO 基于 FLUX 大模型骨干，而 RefTon 可能使用较小 DiT，骨干差异导致直接数值对比需谨慎。

| 消融配置 | VITON-HD Paired FID↓ | 推理时间 (s) |
|---|---|---|
| w/o T.S.R | 3.3102 | 22.2378 |
| w/o S.T.M | 3.4878 | 11.1030 |
| PROMO (Ours) | 3.3103 | 9.1775 |

消融实验显示，移除时间自参考（T.S.R）使推理时间从 9.1775s 增至 22.2378s，但 FID 几乎不变（3.3102 vs 3.3103），证明 T.S.R 主要贡献于效率而非质量。移除空间 Token 合并（S.T.M）使 FID 从 3.3103 升至 3.4878，推理时间从 9.1775s 增至 11.1030s，表明 S.T.M 在保持质量的同时显著降低计算开销。

评估边界方面，论文未报告置信区间，且 VITON-HD 测试集背景较干净，可能高估野外场景性能。可复现性上，论文提供了 LoRA rank 128、Prodigy 优化器等超参数，但未开源代码，且依赖自训练的 DensePose 模型，复现门槛较高。

## 关联研究分析

从方法设计看，PROMO 与 CatVTON 均处理多条件输入，但 CatVTON 采用双 UNet 架构分别处理人物与服装，通过稀疏注意力对齐，而 PROMO 在单 DiT 内通过 Token 合并与 3D-RoPE 分组实现条件区分。CatVTON 的双分支设计增加了参数冗余，PROMO 的自参考机制则通过缓存 KV 对避免了重复计算，这源于 DiT 全局注意力对长序列的处理优势，而非任务特性决定。PROMO 的 3D-RoPE 分组机制是否能在更复杂的层叠服装场景中保持特征独立性，论文未给出回答。

从问题动机看，PROMO 与 PromptDresser 均关注风格控制，但 PromptDresser 依赖闭源 GPT-4o 生成提示，且仅支持单服装描述，而 PROMO 通过微调 7B VLM 生成结构化 JSON，支持多服装属性描述。PromptDresser 的闭源依赖限制了部署灵活性，PROMO 的开源 VLM 方案解决了成本与多服装描述限制。然而，PROMO 的风格提示系统依赖预定义的 JSON Schema，对于非结构化或模糊的风格描述（如“休闲风”）的泛化能力，论文未进行充分验证。

## 总结

PROMO 旨在解决 VTON 中生成保真度、推理效率与风格可控性之间的权衡矛盾。现有方法依赖双网络或像素拼接，导致计算冗余且缺乏细粒度控制，PROMO 通过时间自参考缓存 KV 对与空间 Token 合并，在单 DiT 内实现高效多条件注入，并引入微调 VLM 生成结构化风格提示。实验表明，PROMO 在 DressCode 上 FID 为 3.3103，推理时间 9.1775s，优于 OOTDiffusion 和 CatVTON。其边界在于，性能优势部分源于 FLUX 大模型骨干的先验，且评估主要在干净背景数据集上进行，野外复杂场景下的鲁棒性未充分验证。当支持集增大或背景复杂度提升时，空间 Token 合并导致的细节损失是否会被放大，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.11675)
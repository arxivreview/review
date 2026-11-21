# CVPR2026最新论文 ｜Multi-Patch Global-to-Local Transformer Architecture For Efficient Flow Matching and Diffusion Model ｜多补丁全局到局部扩散Transformer

研究机构：美国罗格斯大学

作者：Quan Dao、Dimitris Metaxas

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_15ced8a1ed7b)

> 扩散Transformer（DiT）在视觉生成中面临训练与推理的双重计算瓶颈，其各层处理相同数量Token的同构设计导致早期块在低分辨率特征上浪费算力。现有稀疏注意力或掩码方法在减少Token时往往牺牲生成质量或引入额外重建开销，而MPDiT通过架构级层级化补丁调度，将全局建模与局部细化解耦。该方法在ImageNet-256上以50%的GFLOPs削减实现了与标准DiT相当的生成质量，但其收益高度依赖特定的补丁层级配置，且在高分辨率外推与动态分辨率场景下的泛化能力尚存疑。

## 研究背景

扩散模型训练的核心矛盾在于潜在空间（Latent Space）的Token数量与注意力计算复杂度之间的非线性关系。VAE编码器将图像压缩为潜在表示后，标准DiT通过固定大小的补丁嵌入（Patch Embedding）将空间维度映射为序列长度。以ImageNet-256为例，潜在尺寸为32x32，经p=2补丁嵌入后得到256个Token。由于自注意力复杂度为$O(N^2)$，256个Token意味着每层需执行约6.5万次点积运算。然而，去噪过程的早期阶段主要建立全局结构，对局部细节不敏感，此时处理256个Token中的大部分信息是冗余的。

主流加速路线分为两类：一是修改注意力机制，如线性注意力（SANA、LIT）或状态空间模型（Mamba），但前者在长程依赖上表现不佳，后者仅在Token数超过1000时才有显著优势，而潜空间扩散模型通常Token数不足1000；二是Token缩减，如MaskDiT通过掩码建模减少计算，但在75%掩码率下FID高达100，远劣于DiT-XL/4的40 FID，且需额外解码器恢复细节。这些方法要么在架构内部做局部优化，要么通过丢弃信息换取效率，未能从网络层级重新定义Token的分布逻辑。MPDiT的切入点在于将“全局-局部”建模从注意力层内部提升至网络层级，通过改变不同深度块处理的Token数量，实现计算资源的按需分配。

## 核心方法

### 方法参照系

标准DiT架构中，所有N个Transformer块处理相同数量的Token（如256个），形成同构的计算流。本文的关键差异在于打破这种同构性，引入层级化补丁调度：早期块处理大补丁（少Token）以捕获全局上下文，后期块处理小补丁（多Token）以细化局部细节，中间通过上采样模块连接。

### 层级化补丁调度

在标准DiT中，补丁嵌入层将潜在特征$z_t \in \mathbb{R}^{h \times w \times d}$映射为固定长度的Token序列。MPDiT将前$N-k$个块的补丁大小设为$p=4$，将Token数从256降至64，使早期块的注意力复杂度从$O(256^2)$降至$O(64^2)$，即仅计算标准DiT的25%。这一设计解决了早期去噪步中全局结构建立对局部细节不敏感的问题，避免了在低信息密度阶段浪费算力。

$$
\text{GFLOPs}_{\text{early}} \propto (N-k) \cdot (64)^2, \quad \text{GFLOPs}_{\text{std}} \propto N \cdot (256)^2
$$

该公式表明，当$N=28, k=6$时，早期块计算量仅为标准DiT的约1/16，整体GFLOPs削减达50%。

### 上采样与残差连接

早期块输出的64个Token需恢复至256个以支持后期块的局部细化。MPDiT引入上采样模块（Upsample Block）将64个Token扩展为256个，并添加来自原始$p=2$补丁嵌入的256个Token的跳跃连接（Skip Connection）。这一设计解决了单纯上采样导致的高频细节丢失问题，确保后期块既能获取早期块的全局语义，又能保留原始空间特征。

$$
\mathbf{T}_{\text{refined}} = \text{Upsample}(\mathbf{T}_{\text{global}}) + \mathbf{T}_{\text{orig}}
$$

其中$\mathbf{T}_{\text{global}}$为早期块输出的64个Token，$\mathbf{T}_{\text{orig}}$为原始256个Token。该残差连接保证了信息流的完整性，使后期块（$k=4 \to 6$）能在不增加额外解码器的情况下实现高质量局部细化。

## 实验评估

实验在ImageNet-256上进行，采用Flow Matching训练范式，对比基线包括DiT-XL/2、DiT-XL/4及MaskDiT。MPDiT-XL（$k=6$）在160 epoch时达到25.00 FID，与SPRINT持平，但显著优于MaskDiT-XL/2在75%掩码率下的100 FID。值得注意的是，MPDiT未对比TeaCache等推理加速方法，其FID 25.00高于AdaCorrection的2.15 FID，但后者属于训练-free推理加速，而MPDiT是架构级训练优化，二者目标不同。

| 方法 | 补丁策略 | FID (ImageNet-256) | GFLOPs削减 |
| --- | --- | --- | --- |
| DiT-XL/4 | p=2 (256 tokens) | ~40 | 0% |
| MaskDiT-XL/2 | 75% mask | ~100 | ~75% |
| MPDiT-XL | p=4→p=2 (64→256) | 25.00 | 50% |

消融实验显示，$k$值从4增至6时FID略有下降，但GFLOPs削减比例从约45%提升至50%，表明后期块数量对质量影响有限，而早期块Token数对效率影响显著。FNO时间嵌入相比线性嵌入带来约4点FID提升，验证了时间步建模对收敛速度的关键作用。

评估边界方面，论文仅报告ImageNet-256结果，未提供512x512或视频生成实验，且未报告置信区间。代码已开源，但超参数（如FNO维度选择32）基于启发式搜索，缺乏系统性消融。

## 关联研究分析

从问题动机看，MPDiT与SPRINT同属架构级Token缩减，但SPRINT通过稀疏-稠密残差路径解耦计算，而MPDiT通过补丁大小层级化实现。SPRINT的稀疏路径需额外训练，MPDiT的上采样模块则依赖跳跃连接，后者在实现上更简洁，但前者在极端压缩比下可能保留更多表达能力。从方法设计看，MPDiT与MaskDiT均涉及Token减少，但MaskDiT通过掩码丢弃信息并需解码器重建，MPDiT通过上采样恢复信息且无需额外解码器。这一差异源于任务特性：MaskDiT面向通用掩码建模，MPDiT针对扩散去噪过程的全局-局部特性，后者在避免信息丢失方面更具优势。

## 总结

MPDiT旨在解决DiT同构架构中早期块计算冗余与后期块细节不足之间的矛盾。其切入点在于将全局-局部建模从注意力层提升至网络层级，通过大补丁减少早期Token数，小补丁细化后期细节，并以跳跃连接保证信息完整性。实验证明，该架构在ImageNet-256上以50% GFLOPs削减实现了25.00 FID，与SPRINT持平但优于MaskDiT。然而，论文未验证高分辨率（512x512）下的三级补丁层级（p=8,4,2）效果，且FNO时间嵌入的维度选择缺乏系统性消融。当潜在空间Token数超过1000时，MPDiT的层级化设计是否仍能保持50%的效率优势，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_15ced8a1ed7b)
# HuggingFace最新推荐论文 ｜MPEG-Diffusion: Mixed-Resolution Video Generation ｜MPEG-Diffusion：混合分辨率视频生成

作者：Dennis Menn、Tianpei Gu、Guande He 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2611.12069)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2611.12069)

> 视频扩散模型（Video Diffusion Transformers, DiTs）在生成高质量视频时面临计算复杂度随Token数量二次方增长的瓶颈。现有加速方法如Token合并或步数蒸馏虽能降低计算量，但往往导致细节丢失或模式崩溃，且混合分辨率生成因注意力机制失配与解码边界伪影而难以实用。MPEG-Diffusion通过双分辨率注意力机制解决跨分辨率键值对（Key/Value）共享导致的注意力偏差，利用混合分辨率解码器消除潜空间边界伪影，并基于DiT特征自选择高分辨率区域。该方法在仅处理30%全分辨率Token的情况下实现4.8倍加速，质量接近全分辨率生成，为空间维度的计算冗余优化提供了新范式。其局限在于线性映射假设在极端纹理下可能失效，且未与步数蒸馏等时间维度优化方法联合评估。

## 研究背景

当视频生成模型处理高分辨率长视频时，Transformer架构中的自注意力机制计算量随Token序列长度呈二次方增长，导致推理延迟极高。为缓解这一瓶颈，研究者尝试在空间维度引入混合分辨率生成（Mixed-Resolution Generation），即对视觉重要区域保持高分辨率（High Resolution, HR），背景区域采用低分辨率（Low Resolution, LR）。然而，现有混合分辨率方法在视频生成中遭遇严重质量下降，表现为细节模糊与分辨率边界处的明显伪影。

这一失效源于三个被忽视的根本原因：首先，在共享键值对（Shared Key/Value, K/V）的注意力机制下，单个LR Token无法等效替代多个HR Token的注意力贡献，导致跨分辨率注意力失配；其次，变分自编码器（Variational Autoencoder, VAE）解码器对邻域敏感，直接拼接HR与LR潜变量会在边界产生严重失真；最后，生成模型需在视频生成前确定HR区域，但早期去噪阶段特征模糊，难以通过外部检测器准确定位主体。MPEG-Diffusion针对这三个根因提出系统性解决方案，将视频编码中“按需分配比特”的思想迁移至视频生成计算资源分配中。

## 核心方法

### 方法参照系：混合分辨率生成流程

混合分辨率生成的标准流程包括：确定HR区域掩码、在HR/LR双轨上并行去噪、以及将混合潜变量解码为视频。本文问题与该通用流程的关键差异在于：传统方法假设HR/LR Token可共享同一套K/V矩阵，且解码时直接拼接或简单上采样，忽略了注意力机制的分辨率敏感性与VAE解码器的邻域依赖性。MPEG-Diffusion通过双分辨率注意力、混合分辨率解码器与自选择区域机制重构了这一流程。

### 双分辨率注意力机制

在标准Transformer中，若HR与LR Token共享K/V，单个LR Token无法匹配其替代的$n$个HR Token的注意力输出。MPEG-Diffusion提出双分辨率注意力，为HR与LR分别维护完整的K/V集合，并通过线性映射补全缺失分辨率的K/V。对于HR查询$Q_H$，其注意力输出为：

$$
O_H = \text{Attn}\left(Q_H, \begin{bmatrix} K_H \\ f_\uparrow(K_L) \end{bmatrix}, \begin{bmatrix} V_H \\ f_\uparrow(V_L) \end{bmatrix}\right)
$$

其中$f_\uparrow$为将LR Token映射至HR分辨率的线性层。该设计确保每个查询仅读取自身分辨率的K/V，避免了跨分辨率注意力导致的语义扭曲。实验表明，HR与LR Token间存在强线性关系（余弦相似度达0.96），使得线性映射足以补全信息，从而在保持Softmax注意力局部细节能力的同时，将计算复杂度从$O(N^2)$降至与Token数量线性相关。

### 混合分辨率解码器

VAE解码器要求输入潜变量具有统一空间网格，直接解码混合分辨率潜变量会导致边界伪影。MPEG-Diffusion提出混合分辨率解码器，在潜空间融合HR与LR特征。首先将LR潜变量$z_l$在HR区域$M$处填充降采样的HR潜变量$D(z_h)$，并通过学习到的上采样器$U$扩展至HR网格：

$$
\hat{z}_l = U\left((1-M) \odot z_l + M \odot D(z_h)\right)
$$

随后，小型3D卷积网络$G$以掩码$M$为引导，预测LR区域的残差$\Delta$以消除边界接缝：

$$
\hat{z} = M_\uparrow \odot z_h + (1-M_\uparrow) \odot (\hat{z}_l + \Delta)
$$

该机制确保每个解码补丁在邻域内看到一致的邻居，实验显示边界处的LPIPS误差从0.19降至0.12，显著缓解了分辨率切换带来的视觉断裂。

### 自选择高分辨率区域

传统混合分辨率方法依赖预知HR区域，而生成模型在早期去噪阶段无法通过外部检测器定位主体。MPEG-Diffusion利用DiT特征本身包含的语义信息，在去噪第$k$步通过线性头预测HR掩码。对于DiT中间层输出$h_b$，评分函数为：

$$
s_b = w^\top \text{LN}(h_b)
$$

其中$w$为学习权重，LN为层归一化。评分经时空平滑后，通过相对阈值化生成掩码$M$。该机制无需外部模型，仅增加0.04%运行时开销，即可在去噪过程中动态追踪视觉主体，实现纯文本到视频的自适应分辨率分配。

## 实验评估

实验在Wan2.1 1.3B（480p）与14B（720p）模型上进行，生成81帧视频，对比Token合并（ToMe, IDM）与混合分辨率基线（Phase-Aligned RoPE, Foveated Diffusion）。在30% Token预算下，MPEG-Diffusion在14B模型上实现4.8倍加速，DOVER质量得分0.794，接近全分辨率的0.819，显著优于Foveated Diffusion的0.743。

| 方法 | 模型 | Token比例 | 加速比 | DOVER | VBench Quality |
| :--- | :--- | :--- | :--- | :--- | :--- |
| HR | Wan2.1 14B | 100% | 1.0× | 0.819 | 85.3 |
| LR | Wan2.1 14B | 25% | 7.2× | 0.768 | 84.4 |
| Foveated Diffusion | Wan2.1 14B | 30% | 5.2× | 0.743 | 83.9 |
| MPEG-Diffusion | Wan2.1 14B | 30% | 4.8× | 0.794 | 83.9 |

消融实验验证了双分辨率注意力的有效性：在HR/LR边界处，双分辨率注意力将时间LPIPS从4.59降至4.14，扭曲误差从2.61降至1.96。自选择区域机制在14B模型上达到0.67的mIoU，准确追踪主体。然而，评估未覆盖与步数蒸馏（如DMD）或线性注意力（如SANA-Video）的联合优化效果，且未报告长视频（>81帧）的时序一致性指标。代码未开源，复现依赖64块NVIDIA B200 GPU的训练环境。

## 关联研究分析

从问题动机看，MPEG-Diffusion与Foveated Diffusion同属混合分辨率路线，但后者依赖预知注视点且采用共享K/V，导致边界伪影与注意力失配。MPEG-Diffusion通过双分辨率K/V映射与潜空间混合解码，解决了跨分辨率信息交互的根本缺陷。相比之下，Token合并方法（如ToMe）直接丢弃冗余Token，在高压缩比下导致噪声崩溃，而MPEG-Diffusion保留LR Token并通过线性映射补全信息，维持了语义完整性。

从方法设计看，MPEG-Diffusion与SANA-Video均旨在降低注意力复杂度，但路径不同：SANA-Video通过线性注意力将复杂度降至$O(N)$，牺牲了Softmax注意力的局部细节建模能力；MPEG-Diffusion保留Softmax注意力，通过空间分辨率混合减少有效Token数量，在保持局部细节的同时实现加速。查询侧增强在数据充足时是否仍有增益，论文未给出回答。

## 总结

MPEG-Diffusion针对混合分辨率视频生成中的注意力失配、解码伪影与区域预知依赖三大瓶颈，提出双分辨率注意力、混合分辨率解码器与自选择区域机制。在Wan2.1 14B上，该方法以30% Token预算实现4.8倍加速，DOVER得分0.794，接近全分辨率质量。其边界在于线性K/V映射假设在极端纹理下可能失效，且未与时间维度优化方法（如步数蒸馏）联合评估。当空间分辨率混合与步数蒸馏叠加时，双分辨率注意力的线性映射是否仍具鲁棒性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2611.12069)
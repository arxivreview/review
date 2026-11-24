# CVPR2026最新论文 ｜Align Images Before You Generate ｜挖掘扩散模型内部对应关系以对齐生成图像

研究机构：新加坡国立大学

作者：Shihua Zhang、Qiuhong Shen、Xinchao Wang

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_baf272fcfad8)

> 多图像扩散模型在生成多视图或视频时，常因缺乏显式几何约束导致纹理与结构漂移，破坏时空一致性。现有方法依赖外部深度图、光流或大规模数据训练，难以在无先验的纯生成场景中通用。本文发现扩散模型中间特征已隐含跨图像对应关系，提出CorrAdapter模块，通过复用注意力权重构建对应并聚合匹配区域特征，实现训练-free的一致性增强。该方法在静态多视图与动态视频任务上均提升了几何一致性，但其有效性依赖于模型内部特征的稳定性，且未验证在极端视角变化下的鲁棒性。

## 研究背景

多图像扩散模型通过潜在空间去噪生成一组图像 $X = \{x_i\}_{i=1}^N$，其核心挑战在于确保不同视图间语义与结构的连贯。传统方法依赖外部几何先验，如深度图或光流，来约束生成过程，但这些先验在纯文本或单图条件生成中不可得。潜在扩散模型（Latent Diffusion Model, LDM）在去噪过程中，Transformer块通过自注意力机制交互所有图像的潜在特征 $Z_t$，这一过程隐含了跨视图的信息关联。

多视图生成与视频生成领域长期受困于时空一致性缺失。主流路线分为两类：一是依赖大规模数据训练的跨图像Transformer，如MVAdapter，其隐式引导能力弱，在大视角变化下仍出现结构漂移；二是引入显式几何约束，如SyncDreamer利用多视图几何，但仅适用于静态场景且需已知图像输入。这些方法无法同时满足静态/动态场景适用性与无外部输入的需求。本文切入点在于挖掘扩散模型内部特征中已存在的对应关系，将其作为生成过程的内在引导，无需额外监督或外部先验。

## 核心方法

### 方法参照系

本文问题属于多图像扩散生成中的时空一致性增强。标准流程为：给定条件 $C$，通过T步去噪生成潜在特征 $Z_0$，再解码为图像。关键差异在于，本文不修改主干去噪网络 $\epsilon_\theta$，而是在Transformer块旁路注入CorrAdapter，利用中间特征 $F_t^{in}$ 构建对应并调制信息交互。

### 原生对应关系构建

CorrAdapter首先从扩散模型中间特征中提取跨图像对应关系。在Transformer块中，注意力权重 $A_t = \text{Softmax}(\frac{Q_t K_t^T}{\sqrt{D}})$ 反映了特征间的相似度。对于图像对 $(i, j)$，相似度分数 $s_t^{i,j}$ 定义为：

$$
s_t^{i,j} = \text{Softmax}\left( \frac{q_t^i (k_t^j)^T}{\sqrt{D}} \right)
$$

其中 $q_t^i, k_t^j$ 分别为图像 $i, j$ 的查询与键向量。通过最近邻匹配 $\text{argmax}_l s_t^{i,j}[:, l]$ 获得对应索引 $c_t^{i,j}$。这一设计动机在于，扩散模型在训练过程中已隐式学习场景结构，中间特征即使处于噪声状态，仍保留语义与几何对齐信息，解决了外部先验缺失下的对应关系获取难题。

### 对齐区域聚合

基于构建的对应关系，CorrAdapter通过对齐区域聚合器强化匹配区域的信息交换。对于图像 $i$ 的特征 $f_t^{in,i}[k]$，在图像 $j$ 中裁剪以 $c_t^{i,j}[k]$ 为中心的 $(2r+1) \times (2r+1)$ 窗口，计算聚合特征：

$$
\hat{f}_t^i[k] = \text{Softmax}\left( \frac{q_t^i[k] (k_{t,crop-k}^j)^T}{\sqrt{D}} \right) v_{t,crop-k}^j
$$

该公式仅聚合对应区域特征，抑制非匹配区域干扰。聚合特征 $\hat{F}_t$ 与原始输出 $\hat{F}_t^{out}$ 加权融合：

$$
\check{F}_t^{out} = \eta \hat{F}_t^{out} + (1-\eta) \hat{F}_t
$$

随后通过前馈网络更新。这一设计通过限制信息交互范围，减少歧义传播，直接提升生成图像的时空一致性。CorrAdapter参数初始化自主干Transformer并冻结，实现训练-free即插即用。

## 实验评估

实验在GSO数据集（图像条件，100场景）与Objaverse数据集（文本条件，1000提示）上进行，基线包括SyncDreamer与MVAdapter。SyncDreamer依赖多视图几何，MVAdapter采用跨图像Transformer，两者均未使用外部深度或光流。CorrAdapter作为旁路模块，不改变主干架构。

| 方法 | PSNR↑ | SSIM↑ | LPIPS↓ | cPSNR↑ | cSSIM↑ | cLPIPS↓ | CD↓ | depth↓ | MEt3R↓ |
|---|---|---|---|---|---|---|---|---|---|
| SyncDreamer | 19.24 | 0.8215 | 0.1557 | 26.28 | 0.8817 | 0.0634 | 2.66 | 14.15 | 0.1656 |
| SyncDreamer+CorrAdapter | 19.72 | 0.8310 | 0.1472 | 27.20 | 0.8926 | 0.0572 | 2.67 | 12.60 | 0.1529 |
| MVAdapter | 23.15 | 0.8761 | 0.1276 | 18.75 | 0.7201 | 0.2519 | 9.75 | 73.47 | 0.2116 |
| MVAdapter+CorrAdapter | 23.82 | 0.8829 | 0.1235 | 19.68 | 0.7396 | 0.2371 | 9.20 | 68.62 | 0.2036 |
| MVAdapter+CorrAdapter⋆ | 24.05 | 0.8866 | 0.1220 | 20.47 | 0.7634 | 0.2256 | 9.33 | 67.47 | 0.1955 |

图像条件任务中，CorrAdapter显著提升几何一致性指标。SyncDreamer+CorrAdapter的cPSNR从26.28提升至27.20，depth误差从14.15降至12.60；MVAdapter+CorrAdapter的cPSNR从18.75提升至19.68，depth误差从73.47降至68.62。带训练方案（⋆）的MVAdapter+CorrAdapter⋆在cPSNR上进一步达到20.47，但CD指标略高于无训练版本（9.33 vs 9.20），表明训练方案在特定指标上存在权衡。

文本条件任务中，MVAdapter+CorrAdapter⋆的FID从24.20降至23.42（无训练）或24.17（训练），IS从15.22提升至15.96或17.07。cPSNR从14.09提升至14.29或15.27，depth误差从79.84降至79.72或77.94。训练方案在IS与cPSNR上收益更明显，但FID提升有限，暗示内部对应关系挖掘对感知质量的影响大于对分布匹配的影响。

评估指标涵盖单图像质量（PSNR, SSIM, LPIPS, FID, IS, CLIP-Score）与几何一致性（cPSNR, cSSIM, cLPIPS, CD, depth, MEt3R）。几何一致性指标基于MVGBench协议，通过3DGS重建评估。代码已开源，但论文未报告计算开销与GPU配置，且未提供置信区间。训练方案依赖LoRA微调与一致性损失，超参数 $\eta, \lambda$ 未详细披露。

## 关联研究分析

从问题动机看，CorrAdapter与SpheRoPE均利用扩散模型内部先验，但SpheRoPE依赖球面位置编码处理ERP投影畸变，而CorrAdapter通过特征匹配建立通用对应关系，不依赖特定几何表示。这一差异源于任务特性：SpheRoPE针对全景视频的球面拓扑约束，CorrAdapter针对通用多视图的局部结构对齐。CorrAdapter在极端视角变化下的鲁棒性未经验证，而SpheRoPE的球面感知机制可能更适应大视角偏移。

从方法设计看，CorrAdapter与Pantheon360均追求几何一致性，但Pantheon360依赖外部3D点云作为条件，显式控制相机轨迹，而CorrAdapter仅使用内部特征，无需3D重建。这一差异反映了“外部条件派”与“架构内嵌派”的分歧：Pantheon360在精确控制上占优，但依赖3D重建质量；CorrAdapter在灵活性上占优，但几何可控性较弱。CorrAdapter未提供证据支持其在3D重建任务上优于显式条件方法，其优势仅限于生成质量提升。

## 总结

本文解决的核心矛盾是纯生成场景下缺乏外部先验导致的时空一致性缺失。现有方法依赖外部几何或大规模数据，无法通用；本文发现扩散模型中间特征已隐含对应关系，通过CorrAdapter复用注意力权重构建对应并聚合匹配区域，实现训练-free的一致性增强。实验显示，在GSO上SyncDreamer+CorrAdapter的cPSNR达27.20，MVAdapter+CorrAdapter⋆的depth误差降至67.47，验证了内部对应关系挖掘的有效性。本文边界在于未验证极端视角变化下的鲁棒性，且训练方案在CD指标上存在轻微退化。当视角变化超过一定阈值时，内部特征对应的稳定性是否足以维持几何一致性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_baf272fcfad8)
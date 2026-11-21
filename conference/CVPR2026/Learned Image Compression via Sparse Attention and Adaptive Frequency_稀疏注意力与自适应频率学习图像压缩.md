# CVPR2026最新论文 ｜Learned Image Compression via Sparse Attention and Adaptive Frequency ｜稀疏注意力与自适应频率学习图像压缩

研究机构：南开大学、新加坡南洋理工大学

作者：Huidong Ma、Xinyan Shi、Hui Sun 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_76f26990d2d2)

> 学习图像压缩（Learned Image Compression, LIC）在率失真性能上已超越传统标准，但主流Transformer架构的二次方复杂度导致解码延迟高，难以满足实时部署需求。现有方法要么牺牲全局依赖建模换取速度，要么依赖固定频率变换缺乏内容适应性。SAAF通过引入窗口条件稀疏全局Token的交叉稀疏窗口注意力（Cross-Sparse Window Attention, CSWA）与内容自适应频率块（Adaptive Frequency Block, AFB），在保持高压缩率的同时将推理延迟降至67ms。该方法在效率-性能平衡上表现优异，但其绝对压缩率仍低于最新超先验SOTA，且未验证在极端低码率下的语义保真度。

## 研究背景

图像压缩的核心在于通过拉格朗日乘子平衡比特率与失真，这一率失真优化（Rate-Distortion Optimization, RDO）准则贯穿所有LIC模型。早期CNN架构受限于局部感受野，引入Transformer后虽提升了长程依赖建模能力，但标准窗口多头自注意力（Window-based Multi-head Self-attention, WMSA）的局部性导致信息传播受限，而移位窗口机制虽解决此问题却引入了更高的计算复杂度。同时，多数LIC方法忽略多尺度频率模式，少数引入频率变换的工作仍依赖固定小波基，无法实现内容自适应。

主流路线在效率与性能间存在显著矛盾：MLIC++等Transformer方法RD性能强但延迟高达211ms；MambaIC等状态空间模型（State Space Model, SSM）路线虽降低复杂度，但在特定纹理场景下泛化能力存疑。SAAF的切入点在于不改变超先验+自回归的主流熵模型框架，而是从变换网络内部重构空间与频率双路径：用稀疏全局Token替代移位窗口以线性复杂度捕获长程依赖，用动态权重生成器替代固定频率基以实现内容自适应，从而在单一架构内同时解决空间建模效率与频率适应性两个瓶颈。

## 核心方法

### 方法参照系

SAAF基于超先验框架，包含主变换网络与熵模型。主变换将图像$x$映射为潜变量$y$，经量化$\hat{y}$后由解码器重建$\hat{x}$；超先验模块从$y$提取超潜变量$z$，估计$y$的高斯分布参数$(\mu, \sigma)$以指导熵编码。本文问题与该通用流程的关键差异在于：传统方法中变换网络的空间建模依赖WMSA或SSM，频率处理依赖固定基，而SAAF将空间路径重构为稀疏注意力，频率路径重构为自适应权重调制。

### 交叉稀疏窗口注意力

WMSA仅建模窗口内局部依赖，移位窗口需多层堆叠才能传播全局信息，导致计算开销随层数线性增长。SAAF提出CSWA，由局部窗口注意力（Local Window Attention, LWA）、全局稀疏注意力（Global Sparse Attention, GSA）和局部-全局混合（Local-Global Mixing, LGM）组成。GSA引入$N_g$个可学习全局Token $G_i$，其值由共享参数$G_{learn}$与窗口$X_i$的均值特征$\bar{X}_i$相加得到，实现窗口条件化的全局表示：

$$G_i = G_{learn} + \bar{X}_i$$

每个窗口的$M^2$个局部Token仅与$N_g$个全局Token计算交叉注意力，注意力矩阵维度从$M^2 \times M^2$降至$M^2 \times N_g$。这一设计以极小的参数开销捕获跨窗口长程依赖，避免了移位窗口的多层堆叠，使单块计算复杂度从二次方降至线性。

### 自适应频率块与去噪正则化

现有频率变换依赖固定小波基，无法适应不同图像内容的频率分布差异。SAAF的AFB通过分解权重生成器（Decomposition Weight Generator, DWG）动态生成4个频率带（LL, LH, HL, HH）的响应权重图$A_{freq} \in \mathbb{R}^{H \times W \times 4}$，并结合可学习全局权重$w_{freq} \in \mathbb{R}^4$对输入特征进行内容自适应重加权：

$$X_{freq} = \sum_{k=1}^{4} w_{freq}^{(k)} \cdot (X \odot A_{freq}^{(k)})$$

其中$\odot$表示逐元素乘法。该公式表明频率分解不再是固定基的线性投影，而是由网络根据输入内容动态决定的非线性调制。此外，SAAF引入训练时去噪正则化（Denoising-as-Regularizer, DaR）模块，通过向潜变量$y$注入噪声并训练轻量级条件噪声预测器估计该噪声，迫使潜空间分布更结构化、平滑。DaR仅在训练阶段生效，推理时零开销，通过正则化潜变量分布提升重建质量与泛化能力。

## 实验评估

实验在Kodak（24张768×512）、CLIC Professional Validation（41张2K）和Tecnick（100张1200×1200）数据集上评估，对比MLIC++、TCM、DCAE、MambaIC等12种基线。基线覆盖Transformer、SSM及混合架构路线，但缺失2026年最新SSM方法如Cassic和ARCHE，且未包含针对机器视觉任务的ICM方法。

| 方法 | Kodak BD-Rate (%) | CLIC BD-Rate (%) | Tecnick BD-Rate (%) | Latency (ms) |
|---|---|---|---|---|
| BASE | -0.64 | -1.86 | -3.52 | - |
| SAB (Ng=2) | -1.86 | -2.53 | -4.16 | - |
| AFB | -3.42 | -4.35 | -5.81 | - |
| DaR | -1.56 | -2.63 | -4.29 | - |
| SAAF (ALL) | -3.99 | -4.59 | -6.04 | 67 |

消融实验显示，AFB对BD-Rate的贡献最大（Kodak上-3.42%），其次为SAB（-1.86%）和DaR（-1.56%）。全局Token数量$N_g$从1增至3时，Kodak BD-Rate从-1.32%改善至-1.64%，但边际收益递减，表明$N_g=2$是效率-性能平衡点。CSWA相比WMSA将延迟从264.24ms降至231.21ms，FLOPs从0.44M降至0.33M，验证了稀疏化的效率优势。

评估边界方面，论文仅报告PSNR和BD-Rate，未提供LPIPS等感知指标，无法评估感知质量；实验未在真实边缘硬件上验证，实验室延迟数据可能高估实际部署性能；代码已开源，但训练超参数（如学习率衰减策略）未详细披露，可复现性依赖默认设置。

## 关联研究分析

从问题动机看，SAAF与MambaIC均针对Transformer复杂度瓶颈，但路线截然不同：MambaIC采用SSM的线性复杂度直接替代注意力，而SAAF保留Transformer框架并通过稀疏化降低计算量。这一差异源于任务特性：SSM在序列建模上具有天然优势，但图像压缩中空间依赖的局部性使得稀疏Token可能比全局状态更经济。SAAF的CSWA在Kodak上BD-Rate为-3.99%，低于MambaIC的-18.06%（据领域综述），表明在绝对压缩率上SSM路线仍占优，但SAAF的67ms延迟显著低于MLIC++的211ms，验证了稀疏化在效率上的竞争力。

从方法设计看，SAAF的AFB与FLIC（Frequency-Aware Transformer）同属频率感知路线，但FLIC依赖固定小波基，SAAF采用动态权重生成。这一改进的根源在于固定基无法适应图像内容的频率分布变化，而动态权重允许网络根据输入内容调整频率响应。然而，SAAF未验证AFB在极端低码率（<0.05 bpp）下的表现，而FLIC在低码率下可能因固定基的稳定性而更具优势。查询侧增强在数据充足时是否仍有增益，论文未给出回答。

## 总结

SAAF要解决的核心矛盾是LIC中率失真性能与推理延迟的冲突。现有Transformer方法延迟高，SSM方法绝对压缩率虽高但架构复杂，固定频率变换缺乏适应性。SAAF通过CSWA的稀疏全局Token实现线性复杂度长程建模，通过AFB的动态权重实现内容自适应频率处理，通过DaR的训练时正则化提升潜空间质量。实验证明SAAF在Kodak上BD-Rate为-3.99%，延迟67ms，优于MLIC++的211ms延迟。其边界在于绝对压缩率低于最新SSM SOTA，且未验证极端低码率下的语义保真度。当全局Token数量$N_g$进一步减少时，CSWA的长程依赖建模能力是否仍能维持，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_76f26990d2d2)
# ICLR2026最新论文 ｜MIXLINEAR: EXTREME LOW RESOURCE MULTIVARI - ATE TIME SERIES FORECASTING WITH 0 _._ 1 _K_ PARAME TERS ｜MixLinear：双域解耦的极端低参数量长期时序预测

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_26439244)

> 长期时序预测（Long-term Time Series Forecasting, LTSF）旨在利用历史多变量数据预测远端未来值，其核心矛盾在于预测视野扩展带来的计算复杂度激增与边缘设备部署需求之间的冲突。现有Transformer架构虽精度高，但二次复杂度与百万级参数量使其在资源受限场景下不可行，而纯线性或纯频域模型又难以兼顾局部波动与全局趋势的差异化统计特性。MixLinear通过时域分段线性分解与频域自适应低秩滤波的双路径解耦，将复杂度从 $O(n^2)$ 降至 $O(n)$，以0.1K参数实现了与主流模型相当的预测精度。该方案在效率-精度权衡上处于前沿，但其无预训练、仅点预测的设计限制了其在分布外场景下的泛化能力验证。

## 研究背景

长期时序预测面临的核心困境是预测视野 $H$ 与模型复杂度的非线性增长关系。当历史窗口 $L$ 和预测视野 $H$ 同时增大时，传统自注意力机制的 $O(L^2)$ 计算复杂度导致推理延迟呈指数级上升，使得模型无法在嵌入式传感器或边缘计算设备上实时运行。这一效率瓶颈并非源于参数量的绝对规模，而是源于当前架构对时序模式表征的结构低效：主流模型使用统一的机制同时捕捉高频局部波动与低频全局趋势，而这两类成分在统计特性上存在本质差异——局部特征具有时间局部性，全局结构则在频域呈现稀疏性。

LTSF领域的主流路线分为两类：一类是基于Transformer的复杂架构（如PatchTST、TimesNet），通过自注意力捕捉长程依赖，但参数量通常在百万级以上；另一类是高效线性模型（如DLinear、FITS、SparseTSF），通过简化计算结构降低开销，但往往牺牲了对复杂模式的捕捉能力。FITS利用频域变换处理全局趋势，效率极高，但用全局频率分量建模局部瞬态变化需要过多系数，导致效率增益被抵消；SparseTSF通过稀疏注意力处理局部模式，但缺乏对全局频谱结构的显式建模。MixLinear的切入点在于识别出这种“单域统一建模”的结构缺陷，提出将局部与全局模式分别在其最自然的域（时域与频域）中处理，并通过极致的参数压缩实现双域协同。

## 核心方法

### 方法参照系

MixLinear属于高效线性LTSF架构，其参照系为DLinear与FITS等单域线性模型。与这些方法的关键差异在于，MixLinear摒弃了单一映射策略，采用双路径解耦架构：时域路径处理局部趋势，频域路径处理全局趋势，两者通过可学习上采样融合。这种设计避免了传统混合时频模型中常见的参数爆炸问题，同时保留了线性模型的 $O(n)$ 复杂度优势。

### 时域分段线性分解

时域路径旨在高效捕捉局部波动，解决纯频域模型在建模瞬态特征时的系数冗余问题。输入序列 $X \in \mathbb{R}^{L \times C}$ 首先通过下采样因子 $\pi$ 降维至 $n = L/\pi$，随后划分为 $M$ 个长度为 $r = L/(\pi \cdot M)$ 的非重叠段。对每段 $x^{(s)}$，应用两个正交线性变换：段内变换 $\mathbf{h}^{(s)}_{\text{intra}} = \text{Linear}_{\text{intra}}(x^{(s)}) \in \mathbb{R}^{d \times C}$ 压缩局部波形信息，段间变换 $\mathbf{H}_{\text{inter}} = \text{Linear}_{\text{inter}}(\mathbf{H}_{\text{intra}}) \in \mathbb{R}^{M \times d \times C}$ 建模跨段依赖。该分解将复杂度从 $O(n^2)$ 降至 $O(dr + dM)$，即 $O(n)$，通过分离局部形状建模与全局趋势聚合，避免了单一全连接层对局部与全局模式的混淆。

$$
\mathbf{X}_T = \text{Upsample}(\text{Reshape}(\mathbf{H}_{\text{inter}}, H)) \in \mathbb{R}^{H \times C}
$$

此公式表示段间依赖经重整形与上采样后重构为预测视野 $H$ 的时域输出，其物理含义是通过分层线性映射保留时序的层级结构，同时以线性复杂度实现长序列处理。

### 频域自适应低秩滤波

频域路径旨在压缩全局趋势，解决全频滤波器的过拟合与计算冗余问题。对下采样序列应用快速傅里叶变换（FFT）得到频谱张量 $\mathbf{X}_S \in \mathbb{C}^{n \times C}$。为避免学习 $(L/\pi) \times (L/\pi)$ 的全尺寸复数滤波器，MixLinear采用秩约束矩阵分解，将频谱变换参数化为秩 $nz$ 算子：$\mathbf{Z}_S = \mathbf{U} \mathbf{V} \mathbf{X}_S$，其中 $\mathbf{U} \in \mathbb{C}^{(L/\pi) \times nz}$，$\mathbf{V} \in \mathbb{C}^{nz \times (L/\pi)}$，且 $nz \ll L/\pi$。该设计将频谱投影至共享低维潜空间，再通过自适应基 $\mathbf{U}$ 重构，仅保留主导频率模式。

$$
\mathbf{X}_F = \text{iFFT}(\mathbf{U} \mathbf{V} \mathbf{X}_S) \in \mathbb{R}^{n \times C}
$$

此公式表示通过低秩滤波后的频谱经逆傅里叶变换重构为时域全局趋势，其算法含义是利用自然信号在频域的稀疏性，以 $4rnz$ 个实参数实现极端压缩，同时保留对长期趋势与季节性的捕捉能力。

## 实验评估

实验在ETTh1、ETTh2、ETTm1、ETTm2、Exchange、Solar、Electricity、Traffic八个LTSF基准上进行，回看窗口 $L=720$，预测视野 $H \in \{96, 192, 336, 720\}$。基线覆盖线性模型（DLinear、FITS、SparseTSF）与Transformer模型（PatchTST、TimesNet），但缺失TSFM类基线（如TimesFM、Chronos），无法直接对比零样本泛化能力。

| 数据集 | 视野 | MixLinear MSE | SparseTSF MSE | FITS MSE | MixLinear MACs | SparseTSF MACs |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| ETTh1 | 720 | 0.426 | 0.426 | 0.434 | 196.56K | 277.20K |
| Exchange | 720 | 0.954 | 0.954 | 0.954 | 224.64K | 316.80K |
| Electricity | 720 | 0.205 | 0.205 | 0.205 | 9.01M | 12.71M |
| Traffic | 720 | 0.448 | 0.448 | 0.448 | 24.20M | 34.14M |

MixLinear在Exchange数据集上较SparseTSF提升16.2%（RPD），在ETTh1上提升5.3%，验证了双域解耦对复杂模式的捕捉优势。在效率方面，MixLinear参数量仅0.1K，较SparseTSF（1K）减少81%，较FITS（10K）减少99%；在Traffic数据集上，推理时间2.05ms，较SparseTSF（4.20ms）加速2.12倍，较FITS（4.77ms）加速2.58倍。

消融实验显示，移除频域滤波（w/o Filtering）在低维数据集（ETTh1）上MSE为0.425，移除时域分段（w/o Segment）为0.474，表明局部线性变换在通道相关性弱时更有效；而在高维数据集（Traffic）上，w/o Segment的MSE为0.478，优于w/o Filtering的0.528，说明低秩频谱滤波在压缩全局动态时更具优势。MixLinear完整模型在Electricity上MSE为0.209，Traffic上为0.452，均优于单路径变体，验证了双域互补性。

评估边界方面，论文仅报告MSE与MACs，未提供置信区间或计算效率的内存占用数据；实验环境为单卡NVIDIA A100，代码未公开，超参数（如下采样因子 $\pi$、段长 $r$、秩 $nz$）的敏感性分析仅覆盖部分数据集，可复现性受限。

## 关联研究分析

从问题动机看，MixLinear与FITS同属频域高效预测路线，但FITS采用全频滤波，而MixLinear引入低秩约束。这一差异的根源在于FITS假设频谱能量均匀分布，而MixLinear利用自然信号在频域的稀疏性，通过秩 $nz=2$ 的极端压缩聚焦主导模式。然而，MixLinear未验证低秩假设在频谱非稀疏场景（如混沌系统）下的有效性，这可能导致其在特定数据分布下性能衰减。

从方法设计看，MixLinear与SparseTSF同属时域高效预测路线，但SparseTSF使用稀疏注意力，而MixLinear采用分段线性分解。这一差异源于SparseTSF试图在单一域内同时处理局部与全局依赖，而MixLinear通过域解耦避免了这种混淆。MixLinear的时域路径复杂度 $O(n)$ 低于SparseTSF的 $O(n \log n)$，但两者均未提供概率预测能力，这与TSFM领域“概率预测更优”的共识形成对比，暗示MixLinear在高风险场景（如金融、医疗）中的应用潜力受限。

## 总结

MixLinear要解决的核心矛盾是LTSF中预测视野扩展与边缘设备部署效率的冲突。其切入点在于识别出单域统一建模的结构低效，通过时域分段线性分解与频域低秩滤波的双路径解耦，将复杂度降至 $O(n)$，以0.1K参数实现了与主流模型相当的精度。实验证明其在Exchange数据集上较SparseTSF提升16.2%，推理时间加速2.58倍，验证了双域解耦的效率-精度优势。然而，论文仅验证了少样本/全样本场景，未提供零样本泛化能力或分布漂移下的鲁棒性数据，且缺乏概率预测维度。当输入序列的频谱稀疏性假设失效时，低秩滤波的性能衰减程度如何，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_26439244)
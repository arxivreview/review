# HuggingFace最新推荐论文 ｜Lightning Unified Video Editing via In-Context Sparse Attention ｜上下文稀疏注意力

研究机构：香港科技大学、美国亚利桑那大学

作者：Shitong Shao、Zikai Zhou、Haopeng Li 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.04569)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.04569)

> 视频编辑任务正从专用模块转向统一的上下文学习（ICL）范式，但将源视频与上下文视频直接拼接导致序列长度翻倍，注意力计算的二次方复杂度成为推理瓶颈。现有稀疏注意力机制未区分上下文与源Token的语义差异，导致在ICL场景下加速比有限且质量损失明显。本文提出ISA，通过预筛选冗余上下文Token并基于Query锐度动态路由至全注意力或零阶泰勒稀疏注意力，在14B模型上实现约60%的注意力延迟降低且保持编辑质量无损。该方案在编辑基准上超越了全注意力基线，但其“无损”定义依赖于特定超参数配置，且未验证在极端长序列下的显存线性增长特性。

## 研究背景

视频编辑模型处理长序列时，注意力机制的计算量随序列长度平方增长。ICL范式通过直接拼接上下文Token与源Token来最大化信息融合，使得序列长度 $N$ 达到数万级别，导致GPU显存与延迟激增。标准注意力计算 $O = \text{softmax}(QK^\top/\sqrt{D})V$ 中，$Q, K, V$ 的维度均为 $N \times D$，当 $N$ 从5K增至50K时，计算成本呈二次方上升，且ICL中上下文Token数量通常与源Token相当，进一步将计算量放大四倍。

主流稀疏注意力方法如Radial Attention、STA等基于通用视频生成设计，未利用ICL中上下文Token与源Token的结构差异。实验显示，源Query与源Key的注意力分数显著高于源Query与上下文Key的交互，且该差异在深层网络中加剧。这表明上下文Token对注意力分布的贡献极低，存在大量冗余。现有方法忽略这一分布特性，导致在保留关键信息的同时无法有效降低计算复杂度，限制了ICL视频编辑模型的实时部署能力。

本文切入点在于识别ICL注意力矩阵的四区域分布特征，特别是上下文Token的低显著性。通过理论分析证明Query锐度与泰勒展开近似误差成正比，ISA利用这一关系动态分组Query，对高误差Query执行全注意力，对低误差Query执行稀疏近似，从而在保持编辑保真度的前提下实现加速。

## 核心方法

### 方法参照系

本文问题属于推理端计算优化，区别于视频离散化器在编码端减少Token数量。标准流程为全注意力计算，本文差异在于引入基于ICL结构特性的稀疏近似机制，而非简单的Token剪枝或合并。

### 上下文Token预筛选

预筛选阶段解决上下文Token冗余导致的计算浪费。通常做法是对所有Token执行全注意力，本文利用Pooling Attention生成压缩评分矩阵 $S_{\text{coarse}}$，通过Top-$k$选择保留 $\alpha_s \lceil L_{\text{ctx}}/b \rceil$ 个最显著的上下文块。该操作将复杂度从 $O(NSD)$ 降至 $O(N(L_{\text{src}} + \alpha_s L_{\text{ctx}})D)$，其中 $L_{\text{src}}$ 和 $L_{\text{ctx}}$ 分别为源和上下文Token数量。设计动机在于利用ICL中上下文Token低显著性的分布特性，从源头减少无效计算。

### 基于锐度的动态分组与泰勒稀疏注意力

预筛选后，剩余计算通过Query锐度 $M_u$ 动态路由。锐度定义为块内注意力分布的方差：

$$ M_u = \mathbb{E}_{i \in \text{Block}_u} [\| \sigma(z_i) \|_2^2] $$

其中 $\sigma(z_i)$ 为Token $i$ 的注意力分布。理论证明近似误差 $E_u$ 上界与 $M_u$ 成正比。高锐度Query路由至FlashAttention v2/3执行全注意力，低锐度Query执行零阶泰勒稀疏注意力，其核心公式为：

$$ \text{exp}(Q_i K_j^\top) V_j \approx \text{exp}(Q_i K_j^{[c] \top}) V_j^{[c]} $$

其中 $K_j^{[c]}, V_j^{[c]}$ 为块均值。该近似将块内计算复杂度从 $O(L_Q L_K D)$ 降至 $O(L_Q D)$。设计动机在于利用锐度作为误差代理指标，避免计算高成本的 $\|Q(K-K^{[c]})^\top\|_\infty$，实现硬件友好的动态分组。

## 实验评估

实验在EditVerseBench、VIE-Bench和IVE-Bench上进行，基线包括TokenFlow、STDF、InsV2V、Lucy Edit等编辑模型及Radial、STA等稀疏注意力变体。基线覆盖全面，但缺失视频压缩领域的专用基线如SCORE或InfoTok，因任务目标不同（编辑保真度 vs 压缩率），此类对比不适用。

| 方法 | Quality | Text Align | Temporal Consistency | Editing Quality | Pick Score (Frame) | Pick Score (Video) | SpeedUp (vs FA3) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| LIVEditor (full-attention) | 7.62 | 19.98 | 27.13 | 23.80 | 99.24 | 99.19 | 1.00 |
| LIVEditor (ISA) | 7.89 | 20.09 | 27.19 | 24.55 | 99.32 | 99.22 | 1.47 |
| EditVerse | 7.65 | 20.07 | 26.73 | 23.93 | 98.56 | 98.44 | - |
| InsV2V | 5.95 | 19.52 | 25.67 | 22.77 | 97.22 | 96.83 | - |

LIVEditor (ISA) 在所有VLM评估指标上均优于全注意力基线，其中Editing Quality提升0.75，Pick Score (Frame)提升0.08，同时实现1.47倍加速。这表明ISA不仅无损，反而因稀疏化去除了噪声干扰提升了质量。

消融实验显示，微调ISA后近似误差显著降低，验证了其可训练性。超参数 $\alpha_f$（Flat Ratio）和 $\alpha_{ns}$（No-Sparsity Ratio）的降低导致加速比单调增加，但论文未报告具体数值阈值下的质量-速度权衡曲线。在训练-free场景下，ISA相比STA、SWA等稀疏基线在Quality和Text Align上优势明显，但SpeedUp仅为1.47，低于STA的2.09，表明ISA在极端稀疏度下可能牺牲了部分加速潜力以换取质量。

评估边界方面，论文未报告显存占用随序列长度的具体增长曲线，仅定性描述为“显著增加”。代码已开源，但超参数 $\alpha_s, \alpha_f, \alpha_{ns}$ 的默认值未在正文中明确列出，仅提及“默认设置BLOCK=64”。指标完备性上，缺乏对时序一致性指标的严格阈值定义，“无损”主要基于VLM评分的相对提升，而非绝对误差界限。

## 关联研究分析

从问题动机看，ISA与FastV均利用模型内部信号进行动态决策，但FastV基于浅层注意力分数剪枝Token，而ISA基于Query锐度近似计算。FastV的剪枝不可逆，可能丢失关键细节，ISA的泰勒近似保留了块均值信息，更适合编辑任务对局部细节的高要求。这一差异源于任务特性：视频理解允许一定信息损失，而视频编辑要求像素级保真。

从方法设计看，ISA与Pooling Attention共享粗粒度筛选机制，但ISA引入了基于泰勒展开的细粒度近似。Pooling Attention仅用于确定块掩码，ISA将其扩展为动态分组依据。与视频离散化器如InfoTok相比，ISA不改变Token数量，而是改变计算精度，属于正交优化路线。InfoTok通过信息熵估计调整Token长度，ISA通过锐度估计调整计算精度，两者可结合使用，但论文未探索这种组合效应。

## 总结

本文核心矛盾是ICL视频编辑中序列长度翻倍导致的注意力计算瓶颈。现有稀疏机制未区分上下文与源Token的语义差异，导致加速比有限。ISA抓住上下文Token低显著性这一被忽略的点，通过预筛选和基于锐度的泰勒稀疏近似，在14B模型上实现1.47倍加速且编辑质量超越全注意力基线。其边界在于“无损”定义依赖于VLM评分的相对提升，且未验证在极端长序列下的显存线性增长特性。当序列长度超过131K时，ISA的稀疏内核与全注意力内核的计算比例是否仍保持最优，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.04569)
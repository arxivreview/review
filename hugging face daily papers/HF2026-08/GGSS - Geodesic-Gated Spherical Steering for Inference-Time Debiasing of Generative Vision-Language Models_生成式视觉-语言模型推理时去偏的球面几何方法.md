# HuggingFace最新推荐论文 ｜GGSS: Geodesic-Gated Spherical Steering for Inference-Time Debiasing of Generative Vision-Language Models ｜生成式视觉-语言模型推理时去偏的球面几何方法

研究机构：新加坡国立大学

作者：Yiqun Sun、Junyu Chen、Pengfei Wei 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2608.25375)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2608.25375)

> 生成式视觉-语言模型（Generative VLMs）在招聘等高风险场景中复现人口统计偏见，而现有针对静态编码器或CLIP架构的推理时去偏方法直接移植至多模态解码器时，因破坏激活范数与忽略token级偏见异质性导致性能崩溃。本文切入点在于识别出欧氏硬投影在生成式架构中的几何失效，提出GGSS框架。该方法通过球面线性插值保持范数，并利用自适应门控仅对高偏见token进行干预。GGSS在四个主流VLM上实现了最低平均偏见降低，同时保持通用能力基本无损，但其效果依赖于反事实图像集的质量与子空间线性假设。

## 研究背景

生成式VLM将图像编码为大量视觉token，这些token经投影层进入语言模型解码器。视觉激活的范数与方向共同决定注意力权重分布，任何对激活向量的几何扰动都会直接影响下游解码质量。传统去偏方法假设偏见信号在嵌入空间中呈线性可分，通过欧氏减法移除偏见方向，但这会同时改变向量的范数与方向，导致注意力机制失效。

该领域长期聚焦于CLIP等静态编码器的嵌入空间偏差，主流路线包括INLP、LEACE等线性子空间投影方法。这些方法在静态嵌入上有效，但生成式VLM的激活具有token级异质性：人口统计信号仅集中在面部或衣物等少数token，而背景或姿态token几乎不含偏见信息。硬投影对所有token施加统一干预，过度修正低偏见token并损害任务性能。此外，种族等属性具有多分类结构，单一偏见方向假设无法覆盖低维子空间中的复杂变异。

本文针对生成式VLM的上述失效模式，提出GGSS框架。其核心假设是：偏见信号在单位超球面上表现为切空间中的低维子空间变异，且token级偏见强度服从可校准的分布。通过球面几何操作与自适应门控，GGSS在保持激活范数的前提下实现选择性去偏，解决了硬投影在生成式架构中的几何与语义双重失效问题。

## 核心方法

### 方法参照系

本文问题属于推理时去偏类别，标准流程为：离线发现偏见方向，在线对激活向量执行投影或算术修正。关键差异在于，生成式VLM的激活是token级张量而非全局嵌入，且范数保持对解码质量至关重要，因此标准欧氏投影流程在此场景下失效。

### 反事实偏见子空间发现

设计动机：传统分类器引导的偏见方向估计依赖监督探针，且假设单一方向，无法处理多分类属性的低维子空间结构。本文从反事实图像集出发，通过球面几何直接估计偏见子空间。

对固定上下文 $u$ 下的反事实图像 $x_{u,a}$，计算归一化池化激活 $y_{u,a}$，并求球面Fréchet均值 $\mu_u$。保护属性 $a$ 的切空间偏移为 $s_{u,a} = \log_{\mu_u}(y_{u,a})$。堆叠所有偏移得到矩阵 $S$，执行奇异值分解 $S = U\Sigma V^\top$，取前 $k$ 个右奇异向量构成偏见子空间 $V_{bias}$：

$$V_{bias} = [v_1, \dots, v_k] \in \mathbb{R}^{D \times k}$$

该公式的物理含义是：$V_{bias}$ 的列空间张成了保护属性在切空间中的主要变异方向，且由于 $V$ 的列正交，$V_{bias}^\top V_{bias} = I_k$，保证了投影的无偏性。

### 球面线性插值与自适应门控

设计动机：欧氏减法破坏范数，且均匀投影过度干预低偏见token。本文用球面线性插值（Spherical Linear Interpolation, Slerp）替代硬投影，并引入基于偏见范数分布的门控机制。

对推理时的token $h_i$，计算半径 $r_i = \|h_i\|_2$ 与单位方向 $\hat{h}_i = \nu(h_i)$。映射到切空间 $t_i = \log_\mu(\hat{h}_i)$，分解为偏见分量 $p_i = V_{bias}V_{bias}^\top t_i$ 与干净分量 $t_i^{clean} = (I - V_{bias}V_{bias}^\top)t_i$。目标方向为 $\hat{h}_i^{target} = \exp_\mu(t_i^{clean})$。门控值 $g_i$ 由发现集的偏见范数分布校准：

$$g_i = g_{floor} + (1 - g_{floor}) \sigma\left(\kappa \frac{\|V_{bias}^\top t_i\|_2 - \tilde{b}}{\sigma_b + \epsilon}\right)$$

其中 $\tilde{b}$ 与 $\sigma_b$ 分别为发现集偏见范数的中位数与标准差。最终更新为 $\hat{h}_i^{steered} = \text{Slerp}(\hat{h}_i, \hat{h}_i^{target}; \alpha g_i)$，并恢复半径 $h_i^{steered} = r_i \hat{h}_i^{steered}$。该公式确保：当 $g_i$ 接近0时，token方向几乎不变；当 $g_i$ 接近1时，执行完整球面旋转。Slerp操作严格保持范数，避免了欧氏减法导致的注意力权重崩溃。

## 实验评估

实验在Pixtral-12B、LLaVA-1.6-Vicuna-7B、LLaVA-1.6-Mistral-7B、Qwen3-VL-4B-Instruct四个生成式VLM上进行，使用REFLECT/FOCUS反事实图像集，评估指标包括MCQ（JSD×10³）、2AFC（race_bias_std）、N/D（性别差距）及MMStar通用能力。基线覆盖INLP、MeanDiff、BendVLM、LEACE四个家族的十种变体，以及提示工程方法。

| 方法 | Pixtral-12B Avg Δ% | LLaVA-Vicuna-7B Avg Δ% | LLaVA-Mistral-7B Avg Δ% | Qwen3-VL-4B Avg Δ% |
| --- | --- | --- | --- | --- |
| INLP (sph.) | -37% | -86% | -78% | -49% |
| BendVLM (Eucl.) | -37% | - | - | - |
| GGSS (Ours) | -55% | -90% | -80% | -60% |

GGSS在全部四个模型上取得最低平均偏见降低，其中LLaVA-Vicuna-7B上达到-90%，显著优于最强基线INLP (sph.)的-86%。在N/D任务上，GGSS将LLaVA-Vicuna-7B的性别差距从0.600降至0.025（-96%），MCQ任务从8.70降至1.36（-84%）。MMStar准确率变化在±0.6 p.p.以内，而BendVLM (sph.)在Pixtral上MMStar崩溃至6.9（-46.7%），验证了球面几何对能力保持的关键作用。

| 变体 | JSD×1k ↓ | Bias Red. % ↑ |
| --- | --- | --- |
| Baseline (unsteered) | 14.646 | – |
| Pooled SVD (Eucl.; hard proj., no gate) | 4.261 | 70.9 |
| Pooled SVD (sph.; hard proj., no gate) | 5.612 | 61.7 |
| GGSS w/o gate (gi ≡1) | 5.612 | 61.7 |
| GGSS w/o Slerp (hard proj. + gate) | 4.533 | 69.1 |
| GGSS (full) | 2.414 | 83.5 |

消融实验显示，完整GGSS（Slerp+门控）比无门控版本多降低14个百分点偏见，比无Slerp版本多降低14.4个百分点。门控与Slerp的贡献相当，但二者协同效应显著：单独使用任一组件均无法达到完整框架的性能。敏感性分析表明，$\kappa=5, g_{floor}=0.3$为最优配置，高$\kappa$配合低$g_{floor}$会导致过选择，正$g_{floor}$可恢复性能。

评估边界方面，MMStar仅覆盖通用能力，未评估生成图像的美学质量或文本对齐度；反事实图像集限于面部特写，未涵盖全身或场景级偏见；代码已开源，但超参数$\kappa$与$g_{floor}$需针对新模型重新校准，缺乏自动调参机制。

## 关联研究分析

从方法设计看，GGSS与FairImagen等T2I去偏方法共享“离线发现偏见方向、在线投影”的范式，但FairImagen作用于扩散模型的提示嵌入，假设偏见在嵌入空间中线性可分，而GGSS作用于生成式VLM的token激活，必须处理范数保持与token级异质性。这一差异源于任务特性：扩散模型的潜空间是连续噪声场，而生成式VLM的激活是离散token序列，后者对几何扰动更敏感。GGSS的球面几何选择是否适用于所有VLM架构的激活分布，论文未给出跨架构的普适性证明。

从问题动机看，GGSS与EquiSteer等动态引导方法均旨在解决公平性与效用权衡，但EquiSteer通过调整引导强度实现动态平衡，而GGSS通过门控实现token级选择性干预。EquiSteer在SD-1.5上取得0.051 Δneutral，但基于交叉注意力机制，无法直接迁移至生成式VLM的解码器架构。GGSS的门控机制是否能在非面部token（如衣物、背景）上有效区分偏见信号，论文未提供细粒度token级分析。

## 总结

本文要解决的核心矛盾是生成式VLM推理时去偏中几何保持与偏见消除的冲突。现有方法因欧氏硬投影破坏激活范数、均匀干预忽略token级异质性而失效，GGSS凭借球面线性插值与自适应门控实现选择性去偏。该方法在四个VLM上取得最低平均偏见降低（-55%至-90%），MMStar变化控制在±0.6 p.p.内。其边界在于反事实图像集限于面部特写，且门控超参数需手动校准。当反事实图像集扩展至全身或场景级时，偏见子空间的低维假设是否仍成立，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2608.25375)
# ICLR2026最新论文 ｜Bridging the Gap Between Promise and Performance for Microscaling FP4 Quantization ｜微缩放FP4量化中的旋转悖论与格式特化补偿

作者：Vage Egiazarian、Roberto L. Castro、Denis Kuznedelev 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.23202)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.23202)

> 导读 微缩放FP4格式（MXFP4/NVFP4）旨在通过硬件原生的块级缩放实现4位推理加速，但现有后训练量化（PTQ）方法直接套用整数量化经验时，精度损失远超预期。本文切入点在于揭示Hadamard旋转对两种FP4格式产生相反效果的底层机制，并据此提出格式特化的MR-GPTQ算法与零开销内核。该工作填补了FP4格式精度-性能权衡的系统性研究空白，但其结论局限于PTQ场景，对训练阶段数值稳定性的影响尚存疑。

## 研究背景

理解本文需厘清微缩放格式的核心参数：组大小（Group Size, G）决定共享缩放因子的粒度，缩放因子精度（Scale Representation, S）决定动态范围覆盖能力。MXFP4采用G=32与E8M0缩放（仅指数位，无尾数），NVFP4采用G=16与E4M3缩放（4位指数+3位尾数）。G与S的组合直接决定了量化网格的稀疏程度与死区（Dead-zone）宽度，进而影响重尾分布下的误差分布。

低精度量化领域长期依赖旋转矩阵分散激活值异常值，这一策略在INT8/INT4格式下被验证有效。然而，当量化格式从均匀整数网格转向非均匀浮点网格时，旋转的有效性不再由单一因素决定，而是与格式特有的缩放机制产生耦合。现有PTQ方法如GPTQ、SmoothQuant均假设量化网格特性与格式无关，导致在FP4格式下出现精度崩溃或性能退化。本文针对这一盲区，系统分析了旋转操作与微缩放格式参数（G, S）的交互作用，并据此设计格式特化的量化算法。

## 核心方法

### 方法参照系

本文基于GPTQ的二阶误差补偿框架，但关键差异在于：标准GPTQ假设均匀量化网格，而FP4格式的非均匀网格导致误差补偿方向与幅度发生系统性偏移。

### 旋转对FP4格式的非对称影响

Hadamard旋转（HT）将重尾Laplace分布转化为高斯分布，这一变换对MXFP4与NVFP4产生相反效果。设计动机在于：MXFP4的E8M0缩放因子仅保留指数信息，旋转后的高斯分布方差更集中，降低了缩放因子量化误差；而NVFP4的E4M3缩放因子保留尾数信息，旋转后的高斯分布尾部更厚，反而增加了缩放因子覆盖难度。

$$
\text{MSE}_{\text{rel}}(G) = \mathbb{E}\left[\frac{\sum_{i=1}^G (X_i - \hat{X}_i)^2}{\sum_{i=1}^G X_i^2}\right]
$$

该公式定义了相对均方误差，衡量量化误差相对于原始信号能量的比例。分析表明，当G较小时（如NVFP4的G=16），HT对NVFP4的MSE_rel产生负向影响；当G较大时（如MXFP4的G=32），HT对MXFP4的MSE_rel产生正向影响。这一非对称性源于两种格式缩放因子精度的差异：E8M0的粗粒度缩放对分布集中性敏感，E4M3的细粒度缩放对分布尾部敏感。

### 块级融合旋转与格式特化Scale搜索

MR-GPTQ在GPTQ基础上引入两项关键改进：块级融合Hadamard旋转与格式特化Scale搜索。设计动机在于：标准GPTQ的逐列量化顺序与FP4的块级缩放结构不匹配，导致误差补偿无法充分利用块内相关性。

$$
\hat{W} = \text{RTN}_Q\left(\frac{H W H^\top}{s_{\text{block}}}\right) \cdot s_{\text{block}}
$$

其中$H$为块级Hadamard矩阵，$s_{\text{block}}$为块级缩放因子。该公式表明，MR-GPTQ在量化前对权重块进行双线性旋转，使块内元素分布更均匀，随后使用格式特化的Scale搜索优化$s_{\text{block}}$。对于MXFP4，Scale搜索限制在2的幂次上；对于NVFP4，Scale搜索在E4M3网格上进行。这种格式特化设计确保了缩放因子与量化网格的精确匹配，避免了标准GPTQ中缩放因子与网格不匹配导致的精度损失。

## 实验评估

实验在Llama-3.1-8B-Instruct、Llama-3.3-70B-Instruct及Qwen3系列模型上进行，评估协议为Open LLM Leaderboard V1的Zero-shot任务（GSM8K, MMLU等）。基线覆盖RTN、GPTQ、SmoothQuant、QuaRot、SpinQuant，但缺失2026年SOTA方法如FAAR、ARCQuant，限制了绝对性能定位。

| 模型 | 格式 | 方法 | 准确率恢复率 (%) |
| --- | --- | --- | --- |
| Llama-3.1-8B | NVFP4 | MR-GPTQ | 98-99 |
| Llama-3.1-8B | MXFP4 | MR-GPTQ | 97-98 |
| Llama-3.3-70B | NVFP4 | GPTQ | 98-99 |
| Qwen3-8B | NVFP4 | MR-GPTQ | >99 |

MR-GPTQ在MXFP4上显著优于现有方法，将精度恢复至NVFP4水平（1-2%差距）；在NVFP4上与GPTQ持平，均达到98-99%恢复率。这一结果验证了格式特化设计的必要性：通用方法在MXFP4上失效，而MR-GPTQ通过块级旋转与Scale搜索实现了跨格式的统一优化。

消融实验表明，块级融合旋转是MXFP4精度提升的关键，移除该组件后MXFP4精度下降超过5%；而NVFP4的精度主要依赖Scale搜索优化，旋转的贡献较小。这一发现进一步证实了两种格式对旋转敏感性的差异。

评估边界方面，论文未报告置信区间，数值比较需谨慎；代码未公开，可复现性受限；实验仅覆盖PTQ场景，未验证QAT或训练阶段的效果。

## 关联研究分析

从问题动机看，本文与QuaRot/SpinQuant的旋转策略形成直接对比。QuaRot假设旋转普遍有效，但本文证明在NVFP4+RTN下旋转反而降低精度，这一冲突源于格式参数（G, S）与旋转效果的耦合关系。根源在于：QuaRot的设计基于INT8/INT4的均匀网格假设，而FP4的非均匀网格改变了旋转对误差分布的影响机制。

从方法设计看，本文与GPTQ的二阶补偿框架一致，但引入了格式特化的Scale搜索。这一差异源于FP4格式的缩放因子精度限制：E8M0/E4M3的离散网格要求Scale搜索与量化网格精确匹配，而标准GPTQ的连续Scale优化在FP4下失效。查询侧增强在数据充足时是否仍有增益，论文未给出回答。

## 总结

本文要解决的核心矛盾是FP4微缩放格式下现有PTQ方法的精度崩溃问题。切入点在于揭示旋转操作与格式参数（G, S）的非对称交互，这一发现使格式特化设计成为可能。MR-GPTQ通过块级融合旋转与格式特化Scale搜索，在MXFP4上实现1-2%的精度恢复，在NVFP4上达到98-99%恢复率。边界在于：实验仅覆盖PTQ场景，未验证训练阶段效果；代码未公开，可复现性受限。当支持集增大到5-shot时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.23202)
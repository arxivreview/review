# ACL2026最新论文 ｜CodeRipple: Wavelet-Based Detection of LLM-Generated Code ｜基于小波变换的LLM生成代码检测

作者：Xingyu Yao、Zhendong Mao、Quan Wang

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8f7185986b6b)

> 现有无训练代码检测器依赖全局困惑度统计，在代码语法强约束下失效。CodeRipple指出LLM与人类代码在全局统计收敛时，局部Token Perplexity Sequence (TPS) 动态存在显著差异：前者呈窄瞬态尖峰，后者呈宽持续波动。该方法利用平稳小波变换 (SWT) 建模形态、离散小波变换 (DWT) 量化能量分布，实现无训练检测。其在多基准上显著优于基线，但对高结构化对抗策略及低资源语言泛化能力存疑。

## 研究背景

检测LLM生成代码需区分机器与人类来源，核心信号是代理模型计算的Token Perplexity Sequence (TPS)，即每个token的条件负对数概率。TPS反映模型对上下文的惊讶程度，是判断生成来源的基础。然而，代码具有严格的语法和语义约束，解空间狭窄，导致LLM与人类代码的全局TPS统计量（如均值、方差）高度收敛，传统基于全局统计的检测器（如LogP、DetectGPT）在此场景下判别力丧失。

现有无训练检测方法主要分两类：一类直接复用自然语言检测技术，如Binoculars利用双模型困惑度差异，但代码的结构刚性使其失效；另一类针对代码调整扰动策略，如DetectCodeGPT测量TPS对语法扰动的敏感度，但仍依赖整体敏感度指标，在受限场景下表现不佳。监督式方法虽有效，但依赖标注数据且泛化性差。CodeRipple的切入点在于揭示被忽略的局部动态差异：尽管全局统计收敛，LLM代码的TPS表现为短跨度的瞬态尖峰，而人类代码表现为长跨度的持续波动。这种形态学差异需通过多尺度分析才能捕捉，小波变换因其时频局部化特性成为理想工具。

## 核心方法

### 方法参照系

无训练代码检测的标准流程是：使用代理LLM提取TPS，计算全局统计量（如均值、敏感度），通过阈值分类。CodeRipple的关键差异在于放弃全局聚合，转而分析TPS信号的局部形态与能量分布，利用小波变换的多尺度特性区分瞬态尖峰与持续波动。

### SWT建模TPS形态

SWT分支旨在捕捉TPS的形态特征，解决全局统计无法区分窄尖峰与宽波动的问题。对TPS信号 $s$，在尺度 $\ell$ 下使用膨胀滤波器 $g^{(\ell)}$ 卷积，得到响应序列 $r_\ell$。计算 $r_\ell$ 的样本熵 $SE_\ell(m, \epsilon)$，衡量该尺度下波动的不规则性。多尺度形态得分定义为：

$$ MSWT = \sum_{\ell=1}^{L} \beta_\ell SE_\ell(m, \epsilon) $$

其中 $\beta_\ell$ 为尺度权重。高MSWT值表明波动形态复杂，对应人类代码的宽持续波动；低值对应LLM代码的窄瞬态尖峰。SWT保持序列长度不变，确保不同尺度下形态特征的可比性。

### DWT量化能量扩散

DWT分支量化TPS能量在尺度间的分布，解决形态特征无法反映能量集中程度的问题。对TPS进行L级DWT分解，得到细节系数序列 $D$。计算 $D$ 的峰度（Kurtosis）作为多尺度能量描述符：

$$ MDWT = \frac{\sum_{j=1}^{M} (d_j - \bar{d})^4}{\left( \sum_{j=1}^{M} (d_j - \bar{d})^2 \right)^2 / M} $$

高MDWT值表明能量集中在少数窄尖峰（LLM代码），低值表明能量均匀分布（人类代码）。最终分类得分融合两分支：

$$ Score = MSWT + \alpha MDWT $$

其中 $\alpha$ 平衡两分量。该设计通过形态与能量的互补，克服了单一全局统计在代码约束下的失效。

## 实验评估

实验在AI Code Detection Education、HumanEval和CoDet-M4三个基准上进行，覆盖Python、Java、C++及多种生成LLM。基线包括LogP、GLTR、FastDetectGPT、Binoculars、DetectCodeGPT等无训练方法，以及PHD和CodeLength启发式基线。CodeRipple在AI Code Detection Education上平均AUROC达0.858，显著优于次优的FastDetectGPT（0.774）和Binoculars（0.740）。在HumanEval上，CodeRipple平均AUROC为0.764，优于DetectCodeGPT（0.650）和Binoculars（0.567）。

| 方法 | AI Code Detection Education (AVG) | HumanEval (AVG) | CoDet-M4 (Python) |
|---|---|---|---|
| LogP | 0.680 | 0.583 | 0.544 |
| FastDetectGPT | 0.774 | 0.572 | 0.645 |
| Binoculars | 0.740 | 0.567 | 0.603 |
| DetectCodeGPT | 0.594 | 0.650 | 0.556 |
| CodeRipple | 0.858 | 0.764 | 0.828 |

消融实验显示，移除SWT分支导致平均AUROC下降0.030，移除DWT分支下降0.020，表明两分支提供互补信号。将SWT替换为原始TPS样本熵，AUROC下降0.111，证实小波变换对形态建模的必要性。将DWT替换为原始TPS峰度，AUROC下降0.048，验证能量分布分析的贡献。在13种对抗策略中，CodeRipple在8种策略下排名第一，但在策略5-7（生成断言、测试用例）下表现不佳，因这些策略产生高度结构化代码，抑制TPS自然波动，削弱小波特征的判别力。

评估边界方面，CodeRipple依赖CodeLlama-7B作为代理模型，未测试更大规模或不同架构的代理模型。超参数（如小波类型、分解层级）对性能影响较小，但权重 $\alpha$ 和 $\beta_\ell$ 需针对数据集调整。代码已开源，但实验仅报告单次运行结果，未提供置信区间。

## 关联研究分析

从问题动机看，CodeRipple与DetectCodeGPT均针对代码检测，但前者聚焦局部动态，后者依赖全局敏感度。DetectCodeGPT通过语法扰动测量TPS变化，假设LLM代码对扰动更敏感，但代码语法约束使扰动效果有限。CodeRipple揭示的局部形态差异是更本质的特征，不受扰动策略影响，这解释了其在多数对抗策略下的优势。然而，CodeRipple在高度结构化策略下的失效，暗示其依赖TPS自然波动，当代码结构被强制约束时，局部动态差异可能消失。

从方法设计看，CodeRipple与Binoculars同属无训练范式，但Binoculars利用双模型困惑度差异，CodeRipple利用单模型TPS的小波特征。Binoculars在策略5-7下优于CodeRipple，因其跨模型差异不受单模型内部波动抑制。这提示，结合多模型困惑度差异与小波形态特征，可能提升在结构化代码下的检测鲁棒性。CodeRipple未探索多模型融合，其单模型依赖是潜在局限。

## 总结

CodeRipple解决的核心矛盾是代码语法约束导致全局TPS统计收敛，使传统无训练检测器失效。其切入点在于揭示LLM与人类代码在局部TPS动态上的形态差异：窄瞬态尖峰 vs 宽持续波动。通过SWT建模形态、DWT量化能量分布，CodeRipple在AI Code Detection Education上达到0.858 AUROC，在HumanEval上达到0.764 AUROC，显著优于现有无训练方法。其边界在于对高度结构化对抗策略（如生成测试用例）的鲁棒性不足，且依赖单代理模型。当代码结构被强制约束至抑制TPS自然波动时，小波特征的判别力是否完全丧失，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_8f7185986b6b)
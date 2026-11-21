# ACL2026最新论文 ｜Exons-Detect: Identifying and Amplifying Exonic Tokens via Hidden-State Discrepancy for Robust AI-Generated Text Detection ｜外显子感知重加权检测

作者：Xiaowei Zhu、Yubing Ren、Fang Fang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_bba32cf5c3e2)

> 训练-free AI生成文本检测在短序列与局部改写攻击下，因均匀聚合token信号导致判别力稀释。现有方法如Binoculars假设所有token贡献均等，无法区分携带来源信号的关键token与噪声token。Exons-Detect通过双模型隐藏状态差异识别“外显子token”并非线性放大其权重，重构翻译分数以增强鲁棒性。该方法在DetectRL上取得92.14%平均AUROC，但依赖双模型前向传播且未验证隐藏状态差异与来源信号的因果关联。

## 研究背景

当检测器面对新生成模型或经过改写的文本时，其训练域与测试域的数据分布出现系统性差异——这一现象称为分布偏移。分布偏移导致传统监督分类器决策边界失效，而实际场景中往往能获取少量目标域样本，这恰好构成了小样本学习的条件：仅凭每个类别极少量标注样本泛化到新任务。解决此类问题的经典框架是原型网络，它计算各类别支持样本的特征均值作为"原型"，再通过距离度量完成分类。

AI生成文本检测的核心矛盾在于：生成模型能力指数级提升导致人机文本分布边界日益模糊，而现有检测器在跨域泛化与对抗鲁棒性上存在严重缺陷。主流路线分为训练式与训练-free两类：训练式方法（如BiScope）依赖大规模标注数据，在分布偏移下性能急剧下降；训练-free方法（如Binoculars）通过代理LLM计算统计分数，但均匀聚合token信号导致短文本或局部修改时判别力稀释。Exons-Detect的切入点在于：不同token对检测的贡献并非均等，携带来源信号的关键token（外显子）应被放大，而噪声token（内含子）应被抑制。

## 核心方法

### 双模型特征提取与翻译分数框架

训练-free检测的标准流程是：输入序列经代理LLM计算token级生成概率，聚合为全局分数（如Log-PPL/Cross-PPL比率）。本文问题与该通用流程的关键差异在于：均匀聚合假设所有token贡献相等，但实际中仅部分token携带强来源信号。Exons-Detect继承Binoculars的翻译分数框架，但引入双模型（M和M̃）的隐藏状态差异作为token重要性度量，打破均匀聚合假设。

### 外显子识别与非线性重加权

在双模型特征提取后，本文计算每个token位置t的隐藏状态差异δt，定义为所有L层余弦距离的均值：

$$\delta_t = \frac{1}{L} \sum_{l=1}^{L} (1 - \cos(h_t^{(l)}, \tilde{h}_t^{(l)}))$$

该公式量化了token在两个模型表示空间中的偏离程度。设计动机：Binoculars等方法的均匀聚合在短文本或局部改写时，关键token的信号被大量噪声token稀释，导致判别力下降。本文通过阈值θ识别外显子token（δt > θ），并用非线性映射g(δt) = 1 - exp(-α(δt - θ)⁺)生成额外权重Δwt，其中(·)⁺为正部算子。最终权重wt = (1 + Δwt) / Σᵢ(1 + Δwᵢ)，归一化后用于计算加权Log-PPL与加权Cross-PPL。这一设计通过放大外显子token的贡献，使检测分数更敏感于来源相关信号，抑制局部修改对全局分数的干扰。

### 突变修复机制集成

在翻译分数计算中，本文集成DNA-DetectLLM的突变修复机制：构造理想AI序列ŝ（每个位置取最大概率token），计算加权Log-PPL(ŝ)并加入初始翻译分数：

$$R(s) = \frac{\log PPL_W^M(s) + \log PPL_W^M(\hat{s})}{\log X\text{-}PPL_W^{M,\tilde{M}}(s)}$$

该公式通过量化输入序列与理想AI序列的修复难度，捕捉内在判别差异。设计动机：仅依赖原始序列的翻译分数在对抗攻击下易被绕过，突变修复机制通过引入“理想AI”参照，增强了分数对来源信号的敏感性。修复过程在外显子权重下进行，确保关键token的修复难度被优先考量。

## 实验评估

实验在M4、DetectRL（Multi-LLM/Multi-Domain）、RealDet三个基准上进行，基线覆盖训练式（OpenAI-D, BiScope, R-Detect）与训练-free（Likelihood, DetectGPT, Binoculars, DNA-DetectLLM等）路线，但缺失水印类基线（因任务不同）。主结果显示：

| 方法 | M4 AUROC | DetectRL Multi-LLM AUROC | DetectRL Multi-Domain AUROC | RealDet AUROC | Avg. AUROC |
| :--- | :--- | :--- | :--- | :--- | :--- |
| DNA-DetectLLM | 91.74 | 88.97 | 88.23 | 94.48 | 90.86 |
| Exons-Detect | 92.43 | 90.67 | 90.46 | 94.98 | 92.14 |

Exons-Detect在DetectRL Multi-LLM上超越DNA-DetectLLM 1.9%，在Multi-Domain上超越2.5%，是唯一在所有数据集AUROC超过90%的方法。消融实验表明：移除非线性映射g(·)导致平均AUROC下降1.0%，移除突变修复机制导致下降4.4%，证明两者均为必要组件。超参数敏感性分析显示，使用32层隐藏状态时性能最优，减少至4层导致DetectRL AUROC相对下降1.9%-3.1%。

评估边界与可复现性：指标仅包含AUROC与F1，未报告置信区间；评估协议未包含计算效率的量化对比（仅定性描述<0.8s）；代码开源（https://github.com/Xiaoweizhu57/Exons-Detect），超参数θ=0.15, α=10，代理模型标准化为Falcon-7B-Instruct/Falcon-7B，确保了公平比较。

## 关联研究分析

从问题动机看，Exons-Detect与Binoculars同属训练-free路线，但Binoculars假设token贡献均等，而Exons-Detect通过隐藏状态差异区分外显子/内含子。这一差异的根源在于：Binoculars的均匀聚合在长文本中可能足够，但在短文本或局部改写时，关键token的信号被稀释；Exons-Detect的重加权机制直接针对这一失效场景。然而，隐藏状态差异是否真正捕捉了来源信号，还是仅反映了模型间分布偏差，论文未提供因果验证。

从方法设计看，Exons-Detect与DNA-DetectLLM同框架，但DNA-DetectLLM的突变修复机制未考虑token重要性差异，而Exons-Detect在外显子权重下进行修复。这一改进的根源在于：突变修复机制本身是全局操作，若关键token的修复难度被噪声token平均，则判别力下降；Exons-Detect通过重加权确保关键token的修复难度被优先考量。但双模型前向传播的计算开销是否在实际部署中可接受，论文未提供大规模效率测试。

## 总结

Exons-Detect要解决的核心矛盾是训练-free检测在短序列与局部改写下的判别力稀释问题。现有方法如Binoculars因均匀聚合token信号，无法区分携带来源信号的关键token与噪声token；Exons-Detect通过双模型隐藏状态差异识别外显子token并非线性放大其权重，重构翻译分数以增强鲁棒性。实验证明其在DetectRL上取得92.14%平均AUROC，超越最强基线DNA-DetectLLM 1.4%。本文的边界在于：依赖双模型前向传播，计算开销高于单模型方法；隐藏状态差异与来源信号的因果关联未验证。当代理模型对特定领域文本的表示偏差较大时，外显子识别的可靠性是否下降，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_bba32cf5c3e2)
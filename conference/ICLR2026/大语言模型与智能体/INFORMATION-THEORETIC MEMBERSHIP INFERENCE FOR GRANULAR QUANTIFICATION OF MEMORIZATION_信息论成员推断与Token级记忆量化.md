# ICLR2026最新论文 ｜INFORMATION-THEORETIC MEMBERSHIP INFERENCE FOR GRANULAR QUANTIFICATION OF MEMORIZATION ｜信息论成员推断与Token级记忆量化

研究机构：新加坡国立大学、谷歌研究院

作者：Jiashu Tao、Reza Shokri

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_27263415)

> 成员推断攻击（MIA）旨在量化模型对训练数据的记忆程度，但现有标准方法鲁棒成员推断攻击（RMIA）依赖大规模种群数据且输出离散信号，难以适配大语言模型（LLM）的评估需求。本文指出序列级MIA将Token级信号压缩为单一比特，掩盖了隐私泄露的局部性，导致评估失真。通过构建基于贝叶斯因子的连续统计量InfoRMIA，并引入Token级细粒度评估框架，实现了更低成本、更高精度的隐私审计。该工作确立了新的SOTA基线，但其在预训练模型上的绝对性能提升有限，且Token级定位的泛化性尚待验证。

## 研究背景

当审计人员试图判断某条文本是否被LLM记忆时，传统MIA将整条序列视为一个整体进行二元判断。这种序列级聚合忽略了Transformer自回归生成的逐Token特性，导致包含敏感信息的短序列因大量非敏感Token的稀释而得分偏低。为了解决这一粒度失真问题，需要一种能直接作用于单个Token预测步骤的评估机制，同时保持统计推断的严谨性。

MIA作为ML隐私研究的核心范式，其SOTA方法RMIA通过计数目标样本在种群数据中的支配比例来构建离散评分。然而，RMIA的评分精度受限于种群数据集 $Z$ 的规模，且其离散特性导致在LLM这种高维数据空间中存在显著的量化误差。随着LLM训练数据规模扩大，获取与训练集线性相关的种群数据变得不切实际，迫使研究者寻找不依赖大规模 $Z$ 的替代方案。

本文切入点在于将RMIA的假设检验框架重构为信息论问题。通过引入连续的对数似然比统计量，消除对 $Z$ 规模的线性依赖，并进一步将评估粒度从序列下沉至Token，从而在降低计算开销的同时，揭示序列级MIA所掩盖的局部记忆模式。

## 核心方法

### 方法参照系

本文问题属于基于参考模型的MIA统计推断路线。标准流程是训练参考模型集，计算目标样本在参考模型上的信号分布，并通过假设检验区分成员与非成员。本文的关键差异在于，不再使用离散的比例计数，而是采用连续的信息增益度量，并将评估单元从序列缩小至Token。

### 信息论统计量重构

RMIA的原始统计量通过计算目标 $x$ 支配的种群样本 $z$ 的比例来构建，其粒度由 $|Z|$ 决定，且需引入阈值超参数 $\gamma$。本文将其转化为复合假设检验问题，利用贝叶斯因子计算目标模型相对于种群数据的期望对数似然比。

$$
\text{Score}_{\text{InfoRMIA}} = \log p(x|\theta) - \log p(x) - D_{KL}(p(z) || p(z|\theta))
$$

该公式第一项衡量模型 $\theta$ 对 $x$ 的信息增益（即记忆程度），第二项通过KL散度量化模型对种群数据分布的偏移。这一设计消除了离散计数的量化误差，使评分精度不再受 $|Z|$ 限制，同时去除了 $\gamma$ 超参数，显著降低了计算复杂度。

### Token级细粒度评估框架

序列级MIA将整条序列的Token信号聚合为单一比特，导致敏感Token（如PII）的记忆信号被非敏感Token稀释。本文提出Token级MIA框架，将InfoRMIA应用于每个Token的预测步骤，生成Token级记忆热力图。

$$
S_t = \log p(x_t|x_{<t}, \theta) - \log p(x_t|x_{<t}) - D_{KL}(p(z_t) || p(z_t|\theta))
$$

其中 $S_t$ 为第 $t$ 个Token的成员推断得分。该框架通过定位高得分Token，实现隐私泄露的微观定位。实验表明，序列级高分序列往往主要记忆非敏感Token，而敏感信息集中在少数高得分Token中，这为精准遗忘（Targeted Unlearning）提供了直接依据。

## 实验评估

| 数据集 | 方法 | AUC | TPR@0.1%FPR |
|---|---|---|---|
| AG News | RMIA | 0.8574 | 0.00% |
| AG News | InfoRMIA | 0.8784 | 12.0% |
| CIFAR-10 | RMIA | 0.8229 | 0.00% |
| CIFAR-10 | InfoRMIA | 0.8330 | 5.82% |
| Purchase100 | RMIA | 0.5311 | 0.00% |
| Purchase100 | InfoRMIA | 0.5754 | 0.32% |

实验在AG News、CIFAR-10、Purchase100及MIMIR基准上进行，基线覆盖RMIA、LiRA、Min-K%++等主流方法。InfoRMIA在低FPR区间表现显著优于RMIA，例如在AG News上TPR@0.1%FPR从0.00%提升至12.0%，AUC从0.8574提升至0.8784。在MIMIR基准的Pythia模型上，InfoRMIA的AUC与最强基线Min-K%++持平或略优，但在TPR@1%FPR指标上普遍领先，验证了其在低误报率场景下的优势。

消融实验显示，使用更晚的参考模型检查点（如Step 100k）会导致InfoRMIA性能下降，证实参考模型需尽可能“OUT”（未见过目标数据）以维持攻击有效性。Token级评估在ai4privacy数据集上揭示，私人Token的平均得分（0.076426）低于非私人Token（0.090224），但高得分Token中私人Token占比更高，表明序列级平均得分确实掩盖了局部隐私风险。

评估边界方面，论文未报告置信区间，且MIMIR基准上预训练模型的AUC提升幅度有限（如Pythia-6.9B在HackerNews上InfoRMIA2 AUC为54.6，与Min-K%++的54.6持平），暗示在大规模预训练数据上，信息论改进的边际收益可能递减。代码已开源，但超参数配置依赖ML Privacy Meter库，复现需遵循特定配置。

## 关联研究分析

从问题动机看，本文与Scalable Extraction（Nasr et al., 2023）均关注LLM隐私风险，但前者聚焦黑盒提取攻击的效率，本文则聚焦白盒/灰盒审计的统计精度。Scalable Extraction通过散度攻击实现吉字节级数据提取，而InfoRMIA通过连续统计量提升成员推断的区分度。差异根源在于任务目标不同：提取攻击旨在恢复数据，而MIA旨在量化风险。本文的Token级框架为提取攻击提供了更精细的目标定位，但两者在计算开销上存在权衡，InfoRMIA需训练参考模型，而Scalable Extraction仅需黑盒查询。

从方法设计看，本文与MoPe（P35）同属白盒攻击路线，但MoPe基于参数扰动测量Hessian迹，本文基于似然比计算信息增益。MoPe无需参考模型，但计算开销大且依赖白盒访问；InfoRMIA需参考模型，但计算效率更高且适用于灰盒场景。差异根源在于信号来源：MoPe利用模型内部几何结构，InfoRMIA利用模型输出分布。在LLM上，MoPe的0.70 TPR@5%FPR（MIMIC数据集）与InfoRMIA在MIMIR上的表现难以直接对比，但InfoRMIA的连续统计量可能更适合高维文本数据，而MoPe的参数扰动在大规模模型上可能面临数值稳定性问题。

## 总结

本文核心矛盾在于序列级MIA的粒度失真与RMIA对大规模种群数据的依赖。通过信息论重构统计量并引入Token级评估，InfoRMIA在低FPR区间显著优于SOTA，例如AG News上TPR@0.1%FPR达12.0%。然而，在MIMIR基准的预训练模型上，其AUC提升有限，且Token级定位的有效性仅在微调模型上得到充分验证。当预训练数据规模进一步扩大时，信息论统计量的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_27263415)
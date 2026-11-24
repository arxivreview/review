# CVPR2026最新论文 ｜RankOOD -- Class Ranking-based Out-of-Distribution Detection ｜基于排序一致性的分布外检测

研究机构：澳大利亚悉尼大学

作者：Dishanika Denipitiyage、Naveen Karunanayake、Suranga Seneviratne 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.19996)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.19996)

> 分布外检测旨在识别模型训练分布之外的样本，以消除其对未见数据的高置信度错误预测。传统后验评分依赖概率值或能量，在语义近邻样本上因特征重叠而失效；现有排序方法如CRAFT需修改架构或忽略相对顺序。RankOOD通过整数线性规划提取规范排序，并利用Plackett-Luce模型下的ListMLE损失重塑Logit层级结构，实现无需外部异常数据的鲁棒检测。该方法在TinyImageNet近邻检测中取得SOTA，但远端检测性能仍落后于视觉语言模型路线，其排序信号在极端分布偏移下的泛化能力存疑。

## 研究背景

当分类器面对未见类别时，其Logit输出往往呈现高置信度但错误的排序结构。这种过度自信源于交叉熵损失仅优化Top-1预测，未约束其余类别Logit的相对顺序。为量化这种顺序的稳定性，研究者引入Rank Probability Matrix (RPM)，记录各类别在正确预测样本中占据不同排名位置的概率分布。然而，RPM仅反映统计频率，无法直接作为检测信号，需转化为可优化的训练目标。

现有OOD检测分为后验评分与训练时正则化两类。后验方法如MSP和Energy Score依赖输出层统计量，在近邻OOD（Near-OOD）场景下因ID与OOD特征空间重叠而区分度不足。训练时方法如Outlier Exposure (OE) 通过引入外部异常数据塑造边界，但依赖辅助数据且可能过拟合。近期工作如CRAFT尝试利用排序信息，但需微调预训练模型并忽略类间相对顺序。RankOOD的切入点在于：不依赖外部数据，不修改架构，而是通过强化Logit的列表级一致性来区分ID与OOD，将排序结构内化为模型属性。

## 核心方法

### 方法参照系

本文问题属于“无外部异常数据的训练时正则化”范畴。标准流程是通过修改损失函数或引入辅助任务优化特征空间，但传统方法仅关注Top-1置信度或范数，未利用Logit向量内部的排序结构。本文的关键差异在于将排序一致性作为显式优化目标，而非后验分析对象。

### 规范排序提取

在训练前，需从预训练模型中获取每个类别的规范排序（Canonical Rank）。通常做法是直接使用RPM的众数，但RPM在高维类别空间中噪声大且存在并列。本文通过求解0-1整数线性规划（ILP）问题，最大化联合分配概率，确保每个排名位置仅分配一个类别，且每个类别仅出现一次。该步骤解决了RPM噪声导致的排序模糊问题，为后续训练提供了无歧义的监督信号。

$$
\max \sum_{i=1}^{C} \sum_{j=1}^{K} p_{ij}^{[c]} x_{ij} \quad \text{s.t.} \quad \sum_{i=1}^{C} x_{ij} = 1, \sum_{j=1}^{K} x_{ij} = 1
$$

该公式通过二元变量 $x_{ij}$ 选择最优排列，其中 $p_{ij}^{[c]}$ 为类别 $c$ 下类别 $i$ 出现在排名 $j$ 的概率，约束条件保证排列的合法性。

### 列表级排序学习

在获得规范排序后，训练阶段需优化Logit以匹配该排序。传统交叉熵损失仅约束Top-1，ListMLE则基于Plackett-Luce模型，对完整排列赋予概率并最大化似然。本文采用混合损失，结合交叉熵与ListMLE，以平衡Top-1准确性与全列表一致性。

$$
\mathcal{L}_{total} = \alpha \mathcal{L}_{CE} + (1-\alpha) \mathcal{L}_{ListMLE}
$$

其中 $\mathcal{L}_{ListMLE}$ 定义为 $-\log \prod_{i=0}^{K-1} \frac{\exp(l_{\pi_i})}{\sum_{j=i}^{K-1} \exp(l_{\pi_j})}$。该设计动机在于：OOD样本虽可能获得高Top-1 Logit，但其Logit序列难以维持ID样本特有的单调衰减结构。通过强化这种结构，ID样本的Logit分布更紧凑，OOD样本则因排序混乱而偏离参考阈值，从而提升检测灵敏度。

## 实验评估

实验在CIFAR-10/100和TinyImageNet上进行，对比34种基线，覆盖后验、无异常训练及有异常训练三类方法。遗漏了扩散模型（如SCOPED）和VLM（如ANTS）等最新路线，导致远端OOD对比不完整。

| 方法 | TinyImageNet Near-OOD AUROC | TinyImageNet Near-OOD FPR95 | CIFAR-100 Far-OOD AUROC | CIFAR-100 Far-OOD FPR95 |
| :--- | :--- | :--- | :--- | :--- |
| RankOOD | 85.30 ± 0.18 | 50.05 ± 0.16 | 83.63 ± 1.06 | 47.44 ± 0.80 |
| OE | 84.84 ± 0.16 | 52.30 ± 0.67 | 81.41 ± 1.49 | 54.82 ± 2.79 |
| G-ODIN | 77.28 ± 0.10 | 69.87 ± 0.46 | 85.67 ± 1.58 | 42.68 ± 3.19 |
| LogitNorm | 82.66 ± 0.15 | 56.46 ± 0.37 | 93.04 ± 0.21 | 26.11 ± 0.52 |

RankOOD在TinyImageNet近邻检测中FPR95为50.05%，优于OE的52.30%，验证了排序信号在近邻场景的有效性。但在CIFAR-100远端检测中，其AUROC 83.63%低于LogitNorm的93.04%，表明排序信号在远端语义偏移下信息量不足，可能因远端样本Logit分布过于离散，排序结构不再具有区分性。

消融实验显示，使用Top-10和Bottom-10排名（N=20）时性能最佳，仅用Top排名导致ID准确率下降，因缺乏语义差异大的类别约束。$\alpha$ 参数在CIFAR-100上取1.0时AUROC最高，说明ListMLE权重需随类别数调整。Logit阈值Ref在0.95时性能峰值，过高则导致低排名Logit偏差被过度惩罚。

评估协议基于OpenOOD基准，使用ResNet-18骨干，报告三次运行均值。未提供代码链接，ILP求解复杂度未详细披露，可能限制其在ImageNet-1K等大规模类别上的可扩展性。

## 关联研究分析

从方法设计看，RankOOD与CRAFT均利用排序信息，但CRAFT将排序建模为2D PMF矩阵并需微调架构，而RankOOD通过ListMLE在标准骨干上优化Logit层级，避免了架构修改。这一差异源于CRAFT关注类间概率分布的静态建模，而RankOOD关注Logit动态生成的序列一致性。CRAFT忽略相对顺序，导致其在近邻检测中不如RankOOD，但CRAFT在远端检测中表现更稳定，可能因其PMF建模对极端偏移更具鲁棒性。

从问题动机看，RankOOD与LogitNorm同属无异常数据训练方法，但LogitNorm约束Logit范数以防止过度自信，RankOOD约束Logit排序以增强结构一致性。LogitNorm在远端OOD中表现优异（AUROC 93.04%），而RankOOD在近邻OOD中更优。这暗示范数约束对远端样本的“低置信度”需求更有效，而排序约束对近邻样本的“结构相似性”需求更敏感。两者互补，但论文未探索联合使用范数与排序约束的可能性，这可能是在复杂分布下提升检测鲁棒性的潜在方向。

## 总结

RankOOD旨在解决近邻OOD检测中传统后验评分失效的问题，通过强化Logit排序一致性实现无外部数据的鲁棒检测。其核心在于利用ILP提取规范排序，并以ListMLE损失重塑Logit层级，使ID样本的Logit序列呈现单调衰减，而OOD样本因排序混乱而偏离参考阈值。实验证明其在TinyImageNet近邻检测中FPR95达50.05%，优于OE，但在CIFAR-100远端检测中AUROC仅83.63%，低于LogitNorm。这一局限暴露了排序信号在远端语义偏移下的信息不足，可能因远端样本Logit分布过于离散，排序结构失去区分性。当类别数增至ImageNet-1K规模时，ILP求解的复杂度与排序信号的稀疏性是否会导致检测性能显著下降，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.19996)
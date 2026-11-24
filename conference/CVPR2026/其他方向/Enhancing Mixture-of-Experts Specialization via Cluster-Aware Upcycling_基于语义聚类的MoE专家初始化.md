# CVPR2026最新论文 ｜Enhancing Mixture-of-Experts Specialization via Cluster-Aware Upcycling ｜基于语义聚类的MoE专家初始化

研究机构：LG AI研究院、美国密歇根大学

作者：Sanghyeok Chu、Pyunghwan Ahn、Gwangmo Song 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.13508)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.13508)

> 混合专家模型（Mixture-of-Experts, MoE）通过稀疏激活解耦参数量与计算成本，但将预训练稠密模型转化为MoE时，复制权重导致的专家对称性阻碍了早期专业化。现有Upcycling方法依赖噪声或随机初始化，无法利用稠密模型中已存在的语义结构。本文提出Cluster-aware Upcycling，利用激活空间的球形k-means聚类初始化专家子空间与路由器，并引入专家集成自蒸馏损失稳定训练。该方法在CLIP视觉基准上验证了结构化初始化对零样本与少样本泛化的提升，但其收益是否源于初始化本身还是后续训练动态，仍需更严格的消融验证。

## 研究背景

MoE架构的核心在于路由机制 $g(x)$ 从 $N$ 个专家中选择 $K$ 个进行计算，输出为 $y = \sum_{i \in g(x)} \tilde{g}_i(x) E_i(x)$。这一机制要求专家具备差异性以捕捉不同输入特征，但初始化阶段的专家权重若完全相同，路由决策将缺乏语义依据，导致所有专家处理相似的Token，形成功能重叠。

将预训练稠密模型转化为MoE的Sparse Upcycling策略通过复制FFN权重实现热启动，但随机初始化的路由器与对称的专家权重构成了早期训练的死锁。Drop-Upcycling通过部分重初始化打破对称性，却破坏了预训练表示空间；DeRS-LM采用共享基与低秩残差表示，虽降低冗余但缺乏对输入分布的感知。这些方法均未利用稠密模型激活中隐含的语义结构，导致专家专业化依赖漫长的训练过程，收敛效率受限。

本文切入点在于识别稠密模型激活流形中的语义簇，将其作为专家初始化的先验。通过球形k-means聚类对齐路由器的余弦相似度计算机制，使专家在训练初期即具备语义分工，从而在保持预训练知识的同时加速专业化进程。

## 核心方法

### 方法参照系

标准MoE Upcycling流程将稠密FFN权重复制至所有专家，路由器随机初始化。本文的关键差异在于：利用稠密模型输入激活的语义结构，分别初始化专家权重与路由器参数，打破专家对称性。

### 语义聚类与专家子空间初始化

传统Upcycling中专家权重相同，导致路由缺乏依据。本文首先对稠密模型FFN输入激活 $\mathbf{X}$ 进行球形k-means聚类，目标函数为：

$$ \min_{\{\mathbf{\mu}_i\}} \sum_{i=1}^{N_e} \sum_{\mathbf{x}_j \in \mathbf{X}_i} \|\mathbf{x}_j - \mathbf{\mu}_i\|_2^2 $$

其中 $\mathbf{\mu}_i$ 为第 $i$ 个簇质心。该聚类基于余弦相似度，与路由器logit计算 $\mathbf{W}_r \mathbf{x}$ 的方向对齐机制一致。随后，通过数据感知截断SVD初始化专家权重。对每个簇 $\mathbf{X}_i$，计算白化矩阵 $\mathbf{S}_i$ 满足 $\mathbf{S}_i \mathbf{S}_i^T = \mathbf{X}_i \mathbf{X}_i^T$，并对 $\mathbf{W}_i \mathbf{S}_i$ 进行截断SVD，保留前 $r_i$ 个奇异方向，其中 $r_i$ 为保留至少 $\tau=0.95$ 谱能量的最小秩。这一设计确保专家权重捕捉其对应簇的主子空间，而非仅依赖权重矩阵本身的统计特性，从而在初始化阶段即建立专家与语义簇的映射关系。

### 路由器初始化与EESD损失

专家初始化后，路由器需与专家子空间对齐。本文使用 $\ell_2$ 归一化的簇质心初始化路由器权重 $\mathbf{W}_r$，使早期路由决策直接反映数据语义结构。然而，训练初期仍存在路由概率接近均匀的不确定Token，阻碍专家专业化巩固。为此，引入专家集成自蒸馏（EESD）损失：

$$ \mathcal{L}_{EESD} = \frac{1}{T} \sum_{t=1}^{T} \left\| \text{sg}(y_{ema}) - y_{moe} \right\|_2^2 $$

其中 $y_{ema}$ 为EMA教师模型（激活所有专家）的输出，$y_{moe}$ 为稀疏MoE模型（Top-2路由）的输出，$\text{sg}(\cdot)$ 为停止梯度算子。EMA教师提供稳定的集成级监督，当路由不确定时，损失值较大，引导模型向集成预测靠拢；当路由置信度高时，损失值小，不干扰专家专业化。该损失与任务损失、负载均衡损失共同构成总目标：$\mathcal{L}_{total} = \mathcal{L}_{task} + \lambda_{lb}\mathcal{L}_{lb} + \lambda_{EESD}\mathcal{L}_{EESD}$。

## 实验评估

实验基于CLIP ViT-B/32与ViT-B/16，在LAION-400M上训练，对比Sparse Upcycling、Drop-Upcycling、DeRS-LM与CLIP-MoE。所有方法使用相同的MoE配置（8专家、Top-2路由）与训练协议，确保公平比较。

| 模型架构 | MoE初始化 | MSCOCO I→T | MSCOCO T→I | ImageNet-1k Val | VTAB Natural |
|---|---|---|---|---|---|
| ViT-B/32 | Dense | 34.0 | 49.6 | 41.9 | 52.4 |
| ViT-B/32 | Sparse Upcycling | 38.1 | 56.0 | 47.7 | 58.3 |
| ViT-B/32 | Cluster-aware | 38.2 | 56.6 | 48.1 | 59.1 |
| ViT-B/16 | Dense | 40.8 | 59.4 | 51.7 | 58.1 |
| ViT-B/16 | Sparse Upcycling | 42.7 | 62.0 | 54.5 | 62.6 |
| ViT-B/16 | Cluster-aware | 43.5 | 63.2 | 55.1 | 63.3 |

Cluster-aware Upcycling在ViT-B/32与ViT-B/16上均优于Sparse Upcycling，尤其在VTAB Natural上提升0.8与0.7个百分点，表明结构化初始化增强了分布外泛化能力。

| 模型架构 | 聚类初始化 | EESD | MSCOCO I→T | ImageNet-1k 10-shot |
|---|---|---|---|---|
| ViT-B/16 | ✓ | ✗ | 35.1 | 57.8 |
| ViT-B/16 | ✗ | ✓ | 34.6 | 58.1 |
| ViT-B/16 | ✓ | ✓ | 35.4 | 58.2 |

消融实验显示，聚类初始化单独提供一致提升，而EESD单独效果微弱且无一致趋势。两者结合时，EESD在聚类初始化基础上进一步增益，表明其作用依赖于初始化建立的专家专业化基础，而非独立有效。

评估协议覆盖零样本检索、分类与少样本微调，但缺乏对路由动态性的细粒度分析。代码未公开，超参数（如EMA系数 $\beta=0.999$、$\lambda_{EESD}$ 随模型规模变化）未提供敏感性分析，可复现性受限。

## 关联研究分析

从问题动机看，本文与DeRS-LM均针对专家冗余，但DeRS-LM通过共享基与低秩残差降低参数冗余，未考虑输入分布；本文通过数据感知SVD将输入统计纳入专家初始化，使冗余消除与语义对齐同步进行。这一差异源于任务特性：视觉对比学习中，激活方向与语义类别强相关，而LLM中Token分布更复杂，数据感知SVD的适用性需进一步验证。

从方法设计看，本文与Switch Transformer的路由机制类似（Top-K），但Switch Transformer依赖训练过程中的负载均衡损失实现专业化，而本文通过初始化先验加速这一过程。EESD损失与集成学习思想相关，但本文将其应用于MoE路由不确定性场景，而非模型集成。查询侧增强在数据充足时是否仍有增益，论文未给出回答。

## 总结

本文解决的核心矛盾是MoE Upcycling中专家对称性与预训练知识保留的冲突。现有方法通过噪声或重初始化打破对称性，但破坏了预训练表示；本文利用稠密模型激活的语义结构，通过球形k-means聚类与数据感知SVD初始化专家子空间，用簇质心初始化路由器，在保持预训练知识的同时建立早期专业化基础。实验证明，该方法在CLIP ViT-B/16上ImageNet 10-shot准确率58.2%，优于Sparse Upcycling的57.8%；VTAB Natural提升0.7个百分点。其边界在于EESD单独效果微弱，且数据感知SVD仅应用于FFN第一层，后续层语义对齐失效。当支持集增大到5-shot时，聚类初始化的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.13508)
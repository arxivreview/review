# CVPR2026最新论文 ｜ConeSep: Cone-based Robust Noise-Unlearning Compositional Network for Composed Image Retrieval ｜基于锥空间几何的噪声三元组遗忘网络

研究机构：山东大学、哈尔滨工业大学

作者：Zixu Li、Yupeng Hu、Zhiwei Chen 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.20358)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.20358)

> 组合图像检索（Composed Image Retrieval, CIR）在真实数据中常面临标注噪声，尤其是参考图与目标图视觉高度相似但修改文本错误的“硬噪声”，这违背了传统噪声学习依赖的“小损失假设”。现有方法多采用粗粒度损失或伪标签修正，难以区分此类噪声且缺乏明确的负向语义锚点，导致修正过程可能损伤邻近干净样本。本文提出ConeSep，通过几何保真量化、负边界学习与基于最优传输的目标遗忘，构建闭环鲁棒训练框架。该方法在FashionIQ上取得64.97%的平均R@10，但在CIRR的R@1指标上略低于部分基线，其泛化边界尚需进一步验证。

## 研究背景

CIR任务要求模型根据参考图像 $I_{ref}$ 和修改文本 $T_{mod}$ 检索目标图像 $I_{target}$。在实际大规模数据集中，人工标注的主观偏差或大语言模型（Large Language Model, LLM）生成的幻觉会导致三元组 $(I_{ref}, T_{mod}, I_{target})$ 出现语义不一致，即噪声三元组对应（Noisy Triplet Correspondence, NTC）。NTC包含部分匹配与硬噪声两种形态，其中硬噪声因参考图与目标图视觉相似度高，导致模型计算出的损失值较小，从而被传统基于“小损失假设”的噪声识别方法误判为干净样本。

主流噪声对应学习（Noisy Correspondence Learning, NCL）方法遵循“识别-修正/抑制”范式，依赖混合损失或结构相似度划分数据，再通过伪标签修正或鲁棒损失函数抑制噪声。然而，这种粗粒度标量度量无法捕捉CIR中视觉特征主导、文本信号被抑制的模态不对称性，导致硬噪声识别失效。即便偶然识别出硬噪声，现有框架仅关注正向对齐，缺乏结构化的负语义锚点，盲目推远操作会在连续且拥挤的度量空间中产生“涟漪效应”，损伤邻近干净样本的表示。本文切入点在于将噪声处理从标量判别升级为几何空间中的结构化遗忘，通过显式构建负边界与平滑传输路径，解决模态抑制、负锚点缺失与遗忘反冲三大挑战。

## 核心方法

### 方法参照系

本文问题属于噪声鲁棒CIR训练，与通用NCL流程的关键差异在于：通用流程依赖损失值阈值进行二分类判别，而本文需处理视觉相似但语义错误的硬噪声，要求特征空间具备细粒度感知、结构化排斥与无损伤遗忘能力。

### 几何保真量化（GFQ）

针对模态抑制导致的噪声误判，GFQ模块通过高斯随机采样估计几何噪声边界，量化样本匹配保真度。设计动机是打破单一混合损失对硬噪声的盲视，利用锥空间几何可分性显式定位噪声边界。

$$
B = \frac{1}{K} \sum_{k=1}^{K} \text{sim}(\mathbf{F}_{c,k}^{G}, \mathbf{F}_{t,k}^{G}) - \text{sim}(\mathbf{F}_{c}, \mathbf{F}_{t})
$$

该公式通过 $K$ 次高斯采样计算参考与目标特征的相似度均值，减去当前样本相似度，得到几何偏移量以估计噪声边界 $B$，从而将批次划分为高保真干净集与低保真噪声集。

### 负边界学习与目标遗忘（NBL & BTU）

NBL模块学习“对角负组合” $\mathbf{F}_{neg}$ 作为显式负锚点，解决负锚点缺失问题。设计动机是避免盲目推远，为遗忘提供明确的方向性语义边界。

$$
\mathcal{L}_{neg} = -\text{sim}(\mathbf{F}_{c}, \mathbf{F}_{neg}) + \text{sim}(\mathbf{F}_{t}, \mathbf{F}_{neg})
$$

该损失函数通过最小化组合特征与负组合的相似度、最大化目标特征与负组合的相似度，构建出与正向语义正交的负向边界。BTU模块将噪声修正建模为熵正则化最优传输（Optimal Transport, OT）问题，通过Sinkhorn-Knopp算法求解平滑传输计划 $\mathbf{P}^*$，将噪声样本的概率分布平滑转移至负边界，避免对邻近干净样本的损伤。

$$
\mathbf{P}^* = \arg\min_{\mathbf{P} \in \Pi(\mathbf{u}, \mathbf{v})} \langle \mathbf{P}, \mathbf{C}_{masked} \rangle - \epsilon H(\mathbf{P})
$$

该公式在满足边际约束 $\Pi(\mathbf{u}, \mathbf{v})$ 下最小化传输成本并最大化熵，生成软标签 $\mathbf{Y}$ 引导目标遗忘，实现精确且无涟漪的噪声消除。

## 实验评估

实验在FashionIQ与CIRR数据集上进行，噪声率 $\sigma$ 设置为0%、20%、50%、80%。基线覆盖SSN、CALA、SPRC、TME、HABIT、INTENT，遗漏了Air-Know与RankVR等最新鲁棒方法。在FashionIQ $\sigma=0.2$ 场景下，ConeSep取得64.97%的平均R@10，优于HABIT（64.38%）与INTENT（64.36%）；在CIRR $\sigma=0.2$ 场景下，ConeSep的R@1为52.29%，低于HABIT（52.71%）与INTENT（52.5%），但Avg(R@5, Rsub@1)达到80.43%，高于所有基线。

| 数据集 | 噪声率 | 方法 | 关键指标 | 数值 |
| :--- | :--- | :--- | :--- | :--- |
| FashionIQ | 20% | ConeSep | Avg R@10 | 64.97 |
| FashionIQ | 20% | HABIT | Avg R@10 | 64.38 |
| CIRR | 20% | ConeSep | R@1 | 52.29 |
| CIRR | 20% | HABIT | R@1 | 52.71 |

消融实验显示，移除GFQ中的随机目标采样导致FashionIQ Avg R@10下降至54.16%，移除NBL中的负提示导致CIRR Avg下降至78.94%，表明几何边界估计与负锚点构建对性能贡献显著。采样策略对比中，高斯采样优于经验分布与拉普拉斯分布，验证了锥空间几何假设的有效性。

评估边界方面，论文仅报告了R@K指标，未提供置信区间或计算效率的详细对比（尽管Table 4提及FLOPs，但未在正文深入分析）。代码已开源，超参数（如 $\omega=0.5$, $\gamma=0.7$）在正文中明确，可复现性较好。

## 关联研究分析

从问题动机看，ConeSep与INTENT均针对NTC中的硬噪声，但INTENT采用因果干预视角建模参考图与修改文本的潜在因果关系，而ConeSep采用几何空间视角。INTENT依赖因果图结构识别噪声，ConeSep依赖锥空间几何可分性。差异根源在于对噪声本质的理解：INTENT认为噪声源于模态间因果断裂，ConeSep认为噪声源于特征空间中的几何重叠。ConeSep在FashionIQ上优于INTENT，但在CIRR R@1上略低，暗示几何方法在开放域复杂语义变化上可能不如因果方法稳健。

从方法设计看，ConeSep与TME同属鲁棒CIR框架，但TME采用GMM分类器进行噪声识别，ConeSep采用GFQ进行几何边界估计。TME的GMM依赖损失值分布，易受模态抑制影响；ConeSep的GFQ通过随机采样估计边界，对硬噪声更敏感。ConeSep引入最优传输进行遗忘，而TME采用伪标签修正。最优传输提供平滑路径，避免TME中伪标签可能带来的语义混淆，但计算开销略高（训练时间5.15s/iteration vs TME 7.858s/iteration，实际ConeSep更快，但GPU内存更高）。

## 总结

ConeSep旨在解决CIR中硬噪声导致的模态抑制与遗忘反冲问题。现有方法依赖粗粒度损失判别，无法区分视觉相似但语义错误的样本，且缺乏负向锚点导致盲目修正。本文通过GFQ估计几何边界、NBL构建负组合、BTU执行最优传输遗忘，实现了结构化鲁棒训练。实验表明，ConeSep在FashionIQ $\sigma=0.2$ 下取得64.97% Avg R@10，CIRR $\sigma=0.2$ 下取得80.43% Avg(R@5, Rsub@1)。其边界在于CIRR R@1指标低于HABIT，且未评估在零样本CIR场景下的迁移能力。当噪声率提升至80%时，ConeSep的FashionIQ Avg R@10降至59.77%，而HABIT降至58.94%，这种微小差距是否源于最优传输在高噪声下的计算精度损失，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.20358)
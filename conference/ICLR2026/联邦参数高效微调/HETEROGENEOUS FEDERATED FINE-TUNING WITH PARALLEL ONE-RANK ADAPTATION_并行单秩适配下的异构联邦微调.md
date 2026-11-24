# ICLR2026最新论文 ｜HETEROGENEOUS FEDERATED FINE-TUNING WITH PARALLEL ONE-RANK ADAPTATION ｜并行单秩适配下的异构联邦微调

作者：Zikai Zhang、Rui Hu、Jiahao Xu

论文原文见 [arXiv](https://arxiv.org/abs/2602.16936)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_25916319)

> 联邦大语言模型微调中，客户端算力差异导致LoRA秩不匹配，传统截断或随机初始化策略引入显著噪声，阻碍全局模型收敛。Fed-PLoRA通过并行单秩模块分解与Select-N-Fold折叠策略，从结构上消除初始化噪声并最小化聚合噪声。该方法在异构设置下显著优于FLoRA与HETLoRA，但其绝对性能受限于骨干模型规模，且在极端非独立同分布数据下的理论收敛性尚未得到验证。

## 研究背景

联邦学习（Federated Learning, FL）允许分布式客户端在不共享原始数据的前提下协同训练大语言模型（Large Language Models, LLMs）。低秩适应（Low-Rank Adaptation, LoRA）通过冻结预训练权重并注入可训练的低秩矩阵 $A$ 和 $B$ 来更新模型，显著降低了通信与计算开销。然而，当客户端资源异构时，不同设备能负担的LoRA秩 $r$ 存在巨大差异，导致本地更新矩阵维度不一致，无法直接进行联邦平均（FedAvg）聚合。

现有异构LoRA聚合方法主要面临初始化与聚合噪声的双重困境。FLoRA采用堆叠策略但每轮随机重新初始化，HETLoRA通过截断全局矩阵初始化本地模块，FlexLoRA依赖奇异值分解（SVD）近似低秩表示。这些策略均因无法精确匹配全局秩与本地秩，导致信息丢失或引入随机扰动，严重削弱了全局模型的泛化能力。Fed-PLoRA的切入点在于重构LoRA的代数结构，将单一多秩矩阵分解为多个并行单秩模块，使客户端仅需训练子集模块，从而在数学上实现零初始化噪声与低聚合噪声。

## 核心方法

### 方法参照系

异构联邦微调的标准流程包含广播、本地更新与服务器聚合三步。传统方法在初始化阶段通过截断或随机生成将全局秩 $R$ 映射为本地秩 $r_i$，在聚合阶段通过零填充或SVD将本地更新映射回全局秩。本文的关键差异在于将LoRA模块从单一多秩结构改为并行单秩结构，使得秩的匹配从“近似映射”转变为“子集选择”。

### 并行单秩适配（PLoRA）

传统LoRA将秩 $R$ 的更新表示为 $\Delta W = BA$，其中 $B \in \mathbb{R}^{d \times R}, A \in \mathbb{R}^{R \times k}$。PLoRA将其分解为 $R$ 个并行单秩组件，总更新为：

$$ \Delta W_{PLoRA} = \sum_{j=1}^{R} B^{(j)} A^{(j)} $$

其中 $B^{(j)} \in \mathbb{R}^{d \times 1}, A^{(j)} \in \mathbb{R}^{1 \times k}$。这一设计动机在于解决传统多秩矩阵在异构场景下无法部分保留的问题：单秩模块具有原子性，客户端可独立选择训练哪些模块，而无需对未选模块进行截断或填充，从而避免了维度不匹配带来的代数误差。

### Select-N-Fold 策略

在PLoRA基础上，Select-N-Fold策略处理客户端资源限制。客户端 $i$ 根据算力预算从全局 $R$ 个模块中随机选择 $r_i$ 个进行训练，未选模块 $j \notin K_i$ 被折叠入冻结权重：

$$ W_i^{(t)} = W_0 + \sum_{j \notin K_i} B^{(j)}_{global} A^{(j)}_{global} $$

这一设计消除了初始化噪声，因为客户端始终从完整的全局状态出发，未选模块的信息被保留在冻结骨干中而非被丢弃。聚合时，服务器仅对客户端上传的已选模块进行加权平均，未选模块保持全局值不变。该策略将聚合噪声从“维度不匹配导致的交叉项误差”降低为“子集采样带来的方差”，且由于单秩模块的独立性，聚合过程无需SVD或零填充，计算开销极低。

## 实验评估

实验在GLUE、Natural Instructions、Dolly-15K、医疗与金融领域数据集上进行，使用BERT-base、Llama-1B、Llama-3.1-8B等模型。基线覆盖FedIT（同构）、FLoRA、FlexLoRA、HETLoRA（异构），但未对比2026年发布的FedPA-LoRA等最新乘积对齐方法。

| 数据集 | 方法 | 平均准确率/Rouge-L |
| :--- | :--- | :--- |
| GLUE (IID) | Fed-PLoRA | 79.89 |
| GLUE (IID) | HETLoRA | 73.55 |
| GLUE (IID) | FLoRA | 47.81 |
| Natural Instructions (non-IID) | Fed-PLoRA | 60.76 |
| Natural Instructions (non-IID) | FlexLoRA | 53.51 |

在GLUE基准上，Fed-PLoRA平均准确率79.89，较HETLoRA提升6.34，较FLoRA提升32.08，表明Select-N-Fold策略对随机初始化噪声的消除效果显著。在Natural Instructions非独立同分布设置下，Fed-PLoRA达到60.76，较FlexLoRA提升7.25，验证了单秩模块在数据异质性下的鲁棒性。

消融实验显示，单秩设计优于双秩设计（60.41 vs 59.35 Matthews Correlation），支持了原子化模块的设计选择。在极端非独立同分布（Dirichlet $\alpha=0.01$）设置下，Fed-PLoRA在CoLA上较FLoRA提升54.40，但在MATH任务上平均准确率28.96，低于同构FedIT的28.38仅0.58，表明在复杂推理任务上，异构聚合的收益被骨干模型能力瓶颈所掩盖。

评估边界方面，论文未报告置信区间，且未包含差分隐私（DP）下的性能测试。代码已开源，超参数与GPU配置（8×RTX A6000）详细披露，可复现性良好。

## 关联研究分析

从方法设计看，Fed-PLoRA与FLoRA均解决异构秩聚合，但FLoRA依赖堆叠与随机初始化，导致每轮引入随机扰动；Fed-PLoRA通过单秩分解与折叠策略，将初始化噪声降至零。这一差异源于对LoRA代数结构的重新审视：FLoRA视LoRA为整体矩阵，Fed-PLoRA视其为可分解的原子模块。根源在于任务特性：在NLU任务中，单秩模块的独立性足以捕捉局部特征，而在复杂推理任务中，多秩模块的联合表达力可能更为关键，论文未深入探讨这一权衡。

从问题动机看，Fed-PLoRA与FedPA-LoRA均关注聚合精度，但FedPA-LoRA通过乘积空间对齐解决因子分解非唯一性，Fed-PLoRA通过结构分解解决维度不匹配。FedPA-LoRA在GLUE上达到92.94，远高于Fed-PLoRA的79.89，但FedPA-LoRA假设同构秩，未处理资源异构。Fed-PLoRA的边界在于其单秩设计在极端非独立同分布下的收敛性理论保证缺失，且未验证与差分隐私噪声注入的兼容性。

## 总结

Fed-PLoRA解决了异构联邦微调中LoRA秩不匹配导致的初始化与聚合噪声问题，通过并行单秩适配与Select-N-Fold策略，在数学上实现了零初始化噪声。实验证明其在GLUE与Natural Instructions上显著优于FLoRA与HETLoRA，但在MATH任务上性能提升有限。论文的边界在于未验证极端非独立同分布下的理论收敛性，且单秩设计在复杂推理任务中的表达力瓶颈未得到解决。当客户端数据分布极度偏斜时，单秩模块的独立更新是否足以维持全局一致性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_25916319)
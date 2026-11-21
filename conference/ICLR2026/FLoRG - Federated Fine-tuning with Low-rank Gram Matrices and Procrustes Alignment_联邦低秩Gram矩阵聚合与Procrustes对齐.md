# ICLR2026最新论文 ｜FLoRG: Federated Fine-tuning with Low-rank Gram Matrices and Procrustes Alignment ｜联邦低秩Gram矩阵聚合与Procrustes对齐

研究机构：加拿大不列颠哥伦比亚大学、南方科技大学

作者：Chuiyang Meng、Ming Tang、Vincent W. S. Wong

论文原文见 [arXiv](https://arxiv.org/abs/2602.17095)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.17095)

> 联邦大语言模型微调中，直接平均低秩因子导致乘积偏差，而聚合乘积后的分解又因非唯一性引发子空间漂移。FLoRG通过单矩阵参数化与Gram矩阵线性聚合消除前者，并引入Procrustes对齐抑制后者。该方法在GLUE基准上显著优于传统因子聚合方案，但缺乏与最新乘积对齐方法的直接对比，其理论优势在极端资源受限场景下的实际收益仍存疑。

## 研究背景

低秩适应（LoRA）通过冻结预训练权重并注入可训练的低秩矩阵 $A$ 和 $B$ 来更新模型，显著减少了可训练参数和通信量。在联邦学习（FL）场景中，客户端上传局部因子，服务器进行聚合。然而，直接对 $A$ 和 $B$ 分别求平均再相乘，其结果 $\bar{A}\bar{B}$ 并不等于各客户端更新矩阵的平均值 $\frac{1}{N}\sum A_i B_i$，这种双线性不一致性引入了系统性聚合误差。

为消除该误差，部分研究（如FeDeRA）选择聚合乘积矩阵 $BA$，随后在服务器端进行矩阵分解以恢复低秩因子。这一策略虽然解决了聚合偏差，却引入了新的问题：矩阵分解的非唯一性。当聚合矩阵秩亏或存在重特征值时，存在多种有效的低秩分解，不同的分解选择会导致参数子空间发生漂移，进而改变后续轮次的梯度方向，累积降低微调性能。FLoRG旨在解决这一矛盾，即如何在消除聚合误差的同时，最小化分解过程带来的漂移。

## 核心方法

### 单矩阵参数化与Gram矩阵聚合

传统联邦LoRA流程中，客户端需上传两个矩阵 $B_n$ 和 $A_n$，服务器分别聚合后广播。FLoRG将LoRA模块重新参数化为单一低秩矩阵 $\mathbf{A}_t \in \mathbb{R}^{r \times k}$，其中 $k = \min(d_{in}, d_{out})$，并引入共享的半正交基矩阵 $\mathbf{L}$ 和 $\mathbf{R}$。更新矩阵表示为 $\Delta \mathbf{W}_t = \mathbf{L} \mathbf{A}_t \mathbf{R}$。客户端仅上传 $\mathbf{A}_t$，服务器聚合其Gram矩阵 $\mathbf{Q}_t = \mathbf{A}_t^\top \mathbf{A}_t$。

$$
\mathbf{Q}_{t+1} = \frac{1}{N} \sum_{n=1}^N \mathbf{A}_{tn+1}^\top \mathbf{A}_{tn+1}
$$

此公式表明，Gram矩阵的聚合是线性操作，且保持正半定性，从而在数学上消除了双线性聚合误差。这一设计将服务器端的双线性聚合转化为线性操作，同时由于仅传输单个矩阵，每轮上行通信开销减半。

### Procrustes对齐与分解漂移抑制

服务器对聚合后的Gram矩阵 $\mathbf{Q}_{t+1}$ 进行特征分解，得到规范分解 $\tilde{\mathbf{A}}_{t+1}$。由于分解非唯一，直接使用该矩阵会导致与上一轮 $\mathbf{A}_t$ 的子空间漂移。FLoRG引入Procrustes对齐矩阵 $\mathbf{S}_t$，通过最小化Frobenius范数距离来稳定更新方向。

$$
\mathbf{S}_{t,\star} = \arg\min_{\mathbf{S}} \|\mathbf{S} \tilde{\mathbf{A}}_{t+1} - \mathbf{A}_t\|_F^2 \quad \text{s.t.} \quad \mathbf{S}^\top \mathbf{S} = \mathbf{I}
$$

该优化问题的闭式解为 $\mathbf{S}_{t,\star} = \mathbf{U}_t \mathbf{V}_t^\top$，其中 $\mathbf{U}_t \mathbf{\Sigma}_t \mathbf{V}_t^\top$ 是 $\mathbf{A}_t \tilde{\mathbf{A}}_{t+1}^\top$ 的奇异值分解。此步骤将分解后的矩阵投影到目标 $r$ 秩子空间，在不改变Gram矩阵的前提下，选择与上一轮最接近的分解，从而抑制子空间漂移并解决秩不匹配问题。

## 实验评估

实验基于OPT-125M、RoBERTa-large和Llama-3.2-3B三个骨干网络，在GLUE基准（MNLI, QNLI, WNLI, RTE等）上进行评估。基线包括FedIT、FeDeRA、FFA-LoRA、FedSA-LoRA和FedEx-LoRA，覆盖了直接因子聚合、乘积聚合及残差修正等主流路线，但缺失2026年最新的乘积对齐方法如FedPA-LoRA。

| Base Model | Dataset | FLoRG | FedIT | FeDeRA | FedEx-LoRA |
| :--- | :--- | :--- | :--- | :--- | :--- |
| OPT-125M | MNLI | **87.35** | 79.42 | 81.15 | 85.83 |
| RoBERTa-large | MNLI | **91.27** | 84.91 | 88.06 | 90.96 |
| Llama-3.2-3B | MNLI | **93.15** | 87.24 | 89.83 | 92.74 |

在MNLI任务上，FLoRG在所有骨干网络上均取得最高准确率，较FedIT提升约7-8个百分点，较FedEx-LoRA提升约1-2个百分点。通信开销方面，FLoRG在达到80%准确率时传输参数量约为 $8.2 \times 10^6$，而FedEx-LoRA需 $1.25 \times 10^{10}$，通信效率提升超过2000倍。

消融实验显示，Procrustes对齐对性能提升至关重要。在RoBERTa-large上，移除对齐后MNLI准确率从91.39降至88.93，降幅达2.46个百分点。此外，FLoRG在极端非IID设置（$\rho=0.1$）下表现稳健，WNLI准确率为60.12，显著优于FedIT的53.07。然而，在Llama-3.2-3B的QNLI任务上，FedSA-LoRA以93.27略高于FLoRG的93.12，表明在特定大模型与任务组合下，单矩阵聚合并非绝对占优。

评估边界方面，论文未报告置信区间，且仅在GLUE和SQuAD上验证，缺乏GSM8K等复杂推理任务的测试。代码未公开，超参数设置（如 $\eta=5e-5, r=4$）固定，限制了可复现性。

## 关联研究分析

从问题动机看，FLoRG与FeDeRA均针对聚合偏差，但FeDeRA通过SVD分解乘积矩阵，忽略了分解非唯一性导致的漂移；FLoRG则通过Gram矩阵聚合与Procrustes对齐，显式处理了漂移问题。这一差异源于FLoRG对分解稳定性的重视，而FeDeRA更关注聚合的无偏性。从方法设计看，FLoRG与FedPA-LoRA同属精确聚合路线，但FedPA-LoRA通过乘积空间对齐实现，FLoRG则通过Gram矩阵空间聚合。FLoRG的通信开销更低，但FedPA-LoRA在GLUE整体准确率上更高（92.94 vs 91.27），这可能源于FedPA-LoRA保留了双矩阵的表达能力，而FLoRG的单矩阵参数化在复杂任务上可能损失部分信息。

## 总结

FLoRG解决了联邦LoRA中聚合偏差与分解漂移的矛盾，通过Gram矩阵线性聚合消除前者，Procrustes对齐抑制后者。在GLUE基准上，其准确率较FedIT提升约7-8个百分点，通信开销降低2000倍以上。然而，其单矩阵参数化在Llama-3.2-3B的QNLI任务上略逊于FedSA-LoRA，且缺乏与最新乘积对齐方法的直接对比。当骨干网络规模扩大至3B以上时，单矩阵表示的表达能力是否足以支撑复杂推理任务，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.17095)
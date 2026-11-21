# WACV2026最新论文 ｜MergeSlide: Continual Model Merging and Task-to-Class Prompt-Aligned Inference for Lifelong Learning on Whole Slide Images ｜基于正交模型合并的终身学习框架

研究机构：法国国家科学研究中心

作者：Doanh C. Bui、Ba Hung Ngo、Hoai Luan Pham 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.13099)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.13099)

> 全切片图像（WSI）终身学习旨在构建单一模型以顺序处理动态新增的癌症亚型分类任务，避免多模型维护的高昂算力与存储成本。现有重放（Rehearsal）方法依赖历史数据缓冲区，面临隐私泄露风险且对任务顺序敏感，而零样本推理虽无需训练但精度不足。MergeSlide 将终身学习重构为离线微调与在线正交模型合并过程，利用病理视觉-语言模型（VLM）的提示嵌入替代传统分类头，实现了无缓冲区的持续适应。该框架在六个 TCGA 数据集上显著优于重放基线，但其依赖全矩阵奇异值分解（SVD）的计算开销及缺乏空间定位能力，限制了其在超大规模任务流与临床证据解释上的适用性。

## 研究背景

WSI 分析通常采用多实例学习（MIL）范式，将千兆像素切片分割为补丁（Patch）并聚合特征以进行包级预测。在终身学习场景下，模型需顺序学习多个癌症亚型分类任务，核心挑战在于灾难性遗忘（Catastrophic Forgetting），即新任务训练导致旧任务性能急剧下降。传统解决方案分为正则化与重放两类，其中重放方法通过存储少量历史样本（Buffer）进行回放训练，虽性能较好，但违反了医疗数据隐私合规要求，且假设任务类别数固定，无法适应临床中动态变化的亚型定义。

随着病理基础模型（如 TITAN、CONCH）的成熟，视觉-语言对齐为 WSI 分析提供了新的语义锚点。然而，现有基于基础模型的终身学习方法仍沿用重放机制，未能充分利用模型合并（Model Merging）在参数隔离上的优势。模型合并通过计算任务向量（Task Vector，即任务特定权重与基础模型权重之差）来整合知识，理论上可避免训练过程中的参数干扰。MergeSlide 的切入点在于：将 WSI 终身学习转化为正交模型合并问题，通过冻结基础模型特征、微调无 MLP 骨干，并利用 SVD 正交投影合并任务向量，从而在无需存储原始 WSI 数据的前提下，实现对新任务的持续吸纳与旧知识的保留。

## 核心方法

### 方法参照系

标准 WSI 分类流程为“特征提取→聚合→分类头预测”。MergeSlide 的关键差异在于去除了可训练的分类头（MLP），改用冻结的类感知提示嵌入（Class-aware Prompt Embeddings）进行点积相似度推理，并将训练过程解耦为独立的任务微调与全局权重合并两个阶段，而非端到端的顺序训练。

### 无 MLP 任务特定微调

传统 MIL 聚合器后接可训练分类头，导致新任务类别数变化时需重新定义 Logits 维度，且微调会直接覆盖旧任务参数。MergeSlide 采用无 MLP 架构，仅微调 Transformer 聚合器 $f_A$ 的权重。对于任务 $t$，利用 TITAN 文本编码器生成类感知提示嵌入 $E_{C,t}$，通过点积计算预测概率：

$$ p_i = \text{softmax}\left( \frac{Z_i E_{C,t}^\top}{\sqrt{d}} \right) $$

其中 $Z_i$ 为切片嵌入，$d$ 为嵌入维度。这一设计使得类别定义由文本提示动态决定，无需预定义最大 Logits 数，解决了固定类别假设在临床动态场景下的失效问题，同时限制了微调范围，降低了参数漂移风险。

### 正交持续模型合并

直接线性合并任务向量会导致新旧任务知识相互干扰。MergeSlide 引入正交投影机制，确保新任务向量 $\Delta \theta_t$ 与已合并向量 $\Delta \tilde{\theta}_{1:t-1}$ 正交。首先对已合并向量进行 SVD 分解 $\Delta \tilde{\theta}_{1:t-1} = U \Sigma V^\top$，定义投影函数 $G(\cdot)$：

$$ G(\Delta \theta_t) = (U^\top \Delta \theta_t V) \odot M $$

其中 $M$ 为零对角掩码矩阵，$\odot$ 为哈达玛积。该公式通过屏蔽对角线分量，提取 $\Delta \theta_t$ 中相对于旧任务的新增信息，保证 $\langle G(\Delta \theta_t), \Delta \tilde{\theta}_{1:t-1} \rangle_F = 0$。合并权重 $\tilde{\theta}_{1:t}$ 由 $\theta_{base} + \lambda_{t-1} \Delta \tilde{\theta}_{1:t-1} + \lambda_t G(\Delta \theta_t)$ 构成，其中 $\lambda_t$ 动态调整以约束合并权重与基础模型的距离，防止模型偏离通用病理知识过远。

## 实验评估

实验在六个 TCGA 癌症亚型数据集（BRCA, RCC, NSCLC, ESCA, TGCT, CESC）上进行，采用 10 折交叉验证，任务序列为从常见到罕见（B→R→N→E→T→C）。基线包括重放方法（DER++, ConSlide, ADaFGrad）、正则化方法（ER-ACE, AGEM）及零样本推理。MergeSlide 在 CLASS-IL 设定下表现最优，其平衡准确率（bACC）达到 87.930%，显著高于 ConSlide 的 70.821% 和 ADaFGrad 的 77.096%。

| 方法 | Buffer Size | bACC (CLASS-IL) | Masked bACC (TASK-IL) | FGT | BWT |
| :--- | :--- | :--- | :--- | :--- | :--- |
| ConSlide | 30 WSIs | 70.821 (±2.180) | 88.896 (±2.442) | 3.117 (±1.784) | -2.521 (±1.940) |
| ADaFGrad | 30 WSIs | 77.096 (±4.474) | 90.216 (±1.677) | 2.304 (±1.072) | -0.821 (±0.918) |
| MergeSlide (naive) | 0 WSIs | 80.636 (±1.865) | 92.109 (±1.700) | 4.246 (±1.585) | -1.808 (±1.987) |
| MergeSlide (w/ TCP) | 0 WSIs | 87.930 (±2.112) | 92.109 (±1.700) | 1.807 (±0.604) | 0.958 (±0.868) |

MergeSlide 在启用任务到类提示对齐（TCP）推理后，bACC 提升 7.294 个百分点，且遗忘指标（FGT）降至 1.807%，优于所有可训练基线。值得注意的是，MergeSlide 的后向迁移（BWT）为正值 0.958，表明新任务学习对旧任务有轻微正向促进，而 ConSlide 为负值。在任务顺序敏感性测试中，MergeSlide 在反向序列（C→T→E→N→R→B）下 bACC 仅下降 0.032%，而 DER++ 和 ConSlide 性能波动较大，验证了其顺序无关性。

计算效率方面，MergeSlide 训练阶段单任务微调耗时 74.26 秒，合并耗时 4.50 秒，总 VRAM 占用 4.09 GB。相比 ADaFGrad 的 104.17 秒训练时间，MergeSlide 快 1.3 倍。推理阶段，MergeSlide 吞吐量为 55.82 slides/s，略低于 ConSlide 的 67.89 slides/s，但考虑到其无需维护缓冲区且精度更高，该权衡在临床部署中可接受。

评估边界方面，实验仅涵盖 TCGA 数据集，未涉及跨机构域偏移（Domain Shift）的严格测试，尽管论文提及 OOD 设置，但主要结果集中在 In-domain。代码已开源，但 SVD 分解的全矩阵计算在任务数量极大时可能成为瓶颈，论文未提供低秩近似的实验对比。

## 关联研究分析

从问题动机看，MergeSlide 与 ConSlide 均针对 WSI 终身学习，但 ConSlide 依赖重放缓冲区解决遗忘，而 MergeSlide 通过参数合并解决。ConSlide 的缓冲区机制在数据隐私受限场景下不可行，且其性能对任务顺序敏感，根源在于其训练过程依赖于历史样本的梯度更新。MergeSlide 的离线微调与在线合并解耦了训练与推理，使得模型更新不再依赖历史数据，从而天然具备顺序无关性。然而，MergeSlide 依赖 TITAN 的文本编码器生成提示，其性能上限受限于基础模型的语义对齐质量，而 ConSlide 直接学习视觉特征，可能在细粒度形态差异识别上更具优势，但论文未提供此类细粒度对比。

从方法设计看，MergeSlide 借鉴了 Task Arithmetic 的任务向量概念，但引入了 SVD 正交投影。与简单的线性加权合并相比，正交投影通过屏蔽共享子空间，强制新任务学习在正交方向上进行，这在理论上保证了知识隔离。然而，这种设计假设任务向量在 SVD 基下具有稀疏性，若新任务与旧任务高度相关（如相似亚型），正交投影可能过度抑制有效信息。相比之下，ADaFGrad 采用梯度蒸馏，虽无正交约束，但通过对比学习保留语义一致性，其在 BWT 指标上表现优于 MergeSlide 的 naive 版本，说明梯度层面的约束在某些场景下可能比参数层面的正交更灵活。

## 总结

MergeSlide 旨在解决 WSI 终身学习中数据隐私与灾难性遗忘的矛盾，通过正交模型合并替代重放机制，实现了无缓冲区的持续学习。其核心创新在于利用 SVD 正交投影隔离任务向量，并结合无 MLP 架构与提示对齐推理，在六个 TCGA 数据集上取得了 87.930% 的 CLASS-IL bACC，显著优于 ConSlide 等重放基线。然而，该方法依赖全矩阵 SVD 计算，随着任务数量增加，合并开销呈二次方增长，且缺乏空间定位能力，无法提供临床所需的区域级证据。当任务流扩展至数十个癌症亚型时，SVD 分解的计算延迟是否会导致合并过程成为系统瓶颈，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.13099)
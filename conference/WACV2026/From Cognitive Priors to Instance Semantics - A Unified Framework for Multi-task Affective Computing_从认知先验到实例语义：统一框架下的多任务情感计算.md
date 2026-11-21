# WACV2026最新论文 ｜From Cognitive Priors to Instance Semantics: A Unified Framework for Multi-task Affective Computing ｜从认知先验到实例语义：统一框架下的多任务情感计算

研究机构：英国伦敦玛丽女王大学

作者：Guanyu Hu、Dimitrios Kollias、Xinyu Yang

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f67ee16dfe18)

> 多任务情感计算旨在同时建模效价-唤醒度（Valence-Arousal, VA）回归、动作单元（Action Units, AUs）检测与基本表情（Expressions, Exprs）分类，但现有方法受限于完整标注假设，无法利用异构数据集。COIN 通过认知引导的伪标签传播与双分支知识蒸馏，在缺失标注条件下实现跨任务监督共享。其核心在于将 FACS 解剖学先验转化为可微分损失，并引入 CLIP 文本编码器进行实例级语义对齐。该框架在单模态视觉基准上超越了单任务与多任务基线，但其对多模态信号的扩展性及认知先验的泛化边界尚待验证。

## 研究背景

面部情感建模面临数据标注的结构性碎片化：AffectNet 提供约 40 万张图像的表情与 VA 标注，而 EmotioNet、DISFA 和 GFT 仅包含 17 个 AUs 的二值标注，且各数据集间标注集合互不重叠。这种异构性导致传统多任务学习（Multi-Task Learning, MTL）面临负迁移（Negative Transfer, NT）与任务特定性能错位（Task-specific Performance Misalignment, TPM）：当 VA 和 AU 任务因数据量较大主导梯度更新时，表情识别性能反而低于单任务基线。

现有 MTL 方法如 MGDA-UB 和 GradNorm 依赖完整标注数据集进行梯度投影或权重平衡，无法处理标注缺失场景。部分跨任务方法尝试从表情推断 AU 或反之，但局限于单任务目标或简单跨数据集设置，未解决回归、检测与分类三类异构任务的联合优化。COIN 的切入点在于利用 FACS 系统中表情与 AU 之间的解剖学关联，构建认知引导的伪标签机制，使监督信号在部分标注样本间传播，从而在不增加数据标注成本的前提下缓解 NT 与 TPM。

## 核心方法

### 方法参照系

标准 MTL 框架假设所有任务共享同一批完整标注样本，通过共享骨干网络与任务特定头联合优化。COIN 的关键差异在于处理标注集合互不重叠（disjoint annotations）的场景，即每个样本仅拥有三类标签中的一种，需通过跨任务推理补全缺失监督。

### 认知引导的 CogXpert 共挖掘

针对标注缺失导致的监督稀疏问题，COIN 在 Stage 1 引入 CogXpert 共挖掘策略，利用表情与 AU 间的认知映射关系生成伪标签。设计动机在于：直接融合异构任务会因数据分布差异引发梯度冲突，而基于 FACS 先验的伪标签能提供语义一致的跨任务约束。具体而言，表情到 AU（E2A）路径通过软目标二元交叉熵损失 $L_{E2A}$ 将表情预测转化为 AU 伪标签：

$$L_{E2A} = -\sum_{i=1}^{K} \left[ q_i^{AU} \cdot \log(p_i^{AU}) + (1 - q_i^{AU}) \cdot \log(1 - p_i^{AU}) \right]$$

其中 $q_i^{AU}$ 由表情预测 $p_i^{Exp}$ 经 Table 1 中的原型/观察性 AU 权重映射生成。AU 到表情（A2E）路径则通过分类交叉熵损失 $L_{A2E}$ 实现反向推理。该机制使模型在仅含表情标注的样本上获得 AU 监督，反之亦然，从而平衡任务学习动态，防止主导任务淹没欠表示任务。

### 专家与语义知识集成（ESKI）

Stage 2 引入 ESKI 双分支架构解决 TPM 问题，即不同任务在训练过程中达到最优性能的时间点不一致。设计动机在于：单纯的知识蒸馏无法完全消除任务间的语义冲突，需引入外部语义锚点。任务特定分支从 Stage 1 提取的三个任务最优 CogXpert（VA、AU、Expr 各一）蒸馏软预测，损失函数为：

$$L_{Task} = \sum_{i=1}^{3} \lambda_i L_{S}^{Task_i} + \sum_{j=1}^{3} \lambda_j L_{D}^{Task_j}$$

其中 $L_{S}$ 为真实标签监督，$L_{D}$ 为专家蒸馏损失。语义对齐分支利用 CLIP 文本编码器，通过类条件提示（Class-Conditioned Prompts）提供静态全局语义锚点，实例自适应提示（Instance-Adaptive Prompts）捕获模型预测的上下文特定线索。推理时移除语义分支，仅保留专家分支，确保部署效率。

## 实验评估

实验在 AffectNet、RAF-DB、EmotioNet、DISFA、GFT 五个数据集上进行，覆盖表情识别（F1/AA）、AU 检测（F1）与 VA 估计（CCC）三类任务。基线包括单任务 SOTA（FUXI、SITU、CLIPER）及 MTL 方法（MGDA-UB、GradNorm、AdaShare、TR）。COIN 在 AffectNet-7 上取得 67.0% F1，RAF-DB 上 83.3% AA，EmotioNet 上 67.4% F1，DISFA 上 60.1% F1，GFT 上 64.3% F1，AffectNet-VA 上 59.7% CCC，全面超越单任务与 MTL 基线。

| 数据集 | 任务 | COIN | 最强基线 | 基线方法 |
| :--- | :--- | :--- | :--- | :--- |
| AffectNet | Expr (F1) | 67.0 ± 0.3 | 66.3 | CLIPER |
| RAF-DB | Expr (AA) | 83.3 ± 0.4 | 80.1 | retrained CLIP |
| EmotioNet | AU (F1) | 67.4 ± 0.4 | 57.9 | CLIPER |
| DISFA | AU (F1) | 60.1 ± 0.3 | 54.9 | CLIPER |
| GFT | AU (F1) | 64.3 ± 0.7 | 61.7 | CLIPER |
| AffectNet | VA (CCC) | 59.7 ± 0.3 | 57.6 | retrained CLIP |

消融实验显示，类条件提示贡献最大，实例自适应提示提供中等增益，噪声注入主要起正则化作用。移除语义分支后性能下降，但双分支设计优于单分支，验证了梯度解耦的有效性。与 VLM 对比，COIN 在冻结与微调设置下均优于 GPT-4o、Gemini-1.5 等模型，表明专用多任务架构在细粒度面部情感任务上的优势。

评估边界方面，COIN 仅在单模态视觉数据上验证，未涉及音频或文本模态；所有实验使用 ConvNeXt-Base 骨干，未测试其他架构的泛化性；代码已开源，但超参数设置（如学习率衰减因子 γ=0.7）未提供敏感性分析。

## 关联研究分析

从问题动机看，COIN 与 MISA 均采用解耦思想，但 MISA 解耦模态不变与模态特定子空间以处理跨模态异质性，而 COIN 解耦任务特定与共享语义以处理跨任务标注缺失。这一差异源于任务特性：多模态融合需对齐不同传感器信号，而多任务学习需协调不同标签空间的监督信号。COIN 的认知先验伪标签是否限制了模型发现非典型情感关联的能力，论文未给出回答。

从方法设计看，COIN 与 CLIPER 均利用 CLIP 进行语义对齐，但 CLIPER 采用冻结编码器与静态提示，而 COIN 引入实例自适应提示与双分支蒸馏。这一差异源于对 TPM 的处理策略：CLIPER 依赖预训练语义的静态匹配，而 COIN 通过动态提示与专家蒸馏实现任务间的语义协调。COIN 未使用 LLM 进行推理，仅用 CLIP 做语义对齐，这是否牺牲了复杂情感语境下的因果归因能力，需进一步验证。

## 总结

COIN 解决的核心矛盾是异构标注下多任务情感计算的负迁移与性能错位问题。其切入点在于利用 FACS 解剖学先验构建跨任务伪标签，使监督信号在部分标注样本间传播，从而在不增加数据成本的前提下实现跨任务知识共享。方法上，COIN 通过 CogXpert 共挖掘与 ESKI 双分支架构，在 AffectNet-7 上取得 67.0% F1，在 EmotioNet 上取得 67.4% F1，超越单任务与 MTL 基线。其边界在于仅验证单模态视觉场景，且认知先验的泛化性未在多模态或跨文化数据上测试。当支持集增大到 5-shot 时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_f67ee16dfe18)
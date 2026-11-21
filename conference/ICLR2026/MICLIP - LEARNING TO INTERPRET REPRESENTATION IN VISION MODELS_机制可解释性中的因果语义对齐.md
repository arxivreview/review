# ICLR2026最新论文 ｜MICLIP: LEARNING TO INTERPRET REPRESENTATION IN VISION MODELS ｜机制可解释性中的因果语义对齐

研究机构：上海科技大学

作者：Yingdong Shi、Zhiyu Yang、Changming Li 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_19626935)

> 视觉模型内部机制的可解释性长期受困于“激活幅度假设”与“输入中心性”的双重局限，导致对神经元功能的描述缺乏因果效力，尤其在模型预测错误时失效。MICLIP 通过对比学习将内部表示单元映射至 CLIP 语义空间，同时接地输入概念与输出语义，实现了从启发式相关性到因果语义对齐的范式转换。该方法在 ImageNet-1k 神经元描述准确率达到 1.0000，并在 DTD 未见概念干预中展现出稳定的因果调控能力。其价值在于提供了跨架构的通用解释框架，但神经元编码器的线性假设是否足以捕捉深层非线性机制，仍是存疑之处。

## 研究背景

当研究者试图理解视觉模型为何将“海葵”误判为“羽毛围巾”时，传统方法往往陷入困境：它们依赖神经元激活幅度的大小来推断概念存在，却忽略了激活值高并不必然意味着该概念参与了决策过程，甚至负激活可能正向影响预测。这一现象揭示了“激活幅度假设”的根本缺陷。为克服此局限，机制可解释性（Mechanistic Interpretability, MI）领域转向分析内部表示单元与人类概念之间的关联，但现有方法多采用“输入中心”范式，仅将神经元激活与输入图像中的概念进行关联，未能捕捉驱动模型输出的因果机制。

主流 MI 路线分为激活基法与表示基法。激活基法如 Network Dissection (Bau et al., 2017) 和 V-Interp (Zhang et al., 2024) 通过选取高激活样本并关联其标注或生成描述来解释神经元，但均隐含激活幅度假设，且在模型预测错误时失效，因为高激活可能源于背景线索而非前景物体。表示基法如 CLIP-Dissect (Oikarinen & Weng, 2023) 尝试在 CLIP 嵌入空间中构建神经元与概念的相关性，但其神经元表示仍基于启发式的激活向量，未通过端到端优化学习语义映射。MICLIP 的切入点在于摒弃启发式设计与激活幅度依赖，通过对比学习直接训练神经元编码器，将内部机制与输入、输出双侧语义对齐，从而建立具有因果效力的解释框架。

## 核心方法

### 方法参照系

本文问题归属于“表示基机制可解释性”类别，其标准流程是将模型内部单元与概念映射至共享嵌入空间并计算相似度。与 CLIP-Dissect 等现有方法的关键差异在于：本文不依赖启发式构建的神经元表示，而是通过可学习的编码器将原始激活映射至 CLIP 语义空间，并引入输出语义作为对齐目标，形成输入-输出双接地机制。

### 对比学习驱动的机制-概念对齐

传统方法如 CLIP-Dissect 使用探针数据集上的激活向量作为神经元表示，这种启发式设计无法捕捉神经元对输出的因果贡献。MICLIP 在此环节引入可训练的神经元编码器 $E_n(\cdot; \theta_n)$，通过对称 InfoNCE 损失将神经元激活 $\mathbf{a} \in \mathbb{R}^n$ 映射至 CLIP 嵌入空间，同时与概念嵌入 $\mathbf{c} = E_c(c)$ 和图像嵌入 $\mathbf{x} = E_i(x)$ 进行对比优化：

$$
\mathcal{L} = -\frac{1}{N} \sum_{i=1}^{N} \log \frac{\exp(\text{sim}(\mathbf{n}_i, \mathbf{c}_i)/\tau)}{\sum_{j=1}^{N} \exp(\text{sim}(\mathbf{n}_i, \mathbf{c}_j)/\tau)} - \frac{1}{N} \sum_{i=1}^{N} \log \frac{\exp(\text{sim}(\mathbf{n}_i, \mathbf{x}_i)/\tau)}{\sum_{j=1}^{N} \exp(\text{sim}(\mathbf{n}_i, \mathbf{x}_j)/\tau)}
$$

该公式的物理含义是：神经元嵌入 $\mathbf{n}_i$ 应与其对应的预测概念 $\mathbf{c}_i$ 和输入图像 $\mathbf{x}_i$ 在语义空间中接近，而与批次内其他概念和图像远离。这一设计解决了输入中心方法无法区分“高激活但无因果贡献”神经元的问题，因为输出语义的引入迫使编码器学习那些真正影响预测结果的机制。

### 双向语义定位与因果干预

基于训练好的编码器，MICLIP 实现双向定位：给定概念 $c$，通过 $\mathbf{L}_c = \text{SelectTop-}_\tau(\{\text{sim}(\mathbf{u}_i, c)\}_{u_i \in U})$ 定位最相关的机制单元；给定单元 $u$，通过 $\mathbf{D}_u = \text{SelectTop-}_\tau(\{\text{sim}(u, c_j)\}_{c_j \in C})$ 生成概念描述。为验证因果性，本文对定位到的单元施加干预：

$$
\tilde{u}_i = \beta u_i \quad (\text{Scaling}) \quad \text{或} \quad \tilde{u}_i = u_i + \beta \quad (\text{Adding}), \quad \forall i \in \mathbf{L}_c
$$

通过调整缩放因子 $\beta$ 或偏置，抑制或放大特定概念的影响。这一干预机制的价值在于：若同一组单元既能通过放大提升准确率，又能通过抑制降低准确率，则证明该单元确实因果性地驱动了模型行为，而非仅与输入相关。

## 实验评估

实验在 ResNet-50、ViT-B/16 和 CLIP/ViT-B-16 上进行，基线包括 CLIP-Dissect、V-Interp、Network Dissection 和 Act-Values。在 ImageNet-1k 神经元描述任务中，MICLIP 在 ResNet-50 和 ViT-B/16 上均取得 1.0000 的准确率，显著优于 CLIP-Dissect 的 0.9995 和 0.9989。在 DTD 未见概念干预实验中，MICLIP 在 CLIP/ViT-B-16 上的增强 $\Delta$Acc 为 0.38% ($\pm$0.11)，移除 $\Delta$Acc 为 -0.91% ($\pm$0.20)，而 CLIP-Dissect 的增强 $\Delta$Acc 仅为 0.00% ($\pm$0.15)，表明 MICLIP 在未见概念上具有更强的因果泛化能力。

| 方法 | ResNet-50 Acc. | ViT-B/16 Acc. | CLIP Acc. |
| :--- | :--- | :--- | :--- |
| CLIP-Dissect | 0.9995 | 0.9989 | - |
| MICLIP | 1.0000 | 1.0000 | - |

消融实验揭示了输入-输出双接地的必要性。Output-Only 变体在 ImageNet-1k 上表现强劲（ResNet-50 移除 $\Delta$Acc -17.98%），但在 DTD 上失效（增强 $\Delta$Acc -2.60%），表明仅依赖输出语义会导致对训练分布的过拟合。Input-Only 变体在 DTD 上泛化较好（增强 $\Delta$Acc 0.69%），但在 ImageNet-1k 上效果较弱（移除 $\Delta$Acc -12.63%）。完整 MICLIP 在两个数据集上均保持稳健，证实了双接地策略的协同效应。

评估边界方面，论文未报告神经元编码器的训练超参数（如学习率、批次大小）和计算开销，仅提及使用三个随机种子进行 t 检验。代码已开源，但缺乏对 SAE 特征提取过程的详细复现指南。此外，实验未包含基于因果干预的其他 MI 方法（如 Gandelsman et al., 2025）作为基线，限制了与最新因果解释方法的直接对比。

## 关联研究分析

从问题动机看，MICLIP 与 CLIP-Dissect 的核心差异在于对“神经元功能”的定义。CLIP-Dissect 将神经元功能定义为其与输入概念的相关性，这是一种描述性关联；而 MICLIP 将功能定义为对输出语义的因果贡献，这是一种机制性解释。这一差异源于任务特性的不同：CLIP-Dissect 旨在生成人类可读的描述，而 MICLIP 旨在支持模型调控。然而，MICLIP 的因果性验证依赖于干预实验，其有效性假设了线性干预的充分性，对于深层非线性机制，这种假设可能过于简化。

从方法设计看，MICLIP 与 Balasubramanian et al. (2024) 同属表示基方法，但后者局限于 ViT 子模块（如注意力头）的线性分解，而 MICLIP 通过可学习编码器支持任意架构的神经元和 SAE 特征。这一泛化能力的代价是引入了额外的训练开销和编码器参数。查询侧增强在数据充足时是否仍有增益，论文未给出回答，因为实验仅在 ImageNet-1k 和 DTD 两个数据集上进行，缺乏大规模多域验证。

## 总结

MICLIP 解决了机制可解释性中激活幅度假设与输入中心性导致的因果缺失问题，通过对比学习将内部机制与输入、输出双侧语义对齐，实现了从描述性关联到因果性解释的转换。在 ImageNet-1k 神经元描述中，MICLIP 取得 1.0000 的准确率，在 DTD 未见概念干预中展现出稳定的因果调控能力。其边界在于神经元编码器的线性假设可能无法捕捉深层非线性机制，且实验缺乏与最新因果干预方法的对比。当支持集增大到 5-shot 时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_19626935)
# HuggingFace最新推荐论文 ｜Nemotron-Labs-Diffusion-Image: Advancing Masked Discrete Diffusion for High-Resolution Image Synthesis ｜离散掩码扩散的自校正与大词表优化

作者：Shufan Li、Greg Heinrich、Hanrong Ye 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.29814)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.29814)

> 离散图像生成旨在利用Token序列兼容大语言模型架构，但现有掩码扩散模型（MDM）存在两大瓶颈：一旦Token被解码便无法修正，且大词表导致训练信号稀疏。本文通过引入Token编辑机制实现推理时的迭代自校正，并提出分组交叉熵（GCE）损失解决大词表下的优化困难。该方案在GenEval上取得0.90的SOTA成绩，但其性能是否完全归因于架构创新，还是得益于预训练语言模型的语义先验，仍需进一步剥离验证。

## 研究背景

离散图像生成将图像映射为Token序列，旨在复用大语言模型（LLM）的优化技术如KV缓存与序列打包。然而，掩码扩散模型（MDM）虽支持并行解码，却缺乏连续扩散模型（LDM）的渐进精修能力。MDM在推理时独立采样每个位置的Token，隐含了Token间独立性的假设，而图像Token实际存在强依赖，导致早期错误无法在后续步骤中修正，造成误差累积。

当前主流离散生成路线如Meissonic和LaViDa-O主要依赖编码器-解码器架构或固定词表，未能解决自校正缺失问题。同时，提升图像保真度需扩大词表规模，但大词表引发“代码本稀疏性”问题：单个Token出现频率骤降，标准交叉熵损失无法捕捉语义相似性，导致训练信号不足。本文切入点在于改造MDM的训练与推理流程，使其具备类似LDM的自校正能力，并设计针对大词表稀疏性的新损失函数。

## 核心方法

### 掩码扩散模型参照系

标准MDM从全掩码序列开始，通过多步去噪逐步揭示Token。其训练目标仅在掩码位置计算交叉熵，推理时一旦Token被揭示即固定不变。本文的关键差异在于：训练时引入Token腐蚀以学习修正能力，推理时允许已揭示Token被替换，从而打破“一次性承诺”的限制。

### Token编辑机制

标准MDM在推理时无法修正早期错误，导致误差累积。本文在训练阶段对可见Token进行腐蚀，使模型学习预测“是否修正”而非仅预测新Token。具体而言，给定干净序列 $y_0$，前向过程 $q'(y_t|y_0)$ 不仅掩码部分Token，还将部分可见Token替换为同图像内随机Token或嵌入空间邻近Token。训练目标扩展至所有位置：

$$
\mathcal{L} = \sum_{i=1}^{L} \left[ \mathbb{1}[y_i^t = M] \log p_\theta(y_i^0 | y^t) + \mathbb{1}[y_i^t \neq M] \log p_\theta(y_i^0 | y^t) \right]
$$

此公式表明，模型需在掩码位置预测新Token，在可见位置预测原Token或修正Token。推理时，若模型对已揭示位置预测不同Token且置信度超过阈值 $\tau$，则执行替换。该机制使MDM具备迭代精修能力，显著降低因Token独立性假设导致的误差累积。

### 分组交叉熵（GCE）

大词表下，标准交叉熵将非目标Token视为同等负例，忽略语义相似性。本文提出GCE，通过K-means将词表聚类为多层级组，在组级别施加交叉熵损失。设词表大小为 $|V|$，聚类数为 $M$，组概率 $P(C_i) = \sum_{j \in C_i} p_j$。GCE目标为：

$$
J_{GCE} = -\log p_\theta(y_0^i | y^t) - \sum_{j=1}^{K} \lambda_j \log P(C_j(y_0^i))
$$

其中 $K$ 为聚类层级数，$\lambda_j$ 为权重。该损失为语义邻近Token提供正向梯度，缓解稀疏性。相比软标签方法SNCE，GCE仅存储离散索引，内存开销更低，且避免软标签导致的优化不稳定。

## 实验评估

| 模型 | 参数量 | GenEval Overall | DPG | MJHQ-30k HPSv3 |
| :--- | :--- | :--- | :--- | :--- |
| Meissonic | 1B | 0.54 | - | - |
| LaViDa-O | 10B | 0.77 | 81.8 | 8.81 |
| FLUX.1-dev | 12B | 0.66 | - | - |
| NLD-Image | 8B | 0.90 | 85.2 | 9.61 |
| NLD-Image* | 8B | - | 86.9 | 10.76 |

*注：NLD-Image* 在6M合成数据上微调。

实验覆盖GenEval、DPG和MJHQ-30k基准，对比了Meissonic、LaViDa-O等离散模型及FLUX.1-dev等连续模型。NLD-Image在GenEval上以0.90显著超越所有基线，DPG得分85.2接近GPT-4o的85.3。消融实验显示，GCE在ImageNet256上将FID从CE的7.53降至3.40，证明其对大词表优化的有效性。Token编辑机制在推理延迟增加8ms的情况下，提升了图像保真度。

评估边界方面，论文未报告置信区间，且FID指标被作者指出与人类感知相关性差，故侧重HPSv3。可复现性上，论文提供训练细节（64 H100 GPUs, 300K steps），但未开源代码，超参数如腐蚀比例 $\tau$ 的敏感性分析缺失。

## 关联研究分析

从问题动机看，本文与连续扩散模型中的动态引导调度（如TCFG）均旨在解决推理时的误差累积，但路径不同。TCFG通过截断后期引导避免过饱和，而NLD-Image通过Token编辑修正离散Token错误。根源在于离散Token的不可逆性：连续空间中噪声可逐步消除，而离散Token一旦解码即固定，必须引入显式修正机制。

从方法设计看，GCE与SNCE均针对大词表稀疏性，但GCE采用离散聚类索引而非软标签。SNCE的软标签需存储 $L \times |V|$ 实数，内存开销大，且固定平滑目标可能导致优化不稳定。GCE通过层级聚类提供动态正向信号，内存开销仅增加离散索引，更适合大规模训练。这一差异源于对“语义相似性”建模方式的根本不同：SNCE依赖距离度量，GCE依赖聚类结构。

## 总结

本文核心矛盾在于离散MDM缺乏自校正能力与大词表训练信号稀疏。通过Token编辑机制和GCE损失，NLD-Image在GenEval上达到0.90，DPG 85.2，显著超越Meissonic和LaViDa-O。其边界在于：性能提升是否完全归因于架构创新，还是得益于8B预训练语言模型的语义先验？论文未提供去除预训练权重的消融实验，无法剥离语言模型贡献。当支持集增大到5-shot时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.29814)
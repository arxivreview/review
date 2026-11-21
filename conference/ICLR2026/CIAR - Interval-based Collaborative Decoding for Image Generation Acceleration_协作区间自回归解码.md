# ICLR2026最新论文 ｜CIAR: Interval-based Collaborative Decoding for Image Generation Acceleration ｜协作区间自回归解码

研究机构：浙江大学、上海交通大学

作者：Keming Ye、Zhou Zhao、Fan Wu 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.25463)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.25463)

> 自回归视觉生成在端侧部署时面临推理延迟高与云端验证开销大的双重瓶颈，传统推测解码因视觉Token空间冗余性导致均匀验证策略效率低下。本文提出CIAR框架，通过端侧连续概率区间量化不确定性，实现选择性云端验证。该方法在保持图像质量基本不变的前提下，将推理延迟降低至基线的30%左右，但其在动态分辨率场景下的泛化能力仍存疑。

## 研究背景

自回归模型将图像转化为离散Token序列进行预测，其核心挑战在于序列长度随分辨率平方增长，导致端侧计算资源受限。推测解码（Speculative Decoding, SD）通过小模型生成候选、大模型验证来加速推理，但在视觉任务中，图像Token具有强烈的空间局部性和低熵区域（如背景），传统基于离散熵或随机策略的验证机制无法区分高置信度与低置信度区域，造成大量冗余通信。

现有视觉加速方法如Lantern和CoDe主要依赖均匀验证或简单的分布对齐，未能充分利用视觉数据的空间异质性不确定性。Lantern虽能加速，但强制所有Token经过云端验证，计算成本高；CoDe在Next-Token范式下存在分布漂移问题，导致生成质量下降。本文切入点在于识别出视觉Token的“空间冗余性”与“边界不确定性”并存特性，提出一种基于连续概率区间的端侧自验证机制，以替代粗粒度的离散熵度量，从而在端侧精准筛选需云端介入的Token。

## 核心方法

### 方法参照系

本文基于云边协同推测解码框架，设备端部署轻量级自回归模型生成Token，云端部署大模型进行验证。与文本SD不同，视觉Token词汇量大且分布扁平，传统LM Head输出的离散概率难以有效量化不确定性，本文引入区间估计替代点估计。

### 区间不确定性量化（Inter-Head）

传统熵度量在大规模视觉码本下失效，因概率分布扁平导致熵值区分度低。本文设计Inter-Head，将输出维度扩展为$2 \times |V|$，分别预测中心logits $\mathbf{c}_t$ 和半径logits $\mathbf{r}_t$，通过Softplus确保半径非负。最终概率区间 $P_t = [p_t^{[l]}, p_t^{[u]}]$ 由InterFuse算子生成，满足 $\sum_i p_i^{[l]} \le 1 \le \sum_i p_i^{[u]}$。该设计将不确定性量化从离散点扩展为连续区间，能更敏感地捕捉空间异质性。

$$
U(P_t) = \Omega_t \cdot \Sigma_t = \|\delta_t\|_1 \cdot \text{std}(\delta_t)
$$

其中 $\delta_t = p_t^{[u]} - p_t^{[l]}$ 为区间宽度向量，$\Omega_t$ 为总模糊体积，$\Sigma_t$ 为置信度差异。该公式表明，仅当总模糊度高且区间宽度方差大时，不确定性得分才高，从而精准定位需云端验证的复杂纹理区域。

### 云端增强解码与分布对齐

端侧生成的Token前缀可能导致云端分布漂移。本文引入Prefix Injection，云端预生成短前缀 $\{y_1, ..., y_m\}$ 引导端侧生成。同时，通过Interval Feature Injection，将端侧区间特征 $\mathbf{f}_t^{[I]}$ 注入云端解码器，约束云端预测分布。训练采用Inter-DRO损失，将下界概率 $q^{[L]}$ 视为最坏情况，通过对抗重加权优化，确保端侧区间估计与云端分布对齐。

$$
\mathcal{L}_{\text{Inter-DRO}} = \mathcal{L}_{\text{anchor}} + \lambda \mathcal{L}_{\text{KL}} + \mathcal{L}_{\text{DRO}}
$$

其中 $\mathcal{L}_{\text{DRO}}$ 对高损失样本赋予更高权重，强化对困难Token的对齐能力，防止端侧置信度虚高导致的错误累积。

## 实验评估

实验在MS-COCO验证集上进行，使用LlamaGen-XL和Anole作为云端模型，端侧模型限制为单层自回归层。基线包括EAGLE-2、Lantern、Entropy-lens、SoftmaxCorr和CoDe。

| 模型 | 方法 | CLIP (↑) | FID (↓) | Speedup | Cloud Call |
| :--- | :--- | :--- | :--- | :--- | :--- |
| LlamaGen (Stage I) | Base | 0.3161 | 23.6900 | x1.00 | 100.00% |
| LlamaGen (Stage I) | Lantern | 0.3159 | 25.5494 | x1.66 | 50.11% |
| LlamaGen (Stage I) | **Ours** | 0.3159 | 24.2459 | **x2.53** | **30.44%** |
| Anole | Base | 0.3215 | 19.9455 | x1.00 | 100.00% |
| Anole | **Ours** | 0.3171 | 23.8593 | **x1.87** | **29.88%** |

在LlamaGen Stage I上，CIAR实现2.53倍加速，云请求率降至30.44%，FID 24.25略高于基线23.69但优于Lantern的25.55。在Anole上，CIAR加速1.87倍，云请求率29.88%，FID 23.86高于基线19.95，显示在复杂模型上质量损失稍大。

消融实验表明，区间量化优于离散熵方法（Entropy-lens FID 24.58 vs CIAR 24.25）。Prefix Injection对初始生成质量至关重要，缺失时FID显著上升。Inter-DRO损失对分布对齐贡献显著，移除后云请求率上升，表明对齐失效导致更多Token需云端验证。

评估边界方面，实验仅在固定分辨率MS-COCO上进行，未测试动态分辨率或高分辨率场景。代码未公开，超参数如阈值0.30的敏感性分析仅在附录提及，缺乏跨数据集泛化验证。

## 关联研究分析

从问题动机看，CIAR与Lantern均针对视觉SD加速，但Lantern采用均匀验证，忽略空间冗余性，导致计算浪费。CIAR通过区间量化实现选择性验证，根源在于视觉Token的空间异质性不确定性，这是文本SD未充分探索的特性。CIAR在云请求率上显著优于Lantern（30.44% vs 50.11%），验证了空间冗余性假设的有效性。

从方法设计看，CIAR与CoDe同属云边协同框架，但CoDe依赖简单分布对齐，在Next-Token范式下易漂移。CIAR引入Inter-DRO和区间特征注入，强化分布对齐，根源在于端侧轻量模型与云端大模型的结构性差异。CIAR在FID上优于CoDe（24.25 vs 35.67），表明区间对齐比简单蒸馏更鲁棒。然而，CIAR未探索多模态统一模型中的跨模态不确定性对齐，其区间量化是否适用于文本-图像交错生成，论文未给出回答。

## 总结

CIAR旨在解决自回归视觉生成在端侧部署时的推理延迟与云端验证开销矛盾。现有方法因忽略视觉Token空间冗余性，导致均匀验证效率低下。CIAR通过Inter-Head连续区间量化不确定性，结合Inter-DRO分布对齐，实现选择性云端验证。实验证明其在LlamaGen上实现2.53倍加速，云请求率降至30.44%，FID保持24.25。其边界在于固定分辨率评估，未验证动态场景下的泛化能力。当图像分辨率动态变化时，区间宽度分布是否保持稳定，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.25463)
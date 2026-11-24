# 卡内基梅隆团队新研究：时空适配器与多头池化

研究机构：美国卡内基梅隆大学、美国匹兹堡大学

作者：Brad Shook、Abby Turner、Jieshi Chen 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.10848)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.10848)

> 通用时间序列基础模型（TSFM）在脑电（EEG）任务上因缺乏空间拓扑建模能力而失效，现有EEG专用基础模型（EEGFM）虽性能强劲但参数量庞大且依赖特定预训练数据。本文切入点在于验证通用TSFM通过轻量级适配器能否替代昂贵的EEG专用预训练。STAMP通过冻结TSFM骨干，利用约0.74M参数的时空适配器重建空间-时间依赖，实现了与SOTA EEGFM相当的性能。其价值在于降低了部署门槛，但绝对性能仍低于大规模EEG专用模型，且未解决高频信号丢失问题。

## 研究背景

当通用TSFM处理单变量时间序列时，其嵌入向量仅包含时间动态信息，丢失了EEG信号中电极间的关键空间拓扑关系。这种空间信息的缺失导致直接应用TSFM进行EEG分类时性能接近随机水平。为解决此问题，需引入空间位置编码与跨通道交互机制，但传统方法往往需要重新训练整个模型或依赖复杂的EEG专用预训练，计算成本高昂。

EEG解码的核心痛点在于信号的非平稳性与个体异质性，早期方法依赖手工特征，泛化能力差。随着深度学习发展，领域转向自监督预训练，LaBraM、CBraMod等EEGFM通过大规模无标签数据学习通用表示，确立了“分词-预训练-微调”范式。然而，这些模型参数量达数百万至数千万，且预训练数据局限于EEG领域，限制了其在资源受限场景下的部署。TSFM在金融、医疗等多领域预训练，具备跨域泛化潜力，但缺乏空间建模能力。本文旨在探索通用TSFM与轻量级适配器的结合，以替代高成本的EEG专用预训练。

## 核心方法

### 方法参照系

本文问题属于下游任务适配中的参数高效适配子类。标准流程为冻结预训练骨干，训练轻量级头。关键差异在于：TSFM骨干仅输出单变量时间嵌入，缺乏空间维度，需通过适配器显式重建空间-时间网格结构，而非直接处理多维输入。

### 时空位置编码与降维

设计动机：TSFM嵌入缺乏空间位置信息，直接聚合导致空间关系丢失。本文在嵌入生成后引入三重可学习位置编码。设TSFM输出嵌入 $E \in \mathbb{R}^{S \times T \times \ell}$，首先通过线性映射 $W$ 降维至 $D$ 维，得到 $E' = E \cdot W$。随后添加token位置嵌入 $p_{ij}$、空间位置嵌入 $s_i$ 和时间位置嵌入 $t_j$，得到修正网格 $\tilde{E}_{ij} = e'_{ij} + p_{ij} + s_i + t_j$。该公式显式标记了每个嵌入在空间-时间网格中的坐标，弥补了单变量嵌入的空间盲区。消融实验表明，仅使用token位置编码或仅使用空间-时间位置编码均不如三者结合，证实了空间-时间解耦编码对EEG建模的必要性。

### Criss-Cross GMLP与多头注意力池化

设计动机：标准Transformer在EEG任务上计算开销大，且未充分利用空间-时间解耦特性。本文采用Criss-Cross Gated MLP (CC-GMLP) 替代Transformer进行token混合。CC-GMLP由 $L$ 个块组成，每个块包含时间门控单元 $g_T(\cdot)$ 和空间门控单元 $g_S(\cdot)$。空间门控单元沿空间维度学习线性映射 $W: \mathbb{R}^S \to \mathbb{R}^S$，实现跨通道信息交互，同时保持时间维度的独立性。这种解耦设计允许模型以参数高效的方式捕获通道间关系，独立于特定信号的时间演化。最终，通过多头注意力池化 (MHAP) 聚合token，公式为 $y = \text{softmax}(W \cdot (\lambda z + (1-\lambda) \hat{e}))$，其中 $z$ 为MHAP聚合向量，$\hat{e}$ 为均值嵌入。MHAP通过查询-键机制学习每个token的重要性权重，避免简单平均池化导致的信号稀释。

## 实验评估

实验在8个EEG基准数据集上进行，包括SHU-MI、PhysioNet-MI、BCIC-IV-2a等。基线覆盖EEG Conformer、ST-Transformer、LaBraM和CBraMod，但缺失NeuroTTT、REVE等最新在线适应或大规模预训练模型。

| 方法 | 参数量 | SHU-MI Balanced Acc. | PhysioNet-MI Balanced Acc. | BCIC-IV-2a Balanced Acc. |
| :--- | :--- | :--- | :--- | :--- |
| EEG Conformer | 0.55M | 0.5900 ± 0.0107 | 0.6049 ± 0.0104 | 0.4696 ± 0.0106 |
| LaBraM | 5.8M | 0.6166 ± 0.0192 | 0.6173 ± 0.0122 | 0.4869 ± 0.0085 |
| CBraMod | 25.5M/46M | 0.6043 ± 0.0069 | 0.6305 ± 0.0017 | 0.4092 ± 0.0221 |
| STAMP | 0.73M/0.78M | 0.5983 ± 0.0096 | 0.6098 ± 0.0084 | 0.5564 ± 0.0212 |

STAMP在BCIC-IV-2a上以0.5564的Balanced Accuracy显著优于CBraMod的0.4092，但在SHU-MI和PhysioNet-MI上略低于LaBraM。这表明STAMP在特定任务上具有竞争力，但整体性能未全面超越EEGFM。

消融实验显示，位置编码从“无PE”到“NST”（token+空间+时间）提升了AUROC，证实了空间-时间解耦编码的有效性。Token混合组件中，CC-GMLP（0.74M参数）性能优于B-TF（1.25M参数）和CC-TF（0.99M参数），表明GMLP在参数效率上优于Transformer。MHAP相比均值池化在多数数据集上表现更优，但提升幅度有限，说明聚合策略对最终性能的影响小于混合策略。

评估协议采用与CBraMod相同的预处理流程（200Hz重采样、噪声滤波），确保可比性。指标包括Balanced Accuracy、AUC-PR、AUROC（二分类）及Cohen’s Kappa、Weighted F1（多分类）。代码开源，使用PyTorch 2.6.0和CUDA 12.4，实验在NVIDIA RTX 2080 Ti GPU上运行。局限在于未报告计算效率指标，且未对比最新SOTA模型如REVE。

## 关联研究分析

从方法设计看，STAMP的CC-GMLP直接受CBraMod的Criss-Cross Transformer (CC-TF) 启发，但将注意力机制替换为门控MLP。这一差异源于参数效率考量：CC-TF在长序列EEG上计算开销大，而GMLP通过线性映射实现跨通道交互，参数量仅为CC-TF的75%。然而，GMLP缺乏Transformer的全局注意力机制，可能在长程依赖建模上存在劣势，论文未验证其在超长序列任务上的表现。

从问题动机看，STAMP与LaBraM代表两条不同路线：LaBraM依赖EEG专用预训练数据学习频谱特征，而STAMP利用通用TSFM的跨域泛化能力。LaBraM在SHU-MI上达到0.6166，STAMP为0.5983，差距约1.8个点。这一差异可能源于TSFM预训练数据中缺乏EEG高频成分，导致频谱偏差。论文未分析TSFM嵌入的频谱特性，也未验证引入频谱平衡损失是否能缩小差距。

## 总结

STAMP旨在解决通用TSFM在EEG任务上因缺乏空间建模能力而失效的问题。其切入点在于利用轻量级适配器重建空间-时间依赖，而非重新预训练。方法核心是三重位置编码与CC-GMLP的组合，实现了约0.74M参数的参数高效适配。实验证明STAMP在BCIC-IV-2a上显著优于CBraMod，但在SHU-MI上略低于LaBraM。边界在于未对比最新SOTA模型，且未分析TSFM嵌入的频谱偏差。当TSFM预训练数据中EEG高频成分占比极低时，STAMP的性能上限是否受限于频谱偏差，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.10848)
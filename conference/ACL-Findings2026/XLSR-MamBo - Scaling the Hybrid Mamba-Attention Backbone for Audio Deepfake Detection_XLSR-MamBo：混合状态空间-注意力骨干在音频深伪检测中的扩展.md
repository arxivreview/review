# ACL-Findings2026最新论文 ｜XLSR-MamBo: Scaling the Hybrid Mamba-Attention Backbone for Audio Deepfake Detection ｜XLSR-MamBo：混合状态空间-注意力骨干在音频深伪检测中的扩展

作者：Kwok-Ho Ng、Tingting Song、Yongdong Wu 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.02944)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.02944)

> 音频深伪检测（ADD）旨在区分真实语音与合成语音，其核心挑战在于生成技术的指数级进步与检测模型泛化能力线性提升之间的不对称性。现有基于Transformer的架构受限于二次计算复杂度，而纯状态空间模型（SSM）虽具备线性复杂度，却缺乏捕捉全局频谱不一致所需的基于内容的精确检索能力。本文提出XLSR-MamBo，通过系统评估四种SSM-Attention混合拓扑及深度缩放，验证了Hydra原生双向建模在开放集场景下的优势。该框架在In-the-Wild基准上显著优于现有SOTA，但其在封闭集上的性能未超越经典方法，且深度缩放对稳定性的影响机制尚需理论解释。

## 研究背景

当检测器面对新生成模型时，其训练域与测试域的数据分布出现系统性差异——这一现象称为分布偏移。分布偏移导致传统分类器决策边界失效，而实际场景中往往能获取少量目标域样本，这恰好构成了小样本学习的条件：仅凭每个类别极少量标注样本泛化到新任务。解决此类问题的经典框架是原型网络，它计算各类别支持样本的特征均值作为"原型"，再通过距离度量完成分类。

音频深伪检测的主流路线已从手工特征转向自监督学习（SSL）骨干，XLS-R等模型通过大规模无标签数据预训练获得通用声学线索，显著提升了跨域鲁棒性。然而，基于Transformer的后端分类器在处理长序列时面临二次计算复杂度瓶颈，限制了其在边缘设备上的部署效率。与此同时，纯SSM架构如Mamba虽解决了效率问题，但其因果性限制使其难以捕捉深伪信号中全局频谱不一致这一关键伪迹。本文切入点在于利用SSM与Attention的互补性，通过混合架构同时捕捉局部高频伪迹与全局频谱不一致，并在深度缩放中寻求稳定性与性能的平衡。

## 核心方法

### 方法参照系

本文问题属于SSL骨干下的架构优化，与标准XLSR-Conformer流程的关键差异在于后端编码器：后者使用标准Transformer层，而本文探索SSM-Attention混合拓扑，旨在以线性复杂度替代二次复杂度，同时保留全局检索能力。

### 混合拓扑设计

在标准Transformer层中，多头自注意力（MHA）与前馈网络（FFN）依次执行。本文提出四种MamBo变体，其中MamBo-3采用交替策略，将Mamba层与Transformer层分离，以评估SSM处理与Attention精炼的独立贡献。设计动机在于解决纯SSM架构在全局检索上的不足，通过引入Attention机制捕捉深伪信号中的全局频谱不一致。MamBo-3的层结构可表示为：

$$
H_{l+1} = \text{Transformer}(H_l) \quad \text{if } l \text{ is even}, \quad H_{l+1} = \text{Mamba}(H_l) \quad \text{if } l \text{ is odd}
$$

该设计将时序压缩与全局关联解耦，避免了单一机制对伪迹捕捉的局限。

### Hydra原生双向建模

标准SSM是因果递归系统，仅利用历史信息。Hydra通过将前向与后向扫描组合参数化为准分离矩阵，实现原生双向处理。其公式定义为：

$$
Y = \text{SS}(X) + \text{shift}(\text{flip}(\text{SS}(X))) + D
$$

其中$\text{SS}(\cdot)$表示状态空间对偶（SSD），$\text{shift}(\cdot)$和$\text{flip}(\cdot)$分别为右移和反转函数，$D$为对角矩阵。这一设计解决了启发式双分支融合的结构冗余问题，使模型能以线性复杂度捕捉整体非因果依赖，更有效地识别违反因果一致性的伪迹。

## 实验评估

实验在ASV19LA上训练，在ASV21LA、ASV21DF、ITW和DFADD上评估，对比基线包括XLSR-Conformer、XLSR-Mamba、Fake-Mamba等SSL骨干方法，但缺失纯手工特征基线（因已淘汰）。主实验结果显示，MamBo-3-Hydra-N3在ASV21LA、ASV21DF和ITW上分别取得0.81%、1.70%和4.97%的EER，其中ITW性能显著优于Fake-Mamba (L)的5.85%。

| 模型 | ASV21LA EER (%) | ASV21DF EER (%) | ITW EER (%) |
| :--- | :--- | :--- | :--- |
| XLSR-Mamba | 0.93 | 1.88 | 6.71 |
| Fake-Mamba (L) | 0.97 | 1.74 | 5.85 |
| MamBo-3-Hydra-N3 | 0.81 | 1.70 | 4.97 |

消融实验表明，深度缩放$N$对性能有显著影响：MamBo-3-Hydra在$N=3$时取得最低EER，而GDN在$N=1$时表现最优，暗示不同SSM变体对深度的敏感性存在差异。这一发现揭示了架构选择与深度配置之间的条件依赖关系，而非简单的“越深越好”。

评估协议采用EER和min t-DCF指标，符合ASVspoof标准，但未报告置信区间，数值比较需谨慎。代码已开源，超参数（如$D=128$，$L=5$）和GPU配置（RTX 4080 Super + 2×RTX 3090）已明确，可复现性较高。

## 关联研究分析

从问题动机看，本文与XLSR-Mamba同属SSM应用路线，但后者依赖手动双向策略（如双分支融合）近似非因果接收性，而本文通过Hydra的准分离矩阵实现原生双向处理。这一差异源于对SSM因果性限制的不同理解：XLSR-Mamba视双向性为结构扩展，本文则视其为数学表达式的自然延伸。从方法设计看，本文与IB-CAAN形成互补：后者通过变分信息瓶颈压缩特征以增强跨域鲁棒性，属数据/正则化驱动；本文则通过架构拓扑搜索优化计算效率，属架构驱动。IB-CAAN在ASV21DF上取得1.83% EER，略逊于本文的1.70%，但其在ITW上的6.48% EER高于本文的4.97%，暗示架构优化在开放集场景下更具优势。

## 总结

本文要解决的核心矛盾是SSM线性复杂度与Attention全局检索能力之间的权衡。现有纯SSM架构因因果性限制无法捕捉全局频谱不一致，而Transformer架构受限于二次复杂度，本文通过混合拓扑设计同时满足两者需求。实验证明MamBo-3-Hydra-N3在ITW上取得4.97% EER，显著优于Fake-Mamba (L)的5.85%，验证了Hydra原生双向建模的有效性。然而，本文在ASV21LA上仅取得0.81% EER，未超越WaveSP-Net的0.13%，暴露了混合架构在封闭集上的性能瓶颈。当支持集增大到5-shot时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.02944)
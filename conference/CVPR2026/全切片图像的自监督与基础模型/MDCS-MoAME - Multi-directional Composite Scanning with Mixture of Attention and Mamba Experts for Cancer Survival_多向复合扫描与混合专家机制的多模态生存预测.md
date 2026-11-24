# CVPR2026最新论文 ｜MDCS-MoAME: Multi-directional Composite Scanning with Mixture of Attention and Mamba Experts for Cancer Survival Prediction ｜多向复合扫描与混合专家机制的多模态生存预测

作者：Linjie Qu、Jin Xiao、Xiangrong Liu 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4fd719e1812f)

> 多模态生存预测旨在融合病理图像与基因组数据以提升癌症预后准确性，但现有方法受限于单一方向扫描导致的长程依赖捕捉不足及模态间异构性建模困难。本文切入点在于通过多方向复合扫描策略扩展感受野，并引入注意力与Mamba混合专家机制动态选择最优交互模式。该方法在五个TCGA数据集上实现了SOTA性能，但其依赖预训练ResNet-50特征提取器且缺乏跨中心鲁棒性验证，限制了其在真实临床场景中的泛化能力评估。

## 研究背景

全切片图像（Whole Slide Image, WSI）包含数十亿像素，直接输入神经网络面临算力瓶颈，而基因组数据则呈现高维稀疏特性。处理WSI时，通常将其划分为区域（Region）与补丁（Patch）层级，利用状态空间模型（State Space Model, SSM）如Mamba以线性复杂度建模长序列依赖，替代传统Transformer的二次方计算开销。然而，现有Mamba方法仅执行水平扫描，导致垂直及斜向的空间关联被忽略，无法充分捕捉组织微环境中的多方向依赖。

多模态生存预测的主流路线包括基于注意力的早期融合（如MCAT）和基于最优传输的跨模态对齐（如MOTCAT），但这些方法在计算效率与长程依赖建模间存在权衡。Mamba-based方法如PAM和SurvMamba虽提升了效率，但受限于单一扫描方向，未能利用WSI的层级结构中的多尺度信息。本文针对这一瓶颈，提出多方向复合扫描（Multi-directional Composite Scanning, MDCS）策略，结合混合专家机制（Mixture of Experts, MoE）以动态适应模态间的复杂关联。

## 核心方法

### 方法参照系

本文问题属于多模态生存预测范畴，标准流程为分别提取病理与基因组特征，通过融合模块交互后预测生存函数。与通用流程的关键差异在于，本文未采用静态融合或单一方向扫描，而是引入多方向序列化策略与动态专家选择，以解决长程依赖与模态异构性难题。

### 多方向复合扫描与特征增强

传统Mamba方法仅对WSI执行水平扫描，导致上下行相邻补丁在序列中距离过远，无法捕捉垂直及斜向依赖。本文在区域与补丁层级引入五种扫描方向：水平（ho）、垂直（ve）、左斜（lo）、右斜（ro）及回环（lb）。对于基因组数据，引入区间扫描（interval scanning）以捕捉稀疏基因组间的潜在关联。扫描后的序列通过Mamba2编码器处理，公式如下：

$$
\overline{I}_r = \{ \text{Norm}(\text{Linear}(\overline{x}_{r,i}^{ho} + \sum_j \overline{x}_{r,\phi^{-1}_{r,j}(i)}^j)) \}_{i=1}^M
$$

该公式通过求和聚合不同方向的Mamba输出，再经线性层与归一化处理，生成增强的模态内表示。这一设计解决了单一方向扫描导致的感受野局限，使模型能同时捕捉局部细节与全局上下文，提升了特征的可区分性。

### 专家驱动跨模态交互

单一注意力或Mamba机制难以充分捕捉WSI与基因组间的异构关联。本文提出混合注意力与Mamba专家（Mixture of Attention and Mamba Experts, MoAME）模块，包含三个专家：交叉注意力（CroAttFusion）、交叉Mamba（CroMamFusion）及堆叠Mamba（StackedMamFusion）。门控网络动态选择专家，公式如下：

$$
F_{1\&2} = \begin{cases} \text{Cross-Attention}(F_1, F_2), & \text{logit}=0 \\ \text{Cross-Mamba}(F_1, F_2), & \text{logit}=1 \\ \text{Cross-Mamba}(F_1, \text{Cross-Mamba}(\mathcal{B}, F_2)), & \text{logit}=2 \end{cases}
$$

该公式通过门控网络输出的logit值选择最优融合策略，其中$\mathcal{B}$为随机初始化特征，用于蒸馏关键信息。这一设计解决了静态融合引入的冗余问题，使模型能灵活聚焦于模态间最具判别力的交互，提升了生存预测的准确性。

## 实验评估

实验在TCGA五个数据集（BLCA, BRCA, GBMLGG, LUAD, UCEC）上进行，采用5折交叉验证，指标为C-index。基线覆盖基因模态（MLP, SNN）、病理模态（ABMIL, PAM）及多模态方法（MCAT, SurvMamba），但缺失最新VLM或智能体导航类基线。

| 模型 | 模态 | LUAD C-index | UCEC C-index |
| :--- | :--- | :--- | :--- |
| MDCS-MoAME | P+G | 0.7079±0.0259 | 0.7263±0.0531 |
| SurvMamba | P+G | 0.6713±0.0230 | 0.6674±0.0391 |
| PAM | P | 0.5674±0.0669 | 0.6382±0.0393 |

MDCS-MoAME在LUAD和UCEC上分别优于SurvMamba 3.66%和5.89%，表明多方向扫描与混合专家机制的有效性。

| 消融项 | LUAD C-index | UCEC C-index |
| :--- | :--- | :--- |
| w/o MDSFE | 0.6695±0.0199 | 0.6752±0.0329 |
| w/o EDIMI | 0.6894±0.0183 | 0.6929±0.0252 |
| w/o Lcro | 0.6864±0.0276 | 0.7143±0.0258 |

移除MDSFE模块导致性能下降最显著（LUAD降5.42%），验证了多方向扫描的核心贡献；移除EDIMI模块降幅较小（LUAD降2.61%），表明跨模态交互的边际收益低于模态内特征增强。

评估仅使用C-index，未报告计算效率或跨中心鲁棒性指标。实验在NVIDIA GTX 4090上进行，超参数如学习率1e-3、batch size 1已披露，但代码未开源，限制了可复现性。

## 关联研究分析

从方法设计看，本文与PAM和SurvMamba同属Mamba-based生存预测路线，但核心差异在于扫描策略。PAM采用双向Mamba，SurvMamba引入层级交互，但均局限于水平或有限方向扫描。本文的五方向复合扫描直接针对WSI的空间结构，而PAM和SurvMamba的单一方向扫描可能遗漏垂直及斜向的组织关联。这一差异源于任务特性：WSI的层级结构要求多尺度信息融合，而单一方向扫描无法充分捕捉这种结构。

从问题动机看，本文与MoME同属混合专家机制应用，但MoME聚焦于模态融合类型的选择（如最大化、间接融合），而本文聚焦于交互机制类型的选择（注意力vs Mamba）。MoME的专家选择基于模态需求，而本文的专家选择基于特征交互的复杂度。这一差异暗示，在异构模态（如稀疏基因组与密集图像）中，交互机制的动态选择可能比融合策略的静态选择更具适应性。

## 总结

本文核心矛盾在于长程WSI依赖捕捉与模态异构性建模的冲突，现有方法因单一方向扫描和静态融合无法同时解决。本文通过多方向复合扫描扩展感受野，结合混合专家机制动态选择交互模式，在TCGA五数据集上实现SOTA，LUAD C-index达0.7079，UCEC达0.7263。其边界在于依赖预训练ResNet-50特征，且未验证跨中心鲁棒性，导致在真实临床场景中泛化能力存疑。当扫描器或染色协议变化时，多方向扫描策略是否仍能保持性能优势，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_4fd719e1812f)
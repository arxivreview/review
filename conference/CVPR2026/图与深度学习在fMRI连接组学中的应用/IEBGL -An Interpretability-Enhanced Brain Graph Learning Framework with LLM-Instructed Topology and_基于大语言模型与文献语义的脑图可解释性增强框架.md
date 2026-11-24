# CVPR2026最新论文 ｜IEBGL:An Interpretability-Enhanced Brain Graph Learning Framework with LLM-Instructed Topology and Literature-Augmented Semantics ｜基于大语言模型与文献语义的脑图可解释性增强框架

研究机构：南京大学

作者：Yihang Duan、Shuo Huang、Li Zhang 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f1de245a93a2)

> 现有基于静息态功能磁共振成像（rs-fMRI）的脑图学习方法依赖统计相关性构建拓扑，导致节点特征缺乏生物学语义，模型预测难以映射至临床知识。IEBGL通过引入大语言模型（LLM）重构拓扑结构，并聚合生物医学文献语义增强节点表征，试图在提升分类精度的同时解决可解释性缺失问题。该框架在REST-meta-MDD和ABIDE数据集上取得了优于多数基线的性能，但其静态功能连接假设与当前动态建模趋势存在张力，且性能未超越领域内最新SOTA。

## 研究背景

rs-fMRI数据经皮尔逊相关系数计算后形成功能连接（Functional Connectivity, FC）矩阵，该矩阵作为图神经网络的输入，其节点特征通常仅为连接强度向量，缺乏脑区功能角色的语义信息。这种纯数值表征导致模型无法区分具有相似连接模式但不同病理机制的脑区，限制了诊断精度与临床可解释性。

主流脑图学习路线通过图神经网络（Graph Neural Networks, GNN）捕捉拓扑依赖，但受限于输入数据的语义贫乏，模型往往被视为黑盒。尽管近期研究尝试引入外部知识，如SK-GNN利用Gumbel-Softmax优化选择关键子图，但多数方法仍未能将文献语义系统性地融入节点表征与拓扑重构过程。IEBGL的切入点在于同时增强拓扑结构与节点语义，通过LLM生成拓扑先验，并通过文献聚合赋予节点临床意义，从而在表征层面实现语义对齐。

## 核心方法

### 方法参照系

标准脑图分类流程将FC矩阵视为邻接矩阵，节点特征为连接向量，直接输入GNN进行分类。IEBGL的关键差异在于在输入GNN前，通过两个独立模块分别重构邻接矩阵和增强节点特征，将外部知识注入图结构本身，而非仅作为辅助特征。

### LLM引导的拓扑重构

针对相关性矩阵缺乏语义先验的问题，LITR模块利用LLM生成脑区关系描述，并通过掩码对比学习优化拓扑。首先，基于AAL图谱为每个脑区设计结构化提示，LLM生成描述性文本并编码为初始节点特征$X_{LLM}$。随后，对原始图进行节点随机掩码和边扰动生成两个视图，输入由两层GCN组成的图自编码器（Graph Auto-Encoder, GAE）。解码器通过双线性映射重构邻接矩阵：

$$ A_{LITR} = \sigma(\tilde{H}_i W \tilde{H}_i^\top) $$

其中$\tilde{H}_i$为掩码后的潜在表示，$W$为可训练参数。该公式通过Sigmoid激活生成权重化的语义拓扑，与原始FC矩阵融合，解决了纯统计相关性无法捕捉脑区功能关联的问题。

### 文献增强的语义聚合

为解决节点特征与文献语义的异构性，LASA模块将脑区特征与文献嵌入投影至统一空间。通过缩放点积注意力计算节点与文献的相似度，选取Top-k相关文献，并引入稀疏约束与熵正则化：

$$ L_{LASA} = \lambda_1 \sum_{i=1}^n \|W_i\|_1 + \lambda_2 \sum_{i=1}^n \left( -\sum_{j=1}^k \tilde{\alpha}_{ij} \log \tilde{\alpha}_{ij} \right) $$

该损失函数平衡了文献关联的稀疏性与多样性，确保每个脑区仅关联少量高相关文献，避免语义噪声。聚合后的文献特征与投影后的节点特征通过MLP融合，生成富含语义的节点表征$X_{LASA}$，使模型预测可追溯至具体医学文献。

## 实验评估

实验在REST-meta-MDD（2,428名受试者）和ABIDE（1,035名受试者）数据集上进行，采用AAL116图谱和5折交叉验证。基线覆盖GCN、BrainGNN、BrainNetTF等经典架构及SK-GNN等知识嵌入方法，但缺失动态功能连接（dFC）专用基线如BrainSTR。

| 数据集 | 方法 | ACC (%) | AUC (%) |
| :--- | :--- | :--- | :--- |
| REST-meta-MDD | IEBGL | 75.00 | 79.45 |
| REST-meta-MDD | SK-GNN | 71.44 | 76.58 |
| ABIDE | IEBGL | 81.43 | 83.92 |
| ABIDE | SK-GNN | 79.22 | 81.48 |

IEBGL在两个数据集上均优于SK-GNN，ACC分别提升3.56%和2.21%。消融实验显示，移除LITR模块导致ACC下降2.91%（MDD），移除LASA模块下降4.87%（MDD），表明文献语义对节点表征的贡献大于拓扑重构。

评估指标包含ACC、AUC、Precision等六项，但未报告计算效率。代码已开源，超参数设置详细（如$\lambda_1=10^{-3}$, $\beta=0.2$），可复现性较高。然而，实验未包含跨站点泛化测试，且未与动态FC方法直接对比，限制了结论的普适性。

## 关联研究分析

从问题动机看，IEBGL与ConceptNeuro同属LLM引导路线，但ConceptNeuro侧重生成临床概念引导GNN，而IEBGL侧重文献聚合增强节点特征。这一差异源于任务特性：ConceptNeuro关注概念层面的可解释性，IEBGL关注文献层面的可追溯性。IEBGL未探索概念生成与文献聚合的协同效应，可能限制了语义深度的挖掘。

从方法设计看，IEBGL采用静态FC输入，与BrainSTR等动态FC方法形成对比。BrainSTR通过时空对比学习捕捉相位变化，在REST-meta-MDD上取得77.2%的ACC，高于IEBGL的75.00%。这一差距暗示静态FC可能不足以捕捉MDD的时变病理机制，而IEBGL的语义增强未能弥补动态信息缺失。查询侧语义增强在数据充足时是否仍有增益，论文未给出回答。

## 总结

IEBGL旨在解决脑图学习中语义缺失导致的可解释性不足问题，通过LLM重构拓扑与文献聚合增强节点特征，实现了预测与医学知识的映射。在REST-meta-MDD上，IEBGL取得75.00%的ACC，优于SK-GNN的71.44%，验证了外部知识注入的有效性。然而，其性能低于动态FC方法BrainSTR的77.2%，暴露了静态FC假设的局限。当支持集增大到5-shot时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_f1de245a93a2)
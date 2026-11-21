# ACL-Findings2026最新论文 ｜MedCPI: A Construct–Personalize–Integrate Framework for KG-enhanced Clinical Prediction ｜任务引导式知识图谱增强临床预测框架

研究机构：英国埃克塞特大学

作者：Hang Wang、Hang Dong、Lu Liu

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_7151df4fd0d7)

> 电子健康记录（EHR）数据稀疏且异构，传统序列模型难以捕捉细粒度临床语义，而直接引入多源医学知识图谱（MKG）又面临Schema噪声与任务无关性干扰。现有方法在知识提取与患者个性化环节缺乏针对性控制，导致弱相关节点稀释预测证据。MedCPI通过“构建-个性化-整合”三阶段框架，利用大语言模型（LLM）进行任务引导的Schema归纳，并实施受控局部扩展构建患者级知识图谱，实现了知识选择与纵向时序的动态对齐。该框架在MIMIC-III/IV上取得了SOTA性能，但其对LLM离线归纳的依赖及跨机构泛化能力仍存疑。

## 研究背景

临床预测模型常受限于EHR数据的不规则采样与高缺失率，导致传统序列模型在捕捉长期依赖时失效。为缓解稀疏性，研究者引入MKG将异构代码映射至共享医学概念，但多源MKG整合了不同粒度的资源，其Schema存在冗余与语义重叠，直接编码会引入大量噪声。此外，现有方法缺乏任务特异性选择，邻域扩展往往检索到弱相关节点，稀释了如糖尿病预测中风险因子等关键证据。

KG增强临床预测已从静态本体层级传播（如GRAM）演进至患者级知识图谱（PKG）推理（如KerPrint、KGxDP）。然而，主流PKG方法仍直接基于原始MKG进行无约束扩展，且知识整合与患者纵向轨迹对齐不足。MedCPI针对这一瓶颈，提出在知识提取前进行任务引导的Schema规范化，并在个性化阶段实施受控局部扩展，旨在解决知识噪声与个性化缺失的双重问题。

## 核心方法

### 方法参照系

标准PKG推理流程直接从原始MKG扩展患者EHR概念，构建全局图并进行注意力编码。本文的关键差异在于前置了“任务引导Schema归纳”与“受控局部扩展”步骤，将知识池从通用多源MKG转化为紧凑的任务特定Concept MKG，并限制了扩展范围以抑制噪声。

### 任务引导Schema归纳与KG规范化

针对多源MKG Schema噪声问题，MedCPI在Construct阶段引入LLM进行任务引导的模式归纳。首先，利用SapBERT嵌入关系文本并进行凝聚聚类，随后由指令微调LLM评估每个簇相对于任务描述 $T_\tau$ 的相关性，分配规范关系名或标记为IGNORE。该过程生成了任务特定的映射函数 $f_\tau: R \rightarrow R_\tau \cup \{IGNORE\}$，将原始关系映射至规范关系集 $R_\tau$ 或丢弃。规范化后的MKG $G_\tau$ 仅保留任务相关三元组，显著降低了后续扩展中的语义噪声。

### 受控PKG构建与时间感知融合

Personalize阶段基于 $G_\tau$ 构建患者级PKG，通过附加EHR概念的一跳邻域及共现概念间的短路径（实验中使用2跳）实现受控扩展，避免无约束邻域引入的弱相关节点。PKG经多层关系图卷积网络（R-GCN）编码，节点表示更新公式为：

$$ h_v^{(l+1)} = \sigma \left( \sum_{r} \sum_{u \in N_r(v)} c_{v,r} W_r^{(l)} h_u^{(l)} + W_0^{(l)} h_v^{(l)} \right) $$

其中 $N_r(v)$ 为关系 $r$ 下的邻居，$c_{v,r}$ 为归一化系数。Integrate阶段采用层级时间感知Transformer（HTT）编码EHR序列，生成时间感知查询 $q_i$，并通过交叉注意力融合PKG节点表示：

$$ c_i = \text{CrossAttn}(q_i, \{h_v^{(L)}\}_{v \in V_{pkg}}) $$

该设计使静态知识整合与纵向临床轨迹动态对齐，解决了此前方法中知识整合与时间上下文脱节的问题。

## 实验评估

实验在MIMIC-III（7,537患者）与MIMIC-IV（100,163患者）上进行，涵盖院内死亡率、30天再入院、T2DM及CAD发病预测。基线覆盖EHR-only（GRU、RETAIN、HiTANet）、静态KG增强（GRAM、KAME）及PKG推理（KerPrint、KGxDP、GraphCare）三类，但未包含多模态融合或LLM协同基线。

| 任务 | 数据集 | 方法 | AUROC | AUPRC |
| :--- | :--- | :--- | :--- | :--- |
| 院内死亡率 | MIMIC-III | MedCPI | 0.713(0.008) | 0.242(0.018) |
| 院内死亡率 | MIMIC-III | GraphCare | 0.691(0.003) | 0.224(0.019) |
| 院内死亡率 | MIMIC-IV | MedCPI | 0.809(0.006) | 0.182(0.012) |
| T2DM发病 | MIMIC-III | MedCPI | 0.798(0.002) | 0.425(0.006) |
| T2DM发病 | MIMIC-III | KGxDP | 0.772(0.003) | 0.411(0.008) |
| CAD发病 | MIMIC-IV | MedCPI | 0.797(0.001) | 0.418(0.003) |
| CAD发病 | MIMIC-IV | GraphCare | 0.772(0.004) | 0.401(0.004) |

MedCPI在所有任务上均优于最强基线GraphCare，尤其在T2DM预测中AUROC提升显著，验证了任务特定知识选择对稀疏数据场景的价值。消融实验表明，Construct阶段的Schema归纳与Personalize阶段的受控扩展均对性能有正向贡献，但论文未量化LLM归纳对最终AUROC的具体边际收益。

评估协议采用8:1:1患者划分，报告5次随机种子的均值与标准差，指标完备。代码已开源，但实验仅在单机构数据上进行，未涉及跨机构分布偏移测试。LLM Schema归纳为离线过程，其计算成本与在线推理效率的平衡未在实验中体现。

## 关联研究分析

从知识提取机制看，MedCPI与KerPrint、KGxDP等PKG推理方法的核心差异在于知识池的来源与筛选策略。KerPrint直接基于原始MKG进行全局图注意力，而MedCPI通过LLM归纳任务特定Schema，将知识池从通用多源MKG压缩为紧凑的Concept MKG。这一差异源于多源MKG的Schema噪声问题，MedCPI通过前置去噪步骤解决了无约束扩展导致的弱相关节点稀释证据问题，但LLM归纳的准确性依赖于提示工程与聚类质量，其临床有效性缺乏标准化评估。

从时序整合方式看，MedCPI与HiTANet共享HTT编码器，但知识整合机制不同。HiTANet仅处理EHR序列，而MedCPI通过交叉注意力将静态PKG表示与时间感知EHR查询融合。这一设计解决了此前方法中知识整合与纵向轨迹脱节的问题，但交叉注意力的计算复杂度随PKG节点数线性增长，在长序列或大规模知识池场景下的效率未经验证。

## 总结

MedCPI针对KG增强临床预测中知识噪声与个性化缺失的矛盾，通过LLM引导的任务特定Schema归纳与受控PKG构建，实现了知识选择与纵向时序的动态对齐。实验显示其在MIMIC-III/IV的T2DM预测中AUROC达0.798，院内死亡率达0.809，优于GraphCare等基线。然而，其依赖离线LLM归纳Schema，且仅在单机构数据上验证，跨机构泛化能力与LLM归纳的临床有效性未获证实。当支持集增大或任务分布偏移时，任务特定Concept MKG的泛化边界如何，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_7151df4fd0d7)
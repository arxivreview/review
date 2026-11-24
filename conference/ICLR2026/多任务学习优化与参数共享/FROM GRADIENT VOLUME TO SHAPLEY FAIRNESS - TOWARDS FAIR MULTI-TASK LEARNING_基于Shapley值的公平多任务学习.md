# ICLR2026最新论文 ｜FROM GRADIENT VOLUME TO SHAPLEY FAIRNESS: TOWARDS FAIR MULTI-TASK LEARNING ｜基于Shapley值的公平多任务学习

研究机构：北京大学

作者：Xiao Wang、Yuying Han、Dazi Li 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_76118913)

> 多任务学习（MTL）中任务级优化不公平导致弱任务性能持续退化，现有梯度平衡方法仅依赖成对余弦相似度或启发式加权，无法量化任务子集对整体梯度的全局贡献。SVFair将Shapley值引入MTL优化，通过Gram矩阵行列式体积度量任务子集的几何冲突，单次训练路径下计算公平权重并引导聚合梯度收敛至Pareto平稳点。该方法在NYUv2上实现$\Delta_m\%$ -8.81，优于PIVRG的-6.50，但缺乏分布外泛化验证，其公平性优势在OOD场景下是否成立仍存疑。

## 研究背景

当共享参数同时优化多个异质任务时，任务梯度方向冲突导致部分任务主导更新方向，其余任务反复被牺牲，这一现象称为任务级优化不公平。不公平不仅降低最弱任务性能，更在安全关键应用中破坏MTL的可靠性。解决该问题的核心在于量化每个任务梯度对整体更新方向的偏离程度，但现有方法仅能捕捉成对关系，无法反映任务子集与其余任务的集体交互结构。

主流梯度平衡方法如PCGrad通过投影消除成对冲突分量，Nash-MTL基于帕累托谈判求解均衡点，FairGrad利用性能下降加权高阶信息。这些方法在任务数较少时有效，但面临两个瓶颈：一是成对指标（余弦相似度、内积）无法扩展至数十个任务的全局冲突建模；二是Shapley值虽能精确量化边际贡献，但其指数复杂度$O(2^N)$阻碍了实际部署。SVFair的切入点在于设计一种几何冲突度量，使其既满足Shapley值所需的集合函数形式，又能在单次训练路径下高效计算，从而将理论公平性与计算可扩展性统一。

## 核心方法

### 梯度聚合参照系

MTL梯度聚合的标准流程是求解权重向量$\alpha$，使聚合梯度$d = \sum_{i=1}^N \alpha_i g_i$在约束条件下最小化加权损失。现有方法如FairGrad通过性能下降$\Delta_m$计算权重，但需对每个任务子集进行完整训练，复杂度为$O(C \cdot 2^N)$。SVFair的关键差异在于将权重计算与训练解耦，通过几何度量替代性能指标，实现单次训练路径下的公平权重求解。

### VolDet与VolDetPro几何冲突度量

VolDet将任务子集$S$的冲突量化为归一化梯度张成的平行六面体体积，即Gram子矩阵$M_S$的行列式：

$$v(S) := \text{Vol}^2(S) = \det(M_S)$$

该公式的物理含义是：梯度方向越分散，体积越大，冲突越强；梯度对齐时体积趋近于零。VolDetPro在此基础上引入符号感知惩罚，仅当Gram子矩阵严格上三角存在负余弦对时激活：

$$v_{\text{Pro}}(S) = \det(M_S) + \sqrt{|I(S)|} \sum_{(i,j) \in I(S)} |(M_S)_{ij}|$$

其中$I(S)$为负相似对索引集。这一设计解决了纯体积度量的符号盲点：当两个子集具有相同体积但一个包含钝角冲突时，VolDetPro能区分出更强的对抗性，避免将有益多样性误判为冲突。

### Shapley值公平聚合

SVFair将VolDet/VolDetPro作为Shapley值的效用函数，计算每个任务$i$的边际贡献$\phi_i$，进而构造温度加权权重$\omega_i = \frac{\exp(\phi_i/\tau)}{\sum_{j=1}^N \exp(\phi_j/\tau)}$。聚合梯度通过KKT条件求解：

$$d^* = \arg\min_d \sum_{i=1}^N \omega_i \ell_i(\theta - \eta d) \quad \text{s.t.} \quad \|d\| \leq \epsilon, \; g_i^\top d > 0$$

该公式确保更新方向在所有任务损失均下降的约束下，最大化Shapley加权的高阶信息。理论证明表明，在梯度线性独立假设下，该过程收敛至Pareto平稳点，且单次训练路径下Shapley值计算复杂度降至$O(C)$，其中$C$为单次训练成本。

## 实验评估

实验覆盖NYUv2（3任务）、Cityscapes（2任务）、Office-31（3任务）、CelebA（40任务）及MT10（10任务RL），基线包括PCGrad、CAGrad、Nash-MTL、FAMO、FairGrad、PIVRG等主流梯度方法，但缺失TSBN、CORE-MTL等结构解耦方法。

| 方法 | NYUv2 MR↓ | NYUv2 $\Delta_m\%$↓ | Cityscapes $\Delta_m\%$↓ |
|---|---|---|---|
| PIVRG | 3.56 | -6.50 | -0.45 |
| FairGrad | 10.56 | -4.66 | 8.13 |
| SVFair(VolDet) | 1.44 | -8.81 | -2.08 |
| SVFair(VolDetPro) | 2.22 | -8.29 | -2.40 |

SVFair在NYUv2上MR 1.44、$\Delta_m\%$ -8.81，显著优于PIVRG（MR 3.56、$\Delta_m\%$ -6.50）和FairGrad（MR 10.56、$\Delta_m\%$ -4.66），表明Shapley公平权重在密集预测任务上有效缓解了任务不平衡。Cityscapes上SVFair(VolDetPro) $\Delta_m\%$ -2.40优于PIVRG的-0.45，验证了符号感知惩罚在深度估计任务中的增益。

消融实验显示温度参数$\tau$对性能影响显著：Cityscapes和CelebA上$\tau=5.0$最优（$\Delta_m\%$ -2.16和-0.10），Office-31上$\tau=0.5$最优（$\Delta_m\%$ -1.49）。VolDetPro在Office-31（PNCP>0.25）优于VolDet，在CelebA（PNCP<0.25）则VolDet更稳定，证实了符号惩罚的适用性依赖于负余弦对比例。蒙特卡洛采样$K=1000$时，CelebA上Shapley值MSE为$1.28 \times 10^{-5}$，单epoch运行时间870秒，与FairGrad的810秒相当，计算开销可接受。

评估边界存在明显局限：论文未报告NYUv2的mIoU绝对值，仅通过MR和$\Delta_m\%$间接反映性能，无法确认公平性优化是否以牺牲绝对精度为代价；未测试OOD场景，无法验证Shapley公平权重在分布偏移下的鲁棒性；代码虽在补充材料中提供，但未公开超参数搜索细节，可复现性依赖作者实现。

## 关联研究分析

从问题动机看，SVFair与Nash-MTL均追求公平，但Nash-MTL基于帕累托谈判均衡，强调所有任务损失均不增加，而SVFair基于Shapley边际贡献，量化每个任务对整体梯度的偏离程度。这一差异源于对"公平"的定义不同：Nash-MTL关注结果均衡，SVFair关注过程贡献。在任务高度不平衡时，Shapley值能更精确识别"搭便车"任务，但Nash-MTL在计算效率上更优，且无需求解Shapley值的近似问题。

从方法设计看，SVFair与PCGrad同属梯度冲突消解路线，但PCGrad仅处理成对冲突，通过投影消除有害分量，而SVFair通过集合级几何度量捕捉全局冲突结构。PCGrad的$O(N^2)$复杂度在CelebA（40任务）上难以扩展，SVFair的单次训练路径设计解决了这一瓶颈。然而，SVFair依赖梯度线性独立假设，在Pareto平稳点附近该假设失效，此时$d$无法表示为任务梯度的线性组合，收敛性保证是否仍成立，论文未给出回答。

## 总结

SVFair要解决的核心矛盾是Shapley值理论公平性与计算可扩展性之间的张力。现有方法如FairGrad依赖性能下降加权，需对每个子集完整训练，复杂度指数增长；PCGrad等成对方法无法建模全局冲突结构。SVFair通过VolDet/VolDetPro几何度量将Shapley值计算解耦于训练过程，单次路径下实现$O(C)$复杂度，并在NYUv2上实现$\Delta_m\%$ -8.81，优于PIVRG的-6.50。其边界在于：实验仅覆盖ID场景，未验证OOD泛化；NYUv2未报告mIoU绝对值，公平性优化是否牺牲精度存疑；梯度线性独立假设在Pareto平稳点附近失效，收敛性保证的适用边界未明确。当任务数扩展至百级且梯度接近线性相关时，VolDet的行列式计算是否仍保持数值稳定性，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_76118913)
# AAAI2026最新论文 ｜FedAdamW: A Communication-Efficient Optimizer with Convergence and Generalization Guarantees for Federated Large Models ｜联邦AdamW优化器

研究机构：天津大学、西安电子科技大学

作者：Junkang Liu、Fanhua Shang、Hongying Liu 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.27486)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.27486)

> 联邦学习（FL）中直接应用AdamW优化器会因数据异质性导致二阶矩估计方差激增、客户端漂移加剧及动量状态频繁重置，阻碍Transformer模型的高效协同训练。现有联邦自适应优化算法多基于Adam设计，未充分适配AdamW的解耦权重衰减特性，且在Transformer架构上缺乏针对性验证。本文提出FedAdamW，通过块级二阶矩均值聚合与全局更新校正机制，在无需梯度异质性假设下实现线性加速收敛。该方法在视觉与语言Transformer上显著降低通信轮次并提升精度，但其块级聚合策略在极端非独立同分布（Non-IID）场景下的细粒度自适应能力仍存疑。

## 研究背景

联邦学习（FL）旨在解决数据孤岛与隐私保护约束下的分布式模型训练问题，其核心挑战在于客户端数据非独立同分布（Non-IID）导致的客户端漂移与聚合失效。在Transformer架构中，查询（Query）、键（Key）、值（Value）等组件对学习率的敏感度差异显著，随机梯度下降（SGD）的固定步长难以适配这种复杂的曲率结构，导致收敛缓慢。自适应优化器如AdamW通过维护一阶和二阶矩估计实现动态步长调整，并采用解耦权重衰减改善泛化，在集中式训练中表现优异，但直接迁移至联邦场景会引发二阶矩估计方差失控与局部过拟合。

主流联邦自适应优化算法如FedAdam和FedLADA主要基于Adam设计，通过服务器端聚合一阶或二阶矩来稳定训练，但这些方法未考虑AdamW解耦权重衰减对泛化误差的影响，且实验多局限于卷积神经网络（CNN）。SCAFFOLD引入控制变量校正客户端漂移，但通信开销较大且未针对Transformer的Hessian块结构优化。本文切入点在于识别AdamW在联邦场景下的三个特有失效模式：二阶矩高方差、局部过拟合导致的客户端漂移、以及每轮重置动量状态造成的收敛延迟，并基于Transformer参数的近似块对角Hessian结构，设计通信高效的块级聚合策略与全局更新校正机制。

## 核心方法

### 联邦自适应优化参照系

联邦自适应优化的标准流程是客户端本地执行自适应更新，服务器聚合优化器状态（如一阶矩$m$或二阶矩$v$）以抑制异质性影响。本文问题与该通用流程的关键差异在于：针对AdamW的解耦权重衰减特性，需同时处理二阶矩方差抑制与客户端漂移校正，且聚合策略需适配Transformer参数的块对角Hessian结构，而非全参数级聚合。

### 块级二阶矩均值聚合

针对二阶矩估计$v$在Non-IID数据下方差过高的问题，本文利用Transformer参数Hessian矩阵的近似块对角结构，将$v$划分为$B$个语义对齐的块（如注意力头、MLP层），仅传输每块的均值至服务器。该设计动机在于避免全参数级$v$聚合带来的双倍通信开销，同时保留块内自适应步长信息。聚合公式为：

$$\bar{v}^{[r]} = \frac{1}{S} \sum_{i \in S} \text{mean}(v_i^{[r,K]})$$

其中$S$为参与客户端数，$v_i^{[r,K]}$为客户端$i$在第$r$轮第$K$步的二阶矩估计。服务器将$\bar{v}^{[r]}$广播回客户端作为下一轮$v$的初始化值，而非重置为零，从而保留跨轮次的自适应统计信息，减少收敛延迟。

### 全局更新校正与解耦权重衰减

针对AdamW加速局部过拟合导致的客户端漂移，本文在本地更新规则中引入全局更新估计$\Delta_G^{[r]}$作为校正项，并强化解耦权重衰减。该设计动机在于通过全局方向约束抑制局部最优偏离，同时利用解耦权重衰减改善泛化。本地更新公式为：

$$x_i^{[r,k+1]} = x_i^{[r,k]} - \eta \left( \frac{m_i^{[r,k]}}{\sqrt{v_i^{[r,k]}} + \epsilon} - \lambda x_i^{[r,k]} + \alpha \Delta_G^{[r]} \right)$$

其中$\alpha$为校正强度，$\lambda$为权重衰减系数。$\Delta_G^{[r]}$由服务器基于客户端参数差值计算，$\alpha=0.5$时平衡局部自适应性与全局一致性，显著降低客户端漂移幅度。

## 实验评估

实验在CIFAR-100、Tiny ImageNet及GLUE基准（SST-2、QQP等）上进行，使用ResNet-18、ViT-Tiny、Swin Transformer及RoBERTa-Base（LoRA微调），数据划分采用Dirichlet分布（Dir-0.6/0.1/0.8）。基线覆盖FedAvg、SCAFFOLD、FedCM、FedAdam、FedLADA及本地Adam/AdamW，但缺失FedPA-LoRA、FedTreeLoRA等当前LoRA聚合SOTA方法，无法直接对比联邦LLM微调的整体性能上限。

| 方法 | CIFAR-100 (ResNet-18, Dir-0.6) Acc | CIFAR-100 (ViT-Tiny, Dir-0.1) Acc | GLUE Avg (RoBERTa-Base) |
|---|---|---|---|
| FedAvg | 64.08±0.18 | 27.14±0.12 | 77.68±0.17 |
| FedAdam | 63.77±0.13 | 23.49±0.15 | 78.32±0.16 |
| FedLADA | 65.07±0.18 | 23.18±0.15 | 77.17±0.17 |
| Local AdamW | 62.84±0.08 | 35.33±0.16 | 78.91±0.15 |
| FedAdamW | 66.12±0.10 | 39.86±0.16 | 81.79±0.14 |

FedAdamW在视觉与语言任务上均取得最优精度，GLUE平均准确率81.79%较FedAvg提升4.11个百分点，验证了块级聚合与全局校正的有效性。消融实验显示，移除二阶矩聚合（A1）导致精度下降2.35个百分点，移除全局校正（A2）下降2.44个百分点，表明两者对抑制方差与漂移均不可或缺。权重衰减$\lambda=0.01$时泛化最优，符合PAC-Bayes理论预测的$\lambda$对泛化误差的权衡作用。

评估边界方面，论文未报告通信轮次收敛曲线细节，仅给出总通信量（如ViT-Tiny Dir-0.1下FedAdamW为1×，SCAFFOLD为2×）；GLUE实验仅使用20客户端、20%参与率，未覆盖极端Non-IID（如Dir-0.05）场景；代码已开源，但超参数搜索范围未完全披露，可复现性依赖附录细节。

## 关联研究分析

从问题动机看，FedAdamW与FedLADA均聚焦联邦自适应优化，但FedLADA基于Adam设计，仅聚合二阶矩以稳定训练，未处理解耦权重衰减对泛化的影响，且实验限于CNN。FedAdamW针对Transformer的Hessian块结构设计块级聚合，并引入全局更新校正，解决了AdamW在联邦场景下的客户端漂移问题，这是FedLADA未覆盖的失效模式。差异根源在于Transformer参数的曲率结构比CNN更复杂，需要更精细的聚合粒度与漂移校正机制。

从方法设计看，FedAdamW的全局更新校正机制与SCAFFOLD的控制变量思想类似，但SCAFFOLD通过服务器维护控制变量校正客户端梯度偏差，通信开销较大；FedAdamW直接利用客户端参数差值估计全局更新，通信量更低，且针对二阶矩方差设计块级聚合，而非全参数级校正。与FedMomentum相比，后者保留LoRA训练动量以维持优化状态连续性，而FedAdamW保留二阶矩均值以抑制方差，两者均关注优化器状态保留，但作用对象与机制不同。FedMomentum针对LoRA因子聚合，FedAdamW针对优化器状态聚合，前者解决聚合不匹配，后者解决自适应步长失效。

## 总结

FedAdamW解决的核心矛盾是AdamW在联邦Transformer训练中因数据异质性导致的二阶矩方差失控与客户端漂移，现有方法如FedAdam未适配解耦权重衰减，SCAFFOLD通信开销大。本文基于Transformer Hessian块结构，提出块级二阶矩均值聚合与全局更新校正机制，在无需梯度异质性假设下实现线性加速收敛。实验证明其在GLUE基准上达到81.79%平均准确率，较FedAvg提升4.11个百分点，通信量与FedAvg相当。但论文实验未覆盖极端Non-IID场景（如Dir-0.05），且块级聚合在细粒度自适应能力上的表现未充分验证。当客户端数据分布差异极大时，块级均值是否仍能保留足够的局部曲率信息以维持自适应步长精度，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.27486)
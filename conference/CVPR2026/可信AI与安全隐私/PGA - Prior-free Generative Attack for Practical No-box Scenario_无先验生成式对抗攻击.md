# CVPR2026最新论文 ｜PGA: Prior-free Generative Attack for Practical No-box Scenario ｜无先验生成式对抗攻击

研究机构：西北工业大学

作者：Hongyu Peng、Xiang Yuan、Gong Cheng

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b82b333315fc)

> 可迁移对抗攻击旨在解决黑盒场景下攻击者无法获取目标模型参数时的安全威胁，但现有生成式攻击严重依赖大规模标注数据与预训练代理模型，这在信息稀缺的实际部署中难以成立。本文切入点在于提出首个适用于“实际无盒场景”（Practical No-box Scenario, PNS）的生成式攻击框架，通过自监督代理学习与区域感知扰动生成，在仅4000张无标签图像下实现高效迁移。该框架通过课程引导的微鲁棒优化与区域一致性正则，解决了数据稀缺下的特征坍缩与空间碎片化问题。其价值在于填补了PNS下生成式攻击的空白，但自监督代理的特征上限是否受限于无标签数据规模，仍存疑。

## 研究背景

当攻击者无法访问目标模型参数且缺乏大规模标注数据时，传统基于预训练代理的迁移攻击失效。这一困境源于两个核心约束：一是代理模型过拟合，即迭代优化易使对抗样本收敛于特定模型的局部尖锐极值，导致跨模型迁移成功率低下；二是生成式攻击的数据依赖，现有方法如BIA、CDA需依赖预训练代理的决策层输出或中间特征进行强监督，而在PNS中，攻击者仅能获取少量无标签图像，无法提供此类监督信号。

可迁移对抗攻击的主流路线分为迭代优化与生成式优化两类。迭代优化方法如MI-FGSM通过动量累积解决局部最优，但在PNS下推理速度慢且迁移性有限；生成式方法如GAP、BIA通过训练生成器实现一步推理，效率高但依赖预训练代理。2024年至2026年，研究焦点转向“异构架构间的频谱/语义偏差”及“真实世界鲁棒性”，但多数工作仍假设预训练代理可用。本文的切入点在于，在完全缺乏预训练代理与标注数据的PNS设定下，探索生成式攻击的潜力，通过从零训练自监督代理与改进生成器训练策略，突破传统生成式攻击的信息依赖瓶颈。

## 核心方法

### 方法参照系

本文问题属于生成模型潜空间攻击的变体，但关键差异在于不优化预训练生成器的潜空间，而是训练一个像素空间生成器直接映射干净图像到对抗样本。标准生成式攻击流程依赖预训练代理提供监督信号，而本文在PNS下需先构建一个无标签自监督代理，再训练生成器，且需解决数据稀缺导致的特征坍缩与扰动碎片化问题。

### 课程引导微鲁棒优化（CMRO）

设计动机：传统自监督方法如SimSiam在有限数据下特征空间严重受限，嵌入坍缩至窄分布，导致代理模型判别性不足，无法为生成器提供有效监督。CMRO通过渐进式引入微鲁棒目标，缓解特征坍缩。具体地，给定无标签图像 $x$，生成两个全局视图 $x_{g1}, x_{g2}$ 和 $L$ 个局部视图 $\{x_{li}\}_{i=1}^L$。代理模型 $f_s$ 编码各视图，经投影头 $g(\cdot)$ 和预测器 $q(\cdot)$ 得到表示。对称相似度损失定义为：

$$
\ell_{\mathrm{sim}}(v,u) = \frac{1}{2}\left[ -\mathrm{sim}\left(\boldsymbol{p}^{(v)}, \operatorname{sg}[\boldsymbol{z}^{(u)}]\right) -\mathrm{sim}\left(\boldsymbol{p}^{(u)}, \operatorname{sg}[\boldsymbol{z}^{(v)}]\right) \right]
$$

其中 $\mathrm{sim}(\boldsymbol{a},\boldsymbol{b}) = \frac{\boldsymbol{a}^\top \boldsymbol{b}}{\|\boldsymbol{a}\|_2\,\|\boldsymbol{b}\|_2}$。从第 $T$ 个epoch起，对全局视图 $x_{g1}$ 施加微鲁棒扰动 $\tilde{x}_{g1} = \mathrm{Proj}_{[0,1]}\left( x_{g1} + \tau \,\mathrm{sign}\left( \nabla_{x_{g1}} \mathcal{L}_{\mathrm{cle}}^{S} \right) \right)$，$\tau$ 从0线性增至 $\tau_{\max}$。最终目标为：

$$
\mathcal{L}^{S}_{\mathrm{tot}} = (1 - \lambda_t)\,\mathcal{L}^{S}_{\mathrm{cle}} + \lambda_t\,\mathcal{L}^{S}_{\mathrm{rob}}, \quad \lambda_t = \begin{cases} 0, & t < T\\ 0.5, & t \ge T \end{cases}
$$

该公式表明，训练初期仅优化干净视图对齐，后期引入扰动视图对齐，渐进式暴露模型于鲁棒性目标，避免直接扰动导致的模型坍缩。

### 区域感知一致扰动学习（RCPL）

设计动机：现有生成式攻击在PNS下缺乏强监督，易产生空间碎片化、覆盖不足的扰动，陷入局部最优。RCPL通过区域级特征分离与跨区域一致性正则，引导生成器产生细粒度、空间连贯的扰动。生成器 $G$ 输出对抗样本 $x^{\mathrm{adv}} = \mathrm{Proj}_{[0,1]}\left( x + \mathrm{Clip}_{[-\epsilon,\epsilon]}\left(G(x) - x\right) \right)$。全局特征相似度损失为：

$$
\mathcal{L}^{G}_{\mathrm{ori}} = \mathrm{sim}\left( f_s^j(x^{\mathrm{adv}}), f_s^j(x) \right)
$$

将图像划分为 $K$ 个非重叠区域，区域级损失为：

$$
\mathcal{L}^{G}_{\mathrm{reg}} = \frac{1}{K}\sum_{k=1}^{K} \mathrm{sim}\left( f_s^j(x^{\mathrm{adv}}_k), f_s^j(x_k) \right)
$$

跨区域一致性损失通过Gram矩阵的Frobenius距离计算：

$$
\mathcal{L}^{G}_{\mathrm{cro}} = \frac{2}{K(K-1)} \sum_{k'<k''} \|\mathbf{Gram}_{k'} - \mathbf{Gram}_{k''}\|_F^2
$$

最终目标为 $\mathcal{L}^{G}_{\mathrm{tot}} = \mathcal{L}^{G}_{\mathrm{ori}} + \alpha \mathcal{L}^{G}_{\mathrm{reg}} + \gamma \mathcal{L}^{G}_{\mathrm{cro}}$，其中 $\alpha=\gamma=1.0$。该设计通过区域级特征分离鼓励细粒度扰动，跨区域一致性正则确保扰动空间平滑，缓解生成器在监督不足下的局部最优陷阱。

## 实验评估

实验在ImageNet和MS COCO上进行，使用4000张无标签图像训练，扰动预算 $\epsilon=16$。基线覆盖PNS迭代攻击（PNAA, ETF, CDTA, AGS）和生成式攻击（CDA, GAPF, BIA, FACL），但缺失最新SOTA如Season、AdvFM（因协议不同）。主结果显示，PGA在ImageNet跨模型攻击中AVGc 71.39%、AVGv 47.50%，显著优于最强PNS基线AGS（AVGc 50.26%、AVGv 31.39%）和生成式基线BIA（AVGc 54.18%、AVGv 32.95%）。

| 方法 | AVGc (%) | AVGv (%) |
| --- | --- | --- |
| AGS | 50.26 | 31.39 |
| BIA | 54.18 | 32.95 |
| FACL | 54.38 | 33.08 |
| PGA | 71.39 | 47.50 |

消融实验表明，区域数 $K=4$ 时性能最优（AVGc 71.39%、AVGv 47.50%），$K=9$ 时AVGv下降至42.29%，提示区域划分过细可能引入噪声。微鲁棒强度 $\tau_{\max}=0.01$ 且起始epoch $T=200$ 时效果最佳，过早或过强扰动导致性能下降。

| K | AVGc (%) | AVGv (%) |
| --- | --- | --- |
| 1 | 65.44 | 43.31 |
| 2 | 68.96 | 45.01 |
| 4 | 71.39 | 47.50 |
| 9 | 67.52 | 42.29 |

评估边界：论文未报告置信区间，数值比较需谨慎；代码未公开，可复现性受限；超参数（如 $T=200$, $\tau_{\max}=0.01$）基于ImageNet调优，跨域泛化性未充分验证。

## 关联研究分析

从问题动机看，本文与BIA、CDA等生成式攻击的核心差异在于信息依赖。BIA依赖预训练代理的中间特征进行监督，而本文在PNS下从零训练自监督代理，通过CMRO缓解特征坍缩。这一差异源于任务特性：PNS假设攻击者无法获取预训练模型，迫使方法转向无标签自监督。然而，自监督代理的特征分布与预训练代理存在本质差异，论文通过KDE可视化显示其更接近标准预训练模型，但未量化这种差异对迁移上限的影响。

从方法设计看，本文与AGS等PNS迭代攻击的差异在于推理效率与扰动结构。AGS使用MI-FGSM迭代优化，推理慢且扰动易过拟合；本文通过生成器一步推理，且RCPL引入区域一致性正则，确保扰动空间连贯。这一设计解决了生成式攻击在数据稀缺下的空间碎片化问题，但区域划分 $K=4$ 是否针对特定分辨率优化，泛化性如何，论文未给出回答。

## 总结

本文要解决的核心矛盾是生成式攻击在PNS下因缺乏预训练代理与标注数据而失效的问题。切入点在于，通过CMRO渐进式引入微鲁棒目标缓解自监督特征坍缩，通过RCPL区域一致性正则解决扰动空间碎片化，从而在无先验信息下实现高效迁移。实验证明，PGA在ImageNet跨模型攻击中AVGc 71.39%、AVGv 47.50%，显著优于PNS基线。边界在于，自监督代理的特征上限受限于4000张无标签图像，且区域划分参数 $K$ 的泛化性未充分验证。当支持集增大到更大规模时，CMRO的课程学习策略是否仍必要，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_b82b333315fc)
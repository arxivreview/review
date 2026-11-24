# WACV2026最新论文 ｜Scalpel: Fine-Grained Alignment of Attention Activation Manifolds via Mixture Gaussian Bridges to Mitigate Multimodal Hallucination ｜基于高斯混合桥的注意力激活流形对齐

作者：Ziqiang Shi、Rujie Liu、Shanshan Yu 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.09541)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.09541)

> 大视觉语言模型（LVLMs）在生成文本时，常因语言先验压制视觉信号而产生对象幻觉，现有推理时干预方法多依赖全局对比或固定向量校正，难以处理同一注意力头内不同token的异质性偏差。Scalpel指出，幻觉源于特定注意力头中激活分布向“可信流形”的偏离，且这种偏离具有组件级（component-level）的几何结构。该方法通过高斯混合模型（GMM）建模可信与幻觉激活分布，利用Schrödinger桥理论计算最优传输映射，实现token级的动态校正。这一设计在POPE基准上超越了基于固定向量的ICT方法，但其离线预计算开销与GMM组件数的敏感性仍存疑。

## 研究背景

当LVLMs处理模糊视觉输入时，模型倾向于依赖预训练LLM中的统计共现规律而非视觉证据，导致生成不存在的物体。这种偏差并非均匀分布于所有Transformer层，而是集中在少数对视觉信号敏感的注意力头中。然而，现有推理时干预方法如VCD（Visual Contrastive Decoding）通过对比原始与扰动图像的logits分布来抑制幻觉，其核心假设是偏差在解码层面是全局一致的，忽略了内部激活空间的几何结构差异。

主流缓解路线分为训练时对齐与推理时干预两类。训练时方法如DPO依赖高质量标注数据，成本高昂且泛化性受限；推理时方法虽免训练，但VCD等对比解码策略需额外前向传播，引入显著延迟，且OPERA等注意力重加权方法采用固定惩罚项，无法适应不同token的偏差强度。Scalpel的切入点在于发现：同一注意力头内，不同token的激活偏离可信流形的方向与幅度存在显著差异，固定向量校正会导致部分token过度校正或校正不足。

## 核心方法

### 方法参照系

Scalpel属于推理时表征空间编辑路线，其参照系为ICT（Inference-time Calibration）。ICT通过逻辑回归探针识别关键注意力头，并施加固定校正向量将激活拉向可信区域。本文与ICT的关键差异在于：ICT假设每个头内的偏差方向一致，而Scalpel认为偏差分布是多峰的，需根据当前token所属的分布组件动态调整校正方向与强度。

### 基于GMM的流形建模与最优传输

Scalpel首先对可信与幻觉激活分别拟合GMM，以捕捉多峰分布结构。对于幻觉GMM的第$i$个组件$N(\mu_0^i, \Sigma_0^i)$与可信GMM的第$j$个组件$N(\mu_1^j, \Sigma_1^j)$，其最优传输映射通过Schrödinger桥问题求解。该问题等价于寻找最小能量控制路径，使初始分布$\rho_H$演化至终端分布$\rho_T$。

$$
\min_{\mathbf{u}} \mathbb{E} \left[ \int_0^1 \|\mathbf{u}(t)\|^2 dt \right] \quad \text{s.t.} \quad \rho_0 = \rho_H, \rho_1 = \rho_T
$$

此公式的物理含义是：在布朗运动噪声背景下，寻找一条使激活从幻觉状态平滑过渡到可信状态的能量最小路径。相比ICT的均值差向量$\mu_1 - \mu_0$，Schrödinger桥考虑了协方差结构，避免了因忽略分布形状而导致的校正失真。

### Token级动态校正机制

在推理阶段，Scalpel计算当前token激活$\mathbf{z}_{current}$在幻觉GMM各组件上的后验概率，确定其最可能所属组件$r^*$。随后，通过预计算的传输权重$\lambda_{r^*j}^*$找到对应的可信组件$j^*$，并计算传输向量$\mathbf{v}_{r^*} = \mu_1^{j^*} - \mu_0^{r^*}$。校正强度由基础系数$\alpha_{base}$与组件匹配置信度$c$共同决定：

$$
\mathbf{h}_{new} = \mathbf{h}_{old} + \alpha_{base} \cdot c \cdot \mathbf{v}_{r^*} \cdot \mathbf{1}_{top-k}
$$

该设计解决了固定向量校正中“一刀切”导致的稳定性问题：高置信度匹配（$c \approx 1$）时施加强校正，模糊匹配时减弱干预，从而在抑制幻觉的同时保留生成连贯性。仅对逻辑回归探针识别的top-$k$关键头执行此操作，确保最小化对模型通用能力的扰动。

## 实验评估

Scalpel在LLaVA-1.5-7B与Qwen2.5-VL-7B上，针对POPE（Random/Popular/Adversarial）与MME基准，对比了VCD、OPERA及ICT。基线覆盖了主流对比解码与注意力校正路线，但缺失HulluEdit等最新子空间投影方法，限制了与细粒度表征编辑方法的直接对比。

| 模型 | 方法 | COCO Random Acc/F1 | COCO Adversarial Acc/F1 | GQA Popular Acc/F1 |
| :--- | :--- | :--- | :--- | :--- |
| LLaVA-1.5 | Vanilla | 83.29/81.33 | 78.96/77.57 | 78.17/78.37 |
| LLaVA-1.5 | ICT | 89.1/88.48 | 83.83/83.84 | 80.86/82.64 |
| LLaVA-1.5 | Scalpel | 90.67/90.74 | 85.97/86.00 | 84.57/85.31 |
| Qwen2.5-VL | Vanilla | 85.4/82.97 | 84.83/82.42 | 84/82.74 |
| Qwen2.5-VL | ICT | 87.53/85.84 | 86.16/84.32 | 86.43/85.47 |
| Qwen2.5-VL | Scalpel | 91.17/90.41 | 88.83/88.49 | 87.20/86.68 |

Scalpel在LLaVA-1.5的COCO Random上取得90.67%准确率，较ICT提升1.57个百分点；在Qwen2.5-VL的GQA Popular上，F1值从85.47提升至86.68。这表明组件级动态校正在处理流行对象共现先验时更具优势。

消融实验显示，GMM组件数$N_0$对性能影响显著。在COCO Random上，32个组件时性能最佳，而16个组件时图像级干预峰值出现，对象级干预则需更高组件数。移除图像级模块导致LLaVA的F1下降8.43%，移除对象级模块下降8.14%，两者联合使用产生超加性效应，验证了双层级干预的必要性。

评估边界方面，论文未报告推理延迟与离线预计算耗时，无法量化“零成本”声明的真实性。代码未公开，超参数（如$\alpha_{base}$、top-$k$）的敏感性分析缺失，限制了可复现性。MME基准中Scalpel得分758.09（LLaVA），虽高于Vanilla，但与领域综述中DSCR的925.96存在协议差异，跨方法绝对值比较需谨慎。

## 关联研究分析

从方法设计看，Scalpel与HulluEdit同属表征空间编辑，但二者对幻觉异质性的处理逻辑不同。HulluEdit假设物体、属性、关系幻觉占据激活空间中不同且部分重叠的方向，通过子空间投影移除幻觉成分；Scalpel则假设同一头内不同token的偏差属于不同高斯组件，通过最优传输映射实现组件级校正。这一差异源于对幻觉分布结构的假设：HulluEdit关注语义类别间的方向分离，Scalpel关注同一语义类别内token间的分布形态差异。若幻觉主要由语义类别混淆引起，HulluEdit可能更优；若由同一对象的不同视觉状态（如遮挡、模糊）引起，Scalpel的组件级校正更具针对性。

从问题动机看，Scalpel与VCD代表了推理时干预的两条路径。VCD在logits层通过对比解码抑制语言先验，其优势在于无需访问内部激活，部署简单；Scalpel在激活层通过几何映射校正，其优势在于可解释性强且无需额外前向传播。然而，VCD的对比信号是全局的，无法区分不同token的偏差来源；Scalpel的组件级校正虽精细，但依赖离线构建的GMM模型，若测试分布偏离训练分布（如新领域图像），GMM组件的覆盖性可能不足，导致校正失效。

## 总结

Scalpel旨在解决推理时干预中固定向量校正无法适应token级异质偏差的问题。其切入点在于发现注意力激活的幻觉偏离具有多峰几何结构，并通过Schrödinger桥理论实现组件级最优传输映射。该方法在POPE基准上以90.67%的准确率（LLaVA-1.5, COCO Random）超越了ICT的89.1%，验证了动态校正的有效性。然而，其边界在于依赖离线预计算的GMM模型，且未量化离线开销与推理延迟的权衡。当测试图像分布显著偏离GMM训练分布时，组件覆盖性不足是否会导致校正失效，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.09541)
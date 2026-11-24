# CVPR2026最新论文 ｜PHASE-Net: Physics-Grounded Harmonic Attention System for Efficient Remote Photoplethysmography Measurement ｜物理驱动的心率信号建模

研究机构：合肥工业大学、北京科技大学

作者：Bo Zhao、Dan Guo、Junzhe Cao 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.24850)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.24850)

> 远程光电容积脉搏波（rPPG）旨在从面部视频中提取微弱生理信号，但现有深度学习方法多依赖经验堆叠，缺乏对血流动力学内在规律的约束，导致跨域泛化能力受限且可解释性差。本文切入点在于将网络架构本身确立为物理定律的计算等价物，而非仅引入物理损失函数。通过从Navier-Stokes方程推导阻尼谐振子模型，证明其离散解等价于因果卷积，从而构建了PHASE-Net框架。该设计在保持极致轻量化的同时提升了鲁棒性，但其物理假设在极端非线性干扰下的适用边界尚待进一步检验。

## 研究背景

理解本文需把握两个核心概念的因果链条：血液体积脉搏（BVP）与信号信噪比（SNR）。心脏搏动引起皮下血容量周期性变化，依据Beer-Lambert定律，这种体积变化线性映射为像素强度的微小波动。然而，面部视频中的运动伪影和光照变化产生的干扰强度往往比真实脉搏信号高出数个数量级，导致SNR极低。传统信号处理方法基于线性假设，在低SNR下迅速失效；而主流深度学习方法虽能端到端回归信号，但其架构设计往往源于其他领域的经验迁移，未针对rPPG的物理本质进行约束，容易过拟合特定数据集的噪声模式。

rPPG领域的核心矛盾在于如何在低SNR、高噪声且标注稀缺的视觉数据中，构建具备因果一致性与跨域泛化能力的生理信号表征。主流路线分为两类：一是数据驱动的Transformer或状态空间模型（SSM），如PhysFormer和FacePhys，它们通过强大的时空建模能力在受控环境下取得高精度，但计算复杂度高且缺乏物理一致性；二是物理先验融合方法，如PHASE-Net的前身工作，通常仅在损失函数中引入周期性约束，网络结构本身仍为黑盒。本文的切入点在于打破“架构即黑盒”的范式，主张网络结构本身应是物理定律的直接体现。通过建立血流动力学ODE与TCN架构的严格数学桥梁，PHASE-Net试图在理论严谨性与部署效率之间找到新的平衡点，解决现有方法在未见环境下的性能骤降问题。

## 核心方法

### 方法参照系

rPPG的标准流程通常包含空间特征提取、时间动态建模和信号回归三个环节。通用做法是采用3D-CNN或Transformer提取时空特征，再通过全连接层或RNN回归BVP信号。本文的关键差异在于，它不将时间建模视为通用的序列预测任务，而是将其约束为特定物理系统的离散解，从而将TCN从经验组件转变为物理定律的计算实现。

### 物理驱动的TCN架构

时间动态建模环节通常使用RNN或Transformer捕捉长程依赖，但这些架构缺乏对脉搏信号内在动力学的约束。PHASE-Net从Navier-Stokes方程出发，通过线性化和一维平均，推导出描述局部脉搏波动的阻尼谐振子ODE：

$$ \ddot{z}(t) + \alpha \dot{z}(t) + \omega^2 z(t) = u(t) $$

其中 $z(t)$ 为潜在生理信号，$\alpha$ 为阻尼系数，$\omega$ 为恢复力系数，$u(t)$ 为外部驱动噪声。该方程的物理含义是：脉搏信号并非随机波动，而是受血管弹性（恢复力）和血液黏滞性（阻尼）共同作用的振荡系统。通过半隐式欧拉法离散化，该ODE转化为线性时不变（LTI）状态空间模型。命题1证明，该LTI系统的解可表示为所有过去输入的因果卷积；命题2进一步指出，无限脉冲响应（IIR）可用有限脉冲响应（FIR）近似，这正是TCN的计算本质。这一设计动机在于，通过强制网络遵循物理动力学，避免模型学习到与生理机制无关的统计捷径，从而提升跨域泛化能力。

### 零FLOP空间置换与自适应滤波

空间特征提取环节通常使用全局平均池化（GAP）聚合空间信息，但这会均匀加权所有区域，导致信号丰富区域（如额头、脸颊）被噪声区域（如发际线、阴影）污染。PHASE-Net引入两个模块解决此问题。首先是Zero-FLOPs Axial Swapper (ZAS)，它对特征图的部分通道执行可逆的空间块转置：

$$ \text{ZAS}(X_{swap}) = P \cdot T(X_{swap}) $$

其中 $P$ 为通道选择投影，$T$ 为块内二维转置。该操作零FLOP成本，通过打破空间局部性，增强长程空间依赖，且因自逆性和1-Lipschitz性质保证训练稳定性。其次是Adaptive Spatial Filter (ASF)，它通过轻量卷积生成帧级空间掩码 $M_t$，对特征进行加权聚合，并计算一阶时间导数拼接至特征中。ASF的设计动机在于显式编码局部脉搏动态，抑制非生理区域噪声，使后续TCN能更专注于信号丰富的区域。

## 实验评估

实验在UBFC-rPPG、PURE、BUAA-MIHR和MMPD四个基准上进行，采用数据集内和跨数据集协议。基线覆盖传统信号处理（CHROM, POS）、CNN（PhysNet）、Transformer（PhysFormer, RhythmFormer）及SSM（EfficientPhys），但未包含最新的多模态融合方法。主实验结果显示，PHASE-Net在受控数据集上表现优异，在复杂数据集上展现出更强的鲁棒性。

| 数据集 | 方法 | MAE (bpm) | RMSE (bpm) | R |
| :--- | :--- | :--- | :--- | :--- |
| UBFC-rPPG | CHROM | 4.06 | 8.83 | 0.89 |
| UBFC-rPPG | PhysFormer | 0.92 | 2.46 | 0.99 |
| UBFC-rPPG | PHASE-Net | 0.15 | 0.53 | 0.99 |
| PURE | RhythmFormer | 0.27 | 0.47 | 0.99 |
| PURE | PHASE-Net | 0.14 | 0.35 | 0.99 |
| BUAA-MIHR | PhysFormer | 8.45 | 10.17 | -0.06 |
| BUAA-MIHR | PHASE-Net | 5.89 | 7.89 | 0.48 |
| MMPD | RhythmFormer | 4.69 | 11.31 | 0.60 |
| MMPD | PHASE-Net | 4.78 | 8.22 | 0.71 |

在UBFC-rPPG和PURE上，PHASE-Net的MAE分别为0.15和0.14 bpm，优于PhysFormer和RhythmFormer。在光照变化剧烈的BUAA-MIHR上，PHASE-Net的MAE为5.89 bpm，而PhysFormer出现负相关（R=-0.06），表明物理约束有效防止了模型在分布偏移下的崩溃。在MMPD上，PHASE-Net的RMSE（8.22 bpm）显著低于RhythmFormer（11.31 bpm），且相关系数更高，验证了其在多传感器、彩色光照下的稳定性。

消融实验揭示了各模块的贡献。移除GTCN导致UBFC-rPPG的RMSE从0.90升至1.26 bpm，表明物理驱动的时间建模是核心；移除Attention在PURE上导致MAE从0.14升至0.36 bpm，说明空间滤波对局部伪影抑制至关重要。TCN深度从1增至3层时，MAE从0.51降至0.15 bpm，但增至4层时回升至0.25 bpm，暗示3层提供了足够的感受野，更深层导致过平滑。损失权重 $\lambda=0.1$ 时性能最佳，$\lambda=1$ 时过正则化导致MAE升至0.43 bpm。

评估边界方面，论文未报告置信区间，且跨数据集实验采用Leave-One-Out协议，可能高估泛化能力。代码已开源，但超参数搜索范围有限，未探讨不同分辨率下的性能变化。

## 关联研究分析

从问题动机看，PHASE-Net与FacePhys同属轻量化路线，但路径截然不同。FacePhys基于状态空间模型（SSM），通过线性复杂度处理长序列，强调计算效率与边缘部署；PHASE-Net则基于物理推导的TCN，强调理论一致性与可解释性。FacePhys在MMPD上MAE为5.30 bpm，PHASE-Net为4.78 bpm，两者在真实世界数据上性能接近，但PHASE-Net参数量仅0.29M，低于FacePhys的719K，表明物理约束可能在参数效率上更具优势。然而，FacePhys的SSM架构在长序列建模上具有天然优势，而PHASE-Net的TCN依赖固定感受野，在极长视频序列上的表现未经验证。

从方法设计看，PHASE-Net与PhysNeXt在空间特征处理上存在差异。PhysNeXt采用双分支结构化注意力融合，处理原始视频帧和时空图（STMap），通过置信度门控解决信号缺失问题；PHASE-Net则通过ASF生成帧级掩码，显式抑制噪声区域。PhysNeXt在UBFC-rPPG上MAE为0.15 bpm，与PHASE-Net持平，但在PURE上PHASE-Net（0.14 bpm）优于PhysNeXt（0.24 bpm）。这种差异可能源于ASF对局部伪影的针对性抑制，而PhysNeXt的注意力机制更侧重于全局特征对齐。PHASE-Net的物理先验是否在所有光照条件下都优于纯数据驱动的注意力机制，论文未给出系统性对比。

## 总结

PHASE-Net旨在解决rPPG模型缺乏物理一致性导致的跨域泛化瓶颈。其切入点在于将网络架构确立为血流动力学ODE的计算等价物，通过证明离散解等价于因果卷积，为TCN提供了理论根基。该方法在UBFC-rPPG上实现0.15 bpm MAE，在BUAA-MIHR上以5.89 bpm MAE显著优于PhysFormer的负相关表现，验证了物理约束对鲁棒性的提升。然而，论文未探讨物理假设在极端非线性干扰（如剧烈表情变化）下的适用性，且跨数据集实验的Leave-One-Out协议可能高估泛化能力。当支持集增大或噪声分布发生剧烈变化时，物理驱动的TCN是否仍能保持优势，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.24850)
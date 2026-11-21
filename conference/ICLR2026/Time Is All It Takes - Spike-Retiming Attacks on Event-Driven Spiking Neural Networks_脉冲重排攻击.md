# ICLR2026最新论文 ｜Time Is All It Takes: Spike-Retiming Attacks on Event-Driven Spiking Neural Networks ｜脉冲重排攻击

研究机构：新加坡南洋理工大学、香港中文大学

作者：Yi Yu、Qixin Zhang、Shuhan Ye 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.03284)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.03284)

> 事件驱动脉冲神经网络（SNN）依赖时间戳编码信息，但现有对抗攻击多修改脉冲幅度或计数，忽略了时间维度的脆弱性。本文提出仅重排脉冲时间戳、保持计数与幅度不变的时序攻击模型，通过投影在环优化实现离散约束下的可微搜索。该工作揭示了SNN在时间域的隐蔽攻击面，但防御机制仍显薄弱，且整数网格的鲁棒性优势未获理论闭环。

## 研究背景

SNN通过离散脉冲模拟生物神经元，其计算稀疏性源于事件驱动机制：神经元仅在膜电位超过阈值时发放脉冲，突触操作仅在脉冲到达时触发。这种机制使实际计算量与输入信号稀疏度成正比，而非网络参数规模，从而在神经形态硬件上实现能效优势。然而，脉冲函数 $S_t = \mathbb{I}(V_t \geq \theta)$ 几乎处处不可微，导致标准反向传播失效，需依赖代理梯度（Surrogate Gradient, SG）近似导数以支持直接训练。

现有对抗攻击主要继承图像域策略，通过修改脉冲强度或事件计数生成扰动。例如，PDSG-SDA（Lun et al., 2025）利用膜电位分布优化稀疏动态帧攻击，SpikeFool（Büchel et al., 2022）将稀疏浮点扰动舍入为二进制值。这些方法虽有效，但改变了脉冲率统计，易被基于强度或速率的防御检测。事件相机等传感器天然存在时间戳噪声（jitter）和读出延迟，部署中常将事件量化为离散时间箱。在此背景下，仅重排现有脉冲时间、保持计数与幅度不变的时序攻击更具物理可实现性，且能规避强度/速率检查，直接冲击SNN依赖的时间计算。

## 核心方法

### 时序威胁模型与预算约束

本文形式化时序-only威胁模型：攻击者仅移动现有脉冲沿时间轴，不创建、删除或分裂脉冲，且每个事件线/时间箱至多容纳一个脉冲（容量-1）。设输入事件张量 $\mathbf{x} \in \mathbb{Z}_{\geq 0}^{T \times C \times H \times W}$，展平空间-通道维度得事件线 $j \in \{1, \dots, N\}$，活跃索引集 $A(\mathbf{x}) = \{(s, j) : \mathbf{x}[s, j] > 0\}$。对每个 $(s, j) \in A(\mathbf{x})$，选择整数移位 $\delta_{s,j}$，目标时间 $t = s + \delta_{s,j}$ 满足 $0 \leq t < T$。预算定义为：

$$
\mathcal{B}_p(\varepsilon) = \begin{cases}
\max_{(s,j)} |\delta_{s,j}| \leq \varepsilon & p=\infty \\
\sum_{(s,j)} |\delta_{s,j}| \leq \varepsilon & p=1 \\
|\{(s,j) : \delta_{s,j} \neq 0\}| \leq \varepsilon & p=0
\end{cases}
$$

该设计动机在于：传统 $\ell_p$ 预算作用于像素/体素，不适用于稀疏事件流；本文预算在脉冲/包级别定义，匹配传感器时间不确定性，且 $\mathcal{B}_0$ 直接量化“篡改脉冲数”，实现隐蔽性度量。

### 投影在环（PIL）优化

离散时序重排空间难以直接优化。本文引入移位概率对数 $\boldsymbol{\phi}[s, j, u]$，定义温度软化概率 $\boldsymbol{\pi}[s, j, u] = \text{softmax}(\boldsymbol{\phi}[s, j, u]/\kappa)$。软重排算子 $S_{\boldsymbol{\pi}}(\mathbf{x})$ 计算期望后攻击包：

$$
\tilde{\mathbf{x}}[t, j] = \sum_{(s,j) \in A(\mathbf{x})} \sum_{u \in U_p} \mathbf{x}[s, j] \cdot \boldsymbol{\pi}[s, j, u] \cdot \mathbb{I}[T_p(s, u) = t]
$$

其中 $T_p(s, u) = s+u$（$p=\infty$）或 $u$（$p \in \{1,0\}$）。前向传播使用严格投影 $P[\cdot](\mathbf{x}; \boldsymbol{\pi}, \mathcal{B}_p(\varepsilon))$ 生成可行离散调度，反向传播沿软重排 $\tilde{\mathbf{x}}$ 计算梯度。该解耦设计解决了纯严格放置破坏梯度、纯软代理违反威胁模型的矛盾，确保评估时满足容量-1与预算约束，同时提供稳定梯度。

## 实验评估

实验在CIFAR10-DVS、DVS-Gesture、N-MNIST上评估，模型包括ConvNet、ResNet18、VGGSNN等直接训练SNN。基线覆盖SpikeFool（稀疏翻转）和PDSG-SDA（稀疏动态攻击），但缺失基于时序的专用防御训练对比。主结果显示，时序攻击在同等预算下ASR显著高于值修改攻击：

| 数据集 | 模型 | 预算 | 本文ASR (%) | PDSG-SDA ASR (%) |
|---|---|---|---|---|
| DVS-Gesture | ResNet18 | $\mathcal{B}_0(4k)$ | 98.5 | 91.2 |
| N-MNIST | VGGSNN | $\mathcal{B}_0(400)$ | 99.8 | 72.4 |
| CIFAR10-DVS | ResNet18 | $\mathcal{B}_0(4k)$ | 80.0 | 100.0 |

在DVS-Gesture和N-MNIST上，本文攻击ASR更高；但在CIFAR10-DVS上，PDSG-SDA在$\mathcal{B}_0(4k)$达100%，高于本文的80.0%，表明值修改攻击在高密度事件流中可能更具破坏性。

消融实验验证PIL组件必要性。移除PIL（仅用软重排）使DVS-Gesture上$\mathcal{B}_1(8k)$ ASR从98.5%降至92.7%；移除容量正则化降至84.3%；移除预算惩罚降至88.6%。这表明严格投影与正则化对维持攻击强度和预算稳定性至关重要。整数网格比二进制网格更鲁棒：DVS-Gesture上ResNet18在$\mathcal{B}_1(8k)$下，二进制ASR 99.6%，整数仅65.4%。论文归因于整数网格保留每箱多重性，时序卷积积分更平滑，需更大总移位才能产生同等特征变化。

评估边界：指标仅含ASR和干净精度，未报告能效或延迟；评估协议未控制骨干网络差异，ASR差异可能部分源于模型架构而非攻击本身；代码已开源，但超参数（如$\kappa=1, \alpha=1, T_{pgd}=20/40$）未提供敏感性分析。

## 关联研究分析

从问题动机看，本文与TMI（CVPR 2026）形成互补：TMI基于时间互信息推导鲁棒性误差紧界，提供理论解释；本文通过实证攻击验证时序脆弱性，但TMI的互信息计算复杂度较高，且未提供防御机制。本文攻击可作为TMI理论界的压力测试，但两者均未解决“时序稀疏性是否必然导致脆弱性”的根本问题。

从方法设计看，本文PIL优化与UltraLIF（Miñoza, 2026）的完全可微框架存在路线分歧：UltraLIF通过超离散化消除前向-反向不匹配，追求理论精确梯度；本文PIL采用软-硬解耦，接受近似梯度以换取计算效率。在攻击场景下，PIL的近似性可能限制攻击强度上限，但论文未量化此差距。此外，本文未对比基于均衡传播（Equilibrium Propagation）的局部学习防御，后者在生物合理性上占优，但深层收敛困难，是否适用于时序攻击防御尚不明确。

## 总结

本文核心矛盾在于SNN时间编码的脆弱性与现有攻击/防御对时间维度的忽视。切入点在于将时序扰动形式化为容量-1约束下的离散赋值问题，通过PIL优化实现可微搜索。方法上，本文定义$\mathcal{B}_\infty/\mathcal{B}_1/\mathcal{B}_0$预算并开发PIL框架，在DVS-Gesture上$\mathcal{B}_0(4k)$ ASR达98.5%，N-MNIST上$\mathcal{B}_0(400)$ ASR达99.8%。边界在于：整数网格鲁棒性优势缺乏理论证明，仅归因于“多重性平滑”；时序对抗训练（AT）在DVS-Gesture上仅将ASR降至20.09%（$\mathcal{B}_1(8k)$），防御效果有限；未探索多模态事件流中的时序一致性约束。当支持集增大或事件密度变化时，时序攻击的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.03284)
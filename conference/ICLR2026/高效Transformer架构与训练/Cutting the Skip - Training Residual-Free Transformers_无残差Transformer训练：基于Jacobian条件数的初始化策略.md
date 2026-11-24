# ICLR2026最新论文 ｜Cutting the Skip: Training Residual-Free Transformers ｜无残差Transformer训练：基于Jacobian条件数的初始化策略

研究机构：新西兰奥克兰大学

作者：Yiping Ji、James Martens、Jianqiao Zheng 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.00345)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.00345)

> 深层Transformer依赖残差连接（Skip Connections）维持梯度流动，但残差连接破坏了表示的层级抽象，导致网络实际有效深度远低于名义深度。现有去除残差的方法要么修改架构导致硬件不兼容，要么收敛速度极慢。本文通过Jacobian分析发现残差连接本质上是正则化项，提出一种无需修改架构的初始化策略，使无残差Vision Transformer（ViT）在监督与自监督任务中达到甚至超越有残差基线。该方法证明了残差连接并非深度学习的必要组件，但其在超深层扩展中的稳定性仍存疑。

## 研究背景

深层网络的训练稳定性长期依赖残差连接，其核心机制在于改善网络Jacobian矩阵的条件数（Condition Number）。Jacobian条件数 $\kappa(\mathbf{J})$ 定义为最大奇异值与最小奇异值之比，直接决定梯度传播的稳定性。当 $\kappa(\mathbf{J})$ 过大时，梯度在反向传播中迅速衰减或爆炸，导致优化停滞。残差连接通过引入恒等映射 $\mathbf{I}$，将Jacobian谱从零点偏移，从而正则化最小奇异值，确保深层网络可训练。

然而，残差连接在稳定优化的同时，将浅层特征直接注入深层，中断了表示从具体到抽象的层级演进。研究表明，收敛后的Transformer中许多深层对最终预测贡献甚微，可被剪枝而不显著损失性能，表明网络实际行为更接近浅层集成而非深层组合。He et al. (2023) 首次尝试训练无残差Transformer，通过修改自注意力块防止核矩阵秩坍缩，但该方法改变了标准架构，不兼容FlashAttention等硬件优化，且收敛速度仍显著慢于残差模型。本文切入点在于：不改变架构，仅通过调整权重初始化恢复Jacobian的良好条件数，从而在保留标准Transformer块兼容性的前提下实现无残差训练。

## 核心方法

### Jacobian条件数分解

标准Transformer块由自注意力块（Self-Attention Block, SAB）和前馈网络（Feed-Forward Network, FFN）组成，均包含残差连接。本文分析表明，SAB的Jacobian子块条件数远差于FFN，是整体网络病态的主要来源。对于第 $\ell$ 层SAB，其Jacobian $\mathbf{J}_\ell$ 可分解为包含恒等矩阵 $\mathbf{I}_{nd}$ 的项与自注意力导数项 $\mathbf{K}_\ell$ 的乘积。残差连接的作用等价于在 $\mathbf{K}_\ell$ 的谱上添加 $\mathbf{I}_{nd}$，即 $\kappa(\mathbf{K}_\ell + \mathbf{I}_{nd}) \ll \kappa(\mathbf{K}_\ell)$。设计动机在于：若能在无残差情况下使 $\kappa(\mathbf{K}_\ell)$ 自然接近 $\kappa(\mathbf{K}_\ell + \mathbf{I}_{nd})$，即可消除对架构修改的依赖。

### 正交与对角主导初始化

本文提出两组初始化策略以改善 $\mathbf{K}_\ell$ 的条件数。首先，对于值投影矩阵 $\mathbf{W}_V$ 和输出投影矩阵 $\mathbf{W}_O$，其乘积 $\mathbf{W}_V \mathbf{W}_O$ 出现在Jacobian的两个主要项中。为使其条件数为1，本文对随机矩阵 $\mathbf{Q}$ 进行奇异值分解（SVD） $\mathbf{Q} = \mathbf{U}\mathbf{S}\mathbf{V}^\top$，并设定：

$$ \mathbf{W}_V = c \cdot \mathbf{U}, \quad \mathbf{W}_O = c \cdot \mathbf{V}^\top $$

其中 $c$ 为缩放常数。这确保 $\mathbf{W}_V \mathbf{W}_O$ 为缩放正交矩阵，所有奇异值相等，从而稳定Jacobian的主项。

其次，对于查询 $\mathbf{W}_Q$ 和键 $\mathbf{W}_K$ 矩阵，随机初始化导致注意力Logits $\mathbf{M}_\ell = \mathbf{X}\mathbf{W}_Q\mathbf{W}_K^\top\mathbf{X}^\top$ 呈“弥散”状态，使注意力矩阵接近秩1的均匀矩阵，条件数随序列长度 $n$ 恶化。本文采用模仿初始化（Mimetic Initialization），设定：

$$ \mathbf{W}_Q\mathbf{W}_K^\top = \alpha \mathbf{Z} + \beta \mathbf{I} $$

其中 $\mathbf{Z}$ 为高斯噪声，$\alpha, \beta$ 为标量。$\beta \mathbf{I}$ 项鼓励对角主导性，使注意力矩阵接近单位矩阵，从而保持良好条件数。该设计无需修改注意力计算图，完全兼容FlashAttention，解决了He et al. (2023) 因架构修改导致的硬件不兼容问题。

## 实验评估

在ImageNet-1k监督分类任务中，本文使用ViT-Base（12层）对比有残差（Skip）与无残差（Skipless）模型，优化器包括AdamW与SOAP。基线覆盖标准ViT及无残差变体，但未对比其他高效架构（如线性注意力或状态空间模型），限制了跨架构的效率比较。

| 模型配置 | 优化器 | 准确率 (%) |
| :--- | :--- | :--- |
| Skip | AdamW | 80.3 |
| Skip | SOAP | 80.1 |
| Skipless | AdamW | 61.4 |
| Skipless | SOAP | 77.0 |
| Skipless + Init | AdamW | 78.1 |
| Skipless + Init | SOAP | 80.8 |

数据显示，无残差模型在AdamW下性能骤降至61.4%，验证了Jacobian病态的严重性。引入本文初始化后，AdamW下恢复至78.1%，SOAP下达到80.8%，超越有残差基线0.5个百分点。这表明初始化策略不仅恢复了稳定性，还通过SOAP优化器实现了性能反超。

在自监督DINO预训练中，ViT-Small模型在VOC2012、COCOStuff和ADE20K上的密集线性探测分割任务显示，无残差模型在单特征提取下于VOC2012和COCOStuff上优于有残差模型（如VOC2012 mIoU 62.3 vs 56.3），但在ADE20K上略低（22.5 vs 23.7）。多尺度特征聚合后，无残差模型在ADE20K上反超（25.6 vs 26.0，注：此处原文数据需仔细核对，表格中Skipless+SOAP+Multiscale ADE20K为25.6，Skip+SOAP+Multiscale为26.3，实际Skip略高，但Skipless在单特征上优势明显）。这一差异归因于ADE20K场景复杂性，残差连接隐式混合了多尺度信息，而无残差模型需显式聚合多层特征才能弥补。

评估边界方面，实验仅覆盖12层ViT，未探索超深层（>100层）扩展性；代码未公开，超参数 $\alpha, \beta, c$ 的敏感性分析不足；视觉任务结论是否适用于语言模型未验证。

## 关联研究分析

从问题动机看，本文与He et al. (2023) 均旨在解决无残差Transformer的秩坍缩与训练不稳定，但He et al. 通过修改注意力块结构防止核矩阵秩1坍缩，而本文通过初始化改善Jacobian条件数。差异根源在于：He et al. 关注前向传播的核性质，本文关注反向传播的梯度条件数。本文方法保留了标准架构，因此兼容FlashAttention，而He et al. 的修改破坏了这种兼容性，限制了其在大规模训练中的实际部署价值。

从方法设计看，本文与知识库中“训练稳定性优化”路线（如Taming Curvature、Post-LN）不同，后者通过归一化层或曲率控制解决深层激活爆炸，而本文通过初始化解决无残差下的Jacobian病态。Taming Curvature假设存在残差连接，通过预热限制曲率增长；本文则完全移除残差，依赖正交初始化维持谱稳定。这种差异暗示：残差连接并非稳定性的唯一来源，良好的初始化可在无残差条件下替代其正则化作用。然而，本文未对比有残差+相同初始化的基线，无法完全排除初始化本身对残差模型的潜在增益。

## 总结

本文核心矛盾在于残差连接稳定优化但破坏层级表示。He et al. (2023) 修改架构解决秩坍缩但牺牲硬件兼容性，本文通过Jacobian分析发现残差连接本质是谱正则化，提出正交 $\mathbf{W}_V\mathbf{W}_O$ 与对角主导 $\mathbf{W}_Q\mathbf{W}_K^\top$ 初始化，无需架构修改即可恢复条件数。实验证明，在12层ViT上，无残差模型配合SOAP优化器在ImageNet-1k达80.8%，在DINO密集预测上优于有残差基线。边界在于仅验证至12层，未探索超深层扩展，且视觉任务结论未推广至语言模型。当模型深度增加至100层以上时，仅靠初始化能否持续抑制Jacobian病态，还是仍需引入其他稳定性机制，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.00345)
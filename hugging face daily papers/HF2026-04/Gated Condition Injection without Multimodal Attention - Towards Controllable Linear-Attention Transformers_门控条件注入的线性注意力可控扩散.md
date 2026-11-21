# HuggingFace最新推荐论文 ｜Gated Condition Injection without Multimodal Attention: Towards Controllable Linear-Attention Transformers ｜门控条件注入的线性注意力可控扩散

研究机构：新加坡国立大学、上海交通大学

作者：Yuhe Liu、Zhenxiong Tan、Yujia Hu 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.27666)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.27666)

> 导读 空间可控图像生成旨在弥合文本语义与像素空间之间的接地鸿沟，其核心价值在于满足设计、游戏资产制作等对物体位置、姿态及布局有严格要求的应用需求。现有主流方案如 ControlNet 依赖特征直接相加，隐含空间对齐假设，在主体驱动等非对齐任务中失效；而 OminiControl 虽通过多模态注意力实现灵活交互，但在线性注意力骨干上收敛极慢。本文切入点在于利用门控机制弥补线性注意力的信息压缩缺陷，实现高效且通用的条件注入。该方法在 SANA 骨干上以极小参数开销实现了比基线快 10 倍的收敛速度，但其对复杂空间推理能力的上限尚存疑。

## 研究背景

当扩散模型从 UNet 架构向 Diffusion Transformer (DiT) 演进时，计算复杂度成为部署瓶颈。标准 Softmax 注意力的二次方复杂度迫使研究者转向线性注意力，如 SANA 采用的 ReLU 线性注意力，其通过核分解将复杂度降至线性，适合端侧部署。然而，线性注意力在长序列处理中会发生信息压缩，导致条件信号在去噪过程中被稀释。

可控生成领域的主流路线分为两类：ControlNet 通过复制主干并特征相加注入条件，T2I-Adapter 则采用轻量级适配器。这两种方法均假设条件与潜变量在空间上严格对齐，适用于边缘、深度等结构控制，但在主体驱动生成中，物体姿态与布局发生几何变化，特征相加导致信号冲突。OminiControl 提出将条件转化为 Token 序列，通过多模态注意力（MMAttn）与噪声潜变量交互，解决了非对齐问题。然而，实验表明 OminiControl 在 SANA 上收敛缓慢，空间任务需 50k 步而主体任务仅需 15k 步，这归因于线性注意力缺乏显式空间对齐机制，导致模型难以快速建立位置对应关系。

本文针对线性注意力骨干下条件注入的收敛效率与空间对齐稳定性矛盾，提出 GateControl 框架。该框架不依赖额外的独立编码器，而是通过共享模块处理噪声潜变量与条件，并引入门控机制选择性融合 Token 信息，旨在以最小参数开销实现快速收敛与通用控制。

## 核心方法

### 共享模块编码

本文方法置于 OminiControl 的 Token 拼接范式下，但摒弃了其独立条件编码器的设计。关键差异在于，本文采用共享模块策略，将噪声潜变量 $X$、文本条件 $C_T$ 与图像条件 $C_I$ 统一为序列 $[X; C_T; C_I]$，由同一骨干网络处理。这一设计消除了 ControlNet 中独立编码器带来的参数冗余（590M vs 0.09M），并保留了原始模型的信息流，使模型能自适应新条件。

### 门控条件注入

共享模块虽实现了灵活交互，但线性注意力的信息压缩导致空间任务收敛缓慢。为此，本文在 Linear Attention 层后引入门控模块，以补偿信息丢失。设计动机在于，线性注意力中部分条件 Token 被抑制，门控机制允许每个 Token 独立决定其保留强度。

门控分数通过线性变换与 Sigmoid 激活计算，实现逐 Token 的动态过滤：

$$
g_X = \sigma(W_{g1} h_X), \quad g_{C_I} = \sigma(W_{g2} h_{C_I})
$$

其中 $h_X$ 与 $h_{C_I}$ 分别为噪声潜变量与图像条件的隐藏状态，$W_{g1}, W_{g2}$ 为可学习参数。门控后的特征通过逐元素乘法调制，再相加融合：

$$
h_{out} = g_X \odot h_X + g_{C_I} \odot h_{C_I}
$$

该公式表明，每个 Token 根据自身重要性独立调节信息贡献，避免了全局注意力交互的计算开销。实验显示，Token-wise 门控比 Element-wise 门控参数少 200M，且训练更稳定；使用 Self-Attention 前的特征计算门控分数优于使用后的特征，因为前者避免了门控梯度对正常注意力交互的干扰，增强了 Token 自主判断能力。

## 实验评估

| Task | Method | Base Model | FID ↓ | SSIM ↑ | CLIP Image ↑ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Canny | ControlNet | SD1.5 | 18.74 | 67.81 | 0.305 |
| Canny | Ours | SANA | 21.97 | 71.86 | 0.263 |
| Colorization | ControlNet | SANA | 24.95 | 47.39 | 0.239 |
| Colorization | Ours | SANA | 10.28 | 54.85 | 0.254 |
| HED | ControlNet | SANA | 20.36 | 55.58 | 0.238 |
| HED | Ours | SANA | 16.81 | 63.06 | 0.259 |

实验在 COCO 2017 验证集（5,000 张）上进行，基线包括 SD1.5 上的 ControlNet/T2I-Adapter 及 SANA 上的 ControlNet/OminiControl。在 SANA 骨干上，本文方法在 Colorization 任务 FID 从 24.95 降至 10.28，HED 任务 MSE 从 2320 降至 1168，显著优于 ControlNet。然而，Canny 任务 FID 21.97 高于 SD1.5 基线的 18.74，这可能源于 SANA 骨干本身的质量上限低于 SD1.5，而非方法缺陷。

消融实验表明，移除门控机制导致 FID 从 19.0 升至 22.6，SSIM 从 0.42 降至 0.36，验证了门控对收敛与质量的贡献。位置选择上，置于 Cross-Attention 后导致训练不稳定，置于 Mix-FFN 后性能波动小，最终选择 Linear Attention 后。门控类型中，Token-wise 门控以 0.09M 参数实现了与 Element-wise（200M 参数）相当的性能，证明动态 Token 选择的关键作用。

评估边界方面，论文未报告置信区间，且仅在 512x512 与 1024x1024 分辨率下测试。可复现性上，提供了 LoRA rank 16、Prodigy 优化器、4 张 H200 GPU 等详细设置，但未开源代码。指标涵盖 FID、SSIM、MUSIQ 及 CLIP 分数，但未评估 3D 几何一致性或长序列一致性。

## 关联研究分析

从问题动机看，本文与 OminiControl 同属多模态 Token 交互路线，但针对线性注意力的信息压缩问题引入门控。OminiControl 依赖 Softmax 注意力的全局交互，在 SANA 上因缺乏显式空间对齐而收敛慢；本文通过门控机制实现局部自适应融合，解决了这一瓶颈。差异根源在于骨干架构特性：Softmax 注意力保留全局依赖，而线性注意力压缩信息，需额外机制补偿。

从方法设计看，本文与 ControlNet 同属条件注入范式，但摒弃了独立编码器。ControlNet 通过特征相加实现控制，隐含空间对齐假设，在主体驱动任务中失效；本文采用共享模块与门控融合，支持非对齐条件。这一设计选择源于对参数效率的追求：ControlNet 需 590M 额外参数，而本文仅 0.09M。然而，本文未对比其他线性注意力可控生成方法，如 SANA-1.0 原生控制，基线覆盖存在缺口。

## 总结

本文核心矛盾是线性注意力骨干下条件注入的收敛效率与空间对齐稳定性冲突。现有方法如 ControlNet 依赖空间对齐假设，OminiControl 收敛缓慢，均无法兼顾高效与通用。本文通过共享模块与门控机制，以 0.09M 参数实现了 SANA 骨干上 Colorization 任务 FID 10.28 与 HED 任务 MSE 1168 的性能，收敛速度提升 10 倍。边界在于，Canny 任务 FID 高于 SD1.5 基线，暗示骨干质量上限限制；且未评估 3D 几何控制能力。当支持集增大或任务复杂度提升时，门控机制在复杂空间推理中的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.27666)
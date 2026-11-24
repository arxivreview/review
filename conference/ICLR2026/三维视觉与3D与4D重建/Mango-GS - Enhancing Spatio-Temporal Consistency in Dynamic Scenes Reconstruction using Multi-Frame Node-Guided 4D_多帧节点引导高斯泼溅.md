# ICLR2026最新论文 ｜Mango-GS: Enhancing Spatio-Temporal Consistency in Dynamic Scenes Reconstruction using Multi-Frame Node-Guided 4D Gaussian Splatting ｜多帧节点引导高斯泼溅

研究机构：清华大学

作者：Tingxuan Huang、Haowei Zhu、Jun-hai Yong 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.11543)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.11543)

> 动态场景重建旨在从视频序列中恢复具有时间一致性的四维几何表示，以支撑虚拟现实与数字孪生应用。现有基于3D高斯泼溅（3D Gaussian Splatting, 3DGS）的方法多采用逐帧优化策略，导致模型记忆瞬时状态而非学习运动规律，在快速运动下产生模糊与伪影。本文通过解耦控制节点表示与多帧时间注意力机制，在稀疏节点空间建模运动趋势，实现了高保真与实时渲染的平衡。该方法在通用动态场景上达到了当前最优性能，但其对长时外推与物理一致性的验证仍显不足。

## 研究背景

动态场景重建的核心难点在于解耦相机运动与物体运动。3DGS通过显式高斯基元与光栅化实现了静态场景的实时渲染，但其动态扩展通常依赖变形场。主流方法如D-3DGS与4DGS使用多层感知机（Multi-Layer Perceptron, MLP）为每个高斯预测逐帧位移，这种逐帧孤立处理导致模型无法捕捉跨帧的运动依赖，在复杂轨迹下出现时间不一致性。

为提升时间一致性，引入时间序列模型是自然选择，但直接对数百万高斯应用Transformer计算开销巨大。SC-GS（Sparse Control Gaussian Splatting）提出用稀疏控制节点驱动密集高斯，但依赖初始帧的空间k-近邻（k-Nearest Neighbors, k-NN）关系。当物体发生大位移时，初始空间邻近的高斯可能运动到不同区域，导致运动传播错误与几何漂移。Mango-GS针对这一邻域漂移问题，提出解耦节点表示与多帧时间注意力，旨在从数据中直接学习连贯的运动模式。

## 核心方法

### 方法参照系

Mango-GS属于节点引导的动态3DGS范式。标准流程（如SC-GS）通过稀疏节点的运动驱动密集高斯，节点与高斯的关联基于初始帧的空间距离。本文的关键差异在于将空间k-NN替换为基于学习式亲和度的语义关联，并将逐帧变形预测升级为多帧联合的时间注意力建模。

### 解耦控制节点表示

传统节点仅由3D坐标定义，导致大运动下邻域失效。Mango-GS将节点 $n_i$ 解耦为规范位置 $p_i \in \mathbb{R}^3$ 与潜在特征码 $f_i \in \mathbb{R}^D$。高斯 $g_j$ 与节点 $n_i$ 的关联权重 $w_{ij}$ 通过轻量级MLP计算，该MLP输入高斯的规范参数 $\phi_j = (x_j, q_j, s_j)$ 与节点特征码，输出亲和度分数，经Softmax归一化得到权重：

$$ w_{ij} = \text{softmax}\left( \text{MLP}(\phi_j, f_i) \right)_{i \in K(j)} $$

这一设计使高斯绑定到语义一致的节点而非单纯的空间邻居，解决了大位移下运动传播错误导致的模糊问题。

### 多帧时间注意力网络

为捕捉运动趋势，Mango-GS在节点空间引入时间Transformer。网络输入为节点规范位置与时间戳嵌入，经MLP骨干与时间自注意力块处理，一次性预测时间窗口 $T$ 内所有节点的位移、旋转与缩放。时间注意力块通过门控机制融合时间信息：

$$ H_{out}^{(l)} = H_{main}^{(l)} + \sigma(w_{gate}) \odot H_{attn} + w_{bias} $$

其中 $H_{attn}$ 为沿时间轴的多头自注意力输出，$\sigma$ 为Sigmoid函数。该机制允许网络自适应地控制时间信息的融入程度，相比逐帧MLP，能生成更连贯、符合物理直觉的运动轨迹。

## 实验评估

实验在HyperNeRF与Neural 3D Video数据集上进行，基线覆盖D-3DGS、4DGS、SC-GS、GaGS等主流动态3DGS方法，但未包含物理驱动类（如VeloGauss）或前馈类（如UniSplat）方法。

| 方法 | Neural 3D Video PSNR (dB) | Neural 3D Video SSIM | HyperNeRF-vrig PSNR (dB) | HyperNeRF-vrig tLPIPS |
| :--- | :--- | :--- | :--- | :--- |
| D-3DGS | 31.15 | 0.941 | 25.0 | 0.0234 |
| 4DGS | 31.58 | 0.942 | 25.4 | 0.0248 |
| SC-GS | 30.20 | 0.935 | 25.2 | 0.0236 |
| TimeFormer | 31.84 | 0.941 | 24.3 | 0.0265 |
| **Mango-GS** | **31.89** | 0.942 | **26.2** | **0.0196** |

Mango-GS在Neural 3D Video上PSNR达31.89 dB，略高于TimeFormer的31.84 dB；在HyperNeRF上PSNR达26.2 dB，显著优于基线，且tLPIPS最低，表明时间一致性最佳。

消融实验显示，解耦节点（Step 3）相比纯节点（Step 2）PSNR提升0.79 dB，验证了语义邻域的有效性。多帧时间注意力（Step 5）相比无注意力（Step 4）PSNR提升0.48 dB。时间窗口 $T=6$ 时PSNR最高（28.39 dB），$T=8$ 时FPS降至156.2，存在性能与速度的权衡。

评估指标包含PSNR、SSIM、LPIPS、tLPIPS、FPS与存储大小，但缺乏几何精度指标（如Chamfer Distance）与物理一致性度量。实验在单张NVIDIA RTX 3090 GPU上完成，代码已开源，超参数（如 $T=6$，节点数2048）明确，可复现性良好。

## 关联研究分析

从运动建模机制看，Mango-GS与TimeFormer均使用Transformer建模时间依赖，但TimeFormer直接作用于密集高斯，计算开销随高斯数量线性增长；Mango-GS将注意力限制在2048个稀疏节点，通过解耦表示实现语义传播，这在大规模场景下更具扩展性。然而，Mango-GS的运动预测仍为数据驱动，未引入物理约束，与VeloGauss等物理驱动方法相比，其在长时外推与反事实模拟中的表现未知。

从节点关联机制看，Mango-GS与SC-GS同属节点引导范式，但SC-GS依赖初始帧空间k-NN，Mango-GS采用学习式亲和度。这一差异源于对大运动场景鲁棒性的需求：空间k-NN在物体分离后失效，而学习式亲和度能维持语义一致性。但Mango-GS未讨论该机制在极端非刚体变形（如布料、流体）下的有效性，其MLP亲和度是否足以捕捉复杂形变规律，论文未给出回答。

## 总结

Mango-GS针对动态3DGS中逐帧优化导致的时间不一致性问题，提出解耦控制节点与多帧时间注意力机制，在稀疏节点空间学习运动趋势。该方法在HyperNeRF上取得26.2 dB PSNR与0.0196 tLPIPS，显著优于基线，验证了语义邻域与时间建模的有效性。其边界在于实验仅覆盖通用小场景，未涉及大规模城市场景或物理约束验证，且时间窗口固定为6帧，长序列依赖滑动窗口策略。当时间窗口扩展至数十帧时，解耦节点的语义稳定性是否仍能维持，论文未提供相关实验数据。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.11543)
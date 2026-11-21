# WACV2026最新论文 ｜RemEdit: Efficient Diffusion Editing with Riemannian Geometry ｜黎曼几何驱动的扩散编辑加速

研究机构：美国利哈伊大学

作者：Eashan Adhikarla、Brian D. Davison

论文原文见 [arXiv](https://arxiv.org/abs/2601.17927)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.17927)

> 扩散模型语义编辑面临语义保真度与推理速度的根本矛盾，线性潜空间偏移易导致图像脱离自然流形产生伪影，而通用剪枝策略无法区分编辑关键Token与背景冗余Token。RemEdit 通过Mamba模块学习潜空间黎曼结构以计算测地线偏移，结合双SLERP插值控制编辑强度，并引入任务感知注意力剪枝保留关键Token。该方法在U-Net架构下实现了2.8秒的实时编辑与92.41%的分割一致性，但其有效性局限于DDIM范式，未验证在新一代整流流架构下的几何稳定性。

## 研究背景

扩散模型编辑的核心困境在于潜空间几何结构的误用。U-Net瓶颈特征空间（h-space）被证明具有语义稳定性，传统方法如Asyrp直接施加线性偏移 $\Delta h_{linear}$ 实现编辑。然而，线性叠加会将潜变量推离自然图像流形，导致身份丢失或结构畸变。为维持流形约束，需引入黎曼几何概念，将编辑路径建模为流形上的测地线，但精确计算测地线通常依赖昂贵的Jacobian估计或优化过程，难以满足实时性要求。

现有编辑方法在保真度与效率间存在显著割裂。Prompt-to-Prompt（P2P）通过注意力操纵实现局部编辑，但推理耗时达38.7秒且对提示词敏感；Asyrp虽快但线性偏移导致分割一致性仅87.90%。与此同时，自注意力层消耗U-Net单次前向传播超过80%的GFLOPs，成为计算瓶颈。现有剪枝方法（如SiTo、ATEDM）为文本生成设计，无法区分全局冗余Token与维持未编辑区域身份的关键Token，盲目剪枝会破坏背景一致性。RemEdit 的切入点在于将几何保真与计算加速统一：通过轻量级Mamba网络直接学习Christoffel符号以高效求解测地线ODE，并设计任务感知剪枝头，使加速过程显式依赖编辑语义目标，从而在抑制背景漂移的同时降低计算开销。

## 核心方法

### 方法参照系

本文基于DDIM反转的U-Net编辑流程，与Asyrp等h-space线性编辑方法共享相同的反转-去噪骨架。关键差异在于：标准流程在h-space执行线性向量加法，而RemEdit将h-space视为黎曼流形，通过指数映射计算测地线偏移，并在去噪末端引入双SLERP插值与任务感知剪枝，以解决线性偏移的流形偏离与通用剪枝的背景破坏问题。

### 测地线导航与黎曼块

传统h-space编辑采用 $h' = h + \Delta h_{linear}$，该操作忽略流形曲率，易产生伪影。RemEdit 在Riemannian Block中引入Mamba网络学习Christoffel符号 $\Gamma_{[k]ij}$，将测地线方程转化为常微分方程（ODE）求解。具体而言，从初始点 $y_0$ 预测切向量 $v_0$，通过ODE积分器求解 $\gamma(t)$，最终偏移量为 $\Delta h = \gamma(1) - y_0$。

$$
\frac{d^2 \gamma^k}{dt^2} + \Gamma^k_{ij} \frac{d\gamma^i}{dt} \frac{d\gamma^j}{dt} = 0
$$

该公式的物理含义是：在弯曲流形上，测地线是“最直”的路径，Christoffel符号编码了局部曲率对路径弯曲的影响。通过Mamba以O(N)复杂度学习连接系数，避免了Jacobian估计的高昂开销，使编辑方向严格保持在数据流形内，显著提升了方向CLIP相似度与分割一致性。

### 双SLERP插值与任务感知剪枝

测地线偏移 $\Delta h$ 提供了几何正确的方向，但直接应用缺乏强度控制。RemEdit 引入双SLERP机制：内层SLERP在特征空间插值 $h' = SLERP(h, h_{geo}, \alpha_{inner})$，控制语义编辑强度；外层正交SLERP在噪声空间分离身份与语义分量，公式为 $x_0 = \alpha_{outer} x_0^{fid} + (1-\alpha_{outer}) o$，其中 $o = x_0^{sem} - proj_{x_0^{fid}}(x_0^{sem})$。

$$
\mathcal{L} = \mathcal{L}_{fidelity} + \lambda_{sparsity} \mathcal{L}_{sparsity}
$$

该损失函数训练PruningHead，使其在保留编辑关键Token的同时最大化剪枝率。设计动机在于解决通用剪枝无法区分“全局冗余”与“局部关键”Token的失效问题。通过条件化于编辑语义向量 $d_{edit}$，PruningHead动态预测Token重要性，在50%剪枝率下仍保持视觉可接受性，推理速度提升约18%。

## 实验评估

| 方法 | Smiling $S_{dir}$↑ | Smiling Seg. Cons.(%)↑ | Sad $S_{dir}$↑ | Tanned $S_{dir}$↑ | 推理时间(s)↓ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Asyrp | 0.190 | 87.90 | 0.159 | 0.177 | 28.9 |
| P2P | 0.170 | 93.70 | 0.163 | 0.174 | 45.2 |
| LEdits++ | 0.182 | 89.70 | 0.169 | 0.175 | 20.1 |
| **RemEdit** | **0.1982** | **92.41** | **0.1792** | **0.1948** | **2.8** |

实验在CelebA-HQ、LSUN-Church和AFHQ-Dog上进行，基线覆盖StyleCLIP、Asyrp、P2P等主流方法，但缺失FlowEdit、FLUX.1 Kontext等RF/DiT架构基线。RemEdit在Smiling任务上 $S_{dir}$ 达0.1982，较Asyrp提升0.0082，推理时间2.8秒仅为P2P的6.2%。LSUN-Church上Ancient任务Seg. Cons.达63.91%，优于Asyrp的60.13%。

| 配置 | $S_{dir}$↑ | Seg. Cons.(%)↑ | 时间(s)↓ |
| :--- | :--- | :--- | :--- |
| Euclidean offset | 0.190 | 87.9 | 1.82 |
| + Geodesic Navigation | 0.196 | 89.5 | 2.76 |
| + Dual-SLERP | 0.198 | 92.4 | 2.89 |
| + Pruning ($\rho=0.5$) | 0.184 | 89.5 | 2.31 |

消融显示，测地线导航将Seg. Cons.从87.9%提升至89.5%，双SLERP进一步推至92.4%，但推理时间从1.82秒增至2.89秒。剪枝至50%时，$S_{dir}$ 降至0.184，Seg. Cons.回落至89.5%，表明激进剪枝对语义保真度有负迁移，但时间降至2.31秒。

评估指标限于 $S_{dir}$、Seg. Cons.和推理时间，缺乏FID或LPIPS等感知质量指标。所有实验基于256×256分辨率DDIM架构，未测试高分辨率场景。代码已开源，但Mamba模块的超参数与训练细节未在正文中完整披露，复现需依赖附录。

## 关联研究分析

从问题动机看，RemEdit 与FlowEdit 形成路线竞争。FlowEdit 基于整流流（RF）的直线ODE轨迹，通过速度场差异实现无反转编辑，规避了DDIM反转的误差累积；而RemEdit 坚持DDIM反转范式，通过黎曼几何优化去噪路径。差异根源在于架构假设：FlowEdit 依赖RF模型的直线轨迹特性，RemEdit 则假设U-Net h-space具有黎曼结构。在RF架构下，h-space的线性稳定性是否仍成立，以及黎曼几何是否必要，论文未提供跨架构验证。

从方法设计看，RemEdit 的任务感知剪枝与RegionE 的区域感知生成存在互补性。RegionE 通过空间分块避免未编辑区域的重复计算，属于空间维度的加速；RemEdit 通过Token重要性剪枝减少注意力计算，属于特征维度的加速。两者均针对自注意力瓶颈，但RegionE 依赖显式区域划分，RemEdit 依赖隐式语义条件。在多对象并发编辑中，任务感知剪枝能否有效解耦不同对象的Token重要性，避免注意力泄漏，是两者共同面临的挑战，但RemEdit 未在此场景下测试。

## 总结

RemEdit 旨在解决扩散编辑中几何保真与计算效率的矛盾，抓住线性偏移导致流形偏离与通用剪枝破坏背景一致性的关键失效点。通过Mamba学习Christoffel符号求解测地线ODE，结合双SLERP控制编辑强度，并引入任务感知剪枝，该方法在U-Net架构下实现了2.8秒推理与92.41%分割一致性。其边界在于实验局限于256×256分辨率DDIM范式，未验证在RF/DiT架构下的几何稳定性与剪枝鲁棒性。当骨干网络迁移至整流流时，h-space的黎曼结构假设是否依然成立，以及任务感知剪枝在直线ODE轨迹下的有效性如何，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.17927)
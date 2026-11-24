# CVPR2026最新论文 ｜TokenLight: Precise Lighting Control in Images using Attribute Tokens ｜属性令牌化光照控制

研究机构：美国耶鲁大学

作者：Sumit Chaturvedi、Yannick Hold-Geoffroy、Mengwei Ren 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.15310)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.15310)

> 图像重光照的核心矛盾在于：用户需要像操作3D软件一样精确控制光源位置与属性，但现有方法要么依赖难以获取的3D重建，要么使用环境图等粗粒度条件导致近场光照失效。TokenLight的切入点是：将物理光照属性直接编码为扩散Transformer的输入令牌，绕过显式几何分解，实现端到端的像素级重渲染。该方法通过大规模合成数据训练，在无需逆渲染监督的情况下，展现了对光-场景交互的隐式理解。其价值在于提供了比文本或环境图更精细的控制接口，但实验未覆盖通用室内场景基准，且缺乏对极端物理幻觉的定量评估。

## 研究背景

当用户试图在一张静态照片中调整一盏台灯的颜色或移动一个虚拟点光源时，传统逆渲染方法面临根本性困境：从单张图像中分离几何、材质和光照存在固有歧义，导致重建的3D场景往往不准确，进而使重光照结果出现几何错位或材质漂移。这种病态性使得基于显式3D重建的方法（如Neural Gaffer）在复杂遮挡或半透明材质上表现脆弱。与此同时，基于环境图（Environment Map）的方法虽然避免了3D重建，但环境图假设光源位于无穷远处，无法建模近场点光源的平方反比衰减和位置依赖的半影效果，导致用户无法精确控制光源在图像空间中的具体位置。

图像重光照领域的主流路线在生成质量与物理一致性之间摇摆。早期基于逆渲染的方法追求物理可解释性，但泛化能力差；2023年后，以IC-Light为代表的扩散模型方法利用强大的生成先验换取视觉逼真度，成为SOTA基线，但其条件输入多为文本或环境图，缺乏对光源空间位置的细粒度控制。TokenLight抓住了这一被忽略的痛点：现有方法缺乏一种既直观又精确的光照表示，能够直接在2D图像域中实现3D空间定位的光照编辑。本文旨在构建一种参数化、可解释且空间局部化的光照控制接口，弥合3D光照工具的灵活性与2D图像编辑的易用性之间的鸿沟。

## 核心方法

### 条件生成参照系

本文遵循扩散模型条件生成的通用范式，将重光照建模为从输入图像 $I$ 和光照编辑 $\Delta L$ 到目标图像 $I_r$ 的条件分布 $p_\theta(I_r | I, \Delta L)$。与Neural Gaffer等依赖显式3D重建或DiffusionRenderer依赖内在分解的方法不同，TokenLight的关键差异在于：它不显式估计场景几何或材质，而是将光照变化直接编码为条件令牌，让模型隐式学习光-场景交互。

### 物理属性令牌编码

设计动机在于解决环境图无法表达近场光源、文本提示缺乏物理精度的问题。TokenLight将光照编辑 $\Delta L$ 分解为四类物理属性：全局环境缩放 $a$、全局漫反射级别 $d_g$、附加点光源 $(\mathbf{p}, \mathbf{c}, \lambda, d)$ 和场景内光源 $(\mathbf{m}, \mathbf{c}, \lambda, t)$。其中，$\mathbf{p}$ 为3D坐标，$\mathbf{c}$ 为颜色，$\lambda$ 为强度，$d$ 为漫反射程度，$\mathbf{m}$ 为光源掩码。这些标量和向量属性通过高斯傅里叶特征（Gaussian Fourier Features）编码为令牌序列：

$$ \text{Token}(\alpha) = \mathbf{B} \cdot \phi(\alpha), \quad \phi(\alpha) = [\cos(2\pi \sigma \alpha), \sin(2\pi \sigma \alpha)] $$

其中 $\alpha$ 为属性值，$\mathbf{B}$ 为投影矩阵，$\sigma=5$ 为频率尺度。这种编码方式将连续物理参数映射到高维空间，使扩散Transformer能够通过自注意力机制精细区分微小的光照变化，从而实现对光源位置、颜色和强度的解耦控制。

### 流匹配训练与条件注入

设计动机在于利用预训练扩散模型的视觉先验，同时确保光照条件与图像内容的空间对齐。模型采用流匹配（Flow Matching）目标函数，学习从噪声到数据潜变量的速度场：

$$ \mathcal{L} = \mathbb{E}_{\tau, \mathbf{X}, \boldsymbol{\epsilon}} \left[ \| u_\theta(\mathbf{z}_\tau, \tau, I, \Delta L) - (\mathbf{X} - \boldsymbol{\epsilon}) \|^2 \right] $$

其中 $\mathbf{z}_\tau = (1-\tau)\boldsymbol{\epsilon} + \tau \mathbf{X}$ 为插值潜变量。输入图像令牌与光照属性令牌拼接成单一序列，共享位置嵌入，通过全自注意力处理。这种架构允许模型在去噪过程中同时推理图像空间内容和光照物理属性，无需显式的几何中间表示。

## 实验评估

实验在合成Objaverse数据集和真实VisibleFixture-60数据集上进行，基线包括Neural Gaffer、DiffusionRenderer和ScribbleLight。值得注意的是，实验未包含IC-Light等当前图像重光照SOTA基线，也未在MIT MIIW等通用室内场景基准上测试，限制了与领域主流方法的直接对比。

| 方法 | PSNR (PointGT) | SSIM (PointGT) | LPIPS (PointGT) | PSNR (PanoGT) |
|---|---|---|---|---|
| DiffusionRenderer | 13.5338 | 0.9374 | 0.0402 | 13.5106 |
| Neural Gaffer | 16.7595 | 0.9436 | 0.0415 | 16.7183 |
| TokenLight | 21.9772 | 0.9759 | 0.0210 | 21.2416 |

在合成数据上，TokenLight的PSNR显著高于基线，表明其空间光照控制精度更高。在真实VisibleFixture-60数据集上，TokenLight的PSNR为20.0772，SSIM为0.8476，均优于ScribbleLight（PSNR 14.6356, SSIM 0.5186），验证了其在真实场景中的泛化能力。

消融实验通过混淆矩阵分析了光源位置精度。TokenLight的敏感性指标 $B/A$ 为1.877，远高于Neural Gaffer的1.111，且对角线误差 $A$ 更低（0.049 vs 0.160），表明模型能更准确地区分相邻光源位置。用户研究显示，77.5%的参与者偏好TokenLight的结果，89.2%认为其优于Careaga et al.，进一步证实了其控制的可解释性和视觉质量。

评估边界方面，论文未报告置信区间，且合成数据与真实数据之间的域差距未通过定量指标衡量。代码未公开，但提供了详细的训练超参数（16×A100-80GB, 15,000步, bfloat16），具备可复现性。

## 关联研究分析

从问题动机看，TokenLight与PI-Light（Liang et al., 2026）均致力于提升重光照的物理一致性，但路线截然不同。PI-Light采用两阶段方法，先通过逆向神经渲染分解内在属性，再基于灰球光照条件微调扩散模型，强调显式的物理分解以确保材质和几何不变。TokenLight则完全摒弃显式分解，依赖大规模合成数据让模型隐式学习光-场景交互。这种差异源于对“物理一致性”的不同定义：PI-Light追求因果可解释性，TokenLight追求视觉逼真度与控制的解耦。TokenLight在透明材质和复杂遮挡上的表现优于基于2.5D重建的Careaga et al.，暗示隐式学习可能比显式几何估计更鲁棒，但其在极端光照下的物理幻觉风险未被定量评估。

从方法设计看，TokenLight与RelightMaster（Bian et al., 2025）同属参数化控制路线，但控制粒度不同。RelightMaster使用多平面光图像（MPLI）作为视频重光照的条件，侧重于时间一致性和动态光照；TokenLight使用属性令牌，侧重于单帧图像的空间精度。TokenLight的令牌表示更紧凑，适合实时交互，但缺乏时间维度建模。相比之下，DiffusionRenderer（Zhang et al., 2025）在统一扩散管道中显式建模逆向分解与正向重合成，虽然物理一致性更强，但计算成本更高且控制接口不如TokenLight直观。TokenLight的创新在于将3D光照属性直接嵌入2D扩散模型的条件空间，实现了无需几何重建的精细控制，这一设计在单帧图像任务上具有优势，但在视频或3D场景任务中是否可扩展，论文未给出回答。

## 总结

TokenLight解决的核心矛盾是图像重光照中精细控制与物理一致性的张力。现有方法要么依赖脆弱的3D重建，要么使用粗粒度的环境图条件，无法实现近场光源的精确空间定位。TokenLight通过将物理光照属性编码为扩散Transformer的令牌，利用大规模合成数据隐式学习光-场景交互，实现了无需显式几何分解的端到端重渲染。在合成PointGT上，其PSNR达到21.9772，显著优于Neural Gaffer的16.7595；在真实VisibleFixture-60上，PSNR为20.0772，验证了其在真实场景中的有效性。然而，实验未覆盖MIT MIIW等通用室内场景基准，且缺乏对极端光照下物理幻觉的定量评估。当输入图像包含复杂间接光照或自发光物体时，隐式学习的物理一致性是否会出现系统性偏差，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.15310)
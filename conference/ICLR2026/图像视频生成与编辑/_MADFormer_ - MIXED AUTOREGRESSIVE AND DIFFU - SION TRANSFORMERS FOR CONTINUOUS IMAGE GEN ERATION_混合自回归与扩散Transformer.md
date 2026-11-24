# ICLR2026最新论文 ｜_MADFormer_ : MIXED AUTOREGRESSIVE AND DIFFU - SION TRANSFORMERS FOR CONTINUOUS IMAGE GEN ERATION ｜混合自回归与扩散Transformer

研究机构：清华大学、美国华盛顿大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_75227605)

> 多模态生成中，自回归（AR）擅长全局结构建模但细节粗糙，扩散模型（Diffusion Model）擅长局部细节但采样步数多导致延迟高。现有混合架构缺乏对AR与扩散层容量分配的系统性指导，导致在低计算预算下效率-质量权衡失衡。MADFormer通过块级AR条件与层间AR/扩散分割，在有限推理步数下显著降低FID。其价值在于提供了可操作的容量分配指南，但绝对生成质量受限于训练步数，未达SOTA。

## 研究背景

当多模态模型尝试统一文本与图像生成时，离散AR模型在视觉token上引入量化伪影，而连续扩散模型虽保真度高却需数十步迭代去噪，导致实时交互场景下的推理延迟成为瓶颈。这一矛盾催生了混合架构路线，旨在结合AR的结构效率与扩散的细节精度。

现有混合方法如Transfusion和ACDiT已验证了AR与扩散共存的可行性，但多聚焦于架构可行性证明，缺乏对“如何分配模型深度给AR与扩散”这一核心设计变量的系统消融。在低推理预算（低NFE）场景下，盲目增加扩散层或AR层均无法最优平衡质量与速度。MADFormer将研究重心从“能否混合”转向“如何最优混合”，通过控制变量实验揭示层间分配与块级粒度对效率-质量权衡的影响规律。

## 核心方法

### 统一Transformer骨干与模态解耦

MADFormer基于Llama解码器构建单一Transformer，通过独立参数集（Text Tower, Clean Tower, Noise Tower）处理不同模态。图像经Stable Diffusion VAE压缩为连续潜变量，线性化后与文本token交错。关键差异在于不显式注入时间步条件，而是通过U-Net下采样器将时间步信息编码进图像潜变量，简化了注意力掩码设计。

### 块级AR条件与层间混合机制

在Token轴上，图像潜变量被划分为粗粒度块（如16块），块间采用因果注意力进行AR建模，块内采用双向注意力。在深度轴上，Transformer前$N-D$层作为AR条件模块，计算全局先验$z_{cond}$；后$D$层执行扩散去噪。AR阶段输出条件表示：

$$ z_{cond} = \text{Decoder}_{1:N-D}(\text{PosEnc}(z_{text}, z_{image}^{clean})) $$

扩散阶段结合噪声潜变量$\sqrt{\bar{\alpha}_t}z_{image} + \sqrt{1-\bar{\alpha}_t}\epsilon$与条件$z_{cond}$，预测干净潜变量：

$$ \hat{z}_{image} = \text{Proj}(\text{Decoder}_{N-D+1:N}(\sqrt{\bar{\alpha}_t}z_{image} + \sqrt{1-\bar{\alpha}_t}\epsilon, z_{cond})) $$

该设计动机在于：AR层提供强初始化，使扩散层在少步迭代中即可收敛，解决了纯扩散模型在低NFE下细节缺失的问题。

## 实验评估

实验在FFHQ-1024（70k样本）和ImageNet 256×256（1.28M样本）上进行，使用DDIM采样器。基线覆盖不同AR/扩散层比例配置，但未直接对比SOTA纯扩散模型（如DiT-XL），因训练步数（50 epochs）远低于SOTA（800 epochs）且未使用CFG，绝对FID偏高。

| 配置 | FFHQ FID | ImageNet FID |
| :--- | :--- | :--- |
| AR Length l=16 | 17.8 | 30.0 |
| AR Length l=64 | 21.9 | 34.5 |
| Clean Blocks + Condition | 17.8 | 30.0 |
| Clean Blocks Only | 20.1 | 31.9 |

消融显示，AR长度（块数）对质量影响显著：l=16优于l=64，表明中等粒度块级AR建模优于过细粒度。引入Clean Blocks与Condition联合损失比单独使用任一组件FID降低2.1-1.9。在低NFE（如280）下，AR-heavy配置（3:1 AR:Diffusion）比全扩散配置FID降低60-75%，验证了AR层在结构建模上的计算效率优势。

评估边界在于：FID计算基于50k样本（ImageNet）或8k样本（FFHQ），未报告置信区间；训练步数少导致绝对性能受限，无法直接对比SOTA；代码未公开，超参数细节仅部分披露，可复现性受限。

## 关联研究分析

从问题动机看，MADFormer与Transfusion（Zhou et al., 2024）均探索AR-扩散混合，但Transfusion侧重统一序列建模，MADFormer聚焦层间容量分配。差异根源在于任务特性：Transfusion面向通用多模态，MADFormer针对图像生成效率优化。MADFormer未探索文本生成侧的AR-扩散混合，是否因图像生成对延迟更敏感？

从方法设计看，MADFormer借鉴ACDiT（Hu et al., 2024）的块级AR条件，但扩展了层间比例可变性。ACDiT固定层分配，MADFormer通过消融揭示最优比例随NFE变化。这一差异源于MADFormer将“容量分配”作为独立研究变量，而ACDiT将其视为架构细节。MADFormer未分析AR层比例随分辨率变化的规律，是否因实验仅覆盖256×256和1024×1024？

## 总结

MADFormer解决的核心矛盾是混合架构中AR与扩散层容量分配缺乏系统指导。其切入点是控制变量实验，通过固定总深度、变化AR/扩散层比例，揭示低NFE下AR-heavy配置的优势。方法上，它通过块级AR条件与层间分割，在FFHQ-1024低NFE下实现FID降低60-75%。边界在于训练步数少（50 epochs）导致绝对FID（30.0）远高于SOTA（1.82），且未使用CFG，掩盖了语义对齐能力。当分辨率提升至4K时，块级AR的因果注意力计算量是否呈二次方增长，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_75227605)
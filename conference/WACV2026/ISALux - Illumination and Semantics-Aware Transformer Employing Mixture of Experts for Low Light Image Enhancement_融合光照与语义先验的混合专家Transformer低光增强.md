# WACV2026最新论文 ｜ISALux: Illumination and Semantics-Aware Transformer Employing Mixture of Experts for Low Light Image Enhancement ｜融合光照与语义先验的混合专家Transformer低光增强

研究机构：英国曼彻斯特大学

作者：Raul Balmez、Alexandru Brateanu、Ciprian Orhei 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_fb58d73dcd5d)

> 低光图像增强（Low-Light Image Enhancement, LLIE）旨在从曝光不足、噪声严重的视觉数据中恢复自然光照外观，其核心驱动力源于自动驾驶、安防监控及移动计算摄影对夜间感知能力的迫切需求。现有基于卷积神经网络（CNN）或标准Transformer的方法往往对所有像素施加均匀增强，忽略了非均匀光照下不同物体区域对亮度校正的差异化需求，导致色彩失真或细节丢失。ISALux通过设计混合光照与语义感知多头自注意力（HISA-MSA）模块，将全局光照上下文与局部语义结构同时嵌入注意力计算，并引入混合专家（MoE）前馈网络以自适应处理不同光照缺陷。该架构在多个基准上取得了有竞争力的性能，但其对预训练语义分割模型的依赖以及未显式建模噪声分布的设计，限制了其在极端低光场景下的泛化能力。

## 研究背景

当传感器在弱光环境下工作时，光子极度匮乏导致信号强度低于噪声底限，图像不仅亮度不足，还伴随严重的散粒噪声与色彩失真。传统直方图均衡化等手工先验难以处理这种复杂退化，而早期基于CNN的方法虽能学习像素映射，却受限于局部感受野，无法有效建模非均匀光照下的全局一致性。Retinex理论的引入将图像分解为光照与反射率分量，确立了物理可解释的增强范式，但光照估计在极端低光下对噪声极度敏感，且多数方法仍采用统一的增强策略，未考虑图像中不同语义区域（如天空与地面）对光照校正的差异化需求。

主流路线中，RetinexFormer（Cai et al., 2023）利用Transformer捕获全局光照依赖，但其注意力机制仅依赖光照先验，缺乏对局部结构信息的显式建模；Zero-DCE等无监督方法解决了配对数据稀缺问题，但受限于预训练模型的先验，恢复图像常出现视觉质量次优。ISALux的切入点在于指出，有效的低光增强需同时利用全局光照上下文与局部语义结构，以应对真实场景中不同物体或实例需要不同光照水平的挑战。

## 核心方法

### 方法参照系

ISALux基于U-shaped Transformer编码器-解码器架构，与RetinexFormer共享全局依赖建模的框架，但关键差异在于其将语义分割先验与光照先验同时注入自注意力机制，并采用MoE替代标准前馈网络，以实现非均匀增强与自适应缺陷处理。

### 混合光照与语义感知多头自注意力

标准Transformer的自注意力模块对所有像素一视同仁，导致非均匀光照下增强策略的偏差。ISALux设计HISA-MSA模块，通过两个并行的多头自注意力分支分别处理光照与语义特征，再交叉富集。具体而言，输入特征 $F_{in} \in \mathbb{R}^{H \times W \times C}$ 经3x3卷积投影为 $Q, K, V$，随后引入低秩适配（LoRA）正则化项：

$$ \Delta q = (F'_{in} \cdot \alpha_q) \cdot \beta_q, \quad \Delta k = (F'_{in} \cdot \alpha_k) \cdot \beta_k, \quad \Delta v = (F'_{in} \cdot \alpha_v) \cdot \beta_v $$

其中 $\alpha, \beta$ 为低秩矩阵，用于防止模型对特定光照模式过拟合。更新后的 $Q, K, V$ 分别计算自注意力，得到光照注意力图 $M_I$ 与语义注意力图 $M_S$，再与对应先验图 $F_{P_i}, F_{P_s}$ 逐元素相乘，最后通过可学习参数 $\nu, \omega$ 加权求和：

$$ M_E = \nu \cdot M_I + \omega \cdot M_S $$

这一设计使光照信息调节全局亮度上下文，语义信息突出结构变化，解决了单一先验导致的局部细节丢失问题。

### 混合专家前馈网络

标准前馈网络对所有特征施加相同变换，难以应对低光图像中噪声、模糊、色彩失真等多样化缺陷。ISALux采用稀疏MoE-FFN，通过门控机制选择Top-K专家（实验中K=2）进行专业化处理。门控分数 $G$ 由输入特征的平均池化计算：

$$ G = \text{softmax}(W_g \cdot \text{avgpool}(F'_{in})) $$

每个专家为独立CNN，输出按门控概率加权求和。该机制使模型能自适应激活不同专家处理特定缺陷，如一个专家专注去噪，另一个专注细节恢复，提升了上下文特征提取的灵活性。

## 实验评估

ISALux在LOL、SDSD及LOL-Blur数据集上评估，基线覆盖RetinexFormer、GLARE、LL-SKF等监督方法，但缺失Zero-DCE++、DiffLL等无监督/生成式强基线。在LOL-v1上，ISALux取得28.01 dB PSNR，较LL-SKF提升0.84 dB；在LOL-v2-Real上，较RetinexFormer提升2.05 dB，较GLARE提升0.78 dB，表明其在真实场景下具有优势。

| 数据集 | 方法 | PSNR (dB) | SSIM |
| :--- | :--- | :--- | :--- |
| LOL-v1 | RetinexFormer | 22.90 | 0.824 |
| LOL-v1 | ISALux | 28.01 | 0.903 |
| LOL-v2-Real | RetinexFormer | 22.90 | 0.824 |
| LOL-v2-Real | ISALux | 25.51 | 0.881 |

消融实验显示，结合光照与语义先验比无先验提升0.59 dB，加入LoRA再提升0.22 dB；损失函数中，L2+VGG19+MS-SSIM组合比单一L2提升0.68 dB，表明感知与结构损失的协同作用关键。剪枝实验表明，50%剪枝后PSNR降至23.67 dB，SSIM降至0.804，显示模型对参数压缩敏感。

评估指标以PSNR/SSIM为主，缺乏LPIPS/FID等感知指标，且未报告计算效率（FLOPs/推理时间）的详细对比。代码未公开，超参数（如学习率调度）虽详细描述，但GPU型号未提及，可复现性受限。

## 关联研究分析

从问题动机看，ISALux与RetinexFormer均基于Retinex理论，但RetinexFormer仅利用光照先验建模全局依赖，而ISALux引入语义先验以解决非均匀光照下的局部增强偏差。这一差异源于ISALux认为语义结构对光照校正具有调制作用，但论文未验证MobileNetV3在低光下的分割精度是否足以支撑该假设，若分割误差较大，语义先验可能引入噪声。

从方法设计看，ISALux与GLARE同属Transformer架构，但GLARE采用标准FFN，而ISALux引入MoE以处理多样化缺陷。MoE的稀疏激活机制理论上提升效率，但实验中K=2专家的选择基于PSNR边际收益（≈0.05 dB），未探讨专家数量对泛化性的影响。此外，ISALux未显式建模噪声分布，而领域共识指出低光噪声具有信号依赖性，简单加性高斯假设不适用，这可能限制其在极端低光下的去噪能力。

## 总结

ISALux旨在解决非均匀光照下不同物体区域需差异化增强的矛盾，通过HISA-MSA融合光照与语义先验，并引入MoE-FFN自适应处理缺陷，在LOL-v1上取得28.01 dB PSNR，较RetinexFormer提升5.11 dB。其边界在于依赖预训练MobileNetV3的语义分割精度，且未显式建模信号依赖性噪声，导致在LOL-v2-Real上性能（25.51 dB）低于生成式方法DiffLL（28.86 dB）。当语义分割在极端低光下精度下降时，HISA-MSA的语义富集是否仍能有效调节增强策略，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_fb58d73dcd5d)
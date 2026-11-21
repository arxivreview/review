# WACV2026最新论文 ｜Codebook Knowledge with Mamba-Transformer For Low-Light Image Enhancement ｜基于码本域适应与混合架构的低光图像增强

研究机构：中国科学技术大学、华东师范大学

作者：Runhua Deng、Aiwen Jiang、Long Peng 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4dc2c478802c)

> 低光图像增强面临噪声、亮度不足与色彩失真的多重耦合退化，传统监督方法难以覆盖所有退化类型，而现有码本方法在低光特征与高质量码本间存在显著域间隙，导致检索失效。CodeMTNet将向量量化码本重构为域适应范式，通过隐式神经表示正则化调整低光特征分布，并引入Mamba-Transformer混合模块提升检索精度。该方法在LOLv1上取得23.400 dB PSNR，优于同类码本方法，但整体性能低于当前扩散模型SOTA，其泛化边界与计算效率仍需进一步验证。

## 研究背景

低光图像增强需同时处理亮度校正、噪声抑制与细节保留，这要求模型具备对复杂退化模式的鲁棒性。向量量化码本（VQ-Codebook）通过存储高质量图像特征提供先验知识，但低光输入特征与码本分布存在域间隙，导致最近邻匹配失效。隐式神经表示（INR）能学习连续域信息，但传统INR在低光场景下易过拟合平均光照，无法处理非均匀亮度分布。

主流LLIE方法分为监督与无监督两类：监督方法依赖配对数据，泛化性受限于训练分布；无监督方法如Zero-DCE通过曲线估计避免配对需求，但难以恢复复杂纹理。码本方法如GLARE和RQ-LLIE尝试利用高质量先验，但前者依赖生成流对齐分布，后者通过残差量化扩展码本容量，均未有效解决低光特征与码本的域间隙问题。CodeMTNet的切入点在于将码本检索视为域适应任务，通过特征分布调整而非码本结构修改来弥合间隙，从而在保持码本知识完整性的同时提升检索鲁棒性。

## 核心方法

### 码本预训练与域适应编码器

码本预训练阶段利用VQGAN框架从DIV2K和Flickr2K正常光图像中学习统一高质量知识，通过像素损失、感知损失、对抗损失和码本特征匹配损失优化。域适应编码器（DAE）嵌入Neural Representation Lighter（NRL）模块，利用INR学习上下文感知光照估计。NRL通过高频函数映射像素坐标，恢复高频细节$F_{l_3}$，与原始特征$F_l$通道拼接后，经三层卷积网络生成光照估计图$F_{map}$，最终通过$F_{l'} = F_{map} \odot F_l + F_l$实现亮度增强。该设计解决了传统INR仅学习平均光照、无法处理非均匀亮度分布的问题，使低光特征分布逐步逼近高质量域。

### 混合Mamba-Transformer检索模块

Mamba-Transformer辅助码本检索块（MCRB）在DAE输出特征后执行，由6个Mamba块和2个Transformer块组成。Mamba块利用状态空间模型（VSSM）以线性复杂度提取特征，Transformer块提供非线性细化能力，共同预测高质量token特征。训练目标包含交叉熵损失$L_{code}^{token}$监督码本索引预测，以及L2损失$L_{code}^{feat'}$约束低光特征$Z_l$逼近高质量量化特征$Z_c$：

$$L_{dae\_mcrb} = \lambda_1 \cdot L_{code}^{feat'} + \lambda_2 \cdot L_{code}^{token}$$

其中$\lambda_1=0.2$，$\lambda_2=2.0$。该混合架构解决了纯Transformer堆叠计算成本高、性能增益边际递减的问题，Mamba块高效提取特征，少量Transformer块实现峰值性能，推理时间仅增加约5%。

### 可控特征融合模块

可控特征融合（CFF）模块在解码器端解决码本检索导致的结构信息丢失问题。CFF通过轻量网络$\mathcal{M}_\theta$从拼接特征$Concat(F_h, F_l)$预测融合参数$\alpha$和$\beta$，结合可调参数$w \in [0,1]$控制融合强度：

$$F_{h'} = F_h + (\beta \odot F_h + \alpha) \times w$$

该数据驱动自适应融合方法替代了固定启发式规则，通过调整$w$平衡恢复质量与保真度，解决了最近邻匹配逐像素处理、忽略结构信息导致的纹理失真问题。

## 实验评估

实验在LOLv1、LOLv2-real和LOLv2-synthetic数据集上进行，基线覆盖Zero-DCE、RetinexMamba、NeRCo等主流方法，但缺失DiffLL等最新扩散模型基线。CodeMTNet在LOLv1上PSNR 23.400 dB、LPIPS 0.0647，优于CodeEnhance（22.900 dB）和RetinexMamba（22.843 dB），LPIPS显著低于所有对比方法，表明感知质量更优。

| 方法 | PSNR↑ | SSIM↑ | LPIPS↓ |
| :--- | :--- | :--- | :--- |
| ZeroDCE | 14.861 | 0.559 | 0.3356 |
| RetinexMamba | 22.843 | 0.821 | 0.0943 |
| CodeEnhance | 22.900 | 0.842 | 0.1268 |
| CodeMTNet | 23.400 | 0.842 | 0.0647 |

消融实验显示，MCRB中6-2配置（6 Mamba+2 Transformer）PSNR 23.400 dB，优于8-0配置（22.757 dB）和0-8配置（22.425 dB），验证了混合架构的效率优势。NRL中$\lambda=32$时PSNR 23.400 dB，$\lambda=64$时PSNR 22.921 dB，表明$\lambda$过大导致过拟合。CFF模块贡献0.657 dB PSNR提升，证明其对结构信息恢复的关键作用。

| 配置 | PSNR↑ | SSIM↑ | LPIPS↓ |
| :--- | :--- | :--- | :--- |
| 4-2 | 23.050 | 0.837 | 0.1026 |
| 8-0 | 22.757 | 0.838 | 0.0984 |
| 0-8 | 22.425 | 0.831 | 0.1046 |
| CodeMTNet(6-2) | 23.400 | 0.842 | 0.0647 |

评估指标包含PSNR、SSIM、LPIPS，但未报告FLOPs、参数量等效率指标（除MCRB消融外）。代码开源，但预训练数据分布（DIV2K/Flickr2K）可能限制泛化性，论文未提供跨域测试的详细分析。

## 关联研究分析

从问题动机看，CodeMTNet与NeRCo均使用INR，但NeRCo将INR用于去噪，CodeMTNet将其用于光照估计以解决非均匀亮度问题。这一差异源于任务特性：低光增强需同时处理亮度校正与细节保留，而NeRCo聚焦单一退化模式。CodeMTNet的域适应范式更适用于多退化耦合场景，但INR在极端低光下的泛化性未充分验证。

从方法设计看，CodeMTNet与RetinexMamba均使用Mamba，但RetinexMamba将Mamba嵌入U-Net直接增强，CodeMTNet将其用于码本检索。这一差异反映了码本方法的核心挑战：检索精度依赖特征分布匹配，而直接增强方法无需此步骤。CodeMTNet的混合架构在检索任务中效率优势显著，但在直接增强任务中是否优于纯Mamba架构，论文未给出对比。

## 总结

CodeMTNet解决的核心矛盾是多退化耦合下码本检索的域间隙问题，其切入点在于将码本检索重构为域适应任务，通过特征分布调整而非码本结构修改来弥合间隙。方法通过NRL调整低光特征分布，MCRB提升检索精度，CFF恢复结构信息，在LOLv1上PSNR 23.400 dB、LPIPS 0.0647，优于同类码本方法。边界在于整体性能低于扩散模型SOTA（据领域综述DiffLL 26.34 dB），且预训练数据分布可能限制泛化性。当测试集包含训练分布外的极端低光场景时，码本检索的鲁棒性是否下降，论文未提供充分证据。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_4dc2c478802c)
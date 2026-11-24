# CVPR2026最新论文 ｜DA-Mamba: Learning Domain-Aware State Space Model for Global-Local Alignment in Domain Adaptive Object Detection ｜域自适应目标检测中的全局-局部对齐：基于状态空间模型的混合架构

研究机构：中国科学院、中科院计算所

作者：Haochen Li、Rui Zhang、Hantao Yao 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.18757)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.18757)

> 域自适应目标检测（Domain Adaptive Object Detection, DAOD）旨在解决检测器从有标签源域迁移至无标签目标域时因分布偏移导致的性能下降。现有基于卷积神经网络（CNN）的方法受限于局部感受野，难以捕捉跨区域的长程依赖，而引入视觉Transformer虽能解决全局对齐问题，却带来二次方计算复杂度，阻碍了实时部署。本文提出DA-Mamba，通过设计图像感知与对象感知的状态空间模型（State Space Models, SSM）模块，在保持线性计算复杂度的同时实现全局与局部域不变特征的联合提取。该架构在效率与精度间取得了显著平衡，但其绝对精度仍低于部分基于视觉基础模型的最新方法，且未充分验证在极端内容级域偏移下的鲁棒性。

## 研究背景

当检测器面对跨域场景时，源域与目标域数据分布的差异导致模型泛化能力失效，这一现象称为分布偏移。为缓解此问题，DAOD利用源域标注数据提升目标域检测性能，其核心在于提取域不变特征。早期方法通过对抗学习对齐特征分布，但CNN的局部连接特性使得对齐局限于局部区域，无法捕捉如物体共现模式或类别语义关联等全局视觉属性。

主流路线试图通过引入视觉Transformer的全局注意力机制来突破CNN的局部性限制，但自注意力机制的二次方复杂度导致巨大的计算与内存开销，难以满足自动驾驶等实时场景需求。部分基于卷积的注意力变体虽试图降低复杂度，但往往依赖全局参数共享而忽略域偏差，或仍隐含二次方复杂度。本文的切入点在于利用状态空间模型（SSM）的线性时间复杂度长程建模能力，将其与CNN结合，以在保持高效推理的同时补充全局域信息。

## 核心方法

### 方法参照系

本文基于YOLO架构实现单阶段检测器，采用无监督域自适应（Unsupervised Domain Adaptation, UDA）设定。标准流程包含源域监督损失、目标域伪标签半监督损失以及图像级与实例级对抗损失。本文的关键差异在于骨干网络与检测头中嵌入SSM模块，以替代或补充传统的局部卷积特征提取，实现全局-局部对齐。

### 图像感知状态空间模型（IA-SSM）

IA-SSM嵌入骨干网络的FPN下采样流，旨在解决CNN仅能提取局部域不变特征的问题。该模块采用双管线架构，分别通过卷积管线提取局部特征，通过SSM管线提取全局特征。输入特征 $\mathbf{f}_{in}$ 首先与可学习的图像级视觉提示 $\mathbf{v}_I$ 拼接，随后通过降维卷积 $E_S, E_C$ 降低维度。SSM管线利用Mamba层 $M$ 捕捉长程依赖，公式为：

$$ \mathbf{z}_S = E_O(M(E_S(\mathbf{f}))) $$

其中 $E_O$ 为升维卷积。卷积管线提取局部特征 $\mathbf{z}_C$，最终输出 $\mathbf{f}_{out} = E_O([\mathbf{z}_S; \mathbf{z}_C])$。这一设计使骨干网络同时具备局部与全局域感知能力，增强了图像级对齐。

### 对象感知状态空间模型（OA-SSM）

OA-SSM嵌入检测头，旨在建模实例间的空间与语义依赖。与IA-SSM不同，OA-SSM的视觉提示 $\mathbf{v}_O$ 需满足像素级与类别条件化要求。通过可学习元网络将输入特征投影为类别相似度矩阵 $\mathbf{W}$，并与CLIP文本编码器生成的类别原型 $\mathbf{E}$ 相乘，得到实例级视觉提示：

$$ \mathbf{v}_O = \mathbf{W} \mathbf{E} $$

该提示将特征图划分为实例级语义区域，使同一实例区域内的像素共享一致的类别语义。OA-SSM随后将 $\mathbf{v}_O$ 与输入特征拼接，通过双管线提取实例级空间与语义依赖，促进实例级对齐。

## 实验评估

实验在Cityscapes→Foggy Cityscapes、Cityscapes→BDD100K、Pascal VOC→Clipart及Pascal VOC→Comic四个基准上进行，评估指标为mAP@0.5。基线覆盖CNN（如DA-Faster, CAT）与Transformer（如DATR, DA-Pro）方法，但缺失基于视觉基础模型（VFM）的最新强基线（如ETS）。

| 基准 | 方法 | mAP (%) |
| :--- | :--- | :--- |
| Cityscapes→Foggy | DA-Mamba | 58.1 |
| Cityscapes→Foggy | DATR | 55.9 |
| Pascal VOC→Clipart | DA-Mamba | 52.5 |
| Pascal VOC→Clipart | CAT | 49.1 |

DA-Mamba在Cityscapes→Foggy上较SOTA方法DATR提升2.2%，在Pascal VOC→Clipart上较CAT提升3.4%。计算开销方面，DA-Mamba的FLOPs仅为Transformer-based方法DATR的50.2%，推理速度提升2.62倍，验证了SSM在效率上的优势。

消融实验显示，IA-SSM与OA-SSM分别带来2.6%~4.5%和2.7%~3.7%的mAP提升，两者结合总提升达5.7%~6.8%。与标准Mamba层相比，DA-Mamba的域感知设计在四个基准上均高出1.0%~2.9%，表明直接应用Mamba因缺乏域对齐机制而表现次优。卷积管线与SSM管线均不可或缺，分别贡献0.4%~1.9%和0.8%~2.0%的提升。

评估边界方面，论文未报告置信区间，且未包含VFM-based基线对比，限制了与最新SOTA的直接比较。实验在单块Tesla V100 GPU上进行，超参数设置明确，但代码未公开，可复现性受限。

## 关联研究分析

从问题动机看，DA-Mamba与DATR均旨在解决CNN局部性导致的全局对齐缺失，但DATR依赖Transformer的二次方复杂度，而DA-Mamba通过SSM实现线性复杂度。这一差异源于任务对实时性的要求：DATR更关注精度上限，而DA-Mamba兼顾效率与精度。然而，DA-Mamba在Cityscapes→Foggy上的58.1% mAP低于据领域综述中DSBCO的64.7%，暗示SSM的全局对齐能力在复杂天气场景下可能不及基于伪标签精炼的方法。

从方法设计看，DA-Mamba与PAGen均探索非对抗对齐策略，但PAGen基于频域相位不变性，而DA-Mamba基于SSM长程依赖。PAGen假设相位在域间不变，适用于纹理或光照变化场景；DA-Mamba则通过显式建模空间与语义依赖，适用于更广泛的域偏移类型。两者均未充分验证在内容级域偏移（如物体形状变化）下的表现，这一盲区可能源于现有基准主要关注风格偏移。

## 总结

DA-Mamba旨在解决CNN局部性与Transformer高计算复杂度之间的矛盾，通过引入域感知的SSM模块实现全局-局部对齐。该方法在Cityscapes→Foggy上达到58.1% mAP，较Transformer-based SOTA提升2.2%，且FLOPs降低至50.2%。然而，其绝对精度低于基于VFM的最新方法，且未验证在极端内容级域偏移下的鲁棒性。当域偏移从风格变化转向物体形状或语义结构变化时，SSM的长程依赖建模是否仍能保持优势，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.18757)
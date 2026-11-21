# CVPR2026最新论文 ｜Leveraging Class Distributions in CLIP for Weakly Supervised Semantic Segmentation ｜基于类分布的CLIP弱监督语义分割

研究机构：英国利物浦大学

作者：Ziqian Yang、Xinqiao Zhao、Xiaolei Wang 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_25241badab10)

> 图像级弱监督语义分割（WSSS）的核心痛点在于CLIP生成的类激活图（CAM）仅覆盖显著区域，导致细粒度定位失效。现有基于多头自注意力（MHSA）亲和度的细化方法因无法建立准确的类内语义关系，致使目标类激活不足。本文提出CD-CLIP框架，通过Jensen-Shannon散度构建类分布相似度矩阵修正亲和度，并引入DINO特征生成超类边界监督。该方法在PASCAL VOC 2012上取得82.5% mIoU，但依赖外部DINO特征解决边界过激活问题，其纯CLIP内部机制的完备性存疑。

## 研究背景

图像级WSSS旨在利用仅含类别标签的弱监督信号生成像素级分割。由于缺乏像素级标注，模型需依赖类激活图（CAM）将全局类别预测映射到空间位置。然而，CLIP的全局对比学习范式导致其[CLS]特征缺乏空间细节，初始CAM往往仅激活物体最显著的部分（如“人”的躯干而忽略头部），形成“全局语义强、局部定位弱”的结构性矛盾。

主流单阶段WSSS方法（如ToCo、WeCLIP）尝试利用ViT编码器中的MHSA权重构建patch间亲和度，以扩展CAM激活区域。然而，MHSA亲和度主要捕捉空间邻近性，难以建立跨区域的准确类内语义关系，导致目标类部分区域持续处于未激活状态。本文切入点在于发现CLIP文本编码器生成的全类别分布中蕴含比单一目标类激活更丰富的语义信息：同一目标类的不同patch虽对目标类响应不同，但其全类别分布高度相似。这一发现为利用分布知识修正亲和度提供了理论依据。

## 核心方法

### 方法参照系

单阶段CLIP-WSSS的标准流程为：冻结CLIP骨干生成初始CAM，利用MHSA权重构建亲和度矩阵细化CAM，最后通过解码器输出分割。本文的关键差异在于将亲和度构建从“空间邻近性”转向“类分布相似性”，并引入外部DINO特征解决边界模糊问题。

### 类分布感知（CDA）模块

CDA模块旨在解决MHSA亲和度无法建立准确类内关系导致的激活不足问题。传统方法直接使用MHSA权重 $A_{init}$ 进行CAM细化，但 $A_{init}$ 中不同类patch间的错误关联会抑制目标类激活。本文首先计算图像特征 $F$ 与所有文本特征 $T_{all}$（含目标类与超类）的注意力图 $S_a$，并通过Softmax估计每个patch的类分布。随后，利用Jensen-Shannon（JS）散度构建类分布相似度矩阵 $S_d$：

$$
\mathbf{S}_d = \frac{(1 - \mathbf{D}_{JS}(\text{Softmax}(\mathbf{S}_a) \| \text{Softmax}(\mathbf{S}_a)^T))}{\tau}
$$

该公式通过JS散度量化patch间类分布的差异，分布越相似则 $S_d$ 值越大。最终，CDA亲和度 $A_d$ 通过 $A_d = \text{Softmax}(S_d) \cdot A_{init}$ 生成，利用分布相似性修正 $A_{init}$ 中的错误关联，使同一目标类的patch在CAM细化过程中被同步激活，从而提升CAM的完整性。

### 超类边界探索（SBE）模块

CDA模块虽提升了类内激活，但不同目标类边界处的patch类分布高度相似，导致CAM在边界区域过激活，产生不准确的边界监督。SBE模块通过引入DINO特征解决此问题。首先，利用CLIP推断的超类CAM $M_s^n$ 对DINO图像特征 $F_d$ 进行类平均池化，生成超类原型 $f_s^n$：

$$
\mathbf{f}_s^n = \text{CAP}(\mathbf{M}_s^n \odot \mathbf{F}_d)
$$

该公式提取每个超类在DINO特征空间中的代表性向量。随后，计算超类原型与DINO特征的余弦相似度生成超类原型CAM $M_p^n$，并通过边界增强损失 $\mathcal{L}_b$ 监督分割预测：

$$
\mathcal{L}_b = \begin{cases} \text{Dice}(\mathbf{P}, \mathbf{Y}_s) & \text{if } |\mathbf{C}_p| \ge 2 \\ 0 & \text{otherwise} \end{cases}
$$

该损失仅在预测包含多个超类时生效，利用DINO特征的强区域分离能力提供精确的超类边界监督，抵消CDA模块导致的边界过激活。

## 实验评估

实验在PASCAL VOC 2012（21类）和MS COCO 2014（81类）上进行，基线覆盖ToCo、WeCLIP、ExCEL等单阶段方法及CPAL、PSDPM等多阶段方法。CD-CLIP在VOC 2012验证集取得82.5% mIoU，测试集82.4%，较基线WeCLIP（76.4%）提升6.1%；在COCO验证集取得54.1% mIoU，较SeCo（46.7%）提升7.4%。

| 方法 | 类型 | VOC 2012 Val (mIoU) | VOC 2012 Test (mIoU) | COCO Val (mIoU) |
| :--- | :--- | :--- | :--- | :--- |
| ToCo | 单阶段 | 42.3 | - | - |
| WeCLIP | 单阶段 | 76.4 | 77.2 | - |
| ExCEL | 单阶段 | 78.4 | 78.5 | - |
| CPAL | 多阶段 | 74.5 | 74.7 | - |
| PSDPM | 多阶段 | 74.1 | 74.9 | - |
| CD-CLIP | 单阶段 | 82.5 | 82.4 | 54.1 |

消融实验显示，CDA模块将CAM mIoU从70.1%提升至80.3%，分割mIoU从68.8%提升至80.2%；SBE模块进一步将分割mIoU提升至81.6%。边界损失 $\mathcal{L}_b$ 仅在多超类图像上生效时，分割mIoU从80.2%提升至81.6%，验证了超类边界监督的有效性。超类集合 $D_s$ 的选择对性能影响显著，使用完整超类集 $D_s$ 时性能最优（81.6%），而移除边界损失后性能降至80.2%。

评估协议采用标准WSSS设置，使用Dense CRF后处理和多尺度推理。代码已开源，但论文未报告计算效率指标。与领域共识相比，CD-CLIP在保持CLIP零样本泛化能力的同时，通过外部DINO特征增强边界精度，符合PEFT保持预训练表示完整性的原则，但引入了额外的DINO编码器计算开销。

## 关联研究分析

从问题动机看，CD-CLIP与WeCLIP同属单阶段CLIP-WSSS路线，但WeCLIP依赖MHSA亲和度直接细化CAM，而CD-CLIP利用类分布JS散度修正亲和度。这一差异源于对MHSA局限性的不同认知：WeCLIP假设MHSA足以捕捉语义关系，而CD-CLIP发现MHSA在类内关系建立上的失效。CD-CLIP的类分布策略更契合CLIP文本编码器的全类别语义特性，但依赖JS散度计算，增加了推理复杂度。

从方法设计看，CD-CLIP与RFCLIP（开放词汇分割）均利用CLIP特征进行细粒度定位，但RFCLIP通过注意力重分配解决全局-局部权衡，而CD-CLIP通过类分布相似性解决激活不足。CD-CLIP引入DINO特征解决边界过激活，这一设计在纯CLIP框架中较为罕见，暗示CLIP内部特征在边界区分上的不足。DINO的引入是否破坏了CLIP纯对比学习的几何一致性，论文未给出理论分析，仅通过实验验证其有效性。

## 总结

CD-CLIP针对CLIP-WSSS中CAM激活不足与边界过激活的矛盾，利用类分布JS散度修正亲和度并引入DINO超类边界监督，在VOC 2012上取得82.5% mIoU。其核心贡献在于发现全类别分布比单一目标类激活蕴含更丰富的语义信息，但依赖外部DINO特征解决边界问题，暴露了CLIP内部特征在边界区分上的局限。当移除DINO特征仅使用CLIP内部机制时，边界过激活问题是否可通过纯CLIP类分布策略完全解决，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_25241badab10)
# CVPR2026最新论文 ｜HOPS: Hierarchical Open-vocabulary Part Segmentation with Attention-Aware Filtering and Affinity-Guided Enhancement ｜层级化开放词汇部件分割

研究机构：天津大学、上海交通大学

作者：Xinlong Li、Di Lin、Shaoyiyi Gao 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e8fc9974eed6)

> 开放词汇部件分割（OVPS）要求模型将物体分解为细粒度语义组件，并泛化至训练阶段未见的部件类别。现有基于视觉-语言模型（VLM）的方法受限于CLIP全局对齐特性，普遍面临物体过分割与部件欠分割的双重失效，导致边界模糊与覆盖不全。本文提出HOPS，通过双向语义-结构注意力融合与亲和引导增强机制，在层级化框架中同时抑制过分割并扩展欠分割区域。该方法在多个基准上取得SOTA性能，但其对微调的依赖与迭代传播的计算开销是否削弱了免训练范式的部署优势，仍存疑。

## 研究背景

VLM（如CLIP）通过对比学习建立图像-文本全局对齐，其patch特征缺乏像素级空间局部性，直接用于密集预测时产生边界模糊。为解决此问题，开放词汇语义分割（OVSS）引入两阶段范式或免训练推理优化，但OVPS额外要求建模物体-部件层级结构，使得空间定位精度与细粒度语义理解成为更严苛的瓶颈。

OVSS领域已形成免训练优化与基础模型集成两条主流路线，前者通过注意力修正提升CLIP特征质量，后者引入DINO/SAM等结构先验。然而，这些方法在OVPS中遭遇新挑战：CLIP对物体级概念激活过强，导致部件级响应被抑制，且缺乏显式空间约束时小部件激活微弱。HOPS的切入点在于利用CLIP语义对齐与DINO结构感知的互补性，通过双向注意力融合与自适应迭代传播，在层级化框架中同时解决过分割与欠分割问题。

## 核心方法

### 层级化分割框架

HOPS基于CATSeg的成本聚合框架，采用两阶段层级化设计。第一阶段进行物体分割，提供空间约束；第二阶段在物体掩码内进行部件分割。关键差异在于引入AFM与AEM模块，将DINO从被动特征提供者升级为主动注意力约束者，以解决OVPS中特有的过分割与欠分割问题。

### 注意力感知过滤模块（AFM）

AFM位于物体分割阶段，旨在抑制CLIP因全局对齐导致的过分割。其设计动机是CLIP注意力常捕获“语义相关但结构无关”的patch对（如牛与草地），而DINO注意力聚焦边界与拓扑结构。AFM通过双向融合机制，利用DINO约束CLIP，同时用CLIP引导DINO，生成语义-结构注意力以精炼成本图。

$$
A_{\text{CLIP} \leftarrow \text{DINO}}^{(l)} = A_{\text{CLIP}}^{(l)} \odot \text{Softmax}\left( A_{\text{DINO}}^{(l)} \right)
$$

该公式表示DINO注意力对CLIP注意力的逐元素乘法，过滤掉结构不一致的语义激活。随后，CLIP注意力均值作为阈值，保留DINO中“结构一致且语义相关”的patch对：

$$
A_{\text{DINO} \leftarrow \text{CLIP}}^{(l)} = A_{\text{DINO}}^{(l)} \odot \mathbb{I}\!\left( A_{\text{CLIP}}^{(l)} > \operatorname{Mean}\!\left( A_{\text{CLIP}}^{(l)} \right) \right)
$$

最终，两路注意力加权融合为语义-结构注意力 $A$，并结合可靠关联掩码与类别置信掩码，增强目标区域激活、抑制无关区域响应，从而缓解过分割。

### 亲和引导增强模块（AEM）

AEM位于部件分割阶段，承接AFM输出的物体掩码，旨在缓解部件欠分割。其设计动机是初始部件响应微弱，需通过迭代传播扩展激活区域。AEM构建基于语义-结构注意力的亲和矩阵 $A_{\text{aff}}$，并在边界框约束下进行自适应迭代增强。

$$
\mathbf{S}_2^{\text{enh},t}(c) = \mathbf{B}^{t-1}(c) \odot A_{\text{aff}} \cdot \mathbf{S}_2^{\text{enh},t-1}(c)
$$

该公式表示第 $t$ 次迭代中，边界框掩码 $\mathbf{B}$ 约束传播范围，亲和矩阵 $A_{\text{aff}}$ 引导响应从显著区域向边界扩散。每次迭代计算增益 $\text{Gain}(t)$，若为正则继续迭代，否则停止，防止过度传播导致响应模糊。

## 实验评估

实验在Pascal-Part-116、ADE20K-Part-234与PartImageNet上进行，基线覆盖PartCATSeg、PBAPS等OVPS经典方法，但未对比OVSS SOTA（如OV-Stitcher），因任务不同。主结果显示，HOPS在Pascal-Part-116上h-IoU达49.29%，较PartCATSeg（45.77%）提升3.52%；mOSI降至23.46%（PartCATSeg为29.57%），表明过分割显著缓解。

| 方法 | Seen mIoU | Unseen mIoU | h-IoU | mOSI ↓ | mUSI ↓ |
| --- | --- | --- | --- | --- | --- |
| PartCATSeg | 52.62 | 40.51 | 45.77 | 29.57 | 37.79 |
| HOPS | 54.77 | 44.81 | 49.29 | 23.46 | 31.62 |

消融实验显示，AFM中语义-结构注意力提升h-IoU并降低mOSI/mUSI；AEM中边界框约束比初始掩码更有效，自适应迭代防止响应模糊。mOSI与mUSI的降低未以牺牲mIoU为代价，反而同步提升，验证了过分割与欠分割缓解的协同性。

评估边界方面，指标完备性良好，但评估协议未涵盖计算效率维度，且跨数据集泛化实验仅覆盖PartImageNet→Pascal-Part-116，未测试更复杂域偏移场景。代码已开源，但超参数细节（如迭代次数、阈值）在正文中未完全披露，可复现性依赖补充材料。

## 关联研究分析

从问题动机看，HOPS与PartCATSeg同属OVPS任务，但PartCATSeg仅将DINO特征拼接至成本嵌入，作为被动结构引导；HOPS则通过双向注意力融合，使DINO主动约束CLIP的语义激活，根源在于OVPS对细粒度定位的更高要求，被动特征拼接无法有效抑制CLIP的过分割。

从方法设计看，HOPS与SCLIP同属免训练推理优化路线，但SCLIP仅修改CLIP自注意力，未引入外部结构先验；HOPS结合DINO结构感知，通过AFM/AEM实现语义-结构互补。差异源于任务特性：OVSS侧重全局语义匹配，而OVPS需同时处理物体级过分割与部件级欠分割，单一注意力修正不足以解决双重失效。

## 总结

HOPS要解决的核心矛盾是CLIP全局对齐导致的物体过分割与部件欠分割在OVPS中的共存问题。现有方法或依赖被动特征拼接，或仅修正单一注意力机制，无法同时抑制过分割并扩展欠分割区域。HOPS通过双向语义-结构注意力融合与自适应迭代传播，在层级化框架中实现双重失效的协同缓解。实验证明，其在Pascal-Part-116上h-IoU达49.29%，mOSI降至23.46%，较PartCATSeg显著提升。然而，HOPS整体框架需微调CLIP/DINO，AFM虽免训练但AEM迭代传播增加计算开销，微调是否削弱免训练范式的部署优势，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_e8fc9974eed6)
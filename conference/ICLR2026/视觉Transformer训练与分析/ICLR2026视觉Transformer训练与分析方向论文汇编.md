# ICLR2026 · 视觉Transformer训练与分析方向论文汇编

> 本方向共 4 篇（ICLR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Block-Recurrent Dynamics in Vision Transformers ｜块递归动力学

研究机构：美国哈佛大学

作者：Mozes Jacobs、Thomas Fel、Richard Hakim 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.19941)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.19941)

> 视觉Transformer（ViT）内部决策的黑盒特性阻碍了安全关键应用的可信度验证，而现有解释方法多依赖静态注意力图，缺乏对深度计算过程的动态因果刻画。本文提出块递归假设（Block-Recurrent Hypothesis, BRH），主张训练后的ViT深度可被少量重复块等价重写，并通过构造性代理模型Raptor验证该假设的功能等价性。Raptor在保持同等运行时下，以2个递归块恢复了DINOv2 96%的ImageNet-1k线性探针精度。该工作为ViT提供了低算法复杂度的动力学解释框架，但其递归压缩在密集预测任务上的泛化边界尚未充分验证。

】

---

【BLOCK-RECURRENT DYNAMICS IN VITS ｜视觉Transformer块递归动力学

研究机构：美国哈佛大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_40235613)

> 视觉Transformer（ViT）在安全关键应用中面临内部计算不可检视与验证的困境，现有解释方法多依赖静态归因，无法揭示深度方向上的功能复用规律。本文提出块递归假设（Block-Recurrent Hypothesis, BRH），主张训练后的ViT深度可被少量连续相位块重写，并通过递归代理模型Raptor进行构造性验证。Raptor以权重共享块逼近预训练ViT的逐层激活轨迹，将深度视为离散时间动力学系统。该框架在机制解释维度提供了新视角，但其递归压缩在密集预测任务上的精度保持能力仍存疑。

】

---

【Locality-Attending Vision Transformer ｜局部注意力视觉Transformer

作者：Sina Hajimiri、Farzad Beizaee、Fereshteh Shakeri 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.04892)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.04892)

> 视觉Transformer在图像分类中凭借全局自注意力取得优势，但该机制导致特征图缺乏局部空间细节，使其在语义分割等密集预测任务中表现受限。现有方案多通过修改骨干结构或引入卷积混合模块来解决，但往往牺牲了架构的简洁性与即插即用性。本文提出LocAtViT，通过在高斯核增强的注意力机制与无参数补丁表征精炼模块，在不改变标准分类训练流程的前提下增强局部感知。该方法在多个基准上显著提升了分割性能且未损害分类精度，但其增益幅度在已具备局部偏置的架构上大幅衰减，且未验证其在大规模基础模型中的泛化边界。

】

---

【Revisiting [CLS] and Patch Token Interaction in Vision Transformers ｜解耦类Token与补丁Token的Transformer层特异性处理

研究机构：法国国家科学研究中心

作者：Alexis Marouani、Oriane Siméoni、Hervé Jégou 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.08626)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.08626)

> 视觉Transformer在密集预测任务中常因全局类Token与局部补丁Token共享计算管线而产生特征冲突，导致局部细节丢失。现有方案如引入寄存器或修改注意力机制仅缓解了高范数异常，未解决Token间功能摩擦的根本问题。本文通过分离归一化层与早期投影层的权重，显式解耦两类Token的计算路径，在不增加推理计算量的前提下提升了分割精度。该架构改进在密集预测上表现优异，但其对分类任务的轻微负面影响及在监督框架下的失效边界仍需进一步厘清。

】

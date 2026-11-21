# CVPR2026最新论文 ｜Black-Box Domain Adaptation for Object Detection with Retention-Driven Knowledge Compression ｜黑盒域适应目标检测中的记忆驱动知识压缩

作者：Yuwu Lu、Chunzhi Liu

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_affd0dd2d5af)

> 黑盒域适应（BBDA）要求模型在无法访问源数据及源模型参数的极端隐私约束下，仅利用云端API返回的静态噪声预测完成目标域适应。现有BBDA方法多针对分类任务设计，缺乏对检测任务中边界框定位与局部分类联合优化的机制，导致在静态预测约束下性能严重退化。本文提出RDKC框架，通过模拟生物记忆机制，将全局平滑策略细化为区域级的对比学习与权重压缩，以解决噪声标签对定位精度的干扰。该框架在多个基准上刷新了BBDA设定的性能上限，但其依赖静态预测的假设限制了其在动态API场景下的适用性。

## 研究背景

当目标检测器部署于新域时，若源数据因隐私法规不可共享，且源模型参数因逆向生成攻击风险不可暴露，模型仅能获取云端API返回的无标签目标域预测结果。这种仅依赖外部静态预测、无内部特征访问的设定称为黑盒域适应（BBDA）。BBDA的核心困境在于，API返回的预测在整个适应过程中保持静态，无法像源自由域适应（SFDA）那样通过迭代更新模型来动态修正伪标签，导致噪声累积效应被放大。

传统无监督域适应（UDA）依赖源数据对齐，源自由域适应（SFDA）依赖源模型参数进行特征重构，二者均无法在BBDA的严格隐私边界下运行。现有BBDA方法如DINE和BiMem主要聚焦于图像分类的全局特征蒸馏，采用自适应标签平滑来抑制噪声，但忽略了检测任务中边界框回归与局部分类的耦合关系。在检测任务中，全局平滑会模糊局部区域的特征差异，导致模型难以区分高置信度的近景目标与低置信度的远景背景，进而引发定位漂移。

本文的切入点在于识别BBDA检测任务中“静态预测”与“局部定位”之间的结构性矛盾。通过引入终身学习中的主动遗忘与选择性稳定机制，RDKC将适应过程从全局特征匹配转化为区域级的知识筛选与压缩，旨在静态预测约束下重建局部特征的判别力。

## 核心方法

### 黑盒检测适应参照系

BBDA检测适应的标准流程通常包含知识蒸馏与自训练两个阶段。教师模型通过API预测进行初步对齐，学生模型在教师指导下更新参数。本文的关键差异在于，传统方法将API预测视为静态监督信号直接用于损失计算，而RDKC将其视为含噪记忆库，通过动态分区机制对预测信号进行二次加工，以适配检测头的局部优化需求。

### 记忆保留机制（MR）

MR模块针对BBDA中静态噪声预测导致的确认偏置问题，通过区分高可靠性（HRP）与低可靠性（LRP）提案框，实施差异化的分数优化。对于HRP框，MR保留最高预测分数并抑制其他类别分数，以强化可靠知识；对于LRP框，保留原始分数以防止灾难性遗忘。该机制通过以下公式实现分数重分配：

$$
\text{Score}_{i,j}^{\text{tea}} = \begin{cases} \alpha \cdot g(\text{Score}_{i,j}^{\text{tea}}) + (1-\alpha)\text{Score}_{i,j}^{\text{tea}*}, & \text{Type}_{i,j} = \text{HRP} \\ \alpha \cdot \text{Score}_{i,j}^{\text{tea}} + (1-\alpha)\text{Score}_{i,j}^{\text{tea}*}, & \text{Type}_{i,j} = \text{LRP} \end{cases}
$$

其中 $\text{Score}^{\text{tea}*}$ 为上一轮迭代的分数，$\alpha=0.6$ 为稳定系数。这一设计解决了全局标签平滑在检测任务中模糊局部边界的问题，通过局部抑制噪声分数，使模型在静态预测约束下仍能聚焦于高置信度区域。

### 场景压缩机制（SC）

SC模块承接MR输出的优化分数，通过近景与远景区域的对比学习生成压缩权重，以增强边界框的细粒度感知。SC利用学生与教师模型预测的余弦相似度计算权重，对高可靠性区域施加更强的对齐约束，对低可靠性区域抑制学习。压缩权重公式为：

$$
W_{i,j} = \begin{cases} \exp(-\log[\cos(\text{Score}_{i,j}^{\text{stu}}, g(\text{Score}_{i,j}^{\text{tea}}))]), & \text{Type}_{i,j} = \text{HRP} \\ \exp(-\log[1-\cos(\text{Score}_{i,j}^{\text{stu}}, \text{Score}_{i,j}^{\text{tea}})]), & \text{Type}_{i,j} = \text{LRP} \end{cases}
$$

该机制通过近景线索引导远景表示学习，解决了静态预测中远景目标因特征模糊而难以定位的问题。SC与MR联合优化，使得学生模型在抑制背景噪声的同时，能够利用近景的高置信度特征修正远景的定位偏差。

## 实验评估

实验在Cityscapes→Foggy-Cityscapes、Sim10K→Cityscapes、KITTI→Cityscapes及Pascal-VOC→Watercolor四个基准上进行，对比了UDA、SFDA及BBDA三类方法。基线覆盖DA-Faster、LPLD、DINE等代表性工作，但缺乏最新VLM引导方法的对比，可能低估了外部语义先验在BBDA中的潜在增益。

| 方法 | 设定 | Cityscapes→Foggy mAP | Sim10K→Cityscapes AP(Car) | KITTI→Cityscapes AP(Car) |
| :--- | :--- | :--- | :--- | :--- |
| DINE | BB | 36.5 | 37.9 | 39.8 |
| LPLD† | BB | 32.6 | 38.9 | 41.3 |
| RDKC | BB | 40.7 | 49.1 | 50.4 |

RDKC在Cityscapes→Foggy-Cityscapes上较DINE提升4.2个点，在Sim10K→Cityscapes上较LPLD†提升10.2个点，表明区域级优化在静态预测约束下显著优于全局蒸馏。消融实验显示，移除SC模块后，mAP从40.7降至37.6，AP(Car)从49.1降至43.9，证实了近景引导远景策略对定位精度的关键作用。参数敏感性分析表明，分区阈值$\lambda$在0.4-0.6区间性能最优，$\lambda=0$或1时性能骤降，验证了HRP/LRP分区机制的必要性。

评估协议采用Faster R-CNN骨干，未报告计算开销与隐私泄露量化指标。代码未公开，超参数如$\alpha=0.6$、EMA率0.8固定，缺乏跨骨干网络的泛化性验证。BBDA设定下性能仍低于UDA上限（如PT在Sim10K上达55.1），凸显了静态预测对性能的根本性限制。

## 关联研究分析

从问题动机看，RDKC与SFDA方法如LPLD的核心差异在于信息访问边界。LPLD依赖源模型参数进行特征对齐，而RDKC仅利用API静态预测。这一差异导致LPLD在BBDA设定下性能从40.9降至32.6，而RDKC通过MR/SC机制在相同约束下达到40.7。根源在于检测任务的局部性：SFDA可通过迭代更新模型动态修正伪标签，而BBDA的静态预测迫使模型必须在单次前向传播中完成噪声抑制，RDKC的区域级对比学习正是针对这一静态约束的适配。

从方法设计看，RDKC与分类任务BBDA方法DINE的差异在于优化粒度。DINE采用全局标签平滑，而RDKC采用区域级分数重分配。这一差异源于检测任务中边界框回归与分类的耦合：全局平滑会模糊局部特征，导致定位漂移，而区域级优化保留了局部判别力。RDKC未引入VLM等外部语义先验，依赖纯视觉对比，这在语义歧义较大的场景（如Pascal-VOC→Watercolor）中可能成为瓶颈，论文未探讨引入外部知识是否能进一步缓解静态预测的局限。

## 总结

RDKC旨在解决BBDA检测任务中静态噪声预测与局部定位优化之间的结构性矛盾。现有BBDA方法因缺乏局部优化机制，在静态预测约束下性能严重退化，而RDKC通过记忆保留与场景压缩机制，将全局平滑转化为区域级对比学习，重建了局部特征的判别力。实验表明，RDKC在Cityscapes→Foggy-Cityscapes上达到40.7% mAP，较DINE提升4.2个点，在Sim10K→Cityscapes上AP(Car)达49.1，较LPLD†提升10.2个点。其边界在于依赖静态预测假设，未验证动态API场景下的适应性，且缺乏VLM等外部语义先验的对比。当API预测从静态转为动态更新时，MR/SC机制中的分数重分配策略是否仍能保持优势，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_affd0dd2d5af)
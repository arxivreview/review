# CVPR2026 · 高效视觉Transformer压缩与加速方向论文汇编

> 本方向共 4 篇（CVPR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Co-Me: Confidence Guided Token Merging for Visual Geometric Transformers ｜置信度引导的Token合并

研究机构：美国卡内基梅隆大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d46a10937cea)

> 视觉几何Transformer（VGT）在3D重建中面临二次方计算复杂度与实时部署需求的矛盾，现有Token剪枝方法在密集几何任务中因丢失空间上下文而失效，启发式Token合并则缺乏对几何关键区域的保护机制。本文提出Co-Me，通过自监督蒸馏轻量级置信度预测模块，基于置信度排名选择性合并低置信度Token，在无需重训练基础模型的前提下实现加速。该方法在VGGT上取得最高21.5倍加速，但其在单帧输入下的加速收益有限，且精度损失在长序列场景下是否可接受于下游SLAM任务，论文未给出明确回答。

】

---

【Edge-RecViT: Efficient Vision Transformer via Semantic-Refined Dynamic Recursion ｜边缘感知动态递归视觉Transformer

作者：YiZhou Li、Jinyi Xu、Mingyu Yin 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_21471707f34e)

> 视觉Transformer（ViT）在边缘部署中面临计算冗余与参数膨胀的双重瓶颈，现有Token自适应方法虽能降低浮点运算量（FLOPs），却因全局注意力机制导致语义贫乏的前景中心Token被过度计算，且深层参数因早退机制而闲置。本文切入点在于利用边缘Token的结构丰富性替代前景重要性作为计算分配依据，并引入递归参数共享以消除层级冗余。通过边缘感知排名器与共享隐藏层结合，Edge-RecViT在ImageNet-1K上以23.2M参数和24.39 GFLOPs达到82.0% Top-1准确率，较DeiT-Base减少73%参数，但其递归结构在密集预测任务中的泛化能力尚未验证。

】

---

【Revisiting Token Compression for Accelerating ViT-based Sparse Multi-View 3D Object Detectors ｜动态Patch粒度选择与跨粒度特征增强

研究机构：南京大学

作者：Mingqian Ji、Shanshan Zhang、Jian Yang

论文原文见 [arXiv](https://arxiv.org/abs/2604.14563)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.14563)

> 稀疏多视角3D目标检测器依赖Vision Transformer（ViT）提取高质量图像特征，但密集Token处理导致推理延迟高企，阻碍了实时部署。现有Token压缩策略如剪枝、合并或简单扩大Patch Size，在3D检测任务中会丢失背景负样本线索或破坏细粒度语义，导致精度显著下降。SEPatch3D通过基于时空Query分布动态调整Patch粒度，并利用熵值筛选信息丰富区域进行跨粒度特征融合，在保持检测精度的同时大幅降低计算开销。该方法在nuScenes上实现了57%的推理加速，但其在不同分辨率下的泛化能力及对非ViT骨干的适用性仍存疑。

】

---

【Scaling Parallel Sequence Models to Vision Foundation Models ｜紧凑广义空间传播网络

研究机构：香港中文大学

作者：Yitong Jiang、Collin McCarthy、Hongjun Wang 等 11 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_13eaf7ebce33)

> 视觉基础模型受限于自注意力的二次方复杂度，导致高分辨率输入下内存与延迟激增。现有子二次方替代方案如线性注意力或状态空间模型多将图像序列化为1D，丢失2D空间连贯性，且原始GSPN在GPU上因通道或批大小增长导致并发饱和，延迟急剧上升。本文提出C-GSPN，通过潜空间压缩传播与两阶段跨算子蒸馏，在保持零样本迁移能力的前提下实现基础模型规模预训练。该方法在1K分辨率下较FlashAttention快2倍，但分类精度略低于ViT基线，其泛化边界尚需验证。

】

# ACL-Findings2026 · 高效长上下文Transformer架构方向论文汇编

> 本方向共 2 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【A Survey of Retentive Network ｜RetNet：固定衰减递归状态下的长序列建模综述

作者：Haiqi Yang、Zhiyuan Li、Yi Chang 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e55fe080e44e)

> 长上下文Transformer面临二次方计算复杂度与线性内存膨胀的双重瓶颈，现有线性注意力或状态空间模型（SSM）虽降低复杂度，但在精确检索任务上因固定状态导致信息过度压缩而失效。本文切入点在于系统化梳理RetNet这一特定递归架构，揭示其通过固定标量衰减实现并行训练与递归推理统一机制的内在逻辑，并指出其“联想回忆瓶颈”这一被忽视的精度缺陷。RetNet通过多尺度保留机制将注意力转化为线性复杂度递归过程，但在高熵检索任务上保真度受限。其价值在于提供了递归架构的完整技术图谱，但固定衰减是否必然导致检索能力上限，仍需更严格的基准验证。

】

---

【Optimizing Native Sparse Attention with Latent Attention and Local Global Alternating Strategies ｜交替稀疏注意力

研究机构：中国人民大学、美团

作者：Yuxuan Hu、Jianchao Tan、Jiaqi Zhang 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_cd0eec310990)

> 长上下文处理中，标准Transformer的二次方计算复杂度与键值缓存（KV Cache）线性内存膨胀构成双重瓶颈，而现有稀疏注意力方案在层内并行计算时，局部窗口分支常因“捷径学习”干扰全局检索分支的有效性。本文切入点在于揭示滑动窗口注意力（SWA）与选择性注意力（SA）共存时的功能冲突，并提出层间交替策略。ASA将SWA与压缩/选择性注意力（CA/SA）在Transformer层间以1:1比例交替排列，并引入多头潜在注意力（MLA）及其变体分组头潜在注意力（GLA）替代分组查询注意力（GQA），在保持检索精度的同时降低50%的KV缓存开销。该架构在340M至1.3B参数规模上验证了有效性，但缺乏大规模模型及标准长上下文基准的横向对比，其层间静态交替策略在复杂动态任务上的泛化能力存疑。

】

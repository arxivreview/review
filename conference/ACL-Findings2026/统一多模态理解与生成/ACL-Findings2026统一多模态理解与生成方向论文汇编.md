# ACL-Findings2026 · 统一多模态理解与生成方向论文汇编

> 本方向共 2 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Towards Unified Multimodal Large Language Models: A survey ｜统一多模态大语言模型架构分类与协同机制审视

研究机构：美国东北大学

作者：Xu Ma、Yitian Zhang、Yun Fu

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9fa04eb6f3bd)

> 统一多模态大语言模型旨在单一架构内融合视觉理解与图像生成，以打破模态壁垒实现深层知识交互。早期级联架构缺乏双向交互，原生自回归模型虽确立 Any-to-Any 范式却暴露出理解与生成在表征空间中的根本冲突。本文通过构建涵盖架构选择、训练策略与模态集成的三维分类体系，系统梳理了从离散 Token 化到混合扩散目标的演进路径，并指出当前领域缺乏量化协同效应的闭环评估标准。该综述提供了清晰的领域认知地图，但其对“伪统一”现象的归因仍停留在架构层面，未深入表征解耦的理论边界。

】

---

【UniCM: A Unified Consistency Model For Efficient Multimodal Generation and Understanding ｜统一一致性模型

研究机构：上海交通大学、同济大学

作者：Chenkai Xu、Xu Wang、Zhenyi Liao 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_aeae2be8eca5)

> 统一多模态模型旨在单一架构内同时处理图像生成与文本理解，但现有方案依赖迭代去噪或自回归解码，导致推理延迟高企。本文切入点在于建立跨模态的统一去噪轨迹，使一致性模型能直接映射任意中间状态至终点，从而跳过中间步骤。通过定义基于自回归并行解码的文本去噪路径与基于掩码扩散的图像去噪路径，并施加统一的一致性蒸馏目标，实现了少步高效推理。该方案在保持接近基线性能的同时大幅降低延迟，但其生成质量在部分指标上未超越专用扩散模型，且缺乏对内部表征协同效应的验证。

】

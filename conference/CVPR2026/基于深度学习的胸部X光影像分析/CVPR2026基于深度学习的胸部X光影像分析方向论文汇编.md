# CVPR2026 · 基于深度学习的胸部X光影像分析方向论文汇编

> 本方向共 2 篇（CVPR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【DARC: Dual Adjustment Reasoning with Counterfactuals for Trustworthy Chest X-ray Classification ｜双调整反事实推理框架

研究机构：中南大学

作者：Zhifang Liao、Junhao Li、HaoKang Ding 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_52185804dc90)

> 胸部X光（CXR）多标签分类模型常因病理共现与非病理视觉混杂产生捷径学习，导致临床部署中的鲁棒性失效。现有因果去偏方法仅能处理单一混淆源，且缺乏像素级混杂标注支撑精确干预。DARC通过构建首个像素级非病理混杂数据集CheXconf，并设计双流因果架构，同时执行后门调整与反事实推理以解耦两类混淆。该框架在因果纯度上优于单一去偏基线，但分类精度低于纯统计依赖建模的SOTA，其临床价值取决于对因果解释与预测精度的权衡。

】

---

【X-WIN: Building Chest Radiograph World Model via Predictive Sensing ｜胸部X光世界模型：基于预测性感知的3D知识蒸馏

研究机构：美国伦斯勒理工学院

作者：Zefan Yang、Ge Wang、James Hendler 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.14918)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.14918)

> 胸部X光（CXR）作为二维投影图像，因结构重叠无法捕捉三维解剖细节，限制了疾病诊断的准确性。现有CXR基础模型仅学习二维局部特征，缺乏对三维空间结构的内化，导致在复杂病理场景下表示能力不足。X-WIN通过构建动作条件世界模型，从CT体积中蒸馏三维空间知识至CXR表示空间，实现了跨模态的空间认知迁移。该方法在标准基准上以线性探测协议超越了现有基础模型，但其模拟域与真实域的分布差异仍制约着临床泛化能力。

】

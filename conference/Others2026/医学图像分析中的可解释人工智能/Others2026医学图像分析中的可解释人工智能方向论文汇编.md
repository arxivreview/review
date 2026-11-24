# Others2026 · 医学图像分析中的可解释人工智能方向论文汇编

> 本方向共 2 篇（Others2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【DCG-Net: Dual Cross-Attention with Concept-Value Graph Reasoning for Interpretable Medical Diagnosis ｜概念-值依赖建模的医学影像诊断框架

研究机构：澳大利亚格里菲斯大学

作者：Getamesay Dagnaw、Xuefei Yin、Muhammad Hassan Maqsood 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.20325)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.20325)

> 医学影像诊断中，概念瓶颈模型（Concept Bottleneck Model, CBM）因忽略临床概念间复杂的上下文依赖，常产生逻辑不一致的解释。现有方法多停留在概念存在性层面，未能捕捉特定概念值组合（如“细胞大”且“核质比低”）所隐含的诊断逻辑。DCG-Net 通过双交叉注意力与参数化概念图，在概念-值对粒度上建立依赖关系，实现了更细粒度的临床推理。该架构在皮肤与血液学数据集上提升了诊断精度与解释一致性，但其对图结构先验的依赖及跨域泛化能力仍存疑。

】

---

【利兹团队新研究：基于固定聚合的自解释胸部X光分类架构

研究机构：英国利兹大学

作者：Patrick Wienholt、Christiane Kuhl、Jakob Nikolas Kather 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.07477)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.07477)

> 临床部署中的深度学习模型常因“黑盒”特性导致医生无法审计其决策逻辑，而事后解释方法（如Grad-CAM）生成的热力图往往与真实决策依据脱节，甚至掩盖捷径学习风险。MedicalPatchNet 通过架构内解释策略，将图像分割为独立处理的Patch，利用固定算术平均聚合局部Logits，使每个Patch的贡献直接可视化为归因信号。该设计在保持与标准EfficientNetV2-S相当分类性能的前提下，显著提升了空间定位的忠实度，但其解释粒度停留在像素区域层面，缺乏临床语义深度，能否满足医生对病理机制的深层理解需求仍存疑。

】

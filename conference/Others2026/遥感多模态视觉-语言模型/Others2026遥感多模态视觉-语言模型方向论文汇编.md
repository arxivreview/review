# Others2026 · 遥感多模态视觉-语言模型方向论文汇编

> 本方向共 1 篇（Others2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【慕尼黑工业团队新研究：自适应梯度校准的单正例多标签遥感图像分类

研究机构：德国慕尼黑工业大学

作者：Chenying Liu、Gianmarco Perantoni、Lorenzo Bruzzone 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.08269)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.08269)

> 遥感多标签分类（Multi-Label Classification, MLC）旨在从单幅图像中恢复完整的语义标签集合，但完整标注成本高昂且易产生缺失。现有弱监督方法在处理遥感数据特有的类间低可分性与类内高变异性时，常因伪标签噪声或固定预热策略导致模型过拟合假阴性。本文提出自适应梯度校准（Adaptive Gradient Calibration, AdaGC）框架，通过双指数移动平均（Dual-EMA）生成鲁棒伪标签，并基于早期学习检测动态触发梯度校准以抑制噪声过拟合。该框架在两个基准数据集上取得了优于现有单正例多标签学习（Single-Positive Multi-Label Learning, SPML）方法的性能，但其依赖CNN骨干且未验证零样本泛化能力，限制了其在视觉语言模型（Vision-Language Models, VLMs）时代的适用性。

】

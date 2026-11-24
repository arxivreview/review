# Others2026 · 脑肿瘤检测与分类方向论文汇编

> 本方向共 2 篇（Others2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【基于EfficientNetV2与MLP-Mixer注意力的可解释脑肿瘤MRI分类

作者：Mustafa Yurdakul、Şakir Taşdemir

论文原文见 [arXiv](https://arxiv.org/abs/2509.06713)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.06713)

> 脑肿瘤MRI分类旨在通过自动化模型替代人工阅片，以解决放射科医生工作负荷高且诊断一致性差的临床痛点。现有CNN架构虽能提取局部纹理，但受限于感受野，难以捕捉肿瘤与周围脑组织的长程空间依赖，且缺乏临床可解释性。本文切入点在于将线性注意力机制嵌入MLP-Mixer结构，并嫁接于EfficientNetV2骨干，以在保持计算效率的同时增强全局特征混合能力。该方法在Figshare三分类任务上取得了99.50%的准确率，但缺乏四分类及跨域泛化验证，其临床部署的鲁棒性存疑。

】

---

【基于非负矩阵分解与扩散去噪的脑肿瘤对抗鲁棒分类

作者：Hiba Adil Al-kharsan、Róbert Rajkó

论文原文见 [arXiv](https://arxiv.org/abs/2603.13182)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.13182)

> 脑肿瘤辅助诊断系统面临的核心矛盾是高精度模型在对抗扰动下的脆弱性，微小输入修改即可导致误诊。现有主流深度学习方法虽在干净数据上表现优异，但普遍缺乏对对抗攻击的防御机制，且特征表示往往不可解释。本文切入点在于将非负矩阵分解（Non-Negative Matrix Factorization, NNMF）的可解释特征提取与扩散模型的特征空间去噪相结合，构建轻量级分类框架。该方法在AutoAttack下将鲁棒准确率从0.0047提升至0.5953，但干净数据准确率仅约83%，远低于领域SOTA，其临床实用性与泛化能力存疑。

】

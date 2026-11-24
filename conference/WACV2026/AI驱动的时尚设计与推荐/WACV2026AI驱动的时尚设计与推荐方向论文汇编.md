# WACV2026 · AI驱动的时尚设计与推荐方向论文汇编

> 本方向共 3 篇（WACV2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【BrandFusion: Aligning Image Generation with Brand Styles ｜品牌视觉身份对齐生成

研究机构：澳大利亚莫纳什大学

作者：Parul Gupta、Varun Khurana、Yaman Kumar Singla 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8bc459b5d925)

> 现有文本到图像模型无法通过纯文本提示捕捉品牌特有的光照、构图与人物表现等细微视觉特征，导致生成的营销内容缺乏品牌辨识度。BrandFusion 提出解耦品牌风格学习与图像生成的双组件架构，利用视觉语言模型从营销上下文预测风格特征与嵌入，再条件化扩散模型生成图像。该方法实现了无需逐品牌微调的跨品牌泛化，但在无图像输入条件下对细微视觉细节的捕捉能力仍存疑。

】

---

【MEDAL: multi-modal MEta-space Distillation and ALignment for Visual Compatibility Learning ｜多模态元空间蒸馏与对齐

作者：Dween Rabius Sanny、Vinay Kumar Verma、Prateek Sircar 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_82edcee1d534)

> 时尚推荐系统需解决视觉兼容性预测（CP）与互补项检索（CIR）两大核心任务，但现有方法依赖全局CNN特征而忽略纹理等局部线索，且将不同品类对强制映射至单一嵌入空间，导致泛化能力受限。MEDAL通过教师-学生ViT架构结合局部-全局增强，将联合特征流形解耦为品类对特异性元空间，并引入远程监督知识蒸馏以消除人工标注依赖。该方法在Polyvore基准上实现了FITB与R@10指标的SOTA提升，但其判别式框架缺乏解释性，且远程监督数据的噪声对长尾品类的鲁棒性影响尚存疑。

】

---

【Sketch2Stitch: GANs for Abstract Sketch-Based Dress Synthesis ｜抽象草图驱动的高保真服装合成

研究机构：沙特阿拉伯阿卜杜拉国王科技大学

作者：Faizan Farooq Khan、Eslam Abdelrahman Bakr、Davide Morelli 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_08caa1cc2f80)

> 时尚设计领域长期存在从非专业抽象草图到目录级写实图像的转化断层，传统基于边缘图或精确线稿的方法无法捕捉业余创作者的变形与抽象特征。现有生成模型在处理自由形态草图时，常因缺乏颜色先验和结构约束导致细节丢失或几何失真。本文通过构建大规模抽象草图数据集并改造StyleGAN编码器，实现了草图与颜色提示到写实服装图像的端到端映射。该方法在视觉保真度上优于主流扩散模型基线，但其依赖GAN架构的选择与当前领域向扩散模型演进的主流趋势存在显著背离。

】

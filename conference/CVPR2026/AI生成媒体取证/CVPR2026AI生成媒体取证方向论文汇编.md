# CVPR2026 · AI生成媒体取证方向论文汇编

> 本方向共 2 篇（CVPR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Attribution as Retrieval: Model-Agnostic AI-Generated Image Attribution ｜基于低比特指纹的实例检索式AI生成图像归因

研究机构：东南大学

作者：Hongsong Wang、Renxi Cheng、Chaolei Han 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.10583)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.10583)

> AI生成图像归因旨在识别特定合成内容的来源模型，但现有分类范式依赖大量标注数据且难以适应快速迭代的新生成器。LIDA将归因重构为实例检索问题，利用RGB通道低比特平面提取生成器特有的噪声指纹，通过无监督预训练与少样本适应实现模型无关的溯源。该方法在GenImage和WildFake数据集上显著优于传统特征提取基线，但其性能高度依赖注册数据库的覆盖度，且未验证在强压缩环境下的鲁棒性。

】

---

【SAGA: Source Attribution of Generative AI Videos ｜生成式AI视频来源归因

研究机构：美国加州大学河滨分校、谷歌DeepMind

作者：Rohit Kundu、Vishal Mohanty、Hao Xiong 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.12834)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.12834)

> 现有AI视频检测多止步于“真/假”二分类，无法应对生成模型快速迭代带来的溯源需求。SAGA通过五级粒度归因框架，将任务从二元检测扩展至具体模型识别，并引入时间注意力签名（T-Sig）提供可解释性。其核心在于利用预训练视觉编码器初始化视频Transformer，结合硬负样本挖掘（HNM）对比损失，在仅0.5%标注数据下实现接近全量监督的归因性能。该框架在数据效率与细粒度区分上具有显著优势，但其对视频压缩鲁棒性及跨域泛化的实际部署能力仍存疑。

】

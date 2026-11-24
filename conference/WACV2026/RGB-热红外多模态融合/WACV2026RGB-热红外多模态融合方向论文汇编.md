# WACV2026 · RGB-热红外多模态融合方向论文汇编

> 本方向共 2 篇（WACV2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【F-ViTA: Foundation Model Guided Visible to Infrared Translation ｜基础模型引导的可见光-热红外翻译

研究机构：美国约翰斯·霍普金斯大学

作者：Jay Nitin Paranjape、Celso M De Melo、Vishal M. Patel

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_2ef6107178af)

> 可见光到热红外翻译旨在解决热红外数据标注成本高、规模小的瓶颈，为下游融合任务提供合成数据。现有基于生成对抗网络或扩散模型的方法在低数据量下易过拟合，且缺乏对场景物体物理特性的细粒度建模。F-ViTA 利用预训练基础模型提取零样本掩码与标签，作为扩散模型的条件嵌入，引导生成过程学习物体级热辐射关联。该方法在多波段数据集上提升了结构保真度，但分布距离指标略逊于物理约束基线，其生成数据的物理一致性边界尚待明确。

】

---

【F-ViTA: Foundation Model Guided Visible-to-Infrared Translation ｜基础模型引导的可见光-红外翻译

研究机构：美国约翰斯·霍普金斯大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_WACV_2026_4542763)

> 可见光到红外图像翻译旨在解决热红外数据标注成本高、规模小导致的模型泛化瓶颈。现有生成方法将翻译视为风格迁移，在低数据场景下易过拟合且难以捕捉对象级物理关联。F-ViTA 利用基础模型零样本提取的掩码与标签作为扩散模型条件，隐式学习对象热签名与像素强度的关联。该方法在结构保真度上显著优于基线，但物理一致性指标仍落后于显式物理约束方法，其多波段生成能力尚缺乏统一评估标准。

】

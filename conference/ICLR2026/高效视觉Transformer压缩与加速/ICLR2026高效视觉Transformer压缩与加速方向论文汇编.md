# ICLR2026 · 高效视觉Transformer压缩与加速方向论文汇编

> 本方向共 3 篇（ICLR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【THICKER AND QUICKER: A JUMBO TOKEN FOR FAST PLAIN VISION TRANSFORMERS ｜宽全局Token加速纯视觉Transformer

研究机构：加拿大不列颠哥伦比亚大学、加拿大向量研究所

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_2986316)

> 视觉Transformer（ViT）在保持通用性的同时面临推理速度瓶颈，现有高效架构多通过引入卷积或层级结构牺牲了纯ViT的生态兼容性。本文切入点在于识别出全局信息容量不足是纯ViT低速场景下的精度短板，而非计算量本身。通过引入一个宽度为Patch Token $J$ 倍的Jumbo Token并共享其FFN参数，在不改变纯ViT接口的前提下实现了速度-精度的帕累托前沿。该设计在保持自监督学习、多模态兼容性的同时提升了效率，但其对极端小模型（Nano级）的增益依赖特定训练协议，且未验证在动态Token剪枝场景下的稳定性。

】

---

【Tianyi Zhang ｜选择与打包注意力

研究机构：美国明尼苏达大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_32397417)

> 视觉Transformer在密集预测任务中因处理大量背景Token导致计算冗余与信息干扰，现有稀疏注意力方法在训练阶段难以实现高效并行或依赖固定比例剪枝导致小目标信息丢失。本文切入点在于利用目标检测标签构建多尺度监督信号，指导门控层动态选择信息Token，并通过打包机制恢复GPU批量训练的并行性。具体做法是设计Select and Pack Attention（SPA）模块，将变长Token序列装入固定长度容器以优化计算图。该方法在COCO2017目标检测任务上以更低计算量实现了精度提升，但其对密集标注标签的强依赖限制了在无标注场景下的泛化能力。

】

---

【卡内基梅隆团队新研究：ACCELERATING VISION TRANSFORMERS WITH ADAPTIVE PATCH SIZES

研究机构：美国卡内基梅隆大学、韩国科学技术院

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_21396229)

> 视觉Transformer在处理高分辨率图像时，固定大小的Patch化导致序列长度激增，而自注意力机制的二次方复杂度使计算成本难以承受。现有Token压缩方法多采用固定比例合并或层内剪枝，无法根据图像局部复杂度动态调整计算量，且常引入不规则形状导致实际加速失效。APT通过计算多尺度熵，在输入端为不同区域分配不同大小的Patch，以零初始化MLP融合多尺度嵌入，实现了训练与推理的双重加速。该方法在ViT-L上实现40%加速且精度无损，但依赖熵阈值调参，且对密集预测任务的适配仍显粗糙。

】

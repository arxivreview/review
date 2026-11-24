# CVPR2026 · KV缓存压缩与管理方向论文汇编

> 本方向共 1 篇（CVPR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Revisiting Multimodal KV Cache Compression: A Frequency-Domain-Guided Outlier-KV-Aware Approach ｜频域引导的离群KV感知压缩

研究机构：复旦大学、香港中文大学

作者：Yaoxin Yang、Peng Ye、Xudong Tan 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.16786)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.16786)

> 多模态大语言模型（MLLM）在长上下文推理中面临视觉Token引发的键值缓存（KV Cache）显存爆炸与解码延迟瓶颈。现有基于注意力分数的驱逐方法因依赖显式注意力矩阵而难以兼容FlashAttention等高效内核，且忽略了Value向量对输出的直接贡献。本文提出FlashCache，通过离散余弦变换（DCT）提取KV矩阵的低频基线，识别偏离基线显著的离群KV（Outlier KVs）并保留，同时依据各层离群能量占比动态分配缓存预算。该方法在保持任务精度的同时实现了最高1.69倍的解码加速，但其频域假设在极端压缩率下的鲁棒性仍存疑。

】

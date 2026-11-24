# Others2026 · 二值化与低位宽神经网络量化方向论文汇编

> 本方向共 1 篇（Others2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Once-for-All Channel Mixers (HYPERTINYPW): Generative Compression for TinyML ｜生成式权重合成压缩微控制器点卷积层

研究机构：美国麻省理工学院

作者：Yassien Shaalan

论文原文见 [arXiv](https://arxiv.org/abs/2603.24916)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.24916)

> 微控制器（MCU）部署中，1×1 点卷积（PW）层在 INT8 量化后仍占据 Flash 存储的主导地位，传统压缩方法仅减少参数量却未消除逐层存储开销。现有动态权重生成方案因逐输入分支导致实时性失效，本文提出“压缩即生成”范式，通过共享微 MLP 在加载时一次性合成 PW 权重，实现无运行时分支的整数推理。该方法在 225 kB 预算下将 1.4 MB 基线压缩 6.31 倍，保留 95% 的 Macro-F1，但其有效性严格依赖于跨层冗余假设，在极端类不平衡下的阈值稳定性仍存疑。

】

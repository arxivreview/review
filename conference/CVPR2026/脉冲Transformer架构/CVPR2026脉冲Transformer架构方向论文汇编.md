# CVPR2026 · 脉冲Transformer架构方向论文汇编

> 本方向共 1 篇（CVPR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Temporal Interaction in Spiking Transformers with Multi-Delay Mixer ｜多延迟混合器（MD-Mixer）：脉冲Transformer中的显式时间动态建模

研究机构：电子科技大学、新加坡国立大学

作者：Kexin Shi、Hanwen Liu、Zeyang Song 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_5c6c8e6dc6c4)

> 脉冲Transformer旨在利用事件驱动特性降低边缘设备能耗，但现有自注意力机制仅捕捉单时间步内的空间关系，缺乏对历史脉冲的显式交互，导致动态视觉任务性能受限。本文通过引入多分支可学习延迟机制，在Key和Value路径中聚合多尺度历史信息，实现了时空混合。该方法作为即插即用模块，在动态基准上刷新了SOTA，但在静态大规模分类中未超越最新架构，其能效收益在真实硬件上的表现仍存疑。

】

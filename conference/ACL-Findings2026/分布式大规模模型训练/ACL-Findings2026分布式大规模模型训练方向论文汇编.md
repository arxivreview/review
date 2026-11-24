# ACL-Findings2026 · 分布式大规模模型训练方向论文汇编

> 本方向共 1 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【High-Throughput and Memory-Efficient Zeroth-Order Fine-tuning LLMs with Distributed Parallel Computing ｜分布式零阶微调的并行化与通信优化

研究机构：沙特阿拉伯阿卜杜拉国王科技大学

作者：Liangyu Wang、Huanyi Xie、Di Wang

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4c512f111535)

> 大语言模型全参数微调受限于显存与算力，零阶优化（ZO）虽通过消除反向传播降低显存占用，但单卡执行导致吞吐量瓶颈，且现有分布式框架无法利用其双前向结构。DistZO2 提出扰动并行（PertP）与适配标量梯度的数据并行，结合硬件感知通信切片，将 ZO 微调扩展至 CPU+多 GPU 异构系统。该方法在 OPT-175B 上实现了 3 倍加速，但缺乏与一阶优化在同等资源约束下的公平对比，其收敛性边界仍存疑。

】

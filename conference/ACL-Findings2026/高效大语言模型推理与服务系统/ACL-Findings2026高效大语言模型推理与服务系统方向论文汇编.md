# ACL-Findings2026 · 高效大语言模型推理与服务系统方向论文汇编

> 本方向共 2 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【EOP-LLM: Energy Oriented Pruning for Large Language Models ｜面向能耗约束的大语言模型动态剪枝

研究机构：美国奥本大学

作者：Guan Huang、Tao Shu

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ec48eeb9e4d9)

> 大语言模型（LLM）推理能耗已成为数据中心运营的主要成本，但现有效率优化方法多聚焦于浮点运算（FLOPs）或延迟，缺乏对实际能耗的显式建模与约束。本文指出 FLOPs 与实际能耗弱相关，提出 EOP-LLM 框架，通过设备校准能量模型与轻量级选择器，在严格每序列能量预算下动态分配计算资源。该方法在 LLaMA 3.2 与 3.1 模型上实现了能耗减半时的质量保持，但实验局限于单设备静态负载，未验证跨硬件泛化与系统级协同。

】

---

【Unlocking the Edge deployment and ondevice acceleration of multi-LoRA enabled one-for-all foundational LLM ｜冻结图约束下的多任务LLM端侧部署与自推测加速

研究机构：三星研究院

作者：Sravanth Kodavanti、Sowmya Vajrala、Srinivas Miriyala 等 16 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.18655)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.18655)

> 移动端LLM部署面临内存、延迟与运行时灵活性的三重硬约束，传统静态合并LoRA或云端协同方案无法在冻结推理图中实现多任务动态切换与低延迟并发生成。本文切入点在于将LoRA权重作为运行时输入注入单一冻结图，结合多流并发解码与无草稿模型的自推测策略，在NPU上实现单图多任务。该框架在三星Galaxy S24/S25上验证了可行性，但LoRA维度固定与静态预测嵌入限制了其泛化边界。

】

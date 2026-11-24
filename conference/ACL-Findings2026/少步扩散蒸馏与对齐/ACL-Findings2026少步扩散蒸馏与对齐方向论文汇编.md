# ACL-Findings2026 · 少步扩散蒸馏与对齐方向论文汇编

> 本方向共 2 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【FastDiSS: Few-step Match Many-step Diffusion Language Model on Sequence-to-Sequence Generation--Full Version ｜少步文本扩散模型的自条件失配与噪声感知训练

作者：Dat Nguyen-Cong、Tung Kieu、Hoang Thanh-Tung

论文原文见 [arXiv](https://arxiv.org/abs/2604.05551)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.05551)

> 连续文本扩散模型在少步采样下，自条件机制因训练-推理分布失配导致误差累积，现有方法未能针对此失效进行训练时修正。FastDiSS 通过自条件扰动（SCP）模拟推理噪声，并结合模型感知噪声缩放（MANS）动态调整高置信 token 的噪声水平，在 5 步内实现接近 20 步的生成质量。该方法在文本序列生成任务上实现了 4 倍至 400 倍的推理加速，但其对长序列误差累积边界的验证尚显不足。

】

---

【On-Policy Self-Distillation for Efficient Diffusion Language Models with Early-Stage Calibration ｜校准在线自蒸馏

作者：Huaisheng Zhu、MingYu Liu、Junze Liu 等 13 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9d223bd4529d)

> 扩散语言模型（DLLMs）在并行解码时面临早期步上下文不足导致的预测失准，严重制约了推理效率与输出质量。现有自蒸馏方法仅最大化似然，无法利用未来步信息修正早期错误，导致模型在增加并行Token数时性能急剧下降。本文提出校准在线自蒸馏（COPSD），通过构建基于未来步信息的非归一化目标分布，将其蒸馏回原始模型以校准早期预测。该方法无需演示数据，显著提升了DLLMs在数学、规划等任务上的并行生成效率，但其效果依赖于训练时的组归一化稳定性，且未验证在复杂长程推理任务上的泛化能力。

】

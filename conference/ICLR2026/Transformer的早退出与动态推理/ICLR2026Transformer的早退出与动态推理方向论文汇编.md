# ICLR2026 · Transformer的早退出与动态推理方向论文汇编

> 本方向共 2 篇（ICLR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【NRGPT: An Energy-based Alternative for GPT ｜能量基生成预训练Transformer

研究机构：IBM研究院、美国布朗大学

作者：Nima Dehmamy、Benjamin Hoover、Bishwajit Saha 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.16762)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.16762)

> 自回归语言建模长期依赖固定深度的前向传播，难以从动力学角度解释推理过程。现有“Transformer即梯度下降”的理论多局限于线性简化或图像补全场景，无法直接适配因果生成任务。本文通过构造特定能量函数，将GPT的层间变换严格形式化为能量景观上的梯度下降过程，并证明了其渐近稳定性。该工作提供了统一的理论视角，但实验规模较小，且未验证在大规模任务上的性能优势。

】

---

【What Layers When: Learning to Skip Compute in LLMs with Residual Gates ｜残差流门控实现解码器LLM的Token级层跳过

研究机构：荷兰阿姆斯特丹大学

作者：Filipe Laitenberger、Dawid Kopiczko、Cees G. M. Snoek 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.13876)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.13876)

> 解码器大语言模型在推理时对所有Token执行相同深度的计算，导致简单Token的算力浪费。现有基于离散路由或辅助头的动态计算方案存在训练不稳定或破坏预训练表示空间的问题，GateSkip通过引入平滑可微的残差门控机制，在微调阶段学习Token重要性，推理时依据门控值动态跳过低重要性Token的模块计算。该方法在1-8B参数模型上实现了生成任务精度的稳定保留，但其对骨干网络微调的依赖限制了其即插即用的通用性。

】

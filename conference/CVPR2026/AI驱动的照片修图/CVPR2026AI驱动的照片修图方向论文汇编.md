# CVPR2026 · AI驱动的照片修图方向论文汇编

> 本方向共 1 篇（CVPR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【InstantRetouch: Efficient and High-Fidelity Instruction-Guided Image Retouching with Bilateral Space ｜基于双边空间蒸馏的高效指令引导修图

研究机构：香港中文大学

作者：Jiarui Wu、Yujin Wang、Ruikang Li 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.05071)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.05071)

> 语言引导修图旨在调整色彩与色调，同时严格保留几何结构与纹理，但现有扩散模型在生成丰富美学效果时往往伴随内容漂移，且迭代采样过程导致高分辨率处理延迟极高。InstantRetouch 指出，修图操作应仅作用于视觉外观而非图像内容，因此提出在紧凑且内容解耦的双边空间中预测仿射变换参数，而非直接编辑像素或潜变量。该方法通过变分分数蒸馏将多步扩散教师模型的知识迁移至单步双边网格生成器，结合 CLIP 提示对齐损失以增强指令遵循能力。尽管其在保真度与效率上实现了数量级提升，但自建基准的泛化性验证及复杂风格指令下的语义上限仍存疑。

】

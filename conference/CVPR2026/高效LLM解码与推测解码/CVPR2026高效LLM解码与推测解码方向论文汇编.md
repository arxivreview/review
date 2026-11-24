# CVPR2026 · 高效LLM解码与推测解码方向论文汇编

> 本方向共 4 篇（CVPR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Parallel Jacobi Decoding for Fast Autoregressive Image Generation ｜并行雅可比解码

研究机构：西湖大学

作者：Boya Liao、Ying Li、Siyong Jian 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.05703)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.05703)

> 自回归图像生成因逐令牌顺序依赖导致推理延迟随分辨率线性增长，现有加速方案在长序列下收敛饱和。本文切入点在于利用图像注意力的空间局部性，将一维序列扩展改造为二维网格并行精化。通过动态激活下一行草稿令牌并引入行因果掩码，PJD 实现了免训练的并行解码。该方法在高分辨率下展现出显著加速优势，但其对长程语义依赖的建模能力仍存疑。

】

---

【Rejection Mixing: Fast Semantic Propagation of Mask Tokens for Efficient DLLM Inference ｜拒绝混合：扩散大语言模型并行解码中的连续状态协调

研究机构：上海交通大学

作者：Yushi Ye、Feng Hong、Huangjie Zheng 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_3f58587f8f0c)

> 扩散大语言模型（DLLM）通过并行去噪打破自回归顺序依赖，但激进并行导致令牌间语义互斥，形成质量-速度权衡困境。现有方法依赖显式验证块或辅助模型，引入额外计算开销且未解决离散采样缺乏位置间感知的根本缺陷。ReMix 引入连续混合状态作为中间层，允许令牌在离散化前进行迭代协调，并通过基于 JS 散度的拒绝机制防止误差级联。该方法在免训练条件下实现了 2-8 倍加速且无质量损失，但其性能上限仍受限于骨干模型能力，未超越当前 SOTA 加速比。

】

---

【SJD-PAC: Accelerating Speculative Jacobi Decoding via Proactive Drafting and Adaptive Continuation ｜主动起草与自适应延续加速投机雅可比解码

研究机构：北京大学、华为

作者：Jialiang Kang、Han Shu、Wenshuo Li 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.18599)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.18599)

> 自回归文本到图像生成因高熵特性导致标准推测解码接受率极低，现有无损加速方法如 SJD 仅能实现约 2 倍加速，难以满足实时交互需求。本文切入点在于识别 SJD 中“单令牌接受”的高频低效步骤及其成因，即拒绝后的上下文失配与验证终止逻辑。通过引入主动起草构建局部候选树与自适应延续保留有效后缀，在严格无损前提下将加速比提升至 3.8 倍。该方法验证了利用图像令牌局部性优化解码逻辑的可行性，但其对极端高熵区域的鲁棒性仍存疑。

】

---

【VVS: Accelerating Speculative Decoding for Visual Autoregressive Generation via Partial Verification Skipping ｜视觉自回归生成中的部分验证跳过加速

研究机构：清华大学、香港中文大学

作者：Haotian Dong、Ye Li、Rongwei Lu 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.13587)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.13587)

> 视觉自回归（AR）生成模型受限于逐令牌预测范式，导致图像合成延迟高，而传统推测解码（SD）虽能加速但无法减少目标模型的前向传播次数。本文切入点在于利用视觉令牌的可互换性，通过部分跳过验证步骤来显式削减目标模型调用。VVS框架结合无验证令牌选择、陈旧特征复用与动态跳过调度，在保持生成质量的同时实现了加速。该工作验证了跳过验证的可行性，但其加速比在绝对值上低于部分最新SOTA，且仅针对图像生成场景。

】

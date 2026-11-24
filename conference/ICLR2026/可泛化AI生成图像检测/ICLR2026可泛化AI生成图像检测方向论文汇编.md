# ICLR2026 · 可泛化AI生成图像检测方向论文汇编

> 本方向共 7 篇（ICLR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Data Provenance for Image Auto-Regressive Generation ｜图像自回归模型的数据溯源

作者：Bihe Zhao、Louis Kerner、Michel Meintz 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.28386)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.28386)

> 图像自回归模型（IARs）生成的图像在视觉上已难以区分，但现有水印或指纹方法需修改生成过程，无法追溯已发布的无标记内容。本文发现IAR的离散量化步骤在图像中留下了模型特有的统计伪迹，通过训练逆解码器放大该信号，实现了无需修改生成流程的后验溯源。该方法在多种IAR上实现了接近100%的归因准确率，但其有效性高度依赖模型内部的量化结构，对非量化架构的适用性存疑。

】

---

【DATA PROVENANCE FOR IMAGE AUTO-REGRESSIVE GENERATION ｜图像自回归生成数据溯源

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_41265013)

> 图像自回归模型（Image Autoregressive Models, IARs）生成的图像在视觉上已与真实照片无异，但现有水印或指纹方法需修改生成过程，无法追溯已发布的无标记内容。本文切入点在于发现IAR特有的量化伪迹：生成图像的Token表示比自然图像更贴近代码本（Codebook）条目。通过微调逆解码器并设计优化Token搜索算法，本文构建了一个后验（Post-hoc）溯源框架，无需任何生成过程干预即可实现模型级归因。该方法在多个IAR上实现了近100%的归因准确率，但其对逆解码器微调的依赖及在极端对抗攻击下的鲁棒性边界尚存疑。

】

---

【ENABLING YOUR FORENSIC DETECTOR KNOW HOW WELL IT PERFORMS ON DISTORTED SAMPLES ｜失真感知置信度模型

研究机构：深圳大学、中山大学

作者：Bin Li、Haoyu Li、Haodong Li 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_98925973)

> 在开放世界退化场景下，AI生成图像检测器常因输入质量受损而“静默失败”，即输出高置信度的错误二元判断，导致下游系统无法区分可靠与不可靠的预测。现有鲁棒性训练方法受限于退化组合爆炸，而标准置信度校准假设在异构分布偏移下失效，无法量化特定样本的检测可靠性。本文提出失真感知置信度模型（Distortion-Aware Confidence Model, DACOM），通过蒸馏全参考图像质量评估（Full-Reference Image Quality Assessment, FR-IQA）与检测精度的单调关系，构建无参考的样本级置信度预测器。该框架在提升选择性过滤准确率方面表现优异，但其对检测器内部特征线性可分性的依赖及在视觉基础模型（Vision Foundation Model, VFM）骨干上的泛化能力尚存疑问。

】

---

【FAKEXPLAIN: AI-GENERATED IMAGE DETECTION VIA HUMAN-ALIGNED GROUNDED REASONING ｜基于人类对齐定位推理的AI生成图像检测

研究机构：上海交通大学

作者：Yikun Ji、Yan Hong、Qi Fan 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_63262800)

> 可解释性检测旨在让系统不仅判断图像真伪，还需指出伪造区域并给出人类可理解的因果解释，以支撑法律与新闻场景下的信任验证。现有专用检测器输出黑盒二分类标签，而多模态大语言模型（MLLM）虽能生成文本解释，却常因缺乏空间锚点产生幻觉或无定位依据。本文切入点在于构建包含边界框与描述性字幕的人工对齐数据集，并通过渐进式强化学习微调MLLM，使其内化定位能力。该方案在检测精度与定位质量上取得平衡，但其对人工可感知伪迹的依赖限制了在完全逼真合成图像上的适用性。

】

---

【HSIC BOTTLENECK FOR CROSS-GENERATOR AND - DOMAIN-INCREMENTAL SYNTHETIC IMAGE DETEC TION ｜基于HSIC瓶颈的跨生成器与域增量合成图像检测

研究机构：国立台湾大学、国立清华大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_33667738)

> 合成图像检测面临生成模型快速迭代与检测器泛化滞后的结构性矛盾，现有基于视觉基础模型（VFM）的方法虽能捕捉通用分布差异，但常受限于骨干网络中无关语义信息的干扰，且缺乏应对新渲染域（如3DGS）的持续适应能力。本文切入点在于识别并抑制CLIP特征中与真实性无关的文本对齐噪声，同时构建信息论引导的回放机制以解决域增量学习中的灾难性遗忘。具体做法是在CLIP ViT中间层特征上施加Hilbert-Schmidt Independence Criterion (HSIC) 瓶颈，并提出HSIC-Guided Replay (HGR) 进行样本选择。该方法在3DGS持续检测任务上显著优于基线，但在通用GenImage基准上未超越最新SOTA，其价值在于为开放世界下的动态检测提供了可解释的特征整形与记忆管理范式，但HSIC对低层伪迹的压缩效应尚存疑。

】

---

【Semantic Visual Anomaly Detection and Reasoning in AI-Generated Images ｜语义视觉异常检测与推理

研究机构：北京交通大学、微软研究院

作者：Chuangchuang Tan、Xiang Ming、Jinglu Wang 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.10231)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.10231)

> 现有AI生成图像检测聚焦于像素级伪迹或全局真伪分类，难以捕捉违背物理常识或逻辑的语义级错误。本文提出将检测任务重构为结构化语义异常推理，通过多智能体框架AnomAgent构建基准AnomReason，并验证微调小模型在该新任务上超越通用大模型。该工作填补了可解释性检测的空白，但其依赖人工验证的标注流程与高昂的推理成本限制了规模化部署。

】

---

【Unveiling Perceptual Artifacts: A Fine-Grained Benchmark for Interpretable AI-Generated Image Detection ｜可解释AI生成图像检测基准与注意力对齐

研究机构：中山大学、澳大利亚国立大学

作者：Yao Xiao、Weiyan Chen、Jiahao Chen 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.19430)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.19430)

> 现有AI生成图像检测器虽能区分真假，但决策过程黑盒化，无法提供人类可验证的视觉证据。主流方法依赖低层统计特征或大语言模型文本解释，前者缺乏空间定位，后者缺乏像素级锚点。本文构建了包含三级伪迹分类的像素级标注基准X-AIGD，并提出注意力对齐损失，强制视觉Transformer关注伪迹区域。该工作揭示了高精度检测与可解释性之间的深层矛盾，但牺牲了跨数据集泛化精度，其价值在于诊断机制而非性能突破。

】

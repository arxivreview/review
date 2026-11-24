# ICLR2026 · AI生成图像质量与美学评估方向论文汇编

> 本方向共 4 篇（ICLR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Constantly Improving Image Models Need Constantly Improving Benchmarks ｜从社区噪声到结构化基准：ECHO 框架

作者：Jiaxin Ge、Grace Luo、Heekyung Lee 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.15021)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.15021)

> 现有图像生成基准滞后于模型能力演进，导致评估指标无法捕捉新模型（如 GPT-4o Image Gen）涌现的“吉卜力化”等社区自发任务。传统基准依赖人工设计或接口收集，存在指令简单、语言分布失真及更新周期长的问题。ECHO 提出一种可复用框架，通过自动化挖掘社交媒体帖子，将非结构化的用户讨论转化为包含输入、输出及社区反馈的结构化基准。该框架在区分前沿模型与开源模型上展现出 3.2 倍的相对性能差距，但其自动评估器与人类评分的弱相关性（$\tau_b=0.117$）仍构成主要存疑点。

】

---

【ImageDoctor: Diagnosing Text-to-Image Generation via Grounded Image Reasoning ｜图像医生：基于空间定位推理的文本到图像生成诊断框架

研究机构：美国约翰斯·霍普金斯大学

作者：Yuxiang Guo、Jiang Liu、Ze Wang 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.01010)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.01010)

> 文本到图像（T2I）生成模型在指令遵循与美学质量上的缺陷往往具有局部性，而现有评估模型仅输出单一标量分数，无法区分“整体美观但细节错位”与“整体平庸但局部真实”两种截然不同的失败模式，更无法指出缺陷在图像中的具体位置。ImageDoctor 通过引入轻量级热图解码器与“看-想-判”推理范式，将评估从标量回归转化为包含像素级伪影与错位定位的多维诊断任务。该框架在 RichHF-18K 基准上将平均 PLCC 从 0.586 提升至 0.741，并验证了密集空间反馈在强化学习奖励信号中的有效性。其价值在于打通了评估解释性与生成模型迭代之间的闭环，但 3B 参数骨干的视觉分辨率上限与热图解码器的架构依赖仍构成潜在瓶颈。

】

---

【ImagenWorld: Stress-Testing Image Generation Models with Explainable Human Evaluation on Open-ended Real-World Tasks ｜ImagenWorld：面向开放世界任务的生成模型可解释性压力测试

研究机构：加拿大滑铁卢大学、美国伊利诺伊大学厄巴纳-香槟分校

作者：Samin Mahdizadeh Sani、Max Ku、Nima Jamali 等 26 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.27862)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.27862)

> 导读 生成模型评估长期受困于指标碎片化与黑盒分数缺乏诊断力的双重困境，现有基准往往局限于单一任务或狭窄领域，无法反映统一模型在真实场景中的泛化能力。ImagenWorld 通过构建覆盖六类任务与六类主题的大规模人类中心基准，并引入对象级与片段级错误标注，将评估从标量打分推进至可解释的失败模式归因。其核心做法是结合结构化人类标注与视觉语言模型（VLM）自动评分，在相对排序上验证了 VLM 的可靠性，但在细粒度错误定位上仍依赖人工。该工作填补了编辑任务与多参考组合评估的空白，但其对人工标注成本的依赖限制了动态扩展性，且未量化 VLM 在片段级错误识别上的具体准确率。

】

---

【PreferThinker: Reasoning-based Personalized Image Preference Assessment ｜基于偏好画像推理的个性化图像偏好评估

研究机构：复旦大学、哈尔滨工业大学

作者：Shengqi Xu、Xinpeng Zhou、Yabo Zhang 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.00609)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.00609)

> 个性化图像偏好评估旨在利用少量参考图判断候选图是否符合特定用户审美，但现有通用偏好模型因数据不可扩展且缺乏解释性而失效。本文通过构建共享视觉元素的偏好画像，将评估转化为“预测-评估”的链式推理任务。该方法利用大规模用户数据训练画像预测，再基于画像进行多维打分，在个性化基准上显著超越通用模型。其价值在于解决了少样本个性化评估的可解释性难题，但画像预测的准确性对最终评估结果的依赖关系仍需进一步验证。

】

# CVPR2026 · AI生成图像质量与美学评估方向论文汇编

> 本方向共 13 篇（CVPR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【A$^3$: Towards Advertising Aesthetic Assessment ｜广告美学评估：从单点打分到层级诊断

研究机构：上海交通大学、华东师范大学

作者：Kaiyuan Ji、Yixuan Gao、Lu Sun 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.24037)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.24037)

> 广告图像评估长期依赖主观打分，缺乏可解释性与规模化能力，现有自动系统仅能作为阈值过滤器，无法提供针对性修改建议。本文切入点在于将抽象的AIDA营销理论操作化为可执行的视觉评估层级，通过构建包含思维链（Chain-of-Thought, CoT）的数据集与多信号强化学习训练范式，实现从感知到欲望的渐进式诊断。该方法在自建基准上显著优于通用多模态大语言模型（Multimodal Large Language Models, MLLMs），但其规则体系隐含的普适性假设与特定商业场景的绑定，使其泛化边界仍存疑。

】

---

【CREward: A Type-Specific Creativity Reward Model ｜类型特定创造力奖励模型

研究机构：加拿大西蒙弗雷泽大学

作者：Jiyeon Han、Ali Mahdavi-Amiri、Hao Zhang 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.19995)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.19995)

> 视觉生成中的创造力常被简化为单一标量分数，导致评估缺乏诊断力且无法指导针对性优化。现有通用美学或质量指标（如FID、CLIPScore）无法区分几何、材质与纹理等具体维度的创造性差异。本文提出CREward，通过解耦三维创造力轴并训练轻量级奖励模型，实现从评估到生成的闭环控制。该框架验证了大视觉语言模型（LVLM）标签的有效性，但在小样本基准上的泛化能力仍存疑。

】

---

【DPGF-Net: Dual-Prior Guided Fusion Network for Joint Assessment of Perceptual Quality and Semantic Consistency in AI-Generated Images ｜双先验引导融合网络

研究机构：重庆大学、新加坡南洋理工大学

作者：Tao Li、Xingran Liao、Mingliang Zhou

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_0c88c94d0833)

> 本文旨在解决AI生成图像中感知质量与语义对齐难以解耦、导致缺陷归因模糊的问题。现有CLIP-based方法虽能处理图文一致性，但缺乏对图像内部失真与内容特征的显式分离，且在跨数据集评估中表现不稳定。DPGF-Net通过引入失真与内容双先验，结合局部文本条件聚合与全局调制机制，实现了两个维度的联合建模。该方法在多个基准上取得了SOTA性能，但其对Re-IQA双编码器结构的依赖及未报告的计算开销，限制了其在实时场景下的适用性判断。

】

---

【E-comIQ-ZH: A Human-Aligned Dataset and Benchmark for Fine-Grained Evaluation of E-commerce Posters with Chain-of-Thought ｜电商海报细粒度评估框架

研究机构：阿里巴巴集团

作者：Meiqi Sun、Mingyu Li、Junxiong Zhu

论文原文见 [arXiv](https://arxiv.org/abs/2602.21698)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.21698)

> 生成式AI在电商海报创作中面临的核心矛盾是：视觉吸引力与商业功能性（如中文文案准确性、产品可见性）难以被现有自动化工具同时量化。传统图像质量评估（IQA）模型仅关注低层失真，通用多模态大语言模型（MLLMs）则缺乏对密集中文排版中笔画级错误的感知能力，导致评估结果与专家判断严重脱节。本文构建了首个包含专家校准思维链（Chain-of-Thought, CoT）的中文电商海报多维数据集，并训练了领域专用评估模型E-comIQ-M。该工作填补了垂直领域功能性评估的空白，但其绝对相关性指标（SRCC 0.433）仍属中等水平，且高度依赖特定领域的专家标注，跨域泛化能力存疑。

】

---

【Evaluating Generative Models via One-Dimensional Code Distributions ｜离散令牌统计视角下的生成模型评估

研究机构：北京大学、复旦大学

作者：Zexi Jia、Pengcheng Luo、Yijia Zhong 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.08064)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.08064)

> 生成模型评估长期受困于连续特征分布指标与人类感知质量的错位，FID等主流方法因高斯假设和全局池化而丢失局部伪影信号。本文摒弃识别特征空间，转向离散视觉令牌（Token）统计域，提出无训练的分布距离CHD与自监督单图质量分CMMS。通过重训练1D分词器并构建VisForm多域基准，验证了令牌频率与共现模式对感知质量的敏感性。该范式在精度上超越现有SOTA，但完全依赖合成退化监督，其能否覆盖真实生成模型的复杂语义缺陷仍存疑。

】

---

【Fine-grained Image Aesthetic Assessment: Learning Discriminative Scores from Relative Ranks ｜细粒度图像美学评估：基于相对排名的判别分数学习

研究机构：西安电子科技大学、香港中文大学

作者：Zhichao Yang、Jianjie Wang、Zhixianhe Zhang 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.03907)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.03907)

> 图像美学评估（Image Aesthetic Assessment, IAA）长期依赖单图绝对打分，但在摄影连拍或AI生成同提示词序列中，图像语义高度一致而美学差异细微，导致传统模型无法区分优劣。现有基准如AVA仅评估独立图像，缺乏序列内相对排序标签，致使模型在细粒度场景下性能骤降。本文提出FGAesthetics数据集与FGAesQ模型，通过差异保留分词与排名感知回归，从相对排名中学习判别分数。该方法在细粒度序列评估上显著超越SOTA，但在粗粒度绝对评分上略逊于最新多模态大模型，其泛化性仍受限于自建数据集的单一来源。

】

---

【PosterIQ: A Design Perspective Benchmark for Poster Understanding and Generation ｜海报设计视角的多模态大语言模型基准

研究机构：香港理工大学

作者：Yuheng Feng、Wen Zhang、Haodong Duan 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.24078)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.24078)

> 现有图像生成评估多聚焦于通用美学或文本对齐，忽视了海报作为高约束视觉媒介中排版、字体与语义意图的耦合关系。通用多模态大语言模型（MLLMs）在海报理解上虽能识别基础元素，但作为自动评分器时缺乏对设计质量的敏感度，且生成模型难以兼顾构图与文字渲染。本文构建了覆盖理解与生成全链路的PosterIQ基准，通过解耦OCR、字体、布局、风格及意图等24项任务，量化了模型在设计约束下的表现。该基准揭示了前沿模型在高层推理上的优势与在细粒度设计评分上的失效，为设计导向的生成模型提供了诊断工具，但其对“创造力”的量化仍局限于元素存在性验证。

】

---

【PosterReward: Unlocking Accurate Evaluation for High-Quality Graphic Design Generation ｜海报生成质量评估与奖励建模

研究机构：香港科技大学、美团

作者：Jianyu Lai、Sixiang Chen、Jialin Gao 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d0163a17a74c)

> 海报生成任务要求模型同时满足视觉质量、文本渲染准确性与版式构图，但现有通用奖励模型（如HPSv3）缺乏针对图形设计的专业评估能力，且领域偏好数据极度稀缺。本文切入点在于构建自动化AI偏好数据闭环，并设计级联式多阶段训练策略，以解耦分析推理与分数预测。该工作验证了专用奖励模型在垂直设计领域的显著优势，但其AI标注可靠性与通用基准上的微弱增益仍存疑。

】

---

【Probabilistic Prompt Adaptation for Unified Image Aesthetics and Quality Assessment ｜概率提示适应统一图像美学与质量评估

作者：Takayuki Hara、Yuya Otsuka

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f397aafbdef6)

> 图像美学与质量评估长期受困于固定评分标准与细粒度语义控制之间的割裂，现有模型要么牺牲精度换取提示灵活性，要么依赖大量文本标注实现特征对齐。本文提出概率提示适应框架，将文本提示视为潜变量，通过边缘化实现无标注训练。该框架在多个基准上达到最先进水平，同时支持任意提示条件评估。其核心假设——最优提示可由图像与任务动态推断——在缺乏极端局部伪影数据时是否依然稳健，尚存疑问。

】

---

【R4-CGQA: Retrieval-based Vision Language Models for Computer Graphics Image Quality Assessment ｜检索增强视觉语言模型用于计算机图形图像质量评估

研究机构：新加坡南洋理工大学

作者：Zhuangzi Li、Jian Jin、Shilv Cai 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.10578)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.10578)

> 计算机图形（CG）渲染图像的质量评估长期受限于数据集仅含标量分数、缺乏可解释性，且直接迁移自然图像评估方法因失真模式差异而失效。现有视觉语言模型（VLM）在CG领域存在幻觉且微调成本高，本文切入点在于利用视觉相似图像的文本描述作为外部知识，通过检索增强生成（Retrieval-Augmented Generation, RAG）提升VLM的评估准确性。具体做法是构建含六维质量描述的3.5K数据集，并设计基于内容-质量双流相似度的贝叶斯检索框架。该方案验证了免微调范式在CG质量诊断上的有效性，但其检索库的静态覆盖范围与实时渲染场景的延迟需求之间仍存在张力。

】

---

【SCIEval: Evaluating and Benchmarking the Faithfulness of Scientific Image Generation and Interpretation with Large Multimodal Models ｜科学图像忠实度评估

研究机构：湖南大学

作者：Guanghui Ye、Huan Zhao、Zhixue Zhao 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8db21ba5a03a)

> 科学图像生成与解读任务要求模型精确捕捉数值、属性等细节，但现有通用评估指标无法区分“大致正确”与“细节错误”。本文切入点在于将忠实度解耦为相关性、准确性与可解释性三个维度，并针对科学域微调轻量级CLIP编码器与LMM解释器。通过构建6,000样本的专用基准，SCIEval在Pearson相关系数上超越GPT-4o等前沿模型。其价值在于提供了低成本、可解释的科学域评估方案，但跨域泛化能力与标注一致性仍存疑。

】

---

【Too Vivid to Be Real? Benchmarking and Calibrating Generative Color Fidelity ｜色彩保真度基准与校准

研究机构：哈尔滨工业大学、复旦大学

作者：Zhengyao Fang、Zexi Jia、Yijia Zhong 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.10990)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.10990)

> 文本到图像生成模型在追求语义对齐时，常因过度优化视觉冲击力而产生过饱和色彩，导致“真实感”缺失。现有偏好驱动指标（如HPSv3）存在系统性鲜艳度偏见，无法区分“生动”与“真实”，致使评估失效。本文通过构建基于引导尺度（CFG）控制的有序失真数据集，训练具备序数感知能力的多模态评估器，并引入无训练的空间-时间引导调制机制。该框架在色彩保真度维度上显著优于通用美学指标，但其有效性依赖于CFG失真模式的覆盖度，且未验证对非色彩类伪影的泛化能力。

】

---

【Venus: Benchmarking and Empowering Multimodal Large Language Models for Aesthetic Guidance and Cropping ｜美学指导与裁剪的多模态大语言模型框架

研究机构：北京大学

作者：Tianxiang Du、Hulingxiao He、Yuxin Peng

论文原文见 [arXiv](https://arxiv.org/abs/2602.23980)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.23980)

> 本文旨在解决普通用户无法在拍摄前获得专业级美学反馈的痛点，现有多模态大语言模型（MLLMs）往往提供过度积极的无效反馈，而专用裁剪模型则缺乏解释性。Venus通过构建首个美学指导（Aesthetic Guidance, AG）基准AesGuide，并采用两阶段指令微调策略，赋予MLLMs识别缺陷并提供可执行建议的能力，进而激活其基于思维链（Chain-of-Thought, CoT）的美学裁剪功能。该框架在真实摄影场景下实现了可解释与交互式的美学优化，但其评估指标依赖GPT作为裁判，且未验证指导对重拍后图像质量的直接因果影响。

】

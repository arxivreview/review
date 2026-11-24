# ICLR2026 · CLIP分析与增强方向论文汇编

> 本方向共 7 篇（ICLR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【CLIP-FMOE: SCALABLE CLIP VIA FUSED MIXTURE OF-EXPERTS WITH ENFORCED SPECIALIZATION ｜CLIP-FMoE：融合门控混合专家架构下的CLIP稀疏扩展

作者：Luong Tran、Lan-Cuong Nguyen、Huynh Dang Nguyen 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_13693607)

> 导读 CLIP模型在细粒度视觉理解与大规模部署中面临容量扩展与计算成本的双重约束，纯参数扩展因训练资源需求过高而难以普及。现有MoE适配方法存在专家专业化不足与灾难性遗忘两大瓶颈，导致零样本泛化能力在微调后显著退化。本文提出CLIP-FMoE，通过隔离约束对比学习（ICCL）并行训练域特定专家，并引入融合门控机制动态保留预训练知识。该方法在保持零样本性能的同时提升了细粒度任务表现，但其专家专业化程度与跨域鲁棒性的量化关系尚待验证。

】

---

【MICLIP: LEARNING TO INTERPRET REPRESENTATION IN VISION MODELS ｜机制可解释性中的因果语义对齐

研究机构：上海科技大学

作者：Yingdong Shi、Zhiyu Yang、Changming Li 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_19626935)

> 视觉模型内部机制的可解释性长期受困于“激活幅度假设”与“输入中心性”的双重局限，导致对神经元功能的描述缺乏因果效力，尤其在模型预测错误时失效。MICLIP 通过对比学习将内部表示单元映射至 CLIP 语义空间，同时接地输入概念与输出语义，实现了从启发式相关性到因果语义对齐的范式转换。该方法在 ImageNet-1k 神经元描述准确率达到 1.0000，并在 DTD 未见概念干预中展现出稳定的因果调控能力。其价值在于提供了跨架构的通用解释框架，但神经元编码器的线性假设是否足以捕捉深层非线性机制，仍是存疑之处。

】

---

【NeuCLIP: Efficient Large-Scale CLIP Training with Neural Normalizer Optimization ｜神经归一化器优化

研究机构：美国德州农工大学、国立台湾大学

作者：Xiyuan Wei、Chih-Jen Lin、Tianbao Yang

论文原文见 [arXiv](https://arxiv.org/abs/2511.08417)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.08417)

> 大规模对比语言-图像预训练（CLIP）的核心瓶颈在于对比损失中归一化项的精确估计，传统方法依赖超大批次或存在偏差的移动平均近似，导致优化误差随数据集规模与批次大小之比线性增长。NeuCLIP 通过凸分析与变分分析重构损失函数，将归一化项显式化为优化变量，并引入紧凑的归一化预测网络（NPN）进行联合优化。该方法在 DFN-14M 数据集上取得 39.16% 的 Datacomp 平均性能，优于 FastCLIP 的 38.45%。其价值在于提供了无偏梯度估计的理论基础，但 NPN 的架构限制与重初始化策略的敏感性仍存疑。

】

---

【RLAP-CLIP: CONTINUAL MULTIMODAL LEARNING - WITH PROTOTYPE ADAPTATION AND DIFFICULTY AWARE ROUTING ｜持续多模态学习中的原型优化与难度感知路由

研究机构：华中科技大学

作者：Ruikun Luo、Jiarui Wang、Yuan Gao 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_37104505)

> 持续学习场景下，视觉-语言模型在序列任务中面临稳定性与可塑性的双重约束，现有参数高效微调方法因被动平均原型与单模态适配导致性能退化。本文指出原型质量随任务累积而漂移、视觉编码器被静态化利用是两大瓶颈，提出基于强化学习的原型优化（RLPO）与难度感知混合专家（MoE）路由机制，结合双模态提示实现跨任务知识保持。该方法在八个基准上取得平均准确率最高4.52个百分点的增益，但其收益高度依赖细粒度任务特性，对粗粒度分类的边际贡献有限，且未验证在极端内存约束下的鲁棒性。

】

---

【Sparse CLIP: Co-Optimizing Interpretability and Performance in Contrastive Learning ｜原生稀疏化对比学习：可解释性与性能的协同优化

研究机构：英国牛津大学

作者：Chuan Qin、Constantin Venhoff、Sonia Joseph 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.20075)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.20075)

> 当前视觉-语言模型面临的核心困境是：增强可解释性的手段往往以牺牲下游任务精度为代价，导致模型在安全审计与高效部署间难以兼顾。事后稀疏自编码器（SAE）虽能解耦特征，但普遍存在重建误差累积及模态割裂问题，无法保留 CLIP 原生的跨模态对齐能力。本文通过修改 CLIP 训练流程，引入非负约束与维度扩展，直接在预训练阶段生成稀疏且多模态的特征表示。这一方法在保持零样本分类性能的同时实现了特征的可解释性，但其性能增益究竟源于稀疏化机制还是维度扩展带来的参数冗余，仍需进一步剥离验证。

】

---

【TEST-TIME POISONED SAMPLE DETECTION BY EX - PLOITING SHALLOW MALICIOUS MATCHING IN BACK DOORED CLIP ｜浅层恶意匹配与子空间检测

研究机构：哈尔滨工业大学、香港中文大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_24119445)

> 后门攻击使CLIP在含触发器图像上产生错误分类，但现有测试时检测方法多依赖单模态扰动或手工文本变体，缺乏对多模态几何结构的系统性利用。本文发现中毒图像与目标文本的匹配是“浅层”的，无法泛化至语义等价变体，而良性图像则保持“深层”匹配。通过构建局部文本流形子空间并沿正方向采样特征放大差异，该方法在测试时实现了对中毒图像的高精度检测。其在ImageNet-1K上平均AUROC达0.922，显著优于现有基线，但依赖手工文本变换的泛化能力仍存疑。

】

---

【UNLOCKING THE POWER OF CO-OCCURRENCE IN CLIP: A DUALPROMPT-DRIVEN METHOD FOR - TRAINING-FREE ZERO-SHOT MULTI-LABEL CLAS SIFICATION ｜双提示驱动无训练零样本多标签分类

研究机构：日本理化学研究所、香港理工大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_44911817)

> 零样本多标签分类要求模型在未见过的图像上同时识别多个物体，但CLIP因预训练目标聚焦单一显著物体且推理提示缺乏标签间关联，导致其在此场景下性能显著下滑。现有方法要么依赖ViT局部特征增强而牺牲骨干通用性，要么通过微调引入过拟合风险，均未能从提示层面解耦共现信息的正负效应。本文提出DualPrompt，通过判别性提示与相关性提示的因果组合，在无训练条件下利用少量数据估计的共现先验校准预测。该方法在MS-COCO上以70.0% mAP超越所有对比基线，但其对共现估计数据量的依赖及对象幻觉的残留风险，限制了其在极端稀疏数据场景下的泛化边界。

】

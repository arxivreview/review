# CVPR2026 · Segment Anything 模型适配与提示工程方向论文汇编

> 本方向共 5 篇（CVPR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Attack for Defense: Adversarial Agents for Point Prompt Optimization Empowering Segment Anything Model ｜对抗式点提示优化

研究机构：南京大学

作者：Xueyu Liu、Xiaoyi Zhang、Guangze Shi 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.18891)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.18891)

> 提示分割基础模型在无人交互场景下依赖低质量初始提示，导致分割精度在跨域任务中显著波动。现有启发式或孤立强化学习策略缺乏对提示效用的动态推理能力，且对初始分布敏感。本文提出 Point Prompt Defender (PPD)，通过攻击-防御双智能体对抗强化学习，在任务无关的双空间图环境中筛选并优化点提示。该框架实现了即插即用的提示净化，但在绝对分割性能上仍受限于纯提示优化的天花板，其对抗训练的泛化边界尚需更严苛的持续流式验证。

】

---

【Dual-level Adapter Boosting Prompt-free Curvilinear Structure Segmentation ｜双层级适配器驱动的无提示曲线结构分割

研究机构：武汉大学

作者：Kai Zhu、Li Chen、Jun Cheng

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e4f1f167675f)

> 曲线结构分割（CSS）面临局部细节保真与全局拓扑连贯性的根本矛盾，且离散提示机制在此类任务中失效。现有SAM适配方法仅处理块内局部特征，缺乏跨层全局建模能力，导致跨域泛化不足。SACM通过冻结SAM编码器并注入块内与块间双层级适配器，结合无提示融合解码器，以18张图像实现少样本微调。该方法在12个数据集上验证了SOTA性能，但其无提示设计是否牺牲了通用分割能力仍存疑。

】

---

【Live Interactive Training for Video Segmentation ｜实时交互式训练（LIT）：推理时在线适配视频分割

研究机构：美国康奈尔大学

作者：Xinyu Yang、Haozheng Yu、Yihong Sun 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.26929)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.26929)

> 交互式视频分割在遮挡、形变等复杂场景下频繁出错，现有模型仅将用户修正用于即时修复，无法从反馈中学习，导致同一错误反复出现，用户需重复标注。本文提出实时交互式训练（Live Interactive Training, LIT）框架，其核心实现 LIT-LoRA 在推理阶段利用用户修正信号在线训练轻量级 LoRA 模块，使模型能泛化至后续相似错误。该方法在四个基准上将用户修正次数减少 18-34%，单次更新开销约 0.5 秒。其价值在于将静态适配转化为动态交互学习，但验证闭环依赖 IoU 阈值，对细微错误的学习边界尚不明确。

】

---

【PR-MaGIC: Prompt Refinement Via Mask Decoder Gradient Flow For In-Context Segmentation ｜掩码解码器梯度流驱动的提示精炼

作者：Minjae Lee、Sungwoo Hur、Soojin Hwang 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.12113)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.12113)

> 少样本分割中，支持图像与查询图像的外观差异导致自动生成的提示点存在假阳性或语义模糊，进而使分割掩码质量下降。现有自动提示框架依赖静态相似度映射，无法在推理阶段修正这些次优提示。PR-MaGIC 提出一种无训练的测试时框架，利用 SAM 掩码解码器的梯度流迭代更新查询嵌入分布，并重采样提示点。该方法在六个基准上作为即插即用模块提升了分割精度，但其收敛性依赖于初始分布接近解码器最优邻域的假设，在语义差距较大时稳定性存疑。

】

---

【SAMIX: Reinforcing SAM2 with Semantic Adapter and Reference Selecting Policy for Mix-Supervised Segmentation ｜混合监督分割中的密集上下文提示机制

研究机构：华中科技大学、上海交通大学

作者：Qiang Hu、Jiajie Wei、Zhenyu Yi 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_cce5c40d92a2)

> 混合监督分割旨在统一利用掩码、框、点等异构标注，但现有基于基础模型的方法仅将弱标签视为稀疏空间提示，导致在边界模糊场景下性能受限且无法利用无标注数据。SAMIX 通过改造 SAM2 的记忆机制，引入跨图像语义检索与强化学习驱动的参考集选择，解决了稀疏提示在复杂场景下的信息缺失问题。该方法在统一数据设定下显著提升了通用与特定数据集的分割精度，但其对参考图像质量的依赖及强化学习训练的稳定性仍存疑。

】

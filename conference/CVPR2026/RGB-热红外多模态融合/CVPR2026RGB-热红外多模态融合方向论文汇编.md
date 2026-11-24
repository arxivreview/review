# CVPR2026 · RGB-热红外多模态融合方向论文汇编

> 本方向共 8 篇（CVPR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【3M-TI: High-Quality Mobile Thermal Imaging via Calibration-free Multi-Camera Cross-Modal Diffusion ｜无标定多相机跨模态扩散热成像

研究机构：上海交通大学、复旦大学

作者：Minchong Chen、Xiaoyun Yuan、Junzhe Wan 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.19117)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.19117)

> 移动端热红外传感器因硬件限制导致分辨率低、纹理模糊，现有RGB引导超分方法依赖严格的像素级标定，难以在实际多相机系统中部署。3M-TI通过变分自编码器潜空间中的跨模态自注意力机制，实现了无需显式配准的特征对齐与融合。该方法结合失配数据增强与单步扩散模型，在真实手机多相机系统上验证了其在感知质量与下游任务中的有效性。尽管其在保真度指标上仅微弱领先，但证明了隐式对齐在复杂非对齐场景下的可行性，其极端失配下的稳定性边界仍存疑。

】

---

【DarkAct: A RGB-Thermal Dataset and Fusion Framework for Multimodal Low-Light Action Recognition ｜低光照RGB-热红外动作识别数据集与融合框架

研究机构：武汉大学、哈尔滨工业大学

作者：Yuanjun Tan、Aoran Xiao、Liqian Deng 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_321cf2d8b52c)

> 导读 低光照环境下，RGB图像纹理丢失与热红外图像缺乏细节的互补性矛盾，使得传统单模态或固定权重融合的动作识别方法失效。现有视觉语言模型在跨光谱低光场景下泛化能力骤降，而缺乏大规模配对视频数据制约了专用模型的训练。本文构建了包含12,778对视频的DarkAct数据集，并提出基于运动感知注意力与光照自适应融合的DarkAct-Net框架。该工作填补了低光照RGB-T动作识别的数据空白，但其融合机制对视频帧间累积漂移的鲁棒性尚未得到充分验证。

】

---

【Physical Adversarial Clothing Evades Visible-Thermal Detectors via Non-Overlapping RGB-T Pattern ｜非重叠RGB-T模式与空间离散连续优化

研究机构：清华大学

作者：Xiaopei Zhu、Guanning Zeng、Zhanhao Hu 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.04675)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.04675)

> RGB-T多模态检测器在物理世界中的对抗脆弱性长期被忽视，现有攻击方法受限于2D视角或材料重叠导致的光衰减。本文通过构建3D全视角模型与非重叠材料设计，提出空间离散连续优化算法，实现了数字与物理世界的高成功率攻击。该方法揭示了多模态融合架构在物理对抗下的系统性失效，但物理世界攻击成功率与数字模拟存在显著差距，材料物理特性的影响尚未完全解耦。

】

---

【Progressive Multi-cue Alignment for Unaligned RGBT Tracking ｜渐进多线索对齐的非对齐RGB-T跟踪

研究机构：安徽大学

作者：Jiandong Jin、Chenglong Li、Hao Feng 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_7638a9932323)

> 非对齐RGB-T跟踪旨在解决传感器视差与时间延迟导致的跨模态空间失配问题，现有方法因同时估计所有对齐参数而难以适应动态变化的失配程度，且计算开销大。本文切入点在于将对齐参数解耦为中心偏移、尺度变换与全局细化三个渐进阶段，并引入难度感知专家路由以平衡精度与效率。该方法通过分层几何校正与变换引导的跨模态融合，在LasHeR-Unaligned和MUART244数据集上取得了SOTA性能。其价值在于证明了渐进式解耦对齐在严重动态失配场景下的有效性，但其在多目标跟踪中的身份一致性维持能力尚未验证。

】

---

【RAGTrack: Language-aware RGBT Tracking with Retrieval-Augmented Generation ｜语言感知RGB-T跟踪与检索增强生成

研究机构：大连理工大学

作者：Hao Li、Yuhao Wang、Wenning Hao 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.03617)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.03617)

> RGB-T跟踪旨在利用可见光与热红外的互补性实现全天候目标定位，但现有方法依赖初始帧视觉模板，在外观剧烈变化时易发生漂移。本文切入点在于引入语言模态作为高层语义锚点，通过检索增强生成机制动态更新目标描述，解决视觉表征的歧义性与搜索冗余问题。RAGTrack通过多模态Transformer编码器、自适应Token融合及上下文感知推理模块，实现了视觉与语言的统一建模。该方法在四个基准上取得SOTA，但引入了MLLM推理延迟，且语言标注的生成依赖预训练模型，其泛化边界尚待验证。

】

---

【TherA: Thermal-Aware Visual-Language Prompting for Controllable RGB-to-Thermal Infrared Translation ｜热感知视觉语言提示下的可控RGB到热红外翻译

研究机构：韩国首尔大学

作者：Dong-Guw Lee、Tai Hyoung Rhee、Hyunsoo Jang 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.19430)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.19430)

> RGB到热红外（RGB-to-TIR）翻译旨在解决热红外数据标注成本高且物理一致性难以保证的问题。现有方法多将翻译简化为像素级风格迁移，导致生成结果违背热辐射物理规律。本文通过引入热感知视觉语言模型（TherA-VLM）生成结构化热嵌入，作为扩散模型的条件输入，实现了物理一致且可控的伪热红外图像生成。该方法在基准测试中显著优于现有SOTA，但仅适用于相对温度图像，绝对辐射值建模仍是空白。

】

---

【Tri-Modal Fusion Transformers for UAV-based Object Detection ｜三模态融合Transformer用于无人机目标检测

研究机构：丰田研究所

作者：Craig Iaboni、Pramod Abichandani

论文原文见 [arXiv](https://arxiv.org/abs/2604.16630)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.16630)

> 无人机在低光照、运动模糊及热杂波等复杂环境下，单一传感器或双模态组合均存在失效盲区，现有检测器缺乏对RGB、热红外与事件相机三模态交互机制的系统性研究。本文切入点在于将三模态融合视为架构设计空间，通过双分支层级Transformer在特定深度插入门控交换模块，实现模态间可控的信息互补。该框架通过61组受控消融实验量化了融合深度与机制的影响，证明了三模态融合优于所有双模态基线，但其在非对齐场景下的鲁棒性因硬件预对齐而被掩盖，且缺乏与主流RGB-T Transformer基线的公平对比。

】

---

【Uncertainty-Aware Modality Fusion for Unaligned RGB-T Salient Object Detection ｜不确定性感知模态融合网络

研究机构：天津大学、西班牙马德里自治大学

作者：Mianzhao Wang、Fan Shi、Xu Cheng 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_456ab30372b5)

> 非对齐RGB-T显著性目标检测（SOD）的核心痛点在于传感器视差导致的像素级错位，传统显式几何配准方法计算开销大且对遮挡敏感。现有隐式对齐方法在语义模糊场景下仍难以建立像素级一致性，且融合阶段缺乏对模态可靠性的动态评估。本文提出UMFNet，将对齐问题重构为特征空间内的不确定性感知表示学习，通过高斯潜变量建模实现隐式对齐，并利用置信度图门控融合。该方法在多个非对齐基准上取得SOTA，但其性能增益是否完全归因于概率建模而非骨干网络优势，仍需更严格的消融验证。

】

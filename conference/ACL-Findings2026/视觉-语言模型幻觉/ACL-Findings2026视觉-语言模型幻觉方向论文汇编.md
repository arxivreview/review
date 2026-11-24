# ACL-Findings2026 · 视觉-语言模型幻觉方向论文汇编

> 本方向共 10 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Aligning with Your Own Voice: Self-Corrected Preference Learning for Hallucination Mitigation in LVLMs ｜基于验证自校正的偏好对齐

作者：Byeonggeuk Lim、JungMin Yun、Junehyoung Kwon 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.24395)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.24395)

> 大视觉语言模型（LVLMs）在生成描述时，常因语言先验压制视觉信号而产生对象、属性及关系幻觉。现有基于直接偏好优化（DPO）的方法依赖专有模型（如GPT-4V）构建偏好对，导致外部数据与目标模型内在分布不匹配，阻碍有效对齐。本文提出AVES-DPO，通过场景图提取与共识验证诊断幻觉，引导模型自校正生成分布内偏好对，以5.2k样本实现SOTA级幻觉抑制。该方法在数据效率上优势显著，但13B模型在通用能力上出现保守倾向，其自校正上限是否受限于初始模型能力仍存疑。

】

---

【Distorted or Fabricated? A Survey on Hallucination in Video LLMs ｜视频大语言模型幻觉的机制驱动分类与缓解

研究机构：美国东北大学

作者：Yiyang Huang、Yitian Zhang、Yizhou Wang 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.12944)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.12944)

> 视频大语言模型（Video Large Language Models, Vid-LLMs）在处理时序输入时，常因静态视觉编码器的局限与语言先验的干扰，生成看似连贯但违背视频实际内容的描述。现有图像幻觉缓解策略难以直接迁移至视频场景，因为视频引入了因果推理、运动动态及音画整合等维度，导致静态指标失效。本文提出了一种基于机制的视频幻觉分类体系，将幻觉划分为动态失真与内容捏造两大类，并系统梳理了针对各子类的评估基准与干预策略。该工作填补了视频幻觉研究的结构性空白，但其分类边界在复杂多模态场景下的鲁棒性仍存疑。

】

---

【Global Context or Local Detail? Adaptive Visual Grounding for Hallucination Mitigation ｜冲突驱动视觉证据获取

研究机构：北京航空航天大学、美团

作者：Yubo Jiang、Xin Yang、Abudukelimu Wuerkaixi 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.24396)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.24396)

> 大视觉语言模型（LVLMs）在多步推理中常因视觉证据脱节产生对象幻觉，现有推理时干预多聚焦于解码或表征层，忽略了输入端视觉证据获取的结构性缺陷。Think-with-Images（TwI）范式试图通过生成辅助视图解决此问题，但面临粒度-上下文权衡与工具提案过度信任两大瓶颈。Active-Look通过双专家分歧检测冲突区域，并采用混合渲染策略在预算约束下选择性验证，实现了无需训练的幻觉抑制。该方法在POPE Adversarial设置上较基线提升4.94%，但在CHAIR自由生成任务上未超越最新SOTA，其依赖外部检测器的设计引入了固定计算开销。

】

---

【Inject to Heal: Alleviating hallucination in LVLMs via Context Embedding Injection ｜上下文嵌入注入

作者：Mehrdad Fazli、Bowen Wei、Ziwei Zhu

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9f9185eac5ff)

> 大视觉语言模型（LVLMs）在开放生成中常因语言先验压制视觉信号而产生对象幻觉，现有推理时干预方法多聚焦于Logits层对比或注意力校准，难以在长序列生成中维持稳定的视觉接地。本文切入点在于发现真实Token比幻觉Token更早稳定概率质量的“承诺深度差距”，并据此提出无需训练的上下文嵌入注入（Context Embedding Injection, CEI）策略。该方法通过复用初始前向传播的隐状态作为接地锚点，动态调整解码过程中的隐状态混合权重，以抑制幻觉。CEI在CHAIR、AMBER和MMHal-Bench上优于主流基线，但其对超参数的依赖及在判别式任务上的表现未经验证。

】

---

【Mitigating Hallucinations in VLMs: Enhancing Visual Attention via Head-Wise Perturbation ｜头部感知扰动与视觉引导训练

研究机构：复旦大学

作者：Zhenghua Wang、Yixin Wu、Feiran Zhang 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1fb3c9be414e)

> 视觉语言模型（VLMs）在生成描述时，常因过度依赖语言先验而忽略视觉证据，导致对象幻觉。现有推理时干预方法虽无需重训，但面临计算开销大与超参数敏感的问题，且难以从根源上改变模型对视觉信号的分配机制。本文提出HWP，通过在多头注意力（MHA）中注入连续均匀噪声并限制损失计算于视觉敏感Token，以训练时微调的方式重构注意力分布。该方法在POPE基准上平均提升2.1点准确率，但其训练时干预路线与当前主流的无训练范式存在部署成本上的根本差异。

】

---

【Perceptual Hallucination in Vision–Language Models: Definition, Analysis and Verification ｜文档感知幻觉的量化与归因分析

作者：Taewook Hwang、Inbum Heo、Sung Jun Lee 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ea1311568b63)

> 视觉语言模型在文档理解任务中常因视觉证据缺失而生成看似感知的虚假信息，这一现象被称为感知幻觉。现有研究多聚焦于自然图像的对象幻觉或推理阶段的逻辑错误，缺乏对文档场景下视觉感知阶段失效的系统性量化。本文构建了包含原始-受损图像对的基准数据集，通过激活补丁技术定位视觉编码器在幻觉生成中的因果作用，并验证了基于大语言模型的后验过滤策略。该工作明确了文档感知幻觉的机制根源，但未提供生成阶段的实时干预算法，其缓解效果仅依赖外部检测器。

】

---

【Revealing and Enhancing Core Visual Regions: Harnessing Internal Attention Dynamics for Hallucination Mitigation in LVLMs ｜正注意力动态增强

研究机构：西安电子科技大学

作者：Guangtao Lyu、Qi Liu、Chenghao Xu 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.15556)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.15556)

> 大视觉语言模型（LVLMs）在生成描述时，常因语言先验压制视觉信号而产生对象幻觉。现有推理时干预方法要么依赖多前向传播引入扰动偏差，要么依赖静态注意力信号易受注意力汇聚（Attention Sink）干扰。本文发现层间正注意力动态（Positive Attention Dynamics, PAD）能更可靠地揭示语义核心视觉区域，据此提出PADE，通过单次前向传播在注意力Logits层注入动态信号以抑制幻觉。该方法在保持通用多模态理解能力方面表现优异，但在幻觉抑制的绝对指标上仍落后于最新解耦解码策略，其动态信号在不同架构下的鲁棒性尚存疑。

】

---

【System-Mediated Attention Imbalances Make Vision-Language Models Say Yes ｜系统介导注意力失衡与视觉语言模型Yes-bias

作者：Tsan Tsai Chan、Varsha Suresh、Anisha Saha 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f8b1ec28d4f9)

> 导读 视觉语言模型（VLMs）在二元判断任务中常表现出无差别回答“是”的偏差，即Yes-bias，这源于输入模态间注意力分配的结构性失衡。现有缓解策略多基于“图像中心”假设，试图通过增强图像注意力来抑制幻觉，但缺乏对系统模态冗余注意力的因果验证，导致在依赖细粒度信息的组合任务上效果受限。本文提出“系统介导”假设，通过因果干预将解码器后层的系统模态注意力比例重分配至图像与文本模态，以恢复细粒度信息提取能力。该框架在五个组合基准上显著优于图像增强基线，但在依赖高层表征的知识提取任务上失效，揭示了注意力干预与任务表征粒度之间的深层耦合。

】

---

【Token-Level Inference-Time Alignment for Vision-Language Models ｜令牌级推理时对齐

研究机构：浙江大学、中山大学

作者：Kejia Chen、Jiawen Zhang、Jiacong Hu 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.21794)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.21794)

> 大视觉语言模型（LVLMs）在生成描述时，常因语言先验压制视觉信号而产生对象幻觉，这一可靠性危机在2023年随开源模型爆发而凸显。现有推理时干预策略多依赖序列级奖励模型，反馈延迟高且计算开销大，难以在解码初期抑制幻觉。本文提出TITA（Token-Level Inference-Time Alignment），通过训练轻量级自回归奖励模型，在解码阶段以令牌级对数概率比提供密集引导。该方法在POPE基准上超越SOTA，但在CHAIRs指标上显著落后，其细粒度生成抑制能力存疑。

】

---

【Towards Mitigating Hallucinations in Large Vision-Language Models by Refining Textual Embeddings ｜视觉对齐嵌入

作者：Aakriti Agrawal、Gouthaman KV、Rohith Aralikatti 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.05017)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.05017)

> 大视觉语言模型（LVLMs）在生成描述时，常因语言先验压制视觉信号而产生对象幻觉，这一可靠性危机在2023年随开源模型爆发而凸显。早期研究聚焦数据对齐与指令微调，试图从源头纠正偏差，但受限于标注成本与泛化瓶颈，效果有限。本文指出主流架构中视觉嵌入仅作为附加项拼接至文本序列，导致LLM骨干在自注意力中系统性偏向文本，提出在训练阶段将平均池化的视觉特征融合进每个文本嵌入，以重构模态间的注意力平衡。该方法在Video-LLaVA上实现了显著的幻觉抑制，但其依赖重新训练的范式与当前主流的推理时干预路线存在根本性差异，且缺乏与SOTA解码策略的横向对比，其泛化边界尚待厘清。

】

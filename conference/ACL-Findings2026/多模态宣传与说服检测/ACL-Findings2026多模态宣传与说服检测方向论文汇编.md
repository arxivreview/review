# ACL-Findings2026 · 多模态宣传与说服检测方向论文汇编

> 本方向共 3 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Do Not Guess, Verify: Logic-Guided Adaptive Reasoning for Multimodal Misinformation Detection ｜逻辑引导自适应推理

作者：Kun Huang、Rui Qiu、Xiaoming Li 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_10185d042b45)

> 导读 多模态虚假信息检测的核心难点在于区分真实图像配虚假文本的混合来源错误，传统特征对齐方法难以捕捉语义层面的矛盾。现有基于多模态大语言模型（MLLMs）的方案虽引入世界知识，但易受无关社会线索干扰产生认知偏差，且固定深度的图推理导致简单与复杂案例计算资源分配不均。LoGAR通过VLM生成显式验证理由作为全局语义锚点，条件化多模态融合与图消息传递，并引入自适应深度控制机制。该框架在精度与效率间取得平衡，但其性能增益是否完全归因于逻辑引导机制而非骨干网络能力，仍需进一步验证。

】

---

【Fine-tuning with Hierarchical Prompting for Robust Propaganda Classification Across Annotation Schemas ｜意图导向宣传分类与分层提示鲁棒性

研究机构：德国柏林工业大学、德国人工智能研究中心

作者：Lukas Stähelin、Veronika Solopova、Max Upravitelev 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_4f43d6bc7476)

> 短文本宣传检测面临标注主观性强与模型对表面词汇过度敏感的困境，现有基于修辞技巧的分类体系因标注者分歧大导致模型学习信号噪声高。本文切入点在于将分类目标从“使用了什么修辞手法”转向“试图达成什么沟通意图”，并验证分层提示策略在低标注一致性条件下的鲁棒性。通过构建意图导向的新分类体系并对比微调前后的分层推理效果，证明了微调是激活层级结构收益的必要条件。该工作揭示了标注可靠性与提示策略的交互效应，但其新体系较低的标注一致性是否真正优于传统体系，仍取决于具体应用场景对解释深度的需求。

】

---

【Probing Multimodal Large Language Models on Cognitive Biases in Chinese Short-Video Misinformation ｜短视频谣言检测中的认知偏差诊断

研究机构：美国约翰斯·霍普金斯大学、香港中文大学

作者：Jen-tse Huang、Chang Chen、Shiyang Lai 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.06600)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ad54e29d1a2b)

> 短视频谣言检测旨在从视听混合内容中识别逻辑谬误与虚假声明，但现有基准多依赖外部事实核查，难以评估模型对内部逻辑链的推理能力。当前多模态大语言模型（MLLMs）虽具备基础推理能力，却在真实社交噪声下表现出系统性判断偏差，且缺乏针对认知偏差的量化评估框架。本文通过构建200条人工标注的短视频数据集，引入心理学控制变量，系统诊断了8个前沿MLLMs在权威ID与流行度指标下的行为失效。该工作提供了诊断MLLMs认知脆弱性的新视角，但其评测规模与指标设计限制了向实际部署场景的直接迁移。

】

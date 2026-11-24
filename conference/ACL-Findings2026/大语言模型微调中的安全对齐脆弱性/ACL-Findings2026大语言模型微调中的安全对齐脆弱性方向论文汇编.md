# ACL-Findings2026 · 大语言模型微调中的安全对齐脆弱性方向论文汇编

> 本方向共 6 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Continual Safety Alignment via Gradient-Based Sample Selection ｜基于梯度幅值的持续安全对齐样本选择

研究机构：澳大利亚迪肯大学

作者：Thong Bach、Dung Nguyen、Thao Minh Le 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17215)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17215)

> 持续微调中，模型需在适应新任务的同时保持安全对齐，但现有参数正则化或架构约束方法无法识别具体哪些样本导致对齐漂移。本文从数据层面切入，发现高梯度样本是激活“弹性回弹”、破坏安全边界的关键因素。通过筛选中梯度样本进行微调，该方法在无需额外安全数据或架构修改的前提下，显著降低了攻击成功率并维持了任务效用。其价值在于提供了低成本的训练时干预手段，但梯度幅值作为代理指标是否足以捕捉复杂的安全漂移机制，仍存疑。

】

---

【Preserving Fairness and Safety in Quantized LLMs Through Critical Weight Protection ｜关键权重保护下的量化公平与安全保持

作者：Muhammad Alif Al Hakim、Alfan Farizki Wicaksono、Fajri Koto

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_b0b0cb9edea0)

> 大语言模型在部署时普遍采用量化压缩以降低显存占用，但精度截断会扰动参数分布，进而破坏模型在公平性与安全性上的对齐表现。现有研究多聚焦于静态量化下的英文场景，对动态量化及多语言环境中的对齐退化缺乏系统评估，且缺乏在量化阶段直接保护对齐敏感参数的机制。本文提出关键权重保护策略，通过敏感度评分识别对公平与安全贡献最大的参数，将其保留在FP16精度，其余参数量化至INT4。该方法在无需重训练的前提下缓解了量化导致的对齐退化，但其保护粒度为权重级别，未触及激活空间或特征子空间，能否应对更深层的对齐结构漂移仍存疑。

】

---

【Preventing Safety Drift in Large Language Models via Coupled Weight and Activation Constraints ｜耦合权重与激活约束防止大语言模型安全漂移

研究机构：中国科学院、国防科技大学

作者：Songping Peng、Zhiheng Zhang、Daojian Zeng 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.12384)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.12384)

> 微调过程常因少量良性数据导致模型拒绝有害请求的能力崩塌，现有防御方案多局限于权重或激活单级干预，无法阻断二者耦合产生的绕过路径。本文提出CWAC，通过同时施加权重子空间投影与稀疏自编码器特征正则化，在训练阶段闭合安全漂移通道。该方法在四个主流开源模型上显著降低了有害分数，但其依赖白盒访问且未验证对黑盒API模型的适用性。

】

---

【The Art of (Mis)alignment: How Fine-Tuning Methods Effectively Misalign and Realign LLMs in Post-Training ｜微调方法在安全失配与再对齐中的效能不对称性

研究机构：电子科技大学、新加坡南洋理工大学

作者：Rui Zhang、Hongwei Li、Yun Shen 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f63cc988fb14)

> 大语言模型（LLM）的安全对齐机制在微调过程中极易被破坏，但不同微调范式在“破坏安全”与“恢复安全”上的效能差异缺乏系统性量化。现有研究多聚焦于单一方向的攻击或防御，忽略了攻防博弈中方法选择的非对称性及其对模型效用的累积影响。本文通过对比四种监督微调（SFT）与两种偏好微调（PFT）方法在失配与再对齐双向任务中的表现，揭示了ORPO在失配上的优势与DPO在再对齐上的效用代价。该研究为防御者选择再对齐策略提供了实证依据，但其结论受限于特定模型规模与数据集规模，未深入探究几何机理。

】

---

【To Intervene or Not: Guiding Inference-time Alignment with Probabilistic Model Blending ｜推理时对齐中的质量盲视与分布混合

研究机构：新加坡南洋理工大学

作者：Jin Gan、Xin Li、Jun Luo

论文原文见 [arXiv](https://arxiv.org/abs/2606.11201)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.11201)

> 推理时对齐旨在通过已对齐模型在生成阶段指导未对齐模型，以规避高昂的重训练成本。现有方法如NUDGING隐含假设所有指导信号均有益，但系统评估显示指导有效性在不同模型组合间剧烈波动，且高干预率反而导致性能下降。本文提出BlendIn，通过基于置信度的概率分布混合替代二元接受/拒绝决策，实现质量感知的软集成。该方法在挑战性模型对上实现了最高50%的性能提升，但其改进幅度在完整测试集上未达统计显著性，且依赖基座模型与指导模型的能力匹配度。

】

---

【Towards Identification and Intervention of Safety-Critical Parameters in Large Language Models ｜预期安全影响（ESI）：基于参数敏感度解耦安全与效用的干预框架

作者：Weiwei Qi、Zefeng Wu、Tianhang Zheng 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_bebdba993896)

> 导读 大语言模型在微调后常出现安全对齐崩塌，但现有方法难以精确定位哪些参数承载安全行为，导致防御策略要么全局冻结损失效用，要么盲目更新破坏安全。本文切入点在于构建一个可微分的参数级安全敏感度度量，将安全关键参数从全参数空间中分离出来。通过引入预期安全影响（Expected Safety Impact, ESI）指标，结合可微分裁判模型估计安全梯度，并据此实施仅更新或仅冻结关键参数的干预策略。该框架在参数定位精度上优于传统剪枝指标，但在效用保持上仍受限于冻结比例，其泛化边界尚待验证。

】

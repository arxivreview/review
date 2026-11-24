# ACL-Findings2026 · 语言模型的知识蒸馏方向论文汇编

> 本方向共 2 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Calibrated Progressive Distillation: Co-Designing Curriculum and Target Mixing for Knowledge Distillation of Large Language Models ｜校准渐进式蒸馏：协同设计课程与目标混合的LLM知识蒸馏框架

作者：Mengxiang Zhang、Lingyuan Liu

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8d546cf53b10)

> 大语言模型知识蒸馏旨在将大型教师模型的参数化知识迁移至小型学生模型，以缓解高并发部署中的推理延迟与内存瓶颈。现有方法通常独立设计课程学习（数据排序）与目标混合（监督信号），导致训练难度轨迹与监督强度失配，引发模式坍塌或学习停滞。本文提出校准渐进式蒸馏（Calibrated Progressive Distillation, CPD），通过统一的难度画像同步调度训练子集与混合系数，实现监督信号与学生能力的动态对齐。该框架在指令跟随、数学推理与代码生成任务上均优于强基线，但其依赖静态难度画像的假设在长序列生成场景下的有效性尚存疑。

】

---

【Fast and Effective On-policy Distillation from Reasoning Prefixes ｜前缀在线策略蒸馏

作者：Dongxu Zhang、Zhichao Yang、Sepehr Janghorbani 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.15260)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.15260)

> 在线策略蒸馏（On-Policy Distillation, OPD）旨在通过学生模型自生成轨迹上的教师反馈消除训练-推理分布失配，但其全量采样机制在长链推理任务中导致计算成本呈线性增长，成为部署瓶颈。现有方法要么依赖离线序列匹配而遗留曝光偏差，要么执行全量在线采样而陷入算力陷阱，本文切入点在于验证“仅监督轨迹前缀”是否足以保留 OPD 的核心收益。通过截断学生 rollout 并仅对前 $L$ 个 token 计算反向 KL 散度，配合线性前缀调度策略，该方法在保持接近全量 OPD 性能的同时，将训练 FLOP 降低 2 至 47 倍。这一工程化改进有效缓解了长序列蒸馏的效率瓶颈，但其对小型模型尾部泛化能力的潜在损害及调度策略的静态性，仍构成应用边界。

】

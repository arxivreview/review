# ACL-Findings2026 · 推理知识蒸馏方向论文汇编

> 本方向共 8 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Cognitive-Uncertainty Guided Knowledge Distillation for Accurate Classification of Student Misconceptions ｜认知不确定性引导的知识蒸馏框架

研究机构：华南理工大学、香港科技大学

作者：Qirui Liu、Hao Chen、Weijie Shi 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.14752)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.14752)

> 教育场景下的学生错误诊断面临真实数据稀缺、标签噪声高及大模型认知偏差三重困境，传统合成数据扩充因分布差距失效，而直接微调小模型又易过拟合噪声。本文切入点在于摒弃数据生成，转而挖掘现有真实数据中的高价值样本，通过两阶段蒸馏与自适应损失实现精准分类。该框架在仅使用10.30%筛选样本的情况下，使4B参数学生模型在MAP-Charting数据集上达到0.9585的MAP@3，超越72B教师模型，但其有效性高度依赖特定教育分类任务的标签结构，泛化至生成式推理场景的潜力存疑。

】

---

【Distilling Long-CoT Reasoning through Collaborative Step-wise Multi-Teacher Decoding ｜协同推理解码

研究机构：韩国科学技术院

作者：Taewon Yun、Jisu Shin、Jeonghwan Choi 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.02290)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.02290)

> 多教师推理蒸馏旨在将大型推理模型（LRM）的长思维链（Long-CoT）能力迁移至小模型，但现有“生成-选择”范式因事后评估无法动态利用异构教师的互补性，导致计算浪费与推理路径单一。CoRD 将蒸馏重构为步级协同解码过程，通过预测困惑度评分与束搜索，让多个教师在解码过程中逐步提议并融合推理步骤。该方法在 AIME25 上使 32B 学生模型超越所有单一教师，但步级分割对长程依赖的破坏及与在线策略蒸馏的兼容性仍存疑。

】

---

【Distilling the Essence: Efficient Reasoning Distillation via Sequence Truncation ｜序列截断下的推理蒸馏效率优化

研究机构：加拿大不列颠哥伦比亚大学

作者：Wei-Rui Chen、Vignesh Kothapalli、Ata Fatahibaarzi 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.21002)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.21002)

> 推理知识蒸馏旨在将大型推理模型的逻辑能力迁移至小模型，但长思维链（Long-CoT）带来的训练计算开销成为部署瓶颈。现有离线蒸馏方法默认使用全序列监督，忽视了序列内部信号分布的不均匀性，导致大量算力浪费在冗余token上。本文提出LeadSpan Proportion (LSP) 动态截断协议，通过仅保留训练序列前50%的token，在数学基准上保留了约91%的准确率，同时将训练时间与显存占用降低约50%。这一发现挑战了“全序列监督最优”的默认假设，但其结论是否适用于非数学领域及跨模型家族蒸馏，仍存疑。

】

---

【DRP: Distilled Reasoning Pruning with Mathematical Skill-aware Step Decomposition for Efficient Large Reasoning Models ｜蒸馏推理剪枝

研究机构：美国亚利桑那州立大学

作者：Yuxuan Jiang、Dawei Li、Francis Ferraro

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_7028d81ceed0)

> 长思维链（Long-CoT）学生模型常生成冗余轨迹，而短思维链（Short-CoT）教师模型直接蒸馏其简洁答案会导致风格不匹配与可学习性差距。现有压缩方法或依赖提示约束、或采用强化学习惩罚长输出，往往在分布外任务上牺牲准确率。DRP 提出“轨迹感知”离线蒸馏：让学生先生成冗长轨迹，由教师进行技能感知步骤分解与剪枝，再将修剪后的轨迹回传给学生进行监督微调。该方法在 GSM8K 上将 Token 消耗降低 64% 同时提升准确率，但 AIME24 准确率未提升，暗示剪枝策略在极高难度任务上的边界尚不明确。

】

---

【Pru-CoT: Towards Efficient Reasoning Distillation via Pruning Chain-of-Thought ｜剪枝思维链以优化推理蒸馏

研究机构：大连理工大学

作者：Han Liu、Shuotian Ma、Hui Li 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e90fdf0261e7)

> 推理知识蒸馏面临的核心困境是教师模型生成的冗长思维链（Chain-of-Thought, CoT）中充斥冗余步骤，导致学生模型过拟合表面语法而非内化核心因果逻辑。现有剪枝方法要么受限于局部启发式规则无法捕捉全局依赖，要么因全局搜索带来不可接受的计算开销。Pru-CoT 通过冻结模型上的可学习权重量化步骤级因果贡献，结合大语言模型（Large Language Model, LLM）引导的保真剪枝，在保留逻辑完整性的同时压缩轨迹。该方法在 DeepSeek-R1-Distill-Qwen-7B 上实现了平均准确率 2.4% 的提升，但其对剪枝代理规模匹配的依赖及未探索的超参数空间限制了其通用性验证。

】

---

【SmartAD: Capacity-Aligned Agent Distillation for Small Language Models ｜容量对齐的智能体蒸馏

研究机构：华中科技大学

作者：Guokai Tang、Feng Zhao

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d5c0433e35c9)

> 智能体蒸馏旨在将大型语言模型（LLM）的工具调用与多步交互能力迁移至小语言模型（SLM），但现有方法常忽视教师轨迹与学生容量间的结构性错配，导致训练不稳定或泛化受限。本文切入点在于识别并过滤那些学生当前无法有效吸收的“高难度”轨迹，并差异化加权关键决策段。SmartAD 通过基于负对数似然（NLL）的轨迹筛选与分段加权损失，实现了数据分布与监督信号的双重对齐。该框架在1.5B和3B模型上验证了有效性，但其离线筛选机制能否替代在线策略蒸馏以彻底解决长程推理中的分布偏移，仍存疑。

】

---

【TRM-Planner: Offline Target Planning and Distillation for Tiny Recursive Models ｜离线目标规划与蒸馏

作者：Euijin Baek、Housam Babiker、Mi-Young Kim 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1f624a71a529)

> 网格推理任务中的Tiny Recursive Models (TRMs)面临监督信号对精化深度与停止策略校准的敏感性问题，导致训练效率低下且性能不稳定。现有方法依赖在线停止决策，难以在固定计算预算下获取高质量中间状态。本文提出TRM-Planner，通过离线规划冻结教师轨迹并缓存高置信度目标，实现“一次计算，多次复用”的蒸馏范式。该方法在ARC-AGI-1/2上显著提升了小模型性能，但其离线缓存机制是否完全规避了分布偏移风险，仍需进一步验证。

】

---

【Why Can Distillation Work with Limited Resources? A Systematic Study ｜低资源蒸馏的认知行为迁移机制

研究机构：清华大学、上海交通大学

作者：Xiao Hu、Xingyu Lu、Liyuan Mao 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_6689b8ebc0ce)

> 推理知识蒸馏旨在将大型模型的复杂逻辑能力压缩至小模型，但现有方法多聚焦于分布对齐或计算效率，缺乏对“蒸馏究竟传递了什么”的机制解释。本文切入点在于：少量高质量样本的SFT蒸馏为何能超越大规模RL训练？作者通过token频率分析与认知行为量化，揭示了蒸馏传递的是“多视角思考”与“元认知意识”两种高级认知行为，而非表面token模式。这一发现为低资源蒸馏提供了认知层面的解释框架，但其结论是否泛化至非数学任务及更大规模模型，仍存疑。

】

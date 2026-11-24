# ACL-Findings2026 · 高效且理论化的思维链推理方向论文汇编

> 本方向共 10 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Concise Math Reasoning via Difficulty-Aware Distillation ｜难度感知思维链蒸馏

作者：Yifan Wu、Jingze Shi、Bingheng Wu 等 11 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_1ef18c04ecf5)

> 思维链（Chain-of-Thought, CoT）蒸馏旨在将大模型的推理能力迁移至小模型，但现有数据普遍冗长，导致学生模型在所有难度问题上均表现出“过度思考”的刚性模式。本文指出，数据冗余不仅增加训练成本，更阻碍了模型根据问题难度自适应调整推理深度的能力。通过引入难度感知重写机制，DAD 在数据生成阶段将长 CoT 压缩为仅保留关键逻辑步骤的短轨迹，构建了平均长度仅 720 tokens 的 LiteCoT 数据集。该方法以 100K 样本量超越了 800K 长 CoT 样本的训练效果，验证了数据简洁性对推理效率与准确率的决定性作用，但其对极限难度任务的泛化边界尚待进一步厘清。

】

---

【CRISP: Compressing Redundancy in Chain-of-Thought via Intrinsic Saliency Pruning ｜基于内在注意力显著性的思维链压缩

研究机构：南京大学

作者：Yangsong Lan、Hongliang Dai、Piji Li

论文原文见 [arXiv](https://arxiv.org/abs/2604.17297)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_3fbdc2b93b50)

> 长思维链（Chain-of-Thought, CoT）推理在提升大语言模型复杂任务准确率的同时，引入了高昂的计算开销与延迟，核心矛盾在于如何在不损失逻辑完整性的前提下剔除冗余步骤。现有压缩方法多依赖外部代理模型评估步骤重要性，导致压缩逻辑与源模型内在推理动态脱节，常误删关键自纠正步骤。本文切入点在于发现 `</think>` 标记符的注意力分布可作为内在显著性信号，据此设计基于原子算子贪心搜索的压缩框架。该方法在7B模型上实现58%的Token缩减且准确率反超基线，但其在极高难度竞赛题上的泛化能力及贪心搜索的全局最优性仍存疑。

】

---

【DiffCoT: Diffusion-styled Chain-of-Thought Reasoning in LLMs ｜扩散式思维链推理

研究机构：香港浸会大学、哈尔滨工业大学

作者：Shidong Cao、Hongzhan Lin、Yuxuan Gu 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_80fead884c59)

> 导读 思维链（Chain-of-Thought, CoT）推理在提升大语言模型数学解题能力的同时，因自回归解码的不可逆性导致早期错误沿链条累积，严重削弱推理鲁棒性。现有偏好优化方法仅做局部步级对齐，无法在推理时回溯修正已生成的错误前缀，暴露偏差问题依然突出。本文提出 DIFFCOT，将 CoT 重构为步级迭代去噪过程，通过滑动窗口与因果噪声调度统一生成与修正。该方法在 GSM8K 和 MATH 高难度子集上显著优于现有偏好优化基线，但其性能增益高度依赖骨干模型能力，且未解决离散 Token 表达瓶颈这一根本限制。

】

---

【Don’t Tell the Answer, Truly Guide the Reasoning During RL Rollouts ｜基于元提示与亲和性感知的强化学习推理框架

作者：Xinyi Wang、Jinyi Han、Zishang Jiang 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_459557586f62)

> 强化学习在提升大语言模型长思维链推理能力时，常因任务难度超出模型容量导致奖励稀疏，使策略更新失效。现有缓解手段多依赖注入部分答案，引发分布失配与训练不稳定。本文提出HINT框架，通过提供抽象元提示引导模型自主探索，并引入亲和性感知策略优化动态门控梯度。该方法在多个基准上验证了训练稳定性与泛化优势，但其对教师模型生成元提示的依赖及特定指标协议下的绝对性能上限仍存疑。

】

---

【Graph-Based Chain-of-Thought Pruning for Reducing Redundant Reflections in Reasoning LLMs ｜基于图结构的思维链反思冗余剪枝

研究机构：中南大学

作者：Hongyuan Yuan、Xinran He、Run Shao 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_18621ef42b84)

> 长思维链推理中，模型常陷入无差别检查与重复验证的“过度思考”陷阱，导致计算资源浪费。现有压缩方法多依赖全局长度惩罚或Token级重要性评分，难以精准定位语义层面的反思冗余。本文切入点在于将线性思维链重构为有向无环图，利用拓扑属性识别并剪除低效反思节点。通过三阶段训练管线内化该剪枝策略，在保持准确率的同时显著降低推理长度。该方法在结构建模上具有创新性，但离线图构建成本与标签粗粒度限制了其通用性。

】

---

【Neural Chain-of-Thought Search: Searching the Optimal Reasoning Path to Enhance Large Language Models ｜神经思维链搜索

研究机构：中山大学

作者：Guoming Ling、Zhongzhan Huang、Yupei Lin 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_29a74a5d98d7)

> 现有大语言模型在生成思维链时缺乏全局规划，常陷入冗余验证或低效分支，导致计算资源浪费。静态长度惩罚或后处理剪枝无法在生成过程中动态识别并规避这些次优路径。本文提出神经思维链搜索框架，将推理重构为对“思考算子”的动态前瞻搜索，通过双因子启发式函数同时评估正确率与效率。该方法在多个基准上实现了准确率与生成长度的帕累托改进，但其依赖小算子空间假设，且在复杂知识密集型任务上的增益显著衰减，暴露了搜索机制对任务类型的敏感性。

】

---

【SpiralThinker: Latent Reasoning through an Iterative Process with Text–Latent Interleaving ｜螺旋思考者

研究机构：韩国延世大学

作者：Shengmin Piao、Sanghyun Park

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_576cf90338a7)

> 潜在推理领域长期受困于隐空间动态不连贯与显隐式推理割裂，导致模型在连续表示中难以维持稳定的推理轨迹。现有方法多将潜在表示视为单次前向传播的静态输入，缺乏对推理过程逐步演化的建模机制。本文提出SpiralThinker，通过迭代更新隐状态并引入渐进对齐目标，实现文本与潜在推理的结构化交替。该框架在潜在推理基准上取得SOTA，但绝对准确率仍显著低于显式方法，且未验证跨模型规模的泛化能力。

】

---

【SyncThink: A Training-Free Strategy to Align Inference Termination with Reasoning Saturation ｜同步思维：基于内部信号对齐推理终止与饱和

研究机构：北京大学

作者：Gengyang Li、Wang Cai、Yifeng Gao 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_a54ceb48fc48)

> 长思维链（Chain-of-Thought, CoT）推理在提升大语言模型（LLM）准确率的同时，引入了显著的推理延迟与计算开销，核心矛盾在于推理深度与计算效率之间的张力。现有方案多依赖训练式压缩或黑盒一致性检查，前者牺牲部署灵活性，后者引入额外推理成本且未利用模型内部动态。本文切入点在于发现模型存在“认知滞后”（Cognitive Lag），即准确率饱和早于自然终止点，并利用边界 Token 的 Logit 动态作为免训练停止信号。通过监控 `</think>` 的秩与熵，SyncThink 实现了动态截断，在保持精度的同时大幅降低 Token 消耗。其价值在于提供了无需微调的高效推理路径，但该方法对显式边界 Token 的依赖限制了其在通用模型上的泛化性。

】

---

【ThinkBrake: Efficient Reasoning via Log-Probability Margin Guided Decoding ｜基于对数概率边际的推理终止机制

研究机构：韩国首尔大学

作者：Sangjun Song、Minjae Oh、Seungkyu Lee 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_5d9847085443)

> 大语言模型在复杂推理中常出现“过度思考”，即在得出正确中间步骤后继续生成并覆盖为错误答案，导致计算资源浪费与精度下降。现有测试时干预方法多依赖手工启发式规则，缺乏理论支撑且在不同难度任务上表现不稳定。本文提出 THINKBRAKE，通过监测句子边界处继续生成 Token 与结束标记 `</think>` 的对数概率边际，实现无需训练的自适应推理终止。该方法在数学与工具调用任务上实现了精度保持与 Token 消耗降低的平衡，但其对高难度任务精度的轻微损失归因于“虚假推理”而非过早终止，这一现象的内在机制尚待深入解析。

】

---

【When Internalization Fails: Finding Better Targets for Reasoning Compression ｜推理轨迹压缩中的蒸馏目标选择：Post-think 优于通用摘要

研究机构：美国芝加哥大学

作者：Mourad Heddaya、Manley Roberts、Rohan Wadhawan 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_7d018c4acb30)

> 推理模型通过生成长思维链提升复杂任务准确率，但数千 Token 的解码过程带来高昂延迟与成本，且存在“过度思考”导致的性能反降。现有课程学习式内化方法在短结构化任务上有效，但在长探索性竞赛数学上失效，直接截断又因模型补偿性生成长尾文本而虚高 Token 预算。本文切入点在于发现教师模型在 `

】

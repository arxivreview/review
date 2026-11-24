# ICLR2026 · 高效LLM解码与推测解码方向论文汇编

> 本方向共 15 篇（ICLR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【AdaBlock-dLLM: Semantic-Aware Diffusion LLM Inference via Adaptive Block Size ｜语义感知自适应块解码

研究机构：英国帝国理工学院、日本东京科学大学

作者：Guanxi Lu、Hao Mark Chen、Yuto Karashima 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.26432)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.26432)

> 扩散语言模型（dLLMs）在半自回归解码中面临固定块大小导致的效率与精度双重损失，现有方法通过置信度阈值控制采样但忽略了块边界与语义结构的错位。本文切入点在于识别解码过程中的“波动带”（Volatility Band, VB），利用语义分隔符的置信度动态调整块大小，实现免训练的即插即用优化。该方法在保持吞吐量不变的前提下提升了生成质量，但其效果高度依赖模型内部置信度分布的稳定性，对从自回归模型适配而来的dLLMs增益有限。

】

---

【Beyond Scattered Acceptance: Fast and Coherent Inference for DLMs via Longest Stable Prefixes ｜最长稳定前缀（LSP）调度器：基于单体前缀吸收的扩散语言模型推理加速

研究机构：阿里巴巴集团、清华大学

作者：Pengxiang Li、Joey Tsai、Hongwei Xue 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.05454)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.05454)

> 扩散语言模型（Diffusion Language Models, dLLMs）旨在通过迭代去噪打破自回归生成的顺序依赖，但实际推理速度常受限于低效的令牌提交策略。现有散点接受方法导致键值缓存（Key-Value Cache, KV Cache）碎片化与收敛缓慢，本文提出最长稳定前缀（Longest Stable Prefix, LSP）调度器，通过原子化提交连续稳定前缀实现几何级活跃后缀衰减。该方法在LLaDA-8B上实现最高3.4倍加速，但仅对比全步长基线，缺乏与SOTA并行解码方法的直接性能参照。

】

---

【DIFFUSION LANGUAGE MODELS KNOW THE ANSWER BEFORE DECODING ｜扩散语言模型早期答案收敛与动态停止解码

研究机构：香港理工大学、美国达特茅斯学院

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_72404407)

> 扩散语言模型（Diffusion Language Models, DLMs）虽具备并行解码潜力，但受限于双向注意力开销及为保质量所需的长迭代步数，实际推理速度仍落后于自回归模型。现有加速方法多聚焦于降低单步计算成本或压缩模型规模，却忽视了去噪轨迹中答案提前稳定这一冗余现象。本文提出免训练策略 Prophet，通过监控答案区域的置信度间隙动态决定何时一次性提交所有剩余令牌。该方法在保持生成质量的前提下实现了最高 3.4 倍的步数压缩，但其加速收益高度依赖任务中存在可识别的明确答案区域，对开放式生成的适用性存疑。

】

---

【Dynamic-dLLM: Dynamic Cache-Budget and Adaptive Parallel Decoding for Training-Free Acceleration of Diffusion LLM ｜动态缓存预算与自适应并行解码加速扩散大语言模型

研究机构：哈尔滨工业大学

作者：Tianyi Wu、Xiaoxi Sun、Yanhua Jiao 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.26120)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.26120)

> 扩散大语言模型（dLLMs）因双向注意力机制在文本生成中表现优异，但其非自回归特性导致计算复杂度随序列长度呈立方级增长，且无法复用键值缓存（KV Cache），成为实时推理的瓶颈。现有加速方法采用静态缓存策略或固定置信度阈值，忽略了令牌在层间和步间动态变化的特性，导致效率与质量难以兼顾。本文提出免训练框架 Dynamic-dLLM，通过动态缓存更新（DCU）自适应分配层间缓存预算，并结合自适应并行解码（APD）动态校准解码阈值，在保持生成质量的前提下实现最高 4.48 倍加速。该方法在 LLaDA 和 Dream 系列模型上验证了有效性，但其对长序列极端场景下的稳定性及多模态泛化能力尚存疑。

】

---

【ES-dLLM: Efficient Inference for Diffusion Large Language Models by Early-Skipping ｜扩散大语言模型推理加速：基于早期跳过的冗余计算消除

研究机构：清华大学

作者：Zijian Zhu、Fei Ren、Zhanhong Tan 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.10088)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.10088)

> 扩散大语言模型（dLLMs）通过迭代去噪实现并行生成，但每步处理全序列导致计算冗余，现有缓存方法仅优化块级KV复用，未解决块内令牌级的无效计算。本文发现迭代间中间张量与置信度变化微小，据此提出免训练的早期跳过框架，在浅层截断低重要性令牌以削减FLOPs。该方法在LLaDA-8B上实现16.8倍加速且质量无损，但固定跳过比率与单一变化指标限制了其自适应潜力，能否动态调整跳过策略以平衡不同任务难度仍存疑。

】

---

【FAST DLLM V2: EFFICIENT BLOCK-DIFFUSION LLM ｜块扩散语言模型的高效适配与层级缓存加速

研究机构：美国麻省理工学院

作者：Chengyue Wu、Hao Zhang、Shuchen Xue 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_87121258)

> 自回归大语言模型（AR LLM）推理受限于严格的左到右顺序依赖，导致内存带宽受限且延迟随生成长度线性增加。全注意力扩散语言模型（dLLM）虽支持并行解码，但无法有效利用键值缓存（KV Cache），且训练成本高达数百亿令牌。本文提出 Fast-dLLM v2，通过块扩散架构与互补掩码训练策略，仅需约 10 亿令牌微调即可将预训练 AR 模型无损适配为 dLLM，并引入层级缓存机制实现 2.5 倍加速。该方法在保持生成质量的前提下显著降低了扩散模型的部署门槛，但其加速比在绝对值上仍低于部分基于推测解码的 AR 加速方案。

】

---

【Gumbel Distillation for Parallel Text Generation ｜Gumbel 蒸馏并行文本生成

研究机构：美国德克萨斯大学奥斯汀分校

作者：Chi Zhang、Xixi Hu、Bo Liu 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.22216)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.22216)

> 并行解码器因假设令牌间条件独立而丢失局部依赖，导致生成质量显著低于自回归模型。现有蒸馏方法仅匹配输出分布，无法捕捉教师模型的采样轨迹信息。本文提出 Gumbel 蒸馏，利用 Gumbel-Max 技巧将教师的随机采样过程转化为确定性的噪声-文本映射，使并行学生模型通过监督学习重建该映射。该方法在 LM1B 和 OpenWebText 上将 MDLM 的 MAUVE 分数提升 30.0%，但缺乏下游任务准确率验证，其质量增益能否转化为逻辑推理能力仍存疑。

】

---

【HIERARCHY DECODING: A TRAINING FREE PARAL LEL DECODING STRATEGY FOR DIFFUSION LARGE LANGUAGE MODELS ｜层级并行解码：基于分治原理的扩散大语言模型加速策略

研究机构：清华大学、华东师范大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_99019673)

> 扩散大语言模型（dLLMs）旨在通过双向注意力打破自回归生成的顺序依赖，但激进并行会导致严重的分布漂移，使得现有开源模型效率不及自回归模型。现有基于置信度的解码策略忽略了未解码令牌的空间分布对预测稳定性的影响，导致连续掩码下的预测误差累积。本文提出 Hierarchy-dLLM，通过递归分治将掩码序列划分为稀疏子区域，利用已解码令牌作为锚点隔离依赖，在免训练条件下实现无损加速。该方法在 GSM8K 上实现了 17 倍于原生解码的加速比，且准确率持平或略升，但其在长序列下的子区域上下文隔离效应及与更复杂调度策略的对比仍存疑。

】

---

【LEARNING TO PARALLEL: ACCELERATING DIFFUSION - LARGE LANGUAGE MODELS VIA LEARNABLE PARAL LEL DECODING ｜学习式并行解码加速扩散大语言模型

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_75388460)

> 扩散大语言模型（dLLMs）通过迭代去噪实现并行生成，但现有加速策略依赖静态置信度阈值，导致大量已正确预测的令牌被反复重掩码，造成计算冗余。本文指出这种“一刀切”的静态规则无法适应不同输入的特异性，提出训练轻量级过滤器动态预测令牌稳定性。通过引入学习式并行解码策略与文本结束预测机制，在保持准确率无损的前提下实现数量级加速。该方法验证了动态决策优于静态启发式的假设，但其泛化能力受限于单一骨干模型与特定任务分布。

】

---

【LESS SAMPLING: A ROBUST HYPERPARAMETER _p_ FREE APPROACH FOR LLM DECODING ｜无超参数采样解码

研究机构：新加坡国立大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_80095365)

> 大语言模型（LLM）解码依赖截断策略平衡生成多样性与连贯性，但现有方法如 top-p 和 min-p 需手动调节超参数，且在高温度下易导致文本退化。本文提出 p-less 采样，利用信息论中的碰撞熵动态计算截断阈值，消除对任务特定超参数的依赖。该方法在数学推理与创意写作任务中，于高温设置下保持了优于基线的准确率与稳定性。其价值在于提供了无超参数的鲁棒解码方案，但在绝对准确率上未超越针对特定任务优化的并行解码方法，且缺乏与系统级加速机制的整合验证。

】

---

【p-less Sampling: A Robust Hyperparameter-Free Approach for LLM Decoding ｜无超参数采样：基于信息论的LLM解码阈值动态调整

研究机构：新加坡国立大学

作者：Runyan Tan、Shuang Wu、Phillip Howard

论文原文见 [arXiv](https://arxiv.org/abs/2509.23234)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.23234)

> 大语言模型（LLM）解码中的截断采样策略长期受困于超参数对任务与温度的敏感性，导致高温度下文本退化。现有方法如 top-p 或 min-p 依赖固定阈值或单点统计，无法适应分布熵的动态变化。本文提出 p-less 采样，利用分布二阶矩计算动态截断阈值，实现无超参数且温度鲁棒的解码。该方法在数学推理与创意写作任务上显著优于基线，但其理论假设在极端分布形态下的普适性仍存疑。

】

---

【Parallel Token Prediction for Language Models ｜并行令牌预测

研究机构：美国加州大学尔湾分校

作者：Felix Draxler、Justus Will、Farrin Marouf Sofian 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.21323)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.21323)

> 自回归语言模型推理受限于逐令牌生成的顺序依赖，导致延迟随生成长度线性增加。现有投机解码依赖独立草稿模型，多令牌预测方法则因独立预测头导致令牌间依赖建模不足，产生不连贯序列。本文提出并行令牌预测（Parallel Token Prediction, PTP），将采样随机性前置为模型输入，使单次前向传播能联合预测多个相互依赖的令牌。该框架在理论上证明了与自回归模型的表达等价性，但在通用基准上仅实现2.4倍加速，其实际部署价值仍受限于有限模型容量下的序列长度瓶颈。

】

---

【ParallelBench: Understanding the Trade-offs of Parallel Decoding in Diffusion LLMs ｜扩散语言模型并行解码的权衡基准

研究机构：微软研究院、韩国首尔大学

作者：Wonjun Kang、Kevin Galim、Seunghyuk Oh 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.04767)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.04767)

> 扩散语言模型（dLLMs）旨在通过并行解码打破自回归生成的顺序依赖，但其条件独立性假设导致在强令牌依赖任务中质量严重退化。现有研究多聚焦于标准基准上的加速比，忽视了并行解码在真实场景下的质量-速度权衡失效。本文通过信息论分析量化这一退化下界，并构建首个专门评估该权衡的基准 ParallelBench。该工作揭示了现有自适应解码策略的局限性，但未提供能动态感知依赖结构的新型解码算法。

】

---

【The End of Manual Decoding: Towards Truly End-to-End Language Models ｜动态解码超参预测

研究机构：腾讯AI实验室、香港中文大学

作者：Zhichao Wang、Dongyang Ma、Xinting Huang 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.26697)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.26697)

> 大语言模型（LLM）生成质量长期受限于静态解码超参的手动调优，现有方法无法在单序列内动态平衡探索与利用。本文指出静态配置在推理路径初期与最终答案阶段存在根本性随机性需求冲突，提出 AutoDeco 架构，通过轻量级预测头在前向传播中逐令牌动态生成温度与 top-p 值。实验表明该方法在八个基准上匹配了测试集 Oracle 调参上限，并涌现出自然语言指令控制解码行为的能力，但其训练数据单一性限制了跨域泛化的理论边界。

】

---

【WIDE-IN, NARROW-OUT: REVOKABLE DECODING FOR EFFICIENT AND EFFECTIVE DLLMS ｜宽进窄出：可撤销解码

研究机构：上海交通大学

作者：Feng Hong、Geng Yu、Yushi Ye 等 8 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_77053457)

> 扩散语言模型（DLLMs）旨在通过并行去噪打破自回归生成的顺序依赖，但激进并行常导致早期错误固化，引发质量崩塌。现有采样压缩策略仅加速不修正，无法解决标准解码不可逆的根本缺陷。本文提出宽进窄出（Wide-In, Narrow-Out, WINO）算法，通过影子块并行验证并撤销低置信令牌，实现免训练的可撤销解码。该方法在保持高加速比的同时提升了生成质量，但其在长序列收敛稳定性及与最新SOTA的绝对性能差距仍存疑。

】

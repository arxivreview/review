# ACL-Findings2026 · 掩码与扩散语言建模方向论文汇编

> 本方向共 8 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Attention Sinks in Diffusion Language Models ｜扩散语言模型中的动态注意力汇聚

研究机构：意大利罗马第一大学

作者：Maximo Eduardo Rulli、Simone Petruzzi、Edoardo Michielon 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.15731)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.15731)

> 掩码扩散语言模型（Masked Diffusion Language Models, MDLM）通过双向注意力实现并行去噪，但其内部注意力分配机制长期缺乏实证研究。现有针对自回归模型（ARM）的注意力汇聚（Attention Sink）分析假设汇聚点位置固定，这一静态假设在MDLM中失效，导致无法解释其生成鲁棒性来源。本文通过定义累积注意力分数指标，追踪三个开源MDLM在去噪过程中的汇聚点轨迹，揭示其动态迁移特性及掩码鲁棒性。该发现修正了对扩散模型注意力机制的认知，但受限于仅分析7B-8B规模模型，未验证该动态特性在更大规模或长序列下的稳定性。

】

---

【Diffusion with Truncated Blocks: Fast and High-Quality Text Generation using Truncated Block Generation ｜截断块生成

作者：Yuyan Zhou、Weiyu Chen、James Kwok

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_c31a76db69d3)

> 掩码扩散语言模型（Masked Diffusion Language Models, MDLM）在并行解码时面临注意力被大量无信息掩码稀释的困境，导致长序列生成质量下降。现有采样策略要么固定长度造成计算浪费，要么全序列去噪引发注意力分散。本文提出截断块生成（Truncated Block Generation, TBG），通过分块迭代与动态截断保留高信息密度上下文，实现加速与提质。该方法在Dream-7B上显著优于基线，但绝对性能仍落后于当前强化学习对齐后的SOTA，且对序列级噪声模型增益有限。

】

---

【DOS: Dependency-Oriented Sampler for Masked Diffusion Language Models ｜依赖导向采样器

研究机构：香港理工大学

作者：Xueyu Zhou、Yangrong Hu、Jian Huang

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9df150274f96)

> 掩码扩散语言模型（Masked Diffusion Language Models, MDLM）在并行解码中面临边际分布与联合分布的偏差，导致长序列生成质量下降。现有基于Token级不确定性的采样策略忽略了Token间依赖，无法恢复目标联合分布。本文提出依赖导向采样器（DOS），利用Transformer注意力矩阵作为Token间依赖的代理，以训练免费的方式重构解码顺序。该方法在单块解码下显著优于传统采样，但其性能上限仍受限于基础模型能力，未触及强化学习对齐后的性能边界。

】

---

【Improving the Throughput of Diffusion-based Large Language Models via a Training-Free Confidence-Aware Calibration ｜置信度自适应解码加速

研究机构：美国莱斯大学、美国德克萨斯大学奥斯汀分校

作者：Jucheng Shen、Gaurav Sarkar、Yeonju Ro 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.07173)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.07173)

> 掩码扩散语言模型（MDLM）的推理瓶颈在于多步去噪带来的计算开销，而现有并行解码方法依赖静态阈值，无法适应序列内置信度的动态变化。本文指出固定调度导致易块过度细化、难块细化不足，提出基于置信度信号的闭环控制机制。通过动态调整块大小、步长、词汇子集与提交阈值，在不重训模型的前提下实现吞吐量提升。该方法验证了最小化自适应调度的有效性，但其线性插值策略是否足以捕捉复杂推理中的非线性置信度波动，仍存疑。

】

---

【Parallelism and Generation Order in Masked Diffusion Language Models: Limits Today, Potential Tomorrow ｜掩码扩散语言模型的并行度与生成顺序解耦分析

研究机构：浙江大学、上海交通大学

作者：Yangyang Zhong、Yanmei Gu、Zhengqing Zang 等 17 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.15593)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.15593)

> 掩码扩散语言模型（Masked Diffusion Language Models, MDLMs）旨在通过并行去噪突破自回归（AR）模型的串行解码瓶颈，但当前模型是否真正利用了其非单调生成潜力仍不明确。现有研究多聚焦于推理策略调优或依赖硬件相关的吞吐量指标，缺乏对解码轨迹的系统性机制剖析。本文提出平均最终化并行度（Average Finalization Parallelism, AFP）与Kendall’s τ指标，在58个基准上解耦并行强度与生成顺序，揭示了并行因子化导致的质量下界及模型在语义转折点处的自适应解码行为。该工作为理解MDLM的性能边界提供了理论框架，但其提出的Generate-then-Edit范式缺乏实证验证。

】

---

【PURE: Post-hoc Unlocking and REfinement for Discrete Diffusion Decoding ｜掩码扩散语言模型的后处理解锁与精化

作者：Yangryeol Park、Kunhui Lee、Hanback Choi 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_26ba2b1ac909)

> 导读 掩码扩散语言模型（Masked Diffusion Language Models, MDLMs）通过并行去噪加速文本生成，但单调解掩策略导致早期错误一旦固化便无法修正，形成质量瓶颈。现有重掩码方法多在生成过程中干预，难以处理已形成的局部自洽错误结构。本文提出PURE，一种免训练的后处理采样策略，通过不稳定性评分定位错误区域，结合确定性窗口掩码与随机左侧松弛打破上下文锁定。该方法在GSM8K上带来12.9分提升，但仅验证于256 token短序列，长文本下的有效性存疑。

】

---

【RACC: Regret-Aware Confidence Calibration for Consistent Masked Discrete Diffusion Decoding ｜后悔感知置信度校准

作者：Qinglin Zeng、Jusheng Zhang、Jing Yang 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_19c41ddc744b)

> 掩码离散扩散模型（Masked Discrete Diffusion Models, MDMs）在并行生成中面临“决策失配”：架构具备双向全局感知能力，但主流解码策略仅依赖当前步瞬时概率，忽略了置信度随去噪进程演化的时间信号，导致早期错误固化且无法自校正。现有方案如重掩码（Re-MDM）和前瞻搜索（LookUM）虽能缓解冲突，却分别以高计算开销和冗余前向传播为代价，未能激活模型内在的自校正潜力。RACC 提出一种零额外推理开销的闭环反馈机制，通过追踪置信度轨迹并施加动态惩罚，将开环采样转化为时间感知的全局轨迹优化。该方法在代码与逻辑推理任务上显著提升了生成一致性，但其效果是否依赖于特定骨干的预训练质量，以及能否突破纯解码优化的性能天花板，仍存疑。

】

---

【Revealing the Attention Floating Mechanism in Masked Diffusion Models ｜掩码扩散模型中的注意力漂浮机制

研究机构：美国东北大学、清华大学

作者：Xin Dai、Pengcheng Huang、Zhenghao Liu 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.07894)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.07894)

> 掩码扩散模型（Masked Diffusion Models, MDMs）在双向注意力下如何分配信息流，是解释其上下文学习鲁棒性的关键。现有研究多聚焦于自回归模型（ARMs）的静态注意力汇聚（Attention Sink），忽视了去噪过程中动态可见性对注意力锚点的影响。本文通过几何分解与检索头分析，揭示了MDMs中“浅层结构感知、深层内容聚焦”的注意力漂浮机制。该发现从机制层面解释了MDMs在知识密集型任务上优于ARMs的原因，但其结论是否适用于纯参数化推理场景仍存疑。

】

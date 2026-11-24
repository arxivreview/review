# ACL2026 · 高效长上下文Transformer架构方向论文汇编

> 本方向共 9 篇（ACL2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Every Token Counts: Generalizing 16M Ultra-Long Context in Large Language Models ｜分层稀疏注意力（HSA）驱动的超长上下文外推

研究机构：西湖大学

作者：Xiang Hu、Zhanchao Zhou、Ruiqi Liang 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.23319)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.23319)

> 长上下文建模旨在突破Transformer二次方计算复杂度与线性内存增长的瓶颈，实现无限长序列的高效处理。现有稀疏注意力方法因块选择机制非端到端可学习，导致在长序列检索任务中精度随上下文长度增加而急剧退化。本文提出HSA-UltraLong架构，通过结合滑动窗口注意力与分层稀疏注意力，并引入无位置编码策略，在8T token规模上验证了从32K到16M token的上下文外推能力。该工作证明了稀疏检索机制在超长上下文中的可行性，但其依赖特定训练数据分布与架构配比，泛化边界尚待厘清。

】

---

【Gated Differentiable Working Memory for Long-Context Language Modeling ｜门控可微工作记忆

研究机构：中国科学院、美国加州大学默塞德分校

作者：Lingrui Mei、Shenghua Liu、Yiwei Wang 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_dbae060b7b04)

> 长上下文推理中，注意力分数在数千Token间稀释导致关键信息丢失，且模型无法在推理时适应新分布。现有测试时训练（Test-Time Training, TTT）方法采用均匀采样策略，将计算预算浪费在低价值区域，且跨语义异构区域的梯度更新相互干扰。GDWM将TTT重构为预算约束下的记忆巩固问题，通过条件点互信息（Conditional Pointwise Mutual Information, CPMI）量化上下文效用并动态分配梯度步数。该方法以4倍更少的梯度步数实现了与均匀基线相当或更优的性能，但在密集覆盖任务上收益有限，且其理论最优分块大小依赖任务特性，缺乏自适应机制。

】

---

【MATCH: Modulating Attention via In-Context Retrieval for Long-Context Transformers ｜上下文内检索增强稀疏注意力

研究机构：加拿大麦吉尔大学、加拿大蒙特利尔大学

作者：Linrui Ma、Chun Hei Lo、Xinyu Wang 等 15 人

论文原文见 [arXiv](https://arxiv.org/abs/2606.29844)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2606.29844)

> 长上下文大语言模型（LLM）在扩展序列长度时，自注意力机制的二次方计算复杂度与键值缓存（KV Cache）内存线性增长构成双重瓶颈。现有稀疏注意力方案通过限制感受野降低开销，但静态模式导致模型在需要精确回忆远距离信息的任务上性能崩塌。本文提出MATCH框架，将输入上下文视为动态数据存储，通过外部检索器动态定位关键Token并重构注意力掩码，在保持稀疏架构效率的同时恢复全局检索能力。该方法在合成与真实基准上显著优于静态稀疏基线，但其依赖外部检索模块的额外计算开销与部署复杂度，限制了其作为通用架构组件的普适性。

】

---

【Native Hybrid Attention for Efficient Sequence Modeling ｜原生混合注意力

研究机构：清华大学、香港科技大学

作者：Jusen Du、Jiaxi Hu、Tao Zhang 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.07019)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.07019)

> 长上下文建模面临二次方计算复杂度与固定状态信息压缩的矛盾，现有混合架构需管理异构层或引入额外融合参数。NHA通过单一滑动窗口超参数统一层内与层间混合，在保持检索精度的同时实现架构同构。其核心在于将线性RNN记忆与局部精确Token拼接后执行统一Softmax，无需手动调参即可动态分配注意力。该设计在小规模预训练及大模型混合化中验证了效率与精度的平衡，但静态窗口机制在动态稀疏场景下的适应性仍存疑。

】

---

【RRAtention: Dynamic Block Sparse Attention via Per-Head Round-Robin Shifts for Long-Context Inference ｜动态块稀疏注意力中的头轮询采样策略

研究机构：北京大学

作者：Siran Liu、Guoxia Wang、Sa Wang 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_7f7fec27edca)

> 长上下文推理面临二次方计算复杂度与内存带宽的双重瓶颈，现有动态稀疏注意力方法在查询独立性、全局评估与计算开销之间存在不可兼得的权衡。RRAttention 通过头轮询采样策略，在保持查询独立性的同时实现全局模式发现，将计算复杂度从 $O(L^2)$ 降至 $O(L^2/S^2)$。该方法在 HELMET 基准上恢复了全注意力 99.7% 的性能，同时仅计算一半的注意力块。其价值在于工程层面的精度-效率平衡优化，但缺乏对纯检索密集任务的验证，且解码阶段仍依赖密集计算，限制了端到端加速的实际收益。

】

---

【S2O: Early Stopping for Sparse Attention via Online Permutation ｜在线置换与早期停止的稀疏注意力机制

研究机构：厦门大学

作者：Yu Zhang、Songwei Liu、Chenqian Yan 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.22575)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.22575)

> 长上下文推理中，块稀疏注意力因固定块粒度导致块内冗余，形成实际稀疏率天花板。现有方法或依赖静态模式，或进行离线物理置换，均无法在细粒度上集中注意力质量。S2O通过逻辑索引映射实现非连续加载，结合单调增益早期停止，突破块粒度限制。该方法在Llama-3.1-8B上实现3.81倍端到端加速，但缺乏与混合架构在绝对精度上的直接对比，其早期停止机制在极端检索任务下的鲁棒性存疑。

】

---

【Threshold Differential Attention for Sink-Free, Ultra-Sparse, and Non-Dispersive Language Modeling ｜阈值差分注意力（TDA）：消除注意力汇聚与弥散的非Softmax机制

研究机构：英国牛津大学、美国卡内基梅隆大学

作者：Xingyue Huang、Xueying Ding、Mingxuan Ju 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.12145)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.12145)

> 长上下文建模面临Softmax归一化引发的结构性缺陷：注意力汇聚（Attention Sink）迫使模型将概率质量分配给无关Token，注意力弥散（Attention Dispersion）则随序列增长稀释关键信息。现有稀疏注意力方法依赖昂贵的排序或迭代投影，且未根本解决归一化约束；整流注意力（ReLA）虽移除约束但受噪声累积影响，长序列性能退化。本文提出阈值差分注意力（TDA），通过长度依赖的极值阈值截断与差分视图抑制，实现无汇聚、超稀疏且非弥散的注意力机制。该机制在162M参数模型上验证了理论有效性，但缺乏大规模模型与主流长上下文基准的实证支持，其工程落地价值存疑。

】

---

【东北团队新研究：CoMeT: Collaborative Memory Transformer for Efficient Long Context Modeling

研究机构：美国东北大学、清华大学

作者：Runsong Zhao、Shilei Liu、Jiwei Tang 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.01766)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.01766)

> 长上下文处理面临计算复杂度二次方增长与键值缓存（KV Cache）内存线性膨胀的双重瓶颈，现有压缩方法受限于信息论无法改变渐近复杂度，而纯递归模型又因缺乏门控机制导致关键信息遗忘。CoMeT 通过引入门控全局记忆与FIFO临时记忆的双模块插件架构，在保留预训练Transformer骨干的前提下，实现了恒定内存占用与线性时间复杂度。该方法仅需32k上下文微调即可外推至1M token检索，但在综合理解任务上仍略低于全注意力基线，其泛化边界尚待更严苛的跨域验证。

】

---

【理研与东京科学大学提出PHOTON：层级自回归建模将KV流量降至线性，实现光速且内存高效的长文本生成

研究机构：日本理化学研究所、日本东京科学大学

作者：Yuma Ichikawa、Naoya Takagi、Takumi Nakagawa 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.20687)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.20687)

> 长上下文推理中，自回归Transformer因逐Token扫描导致键值缓存（KV Cache）读取成为内存带宽瓶颈，现有稀疏注意力或线性注意力方案虽降低计算密度，但未能改变“水平扫描”的访问模式。PHOTON通过构建多层级潜流结构，将全局上下文压缩为低速率状态，仅在最顶层维护全局KV缓存，底层解码器在固定窗口内并行生成Token，从而将解码阶段的KV流量从二次方降至线性。该方法在1.2B模型规模下实现了475倍的吞吐量-内存比（TPM）提升，但语言建模困惑度（PPL）较基线上升约20%，其以质量换效率的边界尚需更严格的检索任务验证。

】

# ACL-Findings2026 · 图像视频生成与编辑方向论文汇编

> 本方向共 31 篇（ACL-Findings2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【A Universal Avoidance Method for Diverse Multi-branch Generation ｜通用避免生成

研究机构：韩国首尔大学

作者：Kyeongman Park、Minha Jhang、Kyomin Jung

论文原文见 [arXiv](https://arxiv.org/abs/2604.17323)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17323)

> 多分支生成任务要求同一提示词产生显著差异的输出，但现有方法要么依赖逐token或逐像素的高开销操作，要么绑定特定架构导致通用性缺失。UAG通过惩罚最终输出与历史输出的相似度梯度，在推理阶段实现跨架构的多样性增强。该方法将局部与全局相似度损失按生成阶段调度，以极低的计算成本同时适用于自回归与扩散模型。其核心价值在于以1/64的FLOPs实现了比SOTA方法更高的多样性，但图像生成中CLIP分数的下降暗示了多样性与语义保真度之间的潜在冲突。

】

---

【Accelerating Training of Autoregressive Video Generation Models via Local Optimization with Representation Continuity ｜局部优化与表示连续性加速自回归视频生成训练

研究机构：澳门大学

作者：Yucheng Zhou、Jianbing Shen

论文原文见 [arXiv](https://arxiv.org/abs/2604.07402)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.07402)

> 自回归视频生成面临训练成本高、时长受限的瓶颈，主流方案通过增加帧数或迭代推理提升质量，却导致误差级联与训练效率低下。本文切入点在于解耦训练序列长度与推理序列长度，通过局部窗口优化消除曝光偏差。具体做法是引入冻结上下文的局部优化策略，并基于Lipschitz连续性约束隐状态平滑性。该方法在保持推理速度不变的前提下实现2倍训练加速，但仅在短序列数据集上验证，长视频一致性未获证实。

】

---

【Attention Sinks in Diffusion Language Models ｜扩散语言模型中的动态注意力汇聚

研究机构：意大利罗马第一大学

作者：Maximo Eduardo Rulli、Simone Petruzzi、Edoardo Michielon 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.15731)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.15731)

> 掩码扩散语言模型（Masked Diffusion Language Models, MDLM）通过双向注意力实现并行去噪，但其内部注意力分配机制长期缺乏实证研究。现有针对自回归模型（ARM）的注意力汇聚（Attention Sink）分析假设汇聚点位置固定，这一静态假设在MDLM中失效，导致无法解释其生成鲁棒性来源。本文通过定义累积注意力分数指标，追踪三个开源MDLM在去噪过程中的汇聚点轨迹，揭示其动态迁移特性及掩码鲁棒性。该发现修正了对扩散模型注意力机制的认知，但受限于仅分析7B-8B规模模型，未验证该动态特性在更大规模或长序列下的稳定性。

】

---

【Auto-Stega: An Agent-Driven System for Lifelong Strategy Evolution in LLM-Based Text Steganography ｜自演化文本隐写框架

研究机构：华东师范大学

作者：Jiuan Zhou、Yu Cheng、Yuan Xie 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_eed9d1397237)

> 生成式文本隐写旨在利用大语言模型（LLM）直接合成承载秘密信息的文本，以消除传统修改型隐写引入的统计伪影。现有方法依赖手工设计的固定策略，在高嵌入率下难以兼顾效率、隐蔽性与安全性，且缺乏跨域适应能力。Auto-Stega 提出首个基于智能体驱动的自演化框架，通过推理时自动发现、评估并更新策略库，结合奇偶约束动态核典型编码器（PC-DNTE）实现高容量分布保持嵌入。该框架在 News 数据集上实现了 5.97 bits/word 的嵌入率与 0.01 的归一化困惑度，但策略同步机制与跨域泛化能力尚存疑。

】

---

【CMIG: Conceptual Metaphor Theory-Inspired Framework for Metaphorical Image Generation ｜隐喻图像生成的结构化提示框架

作者：Qingbao Huang、Cheng Yang、Jiawei Yao 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_81b6cfa6c472)

> 文本到图像模型在处理隐喻时，常陷入字面渲染陷阱，将“人群是咆哮的河流”生成为真实的河流场景。现有提示词优化方法依赖自由形式的语义扩展，缺乏对源域与目标域映射关系的显式控制，导致源域元素过度干扰目标场景。CMIG 基于概念隐喻理论，通过显式域识别、属性过滤及规则化策略选择，将隐喻解构为可控的视觉生成指令。该框架在零样本条件下提升了语义对齐度，但其规则化决策机制对复杂嵌套隐喻的泛化能力存疑。

】

---

【Design First, Code Later: Aesthetically Pleasing Template-Free Slides Generation ｜分层解耦的幻灯片生成工作流

研究机构：西北工业大学、复旦大学

作者：Zhiyao Cui、Chenxu Wang、Shuyue Hu 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f716728183f9)

> 自动化幻灯片生成面临叙事结构与视觉设计的协同难题，现有方法或依赖固定模板限制创意，或直接输出代码而忽略设计环节。DeepSlides 通过解耦“设计推理”与“代码实现”，引入分层工作流与多智能体强化学习，在无模板约束下实现高质量 PPTX 生成。该方法在人类偏好评估中显著优于开源基线，但其缺乏客观几何精度指标，且长文档风格一致性未获充分验证。

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

【EMCompress: Video-LLMs with Endomorphic Multimodal Compression ｜时序视觉筛选（TVS）：基于认知负荷优化的视频-查询联合重构

研究机构：美国伊利诺伊大学厄巴纳-香槟分校、美国西北大学

作者：Zheyu Fan、Jiateng Liu、Yuji Zhang 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_e3edf62118ff)

> 导读 视频大语言模型（Video-LLMs）在处理长视频时面临感知冗余与语义错位的双重瓶颈，导致推理效率低下且监督信号被噪声稀释。现有时间定位方法仅关注视觉片段的检索，忽略了查询与视频间的逻辑耦合，无法解决复杂多跳推理中的认知负荷问题。本文提出时序视觉筛选（Temporal Visual Screening, TVS）任务，通过多智能体框架 ReSimplifyIt 同步裁剪视频并重写查询，构建答案不变的紧凑输入对。该方法在推理阶段带来 33.7% 的相对性能增益，但其在通用基准上未超越 SOTA，且依赖外部 LLM 的迭代验证机制，计算开销与鲁棒性仍存疑。

】

---

【FastDiSS: Few-step Match Many-step Diffusion Language Model on Sequence-to-Sequence Generation--Full Version ｜少步文本扩散模型的自条件失配与噪声感知训练

作者：Dat Nguyen-Cong、Tung Kieu、Hoang Thanh-Tung

论文原文见 [arXiv](https://arxiv.org/abs/2604.05551)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.05551)

> 连续文本扩散模型在少步采样下，自条件机制因训练-推理分布失配导致误差累积，现有方法未能针对此失效进行训练时修正。FastDiSS 通过自条件扰动（SCP）模拟推理噪声，并结合模型感知噪声缩放（MANS）动态调整高置信 token 的噪声水平，在 5 步内实现接近 20 步的生成质量。该方法在文本序列生成任务上实现了 4 倍至 400 倍的推理加速，但其对长序列误差累积边界的验证尚显不足。

】

---

【From Static Inference to Dynamic Interaction: A Survey of Streaming Large Language Models ｜流式大语言模型（Streaming LLM）的统一分类与交互机制

研究机构：上海交通大学

作者：Junlong Tong、Zilong Wang、YuJie Ren 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.04592)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f1ec09d0a64d)

> 流式大语言模型旨在解决静态全上下文范式无法处理无限增量输入与实时交互的矛盾，但现有研究常混淆自回归解码、增量编码与全双工交互，导致概念边界模糊。本文基于数据流与交互并发性，提出输出流式、顺序流式与并发流式的三级分类体系，将流式处理解耦为生成加速、增量感知与架构适配三个独立维度。该框架为流式智能体提供了结构化的技术路线图，但其有效性依赖于分类逻辑的清晰度，缺乏针对具体视频任务的量化验证。

】

---

【Generative Floor Plan Design with LLMs via Reinforcement Learning with Verifiable Rewards ｜基于可验证奖励强化学习的LLM平面图生成

研究机构：加拿大蒙特利尔大学

作者：Luis Lara、Aristides Milios、Zhi Hao Luo 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.14117)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.14117)

> 建筑平面图生成需在满足严格拓扑连通性的同时，精确控制房间尺寸与面积，现有方法多依赖光栅图像或仅关注邻接关系，导致输出难以直接用于CAD且缺乏数值约束控制。本文切入点在于将平面图表示为JSON多边形结构，并引入强化学习以可验证奖励（RLVR）机制，迫使大语言模型（LLM）在生成过程中显式消除重叠并满足面积约束。通过两阶段微调Llama-3.3-70B-Instruct，该方法在八房间任务上将拓扑兼容性误差降低94%，证明了结构化数据到结构化数据生成范式在硬约束满足上的可行性，但其推理成本与单层住宅数据的局限性仍存疑。

】

---

【Human-Agent Collaborative Paper-to-Page Crafting ｜学术网页自动生成

研究机构：上海交通大学

作者：Qianli Ma、Siyu Wang、Chen Yilin 等 10 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_8fdd22e897b1)

> 学术项目页的构建长期依赖人工模板适配，耗时且质量不一。现有端到端大语言模型（LLM）直接生成网页时，常出现布局混乱与事实幻觉，且缺乏对作者意图的响应机制。AutoPage 提出一种粗到细的多智能体协作框架，通过叙事规划、多模态内容生成与交互式渲染三阶段流水线，嵌入事实校验与可选人工干预，实现高保真网页的自动化构建。该框架在自建基准 PageBench 上显著优于基线模型，但其评估体系局限于单一数据集，跨领域泛化能力尚待检验。

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

【Leveraging Pretrained Language Models as Energy Functions for Glauber Dynamics Text Diffusion ｜基于Glauber动力学的离散扩散语言模型

研究机构：美国俄亥俄州立大学

作者：Tarun Kathuria、Sachin Kumar

论文原文见 [arXiv](https://arxiv.org/abs/2605.04291)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.04291)

> 离散扩散语言模型（DLMs）旨在通过并行去噪突破自回归（AR）模型的串行延迟瓶颈，但现有掩码扩散范式因前向过程缺陷难以超越AR模型的质量上限。本文指出，将预训练语言模型作为能量函数嵌入Glauber动力学，能显著拉近噪声分布与数据分布的距离，从而解决离散扩散训练样本效率低下的核心痛点。该方法通过UL2架构实现因果生成与掩码填充的统一，在GPT-2规模下实现了与AR模型相当的生成困惑度。尽管其推理速度较慢，但在同等计算预算下，其单位算力产生的文本质量优于AR模型，为离散扩散提供了理论更严谨的替代路径。

】

---

【LongInsightBench: A Comprehensive Benchmark for Evaluating Omni-Modal Models on Human-Centric Long-Video Understanding ｜长视频全模态理解基准

研究机构：华中科技大学、北京大学

作者：ZhaoYang Han、Qihan Lin、Hao Liang 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.17305)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.17305)

> 长视频理解面临的核心矛盾是海量视觉Token与有限上下文窗口的物理冲突，以及多模态信号在时间轴上的对齐难题。现有基准多侧重短时片段或单一模态，无法评估模型在分钟级视频中对人类意图、观点演变的深层推理能力。本文构建了首个聚焦“人类中心线索”的全模态长视频基准，通过严格过滤与多模态融合实验，揭示了当前全模态大语言模型（OLMs）存在的“融合赤字”现象。该工作填补了评估空白，但其结论是否适用于代理式推理框架尚存疑。

】

---

【Mechanistic Interpretability of Text-to-Image Diffusion Models via Cross-Attention Interventions ｜交叉注意力因果干预下的扩散模型机制可解释性

作者：Maisha Maliha、Dean F. Hougen

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ddd3a8113a00)

> 文本到图像扩散模型在生成高保真图像时，常出现物体遗漏或属性错配，但其内部如何将提示词语义映射至像素结构仍缺乏透明解释。现有注意力可视化方法仅反映查询与键的对齐概率，无法量化语义信号的实际注入量，更无法建立内部组件与语义功能的因果联系。本文通过固定种子移除单个Token生成反事实图像，结合投影输出范数计算Token接地图与Head级KL散度敏感性，构建了从词元到注意力头的因果归因框架。该框架揭示了语义接地的稀疏性与Head特异性，但在U-Net架构上的结论能否泛化至DiT架构，以及归因精度提升是否必然转化为生成质量增益，仍存疑。

】

---

【mPresenter: An Agentic Framework for Generating Multilingual Presentation Videos from Scientific Papers ｜多语言学术视频生成代理系统

作者：Wenhan Han、Xiao Xiao、Mykola Pechenizkiy 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_5bb75c578a43)

> 学术视频生成旨在将静态论文转化为动态视听内容，以解决长文档信息密度高且跨语言理解困难的传播瓶颈。现有单语言流水线系统在处理非英语图表时存在语义断裂，且缺乏针对内容保真度的客观评估基准。本文提出 MPRESENTER，通过规划、审查、编码与解释四个代理的迭代协作，实现多语言论文到视频的高保真转换。该系统在 MPREBENCH 上提升了问答准确率，但其离线迭代架构与实时流式视频理解的因果约束存在本质差异，其多语言泛化能力在极端低资源语言下的鲁棒性仍存疑。

】

---

【On-Policy Self-Distillation for Efficient Diffusion Language Models with Early-Stage Calibration ｜校准在线自蒸馏

作者：Huaisheng Zhu、MingYu Liu、Junze Liu 等 13 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_9d223bd4529d)

> 扩散语言模型（DLLMs）在并行解码时面临早期步上下文不足导致的预测失准，严重制约了推理效率与输出质量。现有自蒸馏方法仅最大化似然，无法利用未来步信息修正早期错误，导致模型在增加并行Token数时性能急剧下降。本文提出校准在线自蒸馏（COPSD），通过构建基于未来步信息的非归一化目标分布，将其蒸馏回原始模型以校准早期预测。该方法无需演示数据，显著提升了DLLMs在数学、规划等任务上的并行生成效率，但其效果依赖于训练时的组归一化稳定性，且未验证在复杂长程推理任务上的泛化能力。

】

---

【One Token Is Enough: Improving Diffusion Language Models with a Sink Token ｜固定注意力汇聚点：扩散语言模型的稳定性修正

作者：Zihou Zhang、Zheyong Xie、Li Zhong 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.19657)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.19657)

> 扩散语言模型（DLMs）在并行解码中面临注意力汇聚点位置随去噪步长漂移的“移动汇聚点”问题，导致推理过程缺乏稳定锚点，进而限制模型性能上限。现有加速或优化方法多聚焦于采样步数或KV缓存，忽视了注意力机制内部的信息混合失控这一底层动力学缺陷。本文通过引入一个仅自注意且全局可见的额外Sink Token，将不稳定的移动汇聚点转化为位置固定的结构锚点。该方案以极低的计算开销实现了跨规模、跨初始化策略的性能提升，但其有效性是否依赖于特定模型规模或长序列场景，仍存疑。

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

---

【ROMA: Real-time Omni-Multimodal Assistant with Interactive Streaming Understanding ｜实时全模态流式助手

研究机构：中国科学院、中科院计算所

作者：Xueyun Tian、Wei Li、Bingbing Xu 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.10323)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.10323)

> 流式视频理解的核心矛盾在于无限输入流与有限上下文窗口的冲突，以及被动响应无法适应实时交互的痛点。现有方法要么仅处理视频而忽略音频，要么将时机决策与内容生成耦合导致语义冲突。ROMA 通过构建同步多模态单元与解耦的 Speak Head，统一了主动与被动交互范式。该框架在主动任务上取得显著优势，但其依赖长上下文 KV 缓存的设计在超长流场景下的显存效率存疑。

】

---

【SCMAPR: Self-Correcting Multi-Agent Prompt Refinement for Complex-Scenario Text-to-Video Generation ｜场景感知自纠正多智能体提示词优化

研究机构：华东师范大学、清华大学

作者：Chengyi Yang、Pengzhen Li、Jiayin Qi 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.05489)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.05489)

> 文本到视频生成在复杂场景下常因提示词模糊导致语义遗漏或时空逻辑断裂，现有检索增强或单次重写方法缺乏对困难源的显式识别与保真校验。SCMAPR 将提示词优化重构为场景路由、策略合成、原子级蕴含验证与条件修正的多智能体流水线。该框架在 VBench 和 EvalCrafter 上分别取得 88.21% 和 66.74 的平均分，显著优于基线，但其性能增益高度依赖底层扩散模型的能力上限，且多智能体推理带来的延迟成本未被量化。

】

---

【SDAR: A Synergistic Diffusion-AutoRegression Paradigm for Scalable Sequence Generation ｜协同扩散-自回归范式

研究机构：浙江大学、美国马里兰大学帕克分校

作者：Shuang Cheng、Yihan Bian、Dawei Liu 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.06303)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.06303)

> 扩散语言模型（DLMs）旨在通过并行解码突破自回归（AR）模型的串行延迟瓶颈，但受限于证据下界（ELBO）训练目标收敛缓慢及缺乏键值（KV）缓存导致的 $O(N^3)$ 推理复杂度，难以在大规模场景落地。现有混合架构虽尝试结合两者优势，却因端到端联合训练带来的算力开销激增而缺乏实用性。本文提出 SDAR，通过解耦训练与推理阶段，利用轻量级适配将预训练 AR 模型转换为块扩散模型，在保留 AR 训练效率的同时实现块内并行生成。该范式在 30B 规模下展现出与 AR 模型相当的推理能力，并因局部双向注意力在科学推理任务上取得优势，但其性能增益是否完全源于架构转换而非数据适配，仍需更严格的隔离实验验证。

】

---

【Spatiotemporal Sycophancy: Negation-Based Gaslighting in Video Large Language Models ｜时空谄媚：视频大语言模型中的否定式煤气灯效应

研究机构：复旦大学、新加坡管理大学

作者：Ziyao Tang、Pengkun Jiao、Bin Zhu 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.17873)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.17873)

> 视频大语言模型在对话交互中面临信念反转风险，即模型在用户否定反馈下撤回正确的视觉判断并编造解释。现有鲁棒性研究多聚焦静态图像或文本，缺乏对视频时空动态证据被对话压力覆盖的系统评估。本文通过构建否定式煤气灯效应评估框架与专用基准，量化了主流模型在对抗交互下的脆弱性。该工作揭示了当前对齐机制在视觉证据与用户指令冲突时的失效边界，但仅提供了推理时防御手段，未解决模型内部时空表征不稳定的根本问题。

】

---

【StreamingEval: A Unified Evaluation Framework towards Realistic Streaming Video Understanding ｜流式视频理解的系统级部署评估框架

研究机构：华东师范大学

作者：Tang Guowei、Tianwen Qian、Huanran Zheng 等 5 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_79ed3ebd1e2f)

> 流式视频理解要求模型在严格因果约束下处理无限视频流，核心矛盾在于实时响应延迟与长程语义记忆的完整性。现有基准多聚焦于答案准确率，忽视了显存溢出、编码积压与解码延迟对系统可部署性的致命影响，导致“在线”模型在真实流式场景中失效。本文提出 StreamingEval，通过固定容量 FIFO 记忆库标准化历史上下文，并联合评估吞吐量、延迟与准确率。该框架揭示了当前主流模型在严格流式约束下的巨大性能缺口，但缺乏对高级记忆管理策略的差异化验证。

】

---

【StreamMeCo: Long-Term Agent Memory Compression for Efficient Streaming Video Understanding ｜流式智能体记忆压缩

研究机构：上海交通大学、复旦大学

作者：Junxi Wang、Te Sun、Jiayi Zhu 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.09000)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.09000)

> 流式视频理解中，基于智能体记忆图的方法虽能维持长程实体一致性，但记忆节点随视频时长线性增长，导致检索延迟呈非线性上升，无法满足实时交互要求。现有视觉Token或KV Cache压缩策略无法处理外部明文记忆图的结构性冗余。StreamMeCo 提出一种免训练的记忆图压缩框架，通过双分支采样与时间衰减检索机制，在70%压缩率下实现1.87倍检索加速且准确率平均提升1.0%。该工作验证了图结构压缩在工业级流式智能体中的可行性，但其在通用流式基准上的泛化能力及与内部KV Cache管理路线的优劣对比仍存疑。

】

---

【When Backdoors Go Beyond Triggers: Semantic Drift in Diffusion Models Under Encoder Attacks ｜编码器后门引发的无触发语义漂移诊断

作者：Shenyang Chen、Liuwan Zhu

论文原文见 [arXiv](https://arxiv.org/abs/2602.20193)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.20193)

> 文本到图像（T2I）扩散模型的后门攻击研究长期聚焦于触发器激活成功率（ASR），却忽视了编码器侧污染对良性生成质量的隐性损害。现有基于ASR的评估范式存在“盲区”，无法捕捉无触发状态下嵌入空间的几何扭曲，导致防御机制在抑制显式攻击的同时遗留结构性缺陷。本文提出SEMAD框架，通过Jacobian局部变形分析与语义漂移评分，量化这种无触发的语义坍缩。该工作揭示了后门攻击的几何本质，但缺乏对修复效果的验证，其诊断价值是否足以指导防御设计仍存疑。

】

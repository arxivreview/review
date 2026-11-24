# ICLR2026 · 扩散Transformer效率优化方向论文汇编

> 本方向共 19 篇（ICLR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【BWCache: Accelerating Video Diffusion Transformers through Block-Wise Caching ｜块级特征缓存加速视频扩散Transformer

研究机构：北京师范大学

作者：Hanshuai Cui、Zhiqing Tang、Zhifei Xu 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.13789)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.13789)

> 视频扩散Transformer（DiT）的推理延迟主要源于多步去噪中DiT块的串行计算，现有缓存方法因粒度粗糙或固定策略导致质量与效率失衡。本文切入点在于发现DiT块特征在中间时间步呈现U形稳定模式，据此设计块级动态缓存机制。通过相对L1距离阈值触发复用并引入周期性重计算，BWCache在保持视觉保真度的同时实现最高2.6倍加速。该方法在训练-free缓存路线中表现优异，但受限于固定阈值与单一粒度，未解决极端压缩下的理论误差界问题。

】

---

【DiffSparse: Accelerating Diffusion Transformers with Learned Token Sparsity ｜可学习稀疏度分配的扩散Transformer加速

研究机构：清华大学

作者：Haowei Zhu、Ji Liu、Ziqiong Liu 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.03674)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.03674)

> 扩散Transformer（DiT）推理加速的核心矛盾在于，固定步数下的计算冗余与生成质量之间的权衡。现有Token级缓存方法依赖人工设定的稀疏率与全计算步，导致加速潜力受限且调参空间巨大。DiffSparse将稀疏度分配建模为动态规划问题，通过可学习成本预测器端到端优化各层稀疏配置，并引入两阶段训练消除全计算步依赖。该方法在PixArt-α上以1.91倍加速比实现FID 27.79，优于ToCa与TaylorSeer，但其加速比远低于投机解码类方法，且需额外训练开销。

】

---

【Diffusion Transformers with Representation Autoencoders ｜表示自编码器与扩散Transformer

研究机构：美国纽约大学

作者：Boyang Zheng、Nanye Ma、Shengbang Tong 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.11690)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.11690)

> 扩散Transformer（DiT）训练长期受限于变分自编码器（VAE）低维潜在空间的语义贫乏与重建瓶颈，导致收敛缓慢且生成质量受限。现有通过外部编码器对齐损失的间接方法引入了额外的训练阶段与调优复杂度，未能从根本上解决潜在空间与生成目标的不匹配。本文提出表示自编码器（RAE），直接以冻结的预训练表示编码器替代VAE编码器，并设计维度依赖的噪声调度与宽浅DiT头以适配高维语义潜在空间。该范式在ImageNet上实现了1.51 FID（无引导）与1.13 FID（有引导）的生成质量，但其在视频生成及极端压缩场景下的泛化能力尚未得到验证。

】

---

【DSA : EFFICIENT SERVING FOR VIDEO GENERATION MODELS VIA DISTRIBUTED SPARSE ATTENTION ｜分布式稀疏注意力

研究机构：新加坡南洋理工大学、美国密歇根大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_79459436)

> 视频生成模型因注意力机制的二次方复杂度导致推理延迟极高，单卡加速手段在分布式场景下失效。现有稀疏注意力方法无法适配序列并行，而序列并行又因通信开销呈现次线性扩展。DSA通过为空间与时间稀疏模式匹配不同的并行策略，并动态调度计算与通信重叠，实现了训练-free的分布式推理加速。该方法在8卡部署下将生成延迟降低至单卡的约1/11，但静态稀疏模式在动态负载下的泛化能力存疑。

】

---

【FastVMT: Eliminating Redundancy in Video Motion Transfer ｜视频运动迁移中的冗余消除

研究机构：上海交通大学

作者：Yue Ma、Zhikai Wang、Tianhao Ren 等 12 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.05551)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.05551)

> 视频运动迁移旨在将参考视频的动作模式迁移至目标视频，同时保留目标外观，但现有基于扩散Transformer（DiT）的训练-free方法在注意力提取与梯度优化阶段存在大量冗余计算，导致推理延迟高达数十分钟。FastVMT通过识别并利用帧间运动的局部平滑性与去噪轨迹梯度的稳定性，分别引入滑动窗口注意力提取与步长跳过梯度优化策略，在不重训的前提下显著降低计算开销。该方法在保持生成质量的同时实现了3.43倍加速，但其固定窗口大小在剧烈运动场景下的鲁棒性仍存疑。

】

---

【Let Features Decide Their Own Solvers: Hybrid Feature Caching for Diffusion Transformers ｜混合特征缓存：让特征维度自选求解器

研究机构：上海交通大学、华南理工大学

作者：Shikang Zheng、Guantao Chen、Qinming Zhou 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.04188)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.04188)

> 扩散Transformer（Diffusion Transformer, DiT）的迭代去噪过程导致推理延迟高企，特征缓存通过复用或预测隐藏状态来缓解这一瓶颈。现有方法隐含假设所有特征维度遵循统一的动态演化规律，采用全局一致的缓存或外推策略，忽视了高维特征空间中不同维度动态行为的异质性。HyCa将特征演化建模为混合常微分方程（Ordinary Differential Equation, ODE），通过离线聚类识别动态模式，并为每个维度簇分配最优数值求解器。该框架在无需重训的前提下实现了图像、视频及编辑任务的高倍加速，但其离线探针阶段的稳定性与超参数敏感性仍需进一步验证。

】

---

【Massive Activations are the Key to Local Detail Synthesis in Diffusion Transformers ｜细节引导

研究机构：上海交通大学、澳大利亚莫纳什大学

作者：Chaofan Gan、Zicheng Zhao、Yuanpeng Tu 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.11538)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.11538)

> 导读 扩散Transformer（Diffusion Transformer, DiT）在生成高质量图像时，常因过度关注全局语义对齐而牺牲局部纹理细节。现有采样引导策略如Classifier-Free Guidance (CFG) 虽能增强文本-图像对齐，却难以独立优化细节保真度，且缺乏对模型内部机制的针对性干预。本文通过系统分析DiT中的Massive Activations (MAs)，揭示其由时间步嵌入调制并驱动局部细节合成的因果机制，提出一种免训练的自引导策略DG。DG通过破坏MAs构建“细节缺失”模型，引导原模型恢复细节，在保持语义一致性的同时显著提升生成质量。该工作填补了DiT内部机制与生成质量优化之间的空白，但其额外前向传播带来的延迟开销在实时场景下的适用性尚存疑。

】

---

【Plug-and-Play Fidelity Optimization for Diffusion Transformer Acceleration via Cumulative Error Minimization ｜累积误差最小化优化扩散Transformer缓存策略

研究机构：哈尔滨工业大学

作者：Tong Shao、Yusen Fu、Guoying Sun 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.23258)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.23258)

> 扩散Transformer（DiT）推理加速的核心瓶颈在于特征缓存引发的误差累积，现有校正方法受限于静态缓存策略，无法充分释放校正潜力。本文切入点在于将缓存策略优化从实时估计转为离线全局规划，通过动态规划求解最小累积误差的间隔组合。该方法作为插件嵌入现有加速框架，在保持加速比的同时显著提升生成保真度，但其离线建模的样本代表性假设在极端内容分布下是否成立仍存疑。

】

---

【Positional Encoding Field ｜位置编码场驱动的扩散Transformer几何生成

研究机构：美国德克萨斯大学奥斯汀分校

作者：Yunpeng Bai、Haoxiang Li、Qixing Huang

论文原文见 [arXiv](https://arxiv.org/abs/2510.20385)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.20385)

> 扩散Transformer（Diffusion Transformer, DiT）在视觉生成中占据主导地位，但其内部如何组织空间结构尚不明确。现有方法多依赖显式几何条件或视频插帧实现新视角合成（Novel View Synthesis, NVS），存在误差累积或计算冗余。本文发现DiT的空间连贯性主要由位置编码（Positional Encoding, PE）而非Token间依赖决定，据此提出PE-Field，将2D PE扩展为3D深度感知与多级层次化结构。该机制通过重映射PE实现几何可控生成，在单图NVS任务上取得SOTA，但其在极端视角变化下的鲁棒性仍待验证。

】

---

【PYRAMIDAL PATCHIFICATION FLOW FOR VISUAL GENERATION ｜金字塔补丁化流

研究机构：复旦大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_79985633)

> 扩散Transformer（DiT）推理延迟主要源于固定补丁大小导致的高噪声阶段Token冗余，现有金字塔流方法通过降低潜变量分辨率来减少计算，但引入了轨迹跳跃与重噪声技巧，破坏了采样连续性。PPFlow抓住“潜变量分辨率不变”这一被忽略的约束，通过在不同去噪阶段使用不同大小的补丁但保持全分辨率潜变量，实现了Token数的自适应缩减。该方法仅需在Patchify和Unpatchify层引入阶段特定的线性投影，DiT块参数完全共享，从而在保持推理流程与标准DiT一致的前提下，将256x256图像生成的测试FLOPs降低37.8%至50.6%。其价值在于以极低的额外训练成本（<10%预训练FLOPs）换取了1.6x至2.0x的推理加速，但sFID指标略差于基线，暗示空间细节可能存在轻微损失。

】

---

【QuantSparse: Comprehensively Compressing Video Diffusion Transformer with Model Quantization and Attention Sparsification ｜量化与稀疏协同压缩的视频扩散Transformer

研究机构：中国科学院、中国科学院大学

作者：Weilun Feng、Chuanguang Yang、Haotong Qin 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.23681)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.23681)

> 视频扩散Transformer（DiT）在高分辨率生成中面临显存与延迟的双重瓶颈，单独使用量化或注意力稀疏化在激进压缩下均会导致生成质量崩塌。现有工作将二者视为正交技术简单叠加，却忽视了稀疏掩码移除低幅值权重后，量化噪声对剩余注意力乘积的系统性扰动会形成“放大注意力偏移”，导致联合压缩性能远低于预期。QuantSparse通过多尺度显著性注意力蒸馏（MSAD）对齐量化偏差，并利用二阶稀疏注意力重参数化（SSAR）恢复稀疏丢失信息，实现了W4A8量化与15%注意力密度下的近无损生成。该框架在14B参数模型上取得了3.80倍存储压缩与1.74倍加速，但其静态密度策略在极端压缩下的鲁棒性仍存疑。

】

---

【RAPID: Tri-Level Reinforced Acceleration Policies for Diffusion Transformer ｜三级强化学习加速策略

研究机构：丰田研究所、新加坡国立大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_10024266)

> 扩散Transformer（Diffusion Transformer, DiT）推理加速面临的核心矛盾是：静态启发式策略无法适应不同图像的复杂度差异，而动态神经网微调成本过高。现有训练-free方法如特征缓存与稀疏注意力虽能加速，但依赖固定阈值或手动规则，导致质量波动与加速比受限。RAPID[3]将DiT采样过程建模为马尔可夫决策过程，通过强化学习训练三个轻量级策略头，在冻结生成器参数的前提下实现逐图自适应加速。该方法在Stable Diffusion 3和FLUX上实现了约3倍加速，但策略头训练仍依赖特定提示词分布，其泛化边界尚待验证。

】

---

【RAPID^3: Tri-Level Reinforced Acceleration Policies for Diffusion Transformer ｜三级强化加速策略

研究机构：丰田研究所、阿里巴巴集团

作者：Wangbo Zhao、Yizeng Han、Zhiwei Tang 等 10 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.22323)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.22323)

> 扩散Transformer（DiT）推理加速面临静态策略质量波动与动态网络训练成本高的双重困境。现有训练-free方法依赖固定启发式，无法适应图像复杂度差异，而动态神经网络需微调骨干参数，部署受限。RAPID[3]将去噪过程建模为马尔可夫决策过程，通过强化学习训练三个轻量策略头，在冻结骨干前提下实现逐图自适应加速。该方法在Stable Diffusion 3和FLUX上实现近3倍加速且保持质量，但其加速比低于基于投机解码的SOTA方法，且未验证视频生成场景。

】

---

【Relational Feature Caching for Accelerating Diffusion Transformers ｜关系特征缓存

研究机构：韩国延世大学、韩国科学技术研究院

作者：Byunggwan Son、Jeimin Jeon、Jeongwoo Choi 等 4 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.19506)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.19506)

> 扩散Transformer（DiT）推理加速的核心矛盾在于时间步间的特征冗余与缓存误差累积之间的权衡。现有预测式缓存方法依赖时间外推，但特征变化幅度的不规则性导致预测误差在长间隔下急剧放大，严重损害生成质量。本文切入点在于发现模块输入特征变化幅度与输出特征变化幅度存在强相关性，利用这一关系替代纯时间外推。具体做法是提出关系特征估计（RFE）与关系缓存调度（RCS），分别用于修正预测幅度和动态触发全计算。该方法在同等计算预算下显著优于TaylorSeer，但其有效性依赖于局部线性假设，在深层非线性模块中的普适性存疑。

】

---

【REPRESENTATION ALIGNMENT FOR DIFFUSION TRANSFORMERS WITHOUT EXTERNAL COMPONENTS ｜自表示对齐加速扩散Transformer训练

研究机构：西北工业大学、浙江大学

作者：Dengyang Jiang、Mengmeng Wang、Liuzhuozheng Li 等 9 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_5360243)

> 扩散Transformer（DiT）训练收敛缓慢，现有加速方法依赖外部预训练编码器或辅助任务，限制了部署灵活性。本文发现DiT内部特征随层深和噪声降低呈现“从坏到好”的判别性趋势，提出自表示对齐（Self-Representation Alignment, SRA）方法。通过让浅层高噪声特征对齐深层低噪声特征，SRA在无外部组件情况下加速收敛。该方法在ImageNet 256x256上以800 epochs达到1.58 FID，优于基线但略逊于依赖外部编码器的REPA，其长期训练下的性能饱和特性尚存疑。

】

---

【SCALINGCACHE: EXTREME ACCELERATION OF DITS THROUGH DIFFERENCE SCALING AND DYNAMIC INTERVAL CACHING ｜ScalingCache：基于差分缩放与动态间隔的DiT推理加速

研究机构：浙江大学、快手

作者：Lihui Gu、Jingbin He、Lianghao Su 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_42972645)

> 扩散Transformer（DiT）的迭代去噪过程导致视频生成延迟高达数分钟，严重制约了专业级应用的实时性。现有特征缓存方法虽能利用时间步冗余，但静态复用或简单线性外推在特征剧烈变化时误差累积显著，无法满足近无损质量要求。本文提出ScalingCache，通过离线预计算的块级差分缩放系数融合零阶与一阶特征，并结合基于累积误差的动态阈值调整计算间隔，在免训练前提下实现2.3–3.1倍加速。该方法在保真度上优于现有缓存策略，但离线系数估计对分布外样本的鲁棒性尚存疑。

】

---

【SLA: BEYOND SPARSITY IN DIFFUSION TRANSFORM ERS VIA FINE-TUNABLE SPARSE–LINEAR ATTENTION ｜稀疏-线性混合注意力

研究机构：清华大学

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_ICLR_2026_60240624)

> 扩散Transformer（DiT）在视频生成中因序列长度达数万至十万级，导致注意力机制的二次方计算复杂度成为主要延迟瓶颈。现有纯稀疏注意力在中等序列长度下难以突破90%稀疏率，而纯线性注意力则因权重高秩特性导致视频质量严重退化。SLA基于注意力权重可分解为高秩稀疏部分与低秩稠密部分的观察，将二者分别用FlashAttention和线性注意力处理，实现95%稀疏率下的无损加速。该混合架构在Wan2.1-1.3B上取得2.2倍端到端加速，但其依赖微调的部署成本与线性注意力作为补偿而非近似的理论边界，仍存疑。

】

---

【SLA: Beyond Sparsity in Diffusion Transformers via Fine-Tunable Sparse-Linear Attention ｜稀疏-线性混合注意力

研究机构：清华大学

作者：Jintao Zhang、Haoxu Wang、Kai Jiang 等 13 人

论文原文见 [arXiv](https://arxiv.org/abs/2509.24006)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.24006)

> 扩散Transformer（Diffusion Transformer, DiT）在视频生成中面临注意力计算的二次方复杂度瓶颈，现有稀疏注意力方法在序列长度低于50K时难以突破90%的稀疏率，而线性注意力单独使用会导致视频质量严重退化。本文发现注意力权重可分解为高秩关键部分与极低秩边缘部分，据此提出SLA，将稀疏注意力与线性注意力融合为单一GPU内核，对关键块执行精确计算、边缘块执行线性补偿、冗余块直接跳过。该设计在Wan2.1-1.3B上实现了95%的注意力计算削减与2.2倍端到端加速，但需依赖少量微调步骤，且其线性补偿机制的有效性边界尚待更广泛的序列长度与模型规模验证。

】

---

【Sprint: Sparse-Dense Residual Fusion for Efficient Diffusion Transformers ｜稀疏-稠密残差融合加速扩散Transformer训练

研究机构：韩国高丽大学、韩国科学技术院

作者：Dogyun Park、Moayed Haji-Ali、Yanyu Li 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2510.21986)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2510.21986)

> 扩散Transformer（DiT）训练成本随序列长度呈二次方增长，导致大规模预训练在算力与内存上不可承受。现有Token丢弃方法在高丢弃率下表示退化严重，且难以与外部监督信号兼容。本文提出SPRINT，通过将DiT解耦为稠密浅层路径与稀疏深层路径并引入残差融合，在75% Token丢弃率下保持生成质量，并衍生出Path-Drop Guidance（PDG）推理加速机制。该方法在训练效率上取得显著突破，但其静态丢弃策略在动态场景中的泛化能力存疑。

】

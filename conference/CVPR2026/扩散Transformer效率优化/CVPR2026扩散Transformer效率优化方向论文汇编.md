# CVPR2026 · 扩散Transformer效率优化方向论文汇编

> 本方向共 25 篇（CVPR2026）。按论文标题字母序排列。
> 每篇包含：英文标题 ｜中文标题、研究机构、作者、原文链接、分析报告链接、一句话导语。

---

【Accelerating Diffusion-based Video Editing via Heterogeneous Caching: Beyond Full Computing at Sampled Denoising Timestep ｜异构缓存加速扩散视频编辑

研究机构：新加坡南洋理工大学、上海交通大学

作者：Tianyi Liu、Ye Lu、Linfeng Zhang 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.24260)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.24260)

> 扩散Transformer（DiT）在视频编辑中面临迭代去噪与空间-时间Token交互的双重计算瓶颈，现有缓存策略仅利用时间步冗余，忽视了编辑任务中区域兴趣（ROI）导致的Token异质性。本文切入点在于联合建模时间步与Token维度的冗余，通过语义聚类与注意力相关性筛选实现部分计算。该方法在保持编辑保真度的前提下实现了2.67倍加速，但其加速上限受限于Token筛选的保守策略，且未验证在极端压缩比下的误差累积边界。

】

---

【AdaCluster: Adaptive Query-Key Clustering for Sparse Attention in Video Generation ｜自适应查询-键聚类稀疏注意力

研究机构：中国科学技术大学、澳门大学

作者：Haoyue Tan、Shengnan Wang、Yulin Qiao 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.18348)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.18348)

> 导读 视频扩散Transformer（DiT）在高分辨率长序列生成中面临二次方注意力复杂度导致的严重延迟瓶颈。现有动态稀疏方法要么忽略Token语义相似性，要么采用固定聚类策略无法适配不同层间分布的异质性，导致精度损失。本文提出AdaCluster，通过为查询和键向量设计非对称的自适应聚类策略，在无需训练的前提下实现加速。该方法在单卡A40上实现了1.67×至4.31×的端到端加速，但其在极端长序列下的理论误差界与硬件感知优化边界仍存疑。

】

---

【Attention Surgery: An Efficient Recipe to Linearize Your Video Diffusion Transformer ｜视频扩散Transformer的注意力线性化手术

作者：Mohsen Ghafoorian、Denis Korzhenkov、Amirhossein Habibian

论文原文见 [arXiv](https://arxiv.org/abs/2509.24899)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2509.24899)

> 视频扩散模型（Video Diffusion Models, VDMs）的核心瓶颈在于自注意力机制的二次方复杂度，导致长序列与高分辨率生成面临计算爆炸。现有加速方案多依赖推理时的动态稀疏或缓存，难以从根本上改变架构的计算复杂度，而从头训练线性注意力模型又受限于巨大的算力成本。本文提出“注意力手术”框架，通过轻量级蒸馏与微调，将预训练模型中的Softmax注意力替换为混合线性注意力，并引入异构块率优化策略。该工作以极低的算力代价实现了接近原始模型的生成质量，为视频生成模型的端侧部署提供了可行的架构级加速路径，但其在复杂时序动态下的保真度边界仍需进一步验证。

】

---

【Beyond Fixed Formulas: Data-Driven Linear Predictor for Efficient Diffusion Models ｜可学习线性预测器

研究机构：上海交通大学、电子科技大学

作者：Zhirong Shen、Rui Huang、Jiacheng Liu 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2604.26365)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2604.26365)

> 扩散Transformer（Diffusion Transformer, DiT）推理加速中，特征缓存路线长期受困于固定系数预测器在长间隔下的误差累积。现有预测方法虽优于静态复用，但其系数由泰勒展开等公式预先确定，无法适应不同模型的特征动态。本文切入点在于揭示这些预测器本质上是历史特征的固定线性组合，进而提出用数据驱动的可学习权重替代公式系数。具体做法是训练一个极轻量的线性预测器，在50张图像上20秒内收敛。该方法在极端加速比下显著优于现有缓存基线，但其评估仅依赖像素级保真度指标，缺乏对生成分布多样性的验证，这一局限是否影响其在实际部署中的泛化能力尚存疑问。

】

---

【DDiT: Dynamic Patch Scheduling for Efficient Diffusion Transformers ｜动态补丁调度

研究机构：美国波士顿大学

作者：Dahye Kim、Deepti Ghadiyaram、Raghudeep Gadde

论文原文见 [arXiv](https://arxiv.org/abs/2602.16968)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.16968)

> 扩散Transformer（DiT）推理延迟主要源于固定Token化导致的二次方注意力计算与迭代去噪的双重冗余。现有加速方法多采用静态剪枝或固定间隔缓存，无法根据输入内容复杂度动态分配计算资源，导致简单场景过度计算或复杂场景细节丢失。本文提出测试时动态补丁调度策略，通过监测潜变量流形演化速率自适应调整Token粒度，在保持生成质量的前提下实现显著加速。该方法在FLUX-1.Dev上取得3.52倍加速比，但需微调LoRA分支以适配新补丁尺寸，其“轻量级训练-based”属性与领域内“训练-free优先”的共识存在张力，部署灵活性是否受损尚需验证。

】

---

【DiT-IC: Aligned Diffusion Transformer for Efficient Image Compression ｜对齐扩散Transformer用于高效图像压缩

研究机构：南京大学

作者：Junqi Shi、Ming Lu、Xingchen Li 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.13162)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.13162)

> 现有扩散图像压缩方法受限于U-Net架构在浅层潜空间的高计算开销，难以兼顾感知质量与解码效率。DiT-IC利用DiT恒定空间分辨率特性，将扩散过程迁移至32×深层潜空间，并通过方差引导流、自蒸馏对齐与潜变量条件引导实现单步重构。该方法在保持SOTA感知质量的同时，将解码延迟降低至0.15秒，并在16GB显存设备上支持2048×2048图像重构。其单步重构策略在极低码率下的语义稳定性及编码器联合微调的潜力，仍需进一步验证。

】

---

【DiverseDiT: Towards Diverse Representation Learning in Diffusion Transformers ｜扩散Transformer中的表示多样性学习

研究机构：复旦大学

作者：Mengping Yang、Zhiyu Tan、Binglei Li 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.04239)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.04239)

> 扩散Transformer (DiT) 训练收敛缓慢的核心瓶颈在于内部表示的同质化，导致不同层特征冗余且缺乏互补性。现有方法如REPA依赖外部编码器对齐，但过度对齐反而抑制了模型内部的表示多样性，且外部依赖增加了资源开销。本文通过系统分析揭示“块间表示多样性”是高效训练的关键，并提出DiverseDiT框架，利用长残差连接和多样性损失显式促进特征分化。该方法无需外部引导即可加速收敛，但在极端压缩或单步生成场景下的泛化边界尚需进一步验证。

】

---

【FlashDecoder: Real-Time Latent-to-Pixel Streaming Decoder with Transformers ｜实时流式视频解码器

作者：Minguk Kang、Suha Kwak

论文原文见 [arXiv](https://arxiv.org/abs/2607.14898)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2607.14898)

> 实时视频生成中，潜空间去噪已接近实时速度，但将潜变量映射回像素的解码器仍占据超过60%的推理时间，成为新的延迟瓶颈。现有3D卷积解码器内存开销大且需空间分块，而双向Transformer解码器无法流式输出。本文提出FlashDecoder，一种纯Transformer架构的逐帧流式解码器，通过固定窗口滚动KV缓存实现恒定延迟与有界内存。该方法在保持与卷积解码器相当的重建质量下，实现了数量级的吞吐提升，但其对长程时序依赖的捕捉能力仍受限于固定窗口大小。

】

---

【Forecast the Principal, Stabilize the Residual: Subspace-Aware Feature Caching for Diffusion Transformers ｜子空间感知特征缓存

作者：Guantao Chen、Shikang Zheng、Yuqi Lin 等 4 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_989c33a15ff4)

> 扩散Transformer（DiT）推理加速的核心矛盾在于迭代去噪过程中的时间步冗余与高维特征空间预测的不可靠性。现有特征缓存方法假设全特征空间时间动态平滑，导致高频噪声在预测中累积，限制了加速比下的生成保真度。本文切入点在于揭示特征空间存在主子空间与残差子空间的时间动态异质性，通过奇异值分解（SVD）将二者解耦，分别采用指数移动平均（EMA）预测与直接复用策略。该方法在FLUX.1-dev上实现了5.55倍加速且ImageReward提升2.267%，但在视频生成任务中VBench分数低于部分基线，其静态SVD基线对分布外输入的鲁棒性存疑。

】

---

【From Sketch to Fresco: Efficient Diffusion Transformer with Progressive Resolution ｜渐进式分辨率扩散Transformer

研究机构：上海交通大学、华南理工大学

作者：Shikang Zheng、Guantao Chen、Lixuan He 等 7 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.07462)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.07462)

> 扩散Transformer（Diffusion Transformer, DiT）在高分辨率生成中面临计算冗余与质量退化的双重瓶颈。现有动态分辨率方法在阶段切换时独立注入噪声，导致去噪轨迹断裂与语义重置，且缺乏对Token收敛状态的感知。Fresco通过构建Token编码统一噪声场与方差引导的渐进式上采样机制，解决了跨阶段一致性问题。该方法在FLUX上实现10.27倍加速且质量优于原模型，但方差阈值静态设定限制了其在极端动态场景下的适应性。

】

---

【Just-in-Time: Training-Free Spatial Acceleration for Diffusion Transformers ｜即时计算：扩散Transformer的空间加速框架

研究机构：电子科技大学

作者：Wenhao Sun、Ji Li、Zhaoqiang Liu

论文原文见 [arXiv](https://arxiv.org/abs/2603.10744)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.10744)

> 扩散Transformer（DiT）推理延迟主要源于自注意力的二次方复杂度与迭代去噪过程，现有加速方法多聚焦于时间步冗余消除或模型压缩，却忽视了生成过程中空间维度的非均匀计算需求。本文提出即时计算（Just-in-Time, JiT）框架，通过动态激活稀疏锚点Token子集并引入确定性微流机制，在无需重训的前提下实现空间域加速。该方法在FLUX.1-dev模型上取得7.07倍加速比，同时保持接近无损的生成质量。其核心贡献在于将ODE求解与动态Token激活结合，但空间冗余消除是否以牺牲时间步精度为代价，论文未给出明确回答。

】

---

【LESA: Learnable Stage-Aware Predictors for Diffusion Model Acceleration ｜阶段感知可学习预测器

研究机构：上海交通大学

作者：Peiliang Cai、Jiacheng Liu、Haowen Xu 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2602.20497)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2602.20497)

> 扩散Transformer（DiT）推理加速的核心矛盾在于，特征缓存虽能利用时间步冗余降低计算量，但固定策略无法适应去噪过程中特征动态的非均匀性，导致高加速比下质量崩塌。现有“缓存-复用”与“缓存-预测”范式均依赖平滑性或静态阈值假设，忽视了高噪声阶段的剧烈震荡与低噪声阶段的精细收敛差异。LESA通过引入阶段感知的多专家架构，利用Kolmogorov–Arnold Network（KAN）学习各阶段特有的非线性时间映射，实现了从启发式规则到数据驱动预测的范式转换。该方法在FLUX.1-dev上以5.00×加速比仅损失1.0%质量，但在训练开销与阶段边界自适应方面仍存在局限。

】

---

【Memory-Efficient Fine-Tuning Diffusion Transformers via Dynamic Patch Sampling and Block Skipping ｜DiT微调内存优化：动态补丁采样与块跳过

研究机构：韩国科学技术院

作者：Sunghyun Park、Jeongho Kim、Hyoungwoo Park 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.20755)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.20755)

> 扩散Transformer（DiT）在个性化微调阶段面临显存瓶颈，阻碍了端侧部署。现有参数高效微调方法虽减少可训练参数，但全网络反向传播仍导致激活值内存激增。本文切入点在于利用去噪时间步的语义特性与DiT块的功能冗余，通过动态调整输入分辨率并跳过非关键块来压缩训练内存。该方法在保持个性化质量的同时将峰值显存降低65.8%，但其在高跳过率下的泛化边界尚待验证。

】

---

【Multi-Patch Global-to-Local Transformer Architecture For Efficient Flow Matching and Diffusion Model ｜多补丁全局到局部扩散Transformer

研究机构：美国罗格斯大学

作者：Quan Dao、Dimitris Metaxas

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_15ced8a1ed7b)

> 扩散Transformer（DiT）在视觉生成中面临训练与推理的双重计算瓶颈，其各层处理相同数量Token的同构设计导致早期块在低分辨率特征上浪费算力。现有稀疏注意力或掩码方法在减少Token时往往牺牲生成质量或引入额外重建开销，而MPDiT通过架构级层级化补丁调度，将全局建模与局部细化解耦。该方法在ImageNet-256上以50%的GFLOPs削减实现了与标准DiT相当的生成质量，但其收益高度依赖特定的补丁层级配置，且在高分辨率外推与动态分辨率场景下的泛化能力尚存疑。

】

---

【One Model, Many Budgets: Elastic Latent Interfaces for Diffusion Transformers ｜弹性潜在接口变换器

研究机构：美国莱斯大学

作者：Moayed Haji-Ali、Willi Menapace、Ivan Skorokhodov 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.12245)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.12245)

> DiT架构将计算量锁定为输入分辨率的固定函数，导致模型在图像不同区域均匀分配算力，忽视了视觉信息分布的不均衡性。现有自适应生成方法要么在推理时无法控制预算，要么依赖复杂的辅助损失与全Token推理，难以实现训练-推理联合的弹性计算分配。本文通过引入可变长度的潜在接口（Latent Interface）及轻量级Read/Write交叉注意力层，解耦了图像尺寸与计算量，使单一模型权重能在推理时通过调整潜在Token数量实现平滑的质量-延迟权衡。该架构在ImageNet-512px上实现了35.3%的FID平均增益，但其大规模从头训练的收益尚未验证，且引导机制存在图像饱和倾向。

】

---

【Pluggable Pruning with Contiguous Layer Distillation for Diffusion Transformers ｜可插拔连续层蒸馏剪枝

研究机构：香港中文大学、中山大学

作者：Jian Ma、Qirong Peng、Xujie Zhu 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2511.16156)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.16156)

> 多模态扩散Transformer（MMDiT）参数量激增导致部署受限，现有剪枝方法缺乏对深层依赖关系的理解且难以灵活配置。PPCL通过线性探针识别连续冗余层区间，并采用非顺序蒸馏打破误差传播链，实现了无需重训的即插即用压缩。该方法在保持生成质量的同时大幅缩减模型规模，但其依赖启发式规则识别层间边界，理论严谨性尚待验证。

】

---

【ResCa: Residual Caching for Diffusion Transformers Acceleration ｜残差缓存加速扩散Transformer

研究机构：中国科学院、中国科学院大学

作者：Haipeng Fang、Yu Li、Fan Tang 等 6 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_aa812e0d03e6)

> 扩散Transformer（DiT）推理加速的核心矛盾在于：挖掘时间步间的特征冗余以跳过重复计算，但静态缓存或简单外推会引入“非更新”或“非自”的去噪方向，导致生成质量随加速比增加而急剧下降。现有方法要么直接复用旧特征（如TeaCache），要么基于历史轨迹外推（如TaylorSeer），均无法在极端加速下保持去噪轨迹的自洽性。ResCa提出“代理去噪”视角，在每个轨迹聚类中仅对一个代理Token执行真实去噪，利用其多阶残差校正其余Token的模拟去噪方向。该方法在FLUX上实现5.51× FLOPs加速且ImageReward保持0.9958，但聚类开销与代理选择的随机性是否影响稳定性，论文未充分验证。

】

---

【ResDiT: Evoking the Intrinsic Resolution Scalability in Diffusion Transformers ｜高分辨率扩散Transformer生成中的位置编码与感受野解耦

研究机构：北京邮电大学、清华大学

作者：Yiyang Ma、Feng Zhou、Xuedan Yin 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.01426)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.01426)

> 预训练扩散Transformer（Diffusion Transformer, DiT）在超出训练分辨率推理时，常因位置编码外推失效导致布局崩塌，且全局注意力范围扩大造成细节模糊。现有免训练方法多依赖低分辨率图像引导，将高分辨率生成异化为超分辨率任务，未能激活模型内在的高分辨率生成能力。ResDiT通过缩放位置编码修正空间布局，并引入重叠补丁局部注意力与频域融合恢复细节，实现单阶段原生高分辨率合成。该方法在3072×3072分辨率下取得了优于两阶段基线的CLIP分数，但4096×4096下的分布偏移问题仍制约其极限性能。

】

---

【Reviving ConvNeXt for Efficient Convolutional Diffusion Models ｜全卷积扩散模型

研究机构：韩国科学技术院

作者：Taesung Kwon、Lorenzo Bianchi、Lennart Wittke 等 8 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.09408)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.09408)

> 扩散Transformer（Diffusion Transformer, DiT）凭借可扩展性成为视觉生成主流，但其二次方注意力复杂度导致训练与推理成本随分辨率呈指数级增长。现有加速方案多聚焦于推理阶段的稀疏化或量化，未能从架构根源消除计算瓶颈，且训练效率与推理效率往往割裂。本文切入点在于重新审视卷积神经网络的局部性偏置与参数效率，提出全卷积扩散模型（Fully Convolutional Diffusion Model, FCDM），以ConvNeXt为骨干替代Transformer块。该架构在保持生成质量竞争力的同时，将计算量降低50%并大幅缩短训练步数，挑战了“Transformer是扩散模型唯一高效路径”的领域共识，但其绝对生成质量尚未超越最新SOTA，且未验证在视频等长序列任务中的适用性。

】

---

【SODA: Sensitivity-Oriented Dynamic Acceleration for Diffusion Transformer ｜敏感度导向的动态加速

研究机构：哈尔滨工业大学

作者：Tong Shao、Yusen Fu、Guoying Sun 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2603.07057)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2603.07057)

> 扩散Transformer（DiT）推理加速面临缓存与剪枝策略固化的困境，现有方法依赖启发式规则，无法捕捉模型内部细粒度的敏感度差异，导致高敏感计算被错误跳过。SODA通过离线建模时间步、层与模块的敏感度误差，利用动态规划优化缓存间隔，并自适应决定剪枝时机与比率，实现了训练-free条件下的全局最优加速调度。该方法在DiT-XL/2上以2.73倍加速比取得2.47的FID，优于ToCa与DuCa，但在视频生成任务中质量仍低于BWCache，其离线建模的通用性边界尚待进一步验证。

】

---

【SRA 2: Variational Autoencoder Self-Representation Alignment for Efficient Diffusion Training ｜变分自编码器自表示对齐

研究机构：浙江大学

作者：Mengmeng Wang、Dengyang Jiang、Liuzhuozheng Li 等 9 人

论文原文见 [arXiv](https://arxiv.org/abs/2601.17830)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2601.17830)

> 扩散Transformer（DiT）训练收敛缓慢，现有加速方法依赖外部编码器或双模型，带来高昂计算开销与领域适配限制。SRA 2 利用潜扩散模型（LDM）第一阶段已离线提取的预训练变分自编码器（VAE）特征作为内置监督信号，通过轻量投影层对齐DiT中间层表示，实现零额外特征提取成本的训练加速。该方法在ImageNet 256×256上显著缩短收敛时间，但绝对生成质量仍低于依赖外部强语义先验的SOTA方法，其效果上限受限于VAE特征的低层纹理属性。

】

---

【TC-Pade: Trajectory-Consistent Pade Approximation for Diffusion Acceleration ｜轨迹一致Padé近似

作者：Shaoxuan He、Benlei Cui、Bukun Huang 等 11 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_f2f454a45605)

> 扩散Transformer（DiT）在20-30步的低步数采样区间内，现有特征缓存方法因时间步间隔增大导致轨迹漂移与质量崩塌。本文指出多项式外推在长间隔下收敛半径受限，且忽略了去噪不同阶段的动态差异，提出基于Padé有理函数近似的残差预测框架。通过轨迹稳定性指标动态门控与步数感知策略，TC-Padé在FLUX.1-dev上实现2.88倍加速且FID损失仅3%。该方法在低步数场景下显著优于现有缓存基线，但其加速比在视频生成任务中相对有限，且对特定硬件环境的依赖未充分披露。

】

---

【Test-time Sparsity for Extreme Fast Action Diffusion ｜测试时稀疏性加速动作扩散

研究机构：清华大学、香港中文大学

作者：Kangye Ji、Yuan Meng、Jianbo Zhou 等 6 人

论文原文见 [arXiv](https://arxiv.org/abs/2605.13316)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2605.13316)

> 动作扩散模型因迭代去噪机制导致推理频率仅5-6Hz，远低于机器人实时控制所需的30Hz，而现有基于静态调度的特征缓存方法无法适应开放环境中多轮交互产生的动态稀疏模式。本文切入点在于将剪枝决策从离线固定策略转变为测试时动态预测，并引入跨时间步、跨Rollout迭代的全向特征复用机制。具体做法是设计并行化推理流水线消除非解码器延迟，并通过3D晶格建模组织历史特征以支撑95%稀疏率下的无损加速。该方法在动作扩散领域实现了5倍加速与47.5Hz频率，但其依赖轻量级剪枝器训练，且仅在特定机器人操作基准上验证，向通用视觉生成迁移的可行性存疑。

】

---

【Trainable Log-linear Sparse Attention for Efficient Diffusion Transformers ｜对数线性稀疏注意力

研究机构：新加坡南洋理工大学、北京大学

作者：Yifan Zhou、Zeqi Xiao、Tianyi Wei 等 5 人

论文原文见 [arXiv](https://arxiv.org/abs/2512.16615)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2512.16615)

> 扩散Transformer（DiT）在高分辨率视觉生成中面临自注意力二次方复杂度的瓶颈，阻碍了长序列的扩展。现有Top-K稀疏注意力方法因单层级设计导致选择阶段仍为$O(N^2)$，且需随序列增长增大$K$以维持质量。本文提出LLSA，通过层级化Top-K选择与层级KV增强机制，将复杂度降至$O(N \log N)$。该方法在像素空间DiT训练中实现了6.09倍的训练加速，但其在潜空间模型及视频生成中的泛化能力尚待验证。

】

---

【UltraFlux: Data-Model Co-Design for High-quality Native 4K Text-to-Image Generation across Diverse Aspect Ratios ｜UltraFlux：面向原生4K多宽高比生成的数据-模型协同设计

作者：Tian Ye、Song Fei、Lei Zhu

论文原文见 [arXiv](https://arxiv.org/abs/2511.18050)

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2511.18050)

> 导读 扩散Transformer（Diffusion Transformer, DiT）在1K分辨率下已实现高质量文本到图像生成，但扩展至原生4K并支持多样宽高比（Aspect Ratio, AR）时，位置编码、变分自编码器（Variational Autoencoder, VAE）压缩与优化目标三者耦合失效，导致生成质量显著退化。现有训练-free缩放或轻量级适配器方法仅解决单一瓶颈，无法应对4K下多因素交互的复杂性。本文提出UltraFlux，通过构建1M规模多AR数据集MultiAspect-4K-1M，并协同设计共振2D旋转位置编码、SNR感知Huber小波损失及阶段性美学课程学习，实现原生4K多AR生成。该方法在AestheticEval@4096基准上FID达143.11，优于Sana等基线，但其性能增益中数据规模与算法改进的贡献占比尚存争议。

】

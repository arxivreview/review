# CVPR2026最新论文 ｜Socratic-Geo: Synthetic Data Generation and Cross-Modal Geometric Reasoning via Multi-Agent Interaction ｜程序化几何数据合成与多智能体协同推理

研究机构：阿里巴巴集团、上海交通大学

作者：Zhengbo Jiao、Zifan Zhang、Shaobo Wang 等 7 人

分析报告见 [ArxivReview](https://www.arxivreview.com/papers/conf_d027662ae91c)

> 几何推理面临高质量图文对极度稀缺的瓶颈，现有自动化方法要么被动适配图像，要么盲目随机生成，导致数据合成与模型学习脱节。Socratic-Geo 通过多智能体交互，将 Solver 的失败路径转化为 Teacher 的程序化绘图指令，实现目标驱动的数据闭环。该框架利用 Python 代码确保几何公理一致性，并蒸馏生成器能力。其价值在于以极少种子数据实现推理与生成的双重提升，但依赖代码执行环境，泛化至非结构化视觉任务的能力存疑。

## 研究背景

几何推理要求视觉感知与逻辑演绎的精确对齐，其核心难点在于图像与文本必须满足公理级一致性。传统多模态大模型（MLLMs）在处理此类任务时，常因训练数据中缺乏显式的几何结构监督，导致模型无法区分语义相似但几何错误的图形。这种“视觉-逻辑”断层使得模型在复杂空间关系推理中频繁失效，而人工标注几何数据成本高昂且难以保证多样性。

主流自动化数据合成方法存在根本局限：基于图像的文本增强仅能优化描述，无法重构几何结构；符号驱动随机生成虽保证正确性，但采用盲目探索策略，效率低下；LLM 驱动增强虽能产生多样内容，但作为黑盒放大器，缺乏细粒度控制且继承模型偏差。更关键的是，这些范式均产生静态、单向的数据集，数据生成独立于模型训练，错失了迭代改进的机会。Socratic-Geo 的切入点在于将数据合成嵌入学习闭环，通过 Solver 的失败诊断驱动 Teacher 进行目标导向的程序化生成，从而解决数据稀缺与训练有效性之间的矛盾。

## 核心方法

### 方法参照系

本文问题置于“智能体生成框架”路线下。标准流程通常依赖外部工具检索或静态模板生成数据，缺乏对学习者当前能力状态的动态响应。本文的关键差异在于引入“程序化控制”，将几何图像生成转化为可执行、可验证的代码修改过程，而非像素级直接生成。

### 目标驱动的程序化合成

Teacher 模块的核心创新在于利用 Python 代码作为几何结构的中间表征，替代模糊的文本提示。当 Solver 在 $k$ 次尝试中全部失败（$\sum_{i=1}^k R_i = 0$）时，Teacher 触发诊断流程，分析错误路径并修改底层几何代码。这一设计解决了纯文本生成无法保证几何公理一致性的问题，确保生成的图像在结构上严格符合题目约束。代码修改后的执行结果 $(I', q', a')$ 需通过 Reflect 机制验证可解性，即 Teacher 自身求解结果需与参考解一致，且几何有效性检查通过。该机制将“盲目生成-事后过滤”转变为“诊断-修改-验证”的主动构造过程，显著提升了数据纯度。

### 多智能体协同优化与知识蒸馏

Solver 采用 Group Relative Policy Optimization (GRPO) 进行强化学习，利用可验证奖励消除价值网络开销。其优化目标定义为：

$$
L_{GRPO}(\theta_S) = -E_{(I,q)\sim C_t} \sum_{a \in Z^+ \cup Z^-} \left[ \frac{1}{|a|} \sum_{t=1}^{|a|} (\hat{A}_t(a) + \beta(r_t - 1)) \log \pi_{\theta_S}(a_t | I, q, a_{<t}) \right]
$$

其中 $Z^+$ 和 $Z^-$ 分别为正负样本集，$\hat{A}_t(a)$ 为组内归一化优势值。当所有尝试失败时，Teacher 的参考解 $a_{ref}$ 被注入为正样本，确保 Solver 在完全失败时仍能获得金标准信号。Generator 作为协同副产品，独立于核心推理循环，通过监督微调（SFT）学习 Teacher 生成的“指令-图像”对。其 SFT 损失为：

$$
L_{SFT}(\phi) = -E_{(d, I') \sim D} \log p_\phi(I' | d)
$$

这一设计将 Teacher 的符号化、规则化绘图智能蒸馏至扩散模型权重中，使 Generator 能够映射结构化指令到几何精确的图像，而非依赖模糊提示。

## 实验评估

实验在六个几何推理基准（MathVerse, MathVista, MathVision, GeoQA, GeomVerse, WeMath）及 GenExam-Math 生成基准上进行。基线覆盖 Socratic-Zero、R-COT、PGPS 等主流方法，但缺失 UniGRPO、AlphaGRPO 等通用强化学习基线，限制了横向对比的广度。

| 方法 | GenExam-Math (Relaxed Score) | Solver 平均准确率 (%) |
| :--- | :--- | :--- |
| Socratic-Generator | 42.4 | - |
| Seedream-4.0 | 39.8 | - |
| Gemini-2.5-Flash-Image | 43.1 | - |
| Socratic-Solver | - | 49.11 |
| Zero-Shot Baseline | - | 44.98 |

Socratic-Generator 在 GenExam-Math 上取得 42.4 分，超越 Seedream-4.0 的 39.8 分，接近 Gemini-2.5-Flash-Image 的 43.1 分，确立开源模型 SOTA。Socratic-Solver 平均准确率达 49.11%，较 Zero-Shot 基线提升 4.13 个百分点，且仅使用四分之一的训练样本。

消融实验显示，Reflect 与 RePI 双验证机制对数据纯度至关重要。移除 RePI 后，几何结构错误率显著上升，导致 Solver 在复杂空间关系任务上性能下降。Generator 的 SFT 训练依赖 Teacher 生成的指令质量，当指令描述过于简略时，生成图像的细节保真度降低，表明程序化指令的粒度直接影响蒸馏效果。

评估边界方面，论文未报告计算效率指标（如生成延迟、GPU 显存占用），且代码执行环境依赖 Python 库，限制了部署灵活性。可复现性受限于未公开完整代码与超参数配置，尤其是 Teacher 的提示工程细节未完全披露，可能影响结果复现。

## 关联研究分析

从问题动机看，Socratic-Geo 与 ThinkMorph 同属交错推理机制，但 ThinkMorph 侧重视觉 Token 的动态调度以解决空间关系错位，而 Socratic-Geo 侧重代码逻辑验证以解决公理一致性。ThinkMorph 的中间状态是像素级的视觉特征，而 Socratic-Geo 的中间状态是符号级的几何代码。这一差异源于任务特性：几何推理要求严格的逻辑推导，代码表征比视觉特征更能捕捉约束关系。然而，代码表征的离散性可能限制其在连续空间任务（如自由形态生成）中的适用性，论文未探索这一边界。

从方法设计看，Socratic-Geo 与 ToolArtist 同属智能体框架，但 ToolArtist 依赖外部工具检索以突破知识截止，而 Socratic-Geo 依赖内部代码执行以实现结构控制。ToolArtist 的优势在于开放世界知识获取，Socratic-Geo 的优势在于结构化数据的精确生成。Socratic-Geo 的“内部代码修改”策略在数据充足时是否仍有增益，论文未给出回答。若训练数据已包含大量高质量几何样本，程序化合成的边际收益可能递减，而 ToolArtist 的检索策略在长尾知识场景下更具优势。

## 总结

Socratic-Geo 旨在解决几何推理中数据稀缺与模型学习脱节的核心矛盾。其切入点在于利用 Solver 的失败路径驱动 Teacher 进行程序化代码修改，通过 Python 执行确保几何公理一致性，从而生成高质量训练数据。框架通过 GRPO 优化 Solver 推理能力，并通过 SFT 蒸馏 Generator 生成能力，实现了推理与生成的协同提升。实验证明，仅用 108 个种子问题，Socratic-Solver 在六个基准上平均准确率提升 4.13 个百分点，Socratic-Generator 在 GenExam-Math 上达到 42.4 分，超越 Seedream-4.0。然而，该方法依赖代码执行环境，且 Generator 的蒸馏效果受限于 Teacher 指令的粒度。当训练数据规模扩大至百万级时，程序化合成的效率优势是否仍能维持，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/conf_d027662ae91c)
# HuggingFace最新推荐论文 ｜OvisOCR3 Technical Report ｜OvisOCR3：面向多任务统一与模型压缩的紧凑视觉语言模型

研究机构：阿里巴巴集团

作者：Yu Xia、Yinglun Li、Yuhui Chen 等 15 人

论文原文见 [arXiv](https://arxiv.org/abs/2610.33066)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2610.33066)

> 文档信息抽取（Document Information Extraction, DIE）旨在从非结构化文档中自动提取结构化数据，其核心价值在于连接数字文档与机器智能。现有端到端视觉语言模型（Vision-Language Model, VLM）虽在通用解析上优于传统光学字符识别（Optical Character Recognition, OCR）流水线，但在多任务统一时面临响应长度差异导致的监督失衡，且大参数量模型难以在垂直领域实现低成本部署。OvisOCR3 通过域平衡中期训练、多教师在线策略蒸馏（Multi-teacher On-Policy Distillation, MOPD）与混合任务强化学习（Mixed-Task Reinforcement Learning, MixRL），在 0.8B 参数规模下统一了文档解析、通用 OCR、关键信息抽取（Key Information Extraction, KIE）、文档图表描述与跨页表格重建。该工作证明了紧凑模型通过精细的数据工程与后训练策略，可在多任务间实现专家级性能，但多任务负迁移风险与跨页结构的全局一致性验证仍需进一步评估。

## 研究背景

当模型面对包含文本、表格、公式及跨页结构的复杂文档时，单一模态或单一任务范式难以同时满足高精度识别与结构化生成的需求。传统 OCR 流水线通过多阶段处理实现文本转录，但误差累积与视觉线索丢失使其在复杂布局下极其脆弱。端到端 VLM 通过像素到文本的直接映射消除了误差传播，但不同 OCR 任务在响应长度与正确性定义上存在显著差异：全页重建包含数千个 token，而字段抽取仅需数个 token。在 token 平均损失下，样本数量的平衡无法保证监督信号的平衡，导致长响应任务主导梯度更新，短响应任务欠拟合。

当前领域处于从“通用识别”向“垂直领域高精度抽取”过渡的阶段。主流路线依赖大参数量模型（如 4B 至 241B）通过海量数据预训练实现多任务泛化，但计算成本高昂，难以在资源受限场景部署。小参数量模型（如 0.8B）虽具备部署优势，但在多任务干扰下性能衰减严重。OvisOCR3 的切入点在于：通过双分支损失归一化平衡不同任务的监督强度，并利用多教师蒸馏与混合强化学习，在极小参数规模下注入领域专家知识，解决多任务监督失衡与精度瓶颈。

## 核心方法

### 方法参照系：多任务统一与监督失衡

OvisOCR3 属于端到端文档解析与关键信息抽取的融合路线。其标准流程为：输入文档图像与任务指令，通过视觉编码器提取特征，解码器自回归生成结构化输出（如 JSON、Markdown、LaTeX）。与单任务模型不同，OvisOCR3 在单一 0.8B 模型中共享参数，通过指令区分任务目标。该流程的关键差异在于：多任务混合训练时，不同任务的响应长度差异导致 token 级监督信号严重失衡，传统单一损失函数无法有效平衡长文本解析与短字段抽取的学习进度。

### 域平衡中期训练：双分支损失归一化

针对多任务监督失衡问题，OvisOCR3 在中期训练阶段引入双分支损失归一化机制。传统做法采用 token 级平均损失，导致长响应任务（如文档解析）主导梯度。本文并行训练两个分支：token 级归一化分支与样本级归一化分支。Token 级损失定义为：

$$
L_{\text{token}}(\theta) = -\frac{\sum_{i \in B} \sum_{t \in S_i} \log p_\theta(y_{i,t} \mid x_i, y_{i,<t})}{\sum_{i \in B} |S_i|}
$$

其中 $B$ 为批次内有效样本，$S_i$ 为监督响应位置集合。该公式按总 token 数归一化，保留长文本的细粒度监督。样本级损失则先计算每个样本的平均 token 损失，再对批次内样本求平均：

$$
L_{\text{sample}}(\theta) = -\frac{1}{|B|} \sum_{i \in B} \frac{1}{|S_i|} \sum_{t \in S_i} \log p_\theta(y_{i,t} \mid x_i, y_{i,<t})
$$

该公式确保每个样本对梯度的贡献相等，防止短响应任务被淹没。训练末期融合两分支权重，使模型同时具备长文本解析能力与短字段抽取精度。

### 多教师在线策略蒸馏与混合强化学习

在域平衡训练后，OvisOCR3 通过 MOPD 将五个领域特定 4B 教师模型的专业知识注入共享学生模型。教师模型仅在训练阶段使用，推理时无需额外模型。随后，采用 MixRL 结合领域特定奖励函数进行联合优化。MixRL 的奖励函数针对任务特性设计：文档解析关注结构一致性，KIE 关注字段准确率，跨页表格关注关系 F1。该设计弥补了监督微调在复杂结构约束上的不足，通过强化学习信号直接优化格式遵循与结构对齐，解决了自回归生成中的崩溃现象。

## 实验评估

实验在 OmniDocBench v1.6、PureDocBench、Real5-OmniDocBench 等公开基准及内部基准上进行。基线覆盖通用 VLM（GPT-5, Gemini 3 Pro）与专用 OCR 模型（PaddleOCR-VL, MinerU 2.5 Pro）。OvisOCR3 在 OmniDocBench v1.6 上取得 96.74 的 Overall 分数，略低于同量级 Xiaomi-OCR-0 的 96.83，但显著超越 4B 级 Qianfan-OCR（93.90）与 12B 级 MinerU 2.5 Pro（95.75）。在 PureDocBench 上，OvisOCR3 以 82.31 的 Overall 分数领先所有对比模型，包括 4B 级 WeVisDoc-4B（75.57）与 0.8B 级 OvisOCR2（75.10）。

| 模型 | 参数量 | OmniDocBench v1.6 Overall | PureDocBench Overall | Real5-OmniDocBench Overall |
| :--- | :--- | :--- | :--- | :--- |
| OvisOCR3 | 0.8B | 96.74 | 82.31 | 93.63 |
| Xiaomi-OCR-0 | 0.8B | 96.83 | 74.60 | 92.73 |
| OvisOCR2 | 0.8B | 96.58 | 75.10 | 92.29 |
| Qianfan-OCR | 4B | 93.90 | - | - |
| MinerU 2.5 Pro | 1.2B | 95.75 | 70.07 | 88.94 |

消融实验显示，双分支损失归一化显著改善了短响应任务（如 KIE）的性能，避免了 token 级损失下的欠拟合。MOPD 与 MixRL 的引入使模型在跨页表格重建（CrossTabBench Relation F1）与文档图表描述（DocFigCapBench Localization F1）上达到 SOTA。评估边界方面，论文未报告置信区间，且未对比同参数量级最新 SOTA 在多任务干扰下的具体衰减曲线。可复现性方面，模型权重已开源，但训练超参数与奖励函数细节未完全公开。

## 关联研究分析

从问题动机看，OvisOCR3 与 Qianfan-OCR 均致力于统一文档解析与理解任务，但 Qianfan-OCR 采用 4B 参数规模并通过 Layout-as-Thought 机制显式生成布局表示，而 OvisOCR3 在 0.8B 规模下通过隐式指令遵循与蒸馏实现多任务统一。Qianfan-OCR 的显式布局输出提供了可解释性，但增加了推理延迟；OvisOCR3 的紧凑架构牺牲了显式中间结果，换取了部署效率。查询侧增强在数据充足时是否仍有增益，论文未给出回答。

从方法设计看，OvisOCR3 与 Logics-Parsing 均采用强化学习优化结构一致性，但 Logics-Parsing 针对单任务（页面解析）设计全局奖励，而 OvisOCR3 的 MixRL 需处理多任务奖励冲突。Logics-Parsing 的 SFT-then-RL 范式在单任务上信号明确，但 OvisOCR3 面临多任务奖励函数设计的复杂性。双分支损失归一化是否比简单的数据重采样更能有效解决多任务监督失衡，论文未提供直接对比实验。

## 总结

OvisOCR3 解决了紧凑模型在多任务 OCR 中因响应长度差异导致的监督失衡与精度瓶颈问题。通过双分支损失归一化平衡监督信号，结合多教师蒸馏与混合强化学习注入领域知识，该模型在 0.8B 参数规模下实现了跨任务专家级性能。在 OmniDocBench v1.6 上取得 96.74 的 Overall 分数，在 PureDocBench 上以 82.31 领先所有对比模型。其边界在于多任务负迁移风险未被充分量化，且跨页结构的全局一致性验证依赖两阶段流水线而非端到端全局优化。当任务数量进一步增加或任务间冲突加剧时，双分支损失归一化与多教师蒸馏的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2610.33066)
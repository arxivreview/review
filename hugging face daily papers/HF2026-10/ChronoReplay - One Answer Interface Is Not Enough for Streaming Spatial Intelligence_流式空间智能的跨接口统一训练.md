# HuggingFace最新推荐论文 ｜ChronoReplay: One Answer Interface Is Not Enough for Streaming Spatial Intelligence ｜流式空间智能的跨接口统一训练

作者：Yihao Hu、Yitong Lin、Pan Wang 等 11 人

论文原文见 [arXiv](https://arxiv.org/abs/2610.34283)

深度分析原文见 [ArxivReview](https://www.arxivreview.com/papers/arxiv_2610.34283)

> 视觉-语言模型（Vision-Language Models, VLMs）在流式视频空间推理中面临分类、度量与时间查询的异构监督冲突，单一接口训练易导致其他空间读数性能退化。现有方法多依赖单接口监督或架构修改，未能解决跨接口迁移失败的问题。ChronoReplay 通过因果回放构建有序剧集，并实施家族平衡学习，在统一骨干下实现跨接口性能提升。该工作为流式空间推理提供了有效的训练策略，但其隐式状态轨迹是否足以替代显式几何约束仍存疑。

## 研究背景

当家庭机器人跟随用户穿过公寓时，它需要回答“镜子在左还是右”“沙发距离多远”“何时经过植物”等问题。这要求模型在因果历史中关联物体、累积观察者运动，并在变化的参考系中恢复空间关系。流式空间基准将这三类查询置于同一因果历史中，但现有训练配方通常针对单一答案格式，导致模型在分类、度量和时间查询之间出现性能割裂。

空间推理的核心难点在于几何接地与视角一致性。早期研究如 CLEVR 和 VSR 奠定了合成数据基准，但局限于静态二维/三维几何关系。随着评估范式转向多视角动态交互，MindCube 和 VSI-Bench 引入了认知映射与视角采样概念。然而，现有方法在表示质量、适应效率与计算成本之间做出不同取舍，形成几何接地、多视角对齐与具身闭环多元并存的格局。ChronoReplay 针对流式视频空间推理中的“接口锁定”（Interface Lock-in）问题，即单一监督导致其他空间读数性能下降，提出通过异构监督平衡抑制特定接口的过拟合。

## 核心方法

### 方法参照系

ChronoReplay 属于工具增强与智能体推理路线中的训练策略优化。与 SpatialLadder 的渐进训练不同，ChronoReplay 强调基于因果前缀的剧集回放，强调时间起源对齐。其核心差异在于：SpatialLadder 依赖大规模多模态数据集，而 ChronoReplay 通过因果回放构建有序剧集，并实施家族平衡学习，显式平衡分类/数值（Preservation）与轨迹/时间（Trajectory）两类风险权重。

### 因果回放构建

ChronoReplay 的第一阶段是因果回放构建。该阶段将异构空间监督作为有序剧集回放，保留源原生目标，并平衡监督家族。具体而言，每个目标保持其原生格式（选项语义、单位和精度或时间戳），每个剧集按时间顺序排列。这一设计解决了此前方法中几何令牌被忽略的问题，通过冻结几何分支和令牌自适应接地，使几何证据成为可操作的约束。

$$
E_i = (c_{ij}, q_{ij}, y_{ij}, \kappa_{ij})_{j=1}^{m_i}, \quad c_{ij} \preceq c_{i,j+1}
$$

该公式表示一个剧集 $E_i$，其中 $c_{ij}$ 是第 $j$ 轮的合法因果前缀，$q_{ij}$ 是空间查询，$\kappa_{ij}$ 标识其原生接口，$y_{ij}$ 是在该前沿有效的目标。因果前缀包含关系 $\preceq$ 确保了每个目标与其有效前缀的绑定。

### 家族平衡学习

ChronoReplay 的第二阶段是家族平衡学习。该阶段归一化单轮保留和度量-时间轨迹风险，然后控制它们对共享参数的相对贡献。这一设计解决了此前方法中几何令牌被忽略的问题，通过冻结几何分支和令牌自适应接地，使几何证据成为可操作的约束。

$$
L_{\text{replay}} = (1 - \lambda) L_P + \lambda L_T, \quad \lambda = \frac{\alpha}{1 + \alpha}
$$

该公式表示 ChronoReplay 的组合风险，其中 $L_P$ 是保留家族风险，$L_T$ 是轨迹家族风险，$\alpha$ 是轨迹损失质量相对于保留的比例。在主要实验中，$\alpha = 0.5$，轨迹接收总质量的 $1/3$，保留接收 $2/3$，分类和数值目标平分。

## 实验评估

### 实验设置与主结果

ChronoReplay 在 OVO-S-Bench、OST-Bench 和 UCS-Bench 上评估，所有检查点从相同的官方 Qwen3-VL-8B-Instruct 修订版开始。ChronoReplay 在 33,180 序列保留家族和 6,381 集轨迹家族上训练语言模型和视觉合并器（视觉编码器冻结），$\alpha = 0.5$。

| 方法 | OVO-S (%) | OST (%) | UCS (%) | 平均 (%) |
| --- | --- | --- | --- | --- |
| Official base | 48.98 | 50.52 | 45.33 | 48.28 |
| ChronoReplay | 53.89 | 63.93 | 52.77 | 56.86 |

ChronoReplay 在 OST-Bench 上提升 13.41 点，在 UCS-Bench 上提升 7.44 点，在 OVO-S-Bench 上提升 4.91 点。这些提升在相同的观察访问下实现，证明了 ChronoReplay 在跨接口迁移上的有效性。

### 消融与设计决策验证

ChronoReplay 的消融实验验证了因果回放和家族平衡学习的关键作用。单家族训练显示不均匀的跨读数迁移，而完整的 ChronoReplay 提供了最高的三基准平均。

| 训练 | OVO-S (%) | OST (%) | UCS (%) | 平均 (%) |
| --- | --- | --- | --- | --- |
| CATEGORICAL-ONLY | 58.03 | 47.48 | 46.72 | 50.74 |
| TRAJECTORY-ONLY | 52.03 | 51.03 | 49.22 | 50.76 |
| ChronoReplay | 53.89 | 63.93 | 52.77 | 56.86 |

CATEGORICAL-ONLY 在 OVO-S 上达到 58.03，但将 OST 降低到 47.48；TRAJECTORY-ONLY 在 OST 上几乎持平于 51.03。完整的 ChronoReplay 模型达到 53.89/63.93/52.77，三基准平均为 56.86，高于两个单家族变体的 50.74 和 50.76。

### 评估边界与可复现性

ChronoReplay 的评估协议在流式因果访问下固定观察访问，但自适应帧选择作为推理时策略单独应用。代码和模型在 GitHub 和 Hugging Face 上公开，超参数和 GPU 配置在附录中详细列出。

## 关联研究分析

从问题动机看，ChronoReplay 与 GeoWeaver 都旨在解决 VLMs 的空间幻觉问题，但 GeoWeaver 通过显式几何接地抑制幻觉，而 ChronoReplay 通过异构监督平衡抑制特定接口的过拟合。GeoWeaver 在 VSI-Bench 上达到 57.9%，而 ChronoReplay 在 OST-Bench 上达到 63.93%。两者在复杂三维任务上表现鲁棒，但 GeoWeaver 依赖显式几何证据，ChronoReplay 依赖隐式状态轨迹。

从方法设计看，ChronoReplay 与 SpatialLadder 都关注空间推理训练，但 SpatialLadder 依赖渐进训练，增加了训练复杂度，而 ChronoReplay 通过因果回放构建有序剧集，强调时间起源对齐。SpatialLadder 在效率上占优，但 ChronoReplay 在跨接口迁移上表现更优。查询侧增强在数据充足时是否仍有增益，论文未给出回答。

## 总结

ChronoReplay 针对流式视频空间推理中的接口锁定问题，通过因果回放和家族平衡学习，在统一骨干下实现跨接口性能提升。该工作在 OST-Bench 上提升 13.41 点，在 UCS-Bench 上提升 7.44 点，证明了其在跨接口迁移上的有效性。然而，ChronoReplay 的隐式状态轨迹是否足以替代显式几何约束仍存疑，当支持集增大到 5-shot 时，查询侧增强的边际收益是否递减，论文未给出回答。

以上为节选，完整内容见[ArxivReview](https://www.arxivreview.com/papers/arxiv_2610.34283)